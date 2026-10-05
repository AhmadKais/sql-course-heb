<div dir="rtl">

# מודול 22 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 כל הפלטים אמיתיים, מהרצה על בסיס הנתונים המוכן. תא ריק בפלט = NULL.

---

## ✅ תרגיל 1 — CROSS JOIN

</div>

```sql
-- a   4 x 5 = 20
SELECT COUNT(*) FROM species CROSS JOIN vaccine_type;

-- b   2 Haifa volunteers x 4 species = 8
SELECT p.first_name AS volunteer, s.name AS species
FROM   person p
CROSS  JOIN species s
WHERE  p.role = 'volunteer' AND p.city = 'Haifa'
ORDER  BY p.first_name, s.name;
```

```text
volunteer  species
---------  -------
Noa        Cat
Noa        Dog
Noa        Parrot
Noa        Rabbit
Ruti       Cat
Ruti       Dog
Ruti       Parrot
Ruti       Rabbit
```

```sql
-- c   LEFT JOIN -- every species, even without vaccines
SELECT s.name AS species, vt.name AS vaccine
FROM   species s
LEFT   JOIN vaccine_type vt ON vt.species_id = s.species_id
ORDER  BY s.name, vt.name;
```

```text
species  vaccine
-------  -----------
Cat      FVRCP
Cat      Rabies
Dog      DHPP
Dog      Rabies
Parrot                    <- no vaccine defined for parrots
Rabbit   Myxomatosis
```

<div dir="rtl">

---

## ✅ תרגיל 2 — NATURAL ו‑USING

**א.** `adoption NATURAL JOIN animal` ⟵ **9**, `intake NATURAL JOIN animal` ⟵ **21**. שתיהן הגיוניות — כי העמודה המשותפת **היחידה** היא `animal_id`. עבד, **במקרה**.

**ב.** `animal NATURAL JOIN species` ⟵ **0**. יש שתי עמודות משותפות: `species_id` **וגם `name`**. החיבור דורש ש‑`animal.name = species.name` — "Luna" = "Dog"? אף פעם.

</div>

```sql
-- c   USING names only the column we want
SELECT COUNT(*) FROM animal a JOIN species s USING (species_id);    -- 20

-- d
SELECT a.name, ad.adoption_date
FROM   animal a
JOIN   adoption ad USING (animal_id)
WHERE  ad.fee_paid >= 400;
```

```text
name     adoption_date
-------  -------------
Luna     2025-07-01
Charlie  2024-12-01
```

<div dir="rtl">

---

## ✅ תרגיל 3 — לחזות, ואז לספור

| השאילתה | התוצאה |
|----------|---------|
| `JOIN` | **9** — אימוצים שיש להם חיה (כולם) |
| `LEFT JOIN` | **21** |
| `RIGHT JOIN` | **9** |
| `FULL JOIN` | **21** |

**א.** 21 = 8 חיות **שאומצו** (9 אימוצים, כי לונה פעמיים) + 12 חיות **שלא אומצו** (שורה אחת עם NULL לכל אחת). לונה תורמת **שתי** שורות. `LEFT JOIN` לא מבטיח שורה אחת לכל חיה — הוא מבטיח **לפחות** אחת.

**ב.** `RIGHT` = `JOIN` כי **אין אימוץ בלי חיה** — לכל שורה ב‑`adoption` יש התאמה (המפתח הזר `NOT NULL`). לכן גם `FULL` = `LEFT`: אין "רק בצד ימין". **המספרים מספרים על האילוצים.**

---

## ✅ תרגיל 4 — מה חסר?

</div>

```sql
-- a
SELECT a.name, vt.name AS missing
FROM   animal a
JOIN   vaccine_type vt ON vt.species_id = a.species_id
LEFT   JOIN vaccination v ON  v.animal_id       = a.animal_id
                          AND v.vaccine_type_id = vt.vaccine_type_id
WHERE  v.vaccination_id IS NULL
ORDER  BY a.name, vt.name;
```

```text
name   missing
-----  -------
Bella  DHPP
Daisy  DHPP
Felix  FVRCP
Lily   FVRCP
Lily   Rabies
Mitzi  FVRCP
Nala   FVRCP
Nala   Rabies
Zoe    DHPP
```

<div dir="rtl">

**ב.** Bella ו‑Zoe **אומצו**, ו‑Daisy **מתה**. החיסון שלהן כבר לא באחריות המקלט — אז זה לא "חסר" במובן שרותי צריכה. **שאילתה נכונה טכנית יכולה להיות לא נכונה עסקית.** מוסיפים:

</div>

```sql
  AND  a.status NOT IN ('adopted', 'deceased')
-- -> Felix, Lily x2, Mitzi, Nala x2  (6 rows)
```

```sql
-- c
SELECT DISTINCT p.first_name, s.name AS species
FROM   adoption ad
JOIN   person  p ON p.person_id  = ad.adopter_id
JOIN   animal  a ON a.animal_id  = ad.animal_id
JOIN   species s ON s.species_id = a.species_id
ORDER  BY p.first_name;
```

