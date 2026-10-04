---
id: 2026_evolvemem-self-evolving-memory-architecture-via-autorese_arxiv-2605-13941
title: "EvolveMem: Self-Evolving Memory Architecture via AutoResearch for LLM Agents"
year: 2026
authors:
  - Jiaqi Liu
  - Xinyu Ye
  - Peng Xia
  - Zeyu Zheng
  - Cihang Xie
  - Mingyu Ding
  - Huaxiu Yao
venue: ""
field:
  - NLP
  - AI Agents
direction:
  - Long-term Memory
  - LLM Agents
  - Retrieval
keywords:
  - EvolveMem
  - LLM agents
  - memory architecture
  - self-evolving retrieval
  - AutoResearch
  - LoCoMo
  - MemBench
status: read
source_path: ""
source_archive_path: ../sources/2026_evolvemem-self-evolving-memory-architecture-via-autorese_arxiv-2605-13941_source.tar.gz
assets_path: ../assets/2026_evolvemem-self-evolving-memory-architecture-via-autorese_arxiv-2605-13941
paper_type: research
---

# EvolveMem: Self-Evolving Memory Architecture via AutoResearch for LLM Agents

## 一句话总结

EvolveMem 的核心不是再提出一种新的“记忆内容组织方式”，而是把长期记忆系统中的检索策略、融合权重、上下文预算、问答风格、验证机制等检索基础设施也作为可演化对象，让 LLM 根据逐题失败日志自动诊断、提出配置修改，并用评测结果决定接受、回滚或继续探索。

## 研究问题

长期运行的 LLM agent 需要跨会话记住用户偏好、项目状态、事实、事件和操作经验。已有记忆系统通常允许“记忆内容”增长、合并或遗忘，但检索系统本身往往在部署后固定：BM25/语义检索是否开启、top-k 多大、融合方式如何、上下文放多少、不同问题类别是否需要不同策略，通常都靠人工调参。

作者认为这里存在一个被低估的错配：当记忆库从几十条增长到几百条、问题类型从事实查询扩展到时间推理、多跳推理和对抗性 name-swap 时，一套冻结的检索配置很难同时适配所有场景。因此，真正自适应的长期记忆系统应当在两个层面共同演化：一是存储知识本身，二是查询这些知识的检索机制。

这篇论文要回答的问题是：能否让记忆系统像一个“小型研究员”一样，观察自己的失败、归因错误类型、提出检索架构调整、实证验证调整效果，并在无需人工调参的情况下不断改进？

## 核心方法

EvolveMem 将长期记忆系统拆成三层能力，并用一个闭环 evolution engine 把它们连接起来。

第一层是结构化记忆库。系统用 LLM 从多轮会话中抽取 typed memory unit，每条记忆包含自然语言内容、embedding、六类记忆类型之一，以及重要性、置信度、实体、地点、人物、主题、时间戳等元数据。抽取过程带有 retry、超长 chunk split 和 coverage verification，避免漏抽关键信息。记忆累积后再做去重、重要性衰减和实体强化。

第二层是可演化检索层。查询会同时走 BM25 词面检索、dense semantic 检索和结构化元数据检索，然后用 sum、weighted-sum 或 RRF 等方式融合。系统还可以按问题类别开启 entity-swap、query decomposition、answer verification 和不同 answer style。关键点是这些不是固定组件，而是统一暴露为 retrieval configuration $\theta$，由后续演化引擎调整。

第三层是 LLM 驱动的自演化引擎。每一轮系统先在 QA 集合上评测当前配置，保存逐题 raw log，包括问题、预测、标准答案、得分和检索到的证据。LLM diagnosis module 读取这些失败日志，判断错误根因，例如检索错实体、上下文不足、时间混淆、多跳问题没有拆解等，然后输出结构化配置修改 $\Delta\theta$。meta-analyzer 负责守门：如果新配置让整体指标明显下降就回滚到历史最佳；如果连续停滞则加入探索扰动；否则应用诊断提出的修改。

作者把这个过程称为 AutoResearch：系统自动执行 observe-hypothesize-experiment-validate 研究循环，只不过研究对象不是外部科学问题，而是自己的检索基础设施。

## 摘要解读

摘要把论文的定位说得很明确：已有长期记忆系统通常只让 stored content 演化，而 retrieval infrastructure 是冻结的。EvolveMem 的创新是把完整检索配置暴露为结构化 action space，并让 LLM 诊断模块基于逐题失败日志提出针对性修改。

作者强调三个结果：从最弱 BM25-only baseline 出发，系统可以自动收敛到更强配置；演化过程中还能发现初始 action space 没有显式包含的新配置维度；在 LoCoMo 和 MemBench 上都超过最强 baseline，并且配置跨 benchmark 迁移不是灾难性退化，而是正迁移。

## 分章节阅读笔记

### 1 Introduction

Introduction 这一章的核心任务是把论文的问题从“LLM agent 需要长期记忆”推进到一个更具体的命题：长期记忆系统不能只让记忆内容增长，检索机制本身也必须随之演化。

作者开篇设定了几个典型长期 agent 场景：个人助手需要跨数月记住用户偏好，coding agent 需要跟踪不断变化的项目决策，客服系统需要在多次会话中保持一致身份和上下文。这些任务都要求 persistent memory，也就是跨会话、可持续增长的长期记忆能力。但作者马上指出，记忆系统增长会带来一个常被忽略的问题：当存储记忆的规模和复杂度变化时，很多系统的 retrieval strategy 仍然停留在部署时的固定配置。

这里的关键例子很直观。事实查询需要 precise keyword matching，时间推理需要 time-aware filtering，多跳推理需要 query decomposition。也就是说，不同问题类型天然对应不同检索策略。一个 frozen retrieval configuration 很难同时服务所有问题。

第二段是在定位已有工作。作者把 recent memory architectures 分成两条线：一条是 memory organization，例如 MemGPT 用 tiered storage 管理 working memory 和 long-term memory，Mem0 与 A-MEM 用知识图谱或关联网络组织记忆内容，SimpleMem 将对话压缩成更适合检索的单元；另一条是 memory maintenance，例如 MemoryBank 用遗忘曲线剪除陈旧记忆，各类 consolidation 机制做去重和合并。作者承认这些工作都推动了 agent memory，但指出它们共享一个基础假设：memory content 可以随时间演化，而 retrieval infrastructure 保持冻结。

