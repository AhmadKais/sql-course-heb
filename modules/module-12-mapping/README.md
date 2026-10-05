<div dir="rtl">

# מודול 12 — מעבר לבסיס הנתונים

> **פרק 12 בתכנית הלימודים** · 4 שעות עיוני + 2 שעות מעשי
> **נושאים:** מבוא למונחי מסד נתונים רלציוני · מיפוי בסיסי — תהליך המעבר · מיפוי יחסים · מיפוי טיפוסי משנה · מבוא ל‑Application Express

> 🧭 **במסלול המשולב:** יחידה 8, לצד [מודול 26 — DDL](../module-26-sql-ddl/). ⭐ **כאן נגמר הציור ומתחילה הבנייה.** המודול הזה אומר **מה** כל סימן ב‑ERD הופך להיות; מודול 26 אומר **איך כותבים** את זה.

---

## 🎯 מה תדעו בסוף המודול

- [ ] להבדיל בין **מודל קונספטואלי** (ERD) ל**מודל לוגי / פיזי** (טבלאות)
- [ ] להכיר את מונחי המסד הרלציוני: טבלה, עמודה, שורה, מפתח ראשי, מפתח זר, אילוץ
- [ ] למפות **ישות** לטבלה, **מאפיין** לעמודה, **מזהה** למפתח
- [ ] למפות כל סוג **יחס**: 1:M, 1:1, יחס מזהה (barred), רקורסיבי, קשת
- [ ] לבחור בין **שלוש** דרכים למפות **טיפוסי משנה** — ולנמק
- [ ] להכיר את **Oracle APEX** — וכלים דומים שמייצרים טבלאות מתרשים

---

## 🗺️ מפת המודול

