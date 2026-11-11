<div dir="rtl">

# מודול 22 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 כל הפלטים אמיתיים, מהרצה על בסיס הנתונים המוכן. תא ריק בפלט = NULL.

---

## ✅ תרגיל 1 — CROSS JOIN

</div>

```sql
-- a   4 x 5 = 20
SELECT COUNT(*) FROM species CROSS JOIN vaccine_type;

-- b   2 Haifa volunteers x 4 species = 8
SELECT p.first_name AS volunteer, s.name AS species
FROM   person p
CROSS  JOIN species s
WHERE  p.role = 'volunteer' AND p.city = 'Haifa'
ORDER  BY p.first_name, s.name;
```

```text
volunteer  species
---------  -------
Noa        Cat
Noa        Dog
Noa        Parrot
Noa        Rabbit
Ruti       Cat
Ruti       Dog
Ruti       Parrot
Ruti       Rabbit
```

```sql
-- c   LEFT JOIN -- every species, even without vaccines
SELECT s.name AS species, vt.name AS vaccine
FROM   species s
LEFT   JOIN vaccine_type vt ON vt.species_id = s.species_id
ORDER  BY s.name, vt.name;
```

```text
species  vaccine
-------  -----------
Cat      FVRCP
Cat      Rabies
Dog      DHPP
Dog      Rabies
Parrot                    <- no vaccine defined for parrots
Rabbit   Myxomatosis
```

<div dir="rtl">

---

## ✅ תרגיל 2 — NATURAL ו‑USING

**א.** `adoption NATURAL JOIN animal` ⟵ **9**, `intake NATURAL JOIN animal` ⟵ **21**. שתיהן הגיוניות — כי העמודה המשותפת **היחידה** היא `animal_id`. עבד, **במקרה**.

**ב.** `animal NATURAL JOIN species` ⟵ **0**. יש שתי עמודות משותפות: `species_id` **וגם `name`**. החיבור דורש ש‑`animal.name = species.name` — "Luna" = "Dog"? אף פעם.

</div>

```sql
-- c   USING names only the column we want
SELECT COUNT(*) FROM animal a JOIN species s USING (species_id);    -- 20

-- d
SELECT a.name, ad.adoption_date
FROM   animal a
JOIN   adoption ad USING (animal_id)
WHERE  ad.fee_paid >= 400;
```

```text
name     adoption_date
-------  -------------
Luna     2025-07-01
Charlie  2024-12-01
```

<div dir="rtl">

---

## ✅ תרגיל 3 — לחזות, ואז לספור

| השאילתה | התוצאה |
|----------|---------|
| `JOIN` | **9** — אימוצים שיש להם חיה (כולם) |
| `LEFT JOIN` | **21** |
| `RIGHT JOIN` | **9** |
| `FULL JOIN` | **21** |

**א.** 21 = 8 חיות **שאומצו** (9 אימוצים, כי לונה פעמיים) + 12 חיות **שלא אומצו** (שורה אחת עם NULL לכל אחת). לונה תורמת **שתי** שורות. `LEFT JOIN` לא מבטיח שורה אחת לכל חיה — הוא מבטיח **לפחות** אחת.

**ב.** `RIGHT` = `JOIN` כי **אין אימוץ בלי חיה** — לכל שורה ב‑`adoption` יש התאמה (המפתח הזר `NOT NULL`). לכן גם `FULL` = `LEFT`: אין "רק בצד ימין". **המספרים מספרים על האילוצים.**

---

## ✅ תרגיל 4 — מה חסר?

</div>

```sql
-- a
SELECT a.name, vt.name AS missing
FROM   animal a
JOIN   vaccine_type vt ON vt.species_id = a.species_id
LEFT   JOIN vaccination v ON  v.animal_id       = a.animal_id
                          AND v.vaccine_type_id = vt.vaccine_type_id
WHERE  v.vaccination_id IS NULL
ORDER  BY a.name, vt.name;
```

```text
name   missing
-----  -------
Bella  DHPP
Daisy  DHPP
Felix  FVRCP
Lily   FVRCP
Lily   Rabies
Mitzi  FVRCP
Nala   FVRCP
Nala   Rabies
Zoe    DHPP
```

