<div dir="rtl">

# מודול 24 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 כל הפלטים אמיתיים, מהרצה על בסיס הנתונים המוכן. סדר השורות בלי `ORDER BY` עלול להיות שונה אצלכם.

---

## ✅ תרגיל 1 — GROUP BY

</div>

```sql
-- a   adopter 6, vet 2, volunteer 4
SELECT role, COUNT(*) FROM person GROUP BY role;

-- b
SELECT city, COUNT(*) AS people
FROM   person
GROUP  BY city
ORDER  BY people DESC, city;
-- Haifa 6, then six cities with 1 each

-- c
SELECT species_id, COUNT(*) AS n, ROUND(AVG(weight_kg), 1) AS avg_kg, MAX(weight_kg) AS heaviest
FROM   animal
GROUP  BY species_id;
```

```text
species_id  n  avg_kg  heaviest
----------  -  ------  --------
1           9  22.1    38.7
2           7  4.1     5.5
3           2  1.6     1.8
4           2  0.1     0.1
```

```sql
-- d
SELECT STRFTIME('%Y', adoption_date) AS year, COUNT(*) AS adoptions, SUM(fee_paid) AS income
FROM   adoption
GROUP  BY year;
```

```text
year  adoptions  income
----  ---------  ------
2023  2          500.0
2024  5          1150.0
2025  2          550.0
```

```sql
-- e   stray 11, surrender 8, transfer 2
SELECT intake_type, COUNT(*) FROM intake GROUP BY intake_type;
```

<div dir="rtl">

> 💡 **השוו לתרגיל 5ב ו‑5ה במודול 23:** אותם מספרים — אבל שם כל ערך היה עמודה (צריך לדעת אותם מראש), וכאן כל ערך הוא שורה (נמצא לבד).

---

## ✅ תרגיל 2 — GROUP BY עם JOIN

</div>

```sql
-- a   Levi 17, Nahum 11
SELECT p.last_name AS vet, COUNT(*) AS shots
FROM   vaccination v
JOIN   person p ON p.person_id = v.vet_id
GROUP  BY p.person_id;

-- b
SELECT vt.name, COUNT(*) AS shots, SUM(v.cost) AS cost
FROM   vaccination v
JOIN   vaccine_type vt ON vt.vaccine_type_id = v.vaccine_type_id
GROUP  BY vt.vaccine_type_id
ORDER  BY shots DESC;
```

```text
name         shots  cost
-----------  -----  -----
Rabies       12     990.0      <- rabies for DOGS (type 1)
DHPP         6      580.0
Rabies       5      405.0      <- rabies for CATS (type 3)
FVRCP        3      270.0
Myxomatosis  2      125.0
```

```sql
-- c   GROUP BY vt.name -- 4 rows
SELECT vt.name, COUNT(*) AS shots
FROM   vaccination v
JOIN   vaccine_type vt ON vt.vaccine_type_id = v.vaccine_type_id
GROUP  BY vt.name;
```

```text
name         shots
-----------  -----
DHPP         6
FVRCP        3
Myxomatosis  2
Rabies       17      <- 12 + 5: two different vaccines merged into one group
```

<div dir="rtl">

**4 שורות במקום 5.** בטבלת `vaccine_type` יש **שני** חיסונים בשם "Rabies" — אחד לכלבים ואחד לחתולים. אלה מוצרים שונים (מינון, מחיר), אבל `GROUP BY vt.name` מאחד אותם. **מקבצים לפי מזהה, מציגים לפי שם.**

</div>

```sql
-- d   every species, even with no adoptions
SELECT s.name, COUNT(ad.adoption_id) AS adoptions
FROM   species s
LEFT   JOIN animal   a  ON a.species_id = s.species_id
LEFT   JOIN adoption ad ON ad.animal_id = a.animal_id
GROUP  BY s.name;
-- Cat 2, Dog 5, Parrot 1, Rabbit 1
```

<div dir="rtl">

---

## ✅ תרגיל 3 — HAVING

</div>

```sql
-- a
SELECT STRFTIME('%Y-%m', expense_date) AS month, SUM(amount) AS total
FROM   expense
WHERE  expense_date LIKE '2024%'
GROUP  BY month
HAVING SUM(amount) > 2000;
```

