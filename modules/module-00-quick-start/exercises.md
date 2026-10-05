<div dir="rtl">

# שיעור 1: תרגילים

> כל התרגילים כאן **בסגנון הבחינה**. תרגילים 1–6 פותרים על הנייר, ותרגילים 7–8 פותרים במחשב, על [בסיס הנתונים של המקלט](../../resources/shelter-db/).
> ⚠️ אל תפתחו את [הפתרונות](solutions.md) לפני שניסיתם.
>
> **רמות:** 🟢 בסיסי · 🟡 בינוני · 🔴 מאתגר

---

## 🟢 תרגיל 1: לקרוא טבלה

</div>

```text
                species
 +------------+---------+--------------+
 | species_id | name    | adoption_fee |
 +------------+---------+--------------+
 | 1          | Dog     | 400          |
 | 2          | Cat     | 250          |
 | 3          | Rabbit  | 100          |
 | 4          | Parrot  | 150          |
 +------------+---------+--------------+
```

<div dir="rtl">

**א.** כמה **רשומות** יש בטבלה? כמה **שדות**?
**ב.** מה **הערך** בשדה `adoption_fee` ברשומה של Rabbit?
**ג.** מהו המפתח הראשי? למה הוא לא `name`?
**ד.** המקלט מתחיל לקבל גם צבים. מה ישתנה, **התבנית** או **המופע**? באיזו פקודה מוסיפים את הצב?

---

## 🟢 תרגיל 2: מפתחות במקלט

אלה הטבלאות של בסיס הנתונים של המקלט (השדות שמופיעים כאן הם רק חלק מהשדות):

</div>

```text
species      (species_id, name, adoption_fee)
person       (person_id, first_name, last_name, role, city)
animal       (animal_id, name, species_id, breed, status)
intake       (intake_id, animal_id, intake_date, brought_by)
vaccine_type (vaccine_type_id, name, species_id, interval_months)
vaccination  (vaccination_id, animal_id, vaccine_type_id, vet_id, given_date, cost)
adoption     (adoption_id, animal_id, adopter_id, adoption_date, fee_paid)
expense      (expense_id, expense_date, category, amount, animal_id)
```

<div dir="rtl">

השלימו את הטבלה. ⚠️ שימו לב: יש שדות שהשם שלהם **שונה** משם המפתח הראשי שהם מפנים אליו.

| הטבלה | המפתח הראשי | המפתחות הזרים (ולאן כל אחד מפנה) |
|-------|-------------|-----------------------------------|
| species | | |
| person | | |
| animal | | |
| intake | | |
| vaccine_type | | |
| vaccination | | |
| adoption | | |
| expense | | |

**כמה מפתחות זרים יש בסך הכול?** ________

---

## 🟢 תרגיל 3: נכון או לא נכון

קבעו לגבי כל היגד אם הוא **נכון** או **לא נכון**, והסבירו בשורה אחת:

1. בטבלה `species` אין מפתח זר.
2. בטבלה `animal` השדה `species_id` הוא מפתח ראשי.
3. הקשר בין `species` ל‑`animal` הוא קשר של יחיד לרבים.
4. השדה `adopter_id` בטבלה `adoption` מפנה לטבלה `animal`.
5. הקשר בין `animal` ל‑`person` (דרך `adoption`) הוא קשר של רבים לרבים.
6. בטבלה `vaccination` יש שלושה מפתחות זרים.

---

## 🟡 תרגיל 4: קווים בתרשים DSD

לפניכם ארבע טבלאות, **בלי קווי הקשר**:

</div>

```text
 +-----------------+   +------------------+   +-----------------+   +-------------+
 | vaccine_type    |   | vaccination      |   | animal          |   | person      |
 +-----------------+   +------------------+   +-----------------+   +-------------+
 | vaccine_type_id |   | vaccination_id   |   | animal_id       |   | person_id   |
 | name            |   | animal_id        |   | name            |   | first_name  |
 | species_id      |   | vaccine_type_id  |   | species_id      |   | last_name   |
 | interval_months |   | vet_id           |   | status          |   | role        |
 |                 |   | given_date       |   |                 |   |             |
 |                 |   | cost             |   |                 |   |             |
 +-----------------+   +------------------+   +-----------------+   +-------------+
```

<div dir="rtl">

