<div dir="rtl">

# שיעור 5 — חישובים ופונקציות שורה

[➡️ השיעור הקודם](../04-order-by/README.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../06-aggregates/README.md)

> 🎯 **בשיעור הזה:** חישובים, חיבור טקסט `||`, `LENGTH`, `SUBSTR`, `ROUND`, `CASE` ו‑`IFNULL`
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
SELECT HourRate * 1.17                    -- + - * /
SELECT FirstName || ' ' || LastName       -- join texts
SELECT LENGTH(FirstName)                  -- number of characters
SELECT SUBSTR(TeacherPhone, 1, 3)         -- part of a text: from char 1, 3 chars
SELECT ROUND(HourRate / 7.0, 1)           -- round to 1 digit after the point
SELECT IFNULL(TeacherPhone, 'אין')        -- replace NULL with a value

SELECT CASE
         WHEN HourRate >= 140 THEN 'יקר'
         WHEN HourRate >= 120 THEN 'בינוני'
         ELSE 'זול'
       END AS PriceGroup
FROM Teachers;
```

<div dir="rtl">

- פונקציית **שורה** מחושבת **לכל שורה בנפרד** — מספר השורות לא משתנה.
- ⚠️ חילוק של שני מספרים שלמים ב‑SQLite הוא חילוק שלם: `7 / 2 = 3`. כדי לקבל `3.5` כותבים `7 / 2.0`.
- `CASE` נבדק מלמעלה למטה — ה‑`WHEN` הראשון שמתקיים מנצח.
- `COALESCE(a, b)` עושה בדיוק את מה ש‑`IFNULL(a, b)` עושה.

</div>

<div dir="rtl">

---

## 4️⃣ דוגמאות פתורות

> קראו את השאלה, נסו לכתוב בעצמכם, ורק אז הסתכלו על הפתרון והתוצאה.

</div>

<div dir="rtl">

### דוגמה 1: השם המלא של כל תלמיד ואורך השם הפרטי.

</div>

```sql
SELECT FirstName || ' ' || LastName AS FullName,
       LENGTH(FirstName) AS NameLen
FROM   Pupils;
```

<div dir="rtl">

| FullName | NameLen |
|---|---|
| אדם חלבי | 3 |
| מאיה כהן | 4 |
| כרים עזאם | 4 |
| שירה לוי | 4 |
| רמי חורי | 3 |
| תמר אברהם | 3 |
| ליאן קבלאן | 4 |
| עומר ביטון | 4 |
| סאלי חסון | 4 |
| יואב שושן | 4 |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### דוגמה 2: קידומת הטלפון של כל מורה, ו'אין טלפון' אם חסר.

</div>

```sql
SELECT TeacherName,
       IFNULL(SUBSTR(TeacherPhone, 1, 3), 'אין טלפון') AS Prefix
FROM   Teachers;
```

<div dir="rtl">

| TeacherName | Prefix |
|---|---|
| סמיר חלבי | 050 |
| רונית לוי | 052 |
| אמיר עזאם | אין טלפון |
| דנה כהן | 054 |
| יוסי פרץ | 053 |
| נור מנסור | אין טלפון |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### דוגמה 3: המחיר לשעה כולל מע"מ 18%, מעוגל לשקל.

</div>

```sql
SELECT TeacherName, ROUND(HourRate * 1.18) AS WithVat
FROM   Teachers;
```

<div dir="rtl">

| TeacherName | WithVat |
|---|---|
| סמיר חלבי | 142.0 |
| רונית לוי | 177.0 |
| אמיר עזאם | 130.0 |
| דנה כהן | 165.0 |
| יוסי פרץ | 118.0 |
| נור מנסור | 153.0 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### דוגמה 4: סיווג המורים: יקר (140+), בינוני (120–139), זול.

</div>

```sql
SELECT TeacherName, HourRate,
       CASE
         WHEN HourRate >= 140 THEN 'יקר'
         WHEN HourRate >= 120 THEN 'בינוני'
         ELSE 'זול'
       END AS PriceGroup
