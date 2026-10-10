<div dir="rtl">

# מודול 25 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 הפלטים אמיתיים, מהרצת כל התרגילים **ברצף** אחרי `shelter.sql` ו‑`PRAGMA foreign_keys = ON;`.

---

## ✅ תרגיל 1 — INSERT

</div>

```sql
-- a   gets person_id 13 (max + 1)
INSERT INTO person (first_name, last_name, role, city, phone, joined_date)
VALUES ('Nour', 'Haddad', 'volunteer', 'Yarka', '052-3434343', '2026-09-01');

SELECT person_id, first_name, city FROM person WHERE last_name = 'Haddad';
-- 13 | Nour | Yarka

-- b   one INSERT, two rows -> ids 21 and 22
INSERT INTO animal (name, species_id, sex, status)
VALUES ('Lucky', 1, 'M', 'quarantine'),
       ('Snow',  2, 'F', 'quarantine');

-- c
INSERT INTO intake (animal_id, intake_date, intake_type, brought_by, location)
VALUES (21, '2026-09-20', 'stray', 13, 'Yarka center');
-- intake_id 22 | animal 21 | stray | brought_by 13 | Yarka center

-- d
INSERT INTO intake (animal_id, intake_date, intake_type) VALUES (99, '2026-09-20', 'stray');
-- Error: FOREIGN KEY constraint failed
```

<div dir="rtl">

**ד.** אין חיה מספר 99 — המפתח הזר חוסם. **בלי `PRAGMA foreign_keys = ON`** השורה הייתה נכנסת: קליטה של חיה שלא קיימת. כל `JOIN` ל‑`animal` היה מעלים אותה בשקט, וכל `COUNT` על `intake` היה סופר אותה. **שורה יתומה.**

> 💡 **בסעיף ג' השתמשנו במזהים 21 ו‑13** שקיבלנו בסעיפים הקודמים. בקוד אמיתי לא "מנחשים" מזהה — שולפים אותו (`SELECT animal_id FROM animal WHERE name = 'Lucky'`), או משתמשים ב‑`last_insert_rowid()` (SQLite) / `RETURNING` (Oracle, PostgreSQL).

---

## ✅ תרגיל 2 — אילוצים

| ה‑INSERT | השגיאה | החוק העסקי |
|-----------|---------|-------------|
| `Ghost` בלי `status` | `NOT NULL constraint failed: animal.status` | לכל חיה **חייב** להיות מצב |
| `Twin` עם `sex = 'X'` | `CHECK constraint failed: sex IN ('M','F','U')` | מין — רק מהרשימה |
| `Dup` עם `animal_id = 1` | `UNIQUE constraint failed: animal.animal_id` | מזהה ייחודי (מפתח ראשי) |
| `Copy` עם השבב של Luna | `UNIQUE constraint failed: animal.chip_number` | שבב אחד = חיה אחת |

> 🔑 כל אחת מארבע השורות האלה הייתה **טעות הקלדה** בעולם האמיתי. האילוצים תפסו את כולן לפני שנכנסו. זו הסיבה שמגדירים אותם (מודול 27).

---

## ✅ תרגיל 3 — UPDATE

</div>

```sql
-- a
SELECT animal_id, name, status FROM animal WHERE name = 'Nala';     -- 9 | Nala | quarantine
UPDATE animal SET status = 'available' WHERE animal_id = 9;
SELECT changes();                                                    -- 1

-- b
UPDATE animal SET breed = 'Mixed' WHERE breed IS NULL AND species_id = 2;
SELECT changes();                                                    -- 4
```

<div dir="rtl">

**ב. 4, לא 3** — כי בתרגיל 1 הוספנו את **Snow**, חתולה בלי גזע. Mitzi, Nala, Lily **ו‑Snow**. זה בדיוק למה `changes()` חשוב: הוא מספר מה **באמת** קרה, לא מה שזכרתם.

</div>

```sql
-- c
UPDATE person SET city = 'Haifa' WHERE first_name = 'Lior';
SELECT changes();                                                    -- 1
```

<div dir="rtl">

