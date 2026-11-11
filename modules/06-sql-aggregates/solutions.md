<div dir="rtl">

# מודול 23 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 כל הפלטים אמיתיים, מהרצה על בסיס הנתונים המוכן, נכון ל‑`'2026-09-21'`.

---

## ✅ תרגיל 1 — חמש הפונקציות

</div>

```sql
-- a   4
SELECT COUNT(*) FROM person WHERE role = 'volunteer';

-- b   2013-03-01 | 2024-02-14
SELECT MIN(joined_date), MAX(joined_date) FROM person WHERE role = 'volunteer';

-- c
SELECT SUM(cost) AS total, ROUND(AVG(cost), 2) AS avg, COUNT(*) AS n FROM vaccination;
```

```text
total   avg    n
------  -----  --
2370.0  84.64  28
```

```sql
-- d   1950.0 | 2024-01-12
SELECT MAX(amount)       FROM expense WHERE category = 'food';
SELECT MIN(expense_date) FROM expense WHERE category = 'medical';

-- e   9 | 22.09
SELECT COUNT(*) AS dogs, ROUND(AVG(weight_kg), 2) AS avg_kg FROM animal WHERE species_id = 1;
```

<div dir="rtl">

---

## ✅ תרגיל 2 — שלושה סוגי COUNT

</div>

```sql
-- a
SELECT COUNT(*) AS people, COUNT(phone) AS with_phone, COUNT(DISTINCT city) AS cities
FROM   person;
```

```text
people  with_phone  cities
------  ----------  ------
12      11          7
```

```sql
-- b   2 | 19 | 9
SELECT COUNT(*)                 FROM intake WHERE brought_by IS NULL;
SELECT COUNT(brought_by)        FROM intake;
SELECT COUNT(DISTINCT brought_by) FROM intake;

-- c   11 shots | 8 animals
SELECT COUNT(*)                  FROM vaccination WHERE given_date LIKE '2024%';
SELECT COUNT(DISTINCT animal_id) FROM vaccination WHERE given_date LIKE '2024%';
```

<div dir="rtl">

**ד.** `COUNT(*)` = **20**, `COUNT(breed)` = **16**. `COUNT(breed)` מדלג על 4 החיות שהגזע שלהן NULL. "כמה חיות יש" = **`COUNT(*)`** — סופר שורות, לא ערכים.

> 💡 **שימו לב לסעיף ב':** 2 + 19 = 21 = כל הקליטות. `COUNT(*) WHERE … IS NULL` + `COUNT(עמודה)` = `COUNT(*)` — תמיד. זו בדיקה טובה שהבנתם.

---

## ✅ תרגיל 3 — NULL וקבוצה ריקה

</div>

```sql
-- a
SELECT ROUND(AVG((JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25), 2)       AS avg_age,
       ROUND(SUM((JULIANDAY('2026-09-21') - JULIANDAY(birth_date)) / 365.25) / COUNT(*), 2) AS wrong
FROM   animal;
-- 5.57 | 4.73
```

<div dir="rtl">

`AVG` מחלק ב‑17 (מי שהגיל שלו ידוע). `SUM / COUNT(*)` מחלק ב‑20 — כאילו ל‑Coco, Lily ו‑Kiwi גיל 0. **`AVG` צודק.** (`SUM / COUNT(birth_date)` היה נותן גם הוא 5.57.)

</div>

```sql
-- b   SUM -> NULL, COUNT -> 0
SELECT SUM(amount), COUNT(*) FROM expense WHERE category = 'toys';

-- fixed
SELECT COALESCE(SUM(amount), 0) FROM expense WHERE category = 'toys';     -- 0

-- c   any filter that matches no row, e.g.
SELECT MAX(weight_kg) FROM animal WHERE species_id = 99;                  -- NULL
```

<div dir="rtl">

**ג.** `MAX` (וגם `MIN`, `SUM`, `AVG`) מחזיר NULL כשאין **אף ערך** שאינו NULL: אין שורות בכלל, או שכל הערכים NULL (`SELECT MAX(breed) FROM animal WHERE breed IS NULL`).

---

## ✅ תרגיל 4 — עם WHERE ועם JOIN

</div>

