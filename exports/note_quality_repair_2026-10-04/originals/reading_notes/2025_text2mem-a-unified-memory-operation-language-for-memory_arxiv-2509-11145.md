---
id: 2025_text2mem-a-unified-memory-operation-language-for-memory_arxiv-2509-11145
title: "Text2Mem: A Unified Memory Operation Language for Memory Operating System"
year: 2025
authors:
  - Yi Wang
  - Lihai Yang
  - Boyu Chen
  - Gongyi Zou
  - Kerun Xu
  - Bo Tang
  - Feiyu Xiong
  - Siheng Chen
  - Zhiyu Li
venue: ""
field:
  - NLP
  - LLM Agents
direction:
  - Agent Memory
  - Memory Operating System
keywords:
  - Text2Mem
  - Memory Operating System
  - LLM agents
  - memory operations
status: read
source_path: ""
source_archive_path: ../sources/2025_text2mem-a-unified-memory-operation-language-for-memory_arxiv-2509-11145_source.tar.gz
assets_path: ../assets/2025_text2mem-a-unified-memory-operation-language-for-memory_arxiv-2509-11145
paper_type: research
---
# Text2Mem: A Unified Memory Operation Language for Memory Operating System

## 一句话总结

Text2Mem 将 LLM agent 的自然语言记忆指令规范化为可验证、可解析、可跨后端执行的记忆操作语言，核心目标是让长期记忆控制从临时 API 调用变成安全、确定、可移植的执行契约。

## 研究问题

现有 agent 记忆框架通常只提供 encode、retrieve、delete 等基础原语，对 merge、promote、demote、split、lock、expire 等高阶控制支持不足或语义不一致；同时，自然语言记忆命令往往隐含作用范围、生命周期和权限规则，缺少形式化且可执行的 schema 会导致不同系统对同一意图执行出不一致甚至危险的行为。论文试图解决的是：如何为 agent memory 建立一套统一、紧凑、语义明确、可验证并能适配不同后端的操作语言。

## 核心方法

论文提出 Text2Mem，包含三个层次。第一，定义覆盖记忆生命周期的 12 个操作：编码阶段的 Encode，存储阶段的 Update、Label、Delete、Promote、Demote、Merge、Split、Lock、Expire，以及检索阶段的 Retrieve、Summarize。第二，用统一 JSON schema 表达每条指令，基本字段为 stage、op、target、args、meta，并通过显式 target、参数约束和安全规则处理作用范围、时间、优先级、锁定和删除等问题。第三，设计 validator--parser--adapter pipeline：validator 检查结构与语义合法性，parser 将 schema 转成强类型操作对象并规范化参数，adapter 再映射到 SQL 原型后端或真实记忆框架。论文还规划 Text2Mem Bench，将自然语言到 schema 的规划层评估与 schema 执行后的数据库效果评估分开，用 SMA、ESR、EMR 等指标衡量可靠性。

## 分章节阅读笔记

### 1 Introduction

引言的主要作用是把 Text2Mem 的研究对象界定为“记忆操作的标准化语言”，而不是单纯提出一个新的记忆检索算法。作者从 LLM agents 的发展趋势切入：agent 正在从单轮对话系统转向能够跨会话、长时段执行任务的系统。在这种长程交互中，memory 不只是附加模块，而是维持身份一致性、累积用户偏好、提供跨时间上下文 grounding 的核心能力。

作者随后指出，现有 memory subsystem 的能力仍然偏基础。多数框架只暴露 encode、retrieve、delete 这类原语，但真实使用中经常需要更细的控制，例如 merge、promote/demote、split、lock、expire。这里的关键不是某一个操作缺失，而是操作集合不完整会带来三个实际后果：同一意图在不同框架中需要重新定义，复杂任务难以用稳定的操作组合表达，用户也无法可靠地组织、保护或管理记忆的生命周期。

第二个障碍是缺少 formal and executable specification。自然语言命令本身经常欠明确，例如 “get rid of old notes” 或 “make rent top priority” 都隐含了作用范围、删除模式、优先级规则或生命周期约束。如果没有 schema 强制写明必填字段和不变量，也没有 typed objects 去规范化时间范围、优先级等参数，系统就无法稳定判断该执行什么。作者把这个问题同时放在用户视角和开发者视角下解释：用户看到的是平台行为不可预测甚至静默失败，开发者面对的是没有共享规范，难以保证扩展之间安全互操作。

### Figure 1: Ambiguity and inconsistency in current systems versus Text2Mem's formalized handling

![Figure 1](../assets/2025_text2mem-a-unified-memory-operation-language-for-memory_arxiv-2509-11145/figures/source_figure_001_ambiguity-and-inconsistency-in-current-systems-v.png)

Figure 1 是引言的核心动机图。左侧用 “I'd rather not bring up anything about lunch for now” 展示自然语言记忆命令的三类歧义：哪些 lunch 相关记忆属于目标范围，操作应该是删除、隐藏还是降低优先级，for now 对应多长时间。不同 agent 可能做出临时抑制、硬删除或忽略命令等不一致行为。右侧展示 Text2Mem 的处理方式：同一句话被形式化为 storage 阶段的 Demote 操作，目标由 lunch tag 确定，参数指定降低优先级而不是删除，再经过 validator、parser、adapter 执行。这个例子说明论文关注的不是更强的语义理解本身，而是把语义理解后的记忆控制变成可检查、可执行、跨后端一致的对象。

