<div dir="rtl">

# מודול 24 — SQL: קיבוץ נתונים ותתי‑שאילתות

> **פרק 24 בתכנית הלימודים** · 6 שעות עיוני + 4 שעות מעשי
> **נושאים:** GROUP BY & HAVING · ROLLUP & CUBE · GROUPING SETS · Subqueries · Single Row Subqueries · Multiple‑row Subqueries · Correlated Subqueries · Using SET Operators

> 🧭 **במסלול המשולב:** יחידה 6, לצד [מודול 6 — נרמול](../module-06-normalization/), אחרי [מודול 23](../module-23-sql-aggregates/). זה המודול הארוך ביותר בחלק ה‑SQL — חלקו אותו לשלושה שיעורים: **קיבוץ** (סעיפים 1–5), **תתי‑שאילתות** (6–9), **פעולות קבוצה** (10).

---

## 🎯 מה תדעו בסוף המודול

- [ ] לקבץ שורות עם `GROUP BY` ולחשב פונקציה מצרפית **לכל קבוצה**
- [ ] לסנן קבוצות עם `HAVING` — ולהבדיל בינו לבין `WHERE`
- [ ] למצוא **כפילויות** עם `GROUP BY … HAVING COUNT(*) > 1`
- [ ] להכיר `ROLLUP`, `CUBE` ו‑`GROUPING SETS` (Oracle), ולבנות סיכומי ביניים בכל מערכת
- [ ] לכתוב תת‑שאילתה שמחזירה **ערך אחד**, **רשימה**, או **טבלה**
- [ ] לכתוב תת‑שאילתה **מתואמת** (correlated) ולהשתמש ב‑`EXISTS`
- [ ] להימנע ממלכודת **`NOT IN` עם NULL**
- [ ] לחבר תוצאות עם `UNION`, `UNION ALL`, `INTERSECT`, `EXCEPT`

---

## 🗺️ מפת המודול