```sql
-- a   16920.0
SELECT SUM(amount) FROM expense WHERE expense_date BETWEEN '2024-01-01' AND '2024-12-31';

-- b   2520.0
SELECT SUM(e.amount)
FROM   expense e
JOIN   animal a ON a.animal_id = e.animal_id
WHERE  a.name = 'Max';

-- c   7 | 4.13 | 2.9 | 5.5
SELECT COUNT(*), ROUND(AVG(a.weight_kg), 2), MIN(a.weight_kg), MAX(a.weight_kg)
FROM   animal a
JOIN   species s ON s.species_id = a.species_id
WHERE  s.name = 'Cat';

-- d
SELECT SUM(ad.fee_paid) AS haifa_total
FROM   adoption ad
JOIN   person p ON p.person_id = ad.adopter_id
WHERE  p.city = 'Haifa';
-- 1250.0   (Dana 300 + 400, Lior 200 + 150, Omer 200)
```

<div dir="rtl">

---

## ✅ תרגיל 5 — ספירה מותנית

</div>

```sql
-- a
SELECT SUM(CASE WHEN sex = 'M' THEN 1 ELSE 0 END) AS males,
       SUM(CASE WHEN sex = 'F' THEN 1 ELSE 0 END) AS females,
       SUM(CASE WHEN sex = 'U' THEN 1 ELSE 0 END) AS unknown
FROM   animal;
```

```text
males  females  unknown
-----  -------  -------
10     9        1
```

```sql
-- b
SELECT SUM(CASE WHEN STRFTIME('%Y', adoption_date) = '2023' THEN fee_paid ELSE 0 END) AS y2023,
       SUM(CASE WHEN STRFTIME('%Y', adoption_date) = '2024' THEN fee_paid ELSE 0 END) AS y2024,
       SUM(CASE WHEN STRFTIME('%Y', adoption_date) = '2025' THEN fee_paid ELSE 0 END) AS y2025
FROM   adoption;
```

```text
y2023  y2024   y2025
-----  ------  -----
500.0  1150.0  550.0
```

```sql
-- c
SELECT SUM(CASE WHEN category = 'medical'   THEN amount ELSE 0 END) AS medical,
       SUM(CASE WHEN category = 'food'      THEN amount ELSE 0 END) AS food,
       SUM(CASE WHEN category = 'utilities' THEN amount ELSE 0 END) AS utilities
FROM   expense;
```

```text
medical  food    utilities
-------  ------  ---------
7470.0   7490.0  3770.0
```

```sql
-- d   40.0
SELECT ROUND(100.0 * SUM(CASE WHEN status = 'adopted' THEN 1 ELSE 0 END) / COUNT(*), 1)
FROM   animal;

-- e   11 | 8 | 2
SELECT SUM(CASE WHEN intake_type = 'stray'     THEN 1 ELSE 0 END) AS strays,
       SUM(CASE WHEN intake_type = 'surrender' THEN 1 ELSE 0 END) AS surrenders,
       SUM(CASE WHEN intake_type = 'transfer'  THEN 1 ELSE 0 END) AS transfers
FROM   intake;
```

<div dir="rtl">

> 💡 **סעיף ב' ו‑ג' הם "טבלת ציר" (pivot)** — ערכים מעמודה אחת (שנה, קטגוריה) הופכים לכותרות עמודות. זה מה שאקסל עושה ב"PivotTable". החיסרון: צריך לדעת מראש את כל הערכים. במודול 24, `GROUP BY` ייתן את אותו מידע **בשורות** — לכל ערך שקיים.

---

## ✅ תרגיל 6 — המלכודות

</div>

```sql
-- a   SQLite: Zoe | 2016-01-01  (a lucky guess)   Oracle: ORA-00937
SELECT name, MIN(birth_date) FROM animal;

-- the correct way
SELECT name, birth_date
FROM   animal
WHERE  birth_date = (SELECT MIN(birth_date) FROM animal);
-- Zoe | 2016-01-01

-- b   8
SELECT COUNT(*) FROM animal WHERE weight_kg > (SELECT AVG(weight_kg) FROM animal);
```

<div dir="rtl">

**ג.** ל‑Rocky יש **הוצאה אחת** (600 ₪, צילום ירך) ו‑**4 חיסונים**. ה‑JOIN יוצר שורה לכל **צירוף** של הוצאה וחיסון: 1 × 4 = 4 שורות, וכל אחת עם `amount = 600`. `SUM` = 2400 — **פי 4 מהאמת**.

</div>

```text
   Rocky -- expense 22 (600) -- vaccination 5
   Rocky -- expense 22 (600) -- vaccination 6
   Rocky -- expense 22 (600) -- vaccination 27      4 rows, the 600 counted 4 times
   Rocky -- expense 22 (600) -- vaccination 28
```

