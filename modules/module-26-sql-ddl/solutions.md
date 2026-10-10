<div dir="rtl">

# מודול 26 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 הפלטים אמיתיים, מהרצה ברצף אחרי `shelter.sql` ו‑`PRAGMA foreign_keys = ON;`.

---

## ✅ תרגיל 1 — טיפוסים

| העמודה | SQLite | Oracle | למה |
|--------|--------|--------|-----|
| טלפון | `TEXT` | `VARCHAR2(15)` | לא מחשבים איתו; 0 מוביל ומקפים |
| משקל | `REAL` | `NUMBER(5,2)` | מספר עשרוני, עושים ממוצעים |
| מספר שבב | `TEXT` | `VARCHAR2(15)` | "מספר" שלא מחשבים איתו |
| תאריך חיסון | `TEXT` (`YYYY-MM-DD`) | `DATE` | הפרשים, מיון, "הבא בעוד 12 חודשים" |
| מעוקר | `INTEGER` (0/1) | `NUMBER(1)` | אמת/שקר |
| מחיר אימוץ | `REAL` | `NUMBER(7,2)` | כסף — עשרוני מדויק ב‑Oracle |
| מין | `TEXT` | `CHAR(1)` | קוד באורך קבוע |
| ת"ז | `TEXT` | `CHAR(9)` | 0 מוביל! `012345678` כמספר הוא `12345678` |

---

## ✅ תרגיל 2 — CREATE TABLE

</div>

```sql
-- a
CREATE TABLE walk (
  walk_id    INTEGER PRIMARY KEY,
  animal_id  INTEGER NOT NULL REFERENCES animal(animal_id),
  person_id  INTEGER NOT NULL REFERENCES person(person_id),
  walk_date  TEXT    NOT NULL,
  minutes    INTEGER NOT NULL DEFAULT 30,
  notes      TEXT
) STRICT;
```

```text
name   volunteer  walk_date   minutes  notes
-----  ---------  ----------  -------  ------------------
Rocky  Noa        2026-09-20  30
Rex    Amir       2026-09-20  45       pulls on the leash
```

<div dir="rtl">

**ב.** `minutes` = **30** — ברירת המחדל.

**ג.** `cannot store TEXT value in INTEGER column walk.minutes`. **בלי `STRICT`** — `'long'` היה נשמר כטקסט בעמודת מספר, ו‑`SUM(minutes)` היה מתעלם ממנו או מחזיר שטויות.

**ד.** `FOREIGN KEY constraint failed` — אין אדם 99.

---

## ✅ תרגיל 3 — מ‑ERD לטבלה

</div>

```text
   TREATMENT
   # treatment_id
   * treatment_date
   * kind
   o weight_kg
   * cost         (default 0)
   o notes
   relationships:  ANIMAL 1 ----< TREATMENT    (mandatory)
                   PERSON(vet) 1 ----< TREATMENT    (mandatory)
```

```sql
CREATE TABLE treatment (
  treatment_id   INTEGER PRIMARY KEY,
  animal_id      INTEGER NOT NULL REFERENCES animal(animal_id),
  vet_id         INTEGER NOT NULL REFERENCES person(person_id),
  treatment_date TEXT    NOT NULL,
  kind           TEXT    NOT NULL,
  weight_kg      REAL,
  cost           REAL    NOT NULL DEFAULT 0,
  notes          TEXT
) STRICT;

INSERT INTO treatment (animal_id, vet_id, treatment_date, kind, weight_kg, cost)
VALUES (8, 4, '2026-09-01', 'leg check-up', 12.6, 150);
INSERT INTO treatment (animal_id, vet_id, treatment_date, kind)
VALUES (9, 5, '2026-09-05', 'quarantine release exam');
INSERT INTO treatment (animal_id, vet_id, treatment_date, kind, cost, notes)
VALUES (3, 4, '2026-09-10', 'hip follow-up', 200, 'stable');

SELECT a.name, p.last_name AS vet, t.treatment_date, t.kind, t.cost
FROM   treatment t
JOIN   animal a ON a.animal_id = t.animal_id
JOIN   person p ON p.person_id = t.vet_id
ORDER  BY t.treatment_date;
```

```text
name   vet    treatment_date  kind                     cost
-----  -----  --------------  -----------------------  -----
Max    Levi   2026-09-01      leg check-up             150.0
Nala   Nahum  2026-09-05      quarantine release exam  0.0
Rocky  Levi   2026-09-10      hip follow-up            200.0
```

<div dir="rtl">

