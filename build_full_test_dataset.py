import json

data = {
    "test_title": "Infosys Systems Engineer (SE) Mock Test — 2027 Batch Pattern",
    "total_questions": 60,
    "total_marks": 75,
    "total_duration_minutes": 120,
    "sections": [
        {
            "id": 1,
            "name": "Reasoning Ability Test",
            "total_questions": 15,
            "max_marks": 15,
            "duration_minutes": 25,
            "instructions": "Topics: Data Sufficiency, Data Interpretation, Logical Deduction, Syllogisms, Statistical Data Interpretation, Data Arrangement, Blood Relations, Coding-Decoding, Directional Sense. ~1 min 40 sec per question."
        },
        {
            "id": 2,
            "name": "Technical Ability Test (Mathematical)",
            "total_questions": 10,
            "max_marks": 10,
            "duration_minutes": 35,
            "instructions": "Topics: Number Series [HP], Ratios & Proportions [HP], Permutation/Combination/Probability [HP], Time-Speed-Distance [HP], Cryptarithmetic, Profit & Loss, Partnerships, Averages, Algebra, Simplification. ~3.5 mins per question."
        },
        {
            "id": 3,
            "name": "Verbal Ability Test",
            "total_questions": 20,
            "max_marks": 20,
            "duration_minutes": 20,
            "instructions": "Topics: Critical Reasoning [HP], English Corrective Usage [HP], English Error Correction [HP], Error Identification, Reading Comprehension, Para Jumbles, Synonyms & Antonyms. 1 min per question."
        },
        {
            "id": 4,
            "name": "Pseudocode Test",
            "total_questions": 5,
            "max_marks": 10,
            "duration_minutes": 10,
            "instructions": "Each question carries 2 marks. Topics: Programming Logic [HP], Loop Tracing (FOR/WHILE), Conditional Statements (IF/ELSE), Basic Algorithms, Array & String Manipulation. 2 mins per question."
        },
        {
            "id": 5,
            "name": "Numerical Puzzle Test",
            "total_questions": 4,
            "max_marks": 10,
            "duration_minutes": 10,
            "instructions": "Each question carries 2.5 marks. Topics: Visual Reasoning [HP], Word Puzzles [HP], Number Based Patterns [HP], Sudoku, Grid Based Puzzles. ~2.5 mins per question."
        },
        {
            "id": 6,
            "name": "English Grammar Test",
            "total_questions": 5,
            "max_marks": 10,
            "duration_minutes": 10,
            "instructions": "Each question carries 2 marks. Topics: Tenses [HP], Subject-Verb Agreement [HP], Articles & Prepositions, Parts of Speech, Active & Passive Voice, Direct & Indirect Speech, Punctuation. 2 mins per question."
        },
        {
            "id": 7,
            "name": "English Writing Test",
            "total_questions": 1,
            "max_marks": 0,
            "marks_label": "NA (Evaluated Separately)",
            "duration_minutes": 10,
            "instructions": "Topics: Essay Writing [HP], Email/Letter Writing [HP], Paragraph Writing, Coherence & Logical Structure, Grammar & Vocabulary Usage. 150-250 words. 10 mins."
        }
    ],
    "questions": []
}

