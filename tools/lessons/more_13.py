"""Lesson 13 — more practice + exam-style questions."""
from _h import Q, X


def extend(L):
    L["exercises"] += [
        X(1, "צרו טבלה `Books` לספרי תווים: קוד (PK), שם (חובה), מחיר. הוסיפו 2 ספרים.",
          "CREATE TABLE Books (\n  BookCode   INTEGER PRIMARY KEY,\n  BookName   TEXT NOT NULL,\n  BookPrice  INTEGER\n);\nINSERT INTO Books VALUES (1, 'תווים לפסנתר א', 60);\nINSERT INTO Books VALUES (2, 'שיטת גיטרה', 75);",
          check="SELECT * FROM Books;"),
        X(1, "הוסיפו לטבלת הכלים עמודה `Price` (מספר).",
          "ALTER TABLE Instruments ADD COLUMN Price INTEGER;",
          check="SELECT * FROM Instruments;"),
        X(2, "שנו את שם העמודה `TeacherPhone` ל‑`Phone`.",
          "ALTER TABLE Teachers RENAME COLUMN TeacherPhone TO Phone;",
          check="SELECT TeacherName, Phone FROM Teachers;"),
        X(2, "הוסיפו לטבלת הרישומים עמודה `Paid` עם ברירת מחדל 0, ועדכנו ל‑1 את הרישומים של 2025.",
          "ALTER TABLE Registrations ADD COLUMN Paid INTEGER DEFAULT 0;\nUPDATE Registrations SET Paid = 1 WHERE RegYear = 2025;",
          check="SELECT Paid, COUNT(*) AS Regs FROM Registrations GROUP BY Paid;"),
        X(2, "מחקו את הטבלה `Lockers` לגמרי.",
          "DROP TABLE Lockers;",
          check="SELECT name FROM sqlite_master WHERE type = 'table';"),
        X(3, "צרו טבלה `Rentals` (השכרת כלים): קוד (PK), תלמיד (FK ל‑Pupils), כלי (FK ל‑Instruments), חודשים עם `CHECK` בין 1 ל‑12. הוסיפו 2 השכרות והציגו שם תלמיד ושם כלי.",
          "CREATE TABLE Rentals (\n  RentId     INTEGER PRIMARY KEY,\n  RentPupil  INTEGER REFERENCES Pupils(PupilId),\n  RentInst   INTEGER REFERENCES Instruments(InstCode),\n  Months     INTEGER CHECK (Months BETWEEN 1 AND 12)\n);\nINSERT INTO Rentals VALUES (1, 203, 20, 6);\nINSERT INTO Rentals VALUES (2, 209, 10, 12);",
          check="SELECT FirstName, InstName, Months\nFROM   Rentals, Pupils, Instruments\nWHERE  RentPupil = PupilId AND RentInst = InstCode;"),
    ]
    L["extra"] += [
        X(1, "הוסיפו לטבלת התלמידים עמודה `Email`.",
          "ALTER TABLE Students ADD COLUMN Email TEXT;",
          check="SELECT FirstName, Email FROM Students LIMIT 3;"),
        X(2, "מחקו מטבלת המורים את העמודה `Phone`.",
          "ALTER TABLE Teachers DROP COLUMN Phone;",
          check="SELECT * FROM Teachers LIMIT 2;"),
        X(3, "צרו טבלת `Clubs` (חוגים) עם קוד (PK), שם (חובה, ייחודי) ומורה אחראי (FK ל‑Teachers). הוסיפו 2 חוגים והציגו שם חוג ושם מורה.",
          "CREATE TABLE Clubs (\n  ClubCode     INTEGER PRIMARY KEY,\n  ClubName     TEXT NOT NULL UNIQUE,\n  TeacherCode  INTEGER REFERENCES Teachers(TeacherCode)\n);\nINSERT INTO Clubs VALUES (1, 'מקהלה', 4);\nINSERT INTO Clubs VALUES (2, 'שחמט', 1);",
          check="SELECT ClubName, FirstName\nFROM   Clubs C, Teachers T\nWHERE  C.TeacherCode = T.TeacherCode;"),
    ]
    L["exam_db"] = "games"
    L["exam"] = [
        Q(1, "הוסיפו לטבלת המשתמשים עמודה `Phone` מסוג טקסט.",
          "ALTER TABLE Users ADD COLUMN Phone TEXT;",
          check="SELECT UserId, FirstName, Phone FROM Users LIMIT 3;"),
        Q(1, "מחקו מטבלת החברות את העמודה `Country`.",
          "ALTER TABLE Companies DROP COLUMN Country;",
          check="SELECT * FROM Companies;"),
        Q(2, "צרו טבלת `Reviews`: קוד (PK), משתמש (FK ל‑Users), משחק (FK ל‑Games), ציון עם `CHECK` בין 1 ל‑5. הוסיפו 2 ביקורות.",
          "CREATE TABLE Reviews (\n  ReviewId    INTEGER PRIMARY KEY,\n  ReviewUser  INTEGER REFERENCES Users(UserId),\n  ReviewGame  INTEGER REFERENCES Games(GameCode),\n  Stars       INTEGER CHECK (Stars BETWEEN 1 AND 5)\n);\nINSERT INTO Reviews VALUES (1, 1, 2, 5);\nINSERT INTO Reviews VALUES (2, 3, 8, 3);",
          check="SELECT FirstName, GameName, Stars\nFROM   Reviews, Users, Games\nWHERE  ReviewUser = UserId AND ReviewGame = GameCode;"),
        Q(2, "מחקו את הטבלה `Categories`.",
          "DROP TABLE Categories;",
          check="SELECT name FROM sqlite_master WHERE type = 'table';"),
        Q(3, "השלימו את הפקודה שמוסיפה עמודת `Discount` למשחקים עם ערך ברירת מחדל 0.",
          "ALTER TABLE Games ADD COLUMN Discount INTEGER DEFAULT 0;", kind="complete",
          check="SELECT GameName, Discount FROM Games LIMIT 3;",
          given="_____ _____ Games ___ ______ Discount INTEGER _______ 0;"),
        Q(3, "כתבו (על דף — SQLite לא מריץ את זה) את הפקודה שמשנה את טיפוס העמודה `Email` ל‑`VARCHAR(50)`. "
             "מה כן אפשר להריץ: שנו את שם העמודה `Email` ל‑`Mail`.",
          "ALTER TABLE Users RENAME COLUMN Email TO Mail;",
          check="SELECT FirstName, Mail FROM Users LIMIT 3;",
          note="בבחינה: `ALTER TABLE Users MODIFY COLUMN Email VARCHAR(50);`"),
    ]
