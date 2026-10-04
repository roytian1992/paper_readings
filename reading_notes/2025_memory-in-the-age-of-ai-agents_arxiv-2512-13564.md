---
id: 2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564
title: "Memory in the Age of AI Agents"
year: 2025
authors:
  - Yuyang Hu
  - Shichun Liu
  - Yanwei Yue
  - Guibin Zhang
  - Boyang Liu
  - Fangyi Zhu
  - Jiahang Lin
  - Honglin Guo
  - Shihan Dou
  - Zhiheng Xi
  - Senjie Jin
  - Jiejun Tan
  - Yanbin Yin
  - Jiongnan Liu
  - Zeyu Zhang
  - Zhongxiang Sun
  - Yutao Zhu
  - Hao Sun
  - Boci Peng
  - Zhenrong Cheng
  - Xuanbo Fan
  - Jiaxin Guo
  - Xinlei Yu
  - Zhenhong Zhou
  - Zewen Hu
  - Jiahao Huo
  - Junhao Wang
  - Yuwei Niu
  - Yu Wang
  - Zhenfei Yin
  - Xiaobin Hu
  - Yue Liao
  - Qiankun Li
  - Kun Wang
  - Wangchunshu Zhou
  - Yixin Liu
  - Dawei Cheng
  - Qi Zhang
  - Tao Gui
  - Shirui Pan
  - Yan Zhang
  - Philip Torr
  - Zhicheng Dou
  - Ji-Rong Wen
  - Xuanjing Huang
  - Yu-Gang Jiang
  - Shuicheng Yan
venue: ""
field:
  - AI Agents
  - NLP
direction:
  - Agent Memory
  - LLM Agents
keywords:
  - agent memory
  - memory systems
  - survey
status: read
source_path: ../sources/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564.pdf
source_archive_path: ../sources/arXiv-2512.13564v2.tar.gz
source_extract_path: ../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564/source
assets_path: ../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564
paper_type: survey
---
# Memory in the Age of AI Agents

## 一句话总结

这篇综述把 AI agent memory 从传统的“短期/长期记忆”分类中拆出来，重新定义为 agent 在环境交互中形成、演化、检索并用于决策的核心能力，并用 `Forms - Functions - Dynamics` 三个维度组织当前研究版图。

## 综述定位与范围

本文关注的是 foundation model-based agents 中的 memory，而不是一般意义上的 LLM 上下文管理或单次 RAG 检索。作者认为，memory 已经成为 agent 长程推理、持续适应和复杂环境交互的基础能力，但当前研究存在两个问题：一是方法增长很快，早期综述的分类已经覆盖不了 2025 年出现的新方向；二是 memory 相关术语高度碎片化，例如 declarative、episodic、semantic、parametric memory 等概念经常混用，导致“agent memory”边界不清。

因此，这篇综述的目标不是提出一个新模型，而是建立一个可以容纳现有工作的概念框架。作者首先区分 agent memory 与 LLM memory、RAG、context engineering，然后用三个问题组织全文：memory 由什么承载，memory 为什么存在，memory 如何在时间中运作和变化。

本文的覆盖范围包括三类内容：agent memory 的形式与功能分类，memory 在 agent 生命周期中的形成、演化、检索机制，以及 benchmarks、datasets、open-source frameworks 和未来研究方向。

## 核心分类体系

本文的中心分类是 `Forms - Functions - Dynamics`。

![Figure 1](../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564/figures/source_figure_001_overview.png)

`Forms` 回答 “What carries memory?”，也就是记忆由什么载体承载。作者把现有 agent memory 实现分成三类：token-level memory、parametric memory 和 latent memory。token-level memory 主要是显式文本、结构化记录、向量库、图结构等；parametric memory 把经验或知识写入模型参数或外部可训练模块；latent memory 则存在于 KV cache、activation、hidden states、latent embeddings 等内部表示中。

`Functions` 回答 “Why agents need memory?”，也就是记忆服务什么功能。作者不用粗粒度的短期/长期分类，而是提出 factual memory、experiential memory 和 working memory。factual memory 记录用户或环境事实；experiential memory 从任务执行经验中积累解决问题的能力；working memory 管理当前任务过程中的临时工作空间信息。

`Dynamics` 回答 “How memory operates and evolves?”，也就是记忆如何随交互过程运作。作者把生命周期分成 memory formation、memory evolution 和 memory retrieval。formation 从交互轨迹、工具输出、推理轨迹、反馈中抽取有用信息；evolution 对记忆进行整合、更新、遗忘、重组；retrieval 在决策时根据当前任务和观察取回相关记忆。

这个分类的重点是：memory 不只是一个存储模块，而是 agent 决策循环中的动态机制。短期/长期记忆不是固定架构差别，而是 formation、evolution、retrieval 在不同时间尺度上被调用后产生的行为差异。

## 章节地图

全文结构基本按“定义边界 -> 三维 taxonomy -> 资源整理 -> 未来方向”展开。

Section 1 Introduction 说明为什么 agent memory 需要新的综述和 taxonomy。核心动机是现有分类跟不上方法发展，并且概念碎片化严重。

Section 2 Preliminaries 形式化 LLM-based agents 和 agent memory systems。作者先把 agent 写成与环境交互的策略系统，再把 memory 写成一个随时间变化的状态 `M_t`，并通过 formation、evolution、retrieval 三个算子接入 agent 决策过程。后半部分区分 agent memory、LLM memory、RAG 和 context engineering。

Section 3 Form 讨论 memory 的承载形式，包括 token-level、parametric、latent 三类。这个部分偏系统实现视角。

Section 4 Functions 讨论 memory 的功能角色，包括 factual、experiential、working memory。这个部分偏“为什么需要记忆”的任务视角。

Section 5 Dynamics 讨论 memory 的生命周期，包括 formation、evolution 和 retrieval。这个部分偏运行机制视角。

Section 6 Resources and Frameworks 汇总 benchmarks、datasets 和 open-source memory frameworks，用来支撑实证研究和系统实现。

Section 7 Positions and Frontiers 给出作者对未来方向的判断，包括 memory retrieval vs. memory generation、自动化 memory management、RL 与 memory、multimodal memory、多 agent shared memory、world model memory、trustworthy memory 和人类认知连接。

Section 8 Conclusion 总结全文观点。

## 逐章阅读笔记

### 1 Introduction

#### 本章作用

Introduction 的作用是给整篇综述建立问题边界：为什么 agent memory 已经值得作为独立研究对象，为什么已有 taxonomy 不够，以及本文准备用什么框架重整这个领域。作者的核心判断是，memory 不是 agent 的附属模块，而是把 LLM 从静态条件生成器转变为可持续交互、可适应环境的 agent 的关键机制。

#### 从 LLM 到 Agent：为什么 memory 变重要

作者先从过去两年 LLM-based agents 的快速发展切入。当前 agent 不再只是调用一个 LLM 生成文本，而是通常包含 reasoning、planning、perception、memory、tool-use 等能力。部分能力，例如 reasoning 和 tool-use，正在通过 RL 等方式被内化到模型参数里；但还有一些能力依赖外部 agentic scaffolds，也就是模型外部的系统脚手架。

在这个背景下，memory 的位置比较特殊。LLM 参数不能在每次交互后快速更新，因此如果 agent 要在长程任务、持续交互、个性化服务、社会模拟、推荐系统、金融调查等场景中保留历史信息，就必须有显式或隐式的 memory mechanism。也就是说，memory 承担的是“持续性”和“适应性”：让 agent 不只响应当前输入，还能利用过去的交互、经验和环境反馈调整行为。

#### 为什么需要新的 Taxonomy

作者提出新 taxonomy 的动机有两个。

第一，已有 taxonomy 已经过时。早期综述对 agent memory 的整理有价值，但它们出现时，很多 2025 年的新方向还没有充分发展。例如：memory frameworks 可以从过去经验中蒸馏 reusable tools；memory-augmented test-time scaling 把 memory 用到测试时扩展和推理增强里。这些方法很难被传统 long-term / short-term memory 或 episodic / semantic memory 分类完整覆盖。

第二，概念碎片化严重。现在很多论文都声称研究 agent memory，但它们的目标、实现方式和假设差别很大。有的关注用户事实，有的关注任务轨迹，有的关注参数更新，有的关注 KV cache 或 latent state。与此同时，declarative、episodic、semantic、parametric memory 等术语经常交叉使用，导致 agent memory 的边界变得不清楚。

因此，这篇综述想做的不是罗列论文，而是建立一个能统一现有定义、吸收新趋势、解释底层原则的系统框架。

#### 五个核心问题


| 问题                                                                      | 对应章节            | 含义                                     |
| --------------------------------------------------------------------------- | --------------------- | ------------------------------------------ |
| agent memory 如何定义，和 LLM memory、RAG、context engineering 有什么关系 | Section 2           | 先划清概念边界                           |
| memory 有哪些承载形式                                                     | Section 3 Forms     | token-level、parametric、latent          |
| agent 为什么需要 memory                                                   | Section 4 Functions | factual、experiential、working memory    |
| memory 如何运作、适应和演化                                               | Section 5 Dynamics  | formation、evolution、retrieval          |
| 未来研究方向是什么                                                        | Section 7 Frontiers | 自动化管理、RL、多模态、多 agent、可信等 |

这五个问题对应全文的主干。Section 2 负责定义边界；Section 3、4、5 分别展开 Forms、Functions、Dynamics；Section 6 整理 benchmarks 和 frameworks；Section 7 给出未来方向。

#### Forms - Functions - Dynamics 的含义

Introduction 中正式引出本文的三维框架。

`Forms` 关注 memory 的承载形态，即 “What architectural or representational forms can agent memory take?”。作者后文会把它分成 token-level、parametric、latent memory。

`Functions` 关注 memory 的目的，即 “Why is agent memory needed, and what roles or purposes does it serve?”。作者后文会把它分成 factual、experiential、working memory。

`Dynamics` 关注 memory 的生命周期，即 “How does agent memory operate, adapt, and evolve over time?”。作者后文会围绕 formation、evolution、retrieval 展开。

这个框架的价值在于，它避免只用时间尺度划分 memory。短期/长期记忆当然重要，但对现代 agent memory 来说，更关键的是：它以什么形式存在，服务什么功能，如何在交互过程中被写入、更新和读取。

#### Figure 1 的作用

Figure 1 是全文 taxonomy 的总览图。它把 agent memory 同时放到三个维度中：底部是 Forms，包括 token-level、parametric、latent memory；斜向维度表示 Functions，包括 factual、experiential、working memory；时间/使用维度体现 short-term 到 long-term。图中还把代表性系统放入这个空间，说明本文不是只做概念分类，而是要把不同系统定位到统一坐标系里。

#### 本文贡献

作者总结了四点贡献：

- 提出一个 up-to-date、多维度的 agent memory taxonomy，即 Forms - Functions - Dynamics。
- 讨论不同 memory forms 与 functional purposes 之间的适配关系，而不是孤立罗列类别。
- 总结 agent memory 的新兴研究方向，给出未来研究路径。
- 整理 benchmarks 和 open-source frameworks，方便后续实证研究和系统开发。

#### 本章小结

Introduction 的核心结论是：agent memory 不是简单的历史记录或上下文缓存，而是 agentic intelligence 的 first-class primitive。后文所有分类都服务于这个判断：如果要理解现代 AI agents 如何持续适应环境，就必须同时理解 memory 的承载形式、功能角色和动态机制。

### 2 Preliminaries: Formalizing Agents and Memory

#### 本章作用

Section 2 是全文的概念地基。作者在这里不急着分类具体 memory 方法，而是先回答两个问题：什么是 LLM-based agent system，什么是 agent memory system。只有把这两个对象形式化之后，后面的 Forms、Functions、Dynamics 才有清晰参照。

本章还负责划清边界：agent memory 和 LLM memory、RAG、context engineering 有大量技术重叠，但研究对象和目标不同。Figure 2 是这个边界讨论的总览图。

#### 2.1 LLM-based Agent Systems

作者把 agent 系统形式化为一个随时间与环境交互的决策过程。设 agent 集合为 $I = \{1, ..., N\}$，其中 $N = 1$ 是单 agent，$N > 1$ 是 multi-agent，例如 debate 或 planner-executor 架构。环境有状态空间 $S$，在每个时间步 $t$，环境根据当前状态和 action 发生转移：

$s_{t+1} \sim \Psi(s_{t+1} \mid s_t, a_t)$

这里 $a_t$ 是时间步 $t$ 执行的动作。这个抽象能覆盖单 agent 顺序决策，也能覆盖 multi-agent 中通过环境产生的隐式协调。

每个 agent $i$ 在时间步 $t$ 接收 observation：

$o_t^i = O_i(s_t, h_t^i, Q)$

其中 $h_t^i$ 是 agent $i$ 可见的交互历史，可能包括历史消息、工具输出、中间推理轨迹、共享工作区状态或其他 agent 的贡献。$Q$ 是任务说明，例如用户指令、目标描述或约束。

这一节强调 LLM-based agent 的 action space 不只是文本生成，而是异质的、结构化的动作空间：


| Action 类型                 | 含义                                                         |
| ----------------------------- | -------------------------------------------------------------- |
| Natural-language generation | 生成推理、解释、回复、指令                                   |
| Tool invocation actions     | 调用 API、搜索引擎、计算器、数据库、模拟器、代码执行环境     |
| Planning actions            | 输出任务分解、执行计划、子目标                               |
| Environment-control actions | 操作外部环境，例如导航、编辑代码仓库、修改共享 memory buffer |
| Communication actions       | 与其他 agent 通过结构化消息协作或协商                        |

虽然这些 action 语义不同，但作者把它们统一为由 autoregressive LLM backbone 在上下文输入条件下产生的策略：

$a_t = \pi_i(o_t^i, m_t^i, Q)$

