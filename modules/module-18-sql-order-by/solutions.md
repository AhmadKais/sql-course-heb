<div dir="rtl">

# מודול 18 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 כל הפלטים אמיתיים — מ‑`shelter.sql` ב‑SQLite. **איפה שהתנהגות Oracle שונה — מסומן.**

---

## ✅ תרגיל 1 — מיון בסיסי

</div>

```sql
-- a  Kiwi (0.04) first ... Rex (38.7) last
SELECT name, weight_kg FROM animal ORDER BY weight_kg;

-- b  Rex first ... Kiwi last
SELECT name, weight_kg FROM animal ORDER BY weight_kg DESC;

-- c  Almog, Bar, Cohen, Dayan, Golan, Katz, Levi, Levi, Mizrahi, Nahum, Peretz, Shalev
SELECT first_name, last_name FROM person ORDER BY last_name;

-- d  2025-03-14 first ... 2024-01-05 last
SELECT expense_date, category, amount FROM expense ORDER BY expense_date DESC;

-- e  100, 150, 200, 200, 200, 250, 300, 400, 400
SELECT adoption_id, fee_paid FROM adoption ORDER BY fee_paid;
```

<div dir="rtl">

> 💡 **ב‑ג':** שני `Levi` — Amir ו‑Dr. Ron. **הסדר ביניהם לא מוגדר.** ראו תרגיל 3 — צריך מפתח שני.

---

## ✅ תרגיל 2 — WHERE + ORDER BY

</div>

```sql
-- a  Rex, Rocky, Bella, Shadow, Zoe, Luna, Daisy, Max, Charlie
SELECT name, weight_kg FROM animal WHERE species_id = 1 ORDER BY weight_kg DESC;

-- b  Bunny, Coco, Felix, Lily, Mitzi, Oscar, Rex, Rocky, Shadow
SELECT name FROM animal WHERE status = 'available' ORDER BY name;

-- c  2100, 1200, 890, 650, 600, 450, 420, 380, 330, 275, 175
SELECT expense_date, amount FROM expense WHERE category = 'medical' ORDER BY amount DESC;

-- d  Ruti 2013, Dr. Ron 2015, Noa 2019, Dana 2023, Lior 2024, Omer 2024
SELECT first_name, joined_date FROM person WHERE city = 'Haifa' ORDER BY joined_date;
```

<div dir="rtl">

### ה. `ORDER BY` לפני `WHERE`

</div>

```sql
SELECT first_name FROM person ORDER BY joined_date WHERE city = 'Haifa';
```

```text
Error: near "WHERE": syntax error
```

<div dir="rtl">

**סדר החלקים קבוע:** `SELECT → FROM → WHERE → ORDER BY → LIMIT`. אי אפשר להחליף. המילה אחרי `near` — `WHERE` — היא המקום שבו בסיס הנתונים הפסיק להבין.

---

## ✅ תרגיל 3 — שני מפתחות

</div>

```sql
-- a
SELECT name, species_id FROM animal ORDER BY species_id, name;
-- -> Bella, Charlie, Daisy, Luna, Max, Rex, Rocky, Shadow, Zoe (dogs A-Z), then cats A-Z...

-- b
SELECT name, species_id, weight_kg FROM animal ORDER BY species_id, weight_kg DESC;
-- -> Rex 38.7, Rocky 31.0 ... Charlie 7.2 (dogs), Oscar 5.5 ... Nala 2.9 (cats), ...

-- c
SELECT first_name, last_name, role FROM person ORDER BY role, last_name;
-- -> adopters: Bar, Cohen, Dayan, Katz, Mizrahi, Shalev
--    vets:     Levi, Nahum
--    volunteers: Almog, Golan, Levi, Peretz

-- d
SELECT category, amount FROM expense ORDER BY category, amount DESC;
```

<div dir="rtl">

### ה. `ORDER BY species_id DESC, weight_kg`

</div>

```text
name     species_id  weight_kg
-------  ----------  ---------
Kiwi     4           0.04       <- parrots now FIRST (species descending)
Coco     4           0.1
Bunny    3           1.5
Thumper  3           1.8
Nala     2           2.9        <- and within each species: LIGHTEST first
...
Rex      1           38.7       <- dogs last, Rex at the very end
```

