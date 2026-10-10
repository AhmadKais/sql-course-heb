<div dir="rtl">

# מודול 32 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 הפלטים אמיתיים (SQLite), מהרצה ברצף.

---

## ✅ תרגיל 1 — COMMIT ו‑ROLLBACK

</div>

```sql
-- a
BEGIN;
DELETE FROM expense;
SELECT COUNT(*) FROM expense;        -- 0
ROLLBACK;
SELECT COUNT(*) FROM expense;        -- 22

-- b
BEGIN;
UPDATE animal SET status = 'adopted' WHERE animal_id = 3;
INSERT INTO adoption (animal_id, adopter_id, adoption_date, fee_paid)
VALUES (3, 12, '2026-09-21', 400);
COMMIT;
SELECT name, status FROM animal WHERE animal_id = 3;    -- Rocky | adopted
SELECT COUNT(*) FROM adoption;                          -- 10

-- c
BEGIN;
UPDATE animal SET status = 'adopted' WHERE animal_id = 13;
INSERT INTO adoption (animal_id, adopter_id, adoption_date, fee_paid)
VALUES (13, 99, '2026-09-21', 400);                     -- FOREIGN KEY constraint failed
SELECT name, status FROM animal WHERE animal_id = 13;   -- Rex | adopted   (!!)
ROLLBACK;
SELECT name, status FROM animal WHERE animal_id = 13;   -- Rex | available
```

<div dir="rtl">

**ג. הגילוי:** השגיאה ביטלה רק את ה‑`INSERT`. ה‑`UPDATE` **נשאר** בטרנזקציה הפתוחה. `COMMIT` עכשיו היה שומר את Rex כמאומץ בלי רישום אימוץ. **ההחלטה לבטל הכול — של מי שכותב את הקוד.**

---

## ✅ תרגיל 2 — חיה חדשה וקליטה

</div>

```sql
BEGIN;
INSERT INTO animal (name, species_id, sex, status) VALUES ('Milo', 2, 'M', 'quarantine');
INSERT INTO intake (animal_id, intake_date, intake_type, brought_by, location)
VALUES (last_insert_rowid(), '2026-09-21', 'stray', 2, 'Yarka center');
COMMIT;

SELECT a.name, i.intake_date, i.location
FROM   intake i JOIN animal a ON a.animal_id = i.animal_id
WHERE  a.name = 'Milo';
-- Milo | 2026-09-21 | Yarka center
```

<div dir="rtl">

> 💡 **למה טרנזקציה?** חיה בלי קליטה = "איך היא הגיעה לכאן?". קליטה בלי חיה — המפתח הזר בכלל לא מאפשר. שתי השורות הן **אירוע אחד**.

---

## ✅ תרגיל 3 — החזרת חיה

</div>

```sql
-- a
BEGIN;
UPDATE adoption SET returned_date = '2026-09-21' WHERE adoption_id = 4;
UPDATE animal   SET status = 'available'          WHERE animal_id = 6;
INSERT INTO intake (animal_id, intake_date, intake_type, brought_by, reason)
VALUES (6, '2026-09-21', 'surrender', 9, 'returned by adopter - moving');
COMMIT;
-- Tom | available
```

<div dir="rtl">

**ב.** בלי שורה 3, Tom "זמין" — אבל **אין קליטה** שמסבירה מתי ואיך חזר. שאילתת "כמה זמן חיה מחכה" (מודול 31) תחשב את ההמתנה שלו מ‑2023 — טעות של שלוש שנים. ובלי שורה 1 — `current_home` (מודול 28) עדיין יראה אותו אצל שירה. **שלושה שינויים שמתארים מציאות אחת — או כולם, או אף אחד.**

**ג.** **מודול 10** (מעקב אחר שינויים): כל כניסה למקלט היא `intake` חדש, ואימוץ שהסתיים מסומן ב‑`returned_date` — לא נמחק. כך ההיסטוריה המלאה נשמרת (ראו לונה), ואפשר לחשב שהות **לכל** תקופה בנפרד.

---

## ✅ תרגיל 4 — SAVEPOINT

