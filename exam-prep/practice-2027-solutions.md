<!-- generated from .moodle_build/assessments/sql_practice2027.src.md -->
<div dir="rtl">

# פתרונות: תרגול לפי ההנחיות של תשפ"ז

> כל התשובות כאן חושבו מהרצה אמיתית של השאילתות על [`db/music.sql`](db/music.sql). השאלות: [practice-2027.md](practice-2027.md).

## חלק א

**1.**

| # | צד המפתח הראשי | צד המפתח הזר |
|:-:|:---:|:---:|
| 1 | CityCode | HomeTown |
| 2 | InstCode | TeachInst |
| 3 | PupilId | RegPupil |
| 4 | TeacherCode | RegTeacher |
| 5 | PupilId | LockerPupil |

**איך מוצאים?** שמות השדות ייחודיים, ולכן מפתח זר **לא** נקרא כמו המפתח הראשי שהוא מפנה אליו. מחפשים שדה שהוא "קוד של משהו אחר", ובודקים בנתונים: הערכים של HomeTown (1–4) הם קודים של ערים.

**2.**
1. **לא נכון.** התלמיד 201 רשום אצל שני מורים, ולכן הערך 201 חוזר בשדה RegPupil. המפתח הראשי **מורכב**: (RegPupil, RegTeacher).
2. **נכון.** RegPupil מפנה ל‑Pupils, ו‑RegTeacher מפנה ל‑Teachers. כך בנויה טבלה מקשרת.
3. **נכון.** לתלמיד יכולים להיות כמה מורים, ולמורה יש כמה תלמידים. הקשר ממומש דרך הטבלה המקשרת Registrations.
4. **נכון.** כל לוקר שייך לתלמיד אחד, וכל תלמיד מופיע **פעם אחת לכל היותר** ב‑LockerPupil (השדה מוגדר `UNIQUE`).
5. **לא נכון.** אף שדה ב‑Instruments לא מפנה לטבלה אחרת. זו טבלת עזר.

**3.** **יחיד לרבים (1:N).** כלי אחד (פסנתר, 10) נלמד אצל כמה מורים (2 ו‑6), ולכל מורה יש כלי אחד. צד ה"רבים" הוא Teachers, ושם נמצא המפתח הזר TeachInst.

**4.** לתלמיד יכולים להיות **כמה** מורים (לאדם 201 יש שניים). בשדה אחד אפשר לשמור רק מורה אחד. לכן קשר רבים לרבים דורש **טבלה מקשרת** (Registrations), שבה כל רישום הוא שורה נפרדת.

## חלק ב

**5.** תשובה **3**. `BETWEEN` **כולל** את 2010 ואת 2012. בתשובה 1 חסרים ילידי 2010 ו‑2012.

**6.** תשובה **4**. משפחת "מיתר" כוללת גיטרה, כינור ועוד. המיון לפי TeacherName הוא בסדר עולה (א'–ת').

**7.**

| # | הערך | הסבר |
|:-:|:-:|---|
| 1 | 5 | `>=` כולל גם את 350 |
| 2 | 130 | רק אמיר (110) ונור (130) בלי טלפון |
| 3 | 338 | ממוצע של 5 רישומים ברמת "מתחיל" |
| 4 | קבלאן | לוקר 3 שייך לתלמיד 207 |
| 5 | 620 | 300 + 320 |

**8.** תשובה **1**. מחברים שלוש טבלאות, ולכן צריך **שני** תנאי חיבור (`PupilId = RegPupil`, `RegTeacher = TeacherCode`).

## חלק ג

**9.** **ירין וליאב.** `AND` מתבצע **לפני** `OR`. אצל נועה התנאי הוא בעצם `HomeTown = 1 OR (HomeTown = 2 AND BirthYear < 2012)`, ולכן כל תלמידי ירכא מופיעים, גם אלה שנולדו ב‑2012 וב‑2013. הסוגריים של ירין, או `IN` של ליאב, פותרים את זה.