**ג. 1** — למרות שהערך לא השתנה בפועל (Haifa ⟵ Haifa). `changes()` סופר **שורות שהתאימו ל‑`WHERE`**, לא שורות שהערך שלהן השתנה. **הלקח:** `changes() = 1` אומר "מצאתי שורה אחת", לא "שיניתי משהו".

</div>

```sql
-- d
UPDATE expense SET amount = amount * 1.18 WHERE category = 'utilities';
SELECT changes();                                                    -- 4
SELECT SUM(amount) FROM expense WHERE category = 'utilities';        -- 4448.6  (was 3770)

-- e
UPDATE animal
SET    status = 'adopted'
WHERE  animal_id IN (SELECT animal_id FROM adoption WHERE returned_date IS NULL)
  AND  status <> 'adopted';
SELECT changes();                                                    -- 0
```

<div dir="rtl">

**ה. 0** — כל החיות עם אימוץ פעיל כבר מסומנות `adopted`. **הנתונים עקביים.** `UPDATE` כזה הוא גם "תיקון" וגם "בדיקה": אם יום אחד יחזיר מספר גדול מ‑0 — מישהו רשם אימוץ ושכח לעדכן את החיה.

---

## ✅ תרגיל 4 — DELETE

</div>

```sql
-- a
DELETE FROM species WHERE species_id = 4;
-- Error: FOREIGN KEY constraint failed    (Coco and Kiwi are parrots)

-- b
DELETE FROM vaccine_type WHERE vaccine_type_id = 5;
-- Error: FOREIGN KEY constraint failed    (Thumper and Bunny got Myxomatosis)

-- c
CREATE TABLE expense_backup AS SELECT * FROM expense;               -- backup first!
DELETE FROM expense WHERE animal_id IS NULL AND expense_date < '2024-04-01';
SELECT changes();                                                    -- 5
```

<div dir="rtl">

**ג.** 5 הוצאות כלליות לפני אפריל: מזון (ינואר), חשמל (ינואר), חול לחתולים, חשמל (פברואר), מזון (מרץ).

**ד.** Daisy לא נמחקה — `status = 'deceased'`. כל ההיסטוריה שלה נשמרת: הקליטה, החיסון, ההוצאה על ביקור החירום. דוח של 2024 עדיין יכלול אותה. **מחיקה רכה** — סעיף 6.2.

---

## ✅ תרגיל 5 — DEFAULT ו‑upsert

</div>

```sql
-- a
INSERT INTO donation (donor_name, amount, donation_date, method) VALUES ('Carmel School', 1200, '2026-06-01', 'transfer');
INSERT INTO donation (donor_name, amount, method)                VALUES ('Anonymous',     250, 'bit');
INSERT INTO donation (donor_name, amount)                        VALUES ('Haifa Rotary',  5000);
SELECT * FROM donation;
```

```text
donation_id  donor_name     amount  donation_date  method
-----------  -------------  ------  -------------  --------
1            Carmel School  1200.0  2026-06-01     transfer
2            Anonymous      250.0   2026-09-21     bit
3            Haifa Rotary   5000.0  2026-09-21     cash
```

<div dir="rtl">

**ב.** `NOT NULL constraint failed: donation.donor_name` — `DEFAULT VALUES` נותן לכל עמודה את ברירת המחדל שלה, אבל ל‑`donor_name` ול‑`amount` **אין** ברירת מחדל, והן `NOT NULL`. אין ממה למלא.

</div>

```sql
-- c
INSERT INTO stock (item, qty) VALUES ('dog food sack', 8), ('flea collar', 20)
ON CONFLICT(item) DO UPDATE SET qty = qty + excluded.qty;
```

```text
item           qty
-------------  ---
dog food sack  20      <- 12 + 8
cat litter     5       <- untouched
flea collar    20      <- new
```

<div dir="rtl">

**ד.** `ON CONFLICT clause does not match any PRIMARY KEY or UNIQUE constraint`. **בלי אילוץ ייחודיות — אין "התנגשות"**, ולכן אין למה להגיב. בסיס הנתונים לא יכול לנחש ש‑`item` "אמור" להיות ייחודי — **רק אילוץ אומר לו את זה.**

