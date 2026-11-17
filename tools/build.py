"""
Build script for the practical SQL course.

    python tools/build.py

What it does:
  1. databases/<name>/README.md  -- every table of every database, rendered
     as a GitHub table (structure + all rows) + the full SQL code to copy.
  2. lessons/<NN-name>/README.md -- the lesson page: load code, the tables used,
     short syntax, worked examples (with REAL output), exercises, extra practice.
  3. lessons/<NN-name>/solutions.md -- every solution + its REAL output.

Every query is executed in SQLite, so all the results in the repo are true.
Lesson content lives in tools/lessons/lNN_*.py (one file per lesson).
Do not edit the generated .md files by hand -- edit the content and rebuild.
"""
from __future__ import annotations

import importlib.util
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO_RAW = "https://raw.githubusercontent.com/AhmadKais/sql-course-heb/main/"
MAX_ROWS = 25  # longer results are cut in the solutions page

# --------------------------------------------------------------------------
# Databases
# --------------------------------------------------------------------------
DBS = {
    "music": dict(
        emoji="🎵", title='בית הספר למוזיקה "צלילים"',
        desc="תלמידים, מורים, רישומים (M:N), ערים, כלים ולוקרים (1:1). שמות שדות ייחודיים — בדיוק כמו בבחינה.",
        use="**בסיס הנתונים הראשי של השיעורים**"),
    "school": dict(
        emoji="🏫", title='בית הספר "עתיד"',
        desc="7 טבלאות: תלמידים, כיתות, מורים, מקצועות, ציונים, היעדרויות וערים. יש בו תאריכים ו‑NULL.",
        use="**תרגול נוסף** בסוף כל שיעור"),
    "clubs": dict(
        emoji="⚽", title="חוגי ספורט עירוניים",
        desc="חוגים, מאמנים, חברים וטבלה מקשרת.", use="בחינה לדוגמה 1"),
    "library": dict(
        emoji="📚", title="ספרייה עירונית",
        desc="ספרים, סופרים, קוראים והשאלות (עם תאריכים).", use="בחינה לדוגמה 2"),
    "games": dict(
        emoji="🎮", title="חנות משחקי מחשב",
        desc="משחקים, חברות, קטגוריות, משתמשים והזמנות.", use="בחינה לדוגמה 3"),
    "cafe": dict(
        emoji="☕", title='בית הקפה "אל‑בלד"',
        desc="מלצרים, מנות, הזמנות וערים. קטן ופשוט.", use="בחינת מתכונת"),
    "repairs": dict(
        emoji="🔧", title='מעבדת "דלתא‑טק"',
        desc="תיקוני מכשירים, טכנאים, חלפים וסוגי מכשירים.", use="בחינת אמצע"),
    "shelter": dict(
        emoji="🐾", title='מקלט בעלי החיים "בית חם"',
        desc="8 טבלאות באנגלית: חיות, אנשים, אימוצים, חיסונים והוצאות. בסיס גדול לתרגול חופשי.",
        use="תרגול חופשי ופרויקט"),
}


def db_path(name: str) -> Path:
    return ROOT / "databases" / name / f"{name}.sql"


def db_sql(name: str) -> str:
    return db_path(name).read_text(encoding="utf-8")


def load(name: str) -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.executescript(db_sql(name))
    return conn


