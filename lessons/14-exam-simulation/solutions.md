<div dir="rtl">

# שיעור 14 — פתרונות

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../13-create-alter-drop/solutions.md) · [🏠 כל השיעורים](../README.md)

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
SELECT DISTINCT Sport
FROM   Clubs
WHERE  Price BETWEEN 150 AND 250;
```

<div dir="rtl">

| Sport |
|---|
| כדורגל |
| שחייה |
| כדורסל |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### שאלה 2

</div>

```sql
SELECT   TownCode, COUNT(*) AS N
FROM     Members
GROUP BY TownCode
HAVING   COUNT(*) >= 3;
```

<div dir="rtl">

| TownCode | N |
|---|---|
| 1 | 4 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### שאלה 3

</div>

```sql
SELECT FirstName
FROM   Members
WHERE  MemberId IN (SELECT MemberNum FROM ClubMembers WHERE ClubNum = 106)
  AND  Age < 16;
```

<div dir="rtl">

| FirstName |
|---|
| מאיה |
| כרים |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### שאלה 4

</div>

```sql
SELECT MAX(Price) - MIN(Price) AS Gap, COUNT(DISTINCT Sport) AS Sports
FROM   Clubs;
```

<div dir="rtl">

| Gap | Sports |
|---|---|
| 180 | 6 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### שאלה 5

</div>

```sql
SELECT COUNT(*)
FROM   ClubMembers
WHERE  ClubNum IN (SELECT ClubCode FROM Clubs WHERE Sport = 'כדורגל');
```

<div dir="rtl">

| COUNT(*) |
|---|
| 6 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### שאלה 6

</div>

```sql
SELECT   Sport, MIN(Price)
FROM     Clubs
GROUP BY Sport
HAVING   COUNT(*) = 2;
```

<div dir="rtl">

| Sport | MIN(Price) |
|---|---|
| כדורגל | 150 |
| שחייה | 220 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

---

## ✏️ תרגילים — ⚽ חוגי ספורט עירוניים

</div>

<div dir="rtl">

### 1. 🟢 הציגו את שמות החברים בני 15 ומטה, ממוינים לפי גיל.

</div>

```sql
SELECT FirstName, LastName, Age
FROM   Members
WHERE  Age <= 15
ORDER BY Age;
```

<div dir="rtl">

| FirstName | LastName | Age |
|---|---|---|
| רוני | אברהם | 13 |
| כרים | חלבי | 13 |
| אדם | חלבי | 14 |
| תמר | שושן | 14 |
| נור | עזאם | 15 |
| מאיה | לוי | 15 |
| עומר | ביטון | 15 |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 2. 🟢 הציגו את החוגים שהמחיר שלהם בין 140 ל‑200, ושמם מכיל 'כדור'.

</div>

```sql
SELECT ClubName, Price
FROM   Clubs
WHERE  Price BETWEEN 140 AND 200 AND ClubName LIKE '%כדור%';
```

<div dir="rtl">

| ClubName | Price |
|---|---|
| כדורגל צעירים | 150 |
| כדורגל בוגרים | 180 |
| כדורסל | 160 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 3. 🟢 הציגו את המאמנים שאין להם טלפון.

</div>

```sql
SELECT CoachFirstName, CoachLastName
FROM   Coaches
WHERE  Phone IS NULL;
```

<div dir="rtl">

| CoachFirstName | CoachLastName |
|---|---|
| מיכל | לוי |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 4. 🟡 הציגו את שם החבר ושם העיר שלו — רק חברים מירכא או מכרמיאל.

</div>

```sql
SELECT FirstName, LastName, CityName
FROM   Members, Cities
WHERE  TownCode = CityCode AND CityName IN ('ירכא', 'כרמיאל');
```

<div dir="rtl">

| FirstName | LastName | CityName |
|---|---|---|
| אדם | חלבי | ירכא |
| נור | עזאם | ירכא |
| יואב | כהן | כרמיאל |
| מאיה | לוי | כרמיאל |
| כרים | חלבי | ירכא |
| ג'וד | מנסור | ירכא |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 5. 🟡 לכל ענף (`Sport`): מספר החוגים והמחיר הממוצע.

</div>

```sql
SELECT   Sport, COUNT(*) AS Clubs, AVG(Price) AS AvgPrice
FROM     Clubs
GROUP BY Sport;
```

<div dir="rtl">

| Sport | Clubs | AvgPrice |
|---|---|---|
| ג'ודו | 1 | 140.0 |
| טניס | 1 | 300.0 |
| יוגה | 1 | 120.0 |
| כדורגל | 2 | 165.0 |
| כדורסל | 1 | 160.0 |
| שחייה | 2 | 235.0 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 6. 🟡 הציגו את שמות החברים בחוג 'כדורגל צעירים'.

</div>

```sql
SELECT FirstName, LastName
FROM   Members, ClubMembers, Clubs
WHERE  MemberId = MemberNum AND ClubNum = ClubCode
  AND  ClubName = 'כדורגל צעירים';
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| אדם | חלבי |
| רוני | אברהם |
| עומר | ביטון |
| כרים | חלבי |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 7. 🟡 חוגים שהמחיר שלהם גבוה מהמחיר הממוצע.