这里的 retrieval infrastructure 不只是“是否检索”，而是一整套检索与生成配置，包括 scoring functions、fusion weights、context budgets 和 answer-generation strategies。换句话说，作者认为过去很多系统把“记忆怎么存”做成动态的，却把“记忆怎么查”做成静态的。

第三段给出这篇论文真正的问题设定。随着记忆从几十条增长到几百条异质记录，原本针对小规模 memory store 调好的 retrieval policy 会逐渐失效；同时，问题类别本身也越来越多样。作者提出关键观察：真正 adaptive 的 memory system 应该在两个层面同时演化。第一，stored knowledge 要被维护和 consolidation；第二，retrieval infrastructure 要根据变化中的 memory landscape 和 query distribution 自适应。

这也解释了为什么论文不只是提出一个更好的 retriever，而是强调系统要能 autonomously observe its own failures、hypothesize root causes、test configuration changes，并只保留能提升性能的变化。Introduction 在这里已经把后文的 self-evolution loop 埋好了。

![Figure 1: EvolveMem self-evolution trajectory](../assets/2026_evolvemem-self-evolving-memory-architecture-via-autorese_arxiv-2605-13941/figures/source_figure_001_self-evolves-its-retrieval-configuration-on-loco.png)

Figure 1 是 Introduction 中最重要的视觉证据。左侧展示了 AutoResearch 的四步闭环：Evaluate 产生失败日志，Diagnose 分析 root cause，Propose 提出配置变化，Guard 判断是否接受或回滚。右侧展示 LoCoMo 上从 R0 到 R7 的 F1 轨迹：系统从 keyword-only retrieval 的 30.5% 起步，经历 R1 的 intent planning + rank fusion、R3 的 name-swap handling、R5 的 multi-hop query decomposition、R7 的 answer verifier + global tuning，最终到 54.3%。图中 R2 被标记为 reverted，说明论文并不是无条件相信 LLM 的修改建议，而是用 guard 机制过滤有害 proposal。

第四段正式介绍 EvolveMem。系统由 typed knowledge store、多视图 retriever 和 LLM-powered diagnosis module 组成。多视图 retriever 覆盖 lexical、semantic 和 structured-metadata signals；完整检索配置被暴露成 structured action space；诊断模块读取 per-question failure logs，分析 root causes，然后提出 targeted configuration adjustments。guarded meta-analyzer 负责防止坏修改持续生效，也就是后文会展开的 revert-on-regression safeguards。

作者把这个闭环称为 AutoResearch：系统自己执行 observe-hypothesize-experiment-validate 循环。这个词在 Introduction 中很重要，因为它把 EvolveMem 的贡献从“自动调参”提升到“系统自动研究自己的架构”。从工程角度看，它的核心仍然是失败日志驱动的配置搜索，加上回滚保护。

最后一段给出贡献和结果。作者声称 EvolveMem 是第一个通过 LLM-driven closed-loop diagnosis 自动演化 retrieval infrastructure 的 memory framework。实验上，在 LoCoMo 上相对最强 baseline 提升 25.7%，相对 minimal baseline 提升 78.0%；在 MemBench 上超过最强 baseline 18.9%。此外，演化出的配置能跨 benchmark 正迁移，而不是 catastrophic transfer。

这一章的逻辑链条可以概括为：长期 agent 需要 memory；memory 会增长和异质化；固定检索配置不适合长期变化；现有工作主要演化内容而非检索机制；EvolveMem 把检索配置变成可演化 action space；LLM 根据失败日志自动诊断和调参；系统用 guarded evaluation 保留有效变化。因此，Introduction 的真正作用是把论文研究问题钉住：长期记忆系统的核心瓶颈之一，是 retrieval policy 的生命周期管理。

### 2 Related Work

Related Work 这一章不是泛泛罗列前人工作，而是在为 Introduction 的核心断言补证据：已有系统确实在做 memory evolution、adaptive retrieval 或 self-improving agent，但它们大多没有把“长期记忆系统的检索基础设施”作为自演化对象。作者按三个方向组织相关工作：LLM agent memory systems、adaptive retrieval、self-improving agents / AutoResearch。

**Memory systems for LLM agents**

这一部分先承认 persistent memory 已经是 LLM agent 架构中的核心组件。作者列举的系统覆盖面很宽：Reflexion 和 Generative Agents 维护 episodic buffers，并按 recency / importance 建索引；MemGPT 使用类似操作系统的 tiered memory；MemoryBank 使用 Ebbinghaus-inspired forgetting；SCM 抽取 entity-aware summaries；Mem0 构建 knowledge graphs；A-MEM 建立 Zettelkasten-style networks；MemSkill 演化 reusable memory skills；SimpleMem、SeCom 和 RMM 分别通过 semantic compression、topic-level segmentation 和 reflective refinement 改善检索质量；LongMem 和 MemoryLLM 则把长期知识直接嵌进模型参数。

这些工作在“记忆内容如何表达、组织、压缩、合并、遗忘”上各有设计，但作者抓住一个共同点：它们多数让 stored content 演化，却让 retrieval infrastructure 保持冻结。EvolveMem 的定位就是补上这个缺口：不仅记忆内容会变，检索配置本身也要通过 LLM-powered closed-loop diagnosis 自演化。

本章的核心对比表可以转写为：

| System | Content evolution | Policy / parameter evolution | Typed memory | Consolidation | Offline evaluation |
|---|---:|---:|---:|---:|---:|
| MemGPT | ✓ |  |  | ✓ |  |
| SCM | ✓ |  |  | ✓ |  |
| SimpleMem | ✓ |  |  | ✓ |  |
| Mem0 | ✓ |  |  | ✓ |  |
| A-MEM | ✓ |  |  | ✓ |  |
| Memory-R1 | ✓ |  |  |  |  |
| Agentic Memory | ✓ |  | ✓ |  |  |
| MemoryBank | ✓ |  |  | ✓ |  |
| MemEvolve | ✓ | ✓ |  |  |  |
| EvolveMem | ✓ | ✓ | ✓ | ✓ | ✓ |