这里 $m_t^i$ 是 memory-derived signal，也就是从 memory 系统中取出的信息。这个公式很关键：memory 不是事后附加的存储，而是直接进入 agent policy 的决策输入。

完整执行过程形成 trajectory：

$\tau = (s_0, o_0, a_0, s_1, o_1, a_1, ..., s_T)$

每一步包含四个环节：环境 observation、可选 memory retrieval、LLM-based computation、action execution。Section 2.1 的作用是把 agent 先定义成一个“观察-记忆-计算-行动”的循环系统。

#### 2.2 Agent Memory Systems

作者接着定义 agent memory system。基本动机是：agent 当前 observation $o_t^i$ 通常不足以支持有效决策，因此 agent 需要利用来自当前任务内部以及过去任务的信息。

作者把 memory 表示为一个随时间演化的状态：

$M_t \in \mathcal{M}$

$\mathcal{M}$ 是所有可接受 memory configuration 的空间。这里作者刻意不规定 $M_t$ 的内部结构，因为它可以是 text buffer、key-value store、vector database、graph structure 或混合表示。这个设计是为了让后续 taxonomy 能覆盖不同实现。

重要的是，作者不把 short-term memory 和 long-term memory 定义为两个固定模块。相反，同一个 memory container 可以同时支持两种作用：

- cross-trial memory：任务开始前已经从过去 trajectories 中蒸馏出的信息，接近长期记忆；
- inside-trial memory：当前任务执行中不断积累的信息，接近短期记忆。

二者的区别来自使用模式，而不是架构上必须分成两个组件。

作者用三个 conceptual operators 描述 memory lifecycle。


| Operator  | 公式                              | 作用                                                                          |
| ----------- | ----------------------------------- | ------------------------------------------------------------------------------- |
| Formation | $M_{t+1}^{form} = F(M_t, \phi_t)$ | 从工具输出、推理轨迹、计划、自评、环境反馈等 artifacts 中抽取有未来价值的信息 |
| Evolution | $M_{t+1} = E(M_{t+1}^{form})$     | 把候选 memory 整合进已有 memory base，可能包括去重、冲突解决、遗忘、重组      |
| Retrieval | $m_t^i = R(M_t, o_t^i, Q)$        | 根据当前 observation 和任务构造查询，返回可供 LLM policy 使用的 memory signal |

这里 $\phi_t$ 表示 agent 在时间步 $t$ 产生的信息 artifacts。作者强调 formation 不是无脑保存完整历史，而是选择性地把潜在有用的信息转成 memory candidates。Evolution 负责让 memory base 可持续维护，而不是无限堆积。Retrieval 则把 memory 格式化为 LLM 能直接消费的文本片段或结构化摘要。

这一节的关键观点是：formation、evolution、retrieval 不必每一步都调用。某些系统只在任务开始时检索一次；某些系统会间歇或连续检索；某些系统只做轻量日志；某些系统会做复杂抽取、压缩和重组。因此 short-term / long-term memory 不是离散模块，而是这些算子在不同时间尺度和频率下被调用产生的现象。

从 agent loop 角度看，整体过程可以概括为：

1. observe environment；
2. optionally retrieve memory；
3. compute action with LLM policy；
4. receive feedback；
5. optionally form and evolve memory。

这为后文 Dynamics 章节提供了直接基础。

#### 2.3 Agent Memory 与相关概念的边界

Section 2.3 处理概念边界。作者指出，agent memory、LLM memory、RAG、context engineering 都涉及信息管理和利用，但它们的研究对象、时间尺度和功能角色不同。

Figure 2 的作用是展示四个概念的交叉关系。图中列出 KV reuse、graph retrieval、agentic RAG、tool-integrated reasoning 等共享技术，但作者强调：agent memory 的独特性在于维护一个 persistent and self-evolving cognitive state，即一个会跨任务积累事实和经验、并随交互演化的认知状态。

![Figure 2](../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564/figures/source_figure_002_concept-comparison.png)

#### 2.3.1 Agent Memory vs. LLM Memory

作者认为，很多早期所谓 “LLM memory” 工作，在今天更适合被理解为 agent memory 的早期实例。原因是 2023-2024 年社区对 LLM agent 的定义还不稳定，有时能调用计算器就被称为 agent，有时则要求 planning、tool-use、memory、reflection 等完整能力。因此像 MemoryBank、MemGPT 这类系统，当时叫 LLM memory，但本质上是在解决 agentic 问题：跟踪用户偏好、维持对话状态、跨多轮交互积累经验。

但 LLM memory 并不完全等于 agent memory。真正属于 LLM-internal memory 的方向包括 KV cache 管理、long-context architecture、RWKV/Mamba 这类架构、attention sparsity、recurrent state persistence 等。这些工作关注的是模型内部表示能力和长上下文处理，不一定涉及 agent 与环境交互，也不一定维护跨任务演化的 memory base。

可以概括为：


| 类别             | 更接近 agent memory                    | 更接近 LLM memory                            |
| ------------------ | ---------------------------------------- | ---------------------------------------------- |
| 目标             | 支持 agent 决策、经验积累、跨任务适应  | 扩展或重组模型内部表示能力                   |
| 典型对象         | 用户偏好、对话状态、任务经验、环境反馈 | KV cache、长上下文、模型架构、attention 状态 |
| 时间尺度         | inside-trial 和 cross-trial 都可能存在 | 通常集中在单次序列或模型内部状态             |
| 是否强调环境交互 | 是                                     | 不一定                                       |

#### 2.3.2 Agent Memory vs. RAG

Agent memory 和 RAG 的重叠很大，因为二者都使用外部信息存储、索引、语义检索、graph retrieval、context expansion 等技术。尤其是 agentic RAG 出现后，二者边界进一步模糊。

作者给出的核心区分是：经典 RAG 主要从外部、相对静态的知识源中检索信息，用于增强单次 inference；agent memory 则嵌入 agent 与环境的持续交互中，会把 agent 自己的 action、反馈和经验写入 persistent memory base。

更实用的区分方式是看 task domain 和 evaluation setting：


| 维度            | RAG                                               | Agent Memory                                         |
| ----------------- | --------------------------------------------------- | ------------------------------------------------------ |
| 信息来源        | 外部文档、知识库、大规模语料                      | agent 自身交互、历史任务、环境反馈，也可包含外部知识 |
| 典型目标        | grounding、减少 hallucination、知识密集任务准确率 | 多轮持续交互、时间依赖、环境适应、经验积累           |
| 典型评测        | HotpotQA、2WikiMQA、MuSiQue 等知识密集 QA         | LoCoMo、LongMemEval、GAIA、SWE-bench、StreamBench 等 |
| memory 是否演化 | 通常不是核心                                      | 是核心                                               |

作者进一步用 RAG taxonomy 说明重叠区域：

- Modular RAG：在 agent memory 中对应 retrieval stage，例如 vector search、semantic matching、rule-based filtering。
- Graph RAG：在 agent memory 中对应 graph-structured memory，用于记录概念、子任务依赖、因果关系等可演化经验结构。
- Agentic RAG：与 agent memory 最接近，因为两者都让 agent 自主决定何时、如何、检索什么。区别是 agentic RAG 通常面向外部或任务特定数据库，而 agent memory 强调内部、持久、自演化的 memory base。

#### 2.3.3 Agent Memory vs. Context Engineering

作者认为 agent memory 和 context engineering 不是包含关系，而是两个操作范式的交集。

Context engineering 把 context window 当作受限计算资源，目标是优化输入 payload，包括 instructions、knowledge、state、memory 等，使模型在有限上下文中高效推理。它关注的是 resource management。

Agent memory 关注的是 persistent cognitive state，即 agent 经过长期交互后知道什么、经历过什么、如何变化。它关注的是 cognitive modeling。

二者在 working memory 和 long-horizon interaction 中有明显重叠。例如 token pruning、importance selection、rolling summary、dynamic retrieval、recursive state update 等技术，既可以被看作 context engineering，也可以被看作短期 agent memory 的实现。

但二者目标不同：


| 维度     | Context Engineering                      | Agent Memory                                                     |
| ---------- | ------------------------------------------ | ------------------------------------------------------------------ |
| 核心问题 | 如何把信息有效放进 context window        | agent 知道什么、经历过什么、如何随时间演化                       |
| 主要关注 | 格式、调度、压缩、工具调用接口、通信协议 | factual knowledge、experiential traces、working memory、参数内化 |
| 时间尺度 | 更偏当前推理或当前交互窗口               | 可跨任务、跨 episode 持续存在                                    |
| 作用层级 | 外部 scaffolding / interface layer       | 内部 cognitive substrate                                         |

这一小节的关键结论是：context engineering 优化 agent 和模型之间的瞬时接口，而 agent memory 维持超越单个 context window 的持续认知状态。

#### 本章小结

Section 2 建立了本文后续分类的理论底座。作者把 agent 定义为一个会观察环境、可选检索 memory、执行 LLM policy、采取 action、接收反馈并更新 memory 的循环系统；再把 memory 定义为一个可由不同结构实现、并通过 formation/evolution/retrieval 运作的动态状态。

本章最重要的概念区分是：agent memory 的核心不是“能不能检索信息”，而是是否维护一个持久、自演化、能参与 agent 决策的 cognitive state。这个标准把它和 LLM memory、RAG、context engineering 区分开来，也解释了为什么后文要分别讨论 Forms、Functions 和 Dynamics。

### 3 Form: What Carries Memory?

#### 本章作用

Section 3 回答 `Forms` 这一维度的问题：agent memory 到底由什么承载。作者不是按用途分类，而是按 memory 存在的位置和表示形式分类。这个角度关注的是 memory 的物理/结构载体：它是显式 token 记录，是模型参数中的统计模式，还是模型内部连续隐状态。

作者提出三种主要 memory form：


| Memory form        | 核心含义                                                                | 主要特征                                                     |
| -------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Token-level memory | 外部可见、离散、可访问的 memory 单元                                    | 可解释、可编辑、易检索，常见于文本片段、向量库、图、表、轨迹 |
| Parametric memory  | 写入模型参数或附加参数模块中的 memory                                   | 隐式、抽象、泛化性强，但更新成本高                           |
| Latent memory      | 存在于 hidden states、KV cache、latent embeddings 等连续表示中的 memory | 高压缩、高效率、机器原生，但可解释性弱                       |

这章的核心观点是：不同 memory form 决定了 agent 如何存储、更新、检索信息，也决定了它适合什么任务。后面的 Function 和 Dynamics 都需要建立在这个结构基础上。

#### 3.1 Token-level Memory

Token-level memory 是最常见、最直观的一类。这里的 token 不是狭义的 tokenizer token，而是任何可以被写入、检索、重组、修改的离散单元，包括文本片段、视觉 token、音频帧、轨迹、用户画像、经验记录、向量条目等。

它的优势是外部可见、可解释、容易编辑，因此适合 retrieval、routing、conflict handling，以及和 parametric / latent memory 协同。缺点是如果缺少结构，记忆容易堆积成噪声，检索质量会成为瓶颈。

作者按 token-level memory 的拓扑结构复杂度分成三类。

![Figure 3](../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564/figures/source_figure_003_token-level-taxonomy.png)


| 类型                     | 结构                           | 典型用途                                     | 主要问题                         |
| -------------------------- | -------------------------------- | ---------------------------------------------- | ---------------------------------- |
| Flat Memory (1D)         | 无显式拓扑，线性序列或独立条目 | 对话历史、用户画像、经验池、多模态片段       | 依赖检索质量，难以表达关系和层级 |
| Planar Memory (2D)       | 单层图、树、表或关系结构       | 知识图谱、时间线、实体关系、任务依赖         | 结构构建和维护成本更高           |
| Hierarchical Memory (3D) | 多层结构，存在跨层连接         | 多粒度摘要、社区图、分层任务图、长期知识组织 | 检索和布局复杂，维护难度最高     |

#### 3.1.1 Flat Memory (1D)

Flat memory 把信息存成离散单元集合，不显式建模条目之间的语义关系或结构依赖。常见存储对象包括 text chunks、user profiles、experience trajectories、vector embeddings、multimodal entries。

作者把 flat memory 的代表方向组织为几类：

- Dialogue memory：保存原始对话、摘要、用户 profile、长对话状态。早期目标主要是防止遗忘和扩展上下文，例如 MemGPT 用类似操作系统的方式区分 active context 和 external storage。
- Preference memory：建模用户偏好、兴趣和决策模式，常见于推荐系统和个性化交互。
- Profile memory：维护稳定用户画像、角色属性或长期身份信息，用于跨任务的一致行为。
- Experience memory：存储任务轨迹、chain of thought、动作序列、环境反馈。进一步可以抽象为 workflows、rules、thought templates、可执行技能或工具使用经验。
- Multimodal memory：把图像、视频帧、音频片段、传感器数据等转成离散记忆单元，用于 video understanding、AR、embodied navigation 等场景。

Flat memory 的优势是简单、可扩展、易追加和删除，可以配合 similarity search 做灵活检索，适合快速变化的交互历史和大范围 recall。它的限制是没有显式关系结构，随着 memory 增长会出现冗余、噪声和上下文碎片化。模型可能检索到相关条目，但不知道条目之间如何关联，因此在组合推理、长程规划、抽象形成方面受限。

#### 3.1.2 Planar Memory (2D)

Planar memory 在 memory units 之间加入显式拓扑，但只在单一结构层内组织。这个拓扑可以是 graph、tree、table 或隐式连接结构，用来表达 adjacency、parent-child ordering、semantic grouping 等关系。

它的关键变化是从“存储”走向“组织”。相比 flat memory，planar memory 不只保存信息，还保存信息之间的关系。

作者主要讨论两类结构：

- Tree：适合层级摘要、coarse-to-fine retrieval、长对话分段和抽象。例如把长交互切成片段，再逐层聚合为更高层概念。
- Graph：适合复杂关联、因果、时间动态和实体关系，是 2D memory 的主流形式。它可以表示用户偏好图、query memory、timeline graph、persona graph、entity-centric multimodal graph、navigation graph 等。

