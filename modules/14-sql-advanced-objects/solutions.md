<div dir="rtl">

# מודול 29 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 הפלטים אמיתיים (SQLite). תוכניות ביצוע עשויות להיראות מעט שונה בגרסאות אחרות.

---

## ✅ תרגיל 1 — מזהים אוטומטיים

**א.** D קיבל **3** — המספר של C, שנמחק, **מוחזר לשימוש**.

**ב.** עם `AUTOINCREMENT`, D קיבל **4**. ב‑`sqlite_sequence`: `donation | 4`.

**ג.**

</div>

```sql
INSERT INTO animal (name, species_id, sex, status) VALUES ('Milo', 2, 'M', 'quarantine');
SELECT last_insert_rowid();                          -- 21

INSERT INTO intake (animal_id, intake_date, intake_type)
VALUES (last_insert_rowid(), '2026-09-21', 'stray');   -- Milo's id, without guessing
```

<div dir="rtl">

> ⚠️ **שימו לב:** אחרי ה‑`INSERT` לקליטה, `last_insert_rowid()` כבר מחזיר את מזהה **הקליטה**. אם צריך את מזהה החיה לעוד פעולות — שמרו אותו קודם (באפליקציה, במשתנה).

**ד.** שני פקידים מקבלים חיה באותה שנייה. שניהם קוראים `MAX = 20`, ושניהם מנסים להכניס 21. אחד מצליח, השני מקבל שגיאת `UNIQUE` — או, אם אין מפתח ראשי, **שתי חיות עם מספר 21**. Sequence / `AUTOINCREMENT` מחלק מספרים **בתוך** בסיס הנתונים, אחד‑אחד, ולכן לעולם לא נותן את אותו מספר פעמיים.

---

## ✅ תרגיל 2 — Sequence ב‑Oracle

</div>

```sql
-- a
CREATE SEQUENCE donation_seq START WITH 1000 INCREMENT BY 1 NOCACHE;

-- b
INSERT INTO donation (donation_id, donor_name, amount)
VALUES (donation_seq.NEXTVAL, 'Haifa Rotary', 5000);

INSERT INTO receipt (receipt_id, donation_id, issued_date)
VALUES (receipt_seq.NEXTVAL, donation_seq.CURRVAL, SYSDATE);   -- CURRVAL = the same donation

-- c
CREATE TABLE donation (
  donation_id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1000) PRIMARY KEY,
  donor_name  VARCHAR2(100) NOT NULL,
  amount      NUMBER(10,2)  NOT NULL
);
```

<div dir="rtl">

---

## ✅ תרגיל 3 — אינדקסים

**א.** לפני: `SCAN animal`. אחרי `CREATE INDEX idx_animal_name ON animal(name);` ⟵ `SEARCH animal USING INDEX idx_animal_name (name=?)`.

**ב.**

</div>

```text
sqlite_autoindex_species_1   <- UNIQUE on species.name
sqlite_autoindex_animal_1    <- UNIQUE on animal.chip_number
idx_animal_name              <- ours
```

<div dir="rtl">

**האינדקסים האוטומטיים** נוצרו מאילוצי `UNIQUE` — כדי לבדוק כפילויות מהר. (`PRIMARY KEY` מסוג `INTEGER` ב‑SQLite הוא ה‑rowid עצמו — אינדקס מובנה.)

**ג.** `SCAN vaccination` ⟵ `CREATE INDEX idx_vacc_animal ON vaccination(animal_id);` ⟵ `SEARCH vaccination USING INDEX idx_vacc_animal (animal_id=?)`.

**ד.**

</div>

```text
before:  |--SCAN v                                         <- every vaccination row
         `--SEARCH a USING INTEGER PRIMARY KEY (rowid=?)

after:   |--SEARCH a USING COVERING INDEX idx_animal_name (name=?)   <- find Rocky
         `--SEARCH v USING INDEX idx_vacc_animal (animal_id=?)       <- jump to his shots
```

<div dir="rtl">

