from _h import E, P, X

LESSON = dict(
    slug="09-joins-3-tables-left-join",
    title="צירוף 3 טבלאות ו‑LEFT JOIN",
    goal="לחבר 3 טבלאות דרך טבלה מקשרת (M:N), ולהציג גם שורות **בלי התאמה** עם `LEFT JOIN`",
    tables=["Pupils", "Registrations", "Teachers", "Instruments", "Cities", "Lockers"],
    syntax="""
-- 3 tables: Pupils <- Registrations -> Teachers     (2 join conditions!)
SELECT FirstName, TeacherName
FROM   Pupils, Registrations, Teachers
WHERE  PupilId    = RegPupil
  AND  RegTeacher = TeacherCode;

-- LEFT JOIN: ALL rows of the left table, even without a match
SELECT CityName, FirstName
FROM   Cities
LEFT JOIN Pupils ON CityCode = HomeTown;    -- no pupil -> NULL

-- rows WITHOUT a match:
... LEFT JOIN ... WHERE right_table_key IS NULL
""",
    tips=[
        "N טבלאות ← צריך **N‑1** תנאי חיבור.",
        "טבלה מקשרת (כמו `Registrations`) מחזיקה **שני** מפתחות זרים — היא הגשר בין שתי הטבלאות.",
        "`JOIN` רגיל מציג רק שורות **שיש להן זוג**. `LEFT JOIN` מציג את **כל** השורות של הטבלה השמאלית.",
        "`COUNT(*)` אחרי `LEFT JOIN` סופר גם את שורת ה‑NULL (1). כדי לקבל 0 — `COUNT(עמודה מהטבלה הימנית)`.",
    ],
    examples=[
        E("לכל רישום: שם התלמיד ושם המורה.",
          "SELECT FirstName, LastName, TeacherName\nFROM   Pupils, Registrations, Teachers\nWHERE  PupilId = RegPupil\n  AND  RegTeacher = TeacherCode;"),
        E("איזה תלמיד לומד איזה כלי? (4 טבלאות — 3 תנאים)",
          "SELECT FirstName, InstName\nFROM   Pupils, Registrations, Teachers, Instruments\nWHERE  PupilId = RegPupil\n  AND  RegTeacher = TeacherCode\n  AND  TeachInst = InstCode\nORDER BY FirstName;"),
        E("כל הערים ומספר התלמידים בכל אחת — **כולל ערים בלי תלמידים**.",
          "SELECT    CityName, COUNT(PupilId) AS Pupils\nFROM      Cities\nLEFT JOIN Pupils ON CityCode = HomeTown\nGROUP BY  CityName;",
          note="מעלות מופיעה עם 0. עם `COUNT(*)` היה יוצא 1 — בגלל שורת ה‑NULL."),
        E("כלים שאף מורה לא מלמד.",
          "SELECT    InstName\nFROM      Instruments\nLEFT JOIN Teachers ON InstCode = TeachInst\nWHERE     TeacherCode IS NULL;"),
    ],
    predict=[
        P("SELECT    TeacherName, RegPupil\nFROM      Teachers\nLEFT JOIN Registrations ON TeacherCode = RegTeacher\nWHERE     RegPupil IS NULL;", "איזה מורה יחזור?"),
        P("SELECT COUNT(*)\nFROM   Pupils, Registrations, Teachers\nWHERE  PupilId = RegPupil AND RegTeacher = TeacherCode;", "מה המספר?",
          note="כמספר השורות בטבלה המקשרת — כל רישום הוא זוג אחד."),
    ],
    exercises=[
        X(1, "לכל רישום: שם התלמיד, שם המורה והתשלום.",
          "SELECT FirstName, TeacherName, MonthlyFee\nFROM   Pupils, Registrations, Teachers\nWHERE  PupilId = RegPupil AND RegTeacher = TeacherCode;"),
        X(1, "אילו תלמידים (שמות) לומדים אצל 'יוסי פרץ'?",
          "SELECT FirstName, LastName\nFROM   Pupils, Registrations, Teachers\nWHERE  PupilId = RegPupil AND RegTeacher = TeacherCode\n  AND  TeacherName = 'יוסי פרץ';"),
        X(2, "אצל אילו מורים (שמות) לומדת 'ליאן'?",
          "SELECT TeacherName\nFROM   Pupils, Registrations, Teachers\nWHERE  PupilId = RegPupil AND RegTeacher = TeacherCode\n  AND  FirstName = 'ליאן';"),
        X(2, "שם התלמיד, שם העיר שלו ושם המורה — רק רישומים ברמת 'מתחיל'.",
          "SELECT FirstName, CityName, TeacherName\nFROM   Pupils, Cities, Registrations, Teachers\nWHERE  HomeTown = CityCode\n  AND  PupilId = RegPupil\n  AND  RegTeacher = TeacherCode\n  AND  PupilLevel = 'מתחיל';"),
        X(2, "כל התלמידים ומספר הלוקר שלהם — גם תלמידים **בלי** לוקר.",
          "SELECT    FirstName, LastName, LockerNum\nFROM      Pupils\nLEFT JOIN Lockers ON PupilId = LockerPupil;"),
        X(2, "תלמידים שאין להם לוקר.",
          "SELECT    FirstName, LastName\nFROM      Pupils\nLEFT JOIN Lockers ON PupilId = LockerPupil\nWHERE     LockerNum IS NULL;"),
        X(3, "כל המורים ומספר הרישומים של כל אחד — כולל מורים עם 0 רישומים.",
          "SELECT    TeacherName, COUNT(RegPupil) AS Regs\nFROM      Teachers\nLEFT JOIN Registrations ON TeacherCode = RegTeacher\nGROUP BY  TeacherCode, TeacherName;"),
        X(3, "לכל כלי (שם): כמה תלמידים לומדים אותו?",
          "SELECT   InstName, COUNT(*) AS Pupils\nFROM     Instruments, Teachers, Registrations\nWHERE    InstCode = TeachInst AND TeacherCode = RegTeacher\nGROUP BY InstName;"),
        X(3, "לכל עיר (שם): סכום התשלומים החודשיים של התלמידים שגרים בה.",
          "SELECT   CityName, SUM(MonthlyFee) AS Total\nFROM     Cities, Pupils, Registrations\nWHERE    CityCode = HomeTown AND PupilId = RegPupil\nGROUP BY CityName;"),
        X(3, "תלמידים (שמות) שלומדים אצל **שני** מורים או יותר, (אין צורך בשמות המורים).",
          "SELECT   FirstName, LastName, COUNT(*) AS Teachers\nFROM     Pupils, Registrations\nWHERE    PupilId = RegPupil\nGROUP BY PupilId, FirstName, LastName\nHAVING   COUNT(*) >= 2;"),
    ],
    extra=[
        X(1, "לכל ציון: שם התלמיד, שם המקצוע והציון — במחצית 1.",
          "SELECT S.FirstName, S.LastName, C.CourseName, G.Grade\nFROM   Students S, Grades G, Courses C\nWHERE  S.StudentId = G.StudentId\n  AND  G.CourseCode = C.CourseCode\n  AND  G.Term = 1;"),
        X(2, "הציונים של 'אדם חלבי' בכל המקצועות (שם מקצוע + ציון + מחצית).",
          "SELECT C.CourseName, G.Term, G.Grade\nFROM   Students S, Grades G, Courses C\nWHERE  S.StudentId = G.StudentId AND G.CourseCode = C.CourseCode\n  AND  S.FirstName = 'אדם' AND S.LastName = 'חלבי';"),
        X(2, "כל המקצועות ושם המורה — כולל מקצוע שעדיין אין לו מורה.",
          "SELECT    C.CourseName, T.FirstName, T.LastName\nFROM      Courses C\nLEFT JOIN Teachers T ON C.TeacherCode = T.TeacherCode;"),
        X(3, "תלמידים שלא נעדרו אף פעם.",
          "SELECT    S.FirstName, S.LastName\nFROM      Students S\nLEFT JOIN Absences A ON S.StudentId = A.StudentId\nWHERE     A.AbsenceId IS NULL;"),
        X(3, "לכל מקצוע (שם): הממוצע במחצית 1, מעוגל, מהגבוה לנמוך.",
          "SELECT   C.CourseName, ROUND(AVG(G.Grade), 1) AS AvgGrade\nFROM     Courses C, Grades G\nWHERE    C.CourseCode = G.CourseCode AND G.Term = 1\nGROUP BY C.CourseName\nORDER BY AvgGrade DESC;"),
    ],
)
