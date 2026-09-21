<div dir="rtl">

# מודול 19 — שאלות ותשובות

> נסחו תשובה — **והריצו** — לפני שאתם פותחים.

---

## 🟢 חלק א' — מושגים

### שאלה 1
**מה ההבדל בין פונקציה "שורה‑שורה" לפונקציה מצרפית?**

<details><summary>💡 תשובה</summary>

| | שורה‑שורה (Single-row) | מצרפית (Aggregate) |
|---|---|---|
| נכנס | שורה אחת | **הרבה** שורות |
| יוצא | שורה אחת | **שורה אחת** |
| דוגמה | `UPPER(name)` — 20 חיות ⟵ 20 תוצאות | `COUNT(*)` — 20 חיות ⟵ תוצאה אחת |
| המודול | **19** (זה) | 23 |

כל הפונקציות במודול הזה הן שורה‑שורה. הן **לא מקטינות** את מספר השורות.

</details>

---

### שאלה 2
**איפה מותר להשתמש בפונקציה?**

<details><summary>💡 תשובה</summary>

**בכל מקום שמותר ערך:**

| המקום | הדוגמה |
|-------|---------|
| `SELECT` | `SELECT UPPER(name)` |
| `WHERE` | `WHERE LENGTH(name) > 5` |
| `ORDER BY` | `ORDER BY UPPER(name)` |
| בתוך פונקציה | `UPPER(SUBSTR(name, 1, 3))` |

**קוראים מבפנים החוצה:** `UPPER(SUBSTR(name, 1, 3))` — קודם חותכים, אז מגדילים.

</details>

---

### שאלה 3
**מה מחזיר `SUBSTR('Rocky', 2, 3)`? ומה `SUBSTR('Rocky', -2)`?**

<details><summary>💡 תשובה</summary>

</div>

```text
   'Rocky'
    12345

   SUBSTR('Rocky', 2, 3)  -->  'ock'    from position 2, take 3
   SUBSTR('Rocky', -2)    -->  'ky'     the last 2
```

<div dir="rtl">

⚠️ **הספירה מ‑1.** `SUBSTR('Rocky', 0, 3)` נותן `'Ro'` ב‑SQLite (2 תווים — כי המיקום 0 "נספר" כריק) ו‑`'Roc'` ב‑Oracle. **אל תשתמשו ב‑0.**

</details>

---

### שאלה 4
**למה `WHERE UPPER(TRIM(name)) = 'LUNA'` עדיף על `WHERE name = 'Luna'`?**

<details><summary>💡 תשובה</summary>

כי הוא **סולח להקלדה**:

| מה הוקלד בטבלה | `= 'Luna'` | `UPPER(TRIM(…)) = 'LUNA'` |
|-----------------|-----------|---------------------------|
| `Luna` | ✅ | ✅ |
| `luna` | ❌ | ✅ |
| `LUNA` | ❌ | ✅ |
| `Luna ` (רווח בסוף) | ❌ | ✅ |

**הסיפור:** יוסי כהן הופיע 4 פעמים ב‑CRM — בגלל אותיות ורווחים. `UPPER(TRIM(…))` איחד 40,000 רשומות ל‑31,000.

**המחיר:** על טבלה ענקית, הפונקציה מסתירה את העמודה מהאינדקס — איטי. מודול 29.

</details>

---

## 🟡 חלק ב' — מספרים ותאריכים

### שאלה 5
**למה `ROUND(x, 2)` תמיד לכסף? תנו דוגמה שמראה את הבעיה.**

<details><summary>💡 תשובה</summary>

</div>

```sql
SELECT 0.1 + 0.2;           -- 0.3    looks right
SELECT 0.1 + 0.2 = 0.3;     -- 0      FALSE!  (floating point: 0.30000000000000004)
SELECT ROUND(0.1 + 0.2, 2) = 0.3;   -- 1  TRUE
```

<div dir="rtl">

מחשבים לא יכולים לייצג `0.1` **בדיוק** (כמו ש‑⅓ אינו ניתן לכתיבה סופית בעשרוני). התוצאה **כמעט** 0.3 — וב‑`WHERE`, "כמעט" זה FALSE.

**בחשבונית עם 1,000 שורות** — סכומים שלא מסתדרים באגורה. `ROUND(…, 2)` בכל חישוב כספי. **תמיד.**

</details>

---

### שאלה 6
**`ROUND` או `FLOOR` לגיל? למה?**

<details><summary>💡 תשובה</summary>

**`FLOOR`.** גיל לא מעגלים — מי שנולד לפני 5.9 שנים הוא בן **5** עד יום ההולדת ה‑6.

</div>

```sql
FLOOR(5.9)  -->  5    correct
ROUND(5.9)  -->  6    wrong -- a 5-year-old is not 6
```

<div dir="rtl">

**ולמה `365.25`?** שנה מעוברת כל 4 שנים. `365` היה נותן שגיאה של יום כל 4 שנים — על כלב בן 10, 2.5 ימים. לא נורא. על מסמך משפטי — כן.

