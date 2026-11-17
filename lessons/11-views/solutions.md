<div dir="rtl">

# שיעור 11 — פתרונות

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../10-subqueries/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../12-insert-update-delete/solutions.md)

> ⚠️ קודם נסו לבד! כל תוצאה כאן היא פלט אמיתי של SQLite. בפקודות שמשנות נתונים כל תרגיל רץ על בסיס נתונים טרי.

</div>

<div dir="rtl">

---

## ❓ שאלות: מה תחזיר השאילתה?

</div>

<div dir="rtl">

### שאלה 1

</div>

```sql
CREATE VIEW Cheap AS
SELECT TeacherName, HourRate FROM Teachers WHERE HourRate < 130;

SELECT COUNT(*) FROM Cheap;
```

<div dir="rtl">

| COUNT(*) |
|---|
| 3 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### שאלה 2

</div>

```sql
CREATE VIEW Q1 AS
SELECT   RegPupil, COUNT(*) AS Lessons
FROM     Registrations
GROUP BY RegPupil;

SELECT Lessons, COUNT(*)
FROM   Q1
GROUP BY Lessons;
```

<div dir="rtl">

| Lessons | COUNT(*) |
|---|---|
| 1 | 6 |
| 2 | 4 |

**התוצאה: 2 שורות**

> 💡 קיבוץ על תוצאה של קיבוץ: כמה תלמידים לומדים שיעור אחד, וכמה — שניים.

</div>

<div dir="rtl">

---

## ✏️ תרגילים — 🎵 בית הספר למוזיקה "צלילים"

</div>

<div dir="rtl">

### 1. 🟢 צרו VIEW בשם `Beginners` עם כל הרישומים של 'מתחיל', והציגו אותו.

</div>

```sql
CREATE VIEW Beginners AS
SELECT * FROM Registrations WHERE PupilLevel = 'מתחיל';

SELECT * FROM Beginners;
```

<div dir="rtl">

| RegPupil | RegTeacher | RegYear | PupilLevel | MonthlyFee |
|---|---|---|---|---|
| 201 | 5 | 2025 | מתחיל | 280 |
| 203 | 1 | 2025 | מתחיל | 300 |
| 204 | 2 | 2025 | מתחיל | 380 |
| 207 | 4 | 2025 | מתחיל | 350 |
| 209 | 2 | 2025 | מתחיל | 380 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 2. 🟢 צרו VIEW בשם `TeacherRegs` — לכל מורה (`RegTeacher`) מספר הרישומים (`Regs`). הציגו רק מורים עם יותר מ‑2.

</div>

```sql
CREATE VIEW TeacherRegs AS
SELECT   RegTeacher, COUNT(*) AS Regs
FROM     Registrations
GROUP BY RegTeacher;

SELECT * FROM TeacherRegs WHERE Regs > 2;
```

<div dir="rtl">

| RegTeacher | Regs |
|---|---|
| 1 | 3 |
| 2 | 3 |
| 3 | 3 |
| 5 | 3 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 3. 🟡 בעזרת `TeacherRegs` מהסעיף הקודם: שם המורה ומספר הרישומים שלו.

</div>

```sql
CREATE VIEW TeacherRegs AS
SELECT   RegTeacher, COUNT(*) AS Regs
FROM     Registrations
GROUP BY RegTeacher;

SELECT TeacherName, Regs
FROM   TeacherRegs, Teachers
WHERE  RegTeacher = TeacherCode;
```

<div dir="rtl">

| TeacherName | Regs |
|---|---|
| סמיר חלבי | 3 |
| רונית לוי | 3 |
| אמיר עזאם | 3 |
| דנה כהן | 2 |
| יוסי פרץ | 3 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 4. 🟡 צרו VIEW בשם `PupilCity` — שם התלמיד ושם העיר. השתמשו בו כדי להציג רק תלמידים מירכא.

</div>

```sql
CREATE VIEW PupilCity AS
SELECT FirstName, LastName, CityName
FROM   Pupils, Cities
WHERE  HomeTown = CityCode;

SELECT FirstName, LastName FROM PupilCity WHERE CityName = 'ירכא';
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| אדם | חלבי |
| כרים | עזאם |
| ליאן | קבלאן |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 5. 🟡 צרו VIEW בשם `Income` — לכל שנת רישום סך התשלומים (`Total`). הציגו את השנה עם ההכנסה הגבוהה ביותר.

</div>

```sql
CREATE VIEW Income AS
SELECT   RegYear, SUM(MonthlyFee) AS Total
FROM     Registrations
GROUP BY RegYear;

