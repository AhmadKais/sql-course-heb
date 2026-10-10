<div dir="rtl">

# מודול 27 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 הפלטים אמיתיים, מהרצה ב‑SQLite אחרי `shelter.sql` ו‑`PRAGMA foreign_keys = ON;`.

---

## ✅ תרגיל 1 — לזהות אילוצים

**א.** **`NOT NULL`:** `name` (לכל חיה יש שם), `species_id` (כל חיה ממין כלשהו), `sex` (גם "לא ידוע" הוא ערך — `'U'`), `status`. **מותר NULL:** `breed` (חיה מעורבת / לא ידוע), `birth_date` (משוטטת — לא יודעים מתי נולדה), `chip_number` (לא לכל חיה יש שבב), `weight_kg`.

**ב.** `sex TEXT NOT NULL CHECK (sex IN ('M','F','U'))` — מין רק מתוך שלושה ערכים.

**ג.** `species.name UNIQUE` (אין שני מינים בשם "Dog"), `animal.chip_number UNIQUE` (שבב אחד = חיה אחת).

**ד.** `animal.status` — אין `CHECK`, אז אפשר להכניס `'adoptd'` (שגיאת כתיב) או `'Adopted'`, וכל שאילתה עם `WHERE status = 'adopted'` תפספס אותם. אותו דבר ל‑`person.role`, `intake.intake_type` ו‑`expense.category`.

---

## ✅ תרגיל 2 — UNIQUE ו‑NULL

**א.** **שתיהן נכנסו.** NULL = "לא ידוע", ושני "לא ידוע" אינם בהכרח שווים — אז אין הפרה של ייחודיות.

**ב.** `UNIQUE constraint failed: contact.email`.

**ג.** אותו עיקרון: 7 ה‑NULL‑ים לא "מתנגשים" זה בזה. `UNIQUE` אוכף ייחודיות **רק בין ערכים שקיימים**. בדיוק מה שהמקלט צריך: לחיה בלי שבב — אין בעיה; שתי חיות עם **אותו** שבב — טעות.

---

## ✅ תרגיל 3 — CHECK

**א.**

</div>

```text
UNIQUE constraint failed: kennel.code
CHECK constraint failed: chk_kennel_size
CHECK constraint failed: chk_kennel_cap
```

```sql
-- b
CREATE TABLE w (weight_kg REAL CHECK (weight_kg > 0));
INSERT INTO w VALUES (NULL);      -- accepted
INSERT INTO w VALUES (-1);        -- CHECK constraint failed: weight_kg > 0
SELECT COUNT(*) FROM w;           -- 1
```

<div dir="rtl">

**ב.** `NULL > 0` הוא "לא ידוע" — ו‑`CHECK` **נכשל רק כשהתנאי false**. "לא ידוע" עובר. כדי לחסום גם NULL — `NOT NULL` בנוסף.

</div>

```sql
-- c
CREATE TABLE expense_v2 (
  expense_id INTEGER PRIMARY KEY,
  animal_id  INTEGER REFERENCES animal(animal_id),
  category   TEXT NOT NULL,
  amount     REAL NOT NULL,
  CONSTRAINT chk_medical_animal CHECK (category <> 'medical' OR animal_id IS NOT NULL)
);
INSERT INTO expense_v2 VALUES (1, NULL, 'food',    100);    -- OK
INSERT INTO expense_v2 VALUES (2, NULL, 'medical', 200);    -- CHECK constraint failed
```

<div dir="rtl">

> 💡 **איך קוראים `A OR B` כחוק:** "**או** שזו לא הוצאה רפואית, **או** שיש חיה" = "אם רפואית — אז יש חיה". זה התרגום הקבוע של "אם … אז …" ל‑`CHECK`.

**ד.** קודם בודקים מה קיים (מודול 24):

</div>

```sql
SELECT status FROM animal GROUP BY status;
-- adopted, available, deceased, medical, quarantine  -- all five, nothing else

CONSTRAINT chk_status CHECK (status IN ('available', 'adopted', 'medical', 'quarantine', 'deceased'))
```

<div dir="rtl">

ב‑SQLite אי אפשר `ALTER TABLE … ADD CONSTRAINT` — בונים טבלה חדשה ומעתיקים (`INSERT INTO animal_v2 SELECT … FROM animal` — כל 20 השורות עברו). ב‑Oracle: `ALTER TABLE animal ADD CONSTRAINT chk_status CHECK (…)` — ואם שורה קיימת מפרה את החוק, ה‑`ALTER` ייכשל.