</details>

---

### שאלה 7
**איך מחשבים הפרש ימים בין שני תאריכים ב‑SQLite, ולמה זה שונה מ‑Oracle?**

<details><summary>💡 תשובה</summary>

</div>

```sql
-- SQLite: dates are TEXT. Convert to a number first, then subtract.
JULIANDAY('2026-09-21') - JULIANDAY(birth_date)

-- Oracle: DATE is a real type. Subtract directly.
SYSDATE - birth_date
```

<div dir="rtl">

`JULIANDAY` הופך תאריך למספר ימים (מאז נקודת ייחוס עתיקה). הפרש בין שני מספרים = ימים.

**למה ההבדל:** ב‑SQLite אין טיפוס `DATE` אמיתי — התאריך הוא טקסט בפורמט ISO. ב‑Oracle יש, וחיסור עובד ישירות. **זה ההבדל הגדול ביותר בין הדיאלקטים בכל הקורס.**

</details>

---

### שאלה 8
**מה ההבדל בין `STRFTIME('%Y', d)` ל‑`EXTRACT(YEAR FROM d)`?**

<details><summary>💡 תשובה</summary>

| | SQLite `STRFTIME` | Oracle `EXTRACT` |
|---|---|---|
| התחביר | `STRFTIME('%Y', d)` | `EXTRACT(YEAR FROM d)` |
| מחזיר | **טקסט** — `'2024'` | **מספר** — `2024` |
| השוואה | `= '2024'` (גרשיים!) | `= 2024` |

⚠️ **המלכודת ב‑SQLite:** `STRFTIME('%Y', d) = 2024` (בלי גרשיים) ⟵ **0 שורות**. טקסט לעולם לא שווה למספר. `= '2024'` ⟵ 19 שורות.

**ו‑`STRFTIME` גם מעצב:** `STRFTIME('%d/%m/%Y', d)` ⟵ `05/01/2024`. המקבילה: `TO_CHAR(d, 'DD/MM/YYYY')`.

</details>

---

### שאלה 9
**מתי החיסון הבא? כתבו ל‑SQLite ול‑Oracle.**

<details><summary>💡 תשובה</summary>

</div>

```sql
-- SQLite
SELECT given_date, DATE(given_date, '+12 months') AS next_due FROM vaccination;

-- Oracle
SELECT given_date, ADD_MONTHS(given_date, 12) AS next_due FROM vaccination;
```

<div dir="rtl">

**ולמה זה חשוב עיצובית:** במודול 9 החלטנו ש‑`next_vaccination_date` **לא נשמר** — הוא מחושב. עכשיו רואים איך: שורה אחת. אם היינו שומרים אותו, שינוי בפרוטוקול (12 ⟵ 6 חודשים) היה דורש עדכון של כל השורות.

</details>

---

## 🔴 חלק ג' — NULL, ביצועים, שילובים

### שאלה 10
**מה מחזיר `LENGTH(NULL)`, ולמה `WHERE LENGTH(x) = 0` לא מוצא ערכים ריקים?**

<details><summary>💡 תשובה</summary>

`LENGTH(NULL)` = **NULL**. לא 0.

**הכלל ממודול 16:** NULL נכנס ⟵ NULL יוצא. **כל** פונקציה.

| הערך | `LENGTH` | `= 0`? |
|-------|----------|--------|
| `'Luna'` | 4 | FALSE |
| `''` (מחרוזת ריקה) | 0 | TRUE |
| `NULL` | **NULL** | **NULL** ⟵ השורה נופלת |

**לתפוס את שניהם:** `WHERE x IS NULL OR LENGTH(x) = 0`.

**ובאותו אופן:** `JULIANDAY(NULL)` = NULL ⟵ גיל של חיה בלי תאריך לידה הוא **NULL**, לא 0. וזה נכון — לא ידוע.

</details>

---

### שאלה 11
**למה `WHERE UPPER(name) = 'LUNA'` איטי על 10 מיליון שורות, ו‑`WHERE name = 'Luna'` מהיר?**

<details><summary>💡 תשובה</summary>

</div>

```text
WHERE name = 'Luna'          -- the database can look 'Luna' up in an INDEX on name.
                             -- Like finding a word in a dictionary. Instant.

WHERE UPPER(name) = 'LUNA'   -- the database must compute UPPER() for EVERY row,
                             -- because the index holds 'Luna', not 'LUNA'.
                             -- Like reading the whole dictionary. Slow.
```

<div dir="rtl">

**פונקציה על צד שמאל של ההשוואה מסתירה את העמודה מהאינדקס.**

**הפתרונות** (מודול 29): אינדקס על הביטוי `UPPER(name)`, או לשמור עמודה מנורמלת מראש. **בינתיים:** על 20 חיות זה לא משנה. על מיליונים — כן.

</details>

---

