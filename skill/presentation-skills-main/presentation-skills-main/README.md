# presentation-skills

[中文版说明](README.zh.md)

**TL;DR.** `presentation-skills` is a collection of production-grade skills for making the artifacts people actually hand over: polished PowerPoint decks, formal Word documents, and publishable demo videos.

| Skill | Best For | Demo Signal |
| --- | --- | --- |
| `ppt-polished-deck-collab` | Editable executive decks, strategy narratives, technical explainers, research talks, formal Chinese research reports | 11-page Apple FY2025 financial report review deck with native charts, native tables, preview export, and validation evidence |
| `word-polished-doc-collab` | Formal reports, board attachments, research appendices, policy docs, consulting-style Word deliverables | Lightweight Chinese report plus refined English consulting report with preview and QA bundle |
| `web-demo-video-synthesis` | Product walkthroughs, narrated web demos, short-form explainers, publishable demo videos | End-to-end webpage, voiceover, subtitles, screen recording, and final MP4 pipeline |
| `xhs-markdown-card-collab` | Publishable Xiaohongshu image-card posts from Markdown, research/job posts, structured note-style social content | Demo bundles with PNG cards, preview HTML, metadata JSON, and theme variation under a locked typography contract |

`presentation-skills` is an open-source repository of high-quality, commercial-grade presentation tools for agent and assistant environments. The goal is reusable workflows that consistently produce polished, editable, validated deliverables close to real business delivery standards.

These skills were not produced in one pass. They were iterated through many real runs, repeated failure analysis, output review, and workflow rewrites. A large amount of paid model tokens was spent to make the workflows, validation gates, and deliverables actually hold up in practice.

## Demo Gallery

| PowerPoint research report | PowerPoint strategy deck |
| --- | --- |
| [![Apple FY2025 financial report review contact sheet](assets/apple-financial-report-review_contact-sheet.png)](demos/apple-financial-report-review/README.md) | [![Standard Wars executive deck contact sheet](assets/standard-wars-executive-deck_contact-sheet.png)](old/demos/standard-wars-executive-deck/README.md) |
| Current flagship `ppt-polished-deck-collab` demo: a formal financial-report review deck with native charts, native tables, and validation evidence. | Archived but still useful `ppt-polished-deck-collab` demo: a strategy narrative deck with diagrams, comparison matrices, and management questions. |

[![Word refined consulting-report demo spread](assets/word-refined-industrial-service-transformation_spread.png)](demos/word-refined-industrial-service-transformation/README.md)

[![Web Demo Video Synthesis preview](demos/web-demo-video-synthesis-financial-agent/assets/preview_en.png)](demos/web-demo-video-synthesis-financial-agent/README.md)

## Prompt Example

![Prompt example for the Apple financial report review deck](assets/ppt-prompt-example.jpg)

This prompt style is intentionally specific about workspace placement, source data, reference style, disclosure language, and the `ppt-polished-deck-collab` skill route. The Apple demo turns that kind of request into a reproducible research-report workspace rather than a one-off presentation file.

## Recent Updates

