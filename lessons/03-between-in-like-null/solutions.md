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

### שאלה 4

</div>

```sql
SELECT FirstName
FROM   Pupils
WHERE  LastName LIKE '%ן';
```

<div dir="rtl">

| FirstName |
|---|
| מאיה |
| ליאן |
| עומר |
| סאלי |
| יואב |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### שאלה 5

</div>

```sql
SELECT COUNT(*)
FROM   Registrations
WHERE  RegTeacher IN (1, 2, 6);
```

<div dir="rtl">

| COUNT(*) |
|---|
| 6 |

**התוצאה: שורה אחת**

> 💡 למורה 6 אין רישומים, אז הוא לא מוסיף כלום.

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

### 12. 🟢 הציגו את הכלים ממשפחות 'הקשה' או 'נשיפה' (עם `IN`).

</div>

```sql
SELECT InstName, InstFamily
FROM   Instruments
WHERE  InstFamily IN ('הקשה', 'נשיפה');
```

<div dir="rtl">

| InstName | InstFamily |
|---|---|
| תופים | הקשה |
| חליל | נשיפה |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 13. 🟢 הציגו מורים שהמחיר שלהם בין 100 ל‑120.

</div>

```sql
SELECT TeacherName, HourRate
FROM   Teachers
WHERE  HourRate BETWEEN 100 AND 120;
```

<div dir="rtl">

| TeacherName | HourRate |
|---|---|
| סמיר חלבי | 120 |
| אמיר עזאם | 110 |
| יוסי פרץ | 100 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 14. 🟡 הציגו תלמידים ששמם הפרטי מתחיל ב‑'ש' או ב‑'ס'.

</div>

```sql
SELECT FirstName, LastName
FROM   Pupils
WHERE  FirstName LIKE 'ש%' OR FirstName LIKE 'ס%';
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| שירה | לוי |
| סאלי | חסון |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 15. 🟡 הציגו רישומים משנים 2021–2023 (עם `BETWEEN`).

</div>

```sql
SELECT RegPupil, RegYear
FROM   Registrations
WHERE  RegYear BETWEEN 2021 AND 2023;
```

<div dir="rtl">

| RegPupil | RegYear |
|---|---|
| 202 | 2022 |
| 204 | 2023 |
| 205 | 2021 |
| 208 | 2023 |
| 210 | 2022 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 16. 🟡 הציגו מורים ששמם הפרטי (המילה הראשונה) בן 3 אותיות בדיוק (רמז: `'___ %'`).

</div>

```sql
SELECT TeacherName
FROM   Teachers
WHERE  TeacherName LIKE '___ %';
```

<div dir="rtl">

| TeacherName |
|---|
| דנה כהן |
| נור מנסור |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 17. 🔴 הציגו את המורים בלי טלפון, או שהמחיר שלהם לא בין 110 ל‑140.

</div>

```sql
SELECT TeacherName, HourRate, TeacherPhone
FROM   Teachers
WHERE  TeacherPhone IS NULL OR HourRate NOT BETWEEN 110 AND 140;
```

<div dir="rtl">

| TeacherName | HourRate | TeacherPhone |
|---|---|---|
| רונית לוי | 150 | 052-2345678 |
| אמיר עזאם | 110 | *NULL* |
| יוסי פרץ | 100 | 053-5678901 |
| נור מנסור | 130 | *NULL* |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 18. 🔴 הציגו רישומים של תלמידים 201–205 שאינם ברמת 'מתחיל'.

</div>

```sql
SELECT RegPupil, PupilLevel
FROM   Registrations
WHERE  RegPupil BETWEEN 201 AND 205 AND PupilLevel NOT IN ('מתחיל');
```

<div dir="rtl">

| RegPupil | PupilLevel |
|---|---|
| 201 | ממשיך |
| 202 | מתקדם |
| 204 | ממשיך |
| 205 | מתקדם |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

---

## 🎓 בסגנון הבחינה — 📚 ספרייה עירונית

</div>

<div dir="rtl">

### 1. 🟢 הציגו את הספרים שיצאו בין 1990 ל‑2010.

</div>

```sql
SELECT Title, PubYear
FROM   Books
WHERE  PubYear BETWEEN 1990 AND 2010;
```

<div dir="rtl">

| Title | PubYear |
|---|---|
| סיפור על אהבה וחושך | 2002 |
| הארי פוטר ואבן החכמים | 1997 |
| הארי פוטר וחדר הסודות | 1998 |
| אשה בורחת מבשורה | 2008 |
| ספר הדקדוק הפנימי | 1991 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 2. 🟢 הציגו את ההשאלות שעדיין לא הוחזרו.

</div>

```sql
SELECT LoanId, ReaderId, BookNum
FROM   Loans
WHERE  ReturnDate IS NULL;
```

<div dir="rtl">

| LoanId | ReaderId | BookNum |
|---|---|---|
| 2 | 501 | 203 |
| 5 | 504 | 207 |
| 7 | 502 | 206 |
| 8 | 506 | 202 |
| 10 | 501 | 205 |
| 11 | 508 | 201 |
| 12 | 505 | 204 |
| 14 | 509 | 208 |

**התוצאה: 8 שורות**

</div>

<div dir="rtl">

### 3. 🟡 הציגו את הסופרים מישראל או ממצרים (עם `IN`).

</div>

```sql
SELECT AuthorFirstName, AuthorLastName
FROM   Authors
WHERE  Country IN ('ישראל', 'מצרים');
```

<div dir="rtl">

| AuthorFirstName | AuthorLastName |
|---|---|
| עמוס | עוז |
| נגיב | מחפוז |
| דויד | גרוסמן |
| סמי | מיכאל |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 4. 🟡 הציגו ספרים ששמם מכיל את המילה 'הארי'.

</div>

```sql
SELECT DISTINCT Title
FROM   Books
WHERE  Title LIKE '%הארי%';
```

<div dir="rtl">

| Title |
|---|
| הארי פוטר ואבן החכמים |
| הארי פוטר וחדר הסודות |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 5. 🟡

</div>

```sql
SELECT FirstName, LastName
FROM   Members
WHERE  LastName LIKE 'כ%';
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| עידו | כהן |
| הילה | כהן |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 6. 🟡 השלימו את הערכים בטבלה שתתקבל.

