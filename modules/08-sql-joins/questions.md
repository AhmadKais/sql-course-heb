<div dir="rtl">

# מודול 21 — שאלות ותשובות

> נסחו תשובה — **והריצו** — לפני שאתם פותחים.

---

## 🟢 חלק א' — מושגים

### שאלה 1
**למה בכלל צריך `JOIN`? למה לא לשמור הכול בטבלה אחת?**

<details><summary>💡 תשובה</summary>

כי **נרמול** (מודול 6) הפריד את המידע לטבלאות, כדי שכל עובדה תישמר פעם אחת: שם המין "Dog" נשמר רק ב‑`species`. אם היינו שומרים אותו בכל שורה של `animal` — שינוי שם היה דורש לעדכן עשרות שורות, ושגיאת הקלדה אחת הייתה יוצרת "Dgo".

`JOIN` הוא המחיר של הנרמול: הנתונים מאוחסנים מפורקים, ונאספים בחזרה בזמן השאילתה.

</details>

---

### שאלה 2
**מהו תוצר קרטזי? כמה שורות יחזיר `SELECT * FROM animal, species`?**

<details><summary>💡 תשובה</summary>

**כל** שורה מהטבלה הראשונה מחוברת עם **כל** שורה מהשנייה. 20 חיות × 4 מינים = **80 שורות**, רובן שגויות (Luna כחתולה, כארנבת…).

זה קורה כשמבקשים שתי טבלאות **בלי תנאי חיבור**. כמעט תמיד באג. **הסימן:** הרבה יותר שורות ממה שציפיתם.

</details>

---

### שאלה 3
**מה ההבדל בין `ON` ל‑`WHERE` בשאילתה עם `JOIN`?**

<details><summary>💡 תשובה</summary>

| | `ON` | `WHERE` |
|---|---|---|
| התפקיד | **איך** מחברים את הטבלאות | **אילו** שורות נשארות בתוצאה |
| דוגמה | `ON s.species_id = a.species_id` | `WHERE a.status = 'available'` |

ב‑`JOIN` רגיל (inner), אפשר להעביר תנאי בין השניים והתוצאה זהה. ב‑`LEFT JOIN` — **לא**: תנאי על הטבלה הימנית ב‑`WHERE` מוחק את השורות שאין להן התאמה (ראו תרגיל 6).

</details>

---

### שאלה 4
**כמה תנאי חיבור צריך כדי לחבר 4 טבלאות?**

<details><summary>💡 תשובה</summary>

לפחות **3** (N − 1). כל תנאי "תופר" טבלה אחת נוספת לשאר. אם חסר תנאי — אחת הטבלאות מתחברת לכל השורות (תוצר קרטזי חלקי), והתוצאה מתנפחת.

</details>

---

### שאלה 5
**השאילתה `SELECT name FROM animal a JOIN species s ON s.species_id = a.species_id` נכשלת. למה?**

<details><summary>💡 תשובה</summary>

`ambiguous column name: name` — בשתי הטבלאות יש עמודה בשם `name`, ו‑SQL לא יודע לאיזו הכוונה. **התיקון:** `a.name` (שם החיה) או `s.name` (שם המין).

**הרגל טוב:** כינוי לפני **כל** עמודה בשאילתה עם `JOIN`.

</details>

---

## 🟡 חלק ב' — סוגי JOIN

### שאלה 6
**מה ההבדל בין `JOIN` ל‑`LEFT JOIN`? תנו דוגמה שבה התוצאה שונה.**

<details><summary>💡 תשובה</summary>

- `JOIN` (inner) — רק שורות שיש להן התאמה **בשני** הצדדים.
- `LEFT JOIN` — **כל** השורות מהטבלה השמאלית; אם אין התאמה, עמודות הימנית NULL.

**דוגמה:** `animal JOIN vaccination` — 16 חיות (28 שורות). `animal LEFT JOIN vaccination` — **כל 20** החיות (32 שורות): Coco, Nala, Lily ו‑Kiwi מופיעות עם NULL.

</details>

---

### שאלה 7
**איך מוצאים חיות שמעולם לא חוסנו? למה בודקים `v.vaccination_id IS NULL` ולא, למשל, `v.cost IS NULL`?**

<details><summary>💡 תשובה</summary>

</div>

```sql
SELECT a.name
FROM   animal a
LEFT   JOIN vaccination v ON v.animal_id = a.animal_id
WHERE  v.vaccination_id IS NULL;
```

<div dir="rtl">

בודקים את **המפתח הראשי** של הטבלה הימנית, כי בשורה אמיתית הוא **לעולם** אינו NULL. לכן NULL בו אומר רק דבר אחד: "אין שורה". עמודה כמו `cost` יכולה בעיקרון להיות NULL גם בשורה אמיתית (נניח חיסון שניתן בחינם ולא נרשם מחיר) — ואז נקבל תשובה שגויה.

</details>

---

### שאלה 8
**מה זה nonequijoin? מתי עדיף על `CASE`?**

<details><summary>💡 תשובה</summary>

חיבור שהתנאי שלו **אינו שוויון** — בדרך כלל טווח: `ON a.weight_kg BETWEEN b.min_kg AND b.max_kg`.