> 💡 **`vet_id` ולא `person_id`** — שם התפקיד (סעיף 5). ⚠️ שימו לב: `REFERENCES person` לא מבטיח שהאדם הוא **וטרינר** — רק שהוא קיים. כדי לאכוף "רק וטרינר" צריך טבלת טיפוס‑משנה נפרדת `vet`, או בדיקה בקוד. **עוד החלטת עיצוב ממודול 4 שיש לה מחיר ב‑SQL.**

---

## ✅ תרגיל 4 — ALTER TABLE

</div>

```sql
-- a   all 20 animals get 0
ALTER TABLE animal ADD COLUMN is_neutered INTEGER NOT NULL DEFAULT 0;

-- b
ALTER TABLE animal ADD COLUMN arrival_note TEXT NOT NULL;
-- Error: Cannot add a NOT NULL column with default value NULL
```

<div dir="rtl">

**ב.** בטבלה כבר יש 20 שורות. העמודה החדשה צריכה ערך בכל אחת — ולא נתתם. NULL אסור (`NOT NULL`), ואין ברירת מחדל. **עמודת חובה חדשה בטבלה קיימת ⟵ חייבת `DEFAULT`.**

</div>

```sql
-- c   Rex
UPDATE animal SET is_neutered = 1
WHERE  animal_id IN (SELECT animal_id FROM expense WHERE description = 'neutering surgery');

-- d
ALTER TABLE walk RENAME COLUMN notes TO remarks;
ALTER TABLE walk DROP COLUMN remarks;
```

<div dir="rtl">

---

## ✅ תרגיל 5 — DROP, TRUNCATE, DELETE

</div>

```sql
-- a   9
CREATE TABLE dog AS SELECT * FROM animal WHERE species_id = 1;

-- b
SELECT sql FROM sqlite_master WHERE name = 'dog';
```

```text
CREATE TABLE dog(
  animal_id INT,
  name TEXT,
  species_id INT,
  breed TEXT,
  sex TEXT,
  birth_date TEXT,
  weight_kg REAL,
  chip_number TEXT,
  status TEXT,
  is_neutered INT
)
```

<div dir="rtl">

**חסר הכול חוץ מהשמות והטיפוסים:** אין `PRIMARY KEY`, אין `NOT NULL`, אין `CHECK` על `sex`, אין `UNIQUE` על השבב, אין `REFERENCES species`. **`CREATE TABLE … AS` מעתיק נתונים, לא חוקים.**

</div>

```sql
-- c
DELETE FROM dog;           -- SQLite. Oracle (fastest): TRUNCATE TABLE dog;
DROP TABLE dog;

-- d
SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name;
PRAGMA table_info(walk);
```

<div dir="rtl">

**ג.** ב‑Oracle `TRUNCATE TABLE dog` מהיר בהרבה מ‑`DELETE` על טבלה גדולה — הוא לא מוחק שורה‑שורה, אלא משחרר את כל השטח בבת אחת. **המחיר:** זה DDL — `COMMIT` אוטומטי, **אין `ROLLBACK`**, ואין `WHERE`.

---

## ✅ תרגיל 6 — הפרויקט שלכם

אין פתרון אחד — זה הפרויקט שלכם. **רשימת בדיקה:**

| ✔ | הבדיקה |
|---|--------|
| ☐ | לכל טבלה `PRIMARY KEY` |
| ☐ | כל `*` ב‑ERD ⟵ `NOT NULL` |
| ☐ | כל קו ב‑ERD ⟵ `REFERENCES` בצד ה"רבים" |
| ☐ | טבלאות קישור לכל יחס רבים‑לרבים (מודול 5) |
| ☐ | `STRICT` על כל טבלה |
| ☐ | `DROP TABLE IF EXISTS` בסדר הפוך בראש הסקריפט |
| ☐ | הסקריפט רץ **פעמיים ברצף** בלי שגיאה |
| ☐ | 3 שאילתות `JOIN` מחזירות תוצאות הגיוניות |

> 💡 **"רץ פעמיים ברצף"** היא הבדיקה החשובה ביותר. אם הסקריפט נכשל בפעם השנייה — ה‑`DROP`‑ים חסרים או בסדר הלא נכון.

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[❓ לשאלות](questions.md)**

</div>

</div>

<!-- exam-style:start -->
<div dir="rtl">

---

## 🎓 תרגול בסגנון הבחינה: פתרונות

**ב1.** **3.**

**ב2.** | הפקודה | מה נמחק? | הטבלה נשארת? |
|---|---|---|
| `DELETE ... WHERE` | רק הרשומות שעונות על התנאי | כן |
| `DELETE FROM Clubs` | כל הרשומות | כן, ריקה |
| `DROP TABLE Clubs` | הכול, כולל המבנה | **לא** |

