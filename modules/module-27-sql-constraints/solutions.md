<div dir="rtl">

# מודול 27 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 הפלטים אמיתיים, מהרצה ב‑SQLite אחרי `shelter.sql` ו‑`PRAGMA foreign_keys = ON;`.

---

## ✅ תרגיל 1 — לזהות אילוצים

**א.** **`NOT NULL`:** `name` (לכל חיה יש שם), `species_id` (כל חיה ממין כלשהו), `sex` (גם "לא ידוע" הוא ערך — `'U'`), `status`. **מותר NULL:** `breed` (חיה מעורבת / לא ידוע), `birth_date` (משוטטת — לא יודעים מתי נולדה), `chip_number` (לא לכל חיה יש שבב), `weight_kg`.

**ב.** `sex TEXT NOT NULL CHECK (sex IN ('M','F','U'))` — מין רק מתוך שלושה ערכים.

**ג.** `species.name UNIQUE` (אין שני מינים בשם "Dog"), `animal.chip_number UNIQUE` (שבב אחד = חיה אחת).

**ד.** `animal.status` — אין `CHECK`, אז אפשר להכניס `'adoptd'` (שגיאת כתיב) או `'Adopted'`, וכל שאילתה עם `WHERE status = 'adopted'` תפספס אותם. אותו דבר ל‑`person.role`, `intake.intake_type` ו‑`expense.category`.

---

## ✅ תרגיל 2 — UNIQUE ו‑NULL

**א.** **שתיהן נכנסו.** NULL = "לא ידוע", ושני "לא ידוע" אינם בהכרח שווים — אז אין הפרה של ייחודיות.

**ב.** `UNIQUE constraint failed: contact.email`.

**ג.** אותו עיקרון: 7 ה‑NULL‑ים לא "מתנגשים" זה בזה. `UNIQUE` אוכף ייחודיות **רק בין ערכים שקיימים**. בדיוק מה שהמקלט צריך: לחיה בלי שבב — אין בעיה; שתי חיות עם **אותו** שבב — טעות.

---

## ✅ תרגיל 3 — CHECK

**א.**

</div>

```text
UNIQUE constraint failed: kennel.code
CHECK constraint failed: chk_kennel_size
CHECK constraint failed: chk_kennel_cap
```

```sql
-- b
CREATE TABLE w (weight_kg REAL CHECK (weight_kg > 0));
INSERT INTO w VALUES (NULL);      -- accepted
INSERT INTO w VALUES (-1);        -- CHECK constraint failed: weight_kg > 0
SELECT COUNT(*) FROM w;           -- 1
```

<div dir="rtl">

**ב.** `NULL > 0` הוא "לא ידוע" — ו‑`CHECK` **נכשל רק כשהתנאי false**. "לא ידוע" עובר. כדי לחסום גם NULL — `NOT NULL` בנוסף.

</div>

```sql
-- c
CREATE TABLE expense_v2 (
  expense_id INTEGER PRIMARY KEY,
  animal_id  INTEGER REFERENCES animal(animal_id),
  category   TEXT NOT NULL,
  amount     REAL NOT NULL,
  CONSTRAINT chk_medical_animal CHECK (category <> 'medical' OR animal_id IS NOT NULL)
);
INSERT INTO expense_v2 VALUES (1, NULL, 'food',    100);    -- OK
INSERT INTO expense_v2 VALUES (2, NULL, 'medical', 200);    -- CHECK constraint failed
```

<div dir="rtl">

> 💡 **איך קוראים `A OR B` כחוק:** "**או** שזו לא הוצאה רפואית, **או** שיש חיה" = "אם רפואית — אז יש חיה". זה התרגום הקבוע של "אם … אז …" ל‑`CHECK`.

**ד.** קודם בודקים מה קיים (מודול 24):

</div>

```sql
SELECT status FROM animal GROUP BY status;
-- adopted, available, deceased, medical, quarantine  -- all five, nothing else

CONSTRAINT chk_status CHECK (status IN ('available', 'adopted', 'medical', 'quarantine', 'deceased'))
```

<div dir="rtl">

ב‑SQLite אי אפשר `ALTER TABLE … ADD CONSTRAINT` — בונים טבלה חדשה ומעתיקים (`INSERT INTO animal_v2 SELECT … FROM animal` — כל 20 השורות עברו). ב‑Oracle: `ALTER TABLE animal ADD CONSTRAINT chk_status CHECK (…)` — ואם שורה קיימת מפרה את החוק, ה‑`ALTER` ייכשל.

