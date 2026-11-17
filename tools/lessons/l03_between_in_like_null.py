from _h import E, P, X

LESSON = dict(
    slug="03-between-in-like-null",
    title="BETWEEN, IN, LIKE ו‑NULL",
    goal="טווח (`BETWEEN`), רשימה (`IN`), חיפוש טקסט (`LIKE`) וערך חסר (`IS NULL`)",
    tables=["Teachers", "Pupils", "Registrations"],
    syntax="""
WHERE HourRate BETWEEN 110 AND 140     -- 110 <= x <= 140   (both ends included!)
WHERE HomeTown IN (1, 3, 4)            -- same as  = 1 OR = 3 OR = 4
WHERE HomeTown NOT IN (1, 3)

WHERE LastName LIKE 'כ%'              -- starts with כ
WHERE LastName LIKE '%ן'              -- ends with ן
WHERE LastName LIKE '%ל%'             -- contains ל
WHERE FirstName LIKE '___'            -- exactly 3 letters   ( _ = one letter )

WHERE TeacherPhone IS NULL            -- empty value
WHERE TeacherPhone IS NOT NULL
""",
    tips=[
        "`BETWEEN` **כולל** את שני הקצוות.",
        "`%` = כל רצף של תווים (גם ריק). `_` = **תו אחד בדיוק**.",
        "⚠️ `= NULL` **לא עובד** ומחזיר 0 שורות. תמיד `IS NULL` / `IS NOT NULL`.",
        "NULL אינו 0 ואינו טקסט ריק — זה **\"אין ערך\"**.",
    ],
    examples=[
        E("מורים שהמחיר שלהם בין 110 ל‑140 (כולל).",
          "SELECT TeacherName, HourRate\nFROM   Teachers\nWHERE  HourRate BETWEEN 110 AND 140;"),
        E("תלמידים שגרים בערים 2 או 4.",
          "SELECT FirstName, HomeTown\nFROM   Pupils\nWHERE  HomeTown IN (2, 4);"),
        E("תלמידים ששם המשפחה שלהם מתחיל ב‑ח.",
          "SELECT FirstName, LastName\nFROM   Pupils\nWHERE  LastName LIKE 'ח%';"),
        E("מורים שאין להם טלפון.",
          "SELECT TeacherName, TeacherPhone\nFROM   Teachers\nWHERE  TeacherPhone IS NULL;"),
    ],
    predict=[
        P("SELECT TeacherName\nFROM   Teachers\nWHERE  TeacherPhone = NULL;", "כמה שורות יחזרו?",
          note="0 שורות! השוואה ל‑NULL עם `=` אף פעם אינה אמת."),
        P("SELECT FirstName\nFROM   Pupils\nWHERE  BirthYear BETWEEN 2010 AND 2012;", "כמה שורות יחזרו?"),
        P("SELECT FirstName\nFROM   Pupils\nWHERE  FirstName LIKE '___';", "אילו שמות יחזרו?"),
    ],
    exercises=[
        X(1, "הציגו תלמידים שנולדו בין 2011 ל‑2013 (כולל).",
          "SELECT FirstName, BirthYear\nFROM   Pupils\nWHERE  BirthYear BETWEEN 2011 AND 2013;"),
        X(1, "הציגו מורים שיש להם טלפון.",
          "SELECT TeacherName, TeacherPhone\nFROM   Teachers\nWHERE  TeacherPhone IS NOT NULL;"),
        X(1, "הציגו רישומים ששולם בהם 300, 320 או 340 לחודש. השתמשו ב‑`IN`.",
          "SELECT RegPupil, MonthlyFee\nFROM   Registrations\nWHERE  MonthlyFee IN (300, 320, 340);"),
        X(1, "הציגו תלמידים ששם המשפחה שלהם מכיל את האות 'ו'.",
          "SELECT FirstName, LastName\nFROM   Pupils\nWHERE  LastName LIKE '%ו%';"),
        X(2, "הציגו תלמידים שלא גרים בערים 1 ו‑2.",
          "SELECT FirstName, HomeTown\nFROM   Pupils\nWHERE  HomeTown NOT IN (1, 2);"),
        X(2, "הציגו מורים ששמם (`TeacherName`) מסתיים באות 'י'.",
          "SELECT TeacherName\nFROM   Teachers\nWHERE  TeacherName LIKE '%י';"),
        X(2, "הציגו תלמידים ששמם הפרטי בן 4 אותיות בדיוק.",
          "SELECT FirstName\nFROM   Pupils\nWHERE  FirstName LIKE '____';"),
        X(2, "הציגו רישומים שהתשלום בהם **לא** בין 300 ל‑350.",
          "SELECT RegPupil, MonthlyFee\nFROM   Registrations\nWHERE  MonthlyFee NOT BETWEEN 300 AND 350;"),
        X(3, "הציגו מורים בלי טלפון שהמחיר שלהם מעל 120.",
          "SELECT TeacherName, HourRate\nFROM   Teachers\nWHERE  TeacherPhone IS NULL AND HourRate > 120;"),
        X(3, "הציגו את שם המורה והטלפון של מורים שהטלפון שלהם מתחיל ב‑050 או ב‑052.",
          "SELECT TeacherName, TeacherPhone\nFROM   Teachers\nWHERE  TeacherPhone LIKE '050%' OR TeacherPhone LIKE '052%';"),
        X(3, "הציגו תלמידים מהערים 1, 3 שנולדו בין 2010 ל‑2012 ושמם הפרטי מכיל 'א'.",
          "SELECT FirstName, BirthYear, HomeTown\nFROM   Pupils\nWHERE  HomeTown IN (1, 3)\n  AND  BirthYear BETWEEN 2010 AND 2012\n  AND  FirstName LIKE '%א%';"),
    ],
    extra=[
        X(1, "הציגו תלמידים שאין להם טלפון.",
          "SELECT FirstName, LastName\nFROM   Students\nWHERE  Phone IS NULL;"),
        X(1, "הציגו ציונים בין 90 ל‑100.",
          "SELECT StudentId, CourseCode, Grade\nFROM   Grades\nWHERE  Grade BETWEEN 90 AND 100;"),
        X(2, "הציגו ציונים חסרים (תלמיד לא נבחן).",
          "SELECT StudentId, CourseCode, Term\nFROM   Grades\nWHERE  Grade IS NULL;"),
        X(2, "הציגו תלמידים שנולדו בשנת 2010 (רמז: `LIKE '2010%'`).",
          "SELECT FirstName, BirthDate\nFROM   Students\nWHERE  BirthDate LIKE '2010%';"),
        X(2, "הציגו מקצועות ששמם מכיל את המילה 'מתמטיקה'.",
          "SELECT CourseName\nFROM   Courses\nWHERE  CourseName LIKE '%מתמטיקה%';"),
        X(3, "הציגו תלמידים שעדיין לא שובצו לכיתה, או שתאריך הלידה שלהם חסר.",
          "SELECT FirstName, ClassCode, BirthDate\nFROM   Students\nWHERE  ClassCode IS NULL OR BirthDate IS NULL;"),
    ],
)
