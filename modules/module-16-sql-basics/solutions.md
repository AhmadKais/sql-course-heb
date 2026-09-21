<div dir="rtl">

# מודול 16 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 **כל הפלטים כאן הם אמיתיים** — הופקו מ‑`shelter.sql`. אם קיבלתם משהו אחר, בדקו שטענתם את הקובץ במלואו.

---

## ✅ תרגיל 1 — הסיור הראשון

### א.

</div>

```sql
SELECT * FROM species;
```

```text
species_id  name    adoption_fee
----------  ------  ------------
1           Dog     400.0
2           Cat     250.0
3           Rabbit  100.0
4           Parrot  150.0
```

<div dir="rtl">

**4 שורות.**

### ב.

</div>

```sql
SELECT * FROM person;
```

<div dir="rtl">

**7 עמודות:** `person_id` · `first_name` · `last_name` · `role` · `city` · `phone` · `joined_date`.
**12 שורות.** שימו לב שלעומר (`person_id = 10`) אין טלפון — NULL.

### ג.

</div>

```sql
SELECT * FROM animal;
```

<div dir="rtl">

**4 חיות בלי גזע:** Mitzi · Nala · Lily · Bunny. (בתצוגה — התא ריק. זה NULL.)

---

## ✅ תרגיל 2 — עמודות נבחרות

</div>

```sql
-- a
SELECT name, status
FROM   animal;

-- b
SELECT first_name, last_name, city
FROM   person;

-- c  -- same columns, different order in the result
SELECT city, first_name, last_name
FROM   person;

-- d
SELECT expense_date, category, amount
FROM   expense;
```

<div dir="rtl">

**פלט של ג'** (ראשונות):

</div>

```text
city          first_name  last_name
------------  ----------  ---------
Haifa         Ruti        Almog
Haifa         Noa         Peretz
Kiryat Ata    Amir        Levi
```

<div dir="rtl">

> 🔑 סדר העמודות בתוצאה = הסדר ב‑`SELECT`. לא הסדר בטבלה.

---

## ✅ תרגיל 3 — כינויים

</div>

```sql
-- a
SELECT name AS animal_name
FROM   animal;

-- b  -- a space in the alias needs double quotes
SELECT weight_kg AS "Weight (kg)"
FROM   animal;

-- c
SELECT fee_paid      AS paid_nis,
       adoption_date AS "date"
FROM   adoption;
```

<div dir="rtl">

### ד. בלי גרשיים

</div>

```sql
SELECT weight_kg AS Weight (kg) FROM animal;
```

```text
Error: near "(": syntax error
```

<div dir="rtl">

**למה:** בסיס הנתונים קרא `Weight` ככינוי, ואז נתקל ב‑`(` ולא ידע מה לעשות איתו. **המילה אחרי `near` היא המקום שבו הוא התבלבל** — והטעות היא ממש לפניה: הכינוי לא היה בגרשיים כפולות.

---

## ✅ תרגיל 4 — חישובים

</div>

```sql
-- a
SELECT name, weight_kg, weight_kg * 1000 AS weight_g
FROM   animal;

-- b
SELECT fee_paid, fee_paid * 1.18 AS with_vat
FROM   adoption;

-- c
SELECT amount, amount / 12 AS per_month
FROM   expense;
```

```text
-- a (first rows)
name     weight_kg  weight_g
-------  ---------  --------
Luna     18.5       18500.0
Simba    4.2        4200.0

-- b (first rows)
fee_paid  with_vat
--------  --------
300.0     354.0
200.0     236.0
```

<div dir="rtl">

### ד. חילוק שלמים

</div>

```sql
SELECT 10 / 4;      -- 2
SELECT 10 / 4.0;    -- 2.5
```

<div dir="rtl">

<div align="center">

**⚠️ שלם חלקי שלם = שלם. השארית נזרקת.**

</div>

`10 / 4` — שני מספרים **שלמים** ⟵ התוצאה שלם ⟵ `2`, לא `2.5`.
`10 / 4.0` — אחד מהם **עשרוני** ⟵ התוצאה עשרונית ⟵ `2.5`.

**למה זה חשוב:** `amount / 12` ב‑ג' עובד כי `amount` מוגדר כ‑`REAL`. אבל אם הייתם מחלקים עמודת `INTEGER` — הייתם מאבדים את השארית **בשקט**, בלי שגיאה. זו טעות שמסתתרת בדוחות כספיים.

> 💡 **בטיחות:** כשמחלקים — כתבו `12.0` ולא `12`. זה לא עולה כלום.

---

## ✅ תרגיל 5 — חיבור מחרוזות

</div>

```sql
-- a
SELECT first_name || ' ' || last_name AS full_name
FROM   person;

-- b
SELECT name || ' - ' || breed AS label
FROM   animal;

-- d
SELECT first_name || ' ' || last_name || ' (' || role || ')' AS label
FROM   person;
```

