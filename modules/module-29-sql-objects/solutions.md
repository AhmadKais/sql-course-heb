<div dir="rtl">

# מודול 29 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 הפלטים אמיתיים (SQLite). תוכניות ביצוע עשויות להיראות מעט שונה בגרסאות אחרות.

---

## ✅ תרגיל 1 — מזהים אוטומטיים

**א.** D קיבל **3** — המספר של C, שנמחק, **מוחזר לשימוש**.

**ב.** עם `AUTOINCREMENT`, D קיבל **4**. ב‑`sqlite_sequence`: `donation | 4`.

**ג.**

</div>

```sql
INSERT INTO animal (name, species_id, sex, status) VALUES ('Milo', 2, 'M', 'quarantine');
SELECT last_insert_rowid();                          -- 21

INSERT INTO intake (animal_id, intake_date, intake_type)
VALUES (last_insert_rowid(), '2026-09-21', 'stray');   -- Milo's id, without guessing
```

<div dir="rtl">

> ⚠️ **שימו לב:** אחרי ה‑`INSERT` לקליטה, `last_insert_rowid()` כבר מחזיר את מזהה **הקליטה**. אם צריך את מזהה החיה לעוד פעולות — שמרו אותו קודם (באפליקציה, במשתנה).

**ד.** שני פקידים מקבלים חיה באותה שנייה. שניהם קוראים `MAX = 20`, ושניהם מנסים להכניס 21. אחד מצליח, השני מקבל שגיאת `UNIQUE` — או, אם אין מפתח ראשי, **שתי חיות עם מספר 21**. Sequence / `AUTOINCREMENT` מחלק מספרים **בתוך** בסיס הנתונים, אחד‑אחד, ולכן לעולם לא נותן את אותו מספר פעמיים.

---

## ✅ תרגיל 2 — Sequence ב‑Oracle

</div>

```sql
-- a
CREATE SEQUENCE donation_seq START WITH 1000 INCREMENT BY 1 NOCACHE;

-- b
INSERT INTO donation (donation_id, donor_name, amount)
VALUES (donation_seq.NEXTVAL, 'Haifa Rotary', 5000);

INSERT INTO receipt (receipt_id, donation_id, issued_date)
VALUES (receipt_seq.NEXTVAL, donation_seq.CURRVAL, SYSDATE);   -- CURRVAL = the same donation

-- c
CREATE TABLE donation (
  donation_id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1000) PRIMARY KEY,
  donor_name  VARCHAR2(100) NOT NULL,
  amount      NUMBER(10,2)  NOT NULL
);
```

<div dir="rtl">

---

## ✅ תרגיל 3 — אינדקסים

**א.** לפני: `SCAN animal`. אחרי `CREATE INDEX idx_animal_name ON animal(name);` ⟵ `SEARCH animal USING INDEX idx_animal_name (name=?)`.

**ב.**

</div>

```text
sqlite_autoindex_species_1   <- UNIQUE on species.name
sqlite_autoindex_animal_1    <- UNIQUE on animal.chip_number
idx_animal_name              <- ours
```

<div dir="rtl">

**האינדקסים האוטומטיים** נוצרו מאילוצי `UNIQUE` — כדי לבדוק כפילויות מהר. (`PRIMARY KEY` מסוג `INTEGER` ב‑SQLite הוא ה‑rowid עצמו — אינדקס מובנה.)

**ג.** `SCAN vaccination` ⟵ `CREATE INDEX idx_vacc_animal ON vaccination(animal_id);` ⟵ `SEARCH vaccination USING INDEX idx_vacc_animal (animal_id=?)`.

**ד.**

</div>

```text
before:  |--SCAN v                                         <- every vaccination row
         `--SEARCH a USING INTEGER PRIMARY KEY (rowid=?)

after:   |--SEARCH a USING COVERING INDEX idx_animal_name (name=?)   <- find Rocky
         `--SEARCH v USING INDEX idx_vacc_animal (animal_id=?)       <- jump to his shots
```

<div dir="rtl">

**לפני:** עובר על **כל** החיסונים, ולכל אחד בודק אם החיה היא Rocky. **אחרי:** מוצא את Rocky באינדקס, וקופץ ישר לחיסונים שלו. על 28 שורות — אותו זמן. על 10 מיליון — שניות מול אלפיות.

> 💡 **COVERING INDEX** — כל מה שהשאילתה צריכה מ‑`animal` (`name` ו‑`animal_id`) נמצא **באינדקס עצמו**, אז אפילו לא צריך לקרוא את הטבלה.

---

## ✅ תרגיל 4 — מתי אינדקס לא עוזר