FROM   Teachers;
```

<div dir="rtl">

| TeacherName | HourRate | PriceGroup |
|---|---|---|
| סמיר חלבי | 120 | בינוני |
| רונית לוי | 150 | יקר |
| אמיר עזאם | 110 | זול |
| דנה כהן | 140 | יקר |
| יוסי פרץ | 100 | זול |
| נור מנסור | 130 | בינוני |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

---

## 5️⃣ שאלות: מה תחזיר השאילתה?

> בלי להריץ! כתבו על דף את הטבלה שתתקבל (או רק את מספר השורות). אחר כך הריצו ובדקו. התשובות ב[פתרונות](solutions.md).

</div>

<div dir="rtl">

**שאלה 1.** מה יהיו שלושת הערכים?

</div>

```sql
SELECT 7 / 2, 7 / 2.0, ROUND(7 / 3.0, 2);
```

<div dir="rtl">

**שאלה 2.** מה יחזור?

</div>

```sql
SELECT SUBSTR('סמיר חלבי', 1, 4) AS Part;
```

<div dir="rtl">

**שאלה 3.** אילו מורים יחזרו?

</div>

```sql
SELECT TeacherName, LENGTH(TeacherName) AS L
FROM   Teachers
WHERE  LENGTH(TeacherName) = 9;
```

<div dir="rtl">

**שאלה 4.** מה שני הערכים?

</div>

```sql
SELECT LENGTH('פסנתר'), SUBSTR('050-1234567', 5, 3);
```

<div dir="rtl">

**שאלה 5.** כמה פעמים יופיע 'כן'?

</div>

```sql
SELECT InstName,
       CASE WHEN InstFamily = 'מיתר' THEN 'כן' ELSE 'לא' END AS Strings
