-- ============================================================
--  בית הקפה "אל-בלד"  ·  בסיס נתונים לבחינת מתכונת (תרגול)
--  הדביקו את כל הקובץ ב-OneCompiler (SQLite), לחצו Run, וכתבו את השאילתות מתחת.
--  לכל שדה בבסיס הנתונים שם ייחודי, ולכן אין צורך בשם הטבלה לפניו.
-- ============================================================
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Dishes;
DROP TABLE IF EXISTS Workers;
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

-- ---------- טבלה ראשית: עובדים ----------
CREATE TABLE Workers (
  WorkerNum    INTEGER PRIMARY KEY,
  WorkerName   TEXT NOT NULL,
  WorkerCity   INTEGER REFERENCES Cities(CityCode),
  StartDate    TEXT NOT NULL,
  HourPay      INTEGER NOT NULL,     -- שכר לשעה בש"ח
  WorkerPhone  TEXT                  -- NULL = לא רשום טלפון
);
INSERT INTO Workers VALUES (1, 'סאלי חדאד',  2, '2022-03-01', 42, '050-1111111');
INSERT INTO Workers VALUES (2, 'יובל נחום',  1, '2023-07-15', 38, NULL);
INSERT INTO Workers VALUES (3, 'אמיר טאהא',  2, '2021-11-10', 50, '054-3333333');
INSERT INTO Workers VALUES (4, 'מיכל שרון',  4, '2024-01-20', 36, '052-4444444');
INSERT INTO Workers VALUES (5, 'רים עבאס',   1, '2020-05-05', 55, NULL);
INSERT INTO Workers VALUES (6, 'תום בראל',   5, '2023-09-01', 38, '053-6666666');

-- ---------- טבלה ראשית: מנות ----------
CREATE TABLE Dishes (
  DishCode   INTEGER PRIMARY KEY,
  DishName   TEXT NOT NULL,
  DishKind   TEXT NOT NULL,
  DishPrice  INTEGER NOT NULL        -- מחיר המנה בש"ח
);
INSERT INTO Dishes VALUES (10, 'חומוס',      'מנה ראשונה', 28);
INSERT INTO Dishes VALUES (20, 'סלט ירקות',  'מנה ראשונה', 32);
INSERT INTO Dishes VALUES (30, 'שניצל',      'מנה עיקרית', 56);
INSERT INTO Dishes VALUES (40, 'פסטה',       'מנה עיקרית', 48);
INSERT INTO Dishes VALUES (50, 'קנאפה',      'קינוח',      30);
INSERT INTO Dishes VALUES (60, 'עוגת גבינה', 'קינוח',      26);
INSERT INTO Dishes VALUES (70, 'לימונדה',    'שתייה',      14);
INSERT INTO Dishes VALUES (80, 'קפה',        'שתייה',      12);

-- ---------- טבלה ראשית: הזמנות ----------
CREATE TABLE Orders (
  OrderNum     INTEGER PRIMARY KEY,
  CustName     TEXT NOT NULL,
  OrderDish    INTEGER REFERENCES Dishes(DishCode),
  OrderWorker  INTEGER REFERENCES Workers(WorkerNum),
  OrderDate    TEXT NOT NULL,
  Guests       INTEGER NOT NULL      -- כמה סועדים ישבו בשולחן
);
INSERT INTO Orders VALUES (101, 'דנה לוי',    30, 1, '2026-02-04',  2);
INSERT INTO Orders VALUES (102, 'עומר חורי',  10, 3, '2026-02-18',  4);
INSERT INTO Orders VALUES (103, 'נועה כץ',    40, 2, '2026-03-05',  3);
INSERT INTO Orders VALUES (104, 'סמיר דיב',   30, 1, '2026-03-22',  6);
INSERT INTO Orders VALUES (105, 'ליאת בר',    50, 4, '2026-04-09',  2);
INSERT INTO Orders VALUES (106, 'ראמי סעיד',  20, 3, '2026-04-27',  5);
INSERT INTO Orders VALUES (107, 'יעל שגיא',   30, 5, '2026-05-11',  2);
INSERT INTO Orders VALUES (108, 'חנאן זועבי', 70, 6, '2026-05-30',  8);
INSERT INTO Orders VALUES (109, 'איתי פלד',   40, 2, '2026-06-14',  3);
INSERT INTO Orders VALUES (110, 'מאיה לוי',   60, 4, '2026-06-28',  4);
INSERT INTO Orders VALUES (111, 'ואיל נסאר',  30, 5, '2026-07-07',  2);
INSERT INTO Orders VALUES (112, 'שני אדרי',   80, 6, '2026-07-21', 10);

SELECT COUNT(*) AS orders_loaded FROM Orders;
