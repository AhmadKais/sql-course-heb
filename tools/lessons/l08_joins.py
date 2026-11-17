from _h import E, P, X

LESSON = dict(
    slug="08-joins",
    title="צירוף שתי טבלאות (JOIN)",
    goal="לחבר שתי טבלאות לפי מפתח ראשי = מפתח זר — בתחביר הבחינה (פסיק + `WHERE`) ובתחביר `JOIN ... ON`",
    tables=["Pupils", "Cities", "Teachers", "Instruments", "Registrations", "Lockers"],
    syntax="""
-- exam style: comma + WHERE  (PK = FK)
SELECT FirstName, CityName
FROM   Pupils, Cities
WHERE  HomeTown = CityCode;          -- FK = PK

-- the same, with JOIN ... ON
SELECT FirstName, CityName
FROM   Pupils
JOIN   Cities ON HomeTown = CityCode;

-- join + more conditions
WHERE  HomeTown = CityCode AND BirthYear > 2011
""",
    tips=[
        "**הצעד הראשון בכל צירוף:** מוצאים את המפתח הזר 🔗 ואת המפתח הראשי 🔑 שהוא מצביע עליו.",
        "⚠️ שכחתם את תנאי החיבור? כל שורה תחובר לכל שורה (10 × 5 = 50 שורות!).",
        "במוזיקה לכל שדה יש שם ייחודי, אז אין צורך לכתוב שם טבלה לפניו. כשיש שני שדות באותו שם (כמו בבית הספר \"עתיד\") — כותבים `Students.CityCode = Cities.CityCode`.",
        "אפשר לתת לטבלה כינוי קצר: `FROM Students S, Cities C WHERE S.CityCode = C.CityCode`.",
    ],
    examples=[
        E("שם התלמיד ושם העיר שלו (תחביר הבחינה).",
          "SELECT FirstName, LastName, CityName\nFROM   Pupils, Cities\nWHERE  HomeTown = CityCode;"),
        E("שם המורה ושם הכלי שהוא מלמד (תחביר `JOIN`).",
          "SELECT TeacherName, InstName\nFROM   Teachers\nJOIN   Instruments ON TeachInst = InstCode;"),
        E("המורים שמלמדים כלי ממשפחת 'מיתר', עם המחיר.",
          "SELECT TeacherName, InstName, HourRate\nFROM   Teachers, Instruments\nWHERE  TeachInst = InstCode\n  AND  InstFamily = 'מיתר';"),
        E("כמה תלמידים יש בכל עיר — עם **שם** העיר.",
          "SELECT   CityName, COUNT(*) AS Pupils\nFROM     Pupils, Cities\nWHERE    HomeTown = CityCode\nGROUP BY CityName;",
          note="שימו לב: העיר מעלות לא מופיעה — אין בה תלמידים. כדי להציג גם אותה צריך `LEFT JOIN` (שיעור 9)."),
    ],
    predict=[
        P("SELECT FirstName, CityName\nFROM   Pupils, Cities;", "כמה שורות יחזרו? (אין תנאי חיבור!)",
          note="10 תלמידים × 5 ערים = 50. כל תלמיד \"גר\" בכל עיר — תוצאה שגויה."),
        P("SELECT CityName\nFROM   Pupils, Cities\nWHERE  HomeTown = CityCode AND FirstName = 'עומר';", "מה יחזור?"),
    ],
    exercises=[
        X(1, "הציגו את שם המורה ואת שם הכלי שלו (בתחביר פסיק + `WHERE`).",
          "SELECT TeacherName, InstName\nFROM   Teachers, Instruments\nWHERE  TeachInst = InstCode;"),
        X(1, "הציגו את מספר הלוקר, הקומה ושם התלמיד שמחזיק בו.",
          "SELECT LockerNum, LockerFloor, FirstName, LastName\nFROM   Lockers, Pupils\nWHERE  LockerPupil = PupilId;"),
        X(1, "הציגו את שם התלמיד ושם העיר — רק לתלמידים מעכו.",
          "SELECT FirstName, LastName\nFROM   Pupils, Cities\nWHERE  HomeTown = CityCode AND CityName = 'עכו';"),
        X(2, "הציגו לכל רישום: שם התלמיד, הרמה והתשלום.",
          "SELECT FirstName, LastName, PupilLevel, MonthlyFee\nFROM   Registrations, Pupils\nWHERE  RegPupil = PupilId;"),
        X(2, "הציגו לכל רישום: שם המורה, השנה והתשלום — רק רישומי 2025.",
          "SELECT TeacherName, RegYear, MonthlyFee\nFROM   Registrations, Teachers\nWHERE  RegTeacher = TeacherCode AND RegYear = 2025;"),
        X(2, "הציגו את המורים לפסנתר (לפי **שם** הכלי, לא לפי הקוד).",
          "SELECT TeacherName\nFROM   Teachers, Instruments\nWHERE  TeachInst = InstCode AND InstName = 'פסנתר';"),
        X(2, "הציגו את התלמידים שיש להם לוקר בקומה 2, ממוינים לפי שם.",
          "SELECT FirstName, LastName, LockerNum\nFROM   Pupils\nJOIN   Lockers ON LockerPupil = PupilId\nWHERE  LockerFloor = 2\nORDER BY FirstName;"),
        X(3, "לכל מורה (לפי **שם**): כמה רישומים יש לו?",
          "SELECT   TeacherName, COUNT(*) AS Regs\nFROM     Teachers, Registrations\nWHERE    TeacherCode = RegTeacher\nGROUP BY TeacherName;"),
        X(3, "לכל משפחת כלים: כמה מורים מלמדים בה, ומה המחיר הממוצע?",
          "SELECT   InstFamily, COUNT(*) AS Teachers, AVG(HourRate) AS AvgRate\nFROM     Teachers, Instruments\nWHERE    TeachInst = InstCode\nGROUP BY InstFamily;"),
        X(3, "שמות התלמידים שמשלמים בסך הכול יותר מ‑600 בחודש.",
          "SELECT   FirstName, LastName, SUM(MonthlyFee) AS Total\nFROM     Pupils, Registrations\nWHERE    PupilId = RegPupil\nGROUP BY PupilId, FirstName, LastName\nHAVING   SUM(MonthlyFee) > 600;"),
    ],
    extra=[
        X(1, "הציגו את שם התלמיד ואת שם הכיתה שלו.",
          "SELECT FirstName, LastName, ClassName\nFROM   Students, Classes\nWHERE  Students.ClassCode = Classes.ClassCode;"),
        X(1, "הציגו את שם המקצוע ושם המורה שמלמד אותו.",
          "SELECT CourseName, FirstName, LastName\nFROM   Courses, Teachers\nWHERE  Courses.TeacherCode = Teachers.TeacherCode;"),
        X(2, "הציגו את המורים שגרים בחיפה (לפי שם העיר).",
          "SELECT FirstName, LastName\nFROM   Teachers T, Cities C\nWHERE  T.CityCode = C.CityCode AND C.CityName = 'חיפה';"),
        X(2, "הציגו לכל כיתה את שמה ואת שם המחנך/ת.",
          "SELECT ClassName, FirstName, LastName\nFROM   Classes\nJOIN   Teachers ON Classes.TeacherCode = Teachers.TeacherCode;"),
        X(3, "כמה תלמידים יש בכל כיתה — לפי **שם** הכיתה, מהגדולה לקטנה.",
          "SELECT   ClassName, COUNT(*) AS Students\nFROM     Students S, Classes C\nWHERE    S.ClassCode = C.ClassCode\nGROUP BY ClassName\nORDER BY Students DESC;"),
        X(3, "שמות התלמידים שנעדרו לפחות פעמיים.",
          "SELECT   FirstName, LastName, COUNT(*) AS Absences\nFROM     Students S, Absences A\nWHERE    S.StudentId = A.StudentId\nGROUP BY S.StudentId, FirstName, LastName\nHAVING   COUNT(*) >= 2;"),
    ],
)
