<div dir="rtl">

# שיעור 9 — פתרונות

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../08-joins/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../10-subqueries/solutions.md)

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
SELECT    TeacherName, RegPupil
FROM      Teachers
LEFT JOIN Registrations ON TeacherCode = RegTeacher
WHERE     RegPupil IS NULL;
```

<div dir="rtl">

| TeacherName | RegPupil |
|---|---|
| נור מנסור | *NULL* |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### שאלה 2

</div>

```sql
SELECT COUNT(*)
FROM   Pupils, Registrations, Teachers
WHERE  PupilId = RegPupil AND RegTeacher = TeacherCode;
```

<div dir="rtl">

| COUNT(*) |
|---|
| 14 |

**התוצאה: שורה אחת**

> 💡 כמספר השורות בטבלה המקשרת — כל רישום הוא זוג אחד.

</div>

<div dir="rtl">

### שאלה 3

</div>

```sql
SELECT    CityName, PupilId
FROM      Cities
LEFT JOIN Pupils ON CityCode = HomeTown
WHERE     PupilId IS NULL;
```

<div dir="rtl">

| CityName | PupilId |
|---|---|
| מעלות | *NULL* |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### שאלה 4

</div>

```sql
SELECT COUNT(*)
FROM   Pupils, Registrations, Teachers
WHERE  PupilId = RegPupil AND RegTeacher = TeacherCode
  AND  HomeTown = 1;
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

### 1. 🟢 לכל רישום: שם התלמיד, שם המורה והתשלום.

</div>

```sql
SELECT FirstName, TeacherName, MonthlyFee
FROM   Pupils, Registrations, Teachers
WHERE  PupilId = RegPupil AND RegTeacher = TeacherCode;
```

<div dir="rtl">

| FirstName | TeacherName | MonthlyFee |
|---|---|---|
| אדם | סמיר חלבי | 320 |
| אדם | יוסי פרץ | 280 |
| מאיה | רונית לוי | 400 |
| כרים | סמיר חלבי | 300 |
| שירה | דנה כהן | 360 |
| שירה | רונית לוי | 380 |
| רמי | אמיר עזאם | 340 |
| תמר | יוסי פרץ | 280 |
| ליאן | דנה כהן | 350 |
| ליאן | סמיר חלבי | 320 |
| עומר | אמיר עזאם | 300 |
| סאלי | רונית לוי | 380 |
| יואב | יוסי פרץ | 300 |
| יואב | אמיר עזאם | 320 |

**התוצאה: 14 שורות**

</div>

<div dir="rtl">

### 2. 🟢 אילו תלמידים (שמות) לומדים אצל 'יוסי פרץ'?

</div>

```sql
SELECT FirstName, LastName
FROM   Pupils, Registrations, Teachers
WHERE  PupilId = RegPupil AND RegTeacher = TeacherCode
  AND  TeacherName = 'יוסי פרץ';
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| אדם | חלבי |
| תמר | אברהם |
| יואב | שושן |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 3. 🟡 אצל אילו מורים (שמות) לומדת 'ליאן'?

</div>

```sql
SELECT TeacherName
FROM   Pupils, Registrations, Teachers
WHERE  PupilId = RegPupil AND RegTeacher = TeacherCode
  AND  FirstName = 'ליאן';
```

<div dir="rtl">

| TeacherName |
|---|
| סמיר חלבי |
| דנה כהן |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 4. 🟡 שם התלמיד, שם העיר שלו ושם המורה — רק רישומים ברמת 'מתחיל'.

</div>

```sql
SELECT FirstName, CityName, TeacherName
FROM   Pupils, Cities, Registrations, Teachers
WHERE  HomeTown = CityCode
  AND  PupilId = RegPupil
  AND  RegTeacher = TeacherCode
  AND  PupilLevel = 'מתחיל';
