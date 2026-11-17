"""Lesson 6 — more practice + exam-style questions."""
from _h import P, Q, X


def extend(L):
    L["predict"] += [
        P("SELECT COUNT(DISTINCT HomeTown), COUNT(*)\nFROM   Pupils;", "מה שני המספרים?"),
        P("SELECT SUM(MonthlyFee)\nFROM   Registrations\nWHERE  RegPupil = 204;", "מה הסכום?"),
    ]
    L["exercises"] += [
        X(1, "כמה כלים יש בטבלת הכלים?",
          "SELECT COUNT(*) AS Instruments\nFROM   Instruments;"),
        X(1, "מה המחיר לשעה הנמוך ביותר?",
          "SELECT MIN(HourRate) AS MinRate\nFROM   Teachers;"),
        X(2, "כמה תלמידים גרים בעיר 1?",
          "SELECT COUNT(*) AS Pupils\nFROM   Pupils\nWHERE  HomeTown = 1;"),
        X(2, "מה התשלום הממוצע ברישומים של שנת 2025?",
          "SELECT AVG(MonthlyFee) AS AvgFee\nFROM   Registrations\nWHERE  RegYear = 2025;"),
        X(2, "כמה לוקרים יש בקומה 2?",
          "SELECT COUNT(*) AS Lockers\nFROM   Lockers\nWHERE  LockerFloor = 2;"),
        X(3, "כמה מורים מלמדים כלי ממשפחת 'מיתר'? (רמז: `TeachInst IN (20, 30, 60)`)",
          "SELECT COUNT(*) AS StringTeachers\nFROM   Teachers\nWHERE  TeachInst IN (20, 30, 60);"),
        X(3, "מה סכום התשלומים, הממוצע (מעוגל) ומספר הרישומים של התלמידים המתקדמים — בשאילתה אחת?",
          "SELECT SUM(MonthlyFee) AS Total, ROUND(AVG(MonthlyFee)) AS AvgFee, COUNT(*) AS Regs\nFROM   Registrations\nWHERE  PupilLevel = 'מתקדם';"),
    ]
    L["extra"] += [
        X(1, "כמה כיתות יש?",
          "SELECT COUNT(*) AS Classes\nFROM   Classes;"),
        X(1, "מה השכר הגבוה ביותר של מורה?",
          "SELECT MAX(Salary) AS MaxSalary\nFROM   Teachers;"),
        X(2, "כמה שעות שבועיות יש בסך הכול בכל המקצועות?",
          "SELECT SUM(WeeklyHours) AS Hours\nFROM   Courses;"),
        X(3, "מה תאריך ההיעדרות הראשון והאחרון בטבלה?",
          "SELECT MIN(AbsenceDate) AS First, MAX(AbsenceDate) AS Last\nFROM   Absences;"),
    ]
    L["exam_db"] = "games"
    L["exam"] = [
        Q(1, "כמה משחקים יש בחנות?",
          "SELECT COUNT(*) AS Games\nFROM   Games;"),
        Q(1, "מה המחיר לשעה הגבוה ביותר?",
          "SELECT MAX(PricePerHour) AS MaxPrice\nFROM   Games;"),
        Q(2, "כמה משתמשים רשמו אימייל? (בלי `WHERE`)",
          "SELECT COUNT(Email) AS WithEmail\nFROM   Users;"),
        Q(2, "כמה שעות הוזמנו בסך הכול בספטמבר 2025?",
          "SELECT SUM(Hours) AS TotalHours\nFROM   Orders\nWHERE  OrderDate BETWEEN '2025-09-01' AND '2025-09-30';"),
        Q(2, "השלימו את שלושת הערכים.",
          "SELECT COUNT(*), COUNT(MakerCode), COUNT(DISTINCT MakerCode)\nFROM   Games;", kind="value"),
        Q(2, "", "SELECT MIN(GameYear) AS Oldest, MAX(GameYear) AS Newest\nFROM   Games;", kind="output"),
        Q(3, "השלימו כך שיוצג המחיר הממוצע לשעה של משחקי הספורט (קטגוריה 2), מעוגל לספרה אחת.",
          "SELECT ROUND(AVG(PricePerHour), 1) AS AvgPrice\nFROM   Games\nWHERE  TypeCode = 2;", kind="complete",
          given="SELECT _____(___(PricePerHour), 1) AS AvgPrice\nFROM   Games\n_____  TypeCode = _;"),
    ]
