import asyncio
import json
import re
import uuid
import hashlib
from typing import Any, Dict, List, Optional, Tuple
from dataclasses import dataclass, field

import networkx as nx

from agents.memo_structure import Sub_memo_layer, MemoStructure
from eval_envs.base_envs import Basic_Recorder
from utils.hire_agent import Agent, Embedding
from langchain_chroma import Chroma


# ----------------------------- Utilities ---------------------------------


def _normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def _truncate(text: Optional[str], n: int = 600) -> Optional[str]:
    if text is None:
        return None
    t = str(text)
    return t if len(t) <= n else t[: n - 3] + "..."


def _clean_list_of_dicts(
    items: List[Dict[str, Any]], drop_none: bool = True, truncate_keys: Optional[List[str]] = None
) -> List[Dict[str, Any]]:
    truncate_keys = truncate_keys or []
    cleaned = []
    for it in items:
        c = {}
        for k, v in it.items():
            if drop_none and (v is None or v == "" or v == [] or v == {}):
                continue
            if isinstance(v, str) and k in truncate_keys:
                c[k] = _truncate(v, 600)
            else:
                c[k] = v
        if c:
            cleaned.append(c)
    return cleaned


def _extract_map_area(long_term_context: str) -> Tuple[int, int]:
    if not long_term_context:
        return 0, 0
    lines = long_term_context.splitlines()
    map_started = False
    map_lines: List[str] = []
    for line in lines:
        if map_started:
            if re.search(r"St:\d", line) or "HP:" in line:
                break
            else:
                map_lines.append(line.rstrip("\n"))
        if line.strip().lower().startswith("map:"):
            map_started = True
    if not map_lines:
        return 0, 0
    height = len(map_lines)
    width = max(len(l) for l in map_lines) if map_lines else 0
    return width, height


def _extract_position(long_term_context: str) -> Optional[Tuple[int, int]]:
    if not long_term_context:
        return None
    cursor_match = re.search(r"\(x\s*=\s*(\d+),\s*y\s*=\s*(\d+)\)", long_term_context)
    if cursor_match:
        return int(cursor_match.group(1)), int(cursor_match.group(2))
    return None


def _extract_stats_line(long_term_context: str) -> str:
    if not long_term_context:
        return ""
    for line in reversed(long_term_context.splitlines()):
        if "HP:" in line:
            return line.strip()
    return ""


def _extract_action_set(action_dict: Dict[str, str]) -> List[str]:
    if not action_dict:
        return []
    return sorted(set(action_dict.keys()))


def _parse_role_race_alignment(long_term_context: str) -> Dict[str, Optional[str]]:
    # Example greeting: "You are a chaotic female human Monk."
    line = ""
    for l in long_term_context.splitlines():
        if "welcome to nethack" in l.lower() or "you are a" in l.lower():
            line = l
            break
    ali = None
    race = None
    role = None
    if line:
        # alignment
        m = re.search(r"\b(chaotic|neutral|lawful)\b", line, re.IGNORECASE)
        if m:
            ali = m.group(1).lower()
        # race
        m2 = re.search(r"\b(human|elf|dwarf|gnome|orc|gnomish)\b", line, re.IGNORECASE)
        if m2:
            race = m2.group(1).lower()
            race = "gnome" if race == "gnomish" else race
        # role: last capitalized word at end or after race
        m3 = re.search(
            r"\b(human|elf|dwarf|gnome|orc|gnomish)\b\s+([A-Za-z\-]+)\.?$",
            line,
            re.IGNORECASE,
        )
        if m3:
            role = m3.group(2).lower()
        else:
            m4 = re.search(r"\b([A-Za-z\-]+)\.?$", line)
            if m4:
                role = m4.group(1).lower()

    # Fallback role from cursor section
    cursor_section = []
    capture_cursor = False
    for l in long_term_context.splitlines():
        if l.strip().lower().startswith("cursor:"):
            capture_cursor = True
            continue
        if capture_cursor:
            cursor_section.append(l.strip())
            if l.strip() == "":
                break
    cursor_text = " ".join(cursor_section).lower()
    mcur = re.search(r"yourself a ([a-z\-]+)", cursor_text)
    if mcur and not role:
        role = mcur.group(1)

    return {"role": role, "race": race, "alignment": ali}


_CANONICAL_ENTITIES = {
    "bars": "wall",
    "wall": "wall",
    "walls": "wall",
    "door": "door",
    "doors": "door",
    "closed door": "door",
    "open door": "door",
    "boulder": "boulder",
    "boulders": "boulder",
    "fountain": "fountain",
    "fountains": "fountain",
    "altar": "altar",
    "altars": "altar",
    "sink": "sink",
    "sinks": "sink",
    "trap": "trap",
    "traps": "trap",
    "stairs up": "stairs_up",
    "stairs down": "stairs_down",
    "staircase up": "stairs_up",
    "staircase down": "stairs_down",
}


def _normalize_dir_token(tok: str) -> Optional[str]:
    w = tok.lower()
    dirs = ["north", "east", "south", "west"]
    has = {d: (d in w) for d in dirs}
    if has["north"] and has["east"]:
        return "northeast"
    if has["north"] and has["west"]:
        return "northwest"
    if has["south"] and has["east"]:
        return "southeast"
    if has["south"] and has["west"]:
        return "southwest"
    if has["north"]:
        return "north"
    if has["east"]:
        return "east"
    if has["south"]:
        return "south"
    if has["west"]:
        return "west"
    return None


def _extract_local_topology(long_term_context: str) -> Dict[str, List[str]]:
    """
    Parse the 'language observation' section to infer local directional topology.
    Returns lists of directions for canonical entities.
    """
    if not long_term_context:
        return {
            "walls_at": [],
            "doors_at": [],
            "stairs_up_at": [],
            "stairs_down_at": [],
            "boulder_at": [],
            "fountain_at": [],
            "other": "{}",
        }
    lines = long_term_context.splitlines()
    capturing = False
    section = []
    for line in lines:
        if line.strip().lower().startswith("language observation"):
            capturing = True
            continue
        if line.strip().lower().startswith("cursor:"):
            break
        if capturing:
            section.append(line)

    entity_dirs: Dict[str, set] = {}
    for raw in section:
        low = raw.lower()
        if "stairs up" in low or "staircase up" in low:
            dirs = []
            for t in re.findall(r"([A-Za-z]+)", low):
                norm = _normalize_dir_token(t)
                if norm:
                    dirs.append(norm)
            entity_dirs.setdefault("stairs_up", set()).update(dirs)
        if "stairs down" in low or "staircase down" in low:
            dirs = []
            for t in re.findall(r"([A-Za-z]+)", low):
                norm = _normalize_dir_token(t)
                if norm:
                    dirs.append(norm)
            entity_dirs.setdefault("stairs_down", set()).update(dirs)

        # general entities
        for k, canon in _CANONICAL_ENTITIES.items():
            if k in low:
                dirs = []
                for t in re.findall(r"([A-Za-z]+)", low):
                    norm = _normalize_dir_token(t)
                    if norm:
                        dirs.append(norm)
                if dirs:
                    entity_dirs.setdefault(canon, set()).update(dirs)

    def to_sorted_list(key: str) -> List[str]:
        return sorted(list(entity_dirs.get(key, set())))

    topology = {
        "walls_at": to_sorted_list("wall"),
        "doors_at": to_sorted_list("door"),
        "stairs_up_at": to_sorted_list("stairs_up"),
        "stairs_down_at": to_sorted_list("stairs_down"),
        "boulder_at": to_sorted_list("boulder"),
        "fountain_at": to_sorted_list("fountain"),
    }
    known = {"wall", "door", "stairs_up", "stairs_down", "boulder", "fountain"}
    other = {k: sorted(list(v)) for k, v in entity_dirs.items() if k not in known}
    topology["other"] = json.dumps(other, ensure_ascii=False)
    return topology