<div dir="rtl">

**מה השתנה:** שני הדברים. המינים התהפכו (4 ⟵ 1), **וגם** המשקל התהפך (הסרנו את `DESC` ממנו). **מה לא השתנה:** העיקרון — עדיין מקבצים לפי מין ומסדרים בתוכו.

---

## ✅ תרגיל 4 — "N הראשונים"

</div>

```sql
-- a  Rex 38.7, Rocky 31.0, Bella 28.4
SELECT name, weight_kg FROM animal ORDER BY weight_kg DESC LIMIT 3;

-- b  Kiwi 0.04, Coco 0.1, Bunny 1.5
SELECT name, weight_kg FROM animal ORDER BY weight_kg LIMIT 3;

-- c  2100 (medical), 1950, 1900, 1850, 1790 (all food)
SELECT expense_date, category, amount FROM expense ORDER BY amount DESC LIMIT 5;

-- d  animal 1 (Luna), 2025-07-01
SELECT animal_id, adoption_date FROM adoption ORDER BY adoption_date DESC LIMIT 1;

-- e  Ruti, 2013-03-01
SELECT first_name, joined_date FROM person ORDER BY joined_date LIMIT 1;
```

<div dir="rtl">

### ו. `LIMIT 3` בלי `ORDER BY`

</div>

```text
name   weight_kg
-----  ---------
Luna   18.5       <- these are just the first 3 rows STORED.
Simba  4.2           Not the heaviest. Not the lightest. Just... three.
Rocky  31.0
```

<div dir="rtl">

**לא "3 הכבדות".** שלוש שורות בסדר האחסון. **וזה הדוח שהמנהל מהסיפור הזמין לפיו מלאי.**

---

## ✅ תרגיל 5 — כינויים וביטויים

</div>

```sql
-- a
SELECT name, weight_kg * 2.2 AS lb FROM animal ORDER BY lb DESC;
-- -> Rex 85.14, Rocky 68.2, Bella 62.48, ...

-- b
SELECT adoption_id, fee_paid, fee_paid * 1.18 AS with_vat FROM adoption ORDER BY with_vat;
-- -> 118, 177, 236, 236, 236, 295, 354, 472, 472

-- d
SELECT first_name || ' ' || last_name AS full_name FROM person ORDER BY full_name;
-- -> Amir Levi, Dana Cohen, Dr. Maya Nahum, Dr. Ron Levi, Eitan Shalev, ...
```

<div dir="rtl">

### ג. ⚠️ `WHERE lb > 40`

| הכלי | מה קורה |
|------|----------|
| **OneCompiler (SQLite)** | ✅ **עובד** — מחזיר Luna, Rocky, Bella, Zoe, Rex, Shadow |
| **Oracle** | ❌ `ORA-00904: "LB": invalid identifier` |

**למה Oracle נכשל:** `WHERE` רץ **לפני** `SELECT`. הכינוי `lb` עוד לא נוצר.
**למה SQLite עובד:** הוא **חורג מהתקן** ומרשה. זו נוחות — וזו מלכודת: שאילתה שעובדת בתרגול תיכשל בבחינה.

**הכתיבה הנכונה (עובדת בכל מקום):**

</div>

```sql
SELECT name, weight_kg * 2.2 AS lb
FROM   animal
WHERE  weight_kg * 2.2 > 40      -- repeat the expression, not the alias
ORDER  BY lb DESC;               -- alias is fine HERE
```

<div dir="rtl">

### ה. מיון לפי `full_name` — פרטי או משפחה?

**לפי שם פרטי.** `full_name` מתחיל בשם הפרטי, ומיון טקסט הוא תו‑תו משמאל. `Amir Levi` לפני `Dana Cohen` — למרות ש‑Cohen לפני Levi.

**אם רוצים לפי משפחה:** `ORDER BY last_name, first_name` — על העמודות המקוריות, לא על הכינוי.

---

## ✅ תרגיל 6 — NULL במיון

### א+ב. איפה NULL

</div>