נועה:

<figure dir="ltr" class="dbtable">

| FirstName | LastName |
|:---:|:---:|
| אדם | חלבי |
| כרים | עזאם |
| שירה | לוי |
| רמי | חורי |
| ליאן | קבלאן |
| יואב | שושן |

</figure>

ירין וליאב (התוצאה הנכונה):

<figure dir="ltr" class="dbtable">

| FirstName | LastName |
|:---:|:---:|
| שירה | לוי |
| רמי | חורי |
| ליאן | קבלאן |
| יואב | שושן |

</figure>

**10.**

1\. **3** שורות: שמות שמתחילים ב"ח".

<figure dir="ltr" class="dbtable">

| LastName |
|:---:|
| חלבי |
| חורי |
| חסון |

</figure>

2\. **5** שורות: שמות שמסתיימים ב"ן". שימו לב: גם "כהן" מסתיים ב"ן".

<figure dir="ltr" class="dbtable">

| LastName |
|:---:|
| כהן |
| קבלאן |
| ביטון |
| חסון |
| שושן |

</figure>

3\. **3** שורות: האות **השנייה** היא ו (`_` הוא תו **אחד** בדיוק).

<figure dir="ltr" class="dbtable">

| LastName |
|:---:|
| לוי |
| חורי |
| שושן |

</figure>

4\. **3** שורות: עם `OR` מספיק שאחד התנאים יתקיים. דנה כהן מופיעה בגלל השם, ואמיר ויוסי בגלל התשלום (`BETWEEN` כולל את 100 ואת 110).

<figure dir="ltr" class="dbtable">

| TeacherName |
|:---:|
| אמיר עזאם |
| דנה כהן |
| יוסי פרץ |

</figure>

**11.** בלי `DISTINCT` מתקבלת שורה לכל רישום: **9** שורות, וקודי מורים חוזרים. עם `DISTINCT` כל מורה מופיע פעם אחת: **5** שורות.

<figure dir="ltr" class="dbtable">

| RegTeacher |
|:---:|
| 1 |
| 5 |
| 2 |
| 4 |
| 3 |

</figure>

**12.** `AS` · `AS` · ואחרי HourRate אחד מאלה: `>=` או `>` (כל תנאי שמשאיר את רונית). למשל:

```sql
SELECT TeacherName AS Teacher, HourRate * 0.9 AS NewRate
FROM Teachers
WHERE HourRate >= 130;
```

<figure dir="ltr" class="dbtable">

| Teacher | NewRate |
|:---:|:---:|
| רונית לוי | 135 |
| דנה כהן | 126 |
| נור מנסור | 117 |

</figure>

בשורה של רונית לוי: Teacher = רונית לוי, NewRate = 135.

## חלק ד

**13.** תשובה **1**. בתוצאה יש את תלמידי כרמיאל (מאיה, סאלי) **וגם** את ילידי 2009 (רמי, יואב), ולכן זה `OR`. בתשובה 2 יש `AND`, ובתשובה 3 חסרות תלמידות כרמיאל. בתשובה 4 הכותרת השנייה היא BirthYear ולא LastName.

**14.** תשובה **4**. שימו לב שהכותרת היא **Pupils_Count**, ולכן תשובה 3 (Count_Pupils) נפסלת. בתשובה 1 אין `WHERE`, ולכן נספרים גם רישומים ישנים. בתשובה 2 אין `HAVING`, ולכן מופיע גם מורה עם תלמיד אחד.

**15.** תשובה **2**. בלי `DISTINCT` (תשובה 3) "ירכא" הייתה מופיעה כמה פעמים. בתשובה 1 חסרות נהריה ועכו, כי הן מגיעות מהמורה 5.

## חלק ה

**16.** `AVG` · `WHERE` · `PupilLevel` · `HAVING`

