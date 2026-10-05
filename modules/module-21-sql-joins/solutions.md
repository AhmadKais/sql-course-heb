<div dir="rtl">

# מודול 21 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 כל הפלטים אמיתיים, מהרצה על בסיס הנתונים המוכן. תא ריק בפלט = NULL.

---

## ✅ תרגיל 1 — התוצר הקרטזי

</div>

```sql
-- a   12 x 9 = 108
SELECT COUNT(*) FROM person, adoption;

-- b   9 -- one per adoption
SELECT COUNT(*)
FROM   person p
JOIN   adoption ad ON ad.adopter_id = p.person_id;
```

<div dir="rtl">

**ג.** אין תנאי חיבור — רק סינון. 9 חיות זמינות × 4 מינים = **36**. כל חיה מופיעה עם **כל** מין. התיקון:

</div>

```sql
SELECT a.name, s.name
FROM   animal a
JOIN   species s ON s.species_id = a.species_id
WHERE  a.status = 'available';      -- 9 rows
```

<div dir="rtl">

---

## ✅ תרגיל 2 — שתי טבלאות

</div>

```sql
-- a
SELECT a.name, s.name AS species
FROM   animal a
JOIN   species s ON s.species_id = a.species_id
WHERE  s.name = 'Cat'
ORDER  BY a.name;
-- Felix, Lily, Mitzi, Nala, Oscar, Simba, Tom

-- b
SELECT a.name, i.intake_date, i.intake_type
FROM   intake i
JOIN   animal a ON a.animal_id = i.animal_id
WHERE  i.intake_type = 'stray'
ORDER  BY i.intake_date
LIMIT  5;
```

```text
name   intake_date  intake_type
-----  -----------  -----------
Luna   2023-03-14   stray
Rocky  2023-05-20   stray
Mitzi  2023-06-11   stray
Tom    2023-08-19   stray
Max    2023-11-05   stray
```

```sql
-- c
SELECT e.expense_date, e.amount, e.description
FROM   expense e
JOIN   animal a ON a.animal_id = e.animal_id
WHERE  a.name = 'Max';
```

```text
expense_date  amount  description
------------  ------  ------------------
2024-01-12    420.0   x-ray + medication
2024-08-22    2100.0  leg surgery
```

```sql
-- d   old style -- same 7 rows
SELECT a.name, s.name AS species
FROM   animal a, species s
WHERE  s.species_id = a.species_id
  AND  s.name = 'Cat'
ORDER  BY a.name;
```

<div dir="rtl">

> 💡 **למה בסעיף א' חיפשנו `s.name = 'Cat'` ולא `species_id = 2`?** כי `2` הוא מספר פנימי שאיש לא אמור לזכור. בשאילתה שאנשים קוראים — מחפשים לפי מה שהם מבינים.

---

## ✅ תרגיל 3 — שלוש טבלאות ויותר

</div>

```sql
-- a
SELECT a.name, i.intake_date, p.first_name || ' ' || p.last_name AS brought_by
FROM   intake i
JOIN   animal a ON a.animal_id = i.animal_id
JOIN   person p ON p.person_id = i.brought_by
WHERE  p.first_name = 'Noa'
ORDER  BY i.intake_date;
```

```text
name   intake_date  brought_by
-----  -----------  ----------
Luna   2023-03-14   Noa Peretz
Mitzi  2023-06-11   Noa Peretz
Nala   2024-01-22   Noa Peretz
Lily   2024-07-09   Noa Peretz
Bunny  2025-02-20   Noa Peretz
```

```sql
-- b
SELECT p.first_name || ' ' || p.last_name AS vet, a.name, v.given_date
FROM   vaccination v
JOIN   person p ON p.person_id = v.vet_id
JOIN   animal a ON a.animal_id = v.animal_id
WHERE  p.last_name = 'Nahum'
  AND  v.given_date >= '2024-01-01'
ORDER  BY v.given_date;
```

```text
vet             name     given_date
--------------  -------  ----------
Dr. Maya Nahum  Thumper  2024-02-20
Dr. Maya Nahum  Oscar    2024-04-22
Dr. Maya Nahum  Oscar    2024-04-22     <- two DIFFERENT vaccines on the same day
Dr. Maya Nahum  Daisy    2024-11-06
Dr. Maya Nahum  Felix    2025-01-20
Dr. Maya Nahum  Bunny    2025-02-25
```

<div dir="rtl">

