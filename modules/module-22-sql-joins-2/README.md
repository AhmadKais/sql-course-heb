<div dir="rtl">

# מודול 22 — SQL: איחוד טבלאות 2

> **פרק 22 בתכנית הלימודים** · 3 שעות עיוני + 2 שעות מעשי
> **נושאים:** Cross Joins and Natural Joins · Join Clauses · Inner Versus Outer Joins

> 🧭 **במסלול המשולב:** יחידה 5, מיד אחרי [מודול 21](../module-21-sql-joins/), לצד [מודול 5 — יחסים](../module-05-relationships/).

---

## 🎯 מה תדעו בסוף המודול

- [ ] לכתוב `CROSS JOIN` — ולדעת מתי תוצר קרטזי הוא **בכוונה**
- [ ] להסביר מה עושה `NATURAL JOIN` — ולמה כמעט אף פעם לא משתמשים בו
- [ ] לבחור בין `ON` ל‑`USING`
- [ ] להבדיל בין `INNER`, `LEFT`, `RIGHT` ו‑`FULL OUTER` — ולצפות כמה שורות יחזרו
- [ ] לזהות את המלכודת של **שרשרת `JOIN`‑ים** שבה `LEFT` אחד "נשבר"
- [ ] לבחור את סוג ה‑JOIN הנכון לפי **השאלה**, לא לפי הרגל

---

## 🗺️ מפת המודול

