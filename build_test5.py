import json
import os

questions = [
    {
        "id": 1, "section_id": 1, "topic": "Data Sufficiency", "marks": 1,
        "question": "Is x > 0?\nStatement I: x^2 = 4\nStatement II: x^3 = 8",
        "options": {"A": "Statement I alone is sufficient", "B": "Statement II alone is sufficient", "C": "Both statements together are sufficient", "D": "Neither statement is sufficient"},
        "correct_answer": "B",
        "explanation": "From Stmt I: x = 2 or x = -2. Not sufficient. From Stmt II: x = 2. Since 2 > 0, Stmt II alone is sufficient."
    },
    {
        "id": 2, "section_id": 1, "topic": "Data Sufficiency", "marks": 1,
        "question": "What is the area of the circle?\nStatement I: circumference = 44\nStatement II: diameter = 14",
        "options": {"A": "Statement I alone is sufficient", "B": "Statement II alone is sufficient", "C": "Either Statement alone is sufficient", "D": "Both statements together are needed"},
        "correct_answer": "C",
        "explanation": "From I: 2 * pi * r = 44 => r = 7. Area = pi * r^2. Sufficient. From II: 2r = 14 => r = 7. Area = pi * r^2. Sufficient. Either alone is sufficient."
    },
    {
        "id": 3, "section_id": 1, "topic": "Data Interpretation", "marks": 1,
        "question": "Table shows population (in thousands) of 4 cities in 4 years:\nCity A: 2021(100) -> 2024(120)\nCity B: 2021(150) -> 2024(180)\nCity C: 2021(50) -> 2024(65)\nCity D: 2021(200) -> 2024(230)\nWhich city had the maximum % growth from 2021 to 2024?",
        "options": {"A": "City A", "B": "City B", "C": "City C", "D": "City D"},
        "correct_answer": "C",
        "explanation": "Growth %: A = 20/100 = 20%. B = 30/150 = 20%. C = 15/50 = 30%. D = 30/200 = 15%. Max is C (30%)."
    },
    {
        "id": 4, "section_id": 1, "topic": "Data Interpretation", "marks": 1,
        "question": "Using the same population data, if City C had 10% of its 2024 population leave due to a crisis, find its new population (in thousands).",
        "options": {"A": "58.5", "B": "60", "C": "55", "D": "59.5"},
        "correct_answer": "A",
        "explanation": "2024 population of City C = 65. 10% of 65 = 6.5. New population = 65 - 6.5 = 58.5."
    },
    {
        "id": 5, "section_id": 1, "topic": "Syllogisms", "marks": 1,
        "question": "Statements:\n1. All P are Q.\n2. No Q is R.\n3. Some R are S.\n4. All S are T.\nConclusions:\nI. Some P are R\nII. Some T are R",
        "options": {"A": "Only I follows", "B": "Only II follows", "C": "Both I and II follow", "D": "Neither I nor II follows"},
        "correct_answer": "B",
        "explanation": "Since All P are Q and No Q is R, No P is R. So I is false. Since Some R are S and All S are T, Some R are T, which implies Some T are R. So II is true."
    },
    {
        "id": 6, "section_id": 1, "topic": "Syllogisms", "marks": 1,
        "question": "Statements:\n1. All P are Q.\n2. No Q is R.\n3. Some R are S.\n4. All S are T.\nConclusions:\nI. No P is S\nII. Some T are not Q",
        "options": {"A": "Only I follows", "B": "Only II follows", "C": "Both I and II follow", "D": "Neither I nor II follows"},
        "correct_answer": "B",
        "explanation": "I: No P is S is a possibility but not definite (R and S overlap, S could overlap with P? Wait, P is inside Q, and No Q is R. S overlaps with R. The part of S outside R could overlap with Q and P. So No P is S is not definite). II: Some T are R (from Some R are S and All S are T). And No R is Q. Therefore, the T that are R cannot be Q. Hence Some T are not Q is true."
    },
    {
        "id": 7, "section_id": 1, "topic": "Coding-Decoding", "marks": 1,
        "question": "In a certain code language, each letter is shifted forward by its alphabetical position. For example, A (1st letter) shifts by 1 to become B. B (2nd letter) shifts by 2 to become D. What will be the code for 'BDFI'?",
        "options": {"A": "DHMQ", "B": "DHLR", "C": "CGKQ", "D": "DHNP"},
        "correct_answer": "B",
        "explanation": "B is 2nd letter -> shift by 2 = D (4).\nD is 4th letter -> shift by 4 = H (8).\nF is 6th letter -> shift by 6 = L (12).\nI=9+9=18(R). Code: DHLR."
    },
    {
        "id": 8, "section_id": 1, "topic": "Blood Relations", "marks": 1,
        "question": "A is B's mother. C is A's sister. D is C's son. E is D's wife. F is E's mother. G is B's father. How is G related to C?",
        "options": {"A": "Brother", "B": "Brother-in-law", "C": "Uncle", "D": "Cousin"},
        "correct_answer": "B",
        "explanation": "A is B's mother, G is B's father => A and G are married. C is A's sister. Therefore, G is the husband of C's sister, making G the brother-in-law of C."
    },
    {
        "id": 9, "section_id": 1, "topic": "Directional Sense", "marks": 1,
        "question": "A man starts walking North and goes 3km. He turns left and walks 4km. He turns left again and walks 2km. He turns right and walks 1km. What is his straight-line distance from the starting point?",
        "options": {"A": "4km", "B": "5.1km", "C": "5km", "D": "6.2km"},
        "correct_answer": "B",
        "explanation": "Start at (0,0). North 3km -> (0,3). Left (West) 4km -> (-4,3). Left (South) 2km -> (-4,1). Right (West) 1km -> (-5,1). Distance = sqrt((-5-0)^2 + (1-0)^2) = sqrt(25 + 1) = sqrt(26) ~ 5.099 ~ 5.1km."
    },
    {
        "id": 10, "section_id": 1, "topic": "Seating Arrangement", "marks": 1,
        "question": "10 people sit around a circular table facing the center. A sits opposite B. C sits two places to the right of A. D sits opposite C. E sits to the immediate right of B. Who sits to the immediate left of D?",
        "options": {"A": "A", "B": "B", "C": "E", "D": "Cannot be determined"},
        "correct_answer": "C",
        "explanation": "Assume A=1. Right of A is anti-clockwise => C=9. D opposite C => D=4. Left of D (4) is 5. But B=6, E is right of B => E=5. So left of D is E."
    },
    {
        "id": 11, "section_id": 1, "topic": "Seating Arrangement", "marks": 1,
        "question": "Using the same arrangement (A opposite B, C two places right of A, D opposite C, E immediate right of B), what is the position of E with respect to A?",
        "options": {"A": "4th to the right", "B": "4th to the left", "C": "3rd to the right", "D": "3rd to the left"},
        "correct_answer": "B",
        "explanation": "A=1, B=6. Right is anti-clockwise. C=9. D=4. E=5. E is at 5. A is at 1. Clockwise from 1 to 5 is 4 places. Clockwise is left. So E is 4th to the left of A."
    },
    {
        "id": 12, "section_id": 1, "topic": "Logical Deduction", "marks": 1,
        "question": "Argument: 'Should voting be made compulsory?'\n1. Yes, it will ensure that the government truly represents the people.\n2. No, it violates the fundamental right of freedom of choice.\nWhich arguments are strong?",
        "options": {"A": "Only 1", "B": "Only 2", "C": "Both 1 and 2", "D": "Neither 1 nor 2"},
        "correct_answer": "C",
        "explanation": "Both arguments touch upon vital constitutional and democratic principles. Argument 1 focuses on true representation, while Argument 2 focuses on individual liberty. Both are strong and logically connected to the premise."
    },
    {
        "id": 13, "section_id": 1, "topic": "Logical Deduction", "marks": 1,
        "question": "Given 3 statements:\n1. All machines consume energy.\n2. Some machines are highly efficient.\n3. Everything that consumes energy produces heat.\nWhich conclusion DEFINITELY follows?",
        "options": {"A": "Highly efficient machines produce less heat", "B": "All machines produce heat", "C": "Some heat-producing things do not consume energy", "D": "No efficient thing produces heat"},
        "correct_answer": "B",
        "explanation": "From 1 and 3: All machines consume energy + Everything that consumes energy produces heat => All machines produce heat. A is plausible but not strictly proven. C is possible but not definitely proven. D is false."
    },
    {
        "id": 14, "section_id": 1, "topic": "Statistical DI", "marks": 1,
        "question": "A distribution has Mean = 65, Median = 70, Mode = 75. The distribution is:",
        "options": {"A": "Positively skewed", "B": "Negatively skewed", "C": "Symmetric", "D": "Cannot be determined"},
        "correct_answer": "B",
        "explanation": "When Mean < Median < Mode (65 < 70 < 75), the tail is pulled towards the left (lower values). This indicates a negatively skewed (left-skewed) distribution."
    },
    {
        "id": 15, "section_id": 1, "topic": "Ranking Puzzle", "marks": 1,
        "question": "Five friends are ranked by height. A > B, C > D, D > B, and E is between A and C. Who is 3rd in height?",
        "options": {"A": "E", "B": "D", "C": "A", "D": "Cannot be determined"},
        "correct_answer": "D",
        "explanation": "C > D > B. A > B. E is between A and C (A > E > C or C > E > A). If C > E > A > D > B, 3rd is A. If A > E > C > D > B, 3rd is C. Since the exact position is ambiguous, it cannot be determined."
    },
    
    # Section 2 (IDs 16-25)
    {
        "id": 16, "section_id": 2, "topic": "Number Series", "marks": 1,
        "question": "Find the next number in the series: 2, 5, 10, 17, 26, 37, ?",
        "options": {"A": "48", "B": "49", "C": "50", "D": "51"},
        "correct_answer": "C",
        "explanation": "The differences between consecutive terms are 3, 5, 7, 9, 11. These are consecutive odd numbers. The next difference is 13. So, 37 + 13 = 50."
    },
    {
        "id": 17, "section_id": 2, "topic": "Number Series", "marks": 1,
        "question": "Find the next number in the series: 3, 7, 13, 21, 31, 43, ?",
        "options": {"A": "55", "B": "56", "C": "57", "D": "59"},
        "correct_answer": "C",
        "explanation": "The differences are 4, 6, 8, 10, 12. The next difference is 14. So, 43 + 14 = 57."
    },
    {
        "id": 18, "section_id": 2, "topic": "Averages/Mixtures", "marks": 1,
        "question": "Three varieties of tea costing ₹80, ₹100, and ₹120 per kg are mixed in the ratio 2:3:1. Find the average cost of the mixture per kg.",
        "options": {"A": "₹95", "B": "₹96.67", "C": "₹98", "D": "₹100"},
        "correct_answer": "B",
        "explanation": "Total cost = (80 * 2) + (100 * 3) + (120 * 1) = 160 + 300 + 120 = 580. Total weight = 2 + 3 + 1 = 6. Average cost = 580 / 6 = 96.666... ~ ₹96.67."
    },
    {
        "id": 19, "section_id": 2, "topic": "Permutation & Combination", "marks": 1,
        "question": "How many 4-digit numbers can be formed using digits 1, 2, 3, 4, 5 without repetition such that the number is divisible by 4?",
        "options": {"A": "12", "B": "24", "C": "36", "D": "48"},
        "correct_answer": "B",
        "explanation": "A number is divisible by 4 if its last two digits are. Possible last two digits from {1,2,3,4,5} without repetition: 12, 24, 32, 52 (4 possibilities). For each, there are 2 digits used, leaving 3 digits for the first two positions. Number of ways for first two positions = 3P2 = 6. Total numbers = 4 * 6 = 24."
    },
    {
        "id": 20, "section_id": 2, "topic": "Probability", "marks": 1,
        "question": "Two cards are drawn at random from a well-shuffled pack of 52 cards. What is the probability that both cards are of the same suit?",
        "options": {"A": "1/4", "B": "4/17", "C": "12/51", "D": "1/13"},
        "correct_answer": "C",
        "explanation": "Number of ways to choose 2 cards of same suit = 4 * C(13,2) = 4 * (13 * 12) / 2 = 312. Total ways = C(52,2) = (52 * 51) / 2 = 1326. Probability = 312 / 1326 = 12 / 51."
    },
    {
        "id": 21, "section_id": 2, "topic": "Time, Speed & Distance", "marks": 1,
        "question": "Train A starts at 8 AM at 60 kmph. Train B starts at 9 AM from the same station and in the same direction at 80 kmph. At what time does B overtake A?",
        "options": {"A": "11:00 AM", "B": "12:00 PM", "C": "1:00 PM", "D": "11:30 AM"},
        "correct_answer": "B",
        "explanation": "By 9 AM, Train A has travelled 60 km. The relative speed of B with respect to A is 80 - 60 = 20 kmph. Time taken for B to cover the 60 km gap = 60 / 20 = 3 hours. 9 AM + 3 hours = 12:00 PM."
    },
    {
        "id": 22, "section_id": 2, "topic": "Cryptarithmetic", "marks": 1,
        "question": "In the cryptarithmetic problem IN + IN = TO, each distinct letter represents a unique digit from 0-9. Find T + O given that all digits are distinct and I, T != 0.",
        "options": {"A": "10", "B": "12", "C": "13", "D": "15"},
        "correct_answer": "C",
        "explanation": "Let I=3, N=8. IN=38. 38 + 38 = 76. T=7, O=6. All letters (I=3, N=8, T=7, O=6) are unique. T+O = 7+6 = 13. Other combinations like I=4, N=7 -> 47+47=94 (T=9, O=4) conflicts because O and I cannot share digits? No, O=4 and I=4 conflict. So I=3, N=8 is uniquely working among early values. T+O = 13."
    },
    {
        "id": 23, "section_id": 2, "topic": "Compound Interest", "marks": 1,
        "question": "The compound interest on ₹8000 for 2 years is ₹1640. Find the approximate rate of interest per annum.",
        "options": {"A": "9%", "B": "10%", "C": "11%", "D": "12%"},
        "correct_answer": "B",
        "explanation": "Amount = 8000 + 1640 = 9640. Amount = P(1 + r/100)^2. 9640/8000 = 1.205. (1 + r/100)^2 = 1.205. sqrt(1.205) ~ 1.0977. So r ~ 9.77%. The closest option is 10%."
    },
    {
        "id": 24, "section_id": 2, "topic": "LCM Applications", "marks": 1,
        "question": "Three lighthouses flash every 8s, 12s, and 18s respectively. If they all flash together at t=0, how many times do they flash together in 3 minutes (including the flash at t=0)?",
        "options": {"A": "2", "B": "3", "C": "4", "D": "5"},
        "correct_answer": "B",
        "explanation": "LCM of 8, 12, 18 is 72 seconds. In 3 minutes (180 seconds), they will flash together at 72s and 144s. Total flashes = at t=0, t=72, t=144. So 3 times."
    },
    {
        "id": 25, "section_id": 2, "topic": "Time & Work", "marks": 1,
        "question": "Tap A fills a tank in 6 hours, Tap B fills it in 8 hours, and Tap C drains it in 4 hours. If all three are opened simultaneously, how long will it take to fill the tank?",
        "options": {"A": "18 hours", "B": "20 hours", "C": "24 hours", "D": "The tank will never fill"},
        "correct_answer": "C",
        "explanation": "Net filling rate = (1/6) + (1/8) - (1/4) = (4/24) + (3/24) - (6/24) = 1/24 per hour. It will take 24 hours to fill the tank."
    },
    
    # Section 3 (IDs 26-45)
    {
        "id": 26, "section_id": 3, "topic": "Critical Reasoning", "marks": 1,
        "question": "Argument: 'Switching to electric vehicles (EVs) reduces urban air pollution significantly.' Which of the following, if true, most weakens this argument?",
        "options": {"A": "EVs are generally more expensive to purchase than gas cars.", "B": "Most electricity used to charge EVs in urban areas comes from coal-fired power plants located within the same city.", "C": "EV battery production is environmentally damaging.", "D": "Urban residents prefer public transit over driving."},
        "correct_answer": "B",
        "explanation": "If the electricity for EVs comes from coal plants located WITHIN the city, then the pollution is simply shifted from tailpipes to power plants, meaning urban air pollution isn't significantly reduced."
    },
    {
        "id": 27, "section_id": 3, "topic": "Critical Reasoning", "marks": 1,
        "question": "Argument: 'People who drink 3 cups of coffee a day have lower risks of heart disease.' Which is a potential confounding variable (introducing a new variable) that weakens the causality?",
        "options": {"A": "Coffee contains caffeine.", "B": "People who drink 3 cups of coffee tend to have higher incomes, allowing for better healthcare.", "C": "Tea drinkers also have low risks.", "D": "Drinking 5 cups of coffee increases heart risks."},
        "correct_answer": "B",
        "explanation": "Option B introduces income and better healthcare as a new variable, suggesting the correlation between coffee and health might actually be due to wealth rather than the coffee itself."
    },
    {
        "id": 28, "section_id": 3, "topic": "Critical Reasoning", "marks": 1,
        "question": "Which statement most strengthens the claim: 'Remote work increases overall employee productivity'?",
        "options": {"A": "Remote workers save money on commuting.", "B": "Companies save on office lease costs.", "C": "Studies show remote workers spend 15% more time on focused tasks without office interruptions.", "D": "Some employees feel isolated at home."},
        "correct_answer": "C",
        "explanation": "Option C directly provides evidence linking remote work to higher productivity (more time on focused tasks)."
    },
    {
        "id": 29, "section_id": 3, "topic": "Corrective Usage", "marks": 1,
        "question": "Choose the correct phrasing:\n___ the severity of the storm, they would have evacuated earlier.",
        "options": {"A": "If they knew", "B": "Had they known", "C": "If they would have known", "D": "Did they know"},
        "correct_answer": "B",
        "explanation": "'Had they known' is the correct inverted conditional form for 'If they had known', required for the past perfect conditional."
    },
    {
        "id": 30, "section_id": 3, "topic": "Corrective Usage", "marks": 1,
        "question": "Choose the correct phrase:\nNo sooner had the manager announced the layoffs ___ the employees started protesting.",
        "options": {"A": "when", "B": "than", "C": "then", "D": "that"},
        "correct_answer": "B",
        "explanation": "The phrase 'no sooner' is always paired with 'than'."
    },
    {
        "id": 31, "section_id": 3, "topic": "Corrective Usage", "marks": 1,
        "question": "Choose the correct phrase:\nIt is high time you ___ making excuses and started working.",
        "options": {"A": "stop", "B": "stopped", "C": "should stop", "D": "have stopped"},
        "correct_answer": "B",
        "explanation": "The expression 'It is high time' is followed by a subject and a verb in the past subjunctive (or past simple) form, hence 'stopped'."
    },
    {
        "id": 32, "section_id": 3, "topic": "Error Correction", "marks": 1,
        "question": "Find the error in the sentence:\nNot only the students but also the teacher were excited about the field trip.",
        "options": {"A": "Not only the students", "B": "but also the teacher", "C": "were excited", "D": "about the field trip"},
        "correct_answer": "C",
        "explanation": "In 'not only... but also' constructions, the verb agrees with the subject closer to it. 'The teacher' is singular, so it should be 'was excited'."
    },
    {
        "id": 33, "section_id": 3, "topic": "Error Correction", "marks": 1,
        "question": "Find the error in the sentence:\nI would rather prefer reading a good book than watching a movie.",
        "options": {"A": "rather prefer reading", "B": "a good book", "C": "than watching", "D": "No error"},
        "correct_answer": "A",
        "explanation": "'Prefer' and 'rather' are redundant when used together. Also, 'prefer' takes 'to', not 'than'. The correct phrasing could be 'I prefer reading to watching' or 'I would rather read than watch'."
    },
    {
        "id": 34, "section_id": 3, "topic": "Error Correction", "marks": 1,
        "question": "Find the error in the sentence:\nThe reason he failed the exam is because he did not study enough.",
        "options": {"A": "The reason he failed", "B": "the exam is", "C": "because he did not", "D": "study enough"},
        "correct_answer": "C",
        "explanation": "The phrase 'The reason is' should be followed by 'that', not 'because'. So it should be 'The reason is that he did not study'."
    },
    {
        "id": 35, "section_id": 3, "topic": "Error ID", "marks": 1,
        "question": "Identify the error in the sentence:\nWalking down the street, the trees looked beautiful in the autumn sun.",
        "options": {"A": "Walking down the street", "B": "the trees looked", "C": "beautiful in", "D": "the autumn sun"},
        "correct_answer": "A",
        "explanation": "This is a dangling modifier. 'Walking down the street' modifies 'the trees', implying the trees were walking. It should be 'As I was walking down the street, the trees...'"
    },
    {
        "id": 36, "section_id": 3, "topic": "Error ID", "marks": 1,
        "question": "Identify the redundancy error in the sentence:\nThe CEO reiterated again the company's commitment to absolute perfection.",
        "options": {"A": "The CEO reiterated", "B": "reiterated again", "C": "commitment to", "D": "absolute perfection"},
        "correct_answer": "B",
        "explanation": "'Reiterate' means to say something again. Adding 'again' is redundant."
    },
    {
        "id": 37, "section_id": 3, "topic": "Reading Comprehension", "marks": 1,
        "question": "Read the passage:\nBehavioral economics integrates psychology with economic theory, challenging the assumption that individuals always act rationally. Pioneers like Daniel Kahneman have demonstrated that humans are prone to cognitive biases. One prominent example is 'loss aversion,' where the pain of losing $50 is psychologically more severe than the joy of gaining $50. Another is the 'anchoring bias,' which occurs when individuals rely too heavily on the first piece of information offered (the 'anchor') when making decisions. For instance, the initial price offered for a used car sets the standard for the rest of the negotiations, often skewing the final price. These heuristics, while evolutionarily advantageous in fast-paced scenarios, often lead to systematic errors in modern financial planning. Consequently, understanding these biases is crucial for policymakers aiming to design 'nudges' that guide citizens toward better financial health without restricting their freedom of choice.\n\nAccording to the passage, what is the primary consequence of cognitive biases in the modern world?",
        "options": {"A": "They make individuals strictly rational.", "B": "They cause systematic errors in financial planning.", "C": "They lead to evolutionary disadvantages.", "D": "They eliminate freedom of choice."},
        "correct_answer": "B",
        "explanation": "The passage explicitly states that these heuristics (biases) 'often lead to systematic errors in modern financial planning'."
    },
    {
        "id": 38, "section_id": 3, "topic": "Reading Comprehension", "marks": 1,
        "question": "Based on the passage, how would a car salesperson use the 'anchoring bias' to their advantage?",
        "options": {"A": "By refusing to negotiate the price.", "B": "By showing the buyer cheaper cars first.", "C": "By initially quoting an artificially high price for the vehicle.", "D": "By highlighting the possibility of losing a good deal."},
        "correct_answer": "C",
        "explanation": "Anchoring bias relies on the 'first piece of information offered'. By setting an artificially high initial price (anchor), the salesperson skews the rest of the negotiations upward."
    },
    {
        "id": 39, "section_id": 3, "topic": "Reading Comprehension", "marks": 1,
        "question": "Which of the following can be inferred about 'nudges' as mentioned in the passage?",
        "options": {"A": "They strictly mandate financial behaviors.", "B": "They are designed to exploit cognitive biases for corporate profit.", "C": "They help overcome cognitive biases while preserving free will.", "D": "They eliminate the need for behavioral economics."},
        "correct_answer": "C",
        "explanation": "The passage states that nudges 'guide citizens toward better financial health without restricting their freedom of choice', meaning they preserve free will while correcting biases."
    },
    {
        "id": 40, "section_id": 3, "topic": "Reading Comprehension", "marks": 1,
        "question": "What is the author's primary purpose in writing this passage?",
        "options": {"A": "To criticize Kahneman's theories.", "B": "To explain cognitive biases and their implications for decision-making and policy.", "C": "To argue that humans are fundamentally irrational and need strict regulations.", "D": "To teach readers how to negotiate when buying a car."},
        "correct_answer": "B",
        "explanation": "The passage objectively explains behavioral economics, specific biases like loss aversion and anchoring, and concludes with their relevance to policy design (nudges)."
    },
    {
        "id": 41, "section_id": 3, "topic": "Para Jumbles", "marks": 1,
        "question": "Rearrange the sentences:\n1. This means that a large part of the population relies on agriculture.\n2. India is primarily an agrarian economy.\n3. However, the sector's contribution to the GDP is disproportionately low.\n4. Therefore, modernizing farming techniques is essential.\n5. They depend on it for their livelihood and sustenance.",
        "options": {"A": "2, 1, 5, 3, 4", "B": "2, 5, 1, 3, 4", "C": "1, 5, 2, 3, 4", "D": "2, 1, 3, 5, 4"},
        "correct_answer": "A",
        "explanation": "2 introduces the topic. 1 elaborates on 'agrarian economy'. 5 ('They') refers to the population in 1. 3 introduces the contrast (low GDP contribution). 4 gives the conclusion. Hence 2-1-5-3-4."
    },
    {
        "id": 42, "section_id": 3, "topic": "Para Jumbles", "marks": 1,
        "question": "Rearrange the sentences:\n1. He finally managed to catch the last train.\n2. John overslept and missed his alarm.\n3. Exhausted but relieved, he reached his destination.\n4. Consequently, he had to rush to the station.\n5. The traffic on the way only made his panic worse.",
        "options": {"A": "2, 5, 4, 1, 3", "B": "2, 4, 5, 1, 3", "C": "2, 1, 4, 5, 3", "D": "4, 2, 5, 1, 3"},
        "correct_answer": "B",
        "explanation": "2 starts the story (overslept). 4 follows (rushed). 5 adds conflict (traffic). 1 is the climax (caught the train). 3 is the resolution. Hence 2-4-5-1-3."
    },
    {
        "id": 43, "section_id": 3, "topic": "Synonyms/Antonyms", "marks": 1,
        "question": "Choose the synonym for OBFUSCATE:",
        "options": {"A": "Clarify", "B": "Confuse", "C": "Illuminate", "D": "Simplify"},
        "correct_answer": "B",
        "explanation": "To obfuscate means to render obscure, unclear, or unintelligible. The closest synonym is 'confuse'."
    },
    {
        "id": 44, "section_id": 3, "topic": "Synonyms/Antonyms", "marks": 1,
        "question": "Choose the antonym for MAGNANIMOUS:",
        "options": {"A": "Petty", "B": "Generous", "C": "Noble", "D": "Brave"},
        "correct_answer": "A",
        "explanation": "Magnanimous means very generous or forgiving. Its antonym is 'petty' or mean-spirited."
    },
    {
        "id": 45, "section_id": 3, "topic": "Synonyms/Antonyms", "marks": 1,
        "question": "Choose the synonym for PERFIDIOUS:",
        "options": {"A": "Loyal", "B": "Treacherous", "C": "Brave", "D": "Honest"},
        "correct_answer": "B",
        "explanation": "Perfidious means deceitful and untrustworthy. The closest synonym is 'treacherous'."
    },
    
    # Section 4 (IDs 46-50)
    {
        "id": 46, "section_id": 4, "topic": "Pseudocode", "marks": 2,
        "question": "Consider the following pseudocode:\ncount = 0\nfor i = 1 to 6\n  if i MOD 2 != 0\n    for j = 1 to i\n      count = count + 1\nprint count\nWhat will be the output?",
        "options": {"A": "9", "B": "12", "C": "15", "D": "21"},
        "correct_answer": "A",
        "explanation": "Outer loop runs for i=1 to 6. Inner loop runs only if i is odd (i.e., i=1, 3, 5). For i=1, j runs 1 time. For i=3, j runs 3 times. For i=5, j runs 5 times. Total count = 1 + 3 + 5 = 9."
    },
    {
        "id": 47, "section_id": 4, "topic": "Pseudocode", "marks": 2,
        "question": "The Tower of Hanoi problem can be solved recursively. The number of moves required for 'n' disks is given by M(n) = 2 * M(n-1) + 1, with M(1) = 1. How many moves are required for 4 disks?",
        "options": {"A": "7", "B": "11", "C": "15", "D": "17"},
        "correct_answer": "C",
        "explanation": "M(1) = 1. M(2) = 2*1 + 1 = 3. M(3) = 2*3 + 1 = 7. M(4) = 2*7 + 1 = 15. The formula is 2^n - 1, so 2^4 - 1 = 15."
    },
    {
        "id": 48, "section_id": 4, "topic": "Pseudocode", "marks": 2,
        "question": "What is the output of the following pseudocode?\nString str = 'HELLO WORLD'\nString res = ''\nFor each word in split(str, ' ')\n  res = res + reverse(word) + ' '\nprint trim(res)",
        "options": {"A": "DLROW OLLEH", "B": "OLLEH DLROW", "C": "DLROW WORLD", "D": "HELLO DLROW"},
        "correct_answer": "B",
        "explanation": "The code splits the string into 'HELLO' and 'WORLD'. It reverses each word individually and appends them in their original order. Reverse of HELLO is OLLEH. Reverse of WORLD is DLROW. Output: 'OLLEH DLROW'."
    },
    {
        "id": 49, "section_id": 4, "topic": "Pseudocode", "marks": 2,
        "question": "Array A = [1, 3, 5, 7, 9, 11, 13]. A two-pointer approach is used to find a pair summing to 14 (left=0, right=6). In each step, if A[left]+A[right] < 14, left++; if > 14, right--; else found. How many sum comparisons are made to find the FIRST pair summing to 14?",
        "options": {"A": "1", "B": "2", "C": "3", "D": "4"},
        "correct_answer": "A",
        "explanation": "Initially left=0 (A[0]=1), right=6 (A[6]=13). Sum = 1 + 13 = 14. This is exactly 14. The pair is found on the very first comparison. Output: 1."
    },
    {
        "id": 50, "section_id": 4, "topic": "Pseudocode", "marks": 2,
        "question": "In a top-down dynamic programming approach (memoization) for Fibonacci numbers where fib(n) stores its result in memo[n] before returning, how many times is memo[] WRITTEN TO when computing fib(6)? (Assume memo is initially empty and fib(0), fib(1) are base cases that are also stored).",
        "options": {"A": "5", "B": "6", "C": "7", "D": "13"},
        "correct_answer": "C",
        "explanation": "To compute fib(6), the unique subproblems solved are fib(6), fib(5), fib(4), fib(3), fib(2), fib(1), and fib(0). Since each is computed exactly once and stored in memo, memo is written to 7 times."
    },
    
    # Section 5 (IDs 51-54)
    {
        "id": 51, "section_id": 5, "topic": "Numerical Puzzles", "marks": 2.5,
        "question": "Find the next fraction in the sequence: 1/2, 2/3, 3/5, 5/8, 8/13, ?",
        "options": {"A": "11/21", "B": "13/21", "C": "13/18", "D": "12/21"},
        "correct_answer": "B",
        "explanation": "The numerators follow the Fibonacci sequence: 1, 2, 3, 5, 8, 13. The denominators also follow the Fibonacci sequence shifted: 2, 3, 5, 8, 13, 21. Next fraction is 13/21."
    },
    {
        "id": 52, "section_id": 5, "topic": "Anagram Puzzles", "marks": 2.5,
        "question": "Which of the following words is a perfect anagram of 'ALGORITHMIC'?",
        "options": {"A": "LOGARITHMIC", "B": "ARITHMETIC", "C": "ALGORITHM", "D": "CHROMATIC"},
        "correct_answer": "A",
        "explanation": "ALGORITHMIC and LOGARITHMIC contain exactly the same letters in different orders."
    },
    {
        "id": 53, "section_id": 5, "topic": "Magic Squares", "marks": 2.5,
        "question": "In a 4x4 magic square, the sum of each row, column, and main diagonal is 34. If a row has the values 16, X, 2, 13, what is the value of X?",
        "options": {"A": "3", "B": "5", "C": "7", "D": "9"},
        "correct_answer": "A",
        "explanation": "The sum of the row is 34. So 16 + X + 2 + 13 = 34. 31 + X = 34. X = 3."
    },
    {
        "id": 54, "section_id": 5, "topic": "Logic Puzzles", "marks": 2.5,
        "question": "Five houses are painted in 5 different colors. The Green house is immediately to the left of the White house. If the White house is house #4, what color is house #3?",
        "options": {"A": "Red", "B": "Blue", "C": "Green", "D": "Yellow"},
        "correct_answer": "C",
        "explanation": "The Green house is immediately to the left of the White house. Since the White house is #4, the Green house must be #3."
    },
    
    # Section 6 (IDs 55-59)
    {
        "id": 55, "section_id": 6, "topic": "English Grammar", "marks": 2,
        "question": "Fill in the blank: 'It is essential that he ___ present at the meeting.'",
        "options": {"A": "is", "B": "be", "C": "was", "D": "will be"},
        "correct_answer": "B",
        "explanation": "Phrases like 'It is essential that' require the mandative subjunctive form of the verb, which is the base form 'be'."
    },
    {
        "id": 56, "section_id": 6, "topic": "English Grammar", "marks": 2,
        "question": "Fill in the blank: 'The data ___ that global temperatures are rising.'",
        "options": {"A": "suggest", "B": "suggests", "C": "are suggesting", "D": "were suggesting"},
        "correct_answer": "B",
        "explanation": "While 'data' is technically plural (singular: datum), in modern academic and general English, it is often treated as a singular mass noun. In strict Infosys formatting tricks, they prefer 'suggests' here as the trap."
    },
    {
        "id": 57, "section_id": 6, "topic": "English Grammar", "marks": 2,
        "question": "Fill in the blanks: 'The ___ you practice, the ___ you become.'",
        "options": {"A": "more / better", "B": "most / best", "C": "much / well", "D": "more / best"},
        "correct_answer": "A",
        "explanation": "The 'the + comparative, the + comparative' structure shows parallel increase. 'more' and 'better' are the comparative forms."
    },
    {
        "id": 58, "section_id": 6, "topic": "English Grammar", "marks": 2,
        "question": "Fill in the blank: 'Not until the last guest ___ did she finally relax.'",
        "options": {"A": "had left", "B": "left", "C": "leaves", "D": "was leaving"},
        "correct_answer": "A",
        "explanation": "Negative inversion sentences often use past perfect for the earlier action. 'Not until X had happened did Y happen'."
    },
    {
        "id": 59, "section_id": 6, "topic": "English Grammar", "marks": 2,
        "question": "Which of the following sentences is grammatically correct and maintains parallelism?\nA) She likes reading, swimming, and cooking.\nB) She likes to read, to swim, and to cook.",
        "options": {"A": "Only A", "B": "Only B", "C": "Both A and B", "D": "Neither A nor B"},
        "correct_answer": "C",
        "explanation": "Both sentences maintain perfect parallelism. A uses gerunds consistently, and B uses infinitives consistently."
    },
    
    # Section 7 (ID 60)
    {
        "id": 60, "section_id": 7, "topic": "English Writing", "marks": 0,
        "question": "Write an essay on the topic:\n'Quantum Computing \u2014 A Paradigm Shift in Computational Power and Its Implications for Cybersecurity and Artificial Intelligence'\nAddress (1) what makes quantum computing fundamentally different from classical computing, (2) specific cybersecurity threats it poses (encryption breaking), (3) how AI can benefit from quantum speedup, and (4) your recommendation for governments and enterprises.",
        "options": {},
        "correct_answer": "",
        "explanation": "Subjective evaluation based on criteria.",
        "is_essay": True,
        "word_limit_min": 150,
        "word_limit_max": 250,
        "sample_high_scoring_response": "Quantum computing represents a monumental paradigm shift from classical computing. While traditional computers rely on bits that represent strictly 0s or 1s, quantum computers utilize qubits. Thanks to principles of superposition and entanglement, qubits can exist in multiple states simultaneously, allowing quantum systems to process vast amounts of possibilities concurrently rather than sequentially.\n\nThis immense computational speedup presents a profound cybersecurity threat. Current encryption protocols, such as RSA, rely on the difficulty of factoring large prime numbers\u2014a task that would take classical computers millennia. However, algorithms like Shor\u2019s algorithm running on a sufficiently powerful quantum computer could break these encryptions in hours, exposing highly sensitive global data.\n\nConversely, Artificial Intelligence stands to benefit enormously from quantum speedup. AI thrives on data analysis and complex optimization problems. Quantum machine learning could drastically reduce the time needed to train complex neural networks, paving the way for breakthroughs in drug discovery, climate modeling, and autonomous systems.\n\nTo navigate this dual-edged sword, it is imperative that governments and enterprises take immediate action. I recommend heavy investment in 'post-quantum cryptography' to secure critical infrastructure before quantum computers reach maturity. Concurrently, public-private partnerships should foster quantum AI research. By proactively standardizing quantum-resistant protocols today, we can safely harness quantum computing\u2019s extraordinary potential tomorrow.",
        "evaluation_criteria": [
            "Addresses all 4 prompt components",
            "Meets word count limits (150-250 words)",
            "Clear logical flow and paragraph structure",
            "Advanced vocabulary (e.g., superposition, entanglement, paradigm shift)",
            "Grammatical accuracy and appropriate formal tone"
        ]
    }
]

data = {
    "test_title": "Infosys SE Mock Test 5 \u2014 2027 Batch Pattern (Advanced Level)",
    "questions": questions
}

output_path = r"C:\Users\devan\.gemini\antigravity\scratch\infosys-se-mock-test\test5.json"

os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(f"Test data successfully written to {output_path}")

section_counts = {}
for q in questions:
    s_id = q.get("section_id")
    section_counts[s_id] = section_counts.get(s_id, 0) + 1

print("\\nSection Counts:")
for s_id, count in sorted(section_counts.items()):
    print(f"Section {s_id}: {count} questions")
print(f"Total: {len(questions)} questions")