Planar memory 的优势是能支持结构化检索和关系推理。例如在对话、KGQA、导航、医学 QA、embodied QA 等任务中，graph/tree 能让 agent 不只找“相似条目”，还能沿关系边找到相关实体、事件、因果或步骤依赖。限制是结构需要持续构建、更新和纠错；如果关系抽取错误，后续推理会被系统性误导。

#### 3.1.3 Hierarchical Memory (3D)

Hierarchical memory 在多个层级之间组织 memory，形成跨粒度、跨抽象层的结构。它不只是单层图或树，而是 raw documents、chunks、summaries、QAs、communities、semantic/episodic layers 等多层表示之间存在连接。

这种设计适合需要多粒度知识组织的场景。例如 GraphRAG 的 multi-level community graph indices 可以从底层实体/关系聚合到高层 community summary；HiAgent 的 goal graphs 可以支持 recursive clustering；HippoRAG 和 Zep 等系统也通过不同形式的 graph 或 temporal knowledge graph 组织长期记忆。

Hierarchical memory 的优势是能同时支持局部细节检索和全局摘要推理，对长文档、多事件、多任务历史尤其有价值。它的问题是结构复杂，检索路径和跨层布局设计困难；如果层级划分不合理，可能导致检索效率下降或语义失真。

#### 3.2 Parametric Memory

Parametric memory 和 token-level memory 相反，它不把 memory 存成外部可见条目，而是写入模型参数或附加参数模块。它的基本思想是：让模型在 forward computation 中隐式调用这些信息，而不需要显式检索外部存储。

作者按 memory 相对核心模型参数的位置分为两类：


| 类型                       | 存储位置                                            | 更新方式                                        | 主要优点                            | 主要问题                               |
| ---------------------------- | ----------------------------------------------------- | ------------------------------------------------- | ------------------------------------- | ---------------------------------------- |
| Internal parametric memory | 原始模型参数，如 weights、biases                    | pre-train、mid-train、post-train、model editing | 无额外推理模块，泛化性强            | 更新困难，成本高，容易遗忘或影响旧知识 |
| External parametric memory | adapter、LoRA、proxy model、auxiliary LM 等附加参数 | 模块化训练、路由、替换                          | 可插拔，可回滚，较少干扰 base model | 需要和模型内部表示流良好对接           |

#### 3.2.1 Internal Parametric Memory

Internal parametric memory 把知识、经验或任务先验直接注入 base model 参数。作者把注入时机分为 pre-train、mid-train、post-train。

- Pre-train：在预训练阶段让模型学会更好地存储或使用知识，也包括提升长窗口能力。
- Mid-train / continued pre-training：注入可泛化的下游任务经验，例如 tool calling、deep research、embodied simulation 等 agent experience。
- Post-train：面向特定下游任务进行个性化、角色、知识编辑或安全行为注入，例如 character fine-tuning、model editing、detoxification。

这种方式的优点是结构简单，不增加额外推理开销或部署模块；模型可以直接用参数化知识进行流畅推理。缺点是更新困难，需要训练或编辑参数，成本高，也容易产生 catastrophic forgetting 或误伤相邻知识。因此它更适合大规模领域知识、任务先验、稳定风格或行为模式，不适合频繁变化的短期个性化 memory。

#### 3.2.2 External Parametric Memory

External parametric memory 是一种折中方案：不直接修改原始 LLM 参数，而是在 frozen base model 外部增加参数模块来承载 memory。

主要方向包括：

- Adapter-based modules：如 MLP-Memory、K-Adapter、WISE、ELDER、LoRA modules 等。它们把新知识或编辑知识放在附加参数空间中，并通过 routing 或 blending 决定何时使用。
- Auxiliary LM-based modules：如 MAC、Retroformer 等，把 memory 存在单独模型或外部知识模块中，再影响主模型推理。

这种方法的优势是模块化、可替换、可回滚，能缓解直接修改 base model 导致的干扰和遗忘。限制是外部参数必须能有效接入模型内部计算路径，memory 注入效果取决于接口设计、路由机制和表示兼容性。

#### 3.3 Latent Memory

Latent memory 位于 token-level memory 和 parametric memory 之间。它不以可读文本或结构化条目存在，也不一定固化进模型参数，而是存在于模型内部连续表示中，例如 hidden states、KV cache、latent embeddings、memory tokens、summary vectors。

![Figure 4](../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564/figures/source_figure_004_latent-memory.png)

作者按 latent state 的来源分成三类：


| 类型      | 含义                                       | 典型形式                                                                |
| ----------- | -------------------------------------------- | ------------------------------------------------------------------------- |
| Generate  | 生成新的 latent representation 作为 memory | gist tokens、summary vectors、memory tokens、trajectory embeddings      |
| Reuse     | 直接复用模型已有内部状态                   | KV cache、past hidden states、memory-attention KV                       |
| Transform | 对已有 latent state 做压缩、筛选、重组     | pruned KV、aggregated prefix KV、layer-wise budget、compensation tokens |

#### 3.3.1 Generate

Generate 型 latent memory 会通过模型或辅助 encoder 生成新的紧凑连续状态，用来替代长原始输入或保留任务状态。这些状态可以是 special tokens、soft tokens、summary vectors、matrix slots、LoRA fragments、multimodal embeddings 等。

单模态方向通常服务 long-context processing 和 language modeling，例如把长 prompt 压缩成 gist tokens、sentinel tokens、summary vectors 或 persistent memory tokens。多模态方向则把 GUI 轨迹、视频 patch、视觉观察、embodied perception 等压缩成 latent embeddings。

优点是信息密度高，能减少反复处理完整上下文的成本，适合长上下文、多模态和跨 episode 信息保留。缺点是生成过程可能有信息损失或偏差，长期读写可能累积漂移；同时需要额外训练模块或复杂工程。

#### 3.3.2 Reuse

Reuse 型 latent memory 不生成新表示，也不压缩修改，而是直接复用模型内部 activation，主要是 KV cache。代表思路是把历史 forward pass 中的 KV pairs 存起来，并在后续 inference 中通过 KNN 或 memory-attention 检索。

这种方法的优势是保留原始内部激活的高保真信息，没有额外压缩损失，也容易接入 Transformer 类模型。缺点是 KV cache 随上下文长度快速增长，存储和检索成本高；效果高度依赖索引和筛选策略。

#### 3.3.3 Transform

Transform 型 latent memory 把已有 latent state 作为可变记忆单元，通过 selection、aggregation、compression、projection 等方式重组。它既不是重新生成新表示，也不是原样复用 raw KV cache，而是在二者之间做压缩和结构调整。

典型方法包括：

- 按 attention score 或 token importance 保留关键 tokens；
- 聚合 prefix KV representations；
- 在不同层之间重新分配 KV budget；
- 用 compensation tokens 保留被丢弃条目的信息；
- 根据 heavy hitter tokens 或 entropy 选择重要内容。

优点是显著降低存储成本，让 long-context reasoning 更高效；缺点是压缩和筛选会带来信息损失，且压缩后的 latent state 更难解释和验证。

#### 3.4 Adaptation

Section 3.4 讨论如何根据任务选择 memory form。作者强调，选择 memory 类型不是简单组合问题，而是在表达“希望 agent 如何利用信息影响行为”。

![Figure 5](../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564/figures/source_figure_005_memory-paradigms.png)

本节可整理为如下选择原则：


| Memory form        | 适合场景                                                                       | 不适合或风险                                 |
| -------------------- | -------------------------------------------------------------------------------- | ---------------------------------------------- |
| Token-level memory | 多轮对话、长期 agent、用户画像、推荐、企业知识库、法律/金融/医疗等高可追溯场景 | 检索噪声、冗余积累、结构化推理不足           |
| Parametric memory  | 角色扮演、数学/代码/游戏、行为风格、领域专家响应、人类偏好和规范先验           | 更新慢，难回滚，可能 catastrophic forgetting |
| Latent memory      | 多模态 agent、端侧/边缘部署、隐私敏感场景、高压缩高吞吐推理                    | 可解释性弱，验证困难，可能信息损失           |

作者的总体建议是：需要透明、可审计、频繁更新时优先 token-level；需要抽象泛化和深层行为模式时考虑 parametric；需要高效率、紧凑表示、多模态融合或隐私保护时考虑 latent。

#### 本章小结

Section 3 通过 memory 的承载形式建立了全文第一条主轴。它说明 agent memory 不是单一结构，而是至少有三种不同工程形态：外部可读的 token-level memory、模型参数中的 parametric memory、内部连续表示中的 latent memory。

这三类 memory 不是互斥关系。实际 agent 系统经常组合使用：token-level memory 负责可解释长期存储，parametric memory 负责稳定知识和行为模式，latent memory 负责高效上下文压缩和内部状态复用。后续 Section 4 会从“这些 memory 服务什么功能”继续展开。

### 4 Functions: Why Agents Need Memory?

#### 本章作用

Section 4 从 `Functions` 维度回答“agent 为什么需要 memory”。如果 Section 3 讨论 memory 由什么承载，那么 Section 4 讨论 memory 在 agent 行为中承担什么功能。作者的出发点是：LLM 从 stateless text processor 变成 autonomous goal-directed agent，不是简单能力增强，而是范式变化。Agent 必须能持续存在、适应环境、跨时间保持一致行为，因此单纯扩大 context window 不够，必须有功能化的 memory。

作者把 memory function 分成三个支柱：factual memory、experiential memory、working memory。它们分别回答三个问题：agent 知道什么，agent 如何改进，agent 当前在想什么。

![Figure 6](../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564/figures/source_figure_006_functional-taxonomy.png)


| Function            | 时间属性   | 回答的问题                            | 核心作用                                             |
| --------------------- | ------------ | --------------------------------------- | ------------------------------------------------------ |
| Factual Memory      | Long-term  | What does the agent know?             | 保存事实、用户偏好、环境状态，保证一致性和上下文感知 |
| Experiential Memory | Long-term  | How does the agent improve?           | 从成功/失败轨迹中抽象经验、策略、技能，实现持续学习  |
| Working Memory      | Short-term | What is the agent thinking about now? | 在当前任务或会话内维护受限工作空间，管理当前推理状态 |

作者强调这三类 memory 不是孤立模块，而是构成 agent 的 cognitive loop。交互结果会通过 summarization、reflection、abstraction 写入长期 memory；当前推理发生在 working memory 中；working memory 又通过 retrieval 从 factual 和 experiential memory 中取回相关事实和技能。

#### 4.1 Factual Memory

Factual memory 是 agent 保存和检索显式 declarative facts 的能力，包括历史事件、用户信息、外部环境状态、对话历史、用户偏好和世界属性。它的核心功能是让 agent 在当前输入之外利用历史事实，从而实现 context awareness、personalization 和 extended task planning。

作者借用认知科学中的 declarative memory 概念，但没有机械套用 episodic / semantic 的二分。在 agent 系统中，factual memory 更像一个处理连续体：系统先记录具体交互历史，例如 dialogue turns、user actions、environment states；再通过 summarization、reflection、entity extraction、fact induction 等过程，把原始事件流转成可复用的 semantic fact base。

Factual memory 支撑三个交互属性：


| 属性         | 含义                                                         |
| -------------- | -------------------------------------------------------------- |
| Consistency  | 行为和自我呈现随时间稳定，避免与过去承诺或用户事实矛盾       |
| Coherence    | 能引用历史上下文，保持话题连续，避免每轮回答像孤立 utterance |
| Adaptability | 根据用户 profile 和历史反馈调整响应风格与决策                |

作者进一步按事实指向的实体，把 factual memory 分成 user factual memory 和 environment factual memory。

#### 4.1.1 User Factual Memory

User factual memory 保存关于特定用户的可验证事实，包括身份、偏好、日常习惯、历史承诺、显著事件等。它主要解决 stateless interaction 的典型问题：coreference drift、重复询问、前后矛盾、长期目标被打断。

作者将 user factual memory 的功能分成两类。

第一类是 dialogue coherence。系统需要保留对话上下文、用户事实和稳定 persona，使后续回复能利用早期披露的信息和情绪线索，而不是反复要求用户说明。实现上通常包括两种策略：

- heuristic selection：根据 relevance、recency、importance、distinctiveness 等分数选择和排序历史条目；
- semantic abstraction：把原始对话片段转成 thought representations、reflections 或 compact user profiles，使 agent 查询的是稳定语义记忆，而不是原始 token 表面形式。

第二类是 goal consistency。Agent 需要持续维护任务表示，记录哪些约束已确认、哪些信息仍缺失、当前目标是什么。这样 clarifying questions、retrieval 和 actions 才不会偏离原始任务。在 embodied 场景中，这类 memory 还会保存家庭成员、物体位置、用户 routine 等事实，从而减少重复探索和重复指令。

#### 4.1.2 Environment Factual Memory

Environment factual memory 指向用户之外的外部实体和状态，例如长文档、代码库、工具、其他 agent、资源可用性、环境交互轨迹等。它的目标是给 agent 提供一个可更新、可检索、可治理的外部事实层。

作者把它分成两类。


| 类型                  | 作用                                                                             | 例子                                                                 |
| ----------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Knowledge Persistence | 持久保存世界知识和领域知识，支持长文档分析、事实 QA、多跳推理、代码/数据资源检索 | knowledge graph、dynamic tree、external DB、model editing memory     |
| Shared Access         | 为 multi-agent 协作提供共同事实基础，减少重复工作，维持目标和中间产物一致        | shared repository、collaborative workspace、social simulation memory |

这一节的关键点是：environment factual memory 不只是“知识库检索”。如果它能随环境变化更新、能被 agent 操作、能在任务阶段之间保持引用稳定，它就成为 agent memory 的一部分。

#### 4.2 Experiential Memory