---

## ✅ תרגיל 4 — מפתחות

**א.** `UNIQUE constraint failed: kennel_stay.animal_id, kennel_stay.from_date` — **"חיה לא מתחילה שתי שהיות באותו יום"**. המפתח הראשי המורכב הוא החוק.

**ב.** `CHECK constraint failed: chk_stay_dates`.

**ג.** **הצליח — 28 שורות.** אין בנתונים אף חיסון כפול (אותה חיה, אותו חיסון, אותו יום). אילו היה — כל ההעתקה הייתה נכשלת.

**ד.** `'2023-05-25'` ⟵ `UNIQUE constraint failed: v2.animal_id, v2.vaccine_type_id, v2.given_date`. `'2023-05-26'` ⟵ **נכנס** — יום אחר, צירוף אחר. (אם זה הגיוני רפואית — זו כבר שאלה ל‑`CHECK` אחר, או לווטרינר.)

---

## ✅ תרגיל 5 — מה קורה במחיקה

**ב.** הכלוב נמחק; השהייה של Rocky **נשארת**, עם `kennel_id` = NULL (`SET NULL`).

**ג.** קודם מוחקים את החיסונים והקליטות של Bunny — כי ל‑`vaccination` ול‑`intake` **אין** `CASCADE`, והם חוסמים. אחרי מחיקת Bunny — השהייה שלה **נמחקה אוטומטית** (`CASCADE`).

</div>

```text
animal_id  kennel_id  from_date
---------  ---------  ----------
3                     2023-05-20      <- only Rocky's stay is left
```

<div dir="rtl">

**ד.** אימוץ הוא **רשומה היסטורית וכספית** — מי אימץ, מתי, כמה שילם. אם חיה נמחקת בטעות, `CASCADE` ימחק גם את רישום התשלום, ודוח ההכנסות ישתנה בדיעבד. כאן **רוצים שהמחיקה תיחסם** — ובעצם לא למחוק חיות בכלל (מחיקה רכה, מודול 25).

---

## ✅ תרגיל 6 — קשת

**א.** רק התשלום הראשון (אימוץ 5 בלבד) נכנס. "גם וגם" ו"אף אחד" ⟵ `CHECK constraint failed: chk_arc`.

</div>

```sql
-- b
CONSTRAINT chk_intake_kind CHECK (
     (intake_type = 'stray'     AND location IS NOT NULL AND reason IS NULL)
  OR (intake_type = 'surrender' AND location IS NULL     AND reason IS NOT NULL)
  OR (intake_type = 'transfer'  AND location IS NULL)
)
```

<div dir="rtl">

בדיקה — שאילתה על הנתונים הקיימים:

</div>

```sql
SELECT intake_type, COUNT(*) AS total,
       SUM(location IS NOT NULL) AS has_location,
       SUM(reason   IS NOT NULL) AS has_reason
FROM   intake GROUP BY intake_type;
```

```text
intake_type  total  has_location  has_reason
-----------  -----  ------------  ----------
stray        11     11            0
surrender    8      0             8
transfer     2      0             2
```

<div dir="rtl">

כל 21 השורות עומדות בחוק (העתקה לטבלה עם האילוץ — הצליחה). קליטה `stray` בלי מיקום ועם סיבה ⟵ `CHECK constraint failed: chk_intake_kind`.

> 🔑 **זה טיפוסי משנה (מודול 4) בטבלה אחת**, ו‑`CHECK` הוא מה שמוודא שכל שורה "מתנהגת" לפי הטיפוס שלה.

---

## ✅ תרגיל 7 — הפרויקט שלכם

אין פתרון אחד. **דוגמה לטבלת "חוק ⟵ אילוץ":**

| החוק העסקי | האילוץ |
|-------------|---------|
| לכל לקוח מספר טלפון | `phone TEXT NOT NULL` |
| אין שני לקוחות עם אותו email | `CONSTRAINT uq_customer_email UNIQUE (email)` |
| הזמנה שייכת ללקוח קיים | `CONSTRAINT fk_order_customer FOREIGN KEY …` |
| כמות בהזמנה — לפחות 1 | `CONSTRAINT chk_item_qty CHECK (qty >= 1)` |
| לא יותר מ‑10 הזמנות פתוחות ללקוח | **לא ניתן ב‑`CHECK`** — דורש ספירת שורות (טריגר / אפליקציה) |

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
PRAGMA foreign_keys = ON;        -- חובה, אחרת ש6/ש7/ש12 לא ייכשלו

