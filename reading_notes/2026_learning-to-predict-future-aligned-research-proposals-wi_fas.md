---
id: 2026_learning-to-predict-future-aligned-research-proposals-wi_fas
title: "Learning to Predict Future-Aligned Research Proposals with Language Models"
year: 2026
authors: []
venue: ""
field:
  - AI
  - Science of Science
direction:
  - Research Agents
  - Scientific Forecasting
keywords:
  - future-aligned research proposals
  - FAS
  - research ideation
status: read
source_path: ../sources/2026_learning-to-predict-future-aligned-research-proposals-wi_fas.pdf
source_archive_path: ""
assets_path: ../assets/2026_learning-to-predict-future-aligned-research-proposals-wi_fas
paper_type: research
---

# Learning to Predict Future-Aligned Research Proposals with Language Models

## 一句话总结

该工作把科研构思转化为时间切分的预测任务，训练模型从截止时间前的材料生成更接近截止时间后真实研究的结构化 proposal。

## 研究问题

给定研究问题和截止时间前的启发论文，语言模型能否生成在假设、方法、创新点和实验计划上更符合后续真实研究发展的 proposal？

## 核心方法

构造包含 17,771 篇论文的时间切分数据，将 proposal 拆成 Research Question、Hypothesis、Proposed Method、Novelty Claims 和 Experimental Details，并以检索未来论文后的最大语义对齐分数 FAS 进行训练和评价。

## 分章节阅读笔记

### 1 Introduction

论文把研究 proposal 生成重写为时间切分的科学预测问题：给定 cutoff 前可见的问题和 inspiring papers，模型生成结构化 proposal，再检查它是否与 cutoff 后真正出现的研究方向语义对齐。作者认为 novelty/creativity 难以直接规模化监督，而未来文献提供了一个可验证但不完整的质量代理。

### 2 Method

#### 2.1 Future-Aligned Proposal Prediction

每个样本由研究问题 `q`、截止时间前的启发论文集合 `S` 和结构化 proposal `P` 组成。proposal 包含 Research Question、Hypothesis、Proposed Method、Novelty Claims 和 Experimental Details，目标是预测未来方向而不是复述目标论文。

#### 2.2 Verifiable Learning Objective

作者先用 embedding 从 `C_future={p: t_p>t_C}` 中检索 top-k 未来论文，再用 LLM judge 计算 proposal 与候选论文的语义对齐，定义 `FAS(P)=max s_llm(P,p)`。同时计算 hypothesis、method、novelty 和 experiment 各组件的 FAS，用于分析模型究竟改善了哪一部分。

#### 2.3 Time-Consistent Supervision from Historical Papers

为避免直接用未来论文训练，作者从历史 target paper 和其 cutoff 前引用中合成监督：抽取泄漏受控的 research question，选择真正可能提供灵感的 references，再生成与当时知识一致的 structured proposal。这样训练样本模拟“站在发表前做规划”，而不是事后解释。

#### 2.4 Citation-Grounded Reasoning Traces

Stepwise CoT 将 proposal 构建拆成三阶段：gap analysis/inspiration borrowing 生成问题与假设，method reasoning 设计方法，experimental planning 设计验证。与一次性 CoT 或无 reasoning trace 的 Direct SFT 相比，它更直接监督科研规划过程。

### 3 Experiments

实验比较 Research Question Only、Papers Only、Question+Papers 等 prompting baseline，以及 Chain-of-Ideas、AI-Researcher 和多种 future-aligned SFT。数据来自 17,771 篇按时间切分的机器学习论文，并在未见未来文献上计算 FAS。

#### 3.1 Experimental Setup

训练采用 LoRA SFT，测试同时报告整体和组件 FAS，并用 human/LLM judge 评估资源有效性、任务-方法一致性和任务-实验一致性。作者还实现两个生成 proposal，检查是否能在 LLM-assisted coding 环境中转化为可运行研究。

#### 3.2 Main Results

Future-aligned SFT 显著优于 prompting 和既有 research-agent baseline；加入 reasoning traces 进一步提高 FAS，Stepwise CoT 通常最好。收益不仅体现在与未来论文相似，也体现在 proposal 的可行性和方法/实验一致性。

#### 3.3 Ablation Studies

去掉 citation-grounded reasoning 或把 stepwise reasoning 合并成单块 CoT 都会下降。引用敏感性分析显示，移除 background 或 method citations 都会使整体 FAS 下降约 9.6%，而 novelty claims 对 citation removal 最敏感；benchmark citations 的影响相对小，说明概念和技术启发比单纯复用评测基准更关键。

### 4 Analysis

#### 4.1 Citation Sensitivity by Citation Type

结果支持模型确实利用 inspiring papers，而不是只生成通用 proposal。不同 citation type 对组件的影响不同：background 帮助问题框定，method/technical 帮助方案设计，benchmark/experimental 主要影响实验细节。

#### 4.2 Multi-Dimensional LLM-Based Judging

Stepwise-CoT 在 Resource Validity、Task–Method Consistency 和 Task–Experiment Consistency 三项均最高；但 Task–Experiment Consistency 仍是最低维度，说明模型在设计能真正检验其假设的实验上仍较弱。

### 5 Related Work

工作连接了 LLM research ideation、literature synthesis、scientific workflow automation 和 forecasting benchmark。它的差异是把训练和评价都绑定到时间截断与未来论文，而不是只让 judge 评价当下 proposal 的新颖或流畅程度。

### 6 Conclusion

论文提出 future-aligned research proposal prediction，用未来论文中的研究方向作为 proposal 质量的可验证代理，构造无未来泄漏的历史监督，并用 citation-grounded Stepwise CoT 学习分阶段科研规划。实验、人工比较和两个可执行案例共同表明，future-aligned SFT 能提高未来对齐、可行性和方法/实验一致性。但 FAS 仍是“后来被发表”这一结果的代理，不能替代科学正确性、真正的新颖性或未被实现的好想法。

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

主要结果是：时间一致监督有效，结构化 proposal 优于无结构生成，Stepwise CoT 比单块 CoT 和 Direct SFT 更能提升未来对齐。引用类型消融进一步表明，问题框定和技术启发对预测未来研究比单纯 benchmark 引用更关键。

## 局限性与可追问点

- 数据主要来自 NeurIPS、ICML、ICLR 的机器学习论文，跨学科泛化未知。
- FAS 偏向已经发表并可被检索到的方向，可能低估原创但未被实现的 proposal。
- 研究问题抽取、引用选择和 reasoning trace 合成均使用 LLM，存在合成偏差。
- 未来应加入时间严格的外部评测、专家盲评和真实项目结果，而不是只依赖语义相似度。

## 对我当前研究/项目的启发

科研 proposal 生成可采用“历史证据 → 分阶段推理 → 结构化 proposal → 未来/专家双重评估”的管线；同时必须把未来对齐当作一个代理指标，并报告其与可行性、事实支持和真正执行结果的差异。