<div dir="rtl">

**ב.** Bella ו‑Zoe **אומצו**, ו‑Daisy **מתה**. החיסון שלהן כבר לא באחריות המקלט — אז זה לא "חסר" במובן שרותי צריכה. **שאילתה נכונה טכנית יכולה להיות לא נכונה עסקית.** מוסיפים:

</div>

```sql
  AND  a.status NOT IN ('adopted', 'deceased')
-- -> Felix, Lily x2, Mitzi, Nala x2  (6 rows)
```

```sql
-- c
SELECT DISTINCT p.first_name, s.name AS species
FROM   adoption ad
JOIN   person  p ON p.person_id  = ad.adopter_id
JOIN   animal  a ON a.animal_id  = ad.animal_id
JOIN   species s ON s.species_id = a.species_id
ORDER  BY p.first_name;
```

```text
first_name  species
----------  -------
Dana        Dog          <- Dana adopted 2 dogs: DISTINCT shows "Dog" once
Eitan       Dog
Lior        Dog
Lior        Parrot       <- Lior: two species
Omer        Dog
Shira       Cat
Shira       Rabbit       <- Shira: two species
Yossi       Cat
```

<div dir="rtl">

---

## ✅ תרגיל 5 — שרשרת JOIN‑ים

</div>

```sql
-- a   15 rows: 12 people, but Dana, Lior and Shira adopted twice
SELECT p.first_name, p.role, a.name AS adopted
FROM   person p
LEFT   JOIN adoption ad ON ad.adopter_id = p.person_id
LEFT   JOIN animal   a  ON a.animal_id   = ad.animal_id
ORDER  BY p.person_id;
```

```text
first_name  role       adopted
----------  ---------  -------
Ruti        volunteer
Noa         volunteer
Amir        volunteer
Dr. Ron     vet
Dr. Maya    vet
Dana        adopter    Luna
Dana        adopter    Charlie
Yossi       adopter    Simba
Lior        adopter    Bella
Lior        adopter    Kiwi
Shira       adopter    Tom
Shira       adopter    Thumper
Omer        adopter    Zoe
Tamar       volunteer
Eitan       adopter    Luna
```

<div dir="rtl">

**ב.** עם `JOIN animal` רגיל — **9** שורות. כל מי שלא אימץ (6 מתנדבים ווטרינרים) **נעלם**: אצלם `ad.animal_id` הוא NULL, ו‑`a.animal_id = NULL` לעולם אינו true. ה‑`JOIN` "שבר" את ה‑`LEFT` שלפניו.

</div>

```sql
-- c   WRONG: 11 rows -- the general expenses vanish at the species JOIN
SELECT e.description, a.name, s.name AS species
FROM   expense e
LEFT   JOIN animal  a ON a.animal_id  = e.animal_id
JOIN   species      s ON s.species_id = a.species_id;

-- c   RIGHT: 22 rows
SELECT e.description, a.name, s.name AS species
FROM   expense e
LEFT   JOIN animal  a ON a.animal_id  = e.animal_id
LEFT   JOIN species s ON s.species_id = a.species_id;
```

```sql
-- d   21 rows
SELECT a.name, s.name AS species, p.first_name AS brought_by, p.city
FROM   intake  i
JOIN   animal  a ON a.animal_id  = i.animal_id      -- JOIN: every intake HAS an animal (NOT NULL)
JOIN   species s ON s.species_id = a.species_id     -- JOIN: every animal HAS a species (NOT NULL)
LEFT   JOIN person p ON p.person_id = i.brought_by  -- LEFT: transfers have no person
ORDER  BY i.intake_id;
```

```text
name   species  brought_by  city
-----  -------  ----------  ----------
Luna   Dog      Noa         Haifa
Simba  Cat      Yossi       Tel Aviv
Rocky  Dog      Amir        Kiryat Ata
Mitzi  Cat      Noa         Haifa
...
```

<div dir="rtl">

