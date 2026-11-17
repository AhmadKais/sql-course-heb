<div dir="rtl">

# שיעור 8 — פתרונות

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../07-group-by-having/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../09-joins-3-tables-left-join/solutions.md)

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
SELECT FirstName, CityName
FROM   Pupils, Cities;
```

<div dir="rtl">

| FirstName | CityName |
|---|---|
| אדם | ירכא |
| אדם | עכו |
| אדם | כרמיאל |
| אדם | נהריה |
| אדם | מעלות |
| מאיה | ירכא |
| מאיה | עכו |
| מאיה | כרמיאל |
| מאיה | נהריה |
| מאיה | מעלות |
| כרים | ירכא |
| כרים | עכו |
| כרים | כרמיאל |
| כרים | נהריה |
| כרים | מעלות |
| שירה | ירכא |
| שירה | עכו |
| שירה | כרמיאל |
| שירה | נהריה |
| שירה | מעלות |
| רמי | ירכא |
| רמי | עכו |
| רמי | כרמיאל |
| רמי | נהריה |
| רמי | מעלות |
| … | … |

**התוצאה: 50 שורות** — מוצגות 25 הראשונות

> 💡 10 תלמידים × 5 ערים = 50. כל תלמיד "גר" בכל עיר — תוצאה שגויה.

</div>

<div dir="rtl">

### שאלה 2

</div>

```sql
SELECT CityName
FROM   Pupils, Cities
WHERE  HomeTown = CityCode AND FirstName = 'עומר';
```

<div dir="rtl">

| CityName |
|---|
| נהריה |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### שאלה 3

</div>

```sql
SELECT InstName
FROM   Teachers, Instruments
WHERE  TeachInst = InstCode AND HourRate > 130;
```

<div dir="rtl">

| InstName |
|---|
| פסנתר |
| כינור |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### שאלה 4

</div>

```sql
SELECT COUNT(*)
FROM   Lockers, Pupils
WHERE  LockerPupil = PupilId AND HomeTown = 2;
```

<div dir="rtl">

| COUNT(*) |
|---|
| 2 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

---

## ✏️ תרגילים — 🎵 בית הספר למוזיקה "צלילים"

</div>

<div dir="rtl">

### 1. 🟢 הציגו את שם המורה ואת שם הכלי שלו (בתחביר פסיק + `WHERE`).

</div>

```sql
SELECT TeacherName, InstName
FROM   Teachers, Instruments
WHERE  TeachInst = InstCode;
```

<div dir="rtl">

| TeacherName | InstName |
|---|---|
| סמיר חלבי | עוד |
| רונית לוי | פסנתר |
| אמיר עזאם | גיטרה |
| דנה כהן | כינור |
| יוסי פרץ | תופים |
| נור מנסור | פסנתר |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 2. 🟢 הציגו את מספר הלוקר, הקומה ושם התלמיד שמחזיק בו.

</div>

```sql
SELECT LockerNum, LockerFloor, FirstName, LastName
FROM   Lockers, Pupils
WHERE  LockerPupil = PupilId;
```

<div dir="rtl">

| LockerNum | LockerFloor | FirstName | LastName |
|---|---|---|---|
| 1 | 1 | מאיה | כהן |
| 2 | 1 | רמי | חורי |
| 3 | 2 | ליאן | קבלאן |
| 4 | 2 | יואב | שושן |
| 5 | 2 | אדם | חלבי |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 3. 🟢 הציגו את שם התלמיד ושם העיר — רק לתלמידים מעכו.

</div>

```sql
SELECT FirstName, LastName
FROM   Pupils, Cities
WHERE  HomeTown = CityCode AND CityName = 'עכו';
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| שירה | לוי |
| רמי | חורי |
| יואב | שושן |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 4. 🟡 הציגו לכל רישום: שם התלמיד, הרמה והתשלום.

</div>

```sql
SELECT FirstName, LastName, PupilLevel, MonthlyFee
FROM   Registrations, Pupils
WHERE  RegPupil = PupilId;
```

<div dir="rtl">

| FirstName | LastName | PupilLevel | MonthlyFee |
|---|---|---|---|
| אדם | חלבי | ממשיך | 320 |
| אדם | חלבי | מתחיל | 280 |
| מאיה | כהן | מתקדם | 400 |
| כרים | עזאם | מתחיל | 300 |
| שירה | לוי | ממשיך | 360 |
| שירה | לוי | מתחיל | 380 |
| רמי | חורי | מתקדם | 340 |
| תמר | אברהם | ממשיך | 280 |
| ליאן | קבלאן | מתחיל | 350 |
| ליאן | קבלאן | ממשיך | 320 |
| עומר | ביטון | ממשיך | 300 |
| סאלי | חסון | מתחיל | 380 |
| יואב | שושן | מתקדם | 300 |
| יואב | שושן | ממשיך | 320 |

