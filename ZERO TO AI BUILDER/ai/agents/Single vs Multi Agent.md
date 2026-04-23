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

  .highlight.good {
    background: #f0fdf4;
    border-color: #bbf7d0;
  }

  .highlight.warn {
    background: #fefce8;
    border-color: #fde68a;
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

  /* Single agent diagram */
  .single-agent {
    background: #111827;
    border-radius: 12px;
    padding: 20px 24px;
    margin: 14px 0;
    display: flex;
    align-items: center;
    gap: 0;
  }

  .agent-node {
    border-radius: 10px;
    padding: 14px 16px;
    text-align: center;
    flex-shrink: 0;
  }

  .agent-node.orchestrator {
    background: #1e3a5f;
    border: 2px solid #2563eb;
    min-width: 120px;
  }

  .agent-node.single {
    background: #1e3a5f;
    border: 2px solid #2563eb;
    min-width: 140px;
  }

  .agent-node.specialist {
    background: #111827;
    border: 1px solid #374151;
    min-width: 110px;
  }

  .agent-node.specialist.researcher { border-color: #1d4ed8; }
  .agent-node.specialist.writer     { border-color: #166534; }
  .agent-node.specialist.reviewer   { border-color: #7c3aed; }
  .agent-node.specialist.coder      { border-color: #92400e; }

  .agent-node .an-icon  { font-size: 20px; margin-bottom: 4px; }

  .agent-node .an-label {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 700;
  }

  .agent-node.orchestrator .an-label { color: #60a5fa; }
  .agent-node.single       .an-label { color: #60a5fa; }

  .agent-node.specialist.researcher .an-label { color: #60a5fa; }
  .agent-node.specialist.writer     .an-label { color: #86efac; }
  .agent-node.specialist.reviewer   .an-label { color: #c4b5fd; }
  .agent-node.specialist.coder      .an-label { color: #fde68a; }

  .agent-node .an-tasks {
    font-size: 10px;
    color: #6b7280;
    margin-top: 4px;
    line-height: 1.5;
    font-family: 'DM Mono', monospace;
  }

  .agent-arrow {
    color: #374151;
    font-size: 16px;
    padding: 0 8px;
    flex-shrink: 0;
  }

  .task-stack {
    display: flex;
    flex-direction: column;
    gap: 6px;
    flex: 1;
    margin-left: 16px;
  }

  .task-pill {
    background: #1f2937;
    border: 1px solid #374151;
    border-radius: 6px;
    padding: 6px 12px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #9ca3af;
    text-align: left;
  }

  /* Multi-agent layout */
  .multi-agent {
    background: #111827;
    border-radius: 12px;
    padding: 20px 24px;
    margin: 14px 0;
  }

  .ma-top {
    display: flex;
    justify-content: center;
    margin-bottom: 12px;
  }

  .ma-row {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 10px;
    margin-top: 4px;
  }

  .ma-connector {
    display: flex;
    justify-content: center;
    gap: 0;
    margin-bottom: 4px;
  }

  .ma-line {
    width: 2px;
    height: 16px;
    background: #374151;
  }

  /* Pros/cons table */
  .proscons-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 16px 0;
  }

  .proscons-card {
    border-radius: 10px;
    overflow: hidden;
  }

  .proscons-card .pc-header {
    padding: 9px 16px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }

  .proscons-card.single-pros .pc-header { background: #1e3a5f; color: #60a5fa; }
  .proscons-card.single-cons .pc-header { background: #451a03; color: #fde68a; }
  .proscons-card.multi-pros  .pc-header { background: #14532d; color: #86efac; }
  .proscons-card.multi-cons  .pc-header { background: #4c0519; color: #f9a8d4; }

  .proscons-card .pc-body {
    background: #0d1117;
    padding: 12px 16px;
    font-size: 13px;
    line-height: 2;
  }

  .proscons-card.single-pros .pc-body { border: 1px solid #1e3a5f; border-top: none; border-radius: 0 0 10px 10px; color: #93c5fd; }
  .proscons-card.single-cons .pc-body { border: 1px solid #451a03; border-top: none; border-radius: 0 0 10px 10px; color: #fde68a; }
  .proscons-card.multi-pros  .pc-body { border: 1px solid #14532d; border-top: none; border-radius: 0 0 10px 10px; color: #86efac; }
  .proscons-card.multi-cons  .pc-body { border: 1px solid #4c0519; border-top: none; border-radius: 0 0 10px 10px; color: #f9a8d4; }

  /* Decision table */
  .decision-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
    margin: 14px 0;
  }

  .decision-table th {
    background: var(--text);
    color: white;
    padding: 9px 14px;
    text-align: left;
    font-weight: 500;
    font-size: 12px;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.05em;
  }

  .decision-table td {
    padding: 9px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
    font-size: 13px;
    vertical-align: top;
  }

  .decision-table tr:nth-child(even) td { background: var(--off-white); }

  .arch-tag {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 4px;
    display: inline-block;
    white-space: nowrap;
  }

  .arch-tag.single { background: #1e3a5f; color: #60a5fa; }
  .arch-tag.multi  { background: #14532d; color: #86efac; }
  .arch-tag.either { background: #374151; color: #9ca3af; }

  /* Visual workflow — orchestrator → specialists */
  .workflow-full {
    background: #111827;
    border-radius: 12px;
    padding: 20px 24px;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
  }

  .wf-row {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 10px;
  }

  .wf-row:last-child { margin-bottom: 0; }

  .wf-badge {
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    padding: 3px 10px;
    border-radius: 999px;
    flex-shrink: 0;
    min-width: 80px;
    text-align: center;
  }

  .wf-badge.user   { background: #374151; color: #9ca3af; }
  .wf-badge.orch   { background: #1e3a5f; color: #60a5fa; }
  .wf-badge.res    { background: #1e3a5f; color: #60a5fa; }
  .wf-badge.write  { background: #14532d; color: #86efac; }
  .wf-badge.review { background: #2e1065; color: #c4b5fd; }
  .wf-badge.output { background: #374151; color: #d1d5db; }

  .wf-msg {
    background: #1f2937;
    border: 1px solid #374151;
    border-radius: 6px;
    padding: 6px 12px;
    color: #d1d5db;
    font-size: 12px;
    flex: 1;
    line-height: 1.5;
  }

  .wf-arrow-h { color: #374151; font-size: 14px; flex-shrink: 0; }

  /* two-col */
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
---

<!-- _class: cover -->

# Single-Agent vs Multi-Agent
## A Simple Breakdown

&nbsp;

**One generalist doing everything — or specialists working in parallel.** Here's how to choose.

`orchestrator` · `specialist` · `handoff` · `parallel` · `role`

---

## The Core Difference

One agent that does everything sequentially — or multiple agents that specialise and collaborate.

<div class="tools">
  <div class="tool-card">
    <div class="icon">🤖</div>
    <div class="name">Single agent</div>
    <div class="desc">One model, one context window, one role. Handles every step of a task from start to finish — sequentially, alone.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🤝</div>
    <div class="name">Multi-agent</div>
    <div class="desc">Multiple specialised agents, each with a defined role. An orchestrator routes subtasks to the right agent and assembles the result.</div>
  </div>
  <div class="tool-card">
    <div class="icon">📏</div>
    <div class="name">It's not about capability</div>
    <div class="desc">A single agent can often do everything a multi-agent system can. The difference is scale, specialisation, and context efficiency.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🎯</div>
    <div class="name">The right choice depends on your task</div>
    <div class="desc">Simple, linear tasks → single. Complex, parallel, or high-quality tasks with distinct stages → multi.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Single Agent — One Does Everything

One agent receives the task and handles every step sequentially in a single context window.

<div class="single-agent">
  <div class="agent-node single">
    <div class="an-icon">🤖</div>
    <div class="an-label">Agent</div>
    <div class="an-tasks">one context<br>all tasks</div>
  </div>
  <div class="agent-arrow">→</div>
  <div class="task-stack">
    <div class="task-pill">1. Search for relevant grid fault data</div>
    <div class="task-pill">2. Analyse patterns across 50 bus results</div>
    <div class="task-pill">3. Write summary report in plain English</div>
    <div class="task-pill">4. Format and export to CSV</div>
    <div class="task-pill">5. Draft email to the engineering team</div>
  </div>
</div>

<div class="two-col">
  <div class="col-card">
    <div class="label">✅ Works well when</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">Tasks are linear, steps share context, and the full workflow fits comfortably in one context window.</p>
  </div>
  <div class="col-card">
    <div class="label">⚠️ Struggles when</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">Context gets too long, tasks require different expertise, or quality needs a separate review pass.</p>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Multi-Agent — Specialists With Roles

An orchestrator agent breaks the task into subtasks and delegates each to a specialist agent.

<div class="multi-agent">
  <div class="ma-top">
    <div class="agent-node orchestrator">
      <div class="an-icon">🎯</div>
      <div class="an-label">Orchestrator</div>
      <div class="an-tasks">routes + assembles</div>
    </div>
  </div>
  <div class="ma-connector">
    <div style="display:flex; gap:64px;">
      <div class="ma-line"></div>
      <div class="ma-line"></div>
      <div class="ma-line"></div>
      <div class="ma-line"></div>
    </div>
  </div>
  <div class="ma-row">
    <div class="agent-node specialist researcher">
      <div class="an-icon">🔍</div>
      <div class="an-label">Researcher</div>
      <div class="an-tasks">searches + retrieves</div>
    </div>
    <div class="agent-node specialist writer">
      <div class="an-icon">✍️</div>
      <div class="an-label">Writer</div>
      <div class="an-tasks">drafts content</div>
    </div>
    <div class="agent-node specialist reviewer">
      <div class="an-icon">🔎</div>
      <div class="an-label">Reviewer</div>
      <div class="an-tasks">critiques + scores</div>
    </div>
    <div class="agent-node specialist coder">
      <div class="an-icon">💻</div>
      <div class="an-label">Coder</div>
      <div class="an-tasks">writes + runs code</div>
    </div>
  </div>
</div>

Each specialist has a narrow, focused system prompt — it only knows what it needs to do its one job well. The orchestrator holds the big picture.

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Pros and Cons — Side by Side

<div class="proscons-grid">
  <div class="proscons-card single-pros">
    <div class="pc-header">✅ Single — pros</div>
    <div class="pc-body">
      ✦ Simple to build and debug<br>
      ✦ One context → coherent output<br>
      ✦ No coordination overhead<br>
      ✦ Easier to trace what went wrong
    </div>
  </div>
  <div class="proscons-card single-cons">
    <div class="pc-header">⚠️ Single — cons</div>
    <div class="pc-body">
      ✦ Context window fills up on long tasks<br>
      ✦ Generalist prompt = diluted quality<br>
      ✦ Sequential — no parallelism<br>
      ✦ One failure breaks the whole task
    </div>
  </div>
  <div class="proscons-card multi-pros">
    <div class="pc-header">✅ Multi — pros</div>
    <div class="pc-body">
      ✦ Each agent is expert in its role<br>
      ✦ Parallel execution = faster results<br>
      ✦ Isolated failures — others continue<br>
      ✦ Scales to arbitrarily complex tasks
    </div>
  </div>
  <div class="proscons-card multi-cons">
    <div class="pc-header">⚠️ Multi — cons</div>
    <div class="pc-body">
      ✦ Much harder to build and debug<br>
      ✦ Handoff errors compound across agents<br>
      ✦ More API calls = higher cost and latency<br>
      ✦ Requires clear interface between agents
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## When to Use Each

<table class="decision-table">
  <tr>
    <th>Situation</th>
    <th>Architecture</th>
    <th>Why</th>
  </tr>
  <tr>
    <td>Simple task with 2–4 clear steps</td>
    <td><span class="arch-tag single">Single</span></td>
    <td>No coordination overhead. One context is enough.</td>
  </tr>
  <tr>
    <td>Task fits in one context window</td>
    <td><span class="arch-tag single">Single</span></td>
    <td>Multi-agent adds complexity with no benefit here.</td>
  </tr>
  <tr>
    <td>High quality needed — separate review pass</td>
    <td><span class="arch-tag multi">Multi</span></td>
    <td>Writer + Reviewer pattern reliably improves output.</td>
  </tr>
  <tr>
    <td>Subtasks are independent and parallelisable</td>
    <td><span class="arch-tag multi">Multi</span></td>
    <td>Run simultaneously instead of waiting sequentially.</td>
  </tr>
  <tr>
    <td>Task exceeds context window limits</td>
    <td><span class="arch-tag multi">Multi</span></td>
    <td>Split into stages — each agent gets a fresh context.</td>
  </tr>
  <tr>
    <td>Research + writing + code in one workflow</td>
    <td><span class="arch-tag multi">Multi</span></td>
    <td>Each domain benefits from a specialised system prompt.</td>
  </tr>
  <tr>
    <td>You're just getting started with agents</td>
    <td><span class="arch-tag single">Single</span></td>
    <td>Understand the limits of one agent before adding more.</td>
  </tr>
</table>

---

<!-- _class: step -->

<div class="step-badge">VISUAL</div>

## The Multi-Agent Workflow — Message by Message

A technical blog post agent: Orchestrator delegates to Researcher, Writer, then Reviewer.

<div class="workflow-full">
  <div class="wf-row">
    <span class="wf-badge user">User</span>
    <span class="wf-arrow-h">→</span>
    <span class="wf-msg">"Write a technical post on N-1 contingency analysis for a non-engineer audience."</span>
  </div>
  <div class="wf-row">
    <span class="wf-badge orch">Orchestrator</span>
    <span class="wf-arrow-h">→</span>
    <span class="wf-msg">Researcher: "Find 3 clear explanations of N-1 contingency. Return key concepts only."</span>
  </div>
  <div class="wf-row">
    <span class="wf-badge res">Researcher</span>
    <span class="wf-arrow-h">→</span>
    <span class="wf-msg">Returns: [3 concept summaries from retrieved sources]</span>
  </div>
  <div class="wf-row">
    <span class="wf-badge orch">Orchestrator</span>
    <span class="wf-arrow-h">→</span>
    <span class="wf-msg">Writer: "Using these concepts, write a 400-word post. Direct tone, no jargon, real-world analogy."</span>
  </div>
  <div class="wf-row">
    <span class="wf-badge write">Writer</span>
    <span class="wf-arrow-h">→</span>
    <span class="wf-msg">Returns: [400-word draft post]</span>
  </div>
  <div class="wf-row">
    <span class="wf-badge orch">Orchestrator</span>
    <span class="wf-arrow-h">→</span>
    <span class="wf-msg">Reviewer: "Score this 1–10 for clarity and accuracy. List any jargon or unclear claims."</span>
  </div>
  <div class="wf-row">
    <span class="wf-badge review">Reviewer</span>
    <span class="wf-arrow-h">→</span>
    <span class="wf-msg">Score: 8/10. Flag: "power flow" unexplained. Suggest: replace with "electricity routing".</span>
  </div>
  <div class="wf-row">
    <span class="wf-badge output">Output</span>
    <span class="wf-arrow-h">→</span>
    <span class="wf-msg">Orchestrator applies feedback, returns final revised post to user.</span>
  </div>
</div>

---

## The Mental Model

<div class="two-col">
  <div class="col-card">
    <div class="label">🤖 Single agent = solo developer</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">Does everything from requirements to deployment. Fast for small projects. Bottleneck for large ones. Quality limited by one person's range.</p>
  </div>
  <div class="col-card">
    <div class="label">🤝 Multi-agent = engineering team</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">Researcher, writer, reviewer, coder — each expert in one thing. Coordination costs exist, but the total output quality and scale is higher.</p>
  </div>
</div>

<div class="highlight good">

**Where to start:** build single-agent first. Run it until it hits a wall — context too long, quality inconsistent, tasks too diverse. That wall tells you exactly which specialist to split off first.

</div>

---

<!-- _class: final -->

# One agent to start.
# Many agents to scale.

&nbsp;

Understand the limits of one before adding more. The architecture follows the problem.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*