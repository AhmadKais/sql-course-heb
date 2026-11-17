<div dir="rtl">

# שיעור 2 — פתרונות

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../01-select/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../03-between-in-like-null/solutions.md)

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
WHERE  HourRate <> 150;
```

<div dir="rtl">

| TeacherName |
|---|
| סמיר חלבי |
| אמיר עזאם |
| דנה כהן |
| יוסי פרץ |
| נור מנסור |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### שאלה 2

</div>

```sql
SELECT RegPupil
FROM   Registrations
WHERE  RegTeacher = 1 OR RegTeacher = 5 AND PupilLevel = 'ממשיך';
```

<div dir="rtl">

| RegPupil |
|---|
| 201 |
| 203 |
| 206 |
| 207 |

**התוצאה: 4 שורות**

> 💡 `AND` מחושב קודם, ולכן נכנסים **כל** הרישומים של מורה 1.

</div>

<div dir="rtl">

### שאלה 3

</div>

```sql
SELECT FirstName
FROM   Pupils
WHERE  NOT HomeTown = 1;
```

<div dir="rtl">

| FirstName |
|---|
| מאיה |
| שירה |
| רמי |
| תמר |
| עומר |
| סאלי |
| יואב |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### שאלה 4

</div>

```sql
SELECT InstName
FROM   Instruments
WHERE  InstFamily <> 'מיתר';
```

<div dir="rtl">

| InstName |
|---|
| פסנתר |
| תופים |
| חליל |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### שאלה 5

</div>

```sql
SELECT COUNT(*)
FROM   Registrations
WHERE  RegYear >= 2024 AND MonthlyFee < 300;
```

<div dir="rtl">

| COUNT(*) |
|---|
| 2 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

---

## ✏️ תרגילים — 🎵 בית הספר למוזיקה "צלילים"

</div>

<div dir="rtl">

### 1. 🟢 הציגו את שמות התלמידים שנולדו בשנת 2012.

</div>

```sql
SELECT FirstName, LastName
FROM   Pupils
WHERE  BirthYear = 2012;
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| אדם | חלבי |
| תמר | אברהם |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 2. 🟢 הציגו את שם המורה ואת המחיר של מורים שהמחיר שלהם קטן מ‑120.

</div>

```sql
SELECT TeacherName, HourRate
FROM   Teachers
WHERE  HourRate < 120;
```

<div dir="rtl">

| TeacherName | HourRate |
|---|---|
| אמיר עזאם | 110 |
| יוסי פרץ | 100 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 3. 🟢 הציגו את כל הרישומים של המורה שהקוד שלו 2.

</div>

```sql
SELECT *
FROM   Registrations
WHERE  RegTeacher = 2;
```

<div dir="rtl">

| RegPupil | RegTeacher | RegYear | PupilLevel | MonthlyFee |
|---|---|---|---|---|
| 202 | 2 | 2022 | מתקדם | 400 |
| 204 | 2 | 2025 | מתחיל | 380 |
| 209 | 2 | 2025 | מתחיל | 380 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 4. 🟢 הציגו את התלמידים שגרים בעיר 3.

</div>

```sql
SELECT FirstName, LastName
FROM   Pupils
WHERE  HomeTown = 3;
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| מאיה | כהן |
| סאלי | חסון |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 5. 🟢 הציגו את הכלים ממשפחת 'מיתר'.

</div>

```sql
SELECT InstName
FROM   Instruments
WHERE  InstFamily = 'מיתר';
```

<div dir="rtl">

| InstName |
|---|
| גיטרה |
| כינור |
| עוד |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 6. 🟡 הציגו רישומים שאינם ברמת 'מתחיל'.

</div>

```sql
SELECT RegPupil, PupilLevel
FROM   Registrations
WHERE  PupilLevel <> 'מתחיל';
```

<div dir="rtl">

| RegPupil | PupilLevel |
|---|---|
| 201 | ממשיך |
| 202 | מתקדם |
| 204 | ממשיך |
| 205 | מתקדם |
| 206 | ממשיך |
| 207 | ממשיך |
| 208 | ממשיך |
| 210 | מתקדם |
| 210 | ממשיך |

**התוצאה: 9 שורות**

</div>

<div dir="rtl">

### 7. 🟡 הציגו תלמידים שנולדו לפני 2011 וגרים בעיר 2.

</div>

```sql
SELECT FirstName, BirthYear, HomeTown
FROM   Pupils
WHERE  BirthYear < 2011 AND HomeTown = 2;
```

<div dir="rtl">

| FirstName | BirthYear | HomeTown |
|---|---|---|
| רמי | 2009 | 2 |
| יואב | 2009 | 2 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 8. 🟡 הציגו רישומים מהשנים 2022 או 2023.

</div>

```sql
SELECT RegPupil, RegYear
FROM   Registrations
WHERE  RegYear = 2022 OR RegYear = 2023;
```

<div dir="rtl">

| RegPupil | RegYear |
|---|---|
| 202 | 2022 |
| 204 | 2023 |
| 208 | 2023 |
| 210 | 2022 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 9. 🟡 הציגו מורים שמלמדים פסנתר (כלי 10) והמחיר שלהם מעל 140.

</div>

```sql
SELECT TeacherName, HourRate
FROM   Teachers
WHERE  TeachInst = 10 AND HourRate > 140;
```

<div dir="rtl">

| TeacherName | HourRate |
|---|---|
| רונית לוי | 150 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 10. 🔴 הציגו רישומים ברמת 'מתקדם' או 'ממשיך', שהתשלום בהם נמוך מ‑330.

</div>

```sql
SELECT RegPupil, PupilLevel, MonthlyFee
FROM   Registrations
WHERE  (PupilLevel = 'מתקדם' OR PupilLevel = 'ממשיך')
  AND  MonthlyFee < 330;
