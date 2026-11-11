<div dir="rtl">

# מודול 28 — SQL: שאילתות שמורות (Views)

> **פרק 28 בתכנית הלימודים** · 2 שעות עיוני + 2 שעות מעשי
> **נושאים:** יצירת View · עדכון נתונים דרך View · ניהול

> 🧭 **במסלול המשולב:** יחידה 10, לצד [מודול 10 — עיצוב למעקב אחר שינויים](../module-10-tracking-changes/) ו[מודול 32 — טרנזקציות](../module-32-sql-transactions/). **היסטוריה נשמרת בטבלאות; ה"מצב הנוכחי" נשאל דרך View.**

---

## 🎯 מה תדעו בסוף המודול

- [ ] להסביר מהו View — ומה ההבדל בינו לבין טבלה
- [ ] ליצור View, לשאול אותו, ולמחוק אותו
- [ ] לנמק **ארבע סיבות** להשתמש ב‑View: פשטות, עקביות, אבטחה, יציבות
- [ ] להבין מתי אפשר **לעדכן** נתונים דרך View — ב‑Oracle וב‑SQLite
- [ ] להכיר `WITH CHECK OPTION` ו‑`WITH READ ONLY`
- [ ] להשתמש ב‑View כדי להציג **מצב נוכחי** מתוך טבלת היסטוריה (מודול 10)

---

## 🗺️ מפת המודול

