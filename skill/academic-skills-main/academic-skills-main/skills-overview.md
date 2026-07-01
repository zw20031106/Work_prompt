# Skills Overview

本仓库围绕“学术研究工作流”组织 8 个 skill。它们不是互相割裂的单点工具，而是可以串联的研究助手组件。

## 组合关系

推荐的串联路径：

1. `paper-feishu-digest`
   用于发现最近值得关注的新论文，输出中文速递。
2. `paper-deep-note`
   用于对单篇重点论文做结构化精读沉淀。
3. `survey-writer`
   用于把多篇论文组织成综述草稿，而不是逐篇摘要堆叠。
4. `benchmark-extractor`
   用于把对比实验中的 benchmark、dataset、metric、baseline 抽成结构化资产。
5. `research-gap-finder`
   用于分析已有覆盖面、瓶颈和潜在切入点。
6. `experiment-log-summarizer`
   用于整理实验改动、结果变化和失败记录。
7. `review-rebuttal`
   用于处理投稿后的审稿意见和 rebuttal 组织。
8. `weekly-lab-update`
   用于把一周的阅读、实验和待讨论问题整理为周报与组会材料。

## Skill 一览

### `paper-deep-note`

- 定位：单篇论文精读卡
- 价值：把阅读结果沉淀为长期知识资产
- 特别要求：只基于摘要时必须明确标记判断边界

### `survey-writer`

- 定位：主题级中文综述草稿
- 价值：帮助从“读过很多篇”过渡到“形成结构化理解”
- 特别要求：强调方法演化、问题结构和覆盖边界

### `paper-feishu-digest`

- 定位：arXiv 监控和中文速递
- 价值：适合实验室晨报、组内共享和日常选题筛选
- 特别要求：提供可运行脚本和保守打分逻辑

### `review-rebuttal`

- 定位：审稿意见拆分与 rebuttal 草稿
- 价值：帮助区分必须补实验的问题和适合澄清的问题
- 特别要求：严禁编造实验结果或既有证据

### `experiment-log-summarizer`

- 定位：实验记录与失败经验总结
- 价值：减少“做了很多实验但很难复盘”的问题
- 特别要求：明确区分证据、猜测和下一步验证动作

### `benchmark-extractor`

- 定位：benchmark / dataset / metric / baseline 抽取
- 价值：把论文对比信息沉淀成后续可扩展的结构化表
- 特别要求：不确定字段必须标记为未知

### `research-gap-finder`

- 定位：研究空白与切入点分析
- 价值：帮助识别真正的研究空白，而不是阅读不全导致的“伪 gap”
- 特别要求：必须输出风险提示

### `weekly-lab-update`

- 定位：周报、组会提纲、英文简报
- 价值：把一周碎片化工作转成导师可快速阅读的总结
- 特别要求：避免流水账，突出结论和待讨论问题

## 文件阅读顺序建议

如果你想快速判断这个仓库是否符合预期，建议按这个顺序查看：

1. [README.md](/D:/lunwen/academic-skills/README.md)
2. [paper-deep-note/SKILL.md](/D:/lunwen/academic-skills/paper-deep-note/SKILL.md)
3. [survey-writer/references/survey_template.md](/D:/lunwen/academic-skills/survey-writer/references/survey_template.md)
4. [paper-feishu-digest/scripts/arxiv_digest.py](/D:/lunwen/academic-skills/paper-feishu-digest/scripts/arxiv_digest.py)
5. [tools/validate_repo_structure.py](/D:/lunwen/academic-skills/tools/validate_repo_structure.py)