**Oscar פעמיים** — כי ב‑22/04/2024 הוא קיבל **שני** חיסונים (Rabies ו‑FVRCP). שתי שורות ב‑`vaccination`, שתי שורות בתוצאה. **`JOIN` לא מאחד שורות — הוא מוסיף להן עמודות.** אם נוסיף את `vaccine_type` נראה את ההבדל.

</div>

```sql
-- c   four tables
SELECT a.name AS animal, s.name AS species,
       p.first_name || ' ' || p.last_name AS adopter, p.city, ad.fee_paid
FROM   adoption ad
JOIN   animal  a ON a.animal_id  = ad.animal_id
JOIN   species s ON s.species_id = a.species_id
JOIN   person  p ON p.person_id  = ad.adopter_id
WHERE  p.city = 'Haifa'
ORDER  BY ad.adoption_date;
```

```text
animal   species  adopter     city   fee_paid
-------  -------  ----------  -----  --------
Luna     Dog      Dana Cohen  Haifa  300.0
Bella    Dog      Lior Bar    Haifa  200.0
Zoe      Dog      Omer Dayan  Haifa  200.0
Charlie  Dog      Dana Cohen  Haifa  400.0
Kiwi     Parrot   Lior Bar    Haifa  150.0
```

```sql
-- d   species joined TWICE: once for the vaccine, once for the animal
SELECT a.name, vt.name AS vaccine, s.name AS vaccine_for, sa.name AS animal_species
FROM   vaccination  v
JOIN   animal       a  ON a.animal_id        = v.animal_id
JOIN   vaccine_type vt ON vt.vaccine_type_id = v.vaccine_type_id
JOIN   species      s  ON s.species_id       = vt.species_id
JOIN   species      sa ON sa.species_id      = a.species_id
WHERE  vt.species_id <> a.species_id;
-- (no rows) -- every animal got a vaccine meant for its own species. Good.
```

<div dir="rtl">

> 💡 **אותה טבלה פעמיים, עם שני כינויים (`s` ו‑`sa`)** — כי יש שתי שאלות שונות: "לאיזה מין החיסון?" ו"מה המין של החיה?". זה כבר כמעט self join.

---

## ✅ תרגיל 4 — Nonequijoin

</div>

```sql
-- a
SELECT a.name, a.weight_kg, b.band
FROM   animal a
JOIN   size_band b ON a.weight_kg BETWEEN b.min_kg AND b.max_kg
ORDER  BY a.weight_kg;
-- 20 rows: Kiwi, Coco tiny ... Rex large  (same as the CASE in module 20)
```

<div dir="rtl">

**ב.** עם `max_kg = 4` ל‑`small`, נשאר **חור** בין 4 ל‑10 — וחמש חיות נופלות לתוכו:

</div>

```sql
SELECT a.name, a.weight_kg
FROM   animal a
LEFT   JOIN size_band b ON a.weight_kg BETWEEN b.min_kg AND b.max_kg
WHERE  b.band IS NULL;
```

```text
name     weight_kg
-------  ---------
Simba    4.2
Tom      4.8
Felix    5.0
Oscar    5.5
Charlie  7.2
```

<div dir="rtl">

ב‑`JOIN` הרגיל הן פשוט **נעלמות** — 15 שורות במקום 20, בלי שום שגיאה. **התיקון:** טווחים צמודים — כל `min` שווה ל‑`max` של הקודם — ותנאי חצי‑פתוח: `a.weight_kg >= b.min_kg AND a.weight_kg < b.max_kg`. כך אין חורים ואין חפיפות, לכל ערך עשרוני.

> 🔑 **טריק הבדיקה:** `LEFT JOIN … WHERE b.band IS NULL` מוצא בדיוק את מי שנפל בין הכיסאות. הריצו אותו בכל פעם שאתם יוצרים טבלת טווחים.

</div>

```sql
-- c
CREATE TABLE fee_discount (min_age INTEGER, max_age INTEGER, pct INTEGER);
INSERT INTO fee_discount VALUES (0, 7, 0), (8, 30, 50);

SELECT a.name,
       CAST((JULIANDAY('2026-09-21') - JULIANDAY(a.birth_date)) / 365.25 AS INTEGER) AS age,
       d.pct
FROM   animal a
JOIN   fee_discount d
       ON CAST((JULIANDAY('2026-09-21') - JULIANDAY(a.birth_date)) / 365.25 AS INTEGER)
          BETWEEN d.min_age AND d.max_age
WHERE  a.species_id = 1
ORDER  BY age DESC;
```

