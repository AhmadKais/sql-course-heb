<div dir="rtl">

# שיעור 1 — פתרונות

[⬅️ חזרה לשיעור](README.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../02-where/solutions.md)

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
SELECT FirstName, BirthYear
FROM   Pupils;
```

<div dir="rtl">

| FirstName | BirthYear |
|---|---|
| אדם | 2012 |
| מאיה | 2010 |
| כרים | 2013 |
| שירה | 2011 |
| רמי | 2009 |
| תמר | 2012 |
| ליאן | 2011 |
| עומר | 2010 |
| סאלי | 2014 |
| יואב | 2009 |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### שאלה 2

</div>

```sql
SELECT DISTINCT TeachInst
FROM   Teachers;
```

<div dir="rtl">

| TeachInst |
|---|
| 60 |
| 10 |
| 20 |
| 30 |
| 40 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### שאלה 3

</div>

```sql
SELECT DISTINCT RegYear, PupilLevel
FROM   Registrations;
```

<div dir="rtl">

| RegYear | PupilLevel |
|---|---|
| 2024 | ממשיך |
| 2025 | מתחיל |
| 2022 | מתקדם |
| 2023 | ממשיך |
| 2021 | מתקדם |

**התוצאה: 5 שורות**

> 💡 `DISTINCT` בודק את **הצירוף** של שתי העמודות.

</div>

<div dir="rtl">

---

## ✏️ תרגילים — 🎵 בית הספר למוזיקה "צלילים"

</div>

<div dir="rtl">

### 1. 🟢 הציגו את השם הפרטי ושם המשפחה של כל התלמידים.

</div>

```sql
SELECT FirstName, LastName
FROM   Pupils;
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| אדם | חלבי |
| מאיה | כהן |
| כרים | עזאם |
| שירה | לוי |
| רמי | חורי |
| תמר | אברהם |
| ליאן | קבלאן |
| עומר | ביטון |
| סאלי | חסון |
| יואב | שושן |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 2. 🟢 הציגו את כל העמודות של טבלת הכלים (`Instruments`).

</div>

```sql
SELECT *
FROM   Instruments;
```

<div dir="rtl">

| InstCode | InstName | InstFamily |
|---|---|---|
| 10 | פסנתר | קלידים |
| 20 | גיטרה | מיתר |
| 30 | כינור | מיתר |
| 40 | תופים | הקשה |
| 50 | חליל | נשיפה |
| 60 | עוד | מיתר |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 3. 🟢 הציגו את שם המורה ואת הטלפון שלו.

</div>

```sql
SELECT TeacherName, TeacherPhone
FROM   Teachers;
```

<div dir="rtl">

| TeacherName | TeacherPhone |
|---|---|
| סמיר חלבי | 050-1234567 |
| רונית לוי | 052-2345678 |
| אמיר עזאם | *NULL* |
| דנה כהן | 054-4567890 |
| יוסי פרץ | 053-5678901 |
| נור מנסור | *NULL* |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 4. 🟢 הציגו את שם המשפחה ואחריו השם הפרטי (בסדר הזה) של התלמידים.

</div>

```sql
SELECT LastName, FirstName
FROM   Pupils;
```

<div dir="rtl">

| LastName | FirstName |
|---|---|
| חלבי | אדם |
| כהן | מאיה |
| עזאם | כרים |
| לוי | שירה |
| חורי | רמי |
| אברהם | תמר |
| קבלאן | ליאן |
| ביטון | עומר |
| חסון | סאלי |
| שושן | יואב |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 5. 🟡 הציגו את קוד התלמיד ואת שנת הלידה, בשמות `Code` ו‑`Born`.

</div>

```sql
SELECT PupilId AS Code, BirthYear AS Born
FROM   Pupils;
```

<div dir="rtl">

| Code | Born |
|---|---|
| 201 | 2012 |
| 202 | 2010 |
| 203 | 2013 |
| 204 | 2011 |
| 205 | 2009 |
| 206 | 2012 |
| 207 | 2011 |
| 208 | 2010 |
| 209 | 2014 |
| 210 | 2009 |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 6. 🟡 הציגו לכל רישום את קוד התלמיד ואת התשלום השנתי (12 חודשים) בשם `YearFee`.

</div>

```sql
SELECT RegPupil, MonthlyFee * 12 AS YearFee
FROM   Registrations;
```

<div dir="rtl">

| RegPupil | YearFee |
|---|---|
| 201 | 3840 |
| 201 | 3360 |
| 202 | 4800 |
| 203 | 3600 |
| 204 | 4320 |
| 204 | 4560 |
| 205 | 4080 |
| 206 | 3360 |
| 207 | 4200 |
| 207 | 3840 |
| 208 | 3600 |
| 209 | 4560 |
| 210 | 3600 |
| 210 | 3840 |

**התוצאה: 14 שורות**

</div>

<div dir="rtl">

### 7. 🟡 הציגו לכל תלמיד את שמו הפרטי ואת גילו בשנת 2026, בשם `Age`.

</div>

```sql
SELECT FirstName, 2026 - BirthYear AS Age
FROM   Pupils;
```

<div dir="rtl">

