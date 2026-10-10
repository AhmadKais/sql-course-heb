<div dir="rtl">

# מודול 21 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 כל הפלטים אמיתיים, מהרצה על בסיס הנתונים המוכן. תא ריק בפלט = NULL.

---

## ✅ תרגיל 1 — התוצר הקרטזי

</div>

```sql
-- a   12 x 9 = 108
SELECT COUNT(*) FROM person, adoption;

-- b   9 -- one per adoption
SELECT COUNT(*)
FROM   person p
JOIN   adoption ad ON ad.adopter_id = p.person_id;
```

<div dir="rtl">

**ג.** אין תנאי חיבור — רק סינון. 9 חיות זמינות × 4 מינים = **36**. כל חיה מופיעה עם **כל** מין. התיקון:

</div>

```sql
SELECT a.name, s.name
FROM   animal a
JOIN   species s ON s.species_id = a.species_id
WHERE  a.status = 'available';      -- 9 rows
```

<div dir="rtl">

---

## ✅ תרגיל 2 — שתי טבלאות

</div>

```sql
-- a
SELECT a.name, s.name AS species
FROM   animal a
JOIN   species s ON s.species_id = a.species_id
WHERE  s.name = 'Cat'
ORDER  BY a.name;
-- Felix, Lily, Mitzi, Nala, Oscar, Simba, Tom

-- b
SELECT a.name, i.intake_date, i.intake_type
FROM   intake i
JOIN   animal a ON a.animal_id = i.animal_id
WHERE  i.intake_type = 'stray'
ORDER  BY i.intake_date
LIMIT  5;
```

```text
name   intake_date  intake_type
-----  -----------  -----------
Luna   2023-03-14   stray
Rocky  2023-05-20   stray
Mitzi  2023-06-11   stray
Tom    2023-08-19   stray
Max    2023-11-05   stray
```

```sql
-- c
SELECT e.expense_date, e.amount, e.description
FROM   expense e
JOIN   animal a ON a.animal_id = e.animal_id
WHERE  a.name = 'Max';
```

```text
expense_date  amount  description
------------  ------  ------------------
2024-01-12    420.0   x-ray + medication
2024-08-22    2100.0  leg surgery
```

```sql
-- d   old style -- same 7 rows
SELECT a.name, s.name AS species
FROM   animal a, species s
WHERE  s.species_id = a.species_id
  AND  s.name = 'Cat'
ORDER  BY a.name;
```

<div dir="rtl">

> 💡 **למה בסעיף א' חיפשנו `s.name = 'Cat'` ולא `species_id = 2`?** כי `2` הוא מספר פנימי שאיש לא אמור לזכור. בשאילתה שאנשים קוראים — מחפשים לפי מה שהם מבינים.

---

## ✅ תרגיל 3 — שלוש טבלאות ויותר

</div>

```sql
-- a
SELECT a.name, i.intake_date, p.first_name || ' ' || p.last_name AS brought_by
FROM   intake i
JOIN   animal a ON a.animal_id = i.animal_id
JOIN   person p ON p.person_id = i.brought_by
WHERE  p.first_name = 'Noa'
ORDER  BY i.intake_date;
```

```text
name   intake_date  brought_by
-----  -----------  ----------
Luna   2023-03-14   Noa Peretz
Mitzi  2023-06-11   Noa Peretz
Nala   2024-01-22   Noa Peretz
Lily   2024-07-09   Noa Peretz
Bunny  2025-02-20   Noa Peretz
```

```sql
-- b
SELECT p.first_name || ' ' || p.last_name AS vet, a.name, v.given_date
FROM   vaccination v
JOIN   person p ON p.person_id = v.vet_id
JOIN   animal a ON a.animal_id = v.animal_id
WHERE  p.last_name = 'Nahum'
  AND  v.given_date >= '2024-01-01'
ORDER  BY v.given_date;
```