Experiential memory 保存的是 procedural and strategic knowledge，来源于过去任务轨迹、失败、成功和反馈。它回答的问题不是“agent 知道什么事实”，而是“agent 如何通过经验变得更好”。

作者按抽象层次把 experiential memory 分成四类：case-based、strategy-based、skill-based、hybrid。

![Figure 7](../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564/figures/source_figure_007_experiential-memory.png)


| 类型                  | 保存内容                                       | 作用                                 |
| ----------------------- | ------------------------------------------------ | -------------------------------------- |
| Case-based Memory     | 具体过去案例、轨迹、成功/失败样例              | 遇到相似问题时检索和复用案例         |
| Strategy-based Memory | 从案例中抽象出的策略、规则、workflow、insights | 跨任务迁移经验，减少对具体案例的依赖 |
| Skill-based Memory    | 可执行函数、代码库、工具调用程序、API/MCP 操作 | 把经验编译成可直接执行的能力         |
| Hybrid Memory         | 同时维护 case、strategy、skill 等多层经验      | 支持从案例到策略再到技能的演化       |

#### 4.2.1 Case-based Memory

Case-based memory 保存具体历史案例，例如 solution traces、action trajectories、environment feedback、失败/成功样例。它适合相似任务复用：当前问题来了以后，agent 检索相似案例，把过去解决路径作为参考。

优点是保真度高，能保留上下文细节；缺点是泛化有限。如果任务和历史案例不够相似，直接复用轨迹可能无效，甚至误导当前决策。

#### 4.2.2 Strategy-based Memory

Strategy-based memory 从具体案例中抽象出更高层的 rules、workflows、patterns、reasoning strategies。相比 case-based memory，它不依赖具体场景复现，而是保存可迁移的经验。

这种 memory 常见于 self-reflection、workflow abstraction、reasoning bank、thought templates 等方向。它的优势是可跨任务迁移，能让 agent 不只记住“上次怎么做”，而是记住“遇到这类问题应该怎么做”。风险是抽象过度后可能丢失关键条件，形成过泛化策略。

#### 4.2.3 Skill-based Memory

Skill-based memory 把经验进一步编译成可执行能力，例如函数、代码片段、工具调用模式、MCP/API 操作、可复用程序库。相比 strategy-based memory 的文本策略，skill-based memory 更接近可操作 artifact。

这类 memory 对 coding、tool use、embodied task、game agent 很重要。它能显著降低重复探索成本，把过去成功经验变成未来可以直接调用的能力。限制是需要维护技能的正确性、适用条件和版本；如果环境变化，旧技能可能失效。

#### 4.2.4 Hybrid Memory

Hybrid memory 同时维护 case、strategy、skill 等不同抽象层次。作者提到，一些系统会把成功案例逐步抽象成策略，再进一步编译成技能，实现从 heavy retrieval 到 rapid execution 的转变。

这类系统更接近完整 cognitive architecture：case 提供细节，strategy 提供迁移能力，skill 提供执行效率。它的问题是 lifecycle 更复杂，需要决定什么时候保留案例、什么时候抽象、什么时候编译成技能，以及如何在失败后回滚或更新。

#### 4.3 Working Memory

Working memory 是 agent 在单次任务或会话中的 active workspace。作者借用认知科学定义：working memory 是容量受限、动态控制的机制，用来选择、维持、转换当前任务相关信息。它不是临时存储的同义词，而是对当前上下文的主动管理。

作者指出，LLM 的 context window 本质上更像被动 read-only buffer。模型可以读上下文，但没有内建机制主动选择、维持、重写当前 workspace。因此需要显式设计 working memory。

作者把 working memory 分成两类。


| 类型                       | 核心问题                                              | 典型机制                                                      |
| ---------------------------- | ------------------------------------------------------- | --------------------------------------------------------------- |
| Single-turn Working Memory | 单次 forward pass 中输入太大，如何构建有限 scratchpad | input condensation、observation abstraction                   |
| Multi-turn Working Memory  | 多轮交互中历史不断增长，如何维持任务状态和时间连续性  | state consolidation、hierarchical folding、cognitive planning |

#### 4.3.1 Single-turn Working Memory

Single-turn working memory 处理的是“当前输入过大”的问题，例如长文档、高维多模态流。目标不是被动塞进全部上下文，而是主动构建一个 writable workspace，提高固定 attention budget 下的信息密度和可操作性。

作者分成两类机制：

- Input condensation：压缩物理 token 数量。Hard condensation 基于重要性指标选择 token；soft condensation 把上下文编码成 dense latent vectors 或 memory slots；hybrid 方法结合两者。
- Observation abstraction：把原始观察转成结构化语义表示。例如把 HTML DOM 重写为任务相关状态摘要，把视频流转成事件描述或视觉特征库。

Single-turn working memory 的价值是提高当前推理的输入密度，但它本质上解决的是静态输入复杂度，不负责长期时间连续性。

#### 4.3.2 Multi-turn Working Memory

Multi-turn working memory 处理长程交互中的状态维护问题。即便 context window 很长，历史持续累积也会带来 attention saturation、latency 增加和 goal drift。因此 multi-turn working memory 要作为外部 state carrier，通过 read-evaluate-write 循环维护关键状态。

作者分成三类机制：


| 机制                 | 含义                                                                           |
| ---------------------- | -------------------------------------------------------------------------------- |
| State Consolidation  | 把不断增长的 trajectory 映射到固定大小状态，通过动态更新保留关键状态并丢弃冗余 |
| Hierarchical Folding | 按 subgoal 分解任务，活跃子任务保留细节，完成后折叠成摘要                      |
| Cognitive Planning   | 把计划或世界模型作为 working memory 核心，使 agent 能维持目标一致性并修正策略  |

这一节的关键结论是：multi-turn working memory 的目标不是保存 raw history，而是构建可操作 state carrier，使 agent 的推理能力不随交互长度线性退化。

#### 本章小结

Section 4 给出了全文第二条主轴：memory 的功能。Factual memory 维护事实和一致性，experiential memory 支持经验积累和自我改进，working memory 管理当前推理和交互状态。

这一章的关键价值是把 memory 从“存储什么”推进到“服务什么”。同一个 memory form 可以承担不同 function；例如 token-level memory 既可以保存 user facts，也可以保存 task trajectories 或 working summaries。后续 Section 5 会继续解释这些 memory 如何形成、演化和检索。

### 5 Dynamics: How Memory Operates and Evolves?

#### 本章作用

Section 5 是全文第三条主轴：`Dynamics`。如果 Section 3 回答 memory 由什么承载，Section 4 回答 memory 为什么有用，那么 Section 5 回答 memory 如何在 agent 运行过程中被形成、维护和使用。

作者在这里强调一个关键差别：agent memory 不是固定数据库，也不是把历史全部 append 到一个向量库里。真正的 agentic memory system 应该能根据交互轨迹和环境反馈抽取新 memory，把新旧 memory 融合、修正、遗忘，并在推理需要的时刻精确检索。这个动态闭环是 agent 从 stateless generator 变成 lifelong/self-evolving system 的核心。

![Figure 8](../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564/figures/source_figure_008_memory-dynamics.png)

作者把 memory lifecycle 拆成三个基本过程：


| 过程             | 回答的问题                 | 核心含义                                                                                       |
| ------------------ | ---------------------------- | ------------------------------------------------------------------------------------------------ |
| Memory Formation | How to extract the memory? | 从 raw interaction、reasoning trace、environment observation 中抽取信息密度更高的 memory units |
| Memory Evolution | How to refine the memory?  | 将新 memory 与已有 memory repository 融合、更新、遗忘，使 memory 保持一致、紧凑、有效          |
| Memory Retrieval | How to utilize the memory? | 在合适时刻构造 task-aware query，从合适的 memory module 中取回对当前推理真正有用的信息         |

这三个过程不是线性 pipeline，而是闭环。Formation 生成新 memory，Evolution 把它整合进 memory base，Retrieval 在推理时调用 memory；推理结果和环境反馈又会回到 Formation 和 Evolution，形成持续自我改进。

#### 5.1 Memory Formation

Memory formation 指把原始上下文编码成 compact knowledge。它的必要性来自 raw context 的三个问题：长度大、噪声多、冗余高。直接把所有历史塞进 prompt 会带来计算成本、显存开销和长上下文 OOD 退化。因此 memory system 需要先把原始数据转成更适合保存和检索的表示。

作者把 formation 分为五类：


| Formation 类型             | 输出形态                                  | 主要作用                                   | 典型风险                                                       |
| ---------------------------- | ------------------------------------------- | -------------------------------------------- | ---------------------------------------------------------------- |
| Semantic Summarization     | 摘要、profile、story、task flow           | 压缩长上下文，保留全局语义                 | 有损压缩，细节和证据可能被抹平                                 |
| Knowledge Distillation     | factual facts、experiential insights      | 抽取可复用事实和经验                       | 依赖抽取 prompt / model 能力，可能漏掉细粒度条件               |
| Structured Construction    | KG、tree、hierarchical graph              | 显式组织实体、关系、层级，支持多跳推理     | schema 僵硬，构建和维护成本高                                  |
| Latent Representation      | embeddings、KV states、latent tokens      | 用机器原生表示保存高密度语义和多模态信息   | 不透明，难以 debug、编辑、审计                                 |
| Parametric Internalization | model weights、adapter、edited parameters | 把外部 knowledge/capability 内化为模型能力 | 更新成本高，可能 catastrophic forgetting 或 off-target effects |

##### 5.1.1 Semantic Summarization

Semantic summarization 是把长序列压成语义摘要。它关注的是 global/high-level semantics，而不是严格保留每个事实细节。典型输出包括文档总体叙事、任务流程、用户长期 profile 等。

作者分成两类：


| 类型                      | 机制                                                            | 优点                                 | 局限                                         |
| --------------------------- | ----------------------------------------------------------------- | -------------------------------------- | ---------------------------------------------- |
| Incremental summarization | 新 chunk 到来后和已有 summary 合并，形成持续演化的摘要          | 支持流式交互，避免全序列处理的高成本 | 串行更新有瓶颈，容易累积错误、遗忘或语义漂移 |
| Partitioned summarization | 按 session、chapter、topic cluster、video clip 等分区后分别摘要 | 效率更高，能保留更细粒度语义         | 分区之间的依赖可能丢失                       |

这一类方法的本质是 lossy compression。它适合长期对话、长文档浏览、视频叙事压缩等场景，但不适合要求精确证据的任务；因为摘要越抽象，越可能丢失少数但关键的细节。

##### 5.1.2 Knowledge Distillation

Knowledge distillation 比 summarization 更细粒度。它不是只提炼“这段历史大概讲了什么”，而是从交互轨迹或文档中抽取可复用的认知资产。这里的 knowledge 对应 Section 4 的 functional memory，主要包括 factual memory 和 experiential memory。

Factual memory distillation 把原始对话、文档、多模态观察转成显式可验证事实。例如用户偏好、目标约束、环境状态、物体位置、日常 routine、视频中的对象和事件。这类 memory 的目标是维持 consistency 和 adaptability。

Experiential memory distillation 从历史任务轨迹中抽取策略。它可以来自成功案例，例如总结成功规划路径；也可以来自失败反思，例如定位错误来源并抽取 correction insight；还可以同时比较成功和失败轨迹，得到更完整的 planning principles。作者特别指出，已有工作多偏 task-level insight，细粒度 step-level insight 仍然不足。

这一类方法的价值是直接服务 agent 改进：不仅记住事实，还记住“遇到类似任务应该怎么做”。但它仍然常常产出 flat memory units，如果不进一步结构化，多个 memory item 之间的层级和依赖关系会被忽略。

##### 5.1.3 Structured Construction

Structured construction 把无结构数据组织成显式拓扑结构，例如 knowledge graph、tree、hierarchical graph。作者强调这不只是存储格式变化，而是 memory formation 的一种主动结构化操作：系统要决定哪些信息被链接、哪些信息被分层、哪些关系可供后续检索和推理使用。

作者按结构构建粒度分成两类：


| 类型                      | 基本单位                  | 代表结构                                                        | 适合的问题                                     |
| --------------------------- | --------------------------- | ----------------------------------------------------------------- | ------------------------------------------------ |
| Entity-level construction | entity / relation triples | semantic graph、episodic graph、temporal graph、community graph | 事实关系、多跳推理、时间约束、实体中心查询     |
| Chunk-level construction  | text chunk / memory item  | tree、cluster graph、dynamic hierarchy                          | 长文档组织、trajectory memory、跨 session 归纳 |

Entity-level construction 通常先抽取实体和关系三元组，再构建 KG 或多层图。优势是结构清晰，适合精确关系推理；问题是抽取噪声会直接污染图结构。

Chunk-level construction 保留文本片段或 memory item 的局部完整性，再把它们组织成树、簇或动态图。它更适合长文档和 streaming memory。早期方法多是静态树或静态 cluster，后续方法开始支持新 memory 到来后的动态插入、局部重组和层级摘要更新。

这一类方法的核心收益是 explainability 和 multi-hop reasoning，但代价是 schema rigidity 和 maintenance cost。对综述中讨论的 agent memory 来说，这类结构往往是从“存储历史”走向“构建可推理世界模型”的关键一步。

##### 5.1.4 Latent Representation

Latent representation 把经验直接编码进机器原生的连续空间，例如 embeddings、KV-cache、latent tokens。和“先总结成文本再 embedding”不同，latent memory 试图绕开人类可读文本，直接保存更高密度的语义信号。

作者讨论两类：


| 类型                             | 例子                                                                   | 价值                                                        |
| ---------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------- |
| Textual latent representation    | KV-cache reuse、自更新 latent embeddings、latent memory tokens         | 减少重复计算，把 past information 注入 transformer 推理过程 |
| Multimodal latent representation | vision-language tokens、egocentric video embeddings、object embeddings | 统一文本、视觉、空间等多模态 memory 表示                    |

