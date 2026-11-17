from _h import E, P, X

LESSON = dict(
    slug="11-views",
    title="שאילתות שמורות (VIEW)",
    goal="לשמור שאילתה בשם (`CREATE VIEW`) ולהשתמש בה כמו בטבלה — כמו `Q1` בבחינה",
    tables=["Pupils", "Registrations", "Teachers", "Instruments", "Cities"],
    syntax="""
-- save a query under a name
CREATE VIEW Q1 AS
SELECT   RegPupil, COUNT(*) AS Lessons, SUM(MonthlyFee) AS Total
FROM     Registrations
GROUP BY RegPupil;

-- use it like a table
SELECT * FROM Q1 WHERE Total > 600;

-- join a view with a table
SELECT FirstName, Total
FROM   Q1, Pupils
WHERE  RegPupil = PupilId;

DROP VIEW Q1;        -- delete the saved query (the data stays!)
""",
    tips=[
        "VIEW לא שומר נתונים — הוא שומר **את השאילתה**. בכל שימוש היא רצה מחדש.",
        "בבחינה: \"נתונה השאילתה השמורה Q1...\" ← מתייחסים ל‑Q1 **כמו לטבלה רגילה**.",
        "שימושי במיוחד כדי לסנן **תוצאה של קיבוץ** או לחבר אותה לטבלה אחרת.",
        "בכל תרגיל כאן ה‑`CREATE VIEW` והשאילתה רצים יחד. ב‑OneCompiler אפשר ליצור כל VIEW פעם אחת בלבד (או `DROP VIEW` קודם).",
    ],
    examples=[
        E("צרו את Q1 (מספר שיעורים וסך תשלום לכל תלמיד), והציגו את כולה.",
          "CREATE VIEW Q1 AS\nSELECT   RegPupil, COUNT(*) AS Lessons, SUM(MonthlyFee) AS Total\nFROM     Registrations\nGROUP BY RegPupil;\n\nSELECT * FROM Q1;"),
        E("בעזרת Q1: שמות התלמידים וסך התשלום שלהם.",
          "CREATE VIEW Q1 AS\nSELECT   RegPupil, COUNT(*) AS Lessons, SUM(MonthlyFee) AS Total\nFROM     Registrations\nGROUP BY RegPupil;\n\nSELECT FirstName, LastName, Total\nFROM   Q1, Pupils\nWHERE  RegPupil = PupilId;"),
        E("בעזרת Q1: התלמידים שמשלמים יותר מממוצע התשלומים הכוללים.",
          "CREATE VIEW Q1 AS\nSELECT   RegPupil, COUNT(*) AS Lessons, SUM(MonthlyFee) AS Total\nFROM     Registrations\nGROUP BY RegPupil;\n\nSELECT RegPupil, Total\nFROM   Q1\nWHERE  Total > (SELECT AVG(Total) FROM Q1);",
          note="\"ממוצע של סכומים\" — בלי VIEW זה כמעט בלתי אפשרי בשאילתה אחת פשוטה."),
    ],
    predict=[
        P("CREATE VIEW Cheap AS\nSELECT TeacherName, HourRate FROM Teachers WHERE HourRate < 130;\n\nSELECT COUNT(*) FROM Cheap;", "מה המספר?"),
        P("CREATE VIEW Q1 AS\nSELECT   RegPupil, COUNT(*) AS Lessons\nFROM     Registrations\nGROUP BY RegPupil;\n\nSELECT Lessons, COUNT(*)\nFROM   Q1\nGROUP BY Lessons;", "מה יחזור?",
          note="קיבוץ על תוצאה של קיבוץ: כמה תלמידים לומדים שיעור אחד, וכמה — שניים."),
    ],
    exercises=[
        X(1, "צרו VIEW בשם `Beginners` עם כל הרישומים של 'מתחיל', והציגו אותו.",
          "CREATE VIEW Beginners AS\nSELECT * FROM Registrations WHERE PupilLevel = 'מתחיל';\n\nSELECT * FROM Beginners;"),
        X(1, "צרו VIEW בשם `TeacherRegs` — לכל מורה (`RegTeacher`) מספר הרישומים (`Regs`). הציגו רק מורים עם יותר מ‑2.",
          "CREATE VIEW TeacherRegs AS\nSELECT   RegTeacher, COUNT(*) AS Regs\nFROM     Registrations\nGROUP BY RegTeacher;\n\nSELECT * FROM TeacherRegs WHERE Regs > 2;"),
        X(2, "בעזרת `TeacherRegs` מהסעיף הקודם: שם המורה ומספר הרישומים שלו.",
          "CREATE VIEW TeacherRegs AS\nSELECT   RegTeacher, COUNT(*) AS Regs\nFROM     Registrations\nGROUP BY RegTeacher;\n\nSELECT TeacherName, Regs\nFROM   TeacherRegs, Teachers\nWHERE  RegTeacher = TeacherCode;"),
        X(2, "צרו VIEW בשם `PupilCity` — שם התלמיד ושם העיר. השתמשו בו כדי להציג רק תלמידים מירכא.",
          "CREATE VIEW PupilCity AS\nSELECT FirstName, LastName, CityName\nFROM   Pupils, Cities\nWHERE  HomeTown = CityCode;\n\nSELECT FirstName, LastName FROM PupilCity WHERE CityName = 'ירכא';"),
        X(2, "צרו VIEW בשם `Income` — לכל שנת רישום סך התשלומים (`Total`). הציגו את השנה עם ההכנסה הגבוהה ביותר.",
          "CREATE VIEW Income AS\nSELECT   RegYear, SUM(MonthlyFee) AS Total\nFROM     Registrations\nGROUP BY RegYear;\n\nSELECT RegYear, Total\nFROM   Income\nWHERE  Total = (SELECT MAX(Total) FROM Income);"),
        X(3, "צרו VIEW בשם `TeacherAvg` — לכל מורה התשלום הממוצע (`AvgFee`). הציגו את שמות המורים שהממוצע שלהם גבוה מ‑330, ממוינים מהגבוה.",
          "CREATE VIEW TeacherAvg AS\nSELECT   RegTeacher, AVG(MonthlyFee) AS AvgFee\nFROM     Registrations\nGROUP BY RegTeacher;\n\nSELECT TeacherName, AvgFee\nFROM   TeacherAvg, Teachers\nWHERE  RegTeacher = TeacherCode AND AvgFee > 330\nORDER BY AvgFee DESC;"),
        X(3, "בעזרת VIEW: כמה תלמידים לומדים בכל משפחת כלים? (VIEW שמחבר רישום למשפחת כלי, ועליו `GROUP BY`)",
          "CREATE VIEW RegFamily AS\nSELECT RegPupil, InstFamily\nFROM   Registrations, Teachers, Instruments\nWHERE  RegTeacher = TeacherCode AND TeachInst = InstCode;\n\nSELECT   InstFamily, COUNT(DISTINCT RegPupil) AS Pupils\nFROM     RegFamily\nGROUP BY InstFamily;"),
    ],
    extra=[
        X(2, "צרו VIEW בשם `StudentAvg` — לכל תלמיד הממוצע במחצית 1 (`AvgGrade`). הציגו תלמידים עם ממוצע 90 ומעלה.",
          "CREATE VIEW StudentAvg AS\nSELECT   StudentId, AVG(Grade) AS AvgGrade\nFROM     Grades\nWHERE    Term = 1\nGROUP BY StudentId;\n\nSELECT * FROM StudentAvg WHERE AvgGrade >= 90;"),
        X(3, "בעזרת `StudentAvg`: שמות התלמידים שהממוצע שלהם גבוה מממוצע הממוצעים.",
          "CREATE VIEW StudentAvg AS\nSELECT   StudentId, AVG(Grade) AS AvgGrade\nFROM     Grades\nWHERE    Term = 1\nGROUP BY StudentId;\n\nSELECT S.FirstName, S.LastName, ROUND(V.AvgGrade, 1) AS AvgGrade\nFROM   StudentAvg V, Students S\nWHERE  V.StudentId = S.StudentId\n  AND  V.AvgGrade > (SELECT AVG(AvgGrade) FROM StudentAvg);"),
        X(3, "צרו VIEW בשם `ClassSize` — לכל כיתה מספר התלמידים. הציגו את שם הכיתה הגדולה ביותר.",
          "CREATE VIEW ClassSize AS\nSELECT   ClassCode, COUNT(*) AS Students\nFROM     Students\nWHERE    ClassCode IS NOT NULL\nGROUP BY ClassCode;\n\nSELECT ClassName, Students\nFROM   ClassSize V, Classes C\nWHERE  V.ClassCode = C.ClassCode\n  AND  Students = (SELECT MAX(Students) FROM ClassSize);"),
    ],
)
