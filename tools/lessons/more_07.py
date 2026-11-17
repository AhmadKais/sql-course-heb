"""Lesson 7 — more practice + exam-style questions."""
from _h import P, Q, X


def extend(L):
    L["predict"] += [
        P("SELECT   LockerFloor, COUNT(*)\nFROM     Lockers\nGROUP BY LockerFloor;", "איזו טבלה תתקבל?"),
        P("SELECT   RegYear, COUNT(*)\nFROM     Registrations\nGROUP BY RegYear\nHAVING   COUNT(*) >= 4;", "אילו שנים יחזרו?"),
    ]
    L["exercises"] += [
        X(1, "כמה כלים יש בכל משפחת כלים?",
          "SELECT   InstFamily, COUNT(*) AS Instruments\nFROM     Instruments\nGROUP BY InstFamily;"),
        X(1, "כמה לוקרים יש בכל קומה?",
          "SELECT   LockerFloor, COUNT(*) AS Lockers\nFROM     Lockers\nGROUP BY LockerFloor;"),
        X(2, "לכל מורה: התשלום הגבוה ביותר שמשלמים לו.",
          "SELECT   RegTeacher, MAX(MonthlyFee) AS MaxFee\nFROM     Registrations\nGROUP BY RegTeacher;"),
        X(2, "שנים שהיו בהן לפחות 3 רישומים.",
          "SELECT   RegYear, COUNT(*) AS Regs\nFROM     Registrations\nGROUP BY RegYear\nHAVING   COUNT(*) >= 3;"),
        X(2, "לכל עיר: שנת הלידה של התלמיד הצעיר ביותר.",
          "SELECT   HomeTown, MAX(BirthYear) AS Youngest\nFROM     Pupils\nGROUP BY HomeTown;"),
        X(3, "כלים (`TeachInst`) שמלמדים אותם יותר ממורה אחד.",
          "SELECT   TeachInst, COUNT(*) AS Teachers\nFROM     Teachers\nGROUP BY TeachInst\nHAVING   COUNT(*) > 1;"),
        X(3, "לכל מורה — רק ברישומים מ‑2024 ואילך — סכום התשלומים. הציגו מורים עם סכום מעל 500, מהגבוה לנמוך.",
          "SELECT   RegTeacher, SUM(MonthlyFee) AS Total\nFROM     Registrations\nWHERE    RegYear >= 2024\nGROUP BY RegTeacher\nHAVING   SUM(MonthlyFee) > 500\nORDER BY Total DESC;"),
    ]
    L["extra"] += [
        X(1, "כמה כיתות יש בכל שכבה?",
          "SELECT   Grade, COUNT(*) AS Classes\nFROM     Classes\nGROUP BY Grade;"),
        X(2, "לכל עיר (`CityCode`): כמה תלמידים, רק ערים עם 3 תלמידים ומעלה.",
          "SELECT   CityCode, COUNT(*) AS Students\nFROM     Students\nGROUP BY CityCode\nHAVING   COUNT(*) >= 3;"),
        X(2, "לכל מחצית: מספר הציונים והציון הממוצע (מעוגל).",
          "SELECT   Term, COUNT(Grade) AS Grades, ROUND(AVG(Grade), 1) AS AvgGrade\nFROM     Grades\nGROUP BY Term;"),
        X(3, "תלמידים שהציון הנמוך ביותר שלהם במחצית 1 הוא מתחת ל‑55.",
          "SELECT   StudentId, MIN(Grade) AS Lowest\nFROM     Grades\nWHERE    Term = 1\nGROUP BY StudentId\nHAVING   MIN(Grade) < 55;"),
    ]
    L["exam_db"] = "repairs"
    L["exam"] = [
        Q(1, "כמה תיקונים יש בכל רמת עדיפות?",
          "SELECT   Priority, COUNT(*) AS Repairs\nFROM     Repairs\nGROUP BY Priority;"),
        Q(1, "לכל טכנאי (`RepairTech`): סך מחירי התיקונים שלו.",
          "SELECT   RepairTech, SUM(RepairPrice) AS Total\nFROM     Repairs\nGROUP BY RepairTech;"),
        Q(2, "סוגי מכשירים (`RepairDev`) שתוקנו 3 פעמים או יותר.",
          "SELECT   RepairDev, COUNT(*) AS Repairs\nFROM     Repairs\nGROUP BY RepairDev\nHAVING   COUNT(*) >= 3;"),
        Q(2, "לכל עיר (`TechCity`): מספר הטכנאים והשכר הממוצע לשעה.",
          "SELECT   TechCity, COUNT(*) AS Techs, AVG(HourWage) AS AvgWage\nFROM     Technicians\nGROUP BY TechCity;"),
        Q(2, "השלימו את הערכים בטבלה שתתקבל.",
          "SELECT   BenchFloor, COUNT(*)\nFROM     Benches\nGROUP BY BenchFloor;", kind="value"),
        Q(3, "", "SELECT   RepairTech, COUNT(*) AS N\nFROM     Repairs\nWHERE    DoneDate IS NULL\nGROUP BY RepairTech;", kind="output"),
        Q(3, "השלימו כך שיוצגו הטכנאים שהמחיר הממוצע של התיקונים שלהם מעל 600.",
          "SELECT   RepairTech, AVG(RepairPrice)\nFROM     Repairs\nGROUP BY RepairTech\nHAVING   AVG(RepairPrice) > 600;", kind="complete",
          given="SELECT   RepairTech, AVG(RepairPrice)\nFROM     Repairs\n_____ __ __________\n______   ___(RepairPrice) > 600;"),
    ]
