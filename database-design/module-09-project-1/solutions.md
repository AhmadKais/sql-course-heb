<div dir="rtl">

# מודול 9 — פתרון הייחוס

> ⚠️ **עצרו.** אם אין לכם ERD מלא משלכם — [חזרו לפרויקט](exercises.md).
>
> 📌 **וזכרו:** זהו **פתרון ייחוס**, לא "התשובה". מודל שונה משלכם יכול להיות נכון לחלוטין —
> **אם הוא מנומק, ואם הוא עונה על שלוש השאלות של רותי.** בדקו את ההנמקה, לא את ההתאמה.

---

## ✅ שלב 1 — חילוץ

### א. שמות עצם והכרעתם (מדגם מייצג)

</div>

```text
CERTAIN ENTITIES                 ATTRIBUTES              VALUES / NOT RELEVANT
----------------                 ----------              ---------------------
Animal      ANIMAL               name                    "brown"   <- a value
Species     SPECIES              colour                  "20-30 calls" <- a metric
Breed       BREED                estimated age           "13 years" <- background
Intake      INTAKE               chip number             Instagram <- out of scope
Kennel      LOCATION             date                    matriculation <- out of scope
Wing        -> LOCATION          amount
Building    -> LOCATION          address
Person      PERSON               phone number
Volunteer   -> a ROLE            surrender reason
Adopter     -> a ROLE            condition at intake
Vet         -> a ROLE
Vet visit   VET_VISIT            (!) NOTE these are NOT entities:
Exam        VET_EXAM               "quarantine" <- a STATE, not an entity
Vaccination VACCINATION            "wing"       <- a LEVEL inside LOCATION
Vaccine type VACCINE_TYPE          "volunteer"  <- a ROLE of PERSON
Protocol    VACCINE_PROTOCOL       "form"       <- = ADOPTION_APPLICATION
Application ADOPTION_APPLICATION   "contract"   <- a document OF adoption
Interview   INTERVIEW              "medical file" <- a VIEW, not an entity
Adoption    ADOPTION
Home visit  HOME_VISIT
Return      RETURN  <- *
Expense     EXPENSE
Expense cat. EXPENSE_CATEGORY
Trait       TRAIT  <- **
Shift       SHIFT
Daily log   DAILY_LOG  <- *
Foster      FOSTER  <- *** (only from Noa!)
```

<div dir="rtl">

### ב. שישה "בדרך כלל" והחוקים שמאחוריהם

| # | מה שנאמר | החוק העסקי שהתגלה |
|---|-----------|---------------------|
| 1 | "**בדרך כלל** אחת בכלוב" | כלוב מכיל בדרך כלל חיה אחת ⟵ **1:M, לא 1:1** |
| 2 | "**חוץ מ**גורים — אמא וגורים ביחד" | מותר כמה חיות בכלוב, בתנאי קרבה משפחתית |
| 3 | "**לפעמים** שני חתולים שהגיעו ביחד" | חוק "הגיעו יחד" — עוד חריג לקיבולת |
| 4 | "**לפעמים** אחרי שלושה חודשים עוד ביקורת" | `HOME_VISIT` הוא **1:M**, לא 1:1 |
| 5 | "**בדרך כלל** שבוע‑שבועיים מטופס לאימוץ" | ⟵ נועה: יש טפסים שנתקעים לנצח ⟵ צריך סטטוס + פקיעה |
| 6 | "זה **נדיר**, עשר פעמים בשנה" (מקלט אחר) | ⚠️ נדיר ≠ לא קיים. ראו בקשה ② בשלב 5 |

### ג. הסתירות

| הסתירה | רותי | נועה | ההכרעה |
|---------|-------|-------|---------|
| **מי מאשר אימוץ** | "אם מאשרים — הוא לוקח" (משתמע: רותי) | "בסופ"ש אנחנו סוגרות ומעדכנות ביום ראשון" | ⚠️ **לא להכריע לבד.** לתעד את שתיהן, להעלות כשאלת מדיניות (מודול 8) |
| **תוצאת הראיון** | לא הזכירה | שלוש אפשרויות: מאושר / **בתנאי** / לא | נועה עושה את זה בפועל ⟵ **מתעדים את המציאות**. `INTERVIEW.result` הוא רשימה של 3 |
| **אומנה** | לא הזכירה כלל | "יש לנו משפחות שלוקחות חיה הביתה" | ⭐ **ישות שלמה שרותי שכחה.** לא כי הסתירה — כי זה לא קורה כל שבוע |