```

<div dir="rtl">

| RegPupil | PupilLevel | MonthlyFee |
|---|---|---|
| 201 | ממשיך | 320 |
| 206 | ממשיך | 280 |
| 207 | ממשיך | 320 |
| 208 | ממשיך | 300 |
| 210 | מתקדם | 300 |
| 210 | ממשיך | 320 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 11. 🔴 הציגו תלמידים שגרים בעיר 1 או בעיר 4, ונולדו בשנת 2012 ואילך.

</div>

```sql
SELECT FirstName, BirthYear, HomeTown
FROM   Pupils
WHERE  (HomeTown = 1 OR HomeTown = 4)
  AND  BirthYear >= 2012;
```

<div dir="rtl">

| FirstName | BirthYear | HomeTown |
|---|---|---|
| אדם | 2012 | 1 |
| כרים | 2013 | 1 |
| תמר | 2012 | 4 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 12. 🔴 הציגו את שם המורה ואת המחיר ל‑3 שעות, רק למורים שהמחיר ל‑3 שעות גבוה מ‑400.

</div>

```sql
SELECT TeacherName, HourRate * 3 AS ThreeHours
FROM   Teachers
WHERE  HourRate * 3 > 400;
```

<div dir="rtl">

| TeacherName | ThreeHours |
|---|---|
| רונית לוי | 450 |
| דנה כהן | 420 |

**התוצאה: 2 שורות**

> 💡 ב‑`WHERE` חוזרים על החישוב — אי אפשר להשתמש שם בכינוי `ThreeHours`.

</div>

<div dir="rtl">

### 13. 🟢 הציגו את הלוקרים שבקומה 1.

</div>

```sql
SELECT LockerNum, LockerPupil
FROM   Lockers
WHERE  LockerFloor = 1;
```

<div dir="rtl">

| LockerNum | LockerPupil |
|---|---|
| 1 | 202 |
| 2 | 205 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 14. 🟢 הציגו את המורים שמחירם בדיוק 130.

</div>

```sql
SELECT TeacherName
FROM   Teachers
WHERE  HourRate = 130;
```

<div dir="rtl">

| TeacherName |
|---|
| נור מנסור |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 15. 🟡 הציגו רישומים משנת 2024 ואילך שאינם ברמת 'ממשיך'.

</div>

```sql
SELECT RegPupil, RegYear, PupilLevel
FROM   Registrations
WHERE  RegYear >= 2024 AND PupilLevel <> 'ממשיך';
```

<div dir="rtl">

| RegPupil | RegYear | PupilLevel |
|---|---|---|
| 201 | 2025 | מתחיל |
| 203 | 2025 | מתחיל |
| 204 | 2025 | מתחיל |
| 207 | 2025 | מתחיל |
| 209 | 2025 | מתחיל |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 16. 🟡 הציגו תלמידים שנולדו ב‑2009 או ב‑2014.

</div>

```sql
SELECT FirstName, BirthYear
FROM   Pupils
WHERE  BirthYear = 2009 OR BirthYear = 2014;
```

<div dir="rtl">

| FirstName | BirthYear |
|---|---|
| רמי | 2009 |
| סאלי | 2014 |
| יואב | 2009 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 17. 🟡 הציגו את המורים שאינם מלמדים את כלי 10 (עם `NOT`).

</div>

```sql
SELECT TeacherName, TeachInst
FROM   Teachers
WHERE  NOT TeachInst = 10;
```

<div dir="rtl">

| TeacherName | TeachInst |
|---|---|
| סמיר חלבי | 60 |
| אמיר עזאם | 20 |
| דנה כהן | 30 |
| יוסי פרץ | 40 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 18. 🔴 הציגו רישומים של המורה 3 או 4, משנת 2023 בלבד.

</div>

```sql
SELECT RegPupil, RegTeacher, RegYear
FROM   Registrations
WHERE  (RegTeacher = 3 OR RegTeacher = 4) AND RegYear = 2023;
```

<div dir="rtl">

| RegPupil | RegTeacher | RegYear |
|---|---|---|
| 204 | 4 | 2023 |
| 208 | 3 | 2023 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 19. 🔴 הציגו רישומים שהתשלום השנתי בהם (12 חודשים) גבוה מ‑4,000.

</div>

```sql
SELECT RegPupil, MonthlyFee * 12 AS YearFee
FROM   Registrations
WHERE  MonthlyFee * 12 > 4000;
```

<div dir="rtl">

| RegPupil | YearFee |
|---|---|
| 202 | 4800 |
| 204 | 4320 |
| 204 | 4560 |
| 205 | 4080 |
| 207 | 4200 |
| 209 | 4560 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

---

## 🎓 בסגנון הבחינה — ☕ בית הקפה "אל‑בלד"

</div>

<div dir="rtl">

### 1. 🟢 הציגו את שמות המנות שמחירן גבוה מ‑30.

</div>

```sql
SELECT DishName, DishPrice
FROM   Dishes
WHERE  DishPrice > 30;
```

<div dir="rtl">

| DishName | DishPrice |
|---|---|
| סלט ירקות | 32 |
| שניצל | 56 |
| פסטה | 48 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 2. 🟢 הציגו את ההזמנות של המנה 30.

</div>

```sql
SELECT OrderNum, CustName
FROM   Orders
WHERE  OrderDish = 30;
```

<div dir="rtl">

| OrderNum | CustName |
|---|---|
| 101 | דנה לוי |
| 104 | סמיר דיב |
| 107 | יעל שגיא |
| 111 | ואיל נסאר |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 3. 🟡 הציגו את העובדים מהעיר 1 או 2 ששכרם לשעה לפחות 42.

</div>

```sql
SELECT WorkerName, HourPay
FROM   Workers
WHERE  (WorkerCity = 1 OR WorkerCity = 2) AND HourPay >= 42;
```

<div dir="rtl">

| WorkerName | HourPay |
|---|---|
| סאלי חדאד | 42 |
| אמיר טאהא | 50 |
| רים עבאס | 55 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 4. 🟡 הציגו את ההזמנות אחרי 1 במאי 2026 שהיו בהן יותר מ‑3 סועדים.

</div>

```sql
SELECT OrderNum, OrderDate, Guests
FROM   Orders
WHERE  OrderDate > '2026-05-01' AND Guests > 3;
```

<div dir="rtl">

| OrderNum | OrderDate | Guests |
|---|---|---|
| 108 | 2026-05-30 | 8 |
| 110 | 2026-06-28 | 4 |
| 112 | 2026-07-21 | 10 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 5. 🟡

</div>

```sql
SELECT DishName
FROM   Dishes
WHERE  DishKind = 'קינוח';
```

<div dir="rtl">

| DishName |
|---|
| קנאפה |
| עוגת גבינה |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 6. 🟡 כמה שורות יחזרו?

</div>

```sql
SELECT WorkerName
FROM   Workers
WHERE  HourPay <> 38;
```

<div dir="rtl">

| WorkerName |
|---|
| סאלי חדאד |
| אמיר טאהא |
| מיכל שרון |
| רים עבאס |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 7. 🔴 השלימו כך שיוצגו המנות העיקריות שמחירן נמוך מ‑50.

</div>

```sql
SELECT DishName
FROM   Dishes
WHERE  DishKind = 'מנה עיקרית' AND DishPrice < 50;
```

<div dir="rtl">

| DishName |
|---|
| פסטה |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

---

## 🏠 תרגול נוסף — 🏫 בית הספר "עתיד"

</div>

<div dir="rtl">

### 1. 🟢 הציגו מורים שמלמדים 'מתמטיקה'.

</div>

```sql
SELECT FirstName, LastName
FROM   Teachers
WHERE  Subject = 'מתמטיקה';
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| נביל | סרחאן |
| גלית | מזרחי |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 2. 🟢 הציגו את שם התלמיד ואת קוד העיר של תלמידות (`Gender = 'F'`).

