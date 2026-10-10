<div dir="rtl">

# מודול 26 — תרגילים

> 💪 **בסוף הדף — [תרגול בכיתה](#-תרגול-בכיתה--בית-הספר-עתיד):** 12 שאלות על בסיס נתונים אחר, [`school.sql`](../../resources/school-db/), שחוזר בכל שיעור SQL. מיועד לשיעור בכיתה.

> **הנחיות:** הדביקו את [`shelter.sql`](../../resources/shelter-db/shelter.sql) ואחריו `PRAGMA foreign_keys = ON;`. **כתבו ברצף.**
>
> ⚠️ אל תפתחו את [הפתרונות](solutions.md) לפני שניסיתם.
>
> **רמות:** 🟢 בסיסי · 🟡 בינוני · 🔴 מאתגר

---

## 🟢 תרגיל 1 — טיפוסים

לכל עמודה — איזה טיפוס ב‑SQLite, ואיזה ב‑Oracle? נמקו במשפט.

| העמודה | דוגמה |
|--------|--------|
| מספר טלפון | `052-1111111` |
| משקל | `18.5` |
| מספר שבב | `985100001` |
| תאריך חיסון | `2024-05-28` |
| האם מעוקר | כן / לא |
| מחיר אימוץ | `400.00` |
| מין | `M` / `F` / `U` |
| מספר ת"ז | `012345678` |

---

## 🟢 תרגיל 2 — CREATE TABLE

**א.** צרו את טבלת `walk` מסעיף 9 במודול (עם `STRICT`). הכניסו את שני הטיולים מהדוגמה, והריצו את ה‑`SELECT`.

**ב.** הכניסו טיול **בלי** `minutes`. מה הערך שנשמר?

**ג.** ⚠️ נסו `minutes = 'long'`. מה קורה? מה היה קורה **בלי** `STRICT`?

**ד.** נסו טיול עם `person_id = 99`. מה קורה?

---

## 🟡 תרגיל 3 — מ‑ERD לטבלה

רותי רוצה לרשום **טיפולים וטרינריים** (לא רק חיסונים): לכל טיפול — החיה, הווטרינר, התאריך, סוג הטיפול (טקסט חופשי, חובה), המשקל שנמדד (אופציונלי), העלות (חובה, ברירת מחדל 0) והערות (אופציונלי).

**א.** ציירו את הישות במילים: מזהה (#), חובה (\*), אופציונלי (o), ויחסים.

**ב.** כתבו `CREATE TABLE treatment` מלא (עם `STRICT` ו‑`REFERENCES`).

**ג.** הכניסו 3 טיפולים, ושאילתה שמציגה שם חיה, שם משפחה של הווטרינר, תאריך וסוג.

---

## 🟡 תרגיל 4 — ALTER TABLE

**א.** הוסיפו ל‑`animal` עמודה `is_neutered` — מספר שלם, חובה, ברירת מחדל 0. בדקו שלכל החיות יש 0.

**ב.** ⚠️ נסו להוסיף `arrival_note TEXT NOT NULL` — **בלי** ברירת מחדל. מה קרה? למה?

**ג.** עדכנו את `is_neutered = 1` ל‑Rex (הוצאה 7 — "neutering surgery"). השתמשו בתת‑שאילתה שמוצאת את החיה לפי תיאור ההוצאה.

**ד.** ב‑`walk`: שנו את שם העמודה `notes` ל‑`remarks`, ואחר כך מחקו אותה.

---

## 🔴 תרגיל 5 — DROP, TRUNCATE, DELETE

**א.** צרו `dog` מתוך `animal` עם `CREATE TABLE … AS SELECT`. כמה שורות?

**ב.** הריצו `SELECT sql FROM sqlite_master WHERE name = 'dog';` והשוו להגדרה של `animal`. **מה חסר?**

**ג.** מחקו את כל השורות מ‑`dog` (הטבלה נשארת). אחר כך מחקו את הטבלה עצמה. איך הייתם עושים את הראשון ב‑Oracle בצורה המהירה ביותר — ומה המחיר?

**ד.** ⭐ הציגו את כל הטבלאות בבסיס הנתונים, ואת העמודות של `walk`.

---

## 🔴 תרגיל 6 — הפרויקט שלכם ⭐

קחו את ה‑ERD של **הפרויקט שלכם** (מודול 9 / מודול 12).

**א.** כתבו `CREATE TABLE` לכל ישות — בסדר הנכון (קודם טבלאות ש**אחרים מצביעים עליהן**).

**ב.** כתבו בראש הסקריפט `DROP TABLE IF EXISTS` לכל טבלה — בסדר **הפוך**.

**ג.** הכניסו לפחות 5 שורות לכל טבלה, והריצו 3 שאילתות `JOIN` שמוכיחות שהיחסים עובדים.

**ד.** שמרו את הסקריפט בקובץ `my_project.sql` — הוא ילווה אתכם עד המצגת הסופית (מודול 15).

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[✅ לפתרונות](solutions.md)**

</div>

</div>


<!-- w3schools:start -->
<div dir="rtl">

---

## 🌐 תרגול נוסף ב‑W3Schools

📖 **לקריאה ב‑W3Schools:** [CREATE TABLE](https://www.w3schools.com/sql/sql_create_table.asp) · [ALTER TABLE](https://www.w3schools.com/sql/sql_alter.asp) · [DROP TABLE](https://www.w3schools.com/sql/sql_drop_table.asp)

> 💻 הפקודות של השיעור הזה **משנות** נתונים או מבנה, ו‑W3Schools לא מאפשר את זה. קראו שם את ההסבר, ואת התרגול עצמו עשו ב‑OneCompiler, על בסיס הנתונים של המקלט ([הוראות](../../resources/setup.md)).

</div>
<!-- w3schools:end -->

<!-- exam-style:start -->
<div dir="rtl">

---

## 🎓 תרגול בסגנון הבחינה

> 🎓 **תרגול בסגנון הבחינה (שאלון 735911).** הסעיפים כאן כתובים בדיוק כמו בבחינה: `Table.Column`, צירוף עם פסיק ומירכאות כפולות. הם רצים על בסיס הנתונים **חוגי ספורט** ([`clubs.sql`](../../exam-prep/db/clubs.sql)). פתרו על הנייר, ואחר כך טענו את הקובץ ל‑OneCompiler ובדקו.

**ב1.** איזו פקודה מוסיפה לטבלה Members שדה בשם Email?
1. `INSERT INTO Members ADD Email Text`  2. `UPDATE Members ADD Email Text`  3. `ALTER TABLE Members ADD Email Text`  4. `ALTER TABLE Members INSERT Email Text`

**ב2.** השלימו את הטבלה:

| הפקודה | מה נמחק? | הטבלה נשארת? |
|---|---|---|
| `DELETE FROM Clubs WHERE Price > 200` | | |
| `DELETE FROM Clubs` | | |
| `DROP TABLE Clubs` | | |

**ב3.** כתבו `CREATE TABLE` לטבלה Halls (אולמות): קוד אולם (מספר, מפתח ראשי), שם אולם (טקסט, חובה), וקיבולת (מספר).


</div>
<!-- exam-style:end -->

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

**עד כה שלפתם ושינתם נתונים. עכשיו אתם בונים את המבנה עצמו.**

**ש1.** בית הספר פותח חוגים. בנו טבלה `Clubs` עם:

| העמודה | הטיפוס | הדרישה |
|---------|---------|---------|
| `ClubId` | שלם | מפתח ראשי |
| `ClubName` | טקסט | חובה, **ייחודי** |
| `TeacherCode` | שלם | מפתח זר ל‑`Teachers` |
| `MeetingDay` | טקסט | אופציונלי |
| `MaxStudents` | שלם | חובה, ברירת מחדל `20` |
| `Fee` | ממשי | חובה, ברירת מחדל `0` |

**ש2.** הכניסו שלושה חוגים ושלפו את הטבלה:
`(1, 'רובוטיקה', 3, 'שלישי')` · `(2, 'דיבייט', 4, 'חמישי', 15, 50.5)` · `(3, 'שחמט')` — השלישי **רק עם שתי העמודות הראשונות**. מה יש אצלו ב‑`MaxStudents` וב‑`Fee`, ומה ב‑`MeetingDay`? **למה זה שונה?**

**ש3.** הוסיפו לטבלה עמודה `RoomNumber` (שלם). מה קיבלו שלוש השורות הקיימות?

**ש4.** שנו את שם העמודה `Fee` ל‑`MonthlyFee`.

**ש5.** שנו את שם הטבלה כולה ל‑`SchoolClubs`.

**ש6.** בנו טבלת קשר `ClubMembers (ClubId, StudentId, JoinDate)` עם **מפתח ראשי מורכב** משני השדות הראשונים ו**שני מפתחות זרים**. הכניסו: `(1, 1007)`, `(1, 1013)`, `(2, 1016)` — כולם ב‑`'2026-09-15'`/`'2026-09-16'`.

**ש7.** **`CREATE TABLE … AS SELECT`.** בנו בשורה אחת טבלה `TopStudents` שמכילה את כל התלמידים שהממוצע שלהם **90 ומעלה**, עם מזהה, שם מלא וממוצע. ⚠️ מי קבע את הטיפוסים של העמודות?

**ש8.** ⚠️ **ההפתעה הגדולה של SQLite.** הריצו:

</div>

```sql
INSERT INTO SchoolClubs (ClubId, ClubName, MaxStudents) VALUES (4, 'תיאטרון', 'עשרים');
SELECT ClubId, ClubName, MaxStudents, TYPEOF(MaxStudents) AS WhatType FROM SchoolClubs;
```

<div dir="rtl">

`MaxStudents` הוגדר `INTEGER`. **האם ה‑`INSERT` נכשל?** מה אומרת `TYPEOF`? ומה ההשלכה על `SUM(MaxStudents)`?

**ש9.** אילו טבלאות קיימות כרגע בבסיס הנתונים? (`SELECT name, type FROM sqlite_master WHERE type = 'table';`)

**ש10.** מחקו את הטבלה `TopStudents` לגמרי, וּודאו ב‑`sqlite_master` שהיא נעלמה.

**ש11.** הריצו `DELETE FROM ClubMembers;` ואז חפשו את `ClubMembers` ב‑`sqlite_master`. **מה ההבדל בין `DELETE` לבין `DROP`?**

**ש12.** ⚠️ **מה `ALTER TABLE` לא מרשה.** הריצו את ארבע הפקודות, ורשמו לכל אחת אם עברה או נכשלה ומה ההודעה:

</div>

```sql
ALTER TABLE Students ADD COLUMN Email TEXT NOT NULL;
ALTER TABLE Students ADD COLUMN Email TEXT NOT NULL DEFAULT 'unknown@school.il';
ALTER TABLE Students DROP COLUMN Email;
ALTER TABLE Students DROP COLUMN StudentId;
```

<div dir="rtl">

**הסבירו את הראשונה והרביעית** — מה הייתה הבעיה בכל אחת?

</div>
<!-- classroom:end -->
