<div dir="rtl">

# שיעור 1 — SELECT — שליפת עמודות

[🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../02-where/README.md)

> 🎯 **בשיעור הזה:** לבחור עמודות, `*`, כינויים עם `AS`, עמודה מחושבת ו‑`DISTINCT`
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
SELECT column1, column2        -- which columns to show
FROM   table_name;             -- from which table

SELECT *          FROM table_name;            -- all the columns
SELECT col AS NewName FROM table_name;        -- alias = a new name for the column
SELECT col * 12   FROM table_name;            -- a calculated column
SELECT DISTINCT col FROM table_name;          -- each value only once
```

<div dir="rtl">

- סדר העמודות בתוצאה = הסדר שכתבתם אחרי `SELECT`.
- בין עמודות שמים **פסיק**, אבל **אין פסיק** לפני `FROM`.
- `DISTINCT` מסיר שורות כפולות — הוא חל על **כל** העמודות שאחריו יחד.
- כינוי (`AS`) משנה רק את שם העמודה בתוצאה, לא את הטבלה עצמה.

</div>

<div dir="rtl">

---

## 4️⃣ דוגמאות פתורות

> קראו את השאלה, נסו לכתוב בעצמכם, ורק אז הסתכלו על הפתרון והתוצאה.

</div>

<div dir="rtl">

### דוגמה 1: הציגו את שם המורה ואת המחיר לשעה של כל המורים.

</div>

```sql
SELECT TeacherName, HourRate
FROM   Teachers;
```

<div dir="rtl">

| TeacherName | HourRate |
|---|---|
| סמיר חלבי | 120 |
| רונית לוי | 150 |
| אמיר עזאם | 110 |
| דנה כהן | 140 |
| יוסי פרץ | 100 |
| נור מנסור | 130 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### דוגמה 2: הציגו את כל העמודות של טבלת התלמידים.

</div>

```sql
SELECT *
FROM   Pupils;
```

<div dir="rtl">

| PupilId | FirstName | LastName | BirthYear | HomeTown |
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

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### דוגמה 3: הציגו את שם המורה ואת המחיר ל‑4 שעות, בשם `FourHours`.

</div>

```sql
SELECT TeacherName, HourRate * 4 AS FourHours
FROM   Teachers;
```

<div dir="rtl">

| TeacherName | FourHours |
|---|---|
| סמיר חלבי | 480 |
| רונית לוי | 600 |
| אמיר עזאם | 440 |
| דנה כהן | 560 |
| יוסי פרץ | 400 |
| נור מנסור | 520 |

**התוצאה: 6 שורות**

> 💡 עמודה מחושבת לא נשמרת בטבלה — היא מחושבת מחדש בכל הרצה.

</div>

<div dir="rtl">

### דוגמה 4: באילו ערים (קוד עיר) גרים התלמידים? כל עיר פעם אחת.

</div>

```sql
SELECT DISTINCT HomeTown
FROM   Pupils;
```

<div dir="rtl">

| HomeTown |
|---|
| 1 |
| 3 |
| 2 |
| 4 |

**התוצאה: 4 שורות**

> 💡 בלי `DISTINCT` היו חוזרות 10 שורות, אחת לכל תלמיד.

</div>

<div dir="rtl">

---

## 5️⃣ שאלות: מה תחזיר השאילתה?

> בלי להריץ! כתבו על דף את הטבלה שתתקבל (או רק את מספר השורות). אחר כך הריצו ובדקו. התשובות ב[פתרונות](solutions.md).

</div>

<div dir="rtl">

**שאלה 1.** כמה שורות וכמה עמודות יחזרו?

</div>

```sql
SELECT FirstName, BirthYear
FROM   Pupils;
```

<div dir="rtl">

**שאלה 2.** כמה שורות יחזרו? (רמז: יש שני מורים לפסנתר)

</div>

```sql
SELECT DISTINCT TeachInst
FROM   Teachers;
```

<div dir="rtl">

**שאלה 3.** כמה שורות יחזרו?

</div>

```sql
SELECT DISTINCT RegYear, PupilLevel
FROM   Registrations;
```

<div dir="rtl">

**שאלה 4.** כמה שורות יחזרו?

</div>

```sql
SELECT DISTINCT RegTeacher
FROM   Registrations;
```

<div dir="rtl">

**שאלה 5.** מה הגיל של מאיה בתוצאה?

</div>

```sql
SELECT FirstName, 2026 - BirthYear AS Age
FROM   Pupils;
```

<div dir="rtl">

---

## 6️⃣ תרגילים — 🎵 בית הספר למוזיקה "צלילים"

> כתבו שאילתה לכל סעיף והריצו. **🔢 מספר השורות הצפוי** עוזר לבדוק את עצמכם. 🟢 קל · 🟡 בינוני · 🔴 מאתגר

1. 🟢 הציגו את השם הפרטי ושם המשפחה של כל התלמידים. _(🔢 10 שורות)_

2. 🟢 הציגו את כל העמודות של טבלת הכלים (`Instruments`). _(🔢 6 שורות)_

3. 🟢 הציגו את שם המורה ואת הטלפון שלו. _(🔢 6 שורות)_

4. 🟢 הציגו את שם המשפחה ואחריו השם הפרטי (בסדר הזה) של התלמידים. _(🔢 10 שורות)_

5. 🟡 הציגו את קוד התלמיד ואת שנת הלידה, בשמות `Code` ו‑`Born`. _(🔢 10 שורות)_

6. 🟡 הציגו לכל רישום את קוד התלמיד ואת התשלום השנתי (12 חודשים) בשם `YearFee`. _(🔢 14 שורות)_

7. 🟡 הציגו לכל תלמיד את שמו הפרטי ואת גילו בשנת 2026, בשם `Age`. _(🔢 10 שורות)_

8. 🟡 אילו משפחות כלים (`InstFamily`) יש בבית הספר? כל משפחה פעם אחת. _(🔢 4 שורות)_

9. 🟡 אילו רמות (`PupilLevel`) קיימות ברישומים? כל רמה פעם אחת. _(🔢 3 שורות)_

10. 🔴 הציגו את שם המורה ואת המחיר לשעה אחרי העלאה של 10%, בשם `NewRate`. _(🔢 6 שורות)_

11. 🔴 הציגו את השם המלא של כל תלמיד בעמודה אחת בשם `FullName` (רמז: `||` מחבר טקסטים). _(🔢 10 שורות)_

12. 🔴 באילו קומות יש לוקרים? כל קומה פעם אחת. _(🔢 2 שורות)_

13. 🟢 הציגו את קוד המורה ואת שם המורה בלבד. _(🔢 6 שורות)_

14. 🟢 הציגו את כל העמודות של טבלת הערים (`Cities`). _(🔢 5 שורות)_

15. 🟡 הציגו לכל לוקר את מספרו ואת הקומה, בשמות `Locker` ו‑`Floor`. _(🔢 5 שורות)_

16. 🟡 אילו תלמידים (קודים) רשומים לשיעורים? כל תלמיד פעם אחת. _(🔢 10 שורות)_

17. 🟡 הציגו לכל רישום את קוד התלמיד, התשלום החודשי והתשלום לשבוע (חלקי 4), בשם `Weekly`. _(🔢 14 שורות)_

18. 🔴 אילו צירופים של שנה ורמה קיימים ברישומים? כל צירוף פעם אחת. _(🔢 5 שורות)_

19. 🔴 הציגו לכל מורה משפט אחד בעמודה `Info`, למשל: `סמיר חלבי - 120`. _(🔢 6 שורות)_

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

**שאלה 1.** 🟢 ✍️ הציגו את שם המשחק ואת שנת היציאה של כל המשחקים. _(🔢 10 שורות)_

</div>

<div dir="rtl">

**שאלה 2.** 🟢 ✍️ הציגו את השם הפרטי, שם המשפחה והאימייל של כל המשתמשים. _(🔢 7 שורות)_

</div>

<div dir="rtl">

**שאלה 3.** 🟡 ✍️ באילו מדינות יש חברות משחקים? כל מדינה פעם אחת. _(🔢 4 שורות)_

</div>

<div dir="rtl">

**שאלה 4.** 🟡 ✍️ הציגו לכל משחק את שמו ואת המחיר ל‑3 שעות משחק, בשם `ThreeHours`. _(🔢 10 שורות)_

</div>

<div dir="rtl">

**שאלה 5.** 🟡 🔎 **איזו שאילתה הציגה את הטבלה?**

</div>

<div dir="rtl">

| BuyerId |
|---|
| 1 |
| 2 |
| 3 |
| 4 |
| 5 |
| 6 |

</div>

<div dir="rtl">

**שאלה 6.** 🟡 🧮 **השלימו את הערכים:** כמה שורות יחזרו, ומה הן?

</div>

```sql
SELECT DISTINCT TypeCode
FROM   Games;
```

<div dir="rtl">

**שאלה 7.** 🔴 🧩 **השלימו את הפקודה:** השלימו כך שיוצגו שם המשחק ומספר השנים מאז שיצא (עד 2026), בשם `Age`.

</div>

```sql
SELECT GameName, ________ AS ____
FROM   _____;
```

<div dir="rtl">

---

## 8️⃣ תרגול נוסף — 🏫 בית הספר "עתיד"

> בסיס נתונים אחר, שאתם לא מכירים — בדיוק כמו בבחינה. [📋 הטבלאות והקוד של בית הספר "עתיד"](../../databases/school/)

1. 🟢 הציגו את השם הפרטי, שם המשפחה והמקצוע של כל המורים. _(🔢 7 שורות)_

2. 🟢 הציגו את כל העמודות של טבלת המקצועות (`Courses`). _(🔢 7 שורות)_

3. 🟡 הציגו לכל מורה את שמו הפרטי ואת השכר השנתי (12 משכורות), בשם `YearSalary`. _(🔢 7 שורות)_

4. 🟡 אילו מקצועות מלמדים המורים? כל מקצוע פעם אחת. _(🔢 6 שורות)_

5. 🔴 הציגו לכל מקצוע את שמו ואת מספר השעות בשנה (40 שבועות), בשם `YearHours`. _(🔢 7 שורות)_

6. 🟢 הציגו את שם הכיתה ואת השכבה של כל הכיתות. _(🔢 5 שורות)_

7. 🟢 הציגו את קוד התלמיד, תאריך ההיעדרות והסיבה מטבלת ההיעדרויות. _(🔢 16 שורות)_

8. 🟡 באילו שכבות יש כיתות? כל שכבה פעם אחת. _(🔢 3 שורות)_

9. 🔴 הציגו לכל ציון את קוד התלמיד ואת הציון אחרי פקטור של 5 נקודות, בשם `WithFactor`. _(🔢 60 שורות)_

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

[🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../02-where/README.md)

</div>
