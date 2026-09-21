<div dir="rtl">

# מודול 19 — SQL: פונקציות

> **פרק 19 בתכנית הלימודים** · 4 שעות עיוני + 2 שעות מעשי
> **נושאים:** מניפולציות לערכים טקסטואליים · פונקציות נומריות · פונקציות תאריך · הזדמנויות קריירה

> 🧭 **במסלול המשולב:** יחידה 3, לצד [מודול 3 — ERD](../module-03-erd/), אחרי [מודול 18](../module-18-sql-order-by/).

---

## 🎯 מה תדעו בסוף המודול

- [ ] להסביר מה זו **פונקציה** ב‑SQL, ואיפה מותר להשתמש בה
- [ ] לעבד **טקסט**: אותיות גדולות/קטנות, אורך, חיתוך, חיפוש, החלפה
- [ ] לעבד **מספרים**: עיגול, ערך מוחלט, שארית, קיצוץ
- [ ] לעבד **תאריכים**: היום, הפרש בין תאריכים, הוספת חודשים, חילוץ שנה/חודש
- [ ] לחשב **גיל** מתאריך לידה — נכון
- [ ] לשלב פונקציות ב‑`WHERE` וב‑`ORDER BY` — ולדעת מה זה עולה
- [ ] להכיר את **ההבדלים בין SQLite ל‑Oracle** בפונקציות הנפוצות

---

## 🗺️ מפת המודול