# ========================================================================
# SECTION 1: REASONING ABILITY TEST (15 Questions, 15 Marks, 25 Minutes)
# Based on real Infosys PYQs — 2027 Batch Syllabus
# ========================================================================
sec1 = [
    {
        "id": 1, "section_id": 1, "topic": "Data Sufficiency", "marks": 1,
        "question": "What is the average age of students in a class?\n\nStatement I: The total age of all students in the class is 500 years.\nStatement II: The number of students in the class is 25.",
        "options": {
            "A": "Statement I alone is sufficient",
            "B": "Statement II alone is sufficient",
            "C": "Both statements together are necessary",
            "D": "Neither statement is sufficient"
        },
        "correct_answer": "C",
        "explanation": "Average = Total Age / Number of Students.\nStatement I gives total age (500) but not the count → insufficient alone.\nStatement II gives the count (25) but not the total → insufficient alone.\nCombining both: Average = 500 / 25 = 20 years. Both statements together are necessary."
    },
    {
        "id": 2, "section_id": 1, "topic": "Data Sufficiency", "marks": 1,
        "question": "Is the two-digit number XY divisible by 9?\n\nStatement I: X + Y = 9.\nStatement II: X = 2Y.",
        "options": {
            "A": "Statement I alone is sufficient",
            "B": "Statement II alone is sufficient",
            "C": "Both statements together are necessary",
            "D": "Neither statement is sufficient"
        },
        "correct_answer": "A",
        "explanation": "Divisibility rule for 9: A number is divisible by 9 if the sum of its digits is divisible by 9.\nStatement I: X + Y = 9. Since 9 is divisible by 9, the number XY is definitely divisible by 9. Sufficient alone.\nStatement II: X = 2Y. Multiple possibilities exist (e.g., 21, 42, 63, 84) — some divisible by 9, some not. Insufficient alone.\nAnswer: Statement I alone is sufficient."
    },
    {
        "id": 3, "section_id": 1, "topic": "Data Interpretation (Table)", "marks": 1,
        "question": "A company's quarterly revenue (in lakhs) is as follows:\nQ1: 45, Q2: 52, Q3: 48, Q4: 55.\n\nWhat is the percentage increase in revenue from Q1 to Q4?",
        "options": {
            "A": "18.18%",
            "B": "22.22%",
            "C": "20.00%",
            "D": "15.00%"
        },
        "correct_answer": "B",
        "explanation": "Increase = Q4 − Q1 = 55 − 45 = 10 lakhs.\nPercentage increase = (10 / 45) × 100 = 22.22%."
    },
    {
        "id": 4, "section_id": 1, "topic": "Data Interpretation (Bar Chart)", "marks": 1,
        "question": "A store's monthly laptop sales are:\nJan: 120, Feb: 150, Mar: 180, Apr: 140, May: 200.\n\nWhat is the average number of laptops sold per month?",
        "options": {
            "A": "158",
            "B": "162",
            "C": "155",
            "D": "170"
        },
        "correct_answer": "A",
        "explanation": "Total = 120 + 150 + 180 + 140 + 200 = 790.\nAverage = 790 / 5 = 158."
    },
    {
        "id": 5, "section_id": 1, "topic": "Syllogism", "marks": 1,
        "question": "Statements:\n1. All dogs are animals.\n2. Some animals are cats.\n\nConclusions:\nI. Some dogs are cats.\nII. Some cats are animals.\n\nWhich conclusions logically follow?",
        "options": {
            "A": "Only Conclusion I follows",
            "B": "Only Conclusion II follows",
            "C": "Both I and II follow",
            "D": "Neither I nor II follows"
        },
        "correct_answer": "B",
        "explanation": "Dogs are a subset of animals. Some animals are cats (partial overlap).\n• Conclusion I: 'Some dogs are cats' — not necessarily true; the overlap between animals and cats may not include the dog subset.\n• Conclusion II: 'Some cats are animals' — directly follows from Statement 2.\nOnly Conclusion II follows."
    },
    {
        "id": 6, "section_id": 1, "topic": "Syllogism", "marks": 1,
        "question": "Statements:\n1. No pen is an eraser.\n2. All erasers are sharpeners.\n\nConclusions:\nI. No pen is a sharpener.\nII. Some sharpeners are erasers.\n\nWhich conclusions logically follow?",
        "options": {
            "A": "Only Conclusion I follows",
            "B": "Only Conclusion II follows",
            "C": "Both I and II follow",
            "D": "Neither follows"
        },
        "correct_answer": "B",
        "explanation": "'All erasers are sharpeners' means erasers are a subset of sharpeners → 'Some sharpeners are erasers' is definitely true (Conclusion II follows).\n'No pen is a sharpener' is not necessarily true — sharpeners include items beyond erasers, and pens might overlap with those → Conclusion I does not follow.\nOnly Conclusion II follows."
    },
    {
        "id": 7, "section_id": 1, "topic": "Coding-Decoding", "marks": 1,
        "question": "In a certain code language, 'COMPUTER' is written as 'FRPSXWHU'.\n\nHow is 'DATA' written in that code?",
        "options": {
            "A": "GDWD",
            "B": "FCVC",
            "C": "GDWC",
            "D": "EDWB"
        },
        "correct_answer": "A",
        "explanation": "Each letter is shifted forward by 3 positions in the English alphabet.\nC→F, O→R, M→P, P→S, U→X, T→W, E→H, R→U ✓\nApplying the same rule to DATA:\nD→G, A→D, T→W, A→D → GDWD."
    },
    {
        "id": 8, "section_id": 1, "topic": "Blood Relations", "marks": 1,
        "question": "Pointing to a woman in a photograph, a man said: 'She is the daughter of the only child of my grandmother.'\n\nHow is the woman related to the man?",
        "options": {
            "A": "Mother",
            "B": "Sister",
            "C": "Aunt",
            "D": "Cousin"
        },
        "correct_answer": "B",
        "explanation": "'The only child of my grandmother' = the man's parent (mother or father).\n'She is the daughter of my parent' = the man's sister.\nTherefore, the woman is the man's sister."
    },
    {
        "id": 9, "section_id": 1, "topic": "Directional Sense", "marks": 1,
        "question": "Ravi starts from his house and walks 10 km towards North. He then turns left and walks 5 km. He then turns left again and walks 10 km.\n\nIn which direction is he from his starting point?",
        "options": {
            "A": "North",
            "B": "South",
            "C": "East",
            "D": "West"
        },
        "correct_answer": "D",
        "explanation": "Starting at origin (0, 0):\n1. 10 km North → (0, 10)\n2. Turn left (West), 5 km → (−5, 10)\n3. Turn left (South), 10 km → (−5, 0)\nFinal position is (−5, 0) — directly 5 km West of the starting point.\nDirection from start: West."
    },
    {
        "id": 10, "section_id": 1, "topic": "Linear Seating Arrangement", "marks": 1,
        "question": "Seven people — P, Q, R, S, T, U, V — are sitting in a straight row facing North.\n• R sits exactly in the middle.\n• P sits at one of the extreme ends.\n• S is to the immediate right of P.\n• Q is to the immediate left of R.\n• T is not adjacent to R.\n• U sits between T and V.\n\nWho sits at the other extreme end (opposite to P)?",
        "options": {
            "A": "T",
            "B": "V",
            "C": "U",
            "D": "Q"
        },
        "correct_answer": "B",
        "explanation": "Positions 1-7 (left to right). R is at position 4 (middle). P is at an end.\nS is immediate right of P → P must be at position 1, S at position 2 (if P at 7, right would be off-board).\nQ is immediate left of R → Q at position 3.\nPositions: P(1), S(2), Q(3), R(4), _, _, _.\nT is not adjacent to R → T cannot be at position 5. T is at 6 or 7.\nU sits between T and V → they must be consecutive in order T-U-V or V-U-T.\nIf T at 6: U at 7, V would need to be at 8 (impossible). If V-U-T: V at 5, U at 6, T at 7 → T not adjacent to R(4) ✓.\nArrangement: P(1), S(2), Q(3), R(4), V(5), U(6), T(7).\nWait, V is at position 7's extreme end? No: T at 7 is the extreme. But 'U between T and V': positions V(5), U(6), T(7) ✓.\nOther extreme end (position 7) = T? But let me check: T not adjacent to R means T ≠ 3 or 5. Q is at 3. If T at 7, U at 6, V at 5: T-U-V has U between T(7) and V(5) ✓, T not adjacent to R(4) ✓.\nThe other extreme = T.\n\nWait, let me re-examine. If P at 1, S at 2, Q at 3, R at 4. Remaining positions 5, 6, 7 for T, U, V. T not adjacent to R means T ≠ 5. 'U between T and V' means one of: T-U-V or V-U-T consecutively. Options: T at 6, U at ?, V at ?: T(6)-U(7)-V(?) impossible, or V(5)-U(6)-T(7) → U between V and T ✓. But 'U between T and V' specifically: T at 7, U at 6, V at 5 → U is between them ✓. T not at 5 ✓.\nExtreme end position 7 = T. But answer option A is T.\n\nAlternatively: T at 6, then U between T and V: V(5)-U(?)-T(6), U would be between 5 and 6 which is impossible (no integer position). Or T(6)-U(7)-V(8) impossible.\nSo only valid: V(5), U(6), T(7). Position 7 = T.\nBut I listed answer as B (V). Let me fix: the other extreme is T."
    },
    {
        "id": 11, "section_id": 1, "topic": "Circular Seating Arrangement", "marks": 1,
        "question": "Six people — A, B, C, D, E, F — sit around a circular table facing the center.\n• A sits opposite to D.\n• B is to the immediate left of A.\n• C is to the immediate right of D.\n• E is not adjacent to A.\n\nWho sits directly opposite to B?",
        "options": {
            "A": "C",
            "B": "E",
            "C": "F",
            "D": "D"
        },
        "correct_answer": "B",
        "explanation": "Place A at position 1 (clockwise: 1,2,3,4,5,6). D is opposite A → D at position 4.\nB is immediate left of A (clockwise from A's perspective facing center) → B at position 6.\nC is immediate right of D (clockwise from D's perspective facing center) → C at position 5.\nOpposite pairs: (1,4), (2,5), (3,6). B at position 6 → opposite is position 3.\nRemaining positions 2 and 3 for E and F. E is not adjacent to A. Position 2 is adjacent to A(1). So E ≠ position 2 → E at position 3, F at position 2.\nOpposite to B(6) = position 3 = E."
    },
    {
        "id": 12, "section_id": 1, "topic": "Logical Deduction", "marks": 1,
        "question": "Statement: 'All employees who work overtime will receive a bonus.'\nFact: Ravi did not receive a bonus.\n\nWhat can be logically concluded?",
        "options": {
            "A": "Ravi did not work overtime",
            "B": "Ravi is not an employee",
            "C": "Ravi worked overtime but was denied the bonus",
            "D": "Cannot be determined"
        },
        "correct_answer": "A",
        "explanation": "The statement establishes: Overtime → Bonus.\nContrapositive: No Bonus → No Overtime.\nSince Ravi received no bonus, by contrapositive (modus tollens), Ravi did not work overtime."
    },
    {
        "id": 13, "section_id": 1, "topic": "Logical Deduction", "marks": 1,
        "question": "Statement: 'If it rains, the cricket match will be cancelled.'\nFact: The cricket match was not cancelled.\n\nWhat can be logically concluded?",
        "options": {
            "A": "It rained",
            "B": "It did not rain",
            "C": "The match was played indoors",
            "D": "Cannot be determined"
        },
        "correct_answer": "B",
        "explanation": "Given: Rain → Match Cancelled.\nContrapositive: Match Not Cancelled → No Rain.\nSince the match was not cancelled, by contrapositive, it did not rain."
    },
    {
        "id": 14, "section_id": 1, "topic": "Statistical Data Interpretation", "marks": 1,
        "question": "The marks obtained by a student in 5 subjects are: 78, 85, 92, 67, 88.\n\nWhat is the median of these marks?",
        "options": {
            "A": "82",
            "B": "85",
            "C": "88",
            "D": "78"
        },
        "correct_answer": "B",
        "explanation": "Arrange in ascending order: 67, 78, 85, 88, 92.\nFor an odd number of values, the median is the middle value.\nMiddle value (3rd of 5) = 85."
    },
    {
        "id": 15, "section_id": 1, "topic": "Statistical Data Interpretation", "marks": 1,
        "question": "In a class of 60 students, the mean marks in Mathematics is 72. If 5 students who scored an average of 40 marks are excluded, what is the new mean of the remaining students (rounded to two decimal places)?",
        "options": {
            "A": "74.91",
            "B": "75.64",
            "C": "76.36",
            "D": "73.45"
        },
        "correct_answer": "A",
        "explanation": "Total marks = 60 × 72 = 4320.\nMarks of 5 excluded students = 5 × 40 = 200.\nRemaining total = 4320 − 200 = 4120.\nRemaining students = 60 − 5 = 55.\nNew mean = 4120 / 55 ≈ 74.91."
    }
]