```text
vet             name     given_date
--------------  -------  ----------
Dr. Maya Nahum  Thumper  2024-02-20
Dr. Maya Nahum  Oscar    2024-04-22
Dr. Maya Nahum  Oscar    2024-04-22     <- two DIFFERENT vaccines on the same day
Dr. Maya Nahum  Daisy    2024-11-06
Dr. Maya Nahum  Felix    2025-01-20
Dr. Maya Nahum  Bunny    2025-02-25
```

<div dir="rtl">

**Oscar פעמיים** — כי ב‑22/04/2024 הוא קיבל **שני** חיסונים (Rabies ו‑FVRCP). שתי שורות ב‑`vaccination`, שתי שורות בתוצאה. **`JOIN` לא מאחד שורות — הוא מוסיף להן עמודות.** אם נוסיף את `vaccine_type` נראה את ההבדל.

</div>

```sql
-- c   four tables
SELECT a.name AS animal, s.name AS species,
       p.first_name || ' ' || p.last_name AS adopter, p.city, ad.fee_paid
FROM   adoption ad
JOIN   animal  a ON a.animal_id  = ad.animal_id
JOIN   species s ON s.species_id = a.species_id
JOIN   person  p ON p.person_id  = ad.adopter_id
WHERE  p.city = 'Haifa'
ORDER  BY ad.adoption_date;
```

```text
animal   species  adopter     city   fee_paid
-------  -------  ----------  -----  --------
Luna     Dog      Dana Cohen  Haifa  300.0
Bella    Dog      Lior Bar    Haifa  200.0
Zoe      Dog      Omer Dayan  Haifa  200.0
Charlie  Dog      Dana Cohen  Haifa  400.0
Kiwi     Parrot   Lior Bar    Haifa  150.0
```

```sql
-- d   species joined TWICE: once for the vaccine, once for the animal
SELECT a.name, vt.name AS vaccine, s.name AS vaccine_for, sa.name AS animal_species
FROM   vaccination  v
JOIN   animal       a  ON a.animal_id        = v.animal_id
JOIN   vaccine_type vt ON vt.vaccine_type_id = v.vaccine_type_id
JOIN   species      s  ON s.species_id       = vt.species_id
JOIN   species      sa ON sa.species_id      = a.species_id
WHERE  vt.species_id <> a.species_id;
-- (no rows) -- every animal got a vaccine meant for its own species. Good.
```

<div dir="rtl">

> 💡 **אותה טבלה פעמיים, עם שני כינויים (`s` ו‑`sa`)** — כי יש שתי שאלות שונות: "לאיזה מין החיסון?" ו"מה המין של החיה?". זה כבר כמעט self join.

---

## ✅ תרגיל 4 — Nonequijoin

</div>

```sql
-- a
SELECT a.name, a.weight_kg, b.band
FROM   animal a
JOIN   size_band b ON a.weight_kg BETWEEN b.min_kg AND b.max_kg
ORDER  BY a.weight_kg;
-- 20 rows: Kiwi, Coco tiny ... Rex large  (same as the CASE in module 20)
```

<div dir="rtl">

**ב.** עם `max_kg = 4` ל‑`small`, נשאר **חור** בין 4 ל‑10 — וחמש חיות נופלות לתוכו:

</div>

```sql
SELECT a.name, a.weight_kg
FROM   animal a
LEFT   JOIN size_band b ON a.weight_kg BETWEEN b.min_kg AND b.max_kg
WHERE  b.band IS NULL;
```

```text
name     weight_kg
-------  ---------
Simba    4.2
Tom      4.8
Felix    5.0
Oscar    5.5
Charlie  7.2
```

<div dir="rtl">

ב‑`JOIN` הרגיל הן פשוט **נעלמות** — 15 שורות במקום 20, בלי שום שגיאה. **התיקון:** טווחים צמודים — כל `min` שווה ל‑`max` של הקודם — ותנאי חצי‑פתוח: `a.weight_kg >= b.min_kg AND a.weight_kg < b.max_kg`. כך אין חורים ואין חפיפות, לכל ערך עשרוני.

> 🔑 **טריק הבדיקה:** `LEFT JOIN … WHERE b.band IS NULL` מוצא בדיוק את מי שנפל בין הכיסאות. הריצו אותו בכל פעם שאתם יוצרים טבלת טווחים.