def tables_of(conn) -> list[str]:
    return [r[0] for r in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY rowid")]


def column_comments(sql: str) -> dict[tuple[str, str], str]:
    """Pick up the '-- comment' written next to each column in CREATE TABLE."""
    out, table = {}, None
    for line in sql.splitlines():
        m = re.match(r"\s*CREATE TABLE\s+(\w+)", line, re.I)
        if m:
            table = m.group(1)
            continue
        if table and line.strip().startswith(")"):
            table = None
            continue
        if table:
            m = re.match(r"\s*(\w+)\s+\w+.*?--\s*(.+)$", line)
            if m:
                out[(table, m.group(1))] = m.group(2).strip()
    return out


# --------------------------------------------------------------------------
# Markdown helpers
# --------------------------------------------------------------------------
def fmt(v) -> str:
    if v is None:
        return "*NULL*"
    if isinstance(v, float):
        r = round(v, 2)
        return f"{r:.1f}" if r.is_integer() else f"{r:g}"
    return str(v).replace("|", "\\|")


def md_table(headers, rows, limit=None) -> str:
    lines = ["| " + " | ".join(headers) + " |",
             "|" + "|".join(["---"] * len(headers)) + "|"]
    shown = rows if limit is None else rows[:limit]
    for r in shown:
        lines.append("| " + " | ".join(fmt(v) for v in r) + " |")
    if limit is not None and len(rows) > limit:
        lines.append("| " + " | ".join(["…"] * len(headers)) + " |")
    return "\n".join(lines)


def rows_word(n: int) -> str:
    if n == 1:
        return "שורה אחת"
    return f"{n} שורות"


def rtl(text: str) -> str:
    return f'<div dir="rtl">\n\n{text.strip()}\n\n</div>\n'


def code(sql: str) -> str:
    return f"```sql\n{sql.strip()}\n```\n"


def key_marks(conn, table):
    """{column: '🔑' / '🔗' / '🔑🔗'} and {column: 'Table(col)'}"""
    info = conn.execute(f"PRAGMA table_info({table})").fetchall()
    fks = {r[3]: f"{r[2]}({r[4]})" for r in conn.execute(f"PRAGMA foreign_key_list({table})")}
    marks = {}
    for cid, col, typ, notnull, dflt, pk in info:
        m = ("🔑" if pk else "") + ("🔗" if col in fks else "")
        marks[col] = m
    return info, fks, marks


def data_table(conn, table, limit=None) -> str:
    info, fks, marks = key_marks(conn, table)
    headers = [f"{c[1]} {marks[c[1]]}".strip() for c in info]
    rows = conn.execute(f"SELECT * FROM {table}").fetchall()
    return md_table(headers, rows, limit)


def structure_table(conn, table, comments) -> str:
    info, fks, marks = key_marks(conn, table)
    lines = ["| עמודה | טיפוס | מפתח | הערה |", "|---|---|---|---|"]
    for cid, col, typ, notnull, dflt, pk in info:
        key = []
        if pk:
            key.append("🔑 PK")
        if col in fks:
            key.append(f"🔗 FK → `{fks[col]}`")
        note = comments.get((table, col), "")
        if notnull and not pk:
            note = ("חובה (NOT NULL). " + note).strip()
        lines.append(f"| `{col}` | {typ} | {' · '.join(key)} | {note} |")
    return "\n".join(lines)


def run(conn, sql: str):
    """Run one or more statements. Returns (headers, rows) of the last SELECT."""
    headers, rows, buf = None, None, ""
    for line in sql.strip().splitlines(keepends=True):
        buf += line
        if sqlite3.complete_statement(buf):
            cur = conn.execute(buf)
            if cur.description:
                headers = [d[0] for d in cur.description]
                rows = cur.fetchall()
            buf = ""
    if buf.strip() and not all(l.strip().startswith("--") or not l.strip() for l in buf.splitlines()):
        cur = conn.execute(buf)
        if cur.description:
            headers = [d[0] for d in cur.description]
            rows = cur.fetchall()
    return headers, rows


def execute(dbname: str, sql: str, check: str | None = None):
    """Fresh database for every query, so changes never leak between exercises."""
    conn = load(dbname)
    try:
        h, r = run(conn, sql)
        if check:
            h, r = run(conn, check)
    except sqlite3.Error as e:
        raise SystemExit(f"\n[{dbname}] SQL error: {e}\n{sql}\n")
    finally:
        conn.close()
    return h, r


def result_block(h, r, limit=None) -> str:
    if h is None:
        return "_(הפקודה לא מחזירה טבלה)_\n"
    if not r:
        return md_table(h, []) + "\n\n**התוצאה: 0 שורות** (טבלה ריקה)\n"
    note = ""
    if limit is not None and len(r) > limit:
        note = f" — מוצגות {limit} הראשונות"
    return md_table(h, r, limit) + f"\n\n**התוצאה: {rows_word(len(r))}**{note}\n"


def load_details(dbname: str) -> str:
    info = DBS[dbname]
    return (
        f'<details>\n<summary>📥 <b>לחצו כאן לקוד שבונה את בסיס הנתונים {info["emoji"]} {info["title"]}</b> '
        f"— מעתיקים הכול ומדביקים ב‑OneCompiler</summary>\n\n"
        f"```sql\n{db_sql(dbname).strip()}\n```\n\n</details>\n"
    )


# --------------------------------------------------------------------------
# Database pages
# --------------------------------------------------------------------------
HOW_TO_RUN = """\
## ▶️ איך מריצים (בלי להתקין כלום)

1. פותחים את **[OneCompiler — SQLite](https://onecompiler.com/sqlite)** (או **[SQLite Online](https://sqliteonline.com/)**, שמציג גם את רשימת הטבלאות בצד).
2. מוחקים את הדוגמה שבחלון (`Ctrl+A` ← `Delete`).
3. מעתיקים את **כל** הקוד של בסיס הנתונים ומדביקים.
4. **מתחת** לקוד כותבים את השאילתה שלכם ולוחצים **Run**.

> 💡 כל קובץ מתחיל ב‑`DROP TABLE IF EXISTS`, אז אפשר להדביק אותו שוב ושוב — הנתונים חוזרים למצב ההתחלתי. זה שימושי אחרי תרגילי `UPDATE` / `DELETE`.
"""


def build_database_page(name: str):
    info = DBS[name]
    sql = db_sql(name)
    conn = load(name)
    comments = column_comments(sql)
    tabs = tables_of(conn)
    counts = {t: conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0] for t in tabs}

    parts = [f'# {info["emoji"]} {info["title"]}\n',
             f'> {info["desc"]}\n>\n> **שימוש:** {info["use"]} · **{len(tabs)} טבלאות**\n',
             "[🏠 לדף הראשי](../../README.md) · [🗄️ כל בסיסי הנתונים](../README.md)\n",
             "---\n", HOW_TO_RUN, "---\n",
             "## 📥 הקוד המלא להעתקה\n",
             f"קובץ: [`{name}.sql`]({name}.sql) · [פתיחה כטקסט נקי (Ctrl+A, Ctrl+C)]({REPO_RAW}databases/{name}/{name}.sql)\n"]
    head = rtl("\n".join(parts))

    body = load_details(name) + "\n"

    overview = ["---\n", "## 🗺️ הטבלאות והקשרים\n",
                "| הטבלה | שורות | מפתח ראשי 🔑 | מפתחות זרים 🔗 |", "|---|:---:|---|---|"]
    for t in tabs:
        info_, fks, _ = key_marks(conn, t)
        pk = ", ".join(f"`{c[1]}`" for c in sorted(info_, key=lambda c: c[5]) if c[5])
        fk = "<br>".join(f"`{c}` → `{ref}`" for c, ref in fks.items()) or "—"
        overview.append(f"| [`{t}`](#{t.lower()}) | {counts[t]} | {pk or '—'} | {fk} |")
    overview.append("\n> 🔑 = מפתח ראשי (PK) · 🔗 = מפתח זר (FK) — מצביע על מפתח ראשי בטבלה אחרת.\n")

    for t in tabs:
        overview.append(f"---\n\n## {t}\n")
        overview.append(f"**המבנה:**\n\n{structure_table(conn, t, comments)}\n")
        overview.append(f"**הנתונים ({rows_word(counts[t])}):**\n\n{data_table(conn, t)}\n")
    conn.close()

    page = head + "\n" + body + "\n" + rtl("\n".join(overview))
    (ROOT / "databases" / name / "README.md").write_text(page, encoding="utf-8")


