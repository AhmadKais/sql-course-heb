-- 17 הטבלאות הקטנות של בחינת ה-Moodle, לתרגול בכיתה
-- נוצר אוטומטית על ידי exam-prep/moodle/build.py - אין לערוך ביד
-- כל טבלה עומדת בפני עצמה; אין ביניהן קשרים.

-- פיצריית „נאפולי” – תפריט
DROP TABLE IF EXISTS Pizzas;
CREATE TABLE Pizzas (
  PizzaCode INTEGER,
  PizzaName TEXT,
  Price INTEGER,
  Slices INTEGER
);
INSERT INTO Pizzas (PizzaCode, PizzaName, Price, Slices) VALUES
  (1, 'מרגריטה', 45, 8),
  (2, 'פטריות', 52, 8),
  (3, 'זיתים', 52, 6),
  (4, 'טונה', 60, 8),
  (5, 'ארבע גבינות', 68, 6),
  (6, 'חריפה', 45, 12);

-- חדר כושר „אנרגיה” – מתאמנים
DROP TABLE IF EXISTS Gym;
CREATE TABLE Gym (
  MemberCode INTEGER,
  MemberName TEXT,
  Age INTEGER,
  City TEXT,
  Fee INTEGER
);
INSERT INTO Gym (MemberCode, MemberName, Age, City, Fee) VALUES
  (101, 'נור חדאד', 19, 'חיפה', 120),
  (102, 'עומר לוי', 34, 'עכו', 150),
  (103, 'רים סאלם', 27, 'חיפה', 150),
  (104, 'יואב ברק', 52, 'נהריה', 90),
  (105, 'לינא עודה', 19, 'עכו', 120),
  (106, 'טל אביבי', 41, 'חיפה', 200);

-- קווי אוטובוס – דוח יומי
DROP TABLE IF EXISTS Buses;
CREATE TABLE Buses (
  LineCode INTEGER,
  LineNum TEXT,
  Driver TEXT,
  City TEXT,
  Riders INTEGER
);
INSERT INTO Buses (LineCode, LineNum, Driver, City, Riders) VALUES
  (1, '9', 'אמיר דיאב', 'חיפה', 340),
  (2, '10', 'סמיר חורי', 'עכו', 210),
  (3, '2', 'רונית שחר', 'חיפה', 480),
  (4, '71', 'אמיר דיאב', 'נהריה', 150),
  (5, '33', 'מאיה גל', 'עכו', 480),
  (6, '4', 'פאדי נסאר', 'חיפה', 95);

-- בית מרקחת „הבריאות” – מלאי
DROP TABLE IF EXISTS Pharmacy;
CREATE TABLE Pharmacy (
  DrugCode INTEGER,
  DrugName TEXT,
  Price INTEGER,
  Stock INTEGER
);
INSERT INTO Pharmacy (DrugCode, DrugName, Price, Stock) VALUES
  (11, 'אקמול', 22, 40),
  (12, 'נורופן', 35, 0),
  (13, 'ויטמין C', 48, 12),
  (14, 'סירופ שיעול', 35, 7),
  (15, 'משחת שיניים', 19, 55),
  (16, 'פלסטרים', 14, 0);

-- ספריית העיר – מדף ספרות
DROP TABLE IF EXISTS Library;
CREATE TABLE Library (
  BookCode INTEGER,
  Title TEXT,
  Author TEXT,
  Year INTEGER,
  Copies INTEGER
);
INSERT INTO Library (BookCode, Title, Author, Year, Copies) VALUES
  (1, 'הגמד', 'דוד גרוסמן', 1986, 3),
  (2, 'סוס אחד נכנס', 'דוד גרוסמן', 2014, 5),
  (3, 'החיים כמשל', 'פנחס שדה', 1958, 2),
  (4, 'מישהו לרוץ איתו', 'דוד גרוסמן', 2000, 7),
  (5, 'כחולים', 'נעמי שמר', 1975, 1),
  (6, 'ימי צקלג', 'ס. יזהר', 1958, 2);

-- מאפיית „עתיד” – מוצרים
DROP TABLE IF EXISTS Bakery;
CREATE TABLE Bakery (
  ItemCode INTEGER,
  ItemName TEXT,
  Price INTEGER,
  Calories INTEGER
);
INSERT INTO Bakery (ItemCode, ItemName, Price, Calories) VALUES
  (1, 'קרואסון', 12, 310),
  (2, 'בורקס', 10, 420),
  (3, 'לחם שיפון', 18, 200),
  (4, 'עוגת שוקולד', 45, 520),
  (5, 'מלאווח', 10, 480),
  (6, 'בייגל', 7, 200);

