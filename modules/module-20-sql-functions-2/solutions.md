<div dir="rtl">

# מודול 20 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 כל הפלטים אמיתיים, מהרצה על בסיס הנתונים המוכן, נכון ל‑`'2026-09-21'`. תא ריק בפלט = NULL.

---

## ✅ תרגיל 1 — המרות

</div>

```sql
-- a   15 | 105
SELECT '10' + 5, '10' || 5;
```

<div dir="rtl">

`+` הוא חיבור **מספרים** — SQLite ממיר את `'10'` למספר ⟵ 15. `||` הוא חיבור **טקסט** — SQLite ממיר את 5 לטקסט ⟵ `'105'`. **האופרטור קובע את הטיפוס.**

</div>

```sql
-- b
SELECT name, weight_kg, CAST(weight_kg AS INTEGER) AS whole_kg
FROM   animal;
```

```text
name   weight_kg  whole_kg
-----  ---------  --------
Luna   18.5       18          <- cut, not rounded (ROUND would give 19)
Bella  28.4       28
Coco   0.1        0
Rex    38.7       38
...
```

```sql
-- c
SELECT adoption_date,
       CAST(STRFTIME('%Y', adoption_date) AS INTEGER) + 1 AS next_year
FROM   adoption;
-- 2023-05-10 -> 2024,  2025-07-01 -> 2026, ...
```

```sql
-- d
SELECT CAST(7 AS INTEGER) / 2 AS int_div,
       CAST(7 AS REAL)    / 2 AS real_div;
```

```text
int_div  real_div
-------  --------
3        3.5
```

<div dir="rtl">

שלם חלקי שלם = שלם (השארית נזרקת — מודול 16). מספיק שצד **אחד** עשרוני, והתוצאה עשרונית.

---

## ✅ תרגיל 2 — COALESCE

</div>

```sql
-- a   Mitzi, Nala, Lily -> unknown
SELECT name, COALESCE(breed, 'unknown') AS breed
FROM   animal
WHERE  species_id = 2;

-- b   only Omer has no phone
SELECT first_name, COALESCE(phone, 'no phone') AS phone
FROM   person;

-- c
SELECT expense_id, amount,
       COALESCE(CAST(animal_id AS TEXT), 'general') AS for_animal
FROM   expense;
```

```text
expense_id  amount  for_animal
----------  ------  ----------
1           1850.0  general
2           420.0   8
3           960.0   general
4           650.0   5
5           310.0   general
...
```

<div dir="rtl">

> 💡 **למה `CAST`?** `animal_id` מספר ו‑`'general'` טקסט. SQLite היה מסתדר גם בלי, אבל Oracle לא. **המירו קודם, ואז `COALESCE`.**

</div>

```sql
-- d   Coco, Kiwi -> unknown
SELECT name, COALESCE(birth_date, 'unknown') AS born
FROM   animal
WHERE  species_id = 4;

-- e
SELECT intake_id, intake_type,
       COALESCE(location, reason, 'no details') AS details
FROM   intake;
```

```text
intake_id  intake_type  details
---------  -----------  -----------------------------
1          stray        Herzl St, Haifa
2          surrender    moving abroad
...
11         transfer     transfer from Akko shelter
...
21         surrender    returned by adopter - allergy
```

<div dir="rtl">

---

## ✅ תרגיל 3 — NULLIF

</div>

```sql
-- a   adoptions 7 and 8 (400) show an empty not_full
SELECT adoption_id, fee_paid, NULLIF(fee_paid, 400) AS not_full
FROM   adoption;

-- b
SELECT 100 / 0 AS plain, 100 / NULLIF(0, 0) AS safe;
```

```text
plain  safe
-----  ----
                <- both NULL in SQLite
```

<div dir="rtl">

ב‑SQLite **שתיהן** NULL — SQLite סלחני. ב‑Oracle `100 / 0` הוא **שגיאה** (`ORA-01476: divisor is equal to zero`) שעוצרת את כל השאילתה, ו‑`100 / NULLIF(0, 0)` הוא NULL. לכן כותבים `NULLIF` תמיד.

</div>

```sql
-- c
SELECT name, weight_kg, ROUND(500 / NULLIF(weight_kg, 0), 1) AS daily_g
FROM   animal;
```

