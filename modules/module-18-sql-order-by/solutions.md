<div dir="rtl">

# מודול 18 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 כל הפלטים אמיתיים — מ‑`shelter.sql` ב‑SQLite. **איפה שהתנהגות Oracle שונה — מסומן.**

---

## ✅ תרגיל 1 — מיון בסיסי

</div>

```sql
-- a  Kiwi (0.04) first ... Rex (38.7) last
SELECT name, weight_kg FROM animal ORDER BY weight_kg;

-- b  Rex first ... Kiwi last
SELECT name, weight_kg FROM animal ORDER BY weight_kg DESC;

-- c  Almog, Bar, Cohen, Dayan, Golan, Katz, Levi, Levi, Mizrahi, Nahum, Peretz, Shalev
SELECT first_name, last_name FROM person ORDER BY last_name;

-- d  2025-03-14 first ... 2024-01-05 last
SELECT expense_date, category, amount FROM expense ORDER BY expense_date DESC;

-- e  100, 150, 200, 200, 200, 250, 300, 400, 400
SELECT adoption_id, fee_paid FROM adoption ORDER BY fee_paid;
```

<div dir="rtl">

> 💡 **ב‑ג':** שני `Levi` — Amir ו‑Dr. Ron. **הסדר ביניהם לא מוגדר.** ראו תרגיל 3 — צריך מפתח שני.

---

## ✅ תרגיל 2 — WHERE + ORDER BY

</div>

```sql
-- a  Rex, Rocky, Bella, Shadow, Zoe, Luna, Daisy, Max, Charlie
SELECT name, weight_kg FROM animal WHERE species_id = 1 ORDER BY weight_kg DESC;

-- b  Bunny, Coco, Felix, Lily, Mitzi, Oscar, Rex, Rocky, Shadow
SELECT name FROM animal WHERE status = 'available' ORDER BY name;

-- c  2100, 1200, 890, 650, 600, 450, 420, 380, 330, 275, 175
SELECT expense_date, amount FROM expense WHERE category = 'medical' ORDER BY amount DESC;

-- d  Ruti 2013, Dr. Ron 2015, Noa 2019, Dana 2023, Lior 2024, Omer 2024
SELECT first_name, joined_date FROM person WHERE city = 'Haifa' ORDER BY joined_date;
```

<div dir="rtl">

### ה. `ORDER BY` לפני `WHERE`

</div>

```sql
SELECT first_name FROM person ORDER BY joined_date WHERE city = 'Haifa';
```

```text
Error: near "WHERE": syntax error
```

<div dir="rtl">

**סדר החלקים קבוע:** `SELECT → FROM → WHERE → ORDER BY → LIMIT`. אי אפשר להחליף. המילה אחרי `near` — `WHERE` — היא המקום שבו בסיס הנתונים הפסיק להבין.

---

## ✅ תרגיל 3 — שני מפתחות

</div>

```sql
-- a
SELECT name, species_id FROM animal ORDER BY species_id, name;
-- -> Bella, Charlie, Daisy, Luna, Max, Rex, Rocky, Shadow, Zoe (dogs A-Z), then cats A-Z...

-- b
SELECT name, species_id, weight_kg FROM animal ORDER BY species_id, weight_kg DESC;
-- -> Rex 38.7, Rocky 31.0 ... Charlie 7.2 (dogs), Oscar 5.5 ... Nala 2.9 (cats), ...

-- c
SELECT first_name, last_name, role FROM person ORDER BY role, last_name;
-- -> adopters: Bar, Cohen, Dayan, Katz, Mizrahi, Shalev
--    vets:     Levi, Nahum
--    volunteers: Almog, Golan, Levi, Peretz

-- d
SELECT category, amount FROM expense ORDER BY category, amount DESC;
```

<div dir="rtl">

### ה. `ORDER BY species_id DESC, weight_kg`

</div>

```text
name     species_id  weight_kg
-------  ----------  ---------
Kiwi     4           0.04       <- parrots now FIRST (species descending)
Coco     4           0.1
Bunny    3           1.5
Thumper  3           1.8
Nala     2           2.9        <- and within each species: LIGHTEST first
...
Rex      1           38.7       <- dogs last, Rex at the very end
```

<div dir="rtl">

**מה השתנה:** שני הדברים. המינים התהפכו (4 ⟵ 1), **וגם** המשקל התהפך (הסרנו את `DESC` ממנו). **מה לא השתנה:** העיקרון — עדיין מקבצים לפי מין ומסדרים בתוכו.

---

## ✅ תרגיל 4 — "N הראשונים"

</div>

