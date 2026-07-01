# 期刊论文 PDF 翻译与 LaTeX 重建任务提示词

你现在需要完成一个“期刊论文 PDF 翻译 + LaTeX 项目重建”任务。请严格按照以下要求执行，最终输出一个可以直接上传到 Overleaf 并正常编译的完整 LaTeX 项目。

---

## 一、任务目标

我会提供一篇英文期刊论文 PDF 文件。你的任务是：

1. 读取并解析该 PDF 论文的完整内容；
2. 将论文正文完整翻译为中文；
3. 保留原论文的学术结构、章节层级、公式编号、图表编号、引用编号和逻辑顺序；
4. 将翻译后的内容重建为 LaTeX 格式；
5. 从原 PDF 中提取所有必要图片、图示、框架图、流程图、实验结果图等；
6. 将提取出的图片正确插入 LaTeX 文件；
7. 对表格进行 LaTeX 重建，优先使用可编辑表格，而不是截图；
8. 保证最终项目能够在 Overleaf 中正常打开、正常渲染、正常编译；
9. 最终输出完整项目文件夹，包含 `.tex`、`.bib`、图片文件、样式文件以及必要说明文档。

---

## 二、核心原则

请遵循以下原则：

1. **忠实翻译优先**  
   不要擅自改写作者观点，不要添加原文没有的结论，不要删除重要内容。

2. **学术表达优先**  
   中文翻译应符合中文期刊论文表达习惯，保持严谨、客观、正式。

3. **LaTeX 可编译优先**  
   所有 LaTeX 内容必须保证语法正确，能够在 Overleaf 中使用 XeLaTeX 或 LuaLaTeX 正常编译。

4. **图表完整优先**  
   论文中的图、表、公式、算法伪代码、符号说明、实验结果图不能遗漏。

5. **结构对应优先**  
   翻译后的论文结构应尽量与原论文保持一致，包括：
   - 标题
   - 摘要
   - 关键词
   - 引言
   - 相关工作
   - 方法
   - 实验
   - 结果分析
   - 消融实验
   - 讨论
   - 结论
   - 致谢
   - 参考文献
   - 附录

6. **不要过度美化**  
   目标不是重新设计论文，而是准确翻译和 LaTeX 化重建。

---

## 三、输入文件

输入文件包括：

```text
paper.pdf
```

如果论文中存在补充材料、附录、数据说明或额外图表，也需要一并处理。

---

## 四、输出项目结构

请最终生成如下结构的 LaTeX 项目：

```text
translated_paper_latex/
├── main.tex
├── references.bib
├── figures/
│   ├── fig1.png
│   ├── fig2.png
│   ├── fig3.png
│   └── ...
├── tables/
│   └── optional_table_notes.md
├── sections/
│   ├── 00_abstract.tex
│   ├── 01_introduction.tex
│   ├── 02_related_work.tex
│   ├── 03_method.tex
│   ├── 04_experiments.tex
│   ├── 05_results.tex
│   ├── 06_discussion.tex
│   ├── 07_conclusion.tex
│   └── appendix.tex
├── compile_notes.md
└── README.md
```

如果论文较短，也可以只使用一个 `main.tex` 文件，但必须保证结构清晰、可维护、可编译。

---

## 五、LaTeX 编译要求

请使用适合中文论文排版的 LaTeX 配置。

推荐使用：

```latex
\documentclass[UTF8,a4paper,12pt]{ctexart}
```

或：

```latex
\documentclass[UTF8,a4paper,12pt]{ctexrep}
```

必须使用中文兼容方案，例如：

```latex
\usepackage{ctex}
\usepackage{fontspec}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{float}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{multirow}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{bm}
\usepackage{algorithm}
\usepackage{algorithmic}
\usepackage{caption}
\usepackage{subcaption}
\usepackage{hyperref}
\usepackage{url}
\usepackage[numbers,sort&compress]{natbib}
```

页面设置建议：

```latex
\geometry{left=2.5cm,right=2.5cm,top=2.8cm,bottom=2.8cm}
```

图片路径设置：

```latex
\graphicspath{{figures/}}
```

超链接设置：

```latex
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    citecolor=blue,
    urlcolor=blue
}
```

编译方式要求：