```text
month    total
-------  ------
2024-01  3230.0
2024-03  2990.0
2024-08  2100.0
```

```sql
-- b   Haifa 3
SELECT city, COUNT(*) FROM person WHERE role = 'adopter' GROUP BY city HAVING COUNT(*) > 1;

-- c   Mixed 3, Tabby 2
SELECT breed, COUNT(*) FROM animal WHERE breed IS NOT NULL GROUP BY breed HAVING COUNT(*) > 1;

-- d
SELECT category, ROUND(AVG(amount), 2) AS avg
FROM   expense
GROUP  BY category
HAVING AVG(amount) > 500
ORDER  BY avg DESC;
```

```text
category     avg
-----------  ------
food         1872.5
utilities    942.5
medical      679.09
maintenance  540.0
```

<div dir="rtl">

**ה.** `breed IS NOT NULL` הוא תנאי על **שורה בודדת** — לכן `WHERE`: מסננים לפני שמקבצים. אפשר גם `HAVING breed IS NOT NULL` (כי `breed` היא עמודת הקיבוץ) — התוצאה זהה, אבל SQL יקבץ קודם גם את ה‑NULL‑ים ורק אז יזרוק אותם. **תנאי על שורה — ב‑`WHERE`.**

---

## ✅ תרגיל 4 — כפילויות

</div>

```sql
-- a   Luna 2
SELECT a.name, COUNT(*) FROM intake i JOIN animal a ON a.animal_id = i.animal_id
GROUP  BY a.animal_id HAVING COUNT(*) > 1;

-- b   Dana 2 / 700, Lior 2 / 350, Shira 2 / 350
SELECT p.first_name || ' ' || p.last_name AS adopter, COUNT(*), SUM(ad.fee_paid)
FROM   adoption ad JOIN person p ON p.person_id = ad.adopter_id
GROUP  BY p.person_id HAVING COUNT(*) > 1;

-- c   Luna 2 (rabies), Rocky 3 (rabies)
SELECT a.name, v.vaccine_type_id, COUNT(*) AS times
FROM   vaccination v JOIN animal a ON a.animal_id = v.animal_id
GROUP  BY v.animal_id, v.vaccine_type_id
HAVING COUNT(*) > 1;

-- d
SELECT a.name, COUNT(v.vaccination_id) AS shots, COALESCE(SUM(v.cost), 0) AS cost
FROM   animal a
LEFT   JOIN vaccination v ON v.animal_id = a.animal_id
GROUP  BY a.animal_id
ORDER  BY cost DESC
LIMIT  5;
```

```text
name     shots  cost
-------  -----  -----
Rocky    4      345.0
Luna     3      260.0
Charlie  2      185.0
Shadow   2      185.0
Max      2      175.0
```

<div dir="rtl">

> 💡 **סעיף ג' מקבץ לפי שתי עמודות** — `(animal_id, vaccine_type_id)` — כי "אותו חיסון לאותה חיה" הוא **זוג**.

---

## ✅ תרגיל 5 — תת‑שאילתה של ערך אחד

</div>

```sql
-- a   Nala 2024-03-01
SELECT name, birth_date FROM animal WHERE birth_date = (SELECT MAX(birth_date) FROM animal);

-- b
SELECT description, amount FROM expense
WHERE  amount > (SELECT AVG(amount) FROM expense)
ORDER  BY amount DESC;
```

```text
description           amount
--------------------  ------
leg surgery           2100.0
dry food, 20 sacks    1950.0
dry food, 20 sacks    1900.0
dry food, 20 sacks    1850.0
dry food, 20 sacks    1790.0
neutering surgery     1200.0
electricity December  1020.0
electricity January   960.0
electricity May       910.0
```

```sql
-- c   8
SELECT COUNT(*) FROM animal WHERE weight_kg > (SELECT AVG(weight_kg) FROM animal);

-- d   Rocky, Bella, Rex, Shadow
SELECT name, weight_kg FROM animal
WHERE  species_id = 1
  AND  weight_kg > (SELECT AVG(weight_kg) FROM animal WHERE species_id = 1);
```

<div dir="rtl">

---

## ✅ תרגיל 6 — IN, NOT IN ו‑EXISTS

</div>