---

## ✅ תרגיל 6 — INSERT … SELECT

</div>

```sql
-- a   2 rows: adoptions 1 and 2
CREATE TABLE adoption_archive AS SELECT * FROM adoption WHERE 0;
INSERT INTO adoption_archive SELECT * FROM adoption WHERE adoption_date LIKE '2023%';

-- b
CREATE TABLE vip_adopter (person_id INTEGER, full_name TEXT, adoptions INTEGER);

INSERT INTO vip_adopter
SELECT p.person_id, p.first_name || ' ' || p.last_name, COUNT(*)
FROM   adoption ad
JOIN   person p ON p.person_id = ad.adopter_id
GROUP  BY p.person_id
HAVING COUNT(*) > 1;

SELECT * FROM vip_adopter;
```

```text
person_id  full_name   adoptions
---------  ----------  ---------
6          Dana Cohen  2
8          Lior Bar    2
9          Shira Katz  2
```

```sql
-- c   SQLite: two INSERT ... SELECT
CREATE TABLE stray_log     (intake_id INTEGER, animal_id INTEGER, location TEXT);
CREATE TABLE surrender_log (intake_id INTEGER, animal_id INTEGER, reason   TEXT);

INSERT INTO stray_log     SELECT intake_id, animal_id, location FROM intake WHERE intake_type = 'stray';
INSERT INTO surrender_log SELECT intake_id, animal_id, reason   FROM intake WHERE intake_type = 'surrender';
-- 11 strays, 8 surrenders (the 2 transfers go nowhere)

-- Oracle: one pass
INSERT ALL
  WHEN intake_type = 'stray'     THEN INTO stray_log     VALUES (intake_id, animal_id, location)
  WHEN intake_type = 'surrender' THEN INTO surrender_log VALUES (intake_id, animal_id, reason)
SELECT intake_id, animal_id, intake_type, location, reason FROM intake;
```

<div dir="rtl">

> 🔑 **שימו לב: `vip_adopter` היא תמונת מצב.** אם Yossi יאמץ מחר חיה שנייה — הטבלה **לא** תתעדכן. זה ההבדל בין **טבלה** שנבנתה מ‑`SELECT` לבין **View** (מודול 28) — שאילתה שמורה שתמיד מחזירה את המצב העדכני.

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[❓ לשאלות](questions.md)**

</div>

</div>

<!-- exam-style:start -->
<div dir="rtl">

---

## 🎓 תרגול בסגנון הבחינה: פתרונות

**ב1.** ```sql
INSERT INTO Members (Id, FirstName, LastName, CityCode, Age, JoinYear)
VALUES (1013, "אור", "גבאי", 6, 15, 2025);
```

**ב2.** ```sql
UPDATE Clubs SET Price = Price + 20
WHERE Sport = "שחייה";
```
**2** רשומות (102 ו‑103). בבחינה כותבים `SET Clubs.Price = Clubs.Price + 20`.

**ב3.** **כל** 18 הרשומות יימחקו, והטבלה תישאר ריקה. לפני `DELETE` או `UPDATE` כדאי להריץ קודם `SELECT` עם אותו `WHERE`, כדי לראות מה ייפגע.

<figure dir="ltr" class="dbtable">

| rows_before |
|:---:|
| 18 |

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
INSERT INTO Students VALUES (1019, 'תאיר', 'אביטן', 102, 'F', '2011-02-28', 3, '2026-09-20', '050-1000019');
SELECT * FROM Students WHERE Students.StudentId = 1019;

-- ש2
INSERT INTO Students (StudentId, FirstName, LastName, Gender, EnrollDate)
VALUES (1020, 'סיוון', 'דהן', 'F', '2026-09-21');
SELECT * FROM Students WHERE Students.StudentId = 1020;

-- ש3
INSERT INTO Absences (AbsenceId, StudentId, AbsenceDate, Excused, Reason) VALUES
  (17, 1019, '2026-09-21', 0, NULL),
  (18, 1020, '2026-09-21', 1, 'מחלה');