```sql
-- a  Rex 38.7, Rocky 31.0, Bella 28.4
SELECT name, weight_kg FROM animal ORDER BY weight_kg DESC LIMIT 3;

-- b  Kiwi 0.04, Coco 0.1, Bunny 1.5
SELECT name, weight_kg FROM animal ORDER BY weight_kg LIMIT 3;

-- c  2100 (medical), 1950, 1900, 1850, 1790 (all food)
SELECT expense_date, category, amount FROM expense ORDER BY amount DESC LIMIT 5;

-- d  animal 1 (Luna), 2025-07-01
SELECT animal_id, adoption_date FROM adoption ORDER BY adoption_date DESC LIMIT 1;

-- e  Ruti, 2013-03-01
SELECT first_name, joined_date FROM person ORDER BY joined_date LIMIT 1;
```

<div dir="rtl">

### ו. `LIMIT 3` בלי `ORDER BY`

</div>

```text
name   weight_kg
-----  ---------
Luna   18.5       <- these are just the first 3 rows STORED.
Simba  4.2           Not the heaviest. Not the lightest. Just... three.
Rocky  31.0
```

<div dir="rtl">

**לא "3 הכבדות".** שלוש שורות בסדר האחסון. **וזה הדוח שהמנהל מהסיפור הזמין לפיו מלאי.**

---

## ✅ תרגיל 5 — כינויים וביטויים

</div>

```sql
-- a
SELECT name, weight_kg * 2.2 AS lb FROM animal ORDER BY lb DESC;
-- -> Rex 85.14, Rocky 68.2, Bella 62.48, ...

-- b
SELECT adoption_id, fee_paid, fee_paid * 1.18 AS with_vat FROM adoption ORDER BY with_vat;
-- -> 118, 177, 236, 236, 236, 295, 354, 472, 472

-- d
SELECT first_name || ' ' || last_name AS full_name FROM person ORDER BY full_name;
-- -> Amir Levi, Dana Cohen, Dr. Maya Nahum, Dr. Ron Levi, Eitan Shalev, ...
```

<div dir="rtl">

### ג. ⚠️ `WHERE lb > 40`

| הכלי | מה קורה |
|------|----------|
| **Programiz (SQLite)** | ✅ **עובד** — מחזיר Luna, Rocky, Bella, Zoe, Rex, Shadow |
| **Oracle** | ❌ `ORA-00904: "LB": invalid identifier` |

**למה Oracle נכשל:** `WHERE` רץ **לפני** `SELECT`. הכינוי `lb` עוד לא נוצר.
**למה SQLite עובד:** הוא **חורג מהתקן** ומרשה. זו נוחות — וזו מלכודת: שאילתה שעובדת בתרגול תיכשל בבחינה.

**הכתיבה הנכונה (עובדת בכל מקום):**

</div>

```sql
SELECT name, weight_kg * 2.2 AS lb
FROM   animal
WHERE  weight_kg * 2.2 > 40      -- repeat the expression, not the alias
ORDER  BY lb DESC;               -- alias is fine HERE
```

<div dir="rtl">

### ה. מיון לפי `full_name` — פרטי או משפחה?

**לפי שם פרטי.** `full_name` מתחיל בשם הפרטי, ומיון טקסט הוא תו‑תו משמאל. `Amir Levi` לפני `Dana Cohen` — למרות ש‑Cohen לפני Levi.

**אם רוצים לפי משפחה:** `ORDER BY last_name, first_name` — על העמודות המקוריות, לא על הכינוי.

---

## ✅ תרגיל 6 — NULL במיון

### א+ב. איפה NULL

</div>

```text
ORDER BY birth_date          ORDER BY birth_date DESC
(ascending)                  (descending)

name  birth_date             name  birth_date
----  ----------             ----  ----------
Coco              <- NULL    Nala  2024-03-01
Lily              <- NULL    Bunny 2024-01-01
Kiwi              <- NULL    ...
Zoe   2016-01-01             Zoe   2016-01-01
...                          Coco              <- NULL
Nala  2024-03-01             Lily              <- NULL
                             Kiwi              <- NULL

SQLite: NULL is the SMALLEST value. First in ASC, last in DESC.
Oracle: NULL is the LARGEST value. Last in ASC, first in DESC.   <- opposite!
```

<div dir="rtl">

### ג. ⚠️ "3 הוותיקות"

</div>

```sql
SELECT name, birth_date FROM animal ORDER BY birth_date LIMIT 3;
```

```text
name  birth_date
----  ----------
Coco
Lily
Kiwi
```

<div dir="rtl">

**שגוי לחלוטין.** אלה לא הוותיקות — אלה שלוש חיות שאין להן תאריך. **הדוח יצא, נראה תקין, ושגוי ב‑100%.** בלי שגיאה.

### ד. התיקון

</div>

```sql
SELECT   name, birth_date
FROM     animal
ORDER BY birth_date IS NULL,     -- 0 for known dates, 1 for NULL -> known first
         birth_date
LIMIT    3;
-- -> Zoe 2016, Rex 2017, Bella 2018   [OK]
```