עדיף על `CASE` כשהטווחים **משתנים**: עם טבלה, מעדכנים שורה — בלי לגעת בקוד. מדרגות מס, דרגות שכר, הנחות כמות — כולן טבלאות טווחים. `CASE` מתאים כשהטווחים קבועים ומופיעים בשאילתה אחת.

</details>

---

### שאלה 9
**מה עושה `(+)` בשאילתת Oracle?**

</div>

```sql
SELECT e.description, a.name
FROM   expense e, animal a
WHERE  e.animal_id = a.animal_id(+);
```

<details><summary>💡 תשובה</summary>

<div dir="rtl">

זה **outer join בתחביר הישן של Oracle**. ה‑`(+)` נכתב **בצד שעלול להיות חסר** — כאן `animal`. התוצאה: כל ההוצאות, ושם החיה אם יש. שקול ל:

</div>

```sql
SELECT e.description, a.name
FROM   expense e
LEFT   JOIN animal a ON a.animal_id = e.animal_id;
```

<div dir="rtl">

**קוראים `(+)`, כותבים `LEFT JOIN`.**

</div>

</details>

<div dir="rtl">

---

## 🔴 חלק ג' — Self join והיררכיה

### שאלה 10
**מה זה self join? למה צריך שני כינויים?**

<details><summary>💡 תשובה</summary>

חיבור של טבלה **לעצמה** — כשהשאלה היא על שתי שורות מאותה טבלה: שתי חיות מאותו גזע, עובד והמנהל שלו (ששניהם ב‑`staff`).

שני כינויים (`a1`, `a2`) — כי SQL צריך להבחין בין "העותק השמאלי" ל"עותק הימני". בלי כינויים — `animal.name` לא אומר מאיזה עותק.

</details>

---

### שאלה 11
**בשאילתת "זוגות מאותו גזע" — מה יקרה אם נשתמש ב‑`a1.animal_id <> a2.animal_id` במקום `<`?**

<details><summary>💡 תשובה</summary>

`<>` מונע חיבור של חיה **לעצמה**, אבל כל זוג יופיע **פעמיים**: Luna–Daisy וגם Daisy–Luna. במקום 4 זוגות — 8 שורות.

`<` משאיר רק את הסדר שבו המזהה הקטן משמאל — כל זוג פעם אחת.

</details>

---

### שאלה 12
**מה ההבדל בין self join לשאילתה רקורסיבית בהיררכיה?**

<details><summary>💡 תשובה</summary>

- **self join** — רמה **אחת**: עובד ⟵ המנהל הישיר שלו. לשתי רמות צריך עוד join, לשלוש — עוד אחד. מספר הרמות חייב להיות ידוע מראש.
- **רקורסיה** (`WITH RECURSIVE` / `CONNECT BY`) — **כל** הרמות, כמה שיהיו. השאילתה מוסיפה שוב ושוב את הרמה הבאה עד שאין יותר.

בעץ ארגוני אמיתי מספר הרמות משתנה — ולכן רקורסיה.

</details>

---

### שאלה 13
**ב‑Oracle: מה אומרים `START WITH` ו‑`CONNECT BY PRIOR`?**

</div>

```sql
SELECT LPAD(' ', (LEVEL - 1) * 4) || name, LEVEL
FROM   staff
START  WITH manager_id IS NULL
CONNECT BY PRIOR staff_id = manager_id;
```

<details><summary>💡 תשובה</summary>

<div dir="rtl">

- **`START WITH manager_id IS NULL`** — מאיפה מתחילים: השורש (מי שאין לו מנהל).
- **`CONNECT BY PRIOR staff_id = manager_id`** — איך יורדים רמה: ה‑`staff_id` של השורה **הקודמת** (`PRIOR`, ההורה) שווה ל‑`manager_id` של השורה הבאה (הילד).
- **`LEVEL`** — עמודה מובנית: עומק השורה בעץ (1 = שורש).

להליכה **למעלה** (מעובד למנהליו) הופכים: `CONNECT BY PRIOR manager_id = staff_id`.

</div>

</details>

<div dir="rtl">

---

### שאלה 14
**הקשר למודול 5: איזה `JOIN` מתאים לכל סוג יחס?**

<details><summary>💡 תשובה</summary>

| היחס ב‑ERD | בטבלאות | ה‑JOIN |
|------------|----------|---------|
| 1 : רבים, חובה | מפתח זר `NOT NULL` | `JOIN` — לכל שורה יש התאמה |
| 1 : רבים, **אופציונלי** | מפתח זר שיכול להיות NULL (`expense.animal_id`) | `LEFT JOIN` — אחרת שורות ייעלמו |
| רבים : רבים | טבלת קישור (`adoption`) | שני `JOIN`‑ים, דרך טבלת הקישור |
| רקורסיבי | מפתח זר לאותה טבלה (`staff.manager_id`) | self join / רקורסיה |

**הקו המקווקו ב‑ERD (אופציונלי) = `LEFT JOIN` ב‑SQL.**

</details>

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[✏️ לתרגילים](exercises.md)**

</div>

</div>
