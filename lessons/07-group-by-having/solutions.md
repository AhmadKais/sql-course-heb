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

### שאלה 4

</div>

```sql
SELECT   LockerFloor, COUNT(*)
FROM     Lockers
GROUP BY LockerFloor;
```

<div dir="rtl">

| LockerFloor | COUNT(*) |
|---|---|
| 1 | 2 |
| 2 | 3 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### שאלה 5

</div>

```sql
SELECT   RegYear, COUNT(*)
FROM     Registrations
GROUP BY RegYear
HAVING   COUNT(*) >= 4;
```

<div dir="rtl">

| RegYear | COUNT(*) |
|---|---|
| 2024 | 4 |
| 2025 | 5 |

**התוצאה: 2 שורות**

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

### 11. 🟢 כמה כלים יש בכל משפחת כלים?

</div>

```sql
SELECT   InstFamily, COUNT(*) AS Instruments
FROM     Instruments
GROUP BY InstFamily;
```

<div dir="rtl">

| InstFamily | Instruments |
|---|---|
| הקשה | 1 |
| מיתר | 3 |
| נשיפה | 1 |
| קלידים | 1 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 12. 🟢 כמה לוקרים יש בכל קומה?

</div>

```sql
SELECT   LockerFloor, COUNT(*) AS Lockers
FROM     Lockers
GROUP BY LockerFloor;
```

<div dir="rtl">

| LockerFloor | Lockers |
|---|---|
| 1 | 2 |
| 2 | 3 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 13. 🟡 לכל מורה: התשלום הגבוה ביותר שמשלמים לו.

</div>

```sql
SELECT   RegTeacher, MAX(MonthlyFee) AS MaxFee
FROM     Registrations
GROUP BY RegTeacher;
```

<div dir="rtl">

| RegTeacher | MaxFee |
|---|---|
| 1 | 320 |
| 2 | 400 |
| 3 | 340 |
| 4 | 360 |
| 5 | 300 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 14. 🟡 שנים שהיו בהן לפחות 3 רישומים.

</div>

```sql
SELECT   RegYear, COUNT(*) AS Regs
FROM     Registrations
GROUP BY RegYear
HAVING   COUNT(*) >= 3;
```

<div dir="rtl">

| RegYear | Regs |
|---|---|
| 2024 | 4 |
| 2025 | 5 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 15. 🟡 לכל עיר: שנת הלידה של התלמיד הצעיר ביותר.

</div>

```sql
SELECT   HomeTown, MAX(BirthYear) AS Youngest
FROM     Pupils
GROUP BY HomeTown;
```

<div dir="rtl">

| HomeTown | Youngest |
|---|---|
| 1 | 2013 |
| 2 | 2011 |
| 3 | 2014 |
| 4 | 2012 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 16. 🔴 כלים (`TeachInst`) שמלמדים אותם יותר ממורה אחד.

</div>

```sql
SELECT   TeachInst, COUNT(*) AS Teachers
FROM     Teachers
GROUP BY TeachInst
HAVING   COUNT(*) > 1;
```

<div dir="rtl">

| TeachInst | Teachers |
|---|---|
| 10 | 2 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 17. 🔴 לכל מורה — רק ברישומים מ‑2024 ואילך — סכום התשלומים. הציגו מורים עם סכום מעל 500, מהגבוה לנמוך.

</div>

```sql
SELECT   RegTeacher, SUM(MonthlyFee) AS Total
FROM     Registrations
WHERE    RegYear >= 2024
GROUP BY RegTeacher
HAVING   SUM(MonthlyFee) > 500
ORDER BY Total DESC;
```

<div dir="rtl">

| RegTeacher | Total |
|---|---|
| 1 | 940 |
| 2 | 760 |
| 5 | 560 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

---

## 🎓 בסגנון הבחינה — 🔧 מעבדת "דלתא‑טק"

</div>

<div dir="rtl">

### 1. 🟢 כמה תיקונים יש בכל רמת עדיפות?

</div>

```sql
SELECT   Priority, COUNT(*) AS Repairs
FROM     Repairs
GROUP BY Priority;
```

<div dir="rtl">

| Priority | Repairs |
|---|---|
| דחוף | 5 |
| מיידי | 3 |
| רגיל | 8 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 2. 🟢 לכל טכנאי (`RepairTech`): סך מחירי התיקונים שלו.

</div>

