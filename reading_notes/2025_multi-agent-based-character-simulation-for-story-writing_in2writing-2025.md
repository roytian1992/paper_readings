---
id: 2025_multi-agent-based-character-simulation-for-story-writing_in2writing-2025
title: "Multi-Agent Based Character Simulation for Story Writing"
year: 2025
authors:
  - Tian Yu
  - Ken Shi
  - Zixin Zhao
  - Gerald Penn
venue: "Proceedings of the Fourth Workshop on Intelligent and Interactive Writing Assistants (In2Writing 2025)"
field:
  - NLP
  - Computational Creativity
direction:
  - Story Generation
  - LLM Agents
keywords:
  - fabula
  - syuzhet
  - character-simulation
status: read
source_path: ../sources/2025_multi-agent-based-character-simulation-for-story-writing_in2writing-2025.pdf
source_archive_path: ""
assets_path: ../assets/2025_multi-agent-based-character-simulation-for-story-writing_in2writing-2025
paper_type: research
---

# Multi-Agent Based Character Simulation for Story Writing

## 一句话总结

这篇论文把“根据叙事计划写故事”的任务拆成两步：先让角色 Agent 按故事世界中的时间顺序进行 role-play 来生成 fabula，再由重写模块按原计划的呈现顺序 syuzhet 写成最终故事，从而提升角色一致性、叙事连贯性和非线性叙事的可控性。

## 研究问题

现有 LLM 故事生成通常直接把 outline 扩写成文本，容易形成线性、模板化的故事；如果故事计划本身包含倒叙、回忆或非线性呈现，模型还容易产生两类问题：一类是没有经历过“时间上更早但叙述上更晚”的事件，导致角色知识缺失和幻觉；另一类是提前看到了完整大纲，把应该后置揭示的信息过早说出。作者要解决的是：如何在已有 narrative plan 的条件下，让系统既能按故事世界的时间积累角色经验，又能按作者希望的呈现顺序组织最终文本。

## 核心方法

系统包含两个核心阶段。第一阶段是 role-play：把原始 presentation plan $P_p$ 转成按时间顺序排列的 role-play plan $P_c$，再由 Director Agent 选择下一位 Character Agent 并下达高层指令，角色 Agent 根据自身目标、记忆、身体状态和聊天历史生成第三人称动作与对白。第二阶段是 rewrite：系统不直接把 role-play 聊天记录当成最终故事，而是把它作为角色动作和对白素材，再结合每个场景的 presentation outline $o_p$，按原计划 $P_p$ 的顺序写出场景文本。这个设计把“角色经历什么”和“读者看到什么”分开处理，对应叙事理论中的 fabula 与 syuzhet。

## 分章节阅读笔记

**1 Introduction**

引言先承认一个背景事实：LLM 已经显著提高了文本的连贯性和流畅度，因此自动故事生成和人机协同写作开始更多使用 LLM。但作者马上把问题从“句子写得是否通顺”转向“故事结构是否可控”。传统故事生成通常包含两个阶段：先规划事件序列，再把这些事件扩写成场景。早期方法如 IPOCL 把叙事规划看成搜索问题，用角色目标或作者目标作为引导；近期方法则把 LLM 用作规划引擎，例如 Agents' Room 用多 Agent 协作做叙事规划，Dramatron 把生成过程模块化成类似剧本创作的步骤。

作者借这段综述建立自己的研究位置：他们不是要证明 LLM 能写流畅文本，而是要解决“已有 narrative plan 如何被更可靠地写成故事”。这个定位很重要，因为它把任务边界缩窄到 writing phase：计划已经存在，系统要做的是把计划变成故事文本。这样一来，方法比较就不只是端到端写作能力，而是比较不同扩写机制如何利用同一个计划。

引言的核心问题是 LLM 生成故事常显得线性、缺少趣味。作者用叙事理论中的 fabula 和 syuzhet 来解释这个问题。fabula 指故事世界中事件实际发生的时间顺序，syuzhet 指文本向读者呈现这些事件的顺序。许多故事之所以有趣，恰恰来自二者不一致：例如倒叙、回忆、悬念式信息延迟、先展示结果再解释原因等。自动故事生成较少处理非线性叙事，是因为一旦改变呈现顺序，就容易引入角色知识错乱、情节漏洞和前后矛盾。

本文的基本想法是先按 fabula 生成，再按 syuzhet 重组。也就是说，系统先让角色 Agent 在故事世界的时间顺序中经历事件，形成较自然的对话、动作、记忆和状态；随后再用 rewrite 步骤把这些中间结果改写成符合原始叙事计划呈现顺序的文本。这个设计把两个困难拆开：role-play 负责角色行为和时间一致性，rewrite 负责叙事呈现和文本润色。

引言还强调作者关心写作者工作流，而不是完全自动替代写作者。模块化的好处是人可以选择介入某些阶段：在 role-play 阶段，人类写作者可以扮演一个角色，与 LLM Agent 一起模拟场景；在 rewrite 阶段，人可以编辑中间场景内容，或把生成结果作为写作灵感。这与 Dramatron 等层级式写作工具的思想一致，但本文把这种模块化改造成“角色模拟 + 重写”的叙事故事生成流程。

最后，作者把贡献概括为两点。第一，把 fabula 和 syuzhet 明确整合进一个故事生成流程，让系统先处理故事世界中的时间顺序，再处理读者看到的叙事顺序。第二，在多 Agent role-play 后加入 rewrite step，使角色模拟结果不会直接等同于最终故事，而是作为更可信的素材被重新组织。引言末尾还说明评价方式：作者将本文方法与两个 LLM 故事生成基线比较，并用 LLM-based automated evaluation 显示其在故事质量多个维度上更优。

**2 Related Work**

这里的“相关工作”不是在泛泛介绍整个故事生成领域，而是在回答一个很具体的问题：本文把“角色模拟 + 层级式故事生成 + LLM 自动评价”拼成一个系统，这三个组件在前人研究中分别有没有依据，本文又到底比前人多做了什么。

