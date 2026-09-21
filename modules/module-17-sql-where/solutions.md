<div dir="rtl">

# מודול 17 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 כל הפלטים אמיתיים — הופקו מ‑`shelter.sql`. **מספר השורות הוא חלק מהתשובה** — אם קיבלתם מספר אחר, משהו בתנאי שונה.

---

## ✅ תרגיל 1 — השוואות בסיסיות

</div>

```sql
-- a  (7 rows)
SELECT name, breed FROM animal WHERE species_id = 2;

-- b  (9 rows)
SELECT name, weight_kg FROM animal WHERE weight_kg < 5;

-- c  (6 rows)
SELECT first_name, role FROM person WHERE role <> 'adopter';

-- d  (7 rows)
SELECT expense_date, category, amount FROM expense WHERE amount > 1000;

-- e  (3 rows)
SELECT adoption_id, animal_id, fee_paid FROM adoption WHERE fee_paid = 200;
```

```text
-- a                      -- e
name   breed              adoption_id  animal_id  fee_paid
-----  -------            -----------  ---------  --------
Simba  Tabby              2            2          200.0
Mitzi                     3            5          200.0
Tom    Siamese            6            11         200.0
Nala
Oscar  Persian            <- three 200-shekel adoptions:
Lily                         one cat at the 2023 rate, and
Felix  Tabby                 two dogs over age 8 at HALF the 2024 rate.
                             Same number, three different reasons.
```

<div dir="rtl">

> 💡 **שימו לב ל‑ה':** שלושה אימוצים של 200 ₪ — מסיבות שונות לגמרי. `WHERE fee_paid = 200` מוצא אותם, אבל לא מסביר. זו הסיבה שבמודול 10 הוספנו `fee_basis`.

---

## ✅ תרגיל 2 — טקסט ותאריכים

### א. `Rocky` מול `rocky`

</div>

```sql
SELECT name FROM animal WHERE name = 'Rocky';   -- 1 row
SELECT name FROM animal WHERE name = 'rocky';   -- 0 rows
```

<div dir="rtl">

**השוואת ערכים רגישה לאותיות.** `'R'` ≠ `'r'`. מילות המפתח לא רגישות; **הערכים בגרשיים כן.**

</div>

```sql
-- b  (7 rows)
SELECT name, birth_date FROM animal WHERE birth_date > '2022-01-01';

-- c  (19 rows, both ways)
SELECT * FROM expense WHERE expense_date >= '2024-01-01' AND expense_date <= '2024-12-31';
SELECT * FROM expense WHERE expense_date BETWEEN '2024-01-01' AND '2024-12-31';

-- d  (3 rows)
SELECT first_name, joined_date FROM person WHERE joined_date < '2020-01-01';
-- -> Ruti 2013, Noa 2019, Dr. Ron 2015
```

<div dir="rtl">

### ה. ⚠️ `'01/01/2025'`

</div>

```sql
SELECT COUNT(*) FROM expense WHERE expense_date > '01/01/2025';
-- -> 22.  ALL the rows.  Including every 2024 expense.
```

<div dir="rtl">

**למה כל השורות?** כי ההשוואה היא **טקסט מול טקסט, תו אחר תו**:

</div>

```text
   '2024-01-05'  >  '01/01/2025'  ?
    ^                ^
    '2'          >   '0'    -> TRUE.  Decided on the FIRST character.
                                      The rest is never even looked at.
```

<div dir="rtl">

**כל תאריך** בבסיס הנתונים מתחיל ב‑`2`, וזה גדול מ‑`0`. אז **הכול** "גדול מ‑2025". אין שגיאה, יש תשובה — **ושגויה לחלוטין.**

> 🔑 **`YYYY-MM-DD` תמיד.** זה לא העדפה; זה הפורמט היחיד שבו `<` על טקסט נותן סדר זמן נכון.

---

## ✅ תרגיל 3 — BETWEEN ו‑IN

</div>

