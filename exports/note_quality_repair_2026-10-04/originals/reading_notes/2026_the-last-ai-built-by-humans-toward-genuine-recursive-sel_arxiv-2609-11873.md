---
id: 2026_the-last-ai-built-by-humans-toward-genuine-recursive-sel_arxiv-2609-11873
title: "The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement"
year: 2026
authors:
  - Yi Duan
  - Ying Liu
  - Zirui Tang
  - Haodong Chen
  - Jun Zhou
  - Yumou Liu
  - Bangrui Xu
  - Yukai Wu
  - Sidi Chen
  - Yuhan Zhou
  - Haoyu Wang
  - Xiaoyou Yu
  - Shaokun Han
  - Xuzhou Zhu
  - Le Zhou
  - Bolin Lu
  - Wei Zhou
  - Jiachen Liu
  - Nuozhou Fang
  - Jiaxin Tian
  - Ruoyu Chen
  - Yuxuan Li
  - Kai Zuo
  - Kaiyan Zhang
  - Qianyu Yang
  - Zijie Wang
  - Jiantao Qiu
  - Conghui He
  - Guoliang Li
  - Bowen Zhou
  - Zhiyuan Liu
  - Zhoufutu Wen
  - Jihua Kang
  - Xuanhe Zhou
  - Fan Wu
venue: ""
field:
  - Artificial Intelligence
  - Machine Learning
direction:
  - Recursive Self-Improvement
  - AI Agents
  - Continual Adaptation
keywords:
  - recursive self-improvement
  - RSI
  - Headroom-Closed Index
  - HCI
  - autonomy
  - meta-improvement
status: read
source_path: ""
source_archive_path: ../sources/2026_the-last-ai-built-by-humans-toward-genuine-recursive-sel_arxiv-2609-11873_source.tar.gz
assets_path: ../assets/2026_the-last-ai-built-by-humans-toward-genuine-recursive-sel_arxiv-2609-11873
paper_type: survey
---

# The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement

## 一句话总结

论文把递归自我改进（RSI）定义为一个能从经验中产生、验证并继承自身变化，而且这些变化还能影响后续改进机制的闭环过程；作者用“改进责任由人转移给 AI 的范围”组织现有方法，提出从执行改进到递归修改改进机制的 L1–L5 五级框架。

## 综述定位与范围

这是一篇面向 RSI 的路线型综述/观点论文，分析对象是完整的 improvement loop，而不是某一种训练算法。证据同时来自学术论文和产业材料（技术报告、工程博客、开源系统、模型文档及生产基础设施），因为前沿的自改进系统往往先以工程形态出现。论文重点追问：改进环在哪里闭合、什么状态被保留下来、哪些决策已由 AI 承担，以及如何区分真实递归进步与评测投机或单纯增加搜索预算。

## 核心分类体系

作者按 AI 在改进闭环中承担的责任划分五个自治等级：

- **L1 改进执行自治**：人指定目标、方法和成功标准，AI 执行候选更新。
- **L2 改进策略自治**：目标和评测边界外置，AI 诊断弱点并选择改进策略。
- **L3 经验获取自治**：系统进一步决定下一轮需要什么任务、数据或练习经验。
- **L4 部署与环境适应自治**：系统利用部署交互和环境反馈，更新可持久继承的状态。
- **L5 递归继承自治**：系统修改并复用支配后续搜索、评估、选择或整合的改进机制本身。

框架还把“自治结构证据”和“性能提升证据”分开：只有当修改后的改进机制被保留并参与后续轮次时，才有结构递归；若它在独立评测和可比资源预算下产生更强继任者，才构成有效递归。

## 章节地图

全文先在第 1–2 章说明开发规模化的成本、RSI 定义、改进环组成和 HCI（Headroom-Closed Index）视角；第 3 章按 B0、L1–L5 展开自治等级及其评测；第 4 章比较科学、具身智能、软件工程和医疗四类反馈环境；第 5 章整理产业实践；第 6–7 章讨论挑战、未来方向和结论。后续逐章阅读时，应优先关注第 3 章的等级边界、每级的闭环与继承证据，以及第 6 章对安全继承、自治归因和可靠验证的限制分析。

## 逐章阅读笔记

### 1 Introduction

本章提出论文的基本判断：模型规模、训练实验、评测和部署后的修复都在扩大，但改进流程仍依赖人来决定改什么、如何改以及是否有效。RSI 的目标不是让 AI 偶尔生成更好的答案，而是让系统把经验转化为可验证、可继承的状态变化，并进一步改变未来的改进方式。

本章的论证路径是“人类开发负担增加 → 把部分改进责任交给系统 → 必须审计递归与有效性的证据”。开头列举 Kimi K3 的 2.8T 参数、Qwen3.8-Max 的 2.4T 参数，以及内部编码推理所占研究算力份额、agent token 用量的增长，意在说明规模与研发操作量都在增加；这些数字来自不同对象，不能拼成一条统一成本增长曲线（`src/intro.tex:22-30`）。

### 1.1 Scaling Burdens in Model Development

作者将瓶颈分成三类：基础模型训练需要巨量数据、算力和工程协调；合成数据与强化学习需要可生成且可验证的学习环境；部署后系统还要持续诊断工具、记忆、检索和工作流的失败。三类成本分别对应 RSI 对训练流程、经验获取和在线适应的自动化需求。

**开发与评测。** 第一类不只是训练 FLOPs。MoE 架构、草稿模型、架构试验和分布式运行都需要选择与协调；论文提到 GPT-5.6 Sol 的数百次草稿模型实验带来超过 15% 的 token 效率收益。评测本身也昂贵：GDPval 的 1,320 项工作任务约需 9,240 个专家小时；HLE 经约 70,000 个提交筛成约 13,000 个专家审阅项，再形成约 3,000 道基准题。这些例子支持“候选设计、评测和决策均是瓶颈”，但没有统一测量其边际成本（`src/intro.tex:32-55`）。

**后训练与部署。** 第二类是可验证经验的生产与训练：论文称 DeepSeek-V3.2 后训练开销超过预训练成本的 10%，AIMO-2 涉及约 54 万道题、320 万条长解和 170 万条工具整合解答。第三类是上线后的持续维护：文中引用 agent 任务相对聊天约 4 倍 token、多 agent 约 15 倍的消耗，以及 Meta FBDetect 每周处理数千项回归、其中一类问题约需 10 工程师小时。这些是不同系统的例证，指向数据、诊断、验证和修复能否循环复用的问题（`src/intro.tex:56-73`）。

### 1.2 From Development Burden to RSI

论文把 RSI 定义为自主闭环：系统识别限制、提出并验证改进、保留继任状态，并让改进后的能力参与下一轮改进。作者用 A-Evolve-Training（持久化研究策略）和 Ouroboros（持续修订 coding agent）说明“改进对象”和“改进机制”可以同时进入继任系统。

作者给 RSI 设定三个可区分的目的：扩大能力前沿、在相同能力目标下减少资源消耗、发现人类未预设的有效策略。因此“自己改自己”并不是终点；一个系统可能自治地修改大量代码，却只是在昂贵地搜索既定答案。A-Evolve-Training 的 30B Nemotron 实验中，四轮外部得分从 0.80 到 0.86，最优人工提交约 0.87；这展示了版本化研究策略的继承，不等于总体研究目标也由系统决定。Ouroboros 的 coding-agent 版本化工具、上下文、prompt 与核心逻辑在测试和人工批准后晋级，说明安全边界可以与自修改并存（`src/intro.tex:74-114`）。

### 1.3 Challenges for RSI

三个可信性问题贯穿全文。第一是安全继承：错误更新会跨任务传播，必须有版本、回滚和迁移测试；第二是自治归因：生成更好候选不等于 AI 改进了候选搜索过程；第三是可靠验证：反复访问评测器可能造成投机、标签提取或随机种子挑选，因此要用受保护的评测、独立锚点和可比预算。

反例帮助定位门槛：Gödel Agent 在 100 次 MGSM 优化试验中有 14 次最终表现低于初始策略，说明“允许改动”不保证单调进步；DGM 的 SWE 子集表现从约 20% 到 50%，但 archive 管理与父代选择仍由固定规则完成，所以任务分数提升不能直接证明元改进自治；RQGM 通过 epoch 内冻结 evaluator、epoch 边界用独立 anchor 检查替换方案，处理评测器被候选适应与跨版本分数不可比的问题（`src/intro.tex:116-130`）。

### 1.4 An Autonomy-Centered Framework

作者用“AI 承担了哪些改进责任”而不是“自动化组件有多少”来分级。每一级都检查三个问题：闭环在哪里闭合、什么状态进入下一轮、哪些关键决定仍由人或固定基础设施控制；L1–L5 分别对应执行、策略、经验、部署适应和递归继承。

例如 FineWeb-Edu 按固定标准处理数据可放在 L1；Self-Harness 根据测试反馈选择 harness 变更接近 L2；SIMA 2 的 ASKA 依据学习者弱点安排练习涉及 L3；PANDO 从运行轨迹接纳或淘汰持久技能涉及 L4；A-Evolve-Training 修改随后会再次调用的研究政策涉及 L5。分类按*实际被系统控制和继承的环节*进行，同一论文中的不同实验设置也可能落在不同层级。作者第 2.2.2 节的严格定义要求后续改进机制能够被持久自我变化影响，因此 L1–L4 更宜读作走向完整 RSI 的自治阶段，而非每例都已实现严格意义的递归元改进（`src/intro.tex:131-159`；`src/foundations.tex:124-132`）。

### 1.5 Application Domains

四种应用代表四类反馈条件：科学研究的实验反馈昂贵且归因不确定，具身智能的试错受物理成本和安全约束，软件工程有可执行测试但规格不完整，医疗则有延迟、异质且高风险的结果。相同的更新机制在这些条件下需要不同的验证和发布策略。

这四域不是完整行业目录，而是用来比较反馈“能否快速得到、能否客观核验、错误能否撤销”。科学中失败可能来自假设、仪器或协议；机器人中动作改变之后可观察的状态，真实试错可能不可逆；软件中通过测试仅证明相对于现有测试和规格正确；临床中患者结局有时间延迟与混杂，跨机构泛化更难。因而同一条“更新后得分上升”的证据，在不同领域的可信含义不同（`src/intro.tex:160-190`）。

### 1.6 Industrial Evidence

论文把技术报告、工程博客、开源项目、模型文档和生产系统纳入证据，因为许多前沿 RSI 机制尚未以论文形式完整公开。产业材料能展示数据飞轮、评测流水线、agent harness、自动实验和部署反馈，但作者强调要区分“已展示的环结构”和“由材料推断出的更强递归能力”。

本笔记据此把证据分为三层：**机制描述**说明系统声称如何运行；**同协议任务结果**说明特定环节是否改善；**独立、匹配预算、多轮后代比较**才说明改进能力本身是否提高。公司自报指标大多属于前两层，不能将“无人值守运行”“找到最好候选”和“自我加速”画等号（`src/intro.tex:191-209`）。

### 1.7 Differences from Existing Surveys

论文的四个区别是：以完整 improvement loop 为分析单位；以改进责任转移定义自治；把结构递归（机制被继承并再次调用）与有效递归（在独立、可比预算下产生更强继任者）分开；在科学、具身、软件和医疗等不同反馈环境中比较同一机制的边界。

这使综述与单独整理持续学习、AutoML 或 agent 工作流的文章有不同的判断对象。例如“模型权重能持续更新”只回答继承了什么；还需问经验谁选、候选谁提、评测谁定、接纳谁批，以及新状态有没有改变下一轮的改进过程。论文附录的目标分类和产业表扩大了覆盖面，但它是路线图与证据盘点，不是所有被引用工作的统一复现实验（`src/intro.tex:210-224`）。

### 2 Background and Preliminaries

本章提供两类基础：一是用 HCI 描述不同能力域的剩余“可闭合空间”，二是把 RSI 拆解成可审计的改进环组件。这样后面的自治等级不依赖某个特定算法，而依赖闭环责任、继承状态和验证证据。