-- השכרת רכב „דרך” – צי הרכבים
DROP TABLE IF EXISTS CarRental;
CREATE TABLE CarRental (
  CarCode INTEGER,
  Model TEXT,
  Year INTEGER,
  DayPrice INTEGER,
  Branch TEXT
);
INSERT INTO CarRental (CarCode, Model, Year, DayPrice, Branch) VALUES
  (1, 'יאריס', 2019, 150, 'חיפה'),
  (2, 'קורולה', 2022, 220, 'עכו'),
  (3, 'פיקנטו', 2019, 130, 'חיפה'),
  (4, 'מאזדה 3', 2023, 260, 'נהריה'),
  (5, 'סוויפט', 2021, 170, 'עכו'),
  (6, 'טרנזיט', 2018, 300, 'חיפה');

-- מרפאה וטרינרית – מטופלים
DROP TABLE IF EXISTS VetClinic;
CREATE TABLE VetClinic (
  PetCode INTEGER,
  PetName TEXT,
  Animal TEXT,
  Age INTEGER,
  OwnerCity TEXT
);
INSERT INTO VetClinic (PetCode, PetName, Animal, Age, OwnerCity) VALUES
  (1, 'לונה', 'כלב', 4, 'חיפה'),
  (2, 'מישמיש', 'חתול', 2, 'עכו'),
  (3, 'רקס', 'כלב', 9, 'חיפה'),
  (4, 'קוקו', 'תוכי', 1, 'נהריה'),
  (5, 'שחורה', 'חתול', 4, 'חיפה'),
  (6, 'בובי', 'כלב', 11, 'עכו');

-- חנות מוזיקה – אלבומים
DROP TABLE IF EXISTS Albums;
CREATE TABLE Albums (
  AlbumCode INTEGER,
  AlbumName TEXT,
  Artist TEXT,
  Year INTEGER,
  Tracks INTEGER
);
INSERT INTO Albums (AlbumCode, AlbumName, Artist, Year, Tracks) VALUES
  (1, 'שבלול', 'אריק איינשטיין', 1970, 12),
  (2, 'בדרך לתל אביב', 'משינה', 1988, 10),
  (3, 'ילדות', 'כוורת', 1974, 12),
  (4, 'אהבתי', 'שרית חדד', 2002, 14),
  (5, 'פוגה', 'אתניקס', 1988, 9),
  (6, 'סוף העולם', 'מוניקה סקס', 1995, 10);

-- חנות פרחים „גן עדן”
DROP TABLE IF EXISTS Flowers;
CREATE TABLE Flowers (
  FlowerCode INTEGER,
  FlowerName TEXT,
  Price INTEGER,
  Color TEXT
);
INSERT INTO Flowers (FlowerCode, FlowerName, Price, Color) VALUES
  (1, 'ורד', 15, 'אדום'),
  (2, 'חמנייה', 12, 'צהוב'),
  (3, 'צבעוני', 20, 'אדום'),
  (4, 'סחלב', 65, 'לבן'),
  (5, 'חרצית', 8, 'צהוב'),
  (6, 'לילך', 20, 'סגול');

-- חנות סלולר – מכשירים
DROP TABLE IF EXISTS Phones;
CREATE TABLE Phones (
  PhoneCode INTEGER,
  Model TEXT,
  Brand TEXT,
  Price INTEGER,
  Storage INTEGER
);
INSERT INTO Phones (PhoneCode, Model, Brand, Price, Storage) VALUES
  (1, 'גלקסי A54', 'סמסונג', 1200, 128),
  (2, 'אייפון 13', 'אפל', 2800, 128),
  (3, 'רדמי נוט', 'שיאומי', 900, 256),
  (4, 'גלקסי S23', 'סמסונג', 3400, 256),
  (5, 'אייפון SE', 'אפל', 1800, 64),
  (6, 'נוקיה G22', 'נוקיה', 700, 64);