```

<div dir="rtl">

| FirstName | CityName | TeacherName |
|---|---|---|
| אדם | ירכא | יוסי פרץ |
| כרים | ירכא | סמיר חלבי |
| שירה | עכו | רונית לוי |
| ליאן | ירכא | דנה כהן |
| סאלי | כרמיאל | רונית לוי |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 5. 🟡 כל התלמידים ומספר הלוקר שלהם — גם תלמידים **בלי** לוקר.

</div>

```sql
SELECT    FirstName, LastName, LockerNum
FROM      Pupils
LEFT JOIN Lockers ON PupilId = LockerPupil;
```

<div dir="rtl">

| FirstName | LastName | LockerNum |
|---|---|---|
| אדם | חלבי | 5 |
| מאיה | כהן | 1 |
| כרים | עזאם | *NULL* |
| שירה | לוי | *NULL* |
| רמי | חורי | 2 |
| תמר | אברהם | *NULL* |
| ליאן | קבלאן | 3 |
| עומר | ביטון | *NULL* |
| סאלי | חסון | *NULL* |
| יואב | שושן | 4 |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 6. 🟡 תלמידים שאין להם לוקר.

</div>

```sql
SELECT    FirstName, LastName
FROM      Pupils
LEFT JOIN Lockers ON PupilId = LockerPupil
WHERE     LockerNum IS NULL;
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

### 7. 🔴 כל המורים ומספר הרישומים של כל אחד — כולל מורים עם 0 רישומים.

</div>

```sql
SELECT    TeacherName, COUNT(RegPupil) AS Regs
FROM      Teachers
LEFT JOIN Registrations ON TeacherCode = RegTeacher
GROUP BY  TeacherCode, TeacherName;
```

<div dir="rtl">

| TeacherName | Regs |
|---|---|
| סמיר חלבי | 3 |
| רונית לוי | 3 |
| אמיר עזאם | 3 |
| דנה כהן | 2 |
| יוסי פרץ | 3 |
| נור מנסור | 0 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 8. 🔴 לכל כלי (שם): כמה תלמידים לומדים אותו?

</div>

```sql
SELECT   InstName, COUNT(*) AS Pupils
FROM     Instruments, Teachers, Registrations
WHERE    InstCode = TeachInst AND TeacherCode = RegTeacher
GROUP BY InstName;
```

<div dir="rtl">

| InstName | Pupils |
|---|---|
| גיטרה | 3 |
| כינור | 2 |
| עוד | 3 |
| פסנתר | 3 |
| תופים | 3 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 9. 🔴 לכל עיר (שם): סכום התשלומים החודשיים של התלמידים שגרים בה.

</div>

```sql
SELECT   CityName, SUM(MonthlyFee) AS Total
FROM     Cities, Pupils, Registrations
WHERE    CityCode = HomeTown AND PupilId = RegPupil
GROUP BY CityName;
```

<div dir="rtl">

| CityName | Total |
|---|---|
| ירכא | 1570 |
| כרמיאל | 780 |
| נהריה | 580 |
| עכו | 1700 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 10. 🔴 תלמידים (שמות) שלומדים אצל **שני** מורים או יותר, (אין צורך בשמות המורים).

</div>

```sql
SELECT   FirstName, LastName, COUNT(*) AS Teachers
FROM     Pupils, Registrations
WHERE    PupilId = RegPupil
GROUP BY PupilId, FirstName, LastName
HAVING   COUNT(*) >= 2;
```

<div dir="rtl">

| FirstName | LastName | Teachers |
|---|---|---|
| אדם | חלבי | 2 |
| שירה | לוי | 2 |
| ליאן | קבלאן | 2 |
| יואב | שושן | 2 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 11. 🟢 שמות התלמידים ושמות המורים — רק רישומים משנת 2024.

</div>

```sql
SELECT FirstName, TeacherName
FROM   Pupils, Registrations, Teachers
WHERE  PupilId = RegPupil AND RegTeacher = TeacherCode
  AND  RegYear = 2024;
```

<div dir="rtl">

| FirstName | TeacherName |
|---|---|
| אדם | סמיר חלבי |
| תמר | יוסי פרץ |
| ליאן | סמיר חלבי |
| יואב | אמיר עזאם |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 12. 🟡 אילו תלמידים (שמות) לומדים כלי ממשפחת 'מיתר'? כל תלמיד פעם אחת.

</div>

