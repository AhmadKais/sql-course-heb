<div dir="rtl">

# 🐾 מקלט בעלי החיים "בית חם"

> 8 טבלאות באנגלית: חיות, אנשים, אימוצים, חיסונים והוצאות. בסיס גדול לתרגול חופשי.
>
> **שימוש:** תרגול חופשי ופרויקט · **8 טבלאות**

[🏠 לדף הראשי](../../README.md) · [🗄️ כל בסיסי הנתונים](../README.md)

---

## ▶️ איך מריצים (בלי להתקין כלום)

1. פותחים את **[OneCompiler — SQLite](https://onecompiler.com/sqlite)** (או **[SQLite Online](https://sqliteonline.com/)**, שמציג גם את רשימת הטבלאות בצד).
2. מוחקים את הדוגמה שבחלון (`Ctrl+A` ← `Delete`).
3. מעתיקים את **כל** הקוד של בסיס הנתונים ומדביקים.
4. **מתחת** לקוד כותבים את השאילתה שלכם ולוחצים **Run**.

> 💡 כל קובץ מתחיל ב‑`DROP TABLE IF EXISTS`, אז אפשר להדביק אותו שוב ושוב — הנתונים חוזרים למצב ההתחלתי. זה שימושי אחרי תרגילי `UPDATE` / `DELETE`.

---

## 📥 הקוד המלא להעתקה

קובץ: [`shelter.sql`](shelter.sql) · [פתיחה כטקסט נקי (Ctrl+A, Ctrl+C)](https://raw.githubusercontent.com/AhmadKais/sql-course-heb/main/databases/shelter/shelter.sql)

</div>

<details>
<summary>📥 <b>לחצו כאן לקוד שבונה את בסיס הנתונים 🐾 מקלט בעלי החיים "בית חם"</b> — מעתיקים הכול ומדביקים ב‑OneCompiler</summary>

```sql
-- ============================================================
--  "Beit Cham" animal shelter -- practice database
--  Course: Databases & SQL (Hebrew) -- units 2-7
--
--  Paste this WHOLE file into OneCompiler (SQLite)
--  (https://onecompiler.com/sqlite) and click Run.
--  Then write your own SELECT queries below it.
--
--  Dialect: SQLite-compatible (works in OneCompiler, DB Browser, DB Fiddle).
--  Dates are stored as TEXT in ISO format 'YYYY-MM-DD'.
-- ============================================================

DROP TABLE IF EXISTS expense;
DROP TABLE IF EXISTS adoption;
DROP TABLE IF EXISTS vaccination;
DROP TABLE IF EXISTS vaccine_type;
DROP TABLE IF EXISTS intake;
DROP TABLE IF EXISTS animal;
DROP TABLE IF EXISTS person;
DROP TABLE IF EXISTS species;

-- ------------------------------------------------------------
-- SPECIES  -- a small lookup table
-- ------------------------------------------------------------
CREATE TABLE species (
  species_id   INTEGER PRIMARY KEY,
  name         TEXT    NOT NULL UNIQUE,
  adoption_fee REAL    NOT NULL          -- current fee in NIS
);

INSERT INTO species VALUES (1, 'Dog',    400);
INSERT INTO species VALUES (2, 'Cat',    250);
INSERT INTO species VALUES (3, 'Rabbit', 100);
INSERT INTO species VALUES (4, 'Parrot', 150);

-- ------------------------------------------------------------
-- PERSON  -- volunteers, adopters and vets, all in one table
-- ------------------------------------------------------------
CREATE TABLE person (
  person_id   INTEGER PRIMARY KEY,
  first_name  TEXT    NOT NULL,
  last_name   TEXT    NOT NULL,
  role        TEXT    NOT NULL,          -- 'volunteer' / 'adopter' / 'vet'
  city        TEXT,
  phone       TEXT,
  joined_date TEXT    NOT NULL
);

INSERT INTO person VALUES ( 1, 'Ruti',   'Almog',   'volunteer', 'Haifa',     '052-1111111', '2013-03-01');
INSERT INTO person VALUES ( 2, 'Noa',    'Peretz',  'volunteer', 'Haifa',     '054-2222222', '2019-09-15');
INSERT INTO person VALUES ( 3, 'Amir',   'Levi',    'volunteer', 'Kiryat Ata','050-3333333', '2022-01-10');
INSERT INTO person VALUES ( 4, 'Dr. Ron','Levi',    'vet',       'Haifa',     '053-4444444', '2015-06-01');
INSERT INTO person VALUES ( 5, 'Dr. Maya','Nahum',  'vet',       'Nesher',    '058-5555555', '2020-02-20');
INSERT INTO person VALUES ( 6, 'Dana',   'Cohen',   'adopter',   'Haifa',     '052-6666666', '2023-05-12');
INSERT INTO person VALUES ( 7, 'Yossi',  'Mizrahi', 'adopter',   'Tel Aviv',  '054-7777777', '2023-08-03');
INSERT INTO person VALUES ( 8, 'Lior',   'Bar',     'adopter',   'Haifa',     '050-8888888', '2024-01-19');
INSERT INTO person VALUES ( 9, 'Shira',  'Katz',    'adopter',   'Karmiel',   '052-9999999', '2024-04-02');
INSERT INTO person VALUES (10, 'Omer',   'Dayan',   'adopter',   'Haifa',     NULL,          '2024-11-30');
INSERT INTO person VALUES (11, 'Tamar',  'Golan',   'volunteer', 'Tirat Carmel','053-1010101','2024-02-14');
INSERT INTO person VALUES (12, 'Eitan',  'Shalev',  'adopter',   'Nahariya',  '054-1212121', '2025-06-08');

-- ------------------------------------------------------------
-- ANIMAL
-- ------------------------------------------------------------
CREATE TABLE animal (
  animal_id    INTEGER PRIMARY KEY,
  name         TEXT    NOT NULL,
  species_id   INTEGER NOT NULL REFERENCES species(species_id),
  breed        TEXT,                     -- NULL when unknown
  sex          TEXT    NOT NULL CHECK (sex IN ('M','F','U')),
  birth_date   TEXT,                     -- estimated; NULL when unknown
  weight_kg    REAL,
  chip_number  TEXT    UNIQUE,           -- NULL for strays without a chip
  status       TEXT    NOT NULL          -- 'available' / 'adopted' / 'medical' / 'quarantine' / 'deceased'
);

INSERT INTO animal VALUES ( 1, 'Luna',   1, 'Mixed',        'F', '2021-03-15', 18.5, '985100001', 'adopted');
INSERT INTO animal VALUES ( 2, 'Simba',  2, 'Tabby',        'M', '2022-07-01',  4.2, '985100002', 'adopted');
INSERT INTO animal VALUES ( 3, 'Rocky',  1, 'Labrador',     'M', '2019-11-20', 31.0, '985100003', 'available');
INSERT INTO animal VALUES ( 4, 'Mitzi',  2, NULL,           'F', '2023-01-10',  3.1, NULL,        'available');
INSERT INTO animal VALUES ( 5, 'Bella',  1, 'German Shepherd','F','2018-05-05',28.4, '985100005', 'adopted');
INSERT INTO animal VALUES ( 6, 'Tom',    2, 'Siamese',      'M', '2020-09-09',  4.8, '985100006', 'adopted');
INSERT INTO animal VALUES ( 7, 'Coco',   4, 'Cockatiel',    'U', NULL,          0.1, NULL,        'available');
INSERT INTO animal VALUES ( 8, 'Max',    1, 'Beagle',       'M', '2022-02-28', 12.3, '985100008', 'medical');
INSERT INTO animal VALUES ( 9, 'Nala',   2, NULL,           'F', '2024-03-01',  2.9, NULL,        'quarantine');
INSERT INTO animal VALUES (10, 'Thumper',3, 'Lop',          'M', '2023-06-15',  1.8, NULL,        'adopted');
INSERT INTO animal VALUES (11, 'Zoe',    1, 'Mixed',        'F', '2016-01-01', 22.0, '985100011', 'adopted');
INSERT INTO animal VALUES (12, 'Oscar',  2, 'Persian',      'M', '2021-12-12',  5.5, '985100012', 'available');
INSERT INTO animal VALUES (13, 'Rex',    1, 'Rottweiler',   'M', '2017-08-08', 38.7, '985100013', 'available');
INSERT INTO animal VALUES (14, 'Lily',   2, NULL,           'F', NULL,          3.4, NULL,        'available');
INSERT INTO animal VALUES (15, 'Charlie',1, 'Poodle',       'M', '2023-10-10',  7.2, '985100015', 'adopted');
INSERT INTO animal VALUES (16, 'Kiwi',   4, 'Budgie',       'F', NULL,          0.04,NULL,        'adopted');
INSERT INTO animal VALUES (17, 'Daisy',  1, 'Mixed',        'F', '2020-04-04', 15.6, '985100017', 'deceased');
INSERT INTO animal VALUES (18, 'Felix',  2, 'Tabby',        'M', '2019-02-14',  5.0, '985100018', 'available');
INSERT INTO animal VALUES (19, 'Bunny',  3, NULL,           'F', '2024-01-01',  1.5, NULL,        'available');
INSERT INTO animal VALUES (20, 'Shadow', 1, 'Husky',        'M', '2021-06-30', 25.1, '985100020', 'available');

-- ------------------------------------------------------------
-- INTAKE  -- one row per arrival; an animal can arrive more than once
-- ------------------------------------------------------------
CREATE TABLE intake (
  intake_id    INTEGER PRIMARY KEY,
  animal_id    INTEGER NOT NULL REFERENCES animal(animal_id),
  intake_date  TEXT    NOT NULL,
  intake_type  TEXT    NOT NULL,         -- 'stray' / 'surrender' / 'transfer'
  brought_by   INTEGER REFERENCES person(person_id),   -- volunteer or previous owner
  location     TEXT,                     -- where found (strays only)
  reason       TEXT                      -- why surrendered (surrenders only)
);

INSERT INTO intake VALUES ( 1,  1, '2023-03-14', 'stray',     2, 'Herzl St, Haifa',      NULL);
INSERT INTO intake VALUES ( 2,  2, '2023-04-02', 'surrender', 7, NULL,                   'moving abroad');
INSERT INTO intake VALUES ( 3,  3, '2023-05-20', 'stray',     3, 'Carmel beach',         NULL);
INSERT INTO intake VALUES ( 4,  4, '2023-06-11', 'stray',     2, 'Hadar market',         NULL);
INSERT INTO intake VALUES ( 5,  5, '2023-07-07', 'surrender', 6, NULL,                   'owner passed away');
INSERT INTO intake VALUES ( 6,  6, '2023-08-19', 'stray',    11, 'Tirat Carmel park',    NULL);
INSERT INTO intake VALUES ( 7,  7, '2023-09-30', 'surrender', 8, NULL,                   'allergy in family');
INSERT INTO intake VALUES ( 8,  8, '2023-11-05', 'stray',     3, 'Route 4 shoulder',     NULL);
INSERT INTO intake VALUES ( 9,  9, '2024-01-22', 'stray',     2, 'Bat Galim',            NULL);
INSERT INTO intake VALUES (10, 10, '2024-02-14', 'surrender', 9, NULL,                   'child lost interest');
INSERT INTO intake VALUES (11, 11, '2024-03-03', 'transfer',  NULL, NULL,                'transfer from Akko shelter');
INSERT INTO intake VALUES (12, 12, '2024-04-18', 'stray',    11, 'Neve Shaanan',         NULL);
INSERT INTO intake VALUES (13, 13, '2024-05-25', 'surrender', 10, NULL,                  'too big for apartment');
INSERT INTO intake VALUES (14, 14, '2024-07-09', 'stray',     2, 'Kiryat Eliezer',       NULL);
INSERT INTO intake VALUES (15, 15, '2024-08-30', 'stray',     3, 'Grand Canyon mall',    NULL);
INSERT INTO intake VALUES (16, 16, '2024-10-12', 'surrender', 12, NULL,                  'cannot afford');
INSERT INTO intake VALUES (17, 17, '2024-11-01', 'stray',    11, 'Wadi Nisnas',          NULL);
INSERT INTO intake VALUES (18, 18, '2025-01-15', 'transfer',  NULL, NULL,                'transfer from Nahariya shelter');
INSERT INTO intake VALUES (19, 19, '2025-02-20', 'stray',     2, 'Technion campus',      NULL);
INSERT INTO intake VALUES (20, 20, '2025-03-08', 'surrender', 7, NULL,                   'moving abroad');
-- Luna (animal 1) was adopted, returned, and re-entered -> a SECOND intake row
INSERT INTO intake VALUES (21,  1, '2024-06-01', 'surrender', 6, NULL,                   'returned by adopter - allergy');

-- ------------------------------------------------------------
-- VACCINE_TYPE and VACCINATION
-- ------------------------------------------------------------
CREATE TABLE vaccine_type (
  vaccine_type_id INTEGER PRIMARY KEY,
  name            TEXT    NOT NULL,
  species_id      INTEGER NOT NULL REFERENCES species(species_id),
  interval_months INTEGER               -- NULL = one-time
);

INSERT INTO vaccine_type VALUES (1, 'Rabies',       1, 12);
INSERT INTO vaccine_type VALUES (2, 'DHPP',         1, 12);
INSERT INTO vaccine_type VALUES (3, 'Rabies',       2, 12);
INSERT INTO vaccine_type VALUES (4, 'FVRCP',        2, 12);
INSERT INTO vaccine_type VALUES (5, 'Myxomatosis',  3, 6);

CREATE TABLE vaccination (
  vaccination_id  INTEGER PRIMARY KEY,
  animal_id       INTEGER NOT NULL REFERENCES animal(animal_id),
  vaccine_type_id INTEGER NOT NULL REFERENCES vaccine_type(vaccine_type_id),
  vet_id          INTEGER NOT NULL REFERENCES person(person_id),
  given_date      TEXT    NOT NULL,
  cost            REAL    NOT NULL
);

INSERT INTO vaccination VALUES ( 1,  1, 1, 4, '2023-03-20', 80);
INSERT INTO vaccination VALUES ( 2,  1, 2, 4, '2023-03-20', 95);
INSERT INTO vaccination VALUES ( 3,  2, 3, 5, '2023-04-08', 80);
INSERT INTO vaccination VALUES ( 4,  2, 4, 5, '2023-04-08', 90);
INSERT INTO vaccination VALUES ( 5,  3, 1, 4, '2023-05-25', 80);
INSERT INTO vaccination VALUES ( 6,  3, 2, 4, '2023-05-25', 95);
INSERT INTO vaccination VALUES ( 7,  4, 3, 5, '2023-06-15', 80);
INSERT INTO vaccination VALUES ( 8,  5, 1, 4, '2023-07-12', 80);
INSERT INTO vaccination VALUES ( 9,  6, 3, 5, '2023-08-24', 80);
INSERT INTO vaccination VALUES (10,  6, 4, 5, '2023-08-24', 90);
INSERT INTO vaccination VALUES (11,  8, 1, 4, '2023-11-10', 80);
INSERT INTO vaccination VALUES (12,  8, 2, 4, '2023-11-10', 95);
INSERT INTO vaccination VALUES (13, 10, 5, 5, '2024-02-20', 60);
INSERT INTO vaccination VALUES (14, 11, 1, 4, '2024-03-08', 80);
INSERT INTO vaccination VALUES (15, 12, 3, 5, '2024-04-22', 80);
INSERT INTO vaccination VALUES (16, 12, 4, 5, '2024-04-22', 90);
INSERT INTO vaccination VALUES (17, 13, 1, 4, '2024-05-30', 80);
INSERT INTO vaccination VALUES (18, 13, 2, 4, '2024-05-30', 95);
INSERT INTO vaccination VALUES (19,  1, 1, 4, '2024-06-05', 85);   -- Luna's booster, one year later
INSERT INTO vaccination VALUES (20, 15, 1, 4, '2024-09-04', 85);
INSERT INTO vaccination VALUES (21, 15, 2, 4, '2024-09-04', 100);
INSERT INTO vaccination VALUES (22, 17, 1, 5, '2024-11-06', 85);
INSERT INTO vaccination VALUES (23, 18, 3, 5, '2025-01-20', 85);
INSERT INTO vaccination VALUES (24, 19, 5, 5, '2025-02-25', 65);
INSERT INTO vaccination VALUES (25, 20, 1, 4, '2025-03-12', 85);
INSERT INTO vaccination VALUES (26, 20, 2, 4, '2025-03-12', 100);
INSERT INTO vaccination VALUES (27,  3, 1, 4, '2024-05-28', 85);   -- Rocky's booster
INSERT INTO vaccination VALUES (28,  3, 1, 4, '2025-05-30', 85);   -- Rocky's second booster

-- ------------------------------------------------------------
-- ADOPTION  -- fee_paid is FROZEN at the value paid on that day
-- ------------------------------------------------------------
CREATE TABLE adoption (
  adoption_id   INTEGER PRIMARY KEY,
  animal_id     INTEGER NOT NULL REFERENCES animal(animal_id),
  adopter_id    INTEGER NOT NULL REFERENCES person(person_id),
  adoption_date TEXT    NOT NULL,
  fee_paid      REAL    NOT NULL,
  returned_date TEXT                    -- NULL unless the animal came back
);

INSERT INTO adoption VALUES ( 1,  1, 6, '2023-05-10', 300, '2024-06-01');   -- 2023 rate; returned
INSERT INTO adoption VALUES ( 2,  2, 7, '2023-06-15', 200, NULL);           -- 2023 cat rate
INSERT INTO adoption VALUES ( 3,  5, 8, '2024-02-10', 200, NULL);           -- 2024 dog rate, but Bella is over 8 -> half price
INSERT INTO adoption VALUES ( 4,  6, 9, '2024-05-05', 250, NULL);
INSERT INTO adoption VALUES ( 5, 10, 9, '2024-06-20', 100, NULL);
INSERT INTO adoption VALUES ( 6, 11,10, '2024-08-15', 200, NULL);           -- Zoe is over 8 -> half price
INSERT INTO adoption VALUES ( 7,  1, 12,'2025-07-01', 400, NULL);           -- Luna adopted AGAIN, 2025 rate
INSERT INTO adoption VALUES ( 8, 15, 6, '2024-12-01', 400, NULL);
INSERT INTO adoption VALUES ( 9, 16, 8, '2025-01-10', 150, NULL);

-- ------------------------------------------------------------
-- EXPENSE  -- animal_id is NULL for general (shelter-wide) expenses
-- ------------------------------------------------------------
CREATE TABLE expense (
  expense_id   INTEGER PRIMARY KEY,
  expense_date TEXT    NOT NULL,
  category     TEXT    NOT NULL,         -- 'food' / 'medical' / 'supplies' / 'utilities' / 'maintenance'
  amount       REAL    NOT NULL,
  animal_id    INTEGER REFERENCES animal(animal_id),   -- NULL = general
  description  TEXT
);

INSERT INTO expense VALUES ( 1, '2024-01-05', 'food',        1850.00, NULL, 'dry food, 20 sacks');
INSERT INTO expense VALUES ( 2, '2024-01-12', 'medical',      420.00,    8, 'x-ray + medication');
INSERT INTO expense VALUES ( 3, '2024-01-31', 'utilities',    960.00, NULL, 'electricity January');
INSERT INTO expense VALUES ( 4, '2024-02-03', 'medical',      650.00,    5, 'dental cleaning');
INSERT INTO expense VALUES ( 5, '2024-02-18', 'supplies',     310.00, NULL, 'cat litter');
INSERT INTO expense VALUES ( 6, '2024-02-28', 'utilities',    880.00, NULL, 'electricity February');
INSERT INTO expense VALUES ( 7, '2024-03-10', 'medical',     1200.00,   13, 'neutering surgery');
INSERT INTO expense VALUES ( 8, '2024-03-15', 'food',        1790.00, NULL, 'dry food, 20 sacks');
INSERT INTO expense VALUES ( 9, '2024-04-02', 'maintenance',  540.00, NULL, 'kennel door repair');
INSERT INTO expense VALUES (10, '2024-04-20', 'medical',      380.00,    9, 'blood tests');
INSERT INTO expense VALUES (11, '2024-05-08', 'medical',      275.00,   12, 'deworming');
INSERT INTO expense VALUES (12, '2024-05-30', 'utilities',    910.00, NULL, 'electricity May');
INSERT INTO expense VALUES (13, '2024-06-14', 'medical',      890.00,    1, 'allergy treatment after return');
INSERT INTO expense VALUES (14, '2024-07-01', 'food',        1900.00, NULL, 'dry food, 20 sacks');
INSERT INTO expense VALUES (15, '2024-08-22', 'medical',     2100.00,    8, 'leg surgery');
INSERT INTO expense VALUES (16, '2024-09-09', 'supplies',     220.00, NULL, 'leashes and bowls');
INSERT INTO expense VALUES (17, '2024-10-17', 'medical',      450.00,   17, 'emergency visit');
INSERT INTO expense VALUES (18, '2024-11-03', 'medical',      175.00,   20, 'microchip');
INSERT INTO expense VALUES (19, '2024-12-12', 'utilities',   1020.00, NULL, 'electricity December');
INSERT INTO expense VALUES (20, '2025-01-20', 'medical',      330.00,   18, 'eye infection');
INSERT INTO expense VALUES (21, '2025-02-05', 'food',        1950.00, NULL, 'dry food, 20 sacks');
INSERT INTO expense VALUES (22, '2025-03-14', 'medical',      600.00,    3, 'hip x-ray');

-- ============================================================
--  Quick check: if this returns 20, everything loaded.
-- ============================================================
SELECT COUNT(*) AS animals_loaded FROM animal;
```

</details>


<div dir="rtl">

---

## 🗺️ הטבלאות והקשרים

| הטבלה | שורות | מפתח ראשי 🔑 | מפתחות זרים 🔗 |
|---|:---:|---|---|
| [`species`](#species) | 4 | `species_id` | — |
| [`person`](#person) | 12 | `person_id` | — |
| [`animal`](#animal) | 20 | `animal_id` | `species_id` → `species(species_id)` |
| [`intake`](#intake) | 21 | `intake_id` | `brought_by` → `person(person_id)`<br>`animal_id` → `animal(animal_id)` |
| [`vaccine_type`](#vaccine_type) | 5 | `vaccine_type_id` | `species_id` → `species(species_id)` |
| [`vaccination`](#vaccination) | 28 | `vaccination_id` | `vet_id` → `person(person_id)`<br>`vaccine_type_id` → `vaccine_type(vaccine_type_id)`<br>`animal_id` → `animal(animal_id)` |
| [`adoption`](#adoption) | 9 | `adoption_id` | `adopter_id` → `person(person_id)`<br>`animal_id` → `animal(animal_id)` |
| [`expense`](#expense) | 22 | `expense_id` | `animal_id` → `animal(animal_id)` |

> 🔑 = מפתח ראשי (PK) · 🔗 = מפתח זר (FK) — מצביע על מפתח ראשי בטבלה אחרת.

---

## species

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `species_id` | INTEGER | 🔑 PK |  |
| `name` | TEXT |  | חובה (NOT NULL). |
| `adoption_fee` | REAL |  | חובה (NOT NULL). current fee in NIS |

**הנתונים (4 שורות):**

| species_id 🔑 | name | adoption_fee |
|---|---|---|
| 1 | Dog | 400.0 |
| 2 | Cat | 250.0 |
| 3 | Rabbit | 100.0 |
| 4 | Parrot | 150.0 |

---

## person

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `person_id` | INTEGER | 🔑 PK |  |
| `first_name` | TEXT |  | חובה (NOT NULL). |
| `last_name` | TEXT |  | חובה (NOT NULL). |
| `role` | TEXT |  | חובה (NOT NULL). 'volunteer' / 'adopter' / 'vet' |
| `city` | TEXT |  |  |
| `phone` | TEXT |  |  |
| `joined_date` | TEXT |  | חובה (NOT NULL). |

**הנתונים (12 שורות):**

| person_id 🔑 | first_name | last_name | role | city | phone | joined_date |
|---|---|---|---|---|---|---|
| 1 | Ruti | Almog | volunteer | Haifa | 052-1111111 | 2013-03-01 |
| 2 | Noa | Peretz | volunteer | Haifa | 054-2222222 | 2019-09-15 |
| 3 | Amir | Levi | volunteer | Kiryat Ata | 050-3333333 | 2022-01-10 |
| 4 | Dr. Ron | Levi | vet | Haifa | 053-4444444 | 2015-06-01 |
| 5 | Dr. Maya | Nahum | vet | Nesher | 058-5555555 | 2020-02-20 |
| 6 | Dana | Cohen | adopter | Haifa | 052-6666666 | 2023-05-12 |
| 7 | Yossi | Mizrahi | adopter | Tel Aviv | 054-7777777 | 2023-08-03 |
| 8 | Lior | Bar | adopter | Haifa | 050-8888888 | 2024-01-19 |
| 9 | Shira | Katz | adopter | Karmiel | 052-9999999 | 2024-04-02 |
| 10 | Omer | Dayan | adopter | Haifa | *NULL* | 2024-11-30 |
| 11 | Tamar | Golan | volunteer | Tirat Carmel | 053-1010101 | 2024-02-14 |
| 12 | Eitan | Shalev | adopter | Nahariya | 054-1212121 | 2025-06-08 |

---

## animal

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `animal_id` | INTEGER | 🔑 PK |  |
| `name` | TEXT |  | חובה (NOT NULL). |
| `species_id` | INTEGER | 🔗 FK → `species(species_id)` | חובה (NOT NULL). |
| `breed` | TEXT |  | NULL when unknown |
| `sex` | TEXT |  | חובה (NOT NULL). |
| `birth_date` | TEXT |  | estimated; NULL when unknown |
| `weight_kg` | REAL |  |  |
| `chip_number` | TEXT |  | NULL for strays without a chip |
| `status` | TEXT |  | חובה (NOT NULL). 'available' / 'adopted' / 'medical' / 'quarantine' / 'deceased' |

**הנתונים (20 שורות):**

| animal_id 🔑 | name | species_id 🔗 | breed | sex | birth_date | weight_kg | chip_number | status |
|---|---|---|---|---|---|---|---|---|
| 1 | Luna | 1 | Mixed | F | 2021-03-15 | 18.5 | 985100001 | adopted |
| 2 | Simba | 2 | Tabby | M | 2022-07-01 | 4.2 | 985100002 | adopted |
| 3 | Rocky | 1 | Labrador | M | 2019-11-20 | 31.0 | 985100003 | available |
| 4 | Mitzi | 2 | *NULL* | F | 2023-01-10 | 3.1 | *NULL* | available |
| 5 | Bella | 1 | German Shepherd | F | 2018-05-05 | 28.4 | 985100005 | adopted |
| 6 | Tom | 2 | Siamese | M | 2020-09-09 | 4.8 | 985100006 | adopted |
| 7 | Coco | 4 | Cockatiel | U | *NULL* | 0.1 | *NULL* | available |
| 8 | Max | 1 | Beagle | M | 2022-02-28 | 12.3 | 985100008 | medical |
| 9 | Nala | 2 | *NULL* | F | 2024-03-01 | 2.9 | *NULL* | quarantine |
| 10 | Thumper | 3 | Lop | M | 2023-06-15 | 1.8 | *NULL* | adopted |
| 11 | Zoe | 1 | Mixed | F | 2016-01-01 | 22.0 | 985100011 | adopted |
| 12 | Oscar | 2 | Persian | M | 2021-12-12 | 5.5 | 985100012 | available |
| 13 | Rex | 1 | Rottweiler | M | 2017-08-08 | 38.7 | 985100013 | available |
| 14 | Lily | 2 | *NULL* | F | *NULL* | 3.4 | *NULL* | available |
| 15 | Charlie | 1 | Poodle | M | 2023-10-10 | 7.2 | 985100015 | adopted |
| 16 | Kiwi | 4 | Budgie | F | *NULL* | 0.04 | *NULL* | adopted |
| 17 | Daisy | 1 | Mixed | F | 2020-04-04 | 15.6 | 985100017 | deceased |
| 18 | Felix | 2 | Tabby | M | 2019-02-14 | 5.0 | 985100018 | available |
| 19 | Bunny | 3 | *NULL* | F | 2024-01-01 | 1.5 | *NULL* | available |
| 20 | Shadow | 1 | Husky | M | 2021-06-30 | 25.1 | 985100020 | available |

---

## intake

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `intake_id` | INTEGER | 🔑 PK |  |
| `animal_id` | INTEGER | 🔗 FK → `animal(animal_id)` | חובה (NOT NULL). |
| `intake_date` | TEXT |  | חובה (NOT NULL). |
| `intake_type` | TEXT |  | חובה (NOT NULL). 'stray' / 'surrender' / 'transfer' |
| `brought_by` | INTEGER | 🔗 FK → `person(person_id)` | volunteer or previous owner |
| `location` | TEXT |  | where found (strays only) |
| `reason` | TEXT |  | why surrendered (surrenders only) |

**הנתונים (21 שורות):**

| intake_id 🔑 | animal_id 🔗 | intake_date | intake_type | brought_by 🔗 | location | reason |
|---|---|---|---|---|---|---|
| 1 | 1 | 2023-03-14 | stray | 2 | Herzl St, Haifa | *NULL* |
| 2 | 2 | 2023-04-02 | surrender | 7 | *NULL* | moving abroad |
| 3 | 3 | 2023-05-20 | stray | 3 | Carmel beach | *NULL* |
| 4 | 4 | 2023-06-11 | stray | 2 | Hadar market | *NULL* |
| 5 | 5 | 2023-07-07 | surrender | 6 | *NULL* | owner passed away |
| 6 | 6 | 2023-08-19 | stray | 11 | Tirat Carmel park | *NULL* |
| 7 | 7 | 2023-09-30 | surrender | 8 | *NULL* | allergy in family |
| 8 | 8 | 2023-11-05 | stray | 3 | Route 4 shoulder | *NULL* |
| 9 | 9 | 2024-01-22 | stray | 2 | Bat Galim | *NULL* |
| 10 | 10 | 2024-02-14 | surrender | 9 | *NULL* | child lost interest |
| 11 | 11 | 2024-03-03 | transfer | *NULL* | *NULL* | transfer from Akko shelter |
| 12 | 12 | 2024-04-18 | stray | 11 | Neve Shaanan | *NULL* |
| 13 | 13 | 2024-05-25 | surrender | 10 | *NULL* | too big for apartment |
| 14 | 14 | 2024-07-09 | stray | 2 | Kiryat Eliezer | *NULL* |
| 15 | 15 | 2024-08-30 | stray | 3 | Grand Canyon mall | *NULL* |
| 16 | 16 | 2024-10-12 | surrender | 12 | *NULL* | cannot afford |
| 17 | 17 | 2024-11-01 | stray | 11 | Wadi Nisnas | *NULL* |
| 18 | 18 | 2025-01-15 | transfer | *NULL* | *NULL* | transfer from Nahariya shelter |
| 19 | 19 | 2025-02-20 | stray | 2 | Technion campus | *NULL* |
| 20 | 20 | 2025-03-08 | surrender | 7 | *NULL* | moving abroad |
| 21 | 1 | 2024-06-01 | surrender | 6 | *NULL* | returned by adopter - allergy |

---

## vaccine_type

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `vaccine_type_id` | INTEGER | 🔑 PK |  |
| `name` | TEXT |  | חובה (NOT NULL). |
| `species_id` | INTEGER | 🔗 FK → `species(species_id)` | חובה (NOT NULL). |
| `interval_months` | INTEGER |  | NULL = one-time |

**הנתונים (5 שורות):**

| vaccine_type_id 🔑 | name | species_id 🔗 | interval_months |
|---|---|---|---|
| 1 | Rabies | 1 | 12 |
| 2 | DHPP | 1 | 12 |
| 3 | Rabies | 2 | 12 |
| 4 | FVRCP | 2 | 12 |
| 5 | Myxomatosis | 3 | 6 |

---

## vaccination

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `vaccination_id` | INTEGER | 🔑 PK |  |
| `animal_id` | INTEGER | 🔗 FK → `animal(animal_id)` | חובה (NOT NULL). |
| `vaccine_type_id` | INTEGER | 🔗 FK → `vaccine_type(vaccine_type_id)` | חובה (NOT NULL). |
| `vet_id` | INTEGER | 🔗 FK → `person(person_id)` | חובה (NOT NULL). |
| `given_date` | TEXT |  | חובה (NOT NULL). |
| `cost` | REAL |  | חובה (NOT NULL). |

**הנתונים (28 שורות):**

| vaccination_id 🔑 | animal_id 🔗 | vaccine_type_id 🔗 | vet_id 🔗 | given_date | cost |
|---|---|---|---|---|---|
| 1 | 1 | 1 | 4 | 2023-03-20 | 80.0 |
| 2 | 1 | 2 | 4 | 2023-03-20 | 95.0 |
| 3 | 2 | 3 | 5 | 2023-04-08 | 80.0 |
| 4 | 2 | 4 | 5 | 2023-04-08 | 90.0 |
| 5 | 3 | 1 | 4 | 2023-05-25 | 80.0 |
| 6 | 3 | 2 | 4 | 2023-05-25 | 95.0 |
| 7 | 4 | 3 | 5 | 2023-06-15 | 80.0 |
| 8 | 5 | 1 | 4 | 2023-07-12 | 80.0 |
| 9 | 6 | 3 | 5 | 2023-08-24 | 80.0 |
| 10 | 6 | 4 | 5 | 2023-08-24 | 90.0 |
| 11 | 8 | 1 | 4 | 2023-11-10 | 80.0 |
| 12 | 8 | 2 | 4 | 2023-11-10 | 95.0 |
| 13 | 10 | 5 | 5 | 2024-02-20 | 60.0 |
| 14 | 11 | 1 | 4 | 2024-03-08 | 80.0 |
| 15 | 12 | 3 | 5 | 2024-04-22 | 80.0 |
| 16 | 12 | 4 | 5 | 2024-04-22 | 90.0 |
| 17 | 13 | 1 | 4 | 2024-05-30 | 80.0 |
| 18 | 13 | 2 | 4 | 2024-05-30 | 95.0 |
| 19 | 1 | 1 | 4 | 2024-06-05 | 85.0 |
| 20 | 15 | 1 | 4 | 2024-09-04 | 85.0 |
| 21 | 15 | 2 | 4 | 2024-09-04 | 100.0 |
| 22 | 17 | 1 | 5 | 2024-11-06 | 85.0 |
| 23 | 18 | 3 | 5 | 2025-01-20 | 85.0 |
| 24 | 19 | 5 | 5 | 2025-02-25 | 65.0 |
| 25 | 20 | 1 | 4 | 2025-03-12 | 85.0 |
| 26 | 20 | 2 | 4 | 2025-03-12 | 100.0 |
| 27 | 3 | 1 | 4 | 2024-05-28 | 85.0 |
| 28 | 3 | 1 | 4 | 2025-05-30 | 85.0 |

---

## adoption

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `adoption_id` | INTEGER | 🔑 PK |  |
| `animal_id` | INTEGER | 🔗 FK → `animal(animal_id)` | חובה (NOT NULL). |
| `adopter_id` | INTEGER | 🔗 FK → `person(person_id)` | חובה (NOT NULL). |
| `adoption_date` | TEXT |  | חובה (NOT NULL). |
| `fee_paid` | REAL |  | חובה (NOT NULL). |
| `returned_date` | TEXT |  | NULL unless the animal came back |

**הנתונים (9 שורות):**

| adoption_id 🔑 | animal_id 🔗 | adopter_id 🔗 | adoption_date | fee_paid | returned_date |
|---|---|---|---|---|---|
| 1 | 1 | 6 | 2023-05-10 | 300.0 | 2024-06-01 |
| 2 | 2 | 7 | 2023-06-15 | 200.0 | *NULL* |
| 3 | 5 | 8 | 2024-02-10 | 200.0 | *NULL* |
| 4 | 6 | 9 | 2024-05-05 | 250.0 | *NULL* |
| 5 | 10 | 9 | 2024-06-20 | 100.0 | *NULL* |
| 6 | 11 | 10 | 2024-08-15 | 200.0 | *NULL* |
| 7 | 1 | 12 | 2025-07-01 | 400.0 | *NULL* |
| 8 | 15 | 6 | 2024-12-01 | 400.0 | *NULL* |
| 9 | 16 | 8 | 2025-01-10 | 150.0 | *NULL* |

---

## expense

**המבנה:**

| עמודה | טיפוס | מפתח | הערה |
|---|---|---|---|
| `expense_id` | INTEGER | 🔑 PK |  |
| `expense_date` | TEXT |  | חובה (NOT NULL). |
| `category` | TEXT |  | חובה (NOT NULL). 'food' / 'medical' / 'supplies' / 'utilities' / 'maintenance' |
| `amount` | REAL |  | חובה (NOT NULL). |
| `animal_id` | INTEGER | 🔗 FK → `animal(animal_id)` | NULL = general |
| `description` | TEXT |  |  |

**הנתונים (22 שורות):**

| expense_id 🔑 | expense_date | category | amount | animal_id 🔗 | description |
|---|---|---|---|---|---|
| 1 | 2024-01-05 | food | 1850.0 | *NULL* | dry food, 20 sacks |
| 2 | 2024-01-12 | medical | 420.0 | 8 | x-ray + medication |
| 3 | 2024-01-31 | utilities | 960.0 | *NULL* | electricity January |
| 4 | 2024-02-03 | medical | 650.0 | 5 | dental cleaning |
| 5 | 2024-02-18 | supplies | 310.0 | *NULL* | cat litter |
| 6 | 2024-02-28 | utilities | 880.0 | *NULL* | electricity February |
| 7 | 2024-03-10 | medical | 1200.0 | 13 | neutering surgery |
| 8 | 2024-03-15 | food | 1790.0 | *NULL* | dry food, 20 sacks |
| 9 | 2024-04-02 | maintenance | 540.0 | *NULL* | kennel door repair |
| 10 | 2024-04-20 | medical | 380.0 | 9 | blood tests |
| 11 | 2024-05-08 | medical | 275.0 | 12 | deworming |
| 12 | 2024-05-30 | utilities | 910.0 | *NULL* | electricity May |
| 13 | 2024-06-14 | medical | 890.0 | 1 | allergy treatment after return |
| 14 | 2024-07-01 | food | 1900.0 | *NULL* | dry food, 20 sacks |
| 15 | 2024-08-22 | medical | 2100.0 | 8 | leg surgery |
| 16 | 2024-09-09 | supplies | 220.0 | *NULL* | leashes and bowls |
| 17 | 2024-10-17 | medical | 450.0 | 17 | emergency visit |
| 18 | 2024-11-03 | medical | 175.0 | 20 | microchip |
| 19 | 2024-12-12 | utilities | 1020.0 | *NULL* | electricity December |
| 20 | 2025-01-20 | medical | 330.0 | 18 | eye infection |
| 21 | 2025-02-05 | food | 1950.0 | *NULL* | dry food, 20 sacks |
| 22 | 2025-03-14 | medical | 600.0 | 3 | hip x-ray |

</div>
