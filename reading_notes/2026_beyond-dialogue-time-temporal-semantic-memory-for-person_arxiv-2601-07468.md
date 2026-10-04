---
id: 2026_beyond-dialogue-time-temporal-semantic-memory-for-person_arxiv-2601-07468
title: "Beyond Dialogue Time: Temporal Semantic Memory for Personalized LLM Agents"
year: 2026
authors:
  - Miao Su
  - Yucan Guo
  - Zhongni Hou
  - Long Bai
  - Zixuan Li
  - Yufei Zhang
  - Guojun Yin
  - Wei Lin
  - Xiaolong Jin
  - Jiafeng Guo
  - Xueqi Cheng
venue: ""
field:
  - NLP
  - AI Agents
direction:
  - LLM Memory
  - Personalization
  - Retrieval
keywords:
  - Temporal Semantic Memory
  - TSM
  - semantic timeline
  - durative memory
  - personalized LLM agents
status: reading
source_path: ""
source_archive_path: ../sources/2026_beyond-dialogue-time-temporal-semantic-memory-for-person_arxiv-2601-07468_source.tar.gz
assets_path: ../assets/2026_beyond-dialogue-time-temporal-semantic-memory-for-person_arxiv-2601-07468
paper_type: research
---

# Beyond Dialogue Time: Temporal Semantic Memory for Personalized LLM Agents

## 一句话总结

本文提出 Temporal Semantic Memory (TSM)，把个性化 LLM agent 的长期记忆从“按对话发生时间存取”推进到“按事件真实发生时间与持续状态存取”，从而更好地支持多轮、多会话和时间敏感的用户记忆问答。

## 研究问题

论文关注个性化对话 agent 中记忆的时间建模问题。作者指出，现有记忆系统通常把聊天轮次发生的 dialogue time 当成主要时间信号，但用户在对话中常常谈论过去事件、未来计划或持续状态，事件的实际发生时间与对话时间并不总是一致。与此同时，许多方法把记忆保存为孤立的 point-wise entries，容易把一段连续经历拆成碎片，难以恢复持续时间、长期偏好和演化状态。这两个问题会导致 agent 在检索长期记忆时出现时间错位或上下文不完整，尤其影响 temporal reasoning、multi-session understanding 和 knowledge update 类问题。

## 核心方法

TSM 的核心是把记忆组织为“语义时间线 + 持续性记忆”的层级结构。构建阶段先从对话中抽取带有效时间的事实，形成 temporal knowledge graph (TKG)，用它记录 episodic memory；随后按时间片和语义相关性聚合实体与对话上下文，形成 topic 和 persona 两类 durative memory，用来表示跨时间持续存在的主题、偏好和用户特征。利用阶段先解析查询中的 semantic-time constraint，再在 topic、persona 和 raw dialogue chunks 中做 dense retrieval，并用时间过滤、TKG 证据映射和时间优先的 reranking 返回更符合查询时间意图的记忆。更新机制上，TSM 用轻量在线图更新维护事实和有效时间，再周期性进行 summary consolidation，降低长期运行中的更新成本。

## 分章节阅读笔记

### 1 Introduction

### 2 Related Work

### 2.1 Agent Memory

### 2.2 Graph-structured Memory

### 3 Methodology

### 3.1 Preliminary

### 3.2 Overview

### 3.3 Duration-aware Memory Construction

### 3.3.1 Episodic Memory Construction

### 3.3.2 Durative Memory Construction

### 3.4 Semantic-time Guided Memory Utilization

### 3.5 Hierarchical Memory Update

### 4 Experiments

### 4.1 Experimental Setup

### 4.2 Main Results

### 4.3 Ablation Study

### 5 Conclusions

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

## 局限性与可追问点

## 对我当前研究/项目的启发
