<div dir="rtl">

# מודול 26 — שאלות ותשובות

> נסחו תשובה לפני שאתם פותחים.

---

### שאלה 1
**מה ההבדל בין DDL ל‑DML?**

<details><summary>💡 תשובה</summary>

**DDL** (`CREATE`, `ALTER`, `DROP`) משנה את **המבנה** — טבלאות ועמודות. **DML** (`INSERT`, `UPDATE`, `DELETE`) משנה את **השורות** שבתוך הטבלאות. DDL קורה לעיתים רחוקות; DML — כל הזמן.

</details>

---

### שאלה 2
**איך מתרגמים כל סימן ב‑ERD ל‑`CREATE TABLE`?**

<details><summary>💡 תשובה</summary>

| ב‑ERD | ב‑SQL |
|-------|-------|
| ישות | `CREATE TABLE` |
| מאפיין | עמודה עם טיפוס |
| `#` מזהה | `PRIMARY KEY` |
| `*` חובה | `NOT NULL` |
| `o` אופציונלי | בלי `NOT NULL` |
| יחס 1:רבים | `REFERENCES` בצד ה"רבים" |
| רבים:רבים | טבלת קישור עם שני מפתחות זרים |

</details>

---

### שאלה 3
**למה מספר טלפון נשמר כטקסט ולא כמספר?**

<details><summary>💡 תשובה</summary>

כי **לא עושים עליו חשבון**, ובשמירה כמספר הוא נפגע: `052-1111111` ⟵ ה‑0 המוביל נעלם, המקף אסור. אותו דין לת"ז, מיקוד ומספר שבב. **השאלה: האם יש היגיון לחבר שני ערכים כאלה?** אם לא — טקסט.

</details>

---

### שאלה 4
**מה זה type affinity ב‑SQLite, ומה עושה `STRICT`?**

<details><summary>💡 תשובה</summary>

ב‑SQLite הטיפוס של עמודה הוא **המלצה**: הוא מנסה להמיר ערך לטיפוס, ואם לא מצליח — שומר אותו כמו שהוא. כך `'abc'` יכול להישמר בעמודת `INTEGER`. **`STRICT`** בסוף `CREATE TABLE` הופך את הטיפוס **לחוק**: ערך שלא מתאים ⟵ שגיאה, כמו ב‑Oracle.

</details>

---

### שאלה 5
**למה אי אפשר להוסיף עמודה `NOT NULL` בלי `DEFAULT` לטבלה שיש בה נתונים?**

<details><summary>💡 תשובה</summary>

כי כל השורות הקיימות צריכות לקבל ערך בעמודה החדשה. בלי `DEFAULT` הערך יהיה NULL — וזה בדיוק מה ש‑`NOT NULL` אוסר. בטבלה **ריקה** זה עובד (אין שורות למלא).

</details>

---

### שאלה 6
**מה ההבדל בין `DELETE FROM t`, `TRUNCATE TABLE t` ו‑`DROP TABLE t`?**

<details><summary>💡 תשובה</summary>

| | השורות | הטבלה | `WHERE` | `ROLLBACK` (Oracle) |
|---|---|---|---|---|
| `DELETE` | נמחקות | נשארת | ✅ | ✅ |
| `TRUNCATE` | נמחקות (מהר) | נשארת | ❌ | ❌ |
| `DROP` | נמחקות | **נמחקת** | ❌ | ❌ |

ב‑SQLite אין `TRUNCATE` — משתמשים ב‑`DELETE`.

</details>

---

### שאלה 7
**מה `CREATE TABLE copy AS SELECT * FROM animal` מעתיק, ומה לא?**

<details><summary>💡 תשובה</summary>

**מעתיק:** שמות עמודות, טיפוסים (בערך), ונתונים. **לא מעתיק:** `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `CHECK`, `REFERENCES`, `DEFAULT`. טוב לגיבוי מהיר ולניסויים — לא לטבלה שמשתמשים בה באמת.

</details>

---

### שאלה 8
**למה בראש `shelter.sql` הטבלאות נמחקות דווקא בסדר `expense` … `species`?**

<details><summary>💡 תשובה</summary>

כי מפתחות זרים חוסמים מחיקה של טבלה ש**אחרים מצביעים עליה**. `species` היא "הורה" של `animal`, ו‑`animal` היא הורה של `expense`. מוחקים **קודם את הילדים**, אחר כך את ההורים — הסדר **ההפוך** ליצירה.

</details>

---

### שאלה 9
**איך יודעים אילו טבלאות ועמודות קיימות בבסיס הנתונים?**

<details><summary>💡 תשובה</summary>

שואלים את **מילון הנתונים**:
- SQLite: `SELECT name FROM sqlite_master WHERE type = 'table';` ו‑`PRAGMA table_info(t);`
- Oracle: `SELECT table_name FROM user_tables;`, `user_tab_columns`, או `DESCRIBE t`.

</details>

---

### שאלה 10
**ב‑Oracle הרצתי `DELETE FROM animal;` ואחריו `CREATE TABLE test (x NUMBER);`. אחר כך `ROLLBACK`. האם החיות חזרו?**

<details><summary>💡 תשובה</summary>

**לא.** ב‑Oracle כל פקודת DDL מבצעת `COMMIT` **אוטומטי** — לפני ואחרי. ה‑`CREATE TABLE` אישר את ה‑`DELETE`, ו‑`ROLLBACK` כבר לא יכול לבטל אותו. **לעולם אל תריצו DDL באמצע עבודה שאולי תרצו לבטל.** (מודול 32.)

</details>

---

<div align="center">

**[⬅️ חזרה למודול](README.md)** · **[✏️ לתרגילים](exercises.md)**

</div>

</div>
