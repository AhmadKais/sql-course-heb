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

### שאלה 4

</div>

```sql
SELECT TeacherName
FROM   Teachers
WHERE  HourRate < (SELECT AVG(HourRate) FROM Teachers);
```

<div dir="rtl">

| TeacherName |
|---|
| סמיר חלבי |
| אמיר עזאם |
| יוסי פרץ |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### שאלה 5

</div>

```sql
SELECT InstName
FROM   Instruments
WHERE  InstCode IN (SELECT TeachInst FROM Teachers WHERE HourRate >= 130);
```

<div dir="rtl">

| InstName |
|---|
| פסנתר |
| כינור |

**התוצאה: 2 שורות**

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

### 11. 🟢 הרישום (או הרישומים) עם התשלום הגבוה ביותר.

</div>

```sql
SELECT RegPupil, RegTeacher, MonthlyFee
FROM   Registrations
WHERE  MonthlyFee = (SELECT MAX(MonthlyFee) FROM Registrations);
```

<div dir="rtl">

| RegPupil | RegTeacher | MonthlyFee |
|---|---|---|
| 202 | 2 | 400 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 12. 🟢 מורים שהמחיר שלהם שווה למחיר של 'נור מנסור' או גבוה ממנו.

</div>

```sql
SELECT TeacherName, HourRate
FROM   Teachers
WHERE  HourRate >= (SELECT HourRate FROM Teachers WHERE TeacherName = 'נור מנסור');
```

<div dir="rtl">

| TeacherName | HourRate |
|---|---|
| רונית לוי | 150 |
| דנה כהן | 140 |
| נור מנסור | 130 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 13. 🟡 תלמידים (שמות) שאינם לומדים אצל המורה 5.

</div>

```sql
SELECT FirstName, LastName
FROM   Pupils
WHERE  PupilId NOT IN (SELECT RegPupil FROM Registrations WHERE RegTeacher = 5);
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| מאיה | כהן |
| כרים | עזאם |
| שירה | לוי |
| רמי | חורי |
| ליאן | קבלאן |
| עומר | ביטון |
| סאלי | חסון |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 14. 🟡 ערים (שמות) שאין בהן תלמידים.

</div>

```sql
SELECT CityName
FROM   Cities
WHERE  CityCode NOT IN (SELECT HomeTown FROM Pupils);
```

<div dir="rtl">

| CityName |
|---|
| מעלות |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 15. 🟡 תלמידים (שמות) שלומדים אצל 'רונית לוי'.

</div>

```sql
SELECT FirstName, LastName
FROM   Pupils
WHERE  PupilId IN (SELECT RegPupil FROM Registrations
                   WHERE  RegTeacher = (SELECT TeacherCode FROM Teachers
                                        WHERE  TeacherName = 'רונית לוי'));
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

### 16. 🔴 מורים שאף אחד מהתלמידים שלהם אינו מתחיל.

</div>

```sql
SELECT TeacherName
FROM   Teachers
WHERE  TeacherCode IN (SELECT RegTeacher FROM Registrations)
  AND  TeacherCode NOT IN (SELECT RegTeacher FROM Registrations
                           WHERE  PupilLevel = 'מתחיל');
```

<div dir="rtl">

| TeacherName |
|---|
| אמיר עזאם |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 17. 🔴 תלמידים שנולדו באותה שנה כמו התלמיד הצעיר ביותר שיש לו לוקר.

</div>

```sql
SELECT FirstName, BirthYear
FROM   Pupils
WHERE  BirthYear = (SELECT MAX(BirthYear) FROM Pupils
                    WHERE  PupilId IN (SELECT LockerPupil FROM Lockers));
```

<div dir="rtl">

| FirstName | BirthYear |
|---|---|
| אדם | 2012 |
| תמר | 2012 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

---

## 🎓 בסגנון הבחינה — 🔧 מעבדת "דלתא‑טק"

</div>

<div dir="rtl">

### 1. 🟢 התיקונים שמחירם גבוה מהמחיר הממוצע של תיקון.

</div>

```sql
SELECT RepairNum, CustName, RepairPrice
FROM   Repairs
WHERE  RepairPrice > (SELECT AVG(RepairPrice) FROM Repairs);
```

<div dir="rtl">

