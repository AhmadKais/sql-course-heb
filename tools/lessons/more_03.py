"""Lesson 3 — more practice + exam-style questions."""
from _h import P, Q, X


def extend(L):
    L["predict"] += [
        P("SELECT FirstName\nFROM   Pupils\nWHERE  LastName LIKE '%ן';", "אילו שמות יחזרו?"),
        P("SELECT COUNT(*)\nFROM   Registrations\nWHERE  RegTeacher IN (1, 2, 6);", "מה המספר?",
          note="למורה 6 אין רישומים, אז הוא לא מוסיף כלום."),
    ]
    L["exercises"] += [
        X(1, "הציגו את הכלים ממשפחות 'הקשה' או 'נשיפה' (עם `IN`).",
          "SELECT InstName, InstFamily\nFROM   Instruments\nWHERE  InstFamily IN ('הקשה', 'נשיפה');"),
        X(1, "הציגו מורים שהמחיר שלהם בין 100 ל‑120.",
          "SELECT TeacherName, HourRate\nFROM   Teachers\nWHERE  HourRate BETWEEN 100 AND 120;"),
        X(2, "הציגו תלמידים ששמם הפרטי מתחיל ב‑'ש' או ב‑'ס'.",
          "SELECT FirstName, LastName\nFROM   Pupils\nWHERE  FirstName LIKE 'ש%' OR FirstName LIKE 'ס%';"),
        X(2, "הציגו רישומים משנים 2021–2023 (עם `BETWEEN`).",
          "SELECT RegPupil, RegYear\nFROM   Registrations\nWHERE  RegYear BETWEEN 2021 AND 2023;"),
        X(2, "הציגו מורים ששמם הפרטי (המילה הראשונה) בן 3 אותיות בדיוק (רמז: `'___ %'`).",
          "SELECT TeacherName\nFROM   Teachers\nWHERE  TeacherName LIKE '___ %';"),
        X(3, "הציגו את המורים בלי טלפון, או שהמחיר שלהם לא בין 110 ל‑140.",
          "SELECT TeacherName, HourRate, TeacherPhone\nFROM   Teachers\nWHERE  TeacherPhone IS NULL OR HourRate NOT BETWEEN 110 AND 140;"),
        X(3, "הציגו רישומים של תלמידים 201–205 שאינם ברמת 'מתחיל'.",
          "SELECT RegPupil, PupilLevel\nFROM   Registrations\nWHERE  RegPupil BETWEEN 201 AND 205 AND PupilLevel NOT IN ('מתחיל');"),
    ]
    L["extra"] += [
        X(1, "הציגו כיתות שעדיין לא שובצה להן כיתת אם (`RoomNumber`).",
          "SELECT ClassName\nFROM   Classes\nWHERE  RoomNumber IS NULL;"),
        X(2, "הציגו היעדרויות שלא נמסרה להן סיבה.",
          "SELECT StudentId, AbsenceDate\nFROM   Absences\nWHERE  Reason IS NULL;"),
        X(2, "הציגו מורים שהתחילו לעבוד בין 2015 ל‑2022.",
          "SELECT FirstName, HireDate\nFROM   Teachers\nWHERE  HireDate BETWEEN '2015-01-01' AND '2022-12-31';"),
        X(3, "הציגו תלמידים ששם המשפחה שלהם מכיל '-' או מתחיל ב‑'ח'.",
          "SELECT FirstName, LastName\nFROM   Students\nWHERE  LastName LIKE '%-%' OR LastName LIKE 'ח%';"),
    ]
    L["exam_db"] = "library"
    L["exam"] = [
        Q(1, "הציגו את הספרים שיצאו בין 1990 ל‑2010.",
          "SELECT Title, PubYear\nFROM   Books\nWHERE  PubYear BETWEEN 1990 AND 2010;"),
        Q(1, "הציגו את ההשאלות שעדיין לא הוחזרו.",
          "SELECT LoanId, ReaderId, BookNum\nFROM   Loans\nWHERE  ReturnDate IS NULL;"),
        Q(2, "הציגו את הסופרים מישראל או ממצרים (עם `IN`).",
          "SELECT AuthorFirstName, AuthorLastName\nFROM   Authors\nWHERE  Country IN ('ישראל', 'מצרים');"),
        Q(2, "הציגו ספרים ששמם מכיל את המילה 'הארי'.",
          "SELECT DISTINCT Title\nFROM   Books\nWHERE  Title LIKE '%הארי%';"),
        Q(2, "", "SELECT FirstName, LastName\nFROM   Members\nWHERE  LastName LIKE 'כ%';", kind="output"),
        Q(2, "השלימו את הערכים בטבלה שתתקבל.",
          "SELECT Title\nFROM   Books\nWHERE  Genre = 'מתח' AND Pages BETWEEN 250 AND 300;", kind="value"),
        Q(3, "השלימו כך שיוצגו ההשאלות מאוקטובר 2025 שכבר הוחזרו.",
          "SELECT LoanId\nFROM   Loans\nWHERE  LoanDate LIKE '2025-10%' AND ReturnDate IS NOT NULL;", kind="complete",
          given="SELECT LoanId\nFROM   Loans\nWHERE  LoanDate ____ '2025-10_' AND ReturnDate __ ___ ____;"),
    ]