```sql
SELECT PupilLevel, COUNT(*) AS Regs, AVG(MonthlyFee) AS AvgFee
FROM Registrations
WHERE RegYear >= 2024
GROUP BY PupilLevel
HAVING COUNT(*) >= 2;
```

<figure dir="ltr" class="dbtable">

| PupilLevel | Regs | AvgFee |
|:---:|:---:|:---:|
| ממשיך | 4 | 310 |
| מתחיל | 5 | 338 |

</figure>

**הכלל:** תנאי על **שורה** (השנה) כותבים ב‑`WHERE`, לפני הקיבוץ. תנאי על **פונקציית קיבוץ** (`COUNT`) כותבים ב‑`HAVING`, אחרי הקיבוץ.

**17.**

```sql
SELECT RegTeacher, SUM(MonthlyFee) AS TotalFees
FROM Registrations
GROUP BY RegTeacher
HAVING SUM(MonthlyFee) > 900;
```

<figure dir="ltr" class="dbtable">

| RegTeacher | TotalFees |
|:---:|:---:|
| 1 | 940 |
| 2 | 1160 |
| 3 | 960 |

</figure>

**18.** רק המורים לפסנתר (רונית ונור):

<figure dir="ltr" class="dbtable">

| Low | High | Total |
|:---:|:---:|:---:|
| 130 | 150 | 280 |

</figure>

## חלק ו

**19.** `NOT IN` · `RegTeacher`

<figure dir="ltr" class="dbtable">

| TeacherName |
|:---:|
| נור מנסור |

</figure>

**20.**

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

**21.**

```sql
SELECT TeacherName, HourRate
FROM Teachers
WHERE HourRate > (SELECT AVG(HourRate) FROM Teachers);
```

הממוצע הוא 125:

<figure dir="ltr" class="dbtable">

| TeacherName | HourRate |
|:---:|:---:|
| רונית לוי | 150 |
| דנה כהן | 140 |
| נור מנסור | 130 |

</figure>

**22.** קוראים **מבפנים החוצה**: (1) הכלים ממשפחת "מיתר", (2) המורים שמלמדים אותם, (3) הרישומים אצל המורים האלה, (4) שמות התלמידים. כלומר: **התלמידים שלומדים כלי מיתר**.

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

## חלק ז

**23.** 1. Q1 מחזירה **5** רשומות, רשומה לכל מורה שיש לו תלמידים. למורה 4 יש **2** תלמידים.
2. `Q1` · `RegTeacher` · `PupilsNum`

```sql
CREATE VIEW Q1 AS
SELECT RegTeacher, COUNT(*) AS PupilsNum FROM Registrations GROUP BY RegTeacher;

SELECT TeacherName, PupilsNum
FROM Teachers, Q1
WHERE TeacherCode = RegTeacher
  AND PupilsNum >= 3;
```

<figure dir="ltr" class="dbtable">

| TeacherName | PupilsNum |
|:---:|:---:|
| סמיר חלבי | 3 |
| רונית לוי | 3 |
| אמיר עזאם | 3 |
| יוסי פרץ | 3 |

</figure>

> **שאילתה שמורה** (ב‑Access) היא **VIEW** ב‑SQL: שאילתה עם שם, שמשתמשים בה ב‑`FROM` כמו בטבלה.

**24.**

```sql
CREATE VIEW Q2 AS SELECT MAX(MonthlyFee) AS TopFee FROM Registrations;

SELECT FirstName, MonthlyFee
FROM Pupils, Registrations, Q2
WHERE PupilId = RegPupil
  AND MonthlyFee = TopFee;
```

<figure dir="ltr" class="dbtable">

| FirstName | MonthlyFee |
|:---:|:---:|
| מאיה | 400 |

</figure>

## חלק ח

**25.**

