---
marp: true
theme: default
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,400;0,500;0,600;1,400&family=DM+Mono:wght@400;500&display=swap');

  :root {
    --amber: #d97706;
    --amber-light: #fffbeb;
    --amber-mid: #fde68a;
    --amber-dim: #b45309;
    --text: #1c1917;
    --muted: #78716c;
    --border: #e7e5e4;
    --white: #ffffff;
    --off-white: #fafaf9;
    --slate: #44403c;
  }

  section {
    font-family: 'DM Sans', sans-serif;
    background: var(--white);
    color: var(--text);
    padding: 52px 64px;
    font-size: 18px;
    line-height: 1.65;
  }

  section::after {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
  }

  h1 {
    font-family: 'DM Sans', sans-serif;
    font-size: 42px;
    font-weight: 600;
    color: var(--text);
    line-height: 1.15;
    margin-bottom: 0.4em;
    letter-spacing: -0.5px;
  }

  h2 {
    font-family: 'DM Sans', sans-serif;
    font-size: 27px;
    font-weight: 600;
    color: var(--text);
    border-bottom: 1.5px solid var(--border);
    padding-bottom: 10px;
    margin-bottom: 22px;
    letter-spacing: -0.3px;
  }

  h3 {
    font-family: 'DM Sans', sans-serif;
    font-size: 19px;
    font-weight: 500;
    color: var(--amber);
    margin-bottom: 8px;
  }

  p { color: var(--text); margin: 0.4em 0; }
  ul { padding-left: 1.4em; }
  li { margin-bottom: 10px; color: var(--text); }
  strong { color: var(--amber-dim); font-weight: 600; }

  code {
    font-family: 'DM Mono', monospace;
    background: var(--amber-light);
    color: var(--amber-dim);
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.87em;
  }

  blockquote {
    border-left: 3px solid var(--amber);
    background: var(--amber-light);
    padding: 16px 20px;
    margin: 20px 0;
    border-radius: 0 6px 6px 0;
    font-family: 'DM Mono', monospace;
    font-size: 0.82em;
    color: #92400e;
    line-height: 1.6;
  }

  blockquote p { color: #92400e; margin: 0; }

  section.cover {
    background: #1c1917;
    color: var(--white);
    display: flex;
    flex-direction: column;
    justify-content: center;
    position: relative;
    overflow: hidden;
  }

  section.cover::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
      radial-gradient(ellipse at 80% 20%, rgba(217,119,6,0.08) 0%, transparent 55%),
      radial-gradient(ellipse at 10% 85%, rgba(217,119,6,0.05) 0%, transparent 45%);
    pointer-events: none;
  }

  section.cover h1 { color: var(--white); font-size: 44px; letter-spacing: -0.8px; }
  section.cover h2 { color: #a8a29e; border-bottom-color: #44403c; font-size: 20px; font-weight: 400; letter-spacing: 0; }
  section.cover p  { color: #78716c; }
  section.cover strong { color: #fbbf24; }
  section.cover code { background: #292524; color: #fbbf24; border: 1px solid #44403c; }

  section.cover .series-badge {
    display: inline-block;
    background: #292524;
    color: #d97706;
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 500;
    padding: 5px 14px;
    border-radius: 4px;
    margin-bottom: 22px;
    letter-spacing: 0.1em;
    border: 1px solid #44403c;
    width: fit-content;
  }

  section.step { background: var(--off-white); }

  .highlight {
    background: var(--amber-light);
    border: 1px solid #fde68a;
    border-radius: 8px;
    padding: 16px 22px;
    margin: 16px 0;
  }

  .step-badge {
    display: inline-block;
    background: var(--text);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    padding: 4px 12px;
    border-radius: 3px;
    margin-bottom: 12px;
    letter-spacing: 0.08em;
  }

  section.final {
    background: #1c1917;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    position: relative;
    overflow: hidden;
  }

  section.final::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at 50% 50%, rgba(217,119,6,0.10) 0%, transparent 65%);
    pointer-events: none;
  }

  section.final h1 { color: white; font-size: 40px; letter-spacing: -0.5px; }
  section.final p  { color: #a8a29e; font-size: 18px; }
  section.final strong { color: #fbbf24; }
  section.final em { color: #a8a29e; }

  .cheat-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13.5px;
    margin: 12px 0;
  }

  .cheat-table th {
    background: var(--text);
    color: white;
    padding: 8px 14px;
    text-align: left;
    font-weight: 500;
    font-size: 11.5px;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.07em;
  }

  .cheat-table td {
    padding: 9px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
  }

  .cheat-table tr:last-child td { border-bottom: none; }
  .cheat-table tr:nth-child(even) td { background: var(--off-white); }
  .cheat-table .mono {
    font-family: 'DM Mono', monospace;
    color: var(--amber-dim);
    font-size: 12.5px;
  }

  .step-list {
    counter-reset: steps;
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .step-list li {
    counter-increment: steps;
    display: flex;
    align-items: flex-start;
    gap: 14px;
    margin-bottom: 14px;
  }

  .step-list li::before {
    content: counter(steps);
    background: var(--amber);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    min-width: 24px;
    height: 24px;
    border-radius: 5px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 2px;
    flex-shrink: 0;
  }

  /* ── Enough / Not Enough grid ── */
  .enough-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .enough-col { padding: 18px 20px; }
  .enough-col.yes { background: var(--off-white); }
  .enough-col.no  { background: #fffbeb; border-left: 1px solid var(--border); }

  .enough-col .ec-label {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.09em;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .enough-col.yes .ec-label { color: #166534; }
  .enough-col.no  .ec-label { color: #92400e; }

  .enough-col .ec-item {
    font-size: 13px;
    color: var(--text);
    padding: 8px 0;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: flex-start;
    gap: 9px;
    line-height: 1.5;
  }

  .enough-col.no .ec-item { border-bottom-color: #fde68a; }
  .enough-col .ec-item:last-child { border-bottom: none; }
  .enough-col .ec-item .ei-dot { flex-shrink: 0; margin-top: 1px; }

  /* ── Warning signs ── */
  .warning-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 14px 0;
  }

  .warning-card {
    background: var(--white);
    border: 1px solid #fecaca;
    border-radius: 10px;
    overflow: hidden;
  }

  .warning-card .wc-head {
    padding: 10px 14px;
    background: #fef2f2;
    border-bottom: 1px solid #fecaca;
    display: flex;
    align-items: center;
    gap: 8px;
    font-weight: 600;
    font-size: 13px;
    color: #991b1b;
  }

  .warning-card .wc-body {
    padding: 12px 14px;
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.6;
  }

  .warning-card .wc-signal {
    margin-top: 9px;
    background: #fff1f2;
    border-radius: 5px;
    padding: 7px 10px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #be185d;
    line-height: 1.5;
  }

  /* ── Failure modes ── */
  .failure-stack {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin: 14px 0;
  }

  .failure-row {
    display: grid;
    grid-template-columns: 200px 1fr 1fr;
    gap: 0;
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .failure-row .fr-label {
    padding: 12px 14px;
    background: var(--text);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11.5px;
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .failure-row .fr-bad {
    padding: 12px 14px;
    background: #fef2f2;
    border-left: 1px solid #fecaca;
    font-size: 12.5px;
    color: #7f1d1d;
    font-family: 'DM Mono', monospace;
    line-height: 1.55;
  }

  .failure-row .fr-good {
    padding: 12px 14px;
    background: #f0fdf4;
    border-left: 1px solid #bbf7d0;
    font-size: 12.5px;
    color: #14532d;
    font-family: 'DM Mono', monospace;
    line-height: 1.55;
  }

  .fr-bad-label {
    font-size: 9.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #ef4444;
    margin-bottom: 4px;
    display: block;
  }

  .fr-good-label {
    font-size: 9.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #22c55e;
    margin-bottom: 4px;
    display: block;
  }

  /* ── Upgrade trigger ── */
  .trigger-flow {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .trigger-row {
    display: grid;
    grid-template-columns: 36px 1fr auto;
    align-items: center;
    gap: 0;
    border-bottom: 1px solid var(--border);
  }

  .trigger-row:last-child { border-bottom: none; }

  .trigger-row .tr-num {
    background: var(--off-white);
    padding: 14px 0;
    text-align: center;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    border-right: 1px solid var(--border);
    align-self: stretch;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .trigger-row .tr-signal {
    padding: 12px 16px;
    font-size: 13px;
    color: var(--text);
    line-height: 1.55;
  }

  .trigger-row .tr-signal strong { color: var(--amber-dim); }

  .trigger-row .tr-badge {
    padding: 12px 16px;
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    white-space: nowrap;
    border-left: 1px solid var(--border);
  }

  .tr-badge.stay    { color: #166534; background: #f0fdf4; }
  .tr-badge.upgrade { color: #92400e; background: #fffbeb; }

  /* ── CTA slide ── */
  section.cta {
    background: #1c1917;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    position: relative;
    overflow: hidden;
  }

  section.cta::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
      radial-gradient(ellipse at 75% 25%, rgba(217,119,6,0.10) 0%, transparent 50%),
      radial-gradient(ellipse at 20% 80%, rgba(217,119,6,0.06) 0%, transparent 45%);
    pointer-events: none;
  }

  section.cta h2 { color: white; border-bottom-color: #44403c; }
  section.cta p  { color: #a8a29e; }
  section.cta strong { color: #fbbf24; }

  .cta-task-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin: 18px 0;
  }

  .cta-card {
    background: #292524;
    border: 1px solid #44403c;
    border-radius: 10px;
    padding: 16px 16px;
  }

  .cta-card .ctac-icon  { font-size: 24px; margin-bottom: 8px; }
  .cta-card .ctac-title { font-weight: 600; font-size: 13.5px; color: #fde68a; margin-bottom: 5px; }
  .cta-card .ctac-desc  { font-size: 12px; color: #a8a29e; line-height: 1.55; }
  .cta-card .ctac-tag {
    display: inline-block;
    margin-top: 10px;
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: #d97706;
    background: rgba(217,119,6,0.10);
    border: 1px solid rgba(217,119,6,0.25);
    border-radius: 3px;
    padding: 3px 8px;
  }
---

<!-- _class: cover -->

<div class="series-badge">SINGLE AGENT SERIES · PART 4 OF 4</div>

# Knowing Its Limits
## When one agent is the right tool — and when it isn't

&nbsp;

**Not every problem needs more agents.** But some problems need exactly one more.

`scope` · `failure modes` · `upgrade trigger` · `one task` · `level 2`

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## When a Single Agent Is Enough

A single agent is the right tool more often than you think. The question isn't complexity — it's dependency.

<div class="enough-grid">
  <div class="enough-col yes">
    <div class="ec-label">✅ &nbsp;Single agent handles this</div>
    <div class="ec-item"><span class="ei-dot">→</span> The task has one clear start and one clear end</div>
    <div class="ec-item"><span class="ei-dot">→</span> All the information it needs can fit in a single context window</div>
    <div class="ec-item"><span class="ei-dot">→</span> The output is a single artifact: a file, a JSON object, a summary</div>
    <div class="ec-item"><span class="ei-dot">→</span> Steps happen in sequence, not in parallel</div>
    <div class="ec-item"><span class="ei-dot">→</span> No step requires a different "expert" to evaluate the last one</div>
    <div class="ec-item"><span class="ei-dot">→</span> Failure is recoverable by just running it again</div>
  </div>
  <div class="enough-col no">
    <div class="ec-label">⚠️ &nbsp;Starting to strain</div>
    <div class="ec-item"><span class="ei-dot">→</span> The prompt is over 800 words and still feels incomplete</div>
    <div class="ec-item"><span class="ei-dot">→</span> You're using "and also" more than twice in the system prompt</div>
    <div class="ec-item"><span class="ei-dot">→</span> The agent needs to research, then decide, then write, then verify</div>
    <div class="ec-item"><span class="ei-dot">→</span> One part of the output depends on a different model or persona</div>
    <div class="ec-item"><span class="ei-dot">→</span> You're checking the output manually because you don't trust it</div>
    <div class="ec-item"><span class="ei-dot">→</span> The same agent runs in two contexts with very different behaviour</div>
  </div>
</div>

<div class="highlight">

**Default to single.** Add a second agent only when you can name the exact problem it solves — not because the task feels big.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Signs Your Agent Is Doing Too Much

These are observable symptoms, not gut feelings. If you're seeing any of these in testing, your agent has outgrown one role.

<div class="warning-grid">
  <div class="warning-card">
    <div class="wc-head">🎭 &nbsp;Personality drift</div>
    <div class="wc-body">The agent gives expert-level answers in one section and shallow answers in another. It's playing two roles and doing neither well.</div>
    <div class="wc-signal">Signal: "It's great at research but the writing sounds wrong."</div>
  </div>
  <div class="warning-card">
    <div class="wc-head">📏 &nbsp;Output inconsistency</div>
    <div class="wc-body">The same prompt returns different formats on different runs — sometimes JSON, sometimes prose. The model is confused about which mode it's in.</div>
    <div class="wc-signal">Signal: json.loads() fails on 30% of runs.</div>
  </div>
  <div class="warning-card">
    <div class="wc-head">🔁 &nbsp;Prompt bloat</div>
    <div class="wc-body">Your system prompt keeps growing. Every new failure adds another rule. You're patching scope creep with words instead of architecture.</div>
    <div class="wc-signal">Signal: "Let me add one more instruction to fix this…"</div>
  </div>
  <div class="warning-card">
    <div class="wc-head">🐢 &nbsp;Slow, expensive runs</div>
    <div class="wc-body">Every call maxes out the token budget because the agent is doing research, synthesis, and formatting in one pass. You're paying for work that could be parallelised.</div>
    <div class="wc-signal">Signal: 4 000+ tokens per call for a simple output.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Common Failure Modes — And How to Fix Them

These three mistakes account for the majority of single-agent failures in the wild.

<div class="failure-stack">
  <div class="failure-row">
    <div class="fr-label">🌫️ &nbsp;Vague prompt</div>
    <div class="fr-bad"><span class="fr-bad-label">❌ What you wrote</span>"Analyse the competitor and give me useful insights."</div>
    <div class="fr-good"><span class="fr-good-label">✓ What to write instead</span>"Extract pricing tiers, target segment, and one key differentiator. Return as JSON."</div>
  </div>
  <div class="failure-row">
    <div class="fr-label">📭 &nbsp;No output format</div>
    <div class="fr-bad"><span class="fr-bad-label">❌ What you wrote</span>"Return whatever you think is most helpful."</div>
    <div class="fr-good"><span class="fr-good-label">✓ What to write instead</span>"Return ONLY a JSON object with keys: name, price, verdict. No prose."</div>
  </div>
  <div class="failure-row">
    <div class="fr-label">🎪 &nbsp;Too many jobs</div>
    <div class="fr-bad"><span class="fr-bad-label">❌ What you wrote</span>"Research, summarise, score, and draft a response email."</div>
    <div class="fr-good"><span class="fr-good-label">✓ What to write instead</span>Split into: research agent → scoring agent → drafting agent. One job each.</div>
  </div>
</div>

<div class="highlight">

**The fix is always the same:** make the contract more specific. Narrow the role. Lock the output format. Reduce the jobs to one.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## The Upgrade Trigger — When to Move to Level 2

Level 2 means multiple agents coordinating: an orchestrator, specialised workers, and handoffs between them. Move here only when you hit a real trigger — not when the task feels complicated.

<div class="trigger-flow">
  <div class="trigger-row">
    <div class="tr-num">1</div>
    <div class="tr-signal">The task needs <strong>two distinct expert personas</strong> — a researcher and a copywriter, a coder and a reviewer — whose work doesn't overlap.</div>
    <div class="tr-badge upgrade">→ Level 2</div>
  </div>
  <div class="trigger-row">
    <div class="tr-num">2</div>
    <div class="tr-signal">Steps can run <strong>in parallel</strong> — you're waiting on sequential calls when the work is actually independent.</div>
    <div class="tr-badge upgrade">→ Level 2</div>
  </div>
  <div class="trigger-row">
    <div class="tr-num">3</div>
    <div class="tr-signal">One agent needs to <strong>critique or verify</strong> the output of another before it moves forward — a self-checking loop.</div>
    <div class="tr-badge upgrade">→ Level 2</div>
  </div>
  <div class="trigger-row">
    <div class="tr-num">4</div>
    <div class="tr-signal">The task is <strong>long enough to overflow</strong> a single context window — you lose early reasoning before reaching the final output.</div>
    <div class="tr-badge upgrade">→ Level 2</div>
  </div>
  <div class="trigger-row">
    <div class="tr-num">5</div>
    <div class="tr-signal">The system prompt is <strong>still clear, one role is assigned, output format is defined</strong> — but failures keep appearing.</div>
    <div class="tr-badge stay">→ Stay single</div>
  </div>
  <div class="trigger-row">
    <div class="tr-num">6</div>
    <div class="tr-signal">The task feels hard and you're not sure why — <strong>no specific trigger applies</strong> yet.</div>
    <div class="tr-badge stay">→ Stay single</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## Quick Reference — Diagnose Before You Scale

Use this table before reaching for a second agent.

<table class="cheat-table">
  <thead>
    <tr><th>Symptom</th><th>Root cause</th><th>Fix</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>Output format changes between runs</td>
      <td>No format constraint in system prompt</td>
      <td>Add explicit JSON schema. Instruct "return ONLY".</td>
    </tr>
    <tr>
      <td>Agent ignores half the instructions</td>
      <td>Too many jobs in one prompt</td>
      <td>Cut to one role and one deliverable.</td>
    </tr>
    <tr>
      <td>Good research, bad writing — or vice versa</td>
      <td>Two personas forced into one agent</td>
      <td>Split into two agents with a handoff.</td>
    </tr>
    <tr>
      <td>Costs keep rising, output stays the same</td>
      <td>Context bloat — too much fed in per call</td>
      <td>Chunk input. Summarise earlier steps before passing.</td>
    </tr>
    <tr>
      <td>Works in testing, drifts in production</td>
      <td>Vague role definition, over-reliance on examples</td>
      <td>Rewrite system prompt with explicit constraints + error returns.</td>
    </tr>
    <tr>
      <td>You keep tweaking the prompt after every run</td>
      <td>Scope creep — the job is growing</td>
      <td>Freeze the scope. Build a second agent for the new job.</td>
    </tr>
  </tbody>
</table>

---

<!-- _class: cta -->

## Your Assignment — One Agent, One Task, Today

You've finished the series. The only move left is to build something real.

<div class="cta-task-grid">
  <div class="cta-card">
    <div class="ctac-icon">📋</div>
    <div class="ctac-title">If you work with text</div>
    <div class="ctac-desc">Pick one document you summarise manually every week — a report, a Slack thread, a news digest. Build an agent that does it and saves the output to a file.</div>
    <div class="ctac-tag">input: raw text → output: summary.md</div>
  </div>
  <div class="cta-card">
    <div class="ctac-icon">🔍</div>
    <div class="ctac-title">If you work with data</div>
    <div class="ctac-desc">Pick one CSV or API you check manually. Build an agent that reads it, flags anything above a threshold, and returns a structured JSON report.</div>
    <div class="ctac-tag">input: data.csv → output: flags.json</div>
  </div>
  <div class="cta-card">
    <div class="ctac-icon">✉️</div>
    <div class="ctac-title">If you work with communication</div>
    <div class="ctac-desc">Pick one type of email or message you draft from scratch repeatedly. Build an agent that takes a context file and returns a ready-to-send draft.</div>
    <div class="ctac-tag">input: brief.txt → output: draft.txt</div>
  </div>
</div>

<p style="font-size:15px; color:#78716c; margin-top: 4px;">The constraint is the point: <strong>one agent, one role, one output format.</strong> No tools yet. No loop. Just the call.</p>

---

<!-- _class: final -->

# That's the Series.

&nbsp;

*You know what an agent is, how it works, how to build one, and when to stop.*

&nbsp;

Next: **Level 2 — Pipeline Agents Systems.**

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*