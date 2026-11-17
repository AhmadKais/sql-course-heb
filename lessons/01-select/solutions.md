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

### שאלה 4

</div>

```sql
SELECT DISTINCT RegTeacher
FROM   Registrations;
```

<div dir="rtl">

| RegTeacher |
|---|
| 1 |
| 5 |
| 2 |
| 4 |
| 3 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### שאלה 5

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

### 13. 🟢 הציגו את קוד המורה ואת שם המורה בלבד.

</div>

```sql
SELECT TeacherCode, TeacherName
FROM   Teachers;
```

<div dir="rtl">

| TeacherCode | TeacherName |
|---|---|
| 1 | סמיר חלבי |
| 2 | רונית לוי |
| 3 | אמיר עזאם |
| 4 | דנה כהן |
| 5 | יוסי פרץ |
| 6 | נור מנסור |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 14. 🟢 הציגו את כל העמודות של טבלת הערים (`Cities`).

</div>

```sql
SELECT *
FROM   Cities;
```

<div dir="rtl">

| CityCode | CityName |
|---|---|
| 1 | ירכא |
| 2 | עכו |
| 3 | כרמיאל |
| 4 | נהריה |
| 5 | מעלות |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 15. 🟡 הציגו לכל לוקר את מספרו ואת הקומה, בשמות `Locker` ו‑`Floor`.

</div>

```sql
SELECT LockerNum AS Locker, LockerFloor AS Floor
FROM   Lockers;
```

<div dir="rtl">

| Locker | Floor |
|---|---|
| 1 | 1 |
| 2 | 1 |
| 3 | 2 |
| 4 | 2 |
| 5 | 2 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 16. 🟡 אילו תלמידים (קודים) רשומים לשיעורים? כל תלמיד פעם אחת.

</div>

```sql
SELECT DISTINCT RegPupil
FROM   Registrations;
```

<div dir="rtl">

| RegPupil |
|---|
| 201 |
| 202 |
| 203 |
| 204 |
| 205 |
| 206 |
| 207 |
| 208 |
| 209 |
| 210 |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 17. 🟡 הציגו לכל רישום את קוד התלמיד, התשלום החודשי והתשלום לשבוע (חלקי 4), בשם `Weekly`.

</div>

```sql
SELECT RegPupil, MonthlyFee, MonthlyFee / 4 AS Weekly
FROM   Registrations;
```

<div dir="rtl">

| RegPupil | MonthlyFee | Weekly |
|---|---|---|
| 201 | 320 | 80 |
| 201 | 280 | 70 |
| 202 | 400 | 100 |
| 203 | 300 | 75 |
| 204 | 360 | 90 |
| 204 | 380 | 95 |
| 205 | 340 | 85 |
| 206 | 280 | 70 |
| 207 | 350 | 87 |
| 207 | 320 | 80 |
| 208 | 300 | 75 |
| 209 | 380 | 95 |
| 210 | 300 | 75 |
| 210 | 320 | 80 |

**התוצאה: 14 שורות**

</div>

<div dir="rtl">

### 18. 🔴 אילו צירופים של שנה ורמה קיימים ברישומים? כל צירוף פעם אחת.

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

</div>

<div dir="rtl">

### 19. 🔴 הציגו לכל מורה משפט אחד בעמודה `Info`, למשל: `סמיר חלבי - 120`.

</div>

```sql
SELECT TeacherName || ' - ' || HourRate AS Info
FROM   Teachers;
```

<div dir="rtl">

| Info |
|---|
| סמיר חלבי - 120 |
| רונית לוי - 150 |
| אמיר עזאם - 110 |
| דנה כהן - 140 |
| יוסי פרץ - 100 |
| נור מנסור - 130 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

---

## 🎓 בסגנון הבחינה — 🎮 חנות משחקי מחשב

</div>

<div dir="rtl">

### 1. 🟢 הציגו את שם המשחק ואת שנת היציאה של כל המשחקים.

</div>

```sql
SELECT GameName, GameYear
FROM   Games;
```

<div dir="rtl">

| GameName | GameYear |
|---|---|
| Mario Kart | 2017 |
| FIFA | 2021 |
| Assassin's Creed | 2020 |
| The Sims | 2014 |
| SimCity | 2013 |
| Zelda | 2023 |
| Anno 1800 | 2019 |
| NBA Live | 2021 |
| Tetris | 1984 |
| Just Dance | 2022 |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 2. 🟢 הציגו את השם הפרטי, שם המשפחה והאימייל של כל המשתמשים.

</div>

```sql
SELECT FirstName, LastName, Email
FROM   Users;
```

<div dir="rtl">

| FirstName | LastName | Email |
|---|---|---|
| רמי | חלבי | rami@mail.com |
| שני | כהן | shani@mail.com |
| וליד | סעד | walid@mail.com |
| אור | לוי | *NULL* |
| דניאל | חורי | dani@mail.com |
| מאיה | פרץ | maya@mail.com |
| נאדר | עזאם | *NULL* |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 3. 🟡 באילו מדינות יש חברות משחקים? כל מדינה פעם אחת.

</div>

```sql
SELECT DISTINCT Country
FROM   Companies;
```

