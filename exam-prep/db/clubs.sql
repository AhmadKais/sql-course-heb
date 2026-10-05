-- ============================================================
--  חוגי ספורט עירוניים  ·  בסיס נתונים לבחינה לדוגמה 1
--  הדביקו את כל הקובץ ב-OneCompiler, לחצו Run, וכתבו את השאילתות מתחת.
-- ============================================================
DROP TABLE IF EXISTS ClubMembers;
DROP TABLE IF EXISTS Members;
DROP TABLE IF EXISTS Clubs;
DROP TABLE IF EXISTS Coaches;
DROP TABLE IF EXISTS Cities;

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

CREATE TABLE Coaches (
  CoachCode  INTEGER PRIMARY KEY,
  FirstName  TEXT NOT NULL,
  LastName   TEXT NOT NULL,
  Phone      TEXT                 -- NULL = no phone number
);
INSERT INTO Coaches VALUES (1, 'סאמר', 'חלבי',   '050-1111111');
INSERT INTO Coaches VALUES (2, 'מיכל', 'לוי',    NULL);
INSERT INTO Coaches VALUES (3, 'ראמי', 'עזאם',   '054-3333333');
INSERT INTO Coaches VALUES (4, 'דנה',  'כהן',    '050-4444444');
INSERT INTO Coaches VALUES (5, 'יוסי', 'אברהם',  '053-5555555');

CREATE TABLE Clubs (
  ClubCode   INTEGER PRIMARY KEY,
  ClubName   TEXT NOT NULL,
  Sport      TEXT NOT NULL,
  CoachCode  INTEGER REFERENCES Coaches(CoachCode),
  Price      INTEGER NOT NULL                          -- monthly price in NIS
);
INSERT INTO Clubs VALUES (100, 'כדורגל צעירים',  'כדורגל',  1,    150);
INSERT INTO Clubs VALUES (101, 'כדורגל בוגרים',  'כדורגל',  1,    180);
INSERT INTO Clubs VALUES (102, 'שחייה מתחילים',  'שחייה',   2,    220);
INSERT INTO Clubs VALUES (103, 'שחייה מתקדמים',  'שחייה',   2,    250);
INSERT INTO Clubs VALUES (104, 'כדורסל',         'כדורסל',  3,    160);
INSERT INTO Clubs VALUES (105, 'טניס',           'טניס',    4,    300);
INSERT INTO Clubs VALUES (106, 'ג''ודו',          'ג''ודו',   3,    140);
INSERT INTO Clubs VALUES (107, 'יוגה',           'יוגה',    4,    120);

CREATE TABLE Members (
  Id         INTEGER PRIMARY KEY,
  FirstName  TEXT NOT NULL,
  LastName   TEXT NOT NULL,
  CityCode   INTEGER REFERENCES Cities(CityCode),
  Age        INTEGER,
  JoinYear   INTEGER
);
INSERT INTO Members VALUES (1001, 'אדם',   'חלבי',  1, 14, 2023);
INSERT INTO Members VALUES (1002, 'נור',   'עזאם',  1, 15, 2024);
INSERT INTO Members VALUES (1003, 'יואב',  'כהן',   3, 16, 2022);
INSERT INTO Members VALUES (1004, 'מאיה',  'לוי',   3, 15, 2025);
INSERT INTO Members VALUES (1005, 'רוני',  'אברהם', 2, 13, 2024);
INSERT INTO Members VALUES (1006, 'סאלי',  'חסון',  2, 17, 2023);
INSERT INTO Members VALUES (1007, 'עומר',  'ביטון', 5, 15, 2025);
INSERT INTO Members VALUES (1008, 'שירה',  'כהן',   4, 16, 2022);
INSERT INTO Members VALUES (1009, 'כרים',  'חלבי',  1, 13, 2025);
INSERT INTO Members VALUES (1010, 'תמר',   'שושן',  5, 14, 2023);
INSERT INTO Members VALUES (1011, 'ליאור', 'לוי',   4, 17, 2024);
INSERT INTO Members VALUES (1012, 'ג''וד',  'מנסור', 1, 16, 2025);

CREATE TABLE ClubMembers (
  Id        INTEGER REFERENCES Members(Id),
  ClubCode  INTEGER REFERENCES Clubs(ClubCode),
  PRIMARY KEY (Id, ClubCode)
);
INSERT INTO ClubMembers VALUES (1001, 100);
INSERT INTO ClubMembers VALUES (1001, 104);
INSERT INTO ClubMembers VALUES (1002, 102);
INSERT INTO ClubMembers VALUES (1003, 101);
INSERT INTO ClubMembers VALUES (1003, 105);
INSERT INTO ClubMembers VALUES (1004, 102);
INSERT INTO ClubMembers VALUES (1004, 106);
INSERT INTO ClubMembers VALUES (1005, 100);
INSERT INTO ClubMembers VALUES (1006, 103);
INSERT INTO ClubMembers VALUES (1006, 104);
INSERT INTO ClubMembers VALUES (1007, 100);
INSERT INTO ClubMembers VALUES (1008, 105);
INSERT INTO ClubMembers VALUES (1009, 100);
INSERT INTO ClubMembers VALUES (1009, 106);
INSERT INTO ClubMembers VALUES (1010, 102);
INSERT INTO ClubMembers VALUES (1011, 101);
INSERT INTO ClubMembers VALUES (1011, 104);
INSERT INTO ClubMembers VALUES (1012, 106);

SELECT COUNT(*) AS members_loaded FROM Members;