</div>

```sql
SELECT ClubName, Price
FROM   Clubs
WHERE  Price > (SELECT AVG(Price) FROM Clubs);
```

<div dir="rtl">

| ClubName | Price |
|---|---|
| שחייה מתחילים | 220 |
| שחייה מתקדמים | 250 |
| טניס | 300 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 8. 🔴 חברים שרשומים ל‑2 חוגים או יותר (שמות), ומה הם משלמים בסך הכול בחודש.

</div>

```sql
SELECT   FirstName, LastName, COUNT(*) AS Clubs, SUM(Price) AS Total
FROM     Members, ClubMembers, Clubs
WHERE    MemberId = MemberNum AND ClubNum = ClubCode
GROUP BY MemberId, FirstName, LastName
HAVING   COUNT(*) >= 2;
```

<div dir="rtl">

| FirstName | LastName | Clubs | Total |
|---|---|---|---|
| אדם | חלבי | 2 | 310 |
| יואב | כהן | 2 | 480 |
| מאיה | לוי | 2 | 360 |
| סאלי | חסון | 2 | 410 |
| כרים | חלבי | 2 | 290 |
| ליאור | לוי | 2 | 340 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 9. 🔴 לכל מאמן (שם): כמה חברים הוא מאמן בסך הכול בכל החוגים שלו?

</div>

```sql
SELECT   CoachFirstName, CoachLastName, COUNT(*) AS Members
FROM     Coaches, Clubs, ClubMembers
WHERE    CoachCode = TrainerCode AND ClubCode = ClubNum
GROUP BY CoachCode, CoachFirstName, CoachLastName;
```

<div dir="rtl">

| CoachFirstName | CoachLastName | Members |
|---|---|---|
| סאמר | חלבי | 6 |
| מיכל | לוי | 4 |
| ראמי | עזאם | 6 |
| דנה | כהן | 2 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 10. 🔴 ערים שאף חבר לא גר בהן.

</div>

```sql
SELECT CityName
FROM   Cities
WHERE  CityCode NOT IN (SELECT TownCode FROM Members);
```

<div dir="rtl">

| CityName |
|---|
| שפרעם |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 11. 🔴 נתונה השאילתה השמורה Q1 — סך התשלום החודשי לכל חבר. הציגו את שם החבר שמשלם הכי הרבה.

</div>

```sql
CREATE VIEW Q1 AS
SELECT   MemberNum, SUM(Price) AS Total
FROM     ClubMembers, Clubs
WHERE    ClubNum = ClubCode
GROUP BY MemberNum;

SELECT FirstName, LastName, Total
FROM   Q1, Members
WHERE  MemberNum = MemberId
  AND  Total = (SELECT MAX(Total) FROM Q1);
```

<div dir="rtl">

| FirstName | LastName | Total |
|---|---|---|
| יואב | כהן | 480 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 12. 🟡 העלו ב‑10% את המחיר של כל חוגי השחייה.

</div>

```sql
UPDATE Clubs
SET    Price = ROUND(Price * 1.1)
WHERE  Sport = 'שחייה';
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT ClubName, Price FROM Clubs;
```

<div dir="rtl">

| ClubName | Price |
|---|---|
| כדורגל צעירים | 150 |
| כדורגל בוגרים | 180 |
| שחייה מתחילים | 242 |
| שחייה מתקדמים | 275 |
| כדורסל | 160 |
| טניס | 300 |
| ג'ודו | 140 |
| יוגה | 120 |

**התוצאה: 8 שורות**

</div>

<div dir="rtl">

### 13. 🟡 מחקו את החוג שאין בו אף חבר.

</div>

```sql
DELETE FROM Clubs
WHERE  ClubCode NOT IN (SELECT ClubNum FROM ClubMembers);
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT ClubCode, ClubName FROM Clubs;
```

<div dir="rtl">

| ClubCode | ClubName |
|---|---|
| 100 | כדורגל צעירים |
| 101 | כדורגל בוגרים |
| 102 | שחייה מתחילים |
| 103 | שחייה מתקדמים |
| 104 | כדורסל |
| 105 | טניס |
| 106 | ג'ודו |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 14. 🟡 הוסיפו לטבלת החברים עמודה `Phone` מסוג טקסט.

