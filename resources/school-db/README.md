<div dir="rtl">

# 🏫 בסיס הנתונים לתרגול בכיתה — בית הספר "עתיד"

> **למה זה קיים?** בסוף התרגילים של **כל** שיעור SQL יש קטע **💪 תרגול בכיתה** — 12 שאלות שליפה שרצות על בסיס הנתונים הזה. הוא נשאר **אותו בסיס נתונים מהשיעור הראשון ועד האחרון**, והשאלות הן שמתקדמות בקושי.
>
> **למה לא מקלט "בית חם"?** כי את המקלט התלמידים כבר מכירים — הפתרונות נמצאים בקובץ שלידם. כאן הנתונים חדשים, אז השאלות דורשות **לקרוא את הסכמה ולחשוב**, בדיוק כמו בבחינה.
>
> **למה אותו בסיס נתונים בכל השיעורים?** כדי שבכיתה לא יבזבזו את עשר הדקות הראשונות על להבין סכמה חדשה. טוענים פעם אחת, ומתחילים לכתוב.

---

## איך מתחילים — 30 שניות

1. פתחו את **[OneCompiler (SQLite)](https://onecompiler.com/sqlite)**
2. מחקו את מה שיש בחלון הקוד (`Ctrl+A` ואז `Delete`)
3. פתחו את [`school.sql`](school.sql) — או [פתיחה להעתקה](https://raw.githubusercontent.com/AhmadKais/sql-course-heb/main/resources/school-db/school.sql) — העתיקו **את כל הקובץ**, והדביקו
4. לחצו **Run**. אם ב‑**Output** מופיע `students_loaded = 18` — הכול טעון
5. **מתחת** לקוד שהדבקתם, כתבו את השאילתה שלכם ולחצו Run שוב

> 📅 **תאריך הייחוס בכל השאלות: `'2026-09-21'`** — שלושה שבועות לתוך שנת הלימודים 2026/27. השתמשו בו במקום `DATE('now')`, אחרת הפלט לא יתאים לפתרונות.
>
> ⚠️ שמות הטבלאות והעמודות כתובים בסגנון הבחינה: `Students.FirstName`, `Grades.Grade`. טקסט בין גרשיים.

---

## מה יש בפנים

</div>

```text
+--------+          +----------+          +---------+          +--------+
| CITIES |--1:M-->--| TEACHERS |--1:M-->--| COURSES |--1:M-->--| GRADES |
| 6 rows |          | 7 rows   |          | 7 rows  |          | 60 rows|
+---+----+          +-----+----+          +---------+          +----+---+
    |                     |                                         |
   1:M                   1:M  (homeroom teacher)                   M:1
    |                     |                                         |
    v                     v                                         |
+---+------+        +-----+-----+                                   |
| STUDENTS |--M:1-->| CLASSES   |                                   |
| 18 rows  |        | 5 rows    |                                   |
+---+---+--+        +-----------+                                   |
    |   |                                                           |
    |   +-------- 1:M  (Grades.StudentId) ---------------------------+
   1:M
    |
    v
+---+--------+      GRADES is the M:M table between
| ABSENCES   |      STUDENTS and COURSES. Its key is
| 16 rows    |      (StudentId, CourseCode, Term).
+------------+
```

<div dir="rtl">

| הטבלה | מה יש בה | למה היא מעניינת לתרגול |
|--------|-----------|------------------------|
| `Cities` | 6 ערים | טבלת קוד קטנה — ראשונה ל‑`JOIN` |
| `Teachers` | 7 מורים: מקצוע, תאריך תחילת עבודה, שכר | `Salary` למספרים · `HireDate` לתאריכים · `Phone` הוא `NULL` אצל שניים |
| `Classes` | 5 כיתות: י1, י2, יא1, יא2, יב1 | `Grade` (שכבה) לקיבוץ · ⭐ **ל‑יא2 אין `RoomNumber`** |
| `Courses` | 7 מקצועות + שעות שבועיות | ⭐ **ל"סדנת פרויקטים" אין מורה** (`TeacherCode IS NULL`) |
| `Students` | 18 תלמידים | `NULL` ב‑`BirthDate`, `CityCode`, `ClassCode`, `Phone` — לתרגול `IS NULL` ו‑`COALESCE` |
| `Grades` | 60 ציונים, שתי מחציות | ⭐ **שני ציונים הם `NULL`** (לא נבחן) — ו‑`AVG` מתעלם מהם · טווח 39–100 ל‑`CASE` |
| `Absences` | 16 היעדרויות בספטמבר 2026 | `Excused` (0/1) · `Reason` הוא `NULL` כשההיעדרות לא מאושרת |

---

## נסו עכשיו — חמש שאילתות ראשונות

</div>

```sql
-- 1. All the students in class 101
SELECT Students.FirstName, Students.LastName
FROM   Students
WHERE  Students.ClassCode = 101;

-- 2. Teachers, highest salary first
SELECT Teachers.FirstName, Teachers.Salary
FROM   Teachers
ORDER  BY Teachers.Salary DESC;

-- 3. Every student with the name of their class (your first JOIN)
SELECT Students.FirstName, Classes.ClassName
FROM   Students, Classes
WHERE  Students.ClassCode = Classes.ClassCode;

-- 4. How many students in each class? (your first GROUP BY)
SELECT Students.ClassCode, COUNT(*) AS HowMany
FROM   Students
GROUP  BY Students.ClassCode;

-- 5. Which student has the highest average?
SELECT Grades.StudentId, ROUND(AVG(Grades.Grade), 1) AS Average
FROM   Grades
GROUP  BY Grades.StudentId
ORDER  BY Average DESC
LIMIT  3;
```

<div dir="rtl">

---

## חמישה דברים מוסתרים בנתונים

הם שם בכוונה. השאלות בשיעורים יתנגשו בהם — וזו המטרה.

| מה | איפה | למה זה שם |
|-----|-------|-----------|
| **לינא חמוד** נרשמה ב‑10 בספטמבר ו**טרם שובצה לכיתה** | `Students.ClassCode IS NULL` | `JOIN` רגיל "מעלים" אותה · `LEFT JOIN` מחזיר אותה. גם: אין לה אף ציון |
| **ל"סדנת פרויקטים" אין מורה** | `Courses.TeacherCode IS NULL` | `COALESCE` · `LEFT JOIN` לכיוון `Teachers` |
| **סמיר אבו‑ראס לא מלמד אף מקצוע** | `Teachers` ללא התאמה ב‑`Courses` | הכיוון ההפוך: `LEFT JOIN … WHERE … IS NULL` |
| **שני ציונים הם `NULL`** (מאיה בהיסטוריה, כרים באנגלית) | `Grades.Grade IS NULL` | `COUNT(*)` מול `COUNT(Grade)` · `AVG` מתעלם מ‑`NULL` ולא מחשיב אותו כאפס |
| **לליאור לוי אין עיר ולסאלי חסון אין תאריך לידה** | `Students.CityCode` · `Students.BirthDate` | חישוב גיל מחזיר `NULL` · `JOIN` לערים מפספס אותו |

---

## מה מחכה בפנים — לפי השיעור

| השיעור | השאלה | הרמז |
|--------|--------|------|
| 16 | מי כל התלמידים? אילו **מקצועות** יש? | `SELECT` · `DISTINCT` |
| 17 | אילו תלמידים **בלי טלפון**? | `Phone IS NULL` |
| 18 | מי התלמיד **הצעיר ביותר**? | `ORDER BY BirthDate DESC` — ומה עם ה‑`NULL`? |
| 19 | כמה **שנים** לכל תלמיד, נכון ל‑`'2026-09-21'`? | פונקציות תאריך |
| 20 | תייגו כל ציון: "מעולה" / "עובר" / "נכשל" | `CASE` |
| 21 | כל ציון עם **שם התלמיד ושם המקצוע** | שני `JOIN`‑ים |
| 22 | אילו מורים **לא מלמדים** אף מקצוע? | `LEFT JOIN … IS NULL` |
| 23 | מה **הממוצע** בבית הספר? כמה ציונים **חסרים**? | `AVG` · `COUNT(*)` מול `COUNT(Grade)` |
| 24 | איזו **שכבה** הכי חלשה במתמטיקה? | `GROUP BY … HAVING` + תת‑שאילתה |
| 25 | רשמו תלמיד חדש · העלו ציון · מחקו היעדרות | `INSERT` · `UPDATE` · `DELETE` |
| 26 | בנו טבלת `Trips` לטיולים שנתיים | `CREATE TABLE` · `ALTER TABLE` |
| 27 | ⭐ מה היה קורה אילו `Grade` היה `CHECK (Grade BETWEEN 0 AND 100)`? | נסו להכניס 120 — ותראו |
| 28 | בנו `View` של "תלמידים בסיכון" | `CREATE VIEW` |
| 32 | העלו ציון, ואז `ROLLBACK` | טרנזקציות |

---

<div align="center">

**[🧭 מסלול הלימוד](../../LEARNING-PATH.md)** · **[📋 קובצי ה‑SQL](../../SQL-FILES.md)** · **[🏠 דף הקורס](../../)**

</div>

</div>
