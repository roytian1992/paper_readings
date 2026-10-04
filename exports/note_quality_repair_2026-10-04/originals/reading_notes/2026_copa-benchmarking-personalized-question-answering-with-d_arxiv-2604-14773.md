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
status: read
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

论文把 personalized QA 的目标从“回答中出现了用户历史词汇”改成“回答是否满足该用户稳定的认知与情境偏好”。CIPD 是关键观察：同一问题中，提问者接受的答案可能不是社区最高票答案，说明用户偏好不能由群体共识直接替代。

### 2 Analysis of CIPD Phenomenon

作者从 StackExchange 的问题、候选答案、投票与接受答案中筛选 CIPD 样本，并分析用户历史是否能够解释其选择。分析结果表明，个体偏好具有可重复结构，既涉及可信感和情境匹配，也涉及答案复杂度、学习支架和情绪动机，而不是纯粹的表面风格。

### 3 Factor distillation

作者让多个 LLM 对 CIPD 案例生成选择理由，再通过跨模型归并、频率筛选和专家核验提炼六个因素：Cognitive Trust、Situational Anchoring、Schema Consistency、Cognitive Load Management、Metacognitive Scaffolding、Affective and Motivational Resonance。六因素分别覆盖可信度、情境锚定、与既有知识结构一致性、信息负担、反思支架和情感/动机共鸣。

### 4 The CoPA Benchmark

CoPA 将每个用户表示为六维 factor profile，把个性化评测转成“回答与用户认知因素的对齐程度”问题。数据包含 1,985 个用户画像和真实历史交互，评价不是用单一 overall 分数，而是逐因素判断，以便区分回答为什么个性化或失配。

### 4.1 Benchmark Construction

构建流程先从 CIPD 样本筛选具有足够历史证据的用户，再为用户生成因素解释和画像，最后由 LLM evaluator 对候选回答逐维打 0/1/2 分。接受答案与最高票答案的差异用于检验因素是否能解释个体选择，而不是只复述社区偏好。

### 4.2 Evaluated Approaches

基线包括无用户信息、直接拼接历史、检索相关历史、压缩画像以及显式 factor profile。比较设计的重点是区分“增加上下文长度”与“提供结构化用户模型”的收益，并测试 profile 是否能在生成和检索两类 personalized QA 中稳定工作。

### 5 Experiments

实验围绕五个问题展开：六因素是否真的提升评价区分度，因素能否迁移到其他数据，CoPA 如何排序不同个性化方法，LLM 评分是否与人类判断一致，以及因素之间是否提供重复信息。

### 5.1 Experimental Setup

作者以 factor-level alignment 作为主指标，并报告平均得分及接受答案/最高票答案区分结果；同时使用外部个性化 QA 数据做迁移验证，并抽取部分样本进行人工核验。这样既评估 benchmark 的内部一致性，也检查其是否只适用于 StackExchange。

### 5.2 Effectiveness of Factors

加入用户画像后，模型回答在六因素上的平均对齐和个体偏好区分能力均提升；只使用原始历史的收益较不稳定，说明信息量本身不能替代认知维度。六因素的贡献并不相同，可信、情境和 schema 一致性通常更接近回答内容本身，情绪和元认知因素则更依赖任务情境。

### 5.3 Generalizability of the Factors

跨数据集测试显示，因素作为评价语言具有一定迁移性，但具体 profile 内容和因素权重会随社区、任务和用户目标变化。作者因此把六因素视为可解释的通用坐标系，而不是所有领域固定不变的用户本体。

### 5.4 Factor-level evaluation of personalized QA approaches using CoPA

CoPA 能区分不同个性化方法的优劣：显式使用用户画像的方法通常在多因素上优于无个性化和简单历史拼接；检索方法在事实相关维度有效，但对认知负担、元认知支架和情感共鸣的提升有限。这说明 personalized QA 不能只优化记忆召回率。

### 5.5 Human Validation of CoPA Scoring

人工验证显示，LLM factor scores 与人类判断具有较高相关性，但不是无偏的替代品。作者特别指出，抽象因素的边界和强度仍可能受 evaluator 的语言偏好、提示设计和标注解释影响，因此人类验证应作为持续校准环节。

### 5.6 Factor Correlation Analysis

因素之间存在相关但并非完全冗余。例如 Cognitive Trust 与 Schema Consistency 可能共同反映“这条回答是否可信且符合用户已有知识”，而 Cognitive Load Management 与 Metacognitive Scaffolding 更关注回答呈现方式和学习支持。相关性分析支持保留多维评分，而不是压成单一风格标签。

### 6 Related Work

相关工作包括 personalized recommendation/QA、用户建模、LLM-as-a-Judge 和认知启发式评价。CoPA 的差异在于因素来自真实个体与群体选择分歧，并把评价目标从词面重合和总体偏好扩展到可解释的认知维度。

### 7 Conclusion

论文通过 CIPD 现象说明，个性化 QA 的“正确答案”不能只由社区共识定义；用户在可信度、情境、知识结构、认知负荷、元认知支持和情感动机上的差异，会影响其接受哪一个回答。CoPA 将这些因素转成用户画像和逐维评价协议，实验表明结构化画像比无个性化或简单历史拼接更能反映个体偏好。作者同时承认，六因素仍是数据驱动的可操作近似，未来需要人类参与、跨文化验证和更稳定的自动评估指标。

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

CoPA 的主要证据链是：CIPD 样本存在稳定个体差异；六因素能解释这些差异；factor profile 能区分个性化方法；LLM 评分与人工判断具有可用一致性。结果支持“先建认知维度、再做个性化评价”的路线，但没有证明六因素覆盖所有用户偏好，也没有把 factor score 直接等同于真实学习效果。

## 局限性与可追问点

- 数据来自 StackExchange，用户画像和接受答案未必代表教育、医疗或中文对话场景。
- 画像与评分大量依赖 LLM 归纳，可能把模型偏见包装成心理因素。
- 排除信息不足或难以解释的用户会提高一致性，但可能低估真实用户异质性。
- 需要研究因素随时间变化、用户目标切换以及多因素冲突时的权重学习。

## 对我当前研究/项目的启发

个性化评测可以把“是否符合用户认知需求”拆成少量可解释维度，再分别验证事实、情境、负荷和支架，而不是用一个整体 judge 分数覆盖所有偏好。对长期记忆系统，还应把用户因素作为可更新状态，并记录每次判断的证据和置信度。
