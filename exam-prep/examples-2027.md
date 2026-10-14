<!-- generated from .moodle_build/assessments/sql_examples2027.src.md -->
<div dir="rtl">

# דוגמאות פתורות, צעד אחרי צעד: SQL לבחינה (תשפ"ז)

> בדף הזה **20 דוגמאות פתורות**, מהקלה לקשה. בכל דוגמה: השאלה, **איך חושבים** עליה, השאילתה, והתוצאה האמיתית שלה.
> כל הדוגמאות רצות על בסיס הנתונים [`db/music.sql`](db/music.sql), בית הספר למוזיקה "צלילים". את הטבלאות המלאות תמצאו ב[דף התרגול](practice-2027.md).
>
> | רמה | מה יש בה |
> |:-:|---|
> | 🟢 **בסיסית** | טבלה אחת: `SELECT`, `WHERE`, `LIKE`, `BETWEEN`, `DISTINCT`, `AS`, `IS NULL` |
> | 🟡 **בינונית** | צירוף טבלאות, פונקציות קיבוץ, `GROUP BY`, `HAVING`, תת־שאילתה אחת |
> | 🔴 **מתקדמת** | מלכודות, כמה רמות של תת־שאילתות, שאילתה שמורה, ניתוח פלט, `UPDATE`/`DELETE`/`ALTER` |
>
> **איך ללמוד מהדף:** קראו את השאלה, **עצרו**, ונסו לכתוב לבד. רק אחר כך קראו את הפתרון.

### השיטה הקבועה: 4 שאלות לפני שכותבים שאילתה

| # | שואלים | כותבים ב‑ |
|:-:|---|---|
| 1 | מאילו **טבלאות** מגיע המידע? | `FROM` |
| 2 | אילו **שורות** רוצים? (תנאי) | `WHERE` |
| 3 | אילו **עמודות** להציג? | `SELECT` |
| 4 | צריך **לקבץ**, **למיין** או **להוריד כפילויות**? | `GROUP BY` · `ORDER BY` · `DISTINCT` |

**תזכורת: מבנה בסיס הנתונים**

- **Pupils** (PupilId, FirstName, LastName, BirthYear, HomeTown → Cities)
- **Teachers** (TeacherCode, TeacherName, TeachInst → Instruments, HourRate, TeacherPhone)
- **Registrations** (RegPupil → Pupils, RegTeacher → Teachers, RegYear, PupilLevel, MonthlyFee)
- טבלאות עזר: **Cities** (CityCode, CityName), **Instruments** (InstCode, InstName, InstFamily), **Lockers** (LockerNum, LockerPupil → Pupils, LockerFloor)

---

## 🟢 רמה בסיסית: טבלה אחת

### דוגמה 1 🟢: תנאי על מספר

**השאלה:** הציגו את השם הפרטי ואת שנת הלידה של התלמידים שנולדו **אחרי** 2011.

**איך חושבים:**
1. המידע על תלמידים נמצא בטבלה **Pupils**.
2. התנאי: שנת לידה **גדולה** מ‑2011. "אחרי 2011" **לא כולל** את 2011, ולכן `>` ולא `>=`.
3. העמודות: FirstName ו‑BirthYear.

```sql
SELECT FirstName, BirthYear
FROM Pupils
WHERE BirthYear > 2011;
```

<figure dir="ltr" class="dbtable">

| FirstName | BirthYear |
|:---:|:---:|
| אדם | 2012 |
| כרים | 2013 |
| תמר | 2012 |
| סאלי | 2014 |

</figure>

### דוגמה 2 🟢: תנאי על טקסט

**השאלה:** הציגו את מספר התלמיד ואת קוד המורה בכל הרישומים ברמה "מתקדם".

**איך חושבים:** הרמה נמצאת בטבלה **Registrations**, בשדה PupilLevel. טקסט כותבים בתוך **מירכאות כפולות**, בדיוק כמו שהוא כתוב בטבלה.

```sql
SELECT RegPupil, RegTeacher
FROM Registrations
WHERE PupilLevel = "מתקדם";
```

<figure dir="ltr" class="dbtable">

| RegPupil | RegTeacher |
|:---:|:---:|
| 202 | 2 |
| 205 | 3 |
| 210 | 5 |

</figure>

> ⚠️ `PupilLevel = מתקדם` (בלי מירכאות) היא **טעות**: בלי מירכאות, SQL מחפש שדה בשם מתקדם.

### דוגמה 3 🟢: LIKE, ארבע תבניות

