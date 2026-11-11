<div dir="rtl">

# נושא 5 — פונקציות ב‑SQL: מצרפיות (`COUNT`, `AVG`, `MAX`) וסקלריות · מדריך למורה

> **בבחינה: שאלות חובה בכל חלק בסיסי הנתונים** · **זמן מוערך: 40 דקות** · **בסיס הנתונים:** `school.sql`
>
> נושא קריטי שבו תלמידים נוטים לאבד נקודות בגלל מלכודות קלאסיות: ההבדל בין `COUNT(*)` ל‑`COUNT(עמודה)`, שימוש בפונקציה מצרפית ב‑`WHERE` (שגיאה נפוצה!), והתנהגות מול `NULL`.

---

## 🎯 מה התלמידים צריכים לדעת בסוף הנושא

- חמש הפונקציות המצרפיות: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`
- שלושת סוגי ה‑`COUNT`: `COUNT(*)`, `COUNT(עמודה)`, `COUNT(DISTINCT עמודה)`
- התעלמות מ‑`NULL` בפונקציות מצרפיות (מדוע `AVG` ו‑`COUNT(col)` מתעלמים)
- **כלל הברזל:** מדוע אסור לשים פונקציה מצרפית ב‑`WHERE` ואיך משתמשים בתת‑שאילתה
- פונקציות סקלריות: `ROUND`, `LENGTH`, `UPPER`, `LOWER`, `COALESCE`

---

## 🧠 ההסבר — מה להגיד, ובאיזה סדר

### 1. ההבדל בין פונקציית שורה לפונקציית קיבוץ

*"עד עכשיו, כל שורה שנכנסה ל‑SELECT יצאה כתוצאה. פונקציה מצרפית מקבלת עמודה שלמה ומחזירה **ערך יחיד** לכל הטבלה."*

</div>

```sql
SELECT COUNT(*) AS NumTeachers,
       AVG(Salary) AS AvgSalary,
       MIN(Salary) AS MinSalary,
       MAX(Salary) AS MaxSalary
FROM Teachers;
```

```text
NumTeachers | AvgSalary        | MinSalary | MaxSalary
7           | 12442.8571428571 | 9800      | 15300
```

<div dir="rtl">

### 2. המלכודת הגדולה: שלושת סוגי `COUNT`

הדגישו בפני התלמידים:
- `COUNT(*)` — סופר את **כל** השורות בטבלה.
- `COUNT(Phone)` — סופר רק שורות שיש בהן טלפון (מדלג על `NULL`). מתוך 7 מורים, רק ל‑5 יש טלפון. התוצאה: **5**.
- `COUNT(DISTINCT CityCode)` — סופר כמה ערים **שונות** קיימות בטבלה.

</div>

```sql
SELECT COUNT(*) AS AllRows,
       COUNT(Phone) AS WithPhone,
       COUNT(DISTINCT CityCode) AS DistinctCities