</div>

```sql
-- c
CREATE TABLE fee_discount (min_age INTEGER, max_age INTEGER, pct INTEGER);
INSERT INTO fee_discount VALUES (0, 7, 0), (8, 30, 50);

SELECT a.name,
       CAST((JULIANDAY('2026-09-21') - JULIANDAY(a.birth_date)) / 365.25 AS INTEGER) AS age,
       d.pct
FROM   animal a
JOIN   fee_discount d
       ON CAST((JULIANDAY('2026-09-21') - JULIANDAY(a.birth_date)) / 365.25 AS INTEGER)
          BETWEEN d.min_age AND d.max_age
WHERE  a.species_id = 1
ORDER  BY age DESC;
```

```text
name     age  pct
-------  ---  ---
Zoe      10   50
Rex      9    50
Bella    8    50
Daisy    6    0
Rocky    6    0
Luna     5    0
Shadow   5    0
Max      4    0
Charlie  2    0
```

<div dir="rtl">

---

## ✅ תרגיל 5 — Outer join

</div>

```sql
-- a   Coco, Nala, Lily, Kiwi
SELECT a.name
FROM   animal a
LEFT   JOIN vaccination v ON v.animal_id = a.animal_id
WHERE  v.vaccination_id IS NULL;

-- b
SELECT a.name, a.status
FROM   animal a
LEFT   JOIN adoption ad ON ad.animal_id = a.animal_id
WHERE  ad.adoption_id IS NULL
ORDER  BY a.name;
```

```text
name    status
------  ----------
Bunny   available
Coco    available
Daisy   deceased
Felix   available
Lily    available
Max     medical
Mitzi   available
Nala    quarantine
Oscar   available
Rex     available
Rocky   available
Shadow  available
```

```sql
-- c   10 animals with no expense rows
SELECT a.name
FROM   animal a
LEFT   JOIN expense e ON e.animal_id = a.animal_id
WHERE  e.expense_id IS NULL
ORDER  BY a.name;
-- Bunny, Charlie, Coco, Kiwi, Lily, Mitzi, Simba, Thumper, Tom, Zoe

-- d
SELECT p.first_name, p.last_name, p.role
FROM   person p
LEFT   JOIN intake i ON i.brought_by = p.person_id
WHERE  i.intake_id IS NULL;
```

```text
first_name  last_name  role
----------  ---------  ---------
Ruti        Almog      volunteer
Dr. Ron     Levi       vet
Dr. Maya    Nahum      vet
```

```sql
-- e
SELECT p.first_name, p.last_name
FROM   person p
LEFT   JOIN adoption ad ON ad.adopter_id = p.person_id
WHERE  p.role = 'adopter'
  AND  ad.adoption_id IS NULL;
-- (no rows)
```

<div dir="rtl">

**אין אף שורה — וזו תשובה נכונה, לא באג.** כל מי שמסומן `adopter` אכן אימץ. זה הגיוני: אדם נרשם כמאמץ **ברגע** האימוץ. **תוצאה ריקה היא מידע** — אל תניחו שהשאילתה שגויה רק כי לא יצא כלום. בדקו בשאילתה הפוכה (`JOIN` רגיל) שהיא מחזירה את כולם.

</div>

```sql
-- f
SELECT e.expense_id, e.description, COALESCE(a.name, 'general') AS animal
FROM   expense e
LEFT   JOIN animal a ON a.animal_id = e.animal_id
ORDER  BY e.expense_id;
```

```text
expense_id  description           animal
----------  --------------------  -------
1           dry food, 20 sacks    general
2           x-ray + medication    Max
3           electricity January   general
4           dental cleaning       Bella
5           cat litter            general
6           electricity February  general
...
```

<div dir="rtl">

---

## ✅ תרגיל 6 — `ON` מול `WHERE`

**א.** A מחזירה **3** שורות; B מחזירה **7**.

</div>