```text
Compiler: XeLaTeX
Bibliography: BibTeX 或 biber
```

最终必须在 `compile_notes.md` 中说明推荐编译方式。

---

## 六、翻译要求

### 1. 标题翻译

保留英文标题，并给出中文标题。

格式示例：

```latex
\title{
英文原题目\\
\large 中文翻译题目
}
```

### 2. 摘要翻译

摘要需要完整翻译，保持原文逻辑，不要压缩。

格式示例：

```latex
\begin{abstract}
这里放中文摘要翻译内容。
\end{abstract}
```

如果原文有英文摘要，可在中文摘要后保留英文摘要：

```latex
\begin{abstract}
中文摘要内容。
\end{abstract}

\begin{abstract}
Original English abstract.
\end{abstract}
```

### 3. 关键词翻译

格式示例：

```latex
\noindent\textbf{关键词：} 多源信息融合；轨迹预测；无人机集群；深度学习；不完整观测
```

### 4. 正文翻译

正文翻译要求：

- 保持原文段落顺序；
- 保持章节标题编号；
- 保持图表引用关系；
- 保持公式前后解释；
- 保留所有专业术语；
- 第一次出现的关键术语可以采用“中文译名（English Term）”形式；
- 不要删除作者原有的限定语、假设、条件和实验说明。

示例：

```latex
\section{引言}

近年来，随着无人系统、传感器网络和多源信息融合技术的发展，轨迹预测任务在智能交通、无人机协同控制和机器人导航等领域中受到了广泛关注。
```

---

## 七、术语翻译要求

请建立统一术语表，保证全文翻译一致。

在 `README.md` 或 `compile_notes.md` 中给出术语对照表，例如：

```markdown
| English Term | 中文译名 |
|---|---|
| trajectory prediction | 轨迹预测 |
| multi-source information fusion | 多源信息融合 |
| incomplete observation | 不完整观测 |
| heterogeneous UAV swarm | 异构无人机集群 |
| attention mechanism | 注意力机制 |
```

如果遇到难以确定的术语，不要随意翻译，应采用：

```text
中文译名（英文原词）
```

---

## 八、公式处理要求

### 1. 所有公式必须使用 LaTeX 重建

不要把公式截图插入正文，除非公式极其复杂且无法识别。

行间公式格式：

```latex
\begin{equation}
    y = f(x; \theta)
    \label{eq:model}
\end{equation}
```

多行公式格式：

```latex
\begin{align}
    h_t &= \sigma(W_x x_t + W_h h_{t-1} + b), \\
    y_t &= W_y h_t + b_y.
    \label{eq:recurrent}
\end{align}
```

### 2. 公式编号

如果原论文有公式编号，应尽量保持一致。

例如原文为 Equation (3)，重建时应使用：

```latex
\label{eq:original_3}
```

正文中引用：

```latex
如式~\eqref{eq:original_3} 所示。
```

### 3. 变量解释

公式后的变量说明必须完整翻译。

示例：

```latex
其中，$x_t$ 表示时刻 $t$ 的输入特征，$h_t$ 表示隐藏状态，$\theta$ 表示模型参数集合。
```

### 4. 数学符号

数学符号不翻译，例如：

```latex
$x_i$、$\theta$、$\mathcal{G}$、$\mathbf{A}$、$\mathbb{R}^d$
```

---

## 九、图片提取与插入要求

### 1. 图片提取

请从 PDF 中提取所有正文中实际使用的图，包括：

- 方法框架图；
- 模型结构图；
- 流程图；
- 数据集示意图；
- 实验结果图；
- 消融实验图；
- 可视化结果图；
- 附录图。

图片应保存到：

```text
figures/
```

命名规则：

```text
fig1.png
fig2.png
fig3.png
...
```

如果原图质量较高，优先保存为：

```text
.pdf
```

或：

```text
.png
```

不建议使用低清晰度 JPG。

### 2. 图片裁剪

提取图片时，应尽量裁剪掉页眉、页脚、正文文字和多余空白，只保留图本体和必要图例。

如果图中包含多个子图，例如：

```text
Figure 3(a), Figure 3(b), Figure 3(c)
```

可以整体保存为一个图，也可以拆分为多个子图。若拆分，需要使用 `subfigure` 或 `subcaption` 插入。

