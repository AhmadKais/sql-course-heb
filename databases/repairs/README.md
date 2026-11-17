<div dir="rtl">

# 🔧 מעבדת "דלתא‑טק"

> תיקוני מכשירים, טכנאים, חלפים וסוגי מכשירים.
>
> **שימוש:** בחינת אמצע · **7 טבלאות**

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

קובץ: [`repairs.sql`](repairs.sql) · [פתיחה כטקסט נקי (Ctrl+A, Ctrl+C)](https://raw.githubusercontent.com/AhmadKais/sql-course-heb/main/databases/repairs/repairs.sql)

</div>

<details>
<summary>📥 <b>לחצו כאן לקוד שבונה את בסיס הנתונים 🔧 מעבדת "דלתא‑טק"</b> — מעתיקים הכול ומדביקים ב‑OneCompiler</summary>

```sql
-- ============================================================
--  מעבדת "דלתא-טק"  ·  בסיס נתונים לבחינת אמצע (SELECT · WHERE · ORDER BY)
--  הדביקו את כל הקובץ ב-OneCompiler (SQLite), לחצו Run, וכתבו את השאילתות מתחת.
--  לכל שדה בבסיס הנתונים שם ייחודי, ולכן אין צורך בשם הטבלה לפניו.
-- ============================================================
DROP TABLE IF EXISTS PartUsage;
DROP TABLE IF EXISTS Benches;
DROP TABLE IF EXISTS Repairs;
DROP TABLE IF EXISTS Parts;
DROP TABLE IF EXISTS Technicians;
DROP TABLE IF EXISTS DevTypes;
DROP TABLE IF EXISTS Cities;

-- ---------- טבלת עזר: ערים ----------
CREATE TABLE Cities (
  CityCode  INTEGER PRIMARY KEY,
  CityName  TEXT NOT NULL
);
INSERT INTO Cities VALUES (1, 'ירכא');
INSERT INTO Cities VALUES (2, 'עכו');
INSERT INTO Cities VALUES (3, 'כרמיאל');
INSERT INTO Cities VALUES (4, 'נהריה');
INSERT INTO Cities VALUES (5, 'שפרעם');
INSERT INTO Cities VALUES (6, 'מעלות');

-- ---------- טבלת עזר: סוגי מכשירים ----------
CREATE TABLE DevTypes (
  DevCode    INTEGER PRIMARY KEY,
  DevName    TEXT NOT NULL,
  DevFamily  TEXT NOT NULL
);
INSERT INTO DevTypes VALUES (10, 'טלפון חכם',    'סלולר');
INSERT INTO DevTypes VALUES (20, 'מחשב נייד',    'מחשבים');
INSERT INTO DevTypes VALUES (30, 'טאבלט',        'סלולר');
INSERT INTO DevTypes VALUES (40, 'שעון חכם',     'לבישים');
INSERT INTO DevTypes VALUES (50, 'אוזניות',      'לבישים');
INSERT INTO DevTypes VALUES (60, 'קונסולת משחק', 'מחשבים');

-- ---------- טבלת עזר: חלפים ----------
CREATE TABLE Parts (
  PartCode   INTEGER PRIMARY KEY,
  PartName   TEXT NOT NULL,
  PartPrice  INTEGER NOT NULL        -- מחיר החלף בש"ח
);
INSERT INTO Parts VALUES (101, 'מסך',        450);
INSERT INTO Parts VALUES (102, 'סוללה',      180);
INSERT INTO Parts VALUES (103, 'שקע טעינה',   90);
INSERT INTO Parts VALUES (104, 'רמקול',       70);
INSERT INTO Parts VALUES (105, 'מקלדת',      220);
INSERT INTO Parts VALUES (106, 'מצלמה',      160);
INSERT INTO Parts VALUES (107, 'כבל שטוח',    45);

-- ---------- טבלה ראשית: טכנאים ----------
CREATE TABLE Technicians (
  TechCode   INTEGER PRIMARY KEY,
  TechFirst  TEXT NOT NULL,
  TechLast   TEXT NOT NULL,
  TechCity   INTEGER REFERENCES Cities(CityCode),
  StartDate  TEXT NOT NULL,
  HourWage   INTEGER NOT NULL,       -- שכר לשעה בש"ח
  TechPhone  TEXT                    -- NULL = לא רשום טלפון
);
INSERT INTO Technicians VALUES (1, 'נביל',  'סרחאן',  1, '2019-03-01',  95, '050-7010101');
INSERT INTO Technicians VALUES (2, 'רונית', 'בר-לב',  4, '2021-09-15',  80, NULL);
INSERT INTO Technicians VALUES (3, 'חוסאם', 'זיאד',   5, '2020-01-12',  88, '054-7030303');
INSERT INTO Technicians VALUES (4, 'דנה',   'כהן',    1, '2023-06-01',  72, '052-7040404');
INSERT INTO Technicians VALUES (5, 'סאמר',  'חלבי',   1, '2018-11-20', 105, NULL);
INSERT INTO Technicians VALUES (6, 'מאיה',  'אברהם',  6, '2024-02-10',  65, '053-7060606');
INSERT INTO Technicians VALUES (7, 'ליאן',  'קבלאן',  2, '2022-05-05',  80, '050-7070707');

-- ---------- טבלה ראשית: תיקונים ----------
CREATE TABLE Repairs (
  RepairNum    INTEGER PRIMARY KEY,
  CustName     TEXT NOT NULL,
  RepairDev    INTEGER REFERENCES DevTypes(DevCode),
  RepairTech   INTEGER REFERENCES Technicians(TechCode),
  InDate       TEXT NOT NULL,        -- תאריך קבלת המכשיר
  DoneDate     TEXT,                 -- NULL = התיקון עדיין פתוח
  RepairPrice  INTEGER NOT NULL,     -- מחיר התיקון בש"ח
  Priority     TEXT NOT NULL         -- רגיל / דחוף / מיידי
);
INSERT INTO Repairs VALUES (1001, 'אדם חלבי',   10, 1, '2026-01-12', '2026-01-15',  420, 'רגיל');
INSERT INTO Repairs VALUES (1002, 'מאיה כהן',   20, 3, '2026-01-20', '2026-02-02',  980, 'דחוף');
INSERT INTO Repairs VALUES (1003, 'כרים עזאם',  10, 2, '2026-02-03', '2026-02-05',  310, 'רגיל');
INSERT INTO Repairs VALUES (1004, 'שירה לוי',   30, 1, '2026-02-14', NULL,          540, 'דחוף');
INSERT INTO Repairs VALUES (1005, 'רמי חורי',   60, 5, '2026-03-02', '2026-03-09',  760, 'רגיל');
INSERT INTO Repairs VALUES (1006, 'תמר אברהם',  40, 4, '2026-03-11', '2026-03-12',  190, 'מיידי');
INSERT INTO Repairs VALUES (1007, 'ליאן קבלאן', 10, 7, '2026-03-25', '2026-04-01',  450, 'רגיל');
INSERT INTO Repairs VALUES (1008, 'עומר ביטון', 20, 3, '2026-04-05', NULL,         1250, 'דחוף');
INSERT INTO Repairs VALUES (1009, 'סאלי חסון',  50, 6, '2026-04-18', '2026-04-19',  120, 'רגיל');
INSERT INTO Repairs VALUES (1010, 'יואב שושן',  10, 1, '2026-05-02', '2026-05-06',  380, 'מיידי');
INSERT INTO Repairs VALUES (1011, 'נור מנסור',  30, 2, '2026-05-15', '2026-05-20',  610, 'רגיל');
INSERT INTO Repairs VALUES (1012, 'אלון כהן',   20, 5, '2026-06-01', '2026-06-14', 1480, 'דחוף');
INSERT INTO Repairs VALUES (1013, 'סלים דיאב',  10, 7, '2026-06-22', '2026-06-24',  290, 'רגיל');
INSERT INTO Repairs VALUES (1014, 'הילה פרץ',   60, 4, '2026-07-03', NULL,          820, 'רגיל');
INSERT INTO Repairs VALUES (1015, 'מוחמד דיב',  40, 6, '2026-07-19', '2026-07-21',  230, 'מיידי');
INSERT INTO Repairs VALUES (1016, 'אורי שמש',   20, 3, '2026-08-04', '2026-08-20', 1100, 'דחוף');

-- ---------- קשר 1:1 — לכל טכנאי עמדת עבודה אחת לכל היותר ----------
CREATE TABLE Benches (
  BenchNum    INTEGER PRIMARY KEY,
  BenchTech   INTEGER UNIQUE REFERENCES Technicians(TechCode),
  BenchFloor  INTEGER NOT NULL
);
INSERT INTO Benches VALUES (1, 1, 1);
INSERT INTO Benches VALUES (2, 3, 1);
INSERT INTO Benches VALUES (3, 5, 2);
INSERT INTO Benches VALUES (4, 7, 2);
INSERT INTO Benches VALUES (5, 4, 2);

-- ---------- טבלה מקשרת M:N — אילו חלפים נכנסו לאיזה תיקון ----------
CREATE TABLE PartUsage (
  UseRepair  INTEGER REFERENCES Repairs(RepairNum),
  UsePart    INTEGER REFERENCES Parts(PartCode),
  UseQty     INTEGER NOT NULL,
  PRIMARY KEY (UseRepair, UsePart)
);
INSERT INTO PartUsage VALUES (1001, 102, 1);
INSERT INTO PartUsage VALUES (1002, 105, 1);
INSERT INTO PartUsage VALUES (1002, 102, 1);
INSERT INTO PartUsage VALUES (1003, 101, 1);
INSERT INTO PartUsage VALUES (1004, 101, 1);
INSERT INTO PartUsage VALUES (1005, 104, 2);
INSERT INTO PartUsage VALUES (1007, 103, 1);
INSERT INTO PartUsage VALUES (1008, 101, 1);
INSERT INTO PartUsage VALUES (1008, 105, 1);
INSERT INTO PartUsage VALUES (1010, 102, 1);
INSERT INTO PartUsage VALUES (1011, 101, 1);
INSERT INTO PartUsage VALUES (1012, 105, 1);
INSERT INTO PartUsage VALUES (1012, 102, 1);
INSERT INTO PartUsage VALUES (1016, 101, 1);
INSERT INTO PartUsage VALUES (1016, 106, 1);

SELECT COUNT(*) AS repairs_loaded FROM Repairs;
```

</details>


<div dir="rtl">

---

## 🗺️ הטבלאות והקשרים

| הטבלה | שורות | מפתח ראשי 🔑 | מפתחות זרים 🔗 |
|---|:---:|---|---|
| [`Cities`](#cities) | 6 | `CityCode` | — |
| [`DevTypes`](#devtypes) | 6 | `DevCode` | — |
| [`Parts`](#parts) | 7 | `PartCode` | — |
| [`Technicians`](#technicians) | 7 | `TechCode` | `TechCity` → `Cities(CityCode)` |
| [`Repairs`](#repairs) | 16 | `RepairNum` | `RepairTech` → `Technicians(TechCode)`<br>`RepairDev` → `DevTypes(DevCode)` |
| [`Benches`](#benches) | 5 | `BenchNum` | `BenchTech` → `Technicians(TechCode)` |
| [`PartUsage`](#partusage) | 15 | `UseRepair`, `UsePart` | `UsePart` → `Parts(PartCode)`<br>`UseRepair` → `Repairs(RepairNum)` |

> 🔑 = מפתח ראשי (PK) · 🔗 = מפתח זר (FK) — מצביע על מפתח ראשי בטבלה אחרת.

---

## Cities

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `CityCode` | INTEGER | 🔑 PK |  |
| `CityName` | TEXT |  | חובה (NOT NULL). |

**הנתונים (6 שורות):**

| CityCode 🔑 | CityName |
|---|---|
| 1 | ירכא |
| 2 | עכו |
| 3 | כרמיאל |
| 4 | נהריה |
| 5 | שפרעם |
| 6 | מעלות |

---

## DevTypes

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `DevCode` | INTEGER | 🔑 PK |  |
| `DevName` | TEXT |  | חובה (NOT NULL). |
| `DevFamily` | TEXT |  | חובה (NOT NULL). |

**הנתונים (6 שורות):**

| DevCode 🔑 | DevName | DevFamily |
|---|---|---|
| 10 | טלפון חכם | סלולר |
| 20 | מחשב נייד | מחשבים |
| 30 | טאבלט | סלולר |
| 40 | שעון חכם | לבישים |
| 50 | אוזניות | לבישים |
| 60 | קונסולת משחק | מחשבים |

---

## Parts

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `PartCode` | INTEGER | 🔑 PK |  |
| `PartName` | TEXT |  | חובה (NOT NULL). |
| `PartPrice` | INTEGER |  | חובה (NOT NULL). מחיר החלף בש"ח |

**הנתונים (7 שורות):**

| PartCode 🔑 | PartName | PartPrice |
|---|---|---|
| 101 | מסך | 450 |
| 102 | סוללה | 180 |
| 103 | שקע טעינה | 90 |
| 104 | רמקול | 70 |
| 105 | מקלדת | 220 |
| 106 | מצלמה | 160 |
| 107 | כבל שטוח | 45 |

---

## Technicians

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `TechCode` | INTEGER | 🔑 PK |  |
| `TechFirst` | TEXT |  | חובה (NOT NULL). |
| `TechLast` | TEXT |  | חובה (NOT NULL). |
| `TechCity` | INTEGER | 🔗 FK → `Cities(CityCode)` |  |
| `StartDate` | TEXT |  | חובה (NOT NULL). |
| `HourWage` | INTEGER |  | חובה (NOT NULL). שכר לשעה בש"ח |
| `TechPhone` | TEXT |  | NULL = לא רשום טלפון |

**הנתונים (7 שורות):**

| TechCode 🔑 | TechFirst | TechLast | TechCity 🔗 | StartDate | HourWage | TechPhone |
|---|---|---|---|---|---|---|
| 1 | נביל | סרחאן | 1 | 2019-03-01 | 95 | 050-7010101 |
| 2 | רונית | בר-לב | 4 | 2021-09-15 | 80 | *NULL* |
| 3 | חוסאם | זיאד | 5 | 2020-01-12 | 88 | 054-7030303 |
| 4 | דנה | כהן | 1 | 2023-06-01 | 72 | 052-7040404 |
| 5 | סאמר | חלבי | 1 | 2018-11-20 | 105 | *NULL* |
| 6 | מאיה | אברהם | 6 | 2024-02-10 | 65 | 053-7060606 |
| 7 | ליאן | קבלאן | 2 | 2022-05-05 | 80 | 050-7070707 |

---

## Repairs

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `RepairNum` | INTEGER | 🔑 PK |  |
| `CustName` | TEXT |  | חובה (NOT NULL). |
| `RepairDev` | INTEGER | 🔗 FK → `DevTypes(DevCode)` |  |
| `RepairTech` | INTEGER | 🔗 FK → `Technicians(TechCode)` |  |
| `InDate` | TEXT |  | חובה (NOT NULL). תאריך קבלת המכשיר |
| `DoneDate` | TEXT |  | NULL = התיקון עדיין פתוח |
| `RepairPrice` | INTEGER |  | חובה (NOT NULL). מחיר התיקון בש"ח |
| `Priority` | TEXT |  | חובה (NOT NULL). רגיל / דחוף / מיידי |

**הנתונים (16 שורות):**

| RepairNum 🔑 | CustName | RepairDev 🔗 | RepairTech 🔗 | InDate | DoneDate | RepairPrice | Priority |
|---|---|---|---|---|---|---|---|
| 1001 | אדם חלבי | 10 | 1 | 2026-01-12 | 2026-01-15 | 420 | רגיל |
| 1002 | מאיה כהן | 20 | 3 | 2026-01-20 | 2026-02-02 | 980 | דחוף |
| 1003 | כרים עזאם | 10 | 2 | 2026-02-03 | 2026-02-05 | 310 | רגיל |
| 1004 | שירה לוי | 30 | 1 | 2026-02-14 | *NULL* | 540 | דחוף |
| 1005 | רמי חורי | 60 | 5 | 2026-03-02 | 2026-03-09 | 760 | רגיל |
| 1006 | תמר אברהם | 40 | 4 | 2026-03-11 | 2026-03-12 | 190 | מיידי |
| 1007 | ליאן קבלאן | 10 | 7 | 2026-03-25 | 2026-04-01 | 450 | רגיל |
| 1008 | עומר ביטון | 20 | 3 | 2026-04-05 | *NULL* | 1250 | דחוף |
| 1009 | סאלי חסון | 50 | 6 | 2026-04-18 | 2026-04-19 | 120 | רגיל |
| 1010 | יואב שושן | 10 | 1 | 2026-05-02 | 2026-05-06 | 380 | מיידי |
| 1011 | נור מנסור | 30 | 2 | 2026-05-15 | 2026-05-20 | 610 | רגיל |
| 1012 | אלון כהן | 20 | 5 | 2026-06-01 | 2026-06-14 | 1480 | דחוף |
| 1013 | סלים דיאב | 10 | 7 | 2026-06-22 | 2026-06-24 | 290 | רגיל |
| 1014 | הילה פרץ | 60 | 4 | 2026-07-03 | *NULL* | 820 | רגיל |
| 1015 | מוחמד דיב | 40 | 6 | 2026-07-19 | 2026-07-21 | 230 | מיידי |
| 1016 | אורי שמש | 20 | 3 | 2026-08-04 | 2026-08-20 | 1100 | דחוף |

---

## Benches

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `BenchNum` | INTEGER | 🔑 PK |  |
| `BenchTech` | INTEGER | 🔗 FK → `Technicians(TechCode)` |  |
| `BenchFloor` | INTEGER |  | חובה (NOT NULL). |

**הנתונים (5 שורות):**

| BenchNum 🔑 | BenchTech 🔗 | BenchFloor |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 3 | 1 |
| 3 | 5 | 2 |
| 4 | 7 | 2 |
| 5 | 4 | 2 |

---

## PartUsage

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `UseRepair` | INTEGER | 🔑 PK · 🔗 FK → `Repairs(RepairNum)` |  |
| `UsePart` | INTEGER | 🔑 PK · 🔗 FK → `Parts(PartCode)` |  |
| `UseQty` | INTEGER |  | חובה (NOT NULL). |

**הנתונים (15 שורות):**

| UseRepair 🔑🔗 | UsePart 🔑🔗 | UseQty |
|---|---|---|
| 1001 | 102 | 1 |
| 1002 | 105 | 1 |
| 1002 | 102 | 1 |
| 1003 | 101 | 1 |
| 1004 | 101 | 1 |
| 1005 | 104 | 2 |
| 1007 | 103 | 1 |
| 1008 | 101 | 1 |
| 1008 | 105 | 1 |
| 1010 | 102 | 1 |
| 1011 | 101 | 1 |
| 1012 | 105 | 1 |
| 1012 | 102 | 1 |
| 1016 | 101 | 1 |
| 1016 | 106 | 1 |

</div>