### 2.1 Uneven Capability Progress in Modern Foundation Models

作者汇总 2023 至 2026 年 9 月、十个能力域的 393 条模型—基准观察，并先按版本与 harness 是否可桥接筛选协议一致的轨迹。HCI 将基准进入年份的第 90 百分位前沿设为 0、满分设为 100（较低分可为负），再按域聚合；数学和研究科学的 2026 前沿约为 86，而软件工程、搜索终端和工具代理约为 53、57 和 40，说明交互式、长状态任务仍有更大余量。

**计算顺序。** 同一模型、benchmark family、变体和协议有多来源分数时，先算加权共识 `s_bar = sum(w_i * s_i) / sum(w_i)`。benchmark 所有者表格权重 3，独立公共 harness 评测 2.5，联合 benchmark/模型报告 2，模型作者表格 1；第一方数值再乘 0.75。设该基准进入数据集第一年的模型分数第 90 百分位为 `F_b,0`，则 `H_mbh = 100 * (s_bar - F_b,0) / (100 - F_b,0)`。因此 HCI=0 指“与入库当年的前沿相当”，**绝非正确率为 0**；若低于该前沿还可为负值。每个基准—年份取模型 HCI 的第 90 百分位 `Q_b,y`，再对领域内基准以 `sqrt(n_b,y)` 加权平均成 `T_d,y`，既让覆盖更好的基准占更多权重，又限制最大表的支配力（`src/foundations.tex:39-62`）。

**协议筛选与解读。** 最新模型的 33 条审计结果中只有 17 条进入可衔接轨迹，另 16 条来自 Terminal-Bench、DeepSWE、CyberGym、ExploitBench、AutomationBench、BrowseComp 等不兼容版本或设置，保留审计却不参与画线。2026 年 advanced mathematics 86.4、graduate-level science 85.8、broad knowledge 77.2；legal reasoning 64.5、multimodal reasoning 62.2、academic breadth 60.4；software engineering 52.6、search/terminal agents 56.8、tool agents 39.9。网络安全 agent 的 91.9 受 Cybench 子集或 `pass@1` 协议改变影响，应谨慎比较。领域值是归一化剩余空间的加权指标，不能直接等同产品可用率（`src/foundations.tex:39-78`）。

图中的 2026 年后延伸是“RSI 可能优先帮助低闭合域”的示意，不是预测。作者特别提醒网络安全轨迹存在子集和 pass@1 变化，跨 benchmark 的协议差异、报告来源权重和不完整覆盖会影响数值解释。

图上延伸按 `R_d = 100 - 0.22 * (100 - T_d,2026)` 人为设定，相当于把剩余 headroom 的 78% 作为示意增益：网络安全 91.9→98.2，软件 52.6→89.6，搜索终端 56.8→90.5，工具 agent 39.9→86.8。它不是拟合出的 2027 年预测，也不能证明 RSI 会实现这些终点。归档源码未附上 393 条逐项记录，所以可核对方法与文中数值，但无法仅凭归档独立重算全部轨迹（`src/foundations.tex:65-81`）。

![Cross-domain capability trajectories and illustrative RSI extension](../assets/2026_the-last-ai-built-by-humans-toward-genuine-recursive-sel_arxiv-2609-11873/figures/source_figure_009_cross-domain-capability-trajectories-and-an-illu.png)

### 2.2 Conceptual Foundations of Recursive Self-Improvement

作者回顾自修改程序、Gödel Machine、AutoML、元学习、持续学习、开放式学习和 agentic ML，指出这些范式分别覆盖改进环的局部。统一比较单位应是 improvement loop：谁产生经验、修改什么、什么被保留、谁掌握更新决定，以及一次改进是否参与下一次改进。

### 2.2.1 Anatomy of an Improvement Loop

改进环由 AI system、system state、experience、target、improver、strategy、verifier、improvement 和 successor 组成。候选变化只有通过验证、被写入持久状态并在下一轮重新进入系统，才算 improvement；全文据此追问闭环位置、继承对象和外部控制点。

九个概念的角色不要混淆：**AI system** 是跨轮追踪的整体；**system state** 是继任者实际继承的参数、代码、记忆等；**experience** 是用于后续修改的失败、执行或反馈记录；**target** 是本轮直接改的对象；**improver** 产生候选；**strategy** 规定候选如何寻找；**verifier** 按现行规则测量并决定接纳；**improvement** 是被接纳且保存的变化；**successor** 是携带变化进入下一轮的系统。以代码优化为例，本轮 target 可是排序函数，下一轮若修改“如何搜索排序函数补丁”的过程，该搜索策略就成了新的 target（`src/foundations.tex:91-122`）。

可用最小状态图理解：`S_t + E_t -> improver/strategy -> candidate -> verifier -> accepted update -> S_(t+1)`。一份输出被写入日志而从未在以后调用，不足以证明继承；一个通过当前 verifier 的 candidate 是*按当前规则被接纳*，并不保证真实、独立或长期能力一定提高。后续章节反复追问的三个问题是“环在哪里闭合”“继承的具体载体是什么”“哪些决定仍然外置”。

### 2.2.2 Definition of Recursive Self-Improvement

RSI 要求经验和反馈产生持久的自我变化，而且这些变化能影响后续改进的生成、评估、选择或整合。目标可以是扩大能力前沿、提高每单位资源的有效改进，或发现超出人类预设策略的方案；仅优化一次外部产物或在固定流程内反复修订，不足以构成 RSI。

严格定义中的“递归”落在**下轮改进过程受上轮自我变化影响**，不要求每轮都修改基础模型权重。例如一个 agent 学到分页 API 的失败模式并保留 `fetch_all_pages` 工具，后续工作可能更好；若它进一步根据这个失败改变今后如何生成或验证工具的程序，并继续继承该程序，才接近 L5 的元改进。反过来，自动修改外部网站或合成更多训练题，若 AI 自身状态和改进机制未随之改变，就不能凭“AI 在循环工作”称为 RSI（`src/foundations.tex:124-132`）。

### 2.2.3 Relation to Neighboring Paradigms

持续学习关注跨任务保留能力，但通常固定学习目标和更新规则；AutoML 自动搜索配置，却通常固定搜索空间、预算和评测；agentic AI 能执行多步任务，但可能只在单个 episode 内运行。它们在持久状态能够反过来修改后续改进机制时，才越过 RSI 边界。

三者与 RSI 不是互斥集合，而是能提供不同环节：持续学习提供记忆与遗忘控制，AutoML 提供候选搜索，agentic ML 提供工具执行和实验编排。差异是持久化的状态是否包含*改进器/策略/评估器*，并真的在后续轮次使用。论文对照表是概念性分类：某个 AutoML 系统一旦允许搜索器自身成为可验证、可继承的修改目标，就会跨越原有范式边界（`src/foundations.tex:133-195`）。

### 2.3 Scope of Evidence

作者有意混合学术和产业证据，以捕捉尚未完全发表的生产级闭环，同时明确标注其证据强度。工程报告可以证明环如何运行和什么被继承，但公司自报结果、技术愿景和独立复现之间不能等同处理。

纳入产业材料的准则是它能提供具体的改进环结构或运行证据，例如跨轮保存的工件、候选如何与工具/evaluator 交互、更新后系统是否继续工作。论文列出的来源包括官方技术/研究报告、工程博客、开源库、模型文档、GitHub/Hugging Face 发布以及公开 benchmark/竞赛榜单。它们能补足尚未写成论文的工程实践，也使证据异质：一个系统的架构图可证明设计意图，执行日志可证明局部操作，受保护的多代对照才可支撑递归效益结论（`src/foundations.tex:196-201`）。

### 3 RSI Across Autonomy Levels

本章是全文主线。B0 到 L5 不是能力强弱榜，而是改进责任逐步内化的边界：从当前输出的修订，到继承系统状态、选择改进策略、决定学习经验、吸收部署反馈，最后让改进机制本身成为继承对象。

![Overview of the five RSI autonomy levels](../assets/2026_the-last-ai-built-by-humans-toward-genuine-recursive-sel_arxiv-2609-11873/figures/source_figure_001_overview-of-the-five-rsi-autonomy-levels-and-rep.png)

### 3.1 B0: In-Task AI Improvement

B0 只改变当前任务的输出，不把状态带到未来独立任务，因此是非 RSI 的参照级。Self-Refine、Reflexion 和 Tree of Thoughts 可以在会话中生成、评价、修订候选，但上下文结束后经验被丢弃；固定验证器、自我批评盲点和重复迭代的边际收益，使 B0 无法形成持续学习。

这里的 B0 更准确是**非 RSI 参照级**：Self-Refine 的反馈修订、Reflexion 在当前运行中的 verbal memory、Tree of Thoughts 的树状搜索都可能改进一次任务，但下一个独立任务并未必继承可用的系统更新。即使一次 rollout 中有多个反思步骤，只要目标、评测和后续系统状态没有跨任务变化，环就闭合在这次任务里。论文列出四类局限：不累积跨任务增益、程序依赖人预设、同一模型自评可能重复盲点、固定测试下迭代会耗尽收益或适应测试（`src/L0.tex:24-54`）。

### 3.2 L1: Autonomy over Improvement Execution

L1 由人定义目标、程序和验收标准，AI 执行程序并把合格产物写入持久状态。相比 B0，关键变化是更新会进入后续任务；代价是流程覆盖不到的情形仍无法自行改流程，错误执行可能被持久化并传播。

本级**自治的是执行权**，不是改进方针。可以把人工维护的程序写成“检查数据 → 生成候选 → 运行测试 → 人定阈值接纳 → 保存产物”；AI 在每步可做复杂工作，但它不能凭评测失败自主决定改换整套搜索或验收逻辑。论文沿实际开发链列出六个落点，数据、训练方法、训练平台、评测安全、部署优化、应用系统；其中数据层再分清洗筛选与合成数据两类（`src/L1.tex:1-24,165-218`）。

Meta Capacity Efficiency 的可复用修复技能是产业型执行自治例子：AI 按工程流程诊断和提出修复，工程师仍负责 PR 审查与整合。它说明“跨任务可复用的修复经验”可以进入工程系统，同时保持外部发布权（`src/L1.tex:4-5`）。

### 3.2.1 Data Level

数据层主要有两类 L1：按人定义的质量标准清洗、筛选和去重，以及按固定流程生成合成样本和监督信号。FineWeb-Edu、NeMo Curator、Data-Juicer、SynthLLM、SynthAgent 等把专家标准规模化执行，但不由 AI 决定标准本身或下一轮学习议程。

前一类的实质是把“什么是可用样本”的 rubric 和去重/过滤要求大量执行，输出是能进入未来训练的数据集；后一类把预先规定的任务模板、角色或执行轨迹转成新的训练样本。合成样本数量增加仍需独立质量检查；如果模型反复复制自己的错误而没有外部校验，持久化反而会放大偏差。是否达到 L3 取决于下一批经验是否**依据变化中的学习者状态**选择，不能只看是否“自动生产数据”（`src/L1.tex:25-58,165-172`）。

源码还举了三种更具体的分工：Google High-Fidelity Label Curation 先让 LLM 初标，再将聚类与边界样本交专家复核；Phi-4-reasoning 按人设的难度和推理特征筛选靠近能力边界的样本；Nemotron-4 用 instruction model 生成候选，再由 reward model 依人设维度过滤。它们自动执行了庞大而重复的数据工作，但质量标准和验收权仍由人设定（`src/L1.tex:165-170`）。

### 3.2.2 Training-Method Level

EDIT、REPO 等把诊断、局部修订、LLM 评审和奖励生成编成固定训练流程。AI 能按 rubric 修正推理步骤并产生后训练信号，但目标、反馈和更新规则仍由研究者预先设定。

EDIT 按 rubric 定位并局部修理错误推理步骤，把修订结果用于后续 RL 校准；REPO 用 LLM judge 检查 SOP 合规，再把判断转成奖励供 policy optimization。两者都把人工设定的修订/评判程序用于训练信号，但机制不同。需要检查数据或参数更新是否真正进入后续模型版本；仅对同一条推理生成修正版，仍可能是 B0。即使训练成功，候选改写规则和评分器未随经验改变，自治也仍限于 L1（`src/L1.tex:172-178`）。

