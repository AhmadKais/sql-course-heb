<div dir="rtl">

# מודול 16 — פתרונות מלאים

> ⚠️ **עצרו.** אם לא הרצתם בעצמכם — [חזרו לתרגילים](exercises.md).
>
> 💡 **כל הפלטים כאן הם אמיתיים** — הופקו מ‑`shelter.sql`. אם קיבלתם משהו אחר, בדקו שטענתם את הקובץ במלואו.

---

## ✅ תרגיל 1 — הסיור הראשון

### א.

</div>

```sql
SELECT * FROM species;
```

```text
species_id  name    adoption_fee
----------  ------  ------------
1           Dog     400.0
2           Cat     250.0
3           Rabbit  100.0
4           Parrot  150.0
```

<div dir="rtl">

**4 שורות.**

### ב.

</div>

```sql
SELECT * FROM person;
```

<div dir="rtl">

**7 עמודות:** `person_id` · `first_name` · `last_name` · `role` · `city` · `phone` · `joined_date`.
**12 שורות.** שימו לב שלעומר (`person_id = 10`) אין טלפון — NULL.

### ג.

</div>

```sql
SELECT * FROM animal;
```

<div dir="rtl">

**4 חיות בלי גזע:** Mitzi · Nala · Lily · Bunny. (בתצוגה — התא ריק. זה NULL.)

---

## ✅ תרגיל 2 — עמודות נבחרות

</div>

```sql
-- a
SELECT name, status
FROM   animal;

-- b
SELECT first_name, last_name, city
FROM   person;

-- c  -- same columns, different order in the result
SELECT city, first_name, last_name
FROM   person;

-- d
SELECT expense_date, category, amount
FROM   expense;
```

<div dir="rtl">

**פלט של ג'** (ראשונות):

</div>

```text
city          first_name  last_name
------------  ----------  ---------
Haifa         Ruti        Almog
Haifa         Noa         Peretz
Kiryat Ata    Amir        Levi
```

<div dir="rtl">

> 🔑 סדר העמודות בתוצאה = הסדר ב‑`SELECT`. לא הסדר בטבלה.

---

## ✅ תרגיל 3 — כינויים

</div>

```sql
-- a
SELECT name AS animal_name
FROM   animal;

-- b  -- a space in the alias needs double quotes
SELECT weight_kg AS "Weight (kg)"
FROM   animal;

-- c
SELECT fee_paid      AS paid_nis,
       adoption_date AS "date"
FROM   adoption;
```

<div dir="rtl">

### ד. בלי גרשיים

</div>

```sql
SELECT weight_kg AS Weight (kg) FROM animal;
```

```text
Error: near "(": syntax error
```

<div dir="rtl">

**למה:** בסיס הנתונים קרא `Weight` ככינוי, ואז נתקל ב‑`(` ולא ידע מה לעשות איתו. **המילה אחרי `near` היא המקום שבו הוא התבלבל** — והטעות היא ממש לפניה: הכינוי לא היה בגרשיים כפולות.

---

## ✅ תרגיל 4 — חישובים

</div>

```sql
-- a
SELECT name, weight_kg, weight_kg * 1000 AS weight_g
FROM   animal;

-- b
SELECT fee_paid, fee_paid * 1.18 AS with_vat
FROM   adoption;

-- c
SELECT amount, amount / 12 AS per_month
FROM   expense;
```

```text
-- a (first rows)
name     weight_kg  weight_g
-------  ---------  --------
Luna     18.5       18500.0
Simba    4.2        4200.0

-- b (first rows)
fee_paid  with_vat
--------  --------
300.0     354.0
200.0     236.0
```

<div dir="rtl">

### ד. חילוק שלמים

</div>

```sql
SELECT 10 / 4;      -- 2
SELECT 10 / 4.0;    -- 2.5
```

<div dir="rtl">

<div align="center">

**⚠️ שלם חלקי שלם = שלם. השארית נזרקת.**

</div>

`10 / 4` — שני מספרים **שלמים** ⟵ התוצאה שלם ⟵ `2`, לא `2.5`.
`10 / 4.0` — אחד מהם **עשרוני** ⟵ התוצאה עשרונית ⟵ `2.5`.