**השאלה:** מה מחזיר כל אחד מהתנאים על שם המשפחה (LastName)?

**איך חושבים:** `%` הוא "כל רצף של תווים, גם רצף ריק", ו‑`_` הוא "תו **אחד** בדיוק".

| התנאי | פירוש | התוצאה |
|---|---|---|
| `LIKE "ח%"` | מתחיל ב‑ח | חלבי, חורי, חסון |
| `LIKE "%ן"` | מסתיים ב‑ן | כהן, קבלאן, ביטון, חסון, שושן |
| `LIKE "%ב%"` | יש בו ב, בכל מקום | חלבי, אברהם, קבלאן, ביטון |
| `LIKE "__ו%"` | האות **השלישית** היא ו | חסון |

```sql
SELECT LastName FROM Pupils WHERE LastName LIKE "%ב%";
```

> ⚠️ שימו לב לשורה השנייה: גם "כהן" מסתיים ב‑ן. בשאלות "איזו טבלה תתקבל" זו מלכודת נפוצה.

### דוגמה 4 🟢: BETWEEN כולל את הקצוות

**השאלה:** כמה רישומים יש עם תשלום חודשי **בין 300 ל‑350**?

**איך חושבים:** `BETWEEN 300 AND 350` הוא בדיוק `>= 300 AND <= 350`. **שני הקצוות בפנים.**

```sql
SELECT COUNT(*) AS Regs
FROM Registrations
WHERE MonthlyFee BETWEEN 300 AND 350;
```

<figure dir="ltr" class="dbtable">

| Regs |
|:---:|
| 8 |

</figure>

לעומת זאת, עם `MonthlyFee > 300 AND MonthlyFee < 350` (בלי הקצוות) מתקבלים רק **4** רישומים: כל הרישומים של 300 ושל 350 בדיוק נשארים בחוץ.

### דוגמה 5 🟢: DISTINCT מוריד כפילויות

**השאלה:** אילו משפחות של כלי נגינה יש בבית הספר? כל משפחה פעם אחת.

**איך חושבים:** בטבלה Instruments יש 6 כלים, אבל "מיתר" מופיע 3 פעמים. `DISTINCT` משאיר כל ערך **פעם אחת**.

```sql
SELECT DISTINCT InstFamily
FROM Instruments;
```

<figure dir="ltr" class="dbtable">

| InstFamily |
|:---:|
| קלידים |
| מיתר |
| הקשה |
| נשיפה |

</figure>

בלי `DISTINCT` היו מתקבלות 6 שורות, ו"מיתר" היה מופיע שלוש פעמים.

### דוגמה 6 🟢: חישוב וכינוי (AS)

**השאלה:** הציגו לכל מורה את שמו ואת המחיר של **שיעור כפול** (שעתיים). הכותרת של העמודה החדשה תהיה DoubleLesson.

**איך חושבים:** אפשר לחשב בתוך `SELECT`. בלי `AS`, הכותרת תהיה הביטוי עצמו (`HourRate * 2`). עם `AS` אנחנו בוחרים לה שם.

```sql
SELECT TeacherName, HourRate * 2 AS DoubleLesson
FROM Teachers;
```

<figure dir="ltr" class="dbtable">

| TeacherName | DoubleLesson |
|:---:|:---:|
| סמיר חלבי | 240 |
| רונית לוי | 300 |
| אמיר עזאם | 220 |
| דנה כהן | 280 |
| יוסי פרץ | 200 |
| נור מנסור | 260 |

</figure>

### דוגמה 7 🟢: IS NULL

**השאלה:** אילו מורים **אין להם** טלפון רשום?

**איך חושבים:** תא ריק בטבלה הוא `NULL`. בודקים אותו **רק** עם `IS NULL`. התנאי `= NULL` לעולם לא מתקיים.

```sql
SELECT TeacherName
FROM Teachers
WHERE TeacherPhone IS NULL;
```

<figure dir="ltr" class="dbtable">

| TeacherName |
|:---:|
| אמיר עזאם |
| נור מנסור |

</figure>

ההפך, המורים **שיש** להם טלפון: `WHERE TeacherPhone IS NOT NULL`.

---

## 🟡 רמה בינונית: צירוף טבלאות וקיבוץ

### דוגמה 8 🟡: צירוף של שתי טבלאות

**השאלה:** הציגו לכל תלמיד את השם הפרטי שלו ואת **שם** העיר שבה הוא גר.

