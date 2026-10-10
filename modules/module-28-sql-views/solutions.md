<div dir="rtl">

# מודול 28 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 הפלטים אמיתיים, נכון ל‑`'2026-09-21'`.

---

## ✅ תרגיל 1 — View ראשון

</div>

```sql
-- a   9 rows
CREATE VIEW dog_view AS
SELECT animal_id, name, breed, weight_kg, status
FROM   animal
WHERE  species_id = 1;

-- b   Rex 38.7, Rocky 31.0, Shadow 25.1
SELECT name, weight_kg FROM dog_view WHERE status = 'available' ORDER BY weight_kg DESC;

-- c   Cat 4, Dog 3, Parrot 1, Rabbit 1
SELECT species, COUNT(*) FROM available_animal GROUP BY species;

-- d
UPDATE animal SET status = 'available' WHERE animal_id = 9;
SELECT COUNT(*) FROM available_animal;        -- 10 (was 9)
```

<div dir="rtl">

**ד.** **לא.** View לא שומר נתונים — השאילתה שבתוכו רצה מחדש בכל פעם. Nala מופיעה מיד.

---

## ✅ תרגיל 2 — View שמסתיר מורכבות

</div>

```sql
-- a
CREATE VIEW vaccination_detail AS
SELECT v.vaccination_id,
       a.name       AS animal,
       vt.name      AS vaccine,
       p.last_name  AS vet,
       v.given_date,
       v.cost,
       DATE(v.given_date, '+' || vt.interval_months || ' months') AS next_due
FROM   vaccination  v
JOIN   animal       a  ON a.animal_id        = v.animal_id
JOIN   vaccine_type vt ON vt.vaccine_type_id = v.vaccine_type_id
JOIN   person       p  ON p.person_id        = v.vet_id;

-- b
SELECT animal, vaccine, given_date, next_due
FROM   vaccination_detail WHERE animal = 'Rocky' ORDER BY given_date;
```

```text
animal  vaccine  given_date  next_due
------  -------  ----------  ----------
Rocky   Rabies   2023-05-25  2024-05-25
Rocky   DHPP     2023-05-25  2024-05-25
Rocky   Rabies   2024-05-28  2025-05-28
Rocky   Rabies   2025-05-30  2026-05-30
```

<div dir="rtl">

**ג.** **28 — בדיוק כמו `vaccination`.** כל ה‑`JOIN`‑ים הם "רבים ⟵ אחד" (לכל חיסון חיה אחת, סוג אחד, וטרינר אחד), אז הם לא מכפילים ולא מעלימים שורות. **זו הבדיקה לכל View עם JOIN:** מספר השורות שווה לטבלה המרכזית. אם היה יותר — יש כפל; פחות — `JOIN` העלים שורות (וצריך `LEFT`).

> 💡 **הערך של ה‑View:** מעכשיו, "מתי החיסון הבא של X?" היא שאילתה של שורה אחת. החישוב עם `interval_months` ו‑`DATE(… '+n months')` — כתוב במקום אחד.

---

## ✅ תרגיל 3 — View כדוח

</div>

```sql
-- a
CREATE VIEW yearly_finance AS
SELECT y AS year,
       SUM(income)                AS income,
       SUM(expense)               AS expense,
       SUM(income) - SUM(expense) AS balance
FROM  (SELECT STRFTIME('%Y', adoption_date) AS y, fee_paid AS income, 0 AS expense FROM adoption
       UNION ALL
       SELECT STRFTIME('%Y', expense_date), 0, amount FROM expense)
GROUP  BY y;

SELECT * FROM yearly_finance;
```

```text
year  income  expense  balance
----  ------  -------  --------
2023  500.0   0        500.0       <- no expenses were recorded in 2023
2024  1150.0  16920.0  -15770.0
2025  550.0   2880.0   -2330.0
```

