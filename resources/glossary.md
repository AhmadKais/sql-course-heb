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
| דרגה | Cardinality | כמה מופעים — אחד או רבים |
| אופציונליות | Optionality | האם חובה — must be / may be |
| אחד לאחד | One‑to‑One (1:1) | |
| אחד לרבים | One‑to‑Many (1:M) | הנפוץ ביותר |
| רבים לרבים | Many‑to‑Many (M:M) | חייב פירוק |
| ישות מקשרת | Intersection Entity | פותרת M:M |
| יחס רקורסיבי | Recursive Relationship | ישות קשורה לעצמה |
| קשת | Arc | יחס בלעדי — "או‑או" |
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

`ACID` · `Anomaly` · `Arc` · `Attribute` · `Barker Notation` · `Business Rule` · `Candidate Key` · `Cardinality` · `Column` · `Composite Attribute` · `Composite Key` · `Conceptual Model` · `Constraint` · `CRUD` · `Crow's Foot` · `Data` · `Database` · `Data Independence` · `Data Integrity` · `Data Model` · `Data Redundancy` · `DBMS` · `DCL` · `DDL` · `Derived Attribute` · `Discriminator` · `DML` · `Entity` · `ERD` · `Exhaustive Rule` · `Foreign Key` · `Hierarchical Model` · `Index` · `Information` · `Inheritance` · `Instance` · `Intersection Entity` · `Knowledge` · `Logical Model` · `Mandatory Attribute` · `Matrix Diagram` · `Multi‑valued Attribute` · `Mutually Exclusive Rule` · `Natural Key` · `Network Model` · `Normalization` · `NULL` · `OLAP` · `OLTP` · `Optionality` · `Optional Attribute` · `Physical Model` · `Primary Key` · `Query` · `Recursive Relationship` · `Redundant Relationship` · `Relational Model` · `Relationship` · `Role` · `Row` · `Schema` · `SDLC` · `SQL` · `Subtype` · `Supertype` · `Surrogate Key` · `Table` · `Transaction` · `UID` · `View` · `Wisdom`

---

<div align="center">

**[🏠 חזרה לדף הקורס](../)**

</div>

</div>
