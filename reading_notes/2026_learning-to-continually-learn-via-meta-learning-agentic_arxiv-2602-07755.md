---
id: 2026_learning-to-continually-learn-via-meta-learning-agentic_arxiv-2602-07755
title: "Learning to Continually Learn via Meta-learning Agentic Memory Designs"
year: 2026
authors:
  - Yiming Xiong
  - Shengran Hu
  - Jeff Clune
venue: ""
field:
  - AI
  - NLP
direction:
  - LLM Agents
  - Agent Memory
  - Meta-learning
keywords:
  - continual learning
  - agent memory
  - meta-learning
  - memory design
status: read
source_path: ../sources/2026_learning-to-continually-learn-via-meta-learning-agentic_arxiv-2602-07755.pdf
source_archive_path: ../sources/2026_learning-to-continually-learn-via-meta-learning-agentic_arxiv-2602-07755_source.tar.gz
source_extract_path: ../assets/2026_learning-to-continually-learn-via-meta-learning-agentic_arxiv-2602-07755/source
assets_path: ../assets/2026_learning-to-continually-learn-via-meta-learning-agentic_arxiv-2602-07755
paper_type: research
---

# Learning to Continually Learn via Meta-learning Agentic Memory Designs

## 一句话总结

ALMA 把 agent memory 的“结构设计”本身变成可学习对象：由一个 Meta Agent 在可执行代码空间里开放式搜索 memory 的数据库 schema、更新流程和检索流程，从而让基于 foundation model 的 agent 更有效地从过去经验中持续学习。

## 论文定位

这篇论文位于 LLM agent、test-time continual learning、agent memory 和 automated design/meta-learning 的交叉处。它不是提出一个新的人工 memory module，而是提出一种“自动发现 memory design”的框架。作者的基本判断是：长期运行的 agent 必须能积累经验，但 memory design 不应该永远由人手写，因为不同任务域需要保存、抽象和复用的经验类型并不一样。

这里的 memory design 不是单个向量库或 prompt trick，而是一整套架构规范：经验如何表示，轨迹如何被写入，哪些内容会被摘要、结构化或丢弃，面对新任务时如何检索，检索结果如何进入 agent 上下文，以及 memory 在部署阶段是否继续更新。ALMA 要学习的正是这套规则。

## 研究问题

Foundation model 在常规推理时是 stateless 的。一个 agent 即使已经完成过许多任务，如果没有外部记忆机制，也很难把过去交互中的经验自然积累到未来任务中。这会导致 agent 在长时程任务或多次任务流中反复从零开始，无法形成真正的 test-time continual learning。

已有工作通常通过人工 memory module 解决这个问题，例如按任务描述检索历史轨迹、为每个任务抽取经验、维护全局 cheatsheet、用图结构组织 insight 和 key steps 等。但这些系统的共同问题是：memory 的数据库组织方式、update 规则和 retrieve 规则基本都是 human-crafted and fixed。作者认为这带来两个核心限制：第一，人工设计成本高；第二，固定设计很难适应真实任务的多样性和非平稳性。

因此，本文的问题可以概括为：能否让 agentic system 自动学习适合某个任务域的 memory design，使 agent 更好地存储、总结、检索和复用经验？

## 核心贡献

第一，提出 ALMA，即 Automated meta-Learning of Memory designs for Agentic systems。ALMA 用 Meta Agent 自动搜索 memory design，希望替代手写 memory design。

第二，把 memory design 表示为可执行 Python 代码。这样搜索空间足够开放，可以表达数据库 schema、多个 memory sub-module、层次化 update/retrieve pipeline、规则库、策略库、图结构 memory，以及它们之间的组合。

第三，在四个 sequential decision-making benchmark 上验证：ALMA 学到的 memory design 在整体成功率、跨 FM 迁移、经验规模扩展、分布转移适应和成本效率上优于多种人工 memory baseline。

## 摘要解读

摘要的功能是把全文主线压缩成一个完整论证链：问题是 foundation models 的 statelessness 限制 agentic systems 持续学习；现有解决方式是加入 memory module；但 memory module 的设计大多由人手写且固定；ALMA 的解决方案是让 Meta Agent 在代码空间中自动搜索 memory design；实验结论是学到的设计比 state-of-the-art human-crafted memory design 更有效、更高效。