**למה זה חשוב:** `amount / 12` ב‑ג' עובד כי `amount` מוגדר כ‑`REAL`. אבל אם הייתם מחלקים עמודת `INTEGER` — הייתם מאבדים את השארית **בשקט**, בלי שגיאה. זו טעות שמסתתרת בדוחות כספיים.

> 💡 **בטיחות:** כשמחלקים — כתבו `12.0` ולא `12`. זה לא עולה כלום.

---

## ✅ תרגיל 5 — חיבור מחרוזות

</div>

```sql
-- a
SELECT first_name || ' ' || last_name AS full_name
FROM   person;

-- b
SELECT name || ' - ' || breed AS label
FROM   animal;

-- d
SELECT first_name || ' ' || last_name || ' (' || role || ')' AS label
FROM   person;
```

```text
-- b
label
------------------------
Luna - Mixed
Simba - Tabby
Rocky - Labrador
                          <- Mitzi: the whole thing is NULL
Bella - German Shepherd

-- d
label
-------------------------
Ruti Almog (volunteer)
Noa Peretz (volunteer)
Amir Levi (volunteer)
Dr. Ron Levi (vet)
```

<div dir="rtl">

### ג. מה קרה ל‑Mitzi

**השורה שלה ריקה לגמרי** — לא `Mitzi - `, אלא כלום.

**למה:** `breed` של Mitzi הוא NULL. `'Mitzi' || ' - ' || NULL` ⟵ **NULL מדביק** ⟵ הכול NULL. אפילו השם נעלם.

זו **הנקודה החשובה ביותר במודול**, ותפגשו אותה שוב ושוב. הפתרון — `COALESCE` — במודול 20.

---

## ✅ תרגיל 6 — DISTINCT

</div>

```sql
-- a
SELECT DISTINCT city FROM person;

-- b
SELECT DISTINCT category FROM expense;

-- c
SELECT DISTINCT species_id, status FROM animal;
```

```text
-- a: 7 cities
city
------------
Haifa
Kiryat Ata
Nesher
Tel Aviv
Karmiel
Tirat Carmel
Nahariya

-- b: 5 categories
category
-----------
food
medical
utilities
supplies
maintenance

-- c: 11 unique (species, status) pairs
species_id  status
----------  ----------
1           adopted
2           adopted
1           available
2           available
4           available
1           medical
2           quarantine
3           adopted
4           adopted
1           deceased
3           available
```

<div dir="rtl">

### ד. `DISTINCT name`

**20 שורות — בדיוק כמו בלי `DISTINCT`.**

**מה זה אומר על הנתונים:** אין שתי חיות עם אותו שם. **בינתיים.** ברגע שייכנס כלב שני בשם Max — `DISTINCT name` יחזיר 20 ו‑`name` יחזיר 21, וכל שאילתה שהסתמכה על "שם = חיה" תישבר.

> 🔑 **וזו הסיבה שהמזהה הוא `animal_id` ולא `name`** (מודול 6). השם ייחודי במקרה; המזהה ייחודי **בהגדרה**.

---

## ✅ תרגיל 7 — NULL בפעולה

</div>

```sql
-- a
SELECT name, chip_number FROM animal;

-- b
SELECT name, 'Chip: ' || chip_number AS chip_label FROM animal;
```

```text
-- a                          -- b
name    chip_number           name    chip_label
------  -----------           ------  ----------------
Luna    985100001             Luna    Chip: 985100001
Simba   985100002             Simba   Chip: 985100002
Rocky   985100003             Rocky   Chip: 985100003
Mitzi                         Mitzi                     <- NULL again
Bella   985100005             Bella   Chip: 985100005
```

<div dir="rtl">

**ב:** 8 חיות בלי שבב ⟵ 8 שורות ריקות ב‑`chip_label`. אותו מנגנון כמו בתרגיל 5.

**ג:** **3 חיות** בלי תאריך לידה — Coco, Lily, Kiwi. (ציפורים וחתולת רחוב — הגיוני שלא יודעים.)

### ד.

</div>

```sql
SELECT NULL + 5;         -- NULL
SELECT NULL || 'text';   -- NULL
SELECT NULL * 0;         -- NULL  (!)  even times zero
```

