<div dir="rtl">

# 🎵 בית הספר למוזיקה "צלילים"

> תלמידים, מורים, רישומים (M:N), ערים, כלים ולוקרים (1:1). שמות שדות ייחודיים — בדיוק כמו בבחינה.
>
> **שימוש:** **בסיס הנתונים הראשי של השיעורים** · **6 טבלאות**

[🏠 לדף הראשי](../../README.md) · [🗄️ כל בסיסי הנתונים](../README.md)

---

## ▶️ איך מריצים (בלי להתקין כלום)

1. פותחים את **[OneCompiler — SQLite](https://onecompiler.com/sqlite)** (או **[SQLite Online](https://sqliteonline.com/)**, שמציג גם את רשימת הטבלאות בצד).
2. מוחקים את הדוגמה שבחלון (`Ctrl+A` ← `Delete`).
3. מעתיקים את **כל** הקוד של בסיס הנתונים ומדביקים.
4. **מתחת** לקוד כותבים את השאילתה שלכם ולוחצים **Run**.

> 💡 כל קובץ מתחיל ב‑`DROP TABLE IF EXISTS`, אז אפשר להדביק אותו שוב ושוב — הנתונים חוזרים למצב ההתחלתי. זה שימושי אחרי תרגילי `UPDATE` / `DELETE`.

---

## 📥 הקוד המלא להעתקה

קובץ: [`music.sql`](music.sql) · [פתיחה כטקסט נקי (Ctrl+A, Ctrl+C)](https://raw.githubusercontent.com/AhmadKais/sql-course-heb/main/databases/music/music.sql)

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

---

## 🗺️ הטבלאות והקשרים

| הטבלה | שורות | מפתח ראשי 🔑 | מפתחות זרים 🔗 |
|---|:---:|---|---|
| [`Cities`](#cities) | 5 | `CityCode` | — |
| [`Instruments`](#instruments) | 6 | `InstCode` | — |
| [`Teachers`](#teachers) | 6 | `TeacherCode` | `TeachInst` → `Instruments(InstCode)` |
| [`Pupils`](#pupils) | 10 | `PupilId` | `HomeTown` → `Cities(CityCode)` |
| [`Registrations`](#registrations) | 14 | `RegPupil`, `RegTeacher` | `RegTeacher` → `Teachers(TeacherCode)`<br>`RegPupil` → `Pupils(PupilId)` |
| [`Lockers`](#lockers) | 5 | `LockerNum` | `LockerPupil` → `Pupils(PupilId)` |

> 🔑 = מפתח ראשי (PK) · 🔗 = מפתח זר (FK) — מצביע על מפתח ראשי בטבלה אחרת.

---

## Cities

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `CityCode` | INTEGER | 🔑 PK |  |
| `CityName` | TEXT |  | חובה (NOT NULL). |

**הנתונים (5 שורות):**

| CityCode 🔑 | CityName |
|---|---|
| 1 | ירכא |
| 2 | עכו |
| 3 | כרמיאל |
| 4 | נהריה |
| 5 | מעלות |

---

## Instruments

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `InstCode` | INTEGER | 🔑 PK |  |
| `InstName` | TEXT |  | חובה (NOT NULL). |
| `InstFamily` | TEXT |  | חובה (NOT NULL). מיתר / קלידים / הקשה / נשיפה |

**הנתונים (6 שורות):**

| InstCode 🔑 | InstName | InstFamily |
|---|---|---|
| 10 | פסנתר | קלידים |
| 20 | גיטרה | מיתר |
| 30 | כינור | מיתר |
| 40 | תופים | הקשה |
| 50 | חליל | נשיפה |
| 60 | עוד | מיתר |

---

## Teachers

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `TeacherCode` | INTEGER | 🔑 PK |  |
| `TeacherName` | TEXT |  | חובה (NOT NULL). |
| `TeachInst` | INTEGER | 🔗 FK → `Instruments(InstCode)` |  |
| `HourRate` | INTEGER |  | חובה (NOT NULL). NIS per lesson hour |
| `TeacherPhone` | TEXT |  | NULL = no phone number |

**הנתונים (6 שורות):**

| TeacherCode 🔑 | TeacherName | TeachInst 🔗 | HourRate | TeacherPhone |
|---|---|---|---|---|
| 1 | סמיר חלבי | 60 | 120 | 050-1234567 |
| 2 | רונית לוי | 10 | 150 | 052-2345678 |
| 3 | אמיר עזאם | 20 | 110 | *NULL* |
| 4 | דנה כהן | 30 | 140 | 054-4567890 |
| 5 | יוסי פרץ | 40 | 100 | 053-5678901 |
| 6 | נור מנסור | 10 | 130 | *NULL* |

---

## Pupils

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `PupilId` | INTEGER | 🔑 PK |  |
| `FirstName` | TEXT |  | חובה (NOT NULL). |
| `LastName` | TEXT |  | חובה (NOT NULL). |
| `BirthYear` | INTEGER |  |  |
| `HomeTown` | INTEGER | 🔗 FK → `Cities(CityCode)` |  |

**הנתונים (10 שורות):**

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

---

## Registrations

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `RegPupil` | INTEGER | 🔑 PK · 🔗 FK → `Pupils(PupilId)` |  |
| `RegTeacher` | INTEGER | 🔑 PK · 🔗 FK → `Teachers(TeacherCode)` |  |
| `RegYear` | INTEGER |  | חובה (NOT NULL). |
| `PupilLevel` | TEXT |  | חובה (NOT NULL). מתחיל / ממשיך / מתקדם |
| `MonthlyFee` | INTEGER |  | חובה (NOT NULL). NIS per month |

**הנתונים (14 שורות):**

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

## Lockers

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `LockerNum` | INTEGER | 🔑 PK |  |
| `LockerPupil` | INTEGER | 🔗 FK → `Pupils(PupilId)` |  |
| `LockerFloor` | INTEGER |  | חובה (NOT NULL). |

**הנתונים (5 שורות):**

| LockerNum 🔑 | LockerPupil 🔗 | LockerFloor |
|---|---|---|
| 1 | 202 | 1 |
| 2 | 205 | 1 |
| 3 | 207 | 2 |
| 4 | 210 | 2 |
| 5 | 201 | 2 |

</div>
