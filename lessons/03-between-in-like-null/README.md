<div dir="rtl">

# שיעור 3 — BETWEEN, IN, LIKE ו‑NULL

[➡️ השיעור הקודם](../02-where/README.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../04-order-by/README.md)

> 🎯 **בשיעור הזה:** טווח (`BETWEEN`), רשימה (`IN`), חיפוש טקסט (`LIKE`) וערך חסר (`IS NULL`)
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

---

## 3️⃣ התחביר בקצרה

</div>

```sql
WHERE HourRate BETWEEN 110 AND 140     -- 110 <= x <= 140   (both ends included!)
WHERE HomeTown IN (1, 3, 4)            -- same as  = 1 OR = 3 OR = 4
WHERE HomeTown NOT IN (1, 3)

WHERE LastName LIKE 'כ%'              -- starts with כ
WHERE LastName LIKE '%ן'              -- ends with ן
WHERE LastName LIKE '%ל%'             -- contains ל
WHERE FirstName LIKE '___'            -- exactly 3 letters   ( _ = one letter )

WHERE TeacherPhone IS NULL            -- empty value
WHERE TeacherPhone IS NOT NULL
```

<div dir="rtl">

- `BETWEEN` **כולל** את שני הקצוות.
- `%` = כל רצף של תווים (גם ריק). `_` = **תו אחד בדיוק**.
- ⚠️ `= NULL` **לא עובד** ומחזיר 0 שורות. תמיד `IS NULL` / `IS NOT NULL`.
- NULL אינו 0 ואינו טקסט ריק — זה **"אין ערך"**.

</div>

<div dir="rtl">

---

## 4️⃣ דוגמאות פתורות

> קראו את השאלה, נסו לכתוב בעצמכם, ורק אז הסתכלו על הפתרון והתוצאה.

</div>

<div dir="rtl">

### דוגמה 1: מורים שהמחיר שלהם בין 110 ל‑140 (כולל).

</div>

```sql
SELECT TeacherName, HourRate
FROM   Teachers
WHERE  HourRate BETWEEN 110 AND 140;
```

<div dir="rtl">

| TeacherName | HourRate |
|---|---|
| סמיר חלבי | 120 |
| אמיר עזאם | 110 |
| דנה כהן | 140 |
| נור מנסור | 130 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### דוגמה 2: תלמידים שגרים בערים 2 או 4.

</div>

```sql
SELECT FirstName, HomeTown
FROM   Pupils
WHERE  HomeTown IN (2, 4);
```

<div dir="rtl">

| FirstName | HomeTown |
|---|---|
| שירה | 2 |
| רמי | 2 |
| תמר | 4 |
| עומר | 4 |
| יואב | 2 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### דוגמה 3: תלמידים ששם המשפחה שלהם מתחיל ב‑ח.

</div>

