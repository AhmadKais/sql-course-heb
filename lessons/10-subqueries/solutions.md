<div dir="rtl">

# שיעור 10 — פתרונות

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../09-joins-3-tables-left-join/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../11-views/solutions.md)

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
SELECT AVG(HourRate) FROM Teachers;
```

<div dir="rtl">

| AVG(HourRate) |
|---|
| 125.0 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### שאלה 2

</div>

```sql
SELECT FirstName
FROM   Pupils
WHERE  BirthYear = (SELECT MIN(BirthYear) FROM Pupils);
```

<div dir="rtl">

| FirstName |
|---|
| רמי |
| יואב |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### שאלה 3

</div>

```sql
SELECT COUNT(*)
FROM   Pupils
WHERE  PupilId NOT IN (SELECT LockerPupil FROM Lockers);
```

<div dir="rtl">

| COUNT(*) |
|---|
| 5 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

---

## ✏️ תרגילים — 🎵 בית הספר למוזיקה "צלילים"

</div>

<div dir="rtl">

### 1. 🟢 התלמידים שנולדו אחרי שנת הלידה הממוצעת.

</div>

```sql
SELECT FirstName, BirthYear
FROM   Pupils
WHERE  BirthYear > (SELECT AVG(BirthYear) FROM Pupils);
```

<div dir="rtl">

| FirstName | BirthYear |
|---|---|
| אדם | 2012 |
| כרים | 2013 |
| תמר | 2012 |
| סאלי | 2014 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 2. 🟢 המורה הזול ביותר.

</div>

```sql
SELECT TeacherName, HourRate
FROM   Teachers
WHERE  HourRate = (SELECT MIN(HourRate) FROM Teachers);
```

<div dir="rtl">

| TeacherName | HourRate |
|---|---|
| יוסי פרץ | 100 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 3. 🟢 רישומים שהתשלום בהם נמוך מהתשלום הממוצע.

</div>

```sql
SELECT RegPupil, RegTeacher, MonthlyFee
FROM   Registrations
WHERE  MonthlyFee < (SELECT AVG(MonthlyFee) FROM Registrations);
```

<div dir="rtl">

| RegPupil | RegTeacher | MonthlyFee |
|---|---|---|
| 201 | 1 | 320 |
| 201 | 5 | 280 |
| 203 | 1 | 300 |
| 206 | 5 | 280 |
| 207 | 1 | 320 |
| 208 | 3 | 300 |
| 210 | 5 | 300 |
| 210 | 3 | 320 |

**התוצאה: 8 שורות**

</div>

<div dir="rtl">

### 4. 🟡 תלמידים שיש להם לוקר (עם `IN`, בלי JOIN).

</div>

```sql
SELECT FirstName, LastName
FROM   Pupils
WHERE  PupilId IN (SELECT LockerPupil FROM Lockers);
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| אדם | חלבי |
| מאיה | כהן |
| רמי | חורי |
| ליאן | קבלאן |
| יואב | שושן |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 5. 🟡 תלמידים שאין להם לוקר.

</div>

```sql
SELECT FirstName, LastName
FROM   Pupils
WHERE  PupilId NOT IN (SELECT LockerPupil FROM Lockers);
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| כרים | עזאם |
| שירה | לוי |
| תמר | אברהם |
| עומר | ביטון |
| סאלי | חסון |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 6. 🟡 מורים שמלמדים לפחות תלמיד מתקדם אחד.

</div>

```sql
SELECT TeacherName
FROM   Teachers
WHERE  TeacherCode IN (SELECT RegTeacher
                       FROM   Registrations
                       WHERE  PupilLevel = 'מתקדם');
```

<div dir="rtl">

| TeacherName |
|---|
| רונית לוי |
| אמיר עזאם |
| יוסי פרץ |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 7. 🟡 תלמידים שגרים באותה עיר כמו 'מאיה'.

</div>

```sql
SELECT FirstName, LastName
FROM   Pupils
WHERE  HomeTown = (SELECT HomeTown FROM Pupils WHERE FirstName = 'מאיה');
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| מאיה | כהן |
| סאלי | חסון |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 8. 🔴 תלמידים שלומדים אצל מורה לפסנתר (3 רמות: תלמידים ← רישומים ← מורים ← כלים).