-- ש1
CREATE TABLE Exams (
  ExamId     INTEGER PRIMARY KEY,
  CourseCode INTEGER NOT NULL REFERENCES Courses(CourseCode),
  ExamDate   TEXT    NOT NULL,
  Room       TEXT    NOT NULL,
  MaxScore   INTEGER NOT NULL DEFAULT 100 CHECK (MaxScore BETWEEN 1 AND 100),
  Weight     REAL    NOT NULL CHECK (Weight > 0 AND Weight <= 1),
  UNIQUE (CourseCode, ExamDate)
);
INSERT INTO Exams VALUES (1, 11, '2027-01-15', 'אולם א', 100, 0.4);
INSERT INTO Exams VALUES (2, 11, '2027-06-10', 'אולם א', 100, 0.6);
INSERT INTO Exams VALUES (3, 13, '2027-01-15', 'חדר 21', 100, 1.0);

-- ש8
CREATE TABLE Lockers (LockerId INTEGER PRIMARY KEY, StudentId INTEGER UNIQUE, Floor1 INTEGER);
INSERT INTO Lockers VALUES (1, 1001, 1), (2, NULL, 1), (3, NULL, 2), (4, NULL, 2);

-- ש9
INSERT INTO Exams (ExamId, CourseCode, ExamDate, Room, Weight)
VALUES (9, 17, '2027-05-20', 'חדר 12', 0.3);

-- ש10
CREATE TABLE GradesChecked (
  StudentId  INTEGER NOT NULL REFERENCES Students(StudentId),
  CourseCode INTEGER NOT NULL REFERENCES Courses(CourseCode),
  Grade      INTEGER CHECK (Grade BETWEEN 0 AND 100),
  PRIMARY KEY (StudentId, CourseCode)
);
INSERT INTO GradesChecked VALUES (1001, 11, 88);
INSERT INTO GradesChecked VALUES (1002, 11, NULL);

-- ש12
CREATE TABLE ClubReg (
  ClubId    INTEGER NOT NULL,
  StudentId INTEGER NOT NULL REFERENCES Students(StudentId) ON DELETE CASCADE,
  PRIMARY KEY (ClubId, StudentId)
);
INSERT INTO ClubReg VALUES (1, 1007), (2, 1007), (1, 1016);
DELETE FROM Grades   WHERE StudentId = 1007;
DELETE FROM Students WHERE StudentId = 1007;
SELECT * FROM ClubReg;
```

<div dir="rtl">

**ש1.** שש עמודות, **שבעה אילוצים**. שימו לב שה‑`UNIQUE` האחרון נכתב **כאילוץ טבלה** ולא כאילוץ עמודה — כי הוא חל על **שתי** עמודות יחד. זה הכלל: אילוץ שנוגע ליותר מעמודה אחת נכתב בסוף, בשורה נפרדת.

<figure dir="ltr" class="dbtable">

| ExamId | CourseCode | ExamDate | Room | MaxScore | Weight |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 11 | 2027-01-15 | אולם א | 100 | 0.4 |
| 2 | 11 | 2027-06-10 | אולם א | 100 | 0.6 |
| 3 | 13 | 2027-01-15 | חדר 21 | 100 | 1 |

</figure>

> 🔎 שורה 3 מראה `1` ולא `1.0`. הערך נשמר כ‑`REAL`, אבל 1.0 מוצג בקיצור. אל תבלבלו את התצוגה עם הטיפוס.

**ש2.–ש6.** חמש ההודעות, וחמישה אילוצים שונים:

</div>

```text
ש2   NOT NULL constraint failed: Exams.Room
ש3   UNIQUE constraint failed: Exams.CourseCode, Exams.ExamDate
ש4   CHECK constraint failed: MaxScore BETWEEN 1 AND 100
     CHECK constraint failed: Weight > 0 AND Weight <= 1
