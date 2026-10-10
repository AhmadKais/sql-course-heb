-- ============================================================
--  בית הספר "עתיד"  ·  בסיס הנתונים לתרגול בכיתה
--  7 טבלאות · 18 תלמידים · שנת הלימודים 2026/27
--  תאריך הייחוס בכל התרגילים: '2026-09-21'
--
--  הדביקו את כל הקובץ ב-OneCompiler (SQLite), לחצו Run,
--  וכתבו את השאילתות שלכם מתחת לקוד.
-- ============================================================
DROP TABLE IF EXISTS Absences;
DROP TABLE IF EXISTS Grades;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Classes;
DROP TABLE IF EXISTS Teachers;
DROP TABLE IF EXISTS Cities;

-- ---------- ערים ----------
CREATE TABLE Cities (
  CityCode  INTEGER PRIMARY KEY,
  CityName  TEXT NOT NULL
);
INSERT INTO Cities VALUES (1, 'ירכא');
INSERT INTO Cities VALUES (2, 'עכו');
INSERT INTO Cities VALUES (3, 'כרמיאל');
INSERT INTO Cities VALUES (4, 'חיפה');
INSERT INTO Cities VALUES (5, 'נהריה');
INSERT INTO Cities VALUES (6, 'שפרעם');

-- ---------- מורים ----------
CREATE TABLE Teachers (
  TeacherCode  INTEGER PRIMARY KEY,
  FirstName    TEXT    NOT NULL,
  LastName     TEXT    NOT NULL,
  Subject      TEXT    NOT NULL,
  HireDate     TEXT    NOT NULL,
  Salary       INTEGER NOT NULL,                      -- שכר חודשי בש"ח
  CityCode     INTEGER REFERENCES Cities(CityCode),
  Phone        TEXT                                   -- NULL = לא עדכן טלפון
);
INSERT INTO Teachers VALUES (1, 'נביל',  'סרחאן',   'מתמטיקה',  '2012-09-01', 14500, 1, '050-7010101');
INSERT INTO Teachers VALUES (2, 'רונית', 'בר-לב',   'אנגלית',   '2018-09-01', 11200, 4, NULL);
INSERT INTO Teachers VALUES (3, 'חוסאם', 'זיאד',    'מחשבים',   '2021-02-15', 12800, 6, '054-7030303');
INSERT INTO Teachers VALUES (4, 'אורלי', 'שמש',     'היסטוריה', '2009-09-01', 15300, 5, '052-7040404');
INSERT INTO Teachers VALUES (5, 'פאדי',  'חדאד',    'ספורט',    '2023-09-01',  9800, 1, '053-7050505');
INSERT INTO Teachers VALUES (6, 'גלית',  'מזרחי',   'מתמטיקה',  '2016-09-01', 13100, 3, NULL);
INSERT INTO Teachers VALUES (7, 'סמיר',  'אבו-ראס', 'ביולוגיה', '2024-09-01', 10400, 2, '050-7070707');

-- ---------- כיתות ----------
CREATE TABLE Classes (
  ClassCode    INTEGER PRIMARY KEY,
  ClassName    TEXT    NOT NULL,
  Grade        INTEGER NOT NULL,                      -- שכבה: 10 / 11 / 12
  TeacherCode  INTEGER REFERENCES Teachers(TeacherCode),   -- מחנך/ת
  RoomNumber   INTEGER                                -- NULL = טרם שובצה כיתת אם
);
INSERT INTO Classes VALUES (101, 'י1',  10, 1, 12);
INSERT INTO Classes VALUES (102, 'י2',  10, 2, 14);
INSERT INTO Classes VALUES (103, 'יא1', 11, 3, 21);
INSERT INTO Classes VALUES (104, 'יא2', 11, 6, NULL);
INSERT INTO Classes VALUES (105, 'יב1', 12, 4, 31);

-- ---------- מקצועות ----------
CREATE TABLE Courses (
  CourseCode   INTEGER PRIMARY KEY,
  CourseName   TEXT    NOT NULL,
  TeacherCode  INTEGER REFERENCES Teachers(TeacherCode),   -- NULL = טרם נקבע מורה
  WeeklyHours  INTEGER NOT NULL
);
INSERT INTO Courses VALUES (11, 'מתמטיקה 5 יח"ל',     1,    5);
INSERT INTO Courses VALUES (12, 'אנגלית 4 יח"ל',      2,    4);
INSERT INTO Courses VALUES (13, 'מבוא לבסיסי נתונים', 3,    3);
INSERT INTO Courses VALUES (14, 'היסטוריה',           4,    2);
INSERT INTO Courses VALUES (15, 'חינוך גופני',        5,    2);
INSERT INTO Courses VALUES (16, 'מתמטיקה 3 יח"ל',     6,    3);
INSERT INTO Courses VALUES (17, 'סדנת פרויקטים',      NULL, 2);

