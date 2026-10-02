// Infosys SE Multi-Test Mock Assessment Engine

let testData = null;
let currentSectionIdx = 0;
let currentQuestionGlobalIdx = 0;
let userResponses = {};
let sectionTimeRemaining = [];
let totalTimeRemaining = 120 * 60;
let timerInterval = null;
let isSubmitted = false;
let eventsSetup = false;

// ==================== TEST SELECTION SCREEN ====================

function getTestsList() {
  if (typeof window !== 'undefined' && window.ALL_TESTS && Array.isArray(window.ALL_TESTS.tests)) {
    return window.ALL_TESTS.tests;
  }
  if (typeof ALL_TESTS !== 'undefined' && ALL_TESTS && Array.isArray(ALL_TESTS.tests)) {
    return ALL_TESTS.tests;
  }
  if (typeof window !== 'undefined' && window.TEST_DATA) {
    return [window.TEST_DATA];
  }
  return null;
}

let renderAttempts = 0;
function renderTestCards() {
  const container = document.getElementById('test-cards-container');
  if (!container) return;

  const tests = getTestsList();
  if (!tests || tests.length === 0) {
    if (renderAttempts < 10) {
      renderAttempts++;
      setTimeout(renderTestCards, 200);
      return;
    }
    container.innerHTML = `
      <div style="background:#fff; padding:2rem; border-radius:12px; border:2px solid #ef4444; text-align:center; max-width:500px;">
        <h3 style="color:#ef4444; margin-bottom:0.5rem;">Test Data Not Loaded</h3>
        <p style="color:#64748b; font-size:0.95rem; margin-bottom:1rem;">Could not load test definitions. Please make sure <code>all_tests.js</code> is in the same folder.</p>
        <button class="btn btn-primary" onclick="renderAttempts=0; renderTestCards()">🔄 Retry Loading</button>
      </div>
    `;
    return;
  }

  container.innerHTML = '';
  tests.forEach((test, idx) => {
    const difficultyLabel = { 4: ' 🔥 Advanced', 5: ' 💀 Expert', 6: ' ⭐ PYQ Special' };
    const topicHighlights = {
      0: 'Syllogisms, Data Sufficiency, Coding-Decoding, Number Series, Ratios, P&C, RC Passage (IoT), Critical Reasoning, Bubble Sort',
      1: 'Seating Arrangements, Blood Relations, Mixture Problems, Probability, Boats & Streams, RC Passage (Climate Change), Recursion, Binary Search, Magic Square',
      2: 'Fibonacci Series, Reverse Alphabet Coding, Two Rows Seating, RC Passage (Telemedicine), Fewer/Less, Lie/Lay, GCD Algorithm, Array Reversal, Cybersecurity Essay',
      3: 'Prime Series, Alligation, Derangement, Shadow Direction, RC Passage (Blockchain), Affect/Effect, Stack Operations, Fibonacci Pseudocode, Digital Privacy Essay',
      4: '🔥 HARD: Trap DS (x²=4 puzzle), 4-statement Syllogisms, 10-person Circular Seating, Tower of Hanoi, RC (Cognitive Biases & Behavioral Economics), OBFUSCATE/MAGNANIMOUS vocab, Inverted Conditionals, Quantum Computing Essay',
      5: '💀 EXPERT: DS where NEITHER stmt is sufficient, 3-set Venn Diagram, 2¹⁰⁰ mod 7 (cyclicity), XOR missing number, Geometric Probability, RC (Neuroplasticity & TBI), SANCTION/CLEAVE dual-meaning vocab, AI Existential Risk Essay',
      6: '⭐ PYQ: Real Infosys Questions — FRIEND→HUMJTK coding, 5km South direction, Train passing platform (132m), Sum doubles in 5 yrs, LEADER arrangements, HCF/LCM ratio, Pipes & tank, Loquacious/Frugal/Tenacious vocab, Anagram TRIANGLE, Squares of primes puzzle, Social Media essay'
    };

    const card = document.createElement('div');
    card.className = 'test-card';
    if (idx === 4) card.style.borderColor = '#f59e0b';
    if (idx === 5) card.style.borderColor = '#ef4444';
    if (idx === 6) card.style.borderColor = '#10b981';
    card.innerHTML = `
      <div class="card-badge" style="${idx===4?'background:#f59e0b':idx===5?'background:#ef4444':idx===6?'background:#10b981':''}">Test ${idx + 1}${difficultyLabel[idx] || ''}</div>
      <h2>${test.test_title || `Infosys SE Mock Test ${idx + 1}`}</h2>
      <p class="card-description">${topicHighlights[idx] || 'Full-length assessment covering all 7 sections with unique PYQ-based questions.'}</p>
      <div class="card-stats">
        <div class="stat-item"><div class="stat-val">${test.total_questions || 60}</div><div class="stat-label">Questions</div></div>
        <div class="stat-item"><div class="stat-val">${test.total_marks || 75}</div><div class="stat-label">Total Marks</div></div>
        <div class="stat-item"><div class="stat-val">${idx===6?'⭐ PYQ':idx>=4?'⚠️ Hard':'Normal'}</div><div class="stat-label">Difficulty</div></div>
        <div class="stat-item"><div class="stat-val">${test.total_duration_minutes || 120} min</div><div class="stat-label">Duration</div></div>
      </div>
      <button class="btn-start-test" style="${idx===4?'background:#f59e0b':idx===5?'background:#ef4444':idx===6?'background:#10b981':''}" onclick="event.stopPropagation(); startTest(${idx})">▶ Start Mock Test ${idx + 1}${difficultyLabel[idx] || ''}</button>
    `;
    card.addEventListener('click', () => startTest(idx));
    container.appendChild(card);
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', renderTestCards);
} else {
  renderTestCards();
}

function startTest(testIndex) {
  const tests = getTestsList();
  if (!tests || !tests[testIndex]) {
    alert("Test data not found. Please refresh the page.");
    return;
  }
  testData = tests[testIndex];
  isSubmitted = false;
  currentSectionIdx = 0;
  currentQuestionGlobalIdx = 0;
  userResponses = {};
  sectionTimeRemaining = [];
  totalTimeRemaining = testData.total_duration_minutes * 60;

  // Hide selection, show exam
  document.getElementById('selection-screen').style.display = 'none';
  document.getElementById('app-header').style.display = 'flex';
  document.getElementById('section-nav-bar').style.display = 'flex';
  document.getElementById('exam-layout').style.display = 'flex';
  document.getElementById('results-dashboard').style.display = 'none';

  // Update header title
  document.getElementById('header-test-title').textContent = testData.test_title;

  initTestState();
  renderSectionTabs();
  renderCurrentQuestion();
  renderPalette();
  startTimer();
  if (!eventsSetup) {
    setupEventListeners();
    eventsSetup = true;
  }
}

function backToSelection() {
  // Stop timers
  clearInterval(timerInterval);
  isSubmitted = false;

  // Hide everything, show selection
  document.getElementById('selection-screen').style.display = 'flex';
  document.getElementById('app-header').style.display = 'none';
  document.getElementById('section-nav-bar').style.display = 'none';
  document.getElementById('exam-layout').style.display = 'none';
  document.getElementById('results-dashboard').style.display = 'none';
  document.getElementById('submit-modal').style.display = 'none';
}

// ==================== EXAM ENGINE ====================

function initTestState() {
  if (!testData) return;
  sectionTimeRemaining = testData.sections.map(s => s.duration_minutes * 60);
  testData.questions.forEach(q => {
    userResponses[q.id] = { answer: null, status: 'unvisited' };
  });
  userResponses[testData.questions[0].id].status = 'unanswered';
}

function startTimer() {
  clearInterval(timerInterval);
  timerInterval = setInterval(() => {
    if (isSubmitted) { clearInterval(timerInterval); return; }
    if (sectionTimeRemaining[currentSectionIdx] > 0) {
      sectionTimeRemaining[currentSectionIdx]--;
    } else {
      handleSectionTimeout();
    }
    if (totalTimeRemaining > 0) {
      totalTimeRemaining--;
    } else {
      clearInterval(timerInterval);
      alert('Total Assessment Time has expired! Submitting automatically.');
      submitTest();
    }
    updateTimerDisplay();
  }, 1000);
}

function updateTimerDisplay() {
  const secSecs = sectionTimeRemaining[currentSectionIdx] || 0;
  const secBox = document.getElementById('section-timer-box');
  const secVal = document.getElementById('section-timer-val');
  const totVal = document.getElementById('total-timer-val');
  if (secVal) secVal.textContent = formatTime(secSecs);
  if (totVal) totVal.textContent = formatTimeHours(totalTimeRemaining);
  if (secBox) {
    if (secSecs <= 60) secBox.className = 'timer-box section-timer danger';
    else if (secSecs <= 300) secBox.className = 'timer-box section-timer warning';
    else secBox.className = 'timer-box section-timer';
  }
}

function formatTime(s) { return `${Math.floor(s/60).toString().padStart(2,'0')}:${(s%60).toString().padStart(2,'0')}`; }
function formatTimeHours(s) { const h=Math.floor(s/3600),m=Math.floor((s%3600)/60),sec=s%60; return `${h.toString().padStart(2,'0')}:${m.toString().padStart(2,'0')}:${sec.toString().padStart(2,'0')}`; }

function handleSectionTimeout() {
  const curSec = testData.sections[currentSectionIdx];
  if (currentSectionIdx < testData.sections.length - 1) {
    alert(`Time for "${curSec.name}" has finished. Advancing to the next section.`);
    switchSection(currentSectionIdx + 1);
  } else {
    alert('Final section time expired! Submitting test.');
    submitTest();
  }
}

function renderSectionTabs() {
  const navBar = document.getElementById('section-nav-bar');
  if (!navBar || !testData) return;
  navBar.innerHTML = '';
  testData.sections.forEach((sec, idx) => {
    const btn = document.createElement('button');
    btn.className = `sec-tab-btn ${idx === currentSectionIdx ? 'active' : ''}`;
    btn.innerHTML = `<span>${sec.name}</span><span class="badge">${sec.total_questions} Qs</span>`;
    btn.addEventListener('click', () => switchSection(idx));
    navBar.appendChild(btn);
  });
}

function switchSection(secIdx) {
  currentSectionIdx = secIdx;
  renderSectionTabs();
  const targetSec = testData.sections[secIdx];
  const firstQIdx = testData.questions.findIndex(q => q.section_id === targetSec.id);
  if (firstQIdx !== -1) goToQuestion(firstQIdx);
}

function goToQuestion(globalIdx) {
  currentQuestionGlobalIdx = globalIdx;
  const q = testData.questions[globalIdx];
  const secIdx = testData.sections.findIndex(s => s.id === q.section_id);
  if (secIdx !== -1 && secIdx !== currentSectionIdx) { currentSectionIdx = secIdx; renderSectionTabs(); }
  if (userResponses[q.id].status === 'unvisited') userResponses[q.id].status = 'unanswered';
  renderCurrentQuestion();
  renderPalette();
}

function renderCurrentQuestion() {
  const q = testData.questions[currentQuestionGlobalIdx];
  if (!q) return;
  const currentSec = testData.sections.find(s => s.id === q.section_id);
  const secQuestions = testData.questions.filter(item => item.section_id === q.section_id);
  const qNumInSection = secQuestions.findIndex(item => item.id === q.id) + 1;

  document.getElementById('q-number-pill').textContent = `Q ${qNumInSection} of ${secQuestions.length} (Overall: Q${q.id}/60)`;
  document.getElementById('q-topic-tag').textContent = `${currentSec.name} • ${q.topic || 'General'}`;
  document.getElementById('q-marks-pill').textContent = q.is_essay ? 'Qualitative' : `+${q.marks} Mark${q.marks > 1 ? 's' : ''}`;
  document.getElementById('q-body').innerHTML = q.question.replace(/\n/g, '<br>');

  const optionsArea = document.getElementById('options-area');
  const essayArea = document.getElementById('essay-area');

  if (q.is_essay) {
    optionsArea.style.display = 'none';
    essayArea.style.display = 'block';
    renderEssayQuestion(q);
  } else {
    essayArea.style.display = 'none';
    optionsArea.style.display = 'flex';
    renderMCQOptions(q);
  }

  const btnPrev = document.getElementById('btn-prev');
  if (btnPrev) { btnPrev.disabled = currentQuestionGlobalIdx === 0; btnPrev.style.opacity = currentQuestionGlobalIdx === 0 ? '0.5' : '1'; }
}

function renderMCQOptions(q) {
  const optionsArea = document.getElementById('options-area');
  optionsArea.innerHTML = '';
  const currentSelection = userResponses[q.id].answer;
  Object.entries(q.options).forEach(([optKey, optText]) => {
    const isSelected = currentSelection === optKey;
    const optCard = document.createElement('div');
    optCard.className = `option-item ${isSelected ? 'selected' : ''}`;
    optCard.innerHTML = `<div class="opt-indicator">${optKey}</div><div class="opt-text">${optText}</div>`;
    optCard.addEventListener('click', () => selectOption(q.id, optKey));
    optionsArea.appendChild(optCard);
  });
}

function selectOption(questionId, optionKey) {
  userResponses[questionId].answer = optionKey;
  if (userResponses[questionId].status !== 'review') userResponses[questionId].status = 'answered';
  renderCurrentQuestion();
  renderPalette();
}

function renderEssayQuestion(q) {
  const textarea = document.getElementById('essay-textarea');
  const wordCountElem = document.getElementById('essay-word-count');
  textarea.value = userResponses[q.id].answer || '';
  const updateStats = () => {
    const text = textarea.value.trim();
    const words = text ? text.split(/\s+/).length : 0;
    wordCountElem.textContent = `${words} / 150-250 words`;
    wordCountElem.style.color = (words >= 150 && words <= 250) ? 'var(--success)' : words > 250 ? 'var(--danger)' : 'var(--text-muted)';
    userResponses[q.id].answer = textarea.value;
    userResponses[q.id].status = words > 0 ? 'answered' : 'unanswered';
    renderPalette();
  };
  textarea.oninput = updateStats;
  updateStats();
}

function renderPalette() {
  const grid = document.getElementById('q-grid');
  if (!grid || !testData) return;
  grid.innerHTML = '';
  const currentSec = testData.sections[currentSectionIdx];
  const secQuestions = testData.questions.filter(q => q.section_id === currentSec.id);
  secQuestions.forEach(q => {
    const globalIdx = testData.questions.findIndex(item => item.id === q.id);
    const resp = userResponses[q.id];
    const btn = document.createElement('button');
    btn.className = `q-btn ${resp.status} ${globalIdx === currentQuestionGlobalIdx ? 'current' : ''}`;
    btn.textContent = q.id;
    btn.addEventListener('click', () => goToQuestion(globalIdx));
    grid.appendChild(btn);
  });
  updatePaletteLegendCounts();
}

function updatePaletteLegendCounts() {
  let answered=0, review=0, unanswered=0, unvisited=0;
  Object.values(userResponses).forEach(r => {
    if (r.status==='answered') answered++; else if (r.status==='review') review++;
    else if (r.status==='unanswered') unanswered++; else unvisited++;
  });
  const e = id => document.getElementById(id);
  if(e('count-answered')) e('count-answered').textContent = answered;
  if(e('count-review')) e('count-review').textContent = review;
  if(e('count-unanswered')) e('count-unanswered').textContent = unanswered;
  if(e('count-unvisited')) e('count-unvisited').textContent = unvisited;
}

function setupEventListeners() {
  document.getElementById('btn-prev')?.addEventListener('click', () => { if (currentQuestionGlobalIdx > 0) goToQuestion(currentQuestionGlobalIdx - 1); });
  document.getElementById('btn-save-next')?.addEventListener('click', () => {
    const q = testData.questions[currentQuestionGlobalIdx];
    if (userResponses[q.id].answer) userResponses[q.id].status = 'answered'; else userResponses[q.id].status = 'unanswered';
    if (currentQuestionGlobalIdx < testData.questions.length - 1) goToQuestion(currentQuestionGlobalIdx + 1); else openSubmitModal();
  });
  document.getElementById('btn-review-next')?.addEventListener('click', () => {
    const q = testData.questions[currentQuestionGlobalIdx];
    userResponses[q.id].status = 'review';
    if (currentQuestionGlobalIdx < testData.questions.length - 1) goToQuestion(currentQuestionGlobalIdx + 1); else openSubmitModal();
  });
  document.getElementById('btn-clear')?.addEventListener('click', () => {
    const q = testData.questions[currentQuestionGlobalIdx];
    userResponses[q.id].answer = null; userResponses[q.id].status = 'unanswered';
    renderCurrentQuestion(); renderPalette();
  });
  document.getElementById('btn-submit-test-sidebar')?.addEventListener('click', openSubmitModal);
  document.getElementById('modal-cancel-btn')?.addEventListener('click', closeSubmitModal);
  document.getElementById('modal-confirm-btn')?.addEventListener('click', () => { closeSubmitModal(); submitTest(); });
}

function openSubmitModal() { document.getElementById('submit-modal').style.display = 'flex'; }
function closeSubmitModal() { document.getElementById('submit-modal').style.display = 'none'; }

// ==================== EVALUATION ====================

function submitTest() {
  isSubmitted = true;
  clearInterval(timerInterval);
  document.getElementById('exam-layout').style.display = 'none';
  document.getElementById('section-nav-bar').style.display = 'none';
  document.getElementById('app-header').style.display = 'none';
  document.getElementById('results-dashboard').style.display = 'block';
  document.getElementById('results-subtitle').textContent = testData.test_title + ' • PYQ-Based Benchmark Evaluation';
  renderEvaluationDashboard();
}

function renderEvaluationDashboard() {
  let totalScore=0, totalCorrect=0, totalIncorrect=0, totalUnattempted=0;
  const sectionSummary = testData.sections.map(sec => {
    const secQuestions = testData.questions.filter(q => q.section_id === sec.id);
    let secScore=0, secCorrect=0, secIncorrect=0, secUnattempted=0;
    secQuestions.forEach(q => {
      if (q.is_essay) return;
      const resp = userResponses[q.id];
      if (resp && resp.answer) { if (resp.answer === q.correct_answer) { secScore += q.marks; secCorrect++; } else secIncorrect++; }
      else secUnattempted++;
    });
    totalScore += secScore; totalCorrect += secCorrect; totalIncorrect += secIncorrect; totalUnattempted += secUnattempted;
    const pct = sec.max_marks > 0 ? ((secScore/sec.max_marks)*100).toFixed(1) : 'NA';
    return { ...sec, score: secScore, correct: secCorrect, incorrect: secIncorrect, unattempted: secUnattempted, percentage: pct, cleared: sec.max_marks > 0 ? (secScore/sec.max_marks >= 0.65) : true };
  });

  const overallPct = ((totalScore/75)*100).toFixed(1);
  document.getElementById('res-total-score').textContent = `${totalScore} / 75`;
  document.getElementById('res-percent').textContent = `${overallPct}%`;
  const v = document.getElementById('res-verdict');
  v.textContent = overallPct >= 65 ? 'CLEARED ✓' : 'NEEDS PRACTICE';
  v.className = `metric-val ${overallPct >= 65 ? 'verdict-pass' : 'verdict-warn'}`;
  document.getElementById('res-correct-count').textContent = totalCorrect;
  document.getElementById('res-incorrect-count').textContent = totalIncorrect;
  document.getElementById('res-unanswered-count').textContent = totalUnattempted;

  const tbody = document.getElementById('section-breakdown-tbody');
  tbody.innerHTML = '';
  sectionSummary.forEach(s => {
    const tr = document.createElement('tr');
    tr.innerHTML = `<td><strong>${s.name}</strong></td><td>${s.total_questions}</td><td>${s.correct}</td><td style="color:var(--danger);font-weight:700;">${s.incorrect}</td><td>${s.unattempted}</td><td><strong>${s.max_marks>0?s.score+'/'+s.max_marks:'Evaluated'}</strong></td><td>${s.percentage!=='NA'?s.percentage+'%':'Qualitative'}</td><td class="${s.cleared?'verdict-pass':'verdict-warn'}">${s.cleared?'✓ Cleared':'✗ Below 65%'}</td>`;
    tbody.appendChild(tr);
  });

  renderReviewList('all');
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.onclick = (e) => { document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active')); e.target.classList.add('active'); renderReviewList(e.target.dataset.filter); };
  });
}

function renderReviewList(filter) {
  const container = document.getElementById('review-list-container');
  if (!container) return;
  container.innerHTML = '';
  testData.questions.forEach(q => {
    const resp = userResponses[q.id];
    const isEssay = q.is_essay;
    const isAnswered = resp && resp.answer;
    const isCorrect = !isEssay && isAnswered && resp.answer === q.correct_answer;
    const isIncorrect = !isEssay && isAnswered && resp.answer !== q.correct_answer;
    const isUnanswered = !isAnswered;

    if (filter === 'incorrect' && !isIncorrect) return;
    if (filter === 'correct' && !isCorrect) return;
    if (filter === 'unanswered' && !isUnanswered) return;

    let statusClass = 'is-unanswered', statusBadge = '<span style="color:#64748b;font-weight:700;">Unattempted</span>';
    if (isEssay) { statusClass = 'is-correct'; statusBadge = '<span style="color:var(--primary);font-weight:700;">Essay Submitted</span>'; }
    else if (isCorrect) { statusClass = 'is-correct'; statusBadge = `<span style="color:var(--success);font-weight:700;">✓ Correct (+${q.marks})</span>`; }
    else if (isIncorrect) { statusClass = 'is-incorrect'; statusBadge = '<span style="color:var(--danger);font-weight:700;">✗ Incorrect</span>'; }

    let choicesHtml = '';
    if (!isEssay && q.options) {
      choicesHtml = '<div class="review-choices">';
      Object.entries(q.options).forEach(([k, text]) => {
        let cls = '';
        if (k === q.correct_answer && k === resp.answer) cls = 'user-correct-pick';
        else if (k === q.correct_answer) cls = 'correct-pick';
        else if (k === resp.answer) cls = 'user-pick';
        choicesHtml += `<div class="choice-box ${cls}"><strong>[${k}]</strong> ${text}${k===q.correct_answer?' <span style="color:var(--success);font-weight:800;">✓ Correct</span>':''}${k===resp.answer&&k!==q.correct_answer?' <span style="color:var(--danger);font-weight:800;">✗ Your Answer</span>':''}</div>`;
      });
      choicesHtml += '</div>';
    }

    let essayHtml = '';
    if (isEssay) {
      const words = resp.answer ? resp.answer.trim().split(/\s+/).length : 0;
      essayHtml = `<div style="background:#f1f5f9;padding:1rem;border-radius:8px;margin-bottom:1rem;"><h4 style="font-size:0.9rem;margin-bottom:0.4rem;">Your Essay (${words} Words):</h4><p style="white-space:pre-wrap;line-height:1.6;">${resp.answer||'No submission.'}</p></div>`;
      if (q.sample_high_scoring_response) {
        essayHtml += `<div style="background:#e6f7ff;border:1px solid #91d5ff;padding:1rem;border-radius:8px;margin-bottom:1rem;"><h4 style="font-size:0.9rem;color:#0050b3;margin-bottom:0.4rem;">Benchmark Model Answer:</h4><p style="white-space:pre-wrap;font-size:0.92rem;line-height:1.6;">${q.sample_high_scoring_response}</p></div>`;
      }
    }

    const item = document.createElement('div');
    item.className = `review-item ${statusClass}`;
    item.innerHTML = `<div class="review-meta"><span>Q${q.id} • ${q.topic||'General'}</span><span>${statusBadge}</span></div><div class="review-q-text"><strong>${q.question.replace(/\n/g,'<br>')}</strong></div>${choicesHtml}${essayHtml}<div class="explanation-card"><strong>💡 Solution:</strong><br>${(q.explanation||'See criteria above.').replace(/\n/g,'<br>')}</div>`;
    container.appendChild(item);
  });
}