def _canonicalize_entities(long_term_context: str) -> List[str]:
    if not long_term_context:
        return []
    section = []
    lines = long_term_context.splitlines()
    capturing = False
    for line in lines:
        if "No  Points     Name" in line:
            break
        if line.strip().lower().startswith("language observation"):
            capturing = True
            continue
        if line.strip().lower().startswith("cursor:"):
            break
        if capturing:
            section.append(line.lower())
    text = " ".join(section)
    ents = set()
    for k, v in _CANONICAL_ENTITIES.items():
        if k in text:
            ents.add(v)
    if re.search(r"\bmonster|monsters|you see a [a-z]+", text):
        ents.add("monster")
    return sorted(ents)


def _normalize_item_name(name: str) -> str:
    # common normalizations for higher-quality retrieval keys
    mapping = {
        "fortune cookies": "fortune cookie",
        "food rations": "food ration",
        "tooled horn": "horn",
        "sprig of wolfsbane": "wolfsbane",
        "cloves of garlic": "garlic",
        "pair of gloves": "gloves",
        "leather gloves": "gloves",
        "robe": "robe",
        "potion of healing": "potion of healing",
        "scroll of identify": "scroll of identify",
        "spellbook of protection": "spellbook of protection",
        "spellbook of identify": "spellbook of identify",
        "fedora": "fedora",
        "fedor": "fedora",
        "potions of extra healing": "potion of extra healing",
        "scrolls of magic mapping": "scroll of magic mapping",
        "hawaiian shirt": "hawaiian shirt",
        "expensive camera": "camera",
        "camera": "camera",
        # melee/ranged common
        "katana": "katana",
        "wakizashi": "wakizashi",
        "yumi": "bow",
        "ya": "arrow",
        "arrows": "arrow",
        "arrow": "arrow",
        "bow": "bow",
    }
    # handle common truncations/typos
    name = name.replace("extrhealing", "extra healing").replace("camer", "camera")
    name = re.sub(r"^\+\s*", "", name)  # strip leading + tokens
    if name in mapping:
        return mapping[name]
    if name.endswith("s") and " of " not in name:
        singular = name[:-1]
        return mapping.get(singular, singular)
    return name


def _simplify_inventory_items(short_term_context: str) -> List[str]:
    if not short_term_context:
        return []
    items: List[str] = []
    for line in short_term_context.splitlines():
        m = re.match(r"^[a-zA-Z]:\s+(.*)$", line.strip())
        if not m:
            continue
        raw = m.group(1).lower()

        # Remove annotations and counts
        raw = re.sub(r"\(.*?\)", "", raw)
        raw = re.sub(r"\b(blessed|uncursed|cursed)\b", "", raw)
        raw = re.sub(r"\b\+\d+\b", "", raw)
        raw = re.sub(r"^\s*\+\s*", "", raw)
        raw = re.sub(r"\b\d+\b", "", raw)

        # Standardize determiners and multiword patterns
        raw = raw.replace("pair of ", "")
        raw = raw.replace("an ", "").replace("a ", "").replace("the ", "")

        # Normalize known weapon-ammo strings
        if "yumi" in raw:
            items.append("bow")
            continue
        # Nethack 'ya' are arrows; sometimes rendered oddly like '+ y'
        if re.search(r"\bya\b", raw) or re.search(r"\b\+\s*y\b", raw) or raw.strip() in {"ya", "y", "+ y"}:
            items.append("arrow")
            continue

        raw = _normalize_space(raw)

        # Prefer item-of-type phrases
        m2 = re.search(r"(wand|ring|potion|scroll|spellbook) of [a-z\- ]+", raw)
        if m2:
            item = _normalize_space(m2.group(0))
        else:
            m3 = re.search(r"([a-z]+ of [a-z\- ]+)", raw)
            if m3:
                item = _normalize_space(m3.group(1))
            else:
                toks = [t for t in re.split(r"[^a-z]+", raw) if t]
                if len(toks) >= 2:
                    item = _normalize_space(" ".join(toks[-2:]))
                elif toks:
                    item = toks[-1]
                else:
                    continue

        item = _normalize_item_name(item)
        # Drop stray single letters and plus signs
        if len(item) == 1 and not item.isalpha():
            continue
        if len(item) == 1 and item.isalpha() and item not in {"y"}:
            continue
        if item == "y":
            item = "arrow"

        items.append(item)

    seen = set()
    out = []
    for it in items:
        if it not in seen and it:
            seen.add(it)
            out.append(it)
    return out[:12]


# ----------------- ASCII map parsing and neighbor semantics ----------------


_DIRS = {
    "north": (0, -1),
    "northeast": (1, -1),
    "east": (1, 0),
    "southeast": (1, 1),
    "south": (0, 1),
    "southwest": (-1, 1),
    "west": (-1, 0),
    "northwest": (-1, -1),
}

_DIR_CODES = {
    "north": "N",
    "northeast": "NE",
    "east": "E",
    "southeast": "SE",
    "south": "S",
    "southwest": "SW",
    "west": "W",
    "northwest": "NW",
}


def _sign(v: int) -> int:
    return 0 if v == 0 else (1 if v > 0 else -1)


def _vector_to_dir(dx: int, dy: int) -> Optional[str]:
    dx = _sign(dx)
    dy = _sign(dy)
    for d, (vx, vy) in _DIRS.items():
        if vx == dx and vy == dy:
            return d
    return None


def _is_passable_char(ch: str) -> bool:
    # Treat '.' and '#' as traversable floors/corridors; '<' and '>' as traversable objectives.
    if ch in {".", "#", "<", ">"}:
        return True
    return False


def _is_hazard_char(ch: str) -> bool:
    # Hazard-like tiles we avoid by default
    return ch in {"`", "}", "~", "^", "L"}


def _entity_from_char(ch: str) -> Optional[str]:
    if ch == "{":
        return "fountain"
    if ch == "<":
        return "stairs_up"
    if ch == ">":
        return "stairs_down"
    if ch == "#":
        # in our semantics, '#' is passable corridor; not a wall entity
        return None
    return None


def _parse_ascii_map(long_term_context: str) -> Dict[str, Any]:
    if not long_term_context:
        return {"grid": [], "width": 0, "height": 0, "hero_xy": None, "neighbors": {}}
    lines = long_term_context.splitlines()
    map_started = False
    map_lines: List[str] = []
    for line in lines:
        if map_started:
            if "HP:" in line or re.search(r"St:\d", line):
                break
            map_lines.append(line.rstrip("\n"))
        if line.strip().lower().startswith("map:"):
            map_started = True
    if not map_lines:
        return {"grid": [], "width": 0, "height": 0, "hero_xy": None, "neighbors": {}}
    width = max(len(l) for l in map_lines)
    height = len(map_lines)
    grid = [l.ljust(width) for l in map_lines]
    pos = _extract_position(long_term_context)
    hero_xy = pos if pos else None

    # Robust calibration: check 3x3 around reported pos, then fallback scan
    def find_at_sign(grid_: List[str]) -> List[Tuple[int, int]]:
        coords = []
        for yy, row in enumerate(grid_):
            for xx, ch in enumerate(row):
                if ch == "@":
                    coords.append((xx, yy))
        return coords

    if hero_xy:
        hx, hy = hero_xy
        found = None
        # Local 3x3 search
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                nx_, ny_ = hx + dx, hy + dy
                if 0 <= ny_ < height and 0 <= nx_ < width and grid[ny_][nx_] == "@":
                    found = (nx_, ny_)
                    break
            if found:
                break
        if found:
            hero_xy = found
        else:
            # Global scan; choose nearest to reported
            at_positions = find_at_sign(grid)
            if at_positions:
                if len(at_positions) == 1:
                    hero_xy = at_positions[0]
                else:
                    hx0, hy0 = hx, hy
                    hero_xy = min(at_positions, key=lambda p: abs(p[0] - hx0) + abs(p[1] - hy0))
            else:
                hero_xy = None
    else:
        # No reported cursor, try global scan
        at_positions = [(xx, yy) for yy, row in enumerate(grid) for xx, ch in enumerate(row) if ch == "@"]
        hero_xy = at_positions[0] if at_positions else None

    neighbors: Dict[str, str] = {}
    if hero_xy:
        hx, hy = hero_xy
        for d, (dx, dy) in _DIRS.items():
            nx_ = hx + dx
            ny_ = hy + dy
            if 0 <= ny_ < height and 0 <= nx_ < width:
                ch = grid[ny_][nx_]
            else:
                ch = " "  # out of bounds
            neighbors[d] = ch
    return {"grid": grid, "width": width, "height": height, "hero_xy": hero_xy, "neighbors": neighbors}


