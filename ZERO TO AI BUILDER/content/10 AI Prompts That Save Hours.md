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

  /* Time-saved intro grid */
  .time-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin: 16px 0;
  }

  .time-card {
    background: #111827;
    border-radius: 10px;
    padding: 16px 18px;
    display: flex;
    align-items: center;
    gap: 14px;
  }

  .time-card .tc-time {
    font-family: 'DM Mono', monospace;
    font-size: 26px;
    font-weight: 700;
    color: #2563eb;
    flex-shrink: 0;
    min-width: 64px;
    text-align: right;
  }

  .time-card .tc-body .tc-task {
    font-size: 14px;
    font-weight: 600;
    color: #f0f6fc;
    margin-bottom: 2px;
  }

  .time-card .tc-body .tc-detail {
    font-size: 12px;
    color: #6b7280;
    line-height: 1.4;
  }

  /* Prompt card — single prompt template */
  .prompt-card {
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 12px;
    overflow: hidden;
    margin: 14px 0;
  }

  .prompt-card .pc-header {
    background: #161b22;
    padding: 10px 18px;
    display: flex;
    align-items: center;
    gap: 10px;
    border-bottom: 1px solid #30363d;
  }

  .prompt-card .pc-num {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    color: #4b5563;
    min-width: 28px;
  }

  .prompt-card .pc-title {
    font-size: 14px;
    font-weight: 600;
    color: #f0f6fc;
    flex: 1;
  }

  .prompt-card .pc-save {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    background: #1e3a5f;
    color: #60a5fa;
    padding: 2px 10px;
    border-radius: 999px;
  }

  .prompt-card .pc-body {
    padding: 14px 18px;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    line-height: 1.8;
    color: #d1d5db;
  }

  .prompt-card .pc-body .ph-role   { color: #f9a8d4; font-weight: 600; }
  .prompt-card .pc-body .ph-task   { color: #86efac; font-weight: 600; }
  .prompt-card .pc-body .ph-ctx    { color: #60a5fa; font-weight: 600; }
  .prompt-card .pc-body .ph-fmt    { color: #c4b5fd; font-weight: 600; }
  .prompt-card .pc-body .ph-blank  { color: #4b5563; font-style: italic; }

  .prompt-card .pc-footer {
    background: #0d1117;
    border-top: 1px solid #21262d;
    padding: 8px 18px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #4b5563;
    display: flex;
    gap: 16px;
  }

  .prompt-card .pc-footer .pf-tag {
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }

  /* 5-prompt grid per slide */
  .prompt-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 14px 0;
  }

  .pg-card {
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 10px;
    overflow: hidden;
  }

  .pg-card .pgc-header {
    background: #161b22;
    padding: 8px 14px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid #21262d;
  }

  .pg-card .pgc-num {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    font-weight: 700;
    color: #4b5563;
    min-width: 22px;
  }

  .pg-card .pgc-title {
    font-size: 13px;
    font-weight: 600;
    color: #f0f6fc;
    flex: 1;
  }

  .pg-card .pgc-save {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    background: #14532d;
    color: #86efac;
    padding: 1px 8px;
    border-radius: 999px;
    flex-shrink: 0;
  }

  .pg-card .pgc-body {
    padding: 10px 14px;
    font-size: 12px;
    color: #9ca3af;
    line-height: 1.7;
    font-family: 'DM Sans', sans-serif;
  }

  .pg-card .pgc-body em {
    color: #60a5fa;
    font-style: normal;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
  }

  /* Category label strip */
  .cat-strip {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-bottom: 14px;
  }

  .cat-pill {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 600;
    padding: 4px 12px;
    border-radius: 999px;
  }

  .cat-pill.writing  { background: #1e3a5f; color: #60a5fa; }
  .cat-pill.thinking { background: #2e1065; color: #c4b5fd; }
  .cat-pill.code     { background: #14532d; color: #86efac; }
  .cat-pill.comms    { background: #451a03; color: #fde68a; }
  .cat-pill.ops      { background: #4c0519; color: #f9a8d4; }

  /* Template reference block */
  .template-ref {
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 10px;
    padding: 16px 20px;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    line-height: 2;
    margin: 12px 0;
  }

  .template-ref .tr-label {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #4b5563;
    margin-bottom: 8px;
  }

  .template-ref .tr-num   { color: #4b5563; }
  .template-ref .tr-name  { color: #f0f6fc; font-weight: 600; }
  .template-ref .tr-where { color: #60a5fa; }
  .template-ref .tr-save  { color: #86efac; }

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

# 10 AI Prompts That Save You
## Hours Every Week

&nbsp;

**Most people use AI reactively.** These prompts make it a system.

`writing` · `thinking` · `code` · `comms` · `ops`

---

## Where the Hours Actually Go

These are the tasks professionals repeat every single week. All of them are now 10-minute jobs.

<div class="time-grid">
  <div class="time-card">
    <span class="tc-time">2h</span>
    <div class="tc-body">
      <div class="tc-task">Drafting emails and messages</div>
      <div class="tc-detail">Writing, rewriting, softening, shortening. Every week.</div>
    </div>
  </div>
  <div class="time-card">
    <span class="tc-time">3h</span>
    <div class="tc-body">
      <div class="tc-task">Summarising documents and reports</div>
      <div class="tc-detail">Reading long docs just to extract 5 key points.</div>
    </div>
  </div>
  <div class="time-card">
    <span class="tc-time">1h</span>
    <div class="tc-body">
      <div class="tc-task">Debugging and fixing code</div>
      <div class="tc-detail">Staring at errors, searching Stack Overflow, guessing.</div>
    </div>
  </div>
  <div class="time-card">
    <span class="tc-time">2h</span>
    <div class="tc-body">
      <div class="tc-task">Planning and thinking through problems</div>
      <div class="tc-detail">Structuring ideas, drafting outlines, deciding between options.</div>
    </div>
  </div>
</div>

<div class="highlight">

That's **8 hours** of recurring weekly work — most of which AI can handle in a fraction of the time, if you ask it right.

</div>

---

<!-- _class: step -->

<div class="step-badge">PROMPTS 01–02</div>

## Writing — Draft and Rewrite

<div class="cat-strip">
  <span class="cat-pill writing">✍️ Writing</span>
</div>

<div class="prompt-card">
  <div class="pc-header">
    <span class="pc-num">01</span>
    <span class="pc-title">The First-Draft Engine</span>
    <span class="pc-save">~45 min saved</span>
  </div>
  <div class="pc-body">
    <span class="ph-role">You are a direct, no-fluff writer.</span> <span class="ph-task">Write a [post / email / report] about [topic].</span> <span class="ph-ctx">Audience: [who they are]. Context: [one sentence of background].</span> <span class="ph-fmt">Tone: [direct / conversational / formal]. Length: [word count]. Format: [bullets / paragraphs / numbered steps].</span> <span class="ph-blank">Do not use: filler openers, "excited to share", exclamation marks.</span>
  </div>
  <div class="pc-footer">
    <span class="pf-tag">📌 Works for: LinkedIn posts, Substack drafts, internal reports, announcements</span>
  </div>
</div>

<div class="prompt-card">
  <div class="pc-header">
    <span class="pc-num">02</span>
    <span class="pc-title">The Rewrite Sharpener</span>
    <span class="pc-save">~30 min saved</span>
  </div>
  <div class="pc-body">
    <span class="ph-task">Rewrite this to be more [concise / direct / clear].</span> <span class="ph-ctx">Keep all the facts. Cut anything that doesn't add meaning.</span> <span class="ph-fmt">Target length: [X words or "half the original"]. Do not change the core message.</span> <span class="ph-blank">[Paste your draft here]</span>
  </div>
  <div class="pc-footer">
    <span class="pf-tag">📌 Works for: anything you've already written that needs tightening</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">PROMPTS 03–04</div>

## Thinking — Analyse and Decide

<div class="cat-strip">
  <span class="cat-pill thinking">🧠 Thinking</span>
</div>

<div class="prompt-card">
  <div class="pc-header">
    <span class="pc-num">03</span>
    <span class="pc-title">The Decision Pressure-Test</span>
    <span class="pc-save">~60 min saved</span>
  </div>
  <div class="pc-body">
    <span class="ph-task">I'm deciding between [option A] and [option B].</span> <span class="ph-ctx">Context: [your situation in 2–3 sentences]. My main priority is [speed / cost / quality / risk].</span> <span class="ph-fmt">Think through the pros and cons of each, then give me your recommendation with the single most important reason. Be direct — don't hedge.</span>
  </div>
  <div class="pc-footer">
    <span class="pf-tag">📌 Works for: tool choices, architecture decisions, career calls, project tradeoffs</span>
  </div>
</div>

<div class="prompt-card">
  <div class="pc-header">
    <span class="pc-num">04</span>
    <span class="pc-title">The Steel-Man Challenge</span>
    <span class="pc-save">~45 min saved</span>
  </div>
  <div class="pc-body">
    <span class="ph-task">I'm leaning toward [your position or plan].</span> <span class="ph-ctx">Make the strongest possible case against it — not a weak counter, the best one.</span> <span class="ph-fmt">Then list the 3 conditions under which my position would be wrong. Don't soften this.</span>
  </div>
  <div class="pc-footer">
    <span class="pf-tag">📌 Works for: project proposals, plans, hiring decisions, technical choices</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">PROMPTS 05–06</div>

## Code — Debug and Explain

<div class="cat-strip">
  <span class="cat-pill code">💻 Code</span>
</div>

<div class="prompt-card">
  <div class="pc-header">
    <span class="pc-num">05</span>
    <span class="pc-title">The Debug Report</span>
    <span class="pc-save">~60 min saved</span>
  </div>
  <div class="pc-body">
    <span class="ph-role">Python [version], [key libraries].</span> <span class="ph-ctx">Here is my code and the full error traceback:</span> <span class="ph-blank">[paste code] [paste full traceback]</span><br>
    <span class="ph-task">First explain what caused this in plain English. Then give me the corrected code with a comment on the fixed line only.</span>
  </div>
  <div class="pc-footer">
    <span class="pf-tag">📌 Works for: any error — Python, JavaScript, SQL, bash</span>
  </div>
</div>

<div class="prompt-card">
  <div class="pc-header">
    <span class="pc-num">06</span>
    <span class="pc-title">The Code Explainer</span>
    <span class="pc-save">~30 min saved</span>
  </div>
  <div class="pc-body">
    <span class="ph-task">Explain what this code does</span> <span class="ph-fmt">as if I understand [Python basics / general programming / nothing about code].</span> <span class="ph-ctx">Don't just restate each line — explain the overall logic and intent.</span> <span class="ph-blank">[paste code]</span>
  </div>
  <div class="pc-footer">
    <span class="pf-tag">📌 Works for: inherited code, AI-generated code you want to understand</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">PROMPTS 07–08</div>

## Communications — Emails and Feedback

<div class="cat-strip">
  <span class="cat-pill comms">📧 Comms</span>
</div>

<div class="prompt-card">
  <div class="pc-header">
    <span class="pc-num">07</span>
    <span class="pc-title">The Difficult Message Drafter</span>
    <span class="pc-save">~40 min saved</span>
  </div>
  <div class="pc-body">
    <span class="ph-role">You are a clear, direct communicator.</span> <span class="ph-task">Help me write a [message / email] that [declines / pushes back on / requests / sets a boundary around] [situation].</span> <span class="ph-ctx">My relationship with this person: [colleague / client / manager]. I want to maintain the relationship but be clear.</span> <span class="ph-fmt">Tone: professional but direct. Length: short — 4 sentences max.</span>
  </div>
  <div class="pc-footer">
    <span class="pf-tag">📌 Works for: declining requests, pushing back on scope, setting deadlines, saying no</span>
  </div>
</div>

<div class="prompt-card">
  <div class="pc-header">
    <span class="pc-num">08</span>
    <span class="pc-title">The Feedback Framer</span>
    <span class="pc-save">~30 min saved</span>
  </div>
  <div class="pc-body">
    <span class="ph-task">Help me give constructive feedback on this [work / document / idea].</span> <span class="ph-ctx">What I actually think: [your honest reaction in plain terms].</span> <span class="ph-fmt">Reframe this as specific, actionable feedback. Keep it direct but not harsh. No filler praise before the critique.</span>
  </div>
  <div class="pc-footer">
    <span class="pf-tag">📌 Works for: code reviews, document reviews, peer feedback, client work</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">PROMPTS 09–10</div>

## Operations — Summarise and Plan

<div class="cat-strip">
  <span class="cat-pill ops">⚙️ Ops</span>
</div>

<div class="prompt-card">
  <div class="pc-header">
    <span class="pc-num">09</span>
    <span class="pc-title">The Document Distiller</span>
    <span class="pc-save">~90 min saved</span>
  </div>
  <div class="pc-body">
    <span class="ph-task">Read this document and give me:</span><br>
    <span class="ph-fmt">1. The single most important thing to know (1 sentence)<br>2. The 3 key decisions or action items<br>3. Anything I need to respond to or act on, with a suggested deadline</span><br>
    <span class="ph-ctx">Skip background information I don't need. Be specific.</span> <span class="ph-blank">[paste document]</span>
  </div>
  <div class="pc-footer">
    <span class="pf-tag">📌 Works for: reports, meeting notes, research papers, long emails, specs</span>
  </div>
</div>

<div class="prompt-card">
  <div class="pc-header">
    <span class="pc-num">10</span>
    <span class="pc-title">The Weekly Planner</span>
    <span class="pc-save">~30 min saved</span>
  </div>
  <div class="pc-body">
    <span class="ph-task">Here are my tasks for this week:</span> <span class="ph-blank">[paste list]</span><br>
    <span class="ph-fmt">Group them into: Deep Work / Admin / Comms. Then order each group by energy — cognitively demanding tasks first.</span> <span class="ph-ctx">Flag anything that should be delegated, automated, or dropped. Keep the output short — one clean list.</span>
  </div>
  <div class="pc-footer">
    <span class="pf-tag">📌 Works for: Monday planning, sprint grooming, daily prioritisation</span>
  </div>
</div>

---

## All 10 at a Glance

<div class="template-ref">
  <div class="tr-label">📋 Quick reference — copy the prompt name to find it above</div>
  <span class="tr-num">01</span> &nbsp;<span class="tr-name">First-Draft Engine</span> &nbsp;&nbsp;<span class="tr-where">writing</span> &nbsp;&nbsp;<span class="tr-save">~45 min</span><br>
  <span class="tr-num">02</span> &nbsp;<span class="tr-name">Rewrite Sharpener</span> &nbsp;&nbsp;<span class="tr-where">writing</span> &nbsp;&nbsp;<span class="tr-save">~30 min</span><br>
  <span class="tr-num">03</span> &nbsp;<span class="tr-name">Decision Pressure-Test</span> &nbsp;&nbsp;<span class="tr-where">thinking</span> &nbsp;&nbsp;<span class="tr-save">~60 min</span><br>
  <span class="tr-num">04</span> &nbsp;<span class="tr-name">Steel-Man Challenge</span> &nbsp;&nbsp;<span class="tr-where">thinking</span> &nbsp;&nbsp;<span class="tr-save">~45 min</span><br>
  <span class="tr-num">05</span> &nbsp;<span class="tr-name">Debug Report</span> &nbsp;&nbsp;<span class="tr-where">code</span> &nbsp;&nbsp;<span class="tr-save">~60 min</span><br>
  <span class="tr-num">06</span> &nbsp;<span class="tr-name">Code Explainer</span> &nbsp;&nbsp;<span class="tr-where">code</span> &nbsp;&nbsp;<span class="tr-save">~30 min</span><br>
  <span class="tr-num">07</span> &nbsp;<span class="tr-name">Difficult Message Drafter</span> &nbsp;&nbsp;<span class="tr-where">comms</span> &nbsp;&nbsp;<span class="tr-save">~40 min</span><br>
  <span class="tr-num">08</span> &nbsp;<span class="tr-name">Feedback Framer</span> &nbsp;&nbsp;<span class="tr-where">comms</span> &nbsp;&nbsp;<span class="tr-save">~30 min</span><br>
  <span class="tr-num">09</span> &nbsp;<span class="tr-name">Document Distiller</span> &nbsp;&nbsp;<span class="tr-where">ops</span> &nbsp;&nbsp;<span class="tr-save">~90 min</span><br>
  <span class="tr-num">10</span> &nbsp;<span class="tr-name">Weekly Planner</span> &nbsp;&nbsp;<span class="tr-where">ops</span> &nbsp;&nbsp;<span class="tr-save">~30 min</span>
</div>

<div class="highlight good">

Total potential time saved per week: **~7 hours.** That's one full working day — every week — doing work you currently do manually.

</div>

---

<!-- _class: final -->

# 10 prompts.
# One saved day per week.
# Every week.

&nbsp;

These aren't tricks. They're systems. Use them consistently and they compound.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*