可以先把第二章读成一张定位表：

| 小节 | 作者要证明什么 | 对应本文组件 | 本文和前人差异 |
|---|---|---|---|
| 2.1 Simulating Characters with LLMs | LLM 可以扮演相对可信的角色，并维护人格、情绪、记忆、互动状态 | Character Agent 的合理性 | 前人多做角色聊天或虚拟人模拟；本文把角色模拟放进 story-writing pipeline，作为生成故事素材的中间步骤 |
| 2.2 Automatic Story Generation | 故事生成一直需要 plot/control，多 Agent 和层级式生成是常见路线 | Director Agent、scene-level plan、hierarchical generation | 前人多关注 screenplay、dialogue 或整体规划；本文关注给定 narrative plan 后，如何用 fabula 顺序模拟、再按 syuzhet 顺序重写 |
| 2.3 Automatic Story Evaluation | 故事质量不能只靠 ROUGE/BERTScore 这类参考相似度指标，LLM pairwise evaluation 是可用替代 | 实验评价方法 | 本文借用 Agents' Room 式的 LLM pairwise comparison，并通过交换 A/B 顺序缓解长文本位置偏差 |

所以，这章的真正作用是“搭桥”：2.1 说明角色 Agent 可行，2.2 说明故事生成需要可控的多阶段流程，2.3 说明后文为什么用 LLM evaluator 评估故事。它没有系统梳理所有相关论文，也没有逐篇深评代表工作。

**2.1 Simulating Characters with LLMs**

这一小节回答的是：为什么本文可以把“角色”做成 LLM Agent，而不是让一个单体 LLM 直接扩写大纲。

作者先给出叙事层面的理由：角色是很多故事的驱动力，故事不只是事件列表，角色如何行动、互动、暴露动机和发生变化，会直接影响情节是否可信。因此，如果系统能先生成符合角色逻辑的动作和对白，再把它们改写成故事文本，理论上会比直接从 outline 到 prose 更稳。

然后作者引用了几类 LLM 角色模拟工作。第一类是用更复杂的角色 prompt 或内部心理结构来提高可信度，例如 ego/superego 式内部冲突、psychological grounding、行为轨迹约束。第二类是把人格特质、日常 routine、情绪和社会互动纳入角色建模，使角色在连续互动中保持稳定。第三类是 Generative Agents 方向：Agent 带有过去互动记忆，能产生个体行为以及群体层面的 emergent social behaviours。

这里最重要的结论不是“LLM 会聊天”，而是“LLM 可以被包装成有设定、有记忆、有状态、有互动历史的角色”。本文借走的是这个能力：Character Agent 在 role-play 阶段根据自身目标、记忆、身体状态和 Director 命令生成动作与对白。

但本文也和这些角色模拟工作不同。前人常关心角色本身是否像真人、是否能互动、是否能在虚拟世界中持续行动；本文关心的是这些角色模拟结果能不能服务于 narrative story writing。也就是说，角色模拟在这里不是最终产品，而是后续 rewrite 的素材来源。

**2.2 Automatic Story Generation**

这一小节回答的是：故事生成领域里，为什么需要“计划、控制、多阶段生成”，以及本文为什么选 Dramatron 和 Agents' Room 作为比较对象。

作者开头先补上一个关键判断：有趣角色本身并不会自动形成好故事。角色必须在事件中被揭示和改变，普通互动才会变成 narrative。因此本文不是做开放式角色聊天，而是把角色互动嵌入一个有事件顺序、有场景计划的故事生成任务。

作者回顾的相关工作大致有三层。

第一层是早期故事生成：Propp 的叙事功能、planning-based story generation、author goal、character goal、interactive drama。这些工作共同说明，故事生成从一开始就不是单纯语言续写，而是要处理情节结构、角色目标和作者意图之间的控制关系。

第二层是神经/LLM 故事生成：Seq2Seq 到 LLM 提高了语言流畅度，但长故事仍容易在连贯性、一致性和上下文保持上出问题。为了解决这个问题，近期工作常用两种路线：多个 LLM 协作，或 hierarchical generation，把 plot planning 和 text generation 分开。

第三层是最接近本文的 agent-based / hierarchical systems。Dramatron 把剧本写作拆成 logline、characters、plot、locations、dialogue 等组件，说明模块化能提高可控性，也方便人类作者介入。IBSEN 用 director-actor 框架生成戏剧脚本，de Lima 等做 interactive storytelling，DramaEngine 和 Agents' Room 用多 Agent workflow 生成叙事。这些工作共同支撑本文的 Director Agent、Character Agents 和分阶段生成思路。

本文的差异主要有两个。第一，很多相近工作偏 screenplay 或 drama script，而本文处理的是 narrative story generation。第二，本文不是简单地“多 Agent 一起写故事”，而是把写作机制拆成两个有叙事学含义的阶段：先按 fabula，也就是故事世界时间顺序，让角色经历事件；再按 syuzhet，也就是文本呈现顺序，把 role-play history 重写成最终故事。这个点才是本文相对 Dramatron、Agents' Room 的核心定位。

**2.3 Automatic Story Evaluation**

这一小节回答的是：后文为什么不用传统文本指标，而是用 LLM 做 pairwise evaluation。

传统指标的问题在于，它们和故事质量不完全对齐。perplexity 更像是在看文本是否符合常见语言分布；ROUGE 和 BERTScore 依赖参考文本相似度。但故事生成通常没有唯一标准答案：同一个 prompt 可以写出多个合理故事，和 gold story 不像不代表质量差。更重要的是，故事质量包含 plot、creativity、character development、language use、coherence 等维度，传统相似度指标很难覆盖。

所以作者转向 LLM evaluator，尤其是 pairwise comparison：让评估器在同一条件下比较故事 A 和故事 B，而不是直接给绝对分。作者引用 Liusie et al.、Liu et al. 和 Zheng et al.，是为了说明 LLM 两两比较在 NLG 评价中已有使用，并且在一些设置下比绝对打分更接近人类判断。

