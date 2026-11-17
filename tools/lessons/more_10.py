"""Lesson 10 — more practice + exam-style questions."""
from _h import P, Q, X


def extend(L):
    L["predict"] += [
        P("SELECT TeacherName\nFROM   Teachers\nWHERE  HourRate < (SELECT AVG(HourRate) FROM Teachers);", "אילו מורים יחזרו?"),
        P("SELECT InstName\nFROM   Instruments\nWHERE  InstCode IN (SELECT TeachInst FROM Teachers WHERE HourRate >= 130);", "אילו כלים יחזרו?"),
    ]
    L["exercises"] += [
        X(1, "הרישום (או הרישומים) עם התשלום הגבוה ביותר.",
          "SELECT RegPupil, RegTeacher, MonthlyFee\nFROM   Registrations\nWHERE  MonthlyFee = (SELECT MAX(MonthlyFee) FROM Registrations);"),
        X(1, "מורים שהמחיר שלהם שווה למחיר של 'נור מנסור' או גבוה ממנו.",
          "SELECT TeacherName, HourRate\nFROM   Teachers\nWHERE  HourRate >= (SELECT HourRate FROM Teachers WHERE TeacherName = 'נור מנסור');"),
        X(2, "תלמידים (שמות) שאינם לומדים אצל המורה 5.",
          "SELECT FirstName, LastName\nFROM   Pupils\nWHERE  PupilId NOT IN (SELECT RegPupil FROM Registrations WHERE RegTeacher = 5);"),
        X(2, "ערים (שמות) שאין בהן תלמידים.",
          "SELECT CityName\nFROM   Cities\nWHERE  CityCode NOT IN (SELECT HomeTown FROM Pupils);"),
        X(2, "תלמידים (שמות) שלומדים אצל 'רונית לוי'.",
          "SELECT FirstName, LastName\nFROM   Pupils\nWHERE  PupilId IN (SELECT RegPupil FROM Registrations\n                   WHERE  RegTeacher = (SELECT TeacherCode FROM Teachers\n                                        WHERE  TeacherName = 'רונית לוי'));"),
        X(3, "מורים שאף אחד מהתלמידים שלהם אינו מתחיל.",
          "SELECT TeacherName\nFROM   Teachers\nWHERE  TeacherCode IN (SELECT RegTeacher FROM Registrations)\n  AND  TeacherCode NOT IN (SELECT RegTeacher FROM Registrations\n                           WHERE  PupilLevel = 'מתחיל');"),
        X(3, "תלמידים שנולדו באותה שנה כמו התלמיד הצעיר ביותר שיש לו לוקר.",
          "SELECT FirstName, BirthYear\nFROM   Pupils\nWHERE  BirthYear = (SELECT MAX(BirthYear) FROM Pupils\n                    WHERE  PupilId IN (SELECT LockerPupil FROM Lockers));"),
    ]
    L["extra"] += [
        X(1, "התלמיד (או התלמידים) עם תאריך הלידה המוקדם ביותר.",
          "SELECT FirstName, LastName, BirthDate\nFROM   Students\nWHERE  BirthDate = (SELECT MIN(BirthDate) FROM Students);"),
        X(2, "מקצועות שאף תלמיד לא קיבל בהם ציון מתחת ל‑60.",
          "SELECT CourseName\nFROM   Courses\nWHERE  CourseCode NOT IN (SELECT CourseCode FROM Grades WHERE Grade < 60);"),
        X(2, "תלמידים שגרים באותה עיר כמו המורה 'נביל'.",
          "SELECT FirstName, LastName\nFROM   Students\nWHERE  CityCode = (SELECT CityCode FROM Teachers WHERE FirstName = 'נביל');"),
        X(3, "ציונים במקצוע 12 שגבוהים מהממוצע של מקצוע 12.",
          "SELECT StudentId, Grade\nFROM   Grades\nWHERE  CourseCode = 12\n  AND  Grade > (SELECT AVG(Grade) FROM Grades WHERE CourseCode = 12);"),
    ]
    L["exam_db"] = "repairs"
    L["exam"] = [
        Q(1, "התיקונים שמחירם גבוה מהמחיר הממוצע של תיקון.",
          "SELECT RepairNum, CustName, RepairPrice\nFROM   Repairs\nWHERE  RepairPrice > (SELECT AVG(RepairPrice) FROM Repairs);"),
        Q(1, "הטכנאי (או הטכנאים) עם השכר לשעה הנמוך ביותר.",
          "SELECT TechFirst, TechLast\nFROM   Technicians\nWHERE  HourWage = (SELECT MIN(HourWage) FROM Technicians);"),
        Q(2, "טכנאים שאין להם עמדת עבודה (`Benches`).",
          "SELECT TechFirst, TechLast\nFROM   Technicians\nWHERE  TechCode NOT IN (SELECT BenchTech FROM Benches);"),
        Q(2, "חלפים שלא השתמשו בהם באף תיקון.",
          "SELECT PartName\nFROM   Parts\nWHERE  PartCode NOT IN (SELECT UsePart FROM PartUsage);"),
        Q(2, "", "SELECT DevName\nFROM   DevTypes\nWHERE  DevCode NOT IN (SELECT RepairDev FROM Repairs WHERE Priority = 'רגיל');", kind="output"),
        Q(3, "השלימו את הערכים בטבלה שתתקבל.",
          "SELECT TechFirst\nFROM   Technicians\nWHERE  TechCode IN (SELECT RepairTech FROM Repairs WHERE Priority = 'מיידי');", kind="value"),
        Q(3, "השלימו כך שיוצגו שמות הלקוחות שבתיקון שלהם הוחלף מסך (חלף 101).",
          "SELECT CustName\nFROM   Repairs\nWHERE  RepairNum IN (SELECT UseRepair FROM PartUsage WHERE UsePart = 101);", kind="complete",
          given="SELECT CustName\nFROM   Repairs\nWHERE  RepairNum __ (______ UseRepair ____ PartUsage _____ UsePart = ___);"),
    ]
