<div dir="rtl">

# שיעור 7 — פתרונות

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../06-aggregates/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../08-joins/solutions.md)

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
SELECT   PupilLevel, COUNT(*)
FROM     Registrations
GROUP BY PupilLevel;
```

<div dir="rtl">

| PupilLevel | COUNT(*) |
|---|---|
| ממשיך | 6 |
| מתחיל | 5 |
| מתקדם | 3 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### שאלה 2

</div>

```sql
SELECT   RegPupil, COUNT(*)
FROM     Registrations
GROUP BY RegPupil
HAVING   COUNT(*) = 2;
```

<div dir="rtl">

| RegPupil | COUNT(*) |
|---|---|
| 201 | 2 |
| 204 | 2 |
| 207 | 2 |
| 210 | 2 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### שאלה 3

</div>

```sql
SELECT   TeachInst, MAX(HourRate)
FROM     Teachers
GROUP BY TeachInst;
```

<div dir="rtl">

| TeachInst | MAX(HourRate) |
|---|---|
| 10 | 150 |
| 20 | 110 |
| 30 | 140 |
| 40 | 100 |
| 60 | 120 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

---

## ✏️ תרגילים — 🎵 בית הספר למוזיקה "צלילים"

</div>

<div dir="rtl">

### 1. 🟢 כמה מורים מלמדים כל כלי (`TeachInst`)?

</div>

```sql
SELECT   TeachInst, COUNT(*) AS Teachers
FROM     Teachers
GROUP BY TeachInst;
```

<div dir="rtl">

| TeachInst | Teachers |
|---|---|
| 10 | 2 |
| 20 | 1 |
| 30 | 1 |
| 40 | 1 |
| 60 | 1 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 2. 🟢 כמה תלמידים נולדו בכל שנה?

</div>

```sql
SELECT   BirthYear, COUNT(*) AS Pupils
FROM     Pupils
GROUP BY BirthYear;
```

<div dir="rtl">

| BirthYear | Pupils |
|---|---|
| 2009 | 2 |
| 2010 | 2 |
| 2011 | 2 |
| 2012 | 2 |
| 2013 | 1 |
| 2014 | 1 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 3. 🟢 מה סכום התשלומים החודשיים בכל שנת רישום?

</div>

```sql
SELECT   RegYear, SUM(MonthlyFee) AS Total
FROM     Registrations
GROUP BY RegYear;
```

<div dir="rtl">

| RegYear | Total |
|---|---|
| 2021 | 340 |
| 2022 | 700 |
| 2023 | 660 |
| 2024 | 1240 |
| 2025 | 1690 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 4. 🟡 לכל תלמיד (`RegPupil`): בכמה שיעורים הוא רשום וכמה הוא משלם בסך הכול בחודש?

</div>

```sql
SELECT   RegPupil, COUNT(*) AS Lessons, SUM(MonthlyFee) AS Total
FROM     Registrations
GROUP BY RegPupil;
```

<div dir="rtl">

| RegPupil | Lessons | Total |
|---|---|---|
| 201 | 2 | 600 |
| 202 | 1 | 400 |
| 203 | 1 | 300 |
| 204 | 2 | 740 |
| 205 | 1 | 340 |
| 206 | 1 | 280 |
| 207 | 2 | 670 |
| 208 | 1 | 300 |
| 209 | 1 | 380 |
| 210 | 2 | 620 |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 5. 🟡 לכל רמה: התשלום הנמוך והגבוה ביותר.

</div>

```sql
SELECT   PupilLevel, MIN(MonthlyFee) AS MinFee, MAX(MonthlyFee) AS MaxFee
FROM     Registrations
GROUP BY PupilLevel;
```

<div dir="rtl">

| PupilLevel | MinFee | MaxFee |
|---|---|---|
| ממשיך | 280 | 360 |
| מתחיל | 280 | 380 |
| מתקדם | 300 | 400 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 6. 🟡 ערים (`HomeTown`) שגרים בהן **יותר מ‑2** תלמידים.

</div>

```sql
SELECT   HomeTown, COUNT(*) AS Pupils
FROM     Pupils
GROUP BY HomeTown
HAVING   COUNT(*) > 2;
```

<div dir="rtl">

| HomeTown | Pupils |
|---|---|
| 1 | 3 |
| 2 | 3 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 7. 🟡 תלמידים שמשלמים בסך הכול **יותר מ‑600** בחודש.

</div>

```sql
SELECT   RegPupil, SUM(MonthlyFee) AS Total
FROM     Registrations
GROUP BY RegPupil
HAVING   SUM(MonthlyFee) > 600;
```

<div dir="rtl">

| RegPupil | Total |
|---|---|
| 204 | 740 |
| 207 | 670 |
| 210 | 620 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 8. 🔴 מורים שהתשלום הממוצע אצלם **מעל 330**, ממוינים מהממוצע הגבוה לנמוך.

</div>

```sql
SELECT   RegTeacher, AVG(MonthlyFee) AS AvgFee
FROM     Registrations
GROUP BY RegTeacher
HAVING   AVG(MonthlyFee) > 330
ORDER BY AvgFee DESC;
```

<div dir="rtl">

| RegTeacher | AvgFee |
|---|---|
| 2 | 386.67 |
| 4 | 355.0 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 9. 🔴 רק ברישומים שאינם 'מתחיל': כמה רישומים יש לכל מורה? הציגו רק מורים עם 2 רישומים כאלה לפחות.

</div>

```sql
SELECT   RegTeacher, COUNT(*) AS Regs
FROM     Registrations
WHERE    PupilLevel <> 'מתחיל'
GROUP BY RegTeacher
HAVING   COUNT(*) >= 2;
```

<div dir="rtl">

| RegTeacher | Regs |
|---|---|
| 1 | 2 |
| 3 | 3 |
| 5 | 2 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 10. 🔴 לכל שנה ולכל רמה (קיבוץ לפי שתי עמודות): כמה רישומים? ממוין לפי שנה.

</div>

```sql
SELECT   RegYear, PupilLevel, COUNT(*) AS Regs
FROM     Registrations
GROUP BY RegYear, PupilLevel
ORDER BY RegYear;
```

<div dir="rtl">

| RegYear | PupilLevel | Regs |
|---|---|---|
| 2021 | מתקדם | 1 |
| 2022 | מתקדם | 2 |
| 2023 | ממשיך | 2 |
| 2024 | ממשיך | 4 |
| 2025 | מתחיל | 5 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

---

## 🏠 תרגול נוסף — 🏫 בית הספר "עתיד"

</div>

<div dir="rtl">

### 1. 🟢 כמה תלמידים יש בכל כיתה (`ClassCode`)?

</div>

```sql
SELECT   ClassCode, COUNT(*) AS Students
FROM     Students
GROUP BY ClassCode;
```

<div dir="rtl">

| ClassCode | Students |
|---|---|
| *NULL* | 1 |
| 101 | 4 |
| 102 | 3 |
| 103 | 3 |
| 104 | 3 |
| 105 | 4 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 2. 🟢 כמה מורים מלמדים כל מקצוע (`Subject`)?

</div>

```sql
SELECT   Subject, COUNT(*) AS Teachers
FROM     Teachers
GROUP BY Subject;
```

<div dir="rtl">

| Subject | Teachers |
|---|---|
| אנגלית | 1 |
| ביולוגיה | 1 |
| היסטוריה | 1 |
| מחשבים | 1 |
| מתמטיקה | 2 |
| ספורט | 1 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 3. 🟡 הציון הממוצע (מעוגל לספרה אחת) של כל תלמיד במחצית 1.

</div>

```sql
SELECT   StudentId, ROUND(AVG(Grade), 1) AS AvgGrade
FROM     Grades
WHERE    Term = 1
GROUP BY StudentId;
```

<div dir="rtl">

| StudentId | AvgGrade |
|---|---|
| 1001 | 84.7 |
| 1002 | 94.7 |
| 1003 | 62.0 |
| 1004 | 55.0 |
| 1005 | 82.7 |
| 1006 | 62.0 |
| 1007 | 91.7 |
| 1008 | 73.0 |
| 1009 | 58.5 |
| 1010 | 95.7 |
| 1011 | 79.3 |
| 1012 | 46.7 |
| 1013 | 92.0 |
| 1014 | 82.7 |
| 1015 | 64.7 |
| 1016 | 96.3 |
| 1017 | 69.0 |

**התוצאה: 17 שורות**

</div>

<div dir="rtl">

### 4. 🟡 תלמידים עם **3 היעדרויות או יותר**.

</div>

```sql
SELECT   StudentId, COUNT(*) AS Absences
FROM     Absences
GROUP BY StudentId
HAVING   COUNT(*) >= 3;
```

<div dir="rtl">

| StudentId | Absences |
|---|---|
| 1009 | 3 |
| 1012 | 4 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 5. 🔴 מקצועות (`CourseCode`) שהממוצע בהם במחצית 1 **מתחת ל‑75**.

</div>

```sql
SELECT   CourseCode, ROUND(AVG(Grade), 1) AS AvgGrade
FROM     Grades
WHERE    Term = 1
GROUP BY CourseCode
HAVING   AVG(Grade) < 75;
```

<div dir="rtl">

| CourseCode | AvgGrade |
|---|---|
| 12 | 74.9 |
| 16 | 59.0 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 6. 🔴 כמה בנים וכמה בנות יש בכל כיתה?

</div>

```sql
SELECT   ClassCode, Gender, COUNT(*) AS Students
FROM     Students
GROUP BY ClassCode, Gender
ORDER BY ClassCode;
```

<div dir="rtl">

| ClassCode | Gender | Students |
|---|---|---|
| *NULL* | F | 1 |
| 101 | F | 1 |
| 101 | M | 3 |
| 102 | F | 2 |
| 102 | M | 1 |
| 103 | F | 1 |
| 103 | M | 2 |
| 104 | F | 2 |
| 104 | M | 1 |
| 105 | F | 2 |
| 105 | M | 2 |

**התוצאה: 11 שורות**

</div>

<div dir="rtl">

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../06-aggregates/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../08-joins/solutions.md)

</div>
