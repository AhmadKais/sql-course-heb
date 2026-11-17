from _h import E, P, X

LESSON = dict(
    slug="12-insert-update-delete",
    title="INSERT, UPDATE, DELETE — שינוי נתונים",
    goal="להוסיף שורות, לעדכן ערכים ולמחוק שורות — ולבדוק את התוצאה",
    tables=["Teachers", "Pupils", "Registrations", "Instruments", "Cities", "Lockers"],
    syntax="""
-- add a row (values in the order of the columns)
INSERT INTO Cities VALUES (6, 'צפת');
INSERT INTO Teachers (TeacherCode, TeacherName, TeachInst, HourRate)
VALUES (7, 'לינה חורי', 50, 125);            -- missing columns -> NULL

-- change values
UPDATE Teachers
SET    HourRate = HourRate + 10
WHERE  TeachInst = 10;

-- delete rows
DELETE FROM Registrations
WHERE  RegYear < 2023;
""",
    tips=[
        "⚠️ **`UPDATE` / `DELETE` בלי `WHERE` = כל השורות בטבלה!** תמיד כותבים קודם `SELECT` עם אותו `WHERE`, ובודקים.",
        "טקסט בגרשיים, מספר בלי. `NULL` — בלי גרשיים.",
        "אפשר לעדכן כמה עמודות יחד: `SET HourRate = 130, TeacherPhone = NULL`.",
        "אי אפשר למחוק שורה שמפתח זר מצביע עליה (כשהאילוצים פעילים), וגם אי אפשר להוסיף מפתח ראשי שכבר קיים.",
        "🔄 התבלגן לכם? הדביקו מחדש את קוד בסיס הנתונים — הכול חוזר למצב ההתחלתי.",
    ],
    examples=[
        E("הוסיפו את העיר 'צפת' בקוד 6.",
          "INSERT INTO Cities VALUES (6, 'צפת');",
          check="SELECT * FROM Cities;"),
        E("העלו ב‑10 את המחיר לשעה של מורי הפסנתר (כלי 10).",
          "UPDATE Teachers\nSET    HourRate = HourRate + 10\nWHERE  TeachInst = 10;",
          check="SELECT TeacherName, TeachInst, HourRate FROM Teachers;"),
        E("עדכנו את הטלפון של 'אמיר עזאם' ל‑'058-1112222'.",
          "UPDATE Teachers\nSET    TeacherPhone = '058-1112222'\nWHERE  TeacherName = 'אמיר עזאם';",
          check="SELECT TeacherName, TeacherPhone FROM Teachers;"),
        E("מחקו את כל הרישומים משנים לפני 2023.",
          "DELETE FROM Registrations\nWHERE  RegYear < 2023;",
          check="SELECT RegPupil, RegTeacher, RegYear FROM Registrations;"),
    ],
    predict=[
        P("UPDATE Registrations SET MonthlyFee = 0 WHERE RegYear = 2030;\nSELECT COUNT(*) FROM Registrations WHERE MonthlyFee = 0;", "כמה שורות עודכנו? מה יחזור?",
          note="אין רישומים מ‑2030 — הפקודה לא שינתה כלום, ואין שגיאה."),
        P("DELETE FROM Lockers WHERE LockerFloor = 1;\nSELECT COUNT(*) FROM Lockers;", "כמה לוקרים נשארו?"),
    ],
    exercises=[
        X(1, "הוסיפו את הכלי 'צ'לו' (קוד 70, משפחת 'מיתר').",
          "INSERT INTO Instruments VALUES (70, 'צ''לו', 'מיתר');",
          check="SELECT * FROM Instruments;",
          note="גרש בתוך טקסט כותבים פעמיים: `'צ''לו'`."),
        X(1, "הוסיפו תלמיד חדש: 211, 'נדים', 'סעב', 2013, עיר 5.",
          "INSERT INTO Pupils VALUES (211, 'נדים', 'סעב', 2013, 5);",
          check="SELECT * FROM Pupils WHERE PupilId = 211;"),
        X(1, "עדכנו את המחיר של המורה 5 ל‑105.",
          "UPDATE Teachers\nSET    HourRate = 105\nWHERE  TeacherCode = 5;",
          check="SELECT TeacherName, HourRate FROM Teachers WHERE TeacherCode = 5;"),
        X(1, "מחקו את הלוקר מספר 4.",
          "DELETE FROM Lockers\nWHERE  LockerNum = 4;",
          check="SELECT * FROM Lockers;"),
        X(2, "הוסיפו מורה חדשה: 7, 'לינה חורי', מלמדת חליל (50), 125 לשעה, **בלי טלפון**. (רשמו את שמות העמודות)",
          "INSERT INTO Teachers (TeacherCode, TeacherName, TeachInst, HourRate)\nVALUES (7, 'לינה חורי', 50, 125);",
          check="SELECT * FROM Teachers;"),
        X(2, "כל התלמידים המתחילים עוברים לרמת 'ממשיך'.",
          "UPDATE Registrations\nSET    PupilLevel = 'ממשיך'\nWHERE  PupilLevel = 'מתחיל';",
          check="SELECT PupilLevel, COUNT(*) AS Regs FROM Registrations GROUP BY PupilLevel;"),
        X(2, "הנחה של 5% על כל הרישומים של שנת 2025.",
          "UPDATE Registrations\nSET    MonthlyFee = MonthlyFee * 0.95\nWHERE  RegYear = 2025;",
          check="SELECT RegPupil, RegYear, MonthlyFee FROM Registrations WHERE RegYear = 2025;"),
        X(2, "למורים שאין להם טלפון — רשמו את הטלפון '000-0000000'.",
          "UPDATE Teachers\nSET    TeacherPhone = '000-0000000'\nWHERE  TeacherPhone IS NULL;",
          check="SELECT TeacherName, TeacherPhone FROM Teachers;"),
        X(3, "מחקו את כל הרישומים של המורה 'יוסי פרץ' (בלי לכתוב את הקוד שלו — עם תת‑שאילתה).",
          "DELETE FROM Registrations\nWHERE  RegTeacher = (SELECT TeacherCode FROM Teachers\n                     WHERE  TeacherName = 'יוסי פרץ');",
          check="SELECT COUNT(*) AS RegsLeft FROM Registrations;"),
        X(3, "העלו ב‑20 את התשלום של כל הרישומים של תלמידים שגרים בעכו.",
          "UPDATE Registrations\nSET    MonthlyFee = MonthlyFee + 20\nWHERE  RegPupil IN (SELECT PupilId FROM Pupils, Cities\n                    WHERE  HomeTown = CityCode AND CityName = 'עכו');",
          check="SELECT RegPupil, MonthlyFee FROM Registrations WHERE RegPupil IN (204, 205, 210);"),
    ],
    extra=[
        X(1, "הוסיפו את העיר 'טמרה' בקוד 7.",
          "INSERT INTO Cities VALUES (7, 'טמרה');",
          check="SELECT * FROM Cities;"),
        X(2, "שבצו את התלמידה 1018 (`לינא`) לכיתה 104.",
          "UPDATE Students\nSET    ClassCode = 104\nWHERE  StudentId = 1018;",
          check="SELECT FirstName, ClassCode FROM Students WHERE StudentId = 1018;"),
        X(2, "העלו ב‑5% את השכר של כל המורים למתמטיקה.",
          "UPDATE Teachers\nSET    Salary = Salary * 1.05\nWHERE  Subject = 'מתמטיקה';",
          check="SELECT FirstName, Subject, Salary FROM Teachers;"),
        X(2, "מחקו את כל ההיעדרויות המאושרות.",
          "DELETE FROM Absences\nWHERE  Excused = 1;",
          check="SELECT COUNT(*) AS Left FROM Absences;"),
        X(3, "פקטור: הוסיפו 5 נקודות לכל הציונים במקצוע 16, אבל לא מעבר ל‑100 (רמז: `MIN(Grade + 5, 100)`).",
          "UPDATE Grades\nSET    Grade = MIN(Grade + 5, 100)\nWHERE  CourseCode = 16 AND Grade IS NOT NULL;",
          check="SELECT StudentId, Term, Grade FROM Grades WHERE CourseCode = 16;"),
    ],
)
