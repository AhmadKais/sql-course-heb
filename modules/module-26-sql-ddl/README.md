<div dir="rtl">

# מודול 26 — SQL: שפת הגדרת אובייקטים (DDL)

> **פרק 26 בתכנית הלימודים** · 3 שעות עיוני + 3 שעות מעשי
> **נושאים:** יצירת טבלאות · שימוש ב‑Datatypes · התאמות בטבלה

> 🧭 **במסלול המשולב:** יחידה 8, לצד [מודול 12 — מעבר לבסיס הנתונים](../module-12-mapping/). ⭐ **מכאן — בסיס נתונים משלכם.** מודול 12 מסביר **איך** הופכים ERD לטבלאות; המודול הזה — **איך כותבים** את זה.

---

## 🎯 מה תדעו בסוף המודול

- [ ] לכתוב `CREATE TABLE` עם עמודות, טיפוסים, מפתח ראשי וברירות מחדל
- [ ] לבחור **טיפוס נתונים** נכון לכל עמודה — ב‑SQLite וב‑Oracle
- [ ] להסביר את מלכודת ה‑"type affinity" של SQLite — ואיך `STRICT` פותר אותה
- [ ] לשנות טבלה קיימת עם `ALTER TABLE`: להוסיף, לשנות שם, למחוק עמודה
- [ ] להבדיל בין `DROP`, `TRUNCATE` ו‑`DELETE`
- [ ] לשאול את **מילון הנתונים** — אילו טבלאות ועמודות קיימות
- [ ] לבנות את **הטבלאות של הפרויקט שלכם** מה‑ERD

---

## 🗺️ מפת המודול