这张表的作用很明确：作者并不是说以前的 memory systems 没有演化，而是说演化对象通常是 content、skill 或 memory operation，而不是一整套可评测、可回滚、可持续调整的 retrieval policy。表中 EvolveMem 同时勾选了 content evolution、policy/parameter evolution、typed memory、consolidation 和 offline evaluation，体现了作者想强调的“系统级闭环”。

**Adaptive retrieval**

第二部分把 EvolveMem 和 RAG / adaptive retrieval 工作区分开。RAG 的基本思想是把外部知识检索进 LLM 输入。后续 Self-RAG、CRAG、FLARE、Adaptive-RAG 等方法确实变得更“自适应”：Self-RAG 用 reflection tokens 判断检索和生成质量，CRAG 做 corrective quality checks，FLARE 在生成置信度下降时触发检索，Adaptive-RAG 按查询复杂度路由不同策略。

但作者认为这些方法主要适配的是 when to retrieve、what to retrieve，或者 post-retrieval filtering；它们不解决一个长期部署问题：随着 memory store 和 query distribution 变化，scoring weights、fusion mode、context budgets 这些 retrieval parameters 是否也应该更新。EvolveMem 的差异就在这里。它不是只判断当前 query 该不该检索，而是通过离线评测和失败日志，在一个 structured action space 中持续调整检索系统的参数。

这部分还提到 LLM-powered database tuning 和 reinforcement-learning-based index optimization，说明“自动优化检索参数”不是完全新概念。但这些工作通常来自数据库或索引优化语境，使用 workload statistics；EvolveMem 则把这类思想迁移到 LLM agent long-term memory 上，并让 LLM diagnosis module 直接读逐题失败日志。

**Self-improving agents and AutoResearch**

第三部分把 EvolveMem 放进 self-improving agents 的谱系中。作者列举了 self-play、iterative refinement、evolutionary optimization，以及 Voyager、ExpeL、EvolveR、SkillRL、MemRL、Memory-R1、Agentic Memory、MemEvolve 等系统。这些工作共同关注 agent 如何从经验、轨迹、任务反馈或强化学习中改进自身能力。

这里的关键区分是“改进对象”。Voyager 更偏 skill library，ExpeL 抽取 reusable insights，SkillRL 做 recursive skill augmentation，MemRL / Memory-R1 更靠近 memory operations 或 episodic memory 的强化学习，MemEvolve 试图联合演化 agent knowledge 和 memory architecture。EvolveMem 的目标更窄也更工程化：它把 retrieval mechanism itself 当成研究对象，让系统通过 diagnosis-driven evolution 自动发现架构改进。

AutoResearchClaw 在这里提供了概念背景：LLM 可以执行 hypothesis generation、experimental design、result interpretation 等自动研究流程。EvolveMem 借用 AutoResearch 这个范式，但研究对象不是开放科学问题，而是系统自己的 retrieval infrastructure。这一定位帮助作者把“自动调参”表述为“系统对自身架构进行研究”。

第二章的整体作用可以概括为：作者把 EvolveMem 放在三个交叉方向的交点上。它继承 memory systems 对内容组织和 consolidation 的关注，继承 adaptive retrieval 对动态检索的关注，也继承 self-improving agents 的闭环改进思想；但它试图证明自己的新意在于，**长期记忆系统的 retrieval configuration 本身可以成为 AutoResearch 的对象**。

### 3 EvolveMem

第三章是论文的技术核心，标题直接用系统名 EvolveMem。它要回答 Introduction 留下的问题：如果 retrieval infrastructure 也要演化，那么系统应该如何表示记忆、如何检索、如何让 LLM 根据失败日志提出可靠的配置变化。

本章的主线可以概括为：先构建一个质量足够高、结构化程度足够强的 memory store；再把 retrieval layer 的所有关键参数显式暴露为 action space；最后用 self-evolution engine 读取失败日志、提出配置更新，并通过评测指标守门。

![Figure 2: EvolveMem architecture](../assets/2026_evolvemem-self-evolving-memory-architecture-via-autorese_arxiv-2605-13941/figures/source_figure_002_architecture-three-layers-connected-by-a-self-ev.png)

Figure 2 是理解第三章的入口。图中从下到上可以看成四层：Base Memory 负责 extractor、typed store 和 consolidator；Multi-View Retrieval + Answer 负责 query decomposition、多视图检索、RRF 融合、answer generation 和 verification；LLM Diagnosis 读取 failure logs，进行 categorize、analyze、suggest；Evolution Engine 则执行 extract、index、retrieve、evaluate、diagnose、adjust 的闭环，并在收敛后输出最优配置 $\theta^*$。右侧红色箭头强调了 self-evolution loop：系统不是一次性配置好检索器，而是在评测和诊断中反复更新检索配置。

#### 3.1 Structured Memory Store

这一小节解决的是“可检索材料本身是否可靠”的问题。作者明确说，一个 self-evolving retrieval system 的上限取决于它能从 memory store 中检索到什么。如果记忆抽取漏掉了关键信息，后面的检索配置再怎么演化也只能在缺失证据上调参。

每条 memory unit 表示为：

$m=(c,\mu,\mathbf{e},\boldsymbol{\eta})$，其中 $\mu\in\mathcal{T}$，$\mathbf{e}\in\mathbb{R}^d$。

这里 $c$ 是自然语言内容，$\mathbf{e}$ 是 dense embedding，$\mu$ 是 memory type，来自六类 taxonomy：episodic、semantic、preference、project state、working summary、procedural knowledge。$\boldsymbol{\eta}$ 是元数据集合，包括 importance、confidence、entity-reinforcement score、抽取实体、人物、地点、主题和创建时间。

这个表示方式的目的不是复杂化存储，而是让后面的多视图检索有足够信号可用。BM25 可以用 $c$，语义检索可以用 $\mathbf{e}$，structured retrieval 可以用 $\boldsymbol{\eta}$ 中的人物、地点、实体和时间。

