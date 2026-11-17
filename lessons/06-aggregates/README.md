<div dir="rtl">

# שיעור 6 — פונקציות מצרפיות — COUNT, SUM, AVG, MIN, MAX

[➡️ השיעור הקודם](../05-row-functions/README.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../07-group-by-having/README.md)

> 🎯 **בשיעור הזה:** לסכם עמודה שלמה לערך אחד: ספירה, סכום, ממוצע, מינימום ומקסימום
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

---

## 3️⃣ התחביר בקצרה

</div>

```sql
SELECT COUNT(*)              FROM Teachers;   -- number of rows
SELECT COUNT(TeacherPhone)   FROM Teachers;   -- rows where the column is NOT NULL
SELECT COUNT(DISTINCT TeachInst) FROM Teachers; -- number of different values
SELECT SUM(MonthlyFee)       FROM Registrations;
SELECT AVG(HourRate)         FROM Teachers;
SELECT MIN(HourRate), MAX(HourRate) FROM Teachers;

-- with WHERE: first filter the rows, then summarize
SELECT COUNT(*) FROM Registrations WHERE RegYear = 2025;
```

<div dir="rtl">

- פונקציה מצרפית **מכווצת** הרבה שורות לשורה **אחת**.
- `COUNT(*)` סופר **הכול**. `COUNT(col)` **מדלג על NULL**.
- `SUM`, `AVG`, `MIN`, `MAX` — מתעלמים מ‑NULL.
- ⚠️ **אסור** פונקציה מצרפית בתוך `WHERE`. `WHERE HourRate > AVG(HourRate)` — שגיאה! (הפתרון בשיעור 10).
- ⚠️ אי אפשר לשים לצד פונקציה מצרפית עמודה רגילה (בלי `GROUP BY` — שיעור 7).

</div>

<div dir="rtl">

---

## 4️⃣ דוגמאות פתורות

> קראו את השאלה, נסו לכתוב בעצמכם, ורק אז הסתכלו על הפתרון והתוצאה.

</div>

<div dir="rtl">

### דוגמה 1: כמה מורים יש, וכמה מהם רשמו טלפון?

</div>

```sql
SELECT COUNT(*)            AS AllTeachers,
       COUNT(TeacherPhone) AS WithPhone
FROM   Teachers;
```

<div dir="rtl">

| AllTeachers | WithPhone |
|---|---|
| 6 | 4 |

**התוצאה: שורה אחת**

> 💡 ההפרש (2) = המורים שהטלפון שלהם NULL.

</div>

<div dir="rtl">

### דוגמה 2: המחיר הממוצע, הנמוך והגבוה של שעת שיעור.

</div>

```sql
SELECT AVG(HourRate) AS AvgRate,
       MIN(HourRate) AS MinRate,
       MAX(HourRate) AS MaxRate
FROM   Teachers;
```

<div dir="rtl">

| AvgRate | MinRate | MaxRate |
|---|---|---|
| 125.0 | 100 | 150 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### דוגמה 3: סך התשלומים החודשיים של רישומי 2025.

</div>

```sql
SELECT SUM(MonthlyFee) AS Total2025
FROM   Registrations
WHERE  RegYear = 2025;
```

<div dir="rtl">

| Total2025 |
|---|
| 1690 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### דוגמה 4: בכמה כלים שונים מלמדים המורים?

</div>

```sql
SELECT COUNT(DISTINCT TeachInst) AS Instruments
FROM   Teachers;
```

<div dir="rtl">

| Instruments |
|---|
| 5 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

---

## 5️⃣ שאלות: מה תחזיר השאילתה?

> בלי להריץ! כתבו על דף את הטבלה שתתקבל (או רק את מספר השורות). אחר כך הריצו ובדקו. התשובות ב[פתרונות](solutions.md).

</div>

<div dir="rtl">

**שאלה 1.** מה שלושת המספרים?

</div>

```sql
SELECT COUNT(*), COUNT(TeacherPhone), COUNT(DISTINCT TeachInst)
FROM   Teachers;
```

