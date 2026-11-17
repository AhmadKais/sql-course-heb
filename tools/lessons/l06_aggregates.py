from _h import E, P, X

LESSON = dict(
    slug="06-aggregates",
    title="פונקציות מצרפיות — COUNT, SUM, AVG, MIN, MAX",
    goal="לסכם עמודה שלמה לערך אחד: ספירה, סכום, ממוצע, מינימום ומקסימום",
    tables=["Teachers", "Registrations"],
    syntax="""
SELECT COUNT(*)              FROM Teachers;   -- number of rows
SELECT COUNT(TeacherPhone)   FROM Teachers;   -- rows where the column is NOT NULL
SELECT COUNT(DISTINCT TeachInst) FROM Teachers; -- number of different values
SELECT SUM(MonthlyFee)       FROM Registrations;
SELECT AVG(HourRate)         FROM Teachers;
SELECT MIN(HourRate), MAX(HourRate) FROM Teachers;

-- with WHERE: first filter the rows, then summarize
SELECT COUNT(*) FROM Registrations WHERE RegYear = 2025;
""",
    tips=[
        "פונקציה מצרפית **מכווצת** הרבה שורות לשורה **אחת**.",
        "`COUNT(*)` סופר **הכול**. `COUNT(col)` **מדלג על NULL**.",
        "`SUM`, `AVG`, `MIN`, `MAX` — מתעלמים מ‑NULL.",
        "⚠️ **אסור** פונקציה מצרפית בתוך `WHERE`. `WHERE HourRate > AVG(HourRate)` — שגיאה! (הפתרון בשיעור 10).",
        "⚠️ אי אפשר לשים לצד פונקציה מצרפית עמודה רגילה (בלי `GROUP BY` — שיעור 7).",
    ],
    examples=[
        E("כמה מורים יש, וכמה מהם רשמו טלפון?",
          "SELECT COUNT(*)            AS AllTeachers,\n       COUNT(TeacherPhone) AS WithPhone\nFROM   Teachers;",
          note="ההפרש (2) = המורים שהטלפון שלהם NULL."),
        E("המחיר הממוצע, הנמוך והגבוה של שעת שיעור.",
          "SELECT AVG(HourRate) AS AvgRate,\n       MIN(HourRate) AS MinRate,\n       MAX(HourRate) AS MaxRate\nFROM   Teachers;"),
        E("סך התשלומים החודשיים של רישומי 2025.",
          "SELECT SUM(MonthlyFee) AS Total2025\nFROM   Registrations\nWHERE  RegYear = 2025;"),
        E("בכמה כלים שונים מלמדים המורים?",
          "SELECT COUNT(DISTINCT TeachInst) AS Instruments\nFROM   Teachers;"),
    ],
    predict=[
        P("SELECT COUNT(*), COUNT(TeacherPhone), COUNT(DISTINCT TeachInst)\nFROM   Teachers;", "מה שלושת המספרים?"),
        P("SELECT COUNT(*)\nFROM   Registrations\nWHERE  RegTeacher = 3;", "מה יחזור?"),
        P("SELECT MAX(BirthYear) - MIN(BirthYear) AS Diff\nFROM   Pupils;", "מה יחזור?"),
    ],
    exercises=[
        X(1, "כמה תלמידים יש בבית הספר?",
          "SELECT COUNT(*) AS Pupils\nFROM   Pupils;"),
        X(1, "מה התשלום החודשי הגבוה ביותר ברישומים?",
          "SELECT MAX(MonthlyFee) AS MaxFee\nFROM   Registrations;"),
        X(1, "מה שנת הלידה של התלמיד המבוגר ביותר?",
          "SELECT MIN(BirthYear) AS Oldest\nFROM   Pupils;"),
        X(1, "מה הסכום של כל התשלומים החודשיים?",
          "SELECT SUM(MonthlyFee) AS Total\nFROM   Registrations;"),
        X(2, "כמה מורים **אין** להם טלפון? (שתי דרכים: עם `WHERE ... IS NULL`, או `COUNT(*) - COUNT(TeacherPhone)`)",
          "SELECT COUNT(*) AS NoPhone\nFROM   Teachers\nWHERE  TeacherPhone IS NULL;"),
        X(2, "מה התשלום הממוצע של תלמידים מתחילים? עגלו ל‑2 ספרות.",
          "SELECT ROUND(AVG(MonthlyFee), 2) AS AvgBeginner\nFROM   Registrations\nWHERE  PupilLevel = 'מתחיל';"),
        X(2, "כמה תלמידים **שונים** רשומים לשיעורים? (תלמיד יכול להופיע פעמיים ברישומים)",
          "SELECT COUNT(DISTINCT RegPupil) AS RegisteredPupils\nFROM   Registrations;"),
        X(2, "כמה רישומים יש למורה 5, ומה סכום התשלומים שלהם?",
          "SELECT COUNT(*) AS Regs, SUM(MonthlyFee) AS Total\nFROM   Registrations\nWHERE  RegTeacher = 5;"),
        X(3, "מה ההפרש בין המחיר היקר ביותר לזול ביותר לשעה?",
          "SELECT MAX(HourRate) - MIN(HourRate) AS Gap\nFROM   Teachers;"),
        X(3, "כמה תלמידים נולדו בין 2010 ל‑2012, ומה שנת הלידה הממוצעת שלהם?",
          "SELECT COUNT(*) AS Pupils, AVG(BirthYear) AS AvgYear\nFROM   Pupils\nWHERE  BirthYear BETWEEN 2010 AND 2012;"),
        X(3, "מה ההכנסה השנתית הכוללת (12 חודשים) מכל הרישומים?",
          "SELECT SUM(MonthlyFee * 12) AS YearIncome\nFROM   Registrations;"),
    ],
    extra=[
        X(1, "כמה תלמידים יש, וכמה מהם רשמו טלפון?",
          "SELECT COUNT(*) AS AllStudents, COUNT(Phone) AS WithPhone\nFROM   Students;"),
        X(1, "מה השכר הממוצע של המורים?",
          "SELECT AVG(Salary) AS AvgSalary\nFROM   Teachers;"),
        X(2, "מה הציון הגבוה, הנמוך והממוצע (מעוגל) במקצוע 11, מחצית 1?",
          "SELECT MAX(Grade) AS Hi, MIN(Grade) AS Lo, ROUND(AVG(Grade), 1) AS Avg\nFROM   Grades\nWHERE  CourseCode = 11 AND Term = 1;"),
        X(2, "כמה היעדרויות לא מאושרות יש?",
          "SELECT COUNT(*) AS NotExcused\nFROM   Absences\nWHERE  Excused = 0;"),
        X(3, "בכמה מקצועות שונים יש ציונים בטבלת הציונים?",
          "SELECT COUNT(DISTINCT CourseCode) AS Courses\nFROM   Grades;"),
        X(3, "כמה ציונים חסרים (NULL) יש בטבלת הציונים? כתבו עם `COUNT(*) - COUNT(Grade)`.",
          "SELECT COUNT(*) - COUNT(Grade) AS Missing\nFROM   Grades;"),
    ],
)