> 💡 **כאן ה‑`JOIN` ל‑`species` בא *לפני* ה‑`LEFT` ולא תלוי בו** — אז אין שבירה. מה שקובע הוא **על מה** תנאי ה‑`ON` נשען: `s` נשען על `a`, ו‑`a` מגיע מ‑`JOIN` רגיל.

---

## ✅ תרגיל 6 — FULL OUTER JOIN

</div>

```sql
-- a   21 rows: 11 general expenses + 10 animals without expenses
SELECT a.name AS animal, e.expense_id, e.description
FROM   animal a
FULL   OUTER JOIN expense e ON e.animal_id = a.animal_id
WHERE  a.animal_id IS NULL OR e.expense_id IS NULL;

-- b
SELECT COALESCE(j.volunteer, f.volunteer) AS volunteer,
       CASE WHEN f.volunteer IS NULL THEN 'january only'
            WHEN j.volunteer IS NULL THEN 'february only'
            ELSE 'both' END AS status
FROM   shift_jan j
FULL   OUTER JOIN shift_feb f ON f.volunteer = j.volunteer
ORDER  BY volunteer;
```

```text
volunteer  status
---------  -------------
Amir       both
Noa        both
Ruti       january only
Tamar      february only
```

<div dir="rtl">

> 🔑 **`COALESCE(j.volunteer, f.volunteer)`** — כי בשורה של Ruti, `f.volunteer` הוא NULL, ובשורה של Tamar — `j.volunteer`. השם נמצא תמיד **באחד** מהצדדים. זה הדפוס הקבוע של `FULL JOIN`: `COALESCE` על המפתח, `CASE` על המקור.

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
SELECT Customers.CustomerName FROM Customers LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID WHERE Orders.OrderID IS NULL;
```

**17** רשומות. השורה הראשונה: `Alfreds Futterkiste`


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
SELECT Students.FirstName, Classes.ClassName
FROM   Students INNER JOIN Classes ON Students.ClassCode = Classes.ClassCode;

-- ש2
SELECT Students.FirstName, Classes.ClassName
FROM   Students JOIN Classes USING (ClassCode);

-- ש3
SELECT * FROM Grades NATURAL JOIN Classes;                    -- 0 שורות (!)
SELECT COUNT(*) AS n FROM Students NATURAL JOIN Classes;      -- 17

-- ש4
SELECT COUNT(*) AS n FROM Classes CROSS JOIN Cities;

-- ש5
SELECT Courses.CourseName, Teachers.LastName
FROM   Courses INNER JOIN Teachers ON Courses.TeacherCode = Teachers.TeacherCode;
SELECT Courses.CourseName, Teachers.LastName
FROM   Courses LEFT  JOIN Teachers ON Courses.TeacherCode = Teachers.TeacherCode;

-- ש6  שתי הדרכים לאותה תשובה
SELECT Courses.CourseName, Teachers.LastName
FROM   Courses RIGHT JOIN Teachers ON Courses.TeacherCode = Teachers.TeacherCode;
SELECT Courses.CourseName, Teachers.LastName
FROM   Teachers LEFT JOIN Courses  ON Courses.TeacherCode = Teachers.TeacherCode;

-- ש7
SELECT Courses.CourseName, Teachers.LastName
FROM   Courses FULL OUTER JOIN Teachers ON Courses.TeacherCode = Teachers.TeacherCode;

-- ש8
SELECT Students.FirstName
FROM   Students LEFT JOIN Absences ON Absences.StudentId = Students.StudentId
WHERE  Absences.AbsenceId IS NULL;

-- ש9
SELECT Students.FirstName
FROM   Students LEFT JOIN Grades ON Grades.StudentId = Students.StudentId
WHERE  Grades.StudentId IS NULL;

-- ש10
SELECT Students.FirstName, Courses.CourseName, Grades.Grade
FROM   Grades
JOIN   Students ON Students.StudentId  = Grades.StudentId
JOIN   Courses  ON Courses.CourseCode  = Grades.CourseCode
WHERE  Grades.Grade IS NULL;

-- ש11  התיקון: התנאי עובר מ-WHERE ל-ON
SELECT Students.FirstName, Absences.AbsenceDate
FROM   Students LEFT JOIN Absences
       ON Absences.StudentId = Students.StudentId AND Absences.Excused = 0
ORDER  BY Students.StudentId;
```