</div>

```sql
BEGIN;
UPDATE species SET adoption_fee = adoption_fee * 1.1;
SAVEPOINT after_fees;
UPDATE animal SET status = 'available' WHERE status = 'adopted';
ROLLBACK TO after_fees;
COMMIT;

SELECT name, adoption_fee FROM species;          -- Dog 440, Cat 275, Rabbit 110, Parrot 165
SELECT COUNT(*) FROM animal WHERE status = 'available';
-- the same number as before the transaction (the mistaken UPDATE was undone)
```

<div dir="rtl">

---

## ✅ תרגיל 5 — מקביליות

</div>

```sql
BEGIN;
UPDATE animal SET status = 'adopted' WHERE animal_id = 13 AND status = 'available';
SELECT changes();      -- 1   "I got him"
UPDATE animal SET status = 'adopted' WHERE animal_id = 13 AND status = 'available';
SELECT changes();      -- 0   "someone was faster"
ROLLBACK;
```

<div dir="rtl">

**א.** ההרצה השנייה מדמה **מתנדב שני** שמנסה לאמץ את אותו כלב. התנאי `AND status = 'available'` כבר לא מתקיים, ו‑`changes() = 0` מודיע לו שהוא איחר.

**ב.** ב"`SELECT` ואז `UPDATE`" יש **פער זמן** בין הבדיקה לפעולה. בפער הזה מתנדב אחר יכול לאמץ — והבדיקה כבר לא נכונה. ב‑`UPDATE … WHERE status = 'available'` הבדיקה והשינוי הם **פקודה אחת**, ובסיס הנתונים נועל את השורה בזמן הביצוע — אין פער.

---

## ✅ תרגיל 6 — DDL בתוך טרנזקציה

**א.** ב‑SQLite: `notes` **לא קיימת**, והוצאות המזון — **4**, כמו בהתחלה. SQLite מאפשר DDL בתוך טרנזקציה, ו‑`ROLLBACK` מבטל גם אותו.

**ב.** ב‑Oracle: `CREATE TABLE` מבצע **`COMMIT` אוטומטי** לפני ואחרי. כלומר — `notes` נוצרת ונשמרת, ו‑`ROLLBACK` מבטל רק את ה‑`DELETE` (שבא **אחרי** ה‑CREATE ועדיין בהמתנה). אבל אם הסדר היה הפוך — `DELETE` ואז `CREATE` — ה‑`DELETE` היה נשמר לצמיתות. **ב‑Oracle — לעולם לא DDL באמצע עבודה שאולי תבטלו.**

---

## ✅ תרגיל 7 — הכנה להסמכה

**א.** רק ה‑**`UPDATE`**. `ROLLBACK TO a` מבטל את כל מה שאחרי savepoint `a` — ה‑`DELETE` וה‑`INSERT` (ו‑savepoint `b` נעלם איתם). `COMMIT` שומר את מה שנשאר.

**ב.** `ROLLBACK` — מבטל **הכול** ו**מסיים** את הטרנזקציה. `ROLLBACK TO SAVEPOINT x` — מבטל רק מה שאחרי `x`, והטרנזקציה **ממשיכה** (צריך עדיין `COMMIT` או `ROLLBACK`).

**ג.** את **הערך הישן** — לפני השינוי של A. ב‑Oracle אף אחד לא רואה שינויים שלא אושרו (read consistency). B גם לא מחכה — קוראים לא נחסמים.

**ד.**

| | ההבטחה | במקלט |
|---|---|---|
| **A**tomicity | הכול או כלום | אימוץ = סטטוס + רישום, שניהם או אף אחד |
| **C**onsistency | מצב תקין ⟵ מצב תקין | אי אפשר לסיים עם אימוץ של אדם שלא קיים |
| **I**solation | לא רואים שינויים לא‑גמורים של אחרים | האתר לא מציג את Rocky "באמצע אימוץ" |
| **D**urability | אחרי `COMMIT` — שמור, גם בנפילת חשמל | המשפחה קיבלה אישור; האימוץ לא ייעלם |

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[❓ לשאלות](questions.md)**

