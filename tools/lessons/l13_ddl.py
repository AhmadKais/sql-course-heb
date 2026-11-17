from _h import E, P, X

LESSON = dict(
    slug="13-create-alter-drop",
    title="CREATE, ALTER, DROP — בניית טבלאות ואילוצים",
    goal="ליצור טבלה עם מפתחות ואילוצים, להוסיף/למחוק/לשנות שם עמודה, ולמחוק טבלה",
    tables=["Teachers", "Pupils", "Lockers"],
    syntax="""
CREATE TABLE Concerts (
  ConcertId    INTEGER PRIMARY KEY,                     -- PK
  ConcertName  TEXT    NOT NULL,                        -- must have a value
  ConcertDate  TEXT,
  Seats        INTEGER CHECK (Seats > 0),               -- allowed values only
  HostTeacher  INTEGER REFERENCES Teachers(TeacherCode) -- FK
);

ALTER TABLE Pupils ADD COLUMN Email TEXT;               -- add a column
ALTER TABLE Pupils DROP COLUMN Email;                   -- delete a column
ALTER TABLE Pupils RENAME COLUMN BirthYear TO BornYear; -- rename a column
DROP TABLE Concerts;                                    -- delete the table + all its data

-- composite PK (linking table):
PRIMARY KEY (RegPupil, RegTeacher)
""",
    tips=[
        "**אילוצים:** `PRIMARY KEY` (ייחודי ולא ריק) · `NOT NULL` · `UNIQUE` · `CHECK (...)` · `REFERENCES` (מפתח זר) · `DEFAULT ערך`.",
        "עמודה חדשה (`ADD COLUMN`) מתמלאת ב‑NULL בכל השורות הקיימות.",
        "בבחינה מופיעה גם `ALTER TABLE ... MODIFY COLUMN` (שינוי טיפוס). **SQLite לא תומך בה** — כותבים אותה על הדף, אבל לא מריצים ב‑OneCompiler.",
        "`DROP TABLE` מוחק את **הטבלה עצמה**. `DELETE FROM` מוחק רק **שורות** — הטבלה נשארת, ריקה.",
    ],
    examples=[
        E("צרו טבלת קונצרטים (Concerts) עם מפתח ראשי, שם חובה ומורה מארח (מפתח זר). הוסיפו קונצרט אחד.",
          "CREATE TABLE Concerts (\n  ConcertId    INTEGER PRIMARY KEY,\n  ConcertName  TEXT    NOT NULL,\n  ConcertDate  TEXT,\n  Seats        INTEGER CHECK (Seats > 0),\n  HostTeacher  INTEGER REFERENCES Teachers(TeacherCode)\n);\nINSERT INTO Concerts VALUES (1, 'קונצרט חנוכה', '2026-12-20', 120, 2);",
          check="SELECT * FROM Concerts;"),
        E("הוסיפו לטבלת התלמידים עמודת אימייל.",
          "ALTER TABLE Pupils ADD COLUMN Email TEXT;",
          check="SELECT PupilId, FirstName, Email FROM Pupils;"),
        E("שנו את השם של העמודה `LockerFloor` ל‑`Floor`.",
          "ALTER TABLE Lockers RENAME COLUMN LockerFloor TO Floor;",
          check="SELECT * FROM Lockers;"),
        E("אילוץ `CHECK` בפעולה: נסו להוסיף קונצרט עם 0 מקומות — ותראו שגיאה.",
          "CREATE TABLE Concerts (\n  ConcertId INTEGER PRIMARY KEY,\n  Seats     INTEGER CHECK (Seats > 0)\n);\nINSERT INTO Concerts VALUES (1, 50);\n-- INSERT INTO Concerts VALUES (2, 0);   -- error: CHECK constraint failed",
          check="SELECT * FROM Concerts;",
          note="הסירו את ה‑`--` מהשורה האחרונה והריצו ב‑OneCompiler כדי לראות את השגיאה."),
    ],
    exercises=[
        X(1, "צרו טבלה `Rooms` עם: מספר חדר (מפתח ראשי), קומה (מספר, חובה) ושם החדר (טקסט). הוסיפו 2 חדרים.",
          "CREATE TABLE Rooms (\n  RoomNum    INTEGER PRIMARY KEY,\n  RoomFloor  INTEGER NOT NULL,\n  RoomName   TEXT\n);\nINSERT INTO Rooms VALUES (1, 1, 'אולם פסנתרים');\nINSERT INTO Rooms VALUES (2, 2, 'חדר תופים');",
          check="SELECT * FROM Rooms;"),
        X(1, "הוסיפו לטבלת המורים עמודה `Email` מסוג טקסט.",
          "ALTER TABLE Teachers ADD COLUMN Email TEXT;",
          check="SELECT TeacherName, Email FROM Teachers;"),
        X(1, "מחקו מטבלת הלוקרים את העמודה `LockerFloor`.",
          "ALTER TABLE Lockers DROP COLUMN LockerFloor;",
          check="SELECT * FROM Lockers;"),
        X(2, "הוסיפו לטבלת התלמידים עמודה `Active` עם ערך ברירת מחדל 1. (רמז: `DEFAULT 1`)",
          "ALTER TABLE Pupils ADD COLUMN Active INTEGER DEFAULT 1;",
          check="SELECT FirstName, Active FROM Pupils;"),
        X(2, "הוסיפו עמודה `Email` לתלמידים, ועדכנו לתלמיד 201 את הכתובת 'adam@mail.com'.",
          "ALTER TABLE Pupils ADD COLUMN Email TEXT;\nUPDATE Pupils SET Email = 'adam@mail.com' WHERE PupilId = 201;",
          check="SELECT PupilId, FirstName, Email FROM Pupils WHERE PupilId IN (201, 202);"),
        X(2, "צרו טבלת `Exams` (מבחני נגינה): קוד מבחן (PK), תלמיד (FK ל‑Pupils), ציון עם `CHECK` בין 0 ל‑100. הוסיפו 3 מבחנים.",
          "CREATE TABLE Exams (\n  ExamId     INTEGER PRIMARY KEY,\n  ExamPupil  INTEGER NOT NULL REFERENCES Pupils(PupilId),\n  ExamScore  INTEGER CHECK (ExamScore BETWEEN 0 AND 100)\n);\nINSERT INTO Exams VALUES (1, 201, 88);\nINSERT INTO Exams VALUES (2, 202, 95);\nINSERT INTO Exams VALUES (3, 205, 72);",
          check="SELECT FirstName, ExamScore\nFROM   Exams, Pupils\nWHERE  ExamPupil = PupilId;"),
        X(3, "צרו טבלה מקשרת `Performances` (איזה תלמיד מופיע באיזה קונצרט) עם **מפתח ראשי מורכב**. צרו גם את טבלת `Concerts`, והוסיפו נתונים.",
          "CREATE TABLE Concerts (\n  ConcertId    INTEGER PRIMARY KEY,\n  ConcertName  TEXT NOT NULL\n);\nCREATE TABLE Performances (\n  PerfConcert  INTEGER REFERENCES Concerts(ConcertId),\n  PerfPupil    INTEGER REFERENCES Pupils(PupilId),\n  PieceName    TEXT,\n  PRIMARY KEY (PerfConcert, PerfPupil)\n);\nINSERT INTO Concerts VALUES (1, 'קונצרט חנוכה');\nINSERT INTO Concerts VALUES (2, 'קונצרט סוף שנה');\nINSERT INTO Performances VALUES (1, 202, 'פור אליזה');\nINSERT INTO Performances VALUES (1, 205, 'בלוז בגיטרה');\nINSERT INTO Performances VALUES (2, 202, 'סונטה');",
          check="SELECT ConcertName, FirstName, PieceName\nFROM   Performances, Concerts, Pupils\nWHERE  PerfConcert = ConcertId AND PerfPupil = PupilId;"),
        X(3, "צרו טבלה, הוסיפו לה שורה, ואז מחקו אותה עם `DROP TABLE`. בדקו ברשימת הטבלאות שהיא נעלמה.",
          "CREATE TABLE Temp (x INTEGER);\nINSERT INTO Temp VALUES (1);\nDROP TABLE Temp;",
          check="SELECT name FROM sqlite_master WHERE type = 'table';",
          note="`sqlite_master` היא \"טבלת הטבלאות\" של SQLite — הרשימה של כל מה שיש בבסיס הנתונים."),
    ],
    extra=[
        X(1, "הוסיפו לטבלת המקצועות עמודה `Room` (מספר).",
          "ALTER TABLE Courses ADD COLUMN Room INTEGER;",
          check="SELECT CourseName, Room FROM Courses;"),
        X(2, "צרו טבלת `Parents`: קוד הורה (PK), שם (חובה), טלפון (ייחודי — `UNIQUE`), תלמיד (FK ל‑Students). הוסיפו 2 הורים.",
          "CREATE TABLE Parents (\n  ParentId    INTEGER PRIMARY KEY,\n  ParentName  TEXT NOT NULL,\n  Phone       TEXT UNIQUE,\n  StudentId   INTEGER REFERENCES Students(StudentId)\n);\nINSERT INTO Parents VALUES (1, 'סמיר חלבי', '050-9000001', 1001);\nINSERT INTO Parents VALUES (2, 'רינה כהן',  '052-9000002', 1003);",
          check="SELECT ParentName, S.FirstName AS Child\nFROM   Parents P, Students S\nWHERE  P.StudentId = S.StudentId;"),
        X(3, "שנו את השם של העמודה `Reason` בטבלת ההיעדרויות ל‑`Note`, ומחקו את העמודה `Excused`.",
          "ALTER TABLE Absences RENAME COLUMN Reason TO Note;\nALTER TABLE Absences DROP COLUMN Excused;",
          check="SELECT * FROM Absences LIMIT 3;"),
    ],
)
