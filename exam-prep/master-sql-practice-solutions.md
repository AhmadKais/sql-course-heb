<div dir="rtl">

# ✅ פתרונות מלאים: מאגר שאילתות ותרגול מהקל למתקדם

> **הפתרונות לכל התרגילים מתוך [מאגר השאילתות (master-sql-practice.md)](master-sql-practice.md)**
> 
> בכל סעיף תמצאו: את **שאילתת ה‑SQL המדויקת**, את **הפלט האמיתי שהתקבל**, ו**הסבר קצר על החוקים והדגשים לבחינה**.

---

## 🟢 פתרונות רמה 1: שליפה בסיסית וסינון פשוט

### פתרון 1.1:
```sql
SELECT FirstName, LastName
FROM Pupils;
```
**הסבר:** בחירת העמודות המבוקשות מתוך הטבלה Pupils ללא סינון (מחזיר את כל 10 התלמידים).

---

### פתרון 1.2:
```sql
SELECT *
FROM Instruments
WHERE InstFamily = 'מיתר';
```
**פלט:** 3 שורות: גיטרה (20), כינור (30), עוד (60).
**הסבר:** כוכבית `*` שולפת את כל העמודות; טקסט נכתב בתוך מירכאות.

---

### פתרון 1.3:
```sql
SELECT TeacherName, HourRate
FROM Teachers
WHERE HourRate > 120;
```
**פלט:** רונית לוי (150), דנה כהן (140), נור מנסור (130).
**דגש לבחינה:** "גבוה מ‑120" פירושו `>` ולא `>=`. סמיר חלבי (120) אינו נכלל!

---

### פתרון 1.4:
```sql
SELECT TeacherName, HourRate * 0.9 AS DiscountedRate
FROM Teachers;
```
**הסבר:** הנחה של 10% משאירה 90% מהמחיר (`* 0.9`). המילה `AS` מעניקה כותרת חדשה לעמודה המחושבת.

---

### פתרון 1.5:
```sql
SELECT DISTINCT HomeTown
FROM Pupils;
```
**פלט:** 1, 2, 3, 4.
**הסבר:** `DISTINCT` מסיר כפילויות ומציג כל קוד עיר פעם אחת בלבד.

---

### פתרון 1.6:
```sql
SELECT FirstName, LastName, BirthYear
FROM Pupils
ORDER BY BirthYear DESC;
```
**הסבר:** שנת לידה גדולה יותר שייכת לתלמיד צעיר יותר. לכן מיון מהצעיר למבוגר דורש `DESC` (סדר יורד: 2014, 2013, 2012...).

---

### פתרון 1.7:
```sql
SELECT *
FROM Registrations
ORDER BY MonthlyFee DESC, RegYear ASC;
```
**הסבר:** מיון רב‑שדות: קודם ממיינים לפי המחיר מהגבוה לנמוך (`DESC`), ולשוויון — לפי השנה מהישן לחדש (`ASC`).

---

### פתרון 1.8:
```sql
SELECT InstName
FROM Instruments
ORDER BY InstName ASC;
```
**פלט:** גיטרה, חליל, כינור, עוד, פסנתר, תופים.
**הסבר:** ברירת המחדל של `ORDER BY` היא סדר עולה (`ASC`).

---

## 🟢 פתרונות רמה 2: תנאים מורכבים ולוגיקה

### פתרון 2.1:
```sql
SELECT FirstName, LastName
FROM Pupils
WHERE BirthYear >= 2011 AND HomeTown = 1;
```
**פלט:** אדם חלבי (2012), כרים עזאם (2013), ליאן קבלאן (2011).

---

### פתרון 2.2:
```sql
SELECT TeacherName, HourRate
FROM Teachers
WHERE HourRate < 110 OR HourRate > 140;
```
**פלט:** יוסי פרץ (100), רונית לוי (150).
**הסבר:** האופרטור `OR` מחזיר שורה שעונה על אחד מהתנאים לפחות.

---

### פתרון 2.3:
```sql
SELECT FirstName, BirthYear
FROM Pupils
WHERE BirthYear BETWEEN 2010 AND 2012;
```
**דגש לבחינה:** `BETWEEN` ב‑SQL **כולל תמיד את הקצוות** (זהה ל‑`>= 2010 AND <= 2012`).

---

### פתרון 2.4:
```sql
SELECT TeacherName, TeachInst
FROM Teachers
WHERE TeachInst IN (10, 20, 30);
```
**הסבר:** `IN` מהווה קיצור נוח ויעיל במקום שרשור של מספר תנאי `OR`.