# Fix Q10 correct answer
sec1[9]["correct_answer"] = "A"
sec1[9]["explanation"] = "Positions 1-7 (left to right). R is at position 4 (middle). P is at an end.\nS is immediate right of P → P must be at position 1, S at position 2.\nQ is immediate left of R → Q at position 3.\nPositions so far: P(1), S(2), Q(3), R(4), _, _, _.\nT is not adjacent to R → T cannot be at position 5. So T is at 6 or 7.\nU sits between T and V → they must be three consecutive positions.\nIf V(5), U(6), T(7): U is between V and T ✓, T is not adjacent to R(4) ✓.\nArrangement: P(1), S(2), Q(3), R(4), V(5), U(6), T(7).\nThe other extreme end (position 7) = T."

# ========================================================================
# SECTION 2: TECHNICAL ABILITY TEST — MATHEMATICAL (10 Qs, 10 Marks, 35 Min)
# ========================================================================
sec2 = [
    {
        "id": 16, "section_id": 2, "topic": "Number Series [HP]", "marks": 1,
        "question": "Find the next number in the series:\n2, 1, 1/2, 1/4, ?",
        "options": {
            "A": "1/3",
            "B": "1/8",
            "C": "1/6",
            "D": "1/16"
        },
        "correct_answer": "B",
        "explanation": "Each term is half (×0.5) of the previous term:\n2 × 0.5 = 1\n1 × 0.5 = 0.5 (= 1/2)\n0.5 × 0.5 = 0.25 (= 1/4)\n0.25 × 0.5 = 0.125 (= 1/8).\nThe next term is 1/8."
    },
    {
        "id": 17, "section_id": 2, "topic": "Number Series [HP]", "marks": 1,
        "question": "What is the next number in the series?\n462, 420, 380, 342, ?",
        "options": {
            "A": "306",
            "B": "312",
            "C": "300",
            "D": "310"
        },
        "correct_answer": "A",
        "explanation": "Differences between consecutive terms:\n462 − 420 = 42\n420 − 380 = 40\n380 − 342 = 38\nThe differences decrease by 2 each time. Next difference = 36.\n342 − 36 = 306."
    },
    {
        "id": 18, "section_id": 2, "topic": "Ratios & Proportions [HP]", "marks": 1,
        "question": "A sum of money is distributed among A, B, C, D in the ratio 5 : 2 : 4 : 3. If C gets ₹1000 more than D, what is B's share?",
        "options": {
            "A": "₹500",
            "B": "₹1500",
            "C": "₹2000",
            "D": "₹2500"
        },
        "correct_answer": "C",
        "explanation": "Let shares be 5x, 2x, 4x, 3x.\nC − D = 4x − 3x = x = ₹1000.\nB's share = 2x = 2 × 1000 = ₹2000."
    },
    {
        "id": 19, "section_id": 2, "topic": "Ratios & Proportions [HP]", "marks": 1,
        "question": "The ratio of ages of A and B is 4 : 3, and the ratio of ages of B and C is 2 : 1. If A's age is 20 years, what is C's age?",
        "options": {
            "A": "5 years",
            "B": "7.5 years",
            "C": "10 years",
            "D": "15 years"
        },
        "correct_answer": "B",
        "explanation": "A : B = 4 : 3. If A = 20, then B = (3/4) × 20 = 15.\nB : C = 2 : 1. If B = 15, then C = 15 / 2 = 7.5 years."
    },
    {
        "id": 20, "section_id": 2, "topic": "Permutation & Combination [HP]", "marks": 1,
        "question": "In how many ways can the letters of the word 'APPLE' be arranged?",
        "options": {
            "A": "120",
            "B": "60",
            "C": "24",
            "D": "48"
        },
        "correct_answer": "B",
        "explanation": "'APPLE' has 5 letters where 'P' repeats twice.\nTotal arrangements = 5! / 2! = 120 / 2 = 60."
    },
    {
        "id": 21, "section_id": 2, "topic": "Permutation & Combination [HP]", "marks": 1,
        "question": "A committee of 5 is to be formed from 6 men and 4 women. In how many ways can this be done if the committee must include at least 2 women?",
        "options": {
            "A": "186",
            "B": "246",
            "C": "252",
            "D": "120"
        },
        "correct_answer": "A",
        "explanation": "At least 2 women means 2W+3M, 3W+2M, or 4W+1M:\n• 2W + 3M: C(4,2) × C(6,3) = 6 × 20 = 120\n• 3W + 2M: C(4,3) × C(6,2) = 4 × 15 = 60\n• 4W + 1M: C(4,4) × C(6,1) = 1 × 6 = 6\nTotal = 120 + 60 + 6 = 186."
    },
    {
        "id": 22, "section_id": 2, "topic": "Time, Speed & Distance [HP]", "marks": 1,
        "question": "A train 125 m long passes a man running at 5 km/hr in the same direction as the train in 10 seconds. What is the speed of the train?",
        "options": {
            "A": "45 km/hr",
            "B": "50 km/hr",
            "C": "54 km/hr",
            "D": "55 km/hr"
        },
        "correct_answer": "B",
        "explanation": "Relative speed (same direction) = Speed of train − Speed of man.\nRelative speed = Distance / Time = 125 / 10 = 12.5 m/s.\nConvert to km/hr: 12.5 × (18/5) = 45 km/hr.\nSpeed of train = Relative speed + Man's speed = 45 + 5 = 50 km/hr."
    },
    {
        "id": 23, "section_id": 2, "topic": "Cryptarithmetic", "marks": 1,
        "question": "In the cryptarithmetic puzzle:\n\n   S E N D\n+  M O R E\n----------\n M O N E Y\n\nEach letter represents a unique digit (0-9). No number begins with 0.\nWhat is the value of M?",
        "options": {
            "A": "0",
            "B": "1",
            "C": "2",
            "D": "3"
        },
        "correct_answer": "B",
        "explanation": "SEND + MORE = MONEY. Since SEND and MORE are 4-digit numbers, their maximum sum is 9999 + 9999 = 19998, a 5-digit number.\nThe carry into the ten-thousands column can only be 1 (since the max carry from adding two single digits plus a carry is 1).\nTherefore, M = 1.\n(Full solution: S=9, E=5, N=6, D=7, M=1, O=0, R=8, Y=2 → 9567 + 1085 = 10652.)"
    },
    {
        "id": 24, "section_id": 2, "topic": "Profit & Loss", "marks": 1,
        "question": "A shopkeeper buys an article for ₹800 and marks it up by 25%. He then offers a discount of 10% on the marked price. What is his profit percentage?",
        "options": {
            "A": "12.5%",
            "B": "10%",
            "C": "15%",
            "D": "12%"
        },
        "correct_answer": "A",
        "explanation": "Cost Price (CP) = ₹800.\nMarked Price (MP) = 800 × 1.25 = ₹1000.\nSelling Price (SP) after 10% discount = 1000 × 0.90 = ₹900.\nProfit = 900 − 800 = ₹100.\nProfit % = (100 / 800) × 100 = 12.5%."
    },
    {
        "id": 25, "section_id": 2, "topic": "Simplification (BODMAS)", "marks": 1,
        "question": "Simplify: 12 + 4 × 3 − 6 ÷ 2",
        "options": {
            "A": "21",
            "B": "22",
            "C": "18",
            "D": "24"
        },
        "correct_answer": "A",
        "explanation": "Following BODMAS/PEMDAS:\n1. Multiplication: 4 × 3 = 12\n2. Division: 6 ÷ 2 = 3\n3. Addition & Subtraction (left to right): 12 + 12 − 3 = 21."
    }
]

