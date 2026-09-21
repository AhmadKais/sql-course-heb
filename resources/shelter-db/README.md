<div dir="rtl">

# 🐾 בסיס הנתונים המוכן — מקלט "בית חם"

> **למה זה קיים?** במסלול המשולב, תלמידים כותבים SQL **מהיחידה השנייה** — הרבה לפני שהם יודעים לבנות טבלאות. בשביל זה צריך בסיס נתונים מוכן לשאילתות. זהו.
>
> ביחידה 8 (פרק 12 + 26) הם יבנו **משלהם**, מה‑ERD שעיצבו — ויוכלו להשוות.

---

## איך מתחילים — 30 שניות

1. פתחו את **[Programiz Online SQL](https://www.programiz.com/sql/online-compiler/)**
2. מחקו את מה שיש בחלון הקוד
3. פתחו את [`shelter.sql`](shelter.sql), העתיקו **את כל הקובץ**, והדביקו
4. לחצו **Run**. אם בתחתית מופיע `animals_loaded = 20` — הכול טעון
5. **מתחת** לקוד שהדבקתם, כתבו את השאילתה שלכם ולחצו Run שוב

> ⚠️ **Programiz לא שומר בין ביקורים.** בכל פעם שפותחים — מדביקים את הקובץ מחדש. שלוש שניות. שמרו את השאילתות **שלכם** בקובץ אצלכם.

---

## מה יש בפנים

</div>

```text
+----------------+       +----------------+       +----------------+
| SPECIES        |  1  M | ANIMAL         |  1  M | INTAKE         |
| 4 rows         +-------+ 20 rows        +-------+ 21 rows        |
+----------------+       +---+----+---+---+       +----------------+
                             |    |   |                    ^
              +--------------+    |   +-----------+        | brought_by
              | 1                 | 1             | 1      |
              | M                 | M             | M      |
+-------------+--+   +------------+---+   +-------+--------+---+
| VACCINATION    |   | ADOPTION       |   | EXPENSE            |
| 28 rows        |   | 9 rows         |   | 22 rows            |
+-------+--------+   +-------+--------+   +--------------------+
        | M                  | M               (animal_id may be NULL
        | 1                  | 1                = a general expense)
+-------+--------+   +-------+--------+
| VACCINE_TYPE   |   | PERSON         |<---- also: vet_id on VACCINATION,
| 5 rows         |   | 12 rows        |            brought_by on INTAKE
+----------------+   +----------------+
```

<div dir="rtl">

| הטבלה | מה יש בה | למה היא מעניינת לתרגול |
|--------|-----------|------------------------|
| `species` | 4 מינים + תעריף אימוץ נוכחי | טבלת קוד קטנה — ראשונה ל‑`JOIN` |
| `person` | 12 אנשים: מתנדבים, מאמצים, וטרינרים | עמודת `role` — ל‑`WHERE`, ל‑`CASE` |
| `animal` | 20 חיות | `NULL` ב‑`breed`, `chip_number`, `birth_date` — לתרגול `IS NULL` |
| `intake` | 21 קליטות | ⭐ **לונה נקלטה פעמיים** — ל‑`GROUP BY … HAVING` |
| `vaccine_type` | 5 סוגי חיסון | `interval_months` — לחישוב "מתי הבא" |
| `vaccination` | 28 חיסונים | ⭐ **רוקי קיבל כלבת 3 פעמים** — אותו חיסון חוזר |
| `adoption` | 9 אימוצים | ⭐ **התעריף השתנה** (300 ב‑2023, 400 ב‑2024) · **בלה מעל גיל 8 — חצי מחיר** · **לונה אומצה פעמיים** |
| `expense` | 22 הוצאות | ⭐ `animal_id` הוא `NULL` בהוצאות כלליות — ל‑`LEFT JOIN` ול‑`IS NULL` |

---

## נסו עכשיו — חמש שאילתות ראשונות

</div>

```sql
-- 1. All the dogs
SELECT name, breed, weight_kg
FROM   animal
WHERE  species_id = 1;

-- 2. Animals still waiting for a home, heaviest first
SELECT name, weight_kg
FROM   animal
WHERE  status = 'available'
ORDER  BY weight_kg DESC;

-- 3. Every animal with its species name (your first JOIN)
SELECT a.name, s.name AS species
FROM   animal a
JOIN   species s ON s.species_id = a.species_id;

-- 4. How many animals of each species? (your first GROUP BY)
SELECT s.name AS species, COUNT(*) AS how_many
FROM   animal a
JOIN   species s ON s.species_id = a.species_id
GROUP  BY s.name;

-- 5. Which animal cost the shelter the most?
SELECT a.name, SUM(e.amount) AS total_cost
FROM   animal a
JOIN   expense e ON e.animal_id = a.animal_id
GROUP  BY a.name
ORDER  BY total_cost DESC
LIMIT  3;
```

<div dir="rtl">

---

## מה מחכה בפנים — שאלות ששווה לנסות

מסודרות לפי היחידה שבה תדעו לענות עליהן:

| יחידה | השאלה | הרמז |
|-------|--------|------|
| 2 | אילו חיות הגיעו **בלי שבב**? | `chip_number IS NULL` |
| 2 | מי המתנדבים מחיפה? | `role = 'volunteer' AND city = 'Haifa'` |
| 3 | סדרו את החיות מהוותיקה לצעירה | `ORDER BY birth_date` — ומה קורה ל‑`NULL`? |
| 3 | כמה שנים לכל חיה? | פונקציות תאריך |
| 4 | תייגו כל חיה: "גור" / "בוגר" / "מבוגר" לפי גיל | `CASE` |
| 5 | כל אימוץ עם שם החיה **ושם המאמץ** | שני `JOIN`‑ים |
| 5 | אילו חיות **מעולם לא חוסנו**? | `LEFT JOIN … IS NULL` |
| 6 | איזו חיה נקלטה **יותר מפעם אחת**? | `GROUP BY … HAVING COUNT(*) > 1` |
| 6 | כמה עלה **בממוצע** להחזיק חיה? | `AVG` על `SUM` — תת‑שאילתה |
| 6 | כמה כסף נכנס מדמי אימוץ **בכל שנה**? | `GROUP BY` על חלק מהתאריך |
| 7 | ⭐ מה היה קורה אילו `fee_paid` היה `NOT NULL`? | נסו להכניס שורה בלי — ותראו |

---

## שלושה דברים מוסתרים בנתונים

הם שם בכוונה. תלמיד שמוצא אותם לבד — הבין את הקורס.

| מה | איפה | למה זה שם |
|-----|-------|-----------|
| **לונה** נקלטה ב‑2023, אומצה, **הוחזרה** ב‑2024, ואומצה שוב ב‑2025 | `intake` (2 שורות) · `adoption` (2 שורות, `returned_date` באחת) | מודול 5 + 10: כניסה חוזרת היא `INTAKE` חדש; שהות מחושבת **בנפרד** |
| **בלה** ו**זואי** שילמו 200 במקום 400 | `adoption.fee_paid` | מודול 10: מעל גיל 8 — חצי מחיר. **המחיר קפוא**; אי אפשר לחשב אותו מחדש מ‑`species.adoption_fee` |
| **שק מזון** של 1,850 ₪ — לאף חיה | `expense.animal_id IS NULL` | מודול 7: "הוצאה כללית" אינה ישות — היא `NULL` |

---

<div align="center">

**[🧭 מסלול הלימוד](../../LEARNING-PATH.md)** · **[🛠️ מדריך סביבת העבודה](../setup.md)** · **[🏠 דף הקורס](../../)**

</div>

</div>