**לפני:** עובר על **כל** החיסונים, ולכל אחד בודק אם החיה היא Rocky. **אחרי:** מוצא את Rocky באינדקס, וקופץ ישר לחיסונים שלו. על 28 שורות — אותו זמן. על 10 מיליון — שניות מול אלפיות.

> 💡 **COVERING INDEX** — כל מה שהשאילתה צריכה מ‑`animal` (`name` ו‑`animal_id`) נמצא **באינדקס עצמו**, אז אפילו לא צריך לקרוא את הטבלה.

---

## ✅ תרגיל 4 — מתי אינדקס לא עוזר

**א.** האינדקס ממוין לפי `name`, לא לפי `UPPER(name)`. בשביל להשוות, SQLite צריך לחשב `UPPER` לכל שורה ⟵ `SCAN`. **תיקון:** `CREATE INDEX idx_animal_upper_name ON animal(UPPER(name));` ⟵ `SEARCH … (<expr>=?)`.

**ב.** אינדקס ממוין לפי **תחילת** הערך. "מסתיים ב‑na" יכול להיות בכל מקום ברשימה הממוינת — אין לאן לקפוץ.

**ג.**

</div>

```sql
EXPLAIN QUERY PLAN SELECT * FROM expense WHERE STRFTIME('%Y', expense_date) = '2024';
-- SCAN expense         <- even with an index on expense_date: a function on the column

-- rewrite: a range on the column itself
EXPLAIN QUERY PLAN SELECT * FROM expense WHERE expense_date BETWEEN '2024-01-01' AND '2024-12-31';
-- SEARCH expense USING INDEX idx_exp_date (expense_date>? AND expense_date<?)
```

<div dir="rtl">

> 🔑 **"פונקציה על העמודה" ⟵ "טווח על העמודה".** במקום `STRFTIME('%Y', d) = '2024'` — `d >= '2024-01-01' AND d < '2025-01-01'`. אותה תשובה, ואינדקס רגיל עובד. זו אחת מהטכניקות החשובות בכתיבת שאילתות מהירות.

**ד.**

| העמודה | אינדקס? | למה |
|--------|---------|-----|
| `chip_number` | ✅ (כבר יש — `UNIQUE`) | חיפוש מדויק, ערכים ייחודיים |
| `vaccination.animal_id` | ✅ | מפתח זר — כל JOIN |
| `expense.expense_date` | ✅ | דוחות לפי תקופה (טווח) |
| `name` | ✅ כנראה | מחפשים לפי שם הרבה |
| `status` | ⚠️ תלוי | 5 ערכים בלבד. שווה רק אם מחפשים ערך **נדיר** (`medical`) |
| `sex` | ❌ | 3 ערכים, כל אחד שליש מהטבלה — אינדקס לא חוסך כלום |

---

## ✅ תרגיל 5 — ראיון בכיתה

</div>

```sql
-- a
SELECT a.name, a.species_id, a.weight_kg
FROM   animal a
WHERE  a.weight_kg = (SELECT MAX(b.weight_kg) FROM animal b WHERE b.species_id = a.species_id)
ORDER  BY a.species_id;
```

```text
name     species_id  weight_kg
-------  ----------  ---------
Rex      1           38.7
Oscar    2           5.5
Thumper  3           1.8
Coco     4           0.1
```

```sql
-- b1   31.0
SELECT MAX(weight_kg) FROM animal
WHERE  weight_kg < (SELECT MAX(weight_kg) FROM animal);

-- b2   Rocky 31.0
SELECT name, weight_kg FROM animal ORDER BY weight_kg DESC LIMIT 1 OFFSET 1;
```

<div dir="rtl">

> 💡 **ההבדל בין שתי הדרכים:** אם שתי חיות שוקלות 38.7, `OFFSET 1` יחזיר את **השנייה מהן** (38.7), ו‑`MAX … < MAX` יחזיר את **הערך השני** (31.0). מראיין טוב ישאל בדיוק את זה — "ומה אם יש שוויון?"

</div>

```sql
-- c   Luna 3, Rocky 4
SELECT a.name, COUNT(*)
FROM   animal a
JOIN   vaccination v ON v.animal_id = a.animal_id
GROUP  BY a.animal_id
HAVING COUNT(*) > 2;
```

