---
id: 2026_11697-p2p-automated-paper-to-p_11697-p2p-automated-paper-to-p
title: "P2P: Automated Paper-to-Poster Generation and Fine-Grained Benchmark"
year: 2026
authors:
  - Tao Sun
  - Enhao Pan
  - Zhengkai Yang
  - Kaixin Sui
  - Jiajun Shi
  - Xianfu Cheng
  - Tongliang Li
  - Wenhao Huang
  - Ge Zhang
  - Jian Yang
  - Zhoujun Li
venue: "ICLR 2026"
field:
  - Multimodal Evaluation
  - Human Preference Modeling
direction:
  - LLM-as-a-Judge
  - Human-Aligned Scoring
keywords:
  - XGBoost
  - human annotation
  - rubric features
  - holistic score
status: read
source_path: ../sources/2026_11697-p2p-automated-paper-to-p_11697-p2p-automated-paper-to-p.pdf
source_archive_path: ""
assets_path: ../assets/2026_11697-p2p-automated-paper-to-p_11697-p2p-automated-paper-to-p
paper_type: research
---

# P2P: Automated Paper-to-Poster Generation and Fine-Grained Benchmark

## 一句话总结

P2P EVAL 将主观整体质量评分拆成 10 个离散、可解释的 LLM 特征，再用 1,701 条人类整体评分训练 XGBoost 学习人类对这些维度的非线性权重；论文报告该混合模型比直接 LLM 整体打分更接近人类评分。

## 研究问题

如何评估从论文自动生成的学术海报，使客观内容保真与主观整体质量分开，并让主观质量分数更接近人类判断？

## 核心方法

- Universal Poster Evaluation：LLM 对 U1--U10 十个固定维度分别给 0--5 分。
- 人类标注：三名标注者独立给 0--50 的整体分，先培训并提供区间锚点；明显分歧样本剔除。论文报告 Krippendorff's alpha=0.95、Spearman=0.96、Cohen's kappa=0.71，共 1,701 条人类评分。
- 聚合器：用 10 个 LLM 维度分作为输入，以人类整体分为标签训练 200 棵树的 XGBoost，并做 10-fold cross-validation；报告 R2=0.92、KL=0.1093、JS=0.0239。直接 LLM 整体打分的 R2=0.27，LLM 回归器=0.51，微调 LLM 聚合器=0.70。
- 数据泄漏控制：人类评分来自去掉 checker/reflection 的 ablated system variant，而非最终系统输出。

## 分章节阅读笔记

### 1 Introduction

论文把海报质量分成 objective fidelity 与 subjective quality，强调单一自动指标不足以覆盖二者。

### 2 Methodology

P2P 是 Figure、Section、Orchestrate 三类 agent 加 checker-reflection 的多 agent 生成流程。

### 3 Benchmark Constructing

P2P EVAL 收集 121 个 paper-poster pair，构造 1,738 个 paper-specific checklist item，并定义 Fine-Grained 与 Universal 两条评估线。

### 3.2.1 Fine-Grained Poster Evaluation

LLM 只对人工 checklist 的每一项做验证，最终按人工给出的重要性权重确定性求和；它不让 LLM 直接决定整体主观分。

### 3.2.2 Universal Poster Evaluation

LLM 对 U1--U10 逐维打分，XGBoost 学习人类如何把这十个维度合成为整体质量分。

### F.1 Details of the Human Rating Protocol

三名标注者独立整体评分，训练前进行评分培训和区间锚定；大分歧样本排除。论文强调训练/评估分布隔离，以避免 checker-reflection 造成泄漏。

### F.2 Details of Universal Poster Evaluation Criteria

十个输入维度均有明确 0--5 评分定义和扣分规则，覆盖标题、图像质量、留白、上下文、图文比例、尺寸、一致性、内容保真、信息流和自包含性。

### F.3 Other Methods Performance

XGBoost 优于直接 LLM 整体评分、LLM 回归器、微调 LLM 聚合器、OLS 和 Random Forest；但这些结果依赖高一致性的人类标签与固定特征定义，不能单独证明跨任务泛化。

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

- 论文报告 MLLM-featurizer + XGBoost 的 Universal Score 与人类整体评分最接近：R2=0.92，KL=0.11，JS=0.02。
- 关键设计是“LLM 做稳定的局部判断，人类标签监督一个独立聚合器”，而非让 LLM 直接输出最终 holistic score。
- 人类一致性本身很高，且显著分歧样本被排除，因此结果不能直接外推到低一致性、开放式研究判断任务。

## 局限性与可追问点

- 训练样本只有 121 个 poster pair / 1,701 ratings，且来自同一海报任务；R2=0.92 需要确认是严格按 poster/document 分组的 held-out 结果，而不是随机切分造成的近重复泄漏。
- 十个维度是海报视觉/内容维度，不能直接迁移到研究决策质量。
- 论文的主观分是单一整体分，不能说明模型是否准确学习了每个维度的因果重要性。
- “排除大分歧样本”会提高标签一致性，但可能削弱真实人类分歧的代表性。
- XGBoost 只解决聚合问题，不能修复 LLM 特征提取器的系统性偏差或 rubric 漂移。

## 对我当前研究/项目的启发

ForeSci 的 Reviewer Persuasiveness 可以借鉴其两阶段结构：先让 judge 对固定的、任务相关的局部维度打离散分，再用人类标注训练一个小型非线性聚合器；但应把特征换成研究决策维度，并严格按 task/document 分组验证。推荐先收集 raw answer 的人类 rubric/整体分数，再比较 XGBoost、ordinal regression 和线性基线；不能在没有人类标签的情况下直接套用 XGBoost，也不能把 Trace/evidence 特征混入 Pers 聚合器。