```sql
-- correct: only the table you aggregate
SELECT SUM(e.amount)
FROM   expense e
JOIN   animal a ON a.animal_id = e.animal_id
WHERE  a.name = 'Rocky';                           -- 600.0
```

<div dir="rtl">

> 🔑 **שתי טבלאות "רבים" באותו JOIN = מכפלה.** זה הבאג הכי נפוץ בדוחות אמיתיים — והכי מסוכן, כי המספר נראה סביר.

</div>

```sql
-- d
SELECT (SELECT COUNT(*) FROM animal WHERE status = 'available')                  AS waiting,
       (SELECT COUNT(*) FROM adoption)                                           AS adoptions,
       (SELECT SUM(fee_paid) FROM adoption)                                      AS income,
       (SELECT SUM(amount)   FROM expense)                                       AS expenses,
       (SELECT SUM(fee_paid) FROM adoption) - (SELECT SUM(amount) FROM expense)  AS balance;
```

```text
waiting  adoptions  income  expenses  balance
-------  ---------  ------  --------  --------
9        9          2200.0  19800.0   -17600.0
```

<div dir="rtl">

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
SELECT AVG(Products.Price) AS AvgPrice, MAX(Products.Price) AS MaxPrice, MIN(Products.Price) AS MinPrice FROM Products;
```

**1** רשומות. השורה הראשונה: `28.866363 · 263.50 · 2.50`

**W2.**

```sql
SELECT COUNT(*) AS cnt FROM Products WHERE Products.CategoryID = 1;
```

**1** רשומות. השורה הראשונה: `12`


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
SELECT COUNT(*) AS Students FROM Students;

-- ש2
SELECT COUNT(*) AS AllRows, COUNT(Grades.Grade) AS WithGrade,
       COUNT(*) - COUNT(Grades.Grade) AS Missing FROM Grades;

-- ש3
SELECT ROUND(AVG(Grades.Grade), 2) AS AvgReal,
       ROUND(AVG(COALESCE(Grades.Grade, 0)), 2) AS AvgWithZeros FROM Grades;

-- ש4
SELECT MIN(Grades.Grade) AS Lowest, MAX(Grades.Grade) AS Highest FROM Grades;

-- ש5
SELECT SUM(Teachers.Salary) AS Payroll, ROUND(AVG(Teachers.Salary), 2) AS AvgSalary,
       MIN(Teachers.Salary) AS Min1, MAX(Teachers.Salary) AS Max1 FROM Teachers;

-- ש6
SELECT COUNT(*) AS Teachers1, COUNT(DISTINCT Teachers.Subject) AS Subjects FROM Teachers;

-- ש7
SELECT COUNT(*) AS GradeRows, COUNT(DISTINCT Grades.StudentId) AS StudentsWithGrades FROM Grades;

-- ש8
SELECT MIN(Absences.AbsenceDate) AS First1, MAX(Absences.AbsenceDate) AS Last1,
       COUNT(*) AS Total FROM Absences;

-- ש9
SELECT ROUND(AVG(Grades.Grade), 2) AS AvgMath5, COUNT(*) AS HowMany
FROM   Grades WHERE Grades.CourseCode = 11;

-- ש10
SELECT SUM(Grades.Grade) AS Total, COUNT(*) AS Rows1, COUNT(Grades.Grade) AS NonNull,
       ROUND(CAST(SUM(Grades.Grade) AS REAL) / COUNT(*), 2) AS DividedBy60,
       ROUND(AVG(Grades.Grade), 2) AS AvgFunction FROM Grades;

-- ש11
SELECT COUNT(*) AS AllStudents, COUNT(Students.Phone) AS WithPhone,
       COUNT(Students.BirthDate) AS WithBirthDate, COUNT(Students.ClassCode) AS WithClass
FROM   Students;

-- ש12
SELECT Students.FirstName, MAX(Grades.Grade) AS Best
FROM   Students, Grades WHERE Students.StudentId = Grades.StudentId;
-- והדרך הנכונה:
SELECT Students.FirstName, Grades.Grade FROM Students, Grades
WHERE  Students.StudentId = Grades.StudentId
  AND  Grades.Grade = (SELECT MAX(Grades.Grade) FROM Grades);
```

<div dir="rtl">

