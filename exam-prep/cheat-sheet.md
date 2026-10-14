<div dir="rtl">

# דף עזר לבחינה: SQL ובסיסי נתונים

> בבחינה (שאלון 735911) **מותר להביא כל חומר עזר כתוב**. הדפיסו את הדף הזה, הוסיפו לו הערות בכתב יד, והביאו אותו לבחינה.

## 1. מושגים: תשובה בשורה אחת

| המושג | התשובה |
|-------|--------|
| **מפתח ראשי (PK)** | מזהה כל רשומה: ייחודי, לא ריק, יציב |
| **מפתח זר (FK)** | שדה שמכיל ערך של מפתח ראשי מטבלה **אחרת** |
| **מפתח מורכב** | מפתח ראשי שבנוי משני שדות או יותר (כמו בטבלת קישור) |
| **1:1** | כל רשומה מתאימה לרשומה **אחת לכל היותר** בטבלה השנייה. המפתח הזר לא חוזר בנתונים |
| **1:N** | המפתח הזר נמצא בצד ה"רבים" |
| **N:M** | צריך **טבלת קישור** (טבלה מקשרת) עם שני מפתחות זרים |
| **טבלה ראשית / טבלת עזר** | בבחינה יש 2–3 טבלאות ראשיות, ועוד טבלאות עזר קטנות (ערים, קטגוריות) |
| **שמות שדות ייחודיים** | לכל שדה בבסיס הנתונים שם משלו, ולכן כותבים אותו **בלי** שם הטבלה. המפתח הזר נקרא בשם אחר מהמפתח הראשי (`TownCode` ← `CityCode`) |
| טבלה **בלי** מפתח זר | טבלה שאף שדה בה לא מפנה לטבלה אחרת (כמו Cities) |
| **DDL** | `CREATE` · `ALTER` · `DROP` (מבנה) |
| **DML** | `SELECT` · `INSERT` · `UPDATE` · `DELETE` (נתונים) |
| **View / שאילתה שמורה** | שאילתה עם שם, שמשתמשים בה כמו בטבלה |

## 2. סדר הכתיבה של SELECT

</div>

```sql
SELECT   [DISTINCT] col1, col2, COUNT(*) AS cnt  -- 5. which columns to show (AS = a new heading)
FROM     T1, T2                                  -- 1. from which tables (or saved queries)
WHERE    pk = fk AND col3 > 10                   -- 2. which rows (before grouping)
GROUP BY col1, col2                              -- 3. group the rows
HAVING   COUNT(*) >= 2                           -- 4. which groups (after grouping)
ORDER BY col1 DESC;                              -- 6. sort (ASC = ascending, the default)
```

<div dir="rtl">

## 3. תנאים ב‑WHERE

| הכתיב | פירוש | ⚠️ |
|-------|-------|----|
| `=` `<>` `>` `<` `>=` `<=` | שווה · שונה · גדול · קטן · גדול או שווה · קטן או שווה | `>` לא כולל את הקצה |
| `BETWEEN 16 AND 19` | בין 16 ל‑19 | **כולל** את 16 ואת 19 |
| `IN (1, 5)` | אחד מהערכים | זה כמו `= 1 OR = 5` |
| `LIKE "%ים%"` | מכיל "ים" | `%` = כל רצף של תווים, גם ריק |
| `LIKE "ש%"` | מתחיל ב"ש" | `LIKE "%ש"` = מסתיים ב"ש" |
| `LIKE "_a%"` | האות השנייה היא a | `_` = תו **אחד** בדיוק |
| `IS NULL` / `IS NOT NULL` | אין ערך / יש ערך | **אף פעם** לא `= NULL` |
| `AND` / `OR` / `NOT` | וגם / או / לא | AND מתבצע לפני OR, ולכן כדאי להוסיף סוגריים: `(A OR B) AND C` |

**כינוי (AS):** `SELECT HourRate * 0.9 AS NewRate` מציג עמודה שהכותרת שלה NewRate. גם `COUNT(*) AS Total`. בשאלות "איזו שאילתה הציגה את הטבלה" **הכותרות** הן הרמז הראשון.

## 4. צירוף טבלאות: שתי צורות, אותה תוצאה

</div>

```sql
-- the exam's form (comma + condition in WHERE). Members.TownCode -> Cities.CityCode
SELECT FirstName, CityName
FROM Members, Cities
WHERE TownCode = CityCode;

-- the JOIN form (the same result)
SELECT FirstName, CityName
FROM Members JOIN Cities ON TownCode = CityCode;
```

<div dir="rtl">

- **שלוש טבלאות** = **שני** תנאי חיבור (`MemberId = MemberNum AND ClubNum = ClubCode`).
- **שכחתם את תנאי החיבור?** כל שורה מתחברת לכל שורה (מכפלה). 5 × 12 = 60 שורות.
- בבחינה שמות השדות ייחודיים, ולכן לא כותבים את שם הטבלה. (אם בבסיס נתונים אחר אותו שם נמצא בשתי טבלאות, **חובה** לכתוב אותו: `Members.CityCode`.)
- "כל אחד, **גם** מי שאין לו התאמה" → `LEFT JOIN ... ON ...`.

