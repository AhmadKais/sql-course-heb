<div dir="rtl">

# שיעור 1: פתרונות

---

## תרגיל 1

**א.** 4 רשומות, 3 שדות.
**ב.** `100`.
**ג.** `species_id`. שם יכול להשתנות (למשל "Dog" יהפוך ל"כלב"), ומפתח ראשי חייב להיות **יציב**. חוץ מזה, מספר קצר נוח יותר כמפתח זר בטבלאות אחרות.
**ד.** משתנה **המופע**: נוספת רשומה, אבל השדות נשארים אותם שדות. מוסיפים עם `INSERT`.

---

## תרגיל 2

| הטבלה | המפתח הראשי | המפתחות הזרים |
|-------|-------------|----------------|
| species | species_id | אין |
| person | person_id | אין |
| animal | animal_id | species_id ← species |
| intake | intake_id | animal_id ← animal · **brought_by ← person** |
| vaccine_type | vaccine_type_id | species_id ← species |
| vaccination | vaccination_id | animal_id ← animal · vaccine_type_id ← vaccine_type · **vet_id ← person** |
| adoption | adoption_id | animal_id ← animal · **adopter_id ← person** |
| expense | expense_id | animal_id ← animal |

**סך הכול: 10 מפתחות זרים.** שלושת המודגשים הם המלכודת: השם שלהם שונה מ‑`person_id`, אבל כולם מפנים ל‑`person`.

---

## תרגיל 3

1. **נכון.** אין ב‑`species` אף שדה שמפנה לטבלה אחרת.
2. **לא נכון.** `species_id` הוא מפתח **זר** ב‑`animal`. המפתח הראשי הוא `animal_id`.
3. **נכון.** למין אחד יש הרבה חיות, ולכל חיה יש מין אחד.
4. **לא נכון.** `adopter_id` מפנה ל‑`person`. את החיה מזהה `animal_id`.
5. **נכון.** אדם יכול לאמץ כמה חיות, וחיה יכולה להיות מאומצת כמה פעמים (Luna אומצה פעמיים). `adoption` היא טבלת הקישור.
6. **נכון.** `animal_id`, `vaccine_type_id`, `vet_id`.

---

## תרגיל 4

**א.** שלושה קווים:
- `vaccine_type.vaccine_type_id (1)` ← `vaccination.vaccine_type_id (N)`
- `animal.animal_id (1)` ← `vaccination.animal_id (N)`
- `person.person_id (1)` ← `vaccination.vet_id (N)`

**ב.** `vaccination`. היא מקשרת בין `animal` ל‑`vaccine_type` (חיה מקבלת הרבה סוגי חיסון, וסוג חיסון ניתן להרבה חיות), ובנוסף רושמת **מי** הווטרינר.

**ג.** **לא.** שני השדות הם מפתחות **זרים**, ושניהם מפנים לטבלה **שלישית**, `species`. קו מחבר תמיד **מפתח ראשי** למפתח זר, ואף פעם לא שני מפתחות זרים זה לזה.

---

## תרגיל 5

| הזוג | סוג הקשר | טבלת קישור |
|------|----------|-------------|
| מורה ↔ כיתת חינוך | **1:1** | לא צריך |
| עיר ↔ תלמיד | **1:N** | לא צריך: `CityCode` בטבלת התלמידים |
| תלמיד ↔ קורס | **N:M** | `Enrollments(StudentId, CourseCode)` |
| שיר ↔ זמר | **N:M** | `PerformSongs(SongId, SingerId)` (כמו בבחינת 2023) |

---

## תרגיל 6

**א.** DML: `SELECT`, `UPDATE`, `INSERT`, `DELETE` · DDL: `CREATE TABLE`, `DROP TABLE`, `ALTER TABLE`

**ב.** 1. `INSERT` 2. `UPDATE` 3. `ALTER TABLE ... ADD` 4. `DELETE` 5. `DROP TABLE`

---

## תרגיל 7

</div>

```sql
-- א: 4 שורות
SELECT * FROM species;

-- ב
SELECT name, status FROM animal;

-- ג
SELECT first_name, last_name, role FROM person;

-- ד: שתי שורות, Dr. Ron Levi ו-Dr. Maya Nahum
SELECT first_name, last_name, role FROM person WHERE role = 'vet';

-- ה: בסגנון הבחינה, אותה תוצאה
SELECT person.first_name, person.last_name, person.role
FROM person
WHERE person.role = 'vet';
```

<div dir="rtl">

---

## תרגיל 8

**תשובה 2: Dog, Cat.** הסימן `>` פירושו "גדול מ", ולכן Parrot (שהמחיר שלו בדיוק 150) **לא** נכלל.
אילו היה כתוב `>=`, גם Parrot היה בתוצאה: Dog, Cat, Parrot (תשובה 1).

</div>

<!-- w3schools:start -->
<div dir="rtl">

---

## 🌐 תרגול ב‑W3Schools: פתרונות

> כל השאילתות כאן הורצו ב‑W3Schools. מספר הרשומות הוא מה שהאתר מחזיר.

**W1.**

```sql
SELECT * FROM Customers;
```

**91** רשומות. השורה הראשונה: `1 · Alfreds Futterkiste · Maria Anders · Obere Str. 57 · Berlin · 12209 · Germany`

**W2.**

```sql
SELECT * FROM Orders;
```

**196** רשומות. השורה הראשונה: `10248 · 90 · 5 · 1996-07-04 · 3`

`CustomerID` מפנה ל‑`Customers`. יש עוד שני מפתחות זרים: `EmployeeID` (מפנה ל‑`Employees`) ו‑`ShipperID` (מפנה ל‑`Shippers`). המפתח הראשי הוא `OrderID`.


</div>
<!-- w3schools:end -->