</div>

</div>

<!-- classroom:start -->
<div dir="rtl">

---

## 💪 תרגול בכיתה — פתרונות

> 🏫 על [`school.sql`](../../resources/school-db/). כל הפלטים כאן **אמיתיים** — כל שאילתה הורצה על בסיס הנתונים, נכון לתאריך הייחוס `'2026-09-21'`.

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

> 💡 כל הפלטים כאן הורצו ב‑SQLite.

</div>

```sql
-- ש1
BEGIN TRANSACTION;
UPDATE Grades SET Grade = 100 WHERE StudentId = 1012;
SELECT StudentId, CourseCode, Grade FROM Grades WHERE StudentId = 1012;
ROLLBACK;
SELECT StudentId, CourseCode, Grade FROM Grades WHERE StudentId = 1012;

-- ש2
BEGIN TRANSACTION;
UPDATE Students SET Phone = '050-0000000' WHERE StudentId = 1002;
COMMIT;
ROLLBACK;                                   -- ❌

-- ש3
UPDATE Students SET Phone = 'XXX' WHERE StudentId = 1001;
ROLLBACK;                                   -- ❌  אין טרנזקציה פתוחה

-- ש4
BEGIN TRANSACTION;
UPDATE Teachers SET Salary = 20000 WHERE TeacherCode = 1;
SAVEPOINT raise1;
UPDATE Teachers SET Salary = 30000 WHERE TeacherCode = 2;
ROLLBACK TO raise1;
COMMIT;

-- ש6
BEGIN TRANSACTION;
DELETE FROM Absences;
SELECT COUNT(*) AS AfterDelete FROM Absences;      -- 0
ROLLBACK;
SELECT COUNT(*) AS AfterRollback FROM Absences;    -- 16

-- ש8
BEGIN TRANSACTION;
SAVEPOINT step1;
UPDATE Teachers SET Salary = 11000 WHERE TeacherCode = 5;
SAVEPOINT step2;
UPDATE Teachers SET Salary = 99999 WHERE TeacherCode = 5;
ROLLBACK TO step2;
RELEASE step1;
COMMIT;

-- ש9
BEGIN TRANSACTION;
DELETE FROM Absences WHERE StudentId = 1015;      -- הילדים קודם
DELETE FROM Grades   WHERE StudentId = 1015;
DELETE FROM Students WHERE StudentId = 1015;      -- האב אחרון
SELECT (SELECT COUNT(*) FROM Students WHERE StudentId=1015) AS S,
       (SELECT COUNT(*) FROM Grades   WHERE StudentId=1015) AS G,
       (SELECT COUNT(*) FROM Absences WHERE StudentId=1015) AS A;
ROLLBACK;
```

<div dir="rtl">

**ש1.** **בתוך** הטרנזקציה כל ארבעת הציונים של ג'וד היו 100. **אחרי** ה‑`ROLLBACK` הם חזרו ל‑47, 51, 42, 39.

<figure dir="ltr" class="dbtable">

| StudentId | CourseCode | Grade (בתוך) | Grade (אחרי ROLLBACK) |
|:---:|:---:|:---:|:---:|
| 1012 | 12 | 100 | 47 |
| 1012 | 13 | 100 | 51 |
| 1012 | 16 | 100 | 42 |
| 1012 | 16 | 100 | 39 |

</figure>

**מה בדיוק עשה ה‑`ROLLBACK`?** הוא לא "הריץ `UPDATE` הפוך". מרגע ה‑`BEGIN`, בסיס הנתונים שומר ביומן (log) את הערכים **הקודמים** של כל מה שהשתנה. `ROLLBACK` מחזיר אותם, והטרנזקציה נעלמת כאילו לא קרתה. גם ה‑`SELECT` הראשון מעניין: **אתם** ראיתם 100, אבל אף משתמש אחר בבסיס הנתונים לא ראה אותו — שינוי לא מאושר נראה רק למי שעשה אותו.

**ש2.** ההודעה:

</div>

```text
cannot rollback - no transaction is active
```

<div dir="rtl">