<div dir="rtl">

**ד. שלוש הטעויות** בשאילתה מסעיף 9.3:
1. **`WHERE COUNT(*) > 2`** — פונקציה מצרפית ב‑`WHERE`. צריך `HAVING`.
2. **אין `GROUP BY`** — בלי קיבוץ, `COUNT(*)` סופר את כל השורות כקבוצה אחת.
3. **`name` לבד** — לא ברור אם `a.name` (ובשאילתה עם JOIN — תמיד כינוי). ובלי `GROUP BY` על החיה — עמודה רגילה ליד מצרפית.

התיקון = סעיף ג'.

**ה.** תשובה טובה, בשלושה משפטים: *"אינדקס הוא עותק ממוין של עמודה, כמו אינדקס בסוף ספר — הוא מאפשר לקפוץ ישר לשורות במקום לסרוק את כל הטבלה. אבל כל `INSERT` ו‑`UPDATE` צריך לעדכן גם את האינדקס, והוא תופס מקום. לכן שמים אינדקס על עמודות שמחפשים ומחברים לפיהן — בעיקר מפתחות זרים — ולא על כל עמודה."*

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

</div>

```sql
-- ש1
EXPLAIN QUERY PLAN SELECT * FROM Students WHERE Students.LastName = 'כהן';   -- לפני
CREATE INDEX idx_students_lastname ON Students(LastName);
EXPLAIN QUERY PLAN SELECT * FROM Students WHERE Students.LastName = 'כהן';   -- אחרי

-- ש3
CREATE UNIQUE INDEX idx_teachers_phone ON Teachers(Phone);
INSERT INTO Teachers VALUES (8, 'דנה', 'אלון', 'אמנות', '2026-09-01', 9500, 4, '050-7010101');  -- ❌

-- ש4
CREATE INDEX idx_grades_course_term ON Grades(CourseCode, Term);
EXPLAIN QUERY PLAN SELECT * FROM Grades WHERE Grades.CourseCode = 11 AND Grades.Term = 2;
EXPLAIN QUERY PLAN SELECT * FROM Grades WHERE Grades.Term = 2;

-- ש5
SELECT name, tbl_name FROM sqlite_master
WHERE  type = 'index' AND name NOT LIKE 'sqlite_%' ORDER BY name;

-- ש6
DROP INDEX idx_students_lastname;

-- ש7
CREATE TABLE Notices (
  NoticeId INTEGER PRIMARY KEY AUTOINCREMENT,
  Title    TEXT NOT NULL,
  Posted   TEXT NOT NULL DEFAULT '2026-09-21'
);
INSERT INTO Notices (Title) VALUES ('אספת הורים');
INSERT INTO Notices (Title) VALUES ('טיול שנתי');
INSERT INTO Notices (Title) VALUES ('בחינות מחצית');

-- ש8
SELECT name, seq FROM sqlite_sequence;

-- ש9
DELETE FROM Notices WHERE NoticeId = 3;
INSERT INTO Notices (Title) VALUES ('הודעה חדשה');
SELECT * FROM Notices;
SELECT name, seq FROM sqlite_sequence;

-- ש10
SELECT Students.rowid, Students.StudentId, Students.FirstName FROM Students LIMIT 3;

-- ש11
CREATE VIEW Pupils AS SELECT * FROM Students;
SELECT COUNT(*) AS n FROM Pupils;

-- ש12
CREATE INDEX idx_students_gender ON Students(Gender);
EXPLAIN QUERY PLAN SELECT * FROM Students WHERE Students.Gender = 'F';
```

<div dir="rtl">

**ש1.** שתי שורות, ובהן כל השיעור:

</div>

```text
לפני:   SCAN Students
אחרי:   SEARCH Students USING INDEX idx_students_lastname (LastName=?)
```

<div dir="rtl">