**התוצאה: 14 שורות**

</div>

<div dir="rtl">

### 5. 🟡 הציגו לכל רישום: שם המורה, השנה והתשלום — רק רישומי 2025.

</div>

```sql
SELECT TeacherName, RegYear, MonthlyFee
FROM   Registrations, Teachers
WHERE  RegTeacher = TeacherCode AND RegYear = 2025;
```

<div dir="rtl">

| TeacherName | RegYear | MonthlyFee |
|---|---|---|
| יוסי פרץ | 2025 | 280 |
| סמיר חלבי | 2025 | 300 |
| רונית לוי | 2025 | 380 |
| דנה כהן | 2025 | 350 |
| רונית לוי | 2025 | 380 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 6. 🟡 הציגו את המורים לפסנתר (לפי **שם** הכלי, לא לפי הקוד).

</div>

```sql
SELECT TeacherName
FROM   Teachers, Instruments
WHERE  TeachInst = InstCode AND InstName = 'פסנתר';
```

<div dir="rtl">

| TeacherName |
|---|
| רונית לוי |
| נור מנסור |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 7. 🟡 הציגו את התלמידים שיש להם לוקר בקומה 2, ממוינים לפי שם.

</div>

```sql
SELECT FirstName, LastName, LockerNum
FROM   Pupils
JOIN   Lockers ON LockerPupil = PupilId
WHERE  LockerFloor = 2
ORDER BY FirstName;
```

<div dir="rtl">

| FirstName | LastName | LockerNum |
|---|---|---|
| אדם | חלבי | 5 |
| יואב | שושן | 4 |
| ליאן | קבלאן | 3 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 8. 🔴 לכל מורה (לפי **שם**): כמה רישומים יש לו?

</div>

```sql
SELECT   TeacherName, COUNT(*) AS Regs
FROM     Teachers, Registrations
WHERE    TeacherCode = RegTeacher
GROUP BY TeacherName;
```

<div dir="rtl">

| TeacherName | Regs |
|---|---|
| אמיר עזאם | 3 |
| דנה כהן | 2 |
| יוסי פרץ | 3 |
| סמיר חלבי | 3 |
| רונית לוי | 3 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 9. 🔴 לכל משפחת כלים: כמה מורים מלמדים בה, ומה המחיר הממוצע?

</div>

```sql
SELECT   InstFamily, COUNT(*) AS Teachers, AVG(HourRate) AS AvgRate
FROM     Teachers, Instruments
WHERE    TeachInst = InstCode
GROUP BY InstFamily;
```

<div dir="rtl">

| InstFamily | Teachers | AvgRate |
|---|---|---|
| הקשה | 1 | 100.0 |
| מיתר | 3 | 123.33 |
| קלידים | 2 | 140.0 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 10. 🔴 שמות התלמידים שמשלמים בסך הכול יותר מ‑600 בחודש.

</div>

```sql
SELECT   FirstName, LastName, SUM(MonthlyFee) AS Total
FROM     Pupils, Registrations
WHERE    PupilId = RegPupil
GROUP BY PupilId, FirstName, LastName
HAVING   SUM(MonthlyFee) > 600;
```

<div dir="rtl">

| FirstName | LastName | Total |
|---|---|---|
| שירה | לוי | 740 |
| ליאן | קבלאן | 670 |
| יואב | שושן | 620 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 11. 🟢 הציגו את שם התלמיד ושם העיר — לתלמידים שנולדו ב‑2012.

</div>

```sql
SELECT FirstName, CityName
FROM   Pupils, Cities
WHERE  HomeTown = CityCode AND BirthYear = 2012;
```

<div dir="rtl">

| FirstName | CityName |
|---|---|
| אדם | ירכא |
| תמר | נהריה |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 12. 🟢 הציגו את שם המורה ואת משפחת הכלי שהוא מלמד.

</div>

```sql
SELECT TeacherName, InstFamily
FROM   Teachers, Instruments
WHERE  TeachInst = InstCode;
```

<div dir="rtl">

| TeacherName | InstFamily |
|---|---|
| סמיר חלבי | מיתר |
| רונית לוי | קלידים |
| אמיר עזאם | מיתר |
| דנה כהן | מיתר |
| יוסי פרץ | הקשה |
| נור מנסור | קלידים |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 13. 🟡 הציגו את המורים שמלמדים כלי ממשפחת 'קלידים' או 'הקשה'.