```text
name   weight_kg  daily_g
-----  ---------  -------
Luna   18.5       27.0
...
Coco   0.1        5000.0
Kiwi   0.04       12500.0     <- a budgie eating 12.5 kg a day: the formula is wrong
Bunny  1.5        333.3          for tiny animals -- but at least it didn't crash!
```

<div dir="rtl">

---

## ✅ תרגיל 4 — CASE פשוט

</div>

```sql
-- a
SELECT name, status,
       CASE status
         WHEN 'available'  THEN 'ready for adoption'
         WHEN 'adopted'    THEN 'has a home'
         WHEN 'medical'    THEN 'under treatment'
         WHEN 'quarantine' THEN 'in quarantine'
         ELSE 'other'
       END AS label
FROM   animal;
```

```text
name   status      label
-----  ----------  ------------------
Luna   adopted     has a home
Rocky  available   ready for adoption
Max    medical     under treatment
Nala   quarantine  in quarantine
Daisy  deceased    other               <- the ELSE catches what we didn't list
...
```

```sql
-- b   ELSE role = "keep the original value"
SELECT first_name || ' ' || last_name AS full_name,
       CASE role WHEN 'vet' THEN 'medical staff' ELSE role END AS role_label
FROM   person;
-- Dr. Ron Levi / Dr. Maya Nahum -> medical staff; everyone else unchanged

-- c
SELECT name,
       CASE sex WHEN 'M' THEN 'male' WHEN 'F' THEN 'female' ELSE 'unknown' END AS sex_label
FROM   animal;
-- Luna female, Simba male, Coco unknown, ...
```

<div dir="rtl">

---

## ✅ תרגיל 5 — CASE מחפש

</div>

```sql
-- a
SELECT name, weight_kg,
       CASE WHEN weight_kg < 1  THEN 'tiny'
            WHEN weight_kg < 10 THEN 'small'
            WHEN weight_kg < 25 THEN 'medium'
            ELSE 'large' END AS size
FROM   animal
ORDER  BY weight_kg;
```

```text
name     weight_kg  size
-------  ---------  ------
Kiwi     0.04       tiny
Coco     0.1        tiny
Bunny    1.5        small
Thumper  1.8        small
Nala     2.9        small
Mitzi    3.1        small
Lily     3.4        small
Simba    4.2        small
Tom      4.8        small
Felix    5.0        small
Oscar    5.5        small
Charlie  7.2        small
Max      12.3       medium
Daisy    15.6       medium
Luna     18.5       medium
Zoe      22.0       medium
Shadow   25.1       large
Bella    28.4       large
Rocky    31.0       large
Rex      38.7       large
```

```sql
-- b   2100 and 1200 need approval; the other 9 are ok
SELECT amount,
       CASE WHEN amount >= 1000 THEN 'needs approval' ELSE 'ok' END AS approval
FROM   expense
WHERE  category = 'medical'
ORDER  BY amount DESC;

-- c
SELECT name,
       CASE
         WHEN birth_date IS NULL THEN 'unknown'
         WHEN (JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25 < 2 THEN 'puppy'
         WHEN (JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25 < 8 THEN 'adult'
         ELSE 'senior'
       END AS life_stage
FROM   animal
WHERE  species_id = 1;
-- Zoe, Rex, Bella: senior. All other dogs: adult. (No dog is under 2.)
```

<div dir="rtl">

### ד. ⚠️ להעביר את `IS NULL` לסוף — ולמחוק אותו

**להעביר לסוף — לא משנה כלום:**

</div>

```text
name  birth_date  life_stage
----  ----------  ----------
Coco              unknown      <- still correct
Lily              unknown
Kiwi              unknown
Zoe   2016-01-01  senior
```

<div dir="rtl">

כשהתאריך NULL, `< 2` ו‑`< 8` הם "לא ידוע" — לא true — אז `CASE` ממשיך הלאה ומגיע ל‑`IS NULL`.

**למחוק את השורה — Coco, Lily ו‑Kiwi הופכים ל‑`senior`.** אין שום `WHEN` שמתקיים, אז הם נופלים ל‑`ELSE`. **שגיאה שקטה:** אין הודעה, רק תשובה לא נכונה.

> 🔑 **המסקנה:** הסדר של `IS NULL` לא קריטי — **הקיום** שלו קריטי. שמים אותו ראשון כדי שקורא הקוד יראה מיד שטיפלתם ב‑NULL.

---

## ✅ תרגיל 6 — CASE בכל מקום

</div>