在提出问题后，作者给出 Text2Mem 的基本定位：它是一种 unified memory operation language，操作集合按 encoding、storage、retrieval 三个认知阶段组织。它试图用紧凑但表达力足够的 verb inventory 消除冗余，同时把 merge、split、promote/demote、lock、expire 这类高阶控制提升为一等操作。每个操作用 schema-based specification 表达，由 required fields 和 invariants 约束，再通过 type parser 生成强类型操作对象。这样，记忆命令不再只是自然语言意图或后端 API 调用，而是可以被自动验证并安全实例化的中间表示。

引言最后把 Text2Mem 的贡献概括为三点。第一，提出面向 LLM-based agents 的统一记忆操作语言，包含覆盖 encoding、storage、retrieval 的 12 个操作。第二，提出 schema-based specification 与 type parser，使每个操作的字段、约束和不变量可以被形式化检查，并转化为安全、确定的 typed operation objects。第三，强调 execution backend 的可移植性：同一个 typed object 可以在 SQL-like reference backend 中执行，也可以映射到真实 memory framework，从而支持跨系统一致行为和可复现实验。

这一节为后文建立了清晰的阅读线索：Section 2 会说明为什么现有 agent memory 和 text-to-SQL 经验共同指向“schema 化操作语言”的必要性；Section 3 会展开 Text2Mem 的操作集合、schema 结构和 validator--parser--adapter pipeline；Section 4 则把这种语言层转化为 benchmark 问题，评估模型能否从自然语言生成可执行 schema，以及 schema 执行后是否产生可验证的记忆状态变化。

### 2 Background and Motivation

这一节承担的是“研究定位”功能：它不是直接进入 Text2Mem 的技术细节，而是说明为什么 agent memory 领域需要一种类似 text-to-SQL 中 schema backbone 的标准化中间层。作者把动机分成两条线索：一条来自 agent memory 系统本身的碎片化，另一条来自 text-to-SQL 对自然语言到可执行结构转换的经验。

### 2.1 Agent memory and operation frameworks

作者先回顾 LLM agent memory 的几类已有路线。第一类是 human-inspired memory，例如借鉴 hippocampal indexing，把语言模型和结构化存储结合起来，增强 consolidation 和 retrieval。第二类强调 transient context 或 working memory，把 attention cache、hierarchical store 等短期上下文机制显式化，以降低推理成本并保持回忆能力。第三类更偏功能模拟，例如通过 note-taking、summarization 等方式改善记忆的组织性和持久性。

接着，作者转向 tool-based memory interface。这里的重点是让系统可以显式编辑或扩展记忆：有些工作从模型参数层面提供知识插入、修改、删除接口；另一些外部记忆模块通过 extract--update 工作流或图结构存储来缓解上下文窗口限制。这些路线都在说明一个事实：memory 已经不再只是“把文本塞进向量库”，而是逐渐变成 agent 可以主动管理的外部能力。

最后，作者讨论 system-oriented designs，例如 MemGPT、A-MEM 和 MemOS。这些系统开始把 memory 当作 agent 的一等操作组件，而不是普通数据库或临时上下文缓存。它们让记忆操控更显式、更实用，但问题仍然是 fragmented：很多接口仍停留在 CRUD-style utilities 或 ad-hoc extensions 层面，缺少一套系统、语义精确的 operation language 来统一 prioritization、consolidation、lifecycle governance 等高阶控制。

这一小节对 Text2Mem 的铺垫是：论文并不否认已有记忆系统的重要性，而是指出这些系统之间缺少一个“共同操作语义层”。也就是说，Text2Mem 不是要替代 MemGPT、mem0、MemOS 这类后端，而是提供一个可以映射到不同后端的上层规范，使同一个记忆意图在不同实现中保持一致。

### 2.2 Lessons from text-to-SQL

text-to-SQL 被作者用作方法论类比。两者面对的共同问题是：自然语言表达往往欠明确、含糊且变化多，但系统最终必须生成精确、可执行的操作。SQL 查询如此，memory command 也是如此。这个类比的重点不是把记忆操作写成 SQL，而是借鉴 text-to-SQL 中“自然语言到结构化可执行表示”的设计经验。

作者从 modeling 和 benchmark 两个角度提炼 text-to-SQL 的经验。建模层面，早期系统把任务视为从 utterance 直接生成 SQL；后续方法引入 relation-aware schema encoding、structure-aware generation 等机制，说明单纯表面映射不够，模型需要显式利用 schema 约束和结构依赖。评测层面，Spider、CoSQL 等 benchmark 的关键贡献在于引入统一 schema 表示和可标准化评测，使跨领域泛化、对话澄清、错误修复都能在共同结构上比较。

作者据此提出，今天的 memory command 处于类似早期 text-to-SQL 的阶段：用户表达含糊、系统实现不一致、缺少公共 schema。Text2Mem 的设计因此借鉴三点经验：定义紧凑但有表达力的 operation set，使用 schema-level constraints 限制字段和行为边界，再用 typed objects 作为执行前的规范化中间表示。这样，memory control 才能从自由文本意图变成可验证、可复现、可跨系统执行的结构化对象。