### 3. 图片插入格式

普通图片：

```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.85\textwidth]{figures/fig1.png}
    \caption{模型整体框架示意图}
    \label{fig:framework}
\end{figure}
```

多子图：

```latex
\begin{figure}[H]
    \centering
    \begin{subfigure}{0.48\textwidth}
        \centering
        \includegraphics[width=\textwidth]{figures/fig3a.png}
        \caption{子图 A}
        \label{fig:sub_a}
    \end{subfigure}
    \hfill
    \begin{subfigure}{0.48\textwidth}
        \centering
        \includegraphics[width=\textwidth]{figures/fig3b.png}
        \caption{子图 B}
        \label{fig:sub_b}
    \end{subfigure}
    \caption{实验结果对比图}
    \label{fig:results}
\end{figure}
```

### 4. 图题翻译

图题必须翻译为中文，同时可以保留英文原图题。

推荐格式：

```latex
\caption{模型整体框架。原文图题：Overall framework of the proposed model.}
```

如果图题太长，可以只保留中文翻译，但需要在 `compile_notes.md` 中说明。

### 5. 图片引用

正文中所有图片引用必须同步修改，例如：

```latex
如图~\ref{fig:framework} 所示，该模型由编码器、融合模块和预测模块组成。
```

---

## 十、表格处理要求

### 1. 表格优先重建为 LaTeX

不要直接截图插入表格，除非表格过于复杂无法可靠识别。

普通表格格式：

```latex
\begin{table}[H]
    \centering
    \caption{不同模型的性能比较}
    \label{tab:comparison}
    \begin{tabular}{lccc}
        \toprule
        方法 & ADE & FDE & RMSE \\
        \midrule
        Model A & 0.42 & 0.81 & 0.56 \\
        Model B & 0.39 & 0.74 & 0.51 \\
        Proposed & 0.31 & 0.62 & 0.44 \\
        \bottomrule
    \end{tabular}
\end{table}
```

### 2. 长表格

如果表格跨页，使用：

```latex
\begin{longtable}{lccc}
...
\end{longtable}
```

### 3. 表题翻译

表题需要翻译为中文：

```latex
\caption{不同基线模型在各数据集上的预测性能比较}
```

### 4. 数值保持一致

所有实验结果数值必须与原文一致，不允许擅自修改。

如果 PDF 识别数值存在不确定，应在 `compile_notes.md` 中标注。

---

## 十一、算法伪代码处理要求

如果论文中包含算法框、伪代码或流程说明，需要使用 LaTeX 重建。

示例：

```latex
\begin{algorithm}[H]
\caption{所提出方法的训练过程}
\label{alg:training}
\begin{algorithmic}[1]
\STATE 初始化模型参数 $\theta$
\FOR{每一个训练轮次}
    \STATE 从训练集中采样一个小批量数据
    \STATE 计算预测结果 $\hat{Y}$
    \STATE 根据损失函数更新参数 $\theta$
\ENDFOR
\RETURN 训练后的模型
\end{algorithmic}
\end{algorithm}
```

如果原文算法步骤为英文，翻译为中文，但变量名、函数名和符号保持不变。

---

## 十二、参考文献处理要求

### 1. 优先构建 BibTeX

将参考文献整理到：

```text
references.bib
```

格式示例：

```bibtex
@article{vaswani2017attention,
  title={Attention Is All You Need},
  author={Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit, Jakob},
  journal={Advances in Neural Information Processing Systems},
  year={2017}
}
```

### 2. 文中引用

正文引用使用：

```latex
\citep{vaswani2017attention}
```

或：

```latex
\citet{vaswani2017attention}
```

如果无法准确恢复 BibTeX key，可以使用顺序 key：

```bibtex
@article{ref1,
  ...
}
```

正文中使用：

```latex
\citep{ref1}
```

### 3. 参考文献完整性

参考文献至少应包含：

- 作者；
- 标题；
- 期刊或会议；
- 年份；
- 卷期页码；
- DOI，如果原文提供。

如果部分字段无法识别，应保留能识别出的字段，并在 `compile_notes.md` 中说明。

---

## 十三、主文件 main.tex 要求

`main.tex` 应包含完整可编译结构，例如：