> 🔑 **הסתירה השלישית היא הלקח המרכזי של הפרויקט:** ראיון אחד לעולם לא מספיק. שאלת הזהב — *"עם מי עוד כדאי שאדבר?"* — הניבה **ישות מרכזית** שהייתה חסרה לגמרי.

### ד. עשר שאלות פתוחות

| # | השאלה |
|---|--------|
| 1 | חיה שחוזרת מאימוץ שנכשל — כניסה חדשה או המשך של הקיימת? |
| 2 | אימוץ בסוף שבוע — לחסום ללא אישור, או לסמן לאישור בדיעבד? |
| 3 | בקשת אימוץ שנתקעה — לסגור אוטומטית אחרי חודש? כמה זמן? |
| 4 | מי מורשה לראות מה? (נועה צריכה כתובת, לא צריכה סכומים) |
| 5 | כמה שנים לשמור רשומות של חיה שעזבה? יש דרישת חוק? |
| 6 | האם חיה יכולה להיות באומנה **ובמקביל** מוצעת לאימוץ? |
| 7 | האם דמי אימוץ מוחזרים אם החיה מוחזרת? |
| 8 | חיה בהסגר — מותר להתחיל תהליך אימוץ, או אסור לחלוטין? |
| 9 | האם עוקבים אחרי מלאי מזון ותרופות, או רק אחרי ההוצאה? |
| 10 | מה קורה לחיה שנפטרת במקלט — מי רושם ומה מתועד? |

---

## ✅ שלב 2 — מסמך חוקים עסקיים (20 חוקים)

</div>

```text
+----+----------------------------------------+-------------------+----------+-------------+
| #  | RULE                                   | ENTITIES          | TYPE     | ENFORCEMENT |
+----+----------------------------------------+-------------------+----------+-------------+
| 1  | Each animal has exactly one species    | ANIMAL, SPECIES   | referent.| (1) structure|
| 2  | No two animals with the same chip      | ANIMAL            | UID      | (1) UNIQUE  |
| 3  | Chip may be empty (a stray)            | ANIMAL            | domain   | (1) NULL    |
| 4  | Intake is street / surrender / transfer| INTAKE + 3 subtypes| subtypes| (1) structure|
|    | -- exactly one of the three            |                   |          |             |
| 5  | New animal in quarantine >= 14 days    | PLACEMENT         | process  | (2) trigger |
| 6  | Only a vet releases from quarantine    | VET_EXAM          | process  | (3) app     |
| 7  | Quarantined animal cannot move to      | PLACEMENT, HEALTH | complex  | (2) trigger |
|    | the adoption wing                      |                   |          |             |
| 8  | An animal is in ONE kennel at a time   | ANIMAL_PLACEMENT  | complex  | (2) trigger |
| 9  | A kennel holds one animal -- unless     | ANIMAL_PLACEMENT  | complex  | (2) trigger |
|    | litter kin or "arrived together"       |                   |          |             |
| 10 | Animal status from a closed list       | ANIMAL_STATUS     | domain   | (1) table   |
| 11 | The same vaccine can repeat on an animal| VACCINATION      | UID      | (1) surrogate|
| 12 | A vaccination cannot move to another   | VACCINATION       | transfer.| (3) app     |
|    | animal (non-transferable)              |                   |          |             |
| 13 | Adoption fee stored as actually paid   | ADOPTION          | historic | (1) structure|
| 14 | Animal over age 8 -- half price         | ADOPTION, ANIMAL  | complex  | (2) trigger |
| 15 | Interview result: approved / with      | INTERVIEW         | domain   | (1) table   |
|    | conditions / not approved              |                   |          |             |
| 16 | Adoption requires an approved applic.  | ADOPTION, APPLIC. | complex  | (2) trigger |
| 17 | First home visit within 30-45 days     | HOME_VISIT        | process  | (3) app     |
| 18 | Expense tied to an animal or general   | EXPENSE           | domain   | (1) structure|
|    | (NULL)                                 |                   |          |             |
| 19 | One invoice can cover several animals  | EXPENSE_ALLOCATION| M:M      | (1) structure|
| 20 | Nothing is deleted -- flag only         | everything        | policy   | (1) RESTRICT|
+----+----------------------------------------+-------------------+----------+-------------+
| 21 | (!) OPEN: weekend adoption approval    | ADOPTION          | policy   | ? pending   |
| 22 | (!) OPEN: expiry of a pending applic.  | APPLICATION       | process  | ? pending   |
+----+----------------------------------------+-------------------+----------+-------------+
```