这一节和后文的关系很直接：`2.1` 说明为什么 agent memory 后端需要统一抽象，`2.2` 说明这个统一抽象应该具备 schema 化、约束化、可执行化的形态。下一节 `3 Text2Mem` 就是在这两个动机之上，把操作集合、schema 和 validator--parser--adapter pipeline 具体化。

### 3 Text2Mem

Text2Mem 是论文的主体方法。作者把它定义为一条从自然语言记忆指令到可靠执行的标准化通路，而不是一个单独的记忆后端。整体 pipeline 分三步：自由文本先被映射成 JSON-based memory operation schema；schema 经过 validator 检查结构和语义合法性，再由 parser 转成 typed operation objects，并规范化时间范围、优先级、标签等参数；最后 adapter 把 typed objects 编译成具体后端动作，可以落到 SQL-like prototype database，也可以映射到真实 memory frameworks。

### Figure 2: Illustration of the Text2Mem execution pathway

![Figure 2](../assets/2025_text2mem-a-unified-memory-operation-language-for-memory_arxiv-2509-11145/figures/source_figure_002_illustration-of-the-text2mem-execution-pathway-n.png)

Figure 2 展示了 Text2Mem 的完整执行路径。左侧是操作集合，按 encoding、storage、retrieval 三个阶段组织。右侧从 agent dialogue 出发：用户自然语言先由模型生成 JSON schema，schema validator 负责检查 required fields、枚举值和约束，type parser 将 JSON 字段加载、规范化并构建 typed object，adapter 再把操作映射到真实 memory framework 或 SQL prototype backend。图中的午餐例子延续引言：Demote 操作降低 lunch 相关记忆的检索权重，使最终响应转向 fitness 相关内容。这个图的关键是把 Text2Mem 解释成一个“语言层 + 执行层”的分离架构：语言层保证表达清楚，执行层保证跨后端落地。

### 3.1 Operation Set Design

`3.1` 解释 Text2Mem 的动词库存如何设计。作者强调，operation set 是 Text2Mem 的核心，因为它决定 agent 如何把“记忆意图”表达成精确、可执行的动作。这里的设计不是简单罗列 API，而是要让每个动词具有稳定语义，并能组合成更复杂的 memory workflow。

### 3.1.1 Design Principles

作者给出三个设计原则。第一是 mutual exclusivity，即每个 verb 对应一种独立原子行为，语义边界不能互相重叠。例如 Promote 和 Update 不应混在一起：前者改变记忆的显著性或触发方式，后者修改内容或字段。这样可以避免同一自然语言意图在多个操作之间摇摆，也方便 validator 独立检查每个操作。

第二是 completeness，即操作集合必须覆盖完整记忆生命周期。作者把生命周期分为 encoding、storage、retrieval 三个阶段，并要求操作集合不仅支持普通写入、检索、删除，还能表达优先级调整、结构变换、生命周期治理和访问治理。这个原则回应了前文对现有框架的批评：如果操作集合缺口太多，用户就只能依赖临时扩展或后端私有行为。

第三是 minimality，即去掉冗余动词和别名，让每个操作都贡献独立表达能力。这个原则和 completeness 是互相制衡的：Text2Mem 既不能少到无法表达真实需求，也不能多到不同动词语义重叠。作者希望最终形成一个 compact but expressive 的 vocabulary，使更复杂流程可以由清晰的 atomic operations 组合出来。

### 3.1.2 Memory Operation Set

最终 Text2Mem 定义 12 个 verb：encoding 阶段 1 个，storage 阶段 9 个，retrieval 阶段 2 个。这个分布本身反映了作者的立场：记忆系统的难点不只是“写入”和“查找”，更多复杂性集中在记忆被创建之后如何治理、重组、保护、降权、过期。

Encoding 阶段只有一个操作 Encode，但它不是简单的 store-and-embed。作者把 Encode 理解为“让新信息成为语义化 memory item”的过程。一个 memory item 需要有内容、上下文、标签/实体/主题等 facets，也需要有 priority、permissions、lineage、lifespan 等治理字段，还可能包含 embeddings、keywords、summaries 等机器可用信号。因此，Encode 要先解析实体和时间、抽取任务/决策/引用、附加 provenance 和 salience，再进行索引或 embedding。这里的重点是 understanding before indexing：先确定这条记忆是什么、如何被治理、以什么粒度存活，再进入检索基础设施。

Storage 阶段包含 Update、Label、Delete、Promote、Demote、Merge、Split、Lock、Expire 九个操作。作者把 storage 从传统 CRUD 提升为 semantic governance。Update 不是盲目覆盖字段，而可以通过生成式能力修正文案、规范实体和时间、把简短记录扩展为带 owner/deadline 的任务。Label 不只是手工打标签，还可以从内容和上下文推断主题、实体并对齐 taxonomy。Delete 支持软删除、恢复窗口、硬删除前的锁和审计检查。

Promote 和 Demote 是论文特别强调的高阶控制，因为它们把 priority 或 memory salience 变成一等操作。Promote 可以让重要目标更容易被检索或提醒，Demote 可以让背景噪声降低出现频率，但二者不需要改写内容本身。这一点对 agent memory 很重要：用户常常不是想删除某条记忆，而是想让它暂时少出现、晚点提醒或降低排序权重。

