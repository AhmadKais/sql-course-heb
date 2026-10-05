<div dir="rtl">

# מודול 30 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא ניסיתם בעצמכם — [חזרו לתרגילים](exercises.md).

---

## ✅ תרגיל 1 — מי צריך מה

| המשתמש | אובייקט | הרשאות |
|---------|---------|---------|
| מנהלת | כל הטבלאות | כולן (בעלת הסכמה) |
| וטרינר | `animal` | `SELECT`, `UPDATE (weight_kg, status)` |
| | `vaccination`, `treatment` | `SELECT`, `INSERT` |
| | `vaccine_type` | `SELECT` |
| מתנדבת | `available_animal` (View) | `SELECT` |
| | `public_person` (View) | `SELECT` |
| | `walk` | `INSERT` |
| רואה חשבון | `expense`, `donation` | `SELECT` |
| | View על `adoption` בלי שמות | `SELECT` |
| האתר | `available_animal` (View) | `SELECT` — **ותו לא** |

> 💡 **שימו לב: אף אחד חוץ מהמנהלת לא מקבל `DELETE`.** חיה שמתה — `UPDATE status` (מחיקה רכה, מודול 25). ורואה החשבון רק **קורא** — הוא לא אמור לשנות את מה שהוא מבקר.

---

## ✅ תרגיל 2 — GRANT ו‑REVOKE

</div>

```sql
-- a
CREATE USER tamar IDENTIFIED BY "Tam@r2026!";
GRANT CREATE SESSION TO tamar;

-- b
GRANT SELECT ON shelter.species TO tamar;

-- c
GRANT SELECT                    ON shelter.animal      TO dr_maya;
GRANT SELECT, INSERT            ON shelter.vaccination TO dr_maya;
GRANT UPDATE (weight_kg, status) ON shelter.animal     TO dr_maya;

-- d
ALTER USER tamar ACCOUNT LOCK;
```

<div dir="rtl">

**ד. `ACCOUNT LOCK`.** `DROP USER` מוחק את המשתמש — ואם יש רישומים שמזכירים אותו (מי הכניס איזה חיסון, יומני ביקורת), הקשר אובד. נעילה מונעת כניסה, ושומרת את ההיסטוריה. ואם תמר חוזרת בעוד שנה — `ACCOUNT UNLOCK`.

**ה.** נועה יכולה לתת את הגישה ל‑`person` — כולל טלפונים — **לכל** משתמש אחר, בלי שמנהלת המערכת תדע. השליטה על מי רואה מידע אישי יוצאת מהידיים. **ובכלל — מתנדבת לא צריכה `person`, רק `public_person`.**

---

## ✅ תרגיל 3 — Roles ו‑Views

</div>

```sql
-- a
CREATE ROLE vet_role;
GRANT CREATE SESSION            TO vet_role;
GRANT SELECT          ON shelter.animal       TO vet_role;
GRANT SELECT, INSERT  ON shelter.vaccination  TO vet_role;
GRANT SELECT          ON shelter.vaccine_type TO vet_role;
GRANT vet_role TO dr_ron;
GRANT vet_role TO dr_maya;

-- b   two commands: create the user, give the role
CREATE USER dr_lina IDENTIFIED BY "L1na!Vet2026";
GRANT vet_role TO dr_lina;

-- c
CREATE VIEW adoption_finance AS
SELECT adoption_id, adoption_date, fee_paid          -- no adopter_id, no names
FROM   adoption;

CREATE ROLE accountant_role;
GRANT CREATE SESSION                     TO accountant_role;
GRANT SELECT ON shelter.adoption_finance TO accountant_role;
GRANT SELECT ON shelter.expense          TO accountant_role;
```

<div dir="rtl">

**ד.** `ORA-00942: table or view does not exist`. ל‑`volunteer_role` אין שום הרשאה על `person` — ו‑Oracle **לא מאשר אפילו שהטבלה קיימת** למי שאין לו גישה אליה. זה מכוון: הודעת "אין לך הרשאה" הייתה מגלה לתוקף "יש כאן טבלה בשם person, שווה לנסות". "לא קיימת" — לא מגלה כלום.

---

## ✅ תרגיל 4 — GLOB

</div>