```sql
SELECT DISTINCT FirstName, LastName
FROM   Pupils, Registrations, Teachers, Instruments
WHERE  PupilId = RegPupil AND RegTeacher = TeacherCode
  AND  TeachInst = InstCode AND InstFamily = 'מיתר';
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| אדם | חלבי |
| כרים | עזאם |
| שירה | לוי |
| רמי | חורי |
| ליאן | קבלאן |
| עומר | ביטון |
| יואב | שושן |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 13. 🟡 כל הכלים ושמות המורים שמלמדים אותם — כולל כלי בלי מורה.

</div>

```sql
SELECT    InstName, TeacherName
FROM      Instruments
LEFT JOIN Teachers ON InstCode = TeachInst;
```

<div dir="rtl">

| InstName | TeacherName |
|---|---|
| פסנתר | נור מנסור |
| פסנתר | רונית לוי |
| גיטרה | אמיר עזאם |
| כינור | דנה כהן |
| תופים | יוסי פרץ |
| חליל | *NULL* |
| עוד | סמיר חלבי |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 14. 🟡 מורים שאין להם אף רישום (עם `LEFT JOIN`).

</div>

```sql
SELECT    TeacherName
FROM      Teachers
LEFT JOIN Registrations ON TeacherCode = RegTeacher
WHERE     RegPupil IS NULL;
```

<div dir="rtl">

| TeacherName |
|---|
| נור מנסור |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 15. 🔴 לכל מורה (שם): כמה ערים שונות מגיעים ממנו התלמידים שלו?

</div>

```sql
SELECT   TeacherName, COUNT(DISTINCT HomeTown) AS Cities
FROM     Teachers, Registrations, Pupils
WHERE    TeacherCode = RegTeacher AND RegPupil = PupilId
GROUP BY TeacherCode, TeacherName;
```

<div dir="rtl">

| TeacherName | Cities |
|---|---|
| סמיר חלבי | 1 |
| רונית לוי | 2 |
| אמיר עזאם | 2 |
| דנה כהן | 2 |
| יוסי פרץ | 3 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 16. 🔴 כל התלמידים וסך התשלום החודשי שלהם — כולל תלמידים בלי רישום (`IFNULL` ל‑0).

</div>

```sql
SELECT    FirstName, LastName, IFNULL(SUM(MonthlyFee), 0) AS Total
FROM      Pupils
LEFT JOIN Registrations ON PupilId = RegPupil
GROUP BY  PupilId, FirstName, LastName;
```

<div dir="rtl">

| FirstName | LastName | Total |
|---|---|---|
| אדם | חלבי | 600 |
| מאיה | כהן | 400 |
| כרים | עזאם | 300 |
| שירה | לוי | 740 |
| רמי | חורי | 340 |
| תמר | אברהם | 280 |
| ליאן | קבלאן | 670 |
| עומר | ביטון | 300 |
| סאלי | חסון | 380 |
| יואב | שושן | 620 |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 17. 🔴 שמות התלמידים שגרים בכרמיאל, שמות המורים שלהם ושמות הכלים (5 טבלאות).

</div>

```sql
SELECT FirstName, TeacherName, InstName
FROM   Cities, Pupils, Registrations, Teachers, Instruments
WHERE  CityCode = HomeTown AND PupilId = RegPupil
  AND  RegTeacher = TeacherCode AND TeachInst = InstCode
  AND  CityName = 'כרמיאל';
```

<div dir="rtl">

| FirstName | TeacherName | InstName |
|---|---|---|
| מאיה | רונית לוי | פסנתר |
| סאלי | רונית לוי | פסנתר |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

---

## 🎓 בסגנון הבחינה — 🎮 חנות משחקי מחשב

</div>

<div dir="rtl">

### 1. 🟢 לכל הזמנה: שם המשתמש, שם המשחק ומספר השעות.

</div>

```sql
SELECT FirstName, LastName, GameName, Hours
FROM   Users, Orders, Games
WHERE  UserId = BuyerId AND GameNum = GameCode;
```

<div dir="rtl">

| FirstName | LastName | GameName | Hours |
|---|---|---|---|
| רמי | חלבי | FIFA | 3 |
| שני | כהן | The Sims | 5 |
| רמי | חלבי | Zelda | 2 |
| וליד | סעד | FIFA | 4 |
| אור | לוי | Mario Kart | 1 |
| שני | כהן | Mario Kart | 2 |
| דניאל | חורי | Anno 1800 | 6 |
| רמי | חלבי | FIFA | 2 |
| מאיה | פרץ | Assassin's Creed | 3 |
| וליד | סעד | NBA Live | 2 |
| שני | כהן | Zelda | 4 |
| דניאל | חורי | FIFA | 1 |
| מאיה | פרץ | The Sims | 3 |

**התוצאה: 13 שורות**

</div>

<div dir="rtl">

### 2. 🟡 אילו משחקים (שמות) הזמין 'רמי חלבי'? כל משחק פעם אחת.

</div>

```sql
SELECT DISTINCT GameName
FROM   Users, Orders, Games
WHERE  UserId = BuyerId AND GameNum = GameCode
  AND  FirstName = 'רמי' AND LastName = 'חלבי';