<div dir="rtl">

> 💡 שימו לב שחוקים 21–22 מסומנים **פתוחים** ולא הוכרעו. זה **לא חוסר** — זו מקצועיות. מסמך שכולו "סגור" חשוד.

---

## ✅ שלב 3 — המודל

### המבנה הכללי

</div>

```text
                          +------------------+
                          | SPECIES          |
                          +------------------+
                          | # species_id     |
                          | * name           |
                          +--------+---------+
                                   | 1
                          +--------+---------+
                          | BREED            |
                          +------------------+
                          | # breed_id       |
                          | * species_id (FK)|
                          | * name           |
                          +--------+---------+
                                   | 1
                                   | M
+----------------------------------+------------------------------+
| ANIMAL                                                          |
+-----------------------------------------------------------------+
| # animal_id          NUMBER                                     |
| * name               VARCHAR2(50)   default "Unnamed"           |
| * species_id  (FK)                                              |
| o breed_id    (FK)                  not always known            |
| * sex         in {male, female, unknown}                        |
| o birth_date         DATE           (!) estimated!              |
| o birth_date_estimated  BOOLEAN                                 |
| o chip_number        <- UNIQUE, may be NULL                     |
| * current_status (FK) <- ANIMAL_STATUS                          |
+---+---------+----------+---------+----------+----------+--------+
    |         |          |         |          |          |
    | M       | M        | M       | M        | M        | M
    |         |          |         |          |          |
+---+---+ +---+----+ +---+-----+ +-+------+ +-+------+ +-+--------+
|INTAKE | |PLACE-  | |VACCINA- | |ANIMAL_ | |FOSTER  | |DAILY_LOG |
|       | |MENT    | |TION     | |TRAIT   | |        | |          |
+---+---+ +--------+ +---------+ +---+----+ +--------+ +----------+
    |                                | M
    | SUBTYPES                       |
    +- STRAY_INTAKE     (location, finder) 1
    +- SURRENDER_INTAKE (owner, reason)   |
    +- TRANSFER_INTAKE  (source shelter) ++----------+
                                      | TRAIT     |
                                      | # trait_id|
                                      | * name    |
                                      | * category|
                                      +-----------+
```

<div dir="rtl">

### הישויות המרכזיות בפירוט

</div>

