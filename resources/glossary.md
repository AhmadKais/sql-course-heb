<div dir="rtl">

# 📖 מילון מונחים — עברית ⇄ אנגלית

> מילון מתעדכן. המונחים מסודרים לפי נושא, ובסוף — אינדקס אלפביתי באנגלית.

---

## מושגי יסוד

| עברית | English | הסבר |
|-------|---------|-------|
| נתון | Data | עובדה גולמית, חסרת הקשר |
| מידע | Information | נתון שעבר עיבוד וקיבל משמעות |
| ידע | Knowledge | דפוסים והסברים שמופקים ממידע |
| תבונה | Wisdom | החלטה מושכלת המבוססת על ידע |
| בסיס נתונים | Database | אוסף מאורגן של נתונים קשורים |
| מערכת לניהול בסיס נתונים | DBMS — Database Management System | התוכנה שמנהלת את בסיס הנתונים |
| כפילות נתונים | Data Redundancy | אותו נתון נשמר בכמה מקומות |
| חוסר עקביות | Data Inconsistency | ערכים סותרים לאותה עובדה |
| עצמאות נתונים | Data Independence | ניתוק מבנה האחסון מהתוכניות |
| שלמות נתונים | Data Integrity | תקינות ואמינות הנתונים |
| טרנזקציה | Transaction | רצף פעולות שמתבצע "הכל או כלום" |
| מודל היררכי | Hierarchical Model | מבנה עץ — הורה אחד לכל צומת |
| מודל רשתי | Network Model | מבנה רשת — כמה הורים |
| מודל רלציוני | Relational Model | מבנה טבלאות (Codd, 1970) |

---

## מודל הנתונים

| עברית | English | הסבר |
|-------|---------|-------|
| מודל נתונים | Data Model | ייצוג מובנה של הנתונים והקשרים |
| מודל קונספטואלי | Conceptual Model | "מה קיים בעסק" — ללא טכנולוגיה |
| מודל לוגי | Logical Model | "איך נייצג" — טבלאות ומפתחות |
| מודל פיזי | Physical Model | "איך יאוחסן" — DDL, אינדקסים |
| ישות | Entity | דבר בעל משמעות לעסק שאוספים עליו מידע |
| מופע | Instance / Occurrence | דוגמה בודדת וספציפית של ישות |
| מאפיין | Attribute | פרט מידע יחיד המתאר ישות |
| מאפיין חובה | Mandatory Attribute | מסומן `*` |
| מאפיין רשות | Optional Attribute | מסומן `o` |
| מאפיין מורכב | Composite Attribute | ניתן לפירוק (כתובת) |
| מאפיין רב‑ערכי | Multi‑valued Attribute | כמה ערכים (טלפונים) |
| מאפיין נגזר | Derived Attribute | ניתן לחישוב (גיל) |
| מזהה ייחודי | UID — Unique Identifier | מסומן `#`; הופך ל‑Primary Key |
| מזהה מלאכותי | Surrogate Key | מספר ללא משמעות עסקית |
| מזהה טבעי | Natural Key | מזהה מהעולם האמיתי (ISBN) |
| מזהה מורכב | Composite Key | צירוף כמה מאפיינים |

---

## ERD ויחסים

| עברית | English | הסבר |
|-------|---------|-------|
| תרשים ישויות‑קשרים | ERD — Entity Relationship Diagram | ייצוג ויזואלי של המודל |
| סימון Barker | Barker Notation | הסימון של אורקל ותכנית הלימודים |
| כף עורב | Crow's Foot | סימון "רבים" בקצה קו יחס |
| יחס | Relationship | קשר עסקי בין שתי ישויות |
| עוצמה | Cardinality | כמה מופעים בצד השני — אחד או רבים |
| דרגה | Degree | כמה ישויות משתתפות ביחס — אונרי (1), בינארי (2), טרנרי (3) |
| ⚠️ | — | **אל תבלבלו:** *עוצמה* = כמה מופעים · *דרגה* = כמה ישויות |
| אופציונליות | Optionality | האם חובה — must be / may be |
| אחד לאחד | One‑to‑One (1:1) | |
| אחד לרבים | One‑to‑Many (1:M) | הנפוץ ביותר |
| רבים לרבים | Many‑to‑Many (M:M) | חייב פירוק |
| ישות מקשרת | Intersection Entity | פותרת M:M |
| יחס רקורסיבי | Recursive Relationship | ישות קשורה לעצמה |
| קשת | Arc | יחס בלעדי — "או‑או". ראו הרחבה במודול 7 |
| דיאגרמה מטריציונית | Matrix Diagram | טבלת כל זוגות הישויות |
| קשר מיותר | Redundant Relationship | נגזר דרך ישות שלישית |

