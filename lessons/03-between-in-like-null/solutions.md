<div dir="rtl">

# שיעור 3 — פתרונות

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../02-where/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../04-order-by/solutions.md)

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
WHERE  TeacherPhone = NULL;
```

<div dir="rtl">

| TeacherName |
|---|

**התוצאה: 0 שורות** (טבלה ריקה)

> 💡 0 שורות! השוואה ל‑NULL עם `=` אף פעם אינה אמת.

</div>

<div dir="rtl">

### שאלה 2

</div>

```sql
SELECT FirstName
FROM   Pupils
WHERE  BirthYear BETWEEN 2010 AND 2012;
```

<div dir="rtl">

| FirstName |
|---|
| אדם |
| מאיה |
| שירה |
| תמר |
| ליאן |
| עומר |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### שאלה 3

</div>

```sql
SELECT FirstName
FROM   Pupils
WHERE  FirstName LIKE '___';
```

<div dir="rtl">

| FirstName |
|---|
| אדם |
| רמי |
| תמר |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

---

## ✏️ תרגילים — 🎵 בית הספר למוזיקה "צלילים"

</div>

<div dir="rtl">

### 1. 🟢 הציגו תלמידים שנולדו בין 2011 ל‑2013 (כולל).

</div>

```sql
SELECT FirstName, BirthYear
FROM   Pupils
WHERE  BirthYear BETWEEN 2011 AND 2013;
```

<div dir="rtl">

| FirstName | BirthYear |
|---|---|
| אדם | 2012 |
| כרים | 2013 |
| שירה | 2011 |
| תמר | 2012 |
| ליאן | 2011 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 2. 🟢 הציגו מורים שיש להם טלפון.

</div>

```sql
SELECT TeacherName, TeacherPhone
FROM   Teachers
WHERE  TeacherPhone IS NOT NULL;
```

<div dir="rtl">

| TeacherName | TeacherPhone |
|---|---|
| סמיר חלבי | 050-1234567 |
| רונית לוי | 052-2345678 |
| דנה כהן | 054-4567890 |
| יוסי פרץ | 053-5678901 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 3. 🟢 הציגו רישומים ששולם בהם 300, 320 או 340 לחודש. השתמשו ב‑`IN`.

</div>

```sql
SELECT RegPupil, MonthlyFee
FROM   Registrations
WHERE  MonthlyFee IN (300, 320, 340);
```

<div dir="rtl">

| RegPupil | MonthlyFee |
|---|---|
| 201 | 320 |
| 203 | 300 |
| 205 | 340 |
| 207 | 320 |
| 208 | 300 |
| 210 | 300 |
| 210 | 320 |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 4. 🟢 הציגו תלמידים ששם המשפחה שלהם מכיל את האות 'ו'.

</div>

```sql
SELECT FirstName, LastName
FROM   Pupils
WHERE  LastName LIKE '%ו%';
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| שירה | לוי |
| רמי | חורי |
| עומר | ביטון |
| סאלי | חסון |
| יואב | שושן |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 5. 🟡 הציגו תלמידים שלא גרים בערים 1 ו‑2.

</div>

```sql
SELECT FirstName, HomeTown
FROM   Pupils
WHERE  HomeTown NOT IN (1, 2);
```

<div dir="rtl">

| FirstName | HomeTown |
|---|---|
| מאיה | 3 |
| תמר | 4 |
| עומר | 4 |
| סאלי | 3 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 6. 🟡 הציגו מורים ששמם (`TeacherName`) מסתיים באות 'י'.

</div>

```sql
SELECT TeacherName
FROM   Teachers
WHERE  TeacherName LIKE '%י';
```

<div dir="rtl">

| TeacherName |
|---|
| סמיר חלבי |
| רונית לוי |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 7. 🟡 הציגו תלמידים ששמם הפרטי בן 4 אותיות בדיוק.

</div>

```sql
SELECT FirstName
FROM   Pupils
WHERE  FirstName LIKE '____';
```

<div dir="rtl">

| FirstName |
|---|
| מאיה |
| כרים |
| שירה |
| ליאן |
| עומר |
| סאלי |
| יואב |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 8. 🟡 הציגו רישומים שהתשלום בהם **לא** בין 300 ל‑350.

</div>

```sql
SELECT RegPupil, MonthlyFee
FROM   Registrations
WHERE  MonthlyFee NOT BETWEEN 300 AND 350;
```

<div dir="rtl">

| RegPupil | MonthlyFee |
|---|---|
| 201 | 280 |
| 202 | 400 |
| 204 | 360 |
| 204 | 380 |
| 206 | 280 |
| 209 | 380 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 9. 🔴 הציגו מורים בלי טלפון שהמחיר שלהם מעל 120.

</div>

```sql
SELECT TeacherName, HourRate
FROM   Teachers
WHERE  TeacherPhone IS NULL AND HourRate > 120;
```

