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
status: read
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

### 1 Introduction

论文认为长篇叙事 QA 的难点不只是上下文长度，而是证据在故事中的功能会变化：同一角色有多个状态，同一关系会随情节转折改变，回答还可能依赖跨场景因果和时间顺序。普通 RAG 按相似段落召回，GraphRAG 按实体/关系召回，都难以表示这些动态叙事角色。

### 2 Related Work

相关工作覆盖 narrative understanding、long-context QA、graph RAG 和 agentic retrieval。NKW 借鉴 event/scene/plotline 层级，但把这些结构落到可回溯的 source-grounded assets，并加入 query-time reasoner 和 reading skill，而不是预先生成一个不可审计的全局故事摘要。

### 3 The Narrative Knowledge Weaver Framework

NKW 的构建阶段把源文档转成 canonical entity-relation graph、atomic facts、events/interactions/occasions、entity state profiles、episodes 和 storylines，所有派生对象保留 provenance。查询阶段只给 reasoner 一个 snapshot preview，由它选择证据视图、工具动作和一种 reading skill，再组装有限 source packet。

#### 3.1 Construction-Time Asset Building

##### 3.1.1 Entity–Relation Backbone

系统从文本块抽取实体和二元关系，统一人物、群体、地点、机构、物件和概念的 canonical identity，并把缺失端点保留为带源链接的 proxy。图索引、向量索引和 entity/chunk 反向链接同步维护。

##### 3.1.2 Narrative Unit Extraction

事件描述行动或状态变化，interaction 描述沟通、冲突和影响，occasion 描述稳定的制度/社会/场景条件。每个 unit 记录参与者、目标、时间、设置、视角、功能角色和来源片段；未知字段保持未知，不由模型补全。

##### 3.1.3 Entity Canonicalization

别名与共指解析让同一角色在不同段落共享 referent，并同步更新事件参与者、关系端点和属性所有者。该步骤对长篇故事尤其重要，因为局部段落中的称谓变化会直接影响后续状态和因果检索。

##### 3.1.4 Entity Attribute and State Enrichment

对图中高连接实体回看来源，补充状态、动作、目标、心理状态和持续关系，并保留 before/after 与时间线索。最终 profile 既用于 snapshot card，也用于 query-time 的 state retrieval。

#### 3.2 Global Episode and Storyline Construction

系统按共享参与者/目标、时间与场景连续性、因果依赖、视角兼容性和来源支持，把 narrative units 聚成 episodes；再把 episodes 连接为包含 blocking、resolving、prerequisite、conflict 和 parallel 的 storyline DAG。SABER 清理弱环边并在有向无环骨架上抽取 trunk-branch chains，保留目标、障碍、转折和结果。

#### 3.3 Narrative-Grounded Retrieval and Reasoning

##### 3.3.1 Evidence Views

同一故事暴露 source passages、atomic facts、entity profiles、event/interaction records、episode/storyline links 等视图。视图互补：原文负责精确措辞，事实负责紧凑命题，状态负责时间变化，storyline 负责长程发展；每条证据都能回到来源。

##### 3.3.2 Snapshot-Guided Query Planning

reasoner 先生成轻量 snapshot preview，再输出约束 `Cq`、证据槽位 `Sq`、动作 `Aq` 和 reading skill `Kq`。未选中的图或叙事通道不会默认被查询，减少无关证据和实体主导偏差。

##### 3.3.3 Skill-Based Evidence Assembly

四类 skill 分别服务 literal verification、character state tracking、cause/outcome tracing 和 narrative perspective。首轮检索后，若证据槽位仍未闭合，skill reader 最多请求一轮、最多两个并行的 bounded supplement，并将最终回答绑定到 source-grounded claims。

### 4 Experimental Setup

实验使用 STAGE、FairytaleQA 和 QuALITY，覆盖剧本级、多类型童话和 passage-centered QA；比较 Hybrid RAG、GraphRAG、LightRAG、HippoRAG、A-RAG、DOS RAG。主设置使用 600-token chunks，并在多个 Qwen、Llama 和 GPT-5.5 backbone 上测试。

### 5 Results

STAGE 上 NKW 在多数 backbone 的 Overall 和 Pass@5 均领先，尤其适合角色状态、因果、时间和 narrative progression 问题；FairytaleQA/QuALITY 等短或局部可回答数据上，轻量 baseline 有时仍具竞争力。消融显示 skill-based assembly、snapshot reasoner 和 narrative hierarchy 都有独立贡献；bounded supplement 在 STAGE 上净提升约 3.6 个百分点，但增加延迟。

### 6 Conclusion

NKW 把事实、图、实体状态、事件、episode 和 storyline 组织成可追溯的叙事知识资产，再由 snapshot-guided reasoner 选择证据视图和 reading skill。实验表明，叙事 QA 的收益来自建模“证据在故事中如何发挥作用”，而不只是扩大上下文或检索相似段落；同时，构建和查询成本、上游抽取错误、跨运行路径方差和领域覆盖仍限制了部署。
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

论文的核心图是框架总览：construction-time asset building 与 query-time snapshot planning 分离，reasoner 选择动作，skill reader 负责 source-grounded assembly。当前本地 assets 目录尚未导入对应图片。

### 关键表格

## 实验结论

NKW 在需要跨角色状态、事件链、时间顺序和情节发展的 STAGE 上优势最明显；在短文本和局部证据题上，复杂叙事结构未必划算。组件消融支持“层级资产 + 受控规划 + 技能化阅读”的组合，而不是单一 graph index 的效果。

## 局限性与可追问点

- 上游事件抽取、共指和状态合并错误会传播到所有下游视图。
- 多阶段构建和 query-time supplement 的成本高于平面检索。
- 单次回答的 reasoner 路径可能变化，技能之间的交互效应尚未完全隔离。
- 数据集主要是英文/中文影视和故事 QA，真实非虚构叙事与开放域研究文本仍需验证。

## 对我当前研究/项目的启发

可以把长期 narrative memory 设计成“原子证据—局部事件—episode—storyline”的可展开层级，并让查询先产出 evidence slots，再调用有限的导航动作。所有高层摘要都应保留 provenance，未知的目标、时间和因果不能由摘要阶段擅自补全。
