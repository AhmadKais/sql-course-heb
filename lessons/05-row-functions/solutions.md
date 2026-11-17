<div dir="rtl">

# שיעור 5 — פתרונות

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../04-order-by/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../06-aggregates/solutions.md)

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
SELECT 7 / 2, 7 / 2.0, ROUND(7 / 3.0, 2);
```

<div dir="rtl">

| 7 / 2 | 7 / 2.0 | ROUND(7 / 3.0, 2) |
|---|---|---|
| 3 | 3.5 | 2.33 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### שאלה 2

</div>

```sql
SELECT SUBSTR('סמיר חלבי', 1, 4) AS Part;
```

<div dir="rtl">

| Part |
|---|
| סמיר |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### שאלה 3

</div>

```sql
SELECT TeacherName, LENGTH(TeacherName) AS L
FROM   Teachers
WHERE  LENGTH(TeacherName) = 9;
```

<div dir="rtl">

| TeacherName | L |
|---|---|
| סמיר חלבי | 9 |
| רונית לוי | 9 |
| אמיר עזאם | 9 |
| נור מנסור | 9 |

**התוצאה: 4 שורות**

> 💡 גם הרווח הוא תו.

</div>

<div dir="rtl">

### שאלה 4

</div>

```sql
SELECT LENGTH('פסנתר'), SUBSTR('050-1234567', 5, 3);
```

<div dir="rtl">

| LENGTH('פסנתר') | SUBSTR('050-1234567', 5, 3) |
|---|---|
| 5 | 123 |

**התוצאה: שורה אחת**

</div>

<div dir="rtl">

### שאלה 5

</div>

```sql
SELECT InstName,
       CASE WHEN InstFamily = 'מיתר' THEN 'כן' ELSE 'לא' END AS Strings
FROM   Instruments;
```

<div dir="rtl">

| InstName | Strings |
|---|---|
| פסנתר | לא |
| גיטרה | כן |
| כינור | כן |
| תופים | לא |
| חליל | לא |
| עוד | כן |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

---

## ✏️ תרגילים — 🎵 בית הספר למוזיקה "צלילים"

</div>

<div dir="rtl">

### 1. 🟢 הציגו לכל רישום את קוד התלמיד ואת התשלום לחצי שנה (6 חודשים), בשם `HalfYear`.

</div>

```sql
SELECT RegPupil, MonthlyFee * 6 AS HalfYear
FROM   Registrations;
```

<div dir="rtl">

| RegPupil | HalfYear |
|---|---|
| 201 | 1920 |
| 201 | 1680 |
| 202 | 2400 |
| 203 | 1800 |
| 204 | 2160 |
| 204 | 2280 |
| 205 | 2040 |
| 206 | 1680 |
| 207 | 2100 |
| 207 | 1920 |
| 208 | 1800 |
| 209 | 2280 |
| 210 | 1800 |
| 210 | 1920 |

**התוצאה: 14 שורות**

</div>

<div dir="rtl">

### 2. 🟢 הציגו את השם המלא של התלמידים בפורמט: שם משפחה, פסיק, שם פרטי (למשל `חלבי, אדם`).

</div>

```sql
SELECT LastName || ', ' || FirstName AS FullName
FROM   Pupils;
```

<div dir="rtl">

| FullName |
|---|
| חלבי, אדם |
| כהן, מאיה |
| עזאם, כרים |
| לוי, שירה |
| חורי, רמי |
| אברהם, תמר |
| קבלאן, ליאן |
| ביטון, עומר |
| חסון, סאלי |
| שושן, יואב |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 3. 🟢 הציגו את שם המורה ואת אורך השם שלו.

</div>

```sql
SELECT TeacherName, LENGTH(TeacherName) AS NameLen
FROM   Teachers;
```

<div dir="rtl">

| TeacherName | NameLen |
|---|---|
| סמיר חלבי | 9 |
| רונית לוי | 9 |
| אמיר עזאם | 9 |
| דנה כהן | 7 |
| יוסי פרץ | 8 |
| נור מנסור | 9 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 4. 🟡 הציגו את האות הראשונה של השם הפרטי של כל תלמיד, בשם `Initial`.

</div>

```sql
SELECT FirstName, SUBSTR(FirstName, 1, 1) AS Initial
FROM   Pupils;
```

<div dir="rtl">

| FirstName | Initial |
|---|---|
| אדם | א |
| מאיה | מ |
| כרים | כ |
| שירה | ש |
| רמי | ר |
| תמר | ת |
| ליאן | ל |
| עומר | ע |
| סאלי | ס |
| יואב | י |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 5. 🟡 הציגו את המחיר לדקה של כל מורה (מחיר לשעה חלקי 60), מעוגל ל‑2 ספרות.

</div>

```sql
SELECT TeacherName, ROUND(HourRate / 60.0, 2) AS PerMinute
FROM   Teachers;
```

<div dir="rtl">

| TeacherName | PerMinute |
|---|---|
| סמיר חלבי | 2.0 |
| רונית לוי | 2.5 |
| אמיר עזאם | 1.83 |
| דנה כהן | 2.33 |
| יוסי פרץ | 1.67 |
| נור מנסור | 2.17 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 6. 🟡 הציגו את שם המורה ואת הטלפון, ובמקום NULL את הטקסט 'לא ידוע'.

</div>

```sql
SELECT TeacherName, IFNULL(TeacherPhone, 'לא ידוע') AS Phone
FROM   Teachers;
```

<div dir="rtl">

| TeacherName | Phone |
|---|---|
| סמיר חלבי | 050-1234567 |
| רונית לוי | 052-2345678 |
| אמיר עזאם | לא ידוע |
| דנה כהן | 054-4567890 |
| יוסי פרץ | 053-5678901 |
| נור מנסור | לא ידוע |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 7. 🟡 הציגו תלמידים ששם המשפחה שלהם ארוך מ‑3 אותיות.

</div>

```sql
SELECT FirstName, LastName
FROM   Pupils
WHERE  LENGTH(LastName) > 3;
```

<div dir="rtl">

| FirstName | LastName |
|---|---|
| אדם | חלבי |
| כרים | עזאם |
| רמי | חורי |
| תמר | אברהם |
| ליאן | קבלאן |
| עומר | ביטון |
| סאלי | חסון |
| יואב | שושן |

**התוצאה: 8 שורות**

</div>

<div dir="rtl">

### 8. 🔴 הציגו לכל תלמיד את שמו ואת 'צעיר' אם נולד ב‑2012 ואילך, אחרת 'בוגר'. בשם `AgeGroup`.

</div>

```sql
SELECT FirstName, BirthYear,
       CASE WHEN BirthYear >= 2012 THEN 'צעיר' ELSE 'בוגר' END AS AgeGroup