| # | הסעיף |
|---|--------|
| 1 | [מה זה View](#1-מה-זה-view) |
| 2 | [CREATE VIEW](#2-create-view) |
| 3 | [View תמיד עדכני](#3-view-תמיד-עדכני) |
| 4 | [ארבע סיבות ל‑View](#4-ארבע-סיבות-לview) |
| 5 | [View ומעקב אחר שינויים](#5-view-ומעקב-אחר-שינויים) |
| 6 | [עדכון נתונים דרך View](#6-עדכון-נתונים-דרך-view) |
| 7 | [ניהול Views](#7-ניהול-views) |
| 8 | [Materialized View — הצצה](#8-materialized-view--הצצה) |
| 9 | [חמש טעויות נפוצות](#9-חמש-טעויות-נפוצות) |
| 10 | [סיכום המודול](#10-סיכום-המודול) |

---

## 1. מה זה View

**View** הוא **שאילתה שמורה עם שם**. נראה כמו טבלה, שואלים אותו כמו טבלה — אבל **אין בו נתונים משלו**. בכל פעם ששואלים אותו, השאילתה שבתוכו רצה מחדש על הטבלאות האמיתיות.

</div>

```text
   TABLE                                 VIEW
   -----                                 ----
   stores rows on disk                   stores only the SELECT text
   INSERT puts data into it              its data comes from other tables
   a snapshot that you maintain          always up to date -- recomputed on every query

   animal, species  ---->  [ CREATE VIEW available_animal AS SELECT ... ]  ---->  you
   (real data)              (a saved question)                                    (see a "table")
```

<div dir="rtl">

> 💡 **משל:** טבלה היא **מחברת** עם נתונים. View הוא **פתק עם שאלה** — "תראה לי את כל החיות הזמינות, עם שם המין והגיל". הפתק לא מכיל תשובה; כל פעם שקוראים אותו, הולכים למחברת ובודקים מחדש.

---

## 2. CREATE VIEW

</div>

```sql
CREATE VIEW available_animal AS
SELECT a.animal_id,
       a.name,
       s.name AS species,
       a.breed,
       a.sex,
       CAST((JULIANDAY('2026-09-21') - JULIANDAY(a.birth_date)) / 365.25 AS INTEGER) AS age,
       a.weight_kg,
       s.adoption_fee
FROM   animal a
JOIN   species s ON s.species_id = a.species_id
WHERE  a.status = 'available';
```

<div dir="rtl">

**ועכשיו — שואלים כמו טבלה:**

</div>

```sql
SELECT name, species, age, adoption_fee
FROM   available_animal
ORDER  BY species, name;
```

```text
name    species  age  adoption_fee
------  -------  ---  ------------
Felix   Cat      7    250.0
Lily    Cat           250.0
Mitzi   Cat      3    250.0
Oscar   Cat      4    250.0
Rex     Dog      9    400.0
Rocky   Dog      6    400.0
Shadow  Dog      5    400.0
Coco    Parrot        150.0
Bunny   Rabbit   2    100.0
```

```sql
-- a View can be filtered, grouped and joined like any table
SELECT species, COUNT(*) FROM available_animal GROUP BY species;
```

<div dir="rtl">

> 🔑 **ה‑JOIN, ה‑`CAST` והחישוב של הגיל — נכתבו פעם אחת.** מי שמשתמש ב‑View לא צריך לדעת ש‑`species` היא טבלה נפרדת, ולא איך מחשבים גיל. הוא שואל `available_animal`.

---

## 3. View תמיד עדכני

</div>

```sql
SELECT COUNT(*) FROM available_animal;              -- 9

UPDATE animal SET status = 'available' WHERE animal_id = 9;   -- Nala leaves quarantine

SELECT COUNT(*) FROM available_animal;              -- 10  -- no need to "refresh" anything
```

<div dir="rtl">

**השוו למודול 25, תרגיל 6ב:** שם בנינו את `vip_adopter` עם `INSERT … SELECT` — **טבלה**. אם מחר מישהו יאמץ חיה שנייה, הטבלה לא תדע. View היה מתעדכן לבד.

| | טבלה מ‑`SELECT` | View |
|---|---|---|
| הנתונים | העתק — תמונת מצב | אין — השאילתה רצה מחדש |
| מתעדכן? | ❌ רק אם ממלאים מחדש | ✅ תמיד |
| מהירות | מהיר (כבר מחושב) | השאילתה רצה בכל פעם |
| מתי | ארכיון, גיבוי, "נכון לתאריך" | כמעט תמיד |

---

## 4. ארבע סיבות ל‑View

### 4.1 פשטות — שאילתה מסובכת, שם פשוט

</div>

```sql
CREATE VIEW animal_cost AS
SELECT a.animal_id, a.name,
       COALESCE((SELECT SUM(e.amount) FROM expense     e WHERE e.animal_id = a.animal_id), 0) AS expenses,
       COALESCE((SELECT SUM(v.cost)   FROM vaccination v WHERE v.animal_id = a.animal_id), 0) AS vaccines
FROM   animal a;

SELECT name, expenses, vaccines, expenses + vaccines AS total
FROM   animal_cost
ORDER  BY total DESC
LIMIT  5;
```

```text
name   expenses  vaccines  total
-----  --------  --------  ------
Max    2520.0    175.0     2695.0
Rex    1200.0    175.0     1375.0
Luna   890.0     260.0     1150.0
Rocky  600.0     345.0     945.0
Bella  650.0     80.0      730.0
```

<div dir="rtl">

> 💡 **שימו לב: תתי‑שאילתות, לא JOIN** — זוכרים את מלכודת הכפל של מודול 23 (Rocky × 4)? ה‑View פותר אותה **פעם אחת**, ואף אחד לא ייפול בה שוב.

### 4.2 עקביות — הגדרה אחת לכולם

"חיה זמינה" — זה `status = 'available'`? ומה עם חיה בהסגר שמשתחררת מחר? אם כל דוח כותב את התנאי לבד — יהיו חמש הגדרות שונות. **ה‑View הוא ההגדרה הרשמית.** משנים אותו במקום אחד — וכל הדוחות מתעדכנים.

### 4.3 אבטחה — להראות רק חלק

</div>

```sql
-- volunteers may see people's names and cities -- not their phone numbers
CREATE VIEW public_person AS
SELECT person_id, first_name, city, role
FROM   person;
```

<div dir="rtl">

נותנים למתנדבים הרשאה ל‑`public_person` — **ולא** ל‑`person` (מודול 30). הם לא יכולים לראות טלפונים, כי העמודה פשוט לא קיימת מבחינתם. זה נקרא **הסתרת עמודות**; עם `WHERE` — **הסתרת שורות** (למשל רק החיות של הסניף שלהם).

### 4.4 יציבות — לשנות טבלאות בלי לשבור דוחות

נניח שמחר מפצלים את `person` ל‑`volunteer`, `adopter` ו‑`vet` (מודול 4). עשרות דוחות שקוראים מ‑`person` יישברו. אבל אם הם קוראים מ‑View — מגדירים מחדש את ה‑View עם `UNION ALL` של שלוש הטבלאות, **והדוחות לא מרגישים כלום.** ה‑View הוא **שכבת הפרדה** בין מבנה האחסון לבין מי שמשתמש בנתונים.

---

## 5. View ומעקב אחר שינויים

במודול 10 למדנו: **לא דורסים היסטוריה.** לונה אומצה, הוחזרה ואומצה שוב — ושלושת האירועים שמורים. אבל רוב השאלות הן על **ההווה**: "איפה לונה **עכשיו**?"

</div>

```sql
CREATE VIEW current_home AS
SELECT ad.animal_id, a.name,
       p.first_name || ' ' || p.last_name AS adopter,
       ad.adoption_date
FROM   adoption ad
JOIN   animal a ON a.animal_id = ad.animal_id
JOIN   person p ON p.person_id = ad.adopter_id
WHERE  ad.returned_date IS NULL;               -- not returned = current

SELECT * FROM current_home WHERE name = 'Luna';
```

```text
animal_id  name  adopter       adoption_date
---------  ----  ------------  -------------
1          Luna  Eitan Shalev  2025-07-01      <- only the current adoption, not Dana's
```

<div dir="rtl">

> 🔑 **הדפוס: טבלה שומרת את כל ההיסטוריה ⟵ View מציג את המצב הנוכחי.** כך מקבלים את שני העולמות: אף נתון לא נמחק, ומי שרק רוצה לדעת "מה עכשיו" — לא צריך לדעת על `returned_date`. זה בדיוק השילוב של מודול 10 + מודול 28 ביחידה 10.

---

## 6. עדכון נתונים דרך View

### 6.1 ב‑SQLite — Views לקריאה בלבד

</div>

```sql
UPDATE available_animal SET weight_kg = 30 WHERE name = 'Rocky';
-- Error: cannot modify available_animal because it is a view
```

<div dir="rtl">

ב‑SQLite אי אפשר `INSERT` / `UPDATE` / `DELETE` על View (אלא עם טריגר `INSTEAD OF` — מעבר לתכנית). **מעדכנים את הטבלה עצמה.**

### 6.2 ב‑Oracle — View "פשוט" אפשר לעדכן

ב‑Oracle, `UPDATE` דרך View עובד — **אם** בסיס הנתונים יכול לדעת בדיוק איזו שורה באיזו טבלה לשנות:

| ב‑View יש… | אפשר לעדכן? | למה |
|-------------|--------------|-----|
| טבלה אחת, עמודות פשוטות | ✅ | כל שורה ב‑View = שורה אחת בטבלה |
| `GROUP BY`, `SUM`, `COUNT`, `DISTINCT` | ❌ | שורה ב‑View = הרבה שורות. איזו לשנות? |
| עמודה מחושבת (`age`) | ❌ על העמודה הזאת | אין עמודת `age` בטבלה |
| `JOIN` | חלקית — רק את הטבלה "המובילה" | מורכב — עדיף לא |

### 6.3 `WITH CHECK OPTION` — לא לברוח מה‑View

</div>

```sql
-- Oracle
CREATE OR REPLACE VIEW dogs AS
SELECT animal_id, name, species_id, status FROM animal WHERE species_id = 1
WITH CHECK OPTION;

UPDATE dogs SET species_id = 2 WHERE name = 'Rex';
-- ORA-01402: view WITH CHECK OPTION where-clause violation
```

<div dir="rtl">

בלי `CHECK OPTION`, ה‑`UPDATE` היה מצליח — ו‑Rex היה **נעלם** מה‑View `dogs` (הוא כבר לא כלב). `WITH CHECK OPTION` אוסר שינוי שמוציא שורה מה‑`WHERE` של ה‑View. **`WITH READ ONLY`** — אוסר כל שינוי דרך ה‑View.

---

## 7. ניהול Views

</div>

```sql
-- list the views (SQLite)
SELECT name FROM sqlite_master WHERE type = 'view';
-- Oracle: SELECT view_name, text FROM user_views;

-- change a View
DROP VIEW IF EXISTS animal_cost;          -- SQLite: drop and create again
CREATE VIEW animal_cost AS ...;
-- Oracle: CREATE OR REPLACE VIEW animal_cost AS ...;   (one step, keeps permissions)

-- remove a View -- the tables and data are NOT touched
DROP VIEW available_animal;
```

<div dir="rtl">

> ⚠️ **View תלוי בטבלאות.** אם מוחקים או משנים שם של עמודה שה‑View משתמש בה — ה‑View נשבר, ושגיאה תופיע רק **כששואלים אותו**. לפני `ALTER TABLE` — בדקו אילו Views משתמשים בטבלה.

> 💡 **מוסכמת שמות:** יש שנותנים ל‑Views קידומת (`v_available_animal`) כדי להבדיל מטבלאות. בקורס הזה — שם תיאורי, בלי קידומת: מי שמשתמש בו לא צריך לדעת שזה View (סעיף 4.4).

---

## 8. Materialized View — הצצה

View רגיל מחשב מחדש **בכל** שאילתה. על מיליוני שורות, דוח מסובך יכול לקחת דקות. **Materialized View** (Oracle, PostgreSQL) **שומר את התוצאה** ומרענן אותה מדי פעם (כל לילה, כל שעה):

</div>

```sql
-- Oracle
CREATE MATERIALIZED VIEW monthly_expense
REFRESH COMPLETE ON DEMAND
AS SELECT TRUNC(expense_date, 'MM') AS month, category, SUM(amount) AS total
   FROM   expense GROUP BY TRUNC(expense_date, 'MM'), category;
```

<div dir="rtl">

| | View | Materialized View | טבלה מ‑`SELECT` |
|---|---|---|---|
| שומר נתונים | ❌ | ✅ | ✅ |
| עדכני | תמיד | נכון לרענון האחרון | לעולם לא, אלא ידנית |
| מהיר | כמו השאילתה | ✅ מאוד | ✅ מאוד |

> 💡 ב‑SQLite אין Materialized View — בונים טבלה עם `CREATE TABLE … AS SELECT` ומוחקים ובונים מחדש כשצריך.

---

## 9. חמש טעויות נפוצות

| # | הטעות | מה קורה | התיקון |
|---|-------|----------|---------|
| 1 | **לחשוב שה‑View שומר נתונים** | "מחקתי את ה‑View — הנתונים נמחקו?" לא! | View = שאילתה. הנתונים בטבלאות |
| 2 | **טבלה מ‑`SELECT` כשרציתם View** | נתונים מיושנים בדוחות | `CREATE VIEW` |
| 3 | **`UPDATE` על View ב‑SQLite** | `cannot modify … because it is a view` | לעדכן את הטבלה |
| 4 | **`SELECT *` בתוך View** | עמודה חדשה בטבלה משנה את ה‑View; ב‑Oracle ה‑`*` "ננעל" ברגע היצירה | לרשום עמודות במפורש |
| 5 | **View על View על View** | איטי, וקשה להבין מה קורה | שתי שכבות לכל היותר |

---

## 10. סיכום המודול

<div align="center">

### 🧠 שש נקודות

</div>

1. **View = שאילתה שמורה עם שם.** נראה כמו טבלה, בלי נתונים משלו — **תמיד עדכני**.
2. **`CREATE VIEW name AS SELECT …`** · `DROP VIEW` · ב‑Oracle `CREATE OR REPLACE VIEW`.
3. **ארבע סיבות:** פשטות (מסתיר JOIN‑ים), עקביות (הגדרה אחת), אבטחה (רק חלק מהעמודות/שורות), יציבות (מפריד בין אחסון לשימוש).
4. **היסטוריה בטבלה, הווה ב‑View** — `WHERE returned_date IS NULL`. ההשלמה של מודול 10.
5. **עדכון דרך View:** ב‑SQLite — אסור. ב‑Oracle — רק ב‑View פשוט; `WITH CHECK OPTION` / `WITH READ ONLY`.
6. **Materialized View** שומר תוצאה ומתרענן — מהירות במחיר של עדכניות.

<div align="center">

---

*"טבלה עונה: מה נשמר.*
*View עונה: מה שואלים."*

---

</div>

## 📎 המשך

| | |
|---|---|
| ❓ | [שאלות ותשובות](questions.md) |
| ✏️ | [תרגילים](exercises.md) |
| ✅ | [פתרונות](solutions.md) |
| ⬅️ | [מודול 27 — SQL: אילוצים](../module-27-sql-constraints/) |
| ➡️ | [מודול 29 — SQL: אובייקטים נוספים](../module-29-sql-objects/) |
| 🏠 | [חזרה לדף הקורס](../../) |

</div>