<div dir="rtl">

**ש1.** 17 שורות — **בדיוק** כמו עם פסיק ו‑`WHERE` בשיעור 21. אותה תוצאה, אותה תוכנית ביצוע; רק התחביר שונה.

| התחביר | היתרון |
|---------|---------|
| `FROM A, B WHERE A.k = B.k` | קצר · **זה מה שמופיע בבחינה (שאלון 735911)** |
| `FROM A JOIN B ON A.k = B.k` | תנאי החיבור **מופרד** מתנאי הסינון — קשה יותר "לשכוח" אותו, ובלעדיו תקבלו שגיאה ולא תוצר קרטזי |

<figure dir="ltr" class="dbtable">

| FirstName | ClassName |
|:---:|:---:|
| אדם | י1 |
| נור | י1 |
| יואב | י1 |
| מאיה | י2 |
| רוני | י2 |

</figure>

**ש2.** `USING` אפשרי רק כששמות העמודות **זהים בשתי הטבלאות** — כאן `ClassCode`. החיסרון: הוא **תלוי בשמות**. אם מישהו ישנה את העמודה ב‑`Classes` ל‑`Code`, השאילתה תישבר; ואם יתווסף שם זהה **נוסף** לשתי הטבלאות, היא תמשיך לרוץ ותחבר לפי **שתי** העמודות — ותחזיר תוצאה אחרת בשקט. התוצאה כאן זהה לש1.

**ש3.** **0 שורות.**

`NATURAL JOIN` לא שואל אותך על מה לחבר — הוא מחבר **לפי כל העמודות ששמן זהה בשתי הטבלאות**. ב‑`Grades` יש `Grade` (ציון), וב‑`Classes` יש `Grade` (**שכבה**: 10, 11, 12). אותו שם, שני דברים שונים לגמרי. SQL חיבר אותם:

</div>

```text
Grades.Grade = Classes.Grade
   ציון       =      שכבה
      88      =       10     ->  לא
      74      =       11     ->  לא
      ...     כל 60 הציונים מול 10/11/12  ->  אף התאמה
```

<div dir="rtl">

אין ציון שערכו 10, 11 או 12, ולכן התוצאה ריקה. **ואין שגיאה.** שאילתה שמחזירה אפס שורות נראית כמו "אין נתונים מתאימים", וכאן היא בכלל לא שאלה את השאלה שהתכוונו אליה.

**ולמה `Students NATURAL JOIN Classes` כן עובד (17 שורות)?** כי שם העמודה המשותפת **היחידה** היא `ClassCode` — וזה במקרה בדיוק מה שרצינו. "במקרה" היא המילה החשובה: ברגע שמישהו יוסיף ל‑`Students` עמודה `RoomNumber` או `Grade`, אותה שאילתה תתחיל לחבר לפי שתי עמודות ותחזיר תוצאה אחרת — בלי שאף אחד נגע בה.

> **המסקנה:** `NATURAL JOIN` חוסך הקלדה ומוסר את השליטה לשמות העמודות. **כתבו `ON` במפורש.** תמיד.

**ש4.** **30 שורות** = 5 × 6. `CROSS JOIN` הוא **בדיוק** מה שפסיק בלי `WHERE` עושה — אותו תוצר קרטזי, אותו מספר שורות.

ההבדל הוא בכוונה, לא בתוצאה: `CROSS JOIN` **מכריז** "התוצר הקרטזי הוא מה שאני רוצה", ולכן מי שקורא את הקוד יודע שזה לא טעות. פסיק בלי `WHERE` נראה כמו `JOIN` ששכחו בו את התנאי — וב‑99% מהמקרים זה בדיוק מה שהוא.

**ש5א.** **6 שורות.** **ש5ב.** **7 שורות** — נוספה `סדנת פרויקטים`, ובעמודת שם המורה יש **`NULL`**.