</div>

```sql
SELECT FirstName, CityCode
FROM   Students
WHERE  Gender = 'F';
```

<div dir="rtl">

| FirstName | CityCode |
|---|---|
| נור | 1 |
| מאיה | 4 |
| סאלי | 2 |
| שירה | 4 |
| תמר | 5 |
| ג'וד | 6 |
| הדיל | 6 |
| ראניה | 6 |
| לינא | 2 |

**התוצאה: 9 שורות**

</div>

<div dir="rtl">

### 3. 🟡 הציגו ציונים מתחת ל‑60 במחצית 1.

</div>

```sql
SELECT StudentId, CourseCode, Grade
FROM   Grades
WHERE  Grade < 60 AND Term = 1;
```

<div dir="rtl">

| StudentId | CourseCode | Grade |
|---|---|---|
| 1003 | 12 | 55 |
| 1004 | 16 | 48 |
| 1006 | 12 | 58 |
| 1009 | 16 | 54 |
| 1012 | 16 | 42 |
| 1012 | 13 | 51 |
| 1012 | 12 | 47 |
| 1015 | 16 | 59 |

**התוצאה: 8 שורות**

</div>

<div dir="rtl">

### 4. 🟡 הציגו מורים שהתחילו לעבוד לפני 2015 (`HireDate < '2015-01-01'`).

