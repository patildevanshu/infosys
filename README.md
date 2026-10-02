# Infosys Systems Engineer (SE) Multi-Test Assessment Platform

Interactive, full-featured web-based assessment platform matching the updated **Infosys Systems Engineer (SE) Test Pattern (2027 Batch)**.

Contains **4 Full-Length Mock Tests (240 Unique Questions, Zero Overlap)** with sectional timers, automated section advancement, real-time question palette, and detailed end-of-test performance scorecard with mistake analysis.

---

## 📊 Exam Structure & Section Timers (per Test)

| Section # | Section Name | Questions | Max Marks | Duration | High Priority Topics |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **Section 1** | **Reasoning Ability Test** | 15 | 15 | 25 Mins | Data Sufficiency, DI (Tables/Charts), Syllogisms, Coding-Decoding, Blood Relations, Directional Sense, Seating Arrangement |
| **Section 2** | **Technical Ability Test (Mathematical)** | 10 | 10 | 35 Mins | Number Series, Ratios & Proportions, P&C & Probability, Time-Speed-Distance, Cryptarithmetic, Profit & Loss, Partnerships |
| **Section 3** | **Verbal Ability Test** | 20 | 20 | 20 Mins | Critical Reasoning, Corrective Usage, Error Correction, Error Identification, Reading Comprehension (Passage + 4 Qs), Para Jumbles, Vocabulary |
| **Section 4** | **Pseudocode Test** | 5 | 10 | 10 Mins | Nested Loops, Recursion, Binary Search, GCD / Euclidean Algorithm, Array & String Logic |
| **Section 5** | **Numerical Puzzle Test** | 4 | 10 | 10 Mins | Visual Reasoning / Rotations, Word Puzzles / Anagrams, Magic Squares / Spirals, Constraint Logic Grids |
| **Section 6** | **English Grammar Test** | 5 | 10 | 10 Mins | Tenses, Subject-Verb Agreement, Active/Passive Voice, Reported Speech, Conditionals, Punctuation |
| **Section 7** | **English Writing Test** | 1 | NA | 10 Mins | Essay Writing (150–250 words) with real-time word counter & benchmark model answer |
| **TOTAL** | | **60** | **75\*** | **120 Mins** | |

---

## 📚 Mock Tests Included (240 Questions Total • Zero Overlap)

* **Test 1**: Internet of Things (RC), Letter Shift Coding, Bubble Sort Pseudocode, SEND+MORE=MONEY Cryptarithmetic, Remote Work Essay.
* **Test 2**: Climate Change (RC), Number Position Coding, Recursion & Binary Search, Magic Square, Mixture Problems, Digital Education Essay.
* **Test 3**: Telemedicine (RC), Reverse Alphabet Coding, Two-Row Seating, GCD & In-Place Reversal, Cards Probability, Cybersecurity Threats Essay.
* **Test 4**: Blockchain Technology (RC), Vowel-Consonant Swap, Fibonacci & Stack Pseudocode, Alligation & Derangement, Digital Privacy Laws Essay.

---

## 🚀 How to Run the Assessment

### Method 1: Direct Browser Launch (100% Offline, No Server Needed)
* Simply open `index.html` in Chrome, Edge, Firefox, or Safari.
* Test datasets are bundled in local JavaScript (`all_tests.js`) — zero CORS issues, works completely offline.

### Method 2: Local Web Server
1. Run `start_test.bat` (on Windows) or:
   ```bash
   python -m http.server 8080
   ```
2. Open [http://localhost:8080](http://localhost:8080) in your browser.

---

## 🎯 Key Features

1. **Test Selection Hub:** Choose between Tests 1, 2, 3, or 4 with clear topic previews and section breakdowns.
2. **Accurate Sectional Timers & Auto-Progression:**
   * Live countdown per section (with visual alerts at 5 mins and 1 min).
   * 120-minute total exam timer.
   * Auto-advances to the next section when time runs out.
3. **Official Question Palette:**
   * Visual status indicators: Answered (Green), Review (Yellow), Unanswered (Red), Not Visited (Gray).
   * Quick navigation between questions in the current section.
4. **Comprehensive Evaluation & Scorecard:**
   * Overall score out of 75 marks with percentage calculation.
   * Infosys sectional cutoff verdict (65%+ threshold indicator).
   * Section-by-section breakdown table with accuracy metrics.
5. **Detailed Mistakes & Solutions Breakdown:**
   * Filter reviews by: `All Questions`, `Mistakes Only`, `Correct Only`, `Unattempted`.
   * Clear side-by-side comparison of candidate answer vs correct answer.
   * Detailed step-by-step mathematical deductions and grammatical explanations for every question.
   * Qualitative essay grading with scoring rubrics and high-scoring benchmark model essays.
6. **Print & PDF Export:** One-click print/save as PDF for offline review.

---

## 🛠️ Adding More Tests

To add a new mock test (e.g. `test5.json`):
1. Create `test5.json` following the existing format.
2. Run:
   ```bash
   python compile_all_tests.py
   ```
3. The platform will automatically bundle and render the new test card!