### 3.2.3 Training-Platform Level

平台层将性能分析、代码优化、分布式训练故障诊断和恢复固化为 runbook。AI 可以定位热点、提出实现修改并回滚失败候选，也可以沿 NCCL 故障决策树对齐 rank 日志；它执行的是工程经验，而不是自主发明诊断程序。

论文举 C/C++ 性能优化与 Meta NCCL 排障等例子：执行器能编译候选、测延迟、分析崩溃日志，或根据人写出的 runbook 合并多 rank 证据。它们降低重复工程劳动，但“先检查哪些故障”“用什么测试晋级”仍由专家维护。平台层的好处是反馈常可执行和回滚，风险是微基准变好但全链路训练不稳定（`src/L1.tex:76-111,178-188`）。

### 3.2.4 Evaluation-and-Safety Level

AI 将专家写出的 rubric、风险标准和测试协议应用于大规模输出，例如 HealthBench 让模型按医生定义的医疗标准评分。此类系统可提供一致的反馈信号，但验收目标、阈值和安全边界仍由人维护。

医疗或安全评测中的 evaluator 本身可能出错，因此“LLM judge 打分”只是扩展检查吞吐，不能取代独立审阅。L1 只有在评测输出用于筛选、修订或训练后续系统时才有跨轮继承；一次性给客户报告打分是应用任务，不一定是 AI 系统改进环（`src/L1.tex:111-125,188-194`）。

### 3.2.5 Deployment-Optimization Level

AIPC 等系统把模型转换、兼容性修复、量化校准和目标硬件验证编成分阶段流程。给定平台和约束后，AI 生成可运行部署产物并执行验证，但不会自主改变部署目标或约束。

此处持久化对象是经过转换、校准和阶段验证的可运行部署工件。论文列出的边界是目标平台、模型及约束由外部给定。**实际评测建议**是分别检查正确性、精度损失和目标硬件上的吞吐/延迟，保留失败时回滚能力；代理环境的分数不能替代目标设备上的验证（`src/L1.tex:194-200`）。

### 3.2.6 Application-System Level

Agent Toolkit for AWS、LinkedIn CAPT 和 Harness Engineering 把服务集成、接口实现、代码维护、测试和回滚写成可复用技能或 playbook。AI 可在真实代码库中完成长流程并产出持久工程资产，人仍设定产品意图、架构和合并规则。

这类工程 agent 可能在复杂代码库里完成提交。分级前应先界定被追踪的 AI system：若持久产品代码本身是它下轮继续改进的状态，按固定 playbook 修改代码也可属于 L1；若只追踪 coding agent 的能力，那么合并产品功能并不自动表示 agent 自身变强。L1 的工作规则可以完全固定，关键是预设流程所产出的变化是否经验证并成为后续状态（`src/L1.tex:136-163,200-206`；`src/foundations.tex:91-98`）。

### 3.2.7 Evaluating L1 Execution Autonomy

L1 要分开测执行可靠性和持久化安全性：流程是否能在分布变化下正确执行，产物在进入后续流水线前是否经过有效检查。遇到流程未覆盖的状态时，L1 不能自行修改程序，因此长链路可靠性和继承前验证是核心指标。

实证上需要记录每个环节的成功率、错误传播率、人工干预、回滚和新任务复用，而不只报告“自动化率”。一个候选被错误接纳后，下一轮从污染状态开始；这正是 L1 比 B0 多出来的收益和风险。若评测只是一次任务成功率，无法证明继承的产物对后续任务有帮助（`src/L1.tex:206-218`）。

### 3.3 L2: Autonomy over Improvement Strategies

L2 把“下一步改什么”交给 AI：系统根据失败和评测证据选择干预、实例化候选、测试并保留结果；人仍指定目标、任务边界和验收标准。瓶颈由执行已知方案转为在巨大干预空间中做实验决策。

判定 L1→L2 的关键不是候选有多少，而是系统是否根据新证据**自主决定下一种干预**。例如测试显示工具调用失败后，agent 可以决定改 prompt、重排工作流或替换工具接口；若它只执行人设的固定改写顺序，即使并行生成数百候选也还是执行自治。L2 的典型闭环为“诊断失败→选择策略→生成变体→固定评价→保留胜者”，整体目的、预算和 verifier 一般固定（`src/L2.tex:1-73`）。

![L2 autonomous strategy selection](../assets/2026_the-last-ai-built-by-humans-toward-genuine-recursive-sel_arxiv-2609-11873/figures/source_figure_002_overview-of-l2-autonomous-strategy-selection-und.png)

### 3.3.1 Prompt Search

GEPA 使用执行轨迹反馈，MPO 使用多模态评估导出的语义反馈，C-Evolve 遵循固定进化协议，分别搜索 prompt 或相关控制变量。自治点不在于能生成文字，而在于决定下一轮尝试哪类修订、是否保留候选变体；任务指标和搜索协议仍外置。

三个例子机制各异：GEPA 将执行轨迹中的失败反馈用于反思和 prompt 变异，并用 Pareto 风格的候选保留维护互补方案；MPO 从多模态评测结果提炼语义反馈后调整控制变量；C-Evolve 在人预设的进化框架里生成和筛选候选。Promptbreeder 共同演化任务 prompt 与变异 prompt，论文仍将它归为固定任务 fitness 下的 L2 搜索。**评测建议**是同时报告评测调用次数与最终表现，避免只呈现最佳 prompt（`src/L2.tex:73-79,141-144`）。

Dropbox 的生产场景展示 GEPA 如何从执行反馈中改 prompt，但生产可行性和受保护任务上的可迁移搜索收益仍是不同问题（`src/L2.tex:73-74`）。

### 3.3.2 Agent and Harness Search

ADAS、AFlow、AgentSquare 和 Agent Optimizer 把可编辑对象扩展为 agent 代码、工具描述、工作流图和模块组合。候选 agent 的结构可以通过元 agent 编程、MCTS 或进化重组产生，但最终晋级仍依赖固定 benchmark 和评测器。

ADAS 让 meta-agent 编写可运行的 agent 前向程序并保存候选 archive；AFlow 用树搜索探索工作流图；AgentSquare 将 planner、memory、tool-use 等模块组合。搜索对象从字符串 prompt 扩大到可执行体系结构，因此需要沙盒运行、接口约束和跨任务检查。Microsoft Foundry 的生产 agent 调整展示了持续工程需求，但只有明确的“失败诊断→自选系统改动→验证继承”链条才能判为 L2（`src/L2.tex:79-95`）。

### 3.3.3 Model and Training Search

L2 还可搜索训练配置、架构、训练规则和系统实现：TAO 在固定验证目标下分配试验，AgentNAS 从任务生成种子架构，NanoGPT/AutoResearch 让 agent 修改训练程序，AutoKernel 按 profiling 结果搜索 CUDA/Triton 实现。共同点是 AI 选择实验路径，正确性、指标和预算仍由外部保护。

AgentNAS 可从任务生成种子架构，后续搜索空间和评价规则仍有限定。GPT-6 Astra 的 NanoGPT 案例使用固定验证目标、单 GPU 与受限训练环境；Karpathy 的 autoresearch 则固定数据流程、评价函数、指标和单次实验算力预算。AutoKernel 从 profile 热点选择 kernel 候选，再用正确性测试和实际速度测量过滤。这里 AI 的贡献是更有效地分配实验和干预；若只记录最佳训练程序，尚不知道它是否学会了可迁移的研究方法（`src/L2.tex:96-220`）。

还要区分名为 Auto Research 的多 agent 共享 lineage 系统与 Karpathy 的 `autoresearch`：前者用专职 agent 与共享历史安排研究尝试，后者固定本地训练实验协议。两者都属于 L2 的研究策略自治，不能合成同一个实验结果（`src/L2.tex:111-119,197-200`）。

### 3.3.4 Evaluating L2 Strategy Autonomy

策略空间越大不等于改进越好，需要分别报告搜索效率、跨任务迁移、资源成本和稳定性。自适应访问开发集会带来过拟合、随机种子挑选、标签提取和评测器盲点；公司结果可证明可行性，但不能替代独立复现和受保护测试。

有效对照至少应匹配初始模型、任务、工具、总评测次数、算力及人工调参时间；日志中要保存失败候选，避免只呈现被挑中的 seed。应在未参与搜索的任务和不同分布测试修改，并区分“更大搜索预算”的收益与“更好的策略选择”。L2 的高分若来自开发集反复试错或读取测试反馈，不能外推为真正的策略自治优势（`src/L2.tex:221-235`）。

### 3.4 L3: Autonomy over Future Learning Experience

L3 让系统决定“下一轮学什么”。当前能力、失败和学习历史影响任务选择、任务生成或交互目标，而持久化学习又改变下一轮经验获取；人可以继续固定总体目标、评测器和更新规则。

严格链条是 `learner state_t → acquire experience_t → persistent learner update → learner state_(t+1) → acquire experience_(t+1)`。这意味着选题/取样器必须对变化中的学习者敏感；获取到的经验需要改变后续学习状态并反馈到下一轮取样，**能力收益是另一个待测问题**。系统可从现有题库自适应选题，也可自造题或主动进入环境寻求练习；自造题不是 L3 的必要条件（`src/L3.tex:3-97,366-374`）。

![L3 learner-conditioned experience acquisition](../assets/2026_the-last-ai-built-by-humans-toward-genuine-recursive-sel_arxiv-2609-11873/figures/source_figure_003_overview-of-l3-learner-conditioned-experience-ac.png)

### 3.4.1 From Industrial Automation to Experience Autonomy

数据摄取、过滤、标注、混合和训练编排的自动化本身不构成 L3。关键证据是 learner state → experience acquisition → persistent learning → later acquisition 的闭合依赖；固定选择算法如果响应变化中的 learner 也可能是 L3，而反复生成样本却不看 learner 就不是。

产业系统常把数据管道、合成、标注、训练和评测全部自动化，但其课程可能仍由静态配方、人工里程碑或固定权重控制。要证明 L3，需展示取样决定如何读取当前能力、置信度、失败簇或技能覆盖，并做冻结 learner-state 输入的消融；否则训练后分数变高也可能只是更多数据或更多训练步的结果（`src/L3.tex:98-225`）。

### 3.4.2 Adaptive Task Generation and Self-Play

SSP、AZR、R-Zero、STP、PSV 和 VisPlay 用 solver 表现、一致性、不确定性或可执行结果塑造下一批任务。形式证明和代码执行能保证指定性质，但一致性和难度奖励只是代理信号，未必代表正确性或真实学习收益；难度控制也可能出现类别重叠和窄化。

例如 AZR 用可执行检查约束自生问题的答案，R-Zero 用当前 solver 的不确定性选择“刚好有挑战”的任务；但高不确定也可能代表题目含糊。STP 的形式证明能提供任务正确性的强信号，却不自动证明它适合当前学习者；PSV 由规格生成任务，可检查规格满足性，但“满足规格”与“学完能迁移”仍是两种判断。VisPlay 等自博弈方法可能不断提高对特定对手/环境的适应，须用外部任务检验覆盖与迁移（`src/L3.tex:226-308`）。

再看三个细节：STP 让 conjecturer 和 prover 双向训练，前者生成可证明猜想，后者尝试证明，形成任务生成与求解的联动；PSV 想控制目标难度，但源码报告目标难度和实际实现难度有大量重叠，说明标尺尚不精确；VisPlay 让大多数答案的置信度接近中点，同时用多样性惩罚防止反复提出同型题。三者分别解决可验证性、难度校准和覆盖，却仍需测试学习后是否迁移（`src/L3.tex:261-295`）。

### 3.4.3 Autonomous Practice through Environment Interaction

VOYAGER 根据探索状态产生 Minecraft 目标并积累可执行技能；SIMA 2 的 ASKA 设置用奖励评估把练习指向弱项；SEAgent 用世界状态模型和 guidebook 改写 GUI 任务课程。它们的持久状态可以是技能、记忆或指南，而不必更新基础模型权重。