</div>

```sql
SELECT FirstName, LastName
FROM   Pupils
WHERE  PupilId IN (
         SELECT RegPupil FROM Registrations
         WHERE  RegTeacher IN (
                SELECT TeacherCode FROM Teachers
                WHERE  TeachInst = (SELECT InstCode FROM Instruments
                                    WHERE  InstName = 'פסנתר')));
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| מאיה | כהן |
| שירה | לוי |
| סאלי | חסון |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 9. 🔴 כלים שאף מורה לא מלמד (עם `NOT IN`).

</div>

```sql
SELECT InstName
FROM   Instruments
WHERE  InstCode NOT IN (SELECT TeachInst FROM Teachers);
```

<div dir="rtl">

| InstName |
|---|
| חליל |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 10. 🔴 תלמידים שמשלמים בסך הכול יותר מהתשלום של הרישום היקר ביותר של 2024.

</div>

```sql
SELECT   RegPupil, SUM(MonthlyFee) AS Total
FROM     Registrations
GROUP BY RegPupil
HAVING   SUM(MonthlyFee) > (SELECT MAX(MonthlyFee)
                            FROM   Registrations
                            WHERE  RegYear = 2024);
```

<div dir="rtl">

| RegPupil | Total |
|---|---|
| 201 | 600 |
| 202 | 400 |
| 204 | 740 |
| 205 | 340 |
| 207 | 670 |
| 209 | 380 |
| 210 | 620 |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

---

## 🏠 תרגול נוסף — 🏫 בית הספר "עתיד"

</div>

<div dir="rtl">

### 1. 🟢 מורים שמשתכרים יותר מהשכר הממוצע.

</div>

```sql
SELECT FirstName, LastName, Salary
FROM   Teachers
WHERE  Salary > (SELECT AVG(Salary) FROM Teachers);
```

<div dir="rtl">

| FirstName | LastName | Salary |
|---|---|---|
| נביל | סרחאן | 14500 |
| חוסאם | זיאד | 12800 |
| אורלי | שמש | 15300 |
| גלית | מזרחי | 13100 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 2. 🟡 תלמידים שלא נעדרו אף פעם (עם `NOT IN`).

</div>

```sql
SELECT FirstName, LastName
FROM   Students
WHERE  StudentId NOT IN (SELECT StudentId FROM Absences);
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| נור | עזאם |
| רוני | אברהם |
| עומר | ביטון |
| שירה | כהן |
| ליאור | לוי |
| דניאל | פרץ |
| הדיל | סעיד |
| ראניה | עבאס |
| נועם | שחר |

**התוצאה: 9 שורות**

</div>

<div dir="rtl">

### 3. 🟡 תלמידים שקיבלו לפחות ציון אחד מתחת ל‑50.

</div>

```sql
SELECT FirstName, LastName
FROM   Students
WHERE  StudentId IN (SELECT StudentId FROM Grades WHERE Grade < 50);
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| מאיה | לוי |
| ג'וד | מנסור |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 4. 🔴 מורים שאינם מחנכים של אף כיתה.

</div>

```sql
SELECT FirstName, LastName
FROM   Teachers
WHERE  TeacherCode NOT IN (SELECT TeacherCode FROM Classes);
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| פאדי | חדאד |
| סמיר | אבו-ראס |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 5. 🔴 התלמיד (או התלמידים) עם הציון הגבוה ביותר במקצוע 13.

</div>

```sql
SELECT FirstName, LastName
FROM   Students
WHERE  StudentId IN (SELECT StudentId FROM Grades
                     WHERE  CourseCode = 13
                       AND  Grade = (SELECT MAX(Grade) FROM Grades
                                     WHERE  CourseCode = 13));
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| ראניה | עבאס |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../09-joins-3-tables-left-join/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../11-views/solutions.md)

</div>
