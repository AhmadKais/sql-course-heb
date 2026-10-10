<div dir="rtl">

# מודול 19 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 כל הפלטים אמיתיים, נכון ל‑`'2026-09-21'`. **ב‑SQLite, `FLOOR` מחזיר `5.0`; `CAST(… AS INTEGER)` מחזיר `5`.** שניהם נכונים — הפתרונות משתמשים בשניהם.

---

## ✅ תרגיל 1 — טקסט

</div>

```sql
-- a
SELECT UPPER(name) FROM animal;

-- b   Ruti ALMOG, Noa PERETZ, Amir LEVI, Dr. Ron LEVI ...
SELECT first_name || ' ' || UPPER(last_name) AS label FROM person;

-- c
SELECT name, LENGTH(name) AS letters FROM animal;

-- d   Lun, Sim, Roc, Mit, Bel ...
SELECT name, SUBSTR(name, 1, 3) AS first_three FROM animal;

-- e   a, a, y, i, a ...
SELECT name, SUBSTR(name, -1) AS last_char FROM animal;

-- f   0521111111, 0542222222 ...   (Omer: NULL -> NULL)
SELECT first_name, REPLACE(phone, '-', '') AS phone_digits FROM person;
```

<div dir="rtl">

### ז. `REPLACE(name, 'a', '@')` — ומה עם `'A'`?

</div>

```text
name   replaced
-----  --------
Luna   Lun@
Simba  Simb@
Nala   N@l@      <- both lowercase a's replaced
Max    M@x
```

<div dir="rtl">

**`'A'` גדולה לא מוחלפת.** `REPLACE` רגיש לאותיות — כמו `=`. אין `'A'` בתחילת שם בבסיס הנתונים שלנו, אבל `REPLACE('Anna', 'a', '@')` היה נותן `Ann@`, לא `@nn@`. **לכל האותיות:** `REPLACE(LOWER(name), 'a', '@')`.

---

## ✅ תרגיל 2 — חיפוש בטקסט

</div>

```sql
-- a   0 for most; Rocky 2, Tom 2, Coco 2, Zoe 2, Shadow 5
SELECT name, INSTR(name, 'o') AS pos FROM animal;

-- b   Rocky, Tom, Coco, Zoe, Shadow  (INSTR > 0 means "found")
SELECT name FROM animal WHERE INSTR(name, 'o') > 0;

-- c   Luna, Lily  -- works for 'luna', 'LUNA', 'Luna'
SELECT name FROM animal WHERE UPPER(SUBSTR(name, 1, 1)) = 'L';

-- d   Simba, Rocky, Mitzi, Bella, Oscar, Daisy, Felix, Bunny  (8)
SELECT name FROM animal WHERE LENGTH(name) = 5;
```

<div dir="rtl">

### ה. מתחיל ומסתיים באותה אות

</div>

```sql
SELECT name
FROM   animal
WHERE  UPPER(SUBSTR(name, 1, 1)) = UPPER(SUBSTR(name, -1));
-- -> 0 rows
```

<div dir="rtl">

**אפס שורות — וזו התשובה הנכונה.** אין חיה כזאת בבסיס הנתונים. (Nala? N…a. Oscar? O…r. לא.)

> 💡 **איך יודעים שהשאילתה נכונה ולא שבורה?** בודקים עם ערך מומצא: `SELECT UPPER(SUBSTR('Anna',1,1)) = UPPER(SUBSTR('Anna',-1));` ⟵ `1`. השאילתה עובדת; פשוט אין התאמות. **אפס שורות הוא תוצאה, לא שגיאה.**

---

## ✅ תרגיל 3 — מספרים

</div>

```sql
-- a   19, 4, 31, 3, 28 ...
SELECT name, ROUND(weight_kg) AS kg_whole FROM animal;

-- b   40.7, 9.24, 68.2, 6.82 ...
SELECT name, ROUND(weight_kg * 2.2, 2) AS lb FROM animal;

-- c   354, 236, 236, 295, 118, 236, 472, 472, 177
SELECT adoption_id, ROUND(fee_paid * 1.18, 2) AS with_vat FROM adoption;

-- d
SELECT expense_id, ROUND(amount / 12, 2) AS per_month FROM expense;

-- e   Simba, Mitzi, Tom, Max, Thumper, Oscar, Lily, Kiwi, Felix, Shadow  (10)
SELECT name FROM animal WHERE animal_id % 2 = 0;

-- g   equal only when the weight is already whole: Rocky 31.0, Zoe 22.0, Felix 5.0
SELECT name, weight_kg, CEIL(weight_kg), FLOOR(weight_kg)
FROM   animal WHERE CEIL(weight_kg) = FLOOR(weight_kg);
```