```text
ORDER BY birth_date          ORDER BY birth_date DESC
(ascending)                  (descending)

name  birth_date             name  birth_date
----  ----------             ----  ----------
Coco              <- NULL    Nala  2024-03-01
Lily              <- NULL    Bunny 2024-01-01
Kiwi              <- NULL    ...
Zoe   2016-01-01             Zoe   2016-01-01
...                          Coco              <- NULL
Nala  2024-03-01             Lily              <- NULL
                             Kiwi              <- NULL

SQLite: NULL is the SMALLEST value. First in ASC, last in DESC.
Oracle: NULL is the LARGEST value. Last in ASC, first in DESC.   <- opposite!
```

<div dir="rtl">

### ג. ⚠️ "3 הוותיקות"

</div>

```sql
SELECT name, birth_date FROM animal ORDER BY birth_date LIMIT 3;
```

```text
name  birth_date
----  ----------
Coco
Lily
Kiwi
```

<div dir="rtl">

**שגוי לחלוטין.** אלה לא הוותיקות — אלה שלוש חיות שאין להן תאריך. **הדוח יצא, נראה תקין, ושגוי ב‑100%.** בלי שגיאה.

### ד. התיקון

</div>

```sql
SELECT   name, birth_date
FROM     animal
ORDER BY birth_date IS NULL,     -- 0 for known dates, 1 for NULL -> known first
         birth_date
LIMIT    3;
-- -> Zoe 2016, Rex 2017, Bella 2018   [OK]
```

<div dir="rtl">

### ה+ו. לפי גזע, NULL בסוף — שתי גרסאות

</div>

```sql
-- SQLite (OneCompiler)
SELECT name, breed FROM animal ORDER BY breed IS NULL, breed;

-- Oracle
SELECT name, breed FROM animal ORDER BY breed NULLS LAST;
```

```text
name     breed
-------  ---------------
Max      Beagle
Kiwi     Budgie
Coco     Cockatiel
...
Simba    Tabby
Felix    Tabby
Mitzi                     <- the four with no breed, at the end
Nala
Lily
Bunny
```

<div dir="rtl">

> 🔑 **הטריק של SQLite עובד גם ב‑Oracle** (`IS NULL` הוא ביטוי חוקי בכל מקום). `NULLS LAST` **לא** עובד ב‑SQLite. אז אם צריך אחד לשניהם — הטריק.

---

## ✅ תרגיל 7 — מיון טקסט

### א. אורך שם

</div>

```sql
SELECT name, LENGTH(name) AS len FROM animal ORDER BY LENGTH(name) DESC;
-- -> Thumper 7, Charlie 7, Shadow 6, Simba 5, Rocky 5, ... , Tom 3, Max 3, Zoe 3, Rex 3
```

<div dir="rtl">

### ב. אותיות מעורבות

</div>

```text
word
------
Apple
Banana
mango
zebra
```

<div dir="rtl">

**נראה בסדר?** רק במקרה — כי `Apple` ו‑`Banana` גם ככה ראשונות. נסו להוסיף `'apple'` באות קטנה: היא תיפול **אחרי** `zebra`. כל האותיות הגדולות (65–90) לפני כל הקטנות (97–122).

### ג. התיקון

</div>

```sql
SELECT word
FROM   (SELECT 'zebra' AS word UNION SELECT 'Apple'
        UNION SELECT 'mango' UNION SELECT 'Banana')
ORDER  BY UPPER(word);
-- -> Apple, Banana, mango, zebra  (now case-insensitive)
```

<div dir="rtl">

⚠️ **למה תת‑שאילתה?** SQLite לא מרשה ביטוי ב‑`ORDER BY` ישירות אחרי `UNION` — רק שמות עמודות. העטיפה פותרת את זה. (על טבלה רגילה, `ORDER BY UPPER(name)` עובד ישירות.)

### ד. מספרים כטקסט

</div>

```text
n
--
1
10      <- '10' before '2': compared character by character, '1' < '2'
2
20
```

<div dir="rtl">

**הלקח:** מספר ששמור כטקסט ממוין כטקסט. **אם זה מספר — שיהיה מספר** (מודול 7, תחומים). ואם כבר תקוע כטקסט: `ORDER BY CAST(n AS INTEGER)` — מודול 20.

---

## ✅ תרגיל 8 — שוויון בקצה

