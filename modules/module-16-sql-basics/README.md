<div dir="rtl">

# מודול 16 — SQL: המשפט הראשון

> **פרק 16 בתכנית הלימודים** · 4 שעות עיוני + 2 שעות מעשי
> **נושאים:** האנטומיה של משפטי SQL · סביבת העבודה של אורקל · אפליקציות · טכנולוגיות מסדי נתונים רלציוניים

> 🧭 **במסלול המשולב:** יחידה 2, לצד [מודול 2 — מודל הנתונים](../module-02-data-model/). **זהו המודול הראשון שבו נוגעים במקלדת.**

---

## 🎯 מה תדעו בסוף המודול

- [ ] לטעון את [בסיס הנתונים המוכן](../../resources/shelter-db/) ל‑Programiz ולהריץ שאילתה
- [ ] לזהות את **החלקים** של משפט `SELECT` ולדעת מה כל אחד עושה
- [ ] לשלוף **עמודות נבחרות** ולא רק `*`
- [ ] לתת **כינוי** (alias) לעמודה
- [ ] לחשב ערכים **תוך כדי שליפה** — חשבון וחיבור מחרוזות
- [ ] להסיר כפילויות עם `DISTINCT`
- [ ] לפגוש **NULL** בפעם הראשונה — ולהבין למה הוא "מדביק" הכול
- [ ] לקרוא **הודעת שגיאה** ולהבין מה השתבש

---

## 🗺️ מפת המודול