```sql
-- a   Bella, Bunny, Charlie, Coco, Daisy, Felix, Kiwi, Lily, Luna, Max, Mitzi
SELECT name FROM animal WHERE name GLOB '[A-M]*' ORDER BY name;

-- b   Rocky, Lily, Daisy, Bunny
SELECT name FROM animal WHERE name GLOB '*y';

-- c   Simba, Rocky, Mitzi, Bella, Oscar, Daisy, Felix, Bunny
SELECT name FROM animal WHERE name GLOB '?????';

-- d   German Shepherd
SELECT DISTINCT breed FROM animal WHERE breed GLOB '* *';

-- e   the four "dry food, 20 sacks"
SELECT description FROM expense WHERE description GLOB '*[0-9]*';

-- f
SELECT name FROM animal WHERE name LIKE 'l%';      -- Luna, Lily
SELECT name FROM animal WHERE name GLOB 'l*';      -- (no rows)
```

<div dir="rtl">

**ו.** `LIKE` ב‑SQLite **לא רגיש** לאותיות גדולות/קטנות (עבור אותיות לטיניות) — `'l%'` מוצא את `Luna`. `GLOB` **רגיש** — `'l*'` מחפש שם שמתחיל ב‑`l` קטנה, ואין כזה.

---

## ✅ תרגיל 5 — תבניות לבדיקת נתונים

</div>

```sql
-- a   only Omer (phone is NULL)
SELECT first_name, phone
FROM   person
WHERE  phone IS NULL
   OR  phone NOT GLOB '05[0-9]-[0-9][0-9][0-9][0-9][0-9][0-9][0-9]';

-- b   (no rows) -- all 13 chips are valid
SELECT name, chip_number
FROM   animal
WHERE  chip_number NOT GLOB '985[0-9][0-9][0-9][0-9][0-9][0-9]';
```

<div dir="rtl">

> ⚠️ **בסעיף א' — `phone IS NULL OR`** חשוב: `NULL NOT GLOB …` הוא "לא ידוע", לא true — בלי ה‑`OR`, Omer לא היה מופיע. (אותה מלכודת כמו `NOT IN` במודול 24.) בסעיף ב' זה בכוונה לא נכלל — חיה בלי שבב היא לא "שבב לא תקין".

</div>

```sql
-- c   Oracle
--   ^[0-9]{4}-[0-9]{2}-[0-9]{2}$          the shape  YYYY-MM-DD
--   better: month 01-12, day 01-31
--   ^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$
ALTER TABLE animal ADD CONSTRAINT chk_birth_date_format
  CHECK (birth_date IS NULL
         OR REGEXP_LIKE(birth_date, '^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'));
-- (in real Oracle, birth_date would be a DATE column -- and then no regex is needed)

-- d   Oracle
SELECT first_name, REGEXP_REPLACE(phone, '[^0-9]', '') AS digits FROM person;
-- 052-1111111 -> 0521111111
```

<div dir="rtl">

> 💡 **שימו לב ל‑`(0[1-9]|1[0-2])`** — "0 ואחריו 1–9, **או** 1 ואחריו 0–2". זה החודשים 01–12. Regex יודע לתאר את הצורה, לא את המשמעות: `2023-02-31` עדיין יעבור. לכן — טיפוס `DATE` אמיתי, כשיש.

---

## ✅ תרגיל 6 — חיפוש עבודה

אין תשובה אחת. **דוגמה לסעיף ב':**

> *"תכננתי ובניתי בסיס נתונים למקלט בעלי חיים: ERD של 8 ישויות, נרמול לצורה נורמלית שלישית, ומימוש ב‑SQLite עם מפתחות זרים, אילוצי CHECK ו‑Views. כתבתי שאילתות דוחות (JOIN, GROUP BY, תתי‑שאילתות) שעונות על שאלות של הנהלת המקלט — כמו עלות ממוצעת לחיה וחיסונים שעבר מועדם. הקוד והתיעוד ב‑GitHub: …"*

**מה עושה אותה טובה:** מספרים (8 ישויות), מונחים מקצועיים שמעסיקים מחפשים (ERD, נרמול, JOIN, Views), **תוצאה עסקית** (מה השאילתות עונות), וקישור.

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[❓ לשאלות](questions.md)**

</div>

</div>
