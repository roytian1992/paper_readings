---
id: 2024_generating-long-form-story-using-dynamic-hierarchical-ou_arxiv-2412-13575
title: "Generating Long-form Story Using Dynamic Hierarchical Outlining with Memory-Enhancement"
year: 2024
authors:
  - Qianyue Wang
  - Jinwu Hu
  - Zhengping Li
  - Yufeng Wang
  - Daiyuan Li
  - Yu Hu
  - Mingkui Tan
venue: ""
field:
  - NLP
  - Computational Creativity
direction:
  - Story Generation
  - Long-form Generation
  - Knowledge Graph Memory
keywords:
  - DOME
  - Dynamic Hierarchical Outline
  - Memory-Enhancement Module
  - Temporal Conflict Analyzer
status: read
source_path: ../sources/2024_generating-long-form-story-using-dynamic-hierarchical-ou_arxiv-2412-13575.pdf
source_archive_path: ../sources/2024_generating-long-form-story-using-dynamic-hierarchical-ou_arxiv-2412-13575_source.tar.gz
assets_path: ../assets/2024_generating-long-form-story-using-dynamic-hierarchical-ou_arxiv-2412-13575
paper_type: research
---

# Generating Long-form Story Using Dynamic Hierarchical Outlining with Memory-Enhancement

## 一句话总结

DOME 将动态分层大纲与基于时序知识图谱的记忆增强结合起来，用于生成更长、更连贯、上下文冲突更少的长篇故事。

## 研究问题

长篇故事生成同时需要宏观情节规划和跨长上下文的一致记忆。论文指出，直接用 LLM 生成长文本容易受长程依赖和记忆限制影响，出现人物、事件或语义上的上下文冲突；固定大纲式 plan-and-write 方法虽然能提供宏观规划，却难以适应写作阶段的不确定性，可能导致重复、冲突或情节发展僵硬；依赖人类交互的渐进式方法更灵活，但缺少稳定的高层故事线，容易影响情节完整性。因此，论文将目标定义为：给定作者提供的故事前提、角色和情节要求，生成在 plot coherence 与 context coherence 两方面都更好的长篇故事。

## 核心方法

DOME 由两个主要模块和一个自动评估器构成。Dynamic Hierarchical Outline 机制先依据小说写作理论生成覆盖完整故事阶段的 rough outline，再在写作过程中逐段动态扩展 detailed outline，使详细大纲能够参考已经生成的内容并适应生成过程中的不确定性。Memory-Enhancement Module 使用时序知识图谱保存用户输入和已生成故事，将句子抽取为带章节索引的四元组 `<subject, action, object, index>`，在后续大纲扩展和故事续写时按实体检索并由 LLM 进行语义相关性过滤，向生成器提供简洁的相关历史信息。Temporal Conflict Analyzer 则基于时序知识图谱中的四元组分组和 LLM 判断检测潜在冲突，以冲突四元组占比 $CR.=m/N \times 100\%$ 衡量上下文一致性。

## 分章节阅读笔记

### 1 Introduction

引言的核心作用是把长篇故事生成的问题拆成两个相互牵连的难点：一是长文本生成中的上下文一致性，二是故事情节的宏观规划。作者认为，LLM 虽然显著提升了故事文本的长度、复杂度和流畅性，但长篇故事并不只是“继续写得更长”。故事越长，模型越需要稳定记住人物、事件、关系和前文事实；同时，它还需要按照叙事结构推进情节，避免故事只有局部连贯而整体松散。

论文把 LLM 在长篇故事生成中的困难概括为两类。第一类是 memory limitations：LLM 依赖自注意力建立上下文联系，但在长距离依赖下仍可能无法精确、无歧义地回忆前文内容，于是出现语义冲突、人物设定漂移、事件前后不一致等问题。第二类是 planning difficulties：LLM 从大规模文本中学到许多语言模式，但并不天然掌握稳定的叙事规划原则，因此难以持续生成情节完整、发展流畅、具有小说结构感的长篇故事。

![Figure 1](../assets/2024_generating-long-form-story-using-dynamic-hierarchical-ou_arxiv-2412-13575/figures/source_figure_001_illustration-and-comparison-of-three-strategies.png)