```text
(1) LOCATION -- a recursive hierarchy
+--------------------------------+
| LOCATION                       |      Building A
+--------------------------------+        +- Quarantine wing
| # location_id                  |        |    +- kennel 1
| * name                         |        |    +- kennel 2
| * level in {building,wing,kennel}|      +- Dog wing
| o parent_location_id (FK) -----+--.     +- Cat wing
| o capacity                     |  |   Building B
+--------------------------------+  |     +- Large-dog wing
              ^                     |     +- Rabbit corner
              '---------------------'

(2) A PERIOD ENTITY -- where the animal is, now and ever
+----------------------------------------+
| ANIMAL_PLACEMENT                       |   Luna:
+----------------------------------------+     Quarantine 14/09 -> 28/09
| # placement_id                         |     Wing A      28/09 -> 03/11
| * animal_id     (FK)                   |     Wing B      03/11 -> NULL
| * location_id   (FK)                   |
| * start_date                           |   <- answers "who was in
| o end_date      (NULL = now)           |      this kennel in the
| o move_reason                          |      last month?"
+----------------------------------------+

(3) * EXPENSES -- the answer to "one invoice, several animals"
+------------------+  1      M +--------------------------+
| EXPENSE          +-----------+ EXPENSE_ALLOCATION       |
+------------------+           +--------------------------+
| # expense_id     |           | # allocation_id          |
| * amount NUMBER  |           | * expense_id    (FK)     |
| * expense_date   |           | * animal_id     (FK)     |
| * category_id(FK)|           | * allocated_amount       |
| o invoice_number |           +--------------------------+
| o supplier_id(FK)|                        | M
+------------------+                        |
                                            | 1
                                    +-------+--------+
                                    | ANIMAL         |
                                    +----------------+

   (!) This is the entity the students in the README story missed.
       A 4,000 NIS invoice for 8 animals splits into 8 allocation rows.
       A general expense (electricity) simply has no allocation rows.

(4) ** FOSTER -- the entity Ruti forgot
+----------------------------------------+
| FOSTER                                 |   (!) This is NOT an adoption:
+----------------------------------------+     . the animal still belongs
| # foster_id                            |       to the shelter
| * animal_id     (FK)                   |     . there is no fee
| * person_id     (FK)  <- foster family |     . there is an expected end date
| * start_date                           |     . the animal comes back
| o expected_end_date                    |
| o actual_end_date                      |
| * reason  in {pups, medical, settling} |
+----------------------------------------+

(5) THE ADOPTION PROCESS -- a chain of four entities
+------------------+ 1   M +--------------+ 1   M +--------------+
| ADOPTION_        +-------+ INTERVIEW    |       | ADOPTION     |
| APPLICATION      |       +--------------+       +--------------+
+------------------+       | # interview  |       | # adoption_id|
| # application_id |       | * app_id (FK)|       | * app_id (FK)|
| * person_id (FK) |       | * interviewer|       | * animal_id  |
| * animal_id (FK) |       |   _id   (FK) |       | * person_id  |
| * applied_date   |       | * date       |       | * adopt_date |
| * status_code(FK)|       | * result in  |       | * fee_paid   |
| o has_yard  BOOL |       |  {approved,  |       |   <- FROZEN! |
| o children_count |       |   w/ conds,  |       | * address_at_|
| o youngest_child |       |   rejected}  |       |   adoption   |
|   _age           |       | o condition  |       |   <- FROZEN! |
| o other_pets     |       | o notes      |       +------+-------+
+------------------+       +--------------+              | 1
                                                         | M
                                                  +------+-------+
                                                  | HOME_VISIT   |
                                                  +--------------+
                                                  | # visit_id   |
                                                  | * adoption_id|
                                                  | * visitor_id |
                                                  | * visit_date |
                                                  | * outcome    |
                                                  +--------------+

(6) ** THE MATCHING -- the knowledge that lived "in Ruti's head"
+--------------+ 1   M +------------------+ M   1 +--------------+
| ANIMAL       +-------+ ANIMAL_TRAIT     +-------+ TRAIT        |
+--------------+       +------------------+       +--------------+
                       | # animal_trait_id|       | # trait_id   |
                       | * animal_id (FK) |       | * name       |
                       | * trait_id  (FK) |       | * category in|
                       | o level in {low, |       |  {children,  |
                       |    medium, high} |       |   other pets,|
                       | o noted_date     |       |   space,noise}|
                       | o noted_by  (FK) |       +--------------+
                       +------------------+

   TRAIT examples:  "patient with children" . "gets on with cats"
                    "needs a lot of space"  . "afraid of noise"
```

<div dir="rtl">

### ו. ⭐ בדיקת שלוש השאלות

<div align="center">

**זה החלק שקובע אם המודל הצליח.**

</div>

| # | השאלה | הישויות הנדרשות | איך מחשבים |
|---|--------|------------------|-------------|
| **1** | כמה זמן חיה שוהה בממוצע? | `INTAKE.intake_date` + `ADOPTION.adoption_date` | ממוצע של ההפרש, לכל חיה שאומצה. ⚠️ **דורש שהחזרה תהיה `INTAKE` חדשה** — אחרת שהות שנייה תיספר כאחת ארוכה |
| **2** | כמה עולה להחזיק חיה? | `EXPENSE` + **`EXPENSE_ALLOCATION`** + `ANIMAL` | סכום `allocated_amount` לכל חיה. ⭐ **בלי ישות ההקצאה — בלתי אפשרי** |
| **3** | איזו חיה מתאימה למשפחה? | `TRAIT` + `ANIMAL_TRAIT` + `ADOPTION_APPLICATION` (`children_count`, `has_yard`, `other_pets`) | סינון: חיות שאין להן תכונה חוסמת מול נתוני המשפחה |

</div>

