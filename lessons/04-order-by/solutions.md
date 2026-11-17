<div dir="rtl">

# שיעור 4 — פתרונות

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../03-between-in-like-null/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../05-row-functions/solutions.md)

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
SELECT TeacherName
FROM   Teachers
ORDER BY HourRate
LIMIT  1;
```

<div dir="rtl">

| TeacherName |
|---|
| יוסי פרץ |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### שאלה 2

</div>

```sql
SELECT FirstName, BirthYear
FROM   Pupils
WHERE  HomeTown = 2
ORDER BY BirthYear DESC;
```

<div dir="rtl">

| FirstName | BirthYear |
|---|---|
| שירה | 2011 |
| רמי | 2009 |
| יואב | 2009 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### שאלה 3

</div>

```sql
SELECT InstName
FROM   Instruments
ORDER BY InstCode DESC
LIMIT  2;
```

<div dir="rtl">

| InstName |
|---|
| עוד |
| חליל |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### שאלה 4

</div>

```sql
SELECT RegPupil, MonthlyFee
FROM   Registrations
WHERE  RegTeacher = 1
ORDER BY MonthlyFee;
```

<div dir="rtl">

| RegPupil | MonthlyFee |
|---|---|
| 203 | 300 |
| 201 | 320 |
| 207 | 320 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

---

## ✏️ תרגילים — 🎵 בית הספר למוזיקה "צלילים"

</div>

<div dir="rtl">

### 1. 🟢 הציגו את התלמידים לפי שנת הלידה, מהמבוגר לצעיר.

</div>

```sql
SELECT FirstName, BirthYear
FROM   Pupils
ORDER BY BirthYear;
```

<div dir="rtl">

| FirstName | BirthYear |
|---|---|
| רמי | 2009 |
| יואב | 2009 |
| מאיה | 2010 |
| עומר | 2010 |
| שירה | 2011 |
| ליאן | 2011 |
| אדם | 2012 |
| תמר | 2012 |
| כרים | 2013 |
| סאלי | 2014 |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 2. 🟢 הציגו את הכלים לפי שם הכלי (א–ת).

</div>

```sql
SELECT InstName
FROM   Instruments
ORDER BY InstName;
```

<div dir="rtl">

| InstName |
|---|
| גיטרה |
| חליל |
| כינור |
| עוד |
| פסנתר |
| תופים |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 3. 🟢 הציגו את המורים לפי המחיר, מהזול ליקר.

</div>

```sql
SELECT TeacherName, HourRate
FROM   Teachers
ORDER BY HourRate ASC;
```

<div dir="rtl">

| TeacherName | HourRate |
|---|---|
| יוסי פרץ | 100 |
| אמיר עזאם | 110 |
| סמיר חלבי | 120 |
| נור מנסור | 130 |
| דנה כהן | 140 |
| רונית לוי | 150 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 4. 🟡 הציגו את הרישומים של שנת 2025, מהתשלום הגבוה לנמוך.

</div>

```sql
SELECT RegPupil, MonthlyFee
FROM   Registrations
WHERE  RegYear = 2025
ORDER BY MonthlyFee DESC;
```

<div dir="rtl">

| RegPupil | MonthlyFee |
|---|---|
| 204 | 380 |
| 209 | 380 |
| 207 | 350 |
| 203 | 300 |
| 201 | 280 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 5. 🟡 הציגו את התלמידים לפי עיר, ובתוך כל עיר — לפי שם פרטי.

</div>

```sql
SELECT HomeTown, FirstName
FROM   Pupils
ORDER BY HomeTown, FirstName;
```

<div dir="rtl">

| HomeTown | FirstName |
|---|---|
| 1 | אדם |
| 1 | כרים |
| 1 | ליאן |
| 2 | יואב |
| 2 | רמי |
| 2 | שירה |
| 3 | מאיה |
| 3 | סאלי |
| 4 | עומר |
| 4 | תמר |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 6. 🟡 הציגו את 2 המורים הזולים ביותר.

</div>

```sql
SELECT TeacherName, HourRate
FROM   Teachers
ORDER BY HourRate
LIMIT  2;
```

<div dir="rtl">

| TeacherName | HourRate |
|---|---|
| יוסי פרץ | 100 |
| אמיר עזאם | 110 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 7. 🟡 הציגו את התלמיד הצעיר ביותר.

</div>

```sql
SELECT FirstName, BirthYear
FROM   Pupils
ORDER BY BirthYear DESC
LIMIT  1;
```

<div dir="rtl">

| FirstName | BirthYear |
|---|---|
| סאלי | 2014 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 8. 🔴 הציגו את שם המורה ואת המחיר ל‑4 שעות (`FourHours`), ממוין לפי `FourHours` מהגבוה לנמוך.

</div>

```sql
SELECT TeacherName, HourRate * 4 AS FourHours
FROM   Teachers
ORDER BY FourHours DESC;
```

<div dir="rtl">

| TeacherName | FourHours |
|---|---|
| רונית לוי | 600 |
| דנה כהן | 560 |
| נור מנסור | 520 |
| סמיר חלבי | 480 |
| אמיר עזאם | 440 |
| יוסי פרץ | 400 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 9. 🔴 הציגו את הרישומים ברמת 'ממשיך' או 'מתקדם', ממוינים לפי רמה ואז לפי תשלום יורד.

</div>

```sql
SELECT PupilLevel, MonthlyFee, RegPupil
FROM   Registrations
WHERE  PupilLevel IN ('ממשיך', 'מתקדם')
ORDER BY PupilLevel, MonthlyFee DESC;
```

<div dir="rtl">

| PupilLevel | MonthlyFee | RegPupil |
|---|---|---|
| ממשיך | 360 | 204 |
| ממשיך | 320 | 201 |
| ממשיך | 320 | 207 |
| ממשיך | 320 | 210 |
| ממשיך | 300 | 208 |
| ממשיך | 280 | 206 |
| מתקדם | 400 | 202 |
| מתקדם | 340 | 205 |
| מתקדם | 300 | 210 |

**התוצאה: 9 שורות**

</div>

<div dir="rtl">

### 10. 🔴 הציגו את 3 הרישומים העדכניים ביותר (לפי שנה), ובתיקו — הזולים קודם.

</div>

```sql
SELECT RegPupil, RegYear, MonthlyFee
FROM   Registrations
ORDER BY RegYear DESC, MonthlyFee ASC
LIMIT  3;
```

<div dir="rtl">

| RegPupil | RegYear | MonthlyFee |
|---|---|---|
| 201 | 2025 | 280 |
| 203 | 2025 | 300 |
| 207 | 2025 | 350 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 11. 🟢 הציגו את הערים לפי שם העיר (א–ת).

</div>

```sql
SELECT CityName
FROM   Cities
ORDER BY CityName;
```

<div dir="rtl">

| CityName |
|---|
| ירכא |
| כרמיאל |
| מעלות |
| נהריה |
| עכו |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 12. 🟢 הציגו את הלוקרים לפי קומה (יורד).

</div>

```sql
SELECT LockerNum, LockerFloor
FROM   Lockers
ORDER BY LockerFloor DESC;
```

<div dir="rtl">

| LockerNum | LockerFloor |
|---|---|
| 3 | 2 |
| 4 | 2 |
| 5 | 2 |
| 1 | 1 |
| 2 | 1 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 13. 🟡 הציגו את התלמידים מעיר 1, מהצעיר למבוגר.

</div>

```sql
SELECT FirstName, BirthYear
FROM   Pupils
WHERE  HomeTown = 1
ORDER BY BirthYear DESC;
```

<div dir="rtl">

| FirstName | BirthYear |
|---|---|
| כרים | 2013 |
| אדם | 2012 |
| ליאן | 2011 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 14. 🟡 הציגו את 3 הרישומים הזולים ביותר.

</div>

```sql
SELECT RegPupil, RegTeacher, MonthlyFee
FROM   Registrations
ORDER BY MonthlyFee
LIMIT  3;
```

<div dir="rtl">

| RegPupil | RegTeacher | MonthlyFee |
|---|---|---|
| 201 | 5 | 280 |
| 206 | 5 | 280 |
| 203 | 1 | 300 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 15. 🟡 הציגו את המורים לפי כלי (`TeachInst`), ובתוך כל כלי מהיקר לזול.

</div>

```sql
SELECT TeachInst, TeacherName, HourRate
FROM   Teachers
ORDER BY TeachInst, HourRate DESC;
```

<div dir="rtl">

| TeachInst | TeacherName | HourRate |
|---|---|---|
| 10 | רונית לוי | 150 |
| 10 | נור מנסור | 130 |
| 20 | אמיר עזאם | 110 |
| 30 | דנה כהן | 140 |
| 40 | יוסי פרץ | 100 |
| 60 | סמיר חלבי | 120 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 16. 🔴 הציגו את המורה השני הכי יקר (רמז: `LIMIT 1 OFFSET 1`).

</div>

```sql
SELECT TeacherName, HourRate
FROM   Teachers
ORDER BY HourRate DESC
LIMIT  1 OFFSET 1;
```

<div dir="rtl">

| TeacherName | HourRate |
|---|---|
| דנה כהן | 140 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 17. 🔴 הציגו את 4 התלמידים הראשונים לפי שם משפחה, ובתיקו לפי שם פרטי.

</div>

```sql
SELECT LastName, FirstName
FROM   Pupils
ORDER BY LastName, FirstName
LIMIT  4;
```

<div dir="rtl">

| LastName | FirstName |
|---|---|
| אברהם | תמר |
| ביטון | עומר |
| חורי | רמי |
| חלבי | אדם |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

---

## 🎓 בסגנון הבחינה — 🔧 מעבדת "דלתא‑טק"

</div>

<div dir="rtl">

### 1. 🟢 הציגו את הטכנאים לפי השכר לשעה, מהגבוה לנמוך.

</div>

```sql
SELECT TechFirst, TechLast, HourWage
FROM   Technicians
ORDER BY HourWage DESC;
```

<div dir="rtl">

| TechFirst | TechLast | HourWage |
|---|---|---|
| סאמר | חלבי | 105 |
| נביל | סרחאן | 95 |
| חוסאם | זיאד | 88 |
| רונית | בר-לב | 80 |
| ליאן | קבלאן | 80 |
| דנה | כהן | 72 |
| מאיה | אברהם | 65 |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 2. 🟢 הציגו את החלפים לפי שם החלף (א–ת).

</div>

```sql
SELECT PartName, PartPrice
FROM   Parts
ORDER BY PartName;
```

<div dir="rtl">

| PartName | PartPrice |
|---|---|
| כבל שטוח | 45 |
| מסך | 450 |
| מצלמה | 160 |
| מקלדת | 220 |
| סוללה | 180 |
| רמקול | 70 |
| שקע טעינה | 90 |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 3. 🟡 הציגו את התיקונים הדחופים, מהיקר לזול.

</div>

```sql
SELECT RepairNum, CustName, RepairPrice
FROM   Repairs
WHERE  Priority = 'דחוף'
ORDER BY RepairPrice DESC;
```

<div dir="rtl">

| RepairNum | CustName | RepairPrice |
|---|---|---|
| 1012 | אלון כהן | 1480 |
| 1008 | עומר ביטון | 1250 |
| 1016 | אורי שמש | 1100 |
| 1002 | מאיה כהן | 980 |
| 1004 | שירה לוי | 540 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 4. 🟡 הציגו את 3 התיקונים הראשונים שהתקבלו במעבדה.

</div>

```sql
SELECT RepairNum, CustName, InDate
FROM   Repairs
ORDER BY InDate
LIMIT  3;
```

<div dir="rtl">

| RepairNum | CustName | InDate |
|---|---|---|
| 1001 | אדם חלבי | 2026-01-12 |
| 1002 | מאיה כהן | 2026-01-20 |
| 1003 | כרים עזאם | 2026-02-03 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 5. 🟡

</div>

```sql
SELECT TechFirst, StartDate
FROM   Technicians
ORDER BY StartDate
LIMIT  2;
```

<div dir="rtl">

| TechFirst | StartDate |
|---|---|
| סאמר | 2018-11-20 |
| נביל | 2019-03-01 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 6. 🟡 מה יהיה בשורה הראשונה?

</div>

```sql
SELECT CustName, RepairPrice
FROM   Repairs
WHERE  RepairDev = 10
ORDER BY RepairPrice;
```

<div dir="rtl">

| CustName | RepairPrice |
|---|---|
| סלים דיאב | 290 |
| כרים עזאם | 310 |
| יואב שושן | 380 |
| אדם חלבי | 420 |
| ליאן קבלאן | 450 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 7. 🔴 השלימו כך שיוצגו התיקונים לפי עדיפות, ובתוך כל עדיפות מהיקר לזול.

</div>

```sql
SELECT Priority, RepairPrice, CustName
FROM   Repairs
ORDER BY Priority, RepairPrice DESC;
```

<div dir="rtl">

| Priority | RepairPrice | CustName |
|---|---|---|
| דחוף | 1480 | אלון כהן |
| דחוף | 1250 | עומר ביטון |
| דחוף | 1100 | אורי שמש |
| דחוף | 980 | מאיה כהן |
| דחוף | 540 | שירה לוי |
| מיידי | 380 | יואב שושן |
| מיידי | 230 | מוחמד דיב |
| מיידי | 190 | תמר אברהם |
| רגיל | 820 | הילה פרץ |
| רגיל | 760 | רמי חורי |
| רגיל | 610 | נור מנסור |
| רגיל | 450 | ליאן קבלאן |
| רגיל | 420 | אדם חלבי |
| רגיל | 310 | כרים עזאם |
| רגיל | 290 | סלים דיאב |
| רגיל | 120 | סאלי חסון |

**התוצאה: 16 שורות**

</div>

<div dir="rtl">

---

## 🏠 תרגול נוסף — 🏫 בית הספר "עתיד"

</div>

<div dir="rtl">

### 1. 🟢 הציגו את המורים לפי השכר, מהגבוה לנמוך.

</div>

```sql
SELECT FirstName, LastName, Salary
FROM   Teachers
ORDER BY Salary DESC;
```

<div dir="rtl">

| FirstName | LastName | Salary |
|---|---|---|
| אורלי | שמש | 15300 |
| נביל | סרחאן | 14500 |
| גלית | מזרחי | 13100 |
| חוסאם | זיאד | 12800 |
| רונית | בר-לב | 11200 |
| סמיר | אבו-ראס | 10400 |
| פאדי | חדאד | 9800 |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 2. 🟡 הציגו את 5 הציונים הגבוהים ביותר במחצית 1.

</div>

```sql
SELECT StudentId, CourseCode, Grade
FROM   Grades
WHERE  Term = 1
ORDER BY Grade DESC
LIMIT  5;
```

<div dir="rtl">

| StudentId | CourseCode | Grade |
|---|---|---|
| 1002 | 15 | 100 |
| 1010 | 11 | 100 |
| 1016 | 13 | 99 |
| 1013 | 17 | 98 |
| 1016 | 11 | 98 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 3. 🟡 הציגו את התלמידים לפי כיתה, ובתוך כיתה לפי שם משפחה.

</div>

```sql
SELECT ClassCode, LastName, FirstName
FROM   Students
ORDER BY ClassCode, LastName;
```

<div dir="rtl">

| ClassCode | LastName | FirstName |
|---|---|---|
| *NULL* | חמוד | לינא |
| 101 | חלבי | אדם |
| 101 | כהן | יואב |
| 101 | עזאם | נור |
| 101 | שחר | נועם |
| 102 | אברהם | רוני |
| 102 | חסון | סאלי |
| 102 | לוי | מאיה |
| 103 | ביטון | עומר |
| 103 | חלבי | כרים |
| 103 | כהן | שירה |
| 104 | לוי | ליאור |
| 104 | מנסור | ג'וד |
| 104 | שושן | תמר |
| 105 | גולן | איתי |
| 105 | סעיד | הדיל |
| 105 | עבאס | ראניה |
| 105 | פרץ | דניאל |

**התוצאה: 18 שורות**

</div>

<div dir="rtl">

### 4. 🔴 הציגו את המורה הוותיק ביותר (תאריך קליטה מוקדם ביותר).

</div>

```sql
SELECT FirstName, LastName, HireDate
FROM   Teachers
ORDER BY HireDate
LIMIT  1;
```

<div dir="rtl">

| FirstName | LastName | HireDate |
|---|---|---|
| אורלי | שמש | 2009-09-01 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 5. 🟢 הציגו את המקצועות לפי מספר השעות השבועיות, מהגבוה לנמוך.

</div>

```sql
SELECT CourseName, WeeklyHours
FROM   Courses
ORDER BY WeeklyHours DESC;
```

<div dir="rtl">

| CourseName | WeeklyHours |
|---|---|
| מתמטיקה 5 יח"ל | 5 |
| אנגלית 4 יח"ל | 4 |
| מבוא לבסיסי נתונים | 3 |
| מתמטיקה 3 יח"ל | 3 |
| היסטוריה | 2 |
| חינוך גופני | 2 |
| סדנת פרויקטים | 2 |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 6. 🟡 הציגו את ההיעדרויות לפי תאריך, מהאחרונה לראשונה.

</div>

```sql
SELECT StudentId, AbsenceDate
FROM   Absences
ORDER BY AbsenceDate DESC;
```

<div dir="rtl">

| StudentId | AbsenceDate |
|---|---|
| 1001 | 2026-09-18 |
| 1015 | 2026-09-17 |
| 1012 | 2026-09-16 |
| 1012 | 2026-09-15 |
| 1018 | 2026-09-15 |
| 1009 | 2026-09-14 |
| 1006 | 2026-09-11 |
| 1012 | 2026-09-10 |
| 1009 | 2026-09-09 |
| 1009 | 2026-09-08 |
| 1010 | 2026-09-08 |
| 1004 | 2026-09-07 |
| 1015 | 2026-09-04 |
| 1003 | 2026-09-03 |
| 1003 | 2026-09-02 |
| 1012 | 2026-09-02 |

**התוצאה: 16 שורות**

</div>

<div dir="rtl">

### 7. 🟡 הציגו את 3 התלמידים הצעירים ביותר (לפי תאריך לידה).

</div>

```sql
SELECT FirstName, BirthDate
FROM   Students
WHERE  BirthDate IS NOT NULL
ORDER BY BirthDate DESC
LIMIT  3;
```

<div dir="rtl">

| FirstName | BirthDate |
|---|---|
| מאיה | 2011-11-30 |
| נועם | 2011-09-02 |
| נור | 2011-07-22 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 8. 🔴 הציגו את הציונים של מקצוע 11, לפי מחצית ובתוך המחצית מהגבוה לנמוך.

</div>

```sql
SELECT Term, StudentId, Grade
FROM   Grades
WHERE  CourseCode = 11
ORDER BY Term, Grade DESC;
```

<div dir="rtl">

| Term | StudentId | Grade |
|---|---|---|
| 1 | 1010 | 100 |
| 1 | 1016 | 98 |
| 1 | 1002 | 95 |
| 1 | 1007 | 93 |
| 1 | 1013 | 89 |
| 1 | 1001 | 88 |
| 1 | 1005 | 77 |
| 1 | 1014 | 76 |
| 1 | 1008 | 72 |
| 1 | 1017 | 65 |
| 2 | 1016 | 100 |
| 2 | 1010 | 97 |
| 2 | 1013 | 92 |
| 2 | 1001 | 91 |
| 2 | 1007 | 90 |

**התוצאה: 15 שורות**

</div>

<div dir="rtl">

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../03-between-in-like-null/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../05-row-functions/solutions.md)

</div>