```sql
-- a
SELECT name, status
FROM   animal
ORDER  BY CASE status
            WHEN 'medical'    THEN 1
            WHEN 'quarantine' THEN 2
            WHEN 'available'  THEN 3
            ELSE 4
          END,
          name;
```

```text
name     status
-------  ----------
Max      medical
Nala     quarantine
Bunny    available
Coco     available
Felix    available
Lily     available
Mitzi    available
Oscar    available
Rex      available
Rocky    available
Shadow   available
Bella    adopted
Charlie  adopted
Daisy    deceased      <- 'adopted' and 'deceased' share priority 4: sorted by name
Kiwi     adopted
Luna     adopted
Simba    adopted
Thumper  adopted
Tom      adopted
Zoe      adopted
```

```sql
-- b
SELECT name, IIF(chip_number IS NULL, 'no chip', 'has chip') AS chip FROM animal;
SELECT name, CASE WHEN chip_number IS NULL THEN 'no chip' ELSE 'has chip' END AS chip FROM animal;
-- identical results. IIF is a shortcut; CASE works in every database (Oracle has no IIF).
```

<div dir="rtl">

**ג.** הפתרון הוא השאילתה מסעיף 10 במודול. הפלט:

</div>

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

```sql
-- d   the full animal card
SELECT UPPER(name)                    AS card_name,
       COALESCE(breed, 'unknown')     AS breed,
       COALESCE(CAST(CAST((JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25
                          AS INTEGER) AS TEXT), 'unknown') AS age,
       CASE WHEN weight_kg < 1  THEN 'tiny'
            WHEN weight_kg < 10 THEN 'small'
            WHEN weight_kg < 25 THEN 'medium'
            ELSE 'large' END          AS size
FROM   animal
WHERE  status = 'available'
ORDER  BY name;
```

```text
card_name  breed       age      size
---------  ----------  -------  -----
BUNNY      unknown     2        small
COCO       Cockatiel   unknown  tiny
FELIX      Tabby       7        small
LILY       unknown     unknown  small
MITZI      unknown     3        small
OSCAR      Persian     4        small
REX        Rottweiler  9        large
ROCKY      Labrador    6        large
SHADOW     Husky       5        large
```

<div dir="rtl">

> 🎉 **השוו לכרטיס במודול 19:** אותם נתונים — אבל עכשיו אין אף תא ריק. כל NULL קיבל משמעות.

---

## ✅ תרגיל 7 — חשיבה

**א.** התוכים: `species_id = 4`, ואין לו `WHEN`.

</div>

```sql
SELECT name, CASE species_id WHEN 1 THEN 'dog' WHEN 2 THEN 'cat' WHEN 3 THEN 'rabbit' END AS kind
FROM   animal
WHERE  species_id = 4;
```

```text
name  kind
----  ----
Coco             <- NULL: no WHEN matched, no ELSE
Kiwi
```

<div dir="rtl">

**ב.** שלוש סיבות:

1. **`IS NULL` יפסיק לעבוד.** כל שאילתה שמחפשת "חיות בלי גזע ידוע" צריכה עכשיו `= 'unknown'` — ומי שלא יודע את זה יפספס.
2. **`COUNT(breed)` ישקר.** הוא סופר רק ערכים שאינם NULL — ופתאום `'unknown'` נספר כגזע.
3. **הטקסט הוא החלטת תצוגה, לא נתון.** מחר ירצו `'לא ידוע'` בעברית, או `'-'`. עם `COALESCE` משנים שאילתה אחת; עם עדכון — את הטבלה כולה.

</div>

```sql
-- c
SELECT expense_id, category, amount,
       CASE WHEN category = 'medical' AND amount > 1000 THEN 1
            WHEN category = 'medical'                   THEN 2
            WHEN category = 'food'                      THEN 3
            ELSE 4 END AS priority
FROM   expense
ORDER  BY priority, amount DESC;
```

```text
expense_id  category  amount  priority
----------  --------  ------  --------
15          medical   2100.0  1
7           medical   1200.0  1
13          medical   890.0   2
4           medical   650.0   2
22          medical   600.0   2
17          medical   450.0   2
2           medical   420.0   2
10          medical   380.0   2
...
```

<div dir="rtl">

> 💡 **שימו לב לסדר ה‑`WHEN`:** "רפואית מעל 1,000" לפני "רפואית". אם נהפוך — כל ההוצאות הרפואיות יקבלו 2.

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[❓ לשאלות](questions.md)**

</div>

