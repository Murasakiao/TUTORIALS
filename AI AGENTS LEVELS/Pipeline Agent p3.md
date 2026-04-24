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
    font-size: 13px;
  }

  .cheat-table tr:last-child td { border-bottom: none; }
  .cheat-table tr:nth-child(even) td { background: var(--off-white); }

  .cheat-table .mono {
    font-family: 'DM Mono', monospace;
    color: var(--amber-dim);
    font-size: 12px;
  }

  /* ── E2E pipeline table ── */
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

  .e2e-row.focus .er-agent { background: #fefce8; border-left: 3px solid var(--amber); }
  .e2e-row.focus .er-task  { background: #fefce8; color: var(--text); }
  .e2e-row.dim   .er-agent,
  .e2e-row.dim   .er-task,
  .e2e-row.dim   .er-artifact { opacity: 0.4; }

  /* ── Code block ── */
  .code-block {
    background: #1c1917;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid #44403c;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
  }

  .code-block .cb-header {
    background: #292524;
    border-bottom: 1px solid #44403c;
    padding: 8px 16px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .code-block .cb-header .cb-dots {
    display: flex;
    gap: 5px;
  }

  .code-block .cb-header .cb-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
  }

  .code-block .cb-header .cb-dot.red    { background: #ef4444; }
  .code-block .cb-header .cb-dot.yellow { background: #eab308; }
  .code-block .cb-header .cb-dot.green  { background: #22c55e; }

  .code-block .cb-header .cb-filename {
    font-size: 11px;
    color: #a8a29e;
    font-weight: 500;
    letter-spacing: 0.04em;
    margin-left: 4px;
  }

  .code-block .cb-body {
    padding: 14px 20px;
    font-size: 11.5px;
    line-height: 1.7;
    color: #d6d3d1;
    white-space: pre;
  }

  .code-block .cb-body .kw  { color: #c084fc; }
  .code-block .cb-body .fn  { color: #fbbf24; }
  .code-block .cb-body .st  { color: #86efac; }
  .code-block .cb-body .cm  { color: #57534e; }
  .code-block .cb-body .nu  { color: #fb923c; }
  .code-block .cb-body .bi  { color: #67e8f9; }
  .code-block .cb-body .va  { color: #d6d3d1; }
  .code-block .cb-body .hl  { background: rgba(217,119,6,0.15); display: inline-block; width: 100%; border-radius: 3px; }

  /* ── JSON schema block ── */
  .schema-block {
    background: #182932;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid #0369a1;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
  }

  .schema-block .sb-header {
    background: #305264;
    padding: 8px 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .schema-block .sb-header .sb-title {
    font-size: 11px;
    color: #bae6fd;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.09em;
  }

  .schema-block .sb-header .sb-badge {
    font-size: 10px;
    background: #0c4a6e;
    color: #7dd3fc;
    padding: 2px 8px;
    border-radius: 3px;
    font-weight: 500;
  }

  .schema-block .sb-body {
    padding: 14px 18px;
    font-size: 11.5px;
    line-height: 1.75;
    color: #bae6fd;
    white-space: pre;
  }

  .schema-block .sb-body .sk { color: #fde68a; }
  .schema-block .sb-body .sv { color: #86efac; }
  .schema-block .sb-body .sn { color: #fb923c; }
  .schema-block .sb-body .sc { color: #57534e; }

  /* ── File tree ── */
  .file-tree {
    background: #1c1917;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid #44403c;
    margin: 14px 0;
  }

  .file-tree .ft-header {
    background: #292524;
    border-bottom: 1px solid #44403c;
    padding: 8px 16px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #a8a29e;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .file-tree .ft-body {
    padding: 14px 20px;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    line-height: 1.9;
    color: #d6d3d1;
    white-space: pre;
  }

  .file-tree .ft-body .fd  { color: #fbbf24; }
  .file-tree .ft-body .fp  { color: #86efac; }
  .file-tree .ft-body .fj  { color: #67e8f9; }
  .file-tree .ft-body .fm  { color: #c4b5fd; }
  .file-tree .ft-body .fc  { color: #57534e; }

  /* ── Sequential vs Parallel compare ── */
  .seq-par-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 14px 0;
  }

  .sp-side {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .sp-side .sp-head {
    padding: 10px 16px;
    font-weight: 600;
    font-size: 13px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border);
  }

  .sp-side.sequential .sp-head { background: #f0f9ff; color: #0c4a6e; border-color: #bae6fd; }
  .sp-side.parallel   .sp-head { background: #f0fdf4; color: #166534; border-color: #bbf7d0; }

  .sp-side .sp-body {
    padding: 12px 16px;
    background: var(--white);
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .sp-step {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 7px 10px;
    border-radius: 6px;
    font-size: 12.5px;
    line-height: 1.45;
  }

  .sp-step .sps-num {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    font-weight: 700;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }

  .sp-step .sps-label { color: var(--text); font-weight: 500; }
  .sp-step .sps-sub   { color: var(--muted); font-size: 11.5px; }

  .sequential .sp-step { background: #f0f9ff; }
  .sequential .sp-step .sps-num { background: #0369a1; color: white; }

  .parallel   .sp-step { background: #f0fdf4; }
  .parallel   .sp-step .sps-num { background: #166534; color: white; }

  .sp-arrow {
    text-align: center;
    font-size: 11px;
    color: var(--muted);
    padding: 1px 10px;
    font-family: 'DM Mono', monospace;
  }

  .sp-par-row {
    display: flex;
    gap: 6px;
    align-items: stretch;
  }

  .sp-par-row .sp-step { flex: 1; }

  /* ── Walkthrough strip ── */
  .walkthrough {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .wt-row {
    display: grid;
    grid-template-columns: 36px 1fr;
    border-bottom: 1px solid var(--border);
    align-items: stretch;
  }

  .wt-row:last-child { border-bottom: none; }

  .wt-row .wr-num {
    background: var(--text);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .wt-row .wr-content {
    padding: 10px 16px;
  }

  .wt-row .wr-content .wrc-title {
    font-weight: 600;
    font-size: 13px;
    color: var(--text);
    margin-bottom: 3px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .wt-row .wr-content .wrc-desc {
    font-size: 12px;
    color: var(--muted);
    line-height: 1.55;
  }

  .wt-row .wr-content .wrc-code {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--amber-dim);
    background: var(--amber-light);
    padding: 2px 8px;
    border-radius: 3px;
    margin-top: 5px;
    display: inline-block;
  }

  .wt-row:nth-child(odd)  .wr-content { background: var(--white); }
  .wt-row:nth-child(even) .wr-content { background: var(--off-white); }

  /* ── Inline two-col ── */
  .two-col-notes {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 12px;
  }

  .tcn-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px 14px;
    display: flex;
    align-items: flex-start;
    gap: 11px;
  }

  .tcn-card .tcn-icon { font-size: 20px; flex-shrink: 0; }
  .tcn-card .tcn-title { font-weight: 600; font-size: 13px; color: var(--text); margin-bottom: 3px; }
  .tcn-card .tcn-desc  { font-size: 12px; color: var(--muted); line-height: 1.5; }

  /* ── Rule strip (horizontal rule list) ── */
  .rule-strip {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .rs-row {
    display: grid;
    grid-template-columns: 28px 1fr;
    border-bottom: 1px solid var(--border);
    align-items: stretch;
  }

  .rs-row:last-child { border-bottom: none; }

  .rs-row .rsr-icon {
    background: var(--off-white);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 13px;
    border-right: 1px solid var(--border);
    flex-shrink: 0;
  }

  .rs-row .rsr-text {
    padding: 9px 14px;
    font-size: 12.5px;
    color: var(--text);
    line-height: 1.55;
    background: var(--white);
  }

  .rs-row:nth-child(even) .rsr-text { background: var(--off-white); }
  .rs-row:nth-child(even) .rsr-icon { background: #f5f4f3; }
---

<!-- _class: cover -->

<div class="series-badge">PIPELINE AGENTS · LEVEL 2 — PART 3 OF 4</div>

# Connecting the Pipeline in Code
## Contracts, state, structure — making the chain run in Python

&nbsp;

**Designing agents is the easy part.** Connecting them so state flows cleanly from one to the next — that's the engineering.

`contracts` · `state` · `sequential` · `parallel` · `orchestrator` · `walkthrough`

---

## What We're Building Toward

We have five designed agents. Now we wire them together. Part 3 covers the four things every working pipeline needs before you write your first `run()` call.

<div class="matters-grid" style="margin-bottom: 16px;">
  <div class="matters-card">
    <div class="mcc-icon">📄</div>
    <div>
      <div class="mcc-title">Output contracts</div>
      <div class="mcc-desc">Define the exact schema each agent must produce. Until the contract is written, no agent can be implemented. The schema is the interface.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🔁</div>
    <div>
      <div class="mcc-title">Passing state in Python</div>
      <div class="mcc-desc">How to capture one agent's output, validate it, and inject it as the next agent's input — without losing data or silently corrupting the chain.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">⚡</div>
    <div>
      <div class="mcc-title">Sequential vs parallel</div>
      <div class="mcc-desc">Not every agent has to wait for the one before it. Knowing when to run stages in parallel — and when you can't — cuts latency without adding complexity.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🗂️</div>
    <div>
      <div class="mcc-title">Project structure</div>
      <div class="mcc-desc">Where the agent files live, where artifacts are saved, and how the orchestrator imports and sequences everything — before you write a single line of agent logic.</div>
    </div>
  </div>
</div>

<div class="highlight">

**The same pipeline throughout.** Every code example in Part 3 uses the five-agent content pipeline from Parts 1 and 2: Research → Outline → Writer → Editor → QA. Same agents, same artifacts — now with real Python.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Designing Output Contracts

A contract is the exact schema an agent must return. You write it before you write the agent. It is the interface between every pair of stages.

<div class="schema-block">
  <div class="sb-header">
    <div class="sb-title">research.json — output contract for the Research agent</div>
    <div class="sb-badge">schema</div>
  </div>
  <div class="sb-body"><span class="sk">"topic"</span>:    <span class="sv">"string — the original query, unchanged"</span>,
<span class="sk">"audience"</span>: <span class="sv">"string — target reader, from input spec"</span>,
<span class="sk">"claims"</span>: [
  {
    <span class="sk">"id"</span>:         <span class="sv">"string — unique key, e.g. C01"</span>,
    <span class="sk">"text"</span>:       <span class="sv">"string — the factual claim, one sentence"</span>,
    <span class="sk">"source"</span>:     <span class="sv">"string — URL or citation"</span>,
    <span class="sk">"confidence"</span>: <span class="sv">"HIGH | LOW"</span>
  }
],
<span class="sk">"keywords"</span>:    [<span class="sv">"string"</span>],   <span class="sc">// top terms for the Outline agent</span>
<span class="sk">"competitors"</span>: [<span class="sv">"string"</span>]   <span class="sc">// competing article URLs if found</span></div>
</div>

<div class="two-col-notes">
  <div class="tcn-card">
    <div class="tcn-icon">✍️</div>
    <div>
      <div class="tcn-title">Write the schema first — always</div>
      <div class="tcn-desc">The schema is the only thing both the agent and orchestrator agree on. Write the agent first and you'll reverse-engineer a schema that fits its output rather than one that serves the next stage.</div>
    </div>
  </div>
  <div class="tcn-card">
    <div class="tcn-icon">🔑</div>
    <div>
      <div class="tcn-title">IDs are the handoff mechanism</div>
      <div class="tcn-desc">Each claim gets an ID (e.g. <code>C01</code>). The Outline agent references <code>C01</code> in its section slots. The Writer pulls claim text by ID. The QA agent checks by ID. IDs make the chain traceable end-to-end.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01 — CONTINUED</div>

## Output Contracts for Every Stage

The full contract set for the five-agent pipeline. Define all five before writing any agent code.

<table class="cheat-table">
  <thead>
    <tr><th>Artifact</th><th>Format</th><th>Key fields</th><th>Consumed by</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="mono">research.json</span></td>
      <td>JSON object</td>
      <td><span class="mono">topic</span>, <span class="mono">claims[]</span> (id, text, source, confidence), <span class="mono">keywords[]</span></td>
      <td>Outline agent</td>
    </tr>
    <tr>
      <td><span class="mono">outline.json</span></td>
      <td>JSON object</td>
      <td><span class="mono">title</span>, <span class="mono">sections[]</span> (heading, claim_ids[], notes)</td>
      <td>Writer agent</td>
    </tr>
    <tr>
      <td><span class="mono">draft.md</span></td>
      <td>Markdown string</td>
      <td>H1 title, H2 section headings matching outline, body paragraphs only</td>
      <td>Editor agent</td>
    </tr>
    <tr>
      <td><span class="mono">edited.md</span></td>
      <td>Markdown string</td>
      <td>Same structure as <span class="mono">draft.md</span> — identical headings, cleaner body</td>
      <td>QA agent</td>
    </tr>
    <tr>
      <td><span class="mono">qa_report.json</span></td>
      <td>JSON object</td>
      <td><span class="mono">verdict</span> (pass/flagged), <span class="mono">flags[]</span> (claim_id, line, issue)</td>
      <td>Human / orchestrator</td>
    </tr>
  </tbody>
</table>

<div class="highlight">

**The markdown contracts are structural, not just format.** Specifying that <code>draft.md</code> uses H1 for the title and H2 for sections is not a style choice — it's an interface contract. The QA agent uses heading structure to locate claims by line. Change the heading level, break the QA agent.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Passing State Between Agents in Python

<div class="code-block">
  <div class="cb-header">
    <div class="cb-dots">
      <div class="cb-dot red"></div>
      <div class="cb-dot yellow"></div>
      <div class="cb-dot green"></div>
    </div>
    <div class="cb-filename">orchestrator.py — core state-passing pattern</div>
  </div>
  <div class="cb-body"><span class="kw">import</span> <span class="va">json</span>, <span class="va">anthropic</span>
<span class="kw">from</span> <span class="va">agents.research</span> <span class="kw">import</span> <span class="fn">run_research_agent</span>
<span class="kw">from</span> <span class="va">agents.outline</span>  <span class="kw">import</span> <span class="fn">run_outline_agent</span>
<span class="kw">from</span> <span class="va">contracts</span>       <span class="kw">import</span> <span class="fn">validate_research</span>, <span class="fn">validate_outline</span>
<span class="cm"># ── Step 1: call the agent ───────────────────────────────────────</span>
<span class="va">research_raw</span> = <span class="fn">run_research_agent</span>(
    <span class="va">topic</span>=<span class="st">"Why sleep deprivation impairs decision-making"</span>,
    <span class="va">audience</span>=<span class="st">"general readers, no medical background"</span>
)
<span class="cm"># ── Step 2: validate the contract ───────────────────────────────</span>
<span class="va">research</span> = <span class="fn">validate_research</span>(<span class="va">research_raw</span>)   <span class="cm"># raises if schema violated</span>
<span class="fn">save_artifact</span>(<span class="st">"artifacts/research.json"</span>, <span class="va">research</span>)
<span class="cm"># ── Step 3: forward only what the next agent needs ──────────────</span>
<span class="va">outline_raw</span> = <span class="fn">run_outline_agent</span>(
    <span class="va">research</span>=<span class="va">research</span>,           <span class="cm"># full contract object</span>
    <span class="va">target_format</span>=<span class="st">"blog post"</span>,
    <span class="va">word_count</span>=<span class="nu">1200</span>
)</div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02 - CONTINUED</div>

## Passing State Between Agents in Python

Every call to an agent follows the same three-step pattern: **call → validate → forward.** Skip validation and a silent contract violation propagates through the entire chain.


<div class="highlight">

**Never pass the raw LLM response downstream.** Parse and validate first. An agent that returns `{"claims": null}` instead of `{"claims": []}` will silently break every downstream agent that iterates over the list.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02 — CONTINUED</div>

## The `validate_*` Pattern — Catching Failures at the Handoff

One Pydantic model per artifact. One validate function per contract. Raises immediately so the error points to the exact handoff broke.

<div class="code-block">
  <div class="cb-header">
    <div class="cb-dots">
      <div class="cb-dot red"></div>
      <div class="cb-dot yellow"></div>
      <div class="cb-dot green"></div>
    </div>
    <div class="cb-filename">contracts.py — validation for research.json</div>
  </div>
  <div class="cb-body"><span class="kw">from</span> <span class="va">pydantic</span> <span class="kw">import</span> <span class="va">BaseModel</span>, <span class="va">Field</span>
<span class="kw">from</span> <span class="va">typing</span>  <span class="kw">import</span> <span class="va">List</span>, <span class="va">Literal</span>
<span class="kw">class</span> <span class="fn">Claim</span>(<span class="va">BaseModel</span>):
    <span class="va">id</span>:         <span class="va">str</span>
    <span class="va">text</span>:       <span class="va">str</span>
    <span class="va">source</span>:     <span class="va">str</span>
    <span class="va">confidence</span>: <span class="va">Literal</span>[<span class="st">"HIGH"</span>, <span class="st">"LOW"</span>]
<span class="kw">class</span> <span class="fn">ResearchArtifact</span>(<span class="va">BaseModel</span>):
    <span class="va">topic</span>:       <span class="va">str</span>
    <span class="va">audience</span>:    <span class="va">str</span>
    <span class="va">claims</span>:      <span class="va">List</span>[<span class="fn">Claim</span>] = <span class="va">Field</span>(<span class="va">min_length</span>=<span class="nu">1</span>)
    <span class="va">keywords</span>:    <span class="va">List</span>[<span class="va">str</span>]
    <span class="va">competitors</span>: <span class="va">List</span>[<span class="va">str</span>] = []
<span class="kw">def</span> <span class="fn">validate_research</span>(<span class="va">raw</span>: <span class="va">dict</span>) -> <span class="fn">ResearchArtifact</span>:
    <span class="kw">return</span> <span class="fn">ResearchArtifact</span>(**<span class="va">raw</span>)  <span class="cm"># raises ValidationError on any violation</span></div>
</div>

<div class="two-col-notes">
  <div class="tcn-card">
    <div class="tcn-icon">🛡️</div>
    <div>
      <div class="tcn-title">Pydantic is the contract enforcer</div>
      <div class="tcn-desc">Write one <code>BaseModel</code> per artifact. The schema is declared once, in code, and checked at every handoff. If the LLM drops a required key or hallucinates a field, validation raises before the next agent runs.</div>
    </div>
  </div>
  <div class="tcn-card">
    <div class="tcn-icon">🐛</div>
    <div>
      <div class="tcn-title">Errors point to the right stage</div>
      <div class="tcn-desc">Without validation, a missing <code>claim_id</code> in <code>research.json</code> produces a <code>KeyError</code> inside the QA agent — three stages later. With it, you get a <code>ValidationError</code> at the Research → Outline handoff, exactly where the fault is.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Sequential vs Parallel Pipelines

Not every stage has to wait for the one before it. Two agents that share no dependency can run simultaneously — cutting wall-clock time without changing logic.

<div class="seq-par-grid">
  <div class="sp-side sequential">
    <div class="sp-head">⏱️ &nbsp;Sequential — one at a time</div>
    <div class="sp-body">
      <div class="sp-step">
        <div class="sps-num">1</div>
        <div><span class="sps-label">Research agent runs</span><br><span class="sps-sub">→ produces research.json</span></div>
      </div>
      <div class="sp-arrow">↓ wait for completion</div>
      <div class="sp-step">
        <div class="sps-num">2</div>
        <div><span class="sps-label">Outline agent runs</span><br><span class="sps-sub">→ needs research.json</span></div>
      </div>
      <div class="sp-arrow">↓ wait for completion</div>
      <div class="sp-step">
        <div class="sps-num">3</div>
        <div><span class="sps-label">Writer agent runs</span><br><span class="sps-sub">→ needs both artifacts</span></div>
      </div>
      <div class="sp-arrow">↓ and so on…</div>
      <div class="sp-step">
        <div class="sps-num">4–5</div>
        <div><span class="sps-label">Editor → QA</span><br><span class="sps-sub">→ each waits on previous</span></div>
      </div>
    </div>
  </div>
  <div class="sp-side parallel">
    <div class="sp-head">⚡ &nbsp;Parallel — independent stages at once</div>
    <div class="sp-body">
      <div class="sp-step">
        <div class="sps-num">1</div>
        <div><span class="sps-label">Research agent runs</span><br><span class="sps-sub">→ produces research.json</span></div>
      </div>
      <div class="sp-arrow">↓ research.json available</div>
      <div class="sp-par-row">
        <div class="sp-step">
          <div class="sps-num">2a</div>
          <div><span class="sps-label">Outline agent</span><br><span class="sps-sub">→ outline.json</span></div>
        </div>
        <div class="sp-step">
          <div class="sps-num">2b</div>
          <div><span class="sps-label">SEO check agent</span><br><span class="sps-sub">→ seo_notes.json</span></div>
        </div>
      </div>
      <div class="sp-arrow">↓ await both, then merge</div>
      <div class="sp-step">
        <div class="sps-num">3</div>
        <div><span class="sps-label">Writer receives both</span><br><span class="sps-sub">→ outline + seo context merged</span></div>
      </div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03 — CONTINUED</div>

## When to Use Each — The Decision Rule

<table class="cheat-table">
  <thead>
    <tr><th>Situation</th><th>Use</th><th>Why</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>Agent B needs Agent A's output to run</td>
      <td><strong>Sequential</strong></td>
      <td>Hard data dependency — B cannot start without A's artifact. No choice.</td>
    </tr>
    <tr>
      <td>Two agents both read the same input, produce independent outputs</td>
      <td><strong>Parallel</strong></td>
      <td>No dependency between them. Run with <span class="mono">asyncio.gather()</span> — halves wait time.</td>
    </tr>
    <tr>
      <td>One agent is slow (web search, large context) and another is fast</td>
      <td><strong>Parallel</strong></td>
      <td>Fast agent completes while slow one runs. Total time = slowest agent, not sum.</td>
    </tr>
    <tr>
      <td>Agent B reads Agent A's output <em>and</em> its own earlier output</td>
      <td><strong>Sequential</strong></td>
      <td>B has a self-dependency on A. Any parallelism here produces a race condition.</td>
    </tr>
    <tr>
      <td>Uncertain whether a dependency exists</td>
      <td><strong>Sequential</strong></td>
      <td>Default to sequential. Add parallelism only when independence is provable. Parallel bugs produce silent corruption, not errors.</td>
    </tr>
  </tbody>
</table>

<div class="highlight">

**In our five-agent pipeline:** Research → Outline → Writer is strictly sequential. But once <code>research.json</code> exists, an optional SEO agent can run in parallel with Outline — both read only research, produce independent outputs, and merge before Writer runs.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Project Structure for a Multi-Agent Pipeline

Before writing any agent file, lay out the folder structure. Where a file lives determines what can import it.

<div class="file-tree">
  <div class="ft-header">📁 &nbsp;pipeline-project/</div>
  <div class="ft-body"><span class="fd">pipeline-project/</span>
├── <span class="fd">agents/</span>                    <span class="fc"># one file per specialist agent</span>
│   ├── <span class="fp">research.py</span>            <span class="fc"># run_research_agent(topic, audience) → dict</span>
│   ├── <span class="fp">outline.py</span>             <span class="fc"># run_outline_agent(research, format)  → dict</span>
│   ├── <span class="fp">writer.py</span>              <span class="fc"># run_writer_agent(outline, research)  → str</span>
│   ├── <span class="fp">editor.py</span>              <span class="fc"># run_editor_agent(draft)              → str</span>
│   └── <span class="fp">qa.py</span>                  <span class="fc"># run_qa_agent(edited, research)       → dict</span>
├── <span class="fd">artifacts/</span>                 <span class="fc"># saved outputs — one file per stage per run</span>
│   ├── <span class="fj">research.json</span>  ├── <span class="fj">outline.json</span>  ├── <span class="fm">draft.md</span>  ├── <span class="fm">edited.md</span>  └── <span class="fj">qa_report.json</span>
├── <span class="fp">contracts.py</span>               <span class="fc"># Pydantic models + validate_* functions</span>
├── <span class="fp">orchestrator.py</span>            <span class="fc"># sequences agents, handles state, runs pipeline</span>
├── <span class="fp">prompts.py</span>                 <span class="fc"># system prompt strings — one constant per agent</span>
└── <span class="fj">config.json</span>                <span class="fc"># model name, temperature, max_tokens per agent</span></div>
</div>

<div class="highlight">

**Three rules that hold for every pipeline project:** one file per agent, one public function per file (`run_*_agent()`), and every artifact written to `artifacts/` before it is forwarded. The orchestrator imports agent functions — it never calls the Anthropic client directly.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04 — CONTINUED</div>

## Why This Structure Matters

Every layout decision has a reason. These four rules prevent the most common refactors.

<div class="rule-strip">
  <div class="rs-row">
    <div class="rsr-icon">📐</div>
    <div class="rsr-text"><strong>One file, one agent, one function.</strong> Each agent file exports exactly one public function: <code>run_*_agent()</code>. The orchestrator imports only these — it never calls the Anthropic client directly from orchestrator code. Agent logic stays in agent files.</div>
  </div>
  <div class="rs-row">
    <div class="rsr-icon">💾</div>
    <div class="rsr-text"><strong>Artifacts are always written to disk before forwarding.</strong> Even in a fully sequential run, save every artifact before passing it on. Disk is your audit log. A crash at stage 4 means you re-run from stage 3's saved artifact — not from the beginning.</div>
  </div>
  <div class="rs-row">
    <div class="rsr-icon">📝</div>
    <div class="rsr-text"><strong>System prompts live in <code>prompts.py</code>, never inline.</strong> Agents import prompt constants — they never define prompt strings inside the function body. Prompts change constantly during development. One file means one place to change them.</div>
  </div>
  <div class="rs-row">
    <div class="rsr-icon">⚙️</div>
    <div class="rsr-text"><strong>Model config lives in <code>config.json</code>, never hardcoded.</strong> Each agent may warrant a different model, temperature, or token budget. Externalising config means you tune without touching agent code — and without breaking imports.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## Live Walkthrough — Research → Outline Handoff

The first real handoff: raw topic input → validated `research.json` → passed as a typed object into the Outline agent.

<div class="walkthrough">
  <div class="wt-row">
    <div class="wr-num">1</div>
    <div class="wr-content">
      <div class="wrc-title">🔍 &nbsp;Call the Research agent</div>
      <div class="wrc-desc">Pass the topic string and audience spec. The agent makes one API call with the Research system prompt and returns a raw JSON string from the model.</div>
      <div class="wrc-code">research_raw = run_research_agent(topic, audience)</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">2</div>
    <div class="wr-content">
      <div class="wrc-title">🛡️ &nbsp;Parse and validate the contract</div>
      <div class="wrc-desc">Strip any markdown fences the model may have added. Parse as JSON. Run through <code>ResearchArtifact</code>. Raises <code>ValidationError</code> immediately if the schema is violated — before anything downstream runs.</div>
      <div class="wrc-code">research = validate_research(json.loads(research_raw))</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">3</div>
    <div class="wr-content">
      <div class="wrc-title">💾 &nbsp;Save the artifact to disk</div>
      <div class="wrc-desc">Write the validated artifact to <code>artifacts/research.json</code> before moving on. This is the checkpoint — if anything after this point fails, the Research stage does not need to re-run.</div>
      <div class="wrc-code">save_artifact("artifacts/research.json", research.dict())</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">4</div>
    <div class="wr-content">
      <div class="wrc-title">🗂️ &nbsp;Call the Outline agent with the typed object</div>
      <div class="wrc-desc">Pass the <code>ResearchArtifact</code> object directly — not the raw dict. A missing field raises before the API call is even made.</div>
      <div class="wrc-code">outline_raw = run_outline_agent(research=research, format="blog post")</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">5</div>
    <div class="wr-content">
      <div class="wrc-title">✅ &nbsp;Validate and save outline.json — repeat</div>
      <div class="wrc-desc">Same pattern: parse → validate against <code>OutlineArtifact</code> → save to disk. The chain is now two stages deep with two verified checkpoints. Continue identically for Writer, Editor, and QA.</div>
      <div class="wrc-code">outline = validate_outline(json.loads(outline_raw))</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05 — CONTINUED</div>

## The Full Agent Function Pattern

Every agent file in `agents/` follows this identical three-section structure. One function. No variation.

<div class="code-block">
  <div class="cb-header">
    <div class="cb-dots">
      <div class="cb-dot red"></div>
      <div class="cb-dot yellow"></div>
      <div class="cb-dot green"></div>
    </div>
    <div class="cb-filename">agents/research.py</div>
  </div>
  <div class="cb-body"><span class="kw">import</span> <span class="va">anthropic</span>, <span class="va">json</span>
<span class="kw">from</span> <span class="va">prompts</span> <span class="kw">import</span> <span class="va">RESEARCH_SYSTEM_PROMPT</span>
<span class="va">client</span> = <span class="va">anthropic</span>.<span class="fn">Anthropic</span>()
<span class="kw">def</span> <span class="fn">run_research_agent</span>(<span class="va">topic</span>: <span class="va">str</span>, <span class="va">audience</span>: <span class="va">str</span>) -> <span class="va">str</span>:
    <span class="cm"># ── 1. Build the user message ────────────────────────────────</span>
    <span class="va">user_msg</span> = <span class="st">f"Topic: {topic}\nAudience: {audience}"</span>
    <span class="cm"># ── 2. Call the API with the specialist system prompt ────────</span>
    <span class="va">response</span> = <span class="va">client</span>.<span class="va">messages</span>.<span class="fn">create</span>(
        <span class="va">model</span>=<span class="st">"claude-sonnet-4-20250514"</span>,
        <span class="va">max_tokens</span>=<span class="nu">2048</span>,
        <span class="va">system</span>=<span class="va">RESEARCH_SYSTEM_PROMPT</span>,
        <span class="va">messages</span>=[{<span class="st">"role"</span>: <span class="st">"user"</span>, <span class="st">"content"</span>: <span class="va">user_msg</span>}]
    )
    <span class="cm"># ── 3. Return raw text — orchestrator validates ───────────────</span>
    <span class="kw">return</span> <span class="va">response</span>.<span class="va">content</span>[<span class="nu">0</span>].<span class="va">text</span></div>
</div>

<div class="highlight">

**The agent function has one job: call the API and return text.** It does not parse JSON. It does not validate. It does not save to disk. All of that happens in the orchestrator — because pipeline logic belongs there, not inside the agent. Keep agents thin.

</div>

---

## Quick Reference — Part 3 in One Table

The patterns, rules, and file locations that apply to every pipeline you build.

<table class="cheat-table">
  <thead>
    <tr><th>Topic</th><th>Rule</th><th>Where it lives</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Output contract</strong></td>
      <td>Write the schema before the agent. One Pydantic model per artifact.</td>
      <td><span class="mono">contracts.py</span></td>
    </tr>
    <tr>
      <td><strong>State passing</strong></td>
      <td>Call → validate → save → forward. Never skip validation.</td>
      <td><span class="mono">orchestrator.py</span></td>
    </tr>
    <tr>
      <td><strong>Artifact persistence</strong></td>
      <td>Write every artifact to disk before forwarding, even in sequential runs.</td>
      <td><span class="mono">artifacts/</span></td>
    </tr>
    <tr>
      <td><strong>Sequential default</strong></td>
      <td>Run sequentially unless independence is provable. Parallel bugs are silent.</td>
      <td><span class="mono">orchestrator.py</span></td>
    </tr>
    <tr>
      <td><strong>Parallel trigger</strong></td>
      <td>Two agents both read the same input, neither reads the other's output.</td>
      <td><span class="mono">asyncio.gather()</span></td>
    </tr>
    <tr>
      <td><strong>Agent function</strong></td>
      <td>One public function per agent file. Takes typed input, returns raw string.</td>
      <td><span class="mono">agents/*.py</span></td>
    </tr>
    <tr>
      <td><strong>System prompts</strong></td>
      <td>All system prompt strings in one file. Agents import — never define inline.</td>
      <td><span class="mono">prompts.py</span></td>
    </tr>
  </tbody>
</table>

---

<!-- _class: final -->

# The pipeline runs on contracts, not code.

&nbsp;

*Get the schemas right and the Python almost writes itself.*

&nbsp;

Next: **Part 4 — Error Handling, Retries, and Quality Gates.**

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*