# ========================================================================
# SECTION 3: VERBAL ABILITY TEST (20 Qs, 20 Marks, 20 Min)
# ========================================================================

rc_passage = """The Internet of Things (IoT) refers to the network of physical objects embedded with sensors, software, and connectivity that enables them to collect and exchange data. From smart thermostats to wearable health monitors, IoT devices are transforming everyday life. However, the proliferation of connected devices raises significant security and privacy concerns. Many IoT devices lack robust security protocols, making them vulnerable to cyber attacks. Furthermore, the vast amount of data collected by these devices raises questions about data ownership and user privacy. Industry experts argue that standardized security frameworks and regulations are essential to ensure the safe adoption of IoT technology."""

sec3 = [
    # Critical Reasoning [HP] — 3 questions
    {
        "id": 26, "section_id": 3, "topic": "Critical Reasoning [HP]", "marks": 1,
        "question": "Statement: 'A new study claims that regular exercise can significantly reduce the risk of developing Type 2 diabetes.'\n\nWhich of the following, if true, would most STRENGTHEN this argument?",
        "options": {
            "A": "Many people who exercise regularly also follow a strict diet.",
            "B": "A controlled clinical trial showed a 58% reduction in diabetes risk among participants who exercised 150 minutes per week.",
            "C": "Type 2 diabetes is primarily caused by genetic factors.",
            "D": "Some people who exercise regularly still develop diabetes."
        },
        "correct_answer": "B",
        "explanation": "Option B provides direct empirical evidence from a controlled clinical trial showing a specific 58% reduction. This is the strongest form of evidence to support the claim. Option A introduces a confounding variable (diet). Option C weakens the argument. Option D weakens it by providing a counter-example."
    },
    {
        "id": 27, "section_id": 3, "topic": "Critical Reasoning [HP]", "marks": 1,
        "question": "Statement: 'The government should ban all single-use plastic bags to protect the environment.'\n\nWhich of the following is an assumption underlying this statement?",
        "options": {
            "A": "Plastic bags are the only source of environmental pollution.",
            "B": "Single-use plastic bags contribute significantly to environmental damage.",
            "C": "The government has the resources to enforce such a ban.",
            "D": "People will stop using bags entirely."
        },
        "correct_answer": "B",
        "explanation": "For the argument to hold, it must be assumed that single-use plastic bags cause significant environmental harm — otherwise the ban is unjustified. Option A is too extreme (not 'only' source). Options C and D are about implementation, not the core reasoning."
    },
    {
        "id": 28, "section_id": 3, "topic": "Critical Reasoning [HP]", "marks": 1,
        "question": "Statement: 'Sales of electric vehicles have doubled in the last year. Therefore, the government's EV subsidy program is successful.'\n\nWhich of the following, if true, would most WEAKEN this conclusion?",
        "options": {
            "A": "The government increased subsidies by 50% last year.",
            "B": "Gasoline prices tripled during the same period, making conventional cars far more expensive to run.",
            "C": "Electric vehicles have become more stylish and appealing.",
            "D": "More charging stations were built last year."
        },
        "correct_answer": "B",
        "explanation": "If gasoline prices tripled, the surge in EV sales could be attributed to rising fuel costs rather than the subsidy program. This provides an alternative explanation that weakens the causal conclusion that the subsidy was responsible."
    },
    # English Corrective Usage [HP] — 3 questions
    {
        "id": 29, "section_id": 3, "topic": "English Corrective Usage [HP]", "marks": 1,
        "question": "Choose the grammatically correct sentence:",
        "options": {
            "A": "Me and him went to the store.",
            "B": "Him and I went to the store.",
            "C": "He and I went to the store.",
            "D": "I and he went to the store."
        },
        "correct_answer": "C",
        "explanation": "Subject pronouns must be used for the subject of a sentence: 'He' (not 'Him') and 'I' (not 'Me'). Convention places 'I' after other pronouns → 'He and I went to the store.'"
    },
    {
        "id": 30, "section_id": 3, "topic": "English Corrective Usage [HP]", "marks": 1,
        "question": "Choose the correct sentence:",
        "options": {
            "A": "I would have went to the party if I had known.",
            "B": "I would have gone to the party if I had known.",
            "C": "I would had gone to the party if I had known.",
            "D": "I will have gone to the party if I had known."
        },
        "correct_answer": "B",
        "explanation": "Third conditional: 'would have + past participle'. 'Gone' is the past participle of 'go' (not 'went'). 'Would had' is grammatically incorrect. 'Will have' is wrong tense for an unreal past condition."
    },
    {
        "id": 31, "section_id": 3, "topic": "English Corrective Usage [HP]", "marks": 1,
        "question": "Choose the correct sentence:",
        "options": {
            "A": "She don't know nothing about it.",
            "B": "She doesn't know anything about it.",
            "C": "She don't know anything about it.",
            "D": "She doesn't know nothing about it."
        },
        "correct_answer": "B",
        "explanation": "'She' (3rd person singular) requires 'doesn't' (not 'don't'). 'Don't know nothing' is a double negative. The correct form uses 'anything' instead of 'nothing'."
    },
    # English Error Correction [HP] — 3 questions
    {
        "id": 32, "section_id": 3, "topic": "English Error Correction [HP]", "marks": 1,
        "question": "Identify and select the corrected version of the sentence:\n'Each of the students have submitted their assignments on time.'",
        "options": {
            "A": "Each of the students has submitted their assignments on time.",
            "B": "Each of the students have submitted his assignments on time.",
            "C": "Each of the students has submitted his or her assignment on time.",
            "D": "No correction needed."
        },
        "correct_answer": "C",
        "explanation": "'Each' is a singular indefinite pronoun → requires singular verb 'has' (not 'have'), singular possessive 'his or her' (not 'their'), and singular noun 'assignment' (not 'assignments')."
    },
    {
        "id": 33, "section_id": 3, "topic": "English Error Correction [HP]", "marks": 1,
        "question": "Correct the sentence:\n'The data shows that the experiment were successful.'",
        "options": {
            "A": "The data show that the experiment was successful.",
            "B": "The data shows that the experiment was successful.",
            "C": "The datum shows that the experiment were successful.",
            "D": "The data shown that the experiment was successful."
        },
        "correct_answer": "A",
        "explanation": "In formal English, 'data' is the plural of 'datum' and takes plural verb 'show'. 'Experiment' (singular) takes singular verb 'was'. Correct: 'The data show that the experiment was successful.'"
    },
    {
        "id": 34, "section_id": 3, "topic": "English Error Correction [HP]", "marks": 1,
        "question": "Correct the sentence:\n'The committee have made their decision and have announced it yesterday.'",
        "options": {
            "A": "The committee has made its decision and announced it yesterday.",
            "B": "The committee have made its decision and announced it yesterday.",
            "C": "The committee has made their decision and has announced it yesterday.",
            "D": "No correction needed."
        },
        "correct_answer": "A",
        "explanation": "'Committee' (collective noun acting as a unit) takes singular verb 'has' and pronoun 'its'. The action 'announced' pairs with the past-time marker 'yesterday' (simple past), not 'have announced'."
    },
    # English Error Identification — 2 questions
    {
        "id": 35, "section_id": 3, "topic": "English Error Identification", "marks": 1,
        "question": "Identify the part of the sentence that contains a grammatical error:\n'The (A) manager along with his (B) team members were (C) present at the (D) meeting.'",
        "options": {
            "A": "Part A: 'The'",
            "B": "Part B: 'team members'",
            "C": "Part C: 'were'",
            "D": "Part D: 'meeting'"
        },
        "correct_answer": "C",
        "explanation": "When the subject is connected by 'along with', the verb agrees with the primary subject ('manager' — singular). 'Were' (plural) should be 'was' (singular)."
    },
    {
        "id": 36, "section_id": 3, "topic": "English Error Identification", "marks": 1,
        "question": "Identify the part with a grammatical error:\n'(A) Neither the teacher (B) nor the students (C) was present (D) in the classroom.'",
        "options": {
            "A": "Part A",
            "B": "Part B",
            "C": "Part C",
            "D": "Part D"
        },
        "correct_answer": "C",
        "explanation": "In 'neither...nor' constructions, the verb agrees with the subject closest to it ('students' — plural). 'Was' should be 'were'."
    },
    # Reading Comprehension — 4 questions
    {
        "id": 37, "section_id": 3, "topic": "Reading Comprehension", "marks": 1,
        "question": f"{rc_passage}\n\nWhat is the main concern associated with IoT devices according to the passage?",
        "options": {
            "A": "The high cost of IoT devices",
            "B": "Security vulnerabilities and privacy issues",
            "C": "Lack of consumer interest in smart devices",
            "D": "Difficulty in manufacturing IoT components"
        },
        "correct_answer": "B",
        "explanation": "The passage explicitly states that IoT raises 'significant security and privacy concerns' and that devices 'lack robust security protocols, making them vulnerable to cyber attacks.'"
    },
    {
        "id": 38, "section_id": 3, "topic": "Reading Comprehension", "marks": 1,
        "question": f"{rc_passage}\n\nWhat do industry experts recommend to address IoT concerns?",
        "options": {
            "A": "Banning all IoT devices immediately",
            "B": "Reducing the number of connected devices in households",
            "C": "Implementing standardized security frameworks and regulations",
            "D": "Increasing the price of IoT devices to limit adoption"
        },
        "correct_answer": "C",
        "explanation": "The passage states: 'Industry experts argue that standardized security frameworks and regulations are essential to ensure the safe adoption of IoT technology.'"
    },
    {
        "id": 39, "section_id": 3, "topic": "Reading Comprehension (Vocabulary)", "marks": 1,
        "question": f"{rc_passage}\n\nWhat does the word 'proliferation' most closely mean in this context?",
        "options": {
            "A": "Reduction or decline",
            "B": "Rapid increase or widespread growth",
            "C": "Malfunction or failure",
            "D": "Obsolescence or outdating"
        },
        "correct_answer": "B",
        "explanation": "'Proliferation' means a rapid increase in number or extent. In the passage, it refers to the rapidly growing number of connected IoT devices."
    },
    {
        "id": 40, "section_id": 3, "topic": "Reading Comprehension (Detail)", "marks": 1,
        "question": f"{rc_passage}\n\nWhich of the following is an example of an IoT device mentioned in the passage?",
        "options": {
            "A": "Desktop computer",
            "B": "Smart thermostat",
            "C": "Traditional wall clock",
            "D": "Printed newspaper"
        },
        "correct_answer": "B",
        "explanation": "The passage explicitly mentions 'smart thermostats' as an example of IoT devices: 'From smart thermostats to wearable health monitors...'"
    },
    # Para Jumbles — 2 questions
    {
        "id": 41, "section_id": 3, "topic": "Para Jumbles", "marks": 1,
        "question": "Rearrange the following sentences into a logically coherent paragraph:\n\nP. However, it also poses challenges such as data privacy and job displacement.\nQ. Artificial intelligence has become an integral part of modern technology.\nR. Therefore, a balanced approach is needed to harness its benefits responsibly.\nS. It has brought numerous benefits including automation, improved healthcare, and enhanced communication.\n\nChoose the correct sequence:",
        "options": {
            "A": "Q - S - P - R",
            "B": "S - Q - P - R",
            "C": "Q - P - S - R",
            "D": "P - Q - R - S"
        },
        "correct_answer": "A",
        "explanation": "Q introduces the topic (AI in modern tech). S elaborates on benefits. P introduces the contrast ('However'). R concludes with a recommendation ('Therefore'). Logical flow: Q → S → P → R."
    },
    {
        "id": 42, "section_id": 3, "topic": "Para Jumbles", "marks": 1,
        "question": "Rearrange the sentences:\n\nP. This phenomenon is primarily driven by the burning of fossil fuels.\nQ. Global warming refers to the long-term increase in Earth's average surface temperature.\nR. Governments worldwide are implementing policies to reduce carbon emissions.\nS. The resulting greenhouse effect traps heat in the atmosphere.\n\nChoose the correct sequence:",
        "options": {
            "A": "Q - P - S - R",
            "B": "P - Q - S - R",
            "C": "Q - S - P - R",
            "D": "R - Q - P - S"
        },
        "correct_answer": "A",
        "explanation": "Q defines global warming (introduction). P explains the cause (fossil fuels → 'This phenomenon'). S explains the mechanism (greenhouse effect → 'The resulting'). R describes the response (policies). Flow: Q → P → S → R."
    },
    # Synonyms & Antonyms — 3 questions
    {
        "id": 43, "section_id": 3, "topic": "Synonyms", "marks": 1,
        "question": "Choose the word most similar in meaning to 'BENEVOLENT':",
        "options": {
            "A": "Malicious",
            "B": "Kind",
            "C": "Indifferent",
            "D": "Hostile"
        },
        "correct_answer": "B",
        "explanation": "'Benevolent' means well-meaning, kind, and generous. Its synonym is 'Kind'."
    },
    {
        "id": 44, "section_id": 3, "topic": "Antonyms", "marks": 1,
        "question": "Choose the word that is most nearly OPPOSITE in meaning to 'ABUNDANT':",
        "options": {
            "A": "Plentiful",
            "B": "Ample",
            "C": "Scarce",
            "D": "Copious"
        },
        "correct_answer": "C",
        "explanation": "'Abundant' means existing in large quantities/plentiful. Its antonym is 'Scarce' (rare, insufficient)."
    },
    {
        "id": 45, "section_id": 3, "topic": "Synonyms", "marks": 1,
        "question": "Choose the word most similar in meaning to 'PRAGMATIC':",
        "options": {
            "A": "Idealistic",
            "B": "Theoretical",
            "C": "Practical",
            "D": "Abstract"
        },
        "correct_answer": "C",
        "explanation": "'Pragmatic' means dealing with things sensibly and realistically, in a practical way. Its synonym is 'Practical'."
    }
]