---

### פתרון 2.5:
```sql
SELECT FirstName, LastName
FROM Pupils
WHERE LastName LIKE 'ח%';
```
**פלט:** חלבי, חורי, חסון.
**הסבר:** התו `%` מייצג רצף של אפס תווים או יותר.

---

### פתרון 2.6:
```sql
SELECT TeacherName
FROM Teachers
WHERE TeacherName LIKE '%כהן%';
```
**פלט:** דנה כהן.
**הסבר:** `%טקסט%` בודק אם המחרוזת מופיעה בכל מקום שהוא בתוך השדה.

---

### פתרון 2.7:
```sql
SELECT TeacherName
FROM Teachers
WHERE TeacherPhone IS NULL;
```
**דגש קריטי לבחינה:** בודקים היעדר ערך אך ורק עם **`IS NULL`**! כתיבה כמו `= NULL` היא שגיאה לוגית ולא תחזיר תוצאות לעולם.

---

### פתרון 2.8:
```sql
SELECT TeacherName
FROM Teachers
WHERE TeacherPhone IS NOT NULL;
```

---

### פתרון 2.9:
```sql
SELECT *
FROM Registrations
WHERE PupilLevel <> 'מתחיל' AND MonthlyFee BETWEEN 300 AND 360;
```
**הסבר:** ב‑SQL שונה מסומן ב‑`<>` (או `!=`).

---

### פתרון 2.10:
```sql
SELECT FirstName, HomeTown, BirthYear
FROM Pupils
WHERE (HomeTown = 1 OR HomeTown = 2) AND BirthYear > 2011;
```
**פלט:** אדם (עיר 1, 2012), כרים (עיר 1, 2013).
**מלכודת נפוצה בבחינה:** לא לשכוח סוגריים מסביב ל‑OR! ללא סוגריים, ה‑`AND` יתבצע קודם ויעוות לחלוטין את התוצאה.

---

## 🟡 פתרונות רמה 3: פונקציות ב‑SQL

### פתרון 3.1:
```sql
SELECT COUNT(*) AS TotalRegistrations
FROM Registrations;
```
**פלט:** `14`.

---

### פתרון 3.2:
```sql
SELECT COUNT(TeacherPhone) AS TeachersWithPhone
FROM Teachers;
```
**פלט:** `4`.
**הסבר:** מתוך 6 מורים, לשניים יש NULL בשדה הטלפון. `COUNT(עמודה)` סופר רק שורות שאינן NULL.

---

### פתרון 3.3:
```sql
SELECT COUNT(DISTINCT HomeTown) AS UniqueCities
FROM Pupils;
```
**פלט:** `4`.
**הסבר:** תלמידים גרים ב‑4 ערים שונות (1, 2, 3, 4). בעיר 5 אין תלמידים.

---

### פתרון 3.4:
```sql
SELECT AVG(HourRate) AS AvgRate,
       MAX(HourRate) AS MaxRate,
       MIN(HourRate) AS MinRate,
       SUM(HourRate) AS TotalRate
FROM Teachers;
```
**פלט:** `AvgRate = 125.0`, `MaxRate = 150`, `MinRate = 100`, `TotalRate = 750`.

---

### פתרון 3.5:
```sql
SELECT ROUND(AVG(MonthlyFee), 2) AS AvgFeeRounded
FROM Registrations;
```
**פלט:** `330.71`.

---

### פתרון 3.6:
```sql
SELECT CityName AS City, LENGTH(CityName) AS CharsCount
FROM Cities;
```

---

### פתרון 3.7:
```sql
SELECT FirstName || ' ' || LastName AS PupilFullName
FROM Pupils;
```

---

### פתרון 3.8:
```sql
SELECT TeacherName, COALESCE(TeacherPhone, 'לא נמסר') AS Phone
FROM Teachers;
```

---

### פתרון 3.9:
```sql
SELECT SUM(MonthlyFee) AS TotalFees2024
FROM Registrations
WHERE RegYear = 2024;
```
**פלט:** `1240`.
**הסבר:** הרישומים של 2024: 320 + 280 + 320 + 320 = 1240.

---

### פתרון 3.10:
```sql
SELECT COUNT(DISTINCT RegPupil) AS PupilsCount2025
FROM Registrations
WHERE RegYear = 2025;
```
**פלט:** `5`.
**הסבר:** 5 תלמידים שונים נרשמו בשנת 2025.

---

