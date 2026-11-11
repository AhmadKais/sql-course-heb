<div dir="rtl">

# מודול 23 — תרגילים

> 💪 **בסוף הדף — [תרגול בכיתה](#-תרגול-בכיתה--בית-הספר-עתיד):** 12 שאלות על בסיס נתונים אחר, [`school.sql`](../../resources/school-db/), שחוזר בכל שיעור SQL. מיועד לשיעור בכיתה.

> **הנחיות:** כל התרגילים על [בסיס הנתונים המוכן](../../resources/shelter-db/). **הריצו.**
>
> ⚠️ אל תפתחו את [הפתרונות](solutions.md) לפני שניסיתם.
>
> **רמות:** 🟢 בסיסי · 🟡 בינוני · 🔴 מאתגר

---

## 🟢 תרגיל 1 — חמש הפונקציות

**א.** כמה מתנדבים יש? (`role = 'volunteer'`)

**ב.** מתי הצטרף המתנדב הוותיק ביותר, ומתי החדש ביותר?

**ג.** החיסונים: עלות כוללת, עלות ממוצעת (2 ספרות), ומספר החיסונים.

**ד.** ההוצאה הגדולה ביותר על מזון. ההוצאה הרפואית **הראשונה** (התאריך).

**ה.** הכלבים: כמה יש, ומה המשקל הממוצע (2 ספרות)?

---

## 🟢 תרגיל 2 — שלושה סוגי COUNT

**א.** בשאילתה אחת: כמה אנשים, לכמה יש טלפון, ובכמה ערים שונות הם גרים.

**ב.** בטבלת `intake`: כמה קליטות **בלי** `brought_by`? כמה **עם**? וכמה **אנשים שונים** הביאו חיות?

**ג.** כמה חיסונים ניתנו ב‑2024? **ולכמה חיות** שונות?

**ד.** ⚠️ הריצו `SELECT COUNT(*), COUNT(breed) FROM animal;`. למה המספרים שונים? איזה מהם עונה על "כמה חיות יש"?

---

## 🟡 תרגיל 3 — NULL וקבוצה ריקה

**א.** מה הגיל הממוצע של החיות? חשבו פעם עם `AVG`, ופעם עם `SUM(…) / COUNT(*)`. מה ההבדל ולמה?

**ב.** הריצו `SELECT SUM(amount), COUNT(*) FROM expense WHERE category = 'toys';`. מה יצא? תקנו כך שהסכום יהיה 0.

**ג.** ⭐ כתבו שאילתה שבה `MAX` מחזיר NULL. מתי זה קורה?

---

## 🟡 תרגיל 4 — עם WHERE ועם JOIN

**א.** כמה המקלט הוציא ב‑2024?

**ב.** כמה עלה Max למקלט (סך ההוצאות עליו)? חפשו לפי שם.

**ג.** החתולים: כמה, ממוצע משקל, הקל והכבד.

**ד.** כמה שילם בסך הכול כל אחד מהמאמצים מחיפה **ביחד**? (סכום אחד.)

---

## 🟡 תרגיל 5 — ספירה מותנית

**א.** בשורה אחת: כמה זכרים, כמה נקבות, וכמה לא ידוע.

**ב.** הכנסות מאימוץ לפי שנה — **בשורה אחת** עם שלוש עמודות: 2023, 2024, 2025.

**ג.** הוצאות רפואיות, מזון וחשמל (`utilities`) — שלוש עמודות בשורה אחת.

**ד.** איזה אחוז מהחיות אומצו? (עיגול לספרה אחת.)

**ה.** בטבלת `intake`, בשורה אחת: כמה `stray`, כמה `surrender`, כמה `transfer`.

---

## 🔴 תרגיל 6 — המלכודות

**א.** הריצו `SELECT name, MIN(birth_date) FROM animal;`. מה SQLite מחזיר? מה Oracle היה עושה? כתבו גרסה נכונה שמחזירה את שם החיה המבוגרת ביותר.

**ב.** כמה חיות שוקלות **יותר מהממוצע**?

**ג.** ⚠️ הריצו:

</div>

```sql
SELECT COUNT(*), SUM(e.amount)
FROM   animal a
JOIN   expense     e ON e.animal_id = a.animal_id
JOIN   vaccination v ON v.animal_id = a.animal_id
WHERE  a.name = 'Rocky';
```

<div dir="rtl">

למי שהתכוון לשאול "כמה הוצאנו על Rocky" — מה לא בסדר? מה התשובה הנכונה? למה יצא 2400?

**ד.** ⭐ **דוח ההנהלה:** בשורה אחת — כמה חיות ממתינות, כמה אימוצים היו, ההכנסה מאימוצים, סך ההוצאות, והמאזן. (רמז: סעיף 8 במודול.)

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[✅ לפתרונות](solutions.md)**

</div>

</div>

<!-- w3schools:start -->
<div dir="rtl">

---

## 🌐 תרגול נוסף ב‑W3Schools

📖 **לקריאה ב‑W3Schools:** [MIN / MAX](https://www.w3schools.com/sql/sql_min_max.asp) · [COUNT](https://www.w3schools.com/sql/sql_count.asp) · [SUM](https://www.w3schools.com/sql/sql_sum.asp) · [AVG](https://www.w3schools.com/sql/sql_avg.asp)

> 🌐 **פותחים את [עורך ה‑SQL של W3Schools](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all)**, מוחקים את מה שכתוב בו, כותבים שאילתה ולוחצים **Run SQL**. בסיס הנתונים שם הוא של חברה לממכר מזון: `Customers`, `Orders`, `OrderDetails`, `Products`, `Categories`, `Suppliers`, `Shippers` ו‑`Employees`. לחיצה על שם טבלה בצד מציגה את התוכן שלה.
>
> ⚠️ בבסיס הנתונים של W3Schools **אפשר רק לקרוא** (`SELECT`). טקסט כותבים שם בין גרשיים **בודדים**: `'Germany'`.

**W1.** המחיר הממוצע, הגבוה והנמוך של המוצרים.

**W2.** כמה מוצרים יש בקטגוריה 1?


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

**מכאן התשובות הן מספר אחד, לא רשימה.** חמש פונקציות: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`.

**ש1.** כמה תלמידים יש בבית הספר?

**ש2.** בטבלת הציונים: כמה **שורות** יש, כמה מהן **עם ציון**, וכמה **חסרים**? (שלוש עמודות, שאילתה אחת.)

**ש3.** **הממוצע הבית‑ספרי** מעוגל לשתי ספרות — פעמיים: פעם על הציונים כמו שהם, ופעם כש‑`NULL` הוחלף ב‑`0`. **מה ההפרש, ואיזה מהשניים נכון?**

**ש4.** הציון **הנמוך** והציון **הגבוה** בבית הספר.

**ש5.** על טבלת המורים בשאילתה אחת: **סך השכר** החודשי, **הממוצע**, **המינימום** וה**מקסימום**.

**ש6.** כמה מורים יש, וכמה **מקצועות שונים** הם מלמדים? (`COUNT(DISTINCT …)`.)

**ש7.** כמה שורות יש ב‑`Grades`, ול**כמה תלמידים שונים** יש בה ציון? ⚠️ יש 18 תלמידים — מה זה אומר על אחד מהם?

**ש8.** על טבלת ההיעדרויות: **התאריך הראשון**, **התאריך האחרון**, ו**סך ההיעדרויות**. ⚠️ `MIN`/`MAX` על תאריכים — למה זה בכלל עובד?

**ש9.** מה הממוצע ב**מתמטיקה 5 יח"ל** (`CourseCode = 11`), ועל כמה ציונים הוא מבוסס?

**ש10.** ⚠️ **איך `AVG` באמת עובד.** בשאילתה אחת הציגו: `SUM(Grade)`, `COUNT(*)`, `COUNT(Grade)`, `SUM(Grade) / COUNT(*)`, ו‑`AVG(Grade)`.

**שתי התוצאות האחרונות שונות. מצאו במה `AVG` מחלק** — ואז הסבירו במשפט אחד מה `AVG` עושה עם `NULL`.

**ש11.** בשאילתה אחת על `Students`: `COUNT(*)`, `COUNT(Phone)`, `COUNT(BirthDate)`, `COUNT(ClassCode)`. **ארבעה מספרים שונים מאותה טבלה** — הסבירו כל אחד.

**ש12.** ⚠️ **המלכודת שאורקל לא מרשה.** הריצו:

</div>

```sql
SELECT Students.FirstName, MAX(Grades.Grade) AS Best
FROM   Students, Grades WHERE Students.StudentId = Grades.StudentId;
```

<div dir="rtl">

**א.** כמה שורות חזרו? איזה שם מופיע?

**ב.** עכשיו בדקו: **כמה תלמידים בכלל קיבלו 100?** (שאילתה נפרדת.) מה זה אומר על התשובה בסעיף א'?

**ג.** באורקל השאילתה הזאת **לא רצה בכלל** ומחזירה `ORA-00937`. **למה זה עדיף** על מה שקרה כאן?

</div>
<!-- classroom:end -->
