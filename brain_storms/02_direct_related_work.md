# 直接相关工作

这部分工作和新 formulation 有直接联系，但通常只覆盖 M1/M2/M3 中的一部分，不构成完整的“叙事记忆受限生成”。

## 1. Agent Memory 近邻

| 工作 | 覆盖点 | 缺口 |
|---|---|---|
| [Beyond Dialogue Time: Temporal Semantic Memory for Personalized LLM Agents, 2026](https://arxiv.org/html/2601.07468v1) | 事件真实发生时间和对话提及时间不同；与 M1 的 temporal organization 有关 | 不处理 discourse reveal time，也不处理角色 M2 的知识边界 |
| [Rashomon Memory, 2026](https://arxiv.org/html/2604.03588v3) | 多 perspective memory，各 perspective 可有独立 ontology/KG | perspective 是解释/目标视角，不是角色知识边界；没有 M1 -> M3 reveal 控制 |
| [Generative Agents, UIST 2023](https://dl.acm.org/doi/10.1145/3586183.3606763) | memory stream、reflection、planning，角色持续行动 | 角色 memory 没有用于受限 discourse realization |
| [MemoryBank, AAAI 2024](https://ojs.aaai.org/index.php/AAAI/article/view/29946) | 长期对话记忆和遗忘 | personalized memory，不是多角色叙事 |
| [MIRIX, 2025](https://arxiv.org/abs/2507.07957) | 多类型 agent memory | memory 类型丰富，但没有叙事 reveal/POV 约束 |
| [Collaborative Memory, 2025](https://arxiv.org/html/2505.18279v1) | private/shared memory access control | access control 机制可借鉴，但不是叙事写作 |

## 2. 长篇故事/剧本生成

| 工作 | 覆盖点 | 缺口 |
|---|---|---|
| [Re3, EMNLP 2022](https://arxiv.org/abs/2210.06774) | recursive reprompting/revision 生成长故事 | 无结构化 M1/M2/M3 |
| [DOC, ACL 2023](https://aclanthology.org/2023.acl-long.190/) | detailed outline control 改善长篇故事 coherence | outline 控制不是 discourse memory 受限生成 |
| [Dramatron, CHI 2023](https://dl.acm.org/doi/fullHtml/10.1145/3544548.3581225) | 剧本层级生成：title/characters/beats/locations/dialogue | 适合作剧本系统 baseline，但无角色知识边界评测 |
| [Agents' Room, ICLR 2025](https://openreview.net/forum?id=HfWcFs7XLR&noteId=xO9yNXp4VJ) | 多 agent 协作叙事生成和 Tell Me A Story prompts | 多 agent 分工不等于角色 epistemic constraints |
| [StoryVerse, FDG 2024](https://arxiv.org/abs/2405.13042) | 作者意图和角色模拟结合 | 相关于 authorial goals，但 M3 不是可验证 memory state |
| [StoryBox, 2025](https://arxiv.org/html/2510.11618v1) | sandbox character simulation 到长篇故事 | 更偏 bottom-up simulation，不主打 constrained discourse generation |

## 3. Theory of Mind / Belief Tracking

| 工作 | 覆盖点 | 缺口 |
|---|---|---|
| [FANToM, EMNLP 2023](https://openreview.net/forum?id=5TEfD2GBUc) | 多人信息不对称下的 belief tracking | 强相关于 M2，但不是长篇生成或 M3 reveal |
| [Minding Language Models' Lack of ToM, ACL 2023](https://aclanthology.org/2023.acl-long.780.pdf) | 多角色 belief tracker | 可用于 M2 评测，不处理 M1 -> M3 |
| [Hi-ToM, EMNLP Findings 2023](https://openreview.net/forum?id=L4yVLb6cLu&noteId=9HtPANhYGe) | 高阶 ToM belief | 可评测“A 认为 B 知道什么”，但不涉及写作呈现 |
| [OpenToM](https://github.com/seacowx/OpenToM) | first/second-order belief benchmark | 可借鉴题型，非创作任务 |
| [AnaToM, Findings 2025](https://aclanthology.org/2025.findings-ijcnlp.14.pdf) | 自动构造 ToM story/question | 可借鉴数据合成，非 discourse memory |

## 4. 综述入口

| 工作 | 用途 |
|---|---|
| [Automatic Story Generation: A Survey of Approaches, TOCHI 2021](https://dl.acm.org/doi/fullHtml/10.1145/3453156) | 传统 story generation、planning、emergent narrative、focalization 的综述入口 |
| [A Review of Plan-Based Approaches to Story/Discourse Generation, 2013](https://justusrobertson.com/papers/Young%20Ware%20Cassell%20and%20Robertson%202013%20-%20Plans%20and%20Planning%20in%20Narrative%20Generation.pdf) | plan-based narrative generation 和 discourse generation 的重要入口 |
| [A Survey on the Memory Mechanism of LLM-based Agents, TOIS 2025](https://dl.acm.org/doi/10.1145/3748302) | agent memory 综述入口 |