作者也承认 LLM evaluator 有风险，尤其是长 prompt 的 “Lost in the middle” 效应。因为故事文本通常很长，评估 prompt 也会很长，模型可能受到 A/B 呈现顺序或位置的影响。本文后文的应对方式是交换两个故事的顺序做两次比较，即 A/B 和 B/A 都评估，以减少位置偏差。

第二章整体可以这样记：本文不是从零发明角色 Agent、故事规划、多 Agent 写作或 LLM 评价；它的贡献是把这些已有线索组合成一个专门处理 narrative plan 写作的两阶段系统。Related Work 的三小节分别给“角色能模拟”“故事要受控生成”“故事要这样评价”三个前提找依据。

**3 Methodology**

第三章是整篇论文的方法核心。作者要解决的不是“如何从零想出一个故事”，而是 outline-based creative writing：已有 narrative plan，系统负责把计划写成故事。方法的关键拆分是：先在故事世界时间中模拟事件，即 role-play；再在叙事呈现顺序中写成文本，即 rewrite。这样，角色知识和行为逻辑由 fabula 顺序保证，读者看到的叙事效果由 syuzhet 顺序控制。

**3.1 The Overall Task**

作者首先把任务限定在 writing phase：narrative plan 已经给定，系统只负责把计划实现为故事文本。这一点和 Dramatron、Agents' Room 等系统有关联，但本文关注的是“给定计划后的写作机制”，而不是完整的故事规划系统。换句话说，本文想比较的是不同系统如何把同一个计划扩写成故事，而不是谁更会构思故事。

这一节引入 fabula 和 syuzhet 的方法论意义。fabula 是故事世界中事件真实发生的时间顺序；syuzhet 是文本呈现给读者的顺序。本文的 role-play step 对应 fabula：角色 Agent 按时间顺序模拟事件，因此角色可以先经历时间上更早的事件，积累记忆和状态。rewrite step 对应 syuzhet：系统把 role-play 的中间产物重新组织为原始计划要求的呈现顺序，使故事仍然符合作者的叙事安排。

### Figure 1: 系统总览

![Figure 1](../assets/2025_multi-agent-based-character-simulation-for-story-writing_in2writing-2025/figures/figure_1_overview.png)

图 1 展示了这套方法的信息流。左侧 role-play step 中，Director Agent 根据 chronological outline $o_c$ 选择下一位角色并发出命令，Character Agents 生成动作和对白，形成 conversation history。右侧 rewrite step 中，系统把 presentation outline $o_p$ 和 conversation history 结合起来，写出最终 scene content。图中的重点是：role-play 不是最终文本，而是为 rewrite 提供角色行为素材；rewrite 也不是凭空扩写，而是受角色模拟结果和呈现大纲共同约束。

**3.2 Implementation Detail**

**3.2.1 The Definition and Agents**

论文先定义输入和基本单位。输入计划记作 $P_p$，它指定 scene 的 presentation order，因此代表 syuzhet。计划由若干 scene 构成，scene 是本文写作流程中的最小计划单位，记作 $S$。每个 scene 包含 presentation outline $o_p$，其中列出事件序列 $e$，同时包含地点信息和参与角色。

角色定义也服务于后面的模拟。角色可以是单个实体，也可以是一组次要支撑实体；其信息包括姓名、性别、年龄、叙事角色、背景设定、说话特征和角色目标。这里的 character goal 很关键，因为 role-play 阶段不只是让角色复述大纲，而是让角色在自己的目标约束下行动。

系统有两类 Agent。Director Agent 记作 $D$，负责控制场景发展：选择下一位发言或行动的角色 `next_speaker`，并给出下一步高层命令 `next_command`。Character Agent 记作 $A$，根据 Director 的命令、自身目标、身体状态和记忆来生成回应 `get_response`。角色回应采用第三人称视角，既包含对白，也包含动作描述，因此它更接近故事写作素材，而不是普通聊天记录。

这个 Agent 设计对应两种叙事控制力量。Director Agent 代表作者目标或剧情推进需求，防止角色自由聊天偏离大纲；Character Agent 代表角色目标和局部知识，防止故事变成单一模型机械扩写。两者结合后，系统既有计划约束，也有角色驱动的局部自然性。

**3.2.2 The Role-playing Step**

Role-play 阶段解决的是 fabula 生成问题。普通 LLM 方法可能直接按 outline 写某一节文本，而本文先把写作过程拆成角色模拟。由于故事的呈现顺序不一定等于事件发生顺序，输入计划 $P_p$ 中可能有两个场景 $S_i$ 和 $S_j$，其中 $S_i$ 在文本里先出现，但在故事世界中其实晚于 $S_j$。如果按 $P_p$ 直接写，角色可能在应该拥有某段经历之前就开口说话；如果把完整大纲直接暴露给模型，又可能提前泄露后文。

因此，作者定义 role-play plan $P_c$：它由 $P_p$ 中的场景按时间顺序重排而成，代表 fabula。系统用一个 LLM-based sorting algorithm 从 $P_p$ 生成 $P_c$。论文在这里做了一个重要假设：任意两个 scene $S_i, S_j \in S$ 在时间域中不重叠，即一个 scene 的所有事件都发生在另一个 scene 之前或之后。这个假设让 scene-level sorting 可行，但也限制了方法对复杂交错叙事的适应性。

除了 scene 之间排序，scene 内部也要排序。每个 scene 原本有 presentation outline $o_p$，它可能按叙事呈现方式组织，不一定适合角色扮演。系统再用 LLM 生成 chronological outline $o_c$，把同一 scene 内的事件调整为时间顺序，并使其更适合后续 character-based role-play。这样，$P_c$ 解决 scene 级时间顺序，$o_c$ 解决 scene 内事件顺序。

附录 B.1 里真正对应 “LLM-based sorting algorithm” 的是 prompt 调用。下面按原 prompt 的结构转写到这里，保留变量名、输入输出 schema 和约束，但不是逐字复刻论文原文。