</div>

<!-- w3schools:start -->
<div dir="rtl">

---

## 🌐 תרגול ב‑W3Schools: פתרונות

> כל השאילתות כאן הורצו ב‑W3Schools. מספר הרשומות הוא מה שהאתר מחזיר.

**W1.**

```sql
SELECT Products.ProductName, CASE WHEN Products.Price < 20 THEN 'cheap' ELSE 'expensive' END AS PriceLevel FROM Products;
```

**77** רשומות. השורה הראשונה: `Chais · cheap`


</div>
<!-- w3schools:end -->

<!-- classroom:start -->
<div dir="rtl">

---

## 💪 תרגול בכיתה — פתרונות

> 🏫 על [`school.sql`](../../resources/school-db/). כל הפלטים כאן **אמיתיים** — כל שאילתה הורצה על בסיס הנתונים, נכון לתאריך הייחוס `'2026-09-21'`.

</div>

```text
Cities    (CityCode, CityName)
Teachers  (TeacherCode, FirstName, LastName, Subject, HireDate, Salary, CityCode, Phone)
Classes   (ClassCode, ClassName, Grade, TeacherCode, RoomNumber)
Courses   (CourseCode, CourseName, TeacherCode, WeeklyHours)
Students  (StudentId, FirstName, LastName, ClassCode, Gender, BirthDate, CityCode, EnrollDate, Phone)
Grades    (StudentId, CourseCode, Term, Grade)          -- PK: StudentId + CourseCode + Term
Absences  (AbsenceId, StudentId, AbsenceDate, Excused, Reason)
```

<div dir="rtl">

</div>

```sql
-- ש1
SELECT Students.FirstName, COALESCE(Students.Phone, 'אין טלפון') AS Contact FROM Students;

-- ש2
SELECT Courses.CourseName, COALESCE(Courses.TeacherCode, 0) AS TeacherOrZero FROM Courses;

-- ש3
SELECT Students.FirstName,
       COALESCE(Students.Phone, 'טרם נמסר') AS Phone1,
       COALESCE(CAST(Students.ClassCode AS TEXT), 'טרם שובץ') AS Class1
FROM   Students WHERE Students.StudentId IN (1001, 1002, 1018);

-- ש4
SELECT Classes.ClassName, Classes.RoomNumber, COALESCE(Classes.RoomNumber, -1) AS RoomOrMinus FROM Classes;

-- ש5
SELECT Grades.StudentId, Grades.CourseCode, Grades.Grade,
       CASE
         WHEN Grades.Grade IS NULL THEN 'לא נבחן'
         WHEN Grades.Grade >= 90   THEN 'מעולה'
         WHEN Grades.Grade >= 75   THEN 'טוב'
         WHEN Grades.Grade >= 60   THEN 'עובר'
         ELSE 'נכשל'
       END AS Label
FROM   Grades WHERE Grades.StudentId IN (1004, 1009, 1012, 1016) ORDER BY Grades.StudentId;

-- ש6
SELECT Students.FirstName,
       CASE Students.Gender WHEN 'M' THEN 'תלמיד' WHEN 'F' THEN 'תלמידה' END AS Title
FROM   Students;

-- ש7
SELECT Absences.AbsenceId, Absences.Excused,
       CASE Absences.Excused WHEN 1 THEN 'מאושרת' ELSE 'לא מאושרת' END AS Status,
       COALESCE(Absences.Reason, 'לא נמסרה סיבה') AS Reason1
FROM   Absences;

-- ש8  התיקון: להפוך את סדר שתי השורות
SELECT Grades.StudentId, Grades.Grade,
       CASE
         WHEN Grades.Grade >= 90 THEN 'מעולה'
         WHEN Grades.Grade >= 60 THEN 'עובר'
         ELSE 'נכשל'
       END AS Label
FROM   Grades WHERE Grades.Grade >= 90;

-- ש9
SELECT CAST('42' AS INTEGER) + 8 AS A, CAST(95 AS TEXT) || ' נקודות' AS B,
       CAST(Grades.Grade AS TEXT) || '/100' AS C FROM Grades LIMIT 3;

-- ש10
SELECT Teachers.LastName, Teachers.Salary / 12 AS IntDiv, Teachers.Salary / 12.0 AS RealDiv,
       ROUND(Teachers.Salary / 12.0, 2) AS Rounded FROM Teachers;

-- ש11
SELECT Grades.StudentId, Grades.Grade, COALESCE(Grades.Grade, 0) AS AsZero
FROM   Grades WHERE Grades.StudentId IN (1004, 1009) ORDER BY Grades.StudentId;
SELECT Absences.StudentId, NULLIF(Absences.Excused, 0) AS OnlyExcused FROM Absences LIMIT 5;

-- ש12
SELECT Students.FirstName || ' ' || Students.LastName AS Student,
       COALESCE(CAST(Students.ClassCode AS TEXT), 'ללא כיתה') AS Class1,
       CASE WHEN Students.Phone IS NULL THEN 'אין קשר טלפוני' ELSE Students.Phone END AS Contact,
       CASE WHEN Students.BirthDate IS NULL THEN 'גיל לא ידוע'
            ELSE CAST(CAST((JULIANDAY('2026-09-21') - JULIANDAY(Students.BirthDate)) / 365.25 AS INTEGER) AS TEXT)
       END AS Age
FROM   Students WHERE Students.StudentId IN (1001, 1006, 1018);
```

