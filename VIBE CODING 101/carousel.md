---
marp: true
paginate: true
html: true
size: 4:3
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,400;0,500;0,600;1,400&family=DM+Mono:wght@400;500&display=swap');

  :root {
    --amber:       #f59e0b;
    --amber-dim:   #d97706;
    --green:       #22c55e;
    --white:       #f1f5f9;
    --off-white:   #cbd5e1;
    --subtle:      #94a3b8;
    --muted:       #64748b;
    --bg:          #080808;
    --card-bg:     #111111;
    --card-border: #222222;
  }

  section {
    font-family: 'DM Sans', sans-serif;
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
    font-weight: 700;
    line-height: 1.08;
    margin: 0 0 14px 0;
    color: var(--white);
    letter-spacing: -1.5px;
  }
  h2 {
    font-size: 28px;
    font-weight: 700;
    line-height: 1.1;
    margin: 0 0 14px 0;
    color: var(--white);
    letter-spacing: -1px;
    border: none;
  }
  p {
    font-size: 16px;
    line-height: 1.6;
    color: var(--subtle);
    margin: 0 0 12px 0;
  }
  strong { color: var(--white); font-weight: 600; }
  em     { color: var(--muted); font-style: normal; }

  /* TAG */
  .tag {
    display: flex;
    align-items: center;
    gap: 12px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 3px;
    color: var(--amber);
    text-transform: uppercase;
    margin-bottom: 18px;
  }
  .tag::before {
    content: '';
    display: block;
    width: 24px;
    height: 2px;
    background: var(--amber);
    flex-shrink: 0;
  }

  /* HEADER ROW */
  .header-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
  }
  .page-num {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--amber-dim);
    letter-spacing: 2px;
    text-transform: uppercase;
  }
  .page-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--muted);
  }

  /* CARDS 2-col */
  .cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-bottom: 12px;
  }
  .card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 10px;
    padding: 14px;
  }
  .card-icon { font-size: 17px; margin-bottom: 6px; display: block; }
  .card h3 {
    font-size: 14px;
    font-weight: 600;
    color: var(--white);
    margin: 0 0 4px;
  }
  .card p {
    font-size: 13px;
    color: var(--subtle);
    line-height: 1.45;
    margin: 0;
  }

  /* CARDS 1-col stacked */
  .cards-col { display: flex; flex-direction: column; gap: 8px; margin-bottom: 12px; }
  .card-row {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 10px;
    padding: 12px 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }
  .card-row-icon { font-size: 17px; flex-shrink: 0; margin-top: 1px; }
  .card-row-body h3 {
    font-size: 14px;
    font-weight: 600;
    color: var(--white);
    margin: 0 0 3px;
  }
  .card-row-body p {
    font-size: 13px;
    color: var(--subtle);
    margin: 0;
    line-height: 1.45;
  }

  /* COMPARE 2-col */
  .compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-bottom: 10px;
  }
  .compare-col {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 10px;
    padding: 14px 16px;
  }
  .compare-col.good { border-color: #14532d; }
  .compare-label {
    font-family: 'DM Mono', monospace;
    font-size: 9px;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 6px;
    color: var(--muted);
  }
  .compare-label.bad  { color: #ef4444; }
  .compare-label.good { color: var(--green); }
  .compare-col h3 {
    font-size: 14px;
    font-weight: 600;
    color: var(--white);
    margin: 0 0 5px;
  }
  .compare-col p {
    font-size: 13px;
    color: var(--subtle);
    line-height: 1.45;
    margin: 0;
  }

  /* LIST numbered rows */
  .list { display: flex; flex-direction: column; gap: 7px; margin-bottom: 12px; }
  .list-item {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 8px;
    padding: 10px 14px;
  }
  .list-num {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--amber);
    flex-shrink: 0;
    margin-top: 1px;
    min-width: 18px;
  }
  .list-text { font-size: 13.5px; color: var(--subtle); line-height: 1.45; }
  .list-text strong { color: var(--white); }

  /* INSIGHT BOX */
  .insight {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 10px;
    padding: 12px 18px;
    margin-top: auto;
  }
  .insight-label {
    font-family: 'DM Mono', monospace;
    font-size: 9px;
    letter-spacing: 3px;
    color: var(--muted);
    text-transform: uppercase;
    margin-bottom: 4px;
  }
  .insight p { font-size: 14px; color: var(--off-white); line-height: 1.5; margin: 0; }

  /* LOOP ROW */
  .loop {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0;
    margin: 16px 0 14px;
  }
  .loop-step {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 10px;
    padding: 12px 14px;
    text-align: center;
    min-width: 100px;
  }
  .loop-step .ls-icon { font-size: 18px; margin-bottom: 4px; display: block; }
  .loop-step .ls-label { font-size: 12px; font-weight: 600; color: var(--white); }
  .loop-arrow { font-size: 16px; color: var(--amber); padding: 0 8px; }

  /* COVER */
  section.cover {
    justify-content: flex-end;
    padding-bottom: 80px;
    background: #050505;
  }
  section.cover h1 { font-size: 48px; }
  section.cover p  { font-size: 17px; color: var(--subtle); }

  /* LVL DIVIDER */
  section.lvl-divider {
    justify-content: center;
    border-left: 5px solid var(--amber);
    background: #0c0c0c;
  }
  section.lvl-divider .tag { margin-bottom: 20px; }
  section.lvl-divider h1   { font-size: 44px; color: var(--amber); margin-bottom: 10px; }
  section.lvl-divider h2   { font-size: 24px; color: var(--white); border: none; margin: 0 0 16px; }
  section.lvl-divider p    { font-size: 15px; color: var(--muted); }

  /* CTA */
  section.cta {
    justify-content: center;
    align-items: center;
    text-align: center;
    background: var(--amber);
  }
  section.cta h1 { color: #0F0F0F; font-size: 40px; letter-spacing: -1px; margin-bottom: 10px; }
  section.cta h2 { color: #3a2e00; font-size: 22px; border: none; margin-bottom: 12px; }
  section.cta p  { color: #5a4700; font-size: 16px; max-width: 540px; margin: 0; }
  section.cta .handle {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #7a6000;
    margin-top: 22px;
    letter-spacing: 2px;
    text-transform: uppercase;
  }
  section.cta .tag { color: #0a0a0a; margin-bottom: 20px; justify-content: center; }
  section.cta .tag::before { background: #0a0a0a; }

  /* FOOTER */
  section::after {
    font-family: 'DM Mono', monospace;
    font-size: 9px;
    color: var(--muted);
    letter-spacing: 1px;
    content: 'Vibe Coding 101 · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
    position: absolute;
    bottom: 20px;
    right: 40px;
  }
---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 1 · COVER                        -->
<!-- ══════════════════════════════════════ -->
<!-- _class: cover -->

<div class="tag">Beginner Guide · Lvl 1–4</div>

# Vibe Coding 101

Build real things without being a developer.
The Cursor + Claude stack — from first principles to shipping.

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 2 · LVL 1 DIVIDER                -->
<!-- ══════════════════════════════════════ -->
<!-- _class: lvl-divider -->

<div class="tag">LEVEL 1</div>

# Mindset & The Stack
## What vibe coding actually is

Directing AI to write code · You are the architect · Cursor + Claude

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 3 · WHAT IS VIBE CODING          -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— lvl 1 · mindset —</span>
  <span class="page-label">the shift</span>
</div>

## You are not the programmer

You are the **architect and reviewer**. AI writes the code.

<div class="compare">
  <div class="compare-col">
    <div class="compare-label bad">❌ The old way</div>
    <h3>Learn to code first</h3>
    <p>Years of study before you can build anything real.</p>
  </div>
  <div class="compare-col good">
    <div class="compare-label good">✅ Vibe coding</div>
    <h3>Describe → Generate</h3>
    <p>You know what you want. Claude writes it. You review it.</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">the one skill that matters</div>
  <p>Knowing what you want <strong>clearly enough to describe it</strong>.</p>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 4 · THE STACK                    -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— lvl 1 · the stack —</span>
  <span class="page-label">cursor + claude</span>
</div>

## The Cursor + Claude stack

<div class="cards">
  <div class="card">
    <span class="card-icon">🖥️</span>
    <h3>Cursor</h3>
    <p>VS Code with AI baked in. Reads your entire codebase, not just your message.</p>
  </div>
  <div class="card">
    <span class="card-icon">🤖</span>
    <h3>Claude</h3>
    <p>Writes, fixes, and explains your code — with full project context.</p>
  </div>
  <div class="card">
    <span class="card-icon">💬</span>
    <h3>Chat · Cmd+L</h3>
    <p>Ask questions and get explanations about your code.</p>
  </div>
  <div class="card">
    <span class="card-icon">⚡</span>
    <h3>Agent · Cmd+I</h3>
    <p>Build across multiple files at once. Your main workhorse.</p>
  </div>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 5 · THE BUILD LOOP               -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— lvl 1 · mindset —</span>
  <span class="page-label">the build loop</span>
</div>

## The build loop

<div class="loop">
  <div class="loop-step">
    <span class="ls-icon">📝</span>
    <span class="ls-label">Describe</span>
  </div>
  <span class="loop-arrow">→</span>
  <div class="loop-step">
    <span class="ls-icon">⚡</span>
    <span class="ls-label">Generate</span>
  </div>
  <span class="loop-arrow">→</span>
  <div class="loop-step">
    <span class="ls-icon">👁️</span>
    <span class="ls-label">Review</span>
  </div>
  <span class="loop-arrow">→</span>
  <div class="loop-step">
    <span class="ls-icon">🔧</span>
    <span class="ls-label">Fix</span>
  </div>
  <span class="loop-arrow">→</span>
  <div class="loop-step">
    <span class="ls-icon">🔁</span>
    <span class="ls-label">Repeat</span>
  </div>
</div>

<div class="insight">
  <div class="insight-label">beginner truth</div>
  <p>Errors are <strong>normal</strong> — not failure. Every error has a prompt that fixes it. Claude will fix them too.</p>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 6 · LVL 2 DIVIDER                -->
<!-- ══════════════════════════════════════ -->
<!-- _class: lvl-divider -->

<div class="tag">LEVEL 2</div>

# The Core Workflow
## Prompts that actually build things

Brief · Prompt · Review · Fix

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 7 · WRITING PROMPTS              -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— lvl 2 · workflow —</span>
  <span class="page-label">prompting right</span>
</div>

## Writing prompts that build

<div class="list">
  <div class="list-item">
    <span class="list-num">01</span>
    <span class="list-text"><strong>Write a project brief first</strong> — what it is, who it's for, what it does</span>
  </div>
  <div class="list-item">
    <span class="list-num">02</span>
    <span class="list-text"><strong>One thing at a time</strong> — never ask for the whole app in one prompt</span>
  </div>
  <div class="list-item">
    <span class="list-num">03</span>
    <span class="list-text"><strong>Use @filename</strong> so Claude knows what already exists before adding more</span>
  </div>
  <div class="list-item">
    <span class="list-num">04</span>
    <span class="list-text"><strong>Test every change</strong> before asking for the next one</span>
  </div>
</div>

<div class="insight">
  <div class="insight-label">anatomy of a good build prompt</div>
  <p>What to build + where it goes + how it should behave.</p>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 8 · THE FIX LOOP                 -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— lvl 2 · fix loop —</span>
  <span class="page-label">when things break</span>
</div>

## The fix loop

<div class="cards-col">
  <div class="card-row">
    <span class="card-row-icon">📋</span>
    <div class="card-row-body">
      <h3>Paste the error directly into Cursor Chat</h3>
      <p>Formula: <strong>error + what I expected + "fix it"</strong></p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">🚫</span>
    <div class="card-row-body">
      <h3>Never manually edit code as a beginner</h3>
      <p>Let Claude make every change — even tiny ones.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">🔄</span>
    <div class="card-row-body">
      <h3>Three fixes deep on the same error?</h3>
      <p>Stop. Describe the feature from scratch instead.</p>
    </div>
  </div>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 9 · LVL 3 DIVIDER                -->
<!-- ══════════════════════════════════════ -->
<!-- _class: lvl-divider -->

<div class="tag">LEVEL 3</div>

# Building Real Things
## Scope · Build · Ship

MVP mindset · Page by page · Deploy with Vercel

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 10 · SCOPING YOUR BUILD          -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— lvl 3 · building —</span>
  <span class="page-label">scope it right</span>
</div>

## Scope your first build

<div class="compare">
  <div class="compare-col">
    <div class="compare-label bad">❌ The beginner trap</div>
    <h3>Build everything at once</h3>
    <p>Too big to finish. Guaranteed to stall before shipping.</p>
  </div>
  <div class="compare-col good">
    <div class="compare-label good">✅ MVP mindset</div>
    <h3>Smallest version that works</h3>
    <p>Write every feature. Cut in half. Cut again.</p>
  </div>
</div>

<div class="cards">
  <div class="card">
    <span class="card-icon">⚙️</span>
    <h3>Core action first</h3>
    <p>Always build the main feature. Never start with settings.</p>
  </div>
  <div class="card">
    <span class="card-icon">🚀</span>
    <h3>Deploy with Vercel</h3>
    <p>Live link in under 5 minutes. Share before it's perfect.</p>
  </div>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 11 · LVL 4 DIVIDER               -->
<!-- ══════════════════════════════════════ -->
<!-- _class: lvl-divider -->

<div class="tag">LEVEL 4</div>

# Going Further
## Managing growth & building the habit

SPEC file · Know your limits · Weekly builds

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 12 · MANAGING A GROWING PROJECT  -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— lvl 4 · going further —</span>
  <span class="page-label">stay in control</span>
</div>

## Managing a growing project

<div class="list">
  <div class="list-item">
    <span class="list-num">01</span>
    <span class="list-text"><strong>Keep a SPEC file</strong> — a living doc describing your entire project</span>
  </div>
  <div class="list-item">
    <span class="list-num">02</span>
    <span class="list-text"><strong>Pin it with @SPEC</strong> at the start of every new Agent session</span>
  </div>
  <div class="list-item">
    <span class="list-num">03</span>
    <span class="list-text"><strong>Claude has no memory</strong> between sessions — your SPEC is its memory</span>
  </div>
  <div class="list-item">
    <span class="list-num">04</span>
    <span class="list-text"><strong>One build per week</strong> beats one big build never</span>
  </div>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 13 · WHEN VIBE CODING BREAKS     -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— lvl 4 · limits —</span>
  <span class="page-label">know when to stop</span>
</div>

## When vibe coding breaks down

<div class="cards">
  <div class="card">
    <span class="card-icon">🌀</span>
    <h3>Complexity outgrows context</h3>
    <p>Claude can't hold everything in mind. Simplify scope first.</p>
  </div>
  <div class="card">
    <span class="card-icon">📋</span>
    <h3>Copy-paste trap</h3>
    <p>Duplicating code across files causes compounding errors.</p>
  </div>
  <div class="card">
    <span class="card-icon">🔄</span>
    <h3>Restart protocol</h3>
    <p>Salvage the SPEC. Leave broken code behind. Start clean.</p>
  </div>
  <div class="card">
    <span class="card-icon">🧑‍💻</span>
    <h3>Bring in a developer</h3>
    <p>Vibe coding is a starting point — not a ceiling.</p>
  </div>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 14 · THE ONE RULE                -->
<!-- ══════════════════════════════════════ -->

<div style="display:flex;flex-direction:column;justify-content:center;height:100%;text-align:center;align-items:center;">
  <div class="tag" style="justify-content:center;margin-bottom:24px;">the builder identity</div>
  <h1 style="font-size:50px;line-height:1.12;letter-spacing:-2px;">Ship it.<br>Learn from it.<br>Build again.</h1>
  <p style="font-size:16px;color:var(--subtle);margin-top:20px;max-width:520px;line-height:1.6;">You don't need a CS degree. You need a clear idea, a good brief, and the habit of building something small every week.</p>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 15 · CTA                         -->
<!-- ══════════════════════════════════════ -->
<!-- _class: cta -->

<div class="tag">Vibe Coding 101 · Lvl 1–4</div>

# Ready to build?

## Write down one thing you've wanted to build.

<p>That's your first project. Open Cursor. Start today.</p>

<div class="handle">cursor + claude · start free</div>