## 5. פונקציות קיבוץ

| הפונקציה | מה היא מחזירה |
|----------|---------------|
| `COUNT(*)` | מספר השורות |
| `COUNT(col)` | מספר השורות שיש בהן ערך (בלי NULL) |
| `SUM` · `AVG` · `MIN` · `MAX` | סכום · ממוצע · הקטן ביותר · הגדול ביותר |

**החוק:** כל שדה שמופיע ב‑`SELECT` ואינו בתוך פונקציה **חייב** להופיע גם ב‑`GROUP BY`.
**ההבדל בין WHERE ל‑HAVING:** תנאי על **שורה** כותבים ב‑`WHERE`. תנאי על **פונקציה** (`COUNT`, `AVG`...) כותבים ב‑`HAVING`.

## 6. תת־שאילתות

</div>

```sql
-- those who do NOT appear in another table
SELECT CoachFirstName FROM Coaches
WHERE CoachCode NOT IN (SELECT TrainerCode FROM Clubs);

-- compare with a single value (max / average)
SELECT ClubName FROM Clubs
WHERE Price = (SELECT MAX(Price) FROM Clubs);
```

<div dir="rtl">

> ⚠️ אם בתת־השאילתה של `NOT IN` יש **NULL**, התוצאה ריקה. אפשר להוסיף לה `WHERE TrainerCode IS NOT NULL`.
> ⚠️ ב‑`(SELECT x FROM T)` השדה x חייב להיות שדה **של T**: `NOT IN (SELECT TrainerCode FROM Clubs)`, לא `CoachCode`.

## 7. שינוי נתונים ומבנה

</div>

```sql
-- data (rows)
INSERT INTO Songs (SongCode, SongName, SongYear) VALUES (117, "eyes", 2019);
UPDATE Contestants SET Result = Result * 1.10 WHERE TownCode = 5;
DELETE FROM Contestants WHERE Age < 18 AND Result < 85;

-- structure (tables and columns)
CREATE TABLE Cities (CityCode INTEGER PRIMARY KEY, CityName TEXT NOT NULL);
ALTER TABLE Contestants ADD Rating INTEGER;              -- add a column
ALTER TABLE Contestants DROP COLUMN Rating;              -- delete a column
ALTER TABLE Contestants MODIFY COLUMN Rating VARCHAR(10); -- change a column's type (MySQL)
DROP TABLE Cities;                                       -- delete the whole table

CREATE VIEW Q1 AS SELECT MAX(Result) AS big FROM Contestants;   -- a saved query
SELECT LastName FROM Contestants, Q1 WHERE Result = big;        -- used like a table
```

<div dir="rtl">

| ❌ טעות נפוצה | ✅ הנכון |
|--------------|---------|
| `UPDATE` / `DELETE` בלי `WHERE` | בלי `WHERE` **כל** הרשומות יתעדכנו או יימחקו |
| `INSERT INTO TABLE ...` | `INSERT INTO Songs ...` (בלי המילה TABLE) |
| `SELECT All FROM ...` | `SELECT * FROM ...` |
| `DELETE` כדי לבטל טבלה | `DROP TABLE` |
| `ALTER TABLE ... INSERT col` | `ALTER TABLE ... ADD col` |
| `ALTER TABLE ... DELETE COLUMN col` | `ALTER TABLE ... DROP COLUMN col` |
| `DROP COLUMN col` כדי למחוק **ערך** | `UPDATE ... SET col = NULL WHERE ...` |
| השלמה בעברית ("עדכן", "שם_עיר") | **באנגלית בלבד**, כמו שהפקודה והשדה כתובים |

## 8. אסטרטגיה לשאלות "איזו טבלה תתקבל?"

1. **קודם `FROM` ו‑`WHERE`:** עברו על טבלת הנתונים וסמנו ✓ ליד כל שורה שעונה על התנאי. (`AND` לפני `OR`!)
2. **אחר כך `SELECT`:** אילו עמודות מופיעות בתוצאה? פסלו מיד כל תשובה עם עמודות אחרות.
3. **ספרו שורות:** פסלו כל תשובה עם מספר שורות שונה.
4. **בסוף `ORDER BY` ו‑`DISTINCT`:** בדקו את הסדר, ואם צריך, מחקו כפילויות.
5. **שימו לב לקצוות:** `>` או `>=`, ו‑`BETWEEN` כולל את הקצוות.

**בסעיפי "השלימו את החסר":** קראו את **התוצאה** שמופיעה בשאלה. היא מגלה אילו עמודות ואילו טבלאות חסרות.

**בסעיפי "איזו שאילתה הציגה את הטבלה" (ניתוח פלט):** הפוך מהשיטה למעלה. קודם הכותרות (שמות השדות והכינויים ב‑`AS`), אחר כך מספר השורות, ובסוף התנאים.

**בבחירה של 5 מתוך 7 סעיפים:** התחילו בסעיפים הקצרים (DROP/UPDATE, נכון/לא נכון). השאירו לסוף את מה שמצריך חישוב ארוך.

</div>