def build_databases_index():
    lines = ["# 🗄️ בסיסי הנתונים של הקורס\n",
             "> כל בסיס נתונים — בתיקייה משלו: **הטבלאות מוצגות כאן ב‑GitHub** (מבנה + כל הנתונים), ולצידן **הקוד המלא** שבונה אותן ב‑SQL.\n",
             "[🏠 לדף הראשי](../README.md)\n", "---\n", HOW_TO_RUN, "---\n",
             "| | בסיס הנתונים | מה יש בו | שימוש | הטבלאות והקוד | קובץ SQL |",
             "|:-:|---|---|---|:-:|:-:|"]
    for name, info in DBS.items():
        lines.append(f'| {info["emoji"]} | **{info["title"]}** | {info["desc"]} | {info["use"]} | '
                     f"[📋 טבלאות + קוד]({name}/) | [`{name}.sql`]({name}/{name}.sql) |")
    (ROOT / "databases" / "README.md").write_text(rtl("\n".join(lines)), encoding="utf-8")


# --------------------------------------------------------------------------
# Lesson pages
# --------------------------------------------------------------------------
LEVEL = {1: "🟢", 2: "🟡", 3: "🔴"}
KIND = {"write": "✍️", "output": "🔎 **איזו שאילתה הציגה את הטבלה?**",
        "value": "🧮 **השלימו את הערכים:**", "complete": "🧩 **השלימו את הפקודה:**"}