```sql
SELECT   RepairTech, SUM(RepairPrice) AS Total
FROM     Repairs
GROUP BY RepairTech;
```

<div dir="rtl">

| RepairTech | Total |
|---|---|
| 1 | 1340 |
| 2 | 920 |
| 3 | 3330 |
| 4 | 1010 |
| 5 | 2240 |
| 6 | 350 |
| 7 | 740 |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 3. 🟡 סוגי מכשירים (`RepairDev`) שתוקנו 3 פעמים או יותר.

</div>

```sql
SELECT   RepairDev, COUNT(*) AS Repairs
FROM     Repairs
GROUP BY RepairDev
HAVING   COUNT(*) >= 3;
```

<div dir="rtl">

| RepairDev | Repairs |
|---|---|
| 10 | 5 |
| 20 | 4 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 4. 🟡 לכל עיר (`TechCity`): מספר הטכנאים והשכר הממוצע לשעה.

</div>

```sql
SELECT   TechCity, COUNT(*) AS Techs, AVG(HourWage) AS AvgWage
FROM     Technicians
GROUP BY TechCity;
```

<div dir="rtl">

| TechCity | Techs | AvgWage |
|---|---|---|
| 1 | 3 | 90.67 |
| 2 | 1 | 80.0 |
| 4 | 1 | 80.0 |
| 5 | 1 | 88.0 |
| 6 | 1 | 65.0 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 5. 🟡 השלימו את הערכים בטבלה שתתקבל.

</div>

```sql
SELECT   BenchFloor, COUNT(*)
FROM     Benches
GROUP BY BenchFloor;
```

<div dir="rtl">

| BenchFloor | COUNT(*) |
|---|---|
| 1 | 2 |
| 2 | 3 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 6. 🔴

</div>

```sql
SELECT   RepairTech, COUNT(*) AS N
FROM     Repairs
WHERE    DoneDate IS NULL
GROUP BY RepairTech;
```

<div dir="rtl">

| RepairTech | N |
|---|---|
| 1 | 1 |
| 3 | 1 |
| 4 | 1 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 7. 🔴 השלימו כך שיוצגו הטכנאים שהמחיר הממוצע של התיקונים שלהם מעל 600.

</div>

```sql
SELECT   RepairTech, AVG(RepairPrice)
FROM     Repairs
GROUP BY RepairTech
HAVING   AVG(RepairPrice) > 600;
```

<div dir="rtl">

| RepairTech | AVG(RepairPrice) |
|---|---|
| 3 | 1110.0 |
| 5 | 1120.0 |

**התוצאה: 2 שורות**

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

### 7. 🟢 כמה כיתות יש בכל שכבה?

</div>

```sql
SELECT   Grade, COUNT(*) AS Classes
FROM     Classes
GROUP BY Grade;
```

<div dir="rtl">

| Grade | Classes |
|---|---|
| 10 | 2 |
| 11 | 2 |
| 12 | 1 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 8. 🟡 לכל עיר (`CityCode`): כמה תלמידים, רק ערים עם 3 תלמידים ומעלה.

</div>

```sql
SELECT   CityCode, COUNT(*) AS Students
FROM     Students
GROUP BY CityCode
HAVING   COUNT(*) >= 3;
```

<div dir="rtl">

| CityCode | Students |
|---|---|
| 1 | 3 |
| 2 | 3 |
| 4 | 4 |
| 6 | 3 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 9. 🟡 לכל מחצית: מספר הציונים והציון הממוצע (מעוגל).

</div>

```sql
SELECT   Term, COUNT(Grade) AS Grades, ROUND(AVG(Grade), 1) AS AvgGrade
FROM     Grades
GROUP BY Term;
```

<div dir="rtl">

| Term | Grades | AvgGrade |
|---|---|---|
| 1 | 50 | 77.7 |
| 2 | 8 | 79.8 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 10. 🔴 תלמידים שהציון הנמוך ביותר שלהם במחצית 1 הוא מתחת ל‑55.

</div>

```sql
SELECT   StudentId, MIN(Grade) AS Lowest
FROM     Grades
WHERE    Term = 1
GROUP BY StudentId
HAVING   MIN(Grade) < 55;
```

<div dir="rtl">

| StudentId | Lowest |
|---|---|
| 1004 | 48 |
| 1009 | 54 |
| 1012 | 42 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../06-aggregates/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../08-joins/solutions.md)

</div>
