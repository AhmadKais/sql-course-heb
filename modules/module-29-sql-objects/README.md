<div dir="rtl">

# מודול 29 — SQL: אובייקטים נוספים

> **פרק 29 בתכנית הלימודים** · 3 שעות עיוני + 2 שעות מעשי
> **נושאים:** ראיון בכיתה · Sequences · אינדקסים וסינונימים

> 🧭 **במסלול המשולב:** יחידה 11, לצד [מודול 11 — מודלים גנריים](../module-11-generic-models/). **מפתחות מלאכותיים — עשויים כמו שצריך.**

---

## 🎯 מה תדעו בסוף המודול

- [ ] להסביר מה זה **Sequence**, ולמה צריך אותו למפתח מלאכותי
- [ ] לייצר מזהים אוטומטיים ב‑SQLite (`AUTOINCREMENT`) וב‑Oracle (`SEQUENCE`, `IDENTITY`)
- [ ] להסביר מה זה **אינדקס** ואיך הוא מאיץ שאילתות — ומה הוא עולה
- [ ] ליצור אינדקס, ולבדוק עם `EXPLAIN QUERY PLAN` שהוא באמת משמש
- [ ] לפתור את הבעיה ממודול 19: אינדקס על `UPPER(name)`
- [ ] להסביר מה זה **סינונים** (Synonym) ב‑Oracle
- [ ] לענות על שאלות **ראיון עבודה** על כל מה שלמדתם

---

## 🗺️ מפת המודול

