<div dir="rtl">

# מודול 25 — תרגילים

> **הנחיות:** הדביקו את [`shelter.sql`](../../resources/shelter-db/shelter.sql), ומיד אחריו:
>
> ```sql
> PRAGMA foreign_keys = ON;
> ```
>
> **כתבו את כל התרגילים ברצף, אחד אחרי השני** — חלק מהם משתמשים בשורות שהוספתם בתרגיל קודם. אם משהו השתבש — הדביקו את הקובץ מחדש והתחילו שוב. זה בדיוק היתרון של סביבת תרגול.
>
> 📋 **אחרי כל `UPDATE` / `DELETE`:** `SELECT changes();` — ובדקו שהמספר הוא מה שציפיתם.
>
> ⚠️ אל תפתחו את [הפתרונות](solutions.md) לפני שניסיתם.
>
> **רמות:** 🟢 בסיסי · 🟡 בינוני · 🔴 מאתגר

---

## 🟢 תרגיל 1 — INSERT

**א.** מתנדבת חדשה: נור חדאד (Nour Haddad), מירכא (Yarka), טלפון `052-3434343`, הצטרפה ב‑`2026-09-01`. **בלי** לתת `person_id`. איזה מזהה היא קיבלה?

**ב.** שתי חיות חדשות **בפקודה אחת**: כלב בשם Lucky (זכר) וחתולה בשם Snow (נקבה), שתיהן בסטטוס `quarantine`. שאר העמודות — לא ידועות.

**ג.** Lucky נמצא במרכז ירכא (`'Yarka center'`) ב‑`2026-09-20`, ונור הביאה אותו. רשמו את הקליטה.

**ד.** ⚠️ נסו לרשום קליטה לחיה מספר 99. מה קרה? ומה היה קורה בלי `PRAGMA foreign_keys = ON`?

---

## 🟢 תרגיל 2 — אילוצים

לכל `INSERT` — **חזו** איזו שגיאה תתקבל, ואז הריצו:

</div>

```sql
INSERT INTO animal (name, species_id, sex) VALUES ('Ghost', 1, 'M');
INSERT INTO animal (name, species_id, sex, status) VALUES ('Twin', 1, 'X', 'available');
INSERT INTO animal (animal_id, name, species_id, sex, status) VALUES (1, 'Dup', 1, 'M', 'available');
INSERT INTO animal (name, species_id, sex, status, chip_number) VALUES ('Copy', 1, 'M', 'available', '985100001');
```

<div dir="rtl">

לכל שגיאה: איזה **חוק עסקי** היא שומרת?

---

## 🟡 תרגיל 3 — UPDATE

**א.** Nala יצאה מהסגר — עדכנו אותה ל‑`available`. (לפי **מזהה**, אחרי `SELECT` שמוודא שזו היא.)

**ב.** כל החתולים בלי גזע — עדכנו ל‑`'Mixed'`. **כמה שורות השתנו? למה לא 3?**

**ג.** ליאור בר עבר לחיפה... רגע, הוא כבר גר בחיפה. הריצו את העדכון בכל זאת. מה מחזיר `changes()`? מה זה מלמד?

**ד.** חשבונות החשמל (`utilities`) נרשמו בלי מע"מ. הוסיפו 18% לכולם. מה הסכום החדש של כל הוצאות החשמל?

**ה.** ⭐ כתבו `UPDATE` אחד שמעדכן את `status` של **כל** חיה שיש לה אימוץ פעיל (בלי `returned_date`) ל‑`adopted` — **רק אם** היא עדיין לא `adopted`. כמה שורות השתנו? מה זה אומר?

---

## 🟡 תרגיל 4 — DELETE

**א.** נסו למחוק את המין "Parrot" (`species_id = 4`). מה קרה? למה?

**ב.** נסו למחוק את סוג החיסון Myxomatosis (`vaccine_type_id = 5`). מה קרה?

