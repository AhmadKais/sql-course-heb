<div dir="rtl">

# מודול 30 — SQL: ניהול משתמשים

> **פרק 30 בתכנית הלימודים** · 3 שעות עיוני + 2 שעות מעשי
> **נושאים:** חיפוש עבודה · שליטה בהרשאות גישה למשתמשים · שליטה בהרשאות גישה לאובייקטים · Regular Expressions

> 🧭 **במסלול המשולב:** יחידה 12, לצד [מודול 13 — SQL I](../module-13-sql-1/) ו[מודול 14 — SDLC](../module-14-sdlc/). **המשימה של היחידה: לתת למתנדבת הרשאת קריאה בלבד.**

---

## 🎯 מה תדעו בסוף המודול

- [ ] להסביר למה בסיס נתונים צריך **משתמשים והרשאות**
- [ ] להבדיל בין הרשאות **מערכת** להרשאות **אובייקט**
- [ ] לתת ולשלול הרשאות עם `GRANT` ו‑`REVOKE`
- [ ] לנהל הרשאות בקבוצות עם **תפקידים** (Roles)
- [ ] לשלב **View + GRANT** כדי להראות רק חלק מהנתונים
- [ ] לחפש תבניות טקסט עם **ביטויים רגולריים** (Oracle) ועם `GLOB` (SQLite)
- [ ] לבנות תוכנית לחיפוש עבודה ראשונה בתחום

---

## 🗺️ מפת המודול