```text
A full example for question 3 -- "family with a 4-year-old, a flat, and a cat":

  STEP 1:  read from the application:  youngest_child_age = 4
                                       has_yard = false
                                       other_pets = "cat"

  STEP 2:  RULE OUT animals with:
             TRAIT "not suitable for small children"
             TRAIT "needs a lot of space"        (because there is no yard)
             TRAIT "does not get on with cats"

  STEP 3:  PREFER animals with:
             TRAIT "patient with children" at a HIGH level

  <- and this is exactly the knowledge that "lived in Ruti's head",
     whose absence let an aggressive dog go to a family with a baby.
```

<div dir="rtl">

> 🔑 **שימו לב לשורה 1 בטבלה:** ההחלטה "חזרה = `INTAKE` חדשה" נראית כמו פרט טכני — אבל היא **קובעת אם התשובה לשאלה 1 נכונה או שגויה**. כך נראה עיצוב שנגזר מהשאלות ולא מהתחושה.

---

## ✅ שלב 4 — ההצגה

### א. מילון ישויות (מדגם)

| הישות | בעברית פשוטה |
|--------|---------------|
| `ANIMAL` | כל חיה שהמקלט טיפל בה אי פעם — גם אם כבר אומצה או נפטרה |
| `INTAKE` | פעם אחת שחיה נכנסה למקלט. חיה שחוזרת מקבלת כניסה חדשה |
| `ANIMAL_PLACEMENT` | איפה כל חיה שוכנת — היום, ובכל רגע בעבר |
| `TRAIT` | תכונת אופי — "סבלני עם ילדים", "מפחד מרעש" |
| `FOSTER` | תקופה שחיה מבלה אצל משפחה בבית, בלי שהיא נמסרת להם |
| `EXPENSE` | הוצאה כספית אחת — חשבונית, קנייה, טיפול |
| `EXPENSE_ALLOCATION` | חלוקת ההוצאה בין החיות שהיא נועדה להן |
| `ADOPTION_APPLICATION` | טופס שמישהו מילא כדי לבקש לאמץ חיה מסוימת |
| `INTERVIEW` | הפגישה שבה מתנדבת בודקת אם המשפחה מתאימה |
| `ADOPTION` | אימוץ שהתבצע בפועל, כולל הסכום ששולם באותו יום |
| `HOME_VISIT` | ביקור מעקב אצל המאמץ אחרי האימוץ |
| `DAILY_LOG` | רישום יומי של מתנדבת: האכלתי, טיילתי, היא נראית עצובה |

### ג. תסריט ההצגה (קטע)

> *"רותי, לפני שאני מראה משהו — בואי ניקח את לונה, הכלבה שהגיעה בספטמבר. נעבור איתה על כל המערכת."*
>
> **[מצביע]** *"כאן לונה עצמה — השם שלה, שהיא כלבה, גיל משוער, ושבב. לא היה לה שבב כשהגיעה, אז השארנו ריק ומילאנו אחר כך."*
>
> ⟵ **[עוצר]**
>
> **[מצביע]** *"וכאן **הכניסה** שלה — שמתנדב מצא אותה ברחוב הרצל, באיזה מצב היא הייתה, ומי הביא אותה. הפרדתי בין השתיים בכוונה. אמרת לי שקורה שחיה חוזרת אחרי אימוץ שנכשל. אם הכול היה במקום אחד, החזרה הייתה **מוחקת** את הפעם הראשונה — ואת תאבדי את התשובה לשאלה כמה זמן היא באמת הייתה אצלך.*
>
> *נכון שזה מה שרצית?"*
>
> ⟵ **[עוצר. לא ממשיך בלי תשובה.]**
>
> **[מצביע]** *"כאן איפה היא שוכנת. שבועיים בהסגר, אחר כך אגף א', ובנובמבר העברת אותה לאגף ב'. ואם בעוד שנה תגלי מחלה בכלוב 4 — תוכלי לשאול מי היה שם בחודשיים האחרונים."*
>
> ⚠️ **[הטעות המכוונת:]**
> *"אז לפי מה שהבנתי, אם חיה חוזרת מאימוץ, אנחנו מתחילים לה תיק רפואי חדש — נכון?"*
>
> ⟵ רותי אמרה במפורש שהתיק הרפואי **נשאר**. אם היא מתקנת ✅ · אם היא מהנהנת ❌ עוצרים ומתחילים מחדש.
>
> **[מצביע]** ⭐ *"וכאן הדבר שהכי חשוב לך. זוכרת שסיפרת שהידע על מי מתאים למי נמצא בראש שלך? כאן הוא יושב. לכל חיה רשומות התכונות שלה — סבלנית עם ילדים, מסתדרת עם חתולים, צריכה מרחב. וכשמשפחה ממלאת טופס, המערכת יודעת להצליב. גם כשאת בחופש."*