| # | המשימה | הפקודה |
|:-:|---|---|
| 1 | לשנות ערך של שדה | `UPDATE ... SET ... WHERE ...` |
| 2 | להוסיף שדה | `ALTER TABLE ... ADD ...` |
| 3 | למחוק שדה | `ALTER TABLE ... DROP COLUMN ...` |
| 4 | לשנות טיפוס של שדה | `ALTER TABLE ... MODIFY COLUMN ...` |
| 5 | למחוק רשומות | `DELETE FROM ... WHERE ...` |
| 6 | להוסיף רשומה | `INSERT INTO ... VALUES (...)` |
| 7 | למחוק טבלה שלמה | `DROP TABLE ...` |

**26.**

```sql
UPDATE Teachers
SET HourRate = HourRate * 1.1
WHERE TeachInst = 10;
```

יתעדכנו **2** רשומות (רונית ונור). ⚠️ בלי `WHERE` **כל** המורים היו מתעדכנים.

**27.**

```sql
ALTER TABLE Pupils ADD Email TEXT;
```

השדה החדש ריק (NULL) בכל הרשומות הקיימות.

**28.**

```sql
ALTER TABLE Teachers DROP COLUMN TeacherPhone;
```

**29.**

```sql
-- MySQL
ALTER TABLE Registrations MODIFY COLUMN PupilLevel VARCHAR(20);
```