## 🟡 פתרונות רמה 4: קיבוץ נתונים ותנאי קבוצה (GROUP BY & HAVING)

### פתרון 4.1:
```sql
SELECT PupilLevel, COUNT(*) AS TotalInLevel
FROM Registrations
GROUP BY PupilLevel;
```
**פלט:** ממשיך (6), מתחיל (5), מתקדם (3).

---

### פתרון 4.2:
```sql
SELECT HomeTown, COUNT(*) AS PupilsCount
FROM Pupils
GROUP BY HomeTown
HAVING COUNT(*) >= 3;
```
**פלט:** עיר 1 (3 תלמידים), עיר 2 (3 תלמידים).

---

### פתרון 4.3:
```sql
SELECT RegTeacher, AVG(MonthlyFee) AS AvgFee
FROM Registrations
GROUP BY RegTeacher
ORDER BY AvgFee DESC;
```
**פלט:**
- מורה 2: ממוצע 386.67
- מורה 4: ממוצע 355.0
- מורה 3: ממוצע 320.0
- מורה 1: ממוצע 313.33
- מורה 5: ממוצע 286.67

---

### פתרון 4.4:
```sql
SELECT RegTeacher, SUM(MonthlyFee) AS TotalIncome
FROM Registrations
GROUP BY RegTeacher
HAVING SUM(MonthlyFee) > 900;
```
**פלט:**
- מורה 1: 940
- מורה 2: 1160
- מורה 3: 960

---

### פתרון 4.5:
```sql
SELECT RegYear, COUNT(*) AS NumRegs, MAX(MonthlyFee) AS MaxFee
FROM Registrations
GROUP BY RegYear;
```

---

### פתרון 4.6:
```sql
SELECT TeachInst, COUNT(*) AS TeachersCount
FROM Teachers
GROUP BY TeachInst
HAVING COUNT(*) > 1;
```
**פלט:** כלי 10 (פסנתר), 2 מורים.

---

### פתרון 4.7:
```sql
SELECT RegTeacher, AVG(MonthlyFee) AS AvgFee
FROM Registrations
WHERE RegYear >= 2024
GROUP BY RegTeacher
HAVING AVG(MonthlyFee) > 310;
```
**הסבר:** 
- `WHERE RegYear >= 2024` מסנן תחילה את השורות (רק מ‑2024 ואילך).
- `GROUP BY RegTeacher` מקבץ לפי מורה.
- `HAVING AVG(MonthlyFee) > 310` מסנן את המורים שהממוצע שלהם עולה על 310.

---

### פתרון 4.8:
**הסבר עקרוני לבחינה:** 
פקודת `WHERE` מסננת שורות יחידות לפני ביצוע הקיבוץ והחישוב, ובשלב זה פונקציית `COUNT(*)` עדיין אינה קיימת!
פקודת `HAVING` מתבצעת לאחר יצירת הקבוצות וחישוב הפונקציות המצרפיות, ולכן סינון על תוצאת פונקציית קיבוץ מתבצע אך ורק ב‑`HAVING`.

---

## 🟡 פתרונות רמה 5: חיבור טבלאות (צירופים — Joins)

### פתרון 5.1:
```sql
SELECT FirstName, CityName
FROM Pupils, Cities
WHERE HomeTown = CityCode;
```
*(או באמצעות תחביר `JOIN`: `SELECT FirstName, CityName FROM Pupils JOIN Cities ON HomeTown = CityCode;`)*

---

### פתרון 5.2:
```sql
SELECT TeacherName, InstName
FROM Teachers, Instruments
WHERE TeachInst = InstCode;
```

---

### פתרון 5.3:
```sql
SELECT FirstName, TeacherName, MonthlyFee
FROM Pupils, Teachers, Registrations
WHERE RegPupil = PupilId AND RegTeacher = TeacherCode;
```
**דגש לבחינה:** צירוף של 3 טבלאות דורש תמיד **שני תנאי חיבור** ב‑`WHERE` המחוברים ב‑`AND`!

---

### פתרון 5.4:
```sql
SELECT FirstName, LockerNum
FROM Pupils, Lockers
WHERE PupilId = LockerPupil AND LockerFloor = 2;
```
**פלט:** אדם (5), ליאן (3), יואב (4).

---

### פתרון 5.5:
```sql
SELECT FirstName, BirthYear
FROM Pupils, Cities
WHERE HomeTown = CityCode AND CityName = 'עכו';
```
**פלט:** שירה (2011), רמי (2009), יואב (2009).

---

