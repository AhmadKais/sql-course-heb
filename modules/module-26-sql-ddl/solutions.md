<div dir="rtl">

# מודול 26 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 הפלטים אמיתיים, מהרצה ברצף אחרי `shelter.sql` ו‑`PRAGMA foreign_keys = ON;`.

---

## ✅ תרגיל 1 — טיפוסים

| העמודה | SQLite | Oracle | למה |
|--------|--------|--------|-----|
| טלפון | `TEXT` | `VARCHAR2(15)` | לא מחשבים איתו; 0 מוביל ומקפים |
| משקל | `REAL` | `NUMBER(5,2)` | מספר עשרוני, עושים ממוצעים |
| מספר שבב | `TEXT` | `VARCHAR2(15)` | "מספר" שלא מחשבים איתו |
| תאריך חיסון | `TEXT` (`YYYY-MM-DD`) | `DATE` | הפרשים, מיון, "הבא בעוד 12 חודשים" |
| מעוקר | `INTEGER` (0/1) | `NUMBER(1)` | אמת/שקר |
| מחיר אימוץ | `REAL` | `NUMBER(7,2)` | כסף — עשרוני מדויק ב‑Oracle |
| מין | `TEXT` | `CHAR(1)` | קוד באורך קבוע |
| ת"ז | `TEXT` | `CHAR(9)` | 0 מוביל! `012345678` כמספר הוא `12345678` |

---

## ✅ תרגיל 2 — CREATE TABLE

</div>

```sql
-- a
CREATE TABLE walk (
  walk_id    INTEGER PRIMARY KEY,
  animal_id  INTEGER NOT NULL REFERENCES animal(animal_id),
  person_id  INTEGER NOT NULL REFERENCES person(person_id),
  walk_date  TEXT    NOT NULL,
  minutes    INTEGER NOT NULL DEFAULT 30,
  notes      TEXT
) STRICT;
```

```text
name   volunteer  walk_date   minutes  notes
-----  ---------  ----------  -------  ------------------
Rocky  Noa        2026-09-20  30
Rex    Amir       2026-09-20  45       pulls on the leash
```

<div dir="rtl">

**ב.** `minutes` = **30** — ברירת המחדל.

**ג.** `cannot store TEXT value in INTEGER column walk.minutes`. **בלי `STRICT`** — `'long'` היה נשמר כטקסט בעמודת מספר, ו‑`SUM(minutes)` היה מתעלם ממנו או מחזיר שטויות.

**ד.** `FOREIGN KEY constraint failed` — אין אדם 99.

---

## ✅ תרגיל 3 — מ‑ERD לטבלה

</div>

```text
   TREATMENT
   # treatment_id
   * treatment_date
   * kind
   o weight_kg
   * cost         (default 0)
   o notes
   relationships:  ANIMAL 1 ----< TREATMENT    (mandatory)
                   PERSON(vet) 1 ----< TREATMENT    (mandatory)
```

```sql
CREATE TABLE treatment (
  treatment_id   INTEGER PRIMARY KEY,
  animal_id      INTEGER NOT NULL REFERENCES animal(animal_id),
  vet_id         INTEGER NOT NULL REFERENCES person(person_id),
  treatment_date TEXT    NOT NULL,
  kind           TEXT    NOT NULL,
  weight_kg      REAL,
  cost           REAL    NOT NULL DEFAULT 0,
  notes          TEXT
) STRICT;

INSERT INTO treatment (animal_id, vet_id, treatment_date, kind, weight_kg, cost)
VALUES (8, 4, '2026-09-01', 'leg check-up', 12.6, 150);
INSERT INTO treatment (animal_id, vet_id, treatment_date, kind)
VALUES (9, 5, '2026-09-05', 'quarantine release exam');
INSERT INTO treatment (animal_id, vet_id, treatment_date, kind, cost, notes)
VALUES (3, 4, '2026-09-10', 'hip follow-up', 200, 'stable');

SELECT a.name, p.last_name AS vet, t.treatment_date, t.kind, t.cost
FROM   treatment t
JOIN   animal a ON a.animal_id = t.animal_id
JOIN   person p ON p.person_id = t.vet_id
ORDER  BY t.treatment_date;
```

```text
name   vet    treatment_date  kind                     cost
-----  -----  --------------  -----------------------  -----
Max    Levi   2026-09-01      leg check-up             150.0
Nala   Nahum  2026-09-05      quarantine release exam  0.0
Rocky  Levi   2026-09-10      hip follow-up            200.0
```

<div dir="rtl">

> 💡 **`vet_id` ולא `person_id`** — שם התפקיד (סעיף 5). ⚠️ שימו לב: `REFERENCES person` לא מבטיח שהאדם הוא **וטרינר** — רק שהוא קיים. כדי לאכוף "רק וטרינר" צריך טבלת טיפוס‑משנה נפרדת `vet`, או בדיקה בקוד. **עוד החלטת עיצוב ממודול 4 שיש לה מחיר ב‑SQL.**