**מה היא אומרת: `COMMIT` הוא נקודת אל‑חזור.** ברגע שהוא נעשה, הטרנזקציה **נסגרה** — אין יותר מה לבטל, ולכן גם אין טרנזקציה "פתוחה" שאפשר לעשות לה `ROLLBACK`. הטלפון של נור הוא `050-0000000`, גם עכשיו וגם אחרי התנתקות והתחברות מחדש.

זה בדיוק ה‑**D** של ACID (Durability). ואחרי `COMMIT` הדרך היחידה "לחזור" היא `UPDATE` חדש שמחזיר את הערך — אם אתם זוכרים מה הוא היה.

**ש3.** אותה הודעת שגיאה — **ו‑`Phone` הוא `'XXX'`.**

<figure dir="ltr" class="dbtable">

| StudentId | Phone |
|:---:|:---:|
| 1001 | XXX |

</figure>

**`autocommit`** הוא מצב ברירת המחדל: כל פקודה בודדת היא **טרנזקציה שלמה בפני עצמה**, ש‑`COMMIT` נעשה לה אוטומטית ברגע שהיא הסתיימה. לכן כשהגיע ה‑`ROLLBACK`, ה‑`UPDATE` כבר היה סופי מזמן, ולא הייתה טרנזקציה פתוחה.

**המסקנה המעשית, והיא כל השיעור:** `ROLLBACK` **אינו** כפתור "בטל" של בסיס הנתונים. הוא עובד **רק** בתוך טרנזקציה שפתחתם במפורש. אם לא כתבתם `BEGIN` — **אין רשת ביטחון**, וכל `UPDATE` ו‑`DELETE` שהרצתם הם עובדה מוגמרת.

**ש4.** **מורה 2 חזר ל‑11200; מורה 1 נשאר 20000** — וה‑`COMMIT` קבע את זה.

<figure dir="ltr" class="dbtable">

| שלב | סרחאן (1) | בר-לב (2) |
|:---:|:---:|:---:|
| אחרי שני העדכונים | 20000 | 30000 |
| אחרי `ROLLBACK TO raise1` | 20000 | **11200** |
| אחרי `COMMIT` | **20000** | **11200** |

</figure>

`SAVEPOINT` הוא **סימנייה בתוך הטרנזקציה**. `ROLLBACK TO <שם>` מבטל רק את מה שקרה **מאז** הסימנייה, ומשאיר את מה שהיה לפניה — והטרנזקציה **נשארת פתוחה**. (`ROLLBACK` בלי שם מבטל הכול וסוגר.)

**למה זה שימושי?** בתהליך ארוך — ייבוא של 1,000 שורות, או עיבוד סוף שנה — אתם לא רוצים שכשלון בשורה 700 יזרוק את 699 השורות הראשונות. שמים `SAVEPOINT` לפני כל קטע, ובכשלון חוזרים רק קטע אחד אחורה.

**ש5א.** ההודעה:

</div>

```text
UNIQUE constraint failed: Grades.StudentId, Grades.CourseCode, Grades.Term
```

<div dir="rtl">

המפתח הראשי של `Grades` הוא `(StudentId, CourseCode, Term)`. לג'וד יש במקצוע 16 **שתי** שורות: מחצית 1 (ציון 42) ומחצית 2 (ציון 39). ה‑`UPDATE` ניסה להפוך את שורת מחצית 2 ל‑מחצית 1 — וכך נוצרו **שתי שורות עם אותו מפתח בדיוק**. המפתח הראשי חסם את זה.

**ש5ב.** ה‑`SELECT` מראה **`ClassCode = 103`** ו‑**17 היעדרויות**:

<figure dir="ltr" class="dbtable">

| Stage | Class1 | Abs1 |
|:---:|:---:|:---:|
| inside tx | 103 | 17 |

</figure>

כלומר **לא. השגיאה לא ביטלה את הטרנזקציה.** שתי הפעולות הראשונות הצליחו, הן עדיין שם, והטרנזקציה **פתוחה וממתינה להוראות שלכם**. בסיס הנתונים ביטל את הפקודה **שנכשלה** בלבד; את ההחלטה מה לעשות עם מה שכן הצליח הוא משאיר לכם.