# ========================================================================
# SECTION 4: PSEUDOCODE TEST (5 Qs, 10 Marks, 10 Min)
# ========================================================================
sec4 = [
    {
        "id": 46, "section_id": 4, "topic": "Programming Logic [HP]", "marks": 2,
        "question": "What will be the output of the following pseudocode?\n\nInteger a = 5, b = 10, c\nc = a + b\nb = a - b\na = a - b\nPrint a, b",
        "options": {
            "A": "10, -5",
            "B": "10, 5",
            "C": "5, -5",
            "D": "15, -5"
        },
        "correct_answer": "A",
        "explanation": "Step-by-step trace:\n1. c = 5 + 10 = 15\n2. b = 5 - 10 = -5\n3. a = 5 - (-5) = 5 + 5 = 10\nPrint a = 10, b = -5.\nOutput: 10, -5"
    },
    {
        "id": 47, "section_id": 4, "topic": "Loop Tracing (FOR)", "marks": 2,
        "question": "What will be the output?\n\nInteger sum = 0\nFor i = 1 to 5\n    If (i mod 2 != 0)\n        sum = sum + i\n    End If\nEnd For\nPrint sum",
        "options": {
            "A": "6",
            "B": "9",
            "C": "15",
            "D": "10"
        },
        "correct_answer": "B",
        "explanation": "The loop adds only ODD values of i:\ni=1 (odd): sum = 0 + 1 = 1\ni=2 (even): skip\ni=3 (odd): sum = 1 + 3 = 4\ni=4 (even): skip\ni=5 (odd): sum = 4 + 5 = 9\nOutput: 9"
    },
    {
        "id": 48, "section_id": 4, "topic": "Conditional Statements (IF/ELSE)", "marks": 2,
        "question": "What will be the output?\n\nInteger x = 10, y = 20\nIf (x > y)\n    Print x + y\nElse If (x == y)\n    Print x * y\nElse\n    Print y - x\nEnd If",
        "options": {
            "A": "30",
            "B": "200",
            "C": "10",
            "D": "-10"
        },
        "correct_answer": "C",
        "explanation": "x = 10, y = 20.\n• x > y → 10 > 20 → False\n• x == y → 10 == 20 → False\n• Else branch executes: y - x = 20 - 10 = 10.\nOutput: 10"
    },
    {
        "id": 49, "section_id": 4, "topic": "Basic Algorithms (Bubble Sort)", "marks": 2,
        "question": "Consider the following Bubble Sort pseudocode on array arr = [5, 3, 8, 1, 2]:\n\nFor i = 0 to n-2\n    For j = 0 to n-i-2\n        If arr[j] > arr[j+1]\n            Swap arr[j] and arr[j+1]\n        End If\n    End For\nEnd For\n\nWhat will be the state of the array after the FIRST complete pass of the outer loop (i = 0)?",
        "options": {
            "A": "[3, 5, 1, 2, 8]",
            "B": "[1, 2, 3, 5, 8]",
            "C": "[3, 5, 8, 1, 2]",
            "D": "[5, 3, 1, 2, 8]"
        },
        "correct_answer": "A",
        "explanation": "First pass (i=0), inner loop j from 0 to 3:\nj=0: Compare (5,3) → swap → [3, 5, 8, 1, 2]\nj=1: Compare (5,8) → no swap → [3, 5, 8, 1, 2]\nj=2: Compare (8,1) → swap → [3, 5, 1, 8, 2]\nj=3: Compare (8,2) → swap → [3, 5, 1, 2, 8]\nAfter first pass: [3, 5, 1, 2, 8]. The largest element (8) has bubbled to the end."
    },
    {
        "id": 50, "section_id": 4, "topic": "Array & String Manipulation", "marks": 2,
        "question": "What will be the output of the following pseudocode?\n\nString str = \"INFOSYS\"\nString result = \"\"\nFor i = length(str) - 1 downto 0\n    result = result + str[i]\nEnd For\nPrint result",
        "options": {
            "A": "INFOSYS",
            "B": "SYSOFNI",
            "C": "INFSOSY",
            "D": "SYSOIFN"
        },
        "correct_answer": "B",
        "explanation": "The loop iterates from the last character to the first, building the reversed string:\nstr[6]='S', str[5]='Y', str[4]='S', str[3]='O', str[2]='F', str[1]='N', str[0]='I'\nresult = 'S'+'Y'+'S'+'O'+'F'+'N'+'I' = 'SYSOFNI'"
    }
]

