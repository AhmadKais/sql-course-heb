<div dir="rtl">

# מודול 23 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 כל הפלטים אמיתיים, מהרצה על בסיס הנתונים המוכן, נכון ל‑`'2026-09-21'`.

---

## ✅ תרגיל 1 — חמש הפונקציות

</div>

```sql
-- a   4
SELECT COUNT(*) FROM person WHERE role = 'volunteer';

-- b   2013-03-01 | 2024-02-14
SELECT MIN(joined_date), MAX(joined_date) FROM person WHERE role = 'volunteer';

-- c
SELECT SUM(cost) AS total, ROUND(AVG(cost), 2) AS avg, COUNT(*) AS n FROM vaccination;
```

```text
total   avg    n
------  -----  --
2370.0  84.64  28
```

```sql
-- d   1950.0 | 2024-01-12
SELECT MAX(amount)       FROM expense WHERE category = 'food';
SELECT MIN(expense_date) FROM expense WHERE category = 'medical';

-- e   9 | 22.09
SELECT COUNT(*) AS dogs, ROUND(AVG(weight_kg), 2) AS avg_kg FROM animal WHERE species_id = 1;
```

<div dir="rtl">

---

## ✅ תרגיל 2 — שלושה סוגי COUNT

</div>

```sql
-- a
SELECT COUNT(*) AS people, COUNT(phone) AS with_phone, COUNT(DISTINCT city) AS cities
FROM   person;
```

```text
people  with_phone  cities
------  ----------  ------
12      11          7
```

```sql
-- b   2 | 19 | 9
SELECT COUNT(*)                 FROM intake WHERE brought_by IS NULL;
SELECT COUNT(brought_by)        FROM intake;
SELECT COUNT(DISTINCT brought_by) FROM intake;

-- c   11 shots | 8 animals
SELECT COUNT(*)                  FROM vaccination WHERE given_date LIKE '2024%';
SELECT COUNT(DISTINCT animal_id) FROM vaccination WHERE given_date LIKE '2024%';
```

<div dir="rtl">

**ד.** `COUNT(*)` = **20**, `COUNT(breed)` = **16**. `COUNT(breed)` מדלג על 4 החיות שהגזע שלהן NULL. "כמה חיות יש" = **`COUNT(*)`** — סופר שורות, לא ערכים.

> 💡 **שימו לב לסעיף ב':** 2 + 19 = 21 = כל הקליטות. `COUNT(*) WHERE … IS NULL` + `COUNT(עמודה)` = `COUNT(*)` — תמיד. זו בדיקה טובה שהבנתם.

---

## ✅ תרגיל 3 — NULL וקבוצה ריקה

</div>

```sql
-- a
SELECT ROUND(AVG((JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25), 2)       AS avg_age,
       ROUND(SUM((JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25) / COUNT(*), 2) AS wrong
FROM   animal;
-- 5.57 | 4.73
```

<div dir="rtl">

`AVG` מחלק ב‑17 (מי שהגיל שלו ידוע). `SUM / COUNT(*)` מחלק ב‑20 — כאילו ל‑Coco, Lily ו‑Kiwi גיל 0. **`AVG` צודק.** (`SUM / COUNT(birth_date)` היה נותן גם הוא 5.57.)

</div>

```sql
-- b   SUM -> NULL, COUNT -> 0
SELECT SUM(amount), COUNT(*) FROM expense WHERE category = 'toys';

-- fixed
SELECT COALESCE(SUM(amount), 0) FROM expense WHERE category = 'toys';     -- 0

-- c   any filter that matches no row, e.g.
SELECT MAX(weight_kg) FROM animal WHERE species_id = 99;                  -- NULL
```

<div dir="rtl">

**ג.** `MAX` (וגם `MIN`, `SUM`, `AVG`) מחזיר NULL כשאין **אף ערך** שאינו NULL: אין שורות בכלל, או שכל הערכים NULL (`SELECT MAX(breed) FROM animal WHERE breed IS NULL`).

---

## ✅ תרגיל 4 — עם WHERE ועם JOIN

</div>

```sql
-- a   16920.0
SELECT SUM(amount) FROM expense WHERE expense_date BETWEEN '2024-01-01' AND '2024-12-31';

-- b   2520.0
SELECT SUM(e.amount)
FROM   expense e
JOIN   animal a ON a.animal_id = e.animal_id
WHERE  a.name = 'Max';

-- c   7 | 4.13 | 2.9 | 5.5
SELECT COUNT(*), ROUND(AVG(a.weight_kg), 2), MIN(a.weight_kg), MAX(a.weight_kg)
FROM   animal a
JOIN   species s ON s.species_id = a.species_id
WHERE  s.name = 'Cat';

-- d
SELECT SUM(ad.fee_paid) AS haifa_total
FROM   adoption ad
JOIN   person p ON p.person_id = ad.adopter_id
WHERE  p.city = 'Haifa';
-- 1250.0   (Dana 300 + 400, Lior 200 + 150, Omer 200)
```

<div dir="rtl">

---

## ✅ תרגיל 5 — ספירה מותנית

</div>

```sql
-- a
SELECT SUM(CASE WHEN sex = 'M' THEN 1 ELSE 0 END) AS males,
       SUM(CASE WHEN sex = 'F' THEN 1 ELSE 0 END) AS females,
       SUM(CASE WHEN sex = 'U' THEN 1 ELSE 0 END) AS unknown
FROM   animal;
```

