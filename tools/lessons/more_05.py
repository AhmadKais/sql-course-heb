"""Lesson 5 — more practice + exam-style questions."""
from _h import P, Q, X


def extend(L):
    L["predict"] += [
        P("SELECT LENGTH('פסנתר'), SUBSTR('050-1234567', 5, 3);", "מה שני הערכים?"),
        P("SELECT InstName,\n       CASE WHEN InstFamily = 'מיתר' THEN 'כן' ELSE 'לא' END AS Strings\nFROM   Instruments;",
          "כמה פעמים יופיע 'כן'?"),
    ]
    L["exercises"] += [
        X(1, "הציגו לכל מורה את שמו ואת המחיר ל‑90 דקות (שעה וחצי), בשם `Lesson90`.",
          "SELECT TeacherName, HourRate * 1.5 AS Lesson90\nFROM   Teachers;"),
        X(1, "הציגו את שם הכלי ואת משפחתו בעמודה אחת, למשל `פסנתר (קלידים)`.",
          "SELECT InstName || ' (' || InstFamily || ')' AS Instrument\nFROM   Instruments;"),
        X(2, "הציגו את 3 הספרות האחרונות של הטלפון של כל מורה (רמז: `SUBSTR(TeacherPhone, -3)`).",
          "SELECT TeacherName, SUBSTR(TeacherPhone, -3) AS Last3\nFROM   Teachers\nWHERE  TeacherPhone IS NOT NULL;"),
        X(2, "הציגו לכל רישום את התשלום החודשי כולל מע\"מ 18%, מעוגל לשקל, בשם `WithVat`.",
          "SELECT RegPupil, ROUND(MonthlyFee * 1.18) AS WithVat\nFROM   Registrations;"),
        X(2, "הציגו לכל תלמיד את שמו ואת מספר האותיות בשם המלא (בלי רווח), בשם `Letters`.",
          "SELECT FirstName, LastName, LENGTH(FirstName) + LENGTH(LastName) AS Letters\nFROM   Pupils;"),
        X(3, "הציגו לכל לוקר: 'קרקע' לקומה 1, 'עליונה' לקומה 2.",
          "SELECT LockerNum,\n       CASE LockerFloor WHEN 1 THEN 'קרקע' ELSE 'עליונה' END AS FloorName\nFROM   Lockers;"),
        X(3, "הציגו לכל רישום את קוד התלמיד ו'ותיק' אם נרשם לפני 2024, 'חדש' אם ב‑2024, ו'חדש מאוד' אם ב‑2025.",
          "SELECT RegPupil, RegYear,\n       CASE\n         WHEN RegYear < 2024 THEN 'ותיק'\n         WHEN RegYear = 2024 THEN 'חדש'\n         ELSE 'חדש מאוד'\n       END AS Seniority\nFROM   Registrations;"),
    ]
    L["extra"] += [
        X(1, "הציגו לכל מורה את השכר אחרי העלאה של 3%, מעוגל לשקל.",
          "SELECT FirstName, ROUND(Salary * 1.03) AS NewSalary\nFROM   Teachers;"),
        X(2, "הציגו לכל תלמיד את חודש הלידה בלבד (תווים 6–7 של `BirthDate`).",
          "SELECT FirstName, SUBSTR(BirthDate, 6, 2) AS BirthMonth\nFROM   Students\nWHERE  BirthDate IS NOT NULL;"),
        X(2, "הציגו לכל כיתה את שמה ואת מספר החדר, ו'אין חדר' כשהוא חסר.",
          "SELECT ClassName, IFNULL(RoomNumber, 'אין חדר') AS Room\nFROM   Classes;"),
        X(3, "הציגו לכל היעדרות 'מאושרת' או 'לא מאושרת' לפי `Excused`.",
          "SELECT StudentId, AbsenceDate,\n       CASE Excused WHEN 1 THEN 'מאושרת' ELSE 'לא מאושרת' END AS Status\nFROM   Absences;"),
    ]
    L["exam_db"] = "cafe"
    L["exam"] = [
        Q(1, "הציגו לכל מנה את שמה ואת המחיר אחרי הנחה של 10%, בשם `Sale`.",
          "SELECT DishName, DishPrice * 0.9 AS Sale\nFROM   Dishes;"),
        Q(1, "הציגו לכל הזמנה את שם הלקוח ואת אורך השם.",
          "SELECT CustName, LENGTH(CustName) AS NameLen\nFROM   Orders;"),
        Q(2, "הציגו לכל עובד את שמו ואת הטלפון, ובמקום NULL — 'אין'.",
          "SELECT WorkerName, IFNULL(WorkerPhone, 'אין') AS Phone\nFROM   Workers;"),
        Q(2, "הציגו לכל עובד את שמו ואת שנת תחילת העבודה בלבד.",
          "SELECT WorkerName, SUBSTR(StartDate, 1, 4) AS StartYear\nFROM   Workers;"),
        Q(2, "השלימו את הערכים בטבלה שתתקבל.",
          "SELECT DishName,\n       CASE WHEN DishPrice >= 30 THEN 'יקר' ELSE 'זול' END AS Level\nFROM   Dishes\nWHERE  DishKind = 'מנה ראשונה';", kind="value"),
        Q(3, "", "SELECT DishName, DishPrice * 2 AS TwoDishes\nFROM   Dishes\nWHERE  DishKind = 'שתייה';", kind="output"),
        Q(3, "השלימו כך שיוצג לכל עובד שכר יומי (8 שעות) מעוגל, בשם `DayPay`.",
          "SELECT WorkerName, ROUND(HourPay * 8) AS DayPay\nFROM   Workers;", kind="complete",
          given="SELECT WorkerName, _____(HourPay * _) AS ______\nFROM   _______;"),
    ]
