from _h import E, P, X

LESSON = dict(
    slug="14-exam-simulation",
    title="סימולציית בחינה — כל הנושאים",
    goal="תרגול מסכם בסגנון שאלון 735911 על בסיס נתונים חדש: שליפה, קיבוץ, צירוף, תת‑שאילתה, VIEW ושינוי נתונים",
    db="clubs",
    extra_db="library",
    tables=["Cities", "Coaches", "Clubs", "Members", "ClubMembers"],
    syntax="""
-- the checklist for every exam question
-- 1. Which tables hold the columns I need?          -> FROM
-- 2. How are they connected? (FK = PK)              -> WHERE ... = ...
-- 3. Which ROWS?                                    -> WHERE
-- 4. "for each ..."?                                -> GROUP BY
-- 5. condition on COUNT/SUM/AVG?                    -> HAVING
-- 6. "who has NO ..."?                              -> NOT IN (SELECT ...)
-- 7. compare to average / max?                      -> (SELECT AVG(...) FROM ...)
-- 8. order?                                         -> ORDER BY
""",
    tips=[
        "**קודם קוראים את הטבלאות** ומסמנים: 🔑 מפתח ראשי, 🔗 מפתח זר, ואיזו טבלה מקשרת (M:N).",
        "בבחינה כותבים צירוף עם **פסיק + `WHERE`**, וערכי טקסט לפעמים במירכאות כפולות: `\"כדורגל\"`.",
        "סוגי שאלות: איזו טבלה תתקבל · השלמת ערכים · כתיבת שאילתה · מהי השאילתה שהציגה פלט נתון · `UPDATE`/`DELETE`/`ALTER`.",
        "📋 הדפיסו את [דף העזר](../../exam-prep/cheat-sheet.md) — מותר להביא אותו לבחינה.",
    ],
    examples=[
        E("שם החוג ושם המאמן של כל חוג.",
          "SELECT ClubName, CoachFirstName, CoachLastName\nFROM   Clubs, Coaches\nWHERE  TrainerCode = CoachCode;"),
        E("לכל חוג (שם): מספר החברים, כולל חוגים בלי חברים.",
          "SELECT    ClubName, COUNT(MemberNum) AS Members\nFROM      Clubs\nLEFT JOIN ClubMembers ON ClubCode = ClubNum\nGROUP BY  ClubCode, ClubName;"),
        E("מאמנים שאינם מאמנים אף חוג.",
          "SELECT CoachFirstName, CoachLastName\nFROM   Coaches\nWHERE  CoachCode NOT IN (SELECT TrainerCode FROM Clubs);"),
    ],
    predict=[
        P("SELECT DISTINCT Sport\nFROM   Clubs\nWHERE  Price BETWEEN 150 AND 250;", "השלימו: כמה שורות, ואילו ערכים?"),
        P("SELECT   TownCode, COUNT(*) AS N\nFROM     Members\nGROUP BY TownCode\nHAVING   COUNT(*) >= 3;", "איזו טבלה תתקבל?"),
        P("SELECT FirstName\nFROM   Members\nWHERE  MemberId IN (SELECT MemberNum FROM ClubMembers WHERE ClubNum = 106)\n  AND  Age < 16;", "אילו שמות יחזרו?"),
        P("SELECT MAX(Price) - MIN(Price) AS Gap, COUNT(DISTINCT Sport) AS Sports\nFROM   Clubs;", "השלימו את שני הערכים."),
    ],
    exercises=[
        X(1, "הציגו את שמות החברים בני 15 ומטה, ממוינים לפי גיל.",
          "SELECT FirstName, LastName, Age\nFROM   Members\nWHERE  Age <= 15\nORDER BY Age;"),
        X(1, "הציגו את החוגים שהמחיר שלהם בין 140 ל‑200, ושמם מכיל 'כדור'.",
          "SELECT ClubName, Price\nFROM   Clubs\nWHERE  Price BETWEEN 140 AND 200 AND ClubName LIKE '%כדור%';"),
        X(1, "הציגו את המאמנים שאין להם טלפון.",
          "SELECT CoachFirstName, CoachLastName\nFROM   Coaches\nWHERE  Phone IS NULL;"),
        X(2, "הציגו את שם החבר ושם העיר שלו — רק חברים מירכא או מכרמיאל.",
          "SELECT FirstName, LastName, CityName\nFROM   Members, Cities\nWHERE  TownCode = CityCode AND CityName IN ('ירכא', 'כרמיאל');"),
        X(2, "לכל ענף (`Sport`): מספר החוגים והמחיר הממוצע.",
          "SELECT   Sport, COUNT(*) AS Clubs, AVG(Price) AS AvgPrice\nFROM     Clubs\nGROUP BY Sport;"),
        X(2, "הציגו את שמות החברים בחוג 'כדורגל צעירים'.",
          "SELECT FirstName, LastName\nFROM   Members, ClubMembers, Clubs\nWHERE  MemberId = MemberNum AND ClubNum = ClubCode\n  AND  ClubName = 'כדורגל צעירים';"),
        X(2, "חוגים שהמחיר שלהם גבוה מהמחיר הממוצע.",
          "SELECT ClubName, Price\nFROM   Clubs\nWHERE  Price > (SELECT AVG(Price) FROM Clubs);"),
        X(3, "חברים שרשומים ל‑2 חוגים או יותר (שמות), ומה הם משלמים בסך הכול בחודש.",
          "SELECT   FirstName, LastName, COUNT(*) AS Clubs, SUM(Price) AS Total\nFROM     Members, ClubMembers, Clubs\nWHERE    MemberId = MemberNum AND ClubNum = ClubCode\nGROUP BY MemberId, FirstName, LastName\nHAVING   COUNT(*) >= 2;"),
        X(3, "לכל מאמן (שם): כמה חברים הוא מאמן בסך הכול בכל החוגים שלו?",
          "SELECT   CoachFirstName, CoachLastName, COUNT(*) AS Members\nFROM     Coaches, Clubs, ClubMembers\nWHERE    CoachCode = TrainerCode AND ClubCode = ClubNum\nGROUP BY CoachCode, CoachFirstName, CoachLastName;"),
        X(3, "ערים שאף חבר לא גר בהן.",
          "SELECT CityName\nFROM   Cities\nWHERE  CityCode NOT IN (SELECT TownCode FROM Members);"),
        X(3, "נתונה השאילתה השמורה Q1 — סך התשלום החודשי לכל חבר. הציגו את שם החבר שמשלם הכי הרבה.",
          "CREATE VIEW Q1 AS\nSELECT   MemberNum, SUM(Price) AS Total\nFROM     ClubMembers, Clubs\nWHERE    ClubNum = ClubCode\nGROUP BY MemberNum;\n\nSELECT FirstName, LastName, Total\nFROM   Q1, Members\nWHERE  MemberNum = MemberId\n  AND  Total = (SELECT MAX(Total) FROM Q1);"),
        X(2, "העלו ב‑10% את המחיר של כל חוגי השחייה.",
          "UPDATE Clubs\nSET    Price = ROUND(Price * 1.1)\nWHERE  Sport = 'שחייה';",
          check="SELECT ClubName, Price FROM Clubs;"),
        X(2, "מחקו את החוג שאין בו אף חבר.",
          "DELETE FROM Clubs\nWHERE  ClubCode NOT IN (SELECT ClubNum FROM ClubMembers);",
          check="SELECT ClubCode, ClubName FROM Clubs;"),
        X(2, "הוסיפו לטבלת החברים עמודה `Phone` מסוג טקסט.",
          "ALTER TABLE Members ADD COLUMN Phone TEXT;",
          check="SELECT MemberId, FirstName, Phone FROM Members LIMIT 3;"),
    ],
    extra=[
        X(1, "ספרים שיצאו לאור אחרי 2000, ממוינים לפי שנה.",
          "SELECT Title, PubYear\nFROM   Books\nWHERE  PubYear > 2000\nORDER BY PubYear;"),
        X(2, "שם הספר ושם הסופר של כל ספר.",
          "SELECT Title, AuthorFirstName, AuthorLastName\nFROM   Books, Authors\nWHERE  WriterCode = AuthorCode;"),
        X(2, "השאלות שעדיין לא הוחזרו: שם הקורא ושם הספר.",
          "SELECT FirstName, LastName, Title\nFROM   Loans, Members, Books\nWHERE  ReaderId = MemberId AND BookNum = BookCode\n  AND  ReturnDate IS NULL;"),
        X(2, "לכל קורא (שם): כמה ספרים השאיל?",
          "SELECT   FirstName, LastName, COUNT(*) AS Loans\nFROM     Members, Loans\nWHERE    MemberId = ReaderId\nGROUP BY MemberId, FirstName, LastName;"),
        X(3, "ספרים שאף פעם לא הושאלו.",
          "SELECT Title\nFROM   Books\nWHERE  BookCode NOT IN (SELECT BookNum FROM Loans);"),
        X(3, "הספר (או הספרים) עם מספר העמודים הגדול ביותר, ושם הסופר.",
          "SELECT Title, Pages, AuthorLastName\nFROM   Books, Authors\nWHERE  WriterCode = AuthorCode\n  AND  Pages = (SELECT MAX(Pages) FROM Books);"),
    ],
)