### א+ב.

</div>

```sql
SELECT name, species_id FROM animal ORDER BY species_id LIMIT 3;
-- -> Luna, Rocky, Bella   (this time)
```

<div dir="rtl">

**שלוש פעמים — אותה תוצאה.** אבל **אין הבטחה**: יש 9 כלבים עם `species_id = 1`, כולם שווים למפתח המיון. בסיס הנתונים בוחר שלושה. היום הוא בחר לפי סדר האחסון; אחרי `UPDATE`, אחרי שדרוג, אחרי אינדקס חדש — עלול לבחור אחרת.

### ג. דטרמיניסטי

</div>

```sql
SELECT name, species_id FROM animal ORDER BY species_id, animal_id LIMIT 3;
-- -> ALWAYS Luna (1), Rocky (3), Bella (5) -- the three lowest ids among dogs
```

<div dir="rtl">

### ד. אימוצים יקרים — שני 400

</div>

```sql
SELECT   adoption_id, animal_id, fee_paid
FROM     adoption
ORDER BY fee_paid DESC,
         adoption_id          -- tie-breaker: lower id first
LIMIT    3;
-- -> 7 (400), 8 (400), 1 (300)
```

<div dir="rtl">

> 🔑 **הכלל:** `LIMIT` + מפתח שיכול להיות שווה = הוסיפו מפתח **ייחודי** אחרון. תמיד.

---

## ✅ תרגיל 9 — סימולציית ראיון

| # | תשובה טובה | ⭐ המלכודת שהופכת אותה למצוינת |
|---|-------------|----------------------------------|
| 1 | `WHERE` בוחר **אילו** שורות; `ORDER BY` — **באיזה סדר** | "ו‑`WHERE` רץ קודם, אז הוא גם מקטין את מה ש‑`ORDER BY` צריך למיין" |
| 2 | 5 שורות **כלשהן** | "ראיתי דוח שעבד שנתיים ככה ונשבר אחרי שדרוג" |
| 3 | תלוי בבסיס הנתונים — ראשון ב‑SQLite, אחרון ב‑Oracle | "ולכן אני תמיד כותב `NULLS LAST` או `IS NULL` כמפתח" |
| 4 | סדר הביצוע — `WHERE` לפני `SELECT`, `ORDER BY` אחרי | "SQLite חורג ומרשה, אז שאילתה שעובדת בתרגול עלולה להיכשל בייצור" |
| 5 | `FROM → WHERE → SELECT → ORDER BY → LIMIT` | "ולכן `LIMIT` לא מאיץ — הוא רץ אחרון" |
| 6 | `a` **עולה** — `DESC` חל רק על `b` | "טעות נפוצה, ראיתי אותה בקוד ייצור" |

**הדירוג העצמי:** אם עניתם נכון על 5+ ובקול בלי גמגום — אתם מוכנים לשאלה כזאת בראיון. אם גמגמתם — זה בדיוק מה שיקרה בראיון. **תרגלו בקול.**

---

## ✅ תרגיל 10 — הדוחות של רותי

</div>

```sql
-- a  Shadow, Rocky, Rex | Mitzi, Felix, Oscar, Lily(NULL) | Bunny | Coco(NULL)
SELECT   name, species_id, weight_kg, birth_date
FROM     animal
WHERE    status = 'available'
ORDER BY species_id,
         birth_date IS NULL,    -- second key: unknowns last WITHIN each species
         weight_kg;

-- b  2100, 1200, 890, 650, 450, 420, 380, 275, 175
SELECT   expense_date, amount, animal_id
FROM     expense
WHERE    category = 'medical'
  AND    expense_date BETWEEN '2024-01-01' AND '2024-12-31'
ORDER BY amount DESC,
         expense_date;          -- tie-breaker (no ties this time, but safe)

-- c  Ruti 2013, Noa 2019, Amir 2022, Tamar 2024
SELECT   first_name, last_name, joined_date
FROM     person
WHERE    role = 'volunteer'
ORDER BY joined_date,
         last_name;

-- d
SELECT   vaccination_id, animal_id, given_date
FROM     vaccination
ORDER BY given_date DESC,
         vaccination_id DESC    -- two on 2025-03-12: without this, order is undefined
LIMIT    3;
-- -> 28 (2025-05-30), 26 (2025-03-12), 25 (2025-03-12)
```