```

<div dir="rtl">

| GameName |
|---|
| FIFA |
| Zelda |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 3. 🟡 לכל משחק: שם המשחק, שם הקטגוריה ושם החברה.

</div>

```sql
SELECT GameName, CatName, CompName
FROM   Games, Categories, Companies
WHERE  TypeCode = CatCode AND MakerCode = CompCode;
```

<div dir="rtl">

| GameName | CatName | CompName |
|---|---|---|
| Mario Kart | ספורט | Nintendo |
| FIFA | ספורט | Electronic Arts |
| Assassin's Creed | פעולה | Ubisoft |
| The Sims | סימולציה | Maxis |
| SimCity | סימולציה | Maxis |
| Zelda | פעולה | Nintendo |
| Anno 1800 | אסטרטגיה | Ubisoft |
| NBA Live | ספורט | Electronic Arts |
| Just Dance | ספורט | Ubisoft |

**התוצאה: 9 שורות**

</div>

<div dir="rtl">

### 4. 🟡 משתמשים שלא הזמינו אף משחק (עם `LEFT JOIN`).

</div>

```sql
SELECT    FirstName, LastName
FROM      Users
LEFT JOIN Orders ON UserId = BuyerId
WHERE     OrderId IS NULL;
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| נאדר | עזאם |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 5. 🔴 לכל משתמש (שם): כמה שילם בסך הכול (שעות × מחיר לשעה).

</div>

```sql
SELECT   FirstName, LastName, SUM(Hours * PricePerHour) AS Paid
FROM     Users, Orders, Games
WHERE    UserId = BuyerId AND GameNum = GameCode
GROUP BY UserId, FirstName, LastName;
```

<div dir="rtl">

| FirstName | LastName | Paid |
|---|---|---|
| רמי | חלבי | 60.0 |
| שני | כהן | 88.0 |
| וליד | סעד | 47.0 |
| אור | לוי | 6.5 |
| דניאל | חורי | 59.0 |
| מאיה | פרץ | 49.5 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 6. 🔴

</div>

```sql
SELECT   CatName, COUNT(*) AS Orders
FROM     Categories, Games, Orders
WHERE    CatCode = TypeCode AND GameCode = GameNum
GROUP BY CatName;
```

<div dir="rtl">

| CatName | Orders |
|---|---|
| אסטרטגיה | 1 |
| סימולציה | 2 |
| ספורט | 7 |
| פעולה | 3 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 7. 🔴 השלימו את הערכים.

</div>

```sql
SELECT    CompName, COUNT(GameCode) AS Games
FROM      Companies
LEFT JOIN Games ON CompCode = MakerCode
GROUP BY  CompName;
```

<div dir="rtl">

| CompName | Games |
|---|---|
| Electronic Arts | 2 |
| Maxis | 2 |
| Nintendo | 2 |
| Playtika | 0 |
| Ubisoft | 3 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

---

## 🏠 תרגול נוסף — 🏫 בית הספר "עתיד"

</div>

<div dir="rtl">

### 1. 🟢 לכל ציון: שם התלמיד, שם המקצוע והציון — במחצית 1.

</div>

```sql
SELECT S.FirstName, S.LastName, C.CourseName, G.Grade
FROM   Students S, Grades G, Courses C
WHERE  S.StudentId = G.StudentId
  AND  G.CourseCode = C.CourseCode
  AND  G.Term = 1;
```

