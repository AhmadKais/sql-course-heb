#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""בונה את מדריך למורה.pdf מתוך exam-prep/teacher-guide/*.md
   הרצה:  python3 handouts/build/build-teacher-guide.py
"""
import re, subprocess, pathlib, sys, shutil

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC  = ROOT / "exam-prep" / "teacher-guide"
OUT  = ROOT / "handouts"
TMP  = OUT / "build" / ".tmp"
TMP.mkdir(parents=True, exist_ok=True)

FILES = ["README.md", "01-keys-and-relations.md", "02-select.md",
         "03-where.md", "04-order-by.md"]

# emoji -> plain markers (DejaVu has no colour emoji)
EMOJI = {
    "👩‍🏫": "", "🎯": "", "🧠": "", "❓": "", "🔘": "", "⏱️": "", "⏱": "",
    "⚠️": "", "⚠": "", "💡": "", "✅": "", "💪": "", "🟢": "", "🟡": "",
    "🔴": "", "📎": "", "🎬": "", "📘": "",
}

def preprocess(md: str) -> str:
    # collapsible answers -> a visible boxed environment
    md = re.sub(r'<details>\s*<summary>\s*(.*?)\s*</summary>',
                lambda m: '\n```{=latex}\n\\begin{answerbox}{' +
                          strip_emoji(m.group(1)).strip() + '}\n```\n',
                md, flags=re.S)
    md = md.replace('</details>', '\n```{=latex}\n\\end{answerbox}\n```\n')
    # the RTL wrappers are a GitHub-rendering device; LaTeX handles bidi itself
    md = md.replace('<div dir="rtl">', '').replace('</div>', '')
    return strip_emoji(md)

def strip_emoji(s: str) -> str:
    for k, v in EMOJI.items():
        s = s.replace(k, v)
    # any remaining pictographs (arrows U+2190-21FF are meaningful - keep them)
    return re.sub(r'[\U0001F000-\U0001FAFF\u2700-\u27BF\uFE0F\u200d]', '', s)

def main():
    if not shutil.which("pandoc"):
        sys.exit("pandoc not found")
    parts = []
    for i, name in enumerate(FILES):
        md = (SRC / name).read_text(encoding="utf-8")
        if i:                      # each topic starts a new page
            parts.append('\n```{=latex}\n\\newpage\n```\n')
        parts.append(preprocess(md))
    merged = TMP / "merged.md"
    merged.write_text("\n\n".join(parts), encoding="utf-8")

    body = TMP / "body.tex"
    subprocess.run(["pandoc", str(merged), "-f", "markdown+raw_attribute-smart",
                    "-t", "latex", "--no-highlight", "-o", str(body)], check=True)

    tex = body.read_text(encoding="utf-8")
    # pandoc writes em/en dashes as --- / -- ; those ligatures don't form in the
    # Hebrew font, so emit the commands explicitly - but never inside verbatim.
    _parts = re.split(r'(\\begin\{verbatim\}.*?\\end\{verbatim\})', tex, flags=re.S)
    for _i in range(0, len(_parts), 2):
        _parts[_i] = (_parts[_i].replace('---', '\\textemdash{}')
                                .replace('--', '\\textendash{}'))
    tex = ''.join(_parts)
    # verbatim must stay left-to-right inside an RTL document
    def _verb(m):
        inner = m.group(1)
        if not inner.startswith('\n'): inner = '\n' + inner
        if not inner.endswith('\n'):   inner = inner + '\n'
        return ('\\begin{otherlanguage}{english}%\n'
                '\\begin{Verbatim}[fontsize=\\small,frame=leftline,framerule=1.2pt,'
                'rulecolor=\\color{rulegray},framesep=7pt,xleftmargin=10pt]'
                + inner + '\\end{Verbatim}\n\\end{otherlanguage}')
    tex = re.sub(r'\\begin\{verbatim\}(.*?)\\end\{verbatim\}', _verb, tex, flags=re.S)
    # pandoc's longtables: keep them, but let the column text wrap
    tex = tex.replace('\\toprule()', '\\toprule').replace('\\midrule()', '\\midrule')
    tex = tex.replace('\\bottomrule()', '\\bottomrule').replace('\\endhead', '\\endhead')
    body.write_text(tex, encoding="utf-8")

    wrapper = TMP / "teacher-guide.tex"
    wrapper.write_text(r"""\documentclass[11pt,a4paper]{article}
\input{../../sqlcommon.tex}
\usepackage{hyperref}
\hypersetup{hidelinks}
\usepackage{calc}
\usepackage{longtable,booktabs}
\setlength{\LTleft}{0pt}\setlength{\LTright}{0pt}

\fancyhead[R]{\small בסיסי נתונים ו\lr{-}\lr{SQL} \textbar{} מדריך למורה}
\fancyhead[L]{\small \lr{\texttt{SELECT} · \texttt{WHERE} · \texttt{ORDER BY}}}

% קופסת תשובה — מה שב-GitHub מתקפל, כאן פשוט מודגש
\newsavebox{\ansbox}
\newenvironment{answerbox}[1]{\par\addvspace{6pt}\begin{lrbox}{\ansbox}%
  \begin{minipage}{\dimexpr\linewidth-2\fboxsep-2\fboxrule}%
  \textbf{\color{okgreen}#1}\par\vspace{2pt}}%
  {\end{minipage}\end{lrbox}\noindent\fcolorbox{okgreen}{white}{\usebox{\ansbox}}\par\addvspace{6pt}}

\begin{document}
\begin{center}
{\LARGE\bfseries\color{inkblue} מדריך למורה \textendash{} חומר הבחינה}\\[4pt]
{\large טבלאות ומפתחות \textbullet{} \texttt{SELECT} \textbullet{} \texttt{WHERE} \textbullet{} \texttt{ORDER BY}}\\[5pt]
{\small בסיס הנתונים: \lr{\texttt{school.sql}} \ \textbullet\ \ כל הפלטים רצו מול \lr{\texttt{sqlite3}}}\\[3pt]
{\small\bfseries\color{warnred} התשובות גלויות בדף הזה \textendash{} למורה בלבד}
\end{center}
\vspace{2pt}{\color{inkblue}\hrule height 1.2pt}\vspace{8pt}
\input{body.tex}
\end{document}
""", encoding="utf-8")

    for _ in range(2):
        subprocess.run(["lualatex", "-interaction=nonstopmode", "teacher-guide.tex"],
                       cwd=TMP, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    pdf = TMP / "teacher-guide.pdf"
    if not pdf.exists():
        sys.exit("build failed - see " + str(TMP / "teacher-guide.log"))
    shutil.copy(pdf, OUT / "מדריך למורה.pdf")
    print("built:", OUT / "מדריך למורה.pdf")

if __name__ == "__main__":
    main()
