<div dir="rtl">

# מודול 20 — SQL: פונקציות 2

> **פרק 20 בתכנית הלימודים** · 3 שעות עיוני + 2 שעות מעשי
> **נושאים:** פונקציות המרה · פונקציות NULL · ביטויי תנאי

> 🧭 **במסלול המשולב:** יחידה 4, לצד [מודול 4 — טיפוסי משנה וטיפוסי על](../module-04-subtypes-supertypes/), אחרי [מודול 19](../module-19-sql-functions/).

---

## 🎯 מה תדעו בסוף המודול

- [ ] להסביר מה זו **המרת טיפוס**, ומתי SQL ממיר לבד (ומתי זה מסוכן)
- [ ] להמיר במפורש עם `CAST` — ולהכיר את `TO_CHAR` / `TO_NUMBER` / `TO_DATE` של Oracle
- [ ] להחליף NULL בערך ברירת מחדל עם `COALESCE`
- [ ] להפוך ערך ל‑NULL עם `NULLIF` — ולמנוע חלוקה באפס
- [ ] לכתוב ביטוי `CASE` — בצורה הפשוטה ובצורה המחפשת
- [ ] להשתמש ב‑`CASE` ב‑`SELECT`, ב‑`WHERE` וב‑`ORDER BY`
- [ ] לקשר בין `CASE` לבין **טיפוסי משנה** ממודול 4

---

## 🗺️ מפת המודול