<div dir="rtl">

| FirstName | LastName | CourseName | Grade |
|---|---|---|---|
| אדם | חלבי | מתמטיקה 5 יח"ל | 88 |
| אדם | חלבי | אנגלית 4 יח"ל | 74 |
| אדם | חלבי | היסטוריה | 92 |
| נור | עזאם | מתמטיקה 5 יח"ל | 95 |
| נור | עזאם | אנגלית 4 יח"ל | 89 |
| נור | עזאם | חינוך גופני | 100 |
| יואב | כהן | מתמטיקה 3 יח"ל | 61 |
| יואב | כהן | אנגלית 4 יח"ל | 55 |
| יואב | כהן | היסטוריה | 70 |
| מאיה | לוי | מתמטיקה 3 יח"ל | 48 |
| מאיה | לוי | אנגלית 4 יח"ל | 62 |
| מאיה | לוי | היסטוריה | *NULL* |
| רוני | אברהם | מתמטיקה 5 יח"ל | 77 |
| רוני | אברהם | אנגלית 4 יח"ל | 81 |
| רוני | אברהם | חינוך גופני | 90 |
| סאלי | חסון | מתמטיקה 3 יח"ל | 66 |
| סאלי | חסון | אנגלית 4 יח"ל | 58 |
| עומר | ביטון | מתמטיקה 5 יח"ל | 93 |
| עומר | ביטון | מבוא לבסיסי נתונים | 97 |
| עומר | ביטון | אנגלית 4 יח"ל | 85 |
| שירה | כהן | מתמטיקה 5 יח"ל | 72 |
| שירה | כהן | מבוא לבסיסי נתונים | 79 |
| שירה | כהן | אנגלית 4 יח"ל | 68 |
| כרים | חלבי | מתמטיקה 3 יח"ל | 54 |
| כרים | חלבי | מבוא לבסיסי נתונים | 63 |
| … | … | … | … |

**התוצאה: 52 שורות** — מוצגות 25 הראשונות

</div>

<div dir="rtl">

### 2. 🟡 הציונים של 'אדם חלבי' בכל המקצועות (שם מקצוע + ציון + מחצית).

</div>

```sql
SELECT C.CourseName, G.Term, G.Grade
FROM   Students S, Grades G, Courses C
WHERE  S.StudentId = G.StudentId AND G.CourseCode = C.CourseCode
  AND  S.FirstName = 'אדם' AND S.LastName = 'חלבי';
```

<div dir="rtl">

| CourseName | Term | Grade |
|---|---|---|
| מתמטיקה 5 יח"ל | 1 | 88 |
| אנגלית 4 יח"ל | 1 | 74 |
| היסטוריה | 1 | 92 |
| מתמטיקה 5 יח"ל | 2 | 91 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 3. 🟡 כל המקצועות ושם המורה — כולל מקצוע שעדיין אין לו מורה.

</div>

```sql
SELECT    C.CourseName, T.FirstName, T.LastName
FROM      Courses C
LEFT JOIN Teachers T ON C.TeacherCode = T.TeacherCode;
```

<div dir="rtl">

| CourseName | FirstName | LastName |
|---|---|---|
| מתמטיקה 5 יח"ל | נביל | סרחאן |
| אנגלית 4 יח"ל | רונית | בר-לב |
| מבוא לבסיסי נתונים | חוסאם | זיאד |
| היסטוריה | אורלי | שמש |
| חינוך גופני | פאדי | חדאד |
| מתמטיקה 3 יח"ל | גלית | מזרחי |
| סדנת פרויקטים | *NULL* | *NULL* |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 4. 🔴 תלמידים שלא נעדרו אף פעם.

</div>

