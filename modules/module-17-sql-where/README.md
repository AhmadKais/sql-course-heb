<div dir="rtl">

# מודול 17 — SQL: הגבלת השליפה

> **פרק 17 בתכנית הלימודים** · 4 שעות עיוני + 2 שעות מעשי
> **נושאים:** עבודה עם עמודות, תווים ושורות · הגבלת מספר הרשומות החוזרות · אופרטורים להשוואה

> 🧭 **במסלול המשולב:** יחידה 2, לצד [מודול 2](../module-02-data-model/) ואחרי [מודול 16](../module-16-sql-basics/).

---

## 🎯 מה תדעו בסוף המודול

- [ ] לבחור **אילו שורות** חוזרות — עם `WHERE`
- [ ] להשוות מספרים, טקסט ותאריכים — `=`, `<>`, `<`, `>`, `<=`, `>=`
- [ ] לחפש **טווח** (`BETWEEN`) ו**רשימה** (`IN`)
- [ ] לחפש **תבנית** בטקסט — `LIKE` עם `%` ו‑`_`
- [ ] למצוא שורות **עם NULL ובלי NULL** — ולהבין למה `= NULL` לא עובד
- [ ] לשלב תנאים עם `AND`, `OR`, `NOT` — ולדעת **מי גובר על מי**
- [ ] להגביל את **מספר** השורות — `LIMIT`

---

## 🗺️ מפת המודול