ה‑`NULL` הזה לא קיים באף טבלה: הוא **הומצא על ידי ה‑`JOIN`** כדי למלא את השורה הימנית שלא נמצאה. זה הדבר שמבדיל `OUTER JOIN` מ‑`INNER JOIN`.

<figure dir="ltr" class="dbtable">

| CourseName | LastName (INNER) | LastName (LEFT) |
|:---:|:---:|:---:|
| מתמטיקה 5 יח"ל | סרחאן | סרחאן |
| אנגלית 4 יח"ל | בר-לב | בר-לב |
| מבוא לבסיסי נתונים | זיאד | זיאד |
| היסטוריה | שמש | שמש |
| חינוך גופני | חדאד | חדאד |
| מתמטיקה 3 יח"ל | מזרחי | מזרחי |
| **סדנת פרויקטים** | *(לא הופיעה)* | **NULL** |

</figure>

**ש6.** **סמיר אבו-ראס.** שתי השאילתות מחזירות 7 שורות זהות.

`RIGHT JOIN` = "כל השורות מהטבלה הימנית". `LEFT JOIN` = "כל השורות מהשמאלית". לכן:

</div>

```text
Courses  RIGHT JOIN  Teachers     ==     Teachers  LEFT JOIN  Courses
```

<div dir="rtl">

הם **אותו דבר** עם הטבלאות בסדר הפוך. לכן `RIGHT JOIN` הוא נוחות ולא יכולת: כל `RIGHT JOIN` נכתב כ‑`LEFT JOIN`, וזו הסיבה שהרבה צוותים אוסרים אותו — קל יותר לקרוא קוד שבו "הטבלה החשובה תמיד שמאלה".

<figure dir="ltr" class="dbtable">

| CourseName | LastName |
|:---:|:---:|
| מתמטיקה 5 יח"ל | סרחאן |
| אנגלית 4 יח"ל | בר-לב |
| מבוא לבסיסי נתונים | זיאד |
| היסטוריה | שמש |
| חינוך גופני | חדאד |
| מתמטיקה 3 יח"ל | מזרחי |
| **NULL** | **אבו-ראס** |

</figure>

**ש7.** **8 שורות** = 6 מותאמות + 2 חריגות, אחת מכל צד:

| השורה | מאיפה היא |
|--------|-----------|
| `סדנת פרויקטים` · `NULL` | מקצוע **בלי מורה** — הצד השמאלי |
| `NULL` · `אבו-ראס` | מורה **בלי מקצוע** — הצד הימני |

`FULL OUTER JOIN` = `LEFT` ∪ `RIGHT`. הוא השאילתה של "**תראה לי את כל אי‑ההתאמות בשני הכיוונים**", ובעבודה אמיתית זו בדיוק שאילתת הבדיקה שמריצים אחרי ייבוא נתונים.

<figure dir="ltr" class="dbtable">

| CourseName | LastName |
|:---:|:---:|
| מתמטיקה 5 יח"ל | סרחאן |
| אנגלית 4 יח"ל | בר-לב |
| מבוא לבסיסי נתונים | זיאד |
| היסטוריה | שמש |
| חינוך גופני | חדאד |
| מתמטיקה 3 יח"ל | מזרחי |
| סדנת פרויקטים | NULL |
| NULL | אבו-ראס |

</figure>

**ש8.** **9 תלמידים** לא נעדרו אף פעם: נור, רוני, עומר, שירה, ליאור, דניאל, הדיל, ראניה, נועם.

שימו לב שבדקנו `Absences.AbsenceId IS NULL` — **עמודה שהיא `NOT NULL` בטבלה**. זה לא מקרי: אם היא `NOT NULL` בהגדרה, `NULL` בה יכול להגיע **רק** מה‑`OUTER JOIN`, כלומר רק מ"לא נמצאה התאמה". לכן תמיד בוחרים לבדיקה הזאת את המפתח הראשי של הטבלה הימנית, ולא עמודה שעשויה להיות `NULL` בפני עצמה (כמו `Reason`).

<figure dir="ltr" class="dbtable">

| FirstName |
|:---:|
| נור |
| רוני |
| עומר |
| שירה |
| ליאור |
| דניאל |
| הדיל |
| ראניה |
| נועם |

