---
marp: true
paginate: true
html: true
size: 4:3
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,400;0,500;0,600;1,400&family=DM+Mono:wght@400;500&display=swap');

  :root {
    --sans: 'DM Sans', system-ui, sans-serif;
    --mono: 'DM Mono', monospace;
    --white:       #f1f5f9;
    --off-white:   #cbd5e1;
    --subtle:      #94a3b8;
    --muted:       #64748b;
    --faint:       #334155;
    --bg:          #0a0a0a;
    --card-bg:     #131313;
    --card-border: #242424;
  }

  section {
    font-family: var(--sans);
    background: var(--bg);
    color: var(--white);
    padding: 44px 52px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    position: relative;
  }

  h1 {
    font-size: 38px;
    font-weight: 700;
    line-height: 1.08;
    margin: 0 0 14px 0;
    color: var(--white);
    letter-spacing: -1.5px;
  }
  h2 {
    font-size: 26px;
    font-weight: 700;
    line-height: 1.1;
    margin: 0 0 14px 0;
    color: var(--white);
    letter-spacing: -0.8px;
    border: none;
  }
  p {
    font-size: 16px;
    line-height: 1.6;
    color: var(--subtle);
    margin: 0 0 12px 0;
  }
  strong { color: var(--white); font-weight: 600; }
  em     { color: var(--muted); font-style: normal; }
  code {
    font-family: var(--mono);
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    color: var(--white);
    padding: 1px 6px;
    border-radius: 3px;
    font-size: 0.88em;
  }
  pre {
    font-family: var(--mono);
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    color: var(--off-white);
    padding: 16px 18px;
    border-radius: 4px;
    font-size: 14px;
    line-height: 1.6;
    margin: 0;
  }
  pre code { background: none; border: none; padding: 0; color: var(--off-white); }

  .tag {
    display: flex;
    align-items: center;
    gap: 12px;
    font-family: var(--mono);
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 3px;
    color: var(--off-white);
    text-transform: uppercase;
    margin-bottom: 18px;
  }
  .tag::before {
    content: '';
    display: block;
    width: 24px;
    height: 2px;
    background: var(--muted);
    flex-shrink: 0;
  }

  .header-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
  }
  .page-num {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--muted);
    letter-spacing: 2px;
    text-transform: uppercase;
  }
  .page-label {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--muted);
  }

  .cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-bottom: 12px;
  }
  .card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 4px;
    padding: 14px;
  }
  .card h3 {
    font-size: 14px;
    font-weight: 600;
    color: var(--white);
    margin: 0 0 4px;
  }
  .card p {
    font-size: 13px;
    color: var(--subtle);
    line-height: 1.45;
    margin: 0;
  }

  .cards-col { display: flex; flex-direction: column; gap: 8px; margin-bottom: 12px; }
  .card-row {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 4px;
    padding: 12px 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }
  .card-row-letter {
    font-family: var(--mono);
    font-size: 12px;
    color: var(--muted);
    flex-shrink: 0;
    margin-top: 1px;
    min-width: 16px;
  }
  .card-row-body h3 {
    font-size: 14px;
    font-weight: 600;
    color: var(--white);
    margin: 0 0 3px;
  }
  .card-row-body p {
    font-size: 13px;
    color: var(--subtle);
    margin: 0;
    line-height: 1.45;
  }

  .compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-bottom: 10px;
  }
  .compare-col {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 4px;
    padding: 14px 16px;
  }
  .compare-col.solid { border-color: var(--off-white); }
  .compare-label {
    font-family: var(--mono);
    font-size: 9px;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 6px;
    color: var(--muted);
  }
  .compare-label.solid { color: var(--white); }
  .compare-col h3 {
    font-size: 14px;
    font-weight: 600;
    color: var(--white);
    margin: 0 0 5px;
  }
  .compare-col p {
    font-size: 13px;
    color: var(--subtle);
    line-height: 1.45;
    margin: 0;
  }

  .list { display: flex; flex-direction: column; gap: 7px; margin-bottom: 12px; }
  .list-item {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 3px;
    padding: 10px 14px;
  }
  .list-num {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--muted);
    flex-shrink: 0;
    margin-top: 1px;
    min-width: 18px;
  }
  .list-text { font-size: 13.5px; color: var(--subtle); line-height: 1.45; }
  .list-text strong { color: var(--white); }

  .pill {
    display: inline-block;
    background: #050505;
    border: 1px solid var(--card-border);
    border-radius: 3px;
    padding: 2px 8px;
    font-family: var(--mono);
    font-size: 11px;
    color: var(--off-white);
  }

  .insight {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 4px;
    padding: 12px 18px;
    margin-top: auto;
  }
  .insight-label {
    font-family: var(--mono);
    font-size: 9px;
    letter-spacing: 3px;
    color: var(--muted);
    text-transform: uppercase;
    margin-bottom: 4px;
  }
  .insight p { font-size: 14px; color: var(--off-white); line-height: 1.5; margin: 0; }

  section.cover {
    justify-content: flex-end;
    padding-bottom: 80px;
    background: #050505;
  }
  section.cover h1 { font-size: 46px; }
  section.cover p  { font-size: 17px; color: var(--subtle); }

  section.divider {
    justify-content: center;
    border-left: 5px solid var(--off-white);
    background: #0d0d0d;
  }
  section.divider .tag { margin-bottom: 20px; }
  section.divider h1   { font-size: 42px; color: var(--white); margin-bottom: 10px; }
  section.divider p    { font-size: 15px; color: var(--muted); }

  section.cta {
    justify-content: center;
    align-items: center;
    text-align: center;
    background: #f1f5f9;
  }
  section.cta h1 { color: #0a0a0a; font-size: 38px; letter-spacing: -1px; margin-bottom: 10px; }
  section.cta h2 { color: #1e293b; font-size: 20px; border: none; margin-bottom: 12px; }
  section.cta p  { color: #475569; font-size: 15px; max-width: 540px; margin: 0; }
  section.cta .handle {
    font-family: var(--mono);
    font-size: 13px;
    color: #334155;
    margin-top: 22px;
    letter-spacing: 2px;
    text-transform: uppercase;
  }

  section::after {
    font-family: var(--mono);
    font-size: 9px;
    color: var(--muted);
    letter-spacing: 1px;
    content: 'PI CODING AGENT · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
    position: absolute;
    bottom: 20px;
    right: 40px;
  }
---

<!-- SLIDE 1 · COVER -->
<!-- _class: cover -->

<div class="tag">Minimal Guide</div>

# Pi Coding Agent

A provider-agnostic, MIT-licensed coding agent with a small core and everything else opt-in.

*4 default tools. 15+ providers. No SaaS backend.*

---

<!-- SLIDE 2 · WHAT IT IS -->

<div class="header-row">
  <span class="page-num">— i · hook —</span>
  <span class="page-label">what it is</span>
</div>

## What Pi actually is

<div class="cards-col">
  <div class="card-row">
    <span class="card-row-letter">A</span>
    <div class="card-row-body">
      <h3>4 default tools only</h3>
      <p>read, write, edit, bash. No plan mode, no sub-agents, no MCP out of the box.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-letter">B</span>
    <div class="card-row-body">
      <h3>Open source, MIT-licensed</h3>
      <p>Built by Mario Zechner (<code>earendil-works/pi</code>). Runs locally — no SaaS backend.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-letter">C</span>
    <div class="card-row-body">
      <h3>15+ providers</h3>
      <p>Anthropic, OpenAI, Google, Groq, and more — swappable at the API layer.</p>
    </div>
  </div>
</div>

---

<!-- SLIDE 3 · WHY PI -->

<div class="header-row">
  <span class="page-num">— ii · why pi —</span>
  <span class="page-label">control vs. convenience</span>
</div>

## Why choose Pi

<div class="compare">
  <div class="compare-col">
    <div class="compare-label">Claude Code / Codex</div>
    <h3>Opinionated, ready fast</h3>
    <p>Decisions made for you. Great defaults, less to configure.</p>
  </div>
  <div class="compare-col solid">
    <div class="compare-label solid">Pi</div>
    <h3>Provider-agnostic, shaped by you</h3>
    <p>No built-in permission system — you sandbox it yourself. That's the trade for flexibility.</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">proof it's real</div>
  <p>Powers OpenClaw. Used daily by engineers like Armin Ronacher, creator of Flask.</p>
</div>

---

<!-- SLIDE 4 · PHILOSOPHY -->

<div class="header-row">
  <span class="page-num">— iii · philosophy —</span>
  <span class="page-label">the core idea</span>
</div>

## Philosophy

<div class="cards">
  <div class="card">
    <h3>Adapt Pi to your workflow</h3>
    <p>Not the other way around. Pi bends to how you already build.</p>
  </div>
  <div class="card">
    <h3>Small core, opt-in everything</h3>
    <p>The base stays minimal. You add exactly what you need, nothing more.</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">the trade-off</div>
  <p>Less handed to you out of the box — more control over what your agent actually does.</p>
</div>

---

<!-- SLIDE 5 · THE 4 PILLARS -->

<div class="header-row">
  <span class="page-num">— iv · architecture —</span>
  <span class="page-label">the 4 pillars</span>
</div>

## The 4 pillars

<div class="list">
  <div class="list-item">
    <span class="list-num">A</span>
    <span class="list-text"><strong>Context</strong> — <code>AGENTS.md</code> and <code>SYSTEM.md</code> load project instructions before Pi acts</span>
  </div>
  <div class="list-item">
    <span class="list-num">B</span>
    <span class="list-text"><strong>Extensions</strong> — TypeScript modules adding tools, commands, and missing features, shared as Pi packages</span>
  </div>
  <div class="list-item">
    <span class="list-num">C</span>
    <span class="list-text"><strong>Skills</strong> — on-demand capability packages, loaded only when needed</span>
  </div>
  <div class="list-item">
    <span class="list-num">D</span>
    <span class="list-text"><strong>Memory</strong> — auto-compaction plus extension-injected context for long sessions</span>
  </div>
</div>

---

<!-- SLIDE 6 · HOW IT RUNS -->

<div class="header-row">
  <span class="page-num">— v · runtime —</span>
  <span class="page-label">how it runs</span>
</div>

## How it runs

<div class="cards">
  <div class="card">
    <h3>Interactive</h3>
    <p>A conversational terminal session for hands-on work.</p>
  </div>
  <div class="card">
    <h3>Print / JSON</h3>
    <p>Single-shot output for scripting and piping.</p>
  </div>
  <div class="card">
    <h3>RPC</h3>
    <p>Drive Pi programmatically over a structured protocol.</p>
  </div>
  <div class="card">
    <h3>SDK</h3>
    <p>Embed Pi directly inside your own application.</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">the point</div>
  <p>Pi is a runtime you can build on — not just a chatbot.</p>
</div>

---

<!-- SLIDE 7 · TRY IT -->

<div class="header-row">
  <span class="page-num">— vi · try it —</span>
  <span class="page-label">install & run</span>
</div>

## Try it

<pre><code>npm i -g @earendil-works/pi-coding-agent
pi</code></pre>

<div class="insight">
  <div class="insight-label">that's it</div>
  <p>One global install, one command. No account, no setup wizard.</p>
</div>

---

<!-- SLIDE 8 · TAKEAWAY -->

<div style="display:flex;flex-direction:column;justify-content:center;height:100%;text-align:center;align-items:center;">
  <div class="tag" style="justify-content:center;margin-bottom:24px;">vii · takeaway</div>
  <h1 style="font-size:46px;line-height:1.15;letter-spacing:-1.5px;">Shape it,<br>don't wait for it<br>to fit you</h1>
  <div class="compare" style="margin-top:24px;width:100%;">
    <div class="compare-col solid">
      <div class="compare-label solid">For</div>
      <p>People who want to shape their own workflow.</p>
    </div>
    <div class="compare-col">
      <div class="compare-label">Not for</div>
      <p>People who want zero setup and fixed decisions made for them.</p>
    </div>
  </div>
</div>

---

<!-- SLIDE 9 · CTA -->
<!-- _class: cta -->

<div class="tag" style="justify-content:center;color:#334155;margin-bottom:20px;">
  Pi Coding Agent
</div>

# Small core. Your rules.

## Install it, sandbox it, shape it.

<p><code>npm i -g @earendil-works/pi-coding-agent</code></p>

<div class="handle">earendil-works/pi</div>