**זו הנקודה שהכי קל לטעות בה**, ובמיוחד בסקריפט שרץ לבד: קל להניח "אם משהו נכשל, הכול התבטל". לא. צריך לבדוק את תוצאת כל פקודה ולהחליט.

**ש5ג.** שתי ההרצות, אותן שתי פעולות שהצליחו — ושתי תוצאות שונות לגמרי:

<figure dir="ltr" class="dbtable">

| הסיום | ClassCode של 1012 | מספר ההיעדרויות | שורות Term=2 במקצוע 16 |
|:---:|:---:|:---:|:---:|
| `ROLLBACK;` | **104** | **16** | 1 |
| `COMMIT;` | **103** | **17** | 1 |

</figure>

**הגרסה עם ה‑`COMMIT` היא "העברת תלמיד שלא הושלמה":** ג'וד רשומה בכיתה 103, יש לה רשומת היעדרות על המעבר — **ושורת הציון שלה עדיין במחצית 2**, כי הפעולה השלישית נכשלה. חצי העברה. בבסיס הנתונים אין שום סימן שמשהו לא גמור; בדוח הבא פשוט יהיה נתון מוזר, ואף אחד לא יידע מאיפה.

**הגרסה עם ה‑`ROLLBACK` היא התשובה הנכונה**: או שההעברה קורית **כולה**, או שהיא **לא קורית בכלל**, ואז מתקנים את הבאג (צריך `DELETE` ואחריו `INSERT`, לא `UPDATE` של המפתח) ומריצים שוב. זה בדיוק ה‑**A** של ACID, ו`BEGIN` הוא מה שנותן לכם את הבחירה.

**ש6.** **0 אחרי המחיקה, 16 אחרי ה‑`ROLLBACK`.** כל 16 ההיעדרויות חזרו.

<figure dir="ltr" class="dbtable">

| Stage | Count |
|:---:|:---:|
| AfterDelete | 0 |
| AfterRollback | 16 |

</figure>

**והקשר לשיעור 25:** שם, בש12, ראינו ש‑`DELETE FROM טבלה;` בלי `WHERE` מוחק הכול בלי אזהרה — ואמרנו ששלושה דברים יכולים להציל אותך. **זה השני מהם**, ועכשיו ראיתם אותו עובד: אותה מחיקה בדיוק, ומצב שלם מוחזר בפקודה אחת.

ההרגל שמוציאים מכאן: לפני כל `DELETE` או `UPDATE` רחב על נתונים אמיתיים — `BEGIN TRANSACTION`, הפקודה, `SELECT` שבודק, ו**רק אז** `COMMIT` או `ROLLBACK`.

**ש7.** `Temp1` **לא שרדה** — החיפוש ב‑`sqlite_master` החזיר 0 שורות. ב‑SQLite גם **DDL הוא חלק מהטרנזקציה**, ו‑`ROLLBACK` מחזיר גם יצירת טבלאות.

⚠️ **באורקל התשובה הפוכה: `Temp1` הייתה שורדת.** באורקל (וב‑MySQL) כל פקודת DDL גורמת ל‑**`COMMIT` אוטומטי** — גם של כל מה שהיה פתוח לפניה:

</div>

```text
Oracle:
   BEGIN
   UPDATE Students ...        <- שינוי לא מאושר
   CREATE TABLE Temp1 ...     <- DDL  =>  COMMIT אוטומטי של ה-UPDATE!
   ROLLBACK                   <- לא עושה כלום. מאוחר מדי.
```

<div dir="rtl">

**המסקנה:** באורקל, **אל תערבבו DDL עם DML באותה טרנזקציה**. פקודת `CREATE` תמימה באמצע סקריפט יכולה לאשר שינויים שהתכוונתם לבטל — וזו תקלה שקשה מאוד לאתר בדיעבד.

**ש8.** השכר בסוף הוא **11000**.

<figure dir="ltr" class="dbtable">

| Stage | Salary |
|:---:|:---:|
| after rollback to step2 | 11000 |
| after release step1 | 11000 |
| after commit | 11000 |

