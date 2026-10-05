<div dir="rtl">

# קורס בסיסי נתונים ו‑SQL 🗄️

### מגמת תקשוב | מערכות תקשוב | התמחות י"ג–י"ד

קורס מלא, מודול אחר מודול, לבניית הבנה עמוקה בעולם בסיסי הנתונים — מהמושגים הבסיסיים ביותר, דרך עיצוב מודל נתונים ותרשימי ERD, ועד לכתיבת שאילתות SQL מורכבות.

הקורס בנוי על פי **תכנית הלימודים של משרד החינוך – מינהל מדע וטכנולוגיה, מגמת תקשוב** (32 פרקים), ומרחיב אותה עם הסברים מלאים, דוגמאות, סיפורים מהעולם האמיתי, שאלות ותשובות ותרגילים עם פתרונות מלאים.

<div align="center">

## 👇 חדשים כאן? התחילו מכאן

### 🚪 **[שיעור 1: טבלאות, מפתחות והשאילתה הראשונה](modules/module-00-quick-start/)**

*מפתח ראשי ומפתח זר · קשרים · תרשים DSD · השאילתה הראשונה, כבר בשיעור הראשון*

### 🧭 **[סדר ההוראה: 20 שיעורים, SQL משיעור 2](LEARNING-PATH.md)**

*כל נושא עיצובי לצד ה‑SQL שמשתמש בו · תרגול בסגנון הבחינה בכל שיעור*

### 📋 **[קובצי ה‑SQL להעתקה](SQL-FILES.md)**