```text
name     age  pct
-------  ---  ---
Zoe      10   50
Rex      9    50
Bella    8    50
Daisy    6    0
Rocky    6    0
Luna     5    0
Shadow   5    0
Max      4    0
Charlie  2    0
```

<div dir="rtl">

---

## ✅ תרגיל 5 — Outer join

</div>

```sql
-- a   Coco, Nala, Lily, Kiwi
SELECT a.name
FROM   animal a
LEFT   JOIN vaccination v ON v.animal_id = a.animal_id
WHERE  v.vaccination_id IS NULL;

-- b
SELECT a.name, a.status
FROM   animal a
LEFT   JOIN adoption ad ON ad.animal_id = a.animal_id
WHERE  ad.adoption_id IS NULL
ORDER  BY a.name;
```

```text
name    status
------  ----------
Bunny   available
Coco    available
Daisy   deceased
Felix   available
Lily    available
Max     medical
Mitzi   available
Nala    quarantine
Oscar   available
Rex     available
Rocky   available
Shadow  available
```

```sql
-- c   10 animals with no expense rows
SELECT a.name
FROM   animal a
LEFT   JOIN expense e ON e.animal_id = a.animal_id
WHERE  e.expense_id IS NULL
ORDER  BY a.name;
-- Bunny, Charlie, Coco, Kiwi, Lily, Mitzi, Simba, Thumper, Tom, Zoe

-- d
SELECT p.first_name, p.last_name, p.role
FROM   person p
LEFT   JOIN intake i ON i.brought_by = p.person_id
WHERE  i.intake_id IS NULL;
```

```text
first_name  last_name  role
----------  ---------  ---------
Ruti        Almog      volunteer
Dr. Ron     Levi       vet
Dr. Maya    Nahum      vet
```

```sql
-- e
SELECT p.first_name, p.last_name
FROM   person p
LEFT   JOIN adoption ad ON ad.adopter_id = p.person_id
WHERE  p.role = 'adopter'
  AND  ad.adoption_id IS NULL;
-- (no rows)
```

<div dir="rtl">

**אין אף שורה — וזו תשובה נכונה, לא באג.** כל מי שמסומן `adopter` אכן אימץ. זה הגיוני: אדם נרשם כמאמץ **ברגע** האימוץ. **תוצאה ריקה היא מידע** — אל תניחו שהשאילתה שגויה רק כי לא יצא כלום. בדקו בשאילתה הפוכה (`JOIN` רגיל) שהיא מחזירה את כולם.

</div>

```sql
-- f
SELECT e.expense_id, e.description, COALESCE(a.name, 'general') AS animal
FROM   expense e
LEFT   JOIN animal a ON a.animal_id = e.animal_id
ORDER  BY e.expense_id;
```

```text
expense_id  description           animal
----------  --------------------  -------
1           dry food, 20 sacks    general
2           x-ray + medication    Max
3           electricity January   general
4           dental cleaning       Bella
5           cat litter            general
6           electricity February  general
...
```

<div dir="rtl">

---

## ✅ תרגיל 6 — `ON` מול `WHERE`

**א.** A מחזירה **3** שורות; B מחזירה **7**.

</div>

```text
A:                                    B:
name   given_date  cost               name   given_date  cost
-----  ----------  ----               -----  ----------  ----
Simba  2023-04-08  90.0               Simba  2023-04-08  90.0
Tom    2023-08-24  90.0               Mitzi
Oscar  2024-04-22  90.0               Tom    2023-08-24  90.0
                                      Nala
                                      Oscar  2024-04-22  90.0
                                      Lily
                                      Felix
```

<div dir="rtl">

ב‑A חסרים Mitzi, Nala, Lily ו‑Felix.

**ב.** **`ON` קובע מי מתחבר; `WHERE` קובע מי נשאר.** תנאי ב‑`ON` של `LEFT JOIN` רק מגביל אילו חיסונים מוצמדים — החתול נשאר בכל מקרה. תנאי ב‑`WHERE` רץ **אחרי** החיבור: אצל חתול בלי חיסון יקר, `v.cost` הוא NULL, `NULL >= 90` אינו true — והשורה נמחקת. ה‑`LEFT` הפך בפועל ל‑`JOIN` רגיל.

**ג.** **B.** "כל החתולים" — אז אסור שחתול ייעלם.

---

## ✅ תרגיל 7 — Self join