```text
A:                                    B:
name   given_date  cost               name   given_date  cost
-----  ----------  ----               -----  ----------  ----
Simba  2023-04-08  90.0               Simba  2023-04-08  90.0
Tom    2023-08-24  90.0               Mitzi
Oscar  2024-04-22  90.0               Tom    2023-08-24  90.0
                                      Nala
                                      Oscar  2024-04-22  90.0
                                      Lily
                                      Felix
```

<div dir="rtl">

ב‑A חסרים Mitzi, Nala, Lily ו‑Felix.

**ב.** **`ON` קובע מי מתחבר; `WHERE` קובע מי נשאר.** תנאי ב‑`ON` של `LEFT JOIN` רק מגביל אילו חיסונים מוצמדים — החתול נשאר בכל מקרה. תנאי ב‑`WHERE` רץ **אחרי** החיבור: אצל חתול בלי חיסון יקר, `v.cost` הוא NULL, `NULL >= 90` אינו true — והשורה נמחקת. ה‑`LEFT` הפך בפועל ל‑`JOIN` רגיל.

**ג.** **B.** "כל החתולים" — אז אסור שחתול ייעלם.

---

## ✅ תרגיל 7 — Self join

</div>

```sql
-- a
SELECT p1.first_name AS p1, p2.first_name AS p2, p1.last_name
FROM   person p1
JOIN   person p2 ON  p1.last_name = p2.last_name
                 AND p1.person_id < p2.person_id;
```

```text
p1    p2       last_name
----  -------  ---------
Amir  Dr. Ron  Levi
```

```sql
-- b
SELECT a1.name AS older, a2.name AS younger, a1.birth_date, a2.birth_date
FROM   animal a1
JOIN   animal a2 ON  a1.species_id = a2.species_id
                 AND a1.birth_date < a2.birth_date
WHERE  a1.species_id = 3;
```

```text
older    younger  birth_date  birth_date
-------  -------  ----------  ----------
Thumper  Bunny    2023-06-15  2024-01-01
```

<div dir="rtl">

> 💡 כאן `<` על **תאריך הלידה** עושה שתי עבודות: מונע זוג של חיה עם עצמה, **וגם** קובע מי "המבוגר" בכל זוג.

</div>

```sql
-- c
SELECT a.name, v1.given_date AS shot, v2.given_date AS later_shot
FROM   vaccination v1
JOIN   vaccination v2 ON  v1.animal_id       = v2.animal_id
                      AND v1.vaccine_type_id = v2.vaccine_type_id
                      AND v1.given_date      < v2.given_date
JOIN   animal a ON a.animal_id = v1.animal_id
ORDER  BY a.name, v1.given_date;
```

```text
name   shot        later_shot
-----  ----------  ----------
Luna   2023-03-20  2024-06-05
Rocky  2023-05-25  2024-05-28
Rocky  2023-05-25  2025-05-30     <- not the NEXT shot: it skips 2024
Rocky  2024-05-28  2025-05-30
```

<div dir="rtl">

**ד.** התנאי `v1.given_date < v2.given_date` אומר "**כל** חיסון מאוחר יותר", לא "החיסון **הבא**". ל‑Rocky שלושה חיסוני כלבת: 2023, 2024, 2025 — ולכן שלושה זוגות: 2023–2024, 2023–2025, 2024–2025. כדי לקבל רק את הבא צריך "**הקטן** מבין המאוחרים" — `MIN` ותת‑שאילתה, מודול 24.

---

## ✅ תרגיל 8 — היררכיה

</div>

```sql
-- a   see section 8.1 in the module (LEFT JOIN keeps Ruti)

-- b   leaves: nobody reports to them
SELECT s.name, s.job
FROM   staff s
LEFT   JOIN staff c ON c.manager_id = s.staff_id
WHERE  c.staff_id IS NULL;
```

```text
name      job
--------  ---------
Dr. Maya  vet
Amir      volunteer
Tamar     volunteer
```

<div dir="rtl">

> 💡 **שימו לב: זה בדיוק "בלי התאמה" מתרגיל 5** — רק שהטבלה הימנית היא אותה טבלה. `c` = "כפיף אפשרי". אם אין — אין כפיפים.