#### Appendix B.1.1 Prompt: Scene Extraction

这个 prompt 是生成 $P_p$ 的前置步骤：先把 gold story 切成结构化 scenes，后面的 `Sort Scenes` 才有东西可排。

```text
Role:
  你根据写作指令、成文故事和角色列表，把整篇故事拆分成 scenes。

Inputs:
  1. <Writing Prompt>
     原始写作指令。

  2. <Story>
     根据该写作指令生成的完整 narrative。

  3. <Characters>
     故事中出现的大部分角色，格式遵循 {{input_story_characters_schema}}。

Task:
  基于 <Story>、<Characters>，并参考 <Writing Prompt>，覆盖整篇故事内容，
  将故事划分为若干 scenes。

Scene definition:
  一个 scene 是发生在同一地点和同一时间段内的故事单位。
  每个 scene 应该是自洽的，并推动故事向前发展。
  拆分时尽量考虑 exposition、rising action、climax、falling action、resolution
  这些 narrative arc / plot elements。

For each scene, return:
  1. name
     scene 的高层名称。

  2. outline
     scene 中动作、互动和戏剧事件的 bullet-point outline。
     outline 需要覆盖参与角色的重要行动和交互。

  3. plot_element
     从 exposition / rising action / climax / falling action / resolution 中选择。

  4. place
     scene 发生地点，需要具体、详细。

  5. importance
     1-10 的整数，表示该 scene 相对重要性。
     依据包括该 scene 在故事中的篇幅占比和情节意义。

  6. characters
     当前 scene 中在场的所有角色。
     同时为每个角色提供 scene-level CHARACTER GOAL。
     如果发现 <Characters> 中遗漏了 scene 里出现的角色，也要补充。

Reflection:
  拆分后检查是否覆盖了整个故事。
  如果有遗漏内容，需要添加 scene 或补充 scene details。

Output:
  JSON following {{OutScenesSchema}}.
```

#### Appendix B.1.1 Prompt: Sort Scenes

这个 prompt 对应正文里的 scene-level sorting：把 $P_p$ 中按呈现顺序排列的 scenes，重排成 fabula 时间顺序，得到 $P_c$。

```text
Role:
  你作为 creative writer，需要对 story scenes 做时间顺序排序。

Input:
  1. <StoryScenes>
     scene 列表，格式遵循 {{input_story_scenes_schema}}。

Task:
  根据每个 scene 的 outline，判断故事发展中的真实 chronological order。
  按时间顺序排列 <StoryScenes>。
  输出排序后的 scene names。

Output:
  JSON following {{sort_scene_results_schema}}.
```

#### Appendix B.1.2 Prompt: Chronological Outline Creation

这个 prompt 对应 scene 内部排序：把某个 scene 的 presentation outline $o_p$ 改成 role-play 使用的 chronological outline $o_c$。

```text
Inputs:
  1. <Scene>
     scene object，包含 scene outline、详细地点描述、参与角色/角色组信息，
     格式遵循 {{input_scene_schema}}。

  2. <Outline>
     当前需要调整的 scene outline。

Task:
  对 scene outline 的 bullet points 进行排序和轻量重写，
  使其适合 RPG / role-playing game 中的角色扮演。

Constraints:
  - 严格按事件发生顺序组织。
  - 避免 retrospective narration，例如不要把“回忆/转述过去事件”当作当前事件推进。
  - 聚焦 character-driven development 和 role-playing dynamics。
  - 事件序列要体现角色之间有意义的互动。
  - 输出格式尽量与原 outline 相似。
  - 事件必须是 chronological order，并用 present tense 表达。
  - 输出长度应接近原 <Outline>。
  - 不添加新事件，只能重排原 <Outline> 中已有事件。

Output:
  返回调整后的 bullet points，类型为 string。
```

因此，本文所谓 sorting algorithm 可以理解为两级 prompt-based temporal normalization：`Sort Scenes` 负责 scene 间排序，`Chronological Outline Creation` 负责 scene 内事件排序。论文没有给传统排序算法、时间图、pairwise comparator 或冲突检测；时间关系主要由 LLM 根据 outline 推断。

### Algorithm 1: Scene-level role-playing

![Algorithm 1](../assets/2025_multi-agent-based-character-simulation-for-story-writing_in2writing-2025/figures/algorithm_1_scene_role_playing.png)

Algorithm 1 描述单个 scene 的 role-play 循环。输入包括当前 scene $S_i$ 和角色 Agent 映射表 $M$。$M$ 的 key 是角色名，value 是对应 Agent 实例；如果角色已经在前面场景出现过，系统会复用同一个 Agent，从而保留跨场景累积的记忆和状态。

每个 scene 开始时，系统初始化聊天历史 $H$ 和 Director Agent。循环中，Director 先判断当前聊天历史是否已经覆盖 $S_i$ 的内容；如果没有结束，Director 选择下一位角色 Agent，并给出下一条命令。若这个角色已存在于 $M$，系统取出原 Agent；若不存在，则创建并加入 $M$。随后角色 Agent 更新自己的 memory 和 physical state，再根据聊天历史、命令、记忆、身体状态和 scene-level goal 生成回应，并把回应加入 $H$。

这里最值得注意的是状态更新机制。作者实现了 text-based memory 和 physical-state system，只基于该角色尚未看过的新聊天历史更新。角色回应时会综合 role-play history、Director 命令、记忆、身体状态和场景目标。这相当于在 author goal 与 character goal 之间做平衡：Director 的命令代表作者或剧情推进意图，角色的目标和记忆代表角色自身逻辑。第三人称输出则让 role-play 结果更容易被 rewrite 阶段转化为叙事文本。

**3.2.3 The Rewrite Step**

Rewrite 阶段解决的是 syuzhet 生成问题。role-play 输出虽然包含角色动作和对白，但它不是最终故事，原因有两个。第一，它按 fabula 顺序展开，而最终故事需要按照原计划 $P_p$ 的 presentation order 呈现。第二，role-play 记录更像模拟过程，可能有重复、冗余或不符合文学表达的部分，需要被整理成真正的 scene content。