```sql
-- a   Dana, Lior, Omer, Eitan
SELECT first_name, last_name FROM person
WHERE  person_id IN (SELECT ad.adopter_id
                     FROM   adoption ad JOIN animal a ON a.animal_id = ad.animal_id
                     WHERE  a.species_id = 1);

-- b   (no rows!)
SELECT first_name, last_name FROM person
WHERE  person_id NOT IN (SELECT brought_by FROM intake);
```

<div dir="rtl">

**ב.** **אף שורה** — וזו מלכודת ה‑NULL מסעיף 7.2. בשתי קליטות מסוג transfer `brought_by` הוא NULL, אז הרשימה מכילה NULL, ו‑`x NOT IN (…, NULL)` לעולם אינו true.

</div>

```sql
-- c1
SELECT first_name, last_name, role FROM person
WHERE  person_id NOT IN (SELECT brought_by FROM intake WHERE brought_by IS NOT NULL);

-- c2 (recommended)
SELECT p.first_name, p.last_name, p.role FROM person p
WHERE  NOT EXISTS (SELECT 1 FROM intake i WHERE i.brought_by = p.person_id);
```

```text
first_name  last_name  role
----------  ---------  ---------
Ruti        Almog      volunteer
Dr. Ron     Levi       vet
Dr. Maya    Nahum      vet
```

```sql
-- d   Bunny, Coco, Felix, Lily, Mitzi, Oscar, Rex, Rocky, Shadow
SELECT a.name FROM animal a
WHERE  a.status = 'available'
  AND  NOT EXISTS (SELECT 1 FROM adoption ad WHERE ad.animal_id = a.animal_id)
ORDER  BY a.name;

-- e
SELECT name FROM animal
WHERE  animal_id IN (SELECT animal_id FROM vaccination
                     INTERSECT
                     SELECT animal_id FROM expense)
ORDER  BY name;
-- Bella, Daisy, Felix, Luna, Max, Oscar, Rex, Rocky, Shadow
```

<div dir="rtl">

> 💡 **בסעיף ה' ה‑NULL‑ים של `expense` לא הפריעו** — כי `INTERSECT` משווה ערכים, ו‑NULL פשוט לא נמצא בצד השני. רק `NOT IN` רגיש כל כך.

---

## ✅ תרגיל 7 — מתואמות

</div>

```sql
-- a
SELECT e.description, e.amount, e.category
FROM   expense e
WHERE  e.amount = (SELECT MAX(e2.amount) FROM expense e2 WHERE e2.category = e.category)
ORDER  BY e.amount DESC;
```

```text
description           amount  category
--------------------  ------  -----------
leg surgery           2100.0  medical
dry food, 20 sacks    1950.0  food
electricity December  1020.0  utilities
kennel door repair    540.0   maintenance
cat litter            310.0   supplies
```

```sql
-- b
SELECT p.first_name,
       (SELECT COUNT(*) FROM adoption ad WHERE ad.adopter_id = p.person_id) AS adoptions
FROM   person p
WHERE  p.role = 'adopter'
ORDER  BY adoptions DESC, p.first_name;
-- Dana 2, Lior 2, Shira 2, Eitan 1, Omer 1, Yossi 1

-- c
SELECT a.name,
       (SELECT MAX(i.intake_date) FROM intake i WHERE i.animal_id = a.animal_id) AS last_intake
FROM   animal a
WHERE  a.status = 'available'
ORDER  BY last_intake
LIMIT  3;
```

```text
name   last_intake
-----  -----------
Rocky  2023-05-20
Mitzi  2023-06-11
Coco   2023-09-30
```

<div dir="rtl">

> 🎬 **Rocky מחכה לבית מאז מאי 2023** — יותר משלוש שנים. שאילתה כזו היא בדיוק מה שמקלט אמיתי צריך כדי להחליט את מי לקדם בפייסבוק השבוע.

**ד.** הפתרון בסעיף 8.2 במודול. במודול 21, self join עם `v1.given_date < v2.given_date` החזיר **כל** חיסון מאוחר — כולל 2023 ⟵ 2025. כאן `MIN(v2.given_date)` בוחר את **הקרוב ביותר** מבין המאוחרים — ולכל חיסון יש בדיוק "הבא" אחד (או NULL).

---

