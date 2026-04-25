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

  /* ── Versus grid ── */
  .versus-grid {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    gap: 0;
    align-items: stretch;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 16px 0;
  }

  .vs-side { padding: 16px 18px; }
  .vs-side.pipeline     { background: var(--off-white); }
  .vs-side.orchestrated { background: #fffbeb; }

  .vs-side .vs-label {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.09em;
    margin-bottom: 8px;
  }

  .vs-side.pipeline     .vs-label { color: var(--muted); }
  .vs-side.orchestrated .vs-label { color: #92400e; }

  .vs-side .vs-title {
    font-weight: 700;
    font-size: 16.5px;
    color: var(--text);
    margin-bottom: 10px;
  }

  .vs-side .vs-item {
    font-size: 13px;
    color: var(--muted);
    padding: 5px 0;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: flex-start;
    gap: 8px;
  }

  .vs-side .vs-item:last-child { border-bottom: none; }
  .vs-side.orchestrated .vs-item { border-bottom-color: #fde68a; color: var(--text); }
  .vs-side .vs-item .vi-icon { flex-shrink: 0; }

  .vs-divider {
    background: var(--white);
    border-left: 1px solid var(--border);
    border-right: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 14px;
    font-weight: 700;
    font-size: 12px;
    color: var(--muted);
    font-family: 'DM Mono', monospace;
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

  /* ── Orchestrator flow ── */
  .orch-flow {
    display: flex;
    align-items: stretch;
    gap: 0;
    margin: 18px 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .of-node {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 18px 10px;
    text-align: center;
    gap: 5px;
    min-width: 0;
  }

  .of-node .ofn-icon { font-size: 26px; }

  .of-node .ofn-type {
    font-family: 'DM Mono', monospace;
    font-size: 9.5px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
  }

  .of-node .ofn-name { font-weight: 700; font-size: 13.5px; color: var(--text); }
  .of-node .ofn-sub  { font-size: 11px; color: var(--muted); line-height: 1.4; }

  .of-node.n-input   { background: #f0f9ff; }
  .of-node.n-input   .ofn-type { color: #0369a1; }

  .of-node.n-orch    { background: var(--amber-light); border: 2px solid #fde68a; }
  .of-node.n-orch    .ofn-type { color: #92400e; }
  .of-node.n-orch    .ofn-name { color: #92400e; }

  .of-node.n-agent   { background: #f0fdf4; }
  .of-node.n-agent   .ofn-type { color: #166534; }

  .of-node.n-output  { background: #fdf4ff; }
  .of-node.n-output  .ofn-type { color: #6b21a8; }

  .of-arrow {
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

  /* ── Router compare ── */
  .router-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 14px 0;
  }

  .router-side {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .router-side .rs-head {
    padding: 11px 16px;
    font-weight: 600;
    font-size: 13px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border);
  }

  .router-side.rule .rs-head { background: #f0f9ff; color: #0c4a6e; border-color: #bae6fd; }
  .router-side.llm  .rs-head { background: var(--amber-light); color: #92400e; border-color: #fde68a; }

  .router-side .rs-body {
    padding: 14px 16px;
    background: var(--white);
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .rs-item {
    display: flex;
    align-items: flex-start;
    gap: 9px;
    font-size: 12.5px;
    color: var(--text);
    line-height: 1.5;
    padding: 8px 10px;
    border-radius: 6px;
  }

  .rs-item .rsi-icon { font-size: 16px; flex-shrink: 0; margin-top: 1px; }
  .rs-item .rsi-label { font-weight: 600; font-size: 12.5px; display: block; }
  .rs-item .rsi-sub   { font-size: 12px; color: var(--muted); }

  .rule .rs-item { background: #f0f9ff; }
  .llm  .rs-item { background: var(--amber-light); }

  .rs-footer {
    padding: 10px 14px;
    border-top: 1px solid var(--border);
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.07em;
  }

  .rule .rs-footer { background: #f0f9ff; color: #0369a1; }
  .llm  .rs-footer { background: var(--amber-light); color: #92400e; }

  /* ── Pipeline problems stack ── */
  .problem-stack {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .ps-row {
    display: grid;
    grid-template-columns: 200px 1fr;
    align-items: stretch;
    border-bottom: 1px solid var(--border);
  }

  .ps-row:last-child { border-bottom: none; }

  .ps-row .psr-label {
    padding: 12px 14px;
    font-weight: 600;
    font-size: 12.5px;
    color: var(--text);
    background: var(--off-white);
    border-right: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 8px;
    line-height: 1.4;
  }

  .ps-row .psr-desc {
    padding: 12px 16px;
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.6;
    display: flex;
    align-items: center;
  }

  .ps-row .psr-desc em {
    font-style: normal;
    font-family: 'DM Mono', monospace;
    font-size: 11.5px;
    color: var(--amber-dim);
    background: var(--amber-light);
    padding: 1px 6px;
    border-radius: 3px;
    margin-left: 4px;
  }

  /* ── Decision grid ── */
  .decision-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .dg-col { padding: 18px 20px; }
  .dg-col + .dg-col { border-left: 1px solid var(--border); }
  .dg-col.pipeline     { background: var(--off-white); }
  .dg-col.orchestrator { background: #fffbeb; }

  .dg-col .dgc-label {
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

  .dg-col.pipeline     .dgc-label { color: var(--muted); }
  .dg-col.orchestrator .dgc-label { color: #92400e; }

  .dg-col .dgc-item {
    font-size: 12.5px;
    padding: 8px 0;
    border-bottom: 1px solid rgba(0,0,0,0.06);
    display: flex;
    align-items: flex-start;
    gap: 9px;
    color: var(--text);
    line-height: 1.5;
  }

  .dg-col .dgc-item:last-child { border-bottom: none; }
  .dg-col .dgc-item .di-dot { flex-shrink: 0; margin-top: 2px; }

  /* ── Traffic controller analogy ── */
  .traffic-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 14px 0;
  }

  .traffic-side {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .traffic-side .ts-head {
    padding: 10px 16px;
    font-weight: 600;
    font-size: 13px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border);
  }

  .traffic-side.real  .ts-head { background: #f0f9ff;           color: #0c4a6e; border-color: #bae6fd; }
  .traffic-side.agent .ts-head { background: var(--amber-light); color: #92400e; border-color: #fde68a; }

  .traffic-side .ts-body {
    padding: 14px 16px;
    background: var(--white);
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .ts-step {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 8px 10px;
    border-radius: 6px;
    font-size: 12.5px;
    line-height: 1.5;
  }

  .ts-step .tss-icon { font-size: 17px; flex-shrink: 0; margin-top: 2px; }
  .ts-step .tss-action { font-weight: 600; font-size: 12.5px; display: block; color: var(--text); }
  .ts-step .tss-sub    { font-size: 12px; color: var(--muted); }

  .real  .ts-step { background: #f0f9ff; }
  .agent .ts-step { background: var(--amber-light); }

  /* ── Orch anatomy box ── */
  .orch-anatomy {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin: 14px 0;
  }

  .oa-card {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .oa-card .oac-head {
    padding: 10px 14px;
    font-weight: 600;
    font-size: 12.5px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border);
  }

  .oa-card.intent .oac-head  { background: #f0f9ff;           color: #0c4a6e; border-color: #bae6fd; }
  .oa-card.select .oac-head  { background: var(--amber-light); color: #92400e; border-color: #fde68a; }
  .oa-card.handle .oac-head  { background: #f0fdf4;           color: #166534; border-color: #bbf7d0; }

  .oa-card .oac-body {
    padding: 12px 14px;
    background: var(--white);
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.6;
  }

  .oa-card .oac-example {
    margin-top: 9px;
    padding: 7px 10px;
    border-radius: 5px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    line-height: 1.5;
  }

  .oa-card.intent .oac-example { background: #e0f2fe; color: #0c4a6e; }
  .oa-card.select .oac-example { background: #fef9c3; color: #92400e; }
  .oa-card.handle .oac-example { background: #dcfce7; color: #166534; }
---

<!-- _class: cover -->

<div class="series-badge">ORCHESTRATOR + SPECIALISTS · LEVEL 3 — PART 1 OF 4</div>

# The Orchestrator Mental Model
## From fixed pipelines to intelligent routing

&nbsp;

**A pipeline always runs the same steps in the same order.** An orchestrator decides which steps to run, in what order, based on what the request actually needs.

`orchestrator` · `intent` · `routing` · `specialist` · `rule-based` · `LLM router`

---

## Pipeline vs. Orchestrated System — The Core Difference

A pipeline is a fixed sequence. An orchestrated system is a dynamic one — the same entry point, but different paths depending on what you ask.

<div class="versus-grid">
  <div class="vs-side pipeline">
    <div class="vs-label">⛓️ &nbsp;Pipeline</div>
    <div class="vs-title">Fixed sequence, every time.</div>
    <div class="vs-item"><span class="vi-icon">→</span> Input always goes through the same stages</div>
    <div class="vs-item"><span class="vi-icon">→</span> Stage order is hardcoded in the orchestrator</div>
    <div class="vs-item"><span class="vi-icon">→</span> Every request uses every agent, even if it doesn't need them</div>
    <div class="vs-item"><span class="vi-icon">→</span> Adding a new task type means adding a new pipeline</div>
    <div class="vs-item"><span class="vi-icon">→</span> Works well when the task is always the same shape</div>
  </div>
  <div class="vs-divider">vs</div>
  <div class="vs-side orchestrated">
    <div class="vs-label">🧭 &nbsp;Orchestrated system</div>
    <div class="vs-title">Dynamic routing, every time.</div>
    <div class="vs-item"><span class="vi-icon">→</span> Input is parsed for intent first</div>
    <div class="vs-item"><span class="vi-icon">→</span> The orchestrator selects which agents to call</div>
    <div class="vs-item"><span class="vi-icon">→</span> Only the relevant agents run — nothing wasted</div>
    <div class="vs-item"><span class="vi-icon">→</span> Adding a new task type means adding a new specialist</div>
    <div class="vs-item"><span class="vi-icon">→</span> Works well when requests vary in shape and scope</div>
  </div>
</div>

<div class="highlight">

**Analogy:** A pipeline is a tram — fixed route, fixed stops, everyone rides the same track. An orchestrated system is a taxi dispatcher — one entry point, different destinations, routes chosen on the fly.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Why Pipelines Break When You Have Too Many of Them

The first pipeline you build is clean. The third one shares code with the first. The sixth one is held together with special-case conditionals. This is the pipeline scaling problem.

<div class="problem-stack">
  <div class="ps-row">
    <div class="psr-label">🔀 &nbsp;Logic gets duplicated</div>
    <div class="psr-desc">Three pipelines all start with a research stage. Each one has its own copy of the research agent call. When you change the model or the system prompt, you update it in three places — and miss one.<em>→ prompt drift</em></div>
  </div>
  <div class="ps-row">
    <div class="psr-label">🌿 &nbsp;Conditionals multiply</div>
    <div class="psr-desc">The pipeline that handles blog posts gets an <code>if topic == "legal"</code> branch. Then an <code>if audience == "technical"</code> branch. Then a <code>if length > 2000</code> branch. Now it's not a pipeline — it's a decision tree wearing a pipeline's clothes.<em>→ hidden router</em></div>
  </div>
  <div class="ps-row">
    <div class="psr-label">🚪 &nbsp;Entry points multiply</div>
    <div class="psr-desc">You now have <code>run_blog_pipeline()</code>, <code>run_report_pipeline()</code>, and <code>run_summary_pipeline()</code>. The caller has to know which one to call before making the call. The routing problem just moved upstream — to your API or UI.<em>→ caller burden</em></div>
  </div>
  <div class="ps-row">
    <div class="psr-label">🧪 &nbsp;Testing surface explodes</div>
    <div class="psr-desc">Six pipelines with three conditional branches each means eighteen test paths at minimum. Add one new agent and every pipeline that touches it needs regression tests. The maintenance burden scales with the product of agents times pipelines.<em>→ combinatorial debt</em></div>
  </div>
</div>

<div class="highlight">

**The signal:** When you find yourself routing to pipelines from outside — picking which pipeline to run before running it — you've already built an orchestrator. It's just not explicit yet.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## The Traffic Controller Analogy

An orchestrator does exactly what an air traffic controller does: it doesn't fly any of the planes itself. It listens to incoming requests, understands what each one needs, and directs it to the right runway.

<div class="traffic-grid">
  <div class="traffic-side real">
    <div class="ts-head">✈️ &nbsp;Air traffic controller</div>
    <div class="ts-body">
      <div class="ts-step">
        <div class="tss-icon">📻</div>
        <div><span class="tss-action">Receive incoming flight</span><span class="tss-sub">Identifies call sign, destination, and current state — not the flight plan itself.</span></div>
      </div>
      <div class="ts-step">
        <div class="tss-icon">🗺️</div>
        <div><span class="tss-action">Assess situation</span><span class="tss-sub">Checks weather, runway availability, and other traffic. Decides which runway and sequence.</span></div>
      </div>
      <div class="ts-step">
        <div class="tss-icon">📡</div>
        <div><span class="tss-action">Issue instructions</span><span class="tss-sub">Directs the flight to runway 27L. Doesn't fly the plane — only gives the right specialist the right job.</span></div>
      </div>
      <div class="ts-step">
        <div class="tss-icon">✅</div>
        <div><span class="tss-action">Confirm and clear</span><span class="tss-sub">Receives confirmation from ground crew. Marks the flight complete. Moves to the next.</span></div>
      </div>
    </div>
  </div>
  <div class="traffic-side agent">
    <div class="ts-head">🧭 &nbsp;Orchestrator agent</div>
    <div class="ts-body">
      <div class="ts-step">
        <div class="tss-icon">💬</div>
        <div><span class="tss-action">Receive user request</span><span class="tss-sub">Reads the raw input. Parses what the user actually wants — intent, not just keywords.</span></div>
      </div>
      <div class="ts-step">
        <div class="tss-icon">🧠</div>
        <div><span class="tss-action">Classify and plan</span><span class="tss-sub">Checks what agents are available and what the request requires. Decides who to call and in what order.</span></div>
      </div>
      <div class="ts-step">
        <div class="tss-icon">⚡</div>
        <div><span class="tss-action">Dispatch to specialists</span><span class="tss-sub">Calls the right agent with the right input. Doesn't do the work itself — only coordinates.</span></div>
      </div>
      <div class="ts-step">
        <div class="tss-icon">📦</div>
        <div><span class="tss-action">Collect and return</span><span class="tss-sub">Receives the specialist's output. Validates, formats, and returns it to the caller.</span></div>
      </div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## What an Orchestrator Does — Three Responsibilities

Every orchestrator has exactly three jobs. It parses intent, selects agents, and handles their results. It does none of the specialist work itself.

<div class="orch-anatomy">
  <div class="oa-card intent">
    <div class="oac-head">🔍 &nbsp;① Intent parsing</div>
    <div class="oac-body">
      Reads the raw request and extracts <em>what the user actually wants</em> — not just the surface words. Identifies the task type, required output format, and any constraints.
      <div class="oac-example">Input: "Summarise last week's support tickets and flag urgent ones."<br><br>Intent: task=summarise, source=tickets, filter=urgent, format=report</div>
    </div>
  </div>
  <div class="oa-card select">
    <div class="oac-head">🎯 &nbsp;② Agent selection</div>
    <div class="oac-body">
      Given the parsed intent, decides which specialist agents to call, with what inputs, and in what order. May call one agent or several — sequentially or in parallel.
      <div class="oac-example">→ call ticket_reader(source="last_week")<br>→ call summarise_agent(tickets)<br>→ call triage_agent(tickets, threshold="urgent")</div>
    </div>
  </div>
  <div class="oa-card handle">
    <div class="oac-head">📦 &nbsp;③ Result handling</div>
    <div class="oac-body">
      Receives each specialist's output, validates it against the contract, assembles the final response, and returns it to the caller. Also handles failures and retries.
      <div class="oac-example">summary = validate(summarise_result)<br>flags  = validate(triage_result)<br>return merge(summary, flags)</div>
    </div>
  </div>
</div>

<div class="orch-flow">
  <div class="of-node n-input">
    <div class="ofn-icon">💬</div>
    <div class="ofn-type">Raw input</div>
    <div class="ofn-name">User request</div>
    <div class="ofn-sub">Any shape,<br>any phrasing</div>
  </div>
  <div class="of-arrow">→</div>
  <div class="of-node n-orch">
    <div class="ofn-icon">🧭</div>
    <div class="ofn-type">Orchestrator</div>
    <div class="ofn-name">Parse → Select → Handle</div>
    <div class="ofn-sub">Never does<br>specialist work</div>
  </div>
  <div class="of-arrow">→</div>
  <div class="of-node n-agent">
    <div class="ofn-icon">🤖</div>
    <div class="ofn-type">Specialist(s)</div>
    <div class="ofn-name">Experts called</div>
    <div class="ofn-sub">One job each,<br>on demand</div>
  </div>
  <div class="of-arrow">→</div>
  <div class="of-node n-output">
    <div class="ofn-icon">📤</div>
    <div class="ofn-type">Output</div>
    <div class="ofn-name">Final result</div>
    <div class="ofn-sub">Assembled and<br>returned</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03 — CONTINUED</div>

## The Orchestrator's Golden Rule

The most important constraint: **the orchestrator never does specialist work itself.** Every time it starts to, it has become a fat single agent, and you lose all the benefits of the architecture.

<div class="walkthrough">
  <div class="wt-row">
    <div class="wr-num">✓</div>
    <div class="wr-content">
      <div class="wrc-title">🧭 &nbsp;Orchestrator parses intent — correct</div>
      <div class="wrc-desc">It extracts <code>task_type="summarise"</code> and <code>source="support_tickets"</code> from the user's message, then calls the summarise specialist with those parameters. It reads the result and passes it back.</div>
      <div class="wrc-code">intent = parse_intent(user_input) → call summarise_agent(intent.params)</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">✗</div>
    <div class="wr-content">
      <div class="wrc-title">🧭 &nbsp;Orchestrator writes the summary — wrong</div>
      <div class="wrc-desc">The orchestrator's system prompt says "when the task is summarisation, read the tickets and write a summary." It has absorbed the specialist's job. Now it's a single-agent doing routing plus work — fragile, untestable, and hard to improve one part without breaking the other.</div>
      <div class="wrc-code">❌ orchestrator prompt: "…also summarise the tickets if needed"</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">✓</div>
    <div class="wr-content">
      <div class="wrc-title">🤖 &nbsp;Specialist writes the summary — correct</div>
      <div class="wrc-desc">The summarise specialist has a focused system prompt, its own context window, and returns a validated artifact. The orchestrator receives that artifact, checks it, and forwards it. Each part is independently improvable.</div>
      <div class="wrc-code">summarise_agent(tickets) → summary.json → orchestrator forwards</div>
    </div>
  </div>
</div>

<div class="highlight">

**Test:** If you removed the orchestrator and called the specialist directly, would it still work? If yes, the division is correct. If no, the orchestrator has leaked into the specialist's role.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Rule-Based Router vs. LLM Router

The intent-parsing step can be done two ways. Which one you choose determines how flexible your system is — and how much it can break.

<div class="router-compare">
  <div class="router-side rule">
    <div class="rs-head">⚙️ &nbsp;Rule-based router</div>
    <div class="rs-body">
      <div class="rs-item">
        <div class="rsi-icon">📋</div>
        <div><span class="rsi-label">How it works</span><span class="rsi-sub">Keyword matching, regex patterns, or explicit if/elif chains. "If input contains 'summarise', call summarise_agent."</span></div>
      </div>
      <div class="rs-item">
        <div class="rsi-icon">✅</div>
        <div><span class="rsi-label">Strengths</span><span class="rsi-sub">Fully deterministic. Fast. Zero extra API calls. Easy to test with unit tests. Auditable — you can read exactly what the routing logic does.</span></div>
      </div>
      <div class="rs-item">
        <div class="rsi-icon">⚠️</div>
        <div><span class="rsi-label">Weaknesses</span><span class="rsi-sub">Breaks on phrasing variation. "Sum up the tickets" and "Give me a summary of tickets" may route differently. Requires manual maintenance as task types grow.</span></div>
      </div>
    </div>
    <div class="rs-footer">Use when: inputs are predictable and controlled</div>
  </div>
  <div class="router-side llm">
    <div class="rs-head">🧠 &nbsp;LLM router</div>
    <div class="rs-body">
      <div class="rs-item">
        <div class="rsi-icon">💬</div>
        <div><span class="rsi-label">How it works</span><span class="rsi-sub">A small, fast LLM call classifies the intent. Returns a structured JSON decision: <code>{"task": "summarise", "params": {...}}</code>.</span></div>
      </div>
      <div class="rs-item">
        <div class="rsi-icon">✅</div>
        <div><span class="rsi-label">Strengths</span><span class="rsi-sub">Handles natural language variation, ambiguity, and novel phrasing. Scales to many task types without adding new code paths. Understands context and nuance.</span></div>
      </div>
      <div class="rs-item">
        <div class="rsi-icon">⚠️</div>
        <div><span class="rsi-label">Weaknesses</span><span class="rsi-sub">Adds one API call per request (use a small, fast model). Non-deterministic — the same input can route differently on different runs. Harder to test exhaustively.</span></div>
      </div>
    </div>
    <div class="rs-footer">Use when: inputs are natural language and varied</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04 — CONTINUED</div>

## Choosing a Router — The Decision Table

<table class="cheat-table">
  <thead>
    <tr><th>Situation</th><th>Use</th><th>Reason</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>Input comes from a UI dropdown or structured form</td>
      <td><strong>Rule-based</strong></td>
      <td>The input is already classified by the form. Routing is trivial — match the field value.</td>
    </tr>
    <tr>
      <td>Input is a free-text chat message from a user</td>
      <td><strong>LLM router</strong></td>
      <td>Natural language varies too much for reliable keyword matching. Let the model classify.</td>
    </tr>
    <tr>
      <td>You have 3–5 task types with very distinct keywords</td>
      <td><strong>Rule-based</strong></td>
      <td>Small, explicit rule sets are fast, auditable, and easy to maintain at this scale.</td>
    </tr>
    <tr>
      <td>You have 10+ task types with overlapping vocabulary</td>
      <td><strong>LLM router</strong></td>
      <td>Rule sets at this scale become unmaintainable. Let the model handle nuance.</td>
    </tr>
    <tr>
      <td>Every misroute is a hard failure (medical, financial, legal)</td>
      <td><strong>Rule-based + human fallback</strong></td>
      <td>LLM routing introduces non-determinism. High-stakes paths need explicit, auditable logic.</td>
    </tr>
    <tr>
      <td>You're prototyping and task types aren't fully defined yet</td>
      <td><strong>LLM router</strong></td>
      <td>Flexible enough to handle undefined cases. Refine into rules later when patterns emerge.</td>
    </tr>
  </tbody>
</table>

<div class="highlight">

**Practical default:** Start with a rule-based router. When phrasing variations start causing misroutes — or you exceed five task types — migrate the routing step to an LLM call. The specialists don't change; only the router does.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## When You Need an Orchestrator vs. When a Pipeline Is Enough

The upgrade from pipeline to orchestrator is a specific decision, not an aspiration. These are the concrete triggers.

<div class="decision-grid">
  <div class="dg-col pipeline">
    <div class="dgc-label">⛓️ &nbsp;Stay with a pipeline when…</div>
    <div class="dgc-item"><span class="di-dot">→</span> Every request always needs the same agents in the same order</div>
    <div class="dgc-item"><span class="di-dot">→</span> There is one task type and one output shape</div>
    <div class="dgc-item"><span class="di-dot">→</span> The caller already knows which pipeline to invoke</div>
    <div class="dgc-item"><span class="di-dot">→</span> You have one pipeline and no plans to add a second</div>
    <div class="dgc-item"><span class="di-dot">→</span> Input is always structured (a form, an API payload)</div>
    <div class="dgc-item"><span class="di-dot">→</span> Routing logic would be a single if/else</div>
  </div>
  <div class="dg-col orchestrator">
    <div class="dgc-label">🧭 &nbsp;Add an orchestrator when…</div>
    <div class="dgc-item"><span class="di-dot">→</span> Different requests need different subsets of agents</div>
    <div class="dgc-item"><span class="di-dot">→</span> You have two or more pipelines sharing agents</div>
    <div class="dgc-item"><span class="di-dot">→</span> The caller doesn't know (or shouldn't care) which pipeline to call</div>
    <div class="dgc-item"><span class="di-dot">→</span> You're adding <code>if/elif</code> branches inside a pipeline to handle variation</div>
    <div class="dgc-item"><span class="di-dot">→</span> Input is free-text and task type must be inferred</div>
    <div class="dgc-item"><span class="di-dot">→</span> You want a single entry point for multiple task types</div>
  </div>
</div>

<div class="highlight">

**The clearest signal:** You're writing routing logic outside of your agents — in a controller, an API handler, or a UI — to decide which pipeline to call. That logic <em>is</em> the orchestrator. Make it explicit, give it its own agent, and give your specialists clean interfaces.

</div>

---

## Quick Reference — Orchestrator Vocabulary

The terms that appear in every Level 3 tutorial, decoded.

<table class="cheat-table">
  <thead>
    <tr><th>Term</th><th>What it means</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="mono">Orchestrator</span></td>
      <td>The agent (or code) that parses intent, selects specialists, and assembles results. Never does specialist work itself.</td>
    </tr>
    <tr>
      <td><span class="mono">Intent parsing</span></td>
      <td>The step where raw user input is converted into a structured decision: what task, which agents, what parameters.</td>
    </tr>
    <tr>
      <td><span class="mono">Rule-based router</span></td>
      <td>Intent classification via keywords, regex, or explicit conditions. Deterministic, fast, and brittle to phrasing variation.</td>
    </tr>
    <tr>
      <td><span class="mono">LLM router</span></td>
      <td>Intent classification via a small, fast LLM call that returns a structured routing decision. Flexible but non-deterministic.</td>
    </tr>
    <tr>
      <td><span class="mono">Specialist agent</span></td>
      <td>An agent with one job, called by the orchestrator on demand. Unchanged from Level 2 — the interface is what's new.</td>
    </tr>
    <tr>
      <td><span class="mono">Agent selection</span></td>
      <td>The orchestrator's decision of which specialist(s) to call for a given intent. The core of what makes a system dynamic.</td>
    </tr>
    <tr>
      <td><span class="mono">Entry point</span></td>
      <td>The single function or endpoint a caller uses to interact with the system. The orchestrator owns this — not individual specialists.</td>
    </tr>
  </tbody>
</table>

---

<!-- _class: final -->

# The orchestrator doesn't do the work. It knows who does.

&nbsp;

*Parse the intent. Pick the specialist. Handle the result. Nothing more.*

&nbsp;

Next: **Part 2 — Building the LLM Router.**

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*