```sql
SELECT    S.FirstName, S.LastName
FROM      Students S
LEFT JOIN Absences A ON S.StudentId = A.StudentId
WHERE     A.AbsenceId IS NULL;
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

### 5. 🔴 לכל מקצוע (שם): הממוצע במחצית 1, מעוגל, מהגבוה לנמוך.

</div>

```sql
SELECT   C.CourseName, ROUND(AVG(G.Grade), 1) AS AvgGrade
FROM     Courses C, Grades G
WHERE    C.CourseCode = G.CourseCode AND G.Term = 1
GROUP BY C.CourseName
ORDER BY AvgGrade DESC;
```

<div dir="rtl">

| CourseName | AvgGrade |
|---|---|
| חינוך גופני | 95.0 |
| סדנת פרויקטים | 88.5 |
| מתמטיקה 5 יח"ל | 85.3 |
| מבוא לבסיסי נתונים | 79.5 |
| היסטוריה | 77.0 |
| אנגלית 4 יח"ל | 74.9 |
| מתמטיקה 3 יח"ל | 59.0 |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 6. 🟢 לכל ציון של מחצית 2: שם התלמיד, שם המקצוע והציון.

</div>

```sql
SELECT S.FirstName, C.CourseName, G.Grade
FROM   Students S, Grades G, Courses C
WHERE  S.StudentId = G.StudentId AND G.CourseCode = C.CourseCode
  AND  G.Term = 2;
```

<div dir="rtl">

| FirstName | CourseName | Grade |
|---|---|---|
| אדם | מתמטיקה 5 יח"ל | 91 |
| יואב | מתמטיקה 3 יח"ל | 67 |
| עומר | מתמטיקה 5 יח"ל | 90 |
| תמר | מתמטיקה 5 יח"ל | 97 |
| ג'וד | מתמטיקה 3 יח"ל | 39 |
| דניאל | מתמטיקה 5 יח"ל | 92 |
| איתי | מתמטיקה 3 יח"ל | 62 |
| ראניה | מתמטיקה 5 יח"ל | 100 |

**התוצאה: 8 שורות**

</div>

<div dir="rtl">

### 7. 🟡 כל התלמידים ושם הכיתה — כולל תלמידה בלי כיתה.

</div>

```sql
SELECT    S.FirstName, S.LastName, C.ClassName
FROM      Students S
LEFT JOIN Classes C ON S.ClassCode = C.ClassCode;
```

<div dir="rtl">

| FirstName | LastName | ClassName |
|---|---|---|
| אדם | חלבי | י1 |
| נור | עזאם | י1 |
| יואב | כהן | י1 |
| מאיה | לוי | י2 |
| רוני | אברהם | י2 |
| סאלי | חסון | י2 |
| עומר | ביטון | יא1 |
| שירה | כהן | יא1 |
| כרים | חלבי | יא1 |
| תמר | שושן | יא2 |
| ליאור | לוי | יא2 |
| ג'וד | מנסור | יא2 |
| דניאל | פרץ | יב1 |
| הדיל | סעיד | יב1 |
| איתי | גולן | יב1 |
| ראניה | עבאס | יב1 |
| נועם | שחר | י1 |
| לינא | חמוד | *NULL* |

**התוצאה: 18 שורות**

</div>

<div dir="rtl">

### 8. 🟡 לכל מורה: שם המורה וכמה ציונים נתן (דרך המקצועות שלו).

</div>

```sql
SELECT   T.FirstName, T.LastName, COUNT(G.Grade) AS Grades
FROM     Teachers T, Courses C, Grades G
WHERE    T.TeacherCode = C.TeacherCode AND C.CourseCode = G.CourseCode
GROUP BY T.TeacherCode, T.FirstName, T.LastName;
```

<div dir="rtl">

| FirstName | LastName | Grades |
|---|---|---|
| נביל | סרחאן | 15 |
| רונית | בר-לב | 14 |
| חוסאם | זיאד | 10 |
| אורלי | שמש | 3 |
| פאדי | חדאד | 2 |
| גלית | מזרחי | 10 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 9. 🔴 כל הערים ומספר התלמידים בכל אחת — כולל ערים בלי תלמידים.

</div>

```sql
SELECT    C.CityName, COUNT(S.StudentId) AS Students
FROM      Cities C
LEFT JOIN Students S ON C.CityCode = S.CityCode
GROUP BY  C.CityName;
```

<div dir="rtl">

| CityName | Students |
|---|---|
| חיפה | 4 |
| ירכא | 3 |
| כרמיאל | 2 |
| נהריה | 2 |
| עכו | 3 |
| שפרעם | 3 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../08-joins/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../10-subqueries/solutions.md)

</div>