| # | הסעיף |
|---|--------|
| 1 | [למה משתמשים והרשאות](#1-למה-משתמשים-והרשאות) |
| 2 | [⚠️ SQLite לעומת Oracle](#2-️-sqlite-לעומת-oracle) |
| 3 | [יצירת משתמש והרשאות מערכת](#3-יצירת-משתמש-והרשאות-מערכת) |
| 4 | [הרשאות אובייקט — GRANT ו‑REVOKE](#4-הרשאות-אובייקט--grant-ו‑revoke) |
| 5 | [תפקידים (Roles)](#5-תפקידים-roles) |
| 6 | [View + GRANT — רק מה שצריך](#6-view--grant--רק-מה-שצריך) |
| 7 | [העיקרון: הרשאה מינימלית](#7-העיקרון-הרשאה-מינימלית) |
| 8 | [ביטויים רגולריים](#8-ביטויים-רגולריים) |
| 9 | [חיפוש עבודה](#9-חיפוש-עבודה) |
| 10 | [סיכום המודול](#10-סיכום-המודול) |

---

## 1. למה משתמשים והרשאות

במקלט "בית חם" יש כמה סוגי אנשים שעובדים עם המערכת:

| מי | מה צריך | מה **אסור** לו |
|----|---------|-----------------|
| **רותי** — מנהלת | הכול | — |
| **וטרינר** | לקרוא חיות, להוסיף חיסונים | לראות כספים; למחוק חיות |
| **מתנדבת** | לראות אילו חיות זמינות | לראות טלפונים של מאמצים; לשנות כל דבר |
| **רואה החשבון** | לקרוא הוצאות ואימוצים | לשנות; לראות מידע רפואי |
| **האתר** (תוכנה) | לקרוא חיות זמינות | כל השאר |

אם כולם מתחברים עם **אותו** משתמש עם **כל** ההרשאות — מתנדבת יכולה בטעות להריץ `DELETE FROM animal`, ופריצה לאתר חושפת את כל הטלפונים. **הרשאות** קובעות מי יכול לעשות מה, על איזה אובייקט.

> 🔑 **הקשר לחוק:** חוק הגנת הפרטיות ותקנות אבטחת המידע בישראל מחייבים ארגון שמחזיק מידע אישי (כמו טלפונים של מאמצים) להגביל את הגישה אליו **רק למי שצריך**. הרשאות בבסיס הנתונים הן הכלי לעשות את זה.

---

## 2. ⚠️ SQLite לעומת Oracle

**ב‑SQLite אין משתמשים ואין `GRANT`.** SQLite הוא **קובץ** — מי שיכול לפתוח את הקובץ, רואה הכול. ההרשאות שלו הן הרשאות הקבצים של מערכת ההפעלה. זה מתאים לאפליקציה בטלפון, לא לארגון עם עשרים עובדים.

</div>

```text
   SQLite                                   Oracle / PostgreSQL / SQL Server
   ------                                   --------------------------------
   a FILE on one computer                   a SERVER on the network
   one app opens it                         many users connect at the same time
   no users, no GRANT                       users, passwords, GRANT, REVOKE, roles
   security = who can read the file         security = inside the database
```

<div dir="rtl">

**לכן כל הקוד בסעיפים 3–6 הוא Oracle.** אפשר להריץ אותו ב‑[Oracle Live SQL](https://livesql.oracle.com) (חינם, עם הרשמה) או ב‑APEX — או פשוט לקרוא ולהבין, ולתרגל על הנייר. ✏️ התרגילים בנויים כך.

---

## 3. יצירת משתמש והרשאות מערכת

</div>

```sql
-- Oracle, as an administrator
CREATE USER noa IDENTIFIED BY "Str0ng!Passw0rd";

GRANT CREATE SESSION TO noa;        -- may log in at all
```

<div dir="rtl">

משתמש חדש **לא יכול לעשות כלום** — אפילו לא להתחבר. כל יכולת ניתנת במפורש.

**הרשאות מערכת** (system privileges) — מה מותר לעשות **בבסיס הנתונים** באופן כללי:

| ההרשאה | מאפשרת |
|---------|---------|
| `CREATE SESSION` | להתחבר |
| `CREATE TABLE` | ליצור טבלאות **בסכמה שלו** |
| `CREATE VIEW` | ליצור Views |
| `CREATE SEQUENCE` | ליצור sequences |
| `CREATE USER` | ליצור משתמשים — למנהלים בלבד |
| `SELECT ANY TABLE` | לקרוא **כל** טבלה של **כל** משתמש — מסוכן |

</div>

```sql
ALTER USER noa IDENTIFIED BY "N3w!Passw0rd";   -- change password
ALTER USER noa ACCOUNT LOCK;                   -- Noa left the shelter: lock, don't delete
DROP USER noa CASCADE;                         -- delete the user AND everything she owns
```

<div dir="rtl">

---

## 4. הרשאות אובייקט — GRANT ו‑REVOKE

**הרשאות אובייקט** (object privileges) — מה מותר לעשות על **טבלה / View / sequence מסוימים**:

</div>

```sql
-- the owner (user SHELTER) gives Noa permission to READ the animal table
GRANT SELECT ON shelter.animal TO noa;

-- the vet may read animals and ADD vaccinations
GRANT SELECT         ON shelter.animal      TO dr_ron;
GRANT SELECT, INSERT ON shelter.vaccination TO dr_ron;

-- may update only specific columns
GRANT UPDATE (weight_kg, status) ON shelter.animal TO dr_ron;

-- take it back
REVOKE INSERT ON shelter.vaccination FROM dr_ron;
```

<div dir="rtl">

| ההרשאה | על | מאפשרת |
|---------|-----|---------|
| `SELECT` | טבלה, View | לקרוא |
| `INSERT` | טבלה, View | להוסיף שורות |
| `UPDATE` (אפשר עם עמודות) | טבלה, View | לשנות |
| `DELETE` | טבלה, View | למחוק |
| `REFERENCES` | טבלה | ליצור מפתח זר שמצביע עליה |
| `ALL` | — | הכול. **כמעט אף פעם** |

### 4.1 `WITH GRANT OPTION`

</div>

```sql
GRANT SELECT ON shelter.animal TO ruti WITH GRANT OPTION;
-- now Ruti may grant SELECT on animal to others
```

<div dir="rtl">

> ⚠️ **זהירות:** `WITH GRANT OPTION` מעביר את השליטה הלאה. מי שקיבל — יכול לתת לכל מי שירצה, ואתם כבר לא יודעים מי רואה מה.

### 4.2 `PUBLIC`

</div>

```sql
GRANT SELECT ON shelter.species TO PUBLIC;     -- every user, now and in the future
```

<div dir="rtl">

מתאים לטבלאות קוד לא רגישות (מינים, סוגי חיסונים). **לעולם** לא לטבלה עם מידע אישי.

---

## 5. תפקידים (Roles)

20 מתנדבים, וכל אחד צריך את אותן 5 הרשאות = 100 פקודות `GRANT`. מתנדב חדש — עוד 5. שינוי בהרשאות — 20 × שינוי. **תפקיד** (role) הוא קבוצת הרשאות עם שם:

</div>

```sql
-- 1. define the role once
CREATE ROLE volunteer_role;
GRANT CREATE SESSION              TO volunteer_role;
GRANT SELECT ON shelter.available_animal TO volunteer_role;
GRANT SELECT ON shelter.public_person    TO volunteer_role;
GRANT INSERT ON shelter.walk             TO volunteer_role;

-- 2. give the role to people
GRANT volunteer_role TO noa;
GRANT volunteer_role TO amir;
GRANT volunteer_role TO tamar;

-- 3. a change in the role changes it for everyone
GRANT SELECT ON shelter.kennel TO volunteer_role;      -- all volunteers can now see kennels
```

```text
                      +--> SELECT available_animal
   noa   --+          |
   amir  --+--> volunteer_role --+--> SELECT public_person
   tamar --+                     |
                                 +--> INSERT walk
```

<div dir="rtl">

> 🔑 **בארגון אמיתי כמעט אף פעם לא נותנים הרשאות לאנשים — רק לתפקידים.** "מה מותר למתנדב?" — עונים במקום אחד. מתנדב חדש — `GRANT volunteer_role`. מתנדב עוזב — `REVOKE volunteer_role`.

---

## 6. View + GRANT — רק מה שצריך

`GRANT SELECT ON person` נותן גישה ל**כל** העמודות ו**כל** השורות. איך נותנים רק חלק? **View** (מודול 28):

</div>

```sql
-- only the columns volunteers may see -- no phone, no last name
CREATE VIEW public_person AS
SELECT person_id, first_name, city, role FROM person;

-- only the rows: available animals
CREATE VIEW available_animal AS
SELECT animal_id, name, species_id, breed, sex, weight_kg FROM animal WHERE status = 'available';

GRANT SELECT ON public_person    TO volunteer_role;
GRANT SELECT ON available_animal TO volunteer_role;
-- and NOTHING on person or animal themselves
```

<div dir="rtl">

המתנדבים שואלים את ה‑Views; אין להם הרשאה לטבלאות. גם אם ינסו `SELECT phone FROM person` — `ORA-00942: table or view does not exist` (מבחינתם, הטבלה פשוט לא קיימת).

> 🔑 **View = מה רואים. GRANT = מי רואה.** יחד הם מערכת האבטחה הבסיסית של כל בסיס נתונים.

---

## 7. העיקרון: הרשאה מינימלית

**Principle of Least Privilege** — כל משתמש מקבל **בדיוק** את ההרשאות שהוא צריך לעבודה שלו, ולא יותר.

| ❌ במקום | ✅ עדיף |
|---------|---------|
| האתר מתחבר כמנהל | משתמש לאתר עם `SELECT` על View אחד |
| `GRANT ALL ON animal` | `GRANT SELECT, INSERT` — רק מה שצריך |
| `SELECT ANY TABLE` | `SELECT` על טבלאות מסוימות |
| עובד שעזב — "נמחק אחר כך" | `ACCOUNT LOCK` ביום שעזב |
| סיסמה משותפת לכולם | משתמש לכל אדם — כך יודעים מי עשה מה |

> 🎬 **למה זה חשוב:** בפריצות רבות לאתרים, התוקף מגיע לבסיס הנתונים **דרך האפליקציה** — למשל בהזרקת SQL (SQL Injection). אם האפליקציה מתחברת כמשתמש עם כל ההרשאות — התוקף מקבל את כולן. אם היא מתחברת עם `SELECT` על View אחד — זה כל מה שהוא יכול לראות. **הרשאה מינימלית לא מונעת פריצה; היא מקטינה את הנזק.**

---

## 8. ביטויים רגולריים

`LIKE` (מודול 17) יודע שני דברים: `%` (כל רצף) ו‑`_` (תו אחד). **ביטוי רגולרי** (regular expression, regex) הוא שפה שלמה לתיאור תבניות טקסט: "טלפון ישראלי תקין", "שם שמתחיל באות גדולה", "רק ספרות".

### 8.1 התחביר הבסיסי

</div>

```text
   ^        start of the text                ^05         starts with "05"
   $        end of the text                  na$         ends with "na"
   .        any one character                L..a        L, any two, a
   [abc]    one of these characters          [aeiou]     a vowel
   [0-9]    a range                          [A-Z]       an uppercase letter
   [^0-9]   NOT one of these                 [^0-9]      not a digit
   *        0 or more of the previous        a*
   +        1 or more                        [0-9]+      one or more digits
   ?        0 or 1 (optional)                -?          an optional dash
   {n}      exactly n times                  [0-9]{7}    exactly 7 digits
   |        or                               cat|dog
```

```text
   Israeli mobile phone:   ^05[0-9]-?[0-9]{7}$
                           ^          start
                           05         "05"
                           [0-9]      one more digit  (050, 052, 054 ...)
                           -?         an optional dash
                           [0-9]{7}   exactly 7 digits
                           $          end
   matches:  052-1111111   0521111111
   no match: 52-1111111   052-111111   052-11111111   +972-52-1111111
```

<div dir="rtl">

### 8.2 ב‑Oracle

</div>

```sql
-- people whose phone is NOT a valid Israeli mobile number
SELECT first_name, phone
FROM   person
WHERE  NOT REGEXP_LIKE(phone, '^05[0-9]-?[0-9]{7}$');

-- names that start with a letter from A to M
SELECT name FROM animal WHERE REGEXP_LIKE(name, '^[A-M]');

-- remove everything that is not a digit:  '052-111 1111' -> '0521111111'
SELECT REGEXP_REPLACE(phone, '[^0-9]', '') FROM person;

-- extract the first number from a text:  'dry food, 20 sacks' -> '20'
SELECT REGEXP_SUBSTR(description, '[0-9]+') FROM expense;

-- a CHECK constraint with a regex (module 27): only valid phones may enter
ALTER TABLE person ADD CONSTRAINT chk_phone CHECK (REGEXP_LIKE(phone, '^05[0-9]-?[0-9]{7}$'));
```

<div dir="rtl">

| הפונקציה | מה היא עושה |
|-----------|-------------|
| `REGEXP_LIKE(x, p)` | האם `x` מתאים לתבנית (`WHERE`, `CHECK`) |
| `REGEXP_REPLACE(x, p, r)` | מחליף כל התאמה ב‑`r` |
| `REGEXP_SUBSTR(x, p)` | מחזיר את ההתאמה הראשונה |
| `REGEXP_INSTR(x, p)` | המיקום של ההתאמה |
| `REGEXP_COUNT(x, p)` | כמה התאמות |

### 8.3 ב‑SQLite: `GLOB`

ב‑SQLite אין `REGEXP_LIKE`. (האופרטור `REGEXP` קיים רק אם הכלי טוען הרחבה — בכלי שורת הפקודה `sqlite3` כן, וגם ב‑OneCompiler, שבדקנו.) **מה שקיים תמיד — `GLOB`**: באמצע הדרך בין `LIKE` ל‑regex.

</div>

```sql
-- valid phones: 05X-XXXXXXX   ([0-9] = one digit, written 7 times -- GLOB has no {7})
SELECT first_name, phone
FROM   person
WHERE  phone GLOB '05[0-9]-[0-9][0-9][0-9][0-9][0-9][0-9][0-9]';
-- 11 people. The 12th, Omer, has no phone (NULL).

-- names with two vowels in a row
SELECT name FROM animal WHERE name GLOB '*[aeiou][aeiou]*';     -- Zoe, Charlie, Daisy

-- titles: names that start with "Dr."
SELECT first_name FROM person WHERE first_name GLOB 'Dr.*';     -- Dr. Ron, Dr. Maya
```

<div dir="rtl">

| | `LIKE` | `GLOB` (SQLite) | regex (Oracle) |
|---|---|---|---|
| כל רצף | `%` | `*` | `.*` |
| תו אחד | `_` | `?` | `.` |
| קבוצת תווים | ❌ | `[0-9]`, `[^a]` | `[0-9]`, `[^a]` |
| חזרות (`{7}`, `+`) | ❌ | ❌ | ✅ |
| אותיות גדולות/קטנות | לא רגיש | **רגיש** | רגיש (אלא עם `'i'`) |

> 💡 **שימו לב:** ב‑`GLOB` התו `.` הוא נקודה רגילה; ב‑regex הוא "כל תו". `'Dr.*'` ב‑`GLOB` = "מתחיל ב‑Dr.". ב‑regex היה צריך `'^Dr\.'`.

---

## 9. חיפוש עבודה

תכנית הלימודים מסיימת את חלק ה‑SQL בהכנה לעולם העבודה. מה שלמדתם בקורס הזה הוא בסיס לכמה כיווני קריירה (ראו גם מודול 19, סעיף 9):

### 9.1 איפה ה‑SQL שלכם שווה משהו

| התפקיד | מה מחפשים בג'וניור | מה מהקורס הכי רלוונטי |
|---------|---------------------|-------------------------|
| **אנליסט/ית נתונים** | `JOIN`, `GROUP BY`, פונקציות תאריך, אקסל/BI | מודולים 21–24 |
| **מפתח/ת Back-end** | עיצוב טבלאות, אילוצים, שאילתות מהירות | 6, 12, 26–29 |
| **בודק/ת תוכנה (QA)** | לאמת נתונים ישירות בבסיס הנתונים | 17–24, 27 |
| **תמיכה טכנית / יישום מערכות** | לשלוף מידע ללקוח, לתקן נתונים בזהירות | 25, 32 |
| **DBA ג'וניור** | גיבויים, הרשאות, אינדקסים, ביצועים | 29, 30, 32 |

### 9.2 תוכנית בארבעה צעדים

1. **תיק עבודות:** פרויקט הגמר שלכם (מודולים 9, 15, 31) — ERD, סקריפט `CREATE` + `INSERT`, ועשר שאילתות שעונות על שאלות אמיתיות. העלו ל‑GitHub עם README קצר. **מעסיקים רוצים לראות קוד, לא רק לשמוע.**
2. **קורות חיים:** תחת "כישורים" — לא רק "SQL", אלא מה ספציפית: "עיצוב ERD ונרמול, JOIN ו‑GROUP BY, Views, אילוצים, SQLite ו‑Oracle". קישור לפרויקט.
3. **תרגול:** אתרים כמו SQLZoo, HackerRank (SQL) ו‑LeetCode (Database) — שאלות בסגנון ראיונות. 20 דקות ביום.
4. **ראיון:** חזרו על "ראיון בכיתה" ממודול 29. **חשבו בקול.**

> 💡 **הסמכה:** Oracle מציעה הסמכת **Oracle Database SQL Certified Associate** (מבחן 1Z0‑071). התוכן קרוב מאוד לחלק ב' של הקורס הזה — במודול 32 נחזור אליה.

---

## 10. סיכום המודול

<div align="center">

### 🧠 שש נקודות

</div>

1. **משתמשים והרשאות** קובעים מי עושה מה. SQLite = קובץ, בלי משתמשים. Oracle = שרת, עם `GRANT`.
2. **הרשאות מערכת** (`CREATE SESSION`, `CREATE TABLE`) מול **הרשאות אובייקט** (`SELECT`, `INSERT`, `UPDATE`, `DELETE` על טבלה מסוימת).
3. **`GRANT … TO`** / **`REVOKE … FROM`**. `WITH GRANT OPTION` — בזהירות. `PUBLIC` — רק לנתונים לא רגישים.
4. **Roles** — הרשאות לתפקיד, תפקיד לאנשים. **View + GRANT** — רק העמודות והשורות הנחוצות.
5. **הרשאה מינימלית** — לא מונעת פריצה, מקטינה נזק.
6. **Regex** (Oracle: `REGEXP_LIKE`, `REGEXP_REPLACE`, `REGEXP_SUBSTR`) לתבניות מורכבות; ב‑SQLite — `GLOB`.

<div align="center">

---

*"הנתונים הכי מוגנים הם אלה*
*שמי שלא צריך אותם — לא יכול לראות."*

---

</div>

## 📎 המשך

| | |
|---|---|
| ❓ | [שאלות ותשובות](questions.md) |
| ✏️ | [תרגילים](exercises.md) |
| ✅ | [פתרונות](solutions.md) |
| ⬅️ | [מודול 29 — SQL: אובייקטים נוספים](../module-29-sql-objects/) |
| ➡️ | [מודול 31 — SQL: פרויקט מסכם](../module-31-sql-final-project/) |
| 🏠 | [חזרה לדף הקורס](../../) |

</div>