FROM   Pupils;
```

<div dir="rtl">

| FirstName | BirthYear | AgeGroup |
|---|---|---|
| אדם | 2012 | צעיר |
| מאיה | 2010 | בוגר |
| כרים | 2013 | צעיר |
| שירה | 2011 | בוגר |
| רמי | 2009 | בוגר |
| תמר | 2012 | צעיר |
| ליאן | 2011 | בוגר |
| עומר | 2010 | בוגר |
| סאלי | 2014 | צעיר |
| יואב | 2009 | בוגר |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 9. 🔴 הציגו לכל רישום את התשלום ואת התשלום אחרי הנחה: 10% למתחילים, 5% לממשיכים, ובלי הנחה למתקדמים.

</div>

```sql
SELECT RegPupil, PupilLevel, MonthlyFee,
       CASE PupilLevel
         WHEN 'מתחיל' THEN MonthlyFee * 0.9
         WHEN 'ממשיך' THEN MonthlyFee * 0.95
         ELSE MonthlyFee
       END AS AfterDiscount
FROM   Registrations;
```

<div dir="rtl">

| RegPupil | PupilLevel | MonthlyFee | AfterDiscount |
|---|---|---|---|
| 201 | ממשיך | 320 | 304.0 |
| 201 | מתחיל | 280 | 252.0 |
| 202 | מתקדם | 400 | 400 |
| 203 | מתחיל | 300 | 270.0 |
| 204 | ממשיך | 360 | 342.0 |
| 204 | מתחיל | 380 | 342.0 |
| 205 | מתקדם | 340 | 340 |
| 206 | ממשיך | 280 | 266.0 |
| 207 | מתחיל | 350 | 315.0 |
| 207 | ממשיך | 320 | 304.0 |
| 208 | ממשיך | 300 | 285.0 |
| 209 | מתחיל | 380 | 342.0 |
| 210 | מתקדם | 300 | 300 |
| 210 | ממשיך | 320 | 304.0 |

**התוצאה: 14 שורות**

</div>

<div dir="rtl">

### 10. 🔴 הציגו את מספר הטלפון של המורים בלי המקף (רמז: `REPLACE(text, '-', '')`).

</div>

```sql
SELECT TeacherName, REPLACE(TeacherPhone, '-', '') AS Digits
FROM   Teachers
WHERE  TeacherPhone IS NOT NULL;
```

<div dir="rtl">

| TeacherName | Digits |
|---|---|
| סמיר חלבי | 0501234567 |
| רונית לוי | 0522345678 |
| דנה כהן | 0544567890 |
| יוסי פרץ | 0535678901 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 11. 🟢 הציגו לכל מורה את שמו ואת המחיר ל‑90 דקות (שעה וחצי), בשם `Lesson90`.

</div>

```sql
SELECT TeacherName, HourRate * 1.5 AS Lesson90
FROM   Teachers;
```

<div dir="rtl">

| TeacherName | Lesson90 |
|---|---|
| סמיר חלבי | 180.0 |
| רונית לוי | 225.0 |
| אמיר עזאם | 165.0 |
| דנה כהן | 210.0 |
| יוסי פרץ | 150.0 |
| נור מנסור | 195.0 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 12. 🟢 הציגו את שם הכלי ואת משפחתו בעמודה אחת, למשל `פסנתר (קלידים)`.

</div>

```sql
SELECT InstName || ' (' || InstFamily || ')' AS Instrument
FROM   Instruments;
```

<div dir="rtl">

| Instrument |
|---|
| פסנתר (קלידים) |
| גיטרה (מיתר) |
| כינור (מיתר) |
| תופים (הקשה) |
| חליל (נשיפה) |
| עוד (מיתר) |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 13. 🟡 הציגו את 3 הספרות האחרונות של הטלפון של כל מורה (רמז: `SUBSTR(TeacherPhone, -3)`).

</div>

```sql
SELECT TeacherName, SUBSTR(TeacherPhone, -3) AS Last3
FROM   Teachers
WHERE  TeacherPhone IS NOT NULL;
```

<div dir="rtl">

| TeacherName | Last3 |
|---|---|
| סמיר חלבי | 567 |
| רונית לוי | 678 |
| דנה כהן | 890 |
| יוסי פרץ | 901 |

**התוצאה: 4 שורות**

</div>

<div dir="rtl">

### 14. 🟡 הציגו לכל רישום את התשלום החודשי כולל מע"מ 18%, מעוגל לשקל, בשם `WithVat`.

</div>

```sql
SELECT RegPupil, ROUND(MonthlyFee * 1.18) AS WithVat
FROM   Registrations;
```

<div dir="rtl">

| RegPupil | WithVat |
|---|---|
| 201 | 378.0 |
| 201 | 330.0 |
| 202 | 472.0 |
| 203 | 354.0 |
| 204 | 425.0 |
| 204 | 448.0 |
| 205 | 401.0 |
| 206 | 330.0 |
| 207 | 413.0 |
| 207 | 378.0 |
| 208 | 354.0 |
| 209 | 448.0 |
| 210 | 354.0 |
| 210 | 378.0 |

**התוצאה: 14 שורות**

</div>

<div dir="rtl">

### 15. 🟡 הציגו לכל תלמיד את שמו ואת מספר האותיות בשם המלא (בלי רווח), בשם `Letters`.

</div>

```sql
SELECT FirstName, LastName, LENGTH(FirstName) + LENGTH(LastName) AS Letters
FROM   Pupils;
```

<div dir="rtl">

| FirstName | LastName | Letters |
|---|---|---|
| אדם | חלבי | 7 |
| מאיה | כהן | 7 |
| כרים | עזאם | 8 |
| שירה | לוי | 7 |
| רמי | חורי | 7 |
| תמר | אברהם | 8 |
| ליאן | קבלאן | 9 |
| עומר | ביטון | 9 |
| סאלי | חסון | 8 |
| יואב | שושן | 8 |

**התוצאה: 10 שורות**

</div>

<div dir="rtl">

### 16. 🔴 הציגו לכל לוקר: 'קרקע' לקומה 1, 'עליונה' לקומה 2.

</div>

```sql
SELECT LockerNum,
       CASE LockerFloor WHEN 1 THEN 'קרקע' ELSE 'עליונה' END AS FloorName
