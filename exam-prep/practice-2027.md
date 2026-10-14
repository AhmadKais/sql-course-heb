<!-- generated from .moodle_build/assessments/sql_practice2027.src.md -->
<div dir="rtl">

# תרגול לפי ההנחיות של תשפ"ז: חלק בסיסי הנתונים (שאלון 735911)

> הדף הזה בנוי לפי **מסמך ההנחיות והדגשים של משרד החינוך לשאלון 735911, תשפ"ז (2027)**. כל חלק בדף מתאים לסעיף במסמך, ומכסה את כל סוגי השאלות שמופיעים בו.
>
> **בסיס הנתונים:** [`db/music.sql`](db/music.sql). פתרו קודם על הנייר, כמו בבחינה, ורק אחר כך טענו את הקובץ ל‑[OneCompiler](https://onecompiler.com/sqlite) ובדקו את עצמכם. הפתרונות: [practice-2027-solutions.md](practice-2027-solutions.md).

> **רמת הקושי של כל סעיף:** 🟢 בסיסי · 🟡 בינוני · 🔴 מתקדם. לא בטוחים? התחילו מה‑[דוגמאות הפתורות](examples-2027.md), ואחר כך פתרו קודם את כל הסעיפים הירוקים.

### שני כללים חדשים מההנחיות, שחשוב לזכור

1. **לכל שדה בבסיס הנתונים יש שם ייחודי**, ולכן בבחינה שמות השדות מופיעים **בלי** שם הטבלה לפניהם. כותבים `WHERE HomeTown = CityCode`, ולא `WHERE Pupils.HomeTown = Cities.CityCode`.
2. **במבנה בסיס הנתונים יש 2–3 טבלאות ראשיות, ועוד כמה טבלאות עזר קטנות.** מפתח ראשי יכול להיות **מורכב** מכמה שדות, ויש שלושה סוגי קשרים: 1:1, 1:N ו‑M:N (שדורש טבלה מקשרת).

## בסיס הנתונים: בית הספר למוזיקה "צלילים"

- **טבלאות ראשיות:**
  - **Pupils (תלמידים):** PupilId הוא מספר התלמיד, HomeTown הוא קוד העיר שבה התלמיד גר.
  - **Teachers (מורים):** TeachInst הוא קוד הכלי שהמורה מלמד, HourRate הוא התשלום לשעה בש"ח. לחלק מהמורים לא רשום טלפון.
  - **Registrations (רישום):** כל שורה אומרת שתלמיד (RegPupil) לומד אצל מורה (RegTeacher): מאיזו שנה, באיזו רמה, וכמה הוא משלם בחודש (MonthlyFee).
- **טבלאות עזר:** **Cities** (ערים), **Instruments** (כלי נגינה; InstFamily היא משפחת הכלי), **Lockers** (לוקרים; LockerPupil הוא התלמיד שהלוקר שייך לו, ולכל תלמיד יש לוקר **אחד לכל היותר**).

<figure dir="ltr" class="dbtable">

**Cities**

| CityCode | CityName |
|:---:|:---:|
| 1 | ירכא |
| 2 | עכו |
| 3 | כרמיאל |
| 4 | נהריה |
| 5 | מעלות |

</figure>

<figure dir="ltr" class="dbtable">

**Instruments**

| InstCode | InstName | InstFamily |
|:---:|:---:|:---:|
| 10 | פסנתר | קלידים |
| 20 | גיטרה | מיתר |
| 30 | כינור | מיתר |
| 40 | תופים | הקשה |
| 50 | חליל | נשיפה |
| 60 | עוד | מיתר |

</figure>

<figure dir="ltr" class="dbtable">

**Teachers**

| TeacherCode | TeacherName | TeachInst | HourRate | TeacherPhone |
|:---:|:---:|:---:|:---:|:---:|
| 1 | סמיר חלבי | 60 | 120 | 050-1234567 |
| 2 | רונית לוי | 10 | 150 | 052-2345678 |
| 3 | אמיר עזאם | 20 | 110 |  |
| 4 | דנה כהן | 30 | 140 | 054-4567890 |
| 5 | יוסי פרץ | 40 | 100 | 053-5678901 |
| 6 | נור מנסור | 10 | 130 |  |

</figure>

<figure dir="ltr" class="dbtable">

**Pupils**

| PupilId | FirstName | LastName | BirthYear | HomeTown |
|:---:|:---:|:---:|:---:|:---:|
| 201 | אדם | חלבי | 2012 | 1 |
| 202 | מאיה | כהן | 2010 | 3 |
| 203 | כרים | עזאם | 2013 | 1 |
| 204 | שירה | לוי | 2011 | 2 |
| 205 | רמי | חורי | 2009 | 2 |
| 206 | תמר | אברהם | 2012 | 4 |
| 207 | ליאן | קבלאן | 2011 | 1 |
| 208 | עומר | ביטון | 2010 | 4 |
| 209 | סאלי | חסון | 2014 | 3 |
| 210 | יואב | שושן | 2009 | 2 |

</figure>

<figure dir="ltr" class="dbtable">

**Registrations**

| RegPupil | RegTeacher | RegYear | PupilLevel | MonthlyFee |
|:---:|:---:|:---:|:---:|:---:|
| 201 | 1 | 2024 | ממשיך | 320 |
| 201 | 5 | 2025 | מתחיל | 280 |
| 202 | 2 | 2022 | מתקדם | 400 |
| 203 | 1 | 2025 | מתחיל | 300 |
| 204 | 4 | 2023 | ממשיך | 360 |
| 204 | 2 | 2025 | מתחיל | 380 |
| 205 | 3 | 2021 | מתקדם | 340 |
| 206 | 5 | 2024 | ממשיך | 280 |
| 207 | 4 | 2025 | מתחיל | 350 |
| 207 | 1 | 2024 | ממשיך | 320 |
| 208 | 3 | 2023 | ממשיך | 300 |
| 209 | 2 | 2025 | מתחיל | 380 |
| 210 | 5 | 2022 | מתקדם | 300 |
| 210 | 3 | 2024 | ממשיך | 320 |

</figure>

<figure dir="ltr" class="dbtable">

**Lockers**

| LockerNum | LockerPupil | LockerFloor |
|:---:|:---:|:---:|
| 1 | 202 | 1 |
| 2 | 205 | 1 |
| 3 | 207 | 2 |
| 4 | 210 | 2 |
| 5 | 201 | 2 |

</figure>

---

## חלק א: מבנה בסיס הנתונים, מפתחות וקשרים (סעיפים 1–2 בהנחיות)

**1.** 🟢 בתרשים ה‑DSD של בסיס הנתונים יש **חמישה** קווי קשר. השלימו את הטבלה:

| # | צד המפתח הראשי | צד המפתח הזר |
|:-:|:---:|:---:|
| 1 | CityCode | ________ |
| 2 | ________ | TeachInst |
| 3 | PupilId | ________ |
| 4 | ________ | RegTeacher |
| 5 | ________ | ________ |

**2.** 🟢 קבעו לגבי כל היגד אם הוא **נכון** או **לא נכון**, והסבירו בשורה אחת:
1. המפתח הראשי בטבלה Registrations הוא השדה RegPupil בלבד.
2. בטבלה Registrations יש שני מפתחות זרים, ויחד הם גם המפתח הראשי שלה.
3. הקשר בין Pupils ל‑Teachers הוא קשר של רבים לרבים.
4. הקשר בין Pupils ל‑Lockers הוא קשר של יחיד ליחיד.
5. בטבלה Instruments יש מפתח זר.

**3.** 🟢 מהו סוג הקשר בין Instruments ל‑Teachers? באיזו טבלה נמצא צד ה"רבים"?

**4.** 🟡 למה **אי אפשר** לשמור את הרישום של תלמיד למורה בתוך הטבלה Pupils (למשל שדה TeacherCode בטבלה Pupils)?

---

## חלק ב: איזו טבלה תתקבל? אילו ערכים יוחזרו? (סעיף 3)

**5.** 🟢 איזו טבלה תתקבל לאחר ביצוע השאילתה?

```sql
SELECT FirstName, LastName
FROM Pupils
WHERE BirthYear BETWEEN 2010 AND 2012
ORDER BY LastName;
```



**1.**

<figure dir="ltr" class="dbtable">

| FirstName | LastName |
|:---:|:---:|
| שירה | לוי |
| ליאן | קבלאן |

</figure>



**2.**

<figure dir="ltr" class="dbtable">

| FirstName | LastName |
|:---:|:---:|
| אדם | חלבי |
| ליאן | קבלאן |
| מאיה | כהן |
| עומר | ביטון |
| שירה | לוי |
| תמר | אברהם |

</figure>



**3.**

<figure dir="ltr" class="dbtable">

| FirstName | LastName |
|:---:|:---:|
| תמר | אברהם |
| עומר | ביטון |
| אדם | חלבי |
| מאיה | כהן |
| שירה | לוי |
| ליאן | קבלאן |

</figure>



**4.**

<figure dir="ltr" class="dbtable">

| FirstName | LastName |
|:---:|:---:|
| תמר | אברהם |
| עומר | ביטון |
| אדם | חלבי |
| סאלי | חסון |
| מאיה | כהן |
| שירה | לוי |
| כרים | עזאם |
| ליאן | קבלאן |

</figure>




**6.** 🟡 איזו טבלה תתקבל לאחר ביצוע השאילתה?

```sql
SELECT TeacherName, InstName
FROM Teachers, Instruments
WHERE TeachInst = InstCode
  AND InstFamily = "מיתר"
ORDER BY TeacherName;
```



**1.**

<figure dir="ltr" class="dbtable">

| TeacherName | InstName |
|:---:|:---:|
| יוסי פרץ | תופים |
| נור מנסור | פסנתר |
| רונית לוי | פסנתר |

</figure>



**2.**

<figure dir="ltr" class="dbtable">

| TeacherName | InstName |
|:---:|:---:|
| סמיר חלבי | עוד |
| דנה כהן | כינור |
| אמיר עזאם | גיטרה |

</figure>



**3.**

<figure dir="ltr" class="dbtable">

| TeacherName | InstName |
|:---:|:---:|
| אמיר עזאם | גיטרה |

</figure>



**4.**

<figure dir="ltr" class="dbtable">

| TeacherName | InstName |
|:---:|:---:|
| אמיר עזאם | גיטרה |
| דנה כהן | כינור |
| סמיר חלבי | עוד |

</figure>




**7.** 🟡 **השלמת ערכים:** כתבו את הערך שכל שאילתה תחזיר.

| # | השאילתה | הערך |
|:-:|---|:-:|
| 1 | `SELECT COUNT(*) FROM Registrations WHERE MonthlyFee >= 350` | ________ |
| 2 | `SELECT MAX(HourRate) FROM Teachers WHERE TeacherPhone IS NULL` | ________ |
| 3 | `SELECT AVG(MonthlyFee) FROM Registrations WHERE PupilLevel = "מתחיל"` | ________ |
| 4 | `SELECT LastName FROM Pupils WHERE PupilId = (SELECT LockerPupil FROM Lockers WHERE LockerNum = 3)` | ________ |
| 5 | `SELECT SUM(MonthlyFee) FROM Registrations WHERE RegPupil = 210` | ________ |

**8.** 🟡 איזו טבלה תתקבל? (צירוף של שלוש טבלאות)

```sql
SELECT FirstName, LastName, PupilLevel
FROM Pupils, Registrations, Teachers
WHERE PupilId = RegPupil
  AND RegTeacher = TeacherCode
  AND TeacherName = "רונית לוי";
```



**1.**

<figure dir="ltr" class="dbtable">

| FirstName | LastName | PupilLevel |
|:---:|:---:|:---:|
| מאיה | כהן | מתקדם |
| שירה | לוי | מתחיל |
| סאלי | חסון | מתחיל |

</figure>



**2.**

<figure dir="ltr" class="dbtable">

| FirstName | LastName | PupilLevel |
|:---:|:---:|:---:|
| שירה | לוי | ממשיך |
| ליאן | קבלאן | מתחיל |

</figure>



**3.**

<figure dir="ltr" class="dbtable">

| FirstName | LastName | PupilLevel |
|:---:|:---:|:---:|
| שירה | לוי | מתחיל |
| סאלי | חסון | מתחיל |

</figure>



**4.**

<figure dir="ltr" class="dbtable">

| FirstName | LastName | PupilLevel |
|:---:|:---:|:---:|
| רמי | חורי | מתקדם |
| עומר | ביטון | ממשיך |
| יואב | שושן | ממשיך |

</figure>




---

## חלק ג: תנאים מורכבים, DISTINCT וכינויים (סעיפים 3 ו‑6)

**9.** 🔴 שלושה תלמידים כתבו שאילתה שמציגה את התלמידים שגרים **בירכא (1) או בעכו (2)**, ונולדו **לפני 2012**. מי צדק? (ייתכן שיותר מתלמיד אחד.)

**נועה:**
```sql
SELECT FirstName, LastName FROM Pupils
WHERE HomeTown = 1 OR HomeTown = 2 AND BirthYear < 2012;
```

**ירין:**
```sql
SELECT FirstName, LastName FROM Pupils
WHERE (HomeTown = 1 OR HomeTown = 2) AND BirthYear < 2012;
```

**ליאב:**
```sql
SELECT FirstName, LastName FROM Pupils
WHERE HomeTown IN (1, 2) AND BirthYear < 2012;
```

**10.** 🟢 כמה שורות תחזיר כל שאילתה? ומה הן?
1. `SELECT LastName FROM Pupils WHERE LastName LIKE "ח%"`
2. `SELECT LastName FROM Pupils WHERE LastName LIKE "%ן"`
3. `SELECT LastName FROM Pupils WHERE LastName LIKE "_ו%"`
4. `SELECT TeacherName FROM Teachers WHERE TeacherName LIKE "%כהן%" OR HourRate BETWEEN 100 AND 110`

**11.** 🟢 מה ההבדל בין שתי השאילתות? כמה שורות תחזיר כל אחת?

```sql
SELECT RegTeacher FROM Registrations WHERE RegYear BETWEEN 2024 AND 2025;

SELECT DISTINCT RegTeacher FROM Registrations WHERE RegYear BETWEEN 2024 AND 2025;
```

**12.** 🟢 **כינויים (AS):** השלימו את השאילתה, כך שבכותרות של התוצאה יופיעו השמות Teacher ו‑NewRate (התשלום לשעה אחרי הנחה של 10%):

```sql
SELECT TeacherName ________ Teacher, HourRate * 0.9 ________ NewRate
FROM Teachers
WHERE HourRate ________ 130;
```

מה יופיע בשורה של רונית לוי?

---

## חלק ד: ניתוח פלט — איזו שאילתה הציגה את הטבלה? (סעיף 3)

**13.** 🟡 לאחר הרצה של שאילתה התקבלה הטבלה הזאת. איזו מבין השאילתות הציגה אותה?

<figure dir="ltr" class="dbtable">

| FirstName | LastName |
|:---:|:---:|
| מאיה | כהן |
| רמי | חורי |
| סאלי | חסון |
| יואב | שושן |

</figure>

**1.**

```sql
SELECT FirstName, LastName FROM Pupils WHERE HomeTown = 3 OR BirthYear = 2009
```

**2.**

```sql
SELECT FirstName, LastName FROM Pupils WHERE HomeTown = 3 AND BirthYear = 2009
```

**3.**

```sql
SELECT FirstName, LastName FROM Pupils WHERE BirthYear = 2009
```

**4.**

```sql
SELECT FirstName, BirthYear FROM Pupils WHERE HomeTown = 3 OR BirthYear = 2009
```


**14.** 🔴 לאחר הרצה של שאילתה התקבלה הטבלה הזאת. איזו מבין השאילתות הציגה אותה? שימו לב גם **לכותרות**.

<figure dir="ltr" class="dbtable">

| RegTeacher | Pupils_Count |
|:---:|:---:|
| 1 | 3 |
| 2 | 2 |
| 5 | 2 |

</figure>

**1.**

```sql
SELECT RegTeacher, COUNT(RegPupil) AS Pupils_Count FROM Registrations GROUP BY RegTeacher HAVING COUNT(RegPupil) >= 2
```

**2.**

```sql
SELECT RegTeacher, COUNT(RegPupil) AS Pupils_Count FROM Registrations WHERE RegYear >= 2024 GROUP BY RegTeacher
```

**3.**

```sql
SELECT RegTeacher, COUNT(RegPupil) AS Count_Pupils FROM Registrations WHERE RegYear >= 2024 GROUP BY RegTeacher HAVING COUNT(RegPupil) >= 2
```

**4.**

```sql
SELECT RegTeacher, COUNT(RegPupil) AS Pupils_Count FROM Registrations WHERE RegYear >= 2024 GROUP BY RegTeacher HAVING COUNT(RegPupil) >= 2
```


**15.** 🟡 לאחר הרצה של שאילתה התקבלה הטבלה הזאת. איזו מבין השאילתות הציגה אותה?

<figure dir="ltr" class="dbtable">

| CityName |
|:---:|
| ירכא |
| נהריה |
| עכו |

</figure>

**1.**

```sql
SELECT DISTINCT CityName FROM Cities, Pupils, Registrations WHERE CityCode = HomeTown AND PupilId = RegPupil AND RegTeacher = 1
```

**2.**

```sql
SELECT DISTINCT CityName FROM Cities, Pupils, Registrations WHERE CityCode = HomeTown AND PupilId = RegPupil AND RegTeacher IN (1, 5)
```

**3.**

```sql
SELECT CityName FROM Cities, Pupils, Registrations WHERE CityCode = HomeTown AND PupilId = RegPupil AND RegTeacher IN (1, 5)
```

**4.**

```sql
SELECT DISTINCT CityName FROM Cities, Pupils WHERE CityCode = HomeTown
```


---

## חלק ה: פונקציות קיבוץ, WHERE ו‑HAVING (סעיף 4)

**16.** 🟡 השלימו את השאילתה שמציגה לכל רמה (PupilLevel) את מספר הרישומים ואת התשלום החודשי הממוצע. רק רישומים **משנת 2024 ואילך**, ורק רמות שיש בהן **2 רישומים לפחות**:

```sql
SELECT PupilLevel, COUNT(*) AS Regs, ________(MonthlyFee) AS AvgFee
FROM Registrations
________ RegYear >= 2024
GROUP BY ________
________ COUNT(*) >= 2;
```

**17.** 🟡 כתבו שאילתה שמציגה לכל מורה (RegTeacher) את **סך** התשלומים החודשיים של התלמידים שלו, רק למורים שהסכום אצלם **גדול מ‑900**.

**18.** 🟢 כתבו את הערכים שהשאילתה תחזיר:

```sql
SELECT MIN(HourRate) AS Low, MAX(HourRate) AS High, SUM(HourRate) AS Total
FROM Teachers
WHERE TeachInst = 10;
```

---

## חלק ו: שאילתות מקוננות (סעיף 5)

**19.** 🟡 השלימו את השאילתה שמציגה את שמות המורים **שאין להם אף תלמיד**:

```sql
SELECT TeacherName
FROM Teachers
WHERE TeacherCode ________ (SELECT ________ FROM Registrations);
```

**20.** 🟡 כתבו שאילתה שמציגה את השם הפרטי ושם המשפחה של התלמידים **שאין להם לוקר**.

**21.** 🟡 כתבו שאילתה שמציגה את המורים שהתשלום לשעה שלהם **גבוה מהממוצע** של כל המורים.

**22.** 🔴 מה תציג השאילתה? תארו במילים, ואחר כך כתבו את הרשומות.

```sql
SELECT FirstName, LastName
FROM Pupils
WHERE PupilId IN (SELECT RegPupil FROM Registrations
                  WHERE RegTeacher IN (SELECT TeacherCode FROM Teachers
                                       WHERE TeachInst IN (SELECT InstCode FROM Instruments
                                                           WHERE InstFamily = "מיתר")));
```

---

## חלק ז: SELECT על טבלאות ועל שאילתות שמורות (סעיף 7)

**23.** 🔴 תלמיד שמר את השאילתה הזאת בשם **Q1**:

```sql
SELECT RegTeacher, COUNT(*) AS PupilsNum
FROM Registrations
GROUP BY RegTeacher;
```

1. כמה רשומות מחזירה Q1? מה הערך של PupilsNum עבור המורה 4?
2. השלימו את השאילתה שמשתמשת ב‑Q1 **כמו בטבלה**, ומציגה את שמות המורים שיש להם **3 תלמידים לפחות**:

```sql
SELECT TeacherName, PupilsNum
FROM Teachers, ________
WHERE TeacherCode = ________
  AND ________ >= 3;
```

**24.** 🔴 תלמיד שמר את השאילתה **Q2**: `SELECT MAX(MonthlyFee) AS TopFee FROM Registrations`. כתבו שאילתה שמשלבת את הטבלאות Pupils ו‑Registrations ואת Q2, ומציגה את השם הפרטי של התלמיד שמשלם את התשלום החודשי **הגבוה ביותר**, ואת התשלום.

---

## חלק ח: פקודות לשינוי נתונים ומבנה (עמוד 6 בהנחיות)

**25.** 🟢 התאימו לכל משימה את הפקודה:

| # | המשימה | הפקודה |
|:-:|---|:-:|
| 1 | לשנות ערך של שדה ברשומות קיימות | ________ |
| 2 | להוסיף שדה (עמודה) לטבלה | ________ |
| 3 | למחוק שדה (עמודה) מטבלה | ________ |
| 4 | לשנות את טיפוס הנתונים של שדה | ________ |
| 5 | למחוק רשומות מטבלה | ________ |
| 6 | להוסיף רשומה לטבלה | ________ |
| 7 | למחוק טבלה שלמה, כולל המבנה שלה | ________ |

**26.** 🟡 כל המורים לפסנתר (TeachInst = 10) מעלים את התשלום לשעה ב‑10%. כתבו את הפקודה. כמה רשומות יתעדכנו?

**27.** 🟢 בית הספר רוצה לשמור את כתובת הדוא"ל של כל תלמיד. כתבו פקודה שמוסיפה לטבלה Pupils שדה בשם Email מטיפוס טקסט.

**28.** 🟢 בית הספר החליט לא לשמור יותר את הטלפון של המורים. כתבו פקודה שמוחקת את השדה TeacherPhone מהטבלה Teachers.

**29.** 🟡 כתבו פקודה שמשנה את הטיפוס של השדה PupilLevel בטבלה Registrations ל‑`VARCHAR(20)`.

**30.** 🟡 כתבו פקודה שמוחקת את כל הרישומים משנת 2021 עד שנת 2022 (כולל). כמה רשומות יימחקו?

**31.** 🔴 תלמידה חדשה נרשמה: מספר 211, ג'וד סעב, ילידת 2013, גרה במעלות. היא תלמד אצל המורה 6 משנת 2025, ברמת "מתחיל", ותשלם 330 ש"ח בחודש. כתבו את **שתי** פקודות ה‑`INSERT`. באיזה סדר חייבים להריץ אותן, ולמה?

**32.** 🟢 מה ההבדל בין `DELETE FROM Lockers;` לבין `DROP TABLE Lockers;`?

**33.** 🟢 איזו מבין הפקודות **כתובה נכון**?
1. `ALTER TABLE Teachers DELETE COLUMN TeacherPhone`
2. `DROP COLUMN TeacherPhone FROM Teachers`
3. `ALTER TABLE Teachers DROP COLUMN TeacherPhone`
4. `UPDATE Teachers DROP TeacherPhone`

---

## חלק ט: עוד תרגול, לפי רמות

### 🟢 בסיסי

**34.** 🟢 כתבו שאילתה שמציגה את השם הפרטי ושם המשפחה של התלמידים שגרים **בנהריה** (קוד העיר 4).

**35.** 🟢 כמה שורות תחזיר השאילתה? `SELECT * FROM Instruments WHERE InstFamily <> "מיתר"`

**36.** 🟢 כתבו שאילתה שמציגה את שמות המורים ואת התשלום לשעה, **מהיקר לזול**.

**37.** 🟢 כתבו שאילתה שמציגה את מספרי הלוקרים ואת מספרי התלמידים של הלוקרים **בקומה 2**.

**38.** 🟢 איזו פקודה מוסיפה תלמיד חדש לטבלה Pupils?
1. `UPDATE Pupils ADD (212, "דן", "לוי", 2012, 1)`
2. `INSERT INTO Pupils VALUES (212, "דן", "לוי", 2012, 1)`
3. `ALTER TABLE Pupils ADD (212, "דן", "לוי", 2012, 1)`
4. `INSERT TABLE Pupils (212, "דן", "לוי", 2012, 1)`

### 🟡 בינוני

**39.** 🟡 כתבו שאילתה שמציגה את השם הפרטי של כל תלמיד **שיש לו לוקר בקומה 2**. (צירוף של Pupils ו‑Lockers.)

**40.** 🟡 כתבו שאילתה שמציגה לכל עיר את **שם** העיר ואת **מספר** התלמידים שגרים בה.

**41.** 🟡 איזו טבלה תתקבל?

```sql
SELECT InstFamily, COUNT(*) AS Instruments_Count
FROM Instruments
GROUP BY InstFamily
HAVING COUNT(*) > 1;
```



**1.**

<figure dir="ltr" class="dbtable">

| InstFamily | Instruments_Count |
|:---:|:---:|
| הקשה | 1 |
| מיתר | 3 |
| נשיפה | 1 |
| קלידים | 1 |

</figure>



**2.**

<figure dir="ltr" class="dbtable">

| InstFamily | Instruments_Count |
|:---:|:---:|
| הקשה | 1 |
| נשיפה | 1 |
| קלידים | 1 |

</figure>



**3.**

<figure dir="ltr" class="dbtable">

| InstFamily | Instruments_Count |
|:---:|:---:|
| מיתר | 3 |

</figure>



**4.**

<figure dir="ltr" class="dbtable">

| InstFamily | Instruments_Count |
|:---:|:---:|
| גיטרה | 1 |
| כינור | 1 |
| עוד | 1 |

</figure>




**42.** 🟡 השלימו את השאילתה שמציגה את המורים שיש בשם שלהם את האות **ר**, והתשלום לשעה שלהם **בין 100 ל‑130** (כולל):

```sql
SELECT TeacherName, HourRate
FROM Teachers
WHERE TeacherName ________ "________"
  ________ HourRate ________ 100 AND 130;
```

**43.** 🟡 כמה שורות תחזיר כל שאילתה?
1. `SELECT RegYear FROM Registrations`
2. `SELECT DISTINCT RegYear FROM Registrations`
3. `SELECT DISTINCT RegYear, PupilLevel FROM Registrations WHERE RegYear = 2025`

### 🔴 מתקדם

**44.** 🔴 לאחר הרצה של שאילתה התקבלה הטבלה הזאת. איזו מבין השאילתות הציגה אותה?

<figure dir="ltr" class="dbtable">

| FirstName | PupilLevel |
|:---:|:---:|
| אדם | מתחיל |
| תמר | ממשיך |
| יואב | מתקדם |

</figure>

**1.**

```sql
SELECT FirstName, PupilLevel FROM Pupils, Registrations WHERE PupilId = RegPupil AND RegTeacher = 3
```

**2.**

```sql
SELECT FirstName, PupilLevel FROM Pupils, Registrations, Teachers WHERE PupilId = RegPupil AND RegTeacher = TeacherCode AND TeacherName = "יוסי פרץ"
```

**3.**

```sql
SELECT FirstName, RegYear FROM Pupils, Registrations, Teachers WHERE PupilId = RegPupil AND RegTeacher = TeacherCode AND TeacherName = "יוסי פרץ"
```

**4.**

```sql
SELECT FirstName, PupilLevel FROM Pupils, Registrations, Teachers WHERE PupilId = RegPupil AND RegTeacher = TeacherCode AND TeacherName LIKE "%פרץ%" AND PupilLevel = "ממשיך"
```


**45.** 🔴 כתבו שאילתה שמציגה את שמות כלי הנגינה **שאף מורה לא מלמד**.

**46.** 🔴 כתבו שאילתה שמציגה את השם הפרטי של כל תלמיד ואת **סך** התשלומים החודשיים שלו, רק לתלמידים שמשלמים **יותר מ‑600** בחודש בסך הכול.

**47.** 🔴 מוחקים את כל הרישומים של התלמידים **שגרים בעכו**. השלימו, וכתבו כמה רשומות יימחקו:

```sql
________ FROM Registrations
WHERE RegPupil IN (SELECT ________ FROM Pupils
                   WHERE HomeTown = (SELECT ________ FROM Cities
                                     WHERE CityName = "עכו"));
```

**48.** 🔴 שלושה תלמידים כתבו שאילתה שמציגה **רק** את שם המורה שמקבל את התשלום לשעה **הגבוה ביותר**. מי צדק? (ייתכן שיותר מאחד.)

**נועה:**
```sql
SELECT TeacherName FROM Teachers ORDER BY HourRate DESC;
```

**ירין:**
```sql
SELECT TeacherName FROM Teachers
WHERE HourRate = (SELECT MAX(HourRate) FROM Teachers);
```

**ליאב** (השורה הראשונה שומרת את השאילתה Q3):
```sql
CREATE VIEW Q3 AS SELECT MAX(HourRate) AS TopRate FROM Teachers;
SELECT TeacherName FROM Teachers, Q3 WHERE HourRate = TopRate;
```

</div>
