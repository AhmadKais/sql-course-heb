<div dir="rtl">

# מודול 20 — שאלות ותשובות

> נסחו תשובה — **והריצו** — לפני שאתם פותחים.

---

## 🟢 חלק א' — מושגים

### שאלה 1
**מה ההבדל בין המרה מרומזת להמרה מפורשת? תנו דוגמה לכל אחת.**

<details><summary>💡 תשובה</summary>

| | מרומזת (implicit) | מפורשת (explicit) |
|---|---|---|
| מי ממיר | בסיס הנתונים, לבד | אתם, בפונקציה |
| דוגמה | `'10' + 5` ⟵ 15 | `CAST('10' AS INTEGER) + 5` ⟵ 15 |
| הסיכון | ההתנהגות שונה בין מערכות, ולפעמים מפתיעה | אין — כתוב מה רציתם |

**ההמלצה:** תמיד מפורשת. הקוד ארוך במילה אחת, וברור לכל מי שקורא אותו.

</details>

---

### שאלה 2
**למה `'9' < '10'` מחזיר false?**

<details><summary>💡 תשובה</summary>

כי שני הצדדים **טקסט**, וטקסט מושווה **תו אחר תו** משמאל: `'9'` מול `'1'`. התו `'1'` קטן מ‑`'9'`, ולכן `'10'` "קטן" מ‑`'9'` — בדיוק כמו ש‑`"apple"` קטן מ‑`"banana"`.

**התיקון:** `CAST('9' AS INTEGER) < CAST('10' AS INTEGER)` ⟵ true.
**התיקון האמיתי:** לשמור מספרים בעמודת מספר (מודול 26).

</details>

---

### שאלה 3
**מה מחזיר `CAST(18.9 AS INTEGER)`? ומה `ROUND(18.9)`?**

<details><summary>💡 תשובה</summary>

- `CAST(18.9 AS INTEGER)` ⟵ **18** — חיתוך (מורידים את מה שאחרי הנקודה).
- `ROUND(18.9)` ⟵ **19** — עיגול לשלם הקרוב.

לגיל — רוצים חיתוך (מי שבן 5.9 הוא בן 5). לכסף — רוצים עיגול (`ROUND(x, 2)`).

</details>

---

### שאלה 4
**מה מחזיר כל ביטוי?**

</div>

```sql
COALESCE(NULL, 'a', 'b')
COALESCE('x', NULL)
COALESCE(NULL, NULL)
NULLIF(5, 5)
NULLIF(5, 6)
```

<details><summary>💡 תשובה</summary>

```text
COALESCE(NULL, 'a', 'b')   -->  'a'    first non-NULL
COALESCE('x', NULL)        -->  'x'
COALESCE(NULL, NULL)       -->  NULL   nothing to fall back to
NULLIF(5, 5)               -->  NULL   equal -> NULL
NULLIF(5, 6)               -->  5      not equal -> the first value
```

</details>

<div dir="rtl">

---

### שאלה 5
**`COALESCE(breed, 'unknown')` משנה את הטבלה?**

<details><summary>💡 תשובה</summary>

**לא.** `COALESCE` משנה רק את **התוצאה** של השאילתה. בטבלה, `breed` של Mitzi נשאר NULL.

וזה בדיוק מה שרוצים: הנתון האמיתי ("לא ידוע") נשמר, ו‑`breed IS NULL` עדיין מוצא אותה. אם היינו שומרים `'unknown'` בטבלה — `IS NULL` כבר לא היה עובד, ו‑`COUNT(breed)` היה סופר אותה כאילו יש לה גזע.

</details>

---

### שאלה 6
**למה כותבים `x / NULLIF(y, 0)`?**

<details><summary>💡 תשובה</summary>

כדי למנוע **חלוקה באפס**. כש‑`y` הוא 0, `NULLIF(y, 0)` מחזיר NULL, וכל חלוקה ב‑NULL נותנת NULL — "אי אפשר לחשב" — במקום שגיאה שעוצרת את השאילתה.

ב‑SQLite חלוקה ב‑0 נותנת NULL גם ככה; ב‑Oracle — שגיאה. `NULLIF` הופך את הקוד לבטוח בכל מערכת.

</details>

---

## 🟡 חלק ב' — CASE

### שאלה 7
**מה ההבדל בין `CASE` הפשוט ל‑`CASE` המחפש? מתי משתמשים בכל אחד?**

<details><summary>💡 תשובה</summary>

</div>

```sql
-- simple: one column compared to values (only "=")
CASE species_id WHEN 1 THEN 'dog' WHEN 2 THEN 'cat' ELSE 'other' END

-- searched: each WHEN is a full condition (<, >, AND, IS NULL ...)
CASE WHEN weight_kg < 10 THEN 'small' WHEN weight_kg < 25 THEN 'medium' ELSE 'large' END
```

<div dir="rtl">

**פשוט** — כשמשווים עמודה אחת לרשימת ערכים קבועים.
**מחפש** — בכל מקרה אחר: טווחים, כמה עמודות, `IS NULL`.

כל `CASE` פשוט אפשר לכתוב כמחפש (`WHEN species_id = 1 …`), אבל לא להפך.

</details>

---