<div dir="rtl">

> 💡 **ב‑ד' יש שוויון אמיתי:** חיסונים 25 ו‑26 ניתנו באותו יום (שני חיסונים ל‑Shadow). בלי שובר השוויון — הסדר ביניהם לא מובטח.

### ה. "הכי כבדה בכל מין"

**❌ לא אפשרי עם מה שלמדנו.** `ORDER BY species_id, weight_kg DESC` מסדר נכון — אבל `LIMIT 1` ייתן רק את **הראשונה בכלל**, לא אחת לכל מין.

**מה חסר:** `GROUP BY species_id` + `MAX(weight_kg)` — **מודול 24**. זו בדיוק השאלה ש‑`GROUP BY` נולד בשבילה.

### ו. ⭐⭐ בטיפול/הסגר ראשונים, ואז כולם לפי שם

</div>

```sql
SELECT   name, status
FROM     animal
ORDER BY status IN ('medical', 'quarantine') DESC,   -- TRUE (1) before FALSE (0)
         name;
```

```text
name     status
-------  ----------
Max      medical       <- the two "urgent" ones first
Nala     quarantine
Bella    adopted       <- then everyone else, A-Z
Bunny    available
Charlie  adopted
...
```

<div dir="rtl">

**המנגנון:** `status IN (…)` הוא ביטוי בוליאני — `1` לשתי החיות, `0` לשאר. `DESC` שם את ה‑1 ראשון. **אותו טריק כמו `IS NULL`** — מפתח ראשון "מלאכותי" שרק מחלק לשתי קבוצות.

> 🎓 **הדפוס הזה שווה זהב:** *"שים את X ראשון, ואז הכול לפי Y"* = `ORDER BY <condition for X> DESC, Y`. עובד לכל תנאי.

---

<div align="center">

### 🎯 סיימתם את מודול 18!

חמש מתוך שמונה השאלות של רותי נענו.
במודול הבא — **פונקציות**: לחתוך טקסט, לעגל מספרים, לחשב גילים.

---

### ➡️ [מודול 19 — SQL: פונקציות](../module-19-sql-functions/)

</div>

---

<div align="center">

**🧭 ניווט המודול**

</div>

| 📖 [חזרה למודול](README.md) | ❓ [שאלות ותשובות](questions.md) | ✏️ [לתרגילים](exercises.md) | 🏠 [דף הקורס](../../) |
|---|---|---|---|

</div>


<!-- w3schools:start -->
<div dir="rtl">

---

## 🌐 תרגול ב‑W3Schools: פתרונות

> כל השאילתות כאן הורצו ב‑W3Schools. מספר הרשומות הוא מה שהאתר מחזיר.

**W1.**

```sql
SELECT Products.ProductName, Products.Price FROM Products ORDER BY Products.Price DESC;
```

**77** רשומות. השורה הראשונה: `Côte de Blaye · 263.50`

**W2.**

```sql
SELECT Customers.Country, Customers.CustomerName FROM Customers ORDER BY Customers.Country, Customers.CustomerName;
```

**91** רשומות. השורה הראשונה: `Argentina · Cactus Comidas para llevar`


</div>
<!-- w3schools:end -->

<!-- exam-style:start -->
<div dir="rtl">

---

## 🎓 תרגול בסגנון הבחינה: פתרונות

**ב1.** **טניס, 300.** `DESC` פירושו מהגדול לקטן.

<figure dir="ltr" class="dbtable">

| ClubName | Price |
|:---:|:---:|
| טניס | 300 |
| שחייה מתקדמים | 250 |
| שחייה מתחילים | 220 |

</figure>

**ב2.** ```sql
SELECT Members.FirstName, Members.Age FROM Members
ORDER BY Members.Age DESC, Members.FirstName;
```

<figure dir="ltr" class="dbtable">

| FirstName | Age |
|:---:|:---:|
| ליאור | 17 |
| סאלי | 17 |
| ג'וד | 16 |
| יואב | 16 |
| שירה | 16 |
| מאיה | 15 |
| נור | 15 |
| עומר | 15 |
| אדם | 14 |
| תמר | 14 |
| כרים | 13 |
| רוני | 13 |

