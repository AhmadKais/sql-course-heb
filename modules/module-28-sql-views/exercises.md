<div dir="rtl">

# מודול 28 — תרגילים

> **הנחיות:** הדביקו את [`shelter.sql`](../../resources/shelter-db/shelter.sql) ו**כתבו ברצף** — חלק מה‑Views משתמשים ב‑Views קודמים.
>
> 📅 תאריך הייחוס: `'2026-09-21'`.
>
> ⚠️ אל תפתחו את [הפתרונות](solutions.md) לפני שניסיתם.
>
> **רמות:** 🟢 בסיסי · 🟡 בינוני · 🔴 מאתגר

---

## 🟢 תרגיל 1 — View ראשון

**א.** צרו `dog_view` עם המזהה, השם, הגזע, המשקל והסטטוס של כל הכלבים. כמה שורות?

**ב.** מתוך `dog_view` — הכלבים הזמינים, מהכבד לקל.

**ג.** צרו את `available_animal` מסעיף 2 במודול. כמה חיות זמינות מכל מין?

**ד.** שחררו את Nala מהסגר (`UPDATE` על `animal`). שאלו שוב את `available_animal`. **האם היה צריך "לרענן" משהו?**

---

## 🟡 תרגיל 2 — View שמסתיר מורכבות

**א.** צרו `vaccination_detail`: מזהה החיסון, שם החיה, שם החיסון, שם המשפחה של הווטרינר, התאריך, העלות, ו‑**`next_due`** — תאריך החיסון הבא (`given_date` + `interval_months` חודשים). (רמז: `DATE(d, '+' || n || ' months')`.)

**ב.** מתוך ה‑View — כל החיסונים של Rocky, עם `next_due`.

**ג.** כמה שורות ב‑`vaccination_detail`? האם זה שווה למספר השורות ב‑`vaccination`? למה זה חשוב?

---

## 🟡 תרגיל 3 — View כדוח

**א.** צרו `yearly_finance`: לכל שנה — הכנסות מאימוצים, הוצאות, ומאזן. (רמז: `UNION ALL` של שתי הטבלאות בתוך ה‑View, ואז `GROUP BY` — מודול 24.)

**ב.** צרו `in_shelter`: כל החיות שעדיין במקלט (`available`, `medical`, `quarantine`), ותאריך הקליטה **האחרון** שלהן. אחר כך — ארבע החיות שנמצאות במקלט הכי הרבה **ימים**.

**ג.** ⭐ צרו `animal_cost` מסעיף 4.1. למה ה‑View משתמש בתתי‑שאילתות ולא ב‑`JOIN`? מה היה יוצא ל‑Rocky עם `JOIN` לשתי הטבלאות?

---

## 🟡 תרגיל 4 — מצב נוכחי מתוך היסטוריה

**א.** צרו `current_home` מסעיף 5. כמה חיות נמצאות כרגע בבית מאמץ?

**ב.** השוו ל‑`SELECT COUNT(*) FROM adoption`. למה המספרים שונים?

**ג.** ⭐ צרו `View` על `View`: `latest_vaccine` — לכל חיה ולכל חיסון: התאריך האחרון ו‑`next_due` האחרון (מתוך `vaccination_detail`). אחר כך: כמה חיסונים **עברו את המועד** נכון ל‑`'2026-09-21'`? למה המספר כל כך גבוה — ואיך הייתם מצמצמים אותו לחיות שבאחריות המקלט?

---

## 🔴 תרגיל 5 — אבטחה ועדכון

**א.** צרו `public_person` — בלי טלפון ובלי שם משפחה. למה זה שימושי?

**ב.** נסו `UPDATE available_animal SET weight_kg = 30 WHERE name = 'Rocky';`. מה קורה ב‑SQLite? איך מעדכנים נכון?

**ג.** ⭐ ב‑Oracle — אילו מה‑Views שיצרתם אפשר היה לעדכן? (`dog_view`, `available_animal`, `yearly_finance`, `current_home`) נמקו לכל אחד.

**ד.** ⭐ ב‑Oracle יצרו את `dog_view` עם `WITH CHECK OPTION`, ומישהו מנסה `UPDATE dog_view SET species_id = 2 WHERE name = 'Rex'`. מה יקרה? מה היה קורה בלי `CHECK OPTION`? (רמז: האם `species_id` בכלל ב‑View?)

---

## 🔴 תרגיל 6 — ניהול

**א.** הציגו את כל ה‑Views בבסיס הנתונים.

**ב.** מחקו את `animal_cost`. האם הוצאה כלשהי נמחקה?

**ג.** ⭐ שנו את `available_animal` כך שיכלול גם חיות ב‑`quarantine`. איך עושים את זה ב‑SQLite, ואיך ב‑Oracle?

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[✅ לפתרונות](solutions.md)**

</div>

</div>


<!-- w3schools:start -->
<div dir="rtl">

---

## 🌐 תרגול נוסף ב‑W3Schools

📖 **לקריאה ב‑W3Schools:** [VIEW](https://www.w3schools.com/sql/sql_view.asp)

> 💻 הפקודות של השיעור הזה **משנות** נתונים או מבנה, ו‑W3Schools לא מאפשר את זה. קראו שם את ההסבר, ואת התרגול עצמו עשו ב‑OneCompiler, על בסיס הנתונים של המקלט ([הוראות](../../resources/setup.md)).

</div>
<!-- w3schools:end -->

<!-- exam-style:start -->
<div dir="rtl">

---

## 🎓 תרגול בסגנון הבחינה

> 🎓 **תרגול בסגנון הבחינה (שאלון 735911).** הסעיפים כאן כתובים בדיוק כמו בבחינה: `Table.Column`, צירוף עם פסיק ומירכאות כפולות. הם רצים על בסיס הנתונים **חוגי ספורט** ([`clubs.sql`](../../exam-prep/db/clubs.sql)). פתרו על הנייר, ואחר כך טענו את הקובץ ל‑OneCompiler ובדקו.

**ב1.** **"שאילתה שמורה" בבחינה = View.** תלמיד שמר את השאילתה Q1:
```sql
SELECT MIN(Clubs.Price) AS cheap FROM Clubs;
```
1. איזה ערך יוחזר בשדה cheap?
2. השלימו את השאילתה שמציגה את שם החוג הזול ביותר:
```sql
SELECT Clubs.ClubName FROM Clubs, ________
WHERE Clubs.Price = ________;
```


</div>
<!-- exam-style:end -->