| # | הסעיף |
|---|--------|
| 1 | [מפת כל סוגי ה‑JOIN](#1-מפת-כל-סוגי-הjoin) |
| 2 | [`CROSS JOIN` — כל הצירופים, בכוונה](#2-cross-join--כל-הצירופים-בכוונה) |
| 3 | [`NATURAL JOIN` — הקסם המסוכן](#3-natural-join--הקסם-המסוכן) |
| 4 | [`ON` מול `USING`](#4-on-מול-using) |
| 5 | [Inner מול Outer — ספירת שורות](#5-inner-מול-outer--ספירת-שורות) |
| 6 | [`RIGHT JOIN` ו‑`FULL OUTER JOIN`](#6-right-join-ו‑full-outer-join) |
| 7 | [שרשרת JOIN‑ים — איפה LEFT נשבר](#7-שרשרת-joinים--איפה-left-נשבר) |
| 8 | [איך בוחרים JOIN — שלוש שאלות](#8-איך-בוחרים-join--שלוש-שאלות) |
| 9 | [חמש טעויות נפוצות](#9-חמש-טעויות-נפוצות) |
| 10 | [סיכום המודול](#10-סיכום-המודול) |

---

## 1. מפת כל סוגי ה‑JOIN

</div>

```text
   A = animal (20 rows)     B = expense (22 rows)     joined on  B.animal_id = A.animal_id

      only A           both           only B
   (no expense)   (matched pairs)   (general expense,
                                     animal_id NULL)
   +---------+    +-----------+     +---------+
   |   10    |    |    11     |     |   11    |
   +---------+    +-----------+     +---------+

   INNER JOIN  ............................  both                      = 11 rows
   LEFT JOIN   ............................  only A + both             = 21 rows
   RIGHT JOIN  ............................  both + only B             = 22 rows
   FULL JOIN   ............................  only A + both + only B    = 32 rows
   CROSS JOIN  ............................  every A with every B      = 440 rows
```

<div dir="rtl">

> 🔑 **שאלו קודם: "מה אני רוצה לראות?"** רק זוגות? כל החיות? כל ההוצאות? הכול? התשובה בוחרת את סוג ה‑JOIN — והמספרים למעלה הם בדיקת השפיות שלכם.

> 💡 **"both" = 11 שורות, אבל רק 10 חיות:** ל‑Max יש 2 הוצאות, ולעוד 9 חיות — הוצאה אחת. JOIN סופר **זוגות**, לא חיות.

---

## 2. `CROSS JOIN` — כל הצירופים, בכוונה

במודול 21 ראינו שתוצר קרטזי הוא בדרך כלל באג. `CROSS JOIN` הוא אותו דבר — אבל **כתוב במפורש**, כדי שכל מי שקורא יידע שזה בכוונה.

</div>

```sql
SELECT COUNT(*) FROM animal CROSS JOIN vaccine_type;     -- 20 x 5 = 100
```

<div dir="rtl">

### 2.1 מתי זה שימושי: "מה **צריך** להיות" מול "מה **יש**"

רותי שואלת: *"אילו חיסונים **חסרים** לחיות הזמינות?"* — כדי לענות צריך קודם את רשימת **כל** החיסונים שכל חיה **אמורה** לקבל:

</div>

```sql
-- step 1: every available animal x every vaccine meant for its species
SELECT a.name, vt.name AS vaccine
FROM   animal a
CROSS  JOIN vaccine_type vt
WHERE  vt.species_id = a.species_id
  AND  a.status = 'available'
ORDER  BY a.name, vt.name;
```

```text
name    vaccine
------  -----------
Bunny   Myxomatosis
Felix   FVRCP
Felix   Rabies
Lily    FVRCP
Lily    Rabies
...
Shadow  DHPP
Shadow  Rabies
```

<div dir="rtl">

> 💡 **רגע — יש `WHERE vt.species_id = a.species_id`, אז זה בעצם `JOIN … ON`.** נכון! `CROSS JOIN` + תנאי ב‑`WHERE` = `JOIN` רגיל. כתבנו כך כדי לראות את הרעיון: **קודם כל הצירופים, אחר כך סינון**. בקוד אמיתי כותבים `JOIN vaccine_type vt ON vt.species_id = a.species_id`.

עכשיו, מה **שאין** לו התאמה ב‑`vaccination` — חסר:

</div>

```sql
-- step 2: what SHOULD be  LEFT JOIN  what IS  -> the gaps
SELECT a.name, vt.name AS missing_vaccine
FROM   animal a
JOIN   vaccine_type vt ON vt.species_id = a.species_id
LEFT   JOIN vaccination v ON  v.animal_id       = a.animal_id
                          AND v.vaccine_type_id = vt.vaccine_type_id
WHERE  v.vaccination_id IS NULL
  AND  a.status = 'available'
ORDER  BY a.name;
```

```text
name   missing_vaccine
-----  ---------------
Felix  FVRCP
Lily   FVRCP
Lily   Rabies
Mitzi  FVRCP
```

<div dir="rtl">

> 🔑 **הדפוס: "הרשימה המלאה" `LEFT JOIN` "מה שקרה" ⟵ `IS NULL` = מה חסר.** כך בונים דוח נוכחות (כל התלמידים × כל השיעורים), בדיקת מלאי (כל המוצרים × כל הסניפים) ותזכורות.

> 🎬 **ומה עם Coco?** תוכי — ואין בכלל `vaccine_type` לתוכים. אז היא לא ברשימה המלאה, ולכן גם לא בחסרים. **השאילתה יכולה לגלות רק חורים בנתונים שקיימים.** אם המקלט שכח להגדיר חיסונים לתוכים — שום JOIN לא יגלה את זה.

---

## 3. `NATURAL JOIN` — הקסם המסוכן

`NATURAL JOIN` מחבר **אוטומטית** לפי **כל** העמודות ששמן זהה בשתי הטבלאות. בלי `ON`, בלי לכתוב כלום:

</div>

```sql
SELECT COUNT(*) FROM vaccination NATURAL JOIN animal;    -- 28  works!
SELECT COUNT(*) FROM animal NATURAL JOIN species;        -- 0   ???
```

<div dir="rtl">

**למה 0?** בין `animal` ל‑`species` יש **שתי** עמודות עם אותו שם: `species_id` — וגם **`name`**. אז `NATURAL JOIN` מחבר לפי שתיהן:

</div>

```text
   animal NATURAL JOIN species   means
   ON  animal.species_id = species.species_id
   AND animal.name       = species.name          <- 'Luna' = 'Dog' ? never.
```

<div dir="rtl">

והחיבור עם `vaccination` "עבד" רק **במקרה** — כי במקרה העמודה המשותפת היחידה היא `animal_id`. מחר מישהו יוסיף לשתי הטבלאות עמודה `notes` או `created_at` — וכל השאילתות עם `NATURAL JOIN` יחזירו 0 שורות, **בלי שגיאה**.

> ⚠️ **אל תשתמשו ב‑`NATURAL JOIN` בקוד אמיתי.** תנאי החיבור צריך להיות **כתוב**, כך שמי שקורא יידע בדיוק מה מחובר למה, ושינוי בטבלה לא ישנה את המשמעות בשקט. **צריך להכיר אותו** — הוא מופיע בתכנית ובמבחנים.

---

## 4. `ON` מול `USING`

כשעמודת החיבור נקראת **אותו דבר** בשתי הטבלאות, יש קיצור:

</div>

```sql
-- ON: write both sides
SELECT a.name, s.name
FROM   animal a JOIN species s ON s.species_id = a.species_id;

-- USING: name the shared column once
SELECT a.name, s.name
FROM   animal a JOIN species s USING (species_id);
```

<div dir="rtl">

| | `ON` | `USING` |
|---|---|---|
| תחביר | `ON a.x = b.y` | `USING (x)` |
| שמות שונים | ✅ (`adopter_id = person_id`) | ❌ רק כשהשם **זהה** |
| תנאים מורכבים | ✅ (`AND`, `<`, `BETWEEN`) | ❌ רק שוויון |
| העמודה בתוצאה | `a.x` ו‑`b.x` — שתיים | `x` **אחת** — בלי כינוי |

</div>

```sql
SELECT species_id, a.name                    -- no alias before species_id with USING
FROM   animal a JOIN species s USING (species_id)
WHERE  a.animal_id <= 2;
```

```text
species_id  name
----------  -----
1           Luna
2           Simba
```

<div dir="rtl">

> 💡 **`USING` הוא `NATURAL JOIN` בטוח:** גם הוא מחבר לפי שם עמודה, אבל **אתם** בוחרים אילו עמודות. ב‑Oracle אסור לשים כינוי לפני עמודת ה‑`USING` (`s.species_id` ⟵ שגיאה).

> 🔑 **ההמלצה:** `ON` תמיד עובד, בכל מצב. `USING` — קיצור נחמד כשהשמות זהים. כאן בקורס נמשיך עם `ON`.

---

## 5. Inner מול Outer — ספירת שורות

הדרך הטובה ביותר להבין סוגי JOIN היא **לספור**. לפני שמריצים — לחזות.

</div>

```sql
SELECT COUNT(*) FROM intake i JOIN      person p ON p.person_id = i.brought_by;   -- 19
SELECT COUNT(*) FROM intake i LEFT JOIN person p ON p.person_id = i.brought_by;   -- 21
```

<div dir="rtl">

**למה 2 שורות חסרות ב‑`JOIN`?** שתי קליטות מסוג `transfer` (Zoe ו‑Felix) הגיעו ממקלט אחר — `brought_by` הוא NULL. אין אדם שמתאים ל‑NULL, אז `JOIN` מעלים אותן.

</div>

```text
   Rule of thumb:
   INNER JOIN rows  <=  LEFT JOIN rows      (LEFT never loses rows of the left table)
   LEFT  JOIN rows  >=  rows in the left table   (more if a row has several matches)
```

<div dir="rtl">

> 🔑 **בדיקת שפיות לכל שאילתה עם JOIN:** כמה שורות יש בטבלה הראשית? כמה יצאו? אם יצאו **פחות** — `JOIN` העלים משהו. אם יצאו **הרבה יותר** — אולי חסר תנאי חיבור.

---

## 6. `RIGHT JOIN` ו‑`FULL OUTER JOIN`

### 6.1 `RIGHT JOIN` — `LEFT` הפוך

`A RIGHT JOIN B` שומר את **כל** B. זה בדיוק `B LEFT JOIN A`:

</div>

```sql
-- every species, with its available animals (Parrot and Rabbit appear too)
SELECT s.name AS species, a.name AS animal
FROM   animal a
RIGHT  JOIN species s ON s.species_id = a.species_id AND a.status = 'available'
ORDER  BY s.name, a.name;

-- same result, the way most people write it
SELECT s.name AS species, a.name AS animal
FROM   species s
LEFT   JOIN animal a ON a.species_id = s.species_id AND a.status = 'available'
ORDER  BY s.name, a.name;
```

<div dir="rtl">

> 💡 **בפועל כמעט כולם כותבים רק `LEFT`** — שמים את הטבלה ה"שמורה" ראשונה. קל יותר לקרוא שאילתה שבה הכיוון תמיד אותו כיוון. ⚠️ `RIGHT` ו‑`FULL` נתמכים ב‑SQLite רק מגרסה 3.39.

### 6.2 `FULL OUTER JOIN` — שני הצדדים

`FULL` שומר את כל השורות **משתי** הטבלאות. השימוש הטבעי: **השוואה בין שתי רשימות** — מה רק כאן, מה רק שם, מה בשתיהן.

</div>

```sql
-- what has no partner on either side?
SELECT a.name AS animal, e.expense_id, e.description
FROM   animal a
FULL   OUTER JOIN expense e ON e.animal_id = a.animal_id
WHERE  a.animal_id IS NULL OR e.expense_id IS NULL
ORDER  BY a.name, e.expense_id;
```

```text
animal   expense_id  description
-------  ----------  --------------------
         1           dry food, 20 sacks       <- only in expense (general)
         3           electricity January
         ...
         21          dry food, 20 sacks
Bunny                                         <- only in animal (no expense)
Charlie
...
Zoe
```

<div dir="rtl">

11 הוצאות כלליות + 10 חיות בלי הוצאות = 21 שורות. בלי ה‑`WHERE` — 32 שורות (סעיף 1).

### 6.3 ב‑Oracle הישן: `(+)` לא יודע `FULL`

עם `(+)` (מודול 21) אפשר לכתוב `LEFT` או `RIGHT` — אבל **לא** `FULL`. זו עוד סיבה לעבור לתחביר ה‑ANSI.

---

## 7. שרשרת JOIN‑ים — איפה LEFT נשבר

המלכודת הכי נפוצה במודול. רוצים **כל** הקליטות, עם שם החיה ושם מי שהביא:

</div>

```sql
SELECT a.name, i.intake_type, p.first_name AS brought_by
FROM   intake i
JOIN   animal a      ON a.animal_id = i.animal_id
LEFT   JOIN person p ON p.person_id = i.brought_by
WHERE  i.intake_type = 'transfer';
```

```text
name   intake_type  brought_by
-----  -----------  ----------
Zoe    transfer                    <- kept by the LEFT JOIN
Felix  transfer
```

<div dir="rtl">

**החלק החשוב:** `intake ⟵ animal` הוא `JOIN` — כי לכל קליטה **חייבת** להיות חיה (`animal_id NOT NULL`). `intake ⟵ person` הוא `LEFT JOIN` — כי `brought_by` **יכול** להיות NULL. **כל חיבור בשרשרת נבחר לפי היחס שלו.**

</div>

```text
   intake  --(JOIN: animal_id is NOT NULL)-->  animal
     |
     +-----(LEFT JOIN: brought_by may be NULL)-->  person
```

<div dir="rtl">

### 7.1 איך LEFT נשבר

אם אחרי `LEFT JOIN` מגיע `JOIN` רגיל **שתלוי בטבלה הימנית** — השורות עם NULL נעלמות שוב:

</div>

```text
   FROM expense e
   LEFT JOIN animal  a ON a.animal_id  = e.animal_id     -- keeps general expenses (a.* NULL)
   JOIN      species s ON s.species_id = a.species_id    -- NULL = ? never -> they vanish!
```

<div dir="rtl">

**התיקון:** כל `JOIN` שבא **אחרי** `LEFT` ותלוי בו — צריך גם הוא להיות `LEFT`:

</div>

```sql
SELECT e.description, a.name, s.name AS species
FROM   expense e
LEFT   JOIN animal  a ON a.animal_id  = e.animal_id
LEFT   JOIN species s ON s.species_id = a.species_id;    -- LEFT here too
```

<div dir="rtl">

> 🔑 **כלל ה"מפל":** ברגע שענף בשרשרת הפך ל‑`LEFT`, כל מה שתלוי בו — גם `LEFT`. אחרת ה‑NULL "שובר" את השרשרת.

---

## 8. איך בוחרים JOIN — שלוש שאלות

</div>

```text
   1. Which table's rows must ALL appear?        -> put it FIRST (FROM ...)
   2. For each other table: can a row be missing?
        no  (FK is NOT NULL, mandatory)          -> JOIN
        yes (FK may be NULL, optional, or
             "maybe it has none")                -> LEFT JOIN
   3. Does anything come after a LEFT JOIN and
      depend on it?                              -> LEFT JOIN too
```

<div dir="rtl">

| השאלה | הטבלה הראשונה | החיבור |
|-------|----------------|---------|
| "כל החיות ומספר החיסונים שלהן" | `animal` | `LEFT JOIN vaccination` (יש חיות בלי) |
| "כל החיסונים, עם שם החיה" | `vaccination` | `JOIN animal` (לכל חיסון יש חיה) |
| "כל ההוצאות עם שם החיה" | `expense` | `LEFT JOIN animal` (הוצאה כללית) |
| "מה חסר?" | הרשימה המלאה | `LEFT JOIN` + `IS NULL` |
| "מה רק כאן ומה רק שם?" | — | `FULL OUTER JOIN` |
| "כל הצירופים" | — | `CROSS JOIN` |

---

## 9. חמש טעויות נפוצות

| # | הטעות | מה קורה | התיקון |
|---|-------|----------|---------|
| 1 | **`NATURAL JOIN`** | מחבר גם לפי `name` — 0 שורות, או משמעות שמשתנה בשקט | `JOIN … ON` מפורש |
| 2 | **`JOIN` רגיל אחרי `LEFT`** | ה‑NULL‑ים של ה‑`LEFT` נעלמים | `LEFT` לכל מה שתלוי בו |
| 3 | **`s.species_id` עם `USING`** | שגיאה ב‑Oracle | בלי כינוי: `species_id` |
| 4 | **`CROSS JOIN` בלי לחשוב על הגודל** | 1,000 × 1,000 = מיליון שורות | לספור לפני: `COUNT(*)` |
| 5 | **לא סופרים שורות** | `JOIN` העלים שורות ואף אחד לא שם לב | לבדוק: שורות בטבלה הראשית מול שורות בתוצאה |

---

## 10. סיכום המודול

<div align="center">

### 🧠 שש נקודות

</div>

1. **חמישה סוגים:** `INNER` (רק זוגות), `LEFT`, `RIGHT`, `FULL` (גם בלי זוג), `CROSS` (כל הצירופים).
2. **`CROSS JOIN`** — תוצר קרטזי **בכוונה**: "כל מה שצריך להיות", ואז `LEFT JOIN` למה שיש ⟵ מה חסר.
3. **`NATURAL JOIN`** מחבר לפי **כל** העמודות בעלות אותו שם — מסוכן. להכיר, לא להשתמש.
4. **`USING (col)`** — קיצור בטוח כשהשם זהה. **`ON`** — תמיד עובד.
5. **`RIGHT` = `LEFT` הפוך**; **`FULL`** — להשוואת שתי רשימות.
6. **בשרשרת:** כל חיבור לפי היחס שלו, ומה שתלוי ב‑`LEFT` — גם `LEFT`. **ותמיד לספור שורות.**

<div align="center">

---

*"אין JOIN נכון או לא נכון.*
*יש JOIN שעונה על השאלה — ויש כזה שעונה על שאלה אחרת."*

---

</div>

## 📎 המשך

| | |
|---|---|
| ❓ | [שאלות ותשובות](questions.md) |
| ✏️ | [תרגילים](exercises.md) — על [בסיס הנתונים המוכן](../../resources/shelter-db/) |
| ✅ | [פתרונות](solutions.md) — עם הפלט האמיתי |
| ⬅️ | [מודול 21 — SQL: איחוד טבלאות](../module-21-sql-joins/) |
| 🧭 | [מסלול הלימוד](../../LEARNING-PATH.md) — יחידה 5 הושלמה; הבאה: מודול 6 + 23–24 |
| ➡️ | [מודול 23 — SQL: פונקציות מצרפיות](../module-23-sql-aggregates/) |
| 🏠 | [חזרה לדף הקורס](../../) |

</div>