- `2026-05-10` Kept the archived Standard Wars executive deck visible in the README as a second `ppt-polished-deck-collab` example, with a new contact-sheet asset linked to the archived workspace.
- `2026-05-10` Replaced the flagship `ppt-polished-deck-collab` demo with an Apple FY2025 financial report review deck, including SEC-derived data, editable Office charts, native tables, preview exports, and validation reports.
- `2026-05-10` Added a Chinese formal-report typography default for `ppt-polished-deck-collab`: SimSun for Chinese, Times New Roman for English, `12pt` body text, first-line indent, `0.5` line paragraph spacing, `1.5` line body spacing, and financial-table alignment rules.
- `2026-04-22` `ppt-polished-deck-collab` now supports automatic quality gates for mobile-open risk, text overflow, object occlusion, and preview-layer layout failures, which materially reduces manual cleanup before delivery.
- `2026-04-22` `ppt-polished-deck-collab` also tightened its template-first workflow, so reference template audit, editable deck build, validation, preview export, and final review happen in a fixed order.
- `2026-04-29` Added `word-polished-doc-collab`, which turns Markdown, DOCX, and Python-generated document assets into a dedicated Word workflow with explicit Chinese-English font profiles, heading scale, caption placement, and quality gates.
- `2026-04-30` Registered two polished `word-polished-doc-collab` demos under `demos/`: a rich lightweight Chinese formal-report sample and a refined English consulting-report sample with full preview and QA evidence.
- `2026-05-04` Added `xhs-markdown-card-collab`, which turns Markdown into publishable Xiaohongshu image cards through explicit cover front matter, browser-based pagination, locked typography contracts, and style-direction guidance that avoids repetitive “AI card” convergence.
- `2026-05-05` Upgraded the XHS fictional demo set from source-only examples into actual exported demo bundles under `demos/`, each with rendered PNG cards, preview HTML, metadata JSON, and a documented theme assignment.

## What This Repo Provides

### `ppt-polished-deck-collab`

`ppt-polished-deck-collab` produces editable, high-quality, highly automated PowerPoint decks for both business and academic use. It can build a new deck from scratch, work from a user-provided template, inherit a user’s existing slide master and layouts, and modify an existing `pptx` while preserving editability.

It is designed for strategy decks, technical explainers, research talks, thesis defenses, product presentations, operations reviews, management decks, and other presentation-heavy workflows where the final artifact must still behave like a real PowerPoint file.

### `word-polished-doc-collab`

`word-polished-doc-collab` turns Markdown, DOCX, and Python-generated document assets into formal Word deliverables that can survive real review. It focuses on explicit Chinese-English font pairing, heading scale, line spacing, paragraph spacing, table and figure title placement, and delivery evidence instead of one-off DOCX export.

It is designed for contracts, policies, explanatory notes, research appendices, operating reports, board or investment committee attachments, and other Word-first workflows where the content source must remain maintainable after delivery.

### `web-demo-video-synthesis`

`web-demo-video-synthesis` produces narrated, subtitled, publishable videos in a highly automated way. It can turn articles, posts, product walkthroughs, web demos, and technical explanations into videos suitable for platforms such as TikTok, Xiaohongshu, and Bilibili.

It is designed for technical introductions, business demos, product explainers, marketing-style walkthroughs, and other short-form or medium-form presentation videos where reproducibility and iteration speed matter.

### `xhs-markdown-card-collab`

`xhs-markdown-card-collab` turns Markdown or lightly structured text into publishable Xiaohongshu image-card posts. It focuses on explicit cover metadata, stable Chinese typography, browser-based pagination, visual QA, and style variation without re-breaking proven type-size ranges.

It is designed for job posts, lab recruiting posts, research-note threads, structured commentary cards, product explainers, and other social content where the output must still read cleanly on a phone rather than merely “fit into a PNG”.

## Skill Details

### `ppt-polished-deck-collab`

This is the flagship deck-making skill in the repository. It is a deck-level workflow rather than a page toy. It plans the narrative, generates editable `pptx`, exports previews, validates structure, and produces evidence bundles for review and handoff.

Core capabilities:
- Deck-first narrative planning with `brief.md`, `deck_narrative.md`, and derived `slide_specs.yaml`
- Editable PowerPoint generation with `python-pptx`
- Support for user-provided templates, slide masters, layouts, and existing `pptx` modification
- Native Office charts, Python figures, native tables, connector-backed diagrams, and icon accents
- Template audit plus three-stage quality gates: `package_preflight`, `structure_precheck`, and `render_review`
- Validation bundles, preview exports, and evidence-driven final delivery

Typical technical stack:
- `python-pptx` for editable PowerPoint objects
- PowerPoint or LibreOffice preview export
- Connector validation via `pptx XML`
- Structure-level and render-level quality gates
- Optional Python figure generation via `matplotlib` / `seaborn` / `pandas`