**ג.** אחרי `INSERT INTO staff VALUES (7, 'Yael', 'kennel volunteer', 5);` — יעל ברמה **4** (רותי 1 ⟵ נועה 2 ⟵ אמיר 3 ⟵ יעל 4). ובסעיף ב', אמיר כבר **לא** עלה — יש לו כפיפה.

</div>

```sql
-- d   walk UP the tree: start from Yael, each step joins to the manager
WITH RECURSIVE chain(staff_id, name, manager_id, step) AS (
  SELECT staff_id, name, manager_id, 0
  FROM   staff WHERE name = 'Yael'
  UNION ALL
  SELECT s.staff_id, s.name, s.manager_id, c.step + 1
  FROM   staff s JOIN chain c ON s.staff_id = c.manager_id     -- reversed direction
)
SELECT step, name FROM chain ORDER BY step;
```

```text
step  name
----  ----
0     Yael
1     Amir
2     Noa
3     Ruti
```

<div dir="rtl">

**ההבדל היחיד מהעץ במודול:** כיוון החיבור. למטה: `s.manager_id = t.staff_id` ("מי שהמנהל שלו בעץ"). למעלה: `s.staff_id = c.manager_id` ("המנהל של מי שכבר בשרשרת"). ב‑Oracle: `START WITH name = 'Yael' CONNECT BY PRIOR manager_id = staff_id`.

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
SELECT Customers.CustomerName, Orders.OrderID FROM Customers, Orders WHERE Customers.CustomerID = Orders.CustomerID AND Customers.Country = 'Germany';
```

**25** רשומות. השורה הראשונה: `Drachenblut Delikatessend · 10391`

**W2.**

```sql
SELECT Products.ProductName, Categories.CategoryName FROM Products, Categories WHERE Products.CategoryID = Categories.CategoryID;
```

**77** רשומות. השורה הראשונה: `Chais · Beverages`

**W3.**

```sql
SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName FROM Orders, Customers, Shippers WHERE Orders.CustomerID = Customers.CustomerID AND Orders.ShipperID = Shippers.ShipperID;
```

**196** רשומות. השורה הראשונה: `10248 · Wilman Kala · Federal Shipping`


</div>
<!-- w3schools:end -->

<!-- exam-style:start -->
<div dir="rtl">

---

## 🎓 תרגול בסגנון הבחינה: פתרונות

**ב1.** `Cities` · `CityCode`. זו **אותה שאילתה** כמו `FROM Members JOIN Cities ON Members.CityCode = Cities.CityCode`.

<figure dir="ltr" class="dbtable">

| FirstName | CityName |
|:---:|:---:|
| אדם | ירכא |
| נור | ירכא |
| יואב | כרמיאל |
| מאיה | כרמיאל |
| רוני | עכו |
| סאלי | עכו |
| עומר | נהריה |
| שירה | חיפה |
| כרים | ירכא |
| תמר | נהריה |
| ליאור | חיפה |
| ג'וד | ירכא |

</figure>

**ב2.** **72** = 12 משתתפים × 6 ערים. זה **תוצר קרטזי**: שכחו את תנאי החיבור.

<figure dir="ltr" class="dbtable">

| cnt |
|:---:|
| 72 |

</figure>

**ב3.** ```sql
SELECT Clubs.ClubName
FROM Clubs, ClubMembers
WHERE Clubs.ClubCode = ClubMembers.ClubCode
  AND ClubMembers.Id = 1001;
```
כאן מספיקות **שתי** טבלאות, כי Id כבר נמצא ב‑ClubMembers. כדי להציג גם את **שם** המשתתף, צריך להוסיף את Members ותנאי חיבור שני.

<figure dir="ltr" class="dbtable">

| ClubName |
|:---:|
| כדורגל צעירים |
| כדורסל |

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

</div>

```sql
-- ש1
SELECT Students.FirstName, Students.LastName, Classes.ClassName
FROM   Students, Classes WHERE Students.ClassCode = Classes.ClassCode;