作者明确指出，role-play 结果遵循 scene 内的 $o_c$ 和 scene 间的 $P_c$，但最终故事需要遵循原始 $o_p$ 和 $P_p$。因此可能出现 $o_c \ne o_p$、$P_c \ne P_p$ 的情况。这个不一致不是 bug，而是本文方法的核心：模拟阶段追求时间顺序，写作阶段追求叙事呈现顺序。

具体做法是：对每个 scene，系统提示 LLM 根据 presentation outline $o_p$ 写出 scene content，同时参考 role-play step 得到的模拟结果，尤其是角色对白和动作。最终 scene 按 $P_p$ 的顺序逐个生成，并且每个 scene 生成前作者可以修改上一场景内容或当前中间结果。这个模块化设计保留了人类写作者介入的空间，也减少了直接从大纲到成文的难度。

第三章的核心可以概括为一个转换链条：$P_p$ 表示作者计划的呈现顺序，系统把它转成 $P_c$ 和 $o_c$ 来做时间顺序上的角色模拟，再把 role-play history 和 $o_p$ 结合起来写回 $P_p$ 所要求的叙事顺序。方法的价值就在于把角色一致性和叙事呈现分开处理，而不是让一个 LLM 同时承担时间推理、角色模拟、信息披露和文学表达。

**4 Experiments**

第四章的目标是说明实验如何公平地比较本文方法、Dramatron 和 Agents' Room。这里作者并不是直接比较“谁从 prompt 写出的故事最好”，而是先从 gold story 反推出各系统需要的计划，再让三个系统基于计划写故事。这样设计的目的，是把评价重点放在 writing-from-plan 能力上：给定相近的故事计划，不同生成机制能否写出更好的最终故事。

实验可以压缩成一条链：

`Tell Me A Story prompt + human-written gold story` → `teacher LLM 反推 synthetic plan` → `三种系统基于各自 plan 写故事` → `Gemini 1.5 Pro 做 pairwise evaluation` → `Bradley-Terry 汇总相对强度`

这条链说明，本文实验并不是测试“模型能不能从一个 prompt 完整构思故事”，而是测试“当故事计划基本来自同一个 gold story 时，不同写作机制能不能把计划写成更好的故事”。因此，实验把 planning ability 尽量外置给 teacher LLM，把比较焦点放在 writing-from-plan。

**4.1 Dataset**

实验使用 Tell Me A Story 数据集。这个数据集来自 Google DeepMind/Agents' Room 相关工作，核心形态是 JSONL 中的 `complex writing prompt + human-written story`。也就是说，它不是只给模型一个题目，也不是只有自动生成文本，而是每个样本都有一个较复杂的写作指令和对应的人类写作故事。本文把这个人类故事称为 gold story，并把它当作反推计划的来源。

论文说 Tell Me A Story 总量为 230 个 prompt。作者没有直接使用全部 prompt，因为人工检查发现很多 prompt 只差少量词，直接使用会导致测试样本重复度较高，评价结果可能被某些相似题材放大。官方仓库也把该数据集定位为用于长篇叙事生成评估的复杂写作 prompt 与人类故事集合。

为减少这种重复偏差，作者先用 sBERT 为每个 prompt 生成句向量，再用 UMAP 降维，最后用 k-means 聚类。经过测试，作者认为 14 个 cluster 最适合这批数据。随后他们人工查看聚类结果，并选择 28 个代表性 prompt，使实验覆盖数据集中较丰富的故事类型，而不是集中在少数相似 prompt 上。

### Figure 2: Tell Me A Story prompt 聚类

![Figure 2](../assets/2025_multi-agent-based-character-simulation-for-story-writing_in2writing-2025/figures/figure_2_prompt_clusters.png)

图 2 展示了 prompt 聚类后的分布。每种颜色对应一个 cluster。它在实验中的作用不是作为模型输入，而是帮助作者抽取更有代表性的测试集。这个步骤让实验更像“覆盖不同故事类型的抽样”，而不是“从 230 个可能高度重复的 prompt 中直接取样”。

**4.2 Experiment Setup**

作者设置了两个基线。第一个是单 Agent/层级式基线 Dramatron，代表通过模块化流程逐场景写作的方式。第二个是多 Agent 基线 Agents' Room，代表用多个 Agent 协作生成叙事的方式。本文方法则是 character-simulation-based system，即先 role-play 再 rewrite。

实验整体被作者描述为 gold story 与 synthetic plan 之间的 back-translation。它的逻辑是：已知 writing prompt 和 gold story，先让 teacher LLM 从 gold story 中抽取或合成计划；然后把计划交给不同系统，让它们写出最终故事。这个设计避免了三种系统各自规划能力差异过大而干扰比较，因为作者关心的是“给定计划后如何写”，而不是“谁规划得更好”。

### Figure 3: 实验流程

![Figure 3](../assets/2025_multi-agent-based-character-simulation-for-story-writing_in2writing-2025/figures/figure_3_experiment_overview.png)

图 3 展示了实验的信息流：输入是 writing prompt 和 golden story；Teacher LLM 生成 synthetic plan；不同 writing systems 基于该计划输出 generated story。这个图的关键是中间的 synthetic plan，它把 gold story 转换成各系统可用的控制条件，从而让比较集中在写作阶段。

**4.2.1 Plan Synthesis**

计划合成是第四章最关键的公平性环节。不同系统需要的 plan 格式不同，因此作者分别为三种系统准备相应计划，但尽量共享信息来源。

对于 Agents' Room，作者把 writing prompt 和 gold story 输入 teacher LLM，也就是 O3-mini，生成 central conflict、characters、setting 和 plot。这里作者明确说遵循 Agents' Room 原工作中的 prompt 来抽取计划，因此这个基线尽量保持原方法设定。

