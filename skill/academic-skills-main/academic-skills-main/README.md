# academic-skills

`academic-skills` 是一个面向中文科研工作流的 ChatGPT skills 仓库，聚焦论文阅读、综述写作、arXiv 监控、飞书速递、审稿回复、实验总结、benchmark 抽取、research gap 分析，以及周报和组会材料生成。

仓库默认面向 AI / NLP / LLM / Agent / RAG / Safety 方向的研究生、科研工程师和实验型研究者。所有 skill 都采用统一目录结构、统一命名规则、统一元数据风格，便于本地维护、批量打包、上传到 ChatGPT Skills，以及后续在 GitHub 上协作迭代。

## 仓库包含的 skill

| skill | 主要定位 | 典型输入 | 典型输出 |
| --- | --- | --- | --- |
| `paper-deep-note` | 单篇论文精读沉淀 | PDF、arXiv 链接、标题摘要、正文片段 | 中文精读卡 |
| `survey-writer` | 多篇论文综述草稿组织 | 主题、论文列表、摘要、相关工作 | 简版 / 长版综述 |
| `paper-feishu-digest` | arXiv 监控与飞书速递 | 类别、时间窗口、关键词、webhook | 中文速递、Markdown、JSON、飞书推送 |
| `review-rebuttal` | 审稿意见拆分与 rebuttal 草稿 | reviews、meta-review、摘要、补充实验信息 | concern 分析、回复策略、rebuttal 草稿 |
| `experiment-log-summarizer` | 实验记录整理 | 训练日志、参数、结果、备注 | 中文实验总结、错误分析、周报摘要 |
| `benchmark-extractor` | benchmark 结构化抽取 | PDF、摘要、论文链接 | 中文说明版、结构化表格版 |
| `research-gap-finder` | 研究空白与切入点分析 | 研究主题、论文集合、已有想法 | gap 分析、小问题切入建议 |
| `weekly-lab-update` | 周报与组会材料生成 | 论文阅读、实验结果、问题、计划 | 中文周报、中文组会提纲、英文简报 |

更详细的定位见 [skills-overview.md](/D:/lunwen/academic-skills/skills-overview.md)。

## 目录结构

```text
academic-skills/
  README.md
  LICENSE
  .gitignore
  skills-overview.md
  tools/
    package_all_skills.py
    validate_repo_structure.py
  paper-deep-note/
  survey-writer/
  paper-feishu-digest/
  review-rebuttal/
  experiment-log-summarizer/
  benchmark-extractor/
  research-gap-finder/
  weekly-lab-update/
```

每个 skill 至少包含：

- `SKILL.md`
- `agents/openai.yaml`

按需要补充：

- `references/`：模板、分类法、写作规范、输出结构
- `scripts/`：只放需要确定性执行的脚本
- `assets/`：当前仓库未预置，后续确有必要再添加

## 统一规范

- skill 目录名全部使用小写和连字符。
- `SKILL.md` frontmatter 只保留 `name` 和 `description`。
- frontmatter 中 `name` 和 `description` 一律 lowercase。
- 默认输出语言为中文，除非 skill 明确提供英文模式。
- 不得假装读过用户未提供的全文，不得编造实验、数据集、结果或审稿背景。
- `SKILL.md` 保持短而清晰，详细模板与判断标准放进 `references/`。
- 脚本优先使用 Python 标准库。

## 本地查看、编辑与校验

建议使用 Python 3.10+。

1. 查看仓库结构

```powershell
Get-ChildItem -Recurse
```

2. 校验仓库结构

```powershell
python tools\validate_repo_structure.py
```

3. 预览批量打包结果

```powershell
python tools\package_all_skills.py --dry-run
```

4. 实际打包 skill

```powershell
python tools\package_all_skills.py
```

5. 查看 arXiv digest 脚本帮助

```powershell
python paper-feishu-digest\scripts\arxiv_digest.py --help
```

## 如何打包并上传到 ChatGPT Skills

推荐流程：

1. 先运行结构校验，确保每个 skill 目录至少包含 `SKILL.md` 和 `agents/openai.yaml`。
2. 运行 `python tools\package_all_skills.py`，在 `dist/` 下生成每个 skill 的 zip 包。
3. 检查 zip 内部目录结构是否正确，确认没有临时文件、缓存文件或编辑器垃圾文件。
4. 按 ChatGPT Skills 的上传流程，逐个上传对应 zip 包。
5. 如果只更新单个 skill，也可以单独对对应目录打包。

注意：

- 上传前优先检查 `SKILL.md` frontmatter 是否仍保持 lowercase。
- 如果某个 skill 新增了脚本，确认脚本使用说明已经写进该 skill 的 `SKILL.md` 或 `references/`。
- 如果某个 skill 需要联网或 webhook，上传说明里应明确输入要求和限制。

## 如何在 GitHub 上协作维护

推荐协作方式：

1. 为每个 skill 的更新建立独立分支。
2. 先改 `references/`，再改 `SKILL.md`，最后再补脚本或工具。
3. 在 PR 中说明：
   - 改了哪个 skill
   - 改了哪类工作流
   - 是否影响输出模板
   - 是否新增脚本或外部依赖
4. 合并前至少运行：
   - `python tools\validate_repo_structure.py`
   - `python tools\package_all_skills.py --dry-run`

## GitHub 初始化与首次推送

在仓库根目录执行：

```powershell
git init
git add .
git commit -m "feat: initialize academic skills repository"
git branch -M main
git remote add origin https://github.com/<your-account>/academic-skills.git
git push -u origin main
```

如果你已经在 GitHub 上创建了空仓库，只需要把 `<your-account>` 替换成你的账号名。

## 依赖说明

本仓库默认不依赖第三方 Python 包。`paper-feishu-digest/scripts/arxiv_digest.py`、`tools/package_all_skills.py`、`tools/validate_repo_structure.py` 都只使用 Python 标准库。

## 推荐先看哪些文件

如果你第一次接手这个仓库，建议先看：

- [skills-overview.md](/D:/lunwen/academic-skills/skills-overview.md)
- [tools/validate_repo_structure.py](/D:/lunwen/academic-skills/tools/validate_repo_structure.py)
- [paper-deep-note/SKILL.md](/D:/lunwen/academic-skills/paper-deep-note/SKILL.md)
- [paper-feishu-digest/scripts/arxiv_digest.py](/D:/lunwen/academic-skills/paper-feishu-digest/scripts/arxiv_digest.py)