</figure>


</div>
<!-- exam-style:end -->

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

> 💡 **למורה:** הבלוק כולו רץ בהרצה אחת (חוץ מ‑ש12, שנכשלת בכוונה).

</div>

```sql
-- ש1
SELECT Students.LastName, Students.FirstName FROM Students ORDER BY Students.LastName;

-- ש2
SELECT Teachers.LastName, Teachers.Salary FROM Teachers ORDER BY Teachers.Salary DESC;

-- ש3
SELECT Grades.StudentId, Grades.CourseCode, Grades.Grade FROM Grades
ORDER BY Grades.Grade DESC LIMIT 5;

-- ש4
SELECT Grades.StudentId, Grades.CourseCode, Grades.Grade FROM Grades
ORDER BY Grades.Grade LIMIT 6;

-- ש5
SELECT Students.ClassCode, Students.LastName, Students.FirstName FROM Students
ORDER BY Students.ClassCode, Students.LastName;

-- ש6
SELECT Students.Gender, Students.FirstName, Students.BirthDate FROM Students
ORDER BY Students.Gender, Students.BirthDate DESC;

-- ש7
SELECT Teachers.LastName, Teachers.Salary * 12 AS AnnualSalary FROM Teachers
ORDER BY Teachers.Salary * 12 DESC;

-- ש8
SELECT Teachers.LastName, Teachers.Salary * 12 AS AnnualSalary FROM Teachers
ORDER BY AnnualSalary DESC;

-- ש9
SELECT Courses.CourseName, Courses.WeeklyHours FROM Courses ORDER BY 2 DESC, 1;

-- ש10  השגויה, ואחריה התיקון
SELECT Students.FirstName, Students.BirthDate FROM Students ORDER BY Students.BirthDate LIMIT 3;
SELECT Students.FirstName, Students.BirthDate FROM Students
WHERE  Students.BirthDate IS NOT NULL ORDER BY Students.BirthDate LIMIT 3;

-- ש11
SELECT Grades.StudentId, Grades.Grade FROM Grades WHERE Grades.Grade < 60 ORDER BY Grades.Grade;

-- ש12  ⚠️ נכשלת בכוונה
SELECT Students.FirstName FROM Students ORDER BY Students.FirstName WHERE Students.ClassCode = 101;
```

<div dir="rtl">

**ש1.** ראשון **אברהם רוני**, אחרון **שחר נועם**. 18 שורות, והמיון העברי תקין.

<figure dir="ltr" class="dbtable">

| LastName | FirstName |
|:---:|:---:|
| אברהם | רוני |
| ביטון | עומר |
| גולן | איתי |
| חלבי | אדם |
| חלבי | כרים |
| … | … |
| שושן | תמר |
| שחר | נועם |

</figure>

> 🔎 **חלבי** מופיע פעמיים (אדם וכרים). אדם לפני כרים — אבל **זה לא מובטח**: לא ביקשנו מפתח שני. ראו ש3.

**ש2.** **אורלי שמש** — 15,300 ₪. אחרונה: פאדי חדאד, 9,800 ₪.

<figure dir="ltr" class="dbtable">

| LastName | Salary |
|:---:|:---:|
| שמש | 15300 |
| סרחאן | 14500 |
| מזרחי | 13100 |
| זיאד | 12800 |
| בר-לב | 11200 |
| אבו-ראס | 10400 |
| חדאד | 9800 |

</figure>

**ש3.** שלושת המאיות הן של נור (ספורט), תמר ומתמטיקה, וראניה ומתמטיקה.

**מי קבע את הסדר ביניהן? אף אחד.** כשיש **תיקו** במפתח המיון, בסיס הנתונים חופשי להחזיר את השורות באיזה סדר שיבחר — ואין הבטחה שההרצה הבאה תחזיר את אותו סדר. אם הסדר חשוב לכם (ולכן גם אם ה‑`LIMIT` חשוב לכם), **הוסיפו מפתח שני ששובר את התיקו**:

</div>

```sql
ORDER BY Grades.Grade DESC, Grades.StudentId;
```

