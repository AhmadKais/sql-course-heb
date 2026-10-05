<div dir="rtl">

# דף עזר לבחינה: SQL ובסיסי נתונים

> בבחינה (שאלון 735911) **מותר להביא כל חומר עזר כתוב**. הדפיסו את הדף הזה, הוסיפו לו הערות בכתב יד, והביאו אותו לבחינה.

## 1. מושגים: תשובה בשורה אחת

| המושג | התשובה |
|-------|--------|
| **מפתח ראשי (PK)** | מזהה כל רשומה: ייחודי, לא ריק, יציב |
| **מפתח זר (FK)** | שדה שמכיל ערך של מפתח ראשי מטבלה **אחרת** |
| **מפתח מורכב** | מפתח ראשי שבנוי משני שדות או יותר (כמו בטבלת קישור) |
| **1:N** | המפתח הזר נמצא בצד ה"רבים" |
| **N:M** | צריך **טבלת קישור** עם שני מפתחות זרים |
| טבלה **בלי** מפתח זר | טבלה שאף שדה בה לא מפנה לטבלה אחרת (כמו Cities) |
| **DDL** | `CREATE` · `ALTER` · `DROP` (מבנה) |
| **DML** | `SELECT` · `INSERT` · `UPDATE` · `DELETE` (נתונים) |
| **View / שאילתה שמורה** | שאילתה עם שם, שמשתמשים בה כמו בטבלה |

## 2. סדר הכתיבה של SELECT

</div>

```sql
SELECT   [DISTINCT] T.col1, T.col2, COUNT(*) AS cnt  -- 5. which columns to show
FROM     T1, T2                                      -- 1. from which tables
WHERE    T1.k = T2.fk AND T1.col > 10                -- 2. which rows (before grouping)
GROUP BY T.col1                                      -- 3. group the rows
HAVING   COUNT(*) >= 2                               -- 4. which groups (after grouping)
ORDER BY T.col1 DESC;                                -- 6. sort (ASC = ascending, the default)
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
| `AND` / `OR` / `NOT` | וגם / או / לא | AND מתבצע לפני OR, ולכן כדאי להוסיף סוגריים |

## 4. צירוף טבלאות: שתי צורות, אותה תוצאה

</div>

```sql
-- the exam's form (comma + condition in WHERE)
SELECT Members.FirstName, Cities.CityName
FROM Members, Cities
WHERE Members.CityCode = Cities.CityCode;

-- the JOIN form (the same result)
SELECT Members.FirstName, Cities.CityName
FROM Members JOIN Cities ON Members.CityCode = Cities.CityCode;
```

<div dir="rtl">

- **שלוש טבלאות** = **שני** תנאי חיבור (`A.k = B.fk AND B.k2 = C.fk2`).
- **שכחתם את תנאי החיבור?** כל שורה מתחברת לכל שורה (מכפלה). 5 × 12 = 60 שורות.
- כשאותו שם שדה נמצא בשתי טבלאות, **חובה** לכתוב את שם הטבלה: `Members.CityCode`.
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
SELECT Coaches.FirstName FROM Coaches
WHERE Coaches.CoachCode NOT IN (SELECT CoachCode FROM Clubs);

-- compare with a single value (max / average)
SELECT Clubs.ClubName FROM Clubs
WHERE Clubs.Price = (SELECT MAX(Price) FROM Clubs);
```

<div dir="rtl">

> ⚠️ אם בתת־השאילתה של `NOT IN` יש **NULL**, התוצאה ריקה. אפשר להוסיף לה `WHERE CoachCode IS NOT NULL`.

## 7. שינוי נתונים ומבנה

</div>

```sql
INSERT INTO Songs (SongCode, SongName, SongYear) VALUES (117, "eyes", 2019);
UPDATE Contestants SET Result = Result * 1.10 WHERE TownCode = 5;
DELETE FROM Contestants WHERE Age < 18 AND Result < 85;

CREATE TABLE Cities (CityCode INTEGER PRIMARY KEY, CityName TEXT NOT NULL);
ALTER TABLE Contestants ADD Rating INTEGER;     -- add a column
DROP TABLE Cities;                              -- delete the whole table

CREATE VIEW Q1 AS SELECT MAX(Result) AS big FROM Contestants;   -- a saved query
```

<div dir="rtl">

| ❌ טעות נפוצה | ✅ הנכון |
|--------------|---------|
| `UPDATE` / `DELETE` בלי `WHERE` | בלי `WHERE` **כל** הרשומות יתעדכנו או יימחקו |
| `INSERT INTO TABLE ...` | `INSERT INTO Songs ...` (בלי המילה TABLE) |
| `SELECT All FROM ...` | `SELECT * FROM ...` |
| `DELETE` כדי לבטל טבלה | `DROP TABLE` |
| `ALTER TABLE ... INSERT col` | `ALTER TABLE ... ADD col` |

## 8. אסטרטגיה לשאלות "איזו טבלה תתקבל?"

1. **קודם `FROM` ו‑`WHERE`:** עברו על טבלת הנתונים וסמנו ✓ ליד כל שורה שעונה על התנאי.
2. **אחר כך `SELECT`:** אילו עמודות מופיעות בתוצאה? פסלו מיד כל תשובה עם עמודות אחרות.
3. **ספרו שורות:** פסלו כל תשובה עם מספר שורות שונה.
4. **בסוף `ORDER BY` ו‑`DISTINCT`:** בדקו את הסדר, ואם צריך, מחקו כפילויות.
5. **שימו לב לקצוות:** `>` או `>=`, ו‑`BETWEEN` כולל את הקצוות.

**בסעיפי "השלימו את החסר":** קראו את **התוצאה** שמופיעה בשאלה. היא מגלה אילו עמודות ואילו טבלאות חסרות.

**בבחירה של 5 מתוך 7 סעיפים:** התחילו בסעיפים הקצרים (DROP/UPDATE, נכון/לא נכון). השאירו לסוף את מה שמצריך חישוב ארוך.

</div>
