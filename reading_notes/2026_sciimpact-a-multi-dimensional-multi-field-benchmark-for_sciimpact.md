---
id: 2026_sciimpact-a-multi-dimensional-multi-field-benchmark-for_sciimpact
title: "SciImpact: A Multi-Dimensional, Multi-Field Benchmark for Scientific Impact Prediction"
year: 2026
authors: []
venue: ""
field:
  - Science of Science
direction:
  - Scientific Impact Prediction
keywords:
  - SciImpact
  - citation
  - award
  - patent
  - media
  - code
  - dataset
  - model
status: read
source_path: ../sources/2026_sciimpact-a-multi-dimensional-multi-field-benchmark-for_sciimpact.pdf
source_archive_path: ""
assets_path: ../assets/2026_sciimpact-a-multi-dimensional-multi-field-benchmark-for_sciimpact
paper_type: benchmark
---

# SciImpact: A Multi-Dimensional, Multi-Field Benchmark for Scientific Impact Prediction

## 一句话总结

SciImpact 将科学影响预测定义为跨 19 个领域、7 种影响维度的匹配对象成对排序任务，覆盖引用、奖项、专利、媒体、代码、数据集和模型影响。

## 研究问题

模型能否仅根据科研产物内容，在控制领域及时间等混杂因素后，判断两个匹配产物中哪一个未来会产生更高的特定维度影响？

## 核心方法

构造 215,928 个对比样本，对同领域且通常同年份、venue 或作者条件下的科研产物按至少两倍的实际影响差异配对，并用 pairwise accuracy 评价不同输入表示和语言模型的影响判断能力。

## 分章节阅读笔记

### 1 Introduction

论文指出，引用数只是科学影响的一种代理，无法覆盖奖项认可、专利转化、媒体传播以及代码/数据集/模型采用。SciImpact 将影响预测定义为 matched artifact pair 的二分类：在同领域、通常同年份的两个产物中判断哪个未来影响更高，从而控制领域和时间等混杂因素。

### 2 Related Work

相关研究从引用预测扩展到奖项、专利、媒体和开放源代码采用，但多集中于单一指标或少数领域。SciImpact 的差异在于把七种影响维度和 19 个领域放入同一 benchmark，并用统一 pairwise protocol 评测 LLM。

### 3 SciImpact Benchmark

每个实例是 `(A+, A-)`，其中 `A+` 在指定影响维度上的信号至少达到阈值，`A-` 的信号更低。数据整合 OpenAlex、MAPLE、奖项来源、专利与媒体数据、GitHub stars、Hugging Face downloads 等，并经过候选检索、影响标注/配对和质量过滤。

#### 3.1 Impact Dimensions and Pair Construction

覆盖 Citation、Award、Patent、Media、Code、Dataset、Model 七个维度。除 Award 外，其他维度用计数阈值和至少两倍差距配对；Award 用是否获奖的布尔标签。所有 pair 要求发表年份一致，降低年龄和累积曝光对模型判断的直接影响。

#### 3.2 Multi-field Coverage and Data Processing

样本跨计算机科学、生物、商业、化学、经济、工程、环境、地理、地质、历史、材料、数学、医学、哲学、物理、政治、心理和社会科学等 19 个领域。论文对网页数据做 DOI/实体匹配、去重和缺失字段爬取，但不同平台的统计口径仍不完全一致。

### 4 Experiments

作者评估 11 个 LLM，并用跨维度数据进行 multi-task instruction tuning，比较闭源模型、开源 base model 和 SFT-Qwen3-4B/LLaMA-3.2-3B。输入主要是截断的论文/工件文本，主指标是 pairwise accuracy。

#### 4.1 Main Results

影响维度差异明显：Best Paper Award 最容易预测，Patent 和 Media 更难，因为后者受市场时机、社会关注和外部网络影响，文本线索不足。SFT-Qwen3-4B 在平均表现上持续超过较大的开源 baseline，部分情况下也超过闭源模型，说明任务定向监督比参数规模更关键。

#### 4.2 Dimension and Field Analysis

模型在不同领域和维度的表现不均匀。Chemistry、Medicine、Physics 等领域通常比 Computer Science/Other Fields 更容易，奖项维度也因标签与文本评价标准更接近而更稳定。引用预测在 2001–2020 不同年代没有显著难度趋势，说明文本-only 设置中年龄线索被较好控制。

#### 4.3 Scaling and Multi-task SFT

单维训练已能改善对应指标，多维联合训练则通常带来更好的平均 accuracy，说明不同影响信号之间存在可共享的文本模式。另一方面，模型可能学习到领域/奖项的表面线索，因此跨领域和时间外推仍需谨慎验证。

### 5 Conclusion

SciImpact 建立了一个覆盖七种影响维度、19 个领域和 215,928 个对比样本的科学影响 benchmark。结果表明，科学影响是多面的：文本可以较好支持奖项等评价线索，但难以单独预测专利和媒体等外部采用。小型 SFT 模型在任务定向训练后可以超过更强通用模型，说明 benchmark 适合研究可解释的影响判断能力；但 pairwise accuracy 不是绝对影响预测，也不能把模型分数当作科研价值判断。

## 关键公式 / 图表

### 关键图

Figure 1 对比 o4-mini、Qwen3-4B 和 SFT-Qwen3-4B 在七个影响维度上的表现；Figure 2 展示 candidate retrieval、impact labeling/pair generation 和 quality control 的数据构建流程；Figure 4 分析不同发表年份的 citation accuracy。

### 关键表格

## 实验结论

SciImpact 的证据链是：多维 benchmark 能揭示影响判断的异质性；任务定向 SFT 有效；外部影响维度比奖项/引用更难由文本推断。结论适用于该数据构造和文本输入设置，不代表模型真正掌握科学价值或未来因果机制。

## 局限性与可追问点

- 文本截断到约 1,000 words，可能丢失方法、实验和 artifact 细节。
- 某些影响信号来自公开平台，存在平台偏差、机构偏差和时间累积偏差。
- pairwise 二分类无法提供绝对影响预测或大规模候选排序。
- 预训练语料可能包含获奖论文等 canonical artifacts，削弱 prospective forecasting 的纯度。
- 在 funding、hiring 或 promotion 等高风险场景使用会触发 Goodhart 效应，不应把预测当作规范性评价。

## 对我当前研究/项目的启发

科研影响评估应把 citation、adoption、award 和 public attention 分开建模，先做 matched pair 再分析跨领域泛化；同时需要保留数据时间边界和平台来源，避免把历史曝光与论文内在质量混为一谈。