### שאלה 12
**כתבו ביטוי שהופך `'lUNA'` ל‑`'Luna'`.**

<details><summary>💡 תשובה</summary>

</div>

```sql
UPPER(SUBSTR(name, 1, 1)) || LOWER(SUBSTR(name, 2))
--    ^^^^^^^^^^^^^^^^^^    ^^^^^^^^^^^^^^^^^^^^^^^
--    first letter, UP      everything from 2nd, low
```

<div dir="rtl">

**קוראים מבפנים:** `SUBSTR(name, 1, 1)` = `'l'` ⟵ `UPPER` = `'L'`. `SUBSTR(name, 2)` = `'UNA'` ⟵ `LOWER` = `'una'`. חיבור = `'Luna'`.

**ב‑Oracle:** `INITCAP(name)` — פונקציה מוכנה.

</details>

---

### שאלה 13
**"כמה חודשים בין שני תאריכים?" — למה זה קשה ב‑SQLite?**

<details><summary>💡 תשובה</summary>

כי ל‑SQLite אין `MONTHS_BETWEEN`. יש רק ימים (`JULIANDAY`).

**הקירוב:** `(JULIANDAY(b) - JULIANDAY(a)) / 30.44` — 30.44 הוא אורך חודש ממוצע. **קירוב**, לא מדויק.

**המדויק** (כשצריך): `(STRFTIME('%Y', b) - STRFTIME('%Y', a)) * 12 + (STRFTIME('%m', b) - STRFTIME('%m', a))` — שנים כפול 12 ועוד הפרש חודשים. מסורבל, אבל נכון.

**ב‑Oracle:** `MONTHS_BETWEEN(b, a)`. שורה אחת.

**הלקח:** תאריכים הם התחום שבו הדיאלקט **באמת** משנה. סעיף 8 ב‑README הוא הטבלה לשמור.

</details>

---

### שאלה 14
**רותי מבקשת "החיות שנקלטו החודש". איך כותבים את זה כך שיעבוד בכל חודש, בלי לשנות את השאילתה?**

<details><summary>💡 תשובה</summary>

</div>

```sql
SELECT a.name, i.intake_date
FROM   intake i, animal a               -- (proper JOIN syntax: module 21)
WHERE  i.animal_id = a.animal_id
  AND  STRFTIME('%Y-%m', i.intake_date) = STRFTIME('%Y-%m', DATE('now'));
```

<div dir="rtl">

**המפתח:** להשוות **שנה‑חודש** של הקליטה ל**שנה‑חודש של היום**. שני הצדדים מחושבים — אין תאריך קבוע בשאילתה. בכל חודש שמריצים, היא נכונה.

⚠️ **הערה:** `DATE('now')` בקורס נותן תאריך שונה מהפתרונות (שמשתמשים ב‑`'2026-09-21'`). לתרגול — תאריך קבוע. בקוד אמיתי — `'now'`.

</details>

---

### שאלה 15
**מה ההבדל בין `CAST(x AS INTEGER)` ל‑`FLOOR(x)` ב‑SQLite?**

<details><summary>💡 תשובה</summary>

| | `FLOOR(x)` | `CAST(x AS INTEGER)` |
|---|---|---|
| `5.9` | `5.0` | `5` |
| `-5.9` | `-6.0` | `-5` ⚠️ |
| מחזיר | מספר **עשרוני** | מספר **שלם** |
| כיוון | תמיד **למטה** | לכיוון **אפס** (קיצוץ) |

**על מספרים חיוביים (גילים, ימים):** אותה תוצאה, אבל `CAST` מציג `10` ולא `10.0`.
**על שליליים:** שונים. `FLOOR(-5.9) = -6`, `CAST(-5.9) = -5`.

**ב‑Oracle:** `FLOOR` מחזיר שלם ישירות; `TRUNC` הוא הקיצוץ.

</details>

---

### שאלה 16
**שאלת ראיון: "איך תחשב גיל מתאריך לידה?" — תנו תשובה מצוינת.**

<details><summary>💡 תשובה</summary>

**תשובה טובה:**
> מחסרים את תאריך הלידה מהיום ומחלקים ב‑365.

**תשובה מצוינת:**
> מחסרים ומחלקים ב‑**365.25** בגלל שנים מעוברות, ואז **`FLOOR`** ולא `ROUND` — כי מי שבן 5.9 הוא בן 5. וחשוב לומר: **לא שומרים גיל בטבלה**, רק תאריך לידה — כי גיל מזדקן, ותאריך לידה לא.
>
> ב‑SQLite זה `FLOOR((JULIANDAY('now') - JULIANDAY(birth_date)) / 365.25)`; ב‑Oracle `FLOOR(MONTHS_BETWEEN(SYSDATE, birth_date) / 12)`.

**מה שהמראיין שומע:** שלושה מלכודות שנמנעו (365 / ROUND / שמירת גיל) + הכרת שני דיאלקטים. **זו תשובה של מישהו שעבד עם זה.**

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