def tables_details(dbname: str) -> str:
    conn = load(dbname)
    parts = [f'<details>\n<summary>📋 <b>הטבלאות של {DBS[dbname]["title"]}</b> (לחצו לפתיחה)</summary>\n\n<div dir="rtl">\n']
    for t in tables_of(conn):
        parts.append(f"**`{t}`**\n\n{data_table(conn, t)}\n")
    conn.close()
    parts.append("</div>\n\n</details>\n")
    return "\n".join(parts)


def load_lessons():
    lessons = []
    sys.path.insert(0, str(ROOT / "tools" / "lessons"))
    for f in sorted((ROOT / "tools" / "lessons").glob("l[0-9][0-9]_*.py")):
        spec = importlib.util.spec_from_file_location(f.stem, f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        lesson = mod.LESSON
        # optional extra practice for this lesson: more_NN.py with extend(LESSON)
        more = f.parent / f"more_{f.stem[1:3]}.py"
        if more.exists():
            spec = importlib.util.spec_from_file_location(more.stem, more)
            mmod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mmod)
            mmod.extend(lesson)
        lessons.append(lesson)
    return lessons


def lesson_nav(lessons, i, file="README.md") -> str:
    prev_ = f"[➡️ השיעור הקודם](../{lessons[i-1]['slug']}/{file})" if i > 0 else ""
    next_ = f"[השיעור הבא ⬅️](../{lessons[i+1]['slug']}/{file})" if i < len(lessons) - 1 else ""
    items = [x for x in (prev_, "[🏠 כל השיעורים](../README.md)", next_) if x]
    return " · ".join(items)