<div dir="rtl">

### ו. `0.1 + 0.2 = 0.3`

</div>

```sql
SELECT 0.1 + 0.2 = 0.3;             -- 0  (FALSE!)
SELECT ROUND(0.1 + 0.2, 2) = 0.3;   -- 1  (TRUE)
```

<div dir="rtl">

המחשב לא יכול לייצג `0.1` בדיוק — התוצאה היא `0.30000000000000004`. **ב‑`WHERE`, "כמעט" זה FALSE.** לכן `ROUND(…, 2)` בכל השוואה כספית.

---

## ✅ תרגיל 4 — תאריכים: חילוץ

</div>

```sql
-- a
SELECT expense_date, STRFTIME('%Y', expense_date) AS year FROM expense;

-- b
SELECT expense_date, STRFTIME('%Y-%m', expense_date) AS year_month FROM expense;

-- c   03, 07, 11, 01, 05 ...
SELECT name, STRFTIME('%m', birth_date) AS born_month FROM animal WHERE birth_date IS NOT NULL;

-- d   1200 (10/03), 1790 (15/03)
SELECT expense_date, amount FROM expense WHERE STRFTIME('%Y-%m', expense_date) = '2024-03';

-- f   10/05/2023, 15/06/2023, 10/02/2024 ...
SELECT adoption_id, STRFTIME('%d/%m/%Y', adoption_date) AS il_date FROM adoption;
```

<div dir="rtl">

### ה. `= 2024` בלי גרשיים

</div>

```sql
SELECT COUNT(*) FROM expense WHERE STRFTIME('%Y', expense_date) = 2024;     -- 0
SELECT COUNT(*) FROM expense WHERE STRFTIME('%Y', expense_date) = '2024';   -- 19
```

<div dir="rtl">

**`STRFTIME` מחזיר טקסט.** `'2024'` (טקסט) ≠ `2024` (מספר). אפס שורות, בלי שגיאה. **גרשיים.**

---

## ✅ תרגיל 5 — תאריכים: חשבון

</div>

```sql
-- a   Zoe 3916, Rex 3331, Bella 3061, Felix 2776 ...
SELECT name, JULIANDAY('2026-09-21') - JULIANDAY(birth_date) AS days
FROM   animal WHERE birth_date IS NOT NULL ORDER BY days DESC;

-- b   Zoe 10, Rex 9, Bella 8, Felix 7, Rocky 6, Tom 6, Daisy 6, Luna 5, Shadow 5 ... Coco/Lily/Kiwi NULL
SELECT name, FLOOR((JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25) AS age
FROM   animal ORDER BY age DESC;

-- c   same numbers, shown as 10 instead of 10.0
SELECT name, CAST((JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25 AS INTEGER) AS age
FROM   animal ORDER BY age DESC;

-- d
SELECT vaccination_id, given_date, DATE(given_date, '+12 months') AS next_due FROM vaccination;

-- e   2023-06-09, 2023-07-15, 2024-03-11 ...
SELECT adoption_id, adoption_date, DATE(adoption_date, '+30 days') AS visit_due FROM adoption;

-- f   1287 days
SELECT JULIANDAY('2026-09-21') - JULIANDAY(intake_date) AS days FROM intake WHERE intake_id = 1;
```

<div dir="rtl">

### ז. חיסונים שפג תוקפם

</div>

```sql
SELECT vaccination_id, animal_id, given_date, DATE(given_date, '+12 months') AS due
FROM   vaccination
WHERE  DATE(given_date, '+12 months') < '2026-09-21';
-- -> 28 rows.  ALL of them.
```

<div dir="rtl">

**כל 28 החיסונים פגי תוקף.** למה? כי הנתונים מסתיימים ב‑2025‑05‑30, והיום הוא 2026‑09‑21 — עברה יותר משנה. **זה לא באג בשאילתה; זה מה שהנתונים אומרים.**

> 🔑 **כשהשאילתה מחזירה הכול — עצרו ושאלו למה.** לפעמים זו שגיאה (`WHERE` שנפל). כאן זו **המציאות**: מקלט שלא חידש חיסונים שנה. במקלט אמיתי — זה משבר.

---

## ✅ תרגיל 6 — פונקציות ב‑WHERE וב‑ORDER BY

</div>

