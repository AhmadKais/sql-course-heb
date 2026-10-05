<div dir="rtl">

# מודול 28 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 הפלטים אמיתיים, נכון ל‑`'2026-09-21'`.

---

## ✅ תרגיל 1 — View ראשון

</div>

```sql
-- a   9 rows
CREATE VIEW dog_view AS
SELECT animal_id, name, breed, weight_kg, status
FROM   animal
WHERE  species_id = 1;

-- b   Rex 38.7, Rocky 31.0, Shadow 25.1
SELECT name, weight_kg FROM dog_view WHERE status = 'available' ORDER BY weight_kg DESC;

-- c   Cat 4, Dog 3, Parrot 1, Rabbit 1
SELECT species, COUNT(*) FROM available_animal GROUP BY species;

-- d
UPDATE animal SET status = 'available' WHERE animal_id = 9;
SELECT COUNT(*) FROM available_animal;        -- 10 (was 9)
```

<div dir="rtl">

**ד.** **לא.** View לא שומר נתונים — השאילתה שבתוכו רצה מחדש בכל פעם. Nala מופיעה מיד.

---

## ✅ תרגיל 2 — View שמסתיר מורכבות

</div>

```sql
-- a
CREATE VIEW vaccination_detail AS
SELECT v.vaccination_id,
       a.name       AS animal,
       vt.name      AS vaccine,
       p.last_name  AS vet,
       v.given_date,
       v.cost,
       DATE(v.given_date, '+' || vt.interval_months || ' months') AS next_due
FROM   vaccination  v
JOIN   animal       a  ON a.animal_id        = v.animal_id
JOIN   vaccine_type vt ON vt.vaccine_type_id = v.vaccine_type_id
JOIN   person       p  ON p.person_id        = v.vet_id;

-- b
SELECT animal, vaccine, given_date, next_due
FROM   vaccination_detail WHERE animal = 'Rocky' ORDER BY given_date;
```

```text
animal  vaccine  given_date  next_due
------  -------  ----------  ----------
Rocky   Rabies   2023-05-25  2024-05-25
Rocky   DHPP     2023-05-25  2024-05-25
Rocky   Rabies   2024-05-28  2025-05-28
Rocky   Rabies   2025-05-30  2026-05-30
```

<div dir="rtl">

**ג.** **28 — בדיוק כמו `vaccination`.** כל ה‑`JOIN`‑ים הם "רבים ⟵ אחד" (לכל חיסון חיה אחת, סוג אחד, וטרינר אחד), אז הם לא מכפילים ולא מעלימים שורות. **זו הבדיקה לכל View עם JOIN:** מספר השורות שווה לטבלה המרכזית. אם היה יותר — יש כפל; פחות — `JOIN` העלים שורות (וצריך `LEFT`).

> 💡 **הערך של ה‑View:** מעכשיו, "מתי החיסון הבא של X?" היא שאילתה של שורה אחת. החישוב עם `interval_months` ו‑`DATE(… '+n months')` — כתוב במקום אחד.

---

## ✅ תרגיל 3 — View כדוח

</div>

```sql
-- a
CREATE VIEW yearly_finance AS
SELECT y AS year,
       SUM(income)                AS income,
       SUM(expense)               AS expense,
       SUM(income) - SUM(expense) AS balance
FROM  (SELECT STRFTIME('%Y', adoption_date) AS y, fee_paid AS income, 0 AS expense FROM adoption
       UNION ALL
       SELECT STRFTIME('%Y', expense_date), 0, amount FROM expense)
GROUP  BY y;

SELECT * FROM yearly_finance;
```

```text
year  income  expense  balance
----  ------  -------  --------
2023  500.0   0        500.0       <- no expenses were recorded in 2023
2024  1150.0  16920.0  -15770.0
2025  550.0   2880.0   -2330.0
```

```sql
-- b
CREATE VIEW in_shelter AS
SELECT a.animal_id, a.name, a.status,
       (SELECT MAX(i.intake_date) FROM intake i WHERE i.animal_id = a.animal_id) AS since
FROM   animal a
WHERE  a.status IN ('available', 'medical', 'quarantine');

SELECT name, status, since,
       CAST(JULIANDAY('2026-09-21') - JULIANDAY(since) AS INTEGER) AS days
FROM   in_shelter
ORDER  BY days DESC
LIMIT  4;
```

```text
name   status     since       days
-----  ---------  ----------  ----
Rocky  available  2023-05-20  1220
Mitzi  available  2023-06-11  1198
Coco   available  2023-09-30  1087
Max    medical    2023-11-05  1051
```

<div dir="rtl">

**ג.** כי `JOIN` של `animal` גם ל‑`expense` וגם ל‑`vaccination` **מכפיל**: לכל הוצאה × כל חיסון. ל‑Rocky — הוצאה אחת ו‑4 חיסונים ⟵ 4 שורות ⟵ ההוצאות היו **2,400** במקום 600 (מודול 23, תרגיל 6ג). תת‑שאילתה לכל טבלה — כל סכום מחושב בנפרד, נכון.