</figure>

**ש9.** **לינא חמוד** — נרשמה ב‑10 בספטמבר, ואין לה עדיין אף ציון.

<figure dir="ltr" class="dbtable">

| FirstName |
|:---:|
| לינא |

</figure>

**ש10.** **2 שורות.** זה שונה מש9: כאן השורה **קיימת** ב‑`Grades`, אבל הציון בה `NULL`. "אין שורה" ו"יש שורה עם `NULL`" הם שני מצבים שונים לגמרי — הראשון נמצא ב‑`LEFT JOIN … IS NULL`, השני ב‑`WHERE … IS NULL` רגיל.

<figure dir="ltr" class="dbtable">

| FirstName | CourseName | Grade |
|:---:|:---:|:---:|
| מאיה | היסטוריה | NULL |
| כרים | אנגלית 4 יח"ל | NULL |

</figure>

**ש11.** הטעות: התנאי `Absences.Excused = 0` נמצא ב‑**`WHERE`** ולא ב‑**`ON`**.

הנה מה שקרה, בסדר הביצוע:

</div>

```text
1. LEFT JOIN   ->  25 שורות: כל התלמידים, כולל 9 עם NULL בהיעדרות
2. WHERE Excused = 0
                   עבור תלמיד בלי היעדרות, Excused הוא NULL
                   NULL = 0  ->  לא ידוע  ->  השורה נזרקת
3. התוצאה      ->  9 שורות בלבד
```

<div dir="rtl">

כלומר ה‑`WHERE` **ביטל את ה‑`LEFT`** והפך את השאילתה ל‑`INNER JOIN` רגיל. זו הטעות הנפוצה ביותר ב‑`OUTER JOIN`, והיא לא מתגלה בשגיאה — רק בשורות שנעלמו.

**התיקון — להעביר את התנאי ל‑`ON`:**

</div>

```sql
FROM  Students LEFT JOIN Absences
      ON Absences.StudentId = Students.StudentId AND Absences.Excused = 0
```

<div dir="rtl">

**22 שורות.** ההבדל העקרוני:

| המקום | מה הוא עושה |
|--------|--------------|
| `ON` | קובע **מה נחשב התאמה**. שורה שמאלית בלי התאמה עדיין חוזרת, עם `NULL` |
| `WHERE` | מסנן את **התוצאה**, אחרי שה‑`JOIN` נגמר — וזורק גם את שורות ה‑`NULL` |

**כלל אצבע:** ב‑`LEFT JOIN`, תנאי על הטבלה **הימנית** שייך ל‑`ON`. תנאי על הטבלה **השמאלית** שייך ל‑`WHERE`.

<figure dir="ltr" class="dbtable">

| FirstName | AbsenceDate |
|:---:|:---:|
| אדם | NULL |
| נור | NULL |
| יואב | NULL |
| מאיה | 2026-09-07 |
| רוני | NULL |
| סאלי | NULL |
| עומר | NULL |
| שירה | NULL |
| כרים | 2026-09-08 |
| כרים | 2026-09-09 |
| … | … |

</figure>

**ש12.** הטבלה המסכמת:

| החיבור | מה חוזר | מתי להשתמש |
|---------|----------|-------------|
| `INNER JOIN` | רק שורות שנמצאה להן התאמה בשני הצדדים | ברירת המחדל — "תראה לי את מה שמתאים" |
| `LEFT JOIN` | כל השמאליות + ההתאמות, `NULL` כשאין | "כל התלמידים, גם מי שאין לו…" · ולמצוא חסרים עם `IS NULL` |
| `RIGHT JOIN` | כל הימניות + ההתאמות | אף פעם לא **צריך** — הפכו את סדר הטבלאות ו‑`LEFT` |
| `FULL OUTER JOIN` | הכול משני הצדדים | בדיקת תקינות: "איפה הנתונים לא מסתדרים?" |
| `CROSS JOIN` | כל צירוף אפשרי (מכפלה) | נדיר ובכוונה — למשל לבנות לוח "כל כיתה × כל יום בשבוע" |

</div>
<!-- classroom:end -->
