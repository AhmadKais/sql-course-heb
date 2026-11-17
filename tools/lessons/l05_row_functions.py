from _h import E, P, X

LESSON = dict(
    slug="05-row-functions",
    title="חישובים ופונקציות שורה",
    goal="חישובים, חיבור טקסט `||`, `LENGTH`, `SUBSTR`, `ROUND`, `CASE` ו‑`IFNULL`",
    tables=["Teachers", "Pupils", "Registrations"],
    syntax="""
SELECT HourRate * 1.17                    -- + - * /
SELECT FirstName || ' ' || LastName       -- join texts
SELECT LENGTH(FirstName)                  -- number of characters
SELECT SUBSTR(TeacherPhone, 1, 3)         -- part of a text: from char 1, 3 chars
SELECT ROUND(HourRate / 7.0, 1)           -- round to 1 digit after the point
SELECT IFNULL(TeacherPhone, 'אין')        -- replace NULL with a value

SELECT CASE
         WHEN HourRate >= 140 THEN 'יקר'
         WHEN HourRate >= 120 THEN 'בינוני'
         ELSE 'זול'
       END AS PriceGroup
FROM Teachers;
""",
    tips=[
        "פונקציית **שורה** מחושבת **לכל שורה בנפרד** — מספר השורות לא משתנה.",
        "⚠️ חילוק של שני מספרים שלמים ב‑SQLite הוא חילוק שלם: `7 / 2 = 3`. כדי לקבל `3.5` כותבים `7 / 2.0`.",
        "`CASE` נבדק מלמעלה למטה — ה‑`WHEN` הראשון שמתקיים מנצח.",
        "`COALESCE(a, b)` עושה בדיוק את מה ש‑`IFNULL(a, b)` עושה.",
    ],
    examples=[
        E("השם המלא של כל תלמיד ואורך השם הפרטי.",
          "SELECT FirstName || ' ' || LastName AS FullName,\n       LENGTH(FirstName) AS NameLen\nFROM   Pupils;"),
        E("קידומת הטלפון של כל מורה, ו'אין טלפון' אם חסר.",
          "SELECT TeacherName,\n       IFNULL(SUBSTR(TeacherPhone, 1, 3), 'אין טלפון') AS Prefix\nFROM   Teachers;"),
        E("המחיר לשעה כולל מע\"מ 18%, מעוגל לשקל.",
          "SELECT TeacherName, ROUND(HourRate * 1.18) AS WithVat\nFROM   Teachers;"),
        E("סיווג המורים: יקר (140+), בינוני (120–139), זול.",
          "SELECT TeacherName, HourRate,\n       CASE\n         WHEN HourRate >= 140 THEN 'יקר'\n         WHEN HourRate >= 120 THEN 'בינוני'\n         ELSE 'זול'\n       END AS PriceGroup\nFROM   Teachers;"),
    ],
    predict=[
        P("SELECT 7 / 2, 7 / 2.0, ROUND(7 / 3.0, 2);", "מה יהיו שלושת הערכים?"),
        P("SELECT SUBSTR('סמיר חלבי', 1, 4) AS Part;", "מה יחזור?"),
        P("SELECT TeacherName, LENGTH(TeacherName) AS L\nFROM   Teachers\nWHERE  LENGTH(TeacherName) = 9;", "אילו מורים יחזרו?",
          note="גם הרווח הוא תו."),
    ],
    exercises=[
        X(1, "הציגו לכל רישום את קוד התלמיד ואת התשלום לחצי שנה (6 חודשים), בשם `HalfYear`.",
          "SELECT RegPupil, MonthlyFee * 6 AS HalfYear\nFROM   Registrations;"),
        X(1, "הציגו את השם המלא של התלמידים בפורמט: שם משפחה, פסיק, שם פרטי (למשל `חלבי, אדם`).",
          "SELECT LastName || ', ' || FirstName AS FullName\nFROM   Pupils;"),
        X(1, "הציגו את שם המורה ואת אורך השם שלו.",
          "SELECT TeacherName, LENGTH(TeacherName) AS NameLen\nFROM   Teachers;"),
        X(2, "הציגו את האות הראשונה של השם הפרטי של כל תלמיד, בשם `Initial`.",
          "SELECT FirstName, SUBSTR(FirstName, 1, 1) AS Initial\nFROM   Pupils;"),
        X(2, "הציגו את המחיר לדקה של כל מורה (מחיר לשעה חלקי 60), מעוגל ל‑2 ספרות.",
          "SELECT TeacherName, ROUND(HourRate / 60.0, 2) AS PerMinute\nFROM   Teachers;"),
        X(2, "הציגו את שם המורה ואת הטלפון, ובמקום NULL את הטקסט 'לא ידוע'.",
          "SELECT TeacherName, IFNULL(TeacherPhone, 'לא ידוע') AS Phone\nFROM   Teachers;"),
        X(2, "הציגו תלמידים ששם המשפחה שלהם ארוך מ‑3 אותיות.",
          "SELECT FirstName, LastName\nFROM   Pupils\nWHERE  LENGTH(LastName) > 3;"),
        X(3, "הציגו לכל תלמיד את שמו ואת 'צעיר' אם נולד ב‑2012 ואילך, אחרת 'בוגר'. בשם `AgeGroup`.",
          "SELECT FirstName, BirthYear,\n       CASE WHEN BirthYear >= 2012 THEN 'צעיר' ELSE 'בוגר' END AS AgeGroup\nFROM   Pupils;"),
        X(3, "הציגו לכל רישום את התשלום ואת התשלום אחרי הנחה: 10% למתחילים, 5% לממשיכים, ובלי הנחה למתקדמים.",
          "SELECT RegPupil, PupilLevel, MonthlyFee,\n       CASE PupilLevel\n         WHEN 'מתחיל' THEN MonthlyFee * 0.9\n         WHEN 'ממשיך' THEN MonthlyFee * 0.95\n         ELSE MonthlyFee\n       END AS AfterDiscount\nFROM   Registrations;"),
        X(3, "הציגו את מספר הטלפון של המורים בלי המקף (רמז: `REPLACE(text, '-', '')`).",
          "SELECT TeacherName, REPLACE(TeacherPhone, '-', '') AS Digits\nFROM   Teachers\nWHERE  TeacherPhone IS NOT NULL;"),
    ],
    extra=[
        X(1, "הציגו את השם המלא של כל מורה בעמודה אחת.",
          "SELECT FirstName || ' ' || LastName AS FullName\nFROM   Teachers;"),
        X(2, "הציגו את שנת הקליטה בלבד של כל מורה (4 התווים הראשונים של `HireDate`).",
          "SELECT FirstName, SUBSTR(HireDate, 1, 4) AS HireYear\nFROM   Teachers;"),
        X(2, "הציגו את הטלפון של התלמידים, ובמקום NULL — 'אין'.",
          "SELECT FirstName, IFNULL(Phone, 'אין') AS Phone\nFROM   Students;"),
        X(3, "הציגו כל ציון ולצידו 'עבר' (55 ומעלה), 'נכשל', או 'לא נבחן' (NULL).",
          "SELECT StudentId, CourseCode, Grade,\n       CASE\n         WHEN Grade IS NULL THEN 'לא נבחן'\n         WHEN Grade >= 55   THEN 'עבר'\n         ELSE 'נכשל'\n       END AS Status\nFROM   Grades\nWHERE  Term = 1;"),
    ],
)