这里最关键的概念是“continual learning during test time”。作者不是在讨论训练阶段的 continual learning，也不是参数更新式学习，而是在部署/推理过程中让 agent 通过外部 memory 保留和复用过去经验。这一点决定了本文为什么聚焦 token-level memory：它不需要重新训练 foundation model，而是通过显式文本、数据库、检索流程和上下文注入来改变 agent 的行为。

摘要还明确指出 ALMA 的搜索对象不是“memory content”，而是“memory design”。这一区分很重要。memory content 是某次运行后记住了哪些经验；memory design 是决定哪些经验会被写入、如何组织、何时检索、怎样进入 prompt 的规则。ALMA 学的是后者，因此它更像是在学习一种学习机制。

作者强调 code search space 的原因有两层。第一，代码能表示任意复杂的 memory workflow，不局限于向量检索或固定 schema。第二，代码使 Meta Agent 能直接生成可执行组件，经过验证和评估后加入 archive。这里的开放性是本文方法的卖点，也是后面安全讨论的来源：自动生成系统组件越灵活，越需要 sandbox 和审计。

摘要最后把 ALMA 放到 self-improving AI systems 的方向里。这个说法需要谨慎理解：本文并没有让 agent 自己在线重写自己的 memory design，也没有训练新的 foundation model；它展示的是一个离线或半离线的 meta-learning 框架，能在 benchmark 上发现比人工设计更好的 memory design。它是朝 self-improving 的一步，而不是完整的自主自改进系统。

## 分章节阅读笔记

### 1 Introduction

引言先从 agentic systems 的能力扩展讲起。基于 foundation models 的 agent 已经能做 autonomous decision-making 和 task execution，但它们的核心瓶颈是推理时无状态。无状态意味着每次任务的上下文主要由当前 prompt 决定，过去交互不会自然沉淀成未来行为的一部分。对单次问答这可能不是问题，但对长期 agent 来说，它会导致系统反复解决相似问题、重复犯错、无法利用过去探索得到的环境知识。

作者接着引入 memory 作为自然补救：memory 允许 agent 保存并复用 past experiences，让积累经验影响未来决策。这里的“memory”不是人类认知意义上的泛称，而是 agent system 中的外部模块。它通常包括若干数据库或文本存储，以及把交互轨迹转成可复用知识的 update 流程和从中取回相关知识的 retrieve 流程。

引言第二段把问题从“是否需要 memory”推进到“memory 应该怎样设计”。作者给出 memory design 的定义：决定 memories 如何表示、存储、检索和更新的 architectural specification。这个定义覆盖了 memory 的全部工程边界，而不只是检索算法。一个设计可以选择保存完整轨迹，也可以保存摘要、规则、失败模式、对象关系、用户偏好或抽象策略；这些选择会直接影响 agent 后续能学到什么。

作者用对话 agent 和战略游戏做对比，说明不同领域的 memory 需求不同。对话 agent 可能要记住用户偏好、事实和个人信息；战略游戏则更需要从过去交互中抽取可迁移的技能和策略，而不是保存容易变化的 episode details。这个例子支撑了本文最重要的动机：如果不同领域需要不同 memory design，那么靠人工为每个领域调结构既困难也低效。

随后作者把 ALMA 放进机器学习历史中的一个更大趋势：手工组件逐渐被学习得到的组件替代。从手工视觉特征到 learned representations，从人工设计架构到 neural architecture search，从手写优化算法到 learned optimizers，再到自动设计 agentic system。ALMA 延续这个思路：既然 agent 需要 memory 才能持续学习，那么能否自动学习“让 agent 持续学习的 memory 机制”？

这一段的标题短语“learn to continually learn”很有指向性。普通 learning 是学会解决任务；continual learning 是不断从新经验中改善；learning to continually learn 则是学习一种能持续吸收经验的机制。ALMA 的 meta-learning 层不直接解决 ALFWorld 或 MiniHack 任务，而是搜索 memory design；被搜索出来的 memory design 再帮助下层 agent 在任务流中学习。

