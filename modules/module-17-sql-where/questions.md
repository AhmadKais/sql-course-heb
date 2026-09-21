<div dir="rtl">

# מודול 17 — שאלות ותשובות

> נסחו תשובה — **והריצו** — לפני שאתם פותחים.

---

## 🟢 חלק א' — WHERE ואופרטורים

### שאלה 1
**מה `WHERE` עושה, ומה קורה לשורה שהתנאי שלה מחזיר NULL?**

<details><summary>💡 תשובה</summary>

`WHERE` בודק את התנאי **לכל שורה בנפרד**:

| התנאי מחזיר | השורה |
|-------------|--------|
| TRUE | נכנסת לתוצאה |
| FALSE | נופלת |
| **NULL** | **נופלת** — כמו FALSE |

הנקודה השלישית היא הקריטית: **NULL אינו TRUE**, ולכן שורה שהתנאי שלה "לא ידוע" — לא חוזרת. זו הסיבה שכל השוואה עם NULL מפילה שורות בשקט.

</details>

---

### שאלה 2
**מה יחזירו שתי השאילתות, ולמה?**

</div>

```sql
SELECT name FROM animal WHERE name = 'Luna';
SELECT name FROM animal WHERE name = 'luna';
```

<div dir="rtl">

<details><summary>💡 תשובה</summary>

| | תוצאה | למה |
|---|---|---|
| `'Luna'` | 1 שורה | התאמה מדויקת |
| `'luna'` | **0 שורות** | השוואת טקסט **רגישה לאותיות** — `'L'` ≠ `'l'` |

**מה כן לא רגיש:** מילות מפתח (`SELECT`/`select`) ושמות טבלאות ועמודות. **רק הערכים בגרשיים** רגישים.

⚠️ ואותו דבר לרווח בסוף: `'Luna '` ≠ `'Luna'`. אם השאילתה מחזירה 0 ואתם בטוחים שהערך קיים — זו הסיבה מספר 1.

</details>

---

### שאלה 3
**למה תאריכים חייבים להיות בפורמט `YYYY-MM-DD`?**

<details><summary>💡 תשובה</summary>

כי בבסיס הנתונים שלנו תאריכים הם **טקסט**, ו‑`<` על טקסט משווה **תו אחר תו משמאל**.

| הפורמט | `'20/11/2019' < '05/01/2020'`? |
|---------|-------------------------------|
| `DD/MM/YYYY` | ❌ **שקר** — כי `'2' > '0'` בתו הראשון |
| `YYYY-MM-DD` | ✅ `'2019-11-20' < '2020-01-05'` — אמת |

**`YYYY-MM-DD` הוא הפורמט היחיד שבו סדר הטקסט = סדר הזמן.** זה תקן ISO 8601. בבסיסי נתונים עם טיפוס `DATE` אמיתי (Oracle, PostgreSQL) הבעיה לא קיימת — אבל ב‑SQLite, ובכל מקום שתאריך נשמר כטקסט, זה הכלל.

</details>

---

### שאלה 4
**כתבו את המקבילה של כל אחת בלי `BETWEEN` ובלי `IN`:**

</div>

```sql
WHERE weight_kg BETWEEN 4 AND 6
WHERE status IN ('medical', 'quarantine')
```

<div dir="rtl">

<details><summary>💡 תשובה</summary>

</div>

```sql
WHERE weight_kg >= 4 AND weight_kg <= 6           -- BETWEEN is INCLUSIVE
WHERE status = 'medical' OR status = 'quarantine'
```

<div dir="rtl">

**שני דברים לזכור:**
- `BETWEEN` **כולל** את שני הקצוות — `>=` ו‑`<=`, לא `>` ו‑`<`
- `IN` הוא `OR` — ולכן הוא **בטוח יותר**: אין סכנת קדימויות עם `AND` שכן

</details>

---

## 🟡 חלק ב' — LIKE ו‑NULL