</div>

```sql
SELECT TeacherName, InstName
FROM   Teachers, Instruments
WHERE  TeachInst = InstCode AND InstFamily IN ('קלידים', 'הקשה');
```

<div dir="rtl">

| TeacherName | InstName |
|---|---|
| רונית לוי | פסנתר |
| יוסי פרץ | תופים |
| נור מנסור | פסנתר |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 14. 🟡 הציגו לכל רישום ברמת 'מתקדם' את שם התלמיד והשנה, ממוין לפי שנה.

</div>

```sql
SELECT FirstName, LastName, RegYear
FROM   Pupils, Registrations
WHERE  PupilId = RegPupil AND PupilLevel = 'מתקדם'
ORDER BY RegYear;
```

<div dir="rtl">

| FirstName | LastName | RegYear |
|---|---|---|
| רמי | חורי | 2021 |
| מאיה | כהן | 2022 |
| יואב | שושן | 2022 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 15. 🟡 הציגו את שמות התלמידים שיש להם לוקר, ואת שם העיר שלהם (3 טבלאות).

</div>

```sql
SELECT FirstName, CityName, LockerNum
FROM   Pupils, Cities, Lockers
WHERE  HomeTown = CityCode AND PupilId = LockerPupil;
```

<div dir="rtl">

| FirstName | CityName | LockerNum |
|---|---|---|
| אדם | ירכא | 5 |
| מאיה | כרמיאל | 1 |
| רמי | עכו | 2 |
| ליאן | ירכא | 3 |
| יואב | עכו | 4 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 16. 🔴 לכל עיר (שם): שנת הלידה הממוצעת של התלמידים שגרים בה.

</div>

```sql
SELECT   CityName, AVG(BirthYear) AS AvgYear
FROM     Pupils, Cities
WHERE    HomeTown = CityCode
GROUP BY CityName;
```

<div dir="rtl">

| CityName | AvgYear |
|---|---|
| ירכא | 2012.0 |
| כרמיאל | 2012.0 |
| נהריה | 2011.0 |
| עכו | 2009.67 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 17. 🔴 מורים (שמות) שסכום התשלומים אצלם גבוה מ‑900.

</div>

```sql
SELECT   TeacherName, SUM(MonthlyFee) AS Total
FROM     Teachers, Registrations
WHERE    TeacherCode = RegTeacher
GROUP BY TeacherCode, TeacherName
HAVING   SUM(MonthlyFee) > 900;
```

<div dir="rtl">

| TeacherName | Total |
|---|---|
| סמיר חלבי | 940 |
| רונית לוי | 1160 |
| אמיר עזאם | 960 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

---

## 🎓 בסגנון הבחינה — 📚 ספרייה עירונית

</div>

<div dir="rtl">

### 1. 🟢 הציגו את שם הספר ואת שם המשפחה של הסופר.

</div>

```sql
SELECT Title, AuthorLastName
FROM   Books, Authors
WHERE  WriterCode = AuthorCode;
```

<div dir="rtl">

| Title | AuthorLastName |
|---|---|
| סיפור על אהבה וחושך | עוז |
| הארי פוטר ואבן החכמים | רולינג |
| הארי פוטר וחדר הסודות | רולינג |
| סמטת מדק | מחפוז |
| רצח באוריינט אקספרס | כריסטי |
| ואז לא נשאר אף אחד | כריסטי |
| סוס אחד נכנס לבר | גרוסמן |
| אשה בורחת מבשורה | גרוסמן |
| מיכאל שלי | עוז |
| ספר הדקדוק הפנימי | גרוסמן |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 2. 🟢 הציגו את שם הקורא ואת שם העיר שלו.

</div>

```sql
SELECT FirstName, LastName, CityName
FROM   Members, Cities
WHERE  TownCode = CityCode;
```

<div dir="rtl">

| FirstName | LastName | CityName |
|---|---|---|
| ראניה | חלבי | ירכא |
| עידו | כהן | כרמיאל |
| מוחמד | עזאם | ירכא |
| נועה | לוי | עכו |
| אליאס | חורי | עכו |
| יעל | פרץ | כרמיאל |
| סאמי | קבלאן | מעלות |
| הילה | כהן | חיפה |
| אמיר | חלבי | ירכא |
| רותם | גבאי | מעלות |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 3. 🟡 הציגו את הספרים שכתבו סופרים מבריטניה.

