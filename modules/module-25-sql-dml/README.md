<div dir="rtl">

# מודול 25 — SQL: מניפולציות לנתונים (DML)

> **פרק 25 בתכנית הלימודים** · 3 שעות עיוני + 3 שעות מעשי
> **נושאים:** יצירת רשומות חדשות · עדכון ומחיקת רשומות קיימות · DEFAULT Values, MERGE, and Multi‑Table Inserts

> 🧭 **במסלול המשולב:** יחידה 9, לצד [מודול 8 — תפקיד היועץ](../module-08-consultant/) ו[מודול 9 — פרויקט I](../module-09-project-1/). ביחידה 8 בניתם את הטבלאות שלכם (מודול 26) — **עכשיו ממלאים אותן.**

---

## 🎯 מה תדעו בסוף המודול

- [ ] להוסיף שורות עם `INSERT` — שורה אחת, כמה שורות, ומתוך `SELECT`
- [ ] לעדכן שורות עם `UPDATE` — ולהבין למה `WHERE` הוא שאלה של חיים ומוות
- [ ] למחוק שורות עם `DELETE` — ולהבין מה מפתח זר עושה למחיקה
- [ ] להשתמש בערכי **ברירת מחדל** (`DEFAULT`)
- [ ] לכתוב "הוסף או עדכן" — `MERGE` (Oracle) ו‑`ON CONFLICT` (SQLite)
- [ ] להכיר **הכנסה לכמה טבלאות** (`INSERT ALL` של Oracle)
- [ ] לעבוד בבטחה: **`SELECT` לפני כל `UPDATE` ו‑`DELETE`**

---

## 🗺️ מפת המודול