### שאלה 5
**מה ההבדל בין `%` ל‑`_` ב‑`LIKE`? תנו דוגמה שמבדילה.**

<details><summary>💡 תשובה</summary>

| התו | מתאים ל |
|------|----------|
| `%` | **כל מספר** של תווים — כולל אפס |
| `_` | **בדיוק תו אחד** |

**הדוגמה שמבדילה:**

</div>

```sql
WHERE name LIKE 'L%'     -- Luna, Lily, L, Leonardo -- anything starting with L
WHERE name LIKE 'L___'   -- Luna, Lily -- exactly 4 letters starting with L
WHERE name LIKE '___'    -- Tom, Max, Zoe, Rex -- exactly 3 letters
```

<div dir="rtl">

⚠️ **`LIKE` בלי `%` ובלי `_`** הוא בדיוק `=`. `LIKE 'Luna'` ≡ `= 'Luna'`.

</details>

---

### שאלה 6
**למה `WHERE chip_number = NULL` מחזיר 0 שורות, למרות ש‑7 חיות אין להן שבב?**

<details><summary>💡 תשובה</summary>

כי `chip_number = NULL` **לא מחזיר TRUE**. הוא מחזיר **NULL** — "לא ידוע".

<div align="center">

*"האם לא‑ידוע שווה ללא‑ידוע?"* — **לא ידוע.**

</div>

ו‑`WHERE` מכניס רק שורות שהתנאי שלהן TRUE. NULL ≠ TRUE ⟵ אף שורה.

**הדרך הנכונה:**

| מה רוצים | ❌ | ✅ |
|-----------|---|---|
| בלי ערך | `= NULL` | `IS NULL` |
| עם ערך | `<> NULL` | `IS NOT NULL` |

**ולמה זה מסוכן:** אין שגיאה. השאילתה רצה, מחזירה 0, ואתם חושבים שאין חיות בלי שבב.

</details>

---

### שאלה 7
**`> 5` מחזיר 10 שורות. `<= 5` מחזיר 10. יחד 20 — כל החיות. אבל `< '2020-01-01'` מחזיר 5 ו‑`>= '2020-01-01'` מחזיר 12. לאן נעלמו 3?**

<details><summary>💡 תשובה</summary>

**ל‑NULL.** לשלוש חיות (Coco, Lily, Kiwi) אין תאריך לידה.

- `NULL < '2020-01-01'` ⟵ NULL ⟵ השורה נופלת
- `NULL >= '2020-01-01'` ⟵ NULL ⟵ השורה נופלת

**הן לא באף קבוצה.** לא "לפני" ולא "אחרי" — פשוט לא נספרות.

לעומת זאת `weight_kg` **אין** בו NULL, ולכן `> 5` ו‑`<= 5` משלימים ל‑20.

> 🔑 **הכלל המעשי:** אם עמודה יכולה להכיל NULL, כל `WHERE` עליה **מדלג** על השורות האלה בשקט. לפעמים זה מה שרוצים; תמיד צריך לדעת. הפתרון: `OR column IS NULL` כשרוצים לכלול אותן.

</details>

---

### שאלה 8
**מה ההבדל בין NULL ב‑`SELECT` (מודול 16) לבין NULL ב‑`WHERE` (מודול 17)?**

<details><summary>💡 תשובה</summary>

אותו עיקרון — **NULL מדביק** — שתי השלכות:

| איפה | מה קורה | הדוגמה |
|-------|----------|---------|
| `SELECT` | הביטוי כולו הופך ל‑NULL | `'Chip: ' \|\| NULL` ⟵ תא ריק |
| `WHERE` | התנאי הופך ל‑NULL ⟵ **השורה נופלת** | `chip_number = NULL` ⟵ 0 שורות |

ב‑`SELECT` אתם **רואים** תא ריק ויודעים שמשהו קרה.
ב‑`WHERE` **השורה נעלמת** — ואין שום סימן. **זה המסוכן מבין השניים.**

</details>

---

## 🔴 חלק ג' — לוגיקה