| # | הסעיף |
|---|--------|
| 1 | [מה זו פונקציה](#1-מה-זו-פונקציה) |
| 2 | [פונקציות טקסט](#2-פונקציות-טקסט) |
| 3 | [פונקציות מספרים](#3-פונקציות-מספרים) |
| 4 | [פונקציות תאריך](#4-פונקציות-תאריך) |
| 5 | [חישוב גיל — הדוגמה שמאחדת הכול](#5-חישוב-גיל--הדוגמה-שמאחדת-הכול) |
| 6 | [פונקציות ב‑WHERE וב‑ORDER BY](#6-פונקציות-בwhere-ובorder-by) |
| 7 | [פונקציות ו‑NULL](#7-פונקציות-וnull) |
| 8 | [SQLite מול Oracle — טבלת התרגום](#8-sqlite-מול-oracle--טבלת-התרגום) |
| 9 | [הזדמנויות קריירה](#9-הזדמנויות-קריירה) |
| 10 | [דוגמה מלאה — כרטיס החיה](#10-דוגמה-מלאה--כרטיס-החיה) |
| 11 | [חמש טעויות נפוצות](#11-חמש-טעויות-נפוצות) |
| 12 | [רשימת בדיקה](#12-רשימת-בדיקה) |
| 13 | [סיכום המודול](#13-סיכום-המודול) |

---

## 1. מה זו פונקציה

<div align="center">

**פונקציה מקבלת ערך, עושה איתו משהו, ומחזירה ערך.**

</div>

</div>

```text
   UPPER('luna')       -->  'LUNA'         text in, text out
   LENGTH('luna')      -->  4              text in, NUMBER out
   ROUND(18.5)         -->  19             number in, number out
   DATE('now')         -->  '2026-09-21'   nothing in, date out

   +--------+     +----------+     +--------+
   | input  | --> | FUNCTION | --> | output |
   +--------+     +----------+     +--------+
```

<div dir="rtl">

במודול 18 פגשנו שתיים: `UPPER` ו‑`LENGTH`. עכשיו — הארגז המלא.

**איפה מותר להשתמש בפונקציה?** בכל מקום שמותר ערך:

| המקום | הדוגמה |
|-------|---------|
| `SELECT` | `SELECT UPPER(name) FROM animal` |
| `WHERE` | `WHERE LENGTH(name) > 5` |
| `ORDER BY` | `ORDER BY UPPER(name)` |
| בתוך פונקציה אחרת | `UPPER(SUBSTR(name, 1, 3))` |

**הפונקציות במודול הזה הן "שורה‑שורה"** (single-row): כל שורה נכנסת, כל שורה יוצאת. 20 חיות נכנסות — 20 תוצאות יוצאות. יש סוג אחר — פונקציות **מצרפיות** (`COUNT`, `SUM`) שמקבלות הרבה שורות ומחזירות אחת — וזה מודול 23.

> 🎬 **סיפור מהשטח: הדוח שספר את "יוסי" ארבע פעמים**
>
> מערכת CRM הפיקה דוח "לקוחות לפי שם". יוסי כהן הופיע ארבע פעמים: `יוסי כהן`, `יוסי כהן ` (רווח בסוף), `Yossi Cohen`, ו‑`YOSSI COHEN`. ארבע רשומות, אדם אחד.
>
> הפתרון לא היה לתקן את הנתונים — היו 40,000 לקוחות. הפתרון היה שורה אחת: `GROUP BY UPPER(TRIM(name))`. פתאום 40,000 הפכו ל‑31,000.
>
> 🔑 **פונקציות הן הכלי לנרמל נתונים מלוכלכים בזמן שאילתה** — בלי לגעת בטבלה. וזה קורה בכל מערכת אמיתית.

---

## 2. פונקציות טקסט

</div>

```sql
SELECT name,
       UPPER(name)              AS upper_name,     -- LUNA
       LOWER(name)              AS lower_name,     -- luna
       LENGTH(name)             AS letters,        -- 4
       SUBSTR(name, 1, 3)       AS first_three,    -- Lun
       SUBSTR(name, -2)         AS last_two,       -- na
       INSTR(name, 'a')         AS where_is_a,     -- 4  (position; 0 = not found)
       REPLACE(name, 'a', '@')  AS replaced        -- Lun@
FROM   animal
WHERE  animal_id = 1;
```

<div dir="rtl">

| הפונקציה | מה היא עושה | דוגמה | תוצאה |
|-----------|-------------|--------|--------|
| `UPPER(x)` | אותיות גדולות | `UPPER('Luna')` | `LUNA` |
| `LOWER(x)` | אותיות קטנות | `LOWER('Luna')` | `luna` |
| `LENGTH(x)` | מספר תווים | `LENGTH('Luna')` | `4` |
| `SUBSTR(x, start, len)` | חיתוך — מתו `start`, `len` תווים | `SUBSTR('Luna', 1, 3)` | `Lun` |
| `SUBSTR(x, -n)` | `n` התווים **האחרונים** | `SUBSTR('Luna', -2)` | `na` |
| `INSTR(x, y)` | **מיקום** של `y` בתוך `x` (0 = לא נמצא) | `INSTR('Luna', 'a')` | `4` |
| `REPLACE(x, old, new)` | החלפה של **כל** המופעים | `REPLACE('Luna', 'a', '@')` | `Lun@` |
| `TRIM(x)` | הסרת רווחים משני הצדדים | `TRIM('  Luna  ')` | `Luna` |
| `x \|\| y` | חיבור (מודול 16) | `'Lu' \|\| 'na'` | `Luna` |

### 2.1 `SUBSTR` — הספירה מתחילה מ‑1

</div>

```text
   'Luna'
    1234        <- positions start at 1, not 0

   SUBSTR('Luna', 1, 2)  = 'Lu'    from position 1, take 2
   SUBSTR('Luna', 2, 2)  = 'un'    from position 2, take 2
   SUBSTR('Luna', 3)     = 'na'    from position 3 to the end
   SUBSTR('Luna', -1)    = 'a'     the last 1 character
   SUBSTR('Luna', -3)    = 'una'   the last 3 characters
```

<div dir="rtl">

### 2.2 `TRIM` — הפתרון לרווחים שמסתתרים

במודול 17 ראינו: `'Luna '` (עם רווח) ≠ `'Luna'`. **הרווח הזה הוא הבעיה מספר 1 בנתונים שהוקלדו ידנית.**

</div>

```sql
-- the safe way to compare user-typed text
WHERE UPPER(TRIM(name)) = 'LUNA'
```

<div dir="rtl">

`TRIM` מסיר רווחים; `UPPER` מאחד אותיות. יחד — השוואה שסולחת להקלדה.

### 2.3 שילוב פונקציות

פונקציה יכולה לקבל **תוצאה של פונקציה אחרת**. קוראים **מבפנים החוצה**:

</div>

```sql
SELECT UPPER(SUBSTR(name, 1, 1)) || LOWER(SUBSTR(name, 2)) AS proper_name
FROM   animal;
--     ^^^^^^^^^^^^^^^^^^^^^^^^    ^^^^^^^^^^^^^^^^^^^^^^^
--     first letter, uppercase     the rest, lowercase
--     -> "Luna" even if stored as "LUNA" or "luna"
```

<div dir="rtl">

> 💡 ב‑Oracle יש לזה פונקציה מוכנה: `INITCAP(name)`. ב‑SQLite — בונים לבד, כמו למעלה.

---

## 3. פונקציות מספרים

</div>

```sql
SELECT weight_kg,
       ROUND(weight_kg)          AS rounded,       -- 19    (nearest whole)
       ROUND(weight_kg, 1)       AS one_decimal,   -- 18.5
       ROUND(weight_kg * 2.2, 2) AS lb,            -- 40.7  (2 decimals)
       ABS(-5)                   AS absolute,      -- 5
       17 % 5                    AS remainder,     -- 2     (17 = 3*5 + 2)
       CEIL(4.2)                 AS ceiling,       -- 5     (round UP)
       FLOOR(4.8)                AS floor_val      -- 4     (round DOWN)
FROM   animal
WHERE  animal_id = 1;
```

<div dir="rtl">

| הפונקציה | מה היא עושה | דוגמה | תוצאה |
|-----------|-------------|--------|--------|
| `ROUND(x)` | עיגול למספר שלם | `ROUND(18.5)` | `19` |
| `ROUND(x, n)` | עיגול ל‑`n` ספרות אחרי הנקודה | `ROUND(40.7333, 2)` | `40.73` |
| `ABS(x)` | ערך מוחלט | `ABS(-5)` | `5` |
| `x % y` | שארית חלוקה | `17 % 5` | `2` |
| `CEIL(x)` | עיגול **למעלה** | `CEIL(4.2)` | `5` |
| `FLOOR(x)` | עיגול **למטה** | `FLOOR(4.8)` | `4` |

### 3.1 עיגול — הפרטים שחשובים לכסף

</div>

```text
   ROUND(4.5)   =  5      halves round AWAY from zero
   ROUND(5.5)   =  6
   ROUND(-4.5)  = -5

   ROUND(x, 2)  for money.  ALWAYS.
   SELECT 0.1 + 0.2;          -->  0.3     looks fine...
   SELECT 0.1 + 0.2 = 0.3;    -->  0       ...but it is NOT equal! (floating point)
   SELECT ROUND(0.1 + 0.2, 2) = 0.3;  -->  1   ROUND fixes it.
```

<div dir="rtl">

> ⚠️ **מודול 16 לימד:** `10 / 4 = 2` — שלם חלקי שלם. `ROUND` **לא** מתקן את זה, כי השארית כבר נזרקה. `ROUND(10 / 4.0, 1)` = `2.5`. **קודם `.0`, אחר כך `ROUND`.**

### 3.2 שארית — למה זה שימושי

</div>

```sql
-- every 3rd animal (for sampling)
SELECT name FROM animal WHERE animal_id % 3 = 0;
-- -> Rocky (3), Tom (6), Nala (9), Oscar (12), Charlie (15), Felix (18)

-- odd / even
SELECT name, animal_id % 2 AS is_odd FROM animal;
```

<div dir="rtl">

---

## 4. פונקציות תאריך

זה החלק שבו הדיאלקטים נבדלים **הכי הרבה**. נלמד את SQLite (Programiz), ונראה את Oracle לצידו.

### 4.1 היום

</div>

```sql
SELECT DATE('now');              -- SQLite:  2026-09-21
-- Oracle:  SELECT SYSDATE FROM DUAL;
```

<div dir="rtl">

> 💡 **בדוגמאות בקורס נשתמש בתאריך קבוע** — `'2026-09-21'` — כדי שהפלט שלכם יתאים לפתרונות. בקוד אמיתי: `DATE('now')`.

### 4.2 הפרש בין תאריכים — ימים

</div>

```sql
-- how many days has Luna been alive?
SELECT name,
       birth_date,
       JULIANDAY('2026-09-21') - JULIANDAY(birth_date) AS days_alive
FROM   animal
WHERE  animal_id = 1;
-- -> 2016.0 days
```

<div dir="rtl">

`JULIANDAY` הופך תאריך ל**מספר** (ימים מאז נקודת ייחוס עתיקה). **הפרש בין שני מספרים = הפרש בימים.** זו הדרך של SQLite.

</div>

```text
   SQLite:   JULIANDAY(date2) - JULIANDAY(date1)       -> days
   Oracle:   date2 - date1                             -> days  (dates subtract directly)
```

<div dir="rtl">

### 4.3 הוספת זמן

</div>

```sql
-- when is the next rabies shot due?  (12 months after the last one)
SELECT given_date,
       DATE(given_date, '+12 months') AS next_due
FROM   vaccination
WHERE  vaccination_id = 1;
-- -> 2023-03-20  ->  2024-03-20
```

<div dir="rtl">

| מה להוסיף | SQLite | Oracle |
|-----------|--------|--------|
| ימים | `DATE(d, '+30 days')` | `d + 30` |
| חודשים | `DATE(d, '+12 months')` | `ADD_MONTHS(d, 12)` |
| שנים | `DATE(d, '+1 year')` | `ADD_MONTHS(d, 12)` |
| **אחורה** | `DATE(d, '-7 days')` | `d - 7` |

### 4.4 חילוץ חלקים — `STRFTIME`

</div>

```sql
SELECT expense_date,
       STRFTIME('%Y', expense_date)    AS year,       -- 2024
       STRFTIME('%m', expense_date)    AS month,      -- 01
       STRFTIME('%Y-%m', expense_date) AS year_month, -- 2024-01
       STRFTIME('%d/%m/%Y', expense_date) AS israeli  -- 05/01/2024
FROM   expense
WHERE  expense_id = 1;
```

<div dir="rtl">

| הקוד | משמעות | דוגמה |
|------|---------|--------|
| `%Y` | שנה, 4 ספרות | `2024` |
| `%m` | חודש, 2 ספרות | `01` |
| `%d` | יום בחודש | `05` |
| `%w` | יום בשבוע (0 = ראשון) | `1` |
| `%Y-%m` | שנה‑חודש | `2024-01` — **מצוין ל‑`GROUP BY` חודשי** (מודול 24) |

</div>

```text
   SQLite:   STRFTIME('%Y', d)        Oracle:   EXTRACT(YEAR FROM d)
             STRFTIME('%m', d)                  EXTRACT(MONTH FROM d)
             STRFTIME('%d/%m/%Y', d)            TO_CHAR(d, 'DD/MM/YYYY')
```

<div dir="rtl">

> ⚠️ **`STRFTIME` מחזיר טקסט.** `STRFTIME('%Y', d) = 2024` (מספר) עלול להיכשל או להתנהג מוזר. `= '2024'` (טקסט) — נכון.

---

## 5. חישוב גיל — הדוגמה שמאחדת הכול

רותי שואלת: *"בן כמה כל כלב?"* — זו השאלה שמאחדת תאריכים, מספרים ועיגול.

</div>

```sql
-- Step 1: days alive
SELECT name, JULIANDAY('2026-09-21') - JULIANDAY(birth_date) AS days
FROM   animal WHERE species_id = 1;

-- Step 2: years (365.25 accounts for leap years)
SELECT name, (JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25 AS years
FROM   animal WHERE species_id = 1;
-- -> Luna 5.52, Rocky 6.84, ...

-- Step 3: whole years -- FLOOR, not ROUND (you are 5 until your 6th birthday)
SELECT name,
       FLOOR((JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25) AS age
FROM   animal
WHERE  species_id = 1
ORDER  BY age DESC;
```

```text
name     age
-------  ----
Zoe      10.0
Rex      9.0
Bella    8.0
Rocky    6.0
Daisy    6.0
Luna     5.0
Shadow   5.0
Max      4.0
Charlie  2.0
```

<div dir="rtl">

> 💡 **למה `10.0` ולא `10`?** ב‑SQLite, `FLOOR` מחזיר מספר עשרוני. לתצוגה נקייה: `CAST(... AS INTEGER)` במקום `FLOOR` — לגילים (חיוביים) זה נותן אותה תוצאה, כ‑`10`. ב‑Oracle `FLOOR` מחזיר `10` ישירות.

**שלוש החלטות בשאילתה הזאת, וכל אחת חשובה:**

| ההחלטה | למה |
|---------|------|
| `365.25` ולא `365` | שנה מעוברת כל 4 שנים. על כלב בן 10 ההבדל הוא 2.5 ימים — לא נורא. על מסמך משפטי — נורא |
| `FLOOR` ולא `ROUND` | גיל **לא מעגלים**. מי שנולד לפני 5.9 שנים הוא בן **5**, לא 6 |
| `birth_date` בעמודה, **לא** `age` | ⭐ מודול 6+10: גיל מזדקן. שומרים תאריך לידה, **מחשבים** גיל. **תמיד.** |

> 🔑 **וזה בדיוק למה מודול 6 אמר "אל תשמרו `age`":** עכשיו אתם רואים שחישוב הגיל הוא שורה אחת. אין שום סיבה לשמור ערך שמשתנה כל יום.

</div>

```sql
-- Oracle version
SELECT name,
       FLOOR(MONTHS_BETWEEN(SYSDATE, birth_date) / 12) AS age
FROM   animal;
```

<div dir="rtl">

---

## 6. פונקציות ב‑WHERE וב‑ORDER BY

### 6.1 ב‑WHERE — הפתרון לבעיות ממודול 17

</div>

```sql
-- case-insensitive search (module 17's problem, solved)
SELECT name FROM animal WHERE UPPER(name) = 'LUNA';
SELECT name FROM animal WHERE LOWER(name) LIKE 'l%';      -- Luna, Lily

-- names of exactly 4 letters (cleaner than LIKE '____')
SELECT name FROM animal WHERE LENGTH(name) = 4;

-- expenses in a specific month
SELECT * FROM expense WHERE STRFTIME('%Y-%m', expense_date) = '2024-03';

-- animals older than 5
SELECT name FROM animal
WHERE  (JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25 > 5;
```

<div dir="rtl">

### 6.2 ב‑ORDER BY — הפתרון לבעיות ממודול 18

</div>

```sql
-- true alphabetical (uppercase and lowercase mixed)
SELECT name FROM animal ORDER BY UPPER(name);

-- by age, oldest first
SELECT name, birth_date FROM animal
ORDER  BY JULIANDAY('2026-09-21') - JULIANDAY(birth_date) DESC;
```

<div dir="rtl">

### 6.3 ⚠️ המחיר

</div>

```text
   WHERE name = 'Luna'            -- can use an INDEX on name: fast, even on 10M rows
   WHERE UPPER(name) = 'LUNA'     -- must compute UPPER() for EVERY row: slow on 10M rows

   A function on the LEFT side of a comparison hides the column from the index.
```

<div dir="rtl">

על 20 חיות — לא מרגישים. על 10 מיליון לקוחות — ההבדל בין שנייה לדקה. **הפתרון** (אינדקס על ביטוי, או לאחסן את הערך מנורמל) — מודול 29. **בינתיים: דעו שזה קיים.**

---

## 7. פונקציות ו‑NULL

**הכלל ממודול 16 נשאר:** NULL נכנס ⟵ NULL יוצא.

</div>

```sql
SELECT name, breed, UPPER(breed), LENGTH(breed)
FROM   animal
WHERE  breed IS NULL;
```

```text
name   breed  UPPER(breed)  LENGTH(breed)
-----  -----  ------------  -------------
Mitzi                                       <- all NULL. LENGTH(NULL) is NULL, not 0.
Nala
```

<div dir="rtl">

| הפונקציה | על NULL |
|-----------|---------|
| `UPPER(NULL)` | NULL |
| `LENGTH(NULL)` | **NULL** — לא 0 |
| `ROUND(NULL)` | NULL |
| `JULIANDAY(NULL)` | NULL — ולכן **גיל של חיה בלי תאריך לידה הוא NULL**, לא 0 |
| `NULL \|\| 'x'` | NULL |

**הפתרון** — לתת ערך ברירת מחדל כשיש NULL — הוא `COALESCE`, **מודול 20**. הוא הפונקציה החשובה ביותר שעוד לא למדתם.

---

## 8. SQLite מול Oracle — טבלת התרגום

</div>

```text
+------------------------+------------------------------+------------------------------+
| WHAT                   | SQLite (Programiz)           | Oracle (APEX / exam)         |
+------------------------+------------------------------+------------------------------+
| uppercase / lowercase  | UPPER(x) / LOWER(x)          | same                         |
| length                 | LENGTH(x)                    | same                         |
| substring              | SUBSTR(x, start, len)        | same                         |
| find position          | INSTR(x, y)                  | same                         |
| replace                | REPLACE(x, old, new)         | same                         |
| trim spaces            | TRIM(x)                      | same                         |
| concatenate            | x || y                       | same  (also CONCAT(x, y))    |
| Title Case             | (build it, section 2.3)      | INITCAP(x)                   |
| pad with zeros/spaces  | PRINTF('%05d', x)            | LPAD(x, 5, '0')              |
+------------------------+------------------------------+------------------------------+
| round                  | ROUND(x, n)                  | same                         |
| absolute               | ABS(x)                       | same                         |
| remainder              | x % y                        | MOD(x, y)                    |
| ceiling / floor        | CEIL(x) / FLOOR(x)           | same                         |
| truncate decimals      | CAST(x AS INTEGER)           | TRUNC(x)                     |
+------------------------+------------------------------+------------------------------+
| today                  | DATE('now')                  | SYSDATE                      |
| days between           | JULIANDAY(a) - JULIANDAY(b)  | a - b                        |
| add months             | DATE(d, '+12 months')        | ADD_MONTHS(d, 12)            |
| add days               | DATE(d, '+30 days')          | d + 30                       |
| months between         | (days / 30.44, approx.)      | MONTHS_BETWEEN(a, b)         |
| year / month           | STRFTIME('%Y', d)            | EXTRACT(YEAR FROM d)         |
| format                 | STRFTIME('%d/%m/%Y', d)      | TO_CHAR(d, 'DD/MM/YYYY')     |
| parse text to date     | DATE('2024-03-15')           | TO_DATE('15/03/2024',        |
|                        |                              |         'DD/MM/YYYY')        |
+------------------------+------------------------------+------------------------------+
```

<div dir="rtl">

> 🔑 **טקסט ומספרים — כמעט זהים. תאריכים — שונים לגמרי.** אם תעברו ל‑APEX, סעיף 4 הוא מה שתצטרכו לתרגם.

---

## 9. הזדמנויות קריירה

תכנית הלימודים עוצרת כאן לרגע, ובצדק: **הפונקציות שלמדתם הרגע הן הכלי היומיומי של ארבעה תפקידים.**

| התפקיד | מה הוא עושה עם פונקציות | דוגמה מהיום |
|---------|--------------------------|--------------|
| **אנליסט נתונים** | מנקה, מקבץ לפי חודש, מחשב גילים ותקופות | `STRFTIME('%Y-%m', …)` בכל דוח |
| **מפתח Back-end** | בונה את השאילתות שמאחורי כל מסך | `UPPER(TRIM(email))` בכל התחברות |
| **מנהל בסיס נתונים (DBA)** | מזהה שאילתות איטיות — לרוב פונקציה על עמודה מאונדקסת | סעיף 6.3 |
| **בודק תוכנה (QA)** | מאמת שהמערכת מחשבת נכון — גיל, מע"מ, תאריכי פירעון | `FLOOR` מול `ROUND` |

> 🎬 **מהשטח:** בראיונות לתפקיד אנליסט מתחיל, השאלה השכיחה ביותר אחרי `JOIN` היא **"איך תחשב גיל מתאריך לידה?"** — והתשובה שמבדילה: מי שאומר `FLOOR` ו‑`365.25` ומסביר למה. זה סעיף 5.

---

## 10. דוגמה מלאה — כרטיס החיה

רותי מבקשת **כרטיס להדפסה** לכל חיה זמינה: שם באותיות גדולות, גיל בשנים, משקל מעוגל, ותאריך החיסון הבא.

</div>

```sql
-- Step 1: the raw data
SELECT name, birth_date, weight_kg, status
FROM   animal
WHERE  status = 'available';

-- Step 2: each piece, formatted
SELECT UPPER(name)                                                    AS card_name,
       FLOOR((JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25) AS age,
       ROUND(weight_kg, 1)                                            AS kg,
       STRFTIME('%d/%m/%Y', birth_date)                               AS born
FROM   animal
WHERE  status = 'available'
ORDER  BY UPPER(name);
```

```text
card_name  age   kg    born
---------  ----  ----  ----------
BUNNY      2.0   1.5   01/01/2024
COCO             0.1               <- no birth date: age and born are NULL
FELIX      7.0   5.0   14/02/2019
LILY             3.4
MITZI      3.0   3.1   10/01/2023
OSCAR      4.0   5.5   12/12/2021
REX        9.0   38.7  08/08/2017
ROCKY      6.0   31.0  20/11/2019
SHADOW     5.0   25.1  30/06/2021
```

<div dir="rtl">

> 💡 **שימו לב ל‑Coco ול‑Lily:** גיל ריק, תאריך ריק. **זה נכון** — לא ידוע. הכרטיס צריך להציג "לא ידוע", לא כלום — וזה `COALESCE`, מודול 20. עד אז, הפלט הזה הוא **מדויק**, רק לא **ידידותי**.

---

## 11. חמש טעויות נפוצות

| # | הטעות | מה קורה | התיקון |
|---|-------|----------|---------|
| 1 | **`SUBSTR(x, 0, 3)`** | ב‑SQLite מחזיר 2 תווים; ב‑Oracle 3. **הספירה מ‑1** | `SUBSTR(x, 1, 3)` |
| 2 | **`ROUND` לגיל** | כלב בן 5.9 הופך ל‑6 | `FLOOR` |
| 3 | **`STRFTIME('%Y', d) = 2024`** | השוואת טקסט למספר — לא יציב | `= '2024'` — טקסט |
| 4 | **לשמור `age` בטבלה** | מזדקן מחר | `birth_date` + חישוב |
| 5 | **`LENGTH(x) = 0` כדי למצוא ריק** | NULL לא נתפס — `LENGTH(NULL)` הוא NULL | `x IS NULL OR LENGTH(x) = 0` |

---

## 12. רשימת בדיקה

| ✔ | הבדיקה |
|---|--------|
| ☐ | הרצתי `UPPER`, `LOWER`, `LENGTH`, `SUBSTR`, `INSTR`, `REPLACE`, `TRIM` על עמודה אמיתית |
| ☐ | חתכתי 3 תווים ראשונים **ו**‑2 אחרונים עם `SUBSTR` |
| ☐ | עיגלתי ל‑2 ספרות, וראיתי ש‑`ROUND(4.5)` הוא 5 |
| ☐ | חישבתי הפרש ימים עם `JULIANDAY` |
| ☐ | חישבתי גיל בשנים עם `FLOOR` ו‑`365.25` |
| ☐ | הוספתי 12 חודשים לתאריך |
| ☐ | חילצתי שנה וחודש עם `STRFTIME('%Y-%m', …)` |
| ☐ | הרצתי `UPPER(name) = 'LUNA'` ב‑`WHERE` — ומצאתי את מה ש‑`= 'luna'` פספס |
| ☐ | ראיתי ש‑`LENGTH(NULL)` הוא NULL, לא 0 |
| ☐ | פתרתי את [התרגילים](exercises.md) בהרצה |

---

## 13. סיכום המודול

<div align="center">

### 🧠 שבע נקודות

</div>

1. **פונקציה = ערך נכנס, ערך יוצא.** מותרת בכל מקום שמותר ערך: `SELECT`, `WHERE`, `ORDER BY`, ובתוך פונקציה אחרת.
2. **טקסט:** `UPPER`/`LOWER`/`TRIM` לנרמול · `LENGTH` · `SUBSTR` (מ‑1!) · `INSTR` · `REPLACE`.
3. **מספרים:** `ROUND(x, 2)` לכסף · `FLOOR` לגיל · `%` לשארית · `ABS`.
4. **תאריכים ב‑SQLite:** `JULIANDAY` להפרש · `DATE(d, '+n months')` להוספה · `STRFTIME` לחילוץ ולעיצוב. **ב‑Oracle כל אלה שונים.**
5. **גיל = `FLOOR(ימים / 365.25)`.** ולכן שומרים תאריך לידה, לא גיל.
6. **פונקציה ב‑`WHERE` פותרת רגישות לאותיות — ועולה ביצועים** על טבלאות גדולות.
7. **NULL נכנס ⟵ NULL יוצא.** `LENGTH(NULL)` אינו 0. הפתרון: `COALESCE`, מודול 20.

<div align="center">

---

*"הנתונים תמיד מלוכלכים. פונקציות הן הדרך לנקות אותם*
*בזמן השאילתה — בלי לגעת במקור."*

---

</div>

## 📎 המשך

| | |
|---|---|
| ❓ | [שאלות ותשובות](questions.md) |
| ✏️ | [תרגילים](exercises.md) — על [בסיס הנתונים המוכן](../../resources/shelter-db/) |
| ✅ | [פתרונות](solutions.md) — עם הפלט האמיתי |
| ⬅️ | [מודול 18 — SQL: מיונים](../module-18-sql-order-by/) |
| 🧭 | [מסלול הלימוד](../../LEARNING-PATH.md) — יחידה 3 הושלמה; הבאה: מודול 4 + 20 |
| ➡️ | מודול 20 — SQL: פונקציות 2 (המרה, NULL, `CASE`) 🔜 |
| 🏠 | [חזרה לדף הקורס](../../) |

</div>
