"""Lesson 2 — more practice + exam-style questions."""
from _h import P, Q, X


def extend(L):
    L["predict"] += [
        P("SELECT InstName\nFROM   Instruments\nWHERE  InstFamily <> 'מיתר';", "אילו כלים יחזרו?"),
        P("SELECT COUNT(*)\nFROM   Registrations\nWHERE  RegYear >= 2024 AND MonthlyFee < 300;", "מה המספר?"),
    ]
    L["exercises"] += [
        X(1, "הציגו את הלוקרים שבקומה 1.",
          "SELECT LockerNum, LockerPupil\nFROM   Lockers\nWHERE  LockerFloor = 1;"),
        X(1, "הציגו את המורים שמחירם בדיוק 130.",
          "SELECT TeacherName\nFROM   Teachers\nWHERE  HourRate = 130;"),
        X(2, "הציגו רישומים משנת 2024 ואילך שאינם ברמת 'ממשיך'.",
          "SELECT RegPupil, RegYear, PupilLevel\nFROM   Registrations\nWHERE  RegYear >= 2024 AND PupilLevel <> 'ממשיך';"),
        X(2, "הציגו תלמידים שנולדו ב‑2009 או ב‑2014.",
          "SELECT FirstName, BirthYear\nFROM   Pupils\nWHERE  BirthYear = 2009 OR BirthYear = 2014;"),
        X(2, "הציגו את המורים שאינם מלמדים את כלי 10 (עם `NOT`).",
          "SELECT TeacherName, TeachInst\nFROM   Teachers\nWHERE  NOT TeachInst = 10;"),
        X(3, "הציגו רישומים של המורה 3 או 4, משנת 2023 בלבד.",
          "SELECT RegPupil, RegTeacher, RegYear\nFROM   Registrations\nWHERE  (RegTeacher = 3 OR RegTeacher = 4) AND RegYear = 2023;"),
        X(3, "הציגו רישומים שהתשלום השנתי בהם (12 חודשים) גבוה מ‑4,000.",
          "SELECT RegPupil, MonthlyFee * 12 AS YearFee\nFROM   Registrations\nWHERE  MonthlyFee * 12 > 4000;"),
    ]
    L["extra"] += [
        X(1, "הציגו את הכיתות של שכבה 11.",
          "SELECT ClassName\nFROM   Classes\nWHERE  Grade = 11;"),
        X(1, "הציגו מקצועות שנלמדים יותר מ‑3 שעות בשבוע.",
          "SELECT CourseName, WeeklyHours\nFROM   Courses\nWHERE  WeeklyHours > 3;"),
        X(2, "הציגו את הציונים של התלמיד 1007 במחצית 2.",
          "SELECT CourseCode, Grade\nFROM   Grades\nWHERE  StudentId = 1007 AND Term = 2;"),
        X(3, "הציגו תלמידים מהעיר 4 או 6 שנרשמו לפני 2026.",
          "SELECT FirstName, CityCode, EnrollDate\nFROM   Students\nWHERE  (CityCode = 4 OR CityCode = 6) AND EnrollDate < '2026-01-01';"),
    ]
    L["exam_db"] = "cafe"
    L["exam"] = [
        Q(1, "הציגו את שמות המנות שמחירן גבוה מ‑30.",
          "SELECT DishName, DishPrice\nFROM   Dishes\nWHERE  DishPrice > 30;"),
        Q(1, "הציגו את ההזמנות של המנה 30.",
          "SELECT OrderNum, CustName\nFROM   Orders\nWHERE  OrderDish = 30;"),
        Q(2, "הציגו את העובדים מהעיר 1 או 2 ששכרם לשעה לפחות 42.",
          "SELECT WorkerName, HourPay\nFROM   Workers\nWHERE  (WorkerCity = 1 OR WorkerCity = 2) AND HourPay >= 42;"),
        Q(2, "הציגו את ההזמנות אחרי 1 במאי 2026 שהיו בהן יותר מ‑3 סועדים.",
          "SELECT OrderNum, OrderDate, Guests\nFROM   Orders\nWHERE  OrderDate > '2026-05-01' AND Guests > 3;"),
        Q(2, "", "SELECT DishName\nFROM   Dishes\nWHERE  DishKind = 'קינוח';", kind="output"),
        Q(2, "כמה שורות יחזרו?", "SELECT WorkerName\nFROM   Workers\nWHERE  HourPay <> 38;", kind="value"),
        Q(3, "השלימו כך שיוצגו המנות העיקריות שמחירן נמוך מ‑50.",
          "SELECT DishName\nFROM   Dishes\nWHERE  DishKind = 'מנה עיקרית' AND DishPrice < 50;", kind="complete",
          given="SELECT DishName\nFROM   Dishes\n_____  DishKind = '__________' ___ DishPrice _ 50;"),
    ]
