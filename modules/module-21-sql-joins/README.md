<div dir="rtl">

# מודול 21 — SQL: איחוד טבלאות (JOIN)

> **פרק 21 בתכנית הלימודים** · 4 שעות עיוני + 3 שעות מעשי
> **נושאים:** תוצרים קרטזיים ופעולות איחוד (Join) · Nonequijoins · Outer Joins · Self Joins ושליפות היררכיות

> 🧭 **במסלול המשולב:** יחידה 5, לצד [מודול 5 — יחסים](../module-05-relationships/). **`JOIN` הוא היחס** — מנקודת המבט של השאילתה.

---

## 🎯 מה תדעו בסוף המודול

- [ ] להסביר למה צריך `JOIN` — ומה הקשר שלו למפתח זר
- [ ] להסביר מהו **תוצר קרטזי**, ולזהות אותו כשהוא קורה בטעות
- [ ] לכתוב **equijoin** בין שתיים, שלוש וארבע טבלאות
- [ ] לכתוב **nonequijoin** — חיבור לפי טווח, לא לפי שוויון
- [ ] לכתוב **outer join** — ולמצוא שורות **בלי** התאמה
- [ ] לכתוב **self join** — טבלה שמתחברת לעצמה
- [ ] לשלוף **היררכיה** (מי מנהל את מי) — ב‑SQLite וב‑Oracle

---

## 🗺️ מפת המודול