```text
first_name  species
----------  -------
Dana        Dog          <- Dana adopted 2 dogs: DISTINCT shows "Dog" once
Eitan       Dog
Lior        Dog
Lior        Parrot       <- Lior: two species
Omer        Dog
Shira       Cat
Shira       Rabbit       <- Shira: two species
Yossi       Cat
```

<div dir="rtl">

---

## ✅ תרגיל 5 — שרשרת JOIN‑ים

</div>

```sql
-- a   15 rows: 12 people, but Dana, Lior and Shira adopted twice
SELECT p.first_name, p.role, a.name AS adopted
FROM   person p
LEFT   JOIN adoption ad ON ad.adopter_id = p.person_id
LEFT   JOIN animal   a  ON a.animal_id   = ad.animal_id
ORDER  BY p.person_id;
```

```text
first_name  role       adopted
----------  ---------  -------
Ruti        volunteer
Noa         volunteer
Amir        volunteer
Dr. Ron     vet
Dr. Maya    vet
Dana        adopter    Luna
Dana        adopter    Charlie
Yossi       adopter    Simba
Lior        adopter    Bella
Lior        adopter    Kiwi
Shira       adopter    Tom
Shira       adopter    Thumper
Omer        adopter    Zoe
Tamar       volunteer
Eitan       adopter    Luna
```

<div dir="rtl">

**ב.** עם `JOIN animal` רגיל — **9** שורות. כל מי שלא אימץ (6 מתנדבים ווטרינרים) **נעלם**: אצלם `ad.animal_id` הוא NULL, ו‑`a.animal_id = NULL` לעולם אינו true. ה‑`JOIN` "שבר" את ה‑`LEFT` שלפניו.

</div>

```sql
-- c   WRONG: 11 rows -- the general expenses vanish at the species JOIN
SELECT e.description, a.name, s.name AS species
FROM   expense e
LEFT   JOIN animal  a ON a.animal_id  = e.animal_id
JOIN   species      s ON s.species_id = a.species_id;

-- c   RIGHT: 22 rows
SELECT e.description, a.name, s.name AS species
FROM   expense e
LEFT   JOIN animal  a ON a.animal_id  = e.animal_id
LEFT   JOIN species s ON s.species_id = a.species_id;
```

```sql
-- d   21 rows
SELECT a.name, s.name AS species, p.first_name AS brought_by, p.city
FROM   intake  i
JOIN   animal  a ON a.animal_id  = i.animal_id      -- JOIN: every intake HAS an animal (NOT NULL)
JOIN   species s ON s.species_id = a.species_id     -- JOIN: every animal HAS a species (NOT NULL)
LEFT   JOIN person p ON p.person_id = i.brought_by  -- LEFT: transfers have no person
ORDER  BY i.intake_id;
```

```text
name   species  brought_by  city
-----  -------  ----------  ----------
Luna   Dog      Noa         Haifa
Simba  Cat      Yossi       Tel Aviv
Rocky  Dog      Amir        Kiryat Ata
Mitzi  Cat      Noa         Haifa
...
```

<div dir="rtl">

> 💡 **כאן ה‑`JOIN` ל‑`species` בא *לפני* ה‑`LEFT` ולא תלוי בו** — אז אין שבירה. מה שקובע הוא **על מה** תנאי ה‑`ON` נשען: `s` נשען על `a`, ו‑`a` מגיע מ‑`JOIN` רגיל.

---

## ✅ תרגיל 6 — FULL OUTER JOIN

</div>

```sql
-- a   21 rows: 11 general expenses + 10 animals without expenses
SELECT a.name AS animal, e.expense_id, e.description
FROM   animal a
FULL   OUTER JOIN expense e ON e.animal_id = a.animal_id
WHERE  a.animal_id IS NULL OR e.expense_id IS NULL;

-- b
SELECT COALESCE(j.volunteer, f.volunteer) AS volunteer,
       CASE WHEN f.volunteer IS NULL THEN 'january only'
            WHEN j.volunteer IS NULL THEN 'february only'
            ELSE 'both' END AS status
FROM   shift_jan j
FULL   OUTER JOIN shift_feb f ON f.volunteer = j.volunteer
ORDER  BY volunteer;
```

```text
volunteer  status
---------  -------------
Amir       both
Noa        both
Ruti       january only
Tamar      february only
```

<div dir="rtl">

> 🔑 **`COALESCE(j.volunteer, f.volunteer)`** — כי בשורה של Ruti, `f.volunteer` הוא NULL, ובשורה של Tamar — `j.volunteer`. השם נמצא תמיד **באחד** מהצדדים. זה הדפוס הקבוע של `FULL JOIN`: `COALESCE` על המפתח, `CASE` על המקור.

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[❓ לשאלות](questions.md)**

</div>

</div>