引言中的 Figure 1 说明 ALMA 的整体循环。Meta Agent 从 memory design archive 中采样旧设计，读取其代码和评估日志，反思现有问题，提出修改计划，然后实现新的 memory design 代码。新设计经过正确性验证后接入固定 agentic system，在任务上评估；评估结果和日志再写回 archive，作为后续探索的材料。

<img src="../assets/2026_learning-to-continually-learn-via-meta-learning-agentic_arxiv-2602-07755/figures/source_figure_001_open-ended-exploration-process-of-ouralgo-the-me.png" alt="Figure 1: ALMA 的开放式探索流程" width="760">

Figure 1 的要点是，ALMA 的 archive 不只是排行榜，而是一个可被 Meta Agent 阅读和改造的设计记忆库。每个节点都有代码、成功率和交互日志。Meta Agent 的输入因此不只是标量 reward，还包括“为什么这个 design 成功或失败”的轨迹证据。这使它有机会做结构性修改，例如新增一个 sub-module、改变检索顺序、增加失败模式库，而不仅是调 prompt。

引言最后说明实验选择：ALFWorld、TextWorld、Baba Is AI、MiniHack 都是文本交互式 sequential decision-making environments。它们适合评估 memory design，因为 agent 需要通过过去轨迹获得预训练知识中不存在的环境信息、规则、策略或失败经验。作者宣称 ALMA 能发现 domain-tailored memory designs，并在 Table 1、Figure 4、Figure 5、Figure 6 中分别验证性能、经验规模扩展、分布转移适应和成本效率。

这一节留下的核心假设是：memory design 的质量能够独立于底层 FM 能力被评估，并且学到的 design 能迁移到更强 FM。后面的实验正是围绕这个假设展开：学习时用 GPT-5-nano 作为 fixed agentic system，测试时还换到 GPT-5-mini，看 memory design 是否仍然有效。

### 2 Related Work

相关工作部分主要完成三件事：界定本文研究的 memory 类型，说明 ALMA 与 learning-to-learn / AI-generating algorithms 的关系，区分 ALMA 和已有 automated agent design 工作。

第一类是 agentic systems 的 memory。作者采用 token-level memory、parametric memory 和 latent memory 的区分。token-level memory 用显式文本或数据库保存经验，再通过检索把相关经验加入 agent prompt；parametric memory 把经验编码进模型参数；latent memory 则依赖隐藏状态或连续表示。本文聚焦 token-level memory，因为它评估更快、不需要额外训练模型，而且结构更可解释、更容易跨 agent 迁移。

这一选择对论文非常关键。如果 ALMA 搜索的是 parametric memory，评估每个设计可能需要训练模型，成本会很高，也难以看清结构；如果搜索 latent memory，学到的东西可能不容易解释。token-level memory 则天然适合代码生成式设计：Meta Agent 可以生成数据库 schema、update/retrieve 函数、摘要流程、图遍历逻辑等。

第二类是 AI-generating algorithms 和 learning-to-learn。作者把 ALMA 放在自动化替代人工组件的传统中。已有工作可以自动学习 neural architecture、learning algorithm、training environment 或 agent workflow。ALMA 更接近“meta-learning learning algorithms”的支柱，因为它学习的不是任务策略本身，而是让 agent 从经验中持续改进的 memory mechanism。

第三类是 automated design of agentic systems。已有系统会自动设计 agent 的工具、模块、工作流或多 agent 结构，但很多工作评估的是 one-shot performance：设计出来的 agent 在当前任务上表现是否更好。ALMA 的差异是优化目标明确指向 continual learning from past experience。也就是说，ALMA 关心的是 memory design 是否能让 agent 从过去任务中积累可复用经验。

相关工作还提到 concurrent work MemEvolve。作者认为其局限在于依赖许多已有 handcrafted memory design 初始化，并倾向 greedy selection top-performing designs。ALMA 的反差是从更少人工先验出发，使用 open-ended exploration，让表现中等但有潜力的设计也可能成为后续改进的 stepping stone。