</div>

```sql
SELECT Title
FROM   Books, Authors
WHERE  WriterCode = AuthorCode AND Country = 'בריטניה';
```

<div dir="rtl">

| Title |
|---|
| הארי פוטר ואבן החכמים |
| הארי פוטר וחדר הסודות |
| רצח באוריינט אקספרס |
| ואז לא נשאר אף אחד |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 4. 🟡 הציגו לכל השאלה את מספר ההשאלה ואת שם הקורא — רק השאלות שלא הוחזרו.

</div>

```sql
SELECT LoanId, FirstName, LastName
FROM   Loans, Members
WHERE  ReaderId = MemberId AND ReturnDate IS NULL;
```

<div dir="rtl">

| LoanId | FirstName | LastName |
|---|---|---|
| 2 | ראניה | חלבי |
| 5 | נועה | לוי |
| 7 | עידו | כהן |
| 8 | יעל | פרץ |
| 10 | ראניה | חלבי |
| 11 | הילה | כהן |
| 12 | אליאס | חורי |
| 14 | אמיר | חלבי |

**התוצאה: 8 שורות**

</div>

<div dir="rtl">

### 5. 🟡 השלימו את הערכים בטבלה שתתקבל.

</div>

```sql
SELECT Title, PubYear
FROM   Books, Authors
WHERE  WriterCode = AuthorCode AND AuthorLastName = 'עוז';
```

<div dir="rtl">

| Title | PubYear |
|---|---|
| סיפור על אהבה וחושך | 2002 |
| מיכאל שלי | 1968 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 6. 🔴

</div>

```sql
SELECT   Country, COUNT(*) AS Books
FROM     Books, Authors
WHERE    WriterCode = AuthorCode
GROUP BY Country;
```

<div dir="rtl">

| Country | Books |
|---|---|
| בריטניה | 4 |
| ישראל | 5 |
| מצרים | 1 |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

### 7. 🔴 השלימו כך שיוצגו שמות הקוראים מירכא.

</div>

```sql
SELECT FirstName, LastName
FROM   Members, Cities
WHERE  TownCode = CityCode AND CityName = 'ירכא';
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| ראניה | חלבי |
| מוחמד | עזאם |
| אמיר | חלבי |

**התוצאה: 3 שורות**

</div>

<div dir="rtl">

---

## 🏠 תרגול נוסף — 🏫 בית הספר "עתיד"

</div>

<div dir="rtl">

### 1. 🟢 הציגו את שם התלמיד ואת שם הכיתה שלו.

</div>

```sql
SELECT FirstName, LastName, ClassName
FROM   Students, Classes
WHERE  Students.ClassCode = Classes.ClassCode;
```

<div dir="rtl">

| FirstName | LastName | ClassName |
|---|---|---|
| אדם | חלבי | י1 |
| נור | עזאם | י1 |
| יואב | כהן | י1 |
| מאיה | לוי | י2 |
| רוני | אברהם | י2 |
| סאלי | חסון | י2 |
| עומר | ביטון | יא1 |
| שירה | כהן | יא1 |
| כרים | חלבי | יא1 |
| תמר | שושן | יא2 |
| ליאור | לוי | יא2 |
| ג'וד | מנסור | יא2 |
| דניאל | פרץ | יב1 |
| הדיל | סעיד | יב1 |
| איתי | גולן | יב1 |
| ראניה | עבאס | יב1 |
| נועם | שחר | י1 |

**התוצאה: 17 שורות**

</div>

<div dir="rtl">

### 2. 🟢 הציגו את שם המקצוע ושם המורה שמלמד אותו.

</div>

```sql
SELECT CourseName, FirstName, LastName
FROM   Courses, Teachers
WHERE  Courses.TeacherCode = Teachers.TeacherCode;
```

<div dir="rtl">

| CourseName | FirstName | LastName |
|---|---|---|
| מתמטיקה 5 יח"ל | נביל | סרחאן |
| אנגלית 4 יח"ל | רונית | בר-לב |
| מבוא לבסיסי נתונים | חוסאם | זיאד |
| היסטוריה | אורלי | שמש |
| חינוך גופני | פאדי | חדאד |
| מתמטיקה 3 יח"ל | גלית | מזרחי |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 3. 🟡 הציגו את המורים שגרים בחיפה (לפי שם העיר).

</div>

```sql
SELECT FirstName, LastName
FROM   Teachers T, Cities C
WHERE  T.CityCode = C.CityCode AND C.CityName = 'חיפה';
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| רונית | בר-לב |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### 4. 🟡 הציגו לכל כיתה את שמה ואת שם המחנך/ת.