**איך חושבים:**
1. השם הפרטי נמצא ב‑Pupils, ושם העיר ב‑Cities. צריך **שתי טבלאות** ב‑`FROM`.
2. איך הן מתחברות? בטבלה Pupils השדה **HomeTown** הוא מפתח זר, והוא מפנה ל‑**CityCode** בטבלה Cities. זה תנאי החיבור.
3. שמות השדות ייחודיים, ולכן לא צריך לכתוב את שם הטבלה לפניהם.

```sql
SELECT FirstName, CityName
FROM Pupils, Cities
WHERE HomeTown = CityCode;
```

<figure dir="ltr" class="dbtable">

| FirstName | CityName |
|:---:|:---:|
| אדם | ירכא |
| מאיה | כרמיאל |
| כרים | ירכא |
| שירה | עכו |
| רמי | עכו |
| תמר | נהריה |
| ליאן | ירכא |
| עומר | נהריה |
| סאלי | כרמיאל |
| יואב | עכו |

</figure>

> ⚠️ **מה קורה אם שוכחים את תנאי החיבור?** כל תלמיד מתחבר לכל עיר: 10 × 5 = **50** שורות, ורובן שגויות. זה נקרא **מכפלה** (תוצר קרטזי).

### דוגמה 9 🟡: צירוף של שלוש טבלאות

**השאלה:** הציגו את השם הפרטי של כל תלמיד ואת **שם** המורה שלו.

**איך חושבים:**
1. שם התלמיד ב‑Pupils, שם המורה ב‑Teachers. אבל אין ביניהן קשר ישיר: הקשר עובר דרך הטבלה המקשרת **Registrations**.
2. **שלוש טבלאות = שני תנאי חיבור:** `PupilId = RegPupil` (תלמיד ← רישום), ו‑`RegTeacher = TeacherCode` (רישום ← מורה).

```sql
SELECT FirstName, TeacherName
FROM Pupils, Registrations, Teachers
WHERE PupilId = RegPupil
  AND RegTeacher = TeacherCode;
```

<figure dir="ltr" class="dbtable">

| FirstName | TeacherName |
|:---:|:---:|
| אדם | סמיר חלבי |
| אדם | יוסי פרץ |
| מאיה | רונית לוי |
| כרים | סמיר חלבי |
| שירה | רונית לוי |
| שירה | דנה כהן |
| רמי | אמיר עזאם |
| תמר | יוסי פרץ |
| ליאן | סמיר חלבי |
| ליאן | דנה כהן |
| עומר | אמיר עזאם |
| סאלי | רונית לוי |
| יואב | אמיר עזאם |
| יואב | יוסי פרץ |

</figure>

שימו לב: אדם, שירה, ליאן ויואב מופיעים **פעמיים**, כי לכל אחד מהם יש שני מורים. זה בדיוק קשר רבים לרבים.

### דוגמה 10 🟡: פונקציות קיבוץ על כל הטבלה

**השאלה:** מה מספר הרישומים, סכום התשלומים, הממוצע, התשלום הנמוך ביותר והגבוה ביותר?

**איך חושבים:** בלי `GROUP BY`, כל הטבלה היא **קבוצה אחת**, ומתקבלת **שורה אחת**.

```sql
SELECT COUNT(*) AS Regs, SUM(MonthlyFee) AS Total, AVG(MonthlyFee) AS Average,
       MIN(MonthlyFee) AS Lowest, MAX(MonthlyFee) AS Highest
FROM Registrations;
```

<figure dir="ltr" class="dbtable">

| Regs | Total | Average | Lowest | Highest |
|:---:|:---:|:---:|:---:|:---:|
| 14 | 4630 | 330.71 | 280 | 400 |

</figure>

> `COUNT(*)` סופר שורות. `COUNT(TeacherPhone)` סופר רק שורות שבהן **יש** ערך: ב‑Teachers זה 4 ולא 6.

### דוגמה 11 🟡: GROUP BY, תוצאה לכל קבוצה

**השאלה:** כמה תלמידים יש לכל מורה?

**איך חושבים:**
1. "לכל מורה" = **קבוצה לכל מורה**: `GROUP BY RegTeacher`.
2. SQL מסדר את הרישומים בערימות, ערימה לכל מורה, ו‑`COUNT(*)` סופר כמה שורות יש בכל ערימה.
3. **החוק:** כל שדה ב‑`SELECT` שאינו בתוך פונקציה חייב להופיע ב‑`GROUP BY`.

```sql
SELECT RegTeacher, COUNT(*) AS Pupils_Count
FROM Registrations
GROUP BY RegTeacher;
```