### 3 Learning of Memory Designs

方法章节先定义搜索空间，再定义 memory design 的评估协议，最后说明 ALMA 的开放式探索流程。理解这一节时可以把它看成三层：设计如何表达，设计如何打分，如何根据打分继续产生新设计。

#### 3.1 Search Space for Memory Designs

作者选择代码作为 memory design 的搜索空间。理论理由是 Python 这样的语言具有足够表达能力，可以表示几乎任意 memory pipeline；实践理由是 foundation models 擅长生成和修改代码，且代码比纯 prompt 更容易执行、调试、保存和审计。

不过，完全开放的代码空间过大，Meta Agent 很难从零构造所有底层函数。因此作者提供了一个抽象接口：`general_update()` 和 `general_retrieve()`。前者在 agent 完成任务或得到轨迹后，把有用经验写入 memory；后者面对新任务时，从 memory 中取回相关经验。agentic system 只需要调用这两个通用接口，memory 内部如何组织则交给设计代码决定。

memory 内部可以有多个 sub-module。每个 sub-module 可以维护自己的 database，也可以实现自己的 `update()` 和 `retrieve()`。一个模块的输出还能传给下一个模块，因此 ALMA 可以发现层次化或流水线式结构。例如，一个模块先抽取任务目标，另一个模块检索相似失败案例，再由第三个模块合成当前任务的建议。

这个接口设计的价值在于兼顾开放性和可控性。开放性来自内部代码可以任意组合；可控性来自外部接口固定，便于把不同 memory design 接入同一个 agentic system，并用统一协议评估。

#### 3.2 Evaluation of Memory Designs

作者把 memory design 的评估拆成两个阶段：Memory Collection Phase 和 Deployment Phase。

Memory Collection Phase 的目标不是当场提升任务成功率，而是收集交互轨迹并更新 memory。这个阶段通常不从 memory 检索，因为它的作用是给 memory design 原始经验输入。关键问题是：一个 design 能否把原始 trajectory 和 feedback 转换成未来有用的知识结构。

Deployment Phase 才是测试 memory 有无帮助的阶段。面对新任务时，agent 先调用 `general_retrieve()` 取回相关知识，把它加入上下文，再执行任务。作者区分 static 和 dynamic 两种 deployment mode。static mode 中 memory 固定，只测试 agent 能否有效利用 collection 阶段形成的 memory；dynamic mode 中 agent 在部署过程中还会把新任务轨迹写回 memory，用来评估分布转移下的持续适应。

学习 memory design 时，作者主要用 static mode，理由是降低评估方差。最终测试时再考察更多性质，包括 dynamic mode 下对新分布的适应能力。这一选择很务实：如果搜索阶段每次评估都允许 dynamic update，性能会受任务顺序和新轨迹质量影响更大，Meta Agent 更难判断某个 design 本身是否真的好。

#### 3.3 Open-Ended Exploration

ALMA 的搜索过程围绕 memory design archive 展开。archive 保存已经探索过的 memory design、代码、成功率和交互日志。每轮迭代中，Meta Agent 从 archive 里采样若干旧设计，然后基于这些设计的代码和评估结果提出新想法，写出新代码，试运行和调试，最后把新设计接入 agentic system 评估。

采样策略是 open-ended 的关键。ALMA 不只是永远选择当前最高分设计继续改，而是让每个设计都有非零概率被采样，同时让成功率高且采样次数少的设计更可能被选中。这样做的原因是，有些中等表现的结构可能包含未来高性能设计需要的局部机制。如果贪心只追最高分，就可能过早收敛在一个局部方向。

Meta Agent 的反思输入包括源代码、retrieved context、interaction logs 和 overall success rate。这让它能从成功与失败案例中提出结构修改，而不仅是调超参数。比如，如果日志显示 agent 在某类环境中反复找不到对象，Meta Agent 可能新增 object-location memory；如果日志显示策略选择错误，可能新增 strategy library 或 failure pattern module。

方法章节的核心贡献不在某个具体 memory module，而在“搜索 protocol”：把 memory design 变成代码、给出统一接口、用 archive 保留设计历史、让 Meta Agent 通过反思日志持续生成新设计。