<div dir="rtl">

**שאלה 2.** מה יחזור?

</div>

```sql
SELECT COUNT(*)
FROM   Registrations
WHERE  RegTeacher = 3;
```

<div dir="rtl">

**שאלה 3.** מה יחזור?

</div>

```sql
SELECT MAX(BirthYear) - MIN(BirthYear) AS Diff
FROM   Pupils;
```

<div dir="rtl">

**שאלה 4.** מה שני המספרים?

</div>

```sql
SELECT COUNT(DISTINCT HomeTown), COUNT(*)
FROM   Pupils;
```

<div dir="rtl">

**שאלה 5.** מה הסכום?

</div>

```sql
SELECT SUM(MonthlyFee)
FROM   Registrations
WHERE  RegPupil = 204;
```

<div dir="rtl">

---

## 6️⃣ תרגילים — 🎵 בית הספר למוזיקה "צלילים"

> כתבו שאילתה לכל סעיף והריצו. **🔢 מספר השורות הצפוי** עוזר לבדוק את עצמכם. 🟢 קל · 🟡 בינוני · 🔴 מאתגר

1. 🟢 כמה תלמידים יש בבית הספר? _(🔢 שורה אחת)_

2. 🟢 מה התשלום החודשי הגבוה ביותר ברישומים? _(🔢 שורה אחת)_

3. 🟢 מה שנת הלידה של התלמיד המבוגר ביותר? _(🔢 שורה אחת)_

4. 🟢 מה הסכום של כל התשלומים החודשיים? _(🔢 שורה אחת)_

5. 🟡 כמה מורים **אין** להם טלפון? (שתי דרכים: עם `WHERE ... IS NULL`, או `COUNT(*) - COUNT(TeacherPhone)`) _(🔢 שורה אחת)_

6. 🟡 מה התשלום הממוצע של תלמידים מתחילים? עגלו ל‑2 ספרות. _(🔢 שורה אחת)_

7. 🟡 כמה תלמידים **שונים** רשומים לשיעורים? (תלמיד יכול להופיע פעמיים ברישומים) _(🔢 שורה אחת)_

8. 🟡 כמה רישומים יש למורה 5, ומה סכום התשלומים שלהם? _(🔢 שורה אחת)_

9. 🔴 מה ההפרש בין המחיר היקר ביותר לזול ביותר לשעה? _(🔢 שורה אחת)_

10. 🔴 כמה תלמידים נולדו בין 2010 ל‑2012, ומה שנת הלידה הממוצעת שלהם? _(🔢 שורה אחת)_

11. 🔴 מה ההכנסה השנתית הכוללת (12 חודשים) מכל הרישומים? _(🔢 שורה אחת)_

12. 🟢 כמה כלים יש בטבלת הכלים? _(🔢 שורה אחת)_

13. 🟢 מה המחיר לשעה הנמוך ביותר? _(🔢 שורה אחת)_

14. 🟡 כמה תלמידים גרים בעיר 1? _(🔢 שורה אחת)_

15. 🟡 מה התשלום הממוצע ברישומים של שנת 2025? _(🔢 שורה אחת)_

16. 🟡 כמה לוקרים יש בקומה 2? _(🔢 שורה אחת)_

17. 🔴 כמה מורים מלמדים כלי ממשפחת 'מיתר'? (רמז: `TeachInst IN (20, 30, 60)`) _(🔢 שורה אחת)_

18. 🔴 מה סכום התשלומים, הממוצע (מעוגל) ומספר הרישומים של התלמידים המתקדמים — בשאילתה אחת? _(🔢 שורה אחת)_

</div>

<div dir="rtl">

---

## 7️⃣ 🎓 בסגנון הבחינה — 🎮 חנות משחקי מחשב

> שאלות בפורמט של שאלון 735911: שמות שדות ייחודיים, צירוף עם פסיק + `WHERE`, השלמת ערכים, זיהוי שאילתה לפי פלט והשלמת פקודות. [📋 הטבלאות והקוד](../../databases/games/)

</div>

