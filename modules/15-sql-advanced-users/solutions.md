<div dir="rtl">

# מודול 30 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא ניסיתם בעצמכם — [חזרו לתרגילים](exercises.md).

---

## ✅ תרגיל 1 — מי צריך מה

| המשתמש | אובייקט | הרשאות |
|---------|---------|---------|
| מנהלת | כל הטבלאות | כולן (בעלת הסכמה) |
| וטרינר | `animal` | `SELECT`, `UPDATE (weight_kg, status)` |
| | `vaccination`, `treatment` | `SELECT`, `INSERT` |
| | `vaccine_type` | `SELECT` |
| מתנדבת | `available_animal` (View) | `SELECT` |
| | `public_person` (View) | `SELECT` |
| | `walk` | `INSERT` |
| רואה חשבון | `expense`, `donation` | `SELECT` |
| | View על `adoption` בלי שמות | `SELECT` |
| האתר | `available_animal` (View) | `SELECT` — **ותו לא** |

> 💡 **שימו לב: אף אחד חוץ מהמנהלת לא מקבל `DELETE`.** חיה שמתה — `UPDATE status` (מחיקה רכה, מודול 25). ורואה החשבון רק **קורא** — הוא לא אמור לשנות את מה שהוא מבקר.

---

## ✅ תרגיל 2 — GRANT ו‑REVOKE

</div>

```sql
-- a
CREATE USER tamar IDENTIFIED BY "Tam@r2026!";
GRANT CREATE SESSION TO tamar;

-- b
GRANT SELECT ON shelter.species TO tamar;

-- c
GRANT SELECT                    ON shelter.animal      TO dr_maya;
GRANT SELECT, INSERT            ON shelter.vaccination TO dr_maya;
GRANT UPDATE (weight_kg, status) ON shelter.animal     TO dr_maya;

-- d
ALTER USER tamar ACCOUNT LOCK;
```

<div dir="rtl">

**ד. `ACCOUNT LOCK`.** `DROP USER` מוחק את המשתמש — ואם יש רישומים שמזכירים אותו (מי הכניס איזה חיסון, יומני ביקורת), הקשר אובד. נעילה מונעת כניסה, ושומרת את ההיסטוריה. ואם תמר חוזרת בעוד שנה — `ACCOUNT UNLOCK`.

**ה.** נועה יכולה לתת את הגישה ל‑`person` — כולל טלפונים — **לכל** משתמש אחר, בלי שמנהלת המערכת תדע. השליטה על מי רואה מידע אישי יוצאת מהידיים. **ובכלל — מתנדבת לא צריכה `person`, רק `public_person`.**

---

## ✅ תרגיל 3 — Roles ו‑Views

</div>

```sql
-- a
CREATE ROLE vet_role;
GRANT CREATE SESSION            TO vet_role;
GRANT SELECT          ON shelter.animal       TO vet_role;
GRANT SELECT, INSERT  ON shelter.vaccination  TO vet_role;
GRANT SELECT          ON shelter.vaccine_type TO vet_role;
GRANT vet_role TO dr_ron;
GRANT vet_role TO dr_maya;

-- b   two commands: create the user, give the role
CREATE USER dr_lina IDENTIFIED BY "L1na!Vet2026";
GRANT vet_role TO dr_lina;

-- c
CREATE VIEW adoption_finance AS
SELECT adoption_id, adoption_date, fee_paid          -- no adopter_id, no names
FROM   adoption;

CREATE ROLE accountant_role;
GRANT CREATE SESSION                     TO accountant_role;
GRANT SELECT ON shelter.adoption_finance TO accountant_role;
GRANT SELECT ON shelter.expense          TO accountant_role;
```

<div dir="rtl">

**ד.** `ORA-00942: table or view does not exist`. ל‑`volunteer_role` אין שום הרשאה על `person` — ו‑Oracle **לא מאשר אפילו שהטבלה קיימת** למי שאין לו גישה אליה. זה מכוון: הודעת "אין לך הרשאה" הייתה מגלה לתוקף "יש כאן טבלה בשם person, שווה לנסות". "לא קיימת" — לא מגלה כלום.

---

## ✅ תרגיל 4 — GLOB

</div>