<div dir="rtl">

| TeacherName | HourRate |
|---|---|
| נור מנסור | 130 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 10. 🔴 הציגו את שם המורה והטלפון של מורים שהטלפון שלהם מתחיל ב‑050 או ב‑052.

</div>

```sql
SELECT TeacherName, TeacherPhone
FROM   Teachers
WHERE  TeacherPhone LIKE '050%' OR TeacherPhone LIKE '052%';
```

<div dir="rtl">

| TeacherName | TeacherPhone |
|---|---|
| סמיר חלבי | 050-1234567 |
| רונית לוי | 052-2345678 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 11. 🔴 הציגו תלמידים מהערים 1, 3 שנולדו בין 2010 ל‑2012 ושמם הפרטי מכיל 'א'.

</div>

```sql
SELECT FirstName, BirthYear, HomeTown
FROM   Pupils
WHERE  HomeTown IN (1, 3)
  AND  BirthYear BETWEEN 2010 AND 2012
  AND  FirstName LIKE '%א%';
```

<div dir="rtl">

| FirstName | BirthYear | HomeTown |
|---|---|---|
| אדם | 2012 | 1 |
| מאיה | 2010 | 3 |
| ליאן | 2011 | 1 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

---

## 🏠 תרגול נוסף — 🏫 בית הספר "עתיד"

</div>

<div dir="rtl">

### 1. 🟢 הציגו תלמידים שאין להם טלפון.

</div>

```sql
SELECT FirstName, LastName
FROM   Students
WHERE  Phone IS NULL;
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| נור | עזאם |
| רוני | אברהם |
| כרים | חלבי |
| ג'וד | מנסור |
| איתי | גולן |
| לינא | חמוד |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 2. 🟢 הציגו ציונים בין 90 ל‑100.

</div>

```sql
SELECT StudentId, CourseCode, Grade
FROM   Grades
WHERE  Grade BETWEEN 90 AND 100;
```

<div dir="rtl">

| StudentId | CourseCode | Grade |
|---|---|---|
| 1001 | 14 | 92 |
| 1001 | 11 | 91 |
| 1002 | 11 | 95 |
| 1002 | 15 | 100 |
| 1005 | 15 | 90 |
| 1007 | 11 | 93 |
| 1007 | 13 | 97 |
| 1007 | 11 | 90 |
| 1010 | 11 | 100 |
| 1010 | 13 | 91 |
| 1010 | 12 | 96 |
| 1010 | 11 | 97 |
| 1013 | 13 | 94 |
| 1013 | 17 | 98 |
| 1013 | 11 | 92 |
| 1014 | 17 | 90 |
| 1016 | 11 | 98 |
| 1016 | 13 | 99 |
| 1016 | 17 | 95 |
| 1016 | 12 | 93 |
| 1016 | 11 | 100 |

**התוצאה: 21 שורות**

</div>

<div dir="rtl">

### 3. 🟡 הציגו ציונים חסרים (תלמיד לא נבחן).

</div>

```sql
SELECT StudentId, CourseCode, Term
FROM   Grades
WHERE  Grade IS NULL;
```

<div dir="rtl">

| StudentId | CourseCode | Term |
|---|---|---|
| 1004 | 14 | 1 |
| 1009 | 12 | 1 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 4. 🟡 הציגו תלמידים שנולדו בשנת 2010 (רמז: `LIKE '2010%'`).

</div>

```sql
SELECT FirstName, BirthDate
FROM   Students
WHERE  BirthDate LIKE '2010%';
```

<div dir="rtl">

| FirstName | BirthDate |
|---|---|
| עומר | 2010-02-11 |
| שירה | 2010-09-25 |
| כרים | 2010-12-03 |
| תמר | 2010-04-07 |
| ליאור | 2010-06-16 |
| ג'וד | 2010-08-29 |
| לינא | 2010-10-19 |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 5. 🟡 הציגו מקצועות ששמם מכיל את המילה 'מתמטיקה'.

</div>

```sql
SELECT CourseName
FROM   Courses
WHERE  CourseName LIKE '%מתמטיקה%';
```

<div dir="rtl">

| CourseName |
|---|
| מתמטיקה 5 יח"ל |
| מתמטיקה 3 יח"ל |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 6. 🔴 הציגו תלמידים שעדיין לא שובצו לכיתה, או שתאריך הלידה שלהם חסר.

</div>

```sql
SELECT FirstName, ClassCode, BirthDate
FROM   Students
WHERE  ClassCode IS NULL OR BirthDate IS NULL;
```

<div dir="rtl">

| FirstName | ClassCode | BirthDate |
|---|---|---|
| סאלי | 102 | *NULL* |
| לינא | *NULL* | 2010-10-19 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../02-where/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../04-order-by/solutions.md)

</div>