<div dir="rtl">

<div align="center">

**המשותף: כולם NULL. אין יוצא מן הכלל.**

</div>

השלישי מפתיע: `NULL * 0` — "הרי כל דבר כפול אפס הוא אפס!" **לא.** NULL אינו מספר; הוא "לא ידוע". ולא ידוע כפול אפס — עדיין לא ידוע.

---

## ✅ תרגיל 8 — לקרוא שגיאות

| | השאילתה | מה קורה | הסבר |
|---|----------|----------|-------|
| a | `wieght_kg` | ❌ `no such column: wieght_kg` | כתיב. `i` ו‑`e` הפוכים |
| b | בלי `;` | ⚠️ **תלוי בכלי.** ב‑OneCompiler השאילתה האחרונה רצה גם בלי `;`. כלים אחרים: "incomplete input" | **תמיד** `;`. גם כשהכלי סולח |
| c | `"name"` בגרשיים כפולות | ✅ **רץ!** מחזיר את העמודה `name` | גרשיים כפולות = **שם**. `"name"` הוא שם עמודה קיים, אז זה עובד. אבל `"Luna"` היה נכשל |
| d | `breed, FROM` | ❌ `near "FROM": syntax error` | פסיק אחרי העמודה האחרונה |
| e | `Animal` באות גדולה | ✅ **רץ.** | SQL לא רגיש לאותיות בשמות (ב‑SQLite וב‑Oracle כאחד) |
| f | `\|\| breed` | ✅ **רץ** — אבל 4 שורות ריקות | לא שגיאה. **NULL מדביק.** זה "רץ אבל לא כמו שציפיתם" |

**השתיים שאינן שגיאות:** **c** ו‑**e** (ובמובן מסוים גם **f**).

> 🔑 **c היא המסוכנת ביותר.** היא עובדת **במקרה** — כי יש עמודה בשם `name`. `SELECT "Luna" FROM animal` **ייכשל** ב‑`no such column: Luna`. הכלל נשאר: **גרש בודד לערך, כפול לשם.**

---

## ✅ תרגיל 9 — הדוח לרותי

### א. בשלבים

</div>

```sql
-- step 1: what's there
SELECT * FROM animal;

-- step 2: only the columns she needs
SELECT name, sex, weight_kg, chip_number, status
FROM   animal;

-- step 3: glue them together
SELECT name || ' | ' || sex || ' | ' || weight_kg || ' kg | chip '
            || chip_number || ' | ' || status   AS line
FROM   animal;
```

```text
line
-------------------------------------------------
Luna | F | 18.5 kg | chip 985100001 | adopted
Simba | M | 4.2 kg | chip 985100002 | adopted
Rocky | M | 31.0 kg | chip 985100003 | available
                                                    <- Mitzi
Bella | F | 28.4 kg | chip 985100005 | adopted
Tom | M | 4.8 kg | chip 985100006 | adopted
                                                    <- Coco
```

<div dir="rtl">

### ב. חיות בלי שבב

**8 שורות ריקות לגמרי.** לא רק "chip" ריק — **כל השורה**, כולל השם. הדוח של רותי חסר 8 חיות.

### ג. למה, ומה צריך

**למה:** `chip_number` הוא NULL ⟵ החיבור כולו NULL. ראינו את זה שלוש פעמים כבר במודול הזה — וזו הפעם שבה זה **באמת** שובר משהו: דוח שנמסר ללקוחה עם 8 שורות חסרות.

**מה צריך:** דרך לומר *"אם `chip_number` ריק — תציג `'none'` במקום"*. הפונקציה הזאת נקראת `COALESCE` והיא במודול 20. עד אז — **דעו שהדוח הזה לא מוכן למסירה.**

### ד. עם פאונד

</div>

```sql
SELECT name || ' | ' || sex || ' | '
            || weight_kg || ' kg / ' || weight_kg * 2.2 || ' lb | chip '
            || chip_number || ' | ' || status   AS line
FROM   animal;
-- -> "Luna | F | 18.5 kg / 40.7 lb | chip 985100001 | adopted"
```

<div dir="rtl">

---

