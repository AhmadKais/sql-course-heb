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

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../12-insert-update-delete/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../14-exam-simulation/solutions.md)

</div>