-- ---------- תלמידים ----------
CREATE TABLE Students (
  StudentId   INTEGER PRIMARY KEY,
  FirstName   TEXT NOT NULL,
  LastName    TEXT NOT NULL,
  ClassCode   INTEGER REFERENCES Classes(ClassCode),   -- NULL = טרם שובץ לכיתה
  Gender      TEXT NOT NULL CHECK (Gender IN ('M','F')),
  BirthDate   TEXT,                                    -- NULL = חסר בתיק
  CityCode    INTEGER REFERENCES Cities(CityCode),
  EnrollDate  TEXT NOT NULL,
  Phone       TEXT                                     -- NULL = אין טלפון נייד
);
INSERT INTO Students VALUES (1001, 'אדם',   'חלבי',  101,  'M', '2011-03-14', 1,    '2026-09-01', '050-1000001');
INSERT INTO Students VALUES (1002, 'נור',   'עזאם',  101,  'F', '2011-07-22', 1,    '2026-09-01', NULL);
INSERT INTO Students VALUES (1003, 'יואב',  'כהן',   101,  'M', '2011-01-09', 3,    '2026-09-01', '052-1000003');
INSERT INTO Students VALUES (1004, 'מאיה',  'לוי',   102,  'F', '2011-11-30', 4,    '2026-09-01', '054-1000004');
INSERT INTO Students VALUES (1005, 'רוני',  'אברהם', 102,  'M', '2011-05-18', 2,    '2026-09-01', NULL);
INSERT INTO Students VALUES (1006, 'סאלי',  'חסון',  102,  'F', NULL,         2,    '2026-09-01', '050-1000006');
INSERT INTO Students VALUES (1007, 'עומר',  'ביטון', 103,  'M', '2010-02-11', 5,    '2025-09-01', '053-1000007');
INSERT INTO Students VALUES (1008, 'שירה',  'כהן',   103,  'F', '2010-09-25', 4,    '2025-09-01', '050-1000008');
INSERT INTO Students VALUES (1009, 'כרים',  'חלבי',  103,  'M', '2010-12-03', 1,    '2025-09-01', NULL);
INSERT INTO Students VALUES (1010, 'תמר',   'שושן',  104,  'F', '2010-04-07', 5,    '2025-09-01', '052-1000010');
INSERT INTO Students VALUES (1011, 'ליאור', 'לוי',   104,  'M', '2010-06-16', NULL, '2025-09-01', '050-1000011');
INSERT INTO Students VALUES (1012, 'ג''וד',  'מנסור', 104,  'F', '2010-08-29', 6,    '2025-09-01', NULL);
INSERT INTO Students VALUES (1013, 'דניאל', 'פרץ',   105,  'M', '2009-01-20', 3,    '2024-09-01', '054-1000013');
INSERT INTO Students VALUES (1014, 'הדיל',  'סעיד',  105,  'F', '2009-10-05', 6,    '2024-09-01', '050-1000014');
INSERT INTO Students VALUES (1015, 'איתי',  'גולן',  105,  'M', '2009-03-27', 4,    '2024-09-01', NULL);
INSERT INTO Students VALUES (1016, 'ראניה', 'עבאס',  105,  'F', '2009-12-12', 6,    '2024-09-01', '053-1000016');
INSERT INTO Students VALUES (1017, 'נועם',  'שחר',   101,  'M', '2011-09-02', 4,    '2026-09-01', '050-1000017');
INSERT INTO Students VALUES (1018, 'לינא',  'חמוד',  NULL, 'F', '2010-10-19', 2,    '2026-09-10', NULL);

