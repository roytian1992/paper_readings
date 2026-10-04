# 可用 Benchmark

目前没有一个 benchmark 完整覆盖 M1 Truth Memory、M2 Character Memory、M3 Discourse Memory 之间的 constrained generation。现有 benchmark 只能分块使用。

## 最相关，可作为核心材料来源

| Benchmark / Dataset | 可用部分 | 缺口 |
|---|---|---|
| [Deciphering Digital Detectives / Jubensha dataset](https://aclanthology.org/2024.findings-acl.490/) | 中文剧本杀，包含 character scripts 和 game rules；天然有角色私有信息、公共规则、互动推理 | 目标是 agent 玩剧本杀和推理，不是写作生成；需补 discourse memory / reveal schedule 标注 |
| [WhodunitBench](https://openreview.net/forum?id=qmvtDIfbmS) / [GitHub](https://github.com/jun0wanan/WhodunitBench-Murder_Mystery_Games) | NeurIPS 2024 D&B spotlight；基于 murder mystery games；50 个 curated scripts + 3000+ QA；数据结构含 roles、public clues、key clues、reason、murderer、image clues | 偏 multimodal agents 和推理/游戏评测；可复用角色/线索/真相结构，但要改造成 M1/M2/M3 生成评测 |
| [WhoDunIt](https://arxiv.org/html/2502.07747v1) | 开放域 mystery novels/short stories，任务是读完整故事识别凶手 | 适合 culprit detection，不含玩家角色手册式 M2，也不含可调 M3 |
| [DetectiveQA](https://arxiv.org/html/2409.02465v2) | 侦探小说长上下文推理 QA | 长文本理解强，但不是剧本杀式多角色私有信息 |
| Llosa-style nonlinear multi-POV novels | 真实文学 stress test：多时间线、多对话层、多角色视角、叙述顺序和真实顺序高度错位；典型参考包括《绿房子》《酒吧长谈》《胡利娅姨妈与作家》 | 版权和标注成本高，不适合直接作为公开 benchmark 主体；更适合做少量人工标注 case study 或抽象成合成数据 schema |
| [ConStory-Bench](https://picrew.github.io/constory-bench.github.io/) | 长篇故事一致性；8k-10k word generations；多类 consistency errors | 不区分 truth memory、character memory、discourse memory；不专测 reveal leakage |
| [Tell Me A Story / Agents' Room](https://github.com/google-deepmind/tell_me_a_story) | 复杂长故事 prompts，可作为生成任务来源 | prompt 级，不带 M1/M2/M3 gold labels |
| [CML-Bench](https://arxiv.org/html/2510.06231v1) | 剧本质量评测：dialogue coherence、character consistency、plot reasonableness | 不测 POV knowledge boundary 或 reveal schedule |
| [Go Back in Time / flashback datasets](https://aclanthology.org/2022.naacl-main.104/) | flashback 和 event temporal prompt；适合 M1/M3 时间错位 | 不含多角色 M2 |
| [Narrative Order Aware Story Generation](https://openreview.net/forum?id=daGbpBMkoy&noteId=iwkRwj7sx2) | narrative order / event order 建模 | 不测角色知识边界 |

## M2 角色知识/信念可用

| Benchmark | 可用部分 | 缺口 |
|---|---|---|
| [FANToM](https://openreview.net/forum?id=5TEfD2GBUc) | 多人对话中的信息不对称和 belief tracking | 对话理解为主，不是长篇叙事生成 |
| [Hi-ToM](https://openreview.net/forum?id=L4yVLb6cLu&noteId=9HtPANhYGe) | 高阶 belief tracking | 缺少 discourse reveal |
| [OpenToM](https://github.com/seacowx/OpenToM) | first/second-order belief、false belief | 短文本 QA，非写作 |
| [AnaToM](https://aclanthology.org/2025.findings-ijcnlp.14.pdf) | 自动生成 ToM 问题，可借鉴构造方法 | 不覆盖长篇 M3 |

## Agent memory 可用

| Benchmark | 可用部分 | 缺口 |
|---|---|---|
| [LoCoMo](https://snap-research.github.io/locomo/) | long-term conversational memory，含时间推理 | conversation memory，不是 narrative discourse |
| [LongMemEval](https://arxiv.org/abs/2410.10813) | 长期记忆 QA，可测 memory retrieval | 无角色视角和揭示顺序 |
| [MemoryAgentBench](https://openreview.net/forum?id=DT7JyQC3MR) | incremental multi-turn agent memory | 不测“知道但不能说/不能用” |
| [MemBench](https://aclanthology.org/2025.findings-acl.989.pdf) | factual/reflective memory；participation/observation scenarios | 可借鉴 observation，但没有 M3 |

## 长文本/长故事外部评测

| Benchmark | 可用部分 | 缺口 |
|---|---|---|
| [LongGenBench](https://proceedings.iclr.cc/paper_files/paper/2025/hash/141304a37d59ec7f116f3535f1b74bde-Abstract-Conference.html) | 长文本复杂指令遵循 | 不专门测叙事 memory |
| [NarrativeQA](https://aclanthology.org/Q18-1023/) | 长故事理解 QA | 理解任务为主，不是生成和 reveal control |
| [GLUCOSE](https://aclanthology.org/2020.emnlp-main.370/) | story commonsense explanation | 可补充因果/事件理解，不测 discourse memory |

## 结论

可用 benchmark 的组合方式：

- 优先看 Jubensha / WhodunitBench，因为它们最接近 M1/M2/M3 的原生数据结构；
- 用 Llosa-style 文学样本作为 high-end qualitative stress test，验证方法能否处理真正复杂的多时间线、多 POV 和嵌套呈现；
- 用 ConStory-Bench / CML-Bench 看长篇故事和剧本的一般一致性；
- 用 FANToM / OpenToM / Hi-ToM 看角色 belief；
- 用 flashback / narrative order 相关数据看 M1/M3 时间错位；
- 用 LongMemEval / LoCoMo / MemoryAgentBench 看 agent memory 基础能力。

但核心 benchmark 仍需自构，因为缺少同时标注：

- truth event order；
- character-specific knowledge / false belief；
- discourse reveal order；
- POV-constrained generation；
- future leakage / POV leakage / belief contradiction。
