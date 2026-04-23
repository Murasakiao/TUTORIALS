---
marp: true
theme: default
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=DM+Mono:wght@400;500&display=swap');

  :root {
    --blue: #2563eb;
    --blue-light: #eff6ff;
    --blue-mid: #bfdbfe;
    --text: #111827;
    --muted: #6b7280;
    --border: #e5e7eb;
    --white: #ffffff;
    --off-white: #f9fafb;
  }

  section {
    font-family: 'DM Sans', sans-serif;
    background: var(--white);
    color: var(--text);
    padding: 52px 64px;
    font-size: 18px;
    line-height: 1.6;
  }

  section::after {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: var(--muted);
  }

  h1 {
    font-family: 'DM Sans', sans-serif;
    font-size: 42px;
    font-weight: 600;
    color: var(--text);
    line-height: 1.2;
    margin-bottom: 0.4em;
  }

  h2 {
    font-family: 'DM Sans', sans-serif;
    font-size: 28px;
    font-weight: 600;
    color: var(--text);
    border-bottom: 2px solid var(--blue);
    padding-bottom: 10px;
    margin-bottom: 24px;
  }

  h3 {
    font-family: 'DM Sans', sans-serif;
    font-size: 20px;
    font-weight: 500;
    color: var(--blue);
    margin-bottom: 8px;
  }

  p { color: var(--text); margin: 0.4em 0; }
  ul { padding-left: 1.4em; }
  li { margin-bottom: 10px; color: var(--text); }
  strong { color: var(--blue); font-weight: 600; }

  code {
    font-family: 'DM Mono', monospace;
    background: var(--blue-light);
    color: var(--blue);
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.88em;
  }

  blockquote {
    border-left: 4px solid var(--blue);
    background: var(--blue-light);
    padding: 16px 20px;
    margin: 20px 0;
    border-radius: 0 8px 8px 0;
    font-family: 'DM Mono', monospace;
    font-size: 0.82em;
    color: #1e40af;
    line-height: 1.6;
  }

  blockquote p { color: #1e40af; margin: 0; }

  section.cover {
    background: var(--text);
    color: var(--white);
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  section.cover h1 { color: var(--white); font-size: 46px; }
  section.cover h2 { color: #93c5fd; border-bottom-color: #374151; }
  section.cover p  { color: #9ca3af; }
  section.cover strong { color: #60a5fa; }
  section.cover code { background: #1e3a5f; color: #93c5fd; }

  section.step { background: var(--off-white); }

  .highlight {
    background: var(--blue-light);
    border: 1px solid var(--blue-mid);
    border-radius: 10px;
    padding: 18px 24px;
    margin: 16px 0;
  }

  .highlight.good {
    background: #f0fdf4;
    border-color: #bbf7d0;
  }

  .highlight.warn {
    background: #fefce8;
    border-color: #fde68a;
  }

  .tools {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 16px;
  }

  .tool-card {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px 20px;
  }

  .tool-card .icon  { font-size: 24px; margin-bottom: 6px; }
  .tool-card .name  { font-weight: 600; font-size: 15px; color: var(--text); }
  .tool-card .desc  { font-size: 13px; color: var(--muted); margin-top: 2px; }

  .step-badge {
    display: inline-block;
    background: var(--blue);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    padding: 4px 14px;
    border-radius: 999px;
    margin-bottom: 12px;
    letter-spacing: 0.05em;
  }

  section.final {
    background: var(--blue);
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
  }

  section.final h1 { color: white; font-size: 40px; }
  section.final p  { color: #bfdbfe; font-size: 18px; }
  section.final strong { color: white; }
  section.final em { color: #bfdbfe; }

  /* Quit cycle diagram */
  .quit-cycle {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0;
    align-items: center;
    margin: 16px 0;
  }

  .qc-node {
    background: #111827;
    border-radius: 8px;
    padding: 14px 12px;
    text-align: center;
  }

  .qc-node .qn-icon  { font-size: 22px; margin-bottom: 6px; }
  .qc-node .qn-label { font-family: 'DM Mono', monospace; font-size: 12px; font-weight: 600; margin-bottom: 4px; }
  .qc-node .qn-desc  { font-size: 11px; color: #6b7280; line-height: 1.4; }

  .qc-node.q1 .qn-label { color: #60a5fa; }
  .qc-node.q2 .qn-label { color: #fde68a; }
  .qc-node.q3 .qn-label { color: #f87171; }
  .qc-node.q4 .qn-label { color: #9ca3af; }

  .qc-arrow { text-align: center; color: #374151; font-size: 18px; padding: 0 4px; }

  /* Motivation vs systems compare */
  .motivation-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 14px 0;
  }

  .mv-card {
    border-radius: 10px;
    overflow: hidden;
  }

  .mv-card .mvc-header {
    padding: 9px 16px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }

  .mv-card.motivation .mvc-header { background: #451a03; color: #fde68a; }
  .mv-card.systems    .mvc-header { background: #14532d; color: #86efac; }

  .mv-card .mvc-body {
    background: #0d1117;
    padding: 14px 16px;
    font-size: 13px;
    line-height: 2;
  }

  .mv-card.motivation .mvc-body { border: 1px solid #451a03; border-top: none; border-radius: 0 0 10px 10px; color: #fde68a; }
  .mv-card.systems    .mvc-body { border: 1px solid #14532d; border-top: none; border-radius: 0 0 10px 10px; color: #86efac; }

  /* Habit stack diagram */
  .habit-stack {
    background: #111827;
    border-radius: 10px;
    padding: 18px 22px;
    margin: 14px 0;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
  }

  .hs-row {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 10px;
  }

  .hs-row:last-child { margin-bottom: 0; }

  .hs-badge {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 999px;
    flex-shrink: 0;
    min-width: 70px;
    text-align: center;
  }

  .hs-badge.anchor  { background: #1e3a5f; color: #60a5fa; }
  .hs-badge.cue     { background: #14532d; color: #86efac; }
  .hs-badge.routine { background: #2e1065; color: #c4b5fd; }
  .hs-badge.reward  { background: #451a03; color: #fde68a; }

  .hs-text { font-size: 13px; color: #d1d5db; line-height: 1.5; }
  .hs-text span { font-family: 'DM Mono', monospace; color: #60a5fa; }

  /* Tiny goals grid */
  .tiny-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 14px 0;
  }

  .tiny-card {
    border-radius: 10px;
    overflow: hidden;
  }

  .tiny-card .tc-header {
    padding: 8px 14px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.07em;
  }

  .tiny-card.too-big  .tc-header { background: #7f1d1d; color: #fca5a5; }
  .tiny-card.just-right .tc-header { background: #14532d; color: #86efac; }

  .tiny-card .tc-body {
    background: #0d1117;
    padding: 12px 14px;
    font-size: 13px;
    line-height: 2;
  }

  .tiny-card.too-big    .tc-body { border: 1px solid #7f1d1d; border-top: none; border-radius: 0 0 10px 10px; color: #f87171; }
  .tiny-card.just-right .tc-body { border: 1px solid #14532d; border-top: none; border-radius: 0 0 10px 10px; color: #86efac; }

  /* Progress tracker mock */
  .tracker-mock {
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
  }

  .tracker-bar-row {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 9px 16px;
    border-bottom: 1px solid #21262d;
  }

  .tracker-bar-row:last-child { border-bottom: none; }

  .tracker-bar-row .tbr-label { color: #8b949e; min-width: 120px; flex-shrink: 0; }

  .tbr-track {
    flex: 1;
    height: 10px;
    background: #1f2937;
    border-radius: 5px;
    overflow: hidden;
  }

  .tbr-fill {
    height: 100%;
    border-radius: 5px;
  }

  .tbr-fill.w100 { width: 100%; background: #2563eb; }
  .tbr-fill.w80  { width: 80%;  background: #2563eb; }
  .tbr-fill.w65  { width: 65%;  background: #2563eb; opacity: 0.7; }
  .tbr-fill.w40  { width: 40%;  background: #374151; }
  .tbr-fill.w20  { width: 20%;  background: #374151; opacity: 0.5; }

  .tracker-bar-row .tbr-pct { color: #60a5fa; min-width: 36px; text-align: right; font-weight: 600; }
  .tracker-bar-row .tbr-pct.dim { color: #4b5563; }

  /* Burnout warning cards */
  .burnout-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin: 14px 0;
  }

  .burnout-card {
    background: #fff1f2;
    border: 1px solid #fecdd3;
    border-radius: 8px;
    padding: 13px 15px;
  }

  .burnout-card .bc-icon  { font-size: 18px; margin-bottom: 6px; }
  .burnout-card .bc-sign  { font-size: 13px; font-weight: 600; color: #9f1239; margin-bottom: 4px; }
  .burnout-card .bc-fix   { font-size: 12px; color: #be123c; line-height: 1.5; }

  /* two-col */
  .two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 16px;
  }

  .col-card {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px 20px;
  }

  .col-card .label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 8px;
  }
---

<!-- _class: cover -->

# Stay Consistent
## When Learning to Code

&nbsp;

**Motivation gets you started.** Systems keep you going.

`habit` · `tiny goals` · `tracking` · `recovery` · `identity`

---

## Why People Quit

Most people don't quit because coding is too hard. They quit because of a predictable, avoidable cycle.

<div class="quit-cycle">
  <div class="qc-node q1">
    <div class="qn-icon">🔥</div>
    <div class="qn-label">Excited</div>
    <div class="qn-desc">New course, new language. Energy is high. Hours fly by.</div>
  </div>
  <div class="qc-arrow">→</div>
  <div class="qc-node q2">
    <div class="qn-icon">🧱</div>
    <div class="qn-label">Stuck</div>
    <div class="qn-desc">Hit a hard concept. Progress slows. Sessions get shorter.</div>
  </div>
  <div class="qc-arrow">→</div>
  <div class="qc-node q3">
    <div class="qn-icon">😔</div>
    <div class="qn-label">Skipped</div>
    <div class="qn-desc">Miss one day. Then three. Guilt makes returning harder.</div>
  </div>
  <div class="qc-arrow">→</div>
  <div class="qc-node q4">
    <div class="qn-icon">🔄</div>
    <div class="qn-label">Restart</div>
    <div class="qn-desc">"I'll start fresh on Monday with a new framework."</div>
  </div>
</div>

The exit point is almost always Step 3 — not because coding got harder, but because the gap between missed sessions grows until returning feels impossible.

<div class="highlight warn">

The solution is not more motivation. It's designing a system where skipping once doesn't spiral into quitting.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## The Motivation Trap

Motivation is a feeling. It rises and falls. Building a learning practice on top of motivation is building on sand.

<div class="motivation-compare">
  <div class="mv-card motivation">
    <div class="mvc-header">⚠️ Motivation-dependent learning</div>
    <div class="mvc-body">
      ✦ Only codes when inspired<br>
      ✦ 3-hour sessions or nothing<br>
      ✦ Skips when tired, busy, or stuck<br>
      ✦ Progress is inconsistent and unpredictable<br>
      ✦ Quits when motivation runs out
    </div>
  </div>
  <div class="mv-card systems">
    <div class="mvc-header">✅ Systems-based learning</div>
    <div class="mvc-body">
      ✦ Codes on schedule, regardless of how it feels<br>
      ✦ 20-minute minimum — always achievable<br>
      ✦ Skipping is allowed — missing twice is not<br>
      ✦ Progress is slow, visible, and cumulative<br>
      ✦ Identity shifts: "I'm someone who codes daily"
    </div>
  </div>
</div>

<div class="highlight">

**The identity shift is the real goal.** "I'm trying to learn to code" and "I'm a developer" produce completely different behaviour when you're tired, busy, or stuck. The habit comes first. The identity follows.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Build a Daily Habit

Habit stacking — attaching your coding session to an existing anchor — is the most reliable way to make it stick.

<div class="habit-stack">
  <div class="hs-row">
    <span class="hs-badge anchor">Anchor</span>
    <span class="hs-text">An existing habit you already do without thinking. <span>Morning coffee. Post-lunch break. Before sleep.</span></span>
  </div>
  <div class="hs-row">
    <span class="hs-badge cue">Cue</span>
    <span class="hs-text">The trigger that starts the session. <span>Laptop open. IDE loaded. No phone within reach.</span> Make it frictionless.</span>
  </div>
  <div class="hs-row">
    <span class="hs-badge routine">Routine</span>
    <span class="hs-text">The minimum viable session. Even <span>20 minutes of writing one function</span> counts. Motion beats perfection.</span>
  </div>
  <div class="hs-row">
    <span class="hs-badge reward">Reward</span>
    <span class="hs-text">Immediate. Concrete. <span>Mark the streak. Log the day. Ship something small.</span> The reward keeps the loop alive.</span>
  </div>
</div>

<div class="two-col">
  <div class="col-card">
    <div class="label">Example habit stack</div>
    <p style="font-size:14px; margin-top:8px; color:#374151; line-height:1.9;">After morning coffee → open VS Code → work on one specific problem for 20 minutes → log it in a text file or Notion</p>
  </div>
  <div class="col-card">
    <div class="label">The two-day rule</div>
    <p style="font-size:14px; margin-top:8px; color:#374151; line-height:1.9;">Missing one day is fine. Missing two in a row breaks the chain. One missed day is a rest. Two is a slide. Three is a pattern.</p>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Set Tiny Goals

The biggest reason sessions don't happen: the goal is too large to start when energy is low.

<div class="tiny-grid">
  <div class="tiny-card too-big">
    <div class="tc-header">❌ Too big — easy to skip</div>
    <div class="tc-body">
      "Today I'll learn OOP in Python"<br>
      "I'll finish the whole pandas chapter"<br>
      "I need 2 hours or it's not worth it"<br>
      "I'll build the full app today"
    </div>
  </div>
  <div class="tiny-card just-right">
    <div class="tc-header">✅ Tiny — always startable</div>
    <div class="tc-body">
      "Write one function that reads a CSV"<br>
      "Learn what groupby does — one example"<br>
      "Fix this one error I left open yesterday"<br>
      "Add input validation to one endpoint"
    </div>
  </div>
</div>

<div class="highlight good">

**The starting trick:** commit to just 5 minutes. Open the file, read the last thing you wrote, type one line. You will almost always keep going. The barrier to starting is the only barrier that matters — once you're in, momentum takes over.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Track Progress Visibly

What gets measured gets maintained. Visible progress creates its own motivation — momentum you can see.

<div class="tracker-mock">
  <div class="tracker-bar-row">
    <span class="tbr-label">Python basics</span>
    <div class="tbr-track"><div class="tbr-fill w100"></div></div>
    <span class="tbr-pct">done ✓</span>
  </div>
  <div class="tracker-bar-row">
    <span class="tbr-label">File I/O + CSV</span>
    <div class="tbr-track"><div class="tbr-fill w100"></div></div>
    <span class="tbr-pct">done ✓</span>
  </div>
  <div class="tracker-bar-row">
    <span class="tbr-label">pandas basics</span>
    <div class="tbr-track"><div class="tbr-fill w80"></div></div>
    <span class="tbr-pct">80%</span>
  </div>
  <div class="tracker-bar-row">
    <span class="tbr-label">Flask intro</span>
    <div class="tbr-track"><div class="tbr-fill w65"></div></div>
    <span class="tbr-pct">65%</span>
  </div>
  <div class="tracker-bar-row">
    <span class="tbr-label">Git + GitHub</span>
    <div class="tbr-track"><div class="tbr-fill w40"></div></div>
    <span class="tbr-pct dim">40%</span>
  </div>
  <div class="tracker-bar-row">
    <span class="tbr-label">Build project</span>
    <div class="tbr-track"><div class="tbr-fill w20"></div></div>
    <span class="tbr-pct dim">20%</span>
  </div>
</div>

Seeing two items fully complete makes quitting feel like throwing away sunk cost. **Progress is a retention mechanism.**

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## Avoid Burnout Before It Happens

Burnout isn't caused by working too much. It's caused by working without recovery or visible progress.

<div class="burnout-grid">
  <div class="burnout-card">
    <div class="bc-icon">😵</div>
    <div class="bc-sign">Everything feels hard</div>
    <div class="bc-fix">Switch to something easier — review old code instead of writing new. Motion without strain.</div>
  </div>
  <div class="burnout-card">
    <div class="bc-icon">🌀</div>
    <div class="bc-sign">Context switching constantly</div>
    <div class="bc-fix">Lock in one language and one project. Tutorial hopping destroys momentum — finish before starting anything new.</div>
  </div>
  <div class="burnout-card">
    <div class="bc-icon">📊</div>
    <div class="bc-sign">No visible progress</div>
    <div class="bc-fix">Refactor old code, add a README, or ship something small. Shipping creates the feeling of forward motion.</div>
  </div>
  <div class="burnout-card">
    <div class="bc-icon">🏆</div>
    <div class="bc-sign">Comparing to experts</div>
    <div class="bc-fix">Compare to yourself 30 days ago, not to senior developers with 5 years of experience. Progress is relative to your start.</div>
  </div>
  <div class="burnout-card">
    <div class="bc-icon">🔇</div>
    <div class="bc-sign">Learning in isolation</div>
    <div class="bc-fix">Share one thing you learned publicly each week — Threads, LinkedIn, a Discord. Accountability and connection both help.</div>
  </div>
  <div class="burnout-card">
    <div class="bc-icon">🛑</div>
    <div class="bc-sign">Skipped 3+ days in a row</div>
    <div class="bc-fix">Don't restart — continue. Open the last file you had open. Read it. Write one line. You don't lose what you learned.</div>
  </div>
</div>

---

## The Consistency System — One Page

<div class="two-col">
  <div class="col-card">
    <div class="label">Daily non-negotiables</div>
    <p style="font-size:14px; margin-top:8px; color:#374151; line-height:2;">
      ✦ Same time, same trigger, every day<br>
      ✦ 20-minute minimum — always achievable<br>
      ✦ One specific goal per session, written down<br>
      ✦ Log it — even "read one function" counts<br>
      ✦ Never miss twice in a row
    </p>
  </div>
  <div class="col-card">
    <div class="label">When you're struggling</div>
    <p style="font-size:14px; margin-top:8px; color:#374151; line-height:2;">
      ✦ Do 5 minutes — just open the file<br>
      ✦ Review old code instead of writing new<br>
      ✦ Switch to a different part of the project<br>
      ✦ Ship something small to restore momentum<br>
      ✦ Ask for help — stuck is not failing
    </p>
  </div>
</div>

<div class="highlight good">

**The long game:** 20 minutes per day = 120 hours in a year. That's more than most people who take courses, attend bootcamps, or binge tutorials on weekends. Slow and steady isn't a consolation — it's the fastest sustainable path.

</div>

---

<!-- _class: final -->

# You don't need motivation.
# You need a system
# you can't easily quit.

&nbsp;

Show up small. Show up often. The skill builds itself.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*