</div>

```sql
SELECT Title
FROM   Books
WHERE  Genre = 'מתח' AND Pages BETWEEN 250 AND 300;
```

<div dir="rtl">

| Title |
|---|
| רצח באוריינט אקספרס |
| ואז לא נשאר אף אחד |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 7. 🔴 השלימו כך שיוצגו ההשאלות מאוקטובר 2025 שכבר הוחזרו.

</div>

```sql
SELECT LoanId
FROM   Loans
WHERE  LoanDate LIKE '2025-10%' AND ReturnDate IS NOT NULL;
```

<div dir="rtl">

| LoanId |
|---|
| 9 |
| 13 |

**התוצאה: 2 שורות**

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

### 7. 🟢 הציגו כיתות שעדיין לא שובצה להן כיתת אם (`RoomNumber`).

</div>

```sql
SELECT ClassName
FROM   Classes
WHERE  RoomNumber IS NULL;
```

<div dir="rtl">

| ClassName |
|---|
| יא2 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 8. 🟡 הציגו היעדרויות שלא נמסרה להן סיבה.

</div>

```sql
SELECT StudentId, AbsenceDate
FROM   Absences
WHERE  Reason IS NULL;
```

<div dir="rtl">

| StudentId | AbsenceDate |
|---|---|
| 1004 | 2026-09-07 |
| 1009 | 2026-09-08 |
| 1009 | 2026-09-09 |
| 1012 | 2026-09-02 |
| 1012 | 2026-09-10 |
| 1012 | 2026-09-15 |
| 1012 | 2026-09-16 |
| 1015 | 2026-09-17 |
| 1018 | 2026-09-15 |

**התוצאה: 9 שורות**

</div>

<div dir="rtl">

### 9. 🟡 הציגו מורים שהתחילו לעבוד בין 2015 ל‑2022.

</div>

```sql
SELECT FirstName, HireDate
FROM   Teachers
WHERE  HireDate BETWEEN '2015-01-01' AND '2022-12-31';
```

<div dir="rtl">

| FirstName | HireDate |
|---|---|
| רונית | 2018-09-01 |
| חוסאם | 2021-02-15 |
| גלית | 2016-09-01 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 10. 🔴 הציגו תלמידים ששם המשפחה שלהם מכיל '-' או מתחיל ב‑'ח'.

</div>

```sql
SELECT FirstName, LastName
FROM   Students
WHERE  LastName LIKE '%-%' OR LastName LIKE 'ח%';
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| אדם | חלבי |
| סאלי | חסון |
| כרים | חלבי |
| לינא | חמוד |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../02-where/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../04-order-by/solutions.md)

</div>
