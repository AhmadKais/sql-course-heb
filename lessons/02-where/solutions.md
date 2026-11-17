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

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../01-select/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../03-between-in-like-null/solutions.md)

</div>
