-- ============================================================
--  מעבדת "דלתא-טק"  ·  בסיס נתונים לבחינת אמצע (SELECT · WHERE · ORDER BY)
--  הדביקו את כל הקובץ ב-OneCompiler (SQLite), לחצו Run, וכתבו את השאילתות מתחת.
--  לכל שדה בבסיס הנתונים שם ייחודי, ולכן אין צורך בשם הטבלה לפניו.
-- ============================================================
DROP TABLE IF EXISTS PartUsage;
DROP TABLE IF EXISTS Benches;
DROP TABLE IF EXISTS Repairs;
DROP TABLE IF EXISTS Parts;
DROP TABLE IF EXISTS Technicians;
DROP TABLE IF EXISTS DevTypes;
DROP TABLE IF EXISTS Cities;

-- ---------- טבלת עזר: ערים ----------
CREATE TABLE Cities (
  CityCode  INTEGER PRIMARY KEY,
  CityName  TEXT NOT NULL
);
INSERT INTO Cities VALUES (1, 'ירכא');
INSERT INTO Cities VALUES (2, 'עכו');
INSERT INTO Cities VALUES (3, 'כרמיאל');
INSERT INTO Cities VALUES (4, 'נהריה');
INSERT INTO Cities VALUES (5, 'שפרעם');
INSERT INTO Cities VALUES (6, 'מעלות');

-- ---------- טבלת עזר: סוגי מכשירים ----------
CREATE TABLE DevTypes (
  DevCode    INTEGER PRIMARY KEY,
  DevName    TEXT NOT NULL,
  DevFamily  TEXT NOT NULL
);
INSERT INTO DevTypes VALUES (10, 'טלפון חכם',    'סלולר');
INSERT INTO DevTypes VALUES (20, 'מחשב נייד',    'מחשבים');
INSERT INTO DevTypes VALUES (30, 'טאבלט',        'סלולר');
INSERT INTO DevTypes VALUES (40, 'שעון חכם',     'לבישים');
INSERT INTO DevTypes VALUES (50, 'אוזניות',      'לבישים');
INSERT INTO DevTypes VALUES (60, 'קונסולת משחק', 'מחשבים');

-- ---------- טבלת עזר: חלפים ----------
CREATE TABLE Parts (
  PartCode   INTEGER PRIMARY KEY,
  PartName   TEXT NOT NULL,
  PartPrice  INTEGER NOT NULL        -- מחיר החלף בש"ח
);
INSERT INTO Parts VALUES (101, 'מסך',        450);
INSERT INTO Parts VALUES (102, 'סוללה',      180);
INSERT INTO Parts VALUES (103, 'שקע טעינה',   90);
INSERT INTO Parts VALUES (104, 'רמקול',       70);
INSERT INTO Parts VALUES (105, 'מקלדת',      220);
INSERT INTO Parts VALUES (106, 'מצלמה',      160);
INSERT INTO Parts VALUES (107, 'כבל שטוח',    45);

-- ---------- טבלה ראשית: טכנאים ----------
CREATE TABLE Technicians (
  TechCode   INTEGER PRIMARY KEY,
  TechFirst  TEXT NOT NULL,
  TechLast   TEXT NOT NULL,
  TechCity   INTEGER REFERENCES Cities(CityCode),
  StartDate  TEXT NOT NULL,
  HourWage   INTEGER NOT NULL,       -- שכר לשעה בש"ח
  TechPhone  TEXT                    -- NULL = לא רשום טלפון
);
INSERT INTO Technicians VALUES (1, 'נביל',  'סרחאן',  1, '2019-03-01',  95, '050-7010101');
INSERT INTO Technicians VALUES (2, 'רונית', 'בר-לב',  4, '2021-09-15',  80, NULL);
INSERT INTO Technicians VALUES (3, 'חוסאם', 'זיאד',   5, '2020-01-12',  88, '054-7030303');
INSERT INTO Technicians VALUES (4, 'דנה',   'כהן',    1, '2023-06-01',  72, '052-7040404');
INSERT INTO Technicians VALUES (5, 'סאמר',  'חלבי',   1, '2018-11-20', 105, NULL);
INSERT INTO Technicians VALUES (6, 'מאיה',  'אברהם',  6, '2024-02-10',  65, '053-7060606');
INSERT INTO Technicians VALUES (7, 'ליאן',  'קבלאן',  2, '2022-05-05',  80, '050-7070707');