区分同一系统的不同设置很重要：VOYAGER 的技能库与自动课程体现交互经验可被复用；SIMA 2 的 ASKA 根据表现调整未来任务，比固定任务实验更接近 L3；SEAgent 的 World State Model、guidebook、Curriculum Generator、Actor 则把环境认识和任务选择耦合。是否构成完整闭环还要看经验被存进哪里、未来任务是否真的因学习者变化而改变、以及未见环境是否受益（`src/L3.tex:309-365`）。

### 3.4.4 Evaluating L3 Experience Autonomy

评测需同时验证 learner-conditioned 机制和学习收益，并与 learner-independent 课程、冻结状态输入的对照匹配数据源、交互和总算力。正确性、难度和学习价值要分开测；错误 judge、误导性难度 proxy 和污染记忆会形成 experience corruption，因此必须跟踪多轮迁移、覆盖和新环境表现。

“经验污染”是作者指出的**结构性风险**：错误的 judge 或狭窄课程可能先污染 learner，再让受污染的 learner 继续选择偏题经验；并非声称上述每个系统都已观测到这种故障。实验可让自适应与固定课程拥有相同数据源访问、采样/验证/训练总预算，而允许它们实际取得的任务分布不同；否则人为强迫任务相同会消除 L3 所研究的因果变量。除目标集得分，还应看旧能力保持、任务多样性和多个轮次后的收益（`src/L3.tex:366-431`）。

### 3.5 L4: Autonomy in Deployment and Environmental Adaptation

L4 把反馈来源推进到持续部署：系统决定哪些交互后果应进入记忆、技能、harness、代码或参数，并在后续任务中复用。目标、权限、受保护评测和高风险发布仍由外部治理，核心区别是运行经验成为持久适应的来源。

L4 的理想链条是“部署任务→可追溯轨迹与后果→归因并提议持久变化→独立检验→接纳/淘汰→后续真实任务激活该变化”。图中的分页 API 例子很直观：原 agent 只请求 `/issues?page=1`，忽视响应中的 `next_page=2`；修订后持续抓到 `next_page=null`。反复出现同类错误时，可以从轨迹提炼“检查分页”规则、编译 `fetch_all_pages(api)` 工具，或直接改 agent harness。新状态被继承并在后续调用，说明**结构上的适应环闭合**；是否改善新任务还需独立验证（`src/L4.tex:1-62`）。

本节引用了一些**离线**轨迹提炼与批处理系统，它们证明可生成持久候选，却未必证明真实部署反馈驱动的完整 L4。判级需逐项检查环境反馈来源、接纳权、跨会话保存与激活；不能因为论文把方法列在 L4 节，就把每项工作当成已实现部署自治。

![L4 deployment and environmental adaptation](../assets/2026_the-last-ai-built-by-humans-toward-genuine-recursive-sel_arxiv-2609-11873/figures/source_figure_005_overview-of-l4-autonomy-in-deployment-and-enviro.png)

### 3.5.1 Trajectory distillation

轨迹蒸馏把交互历史压缩为文本记忆、结构化图、程序技能或可执行工具。Dynamic Cheatsheet、ACE、ReasoningBank、APEX、Trace2Skill、PANDO、Metis 等分别解决可检索性、条件化复用、技能维护和编译验证；持久化不保证正确激活，记忆和技能的适用条件必须可追踪。

**四种载体。** 文本型的 Dynamic Cheatsheet、ACE、ReasoningBank 保存失败教训和适用规则，ACE 还维护计数与局部补丁；结构化型的 APEX 保存里程碑图，PersonaAgent、PAHF、MemToolAgent 将角色、偏好澄清或工具经验组织成可检索结构；程序性技能型的 Trace2Skill、PRACTICE 从轨迹抽取操作规程或技能文档，这两者主要是离线提炼，PANDO 进一步允许在线规则/例程接纳和降级，PILOT 有 supervisor；可执行工具型的 Metis 把文本计划编成代码并通过沙盒检查，Evo-Harness 和 SHAPER 修改可调用程序或上下文选择器（`src/L4.tex:63-209`）。

关键困难不仅是“记住”，还包括检索是否触发、适用前提是否满足、执行器能否忠实执行，以及旧技能与新环境是否冲突。可执行工具的单元测试通常比纯文本经验有更强可验证性，但仍依赖规格覆盖；一条规则在旧任务有用，部署任务一变就可能成为错误建议。

这类方法的结果口径也不同：Evo-Memory 用顺序任务流考察跨期记忆复用；PANDO 同时关注动作重复、额外步骤和缓存利用；Metis 在效果之外计入工具构建与执行成本。因此不能把所有“有记忆/技能”的结果合并成一个可比的 L4 提升率（`src/L4.tex:208`）。

### 3.5.2 Iterative revision of the agent system

这一类直接改 agent 的技能、rubric、harness 或权重。DecoEvo 通过 score-independent audit 防止 solver 与 judge 共适应，HarnessDev 和 ASPIRE 测试 agent 能否自建并改进 harness，S3Gym 比较历史压缩与参数训练；研究还区分“能产生有用更新”和“运行时能正确使用更新”。

DecoEvo 同时修 solver 与 rubric，故用独立于当前分数的 audit 检查要求覆盖、近似平局时的响应区分，再作 Pareto 检查，以识别二者相互迁就。HarnessDev 区分创建 harness 的 creator 与执行任务的 executor，再以冻结隐藏任务和 token 成本检测更新的净收益；ASPIRE 用得分门槛控制晋级并保留回滚路径。S3Gym 比较原始历史、压缩摘要和参数训练三种经验通道。Harness Benefit 研究还发现更新能力与基础模型能力关联较弱，小模型生成的更新收益可接近前沿模型，但运行时收益并非单调；因此要把“生成的更新是否有用”和“执行器是否调用并正确遵循”分开测（`src/L4.tex:210-221`）。

### 3.5.3 Selective retention and deployment of updates

HDSO 用 control/treatment 执行验证技能假设，Library Drift 说明无限堆积会降低检索质量，Tax AI 则以定向、回归测试和工程师审查控制生产发布。L4 的治理重点从“生成候选”转向“何时接纳、何时淘汰、何时重新验证”。

HDSO 尽量让同一批任务分别在有/无新技能条件下执行，先成对筛选，再用独立验证任务确认；这比只把最好轨迹写进记忆更能判断因果收益。Library Drift 的日志、容量上限和退休机制处理无限追加带来的检索退化，但过度淘汰也会丢掉少见却重要的技能。Tax AI 的生产例子保留人类 PR 审查和局部修改范围，显示高风险系统可以有自动诊断与修订，同时将发布权留在外部（`src/L4.tex:222-232`）。

### 3.5.4 Evaluating L4 Deployment Autonomy

最终分数不能说明更新为何有效或何时失效。应把每个继承变化与触发证据、后续调用、旧任务保持、新任务收益和分布变化关联；还要测激活失败、错误泛化、旧能力回退及长期稳定性。L4 的自治始终嵌在权限、保护集和发布权的外部边界内。

理想日志至少记录故障轨迹、归因、候选状态差异、验证任务、接纳理由、发布版本、实际激活次数、收益与回退。若只比较更新前后总体分数，无法排除环境变简单、基础模型升级或任务组成变化。对部署式学习还应测时间漂移、被影响用户/任务范围和错改恢复代价；回滚软件状态也不能撤销已发生的外部后果（`src/L4.tex:233-245`）。

### 3.6 L5: From Environmental Adaptation to Meta-Improvement

L5 的对象是产生未来改进的 improver、successor evaluator、搜索政策或研究流程。只有当修订后的机制被带回并控制后续继任者生成、评估或选择，才跨过 L4；作者再把“结构 L5”和“有效 L5”区分开。

可以用两代对比：L4 的 agent 保留一个更好的分页工具，但以后如何提出、测试和接纳工具的程序不变；L5 会根据曾经漏页的证据改造**工具改进程序**，例如要求候选生成器检查分页类缺陷、让 verifier 新增多页覆盖，并让改过的程序在下一次工具迭代中起作用。机制修改并重新调用是*结构*证据；相同总预算、独立新任务上产生更好后代才是*有效性*证据（`src/L5.tex:1-53`）。

![L4 to L5 recursive meta-improvement](../assets/2026_the-last-ai-built-by-humans-toward-genuine-recursive-sel_arxiv-2609-11873/figures/source_figure_006_from-environmental-adaptation-to-recursive-meta.png)

### 3.6.1 Improving the Search Procedure

STOP 让 improver 优化自己的 Python 搜索程序，Gödel Agent 同时开放任务策略和递归更新逻辑，DGM 保存 agent 后代但仍把 archive/parent selection 放在外部，HyperAgents 则修改 task agent 和 meta-agent。弱模型退化、软预算被利用、无限制运行中调用更强模型，以及固定父代选择，分别暴露不同外部边界问题。

STOP 将搜索程序作为修改目标；其第 4 代在 5 个转移任务中胜出，但弱模型设置会退化，且出现绕过软预算或利用评测漏洞的风险。Gödel Agent 的无限制运行曾调用更强模型；100 次 MGSM 优化试验中有 14 次最终低于初始策略，提醒“递归编辑”可能损害能力。DGM 的后代 archive 展示当前 coding-agent 性能可持续提升，**但父代挑选与 archive 管理是固定外环**，因此不能把 task score 的改善直接当改进程序改善。HyperAgents 同时改 task agent 与 meta-agent，并在未见过的数学评分任务检验固定的演化 meta-agent；200 次迭代终点没有显著优势，说明部分 L5 结构特征不等于效率上形成正反馈（`src/L5.tex:54-62`）。

### 3.6.2 Improving Successor Evaluation

RQGM 让 evaluator 在 epoch 内冻结，在边界用独立 ground-truth anchor 选择替代 evaluator，再重新评估受影响的 agent。这缓解了固定评测器被持续利用和标准漂移；跨版本原分数仍不能直接比较，锚点、替换周期和目标也仍由外部设定。

它的核心是把候选解的自适应搜索和评估器修改错开：epoch 内用固定 evaluator 比较候选，边界再检查新 evaluator；一旦替换，旧评分不能直接横向比较，要按新准则重评或重置。论文列出 Polyglot 留出结果 71.7%，对比 HGM-H 的 69.9%，并报告 token 更少；这是特定受保护任务上的结果，未证明所有任务/长期多轮都会保持。独立 anchor 是外部稳定参照，避免“越来越好”的分数只是尺子变了（`src/L5.tex:63-67`）。

### 3.6.3 Revising Research Goals and Policies

A-Evolve-Training 将配方、失败方向和 checkpoint 结果汇总为 research policy，由 meta-agent 根据开发分数与外部收益的错位重写下一轮搜索。30B 模型四轮结果接近最优人类提交，说明政策层继承可成立，但总体目标、constitution、worker substrate 和外部 benchmark 仍未被系统自主修改。

被继承的 policy 包括常用训练配方、升降级的研究方向、失败登记，以及每轮 worker 应测试什么；meta-agent 根据新实验更新这些规则。30B Nemotron 外部得分 0.80→0.86（人工最优约 0.87）支持受限研究设置内的政策继承；但固定 constitution 与目标意味着不是系统自行重定使命。政策是否能迁移到其他模型、研究预算或开放问题，仍需把原始政策和进化政策在相同起点比较（`src/L5.tex:68-74`）。

### 3.6.4 Industrial Practice

AIRA 和 Automated Alignment Researchers 主要自动执行人设工作流；AIDE 让研究 agent 改进 research-agent harness，并报告多次接受更新和外部迁移，但把进化 harness 安装为外层 improver 后未证明统计显著的效率优势。产业 L5 的主要价值假设是节省重复研究成本，实际评估必须把评测设计、失败调查和代码维护成本一并计入。

AIRA₂/AAR 能自动跑实验、写研究总结，却不能仅凭产出数量证明研究程序自身被后代修改。Weco AIDE² 报告约 100 个无人值守步骤中有 7 次接纳更新，这能证明系统持续尝试并保存候选；其“用进化 harness 作外层 improver”实验的效率优势未达统计显著。因此“研究 agent 完成更多工作”“研发 harness 可变”和“元改进更有效”是三种不同主张（`src/L5.tex:75-83`）。