<details>
<summary>📋 <b>הטבלאות של חנות משחקי מחשב</b> (לחצו לפתיחה)</summary>

<div dir="rtl">

**`Categories`**

| CatCode 🔑 | CatName |
|---|---|
| 1 | פעולה |
| 2 | ספורט |
| 3 | אסטרטגיה |
| 4 | סימולציה |
| 5 | חידות |

**`Companies`**

| CompCode 🔑 | CompName | Country |
|---|---|---|
| 10 | Nintendo | Japan |
| 20 | Electronic Arts | USA |
| 30 | Ubisoft | France |
| 40 | Maxis | USA |
| 50 | Playtika | Israel |

**`Games`**

| GameCode 🔑 | GameName | TypeCode 🔗 | MakerCode 🔗 | GameYear | PricePerHour |
|---|---|---|---|---|---|
| 1 | Mario Kart | 2 | 10 | 2017 | 6.5 |
| 2 | FIFA | 2 | 20 | 2021 | 8.0 |
| 3 | Assassin's Creed | 1 | 30 | 2020 | 9.5 |
| 4 | The Sims | 4 | 40 | 2014 | 7.0 |
| 5 | SimCity | 4 | 40 | 2013 | 5.5 |
| 6 | Zelda | 1 | 10 | 2023 | 10.0 |
| 7 | Anno 1800 | 3 | 30 | 2019 | 8.5 |
| 8 | NBA Live | 2 | 20 | 2021 | 7.5 |
| 9 | Tetris | 5 | *NULL* | 1984 | 3.0 |
| 10 | Just Dance | 2 | 30 | 2022 | 6.0 |

**`Users`**

| UserId 🔑 | FirstName | LastName | Email | BirthYear |
|---|---|---|---|---|
| 1 | רמי | חלבי | rami@mail.com | 2007 |
| 2 | שני | כהן | shani@mail.com | 2008 |
| 3 | וליד | סעד | walid@mail.com | 2006 |
| 4 | אור | לוי | *NULL* | 2009 |
| 5 | דניאל | חורי | dani@mail.com | 2007 |
| 6 | מאיה | פרץ | maya@mail.com | 2008 |
| 7 | נאדר | עזאם | *NULL* | 2006 |

**`Orders`**

| OrderId 🔑 | BuyerId 🔗 | GameNum 🔗 | OrderDate | Hours |
|---|---|---|---|---|
| 101 | 1 | 2 | 2025-09-02 | 3 |
| 102 | 2 | 4 | 2025-09-05 | 5 |
| 103 | 1 | 6 | 2025-09-12 | 2 |
| 104 | 3 | 2 | 2025-09-15 | 4 |
| 105 | 4 | 1 | 2025-09-19 | 1 |
| 106 | 2 | 1 | 2025-09-20 | 2 |
| 107 | 5 | 7 | 2025-09-25 | 6 |
| 108 | 1 | 2 | 2025-09-30 | 2 |
| 109 | 6 | 3 | 2025-10-01 | 3 |
| 110 | 3 | 8 | 2025-10-03 | 2 |
| 111 | 2 | 6 | 2025-10-04 | 4 |
| 112 | 5 | 2 | 2025-10-07 | 1 |
| 113 | 6 | 4 | 2025-10-09 | 3 |

</div>

</details>


<details>
<summary>📥 <b>הקוד שבונה את בסיס הנתונים 🎮 חנות משחקי מחשב</b> — מעתיקים הכול ומדביקים ב‑OneCompiler</summary>

