<div dir="rtl">

# שיעור 6 — פתרונות

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../05-row-functions/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../07-group-by-having/solutions.md)

> ⚠️ קודם נסו לבד! כל תוצאה כאן היא פלט אמיתי של SQLite. בפקודות שמשנות נתונים כל תרגיל רץ על בסיס נתונים טרי.

</div>

<div dir="rtl">

---

## ❓ שאלות: מה תחזיר השאילתה?

</div>

<div dir="rtl">

### שאלה 1

</div>

```sql
SELECT COUNT(*), COUNT(TeacherPhone), COUNT(DISTINCT TeachInst)
FROM   Teachers;
```

<div dir="rtl">

| COUNT(*) | COUNT(TeacherPhone) | COUNT(DISTINCT TeachInst) |
|---|---|---|
| 6 | 4 | 5 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### שאלה 2

</div>

```sql
SELECT COUNT(*)
FROM   Registrations
WHERE  RegTeacher = 3;
```

<div dir="rtl">

| COUNT(*) |
|---|
| 3 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### שאלה 3

</div>

```sql
SELECT MAX(BirthYear) - MIN(BirthYear) AS Diff
FROM   Pupils;
```

<div dir="rtl">

| Diff |
|---|
| 5 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

---

## ✏️ תרגילים — 🎵 בית הספר למוזיקה "צלילים"

</div>

<div dir="rtl">

### 1. 🟢 כמה תלמידים יש בבית הספר?

</div>

```sql
SELECT COUNT(*) AS Pupils
FROM   Pupils;
```

<div dir="rtl">

| Pupils |
|---|
| 10 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 2. 🟢 מה התשלום החודשי הגבוה ביותר ברישומים?

</div>

```sql
SELECT MAX(MonthlyFee) AS MaxFee
FROM   Registrations;
```

<div dir="rtl">

| MaxFee |
|---|
| 400 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 3. 🟢 מה שנת הלידה של התלמיד המבוגר ביותר?

</div>

```sql
SELECT MIN(BirthYear) AS Oldest
FROM   Pupils;
```

<div dir="rtl">

| Oldest |
|---|
| 2009 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 4. 🟢 מה הסכום של כל התשלומים החודשיים?

</div>

```sql
SELECT SUM(MonthlyFee) AS Total
FROM   Registrations;
```

<div dir="rtl">

| Total |
|---|
| 4630 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 5. 🟡 כמה מורים **אין** להם טלפון? (שתי דרכים: עם `WHERE ... IS NULL`, או `COUNT(*) - COUNT(TeacherPhone)`)

</div>

```sql
SELECT COUNT(*) AS NoPhone
FROM   Teachers
WHERE  TeacherPhone IS NULL;
```

<div dir="rtl">

| NoPhone |
|---|
| 2 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 6. 🟡 מה התשלום הממוצע של תלמידים מתחילים? עגלו ל‑2 ספרות.

</div>

```sql
SELECT ROUND(AVG(MonthlyFee), 2) AS AvgBeginner
FROM   Registrations
WHERE  PupilLevel = 'מתחיל';
```

<div dir="rtl">

| AvgBeginner |
|---|
| 338.0 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 7. 🟡 כמה תלמידים **שונים** רשומים לשיעורים? (תלמיד יכול להופיע פעמיים ברישומים)

</div>

```sql
SELECT COUNT(DISTINCT RegPupil) AS RegisteredPupils
FROM   Registrations;
```

<div dir="rtl">

| RegisteredPupils |
|---|
| 10 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 8. 🟡 כמה רישומים יש למורה 5, ומה סכום התשלומים שלהם?

</div>

```sql
SELECT COUNT(*) AS Regs, SUM(MonthlyFee) AS Total
FROM   Registrations
WHERE  RegTeacher = 5;
```

<div dir="rtl">

| Regs | Total |
|---|---|
| 3 | 860 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 9. 🔴 מה ההפרש בין המחיר היקר ביותר לזול ביותר לשעה?

</div>

```sql
SELECT MAX(HourRate) - MIN(HourRate) AS Gap
FROM   Teachers;
```

<div dir="rtl">

| Gap |
|---|
| 50 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 10. 🔴 כמה תלמידים נולדו בין 2010 ל‑2012, ומה שנת הלידה הממוצעת שלהם?

</div>

```sql
SELECT COUNT(*) AS Pupils, AVG(BirthYear) AS AvgYear
FROM   Pupils
WHERE  BirthYear BETWEEN 2010 AND 2012;
```

<div dir="rtl">

| Pupils | AvgYear |
|---|---|
| 6 | 2011.0 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 11. 🔴 מה ההכנסה השנתית הכוללת (12 חודשים) מכל הרישומים?

</div>

```sql
SELECT SUM(MonthlyFee * 12) AS YearIncome
FROM   Registrations;
```

<div dir="rtl">

| YearIncome |
|---|
| 55560 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

---

## 🏠 תרגול נוסף — 🏫 בית הספר "עתיד"

</div>

<div dir="rtl">

### 1. 🟢 כמה תלמידים יש, וכמה מהם רשמו טלפון?

</div>

```sql
SELECT COUNT(*) AS AllStudents, COUNT(Phone) AS WithPhone
FROM   Students;
```

<div dir="rtl">

| AllStudents | WithPhone |
|---|---|
| 18 | 12 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 2. 🟢 מה השכר הממוצע של המורים?

</div>

```sql
SELECT AVG(Salary) AS AvgSalary
FROM   Teachers;
```

<div dir="rtl">

| AvgSalary |
|---|
| 12442.9 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 3. 🟡 מה הציון הגבוה, הנמוך והממוצע (מעוגל) במקצוע 11, מחצית 1?

</div>

```sql
SELECT MAX(Grade) AS Hi, MIN(Grade) AS Lo, ROUND(AVG(Grade), 1) AS Avg
FROM   Grades
WHERE  CourseCode = 11 AND Term = 1;
```

<div dir="rtl">

| Hi | Lo | Avg |
|---|---|---|
| 100 | 65 | 85.3 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 4. 🟡 כמה היעדרויות לא מאושרות יש?

</div>

```sql
SELECT COUNT(*) AS NotExcused
FROM   Absences
WHERE  Excused = 0;
```

<div dir="rtl">

| NotExcused |
|---|
| 9 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 5. 🔴 בכמה מקצועות שונים יש ציונים בטבלת הציונים?

</div>

```sql
SELECT COUNT(DISTINCT CourseCode) AS Courses
FROM   Grades;
```

<div dir="rtl">

| Courses |
|---|
| 7 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 6. 🔴 כמה ציונים חסרים (NULL) יש בטבלת הציונים? כתבו עם `COUNT(*) - COUNT(Grade)`.

</div>

```sql
SELECT COUNT(*) - COUNT(Grade) AS Missing
FROM   Grades;
```

<div dir="rtl">

| Missing |
|---|
| 2 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../05-row-functions/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../07-group-by-having/solutions.md)

</div>