Latent memory 的优势是密度高、适合模型内部计算、多模态对齐自然；缺点也非常明确：不透明。人很难判断 latent memory 里到底存了什么，也难以手工编辑、审计或删除。

##### 5.1.5 Parametric Internalization

Parametric internalization 是把外部 memory 内化进模型参数。它和 latent representation 的区别是：latent memory 通常还是外部或附加的表示，而 parametric internalization 直接改变模型权重、adapter 或可训练模块，使知识或能力变成模型自身的一部分。

作者分成两类：


| 类型                       | 内化对象                                      | 常见机制                                       | 主要问题                                     |
| ---------------------------- | ----------------------------------------------- | ------------------------------------------------ | ---------------------------------------------- |
| Knowledge internalization  | factual knowledge、domain knowledge           | model editing、ROME/MEMIT 类方法、LoRA adapter | off-target effects，难以精确回滚             |
| Capability internalization | procedural expertise、strategy、agentic skill | SFT、DPO、GRPO、从 reasoning traces 学习       | update 成本高，continual learning 下容易遗忘 |

这一类方法的目标是从“检索信息”变成“拥有能力”。好处是零检索延迟，推理时不需要外部 memory lookup；坏处是灵活性差。外部 memory 可以改、删、加版本，参数化 memory 一旦写入模型，精确修改和删除都更困难。

#### 5.2 Memory Evolution

Formation 解决“新 memory 怎么来”，Evolution 解决“新旧 memory 怎么共存”。作者指出，最朴素的 append-only memory bank 会忽略三个问题：memory 之间有语义依赖，memory 之间可能互相矛盾，memory 有时间有效性。因此 memory system 需要主动演化，而不是无限堆积。

![Figure 9](../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564/figures/source_figure_009_memory-evolution.png)

作者把 evolution 分成三类：


| Evolution 机制 | 目标                     | 核心操作                                  |
| ---------------- | -------------------------- | ------------------------------------------- |
| Consolidation  | 让学习累积而不是孤立     | 合并相关 memory，抽象成更高层 insights    |
| Updating       | 维护准确性和时效性       | 发现冲突后修正、替换或标注旧 memory       |
| Forgetting     | 控制容量、噪声和检索成本 | 删除、衰减或压缩过期、低频、低价值 memory |

##### 5.2.1 Consolidation

Consolidation 把短期、碎片化、局部的 traces 组织成稳定的长期知识结构。它的目标不是简单合并文本，而是识别新旧 memory 之间的语义关系，形成更高层 schema 或 insights。

作者按合并范围分成三类：


| 类型                 | 粒度                  | 说明                                                                   |
| ---------------------- | ----------------------- | ------------------------------------------------------------------------ |
| Local consolidation  | 相似 memory fragments | 对高度相似或冗余的条目做局部合并，降低重复、提高精度                   |
| Cluster-level fusion | memory clusters       | 在簇内或簇间融合相关 memory，形成更高阶 reasoning units                |
| Global integration   | 全局历史              | 把长期用户事实、轨迹、反思和工作上下文整合成全局 summary 或 principles |

Consolidation 的收益是 generalization 和 storage efficiency。它让 agent 不只记住单个事件，而能形成可迁移的 schema。风险是 information smoothing：异常案例、少见但重要的细节可能在抽象过程中被抹平。

##### 5.2.2 Updating

Updating 关注 localized correction and synchronization。它和 consolidation 的区别是：consolidation 侧重抽象和泛化，updating 侧重冲突解决和事实修正。新信息到来后，如果它与旧 memory 冲突，系统需要判断是更新旧 memory、保留时间版本，还是把新信息当成噪声。

作者按 memory 所在位置分成两类：


| 类型                   | 更新位置                               | 特点                               |
| ------------------------ | ---------------------------------------- | ------------------------------------ |
| External memory update | vector DB、KG、plain-text memory store | 改外部存储，成本低，支持动态修正   |
| Model editing          | model parameter space                  | 改内部知识，检索开销低，但风险更高 |

External update 的发展路线大致是：早期直接 replace/delete；后来引入 temporal annotation，对冲突事实做 invalid timestamp，而不是硬删除；再后来采用 online soft update + offline reflective consolidation 的 eventual consistency；更进一步则把“何时更新、如何更新、是否更新”建模成学习策略。

Model editing 则是在参数空间内修正知识，包括定位特定事实对应的参数区域并更新，或通过 latent self-updating 机制替换/压缩内部 memory tokens。它的核心难点是 stability-plasticity dilemma：太稳定则无法适应新事实，太可塑则容易覆盖关键知识。

##### 5.2.3 Forgetting

Forgetting 是主动移除、衰减或压缩过期、冗余、低价值 memory。作者强调，遗忘不是失败，而是长期 memory 系统的必要治理机制。否则 memory 会无限膨胀，带来噪声、检索延迟和过时信息干扰。

作者把 forgetting 分成三类：


| 类型                         | 依据                                       | 作用                          | 风险                                            |
| ------------------------------ | -------------------------------------------- | ------------------------------- | ------------------------------------------------- |
| Time-based forgetting        | 创建时间 / 时间衰减                        | 模拟自然遗忘，控制历史膨胀    | 可能删除很久没用但仍重要的信息                  |
| Frequency-based forgetting   | 访问频率 / LRU / LFU                       | 保留常用 memory，提高访问效率 | 长尾知识容易被淘汰                              |
| Importance-driven forgetting | 时间、频率、语义价值、情绪显著性等综合评分 | 更接近任务相关的选择性保留    | 依赖 importance estimator，误判会伤害推理连续性 |

这一节的关键点是：很多系统在存储成本不高时并不会真的硬删除 memory，而是采用软遗忘、归档、降权或压缩。对 agent 来说，forgetting 的设计要比普通 cache eviction 更谨慎，因为 memory 可能承载长期身份、一致性和罕见关键事实。

作者最后还提到更进一步的方向：不仅 memory contents 可以演化，memory architecture 本身也可以演化。例如 meta-evolutionary framework 可以同时优化 agent 的 experiential knowledge 和底层 memory architecture。

#### 5.3 Memory Retrieval

Memory retrieval 是把 Section 5.1/5.2 中构建和维护好的 memory bank，在推理时取出来用。作者把 retrieval 定义为：在合适时刻，从某个 memory repository 中检索相关且简洁的 knowledge fragments，以支持当前 reasoning task。

这一节的重要观点是：retrieval 不是单纯 vector search。一个完整的 agentic memory retrieval pipeline 至少包括四步：什么时候检索、拿什么去检索、怎么检索、检索后怎么处理。


| Retrieval 阶段              | 回答的问题                       | 机制                                                   |
| ----------------------------- | ---------------------------------- | -------------------------------------------------------- |
| Retrieval Timing and Intent | when and where to retrieve       | 判断是否需要检索，以及访问哪个 memory store            |
| Query Construction          | what to retrieve with            | 把用户表层输入改写/拆解成更有效的 retrieval signal     |
| Retrieval Strategies        | how to retrieve                  | lexical、semantic、graph、generative、hybrid retrieval |
| Post-Retrieval Processing   | how to use retrieved information | reranking、filtering、aggregation、compression         |

##### 5.3.1 Retrieval Timing and Intent

Timing 决定什么时候触发检索，Intent 决定访问哪个 memory source。最简单的策略是 always-on retrieval，每次 query 都从所有 memory databases 取回内容。这种方式召回充分，但会引入噪声和成本。

更 agentic 的做法是让模型或 controller 自主判断是否需要检索。早期方法让 LLM 根据 query 调用 memory tool；后续方法引入 fast-slow thinking：先快速回答或初步推理，再评估是否不足，如果不足才触发更深检索。还有方法把 trigger 变成 latent/trainable process，使模型在 rollout state 中学习关键检索时刻。

Intent 方面，系统需要判断检索 plaintext memory、activation memory、parametric memory，还是某个层级 memory store。粗粒度调度可以根据 user/task/org context 选 memory 类型；层级调度则可以从 domain layer 到 episode layer 逐步 narrowing down。

这里的主要风险是 silent failure：agent 过度相信自己的内部知识，没有触发检索，最终 hallucinate。检索触发机制要在“过度检索带来噪声”和“缺失检索导致错误”之间取平衡。

##### 5.3.2 Query Construction

Query construction 是 user utterance 和 memory index 之间的翻译层。直接用用户原始 query 检索很简单，但往往和 memory 的存储语义不匹配。作者总结两类方法：


| 方法                | 机制                                                             | 适用场景                                               |
| --------------------- | ------------------------------------------------------------------ | -------------------------------------------------------- |
| Query decomposition | 把复杂问题拆成多个 sub-queries                                   | 多跳问题、复杂任务、需要分阶段取证的场景               |
| Query rewriting     | 改写原 query，或生成 hypothetical document / draft answer 再检索 | 用户表达和 memory index 语义不对齐、隐含需求较多的场景 |

Decomposition 可以缓解 one-shot retrieval bottleneck。更强的系统会先生成 global retrieval plan，再拆成 sub-queries；还有系统根据 student model 的失败来生成针对性 sub-query。

Rewriting 的典型思想是 HyDE：先让模型生成一个假想答案或文档，再用这个更丰富的语义表示去检索。对 memory system 来说，rewriting 也可以利用 global memory、dialogue context 或澄清树来生成更贴近用户真实意图的 retrieval signal。

这一小节的关键判断是：memory 架构再复杂，如果 query construction 不好，检索仍然会失败。最近工作开始从“设计 memory store”转向“优化 retrieval query 的构造”。

##### 5.3.3 Retrieval Strategies

Retrieval strategy 决定如何从 memory repository 中找到相关内容。作者总结了五类：


| 策略                 | 优点                                                         | 局限                                 |
| ---------------------- | -------------------------------------------------------------- | -------------------------------------- |
| Lexical retrieval    | 快、可解释，适合精确关键词和工具名匹配                       | 捕捉不了语义变体和上下文关系         |
| Semantic retrieval   | 支持 fuzzy matching 和语义泛化，是多数 agent memory 默认选择 | semantic drift、top-K 噪声和虚假召回 |
| Graph retrieval      | 利用实体关系、拓扑路径和时间约束，适合多跳推理               | 依赖图质量，构建和扩展成本高         |
| Generative retrieval | 让模型直接生成相关文档 ID，生成和检索结合紧密                | 需要额外训练，语料变化时扩展性差     |
| Hybrid retrieval     | 融合 lexical、semantic、graph、recency、importance 等信号    | 系统复杂度更高，需要校准各类信号     |

作者对 agent memory 的判断很明确：实际系统通常需要 hybrid retrieval。因为 memory 里的信息类型混杂，有些需要精确匹配工具名或实体，有些需要语义相似，有些需要沿图扩展，有些还要考虑时间、重要性、最近性。

##### 5.3.4 Post-Retrieval Processing

初始检索结果通常包含冗余、噪声、不一致和过长片段。直接塞进 prompt 会导致上下文膨胀、冲突信息干扰和注意力浪费。因此 post-retrieval processing 是 retrieval pipeline 的必要阶段。

作者分成两类：


| 处理方式                    | 作用                                                        |
| ----------------------------- | ------------------------------------------------------------- |
| Re-ranking and Filtering    | 重新估计相关性，移除低价值、过时、不相关 memory，并调整顺序 |
| Aggregation and Compression | 合并多个 fragment，去重、压缩，形成紧凑一致的最终上下文     |

Re-ranking 可以基于 heuristic signals，例如 recency、role relevance、task-stage priority、temporal validity；也可以用 LLM evaluator 或训练出的 auxiliary model 判断某条 memory 是否真的有助于回答。

Aggregation/compression 则把多个检索片段整合成更高级的 context。它不只是减少长度，还要让信息和当前 query、agent role、任务阶段对齐。多 agent 系统里，这一步还可以把通用经验改写成角色特定的 personalized prompt。

#### 本章小结

Section 5 把前两章的静态 taxonomy 接成动态闭环：


| 维度     | 作用                                          |
| ---------- | ----------------------------------------------- |
| Form     | memory 由什么承载                             |
| Function | memory 服务什么 agent 能力                    |
| Dynamics | memory 如何形成、演化、检索并反过来改进 agent |

对实际系统设计来说，本章给出的启发是：agent memory 的瓶颈通常不只是“存不存”，而是 formation quality、evolution governance 和 retrieval precision 三者同时决定。一个系统如果只做向量库存储，没有 consolidation/updating/forgetting，也没有 query construction 和 post-retrieval processing，本质上仍然更接近静态 RAG，而不是完整的 agentic memory。

## 代表性工作矩阵

这篇综述里的多个大表不是普通结果表，而是“领域地图”：作者用表格把方向、memory carrier、memory function、任务场景和代表系统对应起来。读这些表时不需要逐行背所有工作，更重要的是看清楚每个方向现在有哪些典型实现，以及这些实现分别覆盖什么能力边界。

### 按 Memory Form 组织的代表工作

