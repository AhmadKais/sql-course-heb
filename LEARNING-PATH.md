<div dir="rtl">

# 🧭 מסלול הלימוד המומלץ — עיצוב ו‑SQL בשילוב

> **למה הדף הזה קיים?**
> תכנית הלימודים של משרד החינוך בנויה בשני חלקים: **15 פרקי עיצוב** ורק אז **17 פרקי SQL**.
> זה נכון מבחינה לוגית — אבל בכיתה זה אומר חודשים של תיאוריה לפני שנוגעים במקלדת.
>
> הדף הזה מציע **סדר הוראה אחר** לאותם 32 פרקים: בכל יחידה — שיעור עיצוב **ושיעור SQL** שמשתמש בו.
> התלמידים כותבים שאילתות **מהיחידה השנייה**, על בסיס נתונים מוכן של המקלט, ובונים את בסיס הנתונים שלהם בעצמם כשמגיעים לפרק 12.
>
> 📌 **[SYLLABUS.md](SYLLABUS.md)** נשאר המפה הרשמית לפי סדר הפרקים. **הדף הזה** הוא סדר ההוראה.

---

## העיקרון: כל מושג עיצובי — לצד ה‑SQL שמממש אותו

| מושג העיצוב | ה‑SQL שמשתמש בו | למה הם הולכים יחד |
|--------------|------------------|--------------------|
| יחסים (פרק 5) | `JOIN` (פרקים 21–22) | חיבור טבלאות **הוא** היחס — מנקודת מבט אחרת |
| נרמול (פרק 6) | `GROUP BY` (פרקים 23–24) | הדרך למצוא כפילויות היא לספור אותן |
| אילוצים (פרק 7) | אילוצים ב‑SQL (פרק 27) | אותם חוקים, בקוד |
| מעבר לטבלאות (פרק 12) | `CREATE TABLE` (פרק 26) | המיפוי מסתיים בהרצה |
| מעקב אחר שינויים (פרק 10) | `VIEW` + טרנזקציות (28, 32) | היסטוריה נשאלת דרך View; שינוי נשמר בטרנזקציה |

---

## המסלול — 13 יחידות

</div>

```text
UNIT | DESIGN LESSON (chapter)              | SQL LESSON (chapter)                 | What the student can DO after
-----+--------------------------------------+--------------------------------------+---------------------------------
  1  | 0 Intro + 1 Foundations              | --                                   | explain data vs information
  2  | 2 The data model                     | 16 Anatomy of SQL + 17 WHERE         | SELECT animals by name/status
  3  | 3 ERD                                | 18 ORDER BY + 19 Functions           | sort, format dates, calculate age
  4  | 4 Subtypes & supertypes              | 20 Functions 2 (CASE, NULL)          | label rows by type with CASE
  5  | 5 Relationships                      | 21 + 22 JOINs                        | list every animal with its adopter
  6  | 6 Normalization                      | 23 + 24 Aggregates, GROUP BY,        | count duplicates, average stay,
     |                                      |    subqueries                        |  cost per animal
  7  | 7 Constraints                        | 27 Constraints in SQL                | write CHECK / UNIQUE / FK
  8  | 12 From model to tables              | 26 DDL -- CREATE TABLE               | *** build the shelter DB yourself
  9  | 8 The consultant + 9 Project I       | 25 DML -- INSERT / UPDATE / DELETE   | populate your own project DB
 10  | 10 Tracking changes                  | 28 Views + 32 Transactions           | history via VIEW; safe updates
 11  | 11 Generic models                    | 29 Sequences, indexes, synonyms      | surrogate keys done properly
 12  | 13 SQL I (project mgmt) + 14 SDLC    | 30 Users & permissions               | grant a volunteer read-only access
 13  | 15 The presentation                  | 31 Final project                     | present model + working DB

     Units 2-7:  students QUERY a ready-made shelter database (resources/shelter-db/)
     Unit 8+:    students BUILD and populate their own, from their own ERD
```

<div dir="rtl">

### מה כל יחידה דורשת

