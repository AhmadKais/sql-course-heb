<div dir="rtl">

# מודול 17 — תרגילים

> 💪 **בסוף הדף — [תרגול בכיתה](#-תרגול-בכיתה--בית-הספר-עתיד):** 12 שאלות על בסיס נתונים אחר, [`school.sql`](../../resources/school-db/), שחוזר בכל שיעור SQL. מיועד לשיעור בכיתה.

> **הנחיות:** כל התרגילים על [בסיס הנתונים המוכן](../../resources/shelter-db/). **הריצו** כל שאילתה. רשמו כמה שורות חזרו — זו חלק מהתשובה.
>
> ⚠️ אל תפתחו את [הפתרונות](solutions.md) לפני שניסיתם.
>
> **רמות:** 🟢 בסיסי · 🟡 בינוני · 🔴 מאתגר

---

## 🟢 תרגיל 1 — השוואות בסיסיות

לכל שאלה: השאילתה + **מספר השורות**.

**א.** כל החתולים (`species_id = 2`) — שם וגזע.

**ב.** חיות ששוקלות **פחות מ‑5 ק"ג**.

**ג.** אנשים ש**אינם** מאמצים.

**ד.** הוצאות **מעל 1,000 ₪**.

**ה.** אימוצים שבהם שולמו **בדיוק 200 ₪**.

---

## 🟢 תרגיל 2 — טקסט ותאריכים

**א.** מצאו את החיה בשם `Rocky`. ואז נסו `rocky`. **מה קרה, ולמה?**

**ב.** חיות שנולדו **אחרי** 1 בינואר 2022.

**ג.** הוצאות **בשנת 2024** (מ‑01/01 עד 31/12). שתי דרכים: עם `>=`/`<=`, ועם `BETWEEN`.

**ד.** אנשים שהצטרפו **לפני** 2020.

**ה.** ⚠️ נסו: `WHERE expense_date > '01/01/2025'`. כמה שורות? **למה זה שגוי?**

---

## 🟢 תרגיל 3 — BETWEEN ו‑IN

**א.** חיות במשקל **10–30 ק"ג** (כולל). כתבו עם `BETWEEN` **וגם** בלי.

**ב.** חיות שהסטטוס שלהן `medical` **או** `quarantine` **או** `deceased`. עם `IN`.

**ג.** אנשים מ**חיפה, נשר או כרמיאל**.

**ד.** הוצאות בקטגוריות שאינן `food` ולא `utilities`. עם `NOT IN`.

**ה.** חיסונים שניתנו **ברבעון השני של 2024** (אפריל–יוני).

---

## 🟢 תרגיל 4 — LIKE

**א.** חיות ששמן מתחיל ב‑`S`.

**ב.** חיות ששמן מסתיים ב‑`y`.

**ג.** חיות ששמן **מכיל** את האות `e`.

**ד.** חיות ששמן הוא **בדיוק 4 אותיות**.

**ה.** אנשים ששם משפחתם מתחיל ב‑`L`.

**ו.** הוצאות שהתיאור שלהן מכיל את המילה `food`.

**ז.** ⚠️ מה מחזיר `WHERE name LIKE 'Luna'`? ומה `WHERE name LIKE 'Lun'`? **הסבירו את ההבדל.**

---

## 🟡 תרגיל 5 — NULL

**א.** חיות **בלי** שבב. כמה?

**ב.** חיות **עם** שבב. כמה? האם א' + ב' = 20?

**ג.** ⚠️ הריצו `WHERE chip_number = NULL`. כמה שורות? **למה?**

**ד.** חיות **בלי** גזע ידוע **ובלי** תאריך לידה — שני התנאים יחד.

**ה.** הוצאות **כלליות** — שאינן משויכות לחיה. מה מזהה אותן?

**ו.** אנשים בלי מספר טלפון.

**ז.** ⭐ חיות ששוקלות מעל 20 ק"ג **או** שאין להן משקל רשום. (רמז: יש כאלה? בדקו.)

---

## 🟡 תרגיל 6 — AND / OR / NOT

לכל שאלה: השאילתה + מספר השורות.

**א.** כלבים ששוקלים **מעל 25 ק"ג**.

**ב.** חיות שהן **או** כלבים **או** שוקלות מעל 25 ק"ג.

**ג.** חתולים **זמינים לאימוץ**.

**ד.** מתנדבים **מחיפה**.

**ה.** חיות ש**אינן** כלבים ו**אינן** חתולים.

**ו.** הוצאות רפואיות **מעל 500 ₪** **בשנת 2024**.

---

## 🟡 תרגיל 7 — המלכודת

רותי מבקשת: *"כלבים וחתולים שזמינים לאימוץ."*

**א.** כתבו בלי סוגריים: `species_id = 1 OR species_id = 2 AND status = 'available'`. **כמה שורות?** רשמו את שמות החיות.

**ב.** הוסיפו סוגריים. **כמה שורות עכשיו?**

**ג.** אילו חיות היו ב‑א' ואינן ב‑ב'? **למה הן נכנסו?**

**ד.** כתבו את השאילתה בפעם השלישית — עם `IN` ובלי `OR` בכלל.

**ה.** רותי מבקשת עכשיו: *"כלבים זמינים, או חתולים בהסגר."* כתבו נכון. **האם כאן צריך סוגריים?**

---

## 🔴 תרגיל 8 — שאילתות משולבות

**א.** חיות **זמינות**, **עם שבב**, ששוקלות **בין 4 ל‑30 ק"ג**.

**ב.** הוצאות **רפואיות** על **חיה ספציפית** (לא כלליות), **מעל 400 ₪**.

**ג.** אימוצים ש**הוחזרו** (יש להם `returned_date`).

**ד.** אימוצים **פעילים** (לא הוחזרו) שבוצעו **ב‑2024**.

**ה.** חיסונים שנתן **ד"ר רון** (`person_id = 4`) ל**כלבים** (`vaccine_type_id` 1 או 2) **ב‑2024**.

**ו.** חיות ששמן מתחיל ב‑`L` **או** ב‑`M`, **ואינן** מאומצות.

---

## 🔴 תרגיל 9 — מצאו את הבאג

לכל שאילתה: **מה היא אמורה לעשות, מה היא עושה בפועל, ומה התיקון.**

</div>

```sql
-- a: "animals without a breed"
SELECT name FROM animal WHERE breed = NULL;

-- b: "cats and dogs over 20 kg"
SELECT name FROM animal WHERE species_id = 1 OR species_id = 2 AND weight_kg > 20;

-- c: "the animal named luna"
SELECT name FROM animal WHERE name = 'luna';

-- d: "expenses in January 2024"
SELECT * FROM expense WHERE expense_date BETWEEN '2024-01-01' AND '2024-01-31';

-- e: "names starting with T"
SELECT name FROM animal WHERE name LIKE 'T';

-- f: "everyone except vets"
SELECT first_name FROM person WHERE role NOT IN ('vet', NULL);

-- g: "the 3 heaviest animals"
SELECT name, weight_kg FROM animal LIMIT 3;
```

<div dir="rtl">

⚠️ **אחת מהן נכונה.** איזו?

---

## 🔴 תרגיל 10 — הדוחות של רותי

לכל בקשה — שאילתה אחת, כתובה לפי כללי הכתיבה (תנאי בכל שורה).

**א.** *"תראי לי את כל החיות שאפשר להציע לאימוץ השבוע: זמינות, עם שבב, ושוקלות לפחות 3 ק"ג."*

**ב.** *"אילו הוצאות רפואיות היו לי ברבעון הראשון של 2025?"*

**ג.** *"מי מהמאמצים גר מחוץ לחיפה?"* (שם מלא + עיר)

**ד.** *"אילו חיות בהסגר או בטיפול רפואי, ואין להן עדיין שבב?"*

**ה.** ⭐ *"אילו חיות נקלטו מהרחוב ב‑2024 והובאו על ידי נועה?"* (`person_id = 2`)

**ו.** ⭐⭐ *"תני לי את כל החיות שאני **לא יכולה** להציע לאימוץ — ולמה."*
(רמז: מה הסטטוסים שמונעים אימוץ? האם יש עוד סיבה?)

---

<div align="center">

**[✅ לפתרונות](solutions.md)** · [חזרה למודול](README.md)

</div>

---

<div align="center">

**🧭 ניווט המודול**

</div>

| 📖 [חזרה למודול](README.md) | ❓ [שאלות ותשובות](questions.md) | ✅ [לפתרונות](solutions.md) | 🏠 [דף הקורס](../../) |
|---|---|---|---|

</div>


<!-- w3schools:start -->
<div dir="rtl">

---

## 🌐 תרגול נוסף ב‑W3Schools

📖 **לקריאה ב‑W3Schools:** [WHERE](https://www.w3schools.com/sql/sql_where.asp) · [AND](https://www.w3schools.com/sql/sql_and.asp) · [OR](https://www.w3schools.com/sql/sql_or.asp) · [NOT](https://www.w3schools.com/sql/sql_not.asp) · [LIKE](https://www.w3schools.com/sql/sql_like.asp) · [תווים כלליים](https://www.w3schools.com/sql/sql_wildcards.asp) · [IN](https://www.w3schools.com/sql/sql_in.asp) · [BETWEEN](https://www.w3schools.com/sql/sql_between.asp) · [NULL](https://www.w3schools.com/sql/sql_null_values.asp)

> 🌐 **פותחים את [עורך ה‑SQL של W3Schools](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all)**, מוחקים את מה שכתוב בו, כותבים שאילתה ולוחצים **Run SQL**. בסיס הנתונים שם הוא של חברה לממכר מזון: `Customers`, `Orders`, `OrderDetails`, `Products`, `Categories`, `Suppliers`, `Shippers` ו‑`Employees`. לחיצה על שם טבלה בצד מציגה את התוכן שלה.
>
> ⚠️ בבסיס הנתונים של W3Schools **אפשר רק לקרוא** (`SELECT`). טקסט כותבים שם בין גרשיים **בודדים**: `'Germany'`.

**W1.** המוצרים שהמחיר שלהם בין 10 ל‑20 (כולל).

**W2.** הלקוחות מגרמניה **או** מצרפת (`IN`).

**W3.** הלקוחות ששמם מתחיל באות A.

**W4.** הלקוחות מברלין **או** מלונדון, שהשם שלהם **לא** מתחיל באות A.


</div>
<!-- w3schools:end -->

<!-- exam-style:start -->
<div dir="rtl">

---

## 🎓 תרגול בסגנון הבחינה

> 🎓 **תרגול בסגנון הבחינה (שאלון 735911).** הסעיפים כאן כתובים בדיוק כמו בבחינה: `Table.Column`, צירוף עם פסיק ומירכאות כפולות. הם רצים על בסיס הנתונים **חוגי ספורט** ([`clubs.sql`](../../exam-prep/db/clubs.sql)). פתרו על הנייר, ואחר כך טענו את הקובץ ל‑OneCompiler ובדקו.

**ב1.** כמה משתתפים תחזיר השאילתה?
```sql
SELECT Members.FirstName FROM Members
WHERE Members.Age BETWEEN 14 AND 16;
```

**ב2.** השלימו כך שיוצגו המשתתפים ששם המשפחה שלהם **מתחיל** באות ח:
```sql
SELECT Members.FirstName, Members.LastName FROM Members
WHERE Members.LastName ________ "________";
```

**ב3.** כתבו שאילתה שמציגה את המאמנים **שאין להם טלפון**.

**ב4.** מה ההבדל בין `WHERE Members.CityCode IN (1, 5)` לבין `WHERE Members.CityCode = 1 OR Members.CityCode = 5`?


</div>
<!-- exam-style:end -->

<!-- classroom:start -->
<div dir="rtl">

---

## 💪 תרגול בכיתה — בית הספר "עתיד"

> 🏫 **בסיס נתונים אחר, 12 שאלות.** הקטע הזה חוזר בסוף התרגילים של **כל** שיעור SQL, תמיד על אותו בסיס נתונים — [`school.sql`](../../resources/school-db/): 7 טבלאות, 18 תלמידים. השאלות הן שמתקדמות בקושי משיעור לשיעור.
>
> **טוענים פעם אחת:** [**פתיחה להעתקה**](https://raw.githubusercontent.com/AhmadKais/sql-course-heb/main/resources/school-db/school.sql) → `Ctrl+A`, `Ctrl+C` → מדביקים ב‑[OneCompiler (SQLite)](https://onecompiler.com/sqlite) → **Run**. צריך להופיע `students_loaded = 18`.
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

**המנהלת רוצה רשימות ממוקדות.** כל שאלה — שאילתה אחת עם `WHERE`. רשמו גם **כמה שורות** חזרו.

**ש1.** כל התלמידים בכיתה `103` — שם פרטי ושם משפחה.

**ש2.** מורים ששכרם **מעל** 13,000 ₪.

**ש3.** כל הציונים **מתחת ל‑60** (הנכשלים): מזהה תלמיד, מזהה מקצוע, ציון.

**ש4.** **תלמידות** (`Gender = 'F'`) שגרות **בחיפה** (`CityCode = 4`).

**ש5.** כל הציונים **בטווח 70–79**, בעזרת `BETWEEN`. ⚠️ האם 70 ו‑79 נכללים?

**ש6.** תלמידים מהערים `1`, `2` ו‑`6` — בעזרת `IN`. כתבו אחר כך את אותה שאילתה עם `OR`, וּודאו שהתוצאה זהה.

**ש7.** תלמידים ששם המשפחה שלהם **מתחיל באות כ**.

**ש8.** מורים שמספר הטלפון שלהם **מתחיל ב‑050**.

**ש9.** תלמידים ש**אין להם טלפון**. ואחר כך: **כמה** תלמידים **כן** יש להם טלפון?

**ש10.** ⚠️ **המלכודת הגדולה.** הריצו את שתי השאילתות:

</div>

```sql
SELECT Grades.StudentId, Grades.Grade FROM Grades WHERE Grades.Grade = NULL;
SELECT Grades.StudentId, Grades.CourseCode FROM Grades WHERE Grades.Grade IS NULL;
```

<div dir="rtl">

כמה שורות החזירה כל אחת? **הסבירו את ההבדל.** איזו מהן תשתמשו בה כדי למצוא מי לא נבחן?

**ש11.** ⚠️ **סדר קדימויות.** המנהלת ביקשה: *"כל ה**בנים** מכיתות 101 **או** 102."* תלמיד כתב:

</div>

```sql
SELECT Students.FirstName, Students.ClassCode, Students.Gender FROM Students
WHERE Students.ClassCode = 101 OR Students.ClassCode = 102 AND Students.Gender = 'M';
```

<div dir="rtl">

הריצו. **מצאו את השורה שלא הייתה צריכה להיות שם**, הסבירו למה היא נכנסה, ותקנו.

**ש12.** שאלות תאריכים:

**א.** מי נרשם לבית הספר **אחרי** `'2026-09-01'`?

**ב.** תלמידים שנולדו **לפני** `'2010-01-01'`. ⚠️ יש 18 תלמידים — ספרו ידנית כמה אמורים לענות על התנאי, והשוו למה שחזר. מי חסר, ולמה?

</div>
<!-- classroom:end -->