</div>

```sql
SELECT ClassName, FirstName, LastName
FROM   Classes
JOIN   Teachers ON Classes.TeacherCode = Teachers.TeacherCode;
```

<div dir="rtl">

| ClassName | FirstName | LastName |
|---|---|---|
| י1 | נביל | סרחאן |
| י2 | רונית | בר-לב |
| יא1 | חוסאם | זיאד |
| יא2 | גלית | מזרחי |
| יב1 | אורלי | שמש |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 5. 🔴 כמה תלמידים יש בכל כיתה — לפי **שם** הכיתה, מהגדולה לקטנה.

</div>

```sql
SELECT   ClassName, COUNT(*) AS Students
FROM     Students S, Classes C
WHERE    S.ClassCode = C.ClassCode
GROUP BY ClassName
ORDER BY Students DESC;
```

<div dir="rtl">

| ClassName | Students |
|---|---|
| יב1 | 4 |
| י1 | 4 |
| יא2 | 3 |
| יא1 | 3 |
| י2 | 3 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 6. 🔴 שמות התלמידים שנעדרו לפחות פעמיים.

</div>

```sql
SELECT   FirstName, LastName, COUNT(*) AS Absences
FROM     Students S, Absences A
WHERE    S.StudentId = A.StudentId
GROUP BY S.StudentId, FirstName, LastName
HAVING   COUNT(*) >= 2;
```

<div dir="rtl">

| FirstName | LastName | Absences |
|---|---|---|
| יואב | כהן | 2 |
| כרים | חלבי | 3 |
| ג'וד | מנסור | 4 |
| איתי | גולן | 2 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 7. 🟢 הציגו את שם התלמיד ושם העיר שלו.

</div>

```sql
SELECT S.FirstName, S.LastName, C.CityName
FROM   Students S, Cities C
WHERE  S.CityCode = C.CityCode;
```

<div dir="rtl">

| FirstName | LastName | CityName |
|---|---|---|
| אדם | חלבי | ירכא |
| נור | עזאם | ירכא |
| יואב | כהן | כרמיאל |
| מאיה | לוי | חיפה |
| רוני | אברהם | עכו |
| סאלי | חסון | עכו |
| עומר | ביטון | נהריה |
| שירה | כהן | חיפה |
| כרים | חלבי | ירכא |
| תמר | שושן | נהריה |
| ג'וד | מנסור | שפרעם |
| דניאל | פרץ | כרמיאל |
| הדיל | סעיד | שפרעם |
| איתי | גולן | חיפה |
| ראניה | עבאס | שפרעם |
| נועם | שחר | חיפה |
| לינא | חמוד | עכו |

**התוצאה: 17 שורות**

</div>

<div dir="rtl">

### 8. 🟡 הציגו את המקצועות שמלמדים מורים למתמטיקה.

</div>

```sql
SELECT C.CourseName, T.FirstName
FROM   Courses C, Teachers T
WHERE  C.TeacherCode = T.TeacherCode AND T.Subject = 'מתמטיקה';
```

<div dir="rtl">

| CourseName | FirstName |
|---|---|
| מתמטיקה 5 יח"ל | נביל |
| מתמטיקה 3 יח"ל | גלית |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 9. 🟡 הציגו את ההיעדרויות של תלמידי הכיתה 104 (שם תלמיד + תאריך).

</div>

```sql
SELECT S.FirstName, A.AbsenceDate
FROM   Students S, Absences A
WHERE  S.StudentId = A.StudentId AND S.ClassCode = 104;
```

<div dir="rtl">

| FirstName | AbsenceDate |
|---|---|
| ג'וד | 2026-09-02 |
| ג'וד | 2026-09-10 |
| ג'וד | 2026-09-15 |
| ג'וד | 2026-09-16 |
| תמר | 2026-09-08 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 10. 🔴 לכל עיר (שם): כמה מורים גרים בה.

</div>

```sql
SELECT   C.CityName, COUNT(*) AS Teachers
FROM     Teachers T, Cities C
WHERE    T.CityCode = C.CityCode
GROUP BY C.CityName;
```

<div dir="rtl">

| CityName | Teachers |
|---|---|
| חיפה | 1 |
| ירכא | 2 |
| כרמיאל | 1 |
| נהריה | 1 |
| עכו | 1 |
| שפרעם | 1 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../07-group-by-having/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../09-joins-3-tables-left-join/solutions.md)

</div>