### שאלה 9
**רותי רוצה "כלבים וחתולים זמינים". מה לא בסדר, וכמה שורות זה מחזיר?**

</div>

```sql
WHERE species_id = 1 OR species_id = 2 AND status = 'available'
```

<div dir="rtl">

<details><summary>💡 תשובה</summary>

**13 שורות במקום 7** — כולל לונה ובלה (מאומצות) ודייזי (מתה).

**למה:** `AND` גובר על `OR`. בסיס הנתונים קרא:

</div>

```text
species_id = 1  OR  (species_id = 2 AND status = 'available')
```

<div dir="rtl">

= **"כל הכלבים** + חתולים זמינים". ה‑`status` חל רק על החתולים.

**התיקון:**

</div>

```sql
WHERE (species_id = 1 OR species_id = 2) AND status = 'available'   -- 7 rows
-- or, better:
WHERE species_id IN (1, 2) AND status = 'available'
```

<div dir="rtl">

<div align="center">

**כשמערבבים `AND` ו‑`OR` — סוגריים. תמיד. גם כשבטוחים.**

</div>

</details>

---

### שאלה 10
**מה ההבדל בין שתי השאילתות?**

</div>

```sql
WHERE NOT status = 'adopted'
WHERE status <> 'adopted'
```

<div dir="rtl">

<details><summary>💡 תשובה</summary>

**בבסיס הנתונים שלנו — אין הבדל.** שתיהן מחזירות 12 שורות.

**אבל** יש הבדל עקרוני כשיש NULL:

| `status` | `NOT status = 'adopted'` | `status <> 'adopted'` |
|----------|--------------------------|------------------------|
| `'available'` | TRUE | TRUE |
| `'adopted'` | FALSE | FALSE |
| **NULL** | `NOT NULL` = NULL ⟵ נופלת | NULL ⟵ נופלת |

בפועל — זהות. **אבל `NOT` באמת שימושי כשמשלבים:** `NOT (a AND b)`, `NOT IN`, `NOT LIKE`, `NOT BETWEEN`.

</details>

---

### שאלה 11
**מה מסוכן ב‑`NOT IN` ומתי זה יכה?**

<details><summary>💡 תשובה</summary>

אם **אחד הערכים ברשימה הוא NULL** — `NOT IN` מחזיר **0 שורות**, תמיד.

</div>

```sql
WHERE status NOT IN ('adopted', NULL)    -- 0 rows!
```

<div dir="rtl">

**למה:** `NOT IN (a, b)` = `<> a AND <> b`. ו‑`<> NULL` = NULL. ו‑`X AND NULL` = NULL (לכל היותר). ⟵ אף שורה TRUE.

**מתי זה יכה:** לא ברשימה מפורשת — שם לא כותבים NULL. אלא ב**מודול 24**, כשהרשימה מגיעה מתת‑שאילתה: `NOT IN (SELECT animal_id FROM expense)` — ו‑`expense.animal_id` **כן** מכיל NULL. **שאילתה שנראית נכונה ומחזירה כלום.**

</details>

---

### שאלה 12
**למה `LIMIT` בלי `ORDER BY` הוא "לבדיקה בלבד"?**

<details><summary>💡 תשובה</summary>

כי בלי `ORDER BY`, בסיס הנתונים **לא מתחייב לשום סדר**. `LIMIT 3` מחזיר "3 שורות כלשהן" — בדרך כלל לפי סדר האחסון, אבל זה יכול להשתנות.

| השימוש | תקין? |
|---------|--------|
| "תראה לי כמה שורות כדי לבדוק שהשאילתה עובדת" | ✅ |
| "תראה לי את 3 החיות הכבדות ביותר" | ❌ — צריך `ORDER BY weight_kg DESC LIMIT 3` (מודול 18) |

**ובאורקל:** `FETCH FIRST 3 ROWS ONLY` (או `ROWNUM <= 3` בגרסאות ישנות).

</details>

---