FROM   Lockers;
```

<div dir="rtl">

| LockerNum | FloorName |
|---|---|
| 1 | קרקע |
| 2 | קרקע |
| 3 | עליונה |
| 4 | עליונה |
| 5 | עליונה |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 17. 🔴 הציגו לכל רישום את קוד התלמיד ו'ותיק' אם נרשם לפני 2024, 'חדש' אם ב‑2024, ו'חדש מאוד' אם ב‑2025.

</div>

```sql
SELECT RegPupil, RegYear,
       CASE
         WHEN RegYear < 2024 THEN 'ותיק'
         WHEN RegYear = 2024 THEN 'חדש'
         ELSE 'חדש מאוד'
       END AS Seniority
FROM   Registrations;
```

<div dir="rtl">

| RegPupil | RegYear | Seniority |
|---|---|---|
| 201 | 2024 | חדש |
| 201 | 2025 | חדש מאוד |
| 202 | 2022 | ותיק |
| 203 | 2025 | חדש מאוד |
| 204 | 2023 | ותיק |
| 204 | 2025 | חדש מאוד |
| 205 | 2021 | ותיק |
| 206 | 2024 | חדש |
| 207 | 2025 | חדש מאוד |
| 207 | 2024 | חדש |
| 208 | 2023 | ותיק |
| 209 | 2025 | חדש מאוד |
| 210 | 2022 | ותיק |
| 210 | 2024 | חדש |

**התוצאה: 14 שורות**

</div>

<div dir="rtl">

---

## 🎓 בסגנון הבחינה — ☕ בית הקפה "אל‑בלד"

</div>

<div dir="rtl">

### 1. 🟢 הציגו לכל מנה את שמה ואת המחיר אחרי הנחה של 10%, בשם `Sale`.

</div>

```sql
SELECT DishName, DishPrice * 0.9 AS Sale
FROM   Dishes;
```

<div dir="rtl">

| DishName | Sale |
|---|---|
| חומוס | 25.2 |
| סלט ירקות | 28.8 |
| שניצל | 50.4 |
| פסטה | 43.2 |
| קנאפה | 27.0 |
| עוגת גבינה | 23.4 |
| לימונדה | 12.6 |
| קפה | 10.8 |

**התוצאה: 8 שורות**

</div>

<div dir="rtl">

### 2. 🟢 הציגו לכל הזמנה את שם הלקוח ואת אורך השם.

</div>

```sql
SELECT CustName, LENGTH(CustName) AS NameLen
FROM   Orders;
```

<div dir="rtl">

| CustName | NameLen |
|---|---|
| דנה לוי | 7 |
| עומר חורי | 9 |
| נועה כץ | 7 |
| סמיר דיב | 8 |
| ליאת בר | 7 |
| ראמי סעיד | 9 |
| יעל שגיא | 8 |
| חנאן זועבי | 10 |
| איתי פלד | 8 |
| מאיה לוי | 8 |
| ואיל נסאר | 9 |
| שני אדרי | 8 |

**התוצאה: 12 שורות**

</div>

<div dir="rtl">

### 3. 🟡 הציגו לכל עובד את שמו ואת הטלפון, ובמקום NULL — 'אין'.

</div>

```sql
SELECT WorkerName, IFNULL(WorkerPhone, 'אין') AS Phone
FROM   Workers;
```

<div dir="rtl">

| WorkerName | Phone |
|---|---|
| סאלי חדאד | 050-1111111 |
| יובל נחום | אין |
| אמיר טאהא | 054-3333333 |
| מיכל שרון | 052-4444444 |
| רים עבאס | אין |
| תום בראל | 053-6666666 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 4. 🟡 הציגו לכל עובד את שמו ואת שנת תחילת העבודה בלבד.

</div>

```sql
SELECT WorkerName, SUBSTR(StartDate, 1, 4) AS StartYear
FROM   Workers;
```

<div dir="rtl">

| WorkerName | StartYear |
|---|---|
| סאלי חדאד | 2022 |
| יובל נחום | 2023 |
| אמיר טאהא | 2021 |
| מיכל שרון | 2024 |
| רים עבאס | 2020 |
| תום בראל | 2023 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

### 5. 🟡 השלימו את הערכים בטבלה שתתקבל.

</div>

```sql
SELECT DishName,
       CASE WHEN DishPrice >= 30 THEN 'יקר' ELSE 'זול' END AS Level
