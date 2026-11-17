from _h import E, P, X

LESSON = dict(
    slug="07-group-by-having",
    title="GROUP BY ו‑HAVING — קיבוץ",
    goal="לחשב ספירה/סכום/ממוצע **לכל קבוצה**, ולסנן קבוצות עם `HAVING`",
    tables=["Teachers", "Pupils", "Registrations"],
    syntax="""
SELECT   group_col, COUNT(*), AVG(num_col)
FROM     table_name
WHERE    row_condition          -- 1. filter ROWS   (before grouping)
GROUP BY group_col              -- 2. make groups
HAVING   COUNT(*) >= 2          -- 3. filter GROUPS (after grouping)
ORDER BY COUNT(*) DESC;         -- 4. sort
""",
    tips=[
        "כל עמודה ב‑`SELECT` שאינה בתוך פונקציה מצרפית — **חייבת** להופיע ב‑`GROUP BY`.",
        "`WHERE` מסנן **שורות** (לפני הקיבוץ). `HAVING` מסנן **קבוצות** (אחרי הקיבוץ).",
        "פונקציה מצרפית בתנאי? ← `HAVING`, לא `WHERE`.",
        "מספר השורות בתוצאה = מספר הקבוצות.",
    ],
    examples=[
        E("כמה תלמידים גרים בכל עיר?",
          "SELECT   HomeTown, COUNT(*) AS Pupils\nFROM     Pupils\nGROUP BY HomeTown;"),
        E("לכל מורה: מספר הרישומים והתשלום הממוצע.",
          "SELECT   RegTeacher, COUNT(*) AS Regs, AVG(MonthlyFee) AS AvgFee\nFROM     Registrations\nGROUP BY RegTeacher;"),
        E("מורים שיש להם **לפחות 3** רישומים.",
          "SELECT   RegTeacher, COUNT(*) AS Regs\nFROM     Registrations\nGROUP BY RegTeacher\nHAVING   COUNT(*) >= 3;"),
        E("לכל רמה — כמה רישומים מ‑2024 ואילך, רק רמות עם יותר מרישום אחד, מהגדולה לקטנה.",
          "SELECT   PupilLevel, COUNT(*) AS Regs\nFROM     Registrations\nWHERE    RegYear >= 2024\nGROUP BY PupilLevel\nHAVING   COUNT(*) > 1\nORDER BY Regs DESC;",
          note="שימו לב לסדר: `WHERE` → `GROUP BY` → `HAVING` → `ORDER BY`."),
    ],
    predict=[
        P("SELECT   PupilLevel, COUNT(*)\nFROM     Registrations\nGROUP BY PupilLevel;", "כמה שורות יחזרו, ומה המספרים?"),
        P("SELECT   RegPupil, COUNT(*)\nFROM     Registrations\nGROUP BY RegPupil\nHAVING   COUNT(*) = 2;", "אילו תלמידים יחזרו?"),
        P("SELECT   TeachInst, MAX(HourRate)\nFROM     Teachers\nGROUP BY TeachInst;", "כמה שורות יחזרו?"),
    ],
    exercises=[
        X(1, "כמה מורים מלמדים כל כלי (`TeachInst`)?",
          "SELECT   TeachInst, COUNT(*) AS Teachers\nFROM     Teachers\nGROUP BY TeachInst;"),
        X(1, "כמה תלמידים נולדו בכל שנה?",
          "SELECT   BirthYear, COUNT(*) AS Pupils\nFROM     Pupils\nGROUP BY BirthYear;"),
        X(1, "מה סכום התשלומים החודשיים בכל שנת רישום?",
          "SELECT   RegYear, SUM(MonthlyFee) AS Total\nFROM     Registrations\nGROUP BY RegYear;"),
        X(2, "לכל תלמיד (`RegPupil`): בכמה שיעורים הוא רשום וכמה הוא משלם בסך הכול בחודש?",
          "SELECT   RegPupil, COUNT(*) AS Lessons, SUM(MonthlyFee) AS Total\nFROM     Registrations\nGROUP BY RegPupil;"),
        X(2, "לכל רמה: התשלום הנמוך והגבוה ביותר.",
          "SELECT   PupilLevel, MIN(MonthlyFee) AS MinFee, MAX(MonthlyFee) AS MaxFee\nFROM     Registrations\nGROUP BY PupilLevel;"),
        X(2, "ערים (`HomeTown`) שגרים בהן **יותר מ‑2** תלמידים.",
          "SELECT   HomeTown, COUNT(*) AS Pupils\nFROM     Pupils\nGROUP BY HomeTown\nHAVING   COUNT(*) > 2;"),
        X(2, "תלמידים שמשלמים בסך הכול **יותר מ‑600** בחודש.",
          "SELECT   RegPupil, SUM(MonthlyFee) AS Total\nFROM     Registrations\nGROUP BY RegPupil\nHAVING   SUM(MonthlyFee) > 600;"),
        X(3, "מורים שהתשלום הממוצע אצלם **מעל 330**, ממוינים מהממוצע הגבוה לנמוך.",
          "SELECT   RegTeacher, AVG(MonthlyFee) AS AvgFee\nFROM     Registrations\nGROUP BY RegTeacher\nHAVING   AVG(MonthlyFee) > 330\nORDER BY AvgFee DESC;"),
        X(3, "רק ברישומים שאינם 'מתחיל': כמה רישומים יש לכל מורה? הציגו רק מורים עם 2 רישומים כאלה לפחות.",
          "SELECT   RegTeacher, COUNT(*) AS Regs\nFROM     Registrations\nWHERE    PupilLevel <> 'מתחיל'\nGROUP BY RegTeacher\nHAVING   COUNT(*) >= 2;"),
        X(3, "לכל שנה ולכל רמה (קיבוץ לפי שתי עמודות): כמה רישומים? ממוין לפי שנה.",
          "SELECT   RegYear, PupilLevel, COUNT(*) AS Regs\nFROM     Registrations\nGROUP BY RegYear, PupilLevel\nORDER BY RegYear;"),
    ],
    extra=[
        X(1, "כמה תלמידים יש בכל כיתה (`ClassCode`)?",
          "SELECT   ClassCode, COUNT(*) AS Students\nFROM     Students\nGROUP BY ClassCode;"),
        X(1, "כמה מורים מלמדים כל מקצוע (`Subject`)?",
          "SELECT   Subject, COUNT(*) AS Teachers\nFROM     Teachers\nGROUP BY Subject;"),
        X(2, "הציון הממוצע (מעוגל לספרה אחת) של כל תלמיד במחצית 1.",
          "SELECT   StudentId, ROUND(AVG(Grade), 1) AS AvgGrade\nFROM     Grades\nWHERE    Term = 1\nGROUP BY StudentId;"),
        X(2, "תלמידים עם **3 היעדרויות או יותר**.",
          "SELECT   StudentId, COUNT(*) AS Absences\nFROM     Absences\nGROUP BY StudentId\nHAVING   COUNT(*) >= 3;"),
        X(3, "מקצועות (`CourseCode`) שהממוצע בהם במחצית 1 **מתחת ל‑75**.",
          "SELECT   CourseCode, ROUND(AVG(Grade), 1) AS AvgGrade\nFROM     Grades\nWHERE    Term = 1\nGROUP BY CourseCode\nHAVING   AVG(Grade) < 75;"),
        X(3, "כמה בנים וכמה בנות יש בכל כיתה?",
          "SELECT   ClassCode, Gender, COUNT(*) AS Students\nFROM     Students\nGROUP BY ClassCode, Gender\nORDER BY ClassCode;"),
    ],
)