| RepairNum | CustName | RepairPrice |
|---|---|---|
| 1002 | מאיה כהן | 980 |
| 1005 | רמי חורי | 760 |
| 1008 | עומר ביטון | 1250 |
| 1012 | אלון כהן | 1480 |
| 1014 | הילה פרץ | 820 |
| 1016 | אורי שמש | 1100 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 2. 🟢 הטכנאי (או הטכנאים) עם השכר לשעה הנמוך ביותר.

</div>

```sql
SELECT TechFirst, TechLast
FROM   Technicians
WHERE  HourWage = (SELECT MIN(HourWage) FROM Technicians);
```

<div dir="rtl">

| TechFirst | TechLast |
|---|---|
| מאיה | אברהם |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 3. 🟡 טכנאים שאין להם עמדת עבודה (`Benches`).

</div>

```sql
SELECT TechFirst, TechLast
FROM   Technicians
WHERE  TechCode NOT IN (SELECT BenchTech FROM Benches);
```

<div dir="rtl">

| TechFirst | TechLast |
|---|---|
| רונית | בר-לב |
| מאיה | אברהם |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 4. 🟡 חלפים שלא השתמשו בהם באף תיקון.

</div>

```sql
SELECT PartName
FROM   Parts
WHERE  PartCode NOT IN (SELECT UsePart FROM PartUsage);
```

<div dir="rtl">

| PartName |
|---|
| כבל שטוח |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 5. 🟡

</div>

```sql
SELECT DevName
FROM   DevTypes
WHERE  DevCode NOT IN (SELECT RepairDev FROM Repairs WHERE Priority = 'רגיל');
```

<div dir="rtl">

| DevName |
|---|
| מחשב נייד |
| שעון חכם |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 6. 🔴 השלימו את הערכים בטבלה שתתקבל.

</div>

```sql
SELECT TechFirst
FROM   Technicians
WHERE  TechCode IN (SELECT RepairTech FROM Repairs WHERE Priority = 'מיידי');
```

<div dir="rtl">

| TechFirst |
|---|
| נביל |
| דנה |
| מאיה |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 7. 🔴 השלימו כך שיוצגו שמות הלקוחות שבתיקון שלהם הוחלף מסך (חלף 101).

</div>

```sql
SELECT CustName
FROM   Repairs
WHERE  RepairNum IN (SELECT UseRepair FROM PartUsage WHERE UsePart = 101);
```

<div dir="rtl">

| CustName |
|---|
| כרים עזאם |
| שירה לוי |
| עומר ביטון |
| נור מנסור |
| אורי שמש |

**התוצאה: 5 שורות**

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

### 6. 🟢 התלמיד (או התלמידים) עם תאריך הלידה המוקדם ביותר.

</div>

```sql
SELECT FirstName, LastName, BirthDate
FROM   Students
WHERE  BirthDate = (SELECT MIN(BirthDate) FROM Students);
```

<div dir="rtl">

| FirstName | LastName | BirthDate |
|---|---|---|
| דניאל | פרץ | 2009-01-20 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 7. 🟡 מקצועות שאף תלמיד לא קיבל בהם ציון מתחת ל‑60.

</div>

```sql
SELECT CourseName
FROM   Courses
WHERE  CourseCode NOT IN (SELECT CourseCode FROM Grades WHERE Grade < 60);
```

<div dir="rtl">

| CourseName |
|---|
| מתמטיקה 5 יח"ל |
| היסטוריה |
| חינוך גופני |
| סדנת פרויקטים |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 8. 🟡 תלמידים שגרים באותה עיר כמו המורה 'נביל'.

</div>

```sql
SELECT FirstName, LastName
FROM   Students
WHERE  CityCode = (SELECT CityCode FROM Teachers WHERE FirstName = 'נביל');
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| אדם | חלבי |
| נור | עזאם |
| כרים | חלבי |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 9. 🔴 ציונים במקצוע 12 שגבוהים מהממוצע של מקצוע 12.

</div>

```sql
SELECT StudentId, Grade
FROM   Grades
WHERE  CourseCode = 12
  AND  Grade > (SELECT AVG(Grade) FROM Grades WHERE CourseCode = 12);
```

<div dir="rtl">

| StudentId | Grade |
|---|---|
| 1002 | 89 |
| 1005 | 81 |
| 1007 | 85 |
| 1010 | 96 |
| 1011 | 80 |
| 1013 | 87 |
| 1016 | 93 |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../09-joins-3-tables-left-join/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../11-views/solutions.md)

</div>