SELECT COUNT(*) AS TotalAbsences FROM Absences;

-- ש4
UPDATE Students SET Phone = '050-9999999' WHERE Students.StudentId = 1002;

-- ש5
UPDATE Teachers SET Salary = ROUND(Salary * 1.03);

-- ש6
UPDATE Students SET ClassCode = 102 WHERE Students.ClassCode IS NULL;

-- ש7
DELETE FROM Absences WHERE Absences.Excused = 1 AND Absences.AbsenceDate < '2026-09-05';

-- ש8  השגוי, ואחריו הנכון
UPDATE Grades SET Grade = Grade + 5 WHERE Grades.Grade IS NULL;   -- לא משנה כלום
UPDATE Grades SET Grade = 5          WHERE Grades.Grade IS NULL;   -- או COALESCE(Grade,0) + 5

-- ש9  שלושתן נכשלות בכוונה

-- ש10
CREATE TABLE AtRisk (StudentId INTEGER PRIMARY KEY, FullName TEXT, Avg1 REAL);
INSERT INTO AtRisk (StudentId, FullName, Avg1)
SELECT s.StudentId, s.FirstName || ' ' || s.LastName, ROUND(AVG(g.Grade),1)
FROM   Grades g, Students s
WHERE  g.StudentId = s.StudentId
GROUP  BY s.StudentId, s.FirstName, s.LastName
HAVING AVG(g.Grade) < 65;
SELECT * FROM AtRisk ORDER BY Avg1;

-- ש11
CREATE TABLE Trips (
  TripId      INTEGER PRIMARY KEY,
  Destination TEXT    NOT NULL,
  TripDate    TEXT    NOT NULL DEFAULT '2027-05-01',
  Price       INTEGER NOT NULL DEFAULT 120
);
INSERT INTO Trips (TripId, Destination) VALUES (1, 'מצדה');
INSERT INTO Trips VALUES (2, 'הכנרת', '2027-03-15', 90);
SELECT * FROM Trips;