**ב3.** ```sql
CREATE TABLE Halls (
  HallCode  INTEGER PRIMARY KEY,
  HallName  TEXT NOT NULL,
  Capacity  INTEGER
);
```


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
CREATE TABLE Clubs (
  ClubId      INTEGER PRIMARY KEY,
  ClubName    TEXT    NOT NULL UNIQUE,
  TeacherCode INTEGER REFERENCES Teachers(TeacherCode),
  MeetingDay  TEXT,
  MaxStudents INTEGER NOT NULL DEFAULT 20,
  Fee         REAL    NOT NULL DEFAULT 0
);

-- ש2
INSERT INTO Clubs (ClubId, ClubName, TeacherCode, MeetingDay) VALUES (1, 'רובוטיקה', 3, 'שלישי');
INSERT INTO Clubs VALUES (2, 'דיבייט', 4, 'חמישי', 15, 50.5);
INSERT INTO Clubs (ClubId, ClubName) VALUES (3, 'שחמט');
SELECT * FROM Clubs;

-- ש3
ALTER TABLE Clubs ADD COLUMN RoomNumber INTEGER;

-- ש4
ALTER TABLE Clubs RENAME COLUMN Fee TO MonthlyFee;

-- ש5
ALTER TABLE Clubs RENAME TO SchoolClubs;

-- ש6
CREATE TABLE ClubMembers (
  ClubId    INTEGER,
  StudentId INTEGER,
  JoinDate  TEXT,
  PRIMARY KEY (ClubId, StudentId),
  FOREIGN KEY (ClubId)    REFERENCES SchoolClubs(ClubId),
  FOREIGN KEY (StudentId) REFERENCES Students(StudentId)
);
INSERT INTO ClubMembers VALUES (1, 1007, '2026-09-15'), (1, 1013, '2026-09-15'), (2, 1016, '2026-09-16');

-- ש7
CREATE TABLE TopStudents AS
SELECT s.StudentId, s.FirstName || ' ' || s.LastName AS FullName, ROUND(AVG(g.Grade),1) AS Avg1
FROM   Grades g, Students s WHERE g.StudentId = s.StudentId
GROUP  BY s.StudentId, s.FirstName, s.LastName
HAVING AVG(g.Grade) >= 90;

-- ש8
INSERT INTO SchoolClubs (ClubId, ClubName, MaxStudents) VALUES (4, 'תיאטרון', 'עשרים');
SELECT ClubId, ClubName, MaxStudents, TYPEOF(MaxStudents) AS WhatType FROM SchoolClubs;

-- ש9
SELECT name, type FROM sqlite_master WHERE type = 'table' ORDER BY name;

-- ש10
DROP TABLE TopStudents;
SELECT name FROM sqlite_master WHERE name = 'TopStudents';     -- 0 שורות

-- ש11
DELETE FROM ClubMembers;
SELECT COUNT(*) AS Rows1 FROM ClubMembers;                     -- 0
SELECT name FROM sqlite_master WHERE name = 'ClubMembers';     -- הטבלה עדיין שם