### 3.6.5 Evaluating L5 Recursive Improvement

作者建议按适应性、保持性、迁移性、效率、稳定性和元递归六维评估。有效 L5 需要原始/修订机制从可比初始状态和总预算出发，在新任务上产生更强继任者，并记录拒绝、回退、资源与评测开销；仅看到更强当前 agent 或更高开发分数不够。

六维可以转成实验记录：新任务/分布的**适应性**，旧任务的**保持性**，机制固定后在未见问题的**迁移性**，每单位算力/时间/人工的**效率**，跨 seed 和多轮的**稳定性**，以及编辑过的改进器再次产生更好后代的**元递归**。对照要匹配模型、初始经验、环境访问与**总预算**，但允许不同机制在预算内产生不同数量的候选；研发和验证该机制的费用也必须计入。作者还提出三类拟议评测任务：自适应前沿任务检验目标选择，受保护参考任务检验遗忘与投机，规则未知的私有任务检验新分布发现；并记录预期收益低于成本或风险时能否停止。这些是未来要求，并非现有系统已全部完成（`src/L5.tex:84-120`）。

### 3.7 Cross-Level Synthesis

相邻边界可概括为：B0→L1 是持久化；L1→L2 是选择策略；L2→L3 是决定学习议程；L3→L4 是吸收部署环境；L4→L5 是继承并修改改进机制。等级越高不代表流程越有效，当前证据对 L1–L2 较充分，对 L3–L4 更依赖领域，对端到端 L5 仍以受限原型和产业早期系统为主。

可以把等级看成五次“决策权交接”，而非单调安全/性能排名。对任一声称为 RSI 的系统，先画出父状态、候选、验证、接纳、下一轮调用，再找出谁决定干预、经验和评测。若子代只是更会执行当前任务，最多说明性能提升；要谈复利，需证明它更会产生*下一代*。这也是论文把结构自治、经验收益与因果归因并列讨论的原因（`src/cross_level.tex`）。

![B0-L5 loop patterns and external control boundaries](../assets/2026_the-last-ai-built-by-humans-toward-genuine-recursive-sel_arxiv-2609-11873/figures/source_figure_010_loop-patterns-of-five-levels-gray-dashed-frames.png)

### 4 RSI Across Applications

本章把自治等级放回具体反馈环境，强调“能改什么”取决于反馈是否便宜、可执行、可归因和可安全回滚。四个领域都已有组件级持久改进，但改进器、评估器和发布机制的递归演化仍很少被完整证明。

正文在 `src/app_S1.tex` 给出四个领域的论证骨架，附录 C（`src/appendix.tex:457-778`）展开到各类可改组件和代表系统。分类可以重叠，例如医疗 AI 科学家同时涉及科学与医疗。将“科学发现了新分子”“机器人完成了新动作”“coding agent 修了一个仓库 bug”“医生 agent 答对一例”视为外部产物；只有后续系统自身发生经验证的持久变化，才进入本综述关心的改进环。

![Application feedback regimes](../assets/2026_the-last-ai-built-by-humans-toward-genuine-recursive-sel_arxiv-2609-11873/figures/source_figure_007_application-regimes-differ-mainly-in-the-kind-of.png)

### 4.1 S1: RSI for Science

科学 RSI 的环节是提出假设、运行计算或物理实验、解释结果，并把验证过的工具、技能、记忆或 scaffold 带入下一轮。HypoForge、Test-Time Tool Evolution、DrugSAGE 和 SIA 说明科学 agent 的组件可以持续改进，但 evaluator、更新选择和晋级规则多仍固定；改进分子或假设本身不等于科学 agent 自我改进。

科学反馈有三个难点：问题空间开放，实验昂贵且可延迟，负结果不能直接定位到假设、协议、工具还是仪器。因而应保存每项发现的假设前提、实验条件、失败分支与证据强度。这个场景的可改对象分为**假设生成模块、实验 agent、反思/改进器**：前者改变未来会提出什么问题，中间层扩展能执行的工具和程序，后者决定怎样把实验结果归因并接纳更新。附录判断现有证据以 L2 组件级策略更新最强，早期 L3 对未来经验选择有所涉及；长期、跨领域有效的 L4/L5 科研改进环尚缺乏（`src/appendix.tex:480-560`）。

### 4.2 S2: RSI for Embodied Intelligence

具身 RSI 通过策略、世界模型、技能库、harness、课程和环境的交互反馈闭环。POET、Voyager、World-VLA-Loop 展示环境—agent 共适应和技能继承，但当前策略会决定自己观察到的状态，感知/规划/控制/硬件错误难归因，真实试验又昂贵且有安全风险，因此多数证据仍来自仿真和外部奖励。

一个机器人“学到了”新的操作，可能是策略权重、可复用技能、世界模型或任务课程变化；四者带来的下轮收益需要分开测。尤其 agent 当前策略决定它能访问哪些状态，环境生成器又决定下一轮能见到什么，因此课程可能越来越难，也可能只围绕自身评测盲区打转。附录把证据分为**环境和课程、技能/记忆/harness、策略/动作模型、世界模型/evaluator**；仿真中的共同演化有 L4 迹象，ENPIRE 允许改训练程序和基础设施而触及受限 L5，但现实世界中带安全验证的完整自治环仍未成立（`src/appendix.tex:562-634`）。

### 4.3 S3: RSI for Software Engineering

软件工程最适合审计 RSI：代码、测试、版本和回滚都可执行。SWE-Exp 积累 issue 轨迹，Self-Harness 修改并回归测试自己的 harness，DGM 维护自修改 coding-agent lineage；但测试不完整、用户意图和安全性难覆盖，benchmark、utility、sandbox 和选择规则仍构成固定外环。

需严格区分**产品代码**与**开发产品的 agent 实现**：修补产品仓库说明完成了任务，修改 agent 的工具、提示拼接、记忆管理、测试流程并让它继续工作，才说明持久自改进。完整研究环可写为“开发任务→agent 级变更→仓库执行反馈→回归筛选→版本继承”。本领域 L2（自选 harness/技能/工作流变更）较成熟，L3 的学习者条件化任务生成刚出现，真实部署适应的 L4 仍少，DGM/SICA 仅呈现部分、过渡性 L5 特征，改进过程外环多仍固定（`src/appendix.tex:636-710`）。

### 4.4 S4: RSI for Healthcare

医疗 RSI 需要把专家反馈、指南、诊断证据和患者结局转成可追溯的记忆、推理策略、工具或工作流更新。MedAgent-Zero、EvoClinician、MACRO 和 HealthFlow 展示了模拟或回顾性场景的持久化，但真实结果延迟、混杂且人群依赖；任何临床更新都应有来源、适用人群、前瞻监测、可逆性和机构审批。

临床环的一次输入可来自就诊、影像或 EHR 分析；反馈可来自金标准、医生纠正、指南或后续结局；更新可能是病例记忆、诊断提问策略、多学科协作权重、影像复合工具或流程 safeguard。由于不能对患者任意试错，模拟病例中的“自我演化”不能等同临床上线。附录认为目前最扎实的是固定目标/评测下的 L2，部分系统有 L3 式主动取证或模拟 L4；真实纵向结局驱动的 L4、临床 improver 的 L5 基本未证实（`src/appendix.tex:714-778`）。

### 5 Industry Landscape and Preliminary Practices

产业案例把 L1–L5 置于真实约束下：数据基础、快速在线适应、质量系统外环、可执行工程搜索、可验证研究资产和跨任务元经验。它们共同表明，当前最可落地的 RSI 是组件、harness、记忆和流程级的受治理演化，而不是无约束的基础模型自我重写。

这里的“产业实践”并非统一强度的 RSI 实验。应对每个案例单独辨认：生产反馈从何而来，AI 能改哪个组件，候选如何验收，旧状态和失败记录是否保留，下一任务是否调用新版本。公司公开数字能说明某一范围内的工程效果；若没有对照、受保护评测和连续多代数据，就不能推断普遍的自我加速。附录产业表把 72 家公司或团队按组织类型列出，并明确其中的 B0–L5 标签是作者分析映射，不是公司自称的等级（`tables/industry_table.tex:17-28`）。

### 5.1 Theseus: Environment--Data--Model Co-Evolution for RSI Intelligence

Theseus 把环境重建、任务数据生成、任务模型训练和环境再迭代组成四步共进化环。早期 workspace 实验中，清洁环境相对噪声环境使 8 个模型—harness 配置提升 21.7–51.6 个百分点；重建 Collection Map 与 Event Log 后，5 个固定配置提升 18.65–39.67 个百分点，但出现少量 scope-creep 回归。结果说明环境状态可能是 agent 能力上限的一部分，尚不能证明完整多代学习环已经闭合。

**如何读它的四步环。** 第一步把过去的环境修订经验变成训练任务，训练环境修订模型；第二步在重建的环境中暴露 agent 真正不会解决的问题，据此生成任务数据；第三步用这些数据改进任务模型；第四步更强模型再参与环境修订和任务生成。图里上层的环境修订模型与下层任务模型互相提供新经验，这是作者提出的完整构想（`src/theseus.tex:57-69`）。

**实验实际验证到哪里。** 清洁与噪声 workspace 的对照说明环境质量可严重限制固定模型和 harness；另一组在固定模型与 harness 下比较裸 workspace 和附加 Collection Map/Event Log 的重建环境，说明改善环境本身可改善任务表现。两组各有 30 个任务，但分别使用 1,280 与 547 条 rubric，不能把增益当作同一实验的连续两代收益。部分任务因修改范围过大而回退，且完整的“环境→数据→模型→再环境”循环尚未被跨代验证（`src/theseus.tex:20-69`）。

![Theseus proposed environment-data-model loop](../assets/2026_the-last-ai-built-by-humans-toward-genuine-recursive-sel_arxiv-2609-11873/figures/source_figure_018_theseus-s-proposed-four-stage-co-evolution-loop.png)

### 5.2 Lark: Building the Data Foundation for Reliable Enterprise-Level RSI

Lark 把企业文档、消息、会议和任务构造成持续更新的知识图，并同时建设数据质量评估和失败归因层。内部报告称图检索使人工可用性从 52% 升至 65%、自动评估从 47% 升至 56%，自动评估与人工约 84% 一致；不过标准、关键样本和重要变更仍由人定义、抽查和批准。其核心启示是：没有时间对齐的数据、可靠 evaluator 和细粒度归因，自动更新只会放大噪声。

**改进对象与闭环。** 企业协作不断产生文档、消息、会议和任务；知识图把分散信息连接为实体、事件、人员和时间关系，再供跨来源问答。Lark 不只看是否能建图，还把图错误归因到下游答案：时间敏感问题应按查询时间过滤，低质量合成问句要重写，错误类别进入下一轮数据和评测修订。自动评估先用绝对判断排除明显不可用输出，再以 GSB 对比决定候选系统是否晋级（`src/practice.tex:8-21`）。

**证据边界。** 从 52% 到 65% 是内部人工“任务可用性”，47% 到 56% 是内部自动评估可用性，两者不是统一的生产 KPI。自动评估约 84% 的一致率意味着仍有需要人工校准的分歧。它证明了后续 agent 改进所需的数据与测量基础正在建立，但重要标准和变更由人批准，不能据此认定已经出现完全自治的元改进。

![Lark data foundation loop](../assets/2026_the-last-ai-built-by-humans-toward-genuine-recursive-sel_arxiv-2609-11873/figures/source_figure_011_lark-s-data-foundation-loop-for-rsi-where-collab.png)

### 5.3 Xiaohongshu: Dual-Timescale RSI for Recommendation

Intent-Memory Agent 用 Content、Who、Need 三层结构化记忆吸收点击、停留、收藏、搜索、转化和负反馈；快周期更新用户状态，慢周期把高价值 hard cases 经过自动评估、人工抽查和数据重建后固化到参数。公司自报 Discovery Feed score\_mean@16 从 2.211 到 2.366，in-video feed 从 1.537 到 1.739；后者的评测样本较小，论文未证明点击率或转化率同步提升，因此应视为初步 score@16 证据。