<div dir="rtl">

### ה+ו. לפי גזע, NULL בסוף — שתי גרסאות

</div>

```sql
-- SQLite (Programiz)
SELECT name, breed FROM animal ORDER BY breed IS NULL, breed;

-- Oracle
SELECT name, breed FROM animal ORDER BY breed NULLS LAST;
```

```text
name     breed
-------  ---------------
Max      Beagle
Kiwi     Budgie
Coco     Cockatiel
...
Simba    Tabby
Felix    Tabby
Mitzi                     <- the four with no breed, at the end
Nala
Lily
Bunny
```

<div dir="rtl">

> 🔑 **הטריק של SQLite עובד גם ב‑Oracle** (`IS NULL` הוא ביטוי חוקי בכל מקום). `NULLS LAST` **לא** עובד ב‑SQLite. אז אם צריך אחד לשניהם — הטריק.

---

## ✅ תרגיל 7 — מיון טקסט

### א. אורך שם

</div>

```sql
SELECT name, LENGTH(name) AS len FROM animal ORDER BY LENGTH(name) DESC;
-- -> Thumper 7, Charlie 7, Shadow 6, Simba 5, Rocky 5, ... , Tom 3, Max 3, Zoe 3, Rex 3
```

<div dir="rtl">

### ב. אותיות מעורבות

</div>

```text
word
------
Apple
Banana
mango
zebra
```

<div dir="rtl">

**נראה בסדר?** רק במקרה — כי `Apple` ו‑`Banana` גם ככה ראשונות. נסו להוסיף `'apple'` באות קטנה: היא תיפול **אחרי** `zebra`. כל האותיות הגדולות (65–90) לפני כל הקטנות (97–122).

### ג. התיקון

</div>

```sql
SELECT word
FROM   (SELECT 'zebra' AS word UNION SELECT 'Apple'
        UNION SELECT 'mango' UNION SELECT 'Banana')
ORDER  BY UPPER(word);
-- -> Apple, Banana, mango, zebra  (now case-insensitive)
```

<div dir="rtl">

⚠️ **למה תת‑שאילתה?** SQLite לא מרשה ביטוי ב‑`ORDER BY` ישירות אחרי `UNION` — רק שמות עמודות. העטיפה פותרת את זה. (על טבלה רגילה, `ORDER BY UPPER(name)` עובד ישירות.)

### ד. מספרים כטקסט

</div>

```text
n
--
1
10      <- '10' before '2': compared character by character, '1' < '2'
2
20
```

<div dir="rtl">

**הלקח:** מספר ששמור כטקסט ממוין כטקסט. **אם זה מספר — שיהיה מספר** (מודול 7, תחומים). ואם כבר תקוע כטקסט: `ORDER BY CAST(n AS INTEGER)` — מודול 20.

---

## ✅ תרגיל 8 — שוויון בקצה

### א+ב.

</div>

```sql
SELECT name, species_id FROM animal ORDER BY species_id LIMIT 3;
-- -> Luna, Rocky, Bella   (this time)
```

<div dir="rtl">

**שלוש פעמים — אותה תוצאה.** אבל **אין הבטחה**: יש 9 כלבים עם `species_id = 1`, כולם שווים למפתח המיון. בסיס הנתונים בוחר שלושה. היום הוא בחר לפי סדר האחסון; אחרי `UPDATE`, אחרי שדרוג, אחרי אינדקס חדש — עלול לבחור אחרת.

### ג. דטרמיניסטי

</div>

```sql
SELECT name, species_id FROM animal ORDER BY species_id, animal_id LIMIT 3;
-- -> ALWAYS Luna (1), Rocky (3), Bella (5) -- the three lowest ids among dogs
```

<div dir="rtl">

### ד. אימוצים יקרים — שני 400

</div>

```sql
SELECT   adoption_id, animal_id, fee_paid
FROM     adoption
ORDER BY fee_paid DESC,
         adoption_id          -- tie-breaker: lower id first
LIMIT    3;
-- -> 7 (400), 8 (400), 1 (300)
```

<div dir="rtl">

> 🔑 **הכלל:** `LIMIT` + מפתח שיכול להיות שווה = הוסיפו מפתח **ייחודי** אחרון. תמיד.

---

## ✅ תרגיל 9 — סימולציית ראיון

