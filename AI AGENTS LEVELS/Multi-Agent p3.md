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

  .cg-card .cg-body {
    padding: 12px 14px;
    font-size: 12.5px;
    color: var(--muted);
    background: var(--white);
    line-height: 1.65;
  }

  .cg-card.good .cg-body { color: var(--text); }

  /* ── Level upgrade comparison ── */
  .level-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .lc-col { padding: 18px 20px; }
  .lc-col + .lc-col { border-left: 1px solid var(--border); }
  .lc-col.l2 { background: var(--off-white); }
  .lc-col.l3 { background: #fffbeb; }

  .lc-col .lcc-label {
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

  .lc-col.l2 .lcc-label { color: var(--muted); }
  .lc-col.l3 .lcc-label { color: #92400e; }

  .lc-col .lcc-item {
    font-size: 12.5px;
    padding: 8px 0;
    border-bottom: 1px solid rgba(0,0,0,0.06);
    display: flex;
    align-items: flex-start;
    gap: 9px;
    color: var(--text);
    line-height: 1.5;
  }

  .lc-col .lcc-item:last-child { border-bottom: none; }

  .lcc-item .li-tag {
    font-family: 'DM Mono', monospace;
    font-size: 9.5px;
    font-weight: 700;
    padding: 2px 7px;
    border-radius: 3px;
    flex-shrink: 0;
    margin-top: 2px;
    white-space: nowrap;
  }

  .l2 .li-tag { background: #e7e5e4; color: var(--muted); }
  .l3 .li-tag { background: #fde68a; color: #92400e; }

  /* ── Specialist response envelope ── */
  .response-anatomy {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin: 14px 0;
  }

  .ra-card {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .ra-card .rac-head {
    padding: 9px 14px;
    font-weight: 600;
    font-size: 12.5px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border);
  }

  .ra-card.status .rac-head  { background: #f0fdf4;           color: #166534; border-color: #bbf7d0; }
  .ra-card.payload .rac-head { background: var(--amber-light); color: #92400e; border-color: #fde68a; }
  .ra-card.meta   .rac-head  { background: #f0f9ff;           color: #0c4a6e; border-color: #bae6fd; }

  .ra-card .rac-body {
    padding: 12px 14px;
    background: var(--white);
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.6;
  }

  .ra-card .rac-example {
    margin-top: 9px;
    padding: 7px 10px;
    border-radius: 5px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    line-height: 1.55;
  }

  .ra-card.status  .rac-example { background: #dcfce7; color: #166534; }
  .ra-card.payload .rac-example { background: #fef9c3; color: #92400e; }
  .ra-card.meta    .rac-example { background: #e0f2fe; color: #0c4a6e; }

  /* ── Handoff pattern flow ── */
  .handoff-flow {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .hf-row {
    display: grid;
    grid-template-columns: 36px 160px 1fr 160px;
    align-items: stretch;
    border-bottom: 1px solid var(--border);
  }

  .hf-row:last-child { border-bottom: none; }

  .hf-row .hfr-num {
    background: var(--text);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }

  .hf-row .hfr-actor {
    padding: 11px 13px;
    font-weight: 600;
    font-size: 12.5px;
    color: var(--text);
    border-right: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 7px;
    line-height: 1.4;
  }

  .hf-row.orch  .hfr-actor { background: var(--amber-light); }
  .hf-row.spec  .hfr-actor { background: #f0fdf4; }
  .hf-row.valid .hfr-actor { background: #f0f9ff; }

  .hf-row .hfr-action {
    padding: 11px 14px;
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.6;
    display: flex;
    align-items: center;
  }

  .hf-row .hfr-artifact {
    padding: 11px 13px;
    border-left: 1px solid var(--border);
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    display: flex;
    align-items: center;
    gap: 6px;
    font-weight: 500;
  }

  .hf-row:nth-child(1) .hfr-artifact { background: var(--amber-light); color: #92400e; }
  .hf-row:nth-child(2) .hfr-artifact { background: #f0fdf4;            color: #166534; }
  .hf-row:nth-child(3) .hfr-artifact { background: #f0f9ff;            color: #0369a1; }
  .hf-row:nth-child(4) .hfr-artifact { background: #fdf4ff;            color: #6b21a8; }
  .hf-row:nth-child(5) .hfr-artifact { background: #fff7ed;            color: #9a3412; }

  /* ── State store anatomy ── */
  .state-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 14px 0;
  }

  .state-card {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .state-card .sc-head {
    padding: 9px 14px;
    font-weight: 600;
    font-size: 12.5px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border);
  }

  .state-card.store  .sc-head { background: var(--amber-light); color: #92400e; border-color: #fde68a; }
  .state-card.nostore .sc-head { background: var(--off-white); color: var(--muted); }

  .state-card .sc-body {
    padding: 12px 14px;
    background: var(--white);
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.6;
  }

  .state-card .sc-example {
    margin-top: 9px;
    padding: 7px 10px;
    border-radius: 5px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    line-height: 1.55;
  }

  .state-card.store   .sc-example { background: #fef9c3; color: #92400e; }
  .state-card.nostore .sc-example { background: var(--off-white); color: var(--muted); }

  /* ── Contract table rows ── */
  .contract-stack {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .cs-row {
    display: grid;
    grid-template-columns: 160px 1fr 1fr;
    align-items: stretch;
    border-bottom: 1px solid var(--border);
  }

  .cs-row:last-child { border-bottom: none; }

  .cs-row .csr-specialist {
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

  .cs-row .csr-input {
    padding: 11px 13px;
    font-size: 12px;
    color: var(--muted);
    font-family: 'DM Mono', monospace;
    line-height: 1.6;
    border-right: 1px solid var(--border);
    background: #f0f9ff;
    display: flex;
    align-items: center;
  }

  .cs-row .csr-output {
    padding: 11px 13px;
    font-size: 12px;
    color: var(--muted);
    font-family: 'DM Mono', monospace;
    line-height: 1.6;
    background: #f0fdf4;
    display: flex;
    align-items: center;
  }
---

<!-- _class: cover -->

<div class="series-badge">ORCHESTRATOR + SPECIALISTS · LEVEL 3 — PART 3 OF 4</div>

# Designing the Specialists
## Contracts, reporting, handoffs, and state

&nbsp;

**Specialists haven't changed — but their obligations have.** At Level 3, each specialist must speak a language the orchestrator can act on, not just a language a human can read.

`contracts` · `response envelope` · `handoff` · `state` · `reporting` · `scope`

---

## What's Different About Specialists at Level 3

You've built specialists before — in Level 1 and Level 2. The same single-responsibility rule applies. What changes is the interface: who is calling them, and what that caller needs back.

<div class="level-compare">
  <div class="lc-col l2">
    <div class="lcc-label">⛓️ &nbsp;Level 2 — pipeline specialist</div>
    <div class="lcc-item">
      <span class="li-tag">CALLER</span>
      The orchestrator loop. Always the same caller, always the same sequence.
    </div>
    <div class="lcc-item">
      <span class="li-tag">INPUT</span>
      The previous stage's artifact. Shape is fixed — same every run.
    </div>
    <div class="lcc-item">
      <span class="li-tag">OUTPUT</span>
      The next stage's input artifact. Shape is fixed. Validated by the loop.
    </div>
    <div class="lcc-item">
      <span class="li-tag">ERRORS</span>
      Raise an exception. The loop catches it and halts or retries.
    </div>
    <div class="lcc-item">
      <span class="li-tag">CONTEXT</span>
      Only what's in the artifact. No cross-run memory needed.
    </div>
  </div>
  <div class="lc-col l3">
    <div class="lcc-label">🧭 &nbsp;Level 3 — orchestrated specialist</div>
    <div class="lcc-item">
      <span class="li-tag">CALLER</span>
      The orchestrator. Could be called from any request, at any time.
    </div>
    <div class="lcc-item">
      <span class="li-tag">INPUT</span>
      The orchestrator's routing params. Shape varies by request — must be validated.
    </div>
    <div class="lcc-item">
      <span class="li-tag">OUTPUT</span>
      A standard response envelope. Status, payload, and metadata — always the same wrapper.
    </div>
    <div class="lcc-item">
      <span class="li-tag">ERRORS</span>
      Return a structured error in the envelope. Never raise blind — the orchestrator needs to act on it.
    </div>
    <div class="lcc-item">
      <span class="li-tag">CONTEXT</span>
      May need access to orchestrator-managed state across calls — run ID, prior results, user preferences.
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## What Changes About Specialist Design at Level 3

Three specific obligations are new at this level. A specialist that ignores any one of them forces the orchestrator to compensate — which means scope creep starts there, not in the orchestrator prompt.

<div class="matters-grid">
  <div class="matters-card">
    <div class="mcc-icon">📐</div>
    <div>
      <div class="mcc-title">Input must be typed and validated internally</div>
      <div class="mcc-desc">In Level 2, the pipeline loop validated artifacts before passing them on. At Level 3, the orchestrator passes routing params — a different shape every time. Each specialist must validate its own input before doing any work. A specialist that receives unexpected params should return a structured error, not crash.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">📦</div>
    <div>
      <div class="mcc-title">Output must be wrapped in a standard envelope</div>
      <div class="mcc-desc">The orchestrator receives results from many different specialists. If each one returns a different shape, the orchestrator must know the internals of every specialist to read its output. A standard envelope solves this — the orchestrator reads the wrapper, not the content.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🔴</div>
    <div>
      <div class="mcc-title">Errors must be returned, not raised</div>
      <div class="mcc-desc">A pipeline specialist can raise an exception — the loop catches it. An orchestrated specialist is called dynamically, possibly alongside other specialists. An unhandled exception crashes the entire orchestrator call. Errors go in the envelope, always.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🔒</div>
    <div>
      <div class="mcc-title">Scope stays locked even when called differently</div>
      <div class="mcc-desc">Because specialists can now be called from different request paths, there's more temptation to add conditional logic — "if called from context X, also do Y." Resist it. The specialist's job never changes based on the caller. That's the orchestrator's responsibility.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Defining Clear Input/Output Contracts

At Level 3, every specialist has two contracts: an input contract (what it accepts from the orchestrator) and an output contract (what it always returns). Both are Pydantic models. Both are defined before the specialist is written.

<div class="contract-stack">
  <div class="cs-row">
    <div class="csr-specialist">🔍 Research specialist</div>
    <div class="csr-input">topic: str<br>audience: str<br>depth: "quick" | "deep"</div>
    <div class="csr-output">SpecialistResponse(<br>  payload=ResearchResult,<br>  status="ok" | "error"<br>)</div>
  </div>
  <div class="cs-row">
    <div class="csr-specialist">✍️ Writer specialist</div>
    <div class="csr-input">outline: OutlineArtifact<br>research: ResearchArtifact<br>tone: str</div>
    <div class="csr-output">SpecialistResponse(<br>  payload={"draft": str},<br>  status="ok" | "error"<br>)</div>
  </div>
  <div class="cs-row">
    <div class="csr-specialist">📊 Data analyst specialist</div>
    <div class="csr-input">file_path: str<br>question: str<br>output_format: "table" | "summary"</div>
    <div class="csr-output">SpecialistResponse(<br>  payload=AnalysisResult,<br>  status="ok" | "error"<br>)</div>
  </div>
  <div class="cs-row">
    <div class="csr-specialist">✅ QA specialist</div>
    <div class="csr-input">draft: str<br>research: ResearchArtifact<br>checklist: list[str]</div>
    <div class="csr-output">SpecialistResponse(<br>  payload=QAReport,<br>  status="ok" | "flagged"<br>)</div>
  </div>
</div>

<div class="highlight">

**The input contract is defined by the routing params** in <code>routing_decision.json</code>. The orchestrator's <code>params</code> field must map exactly to each specialist's input model. Define both at the same time — they are two halves of the same interface.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02 — CONTINUED</div>

## The Standard Input Validation Pattern

Every specialist function opens the same way: validate input, return a structured error immediately if invalid, do no work otherwise.

<div class="code-block">
  <div class="cb-header">
    <div class="cb-dots">
      <div class="cb-dot red"></div>
      <div class="cb-dot yellow"></div>
      <div class="cb-dot green"></div>
    </div>
    <div class="cb-filename">specialists/research.py — input validation first</div>
  </div>
  <div class="cb-body"><span class="kw">from</span> <span class="va">pydantic</span> <span class="kw">import</span> <span class="va">BaseModel, ValidationError</span>
<span class="kw">from</span> <span class="va">contracts</span> <span class="kw">import</span> <span class="va">SpecialistResponse</span>

<span class="kw">class</span> <span class="fn">ResearchInput</span>(<span class="va">BaseModel</span>):
    <span class="va">topic</span>:    <span class="va">str</span>
    <span class="va">audience</span>: <span class="va">str</span>
    <span class="va">depth</span>:    <span class="va">str</span> = <span class="st">"quick"</span>   <span class="cm"># default — safe to omit</span>

<span class="kw">def</span> <span class="fn">run_research_specialist</span>(**<span class="va">params</span>) -> <span class="va">SpecialistResponse</span>:
    <span class="cm"># ── 1. Validate input immediately ──────────────────────</span>
    <span class="kw">try</span>:
        <span class="va">inputs</span> = <span class="fn">ResearchInput</span>(**<span class="va">params</span>)
    <span class="kw">except</span> <span class="va">ValidationError</span> <span class="kw">as</span> <span class="va">e</span>:
        <span class="kw">return</span> <span class="va">SpecialistResponse</span>(
            <span class="va">status</span>=<span class="st">"error"</span>,
            <span class="va">error</span>=<span class="st">f"Invalid input: {e}"</span>,
            <span class="va">payload</span>=<span class="nu">None</span>
        )
    <span class="cm"># ── 2. Do the work — only if input is valid ─────────────</span>
    <span class="va">result</span> = <span class="fn">_call_research_llm</span>(<span class="va">inputs</span>)

    <span class="cm"># ── 3. Return in the standard envelope ─────────────────</span>
    <span class="kw">return</span> <span class="va">SpecialistResponse</span>(
        <span class="va">status</span>=<span class="st">"ok"</span>,
        <span class="va">payload</span>=<span class="va">result</span>,
        <span class="va">meta</span>={<span class="st">"depth"</span>: <span class="va">inputs</span>.<span class="va">depth</span>, <span class="st">"topic"</span>: <span class="va">inputs</span>.<span class="va">topic</span>}
    )</div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## How Specialists Report Back to the Orchestrator

Every specialist returns the same wrapper — `SpecialistResponse` — regardless of what it does or what it produces. The orchestrator reads the wrapper first. It reads the payload only if the status is `ok`.

<div class="response-anatomy">
  <div class="ra-card status">
    <div class="rac-head">✅ &nbsp;status</div>
    <div class="rac-body">
      The machine-readable result of the call. The orchestrator branches on this field — not on the payload content.
      <div class="rac-example">"ok"<br>"error"<br>"flagged"<br>"needs_clarification"</div>
    </div>
  </div>
  <div class="ra-card payload">
    <div class="rac-head">📦 &nbsp;payload</div>
    <div class="rac-body">
      The specialist's actual output — an artifact, a structured object, or a string. Only read by the orchestrator when status is <code>ok</code> or <code>flagged</code>.
      <div class="rac-example">ResearchArtifact<br>{"draft": "..."}<br>QAReport<br>null (on error)</div>
    </div>
  </div>
  <div class="ra-card meta">
    <div class="rac-head">🏷️ &nbsp;meta</div>
    <div class="rac-body">
      Diagnostic fields the orchestrator logs but doesn't act on — tokens used, duration, model name, input params echoed back. Never used for routing decisions.
      <div class="rac-example">tokens_used: 1842<br>duration_ms: 3201<br>model: "claude-..."<br>specialist: "research"</div>
    </div>
  </div>
</div>

<div class="schema-block">
  <div class="sb-header">
    <div class="sb-title">SpecialistResponse — the universal envelope</div>
    <div class="sb-badge">contracts.py</div>
  </div>
  <div class="sb-body"><span class="sk">"status"</span>:    <span class="sv">"ok" | "error" | "flagged" | "needs_clarification"</span>,
<span class="sk">"payload"</span>:   <span class="sc">// the specialist's result — null on error</span>
<span class="sk">"error"</span>:     <span class="sv">"string — only present when status is error"</span>,
<span class="sk">"meta"</span>:      { <span class="sk">"specialist"</span>: <span class="sv">"string"</span>, <span class="sk">"duration_ms"</span>: <span class="sn">0</span>, <span class="sk">"tokens_used"</span>: <span class="sn">0</span> }</div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03 — CONTINUED</div>

## How the Orchestrator Reads the Envelope

The orchestrator's result-handling code is the same for every specialist — because every specialist returns the same envelope shape.

<div class="code-block">
  <div class="cb-header">
    <div class="cb-dots">
      <div class="cb-dot red"></div>
      <div class="cb-dot yellow"></div>
      <div class="cb-dot green"></div>
    </div>
    <div class="cb-filename">orchestrator.py — reading the SpecialistResponse</div>
  </div>
  <div class="cb-body"><span class="kw">def</span> <span class="fn">handle_specialist_response</span>(
    <span class="va">response</span>: <span class="va">SpecialistResponse</span>,
    <span class="va">specialist_name</span>: <span class="va">str</span>
) -> <span class="va">dict</span>:

    <span class="cm"># ── Log meta regardless of status ──────────────────────</span>
    <span class="fn">log_meta</span>(<span class="va">specialist_name</span>, <span class="va">response</span>.<span class="va">meta</span>)

    <span class="cm"># ── Branch on status — never on payload content ────────</span>
    <span class="kw">if</span> <span class="va">response</span>.<span class="va">status</span> == <span class="st">"ok"</span>:
        <span class="kw">return</span> <span class="fn">wrap_success</span>(<span class="va">response</span>.<span class="va">payload</span>)

    <span class="kw">elif</span> <span class="va">response</span>.<span class="va">status</span> == <span class="st">"flagged"</span>:
        <span class="kw">return</span> <span class="fn">wrap_flagged</span>(<span class="va">response</span>.<span class="va">payload</span>, <span class="va">response</span>.<span class="va">error</span>)

    <span class="kw">elif</span> <span class="va">response</span>.<span class="va">status</span> == <span class="st">"needs_clarification"</span>:
        <span class="kw">return</span> <span class="fn">wrap_clarification</span>(<span class="va">response</span>.<span class="va">error</span>)

    <span class="kw">else</span>:  <span class="cm"># "error"</span>
        <span class="fn">log_error</span>(<span class="va">specialist_name</span>, <span class="va">response</span>.<span class="va">error</span>)
        <span class="kw">raise</span> <span class="va">SpecialistError</span>(<span class="st">f"{specialist_name}: {response.error}"</span>)</div>
</div>

<div class="highlight">

**The orchestrator never inspects payload content to decide what to do next.** It reads <code>status</code>. If it needs to branch based on what the research specialist found, that branching belongs in a downstream specialist — not in the orchestrator's result handler.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## The Handoff Pattern — How Agents Pass Work Cleanly

A handoff is the moment the orchestrator calls one specialist, receives its response, and decides whether and how to call the next one. The handoff is always explicit — no data flows between specialists without the orchestrator touching it first.

<div class="handoff-flow">
  <div class="hf-row orch">
    <div class="hfr-num">1</div>
    <div class="hfr-actor">🧭 Orchestrator</div>
    <div class="hfr-action">Dispatches to the Research specialist with validated params from the routing decision.</div>
    <div class="hfr-artifact">params → research</div>
  </div>
  <div class="hf-row spec">
    <div class="hfr-num">2</div>
    <div class="hfr-actor">🔍 Research specialist</div>
    <div class="hfr-action">Validates input, calls the LLM, returns a <code>SpecialistResponse</code> with <code>status="ok"</code> and a <code>ResearchArtifact</code> payload.</div>
    <div class="hfr-artifact">SpecialistResponse</div>
  </div>
  <div class="hf-row valid">
    <div class="hfr-num">3</div>
    <div class="hfr-actor">🧭 Orchestrator</div>
    <div class="hfr-action">Reads the envelope. Status is <code>ok</code>. Saves the artifact. Decides whether to call the Writer specialist next, based on the routing decision's pipeline sequence.</div>
    <div class="hfr-artifact">artifact saved ✓</div>
  </div>
  <div class="hf-row spec">
    <div class="hfr-num">4</div>
    <div class="hfr-actor">✍️ Writer specialist</div>
    <div class="hfr-action">Receives the Research artifact as part of its input params. Validates its own input contract. Calls the LLM. Returns its own <code>SpecialistResponse</code>.</div>
    <div class="hfr-artifact">SpecialistResponse</div>
  </div>
  <div class="hf-row valid">
    <div class="hfr-num">5</div>
    <div class="hfr-actor">🧭 Orchestrator</div>
    <div class="hfr-action">Reads the envelope. Status is <code>ok</code>. Assembles the final response for the caller from the Writer's payload. Run complete.</div>
    <div class="hfr-artifact">→ caller response</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04 — CONTINUED</div>

## The Handoff Rules

Three rules that govern every handoff. Violating any one of them means the orchestrator is doing specialist work.

<div class="compare-grid">
  <div class="cg-card bad">
    <div class="cg-head">❌ &nbsp;Specialists call each other directly</div>
    <div class="cg-body">
      The Research specialist, after returning its result, directly calls the Writer specialist with the artifact. The orchestrator never sees the handoff — it can't log it, retry it, or branch on the result.<br><br>
      The system now has hidden dependencies between specialists. Testing either one in isolation becomes impossible.
    </div>
  </div>
  <div class="cg-card good">
    <div class="cg-head">✅ &nbsp;All handoffs go through the orchestrator</div>
    <div class="cg-body">
      Every specialist call originates from the orchestrator. Every specialist result returns to the orchestrator. Specialists never know about each other. The orchestrator is the only place that sequences them.<br><br>
      Adding, removing, or reordering a specialist requires one change in one place.
    </div>
  </div>
</div>

<div class="compare-grid">
  <div class="cg-card bad">
    <div class="cg-head">❌ &nbsp;Orchestrator passes its entire state</div>
    <div class="cg-body">
      The orchestrator passes its full run state — all prior artifacts, all prior responses — as context to every specialist. The Writer receives the QA report even though it has no use for it. Context bloat, higher cost, and the specialist might use context it wasn't designed for.
    </div>
  </div>
  <div class="cg-card good">
    <div class="cg-head">✅ &nbsp;Orchestrator passes only what's needed</div>
    <div class="cg-body">
      Each specialist receives exactly the params in its input contract — nothing more. The orchestrator extracts the relevant fields from its state and passes only those. Specialists stay predictable; their behaviour doesn't change based on what else the orchestrator has accumulated.
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## State Management — What the Orchestrator Needs to Remember

The orchestrator runs a sequence of specialist calls. Between calls, it must hold the results of what's already happened. This is run state — and it must be explicit, typed, and never leaked into specialist prompts.

<div class="state-grid">
  <div class="state-card store">
    <div class="sc-head">💾 &nbsp;What to store in run state</div>
    <div class="sc-body">
      Information the orchestrator needs to make decisions between specialist calls. Not content — decisions.
      <div class="sc-example">run_id: "run_20250422_001"<br>routing_decision: RoutingDecision<br>completed_stages: ["research", "outline"]<br>artifacts: {"research": ResearchArtifact}<br>status: "in_progress"</div>
    </div>
  </div>
  <div class="state-card nostore">
    <div class="sc-head">🚫 &nbsp;What not to store in run state</div>
    <div class="sc-body">
      Content that belongs inside specialist artifacts. If the orchestrator stores this, it's either duplicating the artifact or holding data that should have been returned in the response envelope.
      <div class="sc-example">❌ the full research text<br>❌ intermediate LLM outputs<br>❌ the user's preferences (store in user context)<br>❌ specialist system prompts</div>
    </div>
  </div>
</div>

<div class="walkthrough">
  <div class="wt-row">
    <div class="wr-num">1</div>
    <div class="wr-content">
      <div class="wrc-title">🆕 &nbsp;Run begins — initialise state</div>
      <div class="wrc-desc">Create a <code>RunState</code> object with a unique run ID, the routing decision, and an empty artifacts dict. This is the orchestrator's working memory for this request.</div>
      <div class="wrc-code">state = RunState(run_id=uuid(), routing=decision, artifacts={}, completed=[])</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">2</div>
    <div class="wr-content">
      <div class="wrc-title">📥 &nbsp;After each specialist — update state</div>
      <div class="wrc-desc">When a specialist returns <code>status="ok"</code>, add its payload to <code>state.artifacts</code> and append the stage name to <code>state.completed</code>. Never mutate state on error — the state before the failure remains valid.</div>
      <div class="wrc-code">state.artifacts["research"] = response.payload; state.completed.append("research")</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">3</div>
    <div class="wr-content">
      <div class="wrc-title">🔍 &nbsp;Before each specialist call — read state</div>
      <div class="wrc-desc">Extract only the fields the next specialist's input contract requires from <code>state.artifacts</code>. Pass only those. The specialist never receives the <code>RunState</code> object itself.</div>
      <div class="wrc-code">writer_params = {"outline": state.artifacts["outline"], "research": state.artifacts["research"]}</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">4</div>
    <div class="wr-content">
      <div class="wrc-title">💾 &nbsp;Persist state for resumability</div>
      <div class="wrc-desc">Save <code>RunState</code> to disk after every successful specialist call. If the run crashes at stage 4, load the last saved state and resume from <code>state.completed[-1] + 1</code>. Stages already in <code>completed</code> never re-run.</div>
      <div class="wrc-code">save_state(f"runs/{state.run_id}.json", state)</div>
    </div>
  </div>
</div>

---

## Quick Reference — Part 3 Specialist Design

The rules and patterns every specialist in a Level 3 system must follow.

<table class="cheat-table">
  <thead>
    <tr><th>Decision</th><th>Rule</th><th>Where it lives</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Input contract</strong></td>
      <td>One Pydantic model per specialist. Validated at the top of the function before any LLM call.</td>
      <td><span class="mono">specialists/*.py</span></td>
    </tr>
    <tr>
      <td><strong>Output envelope</strong></td>
      <td>Every specialist returns <code>SpecialistResponse</code>. Same wrapper, always. Status field is machine-readable.</td>
      <td><span class="mono">contracts.py</span></td>
    </tr>
    <tr>
      <td><strong>Error handling</strong></td>
      <td>Catch all exceptions internally. Return <code>status="error"</code> in the envelope. Never raise from a specialist.</td>
      <td><span class="mono">specialists/*.py</span></td>
    </tr>
    <tr>
      <td><strong>Handoff direction</strong></td>
      <td>All calls go through the orchestrator. Specialists never call each other directly.</td>
      <td>Architecture rule</td>
    </tr>
    <tr>
      <td><strong>Context scoping</strong></td>
      <td>Pass only what the specialist's input contract requires. Never pass full run state or prior artifacts not in the contract.</td>
      <td><span class="mono">orchestrator.py</span></td>
    </tr>
    <tr>
      <td><strong>Run state fields</strong></td>
      <td>Store run_id, routing decision, completed stages, and artifact references. Never store content inside the state object.</td>
      <td><span class="mono">orchestrator.py → RunState</span></td>
    </tr>
    <tr>
      <td><strong>State persistence</strong></td>
      <td>Save <code>RunState</code> to disk after every successful specialist call. Enables resumption from any checkpoint.</td>
      <td><span class="mono">runs/*.json</span></td>
    </tr>
  </tbody>
</table>

---

<!-- _class: final -->

# Specialists don't know about each other. The orchestrator does.

&nbsp;

*Standard envelope. Typed input. Errors returned, never raised. State owned by the orchestrator alone.*

&nbsp;

Next: **Part 4 — Testing and Scaling the System.**

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*