| # | הסעיף |
|---|--------|
| 1 | [מזהים אוטומטיים — הבעיה](#1-מזהים-אוטומטיים--הבעיה) |
| 2 | [ב‑SQLite: `INTEGER PRIMARY KEY` ו‑`AUTOINCREMENT`](#2-בsqlite-integer-primary-key-ו‑autoincrement) |
| 3 | [ב‑Oracle: `SEQUENCE` ו‑`IDENTITY`](#3-בoracle-sequence-ו‑identity) |
| 4 | [אינדקס — מה זה](#4-אינדקס--מה-זה) |
| 5 | [יצירת אינדקס ובדיקה שהוא עובד](#5-יצירת-אינדקס-ובדיקה-שהוא-עובד) |
| 6 | [מתי אינדקס לא עוזר](#6-מתי-אינדקס-לא-עוזר) |
| 7 | [המחיר של אינדקס — ואיך בוחרים](#7-המחיר-של-אינדקס--ואיך-בוחרים) |
| 8 | [Synonym — שם נוסף לאובייקט](#8-synonym--שם-נוסף-לאובייקט) |
| 9 | [ראיון בכיתה](#9-ראיון-בכיתה) |
| 10 | [סיכום המודול](#10-סיכום-המודול) |

---

## 1. מזהים אוטומטיים — הבעיה

במודול 27 החלטנו: מפתח ראשי **מלאכותי** — מספר בלי משמעות. אבל מאיפה המספר מגיע?

</div>

```text
   idea 1:  SELECT MAX(animal_id) + 1 FROM animal;   then INSERT with that number

   clerk A at 10:00:00.000   reads MAX = 20   -> will insert 21
   clerk B at 10:00:00.001   reads MAX = 20   -> will insert 21
   clerk A inserts 21  OK
   clerk B inserts 21  ERROR: UNIQUE constraint failed   (or worse, without a PK: two animals #21)
```

<div dir="rtl">

כשכמה אנשים עובדים במקביל, `MAX + 1` **נכשל**. צריך מנגנון ש**בסיס הנתונים** מנהל, ושמבטיח שכל מי שמבקש מספר — יקבל מספר **אחר**.

---

## 2. ב‑SQLite: `INTEGER PRIMARY KEY` ו‑`AUTOINCREMENT`

### 2.1 `INTEGER PRIMARY KEY` — מספר אוטומטי

כבר ראינו (מודול 25): עמודה מסוג `INTEGER PRIMARY KEY` שלא קיבלה ערך — מקבלת מספר אוטומטית. **אבל** הוא עלול **למחזר** מספרים:

</div>

```sql
CREATE TABLE d2 (id INTEGER PRIMARY KEY, donor TEXT);
INSERT INTO d2 (donor) VALUES ('A'), ('B'), ('C');      -- 1, 2, 3
DELETE FROM d2 WHERE id = 3;                            -- C is deleted
INSERT INTO d2 (donor) VALUES ('D');
SELECT * FROM d2;
```

```text
id  donor
--  -----
1   A
2   B
3   D        <- D got C's old number!
```

<div dir="rtl">

### 2.2 `AUTOINCREMENT` — לעולם לא אותו מספר פעמיים

</div>

```sql
CREATE TABLE donation (
  donation_id INTEGER PRIMARY KEY AUTOINCREMENT,
  donor       TEXT NOT NULL,
  amount      REAL NOT NULL
);
INSERT INTO donation (donor, amount) VALUES ('A', 100), ('B', 200), ('C', 300);
DELETE FROM donation WHERE donation_id = 3;
INSERT INTO donation (donor, amount) VALUES ('D', 400);
SELECT * FROM donation;
```

```text
donation_id  donor  amount
-----------  -----  ------
1            A      100.0
2            B      200.0
4            D      400.0      <- 3 is never reused
```

<div dir="rtl">

SQLite שומר את המספר האחרון שחולק בטבלה פנימית — `sqlite_sequence` — שהיא בעצם **sequence** קטן.

> 🔑 **למה זה חשוב?** אם קבלה מספר 3 נמחקה, ואז קבלה חדשה מקבלת שוב 3 — מסמך ישן שמזכיר "תרומה 3" מצביע עכשיו על תרומה אחרת. **מזהה שמוחזר לשימוש הוא באג שמחכה.** לכל טבלה שהמזהים שלה יוצאים החוצה (קבלות, הזמנות, מספרי תיק) — `AUTOINCREMENT`.

---

## 3. ב‑Oracle: `SEQUENCE` ו‑`IDENTITY`

### 3.1 `SEQUENCE` — מחולל מספרים עצמאי

ב‑Oracle, **Sequence** הוא אובייקט נפרד בבסיס הנתונים — "מכונת מספרים" שכל קריאה אליה נותנת את המספר הבא:

</div>

```sql
-- Oracle
CREATE SEQUENCE animal_seq
  START WITH 21          -- first number
  INCREMENT BY 1
  NOCACHE;               -- (CACHE 20 = faster, but numbers may be skipped after a restart)

INSERT INTO animal (animal_id, name, species_id, sex, status)
VALUES (animal_seq.NEXTVAL, 'Milo', 2, 'M', 'quarantine');      -- 21

INSERT INTO intake (intake_id, animal_id, intake_date, intake_type)
VALUES (intake_seq.NEXTVAL, animal_seq.CURRVAL, SYSDATE, 'stray');  -- the SAME 21

SELECT animal_seq.CURRVAL FROM dual;     -- 21: the last number THIS session got
```

<div dir="rtl">

| | מה מחזיר |
|---|---|
| `seq.NEXTVAL` | **מקדם** את ה‑sequence ומחזיר את המספר החדש |
| `seq.CURRVAL` | המספר האחרון ש**הסשן הזה** קיבל — בלי לקדם |

> 💡 **`CURRVAL` הוא הדרך לקשר שורות:** יוצרים חיה עם `NEXTVAL`, ומיד רושמים את הקליטה שלה עם `CURRVAL` — אותו מספר, בלי לשאול "מה המספר שקיבלתי?". ב‑SQLite: `last_insert_rowid()`.

> ⚠️ **Sequence לא מבטיח רצף בלי חורים.** אם `INSERT` נכשל או בוטל (`ROLLBACK`), המספר שנלקח **לא חוזר**. מספרי חשבוניות שחייבים להיות רציפים לפי חוק — דורשים מנגנון אחר.

### 3.2 `IDENTITY` — הדרך המודרנית (Oracle 12c+)

</div>

```sql
-- Oracle 12c and later: no separate sequence to manage
CREATE TABLE donation (
  donation_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  donor       VARCHAR2(100) NOT NULL,
  amount      NUMBER(10,2)  NOT NULL
);
```

<div dir="rtl">

| | SQLite | Oracle ישן | Oracle 12c+ | PostgreSQL / SQL Server |
|---|---|---|---|---|
| מזהה אוטומטי | `INTEGER PRIMARY KEY` | `SEQUENCE` + `NEXTVAL` | `GENERATED AS IDENTITY` | `SERIAL` / `IDENTITY` |
| בלי מחזור | `AUTOINCREMENT` | ✅ תמיד | ✅ תמיד | ✅ תמיד |

---

## 4. אינדקס — מה זה

איך מוצאים מילה בספר של 500 עמודים? אפשר לדפדף מהעמוד הראשון עד שמוצאים. או — לפתוח את **האינדקס** בסוף, שם המילים ממוינות ולכל אחת מספר עמוד.

</div>

```text
   without an index  --  "SCAN"                    with an index  --  "SEARCH"

   SELECT * FROM animal WHERE name = 'Rex';        index on name (sorted):
                                                     Bella   -> row 5
   row 1  Luna    no                                 Bunny   -> row 19
   row 2  Simba   no                                 ...
   row 3  Rocky   no                                 Rex     -> row 13    <- jump straight here
   ...                                               Rocky   -> row 3
   row 13 Rex     YES                                ...
   ...  (keeps going -- maybe another Rex?)
   row 20 Shadow  no

   20 rows: who cares.   10,000,000 rows: seconds vs. microseconds.
```

<div dir="rtl">

**אינדקס** הוא מבנה נתונים נוסף (בדרך כלל **B‑tree** — עץ מאוזן) שבסיס הנתונים שומר **בצד**: ערכי העמודה **ממוינים**, ולכל ערך — איפה השורה. חיפוש בו לוקח בערך log₂(n) צעדים: על מיליון שורות — כ‑20, במקום מיליון.

> 🔑 **אינדקס לא משנה את התוצאה — רק את המהירות.** אותה שאילתה, אותה תשובה. לכן אפשר להוסיף ולהסיר אינדקסים בלי לשנות שורת קוד אחת באפליקציה.

---

## 5. יצירת אינדקס ובדיקה שהוא עובד

</div>

```sql
CREATE INDEX idx_animal_name ON animal(name);
DROP INDEX idx_animal_name;
```

<div dir="rtl">

### 5.1 `EXPLAIN QUERY PLAN` — איך בסיס הנתונים מתכנן לבצע

</div>

```sql
EXPLAIN QUERY PLAN SELECT * FROM animal WHERE name = 'Luna';
-- before:   SCAN animal                                          <- reads every row
CREATE INDEX idx_animal_name ON animal(name);
EXPLAIN QUERY PLAN SELECT * FROM animal WHERE name = 'Luna';
-- after:    SEARCH animal USING INDEX idx_animal_name (name=?)   <- jumps to the row
```

<div dir="rtl">

| המילה בתוכנית | המשמעות |
|----------------|----------|
| `SCAN` | עובר על **כל** הטבלה |
| `SEARCH … USING INDEX` | קופץ ישר לשורות המתאימות |
| `USING INTEGER PRIMARY KEY` | חיפוש לפי המפתח הראשי — הכי מהיר |

> 💡 ב‑Oracle: `EXPLAIN PLAN FOR SELECT …;` ואז `SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);` — המילים שם: `TABLE ACCESS FULL` (= SCAN) מול `INDEX RANGE SCAN`.

### 5.2 אינדקסים שכבר קיימים — מאילוצים

</div>

```sql
SELECT name, tbl_name, sql FROM sqlite_master WHERE type = 'index';
```

```text
name                        tbl_name  sql
--------------------------  --------  -------------------------------------------
sqlite_autoindex_species_1  species                       <- from UNIQUE on species.name
sqlite_autoindex_animal_1   animal                        <- from UNIQUE on chip_number
idx_animal_name             animal    CREATE INDEX idx_animal_name ON animal(name)
```

<div dir="rtl">

**כל `PRIMARY KEY` ו‑`UNIQUE` יוצרים אינדקס אוטומטית** — כי כדי לבדוק "האם הערך הזה כבר קיים?" בכל `INSERT`, צריך חיפוש מהיר. לכן חיפוש לפי `chip_number` כבר מהיר:

</div>

```sql
EXPLAIN QUERY PLAN SELECT * FROM animal WHERE chip_number = '985100003';
-- SEARCH animal USING INDEX sqlite_autoindex_animal_1 (chip_number=?)
```

<div dir="rtl">

### 5.3 אינדקס על מפתחות זרים

</div>

```sql
EXPLAIN QUERY PLAN SELECT * FROM vaccination WHERE animal_id = 3;   -- SCAN vaccination
CREATE INDEX idx_vacc_animal ON vaccination(animal_id);
EXPLAIN QUERY PLAN SELECT * FROM vaccination WHERE animal_id = 3;   -- SEARCH ... USING INDEX
```

<div dir="rtl">

> 🔑 **מפתח זר לא יוצר אינדקס אוטומטית** — לא ב‑SQLite ולא ב‑Oracle. אבל כמעט כל `JOIN` הולך דרכו. **כלל אצבע: אינדקס על כל עמודת מפתח זר.** זה האינדקס הכי משתלם שיש.

---

## 6. מתי אינדקס לא עוזר

### 6.1 פונקציה על העמודה — הבעיה ממודול 19

</div>

```sql
EXPLAIN QUERY PLAN SELECT * FROM animal WHERE UPPER(name) = 'LUNA';
-- SCAN animal       <- the index on name is useless: it's sorted by name, not by UPPER(name)
```

<div dir="rtl">

במודול 19 (סעיף 6.3) הבטחנו פתרון. הנה הוא — **אינדקס על ביטוי**:

</div>

```sql
CREATE INDEX idx_animal_upper_name ON animal(UPPER(name));
EXPLAIN QUERY PLAN SELECT * FROM animal WHERE UPPER(name) = 'LUNA';
-- SEARCH animal USING INDEX idx_animal_upper_name (<expr>=?)
```

<div dir="rtl">

> 💡 ב‑Oracle זה נקרא **function-based index** — אותו תחביר.

### 6.2 `LIKE` שמתחיל ב‑`%`

</div>

```sql
EXPLAIN QUERY PLAN SELECT * FROM animal WHERE name LIKE '%na';    -- SCAN animal
```

<div dir="rtl">

אינדקס ממוין לפי **תחילת** הערך — כמו ספר טלפונים. "כל מי שהשם שלו **מסתיים** ב‑na" — אין דרך לקפוץ; חייבים לעבור על הכול. `LIKE 'Lu%'` — כן יכול להשתמש באינדקס (בתנאים מסוימים).

### 6.3 טבלאות קטנות ותנאים לא סלקטיביים

על 20 שורות — `SCAN` מהיר כמו `SEARCH`, ולפעמים בסיס הנתונים יבחר בו בכוונה. ו‑`WHERE status = 'adopted'` על מיליון שורות שחצין מאומצות — אינדקס לא יעזור הרבה: ממילא צריך לקרוא חצי טבלה.

---

## 7. המחיר של אינדקס — ואיך בוחרים

**אינדקס אינו בחינם:**

| המחיר | למה |
|-------|------|
| **מקום בדיסק** | עותק ממוין של העמודה |
| **`INSERT` / `UPDATE` / `DELETE` איטיים יותר** | כל שינוי בטבלה — גם עדכון של כל אינדקס עליה |

**מתי כן:**

| ✅ שווה אינדקס | ❌ לא שווה |
|----------------|-----------|
| עמודות מפתח זר (בשביל `JOIN`) | טבלאות קטנות (מאות שורות) |
| עמודות שמחפשים לפיהן הרבה ב‑`WHERE` | עמודות עם מעט ערכים שונים (`sex`, `status`) |
| עמודות ב‑`ORDER BY` של שאילתות נפוצות | טבלה שכותבים אליה הרבה וקוראים ממנה מעט (יומן) |
| ביטוי שמופיע ב‑`WHERE` (`UPPER(name)`) | "ליתר ביטחון" על כל עמודה |

> 🎬 **מהשטח:** שאילתת דוח באתר מסחר רצה 40 שניות. ה‑DBA הריץ `EXPLAIN`, ראה `TABLE ACCESS FULL` על טבלת הזמנות של 30 מיליון שורות, והוסיף אינדקס אחד על `customer_id`. **0.02 שניות.** אף שורת קוד לא השתנתה. זה הכוח של אינדקס — ולכן זו שאלת ראיון שכיחה.

---

## 8. Synonym — שם נוסף לאובייקט

ב‑Oracle, כל טבלה שייכת ל**סכמה** (schema) — בערך "המשתמש שיצר אותה". טבלת `animal` של המשתמש `SHELTER` היא `SHELTER.ANIMAL`. משתמש אחר צריך לכתוב את השם המלא:

</div>

```sql
-- Oracle, logged in as user REPORTS
SELECT * FROM shelter.animal;          -- works, but every query must say "shelter."

CREATE SYNONYM animal FOR shelter.animal;
SELECT * FROM animal;                  -- now just "animal"

CREATE PUBLIC SYNONYM species FOR shelter.species;   -- for EVERY user (needs admin rights)
DROP SYNONYM animal;
```

<div dir="rtl">

| הסוג | למי |
|------|-----|
| `SYNONYM` (פרטי) | רק למשתמש שיצר אותו |
| `PUBLIC SYNONYM` | לכל המשתמשים |

**שני שימושים:** **נוחות** (שם קצר במקום `schema.table`), ו**יציבות** — אם הטבלה עוברת לסכמה אחרת, משנים את ה‑synonym, והקוד לא משתנה. (כמו View — סעיף 4.4 במודול 28 — רק בלי שאילתה.)

> 💡 **ב‑SQLite אין סכמות ואין synonyms** — כל הטבלאות בקובץ אחד, וכל מי שפתח את הקובץ רואה הכול. (המקבילה הרחוקה: `ATTACH DATABASE` לקובץ נוסף.) ההבדל הזה — Oracle כשרת מרובה משתמשים, SQLite כקובץ — יחזור במודול 30.

---

## 9. ראיון בכיתה

תכנית הלימודים מקדישה לכאן **ראיון עבודה מדומה**. הנה שאלות אמיתיות מראיונות לתפקידי ג'וניור (אנליסט נתונים, מפתח, QA). **עבדו בזוגות:** אחד מראיין, אחד עונה בקול — ואז מתחלפים.

### 9.1 שאלות מושגים

| # | השאלה | המודול |
|---|--------|---------|
| 1 | מה ההבדל בין מפתח ראשי למפתח זר? | 7, 27 |
| 2 | מה זה נרמול, ולמה עושים אותו? מה החיסרון? | 6 |
| 3 | מה ההבדל בין `INNER JOIN` ל‑`LEFT JOIN`? | 21–22 |
| 4 | מה ההבדל בין `WHERE` ל‑`HAVING`? | 24 |
| 5 | מה ההבדל בין `DELETE`, `TRUNCATE` ו‑`DROP`? | 25–26 |
| 6 | מה זה אינדקס? מתי **לא** כדאי להוסיף אחד? | 29 |
| 7 | מה זה View, ומה ההבדל בינו לבין טבלה? | 28 |
| 8 | מה זה NULL? מה מחזיר `NULL = NULL`? | 16, 20 |

### 9.2 שאלות "כתוב שאילתה" — על הלוח, בלי מחשב

1. החיה הכבדה ביותר מכל מין. *(רמז: תת‑שאילתה מתואמת — מודול 24.)*
2. כל המאמצים שאימצו יותר מחיה אחת. *(`GROUP BY … HAVING`.)*
3. חיות שמעולם לא חוסנו — בשתי דרכים. *(`LEFT JOIN … IS NULL` / `NOT EXISTS`.)*
4. הסכום הכולל של ההוצאות לכל חודש ב‑2024. *(`STRFTIME('%Y-%m')` + `GROUP BY`.)*
5. ⭐ "הציון השני בגובהו" — כאן: **המשקל השני בגובהו**. *(קלאסיקה של ראיונות.)*

### 9.3 שאלת ה"מה לא בסדר" — הכי נפוצה בראיונות

</div>

```sql
SELECT name, COUNT(*)
FROM   animal a
JOIN   vaccination v ON v.animal_id = a.animal_id
WHERE  COUNT(*) > 2;
```

<div dir="rtl">

**שלוש** טעויות. מצאתם? *(תשובות בשאלות של המודול.)*

> 🎬 **מה מראיינים באמת בודקים:** לא שתזכרו תחביר בעל פה — אלא ש**תחשבו בקול**. "אני צריך שורה לכל מין, אז `GROUP BY species`… רגע, אני צריך גם את השם, אז זה לא `GROUP BY` אלא תת‑שאילתה…". מי שמסביר את הדרך — מתקבל, גם אם יש לו טעות קטנה בתחביר.

---

## 10. סיכום המודול

<div align="center">

### 🧠 שש נקודות

</div>

1. **`MAX + 1` נכשל במקביליות.** מזהים אוטומטיים מנוהלים על ידי בסיס הנתונים.
2. **SQLite:** `INTEGER PRIMARY KEY` (עלול למחזר) · `AUTOINCREMENT` (לעולם לא). **Oracle:** `SEQUENCE` עם `NEXTVAL` / `CURRVAL`, או `GENERATED AS IDENTITY`.
3. **אינדקס** = עותק ממוין של עמודה ⟵ `SEARCH` במקום `SCAN`. לא משנה את התוצאה, רק את המהירות.
4. **`EXPLAIN QUERY PLAN`** — לבדוק שהאינדקס באמת משמש. `PRIMARY KEY` ו‑`UNIQUE` יוצרים אינדקס לבד; **מפתח זר — לא**.
5. **אינדקס לא עוזר:** פונקציה על העמודה (⟵ אינדקס על ביטוי), `LIKE '%…'`, טבלאות קטנות. **ועולה:** מקום, וכתיבה איטית יותר.
6. **Synonym** (Oracle) — שם נוסף לאובייקט מסכמה אחרת. נוחות ויציבות.

<div align="center">

---

*"אינדקס הוא ההבדל בין לחפש מחט בערימת שחת*
*לבין לדעת בדיוק באיזו ערימה היא."*

---

</div>

## 📎 המשך

| | |
|---|---|
| ❓ | [שאלות ותשובות](questions.md) |
| ✏️ | [תרגילים](exercises.md) |
| ✅ | [פתרונות](solutions.md) |
| ⬅️ | [מודול 28 — SQL: Views](../module-28-sql-views/) |
| ➡️ | [מודול 30 — SQL: ניהול משתמשים](../module-30-sql-users/) |
| 🏠 | [חזרה לדף הקורס](../../) |

</div>