| Form / 方向 | 主要问题 | 代表工作 | 解读重点 |
| --- | --- | --- | --- |
| Token-level flat memory：对话、用户画像、长程 QA | 把历史对话、用户事实、摘要、profile、经验条目作为可检索文本存储 | MemGPT、MemoryBank、Mem0、RMM、MIRIX、LightMem、ComoRAG | 最容易接入闭源 API 和通用 LLM，但质量取决于写入粒度、检索策略和后处理 |
| Token-level experiential memory：轨迹、反思、工作流 | 从历史 episode、成功/失败轨迹中抽取可复用经验 | Reflexion、ExpeL、AgentKB、ReasoningBank、Voyager、LEGOMem、ToolMem | 重点从“记住事实”转向“复用经验”；很多 self-evolving agent 工作落在这里 |
| Token-level multimodal / embodied memory | 把视频、第一视角观察、空间状态、地图和物体状态转成可检索记忆 | Ego-LLaVA、MovieChat、VideoAgent、KARMA、Embodied VideoAgent、Mem2Ego、WorldMM | 多模态 memory 的难点不是只存图像，而是把视觉观察压缩成可检索、可更新的状态 |
| Token-level structured / graph memory | 用图、树、层级结构表达实体关系、事件关系、时间关系和多跳线索 | A-MEM、MemTree、GraphRAG、Zep、HippoRAG、AriGraph、G-Memory、MAGMA | 适合多跳推理、长期知识维护和可解释检索；工程成本高于 flat vector store |
| Parametric internal memory | 把知识、人格、经验或任务先验写入模型原始参数 | StreamingLLM、LMLM、HierMemLM、Agent-Founder、Early Experience、SELF-PARAM、MEND、AlphaEdit | 部署时不需要外部 memory store，但更新成本高，容易遗忘或污染原能力 |
| Parametric external memory | 用 adapter、LoRA、辅助网络或小模型承载记忆 | MLP-Memory、K-Adapter、WISE、ELDER、T-Patcher、Memory Decoder、MemLoRA、Retroformer | 比 internal edit 更模块化，但仍然通常绑定具体模型和训练管线 |
| Latent memory generation | 生成 soft token、summary vector、latent slot 或 persistent token 作为 memory | Gist、AutoCompressor、MemoRAG、MemoryLLM、M+、Titans、MemGen、CoMEM | 优点是压缩率和推理效率，缺点是用户不可直接读写，解释性弱 |
| Latent memory reuse / transform | 复用或压缩 KV cache、hidden state、prefix state 等内部计算状态 | Memorizing Transformers、SirLLM、Memory3、FOT、LONGMEM、SnapKV、PyramidKV、H2O、R3Mem | 更接近模型内部推理优化，需要控制底层模型或推理框架 |

### 按 Memory Function 组织的代表工作

| Function / 子方向 | 主要问题 | 代表工作 | 解读重点 |
| --- | --- | --- | --- |
| Factual memory：用户事实与对话一致性 | 长期记住用户身份、偏好、历史承诺和互动事实 | MemGPT、TiM、MemoryBank、AI Persona、Mem0、RMM、EMem、Memoria | 这是多数产品型 agent 最先需要的 memory；重点是事实更新、冲突处理和隐私 |
| Factual memory：目标一致性与任务约束 | 让 agent 在长程任务中持续遵守目标、约束和历史决策 | RecurrentGPT、Memolet、MemGuide、SGMem、A-MEM、M3-Agent、EverMemOS | 对 web、office、research agent 很重要，因为早期约束会持续影响后续动作 |
| Factual memory：环境知识持久化 | 维护外部世界、文档状态、资源状态、跨 agent 共享事实 | AriGraph、HippoRAG、Zep、MemTree、CAM、MemAct、WISE、MemoryLLM、M+ | 更接近“agent 的可更新世界模型”，通常需要结构化存储或知识图谱 |
| Experiential memory：case-based | 保存原始 solution、trajectory 或 episode，用作示例和 replay | Expel、Synapse、MapCoder、JARVIS-1、MemGen、DreamGym、MemRL | 优点是证据完整，缺点是上下文占用和检索噪声较大 |
| Experiential memory：strategy-based | 把历史经验抽象成 insight、pattern、workflow 或 rule | Reflexion、Buffer of Thoughts、AWM、H2R、ReasoningBank、AgentKB、Dynamic Cheatsheet、MemEvolve | 这是从“保存经历”到“形成方法论”的关键一步，直接支撑跨任务迁移 |
| Experiential memory：skill-based | 把经验编译成可执行代码、函数、API 或 MCP 工具能力 | CREATOR、Gorilla、ToolLLM、Voyager、LEGOMem、Darwin Godel Machine、SkillWeaver、Alita、LearnAct | 更接近 procedural memory，适合工具调用、代码、web 和 embodied control |
| Working memory：input condensation | 在单轮推理里压缩长上下文或冗余输入 | Gist、ICAE、AutoCompressors、LLMLingua、CompAct、HyCo2、R3Mem | 解决“当前上下文太长”的问题，不等同于长期记忆 |
| Working memory：observation abstraction | 把 DOM、视频、GUI、环境观察抽象成低维状态 | Synapse、VideoAgent、MA-LMM、Context as Memory | 对交互环境特别关键，因为原始 observation 往往过长、过噪 |
| Working memory：multi-turn state consolidation | 在多轮任务中持续压缩、继承和更新中间状态 | MEM1、MemGen、MemAgent、ReSum、MemSearcher、IterResearch、SUPO、AgeMem | 连接 short-term working memory 和 long-term experiential memory |
| Working memory：hierarchical folding / planning | 用层级折叠、目标图或规划结构管理长程任务状态 | HiAgent、Context-Folding、AgentFold、DeepAgent、SayPlan、KARMA、Agent-S、PRIME | 更适合 deep research、web automation、robotics 等长程 agent 任务 |

### 按 Memory Dynamics 组织的代表工作

| Dynamics / 方向 | 主要问题 | 代表工作 | 解读重点 |
| --- | --- | --- | --- |
| Semantic summarization | 把原始历史压缩成 textual summary、session summary 或 multimodal summary | MemGPT、Mem0、Mem1、MemAgent、MemoryBank、ReadAgent、LightMem、DeepSeek-OCR、LangRepo | 最常见的 formation 方法，适合作为长期记忆写入前的第一层压缩 |
| Knowledge distillation | 从对话、轨迹、视觉观察中抽取高层 intent、insight、workflow 或 procedural knowledge | TiM、RMM、MemGuide、M3-Agent、AWM、Memp、ExpeL、R2D2、H2R、Memory-R1、Mem-alpha | 目标不是保存原文，而是形成更可迁移的知识 |
| Structured construction | 把 memory 构造成 KG、tree、hierarchical JSON、networked notes 或多层 graph | KGT、Mem0g、D-SMART、GraphRAG、AriGraph、Zep、RAPTOR、MemTree、H-MEM、A-MEM、G-Memory | 强化可解释、多跳和跨 session 查询，但需要维护 schema 和更新策略 |
| Latent representation | 把 memory 编码成 latent vector、latent token、multimodal embedding 或 KV-like state | MemoryLLM、M+、MemGen、ESR、CoMEM、Mem2Ego、KARMA | 适合高压缩和高频调用，但更难人工审计 |
| Parametric internalization | 通过参数更新、model editing、LoRA 或工具调用 SFT 把外部经验内化进模型能力 | MEND、ROME、MEMIT、CoLoR、ToolFormer | 更像把 memory 变成 competence，适合稳定知识或能力，不适合频繁变化的个人记忆 |

这几组表共同说明一个判断：选择相关工作时不要只按论文名或 benchmark 选，而要同时问三个问题：它的 memory form 是什么，它服务 factual / experiential / working 哪个 function，它处理 formation / evolution / retrieval 哪个 dynamics。这样才能判断一篇工作是可直接复用的工程组件，还是只能作为模型训练或底层推理优化参考。

## Benchmarks / Datasets / Frameworks

### 6 Resources and Frameworks

#### 本章作用

Section 6 从前面三条理论主轴转向资源层：用什么 benchmark 评估 agent memory，用什么 open-source framework 搭建 memory-augmented agents。

这一章本身不提出新的 taxonomy，但对后续研究很重要。因为 agent memory 的 claim 很容易泛化成“我们有长期记忆”或“我们能持续学习”，但不同 benchmark 实际测的是不同能力：有些测 factual recall，有些测 personalization，有些测 long-context retrieval，有些测 embodied/web/tool-use 中的状态保持，还有些才真正接近 lifelong/self-evolving agent。

#### 6.1 Benchmarks and Datasets

作者把 benchmark 分成两大类：


| 类别                                                           | 是否显式评估 memory | 典型问题                                                                          |
| ---------------------------------------------------------------- | --------------------- | ----------------------------------------------------------------------------------- |
| Memory / Lifelong-learning / Self-evolving-oriented benchmarks | 是                  | agent 能否构建、维护、更新、检索显式 memory                                       |
| Other related agent benchmarks                                 | 不一定              | 长程交互、多步任务、工具使用、web navigation、embodied action 是否隐式要求 memory |

##### 6.1.1 Memory / Lifelong / Self-Evolving Agent Benchmarks

这一类 benchmark 明确围绕 memory、长期交互或持续学习设计。Table 8 的维度包括 factual memory、experiential memory、multimodal input、environment type、feature 和 scale。

可以按评测目标重新整理成下面几类：


| 评测目标                                     | 主要看什么                                                      | 代表 benchmark                                                                   |
| ---------------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Conversational / user memory                 | 多轮对话中是否记住用户事实、偏好、历史事件，是否保持一致性      | MemBench、LoCoMo、PersonaMem、PerLTQA、MemoryBank、MPR、PrefEval、LOCCO、DialSim |
| Long-context memory                          | 在长上下文或长 synthetic narrative 中是否能定位、保持和使用信息 | LongBench、LongBench v2、RULER、BABILong、MM-Needle、HotpotQA                    |
| Memory hallucination                         | 当 memory 不完整或冲突时是否会编造                              | HaluMem                                                                          |
| Lifelong / continual learning                | 新信息持续到来时，是否能适应新任务且不遗忘旧知识                | MemoryBench、LifelongAgentBench、StreamBench、LongMemEval                        |
| Self-evolving agents                         | agent 是否能跨 episode 积累轨迹、反思、编辑 memory、改进策略    | MemoryAgentBench、Evo-Memory、StoryBench                                         |
| Web / task memory with explicit memory focus | web 或任务流程中是否能维持长期约束和历史状态                    | WebChoreArena、MT-Mind2Web                                                       |

这里有两个重要观察。

第一，很多 memory benchmark 仍然是 simulated environment。这样做的好处是 ground-truth memory 可控，便于判断 agent 是否真的记住了事实；坏处是和真实开放环境的噪声、变化和不完整反馈还有距离。

第二，factual memory 和 experiential memory 需要分开看。一个系统在用户事实 recall 上表现好，不代表它能从失败轨迹中学会策略；反过来，能跨 episode 提升任务表现，也不一定能精确维护用户长期 profile。

##### 6.1.2 Other Related Benchmarks

第二类 benchmark 原本不是为 memory 设计的，但因为任务长、步骤多、状态变化复杂，所以会隐式考验 memory 能力。


| Benchmark 类型                         | 为什么和 memory 有关                                       | 代表 benchmark                                   |
| ---------------------------------------- | ------------------------------------------------------------ | -------------------------------------------------- |
| Embodied / interactive environments    | agent 要记住过去观察、中间目标、环境动态和动作后果         | ALFWorld、ScienceWorld、BabyAI                   |
| Web / tool-augmented interaction       | 早期页面信息、用户约束、工具输出会在后续步骤继续影响决策   | WebShop、WebArena、MMInA、ToolBench              |
| Multi-task agent suites                | 不同任务之间需要保留 task-specific knowledge 和 strategies | AgentGym、AgentBoard、PDDL-based planning        |
| Real-world reasoning / coding / search | 长文件、多源信息、搜索轨迹和中间证据需要跨步骤整合         | SWE-Bench Verified、GAIA、xBench-DS、GenAI-Bench |

这一节的关键提醒是：不要只用“显式 memory benchmark”评估 agent memory。真实 agent 的 memory 能力往往体现在长程任务中是否能保持 state、复用中间结果、避免重复搜索、跨工具调用维持一致目标。

##### Benchmark 选型建议


| 如果要评估                             | 更合适的 benchmark 类型                                             |
| ---------------------------------------- | --------------------------------------------------------------------- |
| 用户画像、偏好、长期对话一致性         | LoCoMo、PersonaMem、PerLTQA、PrefEval、DialSim                      |
| 事实记忆检索和长上下文定位             | LongMemEval、RULER、BABILong、MM-Needle、LongBench                  |
| 持续学习和抗遗忘                       | MemoryBench、LifelongAgentBench、StreamBench                        |
| 自我反思、策略积累、跨 episode 提升    | MemoryAgentBench、Evo-Memory、StoryBench                            |
| web / tool / coding agent 中的长期状态 | WebChoreArena、MT-Mind2Web、WebArena、ToolBench、SWE-Bench Verified |
| memory hallucination 风险              | HaluMem                                                             |

#### 6.2 Open-Source Frameworks

Section 6.2 梳理开源 memory framework。作者的主要判断是：生态正在快速成熟，但框架之间的能力边界差异很大。有些是真正面向 agent 的 memory system，有些更接近 retrieval backend 或 memory-as-a-service。

Table 9 的比较维度包括 factual memory、experiential memory、multimodal memory、内部结构和公开评测。可以按用途整理如下：


| 框架类型                                | 典型结构                                           | 代表框架                                         | 适合用途                                   |
| ----------------------------------------- | ---------------------------------------------------- | -------------------------------------------------- | -------------------------------------------- |
| Agent-centric hierarchical memory       | short/medium/long-term memory，层级记忆管理        | MemGPT、MemoryOS、MemOS、MemU                    | 长期对话、agent 状态管理、记忆生命周期实验 |
| Graph / structured memory               | graph + vector、temporal KG、structured profile    | Mem0、Zep、Cognee、Memobase、Weaviate            | 用户事实、实体关系、时间有效性、多跳检索   |
| Memory manager / API layer              | core API、memory management、modular space         | LangMem、ReMe、AgentMemory、MemEngine、HindSight | 快速接入 agent 应用，统一 memory 操作接口  |
| Vector / retrieval backend              | vector database、semantic search、vector + graph   | Pinecone、Chroma、Weaviate、SuperMemory          | 可扩展存储与检索基础设施                   |
| Context engineering / multimodal memory | context engineering、skill learning、多模态 memory | MIRIX、MineContext、Acontext、PowerMem           | 多模态或上下文工程型 agent memory          |