```sql
-- b
CREATE VIEW in_shelter AS
SELECT a.animal_id, a.name, a.status,
       (SELECT MAX(i.intake_date) FROM intake i WHERE i.animal_id = a.animal_id) AS since
FROM   animal a
WHERE  a.status IN ('available', 'medical', 'quarantine');

SELECT name, status, since,
       CAST(JULIANDAY('2026-09-21') - JULIANDAY(since) AS INTEGER) AS days
FROM   in_shelter
ORDER  BY days DESC
LIMIT  4;
```

```text
name   status     since       days
-----  ---------  ----------  ----
Rocky  available  2023-05-20  1220
Mitzi  available  2023-06-11  1198
Coco   available  2023-09-30  1087
Max    medical    2023-11-05  1051
```

<div dir="rtl">

**ג.** כי `JOIN` של `animal` גם ל‑`expense` וגם ל‑`vaccination` **מכפיל**: לכל הוצאה × כל חיסון. ל‑Rocky — הוצאה אחת ו‑4 חיסונים ⟵ 4 שורות ⟵ ההוצאות היו **2,400** במקום 600 (מודול 23, תרגיל 6ג). תת‑שאילתה לכל טבלה — כל סכום מחושב בנפרד, נכון.

---

## ✅ תרגיל 4 — מצב נוכחי מתוך היסטוריה

</div>

```sql
-- a   8
SELECT COUNT(*) FROM current_home;

-- b   9
SELECT COUNT(*) FROM adoption;
```

<div dir="rtl">

**ב.** 9 אימוצים בהיסטוריה — אבל אחד מהם (Luna אצל Dana, 2023) **הסתיים** בהחזרה. 8 = מה שנכון **היום**. **הטבלה זוכרת הכול; ה‑View עונה על ההווה.**

</div>

```sql
-- c
CREATE VIEW latest_vaccine AS
SELECT animal, vaccine, MAX(given_date) AS last_given, MAX(next_due) AS next_due
FROM   vaccination_detail
GROUP  BY animal, vaccine;

SELECT COUNT(*) FROM latest_vaccine WHERE next_due < '2026-09-21';     -- 25
```

<div dir="rtl">

**25 — כמעט הכול.** כי ה‑View כולל **כל** חיה שחוסנה אי פעם: גם מאומצות (באחריות המשפחה), גם Daisy שמתה. **לצמצם:** להוסיף ל‑`vaccination_detail` את `a.status`, ולסנן `WHERE status IN ('available', 'medical', 'quarantine')`. **שאילתה נכונה טכנית ≠ תשובה עסקית** (מודול 22, תרגיל 4ב).

> 💡 **`GROUP BY animal`** — כאן בסדר כי אין שתי חיות באותו שם. בעבודה אמיתית — הוסיפו `animal_id` ל‑View וקבצו לפיו (מודול 24, סעיף 4).

---

## ✅ תרגיל 5 — אבטחה ועדכון

</div>

```sql
-- a
CREATE VIEW public_person AS
SELECT person_id, first_name, city, role FROM person;
```

<div dir="rtl">

**א.** מתנדבים צריכים לדעת מי עוד בצוות ומאיפה — לא את הטלפונים והשמות המלאים של המאמצים. נותנים הרשאה ל‑View בלבד (מודול 30), והמידע הרגיש פשוט **לא נגיש**. זה גם עניין של חוק הגנת הפרטיות.

**ב.** `cannot modify available_animal because it is a view`. מעדכנים את הטבלה: `UPDATE animal SET weight_kg = 30 WHERE animal_id = 3;`

**ג.**

| ה‑View | עדכון ב‑Oracle? | למה |
|--------|-----------------|-----|
| `dog_view` | ✅ | טבלה אחת, עמודות פשוטות |
| `available_animal` | חלקית | יש `JOIN` ועמודה מחושבת (`age`) — אפשר רק את עמודות `animal` שאינן מחושבות |
| `yearly_finance` | ❌ | `GROUP BY`, `SUM`, `UNION ALL` — שורה ב‑View היא הרבה שורות |
| `current_home` | כמעט לא | `JOIN` של שלוש טבלאות, ועמודת `adopter` מחושבת |