def _neighbors_signature(neighbors: Dict[str, str]) -> str:
    if not neighbors:
        return ""
    ordered = ["north", "northeast", "east", "southeast", "south", "southwest", "west", "northwest"]
    parts = []
    for d in ordered:
        ch = neighbors.get(d, " ")
        code = _DIR_CODES[d]
        parts.append(f"{code}:{ch}")
    return "; ".join(parts)


def _safe_json_dumps(data: Any) -> str:
    try:
        return json.dumps(data, ensure_ascii=False)
    except Exception:
        return str(data)


def _get_default_agent(system_prompt: str, schema: Optional[Dict[str, Any]] = None) -> Agent:
    return Agent(model="gpt-4o-mini", system_prompt=system_prompt, output_schema=schema)


def _suggest_first_moves(
    actions: List[str],
    topology: Dict[str, List[str]],
    map_neighbors: Optional[Dict[str, str]] = None,
    passable_dirs: Optional[List[str]] = None,
    goal_text: str = "",
    hazard_dirs: Optional[List[str]] = None,
    nearest_objective_step: Optional[str] = None,
) -> Dict[str, Any]:
    one_step_dirs = {"north", "northeast", "east", "southeast", "south", "southwest", "west", "northwest"}
    allowed = [a for a in (actions or []) if a in one_step_dirs]

    hazard_dirs = hazard_dirs or []
    passable_dirs = passable_dirs or []
    prioritized: List[str] = []
    blocked_map = set()
    passable_map = set()

    # Map-based passability is primary
    if map_neighbors:
        for d in allowed:
            ch = map_neighbors.get(d, " ")
            if _is_passable_char(ch):
                passable_map.add(d)
            else:
                blocked_map.add(d)

    # If no map info, fallback to passable_dirs
    if not passable_map and passable_dirs:
        passable_map = set(passable_dirs)
    # Derive safe vs hazardous
    hazard_set = set(hazard_dirs)
    safe_passable = [d for d in allowed if d in passable_map and d not in hazard_set]
    hazardous_passable = [d for d in allowed if d in passable_map and d in hazard_set]

    # Objective targeting using neighbors
    objectives_chars = set()
    gt = goal_text.lower()
    if "stairs" in gt:
        objectives_chars.update({"<", ">"})
    if "boulder" in gt or "sokoban" in gt or "boxoban" in gt:
        objectives_chars.update(["{"])  # fountains as targets for boxoban-like
    if map_neighbors:
        for d in allowed:
            ch = map_neighbors.get(d, " ")
            if ch in objectives_chars and d in safe_passable and d not in prioritized:
                prioritized.append(d)

    # nearest objective step hint
    if nearest_objective_step and (nearest_objective_step in allowed) and nearest_objective_step not in prioritized:
        # Ensure it's considered early if safe; otherwise best-effort include
        if nearest_objective_step in safe_passable:
            prioritized.insert(0, nearest_objective_step)
        elif nearest_objective_step in passable_map:
            prioritized.append(nearest_objective_step)

    # Fill with remaining safe passable
    for d in safe_passable:
        if d not in prioritized:
            prioritized.append(d)

    # Only if no safe options exist, consider hazardous passable
    if not prioritized:
        for d in hazardous_passable:
            if d not in prioritized:
                prioritized.append(d)

    blocked_dirs = sorted(list(blocked_map))

    # Fallback non-movement actions if no good moves
    fallback_candidates = []
    for cand in ["search", "wait", "rest"]:
        if cand in (actions or []):
            fallback_candidates.append(cand)

    return {
        "blocked_dirs": blocked_dirs,
        "hazard_dirs": sorted(list(hazard_set)),
        "suggested_first_moves": prioritized[:4],
        "nearby_objectives": {
            "topology": {
                k: v
                for k, v in (topology or {}).items()
                if k in ["fountain_at", "stairs_up_at", "stairs_down_at"] and v
            },
        },
        "fallback_actions": fallback_candidates if not prioritized else [],
    }


def _detect_blocked_move_message(text: str) -> bool:
    low = (text or "").lower()
    patterns = [
        "cannot pass through",
        "cannot move through",
        "it's solid stone",
        "you hit the wall",
        "there is a wall in the way",
        "you bump into",
        "blocked",
    ]
    return any(p in low for p in patterns)


def _compute_oscillation(actions_seq: List[str]) -> Dict[str, Any]:
    opposites = {
        "north": "south",
        "south": "north",
        "east": "west",
        "west": "east",
        "northeast": "southwest",
        "southwest": "northeast",
        "northwest": "southeast",
        "southeast": "northwest",
    }
    toggles = 0
    pairs: Dict[str, int] = {}
    for i in range(2, len(actions_seq)):
        a0, a1, a2 = actions_seq[i - 2 : i + 1]
        if a0 and a1 and a2:
            if opposites.get(a0) == a1 and opposites.get(a1) == a2:
                toggles += 1
                key = f"{a0}<->{a1}"
                pairs[key] = pairs.get(key, 0) + 1
    score = toggles
    return {"score": score, "pairs": pairs}


def _neighbors_hazard_dirs(neighbors: Dict[str, str]) -> List[str]:
    if not neighbors:
        return []
    dirs = []
    for d, ch in neighbors.items():
        if _is_hazard_char(ch):
            dirs.append(d)
    return sorted(dirs)


def _bfs_first_step_to_targets(
    grid: List[str], width: int, height: int, start: Tuple[int, int], targets: set, radius: int = 5
) -> Optional[str]:
    if not start or not grid:
        return None
    from collections import deque

    sx, sy = start
    visited = set()
    q = deque()
    q.append((sx, sy, None))  # (x, y, first_move_dir)
    visited.add((sx, sy))

    def neighbors(x: int, y: int):
        for d, (dx, dy) in _DIRS.items():
            nx_, ny_ = x + dx, y + dy
            if 0 <= nx_ < width and 0 <= ny_ < height:
                yield d, nx_, ny_

    while q:
        x, y, first_dir = q.popleft()
        if abs(x - sx) + abs(y - sy) > radius:
            continue
        ch = grid[y][x]
        if ch in targets and not (x == sx and y == sy):
            return first_dir
        for d, nx_, ny_ in neighbors(x, y):
            if (nx_, ny_) in visited:
                continue
            chn = grid[ny_][nx_]
            # avoid hazards by default; allow stepping onto target even if hazard
            if (nx_, ny_) != (sx, sy) and _is_hazard_char(chn) and chn not in targets:
                continue
            if not _is_passable_char(chn) and chn not in targets:
                continue
            visited.add((nx_, ny_))
            q.append((nx_, ny_, first_dir or d))
    return None


# -------------------------- Compose knowledge query ------------------------


def _compose_knowledge_query(
    goal: str,
    entities: List[str],
    inventory: List[str],
    role: Optional[str],
    race: Optional[str],
    alignment: Optional[str],
    topology: Dict[str, List[str]],
    neighbor_sig: str,
    passable_dirs: List[str],
    hazard_dirs: List[str],
    nearest_step: Optional[str] = None,
) -> str:
    topo_sig = (
        f"walls:{','.join(topology.get('walls_at', []))}; "
        f"up:{','.join(topology.get('stairs_up_at', []))}; "
        f"down:{','.join(topology.get('stairs_down_at', []))}; "
        f"boulder:{','.join(topology.get('boulder_at', []))}; "
        f"fountain:{','.join(topology.get('fountain_at', []))}"
    )
    rr = ",".join([t for t in [role, race, alignment] if t])
    hazard_summary = "hazards:" + ",".join(sorted(hazard_dirs))
    query = (
        _normalize_space(goal)
        + " | role:"
        + rr
        + " | entities:"
        + ",".join(entities[:12])
        + " | inv:"
        + ",".join(inventory[:12])
        + " | topo:"
        + topo_sig
        + " | neighbors:"
        + neighbor_sig
        + " | passable:"
        + ",".join(passable_dirs)
        + " | "
        + hazard_summary
    )
    if nearest_step:
        query += " | objective_step:" + nearest_step
    return query