</figure>

`ROLLBACK TO step2` ביטל את העדכון ל‑99999 והשאיר את 11000. ואז **`RELEASE step1`** — וזו המילה שצריך להבין: היא **לא** מבטלת כלום ולא מאשרת כלום. היא פשוט **מוחקת את הסימנייה**: אחרי `RELEASE`, אי אפשר יותר לעשות `ROLLBACK TO step1`.

למה זה קיים? כי סימנייה היא משאב שהטרנזקציה מחזיקה. בתהליך עם 1,000 נקודות שמירה, אחרי שקטע הסתיים בהצלחה אין טעם לשמור את הסימנייה שלפניו — `RELEASE` משחרר אותה ואומר "הקטע הזה סגור". השינויים עצמם נקבעים רק ב‑`COMMIT`.

**ש9.** אחרי שלוש המחיקות — אפס שורות בכל שלוש הטבלאות; אחרי ה‑`ROLLBACK` — הכול חזר.

<figure dir="ltr" class="dbtable">

| S (Students) | G (Grades) | A (Absences) |
|:---:|:---:|:---:|
| 0 | 0 | 0 |

</figure>

**למה הסדר חשוב?** בגלל **המפתחות הזרים** (שיעור 27). `Grades.StudentId` ו‑`Absences.StudentId` מצביעים ל‑`Students`. אם מתחילים מ‑`DELETE FROM Students`, בסיס הנתונים מסרב: `FOREIGN KEY constraint failed` — כי מיד לאחר המחיקה היו בטבלאות שורות שמצביעות לתלמיד שלא קיים.

הכלל: **הילדים קודם, האב אחרון.** בדיוק הסדר ההפוך מ‑`INSERT`, שבו האב חייב להיות קיים לפני הילדים. (וזה בדיוק מה ש‑`ON DELETE CASCADE` עושה בשבילכם — ראו שיעור 27 ש12.)

**ש10.** **ACID בבית הספר "עתיד":**

| האות | מה זה | הדוגמה |
|------|--------|---------|
| **A** — Atomicity | הטרנזקציה היא **יחידה אחת**: הכול או כלום | **ש5 בדיוק.** העברת תלמיד = 3 פעולות. אם השלישית נכשלה, אסור שהראשונות יישארו — ג'וד תהיה "חצי בכיתה 103" |
| **C** — Consistency | בסיס הנתונים עובר ממצב **חוקי** למצב **חוקי**, והאילוצים נשמרים | ש9: אחרי מחיקת איתי **אין** ציונים יתומים. בסיס הנתונים לא ייתן לכם לעבור למצב שבו ציון מצביע לתלמיד שלא קיים |
| **I** — Isolation | טרנזקציות **לא רואות** זו את העבודה הלא‑מאושרת של זו | ש1: כשהעלינו את ציוני ג'וד ל‑100, **רק אנחנו** ראינו 100. המחנך שהריץ דוח באותו רגע ראה 47, 51, 42, 39 — ולא דוח שבור באמצע עדכון |
| **D** — Durability | אחרי `COMMIT` השינוי **שורד הכול** — התנתקות, כיבוי, קריסה | ש2: הטלפון של נור הוא `050-0000000` גם אחרי שסגרנו וחיברנו מחדש. ולכן גם אין `ROLLBACK` |

**ש11א.** הציון יהיה **100** — הערך של מי שלחץ "שמור" **אחרון**.

**ש11ב.** **לא. אף אחד לא קיבל שום שגיאה.** שני ה‑`UPDATE`‑ים הצליחו, ושניהם קיבלו "1 row affected".

**ש11ג.** **התיקון של חוסאם ל‑99 אבד** — הוא נכתב, ואז נדרס. זה נקרא **עדכון אבוד** (Lost Update), והוא מסוכן בדיוק כי הוא שקט: חוסאם **בטוח** שהציון 99, הוא ראה אישור, והוא יגלה את האמת רק אם יפתח את המסך שוב.

