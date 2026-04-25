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
  .e2e-row.dim   .er-artifact { opacity: 0.35; }

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

  /* ── Error strategy rows ── */
  .strategy-stack {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .ss-row {
    display: grid;
    grid-template-columns: 160px 1fr auto;
    align-items: stretch;
    border-bottom: 1px solid var(--border);
  }

  .ss-row:last-child { border-bottom: none; }

  .ss-row .sr-strategy {
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

  .ss-row .sr-desc {
    padding: 12px 14px;
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.6;
    display: flex;
    align-items: center;
  }

  .ss-row .sr-when {
    padding: 12px 14px;
    border-left: 1px solid var(--border);
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    display: flex;
    align-items: center;
    white-space: nowrap;
  }

  .ss-row.retry   .sr-when { background: #f0f9ff; color: #0369a1; }
  .ss-row.fallback .sr-when { background: var(--amber-light); color: #92400e; }
  .ss-row.halt    .sr-when { background: #fef2f2; color: #991b1b; }
  .ss-row.skip    .sr-when { background: #f0fdf4; color: #166534; }
  .ss-row.cache   .sr-when { background: #fdf4ff; color: #6b21a8; }

  /* ── Log anatomy ── */
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

  /* ── Artifact diff view ── */
  .artifact-chain {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .ac-row {
    display: grid;
    grid-template-columns: 32px 150px 1fr 130px;
    align-items: stretch;
    border-bottom: 1px solid var(--border);
  }

  .ac-row:last-child { border-bottom: none; }

  .ac-row .acr-num {
    background: var(--text);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .ac-row .acr-agent {
    padding: 10px 12px;
    font-weight: 600;
    font-size: 12px;
    color: var(--text);
    border-right: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 7px;
    background: var(--off-white);
  }

  .ac-row .acr-check {
    padding: 10px 14px;
    font-size: 12px;
    color: var(--muted);
    line-height: 1.55;
    display: flex;
    align-items: center;
  }

  .ac-row .acr-status {
    padding: 10px 12px;
    border-left: 1px solid var(--border);
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .ac-row.ok    .acr-status { background: #f0fdf4; color: #166534; }
  .ac-row.warn  .acr-status { background: #fffbeb; color: #92400e; }
  .ac-row.error .acr-status { background: #fef2f2; color: #991b1b; }
  .ac-row.error .acr-agent  { background: #fef2f2; border-left: 3px solid #ef4444; }
  .ac-row.error .acr-check  { background: #fef2f2; color: #7f1d1d; }

  /* ── CTA task grid ── */
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

<div class="series-badge">PIPELINE AGENTS · LEVEL 2 — PART 4 OF 4</div>

# Debugging and Failure Handling
## Reading artifacts, catching failures, keeping pipelines alive

&nbsp;

**A pipeline that never fails is a pipeline that never runs.** Knowing what to look for — and where — is the skill that separates fragile demos from production systems.

`artifacts` · `tracing` · `error handling` · `retry` · `failure modes` · `logging`

---

## Why Pipeline Debugging Is Different

Debugging a single agent is easy — one call, one response, one place to look. A pipeline multiplies the surface area. The failure you see is almost never where the failure happened.

<div class="matters-grid">
  <div class="matters-card">
    <div class="mcc-icon">🔗</div>
    <div>
      <div class="mcc-title">Errors propagate silently</div>
      <div class="mcc-desc">A wrong field in <code>research.json</code> doesn't crash the Writer — it just produces subtly wrong prose. By the time you read the output, the root cause is three stages upstream.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🎭</div>
    <div>
      <div class="mcc-title">Each agent has its own failure modes</div>
      <div class="mcc-desc">The Research agent fails differently from the QA agent. A JSON schema violation looks nothing like a timeout. You need a mental model for each stage, not just one generic "something broke."</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">📄</div>
    <div>
      <div class="mcc-title">Artifacts are the audit trail</div>
      <div class="mcc-desc">Because every stage saves to disk, you already have a log of what every agent produced. The debugging workflow isn't guesswork — it's reading the chain of artifacts in order and finding where the output first diverged.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">💸</div>
    <div>
      <div class="mcc-title">Retrying blindly is expensive</div>
      <div class="mcc-desc">Re-running a five-agent pipeline from scratch because stage 4 failed wastes tokens and time. Knowing which stage failed means re-running exactly that stage — using the saved artifact as the checkpoint.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Reading the Chain of Artifacts to Find Problems

When a pipeline produces wrong output, the artifacts tell you exactly where it went wrong. Read them in order — forward from the input, stopping at the first one that looks wrong.

<div class="artifact-chain">
  <div class="ac-row ok">
    <div class="acr-num">1</div>
    <div class="acr-agent">🔍 research.json</div>
    <div class="acr-check">Claims list is populated. Sources are real URLs. Confidence fields are present. <code>topic</code> and <code>audience</code> match the original input.</div>
    <div class="acr-status">✓ looks good</div>
  </div>
  <div class="ac-row ok">
    <div class="acr-num">2</div>
    <div class="acr-agent">🗂️ outline.json</div>
    <div class="acr-check">Section headings are present. Each section references valid claim IDs from <code>research.json</code>. No sections are empty or duplicated.</div>
    <div class="acr-status">✓ looks good</div>
  </div>
  <div class="ac-row error">
    <div class="acr-num">3</div>
    <div class="acr-agent">✍️ draft.md</div>
    <div class="acr-check">Headings don't match the outline. Two sections are missing. One section repeats a paragraph verbatim. The Writer received a malformed outline — not a writer problem.</div>
    <div class="acr-status">✗ first divergence</div>
  </div>
  <div class="ac-row warn">
    <div class="acr-num">4</div>
    <div class="acr-agent">✂️ edited.md</div>
    <div class="acr-check">Editor worked on the broken draft. Output is tighter prose of the wrong content. Symptom of stage 3 — not a new failure.</div>
    <div class="acr-status">⚠ downstream noise</div>
  </div>
  <div class="ac-row warn">
    <div class="acr-num">5</div>
    <div class="acr-agent">🔎 qa_report.json</div>
    <div class="acr-check">Multiple claim flags — because sections are missing. These flags are symptoms of stage 3, not real factual errors to fix.</div>
    <div class="acr-status">⚠ downstream noise</div>
  </div>
</div>

<div class="highlight">

**The rule:** Find the first artifact that diverges from its contract. Everything after it is noise. Fix stage 3 — not stages 4 and 5.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01 — CONTINUED</div>

## The Artifact Reading Checklist

For each saved artifact, ask these questions in order before moving to the next one.

<table class="cheat-table">
  <thead>
    <tr><th>Artifact</th><th>What to check first</th><th>Red flag</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="mono">research.json</span></td>
      <td>Is <code>claims</code> a non-empty list? Does each claim have an <code>id</code>, <code>text</code>, and <code>source</code>?</td>
      <td><code>claims: []</code> or <code>claims: null</code> — the whole pipeline runs on empty facts.</td>
    </tr>
    <tr>
      <td><span class="mono">outline.json</span></td>
      <td>Does each section reference valid claim IDs from research? Are all sections non-empty?</td>
      <td>Claim IDs in outline don't exist in research — Writer will hallucinate to fill the gap.</td>
    </tr>
    <tr>
      <td><span class="mono">draft.md</span></td>
      <td>Does heading count match <code>outline.json</code> section count? Is every section present?</td>
      <td>Fewer H2s than outline sections — the Writer silently dropped a section.</td>
    </tr>
    <tr>
      <td><span class="mono">edited.md</span></td>
      <td>Do all headings from <code>draft.md</code> still exist? Has the word count dropped by more than 20%?</td>
      <td>A heading disappeared — the Editor deleted a section instead of tightening it.</td>
    </tr>
    <tr>
      <td><span class="mono">qa_report.json</span></td>
      <td>Is <code>verdict</code> present? Are <code>flags</code> tied to real claim IDs that exist in research?</td>
      <td>Flags reference claim IDs not in research — QA is hallucinating citations to check.</td>
    </tr>
  </tbody>
</table>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## What Happens When One Agent Fails

There are three distinct failure types for a pipeline agent. Each one requires a different response — and a different place to look.

<div class="failure-grid">
  <div class="failure-card">
    <div class="fc-head">💥 &nbsp;Hard failure — exception raised</div>
    <div class="fc-body">The API call throws, the JSON parse fails, or Pydantic rejects the schema. The orchestrator stops. Nothing downstream runs. The artifact for this stage was never written.
      <div class="fc-fix">Check the stage's raw LLM output first. Then check the system prompt's format instruction. Then check the input it received.</div>
    </div>
  </div>
  <div class="failure-card">
    <div class="fc-head">👻 &nbsp;Silent failure — wrong output, no crash</div>
    <div class="fc-body">The agent returns a valid JSON object that passes schema validation — but the content is wrong. Missing claims, hallucinated sections, truncated text. The pipeline runs to completion with bad data.
      <div class="fc-fix">Silent failures only appear when you read the artifacts. This is why the artifact checklist exists.</div>
    </div>
  </div>
  <div class="failure-card">
    <div class="fc-head">⏱️ &nbsp;Timeout or rate limit</div>
    <div class="fc-body">Large context or high-concurrency runs hit token-per-minute limits or request timeouts. The call fails mid-stream. The artifact is either empty or truncated — both are worse than no artifact at all.
      <div class="fc-fix">Implement exponential backoff before retrying. Never retry immediately — it usually hits the same limit again.</div>
    </div>
  </div>
  <div class="failure-card">
    <div class="fc-head">🔀 &nbsp;Contract violation — valid JSON, wrong shape</div>
    <div class="fc-body">The model returns JSON, but with different key names, missing required fields, or wrong value types. Pydantic catches this if you validate. Without validation, it propagates silently to the next stage.
      <div class="fc-fix">Every handoff needs a <code>validate_*()</code> call. Contract violations should raise immediately, not quietly forward.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Error Handling Strategies

Every stage in the orchestrator needs an explicit strategy for what to do when it fails. Picking the right one depends on whether the stage is blocking, skippable, or retryable.

<div class="strategy-stack">
  <div class="ss-row retry">
    <div class="sr-strategy">🔄 &nbsp;Retry with backoff</div>
    <div class="sr-desc">Wait, then call the same agent again with the same input. Use for transient failures: timeouts, rate limits, network errors. Cap at 3 attempts before escalating.</div>
    <div class="sr-when">transient errors</div>
  </div>
  <div class="ss-row fallback">
    <div class="sr-strategy">🔁 &nbsp;Retry with a simpler prompt</div>
    <div class="sr-desc">The first call returned a contract violation. Resend with a stricter format instruction — e.g., "Return ONLY valid JSON, no markdown fences." One retry with a fixed prompt before halting.</div>
    <div class="sr-when">format violations</div>
  </div>
  <div class="ss-row skip">
    <div class="sr-strategy">⏭️ &nbsp;Skip and continue</div>
    <div class="sr-desc">Mark the stage as skipped in the run log and move forward with the previous artifact. Only valid for non-blocking stages — e.g., an optional SEO check that enhances but doesn't gate the pipeline.</div>
    <div class="sr-when">optional stages</div>
  </div>
  <div class="ss-row cache">
    <div class="sr-strategy">💾 &nbsp;Resume from last checkpoint</div>
    <div class="sr-desc">The stage after a saved artifact doesn't need to re-run the stages before it. Load the last valid artifact from disk and restart the pipeline from the next stage. Saves tokens and time.</div>
    <div class="sr-when">mid-run crashes</div>
  </div>
  <div class="ss-row halt">
    <div class="sr-strategy">🛑 &nbsp;Halt and surface</div>
    <div class="sr-desc">The stage has exhausted retries, or produced a critical contract violation with no fallback. Stop the pipeline, log the full error with the stage name and input artifact, and surface to the caller.</div>
    <div class="sr-when">unrecoverable errors</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03 — CONTINUED</div>

## Error Handling in Code — The Retry + Halt Pattern

<div class="code-block">
  <div class="cb-header">
    <div class="cb-dots">
      <div class="cb-dot red"></div>
      <div class="cb-dot yellow"></div>
      <div class="cb-dot green"></div>
    </div>
    <div class="cb-filename">orchestrator.py — retry with backoff, then halt</div>
  </div>
  <div class="cb-body"><span class="kw">import</span> <span class="va">time, logging</span>
    <span class="kw">from</span> <span class="va">pydantic</span> <span class="kw">import</span> <span class="va">ValidationError</span>
    <span class="kw">def</span> <span class="fn">run_with_retry</span>(<span class="va">agent_fn</span>, <span class="va">max_attempts</span>=<span class="nu">3</span>, <span class="va">backoff</span>=<span class="nu">2</span>, **<span class="va">kwargs</span>):
        <span class="kw">for</span> <span class="va">attempt</span> <span class="kw">in</span> <span class="bi">range</span>(<span class="nu">1</span>, <span class="va">max_attempts</span> + <span class="nu">1</span>):
            <span class="kw">try</span>:
                <span class="va">raw</span> = <span class="va">agent_fn</span>(**<span class="va">kwargs</span>)
                <span class="kw">return</span> <span class="va">raw</span>                        <span class="cm"># success — return immediately</span>
            <span class="kw">except</span> <span class="va">ValidationError</span> <span class="kw">as</span> <span class="va">e</span>:
                <span class="va">logging</span>.<span class="fn">warning</span>(<span class="st">f"[{agent_fn.__name__}] contract violation (attempt {attempt}): {e}"</span>)
                <span class="kw">if</span> <span class="va">attempt</span> == <span class="va">max_attempts</span>:
                    <span class="kw">raise</span> <span class="va">PipelineError</span>(<span class="st">f"{agent_fn.__name__} failed after {max_attempts} attempts"</span>) <span class="kw">from</span> <span class="va">e</span>
            <span class="kw">except</span> <span class="va">Exception</span> <span class="kw">as</span> <span class="va">e</span>:
                <span class="va">logging</span>.<span class="fn">warning</span>(<span class="st">f"[{agent_fn.__name__}] error (attempt {attempt}): {e}"</span>)
                <span class="kw">if</span> <span class="va">attempt</span> == <span class="va">max_attempts</span>:
                    <span class="kw">raise</span> <span class="va">PipelineError</span>(<span class="st">f"{agent_fn.__name__} unrecoverable"</span>) <span class="kw">from</span> <span class="va">e</span>
            <span class="va">time</span>.<span class="fn">sleep</span>(<span class="va">backoff</span> ** <span class="va">attempt</span>)   <span class="cm"># 2s → 4s → 8s exponential backoff</span></div>
    </div>

<div class="highlight">

**One wrapper, every agent.** Replace every bare `agent_fn()` call in the orchestrator with `run_with_retry(agent_fn, ...)`. All retry logic lives in one place — not copy-pasted into each stage. To change the retry count for all agents, change it once.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Logging Each Agent's Output for Traceability

A log entry per stage gives you a time-stamped record of exactly what each agent received, what it returned, and how long it took. Without this, debugging a failed overnight run means re-running the whole thing.

<div class="log-block">
  <div class="lb-header">
    <div class="lb-title">pipeline run log</div>
    <div class="lb-badge">pipeline.log</div>
  </div>
  <div class="lb-body"><span class="lg-ts">2025-04-22 03:14:01</span> <span class="lg-ok">[OK]</span>     <span class="lg-key">stage=</span><span class="lg-val">research</span>   <span class="lg-info">duration=4.2s  tokens_in=312  tokens_out=1847  artifact=research.json</span>
<span class="lg-ts">2025-04-22 03:14:06</span> <span class="lg-ok">[OK]</span>     <span class="lg-key">stage=</span><span class="lg-val">outline</span>    <span class="lg-info">duration=2.1s  tokens_in=2104 tokens_out=610   artifact=outline.json</span>
<span class="lg-ts">2025-04-22 03:14:09</span> <span class="lg-warn">[WARN]</span>  <span class="lg-key">stage=</span><span class="lg-val">writer</span>     <span class="lg-info">attempt=1 ValidationError: missing field 'sections[2].body'</span>
<span class="lg-ts">2025-04-22 03:14:11</span> <span class="lg-warn">[WARN]</span>  <span class="lg-key">stage=</span><span class="lg-val">writer</span>     <span class="lg-info">attempt=2 retrying with stricter format prompt…</span>
<span class="lg-ts">2025-04-22 03:14:16</span> <span class="lg-ok">[OK]</span>     <span class="lg-key">stage=</span><span class="lg-val">writer</span>     <span class="lg-info">duration=6.8s  tokens_in=2890 tokens_out=3201  artifact=draft.md</span>
<span class="lg-ts">2025-04-22 03:14:23</span> <span class="lg-ok">[OK]</span>     <span class="lg-key">stage=</span><span class="lg-val">editor</span>     <span class="lg-info">duration=3.4s  tokens_in=3401 tokens_out=2980  artifact=edited.md</span>
<span class="lg-ts">2025-04-22 03:14:27</span> <span class="lg-err">[ERROR]</span> <span class="lg-key">stage=</span><span class="lg-val">qa</span>         <span class="lg-info">attempt=3 PipelineError: qa agent unrecoverable — halting</span>
<span class="lg-ts">2025-04-22 03:14:27</span> <span class="lg-err">[HALT]</span>  <span class="lg-key">last_good_artifact=</span><span class="lg-val">edited.md</span>  <span class="lg-info">resume from stage 5 when fixed</span></div>
</div>

<div class="highlight">

**The last line is the most important one.** It tells you exactly where to resume: load <code>edited.md</code>, fix the QA agent, run only stage 5. Stages 1–4 produced valid artifacts — never re-run them.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04 — CONTINUED</div>

## The Minimal Log Entry — What to Record at Every Stage

<div class="walkthrough">
  <div class="wt-row">
    <div class="wr-num">1</div>
    <div class="wr-content">
      <div class="wrc-title">🏷️ &nbsp;Stage name and attempt number</div>
      <div class="wrc-desc">Always include which agent ran and which attempt this was. Without the attempt number, you can't tell a first-try success from a second-try recovery in the log.</div>
      <div class="wrc-code">stage="research"  attempt=1</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">2</div>
    <div class="wr-content">
      <div class="wrc-title">⏱️ &nbsp;Duration and token counts</div>
      <div class="wrc-desc">Wall-clock time per stage tells you where the pipeline is slow. Token counts tell you which stage is most expensive. Both matter for cost optimisation and latency profiling.</div>
      <div class="wrc-code">duration=4.2s  tokens_in=312  tokens_out=1847</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">3</div>
    <div class="wr-content">
      <div class="wrc-title">📄 &nbsp;Artifact path written</div>
      <div class="wrc-desc">Log the exact file path of the artifact that was saved. This is your checkpoint reference — if the run crashes later, this line tells you the last safe restart point.</div>
      <div class="wrc-code">artifact="artifacts/research.json"</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">4</div>
    <div class="wr-content">
      <div class="wrc-title">❌ &nbsp;Error type and message on failure</div>
      <div class="wrc-desc">Log the full exception class and message, not just "error." A <code>ValidationError</code> needs a different fix than a <code>TimeoutError</code> — and you want to know which one without re-running anything.</div>
      <div class="wrc-code">ValidationError: missing field 'claims[0].source'</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">5</div>
    <div class="wr-content">
      <div class="wrc-title">🔁 &nbsp;Last good artifact on halt</div>
      <div class="wrc-desc">When the pipeline halts, record which artifact was the last successfully written and validated one. This is the resume point — no guessing, no re-running earlier stages.</div>
      <div class="wrc-code">last_good_artifact="artifacts/edited.md"  resume_from=stage_5</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## Common Pipeline Failure Modes

These five failure modes account for the vast majority of pipeline problems in the wild. Each has a distinct symptom and a specific fix.

<div class="failure-grid">
  <div class="failure-card">
    <div class="fc-head">🌫️ &nbsp;Schema drift</div>
    <div class="fc-body">The model returns a key named <code>claim_list</code> instead of <code>claims</code>. Or <code>confidence: "medium"</code> instead of <code>"HIGH" | "LOW"</code>. Valid JSON — wrong shape. Passes string checks, fails Pydantic.
      <div class="fc-fix">Add <code>Literal</code> types and required field names to every Pydantic model. Treat unexpected keys as errors, not warnings.</div>
    </div>
  </div>
  <div class="failure-card">
    <div class="fc-head">📦 &nbsp;Truncated output</div>
    <div class="fc-body">The model hits its <code>max_tokens</code> limit mid-response and returns incomplete JSON. The parse succeeds if the truncation happens inside a string value — the worst case.
      <div class="fc-fix">Set <code>max_tokens</code> generously per stage based on expected output size. Log <code>stop_reason</code> — if it's <code>"max_tokens"</code>, the output is always incomplete.</div>
    </div>
  </div>
  <div class="failure-card">
    <div class="fc-head">🔄 &nbsp;Context contamination</div>
    <div class="fc-body">An agent receives too much upstream context — all five prior artifacts in one call — and starts confusing information between stages. The output blends sections from different artifacts.
      <div class="fc-fix">Each agent should receive only the artifact it needs. The Writer gets <code>outline.json</code> + <code>research.json</code>. Nothing more. Build a scoped <code>prepare_input()</code> function per agent.</div>
    </div>
  </div>
  <div class="failure-card">
    <div class="fc-head">📎 &nbsp;Markdown fence leakage</div>
    <div class="fc-body">The model wraps its JSON in <code>```json … ```</code>. Your <code>json.loads()</code> throws. The pipeline halts on a fixable, cosmetic issue. Happens on roughly 15–25% of calls depending on model and prompt.
      <div class="fc-fix">Always strip fences before parsing: <code>raw.strip().removeprefix("```json").removesuffix("```").strip()</code> — apply this to every agent's raw output, unconditionally.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05 — CONTINUED</div>

## The Last Common Failure Mode — Upstream Prompt Rot

The fifth failure mode is the slowest and hardest to catch: the system prompt silently stops working as the task evolves.

<div class="e2e-pipeline">
  <div class="e2e-row dim">
    <div class="er-num">1</div>
    <div class="er-agent">🔍 Research agent</div>
    <div class="er-task">Running correctly. Produces clean <code>research.json</code> with all required fields.</div>
    <div class="er-artifact">✓ research.json</div>
  </div>
  <div class="e2e-row dim">
    <div class="er-num">2</div>
    <div class="er-agent">🗂️ Outline agent</div>
    <div class="er-task">Running correctly. Produces valid <code>outline.json</code> — sections map to claim IDs.</div>
    <div class="er-artifact">✓ outline.json</div>
  </div>
  <div class="e2e-row focus">
    <div class="er-num">3</div>
    <div class="er-agent">✍️ Writer agent</div>
    <div class="er-task">Prompt was written for 800-word posts. Task scope changed to 2 500 words. The Writer now consistently drops the last two sections — not a crash, just quiet truncation. Passes validation.</div>
    <div class="er-artifact">⚠ draft.md</div>
  </div>
  <div class="e2e-row dim">
    <div class="er-num">4</div>
    <div class="er-agent">✂️ Editor agent</div>
    <div class="er-task">Edits the truncated draft. Produces clean output of incomplete content.</div>
    <div class="er-artifact">⚠ edited.md</div>
  </div>
  <div class="e2e-row dim">
    <div class="er-num">5</div>
    <div class="er-agent">🔎 QA agent</div>
    <div class="er-task">Flags missing sections as factual gaps. Multiple flags — all symptoms of stage 3.</div>
    <div class="er-artifact">⚠ qa_report.json</div>
  </div>
</div>

<div class="highlight">

**Prompt rot fix:** Each agent's system prompt should include the expected output size constraint explicitly — e.g., <code>"Write all sections in outline.json. Do not stop until every section is complete."</code> When task scope changes, update the prompt. Treat prompts like code — version them.

</div>

---

<!-- _class: cta -->

## Your Assignment — Map a Manual Task to a Pipeline

You've finished Level 2. The only move left is to take something you do by hand and draw the assembly line.

<div class="cta-task-grid">
  <div class="cta-card">
    <div class="ctac-icon">📊</div>
    <div class="ctac-title">If you work with reports</div>
    <div class="ctac-desc">Pick a report you assemble manually from multiple sources. Map each collection and synthesis step to one agent.</div>
    <div class="ctac-steps">
      <div class="ctac-step">collect.py → raw_data.json</div>
      <div class="ctac-step">summarise.py → summaries.json</div>
      <div class="ctac-step">format.py → report.md</div>
    </div>
  </div>
  <div class="cta-card">
    <div class="ctac-icon">📬</div>
    <div class="ctac-title">If you work with email</div>
    <div class="ctac-desc">Pick a type of email thread you triage manually — support tickets, leads, updates. Map triage, classify, draft reply to three agents.</div>
    <div class="ctac-steps">
      <div class="ctac-step">triage.py → classified.json</div>
      <div class="ctac-step">context.py → context.json</div>
      <div class="ctac-step">draft.py → reply.txt</div>
    </div>
  </div>
  <div class="cta-card">
    <div class="ctac-icon">🔍</div>
    <div class="ctac-title">If you work with research</div>
    <div class="ctac-desc">Pick a topic you research manually before writing. Separate the gathering, the structuring, and the writing into three independent agents.</div>
    <div class="ctac-steps">
      <div class="ctac-step">gather.py → sources.json</div>
      <div class="ctac-step">outline.py → outline.json</div>
      <div class="ctac-step">write.py → draft.md</div>
    </div>
  </div>
</div>

<p style="font-size:15px; color:#78716c; margin-top: 4px;">The constraint is the point: <strong>draw the pipeline first.</strong> Name every artifact before writing a single agent. If you can't name the artifact, the stage isn't ready to be built.</p>

---

<!-- _class: final -->

# Artifacts don't lie. Prompts rot. Logs save you.

&nbsp;

*Read the chain. Find the first divergence. Fix that stage only.*

&nbsp;

**You've completed Level 2 — Pipeline Agents.**

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*