```sql
-- a   Bella, Bunny, Charlie, Coco, Daisy, Felix, Kiwi, Lily, Luna, Max, Mitzi
SELECT name FROM animal WHERE name GLOB '[A-M]*' ORDER BY name;

-- b   Rocky, Lily, Daisy, Bunny
SELECT name FROM animal WHERE name GLOB '*y';

-- c   Simba, Rocky, Mitzi, Bella, Oscar, Daisy, Felix, Bunny
SELECT name FROM animal WHERE name GLOB '?????';

-- d   German Shepherd
SELECT DISTINCT breed FROM animal WHERE breed GLOB '* *';

-- e   the four "dry food, 20 sacks"
SELECT description FROM expense WHERE description GLOB '*[0-9]*';

-- f
SELECT name FROM animal WHERE name LIKE 'l%';      -- Luna, Lily
SELECT name FROM animal WHERE name GLOB 'l*';      -- (no rows)
```

<div dir="rtl">

**ו.** `LIKE` ב‑SQLite **לא רגיש** לאותיות גדולות/קטנות (עבור אותיות לטיניות) — `'l%'` מוצא את `Luna`. `GLOB` **רגיש** — `'l*'` מחפש שם שמתחיל ב‑`l` קטנה, ואין כזה.

---

## ✅ תרגיל 5 — תבניות לבדיקת נתונים

</div>

```sql
-- a   only Omer (phone is NULL)
SELECT first_name, phone
FROM   person
WHERE  phone IS NULL
   OR  phone NOT GLOB '05[0-9]-[0-9][0-9][0-9][0-9][0-9][0-9][0-9]';

-- b   (no rows) -- all 13 chips are valid
SELECT name, chip_number
FROM   animal
WHERE  chip_number NOT GLOB '985[0-9][0-9][0-9][0-9][0-9][0-9]';
```

<div dir="rtl">

> ⚠️ **בסעיף א' — `phone IS NULL OR`** חשוב: `NULL NOT GLOB …` הוא "לא ידוע", לא true — בלי ה‑`OR`, Omer לא היה מופיע. (אותה מלכודת כמו `NOT IN` במודול 24.) בסעיף ב' זה בכוונה לא נכלל — חיה בלי שבב היא לא "שבב לא תקין".

</div>

```sql
-- c   Oracle
--   ^[0-9]{4}-[0-9]{2}-[0-9]{2}$          the shape  YYYY-MM-DD
--   better: month 01-12, day 01-31
--   ^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$
ALTER TABLE animal ADD CONSTRAINT chk_birth_date_format
  CHECK (birth_date IS NULL
         OR REGEXP_LIKE(birth_date, '^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'));
-- (in real Oracle, birth_date would be a DATE column -- and then no regex is needed)

-- d   Oracle
SELECT first_name, REGEXP_REPLACE(phone, '[^0-9]', '') AS digits FROM person;
-- 052-1111111 -> 0521111111
```

<div dir="rtl">

> 💡 **שימו לב ל‑`(0[1-9]|1[0-2])`** — "0 ואחריו 1–9, **או** 1 ואחריו 0–2". זה החודשים 01–12. Regex יודע לתאר את הצורה, לא את המשמעות: `2023-02-31` עדיין יעבור. לכן — טיפוס `DATE` אמיתי, כשיש.

---

## ✅ תרגיל 6 — חיפוש עבודה

אין תשובה אחת. **דוגמה לסעיף ב':**

> *"תכננתי ובניתי בסיס נתונים למקלט בעלי חיים: ERD של 8 ישויות, נרמול לצורה נורמלית שלישית, ומימוש ב‑SQLite עם מפתחות זרים, אילוצי CHECK ו‑Views. כתבתי שאילתות דוחות (JOIN, GROUP BY, תתי‑שאילתות) שעונות על שאלות של הנהלת המקלט — כמו עלות ממוצעת לחיה וחיסונים שעבר מועדם. הקוד והתיעוד ב‑GitHub: …"*

**מה עושה אותה טובה:** מספרים (8 ישויות), מונחים מקצועיים שמעסיקים מחפשים (ERD, נרמול, JOIN, Views), **תוצאה עסקית** (מה השאילתות עונות), וקישור.

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
SELECT Students.FirstName, Students.LastName FROM Students WHERE Students.LastName LIKE 'כ%';
SELECT Students.FirstName, Students.LastName FROM Students WHERE Students.LastName GLOB 'כ*';

-- ש2
SELECT Students.FirstName, Students.Phone FROM Students WHERE Students.Phone GLOB '05[024]-*';

-- ש3
SELECT Students.FirstName, Students.Phone FROM Students
WHERE  Students.Phone GLOB '[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9][0-9]';

-- ש4
SELECT Students.FirstName FROM Students WHERE Students.FirstName LIKE '___';

-- ש5
SELECT Students.FirstName, Students.LastName FROM Students WHERE Students.FirstName GLOB '*''*';