```sql
-- a  (6 rows) -- both are identical
SELECT name, weight_kg FROM animal WHERE weight_kg BETWEEN 10 AND 30;
SELECT name, weight_kg FROM animal WHERE weight_kg >= 10 AND weight_kg <= 30;
-- -> Luna 18.5, Bella 28.4, Max 12.3, Zoe 22.0, Daisy 15.6, Shadow 25.1
--    (Rocky 31.0 and Rex 38.7 are OUT -- above 30)

-- b  (3 rows)
SELECT name, status FROM animal WHERE status IN ('medical', 'quarantine', 'deceased');
-- -> Max, Nala, Daisy

-- c  (8 rows)
SELECT first_name, city FROM person WHERE city IN ('Haifa', 'Nesher', 'Karmiel');

-- d  (14 rows)
SELECT expense_date, category, amount FROM expense WHERE category NOT IN ('food', 'utilities');

-- e  (6 rows)
SELECT vaccination_id, animal_id, given_date
FROM   vaccination
WHERE  given_date BETWEEN '2024-04-01' AND '2024-06-30';
```

<div dir="rtl">

> 💡 **ב‑ה':** שימו לב ל‑`'2024-06-30'` ולא `'2024-06-31'` — יוני הוא 30 יום. ומה קורה אם כותבים `'2024-06-31'`? **עובד!** כי זה טקסט, ו‑`'2024-06-30' <= '2024-06-31'`. אבל זה מריח רע — ובבסיס נתונים עם `DATE` אמיתי זו שגיאה.

---

## ✅ תרגיל 4 — LIKE

</div>

```sql
-- a  (2)   Simba, Shadow
SELECT name FROM animal WHERE name LIKE 'S%';

-- b  (4)   Rocky, Lily, Daisy, Bunny
SELECT name FROM animal WHERE name LIKE '%y';

-- c  (6)   Bella, Thumper, Zoe, Rex, Charlie, Felix
SELECT name FROM animal WHERE name LIKE '%e%';

-- d  (5)   Luna, Coco, Nala, Lily, Kiwi
SELECT name FROM animal WHERE name LIKE '____';

-- e  (2)   Amir Levi, Dr. Ron Levi
SELECT first_name, last_name FROM person WHERE last_name LIKE 'L%';

-- f  (4)   all the "dry food, 20 sacks" rows
SELECT expense_date, description FROM expense WHERE description LIKE '%food%';
```

<div dir="rtl">

### ז. `LIKE 'Luna'` מול `LIKE 'Lun'`

| השאילתה | תוצאה | למה |
|----------|--------|------|
| `LIKE 'Luna'` | **1 שורה** | בלי `%` או `_`, `LIKE` הוא בדיוק `=`. `'Luna' = 'Luna'` |
| `LIKE 'Lun'` | **0 שורות** | `'Lun'` ≠ `'Luna'`. אין תו‑תבנית שיתפוס את ה‑`a` |

**מה שרוב האנשים מתכוונים:** `LIKE 'Lun%'`. **ה‑`%` הוא כל העניין.**

---

## ✅ תרגיל 5 — NULL

</div>

```sql
-- a  (7)
SELECT COUNT(*) FROM animal WHERE chip_number IS NULL;

-- b  (13)
SELECT COUNT(*) FROM animal WHERE chip_number IS NOT NULL;
-- 7 + 13 = 20  [OK] -- IS NULL / IS NOT NULL always partition the table completely
```

<div dir="rtl">

### ג. ⚠️ `= NULL`

</div>

```sql
SELECT name FROM animal WHERE chip_number = NULL;
-- -> 0 rows.  No error.  No warning.  Just nothing.
```

<div dir="rtl">

`chip_number = NULL` מחזיר **NULL**, לא TRUE. ו‑`WHERE` מכניס רק TRUE. **7 חיות נעלמו בשקט.**

</div>

```sql
-- d  (1)   Lily -- the only one missing BOTH
SELECT name FROM animal WHERE breed IS NULL AND birth_date IS NULL;

-- e  (11)  general expenses = no animal attached
SELECT expense_date, category, amount FROM expense WHERE animal_id IS NULL;
-- -> all the food, utilities, supplies and maintenance rows

-- f  (1)   Omer Dayan
SELECT first_name, last_name FROM person WHERE phone IS NULL;

-- g  (5)
SELECT name, weight_kg FROM animal WHERE weight_kg > 20 OR weight_kg IS NULL;
-- -> Rocky, Bella, Zoe, Rex, Shadow
```

