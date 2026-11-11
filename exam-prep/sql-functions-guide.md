<div dir="rtl">

# 🧮 מדריך ותרגול פונקציות ב‑SQL: מצרפיות (קיבוץ) וסקלריות (שורה)

> **מיועד לתלמידי שאלון 735911 (מה"ט / משרד החינוך)**
> 
> בבחינה שואלים שוב ושוב על פונקציות: **`COUNT`**, **`MAX`**, **`AVG`**, **`MIN`**, **`SUM`**, שילובן עם **`WHERE`** ועם **`HAVING`**, וכן פונקציות מחרוזת, מספר וטיפול ב‑NULL.
> 
> הדף הזה מסביר בדיוק איך כל פונקציה עובדת, מה ההבדל בין הסוגים, ממה צריך להיזהר בבחינה, וכולל **25 תרגילי פונקציות ממוקדים עם פתרונות מלאים**.

---

## 🗺️ תוכן העניינים

1. [ההבדל בין שני סוגי הפונקציות](#1-ההבדל-בין-שני-סוגי-הפונקציות)
2. [חמש פונקציות הקיבוץ (Aggregate Functions)](#2-חמש-פונקציות-הקיבוץ-aggregate-functions)
   - [`COUNT` — שלושת הסוגים](#count--שלושת-הסוגים)
   - [`SUM` ו‑`AVG` — חישובים והתנהגות עם NULL](#sum-וavg--חישובים-והתנהגות-עם-null)
   - [`MIN` ו‑`MAX` — הקטן והגדול ביותר](#min-וmax--הקטן-והגדול-ביותר)
3. [כללי ברזל לבחינה: היכן מותר והיכן אסור להשתמש?](#3-כללי-ברזל-לבחינה-היכן-מותר-והיכן-אסור-להשתמש)
   - [ההבדל הקריטי בין `WHERE` לבין `HAVING`](#ההבדל-הקריטי-בין-where-לבין-having)
   - [המלכודת: עמודה רגילה ליד פונקציה מצרפית](#המלכודת-עמודה-רגילה-ליד-פונקציה-מצרפית)
   - [הטעות הנפוצה ביותר: פונקציה מצרפית ב‑WHERE](#הטעות-הנפוצה-ביותר-פונקציה-מצרפית-בwhere)
4. [פונקציות שורה / סקלריות (Scalar Functions)](#4-פונקציות-שורה--סקלריות-scalar-functions)
   - [מחרוזות: `UPPER`, `LOWER`, `LENGTH`, `SUBSTR`, `||`](#מחרוזות-טקסט)
   - [מספרים: `ROUND`, `ABS`, חישובים אריתמטיים](#מספרים-וחשבון)
   - [טיפול ב‑NULL: `COALESCE`, `IFNULL`, `CASE`](#טיפול-בnull-ותנאים)
5. [טבלת עזר מהירה לבחינה](#5-טבלת-עזר-מהירה-לבחינה)
6. [תרגול מעשי ממוקד: 25 שאלות](#6-תרגול-מעשי-ממוקד-25-שאלות)
7. [פתרונות מלאים עם הסברים](#7-פתרונות-מלאים-עם-הסברים)

---

## 1. ההבדל בין שני סוגי הפונקציות

ב‑SQL יש שני סוגים עיקריים של פונקציות:

```text
פונקציית שורה (סקלרית)                      פונקציית קיבוץ (מצרפית)
פועלת על כל שורה בנפרד                     פועלת על קבוצת שורות ומחזירה ערך יחיד

   שורה 1: "אדם"    -> LENGTH -> 3               שורה 1: 320 \
   שורה 2: "כרים"   -> LENGTH -> 4               שורה 2: 280  -- AVG --> 333.33
   שורה 3: "תמר"    -> LENGTH -> 3               שורה 3: 400 /
   (3 שורות נכנסו -> 3 שורות יצאו)             (3 שורות נכנסו -> ערך 1 יצא!)
```

| מאפיין | פונקציה סקלרית (שורה) | פונקציית קיבוץ (מצרפית) |
|---|---|---|
| **דוגמאות** | `UPPER`, `LOWER`, `LENGTH`, `ROUND`, `SUBSTR` | `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` |
| **כמה שורות חוזרות?** | כמספר השורות שנשלפו | **שורה אחת בלבד** (אלא אם יש `GROUP BY`) |
| **איפה כותבים אותה?** | ב‑`SELECT`, ב‑`WHERE`, ב‑`ORDER BY` | ב‑`SELECT` או ב‑`HAVING` בלבד (אסור ב‑`WHERE`!) |

---

## 2. חמש פונקציות הקיבוץ (Aggregate Functions)

### `COUNT` — שלושת הסוגים

`COUNT` סופרת שורות או ערכים. יש **שלושה אופנים** להשתמש בה, וההבדל ביניהם מופיע כמעט בכל בחינה:

```sql
SELECT COUNT(*)                  AS AllRows,
       COUNT(TeacherPhone)       AS WithPhone,
       COUNT(DISTINCT TeachInst) AS UniqueInstruments
FROM Teachers;
```

תוצאה על בסיס הנתונים `music.sql`:
- **`COUNT(*)`** = **6** (סופר את **כל** השורות בטבלה Teachers, כולל שורות שיש בהן ערכי NULL בעמודות מסוימות).
- **`COUNT(TeacherPhone)`** = **4** (סופר רק שורות שבהן יש ערך ב‑TeacherPhone; שני מורים שאין להם טלפון **אינם נספרים**!).
- **`COUNT(DISTINCT TeachInst)`** = **5** (סופר כמה כלי נגינה **שונים** נלמדים. למרות שיש 6 מורים, שני מורים מלמדים פסנתר (10), ולכן יש 5 כלים ייחודיים).

> [!IMPORTANT]
> **החוק:** `COUNT(*)` סופר שורות. `COUNT(עמודה)` סופר רק שורות שאינן `NULL`. `COUNT(DISTINCT עמודה)` סופר ערכים שונים ללא כפילויות וללא NULL.

---

### `SUM` ו‑`AVG` — חישובים והתנהגות עם NULL

- **`SUM(עמודה)`**: מחשב את סכום כל המספרים בעמודה.
- **`AVG(עמודה)`**: מחשב את הממוצע החשבוני של הערכים.

```sql
SELECT SUM(HourRate) AS TotalRate,
       AVG(HourRate) AS AvgRate
FROM Teachers;
```
- סכום התעריפים: `120 + 150 + 110 + 140 + 100 + 130 = 750`.
- ממוצע: `750 / 6 = 125.0`.

#### התנהגות מול NULL:
פונקציות אלו **מתעלמות לחלוטין מ‑NULL**.
אם נחשב ממוצע על עמודה שיש בה NULL: המכנה הוא מספר השורות **שיש בהן ערך מספרי**, ולא סך כל השורות בטבלה!

---

### `MIN` ו‑`MAX` — הקטן והגדול ביותר

- **`MIN(עמודה)`**: הערך הקטן ביותר.
- **`MAX(עמודה)`**: הערך הגדול ביותר.

עובדות לא רק על מספרים אלא גם על:
- **תאריכים ושנים:** `MIN(RegYear)` הוא הרישום הישן ביותר, `MAX(RegYear)` הוא הרישום החדש ביותר.
- **טקסט:** לפי סדר אלפביתי א-ב (בטקסט עברי `MIN` יהיה שם המתחיל באות א', ו‑`MAX` שם המתחיל באות ת').

```sql
SELECT MIN(HourRate) AS MinRate,
       MAX(HourRate) AS MaxRate,
       MIN(RegYear)  AS FirstYear,
       MAX(RegYear)  AS LastYear
FROM Registrations, Teachers;
```

---

## 3. כללי ברזל לבחינה: היכן מותר והיכן אסור להשתמש?

### ההבדל הקריטי בין `WHERE` לבין `HAVING`

זוהי אחת משאלות המפתח הנפוצות ביותר במבחן:

| מאפיין | `WHERE` | `HAVING` |
|---|---|---|
| **על מה התנאי פועל?** | על **שורה בודדת** | על **קבוצה / תוצאת פונקציה מצרפית** |
| **מתי הוא מתבצע?** | **לפני** הקיבוץ וחישוב הפונקציות | **אחרי** הקיבוץ וחישוב הפונקציות |
| **האם מותר לכתוב פונקציה מצרפית?** | ❌ **אסור בהחלט!** (`WHERE AVG(...)` זו שגיאה) | ✅ **מותר ומיועד לכך!** (`HAVING AVG(...) > 300`) |

#### דוגמה להשוואה:
הציגו לכל מורה (RegTeacher) את ממוצע התשלומים החודשיים, **אך ורק לרישומים משנת 2024 ואילך**, ורק למורים שהממוצע שלהם **עולה על 310 ש"ח**:

```sql
SELECT RegTeacher, AVG(MonthlyFee) AS AvgFee
FROM Registrations
WHERE RegYear >= 2024       -- סינון שורות: רק רישומים מ-2024 (מתבצע קודם!)
GROUP BY RegTeacher
HAVING AVG(MonthlyFee) > 310; -- סינון קבוצות: רק מורים עם ממוצע > 310 (מתבצע בסוף!)
```

---

### המלכודת: עמודה רגילה ליד פונקציה מצרפית

האם השאילתה הבאה תקינה?
```sql
-- ❌ שגיאה לוגית נפוצה!
SELECT TeacherName, MAX(HourRate)
FROM Teachers;
```
**מדוע זו מלכודת?**
`MAX(HourRate)` מחזיר ערך מספרי אחד (150). אבל `TeacherName` מכיל 6 שמות! SQL לא יודע איזה שם להצמיד למספר.
ב‑SQL תקני, **אסור לשים עמודה רגילה לצד פונקציה מצרפית**, אלא אם העמודה מופיעה ב‑`GROUP BY`!

**איך מוצאים את שם המורה עם התעריף המקסימלי בצורה נכונה?**
באמצעות **תת‑שאילתה (Subquery)**:
```sql
SELECT TeacherName, HourRate
FROM Teachers
WHERE HourRate = (SELECT MAX(HourRate) FROM Teachers);
```

---

### הטעות הנפוצה ביותר: פונקציה מצרפית ב‑WHERE

> [!CAUTION]
> **לעולם אל תכתבו:**
> `SELECT FirstName FROM Pupils WHERE BirthYear > AVG(BirthYear);` ❌ שגיאת תחביר!
> 
> **הסיבה:** פקודת `WHERE` מסננת שורה‑שורה בזמן שהטבלה נקראת. באותו רגע הממוצע הכללי עדיין אינו ידוע!
> 
> **הדרך הנכונה:**
> `SELECT FirstName FROM Pupils WHERE BirthYear > (SELECT AVG(BirthYear) FROM Pupils);` ✅

---

## 4. פונקציות שורה / סקלריות (Scalar Functions)

פונקציות אלו מעבדות ערך של שורה אחת ומחזירות ערך מעובד.

### מחרוזות (טקסט)

| פונקציה | מה היא עושה | דוגמה | תוצאה |
|---|---|---|---|
| `LENGTH(str)` | סופרת מספר תווים | `LENGTH('ירכא')` | `4` |
| `UPPER(str)` | הופכת אותיות לרישיות (אנגלית) | `UPPER('music')` | `'MUSIC'` |
| `LOWER(str)` | הופכת אותיות לקטנות (אנגלית) | `LOWER('SQL')` | `'sql'` |
| `SUBSTR(str, start, len)` | גוזרת תת‑מחרוזת ממיקום מסוים | `SUBSTR('כרמיאל', 1, 3)` | `'כרמ'` |
| `TRIM(str)` | מנקה רווחים מיותרים מהקצוות | `TRIM('  שלום  ')` | `'שלום'` |
| `REPLACE(str, from, to)` | מחליפה קטע טקסט | `REPLACE('עכו', 'ע', 'א')` | `'אכו'` |
| `str1 || ' ' || str2` | שרשור (חיבור) שתי מחרוזות | `FirstName || ' ' || LastName` | `'אדם חלבי'` |

```sql
-- דוגמה: הצגת שם מלא ומספר תווים בשם
SELECT FirstName || ' ' || LastName AS FullName,
       LENGTH(FirstName) AS NameLen
FROM Pupils
WHERE LENGTH(FirstName) >= 4;
```

---

### מספרים וחשבון

| פונקציה / ביטוי | מה היא עושה | דוגמה | תוצאה |
|---|---|---|---|
| `ROUND(num, d)` | מעגלת מספר ל‑d ספרות אחרי הנקודה | `ROUND(330.666, 1)` | `330.7` |
| `ROUND(num)` | מעגלת למספר שלם קרוב | `ROUND(330.666)` | `331` |
| `ABS(num)` | ערך מוחלט (מסיר סימן שלילי) | `ABS(-50)` | `50` |
| `+`, `-`, `*`, `/` | פעולות חשבון על עמודות | `HourRate * 1.10` | העלאה של 10% |

```sql
-- דוגמה: חישוב תעריף שעה ממוצע מעוגל לספרה אחת
SELECT ROUND(AVG(HourRate), 1) AS RoundedAvgRate
FROM Teachers;
```

---

### טיפול ב‑NULL ותנאים

| פונקציה / תחביר | מה היא עושה | דוגמה |
|---|---|---|
| `COALESCE(val1, val2, ...)` | מחזירה את הערך הראשון שאינו NULL | `COALESCE(TeacherPhone, 'אין טלפון')` |
| `IFNULL(val1, val2)` | זהה ל‑COALESCE עם שני ארגומנטים ב‑SQLite | `IFNULL(TeacherPhone, 'לא צוין')` |
| `CASE WHEN ... THEN ... ELSE ... END` | בדיקת תנאים מתקדמת לפי שורות | יצירת סיווגים מותאמים אישית |

```sql
-- דוגמה: הצגת טלפון עם ערך ברירת מחדל אם ריק
SELECT TeacherName, COALESCE(TeacherPhone, 'אין טלפון') AS Phone
FROM Teachers;

-- דוגמה ל-CASE: חלוקת תעריפי המורים לקבוצות
SELECT TeacherName, HourRate,
       CASE 
           WHEN HourRate >= 140 THEN 'תעריף גבוה'
           WHEN HourRate >= 120 THEN 'תעריף רגיל'
           ELSE 'תעריף מוזל'
       END AS RateCategory
FROM Teachers;
```

---

## 5. טבלת עזר מהירה לבחינה

| משימה נדרשת בשאלה | הפונקציה המתאימה | דוגמת שימוש |
|---|---|---|
| "כמה רשומות/שורות יש..." | `COUNT(*)` | `SELECT COUNT(*) FROM Pupils` |
| "לכמה מורים יש טלפון..." | `COUNT(TeacherPhone)` | `SELECT COUNT(TeacherPhone) FROM Teachers` |
| "בכמה ערים שונות גרים..." | `COUNT(DISTINCT HomeTown)` | `SELECT COUNT(DISTINCT HomeTown) FROM Pupils` |
| "מהו התשלום החודשי הממוצע..." | `AVG(MonthlyFee)` | `SELECT AVG(MonthlyFee) FROM Registrations` |
| "מהו סך כל התשלומים..." | `SUM(MonthlyFee)` | `SELECT SUM(MonthlyFee) FROM Registrations` |
| "מהו התעריף היקר ביותר..." | `MAX(HourRate)` | `SELECT MAX(HourRate) FROM Teachers` |
| "מהו שנת הלידה של התלמיד המבוגר ביותר..." | `MIN(BirthYear)` (שנה קטנה = מבוגר יותר!) | `SELECT MIN(BirthYear) FROM Pupils` |
| "עיגול הממוצע ל‑2 ספרות..." | `ROUND(AVG(...), 2)` | `SELECT ROUND(AVG(MonthlyFee), 2) FROM Registrations` |
| "הצגת שמות באותיות גדולות..." | `UPPER(Name)` | `SELECT UPPER(CityName) FROM Cities` |
| "רק קבוצות שיש בהן לפחות 3 תלמידים..." | `HAVING COUNT(*) >= 3` | `GROUP BY RegTeacher HAVING COUNT(*) >= 3` |
| "הצגת המורה היקר ביותר (שם ותעריף)..." | תת‑שאילתה עם `MAX` | `WHERE HourRate = (SELECT MAX(HourRate) FROM Teachers)` |

---

## 6. תרגול מעשי ממוקד: 25 שאלות

כל השאלות רצות על בסיס הנתונים `music.sql`.
סביבת בדיקה: הדביקו את `music.sql` ב‑[OneCompiler SQLite](https://onecompiler.com/sqlite) או ב‑[SQLite Online](https://sqliteonline.com/).

### חלק א': פונקציות קיבוץ בסיסיות (COUNT, SUM, AVG, MIN, MAX)

**שאלה 1 (🟢 קל):**
כתבו שאילתה שמציגה את מספר המורים הכולל בבית הספר תחת הכותרת `TotalTeachers`.

**שאלה 2 (🟢 קל):**
כתבו שאילתה שמציגה את מספר המורים שיש להם מספר טלפון רשום תחת הכותרת `TeachersWithPhone`.

**שאלה 3 (🟢 קל):**
כתבו שאילתה שמציגה את התעריף הנמוך ביותר (`MinRate`) והתעריף הגבוה ביותר (`MaxRate`) לשעה בטבלת Teachers.

**שאלה 4 (🟢 קל):**
כתבו שאילתה שמציגה את סך התשלום החודשי הכולל (`TotalFees`) ואת ממוצע התשלום החודשי (`AvgFee`) מכל הרישומים בטבלת Registrations.

**שאלה 5 (🟢 קל):**
כתבו שאילתה שמציגה את שנת הלידה של התלמיד הצעיר ביותר (`YoungestYear`) ושנת הלידה של התלמיד המבוגר ביותר (`OldestYear`).

**שאלה 6 (🟡 בינוני):**
כתבו שאילתה אחת שמציגה:
- כמה שורות רישום יש בסך הכול (`TotalRegs`)
- כמה תלמידים שונים רשומים (`DistinctPupils`)
- כמה מורים שונים מלמדים תלמידים בפועל (`DistinctTeachers`)

**שאלה 7 (🟡 בינוני):**
כתבו שאילתה שמציגה את מספר התלמידים שגרים בעיר עכו (קוד עיר 2).

**שאלה 8 (🟡 בינוני):**
כתבו שאילתה שמציגה את סך התשלומים החודשיים (`SumFees`) אך ורק עבור רישומים ברמת "מתקדם".

---

### חלק ב': פונקציות סקלריות (מחרוזות, מספרים, עיגול ו-NULL)

**שאלה 9 (🟢 קל):**
כתבו שאילתה שמציגה את שמות הערים (CityName) באותיות ובכותרת `City`, ולצידם את מספר האותיות בכל שם עיר בכותרת `NameLength`.

**שאלה 10 (🟢 קל):**
כתבו שאילתה שמציגה את שם המורה ואת התעריף לשעה לאחר תוספת של 15%, מעוגל לשקל השלם הקרוב, תחת הכותרת `UpdatedRate`.

**שאלה 11 (🟡 בינוני):**
כתבו שאילתה שמציגה עמודה אחת בשם `FullName` המשרשרת את השם הפרטי ושם המשפחה של התלמידים עם רווח ביניהם, ממוינת לפי א-ב של שם המשפחה.

**שאלה 12 (🟡 בינוני):**
כתבו שאילתה שמציגה את שמות כל המורים. למורה שיש לו טלפון יוצג הטלפון, ולמורה שאין לו טלפון (NULL) יוצג הטקסט `'לא קיים טלפון'`, תחת הכותרת `ContactInfo`.

**שאלה 13 (🟡 בינוני):**
כתבו שאילתה שמציגה את התשלום החודשי הממוצע של כל הרישומים מעוגל ל‑**ספרה אחת** אחרי הנקודה העשרונית, תחת הכותרת `FormattedAvg`.

**שאלה 14 (🔴 מתקדם):**
הציגו את שמות כלי הנגינה (InstName) ואת האות הראשונה של משפחת הכלי (InstFamily) תחת הכותרת `FamilyPrefix`.

---

### חלק ג': שילוב פונקציות עם GROUP BY ו‑HAVING

**שאלה 15 (🟡 בינוני):**
הציגו לכל קוד עיר (HomeTown) את מספר התלמידים שגרים בה (`PupilCount`). מיינו לפי מספר התלמידים מהגבוה לנמוך.

**שאלה 16 (🟡 בינוני):**
הציגו לכל רמת לימוד (PupilLevel) את מספר הרישומים ואת ממוצע התשלום החודשי (מעוגל לשלם).

**שאלה 17 (🟡 בינוני):**
הציגו לכל שנת רישום (RegYear) כמה רישומים בוצעו, **אך ורק לשנים שבהן היו יותר מ‑2 רישומים**.

**שאלה 18 (🔴 מתקדם):**
הציגו לכל מורה (RegTeacher) את סך ההכנסה החודשית מתלמידיו (`TotalIncome`), **אך ורק למורים שיש להם 3 תלמידים ומעלה**.

**שאלה 19 (🔴 מתקדם):**
הציגו לכל קוד כלי נגינה (TeachInst) בטבלת Teachers את התעריף הממוצע לשעה, **אך ורק לכלים שבהם מלמדים לפחות 2 מורים**.

---

### חלק ד': שאלות בסגנון בחינת מה"ט (השלמת ערכים, ניתוח פלט, שגיאות)

**שאלה 20 (🟢 קל):**
מה יהיה הפלט המספרי המדויק של השאילתה הבאה?
```sql
SELECT COUNT(*) - COUNT(TeacherPhone) AS Diff
FROM Teachers;
```

**שאלה 21 (🟡 בינוני):**
מה יהיה הפלט המדויק של השאילתה הבאה?
```sql
SELECT MIN(MonthlyFee), MAX(MonthlyFee), AVG(MonthlyFee)
FROM Registrations
WHERE PupilLevel = 'מתקדם';
```

**שאלה 22 (🟡 בינוני):**
התבוננו בשאילתה הבאה והסבירו מדוע היא תיכשל או תחזיר תוצאה שגויה, ותקנו אותה:
```sql
-- מה השגיאה כאן?
SELECT TeacherName, HourRate
FROM Teachers
WHERE HourRate > AVG(HourRate);
```

**שאלה 23 (🔴 מתקדם):**
כתבו שאילתה שמציגה את השם הפרטי ושם המשפחה של התלמיד (או התלמידים) שנולדו **בשנה המוקדמת ביותר** (התלמיד הכי מבוגר).

**שאלה 24 (🔴 מתקדם):**
השאילתה הבאה הופקה במבחן:
```sql
SELECT RegYear, COUNT(*) AS Cnt
FROM Registrations
WHERE MonthlyFee >= 320
GROUP BY RegYear
HAVING COUNT(*) >= 2
ORDER BY RegYear;
```
אילו שורות יופיעו בפלט הסופי?

**שאלה 25 (🔴 מתקדם):**
כתבו שאילתה שמציגה לכל עיר (שם העיר מטבלת Cities) את מספר התלמידים שגרים בה, כולל ערים שגרים בהן תלמידים וערים שאף תלמיד אינו גר בהן (רמז: שימוש בצירוף וספירה נכונה).

---

## 7. פתרונות מלאים עם הסברים

### פתרון 1:
```sql
SELECT COUNT(*) AS TotalTeachers
FROM Teachers;
```
**פלט:** `6`.
**הסבר:** סופר את כל 6 השורות בטבלת Teachers.

---

### פתרון 2:
```sql
SELECT COUNT(TeacherPhone) AS TeachersWithPhone
FROM Teachers;
```
**פלט:** `4`.
**הסבר:** שני מורים (קוד 3 וקוד 6) מכילים `NULL` בשדה הטלפון, ולכן `COUNT(עמודה)` מדלג עליהם וסופר 4 בלבד.

---

### פתרון 3:
```sql
SELECT MIN(HourRate) AS MinRate, MAX(HourRate) AS MaxRate
FROM Teachers;
```
**פלט:** `MinRate = 100`, `MaxRate = 150`.
**הסבר:** 100 הוא של יוסי פרץ, 150 של רונית לוי.

---

### פתרון 4:
```sql
SELECT SUM(MonthlyFee) AS TotalFees, AVG(MonthlyFee) AS AvgFee
FROM Registrations;
```
**פלט:** `TotalFees = 4630`, `AvgFee = 330.714...`.
**הסבר:** סוכם את שדה MonthlyFee של כל 14 שורות הרישום ומחשב את הממוצע שלהן.

---

### פתרון 5:
```sql
SELECT MAX(BirthYear) AS YoungestYear, MIN(BirthYear) AS OldestYear
FROM Pupils;
```
**פלט:** `YoungestYear = 2014`, `OldestYear = 2009`.
**הסבר:** שימו לב לתשומת לב קלאסית בבחינות: שנת לידה גבוהה (2014) שייכת לתלמיד **הצעיר ביותר**! שנת לידה נמוכה (2009) שייכת לתלמיד **המבוגר ביותר**.

---

### פתרון 6:
```sql
SELECT COUNT(*)                  AS TotalRegs,
       COUNT(DISTINCT RegPupil)   AS DistinctPupils,
       COUNT(DISTINCT RegTeacher) AS DistinctTeachers
FROM Registrations;
```
**פלט:** `TotalRegs = 14`, `DistinctPupils = 10`, `DistinctTeachers = 5`.
**הסבר:** יש 14 רישומים. כל 10 התלמידים רשומים לחוג לפחות פעם אחת. מתוך 6 המורים בבית הספר, רק 5 מלמדים בפועל (המורה 6 טרם קיבל תלמידים).

---

### פתרון 7:
```sql
SELECT COUNT(*) AS AcrePupils
FROM Pupils
WHERE HomeTown = 2;
```
**פלט:** `3`.
**הסבר:** התלמידים מעכו (שירה 204, רמי 205, יואב 210) — סך הכל 3.

---

### פתרון 8:
```sql
SELECT SUM(MonthlyFee) AS SumFees
FROM Registrations
WHERE PupilLevel = 'מתקדם';
```
**פלט:** `1040`.
**הסבר:** הרישומים ברמת מתקדם הם: 400 + 340 + 300 = 1040.

---

### פתרון 9:
```sql
SELECT CityName AS City, LENGTH(CityName) AS NameLength
FROM Cities;
```
**פלט:**
| City | NameLength |
|:---:|:---:|
| ירכא | 4 |
| עכו | 3 |
| כרמיאל | 6 |
| נהריה | 5 |
| מעלות | 5 |

---

### פתרון 10:
```sql
SELECT TeacherName, ROUND(HourRate * 1.15) AS UpdatedRate
FROM Teachers;
```
**הסבר:** מכפילים ב‑1.15 כדי להוסיף 15%, ועוטפים ב‑`ROUND()` ללא פרמטר נוסף כדי לעגל למספר שלם.

---

### פתרון 11:
```sql
SELECT FirstName || ' ' || LastName AS FullName
FROM Pupils
ORDER BY LastName ASC;
```
**הסבר:** אופרטור `||` משרשר מחרוזות. מוסיפים רווח `' '` באמצע כדי להפריד בין השם הפרטי לשם המשפחה.

---

### פתרון 12:
```sql
SELECT TeacherName, COALESCE(TeacherPhone, 'לא קיים טלפון') AS ContactInfo
FROM Teachers;
```
*(ניתן להשתמש גם ב‑`IFNULL(TeacherPhone, 'לא קיים טלפון')`)*.
**הסבר:** הפונקציה בודקת אם השדה הוא NULL; אם כן, היא מחזירה את המחרוזת החלופית.

---

### פתרון 13:
```sql
SELECT ROUND(AVG(MonthlyFee), 1) AS FormattedAvg
FROM Registrations;
```
**פלט:** `330.7`.
**הסבר:** `ROUND(..., 1)` מגדיר בדיוק ספרה אחת מימין לנקודה העשרונית.

---

### פתרון 14:
```sql
SELECT InstName, SUBSTR(InstFamily, 1, 1) AS FamilyPrefix
FROM Instruments;
```
**הסבר:** `SUBSTR(מחרוזת, תו_התחלתי, אורך)` גוזרת תווים. כאן מתחילים מתו 1 ולוקחים תו 1 בודד.

---

### פתרון 15:
```sql
SELECT HomeTown, COUNT(*) AS PupilCount
FROM Pupils
GROUP BY HomeTown
ORDER BY PupilCount DESC;
```
**פלט:**
| HomeTown | PupilCount |
|:---:|:---:|
| 1 | 3 |
| 2 | 3 |
| 3 | 2 |
| 4 | 2 |

---

### פתרון 16:
```sql
SELECT PupilLevel, COUNT(*) AS NumRegs, ROUND(AVG(MonthlyFee)) AS AvgFee
FROM Registrations
GROUP BY PupilLevel;
```
**פלט:**
- ממשיך: 6 רישומים, ממוצע 317 ש"ח.
- מתחיל: 5 רישומים, ממוצע 328 ש"ח.
- מתקדם: 3 רישומים, ממוצע 347 ש"ח.

---

### פתרון 17:
```sql
SELECT RegYear, COUNT(*) AS RegCount
FROM Registrations
GROUP BY RegYear
HAVING COUNT(*) > 2;
```
**פלט:**
- שנת 2024 (4 רישומים)
- שנת 2025 (5 רישומים)
**הסבר:** השנים 2021, 2022, 2023 נפסלו על ידי `HAVING` כי היו בהן פחות מ‑3 רישומים.

---

### פתרון 18:
```sql
SELECT RegTeacher, SUM(MonthlyFee) AS TotalIncome
FROM Registrations
GROUP BY RegTeacher
HAVING COUNT(*) >= 3;
```
**פלט:**
- מורה 1: 940 (3 תלמידים)
- מורה 2: 1160 (3 תלמידים)
- מורה 3: 960 (3 תלמידים)
- מורה 5: 860 (3 תלמידים)
*(למורה 4 יש רק 2 תלמידים, ולמורה 6 יש 0, ולכן סוננו).*

---

### פתרון 19:
```sql
SELECT TeachInst, AVG(HourRate) AS AvgRate
FROM Teachers
GROUP BY TeachInst
HAVING COUNT(*) >= 2;
```
**פלט:**
`TeachInst = 10, AvgRate = 140.0`.
**הסבר:** רק כלי 10 (פסנתר) נלמד על ידי שני מורים (רונית 150 ונור 130). הממוצע הוא `(150 + 130) / 2 = 140`. כל שאר הכלים נלמדים על ידי מורה בודד ונפסלים ב‑HAVING.

---

### פתרון 20:
**פלט:** `2`.
**הסבר:** `COUNT(*)` מחזיר 6. `COUNT(TeacherPhone)` מחזיר 4. התוצאה היא `6 - 4 = 2` (בדיוק מספר המורים ללא טלפון).

---

### פתרון 21:
**פלט:**
| MIN(MonthlyFee) | MAX(MonthlyFee) | AVG(MonthlyFee) |
|:---:|:---:|:---:|
| 300 | 400 | 346.666... |
**הסבר:** הרישומים הם 400, 340, 300. המינימום הוא 300, המקסימום 400, והממוצע `1040 / 3 = 346.66...`.

---

### פתרון 22:
**השגיאה:** אסור להשתמש בפונקציה מצרפית (`AVG`) בתוך פסוקית `WHERE`!
**התיקון הנכון באמצעות תת‑שאילתה:**
```sql
SELECT TeacherName, HourRate
FROM Teachers
WHERE HourRate > (SELECT AVG(HourRate) FROM Teachers);
```
**פלט:** רונית לוי (150), דנה כהן (140), נור מנסור (130). כולן מעל הממוצע (125).

---

### פתרון 23:
```sql
SELECT FirstName, LastName, BirthYear
FROM Pupils
WHERE BirthYear = (SELECT MIN(BirthYear) FROM Pupils);
```
**פלט:** רמי חורי (2009), יואב שושן (2009). שניהם נולדו בשנת המינימום.

---

### פתרון 24:
**שלבי פתרון:**
1. שורות עם `MonthlyFee >= 320`: שורות ברישומים 201 (320), 202 (400), 204 (360), 204 (380), 205 (340), 207 (350), 207 (320), 209 (380), 210 (320).
2. קיבוץ לפי שנה:
   - 2021: 1 רישום (מסונן ע"י HAVING)
   - 2022: 1 רישום (מסונן ע"י HAVING)
   - 2023: 1 רישום (מסונן ע"י HAVING)
   - 2024: 3 רישומים (201, 207, 210) עומד בתנאי!
   - 2025: 3 רישומים (204, 207, 209) עומד בתנאי!
**הפלט הסופי שיתקבל:**
| RegYear | Cnt |
|:---:|:---:|
| 2024 | 3 |
| 2025 | 3 |

---

### פתרון 25:
```sql
SELECT Cities.CityName, COUNT(Pupils.PupilId) AS TotalPupils
FROM Cities
LEFT JOIN Pupils ON Cities.CityCode = Pupils.HomeTown
GROUP BY Cities.CityCode, Cities.CityName;
```
**הסבר חשוב:** 
- משתמשים ב‑`LEFT JOIN` כדי שגם מעלות (שאף תלמיד אינו גר בה) תופיע!
- משתמשים ב‑`COUNT(Pupils.PupilId)` ולא ב‑`COUNT(*)`, כדי שעבור מעלות נקבל `0` ולא `1`!

</div>
