"""Lesson 12 — more practice + exam-style questions."""
from _h import P, Q, X


def extend(L):
    L["predict"] += [
        P("UPDATE Teachers SET HourRate = HourRate * 2 WHERE TeacherCode = 5;\nSELECT HourRate FROM Teachers WHERE TeacherCode = 5;", "מה הערך?"),
        P("DELETE FROM Registrations WHERE PupilLevel = 'מתחיל';\nSELECT COUNT(*) FROM Registrations;", "כמה רישומים נשארו?"),
    ]
    L["exercises"] += [
        X(1, "הוסיפו את העיר 'סח'נין' בקוד 6.",
          "INSERT INTO Cities VALUES (6, 'סח''נין');",
          check="SELECT * FROM Cities;"),
        X(1, "שנו את שם הכלי 'עוד' ל‑'עוד ערבי'.",
          "UPDATE Instruments\nSET    InstName = 'עוד ערבי'\nWHERE  InstCode = 60;",
          check="SELECT * FROM Instruments;"),
        X(2, "הוסיפו רישום חדש: התלמיד 206 לומד אצל המורה 2, בשנת 2026, ברמת 'מתחיל', 390 לחודש.",
          "INSERT INTO Registrations VALUES (206, 2, 2026, 'מתחיל', 390);",
          check="SELECT * FROM Registrations WHERE RegPupil = 206;"),
        X(2, "העבירו את כל הלוקרים מקומה 1 לקומה 3.",
          "UPDATE Lockers\nSET    LockerFloor = 3\nWHERE  LockerFloor = 1;",
          check="SELECT * FROM Lockers;"),
        X(2, "מחקו את כל הרישומים שהתשלום בהם נמוך מ‑300.",
          "DELETE FROM Registrations\nWHERE  MonthlyFee < 300;",
          check="SELECT RegPupil, MonthlyFee FROM Registrations;"),
        X(3, "עדכנו בבת אחת: המורה 3 מקבל טלפון '050-3333333' ומחיר 115.",
          "UPDATE Teachers\nSET    TeacherPhone = '050-3333333', HourRate = 115\nWHERE  TeacherCode = 3;",
          check="SELECT * FROM Teachers WHERE TeacherCode = 3;"),
        X(3, "מחקו את הלוקרים של התלמידים שנולדו לפני 2010.",
          "DELETE FROM Lockers\nWHERE  LockerPupil IN (SELECT PupilId FROM Pupils WHERE BirthYear < 2010);",
          check="SELECT * FROM Lockers;"),
    ]
    L["extra"] += [
        X(1, "הוסיפו מקצוע חדש: 18, 'רובוטיקה', מורה 3, 2 שעות.",
          "INSERT INTO Courses VALUES (18, 'רובוטיקה', 3, 2);",
          check="SELECT * FROM Courses;"),
        X(2, "שבצו את הכיתה 104 לחדר 22.",
          "UPDATE Classes\nSET    RoomNumber = 22\nWHERE  ClassCode = 104;",
          check="SELECT * FROM Classes;"),
        X(2, "תנו ציון 0 לכל מי שלא נבחן (Grade הוא NULL).",
          "UPDATE Grades\nSET    Grade = 0\nWHERE  Grade IS NULL;",
          check="SELECT StudentId, CourseCode, Grade FROM Grades WHERE Grade = 0;"),
        X(3, "מחקו את כל ההיעדרויות של תלמידי הכיתה 104.",
          "DELETE FROM Absences\nWHERE  StudentId IN (SELECT StudentId FROM Students WHERE ClassCode = 104);",
          check="SELECT COUNT(*) AS Left FROM Absences;"),
    ]
    L["exam_db"] = "library"
    L["exam"] = [
        Q(1, "הוסיפו קורא חדש: 511, 'ג'ני', 'נסאר', עיר 3, נולדה ב‑2008.",
          "INSERT INTO Members VALUES (511, 'ג''ני', 'נסאר', 3, 2008);",
          check="SELECT * FROM Members WHERE MemberId = 511;"),
        Q(1, "עדכנו שההשאלה 5 הוחזרה ב‑'2025-10-15'.",
          "UPDATE Loans\nSET    ReturnDate = '2025-10-15'\nWHERE  LoanId = 5;",
          check="SELECT * FROM Loans WHERE LoanId = 5;"),
        Q(2, "הגדילו ב‑10 את מספר העמודים של כל ספרי המתח.",
          "UPDATE Books\nSET    Pages = Pages + 10\nWHERE  Genre = 'מתח';",
          check="SELECT Title, Pages FROM Books WHERE Genre = 'מתח';"),
        Q(2, "מחקו את כל ההשאלות שהוחזרו.",
          "DELETE FROM Loans\nWHERE  ReturnDate IS NOT NULL;",
          check="SELECT COUNT(*) AS Left FROM Loans;"),
        Q(3, "מחקו את כל ההשאלות של הקוראים מעכו.",
          "DELETE FROM Loans\nWHERE  ReaderId IN (SELECT MemberId FROM Members, Cities\n                   WHERE  TownCode = CityCode AND CityName = 'עכו');",
          check="SELECT LoanId, ReaderId FROM Loans;"),
        Q(3, "השלימו את הפקודה שמשנה את הז'אנר של הספר 210 ל‑'מסה'.",
          "UPDATE Books\nSET    Genre = 'מסה'\nWHERE  BookCode = 210;", kind="complete",
          check="SELECT Title, Genre FROM Books WHERE BookCode = 210;",
          given="______ Books\n___    _____ = 'מסה'\n_____  ________ = 210;"),
    ]
