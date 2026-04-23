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

  /* Code block */
  .code-block {
    background: #111827;
    border-radius: 8px;
    padding: 14px 20px;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #e5e7eb;
    line-height: 2;
    margin: 10px 0;
  }

  .code-block .kw  { color: #c4b5fd; }
  .code-block .fn  { color: #60a5fa; }
  .code-block .str { color: #86efac; }
  .code-block .var { color: #f9fafb; }
  .code-block .num { color: #fde68a; }
  .code-block .op  { color: #f9a8d4; }
  .code-block .cmt { color: #4b5563; font-style: italic; }

  /* Tool card grid — what a "tool" is */
  .tool-def-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin: 16px 0;
  }

  .tool-def-card {
    background: #111827;
    border-radius: 10px;
    padding: 16px 16px;
    border-top: 3px solid #1d4ed8;
  }

  .tool-def-card.search  { border-top-color: #1d4ed8; }
  .tool-def-card.code    { border-top-color: #166534; }
  .tool-def-card.send    { border-top-color: #7c3aed; }
  .tool-def-card.read    { border-top-color: #92400e; }
  .tool-def-card.write   { border-top-color: #9d174d; }
  .tool-def-card.calc    { border-top-color: #065f46; }

  .tool-def-card .tdc-icon  { font-size: 22px; margin-bottom: 6px; }
  .tool-def-card .tdc-name  { font-family: 'DM Mono', monospace; font-size: 13px; font-weight: 600; color: #f0f6fc; margin-bottom: 4px; }
  .tool-def-card .tdc-desc  { font-size: 12px; color: #9ca3af; line-height: 1.5; }

  /* API call anatomy */
  .api-anatomy {
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .api-bar {
    background: #161b22;
    padding: 8px 16px;
    border-bottom: 1px solid #30363d;
    display: flex;
    gap: 12px;
    align-items: center;
  }

  .api-bar .ab-method {
    background: #14532d;
    color: #86efac;
    font-size: 11px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 4px;
  }

  .api-bar .ab-method.post { background: #1e3a5f; color: #60a5fa; }

  .api-bar .ab-url { color: #8b949e; font-size: 12px; }

  .api-body {
    padding: 14px 18px;
    line-height: 1.9;
  }

  .api-body .ab-key   { color: #86efac; }
  .api-body .ab-val   { color: #fde68a; }
  .api-body .ab-str   { color: #79c0ff; }
  .api-body .ab-cmt   { color: #4b5563; font-style: italic; }
  .api-body .ab-plain { color: #e5e7eb; }

  /* Agent decision flow */
  .decision-flow {
    background: #111827;
    border-radius: 10px;
    padding: 18px 22px;
    margin: 14px 0;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
  }

  .df-step {
    display: flex;
    gap: 14px;
    align-items: flex-start;
    margin-bottom: 12px;
  }

  .df-step:last-child { margin-bottom: 0; }

  .df-badge {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 600;
    padding: 3px 10px;
    border-radius: 999px;
    flex-shrink: 0;
    margin-top: 1px;
    white-space: nowrap;
  }

  .df-badge.think  { background: #1e3a5f; color: #60a5fa; }
  .df-badge.select { background: #14532d; color: #86efac; }
  .df-badge.call   { background: #2e1065; color: #c4b5fd; }
  .df-badge.read   { background: #451a03; color: #fde68a; }
  .df-badge.answer { background: #111827; color: #9ca3af; border: 1px solid #374151; }

  .df-text { font-size: 13px; color: #d1d5db; line-height: 1.6; }
  .df-text span { font-family: 'DM Mono', monospace; }

  /* Example workflow */
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

  .wf-arrow {
    text-align: center;
    color: #374151;
    font-size: 16px;
    padding: 0 3px;
  }

  /* Email mock */
  .email-mock {
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 10px;
    overflow: hidden;
    margin: 12px 0;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
  }

  .email-bar {
    background: #161b22;
    padding: 8px 16px;
    border-bottom: 1px solid #30363d;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .email-bar .em-icon  { font-size: 14px; }
  .email-bar .em-label { font-family: 'DM Mono', monospace; font-size: 11px; color: #6b7280; text-transform: uppercase; letter-spacing: 0.07em; }
  .email-bar .em-status { margin-left: auto; font-family: 'DM Mono', monospace; font-size: 10px; background: #14532d; color: #86efac; padding: 2px 8px; border-radius: 999px; }

  .email-body {
    padding: 14px 18px;
    line-height: 1.9;
  }

  .email-body .ef-row {
    display: flex;
    gap: 10px;
    margin-bottom: 6px;
    font-size: 13px;
  }

  .email-body .ef-key { color: #6b7280; min-width: 60px; flex-shrink: 0; }
  .email-body .ef-val { color: #d1d5db; }
  .email-body .ef-body { color: #9ca3af; margin-top: 8px; font-size: 12px; line-height: 1.8; border-top: 1px solid #21262d; padding-top: 8px; }

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

# How AI Agents Use Tools
## And Why It's Powerful

&nbsp;

**A model without tools can only talk. With tools, it can act.**

`function calling` · `API` · `search` · `email` · `orchestration`

---

## What "Tools" Mean in AI

In AI agent terms, a "tool" is any function the agent can call to interact with the world beyond its context window.

<div class="tool-def-grid">
  <div class="tool-def-card search">
    <div class="tdc-icon">🔍</div>
    <div class="tdc-name">web_search</div>
    <div class="tdc-desc">Fetches live data from the internet. Breaks the knowledge cutoff barrier.</div>
  </div>
  <div class="tool-def-card code">
    <div class="tdc-icon">▶️</div>
    <div class="tdc-name">run_code</div>
    <div class="tdc-desc">Executes Python in a sandbox. Agent tests its own output, not just writes it.</div>
  </div>
  <div class="tool-def-card send">
    <div class="tdc-icon">📧</div>
    <div class="tdc-name">send_email</div>
    <div class="tdc-desc">Calls a mail API. Agent composes and sends — no copy-paste from you.</div>
  </div>
  <div class="tool-def-card read">
    <div class="tdc-icon">📂</div>
    <div class="tdc-name">read_file</div>
    <div class="tdc-desc">Reads files from your filesystem. Agent works with your actual data.</div>
  </div>
  <div class="tool-def-card write">
    <div class="tdc-icon">✏️</div>
    <div class="tdc-name">write_file</div>
    <div class="tdc-desc">Creates and edits files. Agent's output lands in your project, not just in chat.</div>
  </div>
  <div class="tool-def-card calc">
    <div class="tdc-icon">🧮</div>
    <div class="tdc-name">query_database</div>
    <div class="tdc-desc">Runs SQL or fetches records. Agent retrieves real data instead of hallucinating it.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## API Calls — Explained Simply

When an agent uses a tool, it makes an **API call** — a structured request to an external service.

<div class="api-anatomy">
  <div class="api-bar">
    <span class="ab-method post">POST</span>
    <span class="ab-url">https://api.sendgrid.com/v3/mail/send</span>
  </div>
  <div class="api-body">
    <span class="ab-plain">{</span><br>
    &nbsp;&nbsp;<span class="ab-key">"to"</span><span class="ab-plain">: </span><span class="ab-str">"julius@example.com"</span><span class="ab-plain">,</span><br>
    &nbsp;&nbsp;<span class="ab-key">"subject"</span><span class="ab-plain">: </span><span class="ab-str">"Monthly Grid Report Ready"</span><span class="ab-plain">,</span><br>
    &nbsp;&nbsp;<span class="ab-key">"body"</span><span class="ab-plain">: </span><span class="ab-str">"Your N-1 contingency report has been generated."</span><br>
    <span class="ab-plain">}</span><br>
    <br>
    <span class="ab-cmt">← Agent filled all of these from context. You wrote zero of it.</span>
  </div>
</div>

<div class="two-col">
  <div class="col-card">
    <div class="label">What the agent did</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">Decided an email was needed, constructed the payload from task context, called the API, handled the response.</p>
  </div>
  <div class="col-card">
    <div class="label">What you did</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">Defined the task goal upfront. Nothing else. The agent handled the entire action chain.</p>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## The Agent Decides What to Use

The agent isn't told which tool to call. It reads the task, reasons about what's needed, and selects — the same way a developer would.

<div class="decision-flow">
  <div class="df-step">
    <span class="df-badge think">Think</span>
    <span class="df-text">Task: "Summarise today's energy news and send me a digest." — I need current news, so I need to search the web first.</span>
  </div>
  <div class="df-step">
    <span class="df-badge select">Select</span>
    <span class="df-text">Tool chosen: <span>web_search</span> — query: <span>"energy news today"</span></span>
  </div>
  <div class="df-step">
    <span class="df-badge call">Call</span>
    <span class="df-text"><span>web_search(query="energy news today")</span> → returns 8 articles with titles, sources, snippets</span>
  </div>
  <div class="df-step">
    <span class="df-badge read">Read</span>
    <span class="df-text">Results ingested. Now I have content to summarise. Next tool needed: <span>send_email</span> to deliver the digest.</span>
  </div>
  <div class="df-step">
    <span class="df-badge answer">Done</span>
    <span class="df-text">Email composed from search results and sent. Task complete. No human required between steps.</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">EXAMPLE 01</div>

## Search + Summarize

A two-tool chain that turns a question into a briefing:

<div class="workflow-strip">
  <div class="wf-node w1">
    <div class="wn-icon">💬</div>
    <div class="wn-label">Task</div>
    <div class="wn-desc">"Summarise solar tariff news in the Philippines this week"</div>
  </div>
  <div class="wf-arrow">→</div>
  <div class="wf-node w2">
    <div class="wn-icon">🔍</div>
    <div class="wn-label">web_search</div>
    <div class="wn-desc">Queries news API for recent articles</div>
  </div>
  <div class="wf-arrow">→</div>
  <div class="wf-node w3">
    <div class="wn-icon">📄</div>
    <div class="wn-label">fetch_page</div>
    <div class="wn-desc">Reads full article bodies from top results</div>
  </div>
  <div class="wf-arrow">→</div>
  <div class="wf-node w4">
    <div class="wn-icon">🧠</div>
    <div class="wn-label">Summarise</div>
    <div class="wn-desc">Model distills key points from retrieved content</div>
  </div>
  <div class="wf-arrow">→</div>
  <div class="wf-node w5">
    <div class="wn-icon">✅</div>
    <div class="wn-label">Output</div>
    <div class="wn-desc">Formatted briefing delivered to you</div>
  </div>
</div>

<div class="highlight">

**What changed:** the agent didn't just answer from training data — it searched, retrieved, and synthesized live information. The output is current, sourced, and specific to your query. Without tools, a model would have to guess or admit it doesn't know.

</div>

---

<!-- _class: step -->

<div class="step-badge">EXAMPLE 02</div>

## Email Automation Pipeline

A four-tool chain that runs your reporting workflow end-to-end:

<div class="workflow-strip">
  <div class="wf-node w1">
    <div class="wn-icon">📂</div>
    <div class="wn-label">read_file</div>
    <div class="wn-desc">Loads this week's grid results CSV</div>
  </div>
  <div class="wf-arrow">→</div>
  <div class="wf-node w2">
    <div class="wn-icon">▶️</div>
    <div class="wn-label">run_code</div>
    <div class="wn-desc">Runs pandas summary: voltage flags, region totals</div>
  </div>
  <div class="wf-arrow">→</div>
  <div class="wf-node w3">
    <div class="wn-icon">✏️</div>
    <div class="wn-label">write_file</div>
    <div class="wn-desc">Saves formatted report to summary.xlsx</div>
  </div>
  <div class="wf-arrow">→</div>
  <div class="wf-node w4">
    <div class="wn-icon">📧</div>
    <div class="wn-label">send_email</div>
    <div class="wn-desc">Sends report to team with summary in body</div>
  </div>
  <div class="wf-arrow">→</div>
  <div class="wf-node w5">
    <div class="wn-icon">✅</div>
    <div class="wn-label">Done</div>
    <div class="wn-desc">Full workflow completed autonomously</div>
  </div>
</div>

<div class="email-mock">
  <div class="email-bar">
    <span class="em-icon">📧</span>
    <span class="em-label">Outbound — agent-generated</span>
    <span class="em-status">✓ Sent</span>
  </div>
  <div class="email-body">
    <div class="ef-row"><span class="ef-key">To:</span><span class="ef-val">grid-team@company.com</span></div>
    <div class="ef-row"><span class="ef-key">Subject:</span><span class="ef-val">Weekly Visayas Grid Report — 3 undervoltage flags</span></div>
    <div class="ef-body">Summary attached. 3 buses flagged below 0.95 pu in Region VII. Full contingency results in summary.xlsx. — Auto-generated by pipeline agent.</div>
  </div>
</div>

---

## Defining a Tool in Code

Tools are just Python functions with a description. The model reads the description and decides when to call them.

<div class="code-block">
  <span class="kw">import</span> <span class="var">anthropic</span><br>
  <br>
  <span class="var">tools</span> <span class="op">=</span> [<br>
  &nbsp;&nbsp;{<br>
  &nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"name"</span>: <span class="str">"web_search"</span>,<br>
  &nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"description"</span>: <span class="str">"Search the web for current information on a topic."</span>,<br>
  &nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"input_schema"</span>: {<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"type"</span>: <span class="str">"object"</span>,<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"properties"</span>: {<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"query"</span>: {<span class="str">"type"</span>: <span class="str">"string"</span>, <span class="str">"description"</span>: <span class="str">"Search query"</span>}<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;},<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"required"</span>: [<span class="str">"query"</span>]<br>
  &nbsp;&nbsp;&nbsp;&nbsp;}<br>
  &nbsp;&nbsp;}<br>
  ]<br>
  <br>
  <span class="cmt"># Pass tools to the model — it decides when and how to call them</span><br>
  <span class="var">response</span> <span class="op">=</span> <span class="var">client</span>.<span class="var">messages</span>.<span class="fn">create</span>(<br>
  &nbsp;&nbsp;<span class="var">model</span><span class="op">=</span><span class="str">"claude-sonnet-4-20250514"</span>, <span class="var">tools</span><span class="op">=</span><span class="var">tools</span>, <span class="var">messages</span><span class="op">=</span>[...]<br>
  )
</div>

---

<!-- _class: final -->

# Language is the interface.
# Tools are the hands.

&nbsp;

An agent with tools doesn't just answer — it acts, fetches, creates, and delivers.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*