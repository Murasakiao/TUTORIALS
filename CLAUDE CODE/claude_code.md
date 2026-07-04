---
marp: true
paginate: true
html: true
size: 4:3
style: |
  @import url('https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;1,300&family=Space+Mono:wght@400;700&display=swap');

  :root {
    --accent:      #e5e5e5;
    --accent-dim:  #a3a3a3;
    --white:       #fafafa;
    --off-white:   #d4d4d4;
    --subtle:      #a3a3a3;
    --muted:       #737373;
    --faint:       #262626;
    --bg:          #0a0a0a;
    --card-bg:     #121212;
    --card-border: #232323;
    --good-border: #3f3f3f;
    --bad-color:   #d4d4d4;
  }

  section {
    font-family: 'Inter', sans-serif;
    background: var(--bg);
    color: var(--white);
    padding: 44px 52px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    position: relative;
  }

  h1 {
    font-size: 38px;
    font-weight: 400;
    line-height: 1.08;
    margin: 0 0 14px 0;
    color: var(--white);
    letter-spacing: -1px;
  }
  h2 {
    font-size: 28px;
    font-weight: 400;
    line-height: 1.1;
    margin: 0 0 14px 0;
    color: var(--white);
    letter-spacing: -0.5px;
    border: none;
  }
  p {
    font-size: 16px;
    font-weight: 300;
    line-height: 1.6;
    color: var(--subtle);
    margin: 0 0 12px 0;
  }
  strong { color: var(--white); font-weight: 500; }
  em     { color: var(--muted); font-style: normal; }
  code {
    font-family: 'Space Mono', monospace;
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    color: var(--white);
    padding: 1px 6px;
    border-radius: 2px;
    font-size: 0.88em;
  }

  /* ── TAG ── */
  .tag {
    display: flex;
    align-items: center;
    gap: 12px;
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 3px;
    color: var(--accent-dim);
    text-transform: uppercase;
    margin-bottom: 18px;
  }
  .tag::before {
    content: '';
    display: block;
    width: 24px;
    height: 2px;
    background: var(--accent-dim);
    flex-shrink: 0;
  }
  .tag.green  { color: var(--accent-dim); }
  .tag.green::before { background: var(--accent-dim); }
  .tag.blue   { color: var(--accent-dim); }
  .tag.blue::before  { background: var(--accent-dim); }

  /* ── HEADER ROW ── */
  .header-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
  }
  .page-num {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    color: var(--muted);
    letter-spacing: 2px;
    text-transform: uppercase;
  }
  .page-label {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    color: var(--muted);
  }

  /* ── CARDS 2-col ── */
  .cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-bottom: 12px;
  }
  .card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 3px;
    padding: 14px;
  }
  .card-icon { font-size: 17px; margin-bottom: 6px; display: block; }
  .card h3 {
    font-size: 14px;
    font-weight: 500;
    color: var(--white);
    margin: 0 0 4px;
  }
  .card p {
    font-size: 13px;
    color: var(--subtle);
    line-height: 1.45;
    margin: 0;
  }

  /* ── CARDS 1-col stacked ── */
  .cards-col { display: flex; flex-direction: column; gap: 8px; margin-bottom: 12px; }
  .card-row {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 3px;
    padding: 12px 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }
  .card-row-icon { font-size: 17px; flex-shrink: 0; margin-top: 1px; }
  .card-row-body h3 {
    font-size: 14px;
    font-weight: 500;
    color: var(--white);
    margin: 0 0 3px;
  }
  .card-row-body p {
    font-size: 13px;
    color: var(--subtle);
    margin: 0;
    line-height: 1.45;
  }

  /* ── COMPARE 2-col ── */
  .compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-bottom: 10px;
  }
  .compare-col {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 3px;
    padding: 14px 16px;
  }
  .compare-col.good { border-color: var(--good-border); }
  .compare-label {
    font-family: 'Space Mono', monospace;
    font-size: 9px;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 6px;
    color: var(--muted);
  }
  .compare-label.bad  { color: var(--muted); }
  .compare-label.good { color: var(--white); }
  .compare-col h3 {
    font-size: 14px;
    font-weight: 500;
    color: var(--white);
    margin: 0 0 5px;
  }
  .compare-col p {
    font-size: 13px;
    color: var(--subtle);
    line-height: 1.45;
    margin: 0;
  }

  /* ── LIST (numbered rows) ── */
  .list { display: flex; flex-direction: column; gap: 7px; margin-bottom: 12px; }
  .list-item {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 2px;
    padding: 10px 14px;
  }
  .list-num {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: var(--accent-dim);
    flex-shrink: 0;
    margin-top: 1px;
    min-width: 18px;
  }
  .list-text { font-size: 13.5px; color: var(--subtle); line-height: 1.45; }
  .list-text strong { color: var(--white); }

  /* ── PILL ── */
  .pill {
    display: inline-block;
    background: #0a0a0a;
    border: 1px solid var(--card-border);
    border-radius: 2px;
    padding: 2px 8px;
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: var(--white);
  }

  /* ── INSIGHT BOX ── */
  .insight {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 3px;
    padding: 12px 18px;
    margin-top: auto;
  }
  .insight-label {
    font-family: 'Space Mono', monospace;
    font-size: 9px;
    letter-spacing: 3px;
    color: var(--muted);
    text-transform: uppercase;
    margin-bottom: 4px;
  }
  .insight p { font-size: 14px; color: var(--off-white); line-height: 1.5; margin: 0; }

  /* ── COVER ── */
  section.cover {
    justify-content: flex-end;
    padding-bottom: 80px;
    background: #050505;
  }
  section.cover h1 { font-size: 48px; }
  section.cover p  { font-size: 17px; color: var(--subtle); }

  /* ── VOLUME DIVIDER ── */
  section.vol-divider {
    justify-content: center;
    border-left: 5px solid var(--faint);
    background: #0c0c0c;
  }
  section.vol-divider .tag { margin-bottom: 20px; }
  section.vol-divider h1   { font-size: 44px; color: var(--white); margin-bottom: 10px; }
  section.vol-divider h2   { font-size: 24px; color: var(--off-white); border: none; margin: 0 0 16px; }
  section.vol-divider p    { font-size: 15px; color: var(--muted); }

  /* ── CTA ── */
  section.cta {
    justify-content: center;
    align-items: center;
    text-align: center;
    background: var(--white);
  }
  section.cta h1 { color: #0a0a0a; font-size: 40px; letter-spacing: -1px; margin-bottom: 10px; }
  section.cta h2 { color: #404040; font-size: 22px; border: none; margin-bottom: 12px; }
  section.cta p  { color: #525252; font-size: 16px; max-width: 540px; margin: 0; }
  section.cta .handle {
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    color: #737373;
    margin-top: 22px;
    letter-spacing: 2px;
    text-transform: uppercase;
  }

  /* ── FOOTER ── */
  section::after {
    font-family: 'Space Mono', monospace;
    font-size: 9px;
    color: var(--muted);
    letter-spacing: 1px;
    content: 'Claude Code 101 · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
    position: absolute;
    bottom: 20px;
    right: 40px;
  }
---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 1 · COVER                        -->
<!-- ══════════════════════════════════════ -->
<!-- _class: cover -->

<div class="tag">Mini Tutorial · Vol 1 – Vol 4</div>

# Claude Code 101

Stop copying code into chatbots. Start shipping from your terminal.

*The essential workflow — compact edition.*

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 2 · THE PROBLEM                  -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— vol 1 · mindset —</span>
  <span class="page-label">what's broken</span>
</div>

## The old way breaks flow

<div class="cards-col">
  <div class="card-row">
    <span class="card-row-icon">🔁</span>
    <div class="card-row-body">
      <h3>Endless context-switching</h3>
      <p>Editor → chatbot → terminal → copy-paste. Over and over.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">📋</span>
    <div class="card-row-body">
      <h3>The chatbot can't see your files</h3>
      <p>You describe the code. Claude Code <strong>reads</strong> the code.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">⚡</span>
    <div class="card-row-body">
      <h3>Claude Code lives in your terminal</h3>
      <p>It reads files, runs commands, and sees the results — no copy-paste.</p>
    </div>
  </div>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 3 · WHAT CLAUDE CODE CAN SEE    -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— vol 1 · context —</span>
  <span class="page-label">full project awareness</span>
</div>

## What Claude Code actually sees

<div class="cards">
  <div class="card">
    <span class="card-icon">📁</span>
    <h3>Your files & folders</h3>
    <p>The full project tree, not a snippet you pasted.</p>
  </div>
  <div class="card">
    <span class="card-icon">🔀</span>
    <h3>Git history</h3>
    <p>What changed, when, and why — in context.</p>
  </div>
  <div class="card">
    <span class="card-icon">💻</span>
    <h3>Terminal output</h3>
    <p>Errors, logs, test results — it reads what runs.</p>
  </div>
  <div class="card">
    <span class="card-icon">🚫</span>
    <h3>NOT your intentions</h3>
    <p>Constraints, history, and "don't touch X" must be stated.</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">your role</div>
  <p>You are the <strong>director</strong>, not the typist. Specify clearly — Claude handles the steps.</p>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 4 · THE WORK LOOP               -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— vol 1 · mindset —</span>
  <span class="page-label">the core loop</span>
</div>

## The Claude Code work loop

<div class="list">
  <div class="list-item">
    <span class="list-num">01</span>
    <span class="list-text"><strong>Specify</strong> — describe what exists, then what you want</span>
  </div>
  <div class="list-item">
    <span class="list-num">02</span>
    <span class="list-text"><strong>Execute</strong> — Claude plans, acts, reads results, continues</span>
  </div>
  <div class="list-item">
    <span class="list-num">03</span>
    <span class="list-text"><strong>Review</strong> — does it run? right output? nothing broken?</span>
  </div>
  <div class="list-item">
    <span class="list-num">04</span>
    <span class="list-text"><strong>Correct</strong> — paste the error + what you expected + fix it</span>
  </div>
  <div class="list-item">
    <span class="list-num">05</span>
    <span class="list-text"><strong>Repeat</strong> — one task at a time, always confirm before next</span>
  </div>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 5 · VOL 2 DIVIDER               -->
<!-- ══════════════════════════════════════ -->
<!-- _class: vol-divider -->

<div class="tag">Volume 2</div>

# The Core Workflow
## Orient → Task → Review → Fix

Setting up, writing tasks, reading output, fixing errors

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 6 · CLAUDE.MD                   -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— vol 2 · setup —</span>
  <span class="page-label">your most important file</span>
</div>

## The CLAUDE.md file

Claude Code has **no memory between sessions**. This file restores context instantly.

<div class="cards-col">
  <div class="card-row">
    <span class="card-row-icon">🧱</span>
    <div class="card-row-body">
      <h3>Tech stack + conventions</h3>
      <p>Language, framework, folder structure, naming rules.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">⚙️</span>
    <div class="card-row-body">
      <h3>Commands to run the project</h3>
      <p>How to start, test, and build — so Claude can verify its own work.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">🚧</span>
    <div class="card-row-body">
      <h3>Known constraints</h3>
      <p>What must not be touched. Silence is not a constraint.</p>
    </div>
  </div>
</div>

<div class="insight">
  <div class="insight-label">golden rule</div>
  <p>Always <strong>orient Claude Code to the current state</strong> before handing it any task.</p>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 7 · WRITING TASKS               -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— vol 2 · tasks —</span>
  <span class="page-label">what to build</span>
</div>

## Writing tasks that work

<div class="compare">
  <div class="compare-col">
    <div class="compare-label bad">✕ Vague</div>
    <h3>"Fix the login bug"</h3>
    <p>No file, no symptom, no expected behavior. Claude guesses.</p>
  </div>
  <div class="compare-col good">
    <div class="compare-label good">✓ Precise</div>
    <h3>"In auth/login.js, the token isn't being saved to localStorage after a successful POST to /api/login. Fix it."</h3>
    <p>File + symptom + expected outcome.</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">scope rule</div>
  <p>One task at a time. If you can't describe it in <strong>three sentences</strong>, it's too large for one pass.</p>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 8 · REVIEWING OUTPUT            -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— vol 2 · review —</span>
  <span class="page-label">3 questions every time</span>
</div>

## Review every output before the next task

<div class="cards-col">
  <div class="card-row">
    <span class="card-row-icon">✅</span>
    <div class="card-row-body">
      <h3>Does it run?</h3>
      <p>Start the project. A task that doesn't run is not done.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">🎯</span>
    <div class="card-row-body">
      <h3>Does it produce the right output?</h3>
      <p>Test the behavior — not just the absence of errors.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">🔍</span>
    <div class="card-row-body">
      <h3>Did it touch anything it shouldn't?</h3>
      <p>Read the git diff. Look for what changed, not just how.</p>
    </div>
  </div>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 9 · THE FIX LOOP               -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— vol 2 · fix loop —</span>
  <span class="page-label">errors are normal</span>
</div>

## The fix prompt formula

Errors are not failure. They're information Claude Code can act on.

<div class="list">
  <div class="list-item">
    <span class="list-num">1</span>
    <span class="list-text"><strong>Paste the exact error</strong> — don't paraphrase it</span>
  </div>
  <div class="list-item">
    <span class="list-num">2</span>
    <span class="list-text"><strong>Describe what you expected</strong> — what should have happened</span>
  </div>
  <div class="list-item">
    <span class="list-num">3</span>
    <span class="list-text"><strong>Ask Claude to fix it</strong> — don't manually edit mid-task</span>
  </div>
</div>

<div class="insight">
  <div class="insight-label">3-strikes rule</div>
  <p>Same error after <strong>three fix attempts</strong>? Restate the entire task from scratch — don't keep patching.</p>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 10 · VOL 3 DIVIDER              -->
<!-- ══════════════════════════════════════ -->
<!-- _class: vol-divider -->

<div class="tag">Volume 3</div>

# Doing Real Work
## Scope · Build · Automate · Test

From first feature to a working, tested project

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 11 · SCOPING                    -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— vol 3 · scope —</span>
  <span class="page-label">mvp first</span>
</div>

## Scope before you build

<div class="cards">
  <div class="card">
    <span class="card-icon">🎯</span>
    <h3>Core behavior first</h3>
    <p>Never start with settings, polish, or error handling.</p>
  </div>
  <div class="card">
    <span class="card-icon">💣</span>
    <h3>Define the blast radius</h3>
    <p>State explicitly what Claude must NOT change.</p>
  </div>
  <div class="card">
    <span class="card-icon">🗺️</span>
    <h3>Map dependencies</h3>
    <p>Which tasks must finish before others start — work in that order.</p>
  </div>
  <div class="card">
    <span class="card-icon">📝</span>
    <h3>The scope checklist</h3>
    <p>Is this one thing? Is the success condition clear? Is it bounded?</p>
  </div>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 12 · AUTOMATION                 -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— vol 3 · automate —</span>
  <span class="page-label">scripts & repetitive tasks</span>
</div>

## Claude Code excels at automation

Describe any manual task in three parts:

<div class="list">
  <div class="list-item">
    <span class="list-num">01</span>
    <span class="list-text"><strong>What I do</strong> — the manual steps you take today</span>
  </div>
  <div class="list-item">
    <span class="list-num">02</span>
    <span class="list-text"><strong>When I do it</strong> — the trigger or frequency</span>
  </div>
  <div class="list-item">
    <span class="list-num">03</span>
    <span class="list-text"><strong>What correct looks like</strong> — the expected output or outcome</span>
  </div>
</div>

<div class="insight">
  <div class="insight-label">safety rule</div>
  <p>Always run on a <strong>sample first</strong>. Scope a rollback before anything destructive.</p>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 13 · TESTING                    -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— vol 3 · testing —</span>
  <span class="page-label">high-value use case</span>
</div>

## Ask Claude Code to write your tests

<div class="cards-col">
  <div class="card-row">
    <span class="card-row-icon">🧪</span>
    <div class="card-row-body">
      <h3>Describe the behavior, not the syntax</h3>
      <p>You don't need to know the framework — Claude does.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">🔍</span>
    <div class="card-row-body">
      <h3>Ask what it did NOT test</h3>
      <p>The answer is diagnostic. Coverage gaps are often the most dangerous paths.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">🔄</span>
    <div class="card-row-body">
      <h3>Run the validation loop</h3>
      <p>Generate → run → fix failures → re-run → confirm green.</p>
    </div>
  </div>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 14 · VOL 4 DIVIDER              -->
<!-- ══════════════════════════════════════ -->
<!-- _class: vol-divider -->

<div class="tag">Volume 4</div>

# Going Further
## Manage · Automate · Recover

Growing projects, autonomous mode, and knowing the limits

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 15 · GROWING PROJECTS           -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— vol 4 · scale —</span>
  <span class="page-label">managing complexity</span>
</div>

## Managing a growing project

<div class="cards">
  <div class="card">
    <span class="card-icon">📄</span>
    <h3>CLAUDE.md is a living doc</h3>
    <p>Update it every time something important about the project changes.</p>
  </div>
  <div class="card">
    <span class="card-icon">🧩</span>
    <h3>Module prompting</h3>
    <p>When the codebase is too large for one context — prompt one module at a time.</p>
  </div>
  <div class="card">
    <span class="card-icon">⚠️</span>
    <h3>Watch for drift</h3>
    <p>Repeated mistakes and ignored constraints are signals — not normal operation.</p>
  </div>
  <div class="card">
    <span class="card-icon">🔄</span>
    <h3>Session brief</h3>
    <p>Write a one-minute orientation prompt before every new session.</p>
  </div>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 16 · AUTONOMOUS MODE            -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— vol 4 · agent mode —</span>
  <span class="page-label">use with care</span>
</div>

## Autonomous agent mode

Claude plans and executes multi-step tasks without checking in between.

<div class="compare">
  <div class="compare-col good">
    <div class="compare-label good">✓ Use when</div>
    <h3>Safe to automate</h3>
    <p>Well-scoped task, clear success condition, bounded blast radius, reversible changes.</p>
  </div>
  <div class="compare-col">
    <div class="compare-label bad">✕ Avoid when</div>
    <h3>High stakes</h3>
    <p>Production data, irreversible actions, ambiguous success condition.</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">prompt structure for autonomous mode</div>
  <p><strong>Goal + constraints + stop condition + how to signal completion.</strong> Make permissions explicit.</p>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 17 · THE ONE RULE               -->
<!-- ══════════════════════════════════════ -->

<div style="display:flex;flex-direction:column;justify-content:center;height:100%;text-align:center;align-items:center;">
  <div class="tag" style="justify-content:center;margin-bottom:24px;">the one rule</div>
  <h1 style="font-size:52px;line-height:1.1;letter-spacing:-2px;">Always describe<br>what exists<br>before what you want</h1>
  <p style="font-size:17px;color:var(--subtle);margin-top:20px;max-width:520px;line-height:1.6;">Every technique in Claude Code boils down to this. Orient first — orient always.</p>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 18 · CTA                         -->
<!-- ══════════════════════════════════════ -->
<!-- _class: cta -->

<div class="tag" style="justify-content:center;color:#0a0a0a;margin-bottom:20px;">
  Claude Code 101
</div>

# Ready to ship from the terminal?

## Create your CLAUDE.md. Pick one task. Run it.

<p>One focused session per day compounds faster than occasional marathons.</p>

<div class="handle">Mini Tutorial · Vol 1 – Vol 4</div>