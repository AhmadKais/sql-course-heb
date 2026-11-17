<div dir="rtl">

# שיעור 12 — INSERT, UPDATE, DELETE — שינוי נתונים

[➡️ השיעור הקודם](../11-views/README.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../13-create-alter-drop/README.md)

> 🎯 **בשיעור הזה:** להוסיף שורות, לעדכן ערכים ולמחוק שורות — ולבדוק את התוצאה
>
> 🗄️ **בסיס הנתונים:** 🎵 [בית הספר למוזיקה "צלילים"](../../databases/music/) · ✅ [הפתרונות](solutions.md)

---

## 1️⃣ טוענים את בסיס הנתונים

פותחים את [OneCompiler — SQLite](https://onecompiler.com/sqlite), מדביקים את **כל** הקוד, ומתחתיו כותבים את השאילתות.

</div>

<details>
<summary>📥 <b>לחצו כאן לקוד שבונה את בסיס הנתונים 🎵 בית הספר למוזיקה "צלילים"</b> — מעתיקים הכול ומדביקים ב‑OneCompiler</summary>

```sql
-- ============================================================
--  בית הספר למוזיקה "צלילים"  ·  בסיס נתונים לתרגול לפי ההנחיות של תשפ"ז
--  3 טבלאות ראשיות (Pupils, Teachers, Registrations) ו-3 טבלאות עזר קטנות
--  (Cities, Instruments, Lockers). לכל שדה יש שם ייחודי בכל בסיס הנתונים.
--  הדביקו את כל הקובץ ב-OneCompiler, לחצו Run, וכתבו את השאילתות מתחת.
-- ============================================================
DROP TABLE IF EXISTS Lockers;
DROP TABLE IF EXISTS Registrations;
DROP TABLE IF EXISTS Pupils;
DROP TABLE IF EXISTS Teachers;
DROP TABLE IF EXISTS Instruments;
DROP TABLE IF EXISTS Cities;

-- helper table
CREATE TABLE Cities (
  CityCode  INTEGER PRIMARY KEY,
  CityName  TEXT NOT NULL
);
INSERT INTO Cities VALUES (1, 'ירכא');
INSERT INTO Cities VALUES (2, 'עכו');
INSERT INTO Cities VALUES (3, 'כרמיאל');
INSERT INTO Cities VALUES (4, 'נהריה');
INSERT INTO Cities VALUES (5, 'מעלות');

-- helper table
CREATE TABLE Instruments (
  InstCode    INTEGER PRIMARY KEY,
  InstName    TEXT NOT NULL,
  InstFamily  TEXT NOT NULL            -- מיתר / קלידים / הקשה / נשיפה
);
INSERT INTO Instruments VALUES (10, 'פסנתר', 'קלידים');
INSERT INTO Instruments VALUES (20, 'גיטרה', 'מיתר');
INSERT INTO Instruments VALUES (30, 'כינור', 'מיתר');
INSERT INTO Instruments VALUES (40, 'תופים', 'הקשה');
INSERT INTO Instruments VALUES (50, 'חליל',  'נשיפה');
INSERT INTO Instruments VALUES (60, 'עוד',   'מיתר');

-- main table
CREATE TABLE Teachers (
  TeacherCode   INTEGER PRIMARY KEY,
  TeacherName   TEXT NOT NULL,
  TeachInst     INTEGER REFERENCES Instruments(InstCode),
  HourRate      INTEGER NOT NULL,      -- NIS per lesson hour
  TeacherPhone  TEXT                   -- NULL = no phone number
);
INSERT INTO Teachers VALUES (1, 'סמיר חלבי',   60, 120, '050-1234567');
INSERT INTO Teachers VALUES (2, 'רונית לוי',    10, 150, '052-2345678');
INSERT INTO Teachers VALUES (3, 'אמיר עזאם',   20, 110, NULL);
INSERT INTO Teachers VALUES (4, 'דנה כהן',      30, 140, '054-4567890');
INSERT INTO Teachers VALUES (5, 'יוסי פרץ',     40, 100, '053-5678901');
INSERT INTO Teachers VALUES (6, 'נור מנסור',    10, 130, NULL);

-- main table
CREATE TABLE Pupils (
  PupilId    INTEGER PRIMARY KEY,
  FirstName  TEXT NOT NULL,
  LastName   TEXT NOT NULL,
  BirthYear  INTEGER,
  HomeTown   INTEGER REFERENCES Cities(CityCode)
);
INSERT INTO Pupils VALUES (201, 'אדם',   'חלבי',  2012, 1);
INSERT INTO Pupils VALUES (202, 'מאיה',  'כהן',   2010, 3);
INSERT INTO Pupils VALUES (203, 'כרים',  'עזאם',  2013, 1);
INSERT INTO Pupils VALUES (204, 'שירה',  'לוי',   2011, 2);
INSERT INTO Pupils VALUES (205, 'רמי',   'חורי',  2009, 2);
INSERT INTO Pupils VALUES (206, 'תמר',   'אברהם', 2012, 4);
INSERT INTO Pupils VALUES (207, 'ליאן',  'קבלאן', 2011, 1);
INSERT INTO Pupils VALUES (208, 'עומר',  'ביטון', 2010, 4);
INSERT INTO Pupils VALUES (209, 'סאלי',  'חסון',  2014, 3);
INSERT INTO Pupils VALUES (210, 'יואב',  'שושן',  2009, 2);

-- main table: which pupil learns with which teacher (many-to-many)
CREATE TABLE Registrations (
  RegPupil    INTEGER REFERENCES Pupils(PupilId),
  RegTeacher  INTEGER REFERENCES Teachers(TeacherCode),
  RegYear     INTEGER NOT NULL,
  PupilLevel  TEXT NOT NULL,           -- מתחיל / ממשיך / מתקדם
  MonthlyFee  INTEGER NOT NULL,        -- NIS per month
  PRIMARY KEY (RegPupil, RegTeacher)
);
INSERT INTO Registrations VALUES (201, 1, 2024, 'ממשיך',  320);
INSERT INTO Registrations VALUES (201, 5, 2025, 'מתחיל',  280);
INSERT INTO Registrations VALUES (202, 2, 2022, 'מתקדם',  400);
INSERT INTO Registrations VALUES (203, 1, 2025, 'מתחיל',  300);
INSERT INTO Registrations VALUES (204, 4, 2023, 'ממשיך',  360);
INSERT INTO Registrations VALUES (204, 2, 2025, 'מתחיל',  380);
INSERT INTO Registrations VALUES (205, 3, 2021, 'מתקדם',  340);
INSERT INTO Registrations VALUES (206, 5, 2024, 'ממשיך',  280);
INSERT INTO Registrations VALUES (207, 4, 2025, 'מתחיל',  350);
INSERT INTO Registrations VALUES (207, 1, 2024, 'ממשיך',  320);
INSERT INTO Registrations VALUES (208, 3, 2023, 'ממשיך',  300);
INSERT INTO Registrations VALUES (209, 2, 2025, 'מתחיל',  380);
INSERT INTO Registrations VALUES (210, 5, 2022, 'מתקדם',  300);
INSERT INTO Registrations VALUES (210, 3, 2024, 'ממשיך',  320);

-- helper table: each locker belongs to at most one pupil, and each pupil has at most one locker (1:1)
CREATE TABLE Lockers (
  LockerNum    INTEGER PRIMARY KEY,
  LockerPupil  INTEGER UNIQUE REFERENCES Pupils(PupilId),
  LockerFloor  INTEGER NOT NULL
);
INSERT INTO Lockers VALUES (1, 202, 1);
INSERT INTO Lockers VALUES (2, 205, 1);
INSERT INTO Lockers VALUES (3, 207, 2);
INSERT INTO Lockers VALUES (4, 210, 2);
INSERT INTO Lockers VALUES (5, 201, 2);

SELECT COUNT(*) AS registrations_loaded FROM Registrations;
```

</details>


<div dir="rtl">

## 2️⃣ הטבלאות שעובדים איתן

> 🔑 = מפתח ראשי · 🔗 = מפתח זר. לכל הטבלאות: [בסיס הנתונים המלא](../../databases/music/)

**`Teachers`**

| TeacherCode 🔑 | TeacherName | TeachInst 🔗 | HourRate | TeacherPhone |
|---|---|---|---|---|
| 1 | סמיר חלבי | 60 | 120 | 050-1234567 |
| 2 | רונית לוי | 10 | 150 | 052-2345678 |
| 3 | אמיר עזאם | 20 | 110 | *NULL* |
| 4 | דנה כהן | 30 | 140 | 054-4567890 |
| 5 | יוסי פרץ | 40 | 100 | 053-5678901 |
| 6 | נור מנסור | 10 | 130 | *NULL* |

**`Pupils`**

| PupilId 🔑 | FirstName | LastName | BirthYear | HomeTown 🔗 |
|---|---|---|---|---|
| 201 | אדם | חלבי | 2012 | 1 |
| 202 | מאיה | כהן | 2010 | 3 |
| 203 | כרים | עזאם | 2013 | 1 |
| 204 | שירה | לוי | 2011 | 2 |
| 205 | רמי | חורי | 2009 | 2 |
| 206 | תמר | אברהם | 2012 | 4 |
| 207 | ליאן | קבלאן | 2011 | 1 |
| 208 | עומר | ביטון | 2010 | 4 |
| 209 | סאלי | חסון | 2014 | 3 |
| 210 | יואב | שושן | 2009 | 2 |

**`Registrations`**

| RegPupil 🔑🔗 | RegTeacher 🔑🔗 | RegYear | PupilLevel | MonthlyFee |
|---|---|---|---|---|
| 201 | 1 | 2024 | ממשיך | 320 |
| 201 | 5 | 2025 | מתחיל | 280 |
| 202 | 2 | 2022 | מתקדם | 400 |
| 203 | 1 | 2025 | מתחיל | 300 |
| 204 | 4 | 2023 | ממשיך | 360 |
| 204 | 2 | 2025 | מתחיל | 380 |
| 205 | 3 | 2021 | מתקדם | 340 |
| 206 | 5 | 2024 | ממשיך | 280 |
| 207 | 4 | 2025 | מתחיל | 350 |
| 207 | 1 | 2024 | ממשיך | 320 |
| 208 | 3 | 2023 | ממשיך | 300 |
| 209 | 2 | 2025 | מתחיל | 380 |
| 210 | 5 | 2022 | מתקדם | 300 |
| 210 | 3 | 2024 | ממשיך | 320 |

**`Instruments`**

| InstCode 🔑 | InstName | InstFamily |
|---|---|---|
| 10 | פסנתר | קלידים |
| 20 | גיטרה | מיתר |
| 30 | כינור | מיתר |
| 40 | תופים | הקשה |
| 50 | חליל | נשיפה |
| 60 | עוד | מיתר |

**`Cities`**

| CityCode 🔑 | CityName |
|---|---|
| 1 | ירכא |
| 2 | עכו |
| 3 | כרמיאל |
| 4 | נהריה |
| 5 | מעלות |

**`Lockers`**

| LockerNum 🔑 | LockerPupil 🔗 | LockerFloor |
|---|---|---|
| 1 | 202 | 1 |
| 2 | 205 | 1 |
| 3 | 207 | 2 |
| 4 | 210 | 2 |
| 5 | 201 | 2 |

---

## 3️⃣ התחביר בקצרה

</div>

```sql
-- add a row (values in the order of the columns)
INSERT INTO Cities VALUES (6, 'צפת');
INSERT INTO Teachers (TeacherCode, TeacherName, TeachInst, HourRate)
VALUES (7, 'לינה חורי', 50, 125);            -- missing columns -> NULL

-- change values
UPDATE Teachers
SET    HourRate = HourRate + 10
WHERE  TeachInst = 10;

-- delete rows
DELETE FROM Registrations
WHERE  RegYear < 2023;
```

<div dir="rtl">

- ⚠️ **`UPDATE` / `DELETE` בלי `WHERE` = כל השורות בטבלה!** תמיד כותבים קודם `SELECT` עם אותו `WHERE`, ובודקים.
- טקסט בגרשיים, מספר בלי. `NULL` — בלי גרשיים.
- אפשר לעדכן כמה עמודות יחד: `SET HourRate = 130, TeacherPhone = NULL`.
- אי אפשר למחוק שורה שמפתח זר מצביע עליה (כשהאילוצים פעילים), וגם אי אפשר להוסיף מפתח ראשי שכבר קיים.
- 🔄 התבלגן לכם? הדביקו מחדש את קוד בסיס הנתונים — הכול חוזר למצב ההתחלתי.

</div>

<div dir="rtl">

---

## 4️⃣ דוגמאות פתורות

> קראו את השאלה, נסו לכתוב בעצמכם, ורק אז הסתכלו על הפתרון והתוצאה.

</div>

<div dir="rtl">

### דוגמה 1: הוסיפו את העיר 'צפת' בקוד 6.

</div>

```sql
INSERT INTO Cities VALUES (6, 'צפת');
```

<div dir="rtl">

בדיקה — מה יש בטבלה אחרי הפקודה:

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
| 6 | צפת |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### דוגמה 2: העלו ב‑10 את המחיר לשעה של מורי הפסנתר (כלי 10).

</div>

```sql
UPDATE Teachers
SET    HourRate = HourRate + 10
WHERE  TeachInst = 10;
```

<div dir="rtl">

בדיקה — מה יש בטבלה אחרי הפקודה:

</div>

```sql
SELECT TeacherName, TeachInst, HourRate FROM Teachers;
```

<div dir="rtl">

| TeacherName | TeachInst | HourRate |
|---|---|---|
| סמיר חלבי | 60 | 120 |
| רונית לוי | 10 | 160 |
| אמיר עזאם | 20 | 110 |
| דנה כהן | 30 | 140 |
| יוסי פרץ | 40 | 100 |
| נור מנסור | 10 | 140 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### דוגמה 3: עדכנו את הטלפון של 'אמיר עזאם' ל‑'058-1112222'.

</div>

```sql
UPDATE Teachers
SET    TeacherPhone = '058-1112222'
WHERE  TeacherName = 'אמיר עזאם';
```

<div dir="rtl">

בדיקה — מה יש בטבלה אחרי הפקודה:

</div>

```sql
SELECT TeacherName, TeacherPhone FROM Teachers;
```

<div dir="rtl">

| TeacherName | TeacherPhone |
|---|---|
| סמיר חלבי | 050-1234567 |
| רונית לוי | 052-2345678 |
| אמיר עזאם | 058-1112222 |
| דנה כהן | 054-4567890 |
| יוסי פרץ | 053-5678901 |
| נור מנסור | *NULL* |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### דוגמה 4: מחקו את כל הרישומים משנים לפני 2023.

</div>

```sql
DELETE FROM Registrations
WHERE  RegYear < 2023;
```

<div dir="rtl">

בדיקה — מה יש בטבלה אחרי הפקודה:

</div>

```sql
SELECT RegPupil, RegTeacher, RegYear FROM Registrations;
```

<div dir="rtl">

| RegPupil | RegTeacher | RegYear |
|---|---|---|
| 201 | 1 | 2024 |
| 201 | 5 | 2025 |
| 203 | 1 | 2025 |
| 204 | 4 | 2023 |
| 204 | 2 | 2025 |
| 206 | 5 | 2024 |
| 207 | 4 | 2025 |
| 207 | 1 | 2024 |
| 208 | 3 | 2023 |
| 209 | 2 | 2025 |
| 210 | 3 | 2024 |

**התוצאה: 11 שורות**

</div>

<div dir="rtl">

---

## 5️⃣ שאלות: מה תחזיר השאילתה?

> בלי להריץ! כתבו על דף את הטבלה שתתקבל (או רק את מספר השורות). אחר כך הריצו ובדקו. התשובות ב[פתרונות](solutions.md).

</div>

<div dir="rtl">

**שאלה 1.** כמה שורות עודכנו? מה יחזור?

</div>

```sql
UPDATE Registrations SET MonthlyFee = 0 WHERE RegYear = 2030;
SELECT COUNT(*) FROM Registrations WHERE MonthlyFee = 0;
```

<div dir="rtl">

**שאלה 2.** כמה לוקרים נשארו?

</div>

```sql
DELETE FROM Lockers WHERE LockerFloor = 1;
SELECT COUNT(*) FROM Lockers;
```

<div dir="rtl">

---

## 6️⃣ תרגילים — 🎵 בית הספר למוזיקה "צלילים"

> כתבו שאילתה לכל סעיף והריצו. **🔢 מספר השורות הצפוי** עוזר לבדוק את עצמכם. 🟢 קל · 🟡 בינוני · 🔴 מאתגר

1. 🟢 הוסיפו את הכלי 'צ'לו' (קוד 70, משפחת 'מיתר'). _(🔍 משנה נתונים — בדקו עם SELECT)_

2. 🟢 הוסיפו תלמיד חדש: 211, 'נדים', 'סעב', 2013, עיר 5. _(🔍 משנה נתונים — בדקו עם SELECT)_

3. 🟢 עדכנו את המחיר של המורה 5 ל‑105. _(🔍 משנה נתונים — בדקו עם SELECT)_

4. 🟢 מחקו את הלוקר מספר 4. _(🔍 משנה נתונים — בדקו עם SELECT)_

5. 🟡 הוסיפו מורה חדשה: 7, 'לינה חורי', מלמדת חליל (50), 125 לשעה, **בלי טלפון**. (רשמו את שמות העמודות) _(🔍 משנה נתונים — בדקו עם SELECT)_

6. 🟡 כל התלמידים המתחילים עוברים לרמת 'ממשיך'. _(🔍 משנה נתונים — בדקו עם SELECT)_

7. 🟡 הנחה של 5% על כל הרישומים של שנת 2025. _(🔍 משנה נתונים — בדקו עם SELECT)_

8. 🟡 למורים שאין להם טלפון — רשמו את הטלפון '000-0000000'. _(🔍 משנה נתונים — בדקו עם SELECT)_

9. 🔴 מחקו את כל הרישומים של המורה 'יוסי פרץ' (בלי לכתוב את הקוד שלו — עם תת‑שאילתה). _(🔍 משנה נתונים — בדקו עם SELECT)_

10. 🔴 העלו ב‑20 את התשלום של כל הרישומים של תלמידים שגרים בעכו. _(🔍 משנה נתונים — בדקו עם SELECT)_

</div>

<div dir="rtl">

---

## 7️⃣ תרגול נוסף — 🏫 בית הספר "עתיד"

> בסיס נתונים אחר, שאתם לא מכירים — בדיוק כמו בבחינה. [📋 הטבלאות והקוד של בית הספר "עתיד"](../../databases/school/)

1. 🟢 הוסיפו את העיר 'טמרה' בקוד 7. _(🔍 משנה נתונים — בדקו עם SELECT)_

2. 🟡 שבצו את התלמידה 1018 (`לינא`) לכיתה 104. _(🔍 משנה נתונים — בדקו עם SELECT)_

3. 🟡 העלו ב‑5% את השכר של כל המורים למתמטיקה. _(🔍 משנה נתונים — בדקו עם SELECT)_

4. 🟡 מחקו את כל ההיעדרויות המאושרות. _(🔍 משנה נתונים — בדקו עם SELECT)_

5. 🔴 פקטור: הוסיפו 5 נקודות לכל הציונים במקצוע 16, אבל לא מעבר ל‑100 (רמז: `MIN(Grade + 5, 100)`). _(🔍 משנה נתונים — בדקו עם SELECT)_

</div>

<details>
<summary>📥 <b>הקוד שבונה את בסיס הנתונים 🏫 בית הספר "עתיד"</b> — מעתיקים הכול ומדביקים ב‑OneCompiler</summary>

```sql
-- ============================================================
--  בית הספר "עתיד"  ·  בסיס הנתונים לתרגול בכיתה
--  7 טבלאות · 18 תלמידים · שנת הלימודים 2026/27
--  תאריך הייחוס בכל התרגילים: '2026-09-21'
--
--  הדביקו את כל הקובץ ב-OneCompiler (SQLite), לחצו Run,
--  וכתבו את השאילתות שלכם מתחת לקוד.
-- ============================================================
DROP TABLE IF EXISTS Absences;
DROP TABLE IF EXISTS Grades;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Classes;
DROP TABLE IF EXISTS Teachers;
DROP TABLE IF EXISTS Cities;

-- ---------- ערים ----------
CREATE TABLE Cities (
  CityCode  INTEGER PRIMARY KEY,
  CityName  TEXT NOT NULL
);
INSERT INTO Cities VALUES (1, 'ירכא');
INSERT INTO Cities VALUES (2, 'עכו');
INSERT INTO Cities VALUES (3, 'כרמיאל');
INSERT INTO Cities VALUES (4, 'חיפה');
INSERT INTO Cities VALUES (5, 'נהריה');
INSERT INTO Cities VALUES (6, 'שפרעם');

-- ---------- מורים ----------
CREATE TABLE Teachers (
  TeacherCode  INTEGER PRIMARY KEY,
  FirstName    TEXT    NOT NULL,
  LastName     TEXT    NOT NULL,
  Subject      TEXT    NOT NULL,
  HireDate     TEXT    NOT NULL,
  Salary       INTEGER NOT NULL,                      -- שכר חודשי בש"ח
  CityCode     INTEGER REFERENCES Cities(CityCode),
  Phone        TEXT                                   -- NULL = לא עדכן טלפון
);
INSERT INTO Teachers VALUES (1, 'נביל',  'סרחאן',   'מתמטיקה',  '2012-09-01', 14500, 1, '050-7010101');
INSERT INTO Teachers VALUES (2, 'רונית', 'בר-לב',   'אנגלית',   '2018-09-01', 11200, 4, NULL);
INSERT INTO Teachers VALUES (3, 'חוסאם', 'זיאד',    'מחשבים',   '2021-02-15', 12800, 6, '054-7030303');
INSERT INTO Teachers VALUES (4, 'אורלי', 'שמש',     'היסטוריה', '2009-09-01', 15300, 5, '052-7040404');
INSERT INTO Teachers VALUES (5, 'פאדי',  'חדאד',    'ספורט',    '2023-09-01',  9800, 1, '053-7050505');
INSERT INTO Teachers VALUES (6, 'גלית',  'מזרחי',   'מתמטיקה',  '2016-09-01', 13100, 3, NULL);
INSERT INTO Teachers VALUES (7, 'סמיר',  'אבו-ראס', 'ביולוגיה', '2024-09-01', 10400, 2, '050-7070707');

-- ---------- כיתות ----------
CREATE TABLE Classes (
  ClassCode    INTEGER PRIMARY KEY,
  ClassName    TEXT    NOT NULL,
  Grade        INTEGER NOT NULL,                      -- שכבה: 10 / 11 / 12
  TeacherCode  INTEGER REFERENCES Teachers(TeacherCode),   -- מחנך/ת
  RoomNumber   INTEGER                                -- NULL = טרם שובצה כיתת אם
);
INSERT INTO Classes VALUES (101, 'י1',  10, 1, 12);
INSERT INTO Classes VALUES (102, 'י2',  10, 2, 14);
INSERT INTO Classes VALUES (103, 'יא1', 11, 3, 21);
INSERT INTO Classes VALUES (104, 'יא2', 11, 6, NULL);
INSERT INTO Classes VALUES (105, 'יב1', 12, 4, 31);

-- ---------- מקצועות ----------
CREATE TABLE Courses (
  CourseCode   INTEGER PRIMARY KEY,
  CourseName   TEXT    NOT NULL,
  TeacherCode  INTEGER REFERENCES Teachers(TeacherCode),   -- NULL = טרם נקבע מורה
  WeeklyHours  INTEGER NOT NULL
);
INSERT INTO Courses VALUES (11, 'מתמטיקה 5 יח"ל',     1,    5);
INSERT INTO Courses VALUES (12, 'אנגלית 4 יח"ל',      2,    4);
INSERT INTO Courses VALUES (13, 'מבוא לבסיסי נתונים', 3,    3);
INSERT INTO Courses VALUES (14, 'היסטוריה',           4,    2);
INSERT INTO Courses VALUES (15, 'חינוך גופני',        5,    2);
INSERT INTO Courses VALUES (16, 'מתמטיקה 3 יח"ל',     6,    3);
INSERT INTO Courses VALUES (17, 'סדנת פרויקטים',      NULL, 2);

-- ---------- תלמידים ----------
CREATE TABLE Students (
  StudentId   INTEGER PRIMARY KEY,
  FirstName   TEXT NOT NULL,
  LastName    TEXT NOT NULL,
  ClassCode   INTEGER REFERENCES Classes(ClassCode),   -- NULL = טרם שובץ לכיתה
  Gender      TEXT NOT NULL CHECK (Gender IN ('M','F')),
  BirthDate   TEXT,                                    -- NULL = חסר בתיק
  CityCode    INTEGER REFERENCES Cities(CityCode),
  EnrollDate  TEXT NOT NULL,
  Phone       TEXT                                     -- NULL = אין טלפון נייד
);
INSERT INTO Students VALUES (1001, 'אדם',   'חלבי',  101,  'M', '2011-03-14', 1,    '2026-09-01', '050-1000001');
INSERT INTO Students VALUES (1002, 'נור',   'עזאם',  101,  'F', '2011-07-22', 1,    '2026-09-01', NULL);
INSERT INTO Students VALUES (1003, 'יואב',  'כהן',   101,  'M', '2011-01-09', 3,    '2026-09-01', '052-1000003');
INSERT INTO Students VALUES (1004, 'מאיה',  'לוי',   102,  'F', '2011-11-30', 4,    '2026-09-01', '054-1000004');
INSERT INTO Students VALUES (1005, 'רוני',  'אברהם', 102,  'M', '2011-05-18', 2,    '2026-09-01', NULL);
INSERT INTO Students VALUES (1006, 'סאלי',  'חסון',  102,  'F', NULL,         2,    '2026-09-01', '050-1000006');
INSERT INTO Students VALUES (1007, 'עומר',  'ביטון', 103,  'M', '2010-02-11', 5,    '2025-09-01', '053-1000007');
INSERT INTO Students VALUES (1008, 'שירה',  'כהן',   103,  'F', '2010-09-25', 4,    '2025-09-01', '050-1000008');
INSERT INTO Students VALUES (1009, 'כרים',  'חלבי',  103,  'M', '2010-12-03', 1,    '2025-09-01', NULL);
INSERT INTO Students VALUES (1010, 'תמר',   'שושן',  104,  'F', '2010-04-07', 5,    '2025-09-01', '052-1000010');
INSERT INTO Students VALUES (1011, 'ליאור', 'לוי',   104,  'M', '2010-06-16', NULL, '2025-09-01', '050-1000011');
INSERT INTO Students VALUES (1012, 'ג''וד',  'מנסור', 104,  'F', '2010-08-29', 6,    '2025-09-01', NULL);
INSERT INTO Students VALUES (1013, 'דניאל', 'פרץ',   105,  'M', '2009-01-20', 3,    '2024-09-01', '054-1000013');
INSERT INTO Students VALUES (1014, 'הדיל',  'סעיד',  105,  'F', '2009-10-05', 6,    '2024-09-01', '050-1000014');
INSERT INTO Students VALUES (1015, 'איתי',  'גולן',  105,  'M', '2009-03-27', 4,    '2024-09-01', NULL);
INSERT INTO Students VALUES (1016, 'ראניה', 'עבאס',  105,  'F', '2009-12-12', 6,    '2024-09-01', '053-1000016');
INSERT INTO Students VALUES (1017, 'נועם',  'שחר',   101,  'M', '2011-09-02', 4,    '2026-09-01', '050-1000017');
INSERT INTO Students VALUES (1018, 'לינא',  'חמוד',  NULL, 'F', '2010-10-19', 2,    '2026-09-10', NULL);

-- ---------- ציונים ----------
CREATE TABLE Grades (
  StudentId   INTEGER REFERENCES Students(StudentId),
  CourseCode  INTEGER REFERENCES Courses(CourseCode),
  Term        INTEGER NOT NULL,                        -- מחצית: 1 / 2
  Grade       INTEGER,                                 -- NULL = לא נבחן
  PRIMARY KEY (StudentId, CourseCode, Term)
);
INSERT INTO Grades VALUES (1001, 11, 1,  88);
INSERT INTO Grades VALUES (1001, 12, 1,  74);
INSERT INTO Grades VALUES (1001, 14, 1,  92);
INSERT INTO Grades VALUES (1001, 11, 2,  91);
INSERT INTO Grades VALUES (1002, 11, 1,  95);
INSERT INTO Grades VALUES (1002, 12, 1,  89);
INSERT INTO Grades VALUES (1002, 15, 1, 100);
INSERT INTO Grades VALUES (1003, 16, 1,  61);
INSERT INTO Grades VALUES (1003, 12, 1,  55);
INSERT INTO Grades VALUES (1003, 14, 1,  70);
INSERT INTO Grades VALUES (1003, 16, 2,  67);
INSERT INTO Grades VALUES (1004, 16, 1,  48);
INSERT INTO Grades VALUES (1004, 12, 1,  62);
INSERT INTO Grades VALUES (1004, 14, 1, NULL);
INSERT INTO Grades VALUES (1005, 11, 1,  77);
INSERT INTO Grades VALUES (1005, 12, 1,  81);
INSERT INTO Grades VALUES (1005, 15, 1,  90);
INSERT INTO Grades VALUES (1006, 16, 1,  66);
INSERT INTO Grades VALUES (1006, 12, 1,  58);
INSERT INTO Grades VALUES (1007, 11, 1,  93);
INSERT INTO Grades VALUES (1007, 13, 1,  97);
INSERT INTO Grades VALUES (1007, 12, 1,  85);
INSERT INTO Grades VALUES (1007, 11, 2,  90);
INSERT INTO Grades VALUES (1008, 11, 1,  72);
INSERT INTO Grades VALUES (1008, 13, 1,  79);
INSERT INTO Grades VALUES (1008, 12, 1,  68);
INSERT INTO Grades VALUES (1009, 16, 1,  54);
INSERT INTO Grades VALUES (1009, 13, 1,  63);
INSERT INTO Grades VALUES (1009, 12, 1, NULL);
INSERT INTO Grades VALUES (1010, 11, 1, 100);
INSERT INTO Grades VALUES (1010, 13, 1,  91);
INSERT INTO Grades VALUES (1010, 12, 1,  96);
INSERT INTO Grades VALUES (1010, 11, 2,  97);
INSERT INTO Grades VALUES (1011, 16, 1,  83);
INSERT INTO Grades VALUES (1011, 13, 1,  75);
INSERT INTO Grades VALUES (1011, 12, 1,  80);
INSERT INTO Grades VALUES (1012, 16, 1,  42);
INSERT INTO Grades VALUES (1012, 13, 1,  51);
INSERT INTO Grades VALUES (1012, 12, 1,  47);
INSERT INTO Grades VALUES (1012, 16, 2,  39);
INSERT INTO Grades VALUES (1013, 11, 1,  89);
INSERT INTO Grades VALUES (1013, 13, 1,  94);
INSERT INTO Grades VALUES (1013, 17, 1,  98);
INSERT INTO Grades VALUES (1013, 12, 1,  87);
INSERT INTO Grades VALUES (1013, 11, 2,  92);
INSERT INTO Grades VALUES (1014, 11, 1,  76);
INSERT INTO Grades VALUES (1014, 13, 1,  82);
INSERT INTO Grades VALUES (1014, 17, 1,  90);
INSERT INTO Grades VALUES (1015, 16, 1,  59);
INSERT INTO Grades VALUES (1015, 13, 1,  64);
INSERT INTO Grades VALUES (1015, 17, 1,  71);
INSERT INTO Grades VALUES (1015, 16, 2,  62);
INSERT INTO Grades VALUES (1016, 11, 1,  98);
INSERT INTO Grades VALUES (1016, 13, 1,  99);
INSERT INTO Grades VALUES (1016, 17, 1,  95);
INSERT INTO Grades VALUES (1016, 12, 1,  93);
INSERT INTO Grades VALUES (1016, 11, 2, 100);
INSERT INTO Grades VALUES (1017, 11, 1,  65);
INSERT INTO Grades VALUES (1017, 12, 1,  73);
INSERT INTO Grades VALUES (1017, 14, 1,  69);

-- ---------- היעדרויות ----------
CREATE TABLE Absences (
  AbsenceId    INTEGER PRIMARY KEY,
  StudentId    INTEGER NOT NULL REFERENCES Students(StudentId),
  AbsenceDate  TEXT    NOT NULL,
  Excused      INTEGER NOT NULL CHECK (Excused IN (0,1)),   -- 1 = מאושרת
  Reason       TEXT                                         -- NULL = לא נמסרה סיבה
);
INSERT INTO Absences VALUES (1,  1003, '2026-09-02', 1, 'מחלה');
INSERT INTO Absences VALUES (2,  1003, '2026-09-03', 1, 'מחלה');
INSERT INTO Absences VALUES (3,  1004, '2026-09-07', 0, NULL);
INSERT INTO Absences VALUES (4,  1009, '2026-09-08', 0, NULL);
INSERT INTO Absences VALUES (5,  1009, '2026-09-09', 0, NULL);
INSERT INTO Absences VALUES (6,  1009, '2026-09-14', 1, 'תור לרופא');
INSERT INTO Absences VALUES (7,  1012, '2026-09-02', 0, NULL);
INSERT INTO Absences VALUES (8,  1012, '2026-09-10', 0, NULL);
INSERT INTO Absences VALUES (9,  1012, '2026-09-15', 0, NULL);
INSERT INTO Absences VALUES (10, 1012, '2026-09-16', 0, NULL);
INSERT INTO Absences VALUES (11, 1006, '2026-09-11', 1, 'אירוע משפחתי');
INSERT INTO Absences VALUES (12, 1015, '2026-09-04', 1, 'מחלה');
INSERT INTO Absences VALUES (13, 1015, '2026-09-17', 0, NULL);
INSERT INTO Absences VALUES (14, 1001, '2026-09-18', 1, 'תור לרופא');
INSERT INTO Absences VALUES (15, 1010, '2026-09-08', 1, 'מחלה');
INSERT INTO Absences VALUES (16, 1018, '2026-09-15', 0, NULL);

SELECT COUNT(*) AS students_loaded FROM Students;
```

</details>


<div dir="rtl">

---

✅ **[לפתרונות המלאים — שאילתה + התוצאה האמיתית](solutions.md)**

[➡️ השיעור הקודם](../11-views/README.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../13-create-alter-drop/README.md)

</div>
