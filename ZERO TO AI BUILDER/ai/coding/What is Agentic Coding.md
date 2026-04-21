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
  section.cover h2 { color: var(--white); border-bottom-color: #374151; }
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

  .highlight.danger {
    background: #fff1f2;
    border-color: #fecdd3;
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

  /* Three-mode comparison */
  .mode-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 14px;
    margin: 16px 0;
  }

  .mode-card {
    border-radius: 10px;
    padding: 18px 18px;
  }

  .mode-card.trad   { background: #111827; border: 2px solid #374151; }
  .mode-card.assist { background: #111827; border: 2px solid #1d4ed8; }
  .mode-card.agent  { background: #111827; border: 2px solid #166534; }

  .mode-card .mc-icon  { font-size: 26px; margin-bottom: 8px; }

  .mode-card .mc-title {
    font-family: 'DM Mono', monospace;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 6px;
  }

  .mode-card.trad   .mc-title { color: #9ca3af; }
  .mode-card.assist .mc-title { color: #60a5fa; }
  .mode-card.agent  .mc-title { color: #86efac; }

  .mode-card .mc-who {
    font-size: 11px;
    font-family: 'DM Mono', monospace;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 8px;
  }

  .mode-card.trad   .mc-who { color: #4b5563; }
  .mode-card.assist .mc-who { color: #3b82f6; }
  .mode-card.agent  .mc-who { color: #16a34a; }

  .mode-card .mc-desc {
    font-size: 12px;
    color: #9ca3af;
    line-height: 1.7;
  }

  /* Agent loop diagram */
  .agent-loop {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 0;
    align-items: center;
    margin: 18px 0;
  }

  .al-node {
    background: #111827;
    border-radius: 8px;
    padding: 14px 10px;
    text-align: center;
  }

  .al-node .aln-icon  { font-size: 20px; margin-bottom: 4px; }

  .al-node .aln-label {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 3px;
  }

  .al-node.n1 .aln-label { color: #60a5fa; }
  .al-node.n2 .aln-label { color: #c4b5fd; }
  .al-node.n3 .aln-label { color: #fde68a; }
  .al-node.n4 .aln-label { color: #f87171; }
  .al-node.n5 .aln-label { color: #86efac; }

  .al-node .aln-desc { font-size: 11px; color: #6b7280; line-height: 1.4; }

  .al-arrow {
    text-align: center;
    color: #374151;
    font-size: 16px;
    padding: 0 4px;
  }

  /* Real example cards */
  .example-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin: 14px 0;
  }

  .example-card {
    background: #111827;
    border-radius: 10px;
    padding: 16px 18px;
    border-left: 3px solid #166534;
  }

  .example-card .ec-tool {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: #86efac;
    font-weight: 600;
    margin-bottom: 6px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
  }

  .example-card .ec-task {
    font-size: 14px;
    font-weight: 600;
    color: #f0f6fc;
    margin-bottom: 6px;
    line-height: 1.4;
  }

  .example-card .ec-what {
    font-size: 12px;
    color: #9ca3af;
    line-height: 1.6;
  }

  .example-card .ec-what span { color: #60a5fa; font-family: 'DM Mono', monospace; font-size: 11px; }

  /* Human vs agent responsibility split */
  .split-table {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 14px 0;
  }

  .split-col {
    border-radius: 10px;
    overflow: hidden;
  }

  .split-col .sc-header {
    padding: 9px 16px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }

  .split-col.human .sc-header { background: #1e3a5f; color: #60a5fa; }
  .split-col.agent .sc-header { background: #14532d; color: #86efac; }

  .split-col .sc-body {
    background: #0d1117;
    padding: 12px 16px;
    font-size: 13px;
    line-height: 2;
  }

  .split-col.human .sc-body { border: 1px solid #1e3a5f; border-top: none; border-radius: 0 0 10px 10px; color: #93c5fd; }
  .split-col.agent .sc-body { border: 1px solid #14532d; border-top: none; border-radius: 0 0 10px 10px; color: #86efac; }

  /* When NOT grid */
  .not-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 14px 0;
  }

  .not-card {
    background: #fff1f2;
    border: 1px solid #fecdd3;
    border-radius: 8px;
    padding: 14px 16px;
    display: flex;
    gap: 12px;
    align-items: flex-start;
  }

  .not-card .nc-icon { font-size: 20px; flex-shrink: 0; margin-top: 1px; }

  .not-card .nc-body .nc-title { font-size: 14px; font-weight: 600; color: #9f1239; margin-bottom: 3px; }
  .not-card .nc-body .nc-desc  { font-size: 12px; color: #be123c; line-height: 1.5; }

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

# Agentic Coding
## What It Is and How It's Different

&nbsp;

**You used to write every line. Then you prompted for lines. Now you describe outcomes.**

`agent` · `loop` · `write` · `test` · `fix` · `supervisor`

---

## Three Modes of Coding with AI

The industry has moved through three distinct phases — and most people are still in the middle one.

<div class="mode-grid">
  <div class="mode-card trad">
    <div class="mc-icon">⌨️</div>
    <div class="mc-title">Traditional</div>
    <div class="mc-who">Human writes everything</div>
    <div class="mc-desc">You write every line. AI doesn't exist or isn't in the loop. Full control, full responsibility, full time.</div>
  </div>
  <div class="mode-card assist">
    <div class="mc-icon">💬</div>
    <div class="mc-title">AI-Assisted</div>
    <div class="mc-who">Human prompts, AI suggests</div>
    <div class="mc-desc">You describe a function. AI writes it. You review, edit, and paste it in. You're still driving every decision.</div>
  </div>
  <div class="mode-card agent">
    <div class="mc-icon">🤖</div>
    <div class="mc-title">Agentic</div>
    <div class="mc-who">Agent acts, human supervises</div>
    <div class="mc-desc">You describe a goal. The agent writes, runs, reads the output, fixes errors, and iterates — autonomously, across multiple files.</div>
  </div>
</div>

<div class="highlight">

The shift from assisted to agentic is not just faster coding — it's a different relationship with the work entirely.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## The Agent Loop — Write, Test, Fix

In agentic coding, the AI doesn't just respond to prompts. It runs a loop.

<div class="agent-loop">
  <div class="al-node n1">
    <div class="aln-icon">📋</div>
    <div class="aln-label">Task</div>
    <div class="aln-desc">You define the goal and constraints</div>
  </div>
  <div class="al-arrow">→</div>
  <div class="al-node n2">
    <div class="aln-icon">✍️</div>
    <div class="aln-label">Write</div>
    <div class="aln-desc">Agent writes code across files</div>
  </div>
  <div class="al-arrow">→</div>
  <div class="al-node n3">
    <div class="aln-icon">▶️</div>
    <div class="aln-label">Run</div>
    <div class="aln-desc">Agent executes code, reads output</div>
  </div>
  <div class="al-arrow">→</div>
  <div class="al-node n4">
    <div class="aln-icon">🔧</div>
    <div class="aln-label">Fix</div>
    <div class="aln-desc">Agent reads errors, edits code, reruns</div>
  </div>
  <div class="al-arrow">→</div>
  <div class="al-node n5">
    <div class="aln-icon">✅</div>
    <div class="aln-label">Done</div>
    <div class="aln-desc">Presents working result for review</div>
  </div>
</div>

This loop runs without you in it. The agent reads its own errors, searches documentation, rewrites functions, and tries again — the same way you would, but faster and without getting frustrated.

<div class="highlight warn">

The loop runs across **your actual filesystem**. Files get created, edited, and deleted. Always work in a git-tracked folder so you can undo.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Human as Supervisor

Your role changes completely in agentic coding. You're no longer a writer — you're a director.

<div class="split-table">
  <div class="split-col human">
    <div class="sc-header">👤 You do this</div>
    <div class="sc-body">
      ✦ Define the goal clearly<br>
      ✦ Set the constraints upfront<br>
      ✦ Review the plan before it runs<br>
      ✦ Approve or reject at checkpoints<br>
      ✦ Verify the final output<br>
      ✦ Catch domain-specific mistakes
    </div>
  </div>
  <div class="split-col agent">
    <div class="sc-header">🤖 Agent does this</div>
    <div class="sc-body">
      ✦ Reads and navigates your codebase<br>
      ✦ Creates, edits, deletes files<br>
      ✦ Runs code and reads output<br>
      ✦ Diagnoses and fixes its own errors<br>
      ✦ Searches docs and adjusts approach<br>
      ✦ Iterates until it passes
    </div>
  </div>
</div>

<div class="highlight">

**The skill that matters most now:** writing a clear, scoped task description. The better you define the goal and constraints, the less supervision the agent needs — and the less cleanup you do at the end.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Real Tools Doing This Today

<div class="example-grid">
  <div class="example-card">
    <div class="ec-tool">Claude Code</div>
    <div class="ec-task">Terminal-based agent that edits your actual codebase</div>
    <div class="ec-what">Reads files, writes functions, runs tests, fixes errors across multiple files in one session. <span>Works in your existing repo.</span></div>
  </div>
  <div class="example-card">
    <div class="ec-tool">Cursor / Windsurf</div>
    <div class="ec-task">IDE with an embedded agentic coding layer</div>
    <div class="ec-what">Indexes your full codebase for context. Agent mode writes and edits across files. <span>Full project awareness.</span></div>
  </div>
  <div class="example-card">
    <div class="ec-tool">GitHub Copilot Workspace</div>
    <div class="ec-task">Issue → plan → code → PR in one flow</div>
    <div class="ec-what">Takes a GitHub issue, proposes a plan, writes code, opens a PR. <span>End-to-end from spec to branch.</span></div>
  </div>
  <div class="example-card">
    <div class="ec-tool">Devin / OpenHands</div>
    <div class="ec-task">Fully autonomous coding agents</div>
    <div class="ec-what">Given a task, they browse docs, write code, run it, debug, deploy. <span>Closest thing to a fully autonomous developer.</span></div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## When NOT to Use Agentic Coding

More autonomy means more surface area for things to go wrong. These situations call for the manual approach.

<div class="not-grid">
  <div class="not-card">
    <div class="nc-icon">🔐</div>
    <div class="nc-body">
      <div class="nc-title">Security-critical code</div>
      <div class="nc-desc">Authentication, credential handling, payment flows. Too much risk in autonomous edits to code that must be exactly right.</div>
    </div>
  </div>
  <div class="not-card">
    <div class="nc-icon">🏗️</div>
    <div class="nc-body">
      <div class="nc-title">Architecture decisions</div>
      <div class="nc-desc">How the system is structured is a human call. Agents optimize locally — they can't see your long-term constraints.</div>
    </div>
  </div>
  <div class="not-card">
    <div class="nc-icon">🌐</div>
    <div class="nc-body">
      <div class="nc-title">Production without review</div>
      <div class="nc-desc">Never deploy agent-written code directly. Every output needs a human read before it touches production.</div>
    </div>
  </div>
  <div class="not-card">
    <div class="nc-icon">🧩</div>
    <div class="nc-body">
      <div class="nc-title">Highly domain-specific logic</div>
      <div class="nc-desc">Power flow constraints, regulatory thresholds, clinical rules. The agent doesn't know what it doesn't know about your domain.</div>
    </div>
  </div>
</div>

---

## Agentic vs Assisted — Side by Side

<div class="two-col">
  <div class="col-card">
    <div class="label">💬 AI-Assisted (what most people do)</div>
    <p style="font-size:14px; margin-top:8px; color:#374151; line-height:1.9;">
      ✦ You describe one function at a time<br>
      ✦ AI writes it, you paste it in<br>
      ✦ You run it, find the error, paste back<br>
      ✦ You manage the files yourself<br>
      ✦ Each exchange is one turn
    </p>
  </div>
  <div class="col-card">
    <div class="label">🤖 Agentic (what's coming next)</div>
    <p style="font-size:14px; margin-top:8px; color:#374151; line-height:1.9;">
      ✦ You describe the goal and scope<br>
      ✦ Agent writes, runs, reads, fixes<br>
      ✦ Agent handles multi-file changes<br>
      ✦ You review at checkpoints, not every line<br>
      ✦ Each session is an autonomous work block
    </p>
  </div>
</div>

<div class="highlight good">

**Where to start:** Claude Code in your terminal is the fastest on-ramp to agentic coding — open a repo, describe what you want to build, and watch it work. You can interrupt, redirect, or approve at any point.

</div>

---

<!-- _class: final -->

# Define the goal.
# Supervise the work.
# Own the result.

&nbsp;

The best engineers using agentic tools aren't doing less work — they're doing different work.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*