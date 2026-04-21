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

  /* ── AI vs Agent comparison ── */
  .versus-grid {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    gap: 0;
    align-items: stretch;
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 16px 0;
  }

  .vs-side {
    padding: 18px 20px;
  }

  .vs-side.ai    { background: var(--off-white); }
  .vs-side.agent { background: #f5f3ff; }

  .vs-side .vs-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 10px;
  }

  .vs-side.ai    .vs-label { color: var(--muted); }
  .vs-side.agent .vs-label { color: #5b21b6; }

  .vs-side .vs-title {
    font-weight: 700;
    font-size: 18px;
    color: var(--text);
    margin-bottom: 10px;
  }

  .vs-side .vs-item {
    font-size: 13.5px;
    color: var(--muted);
    padding: 5px 0;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: flex-start;
    gap: 8px;
  }

  .vs-side .vs-item:last-child { border-bottom: none; }

  .vs-side .vs-item .vi-icon { flex-shrink: 0; font-size: 15px; }
  .vs-side.agent .vs-item     { border-bottom-color: #ede9fe; }

  .vs-divider {
    background: var(--border);
    width: 1px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 13px;
    color: var(--muted);
    writing-mode: horizontal-tb;
    padding: 0 14px;
    background: var(--white);
    border-left: 1px solid var(--border);
    border-right: 1px solid var(--border);
  }

  /* ── ReAct loop diagram ── */
  .react-loop {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0;
    margin: 16px 0;
    position: relative;
  }

  .rl-node {
    border-radius: 12px;
    padding: 14px 16px;
    text-align: center;
    min-width: 115px;
    flex-shrink: 0;
  }

  .rl-node .rn-icon  { font-size: 26px; margin-bottom: 4px; }
  .rl-node .rn-label { font-weight: 700; font-size: 13px; text-transform: uppercase; letter-spacing: 0.06em; }
  .rl-node .rn-desc  { font-size: 11.5px; color: inherit; opacity: 0.75; margin-top: 3px; line-height: 1.4; }

  .rl-node.observe  { background: #f0fdf4; border: 2px solid #86efac; }
  .rl-node.think    { background: #f5f3ff; border: 2px solid #c4b5fd; }
  .rl-node.act      { background: var(--blue-light); border: 2px solid var(--blue-mid); }
  .rl-node.result   { background: #fef3c7; border: 2px solid #fde68a; }

  .rl-node.observe .rn-label { color: #166534; }
  .rl-node.think   .rn-label { color: #5b21b6; }
  .rl-node.act     .rn-label { color: #1e40af; }
  .rl-node.result  .rn-label { color: #92400e; }

  .rl-arrow {
    padding: 0 8px;
    font-size: 20px;
    color: var(--blue);
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
    height: 2px;
    background: var(--border);
    flex: 1;
    border-radius: 999px;
    max-width: 80px;
  }

  /* ── Tool card grid ── */
  .tool-pill-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 10px;
    margin-top: 14px;
  }

  .tool-pill {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px 14px;
    display: flex;
    align-items: flex-start;
    gap: 10px;
  }

  .tool-pill .tp-icon { font-size: 20px; flex-shrink: 0; }

  .tool-pill .tp-name {
    font-weight: 600;
    font-size: 13px;
    color: var(--text);
    margin-bottom: 2px;
  }

  .tool-pill .tp-desc {
    font-size: 12px;
    color: var(--muted);
    line-height: 1.45;
  }

  /* ── Memory types ── */
  .memory-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .memory-card {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .memory-card .mem-header {
    padding: 9px 14px;
    font-weight: 600;
    font-size: 13px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border);
  }

  .memory-card.short  .mem-header { background: #fef3c7; color: #92400e; border-color: #fde68a; }
  .memory-card.long   .mem-header { background: #f0fdf4; color: #166534; border-color: #bbf7d0; }
  .memory-card.episod .mem-header { background: var(--blue-light); color: #1e40af; border-color: var(--blue-mid); }
  .memory-card.extern .mem-header { background: #f5f3ff; color: #5b21b6; border-color: #ddd6fe; }

  .memory-card .mem-body {
    padding: 10px 14px;
    background: var(--white);
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.55;
  }

  .memory-card .mem-example {
    padding: 7px 14px;
    background: var(--off-white);
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    border-top: 1px solid var(--border);
  }

  /* ── Real-world example walkthrough ── */
  .agent-trace {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
    margin: 14px 0;
  }

  .agent-trace .at-bar {
    background: var(--text);
    padding: 9px 16px;
    font-family: 'DM Mono', monospace;
    font-size: 11.5px;
    color: #9ca3af;
    letter-spacing: 0.04em;
  }

  .agent-trace .at-body {
    padding: 12px 16px;
    display: flex;
    flex-direction: column;
    gap: 7px;
  }

  .at-step {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 10px 13px;
  }

  .at-step .as-badge {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    font-weight: 600;
    padding: 3px 8px;
    border-radius: 4px;
    flex-shrink: 0;
    margin-top: 1px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }

  .as-badge.observe { background: #f0fdf4; color: #166534; border: 1px solid #bbf7d0; }
  .as-badge.think   { background: #f5f3ff; color: #5b21b6; border: 1px solid #ddd6fe; }
  .as-badge.act     { background: var(--blue-light); color: #1e40af; border: 1px solid var(--blue-mid); }
  .as-badge.result  { background: #fef3c7; color: #92400e; border: 1px solid #fde68a; }

  .at-step .as-text {
    font-size: 13px;
    color: var(--text);
    line-height: 1.5;
  }

  .at-step .as-text .as-tool {
    font-family: 'DM Mono', monospace;
    font-size: 11.5px;
    color: var(--blue);
    background: var(--blue-light);
    padding: 1px 6px;
    border-radius: 3px;
  }

  /* ── Real-world examples ── */
  .example-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .example-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 13px 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }

  .example-card .ec-icon { font-size: 24px; flex-shrink: 0; }

  .example-card .ec-title {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
    margin-bottom: 3px;
  }

  .example-card .ec-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.5;
  }

  .example-card .ec-tools {
    display: flex;
    gap: 5px;
    flex-wrap: wrap;
    margin-top: 6px;
  }

  .example-card .ec-tool {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    padding: 2px 6px;
    border-radius: 3px;
    background: var(--blue-light);
    color: #1e40af;
    border: 1px solid var(--blue-mid);
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

# What Is an AI Agent
## in Plain English

&nbsp;

**Not a chatbot. Not a script. Something in between — and more powerful than both.**

`observe` · `reason` · `act` · `tools` · `memory` · `loop`

---

## AI vs Agent — the Core Difference

A regular AI answers your question. An agent **takes action** to complete a goal — on its own, step by step, using tools.

<div class="versus-grid">
  <div class="vs-side ai">
    <div class="vs-label">💬 &nbsp;Regular AI (ChatGPT, Claude)</div>
    <div class="vs-title">You ask. It answers.</div>
    <div class="vs-item"><span class="vi-icon">→</span> You write the prompt manually</div>
    <div class="vs-item"><span class="vi-icon">→</span> One response per message</div>
    <div class="vs-item"><span class="vi-icon">→</span> Can't browse, run code, or click</div>
    <div class="vs-item"><span class="vi-icon">→</span> Forgets everything next session</div>
    <div class="vs-item"><span class="vi-icon">→</span> You decide what to do with the answer</div>
  </div>
  <div class="vs-divider">vs</div>
  <div class="vs-side agent">
    <div class="vs-label">🤖 &nbsp;AI Agent</div>
    <div class="vs-title">You set the goal. It works.</div>
    <div class="vs-item"><span class="vi-icon">→</span> You give a high-level objective</div>
    <div class="vs-item"><span class="vi-icon">→</span> Takes multiple steps autonomously</div>
    <div class="vs-item"><span class="vi-icon">→</span> Uses tools: search, code, files, APIs</div>
    <div class="vs-item"><span class="vi-icon">→</span> Remembers context across steps</div>
    <div class="vs-item"><span class="vi-icon">→</span> Acts on the result — sends emails, updates databases</div>
  </div>
</div>

<div class="highlight">

**The analogy:** A regular AI is a calculator — ask a question, get an answer. An agent is an intern — give them a goal, they figure out the steps, use the available tools, and report back when done.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## The Observe → Think → Act Loop

Agents don't run once and stop. They loop — observing what happened, deciding what to do next, and acting again — until the goal is complete.

<div class="react-loop">
  <div class="rl-node observe">
    <div class="rn-icon">👁️</div>
    <div class="rn-label">Observe</div>
    <div class="rn-desc">Read the current state. What just happened? What do I know?</div>
  </div>
  <div class="rl-arrow">→</div>
  <div class="rl-node think">
    <div class="rn-icon">🧠</div>
    <div class="rn-label">Think</div>
    <div class="rn-desc">Reason about what to do next. Which tool? Which step?</div>
  </div>
  <div class="rl-arrow">→</div>
  <div class="rl-node act">
    <div class="rn-icon">⚡</div>
    <div class="rn-label">Act</div>
    <div class="rn-desc">Call a tool. Search, write, calculate, send, save.</div>
  </div>
  <div class="rl-arrow">→</div>
  <div class="rl-node result">
    <div class="rn-icon">📋</div>
    <div class="rn-label">Result</div>
    <div class="rn-desc">Tool returns output. Now observe again — is the goal done?</div>
  </div>
</div>

<div class="rl-loop-back">
  <div class="rl-loop-line"></div>
  <span>↩ &nbsp;loop until goal is complete&nbsp; ↺</span>
  <div class="rl-loop-line"></div>
</div>

<div class="two-col" style="margin-top:14px;">
  <div class="col-card">
    <div class="label">How many loops?</div>
    <p style="font-size:13.5px; margin-top:6px;">Depends on the task. Booking a flight might take 4–6 loops. Researching and writing a report could take 20+. The agent decides when it's done.</p>
  </div>
  <div class="col-card">
    <div class="label">When does it stop?</div>
    <p style="font-size:13.5px; margin-top:6px;">When the goal is satisfied, when it hits a defined step limit, or when it determines it cannot proceed and asks a human for help.</p>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Tools — What Agents Can Do

A tool is anything the agent can call to interact with the world. Without tools, an agent can only think — it can't act.

<div class="tool-pill-grid">
  <div class="tool-pill">
    <div class="tp-icon">🔍</div>
    <div>
      <div class="tp-name">Web search</div>
      <div class="tp-desc">Look up current information, prices, news, documentation</div>
    </div>
  </div>
  <div class="tool-pill">
    <div class="tp-icon">💻</div>
    <div>
      <div class="tp-name">Code execution</div>
      <div class="tp-desc">Run Python, analyse data, do maths, process files</div>
    </div>
  </div>
  <div class="tool-pill">
    <div class="tp-icon">📁</div>
    <div>
      <div class="tp-name">File system</div>
      <div class="tp-desc">Read, write, create, and organise files and folders</div>
    </div>
  </div>
  <div class="tool-pill">
    <div class="tp-icon">📧</div>
    <div>
      <div class="tp-name">Email / calendar</div>
      <div class="tp-desc">Read inbox, send replies, create events, check availability</div>
    </div>
  </div>
  <div class="tool-pill">
    <div class="tp-icon">🌐</div>
    <div>
      <div class="tp-name">Browser control</div>
      <div class="tp-desc">Navigate websites, fill forms, click buttons, extract data</div>
    </div>
  </div>
  <div class="tool-pill">
    <div class="tp-icon">🗄️</div>
    <div>
      <div class="tp-name">Database</div>
      <div class="tp-desc">Query, insert, update records across SQL or NoSQL systems</div>
    </div>
  </div>
  <div class="tool-pill">
    <div class="tp-icon">🔌</div>
    <div>
      <div class="tp-name">External APIs</div>
      <div class="tp-desc">Slack, GitHub, Notion, Stripe — any service with an API</div>
    </div>
  </div>
  <div class="tool-pill">
    <div class="tp-icon">🧠</div>
    <div>
      <div class="tp-name">Other AI models</div>
      <div class="tp-desc">Call a specialised model — image generation, transcription, translation</div>
    </div>
  </div>
  <div class="tool-pill">
    <div class="tp-icon">💾</div>
    <div>
      <div class="tp-name">Memory store</div>
      <div class="tp-desc">Save and retrieve facts across sessions — what it learned before</div>
    </div>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**The agent decides which tool to use.** You give it a goal and a toolbox. It figures out which tools to call, in which order, based on what it observes at each step.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Memory — How Agents Remember

Agents have four types of memory — each serving a different purpose.

<div class="memory-grid">
  <div class="memory-card short">
    <div class="mem-header">⚡ &nbsp;Short-term (context window)</div>
    <div class="mem-body">Everything in the current conversation — the goal, tool outputs, observations so far. Cleared when the session ends. This is the agent's "working memory."</div>
    <div class="mem-example">Limit: ~200k tokens. Enough for long tasks.</div>
  </div>
  <div class="memory-card long">
    <div class="mem-header">💾 &nbsp;Long-term (persistent)</div>
    <div class="mem-body">Facts saved to a database between sessions — user preferences, past decisions, learned patterns. The agent writes to it explicitly during a run.</div>
    <div class="mem-example">Stored in: SQLite, Postgres, a JSON file</div>
  </div>
  <div class="memory-card episod">
    <div class="mem-header">📖 &nbsp;Episodic (past runs)</div>
    <div class="mem-body">Logs of what the agent did in previous sessions. Lets it learn from past mistakes — "last time I tried X, it failed. Try Y instead."</div>
    <div class="mem-example">Stored in: log files, vector databases</div>
  </div>
  <div class="memory-card extern">
    <div class="mem-header">🔗 &nbsp;External (retrieval)</div>
    <div class="mem-body">A large document store the agent searches when it needs information — company wikis, documentation, past reports. It retrieves only what's relevant.</div>
    <div class="mem-example">Stored in: vector DBs — Pinecone, Chroma</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## A Real Agent Trace — Step by Step

**Goal given to agent:** "Find the three cheapest flights from Manila to Singapore next month and summarise them."

<div class="agent-trace">
  <div class="at-bar">agent reasoning trace — each loop iteration</div>
  <div class="at-body">
    <div class="at-step">
      <span class="as-badge observe">Observe</span>
      <span class="as-text">Goal received: find cheapest MNL → SIN flights next month. I have access to a web search tool and a code execution tool.</span>
    </div>
    <div class="at-step">
      <span class="as-badge think">Think</span>
      <span class="as-text">I should search for flight prices first. I'll use <span class="as-tool">web_search</span> with query "cheapest flights Manila Singapore May 2026".</span>
    </div>
    <div class="at-step">
      <span class="as-badge act">Act</span>
      <span class="as-text">Calling <span class="as-tool">web_search("cheapest MNL SIN flights May 2026")</span> → returns 12 results with prices from Google Flights, Skyscanner, and airline sites.</span>
    </div>
    <div class="at-step">
      <span class="as-badge observe">Observe</span>
      <span class="as-text">Results show: Cebu Pacific ₱3,200 (May 8), AirAsia ₱3,850 (May 12), Philippine Airlines ₱4,100 (May 5). Three cheapest identified.</span>
    </div>
    <div class="at-step">
      <span class="as-badge think">Think</span>
      <span class="as-text">I have the data I need. Goal is complete. I'll format this into a clear summary for the user.</span>
    </div>
    <div class="at-step">
      <span class="as-badge result">Result</span>
      <span class="as-text">Summary returned with airline, price, date, and booking link for each of the three cheapest options. Task complete in 2 loops.</span>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## Real-World Agent Examples

<div class="example-grid">
  <div class="example-card">
    <div class="ec-icon">🔬</div>
    <div>
      <div class="ec-title">Research agent</div>
      <div class="ec-desc">Given a topic, searches the web, reads multiple sources, synthesises findings, and writes a structured report — without you touching anything.</div>
      <div class="ec-tools">
        <span class="ec-tool">web_search</span>
        <span class="ec-tool">browser</span>
        <span class="ec-tool">write_file</span>
      </div>
    </div>
  </div>
  <div class="example-card">
    <div class="ec-icon">💻</div>
    <div>
      <div class="ec-title">Coding agent (Claude Code)</div>
      <div class="ec-desc">Given a task, reads your codebase, writes code, runs tests, reads errors, fixes bugs, and commits — iterating until the tests pass.</div>
      <div class="ec-tools">
        <span class="ec-tool">read_file</span>
        <span class="ec-tool">write_file</span>
        <span class="ec-tool">run_terminal</span>
      </div>
    </div>
  </div>
  <div class="example-card">
    <div class="ec-icon">📊</div>
    <div>
      <div class="ec-title">Data analyst agent</div>
      <div class="ec-desc">Loads a CSV, runs Python code to explore the data, generates charts, interprets trends, and writes an executive summary with key findings.</div>
      <div class="ec-tools">
        <span class="ec-tool">code_exec</span>
        <span class="ec-tool">read_file</span>
        <span class="ec-tool">write_file</span>
      </div>
    </div>
  </div>
  <div class="example-card">
    <div class="ec-icon">🛒</div>
    <div>
      <div class="ec-title">Shopping / booking agent</div>
      <div class="ec-desc">Given constraints (budget, dates, preferences), searches multiple sources, compares options, and presents a ranked shortlist — or completes the booking.</div>
      <div class="ec-tools">
        <span class="ec-tool">web_search</span>
        <span class="ec-tool">browser</span>
        <span class="ec-tool">send_email</span>
      </div>
    </div>
  </div>
  <div class="example-card">
    <div class="ec-icon">📬</div>
    <div>
      <div class="ec-title">Email triage agent</div>
      <div class="ec-desc">Reads your inbox, categorises every email, drafts replies for routine messages, flags urgent ones, and archives the rest — on a schedule.</div>
      <div class="ec-tools">
        <span class="ec-tool">read_email</span>
        <span class="ec-tool">send_email</span>
        <span class="ec-tool">memory</span>
      </div>
    </div>
  </div>
  <div class="example-card">
    <div class="ec-icon">🏢</div>
    <div>
      <div class="ec-title">Business ops agent</div>
      <div class="ec-desc">Monitors a Slack channel for customer issues, looks up their account in the CRM, drafts a response, creates a follow-up task, and notifies the right team.</div>
      <div class="ec-tools">
        <span class="ec-tool">slack_api</span>
        <span class="ec-tool">crm_query</span>
        <span class="ec-tool">create_task</span>
      </div>
    </div>
  </div>
</div>

---

## AI Agent Quick Reference

<table class="cheat-table">
  <tr>
    <th>Concept</th>
    <th>Plain English</th>
  </tr>
  <tr>
    <td><strong>Agent</strong></td>
    <td>An AI that takes a goal and acts on it autonomously — searching, writing, calling APIs, looping until done</td>
  </tr>
  <tr>
    <td><strong>Tool</strong></td>
    <td>A function the agent can call — web search, code runner, email sender, database query. Each tool has a name, inputs, and outputs</td>
  </tr>
  <tr>
    <td><strong>Loop</strong></td>
    <td>Observe → Think → Act → repeat. The agent loops until the goal is satisfied or it hits a step limit</td>
  </tr>
  <tr>
    <td><strong>Context window</strong></td>
    <td>The agent's short-term memory — everything it can see right now. Cleared at end of session</td>
  </tr>
  <tr>
    <td><strong>Long-term memory</strong></td>
    <td>Facts saved to a database between sessions — user preferences, learned patterns, past decisions</td>
  </tr>
  <tr>
    <td><strong>RAG</strong></td>
    <td>Retrieval-Augmented Generation — the agent searches a document store and injects relevant text into its context before answering</td>
  </tr>
  <tr>
    <td><strong>ReAct pattern</strong></td>
    <td>The most common agent loop: Reason first ("I should search for X"), then Act ("calling web_search(X)"), then observe the result</td>
  </tr>
  <tr>
    <td><strong>Tool call</strong></td>
    <td>The agent outputs a structured JSON request to invoke a tool. Your code runs the tool and returns the result to the agent</td>
  </tr>
  <tr>
    <td><strong>Human-in-the-loop</strong></td>
    <td>A pause point where the agent asks a human to confirm before taking an irreversible action — sending an email, making a purchase</td>
  </tr>
</table>

---

<!-- _class: final -->

# An agent doesn't answer.
# It works.

&nbsp;

Goal in. Observe, think, act — loop. Result out. No hand-holding required.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*