FROM   Dishes
WHERE  DishKind = 'מנה ראשונה';
```

<div dir="rtl">

| DishName | Level |
|---|---|
| חומוס | זול |
| סלט ירקות | יקר |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 6. 🔴

</div>

```sql
SELECT DishName, DishPrice * 2 AS TwoDishes
FROM   Dishes
WHERE  DishKind = 'שתייה';
```

<div dir="rtl">

| DishName | TwoDishes |
|---|---|
| לימונדה | 28 |
| קפה | 24 |

**התוצאה: 2 שורות**

</div>

<div dir="rtl">

### 7. 🔴 השלימו כך שיוצג לכל עובד שכר יומי (8 שעות) מעוגל, בשם `DayPay`.

</div>

```sql
SELECT WorkerName, ROUND(HourPay * 8) AS DayPay
FROM   Workers;
```

<div dir="rtl">

| WorkerName | DayPay |
|---|---|
| סאלי חדאד | 336.0 |
| יובל נחום | 304.0 |
| אמיר טאהא | 400.0 |
| מיכל שרון | 288.0 |
| רים עבאס | 440.0 |
| תום בראל | 304.0 |

**התוצאה: 6 שורות**

</div>

<div dir="rtl">

---

## 🏠 תרגול נוסף — 🏫 בית הספר "עתיד"

</div>

<div dir="rtl">

### 1. 🟢 הציגו את השם המלא של כל מורה בעמודה אחת.

</div>

```sql
SELECT FirstName || ' ' || LastName AS FullName
FROM   Teachers;
```

<div dir="rtl">

| FullName |
|---|
| נביל סרחאן |
| רונית בר-לב |
| חוסאם זיאד |
| אורלי שמש |
| פאדי חדאד |
| גלית מזרחי |
| סמיר אבו-ראס |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 2. 🟡 הציגו את שנת הקליטה בלבד של כל מורה (4 התווים הראשונים של `HireDate`).

</div>

```sql
SELECT FirstName, SUBSTR(HireDate, 1, 4) AS HireYear
FROM   Teachers;
```

<div dir="rtl">

| FirstName | HireYear |
|---|---|
| נביל | 2012 |
| רונית | 2018 |
| חוסאם | 2021 |
| אורלי | 2009 |
| פאדי | 2023 |
| גלית | 2016 |
| סמיר | 2024 |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 3. 🟡 הציגו את הטלפון של התלמידים, ובמקום NULL — 'אין'.

</div>

```sql
SELECT FirstName, IFNULL(Phone, 'אין') AS Phone
FROM   Students;
```

<div dir="rtl">

| FirstName | Phone |
|---|---|
| אדם | 050-1000001 |
| נור | אין |
| יואב | 052-1000003 |
| מאיה | 054-1000004 |
| רוני | אין |
| סאלי | 050-1000006 |
| עומר | 053-1000007 |
| שירה | 050-1000008 |
| כרים | אין |
| תמר | 052-1000010 |
| ליאור | 050-1000011 |
| ג'וד | אין |
| דניאל | 054-1000013 |
| הדיל | 050-1000014 |
| איתי | אין |
| ראניה | 053-1000016 |
| נועם | 050-1000017 |
| לינא | אין |

**התוצאה: 18 שורות**

</div>

<div dir="rtl">

### 4. 🔴 הציגו כל ציון ולצידו 'עבר' (55 ומעלה), 'נכשל', או 'לא נבחן' (NULL).

</div>

```sql
SELECT StudentId, CourseCode, Grade,
       CASE
         WHEN Grade IS NULL THEN 'לא נבחן'
         WHEN Grade >= 55   THEN 'עבר'
         ELSE 'נכשל'
       END AS Status