| FirstName | Age |
|---|---|
| אדם | 14 |
| מאיה | 16 |
| כרים | 13 |
| שירה | 15 |
| רמי | 17 |
| תמר | 14 |
| ליאן | 15 |
| עומר | 16 |
| סאלי | 12 |
| יואב | 17 |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 8. 🟡 אילו משפחות כלים (`InstFamily`) יש בבית הספר? כל משפחה פעם אחת.

</div>

```sql
SELECT DISTINCT InstFamily
FROM   Instruments;
```

<div dir="rtl">

| InstFamily |
|---|
| קלידים |
| מיתר |
| הקשה |
| נשיפה |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 9. 🟡 אילו רמות (`PupilLevel`) קיימות ברישומים? כל רמה פעם אחת.

</div>

```sql
SELECT DISTINCT PupilLevel
FROM   Registrations;
```

<div dir="rtl">

| PupilLevel |
|---|
| ממשיך |
| מתחיל |
| מתקדם |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 10. 🔴 הציגו את שם המורה ואת המחיר לשעה אחרי העלאה של 10%, בשם `NewRate`.

</div>

```sql
SELECT TeacherName, ROUND(HourRate * 1.1, 2) AS NewRate
FROM   Teachers;
```

<div dir="rtl">

| TeacherName | NewRate |
|---|---|
| סמיר חלבי | 132.0 |
| רונית לוי | 165.0 |
| אמיר עזאם | 121.0 |
| דנה כהן | 154.0 |
| יוסי פרץ | 110.0 |
| נור מנסור | 143.0 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 11. 🔴 הציגו את השם המלא של כל תלמיד בעמודה אחת בשם `FullName` (רמז: `||` מחבר טקסטים).

</div>

```sql
SELECT FirstName || ' ' || LastName AS FullName
FROM   Pupils;
```

<div dir="rtl">

| FullName |
|---|
| אדם חלבי |
| מאיה כהן |
| כרים עזאם |
| שירה לוי |
| רמי חורי |
| תמר אברהם |
| ליאן קבלאן |
| עומר ביטון |
| סאלי חסון |
| יואב שושן |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 12. 🔴 באילו קומות יש לוקרים? כל קומה פעם אחת.

</div>

```sql
SELECT DISTINCT LockerFloor
FROM   Lockers;
```

<div dir="rtl">

| LockerFloor |
|---|
| 1 |
| 2 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

---

## 🏠 תרגול נוסף — 🏫 בית הספר "עתיד"

</div>

<div dir="rtl">

### 1. 🟢 הציגו את השם הפרטי, שם המשפחה והמקצוע של כל המורים.

</div>

```sql
SELECT FirstName, LastName, Subject
FROM   Teachers;
```

<div dir="rtl">

| FirstName | LastName | Subject |
|---|---|---|
| נביל | סרחאן | מתמטיקה |
| רונית | בר-לב | אנגלית |
| חוסאם | זיאד | מחשבים |
| אורלי | שמש | היסטוריה |
| פאדי | חדאד | ספורט |
| גלית | מזרחי | מתמטיקה |
| סמיר | אבו-ראס | ביולוגיה |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 2. 🟢 הציגו את כל העמודות של טבלת המקצועות (`Courses`).

</div>

```sql
SELECT *
FROM   Courses;
```

<div dir="rtl">

| CourseCode | CourseName | TeacherCode | WeeklyHours |
|---|---|---|---|
| 11 | מתמטיקה 5 יח"ל | 1 | 5 |
| 12 | אנגלית 4 יח"ל | 2 | 4 |
| 13 | מבוא לבסיסי נתונים | 3 | 3 |
| 14 | היסטוריה | 4 | 2 |
| 15 | חינוך גופני | 5 | 2 |
| 16 | מתמטיקה 3 יח"ל | 6 | 3 |
| 17 | סדנת פרויקטים | *NULL* | 2 |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 3. 🟡 הציגו לכל מורה את שמו הפרטי ואת השכר השנתי (12 משכורות), בשם `YearSalary`.

</div>

```sql
SELECT FirstName, Salary * 12 AS YearSalary
FROM   Teachers;
```

<div dir="rtl">

| FirstName | YearSalary |
|---|---|
| נביל | 174000 |
| רונית | 134400 |
| חוסאם | 153600 |
| אורלי | 183600 |
| פאדי | 117600 |
| גלית | 157200 |
| סמיר | 124800 |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 4. 🟡 אילו מקצועות מלמדים המורים? כל מקצוע פעם אחת.

</div>

```sql
SELECT DISTINCT Subject
FROM   Teachers;
```

<div dir="rtl">

| Subject |
|---|
| מתמטיקה |
| אנגלית |
| מחשבים |
| היסטוריה |
| ספורט |
| ביולוגיה |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 5. 🔴 הציגו לכל מקצוע את שמו ואת מספר השעות בשנה (40 שבועות), בשם `YearHours`.

</div>

```sql
SELECT CourseName, WeeklyHours * 40 AS YearHours
FROM   Courses;
```

<div dir="rtl">

| CourseName | YearHours |
|---|---|
| מתמטיקה 5 יח"ל | 200 |
| אנגלית 4 יח"ל | 160 |
| מבוא לבסיסי נתונים | 120 |
| היסטוריה | 80 |
| חינוך גופני | 80 |
| מתמטיקה 3 יח"ל | 120 |
| סדנת פרויקטים | 80 |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

---

[⬅️ חזרה לשיעור](README.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../02-where/solutions.md)

</div>