**ש1.** **18.** `COUNT(*)` סופר **שורות**, ולא מסתכל בכלל על התוכן — לכן `NULL`ים לא מעניינים אותו.

<figure dir="ltr" class="dbtable">

| Students |
|:---:|
| 18 |

</figure>

**ש2.** **60 שורות, 58 ציונים, 2 חסרים.**

ההבדל בין `COUNT(*)` ל‑`COUNT(עמודה)` הוא כל השיעור בשורה אחת: הראשון סופר שורות, השני סופר **ערכים שאינם `NULL`** באותה עמודה.

<figure dir="ltr" class="dbtable">

| AllRows | WithGrade | Missing |
|:---:|:---:|:---:|
| 60 | 58 | 2 |

</figure>

> 💡 `COUNT(*) - COUNT(עמודה)` הוא הדרך הקצרה לשאול "**כמה חסרים לי בעמודה הזאת?**" — שאילתת בדיקת איכות נתונים שכדאי לזכור.

**ש3.** **77.97 מול 75.37 — הפרש של 2.6 נקודות**, משתי שורות בלבד מתוך 60.

**הנכון הוא 77.97.** `AVG(Grade)` מחלק ב‑58 — מספר הציונים שקיימים. הגרסה השנייה המציאה שני אפסים, חילקה ב‑60, והורידה את הממוצע הבית‑ספרי. מאיה לא נבחנה בהיסטוריה; זה לא אומר שהיא קיבלה 0.

<figure dir="ltr" class="dbtable">

| AvgReal | AvgWithZeros |
|:---:|:---:|
| 77.97 | 75.37 |

</figure>

**ש4.** **39 עד 100.** המינימום הוא הציון של ג'וד מנסור במתמטיקה מחצית ב'. `MIN`/`MAX` **מתעלמות מ‑`NULL`** — אחרת המינימום היה "לא ידוע" לנצח.

<figure dir="ltr" class="dbtable">

| Lowest | Highest |
|:---:|:---:|
| 39 | 100 |

</figure>

**ש5.** בית הספר משלם **87,100 ₪** בחודש למורים.

<figure dir="ltr" class="dbtable">

| Payroll | AvgSalary | Min1 | Max1 |
|:---:|:---:|:---:|:---:|
| 87100 | 12442.86 | 9800 | 15300 |

</figure>

**ש6.** **7 מורים, 6 מקצועות** — נביל וגלית שניהם מלמדים מתמטיקה. `DISTINCT` **בתוך** הפונקציה המצרפית: קודם זורקים כפילויות, אחר כך סופרים.

<figure dir="ltr" class="dbtable">

| Teachers1 | Subjects |
|:---:|:---:|
| 7 | 6 |

</figure>

**ש7.** **60 שורות, 17 תלמידים.** 18 − 17 = 1: ל**תלמיד אחד אין אף ציון** — לינא חמוד, שנרשמה ב‑10 בספטמבר.

שימו לב מה עשינו כאן: גילינו חסר **בלי `JOIN` ובלי `IS NULL`**, רק בהשוואת שתי ספירות. זו בדיקה שלוקחת שנייה וכדאי לעשות אותה לכל טבלת קשר.

<figure dir="ltr" class="dbtable">

| GradeRows | StudentsWithGrades |
|:---:|:---:|
| 60 | 17 |

</figure>

**ש8.** 16 היעדרויות, מ‑2 בספטמבר עד 18 בספטמבר.

**למה `MIN`/`MAX` עובדות על תאריכים?** כי התאריכים נשמרים כטקסט בפורמט `YYYY-MM-DD`, ובפורמט הזה **הסדר האלפביתי זהה לסדר הכרונולוגי** — `'2026-09-02'` קטן מ‑`'2026-09-18'` גם כמחרוזת. זו בדיוק הסיבה שהפורמט הזה הוא התקן (ISO 8601). בפורמט `02/09/2026` זה היה נשבר מיד.

<figure dir="ltr" class="dbtable">

| First1 | Last1 | Total |
|:---:|:---:|:---:|
| 2026-09-02 | 2026-09-18 | 16 |

</figure>

**ש9.** **88.2 על 15 ציונים.** מתמטיקה 5 יח"ל היא המקצוע החזק בבית הספר — למעלה מ‑10 נקודות מעל הממוצע הכללי. (הסבר אפשרי: לשם נרשמים התלמידים החזקים. זו שאלה לשיעור 24.)

<figure dir="ltr" class="dbtable">

