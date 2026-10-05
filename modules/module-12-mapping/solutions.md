<div dir="rtl">

# מודול 12 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא ניסיתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 הקוד בתרגיל 4 נבדק ב‑SQLite, והפלטים אמיתיים.

---

## ✅ תרגיל 1 — מילון המונחים

| ב‑ERD | בטבלה |
|-------|--------|
| ישות | **טבלה** |
| **מופע** | שורה |
| מאפיין `o` | עמודה **שמותר בה NULL** |
| `#` | **מפתח ראשי** |
| **מזהה משני** | `UNIQUE` |
| יחס 1:M, קו רציף בצד הרבים | **מפתח זר `NOT NULL`** בצד הרבים |
| מאפיין רב‑ערכי | **טבלה נפרדת** |
| מאפיין נגזר | **לא נשמר** — מחושב בשאילתה |

---

## ✅ תרגיל 2 — לאן הולך המפתח הזר?

| | הטבלה | העמודה | NULL? |
|---|--------|---------|-------|
| א | `class` | `grade_level_id` | `NOT NULL` — כל כיתה בשכבה |
| ב | `class` | `homeroom_teacher_id` + **`UNIQUE`** | `NOT NULL` — 1:1; הצד שחובה לו |
| ג | `employee` | `manager_id` → `employee` | מותר NULL — למנכ"ל |
| ד | `"order"` | `coupon_id` | מותר NULL — "יכולה" |
| ה | `order_line` | `order_id` **בתוך ה‑pk**: `PRIMARY KEY (order_id, line_no)` | `NOT NULL` (חלק מ‑pk) |

> 💡 **ב'** — 1:1: המפתח הזר בצד שבו היחס **חובה ותמיד קיים** — לכל כיתה יש מחנך. בצד המורה זה אופציונלי (לא כל מורה מחנך), ולכן שם היו הרבה NULL‑ים. `UNIQUE` מבטיח שמורה לא יחנך שתי כיתות.

---

## ✅ תרגיל 3 — טיפוסי משנה

**א.**
- **א. טבלה אחת:** `person (person_id, name, type, grade, parent_birth_date, subject, license_no, seniority)`
- **ב. לכל משנה:** `student (id, name, grade, …)`, `teacher (id, name, subject, …)`
- **ג. על + משנים:** `person (person_id, name, type)` + `student (person_id pk/fk, grade, …)` + `teacher (person_id pk/fk, subject, …)`

**ב.**

| | מה לא נאכף |
|---|---|
| א | אי אפשר `NOT NULL` על `grade` (למורה אין) — צריך `CHECK` לפי `type` |
| ב | `LIBRARY_LOAN` ו‑`PARKING_PERMIT` לא יכולים להצביע על "אדם" במפתח זר אחד; וייחודיות מספר הזהות **בין** שתי הטבלאות |
| ג | בלעדיות — אותו `person_id` יכול להופיע גם ב‑`student` וגם ב‑`teacher` |

**ג.** **ג'** — כי שתי ישויות חיצוניות מצביעות על "אדם" (בלי לדעת מי), ולכל טיפוס משנה כמה מאפיינים ייחודיים. ובלעדיות — בודקים באפליקציה או בטריגר, ורושמים ביומן ההחלטות.

---

## ✅ תרגיל 4 — ספריית בית הספר

**א. 6 טבלאות:** `author`, `book`, `book_author` (פתרון ה‑M:M), `copy`, `member`, `loan`.

</div>

```sql
-- b
PRAGMA foreign_keys = ON;

CREATE TABLE author (
  author_id INTEGER PRIMARY KEY,
  full_name TEXT NOT NULL,
  country   TEXT
) STRICT;

CREATE TABLE book (
  book_id      INTEGER PRIMARY KEY,
  isbn         TEXT    NOT NULL,
  title        TEXT    NOT NULL,
  year_pub     INTEGER,
  prev_book_id INTEGER,                                  -- recursive, optional
  CONSTRAINT uq_book_isbn UNIQUE (isbn),
  CONSTRAINT fk_book_prev FOREIGN KEY (prev_book_id) REFERENCES book(book_id)
) STRICT;

CREATE TABLE book_author (                               -- resolved M:M
  book_id   INTEGER NOT NULL REFERENCES book(book_id),
  author_id INTEGER NOT NULL REFERENCES author(author_id),
  CONSTRAINT pk_book_author PRIMARY KEY (book_id, author_id)
) STRICT;

CREATE TABLE copy (                                      -- barred: pk includes the fk
  book_id INTEGER NOT NULL,
  copy_no INTEGER NOT NULL,
  shelf   TEXT    NOT NULL,
  CONSTRAINT pk_copy      PRIMARY KEY (book_id, copy_no),
  CONSTRAINT fk_copy_book FOREIGN KEY (book_id) REFERENCES book(book_id)
) STRICT;

-- MEMBER: option A (single table) -- only one attribute per subtype,
-- and LOAN must point to "any member"
CREATE TABLE member (
  member_id   INTEGER PRIMARY KEY,
  full_name   TEXT NOT NULL,
  id_number   TEXT,
  member_type TEXT NOT NULL CHECK (member_type IN ('student', 'teacher')),
  grade       INTEGER,
  subject     TEXT,
  CONSTRAINT uq_member_idno UNIQUE (id_number),
  CONSTRAINT chk_member_sub CHECK (
       (member_type = 'student' AND grade   IS NOT NULL AND subject IS NULL)
    OR (member_type = 'teacher' AND subject IS NOT NULL AND grade   IS NULL))
) STRICT;

CREATE TABLE loan (
  loan_id     INTEGER PRIMARY KEY,
  book_id     INTEGER NOT NULL,
  copy_no     INTEGER NOT NULL,
  member_id   INTEGER NOT NULL REFERENCES member(member_id),
  loan_date   TEXT NOT NULL,
  due_date    TEXT NOT NULL,
  return_date TEXT,
  CONSTRAINT fk_loan_copy   FOREIGN KEY (book_id, copy_no) REFERENCES copy(book_id, copy_no),
  CONSTRAINT chk_loan_dates CHECK (due_date >= loan_date)
) STRICT;
```