```sql
-- ============================================================
--  חנות משחקי מחשב  ·  בסיס נתונים לבחינה לדוגמה 3
--  הדביקו את כל הקובץ ב-OneCompiler, לחצו Run, וכתבו את השאילתות מתחת.
-- ============================================================
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Games;
DROP TABLE IF EXISTS Companies;
DROP TABLE IF EXISTS Categories;

CREATE TABLE Categories (
  CatCode  INTEGER PRIMARY KEY,
  CatName  TEXT NOT NULL
);
INSERT INTO Categories VALUES (1, 'פעולה');
INSERT INTO Categories VALUES (2, 'ספורט');
INSERT INTO Categories VALUES (3, 'אסטרטגיה');
INSERT INTO Categories VALUES (4, 'סימולציה');
INSERT INTO Categories VALUES (5, 'חידות');

CREATE TABLE Companies (
  CompCode  INTEGER PRIMARY KEY,
  CompName  TEXT NOT NULL,
  Country   TEXT
);
INSERT INTO Companies VALUES (10, 'Nintendo',        'Japan');
INSERT INTO Companies VALUES (20, 'Electronic Arts', 'USA');
INSERT INTO Companies VALUES (30, 'Ubisoft',         'France');
INSERT INTO Companies VALUES (40, 'Maxis',           'USA');
INSERT INTO Companies VALUES (50, 'Playtika',        'Israel');

CREATE TABLE Games (
  GameCode      INTEGER PRIMARY KEY,
  GameName      TEXT NOT NULL,
  TypeCode      INTEGER REFERENCES Categories(CatCode),
  MakerCode     INTEGER REFERENCES Companies(CompCode),
  GameYear      INTEGER,
  PricePerHour  REAL               -- NIS per hour of play
);
INSERT INTO Games VALUES (1, 'Mario Kart',      2, 10, 2017, 6.5);
INSERT INTO Games VALUES (2, 'FIFA',            2, 20, 2021, 8.0);
INSERT INTO Games VALUES (3, 'Assassin''s Creed', 1, 30, 2020, 9.5);
INSERT INTO Games VALUES (4, 'The Sims',        4, 40, 2014, 7.0);
INSERT INTO Games VALUES (5, 'SimCity',         4, 40, 2013, 5.5);
INSERT INTO Games VALUES (6, 'Zelda',           1, 10, 2023, 10.0);
INSERT INTO Games VALUES (7, 'Anno 1800',       3, 30, 2019, 8.5);
INSERT INTO Games VALUES (8, 'NBA Live',        2, 20, 2021, 7.5);
INSERT INTO Games VALUES (9, 'Tetris',          5, NULL, 1984, 3.0);
INSERT INTO Games VALUES (10, 'Just Dance',     2, 30, 2022, 6.0);

CREATE TABLE Users (
  UserId     INTEGER PRIMARY KEY,
  FirstName  TEXT NOT NULL,
  LastName   TEXT NOT NULL,
  Email      TEXT,
  BirthYear  INTEGER
);
INSERT INTO Users VALUES (1, 'רמי',   'חלבי',  'rami@mail.com',  2007);
INSERT INTO Users VALUES (2, 'שני',   'כהן',   'shani@mail.com', 2008);
INSERT INTO Users VALUES (3, 'וליד',  'סעד',   'walid@mail.com', 2006);
INSERT INTO Users VALUES (4, 'אור',   'לוי',   NULL,             2009);
INSERT INTO Users VALUES (5, 'דניאל', 'חורי',  'dani@mail.com',  2007);
INSERT INTO Users VALUES (6, 'מאיה',  'פרץ',   'maya@mail.com',  2008);
INSERT INTO Users VALUES (7, 'נאדר',  'עזאם',  NULL,             2006);

CREATE TABLE Orders (
  OrderId    INTEGER PRIMARY KEY,
  BuyerId    INTEGER REFERENCES Users(UserId),
  GameNum    INTEGER REFERENCES Games(GameCode),
  OrderDate  TEXT NOT NULL,         -- 'YYYY-MM-DD'
  Hours      INTEGER NOT NULL
);
INSERT INTO Orders VALUES (101, 1, 2, '2025-09-02', 3);
INSERT INTO Orders VALUES (102, 2, 4, '2025-09-05', 5);
INSERT INTO Orders VALUES (103, 1, 6, '2025-09-12', 2);
INSERT INTO Orders VALUES (104, 3, 2, '2025-09-15', 4);
INSERT INTO Orders VALUES (105, 4, 1, '2025-09-19', 1);
INSERT INTO Orders VALUES (106, 2, 1, '2025-09-20', 2);
INSERT INTO Orders VALUES (107, 5, 7, '2025-09-25', 6);
INSERT INTO Orders VALUES (108, 1, 2, '2025-09-30', 2);
INSERT INTO Orders VALUES (109, 6, 3, '2025-10-01', 3);
INSERT INTO Orders VALUES (110, 3, 8, '2025-10-03', 2);
INSERT INTO Orders VALUES (111, 2, 6, '2025-10-04', 4);
INSERT INTO Orders VALUES (112, 5, 2, '2025-10-07', 1);
INSERT INTO Orders VALUES (113, 6, 4, '2025-10-09', 3);

SELECT COUNT(*) AS orders_loaded FROM Orders;
```