对于本文系统，计划需要更细的角色和 scene 信息。作者首先用 O3-mini 从 gold story 中抽取出现过的全部角色；然后把 writing prompt、gold story 和抽取到的角色一起输入 O3-mini，得到 gold story 中发生的 scene 列表，也就是第 3 章定义的 $P_p$。此外，本文系统还使用与 Agents' Room 相同方式得到的 central conflict 和 setting。这样，本文方法既有自己的 scene-level plan，也共享部分全局故事信息。

对于 Dramatron，情况更复杂，因为 Dramatron 原本面向剧本/对白生成，并不直接提供本文这种 story scene plan。作者因此把本文系统抽取出的地点、角色信息以及 $P_p$ 中的 $o_p$ 序列共享给 Dramatron，使它能逐场景生成 narrative scene content。这个处理并不完美，但目的是让 Dramatron 在可比条件下完成同类写作任务。

这一小节可以理解为实验中的“计划对齐”：作者不是让每个系统自由规划，而是尽量从同一个 gold story 反推各自需要的计划格式。这样做的好处是比较更聚焦，风险是 synthetic plan 本身由 teacher LLM 生成，可能带有抽取误差或格式偏向。

**4.2.2 Writing Task**

写作任务设置强调公平性。所有系统都使用 GPT-4o，temperature 设为 0.9，frequency penalty 设为 0.2，并且都采用 zero-shot prompting。作者去掉 Dramatron 原来的 few-shot examples，因为保留示例会让它获得额外上下文，和其它系统不可比。

Agents' Room 的写作过程遵循原论文：创建五个 Agent，分别负责叙事弧中的 exposition、rising action、climax、falling action 和 resolution，最后把五个 Agent 的输出按顺序拼接成完整故事。这种方式的特点是按叙事阶段分工，但它不一定保证角色级记忆和局部信息披露一致。

Dramatron 的写作过程被作者改造为故事场景生成。原 Dramatron 更偏向 screenplay dialogue，本文实验需要 narrative story scenes，因此作者修改 prompt，让它根据地点、角色、plot element、summary 和 outline 写场景内容。除去这些必要改动，作者尽量保留 Dramatron 的 scene-by-scene generation 思路。

本文方法则使用第 3 章描述的完整流程：先根据 $P_p$ 得到按时间顺序组织的 $P_c$ 和 scene 内部的 $o_c$，进行角色 role-play；再按原 presentation order 重写各 scene。三种系统最后都输出故事文本，进入统一评价流程。

**4.3 Evaluation Method**

评价方法借鉴 Agents' Room 的 LLM-based evaluation。作者使用 Gemini 1.5 Pro 作为 evaluator，并采用 side-by-side pairwise comparison。评价维度包括 Plot、Creativity、Development、Language Use，另外还要求 evaluator 给出 Overall 判断。

这四个维度各自关注不同层面。Plot 关注故事是否有清晰结构、事件推进和逻辑一致性；Creativity 关注角色、主题、意象是否有吸引力，是否避免平庸模板；Development 关注角色和设定是否被充分介绍并具有可信细节；Language Use 关注语言是否丰富、多样、有文学表达效果。Overall 则是综合判断。

为了降低呈现顺序偏差，每一对故事会评估两次：一次 A 在前 B 在后，另一次交换顺序。这样做是对第二章提到的长 prompt 位置效应的回应。若两个顺序下判断一致，说明偏好较稳定；若不一致，系统不会把它当成强胜负，而是在后续汇总中自然降低其影响。

对每个评价维度 $c$，作者构造一个 win matrix $W^c$。若有 $N$ 个系统，矩阵大小为 $N \times N$，其中 $W^c_{i,j}$ 表示系统 $i$ 在维度 $c$ 上战胜系统 $j$ 的次数。随后作者使用 Bradley-Terry 模型把成对胜负线性化为 latent ability parameters，也就是每个系统在该维度上的相对 strength。最后按照 Agents' Room 的惯例，对 log strengths 做以 0 为中心的归一化展示。

第四章的重点不是证明本文方法已经赢了，而是交代“胜负如何被产生”。它通过代表性 prompt 抽样、teacher LLM 合成计划、统一写作模型设置、双顺序 pairwise evaluation 和 Bradley-Terry 汇总，建立了后文结果的评估框架。需要注意的是，这套实验强依赖 LLM 评估器和 synthetic plan，因此它更适合证明本文方法在该自动评价框架下有优势，而不是替代真实写作者的最终判断。

**5 Results**

第五章回答实验问题：在同样基于 synthetic plan 写故事的条件下，本文的“角色模拟 + 重写”是否比 Dramatron 和 Agents' Room 更好。作者给出两类证据：一类是 LLM evaluator 的成对偏好结果，另一类是人工查看生成故事后的定性分析。前者说明总体趋势，后者解释为什么这种方法在非线性叙事中更稳。

**5.1 LLM Evaluation Results**

LLM 评估显示本文方法在 Overall、Plot、Creativity、Development 和 Language Use 五个维度上都优于 Agents' Room 与 Dramatron。图 4 中的 system strength 是 Bradley-Terry 模型从成对胜负中估计出来的相对强度，而不是直接评分。本文方法在 Overall、Plot、Development 上分别约为 2.397、2.477、2.397，在 Creativity 和 Language Use 上约为 1.862、2.251；两个基线的数值明显更低。

### Figure 4: LLM 评估结果

![Figure 4](../assets/2025_multi-agent-based-character-simulation-for-story-writing_in2writing-2025/figures/figure_4_llm_eval_strength.png)

图 4 把 pairwise comparison 通过 Bradley-Terry 模型转成 system strength。本文方法在所有维度上最高，说明 LLM evaluator 更倾向于选择角色模拟加重写生成的故事。需要注意的是，纵轴不是“故事质量分数”，而是由胜负关系推出来的相对偏好强度。

附录 A 给出原始 win matrices。按系统顺序 Ours / Agents' Room / Dramatron，可整理为：