-- ש6
SELECT Teachers.LastName FROM Teachers WHERE Teachers.LastName GLOB '*-*';

-- ש7
SELECT Absences.AbsenceId, Absences.AbsenceDate FROM Absences
WHERE  Absences.AbsenceDate NOT GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]';

-- ש8
SELECT Students.FirstName, Students.Phone FROM Students WHERE Students.Phone NOT LIKE '05%';
SELECT COUNT(*) AS n FROM Students WHERE Students.Phone NOT LIKE '05%' OR Students.Phone IS NULL;

-- ש9
SELECT Courses.CourseName FROM Courses WHERE Courses.CourseName LIKE '%יח"ל%';

-- ש10
SELECT Courses.CourseName FROM Courses WHERE Courses.CourseName GLOB '*[0-9]*';
```

<div dir="rtl">

**ש1.** **אותן 2 שורות בשתי הגרסאות** — יואב ושירה כהן.

<figure dir="ltr" class="dbtable">

| FirstName | LastName |
|:---:|:---:|
| יואב | כהן |
| שירה | כהן |

</figure>

**ההבדל בין השניים:**

| | `LIKE` | `GLOB` |
|---|--------|--------|
| "אפס תווים או יותר" | `%` | `*` |
| "תו אחד בדיוק" | `_` | `?` |
| מחלקת תווים (`[0-9]`, `[אב]`) | **אין** | **יש** |
| אותיות גדולות/קטנות | **מתעלם** (`'A' LIKE 'a'` = אמת) | **רגיש** (`'A' GLOB 'a'` = שקר) |
| תקן | **SQL תקני** — יש בכל בסיס נתונים | **ייחודי ל‑SQLite** |

כלומר `GLOB` הוא הצעד של SQLite לכיוון ביטויים רגולריים: הוא נותן מחלקות תווים, שזה בדיוק מה שחסר ב‑`LIKE`. ⚠️ **בבחינה כותבים `LIKE`** — `GLOB` לא קיים באורקל. באורקל הכלי המקביל והחזק יותר הוא `REGEXP_LIKE`.

**ש2.** **10 תלמידים.** `[024]` = "אחד מהתווים האלה, בדיוק אחד". שימו לב שזה **לא** `[0-4]` — זו רשימה, לא טווח.

<figure dir="ltr" class="dbtable">

| FirstName | Phone |
|:---:|:---:|
| אדם | 050-1000001 |
| יואב | 052-1000003 |
| מאיה | 054-1000004 |
| סאלי | 050-1000006 |
| שירה | 050-1000008 |
| תמר | 052-1000010 |
| ליאור | 050-1000011 |
| דניאל | 054-1000013 |
| הדיל | 050-1000014 |
| נועם | 050-1000017 |

</figure>

> 🔎 עומר (053) וראניה (053) **לא** ברשימה — 3 אינו ב‑`[024]`. זו בדיוק המטרה של מחלקת תווים: לבחור במדויק.

**ש3.** **12 מתוך 18.** החסרים הם **ששת התלמידים שאין להם טלפון בכלל** — `NULL GLOB '…'` הוא `NULL`, לא "שקר", ולכן הם נושרים.

<figure dir="ltr" class="dbtable">

| Valid |
|:---:|
| 12 |

</figure>

וזו **בדיקת איכות נתונים** אמיתית: 12 תקינים + 6 חסרים = 18, כלומר **אין אף טלפון בפורמט שגוי**. אם היינו מקבלים 11, היה לנו תלמיד אחד עם טלפון מקולקל — וזו שאילתה שכדאי להריץ אחרי כל ייבוא נתונים.

**ש4.** **3 תלמידים:** אדם, נור, תמר. `_` הוא "תו אחד בדיוק", ושלושה קווים תחתונים = שלושה תווים, לא פחות ולא יותר.

<figure dir="ltr" class="dbtable">

| FirstName |
|:---:|
| אדם |
| נור |
| תמר |

</figure>

**ש5.** **ג'וד מנסור.** גרש בתוך מחרוזת כותבים **פעמיים**: `'*''*'`. הראשון "בורח" מהשני, וSQL מבין שזה תו ולא סוף המחרוזת. זה הכלל בכל בסיסי הנתונים, והוא תופס גם ב‑`INSERT`: `'ג''וד'`.

<figure dir="ltr" class="dbtable">

| FirstName | LastName |
|:---:|:---:|
| ג'וד | מנסור |

</figure>

**ש6.** **רונית בר‑לב וסמיר אבו‑ראס.**

<figure dir="ltr" class="dbtable">

| LastName |
|:---:|
| בר-לב |
| אבו-ראס |

</figure>

**ש7.** **0 שורות.**

<figure dir="ltr" class="dbtable">

| AbsenceId | AbsenceDate |
|:---:|:---:|

</figure>

**ולמה זו תשובה טובה?** כי השאלה הייתה "מצא את השגויים", והתשובה היא "אין". **כל 16 התאריכים בפורמט התקני.**

זה הדפוס שנקרא **שאילתת חריגות** (exception query): מנסחים אותה כך שתוצאה **ריקה** היא הצלחה. זה הפוך מהאינטואיציה, וזו הדרך הנכונה לבדוק תקינות — כי "כל התאריכים תקינים" דורש לקרוא 16 שורות ולהאמין לעצמך, ואילו "אין תאריכים שגויים" היא תשובה שאפשר להסתכל עליה בשנייה. על מיליון שורות, זה כל ההבדל.

**ש8.** **לא, זה בכלל לא אומר את זה.** השאילתה השנייה מחזירה **6**.

| השאילתה | התוצאה |
|----------|---------|
| `WHERE Phone NOT LIKE '05%'` | **0** |
| `WHERE Phone NOT LIKE '05%' OR Phone IS NULL` | **6** |

**ההסבר:** `NULL NOT LIKE '05%'` אינו "אמת" — הוא **`NULL`**. ו‑`WHERE` זורק כל מה שאינו אמת. לכן ששת התלמידים בלי טלפון **לא הופיעו בשתי השאילתות**: לא בזו שמחפשת "מתחיל ב‑05", ולא בזו שמחפשת "לא מתחיל ב‑05".

**וזו הסכנה:** 0 שורות **נראה** כמו "הכול תקין". אבל "0 תלמידים עם טלפון שגוי" ו"0 תלמידים שהטלפון שלהם לא נבדק" הם שני דברים שונים לגמרי, ובשאילתה הראשונה הם נראים זהים.

**הכלל:** בכל `NOT LIKE`, `NOT IN` או `<>` על עמודה שיכולה להיות `NULL` — שאלו את עצמכם **מה קורה ל‑`NULL`ים**, והוסיפו `OR … IS NULL` במפורש אם הם צריכים להיכלל.

**ש9.** **3 מקצועות.** המירכאות הכפולות **לא מפריעות**: בתוך מחרוזת של SQL (שמוגדרת בגרשיים **בודדים**) מירכאה כפולה היא תו רגיל לכל דבר. רק הגרש הבודד צריך הכפלה (ש5).

<figure dir="ltr" class="dbtable">

| CourseName |
|:---:|
| מתמטיקה 5 יח"ל |
| אנגלית 4 יח"ל |
| מתמטיקה 3 יח"ל |

</figure>

**ש10.** **אותם 3 מקצועות** — דרך אחרת לאותה תשובה. `'*[0-9]*'` = "משהו, ספרה, משהו". זה יתר כללי: הוא יתפוס גם `כימיה 2 יח"ל` וגם `שיעור 7`, ואילו ש9 תפס רק `יח"ל`.

**ש11.** טבלת ההרשאות:

| המשתמש | על מה | איזו הרשאה |
|---------|--------|-------------|
| **מזכירות** | `Students` · `Classes` | `SELECT`, `INSERT`, `UPDATE` — **לא `DELETE`** (ראו ש12ד) |
| **מורה מקצועי** | `Grades` · `View` של התלמידים שלו | `SELECT`, `INSERT`, `UPDATE` על `Grades` |
| **מחנך** | **`View` בלבד** | `SELECT` |
| **תלמיד** | **`View` בלבד** | `SELECT` |

**השניים שחייבים `View`: המחנך והתלמיד** — ומסיבה אחת משותפת: שניהם צריכים לראות **חלק מהשורות**, לא חלק מהעמודות.

הרשאות ב‑SQL עובדות על **אובייקטים**, לא על שורות: אפשר לומר "מותר לך לקרוא את `Grades`" או "אסור לך", אבל אין `GRANT SELECT ON Grades WHERE StudentId = 1001`. אפשר להגביל עמודות (ש12ג), אבל לא שורות.

הפתרון הוא להעביר את תנאי השורות **לתוך** `View`, ולתת הרשאה עליו:

</div>

```sql
CREATE VIEW MyClassGrades AS
SELECT s.FirstName, s.LastName, c.CourseName, g.Grade, g.Term
FROM   Grades g, Students s, Classes cl, Courses c
WHERE  g.StudentId = s.StudentId
  AND  s.ClassCode = cl.ClassCode
  AND  g.CourseCode = c.CourseCode
  AND  cl.TeacherCode = <המחנך המחובר>;      -- באורקל: USER / SYS_CONTEXT

