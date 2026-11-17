from _h import E, P, X

LESSON = dict(
    slug="01-select",
    title="SELECT — שליפת עמודות",
    goal="לבחור עמודות, `*`, כינויים עם `AS`, עמודה מחושבת ו‑`DISTINCT`",
    tables=["Teachers", "Pupils", "Registrations", "Instruments", "Lockers"],
    syntax="""
SELECT column1, column2        -- which columns to show
FROM   table_name;             -- from which table

SELECT *          FROM table_name;            -- all the columns
SELECT col AS NewName FROM table_name;        -- alias = a new name for the column
SELECT col * 12   FROM table_name;            -- a calculated column
SELECT DISTINCT col FROM table_name;          -- each value only once
""",
    tips=[
        "סדר העמודות בתוצאה = הסדר שכתבתם אחרי `SELECT`.",
        "בין עמודות שמים **פסיק**, אבל **אין פסיק** לפני `FROM`.",
        "`DISTINCT` מסיר שורות כפולות — הוא חל על **כל** העמודות שאחריו יחד.",
        "כינוי (`AS`) משנה רק את שם העמודה בתוצאה, לא את הטבלה עצמה.",
    ],
    examples=[
        E("הציגו את שם המורה ואת המחיר לשעה של כל המורים.",
          "SELECT TeacherName, HourRate\nFROM   Teachers;"),
        E("הציגו את כל העמודות של טבלת התלמידים.",
          "SELECT *\nFROM   Pupils;"),
        E("הציגו את שם המורה ואת המחיר ל‑4 שעות, בשם `FourHours`.",
          "SELECT TeacherName, HourRate * 4 AS FourHours\nFROM   Teachers;",
          note="עמודה מחושבת לא נשמרת בטבלה — היא מחושבת מחדש בכל הרצה."),
        E("באילו ערים (קוד עיר) גרים התלמידים? כל עיר פעם אחת.",
          "SELECT DISTINCT HomeTown\nFROM   Pupils;",
          note="בלי `DISTINCT` היו חוזרות 10 שורות, אחת לכל תלמיד."),
    ],
    predict=[
        P("SELECT FirstName, BirthYear\nFROM   Pupils;", "כמה שורות וכמה עמודות יחזרו?"),
        P("SELECT DISTINCT TeachInst\nFROM   Teachers;", "כמה שורות יחזרו? (רמז: יש שני מורים לפסנתר)"),
        P("SELECT DISTINCT RegYear, PupilLevel\nFROM   Registrations;",
          "כמה שורות יחזרו?", note="`DISTINCT` בודק את **הצירוף** של שתי העמודות."),
    ],
    exercises=[
        X(1, "הציגו את השם הפרטי ושם המשפחה של כל התלמידים.",
          "SELECT FirstName, LastName\nFROM   Pupils;"),
        X(1, "הציגו את כל העמודות של טבלת הכלים (`Instruments`).",
          "SELECT *\nFROM   Instruments;"),
        X(1, "הציגו את שם המורה ואת הטלפון שלו.",
          "SELECT TeacherName, TeacherPhone\nFROM   Teachers;"),
        X(1, "הציגו את שם המשפחה ואחריו השם הפרטי (בסדר הזה) של התלמידים.",
          "SELECT LastName, FirstName\nFROM   Pupils;"),
        X(2, "הציגו את קוד התלמיד ואת שנת הלידה, בשמות `Code` ו‑`Born`.",
          "SELECT PupilId AS Code, BirthYear AS Born\nFROM   Pupils;"),
        X(2, "הציגו לכל רישום את קוד התלמיד ואת התשלום השנתי (12 חודשים) בשם `YearFee`.",
          "SELECT RegPupil, MonthlyFee * 12 AS YearFee\nFROM   Registrations;"),
        X(2, "הציגו לכל תלמיד את שמו הפרטי ואת גילו בשנת 2026, בשם `Age`.",
          "SELECT FirstName, 2026 - BirthYear AS Age\nFROM   Pupils;"),
        X(2, "אילו משפחות כלים (`InstFamily`) יש בבית הספר? כל משפחה פעם אחת.",
          "SELECT DISTINCT InstFamily\nFROM   Instruments;"),
        X(2, "אילו רמות (`PupilLevel`) קיימות ברישומים? כל רמה פעם אחת.",
          "SELECT DISTINCT PupilLevel\nFROM   Registrations;"),
        X(3, "הציגו את שם המורה ואת המחיר לשעה אחרי העלאה של 10%, בשם `NewRate`.",
          "SELECT TeacherName, ROUND(HourRate * 1.1, 2) AS NewRate\nFROM   Teachers;"),
        X(3, "הציגו את השם המלא של כל תלמיד בעמודה אחת בשם `FullName` (רמז: `||` מחבר טקסטים).",
          "SELECT FirstName || ' ' || LastName AS FullName\nFROM   Pupils;"),
        X(3, "באילו קומות יש לוקרים? כל קומה פעם אחת.",
          "SELECT DISTINCT LockerFloor\nFROM   Lockers;"),
    ],
    extra=[
        X(1, "הציגו את השם הפרטי, שם המשפחה והמקצוע של כל המורים.",
          "SELECT FirstName, LastName, Subject\nFROM   Teachers;"),
        X(1, "הציגו את כל העמודות של טבלת המקצועות (`Courses`).",
          "SELECT *\nFROM   Courses;"),
        X(2, "הציגו לכל מורה את שמו הפרטי ואת השכר השנתי (12 משכורות), בשם `YearSalary`.",
          "SELECT FirstName, Salary * 12 AS YearSalary\nFROM   Teachers;"),
        X(2, "אילו מקצועות מלמדים המורים? כל מקצוע פעם אחת.",
          "SELECT DISTINCT Subject\nFROM   Teachers;"),
        X(3, "הציגו לכל מקצוע את שמו ואת מספר השעות בשנה (40 שבועות), בשם `YearHours`.",
          "SELECT CourseName, WeeklyHours * 40 AS YearHours\nFROM   Courses;"),
    ],
)
