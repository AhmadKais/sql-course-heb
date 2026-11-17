<div dir="rtl">

# 🗄️ SQL מעשי — תרגול לבחינה (שאלון 735911)

### מכללת עתיד | מגמת תקשוב | י"ג–י"ד

> **בלי תיאוריה.** טבלאות, שאילתות, תרגילים ופתרונות.
> כל הטבלאות מוצגות כאן ב‑GitHub, ולכל בסיס נתונים יש **קוד SQL מוכן** שבונה אותו אצלכם בדפדפן — בלי להתקין כלום.

---

## ▶️ מתחילים ב‑3 צעדים

1. פותחים את **[OneCompiler — SQLite](https://onecompiler.com/sqlite)** (או [SQLite Online](https://sqliteonline.com/), שמציג את הטבלאות בצד).
2. נכנסים ל**שיעור**, לוחצים על **📥 הקוד שבונה את בסיס הנתונים**, מעתיקים הכול ומדביקים.
3. מתחת לקוד כותבים את השאילתה ולוחצים **Run**. בודקים מול **מספר השורות הצפוי** ומול **הפתרונות**.

---

## 📚 השיעורים

בכל שיעור: **קוד לטעינה ← הטבלאות ← תחביר קצר ← דוגמאות פתורות ← "מה תחזיר השאילתה?" ← תרגילים ← תרגול נוסף ← פתרונות עם פלט אמיתי**.

| # | שיעור | מה מתרגלים | |
|:-:|---|---|:-:|
| 1 | [SELECT — שליפת עמודות](lessons/01-select/) | עמודות, `*`, `AS`, עמודה מחושבת, `DISTINCT` | [✅](lessons/01-select/solutions.md) |
| 2 | [WHERE — סינון שורות](lessons/02-where/) | `=` `<>` `>` `<`, `AND` / `OR` / `NOT`, סוגריים | [✅](lessons/02-where/solutions.md) |
| 3 | [BETWEEN, IN, LIKE ו‑NULL](lessons/03-between-in-like-null/) | טווח, רשימה, חיפוש טקסט, `IS NULL` | [✅](lessons/03-between-in-like-null/solutions.md) |
| 4 | [ORDER BY ו‑LIMIT](lessons/04-order-by/) | מיון עולה/יורד, לפי כמה עמודות, N הראשונים | [✅](lessons/04-order-by/solutions.md) |
| 5 | [חישובים ופונקציות שורה](lessons/05-row-functions/) | `\|\|`, `LENGTH`, `SUBSTR`, `ROUND`, `CASE`, `IFNULL` | [✅](lessons/05-row-functions/solutions.md) |
| 6 | [פונקציות מצרפיות](lessons/06-aggregates/) | `COUNT` `SUM` `AVG` `MIN` `MAX` | [✅](lessons/06-aggregates/solutions.md) |
| 7 | [GROUP BY ו‑HAVING](lessons/07-group-by-having/) | חישוב לכל קבוצה, סינון קבוצות | [✅](lessons/07-group-by-having/solutions.md) |
| 8 | [צירוף שתי טבלאות](lessons/08-joins/) | PK = FK, פסיק + `WHERE`, `JOIN ... ON` | [✅](lessons/08-joins/solutions.md) |
| 9 | [3 טבלאות ו‑LEFT JOIN](lessons/09-joins-3-tables-left-join/) | טבלה מקשרת (M:N), שורות בלי התאמה | [✅](lessons/09-joins-3-tables-left-join/solutions.md) |
| 10 | [שאילתות מקוננות](lessons/10-subqueries/) | השוואה לממוצע/מקסימום, `IN` / `NOT IN (SELECT ...)` | [✅](lessons/10-subqueries/solutions.md) |
| 11 | [שאילתות שמורות (VIEW)](lessons/11-views/) | `CREATE VIEW`, שימוש ב‑Q1 כמו בטבלה | [✅](lessons/11-views/solutions.md) |
| 12 | [INSERT, UPDATE, DELETE](lessons/12-insert-update-delete/) | הוספה, עדכון ומחיקה של שורות | [✅](lessons/12-insert-update-delete/solutions.md) |
| 13 | [CREATE, ALTER, DROP](lessons/13-create-alter-drop/) | בניית טבלה, מפתחות, אילוצים, הוספה/מחיקת עמודה | [✅](lessons/13-create-alter-drop/solutions.md) |
| 14 | [🎯 סימולציית בחינה](lessons/14-exam-simulation/) | כל הנושאים, על בסיס נתונים חדש | [✅](lessons/14-exam-simulation/solutions.md) |

**250 שאלות ותרגילים**. כל פתרון הורץ ב‑SQLite, וכל הפלטים בדפים הם פלט אמיתי.

---

## 🗄️ בסיסי הנתונים — טבלאות + קוד SQL

לכל בסיס נתונים יש דף עם **כל הטבלאות** (מבנה, מפתחות ונתונים) ועם **הקוד המלא להעתקה**. → [כל בסיסי הנתונים](databases/)

| | בסיס הנתונים | שימוש | |
|:-:|---|---|:-:|
| 🎵 | [בית הספר למוזיקה "צלילים"](databases/music/) | **בסיס הנתונים הראשי של השיעורים** | [`music.sql`](databases/music/music.sql) |
| 🏫 | [בית הספר "עתיד"](databases/school/) | תרגול נוסף בסוף כל שיעור | [`school.sql`](databases/school/school.sql) |
| ⚽ | [חוגי ספורט עירוניים](databases/clubs/) | סימולציית בחינה · בחינה לדוגמה 1 | [`clubs.sql`](databases/clubs/clubs.sql) |
| 📚 | [ספרייה עירונית](databases/library/) | בחינה לדוגמה 2 | [`library.sql`](databases/library/library.sql) |
| 🎮 | [חנות משחקי מחשב](databases/games/) | בחינה לדוגמה 3 | [`games.sql`](databases/games/games.sql) |
| ☕ | [בית הקפה "אל‑בלד"](databases/cafe/) | בחינת מתכונת | [`cafe.sql`](databases/cafe/cafe.sql) |
| 🔧 | [מעבדת "דלתא‑טק"](databases/repairs/) | בחינת אמצע | [`repairs.sql`](databases/repairs/repairs.sql) |
| 🐾 | [מקלט "בית חם"](databases/shelter/) | תרגול חופשי (באנגלית) | [`shelter.sql`](databases/shelter/shelter.sql) |

---

## 🎓 הכנה לבחינה

| | |
|---|---|
| 📋 [דף עזר להדפסה](exam-prep/cheat-sheet.md) | כל התחביר והמלכודות בדף אחד — **מותר להביא לבחינה** |
| 🎯 [48 שאלות בסגנון תשפ"ז](exam-prep/practice-2027.md) | בדיוק כמו בבחינה · [פתרונות](exam-prep/practice-2027-solutions.md) |
| 🏆 [90 שאילתות מדורגות](exam-prep/master-sql-practice.md) | 9 רמות קושי · [פתרונות](exam-prep/master-sql-practice-solutions.md) |
| 💡 [20 דוגמאות פתורות](exam-prep/examples-2027.md) | איך חושבים על שאלה, צעד אחרי צעד |
| 🧮 [מדריך פונקציות](exam-prep/sql-functions-guide.md) | `COUNT` / `SUM` / `AVG` / `MIN` / `MAX` + 25 תרגילים |
| 📄 [מבנה הבחינה וסוגי השאלות](exam-prep/README.md) | מה יש בשאלון 735911, ומה אין |
| 🖨️ [דפים להדפסה (PDF)](handouts/) | בחינת אמצע, בחינת מתכונת, דף עבודה |

---

## ⚠️ 5 המלכודות הנפוצות

| ❌ שגוי | ✅ נכון |
|---|---|
| `WHERE Phone = NULL` | `WHERE Phone IS NULL` |
| `WHERE HourRate > AVG(HourRate)` | `WHERE HourRate > (SELECT AVG(HourRate) FROM Teachers)` |
| `WHERE City = 1 OR City = 2 AND Age > 12` | `WHERE (City = 1 OR City = 2) AND Age > 12` |
| `SELECT Name, COUNT(*) FROM T` | `SELECT Name, COUNT(*) FROM T GROUP BY Name` |
| `WHERE COUNT(*) > 2` | `GROUP BY ... HAVING COUNT(*) > 2` |

---

<details>
<summary>🛠️ <b>למורה: איך מעדכנים את החומר</b></summary>

כל דפי השיעורים ודפי בסיסי הנתונים **נוצרים אוטומטית**. לא עורכים אותם ביד:

- התוכן של כל שיעור (שאלות + פתרונות SQL) נמצא ב‑[`tools/lessons/`](tools/lessons/), קובץ לכל שיעור.
- הנתונים נמצאים בקובצי ה‑`.sql` שב‑[`databases/`](databases/).
- אחרי שינוי מריצים: `python tools/build.py`. הסקריפט מריץ כל שאילתה ב‑SQLite ומעדכן את הטבלאות, מספרי השורות והפלטים.

החומר העיוני הקודם (ERD, נרמול, SDLC, 17 המודולים הארוכים) נשמר בהיסטוריה של git, בתגית [`before-practical-reform`](https://github.com/AhmadKais/sql-course-heb/tree/before-practical-reform).

</details>

<div align="center">

**בהצלחה בבחינה! 🚀**

</div>

</div>