FROM   Instruments;
```

<div dir="rtl">

---

## 6️⃣ תרגילים — 🎵 בית הספר למוזיקה "צלילים"

> כתבו שאילתה לכל סעיף והריצו. **🔢 מספר השורות הצפוי** עוזר לבדוק את עצמכם. 🟢 קל · 🟡 בינוני · 🔴 מאתגר

1. 🟢 הציגו לכל רישום את קוד התלמיד ואת התשלום לחצי שנה (6 חודשים), בשם `HalfYear`. _(🔢 14 שורות)_

2. 🟢 הציגו את השם המלא של התלמידים בפורמט: שם משפחה, פסיק, שם פרטי (למשל `חלבי, אדם`). _(🔢 10 שורות)_

3. 🟢 הציגו את שם המורה ואת אורך השם שלו. _(🔢 6 שורות)_

4. 🟡 הציגו את האות הראשונה של השם הפרטי של כל תלמיד, בשם `Initial`. _(🔢 10 שורות)_

5. 🟡 הציגו את המחיר לדקה של כל מורה (מחיר לשעה חלקי 60), מעוגל ל‑2 ספרות. _(🔢 6 שורות)_

6. 🟡 הציגו את שם המורה ואת הטלפון, ובמקום NULL את הטקסט 'לא ידוע'. _(🔢 6 שורות)_

7. 🟡 הציגו תלמידים ששם המשפחה שלהם ארוך מ‑3 אותיות. _(🔢 8 שורות)_

8. 🔴 הציגו לכל תלמיד את שמו ואת 'צעיר' אם נולד ב‑2012 ואילך, אחרת 'בוגר'. בשם `AgeGroup`. _(🔢 10 שורות)_

9. 🔴 הציגו לכל רישום את התשלום ואת התשלום אחרי הנחה: 10% למתחילים, 5% לממשיכים, ובלי הנחה למתקדמים. _(🔢 14 שורות)_

10. 🔴 הציגו את מספר הטלפון של המורים בלי המקף (רמז: `REPLACE(text, '-', '')`). _(🔢 4 שורות)_

11. 🟢 הציגו לכל מורה את שמו ואת המחיר ל‑90 דקות (שעה וחצי), בשם `Lesson90`. _(🔢 6 שורות)_

12. 🟢 הציגו את שם הכלי ואת משפחתו בעמודה אחת, למשל `פסנתר (קלידים)`. _(🔢 6 שורות)_

13. 🟡 הציגו את 3 הספרות האחרונות של הטלפון של כל מורה (רמז: `SUBSTR(TeacherPhone, -3)`). _(🔢 4 שורות)_

14. 🟡 הציגו לכל רישום את התשלום החודשי כולל מע"מ 18%, מעוגל לשקל, בשם `WithVat`. _(🔢 14 שורות)_

15. 🟡 הציגו לכל תלמיד את שמו ואת מספר האותיות בשם המלא (בלי רווח), בשם `Letters`. _(🔢 10 שורות)_

16. 🔴 הציגו לכל לוקר: 'קרקע' לקומה 1, 'עליונה' לקומה 2. _(🔢 5 שורות)_

17. 🔴 הציגו לכל רישום את קוד התלמיד ו'ותיק' אם נרשם לפני 2024, 'חדש' אם ב‑2024, ו'חדש מאוד' אם ב‑2025. _(🔢 14 שורות)_

</div>

<div dir="rtl">

---

## 7️⃣ 🎓 בסגנון הבחינה — ☕ בית הקפה "אל‑בלד"

> שאלות בפורמט של שאלון 735911: שמות שדות ייחודיים, צירוף עם פסיק + `WHERE`, השלמת ערכים, זיהוי שאילתה לפי פלט והשלמת פקודות. [📋 הטבלאות והקוד](../../databases/cafe/)

</div>

<details>
<summary>📋 <b>הטבלאות של בית הקפה "אל‑בלד"</b> (לחצו לפתיחה)</summary>

<div dir="rtl">

**`Cities`**

| CityCode 🔑 | CityName |
|---|---|
| 1 | ירכא |
| 2 | עכו |
| 3 | כרמיאל |
| 4 | נהריה |
| 5 | שפרעם |

**`Workers`**

| WorkerNum 🔑 | WorkerName | WorkerCity 🔗 | StartDate | HourPay | WorkerPhone |
|---|---|---|---|---|---|
| 1 | סאלי חדאד | 2 | 2022-03-01 | 42 | 050-1111111 |
| 2 | יובל נחום | 1 | 2023-07-15 | 38 | *NULL* |
| 3 | אמיר טאהא | 2 | 2021-11-10 | 50 | 054-3333333 |
| 4 | מיכל שרון | 4 | 2024-01-20 | 36 | 052-4444444 |
| 5 | רים עבאס | 1 | 2020-05-05 | 55 | *NULL* |
| 6 | תום בראל | 5 | 2023-09-01 | 38 | 053-6666666 |

**`Dishes`**

| DishCode 🔑 | DishName | DishKind | DishPrice |
|---|---|---|---|
| 10 | חומוס | מנה ראשונה | 28 |
| 20 | סלט ירקות | מנה ראשונה | 32 |
| 30 | שניצל | מנה עיקרית | 56 |
| 40 | פסטה | מנה עיקרית | 48 |
| 50 | קנאפה | קינוח | 30 |
| 60 | עוגת גבינה | קינוח | 26 |
| 70 | לימונדה | שתייה | 14 |
| 80 | קפה | שתייה | 12 |

**`Orders`**

| OrderNum 🔑 | CustName | OrderDish 🔗 | OrderWorker 🔗 | OrderDate | Guests |
|---|---|---|---|---|---|
| 101 | דנה לוי | 30 | 1 | 2026-02-04 | 2 |
| 102 | עומר חורי | 10 | 3 | 2026-02-18 | 4 |
| 103 | נועה כץ | 40 | 2 | 2026-03-05 | 3 |
| 104 | סמיר דיב | 30 | 1 | 2026-03-22 | 6 |
| 105 | ליאת בר | 50 | 4 | 2026-04-09 | 2 |
| 106 | ראמי סעיד | 20 | 3 | 2026-04-27 | 5 |
| 107 | יעל שגיא | 30 | 5 | 2026-05-11 | 2 |
| 108 | חנאן זועבי | 70 | 6 | 2026-05-30 | 8 |
| 109 | איתי פלד | 40 | 2 | 2026-06-14 | 3 |
| 110 | מאיה לוי | 60 | 4 | 2026-06-28 | 4 |
| 111 | ואיל נסאר | 30 | 5 | 2026-07-07 | 2 |
| 112 | שני אדרי | 80 | 6 | 2026-07-21 | 10 |

</div>

</details>


<details>
<summary>📥 <b>הקוד שבונה את בסיס הנתונים ☕ בית הקפה "אל‑בלד"</b> — מעתיקים הכול ומדביקים ב‑OneCompiler</summary>

```sql
-- ============================================================
--  בית הקפה "אל-בלד"  ·  בסיס נתונים לבחינת מתכונת (תרגול)
--  הדביקו את כל הקובץ ב-OneCompiler (SQLite), לחצו Run, וכתבו את השאילתות מתחת.
--  לכל שדה בבסיס הנתונים שם ייחודי, ולכן אין צורך בשם הטבלה לפניו.
-- ============================================================
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Dishes;
DROP TABLE IF EXISTS Workers;
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

