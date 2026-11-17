<div dir="rtl">

# 📚 ספרייה עירונית

> ספרים, סופרים, קוראים והשאלות (עם תאריכים).
>
> **שימוש:** בחינה לדוגמה 2 · **5 טבלאות**

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

קובץ: [`library.sql`](library.sql) · [פתיחה כטקסט נקי (Ctrl+A, Ctrl+C)](https://raw.githubusercontent.com/AhmadKais/sql-course-heb/main/databases/library/library.sql)

</div>

<details>
<summary>📥 <b>לחצו כאן לקוד שבונה את בסיס הנתונים 📚 ספרייה עירונית</b> — מעתיקים הכול ומדביקים ב‑OneCompiler</summary>

```sql
-- ============================================================
--  ספרייה עירונית  ·  בסיס נתונים לבחינה לדוגמה 2
--  הדביקו את כל הקובץ ב-OneCompiler, לחצו Run, וכתבו את השאילתות מתחת.
-- ============================================================
DROP TABLE IF EXISTS Loans;
DROP TABLE IF EXISTS Members;
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Authors;
DROP TABLE IF EXISTS Cities;

CREATE TABLE Cities (
  CityCode  INTEGER PRIMARY KEY,
  CityName  TEXT NOT NULL
);
INSERT INTO Cities VALUES (1, 'ירכא');
INSERT INTO Cities VALUES (2, 'כרמיאל');
INSERT INTO Cities VALUES (3, 'עכו');
INSERT INTO Cities VALUES (4, 'מעלות');
INSERT INTO Cities VALUES (5, 'חיפה');

CREATE TABLE Authors (
  AuthorCode       INTEGER PRIMARY KEY,
  AuthorFirstName  TEXT NOT NULL,
  AuthorLastName   TEXT NOT NULL,
  Country          TEXT
);
INSERT INTO Authors VALUES (1, 'עמוס',  'עוז',     'ישראל');
INSERT INTO Authors VALUES (2, 'ג''ואן', 'רולינג',  'בריטניה');
INSERT INTO Authors VALUES (3, 'נגיב',  'מחפוז',   'מצרים');
INSERT INTO Authors VALUES (4, 'אגתה',  'כריסטי',  'בריטניה');
INSERT INTO Authors VALUES (5, 'דויד',  'גרוסמן',  'ישראל');
INSERT INTO Authors VALUES (6, 'סמי',   'מיכאל',   'ישראל');

CREATE TABLE Books (
  BookCode    INTEGER PRIMARY KEY,
  Title       TEXT NOT NULL,
  WriterCode  INTEGER REFERENCES Authors(AuthorCode),
  Genre       TEXT,
  PubYear     INTEGER,
  Pages       INTEGER
);
INSERT INTO Books VALUES (201, 'סיפור על אהבה וחושך',     1, 'ביוגרפיה', 2002, 520);
INSERT INTO Books VALUES (202, 'הארי פוטר ואבן החכמים',   2, 'פנטזיה',   1997, 320);
INSERT INTO Books VALUES (203, 'הארי פוטר וחדר הסודות',   2, 'פנטזיה',   1998, 350);
INSERT INTO Books VALUES (204, 'סמטת מדק',               3, 'רומן',     1947, 280);
INSERT INTO Books VALUES (205, 'רצח באוריינט אקספרס',     4, 'מתח',      1934, 250);
INSERT INTO Books VALUES (206, 'ואז לא נשאר אף אחד',      4, 'מתח',      1939, 260);
INSERT INTO Books VALUES (207, 'סוס אחד נכנס לבר',        5, 'רומן',     2014, 200);
INSERT INTO Books VALUES (208, 'אשה בורחת מבשורה',       5, 'רומן',     2008, 640);
INSERT INTO Books VALUES (209, 'מיכאל שלי',              1, 'רומן',     1968, 290);
INSERT INTO Books VALUES (210, 'ספר הדקדוק הפנימי',       5, 'רומן',     1991, 380);

CREATE TABLE Members (
  MemberId   INTEGER PRIMARY KEY,
  FirstName  TEXT NOT NULL,
  LastName   TEXT NOT NULL,
  TownCode   INTEGER REFERENCES Cities(CityCode),
  BirthYear  INTEGER
);
INSERT INTO Members VALUES (501, 'ראניה',  'חלבי',   1, 2008);
INSERT INTO Members VALUES (502, 'עידו',   'כהן',    2, 2007);
INSERT INTO Members VALUES (503, 'מוחמד',  'עזאם',   1, 2009);
INSERT INTO Members VALUES (504, 'נועה',   'לוי',    3, 2008);
INSERT INTO Members VALUES (505, 'אליאס',  'חורי',   3, 2006);
INSERT INTO Members VALUES (506, 'יעל',    'פרץ',    2, 2009);
INSERT INTO Members VALUES (507, 'סאמי',   'קבלאן',  4, 2007);
INSERT INTO Members VALUES (508, 'הילה',   'כהן',    5, 2008);
INSERT INTO Members VALUES (509, 'אמיר',   'חלבי',   1, 2006);
INSERT INTO Members VALUES (510, 'רותם',   'גבאי',   4, 2009);

CREATE TABLE Loans (
  LoanId      INTEGER PRIMARY KEY,
  ReaderId    INTEGER REFERENCES Members(MemberId),
  BookNum     INTEGER REFERENCES Books(BookCode),
  LoanDate    TEXT NOT NULL,          -- 'YYYY-MM-DD'
  ReturnDate  TEXT                    -- NULL = not returned yet
);
INSERT INTO Loans VALUES ( 1, 501, 202, '2025-09-01', '2025-09-15');
INSERT INTO Loans VALUES ( 2, 501, 203, '2025-09-16', NULL);
INSERT INTO Loans VALUES ( 3, 502, 205, '2025-09-03', '2025-09-20');
INSERT INTO Loans VALUES ( 4, 503, 202, '2025-09-05', '2025-09-25');
INSERT INTO Loans VALUES ( 5, 504, 207, '2025-09-07', NULL);
INSERT INTO Loans VALUES ( 6, 505, 204, '2025-09-10', '2025-09-30');
INSERT INTO Loans VALUES ( 7, 502, 206, '2025-09-21', NULL);
INSERT INTO Loans VALUES ( 8, 506, 202, '2025-09-26', NULL);
INSERT INTO Loans VALUES ( 9, 507, 209, '2025-10-01', '2025-10-12');
INSERT INTO Loans VALUES (10, 501, 205, '2025-10-02', NULL);
INSERT INTO Loans VALUES (11, 508, 201, '2025-10-03', NULL);
INSERT INTO Loans VALUES (12, 505, 204, '2025-10-05', NULL);
INSERT INTO Loans VALUES (13, 503, 207, '2025-10-06', '2025-10-20');
INSERT INTO Loans VALUES (14, 509, 208, '2025-10-08', NULL);

SELECT COUNT(*) AS loans_loaded FROM Loans;
```

</details>


<div dir="rtl">

---

## 🗺️ הטבלאות והקשרים

| הטבלה | שורות | מפתח ראשי 🔑 | מפתחות זרים 🔗 |
|---|:---:|---|---|
| [`Cities`](#cities) | 5 | `CityCode` | — |
| [`Authors`](#authors) | 6 | `AuthorCode` | — |
| [`Books`](#books) | 10 | `BookCode` | `WriterCode` → `Authors(AuthorCode)` |
| [`Members`](#members) | 10 | `MemberId` | `TownCode` → `Cities(CityCode)` |
| [`Loans`](#loans) | 14 | `LoanId` | `BookNum` → `Books(BookCode)`<br>`ReaderId` → `Members(MemberId)` |

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
| 2 | כרמיאל |
| 3 | עכו |
| 4 | מעלות |
| 5 | חיפה |

---

## Authors

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `AuthorCode` | INTEGER | 🔑 PK |  |
| `AuthorFirstName` | TEXT |  | חובה (NOT NULL). |
| `AuthorLastName` | TEXT |  | חובה (NOT NULL). |
| `Country` | TEXT |  |  |

**הנתונים (6 שורות):**

| AuthorCode 🔑 | AuthorFirstName | AuthorLastName | Country |
|---|---|---|---|
| 1 | עמוס | עוז | ישראל |
| 2 | ג'ואן | רולינג | בריטניה |
| 3 | נגיב | מחפוז | מצרים |
| 4 | אגתה | כריסטי | בריטניה |
| 5 | דויד | גרוסמן | ישראל |
| 6 | סמי | מיכאל | ישראל |

---

## Books

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `BookCode` | INTEGER | 🔑 PK |  |
| `Title` | TEXT |  | חובה (NOT NULL). |
| `WriterCode` | INTEGER | 🔗 FK → `Authors(AuthorCode)` |  |
| `Genre` | TEXT |  |  |
| `PubYear` | INTEGER |  |  |
| `Pages` | INTEGER |  |  |

**הנתונים (10 שורות):**

| BookCode 🔑 | Title | WriterCode 🔗 | Genre | PubYear | Pages |
|---|---|---|---|---|---|
| 201 | סיפור על אהבה וחושך | 1 | ביוגרפיה | 2002 | 520 |
| 202 | הארי פוטר ואבן החכמים | 2 | פנטזיה | 1997 | 320 |
| 203 | הארי פוטר וחדר הסודות | 2 | פנטזיה | 1998 | 350 |
| 204 | סמטת מדק | 3 | רומן | 1947 | 280 |
| 205 | רצח באוריינט אקספרס | 4 | מתח | 1934 | 250 |
| 206 | ואז לא נשאר אף אחד | 4 | מתח | 1939 | 260 |
| 207 | סוס אחד נכנס לבר | 5 | רומן | 2014 | 200 |
| 208 | אשה בורחת מבשורה | 5 | רומן | 2008 | 640 |
| 209 | מיכאל שלי | 1 | רומן | 1968 | 290 |
| 210 | ספר הדקדוק הפנימי | 5 | רומן | 1991 | 380 |

---

## Members

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `MemberId` | INTEGER | 🔑 PK |  |
| `FirstName` | TEXT |  | חובה (NOT NULL). |
| `LastName` | TEXT |  | חובה (NOT NULL). |
| `TownCode` | INTEGER | 🔗 FK → `Cities(CityCode)` |  |
| `BirthYear` | INTEGER |  |  |

**הנתונים (10 שורות):**

| MemberId 🔑 | FirstName | LastName | TownCode 🔗 | BirthYear |
|---|---|---|---|---|
| 501 | ראניה | חלבי | 1 | 2008 |
| 502 | עידו | כהן | 2 | 2007 |
| 503 | מוחמד | עזאם | 1 | 2009 |
| 504 | נועה | לוי | 3 | 2008 |
| 505 | אליאס | חורי | 3 | 2006 |
| 506 | יעל | פרץ | 2 | 2009 |
| 507 | סאמי | קבלאן | 4 | 2007 |
| 508 | הילה | כהן | 5 | 2008 |
| 509 | אמיר | חלבי | 1 | 2006 |
| 510 | רותם | גבאי | 4 | 2009 |

---

## Loans

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `LoanId` | INTEGER | 🔑 PK |  |
| `ReaderId` | INTEGER | 🔗 FK → `Members(MemberId)` |  |
| `BookNum` | INTEGER | 🔗 FK → `Books(BookCode)` |  |
| `LoanDate` | TEXT |  | חובה (NOT NULL). 'YYYY-MM-DD' |
| `ReturnDate` | TEXT |  | NULL = not returned yet |

**הנתונים (14 שורות):**

| LoanId 🔑 | ReaderId 🔗 | BookNum 🔗 | LoanDate | ReturnDate |
|---|---|---|---|---|
| 1 | 501 | 202 | 2025-09-01 | 2025-09-15 |
| 2 | 501 | 203 | 2025-09-16 | *NULL* |
| 3 | 502 | 205 | 2025-09-03 | 2025-09-20 |
| 4 | 503 | 202 | 2025-09-05 | 2025-09-25 |
| 5 | 504 | 207 | 2025-09-07 | *NULL* |
| 6 | 505 | 204 | 2025-09-10 | 2025-09-30 |
| 7 | 502 | 206 | 2025-09-21 | *NULL* |
| 8 | 506 | 202 | 2025-09-26 | *NULL* |
| 9 | 507 | 209 | 2025-10-01 | 2025-10-12 |
| 10 | 501 | 205 | 2025-10-02 | *NULL* |
| 11 | 508 | 201 | 2025-10-03 | *NULL* |
| 12 | 505 | 204 | 2025-10-05 | *NULL* |
| 13 | 503 | 207 | 2025-10-06 | 2025-10-20 |
| 14 | 509 | 208 | 2025-10-08 | *NULL* |

</div>