Memory extraction 使用 sliding window 处理原始会话 $S=(u_1,\ldots,u_T)$。每个窗口调用 backbone LLM 抽取 typed memory units，并带上前一窗口的上下文以减少重复。作者设计了三个质量控制机制：

- LLM 调用失败时进行 retry，并保留已经抽出的部分结果；
- 窗口超过上下文长度时拆成更小 sub-window，再合并输出；
- coverage verifier 将抽取结果与源文本关键词对比，对缺失内容触发 re-extraction。

Consolidation 则负责维护记忆库长期质量。第一步是 deduplication：如果两条记忆 tokenized content 的 Jaccard similarity 超过阈值 $\tau_J$，就合并并保留更重要的一条。第二步是 importance decay：重要性 $\iota_i$ 随时间线性衰减，但有下限 $\iota_{\min}$，避免旧但仍有用的记忆彻底消失。第三步是 entity reinforcement：当某条记忆中的实体与新 query 反复共现时，强化分数 $\rho_i$ 增加，但 capped at $\rho_{\max}$，避免单条记忆仅凭高频实体支配排序。

这一小节的作用是给后面的 retrieval evolution 打基础：EvolveMem 不只是调检索参数，它也承认高质量抽取和 consolidation 是检索优化的前提。

#### 3.2 Retrieval as an Evolvable Action Space

这一小节是全文最关键的设计。作者把 retrieval configuration 从“人工调好的超参数”变成系统可以搜索和演化的 action space。不同问题需要不同检索策略：事实查询需要 exact keyword match，时间问题要优先 recent memories，多跳问题需要拆成子问题，对抗性 name-swap 问题需要忽略误导性人名、按语义主题找证据。

Retrieval layer 由三类 view 产生候选：

- lexical view：使用 BM25，适合精确关键词匹配；
- semantic view：使用 dense embedding cosine similarity，适合概念相似和 paraphrase；
- structured-metadata view：根据抽取出的人物、地点、实体等结构化字段过滤。

每个 view 独立返回 top-$k$ 候选，然后进入 fusion。作者允许三种 fusion mode：`sum`、`weighted-sum` 和 `rrf`。其中 RRF（reciprocal rank fusion）很重要，因为不同 view 的原始分数尺度可能不一致，RRF 用排名而不是直接用原始分数，能更稳健地合并多路结果。

最终排序公式是：

$s(q,m_i;\theta)=s_{\text{fuse}}(q,m_i;\theta)+\lambda_\iota\iota_i+\lambda_r\text{rec}(m_i)+\rho_i$。

这个公式把候选记忆的最终得分拆成两类信号。第一类是 query-memory relevance，也就是 $s_{\text{fuse}}$；第二类是 memory-intrinsic quality signals，包括重要性 $\iota_i$、时间新近性 $\text{rec}(m_i)$ 和实体强化分数 $\rho_i$。这使得排序不只看“这条记忆和 query 像不像”，还看“这条记忆是否重要、是否新近、是否与反复出现的实体相关”。

Query augmentation 有两个可选机制。第一个是 adversarial entity-swap：从 query 中去掉检测到的人名，再按主题重新搜索，并把结果与原始检索结果取并集。这个设计专门针对 LoCoMo 中 name-swap 类问题，因为问题里的人名可能是误导性的。第二个是 query decomposition：用 LLM 把多跳问题拆成若干 single-hop sub-queries，再分别检索并用 RRF 合并结果。

Answer generation 也被纳入可演化配置。系统不是只调检索，还允许 answer style 变化，例如 concise、explanatory、verifying、inferential。低置信答案还可以经过 second-pass verifier 复核。per-category overrides 允许不同问题类别使用不同检索参数和生成风格，这一点对长期记忆 QA 很关键，因为 single-hop、temporal、multi-hop、open-domain aggregation 和 adversarial question 的失败模式并不相同。

完整 action space 写成：

$\theta=(k_{\text{sem}},k_{\text{kw}},k_{\text{str}},B_{\text{ctx}},\text{mode},\{w_v\},\alpha,\{\theta_c\}_{c\in\mathcal{C}})\in\Theta$。

其中 $k_{\text{sem}}$、$k_{\text{kw}}$、$k_{\text{str}}$ 分别是语义、关键词、结构化检索的候选数量；$B_{\text{ctx}}$ 是放进 answer-generation LLM 的最大记忆数；$\text{mode}$ 是 fusion strategy；$\{w_v\}$ 是各 view 权重；$\alpha$ 是 answer style；$\theta_c$ 是每个 question category 的子配置。作者特别强调所有维度都会被 clamp 到 safe range，避免 LLM diagnosis 给出越界或不可执行的配置。

这一小节的贡献是把“检索系统”改写成“可被搜索的结构化配置空间”。没有这个空间，后面的 self-evolution engine 就没有明确可操作对象。

#### 3.3 Self-Evolution Engine

有了 action space 后，问题变成如何有效搜索它。作者认为 grid search 或 Bayesian optimization 不太适合这里，因为空间混合了连续参数、离散选择、类别特化配置和 answer style，而且每个配置都需要完整评测一遍。EvolveMem 选择用 LLM-powered diagnosis module 来读失败日志、形成 root-cause hypothesis，并提出 targeted adjustment。

演化目标定义为：

$\theta^*=\arg\max_{\theta\in\Theta}F(\theta;\mathcal{K},\mathcal{Q})$，

其中：

$F(\theta;\mathcal{K},\mathcal{Q})=\frac{1}{|\mathcal{Q}|}\sum_{(q,y^*)\in\mathcal{Q}}\mathrm{score}(\hat{y}(q;\theta,\mathcal{K}),y^*)$。

$\mathcal{K}$ 是 memory store，$\mathcal{Q}$ 是带标准答案的 evaluation questions，$\hat{y}$ 是系统在配置 $\theta$ 下给出的答案，$\mathrm{score}$ 在实验中主要是 F1。这个目标说明 EvolveMem 的演化不是在线凭感觉修改，而是以离线 evaluation metric 为准。

