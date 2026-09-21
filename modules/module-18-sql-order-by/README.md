<div dir="rtl">

# מודול 18 — SQL: מיונים

> **פרק 18 בתכנית הלימודים** · 4 שעות עיוני + 2 שעות מעשי
> **נושאים:** השוואות לוגיות וחוקי קדימויות · מיונים · סימולציית ראיון עבודה · פונקציות

> 🧭 **במסלול המשולב:** יחידה 3, לצד [מודול 3 — ERD](../module-03-erd/), יחד עם מודול 19.

---

## 🎯 מה תדעו בסוף המודול

- [ ] למיין תוצאה עם `ORDER BY` — עולה ויורד
- [ ] למיין לפי **כמה מפתחות** — ולהבין מה קורה כשהראשון שווה
- [ ] למיין לפי **ביטוי מחושב** או **כינוי**
- [ ] לדעת **איפה NULL נופל** במיון — ולמה זה שונה בין SQLite ל‑Oracle
- [ ] לכתוב **"N הראשונים"** נכון — `ORDER BY` + `LIMIT` יחד
- [ ] להבין את **סדר הביצוע הלוגי** של שאילתה — ולמה אפשר למיין לפי כינוי אבל לא לסנן לפיו
- [ ] לענות על שאלת ראיון עבודה ברמת המודול הזה

---

## 🗺️ מפת המודול