FROM   Grades
WHERE  Term = 1;
```

<div dir="rtl">

| StudentId | CourseCode | Grade | Status |
|---|---|---|---|
| 1001 | 11 | 88 | עבר |
| 1001 | 12 | 74 | עבר |
| 1001 | 14 | 92 | עבר |
| 1002 | 11 | 95 | עבר |
| 1002 | 12 | 89 | עבר |
| 1002 | 15 | 100 | עבר |
| 1003 | 16 | 61 | עבר |
| 1003 | 12 | 55 | עבר |
| 1003 | 14 | 70 | עבר |
| 1004 | 16 | 48 | נכשל |
| 1004 | 12 | 62 | עבר |
| 1004 | 14 | *NULL* | לא נבחן |
| 1005 | 11 | 77 | עבר |
| 1005 | 12 | 81 | עבר |
| 1005 | 15 | 90 | עבר |
| 1006 | 16 | 66 | עבר |
| 1006 | 12 | 58 | עבר |
| 1007 | 11 | 93 | עבר |
| 1007 | 13 | 97 | עבר |
| 1007 | 12 | 85 | עבר |
| 1008 | 11 | 72 | עבר |
| 1008 | 13 | 79 | עבר |
| 1008 | 12 | 68 | עבר |
| 1009 | 16 | 54 | נכשל |
| 1009 | 13 | 63 | עבר |
| … | … | … | … |

**התוצאה: 52 שורות** — מוצגות 25 הראשונות

</div>

<div dir="rtl">

### 5. 🟢 הציגו לכל מורה את השכר אחרי העלאה של 3%, מעוגל לשקל.

</div>

```sql
SELECT FirstName, ROUND(Salary * 1.03) AS NewSalary
FROM   Teachers;
```

<div dir="rtl">

| FirstName | NewSalary |
|---|---|
| נביל | 14935.0 |
| רונית | 11536.0 |
| חוסאם | 13184.0 |
| אורלי | 15759.0 |
| פאדי | 10094.0 |
| גלית | 13493.0 |
| סמיר | 10712.0 |

**התוצאה: 7 שורות**

</div>

<div dir="rtl">

### 6. 🟡 הציגו לכל תלמיד את חודש הלידה בלבד (תווים 6–7 של `BirthDate`).

</div>

```sql
SELECT FirstName, SUBSTR(BirthDate, 6, 2) AS BirthMonth
FROM   Students
WHERE  BirthDate IS NOT NULL;
```

<div dir="rtl">

| FirstName | BirthMonth |
|---|---|
| אדם | 03 |
| נור | 07 |
| יואב | 01 |
| מאיה | 11 |
| רוני | 05 |
| עומר | 02 |
| שירה | 09 |
| כרים | 12 |
| תמר | 04 |
| ליאור | 06 |
| ג'וד | 08 |
| דניאל | 01 |
| הדיל | 10 |
| איתי | 03 |
| ראניה | 12 |
| נועם | 09 |
| לינא | 10 |

**התוצאה: 17 שורות**

</div>

<div dir="rtl">

### 7. 🟡 הציגו לכל כיתה את שמה ואת מספר החדר, ו'אין חדר' כשהוא חסר.

</div>

```sql
SELECT ClassName, IFNULL(RoomNumber, 'אין חדר') AS Room
FROM   Classes;
```

<div dir="rtl">

| ClassName | Room |
|---|---|
| י1 | 12 |
| י2 | 14 |
| יא1 | 21 |
| יא2 | אין חדר |
| יב1 | 31 |

**התוצאה: 5 שורות**

</div>

<div dir="rtl">

### 8. 🔴 הציגו לכל היעדרות 'מאושרת' או 'לא מאושרת' לפי `Excused`.

</div>

```sql
SELECT StudentId, AbsenceDate,
       CASE Excused WHEN 1 THEN 'מאושרת' ELSE 'לא מאושרת' END AS Status