</details>


<div dir="rtl">

**שאלה 1.** 🟢 ✍️ כמה משחקים יש בחנות? _(🔢 שורה אחת)_

</div>

<div dir="rtl">

**שאלה 2.** 🟢 ✍️ מה המחיר לשעה הגבוה ביותר? _(🔢 שורה אחת)_

</div>

<div dir="rtl">

**שאלה 3.** 🟡 ✍️ כמה משתמשים רשמו אימייל? (בלי `WHERE`) _(🔢 שורה אחת)_

</div>

<div dir="rtl">

**שאלה 4.** 🟡 ✍️ כמה שעות הוזמנו בסך הכול בספטמבר 2025? _(🔢 שורה אחת)_

</div>

<div dir="rtl">

**שאלה 5.** 🟡 🧮 **השלימו את הערכים:** השלימו את שלושת הערכים.

</div>

```sql
SELECT COUNT(*), COUNT(MakerCode), COUNT(DISTINCT MakerCode)
FROM   Games;
```

<div dir="rtl">

**שאלה 6.** 🟡 🔎 **איזו שאילתה הציגה את הטבלה?**

</div>

<div dir="rtl">

| Oldest | Newest |
|---|---|
| 1984 | 2023 |

</div>

<div dir="rtl">

**שאלה 7.** 🔴 🧩 **השלימו את הפקודה:** השלימו כך שיוצג המחיר הממוצע לשעה של משחקי הספורט (קטגוריה 2), מעוגל לספרה אחת.

</div>

```sql
SELECT _____(___(PricePerHour), 1) AS AvgPrice
FROM   Games
_____  TypeCode = _;
```

<div dir="rtl">

---

## 8️⃣ תרגול נוסף — 🏫 בית הספר "עתיד"

> בסיס נתונים אחר, שאתם לא מכירים — בדיוק כמו בבחינה. [📋 הטבלאות והקוד של בית הספר "עתיד"](../../databases/school/)

1. 🟢 כמה תלמידים יש, וכמה מהם רשמו טלפון? _(🔢 שורה אחת)_

2. 🟢 מה השכר הממוצע של המורים? _(🔢 שורה אחת)_

3. 🟡 מה הציון הגבוה, הנמוך והממוצע (מעוגל) במקצוע 11, מחצית 1? _(🔢 שורה אחת)_

4. 🟡 כמה היעדרויות לא מאושרות יש? _(🔢 שורה אחת)_

5. 🔴 בכמה מקצועות שונים יש ציונים בטבלת הציונים? _(🔢 שורה אחת)_

6. 🔴 כמה ציונים חסרים (NULL) יש בטבלת הציונים? כתבו עם `COUNT(*) - COUNT(Grade)`. _(🔢 שורה אחת)_

7. 🟢 כמה כיתות יש? _(🔢 שורה אחת)_

8. 🟢 מה השכר הגבוה ביותר של מורה? _(🔢 שורה אחת)_

9. 🟡 כמה שעות שבועיות יש בסך הכול בכל המקצועות? _(🔢 שורה אחת)_

10. 🔴 מה תאריך ההיעדרות הראשון והאחרון בטבלה? _(🔢 שורה אחת)_

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

[➡️ השיעור הקודם](../05-row-functions/README.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../07-group-by-having/README.md)

</div>