| # | הסעיף |
|---|--------|
| 1 | [GROUP BY — פונקציה מצרפית לכל קבוצה](#1-group-by--פונקציה-מצרפית-לכל-קבוצה) |
| 2 | [קיבוץ לפי כמה עמודות](#2-קיבוץ-לפי-כמה-עמודות) |
| 3 | [HAVING — סינון קבוצות](#3-having--סינון-קבוצות) |
| 4 | [מציאת כפילויות — הקשר לנרמול](#4-מציאת-כפילויות--הקשר-לנרמול) |
| 5 | [ROLLUP, CUBE, GROUPING SETS](#5-rollup-cube-grouping-sets) |
| 6 | [תת‑שאילתה שמחזירה ערך אחד](#6-תתשאילתה-שמחזירה-ערך-אחד) |
| 7 | [תת‑שאילתה שמחזירה רשימה — ומלכודת NOT IN](#7-תתשאילתה-שמחזירה-רשימה--ומלכודת-not-in) |
| 8 | [תת‑שאילתה מתואמת ו‑EXISTS](#8-תתשאילתה-מתואמת-וexists) |
| 9 | [תת‑שאילתה כטבלה — ב‑FROM](#9-תתשאילתה-כטבלה--בfrom) |
| 10 | [פעולות קבוצה — UNION, INTERSECT, EXCEPT](#10-פעולות-קבוצה--union-intersect-except) |
| 11 | [סדר הביצוע של שאילתה](#11-סדר-הביצוע-של-שאילתה) |
| 12 | [שש טעויות נפוצות](#12-שש-טעויות-נפוצות) |
| 13 | [סיכום המודול](#13-סיכום-המודול) |

---

## 1. GROUP BY — פונקציה מצרפית לכל קבוצה

במודול 23 כל השאילתה הצטמצמה ל**שורה אחת**: "כמה חיות?" ⟵ 20. אבל רותי שואלת: *"כמה חיות **בכל סטטוס**?"* — היא רוצה שורה **לכל** סטטוס.

</div>

```sql
SELECT status, COUNT(*) AS animals
FROM   animal
GROUP  BY status
ORDER  BY animals DESC;
```

```text
status      animals
----------  -------
available   9
adopted     8
quarantine  1
medical     1
deceased    1
```

<div dir="rtl">

**מה `GROUP BY` עושה:** ממיין את השורות ל"ערימות" לפי הערך בעמודה, ומפעיל את הפונקציה המצרפית **על כל ערימה בנפרד**:

</div>

```text
   20 rows  --GROUP BY status-->   available:  Rocky, Mitzi, Coco ... (9)   --COUNT-->  9
                                   adopted:    Luna, Simba, Bella ... (8)   --COUNT-->  8
                                   medical:    Max                    (1)   --COUNT-->  1
                                   quarantine: Nala                   (1)   --COUNT-->  1
                                   deceased:   Daisy                  (1)   --COUNT-->  1
```

<div dir="rtl">

### 1.1 הכלל שמודול 23 השאיר פתוח

במודול 23 ראינו ש‑`SELECT name, MAX(weight_kg)` שבור. עכשיו אפשר לנסח את הכלל המלא:

> 🔑 **כל עמודה ב‑`SELECT` חייבת להיות אחד משניים: עמודה שמופיעה ב‑`GROUP BY`, או פונקציה מצרפית.** `status` ב‑`GROUP BY` — מותר. `COUNT(*)` מצרפית — מותר. `name` — אסור: בקבוצת "available" יש 9 שמות, איזה מהם?

### 1.2 עם JOIN

</div>

```sql
SELECT s.name AS species, COUNT(*) AS animals, ROUND(AVG(a.weight_kg), 1) AS avg_kg
FROM   animal a
JOIN   species s ON s.species_id = a.species_id
GROUP  BY s.name
ORDER  BY animals DESC;
```

```text
species  animals  avg_kg
-------  -------  ------
Dog      9        22.1
Cat      7        4.1
Rabbit   2        1.6
Parrot   2        0.1
```

```sql
SELECT category, COUNT(*) AS n, SUM(amount) AS total
FROM   expense
GROUP  BY category
ORDER  BY total DESC;
```

```text
category     n   total
-----------  --  ------
food         4   7490.0
medical      11  7470.0
utilities    4   3770.0
maintenance  1   540.0
supplies     2   530.0
```

<div dir="rtl">

> 💡 **השוו לתרגיל 5ג במודול 23:** שם כתבנו `SUM(CASE …)` לכל קטגוריה, ונאלצנו לדעת אותן מראש. `GROUP BY` מוצא את הקטגוריות **לבד** — כולל קטגוריה שתתווסף מחר.

### 1.3 קבוצות בלי חברים — `LEFT JOIN` + `COUNT(עמודה)`

</div>

```sql
-- available animals per species -- including species with none
SELECT s.name, COUNT(a.animal_id) AS available
FROM   species s
LEFT   JOIN animal a ON a.species_id = s.species_id AND a.status = 'available'
GROUP  BY s.name
ORDER  BY s.name;
```

<div dir="rtl">

> ⚠️ **`COUNT(a.animal_id)`, לא `COUNT(*)`.** אחרי `LEFT JOIN`, קבוצה בלי התאמות היא שורה **אחת** עם NULL. `COUNT(*)` יספור אותה כ‑1; `COUNT(a.animal_id)` ידלג על ה‑NULL ויחזיר 0. **עם `LEFT JOIN` — תמיד סופרים עמודה מהצד הימני.**

---

## 2. קיבוץ לפי כמה עמודות

כל צירוף **שונה** של ערכים = קבוצה:

</div>

```sql
SELECT STRFTIME('%Y', expense_date) AS year, category, SUM(amount) AS total
FROM   expense
GROUP  BY year, category
ORDER  BY year, category;
```

```text
year  category     total
----  -----------  ------
2024  food         5540.0
2024  maintenance  540.0
2024  medical      6540.0
2024  supplies     530.0
2024  utilities    3770.0
2025  food         1950.0
2025  medical      930.0
```

<div dir="rtl">

> 💡 **קיבוץ לפי ביטוי:** `GROUP BY STRFTIME('%Y-%m', expense_date)` — קבוצה לכל חודש. זה מה שמודול 19 הבטיח: "`%Y-%m` מצוין ל‑`GROUP BY` חודשי". ב‑SQLite אפשר לכתוב את הכינוי (`GROUP BY year`); ב‑Oracle — חייבים לחזור על הביטוי המלא.

---

## 3. HAVING — סינון קבוצות

*"אילו קטגוריות עלו יותר מ‑3,000 ₪?"* — הניסיון הראשון:

</div>

```text
   SELECT category, SUM(amount) FROM expense
   WHERE  SUM(amount) > 3000                      -- ERROR: misuse of aggregate
   GROUP  BY category;
```

<div dir="rtl">

`WHERE` רץ **לפני** הקיבוץ — על שורות בודדות. בזמן הזה עוד אין `SUM`. לסינון **אחרי** הקיבוץ יש מילה נפרדת:

</div>

```sql
SELECT category, SUM(amount) AS total
FROM   expense
WHERE  expense_date >= '2024-01-01'          -- 1. filter ROWS
GROUP  BY category                           -- 2. make groups
HAVING SUM(amount) > 3000;                   -- 3. filter GROUPS
```

```text
category   total
---------  ------
food       7490.0
medical    7470.0
utilities  3770.0
```

<div dir="rtl">

| | `WHERE` | `HAVING` |
|---|---|---|
| מסנן | **שורות** | **קבוצות** |
| מתי | לפני `GROUP BY` | אחרי `GROUP BY` |
| פונקציה מצרפית בתנאי | ❌ אסור | ✅ מותר — בשביל זה הוא קיים |
| דוגמה | `WHERE category = 'medical'` | `HAVING COUNT(*) > 1` |

> 💡 **כלל אצבע:** אם התנאי נכון לשורה **בודדת** — `WHERE`. אם הוא על הקבוצה **כולה** (סכום, ספירה, ממוצע) — `HAVING`. תנאי שאפשר לשים ב‑`WHERE` — שמים שם: פחות שורות לקבץ, שאילתה מהירה יותר.

---

## 4. מציאת כפילויות — הקשר לנרמול

**זו הסיבה שמודול 6 ומודול 24 באותה יחידה.** `GROUP BY … HAVING COUNT(*) > 1` הוא **הכלי** למצוא ערכים שחוזרים:

</div>

```sql
-- which animal was taken in more than once?
SELECT a.name, COUNT(*) AS intakes
FROM   intake i
JOIN   animal a ON a.animal_id = i.animal_id
GROUP  BY a.animal_id, a.name
HAVING COUNT(*) > 1;
```

```text
name  intakes
----  -------
Luna  2
```

```sql
-- who adopted more than once?
SELECT p.first_name || ' ' || p.last_name AS adopter,
       COUNT(*) AS adoptions, SUM(ad.fee_paid) AS paid
FROM   adoption ad
JOIN   person p ON p.person_id = ad.adopter_id
GROUP  BY p.person_id
HAVING COUNT(*) >= 2;
```

```text
adopter     adoptions  paid
----------  ---------  -----
Dana Cohen  2          700.0
Lior Bar    2          350.0
Shira Katz  2          350.0
```

```sql
-- the same vaccine more than once (the README promised: Rocky, 3 rabies shots)
SELECT a.name, COUNT(*) AS shots
FROM   vaccination v
JOIN   animal a        ON a.animal_id        = v.animal_id
JOIN   vaccine_type vt ON vt.vaccine_type_id = v.vaccine_type_id
WHERE  vt.name = 'Rabies'
GROUP  BY a.animal_id
HAVING COUNT(*) > 1;
```

```text
name   shots
-----  -----
Luna   2
Rocky  3
```

<div dir="rtl">

> 🔑 **למה `GROUP BY a.animal_id` ולא `GROUP BY a.name`?** שתי חיות **שונות** יכולות להיקרא באותו שם — ואז הן יתמזגו לקבוצה אחת. מקבצים לפי **המזהה**, ומציגים את השם. (ב‑SQLite מותר להציג `a.name` אם קיבצנו לפי `animal_id`; ב‑Oracle צריך להוסיף אותו ל‑`GROUP BY`: `GROUP BY a.animal_id, a.name`.)

> 🎬 **מנרמול לבדיקה:** בעבודה אמיתית, לפני שמוסיפים `UNIQUE` לעמודה (מודול 27), מריצים `GROUP BY col HAVING COUNT(*) > 1`. אם חזרו שורות — האילוץ ייכשל, וצריך קודם לנקות.

---

## 5. ROLLUP, CUBE, GROUPING SETS

אלה הרחבות של `GROUP BY` שמוסיפות **שורות סיכום** — סיכומי ביניים וסך הכול. הן קיימות ב‑Oracle, SQL Server ו‑PostgreSQL. **ב‑SQLite אין אותן** — נראה את התחביר, ואז איך מקבלים את אותה תוצאה בכל מערכת.

### 5.1 ROLLUP — סיכומי ביניים מדורגים

</div>

```sql
-- Oracle
SELECT EXTRACT(YEAR FROM expense_date) AS year, category, SUM(amount) AS total
FROM   expense
GROUP  BY ROLLUP (EXTRACT(YEAR FROM expense_date), category);
```

<div dir="rtl">

`ROLLUP (year, category)` מחזיר שלוש רמות: **כל צירוף** (שנה + קטגוריה), **סיכום לכל שנה** (קטגוריה = NULL), ו**סך הכול** (שנה = NULL וקטגוריה = NULL). זה בדיוק "Subtotal" של אקסל.

**אותה תוצאה ב‑SQLite — שלוש שאילתות ו‑`UNION ALL`** (סעיף 10):

</div>

```sql
SELECT year, category, total FROM (
  SELECT STRFTIME('%Y', expense_date) AS year, category, SUM(amount) AS total, 1 AS lvl
  FROM   expense GROUP BY year, category
  UNION ALL
  SELECT STRFTIME('%Y', expense_date), '-- subtotal', SUM(amount), 2
  FROM   expense GROUP BY 1
  UNION ALL
  SELECT 'all', '== TOTAL', SUM(amount), 3
  FROM   expense
)
ORDER  BY year, lvl, category;
```

```text
year  category     total
----  -----------  -------
2024  food         5540.0
2024  maintenance  540.0
2024  medical      6540.0
2024  supplies     530.0
2024  utilities    3770.0
2024  -- subtotal  16920.0
2025  food         1950.0
2025  medical      930.0
2025  -- subtotal  2880.0
all   == TOTAL     19800.0
```

<div dir="rtl">

### 5.2 CUBE ו‑GROUPING SETS

</div>

```text
   GROUP BY ROLLUP (A, B)          ->  (A, B)  (A)       ()          hierarchical
   GROUP BY CUBE   (A, B)          ->  (A, B)  (A)  (B)  ()          every combination
   GROUP BY GROUPING SETS ((A), (B)) ->        (A)  (B)              exactly the ones you list
```

<div dir="rtl">

| ההרחבה | מתי | דוגמה |
|---------|-----|--------|
| `ROLLUP` | היררכיה — שנה ⟵ חודש ⟵ יום | דוח הוצאות עם סיכום לכל שנה |
| `CUBE` | כל הזוויות — גם לפי שנה וגם לפי קטגוריה | "טבלת ציר" מלאה |
| `GROUPING SETS` | רק הסיכומים שבחרתם | לפי סטטוס, ובנפרד לפי מין — בשאילתה אחת |

> 💡 **הפונקציה `GROUPING(col)`** ב‑Oracle מחזירה 1 בשורת סיכום ו‑0 בשורה רגילה — כדי להבדיל בין NULL "אמיתי" לבין NULL של סיכום. בגרסת ה‑`UNION ALL` אנחנו פשוט כותבים תווית (`'-- subtotal'`).

> 🔑 **מה צריך לזכור למבחן:** מה כל אחת מחזירה (התרשים למעלה). **מה צריך לזכור לעבודה:** שבכל מערכת אפשר לבנות את זה עם `UNION ALL`.

---

## 6. תת‑שאילתה שמחזירה ערך אחד

**תת‑שאילתה** (subquery) היא `SELECT` בתוך סוגריים, בתוך שאילתה אחרת. כבר פגשנו אחת במודול 23:

</div>

```sql
SELECT name, weight_kg
FROM   animal
WHERE  weight_kg = (SELECT MAX(weight_kg) FROM animal);      -- Rex, 38.7
```

<div dir="rtl">

הפנימית רצה **קודם** ומחזירה **ערך אחד** (38.7), והחיצונית משתמשת בו כאילו נכתב שם מספר. זו **single-row subquery**. משתמשים בה עם `=`, `<`, `>`, `<=`, `>=`, `<>`.

</div>

```sql
-- dogs heavier than the AVERAGE dog
SELECT name, weight_kg
FROM   animal
WHERE  species_id = 1
  AND  weight_kg > (SELECT AVG(weight_kg) FROM animal WHERE species_id = 1);
```

```text
name    weight_kg
------  ---------
Rocky   31.0
Bella   28.4
Rex     38.7
Shadow  25.1
```

<div dir="rtl">

> ⚠️ **אם הפנימית מחזירה יותר משורה אחת** — `=` נכשל ב‑Oracle (`ORA-01427: single-row subquery returns more than one row`). SQLite לוקח בשקט את **הראשונה** — עוד ניחוש מסוכן. אם התשובה יכולה להיות רשימה — סעיף 7.

---

## 7. תת‑שאילתה שמחזירה רשימה — ומלכודת NOT IN

### 7.1 `IN`

</div>

```sql
-- animals adopted for less than 250
SELECT name, status
FROM   animal
WHERE  animal_id IN (SELECT animal_id FROM adoption WHERE fee_paid < 250);
```

```text
name     status
-------  -------
Simba    adopted
Bella    adopted
Thumper  adopted
Zoe      adopted
Kiwi     adopted
```

<div dir="rtl">

הפנימית מחזירה **רשימה** של מזהים; `IN` בודק אם הערך ברשימה. זו **multiple-row subquery**.

### 7.2 ⚠️ `NOT IN` ו‑NULL

*"אילו חיות לא חוסנו?"* — עובד:

</div>

```sql
SELECT name FROM animal
WHERE  animal_id NOT IN (SELECT animal_id FROM vaccination);   -- Coco, Nala, Lily, Kiwi
```

<div dir="rtl">

*"אילו חיות לא הוצאנו עליהן כסף?"* — אותה תבנית בדיוק:

</div>

```sql
SELECT COUNT(*) FROM animal
WHERE  animal_id NOT IN (SELECT animal_id FROM expense);       -- 0  (!!)
```

<div dir="rtl">

**אפס.** אף שגיאה, אף אזהרה. אבל יש 10 חיות בלי הוצאות (מודול 22). **מה קרה?**

ב‑`expense` יש הוצאות כלליות, ו‑`animal_id` שלהן **NULL**. הרשימה הפנימית היא `(8, NULL, 5, NULL, 13, …)`. ו‑`x NOT IN (…, NULL, …)` פירושו `x <> 8 AND x <> NULL AND …` — ו‑`x <> NULL` הוא **לא ידוע**. "לא ידוע" ב‑`AND` אף פעם לא נותן true. **כל השורות נפסלות.**

**שני תיקונים:**

</div>

```sql
-- fix 1: remove the NULLs from the list
SELECT name FROM animal
WHERE  animal_id NOT IN (SELECT animal_id FROM expense WHERE animal_id IS NOT NULL);

-- fix 2 (recommended): NOT EXISTS -- immune to NULLs (section 8)
SELECT a.name FROM animal a
WHERE  NOT EXISTS (SELECT 1 FROM expense e WHERE e.animal_id = a.animal_id);
-- both: Bunny, Charlie, Coco, Kiwi, Lily, Mitzi, Simba, Thumper, Tom, Zoe
```

<div dir="rtl">

> 🔑 **הכלל: לעולם אל תכתבו `NOT IN (תת‑שאילתה)` על עמודה שיכולה להיות NULL.** השתמשו ב‑`NOT EXISTS` או ב‑`LEFT JOIN … IS NULL` (מודול 21). זו אחת מהשגיאות המפורסמות ביותר ב‑SQL — כי היא שקטה.

### 7.3 `ANY` ו‑`ALL` (Oracle)

</div>

```text
   x > ALL (subquery)   x is greater than EVERY value   =  x > (SELECT MAX(...))
   x > ANY (subquery)   x is greater than AT LEAST ONE  =  x > (SELECT MIN(...))
   x = ANY (subquery)   same as  x IN (subquery)
```

```sql
-- Oracle: animals heavier than every cat
SELECT name FROM animal
WHERE  weight_kg > ALL (SELECT weight_kg FROM animal WHERE species_id = 2);

-- the same everywhere (SQLite has no ALL / ANY)
SELECT name FROM animal
WHERE  weight_kg > (SELECT MAX(weight_kg) FROM animal WHERE species_id = 2);   -- the 9 dogs
```

<div dir="rtl">

---

## 8. תת‑שאילתה מתואמת ו‑EXISTS

עד עכשיו הפנימית רצה **פעם אחת**. תת‑שאילתה **מתואמת** (correlated) משתמשת בעמודה **מהשאילתה החיצונית** — ולכן רצה מחדש **לכל שורה**:

</div>

```sql
-- animals heavier than the average OF THEIR OWN SPECIES
SELECT a.name, a.weight_kg, a.species_id
FROM   animal a
WHERE  a.weight_kg > (SELECT AVG(b.weight_kg)
                      FROM   animal b
                      WHERE  b.species_id = a.species_id)     -- <- uses the OUTER row
ORDER  BY a.species_id, a.name;
```

```text
name     weight_kg  species_id
-------  ---------  ----------
Bella    28.4       1
Rex      38.7       1
Rocky    31.0       1
Shadow   25.1       1
Felix    5.0        2
Oscar    5.5        2
Simba    4.2        2
Tom      4.8        2
Thumper  1.8        3
Coco     0.1        4
```

<div dir="rtl">

לכל חיה, הפנימית מחשבת את הממוצע **של המין שלה**: לכלב — ממוצע הכלבים (22.1), לחתול — ממוצע החתולים (4.1). `a.species_id` מקשר בין השתיים.

### 8.1 `EXISTS` — "האם יש לפחות אחת?"

</div>

```sql
-- animals with at least one expense over 1,000
SELECT a.name
FROM   animal a
WHERE  EXISTS (SELECT 1 FROM expense e
               WHERE  e.animal_id = a.animal_id AND e.amount > 1000);
-- Max, Rex
```

<div dir="rtl">

`EXISTS` מחזיר true אם הפנימית מחזירה **שורה אחת לפחות** — לא משנה מה בה (לכן `SELECT 1`). הוא עוצר בשורה הראשונה שמצא, ו**לא מושפע מ‑NULL**. `NOT EXISTS` — ההפך: "אין אף אחת".

### 8.2 "החיסון הבא" — מה שמודול 21 לא הצליח

במודול 21 (תרגיל 7) self join החזיר לכל חיסון את **כל** החיסונים המאוחרים. עם תת‑שאילתה מתואמת לוקחים רק את **הקרוב**:

</div>

```sql
SELECT a.name, v1.given_date AS shot,
       (SELECT MIN(v2.given_date)
        FROM   vaccination v2
        WHERE  v2.animal_id       = v1.animal_id
          AND  v2.vaccine_type_id = v1.vaccine_type_id
          AND  v2.given_date      > v1.given_date) AS next_shot
FROM   vaccination v1
JOIN   animal a ON a.animal_id = v1.animal_id
WHERE  a.name = 'Rocky' AND v1.vaccine_type_id = 1;
```

```text
name   shot        next_shot
-----  ----------  ----------
Rocky  2023-05-25  2024-05-28
Rocky  2024-05-28  2025-05-30
Rocky  2025-05-30                 <- no next shot yet
```

<div dir="rtl">

> 💡 **תת‑שאילתה ב‑`SELECT`** — כמו בסעיף 8 של מודול 23. היא חייבת להחזיר ערך אחד (`MIN`). כשאין — NULL.

> ⚠️ **ביצועים:** מתואמת רצה פעם לכל שורה. על 20 חיות — מיידי. על מיליון — לפעמים איטי. JOIN עם `GROUP BY` הוא לרוב החלופה המהירה.

---

## 9. תת‑שאילתה כטבלה — ב‑FROM

תת‑שאילתה ב‑`FROM` היא **טבלה זמנית** — אפשר לשאול אותה כמו כל טבלה. כך עושים **צבירה על צבירה**:

*"כמה עולה **בממוצע** להחזיק חיה?"* — קודם סכום לכל חיה, אחר כך ממוצע של הסכומים:

</div>

```sql
SELECT ROUND(AVG(total), 2) AS avg_cost_per_animal
FROM   (SELECT animal_id, SUM(amount) AS total
        FROM   expense
        WHERE  animal_id IS NOT NULL
        GROUP  BY animal_id);                           -- 747.0
```

<div dir="rtl">

> 💡 **`AVG(SUM(…))` ישירות אסור** — אי אפשר לקנן פונקציות מצרפיות באותה רמה. (Oracle מרשה `MAX(SUM(x))` עם `GROUP BY` — חריג.) תת‑שאילתה ב‑`FROM` היא הדרך הכללית.

> 💡 **`WITH` — אותו דבר, קריא יותר:** ראינו אותו במודול 21 (`WITH RECURSIVE`). גם בלי רקורסיה, `WITH name AS (SELECT …)` נותן שם לתת‑שאילתה ומוציא אותה מהסוגריים:

</div>

```sql
WITH cost_per_animal AS (
  SELECT animal_id, SUM(amount) AS total
  FROM   expense WHERE animal_id IS NOT NULL
  GROUP  BY animal_id
)
SELECT ROUND(AVG(total), 2) FROM cost_per_animal;      -- 747.0
```

<div dir="rtl">

---

## 10. פעולות קבוצה — UNION, INTERSECT, EXCEPT

JOIN מחבר טבלאות **לרוחב** (עוד עמודות). פעולות קבוצה מחברות תוצאות **לאורך** (עוד שורות):

</div>

```text
   A = cities of volunteers          B = cities of adopters
   {Haifa, Kiryat Ata,               {Haifa, Tel Aviv, Karmiel,
    Tirat Carmel}                     Nahariya}

   A UNION B       everything, once each     Haifa, Karmiel, Kiryat Ata, Nahariya,
                                             Tel Aviv, Tirat Carmel
   A INTERSECT B   in both                   Haifa
   A EXCEPT B      in A, not in B            Kiryat Ata, Tirat Carmel
   B EXCEPT A      in B, not in A            Karmiel, Nahariya, Tel Aviv
```

```sql
SELECT city FROM person WHERE role = 'adopter'
EXCEPT
SELECT city FROM person WHERE role = 'volunteer';
```

```text
city
--------
Karmiel
Nahariya
Tel Aviv
```

<div dir="rtl">

| האופרטור | מה | כפילויות |
|-----------|-----|----------|
| `UNION` | כל השורות משתיהן | **מוסר** |
| `UNION ALL` | כל השורות משתיהן | **נשאר** — ומהיר יותר |
| `INTERSECT` | רק מה שבשתיהן | מוסר |
| `EXCEPT` | בראשונה ולא בשנייה | מוסר (ב‑Oracle: **`MINUS`**) |

**שלושה חוקים:**
1. לשתי השאילתות **אותו מספר עמודות**, בטיפוסים מתאימים.
2. שמות העמודות נלקחים **מהראשונה**.
3. `ORDER BY` — **אחד**, בסוף, על כל התוצאה.

### 10.1 `UNION ALL` — שתי טבלאות שונות לרשימה אחת

</div>

```sql
-- the 2025 cash flow: money in and money out, in one timeline
SELECT 'adoption' AS kind, adoption_date AS dt, fee_paid AS amount
FROM   adoption WHERE adoption_date LIKE '2025%'
UNION  ALL
SELECT 'expense', expense_date, -amount
FROM   expense  WHERE expense_date  LIKE '2025%'
ORDER  BY dt;
```

```text
kind      dt          amount
--------  ----------  -------
adoption  2025-01-10  150.0
expense   2025-01-20  -330.0
expense   2025-02-05  -1950.0
expense   2025-03-14  -600.0
adoption  2025-07-01  400.0
```

<div dir="rtl">

> 🔑 **הקשר למודול 4:** כשכל טיפוס משנה בטבלה **נפרדת** (מתנדבים, מאמצים, וטרינרים), `UNION ALL` הוא הדרך לקבל את "כל האנשים" ברשימה אחת. ראינו את זה במודול 20, סעיף 8.

---

## 11. סדר הביצוע של שאילתה

עכשיו, כשיש לנו את כל החלקים — הסדר שבו SQL **באמת** מבצע שאילתה (שונה מהסדר שבו כותבים):

</div>

```text
   written order          execution order
   -------------          ---------------
   SELECT        5        1. FROM / JOIN     which tables, how they connect
   FROM          1        2. WHERE           filter rows
   WHERE         2        3. GROUP BY        make groups
   GROUP BY      3        4. HAVING          filter groups
   HAVING        4        5. SELECT          compute columns, aliases
   ORDER BY      6        6. ORDER BY        sort
   LIMIT         7        7. LIMIT           cut
```

<div dir="rtl">

**הסדר הזה מסביר כמעט כל הודעת שגיאה:**
- `WHERE SUM(x) > 5` — אסור: ב‑2 עוד אין קבוצות.
- `WHERE total > 5` (כינוי מ‑`SELECT`) — אסור: ב‑2 הכינוי עוד לא קיים.
- `ORDER BY total` — מותר: ב‑6 הכינוי כבר קיים.

---

## 12. שש טעויות נפוצות

| # | הטעות | מה קורה | התיקון |
|---|-------|----------|---------|
| 1 | **עמודה ב‑`SELECT` שאינה ב‑`GROUP BY`** | שגיאה ב‑Oracle, ניחוש ב‑SQLite | הוסיפו ל‑`GROUP BY`, או עטפו בפונקציה מצרפית |
| 2 | **פונקציה מצרפית ב‑`WHERE`** | `misuse of aggregate` | `HAVING` |
| 3 | **`COUNT(*)` אחרי `LEFT JOIN`** | קבוצה ריקה נספרת כ‑1 | `COUNT(right.id)` |
| 4 | **`NOT IN` מול עמודה עם NULL** | 0 שורות, בשקט | `NOT EXISTS` |
| 5 | **`GROUP BY name` במקום `GROUP BY id`** | שתי חיות באותו שם מתמזגות | קבצו לפי מזהה |
| 6 | **`UNION` כשרציתם `UNION ALL`** | שורות זהות מתמזגות — שני חיסונים של 80 ₪ הופכים לאחד, והסכום יוצא קטן מדי | `UNION ALL` — אלא אם רוצים במפורש להסיר כפילויות |

---

## 13. סיכום המודול

<div align="center">

### 🧠 שמונה נקודות

</div>

1. **`GROUP BY`** — פונקציה מצרפית **לכל קבוצה**. ב‑`SELECT`: רק עמודות הקיבוץ ופונקציות מצרפיות.
2. **`WHERE` מסנן שורות לפני; `HAVING` מסנן קבוצות אחרי.** פונקציה מצרפית — רק ב‑`HAVING`.
3. **`GROUP BY … HAVING COUNT(*) > 1`** = כפילויות. הכלי של הנרמול — ולפני כל `UNIQUE`.
4. **`ROLLUP` / `CUBE` / `GROUPING SETS`** מוסיפים שורות סיכום (Oracle). בכל מערכת: `UNION ALL`.
5. **תת‑שאילתה:** ערך אחד (`=`, `>`), רשימה (`IN`), או טבלה (`FROM` / `WITH`).
6. **מתואמת** רצה לכל שורה ומשתמשת בעמודה מבחוץ. **`EXISTS`** — "האם יש לפחות אחת".
7. **`NOT IN` + NULL = אפס שורות.** תמיד `NOT EXISTS`.
8. **`UNION` / `INTERSECT` / `EXCEPT` (`MINUS`)** — מחברים תוצאות לאורך. `UNION ALL` שומר כפילויות.

<div align="center">

---

*"שורות הן עובדות. קבוצות הן דפוסים.*
*ודפוסים — הם מה שמנהלים שואלים עליו."*

---

</div>

## 📎 המשך

| | |
|---|---|
| ❓ | [שאלות ותשובות](questions.md) |
| ✏️ | [תרגילים](exercises.md) — על [בסיס הנתונים המוכן](../../resources/shelter-db/) |
| ✅ | [פתרונות](solutions.md) — עם הפלט האמיתי |
| ⬅️ | [מודול 23 — SQL: פונקציות מצרפיות](../module-23-sql-aggregates/) |
| 🧭 | [מסלול הלימוד](../../LEARNING-PATH.md) — יחידה 6 הושלמה; הבאה: מודול 7 + 27 |
| ➡️ | [מודול 25 — SQL: מניפולציות לנתונים (DML)](../module-25-sql-dml/) |
| 🏠 | [חזרה לדף הקורס](../../) |

</div>