### שאלה 13
**כתבו תנאי שמוצא את כל החיות ששמן מתחיל ב‑L או מסתיים ב‑a — בשתי דרכים.**

<details><summary>💡 תשובה</summary>

</div>

```sql
-- with OR
WHERE name LIKE 'L%' OR name LIKE '%a'

-- Luna, Lily (start with L) + Simba, Bella, Nala (end with a)
-- Luna counts once -- it matches both, but it's still one row
```

<div dir="rtl">

**"שתי דרכים":** אין `IN` ל‑`LIKE`, אז `OR` היא הדרך. הדרך השנייה היא ניסוח שקול עם `NOT`: `WHERE NOT (name NOT LIKE 'L%' AND name NOT LIKE '%a')` — נכון, אבל אל תעשו את זה. **קריאוּת גוברת על תחכום.**

</details>

---

### שאלה 14
**איך כותבים `WHERE` עם ארבעה תנאים כך שאפשר יהיה לקרוא אותו בעוד חודש?**

<details><summary>💡 תשובה</summary>

</div>

```sql
SELECT name, species_id, weight_kg
FROM   animal
WHERE  species_id IN (1, 2)
  AND  status = 'available'
  AND  weight_kg > 4
  AND  chip_number IS NOT NULL;
```

<div dir="rtl">

| הכלל | למה |
|------|------|
| **תנאי אחד בכל שורה** | אפשר להעיר אחד בלי לגעת בשאר |
| **`AND` בתחילת השורה** | רואים מיד שכל השורות מתחברות |
| **יישור** | העין קופצת בין התנאים |
| **`IN` במקום `OR`** | מבטל את סכנת הקדימויות |

**הסיפור ממודול 16:** שאילתה של 400 מילים בשורה אחת — שבועיים לפענח. הכתיבה היא לא קוסמטיקה.

</details>

---

### שאלה 15
**מודול 16 השאיר 8 שאלות של רותי. על כמה אפשר לענות עכשיו?**

<details><summary>💡 תשובה</summary>

| # | השאלה | עכשיו? |
|---|--------|---------|
| 1 | כל החיות | ✅ (מודול 16) |
| 2 | רק כלבים | ✅ `WHERE species_id = 1` |
| 3 | מהכבדה לקלה | ❌ מודול 18 |
| 4 | כמה חיות | ❌ מודול 23 |
| 5 | שם המין ולא המספר | ❌ מודול 21 |
| 6 | בלי שבב | ✅ `WHERE chip_number IS NULL` |
| 7 | כמה עלה כל חיה | ❌ מודולים 21+23+24 |
| 8 | שם מלא של מתנדבים | ✅ `WHERE role = 'volunteer'` |

**ארבע מתוך שמונה.** ובמודול הבא — חמש.

</details>

---

### שאלה 16
**מה ההבדל בין SQLite ל‑Oracle ב‑`LIKE`?**

<details><summary>💡 תשובה</summary>

| | SQLite (Programiz) | Oracle |
|---|---|---|
| `name LIKE 'l%'` (אות קטנה) | ✅ **מוצא** את Luna | ❌ 0 שורות |
| למה | `LIKE` לא רגיש לאותיות לטיניות כברירת מחדל | `LIKE` רגיש, כמו `=` |

**ההשלכה:** שאילתה שעובדת ב‑Programiz עלולה להיכשל בבחינה על APEX.

**הפתרון שעובד בכל מקום:** `UPPER(name) LIKE 'L%'` — מודול 19. **אל תסתמכו על סלחנות של כלי.**

</details>

---

<div align="center">

### 📎 [לתרגילים](exercises.md) · [חזרה למודול](README.md)

</div>

---

<div align="center">

**🧭 ניווט המודול**

</div>

| 📖 [חזרה למודול](README.md) | ✏️ [לתרגילים](exercises.md) | ✅ [פתרונות](solutions.md) | 🏠 [דף הקורס](../../) |
|---|---|---|---|

</div>
