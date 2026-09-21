<div dir="rtl">

# מודול 18 — שאלות ותשובות

> נסחו תשובה — **והריצו** — לפני שאתם פותחים.

---

## 🟢 חלק א' — ORDER BY

### שאלה 1
**מה מחזירה שאילתה בלי `ORDER BY` — ולמה זה מסוכן?**

<details><summary>💡 תשובה</summary>

שורות **בסדר שנוח לבסיס הנתונים** — בדרך כלל סדר האחסון, אבל **בלי הבטחה**.

**למה מסוכן:** זה נראה מסודר. הדוח "10 המובילים" עבד שנתיים בלי `ORDER BY`, ואז שדרוג שינה את סדר האחסון — והמנהל הזמין מלאי לפי 10 מוצרים אקראיים.

**הכלל:** אם הסדר חשוב — `ORDER BY`. אם לא כתבתם — לא ביקשתם.

</details>

---

### שאלה 2
**מה ההבדל בין השתיים?**

</div>

```sql
ORDER BY species_id, weight_kg DESC
ORDER BY species_id DESC, weight_kg DESC
```

<div dir="rtl">

<details><summary>💡 תשובה</summary>

| | `species_id` | `weight_kg` |
|---|---|---|
| הראשונה | **עולה** (1, 2, 3, 4) | יורד בתוך כל מין |
| השנייה | **יורד** (4, 3, 2, 1) | יורד בתוך כל מין |

**`DESC` חל על מפתח אחד בלבד** — זה שממש לפניו. אם לא כתבתם `DESC` ליד `species_id`, הוא עולה.

</details>

---

### שאלה 3
**מתי המפתח השני ב‑`ORDER BY` נכנס לפעולה?**

<details><summary>💡 תשובה</summary>

**רק כשהמפתח הראשון שווה.**

`ORDER BY species_id, weight_kg` — קודם כל הכלבים (מין 1), ורק **בתוכם** לפי משקל. ואז כל החתולים (מין 2), ובתוכם לפי משקל.

**המפתח הראשון מקבץ; השני מסדר בתוך הקבוצה.** אם לכל שורה ערך שונה במפתח הראשון — המפתח השני לא משפיע בכלל.

</details>

---

### שאלה 4
**מה יחזיר `ORDER BY name` על הערכים `'apple'`, `'Banana'`, `'cherry'`?**

<details><summary>💡 תשובה</summary>

**`Banana`, `apple`, `cherry`.**

לא אלפביתי "אנושי". בסיס הנתונים משווה **קודי תווים**: `'B'` = 66, `'a'` = 97. **כל האותיות הגדולות לפני כל הקטנות.**

**אותו עיקרון:** `'10'` לפני `'2'` (תו‑תו: `'1'` < `'2'`), ולטינית לפני עברית.

**הפתרון:** `ORDER BY UPPER(name)` — מודול 19. או: אם זה מספר, שיהיה מספר (מודול 7 — תחומים).

</details>

---

## 🟡 חלק ב' — כינויים, NULL, LIMIT

### שאלה 5
**למה `ORDER BY weight_lb` עובד אבל `WHERE weight_lb > 40` נכשל ב‑Oracle?**

<details><summary>💡 תשובה</summary>

בגלל **סדר הביצוע הלוגי**:

</div>

```text
FROM -> WHERE -> SELECT -> ORDER BY -> LIMIT
         ^          ^          ^
         |          |          alias EXISTS here
         |          alias is CREATED here
         alias does NOT exist yet
```

<div dir="rtl">

`WHERE` רץ **לפני** `SELECT` — הכינוי עוד לא נוצר. `ORDER BY` רץ **אחרי** — הכינוי כבר קיים.

⚠️ **מלכודת:** SQLite (Programiz) **מרשה** כינוי ב‑`WHERE`, בניגוד לתקן. שאילתה שעובדת ב‑Programiz תיכשל ב‑APEX עם `ORA-00904`. **כתבו לפי התקן.**

</details>

---

### שאלה 6
**איפה NULL נופל במיון עולה?**

<details><summary>💡 תשובה</summary>

**תלוי בבסיס הנתונים:**

| | `ASC` | `DESC` |
|---|---|---|
| SQLite / MySQL / PostgreSQL | **ראשון** | אחרון |
| **Oracle** | **אחרון** | ראשון |

**ההשלכה:** `ORDER BY birth_date LIMIT 3` ("3 הוותיקות") מחזיר ב‑SQLite **שלוש חיות בלי תאריך לידה**. לא הוותיקות — הלא‑ידועות.