Figure 1 是引言的关键定位图。作者先把已有方法分成两种典型路线。第一种是 hierarchical outline 或 plan-and-write 路线：先从 premise 规划 rough outline，再规划 detailed outline，最后写正文。这类方法的优点是有宏观故事线，能帮助故事变长并保持一定情节完整性；缺点是规划和写作被分开，详细大纲一旦固定，就很难适应实际生成过程中出现的不确定性，容易造成重复、冲突或情节僵化。第二种是 interactive non-hierarchical outline 路线：通过交互和前文相关内容逐步写 partial content。这类方法更能响应局部变化，但缺少高层叙事骨架，生成结果可能只在局部自然，却缺乏完整、可控的故事发展。

DOME 的研究位置正是在这两类方法之间取平衡。它保留层级大纲的宏观规划能力，但不一次性固定全部详细大纲，而是在写作过程中根据当前阶段动态生成 detailed outline；同时，它引入 Memory-Enhancement Module，把已经生成的故事内容存入 temporal knowledge graph，并在后续规划和写作时检索相关历史内容。这样，DOME 试图同时解决 plot coherence 和 context coherence：前者由 Dynamic Hierarchical Outline 机制支撑，后者由基于时序知识图谱的记忆增强支撑。

引言中提出的三个贡献对应论文后续结构。第一，DHO 被定义为一种新的长篇故事生成范式，它把 planning 和 writing 融合起来，使详细大纲能够适应生成阶段的不确定性；作者在引言中预告 DHO 可使 ${Ent}$-2 指标提升 6.87%。第二，MEM 被定义为一种上下文冲突缓解方法，它用 temporal knowledge graph 存储和访问故事历史，并让 LLM 对 KG 检索结果做语义过滤，从而保留简洁、相关的历史信息；作者声称 MEM 可减少 87.61% 的冲突。第三，论文提出 Temporal Conflict Analyzer，用时序知识图谱的信息表示规则先找到潜在冲突，再由 LLM 进一步判断冲突是否存在，用于自动评估长篇故事的上下文一致性。

![Figure 2](../assets/2024_generating-long-form-story-using-dynamic-hierarchical-ou_arxiv-2412-13575/figures/source_figure_002_general-diagram-of-proposed-the-story-generation.png)

Figure 2 在引言末尾给出 DOME 的整体流程：先根据用户输入和写作理论生成 rough outline；在每个阶段 $i$，系统从 MEM 中查询与当前 rough outline 相关的内容，动态扩展 detailed outlines，再依据 detailed outlines 和相关记忆生成 partial stories；每段新生成的故事又被写回 temporal knowledge graph，为后续阶段提供可检索记忆。这个流程说明 DOME 的关键不是单纯“加一个记忆库”，而是让记忆参与大纲扩展和正文生成两个环节，使规划和写作都能受到历史内容约束。

这一节为后文搭建了阅读主线：第 3 节会形式化定义 plot coherence 与 context coherence 的目标；第 4 节会展开 DHO、MEM 和 Temporal Conflict Analyzer 的具体机制；第 5 节则验证这些设计是否真的提升自动指标、人类评价和跨模型适用性。

### 2 Related Work

相关工作章节承担的是“给两个核心模块找位置”的任务。作者没有展开一个完整的故事生成综述，而是选择两条与 DOME 直接相关的线索：长篇故事生成方法如何处理规划，以及知识图谱如何辅助 LLM 使用外部结构化知识。前者对应 DHO，后者对应 MEM。

### 2.1 Long-form Story Generation

长篇故事生成的既有工作被作者按“是否有人类参与”分成两类。第一类是 plan-and-write 或 hierarchical outline 方法，核心思想是模仿人类写作流程，把故事生成拆成规划和写作两个阶段。早期 hierarchical story generation 先生成 premise，再基于 premise 写故事；Plan-and-Write 明确提出先 planning 再 generating；Re3 进一步把写作过程细分为 plan、draft、rewrite、edit；DOC 则强调更细粒度、更层级化的 outline control，以提升长故事连贯性。

这类方法的优势在于能让故事拥有更强的宏观结构。对于长篇故事来说，仅靠局部续写容易丢失整体走向，而大纲可以提前约束人物目标、事件发展和叙事阶段，因此有助于把故事写长并提升 plot fluency。作者对这条路线的批评也很明确：预生成的大纲是刚性的，写作阶段一旦出现未预期的局部变化，固定大纲很难调整，于是可能带来重复情节、矛盾上下文或生硬推进。这个问题正是 DHO 要解决的切入点：不是取消大纲，而是让 detailed outline 在生成过程中动态展开。

