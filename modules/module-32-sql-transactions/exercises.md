<div dir="rtl">

# מודול 32 — תרגילים

> 💪 **בסוף הדף — [תרגול בכיתה](#-תרגול-בכיתה--בית-הספר-עתיד):** 12 שאלות על בסיס נתונים אחר, [`school.sql`](../../resources/school-db/), שחוזר בכל שיעור SQL. מיועד לשיעור בכיתה.

> **הנחיות:** הדביקו את [`shelter.sql`](../../resources/shelter-db/shelter.sql) ואחריו `PRAGMA foreign_keys = ON;`. **כתבו ברצף.**
>
> ⚠️ אל תפתחו את [הפתרונות](solutions.md) לפני שניסיתם.
>
> **רמות:** 🟢 בסיסי · 🟡 בינוני · 🔴 מאתגר

---

## 🟢 תרגיל 1 — COMMIT ו‑ROLLBACK

**א.** בתוך טרנזקציה: מחקו את כל ההוצאות, ספרו אותן, ובטלו. כמה הוצאות יש אחרי?

**ב.** רשמו את האימוץ של Rocky (סעיף 2 במודול) כטרנזקציה אחת. בדקו את הסטטוס ואת מספר האימוצים אחרי.

**ג.** ⚠️ פתחו טרנזקציה, עדכנו את Rex ל‑`adopted`, ונסו לרשום אימוץ על ידי אדם 99. **בדקו את הסטטוס של Rex לפני `ROLLBACK`.** מה גיליתם?

---

## 🟢 תרגיל 2 — חיה חדשה וקליטה, ביחד

כתבו טרנזקציה שקולטת חתול חדש בשם Milo: שורה ב‑`animal` **ו**שורה ב‑`intake` שמצביעה עליו (נמצא ב‑`'Yarka center'` על ידי נועה, `person_id = 2`). השתמשו ב‑`last_insert_rowid()` כדי לקשר.

---

## 🟡 תרגיל 3 — החזרת חיה

Shira Katz מחזירה את Tom (אימוץ 4) כי היא עוברת דירה. **פעולה עסקית אחת, שלושה שינויים:**
1. ב‑`adoption` — תאריך החזרה
2. ב‑`animal` — הסטטוס חוזר ל‑`available`
3. ב‑`intake` — קליטה חדשה מסוג `surrender` עם סיבה

**א.** כתבו את שלושתם כטרנזקציה אחת.

**ב.** למה זה **חייב** להיות טרנזקציה? מה יקרה אם רק 1 ו‑2 יתבצעו?

**ג.** ⭐ איזה מודול בקורס הבטיח שהחזרה נרשמת כ**קליטה חדשה** ולא כ"ביטול" של האימוץ? למה זה חשוב?

---

## 🟡 תרגיל 4 — SAVEPOINT

**א.** בטרנזקציה אחת: העלו את כל תעריפי האימוץ ב‑10%, צרו savepoint, ואז "בטעות" שנו את כל החיות המאומצות ל‑`available`. בטלו רק את הטעות, ואשרו את העלאת המחיר.

**ב.** הציגו את התעריפים ואת מספר החיות הזמינות — ודאו שרק השינוי הראשון נשמר.

---

## 🔴 תרגיל 5 — מקביליות

**א.** כתבו `UPDATE` שמאמץ את Rex **רק אם הוא עדיין זמין**. הריצו אותו פעמיים בתוך אותה טרנזקציה, ובדקו `changes()` אחרי כל פעם. מה זה מדמה?

**ב.** ⭐ הסבירו במילים: למה "קודם `SELECT` לבדוק שזמין, אחר כך `UPDATE`" לא בטוח כששני מתנדבים עובדים בו‑זמנית — ולמה ה‑`UPDATE` מסעיף א' כן?

---

## 🔴 תרגיל 6 — DDL בתוך טרנזקציה

**א.** ב‑SQLite: `BEGIN;` ⟵ `CREATE TABLE notes (txt TEXT);` ⟵ `DELETE FROM expense WHERE category = 'food';` ⟵ `ROLLBACK;`. האם `notes` קיימת? כמה הוצאות מזון יש?

**ב.** ⭐ מה היה קורה **ב‑Oracle** עם אותה סדרה? למה?

---

## 🔴 תרגיל 7 — הכנה להסמכה

ענו בלי להריץ, ואז בדקו:

**א.** ב‑Oracle: `UPDATE …; SAVEPOINT a; DELETE …; SAVEPOINT b; INSERT …; ROLLBACK TO a; COMMIT;` — אילו מהשינויים נשמרו?

**ב.** מה ההבדל בין `ROLLBACK` לבין `ROLLBACK TO SAVEPOINT x`? מה קורה לטרנזקציה אחרי כל אחד?

**ג.** משתמש A עשה `UPDATE` בלי `COMMIT`. משתמש B עושה `SELECT` על אותה שורה. מה B רואה — ב‑Oracle?

**ד.** מה ארבע האותיות של ACID, ומה כל אחת מבטיחה? תנו דוגמה מהמקלט לכל אחת.

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

> 💡 **איך לעבוד בקטע הזה:** ב‑OneCompiler כל ה‑Run הוא **חיבור אחד**, ולכן `BEGIN` ו‑`ROLLBACK` באותה הדבקה עובדים כמו שצריך. הדביקו את `school.sql`, ומתחתיו את כל השאילתה — `BEGIN`, הפעולות, ה‑`SELECT`‑ים וה‑`ROLLBACK` — **יחד**.

**ש1.** ⭐ **הרשת הביטחון.** הריצו:

</div>

```sql
BEGIN TRANSACTION;
UPDATE Grades SET Grade = 100 WHERE StudentId = 1012;
SELECT StudentId, CourseCode, Grade FROM Grades WHERE StudentId = 1012;   -- בתוך הטרנזקציה
ROLLBACK;
SELECT StudentId, CourseCode, Grade FROM Grades WHERE StudentId = 1012;   -- אחרי
```

<div dir="rtl">

מה הראה כל אחד משני ה‑`SELECT`‑ים? **מה בדיוק עשה ה‑`ROLLBACK`?**

**ש2.** עכשיו אותו דבר עם `COMMIT` במקום `ROLLBACK`: עדכנו את הטלפון של נור (`1002`) ל‑`'050-0000000'`, עשו `COMMIT`, שלפו — ואז נסו `ROLLBACK`. **מה ההודעה, ומה היא אומרת?**

**ש3.** ⚠️ **Autocommit.** הריצו `UPDATE` **בלי** `BEGIN` לפניו, ומיד אחריו `ROLLBACK`:

</div>

```sql
UPDATE Students SET Phone = 'XXX' WHERE StudentId = 1001;
ROLLBACK;
SELECT StudentId, Phone FROM Students WHERE StudentId = 1001;
```

<div dir="rtl">

מה קרה? **הסבירו מה זה `autocommit`** ומה המסקנה המעשית.

**ש4.** **`SAVEPOINT`.** הריצו:

</div>

```sql
BEGIN TRANSACTION;
UPDATE Teachers SET Salary = 20000 WHERE TeacherCode = 1;
SAVEPOINT raise1;
UPDATE Teachers SET Salary = 30000 WHERE TeacherCode = 2;
SELECT TeacherCode, LastName, Salary FROM Teachers WHERE TeacherCode IN (1,2);
ROLLBACK TO raise1;
SELECT TeacherCode, LastName, Salary FROM Teachers WHERE TeacherCode IN (1,2);
COMMIT;
```

<div dir="rtl">

**איזה מהשניים חזר לאחור, ואיזה נשאר?** למה זה שימושי?

**ש5.** ⚠️⚠️ **השאלה החשובה בשיעור.** הפעולה "העברת תלמיד לכיתה אחרת" היא **שלוש פעולות**. הריצו:

</div>

```sql
PRAGMA foreign_keys = ON;
BEGIN TRANSACTION;
UPDATE Students SET ClassCode = 103 WHERE StudentId = 1012;                   -- 1
INSERT INTO Absences VALUES (17, 1012, '2026-09-21', 1, 'מעבר כיתה');          -- 2
UPDATE Grades SET Term = 1 WHERE StudentId = 1012 AND Term = 2;               -- 3

SELECT 'inside tx' AS Stage,
       (SELECT ClassCode FROM Students WHERE StudentId=1012) AS Class1,
       (SELECT COUNT(*) FROM Absences) AS Abs1;
```

<div dir="rtl">

**א.** **הפעולה השלישית נכשלה.** העתיקו את ההודעה והסבירו למה (רמז: המפתח הראשי של `Grades`).

**ב.** ה‑`SELECT` שאחריה **כן רץ**. מה הוא מראה? כלומר — **האם השגיאה ביטלה את הטרנזקציה?**

**ג.** עכשיו הריצו את כל הבלוק **פעמיים**: פעם שמסתיימת ב‑`ROLLBACK;` ופעם ב‑`COMMIT;`, ושלפו בכל פעם את `ClassCode` של 1012 ואת `COUNT(*)` של `Absences`. **מה קיבלתם בכל אחת, ואיזו מהן היא "העברת תלמיד שלא הושלמה"?**

**ש6.** הריצו `DELETE FROM Absences;` (בלי `WHERE`!) **בתוך** טרנזקציה, בדקו `COUNT(*)`, ואז `ROLLBACK` ובדקו שוב. **קשרו את זה לש12 של שיעור 25.**

**ש7.** ⚠️ **DDL בתוך טרנזקציה.** הריצו:

</div>

```sql
BEGIN TRANSACTION;
CREATE TABLE Temp1 (Id INTEGER);
INSERT INTO Temp1 VALUES (1);
ROLLBACK;
SELECT name FROM sqlite_master WHERE name = 'Temp1';
```

<div dir="rtl">

האם `Temp1` שרדה? ⚠️ **באורקל התשובה הפוכה — למה?**

**ש8.** `SAVEPOINT` מקוננים. הריצו `SAVEPOINT step1` → `UPDATE` לשכר 11000 של מורה 5 → `SAVEPOINT step2` → `UPDATE` ל‑99999 → `ROLLBACK TO step2` → `RELEASE step1` → `COMMIT`. **מה השכר בסוף, ומה עשה `RELEASE`?**

**ש9.** כתבו **בעצמכם** טרנזקציה שמוחקת לגמרי את התלמיד `1015` (איתי גולן) — עם כל הציונים וההיעדרויות שלו — **בסדר הנכון**. בדקו שהכול נעלם, ואז `ROLLBACK`. ⚠️ **למה הסדר חשוב?**

**ש10.** **ACID.** לכל אחת מארבע האותיות, תנו דוגמה **מבית הספר "עתיד"**:

| האות | מה זה | הדוגמה שלכם |
|------|--------|--------------|
| **A** — Atomicity | | |
| **C** — Consistency | | |
| **I** — Isolation | | |
| **D** — Durability | | |

**ש11.** ⭐ **עדכון אבוד.** שני מורים פותחים את הציון של ראניה במתמטיקה (98) **באותו רגע**. חוסאם מתקן ל‑99, אורלי מתקנת ל‑100. שניהם לוחצים "שמור".

**א.** מה יהיה הציון?
**ב.** האם מישהו קיבל הודעת שגיאה?
**ג.** איזה תיקון **אבד**, ואיך מונעים את זה?

**ש12.** המזכירה רוצה למחוק 200 תלמידים שסיימו. **כתבו את רצף הפקודות המלא** שהייתם ממליצים לה — כולל מה לבדוק, מתי, ומה לעשות אם משהו נראה לא נכון.

</div>
<!-- classroom:end -->
