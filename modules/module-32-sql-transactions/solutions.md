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
