<div dir="rtl">

# שיעור 13 — פתרונות

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../12-insert-update-delete/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../14-exam-simulation/solutions.md)

> ⚠️ קודם נסו לבד! כל תוצאה כאן היא פלט אמיתי של SQLite. בפקודות שמשנות נתונים כל תרגיל רץ על בסיס נתונים טרי.

</div>

<div dir="rtl">

---

## ✏️ תרגילים — 🎵 בית הספר למוזיקה "צלילים"

</div>

<div dir="rtl">

### 1. 🟢 צרו טבלה `Rooms` עם: מספר חדר (מפתח ראשי), קומה (מספר, חובה) ושם החדר (טקסט). הוסיפו 2 חדרים.

</div>

```sql
CREATE TABLE Rooms (
  RoomNum    INTEGER PRIMARY KEY,
  RoomFloor  INTEGER NOT NULL,
  RoomName   TEXT
);
INSERT INTO Rooms VALUES (1, 1, 'אולם פסנתרים');
INSERT INTO Rooms VALUES (2, 2, 'חדר תופים');
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Rooms;
```

<div dir="rtl">

| RoomNum | RoomFloor | RoomName |
|---|---|---|
| 1 | 1 | אולם פסנתרים |
| 2 | 2 | חדר תופים |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 2. 🟢 הוסיפו לטבלת המורים עמודה `Email` מסוג טקסט.

</div>

```sql
ALTER TABLE Teachers ADD COLUMN Email TEXT;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT TeacherName, Email FROM Teachers;
```

<div dir="rtl">

| TeacherName | Email |
|---|---|
| סמיר חלבי | *NULL* |
| רונית לוי | *NULL* |
| אמיר עזאם | *NULL* |
| דנה כהן | *NULL* |
| יוסי פרץ | *NULL* |
| נור מנסור | *NULL* |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 3. 🟢 מחקו מטבלת הלוקרים את העמודה `LockerFloor`.

</div>

```sql
ALTER TABLE Lockers DROP COLUMN LockerFloor;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Lockers;
```

<div dir="rtl">

| LockerNum | LockerPupil |
|---|---|
| 1 | 202 |
| 2 | 205 |
| 3 | 207 |
| 4 | 210 |
| 5 | 201 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 4. 🟡 הוסיפו לטבלת התלמידים עמודה `Active` עם ערך ברירת מחדל 1. (רמז: `DEFAULT 1`)

</div>

```sql
ALTER TABLE Pupils ADD COLUMN Active INTEGER DEFAULT 1;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT FirstName, Active FROM Pupils;
```

<div dir="rtl">

| FirstName | Active |
|---|---|
| אדם | 1 |
| מאיה | 1 |
| כרים | 1 |
| שירה | 1 |
| רמי | 1 |
| תמר | 1 |
| ליאן | 1 |
| עומר | 1 |
| סאלי | 1 |
| יואב | 1 |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 5. 🟡 הוסיפו עמודה `Email` לתלמידים, ועדכנו לתלמיד 201 את הכתובת 'adam@mail.com'.

</div>

```sql
ALTER TABLE Pupils ADD COLUMN Email TEXT;
UPDATE Pupils SET Email = 'adam@mail.com' WHERE PupilId = 201;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT PupilId, FirstName, Email FROM Pupils WHERE PupilId IN (201, 202);
```

<div dir="rtl">

| PupilId | FirstName | Email |
|---|---|---|
| 201 | אדם | adam@mail.com |
| 202 | מאיה | *NULL* |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 6. 🟡 צרו טבלת `Exams` (מבחני נגינה): קוד מבחן (PK), תלמיד (FK ל‑Pupils), ציון עם `CHECK` בין 0 ל‑100. הוסיפו 3 מבחנים.

</div>

```sql
CREATE TABLE Exams (
  ExamId     INTEGER PRIMARY KEY,
  ExamPupil  INTEGER NOT NULL REFERENCES Pupils(PupilId),
  ExamScore  INTEGER CHECK (ExamScore BETWEEN 0 AND 100)
);
INSERT INTO Exams VALUES (1, 201, 88);
INSERT INTO Exams VALUES (2, 202, 95);
INSERT INTO Exams VALUES (3, 205, 72);
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT FirstName, ExamScore
FROM   Exams, Pupils
WHERE  ExamPupil = PupilId;
```

<div dir="rtl">

| FirstName | ExamScore |
|---|---|
| אדם | 88 |
| מאיה | 95 |
| רמי | 72 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 7. 🔴 צרו טבלה מקשרת `Performances` (איזה תלמיד מופיע באיזה קונצרט) עם **מפתח ראשי מורכב**. צרו גם את טבלת `Concerts`, והוסיפו נתונים.

