---
id: 2026_evomembench-benchmarking-agent-memory-from-a-self-evolvi_arxiv-2605-18421
title: "EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective"
year: 2026
authors: []
venue: ""
field:
  - NLP
direction:
  - LLM Agents
keywords:
  - Agent Memory
  - Self-Evolving Agents
  - EvoMemBench
status: read
source_path: ../sources/2026_evomembench-benchmarking-agent-memory-from-a-self-evolvi_arxiv-2605-18421.pdf
source_archive_path: ""
assets_path: ../assets/2026_evomembench-benchmarking-agent-memory-from-a-self-evolvi_arxiv-2605-18421
paper_type: benchmark
---

# EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective

## 一句话总结

EvoMemBench 是从自演化视角评测 LLM Agent 记忆的基准，考察记忆在任务内和跨任务时，如何支持知识更新与执行经验复用。

## 研究问题

现有评测对知识保留、更新和行动支持的覆盖不完整；论文研究不同记忆机制何时改善任务表现、何时引入干扰，以及记忆形式与任务需求是否匹配。

## 核心方法

以任务内／跨任务、知识／执行两个维度构成四类评测，选用或重构六个数据集。任务覆盖信息保留与修订、多轮工具调用、共享背景知识学习、网页搜索和具身交互。比较 15 种记忆方法，以 DeepSeek-V3.2 作为记忆增强 Agent 的统一骨干，同时加入强长上下文基线，评估准确率、成功率和 token 成本。来源：原文第 3–5 节；本次查看 v2（2026-06-15）。

## 分章节阅读笔记

### 1 Introduction

论文指出，许多 memory benchmark 只问 agent 能否记住信息，却没有区分记忆是在当前 episode 内即时更新，还是跨 episode 累积；也没有区分保存事实知识与改进行动策略。EvoMemBench 用两个正交轴把这四种能力拆开，目标是测量 memory 是否真正支持 agent evolution。

### 2 Related Work

相关工作包括长期对话记忆、持续学习、tool-use agent、网页检索和具身交互 benchmark。作者认为现有数据集往往固定一种记忆范围或任务类型，导致不同方法的优势难以比较；EvoMemBench 的贡献是把知识变化和执行变化放入统一矩阵。

### 3 Problem Formulation

论文将 agent memory evolution 定义为：在任务过程中或任务之间，系统利用历史信息改变后续知识状态、行动选择或两者。评测既看最终成功率/准确率，也看更新是否引入干扰以及 token 成本。

### 3.1 Agents with Memory Mechanisms

记忆增强 agent 由统一的 DeepSeek-V3.2 backbone、记忆写入/检索模块和任务执行器组成；同时设置 memory-free 与长上下文基线。这样可以把模型能力、上下文长度和显式 memory 的贡献分开。

### 3.2 Scope of Memory Evolution: In-Episode and Cross-Episode

In-episode 任务要求 agent 在同一任务链中吸收新信息或修正策略；cross-episode 任务要求早期任务的经验在后续独立任务中继续生效。前者测试即时适应，后者测试真正的长期积累与迁移。

### 3.3 Content of Memory Evolution: Knowledge and Execution

Knowledge evolution 关注事实、规则、背景和用户信息的保持与修订；execution evolution 关注工具调用顺序、网页操作和具身动作策略的改进。两者可能脱钩：记住正确事实不等于能按正确流程行动。

### 4 Benchmark Construction

基准组合六个任务来源，覆盖文件/车辆/交易等知识任务、网页搜索、工具调用和具身交互。每类任务都设计了信息首次出现、后续修订或策略反馈，使测试不仅是静态 QA，而是带有时间顺序的学习过程。

### 4.1 In-Episode Knowledge Evolution

该设置在一个 episode 内逐步提供新事实或冲突修订，考察 agent 能否更新记忆并在后续问题中使用最新版本。错误地保留旧事实或把新信息覆盖到错误实体，都会造成可诊断的更新失败。

### 4.2 In-Episode Execution Evolution

该设置让 agent 在连续工具/网页/具身任务中获得动作反馈，观察它是否能从前一轮失败中调整下一轮策略。指标关注任务成功、重复错误和额外 token，而非只看最后一次结果。

