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
  .vs-side.single   { background: var(--off-white); }
  .vs-side.pipeline { background: #fffbeb; }

  .vs-side .vs-label {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.09em;
    margin-bottom: 8px;
  }

  .vs-side.single   .vs-label { color: var(--muted); }
  .vs-side.pipeline .vs-label { color: #92400e; }

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
  .vs-side.pipeline .vs-item { border-bottom-color: #fde68a; color: var(--text); }
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

  /* ── Assembly line compare ── */
  .assembly-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 14px 0;
  }

  .assembly-side {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .assembly-side .as-head {
    padding: 10px 16px;
    font-weight: 600;
    font-size: 13px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border);
  }

  .assembly-side.factory .as-head { background: #f0f9ff;           color: #0c4a6e; border-color: #bae6fd; }
  .assembly-side.agents  .as-head { background: var(--amber-light); color: #92400e; border-color: #fde68a; }

  .assembly-side .as-body {
    padding: 14px 16px;
    background: var(--white);
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .as-step {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 8px 10px;
    border-radius: 6px;
    line-height: 1.5;
  }

  .as-step .ass-icon { font-size: 17px; flex-shrink: 0; margin-top: 2px; }
  .as-step .ass-role { font-weight: 600; font-size: 12.5px; display: block; color: var(--text); }
  .as-step .ass-does { font-size: 12px; color: var(--muted); }

  .as-step.s1 { background: #f0f9ff; }
  .as-step.s2 { background: #f0fdf4; }
  .as-step.s3 { background: #fdf4ff; }
  .as-step.s4 { background: var(--amber-light); }

  .as-arrow {
    text-align: center;
    font-size: 12px;
    color: var(--muted);
    padding: 1px 10px;
    font-family: 'DM Mono', monospace;
  }

  /* ── SRP grid ── */
  .srp-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .srp-col { padding: 18px 20px; }
  .srp-col + .srp-col { border-left: 1px solid var(--border); }
  .srp-col.violated { background: #fef2f2; }
  .srp-col.applied  { background: #f0fdf4; }

  .srp-col .sc-label {
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

  .srp-col.violated .sc-label { color: #991b1b; }
  .srp-col.applied  .sc-label { color: #166534; }

  .srp-col .sc-item {
    font-size: 12.5px;
    padding: 9px 0;
    border-bottom: 1px solid rgba(0,0,0,0.06);
    display: flex;
    align-items: flex-start;
    gap: 10px;
    color: var(--text);
    line-height: 1.5;
  }

  .srp-col .sc-item:last-child { border-bottom: none; }

  .sc-item .si-agent {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    font-weight: 600;
    padding: 2px 7px;
    border-radius: 3px;
    flex-shrink: 0;
    margin-top: 2px;
    white-space: nowrap;
  }

  .violated .si-agent { background: #fee2e2; color: #991b1b; }
  .applied  .si-agent { background: #dcfce7; color: #166534; }

  /* ── Pipeline flow diagram ── */
  .pipeline-flow {
    display: flex;
    align-items: stretch;
    gap: 0;
    margin: 18px 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .pf-node {
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

  .pf-node .pfn-icon { font-size: 24px; }

  .pf-node .pfn-type {
    font-family: 'DM Mono', monospace;
    font-size: 9.5px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
  }

  .pf-node .pfn-name { font-weight: 700; font-size: 13px; color: var(--text); }
  .pf-node .pfn-sub  { font-size: 11px; color: var(--muted); line-height: 1.4; }

  .pf-node.n-input    { background: #f0f9ff; }
  .pf-node.n-input    .pfn-type { color: #0369a1; }
  .pf-node.n-agent-a  { background: var(--amber-light); }
  .pf-node.n-agent-a  .pfn-type { color: #92400e; }
  .pf-node.n-artifact { background: var(--off-white); }
  .pf-node.n-artifact .pfn-type { color: var(--muted); }
  .pf-node.n-agent-b  { background: #f0fdf4; }
  .pf-node.n-agent-b  .pfn-type { color: #166534; }
  .pf-node.n-output   { background: #fdf4ff; }
  .pf-node.n-output   .pfn-type { color: #6b21a8; }

  .pf-arrow {
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
    grid-template-columns: 32px 150px 1fr 170px;
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
---

<!-- _class: cover -->

<div class="series-badge">PIPELINE AGENTS · LEVEL 2 — PART 1 OF 4</div>

# The Pipeline Mental Model
## Chaining specialists instead of overloading one

&nbsp;

**One agent, one hat.** When the job needs more, you don't build a bigger agent — you build a better line.

`pipeline` · `specialist` · `artifact` · `handoff` · `single-responsibility`

---

## Single Agent vs. Pipeline — The Core Difference

A single agent takes a task and runs it alone. A pipeline breaks the same task into stages — each one handled by an agent that does exactly one thing well.

<div class="versus-grid">
  <div class="vs-side single">
    <div class="vs-label">🤖 &nbsp;Single agent</div>
    <div class="vs-title">One prompt. One agent. Everything.</div>
    <div class="vs-item"><span class="vi-icon">→</span> You hand it the full task</div>
    <div class="vs-item"><span class="vi-icon">→</span> It researches, writes, edits, and formats</div>
    <div class="vs-item"><span class="vi-icon">→</span> Quality drops as complexity grows</div>
    <div class="vs-item"><span class="vi-icon">→</span> One bad step corrupts everything after it</div>
    <div class="vs-item"><span class="vi-icon">→</span> Hard to debug — all errors look the same</div>
  </div>
  <div class="vs-divider">vs</div>
  <div class="vs-side pipeline">
    <div class="vs-label">⛓️ &nbsp;Pipeline</div>
    <div class="vs-title">One task. Many specialists.</div>
    <div class="vs-item"><span class="vi-icon">→</span> You hand it the full task</div>
    <div class="vs-item"><span class="vi-icon">→</span> Each agent handles exactly one stage</div>
    <div class="vs-item"><span class="vi-icon">→</span> Quality holds — every agent focuses fully</div>
    <div class="vs-item"><span class="vi-icon">→</span> A bad step is isolated and easy to fix</div>
    <div class="vs-item"><span class="vi-icon">→</span> Each stage is independently debuggable</div>
  </div>
</div>

<div class="highlight">

**Analogy:** A single agent handling a complex task is like one person building an entire car. A pipeline is the assembly line — every station does one thing, hands it forward, and never looks back.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Why Single Agents Break Under Complex Tasks

You've seen the warning signs. Here's the mechanism — what actually happens inside a model when it's asked to wear too many hats at once.

<div class="matters-grid">
  <div class="matters-card">
    <div class="mcc-icon">🎯</div>
    <div>
      <div class="mcc-title">Attention splits across modes</div>
      <div class="mcc-desc">Asking a model to research and write simultaneously means it's "thinking ahead" to prose while it should be evaluating sources. Both modes suffer. The model can't fully commit to either.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">📐</div>
    <div>
      <div class="mcc-title">Output formats conflict</div>
      <div class="mcc-desc">Good research output is dense, structured, and cited. Good writing output is flowing and readable. A single system prompt can't optimise for both — you get a muddy middle.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🧱</div>
    <div>
      <div class="mcc-title">Context gets consumed early</div>
      <div class="mcc-desc">Long intermediate states eat the context window. By step 8, the model has lost the key fact from step 1. The window is finite — complex tasks are long. There's no fix within one call.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🐛</div>
    <div>
      <div class="mcc-title">Failures are invisible</div>
      <div class="mcc-desc">When everything happens inside one call, a wrong inference in step 3 silently propagates through steps 4, 5, and 6. By the time you see the output, the root cause is buried.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## The Assembly Line Analogy

Henry Ford solved this in 1913. The insight wasn't speed — it was specialisation. Agents solve the same problem the same way.

<div class="assembly-compare">
  <div class="assembly-side factory">
    <div class="as-head">🏭 &nbsp;Car factory — assembly line</div>
    <div class="as-body">
      <div class="as-step s1">
        <div class="ass-icon">🔩</div>
        <div><span class="ass-role">Frame welder</span><span class="ass-does">Builds the chassis. Passes it on. Never touches paint.</span></div>
      </div>
      <div class="as-arrow">↓ hands off frame</div>
      <div class="as-step s2">
        <div class="ass-icon">⚙️</div>
        <div><span class="ass-role">Engine fitter</span><span class="ass-does">Installs drivetrain. Assumes the frame is already correct.</span></div>
      </div>
      <div class="as-arrow">↓ hands off body</div>
      <div class="as-step s3">
        <div class="ass-icon">🎨</div>
        <div><span class="ass-role">Paint specialist</span><span class="ass-does">Applies finish. Doesn't know how the engine works.</span></div>
      </div>
      <div class="as-arrow">↓ hands off painted car</div>
      <div class="as-step s4">
        <div class="ass-icon">🔍</div>
        <div><span class="ass-role">QA inspector</span><span class="ass-does">Checks the whole car. Flags problems. Ships or rejects.</span></div>
      </div>
    </div>
  </div>
  <div class="assembly-side agents">
    <div class="as-head">🤖 &nbsp;Content pipeline — agent chain</div>
    <div class="as-body">
      <div class="as-step s1">
        <div class="ass-icon">🔍</div>
        <div><span class="ass-role">Research agent</span><span class="ass-does">Extracts facts and sources. Returns structured JSON. Never writes prose.</span></div>
      </div>
      <div class="as-arrow">↓ hands off research.json</div>
      <div class="as-step s2">
        <div class="ass-icon">✍️</div>
        <div><span class="ass-role">Writer agent</span><span class="ass-does">Turns notes into a draft. Assumes the facts are correct.</span></div>
      </div>
      <div class="as-arrow">↓ hands off draft.md</div>
      <div class="as-step s3">
        <div class="ass-icon">✂️</div>
        <div><span class="ass-role">Editor agent</span><span class="ass-does">Tightens prose. Doesn't re-research. Doesn't change facts.</span></div>
      </div>
      <div class="as-arrow">↓ hands off edited.md</div>
      <div class="as-step s4">
        <div class="ass-icon">✅</div>
        <div><span class="ass-role">Reviewer agent</span><span class="ass-does">Checks accuracy and format. Returns pass or flagged claims.</span></div>
      </div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Single-Responsibility — Applied to Agents

SRP is a software design rule: every module should have exactly one reason to change. For agents: **one job, one output, no "and also."**

<div class="srp-grid">
  <div class="srp-col violated">
    <div class="sc-label">❌ &nbsp;SRP violated — jobs stacked on one agent</div>
    <div class="sc-item">
      <span class="si-agent">AGENT 1</span>
      Research competitors, summarise findings, write a blog post, check for SEO keywords, and format it as HTML.
    </div>
    <div class="sc-item">
      <span class="si-agent">AGENT 2</span>
      Read the CSV, clean the data, analyse trends, write the executive summary, and email it to the team.
    </div>
    <div class="sc-item">
      <span class="si-agent">AGENT 3</span>
      Monitor the API, diagnose errors, write a patch, deploy it, and update the incident log.
    </div>
  </div>
  <div class="srp-col applied">
    <div class="sc-label">✅ &nbsp;SRP applied — one agent, one job</div>
    <div class="sc-item">
      <span class="si-agent">RESEARCH</span>
      Extract competitor data. Return structured JSON. Nothing else.
    </div>
    <div class="sc-item">
      <span class="si-agent">WRITER</span>
      Turn research JSON into a blog draft. Assume input is correct.
    </div>
    <div class="sc-item">
      <span class="si-agent">SEO</span>
      Score the draft for keyword gaps. Return a list. No rewriting.
    </div>
    <div class="sc-item">
      <span class="si-agent">FORMATTER</span>
      Convert final markdown to HTML. No content decisions.
    </div>
  </div>
</div>

<div class="highlight">

**The test:** Can you describe this agent's job in one sentence without using "and"? If you reach for "and" — split it into two agents.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Anatomy of a Pipeline

Every pipeline shares the same shape. Raw input flows through a chain of specialists. Each one produces a named artifact — and that artifact is the only thing the next agent sees.

<div class="pipeline-flow">
  <div class="pf-node n-input">
    <div class="pfn-icon">📥</div>
    <div class="pfn-type">Input</div>
    <div class="pfn-name">Raw material</div>
    <div class="pfn-sub">A URL, a file,<br>a user request</div>
  </div>
  <div class="pf-arrow">→</div>
  <div class="pf-node n-agent-a">
    <div class="pfn-icon">🤖</div>
    <div class="pfn-type">Agent A</div>
    <div class="pfn-name">Specialist #1</div>
    <div class="pfn-sub">One role.<br>One output format.</div>
  </div>
  <div class="pf-arrow">→</div>
  <div class="pf-node n-artifact">
    <div class="pfn-icon">📄</div>
    <div class="pfn-type">Artifact</div>
    <div class="pfn-name">Intermediate</div>
    <div class="pfn-sub">JSON, markdown,<br>structured text</div>
  </div>
  <div class="pf-arrow">→</div>
  <div class="pf-node n-agent-b">
    <div class="pfn-icon">🤖</div>
    <div class="pfn-type">Agent B</div>
    <div class="pfn-name">Specialist #2</div>
    <div class="pfn-sub">Consumes artifact.<br>Produces the next.</div>
  </div>
  <div class="pf-arrow">→</div>
  <div class="pf-node n-output">
    <div class="pfn-icon">📤</div>
    <div class="pfn-type">Output</div>
    <div class="pfn-name">Final result</div>
    <div class="pfn-sub">The deliverable<br>a human reviews</div>
  </div>
</div>

<div class="matters-grid" style="margin-top: 14px;">
  <div class="matters-card">
    <div class="mcc-icon">🔗</div>
    <div>
      <div class="mcc-title">Artifacts are contracts</div>
      <div class="mcc-desc">The output of Agent A is the interface between agents. Define its exact shape before writing either agent's prompt. A vague artifact breaks the whole chain — fix it upstream, not downstream.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🚫</div>
    <div>
      <div class="mcc-title">No skipping or re-doing</div>
      <div class="mcc-desc">Agent B should never redo Agent A's job. If it does, Agent A's output format is incomplete. The fix is always upstream — tighten the artifact, not the downstream prompt.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## Real-World Example — A Content Pipeline, End to End

One blog post request. Five specialist agents. Each does exactly one job and passes a named artifact to the next.

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

**Notice:** No agent touches another's domain. The writer never searches. The editor never checks facts. The QA agent never rewrites. Clean boundaries make every stage independently debuggable.

</div>

---

## Quick Reference — Pipeline Vocabulary

The terms that appear in every Level 2 tutorial, decoded.

<table class="cheat-table">
  <thead>
    <tr><th>Term</th><th>What it means</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="mono">Pipeline</span></td>
      <td>A chain of agents where each one's output is the next one's input. No single agent sees the full task.</td>
    </tr>
    <tr>
      <td><span class="mono">Specialist agent</span></td>
      <td>An agent with a single, narrow role — one job, one output format, clear input assumptions.</td>
    </tr>
    <tr>
      <td><span class="mono">Artifact</span></td>
      <td>The named, structured output of one agent that becomes the input contract for the next. Always saved to disk or memory.</td>
    </tr>
    <tr>
      <td><span class="mono">Handoff</span></td>
      <td>The moment an artifact passes from one agent to the next. A wrong handoff format breaks the whole chain.</td>
    </tr>
    <tr>
      <td><span class="mono">Single-responsibility</span></td>
      <td>The rule that every agent has exactly one reason to change — one job, one owner, one output.</td>
    </tr>
    <tr>
      <td><span class="mono">Orchestrator</span></td>
      <td>The code (or agent) that sequences the pipeline — runs Agent A, captures its artifact, passes it to Agent B. Coming in Part 2.</td>
    </tr>
  </tbody>
</table>

---

<!-- _class: final -->

# Think in Pipelines.

&nbsp;

*Not "what should this agent do?" — but "what should this agent hand off?"*

&nbsp;

Next: **Part 2 — Building the Orchestrator.**

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*