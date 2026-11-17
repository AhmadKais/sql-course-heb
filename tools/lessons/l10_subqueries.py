from _h import E, P, X

LESSON = dict(
    slug="10-subqueries",
    title="שאילתות מקוננות (Subqueries)",
    goal="שאילתה בתוך שאילתה: השוואה לממוצע/מקסימום, `IN (SELECT ...)` ו‑`NOT IN (SELECT ...)`",
    tables=["Teachers", "Pupils", "Registrations", "Instruments", "Lockers"],
    syntax="""
-- compare to ONE calculated value
SELECT TeacherName, HourRate
FROM   Teachers
WHERE  HourRate > (SELECT AVG(HourRate) FROM Teachers);

-- IN: the value appears in the list that the inner query returns
SELECT FirstName
FROM   Pupils
WHERE  PupilId IN (SELECT RegPupil FROM Registrations WHERE RegYear = 2025);

-- NOT IN: "who has NO ..."
SELECT TeacherName
FROM   Teachers
WHERE  TeacherCode NOT IN (SELECT RegTeacher FROM Registrations);
""",
    tips=[
        "השאילתה הפנימית רצה **קודם**, והתוצאה שלה נכנסת לשאילתה החיצונית.",
        "עם `>`, `<`, `=` — השאילתה הפנימית חייבת להחזיר **ערך אחד**. עם `IN` — היא יכולה להחזיר **רשימה**.",
        "\"מי **לא** ...\" / \"מי **אין לו** ...\" ← כמעט תמיד `NOT IN (SELECT ...)`.",
        "זה הפתרון ל‑`WHERE HourRate > AVG(HourRate)` האסור משיעור 6.",
    ],
    examples=[
        E("מורים שהמחיר שלהם גבוה מהממוצע.",
          "SELECT TeacherName, HourRate\nFROM   Teachers\nWHERE  HourRate > (SELECT AVG(HourRate) FROM Teachers);"),
        E("המורה (או המורים) היקר ביותר.",
          "SELECT TeacherName, HourRate\nFROM   Teachers\nWHERE  HourRate = (SELECT MAX(HourRate) FROM Teachers);"),
        E("תלמידים שנרשמו בשנת 2025.",
          "SELECT FirstName, LastName\nFROM   Pupils\nWHERE  PupilId IN (SELECT RegPupil\n                   FROM   Registrations\n                   WHERE  RegYear = 2025);"),
        E("מורים שאין להם אף רישום.",
          "SELECT TeacherName\nFROM   Teachers\nWHERE  TeacherCode NOT IN (SELECT RegTeacher FROM Registrations);"),
    ],
    predict=[
        P("SELECT AVG(HourRate) FROM Teachers;", "מה הממוצע? (זו השאילתה הפנימית של דוגמה 1)"),
        P("SELECT FirstName\nFROM   Pupils\nWHERE  BirthYear = (SELECT MIN(BirthYear) FROM Pupils);", "אילו תלמידים יחזרו?"),
        P("SELECT COUNT(*)\nFROM   Pupils\nWHERE  PupilId NOT IN (SELECT LockerPupil FROM Lockers);", "מה המספר?"),
    ],
    exercises=[
        X(1, "התלמידים שנולדו אחרי שנת הלידה הממוצעת.",
          "SELECT FirstName, BirthYear\nFROM   Pupils\nWHERE  BirthYear > (SELECT AVG(BirthYear) FROM Pupils);"),
        X(1, "המורה הזול ביותר.",
          "SELECT TeacherName, HourRate\nFROM   Teachers\nWHERE  HourRate = (SELECT MIN(HourRate) FROM Teachers);"),
        X(1, "רישומים שהתשלום בהם נמוך מהתשלום הממוצע.",
          "SELECT RegPupil, RegTeacher, MonthlyFee\nFROM   Registrations\nWHERE  MonthlyFee < (SELECT AVG(MonthlyFee) FROM Registrations);"),
        X(2, "תלמידים שיש להם לוקר (עם `IN`, בלי JOIN).",
          "SELECT FirstName, LastName\nFROM   Pupils\nWHERE  PupilId IN (SELECT LockerPupil FROM Lockers);"),
        X(2, "תלמידים שאין להם לוקר.",
          "SELECT FirstName, LastName\nFROM   Pupils\nWHERE  PupilId NOT IN (SELECT LockerPupil FROM Lockers);"),
        X(2, "מורים שמלמדים לפחות תלמיד מתקדם אחד.",
          "SELECT TeacherName\nFROM   Teachers\nWHERE  TeacherCode IN (SELECT RegTeacher\n                       FROM   Registrations\n                       WHERE  PupilLevel = 'מתקדם');"),
        X(2, "תלמידים שגרים באותה עיר כמו 'מאיה'.",
          "SELECT FirstName, LastName\nFROM   Pupils\nWHERE  HomeTown = (SELECT HomeTown FROM Pupils WHERE FirstName = 'מאיה');"),
        X(3, "תלמידים שלומדים אצל מורה לפסנתר (3 רמות: תלמידים ← רישומים ← מורים ← כלים).",
          "SELECT FirstName, LastName\nFROM   Pupils\nWHERE  PupilId IN (\n         SELECT RegPupil FROM Registrations\n         WHERE  RegTeacher IN (\n                SELECT TeacherCode FROM Teachers\n                WHERE  TeachInst = (SELECT InstCode FROM Instruments\n                                    WHERE  InstName = 'פסנתר')));"),
        X(3, "כלים שאף מורה לא מלמד (עם `NOT IN`).",
          "SELECT InstName\nFROM   Instruments\nWHERE  InstCode NOT IN (SELECT TeachInst FROM Teachers);"),
        X(3, "תלמידים שמשלמים בסך הכול יותר מהתשלום של הרישום היקר ביותר של 2024.",
          "SELECT   RegPupil, SUM(MonthlyFee) AS Total\nFROM     Registrations\nGROUP BY RegPupil\nHAVING   SUM(MonthlyFee) > (SELECT MAX(MonthlyFee)\n                            FROM   Registrations\n                            WHERE  RegYear = 2024);"),
    ],
    extra=[
        X(1, "מורים שמשתכרים יותר מהשכר הממוצע.",
          "SELECT FirstName, LastName, Salary\nFROM   Teachers\nWHERE  Salary > (SELECT AVG(Salary) FROM Teachers);"),
        X(2, "תלמידים שלא נעדרו אף פעם (עם `NOT IN`).",
          "SELECT FirstName, LastName\nFROM   Students\nWHERE  StudentId NOT IN (SELECT StudentId FROM Absences);"),
        X(2, "תלמידים שקיבלו לפחות ציון אחד מתחת ל‑50.",
          "SELECT FirstName, LastName\nFROM   Students\nWHERE  StudentId IN (SELECT StudentId FROM Grades WHERE Grade < 50);"),
        X(3, "מורים שאינם מחנכים של אף כיתה.",
          "SELECT FirstName, LastName\nFROM   Teachers\nWHERE  TeacherCode NOT IN (SELECT TeacherCode FROM Classes);"),
        X(3, "התלמיד (או התלמידים) עם הציון הגבוה ביותר במקצוע 13.",
          "SELECT FirstName, LastName\nFROM   Students\nWHERE  StudentId IN (SELECT StudentId FROM Grades\n                     WHERE  CourseCode = 13\n                       AND  Grade = (SELECT MAX(Grade) FROM Grades\n                                     WHERE  CourseCode = 13));"),
    ],
)