⚠️ **שימו לב שטרנזקציה לבדה לא פותרת את זה.** גם אם כל אחד מהם עטף את העדכון שלו ב‑`BEGIN … COMMIT`, שתי הטרנזקציות תקינות לגמרי — אחת פשוט רצה אחרי השנייה. הבעיה אינה בעדכון; היא ב**הנחה** שהערך לא השתנה מאז שקראתם אותו.

**שלוש הדרכים למנוע:**

| השיטה | איך | מתי |
|--------|-----|------|
| **נעילה פסימית** | `SELECT … FOR UPDATE` — נועל את השורה בזמן הקריאה. אורלי תחכה עד שחוסאם יסיים | התנגשויות **תכופות**, פעולות קצרות |
| **נעילה אופטימית** | שומרים `Version` או `UpdatedAt` בשורה, ומעדכנים עם `WHERE Version = <מה שקראתי>`. אם 0 שורות השתנו — מישהו הקדים, ומודיעים למשתמש | התנגשויות **נדירות** — המקרה הנפוץ באפליקציות ווב |
| **לא לקרוא-ולכתוב בכלל** | `SET Grade = Grade + 1` במקום `SET Grade = 99`. הקריאה והכתיבה הן פעולה **אחת** אטומית | כשהעדכון הוא שינוי יחסי (בונוס, מלאי, מונה) |

**ש12.** הרצף שהייתי ממליץ למזכירה — ולא במקרה רק שתי שורות מתוכו הן המחיקה עצמה:

</div>

```sql
-- 1.  קודם כל: לראות את מי זה הולך לתפוס. בלי למחוק כלום.
SELECT COUNT(*) FROM Students WHERE <התנאי>;
SELECT StudentId, FirstName, LastName, ClassCode FROM Students WHERE <התנאי>;
--     מצפים ל-200. קיבלתם 1,847? עצרו. התנאי שגוי.

-- 2.  גיבוי. לפני, לא אחרי.
CREATE TABLE Students_backup_20260921 AS SELECT * FROM Students;

-- 3.  עכשיו, ועם רשת ביטחון:
BEGIN TRANSACTION;

DELETE FROM Absences WHERE StudentId IN (SELECT StudentId FROM Students WHERE <התנאי>);
DELETE FROM Grades   WHERE StudentId IN (SELECT StudentId FROM Students WHERE <התנאי>);
DELETE FROM Students WHERE <התנאי>;

-- 4.  לבדוק *בתוך* הטרנזקציה, לפני שמאשרים:
SELECT COUNT(*) AS StudentsLeft FROM Students;              -- מצפים לירידה של 200 בדיוק
SELECT COUNT(*) AS OrphanGrades FROM Grades
WHERE  StudentId NOT IN (SELECT StudentId FROM Students);   -- חייב להיות 0

-- 5.  ורק אם הכול כמצופה:
COMMIT;        -- או:  ROLLBACK;  אם מספר אחד לא מסתדר
```

<div dir="rtl">

**חמש ההחלטות שבתוך הרצף הזה, וכל אחת מהן מחיר של דקה:**

1. **`SELECT` לפני `DELETE`**, עם אותו `WHERE` בדיוק. זו הבדיקה היחידה שתופסת תנאי שגוי **לפני** שהוא הורס.
2. **גיבוי** — הדבר היחיד שעובד אחרי `COMMIT` (ש2).
3. **`BEGIN`** — בלעדיו אין `ROLLBACK` בכלל (ש3).
4. **סדר המחיקה: ילדים לפני אב** (ש9).
5. **בדיקה בתוך הטרנזקציה**, כולל שאילתת חריגות שצריכה להחזיר 0. התשובה "0 יתומים" היא מה שמרשה לכם ללחוץ `COMMIT`.

> 💡 **ולסיום, הדבר שכדאי לקחת מהשיעור:** `BEGIN TRANSACTION` היא השורה הזולה ביותר ב‑SQL. היא לא עולה כלום, היא לא מאטה כלום ברמה שמורגשת — והיא ההבדל בין "טעיתי ותיקנתי" לבין "טעיתי ועכשיו צריך גיבוי".

</div>
<!-- classroom:end -->