| # | הסעיף |
|---|--------|
| 1 | [DML — שלוש הפעולות שמשנות נתונים](#1-dml--שלוש-הפעולות-שמשנות-נתונים) |
| 2 | [⚠️ לפני שמתחילים — הפעלת מפתחות זרים](#2-️-לפני-שמתחילים--הפעלת-מפתחות-זרים) |
| 3 | [INSERT — שורה חדשה](#3-insert--שורה-חדשה) |
| 4 | [INSERT … SELECT — שורות מתוך שאילתה](#4-insert--select--שורות-מתוך-שאילתה) |
| 5 | [UPDATE — שינוי שורות קיימות](#5-update--שינוי-שורות-קיימות) |
| 6 | [DELETE — מחיקה](#6-delete--מחיקה) |
| 7 | [DEFAULT — ערכי ברירת מחדל](#7-default--ערכי-ברירת-מחדל) |
| 8 | [MERGE — הוסף או עדכן](#8-merge--הוסף-או-עדכן) |
| 9 | [Multi-table insert](#9-multi-table-insert) |
| 10 | [נוהל העבודה הבטוח](#10-נוהל-העבודה-הבטוח) |
| 11 | [שש טעויות נפוצות](#11-שש-טעויות-נפוצות) |
| 12 | [סיכום המודול](#12-סיכום-המודול) |

---

## 1. DML — שלוש הפעולות שמשנות נתונים

עד עכשיו כל מה שכתבנו היה `SELECT` — **קריאה**. שום שאילתה לא שינתה את בסיס הנתונים. מהמודול הזה — **כותבים**.

</div>

```text
   SQL is divided into "sub-languages":

   DQL  Data Query Language          SELECT                    modules 16-24  (read)
   DML  Data Manipulation Language   INSERT  UPDATE  DELETE    THIS module    (change rows)
        (MERGE)
   DDL  Data Definition Language     CREATE  ALTER   DROP      module 26      (change tables)
   DCL  Data Control Language        GRANT   REVOKE            module 30      (permissions)
   TCL  Transaction Control          COMMIT  ROLLBACK          module 32      (undo / confirm)
```

| הפקודה | מה היא עושה | הסכנה |
|---------|-------------|--------|
| `INSERT` | מוסיפה שורות חדשות | נמוכה — אילוצים חוסמים זבל |
| `UPDATE` | משנה ערכים בשורות קיימות | **גבוהה** — בלי `WHERE` משנה הכול |
| `DELETE` | מוחקת שורות | **גבוהה מאוד** — בלי `WHERE` מוחק הכול |

<div dir="rtl">

> 💡 **ב‑Programiz זה בטוח:** בכל ריצה מדביקים את `shelter.sql` מחדש, אז כל שינוי נמחק. **בעבודה אמיתית אין "הדבקה מחדש"** — לכן הנוהל בסעיף 10 הוא החלק החשוב ביותר במודול.

---

## 2. ⚠️ לפני שמתחילים — הפעלת מפתחות זרים

ב‑SQLite, אילוצי **מפתח זר לא נבדקים** כברירת מחדל! נסו:

</div>

```sql
-- species 9 does not exist -- but SQLite accepts it
INSERT INTO animal (name, species_id, sex, status) VALUES ('Bad', 9, 'M', 'available');
```

<div dir="rtl">

השורה נכנסת — חיה ממין שלא קיים. **הפתרון: שורה אחת בתחילת כל סשן:**

</div>

```sql
PRAGMA foreign_keys = ON;

INSERT INTO animal (name, species_id, sex, status) VALUES ('Bad', 9, 'M', 'available');
-- Error: FOREIGN KEY constraint failed
```

<div dir="rtl">

> 🔑 **בכל התרגילים במודול הזה (ובמודולים 26–27): הדביקו את `shelter.sql`, ומיד אחריו `PRAGMA foreign_keys = ON;`.** ב‑Oracle, PostgreSQL ו‑SQL Server מפתחות זרים נבדקים תמיד — זו מוזרות של SQLite בלבד (מסיבות של תאימות לאחור).

---

## 3. INSERT — שורה חדשה

### 3.1 עם רשימת עמודות — הדרך הנכונה

</div>

```sql
INSERT INTO animal (animal_id, name, species_id, breed, sex, birth_date, weight_kg, chip_number, status)
VALUES             (21,        'Milo', 2,        'Tabby', 'M', '2025-04-01', 3.6,     NULL,        'quarantine');

SELECT * FROM animal WHERE animal_id = 21;
```

```text
animal_id  name  species_id  breed  sex  birth_date  weight_kg  chip_number  status
---------  ----  ----------  -----  ---  ----------  ---------  -----------  ----------
21         Milo  2           Tabby  M    2025-04-01  3.6                     quarantine
```

<div dir="rtl">

**הערכים מוצבים לפי הסדר של רשימת העמודות.** עמודה ראשונה ⟵ ערך ראשון. טקסט ותאריכים בגרש בודד; מספרים בלי; NULL בלי גרשיים.

### 3.2 בלי חלק מהעמודות

עמודה שלא מופיעה ברשימה מקבלת את **ברירת המחדל** שלה — ואם אין, **NULL**:

</div>

```sql
INSERT INTO animal (name, species_id, sex, status)
VALUES ('Pip', 4, 'U', 'available');

SELECT animal_id, name, breed, birth_date, weight_kg FROM animal WHERE name = 'Pip';
```

```text
animal_id  name  breed  birth_date  weight_kg
---------  ----  -----  ----------  ---------
22         Pip                                    <- id generated, the rest NULL
```

<div dir="rtl">

**`animal_id` = 22 — מאיפה?** ב‑SQLite, עמודת `INTEGER PRIMARY KEY` שלא קיבלה ערך מקבלת אוטומטית **המקסימום + 1**. ב‑Oracle עושים את זה עם **Sequence** או `IDENTITY` — מודול 29.

### 3.3 בלי רשימת עמודות — ולמה לא

</div>

```sql
INSERT INTO species VALUES (5, 'Hamster', 80);     -- works... today
```

<div dir="rtl">

זה עובד רק אם נותנים ערך **לכל** עמודה, **בסדר המדויק** של הטבלה. מחר מישהו יוסיף עמודה ל‑`species` — וכל ה‑`INSERT`‑ים האלה ישברו. **בקוד אמיתי — תמיד רשימת עמודות.** (`shelter.sql` כותב בלי, כי הוא קובץ טעינה חד‑פעמי.)

### 3.4 כמה שורות בבת אחת

</div>

```sql
INSERT INTO vaccine_type (vaccine_type_id, name, species_id, interval_months)
VALUES (6, 'Psittacosis test', 4, 12),
       (7, 'Leptospirosis',    1, 12);
```

<div dir="rtl">

### 3.5 האילוצים שומרים על הנתונים

</div>

```text
   INSERT INTO animal (name, species_id, sex) VALUES ('Ghost', 1, 'M');
   --> NOT NULL constraint failed: animal.status

   INSERT INTO animal (name, species_id, sex, status) VALUES ('Twin', 1, 'X', 'available');
   --> CHECK constraint failed: sex IN ('M','F','U')

   INSERT INTO animal (animal_id, name, species_id, sex, status) VALUES (1, 'Dup', 1, 'M', 'available');
   --> UNIQUE constraint failed: animal.animal_id
```

<div dir="rtl">

> 🔑 **כל שגיאה כאן היא חוק עסקי ממודול 7 שעובד.** `NOT NULL` = "חובה". `CHECK` = "רק ערכים מותרים". `PRIMARY KEY` = "אין כפילויות". **בלי האילוצים, כל שלוש השורות היו נכנסות** — ומישהו היה מגלה את זה בדוח, חודשים אחר כך. מודול 27 מראה איך מגדירים אותם.

---

## 4. INSERT … SELECT — שורות מתוך שאילתה

במקום `VALUES`, אפשר לתת **שאילתה** — וכל השורות שהיא מחזירה מוכנסות:

</div>

```sql
-- archive the 2023 adoptions into a new table
CREATE TABLE adoption_archive AS SELECT * FROM adoption WHERE 0;   -- empty copy of the structure

INSERT INTO adoption_archive
SELECT * FROM adoption WHERE adoption_date < '2024-01-01';

SELECT COUNT(*) FROM adoption_archive;          -- 2
```

<div dir="rtl">

> 💡 **`WHERE 0`** — תנאי שתמיד false. `CREATE TABLE … AS SELECT … WHERE 0` מעתיק את **מבנה** הטבלה בלי אף שורה. ב‑Oracle: `WHERE 1 = 0`.

שימושים נפוצים: ארכוב, העתקה לטבלת גיבוי לפני שינוי מסוכן, טעינת נתונים מטבלה זמנית.

---

## 5. UPDATE — שינוי שורות קיימות

</div>

```sql
UPDATE table
SET    column1 = value1, column2 = value2
WHERE  condition;            -- WHICH rows. Without it: ALL rows.
```

```sql
-- Rocky was weighed again
UPDATE animal SET weight_kg = 32.5 WHERE name = 'Rocky';
```

<div dir="rtl">

### 5.1 ערך חדש מחושב מהישן

</div>

```sql
-- all adoption fees go up 10%
UPDATE species SET adoption_fee = adoption_fee * 1.10;
SELECT * FROM species;
```

```text
species_id  name    adoption_fee
----------  ------  ------------
1           Dog     440.0
2           Cat     275.0
3           Rabbit  110.0
4           Parrot  165.0
```

<div dir="rtl">

**כאן בלי `WHERE` — בכוונה.** רוצים לשנות את **כל** המחירים. אבל זה היוצא מן הכלל.

> 🎬 **מה זה עשה להיסטוריה?** האימוצים הישנים שמרו את `fee_paid` — הסכום **ששולם בפועל**. לכן העלאת המחיר לא שינתה אותם. **זו בדיוק הסיבה שמודול 10 אמר לשמור את המחיר "הקפוא" בטבלת האימוץ** ולא לחשב אותו מ‑`species`. אילו היינו מחשבים — ההכנסות של 2023 היו "גדלות" ב‑10% ברגע זה.

### 5.2 ⚠️ UPDATE בלי WHERE

</div>

```text
   UPDATE animal SET status = 'adopted';          -- intended: one animal

   -> 20 rows changed. Every animal in the shelter is now "adopted".
      The website shows: "No animals available".
```

<div dir="rtl">

### 5.3 כמה שורות השתנו?

אחרי `UPDATE` או `DELETE` — תמיד לבדוק:

</div>

```sql
UPDATE animal SET status = 'adopted' WHERE animal_id = 999;
SELECT changes();          -- 0  -> no such animal. A typo? Check before moving on.
```

<div dir="rtl">

ב‑SQLite: `changes()`. בכלים אחרים זה מוצג אוטומטית ("1 row updated"). **0 כשציפיתם ל‑1 = טעות בתנאי. 20 כשציפיתם ל‑1 = אסון.**

### 5.4 UPDATE עם תת‑שאילתה

</div>

```sql
-- every animal whose current adoption was not returned must be 'adopted'
UPDATE animal
SET    status = 'adopted'
WHERE  animal_id IN (SELECT animal_id FROM adoption WHERE returned_date IS NULL)
  AND  status <> 'adopted';

SELECT changes();          -- 0: the data is already consistent
```

<div dir="rtl">

> 💡 **0 כאן הוא חדשות טובות** — השאילתה היא בעצם **בדיקת עקביות**: "האם יש חיה שאומצה אבל הסטטוס שלה לא מעודכן?". כדאי להריץ אותה כ‑`SELECT` קודם (סעיף 10).

---

## 6. DELETE — מחיקה

</div>

```sql
DELETE FROM expense WHERE expense_id = 16;
SELECT changes();                   -- 1
SELECT COUNT(*) FROM expense;       -- 21
```

<div dir="rtl">

### 6.1 מחיקה ומפתחות זרים

</div>

```sql
PRAGMA foreign_keys = ON;
DELETE FROM animal WHERE animal_id = 3;
-- Error: FOREIGN KEY constraint failed
```

<div dir="rtl">

ל‑Rocky יש שורות ב‑`intake`, `vaccination` ו‑`expense` שמצביעות עליו. מחיקה שלו תשאיר אותן **יתומות** — חיסון של חיה שלא קיימת. המפתח הזר **חוסם**. כדי למחוק באמת, מוחקים קודם את הילדים:

</div>

```sql
DELETE FROM vaccination WHERE animal_id = 19;
DELETE FROM intake      WHERE animal_id = 19;
DELETE FROM animal      WHERE animal_id = 19;     -- now it works
```

<div dir="rtl">

> 💡 **`ON DELETE CASCADE`** (מודול 27) אומר לבסיס הנתונים למחוק את הילדים אוטומטית. נוח — ומסוכן: מחיקה של מין אחד יכולה למחוק מאות חיות, אלפי חיסונים. **לרוב עדיף שהמחיקה תיחסם.**

### 6.2 האם בכלל למחוק?

**ברוב המערכות האמיתיות — כמעט לא מוחקים.** כשחיה מתה, לא מוחקים אותה — מעדכנים `status = 'deceased'` (כמו Daisy). כשמאמץ עוזב — מסמנים. למה?
- **היסטוריה:** דוח 2024 צריך להציג את Daisy, גם אם היא כבר לא איתנו.
- **ביקורת:** "מי מחק את זה ומתי?" — שאלה שאין לה תשובה אחרי `DELETE`.
- **טעויות:** סטטוס אפשר להחזיר. שורה מחוקה — רק מגיבוי.

זה נקרא **מחיקה רכה** (soft delete). **מחיקה קשה** (`DELETE`) — לנתונים שגויים באמת, או לפי חוק (למשל בקשה למחיקת מידע אישי).

---

## 7. DEFAULT — ערכי ברירת מחדל

ברירת מחדל מוגדרת **בטבלה** (מודול 26), ומשמשת כש‑`INSERT` לא נותן ערך. במודול 23 גילינו שלמקלט **אין טבלת תרומות** — בואו ניצור אחת:

</div>

```sql
CREATE TABLE donation (
  donation_id   INTEGER PRIMARY KEY,
  donor_name    TEXT    NOT NULL,
  amount        REAL    NOT NULL,
  donation_date TEXT    DEFAULT '2026-09-21',     -- in real code: DEFAULT CURRENT_DATE
  method        TEXT    DEFAULT 'cash'
);

INSERT INTO donation (donor_name, amount)         VALUES ('Haifa Rotary', 5000);
INSERT INTO donation (donor_name, amount, method) VALUES ('Anonymous',    250, 'bit');

SELECT * FROM donation;
```

```text
donation_id  donor_name    amount  donation_date  method
-----------  ------------  ------  -------------  ------
1            Haifa Rotary  5000.0  2026-09-21     cash      <- both defaults used
2            Anonymous     250.0   2026-09-21     bit       <- method given, date default
```

<div dir="rtl">

| הדרך | SQLite | Oracle |
|------|--------|--------|
| להשמיט את העמודה | ✅ | ✅ |
| המילה `DEFAULT` בתוך `VALUES` | ❌ שגיאת תחביר | ✅ `VALUES ('X', 100, DEFAULT, 'bit')` |
| `UPDATE … SET col = DEFAULT` | ❌ | ✅ |
| `INSERT … DEFAULT VALUES` (כל העמודות) | ✅ — אם אין `NOT NULL` בלי ברירת מחדל | ❌ |

> 🔑 **הדרך שעובדת בכל מקום: להשמיט את העמודה מהרשימה.** ובהגדרת הטבלה — ברירת מחדל לכל עמודה שיש לה ערך "רגיל" (תאריך היום, סטטוס התחלתי, 0).

---

## 8. MERGE — הוסף או עדכן

מצב נפוץ: מגיעה רשימת מלאי מהספק. מוצר **קיים** ⟵ להוסיף לכמות. מוצר **חדש** ⟵ להכניס שורה. בלי `MERGE` זה `SELECT`, ואז `IF`, ואז `INSERT` או `UPDATE` — לכל שורה.

### 8.1 Oracle: `MERGE`

</div>

```sql
-- Oracle
MERGE INTO stock s
USING (SELECT 'cat litter' AS item, 10 AS qty FROM dual
       UNION ALL
       SELECT 'leash', 4 FROM dual) d
ON    (s.item = d.item)
WHEN MATCHED THEN
      UPDATE SET s.qty = s.qty + d.qty
WHEN NOT MATCHED THEN
      INSERT (item, qty) VALUES (d.item, d.qty);
```

<div dir="rtl">

### 8.2 SQLite (וגם PostgreSQL): `ON CONFLICT` — "upsert"

</div>

```sql
CREATE TABLE stock (item TEXT PRIMARY KEY, qty INTEGER NOT NULL);
INSERT INTO stock VALUES ('dog food sack', 12), ('cat litter', 5);

INSERT INTO stock (item, qty) VALUES ('cat litter', 10), ('leash', 4)
ON CONFLICT(item) DO UPDATE SET qty = qty + excluded.qty;

SELECT * FROM stock;
```

```text
item           qty
-------------  ---
dog food sack  12
cat litter     15      <- existed: 5 + 10
leash          4       <- new: inserted
```

<div dir="rtl">

**`excluded`** = השורה שניסינו להכניס ונתקלה בהתנגשות. `qty` = הערך הקיים; `excluded.qty` = הערך החדש.

> 💡 **`ON CONFLICT` עובד רק אם יש `UNIQUE` או `PRIMARY KEY`** על העמודה — כי "התנגשות" מוגדרת על ידי אילוץ. בלי אילוץ, אין התנגשות — ונקבל שתי שורות של "cat litter".

---

## 9. Multi-table insert

Oracle מאפשר **שאילתה אחת שמכניסה לכמה טבלאות**, לפי תנאים:

</div>

```sql
-- Oracle: split the intakes into two archive tables in one pass
INSERT ALL
  WHEN intake_type = 'stray'     THEN INTO stray_archive     VALUES (intake_id, animal_id, location)
  WHEN intake_type = 'surrender' THEN INTO surrender_archive VALUES (intake_id, animal_id, reason)
SELECT intake_id, animal_id, intake_type, location, reason
FROM   intake;
```

<div dir="rtl">

**ב‑SQLite (ובכל מקום):** פשוט שני `INSERT … SELECT`, אחד לכל טבלה, עם `WHERE` מתאים. `INSERT ALL` חוסך מעבר אחד על הנתונים — חשוב כשמדובר במיליוני שורות.

> 🔑 **הקשר למודול 4:** זה בדיוק מה שקורה כשמחליטים לאחסן טיפוסי משנה בטבלאות נפרדות — כל קליטה הולכת לטבלה של הסוג שלה.

---

## 10. נוהל העבודה הבטוח

**כל `UPDATE` ו‑`DELETE` מתחיל כ‑`SELECT`.**

</div>

```text
   STEP 1 -- write the WHERE as a SELECT, and LOOK at the rows
   SELECT * FROM animal WHERE status = 'quarantine' AND animal_id = 9;
   -> 1 row: Nala.   Good, that's the one.

   STEP 2 -- same WHERE, change only the first line
   UPDATE animal SET status = 'available'
   WHERE  status = 'quarantine' AND animal_id = 9;

   STEP 3 -- check the count
   SELECT changes();     -> 1.   Matches step 1.

   STEP 4 -- look again
   SELECT * FROM animal WHERE animal_id = 9;
```

<div dir="rtl">

**ועוד שלושה הרגלים:**
- **לפי מפתח ראשי** כשמשנים שורה אחת: `WHERE animal_id = 9`, לא `WHERE name = 'Nala'` (אולי יש שתיים).
- **טרנזקציה** סביב שינוי מסוכן: `BEGIN; … ; SELECT …; ROLLBACK;` — מודול 32. אפשר לנסות, להסתכל, ולבטל.
- **גיבוי** לפני שינוי גדול: `CREATE TABLE animal_backup AS SELECT * FROM animal;`

> 🎬 **סיפור מהשטח:** בינואר 2017 מהנדס ב‑GitLab, באמצע לילה של תקלות, מחק בטעות את תיקיית בסיס הנתונים בשרת **הייצור** — הוא היה בטוח שהוא מחובר לשרת הגיבוי. כשניסו לשחזר, התברר שכמה ממנגנוני הגיבוי לא עבדו כבר זמן רב. החברה איבדה כשש שעות של נתונים. **הלקחים זהים לשלנו:** לבדוק **איפה** אתם לפני פקודה הרסנית, להסתכל לפני שמשנים, ולוודא שהגיבוי באמת עובד.

---

## 11. שש טעויות נפוצות

| # | הטעות | מה קורה | התיקון |
|---|-------|----------|---------|
| 1 | **`UPDATE` / `DELETE` בלי `WHERE`** | כל הטבלה | `SELECT` עם אותו `WHERE` קודם |
| 2 | **`INSERT` בלי רשימת עמודות** | נשבר כשמוסיפים עמודה; ערכים בעמודה הלא נכונה | תמיד `INSERT INTO t (a, b, c)` |
| 3 | **לשכוח `PRAGMA foreign_keys = ON`** ב‑SQLite | יתומים ומפתחות שגויים נכנסים | שורה ראשונה בכל סשן |
| 4 | **`WHERE name = …` לשורה אחת** | משנה גם חיה אחרת באותו שם | `WHERE animal_id = …` |
| 5 | **`'NULL'` בגרשיים** | נשמר הטקסט "NULL", לא ערך חסר | `NULL` בלי גרשיים |
| 6 | **`DELETE` כשצריך לעדכן סטטוס** | ההיסטוריה נמחקת | מחיקה רכה: `status = 'deceased'` |

---

## 12. סיכום המודול

<div align="center">

### 🧠 שבע נקודות

</div>

1. **DML = `INSERT`, `UPDATE`, `DELETE`** (+ `MERGE`). מכאן — משנים נתונים, לא רק קוראים.
2. **`INSERT INTO t (cols) VALUES (…)`** — תמיד עם רשימת עמודות. עמודה שהושמטה ⟵ ברירת מחדל או NULL. **`INSERT … SELECT`** — שורות מתוך שאילתה.
3. **`UPDATE … SET … WHERE`** — בלי `WHERE`, כל השורות. אפשר לחשב מהערך הישן (`x = x * 1.1`).
4. **`DELETE … WHERE`** — נחסם על ידי מפתח זר אם יש ילדים. ובמקרים רבים עדיף **מחיקה רכה**.
5. **SQLite: `PRAGMA foreign_keys = ON;`** — אחרת מפתחות זרים לא נבדקים.
6. **"הוסף או עדכן":** `MERGE` ב‑Oracle, `INSERT … ON CONFLICT DO UPDATE` ב‑SQLite. דורש `UNIQUE`.
7. **הנוהל:** `SELECT` ⟵ `UPDATE`/`DELETE` עם אותו `WHERE` ⟵ בדיקת מספר השורות ⟵ `SELECT` שוב.

<div align="center">

---

*"SELECT לא יכול לקלקל כלום.*
*UPDATE בלי WHERE יכול לקלקל הכול."*

---

</div>

## 📎 המשך

| | |
|---|---|
| ❓ | [שאלות ותשובות](questions.md) |
| ✏️ | [תרגילים](exercises.md) — על [בסיס הנתונים המוכן](../../resources/shelter-db/) |
| ✅ | [פתרונות](solutions.md) |
| ⬅️ | [מודול 24 — SQL: קיבוץ נתונים ותתי‑שאילתות](../module-24-sql-group-by/) |
| ➡️ | [מודול 26 — SQL: שפת הגדרת אובייקטים (DDL)](../module-26-sql-ddl/) |
| 🏠 | [חזרה לדף הקורס](../../) |

</div>