-- ש12
DELETE FROM AtRisk;
```

<div dir="rtl">

**ש1.** `INSERT` בלי רשימת עמודות = **כל** העמודות, **בסדר שבו הוגדרו בטבלה**. זה עובד, וזה שביר: אם מישהו יוסיף עמודה ל‑`Students`, השאילתה הזאת תישבר (או, גרוע מזה, תכניס ערכים לעמודות הלא נכונות).

<figure dir="ltr" class="dbtable">

| StudentId | FirstName | LastName | ClassCode | Gender | BirthDate | CityCode | EnrollDate | Phone |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1019 | תאיר | אביטן | 102 | F | 2011-02-28 | 3 | 2026-09-20 | 050-1000019 |

</figure>

**ש2.** בכל מה שלא מילאתם יש **`NULL`**.

<figure dir="ltr" class="dbtable">

| StudentId | FirstName | LastName | ClassCode | Gender | BirthDate | CityCode | EnrollDate | Phone |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1020 | סיוון | דהן | NULL | F | NULL | NULL | 2026-09-21 | NULL |

</figure>

ושימו לב מה זה אומר: הצלחנו להכניס תלמידה **בלי תאריך לידה, בלי עיר ובלי כיתה** — כי אף אחת מהעמודות האלה אינה `NOT NULL`. ה‑`INSERT` עבר בשקט, ומחר מישהו ישאל "למה הדוח מראה גיל ריק?". זו לא בעיית DML; זו **בעיית עיצוב** שמטפלים בה באילוצים (שיעור 27).

כתיבת רשימת עמודות מפורשת היא תמיד עדיפה: היא מתעדת מה מילאתם, והיא לא נשברת כשהטבלה משתנה.

**ש3.** **18 היעדרויות.** `INSERT` אחד עם כמה `VALUES` מופרדים בפסיק — גם יעיל יותר וגם אטומי (או שכולם נכנסו, או אף אחד).

**ש4.**

<figure dir="ltr" class="dbtable">

| StudentId | FirstName | Phone |
|:---:|:---:|:---:|
| 1002 | נור | 050-9999999 |

</figure>

**ש5.** `UPDATE` **בלי `WHERE`** — וכאן זו הכוונה: כל 7 המורים. `SET Salary = ROUND(Salary * 1.03)` קורא את הערך הקיים בכל שורה ומחשב ממנו.

<figure dir="ltr" class="dbtable">

| LastName | Salary (לפני) | Salary (אחרי) |
|:---:|:---:|:---:|
| סרחאן | 14500 | 14935 |
| בר-לב | 11200 | 11536 |
| זיאד | 12800 | 13184 |
| שמש | 15300 | 15759 |
| חדאד | 9800 | 10094 |
| מזרחי | 13100 | 13493 |
| אבו-ראס | 10400 | 10712 |

</figure>

**ש6.** **2 שורות** — לינא (1018) **וגם סיוון (1020)**, שיצרתם בש2.

זו נקודה ששווה לעצור עליה: ה‑`UPDATE` תפס תלמידה שלא חשבתם עליה, כי היא עמדה בתנאי. `WHERE … IS NULL` הוא תנאי על **מצב הנתונים כרגע**, ולא על רשימת שורות שבחרתם. לפני `UPDATE` רחב כדאי להריץ את אותו `WHERE` בתוך `SELECT` ולראות **את מי** זה הולך לתפוס.

<figure dir="ltr" class="dbtable">

| StudentId | FirstName | ClassCode |
|:---:|:---:|:---:|
| 1018 | לינא | 102 |
| 1020 | סיוון | 102 |

</figure>

**ש7.** נמחקו **3** היעדרויות, ונשארו **15** (מתוך 18). שלוש המאושרות שלפני ה‑5 בספטמבר: שתיים של יואב (2 ו‑3 בספטמבר) ואחת של איתי (4 בספטמבר).

**ש8.** העדכון **כן נגע ב‑2 שורות**, ולא שינה בהן כלום. הערך נשאר `NULL`.

הסיבה: `SET Grade = Grade + 5` מחשב לפי הערך **הקיים**, והערך הקיים הוא `NULL`. ו‑`NULL + 5` הוא `NULL`. בסיס הנתונים עשה בדיוק מה שביקשתם: לקח לא‑ידוע, הוסיף 5, וקיבל לא‑ידוע.

זו מלכודת מסוכנת במיוחד כי הדיווח **"2 rows affected"** נראה כמו הצלחה.

**התיקון** תלוי במה שהתכוונתם:

</div>

```sql
UPDATE Grades SET Grade = 5 WHERE Grades.Grade IS NULL;               -- "הציון שלהם הוא 5"
UPDATE Grades SET Grade = COALESCE(Grade, 0) + 5;                     -- "לכולם +5, וחסר נחשב 0"
```

<div dir="rtl">

<figure dir="ltr" class="dbtable">

| StudentId | CourseCode | Grade |
|:---:|:---:|:---:|
| 1004 | 14 | NULL |
| 1009 | 12 | NULL |

</figure>

**ש9.** שלוש שגיאות, שלושה אילוצים שונים:

</div>

```text
א   CHECK constraint failed: Gender IN ('M','F')
ב   FOREIGN KEY constraint failed
ג   UNIQUE constraint failed: Students.StudentId
```

<div dir="rtl">

| הסעיף | האילוץ | מה הוא מנע |
|--------|---------|-------------|
| **א** | `CHECK (Gender IN ('M','F'))` | `'X'` אינו ערך חוקי. האילוץ מגדיר **תחום** (domain) ושומר שלא ייכנס אליו ערך שלא תוכנן |
| **ב** | `FOREIGN KEY (CourseCode)` | אין מקצוע `99`. האילוץ מנע **שורה יתומה** — ציון שמצביע לשום מקום |
| **ג** | `PRIMARY KEY (StudentId)` | `1001` כבר קיים. מפתח ראשי הוא גם `UNIQUE`, ולכן אין שני תלמידים עם אותו מזהה |

**ושימו לב מה קרה בכל שלוש:** השורה **לא נכנסה**. זה בדיוק הערך של אילוצים — הם דוחים נתון שגוי **ברגע הכתיבה**, במקום לתת לו לשבת בטבלה ולהתגלות בדוח חצי שנה אחר כך. ⚠️ ב‑SQLite אילוצי מפתח זר נבדקים רק אם `PRAGMA foreign_keys = ON` — ב‑OneCompiler ייתכן שסעיף ב' **יעבור** ולא ייכשל. אם זה קרה לכם, זה שיעור בפני עצמו: אילוץ שלא נאכף הוא תיעוד, לא הגנה.

**ש10.** **6 תלמידים** בסיכון.

`INSERT INTO … SELECT` הוא הצורה שבה ממלאים טבלה **מתוך שאילתה** — בלי לכתוב `VALUES` אפילו פעם אחת. כאן הוא לקח `GROUP BY … HAVING` שלם והפך אותו ל‑6 שורות בטבלה חדשה. אין הגבלה על מורכבות ה‑`SELECT`: `JOIN`, `GROUP BY`, תת‑שאילתות — הכול מותר.

<figure dir="ltr" class="dbtable">

| StudentId | FullName | Avg1 |
|:---:|:---:|:---:|
| 1012 | ג'וד מנסור | 44.8 |
| 1004 | מאיה לוי | 55 |
| 1009 | כרים חלבי | 58.5 |
| 1006 | סאלי חסון | 62 |
| 1003 | יואב כהן | 63.3 |
| 1015 | איתי גולן | 64 |

</figure>

> ⚠️ **אבל מה בדיוק בנינו?** "תמונת מצב" מהרגע הזה. מחר ייכנסו ציונים חדשים, והטבלה `AtRisk` תישאר כפי שהיא — **נכונה לאתמול**. זה הבדל מהותי מ‑`View` (שיעור 28), שהוא שאילתה שמורה ומתעדכן תמיד. שתיהן שימושיות; צריך לדעת מה בחרתם.

**ש11.** `DEFAULT` נכנס לפעולה **רק** כשלא ציינתם את העמודה. טיול 1 קיבל `2027-05-01` ו‑`120` מברירת המחדל; טיול 2 קיבל את מה שנתנו לו.

<figure dir="ltr" class="dbtable">

| TripId | Destination | TripDate | Price |
|:---:|:---:|:---:|:---:|
| 1 | מצדה | 2027-05-01 | 120 |
| 2 | הכנרת | 2027-03-15 | 90 |

</figure>

> 💡 `DEFAULT` ו‑`NOT NULL` יחד הם צמד חזק: העמודה **חייבת** ערך, ואם לא נתנו — יש לה אחד הגיוני. כך לא נוצרות שורות חלקיות כמו של סיוון בש2.

**ש12.** **0 שורות נשארו.** כל 6 השורות נמחקו, בלי אישור ובלי אזהרה.

`DELETE FROM טבלה;` בלי `WHERE` הוא **הפקודה המסוכנת ביותר ב‑SQL**. בבית ספר אמיתי `DELETE FROM Students;` היה מוחק את כל התלמידים — ואיתם, דרך המפתחות הזרים, גם את הציונים וההיעדרויות שלהם (או, אם האילוצים מגנים, הפקודה הייתה נכשלת, וזו עוד נקודה לזכותם).

**שלושה דברים שהיו מצילים אותך:**

| מה | למה זה עובד |
|-----|--------------|
| **להריץ `SELECT` עם אותו `WHERE` קודם** | רואים **בדיוק** אילו שורות ייעלמו, לפני שהן נעלמות. הרגל של שתי שניות |
| **`BEGIN TRANSACTION` לפני** | אחרי המחיקה בודקים, ואם משהו לא בסדר — `ROLLBACK`, וכלום לא קרה (שיעור 32) |
| **גיבוי** | הדבר היחיד שעוזר **אחרי** ש‑`COMMIT` נעשה. למחיקה שאושרה אין "בטל" |

> 🔮 הסעיף הזה הוא ההקדמה לשיעור 32. `DELETE` בתוך טרנזקציה הוא החלטה הפיכה; `DELETE` עם `COMMIT` הוא עובדה.

</div>
<!-- classroom:end -->