## ✅ תרגיל 10 — מפת הדרכים

| # | השאלה | אפשר עכשיו? | מה חסר |
|---|--------|-------------|---------|
| 1 | כל החיות | ✅ | `SELECT * FROM animal` |
| 2 | רק כלבים | ❌ | **`WHERE`** — מודול 17 |
| 3 | מהכבדה לקלה | ❌ | **`ORDER BY`** — מודול 18 |
| 4 | כמה חיות | ❌ | **`COUNT`** — מודול 23 |
| 5 | שם המין ולא המספר | ❌ | **`JOIN`** — מודול 21 |
| 6 | בלי שבב | ❌ | **`WHERE … IS NULL`** — מודול 17 |
| 7 | כמה עלה כל חיה | ❌ | **`JOIN` + `SUM` + `GROUP BY`** — מודולים 21, 23, 24 |
| 8 | שם מלא של מתנדבים | ⚠️ **חצי** | החיבור אפשר (`\|\|`); הסינון למתנדבים בלבד — **`WHERE`**, מודול 17 |

> 🎓 **שימו לב:** מתוך 8 שאלות פשוטות של רותי — עניתם על אחת. **אחרי מודול 17 תענו על ארבע.** אחרי 21 — על שבע. זה המסלול.

---

<div align="center">

### 🎯 סיימתם את מודול 16!

כתבתם SQL. הרצתם. קיבלתם שגיאות ותיקנתם. **זה כל ההבדל בין מי שיודע על SQL למי שיודע SQL.**
במודול הבא — `WHERE`: לבחור **אילו שורות**.

---

### ➡️ [מודול 17 — SQL: הגבלת השליפה](../module-17-sql-where/)

</div>

---

<div align="center">

**🧭 ניווט המודול**

</div>

| 📖 [חזרה למודול](README.md) | ❓ [שאלות ותשובות](questions.md) | ✏️ [לתרגילים](exercises.md) | 🏠 [דף הקורס](../../) |
|---|---|---|---|

</div>


<!-- w3schools:start -->
<div dir="rtl">

---

## 🌐 תרגול ב‑W3Schools: פתרונות

> כל השאילתות כאן הורצו ב‑W3Schools. מספר הרשומות הוא מה שהאתר מחזיר.

**W1.**

```sql
SELECT Customers.CustomerName, Customers.City FROM Customers;
```

**91** רשומות. השורה הראשונה: `Alfreds Futterkiste · Berlin`

**W2.**

```sql
SELECT DISTINCT Customers.Country FROM Customers;
```

**21** רשומות. השורה הראשונה: `Argentina`

**W3.**

```sql
SELECT Products.ProductName, Products.Price AS PriceUSD FROM Products;
```

**77** רשומות. השורה הראשונה: `Chais · 18.00`


</div>
<!-- w3schools:end -->

<!-- exam-style:start -->
<div dir="rtl">

---

## 🎓 תרגול בסגנון הבחינה: פתרונות

**ב1.** **2.** `*` פירושו כל השדות.

**ב2.** **6** שורות. כדורגל ושחייה מופיעים פעמיים ב‑Clubs, אבל `DISTINCT` מציג כל ענף פעם אחת. בלי `DISTINCT` היו מתקבלות 8 שורות.

<figure dir="ltr" class="dbtable">

| Sport |
|:---:|
| כדורגל |
| שחייה |
| כדורסל |
| טניס |
| ג'ודו |
| יוגה |

</figure>

**ב3.** ```sql
SELECT Clubs.ClubName, Clubs.Price AS "מחיר חודשי"
FROM Clubs;
```


</div>
<!-- exam-style:end -->

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

> 💡 **למורה:** אפשר להדביק את כל הבלוק הבא ב‑OneCompiler **מתחת** ל‑`school.sql` ולהריץ פעם אחת — כל 12 הפלטים יופיעו אחד אחרי השני.

</div>

