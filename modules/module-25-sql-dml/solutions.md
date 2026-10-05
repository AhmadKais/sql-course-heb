<div dir="rtl">

# מודול 25 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 הפלטים אמיתיים, מהרצת כל התרגילים **ברצף** אחרי `shelter.sql` ו‑`PRAGMA foreign_keys = ON;`.

---

## ✅ תרגיל 1 — INSERT

</div>

```sql
-- a   gets person_id 13 (max + 1)
INSERT INTO person (first_name, last_name, role, city, phone, joined_date)
VALUES ('Nour', 'Haddad', 'volunteer', 'Yarka', '052-3434343', '2026-09-01');

SELECT person_id, first_name, city FROM person WHERE last_name = 'Haddad';
-- 13 | Nour | Yarka

-- b   one INSERT, two rows -> ids 21 and 22
INSERT INTO animal (name, species_id, sex, status)
VALUES ('Lucky', 1, 'M', 'quarantine'),
       ('Snow',  2, 'F', 'quarantine');

-- c
INSERT INTO intake (animal_id, intake_date, intake_type, brought_by, location)
VALUES (21, '2026-09-20', 'stray', 13, 'Yarka center');
-- intake_id 22 | animal 21 | stray | brought_by 13 | Yarka center

-- d
INSERT INTO intake (animal_id, intake_date, intake_type) VALUES (99, '2026-09-20', 'stray');
-- Error: FOREIGN KEY constraint failed
```

<div dir="rtl">

**ד.** אין חיה מספר 99 — המפתח הזר חוסם. **בלי `PRAGMA foreign_keys = ON`** השורה הייתה נכנסת: קליטה של חיה שלא קיימת. כל `JOIN` ל‑`animal` היה מעלים אותה בשקט, וכל `COUNT` על `intake` היה סופר אותה. **שורה יתומה.**

> 💡 **בסעיף ג' השתמשנו במזהים 21 ו‑13** שקיבלנו בסעיפים הקודמים. בקוד אמיתי לא "מנחשים" מזהה — שולפים אותו (`SELECT animal_id FROM animal WHERE name = 'Lucky'`), או משתמשים ב‑`last_insert_rowid()` (SQLite) / `RETURNING` (Oracle, PostgreSQL).

---

## ✅ תרגיל 2 — אילוצים

| ה‑INSERT | השגיאה | החוק העסקי |
|-----------|---------|-------------|
| `Ghost` בלי `status` | `NOT NULL constraint failed: animal.status` | לכל חיה **חייב** להיות מצב |
| `Twin` עם `sex = 'X'` | `CHECK constraint failed: sex IN ('M','F','U')` | מין — רק מהרשימה |
| `Dup` עם `animal_id = 1` | `UNIQUE constraint failed: animal.animal_id` | מזהה ייחודי (מפתח ראשי) |
| `Copy` עם השבב של Luna | `UNIQUE constraint failed: animal.chip_number` | שבב אחד = חיה אחת |

> 🔑 כל אחת מארבע השורות האלה הייתה **טעות הקלדה** בעולם האמיתי. האילוצים תפסו את כולן לפני שנכנסו. זו הסיבה שמגדירים אותם (מודול 27).

---

## ✅ תרגיל 3 — UPDATE

</div>

```sql
-- a
SELECT animal_id, name, status FROM animal WHERE name = 'Nala';     -- 9 | Nala | quarantine
UPDATE animal SET status = 'available' WHERE animal_id = 9;
SELECT changes();                                                    -- 1

-- b
UPDATE animal SET breed = 'Mixed' WHERE breed IS NULL AND species_id = 2;
SELECT changes();                                                    -- 4
```

<div dir="rtl">

**ב. 4, לא 3** — כי בתרגיל 1 הוספנו את **Snow**, חתולה בלי גזע. Mitzi, Nala, Lily **ו‑Snow**. זה בדיוק למה `changes()` חשוב: הוא מספר מה **באמת** קרה, לא מה שזכרתם.

</div>

```sql
-- c
UPDATE person SET city = 'Haifa' WHERE first_name = 'Lior';
SELECT changes();                                                    -- 1
```

<div dir="rtl">

**ג. 1** — למרות שהערך לא השתנה בפועל (Haifa ⟵ Haifa). `changes()` סופר **שורות שהתאימו ל‑`WHERE`**, לא שורות שהערך שלהן השתנה. **הלקח:** `changes() = 1` אומר "מצאתי שורה אחת", לא "שיניתי משהו".

</div>

```sql
-- d
UPDATE expense SET amount = amount * 1.18 WHERE category = 'utilities';
SELECT changes();                                                    -- 4
SELECT SUM(amount) FROM expense WHERE category = 'utilities';        -- 4448.6  (was 3770)

-- e
UPDATE animal
SET    status = 'adopted'
WHERE  animal_id IN (SELECT animal_id FROM adoption WHERE returned_date IS NULL)
  AND  status <> 'adopted';
SELECT changes();                                                    -- 0
```

<div dir="rtl">

**ה. 0** — כל החיות עם אימוץ פעיל כבר מסומנות `adopted`. **הנתונים עקביים.** `UPDATE` כזה הוא גם "תיקון" וגם "בדיקה": אם יום אחד יחזיר מספר גדול מ‑0 — מישהו רשם אימוץ ושכח לעדכן את החיה.