第二类方法试图用人类交互替代预先生成的大纲。相关工作包括基于 cue phrases 的 content-inducing 方法，以及 RecurrentGPT 这类把 RNN 式递归思想转化为人类引导长文本生成的框架。它们的优点是更灵活，可以根据当前生成内容和人类反馈逐步推进，因此能缓解固定大纲无法适应局部变化的问题。但作者认为，这类方法缺少稳定的高层控制，容易牺牲故事的整体流畅性和可读性，尤其是缺乏对宏观情节完整性的约束。

因此，DOME 在这一小节中的定位是折中但有针对性的：它继承 hierarchical outline 的宏观规划能力，同时避免 detailed outline 一次性固定；它也吸收交互式/渐进式生成对局部不确定性的适应能力，但不用完全依赖人类参与，而是通过已生成内容和 MEM 检索结果动态调整后续详细大纲。

### 2.2 KG-enhanced LLM Inference

这一小节为 MEM 的设计提供背景。作者先说明 Knowledge Graphs 可以用三元组 `<subject, action, object>` 建模文本中的关键信息。对长篇故事而言，这种表示天然适合抽取人物、行为、对象和关系；而 DOME 后续进一步加入时间/章节索引，把故事记忆表示为 temporal knowledge graph 中的四元组。

LLM 与 KG 结合的相关工作被作者概括为两类。第一类是直接拼接式知识注入：把 KG 中检索到的知识与输入在自然语言层面拼接，或在 token 层面融合。优点是实现简单，能直接把外部知识放进 LLM 上下文；局限是输入与知识之间缺少更深的交互，模型只是被动接收一段附加信息。第二类方法引入额外的 knowledge fusion module，对知识进行更新、筛选或简化，再送入模型。这类方法更强调知识与任务输入之间的适配。

DOME 的 MEM 更接近第二类思路。它不是把所有历史故事内容粗暴塞回上下文，而是先用 KG 结构化存储故事，再按当前大纲或生成片段检索相关信息，并让 LLM 对检索结果做语义过滤。这样做的目标是同时满足两个要求：保留足够的历史事实来避免上下文冲突，又避免把过长、无关的历史文本全部放入上下文，造成噪声和计算负担。

这章与引言的衔接很直接。引言提出长篇故事生成有两个瓶颈：规划困难和记忆限制；相关工作则分别说明，现有长篇故事生成方法在大纲灵活性和宏观控制之间存在张力，现有 KG-LLM 融合方法为结构化记忆与相关信息筛选提供了技术基础。DOME 后续的方法章节就是把这两条线合并：用 DHO 处理故事规划，用 MEM 处理历史内容记忆。

### 3 Problem definition and motivations

这一章把前两章的背景收束成一个明确任务：给定作者提供的故事 premise，系统要生成一个长篇故事，并同时改善情节层面的连贯性和上下文层面的连贯性。它不是完整的方法章节，而是说明 DOME 为什么需要“动态分层大纲”和“记忆增强”这两个设计。

### 3.1 Problem Definition

论文将输入记为作者给定的故事前提 $I$，它可以包含故事设定、人物介绍和情节要求。目标是设计一个生成框架 $F^*$，输出长篇故事 $S$。作者用两个维度衡量故事质量：$C^{Plot}$ 表示 plot coherence，即故事情节是否完整、流畅、合理推进；$C^{Context}$ 表示 context coherence，即人物、事件、关系和前文事实是否前后一致。

这个定义的关键点在于，论文没有把长篇故事生成简单看作“最大化文本长度”或“让语言更流畅”。长篇故事的质量被拆成两个更具体的目标：一方面，故事要有宏观结构，不能只是一段段局部自然的续写；另一方面，故事要能记住已经生成的内容，不能在长文本中产生设定漂移或事实冲突。后续 DHO 和 MEM 正是分别服务于这两个目标。

### 3.2 Motivaiton

