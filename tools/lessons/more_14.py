"""Lesson 14 — more practice + a second full exam on another database."""
from _h import P, Q, X


def extend(L):
    L["predict"] += [
        P("SELECT COUNT(*)\nFROM   ClubMembers\nWHERE  ClubNum IN (SELECT ClubCode FROM Clubs WHERE Sport = 'כדורגל');", "מה המספר?"),
        P("SELECT   Sport, MIN(Price)\nFROM     Clubs\nGROUP BY Sport\nHAVING   COUNT(*) = 2;", "איזו טבלה תתקבל?"),
    ]
    L["exercises"] += [
        X(1, "החברים שהצטרפו בשנת 2025, לפי שם משפחה.",
          "SELECT FirstName, LastName\nFROM   Members\nWHERE  JoinYear = 2025\nORDER BY LastName;"),
        X(2, "לכל עיר (שם): כמה חברים גרים בה, כולל ערים בלי חברים.",
          "SELECT    CityName, COUNT(MemberId) AS Members\nFROM      Cities\nLEFT JOIN Members ON CityCode = TownCode\nGROUP BY  CityName;"),
        X(2, "חברים (שמות) שאינם רשומים לאף חוג כדורגל.",
          "SELECT FirstName, LastName\nFROM   Members\nWHERE  MemberId NOT IN (SELECT MemberNum FROM ClubMembers, Clubs\n                       WHERE  ClubNum = ClubCode AND Sport = 'כדורגל');"),
        X(3, "החוג (או החוגים) עם הכי הרבה חברים.",
          "CREATE VIEW Q1 AS\nSELECT   ClubNum, COUNT(*) AS N\nFROM     ClubMembers\nGROUP BY ClubNum;\n\nSELECT ClubName, N\nFROM   Q1, Clubs\nWHERE  ClubNum = ClubCode AND N = (SELECT MAX(N) FROM Q1);"),
        X(3, "הגיל הממוצע של החברים בכל ענף (`Sport`), מעוגל לספרה אחת.",
          "SELECT   Sport, ROUND(AVG(Age), 1) AS AvgAge\nFROM     Clubs, ClubMembers, Members\nWHERE    ClubCode = ClubNum AND MemberNum = MemberId\nGROUP BY Sport;"),
        X(2, "מחקו את החבר 1012 מכל החוגים.",
          "DELETE FROM ClubMembers\nWHERE  MemberNum = 1012;",
          check="SELECT COUNT(*) AS Left FROM ClubMembers;"),
    ]
    L["extra"] += [
        X(2, "הסופרים שאין להם אף ספר בספרייה.",
          "SELECT AuthorFirstName, AuthorLastName\nFROM   Authors\nWHERE  AuthorCode NOT IN (SELECT WriterCode FROM Books);"),
        X(3, "לכל ז'אנר: מספר ההשאלות (רק ז'אנרים שהושאלו).",
          "SELECT   Genre, COUNT(*) AS Loans\nFROM     Books, Loans\nWHERE    BookCode = BookNum\nGROUP BY Genre;"),
        X(3, "הוסיפו לטבלת ההשאלות עמודה `Fine` (קנס) עם ברירת מחדל 0, ותנו קנס של 20 לכל השאלה שלא הוחזרה.",
          "ALTER TABLE Loans ADD COLUMN Fine INTEGER DEFAULT 0;\nUPDATE Loans SET Fine = 20 WHERE ReturnDate IS NULL;",
          check="SELECT Fine, COUNT(*) AS Loans FROM Loans GROUP BY Fine;"),
    ]
    L["exam_db"] = "repairs"
    L["exam"] = [
        Q(1, "התיקונים שעדיין פתוחים (`DoneDate` ריק), לפי תאריך קבלה.",
          "SELECT RepairNum, CustName, InDate\nFROM   Repairs\nWHERE  DoneDate IS NULL\nORDER BY InDate;"),
        Q(1, "הטכנאים מירכא (לפי שם העיר).",
          "SELECT TechFirst, TechLast\nFROM   Technicians, Cities\nWHERE  TechCity = CityCode AND CityName = 'ירכא';"),
        Q(2, "לכל משפחת מכשירים: מספר התיקונים וסך המחירים.",
          "SELECT   DevFamily, COUNT(*) AS Repairs, SUM(RepairPrice) AS Total\nFROM     Repairs, DevTypes\nWHERE    RepairDev = DevCode\nGROUP BY DevFamily;"),
        Q(2, "", "SELECT DISTINCT TechFirst\nFROM   Technicians, Repairs\nWHERE  TechCode = RepairTech AND Priority = 'דחוף';", kind="output"),
        Q(2, "השלימו את הערכים.",
          "SELECT COUNT(*), SUM(UseQty)\nFROM   PartUsage\nWHERE  UsePart = 101;", kind="value"),
        Q(3, "שם הלקוח, שם החלף ומחיר החלף — לכל חלף שהוחלף בתיקון של מחשב נייד (4 טבלאות).",
          "SELECT CustName, PartName, PartPrice\nFROM   Repairs, PartUsage, Parts, DevTypes\nWHERE  RepairNum = UseRepair AND UsePart = PartCode\n  AND  RepairDev = DevCode AND DevName = 'מחשב נייד';"),
        Q(3, "טכנאים (שמות) שהמחיר הממוצע של התיקונים שלהם גבוה מהממוצע הכללי.",
          "SELECT   TechFirst, TechLast, AVG(RepairPrice) AS AvgPrice\nFROM     Technicians, Repairs\nWHERE    TechCode = RepairTech\nGROUP BY TechCode, TechFirst, TechLast\nHAVING   AVG(RepairPrice) > (SELECT AVG(RepairPrice) FROM Repairs);"),
        Q(2, "סגרו את התיקון 1004: עדכנו את `DoneDate` ל‑'2026-02-20'.",
          "UPDATE Repairs\nSET    DoneDate = '2026-02-20'\nWHERE  RepairNum = 1004;",
          check="SELECT RepairNum, DoneDate FROM Repairs WHERE RepairNum = 1004;"),
        Q(3, "השלימו את הפקודה שמוחקת את החלפים שלא השתמשו בהם אף פעם.",
          "DELETE FROM Parts\nWHERE  PartCode NOT IN (SELECT UsePart FROM PartUsage);", kind="complete",
          check="SELECT PartName FROM Parts;",
          given="______ ____ Parts\nWHERE  PartCode ___ __ (SELECT _______ FROM PartUsage);"),
    ]