### פתרון 5.6:
```sql
SELECT InstName, TeacherName, HourRate
FROM Instruments, Teachers
WHERE TeachInst = InstCode
ORDER BY InstName ASC;
```

---

### פתרון 5.7:
```sql
SELECT FirstName, LockerNum
FROM Pupils
LEFT JOIN Lockers ON PupilId = LockerPupil;
```
**הסבר:** `LEFT JOIN` שומר את כל הרשומות מטבלת התלמידים (שמאל). תלמיד ללא לוקר יוצג עם `NULL` בעמודת הלוקר.

---

### פתרון 5.8:
```sql
SELECT Cities.CityName, COUNT(Pupils.PupilId) AS TotalPupils
FROM Cities
LEFT JOIN Pupils ON Cities.CityCode = Pupils.HomeTown
GROUP BY Cities.CityCode, Cities.CityName;
```
**פלט:** ירכא (3), עכו (3), כרמיאל (2), נהריה (2), מעלות (0).
**הסבר:** חובה להשתמש ב‑`COUNT(PupilId)` ולא ב‑`COUNT(*)`, כדי שמעלות תקבל 0 ולא 1!

---

## 🔴 פתרונות רמה 6: שאילתות מקוננות (Subqueries)

### פתרון 6.1:
```sql
SELECT TeacherName
FROM Teachers
WHERE TeacherCode NOT IN (SELECT RegTeacher FROM Registrations);
```
**פלט:** נור מנסור.
**הסבר:** נור מנסור (קוד 6) לא מופיעה באף שורה בטבלת Registrations.

---

### פתרון 6.2:
```sql
SELECT FirstName, LastName
FROM Pupils
WHERE PupilId NOT IN (SELECT LockerPupil FROM Lockers WHERE LockerPupil IS NOT NULL);
```
**פלט:** כרים, שירה, תמר, עומר, סאלי.

---

### פתרון 6.3:
```sql
SELECT TeacherName, HourRate
FROM Teachers
WHERE HourRate > (SELECT AVG(HourRate) FROM Teachers);
```
**פלט:** רונית לוי (150), דנה כהן (140), נור מנסור (130). הממוצע הוא 125.

---

### פתרון 6.4:
```sql
SELECT FirstName, LastName, BirthYear
FROM Pupils
WHERE BirthYear = (SELECT MAX(BirthYear) FROM Pupils);
```
**פלט:** סאלי חסון (שנת 2014).

---

