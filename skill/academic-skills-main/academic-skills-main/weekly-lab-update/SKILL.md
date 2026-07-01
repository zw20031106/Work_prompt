---
name: weekly-lab-update
description: turn a week's paper reading, experiment progress, debugging notes, and next-step plans into a chinese weekly report, a chinese group-meeting outline, or an english brief when the user needs a concise lab update instead of a raw activity log.
---

# Weekly Lab Update

用这个 skill 把一周内的论文阅读、实验结果、失败排查和下周计划整理成周报、组会提纲和英文简版汇报。重点是突出结论、变化和待讨论问题，而不是记录流水账。

## 输出模式

- 中文周报
- 中文组会提纲
- 英文简版汇报

如果用户没有指定，默认输出中文周报，并附一版简短组会提纲。

## 工作流

1. 先按“论文阅读”“实验进展”“当前问题”“下周计划”整理输入。
2. 参考 `references/weekly_report_template.md` 生成中文周报。
3. 参考 `references/meeting_outline_template.md` 生成中文组会提纲。
4. 在需要英文短汇报时，参考 `references/english_brief_template.md`。

## 输入处理规则

- 接收本周读过的论文、本周实验结果、当前问题和下周计划。
- 如果输入更像碎片笔记，先归并同类项，再提炼结论。
- 如果一周内进展较少，也不要硬凑内容，明确写清当前卡点和需要讨论的问题。

## 输出规则

- 默认结构包括：
  - 本周进展
  - 论文阅读总结
  - 实验结果总结
  - 当前问题
  - 下周计划
  - 希望讨论的问题
- 不要写成按时间排序的流水账。
- 优先写“发生了什么变化、为什么重要、接下来怎么处理”。

## 证据与表述约束

- 不要夸大进展。
- 如果某些结论只是初步观察，直接标注“初步”或“待验证”。
- 如果实验失败较多，也要把失败经验整理成可讨论信息。

## 何时读引用文件

- 输出中文周报时读取 `references/weekly_report_template.md`。
- 输出组会提纲时读取 `references/meeting_outline_template.md`。
- 输出英文简报时读取 `references/english_brief_template.md`。
