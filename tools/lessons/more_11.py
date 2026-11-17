"""Lesson 11 — more practice + exam-style questions."""
from _h import P, Q, X

VIEW_Q1 = ("CREATE VIEW Q1 AS\nSELECT   RegPupil, COUNT(*) AS Lessons, SUM(MonthlyFee) AS Total\n"
           "FROM     Registrations\nGROUP BY RegPupil;\n\n")


def extend(L):
    L["predict"] += [
        P(VIEW_Q1 + "SELECT MAX(Total) FROM Q1;", "מה הערך?"),
        P(VIEW_Q1 + "SELECT COUNT(*) FROM Q1 WHERE Lessons = 1;", "מה המספר?"),
    ]
    L["exercises"] += [
        X(1, "צרו VIEW בשם `Expensive` — המורים שהמחיר שלהם 130 ומעלה. הציגו ממנו רק את השמות.",
          "CREATE VIEW Expensive AS\nSELECT * FROM Teachers WHERE HourRate >= 130;\n\nSELECT TeacherName FROM Expensive;"),
        X(2, "בעזרת Q1 (מספר שיעורים וסך תשלום לכל תלמיד): התלמידים שלומדים 2 שיעורים.",
          VIEW_Q1 + "SELECT RegPupil, Total\nFROM   Q1\nWHERE  Lessons = 2;"),
        X(2, "בעזרת Q1: שמות התלמידים שמשלמים פחות מ‑350, ממוינים לפי הסכום.",
          VIEW_Q1 + "SELECT FirstName, LastName, Total\nFROM   Q1, Pupils\nWHERE  RegPupil = PupilId AND Total < 350\nORDER BY Total;"),
        X(2, "צרו VIEW בשם `CityCount` — מספר התלמידים בכל עיר (`HomeTown`, `N`). הציגו את שם העיר עם הכי הרבה תלמידים.",
          "CREATE VIEW CityCount AS\nSELECT   HomeTown, COUNT(*) AS N\nFROM     Pupils\nGROUP BY HomeTown;\n\nSELECT CityName, N\nFROM   CityCount, Cities\nWHERE  HomeTown = CityCode\n  AND  N = (SELECT MAX(N) FROM CityCount);"),
        X(3, "צרו VIEW בשם `TeacherIncome` — לכל מורה (`RegTeacher`) סך התשלומים (`Income`). הציגו את המורים שההכנסה שלהם מעל הממוצע של ההכנסות.",
          "CREATE VIEW TeacherIncome AS\nSELECT   RegTeacher, SUM(MonthlyFee) AS Income\nFROM     Registrations\nGROUP BY RegTeacher;\n\nSELECT TeacherName, Income\nFROM   TeacherIncome, Teachers\nWHERE  RegTeacher = TeacherCode\n  AND  Income > (SELECT AVG(Income) FROM TeacherIncome);"),
        X(3, "בעזרת Q1: כמה תלמידים משלמים יותר מ‑500, וכמה — 500 או פחות? (קבצו לפי `CASE`)",
          VIEW_Q1 + "SELECT   CASE WHEN Total > 500 THEN 'מעל 500' ELSE '500 ומטה' END AS Range, COUNT(*) AS Pupils\nFROM     Q1\nGROUP BY Range;"),
    ]
    L["extra"] += [
        X(1, "צרו VIEW בשם `Girls` עם כל התלמידות, והציגו כמה יש.",
          "CREATE VIEW Girls AS\nSELECT * FROM Students WHERE Gender = 'F';\n\nSELECT COUNT(*) AS Girls FROM Girls;"),
        X(2, "צרו VIEW בשם `AbsCount` — מספר ההיעדרויות לכל תלמיד. הציגו שמות התלמידים עם 2 היעדרויות ומעלה.",
          "CREATE VIEW AbsCount AS\nSELECT   StudentId, COUNT(*) AS N\nFROM     Absences\nGROUP BY StudentId;\n\nSELECT S.FirstName, S.LastName, V.N\nFROM   AbsCount V, Students S\nWHERE  V.StudentId = S.StudentId AND V.N >= 2;"),
        X(3, "צרו VIEW בשם `CourseAvg` — הממוצע של כל מקצוע במחצית 1. הציגו את שם המקצוע עם הממוצע הנמוך ביותר.",
          "CREATE VIEW CourseAvg AS\nSELECT   CourseCode, AVG(Grade) AS AvgGrade\nFROM     Grades\nWHERE    Term = 1\nGROUP BY CourseCode;\n\nSELECT C.CourseName, ROUND(V.AvgGrade, 1) AS AvgGrade\nFROM   CourseAvg V, Courses C\nWHERE  V.CourseCode = C.CourseCode\n  AND  V.AvgGrade = (SELECT MIN(AvgGrade) FROM CourseAvg);"),
    ]
    q1 = ("CREATE VIEW Q1 AS\nSELECT   OrderWorker, COUNT(*) AS Orders, SUM(Guests) AS AllGuests\n"
          "FROM     Orders\nGROUP BY OrderWorker;\n\n")
    L["exam_db"] = "cafe"
    L["exam"] = [
        Q(1, "נתונה השאילתה השמורה Q1 (לכל עובד: מספר הזמנות וסך הסועדים). הציגו את כל Q1.",
          q1 + "SELECT * FROM Q1;"),
        Q(2, "בעזרת Q1: שם העובד ומספר ההזמנות שלו.",
          q1 + "SELECT WorkerName, Orders\nFROM   Q1, Workers\nWHERE  OrderWorker = WorkerNum;"),
        Q(2, "בעזרת Q1: העובד ששירת הכי הרבה סועדים (שם).",
          q1 + "SELECT WorkerName, AllGuests\nFROM   Q1, Workers\nWHERE  OrderWorker = WorkerNum\n  AND  AllGuests = (SELECT MAX(AllGuests) FROM Q1);"),
        Q(2, "השלימו את הערך.",
          q1 + "SELECT AVG(Orders) FROM Q1;", kind="value"),
        Q(3, "צרו שאילתה שמורה `DishCount` (לכל מנה כמה פעמים הוזמנה), והציגו את שמות המנות שהוזמנו יותר מפעם אחת.",
          "CREATE VIEW DishCount AS\nSELECT   OrderDish, COUNT(*) AS Times\nFROM     Orders\nGROUP BY OrderDish;\n\nSELECT DishName, Times\nFROM   DishCount, Dishes\nWHERE  OrderDish = DishCode AND Times > 1;"),
        Q(3, "השלימו את הפקודה שיוצרת את Q1.",
          q1 + "SELECT * FROM Q1;", kind="complete",
          given="______ ____ Q1 __\nSELECT   OrderWorker, _____(*) AS Orders, ___(Guests) AS AllGuests\nFROM     Orders\n_____ __ OrderWorker;"),
    ]
