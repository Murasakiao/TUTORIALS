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
  .cheat-table tr:last-child td { border-bottom: 1px solid var(--border); }
  .cheat-table tr:nth-child(even) td { background: var(--off-white); }

  .cheat-table .mono {
    font-family: 'DM Mono', monospace;
    color: var(--amber-dim);
    font-size: 12px;
  }

  /* ── Walkthrough step strip ── */
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

  .wt-row .wr-content { padding: 11px 16px; }

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

  .code-block .cb-header .cb-dots { display: flex; gap: 5px; }
  .code-block .cb-header .cb-dot  { width: 10px; height: 10px; border-radius: 50%; }
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
    padding: 16px 20px;
    font-size: 12px;
    line-height: 1.75;
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

  /* ── Schema block ── */
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
    font-size: 12px;
    line-height: 1.8;
    color: #bae6fd;
    white-space: pre;
  }

  .schema-block .sb-body .sk { color: #fde68a; }
  .schema-block .sb-body .sv { color: #86efac; }
  .schema-block .sb-body .sn { color: #fb923c; }
  .schema-block .sb-body .sc { color: #57534e; }

  /* ── Prompt anatomy box ── */
  .prompt-box {
    background: #1c1917;
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0;
    border: 1px solid #44403c;
  }

  .prompt-box .pb-header {
    padding: 9px 18px;
    background: #292524;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #78716c;
    border-bottom: 1px solid #44403c;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .prompt-box .pb-header .pb-label { color: #fbbf24; font-weight: 500; }

  .prompt-box .pb-body {
    padding: 16px 20px;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .pb-section {
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 12.5px;
    line-height: 1.6;
    font-family: 'DM Mono', monospace;
  }

  .pb-section .pbs-tag {
    font-size: 10px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 5px;
    display: block;
  }

  .pb-section.role   { background: rgba(251,191,36,0.10); border: 1px solid rgba(251,191,36,0.2);  color: #fde68a; }
  .pb-section.scope  { background: rgba(134,239,172,0.08); border: 1px solid rgba(134,239,172,0.2); color: #86efac; }
  .pb-section.format { background: rgba(196,181,253,0.08); border: 1px solid rgba(196,181,253,0.2); color: #c4b5fd; }
  .pb-section.limits { background: rgba(253,186,116,0.08); border: 1px solid rgba(253,186,116,0.2); color: #fdba74; }

  .pb-section.role   .pbs-tag { color: #fbbf24; }
  .pb-section.scope  .pbs-tag { color: #86efac; }
  .pb-section.format .pbs-tag { color: #c4b5fd; }
  .pb-section.limits .pbs-tag { color: #fdba74; }

  /* ── Anatomy layer stack ── */
  .anatomy-box {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .anatomy-box .ab-header {
    padding: 10px 14px;
    font-weight: 600;
    font-size: 13.5px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border);
    background: var(--amber-light);
    color: #92400e;
    border-color: #fde68a;
  }

  .anatomy-box { border-color: #fde68a; }

  .anatomy-box .ab-body {
    padding: 12px 14px;
    background: var(--white);
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .ab-layer {
    border-radius: 6px;
    padding: 9px 13px;
    font-size: 13px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .ab-layer .abl-icon { font-size: 18px; flex-shrink: 0; }
  .ab-layer .abl-name { font-weight: 600; font-size: 13px; }
  .ab-layer .abl-desc { font-size: 12px; color: var(--muted); margin-top: 1px; }

  .ab-layer.intent { background: #f0f9ff;           border: 1px solid #bae6fd; }
  .ab-layer.select { background: var(--amber-light); border: 1px solid #fde68a; }
  .ab-layer.handle { background: #f0fdf4;            border: 1px solid #bbf7d0; }
  .ab-layer.limit  { background: #fef2f2;            border: 1px solid #fecaca; }

  /* ── Bad / good compare ── */
  .compare-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin: 14px 0;
  }

  .cg-card {
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .cg-card .cg-head {
    padding: 9px 14px;
    font-weight: 600;
    font-size: 12.5px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border);
  }

  .cg-card.bad  .cg-head { background: #fef2f2; color: #991b1b; border-color: #fecaca; }
  .cg-card.good .cg-head { background: #f0fdf4; color: #166534; border-color: #bbf7d0; }

  .cg-card .cg-body {
    padding: 12px 14px;
    font-size: 12.5px;
    color: var(--muted);
    background: var(--white);
    line-height: 1.65;
  }

  .cg-card.good .cg-body { color: var(--text); }

  /* ── Result handling flow ── */
  .result-flow {
    display: flex;
    align-items: stretch;
    gap: 0;
    margin: 18px 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .rf-node {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 16px 10px;
    text-align: center;
    gap: 5px;
    min-width: 0;
  }

  .rf-node .rfn-icon { font-size: 24px; }

  .rf-node .rfn-type {
    font-family: 'DM Mono', monospace;
    font-size: 9.5px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
  }

  .rf-node .rfn-name { font-weight: 700; font-size: 13px; color: var(--text); }
  .rf-node .rfn-sub  { font-size: 11px; color: var(--muted); line-height: 1.4; }

  .rf-node.n-raw      { background: var(--off-white); }
  .rf-node.n-raw      .rfn-type { color: var(--muted); }
  .rf-node.n-validate { background: #f0f9ff; }
  .rf-node.n-validate .rfn-type { color: #0369a1; }
  .rf-node.n-merge    { background: var(--amber-light); }
  .rf-node.n-merge    .rfn-type { color: #92400e; }
  .rf-node.n-format   { background: #f0fdf4; }
  .rf-node.n-format   .rfn-type { color: #166534; }
  .rf-node.n-return   { background: #fdf4ff; }
  .rf-node.n-return   .rfn-type { color: #6b21a8; }

  .rf-arrow {
    display: flex;
    align-items: center;
    padding: 0 6px;
    font-size: 16px;
    color: var(--amber);
    background: var(--white);
    border-left: 1px solid var(--border);
    border-right: 1px solid var(--border);
    flex-shrink: 0;
  }

  /* ── Drift symptoms ── */
  .drift-stack {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .ds-row {
    display: grid;
    grid-template-columns: 200px 1fr auto;
    align-items: stretch;
    border-bottom: 1px solid var(--border);
  }

  .ds-row:last-child { border-bottom: none; }

  .ds-row .dsr-symptom {
    padding: 11px 14px;
    font-weight: 600;
    font-size: 12.5px;
    color: var(--text);
    background: #fef2f2;
    border-right: 1px solid #fecaca;
    display: flex;
    align-items: center;
    gap: 8px;
    line-height: 1.4;
  }

  .ds-row .dsr-desc {
    padding: 11px 14px;
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.6;
    display: flex;
    align-items: center;
  }

  .ds-row .dsr-fix {
    padding: 11px 14px;
    border-left: 1px solid var(--border);
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    display: flex;
    align-items: center;
    background: #f0fdf4;
    color: #166534;
    white-space: nowrap;
  }
---

<!-- _class: cover -->

<div class="series-badge">ORCHESTRATOR + SPECIALISTS · LEVEL 3 — PART 2 OF 4</div>

# Designing the Orchestrator
## System prompt, intent parsing, routing, and result handling

&nbsp;

**The orchestrator is just an agent with a specific job.** Design it like one — narrow role, tight output format, explicit constraints, and a hard rule about what it must never do.

`anatomy` · `system prompt` · `intent` · `routing` · `result handling` · `scope`

---

## What You're Designing

Part 1 introduced the concept. Part 2 is about implementation — the decisions you make before writing a single line of orchestrator code.

<div class="matters-grid">
  <div class="matters-card">
    <div class="mcc-icon">🏗️</div>
    <div>
      <div class="mcc-title">Anatomy first</div>
      <div class="mcc-desc">Before writing the system prompt, map the orchestrator's four layers: what it reads, what it decides, what it calls, and what it must never do. The anatomy defines everything that follows.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">📝</div>
    <div>
      <div class="mcc-title">Prompt is the contract</div>
      <div class="mcc-desc">The orchestrator's system prompt is the most important prompt in the system. It defines intent parsing, routing logic, and output format for every request the system will ever handle.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🎯</div>
    <div>
      <div class="mcc-title">Intent parsing is a structured output problem</div>
      <div class="mcc-desc">The orchestrator doesn't free-text its way to a decision. It produces a validated JSON routing decision — task type, selected pipeline, parameters — that the orchestrator loop can act on programmatically.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🚧</div>
    <div>
      <div class="mcc-title">Scope boundaries need to be explicit</div>
      <div class="mcc-desc">The hardest thing to design isn't what the orchestrator does — it's what it must not do. Every vague instruction in the system prompt is an invitation for the orchestrator to absorb specialist work.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Anatomy of an Orchestrator Agent

An orchestrator is an agent like any other — model, system prompt, loop. What makes it an orchestrator is what its four layers do and, crucially, what the fourth layer forbids.

<div class="anatomy-box">
  <div class="ab-header">🧭 &nbsp;Orchestrator agent — four layers</div>
  <div class="ab-body">
    <div class="ab-layer intent">
      <div class="abl-icon">🔍</div>
      <div>
        <div class="abl-name">Intent layer</div>
        <div class="abl-desc">Reads raw user input. Produces a structured routing decision — task type, pipeline name, parameters. This is the only thing the LLM decides.</div>
      </div>
    </div>
    <div class="ab-layer select">
      <div class="abl-icon">🎯</div>
      <div>
        <div class="abl-name">Selection layer</div>
        <div class="abl-desc">Your code maps the routing decision to a specialist or pipeline function. The LLM names the route — code executes it. Never let the LLM call specialists directly.</div>
      </div>
    </div>
    <div class="ab-layer handle">
      <div class="abl-icon">📦</div>
      <div>
        <div class="abl-name">Result layer</div>
        <div class="abl-desc">Receives the specialist's artifact. Validates it, formats the final response for the caller, and returns it. May merge results from multiple specialists.</div>
      </div>
    </div>
    <div class="ab-layer limit">
      <div class="abl-icon">🚫</div>
      <div>
        <div class="abl-name">Scope boundary</div>
        <div class="abl-desc">The hard constraint baked into the system prompt: the orchestrator never performs research, writing, editing, or any specialist task. If it cannot route to an available specialist, it returns <code>{"error": "no_route"}</code>.</div>
      </div>
    </div>
  </div>
</div>

<div class="highlight">

**The LLM's only job is the intent layer.** Selection and result handling are Python code. The LLM produces a JSON decision — your loop acts on it. This keeps routing deterministic and auditable.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Writing the Orchestrator System Prompt

The orchestrator's system prompt has the same four-part structure as any agent — Role, Scope, Output format, Constraints — but the content of each part is uniquely important here.

<div class="prompt-box">
  <div class="pb-header">
    <span class="pb-label">prompts/orchestrator_system.txt</span>
    <span>orchestrator system prompt</span>
  </div>
  <div class="pb-body">
    <div class="pb-section role">
      <span class="pbs-tag">① Role</span>
      You are a routing orchestrator. Your only job is to read a user request, identify its intent, and return a structured routing decision. You do not perform any of the tasks yourself.
    </div>
    <div class="pb-section scope">
      <span class="pbs-tag">② Available pipelines (scope)</span>
      You may route to exactly these pipelines:
      "content_pipeline" — for writing, summarising, or editing text content.
      "data_pipeline"    — for analysing, cleaning, or reporting on data files.
      "research_pipeline"— for finding facts, sources, or competitor information.
    </div>
    <div class="pb-section format">
      <span class="pbs-tag">③ Output format — always JSON, no exceptions</span>
      {"pipeline": "&lt;pipeline_name&gt;", "task": "&lt;one_sentence_description&gt;", "params": {"key": "value"}, "confidence": "HIGH|LOW"}
    </div>
    <div class="pb-section limits">
      <span class="pbs-tag">④ Constraints</span>
      If the request does not match any listed pipeline, return {"error": "no_route", "reason": "&lt;why&gt;"}. Never attempt to answer the user's question directly. Never add prose outside the JSON object.
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02 — CONTINUED</div>

## What Makes the Orchestrator Prompt Different

The system prompts you wrote in Level 1 and 2 told agents to *do* something. The orchestrator prompt tells the agent to *decide* something — and explicitly forbids doing anything else.

<div class="compare-grid">
  <div class="cg-card bad">
    <div class="cg-head">❌ &nbsp;Specialist prompt pattern — wrong for orchestrator</div>
    <div class="cg-body">
      "You are a research analyst. Given a topic, find key facts, evaluate sources, and return a structured JSON with claims and citations."<br><br>
      This pattern is correct for a specialist. Applied to an orchestrator, it produces an agent that does research instead of routing to a researcher.
    </div>
  </div>
  <div class="cg-card good">
    <div class="cg-head">✅ &nbsp;Orchestrator prompt pattern — decision only</div>
    <div class="cg-body">
      "You are a routing agent. Read the request, identify which pipeline it belongs to, and return a routing decision as JSON. You do not perform research, writing, or analysis yourself. If you cannot route it, say so."<br><br>
      The prompt closes every door except the routing decision.
    </div>
  </div>
</div>

<div class="matters-grid" style="margin-top: 0;">
  <div class="matters-card">
    <div class="mcc-icon">📋</div>
    <div>
      <div class="mcc-title">List every available pipeline explicitly</div>
      <div class="mcc-desc">Don't say "route to the appropriate pipeline." Name each one with its exact identifier and a one-line description of what it handles. The model cannot route to something it doesn't know exists.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🚫</div>
    <div>
      <div class="mcc-title">Name the failure case explicitly</div>
      <div class="mcc-desc">Tell the orchestrator exactly what to return when it can't route — a specific JSON error structure. Without this, it will attempt to answer the request itself rather than admit it has no route.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## How the Orchestrator Parses Intent

Intent parsing is a structured output problem. The orchestrator reads the raw request and produces one JSON object — and only that object. No prose, no explanation, no hedging.

<div class="schema-block">
  <div class="sb-header">
    <div class="sb-title">routing_decision.json — the orchestrator's only output</div>
    <div class="sb-badge">schema</div>
  </div>
  <div class="sb-body"><span class="sk">"pipeline"</span>:    <span class="sv">"content_pipeline"</span>,          <span class="sc">// exact pipeline identifier string</span>
<span class="sk">"task"</span>:       <span class="sv">"Summarise competitor pricing pages"</span>,
<span class="sk">"params"</span>: {
  <span class="sk">"input_type"</span>: <span class="sv">"url_list"</span>,
  <span class="sk">"output_format"</span>: <span class="sv">"comparison_table"</span>,
  <span class="sk">"audience"</span>:     <span class="sv">"product team"</span>
},
<span class="sk">"confidence"</span>:  <span class="sv">"HIGH"</span>                     <span class="sc">// HIGH = clear match, LOW = uncertain</span></div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03 - C0NTINUED</div>

## Intent Parsing of the Orchestrator

The orchestrator converts a user request into one validated JSON routing decision; LOW confidence triggers a clarification, HIGH confidence dispatches the named pipeline with the validated params.

<div class="walkthrough">
  <div class="wt-row">
    <div class="wr-num">1</div>
    <div class="wr-content">
      <div class="wrc-title">📥 &nbsp;Raw user input arrives</div>
      <div class="wrc-desc">"Can you look at our top five competitors' pricing pages and pull out what each tier costs and what's included?"</div>
      <div class="wrc-code">user_input = "Can you look at our top five competitors..."</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">2</div>
    <div class="wr-content">
      <div class="wrc-title">🧠 &nbsp;Orchestrator LLM call — one API call, one job</div>
      <div class="wrc-desc">The orchestrator's system prompt + user input → LLM → JSON routing decision. The model identifies this as a research + structure task, maps it to <code>research_pipeline</code>, and extracts the implicit parameters.</div>
      <div class="wrc-code">response = call_orchestrator(user_input) → routing_decision.json</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">3</div>
    <div class="wr-content">
      <div class="wrc-title">🛡️ &nbsp;Validate the routing decision</div>
      <div class="wrc-desc">Parse and validate against the <code>RoutingDecision</code> Pydantic model. Check that <code>pipeline</code> is a known identifier. If <code>confidence</code> is LOW, surface to the caller for confirmation before proceeding.</div>
      <div class="wrc-code">decision = validate_routing(json.loads(raw)) → RoutingDecision</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">4</div>
    <div class="wr-content">
      <div class="wrc-title">⚡ &nbsp;Dispatch to the selected pipeline</div>
      <div class="wrc-desc">Your code looks up the pipeline function by name, passes the validated params, and runs it. The orchestrator's LLM is now done — all remaining work is in the specialist pipeline.</div>
      <div class="wrc-code">result = PIPELINE_REGISTRY[decision.pipeline](**decision.params)</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## How the Orchestrator Selects the Right Pipeline

The LLM names the route. Your code executes it. The bridge between them is a pipeline registry — a dictionary that maps string identifiers to callable functions.

<div class="code-block">
  <div class="cb-header">
    <div class="cb-dots">
      <div class="cb-dot red"></div>
      <div class="cb-dot yellow"></div>
      <div class="cb-dot green"></div>
    </div>
    <div class="cb-filename">orchestrator.py — registry + dispatch</div>
  </div>
  <div class="cb-body"><span class="kw">from</span> <span class="va">pipelines.content</span>  <span class="kw">import</span> <span class="fn">run_content_pipeline</span>
<span class="kw">from</span> <span class="va">pipelines.data</span>     <span class="kw">import</span> <span class="fn">run_data_pipeline</span>
<span class="kw">from</span> <span class="va">pipelines.research</span> <span class="kw">import</span> <span class="fn">run_research_pipeline</span>
<span class="cm"># ── The registry: LLM names a key, code calls the value ──</span>
<span class="va">PIPELINE_REGISTRY</span> = {
    <span class="st">"content_pipeline"</span>:  <span class="fn">run_content_pipeline</span>,
    <span class="st">"data_pipeline"</span>:     <span class="fn">run_data_pipeline</span>,
    <span class="st">"research_pipeline"</span>: <span class="fn">run_research_pipeline</span>,
}
<span class="kw">def</span> <span class="fn">dispatch</span>(<span class="va">decision</span>: <span class="va">RoutingDecision</span>) -> <span class="va">dict</span>:
    <span class="kw">if</span> <span class="va">decision</span>.<span class="va">pipeline</span> <span class="kw">not in</span> <span class="va">PIPELINE_REGISTRY</span>:
        <span class="kw">raise</span> <span class="va">PipelineError</span>(<span class="st">f"Unknown pipeline: {decision.pipeline}"</span>)
    <span class="kw">if</span> <span class="va">decision</span>.<span class="va">confidence</span> == <span class="st">"LOW"</span>:
        <span class="kw">return</span> {<span class="st">"status"</span>: <span class="st">"needs_clarification"</span>, <span class="st">"task"</span>: <span class="va">decision</span>.<span class="va">task</span>}
    <span class="va">pipeline_fn</span> = <span class="va">PIPELINE_REGISTRY</span>[<span class="va">decision</span>.<span class="va">pipeline</span>]
    <span class="kw">return</span> <span class="fn">pipeline_fn</span>(**<span class="va">decision</span>.<span class="va">params</span>.<span class="bi">dict</span>())</div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04 — CONTINUED</div>

## Handling the LOW Confidence Case

LOW confidence: a possible but uncertain match — pause for clarification before running the pipeline.

<div class="walkthrough">
  <div class="wt-row">
    <div class="wr-num">1</div>
    <div class="wr-content">
      <div class="wrc-title">💬 &nbsp;Ambiguous input arrives</div>
      <div class="wrc-desc">"Can you help me with the quarterly review?" — This could mean a data report, a written summary, or a research brief. The orchestrator cannot confidently pick one pipeline.</div>
      <div class="wrc-code">input: "Can you help me with the quarterly review?"</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">2</div>
    <div class="wr-content">
      <div class="wrc-title">🧠 &nbsp;Orchestrator returns LOW confidence</div>
      <div class="wrc-desc">Rather than guessing, it returns its best guess with <code>"confidence": "LOW"</code> and a short reason. This is the correct behaviour — not a failure.</div>
      <div class="wrc-code">{"pipeline": "data_pipeline", "confidence": "LOW", "reason": "unclear if data or written report"}</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">3</div>
    <div class="wr-content">
      <div class="wrc-title">⏸️ &nbsp;Dispatcher surfaces for clarification</div>
      <div class="wrc-desc">The <code>dispatch()</code> function checks confidence before running the pipeline. On LOW, it returns a clarification prompt to the caller instead of firing the pipeline. No tokens wasted on a wrong run.</div>
      <div class="wrc-code">return {"status": "needs_clarification", "question": "Is this a data report or a written summary?"}</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">4</div>
    <div class="wr-content">
      <div class="wrc-title">✅ &nbsp;Caller clarifies, orchestrator re-routes with HIGH</div>
      <div class="wrc-desc">The clarified input goes back through the orchestrator. This time it returns HIGH confidence. Dispatch fires the correct pipeline. Total extra cost: one small routing call.</div>
      <div class="wrc-code">re-route → {"pipeline": "data_pipeline", "confidence": "HIGH"} → dispatch</div>
    </div>
  </div>
</div>

<div class="matters-grid" style="margin-top: 0;">
  <div class="matters-card">
    <div class="mcc-icon">🗂️</div>
    <div>
      <div class="mcc-title">The registry is the source of truth</div>
      <div class="mcc-desc">Keep the system prompt and PIPELINE_REGISTRY in sync; mismatches let the LLM pick non‑existent routes, causing dispatch errors.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🔐</div>
    <div>
      <div class="mcc-title">Never let the LLM call functions directly</div>
      <div class="mcc-desc">The LLM returns a pipeline name string; your code looks it up and calls it, and unknown/hallucinated names raise a <code>PipelineError</code>, preventing arbitrary execution.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## How It Handles the Result and Passes It Back

The orchestrator receives the specialist's output, validates it, optionally formats it for the caller, and returns it. The shape of what it returns depends on whether the caller is a human or another system.

<div class="result-flow">
  <div class="rf-node n-raw">
    <div class="rfn-icon">📨</div>
    <div class="rfn-type">Raw result</div>
    <div class="rfn-name">Specialist output</div>
    <div class="rfn-sub">Artifact from<br>pipeline run</div>
  </div>
  <div class="rf-arrow">→</div>
  <div class="rf-node n-validate">
    <div class="rfn-icon">🛡️</div>
    <div class="rfn-type">Validate</div>
    <div class="rfn-name">Contract check</div>
    <div class="rfn-sub">Pydantic model<br>or schema check</div>
  </div>
  <div class="rf-arrow">→</div>
  <div class="rf-node n-merge">
    <div class="rfn-icon">🔀</div>
    <div class="rfn-type">Merge</div>
    <div class="rfn-name">If multi-agent</div>
    <div class="rfn-sub">Combine results<br>from parallel calls</div>
  </div>
  <div class="rf-arrow">→</div>
  <div class="rf-node n-format">
    <div class="rfn-icon">📐</div>
    <div class="rfn-type">Format</div>
    <div class="rfn-name">Shape for caller</div>
    <div class="rfn-sub">Human-readable<br>or API payload</div>
  </div>
  <div class="rf-arrow">→</div>
  <div class="rf-node n-return">
    <div class="rfn-icon">📤</div>
    <div class="rfn-type">Return</div>
    <div class="rfn-name">Final response</div>
    <div class="rfn-sub">To UI, API,<br>or next agent</div>
  </div>
</div>

<div class="compare-grid">
  <div class="cg-card bad">
    <div class="cg-head">❌ &nbsp;Orchestrator rewrites the result</div>
    <div class="cg-body">
      After the writer pipeline returns <code>draft.md</code>, the orchestrator's system prompt says "clean it up and make it more professional before returning." It has become an editor. The writer pipeline's output is no longer what the caller receives — the orchestrator's rewrite is.
    </div>
  </div>
  <div class="cg-card good">
    <div class="cg-head">✅ &nbsp;Orchestrator formats, not rewrites</div>
    <div class="cg-body">
      The orchestrator validates the artifact, wraps it in a standard response envelope — <code>{"status": "ok", "pipeline": "content_pipeline", "result": ...}</code> — and returns it. It shapes the delivery. It never touches the content.
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 06</div>

## Keeping the Orchestrator from Becoming a Worker

Orchestrator scope creep is the most common failure mode at Level 3. It happens gradually — one helpful addition to the system prompt at a time. These are the symptoms and the fixes.

<div class="drift-stack">
  <div class="ds-row">
    <div class="dsr-symptom">🐛 &nbsp;Prompt gets longer after every failure</div>
    <div class="dsr-desc">Each new failure case is patched by adding another instruction to the orchestrator prompt. The prompt now handles edge cases, partial tasks, and fallbacks — all of which should live in the specialists.</div>
    <div class="dsr-fix">move to specialist</div>
  </div>
  <div class="ds-row">
    <div class="dsr-symptom">✍️ &nbsp;"Also summarise the result"</div>
    <div class="dsr-desc">Someone added "and provide a brief summary of the result before returning" to the orchestrator prompt. Now every result passes through an untracked summarisation step that bypasses the summarise specialist.</div>
    <div class="dsr-fix">remove or delegate</div>
  </div>
  <div class="ds-row">
    <div class="dsr-symptom">❓ &nbsp;"If you're unsure, try to answer"</div>
    <div class="dsr-desc">A well-intentioned fallback instruction: "if no pipeline matches, try to answer the user directly." The orchestrator now attempts to handle unrouted requests — becoming a generalist agent with routing bolted on.</div>
    <div class="dsr-fix">return no_route error</div>
  </div>
  <div class="ds-row">
    <div class="dsr-symptom">🔧 &nbsp;Two pipelines merged into one prompt</div>
    <div class="dsr-desc">The content and research pipelines were consolidated into the orchestrator "to save API calls." It now does research and writing in a single call. You've rebuilt the single-agent problem inside the orchestrator.</div>
    <div class="dsr-fix">restore specialist split</div>
  </div>
  <div class="ds-row">
    <div class="dsr-symptom">📈 &nbsp;Token count climbs per request</div>
    <div class="dsr-desc">Orchestrator calls that should be fast and cheap are now expensive. A routing decision shouldn't cost 2 000 output tokens. If it does, the orchestrator is producing content, not just a decision.</div>
    <div class="dsr-fix">audit output length</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 06 — CONTINUED</div>

## The Scope Audit — Checking Your Orchestrator Stays Thin

Run this checklist against your orchestrator whenever its output token count climbs or a new instruction gets added to its prompt.

<table class="cheat-table">
  <thead>
    <tr><th>Check</th><th>Pass condition</th><th>If it fails</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Output size</strong></td>
      <td>Routing decision is under 200 tokens on every call. Always a JSON object, never prose.</td>
      <td>The orchestrator is generating content. Strip everything outside the routing JSON.</td>
    </tr>
    <tr>
      <td><strong>System prompt length</strong></td>
      <td>Orchestrator system prompt is shorter than any specialist's system prompt.</td>
      <td>Instructions have leaked in. Each extra instruction is a job the orchestrator has absorbed.</td>
    </tr>
    <tr>
      <td><strong>No-route behaviour</strong></td>
      <td>Unroutable requests return <code>{"error": "no_route"}</code> — not an answer.</td>
      <td>Remove any "if you can't route, try to help" language from the prompt.</td>
    </tr>
    <tr>
      <td><strong>Result passthrough</strong></td>
      <td>Specialist output reaches the caller unchanged in content. Only the envelope differs.</td>
      <td>The orchestrator is rewriting results. Move that logic into a formatting specialist.</td>
    </tr>
    <tr>
      <td><strong>Registry sync</strong></td>
      <td>Every pipeline named in the system prompt exists in <code>PIPELINE_REGISTRY</code>.</td>
      <td>Update the registry or remove the stale pipeline from the prompt immediately.</td>
    </tr>
  </tbody>
</table>

<div class="highlight">

**The benchmark:** A healthy orchestrator makes one API call per request, returns a JSON object under 200 tokens, and its system prompt names exactly the pipelines in the registry — nothing more. If yours doesn't match this description, run the audit above.

</div>

---

## Quick Reference — Part 2 Design Decisions

The choices you make once, before writing any orchestrator code.

<table class="cheat-table">
  <thead>
    <tr><th>Decision</th><th>Rule</th><th>Where it lives</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Orchestrator role</strong></td>
      <td>Route only. Never perform specialist tasks. Explicitly stated in the system prompt.</td>
      <td><span class="mono">prompts/orchestrator_system.txt</span></td>
    </tr>
    <tr>
      <td><strong>Pipeline list</strong></td>
      <td>Named explicitly in the system prompt with exact identifiers matching the registry.</td>
      <td><span class="mono">prompts/</span> + <span class="mono">PIPELINE_REGISTRY</span></td>
    </tr>
    <tr>
      <td><strong>Routing output schema</strong></td>
      <td>One Pydantic model. Fields: <code>pipeline</code>, <code>task</code>, <code>params</code>, <code>confidence</code>. Validated at every call.</td>
      <td><span class="mono">contracts.py</span></td>
    </tr>
    <tr>
      <td><strong>LOW confidence behaviour</strong></td>
      <td>Return clarification request to caller. Never guess and fire a pipeline.</td>
      <td><span class="mono">orchestrator.py → dispatch()</span></td>
    </tr>
    <tr>
      <td><strong>No-route behaviour</strong></td>
      <td>Return <code>{"error": "no_route"}</code>. Never answer directly.</td>
      <td><span class="mono">prompts/orchestrator_system.txt</span></td>
    </tr>
    <tr>
      <td><strong>Result handling</strong></td>
      <td>Validate the artifact. Wrap in a standard envelope. Never rewrite content.</td>
      <td><span class="mono">orchestrator.py → handle_result()</span></td>
    </tr>
    <tr>
      <td><strong>Scope audit trigger</strong></td>
      <td>Run the audit when output token count rises, or before adding any new prompt instruction.</td>
      <td>Recurring code review</td>
    </tr>
  </tbody>
</table>

---

<!-- _class: final -->

# Design the boundaries before you write the prompt.

&nbsp;

*What it routes. What it never does. What it returns when it can't route. In that order.*

&nbsp;

Next: **Part 3 — Connecting Specialists to the Orchestrator.**

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*