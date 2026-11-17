<div dir="rtl">

# שיעור 12 — פתרונות

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../11-views/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../13-create-alter-drop/solutions.md)

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
UPDATE Registrations SET MonthlyFee = 0 WHERE RegYear = 2030;
SELECT COUNT(*) FROM Registrations WHERE MonthlyFee = 0;
```

<div dir="rtl">

| COUNT(*) |
|---|
| 0 |

**התוצאה: שורה אחת**

> 💡 אין רישומים מ‑2030 — הפקודה לא שינתה כלום, ואין שגיאה.

</div>

<div dir="rtl">

### שאלה 2

</div>

```sql
DELETE FROM Lockers WHERE LockerFloor = 1;
SELECT COUNT(*) FROM Lockers;
```

<div dir="rtl">

| COUNT(*) |
|---|
| 3 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### שאלה 3

</div>

```sql
UPDATE Teachers SET HourRate = HourRate * 2 WHERE TeacherCode = 5;
SELECT HourRate FROM Teachers WHERE TeacherCode = 5;
```

<div dir="rtl">

| HourRate |
|---|
| 200 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### שאלה 4

</div>

```sql
DELETE FROM Registrations WHERE PupilLevel = 'מתחיל';
SELECT COUNT(*) FROM Registrations;
```

<div dir="rtl">

| COUNT(*) |
|---|
| 9 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

---

## ✏️ תרגילים — 🎵 בית הספר למוזיקה "צלילים"

</div>

<div dir="rtl">

### 1. 🟢 הוסיפו את הכלי 'צ'לו' (קוד 70, משפחת 'מיתר').

</div>

```sql
INSERT INTO Instruments VALUES (70, 'צ''לו', 'מיתר');
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Instruments;
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
| 70 | צ'לו | מיתר |

**התוצאה: 7 שורות**

> 💡 גרש בתוך טקסט כותבים פעמיים: `'צ''לו'`.

</div>

<div dir="rtl">

### 2. 🟢 הוסיפו תלמיד חדש: 211, 'נדים', 'סעב', 2013, עיר 5.

</div>

```sql
INSERT INTO Pupils VALUES (211, 'נדים', 'סעב', 2013, 5);
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Pupils WHERE PupilId = 211;
```

<div dir="rtl">

| PupilId | FirstName | LastName | BirthYear | HomeTown |
|---|---|---|---|---|
| 211 | נדים | סעב | 2013 | 5 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 3. 🟢 עדכנו את המחיר של המורה 5 ל‑105.

</div>

```sql
UPDATE Teachers
SET    HourRate = 105
WHERE  TeacherCode = 5;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT TeacherName, HourRate FROM Teachers WHERE TeacherCode = 5;
```

<div dir="rtl">

| TeacherName | HourRate |
|---|---|
| יוסי פרץ | 105 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 4. 🟢 מחקו את הלוקר מספר 4.

</div>

```sql
DELETE FROM Lockers
WHERE  LockerNum = 4;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Lockers;
```

<div dir="rtl">

| LockerNum | LockerPupil | LockerFloor |
|---|---|---|
| 1 | 202 | 1 |
| 2 | 205 | 1 |
| 3 | 207 | 2 |
| 5 | 201 | 2 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 5. 🟡 הוסיפו מורה חדשה: 7, 'לינה חורי', מלמדת חליל (50), 125 לשעה, **בלי טלפון**. (רשמו את שמות העמודות)

</div>

```sql
INSERT INTO Teachers (TeacherCode, TeacherName, TeachInst, HourRate)
VALUES (7, 'לינה חורי', 50, 125);
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Teachers;
```

<div dir="rtl">

| TeacherCode | TeacherName | TeachInst | HourRate | TeacherPhone |
|---|---|---|---|---|
| 1 | סמיר חלבי | 60 | 120 | 050-1234567 |
| 2 | רונית לוי | 10 | 150 | 052-2345678 |
| 3 | אמיר עזאם | 20 | 110 | *NULL* |
| 4 | דנה כהן | 30 | 140 | 054-4567890 |
| 5 | יוסי פרץ | 40 | 100 | 053-5678901 |
| 6 | נור מנסור | 10 | 130 | *NULL* |
| 7 | לינה חורי | 50 | 125 | *NULL* |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 6. 🟡 כל התלמידים המתחילים עוברים לרמת 'ממשיך'.

</div>

```sql
UPDATE Registrations
SET    PupilLevel = 'ממשיך'
WHERE  PupilLevel = 'מתחיל';
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT PupilLevel, COUNT(*) AS Regs FROM Registrations GROUP BY PupilLevel;
```

<div dir="rtl">

