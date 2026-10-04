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
status: skimmed
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

### 2 Related Work

### 3 Problem Formulation

### 3.1 Agents with Memory Mechanisms

### 3.2 Scope of Memory Evolution: In-Episode and Cross-Episode

### 3.3 Content of Memory Evolution: Knowledge and Execution

### 4 Benchmark Construction

### 4.1 In-Episode Knowledge Evolution

### 4.2 In-Episode Execution Evolution

### 4.3 Cross-Episode Knowledge Evolution

### 4.4 Cross-Episode Execution Evolution

### 5 Experiments

### 5.1 Experiment Setup

### 5.2 Main Results

### 5.2.1 In-Episode Knowledge Evolution

### 5.2.2 In-Episode Execution Evolution

### 5.2.3 Cross-Episode Knowledge Evolution

### 5.2.4 Cross-Episode Execution Evolution

### 5.2.5 Summary

### 6 Conclusion

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

## 局限性与可追问点

## 对我当前研究/项目的启发
