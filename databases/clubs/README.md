<div dir="rtl">

# ⚽ חוגי ספורט עירוניים

> חוגים, מאמנים, חברים וטבלה מקשרת.
>
> **שימוש:** בחינה לדוגמה 1 · **5 טבלאות**

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

קובץ: [`clubs.sql`](clubs.sql) · [פתיחה כטקסט נקי (Ctrl+A, Ctrl+C)](https://raw.githubusercontent.com/AhmadKais/sql-course-heb/main/databases/clubs/clubs.sql)

</div>

<details>
<summary>📥 <b>לחצו כאן לקוד שבונה את בסיס הנתונים ⚽ חוגי ספורט עירוניים</b> — מעתיקים הכול ומדביקים ב‑OneCompiler</summary>

```sql
-- ============================================================
--  חוגי ספורט עירוניים  ·  בסיס נתונים לבחינה לדוגמה 1
--  הדביקו את כל הקובץ ב-OneCompiler, לחצו Run, וכתבו את השאילתות מתחת.
-- ============================================================
DROP TABLE IF EXISTS ClubMembers;
DROP TABLE IF EXISTS Members;
DROP TABLE IF EXISTS Clubs;
DROP TABLE IF EXISTS Coaches;
DROP TABLE IF EXISTS Cities;

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

CREATE TABLE Coaches (
  CoachCode       INTEGER PRIMARY KEY,
  CoachFirstName  TEXT NOT NULL,
  CoachLastName   TEXT NOT NULL,
  Phone           TEXT                 -- NULL = no phone number
);
INSERT INTO Coaches VALUES (1, 'סאמר', 'חלבי',   '050-1111111');
INSERT INTO Coaches VALUES (2, 'מיכל', 'לוי',    NULL);
INSERT INTO Coaches VALUES (3, 'ראמי', 'עזאם',   '054-3333333');
INSERT INTO Coaches VALUES (4, 'דנה',  'כהן',    '050-4444444');
INSERT INTO Coaches VALUES (5, 'יוסי', 'אברהם',  '053-5555555');

CREATE TABLE Clubs (
  ClubCode     INTEGER PRIMARY KEY,
  ClubName     TEXT NOT NULL,
  Sport        TEXT NOT NULL,
  TrainerCode  INTEGER REFERENCES Coaches(CoachCode),
  Price        INTEGER NOT NULL                          -- monthly price in NIS
);
INSERT INTO Clubs VALUES (100, 'כדורגל צעירים',  'כדורגל',  1,    150);
INSERT INTO Clubs VALUES (101, 'כדורגל בוגרים',  'כדורגל',  1,    180);
INSERT INTO Clubs VALUES (102, 'שחייה מתחילים',  'שחייה',   2,    220);
INSERT INTO Clubs VALUES (103, 'שחייה מתקדמים',  'שחייה',   2,    250);
INSERT INTO Clubs VALUES (104, 'כדורסל',         'כדורסל',  3,    160);
INSERT INTO Clubs VALUES (105, 'טניס',           'טניס',    4,    300);
INSERT INTO Clubs VALUES (106, 'ג''ודו',          'ג''ודו',   3,    140);
INSERT INTO Clubs VALUES (107, 'יוגה',           'יוגה',    4,    120);

CREATE TABLE Members (
  MemberId   INTEGER PRIMARY KEY,
  FirstName  TEXT NOT NULL,
  LastName   TEXT NOT NULL,
  TownCode   INTEGER REFERENCES Cities(CityCode),
  Age        INTEGER,
  JoinYear   INTEGER
);
INSERT INTO Members VALUES (1001, 'אדם',   'חלבי',  1, 14, 2023);
INSERT INTO Members VALUES (1002, 'נור',   'עזאם',  1, 15, 2024);
INSERT INTO Members VALUES (1003, 'יואב',  'כהן',   3, 16, 2022);
INSERT INTO Members VALUES (1004, 'מאיה',  'לוי',   3, 15, 2025);
INSERT INTO Members VALUES (1005, 'רוני',  'אברהם', 2, 13, 2024);
INSERT INTO Members VALUES (1006, 'סאלי',  'חסון',  2, 17, 2023);
INSERT INTO Members VALUES (1007, 'עומר',  'ביטון', 5, 15, 2025);
INSERT INTO Members VALUES (1008, 'שירה',  'כהן',   4, 16, 2022);
INSERT INTO Members VALUES (1009, 'כרים',  'חלבי',  1, 13, 2025);
INSERT INTO Members VALUES (1010, 'תמר',   'שושן',  5, 14, 2023);
INSERT INTO Members VALUES (1011, 'ליאור', 'לוי',   4, 17, 2024);
INSERT INTO Members VALUES (1012, 'ג''וד',  'מנסור', 1, 16, 2025);

CREATE TABLE ClubMembers (
  MemberNum  INTEGER REFERENCES Members(MemberId),
  ClubNum    INTEGER REFERENCES Clubs(ClubCode),
  PRIMARY KEY (MemberNum, ClubNum)
);
INSERT INTO ClubMembers VALUES (1001, 100);
INSERT INTO ClubMembers VALUES (1001, 104);
INSERT INTO ClubMembers VALUES (1002, 102);
INSERT INTO ClubMembers VALUES (1003, 101);
INSERT INTO ClubMembers VALUES (1003, 105);
INSERT INTO ClubMembers VALUES (1004, 102);
INSERT INTO ClubMembers VALUES (1004, 106);
INSERT INTO ClubMembers VALUES (1005, 100);
INSERT INTO ClubMembers VALUES (1006, 103);
INSERT INTO ClubMembers VALUES (1006, 104);
INSERT INTO ClubMembers VALUES (1007, 100);
INSERT INTO ClubMembers VALUES (1008, 105);
INSERT INTO ClubMembers VALUES (1009, 100);
INSERT INTO ClubMembers VALUES (1009, 106);
INSERT INTO ClubMembers VALUES (1010, 102);
INSERT INTO ClubMembers VALUES (1011, 101);
INSERT INTO ClubMembers VALUES (1011, 104);
INSERT INTO ClubMembers VALUES (1012, 106);

SELECT COUNT(*) AS members_loaded FROM Members;
```

</details>


<div dir="rtl">

---

## 🗺️ הטבלאות והקשרים

| הטבלה | שורות | מפתח ראשי 🔑 | מפתחות זרים 🔗 |
|---|:---:|---|---|
| [`Cities`](#cities) | 6 | `CityCode` | — |
| [`Coaches`](#coaches) | 5 | `CoachCode` | — |
| [`Clubs`](#clubs) | 8 | `ClubCode` | `TrainerCode` → `Coaches(CoachCode)` |
| [`Members`](#members) | 12 | `MemberId` | `TownCode` → `Cities(CityCode)` |
| [`ClubMembers`](#clubmembers) | 18 | `MemberNum`, `ClubNum` | `ClubNum` → `Clubs(ClubCode)`<br>`MemberNum` → `Members(MemberId)` |

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
| 4 | חיפה |
| 5 | נהריה |
| 6 | שפרעם |

---

## Coaches

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `CoachCode` | INTEGER | 🔑 PK |  |
| `CoachFirstName` | TEXT |  | חובה (NOT NULL). |
| `CoachLastName` | TEXT |  | חובה (NOT NULL). |
| `Phone` | TEXT |  | NULL = no phone number |

**הנתונים (5 שורות):**

| CoachCode 🔑 | CoachFirstName | CoachLastName | Phone |
|---|---|---|---|
| 1 | סאמר | חלבי | 050-1111111 |
| 2 | מיכל | לוי | *NULL* |
| 3 | ראמי | עזאם | 054-3333333 |
| 4 | דנה | כהן | 050-4444444 |
| 5 | יוסי | אברהם | 053-5555555 |

---

## Clubs

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `ClubCode` | INTEGER | 🔑 PK |  |
| `ClubName` | TEXT |  | חובה (NOT NULL). |
| `Sport` | TEXT |  | חובה (NOT NULL). |
| `TrainerCode` | INTEGER | 🔗 FK → `Coaches(CoachCode)` |  |
| `Price` | INTEGER |  | חובה (NOT NULL). monthly price in NIS |

**הנתונים (8 שורות):**

| ClubCode 🔑 | ClubName | Sport | TrainerCode 🔗 | Price |
|---|---|---|---|---|
| 100 | כדורגל צעירים | כדורגל | 1 | 150 |
| 101 | כדורגל בוגרים | כדורגל | 1 | 180 |
| 102 | שחייה מתחילים | שחייה | 2 | 220 |
| 103 | שחייה מתקדמים | שחייה | 2 | 250 |
| 104 | כדורסל | כדורסל | 3 | 160 |
| 105 | טניס | טניס | 4 | 300 |
| 106 | ג'ודו | ג'ודו | 3 | 140 |
| 107 | יוגה | יוגה | 4 | 120 |

---

## Members

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `MemberId` | INTEGER | 🔑 PK |  |
| `FirstName` | TEXT |  | חובה (NOT NULL). |
| `LastName` | TEXT |  | חובה (NOT NULL). |
| `TownCode` | INTEGER | 🔗 FK → `Cities(CityCode)` |  |
| `Age` | INTEGER |  |  |
| `JoinYear` | INTEGER |  |  |

**הנתונים (12 שורות):**

| MemberId 🔑 | FirstName | LastName | TownCode 🔗 | Age | JoinYear |
|---|---|---|---|---|---|
| 1001 | אדם | חלבי | 1 | 14 | 2023 |
| 1002 | נור | עזאם | 1 | 15 | 2024 |
| 1003 | יואב | כהן | 3 | 16 | 2022 |
| 1004 | מאיה | לוי | 3 | 15 | 2025 |
| 1005 | רוני | אברהם | 2 | 13 | 2024 |
| 1006 | סאלי | חסון | 2 | 17 | 2023 |
| 1007 | עומר | ביטון | 5 | 15 | 2025 |
| 1008 | שירה | כהן | 4 | 16 | 2022 |
| 1009 | כרים | חלבי | 1 | 13 | 2025 |
| 1010 | תמר | שושן | 5 | 14 | 2023 |
| 1011 | ליאור | לוי | 4 | 17 | 2024 |
| 1012 | ג'וד | מנסור | 1 | 16 | 2025 |

---

## ClubMembers

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `MemberNum` | INTEGER | 🔑 PK · 🔗 FK → `Members(MemberId)` |  |
| `ClubNum` | INTEGER | 🔑 PK · 🔗 FK → `Clubs(ClubCode)` |  |

**הנתונים (18 שורות):**

| MemberNum 🔑🔗 | ClubNum 🔑🔗 |
|---|---|
| 1001 | 100 |
| 1001 | 104 |
| 1002 | 102 |
| 1003 | 101 |
| 1003 | 105 |
| 1004 | 102 |
| 1004 | 106 |
| 1005 | 100 |
| 1006 | 103 |
| 1006 | 104 |
| 1007 | 100 |
| 1008 | 105 |
| 1009 | 100 |
| 1009 | 106 |
| 1010 | 102 |
| 1011 | 101 |
| 1011 | 104 |
| 1012 | 106 |

</div>