-- ---------- טבלה ראשית: עובדים ----------
CREATE TABLE Workers (
  WorkerNum    INTEGER PRIMARY KEY,
  WorkerName   TEXT NOT NULL,
  WorkerCity   INTEGER REFERENCES Cities(CityCode),
  StartDate    TEXT NOT NULL,
  HourPay      INTEGER NOT NULL,     -- שכר לשעה בש"ח
  WorkerPhone  TEXT                  -- NULL = לא רשום טלפון
);
INSERT INTO Workers VALUES (1, 'סאלי חדאד',  2, '2022-03-01', 42, '050-1111111');
INSERT INTO Workers VALUES (2, 'יובל נחום',  1, '2023-07-15', 38, NULL);
INSERT INTO Workers VALUES (3, 'אמיר טאהא',  2, '2021-11-10', 50, '054-3333333');
INSERT INTO Workers VALUES (4, 'מיכל שרון',  4, '2024-01-20', 36, '052-4444444');
INSERT INTO Workers VALUES (5, 'רים עבאס',   1, '2020-05-05', 55, NULL);
INSERT INTO Workers VALUES (6, 'תום בראל',   5, '2023-09-01', 38, '053-6666666');

-- ---------- טבלה ראשית: מנות ----------
CREATE TABLE Dishes (
  DishCode   INTEGER PRIMARY KEY,
  DishName   TEXT NOT NULL,
  DishKind   TEXT NOT NULL,
  DishPrice  INTEGER NOT NULL        -- מחיר המנה בש"ח
);
INSERT INTO Dishes VALUES (10, 'חומוס',      'מנה ראשונה', 28);
INSERT INTO Dishes VALUES (20, 'סלט ירקות',  'מנה ראשונה', 32);
INSERT INTO Dishes VALUES (30, 'שניצל',      'מנה עיקרית', 56);
INSERT INTO Dishes VALUES (40, 'פסטה',       'מנה עיקרית', 48);
INSERT INTO Dishes VALUES (50, 'קנאפה',      'קינוח',      30);
INSERT INTO Dishes VALUES (60, 'עוגת גבינה', 'קינוח',      26);
INSERT INTO Dishes VALUES (70, 'לימונדה',    'שתייה',      14);
INSERT INTO Dishes VALUES (80, 'קפה',        'שתייה',      12);

-- ---------- טבלה ראשית: הזמנות ----------
CREATE TABLE Orders (
  OrderNum     INTEGER PRIMARY KEY,
  CustName     TEXT NOT NULL,
  OrderDish    INTEGER REFERENCES Dishes(DishCode),
  OrderWorker  INTEGER REFERENCES Workers(WorkerNum),
  OrderDate    TEXT NOT NULL,
  Guests       INTEGER NOT NULL      -- כמה סועדים ישבו בשולחן
);
INSERT INTO Orders VALUES (101, 'דנה לוי',    30, 1, '2026-02-04',  2);
INSERT INTO Orders VALUES (102, 'עומר חורי',  10, 3, '2026-02-18',  4);
INSERT INTO Orders VALUES (103, 'נועה כץ',    40, 2, '2026-03-05',  3);
INSERT INTO Orders VALUES (104, 'סמיר דיב',   30, 1, '2026-03-22',  6);
INSERT INTO Orders VALUES (105, 'ליאת בר',    50, 4, '2026-04-09',  2);
INSERT INTO Orders VALUES (106, 'ראמי סעיד',  20, 3, '2026-04-27',  5);
INSERT INTO Orders VALUES (107, 'יעל שגיא',   30, 5, '2026-05-11',  2);
INSERT INTO Orders VALUES (108, 'חנאן זועבי', 70, 6, '2026-05-30',  8);
INSERT INTO Orders VALUES (109, 'איתי פלד',   40, 2, '2026-06-14',  3);
INSERT INTO Orders VALUES (110, 'מאיה לוי',   60, 4, '2026-06-28',  4);
INSERT INTO Orders VALUES (111, 'ואיל נסאר',  30, 5, '2026-07-07',  2);
INSERT INTO Orders VALUES (112, 'שני אדרי',   80, 6, '2026-07-21', 10);