def _make_task_signature(
    goal: str,
    actions: List[str],
    entities: List[str],
    role: Optional[str],
    race: Optional[str],
    alignment: Optional[str],
    topology: Dict[str, Any],
    neighbor_sig: str,
) -> str:
    """
    Deterministic compact signature for the task, based on normalized goal, action set,
    canonical entities, role/race/alignment, coarse topology and neighbor signature.
    """
    topo_keys = ["walls_at", "doors_at", "stairs_up_at", "stairs_down_at", "boulder_at", "fountain_at"]
    topo_norm = {k: sorted(topology.get(k, []) or []) for k in topo_keys}
    payload = {
        "g": _normalize_space(goal),
        "a": sorted(actions or []),
        "e": sorted(entities or []),
        "r": role or "",
        "ra": race or "",
        "al": alignment or "",
        "t": topo_norm,
        "n": neighbor_sig or "",
    }
    blob = json.dumps(payload, sort_keys=True, ensure_ascii=False)
    sig = hashlib.sha1(blob.encode("utf-8")).hexdigest()  # stable and compact
    return f"minihack:{sig}"


# --------------------------- Memory Layers --------------------------------


@dataclass
class TaskSchemaLayer(Sub_memo_layer):
    """
    Parses initial context into a reusable, comparable task schema.
    Stores/retrieves prior schemas with outcome summaries. Distills similar cases.
    """
    layer_intro: str = "Task schema library: normalized task descriptors with goals, action sets, topology, and outcomes."
    database: Optional[Any] = field(default=None)

    def __post_init__(self):
        if self.database is None:
            self.database = Chroma(embedding_function=Embedding())

    async def _build_schema(self, init_dict: Dict[str, Any]) -> Dict[str, Any]:
        goal = init_dict.get("goal", "")
        long_term = init_dict.get("long_term_context", "")
        short_term = init_dict.get("short_term_context", "")
        action_dict = init_dict.get("action_dict", {}) or {}

        map_w, map_h = _extract_map_area(long_term)
        pos = _extract_position(long_term)
        stats_line = _extract_stats_line(long_term)
        role_info = _parse_role_race_alignment(long_term)
        entities = _canonicalize_entities(long_term)
        inv_items = _simplify_inventory_items(short_term)
        actions = _extract_action_set(action_dict)
        topology = _extract_local_topology(long_term)

        # Parse ascii map for neighbors and passability
        parsed_map = _parse_ascii_map(long_term)
        neighbors = parsed_map.get("neighbors", {})
        passable_dirs = [d for d, ch in neighbors.items() if _is_passable_char(ch)]
        hazard_dirs = _neighbors_hazard_dirs(neighbors)
        neighbor_sig = _neighbors_signature(neighbors)

        # Heuristic: nearby objectives within small radius
        targets = set()
        gl = goal.lower()
        if "stairs" in gl:
            targets.update({"<", ">"})
        if "boulder" in gl or "sokoban" in gl or "boxoban" in gl:
            targets.update({"{"})
        nstep = None
        if parsed_map.get("grid") and parsed_map.get("hero_xy"):
            nstep = _bfs_first_step_to_targets(
                parsed_map["grid"], parsed_map["width"], parsed_map["height"], parsed_map["hero_xy"], targets, radius=5
            )

        # Override textual topology with map evidence for adjacency-critical signals
        if neighbors:
            nearby_up = sorted([d for d, ch in neighbors.items() if ch == "<"])
            nearby_down = sorted([d for d, ch in neighbors.items() if ch == ">"])
            if nearby_up:
                topology["stairs_up_at"] = nearby_up
            if nearby_down:
                topology["stairs_down_at"] = nearby_down
            # Fountains near
            fdirs = sorted([d for d, ch in neighbors.items() if ch == "{"])
            if fdirs:
                topology["fountain_at"] = fdirs

        # Augment canonical entities from neighbor evidence
        if neighbors:
            if any(ch == "<" for ch in neighbors.values()) and "stairs_up" not in entities:
                entities.append("stairs_up")
            if any(ch == ">" for ch in neighbors.values()) and "stairs_down" not in entities:
                entities.append("stairs_down")
            if any(ch == "{" for ch in neighbors.values()) and "fountain" not in entities:
                entities.append("fountain")
        entities = sorted(set(entities))

        signature = _make_task_signature(
            goal, actions, entities, role_info["role"], role_info["race"], role_info["alignment"], topology, neighbor_sig
        )
        knowledge_query = _compose_knowledge_query(
            goal,
            entities,
            inv_items,
            role_info["role"],
            role_info["race"],
            role_info["alignment"],
            topology,
            neighbor_sig,
            passable_dirs,
            hazard_dirs,
            nearest_step=nstep,
        )

        schema = {
            "task_id": signature,
            "goal": _normalize_space(goal),
            "actions": actions,
            "initial_entities": entities,
            "inventory_items": inv_items,
            "map_size": {"width": map_w, "height": map_h},
            "initial_position": {"x": pos[0], "y": pos[1]} if pos else None,
            "initial_stats_line": stats_line,
            "role": role_info["role"],
            "race": role_info["race"],
            "alignment": role_info["alignment"],
            "local_topology": topology,
            "map_neighbors": neighbors,
            "passable_dirs": passable_dirs,
            "hazard_dirs": hazard_dirs,
            "nearest_objective_step": nstep,
            "knowledge_query": knowledge_query,
        }
        return schema

    async def _distill_case_lessons(
        self, cases_texts: List[Tuple[str, Dict[str, Any]]], schema: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        if not cases_texts:
            return [
                {
                    "lesson": "Prefer passable safe tiles; avoid oscillation; move toward visible objectives when safe.",
                }
            ]
        distilled: List[Dict[str, Any]] = []
        lesson_schema = {"lesson": {"type": "string", "description": "One or two concise actionable lines"}}
        agent = _get_default_agent(
            "Distill a short, actionable lesson from a prior episode snippet. Focus on transferable insight for grid roguelikes.",
            lesson_schema,
        )
        for text, md in cases_texts[:2]:
            try:
                resp = await agent.ask(
                    f"Current goal: {schema.get('goal')}\nEntities: {', '.join(schema.get('initial_entities', []))}\nTopology: {schema.get('local_topology')}\nSnippet:\n{text}\nProduce one concise lesson (<=180 chars).",
                    with_history=False,
                )
                lesson = _truncate(resp.get("lesson", ""), 200)
            except Exception:
                lesson = _truncate(
                    "Explore open tiles first; avoid pushing objects into corners; align with objectives.",
                    200,
                )
            distilled.append(
                _clean_list_of_dicts(
                    [
                        {
                            "case_id": md.get("case_id"),
                            "reward": md.get("reward"),
                            "outcome": md.get("outcome"),
                            "lesson": lesson,
                        }
                    ],
                    drop_none=True,
                )[0]
            )
        return distilled

    async def retrieve(self, **kwargs) -> Dict[str, Any]:
        init_dict: Dict[str, Any] = kwargs.get("init", {})
        if not isinstance(init_dict, dict):
            raise ValueError("TaskSchemaLayer.retrieve requires init dict")
        schema = await self._build_schema(init_dict)
        docs = self.database.similarity_search(schema["knowledge_query"], k=12)
        ranked: List[Tuple[str, Dict[str, Any]]] = []
        seen_ids = set()
        for d in docs:
            md = d.metadata or {}
            # hygiene: drop empty/generic stubs
            es = str(md.get("episode_summary", "") or "").strip()
            if es and len(es) < 30:
                continue
            case_id = md.get("case_id")
            if case_id and case_id in seen_ids:
                continue
            if case_id:
                seen_ids.add(case_id)
            reward = md.get("reward")
            try:
                reward_f = float(reward) if reward is not None else 0.0
            except Exception:
                reward_f = 0.0
            ranked.append(
                (
                    d.page_content,
                    {
                        "case_id": md.get("case_id"),
                        "task_id": md.get("task_id"),
                        "reward": reward_f,
                        "outcome": md.get("outcome"),
                    },
                )
            )
        ranked = [r for r in ranked if r[1].get("reward", 0.0) > 0.0] or ranked
        ranked.sort(key=lambda x: (x[1].get("reward", 0.0)), reverse=True)
        # Keep top-2 to avoid noise
        ranked = ranked[:2]
        distilled = await self._distill_case_lessons(ranked, schema)
        return {"task_schema": schema, "similar_cases": distilled}

    async def update(self, **kwargs) -> None:
        init_dict: Dict[str, Any] = kwargs.get("init", {})
        reward: float = kwargs.get("reward", 0.0)
        outcome: str = kwargs.get("outcome", "")
        episode_summary: str = kwargs.get("episode_summary", "")
        if not isinstance(init_dict, dict):
            return
        schema = await self._build_schema(init_dict)
        case_id = str(uuid.uuid4())
        meta = {
            "case_id": case_id,
            "task_id": schema["task_id"],
            "reward": float(reward),
            "outcome": outcome,
            "episode_summary": _truncate(episode_summary, 1000),
        }
        text = (
            f"Goal: {schema['goal']}\n"
            f"Role/Race/Align: {schema.get('role')}/{schema.get('race')}/{schema.get('alignment')}\n"
            f"Actions: {', '.join(schema['actions'])}\n"
            f"Entities: {', '.join(schema['initial_entities'])}\n"
            f"Inventory: {', '.join(schema['inventory_items'])}\n"
            f"Topo: {schema['local_topology']}\n"
            f"Neighbors: {_neighbors_signature(schema.get('map_neighbors', {}))}\n"
            f"Passable: {', '.join(schema.get('passable_dirs', []))}\n"
            f"Outcome: {outcome}, Reward: {reward}\n"
            f"Summary: {episode_summary}\n"
        )
        self.database.add_texts(texts=[text], metadatas=[meta], ids=[case_id])


@dataclass
class StrategyLibraryLayer(Sub_memo_layer):
    """
    Stores distilled, transferable strategies and pitfalls.
    Retrieves high-signal guidance for the current task schema and compresses to bullets.
    """
    layer_intro: str = "Strategy library: distilled plan outlines, heuristics, and pitfalls aggregated across tasks."
    database: Optional[Any] = field(default=None)

    def __post_init__(self):
        if self.database is None:
            self.database = Chroma(embedding_function=Embedding())

    async def _compress_suggestions(self, schema: Dict[str, Any], suggestions: List[str]) -> List[str]:
        if not suggestions:
            suggestions = [
                "Survey adjacent passable tiles and favor new exploration paths.",
                "Avoid oscillating moves; if blocked, pivot or search.",
                "Align early moves toward visible objectives when safe.",
            ]
        out_schema = {
            "bullets": {
                "type": "array",
                "items": {"type": "string"},
                "description": "3-6 concise, task-conditioned tips.",
            }
        }
        agent = _get_default_agent(
            "Condense raw strategy hints into 3-6 concise, actionable bullets for grid roguelike tasks. Max total 500 chars.",
            out_schema,
        )
        try:
            joined = "\n".join(suggestions)
            resp = await agent.ask(
                f"Goal: {schema.get('goal')}\nEntities: {', '.join(schema.get('initial_entities', []))}\nInventory: {', '.join(schema.get('inventory_items', []))}\nTopology: {schema.get('local_topology')}\nNeighbors: {_neighbors_signature(schema.get('map_neighbors', {}))}\nRaw hints:\n{joined}\nCondense to bullets.",
                with_history=False,
            )
            bullets = resp.get("bullets", [])[:6]
            bullets = [_truncate(b, 160) for b in bullets]
            if not bullets:
                bullets = [
                    "Explore passable directions; avoid repeated wall bumps.",
                    "Keep escape routes; do not corner pushable objects.",
                    "Approach visible objectives only when safe.",
                ]
            return bullets
        except Exception:
            return [
                "Survey open directions; avoid bumping into walls repeatedly.",
                "Prefer reversible steps; do not corner pushable objects.",
                "Re-evaluate plan after each interaction or new discovery.",
            ]

    async def retrieve(self, **kwargs) -> Dict[str, Any]:
        schema: Dict[str, Any] = kwargs.get("schema", {})
        if not schema:
            return {"strategies": [], "plan_outline": {}, "bulleted_tips": []}
        query = schema.get("knowledge_query", "") or schema.get("goal", "")
        docs = self.database.similarity_search(query, k=10)
        raw_texts = []
        filtered = []
        for d in docs:
            md = d.metadata or {}
            q = md.get("quality")
            try:
                qf = float(q) if q is not None else 0.0
            except Exception:
                qf = 0.0
            if qf < 0.05:
                continue
            raw_texts.append(d.page_content)
            filtered.append(
                {
                    "strategy_id": md.get("strategy_id"),
                    "topics": md.get("topics"),
                    "suggestion": _truncate(d.page_content, 300),
                }
            )
        bullets = await self._compress_suggestions(schema, raw_texts)

        plan_schema = {
            "plan_title": {"type": "string", "description": "Short title for the plan"},
            "ordered_steps": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Ordered, high-level steps.",
            },
            "pitfalls_to_avoid": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Common mistakes and how to avoid them.",
            },
            "key_checks": {
                "type": "array",
                "items": {"type": "string"},
                "description": "State checks to perform during execution.",
            },
        }
        agent = _get_default_agent(
            "Generate concise, transferable plans for grid-based roguelike tasks. Tailor to goal, entities, inventory, and local topology.",
            plan_schema,
        )
        hint_text = "\n".join([s["suggestion"] for s in filtered])
        user_prompt = (
            f"Goal: {schema.get('goal')}\n"
            f"Entities: {', '.join(schema.get('initial_entities', []))}\n"
            f"Actions: {', '.join(schema.get('actions', []))}\n"
            f"Inventory: {', '.join(schema.get('inventory_items', []))}\n"
            f"Topology: {schema.get('local_topology')}\n"
            f"Neighbors: {_neighbors_signature(schema.get('map_neighbors', {}))}\n"
            f"Prior strategy hints:\n{hint_text}\n"
            f"Produce an outline."
        )
        try:
            plan_outline = await agent.ask(user_prompt, with_history=False)
        except Exception:
            plan_outline = {
                "plan_title": "Generic Plan",
                "ordered_steps": [
                    "Survey surroundings and identify objectives and blockers.",
                    "Map reachable safe tiles and plan minimal-risk path.",
                    "Interact with key objects while maintaining retreat paths.",
                ],
                "pitfalls_to_avoid": [
                    "Avoid pushing objects into corners unless goal-aligned.",
                    "Do not enter dead-ends without escape.",
                ],
                "key_checks": [
                    "Re-evaluate objective proximity",
                    "Monitor HP and threats before risky actions",
                ],
            }
        filtered = _clean_list_of_dicts(filtered, drop_none=True, truncate_keys=["suggestion"])
        return {"strategies": filtered[:4], "plan_outline": plan_outline, "bulleted_tips": bullets}

    async def update(self, **kwargs) -> None:
        schema: Dict[str, Any] = kwargs.get("schema", {})
        summary: Dict[str, Any] = kwargs.get("summary", {})
        if not schema or not summary:
            return
        strategies: List[str] = summary.get("transferable_strategies", [])
        pitfalls: List[str] = summary.get("pitfalls", [])
        topics: List[str] = summary.get("topics", [])
        score: float = float(summary.get("signals", {}).get("score", 0.0))
        success = bool(summary.get("signals", {}).get("success", False))

        texts: List[str] = []
        metas: List[Dict[str, Any]] = []
        ids: List[str] = []

        for s in strategies:
            sid = str(uuid.uuid4())
            texts.append(s)
            metas.append(
                {
                    "strategy_id": sid,
                    "source_task_id": schema.get("task_id"),
                    "quality": score if score is not None else 0.0,
                    "success_bias": success,
                    "topics": ",".join(topics[:10]),
                }
            )
            ids.append(sid)

        for p in pitfalls:
            sid = str(uuid.uuid4())
            texts.append("Pitfall: " + p)
            metas.append(
                {
                    "strategy_id": sid,
                    "source_task_id": schema.get("task_id"),
                    "quality": (score or 0.0) * 0.9,
                    "success_bias": success,
                    "topics": ",".join(topics[:10]),
                }
            )
            ids.append(sid)

        if texts:
            self.database.add_texts(texts=texts, metadatas=metas, ids=ids)


