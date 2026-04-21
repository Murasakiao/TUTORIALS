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

  /* ── App connection diagram ── */
  .app-connect {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0;
    margin: 18px 0;
  }

  .app-node {
    border-radius: 14px;
    padding: 16px 18px;
    text-align: center;
    min-width: 110px;
    border: 2px solid var(--border);
    background: var(--white);
  }

  .app-node .an-icon  { font-size: 30px; margin-bottom: 5px; }
  .app-node .an-name  { font-weight: 600; font-size: 14px; color: var(--text); }
  .app-node .an-role  { font-family: 'DM Mono', monospace; font-size: 10.5px; color: var(--muted); margin-top: 3px; }

  .app-node.source  { background: #f0fdf4; border-color: #86efac; }
  .app-node.brain   { background: #f5f3ff; border-color: #c4b5fd; }
  .app-node.dest    { background: var(--blue-light); border-color: var(--blue-mid); }

  .app-node.source .an-role { color: #166534; }
  .app-node.brain  .an-role { color: #5b21b6; }
  .app-node.dest   .an-role { color: #1e40af; }

  .app-arrow {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0 12px;
    gap: 2px;
  }

  .app-arrow .aa-label {
    font-family: 'DM Mono', monospace;
    font-size: 9.5px;
    color: var(--muted);
    white-space: nowrap;
    letter-spacing: 0.04em;
  }

  .app-arrow .aa-line { font-size: 20px; color: var(--blue); }

  /* ── Trigger / action anatomy ── */
  .ta-diagram {
    display: grid;
    grid-template-columns: 1fr 24px 1fr;
    gap: 0;
    align-items: stretch;
    margin: 16px 0;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .ta-side {
    padding: 16px 18px;
  }

  .ta-side.trigger { background: #f0fdf4; }
  .ta-side.action  { background: var(--blue-light); }

  .ta-side .ts-label {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 10px;
  }

  .ta-side.trigger .ts-label { color: #166534; }
  .ta-side.action  .ts-label { color: #1e40af; }

  .ta-side .ts-title {
    font-weight: 600;
    font-size: 15px;
    color: var(--text);
    margin-bottom: 6px;
  }

  .ta-side .ts-examples {
    display: flex;
    flex-direction: column;
    gap: 5px;
    margin-top: 8px;
  }

  .ta-side .ts-ex {
    font-size: 12.5px;
    color: var(--muted);
    display: flex;
    align-items: baseline;
    gap: 6px;
  }

  .ta-side .ts-ex::before {
    content: '→';
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--border);
    flex-shrink: 0;
  }

  .ta-divider {
    background: var(--border);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    color: var(--blue);
  }

  /* ── No-code vs code comparison ── */
  .nc-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 14px;
  }

  .nc-col {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .nc-col .ncc-label {
    padding: 8px 14px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    border-bottom: 1px solid var(--border);
  }

  .nc-col.nocode .ncc-label { background: #f0fdf4; color: #166534; border-color: #bbf7d0; }
  .nc-col.code   .ncc-label { background: #111827; color: #9ca3af; border-color: #1f2937; }

  .nc-col .ncc-body {
    padding: 12px 14px;
    font-size: 13px;
    line-height: 1.7;
  }

  .nc-col.nocode .ncc-body { background: var(--white); color: var(--muted); }
  .nc-col.code   .ncc-body {
    background: #111827;
    color: #9ca3af;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    line-height: 2;
  }

  .nc-col.code .ncc-body .kw { color: #c084fc; }
  .nc-col.code .ncc-body .fn { color: #60a5fa; }
  .nc-col.code .ncc-body .st { color: #fde68a; }
  .nc-col.code .ncc-body .cm { color: #4b5563; font-style: italic; }

  /* ── Zap builder (reused from previous deck) ── */
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

  .zs-type.trigger { background: #f0fdf4; color: #166534; border: 1px solid #bbf7d0; }
  .zs-type.ai      { background: #f5f3ff; color: #5b21b6; border: 1px solid #ddd6fe; }
  .zs-type.action  { background: var(--blue-light); color: #1e40af; border: 1px solid var(--blue-mid); }
  .zs-type.filter  { background: #fef3c7; color: #92400e; border: 1px solid #fde68a; }

  .zap-connector {
    padding: 2px 0 2px 30px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--border);
  }

  /* ── Email → Slack walkthrough ── */
  .walkthrough {
    display: flex;
    gap: 14px;
    margin: 14px 0;
    align-items: flex-start;
  }

  .wt-col {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .wt-label {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.07em;
    margin-bottom: 2px;
  }

  .wt-box {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    flex: 1;
  }

  .wt-box .wb-header {
    padding: 7px 12px;
    font-size: 12px;
    font-weight: 600;
    border-bottom: 1px solid var(--border);
  }

  .wt-box.email   .wb-header { background: #fff7ed; color: #9a3412; }
  .wt-box.ai-box  .wb-header { background: #f5f3ff; color: #5b21b6; }
  .wt-box.slack   .wb-header { background: #f0fdf4; color: #166534; }

  .wt-box .wb-body {
    padding: 10px 12px;
    background: var(--white);
    font-size: 12.5px;
    color: var(--text);
    line-height: 1.6;
  }

  .wt-box.ai-box .wb-body {
    font-family: 'DM Mono', monospace;
    font-size: 11.5px;
    color: var(--blue);
    line-height: 1.8;
  }

  .wt-arrow {
    display: flex;
    align-items: center;
    padding-top: 28px;
    font-size: 20px;
    color: var(--blue);
    flex-shrink: 0;
  }

  /* ── Integration gallery ── */
  .integration-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 14px;
  }

  .int-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px 16px;
  }

  .int-card .ic-title {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .int-card .ic-flow {
    display: flex;
    align-items: center;
    gap: 5px;
    flex-wrap: wrap;
  }

  .int-card .ic-app {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    padding: 2px 8px;
    border-radius: 4px;
    white-space: nowrap;
  }

  .ic-app.src { background: #f0fdf4; color: #166534; border: 1px solid #bbf7d0; }
  .ic-app.ai  { background: #f5f3ff; color: #5b21b6; border: 1px solid #ddd6fe; }
  .ic-app.dst { background: var(--blue-light); color: #1e40af; border: 1px solid var(--blue-mid); }
  .ic-arr     { font-size: 12px; color: var(--muted); }

  .int-card .ic-desc {
    font-size: 12px;
    color: var(--muted);
    margin-top: 6px;
    line-height: 1.5;
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

# Connect Your Apps
## Using AI — No Code

&nbsp;

**Your apps don't talk to each other. AI is the translator.** No code needed.

`trigger` · `integration` · `AI step` · `Zapier` · `Make` · `webhook`

---

## What Integrations Are

An integration is a connection between two apps — when something happens in one, something automatically happens in another.

<div class="app-connect">
  <div class="app-node source">
    <div class="an-icon">📧</div>
    <div class="an-name">Gmail</div>
    <div class="an-role">source app</div>
  </div>
  <div class="app-arrow">
    <div class="aa-label">new email</div>
    <div class="aa-line">→</div>
  </div>
  <div class="app-node brain">
    <div class="an-icon">🤖</div>
    <div class="an-name">AI Model</div>
    <div class="an-role">intelligent step</div>
  </div>
  <div class="app-arrow">
    <div class="aa-label">summary</div>
    <div class="aa-line">→</div>
  </div>
  <div class="app-node dest">
    <div class="an-icon">💬</div>
    <div class="an-name">Slack</div>
    <div class="an-role">destination app</div>
  </div>
</div>

<div class="tools" style="margin-top:4px;">
  <div class="tool-card">
    <div class="icon">🔌</div>
    <div class="name">No code required</div>
    <div class="desc">Platforms like Zapier and Make provide pre-built connectors for 1,000+ apps. You configure, not code.</div>
  </div>
  <div class="tool-card">
    <div class="icon">⚡</div>
    <div class="name">Event-driven</div>
    <div class="desc">Integrations react to events — a new email, a form submission, a new row in a spreadsheet. Nothing runs until the trigger fires.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🤖</div>
    <div class="name">AI makes them smart</div>
    <div class="desc">Without AI, integrations just move data. Add an AI step and the integration can read, interpret, classify, and generate — not just copy.</div>
  </div>
  <div class="tool-card">
    <div class="icon">♾️</div>
    <div class="name">Runs 24 / 7</div>
    <div class="desc">Once built, the integration runs automatically in the background. It doesn't need you present to work — and it never forgets.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## The Trigger + Action Model

Every integration has exactly two required parts — a trigger that starts it and at least one action that follows.

<div class="ta-diagram">
  <div class="ta-side trigger">
    <div class="ts-label">⚡ Trigger</div>
    <div class="ts-title">Something happens in App A</div>
    <p style="font-size:13px; color:var(--muted); margin-top:4px;">The event that starts the chain. Passive — it listens and waits. Nothing runs until this fires.</p>
    <div class="ts-examples">
      <div class="ts-ex">New email arrives in Gmail</div>
      <div class="ts-ex">Form submitted in Typeform</div>
      <div class="ts-ex">Row added to Google Sheets</div>
      <div class="ts-ex">Message posted in Slack</div>
      <div class="ts-ex">Schedule: every day at 9 AM</div>
    </div>
  </div>
  <div class="ta-divider">→</div>
  <div class="ta-side action">
    <div class="ts-label">🎯 Action</div>
    <div class="ts-title">Something happens in App B</div>
    <p style="font-size:13px; color:var(--muted); margin-top:4px;">What the integration does in response. Can be one action or a chain of many. Uses data from the trigger.</p>
    <div class="ts-examples">
      <div class="ts-ex">Send a Slack message</div>
      <div class="ts-ex">Create a Notion page</div>
      <div class="ts-ex">Add a row to Airtable</div>
      <div class="ts-ex">Send an email reply</div>
      <div class="ts-ex">Create a task in Jira</div>
    </div>
  </div>
</div>

<div class="highlight">

**Without AI:** the action just copies the trigger data somewhere else — a form response lands in a spreadsheet. **With AI:** the action does something intelligent with the data before saving or sending it.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Add AI in the Middle

AI lives between trigger and action. It reads the trigger's data, processes it intelligently, and passes a transformed result to the action.

<div class="app-connect" style="margin-bottom:0;">
  <div class="app-node source">
    <div class="an-icon">📥</div>
    <div class="an-name">Trigger</div>
    <div class="an-role">raw data in</div>
  </div>
  <div class="app-arrow">
    <div class="aa-label">raw text</div>
    <div class="aa-line">→</div>
  </div>
  <div class="app-node brain">
    <div class="an-icon">🤖</div>
    <div class="an-name">AI Step</div>
    <div class="an-role">understand + transform</div>
  </div>
  <div class="app-arrow">
    <div class="aa-label">structured result</div>
    <div class="aa-line">→</div>
  </div>
  <div class="app-node dest">
    <div class="an-icon">📤</div>
    <div class="an-name">Action</div>
    <div class="an-role">smart output</div>
  </div>
</div>

<div class="nc-compare" style="margin-top:14px;">
  <div class="nc-col nocode">
    <div class="ncc-label">✅ &nbsp;No-code — Zapier / Make</div>
    <div class="ncc-body">
      Select "ChatGPT" or "OpenAI" as a step. Write your prompt in a text field. Reference trigger data with <code style="font-size:12px;">{{Email Body}}</code>. No setup beyond connecting your OpenAI account.
    </div>
  </div>
  <div class="nc-col code">
    <div class="ncc-label">🔧 &nbsp;Code equivalent (Python)</div>
    <div class="ncc-body">
      <span class="kw">import</span> anthropic<br>
      <span class="cm"># same logic, more control</span><br>
      result = client<span class="fn">.messages.create</span>(<br>
      &nbsp;&nbsp;model=<span class="st">"claude-sonnet-4-6"</span>,<br>
      &nbsp;&nbsp;messages=[{<span class="st">"role"</span>:<span class="st">"user"</span>,<br>
      &nbsp;&nbsp;&nbsp;&nbsp;<span class="st">"content"</span>: prompt}]<br>
      )
    </div>
  </div>
</div>

<div class="highlight" style="margin-top:12px;">

**Use no-code first.** If Zapier or Make can do it, use them — setup takes minutes. Switch to code only when you need custom logic, private data handling, or cost control at scale.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Build It — Email → Summary → Slack

The most useful AI integration for any team. An important email arrives, AI summarises it in 3 bullet points, the summary posts to Slack instantly.

<div class="zap-builder">
  <div class="zb-bar">Zapier — email → AI summary → Slack (full build)</div>
  <div class="zb-body">
    <div class="zap-step">
      <div class="zs-num">1</div>
      <div class="zs-icon">📧</div>
      <div class="zs-app">Gmail</div>
      <div class="zs-action">New email in label: "needs-summary" — fires whenever a starred or labelled email arrives</div>
      <span class="zs-type trigger">TRIGGER</span>
    </div>
    <div class="zap-connector">│</div>
    <div class="zap-step">
      <div class="zs-num">2</div>
      <div class="zs-icon">🤖</div>
      <div class="zs-app">ChatGPT</div>
      <div class="zs-action">Prompt: "Summarise this email in exactly 3 bullet points. Be concise. No preamble. Input: {{Body Plain}}"</div>
      <span class="zs-type ai">AI STEP</span>
    </div>
    <div class="zap-connector">│</div>
    <div class="zap-step">
      <div class="zs-num">3</div>
      <div class="zs-icon">💬</div>
      <div class="zs-app">Slack</div>
      <div class="zs-action">Post to #summaries: "*{{Subject}}* (from {{From Name}})\n{{ChatGPT Response}}"</div>
      <span class="zs-type action">ACTION</span>
    </div>
  </div>
</div>

<div class="highlight" style="margin-top:10px;">

**Setup time: ~10 minutes.** Connect Gmail (step 1), connect OpenAI (step 2 — paste your API key once), connect Slack (step 3 — select workspace + channel). Test it. Enable it. Done.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## What the Output Looks Like

<div class="walkthrough">
  <div class="wt-col">
    <div class="wt-label">📧 &nbsp;Original email</div>
    <div class="wt-box email">
      <div class="wb-header">📧 &nbsp;Gmail — received</div>
      <div class="wb-body">
        <strong>From:</strong> sarah@client.com<br>
        <strong>Subject:</strong> Q3 Budget Revision — Action Required<br><br>
        Hi team, following yesterday's board meeting we need to revise the Q3 marketing budget from $80k to $65k. All planned campaigns over $5k need reapproval. Please submit revised plans by Friday EOD. The new approval form is in the shared drive under Finance › 2026 › Q3.
      </div>
    </div>
  </div>
  <div class="wt-arrow">→</div>
  <div class="wt-col">
    <div class="wt-label">🤖 &nbsp;AI prompt (step 2)</div>
    <div class="wt-box ai-box">
      <div class="wb-header">🤖 &nbsp;ChatGPT — prompt</div>
      <div class="wb-body">Summarise in 3 bullets.<br>Be concise. No preamble.<br><br>Input: {{Body Plain}}</div>
    </div>
  </div>
  <div class="wt-arrow">→</div>
  <div class="wt-col">
    <div class="wt-label">💬 &nbsp;Slack message (step 3)</div>
    <div class="wt-box slack">
      <div class="wb-header">💬 &nbsp;#summaries</div>
      <div class="wb-body">
        <strong>Q3 Budget Revision — Action Required</strong><br>
        <em>from Sarah (client.com)</em><br><br>
        • Q3 marketing budget cut from $80k → $65k<br>
        • Campaigns over $5k need reapproval<br>
        • Revised plans due Friday EOD — form in shared drive
      </div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## More Integrations to Build

<div class="integration-grid">
  <div class="int-card">
    <div class="ic-title">📝 &nbsp;Form → CRM with qualification</div>
    <div class="ic-flow">
      <span class="ic-app src">Typeform</span><span class="ic-arr">→</span>
      <span class="ic-app ai">AI: score lead</span><span class="ic-arr">→</span>
      <span class="ic-app dst">HubSpot contact</span>
    </div>
    <div class="ic-desc">AI reads form answers, scores the lead 1–10, and sets the CRM contact's lifecycle stage automatically.</div>
  </div>
  <div class="int-card">
    <div class="ic-title">🎫 &nbsp;Support ticket routing</div>
    <div class="ic-flow">
      <span class="ic-app src">Intercom</span><span class="ic-arr">→</span>
      <span class="ic-app ai">AI: classify + priority</span><span class="ic-arr">→</span>
      <span class="ic-app dst">Jira issue</span>
    </div>
    <div class="ic-desc">AI reads the ticket, determines category and urgency, assigns to the right team queue, and creates the Jira issue pre-labelled.</div>
  </div>
  <div class="int-card">
    <div class="ic-title">📰 &nbsp;RSS → newsletter draft</div>
    <div class="ic-flow">
      <span class="ic-app src">RSS feed</span><span class="ic-arr">→</span>
      <span class="ic-app ai">AI: curate + write</span><span class="ic-arr">→</span>
      <span class="ic-app dst">Notion / Mailchimp</span>
    </div>
    <div class="ic-desc">AI reads the week's articles, picks the most relevant ones, writes a short summary of each, and drops a draft newsletter into Notion for review.</div>
  </div>
  <div class="int-card">
    <div class="ic-title">🎙️ &nbsp;Meeting → action items</div>
    <div class="ic-flow">
      <span class="ic-app src">Fireflies transcript</span><span class="ic-arr">→</span>
      <span class="ic-app ai">AI: extract tasks</span><span class="ic-arr">→</span>
      <span class="ic-app dst">Asana / Linear</span>
    </div>
    <div class="ic-desc">When a meeting transcript is ready, AI extracts every action item with owner and deadline. Tasks are created automatically in your project tool.</div>
  </div>
  <div class="int-card">
    <div class="ic-title">🛍️ &nbsp;Review → response draft</div>
    <div class="ic-flow">
      <span class="ic-app src">Google Reviews</span><span class="ic-arr">→</span>
      <span class="ic-app ai">AI: draft reply</span><span class="ic-arr">→</span>
      <span class="ic-app dst">Google My Business</span>
    </div>
    <div class="ic-desc">New review triggers AI to draft a personalised, on-brand response. Lands in a Google Sheet for one-click approval before posting.</div>
  </div>
  <div class="int-card">
    <div class="ic-title">📊 &nbsp;Data → weekly report</div>
    <div class="ic-flow">
      <span class="ic-app src">Google Sheets</span><span class="ic-arr">→</span>
      <span class="ic-app ai">AI: analyse + write</span><span class="ic-arr">→</span>
      <span class="ic-app dst">Email / Slack</span>
    </div>
    <div class="ic-desc">Every Monday, AI reads last week's numbers, writes a plain-English summary of key trends, and sends it before standup.</div>
  </div>
</div>

---

## App Integration Quick Reference

<table class="cheat-table">
  <tr>
    <th>Task</th>
    <th>How to do it</th>
  </tr>
  <tr>
    <td>Choose a platform</td>
    <td>Zapier for ease. Make for value + visual flow. n8n for self-hosted + free at scale.</td>
  </tr>
  <tr>
    <td>Set the trigger</td>
    <td>Pick a source app and event. Filter by label, keyword, or sender to avoid noise.</td>
  </tr>
  <tr>
    <td>Reference trigger data</td>
    <td class="mono">{{Email Body}} · {{Subject}} · {{From Name}} — each platform uses its own syntax</td>
  </tr>
  <tr>
    <td>Write an AI prompt</td>
    <td>Be specific. Include the input variable. End with output format instructions.</td>
  </tr>
  <tr>
    <td>Control output format</td>
    <td>Add "Return only JSON" or "Return only bullet points" to keep AI output predictable.</td>
  </tr>
  <tr>
    <td>Pass AI output to action</td>
    <td>Reference the AI step's output with <code>{{AI Response}}</code> or equivalent in the action fields.</td>
  </tr>
  <tr>
    <td>Filter before acting</td>
    <td>Add a Filter step — only continue if AI output meets a condition. Prevents noisy alerts.</td>
  </tr>
  <tr>
    <td>Test before enabling</td>
    <td>Run each step manually with real data. Check the AI response makes sense before going live.</td>
  </tr>
  <tr>
    <td>Monitor running integrations</td>
    <td>Check the task history weekly. Look for AI drift — prompts may need tuning over time.</td>
  </tr>
  <tr>
    <td>Handle failures</td>
    <td>Add an error path or email notification so you know when a step fails silently.</td>
  </tr>
</table>

---

<!-- _class: final -->

# Your apps are talking now.
# You just had to introduce them.

&nbsp;

Trigger. AI in the middle. Action. That's every integration ever built.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*