需要注意一个评估缺口：Table 9 里很多框架没有公开统一 benchmark 结果。少数框架报告了 LoCoMo、MemoryBank、LongMemEval、PersonaMem、BFCL、AppWorld 等，但整体还缺少统一可比的评测协议。

因此读这张表时不能只看“支持 memory”。更应该追问四个问题：


| 问题                      | 含义                                                                                  |
| --------------------------- | --------------------------------------------------------------------------------------- |
| 支持哪类 memory function? | factual、experiential、working memory 是否都支持，还是只支持事实存储                  |
| memory structure 是什么?  | flat vector store、profile、graph、temporal graph、hierarchical memory、modular space |
| 是否支持 dynamics?        | 是否有 formation、consolidation、update、forgetting、retrieval timing/post-processing |
| 是否有可信 evaluation?    | 是否在 memory-oriented benchmark 或真实 agent task 上验证过                           |

#### 本章小结

Section 6 的价值是把前面的概念体系落到“怎么评估、怎么搭建”。对研究而言，benchmark 选择会直接决定 claim 的可信度；对工程而言，framework 选择要区分“存储/检索后端”和“完整 agentic memory system”。

一个实用判断是：如果系统只提供 vector search，它最多覆盖 memory retrieval 的一部分；如果系统还显式处理 formation、evolution、retrieval timing 和 post-retrieval processing，才更接近本文意义上的 agent memory framework。

## 关键图表与表格

### 关键图

- Figure 11：RL-enabled agent memory systems 的演进图。它把 memory system 从 RL-free heuristic/prompt pipeline，到 RL-assisted memory operation，再到 fully RL-driven/self-designing memory architecture 串成一条路线，是 Section 7.3 的核心图。

### 关键表格

- Table 1/3/4/5/6/7：相关工作 taxonomy 表。它们分别从 token-level、parametric、latent、factual、experiential、working memory，以及 formation dynamics 的角度整理代表方法。笔记中已转换为 `代表性工作矩阵`，用于快速判断每类 memory 方向有哪些典型工作、适合什么任务、工程上关注什么。
- Table 8：benchmark 全景表。它按 factual memory、experiential memory、multimodal input、environment type、feature、scale 比较 memory/lifelong/self-evolving benchmarks 和其他长程 agent benchmarks。笔记中已转换为 benchmark 选型表。
- Table 9：开源 memory framework 全景表。它比较框架是否支持 factual/experiential/multimodal memory、内部 memory structure 和公开 evaluation。笔记中已转换为 framework 选型表。

<!-- extracted-assets -->

### 已整理 Figure 资产

> 优先使用 arXiv source 中的原始图。


| Figure    | 资产                                                                                                                                                            | 来源                                   | 用途                                                          |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | --------------------------------------------------------------- |
| Figure 1  | [source_figure_001_overview.png](../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564/figures/source_figure_001_overview.png)                         | source`img/main.png`                   | 全文 Forms / Functions / Dynamics 总览                        |
| Figure 2  | [source_figure_002_concept-comparison.png](../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564/figures/source_figure_002_concept-comparison.png)     | source`img/concept.pdf`                | Agent Memory 与 LLM Memory / RAG / Context Engineering 的边界 |
| Figure 3  | [source_figure_003_token-level-taxonomy.png](../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564/figures/source_figure_003_token-level-taxonomy.png) | source`img/sec3-3.1.pdf`               | Token-level memory taxonomy                                   |
| Figure 4  | [source_figure_004_latent-memory.png](../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564/figures/source_figure_004_latent-memory.png)               | source`img/latent.pdf`                 | Latent memory integration                                     |
| Figure 5  | [source_figure_005_memory-paradigms.png](../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564/figures/source_figure_005_memory-paradigms.png)         | source`img/comparison.pdf`             | Token / parametric / latent memory 对比                       |
| Figure 6  | [source_figure_006_functional-taxonomy.png](../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564/figures/source_figure_006_functional-taxonomy.png)   | source`img/sec4-all-new.pdf`           | Functional taxonomy                                           |
| Figure 7  | [source_figure_007_experiential-memory.png](../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564/figures/source_figure_007_experiential-memory.png)   | source`img/sec4-4.2.pdf`               | Experiential memory taxonomy                                  |
| Figure 8  | [source_figure_008_memory-dynamics.png](../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564/figures/source_figure_008_memory-dynamics.png)           | source`img/sec5-whole.pdf`             | Memory lifecycle / dynamics                                   |
| Figure 9  | [source_figure_009_memory-evolution.png](../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564/figures/source_figure_009_memory-evolution.png)         | source`img/sec5-mem-evolution.pdf`     | Memory evolution mechanisms                                   |
| Figure 11 | [source_figure_011_rl-memory.png](../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564/figures/source_figure_011_rl-memory.png)                       | source`img/frontier-rl-memory-new.pdf` | RL-enabled memory systems evolution                           |

### 已抽取表格候选

暂无结构化表格候选。文字型表格或说明框在逐章阅读时转写为 Markdown list/table。

## 开放问题与未来方向

### 7 Positions and Frontiers

#### 本章作用

Section 7 是作者从“综述整理”转向“立场判断”的章节。前面几章回答 agent memory 现在是什么、怎么分类、怎么运作；这一章回答未来可能往哪里走，以及哪些问题还没有被解决。

作者提出 8 个 frontier。它们不是彼此独立的 topic list，而是围绕同一个趋势展开：memory 正在从外接的、手工设计的、检索中心的模块，走向可学习、可生成、可自治管理、可跨模态/多 agent/世界模型使用，并且必须具备可信治理能力。


| Frontier                               | 作者认为的趋势                                        | 关键问题                                         |
| ---------------------------------------- | ------------------------------------------------------- | -------------------------------------------------- |
| Memory Retrieval vs. Memory Generation | 从检索已有 memory 走向按需生成/重构 memory            | memory 应该只是 search，还是应当能 synthesize?   |
| Automated Memory Management            | 从人工规则走向 agent 自主管理 memory 操作             | agent 是否能自己决定 add/update/delete/retrieve? |
| RL Meets Agent Memory                  | 从 heuristic pipeline 走向 RL-driven memory control   | memory policy 能否端到端学习?                    |
| Multimodal Memory                      | 从 text memory 走向 omnimodal memory                  | 如何统一存储、检索、抽象多模态信号?              |
| Shared Memory in MAS                   | 从 isolated memory 走向 shared cognitive substrate    | 多 agent 如何共享而不混乱、不泄露、不互相污染?   |
| Memory for World Model                 | 从 data caching 走向 state simulation                 | memory 如何维持可交互世界的一致状态?             |
| Trustworthy Memory                     | 从 trustworthy RAG 走向 trustworthy persistent memory | 隐私、可解释、抗幻觉如何作为 memory 基础能力?    |
| Human-Cognitive Connections            | 从静态存储走向类人重构和离线 consolidation            | agent 是否需要 sleep-like memory consolidation?  |

#### 7.1 Memory Retrieval vs. Memory Generation

作者认为，agent memory 的主流范式正在从 retrieval-centric 转向 generation-centric。

传统 memory retrieval 的默认假设是：memory base 已经形成好了，当前任务只需要找到最相关的 entries，然后过滤、排序、拼接给模型。这对应向量检索、混合检索、图检索、reranking 等方法。

但作者指出，真实 agent memory 往往不是“取出原片段”就够了。历史信息可能嘈杂、冗余、粒度不对、和当前任务不匹配。因此 memory usage 需要 abstraction 和 recomposition，也就是从已有材料中生成更适合当前上下文的 memory representation。

作者把 memory generation 分成两类：


| 类型                     | 机制                                                                                   | 关键特点                                   |
| -------------------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------- |
| Retrieve-then-generate   | 先检索相关 memory，再生成更紧凑、更一致、更 task-specific 的 memory 表示               | 保留 grounding，同时允许自适应重组         |
| Direct memory generation | 不显式检索，直接基于当前上下文、历史或 latent state 生成 memory tokens/representations | 更接近模型内部认知，但可解释性和可控性更难 |

未来的 generative memory 需要三个性质：context adaptive、能融合 heterogeneous signals、能通过 RL 或 long-horizon task performance 自优化。这里 latent memory 被作者看作一个潜在技术路径，因为它可以绕开纯文本片段拼接，把 memory 做成更接近模型内部计算的表示。

#### 7.2 Automated Memory Management

作者指出，现有很多 memory system 仍然依赖人工规则：固定阈值、固定 summarization prompt、固定 retrieval pipeline、人工定义的 update/delete 规则。这些设计工程成本低、可解释、可复现，但在动态开放环境中泛化能力有限。

未来方向是把 memory construction、evolution、retrieval 直接纳入 agent decision loop。也就是说，agent 不只是“被动使用 memory module”，而是能显式调用 memory tools，并知道自己正在执行什么 memory action，例如 add、update、delete、retrieve。

这个方向有两个关键点：


| 方向                             | 含义                                                                                 |
| ---------------------------------- | -------------------------------------------------------------------------------------- |
| Tool-based memory management     | agent 通过显式工具调用管理 memory，使 memory 操作进入可追踪的 reasoning/action trace |
| Self-optimizing memory structure | memory store 自己能动态 link、index、reconstruct，而不是固定层级或固定 schema        |

这一节和 Section 5 的 Dynamics 直接相连。Section 5 说 memory lifecycle 包括 formation/evolution/retrieval；Section 7.2 进一步说，这些生命周期操作不应长期依赖人工规则，而应成为 agent 自身可决策、可学习的行动空间。

#### 7.3 Reinforcement Learning Meets Agent Memory

这一节是作者非常明确的立场：agent memory 会从 pipeline-based 走向 model-native，RL 会越来越多地接管 memory management 的关键决策。

![Figure 11](../assets/2025_memory-in-the-age-of-ai-agents_arxiv-2512-13564/figures/source_figure_011_rl-memory.png)

作者用 Figure 11 描述了三阶段演进：


| 阶段                  | 特点                                                  | 例子/机制                                                    |
| ----------------------- | ------------------------------------------------------- | -------------------------------------------------------------- |
| RL-free Memory        | 依赖 heuristic、prompt、semantic search、chunk concat | 固定遗忘阈值、提示词生成 memory、向量检索 pipeline           |
| RL Partially Involved | RL 只优化部分 memory 操作                             | RL reranker、RL memory writer、RL working memory compression |
| Fully RL-driven       | memory architecture 和 control policy 都端到端学习    | agent 自己设计 memory schema、形成/演化/检索全流程由策略控制 |

作者认为 fully RL-driven memory system 需要两个性质。

第一，减少 human-engineered priors。很多现有框架借用人类认知分类，例如 episodic/semantic/procedural memory 或 hippocampus 类比。它们对早期系统有帮助，但不一定是人工 agent 的最优结构。RL 可能让 agent 学出更适合任务和环境的 memory format、storage schema、update rule。

第二，让 agent 控制 memory lifecycle 的所有阶段。当前很多 RL-assisted 方法只控制一部分，例如只训练 memory writer，或者只管理 working memory compression。完整 agentic memory 需要同时学习 multi-granular formation、evolution、retrieval，并协调它们的长期效果。

这里的研究难点也很明显：memory 的 reward 往往是 delayed 的。一次写入或删除是否正确，可能要很多轮以后才显现。因此 memory RL 不是普通单步工具调用优化，而是长时域 credit assignment 问题。

#### 7.4 Multimodal Memory

作者认为，text memory 已经被较多探索，下一阶段必须转向 multimodal memory。真实 agent 的输入不是只有文本，还包括图像、视频、音频、传感器、行动反馈和环境状态。

现有工作分成两条线：


| 方向                                 | 目标                                                 | 现状                                             |
| -------------------------------------- | ------------------------------------------------------ | -------------------------------------------------- |
| Memory for multimodal agents         | 让 agent 存储、检索、使用视觉/音频/视频等感知 memory | 图像和视频最多，音频等其他模态不足               |
| Memory for unified generation models | 用 memory 保持生成中的实体、世界状态、跨帧一致性     | 更偏生成一致性，不一定是 agent experience memory |

未来挑战是 omnimodal memory：不是给每种模态单独接一个 memory store，而是让 heterogeneous signals 能在统一表示里保持 semantic alignment 和 temporal coherence。

这里的关键难点包括：


| 难点                       | 说明                                                                 |
| ---------------------------- | ---------------------------------------------------------------------- |
| Cross-modal alignment      | 文本事实、视觉对象、视频事件、动作反馈如何对齐到同一 memory item     |
| Temporal coherence         | 多模态事件随时间变化，memory 需要保留顺序、持续性和状态转移          |
| Abstraction beyond storage | 多模态 memory 不能只存 embedding，还要支持抽象、检索、推理和长期适应 |

#### 7.5 Shared Memory in Multi-Agent Systems

多 agent 系统早期多依赖 isolated local memories + message passing。这样可以避免不同 agent 互相干扰，但会带来冗余、上下文碎片和通信成本。

后续系统引入 centralized shared memory，例如 global vector store、blackboard、shared documents。它们能作为 team-level memory，支持 joint attention、role handoff、consensus building 和 long-horizon coordination。

但 naive shared memory 也有问题：


| 问题                      | 影响                                                    |
| --------------------------- | --------------------------------------------------------- |
| Memory clutter            | 所有 agent 都写入，memory 很快变脏                      |
| Write contention          | 多个 agent 同时更新同一事实或计划，产生冲突             |
| Lack of role-aware access | 不同角色、权限、可信度的 agent 读写边界不清             |
| Collective privacy        | 多 agent / 多组织共享 memory 时，隐私不再只是单用户问题 |

未来方向是 agent-aware shared memory：读写行为应根据 agent role、expertise、trust 和任务阶段调度。更进一步，shared memory management 也应通过学习来优化，让 agent 根据 long-horizon team performance 决定何时贡献、贡献什么、如何解决冲突。

#### 7.6 Memory for World Model

