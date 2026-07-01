---
name: benchmark-extractor
description: extract structured benchmark information from academic papers when the input includes multiple pdfs, abstracts, or links and the user needs chinese notes or table-ready fields for tasks, datasets, metrics, baselines, sota claims, code release, or evaluation settings.
---

# Benchmark Extractor

用这个 skill 从论文中抽取 benchmark、dataset、metric、baseline、SOTA 等结构化信息，方便后续整理成表格、CSV 或 JSON。

## 工作流

1. 先按论文逐篇抽取稳定字段。
2. 参考 `references/extraction_schema.md` 统一字段名和缺失值写法。
3. 参考 `references/comparison_table_template.md` 输出中文说明版或结构化表格版。

## 输入处理规则

- 接收多篇 PDF、多篇摘要或一组论文链接。
- 如果不同论文信息完整度不一致，仍按统一 schema 填写。
- 未明确写出的字段统一写为 `未知`，不要臆造。

## 输出模式

- 中文说明版：适合先看整体 benchmark 版图。
- 结构化表格版：适合后续导出 CSV、JSON 或继续人工补全。
- 如果用户没有指定，默认同时给出简短说明和结构化表格。

## 输出规则

- 字段尽量包括：
  - 论文标题
  - 任务
  - 数据集
  - 指标
  - baseline
  - 是否报告 SOTA
  - 是否开源代码
  - 是否开源数据
  - 评测设置说明
  - 备注
- 对“是否报告 SOTA”这类字段，如果论文只是声称优于 baseline，但未明确写“state of the art”，优先写“未明确”。

## 证据与表述约束

- 不要根据常识自动补数据集、指标或开源状态。
- 如果只有摘要，明确说明当前抽取只是初步结果。
- 如果字段存在歧义，在备注里写出歧义来源。

## 何时读引用文件

- 始终读取 `references/extraction_schema.md`。
- 在组织表格输出时读取 `references/comparison_table_template.md`。