</div>

```sql
CREATE TABLE Concerts (
  ConcertId    INTEGER PRIMARY KEY,
  ConcertName  TEXT NOT NULL
);
CREATE TABLE Performances (
  PerfConcert  INTEGER REFERENCES Concerts(ConcertId),
  PerfPupil    INTEGER REFERENCES Pupils(PupilId),
  PieceName    TEXT,
  PRIMARY KEY (PerfConcert, PerfPupil)
);
INSERT INTO Concerts VALUES (1, 'קונצרט חנוכה');
INSERT INTO Concerts VALUES (2, 'קונצרט סוף שנה');
INSERT INTO Performances VALUES (1, 202, 'פור אליזה');
INSERT INTO Performances VALUES (1, 205, 'בלוז בגיטרה');
INSERT INTO Performances VALUES (2, 202, 'סונטה');
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT ConcertName, FirstName, PieceName
FROM   Performances, Concerts, Pupils
WHERE  PerfConcert = ConcertId AND PerfPupil = PupilId;
```

<div dir="rtl">

| ConcertName | FirstName | PieceName |
|---|---|---|
| קונצרט חנוכה | מאיה | פור אליזה |
| קונצרט חנוכה | רמי | בלוז בגיטרה |
| קונצרט סוף שנה | מאיה | סונטה |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 8. 🔴 צרו טבלה, הוסיפו לה שורה, ואז מחקו אותה עם `DROP TABLE`. בדקו ברשימת הטבלאות שהיא נעלמה.

</div>

```sql
CREATE TABLE Temp (x INTEGER);
INSERT INTO Temp VALUES (1);
DROP TABLE Temp;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT name FROM sqlite_master WHERE type = 'table';
```

<div dir="rtl">

| name |
|---|
| Cities |
| Instruments |
| Teachers |
| Pupils |
| Registrations |
| Lockers |

**התוצאה: 6 שורות**

> 💡 `sqlite_master` היא "טבלת הטבלאות" של SQLite — הרשימה של כל מה שיש בבסיס הנתונים.

</div>

<div dir="rtl">

### 9. 🟢 צרו טבלה `Books` לספרי תווים: קוד (PK), שם (חובה), מחיר. הוסיפו 2 ספרים.

</div>

```sql
CREATE TABLE Books (
  BookCode   INTEGER PRIMARY KEY,
  BookName   TEXT NOT NULL,
  BookPrice  INTEGER
);
INSERT INTO Books VALUES (1, 'תווים לפסנתר א', 60);
INSERT INTO Books VALUES (2, 'שיטת גיטרה', 75);
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Books;
```

<div dir="rtl">

| BookCode | BookName | BookPrice |
|---|---|---|
| 1 | תווים לפסנתר א | 60 |
| 2 | שיטת גיטרה | 75 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 10. 🟢 הוסיפו לטבלת הכלים עמודה `Price` (מספר).

</div>

```sql
ALTER TABLE Instruments ADD COLUMN Price INTEGER;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Instruments;
```

<div dir="rtl">

| InstCode | InstName | InstFamily | Price |
|---|---|---|---|
| 10 | פסנתר | קלידים | *NULL* |
| 20 | גיטרה | מיתר | *NULL* |
| 30 | כינור | מיתר | *NULL* |
| 40 | תופים | הקשה | *NULL* |
| 50 | חליל | נשיפה | *NULL* |
| 60 | עוד | מיתר | *NULL* |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 11. 🟡 שנו את שם העמודה `TeacherPhone` ל‑`Phone`.

</div>

```sql
ALTER TABLE Teachers RENAME COLUMN TeacherPhone TO Phone;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT TeacherName, Phone FROM Teachers;
```

<div dir="rtl">

| TeacherName | Phone |
|---|---|
| סמיר חלבי | 050-1234567 |
| רונית לוי | 052-2345678 |
| אמיר עזאם | *NULL* |
| דנה כהן | 054-4567890 |
| יוסי פרץ | 053-5678901 |
| נור מנסור | *NULL* |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 12. 🟡 הוסיפו לטבלת הרישומים עמודה `Paid` עם ברירת מחדל 0, ועדכנו ל‑1 את הרישומים של 2025.

</div>

```sql
ALTER TABLE Registrations ADD COLUMN Paid INTEGER DEFAULT 0;
UPDATE Registrations SET Paid = 1 WHERE RegYear = 2025;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT Paid, COUNT(*) AS Regs FROM Registrations GROUP BY Paid;
```

<div dir="rtl">

| Paid | Regs |
|---|---|
| 0 | 9 |
| 1 | 5 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 13. 🟡 מחקו את הטבלה `Lockers` לגמרי.