</div>

```sql
ALTER TABLE Members ADD COLUMN Phone TEXT;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT MemberId, FirstName, Phone FROM Members LIMIT 3;
```

<div dir="rtl">

| MemberId | FirstName | Phone |
|---|---|---|
| 1001 | אדם | *NULL* |
| 1002 | נור | *NULL* |
| 1003 | יואב | *NULL* |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 15. 🟢 החברים שהצטרפו בשנת 2025, לפי שם משפחה.

</div>

```sql
SELECT FirstName, LastName
FROM   Members
WHERE  JoinYear = 2025
ORDER BY LastName;
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| עומר | ביטון |
| כרים | חלבי |
| מאיה | לוי |
| ג'וד | מנסור |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 16. 🟡 לכל עיר (שם): כמה חברים גרים בה, כולל ערים בלי חברים.

</div>

```sql
SELECT    CityName, COUNT(MemberId) AS Members
FROM      Cities
LEFT JOIN Members ON CityCode = TownCode
GROUP BY  CityName;
```

<div dir="rtl">

| CityName | Members |
|---|---|
| חיפה | 2 |
| ירכא | 4 |
| כרמיאל | 2 |
| נהריה | 2 |
| עכו | 2 |
| שפרעם | 0 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 17. 🟡 חברים (שמות) שאינם רשומים לאף חוג כדורגל.

</div>

```sql
SELECT FirstName, LastName
FROM   Members
WHERE  MemberId NOT IN (SELECT MemberNum FROM ClubMembers, Clubs
                       WHERE  ClubNum = ClubCode AND Sport = 'כדורגל');
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| נור | עזאם |
| מאיה | לוי |
| סאלי | חסון |
| שירה | כהן |
| תמר | שושן |
| ג'וד | מנסור |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 18. 🔴 החוג (או החוגים) עם הכי הרבה חברים.

</div>

```sql
CREATE VIEW Q1 AS
SELECT   ClubNum, COUNT(*) AS N
FROM     ClubMembers
GROUP BY ClubNum;

SELECT ClubName, N
FROM   Q1, Clubs
WHERE  ClubNum = ClubCode AND N = (SELECT MAX(N) FROM Q1);
```

<div dir="rtl">

| ClubName | N |
|---|---|
| כדורגל צעירים | 4 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 19. 🔴 הגיל הממוצע של החברים בכל ענף (`Sport`), מעוגל לספרה אחת.

</div>

```sql
SELECT   Sport, ROUND(AVG(Age), 1) AS AvgAge
FROM     Clubs, ClubMembers, Members
WHERE    ClubCode = ClubNum AND MemberNum = MemberId
GROUP BY Sport;
```

<div dir="rtl">

| Sport | AvgAge |
|---|---|
| ג'ודו | 14.7 |
| טניס | 16.0 |
| כדורגל | 14.7 |
| כדורסל | 16.0 |
| שחייה | 15.3 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 20. 🟡 מחקו את החבר 1012 מכל החוגים.

</div>

```sql
DELETE FROM ClubMembers
WHERE  MemberNum = 1012;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT COUNT(*) AS Left FROM ClubMembers;
```

<div dir="rtl">

| Left |
|---|
| 17 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

---

## 🎓 בסגנון הבחינה — 🔧 מעבדת "דלתא‑טק"

</div>

<div dir="rtl">

### 1. 🟢 התיקונים שעדיין פתוחים (`DoneDate` ריק), לפי תאריך קבלה.

</div>

```sql
SELECT RepairNum, CustName, InDate
FROM   Repairs
WHERE  DoneDate IS NULL
ORDER BY InDate;
```

<div dir="rtl">

| RepairNum | CustName | InDate |
|---|---|---|
| 1004 | שירה לוי | 2026-02-14 |
| 1008 | עומר ביטון | 2026-04-05 |
| 1014 | הילה פרץ | 2026-07-03 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 2. 🟢 הטכנאים מירכא (לפי שם העיר).

</div>

```sql
SELECT TechFirst, TechLast
FROM   Technicians, Cities
WHERE  TechCity = CityCode AND CityName = 'ירכא';
```

<div dir="rtl">

| TechFirst | TechLast |
|---|---|
| נביל | סרחאן |
| דנה | כהן |
| סאמר | חלבי |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 3. 🟡 לכל משפחת מכשירים: מספר התיקונים וסך המחירים.

</div>