### 4 Experiments

实验章节要证明四件事：ALMA 学到的 memory design 比人工 baseline 好；这些 design 可以迁移到更强 FM；学到的结构具有领域专门化；优势不是靠无限上下文或高成本堆出来的。

#### 4.1 Experiment Setup

作者在四个 sequential decision-making benchmark 上运行 ALMA：ALFWorld、TextWorld、Baba Is AI 和 MiniHack。每个 benchmark 的数据被分成 learning set 和 testing set；每个 set 又分成 Memory Collection Phase 和 Deployment Phase。这样设计是为了避免在学习 memory design 时直接过拟合最终测试任务。

搜索阶段固定使用 GPT-5-nano 作为 agentic system 的 FM，Meta Agent 使用 GPT-5。Meta Agent 可以在 memory design 中使用 GPT-4o-mini、GPT-4.1 和 text-embedding-3-small 作为工具，例如抽取 insight 或计算语义相似度。最终测试阶段则用 GPT-5-nano 和 GPT-5-mini 两种 agent FM：前者测试同设置有效性，后者测试 memory design 是否能迁移到更强 agent。

ALMA 运行 11 个 learning steps，总共发现 43 个 memory designs。每个 deployment phase 运行三次并报告平均成功率和标准误。这个设置说明本文不是大规模无限搜索，而是在相对有限的探索预算下比较 learned design 与人工 baseline。

#### 4.2 Benchmarks

四个 benchmark 都通过文本观察环境，并用自然语言动作与环境交互，但它们对 memory 的需求不同。

ALFWorld 是家居任务环境，agent 需要把语言指令落到具体对象和动作序列上。有效 memory 可能包括物体位置、房间布局、任务步骤和失败模式。

TextWorld 是文本冒险游戏，强调探索、局部可观察环境中的对象交互和路径规划。memory 需要帮助 agent 组织房间、物体、动作结果等经验。

Baba Is AI 是规则可被操作的网格谜题。这里 memory 更需要保存抽象规则、属性验证、策略切换，而不是单纯保存过去轨迹。

MiniHack 来自 NetHack 风格环境，具有更长时程和更复杂风险。有效 memory 可能要记录计划模板、危险模式、物品或动作的条件性效果。

这些 benchmark 的差异正好服务于本文主张：如果 ALMA 真的能学习 memory design，那么它应该在不同领域发现不同结构，而不是所有任务都用同一个向量检索模板。

#### 4.3 Baselines

作者选了四类人工 memory design baseline。

Trajectory Retrieval 是最直接的强 baseline：更新时保存任务描述和轨迹，检索时按任务描述 embedding 相似度取回最相关轨迹。它的优点是简单、保留细节；缺点是可能带来大量无关 token，也很难抽象出跨任务规则。

ReasoningBank 会为每个任务抽取 experience，并按相似任务检索对应经验。它比完整轨迹更抽象，但仍然主要以任务为单位组织知识。

Dynamic Cheatsheet 维护一个全局语义记忆，把过去轨迹中的 insight 累积到一张 cheatsheet 中。它适合需要全局规则或通用策略的环境，但可能在细粒度对象关系任务中不够精确。

G-Memory 用层次图结构组织任务、insights 和 key steps，并通过图遍历检索相关知识。它的归纳偏置更强，适合结构化经验，但 schema 仍然是人工设计好的。

这些 baseline 覆盖了从轨迹检索、任务级经验抽取、全局摘要到图结构 memory 的主流手写路线，因此 ALMA 的比较对象并不弱。

#### 4.4 Results

主结果来自 Table 1。GPT-5-nano 设置下，No Memory 的 overall average success rate 是 6.1，最佳人工 baseline 是 Trajectory Retrieval 的 8.6，ALMA 达到 12.3，相对 No Memory 提升 6.2。这个结果说明在较弱 agent FM 上，memory design 的改进能显著补足 agent 的经验复用能力。