@dataclass
class SpatialPriorLayer(Sub_memo_layer):
    """
    A knowledge graph of entity/action relations and spatial affordances.
    Nodes: entity types or action tokens. Edges: relation with weights.
    """
    layer_intro: str = "Spatial knowledge graph: entity/action affordances and relations with support counts."
    database: Optional[Any] = field(default=None)

    def __post_init__(self):
        if self.database is None:
            self.database = nx.Graph()
        for node in ["blocks_movement", "pushable", "goal_target", "hazard", "slows", "unknown"]:
            if node not in self.database:
                self.database.add_node(node, kind="relation")
        base_pairs = [
            ("wall", "blocks_movement", 3.0),
            ("door", "blocks_movement", 1.5),
            ("boulder", "pushable", 2.5),
            ("stairs_up", "goal_target", 1.0),
            ("stairs_down", "goal_target", 1.0),
            ("trap", "hazard", 2.0),
            ("lava", "hazard", 2.5),
            ("monster", "hazard", 1.5),
            ("fountain", "goal_target", 1.0),
            ("water", "hazard", 1.0),
        ]
        for e, r, w in base_pairs:
            if e not in self.database:
                self.database.add_node(e, kind="entity")
            if not self.database.has_edge(e, r):
                self.database.add_edge(e, r, weight=w)

    def _increment_relation(self, entity: str, relation: str, weight: float = 1.0):
        g: nx.Graph = self.database
        entity = entity.lower()
        if entity not in g:
            g.add_node(entity, kind="entity")
        if relation not in g:
            g.add_node(relation, kind="relation")
        if g.has_edge(entity, relation):
            g.edges[(entity, relation)]["weight"] += weight
        else:
            g.add_edge(entity, relation, weight=weight)

    def _parse_relations_from_text(self, text: str):
        low = (text or "").lower()
        if "cannot pass through" in low or "cannot move through" in low:
            m = re.search(r"cannot (?:pass|move) through (?:the )?([a-z\- ]+)", low)
            if m:
                mention = m.group(1).strip()
                if "bar" in mention:
                    self._increment_relation("wall", "blocks_movement", 2.0)
                else:
                    self._increment_relation(mention.split()[0], "blocks_movement", 2.0)
        if "it's solid stone" in low or "there is a wall in the way" in low or "you hit the wall" in low:
            self._increment_relation("wall", "blocks_movement", 1.5)
        if "push" in low and "boulder" in low:
            self._increment_relation("boulder", "pushable", 1.2)
        if re.search(r"stairs?\s+up", low):
            self._increment_relation("stairs_up", "goal_target", 0.8)
        if re.search(r"stairs?\s+down", low):
            self._increment_relation("stairs_down", "goal_target", 0.8)
        for obj in ["boulder", "fountain", "altar", "sink"]:
            if re.search(rf"you see here (?:an?|the)?\s*{obj}", low):
                rel = "goal_target" if obj in ["fountain"] else "unknown"
                self._increment_relation(obj, rel, 0.6)
        for hazard in ["trap", "lava", "acid", "poison", "spike", "monster"]:
            if hazard in low:
                self._increment_relation(hazard, "hazard", 1.0)
        if "water" in low or "water floor" in low:
            self._increment_relation("water", "hazard", 1.0)

    async def retrieve(self, **kwargs) -> Dict[str, Any]:
        entities: List[str] = kwargs.get("entities", []) or []
        topology: Dict[str, Any] = kwargs.get("topology", {}) or {}
        neighbors: Dict[str, str] = kwargs.get("map_neighbors", {}) or {}
        inferred: List[str] = list(entities)

        if not inferred and topology:
            if topology.get("stairs_up_at"):
                inferred.append("stairs_up")
            if topology.get("stairs_down_at"):
                inferred.append("stairs_down")
            if topology.get("fountain_at"):
                inferred.append("fountain")
            if topology.get("walls_at"):
                inferred.append("wall")
        if neighbors:
            if any(ch == "<" for ch in neighbors.values()):
                inferred.append("stairs_up")
            if any(ch == ">" for ch in neighbors.values()):
                inferred.append("stairs_down")
            if any(ch == "{" for ch in neighbors.values()):
                inferred.append("fountain")
            if any(_is_hazard_char(ch) for ch in neighbors.values()):
                inferred.append("water")

        g: nx.Graph = self.database
        priors: List[str] = []
        for e in set(inferred):
            if e in g:
                neighbors_rel = []
                for nbr in g.neighbors(e):
                    w = g.edges[(e, nbr)].get("weight", 1.0)
                    if g.nodes[nbr].get("kind") == "relation":
                        neighbors_rel.append((nbr, w))
                neighbors_rel.sort(key=lambda x: -x[1])
                for rel, w in neighbors_rel[:5]:
                    priors.append(f"{e} -> {rel} (support={round(w, 2)})")

        if not priors:
            base = [("wall", "blocks_movement"), ("boulder", "pushable"), ("stairs_down", "goal_target")]
            for e, r in base:
                if g.has_edge(e, r):
                    priors.append(f"{e} -> {r} (support={round(g.edges[(e, r)].get('weight', 1.0), 2)})")
        return {"spatial_priors": priors}

    async def update(self, **kwargs) -> None:
        init_long = (kwargs.get("init") or {}).get("long_term_context", "")
        steps: List[Dict[str, Any]] = kwargs.get("steps", []) or []
        goal_text: str = (kwargs.get("init") or {}).get("goal", "")
        if init_long:
            self._parse_relations_from_text(init_long)
        if goal_text:
            self._parse_relations_from_text("goal: " + goal_text)
        for st in steps:
            ltc = st.get("long_term_context", "")
            if ltc:
                self._parse_relations_from_text(ltc)