-- ש12
ALTER TABLE Students ADD COLUMN Email TEXT NOT NULL;                                -- ❌
ALTER TABLE Students ADD COLUMN Email TEXT NOT NULL DEFAULT 'unknown@school.il';    -- ✅
ALTER TABLE Students DROP COLUMN Email;                                             -- ✅
ALTER TABLE Students DROP COLUMN StudentId;                                         -- ❌
```

<div dir="rtl">

**ש1.** ב‑`CREATE TABLE` יש שתי שכבות: **טיפוס** (`INTEGER`, `TEXT`, `REAL`) ו**אילוצים** (`NOT NULL`, `UNIQUE`, `DEFAULT`, `PRIMARY KEY`, `REFERENCES`). הטיפוס אומר *איזה סוג ערך*; האילוץ אומר *אילו ערכים מותרים*.

**ש2.**

<figure dir="ltr" class="dbtable">

| ClubId | ClubName | TeacherCode | MeetingDay | MaxStudents | Fee |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | רובוטיקה | 3 | שלישי | 20 | 0 |
| 2 | דיבייט | 4 | חמישי | 15 | 50.5 |
| 3 | שחמט | NULL | NULL | 20 | 0 |

</figure>

אצל שחמט: `MaxStudents = 20` ו‑`Fee = 0` — מ**ברירת המחדל**. אבל `TeacherCode` ו‑`MeetingDay` הם **`NULL`**.

**למה שונה?** כי לשתי העמודות האחרונות **לא הגדרנו `DEFAULT`**. כשעמודה חסרה ב‑`INSERT`, SQL שואל: "יש לה `DEFAULT`?" — אם כן, מכניס אותו; אם לא, מכניס `NULL`. `DEFAULT` הוא לא "הערך השכיח", הוא **הערך שנכנס כשלא אמרו כלום**.

**ש3.** שלוש השורות הקיימות קיבלו **`NULL`** ב‑`RoomNumber`. זה הכרחי: הטבלה כבר מכילה נתונים, ול‑SQL אין מה לשים שם. (ולכן גם אסור להוסיף עמודת `NOT NULL` בלי `DEFAULT` — ראו ש12.)

<figure dir="ltr" class="dbtable">

| ClubId | ClubName | TeacherCode | MeetingDay | MaxStudents | Fee | RoomNumber |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | רובוטיקה | 3 | שלישי | 20 | 0 | NULL |
| 2 | דיבייט | 4 | חמישי | 15 | 50.5 | NULL |
| 3 | שחמט | NULL | NULL | 20 | 0 | NULL |

</figure>

**ש4.** הנתונים **לא זזו** — רק השם. `RENAME COLUMN` הוא שינוי במבנה, לא בתוכן.

<figure dir="ltr" class="dbtable">

| ClubId | ClubName | MonthlyFee |
|:---:|:---:|:---:|
| 1 | רובוטיקה | 0 |
| 2 | דיבייט | 50.5 |
| 3 | שחמט | 0 |

</figure>

> ⚠️ ובכל זאת — **כל שאילתה בעולם שכתבה `Fee` נשברה עכשיו.** שינוי שם עמודה הוא הפעולה שהורסת הכי הרבה קוד קיים ביחס לכמה שהיא נראית תמימה. בעבודה אמיתית עושים את זה בשלבים: מוסיפים את החדשה, מעבירים את הקוראים, ורק אז מוחקים את הישנה.

**ש5.** `RENAME TO` — 3 שורות, אותן שורות, שם אחר.

**ש6.** **מפתח ראשי מורכב** הוא בדיוק הכלי לטבלת קשר M:M: הצמד `(ClubId, StudentId)` ייחודי, ולכן אי אפשר לרשום אותו תלמיד לאותו חוג פעמיים — ובכל זאת אפשר לרשום אותו לכמה חוגים, ואת אותו חוג לכמה תלמידים.

<figure dir="ltr" class="dbtable">

| ClubId | StudentId | JoinDate |
|:---:|:---:|:---:|
| 1 | 1007 | 2026-09-15 |
| 1 | 1013 | 2026-09-15 |
| 2 | 1016 | 2026-09-16 |

</figure>

**ש7.** **5 תלמידים.**

`CREATE TABLE … AS SELECT` (מקוצר **CTAS**) בונה טבלה **והטיפוסים נגזרים מהשאילתה** — לא אתם קבעתם אותם, אלא בסיס הנתונים, לפי מה שהחזיר כל ביטוי. זה נוח ומסוכן: אין `PRIMARY KEY`, אין `NOT NULL`, אין אילוצים. CTAS מייצר **טבלת עבודה**, לא טבלה שראויה לשבת בבסיס הנתונים.

<figure dir="ltr" class="dbtable">

| StudentId | FullName | Avg1 |
|:---:|:---:|:---:|
| 1016 | ראניה עבאס | 97 |
| 1010 | תמר שושן | 96 |
| 1002 | נור עזאם | 94.7 |
| 1013 | דניאל פרץ | 92 |
| 1007 | עומר ביטון | 91.3 |

</figure>

**ש8.** **ה‑`INSERT` לא נכשל.** המילה `'עשרים'` נכנסה לעמודה שהוגדרה `INTEGER`, ו‑`TYPEOF` מחזירה **`text`**.

<figure dir="ltr" class="dbtable">

| ClubId | ClubName | MaxStudents | WhatType |
|:---:|:---:|:---:|:---:|
| 1 | רובוטיקה | 20 | integer |
| 2 | דיבייט | 15 | integer |
| 3 | שחמט | 20 | integer |
| 4 | תיאטרון | עשרים | **text** |

</figure>

**זו תכונה של SQLite בשם *type affinity*:** הטיפוס בהגדרת העמודה הוא **העדפה**, לא חוק. SQLite מנסה להמיר את מה שנתתם; אם לא הצליח — שומר אותו כמו שהוא. **בכל בסיס נתונים אחר** (אורקל, MySQL, SQL Server) זו שגיאה מיידית.

**ההשלכה על `SUM(MaxStudents)`:** המחרוזת `'עשרים'` מומרת ל‑**0** בחישוב, ולכן הסכום יהיה 55 במקום 75 — **בלי שגיאה ובלי אזהרה**.

ולכן, בשיעור הזה, זכרו שני דברים: (1) בסביבת התרגול הטיפוס לא מגן עליכם, ולכן אל תסתמכו עליו; (2) מה ש**כן** נאכף ב‑SQLite הוא **אילוצים** — `NOT NULL`, `UNIQUE`, `CHECK`, `PRIMARY KEY`. זה בדיוק מה שהופך אותם למגן האמיתי, והנושא של שיעור 27.

**ש9.** `sqlite_master` היא **קטלוג המערכת** — טבלה שבה בסיס הנתונים מתאר את עצמו. שבע הטבלאות של `school.sql` ועוד שלוש שבניתם:

<figure dir="ltr" class="dbtable">

| name | type |
|:---:|:---:|
| Absences | table |
| Cities | table |
| Classes | table |
| ClubMembers | table |
| Courses | table |
| Grades | table |
| SchoolClubs | table |
| Students | table |
| Teachers | table |
| TopStudents | table |

</figure>

> 💡 `SELECT sql FROM sqlite_master WHERE name = 'Students';` מחזיר את פקודת ה‑`CREATE TABLE` **המלאה** של הטבלה. באורקל המקבילות הן `USER_TABLES` ו‑`USER_TAB_COLUMNS`.

**ש10.** החיפוש החזיר **0 שורות** — הטבלה נעלמה מהקטלוג.

**ש11.** `COUNT(*)` מחזיר **0**, אבל `ClubMembers` **עדיין קיימת** ב‑`sqlite_master`.

| הפקודה | השפה | מה נעלם | מה נשאר |
|---------|------|----------|----------|
| `DELETE FROM T` | **DML** | השורות | הטבלה, העמודות, האילוצים, ההרשאות |
| `DROP TABLE T` | **DDL** | **הכול** | כלום. גם אי אפשר יותר `SELECT * FROM T` |
| `TRUNCATE TABLE T` | DDL (לא ב‑SQLite) | השורות, מהר ובלי לוג | הטבלה — אבל **אין `ROLLBACK`** |

ההבדל המעשי: אחרי `DELETE` אפשר להכניס שורות חדשות מיד. אחרי `DROP` צריך `CREATE TABLE` מההתחלה — ועם כל האילוצים, אחרת בניתם טבלה אחרת בשם זהה.

**ש12.**

</div>

```text
1.  ALTER TABLE Students ADD COLUMN Email TEXT NOT NULL;
    ❌  Cannot add a NOT NULL column with default value NULL