```sql
-- a   Luna -- regardless of case or trailing spaces
SELECT name FROM animal WHERE UPPER(TRIM(name)) = 'LUNA';

-- b   Luna, Rocky, Bella, Tom, Zoe, Rex, Daisy, Felix, Shadow  (9)
SELECT name FROM animal
WHERE  (JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25 > 5;

-- c   Zoe first ... Nala last, then Coco/Lily/Kiwi (NULL -> DESC puts them LAST in SQLite)
SELECT name, birth_date FROM animal
ORDER  BY (JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25 DESC;

-- d   Mizrahi 7, Peretz 6, Shalev 6, Almog 5, ... Bar 3
SELECT last_name, LENGTH(last_name) AS len FROM person ORDER BY LENGTH(last_name) DESC;

-- e   2024-01: 1850, 960, 420 | 2024-02: 880, 650, 310 | ...
SELECT STRFTIME('%Y-%m', expense_date) AS ym, amount
FROM   expense ORDER BY ym, amount DESC;
```

<div dir="rtl">

### ו. `ROUND` במקום `FLOOR` ב‑ב'

</div>

```text
FLOOR > 5:   Rocky 6, Bella 8, Tom 6, Zoe 10, Rex 9, Daisy 6, Felix 7        (7 animals)
ROUND > 5:   + Luna 6  (she is 5.52 -> ROUND gives 6)                        (8 animals)
             and Zoe shows 11, Felix 8, Rocky 7 -- all rounded UP
```

<div dir="rtl">

**לונה נוספה.** היא בת 5.52 — `FLOOR` אומר 5 (נכון), `ROUND` אומר 6 (שגוי). **גיל לא מעגלים.** מי שיוצר רשימת "מעל גיל 5" עם `ROUND` — מכניס חיות שעוד לא הגיעו לשם.

---

## ✅ תרגיל 7 — NULL ופונקציות

| | השאילתה | התוצאה לחיות בלי ערך |
|---|---|---|
| **א** | `LENGTH(breed)` | **NULL** — לא 0 |
| **ב** | `UPPER(chip_number)` | **NULL** |
| **ג** | הגיל של Coco, Lily, Kiwi | **NULL** — לא 0. וזה נכון: לא ידוע |

### ד+ה. `LENGTH(breed) = 0`

</div>

```sql
SELECT COUNT(*) FROM animal WHERE LENGTH(breed) = 0;                    -- 0 rows!
SELECT name FROM animal WHERE breed IS NULL OR LENGTH(breed) = 0;       -- Mitzi, Nala, Lily, Bunny
```

<div dir="rtl">

**0 שורות ב‑ד'** — כי `LENGTH(NULL)` הוא NULL, ו‑`NULL = 0` הוא NULL, והשורה נופלת. הגזעים החסרים הם NULL, לא מחרוזת ריקה. **`IS NULL` תופס אותם; `LENGTH` לא.**

### ו. `birth_date || ' (estimated)'` ל‑Coco

**NULL.** כל השורה ריקה — לא `' (estimated)'`, כלום.

**מה צריך:** פונקציה שאומרת *"אם NULL — תן `'unknown'`, אחרת תן את הערך"*. זו `COALESCE(birth_date, 'unknown')` — **מודול 20**. היא הפונקציה שפותרת את כל בעיות ה‑NULL שנערמו מאז מודול 16.

---

## ✅ תרגיל 8 — שילובים

</div>

```sql
-- a   R.A., N.P., A.L., D.L. ...
SELECT first_name, last_name,
       SUBSTR(first_name, 1, 1) || '.' || SUBSTR(last_name, 1, 1) || '.' AS initials
FROM   person;

-- b   Luna, Simba, Rocky ... (correct even if stored as LUNA or luna)
SELECT UPPER(SUBSTR(name, 1, 1)) || LOWER(SUBSTR(name, 2)) AS proper FROM animal;

-- c   ruti.almog@shelter.org, noa.peretz@shelter.org ...
SELECT LOWER(first_name || '.' || last_name || '@shelter.org') AS email FROM person;

-- d   "dry food, ...", "x-ray + me...", "electricit..."
SELECT SUBSTR(description, 1, 10) || '...' AS short_desc FROM expense;

-- e
SELECT name || ', '
       || CAST((JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25 AS INTEGER)
       || ' years, ' || weight_kg || ' kg'   AS line
FROM   animal;
-- -> "Luna, 5 years, 18.5 kg" ... and Coco: NULL (the whole line vanishes)
```

<div dir="rtl">

> 💡 **ב‑ג':** שימו לב ל‑`dr. ron.levi@shelter.org` — הנקודה והרווח מ‑`Dr. Ron` נכנסו למייל. **הנתונים מלוכלכים, והפונקציה עשתה בדיוק מה שביקשו.** ניקוי אמיתי היה דורש `REPLACE(REPLACE(first_name, 'Dr. ', ''), ' ', '')`. פונקציות לא יודעות מה "נכון" — רק מה ביקשתם.