<div dir="rtl">

> 💡 **ז':** אין חיות בלי משקל — כל 20 יש להן ערך. אז `OR weight_kg IS NULL` לא הוסיף כלום **הפעם**. אבל זה הדפוס הנכון: *"מעל 20, או לא ידוע"* — ואם מחר תיכנס חיה בלי משקל, היא תופיע. **מי שלא כותב את זה — מאבד אותה בשקט.**

---

## ✅ תרגיל 6 — AND / OR / NOT

</div>

```sql
-- a  (4)   Rocky, Bella, Rex, Shadow
SELECT name, weight_kg FROM animal WHERE species_id = 1 AND weight_kg > 25;

-- b  (9)   ALL the dogs -- because every animal over 25 kg is already a dog
SELECT name, species_id, weight_kg FROM animal WHERE species_id = 1 OR weight_kg > 25;

-- c  (4)   Mitzi, Oscar, Lily, Felix
SELECT name FROM animal WHERE species_id = 2 AND status = 'available';

-- d  (2)   Ruti, Noa
SELECT first_name FROM person WHERE role = 'volunteer' AND city = 'Haifa';

-- e  (4)   Coco, Thumper, Kiwi, Bunny
SELECT name, species_id FROM animal WHERE species_id <> 1 AND species_id <> 2;
-- also:  WHERE species_id NOT IN (1, 2)

-- f  (4)
SELECT expense_date, amount, animal_id
FROM   expense
WHERE  category = 'medical'
  AND  amount > 500
  AND  expense_date BETWEEN '2024-01-01' AND '2024-12-31';
-- -> 650 (Bella), 1200 (Rex), 890 (Luna), 2100 (Max)
```

<div dir="rtl">

> 💡 **ב' מלמד משהו:** `OR` הרחיב — אבל התוצאה זהה ל"כל הכלבים", כי אין חתול שוקל 25 ק"ג. `OR` **תמיד** מחזיר לפחות כמו כל צד לבדו.

---

## ✅ תרגיל 7 — המלכודת

### א. בלי סוגריים — 13 שורות

</div>

```sql
SELECT name, species_id, status
FROM   animal
WHERE  species_id = 1 OR species_id = 2 AND status = 'available';
```

```text
name     species_id  status
-------  ----------  ---------
Luna     1           adopted     <- adopted!
Rocky    1           available
Mitzi    2           available
Bella    1           adopted     <- adopted!
Max      1           medical     <- in treatment!
Zoe      1           adopted     <- adopted!
Oscar    2           available
Rex      1           available
Lily     2           available
Charlie  1           adopted     <- adopted!
Daisy    1           deceased    <- deceased!!
Felix    2           available
Shadow   1           available
```

<div dir="rtl">

### ב. עם סוגריים — 7 שורות

</div>

```sql
WHERE (species_id = 1 OR species_id = 2) AND status = 'available';
-- -> Rocky, Mitzi, Oscar, Rex, Lily, Felix, Shadow
```

<div dir="rtl">

### ג. מי נכנס בטעות

**כל הכלבים שאינם זמינים:** Luna, Bella, Zoe, Charlie (מאומצים), Max (בטיפול), Daisy (**מתה**).

**למה:** `AND` נקשר קודם. בסיס הנתונים קרא `species_id = 1 OR (species_id = 2 AND status = 'available')`. ה‑`status` חל **רק על חתולים**. כלבים נכנסו כולם — בלי שום תנאי.

**דוח שהיה מוצע לרותי עם כלבה מתה.** בלי שגיאה. בלי אזהרה.

### ד. עם `IN`

</div>

```sql
WHERE species_id IN (1, 2) AND status = 'available';    -- 7 rows, no parentheses needed
```

<div dir="rtl">

### ה. "כלבים זמינים, או חתולים בהסגר"

