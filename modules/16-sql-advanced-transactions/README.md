<div dir="rtl">

# מודול 32 — SQL: ניהול טרנזקציות

> **פרק 32 בתכנית הלימודים** · 2 שעות עיוני + 2 שעות מעשי
> **נושאים:** טרנזקציות עסקיות · הכנה לבחינת הסמכה

> 🧭 **במסלול המשולב:** יחידה 10, לצד [מודול 10 — מעקב אחר שינויים](../module-10-tracking-changes/) ו[מודול 28 — Views](../module-28-sql-views/). **שינוי בטוח:** או שהכול נשמר — או ששום דבר לא.

---

## 🎯 מה תדעו בסוף המודול

- [ ] להסביר מהי **טרנזקציה**, ולמה פעולה עסקית אחת היא לעיתים כמה פקודות SQL
- [ ] להשתמש ב‑`BEGIN`, `COMMIT` ו‑`ROLLBACK`
- [ ] לנסות שינוי מסוכן, **להסתכל**, ולבטל
- [ ] להשתמש ב‑`SAVEPOINT` לביטול חלקי
- [ ] להסביר את ארבע תכונות **ACID**
- [ ] להבין מה קורה כששני משתמשים משנים את אותם נתונים בו‑זמנית
- [ ] להכיר את ההבדלים בין SQLite ל‑Oracle — כולל ה‑`COMMIT` האוטומטי של DDL
- [ ] להתכונן לבחינת ההסמכה של Oracle

---

## 🗺️ מפת המודול

