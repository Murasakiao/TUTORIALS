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

  /* ── Task audit grid ── */
  .audit-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .audit-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 13px 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }

  .audit-card .ac-icon { font-size: 22px; flex-shrink: 0; margin-top: 1px; }

  .audit-card .ac-task {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
    margin-bottom: 3px;
  }

  .audit-card .ac-signal {
    font-size: 12px;
    color: var(--muted);
    line-height: 1.5;
  }

  .audit-card .ac-tag {
    display: inline-block;
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--blue);
    background: var(--blue-light);
    border: 1px solid var(--blue-mid);
    padding: 2px 7px;
    border-radius: 4px;
    margin-top: 5px;
  }

  /* ── Tool comparison cards ── */
  .platform-compare {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .pc-card {
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
  }

  .pc-card .pcc-header {
    padding: 12px 14px;
    font-weight: 700;
    font-size: 15px;
    color: var(--text);
    border-bottom: 1px solid var(--border);
    background: var(--off-white);
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .pc-card .pcc-body {
    padding: 12px 14px;
    background: var(--white);
  }

  .pc-card .pcc-row {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    padding: 4px 0;
    border-bottom: 1px solid var(--border);
    font-size: 12.5px;
  }

  .pc-card .pcc-row:last-child { border-bottom: none; }

  .pc-card .pcc-row .pcc-label { color: var(--muted); }
  .pc-card .pcc-row .pcc-val   { 
    font-family: 'DM Mono', monospace;
    font-size: 11.5px;
    color: var(--blue);
    font-weight: 500;
  }

  .pc-card .pcc-verdict {
    padding: 8px 14px;
    font-size: 12px;
    font-weight: 600;
    border-top: 1px solid var(--border);
  }

  .pc-card.zapier   .pcc-verdict { background: #fff7ed; color: #9a3412; }
  .pc-card.make     .pcc-verdict { background: #f0fdf4; color: #166534; }
  .pc-card.n8n      .pcc-verdict { background: #f5f3ff; color: #5b21b6; }

  /* ── Zap / scenario builder ── */
  .zap-builder {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
    margin: 14px 0;
  }

  .zap-builder .zb-bar {
    background: var(--text);
    padding: 9px 16px;
    font-family: 'DM Mono', monospace;
    font-size: 11.5px;
    color: #9ca3af;
    letter-spacing: 0.04em;
  }

  .zap-builder .zb-body {
    padding: 14px 18px;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .zap-step {
    display: flex;
    align-items: center;
    gap: 12px;
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 11px 14px;
  }

  .zap-step .zs-num {
    background: var(--blue);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 600;
    min-width: 24px;
    height: 24px;
    border-radius: 999px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }

  .zap-step .zs-icon { font-size: 20px; flex-shrink: 0; }

  .zap-step .zs-app {
    font-weight: 600;
    font-size: 13px;
    color: var(--text);
    min-width: 100px;
  }

  .zap-step .zs-action {
    font-size: 12.5px;
    color: var(--muted);
    flex: 1;
  }

  .zap-step .zs-type {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    padding: 2px 8px;
    border-radius: 4px;
    flex-shrink: 0;
  }

  .zs-type.trigger  { background: #f0fdf4; color: #166534; border: 1px solid #bbf7d0; }
  .zs-type.ai       { background: #f5f3ff; color: #5b21b6; border: 1px solid #ddd6fe; }
  .zs-type.action   { background: var(--blue-light); color: #1e40af; border: 1px solid var(--blue-mid); }
  .zs-type.filter   { background: #fef3c7; color: #92400e; border: 1px solid #fde68a; }

  .zap-connector {
    padding: 2px 0 2px 30px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--border);
  }

  /* ── Real-life examples ── */
  .example-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .example-card {
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
  }

  .example-card .ec-header {
    background: var(--off-white);
    padding: 9px 14px;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .example-card .ec-icon { font-size: 18px; }

  .example-card .ec-title {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
  }

  .example-card .ec-body {
    background: var(--white);
    padding: 10px 14px;
  }

  .example-card .ec-flow {
    display: flex;
    align-items: center;
    gap: 6px;
    flex-wrap: wrap;
    margin-bottom: 6px;
  }

  .example-card .ec-node {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    padding: 3px 8px;
    border-radius: 4px;
    white-space: nowrap;
  }

  .ec-node.trigger { background: #f0fdf4; color: #166534; border: 1px solid #bbf7d0; }
  .ec-node.ai      { background: #f5f3ff; color: #5b21b6; border: 1px solid #ddd6fe; }
  .ec-node.action  { background: var(--blue-light); color: #1e40af; border: 1px solid var(--blue-mid); }

  .ec-arrow { font-size: 12px; color: var(--muted); }

  .example-card .ec-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.5;
    margin-top: 4px;
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

# Automate Your Daily Tasks
## with AI

&nbsp;

**Your time is finite. Your workflows don't have to be.** No code required.

`trigger` · `AI step` · `action` · `Zapier` · `Make` · `n8n`

---

## What's Worth Automating?

Not everything. The best candidates share four signals.

<div class="tools">
  <div class="tool-card">
    <div class="icon">🔁</div>
    <div class="name">Repetitive</div>
    <div class="desc">You do the same steps every time — same apps, same sequence, same output format. If it feels like copy-paste, it's automatable.</div>
  </div>
  <div class="tool-card">
    <div class="icon">⏰</div>
    <div class="name">Time-consuming</div>
    <div class="desc">Tasks that take 10+ minutes each time they happen, or interrupt your focus. Even 15 minutes per day is 60+ hours per year.</div>
  </div>
  <div class="tool-card">
    <div class="icon">📋</div>
    <div class="name">Rule-based</div>
    <div class="desc">The decision logic is consistent. If this, then that. Not requiring human judgment every time — or where AI can substitute that judgment.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔗</div>
    <div class="name">Multi-app</div>
    <div class="desc">Moving data between tools — email to spreadsheet, form to CRM, Slack message to task — is the most common automation target.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Identify Your Repetitive Tasks

Audit your last five working days. Any task you did more than twice is a candidate.

<div class="audit-grid">
  <div class="audit-card">
    <div class="ac-icon">📧</div>
    <div>
      <div class="ac-task">Sorting and replying to emails</div>
      <div class="ac-signal">Same question asked repeatedly, templated replies, forwarding to the right person</div>
      <div class="ac-tag">high-value target</div>
    </div>
  </div>
  <div class="audit-card">
    <div class="ac-icon">📝</div>
    <div>
      <div class="ac-task">Writing summaries or reports</div>
      <div class="ac-signal">Weekly status updates, meeting notes, content summaries — same structure every time</div>
      <div class="ac-tag">high-value target</div>
    </div>
  </div>
  <div class="audit-card">
    <div class="ac-icon">📊</div>
    <div>
      <div class="ac-task">Copying data between apps</div>
      <div class="ac-signal">Form responses to spreadsheet, invoice to accounting system, lead to CRM</div>
      <div class="ac-tag">easy win</div>
    </div>
  </div>
  <div class="audit-card">
    <div class="ac-icon">🔔</div>
    <div>
      <div class="ac-task">Monitoring and alerting</div>
      <div class="ac-signal">Checking dashboards, watching for specific emails, tracking mentions or deadlines</div>
      <div class="ac-tag">easy win</div>
    </div>
  </div>
  <div class="audit-card">
    <div class="ac-icon">📅</div>
    <div>
      <div class="ac-task">Scheduling and follow-ups</div>
      <div class="ac-signal">Sending reminders, booking confirmations, follow-up emails after meetings</div>
      <div class="ac-tag">medium effort</div>
    </div>
  </div>
  <div class="audit-card">
    <div class="ac-icon">🗂️</div>
    <div>
      <div class="ac-task">Content publishing</div>
      <div class="ac-signal">Formatting a post for multiple platforms, resizing images, adding tags, scheduling</div>
      <div class="ac-tag">medium effort</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Choose Your Tool

Three no-code platforms dominate AI automation. Pick the one that fits your comfort level.

<div class="platform-compare">
  <div class="pc-card zapier">
    <div class="pcc-header">⚡ &nbsp;Zapier</div>
    <div class="pcc-body">
      <div class="pcc-row"><span class="pcc-label">Skill level</span><span class="pcc-val">beginner</span></div>
      <div class="pcc-row"><span class="pcc-label">Free tier</span><span class="pcc-val">100 tasks/mo</span></div>
      <div class="pcc-row"><span class="pcc-label">AI step</span><span class="pcc-val">ChatGPT built-in</span></div>
      <div class="pcc-row"><span class="pcc-label">App library</span><span class="pcc-val">6,000+</span></div>
      <div class="pcc-row"><span class="pcc-label">Pricing</span><span class="pcc-val">from $20/mo</span></div>
    </div>
    <div class="pcc-verdict">Best for: first automation ever</div>
  </div>
  <div class="pc-card make">
    <div class="pcc-header">🔧 &nbsp;Make</div>
    <div class="pcc-body">
      <div class="pcc-row"><span class="pcc-label">Skill level</span><span class="pcc-val">intermediate</span></div>
      <div class="pcc-row"><span class="pcc-label">Free tier</span><span class="pcc-val">1,000 ops/mo</span></div>
      <div class="pcc-row"><span class="pcc-label">AI step</span><span class="pcc-val">OpenAI module</span></div>
      <div class="pcc-row"><span class="pcc-label">App library</span><span class="pcc-val">1,500+</span></div>
      <div class="pcc-row"><span class="pcc-label">Pricing</span><span class="pcc-val">from $9/mo</span></div>
    </div>
    <div class="pcc-verdict">Best for: visual flows, better value</div>
  </div>
  <div class="pc-card n8n">
    <div class="pcc-header">🛠️ &nbsp;n8n</div>
    <div class="pcc-body">
      <div class="pcc-row"><span class="pcc-label">Skill level</span><span class="pcc-val">technical</span></div>
      <div class="pcc-row"><span class="pcc-label">Free tier</span><span class="pcc-val">self-host free</span></div>
      <div class="pcc-row"><span class="pcc-label">AI step</span><span class="pcc-val">any model/API</span></div>
      <div class="pcc-row"><span class="pcc-label">App library</span><span class="pcc-val">400+ nodes</span></div>
      <div class="pcc-row"><span class="pcc-label">Pricing</span><span class="pcc-val">free self-hosted</span></div>
    </div>
    <div class="pcc-verdict">Best for: full control + privacy</div>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**Start with Zapier.** Its free tier handles most beginner automations. Once you hit its limits or need more complex logic, move to Make. Use n8n when you need data to stay on your own server.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Add a Trigger

A trigger is the event that starts your automation. Nothing runs until the trigger fires.

<div class="two-col">
  <div class="col-card">
    <div class="label">Time-based triggers</div>
    <ul style="margin-top:8px; padding-left:1.2em;">
      <li style="font-size:13.5px;">Every day at 9 AM</li>
      <li style="font-size:13.5px;">Every Monday morning</li>
      <li style="font-size:13.5px;">First of every month</li>
      <li style="font-size:13.5px;">Every 15 minutes</li>
    </ul>
  </div>
  <div class="col-card">
    <div class="label">Event-based triggers</div>
    <ul style="margin-top:8px; padding-left:1.2em;">
      <li style="font-size:13.5px;">New email received in Gmail</li>
      <li style="font-size:13.5px;">Form submitted in Typeform</li>
      <li style="font-size:13.5px;">New row added to Google Sheets</li>
      <li style="font-size:13.5px;">Slack message in a channel</li>
    </ul>
  </div>
</div>

<div class="zap-builder" style="margin-top:14px;">
  <div class="zb-bar">Zapier — step 1: set up trigger</div>
  <div class="zb-body">
    <div class="zap-step">
      <div class="zs-num">1</div>
      <div class="zs-icon">📧</div>
      <div class="zs-app">Gmail</div>
      <div class="zs-action">New email matching filter: label:inbox subject:"customer review"</div>
      <span class="zs-type trigger">TRIGGER</span>
    </div>
  </div>
</div>

<div class="highlight">

**Rule:** Only one trigger per automation. If you need multiple triggers, build multiple automations that share the same downstream steps. Keep each flow focused on one entry point.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 04</div>

## Add an AI Step

The AI step is where the magic happens — it reads the trigger data and does something intelligent with it.

<div class="zap-builder">
  <div class="zb-bar">Zapier — add AI step after the trigger</div>
  <div class="zb-body">
    <div class="zap-step">
      <div class="zs-num">1</div>
      <div class="zs-icon">📧</div>
      <div class="zs-app">Gmail</div>
      <div class="zs-action">New email matching filter: label:inbox subject:"customer review"</div>
      <span class="zs-type trigger">TRIGGER</span>
    </div>
    <div class="zap-connector">│</div>
    <div class="zap-step">
      <div class="zs-num">2</div>
      <div class="zs-icon">🤖</div>
      <div class="zs-app">ChatGPT</div>
      <div class="zs-action">Prompt: "Classify this review as positive/negative/mixed. Extract: sentiment, score 1–5, main complaint. Return JSON." Input: {{Gmail Body}}</div>
      <span class="zs-type ai">AI STEP</span>
    </div>
    <div class="zap-connector">│</div>
    <div class="zap-step">
      <div class="zs-num">3</div>
      <div class="zs-icon">⚖️</div>
      <div class="zs-app">Filter</div>
      <div class="zs-action">Only continue if: score &lt; 3 (negative reviews only)</div>
      <span class="zs-type filter">CONDITION</span>
    </div>
  </div>
</div>

<div class="highlight" style="margin-top:12px;">

**Prompt tip for automation:** Always end AI prompts with "Return only JSON. No explanation." In a workflow the output goes directly into the next step — prose breaks everything downstream.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 05</div>

## Add the Output

The output step takes what the AI produced and does something with it — saves it, sends it, or creates something.

<div class="zap-builder">
  <div class="zb-bar">Zapier — complete automation with output steps</div>
  <div class="zb-body">
    <div class="zap-step">
      <div class="zs-num">1</div>
      <div class="zs-icon">📧</div>
      <div class="zs-app">Gmail</div>
      <div class="zs-action">New email matching filter</div>
      <span class="zs-type trigger">TRIGGER</span>
    </div>
    <div class="zap-connector">│</div>
    <div class="zap-step">
      <div class="zs-num">2</div>
      <div class="zs-icon">🤖</div>
      <div class="zs-app">ChatGPT</div>
      <div class="zs-action">Classify review — return JSON with sentiment + score</div>
      <span class="zs-type ai">AI STEP</span>
    </div>
    <div class="zap-connector">│</div>
    <div class="zap-step">
      <div class="zs-num">3</div>
      <div class="zs-icon">⚖️</div>
      <div class="zs-app">Filter</div>
      <div class="zs-action">Only continue if score &lt; 3</div>
      <span class="zs-type filter">CONDITION</span>
    </div>
    <div class="zap-connector">│</div>
    <div class="zap-step">
      <div class="zs-num">4</div>
      <div class="zs-icon">💬</div>
      <div class="zs-app">Slack</div>
      <div class="zs-action">Post to #support-urgent: "⚠️ Negative review ({{score}}/5): {{sentiment}} — {{Gmail Subject}}"</div>
      <span class="zs-type action">ACTION</span>
    </div>
    <div class="zap-connector">│</div>
    <div class="zap-step">
      <div class="zs-num">5</div>
      <div class="zs-icon">📊</div>
      <div class="zs-app">Google Sheets</div>
      <div class="zs-action">Add row: date, email subject, sentiment, score, main_complaint</div>
      <span class="zs-type action">ACTION</span>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Real-Life Examples to Steal

<div class="example-grid">
  <div class="example-card">
    <div class="ec-header">
      <div class="ec-icon">📨</div>
      <div class="ec-title">Auto-draft email replies</div>
    </div>
    <div class="ec-body">
      <div class="ec-flow">
        <span class="ec-node trigger">Gmail: new email</span>
        <span class="ec-arrow">→</span>
        <span class="ec-node ai">AI: draft reply</span>
        <span class="ec-arrow">→</span>
        <span class="ec-node action">Gmail: save draft</span>
      </div>
      <div class="ec-desc">AI drafts a reply in your tone. Lands in Drafts for your approval — you review and send in seconds instead of minutes.</div>
    </div>
  </div>
  <div class="example-card">
    <div class="ec-header">
      <div class="ec-icon">📰</div>
      <div class="ec-title">Daily news digest</div>
    </div>
    <div class="ec-body">
      <div class="ec-flow">
        <span class="ec-node trigger">Schedule: 7 AM</span>
        <span class="ec-arrow">→</span>
        <span class="ec-node ai">AI: summarise RSS</span>
        <span class="ec-arrow">→</span>
        <span class="ec-node action">Email: send digest</span>
      </div>
      <div class="ec-desc">Pulls headlines from your chosen RSS feeds. AI summarises the top 5 stories in 3 sentences each. Delivered before your first coffee.</div>
    </div>
  </div>
  <div class="example-card">
    <div class="ec-header">
      <div class="ec-icon">🧾</div>
      <div class="ec-title">Invoice data extraction</div>
    </div>
    <div class="ec-body">
      <div class="ec-flow">
        <span class="ec-node trigger">Gmail: PDF attachment</span>
        <span class="ec-arrow">→</span>
        <span class="ec-node ai">AI: extract fields</span>
        <span class="ec-arrow">→</span>
        <span class="ec-node action">Sheets: add row</span>
      </div>
      <div class="ec-desc">AI reads invoice PDFs and extracts vendor, amount, date, and line items into a spreadsheet. Replaces manual data entry completely.</div>
    </div>
  </div>
  <div class="example-card">
    <div class="ec-header">
      <div class="ec-icon">🐦</div>
      <div class="ec-title">Social content repurposing</div>
    </div>
    <div class="ec-body">
      <div class="ec-flow">
        <span class="ec-node trigger">Notion: blog published</span>
        <span class="ec-arrow">→</span>
        <span class="ec-node ai">AI: rewrite for X/LinkedIn</span>
        <span class="ec-arrow">→</span>
        <span class="ec-node action">Buffer: schedule posts</span>
      </div>
      <div class="ec-desc">Every time you publish a blog post, AI rewrites it as a tweet thread and LinkedIn post. Both scheduled automatically — zero extra effort.</div>
    </div>
  </div>
  <div class="example-card">
    <div class="ec-header">
      <div class="ec-icon">📝</div>
      <div class="ec-title">Meeting notes to tasks</div>
    </div>
    <div class="ec-body">
      <div class="ec-flow">
        <span class="ec-node trigger">Calendar: meeting ends</span>
        <span class="ec-arrow">→</span>
        <span class="ec-node ai">AI: extract action items</span>
        <span class="ec-arrow">→</span>
        <span class="ec-node action">Notion / Jira: create tasks</span>
      </div>
      <div class="ec-desc">Connects to your meeting transcript (Otter, Fireflies). AI extracts every action item with owner and deadline. Tasks created automatically.</div>
    </div>
  </div>
  <div class="example-card">
    <div class="ec-header">
      <div class="ec-icon">🛒</div>
      <div class="ec-title">Lead qualification</div>
    </div>
    <div class="ec-body">
      <div class="ec-flow">
        <span class="ec-node trigger">Typeform: form submit</span>
        <span class="ec-arrow">→</span>
        <span class="ec-node ai">AI: score and classify</span>
        <span class="ec-arrow">→</span>
        <span class="ec-node action">HubSpot: create contact</span>
      </div>
      <div class="ec-desc">AI reads the form responses and scores the lead 1–10. Hot leads go to sales immediately via Slack. Cold leads enter a nurture sequence.</div>
    </div>
  </div>
</div>

---

## Automation Quick Reference

<table class="cheat-table">
  <tr>
    <th>Task</th>
    <th>What to do</th>
  </tr>
  <tr>
    <td>Find automation candidates</td>
    <td>Look for tasks you did 2+ times this week. If it felt like copy-paste, automate it.</td>
  </tr>
  <tr>
    <td>Pick a platform</td>
    <td>Zapier for beginners. Make for more control. n8n if you want self-hosted and free.</td>
  </tr>
  <tr>
    <td>Set the trigger</td>
    <td>One trigger per automation. Time-based (schedule) or event-based (new email, form submit).</td>
  </tr>
  <tr>
    <td>Write the AI prompt</td>
    <td>Be specific. Include input variable with <code>{{placeholder}}</code>. End with "Return only JSON."</td>
  </tr>
  <tr>
    <td>Parse AI output</td>
    <td>Use the platform's JSON parser step to extract specific fields before passing to output actions.</td>
  </tr>
  <tr>
    <td>Add a condition</td>
    <td>Use a Filter step to only continue if the AI output meets a criteria — score, keyword, category.</td>
  </tr>
  <tr>
    <td>Test before enabling</td>
    <td>Run the automation manually on real data first. Check every step's output before going live.</td>
  </tr>
  <tr>
    <td>Handle errors</td>
    <td>Add an error path — most platforms allow a fallback action if any step fails.</td>
  </tr>
  <tr>
    <td>Monitor it</td>
    <td>Check the automation history weekly. Look for failed runs and adjust prompts if AI output drifts.</td>
  </tr>
</table>

---

<!-- _class: final -->

# You set it up once.
# It runs forever.

&nbsp;

Trigger. AI step. Output. That's the whole formula.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*