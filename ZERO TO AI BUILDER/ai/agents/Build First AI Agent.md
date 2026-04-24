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

  /* Platform comparison cards */
  .platform-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin: 16px 0;
  }

  .platform-card {
    border-radius: 12px;
    padding: 20px 22px;
  }

  .platform-card.zapier { background: #111827; border: 2px solid #e85d04; }
  .platform-card.make   { background: #111827; border: 2px solid #7c3aed; }

  .platform-card .pc-icon  { font-size: 28px; margin-bottom: 8px; }

  .platform-card .pc-name {
    font-family: 'DM Mono', monospace;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 6px;
  }

  .platform-card.zapier .pc-name { color: #fb923c; }
  .platform-card.make   .pc-name { color: #c4b5fd; }

  .platform-card .pc-sub {
    font-size: 12px;
    font-family: 'DM Mono', monospace;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 8px;
  }

  .platform-card.zapier .pc-sub { color: #9a3412; }
  .platform-card.make   .pc-sub { color: #7c3aed; }

  .platform-card .pc-desc { font-size: 13px; color: #9ca3af; line-height: 1.7; }

  .platform-card .pc-fact {
    margin-top: 10px;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    line-height: 2;
  }

  .platform-card.zapier .pc-fact span { color: #fb923c; }
  .platform-card.make   .pc-fact span { color: #c4b5fd; }

  /* Zap/Scenario builder mock */
  .builder-mock {
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
  }

  .builder-bar {
    background: #161b22;
    padding: 8px 16px;
    border-bottom: 1px solid #30363d;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .builder-bar .bb-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: 0.07em;
  }

  .builder-bar .bb-name {
    font-size: 13px;
    color: #f0f6fc;
    font-weight: 600;
    margin-left: 4px;
  }

  .builder-body {
    padding: 16px 20px;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .zap-step {
    display: flex;
    align-items: center;
    gap: 14px;
  }

  .zap-step .zs-num {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 700;
    flex-shrink: 0;
    color: white;
  }

  .zs-num.trigger { background: #1d4ed8; }
  .zs-num.ai      { background: #7c3aed; }
  .zs-num.action  { background: #166534; }

  .zap-step .zs-app {
    background: #1f2937;
    border: 1px solid #374151;
    border-radius: 8px;
    padding: 8px 14px;
    flex: 1;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .zs-app .za-icon  { font-size: 16px; }
  .zs-app .za-app   { font-size: 13px; font-weight: 600; color: #f0f6fc; }
  .zs-app .za-event { font-size: 12px; color: #6b7280; margin-left: auto; font-family: 'DM Mono', monospace; }

  .zap-connector {
    display: flex;
    align-items: center;
    padding-left: 14px;
  }

  .zap-connector .zc-line {
    width: 2px;
    height: 16px;
    background: #374151;
    margin-left: 13px;
  }

  /* Workflow pipeline strip */
  .workflow-strip {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 0;
    align-items: center;
    margin: 16px 0;
  }

  .wf-node {
    background: #111827;
    border-radius: 8px;
    padding: 13px 10px;
    text-align: center;
  }

  .wf-node .wn-icon  { font-size: 18px; margin-bottom: 4px; }
  .wf-node .wn-label { font-family: 'DM Mono', monospace; font-size: 11px; font-weight: 600; margin-bottom: 3px; }
  .wf-node .wn-desc  { font-size: 10px; color: #6b7280; line-height: 1.4; }

  .wf-node.w1 .wn-label { color: #60a5fa; }
  .wf-node.w2 .wn-label { color: #c4b5fd; }
  .wf-node.w3 .wn-label { color: #fde68a; }
  .wf-node.w4 .wn-label { color: #f9a8d4; }
  .wf-node.w5 .wn-label { color: #86efac; }

  .wf-arrow { text-align: center; color: #374151; font-size: 16px; padding: 0 3px; }

  /* What you'll build card */
  .build-card {
    background: #111827;
    border-radius: 12px;
    padding: 22px 24px;
    margin: 16px 0;
    border-left: 4px solid #2563eb;
  }

  .build-card .bc-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #4b5563;
    margin-bottom: 10px;
  }

  .build-card .bc-title {
    font-size: 16px;
    font-weight: 600;
    color: #f0f6fc;
    margin-bottom: 8px;
  }

  .build-card .bc-flow {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
    margin-top: 10px;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .bc-pill {
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 600;
  }

  .bc-pill.trigger { background: #1e3a5f; color: #60a5fa; }
  .bc-pill.ai      { background: #2e1065; color: #c4b5fd; }
  .bc-pill.action  { background: #14532d; color: #86efac; }
  .bc-arrow        { color: #374151; font-size: 14px; }

  /* Step list */
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
    margin-bottom: 13px;
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

  /* Two-col */
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

  /* Ideas grid */
  .ideas-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin: 14px 0;
  }

  .idea-card {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 14px 16px;
  }

  .idea-card .ia-icon  { font-size: 20px; margin-bottom: 6px; }
  .idea-card .ia-title { font-size: 13px; font-weight: 600; color: var(--text); margin-bottom: 4px; }
  .idea-card .ia-flow  { font-size: 11px; color: var(--muted); font-family: 'DM Mono', monospace; line-height: 1.6; }
---

<!-- _class: cover -->

# Build Your First AI Agent
## No Code Required

&nbsp;

**You don't need Python.** You need a trigger, an AI step, and an action.

`Zapier` · `Make` · `trigger` · `AI step` · `action`

---

## What You'll Build

A working automation that receives an input, processes it with AI, and takes a real-world action — without writing a single line of code.

<div class="build-card">
  <div class="bc-label">📋 The agent you'll have by the end of this tutorial</div>
  <div class="bc-title">Email → AI Summariser → Slack Notification</div>
  <p style="font-size:14px; color:#9ca3af; margin: 8px 0;">When a new email arrives in Gmail tagged "reports", the agent reads it, asks AI to extract the key points in 3 bullet points, and posts the summary to a Slack channel automatically.</p>
  <div class="bc-flow">
    <span class="bc-pill trigger">📧 Gmail trigger</span>
    <span class="bc-arrow">→</span>
    <span class="bc-pill ai">✦ AI: summarise</span>
    <span class="bc-arrow">→</span>
    <span class="bc-pill action">💬 Slack: post</span>
  </div>
</div>

<div class="highlight good">

Zero code. Runs 24/7. Takes about 20 minutes to set up the first time.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Choose Your Platform

Two tools dominate no-code automation. Pick one and stick with it.

<div class="platform-grid">
  <div class="platform-card zapier">
    <div class="pc-icon">⚡</div>
    <div class="pc-name">Zapier</div>
    <div class="pc-sub">Easiest to start</div>
    <div class="pc-desc">Drag-and-drop interface. 6,000+ app integrations. AI steps built in. Free plan covers 100 tasks/month — enough to test everything.</div>
    <div class="pc-fact">
      <span>✦ Best for: beginners, simple 2–3 step flows</span><br>
      <span>✦ Free tier: 100 tasks/month</span><br>
      <span>✦ URL: zapier.com</span>
    </div>
  </div>
  <div class="platform-card make">
    <div class="pc-icon">🔮</div>
    <div class="pc-name">Make</div>
    <div class="pc-sub">More power, more control</div>
    <div class="pc-desc">Visual flow builder. Handles complex logic, loops, and error routing. Steeper learning curve but far more capable for multi-step agents.</div>
    <div class="pc-fact">
      <span>✦ Best for: complex flows, loops, conditionals</span><br>
      <span>✦ Free tier: 1,000 operations/month</span><br>
      <span>✦ URL: make.com</span>
    </div>
  </div>
</div>

<div class="highlight warn">

Start with Zapier. Once your first automation is running, you'll know exactly what Make's extra power would unlock.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Define the Trigger

A trigger is the event that starts your automation. Nothing runs until the trigger fires.

<div class="builder-mock">
  <div class="builder-bar">
    <span class="bb-label">Zapier</span>
    <span class="bb-name">New Zap — Step 1 of 3</span>
  </div>
  <div class="builder-body">
    <div class="zap-step">
      <div class="zs-num trigger">1</div>
      <div class="zs-app">
        <span class="za-icon">📧</span>
        <span class="za-app">Gmail</span>
        <span class="za-event">New email matching search</span>
      </div>
    </div>
  </div>
</div>

<div class="two-col">
  <div class="col-card">
    <div class="label">Common triggers</div>
    <p style="font-size:14px; margin-top:8px; color:#374151; line-height:1.9;">
      ✦ New email in Gmail / Outlook<br>
      ✦ New row in Google Sheets<br>
      ✦ New form submission (Typeform, Tally)<br>
      ✦ New file in Google Drive / Dropbox<br>
      ✦ Scheduled time (daily at 8am)
    </p>
  </div>
  <div class="col-card">
    <div class="label">Setting up Gmail trigger</div>
    <p style="font-size:14px; margin-top:8px; color:#374151; line-height:1.8;">
      Search filter: <code>label:reports</code><br>
      This fires only when Gmail receives an email with the "reports" label applied — not every email.
    </p>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Add the AI Step

This is where the agent thinks. Connect to an AI model and write your instruction.

<div class="builder-mock">
  <div class="builder-bar">
    <span class="bb-label">Zapier</span>
    <span class="bb-name">New Zap — Step 2 of 3</span>
  </div>
  <div class="builder-body">
    <div class="zap-step">
      <div class="zs-num trigger">1</div>
      <div class="zs-app">
        <span class="za-icon">📧</span>
        <span class="za-app">Gmail</span>
        <span class="za-event">New email matching search</span>
      </div>
    </div>
    <div class="zap-connector"><div class="zc-line"></div></div>
    <div class="zap-step">
      <div class="zs-num ai">2</div>
      <div class="zs-app">
        <span class="za-icon">✦</span>
        <span class="za-app">AI by Zapier</span>
        <span class="za-event">Prompt → Text output</span>
      </div>
    </div>
  </div>
</div>

**Your AI prompt in Zapier:**

> Summarise the following email in exactly 3 bullet points. Focus on decisions, action items, and deadlines. Be concise — no more than 15 words per bullet.
> Email body: **[insert Gmail body field here]**

The `[Gmail body]` is a dynamic variable — Zapier replaces it with the actual email content each time it runs.

---

<!-- _class: step -->

<div class="step-badge">STEP 04</div>

## Add the Action

Actions are what the agent does with the AI output. Connect it to wherever the result should land.

<div class="builder-mock">
  <div class="builder-bar">
    <span class="bb-label">Zapier</span>
    <span class="bb-name">New Zap — Step 3 of 3</span>
  </div>
  <div class="builder-body">
    <div class="zap-step">
      <div class="zs-num trigger">1</div>
      <div class="zs-app">
        <span class="za-icon">📧</span>
        <span class="za-app">Gmail</span>
        <span class="za-event">New email matching search</span>
      </div>
    </div>
    <div class="zap-connector"><div class="zc-line"></div></div>
    <div class="zap-step">
      <div class="zs-num ai">2</div>
      <div class="zs-app">
        <span class="za-icon">✦</span>
        <span class="za-app">AI by Zapier</span>
        <span class="za-event">Prompt → Text output</span>
      </div>
    </div>
    <div class="zap-connector"><div class="zc-line"></div></div>
    <div class="zap-step">
      <div class="zs-num action">3</div>
      <div class="zs-app">
        <span class="za-icon">💬</span>
        <span class="za-app">Slack</span>
        <span class="za-event">Send channel message</span>
      </div>
    </div>
  </div>
</div>

Map the AI output to the Slack message field. The `[AI output]` variable carries the 3-bullet summary directly into the message body — no editing required.

---

<!-- _class: step -->

<div class="step-badge">STEP 05</div>

## Test It

Before turning it on, run a test with real data.

<ul class="step-list">
  <li>In Zapier, click <strong>Test trigger</strong> — it pulls your most recent matching Gmail email as sample data</li>
  <li>Click <strong>Test action</strong> on the AI step — verify the summary output looks right in the preview panel</li>
  <li>Click <strong>Test action</strong> on the Slack step — check that a real message appeared in your channel</li>
  <li>If the summary is too long or wrong format, refine your AI prompt and re-test — takes 30 seconds</li>
  <li>When all three steps show green checkmarks → click <strong>Publish Zap</strong></li>
</ul>

<div class="highlight warn">

⚠️ The Slack message from your test is real — it will actually post to your channel. Test in a private or test channel first, not your main #general.

</div>

---

## 6 More Agent Ideas to Build Next

<div class="ideas-grid">
  <div class="idea-card">
    <div class="ia-icon">📝</div>
    <div class="ia-title">Form → Draft reply</div>
    <div class="ia-flow">Typeform submission → AI drafts personalised reply → Gmail draft</div>
  </div>
  <div class="idea-card">
    <div class="ia-icon">📊</div>
    <div class="ia-title">Sheet → Weekly digest</div>
    <div class="ia-flow">New Sheets row → AI summarises week's data → Email digest every Friday</div>
  </div>
  <div class="idea-card">
    <div class="ia-icon">🐦</div>
    <div class="ia-title">RSS → Social post</div>
    <div class="ia-flow">New blog post in RSS → AI rewrites as LinkedIn post → Drafts in Buffer</div>
  </div>
  <div class="idea-card">
    <div class="ia-icon">🗒️</div>
    <div class="ia-title">Meeting notes → Tasks</div>
    <div class="ia-flow">New note in Notion → AI extracts action items → Creates tasks in Todoist</div>
  </div>
  <div class="idea-card">
    <div class="ia-icon">🔔</div>
    <div class="ia-title">Mention → Brief</div>
    <div class="ia-flow">Brand mention alert → AI scores sentiment + extracts key claim → Slack alert</div>
  </div>
  <div class="idea-card">
    <div class="ia-icon">📂</div>
    <div class="ia-title">File → Summary doc</div>
    <div class="ia-flow">New PDF in Drive → AI summarises → Appends summary to a master Notion page</div>
  </div>
</div>

---

<!-- _class: final -->

# Trigger. Think. Act.
# That's an agent.

&nbsp;

You just built one without writing a single line of code.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*