| # | הסעיף |
|---|--------|
| 1 | [טיפוסים והמרות](#1-טיפוסים-והמרות) |
| 2 | [`CAST` — המרה מפורשת](#2-cast--המרה-מפורשת) |
| 3 | [`COALESCE` — ערך במקום NULL](#3-coalesce--ערך-במקום-null) |
| 4 | [`NULLIF` — NULL במקום ערך](#4-nullif--null-במקום-ערך) |
| 5 | [`CASE` הפשוט](#5-case-הפשוט) |
| 6 | [`CASE` המחפש](#6-case-המחפש) |
| 7 | [`CASE` ב‑WHERE וב‑ORDER BY](#7-case-בwhere-ובorder-by) |
| 8 | [`CASE` וטיפוסי משנה](#8-case-וטיפוסי-משנה) |
| 9 | [SQLite מול Oracle](#9-sqlite-מול-oracle) |
| 10 | [דוגמה מלאה — סוג התשלום על כל אימוץ](#10-דוגמה-מלאה--סוג-התשלום-על-כל-אימוץ) |
| 11 | [חמש טעויות נפוצות](#11-חמש-טעויות-נפוצות) |
| 12 | [סיכום המודול](#12-סיכום-המודול) |

---

## 1. טיפוסים והמרות

לכל ערך ב‑SQL יש **טיפוס**: מספר שלם, מספר עשרוני, טקסט, תאריך. כשמשלבים שני טיפוסים שונים — מישהו צריך להחליט מה יוצא.

</div>

```sql
SELECT '10' + 5          AS a,     -- 15   text was converted to a number
       '10' || 5         AS b,     -- 105  the number was converted to text
       '9' < '10'        AS c;     -- 0    (false!) text compares letter by letter
```

```text
a   b    c
--  ---  -
15  105  0
```

<div dir="rtl">

**שני סוגי המרה:**

| הסוג | מי ממיר | דוגמה | הבעיה |
|------|---------|--------|--------|
| **מרומזת** (implicit) | בסיס הנתונים, לבד | `'10' + 5` | לא תמיד ברור מה יקרה — ושונה בין מערכות |
| **מפורשת** (explicit) | אתם, בפונקציה | `CAST('10' AS INTEGER) + 5` | אין — כתוב בדיוק מה רציתם |

> 🔑 **כלל המקצוע:** אל תסמכו על המרה מרומזת. אם צריך מספר — המירו למספר. אם צריך טקסט — המירו לטקסט. הקוד ארוך במילה אחת וקריא פי כמה.

> 🎬 **סיפור מהשטח: "10" לפני "9"**
>
> מערכת הזמנות שמרה מספרי חדרים כטקסט. דוח "חדרים לפי מספר" הציג: 1, 10, 11, 12, 2, 20, 3… כי טקסט מושווה **תו אחר תו**: `'1'` < `'2'`, ולכן `'10'` < `'2'`. התיקון: `ORDER BY CAST(room AS INTEGER)`. התיקון האמיתי: לשמור מספרים בעמודת מספר — מודול 26.

---

## 2. `CAST` — המרה מפורשת

</div>

```sql
CAST(value AS type)
```

```sql
SELECT CAST('42' AS INTEGER) + 1   AS c,     -- 43
       CAST(18.9 AS INTEGER)       AS d,     -- 18   (cuts, does NOT round)
       CAST(7 AS REAL) / 2         AS e;     -- 3.5  (not 3!)
```

<div dir="rtl">

| ההמרה | למה | דוגמה |
|--------|-----|--------|
| טקסט ⟵ מספר | חישוב על ערך שנשמר כטקסט | `CAST('42' AS INTEGER)` |
| עשרוני ⟵ שלם | **קיצוץ** הספרות אחרי הנקודה | `CAST(18.9 AS INTEGER)` = `18` |
| שלם ⟵ עשרוני | למנוע חלוקת שלמים (מודול 16) | `CAST(7 AS REAL) / 2` = `3.5` |
| מספר ⟵ טקסט | חיבור למחרוזת, או `COALESCE` עם טקסט | `CAST(animal_id AS TEXT)` |

> ⚠️ **`CAST(18.9 AS INTEGER)` הוא 18, לא 19.** `CAST` **חותך**. לעיגול — `ROUND` (מודול 19). לגיל — דווקא החיתוך הוא מה שרוצים: מי שנולד לפני 5.9 שנים הוא בן 5.

### 2.1 המרה עם תאריכים

ב‑SQLite אין טיפוס תאריך נפרד — תאריכים נשמרים כטקסט בפורמט `YYYY-MM-DD`, ופונקציות התאריך (מודול 19) יודעות לקרוא אותו. **לכן כל ההמרות הן `STRFTIME`.**

</div>

```sql
-- year as a NUMBER (STRFTIME returns text)
SELECT adoption_date,
       CAST(STRFTIME('%Y', adoption_date) AS INTEGER) + 1 AS next_year
FROM   adoption
WHERE  adoption_id IN (1, 7);
```

```text
adoption_date  next_year
-------------  ---------
2023-05-10     2024
2025-07-01     2026
```

<div dir="rtl">

### 2.2 ב‑Oracle: שלוש פונקציות המרה

ב‑Oracle יש טיפוס `DATE` אמיתי, ולכן ההמרות מפורשות יותר. **זה מה שיופיע ב‑APEX ובמבחנים המבוססים על Oracle:**

</div>

```text
   TO_CHAR(value, format)     number/date  --> text
   TO_NUMBER(text)            text         --> number
   TO_DATE(text, format)      text         --> date

   TO_CHAR(SYSDATE, 'DD/MM/YYYY')         -->  '21/09/2026'
   TO_CHAR(1850, '9,999.00')              -->  ' 1,850.00'
   TO_NUMBER('42') + 1                    -->  43
   TO_DATE('15/03/2024', 'DD/MM/YYYY')    -->  a real DATE value
```

<div dir="rtl">

| מה | SQLite | Oracle |
|----|--------|--------|
| טקסט ⟵ מספר | `CAST(x AS INTEGER)` | `TO_NUMBER(x)` |
| מספר ⟵ טקסט | `CAST(x AS TEXT)` | `TO_CHAR(x)` |
| תאריך ⟵ טקסט מעוצב | `STRFTIME('%d/%m/%Y', d)` | `TO_CHAR(d, 'DD/MM/YYYY')` |
| טקסט ⟵ תאריך | `DATE('2024-03-15')` | `TO_DATE('15/03/2024', 'DD/MM/YYYY')` |

---

## 3. `COALESCE` — ערך במקום NULL

במודול 19 ראינו שכרטיס החיה של Coco ריק: אין תאריך לידה, אז גם הגיל NULL. הגיע הזמן לתקן.

</div>

```text
   COALESCE(a, b, c, ...)   -->  the FIRST value that is NOT NULL

   COALESCE(NULL, 'x')           -->  'x'
   COALESCE('Tabby', 'x')        -->  'Tabby'
   COALESCE(NULL, NULL, 'z')     -->  'z'
   COALESCE(NULL, NULL)          -->  NULL   (nothing to fall back to)
```

```sql
SELECT name, breed, COALESCE(breed, 'unknown') AS breed_label
FROM   animal
WHERE  species_id = 2;
```

```text
name   breed    breed_label
-----  -------  -----------
Simba  Tabby    Tabby
Mitzi           unknown
Tom    Siamese  Siamese
Nala            unknown
Oscar  Persian  Persian
Lily            unknown
Felix  Tabby    Tabby
```

<div dir="rtl">

### 3.1 יותר משתי אפשרויות

`COALESCE` עובר משמאל לימין ועוצר בערך הראשון שאינו NULL:

</div>

```sql
-- best available identifier: chip -> breed -> 'no info'
SELECT name, COALESCE(chip_number, breed, 'no info') AS id_info
FROM   animal
WHERE  animal_id IN (1, 4, 7, 14);
```

```text
name   id_info
-----  ---------
Luna   985100001     <- has a chip
Mitzi  no info       <- no chip, no breed
Coco   Cockatiel     <- no chip, but a breed
Lily   no info
```

<div dir="rtl">

### 3.2 הכרטיס של מודול 19 — מתוקן

</div>

```sql
SELECT name,
       COALESCE(
         CAST(FLOOR((JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25) AS INTEGER),
         'unknown') AS age
FROM   animal
WHERE  status = 'available'
ORDER  BY name;
```

```text
name    age
------  -------
Bunny   2
Coco    unknown
Felix   7
Lily    unknown
Mitzi   3
Oscar   4
Rex     9
Rocky   6
Shadow  5
```

<div dir="rtl">

> ⚠️ **ערבוב טיפוסים:** בעמודה הזאת יש גם מספרים וגם הטקסט `'unknown'`. SQLite מרשה; **Oracle לא** — שם כל הערכים ב‑`COALESCE` חייבים להיות מאותו טיפוס: `COALESCE(TO_CHAR(age), 'unknown')`. הרגל טוב בכל מקום: **המירו קודם, ואז `COALESCE`.**

### 3.3 `COALESCE` לא משנה את הטבלה

`breed` של Mitzi **עדיין NULL** בטבלה. `COALESCE` משנה רק את מה ש**מוצג** בתוצאה. זה בדיוק מה שרוצים: הנתון האמיתי ("לא ידוע") נשמר, והתצוגה ידידותית.

> 🔑 **מודול 7 + 16:** NULL אינו טעות — הוא המידע "לא ידוע". אל תכניסו `'unknown'` לטבלה עצמה; הציגו אותו עם `COALESCE`.

---

## 4. `NULLIF` — NULL במקום ערך

ההפך של `COALESCE`: מקבל שני ערכים, ומחזיר NULL **אם הם שווים**.

</div>

```text
   NULLIF(a, b)   -->  NULL  if a = b
                  -->  a     otherwise

   NULLIF(400, 400)  -->  NULL
   NULLIF(300, 400)  -->  300
```

<div dir="rtl">

### 4.1 השימוש הקלאסי: חלוקה באפס

</div>

```sql
-- price per kg; a weight of 0 would crash the report in Oracle
SELECT 100 / NULLIF(0, 0) AS safe_div;     -- NULL instead of an error
```

<div dir="rtl">

`x / NULLIF(y, 0)`: אם `y` הוא 0, המכנה הופך ל‑NULL, והתוצאה NULL ("אי אפשר לחשב") — במקום שגיאה שמפילה את כל הדוח.

> 💡 ב‑SQLite חלוקה ב‑0 מחזירה NULL גם בלי `NULLIF`. ב‑Oracle, PostgreSQL ו‑SQL Server — **שגיאה**. כתבו `NULLIF` תמיד; הקוד יעבוד בכל מקום.

### 4.2 שימוש שני: להסתיר ערך "רגיל"

</div>

```sql
-- show only the fees that were NOT the standard 400
SELECT adoption_id, fee_paid, NULLIF(fee_paid, 400) AS not_full
FROM   adoption;
```

```text
adoption_id  fee_paid  not_full
-----------  --------  --------
1            300.0     300.0
2            200.0     200.0
3            200.0     200.0
4            250.0     250.0
5            100.0     100.0
6            200.0     200.0
7            400.0              <- standard fee: hidden
8            400.0
9            150.0     150.0
```

<div dir="rtl">

---

## 5. `CASE` הפשוט

`CASE` הוא ה‑`if` של SQL: מחזיר ערך שונה לפי תנאי. בצורה ה**פשוטה** — משווים עמודה אחת לרשימת ערכים:

</div>

```sql
CASE column
  WHEN value1 THEN result1
  WHEN value2 THEN result2
  ELSE default_result
END
```

```sql
SELECT name, species_id,
       CASE species_id
         WHEN 1 THEN 'dog'
         WHEN 2 THEN 'cat'
         WHEN 3 THEN 'rabbit'
         ELSE 'other'
       END AS kind
FROM   animal
WHERE  animal_id <= 8;
```

```text
name   species_id  kind
-----  ----------  -----
Luna   1           dog
Simba  2           cat
Rocky  1           dog
Mitzi  2           cat
Bella  1           dog
Tom    2           cat
Coco   4           other
Max    1           dog
```

<div dir="rtl">

**ארבעה חוקים:**

1. `CASE` הוא **ביטוי** — הוא מחזיר ערך אחד לכל שורה, ולכן עומד בכל מקום שמותר ערך.
2. נבדק **לפי הסדר**; ה‑`WHEN` הראשון שמתאים — מנצח.
3. אם אף `WHEN` לא מתאים ואין `ELSE` — התוצאה **NULL**.
4. תמיד נגמר ב‑`END`. ותמיד כדאי לתת לו שם עם `AS`.

> 💡 **"אבל יש טבלת `species`!"** נכון — ובקוד אמיתי מביאים את השם ב‑`JOIN` (מודול 21), לא מקודדים אותו ב‑`CASE`. `CASE` מתאים לערכים **שאין להם טבלה**: תוויות תצוגה, קטגוריות מחושבות, תרגומים.

---

## 6. `CASE` המחפש

בצורה ה**מחפשת** (searched), כל `WHEN` הוא תנאי מלא — עם `<`, `>`, `AND`, `IS NULL`, כל מה שמותר ב‑`WHERE`:

</div>

```sql
SELECT name, birth_date,
       CASE
         WHEN birth_date IS NULL THEN 'unknown'
         WHEN (JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25 < 2 THEN 'puppy'
         WHEN (JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25 < 8 THEN 'adult'
         ELSE 'senior'
       END AS life_stage
FROM   animal
WHERE  species_id = 1
ORDER  BY birth_date;
```

```text
name     birth_date  life_stage
-------  ----------  ----------
Zoe      2016-01-01  senior
Rex      2017-08-08  senior
Bella    2018-05-05  senior
Rocky    2019-11-20  adult
Daisy    2020-04-04  adult
Luna     2021-03-15  adult
Shadow   2021-06-30  adult
Max      2022-02-28  adult
Charlie  2023-10-10  adult      <- 2.95 years: just missed "puppy"
```

<div dir="rtl">

### 6.1 ⚠️ הסדר קובע

`CASE` עוצר ב‑`WHEN` **הראשון** שמתקיים. סדר לא נכון — תוצאה שגויה, **בלי שום שגיאה**:

</div>

```sql
-- WRONG order: every animal over 5 kg stops at the first WHEN
SELECT name, weight_kg,
       CASE WHEN weight_kg > 5  THEN 'large'
            WHEN weight_kg > 20 THEN 'huge'      -- never reached!
            ELSE 'small' END AS bad
FROM   animal
WHERE  animal_id IN (3, 13);
```

```text
name   weight_kg  bad
-----  ---------  -----
Rocky  31.0       large     <- should be "huge"
Rex    38.7       large
```

<div dir="rtl">

> 🔑 **כלל:** בטווחים — מהקיצוני אל הכללי. `> 20` לפני `> 5`. או מהקטן לגדול עם `<`, כמו בדוגמת הגיל. **ואל תשכחו `WHEN … IS NULL`:** כל השוואה עם NULL אינה true, אז בלי השורה הזאת NULL נופל ל‑`ELSE` ומקבל תווית שגויה (Coco הייתה הופכת ל‑`'senior'`). נוהגים לשים אותה ראשונה — כך רואים מיד שטיפלתם ב‑NULL.

### 6.2 `IIF` — קיצור לשתי אפשרויות

כשיש רק "כן / לא", SQLite (ו‑SQL Server) מציעים קיצור:

</div>

```sql
SELECT name, IIF(chip_number IS NULL, 'no chip', 'has chip') AS chip
FROM   animal
WHERE  animal_id <= 4;
-- IIF(condition, if_true, if_false)  =  CASE WHEN condition THEN if_true ELSE if_false END
```

<div dir="rtl">

> 💡 **ב‑Oracle אין `IIF`.** יש `DECODE(col, v1, r1, v2, r2, default)` — גרסה ישנה של `CASE` הפשוט. בקוד חדש: `CASE` — עובד בכל מקום.

---

## 7. `CASE` ב‑WHERE וב‑ORDER BY

### 7.1 מיון בסדר "עסקי"

רותי רוצה רשימה שבה **החיות שצריכות טיפול** למעלה: קודם טיפול רפואי, אחר כך הסגר, אחר כך הזמינות לאימוץ, ובסוף כל השאר. זה לא סדר אלפביתי ולא מספרי — **`CASE` הופך אותו למספר:**

</div>

```sql
SELECT name, status
FROM   animal
ORDER  BY CASE status
            WHEN 'medical'    THEN 1
            WHEN 'quarantine' THEN 2
            WHEN 'available'  THEN 3
            ELSE 4
          END,
          name
LIMIT  6;
```

```text
name   status
-----  ----------
Max    medical
Nala   quarantine
Bunny  available
Coco   available
Felix  available
Lily   available
```

<div dir="rtl">

### 7.2 תנאי מורכב ב‑WHERE

</div>

```sql
-- medical expenses of 1,000 or more need the manager's approval
SELECT category, amount,
       CASE WHEN category = 'medical' AND amount >= 1000
            THEN 'needs approval' ELSE 'ok' END AS approval
FROM   expense
WHERE  category = 'medical'
ORDER  BY amount DESC
LIMIT  4;
```

```text
category  amount  approval
--------  ------  --------------
medical   2100.0  needs approval
medical   1200.0  needs approval
medical   890.0   ok
medical   650.0   ok
```

<div dir="rtl">

> 💡 אפשר לכתוב `CASE` גם בתוך `WHERE` — אבל בדרך כלל `AND` / `OR` רגילים קריאים יותר. השימוש העיקרי של `CASE` הוא ב‑`SELECT` (תוויות) וב‑`ORDER BY` (סדר עסקי). במודול 23 נראה שימוש שלישי חזק במיוחד: `SUM(CASE …)` — ספירה מותנית.

---

## 8. `CASE` וטיפוסי משנה

במודול 4 עיצבנו טיפוס‑על `PERSON` עם שלושה טיפוסי משנה: מתנדב, מאמץ ווטרינר. בבסיס הנתונים המוכן, שלושתם בטבלה **אחת** — ועמודת `role` אומרת לאיזה טיפוס משנה שייכת כל שורה. זו בדיוק "עמודת המבחין" (discriminator) ממודול 4.

</div>

```sql
SELECT first_name || ' ' || last_name AS person,
       CASE role
         WHEN 'vet'       THEN 'medical staff'
         WHEN 'volunteer' THEN 'volunteer'
         WHEN 'adopter'   THEN 'adopter'
       END AS role_label
FROM   person
WHERE  person_id IN (1, 4, 6);
```

```text
person        role_label
------------  -------------
Ruti Almog    volunteer
Dr. Ron Levi  medical staff
Dana Cohen    adopter
```

<div dir="rtl">

**ומה עם מאפיינים שקיימים רק לטיפוס משנה אחד?** בטבלת `intake`, לקליטה מסוג `stray` יש `location`, ולקליטה מסוג `surrender` יש `reason`. כל השאר NULL. `COALESCE` מאחד אותם לעמודה אחת:

</div>

```sql
SELECT intake_id, intake_type,
       COALESCE(location, reason, 'no details') AS details
FROM   intake
WHERE  intake_id IN (1, 2, 11, 21);
```

```text
intake_id  intake_type  details
---------  -----------  -----------------------------
1          stray        Herzl St, Haifa
2          surrender    moving abroad
11         transfer     transfer from Akko shelter
21         surrender    returned by adopter - allergy
```

<div dir="rtl">

> 🔑 **הקשר למודול 4:** כשטיפוסי משנה מאוחסנים בטבלה אחת, `CASE` על עמודת המבחין ו‑`COALESCE` על העמודות הייחודיות הם הדרך "לפרק" אותם בחזרה בשאילתה. כשמאחסנים כל טיפוס משנה בטבלה נפרדת — מחברים אותם ב‑`JOIN` (מודול 21) או ב‑`UNION` (מודול 24). **ההחלטה בעיצוב קובעת את ה‑SQL.**

---

## 9. SQLite מול Oracle

</div>

```text
+--------------------------+------------------------------+-------------------------------+
| WHAT                     | SQLite (OneCompiler)           | Oracle (APEX / exam)          |
+--------------------------+------------------------------+-------------------------------+
| convert type             | CAST(x AS INTEGER/REAL/TEXT) | CAST(x AS NUMBER/VARCHAR2(n)) |
| text -> number           | CAST(x AS INTEGER)           | TO_NUMBER(x)                  |
| number/date -> text      | CAST(x AS TEXT), STRFTIME    | TO_CHAR(x, 'format')          |
| text -> date             | DATE('2024-03-15')           | TO_DATE('15/03/2024',         |
|                          |                              |         'DD/MM/YYYY')         |
+--------------------------+------------------------------+-------------------------------+
| first non-NULL           | COALESCE(a, b, ...)          | same  (also NVL(a, b))        |
| two-value NULL default   | IFNULL(a, b)                 | NVL(a, b)                     |
| NULL ? x : y             | IIF(a IS NULL, y, x)         | NVL2(a, x, y)                 |
| NULL if equal            | NULLIF(a, b)                 | same                          |
+--------------------------+------------------------------+-------------------------------+
| conditional              | CASE ... END                 | same                          |
| short if                 | IIF(cond, a, b)              | (none -- use CASE)            |
| old-style simple CASE    | (none)                       | DECODE(x, v1, r1, ..., def)   |
+--------------------------+------------------------------+-------------------------------+
```

<div dir="rtl">

> 🔑 **`COALESCE`, `NULLIF` ו‑`CASE` עובדים זהה בכל המערכות.** את אלה כדאי לזכור בעל פה. `NVL`, `DECODE` ו‑`IIF` — לזהות כשרואים אותם.

---

## 10. דוגמה מלאה — סוג התשלום על כל אימוץ

רותי שואלת: *"על כל אימוץ — שילמו מחיר מלא, חצי מחיר, או תעריף ישן?"* (ב‑README של בסיס הנתונים: התעריף השתנה ב‑2024, ומעל גיל 8 — חצי מחיר.)

</div>

```sql
SELECT ad.adoption_id, a.name, ad.fee_paid, s.adoption_fee,
       CASE
         WHEN ad.fee_paid = s.adoption_fee     THEN 'full price'
         WHEN ad.fee_paid = s.adoption_fee / 2 THEN 'half price'
         ELSE 'old rate'
       END AS fee_type
FROM   adoption ad
JOIN   animal  a ON a.animal_id  = ad.animal_id
JOIN   species s ON s.species_id = a.species_id
ORDER  BY ad.adoption_id;
```

```text
adoption_id  name     fee_paid  adoption_fee  fee_type
-----------  -------  --------  ------------  ----------
1            Luna     300.0     400.0         old rate
2            Simba    200.0     250.0         old rate
3            Bella    200.0     400.0         half price
4            Tom      250.0     250.0         full price
5            Thumper  100.0     100.0         full price
6            Zoe      200.0     400.0         half price
7            Luna     400.0     400.0         full price
8            Charlie  400.0     400.0         full price
9            Kiwi     150.0     150.0         full price
```

<div dir="rtl">

> 💡 **ה‑`JOIN` כאן הוא הצצה למודול 21** — הוא מביא את התעריף הנוכחי מטבלת `species`. את ה‑`CASE` אתם כבר יודעים לקרוא.

> 🎬 **ומה השאילתה מגלה?** "תעריף ישן" הוא ניחוש — השאילתה **לא יודעת** מה היה התעריף ב‑2023, כי `species` שומרת רק את התעריף **הנוכחי**. זו בדיוק הבעיה שמודול 10 (מעקב אחר שינויים) פותר: טבלת היסטוריית מחירים. **שאילתה טובה חושפת חורים בעיצוב.**

---

## 11. חמש טעויות נפוצות

| # | הטעות | מה קורה | התיקון |
|---|-------|----------|---------|
| 1 | **סדר `WHEN` לא נכון** | `> 5` לפני `> 20` — אף אחד לא "huge" | מהקיצוני לכללי |
| 2 | **שוכחים `ELSE`** | ערך שלא כוסה מקבל NULL בשקט | תמיד `ELSE` — גם `ELSE 'other'` |
| 3 | **`CASE` בלי `END`** | שגיאת תחביר | כל `CASE` נסגר ב‑`END` |
| 4 | **`CAST(18.9 AS INTEGER)` לעיגול** | 18, לא 19 | `ROUND` לעיגול; `CAST` לקיצוץ |
| 5 | **שומרים `'unknown'` בטבלה במקום NULL** | `COUNT(breed)` סופר אותו; `IS NULL` לא מוצא | NULL בטבלה, `COALESCE` בתצוגה |

---

## 12. סיכום המודול

<div align="center">

### 🧠 שש נקודות

</div>

1. **המרה מרומזת** קורית לבד ומפתיעה (`'9' < '10'` הוא false). **המירו במפורש** עם `CAST`.
2. `CAST(x AS INTEGER)` **חותך**, לא מעגל. ב‑Oracle: `TO_NUMBER`, `TO_CHAR`, `TO_DATE`.
3. `COALESCE(a, b, …)` — הערך הראשון שאינו NULL. התצוגה ידידותית, הנתון נשאר מדויק.
4. `NULLIF(a, b)` — NULL אם שווים. `x / NULLIF(y, 0)` — חלוקה בטוחה.
5. `CASE` — ה‑if של SQL. פשוט (`CASE col WHEN …`) או מחפש (`CASE WHEN תנאי …`). **הראשון שמתאים מנצח**, ובלי `ELSE` — NULL.
6. `CASE` על עמודת מבחין + `COALESCE` על עמודות ייחודיות = הדרך לשאול **טיפוסי משנה** שמאוחסנים בטבלה אחת.

<div align="center">

---

*"NULL אומר את האמת: לא ידוע.*
*COALESCE ו‑CASE אומרים אותה בשפה שבן אדם מבין."*

---

</div>

## 📎 המשך

| | |
|---|---|
| ❓ | [שאלות ותשובות](questions.md) |
| ✏️ | [תרגילים](exercises.md) — על [בסיס הנתונים המוכן](../../resources/shelter-db/) |
| ✅ | [פתרונות](solutions.md) — עם הפלט האמיתי |
| ⬅️ | [מודול 19 — SQL: פונקציות](../module-19-sql-functions/) |
| 🧭 | [מסלול הלימוד](../../LEARNING-PATH.md) — יחידה 4 הושלמה; הבאה: מודול 5 + 21–22 |
| ➡️ | [מודול 21 — SQL: איחוד טבלאות](../module-21-sql-joins/) |
| 🏠 | [חזרה לדף הקורס](../../) |

</div>