def build_lesson(lessons, i):
    L = lessons[i]
    db, extra_db = L.get("db", "music"), L.get("extra_db", "school")
    num = f"{i + 1:02d}"
    conn = load(db)

    # ---------- README ----------
    out = []
    intro = [f"# שיעור {i + 1} — {L['title']}\n",
             lesson_nav(lessons, i) + "\n",
             f"> 🎯 **בשיעור הזה:** {L['goal']}\n>\n"
             f"> 🗄️ **בסיס הנתונים:** {DBS[db]['emoji']} [{DBS[db]['title']}](../../databases/{db}/) · "
             f"✅ [הפתרונות](solutions.md)\n",
             "---\n", "## 1️⃣ טוענים את בסיס הנתונים\n",
             "פותחים את [OneCompiler — SQLite](https://onecompiler.com/sqlite), מדביקים את **כל** הקוד, ומתחתיו כותבים את השאילתות.\n"]
    out.append(rtl("\n".join(intro)))
    out.append(load_details(db) + "\n")

    tparts = ["## 2️⃣ הטבלאות שעובדים איתן\n",
              "> 🔑 = מפתח ראשי · 🔗 = מפתח זר. לכל הטבלאות: [בסיס הנתונים המלא](../../databases/%s/)\n" % db]
    for t in L["tables"]:
        tparts.append(f"**`{t}`**\n\n{data_table(conn, t)}\n")
    tparts.append("---\n\n## 3️⃣ התחביר בקצרה\n")
    out.append(rtl("\n".join(tparts)))
    out.append(code(L["syntax"]))
    if L.get("tips"):
        out.append(rtl("\n".join(f"- {t}" for t in L["tips"])))

    out.append(rtl("---\n\n## 4️⃣ דוגמאות פתורות\n\n> קראו את השאלה, נסו לכתוב בעצמכם, ורק אז הסתכלו על הפתרון והתוצאה."))
    for n, ex in enumerate(L["examples"], 1):
        h, r = execute(db, ex["sql"], ex.get("check"))
        out.append(rtl(f"### דוגמה {n}: {ex['q']}"))
        out.append(code(ex["sql"]))
        if ex.get("check"):
            out.append(rtl("בדיקה — מה יש בטבלה אחרי הפקודה:"))
            out.append(code(ex["check"]))
        txt = result_block(h, r, MAX_ROWS)
        if ex.get("note"):
            txt += f"\n> 💡 {ex['note']}\n"
        out.append(rtl(txt))

    if L.get("predict"):
        pq = ["---\n\n## 5️⃣ שאלות: מה תחזיר השאילתה?\n",
              "> בלי להריץ! כתבו על דף את הטבלה שתתקבל (או רק את מספר השורות). אחר כך הריצו ובדקו. התשובות ב[פתרונות](solutions.md).\n"]
        out.append(rtl("\n".join(pq)))
        for n, p in enumerate(L["predict"], 1):
            out.append(rtl(f"**שאלה {n}.** {p.get('q', 'מה תחזיר השאילתה?')}"))
            out.append(code(p["sql"]))
    sec = 6 if L.get("predict") else 5

    ex_head = [f"---\n\n## {sec}️⃣ תרגילים — {DBS[db]['emoji']} {DBS[db]['title']}\n",
               "> כתבו שאילתה לכל סעיף והריצו. **🔢 מספר השורות הצפוי** עוזר לבדוק את עצמכם. "
               "🟢 קל · 🟡 בינוני · 🔴 מאתגר\n"]
    for n, x in enumerate(L["exercises"], 1):
        h, r = execute(db, x["sql"], x.get("check"))
        hint = f" _(🔢 {rows_word(len(r))})_" if r is not None and not x.get("check") else (" _(🔍 משנה נתונים — בדקו עם SELECT)_" if x.get("check") else "")
        ex_head.append(f"{n}. {LEVEL[x['level']]} {x['q']}{hint}\n")
    out.append(rtl("\n".join(ex_head)))

    exam_db = L.get("exam_db")
    if L.get("exam"):
        eh = [f"---\n\n## {sec + 1}️⃣ 🎓 בסגנון הבחינה — {DBS[exam_db]['emoji']} {DBS[exam_db]['title']}\n",
              "> שאלות בפורמט של שאלון 735911: שמות שדות ייחודיים, צירוף עם פסיק + `WHERE`, "
              "השלמת ערכים, זיהוי שאילתה לפי פלט והשלמת פקודות. "
              f"[📋 הטבלאות והקוד](../../databases/{exam_db}/)\n"]
        out.append(rtl("\n".join(eh)))
        out.append(tables_details(exam_db) + "\n")
        out.append(load_details(exam_db).replace("לחצו כאן לקוד", "הקוד") + "\n")
        for n, x in enumerate(L["exam"], 1):
            h, r = execute(exam_db, x["sql"], x.get("check"))
            kind = x.get("kind", "write")
            hint = ""
            if kind == "write":
                if x.get("check"):
                    hint = " _(🔍 משנה נתונים)_"
                elif r is not None:
                    hint = f" _(🔢 {rows_word(len(r))})_"
            out.append(rtl(f"**שאלה {n}.** {LEVEL[x['level']]} {KIND[kind]} {x['q']}{hint}"))
            if kind == "output":
                out.append(rtl(md_table(h, r) + "\n"))
            elif kind == "value":
                out.append(code(x["sql"]))
            elif kind == "complete":
                out.append(code(x["given"]))

    if L.get("extra"):
        xh = [f"---\n\n## {sec + 2 if L.get('exam') else sec + 1}️⃣ תרגול נוסף — {DBS[extra_db]['emoji']} {DBS[extra_db]['title']}\n",
              f"> בסיס נתונים אחר, שאתם לא מכירים — בדיוק כמו בבחינה. "
              f"[📋 הטבלאות והקוד של {DBS[extra_db]['title']}](../../databases/{extra_db}/)\n"]
        for n, x in enumerate(L["extra"], 1):
            h, r = execute(extra_db, x["sql"], x.get("check"))
            hint = f" _(🔢 {rows_word(len(r))})_" if r is not None and not x.get("check") else (" _(🔍 משנה נתונים — בדקו עם SELECT)_" if x.get("check") else "")
            xh.append(f"{n}. {LEVEL[x['level']]} {x['q']}{hint}\n")
        out.append(rtl("\n".join(xh)))
        out.append(load_details(extra_db).replace("לחצו כאן לקוד", "הקוד") + "\n")

    out.append(rtl(f"---\n\n✅ **[לפתרונות המלאים — שאילתה + התוצאה האמיתית](solutions.md)**\n\n{lesson_nav(lessons, i)}"))
    lesson_dir = ROOT / "lessons" / L["slug"]
    lesson_dir.mkdir(parents=True, exist_ok=True)
    (lesson_dir / "README.md").write_text("\n".join(out), encoding="utf-8")
    conn.close()

    # ---------- solutions ----------
    s = [rtl(f"# שיעור {i + 1} — פתרונות\n\n[⬅️ חזרה לשיעור](README.md) · {lesson_nav(lessons, i, 'solutions.md')}\n\n"
             "> ⚠️ קודם נסו לבד! כל תוצאה כאן היא פלט אמיתי של SQLite. בפקודות שמשנות נתונים כל תרגיל רץ על בסיס נתונים טרי.")]
    if L.get("predict"):
        s.append(rtl("---\n\n## ❓ שאלות: מה תחזיר השאילתה?"))
        for n, p in enumerate(L["predict"], 1):
            h, r = execute(db, p["sql"])
            s.append(rtl(f"### שאלה {n}"))
            s.append(code(p["sql"]))
            txt = result_block(h, r, MAX_ROWS)
            if p.get("note"):
                txt += f"\n> 💡 {p['note']}\n"
            s.append(rtl(txt))

    def sol_section(title, items, dbname):
        s.append(rtl(f"---\n\n## {title}"))
        for n, x in enumerate(items, 1):
            h, r = execute(dbname, x["sql"], x.get("check"))
            s.append(rtl(f"### {n}. {LEVEL[x['level']]} {x['q']}"))
            s.append(code(x["sql"]))
            if x.get("check"):
                s.append(rtl("בדיקה:"))
                s.append(code(x["check"]))
            txt = result_block(h, r, MAX_ROWS)
            if x.get("note"):
                txt += f"\n> 💡 {x['note']}\n"
            s.append(rtl(txt))

    sol_section(f"✏️ תרגילים — {DBS[db]['emoji']} {DBS[db]['title']}", L["exercises"], db)
    if L.get("exam"):
        sol_section(f"🎓 בסגנון הבחינה — {DBS[exam_db]['emoji']} {DBS[exam_db]['title']}", L["exam"], exam_db)
    if L.get("extra"):
        sol_section(f"🏠 תרגול נוסף — {DBS[extra_db]['emoji']} {DBS[extra_db]['title']}", L["extra"], extra_db)
    s.append(rtl(f"---\n\n[⬅️ חזרה לשיעור](README.md) · {lesson_nav(lessons, i, 'solutions.md')}"))
    (lesson_dir / "solutions.md").write_text("\n".join(s), encoding="utf-8")
    return dict(num=num, slug=L["slug"], title=L["title"], goal=L["goal"],
                n_ex=len(L["exercises"]) + len(L.get("extra", [])) + len(L.get("predict", []))
                + len(L.get("exam", [])))


