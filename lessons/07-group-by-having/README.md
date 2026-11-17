<div dir="rtl">

# שיעור 7 — GROUP BY ו‑HAVING — קיבוץ

[➡️ השיעור הקודם](../06-aggregates/README.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../08-joins/README.md)

> 🎯 **בשיעור הזה:** לחשב ספירה/סכום/ממוצע **לכל קבוצה**, ולסנן קבוצות עם `HAVING`
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
SELECT   group_col, COUNT(*), AVG(num_col)
FROM     table_name
WHERE    row_condition          -- 1. filter ROWS   (before grouping)
GROUP BY group_col              -- 2. make groups
HAVING   COUNT(*) >= 2          -- 3. filter GROUPS (after grouping)
ORDER BY COUNT(*) DESC;         -- 4. sort
```

<div dir="rtl">

- כל עמודה ב‑`SELECT` שאינה בתוך פונקציה מצרפית — **חייבת** להופיע ב‑`GROUP BY`.
- `WHERE` מסנן **שורות** (לפני הקיבוץ). `HAVING` מסנן **קבוצות** (אחרי הקיבוץ).
- פונקציה מצרפית בתנאי? ← `HAVING`, לא `WHERE`.
- מספר השורות בתוצאה = מספר הקבוצות.

</div>

<div dir="rtl">

---

## 4️⃣ דוגמאות פתורות

> קראו את השאלה, נסו לכתוב בעצמכם, ורק אז הסתכלו על הפתרון והתוצאה.

</div>

<div dir="rtl">

### דוגמה 1: כמה תלמידים גרים בכל עיר?

</div>

```sql
SELECT   HomeTown, COUNT(*) AS Pupils
FROM     Pupils
GROUP BY HomeTown;
```

<div dir="rtl">

| HomeTown | Pupils |
|---|---|
| 1 | 3 |
| 2 | 3 |
| 3 | 2 |
| 4 | 2 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### דוגמה 2: לכל מורה: מספר הרישומים והתשלום הממוצע.

</div>

```sql
SELECT   RegTeacher, COUNT(*) AS Regs, AVG(MonthlyFee) AS AvgFee
FROM     Registrations
GROUP BY RegTeacher;
```

<div dir="rtl">

| RegTeacher | Regs | AvgFee |
|---|---|---|
| 1 | 3 | 313.33 |
| 2 | 3 | 386.67 |
| 3 | 3 | 320.0 |
| 4 | 2 | 355.0 |
| 5 | 3 | 286.67 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### דוגמה 3: מורים שיש להם **לפחות 3** רישומים.

</div>

```sql
SELECT   RegTeacher, COUNT(*) AS Regs
FROM     Registrations
GROUP BY RegTeacher
HAVING   COUNT(*) >= 3;
```

<div dir="rtl">

| RegTeacher | Regs |
|---|---|
| 1 | 3 |
| 2 | 3 |
| 3 | 3 |
| 5 | 3 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### דוגמה 4: לכל רמה — כמה רישומים מ‑2024 ואילך, רק רמות עם יותר מרישום אחד, מהגדולה לקטנה.

</div>

```sql
SELECT   PupilLevel, COUNT(*) AS Regs
FROM     Registrations
WHERE    RegYear >= 2024
GROUP BY PupilLevel
HAVING   COUNT(*) > 1
ORDER BY Regs DESC;
```

<div dir="rtl">

| PupilLevel | Regs |
|---|---|
| מתחיל | 5 |
| ממשיך | 4 |

**התוצאה: 2 שורות**

> 💡 שימו לב לסדר: `WHERE` → `GROUP BY` → `HAVING` → `ORDER BY`.

</div>

<div dir="rtl">

---

## 5️⃣ שאלות: מה תחזיר השאילתה?

> בלי להריץ! כתבו על דף את הטבלה שתתקבל (או רק את מספר השורות). אחר כך הריצו ובדקו. התשובות ב[פתרונות](solutions.md).

</div>

<div dir="rtl">

**שאלה 1.** כמה שורות יחזרו, ומה המספרים?

</div>

```sql
SELECT   PupilLevel, COUNT(*)
FROM     Registrations
GROUP BY PupilLevel;
```

<div dir="rtl">

**שאלה 2.** אילו תלמידים יחזרו?

</div>

```sql
SELECT   RegPupil, COUNT(*)
FROM     Registrations
GROUP BY RegPupil
HAVING   COUNT(*) = 2;
```

<div dir="rtl">

**שאלה 3.** כמה שורות יחזרו?

</div>

```sql
SELECT   TeachInst, MAX(HourRate)
FROM     Teachers
GROUP BY TeachInst;
```

<div dir="rtl">

**שאלה 4.** איזו טבלה תתקבל?

</div>

```sql
SELECT   LockerFloor, COUNT(*)
FROM     Lockers
GROUP BY LockerFloor;
```

<div dir="rtl">

**שאלה 5.** אילו שנים יחזרו?

</div>

```sql
SELECT   RegYear, COUNT(*)
FROM     Registrations
GROUP BY RegYear
HAVING   COUNT(*) >= 4;
```

<div dir="rtl">

---

## 6️⃣ תרגילים — 🎵 בית הספר למוזיקה "צלילים"

> כתבו שאילתה לכל סעיף והריצו. **🔢 מספר השורות הצפוי** עוזר לבדוק את עצמכם. 🟢 קל · 🟡 בינוני · 🔴 מאתגר

1. 🟢 כמה מורים מלמדים כל כלי (`TeachInst`)? _(🔢 5 שורות)_

2. 🟢 כמה תלמידים נולדו בכל שנה? _(🔢 6 שורות)_

3. 🟢 מה סכום התשלומים החודשיים בכל שנת רישום? _(🔢 5 שורות)_

4. 🟡 לכל תלמיד (`RegPupil`): בכמה שיעורים הוא רשום וכמה הוא משלם בסך הכול בחודש? _(🔢 10 שורות)_

5. 🟡 לכל רמה: התשלום הנמוך והגבוה ביותר. _(🔢 3 שורות)_

6. 🟡 ערים (`HomeTown`) שגרים בהן **יותר מ‑2** תלמידים. _(🔢 2 שורות)_

7. 🟡 תלמידים שמשלמים בסך הכול **יותר מ‑600** בחודש. _(🔢 3 שורות)_

8. 🔴 מורים שהתשלום הממוצע אצלם **מעל 330**, ממוינים מהממוצע הגבוה לנמוך. _(🔢 2 שורות)_

9. 🔴 רק ברישומים שאינם 'מתחיל': כמה רישומים יש לכל מורה? הציגו רק מורים עם 2 רישומים כאלה לפחות. _(🔢 3 שורות)_

10. 🔴 לכל שנה ולכל רמה (קיבוץ לפי שתי עמודות): כמה רישומים? ממוין לפי שנה. _(🔢 5 שורות)_

11. 🟢 כמה כלים יש בכל משפחת כלים? _(🔢 4 שורות)_

12. 🟢 כמה לוקרים יש בכל קומה? _(🔢 2 שורות)_

13. 🟡 לכל מורה: התשלום הגבוה ביותר שמשלמים לו. _(🔢 5 שורות)_

14. 🟡 שנים שהיו בהן לפחות 3 רישומים. _(🔢 2 שורות)_

15. 🟡 לכל עיר: שנת הלידה של התלמיד הצעיר ביותר. _(🔢 4 שורות)_

16. 🔴 כלים (`TeachInst`) שמלמדים אותם יותר ממורה אחד. _(🔢 שורה אחת)_

17. 🔴 לכל מורה — רק ברישומים מ‑2024 ואילך — סכום התשלומים. הציגו מורים עם סכום מעל 500, מהגבוה לנמוך. _(🔢 3 שורות)_

</div>

<div dir="rtl">

---

## 7️⃣ 🎓 בסגנון הבחינה — 🔧 מעבדת "דלתא‑טק"

> שאלות בפורמט של שאלון 735911: שמות שדות ייחודיים, צירוף עם פסיק + `WHERE`, השלמת ערכים, זיהוי שאילתה לפי פלט והשלמת פקודות. [📋 הטבלאות והקוד](../../databases/repairs/)

</div>

<details>
<summary>📋 <b>הטבלאות של מעבדת "דלתא‑טק"</b> (לחצו לפתיחה)</summary>

<div dir="rtl">

**`Cities`**

| CityCode 🔑 | CityName |
|---|---|
| 1 | ירכא |
| 2 | עכו |
| 3 | כרמיאל |
| 4 | נהריה |
| 5 | שפרעם |
| 6 | מעלות |

**`DevTypes`**

| DevCode 🔑 | DevName | DevFamily |
|---|---|---|
| 10 | טלפון חכם | סלולר |
| 20 | מחשב נייד | מחשבים |
| 30 | טאבלט | סלולר |
| 40 | שעון חכם | לבישים |
| 50 | אוזניות | לבישים |
| 60 | קונסולת משחק | מחשבים |

**`Parts`**

| PartCode 🔑 | PartName | PartPrice |
|---|---|---|
| 101 | מסך | 450 |
| 102 | סוללה | 180 |
| 103 | שקע טעינה | 90 |
| 104 | רמקול | 70 |
| 105 | מקלדת | 220 |
| 106 | מצלמה | 160 |
| 107 | כבל שטוח | 45 |

**`Technicians`**

| TechCode 🔑 | TechFirst | TechLast | TechCity 🔗 | StartDate | HourWage | TechPhone |
|---|---|---|---|---|---|---|
| 1 | נביל | סרחאן | 1 | 2019-03-01 | 95 | 050-7010101 |
| 2 | רונית | בר-לב | 4 | 2021-09-15 | 80 | *NULL* |
| 3 | חוסאם | זיאד | 5 | 2020-01-12 | 88 | 054-7030303 |
| 4 | דנה | כהן | 1 | 2023-06-01 | 72 | 052-7040404 |
| 5 | סאמר | חלבי | 1 | 2018-11-20 | 105 | *NULL* |
| 6 | מאיה | אברהם | 6 | 2024-02-10 | 65 | 053-7060606 |
| 7 | ליאן | קבלאן | 2 | 2022-05-05 | 80 | 050-7070707 |

**`Repairs`**

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

**`Benches`**

| BenchNum 🔑 | BenchTech 🔗 | BenchFloor |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 3 | 1 |
| 3 | 5 | 2 |
| 4 | 7 | 2 |
| 5 | 4 | 2 |

**`PartUsage`**

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

</details>


<details>
<summary>📥 <b>הקוד שבונה את בסיס הנתונים 🔧 מעבדת "דלתא‑טק"</b> — מעתיקים הכול ומדביקים ב‑OneCompiler</summary>

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

**שאלה 1.** 🟢 ✍️ כמה תיקונים יש בכל רמת עדיפות? _(🔢 3 שורות)_

</div>

<div dir="rtl">

**שאלה 2.** 🟢 ✍️ לכל טכנאי (`RepairTech`): סך מחירי התיקונים שלו. _(🔢 7 שורות)_

</div>

<div dir="rtl">

**שאלה 3.** 🟡 ✍️ סוגי מכשירים (`RepairDev`) שתוקנו 3 פעמים או יותר. _(🔢 2 שורות)_

</div>

<div dir="rtl">

**שאלה 4.** 🟡 ✍️ לכל עיר (`TechCity`): מספר הטכנאים והשכר הממוצע לשעה. _(🔢 5 שורות)_

</div>

<div dir="rtl">

**שאלה 5.** 🟡 🧮 **השלימו את הערכים:** השלימו את הערכים בטבלה שתתקבל.

</div>

```sql
SELECT   BenchFloor, COUNT(*)
FROM     Benches
GROUP BY BenchFloor;
```

<div dir="rtl">

**שאלה 6.** 🔴 🔎 **איזו שאילתה הציגה את הטבלה?**

</div>

<div dir="rtl">

| RepairTech | N |
|---|---|
| 1 | 1 |
| 3 | 1 |
| 4 | 1 |

</div>

<div dir="rtl">

**שאלה 7.** 🔴 🧩 **השלימו את הפקודה:** השלימו כך שיוצגו הטכנאים שהמחיר הממוצע של התיקונים שלהם מעל 600.

</div>

```sql
SELECT   RepairTech, AVG(RepairPrice)
FROM     Repairs
_____ __ __________
______   ___(RepairPrice) > 600;
```

<div dir="rtl">

---

## 8️⃣ תרגול נוסף — 🏫 בית הספר "עתיד"

> בסיס נתונים אחר, שאתם לא מכירים — בדיוק כמו בבחינה. [📋 הטבלאות והקוד של בית הספר "עתיד"](../../databases/school/)

1. 🟢 כמה תלמידים יש בכל כיתה (`ClassCode`)? _(🔢 6 שורות)_

2. 🟢 כמה מורים מלמדים כל מקצוע (`Subject`)? _(🔢 6 שורות)_

3. 🟡 הציון הממוצע (מעוגל לספרה אחת) של כל תלמיד במחצית 1. _(🔢 17 שורות)_

4. 🟡 תלמידים עם **3 היעדרויות או יותר**. _(🔢 2 שורות)_

5. 🔴 מקצועות (`CourseCode`) שהממוצע בהם במחצית 1 **מתחת ל‑75**. _(🔢 2 שורות)_

6. 🔴 כמה בנים וכמה בנות יש בכל כיתה? _(🔢 11 שורות)_

7. 🟢 כמה כיתות יש בכל שכבה? _(🔢 3 שורות)_

8. 🟡 לכל עיר (`CityCode`): כמה תלמידים, רק ערים עם 3 תלמידים ומעלה. _(🔢 4 שורות)_

9. 🟡 לכל מחצית: מספר הציונים והציון הממוצע (מעוגל). _(🔢 2 שורות)_

10. 🔴 תלמידים שהציון הנמוך ביותר שלהם במחצית 1 הוא מתחת ל‑55. _(🔢 3 שורות)_

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

[➡️ השיעור הקודם](../06-aggregates/README.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../08-joins/README.md)

</div>
