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
  .vs-side.ai    { background: var(--off-white); }
  .vs-side.agent { background: #fffbeb; }

  .vs-side .vs-label {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.09em;
    margin-bottom: 8px;
  }

  .vs-side.ai    .vs-label { color: var(--muted); }
  .vs-side.agent .vs-label { color: #92400e; }

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
  .vs-side.agent .vs-item { border-bottom-color: #fde68a; color: var(--text); }
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

  .problem-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .problem-card {
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .problem-card .pc-head {
    padding: 9px 14px;
    font-weight: 600;
    font-size: 13px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border);
  }

  .problem-card.problem .pc-head  { background: #fef2f2; color: #991b1b; border-color: #fecaca; }
  .problem-card.solution .pc-head { background: #f0fdf4; color: #166534; border-color: #bbf7d0; }

  .problem-card .pc-body {
    padding: 11px 14px;
    background: var(--white);
    font-size: 13px;
    color: var(--muted);
    line-height: 1.6;
  }

  .anatomy-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 14px;
  }

  .anatomy-box {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .anatomy-box .ab-header {
    padding: 10px 14px;
    font-weight: 600;
    font-size: 13.5px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border);
  }

  .anatomy-box.llm   .ab-header { background: var(--off-white); color: var(--text); }
  .anatomy-box.agent .ab-header { background: var(--amber-light); color: #92400e; border-color: #fde68a; }
  .anatomy-box.agent            { border-color: #fde68a; }

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

  .ab-layer.core    { background: var(--amber-light); border: 1px solid #fde68a; }
  .ab-layer.tools   { background: #eff6ff; border: 1px solid #bfdbfe; }
  .ab-layer.memory  { background: #f0fdf4; border: 1px solid #bbf7d0; }
  .ab-layer.loop    { background: #fdf4ff; border: 1px solid #e9d5ff; }
  .ab-layer.plain   { background: var(--off-white); border: 1px solid var(--border); }

  .react-loop {
    display: flex;
    align-items: stretch;
    justify-content: center;
    gap: 0;
    margin: 16px 0;
  }

  .rl-node {
    border-radius: 10px;
    padding: 14px 14px;
    text-align: center;
    min-width: 118px;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .rl-node .rn-icon  { font-size: 26px; margin-bottom: 4px; }
  .rl-node .rn-label { font-weight: 700; font-size: 12px; text-transform: uppercase; letter-spacing: 0.07em; margin-bottom: 4px; }
  .rl-node .rn-ques  { font-family: 'DM Mono', monospace; font-size: 10.5px; opacity: 0.8; line-height: 1.4; }

  .rl-node.reason  { background: var(--amber-light); border: 2px solid #fde68a; }
  .rl-node.act     { background: #eff6ff; border: 2px solid #bfdbfe; }
  .rl-node.observe { background: #f0fdf4; border: 2px solid #86efac; }
  .rl-node.decide  { background: #fdf4ff; border: 2px solid #e9d5ff; }

  .rl-node.reason  .rn-label { color: #92400e; }
  .rl-node.act     .rn-label { color: #1e40af; }
  .rl-node.observe .rn-label { color: #166534; }
  .rl-node.decide  .rn-label { color: #6b21a8; }

  .rl-arrow {
    display: flex;
    align-items: center;
    padding: 0 6px;
    font-size: 18px;
    color: var(--amber);
    flex-shrink: 0;
  }

  .rl-loop-back {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 8px;
    gap: 6px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
  }

  .rl-loop-line {
    height: 1.5px;
    background: var(--border);
    border-radius: 999px;
    flex: 1;
    max-width: 80px;
  }

  .react-walkthrough {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 14px;
  }

  .rw-step {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px 15px;
    display: flex;
    align-items: flex-start;
    gap: 10px;
  }

  .rw-step .rws-badge {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    font-weight: 600;
    padding: 3px 8px;
    border-radius: 3px;
    flex-shrink: 0;
    margin-top: 1px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    white-space: nowrap;
  }

  .rws-badge.reason  { background: var(--amber-light); color: #92400e; border: 1px solid #fde68a; }
  .rws-badge.act     { background: #eff6ff; color: #1e40af; border: 1px solid #bfdbfe; }
  .rws-badge.observe { background: #f0fdf4; color: #166634; border: 1px solid #bbf7d0; }
  .rws-badge.decide  { background: #fdf4ff; color: #6b21a8; border: 1px solid #e9d5ff; }

  .rw-step .rws-text {
    font-size: 12.5px;
    color: var(--text);
    line-height: 1.55;
  }

  .rw-step .rws-text .rws-tool {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--amber-dim);
    background: var(--amber-light);
    padding: 1px 5px;
    border-radius: 3px;
  }

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

<div class="series-badge">SINGLE AGENT SERIES · PART 1 OF N</div>

# Your First AI Worker
## What Is an Agent

&nbsp;

**Before you build one**, understand what separates it from a plain LLM call.

`ReAct` · `reason` · `act` · `observe` · `tool` · `loop`

---

## AI vs Agent — The Core Difference

A plain AI answers your question and stops. An agent **keeps going** — deciding what to do next, using tools, and looping until the job is done.

<div class="versus-grid">
  <div class="vs-side ai">
    <div class="vs-label">💬 &nbsp;Plain LLM call</div>
    <div class="vs-title">One prompt. One response.</div>
    <div class="vs-item"><span class="vi-icon">→</span> You send a message</div>
    <div class="vs-item"><span class="vi-icon">→</span> It replies once</div>
    <div class="vs-item"><span class="vi-icon">→</span> It cannot call tools or APIs</div>
    <div class="vs-item"><span class="vi-icon">→</span> You decide what to do with the answer</div>
    <div class="vs-item"><span class="vi-icon">→</span> Every step requires a human</div>
  </div>
  <div class="vs-divider">vs</div>
  <div class="vs-side agent">
    <div class="vs-label">🤖 &nbsp;Agent</div>
    <div class="vs-title">One goal. Many steps.</div>
    <div class="vs-item"><span class="vi-icon">→</span> You give a high-level objective</div>
    <div class="vs-item"><span class="vi-icon">→</span> It plans and acts autonomously</div>
    <div class="vs-item"><span class="vi-icon">→</span> It calls tools — search, code, APIs</div>
    <div class="vs-item"><span class="vi-icon">→</span> It decides what to do with each result</div>
    <div class="vs-item"><span class="vi-icon">→</span> It loops until the goal is complete</div>
  </div>
</div>

<div class="highlight">

**Analogy:** A plain LLM is a very smart calculator — ask a question, get an answer. An agent is more like a capable junior colleague — give them a task, they figure out the steps and come back when it's done.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## The Problem a Single Agent Solves

Most real tasks aren't single questions. They're chains of dependent steps — where each step needs the result of the last one.

<div class="problem-grid">
  <div class="problem-card problem">
    <div class="pc-head">❌ &nbsp;Without an agent</div>
    <div class="pc-body">You ask the AI "research competitors." It gives you a summary. You then manually search each one, copy results, paste them back, ask for analysis, copy that, write the report yourself. You are the pipeline.</div>
  </div>
  <div class="problem-card solution">
    <div class="pc-head">✅ &nbsp;With an agent</div>
    <div class="pc-body">You say "research our top 5 competitors and write a summary report." The agent searches each one, reads the pages, extracts key data, writes the report, and saves it. You review the output.</div>
  </div>
  <div class="problem-card problem">
    <div class="pc-head">❌ &nbsp;Without an agent</div>
    <div class="pc-body">"Check if our API is down." You open a terminal, run a curl command, read the output, decide if it's a problem, manually send a Slack alert. Five manual steps for a 10-second task.</div>
  </div>
  <div class="problem-card solution">
    <div class="pc-head">✅ &nbsp;With an agent</div>
    <div class="pc-body">The agent pings the API endpoint, checks the status code, compares against the expected response, and sends a Slack alert only if something is wrong. Runs every 5 minutes, unattended.</div>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**The pattern:** A single agent solves tasks where the next step depends on the result of the current one — and where a human shouldn't need to be in the loop for every iteration.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## What Makes It an Agent — Not Just an LLM Call

Three things separate an agent from a regular prompt/response interaction.

<div class="anatomy-compare">
  <div class="anatomy-box llm">
    <div class="ab-header">💬 &nbsp;Plain LLM call</div>
    <div class="ab-body">
      <div class="ab-layer plain">
        <div class="abl-icon">🧠</div>
        <div>
          <div class="abl-name">Language model</div>
          <div class="abl-desc">Takes prompt → returns text. That's it.</div>
        </div>
      </div>
      <div style="font-size:12px; color:var(--muted); padding:8px 4px; text-align:center; font-style:italic;">No tools. No loop. No memory.<br>One call. One response. Done.</div>
    </div>
  </div>
  <div class="anatomy-box agent">
    <div class="ab-header">🤖 &nbsp;Agent — three additions</div>
    <div class="ab-body">
      <div class="ab-layer core">
        <div class="abl-icon">🧠</div>
        <div>
          <div class="abl-name">Language model (same core)</div>
          <div class="abl-desc">Still the reasoning engine — now with a system prompt that defines the loop</div>
        </div>
      </div>
      <div class="ab-layer tools">
        <div class="abl-icon">🔧</div>
        <div>
          <div class="abl-name">Tools</div>
          <div class="abl-desc">Functions the model can call — search, run code, read files, send email</div>
        </div>
      </div>
      <div class="ab-layer memory">
        <div class="abl-icon">💾</div>
        <div>
          <div class="abl-name">Memory / context</div>
          <div class="abl-desc">Accumulates observations and results across multiple steps</div>
        </div>
      </div>
      <div class="ab-layer loop">
        <div class="abl-icon">🔁</div>
        <div>
          <div class="abl-name">Loop controller</div>
          <div class="abl-desc">Your code that keeps calling the model until the goal is met</div>
        </div>
      </div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## The ReAct Loop — Reason → Act → Observe → Repeat

ReAct (Reasoning + Acting) is the most common agent pattern. The model alternates between thinking about what to do and doing it.

<div class="react-loop">
  <div class="rl-node reason">
    <div class="rn-icon">🧠</div>
    <div class="rn-label">Reason</div>
    <div class="rn-ques">What do I know?<br>What should I do next?</div>
  </div>
  <div class="rl-arrow">→</div>
  <div class="rl-node act">
    <div class="rn-icon">⚡</div>
    <div class="rn-label">Act</div>
    <div class="rn-ques">Call a tool.<br>Get a result back.</div>
  </div>
  <div class="rl-arrow">→</div>
  <div class="rl-node observe">
    <div class="rn-icon">👁️</div>
    <div class="rn-label">Observe</div>
    <div class="rn-ques">What came back?<br>Did it work?</div>
  </div>
  <div class="rl-arrow">→</div>
  <div class="rl-node decide">
    <div class="rn-icon">🔀</div>
    <div class="rn-label">Decide</div>
    <div class="rn-ques">Loop again?<br>Or done?</div>
  </div>
</div>

<div class="rl-loop-back">
  <div class="rl-loop-line"></div>
  ↺ &nbsp;loops back to Reason until the goal is complete
  <div class="rl-loop-line"></div>
</div>

<div class="react-walkthrough">
  <div class="rw-step">
    <span class="rws-badge reason">Reason</span>
    <div class="rws-text">"I need to find the current Visayas grid load. I should call <span class="rws-tool">get_grid_data()</span> first."</div>
  </div>
  <div class="rw-step">
    <span class="rws-badge act">Act</span>
    <div class="rws-text">Calls <span class="rws-tool">get_grid_data(region="visayas")</span> and waits for the result.</div>
  </div>
  <div class="rw-step">
    <span class="rws-badge observe">Observe</span>
    <div class="rws-text">Tool returns load data. Model adds this to context and re-evaluates what to do next.</div>
  </div>
  <div class="rw-step">
    <span class="rws-badge decide">Decide</span>
    <div class="rws-text">Has enough data to complete the task. Exits the loop and returns the final analysis.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Why This Pattern Is Powerful

The ReAct loop isn't just an implementation detail — it's what separates brittle scripts from flexible agents.

<div class="matters-grid">
  <div class="matters-card">
    <div class="mcc-icon">🔍</div>
    <div>
      <div class="mcc-title">Handles unknowns gracefully</div>
      <div class="mcc-desc">A script fails when output doesn't match expectations. An agent reasons about what it got and decides what to try next — it adapts mid-task.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🔧</div>
    <div>
      <div class="mcc-title">Tools extend what's possible</div>
      <div class="mcc-desc">Each tool you give the agent is a new action it can take. Search, code execution, file I/O, API calls — the agent picks the right one per step.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">💾</div>
    <div>
      <div class="mcc-title">Context accumulates naturally</div>
      <div class="mcc-desc">Every observation gets added back to the conversation. The agent doesn't forget — it builds a richer picture of the task with each loop.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🔁</div>
    <div>
      <div class="mcc-title">The loop is your control plane</div>
      <div class="mcc-desc">You decide when it stops: task complete, max iterations hit, or error threshold crossed. The agent does the work; you set the guardrails.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## Building Your First Agent — The Minimal Loop

You only need three things to run a real ReAct agent: a model, at least one tool, and a loop.

<ul class="step-list">
  <li>
    <div><strong>Define your tools.</strong> A tool is just a Python function with a clear name, typed inputs, and a docstring. The model reads the description to know when and how to call it.</div>
  </li>
  <li>
    <div><strong>Write the loop.</strong> Call the model. If it returns a tool call, run the function and append the result to the conversation. If it returns plain text, you're done — that's the final answer.</div>
  </li>
  <li>
    <div><strong>Set a stop condition.</strong> Always cap your loop at a maximum number of iterations. This prevents infinite loops and keeps costs predictable.</div>
  </li>
  <li>
    <div><strong>Inspect the trace.</strong> Print every Reason → Act → Observe step while developing. This is how you debug agent behaviour — the trace is your log.</div>
  </li>
</ul>

<div class="highlight">

**Minimal viable agent:** `model` + `tools list` + `while not done` loop + `max_steps` guard. Everything else — memory stores, multi-agent orchestration, critic loops — builds on top of this.

</div>

---

## Quick Reference — Agent Vocabulary

The terms that appear in every agent tutorial, decoded.

<table class="cheat-table">
  <thead>
    <tr><th>Term</th><th>What it means</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="mono">Agent</span></td>
      <td>An LLM + tools + a loop. Takes a goal and acts until it's done.</td>
    </tr>
    <tr>
      <td><span class="mono">ReAct</span></td>
      <td>Reason + Act pattern. The model thinks, then acts, then observes — repeating until the goal is met.</td>
    </tr>
    <tr>
      <td><span class="mono">Tool</span></td>
      <td>A function the agent can call — a search API, code runner, file reader, database query, etc.</td>
    </tr>
    <tr>
      <td><span class="mono">Loop</span></td>
      <td>The code wrapping the LLM call that keeps running until a stop condition is met.</td>
    </tr>
    <tr>
      <td><span class="mono">Observation</span></td>
      <td>The result returned by a tool. Gets appended to the conversation so the model can reason over it.</td>
    </tr>
    <tr>
      <td><span class="mono">Context window</span></td>
      <td>The agent's working memory — everything it can see in the current call, including all prior observations.</td>
    </tr>
    <tr>
      <td><span class="mono">Stop condition</span></td>
      <td>The rule that ends the loop: task complete, max steps reached, or an unrecoverable error.</td>
    </tr>
  </tbody>
</table>

---

<!-- _class: final -->

# Now Build Your First Agent.

&nbsp;

*You understand the pattern. The next step is running it.*

&nbsp;

**Part 2 →** Giving Your Agent Tools

**Part 3 →** Managing Context and Memory

**Part 4 →** Multi-Agent Patterns