FROM Teachers;
```

```text
AllRows | WithPhone | DistinctCities
7       | 5         | 4
```

<div dir="rtl">

### 3. שגיאת הבחינה הנפוצה ביותר: פונקציה מצרפית ב‑WHERE

שאלו את הכיתה: *"איך נשלוף מורים שמרוויחים מעל הממוצע?"*
תלמידים רבים יכתבו מיד:
`SELECT FirstName FROM Teachers WHERE Salary > AVG(Salary);` ❌

**הסבירו למה זה שגוי:**
`WHERE` רץ בזמן שהטבלה נקראת שורה אחר שורה. באותו רגע הממוצע הכללי עדיין אינו ידוע למנוע מסד הנתונים!
**הדרך הנכונה — תת‑שאילתה:**

</div>

```sql
SELECT FirstName, LastName, Salary
FROM Teachers
WHERE Salary > (SELECT AVG(Salary) FROM Teachers);
```

<div dir="rtl">

---

## ❓ שאלות פתוחות להקרנה ולדיון בכיתה

**1. אם בטבלה של 100 תלמידים יש 10 תלמידים ללא מספר טלפון (ערך NULL), מה יחזיר `COUNT(Phone)` ומה יחזיר `COUNT(*)`?**
<details><summary>💡 תשובה</summary>
`COUNT(*)` יחזיר 100 (כל השורות). `COUNT(Phone)` יחזיר 90 (מדלג על 10 ערכי ה‑NULL).
</details>

**2. האם השאילתה הבאה תקינה? `SELECT FirstName, MAX(Salary) FROM Teachers;`**
<details><summary>💡 תשובה</summary>
לא תקינה ב‑SQL תקני (או מחזירה שורה שרירותית). אי אפשר להציב עמודה רגילה לצד פונקציה מצרפית ללא `GROUP BY`, כי MAX מחזיר שורה אחת ו‑FirstName מחזיר 7 שמות שונים.
</details>

---

## 🔘 שאלות רב-ברירה להקרנה

### שאלה 1: תוצאת COUNT על עמודה עם NULL
נתונה הטבלה Teachers (7 מורים, מתוכם ל‑2 מורים אין טלפון). מה יחזיר הביטוי הבא?
```sql
SELECT COUNT(*) - COUNT(Phone) FROM Teachers;
```
א. 0  
ב. 2  
ג. 5  
ד. שגיאת תחביר  

<details><summary>💡 תשובה והסבר</summary>
**התשובה הנכונה: ב (2).**  
`COUNT(*)` מחזיר 7. `COUNT(Phone)` מדלג על ערכי ה‑NULL ומחזיר 5. ההפרש ביניהם הוא 2 — בדיוק מספר השורות שבהן הטלפון ריק.
</details>

---

### שאלה 2: זיהוי השאילתה התקינה
רוצים לשלוף את שמות התלמידים שקיבלו ציון גבוה מהציון הממוצע של כל בית הספר. איזו שאילתה כתובה נכון?

א. `SELECT StudentId FROM Grades WHERE Grade > AVG(Grade);`  
ב. `SELECT StudentId FROM Grades HAVING Grade > AVG(Grade);`  
ג. `SELECT StudentId FROM Grades WHERE Grade > (SELECT AVG(Grade) FROM Grades);`  
ד. `SELECT StudentId, AVG(Grade) FROM Grades WHERE Grade > AVG(Grade);`  

<details><summary>💡 תשובה והסבר</summary>
**התשובה הנכונה: ג.**  
אסור להשתמש ב‑`AVG` בתוך פסוקית `WHERE` ישירה. תנאי על פונקציה מצרפית ביחס לכלל הטבלה מתבצע באמצעות תת‑שאילתה בסוגריים.
</details>

---

### שאלה 3: עיגול ומחרוזות
מה תפקיד הפונקציה `ROUND(AVG(Salary), 2)`?  
א. סופרת 2 משכורות  
ב. מעגלת את ממוצע השכר ל‑2 ספרות אחרי הנקודה העשרונית  
ג. מחזירה את שתי המשכורות הגבוהות ביותר  
ד. מכפילה את הממוצע ב‑2  

<details><summary>💡 תשובה והסבר</summary>
**התשובה הנכונה: ב.**  
הפונקציה `ROUND(מספר, d)` מעגלת את המספר ל‑d ספרות מימין לנקודה.
</details>

---

## ⏱️ תרגיל כתיבה בכיתה (5 דקות)

כתבו שאילתה שמציגה את הציון הממוצע בבית הספר (`AvgGrade`) מעוגל לשלם (`ROUND`), את הציון הנמוך ביותר (`MinGrade`), ואת הציון הגבוה ביותר (`MaxGrade`) מתוך הטבלה `Grades`.

<details><summary>💡 פתרון</summary>

```sql
SELECT ROUND(AVG(Grade)) AS AvgGrade,
       MIN(Grade)        AS MinGrade,
       MAX(Grade)        AS MaxGrade
FROM Grades;
```
**פלט:** `AvgGrade = 78`, `MinGrade = 39`, `MaxGrade = 100`.
</details>

</div>