---

## טיפוסי משנה וחוקים עסקיים

| עברית | English | הסבר |
|-------|---------|-------|
| טיפוס על | Supertype | ישות כללית עם המאפיינים המשותפים |
| טיפוס משנה | Subtype | תת‑קבוצה עם מאפיינים ייחודיים |
| ירושה | Inheritance | טיפוס משנה יורש מטיפוס העל |
| כלל המיצוי | Exhaustive Rule | כל מופע שייך לטיפוס משנה |
| כלל הבלעדיות | Mutually Exclusive Rule | לטיפוס אחד בדיוק |
| מבחין | Discriminator | השדה שקובע את הסוג |
| תפקיד | Role | מה הישות עושה; יכול להצטבר |
| חוק עסקי | Business Rule | הצהרה שמגבילה היבט בעסק |
| אילוץ | Constraint | מימוש טכני של חוק עסקי |

---

## מונחים רלציוניים (לקראת SQL)

| עברית | English | הסבר |
|-------|---------|-------|
| טבלה | Table | מימוש של ישות |
| שורה / רשומה | Row / Record / Tuple | מימוש של מופע |
| עמודה / שדה | Column / Field | מימוש של מאפיין |
| סכימה | Schema | המבנה הכולל |
| מפתח ראשי | Primary Key (PK) | מזהה ייחודי בטבלה |
| מפתח זר | Foreign Key (FK) | מצביע על PK בטבלה אחרת |
| מפתח מועמד | Candidate Key | מזהה אפשרי נוסף |
| ערך חסר | NULL | היעדר ערך — **לא** אפס ולא מחרוזת ריקה |
| שאילתה | Query | שאלה לבסיס הנתונים |
| נרמול | Normalization | תהליך הקצאת תכונות לישויות |
| אנומליה | Anomaly | בעיה בעדכון/הוספה/מחיקה |
| שאילתה שמורה | View | שאילתה שנשמרת כאובייקט |
| אינדקס | Index | מבנה להאצת חיפוש |

---

## נרמול (מודול 6)

| עברית | English | הסבר |
|-------|---------|-------|
| נרמול | Normalization | תהליך הקצאת תכונות לישויות — כל עובדה במקום אחד בדיוק |
| דה‑נרמול | Denormalization | הכנסת כפילות **במכוון**, בדרך כלל משיקולי ביצועים |
| תלות פונקציונלית | Functional Dependency | `A ⟵ B`: אם ידוע A, אז B ידוע בוודאות |
| תלות טרנזיטיבית / מעבירה | Transitive Dependency | שרשרת `מזהה ⟵ מאפיין ⟵ מאפיין` — אסורה ב‑3NF |
| תלות חלקית | Partial Dependency | מאפיין שתלוי רק בחלק ממזהה מורכב — אסורה ב‑2NF |
| צורה נורמלית ראשונה | First Normal Form (1NF) | ערך אחד בכל תא, ללא קבוצות חוזרות |
| צורה נורמלית שנייה | Second Normal Form (2NF) | אין תלות חלקית — רלוונטית רק למזהה מורכב |
| צורה נורמלית שלישית | Third Normal Form (3NF) | אין תלות טרנזיטיבית |
| חריגת עדכון | Update Anomaly | עובדה כתובה בהרבה שורות; עדכון חלקי יוצר סתירה |
| חריגת הוספה | Insert Anomaly | אי אפשר לרשום דבר בלי דבר אחר |
| חריגת מחיקה | Delete Anomaly | מחיקת שורה מוחקת מידע לא קשור |
| קבוצה חוזרת | Repeating Group | `מוצר_1`, `מוצר_2`, `מוצר_3` — הפרת 1NF |
| ערך אטומי | Atomic Value | ערך יחיד ובלתי מתחלק בתא |
| מזהה מורכב | Composite UID / Key | מזהה שמורכב משתי עמודות או יותר |
| מזהה משני | Secondary UID | מאפיין ייחודי **נוסף** למזהה הראשי; אוכף חוק עסקי |
| מזהה טבעי | Natural Key | מזהה בעל משמעות בעולם האמיתי (ת"ז, מק"ט) |
| שדה מחושב | Derived / Computed Field | ערך הנגזר משדות אחרים — בדרך כלל לא נשמר |
| ערך היסטורי / מוקפא | Historical / Frozen Value | ערך שנקבע ברגע העסקה ואינו משתנה. **אינו כפילות** |