```sql
SELECT   DevFamily, COUNT(*) AS Repairs, SUM(RepairPrice) AS Total
FROM     Repairs, DevTypes
WHERE    RepairDev = DevCode
GROUP BY DevFamily;
```

<div dir="rtl">

| DevFamily | Repairs | Total |
|---|---|---|
| לבישים | 3 | 540 |
| מחשבים | 6 | 6390 |
| סלולר | 7 | 3000 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 4. 🟡

</div>

```sql
SELECT DISTINCT TechFirst
FROM   Technicians, Repairs
WHERE  TechCode = RepairTech AND Priority = 'דחוף';
```

<div dir="rtl">

| TechFirst |
|---|
| חוסאם |
| נביל |
| סאמר |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 5. 🟡 השלימו את הערכים.

</div>

```sql
SELECT COUNT(*), SUM(UseQty)
FROM   PartUsage
WHERE  UsePart = 101;
```

<div dir="rtl">

| COUNT(*) | SUM(UseQty) |
|---|---|
| 5 | 5 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 6. 🔴 שם הלקוח, שם החלף ומחיר החלף — לכל חלף שהוחלף בתיקון של מחשב נייד (4 טבלאות).

</div>

```sql
SELECT CustName, PartName, PartPrice
FROM   Repairs, PartUsage, Parts, DevTypes
WHERE  RepairNum = UseRepair AND UsePart = PartCode
  AND  RepairDev = DevCode AND DevName = 'מחשב נייד';
```

<div dir="rtl">

| CustName | PartName | PartPrice |
|---|---|---|
| מאיה כהן | סוללה | 180 |
| מאיה כהן | מקלדת | 220 |
| עומר ביטון | מסך | 450 |
| עומר ביטון | מקלדת | 220 |
| אלון כהן | סוללה | 180 |
| אלון כהן | מקלדת | 220 |
| אורי שמש | מסך | 450 |
| אורי שמש | מצלמה | 160 |

**התוצאה: 8 שורות**

</div>

<div dir="rtl">

### 7. 🔴 טכנאים (שמות) שהמחיר הממוצע של התיקונים שלהם גבוה מהממוצע הכללי.

</div>

```sql
SELECT   TechFirst, TechLast, AVG(RepairPrice) AS AvgPrice
FROM     Technicians, Repairs
WHERE    TechCode = RepairTech
GROUP BY TechCode, TechFirst, TechLast
HAVING   AVG(RepairPrice) > (SELECT AVG(RepairPrice) FROM Repairs);
```

<div dir="rtl">

| TechFirst | TechLast | AvgPrice |
|---|---|---|
| חוסאם | זיאד | 1110.0 |
| סאמר | חלבי | 1120.0 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 8. 🟡 סגרו את התיקון 1004: עדכנו את `DoneDate` ל‑'2026-02-20'.

</div>

```sql
UPDATE Repairs
SET    DoneDate = '2026-02-20'
WHERE  RepairNum = 1004;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT RepairNum, DoneDate FROM Repairs WHERE RepairNum = 1004;
```

<div dir="rtl">

| RepairNum | DoneDate |
|---|---|
| 1004 | 2026-02-20 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 9. 🔴 השלימו את הפקודה שמוחקת את החלפים שלא השתמשו בהם אף פעם.

</div>

```sql
DELETE FROM Parts
WHERE  PartCode NOT IN (SELECT UsePart FROM PartUsage);
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT PartName FROM Parts;
```

<div dir="rtl">

| PartName |
|---|
| מסך |
| סוללה |
| שקע טעינה |
| רמקול |
| מקלדת |
| מצלמה |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

---

## 🏠 תרגול נוסף — 📚 ספרייה עירונית

</div>

<div dir="rtl">

### 1. 🟢 ספרים שיצאו לאור אחרי 2000, ממוינים לפי שנה.

</div>

```sql
SELECT Title, PubYear
FROM   Books
WHERE  PubYear > 2000
ORDER BY PubYear;
```

<div dir="rtl">

| Title | PubYear |
|---|---|
| סיפור על אהבה וחושך | 2002 |
| אשה בורחת מבשורה | 2008 |
| סוס אחד נכנס לבר | 2014 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 2. 🟡 שם הספר ושם הסופר של כל ספר.

</div>

```sql
SELECT Title, AuthorFirstName, AuthorLastName
FROM   Books, Authors
WHERE  WriterCode = AuthorCode;
```

<div dir="rtl">