---

## ✅ שלב 5 — שילוב השינויים ⭐

זהו החלק שמפריד בין תרגיל לפרויקט. **שתי בקשות מסוכנות, וצריך לזהות אותן.**

### ① "חיה שמורה למישהו"

| | |
|---|---|
| **ההכרעה** | ✅ **מקבלים** |
| **ההשפעה** | ערך חדש בטבלת `ANIMAL_STATUS`: `RESERVED`. אין ישות חדשה |
| **בונוס** | זה גם פותר בעיה שרותי לא הזכירה: שני אנשים שמבקשים את אותה חיה במקביל |

> *"בשמחה, וזה גם פותר משהו נוסף — היום, אם שתי משפחות מבקשות את אותה כלבה באותו שבוע, אין לך דרך לדעת. עם סימון 'שמורה' זה ברור לכולן."*

---

### ② "תורידי את הכניסה ממקלט אחר, זה נדיר"

| | |
|---|---|
| **ההכרעה** | ⚠️ **חלופה — ולא ויתור** |
| **הסכנה** | ⚠️ **זו הבקשה התמימה שמוחקת מידע.** "נדיר" ≠ "לא קיים" — 10 בשנה = 130 חיות מאז 2013 |

> *"אני מבין שזה נראה מיותר. אבל 10 בשנה זה בערך 130 חיות מאז שפתחת — ולכל אחת יש היסטוריה שונה לגמרי, כי היא הגיעה עם תיק רפואי ממקלט אחר.*
>
> *מה שאני מציע: לא להוריד את הסוג, אבל **להסתיר אותו במסך**. כשתקלטי חיה תראי שתי אפשרויות — רחוב ומסירה. ולידן קישור קטן 'אחר'. שנייה אחת של עבודה, ואת לא מאבדת את המידע."*

**🔑 העיקרון:** בקשה לפשט **ממשק** אינה בקשה לפשט **מודל**. אפשר לתת לרותי בדיוק את מה שהיא רוצה בלי למחוק ישות.

---

### ③ "תעדכן אוטומטית את תאריך החיסון הבא"

| | |
|---|---|
| **ההכרעה** | ✅ **מקבלים** — אבל שואלים שאלה אחת קודם |
| **ההשפעה** | ישות חדשה `VACCINE_PROTOCOL` (מין + סוג חיסון + מרווח בימים). ⚠️ הערך המחושב **לא נשמר** — הוא נגזר |

> *"אפשר. אני רק צריך לדעת ממך את הפרוטוקול — לכל מין ולכל חיסון, כמה זמן עד הבא. יש לך את זה כתוב איפשהו, או שזה גם בראש?"*

⚠️ **מלכודת נרמול:** אל תשמרו `next_vaccination_date` כעמודה. היא נגזרת מ‑`vaccination_date + protocol.interval_days`, ותהיה שגויה ברגע שהפרוטוקול ישתנה. **מחשבים בזמן אמת.**

---

### ④ ⚠️ "תשים לי עמודה 'כלוב נוכחי' במקום כל התקופות"

<div align="center">

**זו הבקשה ששוברת את המודל. כאן, ורק כאן, מסרבים.**

</div>

| | |
|---|---|
| **ההכרעה** | ❌ **סירוב מנומק + חלופה** |
| **הסכנה** | עמודה שמתעדכנת במקום **מוחקת את העבר לתמיד** — וזה נוגד ישירות את מה שרותי עצמה ביקשה |

**נוסחת ה"לא" בשלושה שלבים (מודול 8):**

**① הכרה בצורך:**
> *"אני מבין לגמרי — את רוצה לראות איפה החיה בלי לחפש."*

**② התוצאה בעולם שלה:**
> *"אבל תראי מה קורה: אמרת לי בראיון שאם מתגלה מחלה, את חייבת לדעת מי היה בכלוב הזה בחודש האחרון. עם עמודה אחת, ברגע שאני מעביר את לונה מכלוב 4 לכלוב 7 — העובדה שהיא הייתה בכלוב 4 **נמחקת**. אין גיבוי שיחזיר אותה. ביום שתהיה התפרצות, לא תדעי את מי לבדוק."*

