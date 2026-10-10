<div dir="rtl">

# מודול 25 — תרגילים

> 💪 **בסוף הדף — [תרגול בכיתה](#-תרגול-בכיתה--בית-הספר-עתיד):** 12 שאלות על בסיס נתונים אחר, [`school.sql`](../../resources/school-db/), שחוזר בכל שיעור SQL. מיועד לשיעור בכיתה.

> **הנחיות:** הדביקו את [`shelter.sql`](../../resources/shelter-db/shelter.sql), ומיד אחריו:
>
> ```sql
> PRAGMA foreign_keys = ON;
> ```
>
> **כתבו את כל התרגילים ברצף, אחד אחרי השני** — חלק מהם משתמשים בשורות שהוספתם בתרגיל קודם. אם משהו השתבש — הדביקו את הקובץ מחדש והתחילו שוב. זה בדיוק היתרון של סביבת תרגול.
>
> 📋 **אחרי כל `UPDATE` / `DELETE`:** `SELECT changes();` — ובדקו שהמספר הוא מה שציפיתם.
>
> ⚠️ אל תפתחו את [הפתרונות](solutions.md) לפני שניסיתם.
>
> **רמות:** 🟢 בסיסי · 🟡 בינוני · 🔴 מאתגר

---

## 🟢 תרגיל 1 — INSERT

**א.** מתנדבת חדשה: נור חדאד (Nour Haddad), מירכא (Yarka), טלפון `052-3434343`, הצטרפה ב‑`2026-09-01`. **בלי** לתת `person_id`. איזה מזהה היא קיבלה?

**ב.** שתי חיות חדשות **בפקודה אחת**: כלב בשם Lucky (זכר) וחתולה בשם Snow (נקבה), שתיהן בסטטוס `quarantine`. שאר העמודות — לא ידועות.

**ג.** Lucky נמצא במרכז ירכא (`'Yarka center'`) ב‑`2026-09-20`, ונור הביאה אותו. רשמו את הקליטה.

**ד.** ⚠️ נסו לרשום קליטה לחיה מספר 99. מה קרה? ומה היה קורה בלי `PRAGMA foreign_keys = ON`?

---

## 🟢 תרגיל 2 — אילוצים

לכל `INSERT` — **חזו** איזו שגיאה תתקבל, ואז הריצו:

</div>

```sql
INSERT INTO animal (name, species_id, sex) VALUES ('Ghost', 1, 'M');
INSERT INTO animal (name, species_id, sex, status) VALUES ('Twin', 1, 'X', 'available');
INSERT INTO animal (animal_id, name, species_id, sex, status) VALUES (1, 'Dup', 1, 'M', 'available');
INSERT INTO animal (name, species_id, sex, status, chip_number) VALUES ('Copy', 1, 'M', 'available', '985100001');
```

<div dir="rtl">

לכל שגיאה: איזה **חוק עסקי** היא שומרת?

---

## 🟡 תרגיל 3 — UPDATE

**א.** Nala יצאה מהסגר — עדכנו אותה ל‑`available`. (לפי **מזהה**, אחרי `SELECT` שמוודא שזו היא.)

**ב.** כל החתולים בלי גזע — עדכנו ל‑`'Mixed'`. **כמה שורות השתנו? למה לא 3?**

**ג.** ליאור בר עבר לחיפה... רגע, הוא כבר גר בחיפה. הריצו את העדכון בכל זאת. מה מחזיר `changes()`? מה זה מלמד?

**ד.** חשבונות החשמל (`utilities`) נרשמו בלי מע"מ. הוסיפו 18% לכולם. מה הסכום החדש של כל הוצאות החשמל?

**ה.** ⭐ כתבו `UPDATE` אחד שמעדכן את `status` של **כל** חיה שיש לה אימוץ פעיל (בלי `returned_date`) ל‑`adopted` — **רק אם** היא עדיין לא `adopted`. כמה שורות השתנו? מה זה אומר?

---

## 🟡 תרגיל 4 — DELETE

**א.** נסו למחוק את המין "Parrot" (`species_id = 4`). מה קרה? למה?

**ב.** נסו למחוק את סוג החיסון Myxomatosis (`vaccine_type_id = 5`). מה קרה?

**ג.** מחקו את כל ההוצאות **הכלליות** שלפני אפריל 2024. כמה נמחקו? **לפני** — עשו גיבוי של הטבלה.

**ד.** ⭐ במקום למחוק את Daisy (שמתה) — מה כבר עשו בבסיס הנתונים? בדקו. למה זו הדרך הנכונה?

---

## 🔴 תרגיל 5 — DEFAULT ו‑upsert

**א.** צרו את טבלת `donation` מסעיף 7 במודול, והכניסו שלוש תרומות: אחת עם כל העמודות, אחת בלי תאריך, ואחת בלי תאריך ובלי אמצעי תשלום. הציגו את הטבלה.

**ב.** ⚠️ נסו `INSERT INTO donation DEFAULT VALUES;`. מה קרה ולמה?

**ג.** צרו את טבלת `stock` מסעיף 8 במודול. כתבו upsert שמכניס `('dog food sack', 8)` ו‑`('flea collar', 20)`. מה הכמויות אחרי?

**ד.** ⭐ מחקו את ה‑`PRIMARY KEY` מהגדרת `stock` (צרו אותה מחדש בלי), ונסו את אותו upsert. מה קורה? למה?

---

## 🔴 תרגיל 6 — INSERT … SELECT

**א.** צרו טבלת `adoption_archive` עם המבנה של `adoption` (בלי שורות), והעתיקו אליה את כל האימוצים של 2023.

**ב.** צרו טבלת `vip_adopter (person_id, full_name, adoptions)` ומלאו אותה **בשאילתה אחת** — כל מי שאימץ יותר מפעם אחת. (רמז: `INSERT … SELECT … GROUP BY … HAVING`.)

**ג.** ⭐ **multi-table:** צרו `stray_log (intake_id, animal_id, location)` ו‑`surrender_log (intake_id, animal_id, reason)`, ומלאו את שתיהן מ‑`intake`. כמה שורות בכל אחת? איך זה היה נכתב ב‑Oracle?

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[✅ לפתרונות](solutions.md)**

</div>

</div>


<!-- w3schools:start -->
<div dir="rtl">

---

## 🌐 תרגול נוסף ב‑W3Schools

📖 **לקריאה ב‑W3Schools:** [INSERT](https://www.w3schools.com/sql/sql_insert.asp) · [UPDATE](https://www.w3schools.com/sql/sql_update.asp) · [DELETE](https://www.w3schools.com/sql/sql_delete.asp)

> 💻 הפקודות של השיעור הזה **משנות** נתונים או מבנה, ו‑W3Schools לא מאפשר את זה. קראו שם את ההסבר, ואת התרגול עצמו עשו ב‑OneCompiler, על בסיס הנתונים של המקלט ([הוראות](../../resources/setup.md)).

</div>
<!-- w3schools:end -->

<!-- exam-style:start -->
<div dir="rtl">

---

## 🎓 תרגול בסגנון הבחינה

> 🎓 **תרגול בסגנון הבחינה (שאלון 735911).** הסעיפים כאן כתובים בדיוק כמו בבחינה: `Table.Column`, צירוף עם פסיק ומירכאות כפולות. הם רצים על בסיס הנתונים **חוגי ספורט** ([`clubs.sql`](../../exam-prep/db/clubs.sql)). פתרו על הנייר, ואחר כך טענו את הקובץ ל‑OneCompiler ובדקו.

**ב1.** כתבו שאילתה שמוסיפה את המשתתף: ת"ז 1013, השם "אור גבאי", עיר 6, גיל 15, שנת הצטרפות 2025.

**ב2.** כל חוגי השחייה מתייקרים ב‑20 ש"ח. כתבו את פקודת העדכון. כמה רשומות יתעדכנו?

**ב3.** מה יקרה אם נריץ `DELETE FROM ClubMembers;` **בלי** `WHERE`?


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

> ⚠️ **הפעם אתם משנים נתונים.** זה בסדר: כל לחיצה על **Run** מריצה את `school.sql` מחדש, שמוחק את הטבלאות ובונה אותן מאפס. **בכל טעות — Run, ואתם נקיים.**
>
> 💡 אחרי כל `INSERT`/`UPDATE`/`DELETE` הריצו `SELECT` שמוכיח שזה עבד. DML לא מחזיר טבלה, אז אין דרך אחרת לדעת.

**ש1.** רשמו תלמידה חדשה **עם כל העמודות**: `1019`, תאיר אביטן, כיתה 102, `F`, נולדה `2011-02-28`, עיר 3, נרשמה `2026-09-20`, טלפון `050-1000019`.

**ש2.** רשמו תלמידה **עם ארבע עמודות בלבד**: `1020`, סיוון דהן, `F`, נרשמה `2026-09-21`. ⚠️ שלפו אותה — **מה יש בעמודות שלא מילאתם?**

**ש3.** הוסיפו **שתי** היעדרויות ב‑`INSERT` **אחד**: `17` לתאיר (`2026-09-21`, לא מאושרת, בלי סיבה) ו‑`18` לסיוון (`2026-09-21`, מאושרת, `מחלה`). בדקו שיש 18 היעדרויות.

**ש4.** נור עזאם (`1002`) מסרה טלפון: `050-9999999`. עדכנו.

**ש5.** כל המורים מקבלים **העלאה של 3%**, מעוגלת לשקל. עדכנו את כולם בשאילתה אחת, ושלפו את התוצאה.

**ש6.** כל התלמידים **שאין להם כיתה** שובצו לכיתה `102`. עדכנו. **כמה שורות השתנו?**

**ש7.** מחקו את כל ההיעדרויות **המאושרות שלפני `'2026-09-05'`**. כמה נשארו?

**ש8.** ⚠️ **העדכון שלא עשה כלום.** המנהלת ביקשה לתת 5 נקודות בונוס למי שלא נבחן. תלמיד כתב:

</div>

```sql
UPDATE Grades SET Grade = Grade + 5 WHERE Grades.Grade IS NULL;
```

<div dir="rtl">

הריצו, ואז שלפו את שתי השורות האלה. **העדכון דיווח ששתי שורות השתנו — ובכל זאת הציון עדיין `NULL`. הסבירו.** ואיך כותבים את זה נכון?

**ש9.** ⚠️ **שלוש הכנסות שייכשלו.** הריצו כל אחת, **העתיקו את הודעת השגיאה**, והסבירו איזה אילוץ עצר אותה:

</div>

```sql
-- א
INSERT INTO Students (StudentId, FirstName, LastName, Gender, EnrollDate)
VALUES (1021, 'באג', 'בדיקה', 'X', '2026-09-21');

-- ב
INSERT INTO Grades VALUES (1001, 99, 1, 80);

-- ג
INSERT INTO Students (StudentId, FirstName, LastName, Gender, EnrollDate)
VALUES (1001, 'כפול', 'מזהה', 'M', '2026-09-21');
```

<div dir="rtl">

**ש10.** `INSERT INTO … SELECT`. בנו טבלה `AtRisk (StudentId, FullName, Avg1)` ו**מלאו אותה בשאילתה** בכל התלמידים שהממוצע שלהם **מתחת ל‑65**. שלפו אותה מסודרת מהנמוך לגבוה.

**ש11.** **`DEFAULT`.** בנו טבלה `Trips` לטיולים שנתיים: `TripId` (מפתח), `Destination` (חובה), `TripDate` (ברירת מחדל `'2027-05-01'`), `Price` (ברירת מחדל `120`). הכניסו טיול אחד **בלי** תאריך ומחיר, ואחד **עם** — ושלפו.

**ש12.** ⚠️ הריצו `DELETE FROM AtRisk;` — בלי `WHERE`. כמה שורות נשארו? **מה היה קורה אם הייתם כותבים את זה על `Students` בבית ספר אמיתי**, ומה היו שלושת הדברים שהיו מצילים אותך?

</div>
<!-- classroom:end -->
