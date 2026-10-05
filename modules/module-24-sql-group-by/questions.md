<div dir="rtl">

# מודול 24 — שאלות ותשובות

> נסחו תשובה — **והריצו** — לפני שאתם פותחים.

---

## 🟢 חלק א' — GROUP BY ו‑HAVING

### שאלה 1
**מה עושה `GROUP BY status`? כמה שורות יחזיר `SELECT status, COUNT(*) FROM animal GROUP BY status`?**

<details><summary>💡 תשובה</summary>

`GROUP BY` מחלק את השורות לקבוצות לפי הערך ב‑`status`, ומפעיל את `COUNT(*)` על **כל קבוצה בנפרד**. יחזרו **5** שורות — אחת לכל סטטוס שקיים בנתונים (available, adopted, medical, quarantine, deceased).

</details>

---

### שאלה 2
**למה `SELECT status, name, COUNT(*) FROM animal GROUP BY status` שגוי?**

<details><summary>💡 תשובה</summary>

בקבוצה של `available` יש 9 חיות — 9 שמות. השורה של הקבוצה יכולה להכיל רק **ערך אחד** ב‑`name`. איזה מהם?

**הכלל:** כל עמודה ב‑`SELECT` היא **או** עמודת קיבוץ (מופיעה ב‑`GROUP BY`) **או** פונקציה מצרפית. Oracle מסרב לשאילתה; SQLite מחזיר שם אקראי מהקבוצה.

</details>

---

### שאלה 3
**מה ההבדל בין `WHERE` ל‑`HAVING`?**

<details><summary>💡 תשובה</summary>

| | `WHERE` | `HAVING` |
|---|---|---|
| מסנן | שורות | קבוצות |
| רץ | לפני `GROUP BY` | אחרי `GROUP BY` |
| פונקציה מצרפית | ❌ | ✅ |

`WHERE category = 'medical'` — כל שורה נבדקת לבד. `HAVING SUM(amount) > 3000` — הקבוצה כולה נבדקת.

</details>

---

### שאלה 4
**איך מוצאים ערכים כפולים בעמודה?**

<details><summary>💡 תשובה</summary>

</div>

```sql
SELECT col, COUNT(*)
FROM   t
GROUP  BY col
HAVING COUNT(*) > 1;
```

<div dir="rtl">

כל ערך שמופיע יותר מפעם אחת — הוא כפילות. **זה הצעד הראשון לפני `UNIQUE`** (מודול 27): אם השאילתה מחזירה שורות, האילוץ ייכשל.

</div>

</details>

<div dir="rtl">

---

### שאלה 5
**למה כדאי לקבץ לפי `animal_id` ולא לפי `name`?**

<details><summary>💡 תשובה</summary>

כי **שם אינו ייחודי**. שתי חיות שונות בשם "Max" יתמזגו לקבוצה אחת, והספירות שלהן יחוברו. ראינו בדיוק את זה עם "Rabies": שני חיסונים שונים באותו שם התמזגו, 12 + 5 = 17.

**מקבצים לפי מזהה, מציגים לפי שם.**

</details>

---

### שאלה 6
**אחרי `species LEFT JOIN animal` — למה `COUNT(a.animal_id)` ולא `COUNT(*)`?**

<details><summary>💡 תשובה</summary>

מין בלי חיות מתאימות הוא **שורה אחת** אחרי ה‑`LEFT JOIN`, עם NULL בכל עמודות `animal`. `COUNT(*)` סופר את השורה הזאת ⟵ **1** (שגוי). `COUNT(a.animal_id)` מדלג על NULL ⟵ **0** (נכון).

</details>

---

## 🟡 חלק ב' — ROLLUP ותתי‑שאילתות

### שאלה 7
**מה ההבדל בין `ROLLUP (year, category)` ל‑`CUBE (year, category)`?**

<details><summary>💡 תשובה</summary>

| | `ROLLUP` | `CUBE` |
|---|---|---|
| (year, category) | ✅ | ✅ |
| סיכום לכל year | ✅ | ✅ |
| סיכום לכל category | ❌ | ✅ |
| סך הכול | ✅ | ✅ |

`ROLLUP` — **היררכי**: מהפרט לכלל, לפי הסדר. `CUBE` — **כל** הצירופים. שניהם ב‑Oracle; ב‑SQLite בונים עם `UNION ALL`.

</details>

---

### שאלה 8
**מהן שלוש הצורות של תת‑שאילתה, ואיפה כל אחת מופיעה?**

<details><summary>💡 תשובה</summary>

| מה היא מחזירה | איפה | עם מה |
|----------------|-------|--------|
| **ערך אחד** | `WHERE`, `SELECT` | `=`, `>`, `<` … |
| **רשימה** (עמודה אחת, הרבה שורות) | `WHERE` | `IN`, `NOT IN`, `ANY`, `ALL` |
| **טבלה** | `FROM`, `WITH` | כמו כל טבלה |