<figure dir="ltr" class="dbtable">

| RegTeacher | Pupils_Count |
|:---:|:---:|
| 1 | 3 |
| 2 | 3 |
| 3 | 3 |
| 4 | 2 |
| 5 | 3 |

</figure>

המורה 6 **לא** מופיע, כי אין לו אף שורה ב‑Registrations. אין מה לקבץ.

### דוגמה 12 🟡: WHERE, GROUP BY ו‑HAVING יחד

**השאלה:** לכל מורה, מה התשלום החודשי הממוצע של התלמידים שנרשמו **מ‑2024 ואילך**? הציגו רק מורים שהממוצע אצלם **מעל 300**.

**איך חושבים, לפי סדר הביצוע:**
1. `WHERE RegYear >= 2024`: קודם מסננים **שורות** (רישומים ישנים יוצאים).
2. `GROUP BY RegTeacher`: מה שנשאר מתחלק לקבוצות.
3. `HAVING AVG(MonthlyFee) > 300`: מסננים **קבוצות**, לפי תוצאה של פונקציה.

```sql
SELECT RegTeacher, AVG(MonthlyFee) AS AvgFee
FROM Registrations
WHERE RegYear >= 2024
GROUP BY RegTeacher
HAVING AVG(MonthlyFee) > 300;
```

<figure dir="ltr" class="dbtable">

| RegTeacher | AvgFee |
|:---:|:---:|
| 1 | 313.33 |
| 2 | 380 |
| 3 | 320 |
| 4 | 350 |

</figure>

> **איך זוכרים?** תנאי על **שורה** ← `WHERE`. תנאי על **`COUNT`/`SUM`/`AVG`/`MIN`/`MAX`** ← `HAVING`. אי אפשר לכתוב `WHERE AVG(...) > 300`.

### דוגמה 13 🟡: NOT IN, "מי שלא מופיע"

**השאלה:** אילו תלמידים **אין להם** לוקר?

**איך חושבים:**
1. קודם התת־שאילתה (**מבפנים החוצה**): `SELECT LockerPupil FROM Lockers` מחזירה את רשימת התלמידים **שיש** להם לוקר: 201, 202, 205, 207, 210.
2. אחר כך השאילתה החיצונית משאירה את מי שהמספר שלו **לא** ברשימה.

```sql
SELECT FirstName, LastName
FROM Pupils
WHERE PupilId NOT IN (SELECT LockerPupil FROM Lockers);
```

<figure dir="ltr" class="dbtable">

| FirstName | LastName |
|:---:|:---:|
| כרים | עזאם |
| שירה | לוי |
| תמר | אברהם |
| עומר | ביטון |
| סאלי | חסון |

</figure>

> ⚠️ בתוך `(SELECT ... FROM Lockers)` כותבים שדה **של Lockers** (LockerPupil). `SELECT PupilId FROM Lockers` היא טעות.

### דוגמה 14 🟡: השוואה לערך אחד מחושב

**השאלה:** אילו מורים מקבלים תשלום לשעה **גבוה מהממוצע**?

**איך חושבים:** אי אפשר לכתוב `WHERE HourRate > AVG(HourRate)`. מחשבים את הממוצע **בתת־שאילתה**, שמחזירה מספר אחד (125), ומשווים אליו.

```sql
SELECT TeacherName, HourRate
FROM Teachers
WHERE HourRate > (SELECT AVG(HourRate) FROM Teachers);
```

<figure dir="ltr" class="dbtable">

| TeacherName | HourRate |
|:---:|:---:|
| רונית לוי | 150 |
| דנה כהן | 140 |
| נור מנסור | 130 |

</figure>

---

## 🔴 רמה מתקדמת: מלכודות ושאלות מורכבות

### דוגמה 15 🔴: מלכודת AND ו‑OR

**השאלה:** תלמיד רצה את הרישומים ברמה "מתחיל" **אצל המורים 1 או 2**, וכתב:

```sql
SELECT RegPupil, RegTeacher, PupilLevel
FROM Registrations
WHERE PupilLevel = "מתחיל" AND RegTeacher = 1 OR RegTeacher = 2;
```

<figure dir="ltr" class="dbtable">

| RegPupil | RegTeacher | PupilLevel |
|:---:|:---:|:---:|
| 202 | 2 | מתקדם |
| 203 | 1 | מתחיל |
| 204 | 2 | מתחיל |
| 209 | 2 | מתחיל |

</figure>