---

## ✅ תרגיל 4 — ALTER TABLE

</div>

```sql
-- a   all 20 animals get 0
ALTER TABLE animal ADD COLUMN is_neutered INTEGER NOT NULL DEFAULT 0;

-- b
ALTER TABLE animal ADD COLUMN arrival_note TEXT NOT NULL;
-- Error: Cannot add a NOT NULL column with default value NULL
```

<div dir="rtl">

**ב.** בטבלה כבר יש 20 שורות. העמודה החדשה צריכה ערך בכל אחת — ולא נתתם. NULL אסור (`NOT NULL`), ואין ברירת מחדל. **עמודת חובה חדשה בטבלה קיימת ⟵ חייבת `DEFAULT`.**

</div>

```sql
-- c   Rex
UPDATE animal SET is_neutered = 1
WHERE  animal_id IN (SELECT animal_id FROM expense WHERE description = 'neutering surgery');

-- d
ALTER TABLE walk RENAME COLUMN notes TO remarks;
ALTER TABLE walk DROP COLUMN remarks;
```

<div dir="rtl">

---

## ✅ תרגיל 5 — DROP, TRUNCATE, DELETE

</div>

```sql
-- a   9
CREATE TABLE dog AS SELECT * FROM animal WHERE species_id = 1;

-- b
SELECT sql FROM sqlite_master WHERE name = 'dog';
```

```text
CREATE TABLE dog(
  animal_id INT,
  name TEXT,
  species_id INT,
  breed TEXT,
  sex TEXT,
  birth_date TEXT,
  weight_kg REAL,
  chip_number TEXT,
  status TEXT,
  is_neutered INT
)
```

<div dir="rtl">

**חסר הכול חוץ מהשמות והטיפוסים:** אין `PRIMARY KEY`, אין `NOT NULL`, אין `CHECK` על `sex`, אין `UNIQUE` על השבב, אין `REFERENCES species`. **`CREATE TABLE … AS` מעתיק נתונים, לא חוקים.**

</div>

```sql
-- c
DELETE FROM dog;           -- SQLite. Oracle (fastest): TRUNCATE TABLE dog;
DROP TABLE dog;

-- d
SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name;
PRAGMA table_info(walk);
```

<div dir="rtl">

**ג.** ב‑Oracle `TRUNCATE TABLE dog` מהיר בהרבה מ‑`DELETE` על טבלה גדולה — הוא לא מוחק שורה‑שורה, אלא משחרר את כל השטח בבת אחת. **המחיר:** זה DDL — `COMMIT` אוטומטי, **אין `ROLLBACK`**, ואין `WHERE`.

---

## ✅ תרגיל 6 — הפרויקט שלכם

אין פתרון אחד — זה הפרויקט שלכם. **רשימת בדיקה:**

| ✔ | הבדיקה |
|---|--------|
| ☐ | לכל טבלה `PRIMARY KEY` |
| ☐ | כל `*` ב‑ERD ⟵ `NOT NULL` |
| ☐ | כל קו ב‑ERD ⟵ `REFERENCES` בצד ה"רבים" |
| ☐ | טבלאות קישור לכל יחס רבים‑לרבים (מודול 5) |
| ☐ | `STRICT` על כל טבלה |
| ☐ | `DROP TABLE IF EXISTS` בסדר הפוך בראש הסקריפט |
| ☐ | הסקריפט רץ **פעמיים ברצף** בלי שגיאה |
| ☐ | 3 שאילתות `JOIN` מחזירות תוצאות הגיוניות |

> 💡 **"רץ פעמיים ברצף"** היא הבדיקה החשובה ביותר. אם הסקריפט נכשל בפעם השנייה — ה‑`DROP`‑ים חסרים או בסדר הלא נכון.

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[❓ לשאלות](questions.md)**

</div>

</div>

<!-- exam-style:start -->
<div dir="rtl">

---

## 🎓 תרגול בסגנון הבחינה: פתרונות

**ב1.** **3.**

**ב2.** | הפקודה | מה נמחק? | הטבלה נשארת? |
|---|---|---|
| `DELETE ... WHERE` | רק הרשומות שעונות על התנאי | כן |
| `DELETE FROM Clubs` | כל הרשומות | כן, ריקה |
| `DROP TABLE Clubs` | הכול, כולל המבנה | **לא** |

**ב3.** ```sql
CREATE TABLE Halls (
  HallCode  INTEGER PRIMARY KEY,
  HallName  TEXT NOT NULL,
  Capacity  INTEGER
);
```


</div>
<!-- exam-style:end -->