| # | הסעיף |
|---|--------|
| 1 | [למה סדר חשוב](#1-למה-סדר-חשוב) |
| 2 | [ORDER BY — הבסיס](#2-order-by--הבסיס) |
| 3 | [מיון לפי כמה מפתחות](#3-מיון-לפי-כמה-מפתחות) |
| 4 | [מיון טקסט — הפתעות](#4-מיון-טקסט--הפתעות) |
| 5 | [מיון לפי ביטוי, כינוי או מספר עמודה](#5-מיון-לפי-ביטוי-כינוי-או-מספר-עמודה) |
| 6 | [NULL במיון — מלכודת הדיאלקט](#6-null-במיון--מלכודת-הדיאלקט) |
| 7 | [ORDER BY + LIMIT — "N הראשונים"](#7-order-by--limit--n-הראשונים) |
| 8 | [סדר הביצוע הלוגי](#8-סדר-הביצוע-הלוגי) |
| 9 | [חזרה: השוואות לוגיות ולוגיקה תלת‑ערכית](#9-חזרה-השוואות-לוגיות-ולוגיקה-תלתערכית) |
| 10 | [סימולציית ראיון עבודה](#10-סימולציית-ראיון-עבודה) |
| 11 | [טעימה מפונקציות](#11-טעימה-מפונקציות) |
| 12 | [דוגמה מלאה — לוח המודעות של המקלט](#12-דוגמה-מלאה--לוח-המודעות-של-המקלט) |
| 13 | [חמש טעויות נפוצות](#13-חמש-טעויות-נפוצות) |
| 14 | [רשימת בדיקה](#14-רשימת-בדיקה) |
| 15 | [סיכום המודול](#15-סיכום-המודול) |

---

## 1. למה סדר חשוב

<div align="center">

**בלי `ORDER BY`, בסיס הנתונים מחזיר שורות בסדר שנוח לו. לא בסדר שנוח לכם.**

</div>

עד עכשיו, כל התוצאות הגיעו "בסדר שבו הוכנסו". זה **מקרה**, לא הבטחה. ברגע שהטבלה גדולה, עוברת עדכונים, או שבסיס הנתונים בוחר דרך אחרת לשלוף — הסדר משתנה.

> 🎬 **סיפור מהשטח: הדוח ששינה את סדרו**
>
> מנהל חנות קיבל כל בוקר דוח "10 המוצרים הנמכרים ביותר". השאילתה: `SELECT ... LIMIT 10`. בלי `ORDER BY`. במשך שנתיים זה עבד — במקרה, כי הטבלה הייתה קטנה והמוצרים נכנסו לפי פופולריות.
>
> ואז עשו שדרוג לבסיס הנתונים. למחרת הדוח הראה 10 מוצרים אקראיים. המנהל הזמין מלאי לפי הדוח, ובמשך שבוע החנות הייתה מלאה במוצרים שאף אחד לא קונה.
>
> 🔑 **`LIMIT` בלי `ORDER BY` הוא "10 שורות כלשהן".** אם התוצאה נראית נכונה — זה מזל, וגם מזל נגמר.

---

## 2. ORDER BY — הבסיס

</div>

```sql
SELECT name, weight_kg
FROM   animal
ORDER  BY weight_kg;           -- ascending: lightest first
```

```text
name     weight_kg
-------  ---------
Kiwi     0.04
Coco     0.1
Bunny    1.5
Thumper  1.8
...
Rocky    31.0
Rex      38.7
```

<div dir="rtl">

| הכיוון | מילת המפתח | ברירת מחדל? |
|---------|-------------|-------------|
| עולה — מהקטן לגדול | `ASC` | ✅ כן — אפשר להשמיט |
| יורד — מהגדול לקטן | `DESC` | ❌ חייבים לכתוב |

</div>

```sql
SELECT name, weight_kg
FROM   animal
ORDER  BY weight_kg DESC;      -- heaviest first: Rex, Rocky, Bella...
```

<div dir="rtl">

**המיקום קבוע:** `ORDER BY` תמיד **אחרי** `WHERE`, ולפני `LIMIT`.

</div>

```sql
SELECT   name, weight_kg
FROM     animal
WHERE    species_id = 1         -- 1. filter
ORDER BY weight_kg DESC         -- 2. sort what's left
LIMIT    3;                     -- 3. keep the first 3
```

<div dir="rtl">

> 💡 **`ORDER BY` לא משנה את הטבלה.** כמו `SELECT`, הוא פועל על **התוצאה** בלבד. הטבלה נשארת כפי שהיא.

---

## 3. מיון לפי כמה מפתחות

מה קורה כשממיינים לפי `species_id` — ולכל מין יש כמה חיות? **סדר השורות בתוך המין לא מוגדר.** כדי לקבוע אותו — מפתח שני:

</div>

```sql
SELECT   name, species_id, weight_kg
FROM     animal
ORDER BY species_id,            -- first by species...
         weight_kg DESC;        -- ...then heaviest first WITHIN each species
```

```text
name     species_id  weight_kg
-------  ----------  ---------
Rex      1           38.7        <- dogs, heaviest first
Rocky    1           31.0
Bella    1           28.4
...
Charlie  1           7.2
Oscar    2           5.5         <- then cats, heaviest first
Felix    2           5.0
...
Thumper  3           1.8         <- rabbits
Bunny    3           1.5
Coco     4           0.1         <- parrots
Kiwi     4           0.04
```

<div dir="rtl">

**הכלל:** המפתח השני נכנס לפעולה **רק כשהראשון שווה**. ולכל מפתח כיוון משלו — `species_id` עולה, `weight_kg` יורד.

</div>

```text
   ORDER BY species_id, weight_kg DESC

   species 1 ---> sort these by weight DESC ---> Rex, Rocky, Bella, ...
   species 2 ---> sort these by weight DESC ---> Oscar, Felix, Tom, ...
   species 3 ---> sort these by weight DESC ---> Thumper, Bunny
   species 4 ---> sort these by weight DESC ---> Coco, Kiwi

   The first key groups. The second key orders within the group.
```

<div dir="rtl">

> ⚠️ **`DESC` חל על מפתח אחד בלבד.** `ORDER BY a, b DESC` = `a` עולה, `b` יורד. אם רוצים את שניהם יורדים: `ORDER BY a DESC, b DESC`.

---

## 4. מיון טקסט — הפתעות

</div>

```sql
SELECT name FROM animal ORDER BY name;
-- -> Bella, Bunny, Charlie, Coco, Daisy, Felix, ... , Tom, Zoe
```

<div dir="rtl">

אלפביתי. נראה פשוט. **שלוש הפתעות:**

### 4.1 אותיות גדולות לפני קטנות

</div>

```text
   ORDER BY name gives:      Banana, apple, cherry
                              ^^^^^^
   NOT:                       apple, Banana, cherry

   Why: the database compares CHARACTER CODES. 'B' is 66, 'a' is 97.
        ALL uppercase letters come before ALL lowercase letters.
```

<div dir="rtl">

**בבסיס הנתונים שלנו** כל השמות מתחילים באות גדולה, אז לא תרגישו. **בנתונים אמיתיים** — `'iPhone'` יופיע אחרי `'Zebra'`. הפתרון: `ORDER BY UPPER(name)` — מודול 19.

### 4.2 מספרים בתוך טקסט

</div>

```text
   A TEXT column holding "1", "2", "10", "20":
   ORDER BY gives:    1, 10, 2, 20     <- character by character: '1' < '2'
   NOT:               1, 2, 10, 20

   If it should sort as numbers -- it should BE a number. (module 7: domains)
```

<div dir="rtl">

### 4.3 עברית

תווים עבריים ממוינים לפי סדר האלף‑בית **בתוך עברית**. אבל **עברית תמיד אחרי לטינית** (קודי התווים גבוהים יותר). ברשימה מעורבת — כל השמות באנגלית קודם, ואז כל השמות בעברית.

> 🔑 **המסקנה:** מיון טקסט הוא לפי **קוד תו**, לא לפי מה שבן אדם היה עושה. כשזה חשוב — מנרמלים (`UPPER`) או שומרים כמספר.

---

## 5. מיון לפי ביטוי, כינוי או מספר עמודה

שלוש דרכים למיין לפי משהו שאינו עמודה גולמית:

</div>

```sql
-- 1. by an EXPRESSION (recalculated in ORDER BY)
SELECT   name, weight_kg
FROM     animal
ORDER BY weight_kg * 2.2 DESC;

-- 2. by an ALIAS (cleaner -- the expression is defined once)
SELECT   name, weight_kg * 2.2 AS weight_lb
FROM     animal
ORDER BY weight_lb DESC;

-- 3. by COLUMN POSITION (works, but fragile)
SELECT   name, weight_kg
FROM     animal
ORDER BY 2 DESC;                -- "the 2nd column" = weight_kg
```

<div dir="rtl">

| הדרך | ✅ | ❌ |
|------|----|----|
| ביטוי | תמיד עובד | חוזרים על החישוב |
| **כינוי** | ⭐ נקי, קריא | — |
| מספר עמודה | קצר | ⚠️ מוסיפים עמודה ל‑`SELECT` ⟵ המספר מצביע למקום אחר. **אל תשתמשו בקוד אמיתי** |

> 💡 **למה אפשר למיין לפי כינוי, אבל (בתקן) לא לסנן לפיו?** ב‑Oracle, `WHERE weight_lb > 40` **נכשל** — `ORA-00904: invalid identifier`. `ORDER BY weight_lb` **עובד**. ההסבר בסעיף 8 — סדר הביצוע.
>
> ⚠️ **מלכודת דיאלקט:** SQLite (Programiz) **סולח** — הוא מרשה כינוי גם ב‑`WHERE`, בניגוד לתקן. שאילתה שעובדת ב‑Programiz תיכשל ב‑APEX. **אל תסתמכו על זה.**

---

## 6. NULL במיון — מלכודת הדיאלקט

איפה NULL נופל כשממיינים? **תלוי בבסיס הנתונים.**

</div>

```sql
SELECT name, birth_date
FROM   animal
ORDER  BY birth_date;
```

```text
   SQLite (Programiz):              Oracle:

   name    birth_date               name    birth_date
   ------  ----------               ------  ----------
   Coco                <- NULLs     Zoe     2016-01-01
   Lily                   FIRST     Rex     2017-08-08
   Kiwi                             ...
   Zoe     2016-01-01               Nala    2024-03-01
   Rex     2017-08-08               Coco                <- NULLs
   ...                              Lily                   LAST
   Nala    2024-03-01               Kiwi

   SQLite treats NULL as SMALLER than everything.
   Oracle treats NULL as LARGER than everything.
   Same query, different order.
```

<div dir="rtl">

| | `ASC` | `DESC` |
|---|---|---|
| **SQLite / MySQL / PostgreSQL** | NULL **ראשון** | NULL **אחרון** |
| **Oracle** | NULL **אחרון** | NULL **ראשון** |

### לשלוט בזה במפורש

</div>

```sql
-- Oracle: explicit keywords
SELECT name, birth_date FROM animal ORDER BY birth_date NULLS LAST;
SELECT name, birth_date FROM animal ORDER BY birth_date DESC NULLS FIRST;

-- SQLite (Programiz): the trick -- sort by "is it null?" first
SELECT name, birth_date
FROM   animal
ORDER  BY birth_date IS NULL,   -- FALSE (0) before TRUE (1): non-nulls first
          birth_date;           -- then by date
-- -> Zoe, Rex, ..., Nala, Coco, Lily, Kiwi   (NULLs last)
```

<div dir="rtl">

> 🔑 **הלקח:** אם עמודה יכולה להיות NULL ואתם ממיינים לפיה — **אמרו במפורש איפה ה‑NULL**. אחרת הדוח ייראה שונה ב‑Programiz ובבחינה על APEX.

> ⚠️ **ולמה זה חשוב עסקית:** "3 החיות הוותיקות ביותר" — `ORDER BY birth_date LIMIT 3`. ב‑SQLite תקבלו **Coco, Lily, Kiwi** — שלוש חיות **בלי** תאריך לידה. לא הוותיקות; הלא‑ידועות. הדוח שגוי לגמרי, בלי שגיאה.

---

## 7. ORDER BY + LIMIT — "N הראשונים"

זה השימוש האמיתי ב‑`LIMIT`. יחד עם `ORDER BY` הוא הופך מ"כמה שורות כלשהן" ל"**ה‑N הראשונים לפי…**":

</div>

```sql
-- the 3 heaviest animals
SELECT   name, weight_kg
FROM     animal
ORDER BY weight_kg DESC
LIMIT    3;
-- -> Rex 38.7, Rocky 31.0, Bella 28.4

-- the 5 most expensive single expenses
SELECT   expense_date, category, amount
FROM     expense
ORDER BY amount DESC
LIMIT    5;

-- the most recent adoption
SELECT   animal_id, adoption_date
FROM     adoption
ORDER BY adoption_date DESC
LIMIT    1;
```

<div dir="rtl">

| הדפוס | השאילתה |
|--------|----------|
| **הגדול ביותר** | `ORDER BY x DESC LIMIT 1` |
| **הקטן ביותר** | `ORDER BY x ASC LIMIT 1` |
| **10 המובילים** | `ORDER BY x DESC LIMIT 10` |
| **האחרון שקרה** | `ORDER BY date DESC LIMIT 1` |

</div>

```sql
-- Oracle equivalent
SELECT   name, weight_kg
FROM     animal
ORDER BY weight_kg DESC
FETCH FIRST 3 ROWS ONLY;
```

<div dir="rtl">

> ⚠️ **שוויון בקצה:** אם החיה השלישית והרביעית שוקלות אותו דבר, `LIMIT 3` יחזיר **אחת מהן** — ואין לדעת איזו. כדי לקבל תוצאה **יציבה**: הוסיפו מפתח שובר שוויון, למשל `ORDER BY weight_kg DESC, animal_id`.

---

## 8. סדר הביצוע הלוגי

זה הסעיף שמסביר את כל ה"למה" שנערמו עד עכשיו. **אתם כותבים** את השאילתה בסדר אחד; **בסיס הנתונים מבצע** אותה בסדר אחר.

</div>

```text
   HOW YOU WRITE IT:                  HOW THE DATABASE RUNS IT:

   1. SELECT   name, w * 2.2 AS lb    3. SELECT   -- compute the columns, apply aliases
   2. FROM     animal                 1. FROM     -- get the table
   3. WHERE    species_id = 1         2. WHERE    -- drop rows that fail
   4. ORDER BY lb DESC                4. ORDER BY -- sort the survivors
   5. LIMIT    3                      5. LIMIT    -- keep the first N

   FROM -> WHERE -> SELECT -> ORDER BY -> LIMIT
```

<div dir="rtl">

**ועכשיו כל ה"למה" מסתדרים:**

| השאלה | התשובה מסדר הביצוע |
|--------|---------------------|
| למה `WHERE weight_lb > 40` נכשל ב‑Oracle? | `WHERE` רץ **לפני** `SELECT` — הכינוי `weight_lb` עוד לא קיים. (SQLite חורג מהתקן ומרשה; אל תסמכו על זה) |
| למה `ORDER BY weight_lb` עובד? | `ORDER BY` רץ **אחרי** `SELECT` — הכינוי כבר קיים |
| למה `LIMIT` לא מאיץ את `WHERE`? | `LIMIT` רץ **אחרון**. כל הסינון והמיון קורים על כל השורות קודם |
| למה `ORDER BY` לא משנה את הטבלה? | הוא רץ על **התוצאה** של השלבים הקודמים, לא על הטבלה |

> 🔑 **זהו המודל המנטלי שיישאר איתכם לכל הקורס.** במודול 24 נוסיף `GROUP BY` ו‑`HAVING` לרצף הזה — ותבינו מיד למה `HAVING` קיים בכלל.

---

## 9. חזרה: השוואות לוגיות ולוגיקה תלת‑ערכית

תכנית הלימודים מחזירה כאן את הנושא ממודול 17, בגלל היבט אחד שכדאי לראות **במלואו**: **SQL אינו דו‑ערכי.** לכל תנאי יש **שלוש** תוצאות אפשריות.

</div>

```text
   THREE-VALUED LOGIC (TRUE / FALSE / NULL)

   AND     | TRUE   FALSE  NULL         OR      | TRUE   FALSE  NULL
   --------+--------------------        --------+--------------------
   TRUE    | TRUE   FALSE  NULL         TRUE    | TRUE   TRUE   TRUE
   FALSE   | FALSE  FALSE  FALSE        FALSE   | TRUE   FALSE  NULL
   NULL    | NULL   FALSE  NULL         NULL    | TRUE   NULL   NULL

   NOT TRUE  = FALSE
   NOT FALSE = TRUE
   NOT NULL  = NULL          <- (!)  not TRUE

   WHERE keeps a row ONLY when the whole condition is TRUE.
   FALSE -> out.  NULL -> out.
```

<div dir="rtl">

**שלוש תובנות מהטבלה:**

| התובנה | הדוגמה |
|---------|---------|
| `FALSE AND NULL` = **FALSE** — לא NULL | אם צד אחד כבר שקר, לא משנה מה השני |
| `TRUE OR NULL` = **TRUE** — לא NULL | אם צד אחד כבר אמת, לא משנה מה השני |
| ⚠️ `NOT NULL` = **NULL** | `NOT (breed = 'Mixed')` על חיה בלי גזע — עדיין נופלת. `NOT` לא "הופך" NULL ל‑TRUE |

**וסדר הקדימויות המלא:**

</div>

```text
   1. ( )           parentheses
   2. NOT
   3. AND
   4. OR

   NOT a OR b AND c   ==   (NOT a) OR (b AND c)
```

<div dir="rtl">

> 💡 **ולכן שוב:** סוגריים. תמיד. הן לא חלק מהתחביר — הן חלק מהתקשורת.

---

## 10. סימולציית ראיון עבודה

תכנית הלימודים מכניסה כאן סימולציה. **הנה חמש שאלות שבאמת נשאלות בראיונות** ברמה של המודולים 16–18, עם התשובה שמצפים לשמוע:

| # | השאלה | מה המראיין מחפש |
|---|--------|------------------|
| 1 | *"מה ההבדל בין `WHERE` ל‑`ORDER BY`?"* | `WHERE` מסנן **אילו** שורות; `ORDER BY` קובע **באיזה סדר**. אחד מצמצם, השני מסדר |
| 2 | *"איך תמצא את 5 הלקוחות עם ההזמנה הגדולה ביותר?"* | `ORDER BY amount DESC LIMIT 5` — **ולציין** את הבעיה של שוויון בקצה |
| 3 | *"למה `WHERE x = NULL` לא עובד?"* | כי ההשוואה מחזירה NULL, לא TRUE; צריך `IS NULL`. ⭐ **בונוס:** להזכיר לוגיקה תלת‑ערכית |
| 4 | *"אפשר לסנן לפי כינוי ב‑`WHERE`?"* | לפי התקן לא — `WHERE` רץ לפני `SELECT`. **ב‑`ORDER BY`** — כן. ⭐ **בונוס:** לציין ש‑SQLite חורג ומרשה |
| 5 | *"מה מחזיר `SELECT … LIMIT 10` בלי `ORDER BY`?"* | 10 שורות **כלשהן**. הסדר לא מובטח. ⭐ **בונוס:** לספר על הדוח שהשתנה אחרי שדרוג |

> 🎯 **מה שמבדיל תשובה טובה מתשובה מצוינת:** הטובה עונה על השאלה. המצוינת מוסיפה **את המלכודת** — "וכדאי לדעת ש…". המראיין שומע שעבדתם עם זה באמת, לא רק קראתם.

**תרגול:** בחרו שאלה, ענו **בקול רם** תוך 30 שניות. אם אתם מגמגמים — זה מה שתעשו בראיון. [תרגיל 9](exercises.md) עוסק בזה.

---

## 11. טעימה מפונקציות

תכנית הלימודים מציגה כאן "פונקציות" — ומודול 19 מוקדש להן כולו. הטעימה: **פונקציה מקבלת ערך ומחזירה ערך אחר.**

</div>

```sql
SELECT   name,
         UPPER(name)  AS shouted,      -- text -> UPPERCASE text
         LENGTH(name) AS letters       -- text -> a number
FROM     animal
ORDER BY LENGTH(name) DESC;            -- longest names first
-- -> Thumper (7), Charlie (7), Shadow (6), ...
```

<div dir="rtl">

וכבר יש לזה שימוש **במיון**: `ORDER BY UPPER(name)` פותר את בעיית האותיות הגדולות מסעיף 4. **ההמשך במודול 19.**

---

## 12. דוגמה מלאה — לוח המודעות של המקלט

רותי מבקשת דף להדפסה ללוח המודעות: **"החיות הזמינות לאימוץ, מסודרות לפי מין, ובתוך כל מין — מהקלה לכבדה. ואם אין תאריך לידה — בסוף."**

</div>

```sql
-- Step 1: which animals?
SELECT name, species_id, weight_kg, birth_date
FROM   animal
WHERE  status = 'available';

-- Step 2: by species, then weight
SELECT   name, species_id, weight_kg, birth_date
FROM     animal
WHERE    status = 'available'
ORDER BY species_id, weight_kg;

-- Step 3: unknown birth dates go last (SQLite)
SELECT   name, species_id, weight_kg, birth_date
FROM     animal
WHERE    status = 'available'
ORDER BY species_id,
         birth_date IS NULL,        -- known dates before unknown
         weight_kg;
```

```text
name    species_id  weight_kg  birth_date
------  ----------  ---------  ----------
Shadow  1           25.1       2021-06-30
Rocky   1           31.0       2019-11-20
Rex     1           38.7       2017-08-08
Mitzi   2           3.1        2023-01-10
Felix   2           5.0        2019-02-14
Oscar   2           5.5        2021-12-12
Lily    2           3.4                      <- cat, unknown birth date: last among cats
Bunny   3           1.5        2024-01-01
Coco    4           0.1                      <- parrot, unknown: last (and only)
```

<div dir="rtl">

> 💡 **שימו לב:** `birth_date IS NULL` כמפתח **שני** — לא ראשון. אם היה ראשון, כל החיות בלי תאריך היו מתקבצות בסוף הרשימה **כולה**, במקום בסוף כל מין. **סדר המפתחות הוא סדר העדיפויות.**

---

## 13. חמש טעויות נפוצות

| # | הטעות | מה קורה | התיקון |
|---|-------|----------|---------|
| 1 | **`LIMIT` בלי `ORDER BY`** | "N שורות כלשהן" — נראה נכון עד שלא | תמיד `ORDER BY` לפני `LIMIT` |
| 2 | **`ORDER BY a, b DESC` כשרוצים שניהם יורדים** | `a` עולה בשקט | `DESC` על **כל** מפתח שצריך |
| 3 | **מיון לפי מספר עמודה בקוד אמיתי** | מוסיפים עמודה ⟵ המיון קופץ למקום אחר | כינוי |
| 4 | **לשכוח איפה NULL נופל** | "3 הוותיקות" מחזיר 3 חיות בלי תאריך | `IS NULL` כמפתח ראשון (SQLite) / `NULLS LAST` (Oracle) |
| 5 | **`WHERE` לפי כינוי** | עובד ב‑SQLite, **נכשל ב‑Oracle** (`ORA-00904`) | `WHERE` על הביטוי המלא; כינוי רק ב‑`ORDER BY` |

---

## 14. רשימת בדיקה

| ✔ | הבדיקה |
|---|--------|
| ☐ | מיינתי עולה ויורד, וראיתי ש‑`ASC` הוא ברירת המחדל |
| ☐ | מיינתי לפי שני מפתחות בכיוונים שונים |
| ☐ | מיינתי לפי כינוי — ויודע ש‑`WHERE` לפי כינוי עובד רק ב‑SQLite ונכשל ב‑Oracle |
| ☐ | הרצתי `ORDER BY birth_date` וראיתי איפה NULL נופל ב‑SQLite |
| ☐ | הרצתי את הטריק `IS NULL, column` והעברתי את ה‑NULL לסוף |
| ☐ | כתבתי "3 הגדולים ביותר" עם `ORDER BY … DESC LIMIT 3` |
| ☐ | אני יכול לומר בעל פה: `FROM → WHERE → SELECT → ORDER BY → LIMIT` |
| ☐ | עניתי בקול על שאלת ראיון אחת מסעיף 10 תוך 30 שניות |
| ☐ | פתרתי את [התרגילים](exercises.md) בהרצה |

---

## 15. סיכום המודול

<div align="center">

### 🧠 שבע נקודות

</div>

1. **בלי `ORDER BY` אין סדר.** מה שנראה מסודר הוא מקרה, ומקרים משתנים אחרי שדרוג.
2. **`ASC` ברירת מחדל, `DESC` חייבים לכתוב** — ועל כל מפתח בנפרד.
3. **המפתח השני פועל רק כשהראשון שווה.** סדר המפתחות = סדר העדיפויות.
4. **טקסט ממוין לפי קוד תו:** גדולות לפני קטנות, `'10'` לפני `'2'`, לטינית לפני עברית.
5. **⚠️ NULL: ראשון ב‑SQLite, אחרון ב‑Oracle.** אמרו במפורש — `IS NULL` כמפתח או `NULLS LAST`.
6. **`ORDER BY` + `LIMIT` = "N הראשונים".** לבד, `LIMIT` הוא רק לבדיקה.
7. **סדר הביצוע: `FROM → WHERE → SELECT → ORDER BY → LIMIT`.** לכן כינוי עובד ב‑`ORDER BY` — ולפי התקן לא ב‑`WHERE` (SQLite סולח; Oracle לא).

<div align="center">

---

*"בסיס הנתונים לא חייב לכם סדר.*
*הוא חייב לכם רק את מה שביקשתם — ואם לא ביקשתם, לא תקבלו."*

---

</div>

## 📎 המשך

| | |
|---|---|
| ❓ | [שאלות ותשובות](questions.md) |
| ✏️ | [תרגילים](exercises.md) — על [בסיס הנתונים המוכן](../../resources/shelter-db/) |
| ✅ | [פתרונות](solutions.md) — עם הפלט האמיתי |
| ⬅️ | [מודול 17 — SQL: הגבלת השליפה](../module-17-sql-where/) |
| 🧭 | [מסלול הלימוד](../../LEARNING-PATH.md) — יחידה 3 |
| ➡️ | [מודול 19 — SQL: פונקציות](../module-19-sql-functions/) |
| 🏠 | [חזרה לדף הקורס](../../) |

</div>