</div>

```sql
WHERE (species_id = 1 AND status = 'available')
   OR (species_id = 2 AND status = 'quarantine');
-- -> Rocky, Rex, Shadow (available dogs) + Nala (quarantined cat) = 4 rows
```

<div dir="rtl">

**האם כאן צריך סוגריים?** מבחינה טכנית **לא** — `AND` נקשר קודם ממילא, וזה בדיוק מה שרוצים. **אבל כתבו אותם בכל זאת.** מי שקורא בעוד חודש לא צריך לזכור כללי קדימות. סוגריים מיותרים לא עולים כלום; סוגריים חסרים עולים דוח שגוי.

---

## ✅ תרגיל 8 — שאילתות משולבות

</div>

```sql
-- a  (3)   Oscar, Felix, Shadow
SELECT name, weight_kg, chip_number
FROM   animal
WHERE  status = 'available'
  AND  chip_number IS NOT NULL
  AND  weight_kg BETWEEN 4 AND 30;
-- Rocky (31.0) and Rex (38.7) are too heavy; Mitzi/Lily have no chip

-- b  (7)
SELECT expense_date, amount, animal_id
FROM   expense
WHERE  category = 'medical'
  AND  animal_id IS NOT NULL
  AND  amount > 400;

-- c  (1)   adoption 1 -- Luna, returned 2024-06-01
SELECT adoption_id, animal_id, adoption_date, returned_date
FROM   adoption
WHERE  returned_date IS NOT NULL;

-- d  (5)   adoptions 3, 4, 5, 6, 8
SELECT adoption_id, animal_id, adoption_date
FROM   adoption
WHERE  returned_date IS NULL
  AND  adoption_date BETWEEN '2024-01-01' AND '2024-12-31';

-- e  (7)
SELECT vaccination_id, animal_id, vaccine_type_id, given_date
FROM   vaccination
WHERE  vet_id = 4
  AND  vaccine_type_id IN (1, 2)
  AND  given_date BETWEEN '2024-01-01' AND '2024-12-31';

-- f  (3)   Mitzi, Max, Lily
SELECT name, status
FROM   animal
WHERE  (name LIKE 'L%' OR name LIKE 'M%')
  AND  status <> 'adopted';
-- Luna starts with L but is adopted -> OUT
```

<div dir="rtl">

> 💡 **ב‑ו' הסוגריים הכרחיים.** בלעדיהם: `name LIKE 'L%' OR (name LIKE 'M%' AND status <> 'adopted')` — ולונה המאומצת הייתה נכנסת.

---

## ✅ תרגיל 9 — מצאו את הבאג

| | מה היא אמורה | מה היא עושה | התיקון |
|---|-------------|-------------|---------|
| **a** | חיות בלי גזע | **0 שורות** — `= NULL` לעולם לא TRUE | `breed IS NULL` |
| **b** | כלבים וחתולים מעל 20 | **כל הכלבים** + חתולים מעל 20 (אין כאלה) — קדימות | `species_id IN (1,2) AND weight_kg > 20` |
| **c** | לונה | **0 שורות** — אות קטנה | `= 'Luna'` |
| **d** | הוצאות ינואר 2024 | ✅ **נכונה!** | — |
| **e** | שמות שמתחילים ב‑T | **0 שורות** — `LIKE 'T'` הוא `= 'T'` | `LIKE 'T%'` |
| **f** | כולם חוץ מווטרינרים | **0 שורות** — `NOT IN` עם NULL | `role <> 'vet'` או `NOT IN ('vet')` |
| **g** | 3 הכבדות ביותר | **3 שורות כלשהן** (Luna, Simba, Rocky — לפי סדר אחסון) | צריך `ORDER BY weight_kg DESC` — מודול 18 |

**הנכונה: d.** `BETWEEN` על תאריכי ISO — בדיוק כמו שצריך.

> 🔑 **שימו לב ש‑5 מתוך 7 הבאגים מחזירים 0 שורות או "תוצאה סבירה" בלי שגיאה.** זו הסכנה ב‑`WHERE`: הוא לא נכשל בקול. הוא מחזיר תשובה — לא נכונה.