Merge 和 Split 处理记忆粒度。Merge 可以先通过向量检索收集相关条目，再用模型合并重复或近重复内容，并保留 provenance links。Split 则把长条、多主题记忆拆成更原子的片段，使后续检索和治理更精确。Lock 和 Expire 负责安全与生命周期：Lock 可以把敏感或合规相关条目设为 read-only 或 append-only，Expire 可以设置 TTL 或截止日期，并定义到期后的 archive、demote 等动作。

Retrieval 阶段包含 Retrieve 和 Summarize。Retrieve 使用 symbolic predicates 与 embedding similarity 的 hybrid strategy，既能按类型、时间、权限、优先级等字段过滤，又能按语义相似度排序，并尊重 soft delete、expiration、permissions 等治理字段。Summarize 则把一个或多个检索结果压缩为 concise narrative 或 structured digest，例如决策、行动项、负责人、日期和开放问题。它不是简单截断上下文，而是让长期记忆以更紧凑的形式进入后续推理。

这一小节可以整理成一张操作表：

| Stage     | Operations                                                         | 核心作用                                                         |
| --------- | ------------------------------------------------------------------ | ---------------------------------------------------------------- |
| Encoding  | Encode                                                             | 把新信息转成带语义、上下文、治理字段和机器索引信号的 memory item |
| Storage   | Update, Label, Delete, Promote, Demote, Merge, Split, Lock, Expire | 管理记忆内容、标签、优先级、粒度、安全状态和生命周期             |
| Retrieval | Retrieve, Summarize                                                | 过滤/排序取回记忆，并将多条记忆压缩成可复用摘要                  |

### 3.1.3 Implications and Comparison

作者在 `3.1.3` 中强调，Text2Mem 不只是一个 verb list，而是一层 coherent language layer。每个 verb 都是 first-class semantic primitive，可以组合成更复杂的 workflow，例如 Retrieve -> Label -> Promote -> Summarize。由于每一步都有明确语义，组合之后仍能保持可解释性和确定性。

和现有框架的比较也服务于同一个论点。Encode、Delete、Retrieve 这类基础操作在 MemOS、mem0、Letta 等框架中通常已有支持；Update、Label、Summarize 有时只有部分或间接支持；Promote、Demote、Merge、Split、Lock、Expire 这类高阶控制则大多缺失。论文用这个对比说明 Text2Mem 的主要贡献不是“发明所有记忆动作”，而是把已有基础动作和缺失的高阶治理动作放入同一套语义完整、约束明确的操作体系中。

这一节为后面的 `3.2 Operation Schema` 做准备：操作集合定义了“可以做什么”，但要让这些操作真正可验证、可执行，还需要用 schema 明确 stage、op、target、args、meta 等字段，并给 destructive actions、global scope、priority/time 参数等加上约束。

### 3.2 Operation Schema

`3.2` 解决的是“操作如何被写成可靠执行对象”的问题。前一节定义了 Text2Mem 可以表达哪些 memory operations，但仅有动词集合还不够；自然语言命令真正执行前，必须变成字段明确、范围可控、约束可检查的结构化对象。作者因此把 operation schema 定义为 minimal yet expressive contract：每条命令都是一个 typed JSON object，内部包含显式字段和内建约束，使 memory control 可以被解释、验证并移植到不同后端。

这里的关键是把 schema 理解为执行契约，而不是普通数据格式。普通 API payload 可能只告诉后端“做某事”，但 Text2Mem schema 还要回答三个额外问题：作用范围在哪里，参数是否足够明确，操作是否安全。只有这些问题都能被 validator 和 parser 检查，后续 adapter 才能把同一对象映射到 SQL prototype 或真实 memory framework。

### 3.2.1 Design Principles

schema 层有三个原则。第一是 explicitness：凡是会影响执行的因素都必须显式表达，包括 scope、time、permissions、安全确认等。这个原则直接回应引言里的歧义问题，例如 “for now” 不能停留在自然语言层面，而应转成明确的时间范围、过期策略或降权参数。

第二是 minimality：所有操作共享五个核心字段 `stage`、`op`、`target`、`args`、`meta`。作者没有为每个操作设计完全不同的外壳，而是用统一骨架承载不同动词的参数。这让 schema 足够紧凑，也方便 validator、parser 和 adapter 复用同一套处理逻辑。

第三是 safety：validation precedes execution。潜在破坏性操作需要 confirmation 或 dry-run，生命周期约束会阻止删除 locked items 或更新 expired items。这里的安全不是后端临时判断，而是提前写入 schema 规则，使非法或危险命令在执行前就被拦截。

### 3.2.2 Schema Architecture

Text2Mem schema 的五个字段分别承担不同职责：

| Field      | 含义                                    | 在执行中的作用                                                |
| ---------- | --------------------------------------- | ------------------------------------------------------------- |
| `stage`  | 所属认知阶段：`ENC`、`STO`、`RET` | 根据操作动词决定路由，区分编码、存储治理和检索                |
| `op`     | 12 个互斥操作之一                       | 决定该命令的语义边界和可用参数                                |
| `target` | 受影响的 memory items 范围              | 把用户意图边界转成可审计的作用域                              |
| `args`   | 与具体动词相关的参数                    | 描述如何修改、治理、检索或摘要目标                            |
| `meta`   | 执行上下文和安全开关                    | 记录 actor、timestamp、language、confirmation、dry_run 等信息 |

