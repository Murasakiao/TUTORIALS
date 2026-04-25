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
  .code-block .cb-body .hl  { background: rgba(217,119,6,0.15); display: inline-block; width: 100%; border-radius: 3px; }

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
    font-size: 12.5px;
    line-height: 2;
    color: #d6d3d1;
    white-space: pre;
  }

  .file-tree .ft-body .fd  { color: #fbbf24; }
  .file-tree .ft-body .fp  { color: #86efac; }
  .file-tree .ft-body .fj  { color: #67e8f9; }
  .file-tree .ft-body .fm  { color: #c4b5fd; }
  .file-tree .ft-body .fc  { color: #57534e; }
  .file-tree .ft-body .fk  { color: #f97316; }

  /* ── Log block ── */
  .log-block {
    background: #0f172a;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid #1e293b;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
  }

  .log-block .lb-header {
    background: #1e293b;
    padding: 8px 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid #334155;
  }

  .log-block .lb-header .lb-title {
    font-size: 11px;
    color: #94a3b8;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }

  .log-block .lb-header .lb-badge {
    font-size: 10px;
    background: #0f172a;
    color: #64748b;
    padding: 2px 8px;
    border-radius: 3px;
  }

  .log-block .lb-body {
    padding: 14px 18px;
    font-size: 11.5px;
    line-height: 1.9;
    white-space: pre;
  }

  .log-block .lg-ts   { color: #475569; }
  .log-block .lg-ok   { color: #4ade80; font-weight: 600; }
  .log-block .lg-warn { color: #fbbf24; font-weight: 600; }
  .log-block .lg-err  { color: #f87171; font-weight: 600; }
  .log-block .lg-info { color: #94a3b8; }
  .log-block .lg-key  { color: #7dd3fc; }
  .log-block .lg-val  { color: #86efac; }
  .log-block .lg-dim  { color: #334155; }

  /* ── Walkthrough ── */
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

  /* ── Compare grid ── */
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
  .cg-card.rule .cg-head { background: #f0f9ff; color: #0c4a6e; border-color: #bae6fd; }
  .cg-card.llm  .cg-head { background: var(--amber-light); color: #92400e; border-color: #fde68a; }

  .cg-card .cg-body {
    padding: 12px 14px;
    font-size: 12.5px;
    color: var(--muted);
    background: var(--white);
    line-height: 1.65;
  }

  .cg-card.good .cg-body { color: var(--text); }

  /* ── Failure mode cards ── */
  .failure-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 14px 0;
  }

  .failure-card {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid #fecaca;
  }

  .failure-card .fc-head {
    padding: 9px 14px;
    background: #fef2f2;
    border-bottom: 1px solid #fecaca;
    font-weight: 600;
    font-size: 12.5px;
    color: #991b1b;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .failure-card .fc-body {
    padding: 11px 14px;
    background: var(--white);
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.6;
  }

  .failure-card .fc-fix {
    margin-top: 9px;
    padding: 7px 10px;
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-radius: 5px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #166534;
    line-height: 1.5;
  }

  .failure-card .fc-fix::before {
    content: '✓ fix: ';
    font-weight: 700;
  }

  /* ── Test isolation strip ── */
  .test-strip {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .ts-row {
    display: grid;
    grid-template-columns: 160px 1fr auto;
    align-items: stretch;
    border-bottom: 1px solid var(--border);
  }

  .ts-row:last-child { border-bottom: none; }

  .ts-row .tsr-stage {
    padding: 11px 13px;
    font-weight: 600;
    font-size: 12.5px;
    color: var(--text);
    background: var(--off-white);
    border-right: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 7px;
    line-height: 1.4;
  }

  .ts-row .tsr-test {
    padding: 11px 14px;
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.6;
    display: flex;
    align-items: center;
  }

  .ts-row .tsr-verdict {
    padding: 11px 13px;
    border-left: 1px solid var(--border);
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    display: flex;
    align-items: center;
    white-space: nowrap;
  }

  .ts-row.unit     .tsr-verdict { background: #f0fdf4; color: #166534; }
  .ts-row.contract .tsr-verdict { background: #f0f9ff; color: #0369a1; }
  .ts-row.route    .tsr-verdict { background: var(--amber-light); color: #92400e; }
  .ts-row.e2e      .tsr-verdict { background: #fdf4ff; color: #6b21a8; }

  /* ── CTA cards ── */
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

  .cta-card .ctac-steps {
    margin-top: 10px;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  .cta-card .ctac-step {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    color: #d97706;
    background: rgba(217,119,6,0.10);
    border: 1px solid rgba(217,119,6,0.20);
    border-radius: 3px;
    padding: 3px 8px;
  }
---

<!-- _class: cover -->

<div class="series-badge">ORCHESTRATOR + SPECIALISTS · LEVEL 3 — PART 4 OF 4</div>

# Building and Testing the System
## Structure, routing code, logging, isolation testing, and failure modes

&nbsp;

**Designing the system is half the work.** Building it so it's testable, traceable, and recoverable when things go wrong — that's what makes it production-ready.

`project structure` · `routing code` · `logging` · `isolation testing` · `failure modes`

---

## What This Part Covers

Parts 1–3 covered mental models and design. Part 4 is the engineering — the decisions you make when you open a text editor for the first time.

<div class="matters-grid">
  <div class="matters-card">
    <div class="mcc-icon">🗂️</div>
    <div>
      <div class="mcc-title">Project structure</div>
      <div class="mcc-desc">Where every file lives before you write a single line of agent code. The folder layout determines what can import what — get it wrong and you're refactoring before the system even runs.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">⚙️</div>
    <div>
      <div class="mcc-title">Routing in code</div>
      <div class="mcc-desc">LLM routing and rule-based routing look different in Python. Knowing exactly how to implement each — and where the code lives — removes the ambiguity that slows teams down at this step.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">📋</div>
    <div>
      <div class="mcc-title">Logging orchestrator decisions</div>
      <div class="mcc-desc">Every routing decision, every specialist call, every result — logged with a timestamp and a run ID. Without this, debugging a misrouted request means guessing what happened. With it, you read the log.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🧪</div>
    <div>
      <div class="mcc-title">Testing before connecting</div>
      <div class="mcc-desc">Every specialist is tested in isolation — with a fixed input, a known good output — before it's wired into the orchestrator. A specialist that passes isolation tests and fails in the system has a contract problem, not a logic problem.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Project Structure for an Orchestrator + Specialists

The folder layout encodes the architecture. Each layer of the system gets its own directory. Nothing imports sideways — specialists never import from each other, only from `contracts.py`.

<div class="file-tree">
  <div class="ft-header">📁 &nbsp;orchestrator-project/</div>
  <div class="ft-body"><span class="fd">orchestrator-project/</span>
│
├── <span class="fd">orchestrator/</span>
│   ├── <span class="fp">runner.py</span>          <span class="fc"># entry point: run(user_input) → response</span>
│   ├── <span class="fp">router.py</span>          <span class="fc"># parse_intent() + dispatch() + PIPELINE_REGISTRY</span>
│   ├── <span class="fp">state.py</span>           <span class="fc"># RunState dataclass + save/load helpers</span>
│   └── <span class="fp">result_handler.py</span>  <span class="fc"># handle_specialist_response() logic</span>
│
├── <span class="fd">specialists/</span>
│   ├── <span class="fp">research.py</span>        <span class="fc"># run_research_specialist(**params) → SpecialistResponse</span>
│   ├── <span class="fp">writer.py</span>          <span class="fc"># run_writer_specialist(**params)   → SpecialistResponse</span>
│   ├── <span class="fp">data_analyst.py</span>    <span class="fc"># run_analyst_specialist(**params)  → SpecialistResponse</span>
│   └── <span class="fp">qa.py</span>              <span class="fc"># run_qa_specialist(**params)       → SpecialistResponse</span>
│
├── <span class="fd">prompts/</span>
│   ├── <span class="fm">orchestrator.txt</span>   <span class="fc"># routing system prompt</span>
│   └── <span class="fm">specialists/</span>       <span class="fc"># one .txt per specialist</span>
│
├── <span class="fd">runs/</span>              <span class="fc"># persisted RunState JSON, one file per run</span>
├── <span class="fp">contracts.py</span>       <span class="fc"># SpecialistResponse, RoutingDecision, all Pydantic models</span>
├── <span class="fp">logger.py</span>          <span class="fc"># structured logging helpers used by every layer</span>
└── <span class="fj">config.json</span>        <span class="fc"># model names, temperature, max_tokens per role</span></div>
</div>

<div class="highlight">

**One rule governs every import:** specialists import from <code>contracts.py</code> and <code>prompts/</code> only. They never import from <code>orchestrator/</code>. The orchestrator imports from <code>specialists/</code> and <code>contracts.py</code>. The dependency arrow points one way — down.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## LLM Routing vs. If/Else Routing in Code

Both routing strategies live in the same file — `router.py` — but they look completely different. Here is the canonical implementation of each.

<div class="compare-grid">
  <div class="cg-card rule">
    <div class="cg-head">⚙️ &nbsp;Rule-based routing — if/elif chain</div>
    <div class="cg-body">
      Fast, deterministic, zero API cost. Right for structured inputs with a small, stable set of task types.
    </div>
  </div>
  <div class="cg-card llm">
    <div class="cg-head">🧠 &nbsp;LLM routing — one API call</div>
    <div class="cg-body">
      Flexible, handles variation and ambiguity. Right for free-text inputs with many or evolving task types.
    </div>
  </div>
</div>

<div class="code-block">
  <div class="cb-header">
    <div class="cb-dots">
      <div class="cb-dot red"></div>
      <div class="cb-dot yellow"></div>
      <div class="cb-dot green"></div>
    </div>
    <div class="cb-filename">orchestrator/router.py — both strategies, same interface</div>
  </div>
  <div class="cb-body"><span class="cm"># ── Strategy A: rule-based ─────────────────────────────────────</span>
<span class="kw">def</span> <span class="fn">parse_intent_rules</span>(<span class="va">user_input</span>: <span class="va">str</span>) -> <span class="va">RoutingDecision</span>:
    <span class="va">text</span> = <span class="va">user_input</span>.<span class="bi">lower</span>()
    <span class="kw">if</span>   <span class="bi">any</span>(<span class="va">k</span> <span class="kw">in</span> <span class="va">text</span> <span class="kw">for</span> <span class="va">k</span> <span class="kw">in</span> [<span class="st">"research"</span>, <span class="st">"find"</span>, <span class="st">"sources"</span>]):
        <span class="kw">return</span> <span class="va">RoutingDecision</span>(<span class="va">pipeline</span>=<span class="st">"research_pipeline"</span>, <span class="va">confidence</span>=<span class="st">"HIGH"</span>)
    <span class="kw">elif</span> <span class="bi">any</span>(<span class="va">k</span> <span class="kw">in</span> <span class="va">text</span> <span class="kw">for</span> <span class="va">k</span> <span class="kw">in</span> [<span class="st">"write"</span>, <span class="st">"draft"</span>, <span class="st">"blog"</span>]):
        <span class="kw">return</span> <span class="va">RoutingDecision</span>(<span class="va">pipeline</span>=<span class="st">"content_pipeline"</span>, <span class="va">confidence</span>=<span class="st">"HIGH"</span>)
    <span class="kw">elif</span> <span class="bi">any</span>(<span class="va">k</span> <span class="kw">in</span> <span class="va">text</span> <span class="kw">for</span> <span class="va">k</span> <span class="kw">in</span> [<span class="st">"data"</span>, <span class="st">"csv"</span>, <span class="st">"analyse"</span>]):
        <span class="kw">return</span> <span class="va">RoutingDecision</span>(<span class="va">pipeline</span>=<span class="st">"data_pipeline"</span>, <span class="va">confidence</span>=<span class="st">"HIGH"</span>)
    <span class="kw">return</span> <span class="va">RoutingDecision</span>(<span class="va">pipeline</span>=<span class="st">"unknown"</span>, <span class="va">confidence</span>=<span class="st">"LOW"</span>)

<span class="cm"># ── Strategy B: LLM routing ────────────────────────────────────</span>
<span class="kw">def</span> <span class="fn">parse_intent_llm</span>(<span class="va">user_input</span>: <span class="va">str</span>) -> <span class="va">RoutingDecision</span>:
    <span class="va">raw</span> = <span class="va">client</span>.<span class="va">messages</span>.<span class="fn">create</span>(
        <span class="va">model</span>=<span class="st">"claude-haiku-4-5-20251001"</span>,   <span class="cm"># smallest, fastest model</span>
        <span class="va">max_tokens</span>=<span class="nu">256</span>,
        <span class="va">system</span>=<span class="fn">load_prompt</span>(<span class="st">"prompts/orchestrator.txt"</span>),
        <span class="va">messages</span>=[{<span class="st">"role"</span>: <span class="st">"user"</span>, <span class="st">"content"</span>: <span class="va">user_input</span>}]
    ).<span class="va">content</span>[<span class="nu">0</span>].<span class="va">text</span>
    <span class="kw">return</span> <span class="fn">validate_routing</span>(<span class="va">json</span>.<span class="fn">loads</span>(<span class="va">raw</span>.<span class="bi">strip</span>()))</div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02 — CONTINUED</div>

## Combining Both Strategies — The Hybrid Router

Start with rules for known patterns. Fall through to LLM only when rules don't match. This gives you speed and cost savings for common cases, flexibility for edge cases — and a log entry telling you which path fired.

<div class="code-block">
  <div class="cb-header">
    <div class="cb-dots">
      <div class="cb-dot red"></div>
      <div class="cb-dot yellow"></div>
      <div class="cb-dot green"></div>
    </div>
    <div class="cb-filename">orchestrator/router.py — hybrid parse_intent()</div>
  </div>
  <div class="cb-body"><span class="kw">def</span> <span class="fn">parse_intent</span>(<span class="va">user_input</span>: <span class="va">str</span>) -> <span class="va">RoutingDecision</span>:
    <span class="cm"># ── 1. Try rules first — zero API cost ─────────────────</span>
    <span class="va">rule_result</span> = <span class="fn">parse_intent_rules</span>(<span class="va">user_input</span>)

    <span class="kw">if</span> <span class="va">rule_result</span>.<span class="va">confidence</span> == <span class="st">"HIGH"</span>:
        <span class="fn">log_routing</span>(<span class="st">"rule"</span>, <span class="va">rule_result</span>)
        <span class="kw">return</span> <span class="va">rule_result</span>            <span class="cm"># matched — no LLM call needed</span>

    <span class="cm"># ── 2. Rules uncertain — fall through to LLM ───────────</span>
    <span class="fn">log_routing</span>(<span class="st">"llm_fallback"</span>, <span class="va">rule_result</span>)
    <span class="va">llm_result</span> = <span class="fn">parse_intent_llm</span>(<span class="va">user_input</span>)
    <span class="fn">log_routing</span>(<span class="st">"llm"</span>, <span class="va">llm_result</span>)
    <span class="kw">return</span> <span class="va">llm_result</span></div>
</div>

<div class="matters-grid" style="margin-top: 0;">
  <div class="matters-card">
    <div class="mcc-icon">⚡</div>
    <div>
      <div class="mcc-title">Rules handle the majority of requests</div>
      <div class="mcc-desc">In most systems, 70–80% of requests match predictable patterns. Rule matching costs nothing. Only the long tail — ambiguous or novel phrasings — ever reaches the LLM router.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">📋</div>
    <div>
      <div class="mcc-title">Log which strategy fired, every time</div>
      <div class="mcc-desc">The <code>log_routing()</code> call records whether the decision came from rules or LLM. Over time, this tells you which patterns are worth promoting to rules — and whether your rule set is decaying as inputs evolve.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Logging Orchestrator Decisions for Traceability

Every decision the orchestrator makes must leave a log entry. Routing decisions, specialist calls, results, errors, and timing — all timestamped, all keyed to a run ID. Without this, debugging is reconstruction. With it, debugging is reading.

<div class="log-block">
  <div class="lb-header">
    <div class="lb-title">orchestrator run log</div>
    <div class="lb-badge">runs/run_20250422_017.log</div>
  </div>
  <div class="lb-body"><span class="lg-ts">03:41:02</span> <span class="lg-ok">[START]</span>   <span class="lg-key">run_id=</span><span class="lg-val">run_20250422_017</span>  <span class="lg-key">input=</span><span class="lg-val">"research our top 5 competitors..."</span>
<span class="lg-ts">03:41:02</span> <span class="lg-info">[ROUTE]</span>   <span class="lg-key">strategy=</span><span class="lg-val">rule</span>  <span class="lg-key">pipeline=</span><span class="lg-val">research_pipeline</span>  <span class="lg-key">confidence=</span><span class="lg-val">HIGH</span>
<span class="lg-ts">03:41:02</span> <span class="lg-info">[CALL]</span>    <span class="lg-key">specialist=</span><span class="lg-val">research</span>  <span class="lg-key">params=</span><span class="lg-val">{topic, audience, depth}</span>
<span class="lg-ts">03:41:06</span> <span class="lg-ok">[RESULT]</span>  <span class="lg-key">specialist=</span><span class="lg-val">research</span>  <span class="lg-key">status=</span><span class="lg-val">ok</span>  <span class="lg-key">duration=</span><span class="lg-val">4.1s</span>  <span class="lg-key">tokens=</span><span class="lg-val">1842</span>
<span class="lg-ts">03:41:06</span> <span class="lg-info">[SAVE]</span>    <span class="lg-key">artifact=</span><span class="lg-val">runs/run_20250422_017/research.json</span>
<span class="lg-ts">03:41:06</span> <span class="lg-info">[CALL]</span>    <span class="lg-key">specialist=</span><span class="lg-val">writer</span>  <span class="lg-key">params=</span><span class="lg-val">{outline, research}</span>
<span class="lg-ts">03:41:09</span> <span class="lg-warn">[WARN]</span>    <span class="lg-key">specialist=</span><span class="lg-val">writer</span>  <span class="lg-key">attempt=</span><span class="lg-val">1</span>  <span class="lg-key">error=</span><span class="lg-val">ValidationError: missing field 'tone'</span>
<span class="lg-ts">03:41:09</span> <span class="lg-warn">[RETRY]</span>   <span class="lg-key">specialist=</span><span class="lg-val">writer</span>  <span class="lg-key">attempt=</span><span class="lg-val">2</span>  <span class="lg-key">using_stricter_prompt=</span><span class="lg-val">true</span>
<span class="lg-ts">03:41:13</span> <span class="lg-ok">[RESULT]</span>  <span class="lg-key">specialist=</span><span class="lg-val">writer</span>  <span class="lg-key">status=</span><span class="lg-val">ok</span>  <span class="lg-key">duration=</span><span class="lg-val">6.8s</span>  <span class="lg-key">tokens=</span><span class="lg-val">3201</span>
<span class="lg-ts">03:41:13</span> <span class="lg-ok">[DONE]</span>    <span class="lg-key">run_id=</span><span class="lg-val">run_20250422_017</span>  <span class="lg-key">total_duration=</span><span class="lg-val">11.2s</span>  <span class="lg-key">total_tokens=</span><span class="lg-val">5043</span></div>
</div>

<div class="highlight">

**Every log line has a run ID.** When a user reports a wrong result, you search for their run ID — not for "errors" in the last hour. All lines for that run group together. You read them in order and find exactly where the system diverged from the expected path.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03 — CONTINUED</div>

## What to Log at Each Layer

<table class="cheat-table">
  <thead>
    <tr><th>Layer</th><th>Log event</th><th>Fields required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Run start</strong></td>
      <td><span class="mono">[START]</span></td>
      <td><span class="mono">run_id</span>, <span class="mono">timestamp</span>, <span class="mono">input</span> (truncated to 200 chars)</td>
    </tr>
    <tr>
      <td><strong>Routing decision</strong></td>
      <td><span class="mono">[ROUTE]</span></td>
      <td><span class="mono">strategy</span> (rule/llm), <span class="mono">pipeline</span>, <span class="mono">confidence</span>, <span class="mono">task</span></td>
    </tr>
    <tr>
      <td><strong>Specialist call</strong></td>
      <td><span class="mono">[CALL]</span></td>
      <td><span class="mono">specialist</span>, <span class="mono">params</span> (keys only — no values that may contain PII)</td>
    </tr>
    <tr>
      <td><strong>Specialist result</strong></td>
      <td><span class="mono">[RESULT]</span></td>
      <td><span class="mono">specialist</span>, <span class="mono">status</span>, <span class="mono">duration_ms</span>, <span class="mono">tokens_used</span></td>
    </tr>
    <tr>
      <td><strong>Artifact saved</strong></td>
      <td><span class="mono">[SAVE]</span></td>
      <td><span class="mono">artifact</span> (full file path)</td>
    </tr>
    <tr>
      <td><strong>Error / retry</strong></td>
      <td><span class="mono">[WARN]</span> / <span class="mono">[RETRY]</span></td>
      <td><span class="mono">specialist</span>, <span class="mono">attempt</span>, <span class="mono">error</span> (full message)</td>
    </tr>
    <tr>
      <td><strong>Run complete or halted</strong></td>
      <td><span class="mono">[DONE]</span> / <span class="mono">[HALT]</span></td>
      <td><span class="mono">run_id</span>, <span class="mono">total_duration</span>, <span class="mono">total_tokens</span>, <span class="mono">last_good_artifact</span></td>
    </tr>
  </tbody>
</table>

<div class="highlight">

**Log param keys, not values.** You want to know the Research specialist received <code>topic</code>, <code>audience</code>, and <code>depth</code> — not what those values were, in case they contain user data. Log <code>params=keys:[topic, audience, depth]</code>, never <code>params={topic: "competitor analysis", ...}</code>.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Testing Each Specialist in Isolation Before Connecting

The integration test is not the first test. Every specialist gets a unit test and a contract test before the orchestrator ever calls it. If a specialist fails inside the orchestrator, you need to know whether the failure is in the specialist or in the handoff.

<div class="test-strip">
  <div class="ts-row unit">
    <div class="tsr-stage">🧪 Unit test</div>
    <div class="tsr-test">Call the specialist with a known good input. Assert the response envelope has <code>status="ok"</code> and the payload matches the expected shape. No orchestrator involved.</div>
    <div class="tsr-verdict">isolated pass</div>
  </div>
  <div class="ts-row contract">
    <div class="tsr-stage">📐 Contract test</div>
    <div class="tsr-test">Call the specialist with a deliberately malformed input — missing required field, wrong type, empty string. Assert it returns <code>status="error"</code> and a readable error message. Never raises.</div>
    <div class="tsr-verdict">error envelope</div>
  </div>
  <div class="ts-row route">
    <div class="tsr-stage">🧭 Routing test</div>
    <div class="tsr-test">Feed 10–20 representative inputs through <code>parse_intent()</code> only. Assert each one routes to the correct pipeline. No specialist is called — just the routing decision is checked.</div>
    <div class="tsr-verdict">routing only</div>
  </div>
  <div class="ts-row e2e">
    <div class="tsr-stage">🔗 Integration test</div>
    <div class="tsr-test">Only now run the full orchestrator with a real input. If this fails and all isolation tests pass, the failure is in the handoff — the state passing or context scoping between orchestrator and specialist.</div>
    <div class="tsr-verdict">last step</div>
  </div>
</div>

<div class="highlight">

**The test order is the diagnostic hierarchy.** Unit fails → fix the specialist. Contract fails → fix input validation. Routing fails → fix <code>parse_intent()</code>. Integration fails (all others pass) → fix the handoff in <code>orchestrator/router.py</code>.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04 — CONTINUED</div>

## The Isolation Test Pattern in Code

<div class="code-block">
  <div class="cb-header">
    <div class="cb-dots">
      <div class="cb-dot red"></div>
      <div class="cb-dot yellow"></div>
      <div class="cb-dot green"></div>
    </div>
    <div class="cb-filename">tests/test_research_specialist.py</div>
  </div>
  <div class="cb-body"><span class="kw">from</span> <span class="va">specialists.research</span> <span class="kw">import</span> <span class="fn">run_research_specialist</span>
<span class="kw">from</span> <span class="va">contracts</span>             <span class="kw">import</span> <span class="va">SpecialistResponse</span>

<span class="cm"># ── Unit test: happy path ───────────────────────────────────</span>
<span class="kw">def</span> <span class="fn">test_research_returns_ok_envelope</span>():
    <span class="va">result</span> = <span class="fn">run_research_specialist</span>(
        <span class="va">topic</span>=<span class="st">"competitor pricing"</span>,
        <span class="va">audience</span>=<span class="st">"product team"</span>,
        <span class="va">depth</span>=<span class="st">"quick"</span>
    )
    <span class="kw">assert</span> <span class="bi">isinstance</span>(<span class="va">result</span>, <span class="va">SpecialistResponse</span>)
    <span class="kw">assert</span> <span class="va">result</span>.<span class="va">status</span> == <span class="st">"ok"</span>
    <span class="kw">assert</span> <span class="va">result</span>.<span class="va">payload</span> <span class="kw">is not</span> <span class="nu">None</span>
    <span class="kw">assert</span> <span class="bi">len</span>(<span class="va">result</span>.<span class="va">payload</span>.<span class="va">claims</span>) > <span class="nu">0</span>

<span class="cm"># ── Contract test: malformed input ─────────────────────────</span>
<span class="kw">def</span> <span class="fn">test_research_handles_missing_field</span>():
    <span class="va">result</span> = <span class="fn">run_research_specialist</span>(<span class="va">topic</span>=<span class="st">"pricing"</span>)   <span class="cm"># missing audience</span>
    <span class="kw">assert</span> <span class="va">result</span>.<span class="va">status</span> == <span class="st">"error"</span>
    <span class="kw">assert</span> <span class="st">"audience"</span> <span class="kw">in</span> <span class="va">result</span>.<span class="va">error</span>   <span class="cm"># error names the missing field</span>
    <span class="kw">assert</span> <span class="va">result</span>.<span class="va">payload</span> <span class="kw">is</span> <span class="nu">None</span>       <span class="cm"># no payload on error — ever</span></div>
</div>

<div class="matters-grid" style="margin-top: 0;">
  <div class="matters-card">
    <div class="mcc-icon">🔬</div>
    <div>
      <div class="mcc-title">No mocking in isolation tests</div>
      <div class="mcc-desc">Call the real specialist with real API calls. Mocking the LLM in unit tests hides the most common failure — the model returning a slightly different shape than the contract expects. Real calls find real problems.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">📌</div>
    <div>
      <div class="mcc-title">Pin your test inputs to a fixture file</div>
      <div class="mcc-desc">Save the exact input you used in testing to <code>tests/fixtures/research_input.json</code>. When the specialist starts failing weeks later, you replay the exact same input — not a slightly different one that might mask the real regression.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## Common Failure Modes — Wrong Routing, Lost Context, Runaway Loops

Three failure modes account for most production issues in orchestrated systems. Each one has a distinct symptom, a root cause, and a fix that doesn't require rewriting the whole system.

<div class="failure-grid">
  <div class="failure-card">
    <div class="fc-head">🔀 &nbsp;Wrong routing</div>
    <div class="fc-body">A request routes to the wrong pipeline. The specialist runs successfully, the result looks plausible, but it's the wrong kind of output. The hardest failure to catch — it doesn't crash.
      <div class="fc-fix">Log which strategy fired and which pipeline was selected on every call. Add routing test cases for phrasings that have misrouted before. For LLM routing, log the raw JSON decision before validating it.</div>
    </div>
  </div>
  <div class="failure-card">
    <div class="fc-head">💨 &nbsp;Lost context</div>
    <div class="fc-body">A specialist receives params that look correct but are missing a key piece of context — the user's original intent, a constraint from the routing decision, a prior artifact that should have been forwarded. Output is plausible but incomplete.
      <div class="fc-fix">Scope each specialist call explicitly using a <code>prepare_params()</code> function. Never pass the full RunState. Write a test that asserts every required field is present in the params before the specialist is called.</div>
    </div>
  </div>
  <div class="failure-card">
    <div class="fc-head">🔁 &nbsp;Runaway routing loop</div>
    <div class="fc-body">The orchestrator routes to a specialist. The specialist returns <code>needs_clarification</code>. The orchestrator re-routes with the clarification. The specialist returns <code>needs_clarification</code> again. The loop never terminates — burning tokens on every turn.
      <div class="fc-fix">Set a <code>max_clarification_turns</code> counter per run (default: 2). If exceeded, halt and surface a <code>no_route</code> error. Never let a clarification response re-enter the routing loop more than twice.</div>
    </div>
  </div>
  <div class="failure-card">
    <div class="fc-head">🌀 &nbsp;Registry / prompt mismatch</div>
    <div class="fc-body">A pipeline was added to the registry but the orchestrator's system prompt wasn't updated — or vice versa. The LLM routes to a name it knows from the prompt, but dispatch raises <code>KeyError</code> because the registry entry was removed.
      <div class="fc-fix">Add a startup assertion: <code>assert set(PROMPT_PIPELINES) == set(PIPELINE_REGISTRY)</code>. Run this check at import time so the mismatch is caught on startup, not mid-request.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05 — CONTINUED</div>

## Preventing Runaway Loops — The Guard in Code

<div class="code-block">
  <div class="cb-header">
    <div class="cb-dots">
      <div class="cb-dot red"></div>
      <div class="cb-dot yellow"></div>
      <div class="cb-dot green"></div>
    </div>
    <div class="cb-filename">orchestrator/runner.py — loop guard</div>
  </div>
  <div class="cb-body"><span class="va">MAX_CLARIFICATION_TURNS</span> = <span class="nu">2</span>
<span class="va">MAX_SPECIALIST_RETRIES</span>  = <span class="nu">3</span>

<span class="kw">def</span> <span class="fn">run</span>(<span class="va">user_input</span>: <span class="va">str</span>) -> <span class="va">dict</span>:
    <span class="va">state</span>       = <span class="fn">RunState</span>.<span class="fn">new</span>(<span class="va">user_input</span>)
    <span class="va">clarify_ct</span>  = <span class="nu">0</span>
    <span class="va">current_input</span> = <span class="va">user_input</span>

    <span class="kw">while</span> <span class="nu">True</span>:
        <span class="va">decision</span> = <span class="fn">parse_intent</span>(<span class="va">current_input</span>)

        <span class="kw">if</span> <span class="va">decision</span>.<span class="va">pipeline</span> == <span class="st">"unknown"</span>:
            <span class="kw">return</span> {<span class="st">"status"</span>: <span class="st">"no_route"</span>}      <span class="cm"># can't route — stop immediately</span>

        <span class="va">response</span> = <span class="fn">dispatch</span>(<span class="va">decision</span>, <span class="va">state</span>)

        <span class="kw">if</span> <span class="va">response</span>[<span class="st">"status"</span>] == <span class="st">"needs_clarification"</span>:
            <span class="va">clarify_ct</span> += <span class="nu">1</span>
            <span class="kw">if</span> <span class="va">clarify_ct</span> > <span class="va">MAX_CLARIFICATION_TURNS</span>:
                <span class="kw">return</span> {<span class="st">"status"</span>: <span class="st">"no_route"</span>, <span class="st">"reason"</span>: <span class="st">"clarification_limit_reached"</span>}
            <span class="va">current_input</span> = <span class="fn">ask_clarification</span>(<span class="va">response</span>[<span class="st">"question"</span>])
            <span class="kw">continue</span>                            <span class="cm"># re-enter loop with clarified input</span>

        <span class="kw">return</span> <span class="va">response</span>                         <span class="cm"># ok, flagged, or error — stop</span></div>
</div>

<div class="highlight">

**Every loop needs a ceiling.** <code>MAX_CLARIFICATION_TURNS</code> and <code>MAX_SPECIALIST_RETRIES</code> are not optional. Define them as named constants — never as inline magic numbers — so the ceiling is visible and adjustable without touching the loop logic.

</div>

---

<!-- _class: cta -->

## Your Assignment — Build a Router for Pipelines You Already Have

You've finished Level 3. The gap between understanding and building closes with one concrete task.

<div class="cta-task-grid">
  <div class="cta-card">
    <div class="ctac-icon">🗺️</div>
    <div class="ctac-title">Step 1 — Name your pipelines</div>
    <div class="ctac-desc">Write down 2–3 tasks you currently run as separate scripts, pipelines, or manual workflows. Give each one a clear identifier and a one-line description of what input it takes and what it returns.</div>
    <div class="ctac-steps">
      <div class="ctac-step">content_pipeline — text in, draft out</div>
      <div class="ctac-step">data_pipeline — CSV in, report out</div>
      <div class="ctac-step">research_pipeline — topic in, facts out</div>
    </div>
  </div>
  <div class="cta-card">
    <div class="ctac-icon">⚙️</div>
    <div class="ctac-title">Step 2 — Write the router</div>
    <div class="ctac-desc">Start with rule-based routing. Write <code>parse_intent()</code> with one <code>if/elif</code> branch per pipeline. Add a <code>PIPELINE_REGISTRY</code> dict. Write 5–10 test inputs and assert they route correctly before touching any pipeline code.</div>
    <div class="ctac-steps">
      <div class="ctac-step">router.py → parse_intent() only</div>
      <div class="ctac-step">tests/test_routing.py → 10 cases</div>
      <div class="ctac-step">all routing tests pass before wiring</div>
    </div>
  </div>
  <div class="cta-card">
    <div class="ctac-icon">🔗</div>
    <div class="ctac-title">Step 3 — Connect and test in sequence</div>
    <div class="ctac-desc">Wrap each existing pipeline as a specialist with a <code>SpecialistResponse</code> return. Test each one in isolation. Then wire the router to the registry and run one end-to-end call per pipeline. Log every decision.</div>
    <div class="ctac-steps">
      <div class="ctac-step">wrap → test isolated → wire</div>
      <div class="ctac-step">one e2e call per pipeline</div>
      <div class="ctac-step">read the log — not the output</div>
    </div>
  </div>
</div>

<p style="font-size:15px; color:#78716c; margin-top: 4px;">The constraint: <strong>router tests must pass before any specialist is called.</strong> Build the routing layer first, completely, and test it independently. The specialists come second.</p>

---

<!-- _class: final -->

# Test the router before you build the system. Build the system before you scale it.

&nbsp;

*Structure. Route. Log. Test in isolation. Fix at the right layer.*

&nbsp;

**You've completed Level 3 — Orchestrator + Specialists.**

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*