---

## ✅ תרגיל 10 — הדוחות של רותי

</div>

```sql
-- a  (5)   Rocky, Oscar, Rex, Felix, Shadow
SELECT name, weight_kg, chip_number
FROM   animal
WHERE  status = 'available'
  AND  chip_number IS NOT NULL
  AND  weight_kg >= 3;

-- b  (2)   330 (Felix, eye infection) + 600 (Rocky, hip x-ray)
SELECT expense_date, amount, animal_id
FROM   expense
WHERE  category = 'medical'
  AND  expense_date BETWEEN '2025-01-01' AND '2025-03-31';

-- c  (3)   Yossi (Tel Aviv), Shira (Karmiel), Eitan (Nahariya)
SELECT first_name || ' ' || last_name AS full_name, city
FROM   person
WHERE  role = 'adopter'
  AND  city <> 'Haifa';

-- d  (1)   Nala -- in quarantine, no chip yet
SELECT name, status
FROM   animal
WHERE  status IN ('quarantine', 'medical')
  AND  chip_number IS NULL;

-- e  (2)   intakes 9 (Nala, Bat Galim) and 14 (Lily, Kiryat Eliezer)
SELECT intake_id, animal_id, intake_date, location
FROM   intake
WHERE  intake_type = 'stray'
  AND  brought_by = 2
  AND  intake_date BETWEEN '2024-01-01' AND '2024-12-31';
```

<div dir="rtl">

### ו. ⭐⭐ "כל החיות שאני **לא** יכולה להציע — ולמה"

**השאלה הזאת דורשת לחשוב לפני שכותבים.** מה מונע אימוץ?

1. הסטטוס אינו `available` — מאומצת, בטיפול, בהסגר, מתה
2. **וגם:** אין שבב — במקלט לא מוסרים חיה בלי שבב

</div>

```sql
SELECT name, status, chip_number
FROM   animal
WHERE  status <> 'available'
   OR  chip_number IS NULL;
```

```text
name     status      chip_number
-------  ----------  -----------
Luna     adopted     985100001     <- already adopted
Simba    adopted     985100002
Mitzi    available                 <- available, but NO CHIP
Bella    adopted     985100005
Tom      adopted     985100006
Coco     available                 <- available, but NO CHIP
Max      medical     985100008     <- in treatment
Nala     quarantine                <- quarantine AND no chip
Thumper  adopted
Zoe      adopted     985100011
Lily     available                 <- available, but NO CHIP
Charlie  adopted     985100015
Kiwi     adopted
Daisy    deceased    985100017     <- deceased
Bunny    available                 <- available, but NO CHIP
```

<div dir="rtl">

**15 שורות.** ו‑20 − 15 = **5** — בדיוק החיות מסעיף א'. השאילתות משלימות זו את זו.

**"ולמה":** רואים בעיניים — או מהסטטוס או מהשבב הריק. **להציג את הסיבה כטקסט** ("no chip" / "adopted") דורש `CASE` — מודול 20.

> 🎓 **שימו לב לדרך:** רותי שאלה שאלה **עסקית** ("מה אני לא יכולה להציע"), לא שאלה טכנית. **התרגום** — "סטטוס לא זמין **או** בלי שבב" — הוא העבודה. ה‑SQL אחרי זה הוא שתי שורות.

---

<div align="center">

### 🎯 סיימתם את מודול 17 — ואת יחידה 2!

עכשיו אתם עונים על **ארבע** מתוך שמונה השאלות של רותי.
במודול הבא — `ORDER BY`: לא רק **אילו** שורות, אלא **באיזה סדר**.

---

### ➡️ [מודול 18 — SQL: מיונים](../module-18-sql-order-by/)

</div>

---

<div align="center">

**🧭 ניווט המודול**

</div>

| 📖 [חזרה למודול](README.md) | ❓ [שאלות ותשובות](questions.md) | ✏️ [לתרגילים](exercises.md) | 🏠 [דף הקורס](../../) |
|---|---|---|---|

</div>
