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

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../13-create-alter-drop/solutions.md) · [🏠 כל השיעורים](../README.md)

</div>
