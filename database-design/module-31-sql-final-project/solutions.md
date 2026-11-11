<div dir="rtl">

# מודול 31 — פתרון ייחוס: 15 השאילתות על המקלט

> 💡 **זה לא הפרויקט שלכם** — הפרויקט שלכם הוא על הלקוח שלכם. זו **דוגמה** איך 15 השאילתות מסעיף 5 נראות על בסיס נתונים אמיתי, כדי שתדעו מה הרמה המצופה.
>
> כל הפלטים אמיתיים, על [בסיס הנתונים המוכן](../../resources/shelter-db/), נכון ל‑`'2026-09-21'`.

---

## 1 · סינון ו‑ORDER BY

**השאלה:** משפחה עם דירה קטנה ותקציב של עד 250 ₪ — אילו חיות זמינות מתאימות, מהקטנה לגדולה?

</div>

```sql
SELECT a.name, s.name AS species, a.weight_kg
FROM   animal a
JOIN   species s ON s.species_id = a.species_id
WHERE  a.status = 'available'
  AND  s.adoption_fee <= 250
ORDER  BY a.weight_kg;
```

```text
name   species  weight_kg
-----  -------  ---------
Coco   Parrot   0.1
Bunny  Rabbit   1.5
Mitzi  Cat      3.1
Lily   Cat      3.4
Felix  Cat      5.0
Oscar  Cat      5.5
```

<div dir="rtl">

**תובנה:** שש אפשרויות — כל החתולים הזמינים, הארנבת והתוכי. שאילתה כזו יכולה לשבת מאחורי כפתור "חפש" באתר.

---

## 2 · פונקציות תאריך

**השאלה:** למי יש יום הולדת החודש או בחודש הבא? (לפוסט בפייסבוק.)

</div>

```sql
SELECT name, STRFTIME('%d/%m', birth_date) AS birthday
FROM   animal
WHERE  STRFTIME('%m', birth_date) IN ('09', '10')
ORDER  BY STRFTIME('%m-%d', birth_date);
-- Tom 09/09, Charlie 10/10
```

<div dir="rtl">

---

## 3 · CASE ו‑COALESCE

**השאלה:** איזה סוג מאמץ הוא כל אחד — "נאמן" (2+), "חד‑פעמי", או "מעולם לא"?

</div>

```sql
SELECT p.first_name,
       COUNT(ad.adoption_id) AS n,
       CASE WHEN COUNT(ad.adoption_id) >= 2 THEN 'loyal'
            WHEN COUNT(ad.adoption_id) = 1  THEN 'one-time'
            ELSE 'never' END AS label
FROM   person p
LEFT   JOIN adoption ad ON ad.adopter_id = p.person_id
WHERE  p.role = 'adopter'
GROUP  BY p.person_id
ORDER  BY n DESC, p.first_name;
```

```text
first_name  n  label
----------  -  --------
Dana        2  loyal
Lior        2  loyal
Shira       2  loyal
Eitan       1  one-time
Omer        1  one-time
Yossi       1  one-time
```

<div dir="rtl">

**תובנה:** חצי מהמאמצים חזרו לאמץ שוב. **המלצה:** רשימת תפוצה למאמצים קודמים — הם הקהל החם ביותר.

---

## 4 · JOIN של 3 טבלאות ויותר

**השאלה:** כל האימוצים — מי אימץ את מי, מאיזה מין, ובכמה. (מודול 21, תרגיל 3ג — בלי סינון לחיפה.)

---

## 5 · LEFT JOIN … IS NULL

**השאלה:** אילו חיות מעולם לא חוסנו? ⟵ Coco, Nala, Lily, Kiwi (מודול 21, סעיף 6.2).

**תובנה:** Nala ו‑Lily הן חתולות — ויש להן חיסונים מוגדרים. **שתיהן צריכות תור לווטרינר.**

---

## 6 · Nonequijoin