| # | הסעיף |
|---|--------|
| 1 | [WHERE — הפילטר](#1-where--הפילטר) |
| 2 | [אופרטורי השוואה](#2-אופרטורי-השוואה) |
| 3 | [השוואת טקסט — אותיות גדולות וקטנות](#3-השוואת-טקסט--אותיות-גדולות-וקטנות) |
| 4 | [השוואת תאריכים](#4-השוואת-תאריכים) |
| 5 | [BETWEEN ו‑IN — קיצורי דרך](#5-between-וin--קיצורי-דרך) |
| 6 | [LIKE — חיפוש תבנית](#6-like--חיפוש-תבנית) |
| 7 | [NULL — למה = לא עובד](#7-null--למה--לא-עובד) |
| 8 | [AND, OR, NOT — ומי גובר על מי](#8-and-or-not--ומי-גובר-על-מי) |
| 9 | [LIMIT — רק כמה שורות](#9-limit--רק-כמה-שורות) |
| 10 | [דוגמה מלאה — ארבע שאלות של רותי](#10-דוגמה-מלאה--ארבע-שאלות-של-רותי) |
| 11 | [חמש טעויות נפוצות](#11-חמש-טעויות-נפוצות) |
| 12 | [רשימת בדיקה](#12-רשימת-בדיקה) |
| 13 | [סיכום המודול](#13-סיכום-המודול) |

---

## 1. WHERE — הפילטר

במודול 16 שלפנו **את כל השורות**. עכשיו נבחר.

</div>

```sql
SELECT name, breed
FROM   animal
WHERE  species_id = 1;      -- only rows where this is TRUE
```

```text
name     breed
-------  ---------------
Luna     Mixed
Rocky    Labrador
Bella    German Shepherd
Max      Beagle
Zoe      Mixed
Rex      Rottweiler
Charlie  Poodle
Daisy    Mixed
Shadow   Husky
```

<div dir="rtl">

**9 שורות** במקום 20. רק הכלבים.

### איך זה עובד

</div>

```text
   FOR EACH ROW in the table:
       evaluate the condition   species_id = 1
       TRUE  -> the row is IN the result
       FALSE -> the row is OUT
       NULL  -> the row is OUT   (!)  -- see section 7

   +----+-------+------------+          +-------+
   | 1  | Luna  | species 1  |  TRUE -> | Luna  |
   | 2  | Simba | species 2  |  FALSE   |       |
   | 3  | Rocky | species 1  |  TRUE -> | Rocky |
   | 4  | Mitzi | species 2  |  FALSE   |       |
   +----+-------+------------+          +-------+
```

<div dir="rtl">

`WHERE` **תמיד** אחרי `FROM`. תמיד לפני `ORDER BY` (מודול 18). זה הסדר הקבוע ממודול 16.

> 🎬 **סיפור מהשטח: הדוח שהיה כל הלקוחות**
>
> פקידה ביקשה ממתכנת "רשימת לקוחות שלא שילמו". הוא כתב שאילתה, שלח, והיא הדפיסה — 4,000 שורות.
>
> כל הלקוחות. הוא שכח את ה‑`WHERE`.
>
> היא לא שמה לב, כי מי סופר 4,000 שורות. שלחו מכתבי התראה ל‑4,000 לקוחות. 3,800 מהם שילמו בזמן. הטלפונים לא הפסיקו לצלצל שבוע.
>
> 🔑 **`WHERE` הוא ההבדל בין "מה יש" ל"מה אני צריך".** וברוב השאילתות בעולם — הוא החלק החשוב ביותר.

---

## 2. אופרטורי השוואה

| האופרטור | משמעות | דוגמה |
|-----------|---------|--------|
| `=` | שווה | `status = 'adopted'` |
| `<>` | שונה (גם `!=`) | `role <> 'adopter'` |
| `<` | קטן מ | `weight_kg < 5` |
| `>` | גדול מ | `weight_kg > 20` |
| `<=` | קטן או שווה | `fee_paid <= 200` |
| `>=` | גדול או שווה | `expense_date >= '2025-01-01'` |

</div>

```sql
-- heavy animals
SELECT name, weight_kg
FROM   animal
WHERE  weight_kg > 20;
```

```text
name    weight_kg
------  ---------
Rocky   31.0
Bella   28.4
Zoe     22.0
Rex     38.7
Shadow  25.1
```

```sql
-- everyone who is NOT an adopter
SELECT first_name, role
FROM   person
WHERE  role <> 'adopter';
```

<div dir="rtl">

> 💡 **`<>` ולא `!=`:** שניהם עובדים כמעט בכל בסיס נתונים. `<>` הוא התקן. בקורס נשתמש בו.

---

## 3. השוואת טקסט — אותיות גדולות וקטנות

</div>

```sql
SELECT name FROM animal WHERE name = 'Luna';    -- 1 row
SELECT name FROM animal WHERE name = 'luna';    -- 0 rows  (!)
```

<div dir="rtl">

<div align="center">

**השוואת טקסט רגישה לאותיות גדולות/קטנות.** `'Luna'` ≠ `'luna'`.

</div>

זה נכון ב‑SQLite (Programiz) וגם ב‑Oracle. **המילים המפתח** של SQL (`SELECT`, `where`) לא רגישות — אבל **הערכים** כן.

| מה | רגיש? | דוגמה |
|-----|-------|--------|
| מילות מפתח | ❌ | `SELECT` = `select` |
| שמות עמודות וטבלאות | ❌ | `animal` = `Animal` |
| **ערכים בגרשיים** | ✅ | `'Luna'` ≠ `'luna'` |

**הפתרון** כשלא יודעים איך הוקלד — פונקציה שמאחדת (`UPPER`/`LOWER`), במודול 19. בינתיים: הקלידו בדיוק.

> ⚠️ **ומה עם רווח בסוף?** `'Luna '` (עם רווח) ≠ `'Luna'`. אם השאילתה שלכם מחזירה 0 שורות ואתם בטוחים שהערך קיים — בדקו רווחים. זו הבעיה מספר 1 בנתונים שהוזנו ידנית.

---

## 4. השוואת תאריכים

בבסיס הנתונים שלנו תאריכים שמורים כטקסט בפורמט `YYYY-MM-DD`. **הפורמט הזה נבחר בכוונה:** הוא ממוין נכון גם כטקסט.

</div>

```sql
-- animals born before 2020
SELECT name, birth_date
FROM   animal
WHERE  birth_date < '2020-01-01';
```

```text
name   birth_date
-----  ----------
Rocky  2019-11-20
Bella  2018-05-05
Zoe    2016-01-01
Rex    2017-08-08
Felix  2019-02-14
```

```sql
-- expenses this year
SELECT expense_date, amount
FROM   expense
WHERE  expense_date >= '2025-01-01';
```

<div dir="rtl">

| הפורמט | האם `<` עובד נכון? |
|---------|--------------------|
| `2019-11-20` (שנה‑חודש‑יום) | ✅ תמיד |
| `20/11/2019` (יום/חודש/שנה) | ❌ `'20/11/2019' < '05/01/2020'` הוא **שקר** — כי `'2' > '0'` |

> 🔑 **`YYYY-MM-DD` הוא הפורמט היחיד שבו טקסט ותאריך מסתדרים באותו סדר.** זה תקן ISO 8601, ובכל בסיס נתונים אמיתי (Oracle, PostgreSQL) יש טיפוס `DATE` שמטפל בזה. ב‑SQLite שומרים כטקסט ISO — וזה עובד.

**שימו לב:** לחיות בלי תאריך לידה (NULL) — השורה **לא** חוזרת. לא ב‑`<`, לא ב‑`>`. ראו סעיף 7.

---

## 5. BETWEEN ו‑IN — קיצורי דרך

### 5.1 BETWEEN — טווח

</div>

```sql
-- these two are identical:
SELECT name, weight_kg FROM animal WHERE weight_kg >= 4 AND weight_kg <= 6;
SELECT name, weight_kg FROM animal WHERE weight_kg BETWEEN 4 AND 6;
```

```text
name   weight_kg
-----  ---------
Simba  4.2
Tom    4.8
Oscar  5.5
Felix  5.0
```

<div dir="rtl">

⚠️ **`BETWEEN` כולל את שני הקצוות.** `BETWEEN 4 AND 6` = מ‑4 **כולל** עד 6 **כולל**.

עובד גם על תאריכים וטקסט:

</div>

```sql
SELECT expense_date, amount
FROM   expense
WHERE  expense_date BETWEEN '2024-01-01' AND '2024-03-31';   -- Q1 2024
```

<div dir="rtl">

### 5.2 IN — רשימה

</div>

```sql
-- these two are identical:
SELECT name, status FROM animal WHERE status = 'medical' OR status = 'quarantine';
SELECT name, status FROM animal WHERE status IN ('medical', 'quarantine');
```

```text
name  status
----  ----------
Max   medical
Nala  quarantine
```

<div dir="rtl">

`IN` קורא יותר טוב, ומתרחב יותר טוב — רשימה של 10 ערכים היא עדיין שורה אחת.

</div>

```sql
-- NOT IN: everything except
SELECT name, status
FROM   animal
WHERE  status NOT IN ('adopted', 'deceased');
```

<div dir="rtl">

> ⚠️ **`NOT IN` עם NULL הוא מלכודת** — אם אחד הערכים ברשימה הוא NULL, **אף שורה** לא חוזרת. במודול 24 (תת‑שאילתות) זה יכה. בינתיים: ברשימה מפורשת, אין NULL.

---

## 6. LIKE — חיפוש תבנית

`=` דורש התאמה מדויקת. `LIKE` מחפש **תבנית** עם שני תווים מיוחדים:

| התו | משמעות |
|------|---------|
| `%` | **כל מספר** של תווים (כולל אפס) |
| `_` | **בדיוק תו אחד** |

</div>

```sql
-- names starting with L
SELECT name FROM animal WHERE name LIKE 'L%';
-- -> Luna, Lily

-- names ending with a
SELECT name FROM animal WHERE name LIKE '%a';
-- -> Luna, Simba, Bella, Nala

-- names containing "o" anywhere
SELECT name FROM animal WHERE name LIKE '%o%';
-- -> Rocky, Tom, Coco, Zoe, Oscar, Shadow

-- exactly three letters
SELECT name FROM animal WHERE name LIKE '___';
-- -> Tom, Max, Zoe, Rex
```

<div dir="rtl">

| התבנית | מתאים ל | לא מתאים ל |
|---------|----------|-------------|
| `'L%'` | Luna, Lily, L | luna (אות קטנה!) |
| `'%a'` | Luna, Nala | Lucas |
| `'%an%'` | — אף אחת! (Luna היא L‑u‑n‑a, לא a‑n) | Nala, Luna |
| `'_o%'` | Tom, Coco, Rocky, Zoe | Oscar (o ראשונה, לא שנייה) |
| `'%'` | הכול | — |

> ⚠️ **`LIKE` בלי `%` ובלי `_` הוא בדיוק `=`.** `LIKE 'Luna'` ≡ `= 'Luna'`. אם שכחתם את ה‑`%`, תקבלו התאמה מדויקת בלבד.

> 💡 **הבדל דיאלקט:** ב‑Oracle, `LIKE` רגיש לאותיות כמו `=`. ב‑SQLite (Programiz) — `LIKE 'l%'` **כן** ימצא את Luna, כי `LIKE` שם לא רגיש לאותיות לטיניות. אל תסתמכו על זה: לחיפוש שעובד בכל מקום — `UPPER(name) LIKE 'L%'`, מודול 19.

---

## 7. NULL — למה `=` לא עובד

זו הנקודה הכי חשובה במודול. במודול 16 ראינו ש‑NULL **מדביק** בחישובים. ב‑`WHERE` הוא עושה משהו מפתיע יותר:

</div>

```sql
-- animals WITHOUT a chip -- the WRONG way
SELECT name FROM animal WHERE chip_number = NULL;
-- -> 0 rows.  ZERO.  Even though 7 animals have no chip.
```

<div dir="rtl">

**למה?** כי `chip_number = NULL` לא מחזיר TRUE ולא FALSE. הוא מחזיר **NULL** — "לא ידוע". ו‑`WHERE` מכניס רק שורות שהתנאי שלהן **TRUE**.

<div align="center">

**"האם לא‑ידוע שווה ללא‑ידוע?" — לא ידוע. ולכן: אף שורה.**

</div>

### הדרך הנכונה

</div>

```sql
-- WITHOUT a chip
SELECT name FROM animal WHERE chip_number IS NULL;
```

```text
name
-------
Mitzi
Coco
Nala
Thumper
Lily
Kiwi
Bunny
```

```sql
-- WITH a chip
SELECT name FROM animal WHERE chip_number IS NOT NULL;
-- -> 13 rows
```

<div dir="rtl">

| מה רוצים | ❌ שגוי | ✅ נכון |
|-----------|---------|---------|
| שורות **בלי** ערך | `= NULL` | `IS NULL` |
| שורות **עם** ערך | `<> NULL` | `IS NOT NULL` |

### ההשלכה הנסתרת

</div>

```sql
SELECT name FROM animal WHERE weight_kg > 5;       -- 10 rows
SELECT name FROM animal WHERE weight_kg <= 5;      -- 10 rows
                                                   -- ------
                                                   -- 20 total  [OK]

SELECT name FROM animal WHERE birth_date < '2020-01-01';   --  5 rows
SELECT name FROM animal WHERE birth_date >= '2020-01-01';  -- 12 rows
                                                           -- ------
                                                           -- 17 ??  -- 3 animals vanished!
```

<div dir="rtl">

**שלוש החיות בלי תאריך לידה — Coco, Lily, Kiwi — לא נמצאות באף אחת מהקבוצות.** לא "לפני 2020" ולא "מ‑2020". הן פשוט **לא נספרות**.

> 🔑 **הכלל:** כל השוואה עם NULL — `=`, `<`, `>`, `LIKE`, `BETWEEN`, `IN` — מחזירה NULL, והשורה נופלת. **אם הנתונים שלכם כוללים NULL, כל `WHERE` שלכם מדלג עליהם בשקט.** לפעמים זה מה שרוצים. לפעמים לא. תמיד — צריך לדעת.

---

## 8. AND, OR, NOT — ומי גובר על מי

### 8.1 שילוב תנאים

</div>

```sql
-- BOTH must be true
SELECT name, weight_kg
FROM   animal
WHERE  species_id = 1 AND weight_kg > 25;
-- -> Rocky, Bella, Rex, Shadow  (heavy dogs)

-- EITHER must be true
SELECT name, status
FROM   animal
WHERE  status = 'medical' OR status = 'quarantine';
-- -> Max, Nala

-- the opposite
SELECT name, status
FROM   animal
WHERE  NOT status = 'adopted';
-- -> 12 rows (everyone except the 8 adopted)
```

<div dir="rtl">

| | TRUE | FALSE |
|---|---|---|
| `A AND B` | רק אם **שניהם** TRUE | אם **אחד** FALSE |
| `A OR B` | אם **אחד** TRUE | רק אם **שניהם** FALSE |
| `NOT A` | אם A FALSE | אם A TRUE |

### 8.2 ⚠️ סדר הקדימויות — המלכודת

**`AND` גובר על `OR`.** בדיוק כמו שכפל גובר על חיבור.

רותי מבקשת: *"כלבים וחתולים שזמינים לאימוץ."*

</div>

```sql
-- what you might write:
SELECT name, species_id, status
FROM   animal
WHERE  species_id = 1 OR species_id = 2 AND status = 'available';
-- -> 13 rows.  Including Luna (adopted), Bella (adopted), Daisy (deceased)...
```

<div dir="rtl">

**13 שורות — כולל חיות מאומצות ומתה.** למה?

</div>

```text
   What you MEANT:              What the database READ:

   (species = 1 OR species = 2)   species = 1  OR  (species = 2 AND status = 'available')
   AND status = 'available'
                                  = "ALL dogs, plus available cats"
   = "available dogs and cats"
```

<div dir="rtl">

`AND` נקשר קודם. `species_id = 2 AND status = 'available'` הפך לקבוצה, ואז `OR species_id = 1` הוסיף **את כל הכלבים** — מאומצים ומתים כאחד.

### התיקון: סוגריים

</div>

```sql
SELECT name, species_id, status
FROM   animal
WHERE  (species_id = 1 OR species_id = 2) AND status = 'available';
-- -> 7 rows. Only available dogs and cats.  [OK]
```

<div dir="rtl">

<div align="center">

**כשמערבבים `AND` ו‑`OR` — תמיד סוגריים. גם כשאתם בטוחים.**

</div>

**ועוד יותר טוב:** `IN` מבטל את הבעיה לגמרי:

</div>

```sql
WHERE species_id IN (1, 2) AND status = 'available';
```

<div dir="rtl">

> 🎬 **סיפור מהשטח: ההנחה שניתנה לכולם**
>
> חנות מקוונת נתנה 20% הנחה **ללקוחות מועדון שקנו מעל 500 ₪**. הקוד:
> `WHERE is_member = 1 OR total > 500 AND ...`
>
> ה‑`AND` נקשר לתנאי הבא, וה‑`OR is_member = 1` נשאר לבד. **כל חבר מועדון** קיבל 20% — על כל הזמנה, בכל סכום. שלושה שבועות עד שמישהו שם לב לירידה ברווח.
>
> 🔑 סוגריים חינם. שלושה שבועות של הנחות — לא.

---

## 9. LIMIT — רק כמה שורות

לפעמים רוצים לראות רק את **ההתחלה** — כדי לבדוק שהשאילתה נכונה, בלי לשלוף מיליון שורות.

</div>

```sql
SELECT name FROM animal LIMIT 3;
-- -> Luna, Simba, Rocky
```

<div dir="rtl">

| הכלי | הדיאלקט |
|------|----------|
| `LIMIT 3` | SQLite (Programiz), MySQL, PostgreSQL |
| `FETCH FIRST 3 ROWS ONLY` | Oracle 12c+ (וגם התקן) |
| `WHERE ROWNUM <= 3` | Oracle ישן |

> ⚠️ **`LIMIT` בלי `ORDER BY` מחזיר "3 שורות כלשהן".** לא "3 הראשונות" במובן משמעותי — בסיס הנתונים בוחר. אם צריך "3 הכבדות ביותר" — צריך `ORDER BY`, וזה מודול 18. `LIMIT` לבדו הוא **לבדיקה**, לא לדוח.

---

## 10. דוגמה מלאה — ארבע שאלות של רותי

במודול 16, מתוך 8 שאלות של רותי יכולתם לענות על אחת. עכשיו — על ארבע:

</div>

```sql
-- Q2: "Show me only the dogs"
SELECT name, breed, weight_kg
FROM   animal
WHERE  species_id = 1;

-- Q6: "Which animals have no chip?"
SELECT name, status
FROM   animal
WHERE  chip_number IS NULL;

-- Q8: "Full names of all the volunteers"
SELECT first_name || ' ' || last_name AS full_name, city
FROM   person
WHERE  role = 'volunteer';

-- and a new one she asked this morning:
-- "Dogs and cats that are available, over 4 kg, with a chip"
SELECT name, species_id, weight_kg, chip_number
FROM   animal
WHERE  species_id IN (1, 2)
  AND  status = 'available'
  AND  weight_kg > 4
  AND  chip_number IS NOT NULL;
```

```text
-- last query:
name    species_id  weight_kg  chip_number
------  ----------  ---------  -----------
Rocky   1           31.0       985100003
Oscar   2           5.5        985100012
Rex     1           38.7       985100013
Felix   2           5.0        985100018
Shadow  1           25.1       985100020
```

<div dir="rtl">

> 💡 שימו לב לכתיבה: **תנאי אחד בכל שורה**, `AND` בתחילת השורה. כשיש 4 תנאים — זו הדרך היחידה לקרוא אותם בעוד חודש.

---

## 11. חמש טעויות נפוצות

| # | הטעות | מה קורה | התיקון |
|---|-------|----------|---------|
| 1 | **`= NULL`** | 0 שורות, תמיד, בלי שגיאה | `IS NULL` / `IS NOT NULL` |
| 2 | **`AND`/`OR` בלי סוגריים** | תוצאה שגויה בשקט — יותר שורות ממה שרצו | סוגריים תמיד. או `IN` |
| 3 | **אות גדולה/קטנה בערך** | `'luna'` ⟵ 0 שורות | הקלידו בדיוק; `UPPER()` במודול 19 |
| 4 | **`LIKE 'Luna'` בלי `%`** | זה `=` — התאמה מדויקת | `LIKE 'L%'` — תמיד תו‑תבנית |
| 5 | **תאריך בפורמט `DD/MM/YYYY`** | `<` משווה כטקסט ⟵ שגוי | `'YYYY-MM-DD'` תמיד |

---

## 12. רשימת בדיקה

| ✔ | הבדיקה |
|---|--------|
| ☐ | כתבתי `WHERE` עם כל אחד משישת אופרטורי ההשוואה |
| ☐ | הרצתי `= 'luna'` באות קטנה וראיתי 0 שורות |
| ☐ | השתמשתי ב‑`BETWEEN` וב‑`IN`, וכתבתי את המקבילה הארוכה שלהם |
| ☐ | הרצתי `LIKE` עם `%` ועם `_`, וראיתי את ההבדל |
| ☐ | הרצתי `= NULL` וקיבלתי 0 שורות — **ואז** `IS NULL` וקיבלתי 7 |
| ☐ | הרצתי `OR … AND` בלי סוגריים ועם סוגריים, וספרתי את ההבדל |
| ☐ | ספרתי: `> 5` + `<= 5` = 20, אבל `< date` + `>= date` = 17. **הבנתי לאן נעלמו 3** |
| ☐ | פתרתי את [התרגילים](exercises.md) בהרצה |

---

## 13. סיכום המודול

<div align="center">

### 🧠 שבע נקודות

</div>

1. **`WHERE` מסנן שורות.** התנאי נבדק לכל שורה; רק TRUE נכנס.
2. **שישה אופרטורים:** `= <> < > <= >=`. על מספרים, טקסט ותאריכים.
3. **טקסט רגיש לאותיות. תאריכים — רק ב‑`YYYY-MM-DD`.**
4. **`BETWEEN` = טווח כולל. `IN` = רשימה. `LIKE` = תבנית** עם `%` (כל מספר תווים) ו‑`_` (תו אחד).
5. **⚠️ `= NULL` לעולם לא TRUE.** רק `IS NULL`. וכל השוואה עם NULL מפילה את השורה **בשקט**.
6. **`AND` גובר על `OR`.** כשמערבבים — סוגריים. תמיד.
7. **`LIMIT` לבדיקה, לא לדוח.** בלי `ORDER BY` הוא מחזיר "כמה שורות", לא "הראשונות".

<div align="center">

---

*"ההבדל בין דוח נכון לדוח שגוי הוא לעתים קרובות סוגריים אחד —*
*ואף אחד לא יגיד לכם שהוא חסר."*

---

</div>

## 📎 המשך

| | |
|---|---|
| ❓ | [שאלות ותשובות](questions.md) |
| ✏️ | [תרגילים](exercises.md) — על [בסיס הנתונים המוכן](../../resources/shelter-db/) |
| ✅ | [פתרונות](solutions.md) — עם הפלט האמיתי |
| ⬅️ | [מודול 16 — SQL: המשפט הראשון](../module-16-sql-basics/) |
| 🧭 | [מסלול הלימוד](../../LEARNING-PATH.md) — יחידה 2 הושלמה; הבאה: מודול 3 + 18 |
| ➡️ | מודול 18 — SQL: מיונים (`ORDER BY`) 🔜 |
| 🏠 | [חזרה לדף הקורס](../../) |

</div>