2.  ALTER TABLE Students ADD COLUMN Email TEXT NOT NULL DEFAULT 'unknown@school.il';
    ✅  עברה — 18 השורות קיבלו 'unknown@school.il'

3.  ALTER TABLE Students DROP COLUMN Email;
    ✅  עברה

4.  ALTER TABLE Students DROP COLUMN StudentId;
    ❌  cannot drop PRIMARY KEY column: "StudentId"
```

<div dir="rtl">

**הראשונה** נכשלה כי יש בטבלה **18 שורות קיימות**. העמודה החדשה חייבת ערך בכל שורה (`NOT NULL`), ואין שום ערך שבסיס הנתונים יכול לשים שם — הוא לא ממציא נתונים. השורה השנייה מוכיחה את זה: ברגע שנתנו `DEFAULT`, יש לו מה לכתוב, וזה עובד. **הכלל:** `ADD COLUMN … NOT NULL` דורש `DEFAULT` בכל טבלה שאינה ריקה.

**הרביעית** נכשלה כי `StudentId` הוא **המפתח הראשי**. למחוק אותו זה למחוק את הדרך לזהות שורה — ואיתה כל המפתחות הזרים ב‑`Grades` וב‑`Absences` שמצביעים אליו. בסיס הנתונים מסרב, ובצדק: אין "טבלת תלמידים בלי מזהה תלמיד", יש רשימה.

> 💡 **ל‑`ALTER TABLE` ב‑SQLite יש מגבלות נוספות** שאין באורקל: אי אפשר לשנות טיפוס של עמודה קיימת, ואי אפשר להוסיף אילוץ לטבלה קיימת. הדרך המקובלת היא "בנה חדשה, העתק, מחק, שנה שם" — וזה בדיוק מה שתעשו ידנית אם תצטרכו.

</div>
<!-- classroom:end -->