| PupilLevel | Regs |
|---|---|
| ממשיך | 11 |
| מתקדם | 3 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 7. 🟡 הנחה של 5% על כל הרישומים של שנת 2025.

</div>

```sql
UPDATE Registrations
SET    MonthlyFee = MonthlyFee * 0.95
WHERE  RegYear = 2025;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT RegPupil, RegYear, MonthlyFee FROM Registrations WHERE RegYear = 2025;
```

<div dir="rtl">

| RegPupil | RegYear | MonthlyFee |
|---|---|---|
| 201 | 2025 | 266 |
| 203 | 2025 | 285 |
| 204 | 2025 | 361 |
| 207 | 2025 | 332.5 |
| 209 | 2025 | 361 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 8. 🟡 למורים שאין להם טלפון — רשמו את הטלפון '000-0000000'.

</div>

```sql
UPDATE Teachers
SET    TeacherPhone = '000-0000000'
WHERE  TeacherPhone IS NULL;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT TeacherName, TeacherPhone FROM Teachers;
```

<div dir="rtl">

| TeacherName | TeacherPhone |
|---|---|
| סמיר חלבי | 050-1234567 |
| רונית לוי | 052-2345678 |
| אמיר עזאם | 000-0000000 |
| דנה כהן | 054-4567890 |
| יוסי פרץ | 053-5678901 |
| נור מנסור | 000-0000000 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 9. 🔴 מחקו את כל הרישומים של המורה 'יוסי פרץ' (בלי לכתוב את הקוד שלו — עם תת‑שאילתה).

</div>

```sql
DELETE FROM Registrations
WHERE  RegTeacher = (SELECT TeacherCode FROM Teachers
                     WHERE  TeacherName = 'יוסי פרץ');
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT COUNT(*) AS RegsLeft FROM Registrations;
```

<div dir="rtl">

| RegsLeft |
|---|
| 11 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 10. 🔴 העלו ב‑20 את התשלום של כל הרישומים של תלמידים שגרים בעכו.

</div>

```sql
UPDATE Registrations
SET    MonthlyFee = MonthlyFee + 20
WHERE  RegPupil IN (SELECT PupilId FROM Pupils, Cities
                    WHERE  HomeTown = CityCode AND CityName = 'עכו');
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT RegPupil, MonthlyFee FROM Registrations WHERE RegPupil IN (204, 205, 210);
```

<div dir="rtl">

| RegPupil | MonthlyFee |
|---|---|
| 204 | 400 |
| 204 | 380 |
| 205 | 360 |
| 210 | 340 |
| 210 | 320 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 11. 🟢 הוסיפו את העיר 'סח'נין' בקוד 6.

</div>

```sql
INSERT INTO Cities VALUES (6, 'סח''נין');
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Cities;
```

<div dir="rtl">

| CityCode | CityName |
|---|---|
| 1 | ירכא |
| 2 | עכו |
| 3 | כרמיאל |
| 4 | נהריה |
| 5 | מעלות |
| 6 | סח'נין |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 12. 🟢 שנו את שם הכלי 'עוד' ל‑'עוד ערבי'.

</div>

```sql
UPDATE Instruments
SET    InstName = 'עוד ערבי'
WHERE  InstCode = 60;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Instruments;
```

<div dir="rtl">

| InstCode | InstName | InstFamily |
|---|---|---|
| 10 | פסנתר | קלידים |
| 20 | גיטרה | מיתר |
| 30 | כינור | מיתר |
| 40 | תופים | הקשה |
| 50 | חליל | נשיפה |
| 60 | עוד ערבי | מיתר |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 13. 🟡 הוסיפו רישום חדש: התלמיד 206 לומד אצל המורה 2, בשנת 2026, ברמת 'מתחיל', 390 לחודש.

</div>

```sql
INSERT INTO Registrations VALUES (206, 2, 2026, 'מתחיל', 390);
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Registrations WHERE RegPupil = 206;
```

<div dir="rtl">

| RegPupil | RegTeacher | RegYear | PupilLevel | MonthlyFee |
|---|---|---|---|---|
| 206 | 2 | 2026 | מתחיל | 390 |
| 206 | 5 | 2024 | ממשיך | 280 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 14. 🟡 העבירו את כל הלוקרים מקומה 1 לקומה 3.

</div>

```sql
UPDATE Lockers
SET    LockerFloor = 3
WHERE  LockerFloor = 1;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Lockers;
```

<div dir="rtl">

| LockerNum | LockerPupil | LockerFloor |
|---|---|---|
| 1 | 202 | 3 |
| 2 | 205 | 3 |
| 3 | 207 | 2 |
| 4 | 210 | 2 |
| 5 | 201 | 2 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 15. 🟡 מחקו את כל הרישומים שהתשלום בהם נמוך מ‑300.