*כל בסיסי הנתונים של הקורס: מעתיקים בשתי לחיצות ומדביקים ב‑[OneCompiler](https://onecompiler.com/sqlite)*

### 🎓 **[הכנה לבחינה (שאלון 735911)](exam-prep/)**

*איך בנוי חלק בסיסי הנתונים · דף עזר להדפסה · 3 בחינות לדוגמה, עם קבצי `.sql` לבדיקה עצמית*

</div>

---

## 📚 מבנה הקורס

| # | מודול | נושא | סטטוס |
|---|-------|------|-------|
| **0–1** | [**שיעור 1: טבלאות, מפתחות והשאילתה הראשונה**](modules/module-00-quick-start/) | DDL/DML, PK/FK, קשרים, DSD, `SELECT` ראשון. **מחליף** בהוראה את פרקים 0–1 | ✅ חדש |
| 0 | [מבוא, הגרסה המלאה](modules/module-00-intro/) | להרחבה בלבד | ✅ |
| 1 | [רקע ומושגי יסוד](modules/module-01-foundations/) | נתונים מול מידע, היסטוריה של בסיסי נתונים, DBMS | ✅ מוכן |
| 2 | [מודל הנתונים](modules/module-02-data-model/) | ישויות, מופעים, מאפיינים, מזהים | ✅ מוכן |
| 3 | [תרשים ERD](modules/module-03-erd/) | קשרים, יחסים, מוסכמות שרטוט, דיאגרמות מטריציוניות | ✅ מוכן |
| 4 | [טיפוסי משנה וטיפוסי על](modules/module-04-subtypes-supertypes/) | Subtypes, Supertypes, תיעוד חוקים עסקיים | ✅ מוכן |
| 5 | [יחסים](modules/module-05-relationships/) | יחסים עבירים, סוגי יחסים, פתרון M:M, CRUD | ✅ מוכן |
| 6 | [נרמול](modules/module-06-normalization/) | מזהים מלאכותיים/מורכבים/משניים, 1NF, 2NF, 3NF | ✅ מוכן |
| 7 | [אילוצים](modules/module-07-constraints/) | תחומים, קשתות, היררכיות, כללי מחיקה, מידע היסטורי | ✅ מוכן |
| 8 | [תפקיד היועץ](modules/module-08-consultant/) | מיהו היועץ, אפקט הפחד, הצגה ללקוח, יומן החלטות | ✅ מוכן |
| 9 | [פרויקט I](modules/module-09-project-1/) | פרויקט מלא: ראיון ⟵ חוקים ⟵ ERD ⟵ הצגה ⟵ שילוב שינויים | ✅ מוכן |
| 10 | [עיצוב למעקב אחר שינויים](modules/module-10-tracking-changes/) | מימד הזמן, מודל דו‑זמני, מחירים, שיטות מעקב | ✅ מוכן |
| 11 | [מודלים גנריים](modules/module-11-generic-models/) | מוסכמות פריסה, תחומי נושא, הפשטה, EAV | ✅ מוכן |
| 12 | [מעבר לבסיס הנתונים](modules/module-12-mapping/) | מונחים, מיפוי ישויות ויחסים, טיפוסי משנה, APEX | ✅ מוכן |
| 13 | [SQL I — הכרות, עבודת צוות וניהול](modules/module-13-sql-1/) | מפת SQL, תפקידים, Kanban, Git, סיכונים | ✅ מוכן |
| 14 | [SDLC](modules/module-14-sdlc/) | שלבי הפיתוח, Waterfall מול Agile, בדיקות, טבלאות בסבבים | ✅ מוכן |
| 15 | [המצגת](modules/module-15-presentation/) | סיפור, שקפים, הדגמה חיה, מסמך, חזרות | ✅ מוכן |
| **16** | [SQL: המשפט הראשון](modules/module-16-sql-basics/) | `SELECT`, `FROM`, כינויים, חישובים, `DISTINCT`, NULL | ✅ מוכן |
| 17 | [SQL: הגבלת השליפה](modules/module-17-sql-where/) | `WHERE`, `BETWEEN`, `IN`, `LIKE`, `IS NULL`, `AND`/`OR` | ✅ מוכן |
| 18 | [SQL: מיונים](modules/module-18-sql-order-by/) | `ORDER BY`, NULL במיון, `LIMIT`, סדר הביצוע הלוגי | ✅ מוכן |
| 19 | [SQL: פונקציות](modules/module-19-sql-functions/) | טקסט, מספרים, תאריכים, חישוב גיל, SQLite מול Oracle | ✅ מוכן |
| 20 | [SQL: פונקציות 2](modules/module-20-sql-functions-2/) | המרה, `COALESCE`, `NULLIF`, `CASE` | ✅ מוכן |
| 21 | [SQL: איחוד טבלאות](modules/module-21-sql-joins/) | תוצר קרטזי, equi/nonequi, outer, self join, היררכיה | ✅ מוכן |
| 22 | [SQL: איחוד טבלאות 2](modules/module-22-sql-joins-2/) | `CROSS`, `NATURAL`, `USING`, `RIGHT`/`FULL`, שרשראות | ✅ מוכן |
| 23 | [SQL: פונקציות מצרפיות](modules/module-23-sql-aggregates/) | `COUNT`/`SUM`/`AVG`, NULL, `SUM(CASE)` | ✅ מוכן |
| 24 | [SQL: קיבוץ ותתי‑שאילתות](modules/module-24-sql-group-by/) | `GROUP BY`, `HAVING`, `ROLLUP`, תתי‑שאילתות, `UNION` | ✅ מוכן |
| 25 | [SQL: DML](modules/module-25-sql-dml/) | `INSERT`, `UPDATE`, `DELETE`, `DEFAULT`, `MERGE` | ✅ מוכן |
| 26 | [SQL: DDL](modules/module-26-sql-ddl/) | `CREATE`, טיפוסים, `STRICT`, `ALTER`, `DROP` | ✅ מוכן |
| 27 | [SQL: אילוצים](modules/module-27-sql-constraints/) | `NOT NULL`, `UNIQUE`, PK, FK, `CHECK`, קשתות | ✅ מוכן |
| 28 | [SQL: Views](modules/module-28-sql-views/) | יצירה, אבטחה, מצב נוכחי מהיסטוריה | ✅ מוכן |
| 29 | [SQL: אובייקטים נוספים](modules/module-29-sql-objects/) | Sequences, אינדקסים, Synonyms, ראיון בכיתה | ✅ מוכן |
| 30 | [SQL: ניהול משתמשים](modules/module-30-sql-users/) | `GRANT`, Roles, Regex, חיפוש עבודה | ✅ מוכן |
| 31 | [SQL: פרויקט מסכם](modules/module-31-sql-final-project/) | תוצרים, 15 שאילתות, מחוון, הגנה | ✅ מוכן |
| 32 | [SQL: טרנזקציות](modules/module-32-sql-transactions/) | `COMMIT`, `ROLLBACK`, `SAVEPOINT`, ACID, הסמכה | ✅ מוכן |

---

## 🎯 מטרות הקורס

- להקנות מושגי יסוד בניהול ידע ארגוני
- להקנות כלים לניתוח תרחישים עסקיים מורכבים
- ללמד כיצד יוצרים מודל נתונים
- ללמד כיצד מתרגמים מודל נתונים למסד נתונים רלציוני
- הכרות עם מונחי מסד הנתונים הרלציוני
- הכרות מעמיקה עם שפת SQL

---

## 🧭 איך לומדים כאן?

> **באיזה סדר?** לפי [**סדר ההוראה**](LEARNING-PATH.md): 20 שיעורים, ו‑SQL כבר מהשיעור השני. [סדר הפרקים הרשמי](SYLLABUS.md) (15 פרקי עיצוב ואחריהם 17 פרקי SQL) נשאר רק כמפה.

כל מודול בקורס בנוי מארבעה קבצים, וכדאי לעבור עליהם **לפי הסדר**:

| קובץ | מה יש בו | כמה זמן |
|------|----------|---------|
| `README.md` | ההסבר המלא: תיאוריה, דוגמאות וסיפורים מהשטח | 45–60 דק' |
| `questions.md` | שאלות ותשובות לבדיקה עצמית — קראו את השאלה, ענו בראש, ואז פתחו את התשובה | 20 דק' |
| `exercises.md` | תרגילים מעשיים לפי רמות קושי | 60–90 דק' |
| `solutions.md` | פתרונות מלאים עם הסבר — **רק אחרי שניסיתם!** | 30 דק' |

> 💡 **טיפ למידה:** בכל מודול יש קופסאות `🎬 סיפור מהשטח`. אלה לא קישוט — הן מסבירות *למה* המושג התיאורטי קיים. אם משהו לא ברור בתיאוריה, קראו קודם את הסיפור.

### המבנה הקבוע של כל מודול

כל `README.md` בנוי לפי אותו סדר, כדי שתמיד תדעו איפה למצוא מה:

| הסעיף | מה יש בו |
|--------|-----------|
| 🎯 **מה תדעו בסוף המודול** | רשימת יעדים לסימון — השתמשו בה כמבחן עצמי בסוף |
| 🗺️ **מפת המודול** | תוכן עניינים עם קישורים — לקפיצה ישירה לכל סעיף |
| **1 … N** | ההסבר עצמו, מהמושג הבסיסי אל המורכב |
| **דוגמה מלאה מקצה לקצה** | מקרה אחד שמלווה את כל מושגי המודול |
| **טעויות נפוצות** | טבלה של מה משתבש בפועל, ואיך מתקנים |
| **רשימת בדיקה** | לסימון לפני שממשיכים למודול הבא |
| **סיכום המודול** | הנקודות שחייבים לצאת איתן |
| 📎 **המשך** | קישורים לשאלות, תרגילים, פתרונות והמודול הבא |

---

## 👩‍🏫 למרצים ולמציגים בכיתה

הקבצים כתובים כך שאפשר להציג אותם ישירות מהמסך, בלי להכין מצגת:

| מה | איך |
|-----|------|
| **שיעור של 45 דק'** | סעיפים 1–4 של המודול + סיפור מהשטח אחד |
| **שיעור של 90 דק'** | המודול המלא + פתרון משותף של 2–3 תרגילים 🟢🟡 |
| **פתיחת שיעור** | ה‑🎬 **סיפור מהשטח** — הוא נכתב כדי להיאמר בקול |
| **דיון בכיתה** | ה‑❓ **שאלות** — הציגו את השאלה, תנו דקה, ואז פתחו את התשובה |
| **שיעורי בית** | 🟢 ו‑🟡 מה‑**תרגילים**; ה‑🔴 למתקדמים |
| **סיכום שיעור** | טבלת **טעויות נפוצות** + **רשימת הבדיקה** |
| **מבחן** | ה‑❓ שאלות מכל המודולים; מודול 9 כולל מבחן חזרה של 25 שאלות ומחוון של 100 נקודות |

> 💡 **בהצגה על מסך:** קפלו את התשובות ב‑`questions.md` — הן סגורות כברירת מחדל ונפתחות בלחיצה. זה מאפשר לשאול את הכיתה לפני שחושפים.

---

## 🛠️ סביבת עבודה

מודולים 1–11 הם **מודולים עיוניים** של עיצוב נתונים — לא נדרשת התקנה של כלום. נייר ועיפרון (או כלי שרטוט) יספיקו.

מהמודולים המתקדמים ואילך נעבוד עם בסיס נתונים אמיתי. ההמלצות:

| כלי | למה הוא טוב | קישור |
|-----|-------------|-------|
| ⭐ **OneCompiler (SQLite)** | **ברירת המחדל של הקורס**: בדפדפן, בלי התקנה. מדביקים את `shelter.sql` או קובץ של בחינה לדוגמה, וכל הפקודות עובדות | [onecompiler.com/sqlite](https://onecompiler.com/sqlite) |
| ⭐ **W3Schools SQL** | הסבר על כל נושא, ותרגול `SELECT` על בסיס הנתונים שלו (לקריאה בלבד, SQL Server) | [w3schools.com/sql](https://www.w3schools.com/sql/) |
| **DB Fiddle** | חלופה בדפדפן לבדיקת שאילתה בודדת | [db-fiddle.com](https://www.db-fiddle.com) |
| **SQLite + DB Browser** | מקומי, ללא שרת — כשרוצים לשמור פרויקט מתמשך | [sqlitebrowser.org](https://sqlitebrowser.org) |
| **Oracle APEX** | סביבת התרגול הרשמית של תכנית הלימודים | [apex.oracle.com](https://apex.oracle.com) |
| **MySQL / PostgreSQL** | בסיסי נתונים תעשייתיים אמיתיים | — |

לשרטוט תרשימי ERD: [draw.io](https://app.diagrams.net) (חינמי), Lucidchart, או פשוט נייר.

👈 **[מדריך התקנה מפורט צעד‑אחר‑צעד](resources/setup.md)** — כולל פתרון תקלות נפוצות.

---

## 📂 מבנה התיקיות

</div>

```text
sql-course-heb/
├── README.md                    <- you are here
├── LEARNING-PATH.md             <- teaching order (20 lessons, SQL from lesson 2)
├── exam-prep/                   <- Ministry exam 735911: guide, cheat sheet, mock-exam databases
├── SYLLABUS.md                  <- official chapter order (32 chapters)
├── modules/
│   ├── module-00-quick-start/   <- START HERE (lesson 1, replaces 00 + 01 in class)
│   ├── module-00-intro/
│   ├── module-01-foundations/
│   │   ├── README.md            <- full explanation
│   │   ├── questions.md         <- Q & A
│   │   ├── exercises.md         <- exercises
│   │   └── solutions.md         <- solutions
│   ├── module-02-data-model/
│   ├── module-03-erd/
│   ├── module-04-subtypes-supertypes/
│   ├── module-05-relationships/
│   ├── module-06-normalization/
│   ├── module-07-constraints/
│   ├── module-08-consultant/
│   ├── module-08-15-summary/    <- chapters 8, 13, 14, 15 condensed (project + defense)
│   ├── module-09-project-1/
│   ├── module-10-tracking-changes/
│   ├── module-11-generic-models/
│   ├── module-16-sql-basics/
│   ├── module-17-sql-where/
│   ├── module-18-sql-order-by/
│   └── module-19-sql-functions/    (module number = syllabus chapter)
├── project/
│   └── README.md                <- running project: animal shelter
└── resources/
    ├── glossary.md              <- Hebrew-English glossary
    ├── setup.md                 <- environment setup guide
    ├── shelter-db/              <- ready-made practice database (units 2-7)
    └── pro-data.pdf             <- original syllabus
```

<div dir="rtl">

---

## 🐾 הפרויקט המלווה

לאורך כל הקורס נבנה יחד מערכת אחת אמיתית: **מקלט לבעלי חיים**. בכל מודול נוסיף לה שכבה — קודם נבין את הצרכים, אחר כך נבנה מודל נתונים, נשרטט ERD, ולבסוף נתרגם הכל לטבלאות ולשאילתות SQL.

👈 [לפרטי הפרויקט](project/)

---

## 📖 מקורות

- תכנית הלימודים: **משרד החינוך, מינהל מדע וטכנולוגיה, מגמת תקשוב** — "מערכות תקשוב התמחות י"ג, תכנית לימודים – בסיסי נתונים", מאת דגנית סולומון הרטמן.
- Oracle Academy – Database Design & Database Programming with SQL.

---

<div align="center">

**בהצלחה! 🚀**

</div>

</div>