---

## ✅ תרגיל 4 — DELETE

</div>

```sql
-- a
DELETE FROM species WHERE species_id = 4;
-- Error: FOREIGN KEY constraint failed    (Coco and Kiwi are parrots)

-- b
DELETE FROM vaccine_type WHERE vaccine_type_id = 5;
-- Error: FOREIGN KEY constraint failed    (Thumper and Bunny got Myxomatosis)

-- c
CREATE TABLE expense_backup AS SELECT * FROM expense;               -- backup first!
DELETE FROM expense WHERE animal_id IS NULL AND expense_date < '2024-04-01';
SELECT changes();                                                    -- 5
```

<div dir="rtl">

**ג.** 5 הוצאות כלליות לפני אפריל: מזון (ינואר), חשמל (ינואר), חול לחתולים, חשמל (פברואר), מזון (מרץ).

**ד.** Daisy לא נמחקה — `status = 'deceased'`. כל ההיסטוריה שלה נשמרת: הקליטה, החיסון, ההוצאה על ביקור החירום. דוח של 2024 עדיין יכלול אותה. **מחיקה רכה** — סעיף 6.2.

---

## ✅ תרגיל 5 — DEFAULT ו‑upsert

</div>

```sql
-- a
INSERT INTO donation (donor_name, amount, donation_date, method) VALUES ('Carmel School', 1200, '2026-06-01', 'transfer');
INSERT INTO donation (donor_name, amount, method)                VALUES ('Anonymous',     250, 'bit');
INSERT INTO donation (donor_name, amount)                        VALUES ('Haifa Rotary',  5000);
SELECT * FROM donation;
```

```text
donation_id  donor_name     amount  donation_date  method
-----------  -------------  ------  -------------  --------
1            Carmel School  1200.0  2026-06-01     transfer
2            Anonymous      250.0   2026-09-21     bit
3            Haifa Rotary   5000.0  2026-09-21     cash
```

<div dir="rtl">

**ב.** `NOT NULL constraint failed: donation.donor_name` — `DEFAULT VALUES` נותן לכל עמודה את ברירת המחדל שלה, אבל ל‑`donor_name` ול‑`amount` **אין** ברירת מחדל, והן `NOT NULL`. אין ממה למלא.

</div>

```sql
-- c
INSERT INTO stock (item, qty) VALUES ('dog food sack', 8), ('flea collar', 20)
ON CONFLICT(item) DO UPDATE SET qty = qty + excluded.qty;
```

```text
item           qty
-------------  ---
dog food sack  20      <- 12 + 8
cat litter     5       <- untouched
flea collar    20      <- new
```

<div dir="rtl">

**ד.** `ON CONFLICT clause does not match any PRIMARY KEY or UNIQUE constraint`. **בלי אילוץ ייחודיות — אין "התנגשות"**, ולכן אין למה להגיב. בסיס הנתונים לא יכול לנחש ש‑`item` "אמור" להיות ייחודי — **רק אילוץ אומר לו את זה.**

---

## ✅ תרגיל 6 — INSERT … SELECT

</div>

```sql
-- a   2 rows: adoptions 1 and 2
CREATE TABLE adoption_archive AS SELECT * FROM adoption WHERE 0;
INSERT INTO adoption_archive SELECT * FROM adoption WHERE adoption_date LIKE '2023%';

-- b
CREATE TABLE vip_adopter (person_id INTEGER, full_name TEXT, adoptions INTEGER);

INSERT INTO vip_adopter
SELECT p.person_id, p.first_name || ' ' || p.last_name, COUNT(*)
FROM   adoption ad
JOIN   person p ON p.person_id = ad.adopter_id
GROUP  BY p.person_id
HAVING COUNT(*) > 1;

SELECT * FROM vip_adopter;
```

```text
person_id  full_name   adoptions
---------  ----------  ---------
6          Dana Cohen  2
8          Lior Bar    2
9          Shira Katz  2
```

```sql
-- c   SQLite: two INSERT ... SELECT
CREATE TABLE stray_log     (intake_id INTEGER, animal_id INTEGER, location TEXT);
CREATE TABLE surrender_log (intake_id INTEGER, animal_id INTEGER, reason   TEXT);

INSERT INTO stray_log     SELECT intake_id, animal_id, location FROM intake WHERE intake_type = 'stray';
INSERT INTO surrender_log SELECT intake_id, animal_id, reason   FROM intake WHERE intake_type = 'surrender';
-- 11 strays, 8 surrenders (the 2 transfers go nowhere)

-- Oracle: one pass
INSERT ALL
  WHEN intake_type = 'stray'     THEN INTO stray_log     VALUES (intake_id, animal_id, location)
  WHEN intake_type = 'surrender' THEN INTO surrender_log VALUES (intake_id, animal_id, reason)
SELECT intake_id, animal_id, intake_type, location, reason FROM intake;
```

<div dir="rtl">

> 🔑 **שימו לב: `vip_adopter` היא תמונת מצב.** אם Yossi יאמץ מחר חיה שנייה — הטבלה **לא** תתעדכן. זה ההבדל בין **טבלה** שנבנתה מ‑`SELECT` לבין **View** (מודול 28) — שאילתה שמורה שתמיד מחזירה את המצב העדכני.

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[❓ לשאלות](questions.md)**

</div>

</div>