GRANT SELECT ON MyClassGrades TO homeroom_role;
```

<div dir="rtl">

המחנך מקבל גישה ל‑`View` **ולא** ל‑`Grades`. אם ינסה `SELECT * FROM Grades` — שגיאת הרשאה. התנאי "רק הכיתה שלי" לא נסמך על כך שהוא לא ינסה; הוא **לא קיים** מבחינתו. (באורקל זו התבנית הקלאסית של Virtual Private Database.)

**ש12.** פקודות ה‑`GRANT` (תחביר אורקל — לא רץ ב‑SQLite):

</div>

```sql
-- א.  מזכירות
GRANT SELECT, INSERT, UPDATE ON Students TO secretary;

-- ב.  כל המורים — על ה-View, לא על הטבלה
GRANT SELECT ON PublicTeachers TO teacher_role;

-- ג.  חוסאם — עדכון עמודה אחת בלבד
GRANT UPDATE (Grade) ON Grades TO husam;

-- ד.  ביטול
REVOKE DELETE ON Students FROM secretary;

-- ה.  תפקיד במקום 40 משתמשים
CREATE ROLE teacher_role;
GRANT SELECT ON PublicTeachers TO teacher_role;
GRANT SELECT, INSERT, UPDATE ON Grades TO teacher_role;
GRANT teacher_role TO husam, orly, nabil;      -- ... וכל 40
```

<div dir="rtl">

**ש12ב — היתרון של `GRANT` על ה‑`View`:** `PublicTeachers` לא מכיל את `Salary` ואת `Phone`. מורה שמסתכל עליו **לא יכול** לראות את שכר חבריו — לא כי הוא הוגן, אלא כי העמודה לא קיימת בשבילו. `GRANT SELECT ON Teachers` היה חושף את טבלת השכר של כל הסגל לכל הסגל.

**ש12ג — `UPDATE` על עמודה:** זו ההוכחה שהרשאות יורדות לרזולוציית **עמודה**. חוסאם יכול לשנות ציון, אבל לא את `StudentId` ולא את `Term` — כלומר הוא לא יכול "להעביר" ציון מתלמיד לתלמיד.

**ש12ד — למה דווקא `DELETE`:** זו ההרשאה שהנזק ממנה בלתי הפיך. מזכירות צריכה **לרשום ולעדכן**; תלמיד שעוזב אינו מקרה של מחיקה אלא של סימון (`Status = 'left'`), כי הציונים וההיסטוריה שלו חייבים להישאר. זה הכלל שנקרא **הרשאות מינימום** (least privilege): נותנים את מה שנדרש לעבודה, לא את מה שאולי יהיה נוח.

**ש12ה — הבעיה ב‑40 `GRANT`‑ים והפתרון:**

| הבעיה | מה קורה |
|--------|----------|
| **תחזוקה** | מורה חדש = לזכור את כל ההרשאות. אחת תישכח, והוא "לא רואה ציונים" ביום הראשון |
| **שינוי מדיניות** | הוחלט לפתוח למורים גם את `Absences`? **40 פקודות**, וקל לפספס |
| **ביקורת** | "מי יכול לעדכן ציונים?" — צריך לעבור על 40 משתמשים ולאחד את הרשימות |
| **עזיבה** | מורה עוזב — למחוק 6 הרשאות במקום אחת |

**הפתרון: `ROLE`** — "תפקיד". מגדירים **אוסף הרשאות** בשם אחד, נותנים את התפקיד למשתמשים, ומכאן:

- מורה חדש → `GRANT teacher_role TO dana;` — שורה אחת
- שינוי מדיניות → `GRANT SELECT ON Absences TO teacher_role;` — שורה אחת, ו**כל 40 מקבלים מיד**
- ביקורת → ההרשאות מתועדות במקום אחד, ולא מפוזרות על 40 משתמשים

זה בדיוק אותו עקרון של `View` משיעור 28, רק בצד השני: **`View` מרכז את "אילו נתונים", ו‑`ROLE` מרכז את "מי מורשה".** שניהם נותנים מקום **אחד** לשנות דבר שחל על הרבה.

> 💡 **וכשתגיעו לראיון עבודה** — זו שאלה שנשאלת. "איך היית מנהל הרשאות ל‑40 משתמשים?" התשובה "`ROLE`, ו‑`View` לסינון שורות" היא התשובה שמחפשים.

</div>
<!-- classroom:end -->