其中 `target` 是 schema 架构中最关键的安全边界。作者要求 target 在四种范围表达里选择一种：`ids` 表示显式条目 ID，`filter` 表示基于类型、标签、时间、权重等结构化谓词筛选，`search` 表示语义或关键词意图，`all` 表示全局范围。这个设计把“影响谁”从自然语言中抽出来，让系统可以预先判断命令是否过宽、是否需要确认。

范围控制还有额外约束。storage 阶段使用 filter 或 search 时必须带 numeric limit，避免一次模糊查询改动过多记忆；`all=true` 属于异常全局范围，必须在 `meta` 中设置 confirmation 或 dry_run；retrieval 使用 `all` 也需要显式确认。这些规则让窄范围操作可以直接执行，宽范围写操作必须确认，全局操作必须主动 opt-in。

核心操作约束也很明确。`Encode` 必须有 payload；`Label` 必须指定 tags 或 facets，并说明 add、replace、remove 模式；`Update` 必须有 set object；`Promote` 和 `Demote` 的 `weight` 与 `weight_delta` 互斥；`Expire` 必须有有限期限，例如 `ttl` 或 `until`，并指定到期后的动作；`Lock` 必须指定 `read_only` 或 `append_only` 等模式。跨字段不变量进一步约束治理逻辑，例如 locked items 不能 hard-delete，expired items 不能 update，数值和时间参数要被 clamp 到合法范围。

这一架构的含义是：schema 不只是承载参数，而是在执行前就把 action、scope、governance 和 safety 放在同一个对象里。这样，同一条 memory command 即使落到不同后端，也能先经过相同的语义检查和参数规范化。

### 3.2.3 Illustrative Workflows

作者用两个 workflow 展示 schema 如何从单步操作扩展到多步治理流程。每一步都是独立 schema，但多个 schema 之间保持语义连贯，因此可以表达更复杂的 memory management 场景。

第一个例子是 Semantic Promotion Workflow。项目负责人希望提升 OKR 相关笔记的重要性，但不影响无关条目。流程先用两个 `Encode` 操作写入与 OKR 相关的笔记，每条笔记都带有 text、tags、type、time、source、facets 等结构化信息。随后使用一个 `Promote` 操作，通过 `target.search.intent.query = "OKR"` 找到相关记忆，并用 `limit = 3` 限定影响范围，再在 `args` 中把 weight 调整到 0.9。

这个例子的重点在于 search-based target 把语义检索和记忆治理连接起来。系统不是按固定 ID 修改，也不是全局提升，而是先用语义/关键词匹配找到 OKR 相关条目，再在明确 limit 内提升优先级。这样既保留自然语言意图的灵活性，又避免模糊检索导致大范围误改。

第二个例子是 Incident Postmortem Archive。场景是 SEV-1 网络事故后，SRE 记录 war-room timeline、锁定事故记录以满足合规审查，并生成面向管理层的英文摘要。流程第一步 `Encode` 事故时间线，写入事件文本、tags、type、time、facets、location 等信息。第二步 `Lock` 通过 `filter` 选中带有 `incident:p1-network` 标签、位于指定时间范围内且数量不超过 200 的记录，并将其设为 `read_only`；`args.policy` 中还写明允许 Retrieve/Summarize、禁止 Update/Delete、reviewers 和锁定过期时间。第三步 `Summarize` 通过 search target 找到事故 follow-up 相关条目，并在 `args.focus` 中要求突出 root cause、customer impact 和 remediation owners。

这个例子的重点是 lifecycle governance 和 cross-role coordination。Text2Mem 不只是修改一条记忆，而是把记录、访问控制、审计保护和面向不同角色的摘要生成串成一个可验证流程。尤其是 `Lock` 的 policy 字段体现了 schema 的治理能力：它把“谁能做什么、什么时候到期、哪些操作被禁止”直接写进执行对象，而不是依赖后端隐式规则。

### 3.2.4 Discussion and Implications

作者在小结中强调，Text2Mem schema 不是单纯的数据格式，而是 memory control 的 governance layer。它用紧凑字段把安全性、可解释性和确定性直接编码进结构，使自然语言命令可以被转成 verifiable execution plans。

这一节的贡献可以概括为三点。第一，schema 让自然语言记忆命令的隐含假设显式化，特别是 scope、time、permission 和 destructive action 的边界。第二，schema 为 validator 和 parser 提供统一输入，使非法结构、危险范围和冲突参数能在执行前被发现。第三，schema 把 Text2Mem 从“概念上的操作语言”推进为“可跨后端执行的中间表示”，为下一节的 validator--parser--adapter pipeline 奠定基础。

### 3.3 Validator--Parser--Adapter Pipeline

`3.3` 说明 schema 如何真正进入执行系统。上一节已经把自然语言意图转成 JSON schema，但 schema 本身还不能直接操作后端；它需要经过 validator、parser 和 adapter 三层处理，才能从“结构化计划”变成“后端动作”。这一 pipeline 的目标是同时保证 structural validity、semantic determinism 和 backend consistency。