作者对现有路线的动机分析延续了引言和相关工作。传统 plan-write 框架把规划和写作分开，先生成大纲，再按大纲生成故事。这种做法的问题是 detailed outline 通常在写作前就确定了，无法根据生成过程中出现的新内容或局部变化调整，因此难以适应 writing stage 的不确定性。作者还指出，两阶段方法生成的故事可能在开头附近突然停止，造成 plot missing，也就是故事阶段不完整。

另一类方法引入人类对 detailed outline 的偏好或交互反馈，确实能提高 outline 的灵活性，但代价是整体故事线可能变得不可控或不完整。也就是说，现有方法在两个方向之间摇摆：固定大纲有整体控制但不灵活，交互式细节调整更灵活但缺少稳定的宏观结构。DOME 的动机就是同时改善 plot fluency 和 plot completion。

![Figure 3](../assets/2024_generating-long-form-story-using-dynamic-hierarchical-ou_arxiv-2412-13575/figures/source_figure_030_five-stages-novel-writing-theory-from-joseph-cam.png)

作者借用 hierarchical outline 的思想，把大纲分成 rough outline 和 detailed outline。rough outline 负责宏观情节引导，因此要覆盖完整故事阶段；detailed outline 则不一次性全部生成，而是根据对应 rough outline 和前面已生成故事中的相关内容逐步展开。图中展示的五阶段小说写作理论提供了 rough outline 的结构约束：Exposition 交代背景和人物，Rising Action 引入冲突并推进张力，Climax 对应关键转折或主要冲突，Falling Action 处理高潮后的过渡和冲突解决，Denouement or Resolution 完成故事收束。把这套结构放进 rough outline 生成提示中，是为了让模型先获得完整故事骨架，再在后续阶段动态填充细节。

上下文一致性的动机来自长故事长度增加后的记忆压力。随着故事越来越长，直接把历史内容交给 LLM 或依赖模型自身上下文记忆都容易引入噪声、遗漏或冲突。DOME 因此设计 memory module，用 KG 存储故事信息，并通过检索得到与当前生成阶段语义相关的历史内容。这里的关键不是保存所有文本，而是保存可检索、可筛选、足够简洁的相关信息，使模型在生成新内容时能参考正确历史事实。

这一章实际给出了 DOME 的设计逻辑：rough outline 加小说理论保证 plot completion，动态 detailed outline 提升对生成不确定性的适应性，KG-based memory module 提供简洁相关的历史信息以改善 context coherence。第 4 章会把这些动机进一步落实为具体算法和模块。

### 4 Proposed Method

方法章节将前面的动机落实为一个生成闭环。DOME 的目标是同时改善故事的 plot coherence 和 context coherence，因此系统由两个核心模块组成：Dynamic Hierarchical Outline and writing module，简称 DHO，负责情节规划和分阶段写作；KG-based Memory-Enhancement Module，简称 MEM，负责存储、检索和过滤历史故事信息。Temporal Conflict Analyzer 则服务于评估，用来自动检测长篇故事中的上下文冲突。

![Figure 2](../assets/2024_generating-long-form-story-using-dynamic-hierarchical-ou_arxiv-2412-13575/figures/source_figure_002_general-diagram-of-proposed-the-story-generation.png)

整体流程可以理解为一个“规划-写作-记忆更新”的循环。输入 $I$ 包含故事设定、角色介绍和故事线要求。系统先在写作理论指导下生成完整 rough outline，以保证故事覆盖主要叙事阶段。随后，系统不一次性展开所有 detailed outline，而是在第 $i$ 个阶段先根据 rough outline $r_i$ 和 MEM 检索到的相关内容生成 detailed outline，再根据 detailed outline 和相关历史信息生成 partial story。每生成一段 partial story，MEM 都会把它抽取成时序知识图谱中的四元组并写回记忆库，供后续阶段检索。

### 4.1 Dynamic Hierarchical Outline Mechanism

DHO 的核心思想是把 hierarchical outline 拆成两个层次：rough outline $R$ 和 detailed outline $D$。rough outline 负责故事的宏观结构，detailed outline 负责每个阶段的局部展开。这样做的意义在于，故事既有整体骨架，又不会被一开始生成的完整详细大纲完全锁死。