**ד.** `species_id` **בכלל לא ב‑`dog_view`** — אז ה‑`UPDATE` ייכשל עוד לפני `CHECK OPTION` ("invalid identifier"). אילו היה ב‑View: **עם** `CHECK OPTION` ⟵ `ORA-01402`, כי Rex היה יוצא מ‑`WHERE species_id = 1`. **בלי** ⟵ העדכון מצליח, ו‑Rex "נעלם" מ‑`dog_view` והופך לחתול של 38.7 ק"ג.

---

## ✅ תרגיל 6 — ניהול

</div>

```sql
-- a
SELECT name FROM sqlite_master WHERE type = 'view';

-- b   no -- a View holds no data
DROP VIEW animal_cost;
SELECT COUNT(*) FROM expense;     -- still 22

-- c   SQLite
DROP VIEW available_animal;
CREATE VIEW available_animal AS
SELECT ... WHERE a.status IN ('available', 'quarantine');

-- c   Oracle
CREATE OR REPLACE VIEW available_animal AS
SELECT ... WHERE a.status IN ('available', 'quarantine');
```

<div dir="rtl">

> 💡 **ההבדל חשוב ב‑Oracle:** `DROP` + `CREATE` מוחק גם את ה**הרשאות** שניתנו על ה‑View (מודול 30). `CREATE OR REPLACE` שומר אותן.

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[❓ לשאלות](questions.md)**

</div>

</div>

<!-- exam-style:start -->
<div dir="rtl">

---

## 🎓 תרגול בסגנון הבחינה: פתרונות

**ב1.** 1. **120** 2. `Q1` · `Q1.cheap`. ב‑SQL שומרים את Q1 כך:
```sql
CREATE VIEW Q1 AS SELECT MIN(Clubs.Price) AS cheap FROM Clubs;
SELECT Clubs.ClubName FROM Clubs, Q1 WHERE Clubs.Price = Q1.cheap;
```

<figure dir="ltr" class="dbtable">

| ClubName |
|:---:|
| יוגה |

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
CREATE VIEW StudentClass AS
SELECT s.StudentId, s.FirstName, s.LastName, c.ClassName, c.Grade AS GradeLevel
FROM   Students s LEFT JOIN Classes c ON s.ClassCode = c.ClassCode;

-- ש2
SELECT StudentClass.FirstName, StudentClass.LastName FROM StudentClass
WHERE  StudentClass.GradeLevel = 12 ORDER BY StudentClass.LastName;

-- ש3
CREATE VIEW ClassAverages AS
SELECT c.ClassName, COUNT(g.Grade) AS HowMany, ROUND(AVG(g.Grade),1) AS Avg1
FROM   Grades g, Students s, Classes c
WHERE  g.StudentId = s.StudentId AND s.ClassCode = c.ClassCode
GROUP  BY c.ClassName;

-- ש4
CREATE VIEW AtRiskStudents AS
SELECT sc.StudentId, sc.FirstName || ' ' || sc.LastName AS FullName, sc.ClassName,
       ROUND(AVG(g.Grade),1) AS Avg1
FROM   StudentClass sc, Grades g
WHERE  g.StudentId = sc.StudentId
GROUP  BY sc.StudentId, sc.FirstName, sc.LastName, sc.ClassName
HAVING AVG(g.Grade) < 65;

-- ש5
SELECT COUNT(*) AS Before1 FROM StudentClass;
INSERT INTO Students (StudentId, FirstName, LastName, ClassCode, Gender, EnrollDate)
VALUES (1019, 'תאיר', 'אביטן', 105, 'F', '2026-09-21');
SELECT COUNT(*) AS After1 FROM StudentClass;