| יחידה | שיעור העיצוב | שיעור ה‑SQL | הקבצים |
|-------|---------------|-------------|---------|
| **1** | [מודול 0](modules/module-00-intro/) + [מודול 1](modules/module-01-foundations/) | — | |
| **2** | [מודול 2](modules/module-02-data-model/) | [מודול 16](modules/module-16-sql-basics/) + [מודול 17](modules/module-17-sql-where/) ✅ | [בסיס הנתונים המוכן](resources/shelter-db/) |
| **3** | [מודול 3](modules/module-03-erd/) | [מודול 18](modules/module-18-sql-order-by/) + מודול 19 🔜 | |
| **4** | [מודול 4](modules/module-04-subtypes-supertypes/) | מודול 20 🔜 | |
| **5** | [מודול 5](modules/module-05-relationships/) | מודול 21 + 22 🔜 | |
| **6** | [מודול 6](modules/module-06-normalization/) | מודול 23 + 24 🔜 | |
| **7** | [מודול 7](modules/module-07-constraints/) | מודול 27 🔜 | |
| **8** | מודול 12 🔜 | מודול 26 🔜 | ⭐ מכאן — בסיס נתונים משלכם |
| **9** | [מודול 8](modules/module-08-consultant/) + [מודול 9](modules/module-09-project-1/) | מודול 25 🔜 | |
| **10** | [מודול 10](modules/module-10-tracking-changes/) | מודול 28 + 32 🔜 | |
| **11** | [מודול 11](modules/module-11-generic-models/) | מודול 29 🔜 | |
| **12** | מודול 13 + 14 🔜 | מודול 30 🔜 | |
| **13** | מודול 15 🔜 | מודול 31 🔜 | |

---

## למה דווקא הסדר הזה

**1. SQL מתחיל ביחידה 2, לא ביחידה 16.**
תלמיד שכותב `SELECT name FROM animal WHERE species = 'Dog'` בשבוע השני מבין **בשביל מה** לומדים ישויות ומאפיינים. התיאוריה מקבלת משמעות מיד.

**2. כל זוג הוא זוג אמיתי, לא מכני.**
פרק 5 (יחסים) לצד `JOIN` — כי `JOIN` הוא היחס. פרק 6 (נרמול) לצד `GROUP BY` — כי כך מוצאים כפילות. פרק 12 (מיפוי) לצד `CREATE TABLE` — כי המיפוי מסתיים בהרצה.

**3. פרק 12 מוקדם, פרק 8 מאוחר.**
בסדר המקורי, "מעבר לטבלאות" הוא פרק 12 ו"תפקיד היועץ" הוא פרק 8. הפכנו: התלמידים בונים את בסיס הנתונים שלהם **ביחידה 8**, ורק אז לומדים להציג אותו ללקוח. כך ההצגה (פרק 8) והפרויקט (פרק 9) נעשים מול **מערכת עובדת**, לא מול תרשים.

**4. שני בסיסי נתונים, בכוונה.**
ביחידות 2–7 התלמידים שואלים בסיס נתונים **מוכן** של המקלט — הם עוד לא יודעים לבנות אחד. ביחידה 8 הם בונים **משלהם** מה‑ERD שעיצבו. ההשוואה בין השניים היא בעצמה שיעור.

**5. פרק 13 ("SQL I") כמעט מתייתר.**
בסדר המקורי הוא "טעימה ראשונה" של SQL. במסלול הזה הטעימה כבר הייתה ביחידה 2, אז מה שנשאר ממנו — ניהול פרויקט ועבודת צוות — מצטרף לפרק 14.

---

## איך להשתמש בזה בכיתה

| אם אתם... | עשו כך |
|-----------|---------|
| **מלמדים פעמיים בשבוע** | שיעור א' = עיצוב, שיעור ב' = SQL. יחידה בשבוע |
| **מלמדים פעם בשבוע** | חצי שיעור לכל אחד, או יחידה על פני שבועיים |
| **חייבים ללכת לפי סדר הפרקים** | [SYLLABUS.md](SYLLABUS.md) — הכול עדיין שם, לפי המספור המקורי |
| **רוצים רק SQL בהתחלה** | יחידות 2–7, עמודת ה‑SQL בלבד. העיצוב יחכה |

> 💡 **מספרי המודולים בתיקיות לא משתנים.** `module-21-joins` נשאר 21 גם אם מלמדים אותו ביחידה 5. המספר הוא **הפרק בתכנית הלימודים**; היחידה היא **מתי מלמדים**. כך אפשר תמיד לחזור לסדר המקורי.

---

<div align="center">

**[🏠 דף הקורס](README.md)** · **[📚 המפה הרשמית — 32 פרקים](SYLLABUS.md)** · **[🐾 בסיס הנתונים המוכן](resources/shelter-db/)**

</div>

</div>