| 维度 | Ours vs Agents' Room | Ours vs Dramatron | Agents' Room vs Dramatron |
|---|---:|---:|---:|
| Overall | 41:15 | 47:9 | 33:23 |
| Plot | 42:14 | 47:9 | 32:24 |
| Creativity | 36:20 | 44:12 | 35:21 |
| Development | 41:15 | 47:9 | 33:23 |
| Language Use | 39:17 | 47:9 | 34:21 |

这个表的读法是：`41:15` 表示在 Overall 维度上，Ours 被评为优于 Agents' Room 的次数为 41，Agents' Room 被评为优于 Ours 的次数为 15。由于每对故事会交换 A/B 顺序评估两次，这些胜负数也反映了顺序扰动后的总体偏好。结果显示，本文方法对两个基线都保持优势；Agents' Room 也整体优于 Dramatron，但优势幅度小于本文方法对二者的优势。

作者特别提醒，Bradley-Terry strength 不能解读为“本文方法比基线好多少倍”。它更像消费者偏好试验中的选择倾向：评估器更频繁选择某个系统，不等于该系统每篇故事的绝对质量都大幅高出。作者还指出，交换故事呈现顺序后的结果大体一致；少数不一致往往出现在不同评价维度冲突的故事中，例如某个故事语言更好但情节更弱。本文的胜负汇总会把这种不一致视为弱信号，而不是强胜负。

**5.2 Qualitative Analysis**

定性分析解释了为什么两阶段方法有效。作者观察到，本文系统生成的故事通常更能保持 character consistency 和 narrative coherence。这个结论不是只看文字是否优美，而是看角色知道什么、何时知道、何时透露，以及这些信息是否符合故事的非线性结构。

论文举例 train-026：gold story 主要围绕 Scholar Kissen 与 Courier Aerie 的互动。第一场呈现的是两人初次会面，第二场则是 Aerie 回忆自己更早去远程遗址的经历。这是一个典型的非线性安排：文本中第二场叙述的经历，在故事世界时间上早于第一场中的会面。

这个案例对 Dramatron 不利，因为 Dramatron 逐场景写第一场时，模型还没有“经历”第二场中的遗址访问，容易在 Aerie 讲述相关信息时生成不可靠内容。附录 C 的样例显示，Dramatron 生成了关于营地状况的泛化对白，但没有准确承接 gold story 中更具体的设定。作者把这类问题视为 hallucination 或内容失真：模型被要求写出角色已经知道的信息，但它在生成流程中并没有获得足够的时间顺序依据。

Agents' Room 的问题相反。它更可能因为完整 story outline 已经在上下文中可见，而在第一场提前透露本应后文出现的信息。附录 C 中，Agents' Room 的内容提前提到破碎水晶方尖碑、古老铭文、Mage Myssa 等信息，这些细节在叙事节奏上应该稍后出现。也就是说，它拥有了过多全局信息，却缺少“当前场景应该披露多少”的控制。

本文方法在这个案例中更平衡。排序机制让 Aerie 在 role-play 阶段先按时间顺序经历遗址访问，因此当她在第一场会见 Kissen 时，角色记忆中已经有相关经历；rewrite 机制又要求最终场景严格对齐当前 scene outline，因此不会把后文细节全部提前说出。换言之，role-play 解决“角色是否知道”，rewrite 解决“文本是否该说”。这正好对应本文方法拆分 fabula 与 syuzhet 的主张。

作者也观察到其它质量问题。Agents' Room 有时会生成重复内容或随机离题词，作者认为原因是生成约束太弱：除了 plot line 之外，缺少更细的角色状态、场景级信息披露和行为约束。本文系统自身也有问题：group chat manager 有时在不满意角色回应时重复给同一命令，尤其出现在接近 scene outline 末尾的内容上。作者采用最多 10 轮迭代作为工程限制，以避免无限循环。

第五章的证据边界也要看清楚。LLM 评估和定性案例都支持本文方法更适合非线性叙事中的角色一致性控制，但这不是严格的人类写作者大规模评价。它说明在作者设置的自动评价框架和案例分析中，两阶段角色模拟确实减少了两类常见错误：Dramatron 式的时间知识缺失，以及 Agents' Room 式的过早信息披露。

**6 Conclusion**

结论部分的作用是把全文收束回一个核心命题：从 narrative plan 生成故事时，不应该直接把“事件真实发生顺序”和“文本呈现顺序”混在一个生成步骤里处理。作者认为本文的主要贡献在于第一次把 fabula 与 syuzhet 这两个叙事学概念整合进一个统一的故事生成流程：先按故事世界内部的时间顺序模拟角色经历，再按最终文本需要重排和改写内容。

具体来说，fabula generation phase 对应本文的 role-play step。系统让 LLM 支持的 Character Agents 在 Director Agent 的引导下，根据按时间排序后的计划进行角色扮演。这个阶段的重点不是直接写出最终故事，而是生成较自然的角色行为、对白和互动历史。这样做的意义在于，角色的记忆和身体状态可以沿着故事世界的时间推进而更新，角色在后续场景中的反应因此更有因果基础。

syuzhet modification phase 对应 rewrite step。系统不再让最终文本完全受 role-play 顺序限制，而是根据 presentation plan 把已经生成的对白和动作重新组织成目标叙事顺序。作者强调，这一步可以复用大部分 role-play 中得到的 dialogue 和 action，只需要在顺序、衔接和表达上进行调整。也就是说，最难的角色内容生成被前一阶段承担，最终写作阶段主要处理叙事呈现和语言组织，因此降低了直接生成复杂非线性故事的难度。

结论也明确给出当前方法的边界。第一，系统假设一个 scene 是发生在特定地点和时间范围内的一串事件，因此排序是在 scene 级别上完成的。但很多真实叙事会在同一场景中穿插现实对话、回忆、想象或转述，例如角色在当前对话中回忆过去事件。这时，简单的 scene-level sorting 未必能得到严格的时间顺序。作者提出的未来方向是做更细粒度的 event-level sorting，不再被 scene 边界限制。

