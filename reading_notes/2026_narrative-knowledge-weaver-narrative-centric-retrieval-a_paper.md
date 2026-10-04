---
id: 2026_narrative-knowledge-weaver-narrative-centric-retrieval-a_paper
title: "Narrative Knowledge Weaver: Narrative-Centric Retrieval-Augmented Reasoning for Long-Form Text Understanding"
year: 2026
authors: []
venue: "Anonymous ACL submission"
field:
  - NLP
  - Information Retrieval
direction:
  - Narrative QA
  - RAG
  - Graph RAG
keywords:
  - Narrative Knowledge Weaver
  - NKW
  - narrative-centric RAG
  - storyline reasoning
status: reading
source_path: ../sources/2026_narrative-knowledge-weaver-narrative-centric-retrieval-a_paper.pdf
source_archive_path: ""
assets_path: ../assets/2026_narrative-knowledge-weaver-narrative-centric-retrieval-a_paper
paper_type: research
---

# Narrative Knowledge Weaver: Narrative-Centric Retrieval-Augmented Reasoning for Long-Form Text Understanding

## 一句话总结

NKW 将长篇叙事中的文本证据、原子事实、实体状态、事件/互动、episode 和 storyline 组织成带来源的多层资产，并在查询时按问题选择证据视图与阅读技能，以提升跨场景、跨时间和因果叙事问答。

## 研究问题

通用 RAG 通常按相似文本、实体或关系检索，难以判断证据在故事中的功能，也难以表示角色和关系随情节变化的状态。论文研究：如何构建叙事中心、可追溯的证据表示，并让查询时的检索控制匹配角色状态、时间顺序、因果动机和情节推进等问题需求。

## 核心方法

NKW 的离线阶段构建 canonical entity--relation graph，抽取 events、interactions、occasions 和 atomic facts，完成实体消歧与属性/状态增强，再将局部 narrative units 聚合为 episodes 和 storylines，并保留到源文本的 provenance。在线阶段先生成 snapshot preview，由 reasoner 输出约束、证据槽位、动作和一个 reading skill；skill reader 从文本、图和叙事视图组装证据，必要时最多请求一轮有界补充，并审计 actor、scope、polarity、state 和 temporal constraints。

## 分章节阅读笔记

1. Introduction  
2. Related Work  
3. The Narrative Knowledge Weaver Framework  
   - 3.1 Construction-Time Asset Building  
   - 3.2 Global Episode and Storyline Construction  
   - 3.3 Narrative-Grounded Retrieval and Reasoning  
4. Experimental Setup  
5. Experimental Results and Analysis  
   - 5.1 Main Results  
   - 5.2 Controlled Comparisons and Ablations  
   - 5.3 Skill and Tool Analysis  
6. Conclusion

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

## 局限性与可追问点

## 对我当前研究/项目的启发