### 3.3.1 Pipeline Overview

整体流程可以理解为三道关。Validator 是第一道安全关，负责检查 schema 是否结构正确、字段类型是否匹配、枚举值是否合法、是否违反治理约束。Parser 是第二道规范化关，把已经通过验证的 schema 转成 typed operation objects，并规范化时间、优先级、target、权限等参数。Adapter 是第三道落地关，把 typed objects 映射成具体后端动作，可以是 SQL-based simulation，也可以是真实 memory framework 的 API sequence。

作者还提到所有阶段都返回统一的 `ExecutionResult`，其中包含 execution status、affected entries 和 resulting state changes。这一点很重要，因为 Text2Mem 不只关心“有没有执行成功”，还关心执行影响了哪些记忆、状态如何变化、是否可以审计。pipeline 的模块化设计保证三件事： malformed instruction 不会进入执行，valid schema 会被确定性解释，同一 typed object 在不同后端上应表现等价。

### 3.3.2 Validator

Validator 是 pipeline 的第一层保障。它把 Text2Mem specification 中定义的规则应用到每个 schema instance 上。在结构层面，validator 检查 required fields、data types 和 enumerated values，例如 `stage` 是否属于 `ENC/STO/RET`，`op` 是否属于 12 个合法动词，`args` 或 `target` 是否满足该操作的基本要求。

在语义层面，validator 检查跨字段不变量和安全约束。例如 locked items 不能被 hard-delete，expiration 必须有有限 horizon，global writes 必须显式 confirmation。也就是说，validator 不只是 JSON schema 语法检查器，还承担 memory governance 的前置判断。发现问题时，它不会让命令继续执行，而是返回 structured diagnostic，指出失败字段和规则。

这一层的意义是把安全检查从 runtime 后移问题变成 execution before 的前置条件。对于 agent memory 来说，这很关键：一旦错误命令已经执行，可能造成记忆误删、权限绕过或长期状态污染。Validator 通过提前拒绝不安全或欠明确指令，确保后续 parser 和 adapter 处理的都是 well-formed、interpretable instructions。

### 3.3.3 Parser

Parser 把通过验证的 schema instance 转成 typed operation objects，这是 Text2Mem 的 canonical internal form。它的任务不是再次判断“要不要执行”，而是让每个字段变成类型明确、机器可判定、无歧义的内部对象。

具体来说，parser 会给字段分配精确类型，并规范化参数。例如自然语言或 schema 中的时间表达要被转成明确 time range 或 timestamp，priority/weight 要被转成合法数值或枚举，target 中的 search/filter 要被展开成清晰的键值条件。隐式关系也会被展开，例如一个包含时间和权限语义的 target 最终需要在 typed object 中显式表示，方便后续 adapter 不再重新猜测。

如果 parser 发现不一致或缺失引用，也会中止并返回 diagnostic error。它的作用是保证后续所有后端看到的是统一、可解释的内部表示，而不是不同后端各自重新解释 JSON。这样才能做到同一 Text2Mem 操作在 SQL prototype、MemGPT、mem0、Letta 等环境中尽可能保持一致。

### 3.3.4 Adapter

Adapter 负责把 typed operation objects 变成真实或模拟后端中的可执行动作。作者强调 adapter 不是简单字段对字段翻译，而是 semantic-level mapping：Text2Mem 要保留操作意图和治理规则，同时适配目标框架自己的执行模型。

面向真实 memory frameworks 时，adapter 会把一个 typed object 翻译成框架 API sequence。例如带 reminder 的 `Promote` 可能被拆成两步：调整 priority/ranking，以及注册 scheduled notification。`Lock` 需要更新访问控制表或权限层，强制 read-only、append-only 或 review policy。`Merge` 可能先触发 retrieval 收集候选记忆，再调用框架内部 merge API；如果后端没有 merge 能力，就需要借助外部 LLM 服务完成合并。`Summarize` 则可能结合数据库选择和模型压缩，最后返回标准化 summary object。

面向 SQL prototype 时，adapter 把操作编译为关系数据库中的 SQL statements，并在需要语义推理时加入模型调用。简单操作可以直接映射：`Encode` 变成带 text、tags、embeddings、governance metadata 的 `INSERT`；`Update` 和 `Delete` 变成保留 lineage 的 `UPDATE` 或 deactivate。复杂操作则是 hybrid symbolic-semantic workflow：`Merge` 先查询候选记录，再用 LLM 生成合并摘要，并插入新条目、链接来源；`Promote` 通过 SQL 字段更新权重或提醒信息；`Summarize` 先按 target filter `SELECT` 相关条目，再调用摘要模型生成 derived memory。

SQL prototype 的价值在于透明和可审计。它不一定是最终产品后端，但适合作为 reference implementation：每一步都有中间状态和日志，可以用于验证、benchmark 和复现实验。真实 framework adapter 则说明 Text2Mem 不局限于单一数据库，而是可以成为不同记忆系统之间的统一抽象层。

作者还提到 LLM integration。某些操作本身需要模型能力，例如 `Encode` 可能需要 embedding service 生成语义检索信号，`Summarize` 需要 summarization/abstraction model，`Merge` 可能需要模型合并内容。这些派生输出不会脱离 schema，而是重新附加到 memory backend，并保持 traceability。

