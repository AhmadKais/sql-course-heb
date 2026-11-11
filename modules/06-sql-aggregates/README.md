<div dir="rtl">

# מודול 23 — SQL: פונקציות מצרפיות

> **פרק 23 בתכנית הלימודים** · 2 שעות עיוני + 2 שעות מעשי
> **נושאים:** פונקציות מצרפיות

> 🧭 **במסלול המשולב:** יחידה 6, לצד [מודול 6 — נרמול](../module-06-normalization/). **הדרך למצוא כפילויות היא לספור אותן** — ומודול 24 יראה איך.

---

## 🎯 מה תדעו בסוף המודול

- [ ] להסביר מה ההבדל בין פונקציה **שורה‑שורה** (מודול 19) לפונקציה **מצרפית**
- [ ] להשתמש ב‑`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`
- [ ] להבדיל בין `COUNT(*)`, `COUNT(עמודה)` ו‑`COUNT(DISTINCT עמודה)`
- [ ] להסביר מה פונקציות מצרפיות עושות עם **NULL** — ולמה `AVG` יכול "לשקר"
- [ ] לספור **בתנאי** עם `SUM(CASE …)`
- [ ] לשלב פונקציה מצרפית עם `WHERE` ועם `JOIN`
- [ ] להבין למה `SELECT name, MAX(weight_kg)` הוא שאלה שבורה

---

## 🗺️ מפת המודול