| המילה | מה המנוע עושה |
|--------|----------------|
| **`SCAN`** | קורא את **כל** 18 השורות, אחת‑אחת, ובודק בכל אחת אם שם המשפחה הוא 'כהן' |
| **`SEARCH … USING INDEX`** | הולך ישר למקום באינדקס, ומשם לשורות המתאימות |

האינדקס הוא רשימה **ממוינת** של הערכים בעמודה, עם מצביע לשורה. חיפוש ברשימה ממוינת הוא חיפוש בינארי: ב‑18 שורות זה ~5 השוואות במקום 18, וב‑מיליון שורות זה ~20 במקום מיליון. זה ההבדל בין חיפוש שם בספר טלפונים לבין קריאת הספר מהתחלה.

**ש2.** **התוצאה זהה לחלוטין** — אותן שתי שורות, יואב ושירה.

<figure dir="ltr" class="dbtable">

| FirstName | LastName |
|:---:|:---:|
| יואב | כהן |
| שירה | כהן |

</figure>

**וזו הנקודה המרכזית באינדקסים:** אינדקס **לא משנה תשובות, רק מהירות**. הוא לא נתון ולא אילוץ; הוא אופטימיזציה. לכן אפשר לבנות ולמחוק אינדקסים בלי לדאוג לנכונות — ולכן גם אי אפשר "לתקן" שאילתה שגויה באינדקס.

**ש3.** `CREATE UNIQUE INDEX` **עבר**, אף שלרונית ולגלית אין טלפון.

**למה?** אותו כלל של `UNIQUE` משיעור 27: `NULL` אינו שווה ל‑`NULL`, ולכן שני `NULL`ים אינם "ערכים זהים". אינדקס ייחודי מתנהג **בדיוק** כמו אילוץ `UNIQUE` — כי הוא בעצם **אותו דבר**: כש‑SQL מגדיר `UNIQUE`, הוא בונה אינדקס ייחודי מתחת למכסה המנוע. השניים אינם שני מכשירים; הם שם אחד לשניים.

ההכנסה נכשלה:

</div>

```text
UNIQUE constraint failed: Teachers.Phone
```

<div dir="rtl">

הטלפון `050-7010101` כבר שייך לנביל סרחאן. שימו לב שההודעה מדברת על **constraint** אף שבנינו **index** — הוכחה נוספת שמדובר באותו מנגנון.

**ש4.** **רק הראשונה** משתמשת באינדקס:

</div>

```text
WHERE CourseCode = 11 AND Term = 2
    SEARCH Grades USING INDEX idx_grades_course_term (CourseCode=? AND Term=?)   ✅

WHERE Term = 2
    SCAN Grades                                                                   ❌
```

<div dir="rtl">

**למה?** האינדקס ממוין **קודם לפי `CourseCode`, ובתוך כל `CourseCode` לפי `Term`**. זה בדיוק כמו ספר טלפונים הממוין לפי שם משפחה ואז שם פרטי:

| השאלה | בספר טלפונים | באינדקס |
|--------|---------------|----------|
| "כהן, יואב" | קל — דף ה‑כ', ואז יואב | `CourseCode = 11 AND Term = 2` ✅ |
| "כל מי שקוראים לו יואב" | **חייבים לקרוא את כל הספר** | `Term = 2` ❌ |

זה נקרא **כלל העמודה המובילה** (leftmost prefix): אינדקס על `(A, B)` משרת שאילתות על `A` ועל `A`+`B` — אבל **לא** על `B` לבדו. ולכן **סדר העמודות באינדקס מורכב הוא החלטה**, לא פרט טכני: שימו ראשונה את העמודה שמופיעה לבד בשאילתות.

**ש5.** שלושה אינדקסים — ה‑`WHERE name NOT LIKE 'sqlite_%'` מסתיר את האינדקסים שבסיס הנתונים בנה לעצמו למפתחות הראשיים ולאילוצי `UNIQUE`.

<figure dir="ltr" class="dbtable">

| name | tbl_name |
|:---:|:---:|
| idx_grades_course_term | Grades |
| idx_students_lastname | Students |
| idx_teachers_phone | Teachers |

</figure>