**א.** כמה קווי קשר יש **בין ארבע הטבלאות האלה**? רשמו כל קו בצורה `טבלה.שדה (1) ← טבלה.שדה (N)`.
**ב.** איזו טבלה היא "טבלת הקישור" כאן? בין אילו שתי טבלאות היא מקשרת?
**ג.** השדה `species_id` מופיע ב‑`vaccine_type` וגם ב‑`animal`. האם יש קו **ביניהן**? הסבירו.

---

## 🟡 תרגיל 5: סוג הקשר

לכל זוג כתבו **1:1**, **1:N** או **N:M**. אם הקשר הוא N:M, כתבו גם מה צריכה להיות טבלת הקישור.

| הזוג | סוג הקשר | טבלת קישור (אם צריך) |
|------|----------|----------------------|
| מורה ↔ כיתה שהוא מחנך שלה (לכל כיתה מחנך אחד, ולכל מורה כיתת חינוך אחת לכל היותר) | | |
| עיר ↔ תלמיד שגר בה | | |
| תלמיד ↔ קורס שהוא לומד | | |
| שיר ↔ זמר שמבצע אותו (שיר יכול להיות של כמה זמרים) | | |

---

## 🟢 תרגיל 6: DDL או DML, ואיזו פקודה?

**א.** לכל פקודה כתבו **DDL** או **DML**: `SELECT` · `CREATE TABLE` · `UPDATE` · `DROP TABLE` · `INSERT` · `ALTER TABLE` · `DELETE`

**ב.** איזו פקודה מתאימה לכל מקרה?
1. חיה חדשה הגיעה למקלט.
2. המשקל של Rocky השתנה.
3. רוצים לשמור לכל חיה גם את הצבע שלה (שדה חדש).
4. החיסון של Max נרשם בטעות, וצריך למחוק אותו.
5. החליטו שהטבלה `expense` כבר לא נחוצה בכלל.

---

## 🟢 תרגיל 7: השאילתות הראשונות (במחשב)

טענו את `shelter.sql` ל‑OneCompiler והריצו:

**א.** `SELECT * FROM species;` כמה שורות התקבלו?
**ב.** הציגו את `name` ואת `status` של כל החיות.
**ג.** הציגו את `first_name`, `last_name` ו‑`role` של כל האנשים.
**ד.** הציגו רק את האנשים שה‑`role` שלהם הוא `'vet'`.
**ה.** כתבו את שאילתה ד׳ שוב, **בסגנון הבחינה**: עם שם הטבלה לפני כל שדה (`person.first_name`...). הריצו וודאו שהתוצאה זהה.

---

## 🔴 תרגיל 8: איזו טבלה תתקבל?

**בלי להריץ**, ורק לפי הטבלה `species` שבתרגיל 1, מה תחזיר השאילתה?

</div>

```sql
SELECT species.name
FROM species
WHERE species.adoption_fee > 150;
```

<div dir="rtl">

1. Dog, Cat, Parrot   2. Dog, Cat   3. Dog   4. Cat, Rabbit, Parrot

אחרי שעניתם, הריצו ובדקו את עצמכם. מה היה משתנה אילו היה כתוב `>=` במקום `>`?

</div>

<!-- w3schools:start -->
<div dir="rtl">

---

## 🌐 תרגול נוסף ב‑W3Schools

📖 **לקריאה ב‑W3Schools:** [מבוא](https://www.w3schools.com/sql/sql_intro.asp) · [תחביר](https://www.w3schools.com/sql/sql_syntax.asp) · [PRIMARY KEY](https://www.w3schools.com/sql/sql_primarykey.asp) · [FOREIGN KEY](https://www.w3schools.com/sql/sql_foreignkey.asp)

> 🌐 **פותחים את [עורך ה‑SQL של W3Schools](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all)**, מוחקים את מה שכתוב בו, כותבים שאילתה ולוחצים **Run SQL**. בסיס הנתונים שם הוא של חברה לממכר מזון: `Customers`, `Orders`, `OrderDetails`, `Products`, `Categories`, `Suppliers`, `Shippers` ו‑`Employees`. לחיצה על שם טבלה בצד מציגה את התוכן שלה.
>
> ⚠️ בבסיס הנתונים של W3Schools **אפשר רק לקרוא** (`SELECT`). טקסט כותבים שם בין גרשיים **בודדים**: `'Germany'`.

**W1.** הציגו את כל השדות של הטבלה `Customers`. כמה רשומות יש בה?

**W2.** הציגו את כל הטבלה `Orders`. איזה שדה בה הוא מפתח זר שמפנה ל‑`Customers`? ואילו עוד מפתחות זרים יש בה?


</div>
<!-- w3schools:end -->