-- ---------- ציונים ----------
CREATE TABLE Grades (
  StudentId   INTEGER REFERENCES Students(StudentId),
  CourseCode  INTEGER REFERENCES Courses(CourseCode),
  Term        INTEGER NOT NULL,                        -- מחצית: 1 / 2
  Grade       INTEGER,                                 -- NULL = לא נבחן
  PRIMARY KEY (StudentId, CourseCode, Term)
);
INSERT INTO Grades VALUES (1001, 11, 1,  88);
INSERT INTO Grades VALUES (1001, 12, 1,  74);
INSERT INTO Grades VALUES (1001, 14, 1,  92);
INSERT INTO Grades VALUES (1001, 11, 2,  91);
INSERT INTO Grades VALUES (1002, 11, 1,  95);
INSERT INTO Grades VALUES (1002, 12, 1,  89);
INSERT INTO Grades VALUES (1002, 15, 1, 100);
INSERT INTO Grades VALUES (1003, 16, 1,  61);
INSERT INTO Grades VALUES (1003, 12, 1,  55);
INSERT INTO Grades VALUES (1003, 14, 1,  70);
INSERT INTO Grades VALUES (1003, 16, 2,  67);
INSERT INTO Grades VALUES (1004, 16, 1,  48);
INSERT INTO Grades VALUES (1004, 12, 1,  62);
INSERT INTO Grades VALUES (1004, 14, 1, NULL);
INSERT INTO Grades VALUES (1005, 11, 1,  77);
INSERT INTO Grades VALUES (1005, 12, 1,  81);
INSERT INTO Grades VALUES (1005, 15, 1,  90);
INSERT INTO Grades VALUES (1006, 16, 1,  66);
INSERT INTO Grades VALUES (1006, 12, 1,  58);
INSERT INTO Grades VALUES (1007, 11, 1,  93);
INSERT INTO Grades VALUES (1007, 13, 1,  97);
INSERT INTO Grades VALUES (1007, 12, 1,  85);
INSERT INTO Grades VALUES (1007, 11, 2,  90);
INSERT INTO Grades VALUES (1008, 11, 1,  72);
INSERT INTO Grades VALUES (1008, 13, 1,  79);
INSERT INTO Grades VALUES (1008, 12, 1,  68);
INSERT INTO Grades VALUES (1009, 16, 1,  54);
INSERT INTO Grades VALUES (1009, 13, 1,  63);
INSERT INTO Grades VALUES (1009, 12, 1, NULL);
INSERT INTO Grades VALUES (1010, 11, 1, 100);
INSERT INTO Grades VALUES (1010, 13, 1,  91);
INSERT INTO Grades VALUES (1010, 12, 1,  96);
INSERT INTO Grades VALUES (1010, 11, 2,  97);
INSERT INTO Grades VALUES (1011, 16, 1,  83);
INSERT INTO Grades VALUES (1011, 13, 1,  75);
INSERT INTO Grades VALUES (1011, 12, 1,  80);
INSERT INTO Grades VALUES (1012, 16, 1,  42);
INSERT INTO Grades VALUES (1012, 13, 1,  51);
INSERT INTO Grades VALUES (1012, 12, 1,  47);
INSERT INTO Grades VALUES (1012, 16, 2,  39);
INSERT INTO Grades VALUES (1013, 11, 1,  89);
INSERT INTO Grades VALUES (1013, 13, 1,  94);
INSERT INTO Grades VALUES (1013, 17, 1,  98);
INSERT INTO Grades VALUES (1013, 12, 1,  87);
INSERT INTO Grades VALUES (1013, 11, 2,  92);
INSERT INTO Grades VALUES (1014, 11, 1,  76);
INSERT INTO Grades VALUES (1014, 13, 1,  82);
INSERT INTO Grades VALUES (1014, 17, 1,  90);
INSERT INTO Grades VALUES (1015, 16, 1,  59);
INSERT INTO Grades VALUES (1015, 13, 1,  64);
INSERT INTO Grades VALUES (1015, 17, 1,  71);
INSERT INTO Grades VALUES (1015, 16, 2,  62);
INSERT INTO Grades VALUES (1016, 11, 1,  98);
INSERT INTO Grades VALUES (1016, 13, 1,  99);
INSERT INTO Grades VALUES (1016, 17, 1,  95);
INSERT INTO Grades VALUES (1016, 12, 1,  93);
INSERT INTO Grades VALUES (1016, 11, 2, 100);
INSERT INTO Grades VALUES (1017, 11, 1,  65);
INSERT INTO Grades VALUES (1017, 12, 1,  73);
INSERT INTO Grades VALUES (1017, 14, 1,  69);

-- ---------- היעדרויות ----------
CREATE TABLE Absences (
  AbsenceId    INTEGER PRIMARY KEY,
  StudentId    INTEGER NOT NULL REFERENCES Students(StudentId),
  AbsenceDate  TEXT    NOT NULL,
  Excused      INTEGER NOT NULL CHECK (Excused IN (0,1)),   -- 1 = מאושרת
  Reason       TEXT                                         -- NULL = לא נמסרה סיבה
);
INSERT INTO Absences VALUES (1,  1003, '2026-09-02', 1, 'מחלה');
INSERT INTO Absences VALUES (2,  1003, '2026-09-03', 1, 'מחלה');
INSERT INTO Absences VALUES (3,  1004, '2026-09-07', 0, NULL);
INSERT INTO Absences VALUES (4,  1009, '2026-09-08', 0, NULL);
INSERT INTO Absences VALUES (5,  1009, '2026-09-09', 0, NULL);
INSERT INTO Absences VALUES (6,  1009, '2026-09-14', 1, 'תור לרופא');
INSERT INTO Absences VALUES (7,  1012, '2026-09-02', 0, NULL);
INSERT INTO Absences VALUES (8,  1012, '2026-09-10', 0, NULL);
INSERT INTO Absences VALUES (9,  1012, '2026-09-15', 0, NULL);
INSERT INTO Absences VALUES (10, 1012, '2026-09-16', 0, NULL);
INSERT INTO Absences VALUES (11, 1006, '2026-09-11', 1, 'אירוע משפחתי');
INSERT INTO Absences VALUES (12, 1015, '2026-09-04', 1, 'מחלה');
INSERT INTO Absences VALUES (13, 1015, '2026-09-17', 0, NULL);
INSERT INTO Absences VALUES (14, 1001, '2026-09-18', 1, 'תור לרופא');
INSERT INTO Absences VALUES (15, 1010, '2026-09-08', 1, 'מחלה');
INSERT INTO Absences VALUES (16, 1018, '2026-09-15', 0, NULL);

SELECT COUNT(*) AS students_loaded FROM Students;