| # | הסעיף |
|---|--------|
| 1 | [מה זה SQL — ולמה הוא נראה כמו אנגלית](#1-מה-זה-sql--ולמה-הוא-נראה-כמו-אנגלית) |
| 2 | [הכנת סביבת העבודה — 60 שניות](#2-הכנת-סביבת-העבודה--60-שניות) |
| 3 | [האנטומיה של SELECT](#3-האנטומיה-של-select) |
| 4 | [בחירת עמודות](#4-בחירת-עמודות) |
| 5 | [כינויים — לתת שם לתוצאה](#5-כינויים--לתת-שם-לתוצאה) |
| 6 | [חישובים תוך כדי שליפה](#6-חישובים-תוך-כדי-שליפה) |
| 7 | [DISTINCT — בלי כפילויות](#7-distinct--בלי-כפילויות) |
| 8 | [המפגש הראשון עם NULL](#8-המפגש-הראשון-עם-null) |
| 9 | [לקרוא הודעת שגיאה](#9-לקרוא-הודעת-שגיאה) |
| 10 | [כללי כתיבה — כדי שאפשר יהיה לקרוא](#10-כללי-כתיבה--כדי-שאפשר-יהיה-לקרוא) |
| 11 | [סביבת אורקל, אפליקציות והטכנולוגיה](#11-סביבת-אורקל-אפליקציות-והטכנולוגיה) |
| 12 | [דוגמה מלאה — סיור ראשון במקלט](#12-דוגמה-מלאה--סיור-ראשון-במקלט) |
| 13 | [חמש טעויות נפוצות](#13-חמש-טעויות-נפוצות) |
| 14 | [רשימת בדיקה](#14-רשימת-בדיקה) |
| 15 | [סיכום המודול](#15-סיכום-המודול) |

---

## 1. מה זה SQL — ולמה הוא נראה כמו אנגלית

<div align="center">

**SQL היא שפה לשאול שאלות. לא לתכנת — לשאול.**

</div>

בשפות תכנות רגילות אתם אומרים למחשב **איך** לעשות משהו: "עבור על כל השורות, בדוק כל אחת, אם היא כלב — שמור אותה". ב‑SQL אתם אומרים רק **מה** אתם רוצים:

</div>

```sql
SELECT name FROM animal WHERE species_id = 1;
```

<div dir="rtl">

*"תן לי את השם, מטבלת החיות, איפה שהמין הוא 1."* — ובסיס הנתונים כבר ימצא בעצמו את הדרך.

זה נקרא **שפה דקלרטיבית** — ובמודול 1 ראינו שזה בדיוק מה שקוד המציא ב‑1970: המתכנת לא צריך לדעת איך הנתונים מאוחסנים כדי לשאול עליהם.

> 🎬 **סיפור מהשטח: הפקידה שהקדימה את המתכנתים**
>
> בחברת ביטוח בינונית, כל בקשה לדוח הלכה לצוות הפיתוח. תור של שלושה שבועות.
>
> פקידה במחלקת תביעות, רחל, למדה SQL בקורס ערב. שבועיים אחרי, כשהמנהל שלה ביקש "כמה תביעות פתוחות מעל 10,000 ₪ יש לנו לפי סניף" — היא כתבה שורה אחת ושלחה תוך עשר דקות.
>
> תוך חצי שנה היא הפכה לאדם שכל המחלקה פונה אליו. תוך שנה קיבלה תפקיד חדש: אנליסטית.
>
> 🔑 **SQL אינה שפה של מתכנתים. היא שפה של מי שרוצה תשובות.** ובכל ארגון — מי שיכול לשאול את הנתונים ישירות, בלי תור, הוא בעל כוח.

---

## 2. הכנת סביבת העבודה — 60 שניות

הקורס עובד עם **Programiz Online SQL** — בדפדפן, בלי התקנה.

| # | הפעולה |
|---|---------|
| 1 | פתחו **[programiz.com/sql/online-compiler](https://www.programiz.com/sql/online-compiler/)** |
| 2 | מחקו את הקוד לדוגמה בחלון |
| 3 | פתחו את [`shelter.sql`](../../resources/shelter-db/shelter.sql), העתיקו **הכול**, והדביקו |
| 4 | לחצו **Run**. בתחתית צריך להופיע `animals_loaded = 20` |
| 5 | **מתחת** לקוד שהדבקתם — כתבו את השאילתה שלכם, ולחצו Run שוב |

> ⚠️ **Programiz לא זוכר בין ביקורים.** בכל פעם שפותחים — מדביקים את הקובץ מחדש. זה שלוש שניות. שמרו את השאילתות **שלכם** בקובץ אצלכם במחשב.

> 💡 **מה יש בבסיס הנתונים?** 8 טבלאות של מקלט "בית חם": `animal` · `species` · `person` · `intake` · `vaccination` · `vaccine_type` · `adoption` · `expense`. התיאור המלא ב‑[resources/shelter-db](../../resources/shelter-db/). במודול הזה נעבוד בעיקר עם `animal` ו‑`person`.

---

## 3. האנטומיה של SELECT

כל משפט `SELECT` בנוי מחלקים קבועים, **בסדר קבוע**. במודול הזה נפגוש את שני הראשונים. השאר יגיעו במודולים הבאים.

</div>

```text
SELECT   name, weight_kg          <-- WHAT to show     (module 16)
FROM     animal                   <-- from WHERE       (module 16)
WHERE    species_id = 1           <-- which ROWS       (module 17)
ORDER BY weight_kg DESC           <-- in what ORDER    (module 18)
;                                 <-- end of statement

  The order of the clauses is FIXED. You cannot write FROM before SELECT.
  You CAN skip clauses -- but the ones you keep stay in this order.
```

<div dir="rtl">

### 3.1 המשפט המינימלי

</div>

```sql
SELECT *
FROM   animal;
```

<div dir="rtl">

| החלק | מה הוא אומר |
|-------|--------------|
| `SELECT` | "תראה לי" |
| `*` | "את **כל** העמודות" |
| `FROM animal` | "מטבלת `animal`" |
| `;` | "זה סוף המשפט" |

**התוצאה:** כל 20 החיות, כל 9 העמודות. נסו את זה עכשיו.

### 3.2 התוצאה היא טבלה

זה הרעיון החשוב ביותר בפרק, ורוב הלומדים לא שמים לב אליו:

<div align="center">

**כל שאילתה מחזירה טבלה. גם אם יש בה שורה אחת. גם אם יש בה עמודה אחת.**

</div>

</div>

```text
   SELECT name, weight_kg FROM animal;

   INPUT: the animal table (20 rows x 9 columns)

   +----+-------+---------+-------+-----+------------+-----------+------------+-----------+
   | id | name  | species | breed | sex | birth_date | weight_kg | chip       | status    |
   +----+-------+---------+-------+-----+------------+-----------+------------+-----------+
   | 1  | Luna  | 1       | Mixed | F   | 2021-03-15 | 18.5      | 985100001  | adopted   |
   | 2  | Simba | 2       | Tabby | M   | 2022-07-01 | 4.2       | 985100002  | adopted   |
   | .. | ...   | ...     | ...   | ... | ...        | ...       | ...        | ...       |
   +----+-------+---------+-------+-----+------------+-----------+------------+-----------+

                                    |
                                    v

   OUTPUT: a NEW table (20 rows x 2 columns) -- the "result set"

   +-------+-----------+
   | name  | weight_kg |
   +-------+-----------+
   | Luna  | 18.5      |
   | Simba | 4.2       |
   | ...   | ...       |
   +-------+-----------+

   The original table is NOT changed. SELECT only READS.
```

<div dir="rtl">

> 🔑 **למה זה חשוב?** כי בהמשך נלמד לשים שאילתה **בתוך** שאילתה (תת‑שאילתה, מודול 24). זה עובד רק כי התוצאה של שאילתה היא טבלה — ואפשר לשאול טבלה.

---

## 4. בחירת עמודות

`*` נוח ללמידה — ורע לכל דבר אחר. בפועל תמיד מציינים **אילו** עמודות.

</div>

```sql
-- only the columns you need, in the order you want them
SELECT name, status, weight_kg
FROM   animal;
```

<div dir="rtl">

| למה לא `*` | ההסבר |
|-------------|--------|
| **ביצועים** | טבלה עם 40 עמודות ו‑2 מיליון שורות — `*` שולף הכול, גם מה שלא צריך |
| **יציבות** | מוסיפים עמודה לטבלה ⟵ כל `SELECT *` בקוד משתנה בלי שאף אחד התכוון |
| **קריאוּת** | מי שקורא את השאילתה בעוד שנה לא יודע מה חשוב |

**סדר העמודות** בתוצאה הוא הסדר שכתבתם ב‑`SELECT` — לא הסדר בטבלה:

</div>

```sql
SELECT weight_kg, name        -- weight first, then name
FROM   animal;
```

<div dir="rtl">

---

## 5. כינויים — לתת שם לתוצאה

עמודה בתוצאה יכולה לקבל **שם אחר** מהשם שלה בטבלה. זה נקרא **כינוי** (alias), ועושים את זה עם `AS`.

</div>

```sql
SELECT name      AS animal_name,
       weight_kg AS kg
FROM   animal;
```

<div dir="rtl">

**התוצאה:** אותם נתונים — אבל כותרות העמודות הן `animal_name` ו‑`kg`.

</div>

```sql
-- an alias with a space needs double quotes
SELECT name AS "Animal Name"
FROM   animal;

-- AS is optional -- this does the same thing (but is less readable)
SELECT name animal_name
FROM   animal;
```

<div dir="rtl">

| מתי משתמשים בכינוי | הדוגמה |
|---------------------|---------|
| שם העמודה טכני ולא ידידותי | `weight_kg` ⟵ `"משקל"` |
| התוצאה היא **חישוב** ואין לה שם | ראו סעיף 6 |
| שתי טבלאות עם עמודה באותו שם | מודול 21 — `JOIN` |

> 💡 **ההרגל הנכון:** תמיד `AS`. הוא אופציונלי, אבל בלעדיו `SELECT name animal_name` נראה כמו טעות.

---

## 6. חישובים תוך כדי שליפה

`SELECT` לא רק **מציג** עמודות — הוא יכול **לחשב**.

### 6.1 חשבון

</div>

```sql
SELECT name,
       weight_kg,
       weight_kg * 2.2 AS weight_lb      -- kilograms to pounds
FROM   animal;
```

<div dir="rtl">

| הפעולה | הסימן | דוגמה |
|---------|--------|--------|
| חיבור | `+` | `fee_paid + 50` |
| חיסור | `-` | `weight_kg - 1` |
| כפל | `*` | `weight_kg * 2.2` |
| חילוק | `/` | `amount / 12` |
| סוגריים | `( )` | `(fee_paid + 50) * 1.17` |

**סדר הפעולות** הוא כמו במתמטיקה: כפל וחילוק לפני חיבור וחיסור. סוגריים גוברים על הכול.

</div>

```sql
-- these give DIFFERENT results:
SELECT 100 + 20 * 2;      -- 140  (multiplication first)
SELECT (100 + 20) * 2;    -- 240  (parentheses first)
```

<div dir="rtl">

> ⚠️ **העמודה המקורית לא משתנה.** `weight_kg * 2.2` מחשב ערך **לתצוגה** — בטבלה `weight_kg` נשאר כפי שהיה. `SELECT` רק קורא.

### 6.2 חיבור מחרוזות

שתי עמודות טקסט אפשר **להדביק** יחד עם `||`:

</div>

```sql
SELECT first_name || ' ' || last_name AS full_name,
       role
FROM   person;
```

<div dir="rtl">

**התוצאה:**

</div>

```text
full_name       role
--------------  ---------
Ruti Almog      volunteer
Noa Peretz      volunteer
Amir Levi       volunteer
Dr. Ron Levi    vet
...
```

<div dir="rtl">

שימו לב ל‑`' '` באמצע — **רווח בתוך גרשיים**. בלעדיו תקבלו `RutiAlmog`.

</div>

```sql
-- text and numbers can be mixed
SELECT name || ' weighs ' || weight_kg || ' kg' AS description
FROM   animal;
-- -> "Luna weighs 18.5 kg"
```

<div dir="rtl">

> 💡 **גרשיים בודדות למחרוזות. גרשיים כפולות לכינויים.** `'text'` הוא ערך; `"Column Name"` הוא שם. לבלבל ביניהם היא הטעות הראשונה שכולם עושים.

---

## 7. DISTINCT — בלי כפילויות

</div>

```sql
SELECT status
FROM   animal;
```

<div dir="rtl">

**מחזיר 20 שורות** — `adopted`, `adopted`, `available`, `available`, `adopted`... כי יש 20 חיות.

אם רוצים לדעת **אילו** סטטוסים קיימים — כל אחד פעם אחת:

</div>

```sql
SELECT DISTINCT status
FROM   animal;
```

<div dir="rtl">

**התוצאה:**

</div>

```text
status
----------
adopted
available
medical
quarantine
deceased
```

<div dir="rtl">

**5 שורות.** `DISTINCT` הסיר את הכפילויות.

</div>

```sql
-- DISTINCT applies to the COMBINATION of all columns listed
SELECT DISTINCT species_id, status
FROM   animal;
-- -> every unique (species, status) pair
```

<div dir="rtl">

> 🔑 **מתי `DISTINCT` הוא דגל אדום:** אם אתם צריכים אותו כדי "לתקן" תוצאה שיצאה כפולה — לרוב הבעיה היא ב‑`JOIN` שגוי (מודול 21), לא בנתונים. `DISTINCT` מסתיר את הבעיה; הוא לא פותר אותה.

---

## 8. המפגש הראשון עם NULL

במודול 2 למדנו ש‑`NULL` פירושו **"אין ערך"** — לא אפס, לא מחרוזת ריקה, פשוט לא ידוע.

בבסיס הנתונים שלנו, לחלק מהחיות אין גזע ידוע:

</div>

```sql
SELECT name, breed
FROM   animal;
```

<div dir="rtl">

</div>

```text
name    breed
------  ----------------
Luna    Mixed
Simba   Tabby
Rocky   Labrador
Mitzi                     <- NULL: shown as empty
Bella   German Shepherd
...
```

<div dir="rtl">

### הכלל שמפתיע את כולם: NULL "מדביק"

</div>

```sql
SELECT name,
       weight_kg,
       weight_kg + 1 AS heavier
FROM   animal;
```

<div dir="rtl">

עובד מצוין — לכל החיות יש משקל. אבל נסו את זה:

</div>

```sql
SELECT name,
       'Breed: ' || breed AS label
FROM   animal;
```

<div dir="rtl">

</div>

```text
name    label
------  ----------------
Luna    Breed: Mixed
Simba   Breed: Tabby
Mitzi                     <- NOT "Breed: " -- the whole thing is NULL!
```

<div dir="rtl">

<div align="center">

**כל פעולה עם NULL מחזירה NULL.**
**`5 + NULL` = NULL · `'abc' || NULL` = NULL · `NULL * 0` = NULL**

</div>

**למה?** כי NULL הוא "לא ידוע". ו"לא ידוע ועוד 5" — עדיין לא ידוע.

זה יעקוב אחריכם לאורך כל הקורס. במודול 20 נלמד לטפל בזה (`COALESCE`). בינתיים — **דעו שזה קורה.**

---

## 9. לקרוא הודעת שגיאה

תכתבו שאילתה, תלחצו Run, ותקבלו שגיאה. **זה נורמלי.** מה שחשוב זה לדעת לקרוא אותה.

</div>

```text
YOU WROTE:                          THE ERROR SAYS:
----------------------------------  ------------------------------------------
SELECT nam FROM animal;             no such column: nam
                                    -> typo in a column name. Check spelling.

SELECT name FROM animals;           no such table: animals
                                    -> the table is "animal" (singular).

SELECT name, FROM animal;           near "FROM": syntax error
                                    -> a comma with nothing after it.

SELECT name FROM animal             (nothing happens, or "incomplete input")
                                    -> missing semicolon at the end.

SELECT 'Luna FROM animal;           unrecognized token
                                    -> an opening quote with no closing quote.
```

<div dir="rtl">

| הכלל | ההסבר |
|------|--------|
| **קראו את המילה אחרי `near`** | היא מצביעה על המקום שבו בסיס הנתונים התבלבל — הטעות היא בדרך כלל **ממש לפניה** |
| **`no such column` = כתיב** | 90% מהמקרים. בדקו אות‑אות |
| **`syntax error` = פיסוק** | פסיק מיותר, פסיק חסר, גרש לא סגור |
| **שגיאה בשורה 1 ⟵ הבעיה בשורה 1** | Programiz מונה שורות מתחילת הקוד שהדבקתם |

> 💡 **הודעת שגיאה היא לא כישלון. היא בסיס הנתונים שמסביר לכם מה הוא לא הבין.** מי שלומד לקרוא אותן — מתקדם פי שלושה מהר יותר.

---

## 10. כללי כתיבה — כדי שאפשר יהיה לקרוא

SQL לא רגיש לאותיות גדולות/קטנות ולא לרווחים. שני אלה **זהים**:

</div>

```sql
select name,weight_kg from animal;

SELECT name,
       weight_kg
FROM   animal;
```

<div dir="rtl">

אבל השני קריא, והראשון לא. **המוסכמות שנשתמש בהן בקורס:**

| הכלל | דוגמה |
|------|--------|
| **מילות מפתח באותיות גדולות** | `SELECT`, `FROM`, `AS` |
| **שמות טבלאות ועמודות באותיות קטנות** | `animal`, `weight_kg` |
| **כל חלק (clause) בשורה משלו** | `SELECT` בשורה, `FROM` בשורה |
| **עמודות מיושרות** | ראו למעלה |
| **הערות עם `--`** | `-- this explains what the query does` |
| **נקודה‑פסיק בסוף** | תמיד. גם אם הכלי סולח |

</div>

```sql
-- Good: a comment explains WHY, the layout shows the structure
SELECT name,
       weight_kg * 2.2 AS weight_lb    -- for the American vet
FROM   animal;
```

<div dir="rtl">

> 🎬 **סיפור מהשטח: השאילתה בת 400 המילים**
>
> מתכנת עזב חברה והשאיר אחריו שאילתה אחת קריטית — בשורה אחת, 400 מילים, בלי הערה. היא הפיקה את הדוח החודשי להנהלה.
>
> יום אחד הדוח יצא שגוי. אף אחד לא הצליח להבין את השאילתה כדי לתקן. לקח **שבועיים** לפרק אותה ולכתוב מחדש.
>
> 🔑 שאילתה נכתבת פעם אחת ונקראת עשרות פעמים. **כתבו למי שיקרא — לא למחשב.** המחשב לא אכפת לו.

---

## 11. סביבת אורקל, אפליקציות והטכנולוגיה

תכנית הלימודים מזכירה שלושה נושאים נלווים. בקצרה:

### 11.1 סביבת אורקל

הקורס משתמש ב‑Programiz (SQLite) כי הוא מיידי. תכנית הלימודים הרשמית עובדת ב‑**Oracle APEX**. **90% מהתחביר זהה.** ההבדלים שתפגשו בפרק הזה:

| | SQLite (Programiz) | Oracle |
|---|---|---|
| שאילתה בלי טבלה | `SELECT 1+1;` | `SELECT 1+1 FROM DUAL;` |
| חיבור מחרוזות | `\|\|` | `\|\|` — זהה |
| כינוי עם רווח | `"Animal Name"` | `"Animal Name"` — זהה |
| הודעות שגיאה | `no such column` | `ORA-00904: invalid identifier` |

בכל מודול נסמן הבדלים כאלה במפורש. אם תעברו ל‑APEX (ההוראות ב‑[מדריך ההתקנה](../../resources/setup.md)) — תרגישו בבית.

### 11.2 איך אפליקציות משתמשות ב‑SQL

</div>

```text
   YOU (browser)          THE APPLICATION            THE DATABASE
   +------------+         +-----------------+        +--------------+
   | click      |  ---->  | builds a query: |  --->  | runs it,     |
   | "Dogs"     |         | SELECT name     |        | returns rows |
   |            |  <----  | FROM animal     |  <---  |              |
   | sees list  |         | WHERE species=1 |        |              |
   +------------+         +-----------------+        +--------------+

   Every screen in every app you use is a SELECT underneath.
   Every "save" button is an INSERT or UPDATE (module 25).
```

<div dir="rtl">

### 11.3 הטכנולוגיה

במודול 10 ראינו את המובילים: Oracle, SQL Server, PostgreSQL, MySQL. **כולם מדברים SQL.** מי שיודע לכתוב `SELECT` באחד — עובר לאחר בשבוע.

---

## 12. דוגמה מלאה — סיור ראשון במקלט

רותי מבקשת ממכם רשימה להדפסה: **"כל החיות, עם שם מלא של הסוג, ומשקל בפאונד לווטרינר האמריקאי שמגיע לביקור."**

עוד אין לנו `JOIN` (מודול 21), אז "שם הסוג" יחכה. אבל את השאר אפשר:

</div>

```sql
-- Step 1: what's in the table?
SELECT *
FROM   animal;

-- Step 2: only what she asked for
SELECT name, species_id, weight_kg
FROM   animal;

-- Step 3: add the calculation, with a readable heading
SELECT name,
       species_id,
       weight_kg,
       weight_kg * 2.2 AS weight_lb
FROM   animal;

-- Step 4: one line per animal, ready to print
SELECT name || ' (species ' || species_id || '): '
            || weight_kg || ' kg / '
            || weight_kg * 2.2 || ' lb'   AS print_line
FROM   animal;
```

<div dir="rtl">

**התוצאה של שלב 4:**

</div>

```text
print_line
-------------------------------------------
Luna (species 1): 18.5 kg / 40.7 lb
Simba (species 2): 4.2 kg / 9.24 lb
Rocky (species 1): 31.0 kg / 68.2 lb
...
```

<div dir="rtl">

> 💡 **שימו לב לדרך:** לא כתבנו את שלב 4 ישר. התחלנו מ‑`*`, צמצמנו, הוספנו חישוב, ורק אז עיצבנו. **שאילתה בונים בשלבים, ומריצים בכל שלב.** מי שכותב 6 שורות ומריץ פעם אחת — מקבל שגיאה ולא יודע איפה.

---

## 13. חמש טעויות נפוצות

| # | הטעות | מה קורה | התיקון |
|---|-------|----------|---------|
| 1 | **גרש כפול למחרוזת** — `"Luna"` | בסיס הנתונים מחפש **עמודה** בשם Luna | `'Luna'` — גרש בודד לערך |
| 2 | **פסיק אחרי העמודה האחרונה** — `SELECT name, FROM` | `syntax error near FROM` | הסירו את הפסיק |
| 3 | **לשכוח רווח בחיבור מחרוזות** | `RutiAlmog` | `first_name \|\| ' ' \|\| last_name` |
| 4 | **לצפות ש‑NULL יתנהג כמו 0 או כמו ריק** | כל הביטוי נעלם | מודול 20 — `COALESCE`. בינתיים: דעו שזה קורה |
| 5 | **לא להריץ אחרי כל שינוי** | 6 שורות, שגיאה אחת, ואין מושג איפה | הריצו אחרי **כל** שורה שמוסיפים |

---

## 14. רשימת בדיקה

| ✔ | הבדיקה |
|---|--------|
| ☐ | טענתי את `shelter.sql` וקיבלתי `animals_loaded = 20` |
| ☐ | הרצתי `SELECT * FROM animal;` וראיתי 20 שורות |
| ☐ | אני יודע לבחור עמודות ספציפיות, ובסדר שאני רוצה |
| ☐ | נתתי כינוי לעמודה עם `AS` |
| ☐ | חישבתי משהו ב‑`SELECT` — וראיתי שהטבלה עצמה לא השתנתה |
| ☐ | חיברתי שתי מחרוזות עם `\|\|` — כולל הרווח |
| ☐ | הרצתי `SELECT DISTINCT` וראיתי את ההבדל |
| ☐ | ראיתי מה קורה כשמחברים מחרוזת ל‑NULL |
| ☐ | קיבלתי לפחות שגיאה אחת — **וקראתי אותה** לפני שתיקנתי |
| ☐ | פתרתי את [התרגילים](exercises.md) בעצמי |

---

## 15. סיכום המודול

<div align="center">

### 🧠 שבע נקודות

</div>

1. **SQL היא שפה דקלרטיבית** — אומרים **מה** רוצים, לא **איך**. זו הירושה של קוד מ‑1970.
2. **המבנה קבוע:** `SELECT` מה ⟵ `FROM` מאיפה ⟵ (ובהמשך) `WHERE` אילו שורות ⟵ `ORDER BY` באיזה סדר.
3. **כל שאילתה מחזירה טבלה.** התוצאה היא טבלה חדשה; המקור לא משתנה.
4. **`*` ללמידה בלבד.** בפועל — תמיד עמודות מפורשות, בסדר שאתם רוצים.
5. **`SELECT` יודע לחשב:** חשבון עם `+ - * /`, חיבור מחרוזות עם `||`, ותמיד עם `AS` לתת שם לתוצאה.
6. **NULL מדביק.** כל פעולה עם NULL היא NULL. זה יחזור בכל מודול.
7. **הודעת שגיאה היא הסבר, לא כישלון.** קראו את המילה אחרי `near`.

<div align="center">

---

*"בין 'אני צריך דוח' ל'הנה הדוח' עומד תור של שלושה שבועות —*
*או שורה אחת של SQL."*

---

</div>

## 📎 המשך

| | |
|---|---|
| ❓ | [שאלות ותשובות](questions.md) |
| ✏️ | [תרגילים](exercises.md) — כולם על [בסיס הנתונים המוכן](../../resources/shelter-db/) |
| ✅ | [פתרונות](solutions.md) — עם הפלט האמיתי |
| 🧭 | [חזרה למסלול הלימוד](../../LEARNING-PATH.md) — יחידה 2 |
| ➡️ | מודול 17 — SQL: הגבלת השליפה (`WHERE`) 🔜 |
| 🏠 | [חזרה לדף הקורס](../../) |

</div>