GPT-5-mini 设置下，No Memory 的 overall average 是 41.1，最佳人工 baseline 是 Trajectory Retrieval 的 48.6，ALMA 达到 53.9，相对 No Memory 提升 12.8。更重要的是，ALMA 的 design 是在 GPT-5-nano agent 设置下学习出来的，但换到 GPT-5-mini 后仍然提升更大。这支持作者的迁移论点：学到的 memory design 不是只适配某个弱模型的偶然技巧，而是能为更强 agent 提供更有效的经验结构。

单项看，GPT-5-mini 下 ALMA 在 ALFWorld 达到 87.1，在 TextWorld 达到 75.0，在 MiniHack 达到 20.0，都是对应列最高；Baba Is AI 上 Dynamic Cheatsheet 的 38.0 高于 ALMA 的 33.3。这说明 ALMA 并非在所有单项都绝对领先，但整体最强。Baba Is AI 的例外也合理：全局 cheatsheet 对规则型 puzzle 有很强归纳偏置。

Figure 2 展示 Baba Is AI 上的学习过程。左侧 archive tree 表示不同 memory design 的继承关系和成功率，右侧显示逐步学习曲线。作者强调，最佳路径并不是简单从最高分节点一路贪心上升，而是经过一些中等表现设计，这些设计引入了 property validation、spatial object normalization、strategy switching 等机制，最终组合成更强 design。

<img src="../assets/2026_learning-to-continually-learn-via-meta-learning-agentic_arxiv-2602-07755/figures/source_figure_002_the-learning-process-of-ouralgo-on-baba-is-ai-us.png" alt="Figure 2: Baba Is AI 上的 ALMA 学习过程" width="760">

Figure 3 是理解本文贡献的关键图。它展示四个 benchmark 上最终学到的最佳 memory design 并不相同。ALFWorld 和 TextWorld 更偏向细粒度对象、空间关系、任务步骤、失败模式；Baba Is AI 和 MiniHack 更偏向规则推断、策略库、计划合成、风险判断。这直接支持了“不同领域需要不同 memory design”的核心论点。

<img src="../assets/2026_learning-to-continually-learn-via-meta-learning-agentic_arxiv-2602-07755/figures/source_figure_003_the-visualization-of-the-best-learned-memory-des.png" alt="Figure 3: 不同 benchmark 上学到的最佳 memory design" width="760">

Figure 4 研究 memory collection size 的影响。随着 collection phase 的任务数量增加，ALMA 学到的 memory design 比人工 baseline 更快受益，并且在更多轨迹下扩展更好。这说明 ALMA 不只是固定数据量下表现好，它还能更有效地把新增经验转化为有用 memory。

<img src="../assets/2026_learning-to-continually-learn-via-meta-learning-agentic_arxiv-2602-07755/figures/source_figure_004_success-rates-of-different-memory-designs-in-alf.png" alt="Figure 4: Memory collection task size 与成功率" width="520">

Figure 5 测试分布转移下的 dynamic deployment。memory 先在 ALFWorld valid seen 上收集，然后在 valid unseen 上动态部署并继续更新。ALMA 达到 84.1% 成功率，超过人工 baseline。这说明学到的 update/retrieve 机制不只是适合固定 memory，也能在新任务分布中继续吸收经验。

<img src="../assets/2026_learning-to-continually-learn-via-meta-learning-agentic_arxiv-2602-07755/figures/source_figure_005_success-rates-of-different-memory-designs-in-alf.png" alt="Figure 5: 分布转移下的 dynamic deployment" width="520">

Figure 6 讨论成本效率。作者定义 end-to-end memory cost 为把原始交互日志转换成最终检索内容所需的 FM 调用成本，并同时统计检索内容插入 agent 上下文的 token size。ALMA 平均成功率最高，同时总 memory cost 约为 0.09 美元，说明它不是简单靠塞更多上下文或更多 LLM 调用取得优势。

<img src="../assets/2026_learning-to-continually-learn-via-meta-learning-agentic_arxiv-2602-07755/figures/source_figure_006_cost-efficiency-versus-task-performance-across-a.png" alt="Figure 6: 成本效率与任务表现" width="520">