**א.** האינדקס ממוין לפי `name`, לא לפי `UPPER(name)`. בשביל להשוות, SQLite צריך לחשב `UPPER` לכל שורה ⟵ `SCAN`. **תיקון:** `CREATE INDEX idx_animal_upper_name ON animal(UPPER(name));` ⟵ `SEARCH … (<expr>=?)`.

**ב.** אינדקס ממוין לפי **תחילת** הערך. "מסתיים ב‑na" יכול להיות בכל מקום ברשימה הממוינת — אין לאן לקפוץ.

**ג.**

</div>

```sql
EXPLAIN QUERY PLAN SELECT * FROM expense WHERE STRFTIME('%Y', expense_date) = '2024';
-- SCAN expense         <- even with an index on expense_date: a function on the column

-- rewrite: a range on the column itself
EXPLAIN QUERY PLAN SELECT * FROM expense WHERE expense_date BETWEEN '2024-01-01' AND '2024-12-31';
-- SEARCH expense USING INDEX idx_exp_date (expense_date>? AND expense_date<?)
```

<div dir="rtl">

> 🔑 **"פונקציה על העמודה" ⟵ "טווח על העמודה".** במקום `STRFTIME('%Y', d) = '2024'` — `d >= '2024-01-01' AND d < '2025-01-01'`. אותה תשובה, ואינדקס רגיל עובד. זו אחת מהטכניקות החשובות בכתיבת שאילתות מהירות.

**ד.**

| העמודה | אינדקס? | למה |
|--------|---------|-----|
| `chip_number` | ✅ (כבר יש — `UNIQUE`) | חיפוש מדויק, ערכים ייחודיים |
| `vaccination.animal_id` | ✅ | מפתח זר — כל JOIN |
| `expense.expense_date` | ✅ | דוחות לפי תקופה (טווח) |
| `name` | ✅ כנראה | מחפשים לפי שם הרבה |
| `status` | ⚠️ תלוי | 5 ערכים בלבד. שווה רק אם מחפשים ערך **נדיר** (`medical`) |
| `sex` | ❌ | 3 ערכים, כל אחד שליש מהטבלה — אינדקס לא חוסך כלום |

---

## ✅ תרגיל 5 — ראיון בכיתה

</div>

```sql
-- a
SELECT a.name, a.species_id, a.weight_kg
FROM   animal a
WHERE  a.weight_kg = (SELECT MAX(b.weight_kg) FROM animal b WHERE b.species_id = a.species_id)
ORDER  BY a.species_id;
```

```text
name     species_id  weight_kg
-------  ----------  ---------
Rex      1           38.7
Oscar    2           5.5
Thumper  3           1.8
Coco     4           0.1
```

```sql
-- b1   31.0
SELECT MAX(weight_kg) FROM animal
WHERE  weight_kg < (SELECT MAX(weight_kg) FROM animal);

-- b2   Rocky 31.0
SELECT name, weight_kg FROM animal ORDER BY weight_kg DESC LIMIT 1 OFFSET 1;
```

<div dir="rtl">

> 💡 **ההבדל בין שתי הדרכים:** אם שתי חיות שוקלות 38.7, `OFFSET 1` יחזיר את **השנייה מהן** (38.7), ו‑`MAX … < MAX` יחזיר את **הערך השני** (31.0). מראיין טוב ישאל בדיוק את זה — "ומה אם יש שוויון?"

</div>

```sql
-- c   Luna 3, Rocky 4
SELECT a.name, COUNT(*)
FROM   animal a
JOIN   vaccination v ON v.animal_id = a.animal_id
GROUP  BY a.animal_id
HAVING COUNT(*) > 2;
```

<div dir="rtl">

**ד. שלוש הטעויות** בשאילתה מסעיף 9.3:
1. **`WHERE COUNT(*) > 2`** — פונקציה מצרפית ב‑`WHERE`. צריך `HAVING`.
2. **אין `GROUP BY`** — בלי קיבוץ, `COUNT(*)` סופר את כל השורות כקבוצה אחת.
3. **`name` לבד** — לא ברור אם `a.name` (ובשאילתה עם JOIN — תמיד כינוי). ובלי `GROUP BY` על החיה — עמודה רגילה ליד מצרפית.

התיקון = סעיף ג'.

**ה.** תשובה טובה, בשלושה משפטים: *"אינדקס הוא עותק ממוין של עמודה, כמו אינדקס בסוף ספר — הוא מאפשר לקפוץ ישר לשורות במקום לסרוק את כל הטבלה. אבל כל `INSERT` ו‑`UPDATE` צריך לעדכן גם את האינדקס, והוא תופס מקום. לכן שמים אינדקס על עמודות שמחפשים ומחברים לפיהן — בעיקר מפתחות זרים — ולא על כל עמודה."*

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[❓ לשאלות](questions.md)**

</div>

</div>