| # | הסעיף |
|---|--------|
| 1 | [למה צריך JOIN](#1-למה-צריך-join) |
| 2 | [התוצר הקרטזי](#2-התוצר-הקרטזי) |
| 3 | [Equijoin — חיבור לפי שוויון](#3-equijoin--חיבור-לפי-שוויון) |
| 4 | [שלוש טבלאות ויותר](#4-שלוש-טבלאות-ויותר) |
| 5 | [Nonequijoin — חיבור לפי טווח](#5-nonequijoin--חיבור-לפי-טווח) |
| 6 | [Outer join — גם מה שאין לו זוג](#6-outer-join--גם-מה-שאין-לו-זוג) |
| 7 | [Self join — טבלה מול עצמה](#7-self-join--טבלה-מול-עצמה) |
| 8 | [שליפות היררכיות](#8-שליפות-היררכיות) |
| 9 | [SQLite מול Oracle](#9-sqlite-מול-oracle) |
| 10 | [חמש טעויות נפוצות](#10-חמש-טעויות-נפוצות) |
| 11 | [סיכום המודול](#11-סיכום-המודול) |

---

## 1. למה צריך JOIN

במודול 6 (נרמול) פירקנו את המידע לטבלאות, כדי שכל עובדה תישמר **פעם אחת**. שם המין "Dog" שמור רק ב‑`species`; בטבלת `animal` יש רק `species_id = 1`.

**התוצאה:** כל טבלה לבד היא חצי תמונה.

</div>

```text
   animal                                  species
   +----+-------+------------+             +------------+--------+--------------+
   | id | name  | species_id |             | species_id | name   | adoption_fee |
   +----+-------+------------+             +------------+--------+--------------+
   |  1 | Luna  |     1  ----+------------>|      1     | Dog    |    400       |
   |  2 | Simba |     2  ----+------------>|      2     | Cat    |    250       |
   |  3 | Rocky |     1  ----+--+          |      3     | Rabbit |    100       |
   +----+-------+------------+  +--------->|      1  (same row as Luna's)      |
                                           +------------+--------+--------------+

   The FOREIGN KEY (animal.species_id) points to the PRIMARY KEY (species.species_id).
   JOIN follows that arrow and glues the two rows into one result row.
```

<div dir="rtl">

> 🔑 **הקשר למודול 5:** כל קו "1 ל‑רבים" ב‑ERD הפך במעבר לטבלאות למפתח זר. **`JOIN` הולך על הקו הזה בחזרה.** מי שמבין את ה‑ERD — יודע אילו `JOIN`‑ים אפשריים.

---

## 2. התוצר הקרטזי

מה קורה אם מבקשים שתי טבלאות **בלי** לומר איך לחבר אותן?

</div>

```sql
SELECT a.name, s.name AS species
FROM   animal a, species s
WHERE  a.animal_id <= 2
ORDER  BY a.name, s.name;
```

```text
name   species
-----  -------
Luna   Cat        <- Luna is NOT a cat
Luna   Dog
Luna   Parrot
Luna   Rabbit
Simba  Cat
Simba  Dog
Simba  Parrot
Simba  Rabbit
```

<div dir="rtl">

**כל** שורה מ‑`animal` חוברה עם **כל** שורה מ‑`species`. זה **תוצר קרטזי** (Cartesian product): 20 חיות × 4 מינים = **80 שורות**, ורובן שקר.

</div>

```sql
SELECT COUNT(*) FROM animal, species;    -- 80
```

<div dir="rtl">

> ⚠️ **התוצר הקרטזי הוא כמעט תמיד טעות** — שכחתם את תנאי החיבור. על 20 × 4 זה רק מבלבל. על 1,000,000 לקוחות × 50,000 הזמנות — זה 50 מיליארד שורות, ושרת שנתקע. **הסימן:** הרבה יותר שורות ממה שציפיתם.

> 💡 **מתי תוצר קרטזי כן שימושי?** כשרוצים בכוונה את **כל הצירופים** — למשל כל חיה × כל סוג חיסון, כדי לבדוק מה חסר. במודול 22 נכיר את התחביר המפורש לזה: `CROSS JOIN`.

---

## 3. Equijoin — חיבור לפי שוויון

מוסיפים **תנאי חיבור**: רק זוגות שבהם המפתח הזר שווה למפתח הראשי.

</div>

```sql
SELECT a.name, s.name AS species, s.adoption_fee
FROM   animal a
JOIN   species s ON s.species_id = a.species_id
WHERE  a.status = 'available'
ORDER  BY a.name;
```

```text
name    species  adoption_fee
------  -------  ------------
Bunny   Rabbit   100.0
Coco    Parrot   150.0
Felix   Cat      250.0
Lily    Cat      250.0
Mitzi   Cat      250.0
Oscar   Cat      250.0
Rex     Dog      400.0
Rocky   Dog      400.0
Shadow  Dog      400.0
```

<div dir="rtl">

**ארבעה חלקים, ארבעה תפקידים:**

| החלק | התפקיד |
|------|--------|
| `FROM animal a` | הטבלה הראשונה, עם **כינוי** (alias) קצר `a` |
| `JOIN species s` | הטבלה השנייה, עם כינוי `s` |
| `ON s.species_id = a.species_id` | **תנאי החיבור** — מפתח ראשי = מפתח זר |
| `WHERE a.status = 'available'` | **סינון** — כמו תמיד, אחרי החיבור |

### 3.1 כינויים ושמות מלאים

בשתי הטבלאות יש עמודה בשם `name`. אם נכתוב רק `name` — SQL לא יודע לאיזו הכוונה:

</div>

```text
   SELECT name FROM animal a JOIN species s ON ...
   -->  Error: ambiguous column name: name
```

<div dir="rtl">

**הפתרון:** `a.name` ו‑`s.name`. **הרגל טוב:** לכתוב כינוי לפני **כל** עמודה בשאילתה עם `JOIN` — גם כשאין התנגשות. מי שיקרא את הקוד יידע מאיפה כל עמודה מגיעה.

### 3.2 התחביר הישן — `WHERE`

יש דרך ישנה לכתוב בדיוק אותו דבר — וחשוב להכיר אותה, כי היא מופיעה בהרבה קוד קיים ובחומרי Oracle:

</div>

```sql
-- old style (comma + WHERE)                 -- ANSI style (JOIN ... ON)
SELECT a.name, s.name                        SELECT a.name, s.name
FROM   animal a, species s                   FROM   animal a
WHERE  s.species_id = a.species_id           JOIN   species s ON s.species_id = a.species_id
  AND  a.status = 'available';               WHERE  a.status = 'available';
```

<div dir="rtl">

התוצאה **זהה**. אבל בתחביר הישן תנאי החיבור ותנאי הסינון מעורבבים ב‑`WHERE` — ומספיק לשכוח שורה אחת כדי לקבל תוצר קרטזי. **בקוד חדש — תמיד `JOIN … ON`.**

---

## 4. שלוש טבלאות ויותר

טבלת `adoption` היא **טבלת קישור** (מודול 5 — פתרון יחס רבים‑לרבים): בכל שורה יש `animal_id` **וגם** `adopter_id`. כדי לראות שמות — צריך את שתי הטבלאות שמסביב:

</div>

```text
   animal  <----  adoption  ---->  person
   (name)        (animal_id,       (first_name,
                  adopter_id)       last_name)
```

```sql
SELECT a.name                               AS animal,
       p.first_name || ' ' || p.last_name   AS adopter,
       ad.adoption_date,
       ad.fee_paid
FROM   adoption ad
JOIN   animal a ON a.animal_id = ad.animal_id
JOIN   person p ON p.person_id = ad.adopter_id
ORDER  BY ad.adoption_date;
```

```text
animal   adopter        adoption_date  fee_paid
-------  -------------  -------------  --------
Luna     Dana Cohen     2023-05-10     300.0
Simba    Yossi Mizrahi  2023-06-15     200.0
Bella    Lior Bar       2024-02-10     200.0
Tom      Shira Katz     2024-05-05     250.0
Thumper  Shira Katz     2024-06-20     100.0
Zoe      Omer Dayan     2024-08-15     200.0
Charlie  Dana Cohen     2024-12-01     400.0
Kiwi     Lior Bar       2025-01-10     150.0
Luna     Eitan Shalev   2025-07-01     400.0     <- Luna, adopted twice
```

<div dir="rtl">

> 🔑 **הכלל:** כדי לחבר **N** טבלאות צריך לפחות **N − 1** תנאי חיבור. שלוש טבלאות — שני `ON`. פחות מזה — מישהו מתחבר לכולם (תוצר קרטזי חלקי).

### 4.1 ארבע טבלאות

כל החיסונים של Rocky — עם שם החיסון **ושם הווטרינר**:

</div>

```sql
SELECT a.name, v.given_date, vt.name AS vaccine, p.last_name AS vet
FROM   vaccination  v
JOIN   animal       a  ON a.animal_id        = v.animal_id
JOIN   vaccine_type vt ON vt.vaccine_type_id = v.vaccine_type_id
JOIN   person       p  ON p.person_id        = v.vet_id
WHERE  a.name = 'Rocky'
ORDER  BY v.given_date;
```

```text
name   given_date  vaccine  vet
-----  ----------  -------  ----
Rocky  2023-05-25  Rabies   Levi
Rocky  2023-05-25  DHPP     Levi
Rocky  2024-05-28  Rabies   Levi
Rocky  2025-05-30  Rabies   Levi     <- three rabies shots, one per year
```

<div dir="rtl">

> 💡 **שימו לב: `person` מופיעה בבסיס הנתונים בשלושה תפקידים** — מאמץ (`adoption.adopter_id`), וטרינר (`vaccination.vet_id`) ומי שהביא חיה (`intake.brought_by`). אותה טבלה, שלושה מפתחות זרים שונים. **תנאי ה‑`ON` קובע איזה תפקיד שואלים.**

---

## 5. Nonequijoin — חיבור לפי טווח

עד עכשיו כל חיבור היה `=`. אבל תנאי החיבור יכול להיות **כל תנאי** — למשל, ערך שנופל **בתוך טווח**.

נניח שלמקלט יש טבלת "קטגוריות גודל" (בבסיס הנתונים המוכן אין אותה — צרו אותה, זה שלוש שורות):

</div>

```sql
CREATE TABLE size_band (band TEXT, min_kg REAL, max_kg REAL);
INSERT INTO size_band VALUES ('tiny', 0, 0.99), ('small', 1, 9.99),
                             ('medium', 10, 24.99), ('large', 25, 99);

SELECT a.name, a.weight_kg, b.band
FROM   animal a
JOIN   size_band b ON a.weight_kg BETWEEN b.min_kg AND b.max_kg
WHERE  a.species_id = 1
ORDER  BY a.weight_kg;
```

```text
name     weight_kg  band
-------  ---------  ------
Charlie  7.2        small
Max      12.3       medium
Daisy    15.6       medium
Luna     18.5       medium
Zoe      22.0       medium
Shadow   25.1       large
Bella    28.4       large
Rocky    31.0       large
Rex      38.7       large
```

<div dir="rtl">

**אין שום מפתח זר בין `animal` ל‑`size_band`.** החיבור הוא לפי **ערך בתוך טווח** — `BETWEEN`. זה **nonequijoin** (חיבור שאינו שוויון).

> 💡 **"אבל עשינו את זה ב‑`CASE` במודול 20!"** נכון. ההבדל: עם טבלה, מי שמנהל את המקלט יכול לשנות את הגבולות **בלי לגעת בקוד** — רק לעדכן שורה. הטווחים הם **נתונים**, לא קוד. זה גם הדפוס של מדרגות מס, דרגות שכר והנחות כמות.

> ⚠️ **טווחים חייבים לא לחפוף ולא להשאיר חורים.** אם יש חיה של 9.995 ק"ג — היא בין `9.99` ל‑`10`, ולא תופיע בכלל. בטבלה אמיתית מגדירים `min_kg <= w AND w < max_kg` עם גבולות צמודים (`10`, `25`).

---

## 6. Outer join — גם מה שאין לו זוג

### 6.1 הבעיה: `JOIN` מעלים שורות

</div>

```sql
SELECT COUNT(*) FROM animal a JOIN vaccination v ON v.animal_id = a.animal_id;   -- 28
SELECT COUNT(*) FROM animal;                                                     -- 20
```

<div dir="rtl">

28 שורות — אבל **כמה חיות** מופיעות? רק אלה שקיבלו לפחות חיסון אחד. חיה **בלי** חיסונים — אין לה שורה תואמת ב‑`vaccination`, ולכן `JOIN` **מעלים אותה**. בשקט.

`JOIN` רגיל נקרא **inner join**: מחזיר רק זוגות שנמצאו בשני הצדדים.

### 6.2 הפתרון: `LEFT JOIN`

`LEFT JOIN` מחזיר **כל** שורה מהטבלה השמאלית (הראשונה). אם אין לה זוג — עמודות הטבלה הימנית יהיו NULL:

</div>

```text
   animal a  LEFT JOIN  vaccination v

   +--------+       +-------------+          result
   | Luna   |------>| vacc 1, 2   |   -->    Luna   vacc 1
   | Rocky  |------>| vacc 5, 6.. |   -->    Luna   vacc 2
   | Coco   |       (nothing)       -->    ...
   +--------+                        -->    Coco   NULL   <- kept, with NULLs
```

```sql
-- animals that were NEVER vaccinated
SELECT a.name, v.vaccination_id
FROM   animal a
LEFT   JOIN vaccination v ON v.animal_id = a.animal_id
WHERE  v.vaccination_id IS NULL;
```

```text
name  vaccination_id
----  --------------
Coco
Nala
Lily
Kiwi
```

<div dir="rtl">

> 🔑 **הדפוס הכי שימושי במודול: `LEFT JOIN … WHERE <right>.id IS NULL`** = "שורות **בלי** התאמה". חיות שלא חוסנו, לקוחות שלא הזמינו, מוצרים שלא נמכרו. **שימו לב:** בודקים NULL על **המפתח הראשי** של הטבלה הימנית — עמודה שלעולם אינה NULL בשורה אמיתית.

### 6.3 ההוצאה הכללית — `LEFT JOIN` מהצד השני

ב‑`expense`, `animal_id` הוא NULL בהוצאות כלליות (מזון, חשמל). `JOIN` רגיל יעלים את כולן:

</div>

```sql
SELECT e.expense_id, e.amount, e.description, a.name
FROM   expense e
LEFT   JOIN animal a ON a.animal_id = e.animal_id
WHERE  e.expense_id <= 6;
```

```text
expense_id  amount  description           name
----------  ------  --------------------  -----
1           1850.0  dry food, 20 sacks              <- general: kept, name is NULL
2           420.0   x-ray + medication    Max
3           960.0   electricity January
4           650.0   dental cleaning       Bella
5           310.0   cat litter
6           880.0   electricity February
```

<div dir="rtl">

> ⚠️ **סדר הטבלאות קובע.** `LEFT JOIN` שומר את **השמאלית**. `expense LEFT JOIN animal` — כל ההוצאות. `animal LEFT JOIN expense` — כל החיות. שאלה אחרת, תשובה אחרת.

### 6.4 `RIGHT` ו‑`FULL`

| הסוג | שומר | הערה |
|------|-------|-------|
| `LEFT JOIN` | כל השורות מ**שמאל** | הנפוץ ביותר |
| `RIGHT JOIN` | כל השורות מ**ימין** | שקול ל‑`LEFT` עם החלפת סדר. נדיר בקוד |
| `FULL OUTER JOIN` | כל השורות **משני** הצדדים | שימושי להשוואת שתי רשימות |

> 💡 `RIGHT` ו‑`FULL` נתמכים ב‑SQLite רק מגרסה 3.39 (2022). (ב‑OneCompiler יש SQLite 3.45, אז הם עובדים.) אם בכלי אחר מתקבלת שגיאה, החליפו את סדר הטבלאות וכתבו `LEFT`. במודול 22 נרחיב על ההבדלים.

### 6.5 ב‑Oracle: הסימן `(+)`

בקוד Oracle ישן תראו outer join בתחביר ה‑`WHERE`, עם `(+)` **בצד שעלול להיות חסר**:

</div>

```sql
-- Oracle, old style: every expense, with the animal if there is one
SELECT e.description, a.name
FROM   expense e, animal a
WHERE  e.animal_id = a.animal_id(+);      -- (+) on the side that may be missing

-- same thing, ANSI style (works everywhere, including Oracle)
SELECT e.description, a.name
FROM   expense e
LEFT   JOIN animal a ON a.animal_id = e.animal_id;
```

<div dir="rtl">

> 🔑 **קראו `(+)` — כתבו `LEFT JOIN`.** הוא מופיע בחומרי לימוד ישנים ובמבחנים, אז צריך לזהות אותו. אבל הוא עובד רק ב‑Oracle, ומבלבל.

---

## 7. Self join — טבלה מול עצמה

לפעמים השאלה היא על **שתי שורות מאותה טבלה**: שתי חיות מאותו גזע, שתי קליטות של אותה חיה. מחברים את הטבלה **לעצמה** — עם שני כינויים שונים, כאילו היו שתי טבלאות.

### 7.1 זוגות מאותו גזע

</div>

```sql
SELECT a1.name AS animal_1, a2.name AS animal_2, a1.breed
FROM   animal a1
JOIN   animal a2 ON  a1.breed = a2.breed
                 AND a1.animal_id < a2.animal_id
ORDER  BY a1.breed;
```

```text
animal_1  animal_2  breed
--------  --------  -----
Luna      Daisy     Mixed
Luna      Zoe       Mixed
Zoe       Daisy     Mixed
Simba     Felix     Tabby
```

<div dir="rtl">

**למה `a1.animal_id < a2.animal_id`?** בלי התנאי הזה כל חיה מתחברת **לעצמה** (Luna–Luna), וכל זוג מופיע **פעמיים** (Luna–Daisy וגם Daisy–Luna). `<` משאיר כל זוג פעם אחת בדיוק.

### 7.2 לונה חזרה

לונה נקלטה פעמיים. self join על `intake` מוצא את הקליטה הראשונה ואת החזרה **באותה שורה**:

</div>

```sql
SELECT a.name, i1.intake_date AS first_in, i2.intake_date AS back_in
FROM   intake i1
JOIN   intake i2 ON  i1.animal_id   = i2.animal_id
                 AND i1.intake_date < i2.intake_date
JOIN   animal a  ON  a.animal_id    = i1.animal_id;
```

```text
name  first_in    back_in
----  ----------  ----------
Luna  2023-03-14  2024-06-01
```

<div dir="rtl">

> 💡 **שימו לב: גם זה חיבור שמשלב `=` ו‑`<`** — equijoin על החיה, nonequijoin על התאריך. תנאי ה‑`ON` יכול להיות מורכב כמו כל `WHERE`.

---

## 8. שליפות היררכיות

**היררכיה** היא יחס רקורסיבי (מודול 7): עובד שיש לו מנהל, שהוא בעצמו עובד עם מנהל. בטבלה זה מפתח זר **לאותה טבלה**:

</div>

```sql
CREATE TABLE staff (
  staff_id   INTEGER PRIMARY KEY,
  name       TEXT,
  job        TEXT,
  manager_id INTEGER REFERENCES staff(staff_id)   -- points to the SAME table
);
INSERT INTO staff VALUES (1, 'Ruti',     'shelter manager',       NULL),
                         (2, 'Dr. Ron',  'head vet',              1),
                         (3, 'Noa',      'volunteer coordinator', 1),
                         (4, 'Dr. Maya', 'vet',                   2),
                         (5, 'Amir',     'volunteer',             3),
                         (6, 'Tamar',    'volunteer',             3);
```

<div dir="rtl">

### 8.1 רמה אחת: כל עובד ומנהלו — self join

</div>

```sql
SELECT s.name AS employee, s.job, m.name AS manager
FROM   staff s
LEFT   JOIN staff m ON m.staff_id = s.manager_id
ORDER  BY s.staff_id;
```

```text
employee  job                    manager
--------  ---------------------  -------
Ruti      shelter manager                  <- LEFT JOIN keeps the boss (no manager)
Dr. Ron   head vet               Ruti
Noa       volunteer coordinator  Ruti
Dr. Maya  vet                    Dr. Ron
Amir      volunteer              Noa
Tamar     volunteer              Noa
```

<div dir="rtl">

### 8.2 כל הרמות: העץ המלא

self join נותן רמה **אחת**. בשביל כל העץ — מנהל, מנהל של מנהל, וכן הלאה — צריך שאילתה **רקורסיבית**:

</div>

```sql
WITH RECURSIVE tree(staff_id, name, job, level) AS (
  SELECT staff_id, name, job, 1                      -- start: the top (no manager)
  FROM   staff WHERE manager_id IS NULL
  UNION ALL
  SELECT s.staff_id, s.name, s.job, t.level + 1      -- step: everyone whose manager
  FROM   staff s JOIN tree t ON s.manager_id = t.staff_id   -- is already in the tree
)
SELECT SUBSTR('            ', 1, (level - 1) * 4) || name AS org_chart, job, level
FROM   tree
ORDER  BY level, staff_id;
```

```text
org_chart         job                    level
----------------  ---------------------  -----
Ruti              shelter manager        1
    Dr. Ron       head vet               2
    Noa           volunteer coordinator  2
        Dr. Maya  vet                    3
        Amir      volunteer              3
        Tamar     volunteer              3
```

<div dir="rtl">

**איך קוראים את זה:** החלק הראשון מוצא את **השורש** (רותי). החלק השני מוסיף שוב ושוב את מי שהמנהל שלו **כבר בעץ** — עד שאין יותר מה להוסיף. `level` סופר את העומק.

### 8.3 ב‑Oracle: `CONNECT BY`

ל‑Oracle יש תחביר ייעודי — ותכנית הלימודים מבוססת עליו:

</div>

```sql
-- Oracle
SELECT LPAD(' ', (LEVEL - 1) * 4) || name AS org_chart, job, LEVEL
FROM   staff
START  WITH manager_id IS NULL             -- the root
CONNECT BY PRIOR staff_id = manager_id;     -- parent's id = child's manager_id
```

<div dir="rtl">

| | SQLite / סטנדרט | Oracle |
|---|---|---|
| התחביר | `WITH RECURSIVE … UNION ALL` | `START WITH … CONNECT BY PRIOR` |
| מספר הרמה | עמודה שסופרים לבד (`level + 1`) | `LEVEL` מובנה |
| הזחה | `SUBSTR('    ', …)` | `LPAD(' ', …)` |

> 💡 Oracle תומך **גם** ב‑`WITH RECURSIVE` (בלי המילה `RECURSIVE`). `CONNECT BY` קצר יותר, אבל עובד רק ב‑Oracle.

---

## 9. SQLite מול Oracle

</div>

```text
+--------------------------+--------------------------------+--------------------------------+
| WHAT                     | ANSI (SQLite, Oracle, all)     | Oracle old style               |
+--------------------------+--------------------------------+--------------------------------+
| inner join               | a JOIN b ON a.x = b.x          | FROM a, b WHERE a.x = b.x      |
| left outer join          | a LEFT JOIN b ON a.x = b.x     | WHERE a.x = b.x(+)             |
| right outer join         | a RIGHT JOIN b ON ...  (*)     | WHERE a.x(+) = b.x             |
| full outer join          | a FULL JOIN b ON ...   (*)     | (not possible with (+))        |
| nonequijoin              | JOIN b ON a.v BETWEEN b.lo     | WHERE a.v BETWEEN b.lo         |
|                          |                AND b.hi        |                 AND b.hi       |
| hierarchy                | WITH RECURSIVE ...             | START WITH ... CONNECT BY      |
+--------------------------+--------------------------------+--------------------------------+
   (*) SQLite 3.39+ only
```

<div dir="rtl">

---

## 10. חמש טעויות נפוצות

| # | הטעות | מה קורה | התיקון |
|---|-------|----------|---------|
| 1 | **שוכחים את תנאי החיבור** | תוצר קרטזי: 80 שורות במקום 20 | `N` טבלאות ⟵ `N − 1` תנאי `ON` |
| 2 | **`name` בלי כינוי** | `ambiguous column name` | `a.name`, `s.name` |
| 3 | **`JOIN` כשצריך `LEFT JOIN`** | שורות בלי התאמה נעלמות בשקט | שאלו: "האם כל השורות צריכות להופיע?" |
| 4 | **סינון בעמודה של הטבלה הימנית אחרי `LEFT JOIN`** | `WHERE v.cost > 80` מעלים את השורות עם NULL — וה‑`LEFT` הופך ל‑`JOIN` | שימו את התנאי ב‑`ON`, או בדקו `IS NULL` במפורש |
| 5 | **self join בלי `<`** | כל שורה עם עצמה, וכל זוג פעמיים | `a1.id < a2.id` |

---

## 11. סיכום המודול

<div align="center">

### 🧠 שבע נקודות

</div>

1. **`JOIN` הולך על המפתח הזר בחזרה** — מה שהנרמול הפריד, `JOIN` מחבר לשאילתה אחת.
2. **בלי תנאי חיבור — תוצר קרטזי:** כל שורה עם כל שורה. כמעט תמיד באג.
3. **Equijoin:** `JOIN t ON t.pk = x.fk`. ל‑N טבלאות — N − 1 תנאים. כינוי לפני כל עמודה.
4. **Nonequijoin:** תנאי החיבור הוא טווח (`BETWEEN`) — טבלאות מדרגות במקום `CASE`.
5. **`LEFT JOIN`** שומר את כל השמאלית. **`LEFT JOIN … WHERE right.id IS NULL`** = "בלי התאמה".
6. **Self join:** אותה טבלה בשני כינויים. `<` כדי לא לחבר שורה לעצמה ולא לכפול זוגות.
7. **היררכיה:** self join לרמה אחת; `WITH RECURSIVE` (או `CONNECT BY` ב‑Oracle) לעץ כולו.

<div align="center">

---

*"הנרמול מפרק את העולם לטבלאות.*
*JOIN מרכיב אותו בחזרה — בדיוק כפי שצריך לשאלה."*

---

</div>

## 📎 המשך

| | |
|---|---|
| ❓ | [שאלות ותשובות](questions.md) |
| ✏️ | [תרגילים](exercises.md) — על [בסיס הנתונים המוכן](../../resources/shelter-db/) |
| ✅ | [פתרונות](solutions.md) — עם הפלט האמיתי |
| ⬅️ | [מודול 20 — SQL: פונקציות 2](../module-20-sql-functions-2/) |
| ➡️ | [מודול 22 — SQL: איחוד טבלאות 2](../module-22-sql-joins-2/) |
| 🏠 | [חזרה לדף הקורס](../../) |

</div>
