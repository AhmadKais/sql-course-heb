"""Lesson 1 — more practice + exam-style questions."""
from _h import P, Q, X


def extend(L):
    L["predict"] += [
        P("SELECT DISTINCT RegTeacher\nFROM   Registrations;", "כמה שורות יחזרו?"),
        P("SELECT FirstName, 2026 - BirthYear AS Age\nFROM   Pupils;", "מה הגיל של מאיה בתוצאה?"),
    ]
    L["exercises"] += [
        X(1, "הציגו את קוד המורה ואת שם המורה בלבד.",
          "SELECT TeacherCode, TeacherName\nFROM   Teachers;"),
        X(1, "הציגו את כל העמודות של טבלת הערים (`Cities`).",
          "SELECT *\nFROM   Cities;"),
        X(2, "הציגו לכל לוקר את מספרו ואת הקומה, בשמות `Locker` ו‑`Floor`.",
          "SELECT LockerNum AS Locker, LockerFloor AS Floor\nFROM   Lockers;"),
        X(2, "אילו תלמידים (קודים) רשומים לשיעורים? כל תלמיד פעם אחת.",
          "SELECT DISTINCT RegPupil\nFROM   Registrations;"),
        X(2, "הציגו לכל רישום את קוד התלמיד, התשלום החודשי והתשלום לשבוע (חלקי 4), בשם `Weekly`.",
          "SELECT RegPupil, MonthlyFee, MonthlyFee / 4 AS Weekly\nFROM   Registrations;"),
        X(3, "אילו צירופים של שנה ורמה קיימים ברישומים? כל צירוף פעם אחת.",
          "SELECT DISTINCT RegYear, PupilLevel\nFROM   Registrations;"),
        X(3, "הציגו לכל מורה משפט אחד בעמודה `Info`, למשל: `סמיר חלבי - 120`.",
          "SELECT TeacherName || ' - ' || HourRate AS Info\nFROM   Teachers;"),
    ]
    L["extra"] += [
        X(1, "הציגו את שם הכיתה ואת השכבה של כל הכיתות.",
          "SELECT ClassName, Grade\nFROM   Classes;"),
        X(1, "הציגו את קוד התלמיד, תאריך ההיעדרות והסיבה מטבלת ההיעדרויות.",
          "SELECT StudentId, AbsenceDate, Reason\nFROM   Absences;"),
        X(2, "באילו שכבות יש כיתות? כל שכבה פעם אחת.",
          "SELECT DISTINCT Grade\nFROM   Classes;"),
        X(3, "הציגו לכל ציון את קוד התלמיד ואת הציון אחרי פקטור של 5 נקודות, בשם `WithFactor`.",
          "SELECT StudentId, Grade + 5 AS WithFactor\nFROM   Grades;"),
    ]
    L["exam_db"] = "games"
    L["exam"] = [
        Q(1, "הציגו את שם המשחק ואת שנת היציאה של כל המשחקים.",
          "SELECT GameName, GameYear\nFROM   Games;"),
        Q(1, "הציגו את השם הפרטי, שם המשפחה והאימייל של כל המשתמשים.",
          "SELECT FirstName, LastName, Email\nFROM   Users;"),
        Q(2, "באילו מדינות יש חברות משחקים? כל מדינה פעם אחת.",
          "SELECT DISTINCT Country\nFROM   Companies;"),
        Q(2, "הציגו לכל משחק את שמו ואת המחיר ל‑3 שעות משחק, בשם `ThreeHours`.",
          "SELECT GameName, PricePerHour * 3 AS ThreeHours\nFROM   Games;"),
        Q(2, "", "SELECT DISTINCT BuyerId\nFROM   Orders;", kind="output"),
        Q(2, "כמה שורות יחזרו, ומה הן?", "SELECT DISTINCT TypeCode\nFROM   Games;", kind="value"),
        Q(3, "השלימו כך שיוצגו שם המשחק ומספר השנים מאז שיצא (עד 2026), בשם `Age`.",
          "SELECT GameName, 2026 - GameYear AS Age\nFROM   Games;", kind="complete",
          given="SELECT GameName, ________ AS ____\nFROM   _____;"),
    ]