rough outline 的生成由小说写作理论、用户输入和提示词共同驱动，可概括为 $R=LLM(WT,I,P_{rough\_outline})$。其中 $WT$ 是 novel writing theory，$I$ 是用户输入，$P_{rough\_outline}$ 是指导模型生成 rough outline 的提示。作者把写作理论显式写入 rough outline prompt，是为了让粗大纲覆盖完整故事阶段，而不是只给出若干松散事件。

detailed outline 的生成是动态的。论文设 $D=\{d_i\}_{i=1}^{5}$，每个 $d_i$ 对应 rough outline 的一个阶段 $r_i$。在第 $i$ 个阶段，系统先从 MEM 中找到与 $r_i$ 相关的历史内容 $RInfo_i$，再生成该阶段详细大纲：$d_i=LLM(r_i,RInfo_i,P_{detailed\_outline})$。这里的 $d_i=\{do_i^t\}_{t=1}^{M}$，表示一个 rough outline 阶段会被扩展成 $M$ 个 sub-detailed outlines。实验中 $M$ 在后文设为 3。

正文生成进一步沿着 sub-detailed outline 展开。对于第 $i$ 个 rough outline 下的第 $t$ 个 detailed outline $do_i^t$，系统从 MEM 查询与它相关的历史内容 $DInfo_i^t$，再生成局部故事 $s_i^t=LLM(do_i^t,DInfo_i^t,P_{gen\_story})$。这一步体现出 DHO 和 MEM 的耦合：detailed outline 控制当前要写什么，MEM 提供前文中应该被遵守或复用的信息。

算法流程可以概括为：初始化 MEM 中的 KG；生成 rough outline；遍历每个 rough outline 阶段；为当前阶段检索相关内容并生成 detailed outline；再遍历 detailed outline 中的每个子项，检索相关历史、生成 partial story、把 partial story 加入完整故事 $S$，并写回 KG。最终返回 rough outline、detailed outlines 和长篇故事 $S$。

### 4.2 Memory-Enhancement Module

MEM 解决的是长篇生成中的历史信息管理问题。作者引用的出发点是：长输入中间的信息容易被 LLM 忽略，故事越长，直接依赖上下文窗口或模型自身注意力越容易产生遗漏、噪声和冲突。因此，MEM 不把全部历史文本塞回 prompt，而是把历史故事结构化存储，并在需要时检索简洁相关信息。

MEM 使用 temporal knowledge graph，简称 TKG，存储故事内容。普通 KG 通常用 `<subject, action, object>` 三元组表示关键信息；DOME 在此基础上加入 `index`，形成 `<subject, action, object, index>` 四元组，其中 `index` 表示信息所在章节或生成阶段。这个时间/阶段索引很重要，因为故事冲突往往不是单个事实错了，而是前后时间顺序或阶段关系不一致。

存储过程是：MEM 在开始时保存用户输入的故事 premise，在写作过程中持续保存生成内容。对每个生成句子，系统用 LLM 抽取三元组，再加上当前章节编号形成四元组，写入 TKG。这样，故事历史就从长文本变成了可检索的结构化记忆。

![Figure 4](../assets/2024_generating-long-form-story-using-dynamic-hierarchical-ou_arxiv-2412-13575/figures/source_figure_003_the-details-of-querying-for-the-relevant-content.png)

检索过程分两步。第一步是 entity-based quadruple retrieval：给定当前 outline 或 partial outline，系统先用 LLM 识别其中的实体，再到 TKG 中检索包含相关实体的四元组。第二步是 semantic relevance filtering：系统让 LLM 根据语义相关性规则过滤候选四元组，并选出 top-k 相关内容，作为自然语言形式的 query-relevant content 提供给 DHO。

![Figure 5](../assets/2024_generating-long-form-story-using-dynamic-hierarchical-ou_arxiv-2412-13575/figures/source_figure_004_the-criterion-of-filtering-on-semantic-relevance.png)

Figure 5 展示了语义相关性评分规则。评分关注五类关系：候选知识是否与当前 outline 中的 subject 语义相同或相似，object 是否相同或相似，action 是否相同或相似，是否指向相同或相似事件，以及是否能为当前写作补充有用细节或重要信息。每满足一项加 1 分，最终分数用于选择最相关的历史内容。这个设计的作用是让 MEM 不只是按字符串或实体粗检索，而是进一步判断历史信息是否真的能服务当前写作。