<div dir="rtl">

**ש1.** `COALESCE` מחזיר את **הארגומנט הראשון שאינו `NULL`**. שבע השורות הראשונות:

<figure dir="ltr" class="dbtable">

| FirstName | Contact |
|:---:|:---:|
| אדם | 050-1000001 |
| נור | אין טלפון |
| יואב | 052-1000003 |
| מאיה | 054-1000004 |
| רוני | אין טלפון |
| סאלי | 050-1000006 |
| עומר | 053-1000007 |

</figure>

**ש2.** **סדנת פרויקטים** — המקצוע היחיד בלי מורה.

<figure dir="ltr" class="dbtable">

| CourseName | TeacherOrZero |
|:---:|:---:|
| מתמטיקה 5 יח"ל | 1 |
| אנגלית 4 יח"ל | 2 |
| מבוא לבסיסי נתונים | 3 |
| היסטוריה | 4 |
| חינוך גופני | 5 |
| מתמטיקה 3 יח"ל | 6 |
| סדנת פרויקטים | 0 |

</figure>

> ⚠️ **אבל `0` הוא קוד מורה לא חוקי.** הוא "נראה" כמו נתון, ומישהו בהמשך ינסה לעשות לו `JOIN` ולא ימצא מורה. ראו ש4.

**ש3.** צריך **`CAST`**: כל הארגומנטים של `COALESCE` צריכים להיות מאותו טיפוס, ולכן ממירים את המספר לטקסט **לפני** שמציעים טקסט כגיבוי: `COALESCE(CAST(ClassCode AS TEXT), 'טרם שובץ')`.

<figure dir="ltr" class="dbtable">

| FirstName | Phone1 | Class1 |
|:---:|:---:|:---:|
| אדם | 050-1000001 | 101 |
| נור | טרם נמסר | 101 |
| לינא | טרם נמסר | טרם שובץ |

</figure>

**ש4.** `-1` עובד, והוא **רעיון רע בדרך כלל**.

| מתי כן | מתי לא |
|---------|---------|
| בתצוגה בלבד — ובתנאי שהמשתמש מבין שזה "אין" | כשהעמודה תשמש לחישוב: `AVG` יספור את ה‑`-1` ויקלקל את הממוצע |
| כשהערך **בלתי אפשרי** בעולם האמיתי, ולכן אי אפשר להתבלבל | כשהערך אפשרי — `0` כציון, `0` כקוד מורה |

הכלל: `COALESCE` הוא כלי **לתצוגה**. הוא לא מתקן את הנתון ולא משנה את הטבלה — הוא רק מחליף את מה שמוצג במסך. אם המשכתם לחשב עם מה שהחלפתם, המצאתם נתון.

<figure dir="ltr" class="dbtable">

| ClassName | RoomNumber | RoomOrMinus |
|:---:|:---:|:---:|
| י1 | 12 | 12 |
| י2 | 14 | 14 |
| יא1 | 21 | 21 |
| יא2 | NULL | -1 |
| יב1 | 31 | 31 |

</figure>

**ש5.** **15 שורות.** `CASE` המחפש נבדק **מלמעלה למטה ועוצר בראשון שמתקיים**, ולכן אין צורך לכתוב `BETWEEN 75 AND 89` — אם הגענו לשורה הזאת, כבר ידוע שהציון קטן מ‑90.

