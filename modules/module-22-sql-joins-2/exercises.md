<div dir="rtl">

# מודול 22 — תרגילים

> 💪 **בסוף הדף — [תרגול בכיתה](#-תרגול-בכיתה--בית-הספר-עתיד):** 12 שאלות על בסיס נתונים אחר, [`school.sql`](../../resources/school-db/), שחוזר בכל שיעור SQL. מיועד לשיעור בכיתה.

> **הנחיות:** כל התרגילים על [בסיס הנתונים המוכן](../../resources/shelter-db/). **הריצו.**
>
> 🔢 **בכל תרגיל עם JOIN: לפני שמריצים — כתבו כמה שורות אתם מצפים לקבל.** אחר כך בדקו.
>
> ⚠️ אל תפתחו את [הפתרונות](solutions.md) לפני שניסיתם.
>
> **רמות:** 🟢 בסיסי · 🟡 בינוני · 🔴 מאתגר

---

## 🟢 תרגיל 1 — CROSS JOIN

**א.** כמה שורות יחזיר `species CROSS JOIN vaccine_type`? חזו, הריצו.

**ב.** לוח משמרות: כל מתנדב מחיפה × כל מין — שורה לכל צירוף (מי אחראי על איזה מין). מיינו לפי שם המתנדב.

**ג.** לכל מין — אילו חיסונים מוגדרים לו? כל המינים צריכים להופיע, גם מי שאין לו חיסון. (זה לא `CROSS` — איזה JOIN?)

---

## 🟢 תרגיל 2 — NATURAL ו‑USING

**א.** הריצו `SELECT COUNT(*) FROM adoption NATURAL JOIN animal;` ו‑`SELECT COUNT(*) FROM intake NATURAL JOIN animal;`. האם התוצאות הגיוניות? לפי אילו עמודות כל אחד חיבר?

**ב.** הריצו `SELECT COUNT(*) FROM animal NATURAL JOIN species;`. הסבירו את התוצאה.

**ג.** כתבו את סעיף ב' מחדש עם `USING`, כך שהתוצאה תהיה נכונה (20 שורות).

**ד.** האימוצים ששולם בהם 400 ומעלה: שם החיה ותאריך האימוץ — עם `USING (animal_id)`.

---

## 🟡 תרגיל 3 — לחזות, ואז לספור

חזו **לפני** שמריצים, ואז בדקו:

</div>

```sql
SELECT COUNT(*) FROM animal a JOIN       adoption ad ON ad.animal_id = a.animal_id;
SELECT COUNT(*) FROM animal a LEFT JOIN  adoption ad ON ad.animal_id = a.animal_id;
SELECT COUNT(*) FROM animal a RIGHT JOIN adoption ad ON ad.animal_id = a.animal_id;
SELECT COUNT(*) FROM animal a FULL JOIN  adoption ad ON ad.animal_id = a.animal_id;
```

<div dir="rtl">

**א.** למה `LEFT` מחזיר **21** ולא 20, אם יש 20 חיות?

**ב.** למה `RIGHT` שווה ל‑`JOIN`, ו‑`FULL` שווה ל‑`LEFT`? מה זה אומר על הנתונים?

---

## 🟡 תרגיל 4 — מה חסר?

**א.** לכל החיות (לא רק הזמינות): אילו חיסונים חסרים? שם החיה ושם החיסון החסר.

**ב.** ⭐ בתוצאה של א' — Bella, Daisy ו‑Zoe חסרות DHPP. בדקו את הסטטוס שלהן. האם זה באמת "חסר"? איך הייתם מסננים את התוצאה?

**ג.** לכל מאמץ — מאילו מינים הוא אימץ? כל צירוף של שם מאמץ ומין **פעם אחת** (רמז: `DISTINCT` ממודול 16). מי אימץ משני מינים שונים?

---

## 🔴 תרגיל 5 — שרשרת JOIN‑ים

**א.** כל האנשים, ולידם שם החיה שאימצו (אם אימצו). כל האנשים צריכים להופיע — 15 שורות.

**ב.** שנו את ה‑`JOIN` השני בסעיף א' (ל‑`animal`) ל‑`JOIN` רגיל. כמה שורות עכשיו? מי נעלם, ולמה?

**ג.** כל ההוצאות עם שם החיה **ושם המין**. כל 22 ההוצאות צריכות להופיע. כתבו קודם גרסה **שגויה** (11 שורות), ואחר כך תקנו.

**ד.** ⭐ כל הקליטות: שם החיה, שם המין, מי הביא (אם יש) והעיר שלו. אילו חיבורים `JOIN` ואילו `LEFT`? נמקו כל אחד לפי היחס.

---

## 🔴 תרגיל 6 — FULL OUTER JOIN

**א.** בין `animal` ל‑`expense`: הציגו רק את מי **שאין לו זוג** — משני הצדדים. כמה שורות?

**ב.** ⭐ צרו שתי טבלאות קטנות:

</div>

```sql
CREATE TABLE shift_jan (volunteer TEXT);
CREATE TABLE shift_feb (volunteer TEXT);
INSERT INTO shift_jan VALUES ('Ruti'), ('Noa'), ('Amir');
INSERT INTO shift_feb VALUES ('Noa'), ('Amir'), ('Tamar');
```

<div dir="rtl">

כתבו שאילתה אחת שמציגה כל מתנדב ועמודה `status`: `'january only'`, `'february only'` או `'both'`. (רמז: `FULL JOIN` + `CASE` + `COALESCE`.)

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[✅ לפתרונות](solutions.md)**

</div>

</div>

<!-- w3schools:start -->
<div dir="rtl">

---

## 🌐 תרגול נוסף ב‑W3Schools

📖 **לקריאה ב‑W3Schools:** [LEFT JOIN](https://www.w3schools.com/sql/sql_join_left.asp)

> 🌐 **פותחים את [עורך ה‑SQL של W3Schools](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all)**, מוחקים את מה שכתוב בו, כותבים שאילתה ולוחצים **Run SQL**. בסיס הנתונים שם הוא של חברה לממכר מזון: `Customers`, `Orders`, `OrderDetails`, `Products`, `Categories`, `Suppliers`, `Shippers` ו‑`Employees`. לחיצה על שם טבלה בצד מציגה את התוכן שלה.
>
> ⚠️ בבסיס הנתונים של W3Schools **אפשר רק לקרוא** (`SELECT`). טקסט כותבים שם בין גרשיים **בודדים**: `'Germany'`.

**W1.** הלקוחות **שלא הזמינו אף פעם** (`LEFT JOIN` + `IS NULL`).


</div>
<!-- w3schools:end -->

<!-- classroom:start -->
<div dir="rtl">

---

## 💪 תרגול בכיתה — בית הספר "עתיד"

> 🏫 **בסיס נתונים אחר, 12 שאלות.** הקטע הזה חוזר בסוף התרגילים של **כל** שיעור SQL, תמיד על אותו בסיס נתונים — [`school.sql`](../../resources/school-db/): 7 טבלאות, 18 תלמידים. השאלות הן שמתקדמות בקושי משיעור לשיעור.
>
> **טוענים פעם אחת:** [**פתיחה להעתקה**](https://raw.githubusercontent.com/AhmadKais/sql-course-heb/main/resources/school-db/school.sql) → `Ctrl+A`, `Ctrl+C` → מדביקים ב‑[OneCompiler (SQLite)](https://onecompiler.com/sqlite) → **Run**. צריך להופיע `students_loaded = 18`. (או: [**כל הפקודות בבלוק אחד**](../../resources/school-db/README.md#-כל-הפקודות-להעתקה), עם כפתור העתקה.)
>
> 📅 **תאריך הייחוס: `'2026-09-21'`** — השתמשו בו במקום `DATE('now')`. · ⚠️ ה[פתרונות](solutions.md) מחכים בסוף — אחרי שניסיתם.

</div>

```text
Cities    (CityCode, CityName)
Teachers  (TeacherCode, FirstName, LastName, Subject, HireDate, Salary, CityCode, Phone)
Classes   (ClassCode, ClassName, Grade, TeacherCode, RoomNumber)
Courses   (CourseCode, CourseName, TeacherCode, WeeklyHours)
Students  (StudentId, FirstName, LastName, ClassCode, Gender, BirthDate, CityCode, EnrollDate, Phone)
Grades    (StudentId, CourseCode, Term, Grade)          -- PK: StudentId + CourseCode + Term
Absences  (AbsenceId, StudentId, AbsenceDate, Excused, Reason)
```

<div dir="rtl">

**אותם חיבורים — בתחביר ANSI.** `JOIN … ON` במקום פסיק ו‑`WHERE`, ומשם ל‑`OUTER JOIN` על שני הכיוונים.

**ש1.** כתבו מחדש בתחביר `INNER JOIN … ON`: כל תלמיד עם שם הכיתה שלו.

**ש2.** אותה שאילתה עם `JOIN … USING (ClassCode)`. מתי `USING` אפשרי, ומה החיסרון שלו?

**ש3.** ⚠️ **`NATURAL JOIN` — המלכודת.** הריצו:

</div>

```sql
SELECT * FROM Grades NATURAL JOIN Classes;
```

<div dir="rtl">

**כמה שורות קיבלתם?** עכשיו הסתכלו בסכמה ו**מצאו לבד** על איזו עמודה SQL חיבר. ⚠️ הריצו גם `SELECT COUNT(*) FROM Students NATURAL JOIN Classes;` — למה **שם** זה כן עובד?

**ש4.** `SELECT COUNT(*) FROM Classes CROSS JOIN Cities;` — מה קיבלתם, ומה ההבדל בין `CROSS JOIN` לבין פסיק בלי `WHERE`?

**ש5.** לכל מקצוע ושם המורה שלו, פעמיים:

**א.** עם `INNER JOIN` — כמה שורות?

**ב.** עם `LEFT JOIN` — כמה שורות? **מה הופיע בשורה הנוספת?**

**ש6.** מצאו את התשובה לשאלה ההפוכה: **איזה מורה לא מלמד כלום**. פעם אחת עם `RIGHT JOIN`, ופעם אחת — אותה תוצאה בדיוק — עם `LEFT JOIN` בלבד, על ידי **החלפת סדר הטבלאות**.

**ש7.** `FULL OUTER JOIN` בין `Courses` ל‑`Teachers` — 8 שורות. **הסבירו מאיפה כל אחת מהשתיים המיוחדות.**

> 💡 `RIGHT JOIN` ו‑`FULL OUTER JOIN` קיימים ב‑SQLite רק מגרסה 3.39 ומעלה. אם האתר מחזיר `syntax error` — הגרסה שלו ישנה; פתרו את ש6 וש7 **בעיפרון**, והריצו את גרסת ה‑`LEFT JOIN`.

**ש8.** אילו תלמידים **לא נעדרו אף פעם**?

**ש9.** אילו תלמידים **אין להם אף ציון**?

**ש10.** שלוש טבלאות בתחביר ANSI: מי לא נבחן, באיזה מקצוע? (שם התלמיד + שם המקצוע, שם הציון `NULL`.)

**ש11.** ⚠️ **`WHERE` שהורג `LEFT JOIN`.** המנהלת ביקשה: *"כל התלמידים, ולצד כל אחד ההיעדרויות **הלא מאושרות** שלו — גם אם אין לו."* תלמיד כתב:

</div>

```sql
SELECT Students.FirstName, Absences.AbsenceDate
FROM   Students LEFT JOIN Absences ON Absences.StudentId = Students.StudentId
WHERE  Absences.Excused = 0;
```

<div dir="rtl">

הריצו. **קיבלתם 9 שורות במקום 22.** איפה הטעות, ואיך מתקנים אותה בלי לשנות אף מילה אחרת חוץ ממקום אחד?

**ש12.** סכמו בטבלה: מה מחזיר כל אחד מ‑`INNER` / `LEFT` / `RIGHT` / `FULL OUTER` / `CROSS`, ומתי תבחרו בכל אחד.

</div>
<!-- classroom:end -->
