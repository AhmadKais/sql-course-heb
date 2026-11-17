<div dir="rtl">

# שיעור 14 — סימולציית בחינה — כל הנושאים

[➡️ השיעור הקודם](../13-create-alter-drop/README.md) · [🏠 כל השיעורים](../README.md)

> 🎯 **בשיעור הזה:** תרגול מסכם בסגנון שאלון 735911 על בסיס נתונים חדש: שליפה, קיבוץ, צירוף, תת‑שאילתה, VIEW ושינוי נתונים
>
> 🗄️ **בסיס הנתונים:** ⚽ [חוגי ספורט עירוניים](../../databases/clubs/) · ✅ [הפתרונות](solutions.md)

---

## 1️⃣ טוענים את בסיס הנתונים

פותחים את [OneCompiler — SQLite](https://onecompiler.com/sqlite), מדביקים את **כל** הקוד, ומתחתיו כותבים את השאילתות.

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

## 2️⃣ הטבלאות שעובדים איתן

> 🔑 = מפתח ראשי · 🔗 = מפתח זר. לכל הטבלאות: [בסיס הנתונים המלא](../../databases/clubs/)

**`Cities`**

| CityCode 🔑 | CityName |
|---|---|
| 1 | ירכא |
| 2 | עכו |
| 3 | כרמיאל |
| 4 | חיפה |
| 5 | נהריה |
| 6 | שפרעם |

**`Coaches`**

| CoachCode 🔑 | CoachFirstName | CoachLastName | Phone |
|---|---|---|---|
| 1 | סאמר | חלבי | 050-1111111 |
| 2 | מיכל | לוי | *NULL* |
| 3 | ראמי | עזאם | 054-3333333 |
| 4 | דנה | כהן | 050-4444444 |
| 5 | יוסי | אברהם | 053-5555555 |

**`Clubs`**

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

**`Members`**

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

**`ClubMembers`**

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

---

## 3️⃣ התחביר בקצרה

</div>

```sql
-- the checklist for every exam question
-- 1. Which tables hold the columns I need?          -> FROM
-- 2. How are they connected? (FK = PK)              -> WHERE ... = ...
-- 3. Which ROWS?                                    -> WHERE
-- 4. "for each ..."?                                -> GROUP BY
-- 5. condition on COUNT/SUM/AVG?                    -> HAVING
-- 6. "who has NO ..."?                              -> NOT IN (SELECT ...)
-- 7. compare to average / max?                      -> (SELECT AVG(...) FROM ...)
-- 8. order?                                         -> ORDER BY
```

<div dir="rtl">

- **קודם קוראים את הטבלאות** ומסמנים: 🔑 מפתח ראשי, 🔗 מפתח זר, ואיזו טבלה מקשרת (M:N).
- בבחינה כותבים צירוף עם **פסיק + `WHERE`**, וערכי טקסט לפעמים במירכאות כפולות: `"כדורגל"`.
- סוגי שאלות: איזו טבלה תתקבל · השלמת ערכים · כתיבת שאילתה · מהי השאילתה שהציגה פלט נתון · `UPDATE`/`DELETE`/`ALTER`.
- 📋 הדפיסו את [דף העזר](../../exam-prep/cheat-sheet.md) — מותר להביא אותו לבחינה.

</div>

<div dir="rtl">

---

## 4️⃣ דוגמאות פתורות

> קראו את השאלה, נסו לכתוב בעצמכם, ורק אז הסתכלו על הפתרון והתוצאה.

</div>

<div dir="rtl">

### דוגמה 1: שם החוג ושם המאמן של כל חוג.

</div>

```sql
SELECT ClubName, CoachFirstName, CoachLastName
FROM   Clubs, Coaches
WHERE  TrainerCode = CoachCode;
```

<div dir="rtl">

| ClubName | CoachFirstName | CoachLastName |
|---|---|---|
| כדורגל צעירים | סאמר | חלבי |
| כדורגל בוגרים | סאמר | חלבי |
| שחייה מתחילים | מיכל | לוי |
| שחייה מתקדמים | מיכל | לוי |
| כדורסל | ראמי | עזאם |
| טניס | דנה | כהן |
| ג'ודו | ראמי | עזאם |
| יוגה | דנה | כהן |

**התוצאה: 8 שורות**

</div>

<div dir="rtl">

### דוגמה 2: לכל חוג (שם): מספר החברים, כולל חוגים בלי חברים.

</div>

```sql
SELECT    ClubName, COUNT(MemberNum) AS Members
FROM      Clubs
LEFT JOIN ClubMembers ON ClubCode = ClubNum
GROUP BY  ClubCode, ClubName;
```

<div dir="rtl">

| ClubName | Members |
|---|---|
| כדורגל צעירים | 4 |
| כדורגל בוגרים | 2 |
| שחייה מתחילים | 3 |
| שחייה מתקדמים | 1 |
| כדורסל | 3 |
| טניס | 2 |
| ג'ודו | 3 |
| יוגה | 0 |

**התוצאה: 8 שורות**

</div>

<div dir="rtl">

### דוגמה 3: מאמנים שאינם מאמנים אף חוג.

</div>

```sql
SELECT CoachFirstName, CoachLastName
FROM   Coaches
WHERE  CoachCode NOT IN (SELECT TrainerCode FROM Clubs);
```

<div dir="rtl">

| CoachFirstName | CoachLastName |
|---|---|
| יוסי | אברהם |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

---

## 5️⃣ שאלות: מה תחזיר השאילתה?

> בלי להריץ! כתבו על דף את הטבלה שתתקבל (או רק את מספר השורות). אחר כך הריצו ובדקו. התשובות ב[פתרונות](solutions.md).

</div>

<div dir="rtl">

**שאלה 1.** השלימו: כמה שורות, ואילו ערכים?

</div>

```sql
SELECT DISTINCT Sport
FROM   Clubs
WHERE  Price BETWEEN 150 AND 250;
```

<div dir="rtl">

**שאלה 2.** איזו טבלה תתקבל?

</div>

```sql
SELECT   TownCode, COUNT(*) AS N
FROM     Members
GROUP BY TownCode
HAVING   COUNT(*) >= 3;
```

<div dir="rtl">

**שאלה 3.** אילו שמות יחזרו?

</div>

```sql
SELECT FirstName
FROM   Members
WHERE  MemberId IN (SELECT MemberNum FROM ClubMembers WHERE ClubNum = 106)
  AND  Age < 16;
```

<div dir="rtl">

**שאלה 4.** השלימו את שני הערכים.

</div>

```sql
SELECT MAX(Price) - MIN(Price) AS Gap, COUNT(DISTINCT Sport) AS Sports
FROM   Clubs;
```

<div dir="rtl">

**שאלה 5.** מה המספר?

</div>

```sql
SELECT COUNT(*)
FROM   ClubMembers
WHERE  ClubNum IN (SELECT ClubCode FROM Clubs WHERE Sport = 'כדורגל');
```

<div dir="rtl">

**שאלה 6.** איזו טבלה תתקבל?

</div>

```sql
SELECT   Sport, MIN(Price)
FROM     Clubs
GROUP BY Sport
HAVING   COUNT(*) = 2;
```

<div dir="rtl">

---

## 6️⃣ תרגילים — ⚽ חוגי ספורט עירוניים

> כתבו שאילתה לכל סעיף והריצו. **🔢 מספר השורות הצפוי** עוזר לבדוק את עצמכם. 🟢 קל · 🟡 בינוני · 🔴 מאתגר

1. 🟢 הציגו את שמות החברים בני 15 ומטה, ממוינים לפי גיל. _(🔢 7 שורות)_

2. 🟢 הציגו את החוגים שהמחיר שלהם בין 140 ל‑200, ושמם מכיל 'כדור'. _(🔢 3 שורות)_

3. 🟢 הציגו את המאמנים שאין להם טלפון. _(🔢 שורה אחת)_

4. 🟡 הציגו את שם החבר ושם העיר שלו — רק חברים מירכא או מכרמיאל. _(🔢 6 שורות)_

5. 🟡 לכל ענף (`Sport`): מספר החוגים והמחיר הממוצע. _(🔢 6 שורות)_

6. 🟡 הציגו את שמות החברים בחוג 'כדורגל צעירים'. _(🔢 4 שורות)_

7. 🟡 חוגים שהמחיר שלהם גבוה מהמחיר הממוצע. _(🔢 3 שורות)_

8. 🔴 חברים שרשומים ל‑2 חוגים או יותר (שמות), ומה הם משלמים בסך הכול בחודש. _(🔢 6 שורות)_

9. 🔴 לכל מאמן (שם): כמה חברים הוא מאמן בסך הכול בכל החוגים שלו? _(🔢 4 שורות)_

10. 🔴 ערים שאף חבר לא גר בהן. _(🔢 שורה אחת)_

11. 🔴 נתונה השאילתה השמורה Q1 — סך התשלום החודשי לכל חבר. הציגו את שם החבר שמשלם הכי הרבה. _(🔢 שורה אחת)_

12. 🟡 העלו ב‑10% את המחיר של כל חוגי השחייה. _(🔍 משנה נתונים — בדקו עם SELECT)_

13. 🟡 מחקו את החוג שאין בו אף חבר. _(🔍 משנה נתונים — בדקו עם SELECT)_

14. 🟡 הוסיפו לטבלת החברים עמודה `Phone` מסוג טקסט. _(🔍 משנה נתונים — בדקו עם SELECT)_

15. 🟢 החברים שהצטרפו בשנת 2025, לפי שם משפחה. _(🔢 4 שורות)_

16. 🟡 לכל עיר (שם): כמה חברים גרים בה, כולל ערים בלי חברים. _(🔢 6 שורות)_

17. 🟡 חברים (שמות) שאינם רשומים לאף חוג כדורגל. _(🔢 6 שורות)_

18. 🔴 החוג (או החוגים) עם הכי הרבה חברים. _(🔢 שורה אחת)_

19. 🔴 הגיל הממוצע של החברים בכל ענף (`Sport`), מעוגל לספרה אחת. _(🔢 5 שורות)_

20. 🟡 מחקו את החבר 1012 מכל החוגים. _(🔍 משנה נתונים — בדקו עם SELECT)_

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

**שאלה 1.** 🟢 ✍️ התיקונים שעדיין פתוחים (`DoneDate` ריק), לפי תאריך קבלה. _(🔢 3 שורות)_

</div>

<div dir="rtl">

**שאלה 2.** 🟢 ✍️ הטכנאים מירכא (לפי שם העיר). _(🔢 3 שורות)_

</div>

<div dir="rtl">

**שאלה 3.** 🟡 ✍️ לכל משפחת מכשירים: מספר התיקונים וסך המחירים. _(🔢 3 שורות)_

</div>

<div dir="rtl">

**שאלה 4.** 🟡 🔎 **איזו שאילתה הציגה את הטבלה?**

</div>

<div dir="rtl">

| TechFirst |
|---|
| חוסאם |
| נביל |
| סאמר |

</div>

<div dir="rtl">

**שאלה 5.** 🟡 🧮 **השלימו את הערכים:** השלימו את הערכים.

</div>

```sql
SELECT COUNT(*), SUM(UseQty)
FROM   PartUsage
WHERE  UsePart = 101;
```

<div dir="rtl">

**שאלה 6.** 🔴 ✍️ שם הלקוח, שם החלף ומחיר החלף — לכל חלף שהוחלף בתיקון של מחשב נייד (4 טבלאות). _(🔢 8 שורות)_

</div>

<div dir="rtl">

**שאלה 7.** 🔴 ✍️ טכנאים (שמות) שהמחיר הממוצע של התיקונים שלהם גבוה מהממוצע הכללי. _(🔢 2 שורות)_

</div>

<div dir="rtl">

**שאלה 8.** 🟡 ✍️ סגרו את התיקון 1004: עדכנו את `DoneDate` ל‑'2026-02-20'. _(🔍 משנה נתונים)_

</div>

<div dir="rtl">

**שאלה 9.** 🔴 🧩 **השלימו את הפקודה:** השלימו את הפקודה שמוחקת את החלפים שלא השתמשו בהם אף פעם.

</div>

```sql
______ ____ Parts
WHERE  PartCode ___ __ (SELECT _______ FROM PartUsage);
```

<div dir="rtl">

---

## 8️⃣ תרגול נוסף — 📚 ספרייה עירונית

> בסיס נתונים אחר, שאתם לא מכירים — בדיוק כמו בבחינה. [📋 הטבלאות והקוד של ספרייה עירונית](../../databases/library/)

1. 🟢 ספרים שיצאו לאור אחרי 2000, ממוינים לפי שנה. _(🔢 3 שורות)_

2. 🟡 שם הספר ושם הסופר של כל ספר. _(🔢 10 שורות)_

3. 🟡 השאלות שעדיין לא הוחזרו: שם הקורא ושם הספר. _(🔢 8 שורות)_

4. 🟡 לכל קורא (שם): כמה ספרים השאיל? _(🔢 9 שורות)_

5. 🔴 ספרים שאף פעם לא הושאלו. _(🔢 שורה אחת)_

6. 🔴 הספר (או הספרים) עם מספר העמודים הגדול ביותר, ושם הסופר. _(🔢 שורה אחת)_

7. 🟡 הסופרים שאין להם אף ספר בספרייה. _(🔢 שורה אחת)_

8. 🔴 לכל ז'אנר: מספר ההשאלות (רק ז'אנרים שהושאלו). _(🔢 4 שורות)_

9. 🔴 הוסיפו לטבלת ההשאלות עמודה `Fine` (קנס) עם ברירת מחדל 0, ותנו קנס של 20 לכל השאלה שלא הוחזרה. _(🔍 משנה נתונים — בדקו עם SELECT)_

</div>

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

---

✅ **[לפתרונות המלאים — שאילתה + התוצאה האמיתית](solutions.md)**

[➡️ השיעור הקודם](../13-create-alter-drop/README.md) · [🏠 כל השיעורים](../README.md)

</div>