</div>

```sql
DELETE FROM Registrations
WHERE  MonthlyFee < 300;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT RegPupil, MonthlyFee FROM Registrations;
```

<div dir="rtl">

| RegPupil | MonthlyFee |
|---|---|
| 201 | 320 |
| 202 | 400 |
| 203 | 300 |
| 204 | 360 |
| 204 | 380 |
| 205 | 340 |
| 207 | 350 |
| 207 | 320 |
| 208 | 300 |
| 209 | 380 |
| 210 | 300 |
| 210 | 320 |

**התוצאה: 12 שורות**

</div>

<div dir="rtl">

### 16. 🔴 עדכנו בבת אחת: המורה 3 מקבל טלפון '050-3333333' ומחיר 115.

</div>

```sql
UPDATE Teachers
SET    TeacherPhone = '050-3333333', HourRate = 115
WHERE  TeacherCode = 3;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Teachers WHERE TeacherCode = 3;
```

<div dir="rtl">

| TeacherCode | TeacherName | TeachInst | HourRate | TeacherPhone |
|---|---|---|---|---|
| 3 | אמיר עזאם | 20 | 115 | 050-3333333 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 17. 🔴 מחקו את הלוקרים של התלמידים שנולדו לפני 2010.

</div>

```sql
DELETE FROM Lockers
WHERE  LockerPupil IN (SELECT PupilId FROM Pupils WHERE BirthYear < 2010);
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Lockers;
```

<div dir="rtl">

| LockerNum | LockerPupil | LockerFloor |
|---|---|---|
| 1 | 202 | 1 |
| 3 | 207 | 2 |
| 5 | 201 | 2 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

---

## 🎓 בסגנון הבחינה — 📚 ספרייה עירונית

</div>

<div dir="rtl">

### 1. 🟢 הוסיפו קורא חדש: 511, 'ג'ני', 'נסאר', עיר 3, נולדה ב‑2008.

</div>

```sql
INSERT INTO Members VALUES (511, 'ג''ני', 'נסאר', 3, 2008);
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Members WHERE MemberId = 511;
```

<div dir="rtl">

| MemberId | FirstName | LastName | TownCode | BirthYear |
|---|---|---|---|---|
| 511 | ג'ני | נסאר | 3 | 2008 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 2. 🟢 עדכנו שההשאלה 5 הוחזרה ב‑'2025-10-15'.

</div>

```sql
UPDATE Loans
SET    ReturnDate = '2025-10-15'
WHERE  LoanId = 5;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Loans WHERE LoanId = 5;
```

<div dir="rtl">

| LoanId | ReaderId | BookNum | LoanDate | ReturnDate |
|---|---|---|---|---|
| 5 | 504 | 207 | 2025-09-07 | 2025-10-15 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 3. 🟡 הגדילו ב‑10 את מספר העמודים של כל ספרי המתח.

</div>

```sql
UPDATE Books
SET    Pages = Pages + 10
WHERE  Genre = 'מתח';
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT Title, Pages FROM Books WHERE Genre = 'מתח';
```

<div dir="rtl">

| Title | Pages |
|---|---|
| רצח באוריינט אקספרס | 260 |
| ואז לא נשאר אף אחד | 270 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 4. 🟡 מחקו את כל ההשאלות שהוחזרו.

</div>

```sql
DELETE FROM Loans
WHERE  ReturnDate IS NOT NULL;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT COUNT(*) AS Left FROM Loans;
```

<div dir="rtl">

| Left |
|---|
| 8 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 5. 🔴 מחקו את כל ההשאלות של הקוראים מעכו.

</div>

```sql
DELETE FROM Loans
WHERE  ReaderId IN (SELECT MemberId FROM Members, Cities
                   WHERE  TownCode = CityCode AND CityName = 'עכו');
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT LoanId, ReaderId FROM Loans;
```

<div dir="rtl">

| LoanId | ReaderId |
|---|---|
| 1 | 501 |
| 2 | 501 |
| 3 | 502 |
| 4 | 503 |
| 7 | 502 |
| 8 | 506 |
| 9 | 507 |
| 10 | 501 |
| 11 | 508 |
| 13 | 503 |
| 14 | 509 |

**התוצאה: 11 שורות**

</div>

<div dir="rtl">

### 6. 🔴 השלימו את הפקודה שמשנה את הז'אנר של הספר 210 ל‑'מסה'.

</div>

```sql
UPDATE Books
SET    Genre = 'מסה'
WHERE  BookCode = 210;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT Title, Genre FROM Books WHERE BookCode = 210;
```

<div dir="rtl">

| Title | Genre |
|---|---|
| ספר הדקדוק הפנימי | מסה |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

---