| # | הסעיף |
|---|--------|
| 1 | [DDL — משנים את המבנה, לא את הנתונים](#1-ddl--משנים-את-המבנה-לא-את-הנתונים) |
| 2 | [CREATE TABLE](#2-create-table) |
| 3 | [טיפוסי נתונים](#3-טיפוסי-נתונים) |
| 4 | [⚠️ SQLite סלחני מדי — ו‑STRICT](#4-️-sqlite-סלחני-מדי--וstrict) |
| 5 | [מוסכמות שמות](#5-מוסכמות-שמות) |
| 6 | [ALTER TABLE — שינוי טבלה קיימת](#6-alter-table--שינוי-טבלה-קיימת) |
| 7 | [DROP, TRUNCATE, DELETE](#7-drop-truncate-delete) |
| 8 | [מילון הנתונים — הטבלאות על עצמן](#8-מילון-הנתונים--הטבלאות-על-עצמן) |
| 9 | [דוגמה מלאה — מ‑ERD לטבלאות](#9-דוגמה-מלאה--מerd-לטבלאות) |
| 10 | [חמש טעויות נפוצות](#10-חמש-טעויות-נפוצות) |
| 11 | [סיכום המודול](#11-סיכום-המודול) |

---

## 1. DDL — משנים את המבנה, לא את הנתונים

</div>

```text
   DML (module 25)                       DDL (this module)
   ---------------                       -----------------
   INSERT / UPDATE / DELETE              CREATE / ALTER / DROP
   changes ROWS inside a table           changes the TABLE itself
   "add a dog"                           "add a column for microchip date"
   happens every day                     happens rarely -- and carefully
```

<div dir="rtl">

> 🔑 **DDL הוא תרגום של ה‑ERD לקוד.** כל ישות ⟵ `CREATE TABLE`. כל מאפיין ⟵ עמודה. כל מזהה ייחודי ⟵ `PRIMARY KEY`. כל יחס ⟵ `REFERENCES`. מה שציירתם במודולים 2–7 — הופך כאן לטבלאות שאפשר להכניס אליהן נתונים.

---

## 2. CREATE TABLE

</div>

```sql
CREATE TABLE volunteer_shift (
  shift_id    INTEGER PRIMARY KEY,               -- unique identifier
  person_id   INTEGER NOT NULL,                  -- who (a foreign key -- module 27)
  shift_date  TEXT    NOT NULL,                  -- when
  start_hour  INTEGER NOT NULL,
  hours       REAL    DEFAULT 4,                 -- if not given: 4
  notes       TEXT                               -- optional: may be NULL
);

INSERT INTO volunteer_shift (person_id, shift_date, start_hour) VALUES (1, '2026-09-21', 8);
SELECT * FROM volunteer_shift;
```

```text
shift_id  person_id  shift_date  start_hour  hours  notes
--------  ---------  ----------  ----------  -----  -----
1         1          2026-09-21  8           4.0
```

<div dir="rtl">

**המבנה של כל עמודה:**

</div>

```text
   column_name   DATATYPE   [constraints]          [DEFAULT value]
   hours         REAL                              DEFAULT 4
   person_id     INTEGER    NOT NULL
   shift_id      INTEGER    PRIMARY KEY
```

<div dir="rtl">

| החלק | חובה? | תפקיד |
|------|--------|--------|
| שם | ✅ | ייחודי בתוך הטבלה |
| טיפוס | ✅ (ב‑Oracle) | איזה סוג ערכים מותר |
| `NOT NULL` | — | ערך חובה. **בלי זה — העמודה אופציונלית** |
| `PRIMARY KEY` | אחת לטבלה | מזהה ייחודי לכל שורה |
| `DEFAULT` | — | ערך כשלא נמסר ערך |

> 💡 **כלל אצבע: כל עמודה `NOT NULL`, אלא אם יש סיבה עסקית שהיא תהיה ריקה.** מודול 7 אמר: אופציונלי (O) או חובה (\*). ב‑SQL — חובה = `NOT NULL`.

### 2.1 `IF NOT EXISTS` ו‑`CREATE TABLE … AS`

</div>

```sql
CREATE TABLE IF NOT EXISTS volunteer_shift (...);    -- no error if it already exists

CREATE TABLE dog AS                                   -- structure + data from a query
SELECT * FROM animal WHERE species_id = 1;
```

<div dir="rtl">

> ⚠️ **`CREATE TABLE … AS SELECT` מעתיק עמודות ונתונים — אבל לא אילוצים** (מפתח ראשי, `CHECK`, מפתחות זרים). טוב לגיבוי ולניסויים; לא לטבלה "אמיתית".

---

## 3. טיפוסי נתונים

הטיפוס אומר **מה** מותר לשמור בעמודה — ולכן גם אילו פעולות הגיוניות עליה (חיבור למספרים, `UPPER` לטקסט, הפרש לתאריכים).

</div>

```text
+-------------------+----------------------+------------------------------+------------------------+
| KIND              | SQLite               | Oracle                       | example in the shelter |
+-------------------+----------------------+------------------------------+------------------------+
| whole number      | INTEGER              | NUMBER(10)  / INTEGER        | animal_id, start_hour  |
| decimal           | REAL                 | NUMBER(7,2)                  | weight_kg, amount      |
|                   |                      |   7 digits, 2 after the dot  |                        |
| short text        | TEXT                 | VARCHAR2(50)                 | name, city             |
|                   |                      |   up to 50 characters        |                        |
| fixed-size code   | TEXT                 | CHAR(1)                      | sex: 'M' / 'F' / 'U'   |
| long text         | TEXT                 | CLOB                         | a vet's full report    |
| date              | TEXT  'YYYY-MM-DD'   | DATE  (includes time!)       | birth_date             |
| date + time       | TEXT  'YYYY-MM-DD    | TIMESTAMP                    | intake time            |
|                   |        HH:MM:SS'     |                              |                        |
| true / false      | INTEGER  0 / 1       | NUMBER(1)  (BOOLEAN in 23c)  | is_neutered            |
| binary (file)     | BLOB                 | BLOB                         | a photo                |
+-------------------+----------------------+------------------------------+------------------------+
```

<div dir="rtl">

### 3.1 איך בוחרים

| השאלה | אם כן | דוגמה |
|-------|--------|--------|
| עושים עליו חשבון? | מספר | `weight_kg`, `amount` |
| זה "מספר" שלא מחשבים איתו? | **טקסט** | טלפון, מיקוד, מספר שבב, ת"ז |
| מחשבים הפרשים / ממיינים לפי זמן? | תאריך | `birth_date` |
| כסף? | עשרוני **מדויק** (`NUMBER(10,2)`) | `fee_paid` |

> ⚠️ **טלפון הוא טקסט, לא מספר.** `052-1111111` כמספר מאבד את ה‑0 שבהתחלה ואת המקף, ו"052" + 1 אינו טלפון. **שאלו: האם יש היגיון לחבר שני ערכים כאלה?** אם לא — טקסט. אותו דבר למספר שבב, מיקוד ות"ז.

> 💡 **`VARCHAR2(50)` — למה 50?** Oracle דורש לקבוע אורך מקסימלי. בחרו לפי המציאות: שם — 50, עיר — 40, תיאור — 200. ארוך מדי — לא נורא; קצר מדי — שגיאה כשמישהו מגיע עם שם ארוך.

---

## 4. ⚠️ SQLite סלחני מדי — ו‑STRICT

ב‑Oracle, ניסיון לשמור טקסט בעמודת מספר — **שגיאה**. ב‑SQLite?

</div>

```sql
CREATE TABLE t (n INTEGER, x TEXT);
INSERT INTO t VALUES ('abc', 42), ('12', 7);
SELECT n, typeof(n), x, typeof(x) FROM t;
```

```text
n    typeof(n)  x   typeof(x)
---  ---------  --  ---------
abc  text       42  text          <- 'abc' was stored in an INTEGER column!
12   integer    7   text          <- '12' was quietly converted to 12
```

<div dir="rtl">

SQLite משתמש ב‑**type affinity**: הטיפוס הוא **המלצה**. אם אפשר להמיר — ממיר; אם לא — שומר כמו שזה. **`'abc'` נשמר בעמודת `INTEGER`.** כל `SUM(n)` אחרי זה יחזיר תוצאה שגויה.

**הפתרון — `STRICT`** (SQLite 3.37+):

</div>

```sql
CREATE TABLE s (n INTEGER, x TEXT) STRICT;
INSERT INTO s VALUES ('abc', 'ok');
-- Error: cannot store TEXT value in INTEGER column s.n
```

<div dir="rtl">

> 🔑 **בפרויקט שלכם — הוסיפו `STRICT` לכל טבלה.** כך SQLite יתנהג כמו בסיס נתונים "רציני", והשגיאות יופיעו מיד ולא בדוח. (ב‑`STRICT` מותרים רק `INTEGER`, `REAL`, `TEXT`, `BLOB`, `ANY`.)

---

## 5. מוסכמות שמות

שמות טובים הם חצי מהתיעוד. המוסכמות בקורס (ובבסיס הנתונים המוכן):

| הכלל | ✅ | ❌ |
|------|-----|-----|
| אותיות קטנות, קו תחתון בין מילים (snake_case) | `birth_date` | `BirthDate`, `birth date` |
| טבלה — שם עצם ביחיד | `animal` | `animals`, `tbl_animal` |
| מפתח ראשי — `<table>_id` | `animal_id` | `id`, `num` |
| מפתח זר — אותו שם כמו המפתח שהוא מצביע עליו | `animal.species_id` | `animal.type` |
| מפתח זר בתפקיד — שם התפקיד | `adopter_id`, `vet_id` | `person_id2` |
| בלי מילים שמורות | `adoption_date` | `date`, `order`, `user` |
| יחידות בשם, כשיש | `weight_kg`, `interval_months` | `weight` (ק"ג? פאונד?) |

---

## 6. ALTER TABLE — שינוי טבלה קיימת

המציאות משתנה, והטבלה צריכה להשתנות איתה — **בלי** למחוק את הנתונים שכבר בה.

</div>

```sql
-- add a column (existing rows get the DEFAULT, or NULL)
ALTER TABLE volunteer_shift ADD COLUMN task TEXT DEFAULT 'kennels';

-- rename a column
ALTER TABLE volunteer_shift RENAME COLUMN notes TO remarks;

-- drop a column (SQLite 3.35+)
ALTER TABLE volunteer_shift DROP COLUMN remarks;

-- rename the table
ALTER TABLE volunteer_shift RENAME TO shift;
```

<div dir="rtl">

| הפעולה | SQLite | Oracle |
|--------|--------|--------|
| הוספת עמודה | `ADD COLUMN c TYPE` | `ADD (c TYPE)` |
| שינוי שם עמודה | `RENAME COLUMN a TO b` | אותו דבר |
| מחיקת עמודה | `DROP COLUMN c` | אותו דבר |
| **שינוי טיפוס / `NOT NULL`** | ❌ אי אפשר | `MODIFY (c VARCHAR2(100) NOT NULL)` |
| שינוי שם טבלה | `RENAME TO new` | `RENAME old TO new` |

> ⚠️ **ב‑SQLite אי אפשר לשנות טיפוס עמודה או להוסיף לה `NOT NULL`** אחרי שנוצרה. הדרך: ליצור טבלה חדשה במבנה הנכון, להעתיק (`INSERT … SELECT`), למחוק את הישנה ולשנות שם. **לכן כדאי לחשוב טוב לפני `CREATE`.**

> 💡 **הוספת עמודה `NOT NULL` לטבלה עם נתונים** — חייבת `DEFAULT`, אחרת מה ייכנס בשורות הקיימות? `ADD COLUMN is_neutered INTEGER NOT NULL DEFAULT 0`.

---

## 7. DROP, TRUNCATE, DELETE

</div>

```text
   DELETE FROM animal;        rows gone, table stays.     DML -- can be rolled back.
                              WHERE allowed.               slow on big tables (row by row).

   TRUNCATE TABLE animal;     rows gone, table stays.     DDL (Oracle) -- NO rollback.
                              no WHERE. very fast.         SQLite has none: use DELETE.

   DROP TABLE animal;         rows AND table gone.        DDL -- NO rollback.
                              structure, constraints,      the table no longer exists.
                              everything.
```

<div dir="rtl">

> ⚠️ **ב‑Oracle, כל פקודת DDL מבצעת `COMMIT` אוטומטי** (מודול 32). כלומר: `DELETE` אפשר לבטל עם `ROLLBACK`; `TRUNCATE` ו‑`DROP` — **לא**. אין "פח מיחזור" (חוץ מ‑`FLASHBACK` של Oracle, שהמנהל צריך להפעיל).

</div>

```sql
DROP TABLE IF EXISTS shift;        -- IF EXISTS: no error if it's already gone
```

<div dir="rtl">

> 💡 **בסקריפט התקנה**, כמו `shelter.sql`, מתחילים ב‑`DROP TABLE IF EXISTS` לכל טבלה — **בסדר הפוך** לסדר היצירה (קודם הילדים, אחר כך ההורים), כדי שמפתחות זרים לא יחסמו. פתחו את `shelter.sql` ותראו: `expense` נמחקת ראשונה, `species` אחרונה.

---

## 8. מילון הנתונים — הטבלאות על עצמן

בסיס הנתונים שומר **מידע על עצמו** — אילו טבלאות קיימות, אילו עמודות יש בכל אחת. זה נקרא **מילון נתונים** (data dictionary), ושואלים אותו ב‑SQL רגיל:

</div>

```sql
-- SQLite: all tables
SELECT name FROM sqlite_master WHERE type = 'table';

-- SQLite: the columns of one table
PRAGMA table_info(shift);
```

```text
cid  name        type     notnull  dflt_value  pk
---  ----------  -------  -------  ----------  --
0    shift_id    INTEGER  0                    1
1    person_id   INTEGER  1                    0
2    shift_date  TEXT     1                    0
3    start_hour  INTEGER  1                    0
4    hours       REAL     0        4           0
5    task        TEXT     0        'kennels'   0
```

```sql
-- Oracle
SELECT table_name FROM user_tables;
SELECT column_name, data_type, nullable FROM user_tab_columns WHERE table_name = 'ANIMAL';
DESCRIBE animal;
```

<div dir="rtl">

> 💡 **ב‑Oracle שמות טבלאות נשמרים באותיות גדולות** — לכן `'ANIMAL'` ולא `'animal'` בשאילתה על המילון.

---

## 9. דוגמה מלאה — מ‑ERD לטבלאות

רותי רוצה לנהל **טיולים** עם הכלבים: מתנדב לוקח כלב לטיול, בתאריך מסוים, לכמה דקות, ויכול לרשום הערה. מה‑ERD (מודול 12):

</div>

```text
   PERSON  1 ----< WALK >---- 1  ANIMAL
   (volunteer)     # walk_id
                   * walk_date
                   * minutes
                   o notes

   #  identifier      *  mandatory      o  optional
```

```sql
CREATE TABLE walk (
  walk_id    INTEGER PRIMARY KEY,                               -- #  identifier
  animal_id  INTEGER NOT NULL REFERENCES animal(animal_id),     -- relationship, mandatory
  person_id  INTEGER NOT NULL REFERENCES person(person_id),     -- relationship, mandatory
  walk_date  TEXT    NOT NULL,                                  -- *  mandatory
  minutes    INTEGER NOT NULL DEFAULT 30,                       -- *  mandatory, usual value
  notes      TEXT                                               -- o  optional
) STRICT;

INSERT INTO walk (animal_id, person_id, walk_date)            VALUES (3, 2, '2026-09-20');
INSERT INTO walk (animal_id, person_id, walk_date, minutes, notes)
VALUES (13, 3, '2026-09-20', 45, 'pulls on the leash');

SELECT a.name, p.first_name AS volunteer, w.walk_date, w.minutes, w.notes
FROM   walk w
JOIN   animal a ON a.animal_id = w.animal_id
JOIN   person p ON p.person_id = w.person_id;
```

```text
name   volunteer  walk_date   minutes  notes
-----  ---------  ----------  -------  ------------------
Rocky  Noa        2026-09-20  30
Rex    Amir       2026-09-20  45       pulls on the leash
```

<div dir="rtl">

**כל שורה בטבלה עונה על שאלה מה‑ERD:**

| ב‑ERD | ב‑DDL |
|-------|--------|
| `#` מזהה | `PRIMARY KEY` |
| `*` חובה | `NOT NULL` |
| `o` אופציונלי | בלי `NOT NULL` |
| קו לישות אחרת | `REFERENCES other(id)` |
| ערך שכיח | `DEFAULT` |

> 🔑 **`REFERENCES` הוא כבר אילוץ — מפתח זר.** במודול 27 נכיר אותו לעומק, יחד עם `CHECK` ו‑`UNIQUE`. כאן — רק כדי שהטבלה תהיה שלמה.

---

## 10. חמש טעויות נפוצות

| # | הטעות | מה קורה | התיקון |
|---|-------|----------|---------|
| 1 | **טלפון / מיקוד כמספר** | אפסים מובילים נעלמים | `TEXT` / `VARCHAR2` |
| 2 | **שוכחים `NOT NULL`** | עמודות חובה נשארות ריקות | `NOT NULL` כברירת מחדל שלכם |
| 3 | **בלי `STRICT` ב‑SQLite** | טקסט בעמודת מספר | `) STRICT;` |
| 4 | **שם עמודה שהוא מילה שמורה** (`date`, `order`) | שגיאות תחביר מוזרות | `walk_date`, `order_no` |
| 5 | **`DROP` כשרצו `DELETE`** | הטבלה עצמה נעלמה | `DELETE` מוחק שורות; `DROP` מוחק טבלה |

---

## 11. סיכום המודול

<div align="center">

### 🧠 שש נקודות

</div>

1. **DDL משנה מבנה:** `CREATE`, `ALTER`, `DROP`. **DML משנה שורות.**
2. **`CREATE TABLE`:** שם, טיפוס, `NOT NULL`, `PRIMARY KEY`, `DEFAULT` לכל עמודה — תרגום ישיר של ה‑ERD.
3. **טיפוס לפי מה עושים עם הערך:** חשבון ⟵ מספר; "מספר" בלי חשבון ⟵ טקסט; זמן ⟵ תאריך; כסף ⟵ עשרוני מדויק.
4. **SQLite סלחני** — הטיפוס הוא המלצה. **`STRICT`** הופך אותו לחוק.
5. **`ALTER TABLE`:** `ADD`, `RENAME`, `DROP COLUMN`. ב‑SQLite אין שינוי טיפוס — חושבים לפני `CREATE`.
6. **`DELETE` ≠ `TRUNCATE` ≠ `DROP`.** ב‑Oracle, DDL עושה `COMMIT` אוטומטי — אין חזרה.

<div align="center">

---

*"ה‑ERD הוא התוכנית.*
*CREATE TABLE הוא הבטון."*

---

</div>

## 📎 המשך

| | |
|---|---|
| ❓ | [שאלות ותשובות](questions.md) |
| ✏️ | [תרגילים](exercises.md) |
| ✅ | [פתרונות](solutions.md) |
| ⬅️ | [מודול 25 — SQL: מניפולציות לנתונים](../module-25-sql-dml/) |
| ➡️ | [מודול 27 — SQL: אילוצים](../module-27-sql-constraints/) |
| 🏠 | [חזרה לדף הקורס](../../) |

</div>