**הפתרון:**
- Oracle: `ORDER BY birth_date NULLS LAST`
- SQLite: `ORDER BY birth_date IS NULL, birth_date` — הטריק: `IS NULL` מחזיר 0 לערך ו‑1 ל‑NULL, אז הערכים קודם

</details>

---

### שאלה 7
**איך עובד הטריק `ORDER BY birth_date IS NULL, birth_date`?**

<details><summary>💡 תשובה</summary>

`birth_date IS NULL` הוא **ביטוי** שמחזיר:
- `0` (FALSE) לשורות **עם** תאריך
- `1` (TRUE) לשורות **בלי** תאריך

מיון עולה לפי הביטוי הזה ⟵ כל ה‑0 לפני כל ה‑1 ⟵ **הערכים לפני ה‑NULL**.

ואז המפתח השני, `birth_date`, מסדר בתוך קבוצת ה‑0.

**זה מפתח ראשון "מלאכותי"** שכל תפקידו לחלק לשתי קבוצות. אותו דפוס עובד לכל "שים את X בסוף": `ORDER BY status = 'deceased', name`.

</details>

---

### שאלה 8
**מה הבעיה ב‑`ORDER BY 2 DESC`?**

<details><summary>💡 תשובה</summary>

זה **מספר עמודה** — "העמודה השנייה ב‑`SELECT`". עובד, אבל **שביר**:

</div>

```sql
SELECT name, weight_kg FROM animal ORDER BY 2 DESC;         -- sorts by weight  [OK]

-- someone adds a column:
SELECT name, breed, weight_kg FROM animal ORDER BY 2 DESC;  -- now sorts by BREED
```

<div dir="rtl">

אף אחד לא נגע ב‑`ORDER BY`, והמיון השתנה בשקט.

**במקום זה:** כינוי. `ORDER BY weight_kg DESC` או `ORDER BY lb DESC`. קריא ויציב.

</details>

---

### שאלה 9
**"3 החיות הכבדות ביותר" — מה הבעיה אם השלישית והרביעית שוקלות אותו דבר?**

<details><summary>💡 תשובה</summary>

`ORDER BY weight_kg DESC LIMIT 3` יחזיר **אחת מהן** — ואין לדעת איזו. שתי הרצות יכולות לתת תוצאה שונה.

**הפתרון — מפתח שובר שוויון:**

</div>

```sql
ORDER BY weight_kg DESC, animal_id
LIMIT 3;
```

<div dir="rtl">

עכשיו התוצאה **דטרמיניסטית**: בשוויון, המזהה הנמוך קודם. תמיד אותו דבר.

**הכלל:** `LIMIT` עם `ORDER BY` שיכול להכיל שוויון — הוסיפו מפתח ייחודי בסוף.

</details>

---

## 🔴 חלק ג' — לוגיקה וסדר ביצוע

### שאלה 10
**כתבו את סדר הביצוע הלוגי, והסבירו למה `LIMIT` לא מאיץ את `WHERE`.**

<details><summary>💡 תשובה</summary>

</div>

```text
FROM -> WHERE -> SELECT -> ORDER BY -> LIMIT
```

<div dir="rtl">

`LIMIT` רץ **אחרון**. לפניו, `WHERE` כבר בדק **את כל השורות** ו‑`ORDER BY` כבר מיין **את כל מה שנשאר**. רק אז `LIMIT` שומר N.

**כלומר:** `LIMIT 3` על מיליון שורות עדיין **קורא** מיליון שורות. הוא חוסך **תצוגה**, לא **עבודה**.

**מה שכן מאיץ:** `WHERE` צר (פחות שורות לשאר השלבים), ואינדקסים (מודול 29).

</details>

---

### שאלה 11
**מה מחזירים `FALSE AND NULL`, `TRUE OR NULL`, ו‑`NOT NULL`?**

<details><summary>💡 תשובה</summary>

| הביטוי | התוצאה | למה |
|--------|---------|------|
| `FALSE AND NULL` | **FALSE** | צד אחד כבר שקר — לא משנה מה השני |
| `TRUE OR NULL` | **TRUE** | צד אחד כבר אמת — לא משנה מה השני |
| `NOT NULL` | **NULL** | ⚠️ "ההפך מלא‑ידוע" הוא עדיין לא‑ידוע |

