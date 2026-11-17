"""Lesson 4 — more practice + exam-style questions."""
from _h import P, Q, X


def extend(L):
    L["predict"] += [
        P("SELECT InstName\nFROM   Instruments\nORDER BY InstCode DESC\nLIMIT  2;", "אילו שני כלים יחזרו?"),
        P("SELECT RegPupil, MonthlyFee\nFROM   Registrations\nWHERE  RegTeacher = 1\nORDER BY MonthlyFee;",
          "מה תהיה השורה האחרונה?"),
    ]
    L["exercises"] += [
        X(1, "הציגו את הערים לפי שם העיר (א–ת).",
          "SELECT CityName\nFROM   Cities\nORDER BY CityName;"),
        X(1, "הציגו את הלוקרים לפי קומה (יורד).",
          "SELECT LockerNum, LockerFloor\nFROM   Lockers\nORDER BY LockerFloor DESC;"),
        X(2, "הציגו את התלמידים מעיר 1, מהצעיר למבוגר.",
          "SELECT FirstName, BirthYear\nFROM   Pupils\nWHERE  HomeTown = 1\nORDER BY BirthYear DESC;"),
        X(2, "הציגו את 3 הרישומים הזולים ביותר.",
          "SELECT RegPupil, RegTeacher, MonthlyFee\nFROM   Registrations\nORDER BY MonthlyFee\nLIMIT  3;"),
        X(2, "הציגו את המורים לפי כלי (`TeachInst`), ובתוך כל כלי מהיקר לזול.",
          "SELECT TeachInst, TeacherName, HourRate\nFROM   Teachers\nORDER BY TeachInst, HourRate DESC;"),
        X(3, "הציגו את המורה השני הכי יקר (רמז: `LIMIT 1 OFFSET 1`).",
          "SELECT TeacherName, HourRate\nFROM   Teachers\nORDER BY HourRate DESC\nLIMIT  1 OFFSET 1;"),
        X(3, "הציגו את 4 התלמידים הראשונים לפי שם משפחה, ובתיקו לפי שם פרטי.",
          "SELECT LastName, FirstName\nFROM   Pupils\nORDER BY LastName, FirstName\nLIMIT  4;"),
    ]
    L["extra"] += [
        X(1, "הציגו את המקצועות לפי מספר השעות השבועיות, מהגבוה לנמוך.",
          "SELECT CourseName, WeeklyHours\nFROM   Courses\nORDER BY WeeklyHours DESC;"),
        X(2, "הציגו את ההיעדרויות לפי תאריך, מהאחרונה לראשונה.",
          "SELECT StudentId, AbsenceDate\nFROM   Absences\nORDER BY AbsenceDate DESC;"),
        X(2, "הציגו את 3 התלמידים הצעירים ביותר (לפי תאריך לידה).",
          "SELECT FirstName, BirthDate\nFROM   Students\nWHERE  BirthDate IS NOT NULL\nORDER BY BirthDate DESC\nLIMIT  3;"),
        X(3, "הציגו את הציונים של מקצוע 11, לפי מחצית ובתוך המחצית מהגבוה לנמוך.",
          "SELECT Term, StudentId, Grade\nFROM   Grades\nWHERE  CourseCode = 11\nORDER BY Term, Grade DESC;"),
    ]
    L["exam_db"] = "repairs"
    L["exam"] = [
        Q(1, "הציגו את הטכנאים לפי השכר לשעה, מהגבוה לנמוך.",
          "SELECT TechFirst, TechLast, HourWage\nFROM   Technicians\nORDER BY HourWage DESC;"),
        Q(1, "הציגו את החלפים לפי שם החלף (א–ת).",
          "SELECT PartName, PartPrice\nFROM   Parts\nORDER BY PartName;"),
        Q(2, "הציגו את התיקונים הדחופים, מהיקר לזול.",
          "SELECT RepairNum, CustName, RepairPrice\nFROM   Repairs\nWHERE  Priority = 'דחוף'\nORDER BY RepairPrice DESC;"),
        Q(2, "הציגו את 3 התיקונים הראשונים שהתקבלו במעבדה.",
          "SELECT RepairNum, CustName, InDate\nFROM   Repairs\nORDER BY InDate\nLIMIT  3;"),
        Q(2, "", "SELECT TechFirst, StartDate\nFROM   Technicians\nORDER BY StartDate\nLIMIT  2;", kind="output"),
        Q(2, "מה יהיה בשורה הראשונה?",
          "SELECT CustName, RepairPrice\nFROM   Repairs\nWHERE  RepairDev = 10\nORDER BY RepairPrice;", kind="value"),
        Q(3, "השלימו כך שיוצגו התיקונים לפי עדיפות, ובתוך כל עדיפות מהיקר לזול.",
          "SELECT Priority, RepairPrice, CustName\nFROM   Repairs\nORDER BY Priority, RepairPrice DESC;", kind="complete",
          given="SELECT Priority, RepairPrice, CustName\nFROM   Repairs\n_____ __ ________, RepairPrice ____;"),
    ]
