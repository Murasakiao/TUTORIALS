---
marp: true
theme: default
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=DM+Mono:wght@400;500&display=swap');

  :root {
    --blue: #2563eb;
    --blue-light: #eff6ff;
    --blue-mid: #bfdbfe;
    --text: #111827;
    --muted: #6b7280;
    --border: #e5e7eb;
    --white: #ffffff;
    --off-white: #f9fafb;
  }

  section {
    font-family: 'DM Sans', sans-serif;
    background: var(--white);
    color: var(--text);
    padding: 52px 64px;
    font-size: 18px;
    line-height: 1.6;
  }

  section::after {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: var(--muted);
  }

  h1 {
    font-family: 'DM Sans', sans-serif;
    font-size: 42px;
    font-weight: 600;
    color: var(--text);
    line-height: 1.2;
    margin-bottom: 0.4em;
  }

  h2 {
    font-family: 'DM Sans', sans-serif;
    font-size: 28px;
    font-weight: 600;
    color: var(--text);
    border-bottom: 2px solid var(--blue);
    padding-bottom: 10px;
    margin-bottom: 24px;
  }

  h3 {
    font-family: 'DM Sans', sans-serif;
    font-size: 20px;
    font-weight: 500;
    color: var(--blue);
    margin-bottom: 8px;
  }

  p { color: var(--text); margin: 0.4em 0; }
  ul { padding-left: 1.4em; }
  li { margin-bottom: 10px; color: var(--text); }
  strong { color: var(--blue); font-weight: 600; }

  code {
    font-family: 'DM Mono', monospace;
    background: var(--blue-light);
    color: var(--blue);
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.88em;
  }

  blockquote {
    border-left: 4px solid var(--blue);
    background: var(--blue-light);
    padding: 16px 20px;
    margin: 20px 0;
    border-radius: 0 8px 8px 0;
    font-family: 'DM Mono', monospace;
    font-size: 0.82em;
    color: #1e40af;
    line-height: 1.6;
  }

  blockquote p { color: #1e40af; margin: 0; }

  section.cover {
    background: var(--text);
    color: var(--white);
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  section.cover h1 { color: var(--white); font-size: 46px; }
  section.cover h2 { color: #93c5fd; border-bottom-color: #374151; }
  section.cover p  { color: #9ca3af; }
  section.cover strong { color: #60a5fa; }
  section.cover code { background: #1e3a5f; color: #93c5fd; }

  section.step { background: var(--off-white); }

  .highlight {
    background: var(--blue-light);
    border: 1px solid var(--blue-mid);
    border-radius: 10px;
    padding: 18px 24px;
    margin: 16px 0;
  }

  .tools {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 16px;
  }

  .tool-card {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px 20px;
  }

  .tool-card .icon  { font-size: 24px; margin-bottom: 6px; }
  .tool-card .name  { font-weight: 600; font-size: 15px; color: var(--text); }
  .tool-card .desc  { font-size: 13px; color: var(--muted); margin-top: 2px; }

  .step-badge {
    display: inline-block;
    background: var(--blue);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    padding: 4px 14px;
    border-radius: 999px;
    margin-bottom: 12px;
    letter-spacing: 0.05em;
  }

  section.final {
    background: var(--blue);
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
  }

  section.final h1 { color: white; font-size: 40px; }
  section.final p  { color: #bfdbfe; font-size: 18px; }
  section.final strong { color: white; }
  section.final em { color: #bfdbfe; }

  /* ── Code block ── */
  .code-block {
    background: #111827;
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .code-block .cb-bar {
    background: #1f2937;
    padding: 8px 16px;
    font-size: 11.5px;
    color: #6b7280;
    letter-spacing: 0.04em;
  }

  .code-block .cb-body {
    padding: 14px 20px;
    line-height: 2;
  }

  .cb-kw     { color: #c084fc; }
  .cb-fn     { color: #60a5fa; }
  .cb-str    { color: #fde68a; }
  .cb-num    { color: #fb923c; }
  .cb-cmt    { color: #4b5563; font-style: italic; }
  .cb-var    { color: #f9fafb; }
  .cb-prop   { color: #34d399; }
  .cb-op     { color: #6b7280; }
  .cb-hi     { color: #34d399; }
  .cb-prompt { color: #22c55e; }
  .cb-cmd    { color: #f9fafb; }
  .cb-out    { color: #9ca3af; }

  /* ── Two-column layout ── */
  .two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 16px;
  }

  .col-card {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px 20px;
  }

  .col-card .label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 8px;
  }

  /* ── Linear flow (input → process → output) ── */
  .linear-flow {
    display: flex;
    align-items: stretch;
    gap: 0;
    margin: 20px 0;
  }

  .lf-node {
    flex: 1;
    border-radius: 12px;
    padding: 18px 16px;
    text-align: center;
    position: relative;
  }

  .lf-node.input   { background: #f0fdf4; border: 2px solid #86efac; }
  .lf-node.process { background: var(--blue-light); border: 2px solid var(--blue-mid); }
  .lf-node.output  { background: #fef3c7; border: 2px solid #fde68a; }

  .lf-node .lf-icon  { font-size: 28px; margin-bottom: 6px; }
  .lf-node .lf-label {
    font-weight: 700;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    margin-bottom: 4px;
  }

  .lf-node.input   .lf-label { color: #166534; }
  .lf-node.process .lf-label { color: #1e40af; }
  .lf-node.output  .lf-label { color: #92400e; }

  .lf-node .lf-example {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.5;
    margin-top: 4px;
  }

  .lf-arrow {
    display: flex;
    align-items: center;
    padding: 0 10px;
    font-size: 22px;
    color: var(--blue);
    flex-shrink: 0;
  }

  /* ── Node type cards ── */
  .node-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .node-card {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .node-card .nc-header {
    padding: 10px 14px;
    font-weight: 600;
    font-size: 13px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border);
  }

  .node-card.input-node   .nc-header { background: #f0fdf4; color: #166534; }
  .node-card.process-node .nc-header { background: var(--blue-light); color: #1e40af; }
  .node-card.output-node  .nc-header { background: #fef3c7; color: #92400e; }

  .node-card .nc-body {
    padding: 10px 14px;
    background: var(--white);
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.55;
  }

  .node-card .nc-examples {
    padding: 8px 14px 10px;
    background: var(--off-white);
    border-top: 1px solid var(--border);
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    line-height: 1.7;
  }

  /* ── Condition (diamond) diagram ── */
  .condition-flow {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0;
    margin: 18px 0;
  }

  .cf-node {
    border-radius: 10px;
    padding: 12px 16px;
    text-align: center;
    min-width: 100px;
  }

  .cf-node.start  { background: #f0fdf4; border: 2px solid #86efac; }
  .cf-node.decide { background: #fef3c7; border: 2px solid #fde68a; transform: rotate(0deg); }
  .cf-node.yes    { background: var(--blue-light); border: 2px solid var(--blue-mid); }
  .cf-node.no     { background: #fef2f2; border: 2px solid #fecaca; }

  .cf-node .cfl   { font-weight: 700; font-size: 12px; text-transform: uppercase; letter-spacing: 0.06em; }
  .cf-node .cfd   { font-size: 12px; color: var(--muted); margin-top: 3px; }

  .cf-node.start  .cfl { color: #166534; }
  .cf-node.decide .cfl { color: #92400e; }
  .cf-node.yes    .cfl { color: #1e40af; }
  .cf-node.no     .cfl { color: #991b1b; }

  .cf-arrow {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0 6px;
    gap: 2px;
  }

  .cf-arrow .cfa-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--muted);
  }

  .cf-arrow .cfa-line { font-size: 18px; color: var(--blue); }

  /* ── Loop diagram ── */
  .loop-diagram {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px 20px;
    margin: 14px 0;
    position: relative;
  }

  .loop-diagram .ld-label {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.07em;
    margin-bottom: 12px;
  }

  .loop-row {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .loop-node {
    border-radius: 8px;
    padding: 9px 14px;
    font-size: 13px;
    font-weight: 500;
    text-align: center;
    flex: 1;
  }

  .loop-node.fetch   { background: #f0fdf4; color: #166534; border: 1px solid #86efac; }
  .loop-node.process { background: var(--blue-light); color: #1e40af; border: 1px solid var(--blue-mid); }
  .loop-node.check   { background: #fef3c7; color: #92400e; border: 1px solid #fde68a; }
  .loop-node.store   { background: #f5f3ff; color: #5b21b6; border: 1px solid #ddd6fe; }
  .loop-node.done    { background: #fef2f2; color: #991b1b; border: 1px solid #fecaca; }

  .loop-arrow-h { font-size: 16px; color: var(--blue); flex-shrink: 0; }

  .loop-back {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 8px;
    gap: 6px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
  }

  .loop-back-line {
    height: 2px;
    background: var(--border);
    flex: 1;
    border-radius: 999px;
  }

  /* ── Full workflow diagram ── */
  .workflow-diagram {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 18px 20px;
    margin: 14px 0;
  }

  .workflow-diagram .wd-title {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.07em;
    margin-bottom: 14px;
  }

  /* horizontal row of workflow nodes */
  .wf-row {
    display: flex;
    align-items: stretch;
    gap: 0;
    margin-bottom: 6px;
  }

  .wf-node {
    border-radius: 8px;
    padding: 10px 12px;
    font-size: 12px;
    font-weight: 600;
    text-align: center;
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 3px;
  }

  .wf-node .wf-icon { font-size: 16px; }
  .wf-node .wf-label { font-size: 11.5px; font-weight: 600; }
  .wf-node .wf-sub   { font-size: 10px; font-weight: 400; color: inherit; opacity: 0.75; }

  .wf-node.trigger  { background: #f0fdf4; color: #166534; border: 1px solid #86efac; }
  .wf-node.fetch    { background: var(--blue-light); color: #1e40af; border: 1px solid var(--blue-mid); }
  .wf-node.ai       { background: #f5f3ff; color: #5b21b6; border: 1px solid #ddd6fe; }
  .wf-node.check    { background: #fef3c7; color: #92400e; border: 1px solid #fde68a; }
  .wf-node.send     { background: #f0fdf4; color: #166534; border: 1px solid #86efac; }
  .wf-node.log      { background: #fef2f2; color: #991b1b; border: 1px solid #fecaca; }
  .wf-node.store    { background: #eff6ff; color: #1e40af; border: 1px solid #bfdbfe; }

  .wf-arrow { 
    display: flex;
    align-items: center;
    padding: 0 5px;
    font-size: 14px;
    color: var(--blue);
    flex-shrink: 0;
  }

  /* branch row below check node */
  .wf-branch {
    display: flex;
    align-items: flex-start;
    gap: 8px;
    margin-top: 4px;
    padding-left: 0;
  }

  .wf-branch-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--muted);
    padding-top: 12px;
    flex-shrink: 0;
    width: 28px;
    text-align: center;
  }

  /* ── Cheatsheet table ── */
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
    font-size: 12px;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.05em;
  }

  .cheat-table td {
    padding: 9px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
  }

  .cheat-table tr:last-child td { border-bottom: none; }
  .cheat-table tr:nth-child(even) td { background: var(--off-white); }

  .cheat-table .mono {
    font-family: 'DM Mono', monospace;
    color: var(--blue);
    font-size: 12.5px;
  }

  .step-list {
    counter-reset: steps;
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .step-list li {
    counter-increment: steps;
    display: flex;
    align-items: flex-start;
    gap: 14px;
    margin-bottom: 14px;
  }

  .step-list li::before {
    content: counter(steps);
    background: var(--blue);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    min-width: 24px;
    height: 24px;
    border-radius: 999px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 2px;
    flex-shrink: 0;
  }
---

<!-- _class: cover -->

# Build a Simple
## AI Workflow

&nbsp;

**Automate anything.** Input → Process → Output. Then add brains.

`input` · `process` · `output` · `condition` · `loop` · `pipeline`

---

## What Is a Workflow?

A workflow is a sequence of steps where the output of each step becomes the input of the next. Add AI to one or more steps and it becomes intelligent automation.

<div class="tools">
  <div class="tool-card">
    <div class="icon">⚙️</div>
    <div class="name">Without AI</div>
    <div class="desc">A script fetches data, transforms it, and saves it. Useful — but rigid. It can only do what you explicitly coded.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🤖</div>
    <div class="name">With AI</div>
    <div class="desc">One step calls an AI model. The model interprets, classifies, generates, or decides. The workflow handles the rest automatically.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔗</div>
    <div class="name">Composable</div>
    <div class="desc">Workflows are built from small nodes connected in sequence. Each node does one thing. Complex behavior comes from composing simple steps.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔁</div>
    <div class="name">Repeatable</div>
    <div class="desc">Run it once or on a schedule. The same workflow processes 1 item or 10,000 items — you change only the input, not the logic.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Input → Process → Output

Every workflow — no matter how complex — is built on this three-node pattern.

<div class="linear-flow">
  <div class="lf-node input">
    <div class="lf-icon">📥</div>
    <div class="lf-label">Input</div>
    <div class="lf-example">Raw data enters the workflow. User text, file, API response, database row, form submission.</div>
  </div>
  <div class="lf-arrow">→</div>
  <div class="lf-node process">
    <div class="lf-icon">🤖</div>
    <div class="lf-label">Process</div>
    <div class="lf-example">AI model reads the input, applies a prompt, and produces a result. Classify, summarize, extract, generate, decide.</div>
  </div>
  <div class="lf-arrow">→</div>
  <div class="lf-node output">
    <div class="lf-icon">📤</div>
    <div class="lf-label">Output</div>
    <div class="lf-example">Result is saved, sent, or passed to the next step. Database, email, Slack, file, another AI call.</div>
  </div>
</div>

<div class="node-grid">
  <div class="node-card input-node">
    <div class="nc-header">📥 &nbsp;Input nodes</div>
    <div class="nc-body">Where data enters. Passive — they don't transform anything, just provide the raw material for the next step.</div>
    <div class="nc-examples">user text · CSV file · API call<br>webhook · database query · form</div>
  </div>
  <div class="node-card process-node">
    <div class="nc-header">🤖 &nbsp;Process nodes</div>
    <div class="nc-body">Where work happens. Usually the AI call — but also includes data transformation, parsing, and formatting steps.</div>
    <div class="nc-examples">AI prompt · json.loads() · filter<br>regex · sort · merge · translate</div>
  </div>
  <div class="node-card output-node">
    <div class="nc-header">📤 &nbsp;Output nodes</div>
    <div class="nc-body">Where results land. Could be a final destination or an intermediate handoff to another workflow or system.</div>
    <div class="nc-examples">save to DB · send email · Slack msg<br>write file · POST to API · log</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Build the Base Workflow in Python

<div class="code-block">
  <div class="cb-bar">workflow.py — minimal input → process → output</div>
  <div class="cb-body">
    <span class="cb-kw">import</span> <span class="cb-var">anthropic</span><span class="cb-op">,</span> <span class="cb-var">json</span><br>
    <span class="cb-cmt"># ── INPUT ────────────────────────────────────</span><br>
    <span class="cb-var">raw_review</span> <span class="cb-op">=</span> <span class="cb-str">"Battery drains too fast but the screen is stunning."</span><br>
    <span class="cb-cmt"># ── PROCESS ──────────────────────────────────</span><br>
    <span class="cb-var">client</span>   <span class="cb-op">=</span> <span class="cb-var">anthropic</span><span class="cb-op">.</span><span class="cb-fn">Anthropic</span><span class="cb-op">()</span><br>
    <span class="cb-var">response</span> <span class="cb-op">=</span> <span class="cb-var">client</span><span class="cb-op">.</span><span class="cb-var">messages</span><span class="cb-op">.</span><span class="cb-fn">create</span><span class="cb-op">(</span><br>
    &nbsp;&nbsp;<span class="cb-prop">model</span>      <span class="cb-op">=</span> <span class="cb-str">"claude-sonnet-4-6"</span><span class="cb-op">,</span><br>
    &nbsp;&nbsp;<span class="cb-prop">max_tokens</span> <span class="cb-op">=</span> <span class="cb-num">256</span><span class="cb-op">,</span><br>
    &nbsp;&nbsp;<span class="cb-prop">messages</span>   <span class="cb-op">=</span> <span class="cb-op">[{</span><span class="cb-str">"role"</span><span class="cb-op">:</span> <span class="cb-str">"user"</span><span class="cb-op">,</span> <span class="cb-str">"content"</span><span class="cb-op">:</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-str">f"Classify this review. Return JSON with sentiment (positive/negative/mixed) and score (1-5).\n\n</span><span class="cb-op">{</span><span class="cb-var">raw_review</span><span class="cb-op">}</span><span class="cb-str">"</span><br>
    &nbsp;&nbsp;<span class="cb-op">}]</span><br>
    <span class="cb-op">)</span><br>
    <span class="cb-var">result</span> <span class="cb-op">=</span> <span class="cb-var">json</span><span class="cb-op">.</span><span class="cb-fn">loads</span><span class="cb-op">(</span><span class="cb-var">response</span><span class="cb-op">.</span><span class="cb-var">content</span><span class="cb-op">[</span><span class="cb-num">0</span><span class="cb-op">].</span><span class="cb-prop">text</span><span class="cb-op">)</span><br>
    <span class="cb-cmt"># ── OUTPUT ───────────────────────────────────</span><br>
    <span class="cb-fn">print</span><span class="cb-op">(</span><span class="cb-str">f"Sentiment: </span><span class="cb-op">{</span><span class="cb-var">result</span><span class="cb-op">[</span><span class="cb-str">'sentiment'</span><span class="cb-op">]}</span><span class="cb-str"> | Score: </span><span class="cb-op">{</span><span class="cb-var">result</span><span class="cb-op">[</span><span class="cb-str">'score'</span><span class="cb-op">]}</span><span class="cb-str">/5"</span><span class="cb-op">)</span><br>
    <span class="cb-cmt"># save to database, send to Slack, etc.</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Add Conditions

Conditions make the workflow smart — different results take different paths.

<div class="condition-flow">
  <div class="cf-node start">
    <div class="cfl">AI Result</div>
    <div class="cfd">sentiment + score</div>
  </div>
  <div class="cf-arrow">
    <div class="cfa-line">→</div>
  </div>
  <div class="cf-node decide">
    <div class="cfl">Score &lt; 3?</div>
    <div class="cfd">check condition</div>
  </div>
  <div class="cf-arrow">
    <div class="cfa-label">YES</div>
    <div class="cfa-line">→</div>
  </div>
  <div class="cf-node no">
    <div class="cfl">Alert</div>
    <div class="cfd">Slack + ticket</div>
  </div>
  <div style="width:20px;"></div>
  <div class="cf-node decide" style="opacity:0; pointer-events:none;">
    <div class="cfl">Score &lt; 3?</div>
  </div>
  <div class="cf-arrow">
    <div class="cfa-label">NO</div>
    <div class="cfa-line">→</div>
  </div>
  <div class="cf-node yes">
    <div class="cfl">Log</div>
    <div class="cfd">save to DB</div>
  </div>
</div>

<div class="code-block">
  <div class="cb-bar">workflow.py — add a condition after the AI step</div>
  <div class="cb-body">
    <span class="cb-cmt"># After parsing the AI result...</span><br>
    <span class="cb-kw">if</span> <span class="cb-var">result</span><span class="cb-op">[</span><span class="cb-str">"score"</span><span class="cb-op">]</span> <span class="cb-op">&lt;</span> <span class="cb-num">3</span><span class="cb-op">:</span><br>
    &nbsp;&nbsp;<span class="cb-fn">send_slack_alert</span><span class="cb-op">(</span><span class="cb-str">f"⚠️ Negative review: </span><span class="cb-op">{</span><span class="cb-var">raw_review</span><span class="cb-op">}</span><span class="cb-str">"</span><span class="cb-op">)</span>  <span class="cb-cmt"># urgent path</span><br>
    &nbsp;&nbsp;<span class="cb-fn">create_support_ticket</span><span class="cb-op">(</span><span class="cb-var">raw_review</span><span class="cb-op">,</span> <span class="cb-var">result</span><span class="cb-op">)</span><br>
    <span class="cb-kw">else</span><span class="cb-op">:</span><br>
    &nbsp;&nbsp;<span class="cb-fn">save_to_database</span><span class="cb-op">(</span><span class="cb-var">raw_review</span><span class="cb-op">,</span> <span class="cb-var">result</span><span class="cb-op">)</span>               <span class="cb-cmt"># routine path</span>
  </div>
</div>

<div class="highlight">

**Conditions are what make workflows non-trivial.** Without them, every input takes the same path regardless of content. Add conditions and the workflow starts making decisions on your behalf.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Add Loops

Loops run the same workflow node over a collection — processing many items with one piece of logic.

<div class="loop-diagram">
  <div class="ld-label">loop — process every review in a list</div>
  <div class="loop-row">
    <div class="loop-node fetch">📋 Load reviews</div>
    <div class="loop-arrow-h">→</div>
    <div class="loop-node process">🤖 AI classify</div>
    <div class="loop-arrow-h">→</div>
    <div class="loop-node check">⚖️ Score &lt; 3?</div>
    <div class="loop-arrow-h">→</div>
    <div class="loop-node store">💾 Save result</div>
    <div class="loop-arrow-h">→</div>
    <div class="loop-node done">✅ Next item</div>
  </div>
  <div class="loop-back">
    <div class="loop-back-line"></div>
    <span>↩ repeat for each review</span>
    <div class="loop-back-line"></div>
  </div>
</div>

<div class="code-block">
  <div class="cb-bar">workflow.py — loop over a list of reviews</div>
  <div class="cb-body">
    <span class="cb-var">reviews</span> <span class="cb-op">=</span> <span class="cb-fn">load_reviews_from_csv</span><span class="cb-op">(</span><span class="cb-str">"reviews.csv"</span><span class="cb-op">)</span><br>
    <span class="cb-kw">for</span> <span class="cb-var">review</span> <span class="cb-kw">in</span> <span class="cb-var">reviews</span><span class="cb-op">:</span><br>
    &nbsp;&nbsp;<span class="cb-var">result</span> <span class="cb-op">=</span> <span class="cb-fn">classify_with_ai</span><span class="cb-op">(</span><span class="cb-var">review</span><span class="cb-op">)</span>      <span class="cb-cmt"># same AI call each time</span><br>
    &nbsp;&nbsp;<span class="cb-kw">if</span> <span class="cb-var">result</span><span class="cb-op">[</span><span class="cb-str">"score"</span><span class="cb-op">]</span> <span class="cb-op">&lt;</span> <span class="cb-num">3</span><span class="cb-op">:</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-fn">send_slack_alert</span><span class="cb-op">(</span><span class="cb-var">review</span><span class="cb-op">)</span><br>
    &nbsp;&nbsp;<span class="cb-fn">save_to_database</span><span class="cb-op">(</span><span class="cb-var">review</span><span class="cb-op">,</span> <span class="cb-var">result</span><span class="cb-op">)</span>
  </div>
</div>

<div class="two-col" style="margin-top:12px;">
  <div class="col-card">
    <div class="label">Limit API calls</div>
    <p style="font-size:13.5px; margin-top:6px;">Add <code>time.sleep(0.5)</code> between iterations to avoid rate-limiting. Most AI APIs allow 60–1000 requests per minute depending on your plan.</p>
  </div>
  <div class="col-card">
    <div class="label">Handle failures</div>
    <p style="font-size:13.5px; margin-top:6px;">Wrap the AI call in try/except inside the loop. One bad item shouldn't kill the whole batch — log the error and continue.</p>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Full Example — Review Triage Workflow

A complete AI workflow that processes customer reviews on a schedule, alerts on negative ones, and stores everything.

<div class="workflow-diagram">
  <div class="wd-title">review triage workflow — runs daily at 9 AM via cron</div>

  <div class="wf-row">
    <div class="wf-node trigger">
      <div class="wf-icon">⏰</div>
      <div class="wf-label">Trigger</div>
      <div class="wf-sub">cron: 0 9 * * *</div>
    </div>
    <div class="wf-arrow">→</div>
    <div class="wf-node fetch">
      <div class="wf-icon">📥</div>
      <div class="wf-label">Fetch reviews</div>
      <div class="wf-sub">DB: last 24h</div>
    </div>
    <div class="wf-arrow">→</div>
    <div class="wf-node ai">
      <div class="wf-icon">🤖</div>
      <div class="wf-label">AI classify</div>
      <div class="wf-sub">sentiment + score</div>
    </div>
    <div class="wf-arrow">→</div>
    <div class="wf-node check">
      <div class="wf-icon">⚖️</div>
      <div class="wf-label">Score &lt; 3?</div>
      <div class="wf-sub">condition check</div>
    </div>
  </div>

  <div class="wf-branch" style="margin-top:8px;">
    <div style="flex:3; display:flex; gap:8px; align-items:flex-start;">
      <div style="display:flex;flex-direction:column;align-items:center;padding-top:4px;">
        <div style="font-family:'DM Mono',monospace;font-size:10px;color:var(--muted);">YES</div>
        <div style="font-size:16px;color:#dc2626;">↓</div>
      </div>
      <div style="display:flex;flex-direction:column;gap:6px;flex:1;">
        <div class="wf-node send" style="flex:none;">
          <div class="wf-icon">🔔</div>
          <div class="wf-label">Slack alert</div>
          <div class="wf-sub">#support-urgent</div>
        </div>
        <div class="wf-node log" style="flex:none;">
          <div class="wf-icon">🎫</div>
          <div class="wf-label">Open ticket</div>
          <div class="wf-sub">Jira / Linear</div>
        </div>
      </div>
    </div>
    <div style="flex:1; display:flex; flex-direction:column; align-items:center  padding-top:4px;">
      <div style="font-family:'DM Mono',monospace;font-size:10px;color:var(--muted);">NO</div>
      <div style="font-size:16px;color:#2563eb;">↓</div>
    </div>
    <div style="flex:3; display:flex; flex-direction:column; gap:6px;">
      <div class="wf-node store" style="flex:none;">
        <div class="wf-icon">💾</div>
        <div class="wf-label">Save result</div>
        <div class="wf-sub">PostgreSQL</div>
      </div>
    </div>
  </div>
</div>

---

## AI Workflow Quick Reference

<table class="cheat-table">
  <tr>
    <th>Pattern</th>
    <th>When to use it</th>
    <th>Key code</th>
  </tr>
  <tr>
    <td>Input → Process → Output</td>
    <td>Single item, one AI step, one destination</td>
    <td class="mono">result = ai_call(input) · save(result)</td>
  </tr>
  <tr>
    <td>Condition branch</td>
    <td>Different results need different actions</td>
    <td class="mono">if result["score"] &lt; 3: alert()</td>
  </tr>
  <tr>
    <td>Loop over collection</td>
    <td>Same workflow for many items</td>
    <td class="mono">for item in items: process(item)</td>
  </tr>
  <tr>
    <td>Chain AI steps</td>
    <td>Output of one AI call feeds the next</td>
    <td class="mono">step2_input = step1_result["field"]</td>
  </tr>
  <tr>
    <td>Schedule the workflow</td>
    <td>Run automatically on a timer</td>
    <td class="mono">cron · Task Scheduler · APScheduler</td>
  </tr>
  <tr>
    <td>Rate limit protection</td>
    <td>Batch processing many API calls</td>
    <td class="mono">time.sleep(0.5) between iterations</td>
  </tr>
  <tr>
    <td>Fail gracefully</td>
    <td>One bad item shouldn't stop the loop</td>
    <td class="mono">try/except inside the for loop</td>
  </tr>
  <tr>
    <td>Log everything</td>
    <td>Debugging scheduled workflows</td>
    <td class="mono">logging.info() with timestamps</td>
  </tr>
  <tr>
    <td>Validate AI output</td>
    <td>Before acting on parsed JSON</td>
    <td class="mono">Pydantic or manual field check</td>
  </tr>
</table>

---

<!-- _class: final -->

# Input. Process. Output.
# Add conditions.
# Add loops. Ship it.

&nbsp;

Every automation you'll ever build is just these three things composed.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*