**השאלה:** קטגוריית גודל לכל חיה — לפי טבלת `size_band` (מודול 21, סעיף 5). שימושי לשיבוץ לכלובים.

---

## 7 · SUM(CASE …)

**השאלה:** כמה אימוצים "החזיקו", וכמה חזרו?

</div>

```sql
SELECT COUNT(*) AS adoptions,
       SUM(CASE WHEN returned_date IS NULL     THEN 1 ELSE 0 END) AS stayed,
       SUM(CASE WHEN returned_date IS NOT NULL THEN 1 ELSE 0 END) AS returned
FROM   adoption;
-- 9 | 8 | 1
```

<div dir="rtl">

**תובנה:** 89% הצלחה — אבל המדגם קטן. שווה לעקוב שנה נוספת.

---

## 8 · GROUP BY + HAVING

**השאלה:** אילו חיות קיבלו את אותו חיסון יותר מפעם אחת? ⟵ Luna (2), Rocky (3) — מודול 24, תרגיל 4ג. **זה תקין** — חיסון כלבת שנתי.

---

## 9 · GROUP BY לפי זמן

**השאלה:** הכנסות והוצאות לפי שנה ⟵ ה‑View `yearly_finance` (מודול 28, תרגיל 3א).

**תובנה:** ב‑2024 הגירעון היה 15,770 ₪. **אין בבסיס הנתונים טבלת תרומות** — וזו כנראה ההכנסה העיקרית. המלצה: להוסיף.

---

## 10 · תת‑שאילתה של ערך אחד

**השאלה:** אילו הוצאות גבוהות מהממוצע? ⟵ 9 הוצאות, כולן מזון, חשמל או ניתוחים (מודול 24, תרגיל 5ב).

---

## 11 · תת‑שאילתה מתואמת

**השאלה:** כמה זמן לקח לכל חיה למצוא בית? ⟵ סעיף 6 במודול (הקליטה האחרונה לפני כל אימוץ).

---

## 12 · צבירה על צבירה

**השאלה:** כמה עולה, בממוצע, חיה שהוציאו עליה כסף? ⟵ 747 ₪ (מודול 24, סעיף 9).

---

## 13 · UNION ALL

**השאלה:** מה ההיסטוריה המלאה של לונה — ברשימה אחת?

</div>

```sql
SELECT 'intake' AS event, i.intake_date AS dt
FROM   intake i JOIN animal a ON a.animal_id = i.animal_id WHERE a.name = 'Luna'
UNION  ALL
SELECT 'adoption', ad.adoption_date
FROM   adoption ad JOIN animal a ON a.animal_id = ad.animal_id WHERE a.name = 'Luna'
UNION  ALL
SELECT 'returned', ad.returned_date
FROM   adoption ad JOIN animal a ON a.animal_id = ad.animal_id
WHERE  a.name = 'Luna' AND ad.returned_date IS NOT NULL
ORDER  BY dt;
```

```text
event     dt
--------  ----------
intake    2023-03-14
adoption  2023-05-10
intake    2024-06-01
returned  2024-06-01
adoption  2025-07-01
```

<div dir="rtl">

**תובנה:** ציר זמן כזה הוא "התיק" של החיה — מה שמתנדבת צריכה לראות כשמשפחה שואלת על לונה.

---

## 14 · שאילתה על View

**השאלה:** החיות במקלט הכי הרבה זמן ⟵ `in_shelter` (מודול 28, תרגיל 3ב): Rocky 1,220 יום, Mitzi 1,198, Coco 1,087, Max 1,051.

---

## 15 · ⭐ השאלה הכי חשובה

**השאלה:** "כמה זמן חיה מחכה לבית — לפי מין?" (סעיף 6 במודול).

**למה דווקא היא?** כי היא עונה על **המטרה** של המקלט — למצוא בית לכל חיה — ומובילה ישר להמלצה: קמפיין לחיות הוותיקות. **בשאלה הזו הייתי פותח את המצגת.**

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[❓ לשאלות ההגנה](questions.md)**

</div>

</div>