第二，系统虽然会更新 Agent 记忆，让角色只保留自己“应该看到”的信息，但 role-play 过程本身没有显式 privacy control。换句话说，论文试图管理角色知道什么，却没有形式化地保证角色在群聊或交互过程中不会接触到不该知道的信息。这个问题和第五章中“提前披露未来信息”的风险相连：角色知识状态不仅要靠记忆更新维护，还需要更明确的信息访问控制。

第三，评估仍以 LLM evaluator 为主。作者说明评估标准参考了经过人类测试的 criteria，但本文目标只是考察 agent-based simulation 用于 story creation 的潜力。因此，结论没有把结果表述成已经充分替代人类写作者评价，而是把未来工作指向如何让 human participants 更有效地参与这个创作与评估流程。

总体来看，第六章把本文的技术贡献定位为一种“先模拟、后改写”的叙事生成框架。它的价值不在于单纯多 Agent 对话，而在于用时间顺序维护角色经历，再用呈现顺序控制最终文本。这也解释了为什么它在前文实验中尤其适合处理倒叙、回忆和非线性叙事：方法结构本身正是围绕“角色何时知道”和“文本何时说出”这两个问题设计的。

## 关键公式 / 图表

### 关键符号与关系

本文没有复杂的数学推导，核心是方法记号和评估矩阵。$P_p$ 表示输入的 presentation plan，即按文本呈现顺序排列的场景计划；$P_c$ 表示 role-play plan，即由 $P_p$ 重排得到的时间顺序计划。$S$ 表示 scene 集合，单个场景写作 $S_i$；论文假设任意两个场景 $S_i, S_j \in S$ 在时间域中不重叠。$o_p$ 表示单个场景的 presentation outline，$o_c$ 表示该场景内部按时间顺序重排后的 chronological outline。Rewrite 部分特别强调，模拟阶段可能遵循 $o_c$ 和 $P_c$，而最终文本需要遵循 $o_p$ 和 $P_p$，因此 $o_c \ne o_p$、$P_c \ne P_p$ 都是可能且合理的。

Algorithm 1 中，$M$ 是角色 Agent 映射表，key 是角色名，value 是对应 Agent 实例；$H$ 是当前 scene 的 chat history；$D$ 是 Director Agent；$A_i$ 是被选中的 Character Agent；$C_j$ 是 Director 发给该角色的下一条 command；$h_i$ 是角色生成并追加到 $H$ 中的回应。

评估部分中，$W^c \in \mathbb{R}^{N \times N}$ 是评价维度 $c$ 下的 win matrix，$W^c_{i,j}$ 表示系统 $i$ 战胜系统 $j$ 的次数。作者再用 Bradley-Terry 模型从这些成对胜负中估计每个系统的 latent ability / system strength。这里的 strength 是相对偏好强度，不是故事质量的绝对分数。

### 关键图

本笔记已将关键图片放在对应章节附近：Figure 1 位于 `3.1 The Overall Task`，Algorithm 1 位于 `3.2.2 The Role-playing Step`，Figure 2 位于 `4.1 Dataset`，Figure 3 位于 `4.2 Experiment Setup`，Figure 4 位于 `5.1 LLM Evaluation Results`。

### 关键表格

论文主体没有传统结果表。附录 A 的 win matrices 已整理到 `5.1 LLM Evaluation Results`；附录 C 的 consistency comparison 已融入 `5.2 Qualitative Analysis` 的案例解释。

## 实验结论

本文方法在 LLM pairwise evaluation 的五个维度上都领先两个基线。作者把优势归因于 character-based simulation：角色先按时间顺序经历事件，因此在非线性呈现中更容易保持知识状态和行为动机一致；rewrite 阶段再限制当前场景的披露内容，因此减少提前泄露后文信息的风险。定性案例支持这一解释，尤其是包含回忆或倒叙的故事。

实验设计的优势是比较清晰：三种方法都基于由 teacher LLM 从 gold story 反推的计划，评估集中在“根据计划写故事”。但它也意味着结果不等同于完整端到端故事创作能力，因为 planning 阶段是外部合成的。

## 局限性与可追问点

1. Scene 级时间排序假设较强。论文假设不同 scene 时间不重叠，但很多文学叙事会在同一 scene 中穿插回忆、想象、转述和现实对话，未来需要事件级而非 scene 级排序。
2. Role-play privacy control 不足。角色记忆会按“未见过的新历史”更新，但系统没有显式保证角色不能在群聊中接触不该知道的信息。
3. LLM evaluator 仍是主要证据。虽然作者采用 pairwise comparison 和 A/B 顺序交换，但缺少系统性人类写作者评价。
4. 成本与可扩展性没有充分展开。多 Agent role-play、记忆更新、身体状态更新和 rewrite 都需要多次 LLM 调用，长篇故事的计算成本和错误积累值得进一步评估。
5. Director Agent 的重复指令说明控制层还不稳定。最多 10 轮迭代只是工程止损，未真正解决“如何判断场景已经充分覆盖”的问题。

## 对我当前研究/项目的启发

这篇论文对“叙事型 Agent 记忆”很有参考价值。它把记忆从一般的对话历史检索问题，变成叙事时间中的角色知识状态维护问题：角色知道什么、何时知道、何时可以说出来，比单纯检索相关信息更重要。

如果要扩展这条线，可以考虑把论文中的 scene-level sorting 改成 event-level temporal graph：节点是事件，边表示先后、因果、知道/不知道、可披露/不可披露。Role-play 阶段沿事件时间推进，rewrite 阶段沿叙事呈现路径读取可披露信息。这样可以处理 flashback、嵌套回忆和多视角叙事。

另一个可复用点是 Director Agent 与 Character Agent 的职责分离。Director 代表作者意图和叙事约束，Character 代表局部目标、记忆和风格。这种结构适合与你已有的“timeline-constrained narrative agent memory”方向结合：记忆系统不只是保存角色经历，还要支持按作者计划进行 selective disclosure。
