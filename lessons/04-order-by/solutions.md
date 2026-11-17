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

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../03-between-in-like-null/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../05-row-functions/solutions.md)

</div>