### 4.3 Cross-Episode Knowledge Evolution

跨 episode 知识任务把学习阶段和测试阶段分开，要求 agent 将早期获得的规则、背景知识或用户信息迁移到新的任务实例。该设置可以检验记忆是否可复用，以及旧知识是否会污染无关任务。

### 4.4 Cross-Episode Execution Evolution

跨 episode 执行任务考察策略经验能否迁移到新环境或相近任务，例如网页操作和具身动作。它比单 episode 试错更接近 self-evolving agent，因为系统需要在任务之间保留“怎么做”的程序性经验。

### 5 Experiments

实验统一使用 DeepSeek-V3.2，对比 15 种记忆方法、无记忆 agent 和长上下文基线，并报告准确率/成功率与 token 成本。重点不是给出一个绝对排行榜，而是揭示不同 memory design 在四类 evolution setting 下的能力错位。

### 5.1 Experiment Setup

作者将每种方法接入相同的 agent 执行接口，尽量控制 backbone、任务顺序和提示格式。实验还报告不同任务域、跨域迁移和成本统计，以区分“记住了”与“记住后真的改善行动”。

### 5.2 Main Results

结果显示没有一种 memory method 在四个象限都占优。方法往往在知识保留任务上表现较好，但在执行演化或跨 episode 迁移上明显下降；强长上下文基线在部分 in-episode 任务有优势，却不能替代显式的长期写入和检索。

### 5.2.1 In-Episode Knowledge Evolution

当前方法在同一 episode 内更新事实的能力相对成熟，但冲突修订、时间顺序和实体绑定仍会造成错误。说明“能召回相关文本”与“能判断新旧知识优先级”是不同能力。

### 5.2.2 In-Episode Execution Evolution

动作反馈的利用更加不稳定。许多系统可以记录失败描述，却没有把它转化成下一步可执行策略，导致重复调用错误工具或重复无效动作。

### 5.2.3 Cross-Episode Knowledge Evolution

跨任务知识迁移会受到记忆污染和任务边界影响。方法若过度压缩历史，容易丢失条件与例外；若保存过多原文，则检索噪声和 token 成本上升。

### 5.2.4 Cross-Episode Execution Evolution

这是最困难的设置之一。程序性经验需要保留适用条件、动作顺序和失败触发点，而简单事实摘要通常无法支持策略迁移。结果说明 agent memory 的长期提升不能只靠扩大存储容量。

### 5.2.5 Summary

四类设置共同表明，memory evaluation 应同时报告 scope、content、迁移和成本。单一 overall accuracy 会掩盖“知识记忆强、执行演化弱”或“任务内有效、跨任务失效”的结构性差异。

### 6 Conclusion

EvoMemBench 提出一个由 memory scope（in-episode/cross-episode）和 memory content（knowledge/execution）组成的四象限基准。实验显示，当前记忆方法距离通用 self-evolving agent 仍有明显差距，尤其在跨 episode 的程序性执行演化上。论文的价值主要是建立诊断坐标系：未来方法需要说明自己改善的是事实保持、知识修订、即时行动还是长期策略迁移，而不能只报告一个混合分数。

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

当前系统在任务内知识更新上相对可靠，在跨任务执行经验复用上最弱；长上下文能帮助局部记忆，但不能自动解决记忆筛选、冲突处理和策略迁移。EvoMemBench 因此更像能力分解基准，而不是证明某个方法已经解决 agent memory。

## 局限性与可追问点

- 统一 backbone 和固定任务顺序限制了对模型规模、推理风格和在线学习策略的外推。
- 不同 memory 方法的工程实现和提示质量可能影响比较公平性。
- benchmark 仍以离散任务为主，长期开放环境中的记忆衰减、删除和安全风险需要额外测试。

## 对我当前研究/项目的启发

实验设计应把记忆能力拆成“任务内/跨任务”和“事实/程序性”两个轴，并单独记录成功率、旧知识污染、重复错误和 token 成本。对于 procedural memory，必须测试经验能否改变下一次动作，而不是只验证文本是否被召回。
