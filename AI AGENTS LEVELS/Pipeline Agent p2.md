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

  /* ── Cover ── */
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

  /* ── Agent card ── */
  .agent-card {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .agent-card .ac-head {
    padding: 12px 18px;
    display: flex;
    align-items: center;
    gap: 12px;
    border-bottom: 1px solid var(--border);
  }

  .agent-card .ac-head .ac-icon { font-size: 22px; flex-shrink: 0; }

  .agent-card .ac-head .ac-title {
    font-weight: 700;
    font-size: 16px;
    color: var(--text);
  }

  .agent-card .ac-head .ac-role {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.09em;
    margin-left: auto;
    padding: 3px 10px;
    border-radius: 3px;
  }

  .agent-card.researcher .ac-head { background: #f0f9ff; }
  .agent-card.researcher .ac-role { background: #bae6fd; color: #0c4a6e; }
  .agent-card.writer     .ac-head { background: var(--amber-light); }
  .agent-card.writer     .ac-role { background: #fde68a; color: #92400e; }
  .agent-card.critic     .ac-head { background: #fdf4ff; }
  .agent-card.critic     .ac-role { background: #e9d5ff; color: #6b21a8; }
  .agent-card.refiner    .ac-head { background: #f0fdf4; }
  .agent-card.refiner    .ac-role { background: #bbf7d0; color: #166534; }

  .agent-card .ac-body {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    background: var(--white);
  }

  .agent-card .ac-col {
    padding: 14px 16px;
    border-right: 1px solid var(--border);
  }

  .agent-card .ac-col:last-child { border-right: none; }

  .agent-card .ac-col .acc-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.09em;
    color: var(--muted);
    margin-bottom: 8px;
  }

  .agent-card .ac-col .acc-item {
    font-size: 12.5px;
    color: var(--text);
    padding: 5px 0;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: flex-start;
    gap: 7px;
    line-height: 1.5;
  }

  .agent-card .ac-col .acc-item:last-child { border-bottom: none; }

  .agent-card .ac-col .acc-item code {
    font-size: 11px;
    padding: 1px 6px;
  }

  /* ── IO strip ── */
  .io-strip {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .io-side {
    padding: 16px 20px;
  }

  .io-side.input  { background: #f0f9ff; }
  .io-side.output { background: #f0fdf4; }

  .io-side .ios-label {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.09em;
    margin-bottom: 10px;
  }

  .io-side.input  .ios-label { color: #0369a1; }
  .io-side.output .ios-label { color: #166534; }

  .io-side .ios-item {
    font-size: 13px;
    color: var(--text);
    padding: 6px 0;
    border-bottom: 1px solid rgba(0,0,0,0.06);
    display: flex;
    align-items: flex-start;
    gap: 8px;
    line-height: 1.5;
  }

  .io-side .ios-item:last-child { border-bottom: none; }

  .io-divider {
    background: var(--white);
    border-left: 1px solid var(--border);
    border-right: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 16px;
    font-size: 20px;
    color: var(--amber);
    flex-shrink: 0;
  }

  /* ── Prompt anatomy ── */
  .prompt-anatomy {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
  }

  .pa-block {
    display: grid;
    grid-template-columns: 160px 1fr;
    border-bottom: 1px solid var(--border);
  }

  .pa-block:last-child { border-bottom: none; }

  .pa-block .pb-label {
    padding: 12px 14px;
    font-weight: 600;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    display: flex;
    align-items: center;
    gap: 8px;
    border-right: 1px solid var(--border);
  }

  .pa-block .pb-content {
    padding: 12px 16px;
    font-size: 12px;
    line-height: 1.65;
    color: var(--text);
    font-family: 'DM Mono', monospace;
  }

  .pa-block.role    .pb-label { background: #f0f9ff;           color: #0369a1; }
  .pa-block.context .pb-label { background: var(--amber-light); color: #92400e; }
  .pa-block.rules   .pb-label { background: #fdf4ff;            color: #6b21a8; }
  .pa-block.format  .pb-label { background: #f0fdf4;            color: #166534; }
  .pa-block.neg     .pb-label { background: #fef2f2;            color: #991b1b; }

  /* ── Matters grid ── */
  .matters-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .matters-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 14px 16px;
    display: flex;
    align-items: flex-start;
    gap: 13px;
  }

  .matters-card .mcc-icon { font-size: 24px; flex-shrink: 0; }

  .matters-card .mcc-title {
    font-weight: 600;
    font-size: 14px;
    color: var(--text);
    margin-bottom: 4px;
  }

  .matters-card .mcc-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.55;
  }

  /* ── Cheat table ── */
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
  .cheat-table tr:last-child td { border-bottom: 1px solid var(--border); }
  .cheat-table tr:nth-child(even) td { background: var(--off-white); }

  .cheat-table .mono {
    font-family: 'DM Mono', monospace;
    color: var(--amber-dim);
    font-size: 12.5px;
  }

  /* ── Feedback loop diagram ── */
  .feedback-loop {
    display: grid;
    grid-template-columns: 1fr auto 1fr auto 1fr;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 16px 0;
    align-items: stretch;
  }

  .fl-node {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 18px 12px;
    text-align: center;
    gap: 5px;
  }

  .fl-node .fln-icon { font-size: 26px; }
  .fl-node .fln-type {
    font-family: 'DM Mono', monospace;
    font-size: 9.5px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
  }
  .fl-node .fln-name { font-weight: 700; font-size: 14px; color: var(--text); }
  .fl-node .fln-sub  { font-size: 11px; color: var(--muted); line-height: 1.4; }

  .fl-node.n-writer  { background: var(--amber-light); }
  .fl-node.n-writer  .fln-type { color: #92400e; }
  .fl-node.n-critic  { background: #fdf4ff; }
  .fl-node.n-critic  .fln-type { color: #6b21a8; }
  .fl-node.n-refiner { background: #f0fdf4; }
  .fl-node.n-refiner .fln-type { color: #166534; }

  .fl-arrow {
    display: flex;
    align-items: center;
    padding: 0 8px;
    font-size: 16px;
    color: var(--amber);
    background: var(--white);
    border-left: 1px solid var(--border);
    border-right: 1px solid var(--border);
    flex-shrink: 0;
    flex-direction: column;
    justify-content: center;
    gap: 4px;
  }

  .fl-arrow .fla-label {
    font-family: 'DM Mono', monospace;
    font-size: 9px;
    color: var(--muted);
    text-align: center;
    line-height: 1.3;
  }

  /* ── E2E pipeline table (inherited from Part 1) ── */
  .e2e-pipeline {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .e2e-row {
    display: grid;
    grid-template-columns: 32px 160px 1fr 170px;
    align-items: stretch;
    border-bottom: 1px solid var(--border);
  }

  .e2e-row:last-child { border-bottom: none; }

  .e2e-row .er-num {
    background: var(--text);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }

  .e2e-row .er-agent {
    padding: 11px 13px;
    font-weight: 600;
    font-size: 12.5px;
    color: var(--text);
    border-right: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 7px;
    background: var(--off-white);
    line-height: 1.4;
  }

  .e2e-row .er-task {
    padding: 11px 14px;
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.6;
    display: flex;
    align-items: center;
  }

  .e2e-row .er-artifact {
    padding: 11px 13px;
    border-left: 1px solid var(--border);
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    display: flex;
    align-items: center;
    gap: 6px;
    font-weight: 500;
  }

  .e2e-row:nth-child(1) .er-artifact { background: #f0f9ff;            color: #0369a1; }
  .e2e-row:nth-child(2) .er-artifact { background: var(--amber-light);  color: #92400e; }
  .e2e-row:nth-child(3) .er-artifact { background: #f0fdf4;             color: #166534; }
  .e2e-row:nth-child(4) .er-artifact { background: #fdf4ff;             color: #6b21a8; }
  .e2e-row:nth-child(5) .er-artifact { background: #fff7ed;             color: #9a3412; }

  /* ── focused-row highlight for deep-dives ── */
  .e2e-row.focus .er-agent { background: #fefce8; border-left: 3px solid var(--amber); }
  .e2e-row.focus .er-task  { background: #fefce8; color: var(--text); }
  .e2e-row.dim   .er-agent { opacity: 0.45; }
  .e2e-row.dim   .er-task  { opacity: 0.45; }
  .e2e-row.dim   .er-artifact { opacity: 0.45; }
---

<!-- _class: cover -->

<div class="series-badge">PIPELINE AGENTS · LEVEL 2 — PART 2 OF 4</div>

# Designing the Agents in Your Pipeline
## Role, input, output — for every specialist in the chain

&nbsp;

**The pipeline is only as strong as its weakest agent.** Here's how to design each one so the chain never breaks.

`researcher` · `outline` · `writer` · `editor` · `qa` · `system-prompt`

---

## The Pipeline We're Designing — All Five Agents

In Part 1 we named the chain. In Part 2 we go inside each agent. Same pipeline, same artifacts — this time we design the role, input, and output for every stage.

<div class="e2e-pipeline">
  <div class="e2e-row">
    <div class="er-num">1</div>
    <div class="er-agent">🔍 Research agent</div>
    <div class="er-task">Given a topic and target audience, finds key facts, statistics, and competing articles. Evaluates source credibility. Never writes prose.</div>
    <div class="er-artifact">→ research.json</div>
  </div>
  <div class="e2e-row">
    <div class="er-num">2</div>
    <div class="er-agent">🗂️ Outline agent</div>
    <div class="er-task">Takes <code>research.json</code>. Structures a logical narrative arc — intro, sections, conclusion. No sentences written yet.</div>
    <div class="er-artifact">→ outline.json</div>
  </div>
  <div class="e2e-row">
    <div class="er-num">3</div>
    <div class="er-agent">✍️ Writer agent</div>
    <div class="er-task">Takes <code>outline.json</code> + <code>research.json</code>. Writes the full draft in the specified voice and reading level. Assumes facts are correct.</div>
    <div class="er-artifact">→ draft.md</div>
  </div>
  <div class="e2e-row">
    <div class="er-num">4</div>
    <div class="er-agent">✂️ Editor agent</div>
    <div class="er-task">Takes <code>draft.md</code>. Tightens sentences, removes filler, checks flow. Returns the same format — no new research, no new facts.</div>
    <div class="er-artifact">→ edited.md</div>
  </div>
  <div class="e2e-row">
    <div class="er-num">5</div>
    <div class="er-agent">🔎 QA agent</div>
    <div class="er-task">Cross-checks <code>edited.md</code> against <code>research.json</code> for factual accuracy. Returns <code>pass</code> or a list of flagged claims with line numbers.</div>
    <div class="er-artifact">→ qa_report.json</div>
  </div>
</div>

<div class="highlight">

**How this part works:** Each of the next five slides zooms into one row above — its exact role, what it receives, what it must produce, and the system prompt pattern that makes it behave. The artifact names stay identical throughout.

</div>

---

<!-- _class: step -->

<div class="step-badge">AGENT 01</div>

## The Researcher Agent

Its only job is to surface what is true and relevant. It never tries to be useful — it tries to be accurate.

<div class="agent-card researcher">
  <div class="ac-head">
    <div class="ac-icon">🔍</div>
    <div class="ac-title">Researcher Agent</div>
    <div class="ac-role">STAGE 1 OF 4</div>
  </div>
  <div class="ac-body">
    <div class="ac-col">
      <div class="acc-label">📥 &nbsp;Input</div>
      <div class="acc-item">→ Topic string or user query</div>
      <div class="acc-item">→ Optional: target audience, depth level</div>
      <div class="acc-item">→ Optional: source list or domain constraints</div>
    </div>
    <div class="ac-col">
      <div class="acc-label">⚙️ &nbsp;What it does</div>
      <div class="acc-item">→ Identifies the core claim or question</div>
      <div class="acc-item">→ Extracts facts, stats, and named sources</div>
      <div class="acc-item">→ Flags low-confidence or contested claims</div>
      <div class="acc-item">→ Structures everything into <code>research.json</code></div>
    </div>
    <div class="ac-col">
      <div class="acc-label">📤 &nbsp;Output</div>
      <div class="acc-item">→ <code>research.json</code> with keyed sections</div>
      <div class="acc-item">→ Each fact paired with a source reference</div>
      <div class="acc-item">→ Confidence scores or flags where relevant</div>
      <div class="acc-item">→ <strong>No prose. No opinions. No formatting.</strong></div>
    </div>
  </div>
</div>

<div class="matters-grid">
  <div class="matters-card">
    <div class="mcc-icon">🚫</div>
    <div>
      <div class="mcc-title">What it must never do</div>
      <div class="mcc-desc">Write sentences intended for a reader. Summarise in a readable way. Make editorial judgements about what's "important." That's the Writer's job.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🔑</div>
    <div>
      <div class="mcc-title">The one design principle</div>
      <div class="mcc-desc">If the Writer ever has to go back and verify a fact, the Researcher failed. Every claim in <code>research.json</code> should be trusted blindly by the next stage.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">AGENT 02</div>

## The Writer Agent

It doesn't think about what's true — it thinks about what's clear. The research is already done. Its job is translation: structure into prose.

<div class="agent-card writer">
  <div class="ac-head">
    <div class="ac-icon">✍️</div>
    <div class="ac-title">Writer Agent</div>
    <div class="ac-role">STAGE 2 OF 4</div>
  </div>
  <div class="ac-body">
    <div class="ac-col">
      <div class="acc-label">📥 &nbsp;Input</div>
      <div class="acc-item">→ <code>research.json</code> from Researcher</div>
      <div class="acc-item">→ Voice/tone spec (e.g. casual, authoritative)</div>
      <div class="acc-item">→ Target format (blog post, report, thread)</div>
      <div class="acc-item">→ Word count or length constraint</div>
    </div>
    <div class="ac-col">
      <div class="acc-label">⚙️ &nbsp;What it does</div>
      <div class="acc-item">→ Maps research keys to narrative sections</div>
      <div class="acc-item">→ Writes in the specified voice and register</div>
      <div class="acc-item">→ Structures for the target reader, not the source</div>
      <div class="acc-item">→ Produces a complete first draft</div>
    </div>
    <div class="ac-col">
      <div class="acc-label">📤 &nbsp;Output</div>
      <div class="acc-item">→ <code>draft.md</code> — full, readable prose</div>
      <div class="acc-item">→ No JSON, no headers referencing research keys</div>
      <div class="acc-item">→ Ready to hand to the Critic as-is</div>
      <div class="acc-item">→ <strong>No new facts invented or sourced.</strong></div>
    </div>
  </div>
</div>

<div class="highlight">

**Critical constraint:** The Writer agent's system prompt must include an explicit instruction: *"You may only use facts present in the research input. Do not retrieve, infer, or invent any additional claims."* This is the most common failure point in content pipelines — a Writer that adds plausible-sounding but unverified facts.

</div>

---

<!-- _class: step -->

<div class="step-badge">AGENT 03</div>

## The Critic / Editor Agent

It reads the draft like a tough editor — not to improve it, but to measure it. Its output is a report, not a revision.

<div class="agent-card critic">
  <div class="ac-head">
    <div class="ac-icon">🔬</div>
    <div class="ac-title">Critic / Editor Agent</div>
    <div class="ac-role">STAGE 3 OF 4</div>
  </div>
  <div class="ac-body">
    <div class="ac-col">
      <div class="acc-label">📥 &nbsp;Input</div>
      <div class="acc-item">→ <code>draft.md</code> from Writer</div>
      <div class="acc-item">→ <code>research.json</code> for fact-checking</div>
      <div class="acc-item">→ A rubric: the explicit rules to score against</div>
    </div>
    <div class="ac-col">
      <div class="acc-label">⚙️ &nbsp;What it does</div>
      <div class="acc-item">→ Scores each rubric dimension 1–5</div>
      <div class="acc-item">→ Flags specific lines or paragraphs with issues</div>
      <div class="acc-item">→ Cross-checks claims against <code>research.json</code></div>
      <div class="acc-item">→ Returns structured JSON — not prose feedback</div>
    </div>
    <div class="ac-col">
      <div class="acc-label">📤 &nbsp;Output</div>
      <div class="acc-item">→ <code>critique.json</code> with scores + flags</div>
      <div class="acc-item">→ Each flag: line ref, issue type, severity</div>
      <div class="acc-item">→ Overall <code>pass</code> / <code>revise</code> verdict</div>
      <div class="acc-item">→ <strong>No rewrites. No suggestions phrased as prose.</strong></div>
    </div>
  </div>
</div>

<div class="matters-grid">
  <div class="matters-card">
    <div class="mcc-icon">📏</div>
    <div>
      <div class="mcc-title">The rubric is the agent</div>
      <div class="mcc-desc">A Critic without a rubric is just an opinion. Write your rubric first — clarity, factual accuracy, voice match, structure, reading level. The agent scores; the rubric decides what matters.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🚫</div>
    <div>
      <div class="mcc-title">Why it must not rewrite</div>
      <div class="mcc-desc">If the Critic rewrites, you lose the separation of concerns. Now debugging is impossible — did the Refiner apply the fix, or did the Critic already change it? Keep diagnosis and repair in separate agents.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">AGENT 04</div>

## The Refiner Agent

It reads two things — the draft and the critique — and applies every flag. No judgment, no creativity. Pure execution.

<div class="agent-card refiner">
  <div class="ac-head">
    <div class="ac-icon">🔧</div>
    <div class="ac-title">Refiner Agent</div>
    <div class="ac-role">STAGE 4 OF 4</div>
  </div>
  <div class="ac-body">
    <div class="ac-col">
      <div class="acc-label">📥 &nbsp;Input</div>
      <div class="acc-item">→ <code>draft.md</code> from Writer</div>
      <div class="acc-item">→ <code>critique.json</code> from Critic</div>
      <div class="acc-item">→ Optionally: <code>research.json</code> for replacements</div>
    </div>
    <div class="ac-col">
      <div class="acc-label">⚙️ &nbsp;What it does</div>
      <div class="acc-item">→ Iterates through each flag in <code>critique.json</code></div>
      <div class="acc-item">→ Applies the fix at the referenced location</div>
      <div class="acc-item">→ Preserves everything not flagged, unchanged</div>
      <div class="acc-item">→ Produces a clean, final document</div>
    </div>
    <div class="ac-col">
      <div class="acc-label">📤 &nbsp;Output</div>
      <div class="acc-item">→ <code>final.md</code> — ready to ship</div>
      <div class="acc-item">→ No new content beyond what was flagged</div>
      <div class="acc-item">→ Optionally: a diff log of changes applied</div>
      <div class="acc-item">→ <strong>Never re-evaluates. Only fixes what's listed.</strong></div>
    </div>
  </div>
</div>

<div class="highlight">

**The loop pattern:** If the Refiner's output should go back through the Critic for a second pass, that's a **feedback loop** — a more advanced pattern covered in Part 3. For most pipelines, one pass is sufficient. Only add a loop when you have a measurable quality threshold to hit.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## The Writer–Critic–Refiner Loop

Before we move to prompts, here's how the middle three agents relate to each other. The Researcher feeds in; the loop refines; the output exits.

<div class="feedback-loop">
  <div class="fl-node n-writer">
    <div class="fln-icon">✍️</div>
    <div class="fln-type">Agent 2</div>
    <div class="fln-name">Writer</div>
    <div class="fln-sub">Produces first draft<br>from research facts</div>
  </div>
  <div class="fl-arrow">
    →
    <div class="fla-label">draft.md</div>
  </div>
  <div class="fl-node n-critic">
    <div class="fln-icon">🔬</div>
    <div class="fln-type">Agent 3</div>
    <div class="fln-name">Critic</div>
    <div class="fln-sub">Scores the draft<br>against the rubric</div>
  </div>
  <div class="fl-arrow">
    →
    <div class="fla-label">critique.json</div>
  </div>
  <div class="fl-node n-refiner">
    <div class="fln-icon">🔧</div>
    <div class="fln-type">Agent 4</div>
    <div class="fln-name">Refiner</div>
    <div class="fln-sub">Applies every flag.<br>Returns final.md</div>
  </div>
</div>

<div class="matters-grid" style="margin-top: 14px;">
  <div class="matters-card">
    <div class="mcc-icon">📄</div>
    <div>
      <div class="mcc-title">Why the draft passes to both</div>
      <div class="mcc-desc">The Refiner needs the original draft to know what to change. The Critic needs it to know what to score. Both receive <code>draft.md</code> — but only the Refiner writes a new version.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🔁</div>
    <div>
      <div class="mcc-title">When to loop vs. when to stop</div>
      <div class="mcc-desc">Loop only if the Critic's verdict is <code>revise</code> and you have a quality threshold to clear. If every run loops unconditionally, you're adding latency without a quality gate. Define <code>pass</code> criteria first.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 06</div>

## How to Write a System Prompt for a Specialist Agent

A generalist prompt asks the model to be useful. A specialist prompt tells it exactly who it is, what it receives, and what it must never do.

<div class="prompt-anatomy">
  <div class="pa-block role">
    <div class="pb-label">🎭 &nbsp;ROLE</div>
    <div class="pb-content">State the agent's identity in one sentence. Not what it will do — what it is.
"You are a research extraction agent. Your sole function is to extract factual claims from provided source material."</div>
  </div>
  <div class="pa-block context">
    <div class="pb-label">📦 &nbsp;CONTEXT</div>
    <div class="pb-content">Describe what the agent will receive as input and in what format. Be exact.
"You will receive: (1) a topic string, (2) optionally, a list of source URLs or pasted text. No other input will be provided."</div>
  </div>
  <div class="pa-block rules">
    <div class="pb-label">📐 &nbsp;RULES</div>
    <div class="pb-content">State the constraints as numbered rules. The model treats numbered lists as obligations.
"1. Only extract claims present in the input. 2. Do not infer, interpret, or add context. 3. Assign a confidence flag (HIGH / LOW) to each claim."</div>
  </div>
  <div class="pa-block format">
    <div class="pb-label">📄 &nbsp;FORMAT</div>
    <div class="pb-content">Specify the exact output format and schema. Include a short example if the structure is non-obvious.
"Return a valid JSON object with keys: topic, claims[], sources[]. Each claim: { text, source_ref, confidence }."</div>
  </div>
  <div class="pa-block neg">
    <div class="pb-label">🚫 &nbsp;NEVER</div>
    <div class="pb-content">Explicitly list what the agent must not do — even if it seems obvious. Negative constraints prevent the model from "helpfully" overstepping.
"Never write prose summaries. Never suggest what the Writer should emphasise. Never return partial JSON."</div>
  </div>
</div>

---

## Prompt Templates — One Per Agent

The five-block structure, applied to each of the four specialists in the pipeline.

<table class="cheat-table">
  <thead>
    <tr><th>Agent</th><th>ROLE line</th><th>FORMAT line</th><th>Key NEVER rule</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>🔍 <strong>Researcher</strong></td>
      <td>You extract facts and sources from provided material.</td>
      <td>Return <span class="mono">research.json</span> — keyed claims with source refs.</td>
      <td>Never write prose. Never editorialize.</td>
    </tr>
    <tr>
      <td>✍️ <strong>Writer</strong></td>
      <td>You turn structured research into readable prose.</td>
      <td>Return <span class="mono">draft.md</span> — full flowing text, no JSON keys visible.</td>
      <td>Never invent facts not in the research input.</td>
    </tr>
    <tr>
      <td>🔬 <strong>Critic</strong></td>
      <td>You evaluate a draft against a rubric and flag issues.</td>
      <td>Return <span class="mono">critique.json</span> — scores, flags, and a pass/revise verdict.</td>
      <td>Never rewrite. Never suggest phrasing.</td>
    </tr>
    <tr>
      <td>🔧 <strong>Refiner</strong></td>
      <td>You apply a critique report to a draft and return the fixed version.</td>
      <td>Return <span class="mono">final.md</span> — unchanged except where flags apply.</td>
      <td>Never add new content. Never re-evaluate quality.</td>
    </tr>
  </tbody>
</table>

<div class="highlight">

**The NEVER block is the most important block.** Models default to being helpful — which means they'll overstep their role if you don't explicitly forbid it. A Critic without a NEVER block will start rewriting. A Writer without one will start researching. Negative constraints are not optional.

</div>

---

<!-- _class: final -->

# Design the agent before you write the prompt.

&nbsp;

*Role → Input → Output → NEVER. In that order, every time.*

&nbsp;

Next: **Part 3 — Building the Orchestrator.**

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*