| AvgMath5 | HowMany |
|:---:|:---:|
| 88.2 | 15 |

</figure>

**ש10.** `AVG` מחלק ב‑**58**, לא ב‑60.

<figure dir="ltr" class="dbtable">

| Total | Rows1 | NonNull | DividedBy60 | AvgFunction |
|:---:|:---:|:---:|:---:|:---:|
| 4522 | 60 | 58 | 75.37 | 77.97 |

</figure>

החשבון, במפורש:

</div>

```text
SUM(Grade)              = 4522      -- ה-NULLים לא נספרו בסכום
COUNT(*)                =   60      -- כל השורות
COUNT(Grade)            =   58      -- רק הציונים הקיימים

4522 / 60  =  75.37   <- מה שחישבנו ביד
4522 / 58  =  77.97   <- מה ש-AVG מחזיר
```

<div dir="rtl">

**במשפט אחד:** `AVG` **מתעלמת** מ‑`NULL` לגמרי — לא בסכום ולא במונה. היא עונה על "מה הממוצע של הציונים **שיש**", ולא על "מה הממוצע אם נחשיב חסר כאפס". שתי השאלות לגיטימיות, אבל רק אחת מהן היא מה ש‑`AVG` עושה, וכדאי לדעת איזו.

**ש11.** ארבעה מספרים, אותה טבלה:

<figure dir="ltr" class="dbtable">

| AllStudents | WithPhone | WithBirthDate | WithClass |
|:---:|:---:|:---:|:---:|
| 18 | 12 | 17 | 17 |

</figure>

| המספר | מה הוא אומר |
|--------|--------------|
| `COUNT(*) = 18` | **שורות** בטבלה — 18 תלמידים |
| `COUNT(Phone) = 12` | ל‑6 תלמידים אין טלפון |
| `COUNT(BirthDate) = 17` | לאחד (סאלי) חסר תאריך לידה |
| `COUNT(ClassCode) = 17` | אחת (לינא) טרם שובצה לכיתה |

**השורה התחתונה:** `COUNT(עמודה)` הוא לא "כמה תלמידים" — הוא "**כמה תלמידים עם נתון בעמודה הזאת**". מי שמדווח "יש לנו 12 תלמידים" כי הריץ `COUNT(Phone)` טעה ב‑6 תלמידים.

**ש12א.** **שורה אחת: `נור · 100`.**

**ש12ב.** **שלושה** תלמידים קיבלו 100 — נור עזאם, תמר שושן וראניה עבאס.

<figure dir="ltr" class="dbtable">

| FirstName | Grade |
|:---:|:---:|
| נור | 100 |
| תמר | 100 |
| ראניה | 100 |

</figure>

כלומר התשובה בסעיף א' **הסתירה שתי תלמידות**. היא גם לא "שגויה" במובן הפשוט: `MAX` הוא אכן 100, ונור אכן קיבלה 100. פשוט אין שם מקום לשלושתן — `MAX` מחזיר **מספר אחד**, אז השאילתה חייבת להחזיר **שורה אחת**, ו‑SQLite בחר עבורכם איזה שם לשים בה.

**ש12ג.** באורקל זו **שגיאה**: `ORA-00937: not a single-group group function`.

**ולמה שגיאה עדיפה?** כי שגיאה **עוצרת אותך**. היא אומרת "עירבבת שתי רמות: `FirstName` הוא נתון של שורה, `MAX` הוא נתון של כל הטבלה — תחליט מה אתה שואל". SQLite, לעומת זה, מחזיר תוצאה שנראית תקינה לגמרי, אף אחד לא בודק אותה, והיא מגיעה לדוח של המנהלת עם שם אחד מתוך שלושה.

**הדרך הנכונה** היא לשאול בשני שלבים: קודם *מה* המקסימום, ואחר כך *מי* מגיע אליו — וזו **תת‑שאילתה**:

</div>

```sql
SELECT Students.FirstName, Grades.Grade
FROM   Students, Grades
WHERE  Students.StudentId = Grades.StudentId
  AND  Grades.Grade = (SELECT MAX(Grades.Grade) FROM Grades);
```

<div dir="rtl">

> 🔮 תת‑שאילתות הן בדיוק הנושא של שיעור 24, לצד `GROUP BY` — שיענה על "מה המקסימום של **כל** תלמיד", 17 תשובות בשאילתה אחת.

</div>
<!-- classroom:end -->