| # | תשובה טובה | ⭐ המלכודת שהופכת אותה למצוינת |
|---|-------------|----------------------------------|
| 1 | `WHERE` בוחר **אילו** שורות; `ORDER BY` — **באיזה סדר** | "ו‑`WHERE` רץ קודם, אז הוא גם מקטין את מה ש‑`ORDER BY` צריך למיין" |
| 2 | 5 שורות **כלשהן** | "ראיתי דוח שעבד שנתיים ככה ונשבר אחרי שדרוג" |
| 3 | תלוי בבסיס הנתונים — ראשון ב‑SQLite, אחרון ב‑Oracle | "ולכן אני תמיד כותב `NULLS LAST` או `IS NULL` כמפתח" |
| 4 | סדר הביצוע — `WHERE` לפני `SELECT`, `ORDER BY` אחרי | "SQLite חורג ומרשה, אז שאילתה שעובדת בתרגול עלולה להיכשל בייצור" |
| 5 | `FROM → WHERE → SELECT → ORDER BY → LIMIT` | "ולכן `LIMIT` לא מאיץ — הוא רץ אחרון" |
| 6 | `a` **עולה** — `DESC` חל רק על `b` | "טעות נפוצה, ראיתי אותה בקוד ייצור" |

**הדירוג העצמי:** אם עניתם נכון על 5+ ובקול בלי גמגום — אתם מוכנים לשאלה כזאת בראיון. אם גמגמתם — זה בדיוק מה שיקרה בראיון. **תרגלו בקול.**

---

## ✅ תרגיל 10 — הדוחות של רותי

</div>

```sql
-- a  Shadow, Rocky, Rex | Mitzi, Felix, Oscar, Lily(NULL) | Bunny | Coco(NULL)
SELECT   name, species_id, weight_kg, birth_date
FROM     animal
WHERE    status = 'available'
ORDER BY species_id,
         birth_date IS NULL,    -- second key: unknowns last WITHIN each species
         weight_kg;

-- b  2100, 1200, 890, 650, 450, 420, 380, 275, 175
SELECT   expense_date, amount, animal_id
FROM     expense
WHERE    category = 'medical'
  AND    expense_date BETWEEN '2024-01-01' AND '2024-12-31'
ORDER BY amount DESC,
         expense_date;          -- tie-breaker (no ties this time, but safe)

-- c  Ruti 2013, Noa 2019, Amir 2022, Tamar 2024
SELECT   first_name, last_name, joined_date
FROM     person
WHERE    role = 'volunteer'
ORDER BY joined_date,
         last_name;

-- d
SELECT   vaccination_id, animal_id, given_date
FROM     vaccination
ORDER BY given_date DESC,
         vaccination_id DESC    -- two on 2025-03-12: without this, order is undefined
LIMIT    3;
-- -> 28 (2025-05-30), 26 (2025-03-12), 25 (2025-03-12)
```

<div dir="rtl">

> 💡 **ב‑ד' יש שוויון אמיתי:** חיסונים 25 ו‑26 ניתנו באותו יום (שני חיסונים ל‑Shadow). בלי שובר השוויון — הסדר ביניהם לא מובטח.

### ה. "הכי כבדה בכל מין"

**❌ לא אפשרי עם מה שלמדנו.** `ORDER BY species_id, weight_kg DESC` מסדר נכון — אבל `LIMIT 1` ייתן רק את **הראשונה בכלל**, לא אחת לכל מין.

**מה חסר:** `GROUP BY species_id` + `MAX(weight_kg)` — **מודול 24**. זו בדיוק השאלה ש‑`GROUP BY` נולד בשבילה.

### ו. ⭐⭐ בטיפול/הסגר ראשונים, ואז כולם לפי שם

</div>

```sql
SELECT   name, status
FROM     animal
ORDER BY status IN ('medical', 'quarantine') DESC,   -- TRUE (1) before FALSE (0)
         name;
```

```text
name     status
-------  ----------
Max      medical       <- the two "urgent" ones first
Nala     quarantine
Bella    adopted       <- then everyone else, A-Z
Bunny    available
Charlie  adopted
...
```

<div dir="rtl">

**המנגנון:** `status IN (…)` הוא ביטוי בוליאני — `1` לשתי החיות, `0` לשאר. `DESC` שם את ה‑1 ראשון. **אותו טריק כמו `IS NULL`** — מפתח ראשון "מלאכותי" שרק מחלק לשתי קבוצות.

> 🎓 **הדפוס הזה שווה זהב:** *"שים את X ראשון, ואז הכול לפי Y"* = `ORDER BY <condition for X> DESC, Y`. עובד לכל תנאי.

---

<div align="center">

### 🎯 סיימתם את מודול 18!

חמש מתוך שמונה השאלות של רותי נענו.
במודול הבא — **פונקציות**: לחתוך טקסט, לעגל מספרים, לחשב גילים.

---

### ➡️ מודול 19 — SQL: פונקציות 🔜

</div>

---

<div align="center">

**🧭 ניווט המודול**

</div>

| 📖 [חזרה למודול](README.md) | ❓ [שאלות ותשובות](questions.md) | ✏️ [לתרגילים](exercises.md) | 🏠 [דף הקורס](../../) |
|---|---|---|---|

</div>