FROM   Absences;
```

<div dir="rtl">

| StudentId | AbsenceDate | Status |
|---|---|---|
| 1003 | 2026-09-02 | מאושרת |
| 1003 | 2026-09-03 | מאושרת |
| 1004 | 2026-09-07 | לא מאושרת |
| 1009 | 2026-09-08 | לא מאושרת |
| 1009 | 2026-09-09 | לא מאושרת |
| 1009 | 2026-09-14 | מאושרת |
| 1012 | 2026-09-02 | לא מאושרת |
| 1012 | 2026-09-10 | לא מאושרת |
| 1012 | 2026-09-15 | לא מאושרת |
| 1012 | 2026-09-16 | לא מאושרת |
| 1006 | 2026-09-11 | מאושרת |
| 1015 | 2026-09-04 | מאושרת |
| 1015 | 2026-09-17 | לא מאושרת |
| 1001 | 2026-09-18 | מאושרת |
| 1010 | 2026-09-08 | מאושרת |
| 1018 | 2026-09-15 | לא מאושרת |

**התוצאה: 16 שורות**

</div>

<div dir="rtl">

---

[⬅️ חזרה לשיעור](README.md) · [➡️ השיעור הקודם](../04-order-by/solutions.md) · [🏠 כל השיעורים](../README.md) · [השיעור הבא ⬅️](../06-aggregates/solutions.md)

</div>