| # | הסעיף |
|---|--------|
| 1 | [הרבה שורות נכנסות — אחת יוצאת](#1-הרבה-שורות-נכנסות--אחת-יוצאת) |
| 2 | [חמש הפונקציות](#2-חמש-הפונקציות) |
| 3 | [שלושה סוגי COUNT](#3-שלושה-סוגי-count) |
| 4 | [פונקציות מצרפיות ו‑NULL](#4-פונקציות-מצרפיות-וnull) |
| 5 | [עם WHERE ועם JOIN](#5-עם-where-ועם-join) |
| 6 | [ספירה מותנית — `SUM(CASE …)`](#6-ספירה-מותנית--sumcase-) |
| 7 | [המלכודת: עמודה רגילה ליד פונקציה מצרפית](#7-המלכודת-עמודה-רגילה-ליד-פונקציה-מצרפית) |
| 8 | [דוגמה מלאה — דוח המקלט](#8-דוגמה-מלאה--דוח-המקלט) |
| 9 | [חמש טעויות נפוצות](#9-חמש-טעויות-נפוצות) |
| 10 | [סיכום המודול](#10-סיכום-המודול) |

---

## 1. הרבה שורות נכנסות — אחת יוצאת

במודול 19 כל פונקציה עבדה על **שורה אחת**: 20 חיות נכנסו ל‑`UPPER(name)`, 20 תוצאות יצאו. פונקציה **מצרפית** (aggregate) עובדת על **קבוצה** של שורות ומחזירה **ערך אחד**:

</div>

```text
   single-row (module 19)                  aggregate (this module)

   Luna   -> UPPER -> LUNA                 18.5  \
   Simba  -> UPPER -> SIMBA                 4.2   \
   Rocky  -> UPPER -> ROCKY                31.0    >--  AVG  -->  11.557
   ...                                      ...   /
   20 rows in  ->  20 rows out             20 rows in  ->  1 row out
```

<div dir="rtl">

> 🔑 **זה המעבר מ"נתונים" ל"מידע"** (מודול 1). 22 שורות של הוצאות הן נתונים. "המקלט הוציא 19,800 ₪" — זה מידע. כל דוח, כל דשבורד וכל גרף מתחיל בפונקציה מצרפית.

---

## 2. חמש הפונקציות

</div>

```sql
SELECT SUM(amount)   AS total,
       AVG(amount)   AS avg,
       MIN(amount)   AS min,
       MAX(amount)   AS max,
       COUNT(*)      AS n
FROM   expense;
```

```text
total    avg    min    max     n
-------  -----  -----  ------  --
19800.0  900.0  175.0  2100.0  22
```

<div dir="rtl">

| הפונקציה | מה היא מחזירה | על איזה טיפוס |
|-----------|----------------|----------------|
| `COUNT(…)` | **כמה** שורות / ערכים | כל טיפוס |
| `SUM(x)` | **סכום** | מספרים |
| `AVG(x)` | **ממוצע** = `SUM / COUNT` | מספרים |
| `MIN(x)` | הערך **הקטן** ביותר | מספרים, טקסט, תאריכים |
| `MAX(x)` | הערך **הגדול** ביותר | מספרים, טקסט, תאריכים |

### 2.1 `MIN` ו‑`MAX` לא רק למספרים

</div>

```sql
SELECT MIN(birth_date) AS oldest_birth,      -- earliest date = OLDEST animal
       MAX(birth_date) AS youngest_birth,
       MIN(name), MAX(name)                  -- alphabetical first / last
FROM   animal;
```

```text
oldest_birth  youngest_birth  MIN(name)  MAX(name)
------------  --------------  ---------  ---------
2016-01-01    2024-03-01      Bella      Zoe
```

<div dir="rtl">

> ⚠️ **`MIN(birth_date)` הוא החיה ה*מבוגרת* ביותר** — התאריך המוקדם ביותר. מבלבל בפעם הראשונה; כדאי לקרוא את זה בקול: "תאריך הלידה הכי מוקדם".

### 2.2 עיגול

`AVG` מחזיר לרוב מספר עם הרבה ספרות. **לתצוגה — `ROUND`** (מודול 19):

</div>

```sql
SELECT ROUND(AVG(amount), 2) AS avg FROM expense WHERE category = 'medical';   -- 679.09
```

<div dir="rtl">

---

## 3. שלושה סוגי COUNT

</div>

```sql
SELECT COUNT(*)                   AS animals,     -- rows
       COUNT(breed)               AS with_breed,  -- non-NULL values
       COUNT(chip_number)         AS with_chip,
       COUNT(DISTINCT breed)      AS breeds,      -- DIFFERENT non-NULL values
       COUNT(DISTINCT species_id) AS species
FROM   animal;
```

```text
animals  with_breed  with_chip  breeds  species
-------  ----------  ---------  ------  -------
20       16          13         13      4
```

<div dir="rtl">

| הצורה | סופרת | כאן |
|-------|--------|-----|
| `COUNT(*)` | **שורות** — כולן, כולל שורות עם NULL | 20 חיות |
| `COUNT(עמודה)` | ערכים **שאינם NULL** בעמודה | 16 עם גזע (4 בלי) |
| `COUNT(DISTINCT עמודה)` | ערכים **שונים** שאינם NULL | 13 גזעים שונים ("Mixed" ו‑"Tabby" חוזרים) |

</div>

```sql
-- the difference tells a story
SELECT COUNT(DISTINCT adopter_id) AS adopters,    -- 6 people
       COUNT(adopter_id)          AS adoptions,   -- 9 adoptions
       COUNT(DISTINCT animal_id)  AS animals      -- 8 animals (Luna twice)
FROM   adoption;
```

<div dir="rtl">

> 🔑 **"כמה X יש?" — תמיד לשאול: שורות, ערכים, או ערכים שונים?** "כמה אימוצים?" = 9. "כמה משפחות אימצו?" = 6. "כמה חיות מצאו בית?" = 8. שלוש שאלות, שלוש תשובות, מאותה טבלה.

---

## 4. פונקציות מצרפיות ו‑NULL

**הכלל: כל הפונקציות המצרפיות מתעלמות מ‑NULL** — חוץ מ‑`COUNT(*)`, שסופר שורות.

### 4.1 `AVG` מחשב רק על מה שידוע

</div>

```sql
SELECT COUNT(*)          AS all_rows,
       COUNT(birth_date) AS known,
       ROUND(AVG((JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25), 2) AS avg_age,
       ROUND(SUM((JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25)
             / COUNT(*), 2)                                                     AS wrong_avg
FROM   animal;
```

```text
all_rows  known  avg_age  wrong_avg
--------  -----  -------  ---------
20        17     5.57     4.73
```

<div dir="rtl">

`AVG` חילק ב‑**17** — רק החיות שהגיל שלהן ידוע. החישוב "הידני" חילק ב‑**20**, כאילו לשלוש החיות בלי תאריך לידה יש גיל 0. **5.57 נכון; 4.73 מטעה.**

> 💡 **זה בדיוק למה NULL ≠ 0** (מודול 16). אילו היינו שומרים 0 במקום NULL — גם `AVG` היה מחשב 4.73, ואף אחד לא היה יודע.

### 4.2 סכום של "כלום"

</div>

```sql
SELECT SUM(amount)              FROM expense WHERE category = 'toys';   -- NULL  (!)
SELECT COUNT(*)                 FROM expense WHERE category = 'toys';   -- 0
SELECT COALESCE(SUM(amount), 0) FROM expense WHERE category = 'toys';   -- 0
```

<div dir="rtl">

כשאין אף שורה: `COUNT` מחזיר **0**, אבל `SUM`, `AVG`, `MIN`, `MAX` מחזירים **NULL**. בדוח כספי רוצים 0 — **`COALESCE(SUM(…), 0)`** (מודול 20).

---

## 5. עם WHERE ועם JOIN

### 5.1 `WHERE` מסנן **לפני** הצבירה

</div>

```text
   FROM expense  -->  WHERE category = 'medical'  -->  SUM(amount)
   22 rows            11 rows                          1 value
```

```sql
-- income from adoptions in 2024
SELECT SUM(fee_paid) FROM adoption WHERE STRFTIME('%Y', adoption_date) = '2024';   -- 1150.0

-- all expenses in 2024
SELECT SUM(amount)   FROM expense  WHERE expense_date BETWEEN '2024-01-01' AND '2024-12-31';  -- 16920.0
```

<div dir="rtl">

### 5.2 `JOIN` ואז צבירה

</div>

```sql
-- statistics for cats -- by species NAME, so we need species
SELECT COUNT(*)               AS cats,
       ROUND(AVG(weight_kg),2) AS avg_kg,
       MIN(weight_kg)          AS lightest,
       MAX(weight_kg)          AS heaviest
FROM   animal a
JOIN   species s ON s.species_id = a.species_id
WHERE  s.name = 'Cat';
```

```text
cats  avg_kg  lightest  heaviest
----  ------  --------  --------
7     4.13    2.9       5.5
```

```sql
-- how much did Max cost the shelter?
SELECT SUM(e.amount) AS max_cost
FROM   expense e
JOIN   animal a ON a.animal_id = e.animal_id
WHERE  a.name = 'Max';                        -- 2520.0  (x-ray 420 + surgery 2100)
```

<div dir="rtl">

> ⚠️ **JOIN עלול לכפול שורות — וכך לכפול סכומים.** אם נחבר `animal` גם ל‑`expense` וגם ל‑`vaccination` באותה שאילתה, כל הוצאה של Rocky תופיע פעם לכל חיסון שלו — ו‑`SUM(amount)` יהיה פי 4. **כלל:** צוברים מטבלה אחת "רבים" בכל שאילתה. (במודול 24 נראה איך לשלב בבטחה.)

---

## 6. ספירה מותנית — `SUM(CASE …)`

רוצים כמה ספירות שונות **בשורה אחת** — זמינות, מאומצות, בלי שבב? `WHERE` מסנן את **כל** השאילתה, אז הוא לא יעזור. הטריק: `CASE` הופך כל שורה ל‑1 או 0, ו‑`SUM` סופר את ה‑1‑ים:

</div>

```sql
SELECT COUNT(*)                                             AS total,
       SUM(CASE WHEN status = 'available'  THEN 1 ELSE 0 END) AS available,
       SUM(CASE WHEN status = 'adopted'    THEN 1 ELSE 0 END) AS adopted,
       SUM(CASE WHEN chip_number IS NULL   THEN 1 ELSE 0 END) AS no_chip
FROM   animal;
```

```text
total  available  adopted  no_chip
-----  ---------  -------  -------
20     9          8        7
```

<div dir="rtl">

אותו טריק עם **סכומים** — `THEN amount` במקום `THEN 1`:

</div>

```sql
SELECT SUM(CASE WHEN animal_id IS NULL     THEN amount ELSE 0 END) AS general,
       SUM(CASE WHEN animal_id IS NOT NULL THEN amount ELSE 0 END) AS per_animal
FROM   expense;
```

```text
general  per_animal
-------  ----------
12330.0  7470.0
```

<div dir="rtl">

> 🎬 **מה זה מגלה?** 62% מההוצאות של המקלט (12,330 מתוך 19,800) הן **כלליות** — מזון וחשמל — ולא קשורות לחיה מסוימת. כשרותי מבקשת תקציב, "כמה עולה חיה?" היא שאלה מסובכת יותר ממה שנראה.

### 6.1 אחוזים

</div>

```sql
SELECT ROUND(100.0 * SUM(CASE WHEN chip_number IS NULL THEN 1 ELSE 0 END) / COUNT(*), 1)
       AS pct_no_chip
FROM   animal;                                -- 35.0
```

<div dir="rtl">

> ⚠️ **`100.0` ולא `100`** — אחרת חלוקת שלמים (מודול 16): `7 * 100 / 20` עובד, אבל `7 / 20 * 100` = 0.

> 💡 **ב‑SQLite יש קיצור:** תנאי הוא בעצמו 1 או 0, אז `SUM(status = 'available')` עובד. ב‑Oracle — לא. `SUM(CASE …)` עובד בכל מקום.

---

## 7. המלכודת: עמודה רגילה ליד פונקציה מצרפית

*"מי החיה הכבדה ביותר?"* — הניסיון הטבעי:

</div>

```sql
SELECT name, MAX(weight_kg) FROM animal;
```

```text
   SQLite:  Rex | 38.7          <- happens to work (SQLite picks the row of the MAX)
   Oracle:  ORA-00937: not a single-group group function
```

<div dir="rtl">

**למה Oracle צודק?** `MAX(weight_kg)` מתכווץ ל‑**ערך אחד**; `name` הוא **20** ערכים. איזה מהם לשים בשורה האחת? ומה אם נבקש `name, AVG(weight_kg)` — שם של איזו חיה שייך לממוצע? **השאלה עצמה שבורה.** SQLite מנחש; רוב בסיסי הנתונים מסרבים.

**הדרך הנכונה — שני שלבים: קודם מוצאים את המקסימום, אחר כך מי שיש לו אותו:**

</div>

```sql
SELECT name, weight_kg
FROM   animal
WHERE  weight_kg = (SELECT MAX(weight_kg) FROM animal);    -- a subquery: module 24
```

```text
name  weight_kg
----  ---------
Rex   38.7
```

<div dir="rtl">

> 🔑 **הכלל:** ב‑`SELECT` עם פונקציה מצרפית (בלי `GROUP BY`), **כל** העמודות חייבות להיות מצרפיות. רוצים גם עמודה רגילה? זה בדיוק `GROUP BY` — מודול 24.

---

## 8. דוגמה מלאה — דוח המקלט

רותי צריכה שורה אחת לישיבת ההנהלה:

</div>

```sql
SELECT (SELECT COUNT(*) FROM animal WHERE status = 'available')        AS waiting,
       (SELECT COUNT(*) FROM adoption)                                 AS adoptions,
       (SELECT SUM(fee_paid) FROM adoption)                            AS income,
       (SELECT SUM(amount)   FROM expense)                             AS expenses,
       (SELECT SUM(fee_paid) FROM adoption) - (SELECT SUM(amount) FROM expense) AS balance;
```

```text
waiting  adoptions  income  expenses  balance
-------  ---------  ------  --------  --------
9        9          2200.0  19800.0   -17600.0
```

<div dir="rtl">

> 🎬 **המספר האדום:** הכנסות מאימוץ מכסות רק 11% מההוצאות. המקלט חי מתרומות — ואין להן טבלה. **שאילתה טובה לא רק עונה; היא מראה מה חסר במודל.**

> 💡 **שימו לב לתחביר:** כל עמודה היא שאילתה נפרדת בסוגריים — **תת‑שאילתה** שמחזירה ערך אחד. כך מצרפים מטבלאות שונות בלי JOIN (ובלי לכפול סכומים, סעיף 5.2). מודול 24 מרחיב.

---

## 9. חמש טעויות נפוצות

| # | הטעות | מה קורה | התיקון |
|---|-------|----------|---------|
| 1 | **`COUNT(breed)` כשרצו את מספר החיות** | 16 במקום 20 — NULL לא נספר | `COUNT(*)` לשורות |
| 2 | **`SUM` על קבוצה ריקה** | NULL במקום 0 בדוח | `COALESCE(SUM(x), 0)` |
| 3 | **`SELECT name, MAX(x)`** | שגיאה ב‑Oracle, ניחוש ב‑SQLite | תת‑שאילתה, או `GROUP BY` |
| 4 | **JOIN לשתי טבלאות "רבים" ואז `SUM`** | סכומים כפולים | צבירה מטבלה אחת; תתי‑שאילתות |
| 5 | **שמירת 0 במקום NULL** | `AVG` מחושב על ערכים מומצאים | NULL לערך לא ידוע — `AVG` כבר יודע לדלג |

---

## 10. סיכום המודול

<div align="center">

### 🧠 שש נקודות

</div>

1. **פונקציה מצרפית:** הרבה שורות נכנסות, **ערך אחד** יוצא. `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`.
2. **`COUNT(*)`** = שורות · **`COUNT(x)`** = ערכים שאינם NULL · **`COUNT(DISTINCT x)`** = ערכים שונים.
3. **NULL מדולג** בכל הפונקציות (חוץ מ‑`COUNT(*)`). `AVG` מחשב רק על הידוע — וזה נכון.
4. **קבוצה ריקה:** `COUNT` = 0, השאר NULL ⟵ `COALESCE(SUM(x), 0)`.
5. **`SUM(CASE WHEN … THEN 1 ELSE 0 END)`** — כמה ספירות מותנות בשורה אחת.
6. **אסור לערבב** עמודה רגילה עם מצרפית בלי `GROUP BY`. ובזהירות עם `JOIN` — הוא יכול לכפול סכומים.

<div align="center">

---

*"עשרים שורות הן רשימה.*
*מספר אחד הוא תשובה."*

---

</div>

## 📎 המשך

| | |
|---|---|
| ❓ | [שאלות ותשובות](questions.md) |
| ✏️ | [תרגילים](exercises.md) — על [בסיס הנתונים המוכן](../../resources/shelter-db/) |
| ✅ | [פתרונות](solutions.md) — עם הפלט האמיתי |
| ⬅️ | [מודול 22 — SQL: איחוד טבלאות 2](../module-22-sql-joins-2/) |
| ➡️ | [מודול 24 — SQL: קיבוץ נתונים ותתי‑שאילתות](../module-24-sql-group-by/) |
| 🏠 | [חזרה לדף הקורס](../../) |

</div>