### שאלה 8
**מה יחזיר `CASE` כשאף `WHEN` לא מתאים ואין `ELSE`?**

<details><summary>💡 תשובה</summary>

**NULL** — בשקט, בלי שגיאה. לכן כמעט תמיד כדאי `ELSE`, ולו `ELSE 'other'` — כך רואים מיד שיש ערך שלא חשבתם עליו.

</details>

---

### שאלה 9
**מה לא בסדר בשאילתה? מה היא תחזיר עבור Rex (38.7 ק"ג)?**

</div>

```sql
SELECT name,
       CASE WHEN weight_kg > 5  THEN 'large'
            WHEN weight_kg > 20 THEN 'huge'
            ELSE 'small' END AS size
FROM animal;
```

<details><summary>💡 תשובה</summary>

<div dir="rtl">

Rex יקבל **`'large'`**, לא `'huge'`. `CASE` עוצר ב‑`WHEN` **הראשון** שמתקיים, ו‑`38.7 > 5` מתקיים. ה‑`WHEN` של `> 20` לעולם לא מגיע.

**התיקון:** מהקיצוני לכללי — `> 20` קודם, אחר כך `> 5`.

</div>

</details>

<div dir="rtl">

---

### שאלה 10
**בשאילתת שלב החיים — מה יקרה לחיה בלי תאריך לידה אם נמחק את השורה `WHEN birth_date IS NULL`?**

<details><summary>💡 תשובה</summary>

אם `birth_date` הוא NULL, כל החישוב `(JULIANDAY(…) - JULIANDAY(birth_date)) / 365.25` הוא NULL, וכל השוואה עם NULL (`< 2`, `< 8`) היא "לא ידוע" — לא true. אז החיה **נופלת ל‑`ELSE`** ומקבלת `'senior'`. חיה שאנחנו לא יודעים בת כמה — מתויגת כזקנה. טעות שקטה.

**שימו לב:** המיקום של `WHEN … IS NULL` (ראשון או אחרון לפני `ELSE`) לא משנה את התוצאה — השוואות עם NULL ממילא לא מתקיימות. מה שקובע הוא שהשורה **קיימת**. שמים אותה ראשונה כדי שיהיה ברור שטיפלתם ב‑NULL.

</details>

---

### שאלה 11
**למה לא להשתמש ב‑`CASE species_id WHEN 1 THEN 'Dog' …` בקוד אמיתי?**

<details><summary>💡 תשובה</summary>

כי **יש טבלת `species`** עם השמות. אם יוסיפו מין חמישי — `CASE` לא יכיר אותו (יקבל `'other'`), וצריך לשנות כל שאילתה. `JOIN` לטבלת הקוד (מודול 21) תמיד מעודכן.

`CASE` מתאים לערכים **שאין להם טבלה**: תוויות תצוגה ("small/medium/large"), קטגוריות מחושבות, סדר מיון עסקי.

</details>

---

## 🔴 חלק ג' — חשיבה

### שאלה 12
**איך `CASE` ו‑`COALESCE` עוזרים לשאול טיפוסי משנה (מודול 4)?**

<details><summary>💡 תשובה</summary>

כשכל טיפוסי המשנה שמורים **בטבלה אחת** (כמו `person` עם `role`):

- `CASE` על **עמודת המבחין** (`role`) נותן לכל שורה את התנהגות / התווית של טיפוס המשנה שלה.
- `COALESCE` מאחד **עמודות ייחודיות** של טיפוסי משנה שונים לעמודה אחת: `COALESCE(location, reason)` ב‑`intake`.

כשכל טיפוס משנה בטבלה נפרדת — משתמשים ב‑`JOIN` או `UNION` במקום. **ההחלטה בעיצוב קובעת את ה‑SQL.**

</details>

---

### שאלה 13
**איך תמיינו את החיות כך שאלו שבטיפול רפואי יופיעו ראשונות, ואחריהן הזמינות לאימוץ?**

<details><summary>💡 תשובה</summary>

</div>

```sql
SELECT name, status
FROM   animal
ORDER  BY CASE status WHEN 'medical'   THEN 1
                      WHEN 'available' THEN 2
                      ELSE 3 END,
          name;
```

<div dir="rtl">

`CASE` הופך כל סטטוס **למספר עדיפות**, ו‑`ORDER BY` ממיין לפי המספר. `name` שני — כדי שבתוך כל קבוצה הסדר יהיה אלפביתי.

</details>

---

### שאלה 14
**`COALESCE(age, 'unknown')` עובד ב‑SQLite אבל נכשל ב‑Oracle. למה, ואיך כותבים גרסה שעובדת בשניהם?**

<details><summary>💡 תשובה</summary>

ב‑Oracle כל הערכים ב‑`COALESCE` חייבים להיות **מאותו טיפוס**. `age` הוא מספר ו‑`'unknown'` טקסט — שגיאה. SQLite סלחני ומערבב טיפוסים בעמודה.

**גרסה שעובדת בכל מקום:** להמיר את המספר לטקסט **לפני** `COALESCE`:
`COALESCE(CAST(age AS TEXT), 'unknown')` (ב‑Oracle: `COALESCE(TO_CHAR(age), 'unknown')`).

</details>

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[✏️ לתרגילים](exercises.md)**

</div>

</div>