### ו. ⭐⭐ ימים עד החיסון הבא

</div>

```sql
SELECT   vaccination_id, animal_id,
         DATE(given_date, '+12 months')                                            AS due,
         CAST(JULIANDAY(DATE(given_date, '+12 months')) - JULIANDAY('2026-09-21') AS INTEGER) AS days_left
FROM     vaccination
ORDER BY days_left DESC;
```

```text
vaccination_id  animal_id  due         days_left
--------------  ---------  ----------  ---------
28              3          2026-05-30  -114        <- the "freshest" is 114 days overdue
25              20         2026-03-12  -193
26              20         2026-03-12  -193
24              19         2026-02-25  -208
...
```

<div dir="rtl">

**כולם שליליים.** קוראים מבפנים: `DATE(…)` ⟵ מועד החידוש; `JULIANDAY` על שניהם ⟵ הפרש ימים; `CAST` ⟵ מספר שלם. **שלוש פונקציות מקוננות** — ובכל שלב אפשר להריץ ולבדוק.

---

## ✅ תרגיל 9 — מצאו את הבאג

| | אמורה | עושה | התיקון |
|---|-------|-------|---------|
| **a** | 3 תווים ראשונים | `Lu` — **2 תווים**. מיקום 0 "נספר" כריק | `SUBSTR(name, 1, 3)` |
| **b** | גיל בשנים | `ROUND` ⟵ 5.9 הופך ל‑6; `365` ⟵ שגיאת יום כל 4 שנים | `FLOOR(… / 365.25)` |
| **c** | הוצאות 2024 | **0 שורות** — טקסט מול מספר | `= '2024'` |
| **d** | גזע ריק | **0 שורות** — `LENGTH(NULL)` הוא NULL | `breed IS NULL` |
| **e** | פאונד, 2 ספרות | `ROUND(weight_kg) * 2.2` — עיגול **לפני** הכפל: Luna 41.8 במקום 40.7 | `ROUND(weight_kg * 2.2, 2)` |
| **f** | חיסון הבא | ⚠️ `'2023-03-20' + 365` = **`2388`** — SQLite הפך את הטקסט ל‑2023 והוסיף 365 | `DATE(given_date, '+365 days')` |
| **g** | לונה, כל אות | **0 שורות** — `UPPER(name)` הוא `'LUNA'`, לא `'Luna'` | `= 'LUNA'` |

> 🔑 **f היא המסוכנת ביותר.** לא שגיאה, לא NULL — **מספר שנראה סביר** (2388) ואומר כלום. SQLite לקח את `'2023-03-20'`, קרא ממנו את `2023`, והוסיף. **על תאריכים — פונקציות תאריך. תמיד.**

---

## ✅ תרגיל 10 — הדוחות של רותי

### א. כרטיס החיה

</div>

```sql
SELECT   UPPER(name)                                                          AS card_name,
         CAST((JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25 AS INTEGER) AS age,
         ROUND(weight_kg, 1)                                                  AS kg,
         STRFTIME('%d/%m/%Y', birth_date)                                     AS born
FROM     animal
WHERE    status = 'available'
ORDER BY UPPER(name);
```

```text
card_name  age  kg    born
---------  ---  ----  ----------
BUNNY      2    1.5   01/01/2024
COCO            0.1               <- unknown -> NULL (correct, not pretty: module 20)
FELIX      7    5.0   14/02/2019
LILY            3.4
MITZI      3    3.1   10/01/2023
OSCAR      4    5.5   12/12/2021
REX        9    38.7  08/08/2017
ROCKY      6    31.0  20/11/2019
SHADOW     5    25.1  30/06/2021
```

<div dir="rtl">

### ב. חידוש ב‑3 החודשים הקרובים

</div>

```sql
SELECT   vaccination_id, animal_id,
         DATE(given_date, '+12 months') AS due
FROM     vaccination
WHERE    DATE(given_date, '+12 months') BETWEEN '2026-09-21' AND DATE('2026-09-21', '+90 days');
-- -> 0 rows
```

<div dir="rtl">