Failure diagnosis 是闭环的核心。每轮评测后，系统写出 per-question raw log，包括 question、prediction、ground-truth answer、score 和 retrieved sources。LLM diagnosis module 按结构化 rubric 读取这些日志，分析常见失败模式，例如 wrong entity retrieved、insufficient context、temporal confusion，然后输出结构化 proposal $\Delta\theta_r$。作者强调 rubric 是按 failure patterns 写的，不绑定具体 benchmark，因此新发现的配置维度可以在不改 rubric 的情况下被利用。

Update rule 是防止“LLM 乱调参”的关键。meta-analyzer 不直接相信诊断建议，而是用三分支规则处理：

1. 如果当前轮相对上一轮性能下降超过 $\tau_{\text{rev}}$，则 revert 到历史最佳配置 $\theta^\star$；
2. 如果连续两轮变化小于 $\epsilon$，说明停滞，则加入随机扰动 $\eta_{\text{exp}}$ 做 explore；
3. 其他情况下，应用诊断建议 $\Delta\theta_r$，并通过 $\mathrm{clamp}_\Theta$ 投影到合法范围。

形式上：

$\theta_{r+1}=\theta^\star_{r-1}$，当 $f_{r-1}-f_r>\tau_{\text{rev}}$；

$\theta_{r+1}=\theta_r\oplus\eta_{\text{exp}}$，当连续两轮 $|f_r-f_{r-1}|<\epsilon$；

$\theta_{r+1}=\mathrm{clamp}_\Theta(\theta_r\oplus\Delta\theta_r)$，其他情况下。

这个规则体现了 EvolveMem 的工程理性：LLM 负责提出有语义解释的修改方向，评测指标负责决定是否接受，回滚机制负责避免坏 proposal 长期污染系统。

算法流程可以理解为：

| Step | 操作 | 作用 |
|---|---|---|
| Extract | 从 sessions 中抽取 memory store $\mathcal{K}$ | 建立可检索知识库 |
| Retrieve & Answer | 用当前配置 $\theta_r$ 回答 QA 集合 | 得到预测和检索证据 |
| Score | 用任务指标计算 $f_r$ | 量化当前配置质量 |
| Diagnose | LLM 读取 raw log，提出 $\Delta\theta_r$ | 形成失败归因和配置修改 |
| Guard / Update | 回滚、探索或应用建议 | 防止退化并继续搜索 |
| Targeted re-extraction | 若诊断发现记忆覆盖缺口，重新抽取 | 把反馈从检索层传回记忆层 |

本章最后补充了停止条件：当 round-over-round improvement 低于 $\epsilon$，或达到最大轮数 $R_{\max}$ 时停止，返回历史最佳配置 $\theta^\star$。如果 diagnosis 发现失败来自 memory coverage gap，系统会触发 targeted re-extraction，这使反馈闭环不仅能调 retrieval，也能反向修补 memory store。

第三章的整体结论是：EvolveMem 的方法不是单个 retriever，也不是单次超参数搜索，而是一个“结构化记忆库 + 可演化检索配置 + LLM 失败诊断 + 指标守门”的闭环系统。它的核心技术价值在于把 retrieval policy 变成可观察、可诊断、可验证、可回滚的对象。

### 4 Experiments

第四章的作用是给前面的方法主张提供实验证据。作者围绕四个问题组织实验：自演化是否能从弱 baseline 获得显著提升；演化轨迹如何展开、LLM diagnosis 发现了哪些新维度；各组件分别贡献多少；演化出的配置是否能跨 benchmark 迁移，从而说明它学到的不是单一 benchmark trick。

#### 4.1 Experimental Setup

实验使用两个长期记忆 benchmark。LoCoMo 是 multi-session dialogue QA，论文使用完整 LoCoMo-10 release：10 个 conversations、1,986 个 QA pairs，每个样本有 19--32 个 sessions、369--689 turns，问题类别包括 single-hop、temporal、multi-hop/inferential、open-domain 和 adversarial name-swap。MemBench 是 memory-tool-use benchmark，包含 simple、comparative、aggregative、conditional、knowledge_update、post_processing、noisy 七个 LowLevel categories，作者评估 28 个 samples，即 $7$ 类别 $\times$ $2$ topics $\times$ $2$ samples。

指标上，LoCoMo 使用 token-level F1 和 BLEU-1；MemBench 使用 multiple-choice exact-match accuracy。LoCoMo 的 baseline 包括 MemVerse、Mem0、Claude-Mem、A-MEM、MemGPT、SimpleMem；MemBench 的 baseline 包括 RecentMemory、MemGPT、MemoryBank、SCMemory。

实现设置有一个关键点：EvolveMem 的初始配置 $\theta_0$ 被故意设得很弱。它只用 BM25-only fusion，semantic 和 structured views 关闭，$k_{\text{kw}}=5$，context budget $B_{\text{ctx}}=8$，entity-swap 和 query decomposition 都关闭。这样设置是为了证明性能提升来自 self-evolution，而不是来自作者手工提供的强初始检索器。演化最多运行 $R_{\max}=7$ 轮。

#### 4.2 Main Results

LoCoMo 主结果表很大，最需要抓住 overall F1 / BLEU 和类别上的主要趋势。简化后的 overall 对比如下：

| Backbone | Method | Overall F1 | Overall BLEU |
|---|---|---:|---:|
| GPT-4o | MemVerse | 0.365 | 0.342 |
| GPT-4o | Mem0 | 0.397 | 0.371 |
| GPT-4o | Claude-Mem | 0.383 | 0.360 |
| GPT-4o | A-MEM | 0.394 | 0.370 |
| GPT-4o | MemGPT | 0.404 | 0.376 |
| GPT-4o | SimpleMem | 0.432 | 0.407 |
| GPT-4o | EvolveMem | 0.543 | 0.569 |
| GPT-5.1 | MemVerse | 0.383 | 0.362 |
| GPT-5.1 | Mem0 | 0.390 | 0.369 |
| GPT-5.1 | Claude-Mem | 0.388 | 0.368 |
| GPT-5.1 | A-MEM | 0.385 | 0.365 |
| GPT-5.1 | MemGPT | 0.385 | 0.364 |
| GPT-5.1 | SimpleMem | 0.418 | 0.376 |
| GPT-5.1 | EvolveMem | 0.572 | 0.536 |