</div>

```sql
DROP TABLE Lockers;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT name FROM sqlite_master WHERE type = 'table';
```

<div dir="rtl">

| name |
|---|
| Cities |
| Instruments |
| Teachers |
| Pupils |
| Registrations |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 14. 🔴 צרו טבלה `Rentals` (השכרת כלים): קוד (PK), תלמיד (FK ל‑Pupils), כלי (FK ל‑Instruments), חודשים עם `CHECK` בין 1 ל‑12. הוסיפו 2 השכרות והציגו שם תלמיד ושם כלי.

</div>

```sql
CREATE TABLE Rentals (
  RentId     INTEGER PRIMARY KEY,
  RentPupil  INTEGER REFERENCES Pupils(PupilId),
  RentInst   INTEGER REFERENCES Instruments(InstCode),
  Months     INTEGER CHECK (Months BETWEEN 1 AND 12)
);
INSERT INTO Rentals VALUES (1, 203, 20, 6);
INSERT INTO Rentals VALUES (2, 209, 10, 12);
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT FirstName, InstName, Months
FROM   Rentals, Pupils, Instruments
WHERE  RentPupil = PupilId AND RentInst = InstCode;
```

<div dir="rtl">

| FirstName | InstName | Months |
|---|---|---|
| כרים | גיטרה | 6 |
| סאלי | פסנתר | 12 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

---

## 🎓 בסגנון הבחינה — 🎮 חנות משחקי מחשב

</div>

<div dir="rtl">

### 1. 🟢 הוסיפו לטבלת המשתמשים עמודה `Phone` מסוג טקסט.

</div>

```sql
ALTER TABLE Users ADD COLUMN Phone TEXT;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT UserId, FirstName, Phone FROM Users LIMIT 3;
```

<div dir="rtl">

| UserId | FirstName | Phone |
|---|---|---|
| 1 | רמי | *NULL* |
| 2 | שני | *NULL* |
| 3 | וליד | *NULL* |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 2. 🟢 מחקו מטבלת החברות את העמודה `Country`.

</div>

```sql
ALTER TABLE Companies DROP COLUMN Country;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Companies;
```

<div dir="rtl">

| CompCode | CompName |
|---|---|
| 10 | Nintendo |
| 20 | Electronic Arts |
| 30 | Ubisoft |
| 40 | Maxis |
| 50 | Playtika |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 3. 🟡 צרו טבלת `Reviews`: קוד (PK), משתמש (FK ל‑Users), משחק (FK ל‑Games), ציון עם `CHECK` בין 1 ל‑5. הוסיפו 2 ביקורות.

</div>

```sql
CREATE TABLE Reviews (
  ReviewId    INTEGER PRIMARY KEY,
  ReviewUser  INTEGER REFERENCES Users(UserId),
  ReviewGame  INTEGER REFERENCES Games(GameCode),
  Stars       INTEGER CHECK (Stars BETWEEN 1 AND 5)
);
INSERT INTO Reviews VALUES (1, 1, 2, 5);
INSERT INTO Reviews VALUES (2, 3, 8, 3);
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT FirstName, GameName, Stars
FROM   Reviews, Users, Games
WHERE  ReviewUser = UserId AND ReviewGame = GameCode;
```

<div dir="rtl">

| FirstName | GameName | Stars |
|---|---|---|
| רמי | FIFA | 5 |
| וליד | NBA Live | 3 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 4. 🟡 מחקו את הטבלה `Categories`.

</div>

```sql
DROP TABLE Categories;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT name FROM sqlite_master WHERE type = 'table';
```

<div dir="rtl">

| name |
|---|
| Companies |
| Games |
| Users |
| Orders |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 5. 🔴 השלימו את הפקודה שמוסיפה עמודת `Discount` למשחקים עם ערך ברירת מחדל 0.

</div>

```sql
ALTER TABLE Games ADD COLUMN Discount INTEGER DEFAULT 0;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT GameName, Discount FROM Games LIMIT 3;
```

<div dir="rtl">

| GameName | Discount |
|---|---|
| Mario Kart | 0 |
| FIFA | 0 |
| Assassin's Creed | 0 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 6. 🔴 כתבו (על דף — SQLite לא מריץ את זה) את הפקודה שמשנה את טיפוס העמודה `Email` ל‑`VARCHAR(50)`. מה כן אפשר להריץ: שנו את שם העמודה `Email` ל‑`Mail`.

</div>

```sql
ALTER TABLE Users RENAME COLUMN Email TO Mail;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT FirstName, Mail FROM Users LIMIT 3;
```

<div dir="rtl">