### 4.3 Temporal Conflict Analyzer

Temporal Conflict Analyzer 是论文提出的自动上下文一致性评估方法。长篇故事质量以往常依赖人工评价，但人工评价成本高且耗时。既然 MEM 已经把故事存成 TKG，作者就进一步利用 TKG 来检测潜在冲突，并用冲突率衡量 context coherence。

设生成故事中的所有四元组为 $Q=\{q_i\}_{i=1}^{N}$。系统先按照规则对 TKG 中的四元组进行顺序、无重复分组，聚合可能存在冲突的信息。随后，作者使用 LLM-as-a-judge 思路，让 LLM 根据时间顺序和规则进一步判断这些候选四元组是否真的包含冲突。最终得到冲突四元组集合 $Q^{conflict}=\{q_i^{conflict}\}_{i=1}^{m}$。

冲突率定义为 $CR.=m/N \times 100\%$，其中 $N$ 是 TKG 中四元组总数，$m$ 是被判定为冲突的四元组数量。这个指标越低，表示生成故事的上下文冲突越少。需要注意的是，$CR.$ 不是传统语言流畅度指标，也不是情节完整性指标；它专门衡量基于 TKG 表示的上下文一致性，因此后续实验会把它和 ${Ent}$-2、人类评价等指标一起使用。

这一章的关键在于 DOME 不是线性调用 LLM 的 prompt pipeline，而是一个带记忆回写的迭代系统。DHO 决定故事在每个阶段如何展开，MEM 让每次展开都能参考已生成历史，Temporal Conflict Analyzer 则把同一套 TKG 表示复用于自动评估。方法的强项在于模块之间共享同一种结构化历史表示；潜在风险则是性能会依赖 LLM 抽取四元组、语义过滤和冲突判断的稳定性，这一点需要在实验与案例中继续观察。

### 5 Experiment

实验章节要回答四个问题：DOME 是否优于直接用 LLM 和已有长篇故事生成方法；DHO 与 MEM 各自是否有效；DOME 是否能迁移到不同 LLM；以及动态构建 KG 带来的计算与存储开销是否可接受。

实验设置中，DHO 每个 rough outline 被扩展为 3 个 detailed outlines，即方法章节中的 $M=3$。MEM 的 entity-based query 使用 bge-large-en-v1.5 作为 embedding model，用 cosine similarity 进行匹配，过滤阈值设为 0.75。使用 MEM 时，作者关闭了 LLM 默认的历史内容输入，以便检验 MEM 提供历史信息的效果。生成参数为 temperature 0.5、max token 1000，实验运行在 2 张 A800 GPU 上。

数据和 baseline 方面，作者沿用 DOC 的 story premises，生成 20 个长篇故事用于评价。主生成模型使用 Qwen1.5-72B-Chat。比较对象包括两类：一类是直接提示 LLM 尽可能生成长故事，包括 Llama3-70B-Instruct 和 Qwen1.5-72B-Chat；另一类是长篇故事生成 SOTA 方法，包括 Re3 和 DOC。扩展性实验则把 DOME 应用于 Yi1.5-34B-Chat、Llama3-70B-Instruct 和 Qwen1.5-72B-Chat。

评价指标分成自动评价和人工评价。自动评价包括 Word Num.、冲突率 $CR.$ 和 2-gram entropy ${Ent}$-2。$CR.$ 越低表示上下文冲突越少，${Ent}$-2 越高表示词汇/内容重复程度越低、内容多样性越好。人工评价采用平均排名，指标包括 Plot Completeness ($PCo.$)、Plot Coherence ($PCoh.$)、Relevance ($Rel.$)、Interesting ($Int.$) 和 Expression Coherence ($ECoh.$)，这些指标在表中都是越低越好。

### 5.1 Comparison experiments

主结果表明，DOME 在自动评价和人工评价上都优于直接 LLM baseline 与 Re3、DOC。