-- ליגת כדורסל – שחקנים
DROP TABLE IF EXISTS Players;
CREATE TABLE Players (
  PlayerCode INTEGER,
  PlayerName TEXT,
  Team TEXT,
  Points INTEGER,
  Height INTEGER
);
INSERT INTO Players (PlayerCode, PlayerName, Team, Points, Height) VALUES
  (1, 'עלי זועבי', 'הפועל חיפה', 18, 191),
  (2, 'דן אוחיון', 'מכבי עכו', 24, 205),
  (3, 'יוסף טהא', 'הפועל חיפה', 24, 188),
  (4, 'רון סלע', 'מכבי עכו', 11, 197),
  (5, 'כרים דאוד', 'בני נהריה', 31, 201),
  (6, 'איתי גור', 'בני נהריה', 18, 188);

-- מדריך מסעדות – דירוגים
DROP TABLE IF EXISTS Restaurants;
CREATE TABLE Restaurants (
  RestCode INTEGER,
  RestName TEXT,
  City TEXT,
  Rating INTEGER,
  Seats INTEGER
);
INSERT INTO Restaurants (RestCode, RestName, City, Rating, Seats) VALUES
  (1, 'אל-בלד', 'עכו', 5, 60),
  (2, 'הדייג', 'חיפה', 4, 120),
  (3, 'פטיסרי', 'חיפה', 5, 35),
  (4, 'אבו כריסטו', 'עכו', 4, 80),
  (5, 'המטבח', 'נהריה', 3, 50),
  (6, 'ליבנה', 'חיפה', 3, 35);

-- מערכת שעות – קורסים
DROP TABLE IF EXISTS Courses;
CREATE TABLE Courses (
  CourseCode INTEGER,
  CourseName TEXT,
  Teacher TEXT,
  Hours INTEGER,
  Students INTEGER
);
INSERT INTO Courses (CourseCode, CourseName, Teacher, Hours, Students) VALUES
  (1, 'בסיסי נתונים', 'אחמד קיס', 4, 28),
  (2, 'אלגברה', 'מרים דאנא', 5, 31),
  (3, 'פיזיקה', 'יוסי אלון', 3, 22),
  (4, 'תכנות', 'אחמד קיס', 6, 28),
  (5, 'כימיה', 'מרים דאנא', 3, 19),
  (6, 'היסטוריה', 'נדיה חלבי', 2, 35);

-- חברת „אופק” – עובדים
DROP TABLE IF EXISTS Workers;
CREATE TABLE Workers (
  WorkerCode INTEGER,
  WorkerName TEXT,
  Phone TEXT,
  Salary INTEGER,
  City TEXT
);
INSERT INTO Workers (WorkerCode, WorkerName, Phone, Salary, City) VALUES
  (1, 'סאמר נאסר', '0501111111', 9000, 'חיפה'),
  (2, 'גלית אורן', NULL, 12000, 'עכו'),
  (3, 'פאדי חורי', '0523333333', 9000, 'חיפה'),
  (4, 'תמר ניר', NULL, 7500, 'נהריה'),
  (5, 'מוחמד זיאד', '0545555555', 15000, 'עכו'),
  (6, 'אורי שגב', '0506666666', NULL, 'חיפה');

-- בית ספר – ציוני מחצית
DROP TABLE IF EXISTS Students;
CREATE TABLE Students (
  StudentCode INTEGER,
  StudentName TEXT,
  Grade INTEGER,
  ClassName TEXT
);
INSERT INTO Students (StudentCode, StudentName, Grade, ClassName) VALUES
  (1, 'אמל חדיד', 92, 'י1'),
  (2, 'נועם פרץ', NULL, 'י2'),
  (3, 'סלמא עוויסאת', 78, 'י1'),
  (4, 'דור כהן', 92, 'י3'),
  (5, 'ראמי שאהין', NULL, 'י2'),
  (6, 'שירה מלכה', 55, 'י3');

-- ארוניות בבית הספר
DROP TABLE IF EXISTS Lockers;
CREATE TABLE Lockers (
  LockerId INTEGER,
  LockerNum TEXT,
  Owner TEXT,
  Floor INTEGER
);
INSERT INTO Lockers (LockerId, LockerNum, Owner, Floor) VALUES
  (1, '7', 'נור עבאס', 1),
  (2, '10', 'יונתן הר', 2),
  (3, '9', 'מאיה דרור', 1),
  (4, '100', 'אחמד סרור', 3),
  (5, '25', 'רותם בן חיים', 2),
  (6, '3', 'ליאן פארס', 1);

-- בדיקת טעינה: אמור להחזיר 17
SELECT COUNT(*) AS tables_loaded FROM sqlite_master WHERE type = 'table';
