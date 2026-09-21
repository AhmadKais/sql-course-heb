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

### ➡️ מודול 20 — SQL: פונקציות 2 🔜

</div>

---

<div align="center">

**🧭 ניווט המודול**

</div>

| 📖 [חזרה למודול](README.md) | ❓ [שאלות ותשובות](questions.md) | ✏️ [לתרגילים](exercises.md) | 🏠 [דף הקורס](../../) |
|---|---|---|---|

</div>