**ש6.** האינדקס נעלם; **אף נתון לא נמחק.**

<figure dir="ltr" class="dbtable">

| name |
|:---:|
| idx_grades_course_term |
| idx_teachers_phone |

</figure>

אינדקס הוא **נתון נגזר** — אפשר לבנות אותו מחדש מהטבלה בכל רגע. לכן `DROP INDEX` הוא מהפעולות הבטוחות ביותר ב‑SQL: היא עלולה להאט שאילתות, אבל היא לא יכולה לאבד מידע. (זו גם הסיבה שלפני ייבוא המוני של נתונים מוחקים אינדקסים ובונים אותם מחדש בסוף — מהר יותר.)

**ש7.** **1, 2, 3** — בלי שציינתם מזהה אף פעם.

<figure dir="ltr" class="dbtable">

| NoticeId | Title | Posted |
|:---:|:---:|:---:|
| 1 | אספת הורים | 2026-09-21 |
| 2 | טיול שנתי | 2026-09-21 |
| 3 | בחינות מחצית | 2026-09-21 |

</figure>

זה הפתרון של SQLite לבעיה שאורקל פותר ב‑**`SEQUENCE`**: מי מייצר את המזהה הבא? בשני המקרים התשובה היא "בסיס הנתונים, ולא האפליקציה" — וזה חשוב, כי אם שתי אפליקציות ינסו לחשב "המזהה הגדול + 1" בו‑זמנית, שתיהן יקבלו את אותו מספר.

| | SQLite | Oracle |
|---|--------|--------|
| ההגדרה | `INTEGER PRIMARY KEY AUTOINCREMENT` בעמודה | `CREATE SEQUENCE seq_notices START WITH 1 INCREMENT BY 1;` — **אובייקט נפרד** |
| השימוש | אוטומטי, לא כותבים כלום | `INSERT INTO Notices VALUES (seq_notices.NEXTVAL, 'אספת הורים', …)` |
| שיתוף בין טבלאות | אי אפשר — צמוד לעמודה | **אפשר** — אותו `SEQUENCE` יכול לשרת כמה טבלאות |

**ש8.** `sqlite_sequence` היא טבלת מערכת ש‑**SQLite יצר בעצמו**, ברגע שהגדרתם עמודה עם `AUTOINCREMENT`. היא זוכרת, לכל טבלה כזאת, **מה המזהה הגבוה ביותר שחולק עד כה**.

<figure dir="ltr" class="dbtable">

| name | seq |
|:---:|:---:|
| Notices | 3 |

</figure>

**ש9.** ההודעה החדשה קיבלה **`4`**, ו‑`3` **נשאר חור לנצח**.

<figure dir="ltr" class="dbtable">

| NoticeId | Title | Posted |
|:---:|:---:|:---:|
| 1 | אספת הורים | 2026-09-21 |
| 2 | טיול שנתי | 2026-09-21 |
| 4 | הודעה חדשה | 2026-09-21 |

</figure>

**לא, זה לא באג — זו הגדרה.** המחולל שומר את המספר **האחרון שחולק** (`seq = 4` עכשיו), ולא בודק מה קיים בטבלה. גם באורקל `SEQUENCE` מתנהג כך, וגם הוא משאיר חורים — אחרי `ROLLBACK`, אחרי מחיקה, או אחרי קריסה.

**ולמה זה דווקא טוב?** כי אם המחולל היה "ממלא חורים", הוא היה צריך **לבדוק את הטבלה** בכל הכנסה — וכל מי שמכניס שורה היה צריך לחכות בתור. חורים הם המחיר של מהירות ושל עבודה במקביל.

**המסקנה המעשית, והיא החשובה:** מזהה אוטומטי הוא **מזהה, לא מונה**. אל תסיקו מ‑`NoticeId = 100` ש"יש 100 הודעות" — לזה יש `COUNT(*)`. ואל תבנו עליו שום לוגיקה עסקית ("מספר קבלה רצוף"), כי רצף הוא לא מה שהוא מבטיח.

**ש10.** **שתי העמודות זהות** — שתיהן מחזירות 1001, 1002, 1003.