@dataclass
class RiskAndInteractionLayer(Sub_memo_layer):
    """
    Stores risk management heuristics and interaction patterns with inventory/terrain/monsters.
    Compresses retrieved tips into concise bullets.
    """
    layer_intro: str = "Risk and interaction library: safety heuristics and inventory usage rules."
    database: Optional[Any] = field(default=None)

    def __post_init__(self):
        if self.database is None:
            self.database = Chroma(embedding_function=Embedding())

    async def _compress_tips(self, schema: Dict[str, Any], tips_texts: List[str]) -> List[str]:
        if not tips_texts:
            tips_texts = [
                "Avoid repeating blocked moves; pivot to passable directions or search.",
                "Maintain escape routes; do not corner yourself while exploring.",
                "Use healing items proactively when HP is low before risky moves.",
            ]
        out_schema = {"tips": {"type": "array", "items": {"type": "string"}}}
        agent = _get_default_agent(
            "Condense risk and interaction notes into 3-6 concise bullets tailored to goal, topology, and inventory. Max total 450 chars.",
            out_schema,
        )
        try:
            joined = "\n".join(tips_texts)
            resp = await agent.ask(
                f"Goal: {schema.get('goal')}\nInventory: {', '.join(schema.get('inventory_items', []))}\nEntities: {', '.join(schema.get('initial_entities', []))}\nTopology: {schema.get('local_topology')}\nNeighbors: {_neighbors_signature(schema.get('map_neighbors', {}))}\nNotes:\n{joined}\nCondense.",
                with_history=False,
            )
            bullets = resp.get("tips", [])[:6]
            bullets = [_truncate(b, 150) for b in bullets]
            if not bullets:
                bullets = [
                    "Avoid repeating blocked moves; pivot or search.",
                    "Keep escape routes; avoid tight corners near walls.",
                ]
            return bullets
        except Exception:
            return [
                "Avoid repeated moves into blocked tiles; pivot and explore open directions.",
                "Preserve escape routes when engaging hazards.",
                "Use healing consumables preemptively at low HP.",
            ]

    async def retrieve(self, **kwargs) -> Dict[str, Any]:
        schema: Dict[str, Any] = kwargs.get("schema", {})
        if not schema:
            return {"risk_tips": []}
        inv = schema.get("inventory_items", [])
        ents = schema.get("initial_entities", [])
        query = (
            "risk safety interactions | items: "
            + ", ".join(inv[:10])
            + " | ents: "
            + ", ".join(ents[:10])
            + " | topo:"
            + json.dumps(schema.get("local_topology", {}))
        )
        docs = self.database.similarity_search(query, k=10)
        raw_texts = []
        for d in docs:
            md = d.metadata or {}
            conf = md.get("confidence")
            try:
                cf = float(conf) if conf is not None else 0.0
            except Exception:
                cf = 0.0
            if cf < 0.05:
                continue
            raw_texts.append(d.page_content)
        bullets = await self._compress_tips(schema, raw_texts)
        return {"risk_tips": bullets}

    async def update(self, **kwargs) -> None:
        schema: Dict[str, Any] = kwargs.get("schema", {})
        summary: Dict[str, Any] = kwargs.get("summary", {})
        if not schema or not summary:
            return
        risk_notes: List[str] = summary.get("risk_notes", [])
        score: float = float(summary.get("signals", {}).get("score", 0.0))
        success = bool(summary.get("signals", {}).get("success", False))
        texts, metas, ids = [], [], []
        for r in risk_notes:
            rid = str(uuid.uuid4())
            texts.append(r)
            metas.append(
                {
                    "tip_id": rid,
                    "source_task_id": schema.get("task_id"),
                    "confidence": score * (1.2 if success else 0.8),
                }
            )
            ids.append(rid)
        if texts:
            self.database.add_texts(texts=texts, metadatas=metas, ids=ids)


