# Problem Formulation

## 研究对象

我们研究的不是一般的 long-form story memory，而是：

> Narrative memory as constrained generation / constrained realization.

给定完整真实故事世界，系统需要在写作过程中选择哪些事实可以被当前文本使用、哪些必须隐藏、哪些只能通过某个角色的误解或局部观察呈现。

## 三类 Memory

### M1: Truth Memory

按真实时间顺序组织的实际世界记忆。

包含：

- event timeline；
- causal links；
- character physical states；
- locations；
- object ownership；
- secrets and hidden truths；
- author-level omniscient facts。

### M2: Character Memory

每个角色各自拥有的主观记忆。

它不是 M1 的简单子集，因为它还包含推断和误解：

> M2_i = visible subset of M1 + heard facts + inferred beliefs + false beliefs.

M2 决定当前 POV 中哪些信息可以被角色知道、说出、行动依据化。

### M3: Discourse Memory

按写作顺序/读者阅读顺序组织的呈现记忆。

包含：

- discourse order；
- reader-known facts；
- reveal schedule；
- foreshadowing；
- suspense and ambiguity；
- scene/POV history；
- planned twist or delayed revelation。

M3 是 M1 的重组，但必须受 M2 和叙事目的约束。

## 核心生成约束

给定 M1、{M2_i}、当前 discourse position d、当前 POV character c、narrative goal g，生成下一段文本 y，需要满足：

1. **Truth consistency**：y 不违反 M1 中的真实时间、因果和物理状态。
2. **Epistemic consistency**：y 不让 POV 角色 c 使用 M2_c 中没有的信息。
3. **Discourse consistency**：y 不提前泄露 M3 中尚未揭示给读者的信息。
4. **Narrative-goal consistency**：y 服务 g，例如悬念、伏笔、误导、反转、节奏。
5. **State update correctness**：生成后正确更新 M3 和相关角色 M2。

## 与已有工作的边界

### 与 Multi-Agent Character Simulation

一句话：

> 它把写作呈现顺序当作给定 presentation outline 和最终 rewrite 目标；我们把 M3 当作可调、可更新、可验证的 discourse state，研究如何在角色知识边界和叙事目标约束下从 M1 受限生成 M3。

更具体地说，它已有 chronological fabula、syuzhet rewrite 和 character memory，但没有把 M1/M2/M3 的关系形式化为 constrained generation，也没有系统评测 future leakage、POV leakage、belief contradiction 和 reveal schedule control。

### 与 Temporal Semantic Memory

TSM 解决的是：

> 事件被提及的对话时间不等于事件真实发生时间。

本课题解决的是：

> 事件在真实世界已发生，但读者尚未读到、角色可能不知道；系统必须记住真相，同时在错误 discourse/POV 下禁止使用真相。

### 与 Rashomon Memory

Rashomon Memory 解决多解释视角并存和协商。

本课题解决角色知识边界：

> 不同角色在同一真实世界中拥有不同且可能错误的主观记忆，生成时需要避免角色越界知道作者真相。

### 与 DOME

DOME 的 temporal KG memory 主要服务长篇故事全局一致性。

本课题强调：

> 全局一致性不等于叙事正确性。叙事正确性要求系统知道完整真相，但在特定 POV 和 reveal schedule 下主动不使用某些真相。

## 推荐论文表述

英文：

> We formulate narrative memory as constrained generation over truth, character, and discourse memories, where correct story writing requires realizing truth-level events into discourse-time text while respecting character-specific knowledge boundaries and authorial reveal goals.

中文：

> 我们将叙事记忆形式化为真实记忆、角色记忆和呈现记忆之间的受限生成问题：系统需要把完整故事真相实现为写作顺序上的文本，同时遵守角色知识边界和作者揭示目标。