Typical workflow:
- Audit template if one is provided
- Lock brief and narrative
- Build editable deck
- Run package and structure gates
- Run module validation
- Export previews
- Run render review
- Finish with visual review and final handoff

Featured deck examples:
- Current research-report demo: `demos/apple-financial-report-review/`
- Archived strategy-deck demo: `old/demos/standard-wars-executive-deck/`

Key outputs:
- `demos/apple-financial-report-review/final/apple_fy2025_financial_report_review.pptx`
- `demos/apple-financial-report-review/final/apple_fy2025_financial_report_review.pdf`
- `demos/apple-financial-report-review/build/rendered/contact_sheet.png`
- `demos/apple-financial-report-review/validation/package_preflight/history/`
- `demos/apple-financial-report-review/validation/structure_precheck/history/`
- `demos/apple-financial-report-review/validation/render_review/history/`

[![Apple FY2025 revenue and net-income page](assets/apple-financial-report-review_revenue-page.png)](demos/apple-financial-report-review/README.md)

[![Standard Wars executive deck contact sheet](assets/standard-wars-executive-deck_contact-sheet.png)](old/demos/standard-wars-executive-deck/README.md)

### `word-polished-doc-collab`

This is the repository’s Word-document collaboration skill. It turns a loose Markdown or DOCX drafting process into a disciplined document workspace: semantic source, explicit typography, stable captions, preview evidence, and QA reports that make the final `.docx` easier to trust.

Core capabilities:
- Mode-aware routing for `lightweight` and `refined` document workflows
- Reference CLI bundle with `init_doc_workspace.py`, `check_word_environment.py`, `lint_doc_markdown.py`, `build_docx.py`, `export_docx_preview.py`, and `run_docx_qa.py`
- Support for both `docx -> markdown -> docx` and `markdown -> docx`
- Explicit default typography for `Chinese SimSun + English Times New Roman`, plus optional `KaiTi + Times New Roman`, `HeiTi + Arial`, and generic English consulting presets
- Fixed rules for body text `12pt`, heading and body line spacing `1.5`, paragraph spacing `0.5` lines, table text `10.5pt / 9pt`, table-title bolding, and caption placement
- Asset routing for static images, Python figures, and future Office-native objects
- Quality gates for source integrity, style contract, font-slot integrity, section layout, asset manifest integrity, and visual review

Typical workflow:
- Choose `lightweight` or `refined` based on formality, chart density, and validation needs
- Initialize a clean workspace
- Lock semantic Markdown and the active `style_profile`
- Lint the source before build
- Build the `.docx`, export the preview bundle, and run QA when required
- Finish with a visual review note and handoff-ready evidence

Featured demos:
- `demos/word-lightweight-industrial-operations-brief/`
- `demos/word-refined-industrial-service-transformation/`

Key outputs:
- `demos/word-lightweight-industrial-operations-brief/out/industrial_operations_brief.docx`
- `demos/word-lightweight-industrial-operations-brief/out/preview/industrial_operations_brief.pdf`
- `demos/word-refined-industrial-service-transformation/build/docx/industrial_service_transformation.docx`
- `demos/word-refined-industrial-service-transformation/temp/qa/qa_report.md`

Key docs:
- `word-polished-doc-collab/SKILL.md`
- `word-polished-doc-collab/references/principles.md`
- `word-polished-doc-collab/references/doc_workflow.md`
- `word-polished-doc-collab/references/typography_profiles.md`
- `word-polished-doc-collab/references/local_pipeline_case_study.md`

### `web-demo-video-synthesis`

This is the flagship video-making skill in the repository. It turns a source narrative into a reproducible workspace for TTS, timing, subtitles, recording, mixing, and final rendering. The result is not a one-off export. The result is a workspace that can be reviewed, edited, rerun, and published.

