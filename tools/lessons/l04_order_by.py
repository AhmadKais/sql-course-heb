from _h import E, P, X

LESSON = dict(
    slug="04-order-by",
    title="ORDER BY ו‑LIMIT — מיון",
    goal="למיין עולה/יורד (`ASC`/`DESC`), לפי כמה עמודות, ולהציג רק את ה‑N הראשונים (`LIMIT`)",
    tables=["Teachers", "Pupils", "Registrations", "Instruments"],
    syntax="""
SELECT columns
FROM   table_name
WHERE  condition
ORDER BY col1 ASC, col2 DESC     -- ASC = small -> big (default)   DESC = big -> small
LIMIT  3;                        -- only the first 3 rows

-- the fixed order of a query:
-- SELECT -> FROM -> WHERE -> GROUP BY -> HAVING -> ORDER BY -> LIMIT
""",
    tips=[
        "בלי `ORDER BY` — הסדר **אינו מובטח**.",
        "מיון לפי שתי עמודות: קודם לפי הראשונה; רק כשיש **תיקו** — לפי השנייה.",
        "`ASC` הוא ברירת המחדל, אפשר לא לכתוב אותו.",
        "אפשר למיין לפי כינוי או לפי עמודה מחושבת.",
    ],
    examples=[
        E("המורים לפי המחיר, מהיקר לזול.",
          "SELECT TeacherName, HourRate\nFROM   Teachers\nORDER BY HourRate DESC;"),
        E("התלמידים לפי שם המשפחה (א–ת).",
          "SELECT LastName, FirstName\nFROM   Pupils\nORDER BY LastName;"),
        E("הרישומים לפי שנה (עולה), ובתוך כל שנה — לפי התשלום (יורד).",
          "SELECT RegYear, MonthlyFee, RegPupil\nFROM   Registrations\nORDER BY RegYear ASC, MonthlyFee DESC;"),
        E("3 הרישומים היקרים ביותר.",
          "SELECT RegPupil, MonthlyFee\nFROM   Registrations\nORDER BY MonthlyFee DESC\nLIMIT  3;"),
    ],
    predict=[
        P("SELECT TeacherName\nFROM   Teachers\nORDER BY HourRate\nLIMIT  1;", "מה השם שיחזור?"),
        P("SELECT FirstName, BirthYear\nFROM   Pupils\nWHERE  HomeTown = 2\nORDER BY BirthYear DESC;", "מי יהיה בשורה הראשונה?"),
    ],
    exercises=[
        X(1, "הציגו את התלמידים לפי שנת הלידה, מהמבוגר לצעיר.",
          "SELECT FirstName, BirthYear\nFROM   Pupils\nORDER BY BirthYear;"),
        X(1, "הציגו את הכלים לפי שם הכלי (א–ת).",
          "SELECT InstName\nFROM   Instruments\nORDER BY InstName;"),
        X(1, "הציגו את המורים לפי המחיר, מהזול ליקר.",
          "SELECT TeacherName, HourRate\nFROM   Teachers\nORDER BY HourRate ASC;"),
        X(2, "הציגו את הרישומים של שנת 2025, מהתשלום הגבוה לנמוך.",
          "SELECT RegPupil, MonthlyFee\nFROM   Registrations\nWHERE  RegYear = 2025\nORDER BY MonthlyFee DESC;"),
        X(2, "הציגו את התלמידים לפי עיר, ובתוך כל עיר — לפי שם פרטי.",
          "SELECT HomeTown, FirstName\nFROM   Pupils\nORDER BY HomeTown, FirstName;"),
        X(2, "הציגו את 2 המורים הזולים ביותר.",
          "SELECT TeacherName, HourRate\nFROM   Teachers\nORDER BY HourRate\nLIMIT  2;"),
        X(2, "הציגו את התלמיד הצעיר ביותר.",
          "SELECT FirstName, BirthYear\nFROM   Pupils\nORDER BY BirthYear DESC\nLIMIT  1;"),
        X(3, "הציגו את שם המורה ואת המחיר ל‑4 שעות (`FourHours`), ממוין לפי `FourHours` מהגבוה לנמוך.",
          "SELECT TeacherName, HourRate * 4 AS FourHours\nFROM   Teachers\nORDER BY FourHours DESC;"),
        X(3, "הציגו את הרישומים ברמת 'ממשיך' או 'מתקדם', ממוינים לפי רמה ואז לפי תשלום יורד.",
          "SELECT PupilLevel, MonthlyFee, RegPupil\nFROM   Registrations\nWHERE  PupilLevel IN ('ממשיך', 'מתקדם')\nORDER BY PupilLevel, MonthlyFee DESC;"),
        X(3, "הציגו את 3 הרישומים העדכניים ביותר (לפי שנה), ובתיקו — הזולים קודם.",
          "SELECT RegPupil, RegYear, MonthlyFee\nFROM   Registrations\nORDER BY RegYear DESC, MonthlyFee ASC\nLIMIT  3;"),
    ],
    extra=[
        X(1, "הציגו את המורים לפי השכר, מהגבוה לנמוך.",
          "SELECT FirstName, LastName, Salary\nFROM   Teachers\nORDER BY Salary DESC;"),
        X(2, "הציגו את 5 הציונים הגבוהים ביותר במחצית 1.",
          "SELECT StudentId, CourseCode, Grade\nFROM   Grades\nWHERE  Term = 1\nORDER BY Grade DESC\nLIMIT  5;"),
        X(2, "הציגו את התלמידים לפי כיתה, ובתוך כיתה לפי שם משפחה.",
          "SELECT ClassCode, LastName, FirstName\nFROM   Students\nORDER BY ClassCode, LastName;"),
        X(3, "הציגו את המורה הוותיק ביותר (תאריך קליטה מוקדם ביותר).",
          "SELECT FirstName, LastName, HireDate\nFROM   Teachers\nORDER BY HireDate\nLIMIT  1;"),
    ],
)
