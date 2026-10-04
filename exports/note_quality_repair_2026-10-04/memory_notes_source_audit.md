# Independent repair and source audit — memory notes

Audit date: 2026-10-05. Scope is Chinese reading notes through the original main-body conclusion, with substantive explanation of real sections, numeric evidence, and inline original paper figures; this is not a claim to translate every appendix. Original YAML preserved; no global metadata edited.

## Seven repaired notes

| Note | Body characters | Inline source figures | Missing asset links | Display-math delimiter balance |
|---|---:|---:|---:|---|
| 2026_beyond-dialogue-time-temporal-semantic-memory-for-person_arxiv-2601-07468.md | 10796 | 3 | 0 | Pass |
| 2024_memorybank-enhancing-large-language-models-with-long-ter_arxiv-2305-10250.md | 7814 | 4 | 0 | Pass |
| 2026_copa-benchmarking-personalized-question-answering-with-d_arxiv-2604-14773.md | 11651 | 5 | 0 | Pass |
| 2026_evomembench-benchmarking-agent-memory-from-a-self-evolvi_arxiv-2605-18421.md | 11743 | 4 | 0 | Pass |
| 2024_evaluating-very-long-term-conversational-memory-of-llm-a_doi-10-18653-v1-2024-acl-long-74.md | 10187 | 4 | 0 | Pass |
| 2025_membench-towards-more-comprehensive-evaluation-on-the-me_doi-10-18653-v1-2025-findings-ac.md | 10249 | 5 | 0 | Pass |
| 2026_evaluating-memory-in-llm-agents-via-incremental-multi-tu_arxiv-2507-05257.md | 11658 | 3 | 0 | Pass |

All seven front matters parse as YAML. All source image crops were visually inspected; figure provenance is preserved under each paper’s asset directory. TSM uses the archived TeX source and original extracted figures. The six other notes use the archived PDFs.

Source cautions explicitly retained in the notes: TSM ablation arithmetic and LoCoMo aggregate inconsistencies plus its ambiguous date example; CoPA unmatched table results and non-monotonic ablation claims; MemBench conflicting long-context length statements, differing sampled subsets, repeated factual/reflective scores, and a prose-versus-cost-table discrepancy; MemoryAgentBench appendix replication/table differences and mixed task metrics. MemoryBank’s absence of a true forgetting ablation is stated. EvoMemBench difficulty labels and transfer limits are qualified.

## Independent review of root-owned notes

Reviewed P2P, Narrative Theory, and Lookbacks against archived source text/PDF figures, focusing on actual section coverage, numeric claims, equations, source semantics, and crop boundaries. All 14 embedded source-figure crops were inspected together at high enough resolution to see overall panel/caption boundaries; no obvious clipped labels or panels were found. No factual correction was required in the reviewed current versions.

- P2P: checked main benchmark and human-preference numbers, HTML/SVG/LaTeX ablation, checker mechanisms (0.85 starting threshold, 0.05 decrement, 10% whitespace, 2.32/3.47 average reflection iterations, escalation after 5 retries), and calibration table. Note correctly distinguishes XGBoost’s best R²/JS from fine-tuned LLM’s lower KL.
- Narrative Theory: checked original main sections, ten A–J elements despite source prose saying eight, Genette’s story/discourse/narrating definitions, and all three Section 3 directions. Narrative economies and narrative beliefs are now represented with their social/cultural meaning. The note appropriately omits invented quantitative experiments.
- Lookbacks: checked behavioral table (10 independent runs × 100 samples), causal-intervention interpretation, three main mechanism diagrams, subspace/layer intervals, and visibility source 10–23 / joint address-pointer 24–31 / payload after 31. The note correctly treats pointer/address as causally supported representations rather than literal exact tensor copies.