```latex
\documentclass[UTF8,a4paper,12pt]{ctexart}

\usepackage{ctex}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{float}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{multirow}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{bm}
\usepackage{algorithm}
\usepackage{algorithmic}
\usepackage{caption}
\usepackage{subcaption}
\usepackage{hyperref}
\usepackage[numbers,sort&compress]{natbib}

\geometry{left=2.5cm,right=2.5cm,top=2.8cm,bottom=2.8cm}
\graphicspath{{figures/}}

\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    citecolor=blue,
    urlcolor=blue
}

\title{英文原题目\\\large 中文翻译题目}
\author{原作者信息}
\date{}

\begin{document}

\maketitle

\input{sections/00_abstract}
\input{sections/01_introduction}
\input{sections/02_related_work}
\input{sections/03_method}
\input{sections/04_experiments}
\input{sections/05_results}
\input{sections/06_discussion}
\input{sections/07_conclusion}

\bibliographystyle{plainnat}
\bibliography{references}

\appendix
\input{sections/appendix}

\end{document}
```

如果不拆分章节，也可以将所有内容直接写入 `main.tex`，但需要保证结构清晰。

---

## 十四、README.md 要求

请生成 `README.md`，内容包括：

```markdown
# 中文翻译版 LaTeX 项目说明

## 文件说明

- `main.tex`：主 LaTeX 文件
- `references.bib`：参考文献文件
- `figures/`：从原 PDF 中提取的图片
- `sections/`：各章节 LaTeX 文件
- `compile_notes.md`：编译说明与问题记录

## 编译方式

推荐使用 Overleaf，编译器选择：

- XeLaTeX

编译顺序：

1. XeLaTeX
2. BibTeX
3. XeLaTeX
4. XeLaTeX

## 注意事项

如果参考文献未正确显示，请重新运行 BibTeX 或切换 Overleaf 的编译器为 XeLaTeX。
```

---

## 十五、compile_notes.md 要求

请生成 `compile_notes.md`，记录以下内容：

1. 原论文 PDF 文件名；
2. 翻译处理日期；
3. 使用的 LaTeX 编译器；
4. 图片提取数量；
5. 表格重建数量；
6. 公式重建数量；
7. 无法完全确认的内容；
8. PDF 识别存在歧义的位置；
9. 是否存在低清晰度图片；
10. Overleaf 编译注意事项。

示例：

```markdown
# 编译与处理说明

## 推荐编译器

XeLaTeX

## 图片处理

共提取图片 8 张，保存于 `figures/` 文件夹。

## 表格处理

共重建表格 5 个，均采用 LaTeX tabular 环境。

## 公式处理

共重建公式 23 个，公式编号尽量与原文保持一致。

## 不确定项

- 第 7 页表 2 中部分数值由于 PDF 清晰度较低，已根据上下文进行人工核对，但仍建议再次检查。
- 图 5 原图分辨率较低，已尽量裁剪并保留原始清晰度。
```

---

## 十六、质量检查要求

完成后必须进行以下检查：

### 1. 编译检查

确认 `main.tex` 可以正常编译。

如果不能编译，需要修复错误，包括但不限于：

- 中文字体错误；
- 图片路径错误；
- 表格环境错误；
- 数学公式语法错误；
- 引用 key 不存在；
- 特殊字符未转义；
- 下划线 `_` 未处理；
- 百分号 `%` 未转义；
- `&` 未转义；
- 图片文件名含空格或特殊字符。

### 2. 图表检查

确认：

- 所有正文提到的图都存在；
- 所有图都能正常显示；
- 所有图题已翻译；
- 所有图编号与正文引用一致；
- 所有表格都能正常显示；
- 表格未超出版心；
- 长表格可以跨页显示。

### 3. 公式检查

确认：

- 所有公式均为 LaTeX 公式；
- 所有公式可以正常渲染；
- 公式编号和引用正确；
- 变量说明没有遗漏；
- 没有把普通正文错误放入数学环境。

### 4. 参考文献检查

确认：

- 文中引用可以跳转；
- `references.bib` 中存在对应条目；
- 参考文献列表能够正常生成；
- 没有未定义引用。

### 5. 中文排版检查

确认：