@dataclass
class ReflexRulesLayer(Sub_memo_layer):
    """
    Reflexive, topology-conditioned micro-advice for immediate next moves.
    Stateless generation based on current schema and spatial priors.
    """
    layer_intro: str = "Reflex rules: pattern-to-action guidance tied to local topology and common affordances."
    database: Optional[Any] = field(default=None)

    async def retrieve(self, **kwargs) -> Dict[str, Any]:
        schema: Dict[str, Any] = kwargs.get("schema", {})
        spatial_priors: List[str] = kwargs.get("spatial_priors", [])
        hazard_dirs: List[str] = kwargs.get("hazard_dirs", []) or []
        goal = (schema.get("goal", "") or "")
        topo = schema.get("local_topology", {}) or {}
        neighbors: Dict[str, str] = schema.get("map_neighbors", {}) or {}
        actions: List[str] = schema.get("actions", []) or []
        tips: List[str] = []

        blocked_dirs = topo.get("walls_at", []) or []
        if blocked_dirs:
            tips.append(
                f"Avoid bumping into blocked directions: {', '.join(sorted(blocked_dirs))}. Pivot to open tiles."
            )
        if neighbors:
            blocked_map = [d for d, ch in neighbors.items() if not _is_passable_char(ch)]
            if blocked_map:
                tips.append(f"Adjacent blocked tiles: {', '.join(sorted(blocked_map))}. Favor passable neighbors.")
        if hazard_dirs:
            tips.append(
                "Avoid stepping onto hazardous tiles (water/lava/traps) unless necessary; prefer safe passable neighbors."
            )
        sokoban_like = "boulder" in goal.lower() or "sokoban" in goal.lower() or "boxoban" in goal.lower()
        if sokoban_like:
            tips.append("Leave space behind boulders before pushing; avoid pushing into corners or against walls.")
            if topo.get("boulder_at") and topo.get("fountain_at"):
                tips.append("Align boulder-fountain along open lanes; scout path before any push.")
        for p in spatial_priors:
            if "boulder -> pushable" in p and not any("Boulders are pushable" in t for t in tips):
                tips.append("Boulders are pushable; ensure the tile behind is free before pushing.")
            if "wall -> blocks_movement" in p and not any("Walls/bars block" in t for t in tips):
                tips.append("Walls/bars block movement; navigate around instead of repeating bumps.")
        stairs_adjacent = any(ch in ("<", ">") for ch in neighbors.values())
        progress_goal = any(k in goal.lower() for k in ["as far as possible", "progress", "deeper", "descend", "ascend"])
        if stairs_adjacent:
            if progress_goal:
                tips.append("Objective is progress—descend/ascend now if safe (HP ok, no threats adjacent).")
            else:
                tips.append("Only approach stairs after scanning the room; avoid premature level changes.")
        if "search" in actions:
            near_walls = [d for d, ch in neighbors.items() if ch == "#"]
            if near_walls and not topo.get("doors_at"):
                tips.append("If adjacent to walls/bars with no door visible, try searching along the wall before advancing.")
        tips = [_truncate(t, 180) for t in tips][:6]
        return {"reflex_tips": tips}

    async def update(self, **kwargs) -> None:
        return


# -------------------------- Orchestrator ----------------------------------


def _normalize_action_token(action: Optional[str]) -> Optional[str]:
    if not action:
        return None
    a = _normalize_space(action).lower()
    # remove 'move ' prefix
    a = re.sub(r"^move\s+", "", a)
    # reduce 'far ' prefix
    a = re.sub(r"^far\s+", "", a)
    mapping = {
        "n": "north",
        "e": "east",
        "s": "south",
        "w": "west",
        "ne": "northeast",
        "se": "southeast",
        "sw": "southwest",
        "nw": "northwest",
        "north": "north",
        "east": "east",
        "south": "south",
        "west": "west",
        "northeast": "northeast",
        "southeast": "southeast",
        "southwest": "southwest",
        "northwest": "northwest",
    }
    if a in mapping:
        return mapping[a]
    # try to map tokens like "northwest " with extra text
    for k, v in mapping.items():
        if a.startswith(k):
            return v
    return a if a in mapping.values() else None