**השלישי הוא המפתיע.** `WHERE NOT (breed = 'Mixed')` על חיה בלי גזע — `NOT NULL` = NULL ⟵ השורה נופלת. `NOT` **לא הופך** NULL ל‑TRUE.

זו **לוגיקה תלת‑ערכית**: TRUE / FALSE / NULL. וב‑`WHERE` רק TRUE נכנס.

</details>

---

### שאלה 12
**מה סדר הקדימויות המלא, ואיך קוראים `NOT a OR b AND c`?**

<details><summary>💡 תשובה</summary>

</div>

```text
1. ( )
2. NOT
3. AND
4. OR

NOT a OR b AND c   ==   (NOT a) OR (b AND c)
```

<div dir="rtl">

`NOT` נקשר הכי חזק (רק ל‑`a`). `AND` אחריו (`b AND c`). `OR` הכי חלש — מחבר את השניים.

**ובפועל:** אל תכתבו את זה בלי סוגריים. גם אם אתם יודעים את הכלל — מי שיקרא אולי לא.

</details>

---

### שאלה 13
**שאלת ראיון: "איך תמצא את 5 הלקוחות עם ההזמנה הגדולה ביותר?" — תנו תשובה מצוינת, לא רק טובה.**

<details><summary>💡 תשובה</summary>

**תשובה טובה:**
> `ORDER BY amount DESC LIMIT 5`.

**תשובה מצוינת:**
> `ORDER BY amount DESC LIMIT 5` — ושתי הערות: אחת, אם יש שוויון בסכום החמישי, כדאי מפתח שובר שוויון כמו `customer_id` כדי שהתוצאה תהיה יציבה. שתיים, ב‑Oracle זה `FETCH FIRST 5 ROWS ONLY`, לא `LIMIT`.

**ההבדל:** הטובה עונה. המצוינת מוסיפה **מלכודת אחת** שמראה שעבדתם עם זה באמת.

</details>

---

### שאלה 14
**רותי רוצה "חיות זמינות, לפי מין, ובתוך כל מין לפי משקל — ובלי תאריך לידה בסוף כל מין". למה `IS NULL` חייב להיות המפתח השני ולא הראשון?**

<details><summary>💡 תשובה</summary>

| הסדר | התוצאה |
|-------|---------|
| `ORDER BY birth_date IS NULL, species_id, weight_kg` | כל החיות **עם** תאריך (כל המינים), ואז כל החיות **בלי** — בסוף הרשימה **כולה** |
| `ORDER BY species_id, birth_date IS NULL, weight_kg` | ✅ מין 1, בתוכו הידועות ואז הלא‑ידועות; מין 2, אותו דבר… |

**סדר המפתחות הוא סדר העדיפויות.** מה שרותי ביקשה — "בסוף כל מין" — אומר שהמין קודם, וה‑NULL אחריו.

</details>

---

### שאלה 15
**מה עושה `LENGTH(name)` ואיך זה קשור למיון?**

<details><summary>💡 תשובה</summary>

`LENGTH(name)` היא **פונקציה** — מקבלת טקסט, מחזירה מספר (כמה תווים).

</div>

```sql
SELECT   name, LENGTH(name) AS letters
FROM     animal
ORDER BY LENGTH(name) DESC;
-- -> Thumper 7, Charlie 7, Shadow 6, ...
```

<div dir="rtl">

**הקשר למיון:** אפשר למיין לפי **תוצאה של פונקציה**, לא רק לפי עמודה. ו‑`ORDER BY UPPER(name)` פותר את בעיית האותיות הגדולות משאלה 4.

**זו הטעימה.** מודול 19 כולו פונקציות — טקסט, מספרים, תאריכים.

</details>

---

### שאלה 16
**מודול 16 השאיר 8 שאלות של רותי. על כמה אפשר לענות עכשיו?**

<details><summary>💡 תשובה</summary>

| # | השאלה | עכשיו? |
|---|--------|---------|
| 1 | כל החיות | ✅ 16 |
| 2 | רק כלבים | ✅ 17 |
| **3** | **מהכבדה לקלה** | ✅ **18** — `ORDER BY weight_kg DESC` |
| 4 | כמה חיות | ❌ 23 |
| 5 | שם המין ולא המספר | ❌ 21 |
| 6 | בלי שבב | ✅ 17 |
| 7 | כמה עלה כל חיה | ❌ 21+23+24 |
| 8 | שם מלא של מתנדבים | ✅ 17 |

**חמש מתוך שמונה.** הבאה — מודול 21.

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