ש5   UNIQUE constraint failed: Exams.ExamId
ש6   FOREIGN KEY constraint failed
```

<div dir="rtl">

| הסעיף | האילוץ | מה הוא שמר |
|--------|---------|-------------|
| **ש2** | `NOT NULL` | בחינה **חייבת** חדר. "לא ידוע" אינו מצב חוקי לבחינה שנקבעה |
| **ש3** | `UNIQUE (CourseCode, ExamDate)` | אין שתי בחינות באותו מקצוע באותו יום. ⚠️ הודעת השגיאה **מצטטת את שתי העמודות** — כך מזהים שזה אילוץ הטבלה ולא אילוץ עמודה |
| **ש4** | `CHECK` | 120 אינו ציון אפשרי, 1.5 אינו משקל אפשרי. `CHECK` מגדיר **תחום** (domain) שאפשר לתאר במשפט לוגי |
| **ש5** | `PRIMARY KEY` (שהוא גם `UNIQUE`) | מזהה 1 תפוס. זהו האילוץ ש"שורה אחת = ישות אחת" נשען עליו |
| **ש6** | `FOREIGN KEY` | אין מקצוע 99. בחינה למקצוע שלא קיים היא **שורה יתומה** — נתון שמצביע לשום מקום |

**ש7.** המחיקה **נכשלה**: `FOREIGN KEY constraint failed`.

מי מנע? **הבחינות 1 ו‑2, שמצביעות למקצוע 11** — וגם 15 שורות ב‑`Grades`. בסיס הנתונים מסרב למחוק "אב" שיש לו "ילדים", כי מיד לאחר המחיקה היו בטבלה שורות שמצביעות למקצוע שלא קיים. זה נקרא **שלמות התייחסותית** (Referential Integrity), והוא עובד **בשני הכיוונים**: גם `INSERT` של ילד בלי אב (ש6), וגם `DELETE` של אב עם ילדים (ש7).

**שלוש הדרכים לטפל בזה** — והבחירה היא **עסקית**, לא טכנית:

| ההתנהגות | מה קורה במחיקת אב | מתי נכון |
|-----------|---------------------|-----------|
| `ON DELETE RESTRICT` (ברירת המחדל) | הפעולה **נכשלת** | ציונים, הזמנות, כסף — "אל תיתן לי למחוק משהו שיש לו היסטוריה" |
| `ON DELETE CASCADE` | הילדים **נמחקים איתו** | רשומות שאין להן קיום בלי האב — רישום לחוג, שורות בעגלת קניות (ראו ש12) |
| `ON DELETE SET NULL` | המפתח הזר בילדים הופך `NULL` | "המקצוע בוטל, הציון נשאר רשום בלי מקצוע" |

**ש8א.** **כל ארבע השורות נכנסו** — אף ששלוש מהן `NULL` באותה עמודה `UNIQUE`.

הסיבה היא אותו כלל שפגשתם בשיעור 17: **`NULL` אינו שווה ל‑`NULL`**. `UNIQUE` אוסר **ערכים זהים**, והוא בודק את זה בהשוואה. שתי שורות עם `NULL`? ההשוואה `NULL = NULL` מחזירה "לא ידוע", לא "אמת" — ולכן אין **הוכחה** שהן זהות, ו‑`UNIQUE` מרשה את שתיהן.

**המשמעות המעשית:** `UNIQUE` **אינו** מבטיח שיש לכם ערך בכל שורה. "לכל תא יש לכל היותר תלמיד אחד" — כן. "לכל תא יש תלמיד" — **לא**. למי שצריך את השני, האילוץ הוא `UNIQUE NOT NULL`, שניהם יחד.

<figure dir="ltr" class="dbtable">

| LockerId | StudentId | Floor1 |
|:---:|:---:|:---:|
| 1 | 1001 | 1 |
| 2 | NULL | 1 |
| 3 | NULL | 2 |
| 4 | NULL | 2 |

</figure>

**ש8ב.** `UNIQUE constraint failed: Lockers.StudentId` — כאן יש **ערך אמיתי** זהה (1001), וההשוואה מחזירה "אמת". שתי שורות, אותו תא לאותו תלמיד: נחסם.

**ש9.** נכנס **100** — ברירת המחדל. **וכן, ה‑`CHECK` נבדק גם עליה.**

זו נקודה שקל לפספס: `DEFAULT` ו‑`CHECK` אינם מתחרים. `DEFAULT` **מייצר** את הערך, ואחר כך `CHECK` **בודק** אותו — בדיוק כמו כל ערך שהמשתמש היה כותב. אם היינו מגדירים `DEFAULT 150` עם `CHECK (MaxScore BETWEEN 1 AND 100)`, כל `INSERT` שמשמיט את העמודה היה נכשל. (זו בדיוק הסיבה שכדאי לבדוק את ברירות המחדל שלכם פעם אחת ידנית.)

<figure dir="ltr" class="dbtable">

| ExamId | CourseCode | MaxScore | Weight |
|:---:|:---:|:---:|:---:|
| 9 | 17 | 100 | 0.3 |

</figure>

**ש10א.** **שתי השורות עברו**, כולל זו עם `NULL`.

<figure dir="ltr" class="dbtable">

| StudentId | CourseCode | Grade |
|:---:|:---:|:---:|
| 1001 | 11 | 88 |
| 1002 | 11 | NULL |

</figure>

**איך?** `CHECK` חוסם שורה רק כשהתנאי מחזיר **שקר**. `NULL BETWEEN 0 AND 100` אינו שקר — הוא **"לא ידוע"**. ו‑`CHECK` מרשה כל מה שאינו שקר מוכח.

זה עקבי עם כל מה שלמדנו על `NULL`, וזה גם **שימושי**: הוא מאפשר בדיוק את מה שבית הספר צריך — "ציון, אם יש, חייב להיות 0–100; ו'לא נבחן' הוא מצב חוקי". אם רציתם לאסור גם את זה, מוסיפים `NOT NULL` בנפרד. `CHECK` ו‑`NOT NULL` הם שני אילוצים שונים שעושים שני דברים שונים.

**ש10ב.** `CHECK constraint failed: Grade BETWEEN 0 AND 100` — 120 הוא שקר מוכח, ולכן נחסם.

**ש11.** **זה עבר.** השורה `(1001, 13, 1, 120)` נכנסה לטבלת `Grades` האמיתית, וה‑`SELECT` מצא אותה:

<figure dir="ltr" class="dbtable">

| StudentId | CourseCode | Grade |
|:---:|:---:|:---:|
| 1001 | 13 | 120 |

</figure>

**למה?** כי **ב‑`school.sql` אין `CHECK` על `Grade`.** תסתכלו בהגדרת הטבלה: `Grade INTEGER` — וזה הכול. אין גבול תחתון, אין גבול עליון.

**ומה זה אומר על `school.sql`?** שהוא, כמו רוב בסיסי הנתונים האמיתיים, **מעוצב חלקית**. יש בו מפתחות ראשיים ומפתחות זרים, יש `CHECK` על `Gender` ועל `Excused` — ואין על `Grade`. מישהו חשב על הראשונים ולא על השלישי, וזה בדיוק מה שקורה בפרויקטים.

**המסקנה המעשית:** ציון 120 הוא לא באג בקוד שהכניס אותו — הוא באג **בעיצוב הטבלה**. אפליקציה שבודקת בעצמה "0 עד 100" מגנה רק על עצמה; מי שיתחבר לבסיס הנתונים דרך כלי אחר, סקריפט ייבוא או `INSERT` ידני, יעקוף את הבדיקה. **אילוץ בבסיס הנתונים הוא הבדיקה היחידה שאף אחד לא יכול לדלג עליה.**

**ש12.** **ב‑`ClubReg` נשארה שורה אחת** — `(1, 1016)`. שתי השורות של 1007 **נמחקו מעצמן**.

<figure dir="ltr" class="dbtable">

| ClubId | StudentId |
|:---:|:---:|
| 1 | 1016 |

</figure>

**ובמה זה שונה מש7?** בהגדרה, ובה בלבד:

</div>

```text
Exams.CourseCode  REFERENCES Courses(CourseCode)                      -- ברירת מחדל = RESTRICT
                  ->  מחיקת מקצוע 11  =  שגיאה

ClubReg.StudentId REFERENCES Students(StudentId) ON DELETE CASCADE
                  ->  מחיקת תלמיד 1007  =  הרישומים שלו נמחקים אוטומטית
```

<div dir="rtl">

שימו לב שגם כאן נדרשה מחיקה ידנית של ה**ציונים** של 1007 — כי `Grades` מוגדר ב‑`school.sql` **בלי** `CASCADE`. באותו בסיס נתונים, עם אותו תלמיד, יש **שתי התנהגויות שונות** לפי מה שכל טבלה הגדירה. זה לא חוסר עקביות: זו החלטה נכונה. רישום לחוג אין לו משמעות בלי התלמיד; **ציון יש לו**, והוא היסטוריה שאסור שתיעלם בלי ששמים לב.

> ⚠️ **`CASCADE` הוא כלי חד.** `DELETE` אחד יכול למחוק שורות בחמש טבלאות, בלי שתראו אותן ובלי שתאשרו. השתמשו בו **רק** כשהילדים חסרי משמעות בלי האב — ולא בשום מקום שיש בו כסף, ציונים או היסטוריה.

</div>
<!-- classroom:end -->