def build_lessons_index(meta):
    lines = ["# 📚 השיעורים\n", "[🏠 לדף הראשי](../README.md)\n",
             "> כל שיעור: **קוד לטעינת בסיס הנתונים ← הטבלאות ← תחביר קצר ← דוגמאות פתורות ← שאלות ותרגילים ← 🎓 שאלות בסגנון הבחינה ← פתרונות עם פלט אמיתי.**\n",
             "| # | השיעור | מה מתרגלים | שאלות | |", "|:-:|---|---|:-:|:-:|"]
    for m in meta:
        lines.append(f"| {int(m['num'])} | [{m['title']}]({m['slug']}/) | {m['goal']} | {m['n_ex']} | [✅ פתרונות]({m['slug']}/solutions.md) |")
    (ROOT / "lessons" / "README.md").write_text(rtl("\n".join(lines)), encoding="utf-8")


def main():
    for name in DBS:
        build_database_page(name)
    build_databases_index()
    lessons = load_lessons()
    meta = [build_lesson(lessons, i) for i in range(len(lessons))]
    if meta:
        build_lessons_index(meta)
    total = sum(m["n_ex"] for m in meta)
    print(f"built {len(DBS)} databases, {len(meta)} lessons, {total} questions")


if __name__ == "__main__":
    sys.exit(main())