在 GPT-4o 上，EvolveMem 的 overall F1 是 0.543，超过最强 baseline SimpleMem 的 0.432，相对提升 25.7%。从类别看，提升最明显的是 single-hop 和 temporal：single-hop F1 从 SimpleMem 的 0.195 提升到 0.329，temporal F1 从 0.235 提升到 0.384。作者将这些收益归因于早期演化中激活的 semantic retrieval 和 recency-weighted fusion。open-domain 也从 0.402 提升到 0.496。adversarial 类别中 MemVerse 的 F1 最高为 0.944，EvolveMem 为 0.936，略低于 MemVerse，但 overall 仍然最高。

在 GPT-5.1 上，EvolveMem 的 overall F1 是 0.572，超过 SimpleMem 的 0.418，相对提升 36.8%。它在所有列上都达到最好，包括 multi-hop、single-hop、temporal、open-domain 和 adversarial。这说明作者想强调：演化后的 pipeline 不是只依赖 GPT-4o，而是在更强 backbone 上也保持有效。

MemBench 主结果如下：

| Method | GPT-4o Recall | GPT-4o Reasoning | GPT-4o Robustness | GPT-4o Overall | GPT-5.1 Recall | GPT-5.1 Reasoning | GPT-5.1 Robustness | GPT-5.1 Overall |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| RecentMem | 62.5 | 50.0 | 62.5 | 57.1 | 75.0 | 50.0 | 62.5 | 60.7 |
| MemGPT | 62.5 | 50.0 | 62.5 | 57.1 | 75.0 | 58.3 | 50.0 | 60.7 |
| MemBank | 37.5 | 33.3 | 75.0 | 46.4 | 75.0 | 50.0 | 75.0 | 64.3 |
| SCMem | 62.5 | 25.0 | 37.5 | 39.3 | 50.0 | 25.0 | 25.0 | 32.1 |
| EvolveMem | 87.5 | 66.7 | 50.0 | 67.9 | 87.5 | 66.7 | 62.5 | 71.4 |

MemBench 上，EvolveMem 在 GPT-4o 和 GPT-5.1 的 overall accuracy 分别是 67.9% 和 71.4%，都排名最高。收益主要集中在 Recall 和 Reasoning：GPT-4o Recall 达到 87.5，比最强 baseline 的 62.5 高很多；Reasoning 达到 66.7，也超过 baseline。Robustness 是弱项，GPT-4o 上只有 50.0，低于 MemBank 的 75.0。作者解释说 post_processing 类错误往往来自 memory store 中缺少相关记忆，这类 coverage limitation 不是单纯调 retrieval config 能解决的。

#### 4.3 Self-Evolution Trajectory and Dimension Discovery

这一小节是实验章最关键的证据，因为它展示了性能不是一次性跳上去，而是多轮自动诊断逐步打开不同机制。

| Round | Stage | Automated change | F1 (%) |
|---|---|---|---:|
| R0 | weak | BM25-only, $k=5$, $B_{\text{ctx}}=8$ | 30.5 |
| R1 | auto | intent planning + RRF fusion | 35.8 |
| R2 | revert | MMR diversity on Cat. 3，被回滚 | 34.8 |
| R3 | auto | entity-swap for Cat. 5 | 37.2 |
| R4 | auto | per-category answer-style flags | 38.5 |
| R5 | auto | query decomposition for Cat. 1/4 | 38.1 |
| R6 | auto | Cat. 3 inferential subtypes + Cat. 5 entity-swap expansion | 45.4 |
| R7 | auto | answer verification + hyperparameter sweep + context-budget tuning | 54.3 |

这张表体现了三个信息。第一，系统从非常弱的 BM25-only baseline 出发，最终从 30.5% 到 54.3%，相对提升 78.0%。第二，R2 是一个重要反例：LLM diagnosis 提出的 MMR diversity rerank 造成整体 F1 下降，于是 meta-analyzer 自动回滚。这说明系统不是盲目信任 LLM proposal。第三，很多收益来自逐步激活原本 dormant 的机制：semantic / RRF fusion、entity-swap、query decomposition、per-category answer style、answer verification。

作者特别强调三个由 diagnosis LLM 激活的配置维度：adversarial entity-swap、query decomposition、answer verification。entity-swap 去掉 query 中可能误导的人名，恢复一条按主题检索的 evidence pool；query decomposition 把复杂多跳问题拆成 single-hop sub-queries；answer verification 对低置信答案做第二次证据检查。它们不是单纯微调 top-k，而是结构性改变检索-回答流程。

#### 4.4 Cross-Benchmark Transfer and Generalization

这一小节回应一个关键质疑：EvolveMem 是否只是对 LoCoMo 过拟合。作者设计了跨 benchmark 迁移实验：

| Configuration | LoCoMo | MemBench |
|---|---:|---:|
| Baseline | 0.305 | / |
| $\mathcal{C}_L$ (LoCoMo only) | 0.543 | 0.543 |
| $\mathcal{C}_{LM}$ (LoCoMo → MemBench) | 0.593 | 0.792 |
| $\mathcal{C}_M$ (MemBench only) | / | 0.679 |

$\mathcal{C}_L$ 表示只在 LoCoMo 上演化 7 轮得到的配置。它 zero-shot 应用到 MemBench 后达到 54.3%，说明 LoCoMo 上学到的检索策略并非完全不能迁移。随后作者从 $\mathcal{C}_L$ 继续在 MemBench 上演化，得到 $\mathcal{C}_{LM}$，MemBench 达到 79.2%，超过从 MemBench scratch 演化的 $\mathcal{C}_M$ 67.9%。更重要的是，$\mathcal{C}_{LM}$ 反过来让 LoCoMo 从 0.543 提升到 0.593，没有出现 catastrophic transfer。

这个实验是作者用来支撑“self-evolution discovers generalizable retrieval principles”的主要证据。不过需要注意，它仍然是在两个固定 benchmark 之间迁移；它证明了跨 benchmark 有正迁移，但还没有完全证明真实开放环境下也能稳定泛化。

#### 4.5 Ablation Study

消融实验回答“到底哪些组件有用”。作者在 LoCoMo 上逐个移除组件并重新运行 evolution procedure：

