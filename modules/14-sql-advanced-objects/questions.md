<div dir="rtl">

# מודול 29 — שאלות ותשובות

> נסחו תשובה לפני שאתם פותחים.

---

### שאלה 1
**למה צריך Sequence? למה לא `MAX + 1`?**

<details><summary>💡 תשובה</summary>

כי `MAX + 1` **לא בטוח במקביליות**: שני משתמשים שקוראים את ה‑MAX באותו רגע יקבלו את אותו מספר. Sequence מנוהל בתוך בסיס הנתונים ומבטיח שכל בקשה מקבלת מספר **אחר** — גם אם אלף משתמשים מבקשים בו‑זמנית.

</details>

---

### שאלה 2
**מה ההבדל בין `NEXTVAL` ל‑`CURRVAL`?**

<details><summary>💡 תשובה</summary>

`NEXTVAL` **מקדם** את ה‑sequence ומחזיר מספר חדש. `CURRVAL` מחזיר את המספר האחרון ש**הסשן הנוכחי** קיבל, בלי לקדם — כדי להשתמש באותו מזהה בשורה קשורה (למשל: חיה ⟵ הקליטה שלה). `CURRVAL` לפני `NEXTVAL` בסשן — שגיאה.

</details>

---

### שאלה 3
**ב‑SQLite, מה ההבדל בין `INTEGER PRIMARY KEY` ל‑`INTEGER PRIMARY KEY AUTOINCREMENT`?**

<details><summary>💡 תשובה</summary>

שניהם נותנים מספר אוטומטי. בלי `AUTOINCREMENT`, מספר של שורה **שנמחקה** (אם הייתה האחרונה) יכול להינתן שוב לשורה חדשה. עם `AUTOINCREMENT` — לעולם לא; SQLite זוכר את המספר הגבוה ביותר שחולק ב‑`sqlite_sequence`. לטבלאות שהמזהים שלהן "יוצאים החוצה" (קבלות, מספרי תיק) — `AUTOINCREMENT`.

</details>

---

### שאלה 4
**האם Sequence מבטיח מספרים רציפים בלי חורים?**

<details><summary>💡 תשובה</summary>

**לא.** אם `INSERT` נכשל או בוטל, המספר שנלקח לא חוזר. עם `CACHE`, הפעלה מחדש של השרת "מדלגת" על מספרים. Sequence מבטיח **ייחודיות**, לא **רציפות**.

</details>

---

### שאלה 5
**מה זה אינדקס? האם הוא משנה את התוצאה של שאילתה?**

<details><summary>💡 תשובה</summary>

מבנה נתונים נוסף (בדרך כלל B‑tree) שמחזיק את ערכי העמודה **ממוינים**, עם הפניה לשורה. מאפשר לקפוץ ישר לשורות מתאימות (`SEARCH`) במקום לסרוק הכול (`SCAN`).

**לא משנה את התוצאה** — רק את המהירות. לכן אפשר להוסיף ולהסיר אינדקסים בלי לשנות קוד.

</details>

---

### שאלה 6
**אילו אינדקסים נוצרים אוטומטית, ואילו לא?**

<details><summary>💡 תשובה</summary>

**אוטומטית:** על `PRIMARY KEY` ועל `UNIQUE` — כי צריך לבדוק כפילויות מהר.
**לא אוטומטית:** על **מפתחות זרים** — למרות שכמעט כל JOIN עובר דרכם. לכן כלל אצבע: ליצור אינדקס על כל מפתח זר.

</details>

---

### שאלה 7
**יש אינדקס על `name`. למה `WHERE UPPER(name) = 'LUNA'` עדיין סורק את כל הטבלה?**

<details><summary>💡 תשובה</summary>

כי האינדקס ממוין לפי `name`, ולא לפי `UPPER(name)`. כדי להשוות, בסיס הנתונים חייב לחשב `UPPER` לכל שורה. **פתרונות:** אינדקס על הביטוי — `CREATE INDEX … ON animal(UPPER(name))`; או לשמור את הערך מנורמל מראש.

</details>

---

### שאלה 8
**מה המחיר של אינדקס? למה לא לאנדקס כל עמודה?**

<details><summary>💡 תשובה</summary>

1. **מקום בדיסק** — עותק ממוין של העמודה.
2. **כתיבה איטית יותר** — כל `INSERT` / `UPDATE` / `DELETE` מעדכן גם את כל האינדקסים על הטבלה.
3. **לא תמיד עוזר** — בעמודה עם מעט ערכים שונים (`sex`) או בטבלה קטנה, הסריקה מהירה באותה מידה.

</details>

---

### שאלה 9
**מה זה Synonym, ולמה הוא קיים ב‑Oracle ולא ב‑SQLite?**

<details><summary>💡 תשובה</summary>

שם נוסף לאובייקט — לרוב לטבלה מ**סכמה של משתמש אחר**: `CREATE SYNONYM animal FOR shelter.animal`. חוסך לכתוב `shelter.` בכל שאילתה, ומאפשר להעביר את הטבלה בלי לשנות קוד.

ב‑Oracle יש משתמשים וסכמות — כל משתמש "מחזיק" אובייקטים משלו. SQLite הוא קובץ אחד בלי משתמשים — אין סכמות, ולכן אין צורך ב‑synonyms.

</details>

---

### שאלה 10 (ראיון)
**מה לא בסדר? מצאו שלוש טעויות.**

</div>

```sql
SELECT name, COUNT(*)
FROM   animal a
JOIN   vaccination v ON v.animal_id = a.animal_id
WHERE  COUNT(*) > 2;
```

<details><summary>💡 תשובה</summary>

<div dir="rtl">

1. פונקציה מצרפית ב‑`WHERE` ⟵ `HAVING`.
2. חסר `GROUP BY` (לכל חיה).
3. `name` — עמודה רגילה ליד מצרפית בלי קיבוץ, ובלי כינוי.

</div>

```sql
SELECT a.name, COUNT(*)
FROM   animal a
JOIN   vaccination v ON v.animal_id = a.animal_id
GROUP  BY a.animal_id
HAVING COUNT(*) > 2;
```

</details>

<div dir="rtl">

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[✏️ לתרגילים](exercises.md)**

</div>

</div>