-- ש2
SELECT Students.FirstName, Cities.CityName
FROM   Students, Cities WHERE Students.CityCode = Cities.CityCode;

-- ש3
SELECT Students.FirstName, Courses.CourseName, Grades.Term, Grades.Grade
FROM   Grades, Students, Courses
WHERE  Grades.StudentId = Students.StudentId
  AND  Grades.CourseCode = Courses.CourseCode
  AND  Students.StudentId = 1013
ORDER  BY Grades.Grade DESC;

-- ש4
SELECT Courses.CourseName, Teachers.FirstName, Teachers.LastName
FROM   Courses, Teachers WHERE Courses.TeacherCode = Teachers.TeacherCode;

-- ש5
SELECT Classes.ClassName, Classes.Grade, Teachers.FirstName || ' ' || Teachers.LastName AS Homeroom
FROM   Classes, Teachers WHERE Classes.TeacherCode = Teachers.TeacherCode
ORDER  BY Classes.ClassName;

-- ש6
SELECT COUNT(*) AS CartesianRows FROM Students, Classes;

-- ש7
SELECT Students.FirstName, Classes.ClassName
FROM   Students LEFT JOIN Classes ON Students.ClassCode = Classes.ClassCode
ORDER  BY Classes.ClassName;

-- ש8
SELECT Teachers.FirstName, Teachers.LastName, Teachers.Subject
FROM   Teachers LEFT JOIN Courses ON Courses.TeacherCode = Teachers.TeacherCode
WHERE  Courses.CourseCode IS NULL;

-- ש9
SELECT a.FirstName AS Student1, b.FirstName AS Student2, a.ClassCode
FROM   Students a, Students b
WHERE  a.ClassCode = b.ClassCode AND a.StudentId < b.StudentId AND a.ClassCode = 103;

-- ש10
SELECT t1.LastName AS Earns_More, t2.LastName AS Than
FROM   Teachers t1, Teachers t2
WHERE  t1.Salary > t2.Salary AND t1.TeacherCode = 3;

-- ש11
SELECT Students.FirstName, Courses.CourseName, Grades.Grade
FROM   Grades, Students, Courses
WHERE  Grades.StudentId = Students.StudentId
  AND  Grades.CourseCode = Courses.CourseCode
  AND  Students.ClassCode = 105 AND Grades.Grade >= 90
ORDER  BY Grades.Grade DESC;