```sql
-- ש1
SELECT * FROM Teachers;

-- ש2
SELECT Students.FirstName, Students.LastName FROM Students;

-- ש3
SELECT Courses.CourseName AS "מקצוע", Courses.WeeklyHours AS "שעות שבועיות" FROM Courses;

-- ש4
SELECT DISTINCT Teachers.Subject FROM Teachers;

-- ש5
SELECT DISTINCT Classes.Grade FROM Classes;

-- ש6
SELECT Teachers.FirstName || ' ' || Teachers.LastName AS FullName FROM Teachers;

-- ש7
SELECT Teachers.LastName, Teachers.Salary, Teachers.Salary * 12 AS AnnualSalary FROM Teachers;

-- ש8
SELECT Courses.CourseName, Courses.WeeklyHours * 30 AS YearlyHours FROM Courses;

-- ש9
SELECT Students.FirstName, Students.Phone FROM Students;

-- ש10
SELECT Students.FirstName, Students.Phone || ' (בית)' AS PhoneLabel FROM Students;

-- ש11
SELECT * FROM Grades LIMIT 5;

-- ש12  -- ⚠️ נכשלת בכוונה
SELECT Students.FirstName, Students.LastName FROM Student;
```

<div dir="rtl">

**ש1.** **7 שורות** — 7 מורים. `*` מחזיר את כל 8 העמודות, כולל `Phone` שהוא `NULL` אצל רונית וגלית.

<figure dir="ltr" class="dbtable">

| TeacherCode | FirstName | LastName | Subject | HireDate | Salary | CityCode | Phone |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | נביל | סרחאן | מתמטיקה | 2012-09-01 | 14500 | 1 | 050-7010101 |
| 2 | רונית | בר-לב | אנגלית | 2018-09-01 | 11200 | 4 | NULL |
| 3 | חוסאם | זיאד | מחשבים | 2021-02-15 | 12800 | 6 | 054-7030303 |
| 4 | אורלי | שמש | היסטוריה | 2009-09-01 | 15300 | 5 | 052-7040404 |
| 5 | פאדי | חדאד | ספורט | 2023-09-01 | 9800 | 1 | 053-7050505 |
| 6 | גלית | מזרחי | מתמטיקה | 2016-09-01 | 13100 | 3 | NULL |
| 7 | סמיר | אבו-ראס | ביולוגיה | 2024-09-01 | 10400 | 2 | 050-7070707 |

</figure>

**ש2.** **18 שורות.** חמש הראשונות:

<figure dir="ltr" class="dbtable">

| FirstName | LastName |
|:---:|:---:|
| אדם | חלבי |
| נור | עזאם |
| יואב | כהן |
| מאיה | לוי |
| רוני | אברהם |

</figure>

**ש3.** כינוי עם רווח או עברית — בין **מירכאות כפולות**: `AS "שעות שבועיות"`.

<figure dir="ltr" class="dbtable">

| מקצוע | שעות שבועיות |
|:---:|:---:|
| מתמטיקה 5 יח"ל | 5 |
| אנגלית 4 יח"ל | 4 |
| מבוא לבסיסי נתונים | 3 |
| היסטוריה | 2 |
| חינוך גופני | 2 |
| מתמטיקה 3 יח"ל | 3 |
| סדנת פרויקטים | 2 |

</figure>

**ש4.** **6 שורות, לא 7.** נביל וגלית **שניהם** מלמדים מתמטיקה — `DISTINCT` מאחד אותם לשורה אחת. זו בדיוק המטרה שלו: הוא מתאר **אילו ערכים קיימים**, לא **כמה שורות יש**.

<figure dir="ltr" class="dbtable">

| Subject |
|:---:|
| מתמטיקה |
| אנגלית |
| מחשבים |
| היסטוריה |
| ספורט |
| ביולוגיה |

</figure>

**ש5.** 5 כיתות — אבל רק **3 שכבות**.

<figure dir="ltr" class="dbtable">

| Grade |
|:---:|
| 10 |
| 11 |
| 12 |

</figure>

**ש6.** הרווח הוא מחרוזת בפני עצמה: `|| ' ' ||`. בלעדיו תקבלו `נבילסרחאן`.

<figure dir="ltr" class="dbtable">

| FullName |
|:---:|
| נביל סרחאן |
| רונית בר-לב |
| חוסאם זיאד |
| אורלי שמש |
| פאדי חדאד |
| גלית מזרחי |
| סמיר אבו-ראס |

</figure>