### 3.3.5 Summary

Validator、parser 和 adapter 共同构成 Text2Mem 的 operational backbone。Validator 负责安全和合法性，parser 负责规范化和类型化，adapter 负责跨后端执行一致性。三者连接起来，就把原本欠明确的用户意图转成 deterministic、auditable、portable memory operations。

这一节也把 Text2Mem 的贡献从“语言设计”推进到“执行系统设计”。如果只有 schema，Text2Mem 只能规范表达；有了 validator--parser--adapter pipeline，schema 才能稳定进入真实系统，并在不同后端上产生可比较、可审计的行为。这为下一节 Text2Mem Bench 打基础：benchmark 之所以能评估 planning 和 execution，是因为 Text2Mem 把生成 schema、验证 schema、执行 schema、检查结果串成了可复现流程。

### 4 Text2Mem Bench

`4 Text2Mem Bench` 把前面提出的语言和执行 pipeline 转成可评估问题。作者强调，Text2Mem Bench 不是只评估模型能不能“理解记忆相关指令”，而是同时评估两件事：模型能否把自然语言形式化为合法 Text2Mem schema，以及这些 schema 在动态 memory environment 中执行后，是否真的产生预期数据库效果。

### Figure 3: Overview of the Text2Mem Benchmark pipeline

![Figure 3](../assets/2025_text2mem-a-unified-memory-operation-language-for-memory_arxiv-2509-11145/figures/source_figure_003_overview-of-the-text2mem-benchmark-pipeline-the.png)

Figure 3 展示 benchmark 的整体流程。左上角先配置场景维度，包括中英文、direct/indirect、single/workflow 等；随后从 scenario 生成 realistic natural-language request；再把自然语言请求翻译成 Text2Mem JSON schema，包括 prerequisites 和 schema_list；最后生成 execution expectation，用于自动测试。左下角对应两层评估：plan-level evaluation 检查 schema_list 与 gold truth 的匹配和可执行性，execution-level evaluation 检查执行后的状态是否满足期望。

这一节的核心价值在于把 “schema 看起来正确” 和 “schema 执行后真的正确” 分开。很多结构化生成任务只评估输出格式或字符串匹配，但 Text2Mem Bench 还要求检查执行后的 memory state，例如某条记录是否被创建、权重是否提升、标签是否改变、摘要是否与上下文一致。这使它更接近真实 memory control 的可靠性评估。

### 4.1 Evaluation Methodology

Text2Mem Bench 的评估分为 planning layer 和 execution layer。Planning layer 关注自然语言到 Text2Mem schema 的翻译是否准确；execution layer 关注这些 schema 在 memory environment 中执行后，是否产生可验证的 operational effects。为了让评估可复现、可解释，作者将 benchmark 执行放在一个 structured SQL-based prototype 中，这个 prototype 模拟真实 memory framework，同时保留完整审计轨迹。

Structured memory environment 的作用是为所有操作提供统一数据库状态。每条 record 都是 typed、addressable 的 memory item，包含 content、semantic facets、importance、embeddings、provenance、lifecycle metadata、locks、lineage、permissions 等字段。这样，Encode、Update、Promote、Lock、Retrieve 等操作都能在同一结构里留下可查询痕迹。

每个测试开始时，benchmark 会初始化一个空白 memory database，然后执行一系列 predefined setup operations，例如插入 notes、tasks、events、references，构造一个语义连贯的上下文。这样做的原因是 memory command 往往依赖已有状态：同一句“把最近事故相关报告锁定”只有在数据库里已有事故记录、报告标签和时间范围时才可判断是否执行正确。

Planning 阶段要求系统输出满足三类条件的 schema。第一，JSON 结构必须符合 Text2Mem specification。第二，字段、slot 和参数必须语义/语法良好，能够被 parser 直接规范化为 typed operation objects，例如明确的 time ranges、priorities、targets。第三，对于 composite 或 multi-step command，系统要生成有顺序和依赖关系的 schema_list，而不是孤立操作集合。

Execution 阶段评估 schema 是否产生真实效果。作者把这类评估类比为验证“语法正确的伪代码是否真的能运行成正确程序”。它检查的不是 schema 字面形式，而是执行后的数据库变化，包括编辑操作的 state transition、检索输出的 ranked results、reminder 或 expiration 等 temporal triggers。所有结果通过 declarative SQL assertions 验证，从而把功能正确性转成可自动检查的条件。

作者使用三个指标。Planning layer 有两个指标：`SMA`，即 String Match Accuracy，衡量生成 schema 与 gold reference 的精确匹配；`ESR`，即 Execution Success Rate，衡量 schema 能否被 benchmark engine 成功解析和执行。Execution layer 使用 `EMR`，即 Expectation Match Rate，衡量满足的断言数量占全部 verifiable conditions 的比例。

指标含义可以这样理解：`SMA` 看“写得是否和标准答案完全一样”，`ESR` 看“写得是否至少能跑起来”，`EMR` 看“跑完以后结果是否符合预期”。这三个指标覆盖了从形式一致性、执行鲁棒性到行为正确性的不同层面。

