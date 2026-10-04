---
id: 2022_guiding-neural-story-generation-with-reader-models_arxiv-2112-08596
title: "Guiding Neural Story Generation with Reader Models"
year: 2022
authors:
  - Xiangyu Peng
  - Kaige Xie
  - Amal Alabdulkarim
  - Harshith Kayam
  - Samihan Dani
  - Mark O. Riedl
venue: "AAAI 2022"
field:
  - Natural Language Processing
  - Artificial Intelligence
direction:
  - Story Generation
  - Reader Modeling
keywords:
  - StoRM
  - reader model
  - story generation
  - knowledge graph
status: read
source_path: ../sources/2022_guiding-neural-story-generation-with-reader-models_arxiv-2112-08596.pdf
source_archive_path: ""
assets_path: ../assets/2022_guiding-neural-story-generation-with-reader-models_arxiv-2112-08596
paper_type: research
---

# Guiding Neural Story Generation with Reader Models

## 一句话总结

StoRM 从故事文本增量抽取并扩展 commonsense knowledge graph，用一组候选 reader graphs 引导续写兼顾局部连贯和 story-world goal。

## 研究问题

神经生成器容易产生局部因果断裂或偏离预设结局；作者希望以外显、随文本更新的结构约束候选，而非只按语言模型似然续写。

## 核心方法

系统用 OpenIE、SRL、coreference 从文本抽图，再以 ConceptNet/ATOMIC 扩展实体与事件。RoBERTa infilling 产生候选句，每个候选更新一张图；beam search 保留 K 个 reader models，用图对 goal 的可达/奖励和局部关联选择。这里的 reader model 是故事知识图，不是角色心智或真实读者认知模型。

## 分章节阅读笔记

### 1 Introduction

论文将贡献定义为一种能显式表示读者已从文本推断出什么的 generation guidance，并以 storyworld goal 作为全局目标。

### 2 Related Work and Background

对比 plot planning、commonsense grounding 和 goal-oriented story generation；StoRM 的不同点是每一步都更新候选图，而不是只在开始生成固定 plot。

### 3 Reader Model Guided Story Generation

3.1 获取知识图；后续步骤扩展 commonsense、计算 goal reward 并生成候选。beam 中保存多张图，避免单一早期抽取路径锁死后续生成。

### 4 Experiments

使用 ROCStories 98,159 条五句故事、WritingPrompts（平均 59.35 句）和 695 篇 fairy tales（平均 24.80 句）。每个数据集随机抽 15 篇做人类成对比较。相对 CP，WritingPrompts logical sense 胜/负/平 72.0/18.7/9.3%，enjoyable 52/40/8%，fluency 74.7/18.7/6.7%；相对 C2PO 的逻辑优势在 ROCStories 为 72.9/17.1/10%，fairy tales 为 58.7/22.7/18.7%。Goal/quality 多数也占优，但并非全部显著。

### 5 Conclusion

作者认为 reader graph guidance 改善 coherence 与 goal achievement，同时保留一定开放性。

### 6 Broader Impact

指出训练数据偏见、错误常识和虚构内容被误用的风险。

### Appendices A-F

补充抽取、commonsense relations、候选生成、训练与 baseline 细节。255 个 triplets 的人工检查 precision 81.96%、recall 72.89%，说明图不是 oracle。论文只链接工具与 baseline repositories，未给 StoRM 自身公开代码。

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

显式 story KG 在当时模型与小规模人评下能改善多项相对指标；证据规模和年代不足以证明现代长上下文 LLM 下仍同样有效。

## 局限性与可追问点

每数据集人评仅 15 篇；抽取误差传播；commonsense expansion 可能引入未经文本授权的事实。reader 命名容易掩盖它不含角色、观察权限、authority、discourse reveal 或 branch semantics。

## 对我当前研究/项目的启发

StoRM 是 graph-expanded generation baseline 的早期证据，适合启发 A13。比较必须匹配输入和预算，并把 extracted/inferred graph 与 oracle state 分开；不能把它作为 character-mind view 的先例。