</div>

```sql
-- a
SELECT p1.first_name AS p1, p2.first_name AS p2, p1.last_name
FROM   person p1
JOIN   person p2 ON  p1.last_name = p2.last_name
                 AND p1.person_id < p2.person_id;
```

```text
p1    p2       last_name
----  -------  ---------
Amir  Dr. Ron  Levi
```

```sql
-- b
SELECT a1.name AS older, a2.name AS younger, a1.birth_date, a2.birth_date
FROM   animal a1
JOIN   animal a2 ON  a1.species_id = a2.species_id
                 AND a1.birth_date < a2.birth_date
WHERE  a1.species_id = 3;
```

```text
older    younger  birth_date  birth_date
-------  -------  ----------  ----------
Thumper  Bunny    2023-06-15  2024-01-01
```

<div dir="rtl">

> 💡 כאן `<` על **תאריך הלידה** עושה שתי עבודות: מונע זוג של חיה עם עצמה, **וגם** קובע מי "המבוגר" בכל זוג.

</div>

```sql
-- c
SELECT a.name, v1.given_date AS shot, v2.given_date AS later_shot
FROM   vaccination v1
JOIN   vaccination v2 ON  v1.animal_id       = v2.animal_id
                      AND v1.vaccine_type_id = v2.vaccine_type_id
                      AND v1.given_date      < v2.given_date
JOIN   animal a ON a.animal_id = v1.animal_id
ORDER  BY a.name, v1.given_date;
```

```text
name   shot        later_shot
-----  ----------  ----------
Luna   2023-03-20  2024-06-05
Rocky  2023-05-25  2024-05-28
Rocky  2023-05-25  2025-05-30     <- not the NEXT shot: it skips 2024
Rocky  2024-05-28  2025-05-30
```

<div dir="rtl">

**ד.** התנאי `v1.given_date < v2.given_date` אומר "**כל** חיסון מאוחר יותר", לא "החיסון **הבא**". ל‑Rocky שלושה חיסוני כלבת: 2023, 2024, 2025 — ולכן שלושה זוגות: 2023–2024, 2023–2025, 2024–2025. כדי לקבל רק את הבא צריך "**הקטן** מבין המאוחרים" — `MIN` ותת‑שאילתה, מודול 24.

---

## ✅ תרגיל 8 — היררכיה

</div>

```sql
-- a   see section 8.1 in the module (LEFT JOIN keeps Ruti)

-- b   leaves: nobody reports to them
SELECT s.name, s.job
FROM   staff s
LEFT   JOIN staff c ON c.manager_id = s.staff_id
WHERE  c.staff_id IS NULL;
```

```text
name      job
--------  ---------
Dr. Maya  vet
Amir      volunteer
Tamar     volunteer
```

<div dir="rtl">

> 💡 **שימו לב: זה בדיוק "בלי התאמה" מתרגיל 5** — רק שהטבלה הימנית היא אותה טבלה. `c` = "כפיף אפשרי". אם אין — אין כפיפים.

**ג.** אחרי `INSERT INTO staff VALUES (7, 'Yael', 'kennel volunteer', 5);` — יעל ברמה **4** (רותי 1 ⟵ נועה 2 ⟵ אמיר 3 ⟵ יעל 4). ובסעיף ב', אמיר כבר **לא** עלה — יש לו כפיפה.

</div>

```sql
-- d   walk UP the tree: start from Yael, each step joins to the manager
WITH RECURSIVE chain(staff_id, name, manager_id, step) AS (
  SELECT staff_id, name, manager_id, 0
  FROM   staff WHERE name = 'Yael'
  UNION ALL
  SELECT s.staff_id, s.name, s.manager_id, c.step + 1
  FROM   staff s JOIN chain c ON s.staff_id = c.manager_id     -- reversed direction
)
SELECT step, name FROM chain ORDER BY step;
```

```text
step  name
----  ----
0     Yael
1     Amir
2     Noa
3     Ruti
```

<div dir="rtl">

**ההבדל היחיד מהעץ במודול:** כיוון החיבור. למטה: `s.manager_id = t.staff_id` ("מי שהמנהל שלו בעץ"). למעלה: `s.staff_id = c.manager_id` ("המנהל של מי שכבר בשרשרת"). ב‑Oracle: `START WITH name = 'Yael' CONNECT BY PRIOR manager_id = staff_id`.

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[❓ לשאלות](questions.md)**

</div>

</div>