```sql
SELECT FirstName, LastName
FROM   Pupils
WHERE  LastName LIKE 'ח%';
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| אדם | חלבי |
| רמי | חורי |
| סאלי | חסון |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### דוגמה 4: מורים שאין להם טלפון.

</div>

```sql
SELECT TeacherName, TeacherPhone
FROM   Teachers
WHERE  TeacherPhone IS NULL;
```

<div dir="rtl">

| TeacherName | TeacherPhone |
|---|---|
| אמיר עזאם | *NULL* |
| נור מנסור | *NULL* |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

---

## 5️⃣ שאלות: מה תחזיר השאילתה?

> בלי להריץ! כתבו על דף את הטבלה שתתקבל (או רק את מספר השורות). אחר כך הריצו ובדקו. התשובות ב[פתרונות](solutions.md).

</div>

<div dir="rtl">

**שאלה 1.** כמה שורות יחזרו?

</div>

```sql
SELECT TeacherName
FROM   Teachers
WHERE  TeacherPhone = NULL;
```

<div dir="rtl">

**שאלה 2.** כמה שורות יחזרו?

</div>

```sql
SELECT FirstName
FROM   Pupils
WHERE  BirthYear BETWEEN 2010 AND 2012;
```

<div dir="rtl">

**שאלה 3.** אילו שמות יחזרו?

</div>

```sql
SELECT FirstName
FROM   Pupils
WHERE  FirstName LIKE '___';
```

<div dir="rtl">

**שאלה 4.** אילו שמות יחזרו?

</div>

```sql
SELECT FirstName
FROM   Pupils
WHERE  LastName LIKE '%ן';
```

<div dir="rtl">

**שאלה 5.** מה המספר?

</div>

```sql
SELECT COUNT(*)
FROM   Registrations
WHERE  RegTeacher IN (1, 2, 6);
```

<div dir="rtl">

---

## 6️⃣ תרגילים — 🎵 בית הספר למוזיקה "צלילים"

> כתבו שאילתה לכל סעיף והריצו. **🔢 מספר השורות הצפוי** עוזר לבדוק את עצמכם. 🟢 קל · 🟡 בינוני · 🔴 מאתגר

1. 🟢 הציגו תלמידים שנולדו בין 2011 ל‑2013 (כולל). _(🔢 5 שורות)_

2. 🟢 הציגו מורים שיש להם טלפון. _(🔢 4 שורות)_

3. 🟢 הציגו רישומים ששולם בהם 300, 320 או 340 לחודש. השתמשו ב‑`IN`. _(🔢 7 שורות)_

4. 🟢 הציגו תלמידים ששם המשפחה שלהם מכיל את האות 'ו'. _(🔢 5 שורות)_

5. 🟡 הציגו תלמידים שלא גרים בערים 1 ו‑2. _(🔢 4 שורות)_

6. 🟡 הציגו מורים ששמם (`TeacherName`) מסתיים באות 'י'. _(🔢 2 שורות)_

7. 🟡 הציגו תלמידים ששמם הפרטי בן 4 אותיות בדיוק. _(🔢 7 שורות)_

8. 🟡 הציגו רישומים שהתשלום בהם **לא** בין 300 ל‑350. _(🔢 6 שורות)_

9. 🔴 הציגו מורים בלי טלפון שהמחיר שלהם מעל 120. _(🔢 שורה אחת)_

10. 🔴 הציגו את שם המורה והטלפון של מורים שהטלפון שלהם מתחיל ב‑050 או ב‑052. _(🔢 2 שורות)_

11. 🔴 הציגו תלמידים מהערים 1, 3 שנולדו בין 2010 ל‑2012 ושמם הפרטי מכיל 'א'. _(🔢 3 שורות)_

12. 🟢 הציגו את הכלים ממשפחות 'הקשה' או 'נשיפה' (עם `IN`). _(🔢 2 שורות)_

13. 🟢 הציגו מורים שהמחיר שלהם בין 100 ל‑120. _(🔢 3 שורות)_

14. 🟡 הציגו תלמידים ששמם הפרטי מתחיל ב‑'ש' או ב‑'ס'. _(🔢 2 שורות)_

15. 🟡 הציגו רישומים משנים 2021–2023 (עם `BETWEEN`). _(🔢 5 שורות)_

16. 🟡 הציגו מורים ששמם הפרטי (המילה הראשונה) בן 3 אותיות בדיוק (רמז: `'___ %'`). _(🔢 2 שורות)_

17. 🔴 הציגו את המורים בלי טלפון, או שהמחיר שלהם לא בין 110 ל‑140. _(🔢 4 שורות)_

18. 🔴 הציגו רישומים של תלמידים 201–205 שאינם ברמת 'מתחיל'. _(🔢 4 שורות)_

</div>

<div dir="rtl">

---

## 7️⃣ 🎓 בסגנון הבחינה — 📚 ספרייה עירונית

> שאלות בפורמט של שאלון 735911: שמות שדות ייחודיים, צירוף עם פסיק + `WHERE`, השלמת ערכים, זיהוי שאילתה לפי פלט והשלמת פקודות. [📋 הטבלאות והקוד](../../databases/library/)

</div>

<details>
<summary>📋 <b>הטבלאות של ספרייה עירונית</b> (לחצו לפתיחה)</summary>

<div dir="rtl">

**`Cities`**

| CityCode 🔑 | CityName |
|---|---|
| 1 | ירכא |
| 2 | כרמיאל |
| 3 | עכו |
| 4 | מעלות |
| 5 | חיפה |

**`Authors`**

| AuthorCode 🔑 | AuthorFirstName | AuthorLastName | Country |
|---|---|---|---|
| 1 | עמוס | עוז | ישראל |
| 2 | ג'ואן | רולינג | בריטניה |
| 3 | נגיב | מחפוז | מצרים |
| 4 | אגתה | כריסטי | בריטניה |
| 5 | דויד | גרוסמן | ישראל |
| 6 | סמי | מיכאל | ישראל |

**`Books`**

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

**`Members`**

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

**`Loans`**

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

</details>


<details>
<summary>📥 <b>הקוד שבונה את בסיס הנתונים 📚 ספרייה עירונית</b> — מעתיקים הכול ומדביקים ב‑OneCompiler</summary>

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

**שאלה 1.** 🟢 ✍️ הציגו את הספרים שיצאו בין 1990 ל‑2010. _(🔢 5 שורות)_

</div>

<div dir="rtl">

**שאלה 2.** 🟢 ✍️ הציגו את ההשאלות שעדיין לא הוחזרו. _(🔢 8 שורות)_

</div>

<div dir="rtl">

**שאלה 3.** 🟡 ✍️ הציגו את הסופרים מישראל או ממצרים (עם `IN`). _(🔢 4 שורות)_

</div>

<div dir="rtl">

**שאלה 4.** 🟡 ✍️ הציגו ספרים ששמם מכיל את המילה 'הארי'. _(🔢 2 שורות)_

</div>

<div dir="rtl">

**שאלה 5.** 🟡 🔎 **איזו שאילתה הציגה את הטבלה?**

</div>

<div dir="rtl">

| FirstName | LastName |
|---|---|
| עידו | כהן |
| הילה | כהן |

</div>

<div dir="rtl">

**שאלה 6.** 🟡 🧮 **השלימו את הערכים:** השלימו את הערכים בטבלה שתתקבל.

</div>

```sql
SELECT Title
FROM   Books
WHERE  Genre = 'מתח' AND Pages BETWEEN 250 AND 300;
```

<div dir="rtl">

**שאלה 7.** 🔴 🧩 **השלימו את הפקודה:** השלימו כך שיוצגו ההשאלות מאוקטובר 2025 שכבר הוחזרו.

</div>

```sql
SELECT LoanId
FROM   Loans
WHERE  LoanDate ____ '2025-10_' AND ReturnDate __ ___ ____;
```

<div dir="rtl">

---

## 8️⃣ תרגול נוסף — 🏫 בית הספר "עתיד"

> בסיס נתונים אחר, שאתם לא מכירים — בדיוק כמו בבחינה. [📋 הטבלאות והקוד של בית הספר "עתיד"](../../databases/school/)

1. 🟢 הציגו תלמידים שאין להם טלפון. _(🔢 6 שורות)_

2. 🟢 הציגו ציונים בין 90 ל‑100. _(🔢 21 שורות)_

3. 🟡 הציגו ציונים חסרים (תלמיד לא נבחן). _(🔢 2 שורות)_

4. 🟡 הציגו תלמידים שנולדו בשנת 2010 (רמז: `LIKE '2010%'`). _(🔢 7 שורות)_

5. 🟡 הציגו מקצועות ששמם מכיל את המילה 'מתמטיקה'. _(🔢 2 שורות)_

6. 🔴 הציגו תלמידים שעדיין לא שובצו לכיתה, או שתאריך הלידה שלהם חסר. _(🔢 2 שורות)_

7. 🟢 הציגו כיתות שעדיין לא שובצה להן כיתת אם (`RoomNumber`). _(🔢 שורה אחת)_

8. 🟡 הציגו היעדרויות שלא נמסרה להן סיבה. _(🔢 9 שורות)_

9. 🟡 הציגו מורים שהתחילו לעבוד בין 2015 ל‑2022. _(🔢 3 שורות)_

10. 🔴 הציגו תלמידים ששם המשפחה שלהם מכיל '-' או מתחיל ב‑'ח'. _(🔢 4 שורות)_

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

[➡️ השיעור הקודם](../02-where/README.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../04-order-by/README.md)

</div>