---

## ✅ תרגיל 4 — מפתחות

**א.** `UNIQUE constraint failed: kennel_stay.animal_id, kennel_stay.from_date` — **"חיה לא מתחילה שתי שהיות באותו יום"**. המפתח הראשי המורכב הוא החוק.

**ב.** `CHECK constraint failed: chk_stay_dates`.

**ג.** **הצליח — 28 שורות.** אין בנתונים אף חיסון כפול (אותה חיה, אותו חיסון, אותו יום). אילו היה — כל ההעתקה הייתה נכשלת.

**ד.** `'2023-05-25'` ⟵ `UNIQUE constraint failed: v2.animal_id, v2.vaccine_type_id, v2.given_date`. `'2023-05-26'` ⟵ **נכנס** — יום אחר, צירוף אחר. (אם זה הגיוני רפואית — זו כבר שאלה ל‑`CHECK` אחר, או לווטרינר.)

---

## ✅ תרגיל 5 — מה קורה במחיקה

**ב.** הכלוב נמחק; השהייה של Rocky **נשארת**, עם `kennel_id` = NULL (`SET NULL`).

**ג.** קודם מוחקים את החיסונים והקליטות של Bunny — כי ל‑`vaccination` ול‑`intake` **אין** `CASCADE`, והם חוסמים. אחרי מחיקת Bunny — השהייה שלה **נמחקה אוטומטית** (`CASCADE`).

</div>

```text
animal_id  kennel_id  from_date
---------  ---------  ----------
3                     2023-05-20      <- only Rocky's stay is left
```

<div dir="rtl">

**ד.** אימוץ הוא **רשומה היסטורית וכספית** — מי אימץ, מתי, כמה שילם. אם חיה נמחקת בטעות, `CASCADE` ימחק גם את רישום התשלום, ודוח ההכנסות ישתנה בדיעבד. כאן **רוצים שהמחיקה תיחסם** — ובעצם לא למחוק חיות בכלל (מחיקה רכה, מודול 25).

---

## ✅ תרגיל 6 — קשת

**א.** רק התשלום הראשון (אימוץ 5 בלבד) נכנס. "גם וגם" ו"אף אחד" ⟵ `CHECK constraint failed: chk_arc`.

</div>

```sql
-- b
CONSTRAINT chk_intake_kind CHECK (
     (intake_type = 'stray'     AND location IS NOT NULL AND reason IS NULL)
  OR (intake_type = 'surrender' AND location IS NULL     AND reason IS NOT NULL)
  OR (intake_type = 'transfer'  AND location IS NULL)
)
```

<div dir="rtl">

בדיקה — שאילתה על הנתונים הקיימים:

</div>

```sql
SELECT intake_type, COUNT(*) AS total,
       SUM(location IS NOT NULL) AS has_location,
       SUM(reason   IS NOT NULL) AS has_reason
FROM   intake GROUP BY intake_type;
```

```text
intake_type  total  has_location  has_reason
-----------  -----  ------------  ----------
stray        11     11            0
surrender    8      0             8
transfer     2      0             2
```

<div dir="rtl">

כל 21 השורות עומדות בחוק (העתקה לטבלה עם האילוץ — הצליחה). קליטה `stray` בלי מיקום ועם סיבה ⟵ `CHECK constraint failed: chk_intake_kind`.

> 🔑 **זה טיפוסי משנה (מודול 4) בטבלה אחת**, ו‑`CHECK` הוא מה שמוודא שכל שורה "מתנהגת" לפי הטיפוס שלה.

---

## ✅ תרגיל 7 — הפרויקט שלכם

אין פתרון אחד. **דוגמה לטבלת "חוק ⟵ אילוץ":**

| החוק העסקי | האילוץ |
|-------------|---------|
| לכל לקוח מספר טלפון | `phone TEXT NOT NULL` |
| אין שני לקוחות עם אותו email | `CONSTRAINT uq_customer_email UNIQUE (email)` |
| הזמנה שייכת ללקוח קיים | `CONSTRAINT fk_order_customer FOREIGN KEY …` |
| כמות בהזמנה — לפחות 1 | `CONSTRAINT chk_item_qty CHECK (qty >= 1)` |
| לא יותר מ‑10 הזמנות פתוחות ללקוח | **לא ניתן ב‑`CHECK`** — דורש ספירת שורות (טריגר / אפליקציה) |

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[❓ לשאלות](questions.md)**

</div>

</div>