实验章节的整体结论是：ALMA 的优势来自更适合领域需求的经验组织方式，而不是单一通用 memory trick。它在整体性能、跨 FM 迁移、经验规模扩展、分布转移适应和成本效率上都给出了证据。

### 5 Conclusion, Safety, and Future Work

结论把 ALMA 定位为迈向 continual-learning agentic systems 的一步。作者强调，ALMA 学到的 memory design 能稳定超过人工 baseline，并且表现出 scalability、transferability 和 cost efficiency。

安全讨论不是附带内容，因为 ALMA 让 Meta Agent 生成可执行代码。自动生成的系统组件可能偏离人类意图，尤其当优化指标不能覆盖所有安全属性时。论文中的缓解方式包括：在 isolated sandbox 中验证和执行 memory design，限制其访问外部系统，并对学到的 memory design 做 human oversight，排查 prompt injection 等潜在有害行为。

作者也承认，随着系统规模扩大或进入真实部署，手工检查不够，需要更系统的 inspection mechanism，可能结合 AI inspection 和 human inspection。这里的安全问题不是“memory 是否会泄露隐私”这一点而已，而是更广泛的 automated code generation risk：一个会改系统组件的 Meta Agent 必须有明确边界。

未来工作主要有两条。第一，目前 ALMA 在预定义 learning set 上学习 memory design，而不是在真实部署中在线学习新 design。理想的 adaptive continual learner 应该能在动态数据流中继续调整 memory design，但这需要大量 rollouts，计算成本很高。第二，当前 ALMA 在 code space 里设计外部 memory，能力受底层 FM 代码生成能力限制；未来可以探索自动设计带原生 memory 支持的 foundation model 架构。

## 关键图表

### 关键图

| 图 | 作用 | 来源 |
|---|---|---|
| Figure 1 | ALMA 的开放式探索流程：采样旧设计、反思、编码、验证、评估、归档 | [source figure](../assets/2026_learning-to-continually-learn-via-meta-learning-agentic_arxiv-2602-07755/figures/source_figure_001_open-ended-exploration-process-of-ouralgo-the-me.png) |
| Figure 2 | Baba Is AI 上的 archive tree 和逐步学习过程，体现 stepping-stone 式探索 | [source figure](../assets/2026_learning-to-continually-learn-via-meta-learning-agentic_arxiv-2602-07755/figures/source_figure_002_the-learning-process-of-ouralgo-on-baba-is-ai-us.png) |
| Figure 3 | 四个 benchmark 上学到的最佳 memory design 结构，证明 domain-tailored design | [source figure](../assets/2026_learning-to-continually-learn-via-meta-learning-agentic_arxiv-2602-07755/figures/source_figure_003_the-visualization-of-the-best-learned-memory-des.png) |
| Figure 4 | collection trajectory 数量增加时的性能扩展，测试 sample efficiency 和 scalability | [source figure](../assets/2026_learning-to-continually-learn-via-meta-learning-agentic_arxiv-2602-07755/figures/source_figure_004_success-rates-of-different-memory-designs-in-alf.png) |
| Figure 5 | valid seen 到 valid unseen 的分布转移适应，测试 dynamic deployment | [source figure](../assets/2026_learning-to-continually-learn-via-meta-learning-agentic_arxiv-2602-07755/figures/source_figure_005_success-rates-of-different-memory-designs-in-alf.png) |
| Figure 6 | 成本、检索 token 和成功率的权衡，说明 ALMA 不是靠高成本堆性能 | [source figure](../assets/2026_learning-to-continually-learn-via-meta-learning-agentic_arxiv-2602-07755/figures/source_figure_006_cost-efficiency-versus-task-performance-across-a.png) |

### 关键表格

Table 1 是主结果表。这里保留最关键的整体平均结果：

| Agent FM | Memory Design | Overall Avg. | 相对 No Memory |
|---|---:|---:|---:|
| GPT-5-nano | No Memory | 6.1 | - |
| GPT-5-nano | best manual baseline | 8.6 | +2.5 |
| GPT-5-nano | ALMA | 12.3 | +6.2 |
| GPT-5-mini | No Memory | 41.1 | - |
| GPT-5-mini | best manual baseline | 48.6 | +7.5 |
| GPT-5-mini | ALMA | 53.9 | +12.8 |