<div dir="rtl">

| Country |
|---|
| Japan |
| USA |
| France |
| Israel |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 4. 🟡 הציגו לכל משחק את שמו ואת המחיר ל‑3 שעות משחק, בשם `ThreeHours`.

</div>

```sql
SELECT GameName, PricePerHour * 3 AS ThreeHours
FROM   Games;
```

<div dir="rtl">

| GameName | ThreeHours |
|---|---|
| Mario Kart | 19.5 |
| FIFA | 24.0 |
| Assassin's Creed | 28.5 |
| The Sims | 21.0 |
| SimCity | 16.5 |
| Zelda | 30.0 |
| Anno 1800 | 25.5 |
| NBA Live | 22.5 |
| Tetris | 9.0 |
| Just Dance | 18.0 |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 5. 🟡

</div>

```sql
SELECT DISTINCT BuyerId
FROM   Orders;
```

<div dir="rtl">

| BuyerId |
|---|
| 1 |
| 2 |
| 3 |
| 4 |
| 5 |
| 6 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 6. 🟡 כמה שורות יחזרו, ומה הן?

</div>

```sql
SELECT DISTINCT TypeCode
FROM   Games;
```

<div dir="rtl">

| TypeCode |
|---|
| 2 |
| 1 |
| 4 |
| 3 |
| 5 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 7. 🔴 השלימו כך שיוצגו שם המשחק ומספר השנים מאז שיצא (עד 2026), בשם `Age`.

</div>

```sql
SELECT GameName, 2026 - GameYear AS Age
FROM   Games;
```

<div dir="rtl">

| GameName | Age |
|---|---|
| Mario Kart | 9 |
| FIFA | 5 |
| Assassin's Creed | 6 |
| The Sims | 12 |
| SimCity | 13 |
| Zelda | 3 |
| Anno 1800 | 7 |
| NBA Live | 5 |
| Tetris | 42 |
| Just Dance | 4 |

**התוצאה: 10 שורות**

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

### 6. 🟢 הציגו את שם הכיתה ואת השכבה של כל הכיתות.

</div>

```sql
SELECT ClassName, Grade
FROM   Classes;
```

<div dir="rtl">

| ClassName | Grade |
|---|---|
| י1 | 10 |
| י2 | 10 |
| יא1 | 11 |
| יא2 | 11 |
| יב1 | 12 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 7. 🟢 הציגו את קוד התלמיד, תאריך ההיעדרות והסיבה מטבלת ההיעדרויות.

</div>

```sql
SELECT StudentId, AbsenceDate, Reason
FROM   Absences;
```

<div dir="rtl">

| StudentId | AbsenceDate | Reason |
|---|---|---|
| 1003 | 2026-09-02 | מחלה |
| 1003 | 2026-09-03 | מחלה |
| 1004 | 2026-09-07 | *NULL* |
| 1009 | 2026-09-08 | *NULL* |
| 1009 | 2026-09-09 | *NULL* |
| 1009 | 2026-09-14 | תור לרופא |
| 1012 | 2026-09-02 | *NULL* |
| 1012 | 2026-09-10 | *NULL* |
| 1012 | 2026-09-15 | *NULL* |
| 1012 | 2026-09-16 | *NULL* |
| 1006 | 2026-09-11 | אירוע משפחתי |
| 1015 | 2026-09-04 | מחלה |
| 1015 | 2026-09-17 | *NULL* |
| 1001 | 2026-09-18 | תור לרופא |
| 1010 | 2026-09-08 | מחלה |
| 1018 | 2026-09-15 | *NULL* |

**התוצאה: 16 שורות**

</div>

<div dir="rtl">

### 8. 🟡 באילו שכבות יש כיתות? כל שכבה פעם אחת.

</div>

```sql
SELECT DISTINCT Grade
FROM   Classes;
```

<div dir="rtl">

| Grade |
|---|
| 10 |
| 11 |
| 12 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 9. 🔴 הציגו לכל ציון את קוד התלמיד ואת הציון אחרי פקטור של 5 נקודות, בשם `WithFactor`.

</div>

```sql
SELECT StudentId, Grade + 5 AS WithFactor
FROM   Grades;
```

<div dir="rtl">

| StudentId | WithFactor |
|---|---|
| 1001 | 93 |
| 1001 | 79 |
| 1001 | 97 |
| 1001 | 96 |
| 1002 | 100 |
| 1002 | 94 |
| 1002 | 105 |
| 1003 | 66 |
| 1003 | 60 |
| 1003 | 75 |
| 1003 | 72 |
| 1004 | 53 |
| 1004 | 67 |
| 1004 | *NULL* |
| 1005 | 82 |
| 1005 | 86 |
| 1005 | 95 |
| 1006 | 71 |
| 1006 | 63 |
| 1007 | 98 |
| 1007 | 102 |
| 1007 | 90 |
| 1007 | 95 |
| 1008 | 77 |
| 1008 | 84 |
| … | … |

**התוצאה: 60 שורות** — מוצגות 25 הראשונות

</div>

<div dir="rtl">

---

[⬅️ חזרה לשיעור](README.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../02-where/solutions.md)

</div>