SELECT COUNT(*) AS orders_loaded FROM Orders;
```

</details>


<div dir="rtl">

**שאלה 1.** 🟢 ✍️ הציגו לכל מנה את שמה ואת המחיר אחרי הנחה של 10%, בשם `Sale`. _(🔢 8 שורות)_

</div>

<div dir="rtl">

**שאלה 2.** 🟢 ✍️ הציגו לכל הזמנה את שם הלקוח ואת אורך השם. _(🔢 12 שורות)_

</div>

<div dir="rtl">

**שאלה 3.** 🟡 ✍️ הציגו לכל עובד את שמו ואת הטלפון, ובמקום NULL — 'אין'. _(🔢 6 שורות)_

</div>

<div dir="rtl">

**שאלה 4.** 🟡 ✍️ הציגו לכל עובד את שמו ואת שנת תחילת העבודה בלבד. _(🔢 6 שורות)_

</div>

<div dir="rtl">

**שאלה 5.** 🟡 🧮 **השלימו את הערכים:** השלימו את הערכים בטבלה שתתקבל.

</div>

```sql
SELECT DishName,
       CASE WHEN DishPrice >= 30 THEN 'יקר' ELSE 'זול' END AS Level
FROM   Dishes
WHERE  DishKind = 'מנה ראשונה';
```

<div dir="rtl">

**שאלה 6.** 🔴 🔎 **איזו שאילתה הציגה את הטבלה?**

</div>

<div dir="rtl">

| DishName | TwoDishes |
|---|---|
| לימונדה | 28 |
| קפה | 24 |

</div>

<div dir="rtl">

**שאלה 7.** 🔴 🧩 **השלימו את הפקודה:** השלימו כך שיוצג לכל עובד שכר יומי (8 שעות) מעוגל, בשם `DayPay`.

</div>

```sql
SELECT WorkerName, _____(HourPay * _) AS ______
FROM   _______;
```

<div dir="rtl">

---

## 8️⃣ תרגול נוסף — 🏫 בית הספר "עתיד"

> בסיס נתונים אחר, שאתם לא מכירים — בדיוק כמו בבחינה. [📋 הטבלאות והקוד של בית הספר "עתיד"](../../databases/school/)

1. 🟢 הציגו את השם המלא של כל מורה בעמודה אחת. _(🔢 7 שורות)_

2. 🟡 הציגו את שנת הקליטה בלבד של כל מורה (4 התווים הראשונים של `HireDate`). _(🔢 7 שורות)_

3. 🟡 הציגו את הטלפון של התלמידים, ובמקום NULL — 'אין'. _(🔢 18 שורות)_

4. 🔴 הציגו כל ציון ולצידו 'עבר' (55 ומעלה), 'נכשל', או 'לא נבחן' (NULL). _(🔢 52 שורות)_

5. 🟢 הציגו לכל מורה את השכר אחרי העלאה של 3%, מעוגל לשקל. _(🔢 7 שורות)_

6. 🟡 הציגו לכל תלמיד את חודש הלידה בלבד (תווים 6–7 של `BirthDate`). _(🔢 17 שורות)_

7. 🟡 הציגו לכל כיתה את שמה ואת מספר החדר, ו'אין חדר' כשהוא חסר. _(🔢 5 שורות)_

8. 🔴 הציגו לכל היעדרות 'מאושרת' או 'לא מאושרת' לפי `Excused`. _(🔢 16 שורות)_

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

[➡️ השיעור הקודם](../04-order-by/README.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../06-aggregates/README.md)

</div>
