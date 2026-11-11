<div dir="rtl">

# 📖 מדריך הקורס המעשי: SQL מהקל למתקדם (ללא תיאוריה)

> **מיועד לתלמידי שאלון 735911 (מה"ט / משרד החינוך)**
> 
> המדריך הזה נכתב במטרה אחת: **ללמד אתכם לכתוב ולפתור שאילתות SQL לבחינה במהירות וביעילות**.  
> בלי סיפורי רקע, בלי היסטוריה של בסיסי נתונים ובלי פילוסופיה של מודלים עיוניים.  
> **רק תחביר נקי, דוגמאות קוד אמיתיות להרצה, מלכודות נפוצות בבחינה, ותרגול ממוקד.**
> 
> **בסיס הנתונים לדוגמאות:** בית הספר למוזיקה "צלילים" ([`db/music.sql`](db/music.sql)).

---

## 🗺️ תוכן העניינים

1. [מבנה בסיס הנתונים והכללים לבחינה](#1-מבנה-בסיס-הנתונים-והכללים-לבחינה)
2. [פרק 1: שליפה בסיסית וסינון ראשוני (`SELECT`, `FROM`, `AS`, `DISTINCT`)](#פרק-1-שליפה-בסיסית-וסינון-ראשוני)
3. [פרק 2: תנאים מורכבים ולוגיקה (`WHERE`, `AND`, `OR`, `BETWEEN`, `IN`, `LIKE`, `IS NULL`)](#פרק-2-תנאים-מורכבים-ולוגיקה)
4. [פרק 3: מיונים (`ORDER BY`, `ASC`, `DESC`)](#פרק-3-מיונים)
5. [פרק 4: פונקציות סקלריות / שורה (`LENGTH`, `UPPER`, `ROUND`, `SUBSTR`, `COALESCE`)](#פרק-4-פונקציות-סקלריות--שורה)
6. [פרק 5: פונקציות קיבוץ ומצרפיות (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`)](#פרק-5-פונקציות-קיבוץ-ומצרפיות)
7. [פרק 6: קיבוץ נתונים ותנאי קבוצה (`GROUP BY`, `HAVING` לעומת `WHERE`)](#פרק-6-קיבוץ-נתונים-ותנאי-קבוצה)
8. [פרק 7: חיבור טבלאות (צירופים — Joins)](#פרק-7-חיבור-טבלאות-צירופים--joins)
9. [פרק 8: שאילתות מקוננות (תת‑שאילתות — Subqueries)](#פרק-8-שאילתות-מקוננות-תתשאילתות--subqueries)
10. [פרק 9: שאילתות שמורות (`CREATE VIEW`, שימוש כטבלה `Q1`)](#פרק-9-שאילתות-שמורות)
11. [פרק 10: פקודות שינוי נתונים (`INSERT`, `UPDATE`, `DELETE`)](#פרק-10-פקודות-שינוי-נתונים)
12. [פרק 11: פקודות שינוי מבנה (`CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`)](#פרק-11-פקודות-שינוי-מבנה)
13. [פרק 12: מפתחות וקשרים בבחינה (PK, FK, 1:1, 1:N, M:N, DSD)](#פרק-12-מפתחות-וקשרים-בבחינה)

---

## 1. מבנה בסיס הנתונים והכללים לבחינה

בבחינה (שאלון 735911) יש שני כללים שמקלים על כתיבת השאילתות:
1. **לכל שדה בבסיס הנתונים יש שם ייחודי:** אין צורך לכתוב את שם הטבלה לפני השדה! כותבים `WHERE HomeTown = CityCode` (ולא `Pupils.HomeTown = Cities.CityCode`).
2. **טקסט נכתב במירכאות כפולות או יחידות:** `"מתקדם"` או `'מתקדם'`.

### סכמת הטבלאות ב‑`music.sql`:
- **Pupils** (`PupilId` PK, `FirstName`, `LastName`, `BirthYear`, `HomeTown` FK)
- **Teachers** (`TeacherCode` PK, `TeacherName`, `TeachInst` FK, `HourRate`, `TeacherPhone`)
- **Registrations** (`RegPupil` FK, `RegTeacher` FK, `RegYear`, `PupilLevel`, `MonthlyFee`) — מפתח ראשי מורכב: `(RegPupil, RegTeacher)`
- **Cities** (`CityCode` PK, `CityName`)
- **Instruments** (`InstCode` PK, `InstName`, `InstFamily`)
- **Lockers** (`LockerNum` PK, `LockerPupil` FK UNIQUE, `LockerFloor`)

---

## פרק 1: שליפה בסיסית וסינון ראשוני

### מה עושים?
בוחרים אילו עמודות להציג ומאיזו טבלה לשלוף.

```sql
SELECT FirstName, LastName
FROM Pupils;
```

### הרחבות ושימושים נפוצים:
- **שליפת כל העמודות (`*`):** `SELECT * FROM Instruments;`
- **הסרת כפילויות (`DISTINCT`):** מחזיר כל ערך פעם אחת בלבד.
  ```sql
  SELECT DISTINCT HomeTown FROM Pupils;
  ```
- **כינוי לעמודה (`AS`):** משנה את כותרת העמודה בתוצאה (או תוצאת חישוב).
  ```sql
  SELECT TeacherName, HourRate * 0.9 AS DiscountRate FROM Teachers;
  ```

> ⚠️ **מלכודת בחינה:** `DISTINCT` מופיע מיד אחרי `SELECT`, ולא אחרי שמות העמודות!

---

## פרק 2: תנאים מורכבים ולוגיקה

### מה עושים?
מסננים שורות באמצעות פסוקית `WHERE`.

```sql
SELECT TeacherName, HourRate
FROM Teachers
WHERE HourRate >= 120;
```

### ארגז הכלים של WHERE:
| אופרטור | משמעות | דוגמה | דגש לבחינה |
|---|---|---|---|
| `=`, `<>` | שווה, שונה | `WHERE PupilLevel <> "מתחיל"` | שונה יכול להיכתב גם `!=` |
| `>`, `<`, `>=`, `<=` | השוואות מספרים | `WHERE BirthYear > 2011` | `>` לא כולל את 2011! |
| `BETWEEN x AND y` | בטווח שבין x ל‑y | `WHERE BirthYear BETWEEN 2010 AND 2012` | **כולל תמיד את x ואת y!** |
| `IN (a, b, c)` | שווה לאחד הערכים | `WHERE TeachInst IN (10, 20, 30)` | קיצור במקום כמה תנאי `OR` |
| `LIKE` | תבנית טקסט | `WHERE LastName LIKE "ח%"` | `%` = כל רצף, `_` = תו יחיד |
| `IS NULL` | ערך חסר/ריק | `WHERE TeacherPhone IS NULL` | **לעולם לא `= NULL`!** |
| `IS NOT NULL` | ערך קיים | `WHERE TeacherPhone IS NOT NULL` | |
| `AND`, `OR`, `NOT` | קשרים לוגיים | `WHERE (HomeTown = 1 OR HomeTown = 2) AND BirthYear > 2011` | **AND קודם ל‑OR!** חובה סוגריים מסביב ל‑OR |

---

## פרק 3: מיונים

### מה עושים?
קובעים את סדר השורות בתוצאה באמצעות `ORDER BY` (נכתב תמיד בסוף השאילתה).

```sql
SELECT FirstName, LastName, BirthYear
FROM Pupils
ORDER BY BirthYear DESC;  -- סדר יורד: מהצעיר ביותר למבוגר ביותר
```

- **`ASC` (ברירת מחדל):** סדר עולה (א‑ב, מהקטן לגדול).
- **`DESC`:** סדר יורד (ת‑א, מהגדול לקטן).
- **מיון לפי מספר עמודות:**
  ```sql
  SELECT * FROM Registrations
  ORDER BY MonthlyFee DESC, RegYear ASC;
  ```

---

## פרק 4: פונקציות סקלריות / שורה

פועלות על **כל שורה בנפרד** ומחזירות ערך מעובד לאותה שורה:

```sql
SELECT CityName, LENGTH(CityName) AS NameLen
FROM Cities;
```

| פונקציה | מה היא עושה? | דוגמת קוד |
|---|---|---|
| `LENGTH(str)` | סופרת תווים | `SELECT LENGTH(FirstName) FROM Pupils;` |
| `UPPER(str)` / `LOWER(str)` | אותיות גדולות/קטנות | `SELECT UPPER(CityName) FROM Cities;` |
| `SUBSTR(str, start, len)` | גזירת תת‑מחרוזת | `SELECT SUBSTR(InstFamily, 1, 1) FROM Instruments;` |
| `ROUND(num, d)` | עיגול מספר ל‑d ספרות | `SELECT ROUND(MonthlyFee * 1.17, 2) FROM Registrations;` |
| `str1 || ' ' || str2` | שרשור (חיבור) טקסט | `SELECT FirstName || ' ' || LastName AS FullName FROM Pupils;` |
| `COALESCE(col, 'ברירת מחדל')` | החלפת NULL בטקסט חלופי | `SELECT TeacherName, COALESCE(TeacherPhone, 'אין טלפון') FROM Teachers;` |

---

## פרק 5: פונקציות קיבוץ ומצרפיות

פועלות על **קבוצת שורות** ומחזירות **ערך יחיד**:

```sql
SELECT COUNT(*)    AS TotalTeachers,
       AVG(HourRate) AS AvgRate,
       MIN(HourRate) AS MinRate,
       MAX(HourRate) AS MaxRate,
       SUM(HourRate) AS TotalSalaries
FROM Teachers;
```

### שלושת סוגי `COUNT` — שאלת מפתח בבחינה:
1. **`COUNT(*)`** — סופר את **כל** השורות בטבלה (בטבלת Teachers מחזיר `6`).
2. **`COUNT(TeacherPhone)`** — סופר רק שורות שאינן NULL (מחזיר `4`, כי לשני מורים אין טלפון).
3. **`COUNT(DISTINCT TeachInst)`** — סופר כמה ערכים ייחודיים שונים קיימים (מחזיר `5`).

> ⚠️ **כלל הברזל לבחינה:** לעולם אל תכתבו פונקציה מצרפית ב‑WHERE!  
> ❌ `WHERE HourRate > AVG(HourRate)`  
> ✅ `WHERE HourRate > (SELECT AVG(HourRate) FROM Teachers)`

---

## פרק 6: קיבוץ נתונים ותנאי קבוצה

### חלוקה לקבוצות עם `GROUP BY`:
כאשר רוצים תוצאה **לכל קבוצה בנפרד** (לכל עיר, לכל מורה, לכל רמה):

```sql
SELECT PupilLevel, COUNT(*) AS RegCount, AVG(MonthlyFee) AS AvgFee
FROM Registrations
GROUP BY PupilLevel;
```

### סינון קבוצות עם `HAVING`:
- תנאי על **שורה בודדת** מסננים ב‑`WHERE` (לפני הקיבוץ).
- תנאי על **תוצאת פונקציה מצרפית** מסננים ב‑`HAVING` (אחרי הקיבוץ).

```sql
SELECT RegTeacher, SUM(MonthlyFee) AS TotalIncome
FROM Registrations
WHERE RegYear >= 2024          -- סינון שורות: רק רישומים מ-2024
GROUP BY RegTeacher            -- קיבוץ לפי מורה
HAVING COUNT(*) >= 2;          -- סינון קבוצות: רק מורים עם לפחות 2 תלמידים
```

> ⚠️ **חוק הברזל:** כל שדה שמופיע ב‑`SELECT` ואינו בתוך פונקציה מצרפית **חייב** להופיע ב‑`GROUP BY`!

---

## פרק 7: חיבור טבלאות (צירופים — Joins)

כאשר המידע הדרוש מפוזר ביותר מטבלה אחת:

### צורה 1: תחביר פסיק ב‑WHERE (הנפוץ בבחינה)
מחברים מפתח ראשי למפתח הזר המפנה אליו:
```sql
SELECT FirstName, CityName
FROM Pupils, Cities
WHERE HomeTown = CityCode;
```

### צירוף של 3 טבלאות (טבלה מקשרת):
חובה **שני** תנאי חיבור עם `AND`:
```sql
SELECT FirstName, TeacherName, MonthlyFee
FROM Pupils, Teachers, Registrations
WHERE RegPupil = PupilId AND RegTeacher = TeacherCode;
```

### צורה 2: `JOIN ... ON` ו‑`LEFT JOIN`
- **`JOIN ... ON`**: מחזיר רק שורות שיש להן התאמה בשתי הטבלאות.
- **`LEFT JOIN`**: מחזיר את **כל** השורות מהטבלה השמאלית, גם אם אין להן התאמה (תלמיד ללא לוקר יוצג עם NULL).
  ```sql
  SELECT FirstName, LockerNum
  FROM Pupils
  LEFT JOIN Lockers ON PupilId = LockerPupil;
  ```

---

## פרק 8: שאילתות מקוננות (תת‑שאילתות — Subqueries)

שאילתת `SELECT` שנמצאת בתוך סוגריים בתוך שאילתה ראשית:

### 1. מי שלא מופיע בטבלה אחרת (`NOT IN`):
```sql
-- מורים שאין להם אף תלמיד
SELECT TeacherName
FROM Teachers
WHERE TeacherCode NOT IN (SELECT RegTeacher FROM Registrations);
```

### 2. השוואה לערך מחושב יחיד (ממוצע / מקסימום):
```sql
-- מורים שמרוויחים מעל הממוצע
SELECT TeacherName, HourRate
FROM Teachers
WHERE HourRate > (SELECT AVG(HourRate) FROM Teachers);
```

### 3. מציאת השורה עם הערך המקסימלי:
```sql
-- התלמיד שמשלם את הסכום הגבוה ביותר
SELECT FirstName, LastName
FROM Pupils
WHERE PupilId IN (
    SELECT RegPupil 
    FROM Registrations 
    WHERE MonthlyFee = (SELECT MAX(MonthlyFee) FROM Registrations)
);
```

---

## פרק 9: שאילתות שמורות

בבחינה מופיעה לעיתים שאילתה שנשמרה כ‑**`View`** או בשם **`Q1`**, ומשתמשים בה **כמו בטבלה**:

```sql
-- יצירת שאילתה שמורה
CREATE VIEW Q1 AS
SELECT RegTeacher, COUNT(*) AS Cnt
FROM Registrations
GROUP BY RegTeacher;

-- שימוש בה ב-FROM לצד טבלה רגילה
SELECT TeacherName, Cnt
FROM Teachers, Q1
WHERE TeacherCode = RegTeacher;
```

---

## פרק 10: פקודות שינוי נתונים (DML)

שינוי שורות וערכים בטבלה קיימת:

### 1. `INSERT INTO` (הוספת שורה):
```sql
INSERT INTO Cities (CityCode, CityName)
VALUES (6, "חיפה");
```

### 2. `UPDATE ... SET ... WHERE` (עדכון שורה):
```sql
UPDATE Teachers
SET HourRate = HourRate * 1.10
WHERE TeachInst = 10;
```
> ⚠️ **סכנה:** אם תשכחו את `WHERE`, **כל** המורים יתעדכנו!

### 3. `DELETE FROM ... WHERE` (מחיקת שורה):
```sql
DELETE FROM Registrations
WHERE RegYear < 2023;
```
> ⚠️ **סכנה:** `DELETE FROM Registrations;` ללא WHERE מוחק את **כל** השורות בטבלה!

---

## פרק 11: פקודות שינוי מבנה (DDL)

שינוי מבנה הטבלאות והעמודות עצמן:

### 1. `CREATE TABLE`:
```sql
CREATE TABLE Rooms (
    RoomNum INTEGER PRIMARY KEY,
    FloorNum INTEGER NOT NULL,
    Capacity INTEGER
);
```

### 2. `ALTER TABLE`:
- **הוספת עמודה:** `ALTER TABLE Pupils ADD Email TEXT;`
- **מחיקת עמודה:** `ALTER TABLE Teachers DROP COLUMN TeacherPhone;`

### 3. `DROP TABLE` מול `DELETE`:
- `DELETE FROM Lockers;` — פקודת **DML**. מוחקת את כל השורות, אך הטבלה והעמודות נשארות קיימות.
- `DROP TABLE Lockers;` — פקודת **DDL**. מוחקת את **הטבלה כולה** מהמסד!

---

## פרק 12: מפתחות וקשרים בבחינה

בבחינה תמיד יש שאלה של ניתוח קשרים ותרשים DSD:

| מושג | מה זה אומר? | דוגמה ב‑`music.sql` |
|---|---|---|
| **מפתח ראשי (PK)** | מזהה ייחודי של שורה, לא חוזר ולעולם לא ריק | `PupilId`, `TeacherCode` |
| **מפתח מורכב** | מפתח ראשי המורכב משני שדות או יותר | `(RegPupil, RegTeacher)` ב‑Registrations |
| **מפתח זר (FK)** | שדה שמכיל מפתח ראשי מטבלה אחרת | `HomeTown` מפנה ל‑`CityCode` |
| **קשר 1:N (אחד לרבים)** | עיר אחת -> הרבה תלמידים. המפתח הזר בצד ה"רבים" | Cities (1) -> Pupils (N) |
| **קשר 1:1 (אחד לאחד)** | לכל תלמיד לוקר אחד לכל היותר. המפתח הזר מוגדר `UNIQUE` | Pupils (1) <-> Lockers (1) |
| **קשר M:N (רבים לרבים)** | תלמיד לומד אצל כמה מורים, מורה מלמד כמה תלמידים. **מחייב טבלת קישור!** | Registrations מקשרת בין Pupils ל‑Teachers |

---

## 🎯 לאן ממשיכים מכאן?

1. 🧮 **[מדריך ותרגול פונקציות SQL](sql-functions-guide.md)** — להעמקה בכל סוגי ה‑COUNT, הפונקציות המצרפיות והסקלריות.
2. 🏆 **[מאגר 90 שאלות מדורגות (Master Practice)](master-sql-practice.md)** ([פתרונות](master-sql-practice-solutions.md)) — פתרו את השאלות מהרמה הקלה ועד לרמת הבחינה.
3. 🎯 **[תרגול תשפ"ז לפי הנחיות משרד החינוך](practice-2027.md)** — סימולציה ישירה של שאלון 735911.
4. 📋 **[דף עזר מהיר לבחינה](cheat-sheet.md)** — הדפיסו וקחו אתכם לבחינה.

</div>