---

## ✅ תרגיל 4 — מצב נוכחי מתוך היסטוריה

</div>

```sql
-- a   8
SELECT COUNT(*) FROM current_home;

-- b   9
SELECT COUNT(*) FROM adoption;
```

<div dir="rtl">

**ב.** 9 אימוצים בהיסטוריה — אבל אחד מהם (Luna אצל Dana, 2023) **הסתיים** בהחזרה. 8 = מה שנכון **היום**. **הטבלה זוכרת הכול; ה‑View עונה על ההווה.**

</div>

```sql
-- c
CREATE VIEW latest_vaccine AS
SELECT animal, vaccine, MAX(given_date) AS last_given, MAX(next_due) AS next_due
FROM   vaccination_detail
GROUP  BY animal, vaccine;

SELECT COUNT(*) FROM latest_vaccine WHERE next_due < '2026-09-21';     -- 25
```

<div dir="rtl">

**25 — כמעט הכול.** כי ה‑View כולל **כל** חיה שחוסנה אי פעם: גם מאומצות (באחריות המשפחה), גם Daisy שמתה. **לצמצם:** להוסיף ל‑`vaccination_detail` את `a.status`, ולסנן `WHERE status IN ('available', 'medical', 'quarantine')`. **שאילתה נכונה טכנית ≠ תשובה עסקית** (מודול 22, תרגיל 4ב).

> 💡 **`GROUP BY animal`** — כאן בסדר כי אין שתי חיות באותו שם. בעבודה אמיתית — הוסיפו `animal_id` ל‑View וקבצו לפיו (מודול 24, סעיף 4).

---

## ✅ תרגיל 5 — אבטחה ועדכון

</div>

```sql
-- a
CREATE VIEW public_person AS
SELECT person_id, first_name, city, role FROM person;
```

<div dir="rtl">

**א.** מתנדבים צריכים לדעת מי עוד בצוות ומאיפה — לא את הטלפונים והשמות המלאים של המאמצים. נותנים הרשאה ל‑View בלבד (מודול 30), והמידע הרגיש פשוט **לא נגיש**. זה גם עניין של חוק הגנת הפרטיות.

**ב.** `cannot modify available_animal because it is a view`. מעדכנים את הטבלה: `UPDATE animal SET weight_kg = 30 WHERE animal_id = 3;`

**ג.**

| ה‑View | עדכון ב‑Oracle? | למה |
|--------|-----------------|-----|
| `dog_view` | ✅ | טבלה אחת, עמודות פשוטות |
| `available_animal` | חלקית | יש `JOIN` ועמודה מחושבת (`age`) — אפשר רק את עמודות `animal` שאינן מחושבות |
| `yearly_finance` | ❌ | `GROUP BY`, `SUM`, `UNION ALL` — שורה ב‑View היא הרבה שורות |
| `current_home` | כמעט לא | `JOIN` של שלוש טבלאות, ועמודת `adopter` מחושבת |

**ד.** `species_id` **בכלל לא ב‑`dog_view`** — אז ה‑`UPDATE` ייכשל עוד לפני `CHECK OPTION` ("invalid identifier"). אילו היה ב‑View: **עם** `CHECK OPTION` ⟵ `ORA-01402`, כי Rex היה יוצא מ‑`WHERE species_id = 1`. **בלי** ⟵ העדכון מצליח, ו‑Rex "נעלם" מ‑`dog_view` והופך לחתול של 38.7 ק"ג.

---

## ✅ תרגיל 6 — ניהול

</div>

```sql
-- a
SELECT name FROM sqlite_master WHERE type = 'view';

-- b   no -- a View holds no data
DROP VIEW animal_cost;
SELECT COUNT(*) FROM expense;     -- still 22

-- c   SQLite
DROP VIEW available_animal;
CREATE VIEW available_animal AS
SELECT ... WHERE a.status IN ('available', 'quarantine');

-- c   Oracle
CREATE OR REPLACE VIEW available_animal AS
SELECT ... WHERE a.status IN ('available', 'quarantine');
```

<div dir="rtl">

> 💡 **ההבדל חשוב ב‑Oracle:** `DROP` + `CREATE` מוחק גם את ה**הרשאות** שניתנו על ה‑View (מודול 30). `CREATE OR REPLACE` שומר אותן.

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[❓ לשאלות](questions.md)**

</div>

</div>

<!-- exam-style:start -->
<div dir="rtl">

---

## 🎓 תרגול בסגנון הבחינה: פתרונות

**ב1.** 1. **120** 2. `Q1` · `Q1.cheap`. ב‑SQL שומרים את Q1 כך:
```sql
CREATE VIEW Q1 AS SELECT MIN(Clubs.Price) AS cheap FROM Clubs;
SELECT Clubs.ClubName FROM Clubs, Q1 WHERE Clubs.Price = Q1.cheap;
```

<figure dir="ltr" class="dbtable">

| ClubName |
|:---:|
| יוגה |

</figure>


</div>
<!-- exam-style:end -->