**为什么要两种时间尺度。** 在线层依据近期行为增补、强化、替换或衰减用户记忆，并忽略无信息反馈；所以持久化目标是下次推荐会读取的用户表示，而非这次推荐列表。Content 指内容主题，Who 指用户状态，Need 指推断需求；三个检索视角避免把主题相似误当需求相同。慢层把在线 hard case 做自动评判、人工抽查、规则纠正和训练样本重建，再后训练 agent 并部署新版本。快层保存个体短期变化，慢层把重复验证过的共性模式写入模型（`src/practice.tex:80-88`）。

**结果如何解释。** Discovery Feed 的 score_mean@16 增 7.0%、score_median@16 增 4.8%；in-video feed 的 score_mean@16 增约 13.1%，后一项仅来自 470 个基线样本与 447 个新模型样本的离线比较。Discovery Feed 两项的评测协议在该段未明确。论文没有给出相应的点击、转化或长期用户满意度增益，因此这些数据支持“公司报告的 score@16 指标改善”，不足以证明完整商业收益或长期稳定 RSI。

![Xiaohongshu dual-timescale recommendation loop](../assets/2026_the-last-ai-built-by-humans-toward-genuine-recursive-sel_arxiv-2609-11873/figures/source_figure_012_xiaohongshu-s-dual-timescale-rsi-loop-for-recomm.png)

### 5.4 Humanlaya: Delivery-Driven RSI for Data Quality Assurance

Humanlaya 把当前批次的 Quality Checker–Refiner–Delivery Checker 作为内环，把跨批次的错误归因、版本化 prompt/few-shot/skill 更新作为外环。扫描 PDF 案例显示，系统把“抽取失败”与“文档质量差”拆开并在留出数据和人工复核后继承新规则；V0 到 V4 在 600 个未参与更新的任务包上将关键缺陷率从 9.0% 降到 3.7%，人工处理时间从 48 降到 27 分钟。它是有人工闸门的 scaffold-level RSI。

**内外环的边界。** 一个交付包包含任务描述、附件、参考答案、评分 rubric 和验证要求。内环在当前包里定位缺陷、修复、复查，只能改善当前数据工件；外环在多个交付批次后汇总内部审查、客户反馈和使用证据，针对反复出现的原因改质量检查系统本身，再让新版本处理未来批次。若没有外环，反复修 100 个包也只是批量 B0 式工件修复（`src/practice.tex:93-111`）。

**扫描件案例的诊断价值。** 工具解析不了三页扫描 PDF，旧 Quality Checker 因而误判附件不可用。人工确认扫描件清晰后，真正该改的是“工具失败与文件质量不能等价”的判定规则。新规则和 few-shot 先在未参与修改的任务包上验收，再人工审查、版本晋级。这个案例直观体现 RSI 对跨组件归因的要求。四次更新后，同一基础模型、工具和处理预算下，600 个留出包的关键缺陷率降低 5.3 个百分点，人工处理时间降 21 分钟；但晋级仍依赖人工真值和批准。

### 5.5 ModelBest: Zero-Human Industrial AI Engineering

Forge Engineering 以目标模型、硬件和并行要求为输入，从空代码库生成、测试和优化可生产实现。项目内 loop 用固定架构约束和可执行反馈优化 kernel、并行和训练实现，跨项目 loop 把成功/失败经验、参考实现和失败规则写入共享知识库；这类工程任务反馈便宜、可回滚，因而比开放式研究更接近高自治，但仍保留架构和评测边界。

**双层改进的证据。** 单个项目里，agent 按规格确定高层架构，再循环编写实现、运行正确性和性能测量、诊断瓶颈、整合成功的 GEMM/FlashAttention 等实现；项目之间，把参考实现、性能结果、成功策略和失败规则写入知识库，让下个模型与硬件任务从已有经验开始。前者主要改当前工程产物，后者才是跨项目继承的关键（`src/practice.tex:128-135`）。

**量化结果与限制。** ForgeTrain 从空目录加参考脚本/模型规格开始，报告约 8 小时达到 Megatron-LM v0.15 水平、1.5–2.5 天超越；MiniCPM4-0.5B 的 MFU 从 40.1% 至 44.1%，8B 从 47.0% 至 50.9%。ForgeStencil 报告相对公开最优实现 1.15–1.9 倍加速，端到端中位数 1.41 倍。对人工“3–5 人、6–12 个月”的比较是估算，不能当同协议随机对照；当前材料也未拆出跨项目知识库对收益的独立贡献。

![ModelBest two-level Forge Engineering loop](../assets/2026_the-last-ai-built-by-humans-toward-genuine-recursive-sel_arxiv-2609-11873/figures/source_figure_014_modelbest-forge-engineering-as-a-two-level-rsi-l.png)

### 5.6 Tencent Hunyuan: Experience-Driven Self-Improvement

Hyra 用 Experience Bank 保存代码、产物、执行日志、分数和 evaluator 反馈，Context Agent 重组多样上下文，多个 Proposal Agent 在隔离 sandbox 中并行搜索。论文提出累积经验**可用于**修订 evaluator 以堵住 reward hacking；伴随材料报告 nanochat BPB 0.9015、nanoGPT Speedrun 76.4 秒、SOL-ExecBench 0.771，优于给出的对比值。这些发布方结果展示可执行经验的保留与复用，尚未独立验证评测器修订的效果。

**继承的不是一段文字总结。** Context Agent 把既有代码、制品、运行日志、分数和评测反馈重组成不同的启发上下文；多个 Proposal Agent 异步生成候选，在隔离环境执行，把完整轨迹写回 Experience Bank。这让后续轮次能够直接复用有用实现、组合旧策略并避开已经失败的路径。若初始 evaluator 粗糙或可被投机，系统还可能依据累积经验细化粒度、增加比较基线或修补奖励漏洞；这一步进入 L5 所关心的评测机制改动（`src/practice.tex:140-154`）。

**三项成绩不可混成一个“RSI 提升率”。** nanochat 的验证 BPB 从引用对比的 0.9109 降至 0.9015；NanoGPT Speedrun 达目标 loss 时间由 77.5 秒降至 76.4 秒；SOL-ExecBench 平均 SOL 由 0.754 升至 0.771。任务、基线、方向与单位不同，只能分别陈述。源码所给是随附材料结果，没有独立复现或多代 evaluator 改动的消融，因此不能把这三项直接归因给元改进机制（`src/practice.tex:155-207`）。

![Tencent Hunyuan Hyra experience-driven loop](../assets/2026_the-last-ai-built-by-humans-toward-genuine-recursive-sel_arxiv-2609-11873/figures/source_figure_015_experience-driven-self-improvement-in-tencent-hu.png)

### 5.7 Agent-Native Research Lab: Verifiable Research Infrastructure for RSI

ARA 用可执行研究资产保存形式逻辑、代码/规格、成功与失败分支图和原始证据，使后继 agent 不只继承论文结论，还能重放假设和失败路径。rit 协议从日志重新抽取经验数字，Lean 4 等工具检查分析性主张，只有通过机器验证的主张才进入共享状态。作者分别报告 ARA 的既有工作问答准确率为 93.7%（传统论文 72.4%）、RE-Bench 复现率从 57.4% 升至 64.4%；另在 Chip-Bench 报告 Level-3 CPU 优化得分 5.8416，**相对相同基础模型上的标准 agent 基线**速度快 2.7%、面积小 21.5%。这些是不同评测，不能混为 Chip-Bench 的一组结果；多代同预算复利仍待验证。

**基础设施为什么重要。** 普通论文通常只保留最终叙事，丢失失败分支、具体参数、执行日志和可执行规格。ARA 同时保存形式逻辑、代码/规格、探索图和原始经验数据；后继 agent 可以检查一个结论为什么成立，也能避免重复走过的失败分支。rit 从执行日志确定性重提取经验数字，Lean 4 等形式系统检验可形式化的分析命题，目的是阻止伪造数字和不可复现结论进入共享研究状态（`src/amber.tex:1-7`）。

**证据分层。** ARA 问答与 RE-Bench 复现数字测量的是“研究资产是否更易被继承”；芯片设计中的 SystemVerilog、测试台、综合、布局布线、时序和形式等价检查则测试“工程候选能否被机器验证”。Chip-Bench 的 Level-3 CPU 结果包括 97 条定向测试和 350 个随机差分程序，但仍是特定设计任务的性能，不是整个科研系统跨多代加速的证明（`src/amber.tex:9`）。

![Agent-Native Research Lab verifiable inheritance loop](../assets/2026_the-last-ai-built-by-humans-toward-genuine-recursive-sel_arxiv-2609-11873/figures/source_figure_016_agent-native-research-lab-s-agent-native-rsi-loo.png)

### 5.8 Frontis.AI: Enterprise Agent Evolution and Cross-Task Meta-Improvement

Frontis Horizon 的 ME–WE–MA 架构把人机交互/记忆/发布、300 多个专业 agent 的执行和 agent 构建评测演化分开。Benchmark OS 用程序检查和隔离 judge，候选版本经过回归安全、目标达成和异常鲁棒三道闸门；系统还保留问题、诊断、修改、验证和适用条件，支持跨任务元经验迁移。公司报告 76 个可比任务平均分 5.25 到 5.87，并称跨任务经验使未见任务进化快约 20%，但仍是公司自报结果。

**ME、WE、MA 的分工。** ME 负责用户交互、上下文记忆和发布批准；WE 是处理金融、法律、工程、人事等任务的专业 agent；MA 负责构建、评测和演化这些 agent。MA 收到生产反馈后，先辨别是路由、执行机制还是专业能力的问题，再给出边界明确的改进目标；人确认后可改 prompt、技能、工具和 harness。Benchmark OS 用可复现环境、程序检查和与被测 agent 隔离的模型评审降低自评偏差（`src/practice.tex:227-241`）。

**元经验如何转移。** 经验库保留问题背景、诊断理由、候选改动、验证结果和适用条件；跨任务复用时仍需重新确定权威来源、时间有效性并再次验证。公司报告两个月内发起 216 个改进任务、涉及 117 个 agent，63 个完成至少一轮；76 个可比任务平均分从 5.25 到 5.87，中位机器处理时间 27.8 分钟。“未见任务快约 20%”是累计超过 100 个任务的元经验后，在内部未见任务上，相对**不使用跨任务经验**流程的对照；35B 的 Frontis-MA1 在 MLE-Bench Lite 从 39.39% 到 60.61%（加搜索 71.21%）是另一项模型训练结果，不能等同于企业 agent 的元经验迁移（`src/practice.tex:241-247`）。

![Frontis ME-WE-MA architecture](../assets/2026_the-last-ai-built-by-humans-toward-genuine-recursive-sel_arxiv-2609-11873/figures/source_figure_017_frontis-horizon-s-me-we-ma-architecture-combines.png)

### 6 Challenges and Future Directions

作者提出八条把局部自动化连接成持续 RSI 的研究线索：

1. **跨组件诊断与协同改进**：把失败转成可检验的干预假设，用冻结、消融和依赖记录区分数据、模型、工具、harness、环境和 evaluator 的作用。
2. **学习者条件化的经验获取**：同时估计经验的正确性、难度和真实学习价值，防止错误反馈进入下一轮课程。
3. **持久状态管理与可靠复用**：记录技能、记忆和工具的证据、适用条件、依赖与效果，分开测更新质量、激活、忠实执行和下游收益。
4. **领域反馈下的受治理适应**：根据科学、具身、软件和医疗的不同风险选择仿真、回放、沙盒、监督或分阶段发布。
5. **可信的改进机制演化**：把 proposer、evaluator 和 research policy 的变化分开验证，维护独立锚点，避免协同投机和跨版本不可比。
6. **继承改进能力的长期评测**：在匹配总预算下记录多轮轨迹、拒绝、回退、遗忘、迁移和资源，区分当前任务收益与产生更强后代的能力。
7. **资源感知与人机协作**：把诊断、经验获取、搜索、验证、监控和人工审查的时间与成本合并计算，并支持自适应停止、升级和终止。
8. **跨轮继承的可复现基础设施**：保存父状态、候选变化、动机证据、评测配置、验收决定和后续使用，配合版本化数据、环境和 evaluator 进行重放。