ובנוסף: **`EXISTS`** — לא משנה מה היא מחזירה, רק **אם** היא מחזירה משהו.

</details>

---

### שאלה 9
**מה זו תת‑שאילתה מתואמת? תנו דוגמה.**

<details><summary>💡 תשובה</summary>

תת‑שאילתה שמשתמשת בעמודה **מהשאילתה החיצונית**, ולכן רצה מחדש **לכל שורה**:

</div>

```sql
SELECT a.name FROM animal a
WHERE  a.weight_kg > (SELECT AVG(b.weight_kg) FROM animal b
                      WHERE  b.species_id = a.species_id);
```

<div dir="rtl">

`a.species_id` בא מבחוץ. לכל חיה, הפנימית מחשבת את ממוצע **המין שלה**. תת‑שאילתה רגילה (לא מתואמת) רצה פעם אחת ונותנת ערך אחד לכולם.

</div>

</details>

<div dir="rtl">

---

### שאלה 10 ⚠️
**למה השאילתה הזאת מחזירה 0 שורות, למרות שיש 10 חיות בלי הוצאות?**

</div>

```sql
SELECT name FROM animal
WHERE  animal_id NOT IN (SELECT animal_id FROM expense);
```

<details><summary>💡 תשובה</summary>

<div dir="rtl">

כי בעמודה `expense.animal_id` יש **NULL** (הוצאות כלליות). הרשימה היא `(8, NULL, 5, …)`, ו‑`x NOT IN (…)` פירושו `x <> 8 AND x <> NULL AND x <> 5 …`. ההשוואה `x <> NULL` היא "לא ידוע", ו‑`AND` עם "לא ידוע" לעולם אינו true. **כל השורות נפסלות, בשקט.**

**תיקון:** `NOT EXISTS (SELECT 1 FROM expense e WHERE e.animal_id = a.animal_id)` — או `WHERE animal_id IS NOT NULL` בתוך הפנימית.

</div>

</details>

<div dir="rtl">

---

### שאלה 11
**למה אי אפשר לכתוב `AVG(SUM(amount))`? איך מחשבים "ממוצע של סכומים"?**

<details><summary>💡 תשובה</summary>

כי שתי פונקציות מצרפיות לא יכולות לפעול באותה רמה: `SUM` צריך קבוצות, ו‑`AVG` צריך את **תוצאות** הקבוצות. פותרים בשתי רמות — תת‑שאילתה ב‑`FROM` (או `WITH`):

</div>

```sql
SELECT AVG(total)
FROM   (SELECT animal_id, SUM(amount) AS total FROM expense
        WHERE animal_id IS NOT NULL GROUP BY animal_id);
```

</details>

<div dir="rtl">

---

## 🔴 חלק ג' — פעולות קבוצה וסדר ביצוע

### שאלה 12
**מה ההבדל בין `UNION` ל‑`UNION ALL`? מתי כל אחד?**

<details><summary>💡 תשובה</summary>

`UNION` מסיר שורות כפולות (גם בתוך כל צד!). `UNION ALL` משאיר הכול — ומהיר יותר, כי לא צריך לבדוק כפילויות.

**ברירת המחדל: `UNION ALL`.** `UNION` רק כשרוצים במפורש רשימה של ערכים **שונים**. אם מחברים תנועות כספיות ב‑`UNION`, שתי הוצאות זהות יתמזגו — והסכום יהיה שגוי.

</details>

---

### שאלה 13
**מה הם `INTERSECT` ו‑`EXCEPT`? מה השם של `EXCEPT` ב‑Oracle?**

<details><summary>💡 תשובה</summary>

- `A INTERSECT B` — שורות שמופיעות **בשתיהן**.
- `A EXCEPT B` — שורות שב‑A ו**לא** ב‑B. ב‑Oracle: **`MINUS`**.

שתיהן מסירות כפילויות. **הסדר חשוב ב‑`EXCEPT`:** `A EXCEPT B` ≠ `B EXCEPT A`.

</details>

---

### שאלה 14
**סדרו לפי סדר הביצוע: `SELECT`, `WHERE`, `ORDER BY`, `FROM`, `HAVING`, `GROUP BY`. למה `WHERE total > 100` (כש‑`total` כינוי מ‑`SELECT`) נכשל, ו‑`ORDER BY total` עובד?**

<details><summary>💡 תשובה</summary>

`FROM` ⟵ `WHERE` ⟵ `GROUP BY` ⟵ `HAVING` ⟵ `SELECT` ⟵ `ORDER BY`.

הכינוי `total` נוצר ב‑`SELECT` (שלב 5). `WHERE` (שלב 2) רץ לפניו — הכינוי עוד לא קיים. `ORDER BY` (שלב 6) רץ אחריו — הכינוי כבר שם.

</details>

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[✏️ לתרגילים](exercises.md)**

</div>

</div>
