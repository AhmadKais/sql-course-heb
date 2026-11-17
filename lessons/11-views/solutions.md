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

### שאלה 3

</div>

```sql
CREATE VIEW Q1 AS
SELECT   RegPupil, COUNT(*) AS Lessons, SUM(MonthlyFee) AS Total
FROM     Registrations
GROUP BY RegPupil;

SELECT MAX(Total) FROM Q1;
```

<div dir="rtl">

| MAX(Total) |
|---|
| 740 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### שאלה 4

</div>

```sql
CREATE VIEW Q1 AS
SELECT   RegPupil, COUNT(*) AS Lessons, SUM(MonthlyFee) AS Total
FROM     Registrations
GROUP BY RegPupil;

SELECT COUNT(*) FROM Q1 WHERE Lessons = 1;
```

<div dir="rtl">

| COUNT(*) |
|---|
| 6 |

**התוצאה: שורה אחת**

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

### 8. 🟢 צרו VIEW בשם `Expensive` — המורים שהמחיר שלהם 130 ומעלה. הציגו ממנו רק את השמות.

</div>

```sql
CREATE VIEW Expensive AS
SELECT * FROM Teachers WHERE HourRate >= 130;

SELECT TeacherName FROM Expensive;
```

<div dir="rtl">

| TeacherName |
|---|
| רונית לוי |
| דנה כהן |
| נור מנסור |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 9. 🟡 בעזרת Q1 (מספר שיעורים וסך תשלום לכל תלמיד): התלמידים שלומדים 2 שיעורים.

</div>

```sql
CREATE VIEW Q1 AS
SELECT   RegPupil, COUNT(*) AS Lessons, SUM(MonthlyFee) AS Total
FROM     Registrations
GROUP BY RegPupil;

SELECT RegPupil, Total
FROM   Q1
WHERE  Lessons = 2;
```

<div dir="rtl">

| RegPupil | Total |
|---|---|
| 201 | 600 |
| 204 | 740 |
| 207 | 670 |
| 210 | 620 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 10. 🟡 בעזרת Q1: שמות התלמידים שמשלמים פחות מ‑350, ממוינים לפי הסכום.

</div>

```sql
CREATE VIEW Q1 AS
SELECT   RegPupil, COUNT(*) AS Lessons, SUM(MonthlyFee) AS Total
FROM     Registrations
GROUP BY RegPupil;

SELECT FirstName, LastName, Total
FROM   Q1, Pupils
WHERE  RegPupil = PupilId AND Total < 350
ORDER BY Total;
```

<div dir="rtl">

| FirstName | LastName | Total |
|---|---|---|
| תמר | אברהם | 280 |
| כרים | עזאם | 300 |
| עומר | ביטון | 300 |
| רמי | חורי | 340 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 11. 🟡 צרו VIEW בשם `CityCount` — מספר התלמידים בכל עיר (`HomeTown`, `N`). הציגו את שם העיר עם הכי הרבה תלמידים.

</div>

```sql
CREATE VIEW CityCount AS
SELECT   HomeTown, COUNT(*) AS N
FROM     Pupils
GROUP BY HomeTown;

SELECT CityName, N
FROM   CityCount, Cities
WHERE  HomeTown = CityCode
  AND  N = (SELECT MAX(N) FROM CityCount);
```

<div dir="rtl">

| CityName | N |
|---|---|
| ירכא | 3 |
| עכו | 3 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 12. 🔴 צרו VIEW בשם `TeacherIncome` — לכל מורה (`RegTeacher`) סך התשלומים (`Income`). הציגו את המורים שההכנסה שלהם מעל הממוצע של ההכנסות.

</div>

```sql
CREATE VIEW TeacherIncome AS
SELECT   RegTeacher, SUM(MonthlyFee) AS Income
FROM     Registrations
GROUP BY RegTeacher;

SELECT TeacherName, Income
FROM   TeacherIncome, Teachers
WHERE  RegTeacher = TeacherCode
  AND  Income > (SELECT AVG(Income) FROM TeacherIncome);
```

<div dir="rtl">

| TeacherName | Income |
|---|---|
| סמיר חלבי | 940 |
| רונית לוי | 1160 |
| אמיר עזאם | 960 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 13. 🔴 בעזרת Q1: כמה תלמידים משלמים יותר מ‑500, וכמה — 500 או פחות? (קבצו לפי `CASE`)

</div>

```sql
CREATE VIEW Q1 AS
SELECT   RegPupil, COUNT(*) AS Lessons, SUM(MonthlyFee) AS Total
FROM     Registrations
GROUP BY RegPupil;

SELECT   CASE WHEN Total > 500 THEN 'מעל 500' ELSE '500 ומטה' END AS Range, COUNT(*) AS Pupils
FROM     Q1
GROUP BY Range;
```

<div dir="rtl">

| Range | Pupils |
|---|---|
| 500 ומטה | 6 |
| מעל 500 | 4 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

---

## 🎓 בסגנון הבחינה — ☕ בית הקפה "אל‑בלד"

</div>

<div dir="rtl">

### 1. 🟢 נתונה השאילתה השמורה Q1 (לכל עובד: מספר הזמנות וסך הסועדים). הציגו את כל Q1.

</div>

```sql
CREATE VIEW Q1 AS
SELECT   OrderWorker, COUNT(*) AS Orders, SUM(Guests) AS AllGuests
FROM     Orders
GROUP BY OrderWorker;

SELECT * FROM Q1;
```