-- ש6 / ש7  שתיהן נכשלות
UPDATE StudentClass  SET FirstName = 'תאיר-לי' WHERE StudentId = 1019;
UPDATE ClassAverages SET Avg1 = 100 WHERE ClassName = 'י1';

-- ש8
CREATE VIEW PublicTeachers AS
SELECT Teachers.TeacherCode, Teachers.FirstName, Teachers.LastName, Teachers.Subject
FROM   Teachers;
SELECT PublicTeachers.Salary FROM PublicTeachers;      -- ❌

-- ש9 / ש10
SELECT name, type FROM sqlite_master WHERE type = 'view' ORDER BY name;
SELECT sql FROM sqlite_master WHERE name = 'ClassAverages';

-- ש11
DROP VIEW AtRiskStudents;

-- ש12
CREATE TABLE AtRiskSnapshot AS SELECT * FROM ClassAverages;
UPDATE Grades SET Grade = 100 WHERE Grades.StudentId = 1012;
```

<div dir="rtl">

**ש1.** `LEFT JOIN` ולא `JOIN` — כדי שלינא, שאין לה כיתה, **תופיע** ב‑`View` עם `NULL` בשם הכיתה.

זו החלטה שמתקבלת **פעם אחת**, בהגדרת ה‑`View`, ואחר כך כל מי שישלוף ממנו יקבל אותה אוטומטית. זה הערך האמיתי של `View`: הוא **מקום לשים בו החלטה** כדי שלא יצטרכו לחזור עליה, ולא ישכחו אותה.

<figure dir="ltr" class="dbtable">

| StudentId | FirstName | LastName | ClassName | GradeLevel |
|:---:|:---:|:---:|:---:|:---:|
| 1001 | אדם | חלבי | י1 | 10 |
| 1002 | נור | עזאם | י1 | 10 |
| 1003 | יואב | כהן | י1 | 10 |
| 1004 | מאיה | לוי | י2 | 10 |
| 1005 | רוני | אברהם | י2 | 10 |

</figure>

**ש2.** **4 תלמידים.** ושימו לב מה קרה לשאילתה: היא נראית כמו `SELECT` מטבלה פשוטה, בלי `JOIN` ובלי כינויים. ה‑`JOIN` לא נעלם — הוא **הוסתר** בתוך ה‑`View`, ובסיס הנתונים מריץ אותו בכל שליפה.

<figure dir="ltr" class="dbtable">

| FirstName | LastName |
|:---:|:---:|
| איתי | גולן |
| הדיל | סעיד |
| ראניה | עבאס |
| דניאל | פרץ |

</figure>

**ש3.**

<figure dir="ltr" class="dbtable">

| ClassName | HowMany | Avg1 |
|:---:|:---:|:---:|
| יב1 | 17 | 85.2 |
| יא1 | 9 | 77.9 |
| י1 | 14 | 77.8 |
| יא2 | 11 | 72.8 |
| י2 | 7 | 68.9 |

</figure>

> 🔎 השוו ל‑ש5 של שיעור 24: שם `COUNT(*)` נתן ל‑יא1 **10** ול‑י2 **8**. כאן `COUNT(g.Grade)` נותן 9 ו‑7 — כי שני הציונים שהם `NULL` לא נספרים. אותה כיתה, שתי ספירות נכונות, שתי שאלות שונות.

**ש4.** **כן, מותר ומומלץ.** `View` הוא שאילתה, ושאילתה יכולה לשלוף מ‑`View` בדיוק כמו מטבלה. כאן `AtRiskStudents` בנוי על `StudentClass`, ולכן הוא **יורש** את ה‑`LEFT JOIN` ואת הכינוי `GradeLevel` בחינם.

זו הדרך לבנות שכבות: `View` בסיסי שמנקה ומחבר, ומעליו `View`‑ים שעונים על שאלות. כל תיקון בשכבה התחתונה מתקן אוטומטית את כל מה שמעליה.

<figure dir="ltr" class="dbtable">

| StudentId | FullName | ClassName | Avg1 |
|:---:|:---:|:---:|:---:|
| 1012 | ג'וד מנסור | יא2 | 44.8 |
| 1004 | מאיה לוי | י2 | 55 |
| 1009 | כרים חלבי | יא1 | 58.5 |
| 1006 | סאלי חסון | י2 | 62 |
| 1003 | יואב כהן | י1 | 63.3 |
| 1015 | איתי גולן | יב1 | 64 |

</figure>

**ש5.** **18 לפני, 19 אחרי.** תאיר מופיעה ב‑`View` מיד, עם `יב1` ו‑`12` — ולא עשינו ל‑`View` שום דבר.

<figure dir="ltr" class="dbtable">

| StudentId | FirstName | LastName | ClassName | GradeLevel |
|:---:|:---:|:---:|:---:|:---:|
| 1019 | תאיר | אביטן | יב1 | 12 |

</figure>

**למה?** כי ב‑`View` **אין נתונים**. הוא לא מחזיק עותק ולא "מתעדכן"; הוא שם של שאילתה. כל `SELECT … FROM StudentClass` מריץ את השאילתה **מחדש, עכשיו**, על הטבלאות כמו שהן באותו רגע. לכן אין מה לרענן ואין מה לסנכרן — ואין גם סיכון שה‑`View` "יתיישן".

**ש6.–ש7.** שתיהן נכשלות באותה הודעה:

</div>

```text
cannot modify StudentClass because it is a view
cannot modify ClassAverages because it is a view
```

<div dir="rtl">

**ב‑SQLite כל `View` הוא לקריאה בלבד.** (דרך לעקוף: `INSTEAD OF` trigger, מעבר להיקף השיעור.)

⚠️ **ובאורקל זה שונה**, וכאן הנושא נעשה מעניין. אורקל **כן** מאפשר `UPDATE` דרך `View` — אבל רק אם הוא **"פשוט"**: טבלה אחת, בלי `GROUP BY`, בלי `DISTINCT`, בלי פונקציות מצרפיות. כלומר באורקל:

| ה‑`View` | `UPDATE` דרכו |
|-----------|----------------|
| `PublicTeachers` (טבלה אחת, בלי קיבוץ) | **מותר** — העדכון עובר לטבלת `Teachers` |
| `StudentClass` (שתי טבלאות) | מותר **חלקית**, ורק על הטבלה "המשמרת מפתח" |
| `ClassAverages` (`GROUP BY` + `AVG`) | **אסור, בכל בסיס נתונים** |

**ולמה האחרון אסור בכל מקום? זו השאלה בש7.** נניח שהיה מותר: `SET Avg1 = 100` לכיתה י1. הממוצע 77.8 מחושב מ‑**14 ציונים** של 4 תלמידים. איזה ציון בטבלת `Grades` צריך להשתנות כדי שהממוצע יהיה 100? כולם? רק אחד, ל‑400? **אין תשובה** — ולכן אין פעולה. הפעולה ההפוכה לקיבוץ אינה מוגדרת: אפשר לדעת את הממוצע מהציונים, אבל אי אפשר לדעת את הציונים מהממוצע.

**ש8.** השליפה נכשלה: **`no such column: PublicTeachers.Salary`**.

<figure dir="ltr" class="dbtable">

| TeacherCode | FirstName | LastName | Subject |
|:---:|:---:|:---:|:---:|
| 1 | נביל | סרחאן | מתמטיקה |
| 2 | רונית | בר-לב | אנגלית |
| 3 | חוסאם | זיאד | מחשבים |

</figure>

וזה **השימוש השני בחשיבותו** ב‑`View`: **אבטחה**. במקום לתת למישהו הרשאה לטבלת `Teachers` כולה, נותנים לו הרשאה ל‑`PublicTeachers` בלבד. מבחינתו עמודת `Salary` **לא קיימת** — אין מה לנסות, אין מה לעקוף, ואין צורך לסמוך עליו שלא יסתכל.

> 🔮 שיעור 30 מחבר את שני החלקים: `GRANT SELECT ON PublicTeachers TO …` — הרשאה על ה‑`View`, לא על הטבלה.

**ש9.** ארבעה `View`‑ים:

<figure dir="ltr" class="dbtable">

| name | type |
|:---:|:---:|
| AtRiskStudents | view |
| ClassAverages | view |
| PublicTeachers | view |
| StudentClass | view |

</figure>

**ש10.** חזר **הקוד עצמו**, אות באות:

</div>

```sql
CREATE VIEW ClassAverages AS
SELECT c.ClassName, COUNT(g.Grade) AS HowMany, ROUND(AVG(g.Grade),1) AS Avg1
FROM Grades g, Students s, Classes c
WHERE g.StudentId = s.StudentId AND s.ClassCode = c.ClassCode
GROUP BY c.ClassName
```

<div dir="rtl">

**וזה כל מה ש‑`View` מאחסן: טקסט.** לא שורות, לא עותק, לא אינדקס — **משפט `SELECT`**. זו התשובה המלאה לשאלה "מה זה `View`", ומכאן נגזר כל השאר: למה הוא תמיד מעודכן (ש5), למה אי אפשר לעדכן דרכו (ש6), ולמה `DROP VIEW` לא מוחק נתונים (ש11).

**ש11.** `AtRiskStudents` נעלם מהרשימה — **ואף נתון לא נמחק.**

<figure dir="ltr" class="dbtable">

| name |
|:---:|
| ClassAverages |
| PublicTeachers |
| StudentClass |

</figure>

`DROP VIEW` מוחק **טקסט של שאילתה** מהקטלוג. הציונים, התלמידים והכיתות שלא נגעו בהם — כולם במקום. זה ההבדל מ‑`DROP TABLE`, שהוא בלתי הפיך ומוחק נתונים. `View` תמיד אפשר לבנות מחדש מהקוד; טבלה — לא.

**ש12.**

<figure dir="ltr" class="dbtable">

| Source | ClassName | Avg1 |
|:---:|:---:|:---:|
| VIEW (live) | יא2 | **92.9** |
| TABLE (frozen) | יא2 | **72.8** |

</figure>

**שני המספרים נכונים, והם עונים על שתי שאלות שונות:**

| | מה זה | מה הוא אומר |
|---|-------|--------------|
| **92.9** | ה‑`View` הריץ את השאילתה **עכשיו**, אחרי שכל הציונים של ג'וד הועלו ל‑100 | "מה הממוצע **כרגע**" |
| **72.8** | הטבלה נוצרה ב‑CTAS **לפני** העדכון, והיא עותק קפוא של אותו רגע | "מה היה הממוצע **כשצילמנו**" |

**מתי רוצים כל אחד:**

- **`View`** — לכל דוח שצריך להיות נכון: מצב נוכחי, רשימת תלמידים בסיכון, לוח מודעות. אין סיכון שהוא יתיישן, ואין עבודת תחזוקה.
- **טבלה (צילום מצב)** — כשדווקא **רוצים** שהנתון יקפא: ציוני סוף שנה, דוח שהוגש למשרד החינוך, השוואה "לפני ואחרי". דוח שהוגש אסור לו להשתנות למחרת רק כי מישהו תיקן ציון.

> 💡 ההבדל הזה הוא בדיוק מה שהיה חסר ב‑ש10 של שיעור 26: שם בנינו `AtRisk` כטבלה, ושאלנו "אבל מה בדיוק בנינו?". **התשובה: צילום מצב.** עכשיו יש לכם את שתי האפשרויות, והבחירה ביניהן היא שאלה אמיתית שנשאלת בכל פרויקט.

</div>
<!-- classroom:end -->