## ✅ תרגיל 8 — צבירה על צבירה, ופעולות קבוצה

</div>

```sql
-- a   1.5
SELECT ROUND(AVG(n), 2)
FROM   (SELECT adopter_id, COUNT(*) AS n FROM adoption GROUP BY adopter_id);

-- b   food
WITH totals AS (SELECT category, SUM(amount) AS total FROM expense GROUP BY category)
SELECT category FROM totals WHERE total = (SELECT MAX(total) FROM totals);
-- (or simply: ... GROUP BY category ORDER BY SUM(amount) DESC LIMIT 1)

-- c
SELECT first_name || ' ' || last_name AS name, 'person' AS kind
FROM   person WHERE city = 'Haifa'
UNION  ALL
SELECT name, 'animal'
FROM   animal
WHERE  animal_id IN (SELECT animal_id FROM intake WHERE location LIKE '%Haifa%');
```

```text
name          kind
------------  ------
Ruti Almog    person
Noa Peretz    person
Dr. Ron Levi  person
Dana Cohen    person
Lior Bar      person
Omer Dayan    person
Luna          animal
```

<div dir="rtl">

**ד.** `UNION` ⟵ **7**; `UNION ALL` ⟵ **56**. ב‑`vaccination` יש 28 שורות, אבל רק **7 מחירים שונים** (60, 65, 80, 85, 90, 95, 100). `UNION` מסיר כפילויות — גם בתוך כל צד — ונשארים 7. `UNION ALL` פשוט מדביק: 28 + 28 = 56.

**ה.** הפתרון בסעיף 5.1 במודול. הנקודה החשובה: **שלוש רמות, שלוש שאילתות** — הפירוט, הסיכום לשנה, והסך הכול — מחוברות ב‑`UNION ALL`, ועמודת `lvl` נסתרת כדי שהסיכום יבוא **אחרי** הפירוט.

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[❓ לשאלות](questions.md)**

</div>

</div>


<!-- w3schools:start -->
<div dir="rtl">

---

## 🌐 תרגול ב‑W3Schools: פתרונות

> כל השאילתות כאן הורצו ב‑W3Schools. מספר הרשומות הוא מה שהאתר מחזיר.

**W1.**

```sql
SELECT Customers.Country, COUNT(Customers.CustomerID) AS cnt FROM Customers GROUP BY Customers.Country HAVING COUNT(Customers.CustomerID) > 5;
```

**5** רשומות. השורה הראשונה: `Brazil · 9`

**W2.**

```sql
SELECT Products.ProductName, Products.Price FROM Products WHERE Products.Price > (SELECT AVG(Price) FROM Products);
```

**25** רשומות. השורה הראשונה: `Uncle Bobs Organic Dried Pears · 30.00`

**W3.**

```sql
SELECT Customers.CustomerName FROM Customers WHERE Customers.CustomerID NOT IN (SELECT CustomerID FROM Orders);
```

**17** רשומות. השורה הראשונה: `Alfreds Futterkiste`


</div>
<!-- w3schools:end -->

<!-- exam-style:start -->
<div dir="rtl">

---

## 🎓 תרגול בסגנון הבחינה: פתרונות

**ב1.** רק עיר 1 (ירכא), עם 4 משתתפים. לכל שאר הערים יש פחות מ‑3 משתתפים.

<figure dir="ltr" class="dbtable">

| CityCode | cnt |
|:---:|:---:|
| 1 | 4 |

</figure>

**ב2.** ```sql
SELECT Cities.CityName FROM Cities
WHERE Cities.CityCode NOT IN (SELECT CityCode FROM Members);
```

<figure dir="ltr" class="dbtable">

| CityName |
|:---:|
| שפרעם |

</figure>

**ב3.** ```sql
SELECT Clubs.ClubName, Clubs.Price FROM Clubs
WHERE Clubs.Price > (SELECT AVG(Price) FROM Clubs);
```

<figure dir="ltr" class="dbtable">

| avg_price |
|:---:|
| 190 |

</figure>

<figure dir="ltr" class="dbtable">

| ClubName | Price |
|:---:|:---:|
| שחייה מתחילים | 220 |
| שחייה מתקדמים | 250 |
| טניס | 300 |

</figure>


</div>
<!-- exam-style:end -->