GPT-5-mini 设置下，ALMA 在四个环境上的成功率分别是：ALFWorld 87.1、TextWorld 75.0、Baba Is AI 33.3、MiniHack 20.0。Baba Is AI 上 Dynamic Cheatsheet 单项更高，但整体平均仍是 ALMA 最强。

## 实验结论

这篇论文的实验证据支持四个结论。

第一，自动学到的 memory design 可以超过人工设计。GPT-5-nano 和 GPT-5-mini 两种 agent FM 下，ALMA 的整体平均成功率都高于所有人工 baseline。

第二，学到的 memory design 有跨 FM 迁移能力。学习阶段使用 GPT-5-nano 作为固定 agentic system，测试时换成 GPT-5-mini 后仍然带来更大提升，说明 memory design 学到的是较稳定的经验组织机制。

第三，ALMA 会学出领域专门化结构。不同 benchmark 上的最佳 memory design 并不相同，这正是自动 memory design 的价值所在。

第四，ALMA 的优势不只是性能，也包括经验规模扩展、分布转移适应和成本效率。尤其 Figure 6 表明，ALMA 不依赖极长检索上下文或高昂 memory 处理成本。

## 局限性与可追问点

论文承认的主要局限是，ALMA 目前在预定义 learning set 上搜索 memory design，而不是在真实部署过程中在线改造 memory design。真正的 adaptive continual learner 应该能在动态任务流中持续调整自己的记忆结构，但这会需要大量 rollouts，计算成本很高。

第二个局限是，ALMA 的搜索能力受 Meta Agent 和底层 foundation model 的代码生成能力限制。代码空间足够开放，但开放空间不等于高效搜索。生成代码还带来安全问题，需要 sandbox、权限限制和系统化检查。

第三，实验主要是文本交互式游戏和具身模拟环境。它们适合评估经验复用，但与真实软件工程、科研助理、医疗工作流或企业长期 agent 仍有距离。

值得继续追问的问题：

- 如果把 latency、cost、context length 显式作为优化目标，ALMA 会学出什么 memory design？
- archive 中的 memory design 能否跨领域迁移，而不是每个 benchmark 重新搜索？
- 学到的优势究竟来自结构创新，还是来自额外 LLM 调用、反思和调试流程？
- 对真实长期 agent，memory design 的在线更新如何与安全审计共存？
- 如果 agent 本体、tool-use policy 和 memory design 同时被自动设计，三者边界会如何变化？

## 对我当前研究/项目的启发

这篇论文最有价值的启发是：agent memory 不应只被看作“向量库加检索 prompt”，而应被看作一个可学习、可组合、可评估的系统组件。真正重要的不是保存更多文本，而是选择合适的经验抽象层级。

对工程实现来说，可以先借鉴 ALMA 的接口思想，而不一定立即开放到任意代码生成。一个稳妥版本是固定 `update/retrieve` 接口，并允许系统在有限的 memory sub-module 集合中组合，例如轨迹库、失败模式库、规则库、策略库、空间关系图、任务签名检索器等。这样比完全开放代码更安全，也更容易调试。

对研究来说，ALMA 提供了一个清晰问题：memory design 的评价指标应该是什么。成功率是必要的，但长期 agent 还需要考虑稳定性、遗忘、冲突经验、错误经验污染、检索成本、隐私与安全边界。这些都可以成为后续研究的切入点。

## 本地资源

- PDF: [archived PDF](../sources/2026_learning-to-continually-learn-via-meta-learning-agentic_arxiv-2602-07755.pdf)
- Source archive: [arXiv source tarball](../sources/2026_learning-to-continually-learn-via-meta-learning-agentic_arxiv-2602-07755_source.tar.gz)
- Extracted source tree: [source directory](../assets/2026_learning-to-continually-learn-via-meta-learning-agentic_arxiv-2602-07755/source)
- Extracted source figures: [figures directory](../assets/2026_learning-to-continually-learn-via-meta-learning-agentic_arxiv-2602-07755/figures)