```text
males  females  unknown
-----  -------  -------
10     9        1
```

```sql
-- b
SELECT SUM(CASE WHEN STRFTIME('%Y', adoption_date) = '2023' THEN fee_paid ELSE 0 END) AS y2023,
       SUM(CASE WHEN STRFTIME('%Y', adoption_date) = '2024' THEN fee_paid ELSE 0 END) AS y2024,
       SUM(CASE WHEN STRFTIME('%Y', adoption_date) = '2025' THEN fee_paid ELSE 0 END) AS y2025
FROM   adoption;
```

```text
y2023  y2024   y2025
-----  ------  -----
500.0  1150.0  550.0
```

```sql
-- c
SELECT SUM(CASE WHEN category = 'medical'   THEN amount ELSE 0 END) AS medical,
       SUM(CASE WHEN category = 'food'      THEN amount ELSE 0 END) AS food,
       SUM(CASE WHEN category = 'utilities' THEN amount ELSE 0 END) AS utilities
FROM   expense;
```

```text
medical  food    utilities
-------  ------  ---------
7470.0   7490.0  3770.0
```

```sql
-- d   40.0
SELECT ROUND(100.0 * SUM(CASE WHEN status = 'adopted' THEN 1 ELSE 0 END) / COUNT(*), 1)
FROM   animal;

-- e   11 | 8 | 2
SELECT SUM(CASE WHEN intake_type = 'stray'     THEN 1 ELSE 0 END) AS strays,
       SUM(CASE WHEN intake_type = 'surrender' THEN 1 ELSE 0 END) AS surrenders,
       SUM(CASE WHEN intake_type = 'transfer'  THEN 1 ELSE 0 END) AS transfers
FROM   intake;
```

<div dir="rtl">

> 💡 **סעיף ב' ו‑ג' הם "טבלת ציר" (pivot)** — ערכים מעמודה אחת (שנה, קטגוריה) הופכים לכותרות עמודות. זה מה שאקסל עושה ב"PivotTable". החיסרון: צריך לדעת מראש את כל הערכים. במודול 24, `GROUP BY` ייתן את אותו מידע **בשורות** — לכל ערך שקיים.

---

## ✅ תרגיל 6 — המלכודות

</div>

```sql
-- a   SQLite: Zoe | 2016-01-01  (a lucky guess)   Oracle: ORA-00937
SELECT name, MIN(birth_date) FROM animal;

-- the correct way
SELECT name, birth_date
FROM   animal
WHERE  birth_date = (SELECT MIN(birth_date) FROM animal);
-- Zoe | 2016-01-01

-- b   8
SELECT COUNT(*) FROM animal WHERE weight_kg > (SELECT AVG(weight_kg) FROM animal);
```

<div dir="rtl">

**ג.** ל‑Rocky יש **הוצאה אחת** (600 ₪, צילום ירך) ו‑**4 חיסונים**. ה‑JOIN יוצר שורה לכל **צירוף** של הוצאה וחיסון: 1 × 4 = 4 שורות, וכל אחת עם `amount = 600`. `SUM` = 2400 — **פי 4 מהאמת**.

</div>

```text
   Rocky -- expense 22 (600) -- vaccination 5
   Rocky -- expense 22 (600) -- vaccination 6
   Rocky -- expense 22 (600) -- vaccination 27      4 rows, the 600 counted 4 times
   Rocky -- expense 22 (600) -- vaccination 28
```

```sql
-- correct: only the table you aggregate
SELECT SUM(e.amount)
FROM   expense e
JOIN   animal a ON a.animal_id = e.animal_id
WHERE  a.name = 'Rocky';                           -- 600.0
```

<div dir="rtl">

> 🔑 **שתי טבלאות "רבים" באותו JOIN = מכפלה.** זה הבאג הכי נפוץ בדוחות אמיתיים — והכי מסוכן, כי המספר נראה סביר.

</div>

```sql
-- d
SELECT (SELECT COUNT(*) FROM animal WHERE status = 'available')                  AS waiting,
       (SELECT COUNT(*) FROM adoption)                                           AS adoptions,
       (SELECT SUM(fee_paid) FROM adoption)                                      AS income,
       (SELECT SUM(amount)   FROM expense)                                       AS expenses,
       (SELECT SUM(fee_paid) FROM adoption) - (SELECT SUM(amount) FROM expense)  AS balance;
```

```text
waiting  adoptions  income  expenses  balance
-------  ---------  ------  --------  --------
9        9          2200.0  19800.0   -17600.0
```

<div dir="rtl">

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[❓ לשאלות](questions.md)**

</div>

</div>

<!-- w3schools:start -->
<div dir="rtl">

---

## 🌐 תרגול ב‑W3Schools: פתרונות

> כל השאילתות כאן הורצו ב‑W3Schools. מספר הרשומות הוא מה שהאתר מחזיר.

**W1.**

```sql
SELECT AVG(Products.Price) AS AvgPrice, MAX(Products.Price) AS MaxPrice, MIN(Products.Price) AS MinPrice FROM Products;
```

**1** רשומות. השורה הראשונה: `28.866363 · 263.50 · 2.50`

**W2.**

```sql
SELECT COUNT(*) AS cnt FROM Products WHERE Products.CategoryID = 1;
```

**1** רשומות. השורה הראשונה: `12`


</div>
<!-- w3schools:end -->