| Method | Word Num. | $CR. \downarrow$ | ${Ent}$-2 $\uparrow$ | $PCo. \downarrow$ | $PCoh. \downarrow$ | $Rel. \downarrow$ | $Int. \downarrow$ | $ECoh. \downarrow$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Llama3-70B-Instruct | 612.65 | 6.78 | 9.25 | 3.77 | 3.81 | 3.58 | 3.96 | 3.72 |
| Qwen1.5-72B-Chat | 495.70 | 0.66 | 9.06 | 4.77 | 4.80 | 4.58 | 4.96 | 4.72 |
| Re3 | 3802.15 | 0.77 | 11.56 | 2.73 | 2.53 | 2.96 | 2.56 | 2.83 |
| DOC | 3904.90 | 1.21 | 11.55 | 2.58 | 2.43 | 2.63 | 2.34 | 2.56 |
| Ours (Qwen1.5-72B-Chat) | 7113.75 | 0.56 | 12.29 | 1.15 | 1.44 | 1.26 | 1.77 | 1.16 |

自动评价上，DOME 生成的故事最长，平均 7113.75 词；同时 $CR.$ 最低，为 0.56；${Ent}$-2 最高，为 12.29。作者强调，与 Qwen1.5-72B-Chat 直接生成相比，DOME 的 ${Ent}$-2 提升 35.7%，$CR.$ 降低 15.2%；与 Re3 相比，${Ent}$-2 提升 6.3%，$CR.$ 降低 27.3%。这说明 DOME 不只是写得更长，还能在更长文本中维持更低冲突率和更高内容多样性。

人工评价上，DOME 在五项指标中都排名第一。论文把这些提升归因于两部分：MEM 通过语义过滤提供相关历史内容，减少 LLM 记忆不清带来的冲突，从而提升 relevance 和 expression coherence；DHO 根据故事发展动态生成 detailed outline，适应生成不确定性，从而提升 plot coherence。写作理论引导的 rough outline 则帮助故事覆盖更完整的叙事阶段，因此改善 plot completeness 和阅读兴趣。

### 5.2 Ablation studies

消融实验分别移除 DHO 和 MEM，用来验证两个模块的作用。

| Method | Word Num. | $CR. \downarrow$ | ${Ent}$-2 $\uparrow$ | $PCo. \downarrow$ | $PCoh. \downarrow$ | $Rel. \downarrow$ | $Int. \downarrow$ | $ECoh. \downarrow$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| w/o MEM | 6511.10 | 4.52 | 10.00 | 1.88 | 2.24 | 1.97 | 1.96 | 2.22 |
| w/o DHO | 1471.90 | 0.65 | 11.50 | 2.92 | 2.36 | 2.86 | 2.88 | 2.46 |
| Ours (Qwen1.5-72B-Chat) | 7113.75 | 0.56 | 12.29 | 1.20 | 1.40 | 1.17 | 1.62 | 1.32 |

移除 DHO 时，系统使用固定且与输入 storyline 一致的大纲。结果显示，w/o DHO 的故事长度大幅下降到 1471.90，人工评价也普遍变差，尤其 $PCo.$、$Rel.$ 和 $Int.$ 排名明显落后。作者据此认为，动态调整 detailed outline 对控制故事生成和保持情节连贯很重要；同时，小说写作理论对 rough outline 的约束有助于情节完整性。

移除 MEM 时，系统不再使用 KG 作为记忆参考，而是依赖 LLM 的多轮聊天能力生成内容；由于计算成本限制，最大聊天轮数设为 2。结果中最明显的变化是 $CR.$ 从完整模型的 0.56 上升到 4.52，${Ent}$-2 从 12.29 降到 10.00，所有人工评价指标也都有退化。这支持作者的核心判断：MEM 提供的相关历史内容能显著降低上下文冲突，并间接改善 plot coherence 与人类偏好。

### 5.3 The Scalability of DOME

扩展性实验考察 DOME 是否只适用于 Qwen1.5-72B-Chat，还是能迁移到不同参数规模和模型家族的 LLM。作者将 DOME 分别应用到 Yi1.5-34B-Chat、Llama3-70B-Instruct 和 Qwen1.5-72B-Chat。

![Figure 6](../assets/2024_generating-long-form-story-using-dynamic-hierarchical-ou_arxiv-2412-13575/figures/source_figure_005_scalability-results-of-applying-on-different-llm.png)

