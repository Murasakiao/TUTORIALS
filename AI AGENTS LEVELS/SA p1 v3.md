---
marp: true
theme: default
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,400;0,500;0,600;1,400&family=DM+Mono:wght@400;500&display=swap');

  :root {
    --teal: #2dd4bf;
    --teal-dim: #0d9488;
    --teal-mute: rgba(45,212,191,0.08);
    --teal-border: rgba(45,212,191,0.18);
    --bg: #111110;
    --bg-raised: #1a1a18;
    --bg-card: #1e1e1c;
    --bg-card-alt: #232321;
    --text: #e8e8e4;
    --text-sub: #a8a8a2;
    --muted: #66665e;
    --border: #2a2a28;
    --border-mid: #333330;
  }

  section {
    font-family: 'DM Sans', sans-serif;
    background: var(--bg-raised);
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
    border-bottom: 1px solid var(--border-mid);
    padding-bottom: 10px;
    margin-bottom: 22px;
    letter-spacing: -0.3px;
  }

  h3 {
    font-family: 'DM Sans', sans-serif;
    font-size: 19px;
    font-weight: 500;
    color: var(--teal);
    margin-bottom: 8px;
  }

  p { color: var(--text); margin: 0.4em 0; }
  ul { padding-left: 1.4em; }
  li { margin-bottom: 10px; color: var(--text-sub); }
  strong { color: var(--teal); font-weight: 600; }

  code {
    font-family: 'DM Mono', monospace;
    background: var(--teal-mute);
    color: var(--teal);
    border: 1px solid var(--teal-border);
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.87em;
  }

  blockquote {
    border-left: 2px solid var(--teal-dim);
    background: var(--teal-mute);
    padding: 16px 20px;
    margin: 20px 0;
    border-radius: 0 6px 6px 0;
    font-family: 'DM Mono', monospace;
    font-size: 0.82em;
    color: var(--teal);
    line-height: 1.6;
  }

  blockquote p { color: var(--teal); margin: 0; }

  /* ── Cover ── */
  section.cover {
    background: var(--bg);
    color: var(--text);
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
      radial-gradient(ellipse at 75% 15%, rgba(45,212,191,0.06) 0%, transparent 50%),
      radial-gradient(ellipse at 15% 90%, rgba(45,212,191,0.04) 0%, transparent 45%);
    pointer-events: none;
  }

  section.cover h1 { color: var(--text); font-size: 44px; letter-spacing: -0.8px; }
  section.cover h2 { color: var(--muted); border-bottom-color: var(--border); font-size: 20px; font-weight: 400; letter-spacing: 0; }
  section.cover p  { color: var(--muted); }
  section.cover strong { color: var(--teal); }
  section.cover code { background: rgba(45,212,191,0.07); color: var(--teal); border-color: rgba(45,212,191,0.2); }

  section.cover .series-badge {
    display: inline-block;
    background: transparent;
    color: var(--teal-dim);
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 500;
    padding: 4px 12px;
    border-radius: 3px;
    margin-bottom: 24px;
    letter-spacing: 0.1em;
    border: 1px solid rgba(45,212,191,0.2);
    width: fit-content;
  }

  /* step slides slightly lighter than base */
  section.step { background: var(--bg-card); }

  .highlight {
    background: var(--teal-mute);
    border: 1px solid var(--teal-border);
    border-radius: 7px;
    padding: 14px 20px;
    margin: 14px 0;
  }

  .highlight strong { color: var(--teal); }
  .highlight p { color: var(--text-sub); }

  /* ── Tools grid ── */
  .tools {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 16px;
  }

  .tool-card {
    background: var(--bg-card-alt);
    border: 1px solid var(--border-mid);
    border-radius: 8px;
    padding: 16px 20px;
  }

  .tool-card .icon  { font-size: 22px; margin-bottom: 6px; }
  .tool-card .name  { font-weight: 600; font-size: 15px; color: var(--text); }
  .tool-card .desc  { font-size: 13px; color: var(--muted); margin-top: 2px; }

  .step-badge {
    display: inline-block;
    background: transparent;
    color: var(--teal-dim);
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 500;
    padding: 3px 10px;
    border-radius: 3px;
    margin-bottom: 12px;
    letter-spacing: 0.1em;
    border: 1px solid rgba(45,212,191,0.18);
  }

  section.final {
    background: var(--bg);
    color: var(--text);
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
    background: radial-gradient(ellipse at 50% 50%, rgba(45,212,191,0.07) 0%, transparent 60%);
    pointer-events: none;
  }

  section.final h1 { color: var(--text); font-size: 40px; letter-spacing: -0.5px; }
  section.final p  { color: var(--text-sub); font-size: 18px; }
  section.final strong { color: var(--teal); }
  section.final em { color: var(--muted); }

  /* ── Two-column layout ── */
  .two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
    margin-top: 16px;
  }

  .col-card {
    background: var(--bg-card-alt);
    border: 1px solid var(--border-mid);
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

  /* ── AI vs Agent split ── */
  .versus-grid {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    gap: 0;
    align-items: stretch;
    border-radius: 9px;
    overflow: hidden;
    border: 1px solid var(--border-mid);
    margin: 14px 0;
  }

  .vs-side { padding: 16px 18px; }
  .vs-side.ai    { background: var(--bg-card); }
  .vs-side.agent { background: var(--bg-card-alt); }

  .vs-side .vs-label {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.09em;
    margin-bottom: 8px;
  }

  .vs-side.ai    .vs-label { color: var(--muted); }
  .vs-side.agent .vs-label { color: var(--teal-dim); }

  .vs-side .vs-title {
    font-weight: 700;
    font-size: 16px;
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
  .vs-side.agent .vs-item { border-bottom-color: var(--border-mid); color: var(--text-sub); }
  .vs-side .vs-item .vi-icon { flex-shrink: 0; color: var(--muted); }

  .vs-divider {
    background: var(--bg-raised);
    border-left: 1px solid var(--border-mid);
    border-right: 1px solid var(--border-mid);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 12px;
    font-weight: 600;
    font-size: 11px;
    color: var(--muted);
    font-family: 'DM Mono', monospace;
  }

  /* ── Problem → solution cards ── */
  .problem-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 12px;
  }

  .problem-card {
    border-radius: 7px;
    overflow: hidden;
    border: 1px solid var(--border-mid);
  }

  .problem-card .pc-head {
    padding: 8px 14px;
    font-weight: 600;
    font-size: 12.5px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border-mid);
  }

  .problem-card.problem  .pc-head { background: rgba(239,68,68,0.08);  color: #fca5a5; border-color: rgba(239,68,68,0.15); }
  .problem-card.solution .pc-head { background: rgba(45,212,191,0.07); color: var(--teal); border-color: var(--teal-border); }

  .problem-card .pc-body {
    padding: 11px 14px;
    background: var(--bg-card);
    font-size: 12.5px;
    color: var(--text-sub);
    line-height: 1.6;
  }

  /* ── LLM vs Agent anatomy ── */
  .anatomy-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 14px;
  }

  .anatomy-box {
    border-radius: 9px;
    overflow: hidden;
    border: 1px solid var(--border-mid);
  }

  .anatomy-box .ab-header {
    padding: 10px 14px;
    font-weight: 600;
    font-size: 13px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border-mid);
  }

  .anatomy-box.llm   .ab-header { background: var(--bg-card-alt); color: var(--text-sub); }
  .anatomy-box.agent .ab-header { background: rgba(45,212,191,0.07); color: var(--teal); border-color: var(--teal-border); }
  .anatomy-box.agent            { border-color: var(--teal-border); }

  .anatomy-box .ab-body {
    padding: 12px 14px;
    background: var(--bg-card);
    display: flex;
    flex-direction: column;
    gap: 7px;
  }

  .ab-layer {
    border-radius: 6px;
    padding: 9px 12px;
    font-size: 13px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .ab-layer .abl-icon { font-size: 17px; flex-shrink: 0; }
  .ab-layer .abl-name { font-weight: 600; font-size: 12.5px; color: var(--text); }
  .ab-layer .abl-desc { font-size: 11.5px; color: var(--muted); margin-top: 1px; }

  .ab-layer.core   { background: rgba(45,212,191,0.07);  border: 1px solid var(--teal-border); }
  .ab-layer.tools  { background: rgba(99,102,241,0.08);  border: 1px solid rgba(99,102,241,0.18); }
  .ab-layer.memory { background: rgba(34,197,94,0.07);   border: 1px solid rgba(34,197,94,0.18); }
  .ab-layer.loop   { background: rgba(168,85,247,0.07);  border: 1px solid rgba(168,85,247,0.18); }
  .ab-layer.plain  { background: var(--bg-card-alt);      border: 1px solid var(--border); }

  /* ── ReAct loop diagram ── */
  .react-loop {
    display: flex;
    align-items: stretch;
    justify-content: center;
    gap: 0;
    margin: 18px 0;
  }

  .rl-node {
    border-radius: 9px;
    padding: 14px 13px;
    text-align: center;
    min-width: 116px;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .rl-node .rn-icon  { font-size: 24px; margin-bottom: 5px; }
  .rl-node .rn-label { font-weight: 700; font-size: 11.5px; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 5px; }
  .rl-node .rn-ques  { font-family: 'DM Mono', monospace; font-size: 10px; opacity: 0.7; line-height: 1.45; }

  .rl-node.reason  { background: rgba(45,212,191,0.08);  border: 1px solid rgba(45,212,191,0.2); }
  .rl-node.act     { background: rgba(99,102,241,0.09);  border: 1px solid rgba(99,102,241,0.2); }
  .rl-node.observe { background: rgba(34,197,94,0.08);   border: 1px solid rgba(34,197,94,0.2); }
  .rl-node.decide  { background: rgba(168,85,247,0.08);  border: 1px solid rgba(168,85,247,0.2); }

  .rl-node.reason  .rn-label { color: var(--teal); }
  .rl-node.act     .rn-label { color: #818cf8; }
  .rl-node.observe .rn-label { color: #4ade80; }
  .rl-node.decide  .rn-label { color: #c084fc; }

  .rl-arrow {
    display: flex;
    align-items: center;
    padding: 0 8px;
    font-size: 16px;
    color: var(--border-mid);
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
    height: 1px;
    background: var(--border-mid);
    border-radius: 999px;
    flex: 1;
    max-width: 80px;
  }

  /* ── ReAct walkthrough ── */
  .react-walkthrough {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 9px;
    margin-top: 14px;
  }

  .rw-step {
    background: var(--bg-card-alt);
    border: 1px solid var(--border-mid);
    border-radius: 7px;
    padding: 11px 14px;
    display: flex;
    align-items: flex-start;
    gap: 10px;
  }

  .rw-step .rws-badge {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    font-weight: 600;
    padding: 3px 7px;
    border-radius: 3px;
    flex-shrink: 0;
    margin-top: 1px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    white-space: nowrap;
  }

  .rws-badge.reason  { background: rgba(45,212,191,0.1);  color: var(--teal);  border: 1px solid rgba(45,212,191,0.2); }
  .rws-badge.act     { background: rgba(99,102,241,0.1);  color: #818cf8;      border: 1px solid rgba(99,102,241,0.2); }
  .rws-badge.observe { background: rgba(34,197,94,0.1);   color: #4ade80;      border: 1px solid rgba(34,197,94,0.2); }
  .rws-badge.decide  { background: rgba(168,85,247,0.1);  color: #c084fc;      border: 1px solid rgba(168,85,247,0.2); }

  .rw-step .rws-text {
    font-size: 12.5px;
    color: var(--text-sub);
    line-height: 1.55;
  }

  .rw-step .rws-text .rws-tool {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--teal);
    background: var(--teal-mute);
    border: 1px solid var(--teal-border);
    padding: 1px 5px;
    border-radius: 3px;
  }

  /* ── Why it matters cards ── */
  .matters-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 14px;
  }

  .matters-card {
    background: var(--bg-card-alt);
    border: 1px solid var(--border-mid);
    border-radius: 7px;
    padding: 14px 15px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }

  .matters-card .mcc-icon { font-size: 22px; flex-shrink: 0; }

  .matters-card .mcc-title {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
    margin-bottom: 4px;
  }

  .matters-card .mcc-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.55;
  }

  /* ── Cheatsheet table ── */
  .cheat-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
    margin: 12px 0;
  }

  .cheat-table th {
    background: var(--bg-card-alt);
    color: var(--text-sub);
    padding: 8px 14px;
    text-align: left;
    font-weight: 500;
    font-size: 11px;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.08em;
    border-bottom: 1px solid var(--border-mid);
  }

  .cheat-table td {
    padding: 9px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text-sub);
  }

  .cheat-table tr:last-child td { border-bottom: none; }
  .cheat-table tr:nth-child(even) td { background: var(--bg-card-alt); }

  .cheat-table .mono {
    font-family: 'DM Mono', monospace;
    color: var(--teal);
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
    background: transparent;
    color: var(--teal);
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    min-width: 24px;
    height: 24px;
    border-radius: 4px;
    border: 1px solid rgba(45,212,191,0.25);
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

**Before you build one, understand what separates it from a plain LLM call.**

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