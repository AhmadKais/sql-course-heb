from _h import E, P, X

LESSON = dict(
    slug="02-where",
    title="WHERE — סינון שורות",
    goal="לבחור אילו **שורות** חוזרות: `=`, `<>`, `>`, `<`, `>=`, `<=` ושילוב תנאים עם `AND`, `OR`, `NOT`",
    tables=["Teachers", "Pupils", "Registrations", "Instruments"],
    syntax="""
SELECT columns
FROM   table_name
WHERE  condition;                 -- only rows where the condition is TRUE

-- comparison:   =   <>   >   <   >=   <=
WHERE HourRate > 120
WHERE PupilLevel = 'מתחיל'        -- text goes inside quotes

-- combining conditions
WHERE cond1 AND cond2             -- both must be true
WHERE cond1 OR  cond2             -- at least one is true
WHERE NOT cond1                   -- the opposite
WHERE (cond1 OR cond2) AND cond3  -- brackets! AND is stronger than OR
""",
    tips=[
        "טקסט ותאריך — **בתוך גרשיים**: `'מתחיל'`. מספר — **בלי** גרשיים: `120`.",
        "בבחינה כותבים לפעמים מירכאות כפולות: `\"מתחיל\"`. ב‑OneCompiler שתי הצורות עובדות.",
        "⚠️ `AND` חזק יותר מ‑`OR`. כשמשלבים את שניהם — **תמיד סוגריים** סביב ה‑`OR`.",
        "`<>` פירושו **שונה מ‑** (אפשר גם `!=`).",
    ],
    examples=[
        E("מורים שהמחיר לשעה שלהם גבוה מ‑120.",
          "SELECT TeacherName, HourRate\nFROM   Teachers\nWHERE  HourRate > 120;"),
        E("רישומים של תלמידים מתחילים.",
          "SELECT RegPupil, RegTeacher, PupilLevel\nFROM   Registrations\nWHERE  PupilLevel = 'מתחיל';"),
        E("רישומים משנת 2025 שהתשלום החודשי בהם לפחות 350.",
          "SELECT RegPupil, RegYear, MonthlyFee\nFROM   Registrations\nWHERE  RegYear = 2025 AND MonthlyFee >= 350;"),
        E("רישומים של המורים 1 או 5, ברמת 'ממשיך'.",
          "SELECT RegPupil, RegTeacher, PupilLevel\nFROM   Registrations\nWHERE  (RegTeacher = 1 OR RegTeacher = 5)\n  AND  PupilLevel = 'ממשיך';",
          note="בלי הסוגריים התנאי היה: מורה 1 (בכל רמה) **או** (מורה 5 וגם ממשיך) — תוצאה אחרת!"),
    ],
    predict=[
        P("SELECT TeacherName\nFROM   Teachers\nWHERE  HourRate <> 150;", "כמה שורות יחזרו?"),
        P("SELECT RegPupil\nFROM   Registrations\nWHERE  RegTeacher = 1 OR RegTeacher = 5 AND PupilLevel = 'ממשיך';",
          "כמה שורות יחזרו? השוו לדוגמה 4.",
          note="`AND` מחושב קודם, ולכן נכנסים **כל** הרישומים של מורה 1."),
        P("SELECT FirstName\nFROM   Pupils\nWHERE  NOT HomeTown = 1;", "אילו תלמידים יחזרו?"),
    ],
    exercises=[
        X(1, "הציגו את שמות התלמידים שנולדו בשנת 2012.",
          "SELECT FirstName, LastName\nFROM   Pupils\nWHERE  BirthYear = 2012;"),
        X(1, "הציגו את שם המורה ואת המחיר של מורים שהמחיר שלהם קטן מ‑120.",
          "SELECT TeacherName, HourRate\nFROM   Teachers\nWHERE  HourRate < 120;"),
        X(1, "הציגו את כל הרישומים של המורה שהקוד שלו 2.",
          "SELECT *\nFROM   Registrations\nWHERE  RegTeacher = 2;"),
        X(1, "הציגו את התלמידים שגרים בעיר 3.",
          "SELECT FirstName, LastName\nFROM   Pupils\nWHERE  HomeTown = 3;"),
        X(1, "הציגו את הכלים ממשפחת 'מיתר'.",
          "SELECT InstName\nFROM   Instruments\nWHERE  InstFamily = 'מיתר';"),
        X(2, "הציגו רישומים שאינם ברמת 'מתחיל'.",
          "SELECT RegPupil, PupilLevel\nFROM   Registrations\nWHERE  PupilLevel <> 'מתחיל';"),
        X(2, "הציגו תלמידים שנולדו לפני 2011 וגרים בעיר 2.",
          "SELECT FirstName, BirthYear, HomeTown\nFROM   Pupils\nWHERE  BirthYear < 2011 AND HomeTown = 2;"),
        X(2, "הציגו רישומים מהשנים 2022 או 2023.",
          "SELECT RegPupil, RegYear\nFROM   Registrations\nWHERE  RegYear = 2022 OR RegYear = 2023;"),
        X(2, "הציגו מורים שמלמדים פסנתר (כלי 10) והמחיר שלהם מעל 140.",
          "SELECT TeacherName, HourRate\nFROM   Teachers\nWHERE  TeachInst = 10 AND HourRate > 140;"),
        X(3, "הציגו רישומים ברמת 'מתקדם' או 'ממשיך', שהתשלום בהם נמוך מ‑330.",
          "SELECT RegPupil, PupilLevel, MonthlyFee\nFROM   Registrations\nWHERE  (PupilLevel = 'מתקדם' OR PupilLevel = 'ממשיך')\n  AND  MonthlyFee < 330;"),
        X(3, "הציגו תלמידים שגרים בעיר 1 או בעיר 4, ונולדו בשנת 2012 ואילך.",
          "SELECT FirstName, BirthYear, HomeTown\nFROM   Pupils\nWHERE  (HomeTown = 1 OR HomeTown = 4)\n  AND  BirthYear >= 2012;"),
        X(3, "הציגו את שם המורה ואת המחיר ל‑3 שעות, רק למורים שהמחיר ל‑3 שעות גבוה מ‑400.",
          "SELECT TeacherName, HourRate * 3 AS ThreeHours\nFROM   Teachers\nWHERE  HourRate * 3 > 400;",
          note="ב‑`WHERE` חוזרים על החישוב — אי אפשר להשתמש שם בכינוי `ThreeHours`."),
    ],
    extra=[
        X(1, "הציגו מורים שמלמדים 'מתמטיקה'.",
          "SELECT FirstName, LastName\nFROM   Teachers\nWHERE  Subject = 'מתמטיקה';"),
        X(1, "הציגו את שם התלמיד ואת קוד העיר של תלמידות (`Gender = 'F'`).",
          "SELECT FirstName, CityCode\nFROM   Students\nWHERE  Gender = 'F';"),
        X(2, "הציגו ציונים מתחת ל‑60 במחצית 1.",
          "SELECT StudentId, CourseCode, Grade\nFROM   Grades\nWHERE  Grade < 60 AND Term = 1;"),
        X(2, "הציגו מורים שהתחילו לעבוד לפני 2015 (`HireDate < '2015-01-01'`).",
          "SELECT FirstName, HireDate\nFROM   Teachers\nWHERE  HireDate < '2015-01-01';"),
        X(3, "הציגו מורים למתמטיקה או לאנגלית שמשתכרים יותר מ‑12,000.",
          "SELECT FirstName, Subject, Salary\nFROM   Teachers\nWHERE  (Subject = 'מתמטיקה' OR Subject = 'אנגלית')\n  AND  Salary > 12000;"),
        X(3, "הציגו היעדרויות לא מאושרות (`Excused = 0`) מחודש ספטמבר אחרי ה‑10 בו.",
          "SELECT StudentId, AbsenceDate\nFROM   Absences\nWHERE  Excused = 0 AND AbsenceDate > '2026-09-10';"),
    ],
)