<div dir="rtl">

<figure dir="ltr" class="dbtable">

| StudentId | CourseCode | Grade |
|:---:|:---:|:---:|
| 1002 | 15 | 100 |
| 1010 | 11 | 100 |
| 1016 | 11 | 100 |
| 1016 | 13 | 99 |
| 1013 | 17 | 98 |

</figure>

**ש4.** שני ה‑`NULL` נפלו **בהתחלה**, **לפני** הציון 39.

ב‑SQLite (וגם ב‑MySQL ו‑PostgreSQL) `NULL` נחשב **הקטן מכולם** במיון עולה. ⚠️ **באורקל זה הפוך** — שם `NULL` גדול מכולם, ובמיון עולה הוא יופיע **בסוף**. זהו הבדל דיאלקט אמיתי, ולכן אל תסתמכו על מקום ה‑`NULL`: אם הוא חשוב, הוציאו אותו ב‑`WHERE` או טפלו בו במפורש.

<figure dir="ltr" class="dbtable">

| StudentId | CourseCode | Grade |
|:---:|:---:|:---:|
| 1004 | 14 | NULL |
| 1009 | 12 | NULL |
| 1012 | 16 | 39 |
| 1012 | 16 | 42 |
| 1012 | 12 | 47 |
| 1004 | 16 | 48 |

</figure>

**ש5.** **לינא ראשונה** — לפני כיתה 101. אותו כלל: `NULL` קטן מהכול במיון עולה. פתאום "התלמידה שטרם שובצה" פותחת את דוח הכיתות, וזה בדיוק סוג הבאג שמגיע לדוח מודפס.

<figure dir="ltr" class="dbtable">

| ClassCode | LastName | FirstName |
|:---:|:---:|:---:|
| NULL | חמוד | לינא |
| 101 | חלבי | אדם |
| 101 | כהן | יואב |
| 101 | עזאם | נור |
| 101 | שחר | נועם |
| 102 | אברהם | רוני |
| … | … | … |
| 105 | פרץ | דניאל |

</figure>

**ש6.** הפעם סאלי נפלה **בסוף קבוצת ה‑F** — כי המפתח השני הוא `DESC`, ו‑`NULL` הקטן מכולם עובר לסוף. **אותו ערך `NULL`, מקום הפוך, רק כי הפכנו את כיוון המיון.**

<figure dir="ltr" class="dbtable">

| Gender | FirstName | BirthDate |
|:---:|:---:|:---:|
| F | מאיה | 2011-11-30 |
| F | נור | 2011-07-22 |
| F | לינא | 2010-10-19 |
| F | שירה | 2010-09-25 |
| F | ג'וד | 2010-08-29 |
| F | תמר | 2010-04-07 |
| F | ראניה | 2009-12-12 |
| F | הדיל | 2009-10-05 |
| F | סאלי | NULL |
| M | נועם | 2011-09-02 |
| M | רוני | 2011-05-18 |
| M | אדם | 2011-03-14 |
| M | יואב | 2011-01-09 |
| M | כרים | 2010-12-03 |
| M | ליאור | 2010-06-16 |
| M | עומר | 2010-02-11 |
| M | איתי | 2009-03-27 |
| M | דניאל | 2009-01-20 |

</figure>

**ש7.** המיון זהה לש2 — ומובן: הכפלה ב‑12 היא פעולה **מונוטונית**, היא לא משנה את הסדר. אבל SQL לא יודע את זה; הוא חישב את הביטוי בכל שורה ומיין לפי התוצאה.

<figure dir="ltr" class="dbtable">

| LastName | AnnualSalary |
|:---:|:---:|
| שמש | 183600 |
| סרחאן | 174000 |
| מזרחי | 157200 |
| זיאד | 153600 |
| בר-לב | 134400 |
| אבו-ראס | 124800 |
| חדאד | 117600 |

</figure>

**ש8.** **כן, עובד** — ותוצאה זהה. ה‑`ORDER BY` הוא השלב **האחרון** בביצוע הלוגי, ובשלב הזה הכינויים כבר קיימים. (זכרו: ב‑`WHERE` הם **לא** קיימים, כי `WHERE` רץ **לפני** ה‑`SELECT`.)