**ש7.** החישוב נעשה **בשליפה**; בטבלה לא נשמר כלום.

<figure dir="ltr" class="dbtable">

| LastName | Salary | AnnualSalary |
|:---:|:---:|:---:|
| סרחאן | 14500 | 174000 |
| בר-לב | 11200 | 134400 |
| זיאד | 12800 | 153600 |
| שמש | 15300 | 183600 |
| חדאד | 9800 | 117600 |
| מזרחי | 13100 | 157200 |
| אבו-ראס | 10400 | 124800 |

</figure>

**ש8.**

<figure dir="ltr" class="dbtable">

| CourseName | YearlyHours |
|:---:|:---:|
| מתמטיקה 5 יח"ל | 150 |
| אנגלית 4 יח"ל | 120 |
| מבוא לבסיסי נתונים | 90 |
| היסטוריה | 60 |
| חינוך גופני | 60 |
| מתמטיקה 3 יח"ל | 90 |
| סדנת פרויקטים | 60 |

</figure>

**ש9.** **6 תלמידים בלי טלפון:** נור, רוני, כרים, ג'וד, איתי, לינא.

<figure dir="ltr" class="dbtable">

| FirstName | Phone |
|:---:|:---:|
| אדם | 050-1000001 |
| נור | NULL |
| יואב | 052-1000003 |
| … | … |
| לינא | NULL |

</figure>

**ש10.** אצל ששת התלמידים האלה קיבלתם **`NULL`** — ולא `(בית)`.

`NULL` אינו "ריק"; הוא **"לא ידוע"**. וכל חישוב שמשתתף בו ערך לא‑ידוע — תוצאתו לא ידועה. מה זה "לא‑ידוע ועוד `' (בית)'`"? לא ידוע. לכן `NULL` **"מדביק"**: הוא בולע כל ביטוי שהוא נוגע בו, גם חיבור מחרוזות וגם חשבון.

<figure dir="ltr" class="dbtable">

| FirstName | PhoneLabel |
|:---:|:---:|
| אדם | 050-1000001 (בית) |
| נור | NULL |
| יואב | 052-1000003 (בית) |
| מאיה | 054-1000004 (בית) |
| רוני | NULL |

</figure>

> 🔮 בשיעור 20 תפגשו את `COALESCE` — הפונקציה שמחליפה `NULL` בערך ברירת מחדל, ופותרת בדיוק את זה.

**ש11.** `1001` מופיע **ארבע פעמים**, ו‑`CourseCode = 11` מופיע **פעמיים** — לכן אף אחד מהם לבדו אינו מזהה שורה. גם הצמד `(1001, 11)` חוזר פעמיים, במחצית 1 ובמחצית 2. המפתח הראשי הוא **שלושת השדות יחד**: `(StudentId, CourseCode, Term)`. זה "מפתח מורכב", והוא מה שמאפשר לשמור לאותו תלמיד ציון באותו מקצוע בשתי מחציות.

<figure dir="ltr" class="dbtable">

| StudentId | CourseCode | Term | Grade |
|:---:|:---:|:---:|:---:|
| 1001 | 11 | 1 | 88 |
| 1001 | 12 | 1 | 74 |
| 1001 | 14 | 1 | 92 |
| 1001 | 11 | 2 | 91 |
| 1002 | 11 | 1 | 95 |

</figure>

**ש12.** ההודעה:

</div>

```text
no such table: Student
```

<div dir="rtl">

המילה החשובה היא **`Student`** — ההודעה מצטטת לכם בדיוק את מה שלא מצאה. הטבלה נקראת `Students`, **ברבים**. התיקון: `FROM Students`.

שלוש הודעות שתפגשו הכי הרבה, ומה הן אומרות:

| ההודעה | מה קרה | התיקון |
|---------|---------|---------|
| `no such table: X` | שם טבלה שגוי | בדקו רבים/יחיד ואיות |
| `no such column: X` | שם עמודה שגוי | `Grade` או `Grades`? עמודה או טבלה? |
| `near "FORM": syntax error` | מילה שמורה מאויתת לא נכון | המילה **לפני** המצוטטת היא בדרך כלל האשמה |

</div>
<!-- classroom:end -->