| Configuration | F1 (%) | Drop |
|---|---:|---:|
| EvolveMem | 54.3 | -- |
| - Extraction quality control | 31.08 | -23.22 |
| - Semantic search | 43.98 | -10.32 |
| - LLM-powered diagnosis | 44.67 | -9.63 |
| - BM25 keyword search | 47.43 | -6.87 |
| - Entity-swap retrieval | 51.20 | -3.10 |
| - Query decomposition | 51.46 | -2.84 |
| - Structured metadata search | 51.97 | -2.33 |
| - Self-evolution | 52.27 | -2.03 |
| - Answer verification | 52.47 | -1.83 |
| Baseline (all disabled) | 30.50 | -23.80 |

最大掉分来自 extraction quality control：去掉 retry、chunk-splitting、coverage verification 后，F1 从 54.3 掉到 31.08，几乎回到 baseline。这说明检索演化的前提是 memory store 里确实有足够完整的证据。

第二组重要组件是 multi-view retrieval。去掉 semantic search 掉 10.32，去掉 BM25 掉 6.87，去掉 structured metadata search 掉 2.33。semantic search 的贡献最大，说明 paraphrase、抽象表述和非字面匹配在长期记忆 QA 中很关键；BM25 仍然重要，因为很多事实查询需要精确词面匹配。

第三个关键证据是 LLM-powered diagnosis。用 random perturbation 替代 diagnosis module 会掉 9.63 F1，说明逐题 failure logs 确实提供了有效优化信号，不只是 action space 本身足够强。

三个 diagnosis-discovered dimensions 合计也有明显贡献：entity-swap、query decomposition、answer verification 分别掉 3.10、2.84、1.83，合计约 7.77 F1。这个结果支撑作者的说法：self-evolution 不只是调已有权重，也发现了有结构意义的新机制。

第四章整体结论是：EvolveMem 的实验确实支持“失败日志驱动的 retrieval configuration 演化”能显著提升固定 benchmark 表现；消融说明抽取质量、多视图检索和 LLM diagnosis 是主要支柱；迁移实验提供了一定的泛化证据。但这章也暴露出边界：系统仍依赖固定 QA / gold answer / metric 来驱动演化，Robustness 和 post_processing 类问题仍受 memory coverage 限制。


### 5 Conclusion

Conclusion 很短，主要收束三个主张。第一，EvolveMem 是一种能 autonomously evolve retrieval infrastructure 的 memory architecture。它通过 LLM-driven closed-loop diagnosis，把原本需要人工调参的检索配置搜索变成一个 AutoResearch 过程：从最小起点出发，系统自己观察失败、提出修改、验证效果，并保留有效策略。

第二，作者用实验结果支持这个主张：LoCoMo 上相对最强 published baseline 提升 25.7%，相对 minimal baseline 提升 78.0%；MemBench 上超过最强 baseline 18.9%。这些数字在结论里不是重新展开实验，而是服务于一个更高层判断：self-evolution 不只是小幅调参，而是在弱初始配置上找到了显著更有效的 retrieval strategies。

第三，作者强调 self-expanding 和 transfer。所谓 self-expanding，是指 entity-swap、query decomposition、answer verification 这类新配置维度来自 failure diagnosis，而不是完全手工预置的固定调参列表。所谓 positive transfer，是指演化配置跨 benchmark 后没有 catastrophic transfer，反而在 LoCoMo 和 MemBench 上都能带来正收益。

结论的未来方向是 dynamic scenarios 和 multimodal settings。这里的 dynamic scenarios 很值得追问，因为当前论文主要还是在固定 QA benchmark 上做离线演化；真正长期 agent 会遇到用户偏好漂移、项目状态变化、记忆库持续增长、无标准答案反馈等问题。multimodal settings 则意味着记忆不只来自文本对话，还可能包括图像、界面状态、视频或文档截图，届时 retrieval infrastructure 的 action space 会更复杂。

因此，这篇论文最终留下的核心判断是：它证明了“让 retrieval policy 自演化”这条路线在离线长期记忆 benchmark 上有效，但还没有完全解决开放环境中如何构造持续反馈、如何避免 benchmark overfitting、如何自动生成 curriculum QA、如何处理动态和多模态记忆的问题。

## 关键公式 / 图表

### 关键公式

1. 融合排序公式：$s(q,m_i;\theta)=s_{\text{fuse}}(q,m_i;\theta)+\lambda_\iota \iota_i+\lambda_r\text{rec}(m_i)+\rho_i$。它把多视图检索得分、记忆重要性、时间新近性和实体强化结合起来。

2. 配置空间：$\theta=(k_{\text{sem}},k_{\text{kw}},k_{\text{str}},B_{\text{ctx}},\text{mode},\{w_v\},\alpha,\{\theta_c\}_{c\in\mathcal{C}})$。这一定义说明可演化对象不是一个参数，而是一组检索与生成策略。

3. 演化目标：$F(\theta;\mathcal{K},\mathcal{Q})=\frac{1}{|\mathcal{Q}|}\sum \mathrm{score}(\hat{y},y^*)$。系统通过离线 QA 评测来判断配置好坏。

4. guarded update：退步超过阈值则回滚，停滞则探索，否则应用 $\Delta\theta$。这个守门机制是论文避免 LLM 随意调参的关键。

### 关键图

Figure 1 展示了从 BM25 baseline 到 R7 的自演化路径。它的作用不是只展示性能曲线，而是说明每一轮接受或回滚的配置变化：R2 是有害 proposal，被自动回滚；R7 加入 answer verifier 和全局 tuning 后获得最大跃升。

Figure 2 是系统架构图，最值得看的是四层之间的信息流：Base Memory 负责抽取和 consolidation，Multi-View Retrieval + Answer 负责实际问答，LLM Diagnosis 读取 failure logs 并提出配置修改，Evolution Engine 负责评测、回滚、继续搜索和收敛。

### 关键表格

LoCoMo 主结果表说明 EvolveMem 在 GPT-4o 和 GPT-5.1 两个 backbone 上都超过已有 memory baselines，尤其在 temporal、single-hop 和 open-domain 上提升明显。对抗性类别里 MemVerse 在 GPT-4o 的 adversarial F1 很高，但 EvolveMem 的整体分数仍最高。