---

## אילוצים (מודול 7)

| עברית | English | הסבר |
|-------|---------|-------|
| אילוץ | Constraint | חוק עסקי שנאכף בבסיס הנתונים — לא רק מתועד |
| תחום | Domain | קבוצת הערכים החוקיים שמאפיין יכול לקבל |
| קשת | Arc | "בדיוק אחד" מבין כמה יחסים היוצאים מאותה ישות |
| שלמות התייחסותית | Referential Integrity | מפתח זר חייב להצביע על שורה קיימת |
| שלמות ישות | Entity Integrity | לכל שורה מזהה ייחודי ומלא |
| אילוץ בדיקה | Check Constraint | תנאי שכל שורה חייבת לקיים |
| כלל מחיקה | Delete Rule | מה קורה לילדים כשמוחקים את ההורה |
| מחיקה מדורגת | Cascade Delete | מחיקת ההורה מוחקת גם את הילדים |
| מניעת מחיקה | Restrict / No Action | המחיקה נדחית כל עוד יש ילדים |
| איפוס הפניה | Set Null | מחיקת ההורה מרוקנת את המפתח הזר |
| טריגר | Trigger | קוד שרץ אוטומטית בבסיס הנתונים בעת שינוי |
| יחס היררכי | Hierarchical Relationship | יחס רקורסיבי 1:M — עץ, לכל צומת הורה אחד |
| שאילתה רקורסיבית | Recursive Query | `CONNECT BY` / `WITH RECURSIVE` — טיול בעץ |
| ישות תקופה | Period / History Entity | ישות עם `start_date` ו‑`end_date` ששומרת מה היה |
| תקופה פתוחה | Open Period | שורה עם `end_date IS NULL` — התקופה הנוכחית |
| מידע היסטורי | Historical Data | תיעוד מה **היה**, לא רק מה **יש** |
| טבלת קוד | Code / Lookup Table | טבלה קטנה של ערכים חוקיים (סטטוסים, סוגים) |

---

## תפקיד היועץ (מודול 8)

| עברית | English | הסבר |
|-------|---------|-------|
| אפקט הפחד | Fear Effect | התנגדות והסתרה של אנשים בארגון מול פרויקט מערכת חדשה |
| בעלי עניין | Stakeholders | כל מי שהמערכת משפיעה עליו — לא רק מי שמזמין אותה |
| יומן החלטות | Decision Log | תיעוד של מה הוחלט, למה, ומי החליט |
| זחילת היקף | Scope Creep | גדילה הדרגתית של הפרויקט דרך בקשות קטנות |
| הצגה חוזרת | Playback | חזרה על מה שהובן, במילות הלקוח, לאימות |
| שאלת הזהב | — | "עם מי עוד כדאי שאדבר?" |
| מסמך חוקים עסקיים | Business Rules Document | כל חוק, איפה נאכף, ומה קורה כשמפרים |
| מילון ישויות | Data Dictionary | הסבר בעברית פשוטה מה כל ישות ומאפיין אומרים |
| רשימת שלב ב' | Phase 2 Backlog | בקשות שנדחו במכוון, מתועדות וגלויות ללקוח |
| מסירה | Handover | חבילת המסמכים שמאפשרת ללקוח להמשיך בלעדיכם |

---

## מעקב אחר שינויים (מודול 10)

| עברית | English | הסבר |
|-------|---------|-------|
| מימד הזמן | Time Dimension | היכולת לענות לא רק "מה יש" אלא "מה היה" |
| זמן תקף | Valid Time | מתי העובדה נכונה **בעולם** |
| זמן רישום | Transaction Time | מתי **המערכת ידעה** על העובדה |
| מודל דו‑זמני | Bitemporal Model | שמירת שני צירי הזמן יחד |
| נקודת זמן | Point in Time | אירוע שקרה בתאריך — עמודה אחת |
| שרשרת אירועים | Event Chain | שורות עם `from` בלבד; כל אחת נגמרת כשהבאה מתחילה |
| יומן ביקורת | Audit Log | טבלה שרושמת כל שינוי: מי, מה, מתי |
| ניהול גרסאות | Versioning | כל שינוי יוצר שורה חדשה שלמה |
| SCD Type 2 | Slowly Changing Dimension | השם התקני של ישות תקופה בעולם מחסני הנתונים |
| מחירון | Price List | מחירים עם `valid_from` / `valid_to` |
| מחיר מוקפא | Frozen / Paid Price | המחיר ששולם בפועל — נעול לנצח |
| בסיס החישוב | Calculation Basis | עמודה שמסבירה **למה** יצא הסכום הזה |
| נעילת מחיר | Price Lock | לקוח שנשאר במחיר שבו נרשם |

