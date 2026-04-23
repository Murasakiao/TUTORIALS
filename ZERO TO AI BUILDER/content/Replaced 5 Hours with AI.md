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

  /* Before / after time comparison */
  .time-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 16px 0;
  }

  .time-col {
    border-radius: 12px;
    overflow: hidden;
  }

  .time-col .tc-header {
    padding: 10px 18px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }

  .time-col.before .tc-header { background: #7f1d1d; color: #fca5a5; }
  .time-col.after  .tc-header { background: #14532d; color: #86efac; }

  .time-col .tc-body {
    background: #0d1117;
    padding: 14px 18px;
  }

  .time-col.before .tc-body { border: 1px solid #7f1d1d; border-top: none; border-radius: 0 0 12px 12px; }
  .time-col.after  .tc-body { border: 1px solid #14532d; border-top: none; border-radius: 0 0 12px 12px; }

  .time-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 7px 0;
    border-bottom: 1px solid #21262d;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
  }

  .time-row:last-child { border-bottom: none; }

  .time-row .tr-task { color: #9ca3af; }
  .time-col.before .time-row .tr-time { color: #f87171; font-weight: 600; }
  .time-col.after  .time-row .tr-time { color: #86efac; font-weight: 600; }

  .time-col .tc-total {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0 0 0;
    margin-top: 4px;
    font-family: 'DM Mono', monospace;
    font-size: 14px;
    font-weight: 700;
  }

  .time-col.before .tc-total { color: #f87171; }
  .time-col.after  .tc-total { color: #86efac; }

  /* Tool stack cards */
  .tool-stack {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 14px 0;
  }

  .ts-card {
    background: #111827;
    border-radius: 10px;
    padding: 14px 18px;
    display: flex;
    gap: 14px;
    align-items: flex-start;
  }

  .ts-card .tsc-icon { font-size: 22px; flex-shrink: 0; margin-top: 2px; }

  .ts-card .tsc-body .tsc-name {
    font-weight: 600;
    font-size: 14px;
    color: #f0f6fc;
    margin-bottom: 3px;
  }

  .ts-card .tsc-body .tsc-role {
    font-size: 12px;
    color: #6b7280;
    line-height: 1.5;
  }

  .ts-card .tsc-body .tsc-cost {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    margin-top: 4px;
  }

  .ts-card .tsc-body .tsc-cost.free { color: #86efac; }
  .ts-card .tsc-body .tsc-cost.paid { color: #fde68a; }

  /* Workflow pipeline with times */
  .workflow-timed {
    background: #111827;
    border-radius: 10px;
    padding: 18px 22px;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .wt-step {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 10px;
  }

  .wt-step:last-child { margin-bottom: 0; }

  .wt-num {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: #2563eb;
    color: white;
    font-size: 11px;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }

  .wt-label { color: #f0f6fc; font-size: 13px; flex: 1; line-height: 1.4; }
  .wt-tool  { color: #60a5fa; font-size: 11px; min-width: 80px; text-align: right; flex-shrink: 0; }
  .wt-time  { color: #86efac; font-size: 11px; min-width: 50px; text-align: right; flex-shrink: 0; font-weight: 600; }

  /* Results stat cards */
  .result-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 14px;
    margin: 16px 0;
  }

  .result-card {
    background: #111827;
    border-radius: 10px;
    padding: 18px 16px;
    text-align: center;
    border-top: 3px solid #2563eb;
  }

  .result-card.rc-time  { border-top-color: #86efac; }
  .result-card.rc-qual  { border-top-color: #60a5fa; }
  .result-card.rc-freq  { border-top-color: #c4b5fd; }

  .result-card .rv-number {
    font-family: 'DM Mono', monospace;
    font-size: 36px;
    font-weight: 700;
    line-height: 1;
    margin-bottom: 6px;
  }

  .result-card.rc-time .rv-number { color: #86efac; }
  .result-card.rc-qual .rv-number { color: #60a5fa; }
  .result-card.rc-freq .rv-number { color: #c4b5fd; }

  .result-card .rv-label {
    font-size: 13px;
    font-weight: 600;
    color: #f0f6fc;
    margin-bottom: 4px;
  }

  .result-card .rv-detail {
    font-size: 11px;
    color: #6b7280;
    line-height: 1.5;
  }

  /* Lesson cards */
  .lesson-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 14px 0;
  }

  .lesson-card {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 14px 16px;
    display: flex;
    gap: 12px;
    align-items: flex-start;
  }

  .lesson-card .lc-num {
    font-family: 'DM Mono', monospace;
    font-size: 18px;
    font-weight: 700;
    color: #2563eb;
    flex-shrink: 0;
    line-height: 1.2;
    min-width: 24px;
  }

  .lesson-card .lc-body .lc-title {
    font-size: 14px;
    font-weight: 600;
    color: var(--text);
    margin-bottom: 3px;
  }

  .lesson-card .lc-body .lc-detail {
    font-size: 12px;
    color: var(--muted);
    line-height: 1.5;
  }

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

# How I Replaced 5 Hours
## of Work with AI

&nbsp;

**This isn't theory.** This is a real workflow I run every week.

`Claude` · `Python` · `pandas` · `n8n` · `Substack`

---

## The Problem I Had Every Week

As an engineer and content creator, my week had a recurring bottleneck: two completely different workloads, both demanding, neither helping the other.

<div class="tools">
  <div class="tool-card">
    <div class="icon">⚡</div>
    <div class="name">Engineering work</div>
    <div class="desc">Power flow analysis, N-1 contingency runs, grid data processing — all manual, all repetitive formatting and reporting.</div>
  </div>
  <div class="tool-card">
    <div class="icon">✍️</div>
    <div class="name">Content creation</div>
    <div class="desc">Substack posts, LinkedIn carousels, Threads — each needing research, drafting, editing, and formatting from scratch.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔁</div>
    <div class="name">The pattern</div>
    <div class="desc">Same tasks, every week. Process grid results → write report. Pick a topic → draft post → edit → format → publish.</div>
  </div>
  <div class="tool-card">
    <div class="icon">⏱️</div>
    <div class="name">The cost</div>
    <div class="desc">5+ hours of weekly work that was either automatable or AI-acceleratable — I just hadn't built the systems yet.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">BEFORE vs AFTER</div>

## The Time Comparison

<div class="time-compare">
  <div class="time-col before">
    <div class="tc-header">❌ Before — manual workflow</div>
    <div class="tc-body">
      <div class="time-row"><span class="tr-task">Grid data cleaning + formatting</span><span class="tr-time">90 min</span></div>
      <div class="time-row"><span class="tr-task">Voltage flag report writing</span><span class="tr-time">45 min</span></div>
      <div class="time-row"><span class="tr-task">Substack draft + edit</span><span class="tr-time">90 min</span></div>
      <div class="time-row"><span class="tr-task">LinkedIn carousel creation</span><span class="tr-time">60 min</span></div>
      <div class="time-row"><span class="tr-task">Email summary to team</span><span class="tr-time">20 min</span></div>
      <div class="tc-total"><span>Total weekly</span><span>5h 25min</span></div>
    </div>
  </div>
  <div class="time-col after">
    <div class="tc-header">✅ After — AI-assisted workflow</div>
    <div class="tc-body">
      <div class="time-row"><span class="tr-task">Grid data cleaning + formatting</span><span class="tr-time">8 min</span></div>
      <div class="time-row"><span class="tr-task">Voltage flag report writing</span><span class="tr-time">5 min</span></div>
      <div class="time-row"><span class="tr-task">Substack draft + edit</span><span class="tr-time">25 min</span></div>
      <div class="time-row"><span class="tr-task">LinkedIn carousel creation</span><span class="tr-time">15 min</span></div>
      <div class="time-row"><span class="tr-task">Email summary to team</span><span class="tr-time">2 min</span></div>
      <div class="tc-total"><span>Total weekly</span><span>55 min</span></div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">TOOLS</div>

## What I Use and Why

<div class="tool-stack">
  <div class="ts-card">
    <div class="tsc-icon">🤖</div>
    <div class="tsc-body">
      <div class="tsc-name">Claude (Anthropic)</div>
      <div class="tsc-role">Writing, reasoning, code review, prompt-based content generation. My primary thinking partner for anything requiring language.</div>
      <div class="tsc-cost paid">claude.ai Pro — $20/mo</div>
    </div>
  </div>
  <div class="ts-card">
    <div class="tsc-icon">🐍</div>
    <div class="tsc-body">
      <div class="tsc-name">Python + pandas</div>
      <div class="tsc-role">All data pipeline work — CSV ingestion, voltage flagging, summary generation, report export. AI wrote 80% of the scripts.</div>
      <div class="tsc-cost free">Free — open source</div>
    </div>
  </div>
  <div class="ts-card">
    <div class="tsc-icon">🔄</div>
    <div class="tsc-body">
      <div class="tsc-name">n8n (self-hosted)</div>
      <div class="tsc-role">Automation orchestration — connects data pipeline outputs to email, Substack drafts, and Notion. Runs on Oracle Cloud Always Free.</div>
      <div class="tsc-cost free">Free — self-hosted</div>
    </div>
  </div>
  <div class="ts-card">
    <div class="tsc-icon">📝</div>
    <div class="tsc-body">
      <div class="tsc-name">Substack + Notion</div>
      <div class="tsc-role">Publishing and knowledge management. Notion stores my content system; n8n pushes AI-generated drafts directly into both.</div>
      <div class="tsc-cost free">Free tier sufficient</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">WORKFLOW</div>

## The Step-by-Step System

<div class="workflow-timed">
  <div class="wt-step">
    <div class="wt-num">1</div>
    <span class="wt-label">Drop weekly grid export CSV into watched folder</span>
    <span class="wt-tool">Manual</span>
    <span class="wt-time">1 min</span>
  </div>
  <div class="wt-step">
    <div class="wt-num">2</div>
    <span class="wt-label">Python pipeline cleans data, flags undervoltage buses, generates summary stats</span>
    <span class="wt-tool">Python/pandas</span>
    <span class="wt-time">Auto</span>
  </div>
  <div class="wt-step">
    <div class="wt-num">3</div>
    <span class="wt-label">n8n picks up output, sends summary.xlsx + flag count to email</span>
    <span class="wt-tool">n8n</span>
    <span class="wt-time">Auto</span>
  </div>
  <div class="wt-step">
    <div class="wt-num">4</div>
    <span class="wt-label">Claude prompted with grid results → writes plain-English insight post draft</span>
    <span class="wt-tool">Claude</span>
    <span class="wt-time">3 min</span>
  </div>
  <div class="wt-step">
    <div class="wt-num">5</div>
    <span class="wt-label">I edit the draft — voice, accuracy, remove anything generic</span>
    <span class="wt-tool">Manual</span>
    <span class="wt-time">15 min</span>
  </div>
  <div class="wt-step">
    <div class="wt-num">6</div>
    <span class="wt-label">n8n formats and pushes draft to Substack + Notion content log</span>
    <span class="wt-tool">n8n</span>
    <span class="wt-time">Auto</span>
  </div>
  <div class="wt-step">
    <div class="wt-num">7</div>
    <span class="wt-label">Review everything, approve for publish</span>
    <span class="wt-tool">Manual</span>
    <span class="wt-time">5 min</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">RESULTS</div>

## What Actually Changed

<div class="result-grid">
  <div class="result-card rc-time">
    <div class="rv-number">4.5h</div>
    <div class="rv-label">Saved per week</div>
    <div class="rv-detail">From 5h 25min down to 55 minutes on the same recurring work</div>
  </div>
  <div class="result-card rc-qual">
    <div class="rv-number">~80%</div>
    <div class="rv-label">AI contribution</div>
    <div class="rv-detail">AI writes the structure and first pass. I supply domain knowledge, voice, and final judgment.</div>
  </div>
  <div class="result-card rc-freq">
    <div class="rv-number">2×</div>
    <div class="rv-label">Publishing frequency</div>
    <div class="rv-detail">Went from one post every 2 weeks to one per week — same effort, higher output.</div>
  </div>
</div>

<div class="highlight good">

The engineering work didn't get worse — it got faster and more consistent. The content work didn't get generic — the AI handles structure, I supply the insight. Quality went up because I stopped spending energy on formatting and started spending it on thinking.

</div>

---

## Lessons That Actually Matter

<div class="lesson-grid">
  <div class="lesson-card">
    <div class="lc-num">1</div>
    <div class="lc-body">
      <div class="lc-title">Start with the task you hate most</div>
      <div class="lc-detail">The thing you dread every week is the highest-leverage automation target. I started with data cleaning — the most mechanical, least creative part.</div>
    </div>
  </div>
  <div class="lesson-card">
    <div class="lc-num">2</div>
    <div class="lc-body">
      <div class="lc-title">AI is a draft machine, not a publisher</div>
      <div class="lc-detail">Everything AI produces goes through my edit pass. The AI removes 80% of the effort. I still own 100% of the output.</div>
    </div>
  </div>
  <div class="lesson-card">
    <div class="lc-num">3</div>
    <div class="lc-body">
      <div class="lc-title">Build the pipeline once, run it forever</div>
      <div class="lc-detail">The Python script took 2 hours to build with AI help. It has now run 20+ times. That's 80:1 ROI on the setup time.</div>
    </div>
  </div>
  <div class="lesson-card">
    <div class="lc-num">4</div>
    <div class="lc-body">
      <div class="lc-title">Context is your biggest multiplier</div>
      <div class="lc-detail">The more context Claude has about my stack, voice, and audience, the less editing I do. System prompts are infrastructure.</div>
    </div>
  </div>
  <div class="lesson-card">
    <div class="lc-num">5</div>
    <div class="lc-body">
      <div class="lc-title">Free tools are genuinely enough</div>
      <div class="lc-detail">n8n on Oracle Free, Python, pandas — the only paid tool is Claude Pro at $20/month. The ROI on that alone is enormous.</div>
    </div>
  </div>
  <div class="lesson-card">
    <div class="lc-num">6</div>
    <div class="lc-body">
      <div class="lc-title">The work that remains is the real work</div>
      <div class="lc-detail">After AI handles the mechanical tasks, what's left is judgment, domain knowledge, and voice — the things that actually differentiate you.</div>
    </div>
  </div>
</div>

---

<!-- _class: final -->

# AI didn't replace my work.
# It replaced the work
# that was in the way.

&nbsp;

Build the system once. Spend your time on what only you can do.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*