Figure 6 左图显示，DOME 在三种 LLM 上都提升了 ${Ent}$-2：Llama3-70B-Instruct 达到 125.51%，Qwen1.5-72B-Chat 达到 135.65%，Yi1.5-34B-Chat 达到 129.68%。右图显示，DOME 在三种 LLM 上都降低了 $CR.$：Llama3-70B-Instruct 降到 81.71%，Qwen1.5-72B-Chat 降到 84.85%，Yi1.5-34B-Chat 降到 60.43%。这里的百分比以各自原始 LLM 表现为 100% 基准，因此 ${Ent}$-2 高于 100% 表示提升，$CR.$ 低于 100% 表示冲突减少。

作者认为这种可迁移性来自 DOME 的提示和模块流程相对直接：它不需要对某个 LLM 做专门训练，而是通过 prompt、outline generation、KG retrieval 和 semantic filtering 组织生成过程。因此，只要 LLM 具备基本理解、生成和信息抽取能力，DOME 就可以作为外部生成框架套在不同模型上。

### 5.4 Computation and storage cost of DOME

成本分析报告的是动态构建 KG 所需的存储规模和平均 API 调用次数。

| LLM (w/ DOME) | Nodes | Relations | Quadruples | API calls |
|---|---:|---:|---:|---:|
| Yi1.5-34B-Chat | 691.3 | 328.45 | 354.55 | 16 |
| Llama3-70B-Instruct | 844.6 | 345.65 | 434.0 | 16 |
| Qwen1.5-72B-Chat | 791.35 | 258.23 | 404.85 | 16 |

作者认为这个开销是可接受的。以 Qwen1.5-72B-Chat 为例，DOME 额外引入约 791 个节点和 16 次用于 KG 构建的 LLM API 调用，但换来主实验中所有指标优于 SOTA baseline 的结果。这里需要注意，表中的 API calls 仅指 KG construction 的平均调用次数，不等同于完整故事生成的全部 LLM 调用成本；论文限制部分还会提到，完整框架生成一个故事平均约需要 200 次 API 调用。

实验章节总体支持论文的三个主张：DHO 改善长篇故事的情节展开和完整性，MEM 显著降低上下文冲突，DOME 作为外部框架可以迁移到多个 LLM。证据最强的是 MEM 消融中的 $CR.$ 变化，因为移除 MEM 后冲突率从 0.56 升到 4.52；相对需要谨慎看待的是人工评价和自动冲突指标都依赖具体评价设定，其中 $CR.$ 本身又由 TKG 抽取和 LLM 判断共同决定。

### 6 Conclusion

结论部分把论文的贡献重新压缩成三个模块。DOME 被定义为一种 dynamic hierarchical outlining with memory-enhancement 的长篇故事生成方法，目标是生成更连贯的长篇故事。这里的“连贯”仍然对应全文反复强调的两个维度：情节层面的 plot coherence，以及表达/上下文层面的 context 或 expression coherence。

第一项贡献是 DHO。作者强调 DHO 建立在 plan-write 框架和小说写作理论之上，但不是传统的固定大纲写作。它先生成符合写作理论的 rough outline，以保证故事有完整宏观结构；再在写作过程中动态生成 detailed outline，从而根据已经生成的故事内容调整后续展开。这一点回应了论文开头提出的固定大纲不适应生成不确定性的问题。

第二项贡献是 MEM。结论再次强调，MEM 使用 temporal knowledge graph 存储和访问已生成故事，并为 detailed outline planning 和 story writing 两个环节提供上下文内容。它的作用不是单纯扩展上下文长度，而是通过结构化存储与相关信息检索减少上下文冲突，使模型在长篇写作中更稳定地遵守前文事实。

第三项贡献是 Temporal Conflict Analyzer。它同样基于 temporal knowledge graph，先检测潜在冲突，再结合 LLM 自动评估生成文本的上下文一致性。这使论文不仅提出了生成框架，也提供了一个自动评价长篇故事上下文冲突的指标 $CR.$。

结论最后把实验结果概括为：与 SOTA 方法相比，DOME 能显著提升长篇故事在 plot 和 expression 两方面的连贯性与整体质量。结合前面的实验章节，这个结论主要由三组证据支撑：主实验中 DOME 在自动指标和人工评价上整体领先；消融实验显示 DHO 和 MEM 分别贡献于情节控制与上下文一致性；扩展性实验说明该框架可以迁移到不同 LLM。

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

## 局限性与可追问点

## 对我当前研究/项目的启发