**מה השתבש?** `AND` מתבצע **לפני** `OR`, ולכן SQL הבין: (מתחיל **וגם** מורה 1) **או** (מורה 2, בכל רמה). כך נכנס גם תלמיד "מתקדם" של מורה 2.

**התיקון:** סוגריים, או `IN`:

```sql
SELECT RegPupil, RegTeacher, PupilLevel
FROM Registrations
WHERE PupilLevel = "מתחיל" AND RegTeacher IN (1, 2);
```

<figure dir="ltr" class="dbtable">

| RegPupil | RegTeacher | PupilLevel |
|:---:|:---:|:---:|
| 203 | 1 | מתחיל |
| 204 | 2 | מתחיל |
| 209 | 2 | מתחיל |

</figure>

### דוגמה 16 🔴: שלוש רמות של תת־שאילתות

**השאלה:** אילו תלמידים לומדים אצל מורה שמלמד כלי ממשפחת **"מיתר"**? (בלי צירוף בפסיקים, רק עם `IN`.)

**איך חושבים: בונים מבפנים החוצה, שלב אחרי שלב:**

| שלב | השאילתה | מה היא מחזירה |
|:-:|---|---|
| 1 | `SELECT InstCode FROM Instruments WHERE InstFamily = "מיתר"` | 20, 30, 60 |
| 2 | `SELECT TeacherCode FROM Teachers WHERE TeachInst IN (שלב 1)` | 1, 3, 4 |
| 3 | `SELECT RegPupil FROM Registrations WHERE RegTeacher IN (שלב 2)` | 201, 203, 204, 205, 207, 207, 208, 210 |

```sql
SELECT FirstName, LastName
FROM Pupils
WHERE PupilId IN (SELECT RegPupil FROM Registrations
                  WHERE RegTeacher IN (SELECT TeacherCode FROM Teachers
                                       WHERE TeachInst IN (SELECT InstCode FROM Instruments
                                                           WHERE InstFamily = "מיתר")));
```

<figure dir="ltr" class="dbtable">

| FirstName | LastName |
|:---:|:---:|
| אדם | חלבי |
| כרים | עזאם |
| שירה | לוי |
| רמי | חורי |
| ליאן | קבלאן |
| עומר | ביטון |
| יואב | שושן |

</figure>

### דוגמה 17 🔴: שאילתה שמורה (Q1) ביחד עם טבלה

**השאלה:** תלמיד שמר שאילתה בשם **Q1**, שמחשבת לכל מורה את מספר התלמידים שלו. השתמשו בה כדי להציג את **שמות** המורים שיש להם **בדיוק 3** תלמידים.

**איך חושבים:**
1. Q1 היא כמו **טבלה חדשה** עם שתי עמודות: RegTeacher ו‑PupilsNum.
2. את השמות של המורים יש רק ב‑Teachers. מצרפים את Teachers ל‑Q1 בדיוק כמו שמצרפים שתי טבלאות: `TeacherCode = RegTeacher`.

```sql
CREATE VIEW Q1 AS
SELECT RegTeacher, COUNT(*) AS PupilsNum FROM Registrations GROUP BY RegTeacher;

SELECT TeacherName, PupilsNum
FROM Teachers, Q1
WHERE TeacherCode = RegTeacher
  AND PupilsNum = 3;
```

<figure dir="ltr" class="dbtable">

| TeacherName | PupilsNum |
|:---:|:---:|
| סמיר חלבי | 3 |
| רונית לוי | 3 |
| אמיר עזאם | 3 |
| יוסי פרץ | 3 |

</figure>

> ב‑Access זו "שאילתה שמורה". ב‑SQL זה **VIEW** (`CREATE VIEW`). בבחינה Q1 כבר שמורה, ואתם רק משתמשים בה ב‑`FROM`.

### דוגמה 18 🔴: ניתוח פלט, איזו שאילתה הציגה את הטבלה?

**השאלה:** התקבלה הטבלה הזאת:

<figure dir="ltr" class="dbtable">

| PupilLevel | Regs |
|:---:|:---:|
| ממשיך | 4 |
| מתחיל | 3 |
| מתקדם | 2 |

</figure>

איזו מבין השאילתות הציגה אותה?
1. `SELECT PupilLevel, COUNT(*) AS Regs FROM Registrations GROUP BY PupilLevel`
2. `SELECT PupilLevel, COUNT(*) AS Total FROM Registrations WHERE MonthlyFee >= 320 GROUP BY PupilLevel`
3. `SELECT PupilLevel, COUNT(*) AS Regs FROM Registrations WHERE MonthlyFee >= 320 GROUP BY PupilLevel`
4. `SELECT PupilLevel, COUNT(*) AS Regs FROM Registrations WHERE MonthlyFee > 320 GROUP BY PupilLevel`

