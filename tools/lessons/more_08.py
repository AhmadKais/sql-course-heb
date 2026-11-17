"""Lesson 8 — more practice + exam-style questions."""
from _h import P, Q, X


def extend(L):
    L["predict"] += [
        P("SELECT InstName\nFROM   Teachers, Instruments\nWHERE  TeachInst = InstCode AND HourRate > 130;", "אילו כלים יחזרו?"),
        P("SELECT COUNT(*)\nFROM   Lockers, Pupils\nWHERE  LockerPupil = PupilId AND HomeTown = 2;", "מה המספר?"),
    ]
    L["exercises"] += [
        X(1, "הציגו את שם התלמיד ושם העיר — לתלמידים שנולדו ב‑2012.",
          "SELECT FirstName, CityName\nFROM   Pupils, Cities\nWHERE  HomeTown = CityCode AND BirthYear = 2012;"),
        X(1, "הציגו את שם המורה ואת משפחת הכלי שהוא מלמד.",
          "SELECT TeacherName, InstFamily\nFROM   Teachers, Instruments\nWHERE  TeachInst = InstCode;"),
        X(2, "הציגו את המורים שמלמדים כלי ממשפחת 'קלידים' או 'הקשה'.",
          "SELECT TeacherName, InstName\nFROM   Teachers, Instruments\nWHERE  TeachInst = InstCode AND InstFamily IN ('קלידים', 'הקשה');"),
        X(2, "הציגו לכל רישום ברמת 'מתקדם' את שם התלמיד והשנה, ממוין לפי שנה.",
          "SELECT FirstName, LastName, RegYear\nFROM   Pupils, Registrations\nWHERE  PupilId = RegPupil AND PupilLevel = 'מתקדם'\nORDER BY RegYear;"),
        X(2, "הציגו את שמות התלמידים שיש להם לוקר, ואת שם העיר שלהם (3 טבלאות).",
          "SELECT FirstName, CityName, LockerNum\nFROM   Pupils, Cities, Lockers\nWHERE  HomeTown = CityCode AND PupilId = LockerPupil;"),
        X(3, "לכל עיר (שם): שנת הלידה הממוצעת של התלמידים שגרים בה.",
          "SELECT   CityName, AVG(BirthYear) AS AvgYear\nFROM     Pupils, Cities\nWHERE    HomeTown = CityCode\nGROUP BY CityName;"),
        X(3, "מורים (שמות) שסכום התשלומים אצלם גבוה מ‑900.",
          "SELECT   TeacherName, SUM(MonthlyFee) AS Total\nFROM     Teachers, Registrations\nWHERE    TeacherCode = RegTeacher\nGROUP BY TeacherCode, TeacherName\nHAVING   SUM(MonthlyFee) > 900;"),
    ]
    L["extra"] += [
        X(1, "הציגו את שם התלמיד ושם העיר שלו.",
          "SELECT S.FirstName, S.LastName, C.CityName\nFROM   Students S, Cities C\nWHERE  S.CityCode = C.CityCode;"),
        X(2, "הציגו את המקצועות שמלמדים מורים למתמטיקה.",
          "SELECT C.CourseName, T.FirstName\nFROM   Courses C, Teachers T\nWHERE  C.TeacherCode = T.TeacherCode AND T.Subject = 'מתמטיקה';"),
        X(2, "הציגו את ההיעדרויות של תלמידי הכיתה 104 (שם תלמיד + תאריך).",
          "SELECT S.FirstName, A.AbsenceDate\nFROM   Students S, Absences A\nWHERE  S.StudentId = A.StudentId AND S.ClassCode = 104;"),
        X(3, "לכל עיר (שם): כמה מורים גרים בה.",
          "SELECT   C.CityName, COUNT(*) AS Teachers\nFROM     Teachers T, Cities C\nWHERE    T.CityCode = C.CityCode\nGROUP BY C.CityName;"),
    ]
    L["exam_db"] = "library"
    L["exam"] = [
        Q(1, "הציגו את שם הספר ואת שם המשפחה של הסופר.",
          "SELECT Title, AuthorLastName\nFROM   Books, Authors\nWHERE  WriterCode = AuthorCode;"),
        Q(1, "הציגו את שם הקורא ואת שם העיר שלו.",
          "SELECT FirstName, LastName, CityName\nFROM   Members, Cities\nWHERE  TownCode = CityCode;"),
        Q(2, "הציגו את הספרים שכתבו סופרים מבריטניה.",
          "SELECT Title\nFROM   Books, Authors\nWHERE  WriterCode = AuthorCode AND Country = 'בריטניה';"),
        Q(2, "הציגו לכל השאלה את מספר ההשאלה ואת שם הקורא — רק השאלות שלא הוחזרו.",
          "SELECT LoanId, FirstName, LastName\nFROM   Loans, Members\nWHERE  ReaderId = MemberId AND ReturnDate IS NULL;"),
        Q(2, "השלימו את הערכים בטבלה שתתקבל.",
          "SELECT Title, PubYear\nFROM   Books, Authors\nWHERE  WriterCode = AuthorCode AND AuthorLastName = 'עוז';", kind="value"),
        Q(3, "", "SELECT   Country, COUNT(*) AS Books\nFROM     Books, Authors\nWHERE    WriterCode = AuthorCode\nGROUP BY Country;", kind="output"),
        Q(3, "השלימו כך שיוצגו שמות הקוראים מירכא.",
          "SELECT FirstName, LastName\nFROM   Members, Cities\nWHERE  TownCode = CityCode AND CityName = 'ירכא';", kind="complete",
          given="SELECT FirstName, LastName\nFROM   _______, ______\nWHERE  ________ = ________ AND ________ = '____';"),
    ]