---

## ראשי תיבות

| ר"ת | הפירוש | בעברית |
|-----|---------|---------|
| **SQL** | Structured Query Language | שפת שאילתות מובנית |
| **DBMS** | Database Management System | מערכת לניהול בסיס נתונים |
| **RDBMS** | Relational DBMS | DBMS רלציוני |
| **ERD** | Entity Relationship Diagram | תרשים ישויות‑קשרים |
| **UID** | Unique Identifier | מזהה ייחודי |
| **PK / FK** | Primary / Foreign Key | מפתח ראשי / זר |
| **DDL** | Data Definition Language | שפת הגדרת אובייקטים |
| **DML** | Data Manipulation Language | שפת מניפולציית נתונים |
| **DCL** | Data Control Language | שפת בקרת גישה |
| **ACID** | Atomicity, Consistency, Isolation, Durability | ארבע תכונות הטרנזקציה |
| **CRUD** | Create, Read, Update, Delete | ארבע הפעולות הבסיסיות |
| **SDLC** | System Development Life Cycle | מחזור חיי פיתוח מערכת |
| **OLTP** | Online Transaction Processing | מערכת תפעולית |
| **OLAP** | Online Analytical Processing | מערכת ניתוחית |
| **1NF/2NF/3NF** | Normal Forms | צורות נרמול |
| **EAV** | Entity‑Attribute‑Value | מודל גמיש — ⚠️ להימנע |

---

## 🔤 אינדקס אלפביתי (אנגלית)

`ACID` · `Anomaly` · `Arc` · `Attribute` · `Audit Log` · `Barker Notation` · `Bitemporal Model` · `Business Rule` · `Candidate Key` · `Cardinality` · `Cascade Delete` · `Check Constraint` · `Code Table` · `Column` · `Composite Attribute` · `Composite Key` · `Conceptual Model` · `Constraint` · `Crow's Foot` · `CRUD` · `Data` · `Data Dictionary` · `Data Independence` · `Data Integrity` · `Data Model` · `Data Redundancy` · `Database` · `DBMS` · `DCL` · `DDL` · `Decision Log` · `Degree` · `Delete Rule` · `Denormalization` · `Derived Attribute` · `Discriminator` · `DML` · `Domain` · `Entity` · `Entity Integrity` · `ERD` · `Event Chain` · `Exhaustive Rule` · `Fear Effect` · `First Normal Form` · `Foreign Key` · `Frozen Value` · `Functional Dependency` · `Handover` · `Hierarchical Model` · `Hierarchical Relationship` · `Historical Data` · `Index` · `Information` · `Inheritance` · `Instance` · `Intersection Entity` · `Knowledge` · `Logical Model` · `Mandatory Attribute` · `Matrix Diagram` · `Multi‑valued Attribute` · `Mutually Exclusive Rule` · `Natural Key` · `Network Model` · `Normalization` · `NULL` · `OLAP` · `OLTP` · `Open Period` · `Optional Attribute` · `Optionality` · `Partial Dependency` · `Physical Model` · `Playback` · `Point in Time` · `Price List` · `Price Lock` · `Primary Key` · `Query` · `Recursive Query` · `Recursive Relationship` · `Redundant Relationship` · `Referential Integrity` · `Relational Model` · `Relationship` · `Repeating Group` · `Role` · `Row` · `SCD` · `Schema` · `Scope Creep` · `SDLC` · `Second Normal Form` · `Secondary UID` · `Set Null` · `SQL` · `Stakeholders` · `Subtype` · `Supertype` · `Surrogate Key` · `Table` · `Third Normal Form` · `Time Dimension` · `Transaction` · `Transaction Time` · `Transitive Dependency` · `Trigger` · `UID` · `Valid Time` · `Versioning` · `View` · `Wisdom`

---

<div align="center">

**[🏠 חזרה לדף הקורס](../)**

</div>

</div>