**③ החלופה שנותנת לה בדיוק מה שרצתה:**
> *"מה שאני מציע: המסך יראה בדיוק מה שביקשת — שורה אחת, 'לונה, כלוב 7'. פשוט כמו שרצית. ההיסטוריה יושבת מתחת ולא מפריעה לאף אחד, ותהיה שם ביום שתצטרכי אותה."*

> 🎓 **זהו הלקח המרכזי של שלב 5:** רותי לא ביקשה משהו טיפשי — היא ביקשה **פשטות בממשק** ותיארה אותה במונחי **מבנה**. תפקידכם לתת לה את הראשונה בלי לוותר על השנייה.

---

### ⑤ "מתנדבת תראה כתובת אבל לא סכומים"

| | |
|---|---|
| **ההכרעה** | ✅ **מקבלים — וזו בקשה מצוינת** |
| **ההשפעה** | **אפס שינוי במודל.** זו שאלת **הרשאות**, לא עיצוב |

> *"בהחלט, וטוב שהעלית. זה לא משנה שום דבר במבנה — זה עניין של מי רואה מה במסך. אני רושם את זה כדרישה, ונגדיר יחד מי רואה כל שדה."*

**🔑 עיקרון:** לא כל בקשה היא בקשה למודל. חלק מהבקשות הן **דרישות מערכת** — ולזהות את ההבדל זה חלק מהמקצוע.

---

### ⑥ "מודול תרומות ל‑300 תורמים"

| | |
|---|---|
| **ההכרעה** | ⚠️ **"כן, וזה עולה"** ⟵ שלב ב' |
| **ההשפעה** | `DONOR` · `DONATION` · `RECEIPT` · דיווח לרשויות · תרומה בהוראת קבע. **מערכת שנייה** |

> *"אפשר בהחלט. רק שנדע מה זה כולל: תורם, תרומה, קבלה — ואם יש קבלות לעמותה, גם דיווח שנתי לרשויות. בערך שלושה שבועות.*
>
> *שתי אפשרויות: (א) נכניס עכשיו והעלייה נדחית בשלושה שבועות. (ב) נסיים את החיות והאימוצים, תתחילי לעבוד, ונוסיף תרומות מיד אחרי.*
>
> *אני ממליץ על ב' — כי הכאב הכי גדול שלך היום הוא הטלפונים והעלויות, לא התורמים. אבל זו החלטה שלך."*

### 📊 סיכום שלב 5

| הבקשה | ההכרעה | הלקח |
|--------|---------|-------|
| ① שמורה | ✅ קבלה | בקשה טובה שגם פותרת בעיה נסתרת |
| ② הורדת סוג קליטה | ⚠️ חלופה | **פישוט ממשק ≠ פישוט מודל** |
| ③ חיסון אוטומטי | ✅ קבלה + שאלה | ⚠️ ערך מחושב — לא לשמור |
| ④ כלוב נוכחי | ❌ **סירוב** | ⚠️ **הבקשה ששוברת את המודל** |
| ⑤ הרשאות | ✅ קבלה | לא כל בקשה היא בקשה למודל |
| ⑥ תרומות | ⚠️ שלב ב' | "כן, וזה עולה" |

---

## ✅ שלב 6 — יומן ההחלטות (מדגם)

</div>