| # | הסעיף |
|---|--------|
| 1 | [הבעיה: פעולה אחת, שתי פקודות](#1-הבעיה-פעולה-אחת-שתי-פקודות) |
| 2 | [BEGIN, COMMIT, ROLLBACK](#2-begin-commit-rollback) |
| 3 | [כשמשהו נכשל באמצע](#3-כשמשהו-נכשל-באמצע) |
| 4 | [ROLLBACK כרשת ביטחון](#4-rollback-כרשת-ביטחון) |
| 5 | [SAVEPOINT — ביטול חלקי](#5-savepoint--ביטול-חלקי) |
| 6 | [ACID](#6-acid) |
| 7 | [משתמשים במקביל — נעילות ובידוד](#7-משתמשים-במקביל--נעילות-ובידוד) |
| 8 | [SQLite מול Oracle](#8-sqlite-מול-oracle) |
| 9 | [הכנה לבחינת הסמכה](#9-הכנה-לבחינת-הסמכה) |
| 10 | [סיכום המודול — וסיכום הקורס](#10-סיכום-המודול--וסיכום-הקורס) |

---

## 1. הבעיה: פעולה אחת, שתי פקודות

Rocky אומץ! במערכת, **אימוץ** הוא שני שינויים:

</div>

```sql
UPDATE animal SET status = 'adopted' WHERE animal_id = 3;                       -- 1
INSERT INTO adoption (animal_id, adopter_id, adoption_date, fee_paid)           -- 2
VALUES (3, 12, '2026-09-21', 400);
```

<div dir="rtl">

**מה אם פקודה 1 הצליחה, ופקודה 2 נכשלה** — הקלדה שגויה, ניתוק רשת, נפילת חשמל?

</div>

```text
   after 1, before 2:   Rocky is "adopted"   -- but there is NO adoption record.
                        Who adopted him? When? Did they pay?  Nobody knows.
                        The website stops showing him. He is "lost" in the system.
```

<div dir="rtl">

> 🎬 **הדוגמה הקלאסית — העברה בנקאית:** להוריד 100 ₪ מחשבון A, ולהוסיף 100 ₪ לחשבון B. אם המערכת נופלת באמצע — 100 ₪ נעלמו מהעולם. **אף בנק לא יכול לעבוד ככה.**

**טרנזקציה** (transaction) היא קבוצת פקודות שבסיס הנתונים מתייחס אליהן כ**יחידה אחת**: **או שכולן מתבצעות — או שאף אחת.**

---

## 2. BEGIN, COMMIT, ROLLBACK

</div>

```sql
BEGIN;                                              -- start: changes are "pending"

UPDATE animal SET status = 'adopted' WHERE animal_id = 3;
INSERT INTO adoption (animal_id, adopter_id, adoption_date, fee_paid)
VALUES (3, 12, '2026-09-21', 400);

COMMIT;                                             -- both become permanent, together
```

<div dir="rtl">

| הפקודה | מה היא עושה |
|---------|-------------|
| `BEGIN` (או `BEGIN TRANSACTION`) | מתחילה טרנזקציה. מכאן — השינויים "בהמתנה" |
| `COMMIT` | **מאשרת**: כל השינויים מאז `BEGIN` נשמרים לצמיתות, ונראים לכולם |
| `ROLLBACK` | **מבטלת**: כל השינויים מאז `BEGIN` נעלמים, כאילו לא היו |

</div>

```text
   BEGIN --- UPDATE --- INSERT --- COMMIT        -> both saved
                                                    nobody ever sees "Rocky adopted, no record"

   BEGIN --- UPDATE --- INSERT --- ROLLBACK      -> both undone
                                                    the database is exactly as before BEGIN
```

<div dir="rtl">

> 💡 **בלי `BEGIN`**, ב‑SQLite כל פקודה היא טרנזקציה של פקודה אחת — היא נשמרת מיד (**autocommit**). זה מה שקרה בכל הקורס עד עכשיו.

---

## 3. כשמשהו נכשל באמצע

</div>

```sql
PRAGMA foreign_keys = ON;
BEGIN;
UPDATE animal SET status = 'adopted' WHERE animal_id = 13;             -- OK
INSERT INTO adoption (animal_id, adopter_id, adoption_date, fee_paid)
VALUES (13, 99, '2026-09-21', 400);                                    -- FAILS: no person 99

SELECT name, status FROM animal WHERE animal_id = 13;
-- Rex | adopted       <- !!! the UPDATE is still there, inside the open transaction
```

<div dir="rtl">

> ⚠️ **שגיאה בפקודה לא מבטלת את הטרנזקציה!** רק את הפקודה **שנכשלה**. ה‑`UPDATE` שלפניה עדיין "בהמתנה". אם עכשיו נכתוב `COMMIT` — Rex יישמר כמאומץ, בלי רישום אימוץ. **בדיוק הבעיה מסעיף 1.**

**מי שכותב את הטרנזקציה אחראי להחליט:**

</div>

```sql
ROLLBACK;                                                    -- something failed -> undo ALL
SELECT name, status FROM animal WHERE animal_id = 13;        -- Rex | available
```

<div dir="rtl">

> 🔑 **הכלל:** אם **כל** הפקודות הצליחו ⟵ `COMMIT`. אם **אחת** נכשלה ⟵ `ROLLBACK`. באפליקציה אמיתית זה נראה כך (בכל שפת תכנות):

</div>

```text
   try:
       BEGIN
       UPDATE animal ...
       INSERT INTO adoption ...
       COMMIT
   except (any error):
       ROLLBACK
       show "the adoption was not saved, please try again"
```

<div dir="rtl">

---

## 4. ROLLBACK כרשת ביטחון

במודול 25 (סעיף 10) הבטחנו: אפשר **לנסות** שינוי מסוכן, **להסתכל**, ורק אז להחליט.

</div>

```sql
BEGIN;
DELETE FROM expense;                           -- oops. Or was it deliberate?
SELECT COUNT(*) AS during FROM expense;        -- 0       look at the damage
ROLLBACK;                                      -- undo
SELECT COUNT(*) AS after FROM expense;         -- 22      nothing happened
```

<div dir="rtl">

**הנוהל הבטוח המלא — לכל `UPDATE` / `DELETE` בנתונים אמיתיים:**

</div>

```text
   1.  SELECT ... WHERE <condition>;        how many rows? which ones?
   2.  BEGIN;
   3.  UPDATE / DELETE ... WHERE <condition>;
   4.  SELECT changes();                    the same number as step 1?
   5.  SELECT ...;                          does the data look right now?
   6.  COMMIT;   -- if yes
       ROLLBACK; -- if anything looks wrong
```

<div dir="rtl">

> 💡 **בכלים כמו SQL Developer של Oracle**, ה‑autocommit **כבוי** כברירת מחדל — כל שינוי ממתין ל‑`COMMIT` ידני. מי שסוגר את התוכנה בלי `COMMIT` — מגלה למחרת שהעבודה שלו לא נשמרה. מי שעושה `COMMIT` מהר מדי — לא יכול לבטל.

---

## 5. SAVEPOINT — ביטול חלקי

טרנזקציה ארוכה, עם כמה שלבים. רוצים לבטל רק את **השלב האחרון**, ולשמור את מה שלפניו:

</div>

```sql
BEGIN;
UPDATE species SET adoption_fee = adoption_fee * 1.1;          -- step 1: new prices (good)

SAVEPOINT after_fees;                                          -- a "bookmark"

UPDATE animal SET status = 'available' WHERE status = 'adopted';   -- step 2: a mistake!
SELECT COUNT(*) FROM animal WHERE status = 'available';            -- 17 -- way too many

ROLLBACK TO after_fees;                                        -- undo ONLY step 2
SELECT COUNT(*) FROM animal WHERE status = 'available';        -- back to normal

COMMIT;                                                        -- step 1 is saved
SELECT name, adoption_fee FROM species;                        -- Dog 440, Cat 275, ...
```

<div dir="rtl">

| הפקודה | מבטלת |
|---------|--------|
| `ROLLBACK` | **הכול** מאז `BEGIN` |
| `ROLLBACK TO name` | רק מה שאחרי ה‑savepoint. הטרנזקציה **ממשיכה** |
| `RELEASE name` (SQLite) | מוחקת את הסימנייה, בלי לבטל |

---

## 6. ACID

ארבע ההבטחות של טרנזקציה — ראשי תיבות שמופיעים בכל ראיון ובכל מבחן:

| האות | השם | ההבטחה | בדוגמה של Rocky |
|------|-----|---------|------------------|
| **A** | Atomicity (אטומיות) | הכול או כלום | הסטטוס והאימוץ — שניהם, או אף אחד |
| **C** | Consistency (עקביות) | הטרנזקציה מעבירה את בסיס הנתונים ממצב תקין למצב תקין — כל האילוצים נשמרים | אי אפשר לסיים עם אימוץ של אדם 99 שלא קיים |
| **I** | Isolation (בידוד) | טרנזקציות שרצות במקביל לא רואות זו את השינויים הלא‑גמורים של זו | מתנדבת שגולשת באתר לא תראה את Rocky "באמצע אימוץ" |
| **D** | Durability (עמידות) | אחרי `COMMIT` — השינוי שמור, גם אם החשמל נופל שנייה אחרי | המאמץ קיבל אישור — האימוץ לא "ייעלם" בלילה |

> 🔑 **"אטום" = "בלתי ניתן לחלוקה"** (ביוונית). טרנזקציה אטומית — אי אפשר לבצע "חצי" ממנה.

---

## 7. משתמשים במקביל — נעילות ובידוד

**שני מתנדבים, אותו רגע, אותו כלב:**

</div>

```text
   10:00:00  Noa  (at the shelter): BEGIN;  is Rex available?  yes.
   10:00:01  Amir (on the phone):   BEGIN;  is Rex available?  yes.
   10:00:02  Noa:  UPDATE animal SET status = 'adopted' WHERE animal_id = 13;   -- Rex is LOCKED
   10:00:03  Amir: UPDATE animal SET status = 'adopted' WHERE animal_id = 13;   -- must WAIT...
   10:00:05  Noa:  INSERT adoption ...;  COMMIT;                                -- lock released
   10:00:05  Amir: his UPDATE now runs -- Rex is "adopted" twice. Two families, one dog.
```

<div dir="rtl">

**נעילה** (lock) מונעת משני משתמשים לשנות את **אותה שורה בדיוק** באותו רגע — השני מחכה. אבל היא לא מונעת את הבעיה הלוגית: אמיר בדק "זמין?" **לפני** שנועה שינתה. **הפתרון:** לבדוק ולשנות **בפקודה אחת**:

</div>

```sql
UPDATE animal SET status = 'adopted'
WHERE  animal_id = 13 AND status = 'available';     -- only if STILL available
SELECT changes();                                   -- 1: you got him.  0: someone was faster.
```

<div dir="rtl">

אם `changes()` מחזיר 0 — האפליקציה מודיעה "מצטערים, Rex אומץ זה עתה" ועושה `ROLLBACK`.

| | SQLite | Oracle |
|---|---|---|
| מה ננעל בכתיבה | **כל הקובץ** — כותב אחד בכל רגע | **השורה** בלבד |
| קוראים בזמן כתיבה | רואים את המצב שלפני השינוי | רואים את המצב שלפני השינוי (read consistency) |
| מתאים ל | אפליקציה אחת, מעט כותבים | אלפי משתמשים במקביל |

> 💡 **"קוראים לא חוסמים כותבים, וכותבים לא חוסמים קוראים"** — העיקרון של Oracle. מתנדבת שגולשת באתר תמיד תראה תמונה **עקבית**: או לפני האימוץ, או אחריו — לעולם לא באמצע (ה‑I של ACID).

---

## 8. SQLite מול Oracle

</div>

```text
+-----------------------------+--------------------------------+---------------------------------+
| WHAT                        | SQLite                         | Oracle                          |
+-----------------------------+--------------------------------+---------------------------------+
| start a transaction         | BEGIN;                         | (automatic: the first DML       |
|                             |                                |  statement starts one)          |
| without BEGIN               | autocommit -- each statement   | every change waits for COMMIT   |
|                             | is saved immediately           | (in SQL Developer / SQL*Plus)   |
| confirm / undo              | COMMIT; / ROLLBACK;            | same                            |
| savepoint                   | SAVEPOINT s; ROLLBACK TO s;    | SAVEPOINT s; ROLLBACK TO s;     |
| DDL (CREATE, ALTER, DROP)   | can be inside a transaction    | *** IMPLICIT COMMIT ***         |
|                             | and rolled back                | before and after -- no undo     |
| locking                     | whole database file            | row level                       |
| a failed statement          | only that statement is undone  | only that statement is undone   |
+-----------------------------+--------------------------------+---------------------------------+
```

<div dir="rtl">

> ⚠️ **ה‑COMMIT האוטומטי של DDL ב‑Oracle** (מודול 26) הוא המלכודת הכי מסוכנת כאן:

</div>

```sql
-- Oracle
DELETE FROM expense WHERE category = 'food';       -- pending
CREATE TABLE notes (txt VARCHAR2(100));            -- DDL -> implicit COMMIT! the DELETE is now permanent
ROLLBACK;                                          -- too late. The food expenses are gone.
```

<div dir="rtl">

**כלל:** אף פעם לא `CREATE` / `ALTER` / `DROP` / `TRUNCATE` באמצע עבודה שאולי תרצו לבטל.

---

## 9. הכנה לבחינת הסמכה

תכנית הלימודים מסתיימת בהכנה לבחינה. ההסמכה הרלוונטית: **Oracle Database SQL Certified Associate** (קוד בחינה **1Z0‑071**). הבחינה ממוחשבת, באנגלית, שאלות אמריקאיות — וכמעט כל החומר שלה מכוסה בחלק ב' של הקורס.

### 9.1 מיפוי הנושאים

| נושא בבחינה | המודולים |
|--------------|-----------|
| Retrieving data, restricting and sorting | 16, 17, 18 |
| Single-row functions, conversion functions, conditional expressions | 19, 20 |
| Group functions, GROUP BY, HAVING | 23, 24 |
| Joins (all types) | 21, 22 |
| Subqueries, set operators | 24 |
| DML, transactions | 25, 32 |
| DDL, data types, constraints | 26, 27 |
| Views, sequences, synonyms, indexes | 28, 29 |
| Users, privileges, roles | 30 |
| Data dictionary views | 26, 27, 28 |

### 9.2 מה הבחינה אוהבת לשאול

הבחינה בנויה על **מלכודות** — רובן כבר פגשתם:

| המלכודת | המודול |
|----------|---------|
| `NULL` בהשוואות, ב‑`NOT IN`, ב‑`COUNT(col)` מול `COUNT(*)` | 16, 23, 24 |
| עמודה ב‑`SELECT` שאינה ב‑`GROUP BY` | 24 |
| `WHERE` מול `HAVING` | 24 |
| `NATURAL JOIN` ו‑`USING` — כינוי לפני עמודת `USING` | 22 |
| תת‑שאילתה של שורה אחת שמחזירה כמה | 24 |
| `DDL` ⟵ `COMMIT` אוטומטי | 26, 32 |
| `TRUNCATE` מול `DELETE` מול `DROP` | 26 |
| `UNION` מול `UNION ALL`, ו‑`ORDER BY` בסוף | 24 |
| תאריכים ב‑Oracle: `SYSDATE`, `ADD_MONTHS`, `MONTHS_BETWEEN`, `TO_CHAR` | 19, 20 |

### 9.3 איך מתכוננים

1. **טבלאות ה‑"SQLite מול Oracle"** בסוף כל מודול — הבחינה היא **Oracle בלבד**.
2. **Oracle Live SQL** (חינם) — הריצו את הדוגמאות בתחביר Oracle.
3. **שאלות לדוגמה** — Oracle מפרסמת שאלות לדוגמה באתר ההסמכות. ובכל מודול כאן, חלק השאלות ג' בנוי בסגנון דומה.
4. **קראו כל שאלה פעמיים.** ברוב השאלות, שלוש תשובות "כמעט נכונות" — והמלכודת היא פרט קטן: NULL, כינוי, סדר.

---

## 10. סיכום המודול — וסיכום הקורס

<div align="center">

### 🧠 שש נקודות על טרנזקציות

</div>

1. **טרנזקציה = יחידה אחת:** כמה פקודות שמתבצעות כולן — או אף אחת.
2. **`BEGIN` ⟵ פקודות ⟵ `COMMIT`** (לשמור) או **`ROLLBACK`** (לבטל הכול).
3. **שגיאה בפקודה לא מבטלת את הטרנזקציה** — רק את הפקודה. ההחלטה (`ROLLBACK`) — שלכם.
4. **`SAVEPOINT` / `ROLLBACK TO`** — ביטול חלקי.
5. **ACID:** אטומיות, עקביות, בידוד, עמידות.
6. **ב‑Oracle:** כל DML פותח טרנזקציה; **כל DDL עושה `COMMIT` אוטומטי**.

<div align="center">

---

### 🎓 סוף הקורס

</div>

התחלתם בשאלה "מה ההבדל בין נתונים למידע?" (מודול 1). מאז:
- **ראיינתם לקוח**, מצאתם ישויות ויחסים, וציירתם ERD (2–5)
- **נרמלתם** והגדרתם חוקים עסקיים (6–7)
- **הצגתם ללקוח**, ותכננתם למעקב אחר שינויים ולמודלים גנריים (8–11)
- **הפכתם את המודל לטבלאות** (12, 26, 27)
- **שאלתם את הנתונים** בכל דרך אפשרית (16–24)
- **שיניתם אותם בבטחה** (25, 32), **הסתרתם, האצתם והגנתם** עליהם (28–30)
- **ובניתם מערכת שלמה ללקוח אמיתי** (9, 15, 31)

<div align="center">

*"בסיס נתונים טוב לא נראה.*
*הוא פשוט עונה נכון — כל פעם, לכל אחד, גם כשהחשמל נופל."*

---

</div>

## 📎 המשך

| | |
|---|---|
| ❓ | [שאלות ותשובות](questions.md) |
| ✏️ | [תרגילים](exercises.md) |
| ✅ | [פתרונות](solutions.md) |
| ⬅️ | [מודול 31 — SQL: פרויקט מסכם](../module-31-sql-final-project/) |
| 🏠 | [חזרה לדף הקורס](../../) |

</div>
