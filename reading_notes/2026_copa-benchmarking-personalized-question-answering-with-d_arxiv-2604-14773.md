---
id: 2026_copa-benchmarking-personalized-question-answering-with-d_arxiv-2604-14773
title: "CoPA: Benchmarking Personalized Question Answering with Data-Informed Cognitive Factors"
year: 2026
authors:
  - Hang Su
  - Zequn Liu
  - Chen Hu
  - Xuesong Lu
  - Yingce Xia
  - Zhen Liu
venue: "ACL 2026"
field:
  - NLP
  - Education
direction:
  - Personalized Learning
  - Educational Question Answering
  - AI Evaluation
keywords:
  - CoPA
  - CIPD
  - personalized QA
  - Cognitive Trust
  - Situational Anchoring
  - Schema Consistency
  - Cognitive Load Management
  - Metacognitive Scaffolding
  - Affective and Motivational Resonance
status: reading
source_path: ../sources/2026_copa-benchmarking-personalized-question-answering-with-d_arxiv-2604-14773.pdf
source_archive_path: ""
assets_path: ../assets/2026_copa-benchmarking-personalized-question-answering-with-d_arxiv-2604-14773
paper_type: benchmark
---

# CoPA: Benchmarking Personalized Question Answering with Data-Informed Cognitive Factors

## 一句话总结

CoPA 从社区共识与个体选择分歧中数据驱动地提炼六个认知偏好因素，并用 1,985 个用户画像建立细粒度 personalized QA 评测，使“回答是否个性化”从词面相似度转向用户认知需求对齐。

## 研究问题

现有 personalized QA 评测主要依赖 BLEU/ROUGE 等词面重合、用户历史的启发式相似度或通用 LLM-as-a-Judge prompt，缺少由真实用户选择验证的评价维度。论文研究能否利用 Community-Individual Preference Divergence（CIPD），即提问者接受的答案不同于社区最高票答案，发现决定个体偏好的稳定认知因素，并据此建立可区分个性化质量的 benchmark。

## 核心方法

作者从约 680 万条 StackExchange 问题中筛得 626,786 条 CIPD 相关问题和 15,963 名用户，使用最多 50 条历史交互、当前问题、接受答案及其他候选答案，让 LLM 推断用户选择背后的 rationale；再通过多模型重复归纳、频率共识和心理学专家核验，得到 Cognitive Trust、Situational Anchoring、Schema Consistency、Cognitive Load Management、Metacognitive Scaffolding、Affective and Motivational Resonance 六个因素。

CoPA 从中构建 1,985 个用户的交互画像，以 LLM 将每位用户映射到六维 factor profile，并由 evaluator LLM 使用 0/1/2 三点 Likert 量表逐维判断生成回答与画像的对齐程度。实验比较无个性化、时间历史、RAG 历史和压缩用户画像等方法，并通过 accepted-vs-top-voted 区分、外部数据集迁移、消融与小规模人工标注验证该评价框架。

## 分章节阅读笔记

### 1 Introduction

### 2 Analysis of CIPD Phenomenon

### 3 Factor distillation

### 4 The CoPA Benchmark

### 4.1 Benchmark Construction

### 4.2 Evaluated Approaches

### 5 Experiments

### 5.1 Experimental Setup

### 5.2 Effectiveness of Factors

### 5.3 Generalizability of the Factors

### 5.4 Factor-level evaluation of personalized QA approaches using CoPA

### 5.5 Human Validation of CoPA Scoring

### 5.6 Factor Correlation Analysis

### 6 Related Work

### 7 Conclusion

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

## 局限性与可追问点

## 对我当前研究/项目的启发