Core capabilities:
- Turn cues, articles, or posts into timeline-driven demo videos
- Generate or integrate segment audio, subtitles, and final rendering
- Preserve a reproducible workspace for iteration and partial reruns
- Target platform-ready outputs for TikTok, Xiaohongshu, Bilibili, and similar channels

Typical technical stack:
- Timeline-driven workspace orchestration
- TTS and subtitle generation
- Screen recording and video compositing
- Final MP4 rendering with reproducible intermediate assets

Typical workflow:
- Prepare workspace and cues
- Generate segment audio
- Build timeline
- Record or synthesize visual track
- Generate subtitles
- Mix audio and video
- Export final MP4

Featured demo:
- `demos/web-demo-video-synthesis-financial-agent/`

Public demo video:
- Bilibili: https://www.bilibili.com/video/BV1j6NwzaEDZ/

### `xhs-markdown-card-collab`

This is the repository’s Xiaohongshu image-card workflow skill. It treats content cleanup, cover planning, typography control, browser pagination, and image review as one workflow instead of as separate ad hoc styling steps.

Core capabilities:
- Explicit YAML front matter for cover title, role line, badges, and highlights
- Markdown cleanup that prefers semantic headings, standard lists, and light emphasis over rewriting the source
- Browser-based pagination for Chinese text, lists, and mixed English strings
- Locked typography guidance with validated size bands for cover, body, spacing, and frame width
- Style-direction guidance to vary tone, layout, and theme without collapsing into repetitive AI-looking cards
- Visual QA rules for cover density, orphan headings, over-wide borders, empty pages, and mobile readability

Key docs:
- `xhs-markdown-card-collab/SKILL.md`
- `xhs-markdown-card-collab/references/workflow.md`
- `xhs-markdown-card-collab/references/typography_lock.md`
- `xhs-markdown-card-collab/references/style_directions.md`

## Repository Layout

- `ppt-polished-deck-collab/`: active polished-deck skill
- `word-polished-doc-collab/`: active Word-document collaboration skill
- `web-demo-video-synthesis/`: active web-demo-to-video skill
- `xhs-markdown-card-collab/`: active Xiaohongshu Markdown-card skill
- `demos/`: registered demo workspaces
- `old/`: archived skills and historical demos
- `assets/`: root-level preview assets used by the repository README

## Demos

- Registered polished deck demo: `demos/apple-financial-report-review/`
- Registered Word lightweight demo: `demos/word-lightweight-industrial-operations-brief/`
- Registered Word refined demo: `demos/word-refined-industrial-service-transformation/`
- Registered web demo synthesis demo: `demos/web-demo-video-synthesis-financial-agent/`
- Registered XHS recruiting-style demo: `demos/xhs-fictional-north-quay-lab-recruiting/`
- Registered XHS research-note demo: `demos/xhs-fictional-grid-storage-research-note/`
- Registered XHS product-explainer demo: `demos/xhs-fictional-orbitops-product-explainer/`
- Registered XHS weekly-brief demo: `demos/xhs-fictional-ridership-weekly-brief/`
- Archived complex diagram demo: `old/demos/ppt-complex-diagram-collab-stock-architecture/`
- Archived polished deck demo: `old/demos/ppt-polished-deck-collab-ai-market-intelligence/`
- Archived polished deck demo: `old/demos/standard-wars-executive-deck/`

## XHS Demo Set

The `xhs-markdown-card-collab` skill now includes four fully fictional demos under `demos/` with actual exported deliverables, so the workflow can be understood without relying on any real recruiting, research, or product copy:

- `demos/xhs-fictional-north-quay-lab-recruiting/`: institution recruiting / lab intake style, exported with `lumen`
- `demos/xhs-fictional-grid-storage-research-note/`: research-summary / framework-note style, exported with `ink`
- `demos/xhs-fictional-orbitops-product-explainer/`: product-explainer / capability-card style, exported with `clay`
- `demos/xhs-fictional-ridership-weekly-brief/`: weekly-brief / data-quick-take style, exported with `ink`
