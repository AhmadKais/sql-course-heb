<div dir="rtl">

# 🗄️ תרגול SQL מעשי והכנה לבחינה (שאלון 735911)

### מכללת עתיד | מגמת תקשוב | התמחות י"ג–י"ד | מה"ט ומשרד החינוך

> 🎯 **מטרת המאגר:** הכנה מעשית ממוקדת לבחינה. **ללא תיאוריה מיותרת של עיצוב בסיסי נתונים** — אלא 100% תרגול שאילתות SQL מהרמה הבסיסית ביותר ועד לשאלות הבחינה המורכבות.

---

## ⚡ התחילו כאן: הכלים המרכזיים לפתרון הבחינה

<div align="center">

### 📖 [ספר הקורס המעשי: SQL מהקל למתקדם — ללא תיאוריה](exam-prep/practical-course-guide.md)
*מדריך מקיף וקצר שמכסה את כל נושאי השאילתות לבחינה ב-12 פרקים תמציתיים: תחביר, דוגמאות קוד, ומלכודות בחינה.*

### 🏆 [מאגר שאילתות ותרגול מהקל למתקדם (90 שאלות מדורגות)](exam-prep/master-sql-practice.md)
*מסלול תרגול מקיף ב‑9 רמות קושי מדורגות עם [פתרונות מלאים](exam-prep/master-sql-practice-solutions.md)*

### 🧮 [מדריך ותרגול פונקציות ב‑SQL (COUNT, MAX, AVG, MIN, SUM ועוד)](exam-prep/sql-functions-guide.md)
*כל מה שצריך לדעת על פונקציות קיבוץ ופונקציות שורה, כללי ברזל לבחינה, ו‑25 תרגילי פונקציות עם פתרונות*

### 🎯 [תרגול לפי הנחיות משרד החינוך לתשפ"ז (48 שאלות בחינה)](exam-prep/practice-2027.md)
*שאלות בסגנון הבחינה המדויק על בסיס הנתונים `music.sql` עם [פתרונות מלאים](exam-prep/practice-2027-solutions.md)*

### 💡 [20 דוגמאות פתורות צעד אחרי צעד](exam-prep/examples-2027.md)
*איך לגשת לשאלה, איך לחשוב, השאילתה והתוצאה המדויקת שלה*

### 📋 [דף עזר להדפסה ולבחינה (Cheat Sheet)](exam-prep/cheat-sheet.md)
*כל התחביר, הפונקציות, המלכודות והכללים בטבלאות מרוכזות — מותר להביא לבחינה!*