-- ---------- טבלה ראשית: תיקונים ----------
CREATE TABLE Repairs (
  RepairNum    INTEGER PRIMARY KEY,
  CustName     TEXT NOT NULL,
  RepairDev    INTEGER REFERENCES DevTypes(DevCode),
  RepairTech   INTEGER REFERENCES Technicians(TechCode),
  InDate       TEXT NOT NULL,        -- תאריך קבלת המכשיר
  DoneDate     TEXT,                 -- NULL = התיקון עדיין פתוח
  RepairPrice  INTEGER NOT NULL,     -- מחיר התיקון בש"ח
  Priority     TEXT NOT NULL         -- רגיל / דחוף / מיידי
);
INSERT INTO Repairs VALUES (1001, 'אדם חלבי',   10, 1, '2026-01-12', '2026-01-15',  420, 'רגיל');
INSERT INTO Repairs VALUES (1002, 'מאיה כהן',   20, 3, '2026-01-20', '2026-02-02',  980, 'דחוף');
INSERT INTO Repairs VALUES (1003, 'כרים עזאם',  10, 2, '2026-02-03', '2026-02-05',  310, 'רגיל');
INSERT INTO Repairs VALUES (1004, 'שירה לוי',   30, 1, '2026-02-14', NULL,          540, 'דחוף');
INSERT INTO Repairs VALUES (1005, 'רמי חורי',   60, 5, '2026-03-02', '2026-03-09',  760, 'רגיל');
INSERT INTO Repairs VALUES (1006, 'תמר אברהם',  40, 4, '2026-03-11', '2026-03-12',  190, 'מיידי');
INSERT INTO Repairs VALUES (1007, 'ליאן קבלאן', 10, 7, '2026-03-25', '2026-04-01',  450, 'רגיל');
INSERT INTO Repairs VALUES (1008, 'עומר ביטון', 20, 3, '2026-04-05', NULL,         1250, 'דחוף');
INSERT INTO Repairs VALUES (1009, 'סאלי חסון',  50, 6, '2026-04-18', '2026-04-19',  120, 'רגיל');
INSERT INTO Repairs VALUES (1010, 'יואב שושן',  10, 1, '2026-05-02', '2026-05-06',  380, 'מיידי');
INSERT INTO Repairs VALUES (1011, 'נור מנסור',  30, 2, '2026-05-15', '2026-05-20',  610, 'רגיל');
INSERT INTO Repairs VALUES (1012, 'אלון כהן',   20, 5, '2026-06-01', '2026-06-14', 1480, 'דחוף');
INSERT INTO Repairs VALUES (1013, 'סלים דיאב',  10, 7, '2026-06-22', '2026-06-24',  290, 'רגיל');
INSERT INTO Repairs VALUES (1014, 'הילה פרץ',   60, 4, '2026-07-03', NULL,          820, 'רגיל');
INSERT INTO Repairs VALUES (1015, 'מוחמד דיב',  40, 6, '2026-07-19', '2026-07-21',  230, 'מיידי');
INSERT INTO Repairs VALUES (1016, 'אורי שמש',   20, 3, '2026-08-04', '2026-08-20', 1100, 'דחוף');

-- ---------- קשר 1:1 — לכל טכנאי עמדת עבודה אחת לכל היותר ----------
CREATE TABLE Benches (
  BenchNum    INTEGER PRIMARY KEY,
  BenchTech   INTEGER UNIQUE REFERENCES Technicians(TechCode),
  BenchFloor  INTEGER NOT NULL
);
INSERT INTO Benches VALUES (1, 1, 1);
INSERT INTO Benches VALUES (2, 3, 1);
INSERT INTO Benches VALUES (3, 5, 2);
INSERT INTO Benches VALUES (4, 7, 2);
INSERT INTO Benches VALUES (5, 4, 2);

-- ---------- טבלה מקשרת M:N — אילו חלפים נכנסו לאיזה תיקון ----------
CREATE TABLE PartUsage (
  UseRepair  INTEGER REFERENCES Repairs(RepairNum),
  UsePart    INTEGER REFERENCES Parts(PartCode),
  UseQty     INTEGER NOT NULL,
  PRIMARY KEY (UseRepair, UsePart)
);
INSERT INTO PartUsage VALUES (1001, 102, 1);
INSERT INTO PartUsage VALUES (1002, 105, 1);
INSERT INTO PartUsage VALUES (1002, 102, 1);
INSERT INTO PartUsage VALUES (1003, 101, 1);
INSERT INTO PartUsage VALUES (1004, 101, 1);
INSERT INTO PartUsage VALUES (1005, 104, 2);
INSERT INTO PartUsage VALUES (1007, 103, 1);
INSERT INTO PartUsage VALUES (1008, 101, 1);
INSERT INTO PartUsage VALUES (1008, 105, 1);
INSERT INTO PartUsage VALUES (1010, 102, 1);
INSERT INTO PartUsage VALUES (1011, 101, 1);
INSERT INTO PartUsage VALUES (1012, 105, 1);
INSERT INTO PartUsage VALUES (1012, 102, 1);
INSERT INTO PartUsage VALUES (1016, 101, 1);
INSERT INTO PartUsage VALUES (1016, 106, 1);

SELECT COUNT(*) AS repairs_loaded FROM Repairs;