- 中文能够正常显示；
- 英文专业术语与中文之间排版自然；
- 数学符号前后间距合理；
- 没有乱码；
- 没有 PDF 解析产生的断行错误；
- 没有重复页眉、页脚或脚注残留。

---

## 十七、常见错误处理要求

请特别避免以下错误：

1. 不要把整页 PDF 截图当作正文；
2. 不要遗漏图片；
3. 不要把公式截图插入正文；
4. 不要丢失参考文献；
5. 不要将图题、表题漏翻译；
6. 不要让图片路径出现中文、空格或特殊字符；
7. 不要使用 Overleaf 不支持或不稳定的本地字体；
8. 不要让表格超出页面；
9. 不要让中文在 pdfLaTeX 下乱码；
10. 不要生成无法编译的 LaTeX 文件；
11. 不要将原文 OCR 错误直接带入译文；
12. 不要随意压缩或概括原论文内容。

---

## 十八、特殊字符处理要求

LaTeX 中以下字符需要正确转义：

```text
_  → \_
%  → \%
&  → \&
#  → \#
$  → \$
{  → \{
}  → \}
```

但在数学公式环境中，应保留数学语法，不要错误转义。

例如：

```latex
$x_i$
```

不要写成：

```latex
$x\_i$
```

---

## 十九、图片文件命名要求

图片文件统一使用英文小写命名：

```text
fig1.png
fig2.png
fig3.png
fig4a.png
fig4b.png
framework.png
architecture.png
experiment_results.png
```

不要使用：

```text
图1.png
Figure 1 final version.png
模型结构图（修改版）.png
```

---

## 二十、最终交付物

最终需要交付：

```text
translated_paper_latex.zip
```

压缩包内必须包含：

```text
main.tex
references.bib
figures/
sections/
README.md
compile_notes.md
```

如果存在额外样式文件，也应一并包含。

---

## 二十一、最终回答格式

完成任务后，请按照以下格式回复：

```markdown
已完成论文翻译与 LaTeX 重建。

## 输出文件

- `translated_paper_latex.zip`

## 处理结果

- 已翻译正文：是
- 已重建公式：是
- 已提取图片：是
- 已重建表格：是
- 已整理参考文献：是
- Overleaf 编译检查：已完成 / 存在问题

## 编译方式

建议使用 XeLaTeX 编译。

## 需要人工复核的位置

1. 第 X 页图 X 的清晰度较低；
2. 第 X 页表 X 的部分数值需要人工确认；
3. 参考文献中第 X 条 DOI 缺失。
```

如果无法完成某一部分，必须明确说明原因，不允许假装完成。

---

## 二十二、建议执行顺序

为了降低错误率，建议按以下顺序执行：

1. **PDF 结构解析**  
   提取标题、摘要、章节、图表、公式、参考文献清单。

2. **图表清单核对**  
   列出论文中的全部图、表、算法、公式编号，确认没有遗漏。

3. **图片提取与裁剪**  
   从 PDF 中提取图片，统一命名并存入 `figures/` 文件夹。

4. **表格重建**  
   将表格优先转为 LaTeX 表格，复杂表格再考虑截图方式。

5. **公式重建**  
   使用 LaTeX 公式环境重建所有公式，并设置标签。

6. **正文翻译**  
   按章节翻译正文，保持术语一致。

7. **参考文献整理**  
   构建 `references.bib`，并保证正文引用 key 可用。

8. **主文件整合**  
   编写 `main.tex`，整合章节、图表、公式和参考文献。

9. **编译验证**  
   使用 XeLaTeX + BibTeX 进行编译检查，修复路径、引用、公式、表格错误。

10. **生成说明文档**  
    输出 `README.md` 和 `compile_notes.md`。

---

## 二十三、成功标准

只有满足以下条件，才认为任务完成：

1. `main.tex` 能够在 Overleaf 中打开；
2. 使用 XeLaTeX 能够正常编译；
3. 中文正文无乱码；
4. 图像能够正常显示；
5. 表格能够正常显示；
6. 公式能够正常渲染；
7. 文中引用、图表引用、公式引用基本可用；
8. 参考文献能够正常生成；
9. 文件结构清晰；
10. 所有不确定内容已在 `compile_notes.md` 中标注。