# ========================================================================
# SECTION 5: NUMERICAL PUZZLE TEST (4 Qs, 10 Marks, 10 Min)
# ========================================================================
sec5 = [
    {
        "id": 51, "section_id": 5, "topic": "Visual Reasoning [HP]", "marks": 2.5,
        "question": "In a sequence of dot-patterns, each figure adds dots following a triangular number pattern:\n• Figure 1: 1 dot\n• Figure 2: 3 dots\n• Figure 3: 6 dots\n• Figure 4: 10 dots\n\nHow many dots will Figure 7 have?",
        "options": {
            "A": "21",
            "B": "28",
            "C": "36",
            "D": "15"
        },
        "correct_answer": "B",
        "explanation": "This is the triangular number sequence: T(n) = n(n+1)/2.\nT(1) = 1, T(2) = 3, T(3) = 6, T(4) = 10, T(5) = 15, T(6) = 21, T(7) = 28.\nT(7) = 7 × 8 / 2 = 28."
    },
    {
        "id": 52, "section_id": 5, "topic": "Word Puzzle [HP]", "marks": 2.5,
        "question": "Rearrange the letters 'CINERAMA' to form a meaningful English word related to a country's nationality.\n\nWhat is the word?",
        "options": {
            "A": "AMERICAN",
            "B": "CAMERAIN",
            "C": "CREMAINA",
            "D": "MANICERA"
        },
        "correct_answer": "A",
        "explanation": "The letters C, I, N, E, R, A, M, A can be rearranged to form 'AMERICAN' (A, M, E, R, I, C, A, N)."
    },
    {
        "id": 53, "section_id": 5, "topic": "Number Based Pattern [HP]", "marks": 2.5,
        "question": "Find the missing number (?) in the following grid:\n\n[  2   3   10  ]\n[  4   5   26  ]\n[  6   7    ?  ]",
        "options": {
            "A": "50",
            "B": "48",
            "C": "42",
            "D": "55"
        },
        "correct_answer": "A",
        "explanation": "Examine the pattern row by row:\nRow 1: (2 × 3) + 4 = 6 + 4 = 10 ✓\nRow 2: (4 × 5) + 6 = 20 + 6 = 26 ✓\nRow 3: (6 × 7) + 8 = 42 + 8 = 50\n(The addend increases by 2 each row: +4, +6, +8.)\nMissing number = 50."
    },
    {
        "id": 54, "section_id": 5, "topic": "Grid Based Puzzle (Latin Square)", "marks": 2.5,
        "question": "In a 4×4 grid, the numbers 1 to 4 must appear exactly once in each row and each column. Given the partially filled grid:\n\nRow 1: [ 1,  _,  _,  4 ]\nRow 2: [ _,  3,  _,  _ ]\nRow 3: [ _,  _,  1,  _ ]\nRow 4: [ 4,  _,  _,  2 ]\n\nWhat number goes in Row 1, Column 2?",
        "options": {
            "A": "2",
            "B": "3",
            "C": "4",
            "D": "1"
        },
        "correct_answer": "A",
        "explanation": "Row 1 already has 1 and 4 → needs 2 and 3.\nColumn 2 already has 3 (from Row 2) → Column 2 cannot have 3 again.\nTherefore, Row 1, Column 2 = 2."
    }
]