**ג.** מחקו את כל ההוצאות **הכלליות** שלפני אפריל 2024. כמה נמחקו? **לפני** — עשו גיבוי של הטבלה.

**ד.** ⭐ במקום למחוק את Daisy (שמתה) — מה כבר עשו בבסיס הנתונים? בדקו. למה זו הדרך הנכונה?

---

## 🔴 תרגיל 5 — DEFAULT ו‑upsert

**א.** צרו את טבלת `donation` מסעיף 7 במודול, והכניסו שלוש תרומות: אחת עם כל העמודות, אחת בלי תאריך, ואחת בלי תאריך ובלי אמצעי תשלום. הציגו את הטבלה.

**ב.** ⚠️ נסו `INSERT INTO donation DEFAULT VALUES;`. מה קרה ולמה?

**ג.** צרו את טבלת `stock` מסעיף 8 במודול. כתבו upsert שמכניס `('dog food sack', 8)` ו‑`('flea collar', 20)`. מה הכמויות אחרי?

**ד.** ⭐ מחקו את ה‑`PRIMARY KEY` מהגדרת `stock` (צרו אותה מחדש בלי), ונסו את אותו upsert. מה קורה? למה?

---

## 🔴 תרגיל 6 — INSERT … SELECT

**א.** צרו טבלת `adoption_archive` עם המבנה של `adoption` (בלי שורות), והעתיקו אליה את כל האימוצים של 2023.

**ב.** צרו טבלת `vip_adopter (person_id, full_name, adoptions)` ומלאו אותה **בשאילתה אחת** — כל מי שאימץ יותר מפעם אחת. (רמז: `INSERT … SELECT … GROUP BY … HAVING`.)

**ג.** ⭐ **multi-table:** צרו `stray_log (intake_id, animal_id, location)` ו‑`surrender_log (intake_id, animal_id, reason)`, ומלאו את שתיהן מ‑`intake`. כמה שורות בכל אחת? איך זה היה נכתב ב‑Oracle?

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[✅ לפתרונות](solutions.md)**

</div>

</div>


<!-- w3schools:start -->
<div dir="rtl">

---

## 🌐 תרגול נוסף ב‑W3Schools

📖 **לקריאה ב‑W3Schools:** [INSERT](https://www.w3schools.com/sql/sql_insert.asp) · [UPDATE](https://www.w3schools.com/sql/sql_update.asp) · [DELETE](https://www.w3schools.com/sql/sql_delete.asp)

> 💻 הפקודות של השיעור הזה **משנות** נתונים או מבנה, ו‑W3Schools לא מאפשר את זה. קראו שם את ההסבר, ואת התרגול עצמו עשו ב‑OneCompiler, על בסיס הנתונים של המקלט ([הוראות](../../resources/setup.md)).

</div>
<!-- w3schools:end -->

<!-- exam-style:start -->
<div dir="rtl">

---

## 🎓 תרגול בסגנון הבחינה

> 🎓 **תרגול בסגנון הבחינה (שאלון 735911).** הסעיפים כאן כתובים בדיוק כמו בבחינה: `Table.Column`, צירוף עם פסיק ומירכאות כפולות. הם רצים על בסיס הנתונים **חוגי ספורט** ([`clubs.sql`](../../exam-prep/db/clubs.sql)). פתרו על הנייר, ואחר כך טענו את הקובץ ל‑OneCompiler ובדקו.

**ב1.** כתבו שאילתה שמוסיפה את המשתתף: ת"ז 1013, השם "אור גבאי", עיר 6, גיל 15, שנת הצטרפות 2025.

**ב2.** כל חוגי השחייה מתייקרים ב‑20 ש"ח. כתבו את פקודת העדכון. כמה רשומות יתעדכנו?

**ב3.** מה יקרה אם נריץ `DELETE FROM ClubMembers;` **בלי** `WHERE`?


</div>
<!-- exam-style:end -->
