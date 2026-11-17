"""Lesson 9 — more practice + exam-style questions."""
from _h import P, Q, X


def extend(L):
    L["predict"] += [
        P("SELECT    CityName, PupilId\nFROM      Cities\nLEFT JOIN Pupils ON CityCode = HomeTown\nWHERE     PupilId IS NULL;", "איזו עיר תחזור?"),
        P("SELECT COUNT(*)\nFROM   Pupils, Registrations, Teachers\nWHERE  PupilId = RegPupil AND RegTeacher = TeacherCode\n  AND  HomeTown = 1;", "מה המספר?"),
    ]
    L["exercises"] += [
        X(1, "שמות התלמידים ושמות המורים — רק רישומים משנת 2024.",
          "SELECT FirstName, TeacherName\nFROM   Pupils, Registrations, Teachers\nWHERE  PupilId = RegPupil AND RegTeacher = TeacherCode\n  AND  RegYear = 2024;"),
        X(2, "אילו תלמידים (שמות) לומדים כלי ממשפחת 'מיתר'? כל תלמיד פעם אחת.",
          "SELECT DISTINCT FirstName, LastName\nFROM   Pupils, Registrations, Teachers, Instruments\nWHERE  PupilId = RegPupil AND RegTeacher = TeacherCode\n  AND  TeachInst = InstCode AND InstFamily = 'מיתר';"),
        X(2, "כל הכלים ושמות המורים שמלמדים אותם — כולל כלי בלי מורה.",
          "SELECT    InstName, TeacherName\nFROM      Instruments\nLEFT JOIN Teachers ON InstCode = TeachInst;"),
        X(2, "מורים שאין להם אף רישום (עם `LEFT JOIN`).",
          "SELECT    TeacherName\nFROM      Teachers\nLEFT JOIN Registrations ON TeacherCode = RegTeacher\nWHERE     RegPupil IS NULL;"),
        X(3, "לכל מורה (שם): כמה ערים שונות מגיעים ממנו התלמידים שלו?",
          "SELECT   TeacherName, COUNT(DISTINCT HomeTown) AS Cities\nFROM     Teachers, Registrations, Pupils\nWHERE    TeacherCode = RegTeacher AND RegPupil = PupilId\nGROUP BY TeacherCode, TeacherName;"),
        X(3, "כל התלמידים וסך התשלום החודשי שלהם — כולל תלמידים בלי רישום (`IFNULL` ל‑0).",
          "SELECT    FirstName, LastName, IFNULL(SUM(MonthlyFee), 0) AS Total\nFROM      Pupils\nLEFT JOIN Registrations ON PupilId = RegPupil\nGROUP BY  PupilId, FirstName, LastName;"),
        X(3, "שמות התלמידים שגרים בכרמיאל, שמות המורים שלהם ושמות הכלים (5 טבלאות).",
          "SELECT FirstName, TeacherName, InstName\nFROM   Cities, Pupils, Registrations, Teachers, Instruments\nWHERE  CityCode = HomeTown AND PupilId = RegPupil\n  AND  RegTeacher = TeacherCode AND TeachInst = InstCode\n  AND  CityName = 'כרמיאל';"),
    ]
    L["extra"] += [
        X(1, "לכל ציון של מחצית 2: שם התלמיד, שם המקצוע והציון.",
          "SELECT S.FirstName, C.CourseName, G.Grade\nFROM   Students S, Grades G, Courses C\nWHERE  S.StudentId = G.StudentId AND G.CourseCode = C.CourseCode\n  AND  G.Term = 2;"),
        X(2, "כל התלמידים ושם הכיתה — כולל תלמידה בלי כיתה.",
          "SELECT    S.FirstName, S.LastName, C.ClassName\nFROM      Students S\nLEFT JOIN Classes C ON S.ClassCode = C.ClassCode;"),
        X(2, "לכל מורה: שם המורה וכמה ציונים נתן (דרך המקצועות שלו).",
          "SELECT   T.FirstName, T.LastName, COUNT(G.Grade) AS Grades\nFROM     Teachers T, Courses C, Grades G\nWHERE    T.TeacherCode = C.TeacherCode AND C.CourseCode = G.CourseCode\nGROUP BY T.TeacherCode, T.FirstName, T.LastName;"),
        X(3, "כל הערים ומספר התלמידים בכל אחת — כולל ערים בלי תלמידים.",
          "SELECT    C.CityName, COUNT(S.StudentId) AS Students\nFROM      Cities C\nLEFT JOIN Students S ON C.CityCode = S.CityCode\nGROUP BY  C.CityName;"),
    ]
    L["exam_db"] = "games"
    L["exam"] = [
        Q(1, "לכל הזמנה: שם המשתמש, שם המשחק ומספר השעות.",
          "SELECT FirstName, LastName, GameName, Hours\nFROM   Users, Orders, Games\nWHERE  UserId = BuyerId AND GameNum = GameCode;"),
        Q(2, "אילו משחקים (שמות) הזמין 'רמי חלבי'? כל משחק פעם אחת.",
          "SELECT DISTINCT GameName\nFROM   Users, Orders, Games\nWHERE  UserId = BuyerId AND GameNum = GameCode\n  AND  FirstName = 'רמי' AND LastName = 'חלבי';"),
        Q(2, "לכל משחק: שם המשחק, שם הקטגוריה ושם החברה.",
          "SELECT GameName, CatName, CompName\nFROM   Games, Categories, Companies\nWHERE  TypeCode = CatCode AND MakerCode = CompCode;"),
        Q(2, "משתמשים שלא הזמינו אף משחק (עם `LEFT JOIN`).",
          "SELECT    FirstName, LastName\nFROM      Users\nLEFT JOIN Orders ON UserId = BuyerId\nWHERE     OrderId IS NULL;"),
        Q(3, "לכל משתמש (שם): כמה שילם בסך הכול (שעות × מחיר לשעה).",
          "SELECT   FirstName, LastName, SUM(Hours * PricePerHour) AS Paid\nFROM     Users, Orders, Games\nWHERE    UserId = BuyerId AND GameNum = GameCode\nGROUP BY UserId, FirstName, LastName;"),
        Q(3, "", "SELECT   CatName, COUNT(*) AS Orders\nFROM     Categories, Games, Orders\nWHERE    CatCode = TypeCode AND GameCode = GameNum\nGROUP BY CatName;", kind="output"),
        Q(3, "השלימו את הערכים.",
          "SELECT    CompName, COUNT(GameCode) AS Games\nFROM      Companies\nLEFT JOIN Games ON CompCode = MakerCode\nGROUP BY  CompName;", kind="value"),
    ]