> 💻 **לבדיקה:** `MODIFY COLUMN` היא פקודה של MySQL, ו‑SQLite לא מכיר אותה. כדי להריץ אותה, בחרו ב‑OneCompiler את **MySQL** ([onecompiler.com/mysql](https://onecompiler.com/mysql)), הדביקו את `music.sql` והוסיפו את הפקודה. בבחינה כותבים אותה בדיוק כך.

**30.**

```sql
DELETE FROM Registrations
WHERE RegYear BETWEEN 2021 AND 2022;
```

יימחקו **3** רשומות (`BETWEEN` כולל את 2021 ואת 2022).

**31.** קודם את התלמידה, ורק אחר כך את הרישום:

```sql
INSERT INTO Pupils (PupilId, FirstName, LastName, BirthYear, HomeTown)
VALUES (211, "ג'וד", "סעב", 2013, 5);

INSERT INTO Registrations (RegPupil, RegTeacher, RegYear, PupilLevel, MonthlyFee)
VALUES (211, 6, 2025, "מתחיל", 330);
```

**למה בסדר הזה?** RegPupil הוא **מפתח זר**: הערך 211 חייב להיות קיים קודם ב‑Pupils. אי אפשר לרשום למורה תלמידה שעוד לא קיימת.

**32.** `DELETE FROM Lockers` מוחק את **כל הרשומות**, אבל הטבלה (המבנה שלה) **נשארת**, ריקה. `DROP TABLE Lockers` מוחק את הטבלה **כולה**, כולל המבנה, ואחריה אי אפשר להכניס לטבלה רשומות.

**33.** תשובה **3**. מוחקים שדה עם `ALTER TABLE ... DROP COLUMN`. אין `DELETE COLUMN` (1), `DROP` לבד מוחק טבלה ולא שדה (2), ו‑`UPDATE` משנה ערכים, לא מבנה (4).


## חלק ט

**34.**

```sql
SELECT FirstName, LastName FROM Pupils WHERE HomeTown = 4;
```

<figure dir="ltr" class="dbtable">

| FirstName | LastName |
|:---:|:---:|
| תמר | אברהם |
| עומר | ביטון |

</figure>

**35.** **3** שורות. `<>` פירושו "שונה מ": פסנתר, תופים וחליל.

**36.**

```sql
SELECT TeacherName, HourRate FROM Teachers ORDER BY HourRate DESC;
```

<figure dir="ltr" class="dbtable">

| TeacherName | HourRate |
|:---:|:---:|
| רונית לוי | 150 |
| דנה כהן | 140 |
| נור מנסור | 130 |
| סמיר חלבי | 120 |
| אמיר עזאם | 110 |
| יוסי פרץ | 100 |

</figure>

**37.**

```sql
SELECT LockerNum, LockerPupil FROM Lockers WHERE LockerFloor = 2;
```

<figure dir="ltr" class="dbtable">

| LockerNum | LockerPupil |
|:---:|:---:|
| 3 | 207 |
| 4 | 210 |
| 5 | 201 |

</figure>

**38.** תשובה **2**. מוסיפים **רשומה** עם `INSERT INTO ... VALUES`. `ALTER TABLE` משנה את **המבנה**, `UPDATE` משנה רשומות **קיימות**, ו‑`INSERT TABLE` אינו כתיב של SQL.

**39.**

```sql
SELECT FirstName
FROM Pupils, Lockers
WHERE PupilId = LockerPupil
  AND LockerFloor = 2;
```

<figure dir="ltr" class="dbtable">

| FirstName |
|:---:|
| ליאן |
| יואב |
| אדם |

</figure>

**40.**

```sql
SELECT CityName, COUNT(*) AS Pupils_Count
FROM Cities, Pupils
WHERE CityCode = HomeTown
GROUP BY CityName;
```

<figure dir="ltr" class="dbtable">

| CityName | Pupils_Count |
|:---:|:---:|
| ירכא | 3 |
| כרמיאל | 2 |
| נהריה | 2 |
| עכו | 3 |

</figure>

מעלות לא מופיעה: אין בה אף תלמיד, ולכן אין לה אף שורה אחרי הצירוף.

**41.** תשובה **3**. רק למשפחת "מיתר" יש יותר מכלי אחד. בתשובה 1 אין `HAVING`, ולכן מופיעות כל המשפחות.

**42.** `LIKE` · `%ר%` · `AND` · `BETWEEN`

<figure dir="ltr" class="dbtable">

| TeacherName | HourRate |
|:---:|:---:|
| סמיר חלבי | 120 |
| אמיר עזאם | 110 |
| יוסי פרץ | 100 |
| נור מנסור | 130 |

</figure>

**43.** 1. **14** שורות, שורה לכל רישום. 2. **5** שורות, כל שנה פעם אחת. 3. **1** (שורה אחת). `DISTINCT` על **שתי** עמודות מוריד שורה רק כששני הערכים חוזרים, וב‑2025 כל 5 הרישומים הם (2025, "מתחיל").

**44.** תשובה **2**. יוסי פרץ הוא המורה **5**, ולכן תשובה 1 (מורה 3) נפסלת. בתשובה 3 הכותרת השנייה היא RegYear, ובתשובה 4 חסרים התלמידים שאינם ברמת "ממשיך".

**45.**

```sql
SELECT InstName
FROM Instruments
WHERE InstCode NOT IN (SELECT TeachInst FROM Teachers);
```

<figure dir="ltr" class="dbtable">

| InstName |
|:---:|
| חליל |

</figure>

**46.**

```sql
SELECT FirstName, SUM(MonthlyFee) AS TotalFee
FROM Pupils, Registrations
WHERE PupilId = RegPupil
GROUP BY PupilId, FirstName
HAVING SUM(MonthlyFee) > 600;
```

<figure dir="ltr" class="dbtable">

| FirstName | TotalFee |
|:---:|:---:|
| שירה | 740 |
| ליאן | 670 |
| יואב | 620 |

</figure>

מקבצים לפי **PupilId** (ולא רק לפי השם), כי יכולים להיות שני תלמידים עם אותו שם פרטי.

**47.** `DELETE` · `PupilId` · `CityCode`. יימחקו **5** רשומות (של שירה, רמי ויואב).

**48.** **ירין וליאב.** שתי השאילתות מחזירות רק את רונית לוי. השאילתה של ליאב משתמשת בשאילתה שמורה במקום בתת־שאילתה, וזה אותו רעיון. נועה **מיינה** את כל המורים, ולכן קיבלה את **כולם** (6 שורות), ולא רק את הראשון.

</div>