MemBench 表说明 EvolveMem 的优势集中在 Recall 和 Reasoning；Robustness 没有全面领先，提示系统仍受限于记忆覆盖和 post-processing 类型问题。

消融表最重要的结论是 extraction quality control 是基础，semantic search 和 LLM diagnosis 是主要增益来源，entity-swap/query decomposition/verification 是自演化发现的增益项。

## 实验结论

EvolveMem 的实验支持三个层次的结论。第一，从弱检索 baseline 出发，LLM 诊断驱动的配置演化可以产生大幅性能提升。第二，提升不是单个组件造成的，而是抽取质量、多视图检索、诊断模块、类别特化和验证机制共同作用。第三，LoCoMo 上演化得到的配置迁移到 MemBench 后仍有正效果，继续在 MemBench 上演化还会提升 LoCoMo，作者据此主张系统发现的是较通用的检索原则，而不只是 benchmark-specific trick。

不过实验也暴露边界：当相关记忆没有被抽取到 store 中时，检索层演化无法弥补；post_processing/noisy 这类鲁棒性问题仍是短板。另外，演化过程依赖带标准答案的离线评测集，真实开放环境中如何获得稳定反馈仍未完全解决。

## 局限性与可追问点

1. 自演化依赖固定评测集和指标。论文中的 evolution objective 需要 $\mathcal{Q}=\{(q,y^*)\}$ 这样的 QA pairs 和 ground truth，本质上是在 LoCoMo / MemBench 这类外部提供的监督信号上优化 retrieval configuration。真实个人助手、coding agent 或资产管理 agent 不一定持续拥有稳定 gold answer 和评分函数。

2. 存在 benchmark overfitting 风险。EvolveMem 虽然做了 LoCoMo $\rightarrow$ MemBench 的 positive transfer，但演化过程仍可能学习到某个 benchmark 的问题分布、答案风格、类别定义、adversarial name-swap 模式和 F1/BLEU/accuracy 指标偏好。跨两个固定 benchmark 的正迁移是有力证据，但还不足以证明开放动态环境中的稳健泛化。

3. 缺少基于自身 memory assets 的 QA / curriculum 数据飞轮。系统会读取固定 QA 的 failure logs 来调 retrieval config，但没有根据当前 memory store 自动生成 factual、temporal、multi-hop、aggregation、adversarial 等 probe QA，也没有自动验证 gold answer、组织由易到难的 curriculum，再把这些新 QA 加入后续演化。也就是说，它是 benchmark-supervised config evolution，不是 self-supervised memory curriculum learning。

4. 优化对象主要是 retrieval / answer configuration，而不是完整 memory lifecycle。`Retrieval as an Evolvable Action Space` 优化的是 top-k、fusion mode、view weights、context budget、answer style、entity-swap、query decomposition、verification、per-category overrides 等检索与回答参数。importance、confidence、memory typing 和 extraction prompts 虽会影响系统，但不是这一 action space 的主要自动优化对象；targeted re-extraction 也更像补 coverage gap，而不是系统性学习新的抽取策略。

5. “发现新配置维度”的边界需要澄清。论文说 diagnosis LLM 可以提出初始 action space 中没有的新维度，例如 entity-swap、query decomposition、answer verification；但实际系统仍需要代码层支持这些维度如何执行。这里更像半开放的配置扩展，而不是任意架构自动编程或自动实现新模块。

6. 诊断 LLM 的成本和稳定性需要更细评估。附录给出 LoCoMo 单样本 7 轮约 25--35 分钟，主要成本来自 QA evaluation LLM calls；这对离线调优合理，但对高频在线演化偏重。诊断结果还可能受 prompt、backbone、日志格式和采样波动影响。

7. 与更强工程 baseline 或人工调参的对比仍可加强。EvolveMem 和 SimpleMem/MemoryBank/MemGPT 等比较清楚，但如果人工专家也基于 LoCoMo failure logs 调参，EvolveMem 相对人工调参能省多少成本、是否达到更优、是否更稳定，还可以进一步量化。

8. 动态部署风险尚未充分覆盖。回滚机制能处理离线 F1 退步，但真实用户偏好变化、长期项目状态漂移、新实体持续加入、隐私约束、跨用户 memory contamination、反馈稀疏或冲突等问题不在当前实验范围内。

9. 对 coverage gap 的处理仍偏被动。论文允许 diagnosis 发现缺失记忆后触发 targeted re-extraction，但如果原始会话中信息本身含糊、矛盾、跨模态，或需要主动向用户追问，当前框架没有形成主动补全记忆资产的机制。

10. 多模态和工具环境仍是未来工作。论文结论提到 multimodal settings，但当前实验主要是文本长期记忆 QA。若记忆资产包含截图、代码仓库状态、表格、图像、视频或工具执行轨迹，retrieval action space、evidence grounding 和 evaluation signal 都需要重新设计。

## 对我当前研究/项目的启发

这篇论文对 agent memory / GraphRAG / 长期项目助手的直接启发是：不要只把“记忆内容”当作可演化对象，也应该把 retrieval policy 记录成结构化配置，并把每次失败的 query、answer、gold/reference、retrieved evidence、score 和配置快照保存下来。只有这样，系统才可能从失败日志中做可复现的诊断和演化。

工程上可以借鉴三点。第一，先建立弱但可运行的 baseline，然后让 evolution log 显示每个组件何时被打开、是否带来收益。第二，把所有检索行为参数化，包括 top-k、fusion、context budget、query decomposition、answer style 和 verifier，而不是散落在代码里。第三，必须有 guardrail：任何 LLM 提议都要经过离线验证、回滚和配置版本管理，不能直接写入生产策略。

如果用于叙事知识图谱或长期剧情 QA，EvolveMem 的 category-specific overrides 特别有价值：单跳事实、时间顺序、多跳因果、开放聚合、角色混淆问题本来就需要不同检索策略。可复用的方向是把问题分类器、失败日志 schema 和检索配置搜索空间先固定下来，再让诊断模块在这个空间里做逐轮调整。