| Title | AuthorFirstName | AuthorLastName |
|---|---|---|
| סיפור על אהבה וחושך | עמוס | עוז |
| הארי פוטר ואבן החכמים | ג'ואן | רולינג |
| הארי פוטר וחדר הסודות | ג'ואן | רולינג |
| סמטת מדק | נגיב | מחפוז |
| רצח באוריינט אקספרס | אגתה | כריסטי |
| ואז לא נשאר אף אחד | אגתה | כריסטי |
| סוס אחד נכנס לבר | דויד | גרוסמן |
| אשה בורחת מבשורה | דויד | גרוסמן |
| מיכאל שלי | עמוס | עוז |
| ספר הדקדוק הפנימי | דויד | גרוסמן |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 3. 🟡 השאלות שעדיין לא הוחזרו: שם הקורא ושם הספר.

</div>

```sql
SELECT FirstName, LastName, Title
FROM   Loans, Members, Books
WHERE  ReaderId = MemberId AND BookNum = BookCode
  AND  ReturnDate IS NULL;
```

<div dir="rtl">

| FirstName | LastName | Title |
|---|---|---|
| ראניה | חלבי | הארי פוטר וחדר הסודות |
| נועה | לוי | סוס אחד נכנס לבר |
| עידו | כהן | ואז לא נשאר אף אחד |
| יעל | פרץ | הארי פוטר ואבן החכמים |
| ראניה | חלבי | רצח באוריינט אקספרס |
| הילה | כהן | סיפור על אהבה וחושך |
| אליאס | חורי | סמטת מדק |
| אמיר | חלבי | אשה בורחת מבשורה |

**התוצאה: 8 שורות**

</div>

<div dir="rtl">

### 4. 🟡 לכל קורא (שם): כמה ספרים השאיל?

</div>

```sql
SELECT   FirstName, LastName, COUNT(*) AS Loans
FROM     Members, Loans
WHERE    MemberId = ReaderId
GROUP BY MemberId, FirstName, LastName;
```

<div dir="rtl">

| FirstName | LastName | Loans |
|---|---|---|
| ראניה | חלבי | 3 |
| עידו | כהן | 2 |
| מוחמד | עזאם | 2 |
| נועה | לוי | 1 |
| אליאס | חורי | 2 |
| יעל | פרץ | 1 |
| סאמי | קבלאן | 1 |
| הילה | כהן | 1 |
| אמיר | חלבי | 1 |

**התוצאה: 9 שורות**

</div>

<div dir="rtl">

### 5. 🔴 ספרים שאף פעם לא הושאלו.

</div>

```sql
SELECT Title
FROM   Books
WHERE  BookCode NOT IN (SELECT BookNum FROM Loans);
```

<div dir="rtl">

| Title |
|---|
| ספר הדקדוק הפנימי |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 6. 🔴 הספר (או הספרים) עם מספר העמודים הגדול ביותר, ושם הסופר.

</div>

```sql
SELECT Title, Pages, AuthorLastName
FROM   Books, Authors
WHERE  WriterCode = AuthorCode
  AND  Pages = (SELECT MAX(Pages) FROM Books);
```

<div dir="rtl">

| Title | Pages | AuthorLastName |
|---|---|---|
| אשה בורחת מבשורה | 640 | גרוסמן |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 7. 🟡 הסופרים שאין להם אף ספר בספרייה.

</div>

```sql
SELECT AuthorFirstName, AuthorLastName
FROM   Authors
WHERE  AuthorCode NOT IN (SELECT WriterCode FROM Books);
```

<div dir="rtl">

| AuthorFirstName | AuthorLastName |
|---|---|
| סמי | מיכאל |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 8. 🔴 לכל ז'אנר: מספר ההשאלות (רק ז'אנרים שהושאלו).

</div>

```sql
SELECT   Genre, COUNT(*) AS Loans
FROM     Books, Loans
WHERE    BookCode = BookNum
GROUP BY Genre;
```

<div dir="rtl">

| Genre | Loans |
|---|---|
| ביוגרפיה | 1 |
| מתח | 3 |
| פנטזיה | 4 |
| רומן | 6 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 9. 🔴 הוסיפו לטבלת ההשאלות עמודה `Fine` (קנס) עם ברירת מחדל 0, ותנו קנס של 20 לכל השאלה שלא הוחזרה.

</div>

```sql
ALTER TABLE Loans ADD COLUMN Fine INTEGER DEFAULT 0;
UPDATE Loans SET Fine = 20 WHERE ReturnDate IS NULL;
```

<div dir="rtl">

בדיקה:

</div>

```sql
SELECT Fine, COUNT(*) AS Loans FROM Loans GROUP BY Fine;
```

<div dir="rtl">

| Fine | Loans |
|---|---|
| 0 | 6 |
| 20 | 8 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../13-create-alter-drop/solutions.md) · [🏠 כל השיעורים](../README.md)

</div>