### 💻 [קובצי ה‑SQL להרצה מיידית בדפדפן](SQL-FILES.md)
*העתיקו בלחיצה אחת והדביקו ב‑[OneCompiler SQLite](https://onecompiler.com/sqlite) או ב‑[SQLite Online](https://sqliteonline.com/)*

</div>

---

## 🧭 מסלול לימוד שאילתות SQL: מהקל למתקדם

כל החומר של הבחינה מחולק ל‑9 שלבים מדורגים. עברו שלב אחר שלב:

| שלב | נושא השאילתות | מה לומדים ומתרגלים? | מודול מעשי ותרגול מומלץ |
|:---:|---|---|:---:|
| **🟢 שלב 1** | **שליפה בסיסית וסינון פשוט** | `SELECT`, `FROM`, `WHERE` (`=, >, <, <>`), `ORDER BY` (`ASC/DESC`), `DISTINCT`, כינויים (`AS`) | [מאגר שאלות: רמה 1](exam-prep/master-sql-practice.md#🟢-רמה-1-שליפה-בסיסית-וסינון-פשוט) · [01 sql-basics](modules/01-sql-basics/) · [02 sql-where](modules/02-sql-where/) · [03 sql-order-by](modules/03-sql-order-by/) |
| **🟢 שלב 2** | **תנאים מורכבים ולוגיקה** | שילוב `AND`, `OR`, `NOT`, שימוש בסוגריים, `BETWEEN` (כולל קצוות), `IN`, חיפוש טקסט `LIKE ('%_')`, בדיקת ערך חסר `IS NULL` / `IS NOT NULL` | [מאגר שאלות: רמה 2](exam-prep/master-sql-practice.md#🟢-רמה-2-תנאים-מורכבים-ולוגיקה-and-or-between-in-like-null) · [02 sql-where](modules/02-sql-where/) |
| **🟡 שלב 3** | **פונקציות ב‑SQL (ספירה וצבירה)** | פונקציות מצרפיות: `COUNT(*)`, `COUNT(col)`, `COUNT(DISTINCT)`, `SUM`, `AVG`, `MIN`, `MAX`. פונקציות שורה: `LENGTH`, `UPPER`, `LOWER`, `ROUND`, `SUBSTR`, `COALESCE` | 🧮 **[מדריך הפונקציות המלא](exam-prep/sql-functions-guide.md)** · [מאגר שאלות: רמה 3](exam-prep/master-sql-practice.md#🟡-רמה-3-פונקציות-בsql-קיבוץ-סקלריות-מחרוזות-ועיגול) · [04 sql-functions](modules/04-sql-functions/) · [06 sql-aggregates](modules/06-sql-aggregates/) |
| **🟡 שלב 4** | **קיבוץ נתונים (GROUP BY & HAVING)** | חלוקה לקבוצות לפי עמודות, חישוב מצרפי לכל קבוצה, סינון קבוצות ב‑`HAVING`, ההבדל הקריטי בין `WHERE` (שורה) ל‑`HAVING` (קבוצה) | [מאגר שאלות: רמה 4](exam-prep/master-sql-practice.md#🟡-רמה-4-קיבוץ-נתונים-ותנאי-קבוצה-group-by--having) · [07 sql-group-by-having](modules/07-sql-group-by-having/) |
| **🟡 שלב 5** | **חיבור טבלאות (צירופים — Joins)** | צירוף 2 ו‑3 טבלאות לפי מפתח ראשי וזר (`WHERE PK = FK`), תחביר `JOIN ... ON`, וצירוף חיצוני `LEFT JOIN` להצגת נתונים שאין להם התאמה | [מאגר שאלות: רמה 5](exam-prep/master-sql-practice.md#🟡-רמה-5-חיבור-טבלאות-צירופים--joins) · [08 sql-joins](modules/08-sql-joins/) · [09 sql-joins-advanced](modules/09-sql-joins-advanced/) |
| **🔴 שלב 6** | **שאילתות מקוננות (Subqueries)** | שאילתה בתוך שאילתה: `WHERE col IN (SELECT...)`, `WHERE col NOT IN (...)`, השוואה לערך מקסימלי או ממוצע מחושב | [מאגר שאלות: רמה 6](exam-prep/master-sql-practice.md#🔴-רמה-6-שאילתות-מקוננות-תתשאילתות--subqueries) · [דוגמאות 13–16](exam-prep/examples-2027.md) |
| **🔴 שלב 7** | **שאילתות שמורות (Views)** | שימוש בשאילתה שמורה (Q1) כטבלה, יצירת View (`CREATE VIEW`), תת‑שאילתה בתוך ה‑`FROM` | [מאגר שאלות: רמה 7](exam-prep/master-sql-practice.md#🔴-רמה-7-שאילתות-שמורות-ותתשאילתה-בfrom) · [13 sql-views](modules/13-sql-views/) |
| **🟡-🔴 שלב 8** | **שינוי נתונים ומבנה (DML & DDL)** | עדכון שורות (`UPDATE SET WHERE`), מחיקת שורות (`DELETE FROM WHERE`), הוספת רשומות (`INSERT INTO`), הוספה ומחיקת עמודות (`ALTER TABLE`), ומחיקת טבלה (`DROP TABLE`) | [מאגר שאלות: רמה 8](exam-prep/master-sql-practice.md#🟡-🔴-רמה-8-שינוי-נתונים-ומבנה-dml--ddl) · [10 sql-dml](modules/10-sql-dml/) · [11 sql-ddl](modules/11-sql-ddl/) · [12 sql-constraints](modules/12-sql-constraints/) |
| **🎯 שלב 9** | **סימולציית הבחינה הרשמית** | 5 הפורמטים של הבחינה: זיהוי טבלה מתקבלת, השלמת ערכים מספריים, השלמת פקודות (באנגלית), ניתוח פלט (התאמת שאילתה לטבלה), ומפתחות/קשרים ב‑DSD | [מאגר שאלות: רמה 9](exam-prep/master-sql-practice.md#🎯-רמה-9-סימולציית-הבחינה-הרשמית-מגוון-סגנונות) · [תרגול תשפ"ז](exam-prep/practice-2027.md) |

---

## 📂 סדר המודולים המעשיים בתיקיית `modules/`

כל המודולים בתיקייה מסודרים **בסדר כרונולוגי מהקל למתקדם**:

| מספר | תיקיית המודול | הנושא הנלמד |
|:---:|---|---|
| **00** | [00-quick-start](modules/00-quick-start/) | טבלאות, מפתח ראשי (PK), מפתח זר (FK), קשרים 1:1, 1:N, M:N ותרשים DSD |
| **01** | [01-sql-basics](modules/01-sql-basics/) | משפט `SELECT` הראשון, בחירת עמודות, `DISTINCT`, וכינויים (`AS`) |
| **02** | [02-sql-where](modules/02-sql-where/) | הגבלת שליפה עם `WHERE`, אופרטורים, `BETWEEN`, `IN`, `LIKE`, `IS NULL` |
| **03** | [03-sql-order-by](modules/03-sql-order-by/) | מיונים עם `ORDER BY`, `ASC`, `DESC`, ומיון לפי מספר עמודות |
| **04** | [04-sql-functions](modules/04-sql-functions/) | פונקציות סקלריות: מחרוזות (`LENGTH`, `UPPER`, `SUBSTR`), מספרים וחישובים |
| **05** | [05-sql-functions-case-null](modules/05-sql-functions-case-null/) | תנאים בשורה עם `CASE`, טיפול בערכים חסרים עם `COALESCE` ו‑`IFNULL` |
| **06** | [06-sql-aggregates](modules/06-sql-aggregates/) | פונקציות מצרפיות: `COUNT(*)`, `COUNT(col)`, `COUNT(DISTINCT)`, `SUM`, `AVG`, `MIN`, `MAX` |
| **07** | [07-sql-group-by-having](modules/07-sql-group-by-having/) | קיבוץ נתונים לקבוצות `GROUP BY`, וסינון קבוצות לפי פונקציה עם `HAVING` |
| **08** | [08-sql-joins](modules/08-sql-joins/) | צירוף טבלאות ראשון: תחביר פסיק ב‑`WHERE`, ו‑`INNER JOIN ... ON` |
| **09** | [09-sql-joins-advanced](modules/09-sql-joins-advanced/) | צירוף 3 טבלאות (כולל טבלת קישור), וצירוף חיצוני `LEFT JOIN` |
| **10** | [10-sql-dml](modules/10-sql-dml/) | פקודות שינוי נתונים: `INSERT INTO`, `UPDATE SET WHERE`, `DELETE FROM` |
| **11** | [11-sql-ddl](modules/11-sql-ddl/) | הגדרת מבנה: `CREATE TABLE`, `ALTER TABLE` (הוספה/מחיקת עמודה), `DROP TABLE` |
| **12** | [12-sql-constraints](modules/12-sql-constraints/) | אילוצים: `PRIMARY KEY`, `FOREIGN KEY`, `CHECK`, `UNIQUE`, `NOT NULL` |
| **13** | [13-sql-views](modules/13-sql-views/) | שאילתות שמורות (`CREATE VIEW`) ושימוש בשאילתה כטבלה (`Q1` בבחינה) |
| **14** | [14-sql-advanced-objects](modules/14-sql-advanced-objects/) | אובייקטים נוספים: אינדקסים (Indexes) לשיפור ביצועים וסיקוונסים |
| **15** | [15-sql-advanced-users](modules/15-sql-advanced-users/) | ניהול משתמשים והרשאות אבטחה: `GRANT` ו‑`REVOKE` |
| **16** | [16-sql-advanced-transactions](modules/16-sql-advanced-transactions/) | טרנזקציות עסקיות: `COMMIT` ו‑`ROLLBACK` |

---

## 🗄️ בסיסי הנתונים לתרגול

בבחינה מקבלים בסיס נתונים עם **שמות שדות ייחודיים** (ללא צורך בקידומת שם הטבלה).
הקוד של כל בסיסי הנתונים מוכן להעתקה מיידית ולהרצה:

| בסיס נתונים | תיאור | קובץ להעתקה | שימוש מומלץ |
|---|---|:---:|---|
| 🎵 **בית הספר למוזיקה "צלילים"** | 3 טבלאות ראשיות (תלמידים, מורים, רישומים) ו‑3 טבלאות עזר (ערים, כלים, לוקרים). קשר 1:1, 1:N, M:N | [`db/music.sql`](exam-prep/db/music.sql) | **בסיס הנתונים הראשי של הבחינה** ([מאגר תרגול](exam-prep/master-sql-practice.md) ו[מדריך פונקציות](exam-prep/sql-functions-guide.md)) |
| 🔧 **מעבדת "דלתא‑טק"** | תיקוני מכשירים, טכנאים, חלפים ולקוחות | [`db/repairs.sql`](exam-prep/db/repairs.sql) | בחינת אמצע (SELECT, WHERE, ORDER BY) |
| ☕ **בית הקפה "אל‑בלד"** | מלצרים, הזמנות, שולחנות ומנות | [`db/cafe.sql`](exam-prep/db/cafe.sql) | בחינת מתכונת ותרגול מהיר |
| ⚽ **חוגי ספורט עירוניים** | מועדונים, מאמנים ומשתתפים | [`db/clubs.sql`](exam-prep/db/clubs.sql) | בחינה לדוגמה 1 |
| 📚 **ספרייה עירונית** | ספרים, השאלות, קוראים וסניפים | [`db/library.sql`](exam-prep/db/library.sql) | בחינה לדוגמה 2 |
| 🎮 **חנות משחקי מחשב** | משחקים, לקוחות, הזמנות וז'אנרים | [`db/games.sql`](exam-prep/db/games.sql) | בחינה לדוגמה 3 |

---

## ⚠️ 5 מלכודות SQL נפוצות בבחינה שחייבים להכיר

1. **פונקציה מצרפית ב‑WHERE:**
   - ❌ `WHERE HourRate > AVG(HourRate)` — **שגיאה!** אסור לשים פונקציה מצרפית ב‑WHERE.
   - ✅ `WHERE HourRate > (SELECT AVG(HourRate) FROM Teachers)` — תמיד דרך תת‑שאילתה.
2. **`COUNT(*)` מול `COUNT(col)`:**
   - `COUNT(*)` סופר את **כל** השורות כולל אלו שיש בהן NULL.
   - `COUNT(col)` סופר רק שורות שבהן העמודה אינה ריקה (מדלג על NULL).
3. **סוגריים ב‑AND ו‑OR:**
   - האופרטור `AND` קודם ל‑`OR`! תמיד עטפו תנאי `OR` בסוגריים: `WHERE (City = 1 OR City = 2) AND Age > 12`.
4. **בדיקת NULL:**
   - ❌ `WHERE Phone = NULL` — שגוי לחלוטין ולא מחזיר דבר.
   - ✅ `WHERE Phone IS NULL` או `WHERE Phone IS NOT NULL`.
5. **עמודות רגילות לצד פונקציות קיבוץ:**
   - כל שדה שמופיע ב‑`SELECT` ואינו בתוך פונקציה מצרפית **חייב** להופיע ב‑`GROUP BY`.

---

<details>
<summary>📚 <b>פרקי העשרה עיוניים: עיצוב בסיסי נתונים (רשות — אינו נדרש לבחינת השאילתות)</b></summary>

> מודולים אלו שייכים לחלק התיאורטי של תכנית הלימודים (ERD, נרמול ומידול). בבחינת השאילתות **אין צורך לשרטט ERD או לבצע תהליכי נרמול**. החומר נשמר כאן לעיון בלבד:

- [מודול 1 — מבוא ונתונים מול מידע](database-design/module-01-foundations/)
- [מודול 2 — מודל הנתונים](database-design/module-02-data-model/)
- [מודול 3 — תרשימי ERD](database-design/module-03-erd/)
- [מודול 4 — טיפוסי על ותת טיפוסים](database-design/module-04-subtypes-supertypes/)
- [מודול 5 — יחסים בין ישויות](database-design/module-05-relationships/)
- [מודול 6 — נרמול (1NF, 2NF, 3NF)](database-design/module-06-normalization/)
- [מודול 7 — אילוצים עסקיים](database-design/module-07-constraints/)
- [מודול 8 — תפקיד היועץ](database-design/module-08-consultant/)
- [מודול 10 — מעקב אחר שינויים](database-design/module-10-tracking-changes/)
- [מודול 11 — מודלים גנריים](database-design/module-11-generic-models/)
- [מודול 12 — מיפוי מודל לטבלאות](database-design/module-12-mapping/)
- [מודול 14 — מחזור חיי פיתוח מערכת (SDLC)](database-design/module-14-sdlc/)
- [מודול 15 — הצגת פרויקט](database-design/module-15-presentation/)

</details>

---

<div align="center">

**בהצלחה בבחינה! 🚀**

</div>

</div>