SELECT RegYear, Total
FROM   Income
WHERE  Total = (SELECT MAX(Total) FROM Income);
```

<div dir="rtl">

| RegYear | Total |
|---|---|
| 2025 | 1690 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 6. 🔴 צרו VIEW בשם `TeacherAvg` — לכל מורה התשלום הממוצע (`AvgFee`). הציגו את שמות המורים שהממוצע שלהם גבוה מ‑330, ממוינים מהגבוה.

</div>

```sql
CREATE VIEW TeacherAvg AS
SELECT   RegTeacher, AVG(MonthlyFee) AS AvgFee
FROM     Registrations
GROUP BY RegTeacher;

SELECT TeacherName, AvgFee
FROM   TeacherAvg, Teachers
WHERE  RegTeacher = TeacherCode AND AvgFee > 330
ORDER BY AvgFee DESC;
```

<div dir="rtl">

| TeacherName | AvgFee |
|---|---|
| רונית לוי | 386.67 |
| דנה כהן | 355.0 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 7. 🔴 בעזרת VIEW: כמה תלמידים לומדים בכל משפחת כלים? (VIEW שמחבר רישום למשפחת כלי, ועליו `GROUP BY`)

</div>

```sql
CREATE VIEW RegFamily AS
SELECT RegPupil, InstFamily
FROM   Registrations, Teachers, Instruments
WHERE  RegTeacher = TeacherCode AND TeachInst = InstCode;

SELECT   InstFamily, COUNT(DISTINCT RegPupil) AS Pupils
FROM     RegFamily
GROUP BY InstFamily;
```

<div dir="rtl">

| InstFamily | Pupils |
|---|---|
| הקשה | 3 |
| מיתר | 7 |
| קלידים | 3 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

---

## 🏠 תרגול נוסף — 🏫 בית הספר "עתיד"

</div>

<div dir="rtl">

### 1. 🟡 צרו VIEW בשם `StudentAvg` — לכל תלמיד הממוצע במחצית 1 (`AvgGrade`). הציגו תלמידים עם ממוצע 90 ומעלה.

</div>

```sql
CREATE VIEW StudentAvg AS
SELECT   StudentId, AVG(Grade) AS AvgGrade
FROM     Grades
WHERE    Term = 1
GROUP BY StudentId;

SELECT * FROM StudentAvg WHERE AvgGrade >= 90;
```

<div dir="rtl">

| StudentId | AvgGrade |
|---|---|
| 1002 | 94.67 |
| 1007 | 91.67 |
| 1010 | 95.67 |
| 1013 | 92.0 |
| 1016 | 96.25 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 2. 🔴 בעזרת `StudentAvg`: שמות התלמידים שהממוצע שלהם גבוה מממוצע הממוצעים.

</div>

```sql
CREATE VIEW StudentAvg AS
SELECT   StudentId, AVG(Grade) AS AvgGrade
FROM     Grades
WHERE    Term = 1
GROUP BY StudentId;

SELECT S.FirstName, S.LastName, ROUND(V.AvgGrade, 1) AS AvgGrade
FROM   StudentAvg V, Students S
WHERE  V.StudentId = S.StudentId
  AND  V.AvgGrade > (SELECT AVG(AvgGrade) FROM StudentAvg);
```

<div dir="rtl">

| FirstName | LastName | AvgGrade |
|---|---|---|
| אדם | חלבי | 84.7 |
| נור | עזאם | 94.7 |
| רוני | אברהם | 82.7 |
| עומר | ביטון | 91.7 |
| תמר | שושן | 95.7 |
| ליאור | לוי | 79.3 |
| דניאל | פרץ | 92.0 |
| הדיל | סעיד | 82.7 |
| ראניה | עבאס | 96.3 |

**התוצאה: 9 שורות**

</div>

<div dir="rtl">

### 3. 🔴 צרו VIEW בשם `ClassSize` — לכל כיתה מספר התלמידים. הציגו את שם הכיתה הגדולה ביותר.

</div>

```sql
CREATE VIEW ClassSize AS
SELECT   ClassCode, COUNT(*) AS Students
FROM     Students
WHERE    ClassCode IS NOT NULL
GROUP BY ClassCode;

SELECT ClassName, Students
FROM   ClassSize V, Classes C
WHERE  V.ClassCode = C.ClassCode
  AND  Students = (SELECT MAX(Students) FROM ClassSize);
```

<div dir="rtl">

| ClassName | Students |
|---|---|
| י1 | 4 |
| יב1 | 4 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../10-subqueries/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../12-insert-update-delete/solutions.md)

</div>