```text
-- b
label
------------------------
Luna - Mixed
Simba - Tabby
Rocky - Labrador
                          <- Mitzi: the whole thing is NULL
Bella - German Shepherd

-- d
label
-------------------------
Ruti Almog (volunteer)
Noa Peretz (volunteer)
Amir Levi (volunteer)
Dr. Ron Levi (vet)
```

<div dir="rtl">

### ג. מה קרה ל‑Mitzi

**השורה שלה ריקה לגמרי** — לא `Mitzi - `, אלא כלום.

**למה:** `breed` של Mitzi הוא NULL. `'Mitzi' || ' - ' || NULL` ⟵ **NULL מדביק** ⟵ הכול NULL. אפילו השם נעלם.

זו **הנקודה החשובה ביותר במודול**, ותפגשו אותה שוב ושוב. הפתרון — `COALESCE` — במודול 20.

---

## ✅ תרגיל 6 — DISTINCT

</div>

```sql
-- a
SELECT DISTINCT city FROM person;

-- b
SELECT DISTINCT category FROM expense;

-- c
SELECT DISTINCT species_id, status FROM animal;
```

```text
-- a: 7 cities
city
------------
Haifa
Kiryat Ata
Nesher
Tel Aviv
Karmiel
Tirat Carmel
Nahariya

-- b: 5 categories
category
-----------
food
medical
utilities
supplies
maintenance

-- c: 11 unique (species, status) pairs
species_id  status
----------  ----------
1           adopted
2           adopted
1           available
2           available
4           available
1           medical
2           quarantine
3           adopted
4           adopted
1           deceased
3           available
```

<div dir="rtl">

### ד. `DISTINCT name`

**20 שורות — בדיוק כמו בלי `DISTINCT`.**

**מה זה אומר על הנתונים:** אין שתי חיות עם אותו שם. **בינתיים.** ברגע שייכנס כלב שני בשם Max — `DISTINCT name` יחזיר 20 ו‑`name` יחזיר 21, וכל שאילתה שהסתמכה על "שם = חיה" תישבר.

> 🔑 **וזו הסיבה שהמזהה הוא `animal_id` ולא `name`** (מודול 6). השם ייחודי במקרה; המזהה ייחודי **בהגדרה**.

---

## ✅ תרגיל 7 — NULL בפעולה

</div>

```sql
-- a
SELECT name, chip_number FROM animal;

-- b
SELECT name, 'Chip: ' || chip_number AS chip_label FROM animal;
```

```text
-- a                          -- b
name    chip_number           name    chip_label
------  -----------           ------  ----------------
Luna    985100001             Luna    Chip: 985100001
Simba   985100002             Simba   Chip: 985100002
Rocky   985100003             Rocky   Chip: 985100003
Mitzi                         Mitzi                     <- NULL again
Bella   985100005             Bella   Chip: 985100005
```

<div dir="rtl">

**ב:** 8 חיות בלי שבב ⟵ 8 שורות ריקות ב‑`chip_label`. אותו מנגנון כמו בתרגיל 5.

**ג:** **3 חיות** בלי תאריך לידה — Coco, Lily, Kiwi. (ציפורים וחתולת רחוב — הגיוני שלא יודעים.)

### ד.

</div>

```sql
SELECT NULL + 5;         -- NULL
SELECT NULL || 'text';   -- NULL
SELECT NULL * 0;         -- NULL  (!)  even times zero
```

<div dir="rtl">

<div align="center">

**המשותף: כולם NULL. אין יוצא מן הכלל.**

</div>

השלישי מפתיע: `NULL * 0` — "הרי כל דבר כפול אפס הוא אפס!" **לא.** NULL אינו מספר; הוא "לא ידוע". ולא ידוע כפול אפס — עדיין לא ידוע.

---

## ✅ תרגיל 8 — לקרוא שגיאות

| | השאילתה | מה קורה | הסבר |
|---|----------|----------|-------|
| a | `wieght_kg` | ❌ `no such column: wieght_kg` | כתיב. `i` ו‑`e` הפוכים |
| b | בלי `;` | ⚠️ **תלוי בכלי.** Programiz: רץ. כלים אחרים: "incomplete input" | **תמיד** `;`. גם כשהכלי סולח |
| c | `"name"` בגרשיים כפולות | ✅ **רץ!** מחזיר את העמודה `name` | גרשיים כפולות = **שם**. `"name"` הוא שם עמודה קיים, אז זה עובד. אבל `"Luna"` היה נכשל |
| d | `breed, FROM` | ❌ `near "FROM": syntax error` | פסיק אחרי העמודה האחרונה |
| e | `Animal` באות גדולה | ✅ **רץ.** | SQL לא רגיש לאותיות בשמות (ב‑SQLite וב‑Oracle כאחד) |
| f | `\|\| breed` | ✅ **רץ** — אבל 4 שורות ריקות | לא שגיאה. **NULL מדביק.** זה "רץ אבל לא כמו שציפיתם" |

