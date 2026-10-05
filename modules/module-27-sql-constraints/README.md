<div dir="rtl">

# מודול 27 — SQL: אילוצים

> **פרק 27 בתכנית הלימודים** · 3 שעות עיוני + 3 שעות מעשי
> **נושאים:** NOT NULL and UNIQUE · PRIMARY KEY, FOREIGN KEY, and CHECK · ניהול אילוצים

> 🧭 **במסלול המשולב:** יחידה 7, לצד [מודול 7 — אילוצים](../module-07-constraints/). **אותם חוקים — בקוד.** מודול 7 אמר מה החוקים העסקיים; כאן בסיס הנתונים אוכף אותם.

---

## 🎯 מה תדעו בסוף המודול

- [ ] להסביר למה אילוץ בבסיס הנתונים עדיף על בדיקה בתוכנה
- [ ] להגדיר את חמשת האילוצים: `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`, `CHECK`
- [ ] להגדיר מפתח ראשי ו‑`UNIQUE` **מורכבים** (כמה עמודות)
- [ ] לבחור מה קורה למחיקת הורה: חסימה, `CASCADE` או `SET NULL`
- [ ] לתרגם **קשת** (arc) ממודול 7 לאילוץ `CHECK`
- [ ] לתת שמות לאילוצים, ולהוסיף / למחוק / להשבית אותם (Oracle)

---

## 🗺️ מפת המודול