</div>

```sql
SELECT FirstName, HireDate
FROM   Teachers
WHERE  HireDate < '2015-01-01';
```

<div dir="rtl">

| FirstName | HireDate |
|---|---|
| נביל | 2012-09-01 |
| אורלי | 2009-09-01 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 5. 🔴 הציגו מורים למתמטיקה או לאנגלית שמשתכרים יותר מ‑12,000.

</div>

```sql
SELECT FirstName, Subject, Salary
FROM   Teachers
WHERE  (Subject = 'מתמטיקה' OR Subject = 'אנגלית')
  AND  Salary > 12000;
```

<div dir="rtl">

| FirstName | Subject | Salary |
|---|---|---|
| נביל | מתמטיקה | 14500 |
| גלית | מתמטיקה | 13100 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 6. 🔴 הציגו היעדרויות לא מאושרות (`Excused = 0`) מחודש ספטמבר אחרי ה‑10 בו.

</div>

```sql
SELECT StudentId, AbsenceDate
FROM   Absences
WHERE  Excused = 0 AND AbsenceDate > '2026-09-10';
```

<div dir="rtl">

| StudentId | AbsenceDate |
|---|---|
| 1012 | 2026-09-15 |
| 1012 | 2026-09-16 |
| 1015 | 2026-09-17 |
| 1018 | 2026-09-15 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 7. 🟢 הציגו את הכיתות של שכבה 11.

</div>

```sql
SELECT ClassName
FROM   Classes
WHERE  Grade = 11;
```

<div dir="rtl">

| ClassName |
|---|
| יא1 |
| יא2 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 8. 🟢 הציגו מקצועות שנלמדים יותר מ‑3 שעות בשבוע.

</div>

```sql
SELECT CourseName, WeeklyHours
FROM   Courses
WHERE  WeeklyHours > 3;
```

<div dir="rtl">

| CourseName | WeeklyHours |
|---|---|
| מתמטיקה 5 יח"ל | 5 |
| אנגלית 4 יח"ל | 4 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 9. 🟡 הציגו את הציונים של התלמיד 1007 במחצית 2.

</div>

```sql
SELECT CourseCode, Grade
FROM   Grades
WHERE  StudentId = 1007 AND Term = 2;
```

<div dir="rtl">

| CourseCode | Grade |
|---|---|
| 11 | 90 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 10. 🔴 הציגו תלמידים מהעיר 4 או 6 שנרשמו לפני 2026.

</div>

```sql
SELECT FirstName, CityCode, EnrollDate
FROM   Students
WHERE  (CityCode = 4 OR CityCode = 6) AND EnrollDate < '2026-01-01';
```

<div dir="rtl">

| FirstName | CityCode | EnrollDate |
|---|---|---|
| שירה | 4 | 2025-09-01 |
| ג'וד | 6 | 2025-09-01 |
| הדיל | 6 | 2024-09-01 |
| איתי | 4 | 2024-09-01 |
| ראניה | 6 | 2024-09-01 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../01-select/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../03-between-in-like-null/solutions.md)

</div>