| # | הסעיף |
|---|--------|
| 1 | [משלושה מודלים — מהשיחה עם הלקוח לדיסק](#1-משלושה-מודלים--מהשיחה-עם-הלקוח-לדיסק) |
| 2 | [מילון המונחים: ERD מול טבלאות](#2-מילון-המונחים-erd-מול-טבלאות) |
| 3 | [מיפוי בסיסי — ישות, מאפיין, מזהה](#3-מיפוי-בסיסי--ישות-מאפיין-מזהה) |
| 4 | [מיפוי יחסים](#4-מיפוי-יחסים) |
| 5 | [מיפוי טיפוסי משנה — שלוש דרכים](#5-מיפוי-טיפוסי-משנה--שלוש-דרכים) |
| 6 | [מוסכמות שמות במעבר](#6-מוסכמות-שמות-במעבר) |
| 7 | [דוגמה מלאה — חלק מהמקלט](#7-דוגמה-מלאה--חלק-מהמקלט) |
| 8 | [מבוא ל‑Application Express (APEX)](#8-מבוא-לapplication-express-apex) |
| 9 | [שש טעויות נפוצות](#9-שש-טעויות-נפוצות) |
| 10 | [סיכום המודול](#10-סיכום-המודול) |

---

## 1. משלושה מודלים — מהשיחה עם הלקוח לדיסק

</div>

```text
   CONCEPTUAL model            LOGICAL model                 PHYSICAL model
   (modules 2-11)              (THIS module)                 (module 26)
   ------------------          ------------------            ------------------
   entities, attributes,       tables, columns,              CREATE TABLE in a
   relationships, UIDs         primary & foreign keys,       specific database:
   "what the business is"      constraints                   data types, STRICT,
                                                             indexes, storage
   for the CLIENT              for the DESIGNER              for the DATABASE
   no technology               any relational database       SQLite / Oracle / ...
```

<div dir="rtl">

> 🔑 **למה לא קופצים ישר מה‑ERD ל‑`CREATE TABLE`?** כי יש החלטות שה‑ERD לא מכריע: איך ממפים טיפוסי משנה? איפה שמים את המפתח הזר ביחס 1:1? מה עושים עם קשת? **המיפוי הוא סדרת החלטות** — והמודול הזה מלמד את החוקים, ואיפה יש בחירה.

---

## 2. מילון המונחים: ERD מול טבלאות

| ב‑ERD (קונספטואלי) | בטבלאות (לוגי) | בבסיס הנתונים |
|---------------------|----------------|----------------|
| ישות (entity) | **טבלה** (table) | `CREATE TABLE` |
| מופע (instance) | **שורה** (row) | `INSERT` |
| מאפיין (attribute) | **עמודה** (column) | עמודה עם טיפוס |
| מאפיין חובה `*` | עמודת `NOT NULL` | `NOT NULL` |
| מאפיין אופציונלי `o` | עמודה שמותר NULL | — |
| מזהה ייחודי `#` | **מפתח ראשי** (pk) | `PRIMARY KEY` |
| מזהה משני | **מפתח ייחודי** (uk) | `UNIQUE` |
| יחס (relationship) | **מפתח זר** (fk) | `REFERENCES` |
| חוק עסקי | **אילוץ** (constraint) | `CHECK`, `NOT NULL`… |
| תחום (domain) של מאפיין | טיפוס + `CHECK` | `TEXT CHECK (sex IN …)` |

> 💡 **מילה אחת שמבלבלת:** ב‑ERD "יחס" (relationship) הוא קו בין ישויות. במתמטיקה של בסיסי נתונים, **"relation" = טבלה** — ומשם השם "רלציוני". כשאומרים "בסיס נתונים רלציוני", הכוונה "בסיס נתונים של טבלאות".

---

## 3. מיפוי בסיסי — ישות, מאפיין, מזהה

**החוק:** כל ישות ⟵ טבלה. כל מאפיין ⟵ עמודה. המזהה ⟵ מפתח ראשי.

</div>

```text
   ERD                                  TABLE: species
   +-----------------------+            +------+----------------+------------------+
   | SPECIES               |            | key  | column         | null?            |
   | # species id          |  ------>   | pk   | species_id     | NOT NULL         |
   | * name                |            | uk   | name           | NOT NULL         |
   | * adoption fee        |            |      | adoption_fee   | NOT NULL         |
   +-----------------------+            +------+----------------+------------------+
```

```sql
CREATE TABLE species (
  species_id   INTEGER PRIMARY KEY,
  name         TEXT    NOT NULL,
  adoption_fee REAL    NOT NULL,
  CONSTRAINT uq_species_name UNIQUE (name)
);
```

<div dir="rtl">

### 3.1 מאפיינים שלא עוברים כמו שהם

| במודל הקונספטואלי | בטבלה | למה |
|---------------------|--------|-----|
| מאפיין **מורכב** — "כתובת" | כמה עמודות: `street`, `city`, `zip` | שאילתות לפי עיר |
| מאפיין **רב‑ערכי** — "טלפונים" | **טבלה נפרדת** `phone` | 1NF — ראינו בנרמול (מודול 6) |
| מאפיין **נגזר** — "גיל" | **לא נשמר** — מחושב | החלטה 12 בפרויקט; מודול 19 |
| מאפיין עם **רשימת ערכים** — "מין" | עמודה + `CHECK` | או טבלת קוד, אם הרשימה משתנה |

> 🔑 **אם ביצעתם נרמול כמו שצריך במודול 6, המיפוי פשוט:** הרב‑ערכיים כבר הפכו לישויות (`PHONE`, `TRAIT`), והנגזרים כבר הוצאו. **נרמול עושה את העבודה הקשה מראש.**

---

## 4. מיפוי יחסים

### 4.1 יחס 1:M — מפתח זר בצד ה"רבים"

</div>

```text
   SPECIES  1 -------< M  ANIMAL          "each animal is of exactly one species"

   ANIMAL table gets:  species_id  (fk -> species)
                       NOT NULL     because the relationship is MANDATORY on the animal side
```

<div dir="rtl">

**החוק:** המפתח הזר הולך **תמיד** לצד של ה"רבים" (הרגל של העורב). חיה מכירה את המין שלה; המין לא מחזיק רשימה של חיות.

| האופציונליות בצד ה"רבים" | העמודה |
|---------------------------|---------|
| חובה ("כל חיה **חייבת** מין") — קו רציף | `species_id INTEGER NOT NULL` |
| אופציונלי ("הוצאה **יכולה** להיות של חיה") — קו מקווקו | `animal_id INTEGER` (מותר NULL) |

> 💡 **בדיקה:** בבסיס הנתונים המוכן, `animal.species_id` הוא `NOT NULL`, ו‑`expense.animal_id` מותר NULL. **ה‑ERD קבע את זה** — המיפוי רק תרגם.

### 4.2 יחס M:M — כבר נפתר

אם עשיתם את מודול 5 נכון, אין יותר יחסי רבים‑לרבים: כל אחד הפך ל**ישות מקשרת** (`ADOPTION` בין `ANIMAL` ל‑`PERSON`). והישות המקשרת ממופה כמו כל ישות — **עם שני מפתחות זרים**.

> ⚠️ **אם נשאר M:M בתרשים — עצרו וחזרו למודול 5.** אין דרך למפות M:M ישירות לטבלאות.

### 4.3 יחס מזהה (barred) — המפתח הזר הוא חלק מהמפתח הראשי

במודול 5 סימנו בקו (bar) יחס שבו הישות **מזוהה** דרך ההורה שלה. טלפון מזוהה על ידי **האדם** + **המספר**:

</div>

```text
   PERSON  1 ---|----< M  PHONE           the bar: PHONE is identified THROUGH person
                                          # person (via the relationship)
                                          # phone number
```

```sql
CREATE TABLE phone (
  person_id INTEGER NOT NULL,
  phone_no  TEXT    NOT NULL,
  kind      TEXT    NOT NULL DEFAULT 'mobile',
  CONSTRAINT pk_phone        PRIMARY KEY (person_id, phone_no),          -- fk is PART of the pk
  CONSTRAINT fk_phone_person FOREIGN KEY (person_id) REFERENCES person(person_id)
);
```

<div dir="rtl">

### 4.4 יחס 1:1 — מפתח זר + `UNIQUE`

פרטי וטרינר (מספר רישיון) שייכים לאדם אחד, ולכל אדם לכל היותר רשומת וטרינר אחת:

</div>

```sql
CREATE TABLE vet_details (
  person_id      INTEGER PRIMARY KEY REFERENCES person(person_id),   -- fk AND pk = 1:1
  license_number TEXT    NOT NULL UNIQUE
);
```

<div dir="rtl">

**איפה שמים את המפתח הזר ב‑1:1?** בצד ה**אופציונלי** — הצד ש"לא תמיד קיים". לא לכל אדם יש פרטי וטרינר, אבל לכל פרטי וטרינר יש אדם. אם המפתח הזר הוא גם המפתח הראשי — הייחודיות מובטחת אוטומטית.

### 4.5 יחס רקורסיבי — מפתח זר לאותה טבלה

החלטה 5 בפרויקט: אמא ⟵ גורים.

</div>

```sql
CREATE TABLE animal (
  animal_id INTEGER PRIMARY KEY,
  mother_id INTEGER REFERENCES animal(animal_id),    -- NULL: mother unknown / not ours
  ...
);
```

<div dir="rtl">

> 💡 **רקורסיבי הוא תמיד אופציונלי** בצד אחד לפחות — אחרת לא הייתה "חיה ראשונה". ושליפה של כל הצאצאים — `WITH RECURSIVE` (מודול 21).

### 4.6 קשת (arc) — שני מפתחות זרים + `CHECK`

</div>

```sql
CREATE TABLE payment (
  payment_id  INTEGER PRIMARY KEY,
  adoption_id INTEGER REFERENCES adoption(adoption_id),
  donation_id INTEGER REFERENCES donation(donation_id),
  CONSTRAINT chk_payment_arc CHECK (
       (adoption_id IS NOT NULL AND donation_id IS NULL)
    OR (adoption_id IS NULL     AND donation_id IS NOT NULL))
);
```

<div dir="rtl">

(מפורט במודול 27, סעיף 7.)

### 4.7 סיכום מיפוי היחסים

| ב‑ERD | בטבלאות |
|-------|---------|
| 1:M, חובה בצד הרבים | fk `NOT NULL` בצד הרבים |
| 1:M, אופציונלי | fk שמותר NULL |
| M:M | ⛔ — חייב להיפתר קודם לישות מקשרת |
| יחס מזהה (bar) | fk שהוא **חלק מה‑pk** |
| 1:1 | fk + `UNIQUE` (או fk = pk), בצד האופציונלי |
| רקורסיבי | fk לאותה טבלה, מותר NULL |
| קשת | fk לכל ענף + `CHECK` "בדיוק אחד" |

---

## 5. מיפוי טיפוסי משנה — שלוש דרכים

**ההחלטה הכי חשובה במודול.** ב‑ERD יש `ANIMAL` עם טיפוסי משנה `DOG`, `CAT`, `RABBIT`, `PARROT`. לכלב יש `is_house_trained`; לחתול `is_indoor`. איך זה הופך לטבלאות?

</div>

```text
   A. SINGLE TABLE              B. TABLE PER SUBTYPE           C. SUPERTYPE + SUBTYPES
      (supertype only)             (subtypes only)                (both)

   animal                       dog          cat               animal         dog
   +-------------------+        +--------+   +--------+        +---------+    +-----------------+
   | animal_id         |        | id     |   | id     |        | id      |<---| animal_id (pk,fk)|
   | name              |        | name   |   | name   |        | name    |    | is_house_trained|
   | species  (D/C/..) |        | sex    |   | sex    |        | sex     |    +-----------------+
   | is_house_trained  |        | house_ |   | is_    |        | species |    cat
   | is_indoor         |        | trained|   | indoor |        +---------+    +-----------------+
   +-------------------+        +--------+   +--------+                  <---| animal_id (pk,fk)|
   one table, many NULLs        common columns repeated                      | is_indoor        |
                                in every table                               +-----------------+
```

| | א. טבלה אחת | ב. טבלה לכל משנה | ג. על + משנים |
|---|---|---|---|
| טבלאות | 1 | 4 | 5 |
| עמודות ייחודיות | NULL ברוב השורות | כל אחת בטבלה שלה | כל אחת בטבלה שלה |
| `NOT NULL` על עמודה ייחודית | ❌ אי אפשר (חתול לא אילוף) — רק `CHECK` | ✅ | ✅ |
| "כל החיות" | `SELECT` פשוט | `UNION ALL` של 4 | `SELECT` מ‑`animal` |
| מפתח זר מבחוץ ל"חיה" | ✅ | ❌ — לאיזו טבלה? | ✅ ל‑`animal` |
| עמודות משותפות | פעם אחת | **חוזרות** ב‑4 טבלאות | פעם אחת |
| שאילתה על כלב עם כל הפרטים | פשוטה | פשוטה | `JOIN` |

**מתי מה:**
- **א. טבלה אחת** — כשלטיפוסי המשנה **מעט** מאפיינים ייחודיים (1–2). כך עשינו בבסיס הנתונים **המוכן**: `animal` אחת עם `species_id`, ו‑`person` אחת עם `role` (מודול 20, סעיף 8).
- **ב. טבלה לכל משנה** — כשטיפוסי המשנה כמעט לא חולקים כלום, ואף אחד מבחוץ לא מצביע על "כולם".
- **ג. על + משנים** — כשיש **הרבה** מאפיינים ייחודיים **וגם** ישויות אחרות מצביעות על "חיה כללית".

> 🔑 **בפרויקט המקלט נבחרה דרך ג'** (החלטה 3): חמש ישויות (`VACCINATION`, `ADOPTION`, `INTAKE`, `EXPENSE`, `ANIMAL_PLACEMENT`) צריכות להצביע על "חיה" — בלי לדעת אם זה כלב או חתול. **רק `animal` משותפת מאפשרת מפתח זר אחד.**

### 5.1 ⚠️ מה דרך ג' לא אוכפת

</div>

```sql
INSERT INTO dog (animal_id, good_with_kids) VALUES (1, 1);
INSERT INTO cat (animal_id)                 VALUES (1);       -- accepted!
-- Luna is now both a dog AND a cat
```

<div dir="rtl">

כלל ה**בלעדיות** של טיפוסי משנה (מודול 4) — "כל חיה בדיוק טיפוס אחד" — **לא נאכף** על ידי מפתחות זרים לבד. שום דבר גם לא מבטיח שהשורה ב‑`dog` היא של חיה שה‑`species` שלה "Dog". **פתרונות:** עמודת מבחין + מפתח זר מורכב `(animal_id, species_id)` עם `CHECK`, או טריגר, או בדיקה באפליקציה. **כל דרך מיפוי משאירה חוק אחד שצריך לאכוף בנפרד — כתבו אותו ביומן ההחלטות.**

---

## 6. מוסכמות שמות במעבר

| ב‑ERD | בטבלה | דוגמה |
|-------|--------|--------|
| שם ישות ביחיד, אותיות גדולות | שם טבלה ביחיד, `snake_case` | `ADOPTION APPLICATION` ⟵ `adoption_application` |
| מזהה "id" | `<table>_id` | `animal_id` |
| שם היחס ("adopted by") | שם התפקיד במפתח הזר | `adopter_id`, `vet_id`, `brought_by` |
| שמות בעברית בתרשים ללקוח | אנגלית בבסיס הנתונים | "חיה" ⟵ `animal` |

> 💡 **Oracle Academy משתמשת בשמות טבלה ברבים** (`ANIMALS`) ובקיצורים של 3–4 אותיות לכל טבלה (`ANL`) לשמות אילוצים. **כל מוסכמה טובה — אם היא עקבית.** בקורס: ביחיד, כמו בבסיס הנתונים המוכן (מודול 26, סעיף 5).

---

## 7. דוגמה מלאה — חלק מהמקלט

מיפוי של שבע ישויות מהפרויקט, לפי ההחלטות שנרשמו (project/README):

</div>

```sql
PRAGMA foreign_keys = ON;

CREATE TABLE species (                          -- simple entity
  species_id INTEGER PRIMARY KEY,
  name       TEXT NOT NULL,
  CONSTRAINT uq_species_name UNIQUE (name)
) STRICT;

CREATE TABLE animal (                           -- supertype (option C)
  animal_id   INTEGER PRIMARY KEY,
  species_id  INTEGER NOT NULL,                 -- 1:M mandatory
  mother_id   INTEGER,                          -- recursive, optional
  name        TEXT    NOT NULL,
  sex         TEXT    NOT NULL,
  birth_date  TEXT,                             -- optional; NO age column (decision 12)
  chip_number TEXT,                             -- secondary UID, may be NULL (decision 10)
  CONSTRAINT fk_animal_species FOREIGN KEY (species_id) REFERENCES species(species_id),
  CONSTRAINT fk_animal_mother  FOREIGN KEY (mother_id)  REFERENCES animal(animal_id),
  CONSTRAINT uq_animal_chip    UNIQUE (chip_number),
  CONSTRAINT chk_animal_sex    CHECK (sex IN ('M', 'F', 'U'))
) STRICT;

CREATE TABLE dog (                              -- subtype: pk = fk to the supertype
  animal_id        INTEGER PRIMARY KEY,
  is_house_trained INTEGER NOT NULL DEFAULT 0,
  good_with_kids   INTEGER,
  CONSTRAINT fk_dog_animal FOREIGN KEY (animal_id) REFERENCES animal(animal_id)
) STRICT;

CREATE TABLE person (
  person_id  INTEGER PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name  TEXT NOT NULL
) STRICT;

CREATE TABLE phone (                            -- multi-valued attribute -> barred entity
  person_id INTEGER NOT NULL,
  phone_no  TEXT    NOT NULL,
  kind      TEXT    NOT NULL DEFAULT 'mobile',
  CONSTRAINT pk_phone        PRIMARY KEY (person_id, phone_no),
  CONSTRAINT fk_phone_person FOREIGN KEY (person_id) REFERENCES person(person_id)
) STRICT;

CREATE TABLE trait (
  trait_id INTEGER PRIMARY KEY,
  name     TEXT NOT NULL UNIQUE
) STRICT;

CREATE TABLE animal_trait (                     -- resolved M:M
  animal_id INTEGER NOT NULL REFERENCES animal(animal_id),
  trait_id  INTEGER NOT NULL REFERENCES trait(trait_id),
  CONSTRAINT pk_animal_trait PRIMARY KEY (animal_id, trait_id)
) STRICT;
```

<div dir="rtl">

**ובדיקה שהמיפוי עובד:**

</div>

```sql
INSERT INTO species VALUES (1, 'Dog'), (2, 'Cat');
INSERT INTO animal  VALUES (1, 1, NULL, 'Luna', 'F', '2021-03-15', '985100001'),
                           (2, 1, 1,    'Pup',  'M', '2024-01-01', NULL);
INSERT INTO dog (animal_id, good_with_kids) VALUES (1, 1), (2, NULL);

SELECT a.name, s.name AS species, d.is_house_trained, d.good_with_kids, m.name AS mother
FROM   animal a
JOIN   species s ON s.species_id = a.species_id
LEFT   JOIN dog d    ON d.animal_id = a.animal_id
LEFT   JOIN animal m ON m.animal_id = a.mother_id;
```

```text
name  species  is_house_trained  good_with_kids  mother
----  -------  ----------------  --------------  ------
Luna  Dog      0                 1
Pup   Dog      0                                 Luna
```

<div dir="rtl">

---

## 8. מבוא ל‑Application Express (APEX)

**Oracle APEX** הוא כלי של Oracle לבניית אפליקציות על בסיס נתונים — **בדפדפן**, כמעט בלי לכתוב קוד. תכנית הלימודים המקורית בנויה עליו.

| מה APEX נותן | בקורס |
|---------------|--------|
| **SQL Workshop** — חלון להרצת SQL | כמו OneCompiler, אבל Oracle אמיתי |
| **Object Browser** — טבלאות, עמודות ואילוצים בממשק גרפי | כמו מילון הנתונים (מודול 26) |
| **Data Workshop** — ייבוא CSV / Excel לטבלה | טעינת נתונים לפרויקט |
| **App Builder** — טפסים ודוחות על הטבלאות | "האתר" של המקלט — בלי לתכנת |
| **Quick SQL** — כותבים רשימת ישויות בטקסט פשוט, ומקבלים `CREATE TABLE` | ⭐ מיפוי אוטומטי — ראו למטה |

</div>

```text
   Quick SQL input  (plain text, indentation = columns)        Quick SQL output
   ------------------------------------------------            ----------------
   species                                                     create table species (
     name vc50 /nn /unique                                       id    number generated ... primary key,
   animals                                                       name  varchar2(50) not null unique
     species id /fk species                                    );
     name vc50 /nn                                             create table animals (
     birth_date d                                                id          number ... primary key,
                                                                 species_id  number references species,
                                                                 name        varchar2(50) not null,
                                                                 birth_date  date
                                                               );
```

<div dir="rtl">

**איך מתחילים:** [apex.oracle.com](https://apex.oracle.com) ⟵ "Request a Free Workspace" — סביבת Oracle אמיתית, חינם, בדפדפן. (לחלופין: **Oracle Live SQL** להרצת SQL בלבד.)

> 🔑 **כלים כמו Quick SQL (וגם Oracle SQL Developer Data Modeler, ו‑dbdiagram.io) מבצעים מיפוי אוטומטי** — אבל הם מבצעים **בדיוק** את החוקים בסעיפים 3–5, ובוחרים ברירות מחדל בהחלטות שיש בהן בחירה. **מי שמבין את החוקים — יודע מתי הכלי טעה.**

---

## 9. שש טעויות נפוצות

| # | הטעות | מה קורה | התיקון |
|---|-------|----------|---------|
| 1 | **מפתח זר בצד ה"אחד"** | `species` עם עמודת `animal_id` — מין יכול להחזיק חיה אחת בלבד | fk תמיד בצד הרבים |
| 2 | **M:M שלא נפתר** | אין דרך לבנות טבלה | ישות מקשרת (מודול 5) |
| 3 | **רב‑ערכי כעמודה** | `phones = '052…, 04…'` — שובר 1NF | טבלה נפרדת |
| 4 | **שמירת מאפיין נגזר** | עמודת `age` שמזדקנת | מחשבים בשאילתה |
| 5 | **קו מקווקו ⟵ `NOT NULL`** | אי אפשר להכניס הוצאה כללית | אופציונלי = מותר NULL |
| 6 | **טיפוסי משנה בלי לרשום מה לא נאכף** | חיה שהיא גם כלב וגם חתול | יומן החלטות + אכיפה (טריגר / אפליקציה) |

---

## 10. סיכום המודול

<div align="center">

### 🧠 שש נקודות

</div>

1. **קונספטואלי ⟵ לוגי ⟵ פיזי.** הלקוח מבין ERD; בסיס הנתונים מבין טבלאות; המיפוי מחבר.
2. **ישות ⟵ טבלה · מאפיין ⟵ עמודה · `#` ⟵ pk · מזהה משני ⟵ uk · `*` ⟵ `NOT NULL`.**
3. **יחס 1:M ⟵ fk בצד הרבים** (`NOT NULL` אם חובה). **M:M** — רק אחרי שנפתר לישות מקשרת.
4. **מזהה (bar) ⟵ fk בתוך ה‑pk · 1:1 ⟵ fk + `UNIQUE` · רקורסיבי ⟵ fk לאותה טבלה · קשת ⟵ fk‑ים + `CHECK`.**
5. **טיפוסי משנה — שלוש דרכים:** טבלה אחת (מעט הבדלים), טבלה לכל משנה (אין מצביעים מבחוץ), על + משנים (המקלט). לכל אחת — חוק שלא נאכף לבד.
6. **APEX / Quick SQL** מבצעים מיפוי אוטומטי — לפי אותם חוקים.

<div align="center">

---

*"ה‑ERD הוא מה שהלקוח אמר.*
*הטבלאות הן מה שהמחשב יזכור."*

---

</div>

## 📎 המשך

| | |
|---|---|
| ❓ | [שאלות ותשובות](questions.md) |
| ✏️ | [תרגילים](exercises.md) |
| ✅ | [פתרונות](solutions.md) |
| ⬅️ | [מודול 11 — מודלים גנריים](../module-11-generic-models/) |
| 🧭 | ⭐ ביחידה 8 — יחד עם [מודול 26 — DDL](../module-26-sql-ddl/) |
| ➡️ | [מודול 13 — SQL I: הכרות, עבודת צוות וניהול הפרויקט](../module-13-sql-1/) |
| 🏠 | [חזרה לדף הקורס](../../) |

</div>