表格中的 assertion template 把 12 个操作都转成 pre-state、post-state 和 check expression：

| Operation            | 典型验证逻辑                                              |
| -------------------- | --------------------------------------------------------- |
| Encode               | 原 ID 不存在，执行后新增带内容和元数据的记录，计数增加    |
| Update / Label       | 记录存在，字段或标签集合发生预期变化，并保留 lineage      |
| Promote / Demote     | 权重按预期上升或下降，或触发 reminder                     |
| Merge / Split        | 多源记录被合并并保留 lineage，或复合记录被拆成多个 child  |
| Delete               | active record 被标记删除或移除                            |
| Lock / Expire        | 设置 RO/AO lock，或注册 expiry 和 trigger                 |
| Retrieve / Summarize | 返回结果的 ID/rank 符合预期，或摘要与上下文相似度超过阈值 |

### 4.2 Dataset Construction

数据集构造沿四个维度组织 benchmark instances：linguistic difficulty、operational structure、language 和 evaluation layer。论文中具体展开了 direct vs. indirect、single vs. workflow、English vs. Chinese 三个主要维度，并说明每个 instance 都会自动通过 Text2Mem schema 验证并绑定 SQL assertions。

### 4.2.1 Scenario Planning.

Scenario Planning 定义每个测试样本的最小但语义丰富的上下文。样本来自会议纪要、任务追踪、项目文档等现实工作和知识管理材料，目的是让 memory operation 不停留在孤立句子层面，而是在有上下文、有已有记忆状态的场景中被测试。

Instruction type 分为 direct 和 indirect。Direct instruction 明确给出操作和参数，例如“把 note 42 的优先级提高到 high，并为明天设置提醒”，主要测试模型能否正确填 schema 字段。Indirect instruction 则通过语用线索隐含意图，例如“stop bringing up the lunch topic for a while” 可能意味着 Demote 或 temporary Expire，“can you make this easier to find later?” 可能意味着 tagging 或 promotion。这一维度测试模型能否把欠明确语言解析成显式、可执行的 memory operation。

Structure 分为 single 和 workflow。Single instruction 对应单个原子操作，适合测试单一 schema 生成和执行。Workflow instruction 则由多个依赖步骤构成，通常三到五步，例如先 Retrieve 一组会议笔记，再 Label 为 urgent，再 Promote 关键项，最后 Summarize 成报告。workflow 测试的是跨步骤规划、状态传递和引用传播能力。

Language 分为 English 和 Chinese，并保留部分 bilingual pairs。这个维度用于测试 schema grounding 是否跨语言稳定：同一记忆意图用中文或英文表达时，系统应生成语义一致的操作结构。

### 4.2.2 Dataset Generation Process.

Text2Mem Bench 的数据生成分三步。第一步是 context synthesis，从会议记录、任务日志、协作文档等现实材料中合成最小但语义充足的 memory context，其中包含 notes、tasks、events、references 等异构条目。这个 context 是后续指令解释和执行验证的环境状态。

第二步是 schema generation。自然语言指令会与对应 Text2Mem schema 配对，生成流程是半自动的：先用 high-precision schema synthesis rules 和 model-assisted alignment 生成模板，再由人工验证。最终 schema 必须符合官方 JSON specification，并通过结构解析。

第三步是 assertion binding。每个 schema 都会根据操作类型绑定一组 declarative SQL assertions，用于描述预期数据库状态变化，例如 insert、update、merge、retrieve 等操作完成后应该满足什么条件。这使每个样本都从自然语言、schema 到 post-execution effect 形成端到端可验证链条。

最后，作者说明所有 schema 和 assertions 都会经过最终验证，保留下来的样本构成 official benchmark dataset。论文目前更像是在提出 benchmark 设计和即将发布的评估框架，而不是已经报告完整模型排行榜；作者表示后续会发布不同 foundation models 在该 benchmark 上的 planning accuracy、execution accuracy 和 cross-backend consistency 结果。

### 5 Conclusion

结论部分回到论文主张：Text2Mem 是面向 agents 的 unified memory operation language。作者将整套设计概括为四个组件：按 encoding、storage、retrieval 组织的 operation set；通过字段和 invariants 约束操作的 schema-based specification；用于确定性解析的 typed operation objects；以及能在 prototype database 和真实 frameworks 中一致执行的 adapters。

作者强调，Text2Mem 的价值在于建立从自然语言到可靠 memory control 的标准化路径。这个路径的保证包括 safety、determinism 和 portability：安全性来自 schema 与 validator 的前置约束，确定性来自 typed object 的规范化解释，可移植性来自 adapter 对不同后端的语义级映射。

结论也再次说明 Text2Mem Bench 的作用：通过区分 planning 和 execution，benchmark 可以端到端评估模型是否不仅能生成看似正确的 schema，还能让这些 schema 在后端中产生正确行为。作者把这看作未来系统集成和可复现实验的基础。

这一节没有新增实验结果或额外技术细节，而是把论文定位收束为“语言层”的贡献：Text2Mem 不是某个具体 memory backend，而是让不同后端可以共享同一套操作语义、验证规则和执行接口，从而提升 agent memory 的可预测性和互操作性。

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

## 局限性与可追问点

## 对我当前研究/项目的启发
