<div dir="rtl">

# מודול 29 — תרגילים

> 💪 **בסוף הדף — [תרגול בכיתה](#-תרגול-בכיתה--בית-הספר-עתיד):** 12 שאלות על בסיס נתונים אחר, [`school.sql`](../../resources/school-db/), שחוזר בכל שיעור SQL. מיועד לשיעור בכיתה.

> **הנחיות:** הדביקו את [`shelter.sql`](../../resources/shelter-db/shelter.sql) ו**כתבו ברצף**.
>
> ⚠️ אל תפתחו את [הפתרונות](solutions.md) לפני שניסיתם.
>
> **רמות:** 🟢 בסיסי · 🟡 בינוני · 🔴 מאתגר

---

## 🟢 תרגיל 1 — מזהים אוטומטיים

**א.** צרו `d2 (id INTEGER PRIMARY KEY, donor TEXT)`. הכניסו A, B, C (בלי `id`), מחקו את C, והכניסו D. איזה `id` קיבל D?

**ב.** עשו אותו דבר עם `donation` עם `AUTOINCREMENT` (סעיף 2.2). איזה `id` קיבל D עכשיו? הציגו את `sqlite_sequence`.

**ג.** הכניסו חיה חדשה (Milo, חתול, quarantine), ומיד אחריה `SELECT last_insert_rowid();`. מה קיבלתם? איך זה עוזר לרשום את הקליטה שלה?

**ד.** ⭐ למה `SELECT MAX(animal_id) + 1` לא בטוח במערכת עם כמה משתמשים? תארו תרחיש.

---

## 🟢 תרגיל 2 — Sequence ב‑Oracle (על הנייר)

**א.** כתבו `CREATE SEQUENCE` לתרומות, שמתחיל מ‑1000 ועולה ב‑1.

**ב.** כתבו `INSERT` של תרומה חדשה שמשתמש ב‑sequence, ומיד אחריו `INSERT` של קבלה (`receipt`) שמצביעה על **אותה** תרומה.

**ג.** כתבו את טבלת התרומות מחדש עם `IDENTITY` במקום sequence.

---

## 🟡 תרגיל 3 — אינדקסים

**א.** הריצו `EXPLAIN QUERY PLAN SELECT * FROM animal WHERE name = 'Luna';`. אחר כך צרו אינדקס על `name`, והריצו שוב. מה השתנה?

**ב.** הציגו את כל האינדקסים בבסיס הנתונים. מאיפה הגיעו אלה שלא יצרתם?

**ג.** בדקו את התוכנית של `SELECT * FROM vaccination WHERE animal_id = 3;`. צרו את האינדקס שחסר ובדקו שוב.

**ד.** בדקו את התוכנית של JOIN בין `animal` ל‑`vaccination` לפי שם החיה — **לפני ואחרי** שני האינדקסים. מה ההבדל?

---

## 🟡 תרגיל 4 — מתי אינדקס לא עוזר

**א.** עם האינדקס על `name`: בדקו את התוכנית של `WHERE UPPER(name) = 'LUNA'`. למה `SCAN`? תקנו עם אינדקס על ביטוי.

**ב.** בדקו `WHERE name LIKE '%na'`. למה אין אינדקס שיכול לעזור כאן?

**ג.** בדקו `WHERE STRFTIME('%Y', expense_date) = '2024'`. צרו אינדקס על `expense_date`. האם עכשיו הוא משמש? **כתבו את התנאי מחדש כך שישתמש בו.**

**ד.** ⭐ אילו מהעמודות האלה הייתם מאנדקסים במקלט עם מיליון חיות? `animal.status`, `animal.sex`, `animal.chip_number`, `vaccination.animal_id`, `expense.expense_date`, `animal.name`. נמקו.

---

## 🔴 תרגיל 5 — ראיון בכיתה

עבדו בזוגות. כתבו על נייר — ורק אחר כך הריצו:

**א.** החיה הכבדה ביותר **מכל מין**.

**ב.** המשקל **השני** בגובהו — בשתי דרכים (תת‑שאילתה, ו‑`LIMIT … OFFSET`).

**ג.** חיות שקיבלו יותר משני חיסונים.

**ד.** מצאו את **שלוש** הטעויות בשאילתה מסעיף 9.3 במודול, ותקנו אותה.

**ה.** ⭐ הסבירו בקול, בשתי דקות, לבן הזוג: "מה זה אינדקס, ולמה לא שמים אחד על כל עמודה?"

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[✅ לפתרונות](solutions.md)**

</div>

</div>

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

**אובייקטים שאינם טבלאות: אינדקסים, מחולל מזהים, ושם נוסף לאותו דבר.**

**ש1.** ⭐ **לראות את מנוע השאילתות עובד.** הריצו **לפני** שבניתם אינדקס:

</div>

```sql
EXPLAIN QUERY PLAN SELECT * FROM Students WHERE Students.LastName = 'כהן';
```

<div dir="rtl">

רשמו את העמודה `detail`. עכשיו בנו אינדקס: `CREATE INDEX idx_students_lastname ON Students(LastName);` והריצו **את אותה שורה** שוב. **מה השתנה בטקסט?**

**ש2.** הריצו את השאילתה עצמה (`WHERE LastName = 'כהן'`). **האם התוצאה שונה?** מה כן השתנה?

**ש3.** **אינדקס ייחודי.** הריצו `CREATE UNIQUE INDEX idx_teachers_phone ON Teachers(Phone);` — הוא עובר, אף שלשני מורים אין טלפון (`NULL`). **למה?** ואז נסו להוסיף מורה עם טלפון **קיים**:

</div>

```sql
INSERT INTO Teachers VALUES (8, 'דנה', 'אלון', 'אמנות', '2026-09-01', 9500, 4, '050-7010101');
```

<div dir="rtl">

**ש4.** ⚠️ **אינדקס מורכב — כלל העמודה המובילה.** בנו `CREATE INDEX idx_grades_course_term ON Grades(CourseCode, Term);` והריצו `EXPLAIN QUERY PLAN` על שתי השאילתות:

</div>

```sql
SELECT * FROM Grades WHERE Grades.CourseCode = 11 AND Grades.Term = 2;
SELECT * FROM Grades WHERE Grades.Term = 2;
```

<div dir="rtl">

**רק אחת מהן משתמשת באינדקס. איזו, ולמה?**

**ש5.** אילו אינדקסים קיימים? (`sqlite_master`, `type = 'index'`, ובלי `name LIKE 'sqlite_%'`.)

**ש6.** מחקו את `idx_students_lastname` ב‑`DROP INDEX` וּודאו. **האם נמחק נתון?**

**ש7.** **מחולל מזהים.** בנו טבלה `Notices (NoticeId INTEGER PRIMARY KEY AUTOINCREMENT, Title TEXT NOT NULL, Posted TEXT NOT NULL DEFAULT '2026-09-21')`. הכניסו שלוש הודעות — **בלי לציין `NoticeId` אף פעם** — ושלפו.

**ש8.** הריצו `SELECT name, seq FROM sqlite_sequence;`. **מה הטבלה הזאת, ומי יצר אותה?**

**ש9.** ⚠️ **החור ברצף.** מחקו את הודעה 3, הכניסו הודעה חדשה, ושלפו שוב — גם את `sqlite_sequence`. **איזה מזהה קיבלה ההודעה החדשה?** האם זה באג?

**ש10.** הריצו `SELECT Students.rowid, Students.StudentId, Students.FirstName FROM Students LIMIT 3;`. **מה הקשר בין שתי העמודות הראשונות?**

**ש11.** **סינונים (Synonym).** ב‑SQLite אין `CREATE SYNONYM`. בנו `Pupils` כשם נוסף ל‑`Students` בכלים שיש לכם, וּודאו ש‑`SELECT COUNT(*) FROM Pupils;` מחזיר 18. **איזה כלי השתמשתם, ומה ההבדל מסינונים אמיתי?**

**ש12.** ⚠️ **אינדקס שלא כדאי.** בנו `CREATE INDEX idx_students_gender ON Students(Gender);` והריצו `EXPLAIN QUERY PLAN` על `WHERE Gender = 'F'`.

**האינדקס כן נבחר.** ובכל זאת — **למה זה בדרך כלל אינדקס מיותר?** חשבו על (א) כמה שורות מתוך 18 הוא מסנן, ו‑(ב) מה קורה בכל `INSERT`.

</div>
<!-- classroom:end -->