### פתרון 6.5:
```sql
SELECT FirstName, LastName
FROM Pupils
WHERE PupilId IN (
    SELECT RegPupil 
    FROM Registrations 
    WHERE MonthlyFee = (SELECT MAX(MonthlyFee) FROM Registrations)
);
```
**פלט:** מאיה כהן (משלמת 400 ש"ח).

---

### פתרון 6.6:
```sql
SELECT InstName
FROM Instruments
WHERE InstCode NOT IN (SELECT TeachInst FROM Teachers);
```
**פלט:** חליל (קוד 50). אף מורה לא מלמד חליל בבית הספר.

---

### פתרון 6.7:
```sql
SELECT FirstName, PupilLevel, MonthlyFee
FROM Pupils, Registrations R1
WHERE PupilId = RegPupil
  AND MonthlyFee > (
      SELECT AVG(MonthlyFee) 
      FROM Registrations R2 
      WHERE R2.PupilLevel = R1.PupilLevel
  );
```

---

## 🔴 פתרונות רמה 7: שאילתות שמורות ותת‑שאילתה ב‑FROM

### פתרון 7.1:
```sql
SELECT TeacherName, PupilCount
FROM Teachers, Q1
WHERE TeacherCode = RegTeacher;
```

---

### פתרון 7.2:
```sql
SELECT TeacherName
FROM Teachers, Q1
WHERE TeacherCode = RegTeacher AND PupilCount >= 3;
```
**פלט:** סמיר חלבי, רונית לוי, אמיר עזאם, יוסי פרץ.

---

### פתרון 7.3:
```sql
SELECT MAX(AvgFee) AS TopAvg
FROM (
    SELECT PupilLevel, AVG(MonthlyFee) AS AvgFee
    FROM Registrations
    GROUP BY PupilLevel
);
```
**פלט:** `346.666...` (רמת מתקדם).

---

## 🟡-🔴 פתרונות רמה 8: שינוי נתונים ומבנה (DML & DDL)

### פתרון 8.1:
```sql
INSERT INTO Cities (CityCode, CityName)
VALUES (6, 'חיפה');
```

---

### פתרון 8.2:
```sql
INSERT INTO Pupils (PupilId, FirstName, LastName, BirthYear, HomeTown)
VALUES (211, 'דן', 'לוי', 2013, 6);
```
**דגש לבחינה:** חובה קודם להכניס את העיר ל‑Cities (פתרון 8.1), ורק אחר כך את התלמיד שמפנה אליה במפתח זר!

---

### פתרון 8.3:
```sql
UPDATE Teachers
SET HourRate = 120
WHERE TeacherCode = 5;
```

---

### פתרון 8.4:
```sql
UPDATE Registrations
SET MonthlyFee = MonthlyFee * 1.10
WHERE PupilLevel = 'מתקדם';
```

---

### פתרון 8.5:
```sql
DELETE FROM Registrations
WHERE RegYear < 2023;
```

---

### פתרון 8.6:
```sql
ALTER TABLE Pupils
ADD Email TEXT;
```

---

### פתרון 8.7:
```sql
ALTER TABLE Teachers
DROP COLUMN TeacherPhone;
```

---

### פתרון 8.8:
- **`DELETE FROM Lockers;`** — מוחקת את כל **הנתונים (השורות)** בטבלה, אך מבנה הטבלה נשאר קיים בבסיס הנתונים (הטבלה ריקה). זוהי פקודת **DML**.
- **`DROP TABLE Lockers;`** — מוחקת את **הטבלה כולה** כולל המבנה וההגדרות שלה מתוך מסד הנתונים. זוהי פקודת **DDL**.

---

## 🎯 פתרונות רמה 9: סימולציית הבחינה הרשמית

### פתרון 9.1: זיהוי טבלה מתקבלת
**התשובה הנכונה:** **אפשרות 1**.
**הסבר:**
- מורים עם תעריף שעה `>= 130`: רונית לוי (150, פסנתר), דנה כהן (140, כינור), נור מנסור (130, פסנתר).
- התנאי כולל את 130 (`>=`).
- המיון הוא לפי תעריף יורד (`ORDER BY HourRate DESC`), ולכן הסדר הוא: 150, 140, 130.

---

### פתרון 9.2: השלמת ערכים מספריים
**התשובה:**
- **`Cnt = 5`** (נרשמו 5 תלמידים בשנת 2025: תלמידים 201, 203, 204, 207, 209).
- **`MinF = 280`** (התשלום הנמוך ביותר ב‑2025).
- **`MaxF = 380`** (התשלום הגבוה ביותר ב‑2025).

---

### פתרון 9.3: השלמת פקודות
```sql
SELECT CityName, COUNT(*) AS NumPupils
FROM Pupils, Cities
WHERE HomeTown = CityCode
GROUP BY CityName
HAVING COUNT(*) >= 3;
```
**מילים שהושלמו:** `HomeTown`, `CityCode`, `CityName`, `HAVING`.

---

### פתרון 9.4: ניתוח פלט
**התשובה הנכונה:** **שאילתה 1** (`SELECT TeacherName FROM Teachers WHERE HourRate > 130;`).
**פסילת המסיחים:**
- שאילתה 2 (`>= 130`): כוללת גם את נור מנסור (130), ולכן הייתה מחזירה 3 שורות ולא 2.
- שאילתה 3 (`BETWEEN 130 AND 150`): כוללת את 130, ושוב נור מנסור הייתה מופיעה.
- שאילתה 4 (`TeacherPhone IS NULL`): דנה כהן ורונית לוי שתיהן בעלות טלפון רשום, ולכן התוצאה הייתה ריקה.

---

### פתרון 9.5: שאלת מפתחות וקשרים
1. **לא נכון:** הקשר בין Pupils ל‑Lockers הוא **1:1 (אחד לאחד)**, מאחר ששדה `LockerPupil` בטבלת Lockers מוגדר כ‑`UNIQUE`. לכל תלמיד יש לכל היותר לוקר אחד, ולכל לוקר תלמיד אחד.
2. **נכון:** בטבלת Registrations המפתח הראשי הוא מפתח מורכב של שני שדות: `(RegPupil, RegTeacher)`.
3. **לא נכון:** בטבלת Cities אין שום מפתח זר (היא טבלת עזר עצמאית). המפתח הזר נמצא בטבלת Pupils (`HomeTown` המפנה ל‑`CityCode`).
4. **נכון:** `TeachInst` בטבלת Teachers מפנה למפתח הראשי `InstCode` בטבלת Instruments (קשר 1:N).

</div>