## 🏠 תרגול נוסף — 🏫 בית הספר "עתיד"

</div>

<div dir="rtl">

### 1. 🟢 הוסיפו את העיר 'טמרה' בקוד 7.

</div>

```sql
INSERT INTO Cities VALUES (7, 'טמרה');
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Cities;
```

<div dir="rtl">

| CityCode | CityName |
|---|---|
| 1 | ירכא |
| 2 | עכו |
| 3 | כרמיאל |
| 4 | חיפה |
| 5 | נהריה |
| 6 | שפרעם |
| 7 | טמרה |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 2. 🟡 שבצו את התלמידה 1018 (`לינא`) לכיתה 104.

</div>

```sql
UPDATE Students
SET    ClassCode = 104
WHERE  StudentId = 1018;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT FirstName, ClassCode FROM Students WHERE StudentId = 1018;
```

<div dir="rtl">

| FirstName | ClassCode |
|---|---|
| לינא | 104 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 3. 🟡 העלו ב‑5% את השכר של כל המורים למתמטיקה.

</div>

```sql
UPDATE Teachers
SET    Salary = Salary * 1.05
WHERE  Subject = 'מתמטיקה';
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT FirstName, Subject, Salary FROM Teachers;
```

<div dir="rtl">

| FirstName | Subject | Salary |
|---|---|---|
| נביל | מתמטיקה | 15225 |
| רונית | אנגלית | 11200 |
| חוסאם | מחשבים | 12800 |
| אורלי | היסטוריה | 15300 |
| פאדי | ספורט | 9800 |
| גלית | מתמטיקה | 13755 |
| סמיר | ביולוגיה | 10400 |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 4. 🟡 מחקו את כל ההיעדרויות המאושרות.

</div>

```sql
DELETE FROM Absences
WHERE  Excused = 1;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT COUNT(*) AS Left FROM Absences;
```

<div dir="rtl">

| Left |
|---|
| 9 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 5. 🔴 פקטור: הוסיפו 5 נקודות לכל הציונים במקצוע 16, אבל לא מעבר ל‑100 (רמז: `MIN(Grade + 5, 100)`).

</div>

```sql
UPDATE Grades
SET    Grade = MIN(Grade + 5, 100)
WHERE  CourseCode = 16 AND Grade IS NOT NULL;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT StudentId, Term, Grade FROM Grades WHERE CourseCode = 16;
```

<div dir="rtl">

| StudentId | Term | Grade |
|---|---|---|
| 1003 | 1 | 66 |
| 1003 | 2 | 72 |
| 1004 | 1 | 53 |
| 1006 | 1 | 71 |
| 1009 | 1 | 59 |
| 1011 | 1 | 88 |
| 1012 | 1 | 47 |
| 1012 | 2 | 44 |
| 1015 | 1 | 64 |
| 1015 | 2 | 67 |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 6. 🟢 הוסיפו מקצוע חדש: 18, 'רובוטיקה', מורה 3, 2 שעות.

</div>

```sql
INSERT INTO Courses VALUES (18, 'רובוטיקה', 3, 2);
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Courses;
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
| 18 | רובוטיקה | 3 | 2 |

**התוצאה: 8 שורות**

</div>

<div dir="rtl">

### 7. 🟡 שבצו את הכיתה 104 לחדר 22.

</div>

```sql
UPDATE Classes
SET    RoomNumber = 22
WHERE  ClassCode = 104;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT * FROM Classes;
```

<div dir="rtl">

| ClassCode | ClassName | Grade | TeacherCode | RoomNumber |
|---|---|---|---|---|
| 101 | י1 | 10 | 1 | 12 |
| 102 | י2 | 10 | 2 | 14 |
| 103 | יא1 | 11 | 3 | 21 |
| 104 | יא2 | 11 | 6 | 22 |
| 105 | יב1 | 12 | 4 | 31 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 8. 🟡 תנו ציון 0 לכל מי שלא נבחן (Grade הוא NULL).

</div>

```sql
UPDATE Grades
SET    Grade = 0
WHERE  Grade IS NULL;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT StudentId, CourseCode, Grade FROM Grades WHERE Grade = 0;
```

<div dir="rtl">

| StudentId | CourseCode | Grade |
|---|---|---|
| 1004 | 14 | 0 |
| 1009 | 12 | 0 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 9. 🔴 מחקו את כל ההיעדרויות של תלמידי הכיתה 104.

</div>

```sql
DELETE FROM Absences
WHERE  StudentId IN (SELECT StudentId FROM Students WHERE ClassCode = 104);
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT COUNT(*) AS Left FROM Absences;
```

<div dir="rtl">

| Left |
|---|
| 11 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../11-views/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../13-create-alter-drop/solutions.md)

</div>