`WHEN Grade IS NULL` נמצא **ראשון** בכוונה: אם הוא היה בסוף, שתי השורות של "לא נבחן" היו נופלות ל‑`ELSE` ומקבלות **`נכשל`** — וזה הבדל בין "לא בא לבחינה" ל"נכשל בה".

<figure dir="ltr" class="dbtable">

| StudentId | CourseCode | Grade | Label |
|:---:|:---:|:---:|:---:|
| 1004 | 12 | 62 | עובר |
| 1004 | 14 | NULL | לא נבחן |
| 1004 | 16 | 48 | נכשל |
| 1009 | 12 | NULL | לא נבחן |
| 1009 | 13 | 63 | עובר |
| 1009 | 16 | 54 | נכשל |
| 1012 | 12 | 47 | נכשל |
| 1012 | 13 | 51 | נכשל |
| 1012 | 16 | 42 | נכשל |
| 1012 | 16 | 39 | נכשל |
| 1016 | 11 | 98 | מעולה |
| 1016 | 11 | 100 | מעולה |
| 1016 | 12 | 93 | מעולה |
| 1016 | 13 | 99 | מעולה |
| 1016 | 17 | 95 | מעולה |

</figure>

> 🔎 ג'וד מנסור (1012) — **ארבעה "נכשל" מתוך ארבעה**. ראניה עבאס (1016) — חמישה "מעולה" מתוך חמישה.

**ש6.** `CASE` הפשוט משווה עמודה **אחת** לערכים. שימו לב שאין `ELSE` — ואין צורך, כי `Gender` מוגבל ב‑`CHECK` ל‑`'M'`/`'F'`. אילו היה ערך שלישי, היינו מקבלים `NULL` בשקט.

<figure dir="ltr" class="dbtable">

| FirstName | Title |
|:---:|:---:|
| אדם | תלמיד |
| נור | תלמידה |
| יואב | תלמיד |
| מאיה | תלמידה |
| רוני | תלמיד |

</figure>

**ש7.** שתי הפונקציות יחד: `CASE` הופך קוד לתווית, `COALESCE` ממלא את החסר.

<figure dir="ltr" class="dbtable">

| AbsenceId | Excused | Status | Reason1 |
|:---:|:---:|:---:|:---:|
| 1 | 1 | מאושרת | מחלה |
| 2 | 1 | מאושרת | מחלה |
| 3 | 0 | לא מאושרת | לא נמסרה סיבה |
| 4 | 0 | לא מאושרת | לא נמסרה סיבה |
| 5 | 0 | לא מאושרת | לא נמסרה סיבה |
| 6 | 1 | מאושרת | תור לרופא |

</figure>

**ש8.** **אפס "מעולה".** כל 21 הציונים שמ‑90 ומעלה קיבלו **`עובר`**.

`CASE` עוצר בתנאי הראשון שמתקיים. ציון 98 מקיים את `>= 60` — זה כתוב ראשון, הבדיקה נגמרה, והשורה `>= 90` **לעולם לא נבדקת**. היא קוד מת. אין שגיאה, אין אזהרה: רק דוח שבו כל המצטיינים מסומנים "עובר".

**התיקון:** להפוך את סדר שתי השורות. ב‑`CASE` מחפש כותבים את התנאים **מהמחמיר לרחב** — מהצר לרחב, לא ההפך.

חמש השורות הראשונות מתוך 21:

<figure dir="ltr" class="dbtable">

| StudentId | Grade | Label (השגוי) | Label (המתוקן) |
|:---:|:---:|:---:|:---:|
| 1001 | 92 | עובר | מעולה |
| 1001 | 91 | עובר | מעולה |
| 1002 | 95 | עובר | מעולה |
| 1002 | 100 | עובר | מעולה |
| 1005 | 90 | עובר | מעולה |

</figure>

**ש9.** `CAST` עובד לשני הכיוונים: טקסט שנראה כמו מספר הופך למספר, ומספר הופך לטקסט שאפשר לחבר ב‑`||`.

<figure dir="ltr" class="dbtable">

| A | B | C |
|:---:|:---:|:---:|
| 50 | 95 נקודות | 88/100 |
| 50 | 95 נקודות | 74/100 |
| 50 | 95 נקודות | 92/100 |

</figure>

**ש10.** `Salary / 12` החזיר **1208** — ו‑`Salary / 12.0` החזיר **1208.3333333333333**.

