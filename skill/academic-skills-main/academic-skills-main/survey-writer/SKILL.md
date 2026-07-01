---
name: survey-writer
description: write a chinese survey draft around a research topic when the input includes a topic, multiple papers, abstracts, links, pdfs, or a user curated related-work list and the user needs a short survey, long survey, taxonomy, or method evolution summary.
---

# Survey Writer

用这个 skill 围绕一个研究主题组织多篇论文，输出中文综述草稿。重点是梳理研究问题、方法演化、代表性路线和当前局限，而不是逐篇摘要拼接。

## 工作流

1. 先确认覆盖范围：主题边界、论文数量、输入完整度。
2. 判断输出模式：简版综述或长版综述。
3. 依据 `references/comparison_dimensions.md` 建立对比维度。
4. 依据 `references/related_work_patterns.md` 组织 related work 语言。
5. 依据 `references/survey_template.md` 输出综述草稿。

## 模式选择

- 在材料较少、用户只需快速整理时，输出简版综述。
- 在材料较多、需要形成成稿框架时，输出长版综述。
- 如果输入覆盖不全，在开头明确说明“当前综述仅覆盖已提供材料，不代表完整文献全景”。

## 输入处理规则

- 接收研究主题、多篇标题、摘要、PDF、链接，或用户已有的相关工作列表。
- 如果不同论文信息粒度不一致，先按可比字段组织，再明确缺口。
- 如果用户只给了论文列表而没有内容，先做结构化框架和阅读建议，不要伪造具体实验细节。

## 输出规则

- 不要按“论文 A 说了什么、论文 B 说了什么”的流水账方式写作。
- 强调问题定义、方法分类、方法演化、代表性工作对比和开放问题。
- 在 benchmark、dataset、metric 部分，只总结输入中明确出现的信息。
- 在“开放问题”和“值得继续看的方向”部分，区分已有证据支持的趋势与个人推断。

## 证据与表述约束

- 不要把覆盖不全的材料写成全面综述。
- 不要编造时间线、代表作地位或 benchmark 事实。
- 如果论文数量过少，明确输出“这是初步综述草稿，不足以代表完整研究版图”。

## 何时读引用文件

- 始终读取 `references/survey_template.md`。
- 在组织论文比较时读取 `references/comparison_dimensions.md`。
- 在写 related work 段落时读取 `references/related_work_patterns.md`。