# ========================================================================
# SECTION 6: ENGLISH GRAMMAR TEST (5 Qs, 10 Marks, 10 Min)
# ========================================================================
sec6 = [
    {
        "id": 55, "section_id": 6, "topic": "Tenses [HP]", "marks": 2,
        "question": "Choose the grammatically correct sentence:",
        "options": {
            "A": "She has been working here since five years.",
            "B": "She has been working here for five years.",
            "C": "She is working here since five years.",
            "D": "She was working here for five years."
        },
        "correct_answer": "B",
        "explanation": "Present perfect continuous tense uses:\n• 'for' + duration of time (e.g., 'for five years')\n• 'since' + point in time (e.g., 'since 2021')\n'Five years' is a duration → 'for' is correct. The sentence describes an action continuing from the past to now → present perfect continuous ('has been working') is correct."
    },
    {
        "id": 56, "section_id": 6, "topic": "Subject-Verb Agreement [HP]", "marks": 2,
        "question": "Choose the correct option to fill the blank:\n'The team of players ______ ready for the tournament.'",
        "options": {
            "A": "are",
            "B": "is",
            "C": "were",
            "D": "have been"
        },
        "correct_answer": "B",
        "explanation": "'The team' is a collective noun acting as a single unit. The prepositional phrase 'of players' is a modifier and does not change the subject. A singular collective noun takes a singular verb → 'is'."
    },
    {
        "id": 57, "section_id": 6, "topic": "Articles & Prepositions", "marks": 2,
        "question": "Fill in the blanks:\n'She is ___ honest woman and she believes ___ hard work.'",
        "options": {
            "A": "a, on",
            "B": "an, in",
            "C": "an, on",
            "D": "the, in"
        },
        "correct_answer": "B",
        "explanation": "'Honest' begins with a vowel sound (/ɒnɪst/ — the 'h' is silent), so the article 'an' is used.\n'Believes in' is the standard prepositional collocation (not 'believes on').\nCorrect: 'an, in'."
    },
    {
        "id": 58, "section_id": 6, "topic": "Active & Passive Voice", "marks": 2,
        "question": "Convert to passive voice:\n'The manager will complete the project by Friday.'",
        "options": {
            "A": "The project will be completed by the manager by Friday.",
            "B": "The project will completed by the manager by Friday.",
            "C": "The project would be completed by the manager by Friday.",
            "D": "The project is completed by the manager by Friday."
        },
        "correct_answer": "A",
        "explanation": "Active: Subject + will + V1 + Object.\nPassive: Object + will be + V3 (past participle) + by + Subject.\n'The project will be completed by the manager by Friday.'\nOption B omits 'be'. Option C uses 'would' (wrong tense). Option D uses present tense."
    },
    {
        "id": 59, "section_id": 6, "topic": "Direct & Indirect Speech", "marks": 2,
        "question": "Convert to indirect speech:\nHe said, 'I am going to the market.'",
        "options": {
            "A": "He said that he is going to the market.",
            "B": "He said that he was going to the market.",
            "C": "He said that he had been going to the market.",
            "D": "He told that he was going to the market."
        },
        "correct_answer": "B",
        "explanation": "Rules for converting direct to indirect speech:\n• 'I' changes to 'he' (matching the subject).\n• 'am going' (present continuous) backshifts to 'was going' (past continuous).\n• Reporting verb 'said' remains and is followed by 'that'.\n• 'Told' requires an object (e.g., 'told him'), so Option D is wrong.\nCorrect: 'He said that he was going to the market.'"
    }
]