-- ש12
SELECT COUNT(*) AS n FROM Students, Classes, Cities;
```

<div dir="rtl">

**ש1.** **17 שורות, לא 18. נעלמה לינא חמוד.**

ה‑`ClassCode` שלה הוא `NULL`, והתנאי `Students.ClassCode = Classes.ClassCode` לא מתקיים עבורה — `NULL = 101` אינו "אמת". חיבור רגיל (`INNER JOIN`) מחזיר **רק שורות שנמצאה להן התאמה**, ולא מודיע על מה שנשר. לינא נעלמה מהדוח **בשקט**.

<figure dir="ltr" class="dbtable">

| FirstName | LastName | ClassName |
|:---:|:---:|:---:|
| אדם | חלבי | י1 |
| נור | עזאם | י1 |
| יואב | כהן | י1 |
| מאיה | לוי | י2 |
| רוני | אברהם | י2 |
| סאלי | חסון | י2 |
| … | … | … |

</figure>

**ש2.** **גם כאן 17 — אבל נעלם מישהו אחר: ליאור לוי.** ל‑`CityCode` שלו אין ערך.

**זו הנקודה החשובה בשיעור:** אותו `JOIN`, אותה טבלה, אותו מספר שורות — ו**תלמיד אחר** נשר בכל פעם. מי שלא ספר את השורות, לא יידע שחסר מישהו. ספירת שורות היא לא פדנטיות; היא הבדיקה.

<figure dir="ltr" class="dbtable">

| FirstName | CityName |
|:---:|:---:|
| אדם | ירכא |
| נור | ירכא |
| יואב | כרמיאל |
| מאיה | חיפה |
| רוני | עכו |
| סאלי | עכו |
| … | … |

</figure>

**ש3.** **5 שורות.** שלוש טבלאות — **שני** תנאי חיבור. הכלל: `N` טבלאות דורשות **`N-1`** תנאי חיבור לפחות.

שימו לב ש"מתמטיקה 5 יח"ל" מופיעה פעמיים — מחצית 1 ומחצית 2. זה לא כפילות, זה הנתון.

<figure dir="ltr" class="dbtable">

| FirstName | CourseName | Term | Grade |
|:---:|:---:|:---:|:---:|
| דניאל | סדנת פרויקטים | 1 | 98 |
| דניאל | מבוא לבסיסי נתונים | 1 | 94 |
| דניאל | מתמטיקה 5 יח"ל | 2 | 92 |
| דניאל | מתמטיקה 5 יח"ל | 1 | 89 |
| דניאל | אנגלית 4 יח"ל | 1 | 87 |

</figure>

**ש4.** **6 שורות מתוך 7.** "סדנת פרויקטים" נעלמה — `TeacherCode` שלה `NULL`, כי טרם נקבע לה מורה.

<figure dir="ltr" class="dbtable">

| CourseName | FirstName | LastName |
|:---:|:---:|:---:|
| מתמטיקה 5 יח"ל | נביל | סרחאן |
| אנגלית 4 יח"ל | רונית | בר-לב |
| מבוא לבסיסי נתונים | חוסאם | זיאד |
| היסטוריה | אורלי | שמש |
| חינוך גופני | פאדי | חדאד |
| מתמטיקה 3 יח"ל | גלית | מזרחי |

</figure>

**ש5.** כאן כל 5 הכיתות חזרו — לכולן יש מחנך/ת.

<figure dir="ltr" class="dbtable">

| ClassName | Grade | Homeroom |
|:---:|:---:|:---:|
| י1 | 10 | נביל סרחאן |
| י2 | 10 | רונית בר-לב |
| יא1 | 11 | חוסאם זיאד |
| יא2 | 11 | גלית מזרחי |
| יב1 | 12 | אורלי שמש |

</figure>

**ש6.** **90 שורות** = **18 × 5**.

מה שחסר הוא **תנאי החיבור** — ה‑`WHERE Students.ClassCode = Classes.ClassCode`. בלעדיו בסיס הנתונים עושה בדיוק מה שביקשתם: מצמיד **כל** תלמיד ל**כל** כיתה. אדם מופיע עם י1, עם י2, עם יא1, עם יא2 ועם יב1 — חמש שורות, ארבע מהן שקר.

זה נקרא **תוצר קרטזי** (Cartesian Product), והוא לא שגיאה — אין הודעה, רק תוצאה גדולה ושגויה. הסימן המזהה: **מספר השורות הוא בדיוק מכפלה של גדלי הטבלאות.**

<figure dir="ltr" class="dbtable">

| CartesianRows |
|:---:|
| 90 |

</figure>

**ש7.** **18 שורות — לינא חזרה**, עם `NULL` בשם הכיתה.

`LEFT JOIN` אומר: "החזר את **כל** השורות מהטבלה **השמאלית** (`Students`), וכשנמצאה התאמה בימנית — צרף אותה; כשלא — שים `NULL`." ההבדל בין 17 ל‑18 הוא כל ההבדל בין "דוח כיתות" ל"דוח כל התלמידים", והוא בחירה שלכם, לא של בסיס הנתונים.

<figure dir="ltr" class="dbtable">

| FirstName | ClassName |
|:---:|:---:|
| לינא | NULL |
| אדם | י1 |
| נור | י1 |
| יואב | י1 |
| נועם | י1 |
| מאיה | י2 |
| … | … |
| ראניה | יב1 |

</figure>

**ש8.** **סמיר אבו-ראס** — מורה לביולוגיה, ובית הספר לא פתח מקצוע ביולוגיה.

**התרגיל הזה הוא התבנית החשובה ביותר בשיעור:** `LEFT JOIN` ואחר כך `WHERE <עמודה מהימנית> IS NULL` = **"מי מהשמאליים לא מצא אף התאמה"**. ה‑`LEFT JOIN` מביא את כולם, וה‑`IS NULL` מסנן ומשאיר **רק** את מי שלא נמצאה לו התאמה.

<figure dir="ltr" class="dbtable">

| FirstName | LastName | Subject |
|:---:|:---:|:---:|
| סמיר | אבו-ראס | ביולוגיה |

</figure>

**ש9.** **3 זוגות** — וזה בדיוק מה שמצפים מ‑3 תלמידים: כל אחד עם כל אחד, פעם אחת.

שני התנאים עושים שני דברים שונים, וצריך את שניהם:

| התנאי | מה הוא מונע |
|--------|--------------|
| `a.StudentId <> b.StudentId` | זיווג תלמיד **עם עצמו** (עומר-עומר) |
| `a.StudentId < b.StudentId` | גם את זה, **וגם** את הכפילות ההפוכה (עומר-שירה **וגם** שירה-עומר) |

לכן כותבים `<` ולא `<>`: הוא גם מסיר את העצמי וגם קובע סדר, וכך כל זוג מופיע פעם אחת. עם `<>` היינו מקבלים 6 שורות — כל זוג פעמיים.

<figure dir="ltr" class="dbtable">

| Student1 | Student2 | ClassCode |
|:---:|:---:|:---:|
| עומר | כרים | 103 |
| עומר | שירה | 103 |
| שירה | כרים | 103 |

</figure>

**ש10.** **3 מורים** מרוויחים פחות מחוסאם: רונית בר-לב, פאדי חדאד וסמיר אבו-ראס.

זה `Nonequijoin` — תנאי החיבור הוא `>` ולא `=`. אין כאן מפתח זר ואין קשר בין השורות; מה שמחבר אותן הוא **השוואה**. הכינויים `t1` ו‑`t2` הם חובה: בלעדיהם אין דרך לומר "השכר של זה גדול מהשכר של ההוא", כי שתי הטבלאות הן אותה טבלה.

<figure dir="ltr" class="dbtable">

| Earns_More | Than |
|:---:|:---:|
| זיאד | בר-לב |
| זיאד | חדאד |
| זיאד | אבו-ראס |

</figure>

**ש11.** **9 שורות.** `JOIN` של שלוש טבלאות + `WHERE` על שתיהן + `ORDER BY` — שאילתה בגודל אמיתי. ראניה עבאס לוקחת 5 מתוך 9.

<figure dir="ltr" class="dbtable">

| FirstName | CourseName | Grade |
|:---:|:---:|:---:|
| ראניה | מתמטיקה 5 יח"ל | 100 |
| ראניה | מבוא לבסיסי נתונים | 99 |
| דניאל | סדנת פרויקטים | 98 |
| ראניה | מתמטיקה 5 יח"ל | 98 |
| ראניה | סדנת פרויקטים | 95 |
| דניאל | מבוא לבסיסי נתונים | 94 |
| ראניה | אנגלית 4 יח"ל | 93 |
| דניאל | מתמטיקה 5 יח"ל | 92 |
| הדיל | סדנת פרויקטים | 90 |

</figure>

**ש12.** **540 שורות** = **18 × 5 × 6**. התוצר הקרטזי **מכפיל**, הוא לא מחבר.

ועכשיו החשבון המפחיד: עם 10,000 תלמידים, 400 כיתות ו‑250 ערים זה **מיליארד שורות** — בסיס הנתונים ינסה לבנות אותן, השרת ייתקע, וכל מי שעובד עליו באותו רגע ירגיש. זו הסיבה שבבחינה **מורידים נקודות** על `JOIN` בלי תנאי חיבור, וזו גם הסיבה שבעבודה אמיתית בודקים את מספר השורות **לפני** שמריצים על נתוני הייצור.

<figure dir="ltr" class="dbtable">

| n |
|:---:|
| 540 |

</figure>

</div>
<!-- classroom:end -->
