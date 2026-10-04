# 严格相关工作

严格相关指：工作已经处理“从故事世界/真实事件到叙述呈现”的受限实现，或显式建模 focalization、reader knowledge、character belief、reveal order、suspense/foreshadowing。它们不是 LLM agent memory，但和新 formulation 最贴。

## 1. Focalization / POV 叙事生成

| 工作 | 为什么严格相关 | 和本课题的差别 |
|---|---|---|
| [Toward a Computational Model of Focalization in Narrative, FDG 2011](https://dl.acm.org/doi/pdf/10.1145/2159365.2159423) | 将 focalization 作为 narrative generation 中的计算问题：叙述由谁的视角组织，读者能看到什么 | 主要是 planning-based 叙事模型，不是 LLM/agent memory；没有长篇 memory 更新与 benchmark |
| [Automated Story Generation with Multiple Internal Focalization, 2011](https://inglab.github.io/assets/files/CIG2011Bae.pdf) | 多 internal focalization，直接对应多 POV 下的选择性呈现 | 重点是生成多视角叙述结构，不是 M1/M2/M3 三层 memory 与受限检索 |
| [Narrative Generation through Character's Point of View, CHI 2010](https://dl.acm.org/doi/10.1145/1753326.1753667) | 从角色 POV 生成叙事，限制呈现内容 | 经典 symbolic/interactive storytelling，和 LLM 长文本创作、自动评测距离较远 |
| [A Narrative Sentence Planner and Structurer, D&D 2019](https://aclanthology.org/2019.dnd-10.6.pdf) | 明确把 focalization 解释为选择 discourse 中可访问的知识 | 句子规划和结构化层面，非 memory architecture |

## 2. Reader model / 悬念 / 揭示控制

| 工作 | 为什么严格相关 | 和本课题的差别 |
|---|---|---|
| [A Computational Model of Narrative Generation for Suspense, AAAI WS 2006](https://cdn.aaai.org/Workshops/2006/WS-06-04/WS06-04-003.pdf) | Suspenser 将给定 fabula 转为能影响读者 suspense 的 narrative structure；显式考虑“何时告诉读者什么” | 很接近 M1 -> M3，但目标主要是 suspense，不处理角色 M2 和 LLM memory |
| [Narrative Generation for Suspense: Modeling and Evaluation, ICIDS 2008](https://link.springer.com/chapter/10.1007/978-3-540-89454-4_21) | reader model + suspense evaluation，是 reveal control 的早期系统工作 | 范围窄于多角色、多 POV、长篇写作 |
| [Creating Suspenseful Stories: Iterative Planning with LLMs, EACL 2024](https://aclanthology.org/2024.eacl-long.147.pdf) | LLM 时代的 suspenseful story planning，说明 LLM 故事生成中 suspense/reveal 仍然是难点 | 主要生成 suspense，不把 discourse memory 作为可更新状态，也不测 POV leakage |
| [Towards Human-Level Book-Writing Capability, 2026 preprint](https://arxiv.org/html/2605.17064v1) | 直接指出长篇小说需要 withholding information、preserving ambiguity、false beliefs | 更像系统/路线宣言，不是针对 M1/M2/M3 的 benchmark |

## 3. Character belief / false belief narrative planning

| 工作 | 为什么严格相关 | 和本课题的差别 |
|---|---|---|
| [Incorporating Global and Local Knowledge in Intentional Narrative Planning, AAMAS 2015](https://www.ifaamas.org/Proceedings/aamas2015/aamas/p1539.pdf) | 明确区分 global world state 和角色 local/imperfect knowledge，和 M1/M2 高度相关 | 主要用于 symbolic narrative planning，不处理 discourse memory M3 和 LLM 写作 |
| [HeadSpace: Incorporating Action Failure and Character Beliefs into Narrative Planning, AIIDE 2022](https://ojs.aaai.org/index.php/AIIDE/article/view/21961) | 用角色 false beliefs 生成行动失败的故事，直接对应 M2 中的误知 | 关注 plot planning 和 failed actions，不关注文本揭示顺序和读者知识状态 |
| [Generating Stories that Include Failed Actions by Modeling False Character Beliefs, 2017](https://cdn.aaai.org/ojs/12988/12988-52-16505-1-2-20201228.pdf) | false belief 作为叙事生成机制 | 不是长篇 LLM memory，也没有 M3 受限生成 |
| [Story Generation with Characters That Perceive and Assume, AIIDE 2014](https://theune.personalweb.utwente.nl/VS/tenbrinke-linssen-theune-AIIDE2014.pdf) | 将 omniscient characters 改成受感知限制的角色，直接对应角色可见性 | 角色感知和信念更新为主，非 discourse/reveal 生成 |
| [Toward Characters Who Observe, Tell, Misremember, and Lie, 2015](https://eis.ucsc.edu/papers/ryanEtAl_TowardCharactersWhoObserveTellMisrememberLie.pdf) | 角色观察、讲述、误记、撒谎，涉及主观记忆与叙事呈现 | 方向高度贴近，但不是 LLM agent memory benchmark |

## 4. 非线性叙事与 discourse order 控制

| 工作 | 为什么严格相关 | 和本课题的差别 |
|---|---|---|
| [Go Back in Time: Generating Flashbacks in Stories with Event Temporal Prompts, NAACL 2022](https://aclanthology.org/2022.naacl-main.104/) | 用 temporal prompts 控制 flashback，直接处理 event order 与 narrative order 不同 | 主要控制时间顺序，不处理角色知识边界和 M3 状态更新 |
| [Narrative Order Aware Story Generation, EMNLP Findings 2023](https://openreview.net/forum?id=daGbpBMkoy&noteId=iwkRwj7sx2) | 直接建模 narrative order，与 M1/M3 错位相关 | 不处理 M2 角色记忆，也不是受限 memory generation |
| [Generating Game Narratives with Focalization and Flashbacks, 2014](https://cdn.aaai.org/ojs/12758/12758-52-16275-1-2-20201228.pdf) | 同时涉及 focalization 和 flashback，是 M2/M3 交叉的经典近邻 | 游戏叙事/训练场景，非 LLM 长篇文本 |
| [Story Curves: Visualizing Nonlinear Narratives, 2017](https://www.researchgate.net/publication/319326463_Visualizing_Nonlinear_Narratives_with_Story_Curves) | 可视化 chronological order 与 narrative order 的差异 | 分析/可视化为主，不是生成方法 |

## 5. 最接近的 LLM 故事系统

| 工作 | 为什么严格相关 | 和本课题的差别 |
|---|---|---|
| [Multi-Agent Based Character Simulation for Story Writing, In2Writing 2025](https://aclanthology.org/2025.in2writing-1.9.pdf) | 已有 chronological fabula、syuzhet rewrite、character memory；是最需要正面区分的工作 | 它把 syuzhet 当作 presentation outline/rewrite 目标；本课题把 M3 当作可调、可更新、可验证的 discourse memory |
| [DOME: Dynamic Hierarchical Outlining with Memory-Enhancement, NAACL 2025](https://aclanthology.org/2025.naacl-long.63/) | 长篇故事生成中显式使用 temporal KG memory 和 conflict analyzer | 维护全局一致性，但不解决“知道但不能说”的 discourse/POV 受限生成 |

## 关键结论

新 formulation 并不是完全空白。最贴近的传统线索是：

- focalization = POV 下的可见性约束；
- suspense/reader model = 读者知识和 reveal schedule；
- belief narrative planning = 角色主观知识/误知；
- flashback/narrative order = M1 与 M3 的时间错位。

可发表空间在于把这些分散的 symbolic/narratology 机制转成 LLM/agent memory 场景下统一、可评测的 constrained generation 问题。