| # | הסעיף |
|---|--------|
| 1 | [למה אילוצים](#1-למה-אילוצים) |
| 2 | [NOT NULL](#2-not-null) |
| 3 | [UNIQUE](#3-unique) |
| 4 | [PRIMARY KEY](#4-primary-key) |
| 5 | [FOREIGN KEY — ומה קורה במחיקה](#5-foreign-key--ומה-קורה-במחיקה) |
| 6 | [CHECK — כל חוק שאפשר לנסח כתנאי](#6-check--כל-חוק-שאפשר-לנסח-כתנאי) |
| 7 | [קשתות (Arcs) ב‑CHECK](#7-קשתות-arcs-בcheck) |
| 8 | [שמות לאילוצים, ורמת עמודה מול רמת טבלה](#8-שמות-לאילוצים-ורמת-עמודה-מול-רמת-טבלה) |
| 9 | [ניהול אילוצים](#9-ניהול-אילוצים) |
| 10 | [דוגמה מלאה — טבלת השיכון](#10-דוגמה-מלאה--טבלת-השיכון) |
| 11 | [חמש טעויות נפוצות](#11-חמש-טעויות-נפוצות) |
| 12 | [סיכום המודול](#12-סיכום-המודול) |

---

## 1. למה אילוצים

אפשר לבדוק כל חוק **בתוכנה** — בטופס באתר, באפליקציה. אז למה גם בבסיס הנתונים?

</div>

```text
   the website form       checks "sex is M/F/U"     OK
   the mobile app         forgot the check          'X' gets in
   an import script       no checks at all          'male', 'm', '1' get in
   a manual UPDATE        nobody checks             ...

   one CHECK constraint in the table  -->  ALL of them are blocked. Always.
```

<div dir="rtl">

> 🔑 **בסיס הנתונים הוא קו ההגנה האחרון — והיחיד שכולם עוברים דרכו.** אפליקציות מתחלפות; הנתונים נשארים לשנים. חוק שנאכף רק בקוד — ייעקף, במוקדם או במאוחר.

**חמשת האילוצים:**

| האילוץ | החוק | ממודול 7 |
|---------|------|-----------|
| `NOT NULL` | חייב ערך | מאפיין חובה (`*`) |
| `UNIQUE` | אין שני ערכים זהים | מזהה ייחודי משני |
| `PRIMARY KEY` | `NOT NULL` + `UNIQUE` — המזהה של השורה | מזהה ייחודי (`#`) |
| `FOREIGN KEY` | הערך חייב להופיע בטבלה אחרת | יחס |
| `CHECK` | כל תנאי | תחומים (domains), קשתות |

> ⚠️ **ב‑SQLite — `PRAGMA foreign_keys = ON;` בתחילת כל סשן** (מודול 25), אחרת מפתחות זרים לא נבדקים.

---

## 2. NOT NULL

</div>

```sql
name  TEXT NOT NULL
```

<div dir="rtl">

הפשוט והחשוב מכולם. **כלל:** כל עמודה `NOT NULL`, אלא אם יש **סיבה עסקית** שערך יהיה חסר — תאריך לידה של חיה משוטטת, שבב לחיה שאין לה. **כל עמודה שמותר לה NULL היא שאלה שכל שאילתה תצטרך לענות עליה** (מודולים 16, 20, 23).

---

## 3. UNIQUE

</div>

```sql
chip_number TEXT UNIQUE          -- one chip = one animal
```

```text
   INSERT ... chip_number = '985100001'   (Luna's chip)
   --> UNIQUE constraint failed: animal.chip_number
```

<div dir="rtl">

### 3.1 UNIQUE ו‑NULL

</div>

```sql
CREATE TABLE contact (person_id INTEGER, email TEXT UNIQUE);
INSERT INTO contact VALUES (1, NULL), (2, NULL);       -- both accepted!
```

<div dir="rtl">

**שני NULL‑ים לא נחשבים כפילות** — כי NULL הוא "לא ידוע", ושני "לא ידוע" אינם בהכרח שווים. לכן 7 חיות בלי שבב לא מפרות את `UNIQUE` על `chip_number`. **זה בדיוק מה שרוצים**: ייחודי **כשיש** ערך.

### 3.2 UNIQUE מורכב

לפעמים הייחודיות היא של **צירוף**: לא יכול להיות שאותה חיה תקבל אותו חיסון פעמיים **באותו יום**. כל עמודה לבד יכולה לחזור — הצירוף לא:

</div>

```sql
CONSTRAINT uq_vacc UNIQUE (animal_id, vaccine_type_id, given_date)
```

<div dir="rtl">

> 💡 **לפני שמוסיפים `UNIQUE` לטבלה קיימת** — בודקים שאין כבר כפילויות (מודול 24): `GROUP BY col HAVING COUNT(*) > 1`. אם יש — האילוץ ייכשל.

---

## 4. PRIMARY KEY

`PRIMARY KEY` = `NOT NULL` + `UNIQUE` + "**זה** המזהה של השורה". אחד לטבלה.

### 4.1 מפתח מלאכותי מול מפתח טבעי

| | מלאכותי (surrogate) | טבעי (natural) |
|---|---|---|
| דוגמה | `animal_id = 7` | `chip_number = '985100007'` |
| משמעות עסקית | אין | יש |
| יכול להשתנות? | לעולם לא | כן — שבב מוחלף, ת"ז מתוקנת |
| תמיד קיים? | כן | לא — לחיה משוטטת אין שבב |

> 🔑 **מודול 6:** משתמשים במפתח **מלאכותי** כמפתח ראשי, ושמים `UNIQUE` על המזהה הטבעי. כך מקבלים את שני העולמות: מזהה יציב, **וגם** הגנה מכפילויות.

### 4.2 מפתח ראשי מורכב

בטבלת קישור (מודול 5) המפתח הוא לעיתים **צירוף** המפתחות הזרים:

</div>

```sql
CREATE TABLE kennel_stay (
  animal_id  INTEGER NOT NULL REFERENCES animal(animal_id),
  kennel_id  INTEGER NOT NULL REFERENCES kennel(kennel_id),
  from_date  TEXT    NOT NULL,
  to_date    TEXT,
  CONSTRAINT pk_kennel_stay PRIMARY KEY (animal_id, from_date)    -- two columns
);
```

<div dir="rtl">

**החוק שהמפתח אוכף:** "חיה לא יכולה להתחיל שתי שהיות באותו יום". אותה חיה — בימים שונים ✅. אותו יום — חיות שונות ✅. אותה חיה **ואותו** יום ❌.

---

## 5. FOREIGN KEY — ומה קורה במחיקה

</div>

```sql
species_id INTEGER NOT NULL REFERENCES species(species_id)
```

<div dir="rtl">

מפתח זר מבטיח **שלמות התייחסותית** (referential integrity): אין חיה ממין שלא קיים, אין חיסון של חיה שלא קיימת. **שתי בדיקות:**
- **הכנסה / עדכון בילד:** הערך חייב להופיע בהורה.
- **מחיקה / עדכון בהורה:** מה קורה לילדים?

### 5.1 שלוש אפשרויות למחיקת הורה

</div>

```text
   DELETE FROM kennel WHERE kennel_id = 2;    -- kennel 2 has animals in it

   (default)              -> ERROR. You must deal with the children first.
   ON DELETE CASCADE      -> the children are deleted too.
   ON DELETE SET NULL     -> the children stay, their FK becomes NULL.
```

```sql
CREATE TABLE kennel_stay (
  animal_id INTEGER NOT NULL REFERENCES animal(animal_id) ON DELETE CASCADE,
  kennel_id INTEGER          REFERENCES kennel(kennel_id) ON DELETE SET NULL,
  from_date TEXT    NOT NULL,
  PRIMARY KEY (animal_id, from_date)
);
INSERT INTO kennel_stay VALUES (19, 1, '2025-02-20'), (3, 2, '2023-05-20');

DELETE FROM kennel WHERE kennel_id = 2;      -- the kennel is demolished
SELECT * FROM kennel_stay;
```

```text
animal_id  kennel_id  from_date
---------  ---------  ----------
19         1          2025-02-20
3                     2023-05-20     <- SET NULL: Rocky's stay is kept, kennel unknown
```

<div dir="rtl">

| ההתנהגות | מתי מתאים | דוגמה |
|----------|-----------|--------|
| **חסימה** (ברירת מחדל) | כמעט תמיד | אי אפשר למחוק מין שיש לו חיות |
| `CASCADE` | הילד **חסר משמעות** בלי ההורה | שורות הזמנה כשההזמנה נמחקת |
| `SET NULL` | הילד **קיים** גם בלי ההורה | הוצאה נשארת גם אם החיה נמחקה (הופכת ל"כללית") |

> ⚠️ **`CASCADE` הוא אקדח טעון.** מחיקת מין אחד ⟵ כל החיות ממנו ⟵ כל החיסונים, האימוצים וההוצאות שלהן. שורה אחת, מאות מחיקות, בלי אזהרה. **השתמשו בו רק כשהילד באמת "חלק" מההורה.** ו‑`SET NULL` דורש שהעמודה **תאפשר** NULL.

---

## 6. CHECK — כל חוק שאפשר לנסח כתנאי

</div>

```sql
sex      TEXT    NOT NULL CHECK (sex IN ('M', 'F', 'U')),
capacity INTEGER NOT NULL CHECK (capacity BETWEEN 1 AND 4),
CONSTRAINT chk_dates CHECK (to_date IS NULL OR to_date >= from_date)
```

```text
   INSERT ... size = 'XL'                  --> CHECK constraint failed: size IN ('S','M','L')
   INSERT ... capacity = 9                 --> CHECK constraint failed: capacity BETWEEN 1 AND 4
   INSERT ... from 2024-05-25 to 2024-05-01 --> CHECK constraint failed: chk_dates
```

<div dir="rtl">

| סוג החוק | הדוגמה |
|----------|---------|
| רשימת ערכים (תחום) | `CHECK (status IN ('available', 'adopted', …))` |
| טווח | `CHECK (weight_kg > 0)` |
| השוואה בין עמודות | `CHECK (to_date >= from_date)` |
| תנאי מותנה | `CHECK (category <> 'medical' OR animal_id IS NOT NULL)` — "הוצאה רפואית חייבת חיה" |

> ⚠️ **`CHECK` עם NULL עובר.** `CHECK (weight_kg > 0)` על `weight_kg = NULL` ⟵ התנאי "לא ידוע" ⟵ **מותר**. אם רוצים לאסור גם NULL — `NOT NULL` בנוסף.

> 💡 **מה `CHECK` לא יכול:** לבדוק **שורות אחרות** או **טבלאות אחרות**. "לא יותר מ‑4 חיות בכלוב" — דורש לספור שורות; זה לא `CHECK`. לזה יש **טריגרים** (Triggers) — מעבר לתכנית, אבל טוב לדעת שקיימים.

---

## 7. קשתות (Arcs) ב‑CHECK

במודול 7 למדנו **קשת**: ישות שקשורה ל**אחת** משתי ישויות — לא לשתיהן, לא לאף אחת. תשלום הוא **או** דמי אימוץ **או** תרומה:

</div>

```text
                 +--------- ADOPTION
   PAYMENT ---- (arc)
                 +--------- DONATION        exactly ONE of the two
```

```sql
CREATE TABLE payment (
  payment_id  INTEGER PRIMARY KEY,
  adoption_id INTEGER REFERENCES adoption(adoption_id),
  donation_id INTEGER,
  CONSTRAINT chk_arc CHECK (
       (adoption_id IS NOT NULL AND donation_id IS NULL)
    OR (adoption_id IS NULL     AND donation_id IS NOT NULL)
  )
);

INSERT INTO payment VALUES (1, 5, NULL);     -- OK: an adoption payment
INSERT INTO payment VALUES (2, 5, 7);        -- CHECK constraint failed: chk_arc  (both)
INSERT INTO payment VALUES (3, NULL, NULL);  -- CHECK constraint failed: chk_arc  (neither)
```

<div dir="rtl">

> 🔑 **קשת = שני מפתחות זרים אופציונליים + `CHECK` ש"בדיוק אחד" מהם מלא.** זה התרגום הסטנדרטי — ושאלה נפוצה במבחן.

---

## 8. שמות לאילוצים, ורמת עמודה מול רמת טבלה

### 8.1 שתי דרכים לכתוב

</div>

```sql
CREATE TABLE kennel (
  kennel_id INTEGER PRIMARY KEY,                       -- column level: right after the column
  code      TEXT    NOT NULL UNIQUE,
  size      TEXT    NOT NULL,
  CONSTRAINT chk_kennel_size CHECK (size IN ('S','M','L'))   -- table level: at the end, with a name
);
```

<div dir="rtl">

| | רמת עמודה | רמת טבלה |
|---|---|---|
| איפה | ליד העמודה | בסוף, אחרי כל העמודות |
| כמה עמודות | אחת | אחת או יותר |
| חובה ל‑ | — | מפתח ראשי / `UNIQUE` **מורכב**, `CHECK` בין עמודות |
| `NOT NULL` | ✅ רק כאן | ❌ |

### 8.2 למה לתת שם

</div>

```text
   without a name:   ORA-02290: check constraint (SHELTER.SYS_C0012345) violated
   with a name:      ORA-02290: check constraint (SHELTER.CHK_KENNEL_SIZE) violated
```

<div dir="rtl">

הודעת שגיאה עם **שם שמסביר** חוסכת חצי שעה של חיפוש. וכדי למחוק או להשבית אילוץ (סעיף 9) — צריך לדעת את שמו. **מוסכמה:** `pk_` מפתח ראשי, `fk_` מפתח זר, `uq_` ייחודי, `chk_` בדיקה, ואחריו שם הטבלה/העמודה.

---

## 9. ניהול אילוצים

### 9.1 ב‑Oracle

</div>

```sql
ALTER TABLE animal ADD CONSTRAINT chk_weight CHECK (weight_kg > 0);
ALTER TABLE animal DROP CONSTRAINT chk_weight;

ALTER TABLE animal DISABLE CONSTRAINT fk_animal_species;   -- e.g. during a big import
ALTER TABLE animal ENABLE  CONSTRAINT fk_animal_species;   -- checks ALL rows again

SELECT constraint_name, constraint_type, search_condition
FROM   user_constraints
WHERE  table_name = 'ANIMAL';
-- constraint_type:  P = primary key, R = foreign key (Reference), U = unique, C = check / not null
```

<div dir="rtl">

### 9.2 ב‑SQLite

ב‑SQLite **אי אפשר** להוסיף או למחוק אילוץ בטבלה קיימת עם `ALTER TABLE`. הדרך היא "הבנייה מחדש": טבלה חדשה עם האילוצים הנכונים ⟵ `INSERT … SELECT` ⟵ `DROP` הישנה ⟵ `RENAME` החדשה. (בדיוק כמו שינוי טיפוס במודול 26.)

> 🔑 **המסקנה המעשית:** חשבו על האילוצים **לפני** `CREATE TABLE`. כל חוק ממודול 7 — שורה בהגדרת הטבלה.

---

## 10. דוגמה מלאה — טבלת השיכון

רותי רוצה לדעת איפה כל חיה ישנה. **החוקים העסקיים:** כל כלוב עם קוד ייחודי, גודל S/M/L, וקיבולת 1–4. כל שהייה — חיה, כלוב, תאריך התחלה (חובה) ותאריך סיום (אופציונלי, לא לפני ההתחלה). חיה לא מתחילה שתי שהיות באותו יום. אם חיה נמחקת — השהיות שלה נמחקות.

</div>

```sql
PRAGMA foreign_keys = ON;

CREATE TABLE kennel (
  kennel_id  INTEGER PRIMARY KEY,
  code       TEXT    NOT NULL,
  size       TEXT    NOT NULL,
  capacity   INTEGER NOT NULL,
  CONSTRAINT uq_kennel_code  UNIQUE (code),
  CONSTRAINT chk_kennel_size CHECK (size IN ('S', 'M', 'L')),
  CONSTRAINT chk_kennel_cap  CHECK (capacity BETWEEN 1 AND 4)
) STRICT;

CREATE TABLE kennel_stay (
  animal_id  INTEGER NOT NULL,
  kennel_id  INTEGER NOT NULL,
  from_date  TEXT    NOT NULL,
  to_date    TEXT,
  CONSTRAINT pk_kennel_stay PRIMARY KEY (animal_id, from_date),
  CONSTRAINT fk_stay_animal FOREIGN KEY (animal_id) REFERENCES animal(animal_id) ON DELETE CASCADE,
  CONSTRAINT fk_stay_kennel FOREIGN KEY (kennel_id) REFERENCES kennel(kennel_id),
  CONSTRAINT chk_stay_dates CHECK (to_date IS NULL OR to_date >= from_date)
) STRICT;

INSERT INTO kennel VALUES (1, 'A-01', 'L', 2), (2, 'A-02', 'L', 2), (3, 'C-01', 'S', 4);
INSERT INTO kennel_stay VALUES (3, 1, '2023-05-20', NULL);
```

<div dir="rtl">

**וכל ניסיון לשבור חוק — נחסם:**

</div>

```text
   INSERT INTO kennel VALUES (4, 'A-01', 'M', 2);              UNIQUE constraint failed: kennel.code
   INSERT INTO kennel VALUES (4, 'B-01', 'XL', 2);             CHECK constraint failed: chk_kennel_size
   INSERT INTO kennel VALUES (4, 'B-01', 'M', 9);              CHECK constraint failed: chk_kennel_cap
   INSERT INTO kennel_stay VALUES (3, 2, '2023-05-20', NULL);  UNIQUE constraint failed:
                                                                 kennel_stay.animal_id, kennel_stay.from_date
   INSERT INTO kennel_stay VALUES (13, 1, '2024-05-25', '2024-05-01');   CHECK constraint failed: chk_stay_dates
   INSERT INTO kennel_stay VALUES (13, 9, '2024-05-25', NULL); FOREIGN KEY constraint failed
```

<div dir="rtl">

> 🎬 **שש שורות — שש טעויות שלא ייכנסו לעולם.** ושימו לב לחוק שחסר: "לא יותר מ‑2 חיות בכלוב A-01 בו‑זמנית". `capacity` שמור — אבל **שום אילוץ לא סופר** כמה חיות יש בכלוב (סעיף 6). זה יצטרך טריגר, או בדיקה באפליקציה.

---

## 11. חמש טעויות נפוצות

| # | הטעות | מה קורה | התיקון |
|---|-------|----------|---------|
| 1 | **לשכוח `PRAGMA foreign_keys = ON`** | מפתחות זרים לא נבדקים | שורה ראשונה בכל סשן SQLite |
| 2 | **`CHECK` בלי `NOT NULL`** | NULL עובר את הבדיקה | שניהם, אם הערך חובה |
| 3 | **`CASCADE` בכל מקום** | מחיקה אחת מוחקת חצי מבסיס הנתונים | ברירת המחדל (חסימה), אלא אם יש סיבה |
| 4 | **מפתח טבעי כמפתח ראשי** | שבב מוחלף ⟵ צריך לעדכן בכל הטבלאות | מפתח מלאכותי + `UNIQUE` על הטבעי |
| 5 | **אילוצים בלי שמות** | `SYS_C0012345` בהודעת השגיאה | `CONSTRAINT chk_… CHECK (…)` |

---

## 12. סיכום המודול

<div align="center">

### 🧠 שש נקודות

</div>

1. **אילוצים = החוקים העסקיים, בתוך בסיס הנתונים.** הם חלים על כל מי שכותב — אפליקציה, סקריפט, אדם.
2. **`NOT NULL`** — חובה. **`UNIQUE`** — בלי כפילויות (NULL‑ים מותרים). **`PRIMARY KEY`** — שניהם יחד, אחד לטבלה.
3. **מורכב:** `PRIMARY KEY (a, b)` / `UNIQUE (a, b, c)` — הייחודיות של **הצירוף**.
4. **`FOREIGN KEY`:** חסימה (ברירת מחדל) · `ON DELETE CASCADE` · `ON DELETE SET NULL`.
5. **`CHECK`** — כל תנאי על השורה. **קשת** = שני מפתחות זרים + `CHECK` "בדיוק אחד". NULL עובר `CHECK`.
6. **שמות לאילוצים** — `pk_`, `fk_`, `uq_`, `chk_`. ב‑Oracle: `ADD` / `DROP` / `DISABLE` / `ENABLE CONSTRAINT`. ב‑SQLite: חושבים מראש.

<div align="center">

---

*"כל אילוץ הוא באג שלא יקרה.*
*וכל חוק עסקי בלי אילוץ — הוא באג שמחכה."*

---

</div>

## 📎 המשך

| | |
|---|---|
| ❓ | [שאלות ותשובות](questions.md) |
| ✏️ | [תרגילים](exercises.md) |
| ✅ | [פתרונות](solutions.md) |
| ⬅️ | [מודול 26 — SQL: DDL](../module-26-sql-ddl/) |
| 🧭 | [מסלול הלימוד](../../LEARNING-PATH.md) — יחידה 7 הושלמה; הבאה: מודול 12 + 26 |
| ➡️ | [מודול 28 — SQL: שאילתות שמורות (Views)](../module-28-sql-views/) |
| 🏠 | [חזרה לדף הקורס](../../) |

</div>
