-- ============================================================
--  חנות משחקי מחשב  ·  בסיס נתונים לבחינה לדוגמה 3
--  הדביקו את כל הקובץ ב-OneCompiler, לחצו Run, וכתבו את השאילתות מתחת.
-- ============================================================
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Games;
DROP TABLE IF EXISTS Companies;
DROP TABLE IF EXISTS Categories;

CREATE TABLE Categories (
  CatCode  INTEGER PRIMARY KEY,
  CatName  TEXT NOT NULL
);
INSERT INTO Categories VALUES (1, 'פעולה');
INSERT INTO Categories VALUES (2, 'ספורט');
INSERT INTO Categories VALUES (3, 'אסטרטגיה');
INSERT INTO Categories VALUES (4, 'סימולציה');
INSERT INTO Categories VALUES (5, 'חידות');

CREATE TABLE Companies (
  CompCode  INTEGER PRIMARY KEY,
  CompName  TEXT NOT NULL,
  Country   TEXT
);
INSERT INTO Companies VALUES (10, 'Nintendo',        'Japan');
INSERT INTO Companies VALUES (20, 'Electronic Arts', 'USA');
INSERT INTO Companies VALUES (30, 'Ubisoft',         'France');
INSERT INTO Companies VALUES (40, 'Maxis',           'USA');
INSERT INTO Companies VALUES (50, 'Playtika',        'Israel');

CREATE TABLE Games (
  GameCode      INTEGER PRIMARY KEY,
  GameName      TEXT NOT NULL,
  CatCode       INTEGER REFERENCES Categories(CatCode),
  CompCode      INTEGER REFERENCES Companies(CompCode),
  GameYear      INTEGER,
  PricePerHour  REAL               -- NIS per hour of play
);
INSERT INTO Games VALUES (1, 'Mario Kart',      2, 10, 2017, 6.5);
INSERT INTO Games VALUES (2, 'FIFA',            2, 20, 2021, 8.0);
INSERT INTO Games VALUES (3, 'Assassin''s Creed', 1, 30, 2020, 9.5);
INSERT INTO Games VALUES (4, 'The Sims',        4, 40, 2014, 7.0);
INSERT INTO Games VALUES (5, 'SimCity',         4, 40, 2013, 5.5);
INSERT INTO Games VALUES (6, 'Zelda',           1, 10, 2023, 10.0);
INSERT INTO Games VALUES (7, 'Anno 1800',       3, 30, 2019, 8.5);
INSERT INTO Games VALUES (8, 'NBA Live',        2, 20, 2021, 7.5);
INSERT INTO Games VALUES (9, 'Tetris',          5, NULL, 1984, 3.0);
INSERT INTO Games VALUES (10, 'Just Dance',     2, 30, 2022, 6.0);

CREATE TABLE Users (
  UserId     INTEGER PRIMARY KEY,
  FirstName  TEXT NOT NULL,
  LastName   TEXT NOT NULL,
  Email      TEXT,
  BirthYear  INTEGER
);
INSERT INTO Users VALUES (1, 'רמי',   'חלבי',  'rami@mail.com',  2007);
INSERT INTO Users VALUES (2, 'שני',   'כהן',   'shani@mail.com', 2008);
INSERT INTO Users VALUES (3, 'וליד',  'סעד',   'walid@mail.com', 2006);
INSERT INTO Users VALUES (4, 'אור',   'לוי',   NULL,             2009);
INSERT INTO Users VALUES (5, 'דניאל', 'חורי',  'dani@mail.com',  2007);
INSERT INTO Users VALUES (6, 'מאיה',  'פרץ',   'maya@mail.com',  2008);
INSERT INTO Users VALUES (7, 'נאדר',  'עזאם',  NULL,             2006);

CREATE TABLE Orders (
  OrderId    INTEGER PRIMARY KEY,
  UserId     INTEGER REFERENCES Users(UserId),
  GameCode   INTEGER REFERENCES Games(GameCode),
  OrderDate  TEXT NOT NULL,         -- 'YYYY-MM-DD'
  Hours      INTEGER NOT NULL
);
INSERT INTO Orders VALUES (101, 1, 2, '2025-09-02', 3);
INSERT INTO Orders VALUES (102, 2, 4, '2025-09-05', 5);
INSERT INTO Orders VALUES (103, 1, 6, '2025-09-12', 2);
INSERT INTO Orders VALUES (104, 3, 2, '2025-09-15', 4);
INSERT INTO Orders VALUES (105, 4, 1, '2025-09-19', 1);
INSERT INTO Orders VALUES (106, 2, 1, '2025-09-20', 2);
INSERT INTO Orders VALUES (107, 5, 7, '2025-09-25', 6);
INSERT INTO Orders VALUES (108, 1, 2, '2025-09-30', 2);
INSERT INTO Orders VALUES (109, 6, 3, '2025-10-01', 3);
INSERT INTO Orders VALUES (110, 3, 8, '2025-10-03', 2);
INSERT INTO Orders VALUES (111, 2, 6, '2025-10-04', 4);
INSERT INTO Orders VALUES (112, 5, 2, '2025-10-07', 1);
INSERT INTO Orders VALUES (113, 6, 4, '2025-10-09', 3);

SELECT COUNT(*) AS orders_loaded FROM Orders;