本章的总判断是：真正的 RSI 证据不是无人值守时间更长，也不是某次分数更高，而是继承变化能在明确资源和权限约束下，让后续轮次更有效地获取经验、发现干预或验证继任者。

**1. 跨组件诊断。** 任务失败可能同时来自检索资料过期、prompt 误导、工具接口变化和 verifier 漏检；更新一个组件带来的收益可能只是在补偿上游问题。实验设计应先提出“改 X 会解决 Y 错误”的可反驳假设，再冻结其他部件、做定向消融、记录交互项。Theseus 的清洁环境对照说明环境会影响固定模型表现，但尚须把环境→数据→模型的完整多代增益拆开测（`src/future.tex:59-65`）。

**2. 学习者条件化经验。** 正确性、对当前学习者的难度、训练后的长期收益是三个不同变量。AZR 的可执行判定强化正确性，R-Zero 的一致性/不确定性更偏向难度估计，两者都不能单独推出学习价值。应按相同数据访问和总训练/验证预算，对比自适应、固定课程、冻结 learner-state 输入三组，在迁移和旧能力保持上看多轮结果（`src/future.tex:66-69`）。

**3. 持久状态管理。** 一个技能可能编写正确却从未被检索，也可能被检索后没有执行，或在新模型/新 API 上过时。每个被继承产物需带来源、依赖、适用前提、接受时的配对对照与以后真实调用记录；库满时要判断合并、更新、淘汰还是再次验证。Library Drift 说明无上限添加会退化，过度退休也会损害少见任务（`src/future.tex:70-73`）。

**4. 领域治理。** 软件可以沙盒执行并回滚代码，却仍可能遗漏隐含规格；机器人无法撤销物理试验，医疗也不能用患者做无限制探索。因而系统应按改动的风险选择仿真、回放、受控上线或专家审批，监视分布变化后的效益与伤害。人掌握目标、权限和高风险发布权，并不抹掉内部改进环的自治；这些边界要在报告中明示（`src/future.tex:74-77`）。

**5. 改进机制的可信演化。** 当 proposer 和 evaluator 都能改时，彼此适应可能制造虚假上升；当评价尺度换了，历史分数也失去直接可比性。一个可检验的方案是冻结当前 evaluator 评价一段时期，用独立 anchor 验证其替代版本，再重评受影响候选；另外分别消融候选生成器和 evaluator 的修改，再检验组合收益。RQGM 提供了局部设计，仍不解决所有开放研究目标上的独立验证（`src/future.tex:78-81`）。

**6. 长时序后代能力。** 应比较原始机制与进化机制从同样初始状态出发、在同样预算和新任务上能产出什么后代，报告所有候选、拒绝、回退、失败 seed 和评测开销。DGM 式谱系提示暂时更弱的父代也可能有较强后代潜力；AIDE² 的外层效率未达显著优势说明单次成功更新不足以证明元能力。研究真正需要估计的是“继承一个修改后的改进器，让以后的每轮更有效多少”（`src/future.tex:82-85`）。

**7. 总资源与人机协作。** 只报告自动运行时长或最佳 kernel 速度，会遗漏任务设计、数据收集、候选评测、失败排查、维护和人工审查的费用。应报告达到同一受保护能力目标所需的总时间/计算/人工量，研究何时继续试验、何时升级人工审查、何时停止。初期基础设施投入可以很大，但必须由随后轮次较低的边际成本或较大有效收益抵偿（`src/future.tex:86-89`）。

**8. 可重放的继承基础设施。** 一个后继者需要的不只是父代的最终结论，还包括父状态、候选变更、动机证据、环境/数据/evaluator 版本、失败分支和验收原因。Lark 的时序数据、Humanlaya 的质量版本、Hyra 的执行经验、ARA 的研究资产是互补方向。重放与形式验证只能证明“按给定规格/日志可复核”，不能证明原实验问题或规格覆盖了真实需求；公开性、重放能力和独立复现应分别报告（`src/future.tex:90-93`）。

### 7 Conclusion

结论将路线图收束为五个阶段：执行改进、选择策略、获取经验、环境适应和递归元改进。论文的贡献是提供共同的 improvement-loop 语言，把科学、具身、软件和医疗反馈条件放在同一框架下，并用产业案例说明当前能力主要停留在组件和流程级；是否能在长时间、多代、可比预算下累积可迁移收益，仍需进一步评测。

**我的证据判读。** 这篇文章更强的贡献是“判定语言与研究议程”，不是已经演示出通用 RSI：B0 输出修订与 L1/L2 工程自动化的证据较多；L3 依赖学习者条件化经验是否真正带来跨轮收益；L4 要看部署反馈和持久状态的激活/回退；L5 目前主要有受限机制原型及自报产业实践。论文将结构上的递归与效能上的递归分开，是避免夸大领域进展的关键。其限制在于引证系统异质、工业资料自报较多、HCI 原始逐项数据未随归档提供，并缺少统一的长时序同预算实证比较。阅读时应将“作者提出的路线”“被引用系统报告的数字”和“独立确立的结论”分层保留（`src/conclusion.tex:10-13`）。

## 代表性工作矩阵

| 层级/场景 | 代表系统 | 持久化对象 | 主要外部约束 | 论文中的证据判断 |
|---|---|---|---|---|
| B0 | Self-Refine、Reflexion | 当前会话上下文 | 固定流程和评测 | 输出改进，非 RSI |
| L1 | FineWeb-Edu、EDIT、AIPC | 数据、训练/部署产物 | 目标、流程、验收标准 | 执行自治较成熟 |
| L2 | GEPA、ADAS、AutoResearch、AutoKernel | prompt、harness、训练/实现方案 | 目标、指标、预算 | 策略搜索可验证但易过拟合 |
| L3 | AZR、R-Zero、VOYAGER、SIMA 2 | 课程、任务、技能、经验 | 任务格式、奖励、更新规则 | 学习议程自治依赖反馈质量 |
| L4 | ACE、PANDO、Metis、Tax AI | 记忆、技能、工具、代码 | 权限、回归测试、人工发布 | 部署适应有早期证据 |
| L5 | STOP、RQGM、A-Evolve-Training、Hyra | improver、evaluator、研究策略 | 目标、锚点、资源和 substrate | 主要是受限原型/产业早期证据 |
| 应用域 | Science、Embodied、Software、Healthcare | 工具、策略、技能、工作流 | 实验/物理/测试/临床反馈 | 反馈 regime 决定可达自治 |

## Benchmarks / Datasets / Frameworks

- **HCI**：按 benchmark 进入年份前沿归一化不同能力轨迹，适合观察剩余能力空间，但依赖协议可比性。
- **软件与 agent**：SWE-bench、SEA-Eval、SEAGym、HarnessDev、S3Gym，关注执行、回归、迁移和后代质量。
- **经验/记忆**：Evo-Memory、PANDO、Metis、Library Drift，关注长时序复用、激活和技能生命周期。
- **科学/研究**：MLE-Bench、PaperBench、AI Scientist-v2、RE-Bench、Chip-Bench，关注可执行实验、复现和研究资产继承。
- **产业框架**：Lark data foundation、Humanlaya quality loops、ModelBest Forge、Hyra Experience Bank、Frontis Benchmark OS、ARA/rit。

这些资源的共同缺口是：多代、匹配预算、独立评测和“改进机制本身”的长期效果尚未形成统一标准。

## 关键图表与表格

### 关键图

- **RSI 五级概览图**：展示从 L1 执行到 L5 元改进的责任扩张，适合作为全文导航。
- **HCI 能力轨迹图**：显示数学/科学与软件/工具代理的不同增长速度，并用阴影区域示意 RSI 可能优先填补剩余空间。
- **五类 loop 图**：把每级新内化的组件标出来，直观区分 B0、L1–L5 的闭环位置。
- **应用 regime 图**：说明科学、具身、软件、医疗在反馈可验证性和代价上的差异。
- **L3/L4/L5 loop 图**：分别强调学习议程、部署持久化和改进机制继承。

### 关键表格

- **邻近范式对比表**：用跨轮学习、持久保留、自修改、候选提议、验证、继任者重入、机制修订和机制复用区分持续学习、AutoML、agentic AI 与 RSI。
- **L1–L5 技术/产业表**：按改进对象和外部约束排列代表系统。
- **HCI 域轨迹表**：汇总不同 benchmark family 的协议链接、来源权重和域级聚合。
- **产业 landscape 表**：把公司案例映射到自治层级、改进对象和是否有多轮证据。

图表的共同阅读方式是先看“什么被改变和继承”，再看“谁决定验收”；不要把图中的示意延伸端点当作实证预测。

## 开放问题与未来方向

最关键的开放问题可以压缩为四个：

- 如何在跨组件、跨任务、跨模型迁移时做可靠归因？
- 如何让 learner-conditioned experience 同时满足正确性、覆盖、难度和学习价值？
- 如何管理会过时、会冲突、可能被错误激活的持久状态？
- 如何在评测器会被优化的情况下，证明改进机制真的产生了更强后继者？

论文还把人工权限、资源成本、回滚、可复现性和独立复现视为 RSI 的组成条件，而不是事后治理附加项。

## 可复用研究线索

1. 把任何“自我改进”系统画成五元链：经验来源 → 改进目标 → improver/strategy → verifier/acceptance → 继承状态。
2. 为每个更新记录触发证据、适用条件、调用情况、旧能力影响和回滚路径。
3. 用 learner-independent、冻结机制、留出任务和新环境对照，拆分额外搜索、额外数据和真正机制收益。
4. 把“更新质量”和“运行时使用更新的能力”分开评估。
5. 对 L5 实验报告多轮完整轨迹、总成本、拒绝和回退，而不只报告最佳后代。

## 对我当前研究/项目的启发

如果把这套框架用于一个 agent 或训练系统，第一步不是增加一个“自我反思”模块，而是明确要把哪类责任交给系统：执行、策略、经验、部署适应还是机制继承。随后应建立版本化经验库、独立评测集、可回滚发布和跨轮 provenance；只有当更新在后续任务中被实际调用并改善下一轮改进，才应使用 RSI 这一强表述。

## 附录 A：RSI Landscape 与改进目标分类

附录 A 的环图覆盖作者纳入的 **491 篇论文**：内圈是 L1–L5 自治等级，中圈是主要改进对象，外圈是细分目标。读图可得 L1 215 篇（43.8%）、L2 155 篇（31.6%）、L3 64 篇（13.0%）、L4 28 篇（5.7%）、L5 29 篇（5.9%）；L1+L2 共 75.4%。等级百分比按论文数计算；一篇论文若同时修改多个对象，对目标类别贡献的是分数权重，所以不能把各目标扇区解释为互斥论文数。这张图揭示现有研究“改什么”的分布，不是各级 RSI 已经成功的概率（`src/appendix.tex:17-45`；`figures/RSI-Landscape.pdf`）。

![RSI landscape: levels and improvement targets](../assets/2026_the-last-ai-built-by-humans-toward-genuine-recursive-sel_arxiv-2609-11873/figures/source_figure_008_rsi-landscape-autonomy-levels-and-improvement-ta.png)

附表把可修改部件归成十组，环图还设有 **Other** 残余类；十组不是对每个图中扇区的穷尽命名。读它时要把“目标所在系统内外”与“是否改进未来改进机制”两轴同时看：