| FirstName | Mail |
|---|---|
| רמי | rami@mail.com |
| שני | shani@mail.com |
| וליד | walid@mail.com |

**התוצאה: 3 שורות**

> 💡 בבחינה: `ALTER TABLE Users MODIFY COLUMN Email VARCHAR(50);`

</div>

<div dir="rtl">

---

## 🏠 תרגול נוסף — 🏫 בית הספר "עתיד"

</div>

<div dir="rtl">

### 1. 🟢 הוסיפו לטבלת המקצועות עמודה `Room` (מספר).

</div>

```sql
ALTER TABLE Courses ADD COLUMN Room INTEGER;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT CourseName, Room FROM Courses;
```

<div dir="rtl">

| CourseName | Room |
|---|---|
| מתמטיקה 5 יח"ל | *NULL* |
| אנגלית 4 יח"ל | *NULL* |
| מבוא לבסיסי נתונים | *NULL* |
| היסטוריה | *NULL* |
| חינוך גופני | *NULL* |
| מתמטיקה 3 יח"ל | *NULL* |
| סדנת פרויקטים | *NULL* |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 2. 🟡 צרו טבלת `Parents`: קוד הורה (PK), שם (חובה), טלפון (ייחודי — `UNIQUE`), תלמיד (FK ל‑Students). הוסיפו 2 הורים.

</div>

```sql
CREATE TABLE Parents (
  ParentId    INTEGER PRIMARY KEY,
  ParentName  TEXT NOT NULL,
  Phone       TEXT UNIQUE,
  StudentId   INTEGER REFERENCES Students(StudentId)
);
INSERT INTO Parents VALUES (1, 'סמיר חלבי', '050-9000001', 1001);
INSERT INTO Parents VALUES (2, 'רינה כהן',  '052-9000002', 1003);
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT ParentName, S.FirstName AS Child
FROM   Parents P, Students S
WHERE  P.StudentId = S.StudentId;
```

<div dir="rtl">

| ParentName | Child |
|---|---|
| סמיר חלבי | אדם |
| רינה כהן | יואב |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 3. 🔴 שנו את השם של העמודה `Reason` בטבלת ההיעדרויות ל‑`Note`, ומחקו את העמודה `Excused`.

</div>

```sql
ALTER TABLE Absences RENAME COLUMN Reason TO Note;
ALTER TABLE Absences DROP COLUMN Excused;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Absences LIMIT 3;
```

<div dir="rtl">

| AbsenceId | StudentId | AbsenceDate | Note |
|---|---|---|---|
| 1 | 1003 | 2026-09-02 | מחלה |
| 2 | 1003 | 2026-09-03 | מחלה |
| 3 | 1004 | 2026-09-07 | *NULL* |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 4. 🟢 הוסיפו לטבלת התלמידים עמודה `Email`.

</div>

```sql
ALTER TABLE Students ADD COLUMN Email TEXT;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT FirstName, Email FROM Students LIMIT 3;
```

<div dir="rtl">

| FirstName | Email |
|---|---|
| אדם | *NULL* |
| נור | *NULL* |
| יואב | *NULL* |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 5. 🟡 מחקו מטבלת המורים את העמודה `Phone`.

</div>

```sql
ALTER TABLE Teachers DROP COLUMN Phone;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Teachers LIMIT 2;
```

<div dir="rtl">

| TeacherCode | FirstName | LastName | Subject | HireDate | Salary | CityCode |
|---|---|---|---|---|---|---|
| 1 | נביל | סרחאן | מתמטיקה | 2012-09-01 | 14500 | 1 |
| 2 | רונית | בר-לב | אנגלית | 2018-09-01 | 11200 | 4 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 6. 🔴 צרו טבלת `Clubs` (חוגים) עם קוד (PK), שם (חובה, ייחודי) ומורה אחראי (FK ל‑Teachers). הוסיפו 2 חוגים והציגו שם חוג ושם מורה.

</div>

```sql
CREATE TABLE Clubs (
  ClubCode     INTEGER PRIMARY KEY,
  ClubName     TEXT NOT NULL UNIQUE,
  TeacherCode  INTEGER REFERENCES Teachers(TeacherCode)
);
INSERT INTO Clubs VALUES (1, 'מקהלה', 4);
INSERT INTO Clubs VALUES (2, 'שחמט', 1);
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT ClubName, FirstName
FROM   Clubs C, Teachers T
WHERE  C.TeacherCode = T.TeacherCode;
```

<div dir="rtl">

| ClubName | FirstName |
|---|---|
| מקהלה | אורלי |
| שחמט | נביל |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../12-insert-update-delete/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../14-exam-simulation/solutions.md)

</div>