**השתיים שאינן שגיאות:** **c** ו‑**e** (ובמובן מסוים גם **f**).

> 🔑 **c היא המסוכנת ביותר.** היא עובדת **במקרה** — כי יש עמודה בשם `name`. `SELECT "Luna" FROM animal` **ייכשל** ב‑`no such column: Luna`. הכלל נשאר: **גרש בודד לערך, כפול לשם.**

---

## ✅ תרגיל 9 — הדוח לרותי

### א. בשלבים

</div>

```sql
-- step 1: what's there
SELECT * FROM animal;

-- step 2: only the columns she needs
SELECT name, sex, weight_kg, chip_number, status
FROM   animal;

-- step 3: glue them together
SELECT name || ' | ' || sex || ' | ' || weight_kg || ' kg | chip '
            || chip_number || ' | ' || status   AS line
FROM   animal;
```

```text
line
-------------------------------------------------
Luna | F | 18.5 kg | chip 985100001 | adopted
Simba | M | 4.2 kg | chip 985100002 | adopted
Rocky | M | 31.0 kg | chip 985100003 | available
                                                    <- Mitzi
Bella | F | 28.4 kg | chip 985100005 | adopted
Tom | M | 4.8 kg | chip 985100006 | adopted
                                                    <- Coco
```

<div dir="rtl">

### ב. חיות בלי שבב

**8 שורות ריקות לגמרי.** לא רק "chip" ריק — **כל השורה**, כולל השם. הדוח של רותי חסר 8 חיות.

### ג. למה, ומה צריך

**למה:** `chip_number` הוא NULL ⟵ החיבור כולו NULL. ראינו את זה שלוש פעמים כבר במודול הזה — וזו הפעם שבה זה **באמת** שובר משהו: דוח שנמסר ללקוחה עם 8 שורות חסרות.

**מה צריך:** דרך לומר *"אם `chip_number` ריק — תציג `'none'` במקום"*. הפונקציה הזאת נקראת `COALESCE` והיא במודול 20. עד אז — **דעו שהדוח הזה לא מוכן למסירה.**

### ד. עם פאונד

</div>

```sql
SELECT name || ' | ' || sex || ' | '
            || weight_kg || ' kg / ' || weight_kg * 2.2 || ' lb | chip '
            || chip_number || ' | ' || status   AS line
FROM   animal;
-- -> "Luna | F | 18.5 kg / 40.7 lb | chip 985100001 | adopted"
```

<div dir="rtl">

---

## ✅ תרגיל 10 — מפת הדרכים

| # | השאלה | אפשר עכשיו? | מה חסר |
|---|--------|-------------|---------|
| 1 | כל החיות | ✅ | `SELECT * FROM animal` |
| 2 | רק כלבים | ❌ | **`WHERE`** — מודול 17 |
| 3 | מהכבדה לקלה | ❌ | **`ORDER BY`** — מודול 18 |
| 4 | כמה חיות | ❌ | **`COUNT`** — מודול 23 |
| 5 | שם המין ולא המספר | ❌ | **`JOIN`** — מודול 21 |
| 6 | בלי שבב | ❌ | **`WHERE … IS NULL`** — מודול 17 |
| 7 | כמה עלה כל חיה | ❌ | **`JOIN` + `SUM` + `GROUP BY`** — מודולים 21, 23, 24 |
| 8 | שם מלא של מתנדבים | ⚠️ **חצי** | החיבור אפשר (`\|\|`); הסינון למתנדבים בלבד — **`WHERE`**, מודול 17 |

> 🎓 **שימו לב:** מתוך 8 שאלות פשוטות של רותי — עניתם על אחת. **אחרי מודול 17 תענו על ארבע.** אחרי 21 — על שבע. זה המסלול.

---

<div align="center">

### 🎯 סיימתם את מודול 16!

כתבתם SQL. הרצתם. קיבלתם שגיאות ותיקנתם. **זה כל ההבדל בין מי שיודע על SQL למי שיודע SQL.**
במודול הבא — `WHERE`: לבחור **אילו שורות**.

---

### ➡️ [מודול 17 — SQL: הגבלת השליפה](../module-17-sql-where/)

</div>

---

<div align="center">

**🧭 ניווט המודול**

</div>

| 📖 [חזרה למודול](README.md) | ❓ [שאלות ותשובות](questions.md) | ✏️ [לתרגילים](exercises.md) | 🏠 [דף הקורס](../../) |
|---|---|---|---|

</div>
