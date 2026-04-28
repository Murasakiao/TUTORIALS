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
  .matters-card .mcc-title { font-weight: 600; font-size: 14px; color: var(--text); margin-bottom: 4px; }
  .matters-card .mcc-desc  { font-size: 12.5px; color: var(--muted); line-height: 1.55; }

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
  .cheat-table tr:last-child td { border-bottom: 1px solid var(--border); }
  .cheat-table .mono { font-family: 'DM Mono', monospace; color: var(--amber-dim); font-size: 12px; }

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

  .log-block .lg-ts    { color: #475569; }
  .log-block .lg-ok    { color: #4ade80; font-weight: 600; }
  .log-block .lg-warn  { color: #fbbf24; font-weight: 600; }
  .log-block .lg-err   { color: #f87171; font-weight: 600; }
  .log-block .lg-pause { color: #c084fc; font-weight: 600; }
  .log-block .lg-info  { color: #94a3b8; }
  .log-block .lg-key   { color: #7dd3fc; }
  .log-block .lg-val   { color: #86efac; }

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

  .cg-card { border-radius: 8px; overflow: hidden; border: 1px solid var(--border); }
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

  /* ── Checkpoint flow ── */
  .checkpoint-flow {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .cpf-row {
    display: grid;
    grid-template-columns: 36px 180px 1fr auto;
    align-items: stretch;
    border-bottom: 1px solid var(--border);
  }

  .cpf-row:last-child { border-bottom: none; }

  .cpf-row .cpfr-num {
    background: var(--text);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }

  .cpf-row .cpfr-stage {
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

  .cpf-row .cpfr-action {
    padding: 11px 14px;
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.6;
    display: flex;
    align-items: center;
  }

  .cpf-row .cpfr-type {
    padding: 11px 13px;
    border-left: 1px solid var(--border);
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    display: flex;
    align-items: center;
    white-space: nowrap;
  }

  .cpf-row.auto   .cpfr-type { background: #f0fdf4;           color: #166534; }
  .cpf-row.human  .cpfr-type { background: #fdf4ff;           color: #6b21a8; }
  .cpf-row.staged .cpfr-type { background: var(--amber-light); color: #92400e; }
  .cpf-row.gate   .cpfr-type { background: #fef2f2;           color: #991b1b; }

  /* ── Guardrail stack ── */
  .guardrail-stack {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .gr-row {
    display: grid;
    grid-template-columns: 180px 1fr auto;
    align-items: stretch;
    border-bottom: 1px solid var(--border);
  }

  .gr-row:last-child { border-bottom: none; }

  .gr-row .grr-type {
    padding: 11px 14px;
    font-weight: 700;
    font-size: 12.5px;
    color: var(--text);
    background: var(--off-white);
    border-right: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 8px;
    line-height: 1.4;
  }

  .gr-row .grr-desc {
    padding: 11px 14px;
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.6;
    display: flex;
    align-items: center;
  }

  .gr-row .grr-layer {
    padding: 11px 13px;
    border-left: 1px solid var(--border);
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    display: flex;
    align-items: center;
    white-space: nowrap;
  }

  .gr-row.prompt   .grr-layer { background: var(--amber-light); color: #92400e; }
  .gr-row.contract .grr-layer { background: #f0f9ff;            color: #0369a1; }
  .gr-row.code     .grr-layer { background: #f0fdf4;            color: #166534; }
  .gr-row.scope    .grr-layer { background: #fdf4ff;            color: #6b21a8; }
  .gr-row.budget   .grr-layer { background: #fef2f2;            color: #991b1b; }

  /* ── Monitor panel ── */
  .monitor-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 14px 0;
  }

  .monitor-card {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .monitor-card .mc-head {
    padding: 9px 14px;
    font-weight: 600;
    font-size: 12.5px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border);
  }

  .monitor-card.signal .mc-head { background: #f0f9ff;           color: #0c4a6e; border-color: #bae6fd; }
  .monitor-card.metric .mc-head { background: var(--amber-light); color: #92400e; border-color: #fde68a; }
  .monitor-card.alert  .mc-head { background: #fef2f2;           color: #991b1b; border-color: #fecaca; }
  .monitor-card.action .mc-head { background: #f0fdf4;           color: #166534; border-color: #bbf7d0; }

  .monitor-card .mc-body {
    padding: 11px 14px;
    background: var(--white);
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.6;
    display: flex;
    flex-direction: column;
    gap: 5px;
  }

  .mc-item {
    display: flex;
    align-items: flex-start;
    gap: 8px;
    font-size: 12px;
    line-height: 1.5;
    padding: 4px 0;
    border-bottom: 1px solid var(--border);
  }

  .mc-item:last-child { border-bottom: none; }

  .mc-item .mci-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    font-weight: 700;
    padding: 2px 5px;
    border-radius: 3px;
    flex-shrink: 0;
    margin-top: 1px;
  }

  .signal .mci-label { background: #bae6fd; color: #0369a1; }
  .metric .mci-label { background: #fde68a; color: #92400e; }
  .alert  .mci-label { background: #fecaca; color: #991b1b; }
  .action .mci-label { background: #bbf7d0; color: #166534; }

  /* ── Recovery decision stack ── */
  .recovery-stack {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .rs-row {
    display: grid;
    grid-template-columns: 36px 180px 1fr auto;
    align-items: stretch;
    border-bottom: 1px solid var(--border);
  }

  .rs-row:last-child { border-bottom: none; }

  .rs-row .rsr-num {
    background: var(--text);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .rs-row .rsr-condition {
    padding: 11px 13px;
    font-weight: 600;
    font-size: 12px;
    color: var(--text);
    background: var(--off-white);
    border-right: 1px solid var(--border);
    display: flex;
    align-items: center;
    line-height: 1.4;
  }

  .rs-row .rsr-action {
    padding: 11px 14px;
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.6;
    display: flex;
    align-items: center;
  }

  .rs-row .rsr-verdict {
    padding: 11px 13px;
    border-left: 1px solid var(--border);
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    display: flex;
    align-items: center;
    white-space: nowrap;
  }

  .rs-row.retry    .rsr-verdict { background: #f0f9ff;           color: #0369a1; }
  .rs-row.partial  .rsr-verdict { background: var(--amber-light); color: #92400e; }
  .rs-row.escalate .rsr-verdict { background: #fdf4ff;           color: #6b21a8; }
  .rs-row.halt     .rsr-verdict { background: #fef2f2;           color: #991b1b; }

  /* ── Trace block ── */
  .trace-block {
    background: #0f172a;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid #1e293b;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
  }

  .trace-block .tb-header {
    background: #1e293b;
    padding: 8px 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid #334155;
  }

  .trace-block .tb-header .tb-title {
    font-size: 11px;
    color: #94a3b8;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }

  .trace-block .tb-header .tb-badge {
    font-size: 10px;
    background: #0f172a;
    color: #64748b;
    padding: 2px 8px;
    border-radius: 3px;
  }

  .trace-block .tb-body {
    padding: 14px 18px;
    font-size: 11.5px;
    line-height: 1.9;
    white-space: pre;
  }

  .trace-block .tr-l0  { color: #fbbf24; font-weight: 600; }
  .trace-block .tr-l1  { color: #86efac; }
  .trace-block .tr-l2  { color: #7dd3fc; }
  .trace-block .tr-l3  { color: #c4b5fd; }
  .trace-block .tr-ts  { color: #475569; }
  .trace-block .tr-ok  { color: #4ade80; font-weight: 600; }
  .trace-block .tr-err { color: #f87171; font-weight: 600; }
  .trace-block .tr-dim { color: #334155; }
---

<!-- _class: cover -->

<div class="series-badge">AGENT TEAMS · LEVEL 4 — PART 3 OF 4</div>

# Control, Safety, and Observability
## Checkpoints, guardrails, monitoring, tracing, and recovery

&nbsp;

**An autonomous team that you can't see is not autonomous — it's uncontrolled.** Visibility, boundaries, and recovery paths are not optional features. They are the system.

`human-in-the-loop` · `guardrails` · `monitoring` · `distributed tracing` · `recovery`

---

## Why Control Matters More at Level 4

At Level 1, one agent makes one call. You read the output and decide what to do. At Level 4, a team of agents makes dozens of calls across multiple orchestrators before you see a single result. The surface area for undetected failure is enormous — and the cost of a wrong result running to completion is proportionally higher.

<div class="matters-grid">
  <div class="matters-card">
    <div class="mcc-icon">🔍</div>
    <div>
      <div class="mcc-title">Failures compound across layers</div>
      <div class="mcc-desc">A wrong routing decision at the top level produces a wrong specialist call three layers down, which produces a wrong artifact, which gets QA-passed by a critic that wasn't designed to catch that class of error. Each layer amplifies the original mistake.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">💸</div>
    <div>
      <div class="mcc-title">Cost scales with pipeline depth</div>
      <div class="mcc-desc">A five-stage pipeline running across four specialists costs five times as much as a single agent call. A wrong run that completes costs the same as a correct one. Without early detection, you pay full price for wrong results.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🎭</div>
    <div>
      <div class="mcc-title">Agents don't know they've drifted</div>
      <div class="mcc-desc">An agent that has started doing something outside its defined scope doesn't signal this. It produces output, marks status "ok", and the pipeline continues. Scope drift is invisible without external monitoring and explicit boundary enforcement.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🏗️</div>
    <div>
      <div class="mcc-title">Debugging across orchestrators requires traces</div>
      <div class="mcc-desc">A wrong final result from a four-team system could originate at the top-level router, the team orchestrator, or any of eight specialists. Without a distributed trace keyed to a single run ID, finding the origin requires reconstructing the entire call sequence manually.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Human-in-the-Loop — Where to Put Approval Checkpoints

Human approval is expensive — it adds latency, breaks autonomy, and defeats the purpose of building automated teams. The goal is not to add checkpoints everywhere. It is to add them at the exact moments where human judgment changes the outcome.

<div class="checkpoint-flow">
  <div class="cpf-row auto">
    <div class="cpfr-num">1</div>
    <div class="cpfr-stage">🌐 Top-level routing</div>
    <div class="cpfr-action">Orchestrator parses intent and selects the Content Team. Confidence is HIGH. This is fully reversible — routing decisions cost nothing to retry. No human needed.</div>
    <div class="cpfr-type">auto — no checkpoint</div>
  </div>
  <div class="cpf-row auto">
    <div class="cpfr-num">2</div>
    <div class="cpfr-stage">✍️ Content Team runs</div>
    <div class="cpfr-action">Research → Outline → Write → Edit. All internal to the team. Intermediate artifacts stay internal. No external side effects. Fully reversible at any point. No human needed.</div>
    <div class="cpfr-type">auto — no checkpoint</div>
  </div>
  <div class="cpf-row human">
    <div class="cpfr-num">3</div>
    <div class="cpfr-stage">📋 Before publishing</div>
    <div class="cpfr-action">Content Team returns the final draft. The system pauses. A human reviews the draft before the Engineering Team is called to publish it. Publishing is irreversible — this is the checkpoint.</div>
    <div class="cpfr-type">⏸ human approval</div>
  </div>
  <div class="cpf-row staged">
    <div class="cpfr-num">4</div>
    <div class="cpfr-stage">⚙️ Engineering Team</div>
    <div class="cpfr-action">Human approved. Engineering Team formats and deploys. Staged deploy first — publishes to a preview URL, not production. Human confirms the preview before production promotion.</div>
    <div class="cpfr-type">⏸ staged review</div>
  </div>
  <div class="cpf-row gate">
    <div class="cpfr-num">5</div>
    <div class="cpfr-stage">🚀 Production push</div>
    <div class="cpfr-action">Human confirms preview. System promotes to production. This is the final irreversible action — the second and last checkpoint in the entire pipeline.</div>
    <div class="cpfr-type">🔴 hard gate</div>
  </div>
</div>

<div class="highlight">

**The rule for placing checkpoints:** Add a human approval step before any action that is <strong>irreversible</strong> (publishing, sending, deploying, deleting) or <strong>high-stakes</strong> (financial, legal, medical, customer-facing). Everything reversible runs autonomously.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01 — CONTINUED</div>

## Implementing Checkpoints Without Blocking the System

A checkpoint that blocks a thread while waiting for human input wastes resources and creates fragile systems. The correct pattern is pause-and-persist — the system saves state and exits. It resumes when the human responds.

<div class="code-block">
  <div class="cb-header">
    <div class="cb-dots">
      <div class="cb-dot red"></div>
      <div class="cb-dot yellow"></div>
      <div class="cb-dot green"></div>
    </div>
    <div class="cb-filename">top_level/runner.py — pause-and-persist checkpoint</div>
  </div>
  <div class="cb-body"><span class="kw">def</span> <span class="fn">run</span>(<span class="va">ctx</span>: <span class="va">GlobalContext</span>, **<span class="va">params</span>) -> <span class="va">dict</span>:
    <span class="cm"># ── Phase 1: content team runs autonomously ─────────────</span>
    <span class="va">content_result</span> = <span class="fn">run_content_team</span>(<span class="va">ctx</span>, **<span class="va">params</span>)
    <span class="fn">save_run_state</span>(<span class="va">ctx</span>.<span class="va">run_id</span>, <span class="st">"after_content"</span>, <span class="va">content_result</span>)

    <span class="cm"># ── Checkpoint: pause before irreversible action ─────────</span>
    <span class="fn">request_human_approval</span>(
        <span class="va">run_id</span>   = <span class="va">ctx</span>.<span class="va">run_id</span>,
        <span class="va">stage</span>    = <span class="st">"pre_publish"</span>,
        <span class="va">payload</span>  = <span class="va">content_result</span>.<span class="va">payload</span>,
        <span class="va">callback</span> = <span class="st">"/api/runs/resume"</span>   <span class="cm"># webhook — system exits after this</span>
    )
    <span class="kw">return</span> {<span class="st">"status"</span>: <span class="st">"awaiting_approval"</span>, <span class="st">"run_id"</span>: <span class="va">ctx</span>.<span class="va">run_id</span>}

<span class="kw">def</span> <span class="fn">resume</span>(<span class="va">run_id</span>: <span class="va">str</span>, <span class="va">approved</span>: <span class="va">bool</span>, <span class="va">notes</span>: <span class="va">str</span> = <span class="st">""</span>):
    <span class="kw">if</span> <span class="kw">not</span> <span class="va">approved</span>:
        <span class="kw">return</span> {<span class="st">"status"</span>: <span class="st">"rejected"</span>, <span class="st">"notes"</span>: <span class="va">notes</span>}
    <span class="va">state</span> = <span class="fn">load_run_state</span>(<span class="va">run_id</span>, <span class="st">"after_content"</span>)  <span class="cm"># resume exactly here</span>
    <span class="kw">return</span> <span class="fn">run_engineering_team</span>(<span class="va">state</span>.<span class="va">ctx</span>, <span class="va">content</span>=<span class="va">state</span>.<span class="va">payload</span>)</div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Guardrails — Keeping Agents Inside Their Boundaries

Guardrails are the constraints that prevent an agent from doing something outside its defined scope — regardless of what the input asks for. They are not the same as system prompt instructions. Instructions can be overridden by clever prompting. Guardrails are enforced in code.

<div class="guardrail-stack">
  <div class="gr-row prompt">
    <div class="grr-type">📝 &nbsp;Prompt-level guardrail</div>
    <div class="grr-desc">The system prompt explicitly names what the agent must not do: "You do not write code. You do not make API calls. You return only structured JSON." Weakest layer — can be undermined by adversarial input, but prevents accidental drift.</div>
    <div class="grr-layer">system prompt</div>
  </div>
  <div class="gr-row contract">
    <div class="grr-type">📐 &nbsp;Contract-level guardrail</div>
    <div class="grr-desc">Pydantic models enforce the exact shape of every input and output. An agent that produces a field outside its output contract raises <code>ValidationError</code> immediately — before the result reaches any downstream stage.</div>
    <div class="grr-layer">contracts.py</div>
  </div>
  <div class="gr-row code">
    <div class="grr-type">🔧 &nbsp;Code-level guardrail</div>
    <div class="grr-desc">The orchestrator's registry maps string identifiers to functions. An agent that tries to call a pipeline or specialist by name — rather than returning a routing decision — cannot execute it. The dispatch layer controls what runs.</div>
    <div class="grr-layer">PIPELINE_REGISTRY</div>
  </div>
  <div class="gr-row scope">
    <div class="grr-type">🔒 &nbsp;Scope-level guardrail</div>
    <div class="grr-desc">Each specialist receives only the params its input contract requires. It has no access to the run state, the global context beyond what's explicitly passed, or other specialists' artifacts. Scoped injection prevents lateral access.</div>
    <div class="grr-layer">prepare_params()</div>
  </div>
  <div class="gr-row budget">
    <div class="grr-type">💰 &nbsp;Budget-level guardrail</div>
    <div class="grr-desc">A hard ceiling on tokens and wall-clock time per stage, per team, and per run. If a specialist exceeds its token budget, the call is aborted and the team returns <code>status="error"</code>. Prevents runaway cost from loops or oversized context.</div>
    <div class="grr-layer">max_tokens config</div>
  </div>
</div>

<div class="highlight">

**Guardrails work in layers.** The prompt layer stops accidental violations. The contract layer stops structural violations. The code layer stops execution violations. The budget layer stops cost violations. Each layer catches what the layer above it misses.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Monitoring — Knowing What Your Team Is Doing at Any Moment

Monitoring at Level 4 is not about logging errors. It is about knowing the current state of every running team in real time — so you can intervene before a problem completes its full pipeline.

<div class="monitor-grid">
  <div class="monitor-card signal">
    <div class="mc-head">📡 &nbsp;Signals to watch</div>
    <div class="mc-body">
      <div class="mc-item"><span class="mci-label">STAGE</span>Which stage of which team is currently running, keyed to run_id</div>
      <div class="mc-item"><span class="mci-label">DEPTH</span>Number of nested orchestrator calls in the current request</div>
      <div class="mc-item"><span class="mci-label">AGE</span>Wall-clock time since the run started — flag runs older than threshold</div>
      <div class="mc-item"><span class="mci-label">QUEUE</span>Number of pending human approval checkpoints awaiting response</div>
    </div>
  </div>
  <div class="monitor-card metric">
    <div class="mc-head">📊 &nbsp;Metrics to track per run</div>
    <div class="mc-body">
      <div class="mc-item"><span class="mci-label">TOKENS</span>Cumulative token spend — per specialist, per team, per run</div>
      <div class="mc-item"><span class="mci-label">LATENCY</span>Duration per stage — helps identify which specialist is the bottleneck</div>
      <div class="mc-item"><span class="mci-label">RETRIES</span>Count of retry attempts per stage — sustained retries signal a prompt issue</div>
      <div class="mc-item"><span class="mci-label">STATUS</span>Distribution of ok / error / flagged / partial across all recent runs</div>
    </div>
  </div>
  <div class="monitor-card alert">
    <div class="mc-head">🚨 &nbsp;Alert thresholds</div>
    <div class="mc-body">
      <div class="mc-item"><span class="mci-label">COST</span>Single run exceeds token budget ceiling — halt immediately</div>
      <div class="mc-item"><span class="mci-label">TIME</span>Run age exceeds 3× median duration for that pipeline</div>
      <div class="mc-item"><span class="mci-label">LOOP</span>Same specialist called more than <code>MAX_RETRIES</code> in one run</div>
      <div class="mc-item"><span class="mci-label">ERROR</span>Error rate across last 20 runs exceeds 15%</div>
    </div>
  </div>
  <div class="monitor-card action">
    <div class="mc-head">⚡ &nbsp;Automated responses</div>
    <div class="mc-body">
      <div class="mc-item"><span class="mci-label">PAUSE</span>Suspend the run at next checkpoint — do not abort, preserve state</div>
      <div class="mc-item"><span class="mci-label">NOTIFY</span>Send alert with run_id, current stage, and last artifact path</div>
      <div class="mc-item"><span class="mci-label">THROTTLE</span>Reduce concurrent runs when token spend rate exceeds threshold</div>
      <div class="mc-item"><span class="mci-label">HALT</span>Abort run when budget ceiling or loop guard is exceeded</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Logging and Tracing Decisions Across Multiple Orchestrators

At Level 4, one user request triggers calls across the top-level orchestrator, one or more team orchestrators, and multiple specialists. A flat log file is not enough — you need a distributed trace that groups all calls under a single run ID and shows the nesting structure.

<div class="trace-block">
  <div class="tb-header">
    <div class="tb-title">distributed trace — run_20250422_031</div>
    <div class="tb-badge">structured_trace.log</div>
  </div>
  <div class="tb-body"><span class="tr-l0">▶ [TOP]</span>  <span class="tr-ts">03:51:00</span>  <span class="tr-ok">[START]</span>   <span class="tr-l0">run_id=run_20250422_031</span>  input="research and publish a competitor analysis"
  <span class="tr-l0">│</span>
  <span class="tr-l0">├─</span><span class="tr-l1"> [TOP→ROUTE]</span>  <span class="tr-ts">03:51:00</span>  strategy=rule  team=content_team  confidence=HIGH
  <span class="tr-l1">│</span>
  <span class="tr-l1">├─── [CONTENT TEAM]</span>  <span class="tr-ts">03:51:01</span>  <span class="tr-ok">[START]</span>   run_id=run_20250422_031  stage=research
  <span class="tr-l1">│   ├─</span><span class="tr-l2"> [SPEC:research]</span>  <span class="tr-ts">03:51:01</span>  <span class="tr-ok">[CALL]</span>    tokens_in=312   duration=4.1s  <span class="tr-ok">status=ok</span>
  <span class="tr-l1">│   ├─</span><span class="tr-l2"> [SPEC:outline]</span>   <span class="tr-ts">03:51:05</span>  <span class="tr-ok">[CALL]</span>    tokens_in=2104  duration=2.2s  <span class="tr-ok">status=ok</span>
  <span class="tr-l1">│   ├─</span><span class="tr-l2"> [SPEC:writer]</span>    <span class="tr-ts">03:51:07</span>  <span class="tr-ok">[CALL]</span>    tokens_in=2890  duration=6.8s  <span class="tr-ok">status=ok</span>
  <span class="tr-l1">│   ├─</span><span class="tr-l2"> [SPEC:editor]</span>    <span class="tr-ts">03:51:14</span>  <span class="tr-ok">[CALL]</span>    tokens_in=3401  duration=3.4s  <span class="tr-ok">status=ok</span>
  <span class="tr-l1">│   └─</span><span class="tr-l2"> [SPEC:qa]</span>        <span class="tr-ts">03:51:17</span>  <span class="tr-ok">[CALL]</span>    tokens_in=3850  duration=2.9s  <span class="tr-ok">status=ok</span>
  <span class="tr-l1">│</span>
  <span class="tr-l1">├─── [CONTENT TEAM]</span>  <span class="tr-ts">03:51:20</span>  <span class="tr-ok">[DONE]</span>    total=19.4s  total_tokens=12557
  <span class="tr-l0">│</span>
  <span class="tr-l0">├─</span><span class="tr-l1"> [TOP→CHECKPOINT]</span>  <span class="tr-ts">03:51:20</span>  <span class="tr-ok">[PAUSE]</span>   stage=pre_publish  awaiting_human_approval
  <span class="tr-l0">│</span>   <span class="tr-dim">... 4m 12s elapsed ...</span>
  <span class="tr-l0">├─</span><span class="tr-l1"> [TOP→RESUME]</span>     <span class="tr-ts">03:55:32</span>  <span class="tr-ok">[APPROVED]</span>  reviewer=julius@example.com</div>
</div>

<div class="highlight">

**The nesting is the trace.** Each level of indentation is a level of the call hierarchy: top-level → team → specialist. Every entry shares the same <code>run_id</code>. To debug any result, search for its run_id — the full nested trace collapses the entire multi-orchestrator call sequence into one readable document.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04 — CONTINUED</div>

## What Every Trace Entry Must Contain

A trace entry that omits any of these fields forces you to reconstruct information when debugging. Define the schema once in `logger.py` and enforce it across every orchestrator layer.

<table class="cheat-table">
  <thead>
    <tr><th>Field</th><th>Required at</th><th>Why it matters</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="mono">run_id</span></td>
      <td>Every entry, every layer</td>
      <td>The primary key for grouping a full multi-orchestrator trace. Without it, entries from concurrent runs mix together.</td>
    </tr>
    <tr>
      <td><span class="mono">level</span></td>
      <td>Every entry</td>
      <td>Which orchestrator layer produced this entry — <code>top</code>, <code>team</code>, or <code>specialist</code>. Determines the indentation and hierarchy in the trace viewer.</td>
    </tr>
    <tr>
      <td><span class="mono">actor</span></td>
      <td>Every entry</td>
      <td>The name of the orchestrator, team, or specialist that produced this log line. Combined with <code>level</code>, it uniquely identifies the source.</td>
    </tr>
    <tr>
      <td><span class="mono">event</span></td>
      <td>Every entry</td>
      <td>What happened — START, CALL, RESULT, PAUSE, APPROVE, DONE, ERROR. Structured vocab enables programmatic analysis.</td>
    </tr>
    <tr>
      <td><span class="mono">timestamp</span></td>
      <td>Every entry</td>
      <td>ISO 8601 with milliseconds. Enables duration calculation between any two entries in the trace without storing durations explicitly.</td>
    </tr>
    <tr>
      <td><span class="mono">tokens / duration</span></td>
      <td>CALL + RESULT entries</td>
      <td>Cost and latency attribution per specialist. Without per-call token counts, you cannot identify which specialist is responsible for a cost spike.</td>
    </tr>
  </tbody>
</table>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## What to Do When a Team Produces a Wrong or Incomplete Result

A wrong result is not always a crash. A team can complete its full pipeline, return <code>status="ok"</code>, and still produce output that is factually wrong, structurally incomplete, or misaligned with the original intent. Each condition has a specific recovery path.

<div class="recovery-stack">
  <div class="rs-row retry">
    <div class="rsr-num">1</div>
    <div class="rsr-condition">🔄 Contract violation — wrong schema shape</div>
    <div class="rsr-action">The team returned a structurally incorrect artifact — a field is missing or the wrong type. The problem is likely the specialist's system prompt or output format instruction. Retry once with a stricter format prompt.</div>
    <div class="rsr-verdict">→ retry once</div>
  </div>
  <div class="rs-row partial">
    <div class="rsr-num">2</div>
    <div class="rsr-condition">✂️ Incomplete — some stages skipped</div>
    <div class="rsr-action">The QA agent flagged missing sections. The team returned <code>status="flagged"</code> with a partial payload. The top level surfaces the partial result to the caller with the QA notes. Do not re-run the whole team — resume from the last saved artifact.</div>
    <div class="rsr-verdict">→ surface partial</div>
  </div>
  <div class="rs-row escalate">
    <div class="rsr-num">3</div>
    <div class="rsr-condition">🎭 Wrong domain — misrouted by intent parser</div>
    <div class="rsr-action">The Content Team ran but the task was actually a data analysis request. The wrong team ran to completion. Add this input to the routing test suite. Re-route to the correct team from the top level using the saved global context — no specialist work is reused.</div>
    <div class="rsr-verdict">→ re-route</div>
  </div>
  <div class="rs-row escalate">
    <div class="rsr-num">4</div>
    <div class="rsr-condition">🌫️ Plausible but factually wrong</div>
    <div class="rsr-action">The output passed schema validation and QA, but contains a factual error — a wrong statistic, a hallucinated citation. This is a silent failure. Surface to human review. Add a fact-check specialist to the team's pipeline to catch this class of error in future runs.</div>
    <div class="rsr-verdict">→ human review</div>
  </div>
  <div class="rs-row halt">
    <div class="rsr-num">5</div>
    <div class="rsr-condition">💥 Unrecoverable — team halted mid-run</div>
    <div class="rsr-action">The team's orchestrator exceeded retries or hit an unrecoverable error. The run state was saved before the last successful stage. Log the halt with the run_id and last good artifact path. Notify the operator. Do not auto-retry without understanding the root cause.</div>
    <div class="rsr-verdict">→ halt + notify</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05 — CONTINUED</div>

## The Recovery Decision Tree

Before taking any action on a wrong or incomplete result, ask these four questions in order. The answer to each one determines the next step.

<div class="walkthrough">
  <div class="wt-row">
    <div class="wr-num">Q1</div>
    <div class="wr-content">
      <div class="wrc-title">📋 &nbsp;Did the schema validate?</div>
      <div class="wrc-desc">Check whether the <code>TeamResponse</code> payload passes its Pydantic model. If no → the problem is structural. Retry with a stricter prompt. Do not proceed to Q2 until the schema is valid.</div>
      <div class="wrc-code">No → retry with stricter format prompt (once). Yes → proceed to Q2.</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">Q2</div>
    <div class="wr-content">
      <div class="wrc-title">🎯 &nbsp;Did the right team run?</div>
      <div class="wrc-desc">Check the trace — specifically the <code>[TOP→ROUTE]</code> entry. Did the routing decision match the user's actual intent? If no → the problem is routing, not team quality. Re-route to the correct team. The wrong team's output is discarded.</div>
      <div class="wrc-code">No → re-route using saved GlobalContext. Yes → proceed to Q3.</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">Q3</div>
    <div class="wr-content">
      <div class="wrc-title">📦 &nbsp;Is the output complete?</div>
      <div class="wrc-desc">Check whether all expected sections, fields, and artifacts are present. If no → surface the partial result with the QA notes. Resume from the last checkpoint rather than restarting. The completed stages do not re-run.</div>
      <div class="wrc-code">No → return partial status + resume from checkpoint. Yes → proceed to Q4.</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">Q4</div>
    <div class="wr-content">
      <div class="wrc-title">✅ &nbsp;Is the content correct?</div>
      <div class="wrc-desc">The schema is valid, the right team ran, and the output is complete — but the content itself is wrong. This is a quality failure, not a structural one. Surface to human review. Add the failure case to the team's QA rubric to prevent recurrence.</div>
      <div class="wrc-code">No → human review + update QA rubric. Yes → output is correct.</div>
    </div>
  </div>
</div>

---

## Quick Reference — Part 3 Control and Safety Rules

<table class="cheat-table">
  <thead>
    <tr><th>Concern</th><th>Rule</th><th>Where it lives</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Checkpoint placement</strong></td>
      <td>Before every irreversible or high-stakes action. Everything reversible runs autonomously.</td>
      <td><span class="mono">top_level/runner.py</span></td>
    </tr>
    <tr>
      <td><strong>Checkpoint implementation</strong></td>
      <td>Pause-and-persist. Save state, exit, resume via webhook. Never block a thread.</td>
      <td><span class="mono">save_run_state() + /api/runs/resume</span></td>
    </tr>
    <tr>
      <td><strong>Guardrail layering</strong></td>
      <td>Prompt → contract → code → scope → budget. Each layer catches what the layer above misses.</td>
      <td>System-wide</td>
    </tr>
    <tr>
      <td><strong>Monitoring alerts</strong></td>
      <td>Alert on: budget exceeded, run age > 3× median, retry count > MAX, error rate > 15%.</td>
      <td><span class="mono">monitoring/alerts.py</span></td>
    </tr>
    <tr>
      <td><strong>Trace structure</strong></td>
      <td>Every entry: run_id, level, actor, event, timestamp. CALL+RESULT entries: tokens, duration.</td>
      <td><span class="mono">logger.py</span></td>
    </tr>
    <tr>
      <td><strong>Recovery sequence</strong></td>
      <td>Q1: schema valid? Q2: right team? Q3: complete? Q4: content correct? Act on first "no".</td>
      <td>Operator runbook</td>
    </tr>
    <tr>
      <td><strong>Silent failure response</strong></td>
      <td>Valid schema + correct team + complete output + wrong content → human review + update QA rubric.</td>
      <td>QA specialist prompt</td>
    </tr>
  </tbody>
</table>

---

<!-- _class: final -->

# Visibility is not a feature. It is the architecture.

&nbsp;

*Checkpoint the irreversible. Enforce guardrails in code, not prompts. Trace every layer. Recover at the right stage.*

&nbsp;

Next: **Part 4 — Scaling, Evaluation, and What Comes Next.**

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*