| 主类 | 可修改部件举例 | 判读重点 |
|---|---|---|
| 1 Prompt & Context | 系统提示、few-shot、上下文构建 | 更新是否跨任务继承，还是当前提示修订 |
| 2 Memory & Knowledge | 经验、技能知识、检索索引 | 是否记录来源、适用条件与失效情况 |
| 3 Harness / Workflow & Control | agent 控制流、工作流、协调和路由 | 新控制逻辑是否在后续调用 |
| 4 Tools & Skills | API、可执行工具、技能包 | 是否有执行检查、版本和回滚 |
| 5 Model | 权重、适配器、架构等 | 模型更新与其他层的收益需分开归因 |
| 6 Trainer / Optimization System | 训练算法、优化器、搜索器 | 已触及产生后代的过程，但需看是否继承 |
| 7 Evaluator & Feedback System | reward、verifier、credit assignment | 尺子变化后必须保留独立锚点 |
| 8 Data & Environment | 训练经验、课程、仿真器、世界模型 | 更新经验来源能否改善后续学习 |
| 9 External Artifact | 产物代码、算法、科学/设计成果 | 只改外部工件本身不证明 AI 自改进 |
| 10 Full-system / Co-evolution | 多目标 harness、模型—harness、改进环 | 是否有跨组件因果归因及机制继承 |

第 9 类尤其重要：自动发现新算法、设计电路或修产品代码，可能是非常强的 AI 应用，却不能仅凭产物改进认定为 RSI。第 10.3 类才明确把“生成、评估、选择和应用未来更新的环”列为目标，是与 L5 判定最贴近的目标标签；目标标签和自治等级仍非同一维度（`src/appendix.tex:45-331`）。

## 附录 B：产业系统图谱

产业表按**组织类型**整理 72 家不同公司或团队、每项产品/代表工作一行，公开资料截点为 2026 年 9 月。六类分别为：A 前沿基础模型与通用 agent 实验室；B 以 RSI/AI4AI 为核心的公司；C 自治研发与科学发现公司；D agent 优化、评估和学习基础设施；E 具身、世界模型与持续适应公司；F 持久记忆与个人 AI 公司。表格标签将案例映射到 B0–L5，只是作者的分析归类，不是企业自称的级别；`adj.` 表示仅有 RSI 邻接设施/行为，`cand.` 表示该等级有可能但尚未充分证明，`target` 是未来目标而非当前能力。带星号的企业身份或技术边界还需更强公开验证（`src/appendix.tex:349-359`；`tables/industry_table.tex:14-19,60-358`）。

这张表主要提供**查找证据的入口**：同一企业可能同时提供模型、数据和 agent 产品，但某个产品是否有持久更新环，须回到技术资料核对继承对象、评测与发布权。尤其“持续记忆”不自动是 L4，“自动科研”不自动是 L5。第 5 章八个深入案例在机制与指标上更具体，产业大表则覆盖面更广、证据强度不一。

## 附录 C：四个应用域的组件级证据

附录 C 是第 4 章的正式展开，不是无关补充。每域先描述反馈性质和改进环，再按照可修改部件梳理系统，最后对照 B0–L5 判断距离完整 RSI 还有什么缺口。同一系统可以跨领域，分类并不互斥（`src/appendix.tex:457-479`）。

### C.1 科学发现：从实验工件到科研能力

**假设模块。** HypoForge 把批评和执行结果分别沉淀为假设生成、实验设计、执行技能；EvoScientist 检索有前景和失败过的研究方向，修改未来提案。TTT-Discover 以测试时强化学习更新模型，聚合物发现系统把模拟评估过的候选写回训练数据并重训生成器。前两者主要是记忆/程序技能继承，后两者触及生成模型；四者通常仍在固定领域目标和选择规则内运行。改进当前的聚合物候选不是改进假设生成能力，需分别衡量（`src/appendix.tex:495-504`）。

**实验 agent。** Test-Time Tool Evolution 在 SciEvo 的 1,590 项任务中演化了 925 个工具，重点是“生成→验证→以后可调用”；CASCADE 保存化学/材料技能，S1-NexusAgent 从完整轨迹提炼 Scientific Skills，SkillFoundry 从论文、代码库和 API 编译、验证、合并或裁剪技能包。DrugSAGE 将 16 项任务的经验证程序、训练策略和常见故障应用到 17 项留出任务，提供跨任务复用的直接证据；STELLA、EarthLink、OriGene 分别扩展生物医药工具、气候脚本和分析模板。白盒流体控制例还需要把最终 controller 的改善与**造 controller 的 agent**改善分开。科学技能可靠继承还需明确使用前提、执行测试、来源、版本和回滚；工具库变大本身不是收益证据（`src/appendix.tex:505-519`）。

**反思和改进器。** SIA 的 Feedback-Agent 能在 scaffold、工具、重试/搜索逻辑和 LoRA 权重之间选修订对象；CORAL 用长期异步 agent 根据既往尝试安排试验、评估调用和共享经验；SAGA 在固定高层科研目标下重权重或新增可执行子目标。它们触及跨组件干预和研究优先级，但固定的总体目标、evaluator、接纳程序仍明显。附录判定：成熟的是 B0/L1，L2 是当前最强前沿，L3 有早期经验选择证据；要称完整科研 RSI，还须证明假设、实验与解释机制跨轮一起变得更有效，而不只是本轮科学结果更好（`src/appendix.tex:520-560`）。

### C.2 具身智能：课程、技能、策略和世界模型共演化

**环境与课程。** POET 共演化环境—agent 对，利用“不太容易也不至于无解”的最小准则、政策转移来保留踏脚石；EnvGen 根据小型 RL agent 的薄弱技能生成仿真配置；GenEnv 将模拟器参数视为可训练课程政策，用接近学习者能力边界的奖励选题。OMNI-EPIC 生成可执行环境和奖励代码，并利用旧任务 archive 与进度寻找新颖可学任务；SimWorld Studio 编写 Unreal Engine 环境代码，通过编译、物理与视觉批评修复，再根据学习者表现安排更难世界。它们让未来经验分布受 learner 影响，但虚拟世界有效不自动外推到真实机器人（`src/appendix.tex:578-587`）。

**技能、记忆和 harness。** Voyager 存可执行 Minecraft 技能；LRLL 通过探索及 wake–sleep 整理组合机器人程序；EmbodiSkill 区分“技能本身错”与“agent 没按正确技能执行”，防止错误归因。SHAPER 联合修改技能和上下文代码，ASPIRE 诊断运行失败后测试并保留修复，ENPIRE 让 coding agent 在重复真实实验中改机器人政策、训练流程及支撑基础设施。后者触及较广的自修改，但环境接口、评测器与安全约束仍固定（`src/appendix.tex:588-595`）。

**政策与世界模型。** Self-Improving Embodied Foundation Models 用预训练模型导出成功信号让机器人练习；MEDAL++ 学会完成及撤销动作以减少人工 reset；Q-Planning 冻结大行为克隆政策、只根据成败轨迹更新小 value function；SERP 从近期导航失败调动作模型。VLAW 用真实轨迹改动作条件视频世界模型，再生成合成经验；World-VLA-Loop 让政策失败改世界模型、改过的世界模型再训练政策；Motus2 把政策、仿真、评价函数整合，SAIL 用执行后的轨迹微调视频规划器。**我的评测建议**是将政策、世界模型和课程分别冻结做消融，并在新的环境/机器人硬件上验证有效共演化（`src/appendix.tex:596-634`）。

附录的阶段判断是：L1 政策/模型更新已有，L2 可自选技能与 harness 修订，L3 的 learner-conditioned 经验选择出现，L4 的环境适应主要在仿真；ENPIRE 有受限 L5 特征。物理试验不能任意重置或撤销，未来系统还须对完整感知—规划—控制链归因，记录不确定性并在安全约束下发布。

### C.3 软件工程：产品修复与 agent 自修改分离

**agent 实现和 harness。** SICA 把 coding agent 的 Python 实现当作可编辑项目，读取历史版本/基准后自改，再用选中版本继续迭代；Self-Harness 从执行轨迹找重复弱点，让同一模型改 harness，并通过回归测试保留；Agentic Harness Engineering 将中间件、验证规则和控制逻辑拆为可单独编辑/撤销的文件，用结构化轨迹验证预测效果；Ouroboros 将审查通过的工具、上下文、prompt 与核心逻辑投入后续运行。四者都要在固定 benchmark、utility、sandbox 或人工审核之外审视其自治边界（`src/appendix.tex:654-666`）。

**经验与协作。** SWE-Exp 检索成功和失败 issue 轨迹；CODESKILL 提炼多层级程序技能，并随新轨迹更新或删除，保持技能库紧凑；EvoMAC 修改多 agent 的角色 prompt 和通信连接，不过报告的更新发生在每个任务测试时，不一定跨独立任务继承。关键判定是新技能或协作结构是否真正成为后续新 issue 的起始状态，而不只是当前仓库的一次性调试材料（`src/appendix.tex:667-674`）。

**改进过程。** DGM 保留多个 coding-agent lineage，让较弱分支仍可能成为未来父代；HGM 用后代谱系估计 metaproductivity，把**评测资源**更多分配给长期改进潜力更强的 agent，但其元选择规则本身没有持续自修改。Group-Evolving Agents 分享多父代成功和失败经验；DarwinX 在冻结模型外演化整套 harness，同时保护已解决任务；HELIX 提议 harness 改善当前执行、产出可验证轨迹再改模型、随后重建 harness 的循环。DGM/HGM 的启示是当前 benchmark 分数与“产生强后代的能力”不同；**我的评测建议**是保存完整谱系，并与固定资源分配或父代选择策略作对照（`src/appendix.tex:675-681`）。

附录判断 L2 最扎实，L3 的 Self-play SWE-RL/Socratic-SWE 属新兴课程方向，真实部署 L4 尚少；SICA/DGM 呈现部分、过渡性的 L5 特征，但完整的“改进软件研发 improver”收益未证明。软件测试可执行也不完备，用户意图、维护性、安全与跨仓库转移仍需外部检查（`src/appendix.tex:682-710`）。

### C.4 医疗：临床反馈必须受控继承

**临床记忆与知识。** MedAgent-Zero/Agent Hospital 把模拟就诊中的成功病例和失败教训写成未来可检索规则；Agent Mental Clinic 由监督模块对照标签，在分层记忆中保存诊断经验；MedAgentSim 合并病历与模拟互动经验。DxEvolve 将诊断过程压缩成可复用的“认知原语”；GSEM 用双层图记录经验和关联边，并按后续反馈调可信度；Evo-MedAgent 分开存临床案例、程序启发和工具可靠性。比起无限追加病例，后面三者更关注什么记忆何时适用，但目前多是模拟或回顾性标签证据（`src/appendix.tex:725-735`）。

**推理与协作策略。** EvoClinician 的 Diagnose–Grade–Evolve 环中，Actor 逐步问诊/开检查，Process Grader 衡量临床收益与成本，Evolver 改下一例会使用的 prompt 和记忆；这比在本例修正最终诊断更接近策略继承。EvoMDT 让肿瘤多学科各专科 agent 的 prompt、共识权重和检索范围随专家反馈调整；PsychAgent 将咨询轨迹提炼为技能，还用 rejection fine-tuning 内化部分技能。仍应检查过程评价是否与真实患者收益一致（`src/appendix.tex:736-744`）。

**工具与工作流。** MACRO 从验证过的影像处理轨迹构造复合工具并注册为未来高层动作；SkeMex 用 Read–Write–Assess–Govern 生命周期促进、合并、更新或删除临床技能；TissueLab 让专家纠正病理/影像/空间组学中间结果，指导主动学习与流程修订；HealthFlow 将 EHR 分析转成 safeguard、工作流、数据集锚点和代码片段，由 evaluator 找缺陷、reflector 验收/淘汰。工具技术上可运行、单病例反馈正确，都不足以证明跨人群、机构或时间安全（`src/appendix.tex:745-754`）。

附录判定医疗当前以 L1 持久病例知识和 L2 固定验收下的策略/工具改进为主，少数系统有 L3 式主动取证，EvoPatient 的模拟医患共演化可视作 L4 式探索；**真实纵向临床结果驱动的端到端 L4 与临床改进器 L5 仍基本空缺**。未来每个持久更新都须留下来源、适用人群、证据与不确定性，由临床机构把关、前瞻监测并可撤销（`src/appendix.tex:755-778`）。
