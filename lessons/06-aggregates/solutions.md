<div dir="rtl">

# שיעור 6 — פתרונות

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../05-row-functions/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../07-group-by-having/solutions.md)

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
SELECT COUNT(*), COUNT(TeacherPhone), COUNT(DISTINCT TeachInst)
FROM   Teachers;
```

<div dir="rtl">

| COUNT(*) | COUNT(TeacherPhone) | COUNT(DISTINCT TeachInst) |
|---|---|---|
| 6 | 4 | 5 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### שאלה 2

</div>

```sql
SELECT COUNT(*)
FROM   Registrations
WHERE  RegTeacher = 3;
```

<div dir="rtl">

| COUNT(*) |
|---|
| 3 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### שאלה 3

</div>

```sql
SELECT MAX(BirthYear) - MIN(BirthYear) AS Diff
FROM   Pupils;
```

<div dir="rtl">

| Diff |
|---|
| 5 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### שאלה 4

</div>

```sql
SELECT COUNT(DISTINCT HomeTown), COUNT(*)
FROM   Pupils;
```

<div dir="rtl">

| COUNT(DISTINCT HomeTown) | COUNT(*) |
|---|---|
| 4 | 10 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### שאלה 5

</div>

```sql
SELECT SUM(MonthlyFee)
FROM   Registrations
WHERE  RegPupil = 204;
```

<div dir="rtl">

| SUM(MonthlyFee) |
|---|
| 740 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

---

## ✏️ תרגילים — 🎵 בית הספר למוזיקה "צלילים"

</div>

<div dir="rtl">

### 1. 🟢 כמה תלמידים יש בבית הספר?

</div>

```sql
SELECT COUNT(*) AS Pupils
FROM   Pupils;
```

<div dir="rtl">

| Pupils |
|---|
| 10 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 2. 🟢 מה התשלום החודשי הגבוה ביותר ברישומים?

</div>

```sql
SELECT MAX(MonthlyFee) AS MaxFee
FROM   Registrations;
```

<div dir="rtl">

| MaxFee |
|---|
| 400 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 3. 🟢 מה שנת הלידה של התלמיד המבוגר ביותר?

</div>

```sql
SELECT MIN(BirthYear) AS Oldest
FROM   Pupils;
```

<div dir="rtl">

| Oldest |
|---|
| 2009 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 4. 🟢 מה הסכום של כל התשלומים החודשיים?

</div>

```sql
SELECT SUM(MonthlyFee) AS Total
FROM   Registrations;
```

<div dir="rtl">

| Total |
|---|
| 4630 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 5. 🟡 כמה מורים **אין** להם טלפון? (שתי דרכים: עם `WHERE ... IS NULL`, או `COUNT(*) - COUNT(TeacherPhone)`)

</div>

```sql
SELECT COUNT(*) AS NoPhone
FROM   Teachers
WHERE  TeacherPhone IS NULL;
```

<div dir="rtl">

| NoPhone |
|---|
| 2 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 6. 🟡 מה התשלום הממוצע של תלמידים מתחילים? עגלו ל‑2 ספרות.

</div>

```sql
SELECT ROUND(AVG(MonthlyFee), 2) AS AvgBeginner
FROM   Registrations
WHERE  PupilLevel = 'מתחיל';
```

<div dir="rtl">

| AvgBeginner |
|---|
| 338.0 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 7. 🟡 כמה תלמידים **שונים** רשומים לשיעורים? (תלמיד יכול להופיע פעמיים ברישומים)

</div>

```sql
SELECT COUNT(DISTINCT RegPupil) AS RegisteredPupils
FROM   Registrations;
```

<div dir="rtl">

| RegisteredPupils |
|---|
| 10 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 8. 🟡 כמה רישומים יש למורה 5, ומה סכום התשלומים שלהם?

</div>

```sql
SELECT COUNT(*) AS Regs, SUM(MonthlyFee) AS Total
FROM   Registrations
WHERE  RegTeacher = 5;
```

<div dir="rtl">

| Regs | Total |
|---|---|
| 3 | 860 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 9. 🔴 מה ההפרש בין המחיר היקר ביותר לזול ביותר לשעה?

</div>

```sql
SELECT MAX(HourRate) - MIN(HourRate) AS Gap
FROM   Teachers;
```

<div dir="rtl">

| Gap |
|---|
| 50 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 10. 🔴 כמה תלמידים נולדו בין 2010 ל‑2012, ומה שנת הלידה הממוצעת שלהם?

</div>

```sql
SELECT COUNT(*) AS Pupils, AVG(BirthYear) AS AvgYear
FROM   Pupils
WHERE  BirthYear BETWEEN 2010 AND 2012;
```

<div dir="rtl">

| Pupils | AvgYear |
|---|---|
| 6 | 2011.0 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 11. 🔴 מה ההכנסה השנתית הכוללת (12 חודשים) מכל הרישומים?

</div>

```sql
SELECT SUM(MonthlyFee * 12) AS YearIncome
FROM   Registrations;
```

<div dir="rtl">

| YearIncome |
|---|
| 55560 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 12. 🟢 כמה כלים יש בטבלת הכלים?

</div>

```sql
SELECT COUNT(*) AS Instruments
FROM   Instruments;
```

<div dir="rtl">

| Instruments |
|---|
| 6 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 13. 🟢 מה המחיר לשעה הנמוך ביותר?

</div>

```sql
SELECT MIN(HourRate) AS MinRate
FROM   Teachers;
```

<div dir="rtl">

| MinRate |
|---|
| 100 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 14. 🟡 כמה תלמידים גרים בעיר 1?

</div>

```sql
SELECT COUNT(*) AS Pupils
FROM   Pupils
WHERE  HomeTown = 1;
```

<div dir="rtl">

| Pupils |
|---|
| 3 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 15. 🟡 מה התשלום הממוצע ברישומים של שנת 2025?

</div>

```sql
SELECT AVG(MonthlyFee) AS AvgFee
FROM   Registrations
WHERE  RegYear = 2025;
```

<div dir="rtl">

| AvgFee |
|---|
| 338.0 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 16. 🟡 כמה לוקרים יש בקומה 2?

</div>

```sql
SELECT COUNT(*) AS Lockers
FROM   Lockers
WHERE  LockerFloor = 2;
```

<div dir="rtl">

| Lockers |
|---|
| 3 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 17. 🔴 כמה מורים מלמדים כלי ממשפחת 'מיתר'? (רמז: `TeachInst IN (20, 30, 60)`)

</div>

```sql
SELECT COUNT(*) AS StringTeachers
FROM   Teachers
WHERE  TeachInst IN (20, 30, 60);
```

<div dir="rtl">

| StringTeachers |
|---|
| 3 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 18. 🔴 מה סכום התשלומים, הממוצע (מעוגל) ומספר הרישומים של התלמידים המתקדמים — בשאילתה אחת?

</div>

```sql
SELECT SUM(MonthlyFee) AS Total, ROUND(AVG(MonthlyFee)) AS AvgFee, COUNT(*) AS Regs
FROM   Registrations
WHERE  PupilLevel = 'מתקדם';
```

<div dir="rtl">

| Total | AvgFee | Regs |
|---|---|---|
| 1040 | 347.0 | 3 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

---

## 🎓 בסגנון הבחינה — 🎮 חנות משחקי מחשב

</div>

<div dir="rtl">

### 1. 🟢 כמה משחקים יש בחנות?

</div>

```sql
SELECT COUNT(*) AS Games
FROM   Games;
```

<div dir="rtl">

| Games |
|---|
| 10 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 2. 🟢 מה המחיר לשעה הגבוה ביותר?

</div>

```sql
SELECT MAX(PricePerHour) AS MaxPrice
FROM   Games;
```

<div dir="rtl">

| MaxPrice |
|---|
| 10.0 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 3. 🟡 כמה משתמשים רשמו אימייל? (בלי `WHERE`)

</div>

```sql
SELECT COUNT(Email) AS WithEmail
FROM   Users;
```

<div dir="rtl">

| WithEmail |
|---|
| 5 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 4. 🟡 כמה שעות הוזמנו בסך הכול בספטמבר 2025?

</div>

```sql
SELECT SUM(Hours) AS TotalHours
FROM   Orders
WHERE  OrderDate BETWEEN '2025-09-01' AND '2025-09-30';
```

<div dir="rtl">

| TotalHours |
|---|
| 25 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 5. 🟡 השלימו את שלושת הערכים.

</div>

```sql
SELECT COUNT(*), COUNT(MakerCode), COUNT(DISTINCT MakerCode)
FROM   Games;
```

<div dir="rtl">

| COUNT(*) | COUNT(MakerCode) | COUNT(DISTINCT MakerCode) |
|---|---|---|
| 10 | 9 | 4 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 6. 🟡

</div>

```sql
SELECT MIN(GameYear) AS Oldest, MAX(GameYear) AS Newest
FROM   Games;
```

<div dir="rtl">

| Oldest | Newest |
|---|---|
| 1984 | 2023 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 7. 🔴 השלימו כך שיוצג המחיר הממוצע לשעה של משחקי הספורט (קטגוריה 2), מעוגל לספרה אחת.

</div>

```sql
SELECT ROUND(AVG(PricePerHour), 1) AS AvgPrice
FROM   Games
WHERE  TypeCode = 2;
```

<div dir="rtl">

| AvgPrice |
|---|
| 7.0 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

---

## 🏠 תרגול נוסף — 🏫 בית הספר "עתיד"

</div>

<div dir="rtl">

### 1. 🟢 כמה תלמידים יש, וכמה מהם רשמו טלפון?

</div>

```sql
SELECT COUNT(*) AS AllStudents, COUNT(Phone) AS WithPhone
FROM   Students;
```

<div dir="rtl">

| AllStudents | WithPhone |
|---|---|
| 18 | 12 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 2. 🟢 מה השכר הממוצע של המורים?

</div>

```sql
SELECT AVG(Salary) AS AvgSalary
FROM   Teachers;
```

<div dir="rtl">

| AvgSalary |
|---|
| 12442.9 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 3. 🟡 מה הציון הגבוה, הנמוך והממוצע (מעוגל) במקצוע 11, מחצית 1?

</div>

```sql
SELECT MAX(Grade) AS Hi, MIN(Grade) AS Lo, ROUND(AVG(Grade), 1) AS Avg
FROM   Grades
WHERE  CourseCode = 11 AND Term = 1;
```

<div dir="rtl">

| Hi | Lo | Avg |
|---|---|---|
| 100 | 65 | 85.3 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 4. 🟡 כמה היעדרויות לא מאושרות יש?

</div>

```sql
SELECT COUNT(*) AS NotExcused
FROM   Absences
WHERE  Excused = 0;
```

<div dir="rtl">

| NotExcused |
|---|
| 9 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 5. 🔴 בכמה מקצועות שונים יש ציונים בטבלת הציונים?

</div>

```sql
SELECT COUNT(DISTINCT CourseCode) AS Courses
FROM   Grades;
```

<div dir="rtl">

| Courses |
|---|
| 7 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 6. 🔴 כמה ציונים חסרים (NULL) יש בטבלת הציונים? כתבו עם `COUNT(*) - COUNT(Grade)`.

</div>

```sql
SELECT COUNT(*) - COUNT(Grade) AS Missing
FROM   Grades;
```

<div dir="rtl">

| Missing |
|---|
| 2 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 7. 🟢 כמה כיתות יש?

</div>

```sql
SELECT COUNT(*) AS Classes
FROM   Classes;
```

<div dir="rtl">

| Classes |
|---|
| 5 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 8. 🟢 מה השכר הגבוה ביותר של מורה?

</div>

```sql
SELECT MAX(Salary) AS MaxSalary
FROM   Teachers;
```

<div dir="rtl">

| MaxSalary |
|---|
| 15300 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 9. 🟡 כמה שעות שבועיות יש בסך הכול בכל המקצועות?

</div>

```sql
SELECT SUM(WeeklyHours) AS Hours
FROM   Courses;
```

<div dir="rtl">

| Hours |
|---|
| 21 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 10. 🔴 מה תאריך ההיעדרות הראשון והאחרון בטבלה?

</div>

```sql
SELECT MIN(AbsenceDate) AS First, MAX(AbsenceDate) AS Last
FROM   Absences;
```

<div dir="rtl">

| First | Last |
|---|---|
| 2026-09-02 | 2026-09-18 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../05-row-functions/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../07-group-by-having/solutions.md)

</div>