<div dir="rtl">

**ג.** המפתח הזר **מורכב גם הוא** — שתי עמודות שמצביעות יחד על שתי עמודות: `FOREIGN KEY (book_id, copy_no) REFERENCES copy(book_id, copy_no)`. זה המחיר של יחס מזהה: כל מי שמצביע על `copy` צריך את **שני** החלקים.

</div>

```sql
-- d
INSERT INTO author VALUES (1, 'Noa Ben-David', 'Israel'), (2, 'Yosef Haddad', 'Israel');
INSERT INTO book (book_id, isbn, title, year_pub)
VALUES (1, '978-1', 'The Carmel Summer', 2019), (2, '978-2', 'Two Cities', 2022);
INSERT INTO book_author VALUES (1, 1), (2, 1), (2, 2);
INSERT INTO copy VALUES (1, 1, 'A3'), (1, 2, 'A3'), (2, 1, 'B1');
INSERT INTO member VALUES (1, 'Dana Levi', '123', 'student', 11, NULL),
                          (2, 'Omar Khalil', '456', 'teacher', NULL, 'History');
INSERT INTO loan (book_id, copy_no, member_id, loan_date, due_date)
VALUES (1, 2, 1, '2026-09-01', '2026-09-15');

SELECT m.full_name, b.title, l.copy_no, l.due_date
FROM   loan l
JOIN   member m ON m.member_id = l.member_id
JOIN   book   b ON b.book_id   = l.book_id;
```

```text
full_name  title              copy_no  due_date
---------  -----------------  -------  ----------
Dana Levi  The Carmel Summer  2        2026-09-15
```

<div dir="rtl">

**ה.**

</div>

```text
INSERT INTO member VALUES (3, 'X', NULL, 'student', NULL, 'Math');
--> CHECK constraint failed: chk_member_sub

INSERT INTO loan (book_id, copy_no, member_id, loan_date, due_date) VALUES (2, 5, 1, ...);
--> FOREIGN KEY constraint failed          (book 2 has no copy number 5)
```

<div dir="rtl">

---

## ✅ תרגיל 5 — המקלט

</div>

```sql
-- a
CREATE TABLE vet_details (
  person_id      INTEGER PRIMARY KEY REFERENCES person(person_id),   -- 1:1
  license_number TEXT    NOT NULL UNIQUE,
  clinic_id      INTEGER REFERENCES vet_clinic(clinic_id)
);

CREATE TABLE adoption_fee_schedule (
  species_id INTEGER NOT NULL REFERENCES species(species_id),
  valid_from TEXT    NOT NULL,
  valid_to   TEXT,                                    -- NULL = the current price
  fee        REAL    NOT NULL CHECK (fee >= 0),
  CONSTRAINT pk_fee_schedule PRIMARY KEY (species_id, valid_from),
  CONSTRAINT chk_fee_period  CHECK (valid_to IS NULL OR valid_to > valid_from)
);
```

<div dir="rtl">

**א.** המפתח של המחירון: **`(species_id, valid_from)`** — לכל מין, מחיר אחד שמתחיל בכל תאריך. (אילוץ "אין חפיפה בין תקופות" — לא ניתן ב‑`CHECK`; זה עוד חוק לאפליקציה / טריגר.)

</div>

```sql
-- b
CREATE TABLE role (
  role_id INTEGER PRIMARY KEY,
  name    TEXT NOT NULL UNIQUE                  -- volunteer / adopter / vet / previous owner
);
CREATE TABLE person_role (
  person_id INTEGER NOT NULL REFERENCES person(person_id),
  role_id   INTEGER NOT NULL REFERENCES role(role_id),
  since     TEXT    NOT NULL,
  CONSTRAINT pk_person_role PRIMARY KEY (person_id, role_id)
);
```

<div dir="rtl">

**ב.** כי זה **לא** טיפוסי משנה. טיפוסי משנה הם **בלעדיים** — כל מופע בדיוק אחד. אבל אדם יכול להיות **גם** מתנדב **וגם** מאמץ. זה יחס **M:M** בין `PERSON` ל‑`ROLE` — ולכן ממופה כמו כל M:M: ישות מקשרת. **זיהוי נכון של הדפוס ב‑ERD קובע את המיפוי.**

**ג.**

</div>

```sql
INSERT INTO dog (animal_id) VALUES (1);
INSERT INTO cat (animal_id) VALUES (1);      -- accepted: Luna is a dog AND a cat
```

<div dir="rtl">

**מניעה:** (1) עמודת `species_id` ב‑`dog` ו‑`cat` עם `CHECK (species_id = 1)` / `(species_id = 2)`, ומפתח זר **מורכב** `(animal_id, species_id)` ל‑`animal` (שעליה `UNIQUE (animal_id, species_id)`). כך שורה ב‑`dog` חייבת להתאים לחיה שהמין שלה כלב — ולכן לא יכולה להתאים גם לחתול. (2) או טריגר שבודק. (3) או אכיפה באפליקציה — ותיעוד ביומן ההחלטות.

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[❓ לשאלות](questions.md)**

</div>

</div>