这一节把 memory 放到 world model 里讨论。World model 的目标不是生成固定视频片段，而是构建可以实时交互、无限延展、能根据 action 预测 next state 的内部环境。

在这种系统里，memory 是维持世界一致性的核心。它需要保存前一时刻的空间信息、语义信息、对象属性、运动逻辑或 hidden states，保证下一段生成不会忘记早期场景。

作者概括了从简单缓存到结构化状态的变化：


| 路线                            | 机制                                      | 局限/价值                                      |
| --------------------------------- | ------------------------------------------- | ------------------------------------------------ |
| Frame sampling                  | 用少量历史帧条件化生成                    | 容易 context fragmentation 和 perceptual drift |
| Sliding window / local KV cache | 固定窗口保存近期上下文                    | 超出窗口后对象被遗忘，难做 loop closure        |
| SSM-style state                 | 把无限历史压到固定递归状态                | 成本稳定，但精确召回受限                       |
| Explicit memory banks           | 外部保存历史表示，按相似度/几何关系检索   | 支持精确召回和场景一致性                       |
| Sparse memory retrieval         | 注入稀疏历史帧或 pose-conditioned context | 平衡效率和长期一致性                           |

未来趋势是从 data caching 转向 state simulation。作者提出两个可能范式：


| 范式                     | 含义                                                                             |
| -------------------------- | ---------------------------------------------------------------------------------- |
| Dual-system architecture | System 1 负责快速物理/流畅交互，System 2 负责慢速推理、规划和世界一致性          |
| Active memory management | world model 不只是记住最近 N 帧，而是主动维护 coherent and queryable world state |

这个方向和 embodied agent、robotics、interactive video generation 都有关。memory 的目标从“帮语言模型回答问题”扩展为“维持一个可交互世界的连续状态”。

#### 7.7 Trustworthy Memory

作者把 trustworthy memory 视为真实部署的基础要求，而不是附加功能。相比 RAG，agent memory 的信任问题更严重，因为它保存的是长期、持久、用户特定、可能敏感的信息，包括交互历史、偏好、行为轨迹和个性化事实。

作者提出三根支柱：


| 支柱                     | 要解决的问题                                       | 可能机制                                                                                                                    |
| -------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Privacy preservation     | memory 泄露、过度保留、间接 prompt attack          | permissioned memory、user-governed retention、on-device/encrypted storage、federated access、redaction、adaptive forgetting |
| Explainability           | 用户和开发者不知道哪些 memory 被检索、如何影响输出 | traceable access paths、retrieval rationale、counterfactual explanation、memory influence visualization                     |
| Hallucination robustness | memory 冲突、不完整、低置信检索导致错误            | conflict detection、uncertainty-aware generation、abstention、fallback、multi-agent cross-checking                          |

这一节的一个重要判断是：未来 memory system 可能需要 OS-like abstractions。也就是 memory 被分段、版本化、可审计，并由 agent 和 user 共同管理。这个判断和本文开头把 memory 称为 agent 的 foundational primitive 是一致的：如果 memory 是长期 agent 的核心资源，它就需要类似操作系统级别的权限、版本、隔离和审计。

#### 7.8 Human-Cognitive Connections

最后作者回到认知科学。现有 agent memory 和人类记忆有结构相似性：有限 context window 类似 working memory，外部 vector database 类似 long-term memory；interaction logs、world knowledge、code skills 也分别接近 episodic、semantic、procedural memory。

但作者强调一个根本差异：人类记忆不是精确 replay，而是 constructive reconstruction。人会根据当前认知状态重构过去，记忆会抽象、扭曲、重组。多数 agent memory 仍然像 RAG 一样做 verbatim retrieval，把 memory 当成不可变 token 仓库。

未来方向是引入类似 sleep 的 offline consolidation：


| 机制                            | 含义                                                |
| --------------------------------- | ----------------------------------------------------- |
| Offline consolidation intervals | agent 暂停实时交互，整理、压缩、重构历史 memory     |
| Generative replay               | 从 episodic traces 中重放/生成经验，用于抽象 schema |
| Active forgetting               | 主动剪枝冗余噪声，保留长期有用结构                  |
| Index optimization              | 在无实时延迟压力下重建索引和 memory organization    |

这对应从 explicit text retrieval 走向 generative reconstruction。作者认为，agent 未来不应只是 archive data，而应 internalize experience，把大量 episodic streams 周期性压缩成更高效的 parametric intuition 或 latent memory。

#### Section 7 小结

Section 7 的主线可以压缩成一句话：agent memory 的未来不是更大的向量库，而是更自主、更可学习、更可信的 memory subsystem。

对研究选题来说，最有价值的切入点集中在下面几类：


| 方向                     | 可研究问题                                                                             |
| -------------------------- | ---------------------------------------------------------------------------------------- |
| Generative memory        | 如何评价生成式 memory 是否 faithful、useful、可控                                      |
| RL memory policy         | formation、update、forget、retrieve 的 reward 怎么设计，如何做长时域 credit assignment |
| Automated memory tools   | agent 的 memory action space 应该如何设计，如何审计每次 add/update/delete              |
| Trustworthy memory       | 可验证遗忘、权限控制、memory provenance、memory influence tracing                      |
| Multimodal/shared memory | 多模态、多 agent memory 的对齐、权限、冲突解决                                         |
| Offline consolidation    | 如何设计 sleep-like 机制，把 episodic traces 压缩为 stable schemas                     |

### 8 Conclusion

#### 本章作用

Conclusion 把全文重新压回三个关键词：forms、functions、dynamics。作者的核心论断是，agent memory 不是一个辅助存储模块，而是 LLM-based agent 获得时间连续性、长期适应和长程能力的基础 substrate。

作者在结论里重申三层统一框架：


| 层次      | 论文给出的分类                         | 作用                                                                       |
| ----------- | ---------------------------------------- | ---------------------------------------------------------------------------- |
| Forms     | token-level、parametric、latent memory | 说明 memory 由什么承载，以及不同表示在可解释性、更新性、效率上的 trade-off |
| Functions | factual、experiential、working memory  | 说明 memory 服务什么能力：知识保持、能力积累、任务级推理                   |
| Dynamics  | formation、evolution、retrieval        | 说明 memory 如何形成、维护、使用，并构成持续学习闭环                       |

结论的关键判断是：未来 agent memory 会越来越可学习、自适应、自组织。尤其是 RL、multimodal/multi-agent settings、generative memory paradigm 这三条线，会推动 memory system 从外接模块变成 agent policy 的一部分。

#### 全文最终 takeaway

这篇综述的最终判断是：agent memory 不是附加的文本缓存，而是连接感知、推理、行动和持续适应的基础设施。作者用三个互补维度组织领域：`form` 说明记忆以 token、参数或 latent state 的什么载体存在；`function` 区分 factual、experiential 和 working memory 的用途；`dynamics` 描述记忆如何形成、演化、检索和被遗忘。三者组合比传统的“短期/长期记忆”二分更能解释不同系统的设计取舍。

综述进一步把研究前沿归纳为从 retrieval 到 generation、从手工规则到自动管理、从独立记忆到强化学习内化、从单模态到多 agent 共享，以及面向 world model、可信性和认知科学的连接。作者的结论不是某一种架构已经胜出，而是记忆系统正在从静态存储走向可学习、可维护、能参与策略更新的 agent substrate。后续工作需要同时报告记忆质量、检索和使用成本、跨任务适应、错误传播与安全边界。

这篇综述的最终立场可以概括为：


| 过去/当前常见做法                   | 作者认为的未来方向                                              |
| ------------------------------------- | ----------------------------------------------------------------- |
| 把 memory 当作检索增强模块          | 把 memory 当作 agentic intelligence 的基础机制                  |
| 手工设计 memory schema 和规则       | 让 agent 学习和管理 memory policy                               |
| 存储并检索原始历史片段              | 生成、重构、压缩更适合当前任务的 memory representation          |
| 单模态、单 agent、静态 memory store | 多模态、多 agent、动态演化、可信治理的 memory subsystem         |
| 长上下文或向量库解决一切            | formation + evolution + retrieval + governance 共同决定长期能力 |

因此，本文不是在说“agent 需要一个更大的记忆库”，而是在说：如果 LLM 要变成真正能持续交互、自我改进、跨时间保持一致性的 agent，memory 必须被设计成一个完整的、可管理的、可学习的系统。

## 可复用研究线索

### 可以直接复用的研究框架

1. **Forms / Functions / Dynamics 三轴框架**

   这是全文最可复用的分析框架。读任何 agent memory 论文时，都可以用三个问题拆解：


   | 问题                                | 对应维度  |
   | ------------------------------------- | ----------- |
   | memory 存在哪里、以什么形式存在？   | Forms     |
   | memory 服务什么 agent 能力？        | Functions |
   | memory 如何产生、更新、遗忘、检索？ | Dynamics  |
2. **Agent memory lifecycle**

   可以把任何系统拆成 `formation -> evolution -> retrieval -> feedback` 闭环。这样能避免只讨论 vector DB 或 retrieval accuracy，而忽略 memory 如何变脏、如何更新、如何遗忘。
3. **Benchmark 选型逻辑**

   评估 memory system 时，必须先说明要测哪种能力：


   | 能力                | 应选 benchmark                                |
   | --------------------- | ----------------------------------------------- |
   | 用户长期事实和偏好  | LoCoMo、PersonaMem、PrefEval                  |
   | 长上下文定位和召回  | LongBench、RULER、BABILong、MM-Needle         |
   | 持续学习和抗遗忘    | MemoryBench、LifelongAgentBench、StreamBench  |
   | 自我演化和策略积累  | MemoryAgentBench、Evo-Memory、StoryBench      |
   | 真实长程 agent 任务 | WebArena、ToolBench、SWE-Bench Verified、GAIA |
4. **Trustworthy memory 设计清单**

   后续做 memory 系统时，可以把下面四个能力作为基本治理层：


   | 能力                   | 具体问题                                   |
   | ------------------------ | -------------------------------------------- |
   | provenance             | 这条 memory 从哪里来，什么时候写入，谁写入 |
   | permission             | 谁可以读、写、删、导出                     |
   | retention / forgetting | 什么时候过期，能否验证删除                 |
   | influence tracing      | 哪些 memory 影响了这次输出                 |
5. **RL memory policy 研究问题**

   如果要做 RL-for-memory，可以把 action space 先定义清楚：


   | Action          | 含义                                               |
   | ----------------- | ---------------------------------------------------- |
   | add             | 写入新 memory                                      |
   | update          | 修改已有 memory                                    |
   | delete / forget | 删除、归档或降权 memory                            |
   | retrieve        | 选择何时、从哪里、用什么 query 检索                |
   | consolidate     | 把多条 memory 合并为更高层 schema                  |
   | generate        | 根据上下文生成 task-specific memory representation |

   真正难点不是 action 本身，而是 delayed reward：一次 memory 操作的好坏，往往要在未来很多轮任务后才能观察到。
6. **Sleep-like offline consolidation**

   这是很有潜力的系统方向：agent 在线交互时只做轻量写入和检索，离线阶段再做重组、去重、冲突解决、摘要、索引优化和遗忘。它比实时维护所有 memory 更符合工程约束，也更接近作者强调的 cognitive connection。

## 对我当前研究/项目的启发

### 对 `paper_readings` / academic-paper-reading skill 的直接启发

我们正在搭的 `paper_readings` 其实已经可以看成一个小型 agent memory system：


| 当前组件                         | 对应 memory 概念                                |
| ---------------------------------- | ------------------------------------------------- |
| `sources/` PDF 原文              | raw experience / source memory                  |
| `reading_notes/`                 | semantic summarization + knowledge distillation |
| `assets/figures/`                | multimodal memory assets                        |
| `metadata/papers.jsonl`          | structured factual memory                       |
| `taxonomy.yaml` / `aliases.yaml` | evolving category schema                        |
| `indexes/`                       | retrieval-oriented views                        |
| section-by-section reading       | incremental formation                           |

下一步如果继续优化这个 skill，最值得做的不是继续堆功能，而是补齐 Section 5/7 反复强调的 lifecycle：


| 优化方向              | 具体做法                                                                                                    |
| ----------------------- | ------------------------------------------------------------------------------------------------------------- |
| Formation 更稳定      | 每篇论文按章节固定生成`问题-方法-证据-局限-研究线索` 结构                                                   |
| Evolution 更明确      | taxonomy 改名、方向合并、关键词归一化时记录 alias 和变更历史                                                |
| Retrieval 更强        | 支持按领域、方法、benchmark、开放问题、图表类型检索论文和笔记                                               |
| Provenance 更清楚     | 每条关键笔记尽量保留 section/page/figure/table 来源                                                         |
| Assets 更有用         | 图只截 taxonomy/architecture/curve 等真正有视觉价值的内容；文字表格转 Markdown                              |
| Offline consolidation | 定期把多篇论文的 notes 合并成方向综述，例如`Agent Memory Benchmarks`、`Trustworthy Memory`、`RL for Memory` |

### 对后续研究选题的启发

如果围绕 agent memory 做研究，我会优先关注三条路线：

1. **可信 agent memory**

   这是工程和研究都缺口明显的方向。可以从 memory provenance、permission、auditable forgetting、influence tracing 入手，做一个能解释“这次回答用了哪些 memory”的系统。
2. **Reading-agent as memory system**

   把论文阅读本身做成一个 agent memory 任务：读论文不是生成一次性摘要，而是持续构建研究记忆库。这里可以评估分类是否稳定、检索是否有效、跨论文 synthesis 是否准确。
3. **Offline consolidation for research notes**

   借鉴 Section 7.8 的 sleep-like consolidation：平时逐篇读论文，离线阶段自动把 notes 合并成领域地图、代表工作矩阵、benchmark 对比和开放问题清单。这和我们现在的 `paper_readings` 目录结构非常匹配。