<figure dir="ltr" class="dbtable">

| StudentId | StudentId | FirstName |
|:---:|:---:|:---:|
| 1001 | 1001 | אדם |
| 1002 | 1002 | נור |
| 1003 | 1003 | יואב |

</figure>

⚠️ ושימו לב לכותרות: ביקשנו `rowid` וקיבלנו עמודה בשם **`StudentId`** — פעמיים. זו לא טעות בהעתקה: SQLite יודע שהשתיים הן אותה עמודה, ומדווח על שם העמודה האמיתי.

לכל טבלה ב‑SQLite יש עמודה נסתרת `rowid` — מזהה פיזי של השורה. וכשמגדירים עמודה **בדיוק** בצורה `INTEGER PRIMARY KEY`, היא אינה עמודה נוספת: היא הופכת ל‑**כינוי ל‑`rowid`**. לכן אין כאן כפילות ולא בזבוז מקום, והחיפוש לפי `StudentId` הוא מהיר ביותר שאפשר — הוא חיפוש לפי המזהה הפיזי.

> 🔎 דקדוק שחשוב: `INTEGER PRIMARY KEY` הופך ל‑`rowid`; `INT PRIMARY KEY` **לא**. אותו טיפוס לכל דבר אחר, התנהגות שונה לגמרי כאן.

**ש11.** הכלי הוא **`View`**: `CREATE VIEW Pupils AS SELECT * FROM Students;` — ו‑`COUNT(*)` מחזיר 18.

**מה ההבדל מסינונים אמיתי?**

| | `SYNONYM` (אורקל) | `VIEW` כתחליף |
|---|--------------------|----------------|
| מה הוא | **שם** נוסף לאובייקט. אין בו שאילתה | שאילתה שמורה |
| `INSERT`/`UPDATE` דרכו | עובד — הוא שקוף לגמרי | תלוי במגבלות `View` (ובSQLite: אסור) |
| למה הוא קיים | שלא יצטרכו לכתוב `HR.EMPLOYEES` אלא `EMPLOYEES` · ולהחליף אובייקט מתחת למשתמשים בלי לשנות את הקוד שלהם | — |

כלומר סינונים הוא **הפניה**, ו‑`View` הוא **הגדרה**. לקריאה הם מרגישים זהים; לכתיבה ולביצועים — לא.

**ש12.** האינדקס **כן נבחר**: `SEARCH Students USING INDEX idx_students_gender (Gender=?)`.

**ובכל זאת זה אינדקס מיותר, משתי סיבות:**

**(א) סלקטיביות.** בעמודה `Gender` יש **שני ערכים אפשריים**. `WHERE Gender = 'F'` מתאים ל‑9 שורות מתוך 18 — **חצי מהטבלה**. אינדקס עוזר כשהוא מצמצם מהרבה למעט; כאן הוא מצמצם מ‑18 ל‑9, ואז בכל אחת מה‑9 צריך בכל זאת לקפוץ לשורה עצמה. על טבלה גדולה זה בדרך כלל **איטי יותר** מסתם לקרוא את הטבלה ברצף, ומנוע שאילתות חכם יתעלם מהאינדקס כזה. (על 18 שורות אין משמעות, ולכן SQLite בחר בו כאן.)

**(ב) מחיר הכתיבה.** אינדקס הוא מבנה נוסף שצריך **לעדכן בכל `INSERT`, `UPDATE` ו‑`DELETE`**. חמישה אינדקסים על טבלה = כל הכנסת שורה כותבת שש פעמים. אינדקסים אינם חינם — הם **מחליפים** מהירות קריאה במהירות כתיבה ובמקום בדיסק.

**הכלל:** צרו אינדקס על עמודה ש(1) מופיעה הרבה ב‑`WHERE` או ב‑`JOIN`, ו‑(2) יש בה **הרבה ערכים שונים** — מזהים, שמות משפחה, תאריכים. לא על `Gender`, לא על `Excused`, ולא על עמודת סטטוס עם שלושה ערכים.

</div>
<!-- classroom:end -->