**אפס — כי כולם כבר פגי תוקף** (תרגיל 5ז'). השאילתה נכונה; אין מה לחדש "בקרוב" כי הכול היה צריך להתחדש **מזמן**. הדוח האמיתי שרותי צריכה:

</div>

```sql
-- overdue, most urgent (longest overdue) first
SELECT   vaccination_id, animal_id,
         DATE(given_date, '+12 months') AS due,
         CAST(JULIANDAY('2026-09-21') - JULIANDAY(DATE(given_date, '+12 months')) AS INTEGER) AS days_overdue
FROM     vaccination
WHERE    DATE(given_date, '+12 months') < '2026-09-21'
ORDER BY days_overdue DESC;
```

<div dir="rtl">

> 🎓 **הלקח:** רותי שאלה שאלה אחת; הנתונים ענו על אחרת. **שאילתה טובה מגלה מה הלקוחה באמת צריכה לדעת** — ופה זה "הכול פג, מה הכי דחוף".

### ג. זמן המתנה עד אימוץ

**❌ לא אפשרי עדיין.** `intake_date` ב‑`intake`, `adoption_date` ב‑`adoption` — **שתי טבלאות**. חיבור ביניהן = `JOIN`, **מודול 21**.

**מה כן אפשר:** לחשב לכל אימוץ **כמה זמן עבר מאז** — עמודה אחת, טבלה אחת:

</div>

```sql
SELECT adoption_id, animal_id,
       CAST(JULIANDAY('2026-09-21') - JULIANDAY(adoption_date) AS INTEGER) AS days_since
FROM   adoption
WHERE  returned_date IS NULL;
```

<div dir="rtl">

### ד. הוצאות לפי חודש

</div>

```sql
SELECT   STRFTIME('%Y-%m', expense_date) AS month, category, amount
FROM     expense
ORDER BY month, amount DESC;
```

<div dir="rtl">

**רואים** שינואר 2024 ויולי 2024 יקרים — אבל **לא סוכמים**. "כמה סה"כ בכל חודש" = `GROUP BY month` + `SUM(amount)`, **מודול 24**. עכשיו יש לכם את `STRFTIME('%Y-%m', …)` — זה בדיוק מפתח הקיבוץ שתצטרכו.

### ה. ותק מתנדבות

</div>

```sql
SELECT   first_name || ' ' || last_name AS volunteer,
         CAST((JULIANDAY('2026-09-21') - JULIANDAY(joined_date)) / 365.25 AS INTEGER) AS years
FROM     person
WHERE    role = 'volunteer'
ORDER BY years DESC;
```

```text
volunteer    years
-----------  -----
Ruti Almog   13
Noa Peretz   7
Amir Levi    4
Tamar Golan  2
```

<div dir="rtl">

**הכוכבית:** *"אם מעל 5 — `*`, אחרת ריק"* — זו **החלטה בתוך השאילתה**, וזה `CASE WHEN years > 5 THEN '*' ELSE '' END`. **מודול 20.** בינתיים: הוותק מחושב, ורותי רואה בעיניים מי מעל 5.

---

<div align="center">

### 🎯 סיימתם את מודול 19 — ואת יחידה 3!

יש לכם את הארגז המלא: טקסט, מספרים, תאריכים.
במודול הבא — **`COALESCE` ו‑`CASE`**: לתת ל‑NULL ערך, ולקבל החלטות בתוך השאילתה.

---

### ➡️ [מודול 20 — SQL: פונקציות 2](../module-20-sql-functions-2/)

</div>

---

<div align="center">

**🧭 ניווט המודול**

</div>

| 📖 [חזרה למודול](README.md) | ❓ [שאלות ותשובות](questions.md) | ✏️ [לתרגילים](exercises.md) | 🏠 [דף הקורס](../../) |
|---|---|---|---|

</div>

<!-- w3schools:start -->
<div dir="rtl">

---

## 🌐 תרגול ב‑W3Schools: פתרונות

> כל השאילתות כאן הורצו ב‑W3Schools. מספר הרשומות הוא מה שהאתר מחזיר.

**W1.**

```sql
SELECT UPPER(Customers.CustomerName) AS Name, LEN(Customers.CustomerName) AS NameLength FROM Customers;
```

**91** רשומות. השורה הראשונה: `ALFREDS FUTTERKISTE · 19`


</div>
<!-- w3schools:end -->

<!-- classroom:start -->
<div dir="rtl">

---

## 💪 תרגול בכיתה — פתרונות

> 🏫 על [`school.sql`](../../resources/school-db/). כל הפלטים כאן **אמיתיים** — כל שאילתה הורצה על בסיס הנתונים, נכון לתאריך הייחוס `'2026-09-21'`.

</div>

```text
Cities    (CityCode, CityName)
Teachers  (TeacherCode, FirstName, LastName, Subject, HireDate, Salary, CityCode, Phone)
Classes   (ClassCode, ClassName, Grade, TeacherCode, RoomNumber)
Courses   (CourseCode, CourseName, TeacherCode, WeeklyHours)
Students  (StudentId, FirstName, LastName, ClassCode, Gender, BirthDate, CityCode, EnrollDate, Phone)
Grades    (StudentId, CourseCode, Term, Grade)          -- PK: StudentId + CourseCode + Term
Absences  (AbsenceId, StudentId, AbsenceDate, Excused, Reason)
```

<div dir="rtl">

> 💡 כל הפלטים נכונים ל‑`'2026-09-21'`.

</div>

```sql
-- ש1
SELECT Students.FirstName, LENGTH(Students.FirstName) AS Letters FROM Students
ORDER BY Letters DESC, Students.FirstName LIMIT 6;

-- ש2
SELECT Students.FirstName || ' ' || SUBSTR(Students.LastName, 1, 1) || '.' AS ShortName FROM Students;

-- ש3
SELECT Students.FirstName, REPLACE(Students.Phone, '-', '') AS Digits FROM Students;

-- ש4
SELECT DISTINCT SUBSTR(Students.Phone, 1, 3) AS Prefix FROM Students;

-- ש5
SELECT Teachers.Subject, UPPER(Teachers.Subject) AS Upper1, LENGTH(Teachers.Subject) AS Len FROM Teachers;

-- ש6
SELECT Teachers.LastName, Teachers.Salary, ROUND(Teachers.Salary * 0.88, 2) AS NetSalary FROM Teachers;

-- ש7
SELECT Grades.StudentId, Grades.Grade, Grades.Grade - 75 AS Diff, ABS(Grades.Grade - 75) AS Gap
FROM   Grades WHERE Grades.CourseCode = 13 ORDER BY Gap;

-- ש8
SELECT Students.FirstName, Students.BirthDate,
       CAST((JULIANDAY('2026-09-21') - JULIANDAY(Students.BirthDate)) / 365.25 AS INTEGER) AS Age
FROM   Students ORDER BY Age;

-- ש9
SELECT Students.FirstName, STRFTIME('%Y', Students.BirthDate) AS BirthYear FROM Students;

-- ש10
SELECT Teachers.LastName, Teachers.HireDate,
       CAST((JULIANDAY('2026-09-21') - JULIANDAY(Teachers.HireDate)) / 365.25 AS INTEGER) AS Seniority
FROM   Teachers ORDER BY Seniority DESC;

-- ש11
SELECT Absences.AbsenceId, Absences.AbsenceDate,
       JULIANDAY('2026-09-21') - JULIANDAY(Absences.AbsenceDate) AS DaysAgo
FROM   Absences ORDER BY DaysAgo DESC LIMIT 5;

-- ש12  השגויה, ואחריה הנכונה
SELECT Students.FirstName, Students.BirthDate, Students.BirthDate + 365 AS Wrong FROM Students LIMIT 4;
SELECT Students.FirstName, Students.BirthDate, DATE(Students.BirthDate, '+365 days') AS Right1 FROM Students LIMIT 4;
```

<div dir="rtl">

**ש1.** שלושה שמות באורך 5. התיקו נשבר לפי שם (`, Students.FirstName`) — בלעדיו הסדר ביניהם לא מובטח.

<figure dir="ltr" class="dbtable">

| FirstName | Letters |
|:---:|:---:|
| דניאל | 5 |
| ליאור | 5 |
| ראניה | 5 |
| איתי | 4 |
| ג'וד | 4 |
| הדיל | 4 |

</figure>

> 🔎 `ג'וד` באורך 4 — הגרש נספר כתו. `LENGTH` סופר **תווים**, לא "אותיות".

**ש2.** `SUBSTR(טקסט, התחלה, כמה)` — כאן: מהתו הראשון, תו אחד. שימו לב שהמחרוזות הקבועות (`' '` ו‑`'.'`) מחוברות ב‑`||` בדיוק כמו עמודות.

<figure dir="ltr" class="dbtable">

| ShortName |
|:---:|
| אדם ח. |
| נור ע. |
| יואב כ. |
| מאיה ל. |
| רוני א. |
| סאלי ח. |

</figure>

**ש3.** אצל ששת התלמידים בלי טלפון קיבלתם **`NULL`**, לא מחרוזת ריקה. `REPLACE(NULL, …)` הוא `NULL` — כל פונקציית טקסט שמקבלת `NULL` מחזירה `NULL`.

<figure dir="ltr" class="dbtable">

| FirstName | Digits |
|:---:|:---:|
| אדם | 0501000001 |
| נור | NULL |
| יואב | 0521000003 |
| מאיה | 0541000004 |
| רוני | NULL |
| סאלי | 0501000006 |

</figure>

**ש4.** **5 שורות — וארבע קידומות אמיתיות.** ⚠️ `NULL` הוא אחת מהשורות: `DISTINCT` מתייחס לכל ה‑`NULL`ים כערך **אחד**, ומחזיר אותו כשורה. זה מבלבל, כי בכל מקום אחר ב‑SQL `NULL` **אינו** שווה ל‑`NULL`.

<figure dir="ltr" class="dbtable">

| Prefix |
|:---:|
| 050 |
| NULL |
| 052 |
| 054 |
| 053 |

</figure>

**ש5.** `UPPER` **לא עשתה כלום** — העמודה `Upper1` זהה בדיוק ל‑`Subject`.

**למה?** לאלפבית העברי (וגם לערבי) **אין אותיות גדולות וקטנות** — אין "מ גדולה". `UPPER` ו‑`LOWER` הן פונקציות שממפות תו לתו: `a→A`. לעברית אין מיפוי כזה, ולכן הן מחזירות את הקלט כמו שהוא. הן לא נכשלות ולא מזהירות — פשוט לא קורה כלום.

**המשמעות המעשית:** בבסיס נתונים בעברית, `UPPER(Name) = UPPER('אדם')` **אינו** פותר בעיות של אותיות גדולות/קטנות — כי אין כאלה. מה שהוא **כן** לא פותר, ושווה לזכור: **רווחים מיותרים** (`'אדם '` מול `'אדם'`) ו**אותיות סופיות**. לרווחים הפתרון הוא `TRIM`:

</div>

```sql
WHERE TRIM(Students.FirstName) = 'אדם'
```

<div dir="rtl">

<figure dir="ltr" class="dbtable">

| Subject | Upper1 | Len |
|:---:|:---:|:---:|
| מתמטיקה | מתמטיקה | 7 |
| אנגלית | אנגלית | 6 |
| מחשבים | מחשבים | 6 |
| היסטוריה | היסטוריה | 8 |
| ספורט | ספורט | 5 |
| מתמטיקה | מתמטיקה | 7 |
| ביולוגיה | ביולוגיה | 8 |

</figure>

**ש6.** `ROUND(מספר, ספרות)`. כל התוצאות כאן יצאו שלמות במקרה — 14500 × 0.88 = 12760 בדיוק.

<figure dir="ltr" class="dbtable">

| LastName | Salary | NetSalary |
|:---:|:---:|:---:|
| סרחאן | 14500 | 12760 |
| בר-לב | 11200 | 9856 |
| זיאד | 12800 | 11264 |
| שמש | 15300 | 13464 |
| חדאד | 9800 | 8624 |
| מזרחי | 13100 | 11528 |
| אבו-ראס | 10400 | 9152 |

</figure>

**ש7.** **ליאור לוי** — ציון 75 בדיוק, `Gap = 0`.

הטור `Diff` הוא שלילי אצל מי שמתחת ל‑75, ו‑`ABS` "מקפל" אותו לחיובי. לכן מיון לפי `Diff` היה נותן את **הנכשלים** בראש, ומיון לפי `Gap` נותן את **הקרובים לממוצע** — שתי שאלות שונות לגמרי. שימו לב גם לשורות האחרונות: 51 ו‑99 במרחק **זהה** מ‑75, בכיוונים הפוכים.

<figure dir="ltr" class="dbtable">

| StudentId | Grade | Diff | Gap |
|:---:|:---:|:---:|:---:|
| 1011 | 75 | 0 | 0 |
| 1008 | 79 | 4 | 4 |
| 1014 | 82 | 7 | 7 |
| 1015 | 64 | -11 | 11 |
| 1009 | 63 | -12 | 12 |
| 1010 | 91 | 16 | 16 |
| 1013 | 94 | 19 | 19 |
| 1007 | 97 | 22 | 22 |
| 1012 | 51 | -24 | 24 |
| 1016 | 99 | 24 | 24 |

</figure>

**ש8.** אצל **סאלי קיבלתם `NULL`** — ואין לה תאריך לידה, אז זו התשובה הנכונה. `JULIANDAY(NULL)` הוא `NULL`, וחיסור שמשתתף בו `NULL` הוא `NULL`. בסיס הנתונים **לא ניחש** גיל, וזה בדיוק מה שאנחנו רוצים.

מחלקים ב‑`365.25` ולא ב‑365, בגלל שנים מעוברות. `CAST(… AS INTEGER)` **קוטם** את השבר (14.8 → 14) — וזה הנכון לגיל: ילד בן 14 ועשרה חודשים הוא בן **14**, לא 15. `ROUND` היה מעגל אותו ל‑15 ומכניס אותו בטעות לכל רשימה של "בני 15".

<figure dir="ltr" class="dbtable">

| FirstName | BirthDate | Age |
|:---:|:---:|:---:|
| סאלי | NULL | NULL |
| מאיה | 2011-11-30 | 14 |
| אדם | 2011-03-14 | 15 |
| נור | 2011-07-22 | 15 |
| יואב | 2011-01-09 | 15 |
| רוני | 2011-05-18 | 15 |
| שירה | 2010-09-25 | 15 |
| כרים | 2010-12-03 | 15 |
| נועם | 2011-09-02 | 15 |
| לינא | 2010-10-19 | 15 |
| עומר | 2010-02-11 | 16 |
| תמר | 2010-04-07 | 16 |
| ליאור | 2010-06-16 | 16 |
| ג'וד | 2010-08-29 | 16 |
| הדיל | 2009-10-05 | 16 |
| ראניה | 2009-12-12 | 16 |
| דניאל | 2009-01-20 | 17 |
| איתי | 2009-03-27 | 17 |

</figure>

**ש9.** `STRFTIME('%Y', תאריך)` מחזיר את השנה — **כטקסט**, לא כמספר. `'%m'` יחזיר חודש, `'%d'` יום.

<figure dir="ltr" class="dbtable">

| FirstName | BirthYear |
|:---:|:---:|
| אדם | 2011 |
| נור | 2011 |
| יואב | 2011 |
| מאיה | 2011 |
| רוני | 2011 |
| סאלי | NULL |

</figure>

**ש10.** **אורלי שמש — 17 שנות ותק**, מ‑2009. אותו חישוב בדיוק כמו גיל: בסיס נתונים לא מבדיל בין "גיל אדם" ל"ותק בעבודה", שניהם הפרש בין שני תאריכים.

<figure dir="ltr" class="dbtable">

| LastName | HireDate | Seniority |
|:---:|:---:|:---:|
| שמש | 2009-09-01 | 17 |
| סרחאן | 2012-09-01 | 14 |
| מזרחי | 2016-09-01 | 10 |
| בר-לב | 2018-09-01 | 8 |
| זיאד | 2021-02-15 | 5 |
| חדאד | 2023-09-01 | 3 |
| אבו-ראס | 2024-09-01 | 2 |

</figure>

**ש11.** `JULIANDAY` מחזיר מספר ימים, ולכן ההפרש בין שניים הוא פשוט **מספר הימים**.

<figure dir="ltr" class="dbtable">

| AbsenceId | AbsenceDate | DaysAgo |
|:---:|:---:|:---:|
| 1 | 2026-09-02 | 19 |
| 7 | 2026-09-02 | 19 |
| 2 | 2026-09-03 | 18 |
| 12 | 2026-09-04 | 17 |
| 3 | 2026-09-07 | 14 |

</figure>

**ש12א.** **לא קיבלתם שגיאה.** קיבלתם **`2376`** — ואת אותו מספר **אצל כל ארבעת התלמידים**, למרות שנולדו בתאריכים שונים.

**ש12ב. מאיפה 2376?**

`BirthDate` הוא **טקסט**: `'2011-03-14'`. כשמבקשים לחבר לו מספר, SQLite לא מתלונן — הוא **ממיר** את הטקסט למספר. ההמרה קוראת ספרות מתחילת המחרוזת ועוצרת בתו הראשון שאינו ספרה:

</div>

```text
'2011-03-14'  ->  קורא "2011", נעצר ב-'-'  ->  2011
2011 + 365    ->  2376
```

<div dir="rtl">

לכן **כל** תאריך משנת 2011 נותן 2376, בלי קשר לחודש וליום. התוצאה **נראית** כמו מספר סביר, ואין שום סימן שמשהו השתבש — אין שגיאה, אין `NULL`, אין אזהרה. דוח שבנוי על החישוב הזה יהיה שגוי לחלוטין וייראה תקין לגמרי.

**הכלל:** לתאריכים יש פונקציות **משלהם**. `DATE(תאריך, '+365 days')` מחזיר תאריך; `JULIANDAY` מחזיר ימים להפרשים. `+` על עמודת תאריך הוא **באג**, גם אם הוא רץ.

<figure dir="ltr" class="dbtable">

| FirstName | BirthDate | Wrong | Right1 |
|:---:|:---:|:---:|:---:|
| אדם | 2011-03-14 | 2376 | 2012-03-13 |
| נור | 2011-07-22 | 2376 | 2012-07-21 |
| יואב | 2011-01-09 | 2376 | 2012-01-09 |
| מאיה | 2011-11-30 | 2376 | 2012-11-29 |

</figure>

> 🔎 גם ב‑`Right1` יש מה לראות: 365 יום **אינם** שנה. אצל אדם התוצאה היא 13 במרץ, יום **לפני** יום ההולדת — כי 2012 היא שנה מעוברת. ל"שנה אחת" כותבים `'+1 year'`.

</div>
<!-- classroom:end -->