**ש9.** `ORDER BY 2 DESC, 1` = "לפי העמודה השנייה ברשימת ה‑`SELECT`, יורד; ואז לפי הראשונה, עולה". שימו לב שהתיקו ב‑3 שעות נשבר נכון (`מבוא לבסיסי נתונים` לפני `מתמטיקה 3 יח"ל`), וכך גם התיקו ב‑2 שעות.

<figure dir="ltr" class="dbtable">

| CourseName | WeeklyHours |
|:---:|:---:|
| מתמטיקה 5 יח"ל | 5 |
| אנגלית 4 יח"ל | 4 |
| מבוא לבסיסי נתונים | 3 |
| מתמטיקה 3 יח"ל | 3 |
| היסטוריה | 2 |
| חינוך גופני | 2 |
| סדנת פרויקטים | 2 |

</figure>

> ⚠️ **זה נוח ומסוכן.** ברגע שמישהו יוסיף עמודה ל‑`SELECT`, `ORDER BY 2` יתחיל למיין לפי משהו אחר — בשקט. בבחינה זה מותר; בקוד אמיתי כתבו שם עמודה.

**ש10.** השאילתה החזירה את **סאלי חסון** במקום הראשון — ולסאלי אין תאריך לידה בכלל.

זהו ש4 וש5 שחוזרים, אבל הפעם **עם `LIMIT`, וזה מה שהופך את זה למלכודת של ממש**: ה‑`NULL` לא רק נראה במקום מוזר — הוא **דחף תלמיד אמיתי מחוץ לרשימה**. הדוח טוען שלושה "ותיקים", ואחד מהם שגוי והרביעי האמיתי נעלם.

**התיקון** — הוציאו את ה‑`NULL` ב‑`WHERE`, כי "הוותיק ביותר" חל רק על מי שתאריך הלידה שלו ידוע:

</div>

```sql
SELECT Students.FirstName, Students.BirthDate FROM Students
WHERE  Students.BirthDate IS NOT NULL
ORDER  BY Students.BirthDate LIMIT 3;
```

<div dir="rtl">

| | השגויה | המתוקנת |
|---|---------|----------|
| 1 | **סאלי · NULL** | דניאל · 2009-01-20 |
| 2 | דניאל · 2009-01-20 | איתי · 2009-03-27 |
| 3 | איתי · 2009-03-27 | **הדיל · 2009-10-05** |

> 💡 **הכלל:** `ORDER BY` + `LIMIT` על עמודה שיכולה להיות `NULL` — **תמיד** שאלו את עצמכם איפה ה‑`NULL` נופל.

**ש11.** **9 שורות.** הציון הנמוך בבית הספר הוא **39**, של ג'וד מנסור (1012) במתמטיקה 3 יח"ל, מחצית ב'. ג'וד מופיעה כאן **ארבע פעמים** — יותר מכל תלמיד אחר.

<figure dir="ltr" class="dbtable">

| StudentId | Grade |
|:---:|:---:|
| 1012 | 39 |
| 1012 | 42 |
| 1012 | 47 |
| 1004 | 48 |
| 1012 | 51 |
| 1009 | 54 |
| 1003 | 55 |
| 1006 | 58 |
| 1015 | 59 |

</figure>

**ש12.** ההודעה:

</div>

```text
near "WHERE": syntax error
```

<div dir="rtl">

הסדר הנכון הוא תמיד:

</div>

```text
SELECT   ...      -- אילו עמודות
FROM     ...      -- מאיזו טבלה
WHERE    ...      -- אילו שורות
ORDER BY ...      -- באיזה סדר      <-- אחרון, תמיד
```

<div dir="rtl">

**ולמה זה לא שרירותי?** כי זה גם סדר **הביצוע** המעשי: קודם שולפים את הטבלה (`FROM`), אחר כך זורקים שורות שלא עומדות בתנאי (`WHERE`), ורק את מה שנשאר יש טעם למיין (`ORDER BY`). למיין 18 שורות ואחר כך לזרוק 14 מהן זה בזבוז — ולכן השפה בכלל לא מרשה לכתוב את זה.

</div>
<!-- classroom:end -->
