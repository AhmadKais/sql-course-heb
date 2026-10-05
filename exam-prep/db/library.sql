-- ============================================================
--  ספרייה עירונית  ·  בסיס נתונים לבחינה לדוגמה 2
--  הדביקו את כל הקובץ ב-OneCompiler, לחצו Run, וכתבו את השאילתות מתחת.
-- ============================================================
DROP TABLE IF EXISTS Loans;
DROP TABLE IF EXISTS Members;
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Authors;
DROP TABLE IF EXISTS Cities;

CREATE TABLE Cities (
  CityCode  INTEGER PRIMARY KEY,
  CityName  TEXT NOT NULL
);
INSERT INTO Cities VALUES (1, 'ירכא');
INSERT INTO Cities VALUES (2, 'כרמיאל');
INSERT INTO Cities VALUES (3, 'עכו');
INSERT INTO Cities VALUES (4, 'מעלות');
INSERT INTO Cities VALUES (5, 'חיפה');

CREATE TABLE Authors (
  AuthorCode  INTEGER PRIMARY KEY,
  FirstName   TEXT NOT NULL,
  LastName    TEXT NOT NULL,
  Country     TEXT
);
INSERT INTO Authors VALUES (1, 'עמוס',  'עוז',     'ישראל');
INSERT INTO Authors VALUES (2, 'ג''ואן', 'רולינג',  'בריטניה');
INSERT INTO Authors VALUES (3, 'נגיב',  'מחפוז',   'מצרים');
INSERT INTO Authors VALUES (4, 'אגתה',  'כריסטי',  'בריטניה');
INSERT INTO Authors VALUES (5, 'דויד',  'גרוסמן',  'ישראל');
INSERT INTO Authors VALUES (6, 'סמי',   'מיכאל',   'ישראל');

CREATE TABLE Books (
  BookCode    INTEGER PRIMARY KEY,
  Title       TEXT NOT NULL,
  AuthorCode  INTEGER REFERENCES Authors(AuthorCode),
  Genre       TEXT,
  PubYear     INTEGER,
  Pages       INTEGER
);
INSERT INTO Books VALUES (201, 'סיפור על אהבה וחושך',     1, 'ביוגרפיה', 2002, 520);
INSERT INTO Books VALUES (202, 'הארי פוטר ואבן החכמים',   2, 'פנטזיה',   1997, 320);
INSERT INTO Books VALUES (203, 'הארי פוטר וחדר הסודות',   2, 'פנטזיה',   1998, 350);
INSERT INTO Books VALUES (204, 'סמטת מדק',               3, 'רומן',     1947, 280);
INSERT INTO Books VALUES (205, 'רצח באוריינט אקספרס',     4, 'מתח',      1934, 250);
INSERT INTO Books VALUES (206, 'ואז לא נשאר אף אחד',      4, 'מתח',      1939, 260);
INSERT INTO Books VALUES (207, 'סוס אחד נכנס לבר',        5, 'רומן',     2014, 200);
INSERT INTO Books VALUES (208, 'אשה בורחת מבשורה',       5, 'רומן',     2008, 640);
INSERT INTO Books VALUES (209, 'מיכאל שלי',              1, 'רומן',     1968, 290);
INSERT INTO Books VALUES (210, 'ספר הדקדוק הפנימי',       5, 'רומן',     1991, 380);

CREATE TABLE Members (
  MemberId   INTEGER PRIMARY KEY,
  FirstName  TEXT NOT NULL,
  LastName   TEXT NOT NULL,
  CityCode   INTEGER REFERENCES Cities(CityCode),
  BirthYear  INTEGER
);
INSERT INTO Members VALUES (501, 'ראניה',  'חלבי',   1, 2008);
INSERT INTO Members VALUES (502, 'עידו',   'כהן',    2, 2007);
INSERT INTO Members VALUES (503, 'מוחמד',  'עזאם',   1, 2009);
INSERT INTO Members VALUES (504, 'נועה',   'לוי',    3, 2008);
INSERT INTO Members VALUES (505, 'אליאס',  'חורי',   3, 2006);
INSERT INTO Members VALUES (506, 'יעל',    'פרץ',    2, 2009);
INSERT INTO Members VALUES (507, 'סאמי',   'קבלאן',  4, 2007);
INSERT INTO Members VALUES (508, 'הילה',   'כהן',    5, 2008);
INSERT INTO Members VALUES (509, 'אמיר',   'חלבי',   1, 2006);
INSERT INTO Members VALUES (510, 'רותם',   'גבאי',   4, 2009);

CREATE TABLE Loans (
  LoanId      INTEGER PRIMARY KEY,
  MemberId    INTEGER REFERENCES Members(MemberId),
  BookCode    INTEGER REFERENCES Books(BookCode),
  LoanDate    TEXT NOT NULL,          -- 'YYYY-MM-DD'
  ReturnDate  TEXT                    -- NULL = not returned yet
);
INSERT INTO Loans VALUES ( 1, 501, 202, '2025-09-01', '2025-09-15');
INSERT INTO Loans VALUES ( 2, 501, 203, '2025-09-16', NULL);
INSERT INTO Loans VALUES ( 3, 502, 205, '2025-09-03', '2025-09-20');
INSERT INTO Loans VALUES ( 4, 503, 202, '2025-09-05', '2025-09-25');
INSERT INTO Loans VALUES ( 5, 504, 207, '2025-09-07', NULL);
INSERT INTO Loans VALUES ( 6, 505, 204, '2025-09-10', '2025-09-30');
INSERT INTO Loans VALUES ( 7, 502, 206, '2025-09-21', NULL);
INSERT INTO Loans VALUES ( 8, 506, 202, '2025-09-26', NULL);
INSERT INTO Loans VALUES ( 9, 507, 209, '2025-10-01', '2025-10-12');
INSERT INTO Loans VALUES (10, 501, 205, '2025-10-02', NULL);
INSERT INTO Loans VALUES (11, 508, 201, '2025-10-03', NULL);
INSERT INTO Loans VALUES (12, 505, 204, '2025-10-05', NULL);
INSERT INTO Loans VALUES (13, 503, 207, '2025-10-06', '2025-10-20');
INSERT INTO Loans VALUES (14, 509, 208, '2025-10-08', NULL);

SELECT COUNT(*) AS loans_loaded FROM Loans;