<div dir="rtl">

| OrderWorker | Orders | AllGuests |
|---|---|---|
| 1 | 2 | 8 |
| 2 | 2 | 6 |
| 3 | 2 | 9 |
| 4 | 2 | 6 |
| 5 | 2 | 4 |
| 6 | 2 | 18 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 2. 🟡 בעזרת Q1: שם העובד ומספר ההזמנות שלו.

</div>

```sql
CREATE VIEW Q1 AS
SELECT   OrderWorker, COUNT(*) AS Orders, SUM(Guests) AS AllGuests
FROM     Orders
GROUP BY OrderWorker;

SELECT WorkerName, Orders
FROM   Q1, Workers
WHERE  OrderWorker = WorkerNum;
```

<div dir="rtl">

| WorkerName | Orders |
|---|---|
| סאלי חדאד | 2 |
| יובל נחום | 2 |
| אמיר טאהא | 2 |
| מיכל שרון | 2 |
| רים עבאס | 2 |
| תום בראל | 2 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 3. 🟡 בעזרת Q1: העובד ששירת הכי הרבה סועדים (שם).

</div>

```sql
CREATE VIEW Q1 AS
SELECT   OrderWorker, COUNT(*) AS Orders, SUM(Guests) AS AllGuests
FROM     Orders
GROUP BY OrderWorker;

SELECT WorkerName, AllGuests
FROM   Q1, Workers
WHERE  OrderWorker = WorkerNum
  AND  AllGuests = (SELECT MAX(AllGuests) FROM Q1);
```

<div dir="rtl">

| WorkerName | AllGuests |
|---|---|
| תום בראל | 18 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 4. 🟡 השלימו את הערך.

</div>

```sql
CREATE VIEW Q1 AS
SELECT   OrderWorker, COUNT(*) AS Orders, SUM(Guests) AS AllGuests
FROM     Orders
GROUP BY OrderWorker;

SELECT AVG(Orders) FROM Q1;
```

<div dir="rtl">

| AVG(Orders) |
|---|
| 2.0 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 5. 🔴 צרו שאילתה שמורה `DishCount` (לכל מנה כמה פעמים הוזמנה), והציגו את שמות המנות שהוזמנו יותר מפעם אחת.

</div>

```sql
CREATE VIEW DishCount AS
SELECT   OrderDish, COUNT(*) AS Times
FROM     Orders
GROUP BY OrderDish;

SELECT DishName, Times
FROM   DishCount, Dishes
WHERE  OrderDish = DishCode AND Times > 1;
```

<div dir="rtl">

| DishName | Times |
|---|---|
| שניצל | 4 |
| פסטה | 2 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 6. 🔴 השלימו את הפקודה שיוצרת את Q1.

</div>

```sql
CREATE VIEW Q1 AS
SELECT   OrderWorker, COUNT(*) AS Orders, SUM(Guests) AS AllGuests
FROM     Orders
GROUP BY OrderWorker;

SELECT * FROM Q1;
```

<div dir="rtl">

| OrderWorker | Orders | AllGuests |
|---|---|---|
| 1 | 2 | 8 |
| 2 | 2 | 6 |
| 3 | 2 | 9 |
| 4 | 2 | 6 |
| 5 | 2 | 4 |
| 6 | 2 | 18 |

**התוצאה: 6 שורות**

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

### 4. 🟢 צרו VIEW בשם `Girls` עם כל התלמידות, והציגו כמה יש.

</div>

```sql
CREATE VIEW Girls AS
SELECT * FROM Students WHERE Gender = 'F';

SELECT COUNT(*) AS Girls FROM Girls;
```

<div dir="rtl">

| Girls |
|---|
| 9 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 5. 🟡 צרו VIEW בשם `AbsCount` — מספר ההיעדרויות לכל תלמיד. הציגו שמות התלמידים עם 2 היעדרויות ומעלה.

</div>

```sql
CREATE VIEW AbsCount AS
SELECT   StudentId, COUNT(*) AS N
FROM     Absences
GROUP BY StudentId;

SELECT S.FirstName, S.LastName, V.N
FROM   AbsCount V, Students S
WHERE  V.StudentId = S.StudentId AND V.N >= 2;
```

<div dir="rtl">

| FirstName | LastName | N |
|---|---|---|
| יואב | כהן | 2 |
| כרים | חלבי | 3 |
| ג'וד | מנסור | 4 |
| איתי | גולן | 2 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 6. 🔴 צרו VIEW בשם `CourseAvg` — הממוצע של כל מקצוע במחצית 1. הציגו את שם המקצוע עם הממוצע הנמוך ביותר.

</div>

```sql
CREATE VIEW CourseAvg AS
SELECT   CourseCode, AVG(Grade) AS AvgGrade
FROM     Grades
WHERE    Term = 1
GROUP BY CourseCode;

SELECT C.CourseName, ROUND(V.AvgGrade, 1) AS AvgGrade
FROM   CourseAvg V, Courses C
WHERE  V.CourseCode = C.CourseCode
  AND  V.AvgGrade = (SELECT MIN(AvgGrade) FROM CourseAvg);
```

<div dir="rtl">

| CourseName | AvgGrade |
|---|---|
| מתמטיקה 3 יח"ל | 59.0 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../10-subqueries/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../12-insert-update-delete/solutions.md)

</div>