class MiniHackMemory(MemoStructure):
    """
    Multi-layer memory: Task schema -> Spatial priors -> Strategy retrieval -> Risk tips -> Reflex tips
    Update: Summarize episode (+action failure counts, oscillation) -> Update Spatial KG -> Update Strategy & Risk -> Index Schema
    """

    def __init__(self):
        super().__init__()
        self.schema_layer = TaskSchemaLayer()
        self.strategy_layer = StrategyLibraryLayer()
        self.spatial_layer = SpatialPriorLayer()
        self.risk_layer = RiskAndInteractionLayer()
        self.reflex_layer = ReflexRulesLayer()

    async def _summarize_episode(
        self, init_dict: Dict[str, Any], steps: List[Dict[str, Any]], reward: float
    ) -> Dict[str, Any]:
        schema = {
            "episode_summary": {"type": "string", "description": "Concise summary of what happened."},
            "transferable_strategies": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Generic strategies that can transfer to similar tasks.",
            },
            "pitfalls": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Common mistakes made or observed.",
            },
            "risk_notes": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Safety-related notes and interactions.",
            },
            "signals": {
                "type": "object",
                "description": "Outcome signals.",
                "properties": {
                    "success": {"type": "boolean"},
                    "score": {"type": "number"},
                },
                "required": ["success", "score"],
            },
            "topics": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Short topic tags like 'pushing', 'navigation', 'hazards'.",
            },
        }
        agent = _get_default_agent(
            "Summarize an episode from MiniHack. Extract transferable strategies, pitfalls, and risk notes. "
            "Use repeated failed actions and oscillation info to craft actionable pitfalls. Keep outputs concise and generic.",
            schema,
        )
        init_text = (
            f"Goal: {init_dict.get('goal','')}\n"
            f"Init entities: {', '.join(_canonicalize_entities(init_dict.get('long_term_context','')))}\n"
            f"Init inventory: {', '.join(_simplify_inventory_items(init_dict.get('short_term_context','')))}\n"
            f"Actions: {', '.join(_extract_action_set(init_dict.get('action_dict',{})))}\n"
        )
        sample_steps = steps[-12:] if len(steps) > 12 else steps
        step_summaries = []
        blocked_counts: Dict[str, int] = {}
        action_seq: List[str] = []
        for i, st in enumerate(sample_steps):
            msg = st.get("long_term_context", "")
            info = _extract_stats_line(msg)
            step_summaries.append(f"t{i}: {info} | msg_head: {msg.splitlines()[0] if msg else ''}")
        for st in steps:
            acts = st.get("action_took")
            if isinstance(acts, str):
                direction = _normalize_action_token(acts)
            elif isinstance(acts, list) and acts:
                direction = _normalize_action_token(acts[0])
            else:
                direction = None
            if direction:
                action_seq.append(direction)
            if _detect_blocked_move_message(st.get("long_term_context", "")):
                if direction:
                    blocked_counts[direction] = blocked_counts.get(direction, 0) + 1
        blocked_summary = ", ".join([f"{d}:{c}" for d, c in sorted(blocked_counts.items(), key=lambda x: -x[1])])
        oscill = _compute_oscillation(action_seq)

        user_prompt = (
            f"Episode overview:\n{init_text}\n"
            f"Reward: {reward}\n"
            f"Repeated blocked moves (direction:count): {blocked_summary if blocked_summary else 'none'}\n"
            f"Oscillation score: {oscill['score']}, pairs: {oscill['pairs']}\n"
            f"Recent steps (compact):\n" + "\n".join(step_summaries)
        )
        try:
            result = await agent.ask(user_prompt, with_history=False)
        except Exception:
            result = {
                "episode_summary": "Summary unavailable.",
                "transferable_strategies": [
                    "Reassess pathing when encountering blocked tiles; shift to open directions.",
                    "Plan pushes to keep escape routes and avoid corners.",
                ],
                "pitfalls": [
                    "Repeating moves into known walls; pivot and explore new paths.",
                ],
                "risk_notes": ["Monitor HP; avoid entering unknown areas when low."],
                "signals": {"success": reward > 0, "score": float(reward)},
                "topics": ["navigation", "planning"],
            }

        if oscill["score"] > 1:
            pair_txt = ", ".join([f"{k}:{v}" for k, v in sorted(oscill["pairs"].items(), key=lambda x: -x[1])])
            osc_pitfall = f"Avoid back-and-forth oscillation ({pair_txt}); commit to a new passable direction or search."
            result.setdefault("pitfalls", [])
            if osc_pitfall not in result["pitfalls"]:
                result["pitfalls"].append(osc_pitfall)
            result.setdefault("topics", [])
            if "oscillation" not in result["topics"]:
                result["topics"].append("oscillation")

        return result

    async def general_retrieve(self, recorder: Basic_Recorder) -> Dict:
        init_dict = getattr(recorder, "init", {}) or {}

        # Step 1: Task schema and filtered, distilled similar cases
        schema_ret = await self.schema_layer.retrieve(init=init_dict)
        schema = schema_ret.get("task_schema", {})

        # Step 2: Spatial priors for canonical entities (with topology and map neighbors)
        spatial_ret = await self.spatial_layer.retrieve(
            entities=schema.get("initial_entities", []),
            topology=schema.get("local_topology", {}),
            map_neighbors=schema.get("map_neighbors", {}),
        )

        # Step 3: Strategies and condensed bullets tailored to schema
        strat_ret = await self.strategy_layer.retrieve(schema=schema)

        # Step 4: Risk and interaction tips condensed
        risk_ret = await self.risk_layer.retrieve(schema=schema)

        # Step 5: Reflex micro-advice (hazard-aware)
        reflex_ret = await self.reflex_layer.retrieve(
            schema=schema,
            spatial_priors=spatial_ret.get("spatial_priors", []),
            hazard_dirs=schema.get("hazard_dirs", []),
        )

        # Step 6: Initial movement suggestions based on local map neighbors and topology with hazard-awareness
        move_suggestions = _suggest_first_moves(
            schema.get("actions", []),
            schema.get("local_topology", {}) or {},
            map_neighbors=schema.get("map_neighbors", {}),
            passable_dirs=schema.get("passable_dirs", []),
            goal_text=schema.get("goal", "") or "",
            hazard_dirs=schema.get("hazard_dirs", []),
            nearest_objective_step=schema.get("nearest_objective_step"),
        )

        # Action mask for downstream planners
        allowed_safe = [d for d in schema.get("passable_dirs", []) if d not in set(move_suggestions.get("hazard_dirs", []))]
        action_mask = {
            "allowed": sorted(allowed_safe),
            "blocked": move_suggestions.get("blocked_dirs", []),
            "hazard": move_suggestions.get("hazard_dirs", []),
            "fallback": move_suggestions.get("fallback_actions", []),
        }

        # Build clean memory package
        task_overview = {
            "goal": schema.get("goal"),
            "role": schema.get("role"),
            "race": schema.get("race"),
            "alignment": schema.get("alignment"),
            "actions": schema.get("actions"),
            "map_size": schema.get("map_size"),
            "initial_position": schema.get("initial_position"),
            "initial_entities": schema.get("initial_entities"),
            "inventory_items": schema.get("inventory_items"),
            "local_topology": schema.get("local_topology"),
            "map_neighbors": schema.get("map_neighbors"),
            "passable_dirs": schema.get("passable_dirs"),
            "hazard_dirs": schema.get("hazard_dirs"),
            "nearest_objective_step": schema.get("nearest_objective_step"),
            "initial_movement_suggestions": move_suggestions,
            "action_mask": action_mask,
            "similar_cases": schema_ret.get("similar_cases", []),
        }
        task_overview = {k: v for k, v in task_overview.items() if v not in [None, {}, [], ""]}

        memory_package = {
            "task_overview": task_overview,
            "suggested_strategies": {
                "plan_outline": strat_ret.get("plan_outline"),
                "bulleted_tips": strat_ret.get("bulleted_tips", []),
            },
            "spatial_priors": spatial_ret.get("spatial_priors", []),
            "risk_and_interactions": risk_ret.get("risk_tips", []),
            "reflex_tips": reflex_ret.get("reflex_tips", []),
            "retrieval_metadata": {
                "task_id": schema.get("task_id"),
                "knowledge_query": schema.get("knowledge_query"),
            },
        }
        if isinstance(memory_package.get("task_overview", {}).get("similar_cases"), list):
            memory_package["task_overview"]["similar_cases"] = _clean_list_of_dicts(
                memory_package["task_overview"]["similar_cases"], drop_none=True, truncate_keys=["lesson"]
            )
        memory_package["retrieval_metadata"] = {k: v for k, v in memory_package["retrieval_metadata"].items() if v}
        return memory_package

    async def general_update(self, recorder: Basic_Recorder) -> None:
        init_dict = getattr(recorder, "init", {}) or {}
        steps: List[Dict[str, Any]] = getattr(recorder, "steps", []) or []
        reward: float = float(getattr(recorder, "reward", 0.0) or 0.0)

        # Build schema once for downstream updates
        schema_ret = await self.schema_layer.retrieve(init=init_dict)
        schema = schema_ret.get("task_schema", {}) or {}

        # Summarize the episode with repeated failure counts and oscillation
        summary = await self._summarize_episode(init_dict, steps, reward)

        # Update spatial knowledge first
        await self.spatial_layer.update(init=init_dict, steps=steps)

        # Update strategy and risk libraries with distilled info
        await self.strategy_layer.update(schema=schema, summary=summary)
        await self.risk_layer.update(schema=schema, summary=summary)

        # Finally, index the task schema with outcome and full summary
        outcome = "success" if summary.get("signals", {}).get("success", False) else "failure_or_partial"
        await self.schema_layer.update(
            init=init_dict,
            reward=reward,
            outcome=outcome,
            episode_summary=summary.get("episode_summary", ""),
        )