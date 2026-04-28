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

  /* ── Framework table ── */
  .framework-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 12.5px;
    margin: 14px 0;
  }

  .framework-table th {
    background: var(--text);
    color: white;
    padding: 9px 14px;
    text-align: left;
    font-weight: 500;
    font-size: 11px;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.07em;
  }

  .framework-table td {
    padding: 10px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
    font-size: 12.5px;
    vertical-align: top;
    line-height: 1.55;
  }

  .framework-table tr:last-child td { border-bottom: none; }
  .framework-table tr:nth-child(even) td { background: var(--off-white); }
  .framework-table .tag {
    display: inline-block;
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    font-weight: 700;
    padding: 2px 7px;
    border-radius: 3px;
    white-space: nowrap;
  }
  .framework-table .tag.good { background: #f0fdf4; color: #166534; }
  .framework-table .tag.warn { background: var(--amber-light); color: #92400e; }
  .framework-table .tag.bad  { background: #fef2f2; color: #991b1b; }

  /* ── Checklist stack ── */
  .checklist-stack {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .cl-row {
    display: grid;
    grid-template-columns: 36px 1fr auto;
    align-items: stretch;
    border-bottom: 1px solid var(--border);
  }

  .cl-row:last-child { border-bottom: none; }

  .cl-row .clr-num {
    background: var(--text);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .cl-row .clr-question {
    padding: 11px 14px;
    font-size: 12.5px;
    color: var(--text);
    line-height: 1.55;
    display: flex;
    align-items: center;
  }

  .cl-row .clr-verdict {
    padding: 11px 13px;
    border-left: 1px solid var(--border);
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    display: flex;
    align-items: center;
    white-space: nowrap;
  }

  .cl-row.pass   .clr-verdict { background: #f0fdf4; color: #166534; }
  .cl-row.fail   .clr-verdict { background: #fef2f2; color: #991b1b; }
  .cl-row.warn   .clr-verdict { background: var(--amber-light); color: #92400e; }
  .cl-row.gate   .clr-verdict { background: #fdf4ff; color: #6b21a8; }

  /* ── Pipeline flow ── */
  .pipeline-flow {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .pf-row {
    display: grid;
    grid-template-columns: 36px 160px 1fr auto;
    align-items: stretch;
    border-bottom: 1px solid var(--border);
  }

  .pf-row:last-child { border-bottom: none; }

  .pf-row .pfr-num {
    background: var(--text);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }

  .pf-row .pfr-team {
    padding: 11px 13px;
    font-weight: 600;
    font-size: 12px;
    color: var(--text);
    border-right: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 7px;
    line-height: 1.4;
    background: var(--off-white);
  }

  .pf-row .pfr-action {
    padding: 11px 14px;
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.6;
    display: flex;
    align-items: center;
  }

  .pf-row .pfr-output {
    padding: 11px 13px;
    border-left: 1px solid var(--border);
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    display: flex;
    align-items: center;
    white-space: nowrap;
  }

  .pf-row.content  .pfr-output { background: #f0f9ff; color: #0369a1; }
  .pf-row.eng      .pfr-output { background: #f0fdf4; color: #166534; }
  .pf-row.router   .pfr-output { background: var(--amber-light); color: #92400e; }
  .pf-row.done     .pfr-output { background: #fdf4ff; color: #6b21a8; }

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

<div class="series-badge">AGENT TEAMS · LEVEL 4 — PART 4 OF 4</div>

# Scaling Decisions and Full Example
## Frameworks vs raw Python, the cost of complexity, and a complete end-to-end walkthrough

&nbsp;

**Building a team is easy. Knowing when not to is the real skill.** This part gives you the decision frameworks, the scaling checklist, and a live example before you write a single line of code.

`crewai` · `langgraph` · `raw-python` · `scaling-checklist` · `end-to-end`

---

## The Framework Decision: CrewAI, LangGraph, or Raw Python

You have three serious options at team scale. Each imposes a different mental model. Pick the wrong one and you spend more time fighting the framework than building the system.

<table class="framework-table">
  <thead>
    <tr>
      <th>FRAMEWORK</th>
      <th>MENTAL MODEL</th>
      <th>BEST FOR</th>
      <th>WATCH OUT FOR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>CrewAI</strong></td>
      <td>Role-based crews with tasks and delegation</td>
      <td>Structured pipelines, clear roles, fast prototyping</td>
      <td><span class="tag warn">OPAQUE</span> Magic delegation hides routing logic; hard to debug</td>
    </tr>
    <tr>
      <td><strong>LangGraph</strong></td>
      <td>Explicit state machine with nodes and edges</td>
      <td>Complex conditional flows, loops, human-in-the-loop</td>
      <td><span class="tag warn">VERBOSE</span> Graph wiring overhead before you see any output</td>
    </tr>
    <tr>
      <td><strong>Raw Python</strong></td>
      <td>Plain functions, queues, and API calls</td>
      <td>Full control, custom orchestration, production systems</td>
      <td><span class="tag bad">NO RAILS</span> You rebuild every abstraction from scratch</td>
    </tr>
  </tbody>
</table>

> **The honest rule:** start raw. Add a framework only when you hit a concrete problem the framework solves — not because you expect to need it.

---

## Framework Trade-offs at Team Scale

As agent count grows, the trade-offs sharpen. A framework that feels lightweight at two agents can become a cage at eight.

<div class="matters-grid">
  <div class="matters-card">
    <div class="mcc-icon">🧩</div>
    <div>
      <div class="mcc-title">CrewAI — role abstraction hides wiring</div>
      <div class="mcc-desc">Defining a <code>Researcher</code> and a <code>Writer</code> feels natural. But when the writer needs to loop back to the researcher with follow-up questions, the framework's sequential task model starts to resist you. Workarounds accumulate.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🔀</div>
    <div>
      <div class="mcc-title">LangGraph — graph gives you loops for free</div>
      <div class="mcc-desc">Every node is explicit. Every edge is intentional. Conditional branching and retry loops are first-class. The cost is upfront verbosity — a simple two-agent handoff is 40 lines before it runs.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🔧</div>
    <div>
      <div class="mcc-title">Raw Python — you own every failure mode</div>
      <div class="mcc-desc">No magic. A wrong routing decision is your function returning the wrong string. A retry is a <code>for</code> loop. This is also the only option where you can instrument exactly what you need without fighting the framework's telemetry model.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">📦</div>
    <div>
      <div class="mcc-title">The migration trap</div>
      <div class="mcc-desc">Teams that prototype in CrewAI and migrate to raw Python for production spend two weeks on the migration. Teams that prototype in raw Python and later wrap with LangGraph for a specific feature spend two hours. Start simple.</div>
    </div>
  </div>
</div>

---

## The Cost of Complexity: Why Teams Are a Last Resort

Every agent you add to a system is a multiplier — on latency, on cost, on debugging surface, and on the number of ways it can fail silently.

<div class="compare-grid">
  <div class="cg-card bad">
    <div class="cg-head">❌ What people assume about teams</div>
    <div class="cg-body">
      More agents means more parallelism, which means faster results. Specialists outperform generalists, so splitting roles always wins. The framework handles coordination — I just define the agents.
    </div>
  </div>
  <div class="cg-card good">
    <div class="cg-head">✅ What actually happens at runtime</div>
    <div class="cg-body">
      Coordination overhead adds latency at every handoff. A well-prompted single agent often matches a three-agent team for structured tasks. Frameworks hide the complexity — they don't remove it.
    </div>
  </div>
</div>

<div class="highlight">
  <strong>The complexity tax:</strong> a two-agent pipeline has one handoff to get wrong. A five-agent pipeline has four. Each handoff is a prompt boundary — context gets lost, format assumptions break, and errors compound before any single agent notices. Every team member is also a new point of cost.
</div>

---

## When Complexity Actually Pays Off

Teams are not always wrong. They are wrong when added prematurely. There are clear signals that justify the investment.

<div class="walkthrough">
  <div class="wt-row">
    <div class="wr-num">1</div>
    <div class="wr-content">
      <div class="wrc-title">⚡ True parallelism on independent subtasks</div>
      <div class="wrc-desc">If you can split a task into N parts with no shared state between them, running N agents in parallel cuts wall-clock time by N. This is the only case where teams give you a speed gain that a single agent cannot match.</div>
      <div class="wrc-code">content_agent || research_agent || code_agent → merge</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">2</div>
    <div class="wr-content">
      <div class="wrc-title">🎯 Context windows that genuinely won't fit</div>
      <div class="wrc-desc">A single agent processing a 200-page codebase to produce a migration plan will degrade in quality. Routing subsections to specialist agents and aggregating outputs is architecturally sound — but only when you've confirmed the window is the actual bottleneck.</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">3</div>
    <div class="wr-content">
      <div class="wrc-title">🔁 Critic loops that require genuine separation</div>
      <div class="wrc-desc">An agent critiquing its own output in the same context has a well-documented bias toward self-validation. A second agent with no shared context history produces meaningfully different feedback. This justifies the handoff cost.</div>
      <div class="wrc-code">writer_agent → critic_agent (clean context) → revision</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">4</div>
    <div class="wr-content">
      <div class="wrc-title">🏛️ Domain tools that cannot coexist in one agent</div>
      <div class="wrc-desc">If your writing agent needs no code execution access and your engineering agent needs a full shell, separate agents enforce a meaningful security boundary. This is an architecture reason, not a capability reason.</div>
    </div>
  </div>
</div>

---

## Scaling Checklist: Questions to Answer Before You Build

Print this. Answer every question. If you hit a STOP, a team is probably not your next move.

<div class="checklist-stack">
  <div class="cl-row pass">
    <div class="clr-num">1</div>
    <div class="clr-question"><strong>Have you confirmed a single well-prompted agent can't do this?</strong> Run the best single-agent version first. Measure quality. Only proceed if it fails on a specific, nameable dimension.</div>
    <div class="clr-verdict">✓ REQUIRED</div>
  </div>
  <div class="cl-row pass">
    <div class="clr-num">2</div>
    <div class="clr-question"><strong>Can you draw the data flow without guessing?</strong> Every agent's inputs and outputs should be specifiable as a typed schema before writing any code. Ambiguous handoffs become runtime failures.</div>
    <div class="clr-verdict">✓ REQUIRED</div>
  </div>
  <div class="cl-row warn">
    <div class="clr-num">3</div>
    <div class="clr-question"><strong>What happens when agent N fails mid-pipeline?</strong> Name the recovery path. If the answer is "restart from the top," your pipeline has no checkpoints and every failure is expensive.</div>
    <div class="clr-verdict">⚠ DESIGN FIRST</div>
  </div>
  <div class="cl-row warn">
    <div class="clr-num">4</div>
    <div class="clr-question"><strong>What is the worst-case token cost of a full run?</strong> Count every agent call, every tool call, every retry. If you can't estimate within 2×, your pipeline isn't well-defined enough to build.</div>
    <div class="clr-verdict">⚠ ESTIMATE FIRST</div>
  </div>
  <div class="cl-row fail">
    <div class="clr-num">5</div>
    <div class="clr-question"><strong>Are you adding agents because it feels more powerful?</strong> Architectural intuition is not a reason. Teams feel impressive. They are not inherently better. If this is your reason, stop and simplify.</div>
    <div class="clr-verdict">✗ STOP</div>
  </div>
  <div class="cl-row gate">
    <div class="clr-num">6</div>
    <div class="clr-question"><strong>Do you have observability in place before the first real run?</strong> Logs, trace IDs, per-agent cost tracking. If you build the team first and add monitoring later, you will debug blind on the first failure.</div>
    <div class="clr-verdict">🔒 GATE</div>
  </div>
</div>

---

## Full Example: One Prompt, Two Teams

**Scenario:** A solopreneur types one prompt — *"launch post for my new Python course"* — into an orchestrator. Two teams activate in parallel: a **Content Team** and an **Engineering Team**. Here is the full pipeline from prompt to artifact.

<div class="pipeline-flow">
  <div class="pf-row router">
    <div class="pfr-num">0</div>
    <div class="pfr-team">🧠 Top Orchestrator</div>
    <div class="pfr-action">Receives the user prompt. Classifies intent as requiring both content production and landing page deployment. Spawns Content Team and Engineering Team in parallel with shared <code>run_id</code>.</div>
    <div class="pfr-output">ROUTER</div>
  </div>
  <div class="pf-row content">
    <div class="pfr-num">1</div>
    <div class="pfr-team">✍️ Content Team</div>
    <div class="pfr-action">Content Orchestrator receives brief. Researcher agent pulls audience insights and course topic context. Writer agent drafts Substack post + LinkedIn carousel copy. Critic agent reviews tone and CTA strength. Output: reviewed draft bundle.</div>
    <div class="pfr-output">CONTENT</div>
  </div>
  <div class="pf-row eng">
    <div class="pfr-num">2</div>
    <div class="pfr-team">⚙️ Engineering Team</div>
    <div class="pfr-action">Eng Orchestrator receives brief. Scaffolder agent generates landing page HTML from brand template. Tester agent validates links and responsive layout. Deployer agent pushes to GitHub Pages via API. Output: live URL + deploy log.</div>
    <div class="pfr-output">ENGINEERING</div>
  </div>
  <div class="pf-row done">
    <div class="pfr-num">3</div>
    <div class="pfr-team">🔗 Merge Layer</div>
    <div class="pfr-action">Top orchestrator waits for both teams to emit a <code>DONE</code> signal. Injects the live URL into the content draft as the CTA link. Packages final output: Substack draft, carousel copy, and landing page URL.</div>
    <div class="pfr-output">FINAL OUTPUT</div>
  </div>
</div>

---

## Inside the Content Team: Step by Step

<div class="walkthrough">
  <div class="wt-row">
    <div class="wr-num">1</div>
    <div class="wr-content">
      <div class="wrc-title">📥 Content Orchestrator receives brief</div>
      <div class="wrc-desc">Receives <code>{ run_id, intent: "launch_post", topic: "Python course", audience: "self-improvers" }</code> from the top orchestrator. Validates schema. Initialises shared state dict.</div>
      <div class="wrc-code">state = { run_id, brief, stage: "research" }</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">2</div>
    <div class="wr-content">
      <div class="wrc-title">🔍 Researcher agent pulls context</div>
      <div class="wrc-desc">Queries the voice document and content framework files. Returns a structured context block: audience pain points, tone guidelines, relevant prior posts. Appends to shared state.</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">3</div>
    <div class="wr-content">
      <div class="wrc-title">✍️ Writer agent drafts outputs</div>
      <div class="wrc-desc">Receives brief + context. Produces two artefacts: a 600-word Substack post and a 7-slide LinkedIn carousel script. Both scoped to the voice document. No hallucinated claims — sourced only from context.</div>
      <div class="wrc-code">output = { substack_draft, carousel_slides }</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">4</div>
    <div class="wr-content">
      <div class="wrc-title">🧪 Critic agent reviews and scores</div>
      <div class="wrc-desc">Fresh context. Receives only the draft outputs and a rubric: voice alignment, CTA clarity, hook strength. Returns a score and a list of specific revision instructions. If score &lt; 7, the writer loops once.</div>
      <div class="wrc-code">{ score: 8.2, revisions: [], status: "APPROVED" }</div>
    </div>
  </div>
</div>

---

## Inside the Engineering Team: Step by Step

<div class="walkthrough">
  <div class="wt-row">
    <div class="wr-num">1</div>
    <div class="wr-content">
      <div class="wrc-title">📥 Eng Orchestrator receives brief</div>
      <div class="wrc-desc">Receives the same <code>run_id</code> and a deploy spec: course title, pricing tier, CTA text placeholder. Validates that the brand template exists in the asset store before proceeding.</div>
      <div class="wrc-code">assert template_exists("landing_v2") → True</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">2</div>
    <div class="wr-content">
      <div class="wrc-title">🏗️ Scaffolder agent generates landing page</div>
      <div class="wrc-desc">Injects course metadata into the brand HTML template. Fills headline, sub-headline, feature list, and a <code>CTA_URL_PLACEHOLDER</code> token. Does not generate free-form HTML — works strictly from the template.</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">3</div>
    <div class="wr-content">
      <div class="wrc-title">🧪 Tester agent validates output</div>
      <div class="wrc-desc">Runs a headless browser check: all internal links resolve, layout passes 375px and 1280px breakpoints, no missing alt attributes. Returns pass/fail per check. On any failure, patches and re-validates once.</div>
      <div class="wrc-code">{ links: PASS, responsive: PASS, a11y: PASS }</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">4</div>
    <div class="wr-content">
      <div class="wrc-title">🚀 Deployer agent pushes to GitHub Pages</div>
      <div class="wrc-desc">Commits validated HTML to the <code>gh-pages</code> branch via GitHub API. Polls deployment status until live URL is confirmed. Emits <code>{ status: "DONE", url }</code> back to the top orchestrator.</div>
      <div class="wrc-code">url = "julius.dev/python-course" → LIVE</div>
    </div>
  </div>
</div>

---

## The Merge: What the Top Orchestrator Does Last

<div class="checkpoint-flow">
  <div class="cpf-row auto">
    <div class="cpfr-num">1</div>
    <div class="cpfr-stage">⏳ Await signals</div>
    <div class="cpfr-action">Top orchestrator holds open two futures: <code>content_team.done</code> and <code>eng_team.done</code>. Uses <code>asyncio.gather</code> — neither team blocks the other. Timeout set at 120s per team.</div>
    <div class="cpfr-type">AUTO</div>
  </div>
  <div class="cpf-row auto">
    <div class="cpfr-num">2</div>
    <div class="cpfr-stage">🔗 Inject URL into draft</div>
    <div class="cpfr-action">Replaces <code>CTA_URL_PLACEHOLDER</code> in the Substack draft and carousel slide 7 with the confirmed live URL from the Engineering Team output. One string replace — no re-generation.</div>
    <div class="cpfr-type">AUTO</div>
  </div>
  <div class="cpf-row staged">
    <div class="cpfr-num">3</div>
    <div class="cpfr-stage">📦 Package final output</div>
    <div class="cpfr-action">Produces a single output envelope: <code>{ substack_draft, carousel_slides, landing_url, run_id, total_tokens, elapsed_ms }</code>. Writes to output store with the shared <code>run_id</code> as the key.</div>
    <div class="cpfr-type">STAGED</div>
  </div>
  <div class="cpf-row human">
    <div class="cpfr-num">4</div>
    <div class="cpfr-stage">👤 Human review gate</div>
    <div class="cpfr-action">Output is surfaced to the user. Nothing has been published. The Substack draft requires a manual "Schedule" click. The landing page is live but the CTA only goes live after the post is published. Human stays in control of the moment of release.</div>
    <div class="cpfr-type">HUMAN</div>
  </div>
</div>

---

## What the Trace Looks Like

<div class="trace-block">
  <div class="tb-header">
    <span class="tb-title">FULL RUN TRACE — run_id: cs-launch-0041</span>
    <span class="tb-badge">4 agents · 2 teams · 1 orchestrator</span>
  </div>
  <div class="tb-body"><span class="tr-ts">[00:00]</span> <span class="tr-l0">TOP_ORCHESTRATOR</span>  prompt received → intent classified
<span class="tr-ts">[00:01]</span> <span class="tr-l0">TOP_ORCHESTRATOR</span>  spawning content_team + eng_team (parallel)
<span class="tr-dim">──────────────────────────────────────────────────────</span>
<span class="tr-ts">[00:02]</span> <span class="tr-l1">  CONTENT_ORCH</span>      brief validated → state init
<span class="tr-ts">[00:03]</span> <span class="tr-l2">    RESEARCHER</span>       context pulled → 1,840 tokens
<span class="tr-ts">[00:07]</span> <span class="tr-l2">    WRITER</span>           substack draft → 620 words
<span class="tr-ts">[00:08]</span> <span class="tr-l2">    WRITER</span>           carousel copy → 7 slides
<span class="tr-ts">[00:12]</span> <span class="tr-l2">    CRITIC</span>           score: 8.2 → <span class="tr-ok">APPROVED</span>
<span class="tr-ts">[00:12]</span> <span class="tr-l1">  CONTENT_ORCH</span>      <span class="tr-ok">DONE</span> → emitting to top
<span class="tr-dim">──────────────────────────────────────────────────────</span>
<span class="tr-ts">[00:02]</span> <span class="tr-l1">  ENG_ORCH</span>          deploy spec validated → template found
<span class="tr-ts">[00:03]</span> <span class="tr-l3">    SCAFFOLDER</span>       HTML generated from template
<span class="tr-ts">[00:06]</span> <span class="tr-l3">    TESTER</span>           links PASS · responsive PASS · a11y PASS
<span class="tr-ts">[00:10]</span> <span class="tr-l3">    DEPLOYER</span>         pushed → polling gh-pages...
<span class="tr-ts">[00:14]</span> <span class="tr-l3">    DEPLOYER</span>         <span class="tr-ok">LIVE</span> → julius.dev/python-course
<span class="tr-ts">[00:14]</span> <span class="tr-l1">  ENG_ORCH</span>          <span class="tr-ok">DONE</span> → emitting url to top
<span class="tr-dim">──────────────────────────────────────────────────────</span>
<span class="tr-ts">[00:15]</span> <span class="tr-l0">TOP_ORCHESTRATOR</span>  both teams done → injecting url → packaging
<span class="tr-ts">[00:15]</span> <span class="tr-l0">TOP_ORCHESTRATOR</span>  output written → awaiting human review</div>
</div>

---

## Cost Reality Check for This Run

Before you build, know what it costs. This example is intentionally lean — every agent call is scoped to do exactly one thing.

<table class="framework-table">
  <thead>
    <tr>
      <th>AGENT</th>
      <th>INPUT TOKENS</th>
      <th>OUTPUT TOKENS</th>
      <th>CALLS</th>
      <th>NOTES</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Researcher</strong></td>
      <td>~2,400</td>
      <td>~800</td>
      <td>1</td>
      <td>Context window bounded by voice doc + framework files only</td>
    </tr>
    <tr>
      <td><strong>Writer</strong></td>
      <td>~3,200</td>
      <td>~1,400</td>
      <td>1</td>
      <td>Produces two artefacts in one call — not two separate calls</td>
    </tr>
    <tr>
      <td><strong>Critic</strong></td>
      <td>~2,000</td>
      <td>~300</td>
      <td>1</td>
      <td>Rubric-based structured output — short response by design</td>
    </tr>
    <tr>
      <td><strong>Scaffolder</strong></td>
      <td>~1,200</td>
      <td>~900</td>
      <td>1</td>
      <td>Template fill — not free-form generation</td>
    </tr>
    <tr>
      <td><strong>Tester</strong></td>
      <td>~600</td>
      <td>~200</td>
      <td>1</td>
      <td>Tool calls to headless browser — not LLM judgement</td>
    </tr>
    <tr>
      <td><strong>Deployer</strong></td>
      <td>~400</td>
      <td>~100</td>
      <td>1</td>
      <td>API call wrapper — nearly zero token cost</td>
    </tr>
  </tbody>
</table>

<div class="highlight">
  <strong>Total: ~13,000 tokens across 6 agent calls.</strong> At Sonnet pricing, this run costs under $0.05. A single bloated orchestrator prompt that tried to do all of this would cost more and hallucinate more. Scoping works.
</div>

---

## The Four Things That Make This System Work

The example above is not just a list of agents. It works because four structural decisions were made before a single agent was defined.

<div class="matters-grid">
  <div class="matters-card">
    <div class="mcc-icon">🪪</div>
    <div>
      <div class="mcc-title">Shared run_id across all agents</div>
      <div class="mcc-desc">Every agent call tags its logs, outputs, and errors with the same <code>run_id</code>. When something fails, you trace the entire run in one query. Without this, parallel teams produce orphaned logs you cannot join.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🔖</div>
    <div>
      <div class="mcc-title">Typed handoffs, not string passing</div>
      <div class="mcc-desc">Every inter-agent message is a validated dict with known keys. The writer does not receive a prose summary of the research — it receives a structured object. Schema validation at each boundary catches format errors before they propagate.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🧱</div>
    <div>
      <div class="mcc-title">Placeholder tokens, not re-generation</div>
      <div class="mcc-desc">The URL was not known when the content was written. Instead of re-running the writer with the URL, a <code>CTA_URL_PLACEHOLDER</code> token was injected at merge time. This keeps agent calls idempotent and eliminates a whole class of re-generation cost.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🔐</div>
    <div>
      <div class="mcc-title">Human gate before any public action</div>
      <div class="mcc-desc">The landing page was deployed but not promoted. The post was drafted but not scheduled. The agent team completed its work entirely within a staging state. The human's single action — pressing "Schedule" — is the only irreversible step.</div>
    </div>
  </div>
</div>

---

## What to Do Before Writing a Single Line of Code

This is the only CTA in this series. It is not "try the code." It is "do this thinking first."

<div class="walkthrough">
  <div class="wt-row">
    <div class="wr-num">1</div>
    <div class="wr-content">
      <div class="wrc-title">🗺️ Map your workflow as a data flow diagram</div>
      <div class="wrc-desc">Draw every input, every transformation, every output. Label the data type at each arrow. If you cannot draw this in under ten minutes, the problem is not yet well-enough defined to be automated.</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">2</div>
    <div class="wr-content">
      <div class="wrc-title">✂️ Identify every natural boundary</div>
      <div class="wrc-desc">Where does the work change domain? Where does context need to be isolated? Where would a specialist human hand off to another specialist? These are your agent boundaries — not arbitrary role names.</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">3</div>
    <div class="wr-content">
      <div class="wrc-title">🔢 Count the minimum viable agents</div>
      <div class="wrc-desc">Start with the fewest agents that cover the boundaries you found. If you have five agents on your first draft, challenge each one: can this merge with its neighbour without context window problems?</div>
      <div class="wrc-code">target: fewest agents, not most agents</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">4</div>
    <div class="wr-content">
      <div class="wrc-title">💀 Name every failure mode before day one</div>
      <div class="wrc-desc">For each agent, answer: what does it do when the upstream output is malformed? What is the retry strategy? What is the escalation path? Write these as comments in your architecture doc before writing a function signature.</div>
    </div>
  </div>
</div>

---

<!-- _class: final -->

# Map First. Build Second.

**The teams that scale are the ones that were designed — not the ones that grew.**

&nbsp;

Every agent you add should answer a concrete question: *which specific failure or limitation in the previous system does this agent fix?*

&nbsp;

If the answer is "it feels more capable," that is not an answer.

&nbsp;

*Design the architecture. Validate the boundaries. Then write the first line.*

&nbsp;

**`agent-teams` · `level-4` · `part-4-of-4`**