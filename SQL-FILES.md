<div dir="rtl">

# 📋 קובצי ה‑SQL של הקורס: להעתיק ולהדביק

> כל בסיסי הנתונים של הקורס נמצאים בדף הזה. **בוחרים קובץ, מעתיקים את כולו, ומדביקים ב‑[OneCompiler (SQLite)](https://onecompiler.com/sqlite).**

---

## איך מעתיקים קובץ שלם (שתי לחיצות)

**דרך א' (הכי קלה):** לוחצים על **"פתיחה להעתקה"** ליד הקובץ. נפתח דף שיש בו רק את הקוד. לוחצים `Ctrl+A` (בוחר הכול) ואז `Ctrl+C` (מעתיק).

**דרך ב':** לוחצים על **שם הקובץ**. בדף שנפתח, למעלה מימין מעל הקוד, יש כפתור של שני ריבועים (**Copy raw file**). לוחצים עליו, וכל הקובץ מועתק.

**ואז, ב‑OneCompiler:**
1. פותחים את [onecompiler.com/sqlite](https://onecompiler.com/sqlite).
2. בחלון השמאלי לוחצים `Ctrl+A` ואז `Delete`, כדי למחוק את הדוגמה.
3. מדביקים עם `Ctrl+V`.
4. **מתחת** לקוד שהדבקתם כותבים את השאילתה שלכם, ולוחצים **Run**.

> 💡 **שאילתות מתוך השיעורים:** בכל דף של שיעור כאן ב‑GitHub, כשמעבירים את העכבר מעל קטע קוד, מופיע בפינה שלו כפתור העתקה (📋).

---

## בסיסי הנתונים

| הקובץ | מה יש בו | מתי משתמשים בו | העתקה |
|-------|----------|-----------------|-------|
| [`shelter.sql`](resources/shelter-db/shelter.sql) | 🐾 מקלט בעלי החיים "בית חם": 8 טבלאות, 20 חיות | רוב השיעורים (2–17) | [פתיחה להעתקה](https://raw.githubusercontent.com/AhmadKais/sql-course-heb/main/resources/shelter-db/shelter.sql) |
| [`school.sql`](resources/school-db/school.sql) | 🏫 בית הספר "עתיד": 7 טבלאות, 18 תלמידים · גם [כל הפקודות בדף אחד](resources/school-db/README.md#-כל-הפקודות-להעתקה) | קטע **💪 תרגול בכיתה** בסוף התרגילים של כל שיעור SQL | [פתיחה להעתקה](https://raw.githubusercontent.com/AhmadKais/sql-course-heb/main/resources/school-db/school.sql) |
| [`clubs.sql`](exam-prep/db/clubs.sql) | ⚽ חוגי ספורט עירוניים: 5 טבלאות | בחינה לדוגמה 1, ו"🎓 תרגול בסגנון הבחינה" בסוף התרגילים של כל שיעור | [פתיחה להעתקה](https://raw.githubusercontent.com/AhmadKais/sql-course-heb/main/exam-prep/db/clubs.sql) |
| [`library.sql`](exam-prep/db/library.sql) | 📚 ספרייה עירונית: 5 טבלאות | בחינה לדוגמה 2 | [פתיחה להעתקה](https://raw.githubusercontent.com/AhmadKais/sql-course-heb/main/exam-prep/db/library.sql) |
| [`games.sql`](exam-prep/db/games.sql) | 🎮 חנות משחקי מחשב: 5 טבלאות | בחינה לדוגמה 3 | [פתיחה להעתקה](https://raw.githubusercontent.com/AhmadKais/sql-course-heb/main/exam-prep/db/games.sql) |

**איך יודעים שהכול נטען?** אחרי Run, הדבר הראשון שמופיע ב‑**Output** הוא מספר:

| הקובץ | מה צריך להופיע |
|-------|-----------------|
| `shelter.sql` | `animals_loaded = 20` |
| `school.sql` | `students_loaded = 18` |
| `clubs.sql` | `members_loaded = 12` |
| `library.sql` | `loans_loaded = 14` |
| `games.sql` | `orders_loaded = 13` |

---

## ⚠️ שלושה דברים שחשוב לזכור

1. **כל Run מתחיל מההתחלה.** הקובץ מוחק את הטבלאות ובונה אותן מחדש. לכן אחרי `DELETE` או `UPDATE` אפשר פשוט ללחוץ Run שוב, ולקבל בסיס נתונים נקי.
2. **האתר לא שומר את העבודה שלכם.** שמרו את השאילתות שכתבתם בקובץ אצלכם במחשב.
3. **ב‑W3Schools הקבצים האלה לא עובדים.** W3Schools מיועד לקריאת ההסברים ולתרגול על בסיס הנתונים שלו. הסבר מלא נמצא ב[מדריך סביבת העבודה](resources/setup.md).

</div>