```text
+----+----------+----------------------------+--------------------+---------+--------+
| #  | date     | DECISION                   | REASON             | WHO     | STATUS |
+----+----------+----------------------------+--------------------+---------+--------+
| 1  | 14/09    | ANIMAL and INTAKE separate | animals return;    | cons. * | closed |
|    |          |                            | needed to compute  |         |        |
|    |          |                            | average stay       |         |        |
| 2  | 14/09    | Three subtypes for INTAKE  | each source has    | cons. * | closed |
|    |          |                            | 4-5 unique attrs   |         |        |
| 3  | 16/09    | * EXPENSE_ALLOCATION as an | one invoice for 8  | Ruti    | closed |
|    |          | M:M intersection entity    | animals -- else no |         |        |
|    |          |                            | answer to Q2       |         |        |
| 4  | 16/09    | * FOSTER separate from     | raised by Noa; the | Noa     | closed |
|    |          | ADOPTION                   | animal stays ours  |         |        |
| 5  | 16/09    | TRAIT as an entity, not    | matching IS the    | Ruti    | closed |
|    |          | free text                  | core function      |         |        |
| 6  | 16/09    | Interview result = 3 values| Noa describes      | cons. * | closed |
|    |          | (incl. "with conditions")  | reality; Ruti      |         |        |
|    |          |                            | didn't know        |         |        |
| 7  | 20/09    | Fee + address FROZEN in    | rate changed 2024; | Ruti    | closed |
|    |          | the adoption record        | visits use the     |         |        |
|    |          |                            | address of the day |         |        |
| 8  | 20/09    | next_vaccination COMPUTED, | the protocol       | cons. * | closed |
|    |          | not stored                 | changes            |         |        |
| 9  | 24/09    | [X] REJECTED: a            | erases history     | cons. + | closed |
|    |          | "current kennel" column    | Ruti herself needs | Ruti *  |        |
|    |          | instead of a period entity |                    |         |        |
| 10 | 24/09    | Intake type "other shelter"| 130 animals since  | Ruti *  | closed |
|    |          | kept, hidden in the UI     | 2013               |         |        |
| 11 | 24/09    | Donations -> phase 2       | a second system,   | Ruti    | closed |
|    |          |                            | ~3 weeks           |         |        |
+----+----------+----------------------------+--------------------+---------+--------+
| 12 | 24/09    | (!) weekend adoption       | Ruti and Noa       | waiting | open   |
|    |          | approval?                  | described          | on mgmt |        |
|    |          |                            | different rules    |         |        |
| 13 | 24/09    | (!) pending application    | Noa: "dozens of    | waiting | open   |
|    |          | expires after how long?    | stuck forms"       | on Ruti |        |
| 14 | 24/09    | (!) how many years to keep | possible legal     | waiting | open   |
|    |          | records?                   | requirements       | on Ruti |        |
+----+----------+----------------------------+--------------------+---------+--------+

   * = decided by the consultant, approved by the client
```

<div dir="rtl">

---

## 🎓 שלב 7 — הרפלקציה: מה היה אמור לקרות

| השאלה | התשובה הצפויה |
|--------|-----------------|
| **א.** כמה ישויות בהתחלה ובסוף? | בערך 12 אחרי קריאה ראשונה ⟵ **22–26** בסוף. הגידול הוא מנרמול, מהראיון השני, ומשלוש השאלות |
| **ב.** מה פספסתם עד נועה? | **`FOSTER`** (ישות שלמה) · **"מאושר בתנאי"** · פקיעת בקשות · הסתירה על אישור בסופ"ש |
| **ג.** ההחלטה הקשה | בדרך כלל אחת משתיים: איך מפרקים חשבונית לכמה חיות · האם חזרה היא `INTAKE` חדש |
| **ד.** מה לעשות אחרת | לרוב: **לא להתחיל לצייר מוקדם מדי.** מי שצייר אחרי 10 דקות בנה מודל שלא כלל את ההוצאות ואת ההתאמה |
| **ה.** התשובה החלשה | ברוב הפתרונות — **שאלה 2 (עלות לחיה)**, כי היא דורשת ישות שלא נאמרה במפורש באף מקום |

<div align="center">

---

### 🏆 סיימתם את חלק א' של הקורס!

בנֵיתם מודל מלא מראיון גולמי, הגנתם עליו, שילבתם שינויים — וידעתם מתי לומר "לא".
זה בדיוק מה שעושה מעצב בסיסי נתונים.

**נשארו עוד שישה פרקים בחלק א' (10–15), ואז — SQL.**

---

### ➡️ [מודול 10 — עיצוב למעקב אחר שינויים](../module-10-tracking-changes/)

</div>

---

[⬅️ לפרויקט](exercises.md) · [❓ למבחן החזרה](questions.md) · [📖 חזרה למודול](README.md) · [🏠 דף הקורס](../../)

---

<div align="center">

**🧭 ניווט המודול**

</div>

| 📖 [חזרה למודול](README.md) | ❓ [שאלות ותשובות](questions.md) | ✏️ [לתרגילים](exercises.md) | 🏠 [דף הקורס](../../) |
|---|---|---|---|
</div>