**איך חושבים, בשלושה סינונים:**
1. **כותרות:** בטבלה העמודה נקראת **Regs**. תשובה 2 (`AS Total`) נפסלת.
2. **מספרים:** תשובה 1 סופרת את **כל** הרישומים. למשל ל"מתחיל" היא נותנת 5, ובטבלה כתוב 3. נפסלת.
3. **קצוות:** בין `>=` ל‑`>` ההבדל הוא הרישומים של **320 בדיוק**. עם `>` ל"ממשיך" יוצא 1 ולא 4. נשארת **תשובה 3**.

### דוגמה 19 🔴: UPDATE עם תת־שאילתה

**השאלה:** המורה "דנה כהן" מעלה ב‑10% את התשלום החודשי של **כל התלמידים שלה**. כתבו את הפקודה. כמה רשומות יתעדכנו?

**איך חושבים:**
1. מעדכנים את **MonthlyFee**, שנמצא ב‑Registrations: `UPDATE Registrations`.
2. שם המורה נמצא ב‑Teachers, אבל ב‑Registrations יש רק את **הקוד** שלה. מוצאים את הקוד בתת־שאילתה.
3. **בלי `WHERE` כל הרישומים יתעדכנו.** לכן לפני `UPDATE` כדאי להריץ `SELECT` עם אותו `WHERE` ולבדוק מה ייפגע.

```sql
UPDATE Registrations
SET MonthlyFee = MonthlyFee * 1.1
WHERE RegTeacher = (SELECT TeacherCode FROM Teachers WHERE TeacherName = "דנה כהן");
```

יתעדכנו **2** רשומות: הרישומים של שירה ושל ליאן.

### דוגמה 20 🔴: שינוי מבנה ונתונים, לפי הסדר הנכון

**השאלה:** בית הספר מוסיף כלי חדש, **"צ'לו"** (קוד 70, משפחת "מיתר"), ומורה חדשה שמלמדת אותו: **"ריהאם חסון"** (קוד 7), 145 ש"ח לשעה, בלי טלפון. בנוסף, רוצים לשמור לכל מורה את **שנת ההתחלה** שלו (שדה חדש), ולשנות את הטיפוס של TeacherName ל‑`VARCHAR(40)`.

**איך חושבים:**
1. **קודם הכלי, ואחר כך המורה.** TeachInst הוא מפתח זר: הקוד 70 חייב להיות קיים ב‑Instruments לפני שמורה מפנה אליו.
2. שדה **חדש** ← `ALTER TABLE ... ADD`. שינוי **טיפוס** של שדה ← `ALTER TABLE ... MODIFY COLUMN`.

```sql
INSERT INTO Instruments (InstCode, InstName, InstFamily)
VALUES (70, "צ'לו", "מיתר");

INSERT INTO Teachers (TeacherCode, TeacherName, TeachInst, HourRate)
VALUES (7, "ריהאם חסון", 70, 145);

ALTER TABLE Teachers ADD StartYear INTEGER;
```

```sql
-- MySQL
ALTER TABLE Teachers MODIFY COLUMN TeacherName VARCHAR(40);
```

TeacherPhone לא מופיע ברשימת השדות של `INSERT`, ולכן הוא נשאר ריק (NULL), כמו שביקשו. `MODIFY COLUMN` היא פקודה של MySQL. ב‑OneCompiler מריצים אותה במצב [MySQL](https://onecompiler.com/mysql).

| המשימה | הפקודה |
|---|---|
| למחוק את **השדה** StartYear | `ALTER TABLE Teachers DROP COLUMN StartYear` |
| למחוק את **הרשומות** של מורה 7 | `DELETE FROM Teachers WHERE TeacherCode = 7` |
| למחוק את **הטבלה** כולה | `DROP TABLE Lockers` |

---

## ✅ מה הלאה?

1. **[תרגול לפי ההנחיות](practice-2027.md):** 48 סעיפים על אותו בסיס נתונים, עם רמת קושי לכל סעיף ([פתרונות](practice-2027-solutions.md)).
2. **[דף העזר](cheat-sheet.md):** להדפיס ולהביא לבחינה.
3. **בחינות לדוגמה** ב‑Moodle, ובחינות אמיתיות משנים קודמות ([README](README.md)).

</div>