# ========================================================================
# SECTION 7: ENGLISH WRITING TEST (1 Question, Evaluated Separately)
# ========================================================================
sec7 = [
    {
        "id": 60, "section_id": 7, "topic": "Essay / Email Writing [HP]", "marks": 0,
        "is_essay": True,
        "word_limit_min": 150,
        "word_limit_max": 250,
        "question": "Topic: 'Remote Work vs. Office Work — Advantages, Challenges, and the Future of Hybrid Models.'\n\nPrompt:\nDraft a well-structured essay or formal corporate memo (150 - 250 words) addressing:\n1. The key advantages and disadvantages of remote working.\n2. How it affects employee productivity, collaboration, and work-life balance.\n3. Your recommendation on whether companies should adopt a hybrid model and why.",
        "sample_high_scoring_response": "The global shift toward remote work, catalyzed by the COVID-19 pandemic, has fundamentally transformed organizational workforce strategies. Remote work offers significant advantages: employees enjoy enhanced work-life balance, elimination of commuting costs, and greater scheduling flexibility. Studies consistently demonstrate that focused, individual tasks often see productivity gains in remote settings.\n\nHowever, remote work introduces notable challenges. Spontaneous collaboration, mentorship, and cross-functional innovation frequently diminish when teams operate in isolation. Prolonged remote work can also foster social disconnection, burnout from blurred professional-personal boundaries, and communication inefficiencies across time zones.\n\nConsequently, a hybrid model — combining structured in-office days with remote flexibility — represents the most pragmatic solution for modern enterprises. Organizations should mandate two to three in-office collaboration days per week for team syncs, brainstorming sessions, and cultural bonding, while preserving remote days for deep, focused work. This balanced approach maximizes both productivity and employee satisfaction while maintaining organizational cohesion.\n\nIn conclusion, rather than choosing exclusively between remote and office paradigms, enterprises should strategically adopt hybrid frameworks that leverage the distinct strengths of both models.",
        "evaluation_criteria": [
            "Coherence & Logical Flow: Clear introduction, body, and conclusion.",
            "Vocabulary & Lexical Resource: Professional terminology and varied sentence structures.",
            "Grammar & Sentence Variety: Correct tense, complex sentences, no errors.",
            "Relevance & Prompt Adherence: All three prompt points addressed within word limit."
        ],
        "explanation": "This is an essay question evaluated qualitatively on structure, grammar, vocabulary, and relevance. See the benchmark model answer and evaluation criteria above."
    }
]

# Assemble all
data["questions"] = sec1 + sec2 + sec3 + sec4 + sec5 + sec6 + sec7

with open('questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

with open('questions.js', 'w', encoding='utf-8') as f:
    f.write('const TEST_DATA = ' + json.dumps(data, indent=2, ensure_ascii=False) + ';\n')

print(f"Total questions: {len(data['questions'])}")
for s in data['sections']:
    cnt = len([q for q in data['questions'] if q['section_id'] == s['id']])
    print(f"  Section {s['id']} ({s['name']}): {cnt} questions (expected {s['total_questions']})")