**למה?** כששני האופרנדים הם **שלמים**, החלוקה היא **חלוקה שלמה**: השבר נזרק (לא מעוגל — **נקטם**). ברגע שאחד מהם הוא מספר ממשי (`12.0`), החלוקה ממשית.

</div>

```sql
Salary / 12            -- 14500 / 12  =  1208      ❌ איבדנו 4 אגורות
Salary / 12.0          -- 14500 / 12.0 = 1208.3333  ✅
CAST(Salary AS REAL) / 12   --                 ✅  דרך שנייה לאותו דבר
```

<div dir="rtl">

<figure dir="ltr" class="dbtable">

| LastName | IntDiv | RealDiv | Rounded |
|:---:|:---:|:---:|:---:|
| סרחאן | 1208 | 1208.3333333333333 | 1208.33 |
| בר-לב | 933 | 933.3333333333334 | 933.33 |
| זיאד | 1066 | 1066.6666666666667 | 1066.67 |
| שמש | 1275 | 1275.0 | 1275.0 |

</figure>

> 🔎 אצל שמש יצא **`1275.0`** ולא `1275`: החלוקה הייתה מדויקת, אבל **הטיפוס** נשאר ממשי. ב‑SQLite מספר ממשי מוצג תמיד עם נקודה עשרונית, גם כשאין שבר. זה לא באג — זה הטיפוס.

**ש11א.**

<figure dir="ltr" class="dbtable">

| StudentId | Grade | AsZero |
|:---:|:---:|:---:|
| 1004 | 62 | 62 |
| 1004 | NULL | 0 |
| 1004 | 48 | 48 |
| 1009 | NULL | 0 |
| 1009 | 63 | 63 |
| 1009 | 54 | 54 |

</figure>

**האם זה נכון? כמעט תמיד לא.** `0` אינו "לא נבחן" — `0` הוא **ציון**, והוא הציון הגרוע ביותר שאפשר. מאיה לא נבחנה בהיסטוריה; ברגע שהחלפנו את ה‑`NULL` באפס, הממוצע שלה צונח, היא מופיעה בכל רשימת הנכשלים, והנתון שאומר "חסר מידע" הפך לנתון שאומר "נכשלה לגמרי".

זו **החלטה מדיניות, לא החלטה טכנית**: בבית ספר אמיתי, "לא נבחן" מטופל אחרת מ‑0 (מועד ב'). `NULL` הוא התיאור הנאמן של המצב, ולכן עדיף להשאיר אותו ולתייג אותו ב‑`CASE` (ש5) מאשר להמציא לו מספר.

**ש11ב.** `NULLIF(a, b)` מחזיר `NULL` אם `a = b`, ואחרת את `a`. כאן הוא הפך כל `0` ל‑`NULL` — מה שמשאיר רק את ההיעדרויות המאושרות כערך "אמיתי". השימוש הקלאסי שלו הוא אחר: `a / NULLIF(b, 0)` — כך חלוקה באפס מחזירה `NULL` במקום שגיאה.

<figure dir="ltr" class="dbtable">

| StudentId | OnlyExcused |
|:---:|:---:|
| 1003 | 1 |
| 1003 | 1 |
| 1004 | NULL |
| 1009 | NULL |
| 1009 | NULL |

</figure>

**ש12.** שורת דוח שלמה — **ואף `NULL` אחד**. שימו לב ל‑`CAST` הכפול בגיל: `CAST(… AS INTEGER)` כדי לקטום את השבר, ו‑`CAST(… AS TEXT)` כדי שהענף הזה יחזיר טקסט כמו הענף השני. עמודה אחת — טיפוס אחד.

<figure dir="ltr" class="dbtable">

| Student | Class1 | Contact | Age |
|:---:|:---:|:---:|:---:|
| אדם חלבי | 101 | 050-1000001 | 15 |
| סאלי חסון | 102 | 050-1000006 | גיל לא ידוע |
| לינא חמוד | ללא כיתה | אין קשר טלפוני | 15 |

</figure>

**שלוש השורות האלה הן כל השיעור:** אדם הוא המקרה הרגיל, ולסאלי וללינא חסר משהו אחר. בלי `COALESCE` ו‑`CASE` היה בדוח `NULL` במקום הכיתה, במקום הטלפון ובמקום הגיל — ומי שקורא את הדוח לא היה יודע אם הנתון חסר, אם השאילתה שבורה, או אם התלמידה לא קיימת.

</div>
<!-- classroom:end -->
