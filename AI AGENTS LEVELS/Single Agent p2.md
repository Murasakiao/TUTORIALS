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

  .tools {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 16px;
  }

  .tool-card {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px 20px;
  }

  .tool-card .icon  { font-size: 24px; margin-bottom: 6px; }
  .tool-card .name  { font-weight: 600; font-size: 15px; color: var(--text); }
  .tool-card .desc  { font-size: 13px; color: var(--muted); margin-top: 2px; }

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

  .two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 16px;
  }

  .col-card {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px 20px;
  }

  .col-card .label {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 8px;
  }

  /* ── Four-part anatomy diagram ── */
  .anatomy-stack {
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin: 16px 0;
  }

  .anat-layer {
    border-radius: 8px;
    padding: 13px 18px;
    display: flex;
    align-items: center;
    gap: 16px;
    border: 1.5px solid transparent;
  }

  .anat-layer.sys { background: var(--amber-light); border-color: var(--amber-mid); }
  .anat-layer.ctx { background: #f0fdf4; border-color: #86efac; }
  .anat-layer.inp { background: #eff6ff; border-color: #bfdbfe; }
  .anat-layer.out { background: #fdf4ff; border-color: #e9d5ff; }

  .anat-layer .al-icon  { font-size: 22px; flex-shrink: 0; }

  .anat-layer .al-num {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 600;
    width: 22px;
    height: 22px;
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    color: white;
  }

  .anat-layer.sys .al-num { background: var(--amber); }
  .anat-layer.ctx .al-num { background: #16a34a; }
  .anat-layer.inp .al-num { background: #2563eb; }
  .anat-layer.out .al-num { background: #7c3aed; }

  .anat-layer .al-name {
    font-weight: 700;
    font-size: 14.5px;
    min-width: 130px;
  }

  .anat-layer.sys .al-name { color: var(--amber-dim); }
  .anat-layer.ctx .al-name { color: #14532d; }
  .anat-layer.inp .al-name { color: #1e3a8a; }
  .anat-layer.out .al-name { color: #4c1d95; }

  .anat-layer .al-desc {
    font-size: 13px;
    color: var(--muted);
    flex: 1;
    line-height: 1.5;
  }

  /* ── System prompt block ── */
  .sp-block {
    background: #1c1917;
    border-radius: 8px;
    overflow: hidden;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 12.5px;
    border: 1px solid #292524;
  }

  .sp-block .sb-bar {
    background: #292524;
    padding: 8px 16px;
    font-size: 11px;
    color: #78716c;
    letter-spacing: 0.06em;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid #44403c;
  }

  .sp-block .sb-bar .sb-badge {
    font-size: 9.5px;
    padding: 2px 8px;
    border-radius: 3px;
    background: #292524;
    color: #d97706;
    border: 1px solid #44403c;
    font-weight: 600;
    letter-spacing: 0.08em;
  }

  .sp-block .sb-body {
    padding: 14px 18px;
    line-height: 2;
  }

  .sp-section { margin-bottom: 6px; }
  .sp-section .sps-label { color: #44403c; font-size: 11px; font-style: italic; }
  .sp-role    { color: #a8a29e; }
  .sp-rule    { color: #e7e5e4; }
  .sp-tool    { color: #34d399; }
  .sp-format  { color: #93c5fd; }
  .sp-limit   { color: #fbbf24; }

  /* ── Context injection diagram ── */
  .ctx-diagram {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    gap: 0;
    align-items: stretch;
    margin: 14px 0;
  }

  .ctx-sources {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .ctx-source {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 10px 13px;
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 13px;
  }

  .ctx-source .cs-icon { font-size: 18px; flex-shrink: 0; }
  .ctx-source .cs-name { font-weight: 600; color: var(--text); font-size: 13px; }
  .ctx-source .cs-desc { font-size: 11.5px; color: var(--muted); margin-top: 1px; }

  .ctx-arrow {
    display: flex;
    align-items: center;
    padding: 0 14px;
    font-size: 22px;
    color: var(--amber);
    flex-shrink: 0;
  }

  .ctx-window {
    background: var(--amber-light);
    border: 1.5px solid var(--amber-mid);
    border-radius: 8px;
    padding: 14px 16px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 5px;
  }

  .ctx-window .cw-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--amber-dim);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 4px;
    font-weight: 600;
  }

  .ctx-slot {
    border-radius: 4px;
    padding: 5px 10px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
  }

  .ctx-slot.sys  { background: #fef3c7; color: #92400e; }
  .ctx-slot.mem  { background: #dcfce7; color: #166534; }
  .ctx-slot.hist { background: #dbeafe; color: #1e40af; }
  .ctx-slot.msg  { background: #fdf4ff; color: #6b21a8; }

  /* ── Tool flow diagram ── */
  .tool-flow {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0;
    margin: 16px 0;
  }

  .tf-node {
    border-radius: 8px;
    padding: 12px 14px;
    text-align: center;
    min-width: 100px;
    flex-shrink: 0;
  }

  .tf-node .tfn-icon  { font-size: 22px; margin-bottom: 3px; }
  .tf-node .tfn-label { font-weight: 600; font-size: 12.5px; }
  .tf-node .tfn-sub   { font-family: 'DM Mono', monospace; font-size: 10px; opacity: 0.75; margin-top: 2px; }

  .tf-node.model  { background: var(--amber-light); border: 1.5px solid var(--amber-mid); }
  .tf-node.call   { background: #eff6ff; border: 1.5px solid #bfdbfe; }
  .tf-node.exec   { background: #f0fdf4; border: 1.5px solid #86efac; }
  .tf-node.result { background: #fdf4ff; border: 1.5px solid #e9d5ff; }

  .tf-node.model  .tfn-label { color: var(--amber-dim); }
  .tf-node.call   .tfn-label { color: #1e40af; }
  .tf-node.exec   .tfn-label { color: #166534; }
  .tf-node.result .tfn-label { color: #6b21a8; }

  .tf-arrow {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0 8px;
    gap: 1px;
    flex-shrink: 0;
  }

  .tf-arrow .tfa-label {
    font-family: 'DM Mono', monospace;
    font-size: 9.5px;
    color: var(--muted);
    white-space: nowrap;
  }

  .tf-arrow .tfa-line { font-size: 18px; color: var(--amber); }

  /* ── Tool definition block ── */
  .tool-def {
    background: #1c1917;
    border-radius: 8px;
    overflow: hidden;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 12.5px;
    border: 1px solid #292524;
  }

  .tool-def .td-bar {
    background: #292524;
    padding: 8px 16px;
    font-size: 11px;
    color: #78716c;
    letter-spacing: 0.06em;
    border-bottom: 1px solid #44403c;
  }

  .tool-def .td-body {
    padding: 14px 18px;
    line-height: 2;
  }

  .td-key   { color: #93c5fd; }
  .td-str   { color: var(--amber-mid); }
  .td-type  { color: #c084fc; }
  .td-bool  { color: #34d399; }
  .td-punct { color: #44403c; }
  .td-cmt   { color: #44403c; font-style: italic; }

  /* ── Contract grid ── */
  .contract-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 14px;
  }

  .contract-side {
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .contract-side .cs-header {
    padding: 10px 14px;
    font-weight: 600;
    font-size: 13px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border);
  }

  .contract-side.input-side  .cs-header { background: var(--amber-light); color: var(--amber-dim); border-color: var(--amber-mid); }
  .contract-side.output-side .cs-header { background: #fdf4ff; color: #6b21a8; border-color: #e9d5ff; }
  .contract-side.input-side             { border-color: var(--amber-mid); }
  .contract-side.output-side            { border-color: #e9d5ff; }

  .contract-side .cs-body {
    padding: 10px 14px;
    background: var(--white);
  }

  .contract-side .cs-rule {
    display: flex;
    align-items: baseline;
    gap: 8px;
    padding: 5px 0;
    border-bottom: 1px solid var(--border);
    font-size: 13px;
  }

  .contract-side .cs-rule:last-child { border-bottom: none; }

  .contract-side .cs-rule .cr-key {
    font-family: 'DM Mono', monospace;
    font-size: 11.5px;
    color: var(--amber-dim);
    font-weight: 500;
    min-width: 100px;
    flex-shrink: 0;
  }

  .contract-side.output-side .cs-rule .cr-key { color: #6b21a8; }

  /* ── Bad / good contract compare ── */
  .contract-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 14px;
  }

  .cc-col {
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .cc-col .ccl-label {
    padding: 8px 14px;
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    border-bottom: 1px solid var(--border);
  }

  .cc-col.bad  .ccl-label { background: #fef2f2; color: #991b1b; border-color: #fecaca; }
  .cc-col.good .ccl-label { background: #f0fdf4; color: #166534; border-color: #bbf7d0; }
  .cc-col.bad             { border-color: #fecaca; }
  .cc-col.good            { border-color: #bbf7d0; }

  .cc-col .ccl-body {
    background: #1c1917;
    padding: 12px 16px;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    line-height: 2;
  }

  .jb-key   { color: #93c5fd; }
  .jb-str   { color: var(--amber-mid); }
  .jb-str-b { color: #34d399; }
  .jb-num   { color: #fb923c; }
  .jb-bool  { color: #c084fc; }
  .jb-null  { color: #f87171; }
  .jb-punct { color: #44403c; }
  .jb-cmt   { color: #44403c; font-style: italic; }

  /* ── Cheatsheet table ── */
  .cheat-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
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
    background: var(--amber);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    min-width: 24px;
    height: 24px;
    border-radius: 5px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 2px;
    flex-shrink: 0;
  }
---

<!-- _class: cover -->

<div class="series-badge">SINGLE AGENT SERIES · PART 2 OF 4</div>

# Anatomy of an Agent
## The Four Parts of Every Agent

&nbsp;

**Understanding the structure** is what separates guessing from engineering.

`system prompt` · `context` · `tools` · `input` · `output contract`

---

## The Four Parts of Every Agent

Every agent — no matter how complex — is built from exactly four structural parts. Change any one of them and the agent behaves differently.

<div class="anatomy-stack">
  <div class="anat-layer sys">
    <div class="al-num">1</div>
    <div class="al-icon">📋</div>
    <div class="al-name">System Prompt</div>
    <div class="al-desc">The agent's standing instructions — who it is, what it can do, how it behaves, and what tools it has. Set once. Shapes every decision.</div>
  </div>
  <div class="anat-layer ctx">
    <div class="al-num">2</div>
    <div class="al-icon">💾</div>
    <div class="al-name">Context</div>
    <div class="al-desc">Everything injected into the conversation before the user's message — memory, past tool results, retrieved documents, conversation history.</div>
  </div>
  <div class="anat-layer inp">
    <div class="al-num">3</div>
    <div class="al-icon">📥</div>
    <div class="al-name">Input</div>
    <div class="al-desc">The current user message or triggering event. What the agent is being asked to do right now, in this loop iteration.</div>
  </div>
  <div class="anat-layer out">
    <div class="al-num">4</div>
    <div class="al-icon">📤</div>
    <div class="al-name">Output</div>
    <div class="al-desc">Either a tool call (the agent wants to act) or a final answer (the goal is met). Never both in the same turn. Always one or the other.</div>
  </div>
</div>

<div class="highlight" style="margin-top:12px;">

**The loop is just these four parts repeating.** System prompt stays constant. Context grows with each step. Input changes each iteration. Output drives the next action.

</div>

---

<!-- _class: step -->

<div class="step-badge">PART 01</div>

## System Prompt — The Agent's Job Description

The system prompt is the most important thing you write. It defines the agent's **identity, rules, tools, and output format** — before the user says a word.

<div class="sp-block">
  <div class="sb-bar">
    <span>system prompt — research agent</span>
    <span class="sb-badge">SYSTEM</span>
  </div>
  <div class="sb-body">
    <div class="sp-section">
      <span class="sps-label"># Role</span><br>
      <span class="sp-role">You are a research assistant. Your job is to answer questions by searching the web and synthesising findings into a concise, accurate response.</span>
    </div>
    <div class="sp-section">
      <span class="sps-label"># Rules</span><br>
      <span class="sp-rule">- Always search before answering. Never rely on your training data for current facts.</span><br>
      <span class="sp-rule">- If the search result is unclear, search again with a different query.</span><br>
      <span class="sp-rule">- Cite your sources. Never fabricate a URL.</span>
    </div>
    <div class="sp-section">
      <span class="sps-label"># Tools available</span><br>
      <span class="sp-tool">- web_search(query: str) → list of results</span><br>
      <span class="sp-tool">- fetch_page(url: str) → full page text</span>
    </div>
    <div class="sp-section">
      <span class="sps-label"># Output format</span><br>
      <span class="sp-format">Return a JSON object: {"answer": str, "sources": [str], "confidence": "high"|"medium"|"low"}</span>
    </div>
    <span class="sps-label"># Limits</span><br>
    <span class="sp-limit">Stop after 10 tool calls. If still unsure, return your best answer with confidence: "low".</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">PART 01 — continued</div>

## What a System Prompt Must Include

<div class="two-col">
  <div class="col-card">
    <div class="label">Required sections</div>
    <ul style="margin-top:8px; padding-left:1.2em;">
      <li style="font-size:13.5px;"><strong>Role</strong> — What is this agent? What is it for?</li>
      <li style="font-size:13.5px;"><strong>Rules</strong> — What must it always / never do?</li>
      <li style="font-size:13.5px;"><strong>Tools</strong> — What tools exist, their names and signatures</li>
      <li style="font-size:13.5px;"><strong>Output format</strong> — Exact shape of the response</li>
      <li style="font-size:13.5px;"><strong>Limits</strong> — Max steps, fallback behavior</li>
    </ul>
  </div>
  <div class="col-card">
    <div class="label">Common mistakes</div>
    <ul style="margin-top:8px; padding-left:1.2em;">
      <li style="font-size:13.5px;">No output format → unpredictable, unparseable responses</li>
      <li style="font-size:13.5px;">No step limit → infinite loops on ambiguous goals</li>
      <li style="font-size:13.5px;">Vague role → the model improvises and drifts</li>
      <li style="font-size:13.5px;">Tools listed but not described → model calls them wrong</li>
      <li style="font-size:13.5px;">No fallback rule → agent freezes when it gets stuck</li>
    </ul>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**Write the system prompt before anything else.** It is the agent's constitution. Everything the agent does flows from it. A good system prompt makes tool definitions, loop logic, and output parsing all easier downstream.

</div>

---

<!-- _class: step -->

<div class="step-badge">PART 02</div>

## Context Injection — How You Feed the Agent Memory

The context is everything you place in the conversation **before the user's message** — the agent's working memory for this run.

<div class="ctx-diagram">
  <div class="ctx-sources">
    <div class="ctx-source">
      <div class="cs-icon">🗃️</div>
      <div>
        <div class="cs-name">Long-term memory</div>
        <div class="cs-desc">User preferences, past decisions, learned facts from a database</div>
      </div>
    </div>
    <div class="ctx-source">
      <div class="cs-icon">📜</div>
      <div>
        <div class="cs-name">Conversation history</div>
        <div class="cs-desc">Previous turns in this session — what was asked and answered</div>
      </div>
    </div>
    <div class="ctx-source">
      <div class="cs-icon">🔍</div>
      <div>
        <div class="cs-name">Retrieved documents</div>
        <div class="cs-desc">Relevant chunks from a vector DB, injected by a RAG pipeline</div>
      </div>
    </div>
    <div class="ctx-source">
      <div class="cs-icon">⚙️</div>
      <div>
        <div class="cs-name">Tool results</div>
        <div class="cs-desc">Output from the last tool call — accumulated across loop iterations</div>
      </div>
    </div>
  </div>
  <div class="ctx-arrow">→</div>
  <div class="ctx-window">
    <div class="cw-label">context window</div>
    <div class="ctx-slot sys">📋 system prompt</div>
    <div class="ctx-slot mem">🗃️ memory: "user prefers JSON output"</div>
    <div class="ctx-slot hist">📜 history: [prev turns]</div>
    <div class="ctx-slot mem">🔍 docs: [retrieved chunks]</div>
    <div class="ctx-slot hist">⚙️ tool result: {search output}</div>
    <div class="ctx-slot msg">📥 user: "What's the weather?"</div>
  </div>
</div>

<div class="highlight" style="margin-top:10px;">

**You control what goes in.** The model only knows what's in its context window. If something isn't injected, the agent doesn't know it — even if you told it in a different session.

</div>

---

<!-- _class: step -->

<div class="step-badge">PART 03</div>

## Tools — What They Are and Why Agents Need Them

A tool is a function the agent can call to interact with the world. Without tools, the agent can only reason with what's already in its context — it cannot fetch, run, or write anything.

<div class="tool-flow">
  <div class="tf-node model">
    <div class="tfn-icon">🧠</div>
    <div class="tfn-label">Model decides</div>
    <div class="tfn-sub">outputs tool call JSON</div>
  </div>
  <div class="tf-arrow">
    <div class="tfa-label">tool call</div>
    <div class="tfa-line">→</div>
  </div>
  <div class="tf-node call">
    <div class="tfn-icon">📡</div>
    <div class="tfn-label">Your code receives</div>
    <div class="tfn-sub">parses name + args</div>
  </div>
  <div class="tf-arrow">
    <div class="tfa-label">executes</div>
    <div class="tfa-line">→</div>
  </div>
  <div class="tf-node exec">
    <div class="tfn-icon">⚡</div>
    <div class="tfn-label">Function runs</div>
    <div class="tfn-sub">search, code, API...</div>
  </div>
  <div class="tf-arrow">
    <div class="tfa-label">result</div>
    <div class="tfa-line">→</div>
  </div>
  <div class="tf-node result">
    <div class="tfn-icon">📋</div>
    <div class="tfn-label">Appended to context</div>
    <div class="tfn-sub">model reads & continues</div>
  </div>
</div>

<div class="tool-def">
  <div class="td-bar">tool definition — how you describe a tool to the model</div>
  <div class="td-body">
    <span class="td-punct">{</span><br>
    &nbsp;&nbsp;<span class="td-key">"name"</span><span class="td-punct">:</span>        <span class="td-str">"web_search"</span><span class="td-punct">,</span><br>
    &nbsp;&nbsp;<span class="td-key">"description"</span><span class="td-punct">:</span> <span class="td-str">"Search the web for current information. Use when you need facts not in your training data."</span><span class="td-punct">,</span><br>
    &nbsp;&nbsp;<span class="td-key">"parameters"</span><span class="td-punct">: {</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="td-key">"query"</span><span class="td-punct">:</span> <span class="td-punct">{</span> <span class="td-key">"type"</span><span class="td-punct">:</span> <span class="td-type">"string"</span><span class="td-punct">,</span> <span class="td-key">"description"</span><span class="td-punct">:</span> <span class="td-str">"The search query"</span> <span class="td-punct">}</span><br>
    &nbsp;&nbsp;<span class="td-punct">},</span><br>
    &nbsp;&nbsp;<span class="td-key">"required"</span><span class="td-punct">:</span> <span class="td-punct">[</span><span class="td-str">"query"</span><span class="td-punct">]</span><br>
    <span class="td-punct">}</span>
  </div>
</div>

<div class="highlight">

**The description is everything.** The model reads it to decide when to use the tool. Vague descriptions → wrong tool calls. Precise descriptions → the model calls the right tool at the right time.

</div>

---

<!-- _class: step -->

<div class="step-badge">PART 04</div>

## Input / Output Contracts — Why They Matter

A contract is a **strict agreement** about what goes in and what comes out. Agents without contracts produce unpredictable output that breaks downstream code.

<div class="contract-grid">
  <div class="contract-side input-side">
    <div class="cs-header">📥 &nbsp;Input contract</div>
    <div class="cs-body">
      <div class="cs-rule"><span class="cr-key">goal</span> Plain-language description of what to accomplish</div>
      <div class="cs-rule"><span class="cr-key">context</span> Structured data the agent needs to do the job</div>
      <div class="cs-rule"><span class="cr-key">constraints</span> Rules for this specific run — max steps, format</div>
      <div class="cs-rule"><span class="cr-key">format_hint</span> Optional nudge if output format needs reinforcing</div>
    </div>
  </div>
  <div class="contract-side output-side">
    <div class="cs-header">📤 &nbsp;Output contract</div>
    <div class="cs-body">
      <div class="cs-rule"><span class="cr-key">result</span> The answer, summary, or generated content</div>
      <div class="cs-rule"><span class="cr-key">status</span> "complete" | "partial" | "failed"</div>
      <div class="cs-rule"><span class="cr-key">steps_taken</span> How many loop iterations were used</div>
      <div class="cs-rule"><span class="cr-key">confidence</span> "high" | "medium" | "low" — model's self-assessment</div>
    </div>
  </div>
</div>

<div class="contract-compare" style="margin-top:14px;">
  <div class="cc-col bad">
    <div class="ccl-label">❌ &nbsp;No contract — unpredictable</div>
    <div class="ccl-body">
      <span class="jb-cmt">// sometimes a string</span><br>
      <span class="jb-str">"Here are the results..."</span><br>
      <span class="jb-cmt">// sometimes a dict</span><br>
      <span class="jb-punct">{</span><span class="jb-key">"answer"</span><span class="jb-punct">:</span> <span class="jb-str">"..."</span><span class="jb-punct">}</span><br>
      <span class="jb-cmt">// sometimes markdown</span><br>
      <span class="jb-str">"## Results\n- item..."</span><br>
      <span class="jb-cmt">// json.loads() breaks on all three</span>
    </div>
  </div>
  <div class="cc-col good">
    <div class="ccl-label">✅ &nbsp;With contract — always parseable</div>
    <div class="ccl-body">
      <span class="jb-punct">{</span><br>
      &nbsp;&nbsp;<span class="jb-key">"result"</span><span class="jb-punct">:</span>      <span class="jb-str-b">"Manila: 31°C, thunderstorm"</span><span class="jb-punct">,</span><br>
      &nbsp;&nbsp;<span class="jb-key">"status"</span><span class="jb-punct">:</span>      <span class="jb-str-b">"complete"</span><span class="jb-punct">,</span><br>
      &nbsp;&nbsp;<span class="jb-key">"steps_taken"</span><span class="jb-punct">:</span> <span class="jb-num">2</span><span class="jb-punct">,</span><br>
      &nbsp;&nbsp;<span class="jb-key">"confidence"</span><span class="jb-punct">:</span>  <span class="jb-str-b">"high"</span><br>
      <span class="jb-punct">}</span><br>
      <span class="jb-cmt">// same shape every single run</span>
    </div>
  </div>
</div>

---

## Part 2 Quick Reference

<table class="cheat-table">
  <thead>
    <tr><th>Part</th><th>What it is</th><th>Key rule</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="mono">System prompt</span></td>
      <td>The agent's standing instructions — role, rules, tools, format, limits</td>
      <td>Write it first. Be explicit. Always include output format and step limit.</td>
    </tr>
    <tr>
      <td><span class="mono">Context</span></td>
      <td>Everything injected before the user message — memory, history, retrieved docs, tool results</td>
      <td>You control what goes in. If it's not injected, the agent doesn't know it.</td>
    </tr>
    <tr>
      <td><span class="mono">Input</span></td>
      <td>The current goal or message — what the agent is asked to do right now</td>
      <td>Be specific. Vague goals produce vague actions. Include constraints per-run.</td>
    </tr>
    <tr>
      <td><span class="mono">Output</span></td>
      <td>Tool call (act) or final answer (done) — always one or the other, never both</td>
      <td>Define the exact shape in the system prompt. Validate with Pydantic downstream.</td>
    </tr>
    <tr>
      <td><span class="mono">Tool definition</span></td>
      <td>Name, description, parameter schema — how you tell the model a tool exists</td>
      <td>The description decides when the model uses it. Make it unambiguous.</td>
    </tr>
    <tr>
      <td><span class="mono">Tool call flow</span></td>
      <td>Model outputs JSON → your code runs the function → result appended to context</td>
      <td>The model never runs tools directly. Your loop controller executes them.</td>
    </tr>
    <tr>
      <td><span class="mono">Input contract</span></td>
      <td>Defined schema for what goes into the agent each run</td>
      <td>Consistent input structure makes agents debuggable and testable.</td>
    </tr>
    <tr>
      <td><span class="mono">Output contract</span></td>
      <td>Defined schema for what the agent always returns</td>
      <td>Same shape every run. Include status and confidence — not just the result.</td>
    </tr>
  </tbody>
</table>

---

<!-- _class: final -->

# Know the structure.
# Own the behavior.

&nbsp;

System prompt. Context. Input. Output. Four parts — endless combinations.

&nbsp;

Next: **Part 3 — Building Your First Agent.**

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*