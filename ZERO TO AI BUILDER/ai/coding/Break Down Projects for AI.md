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

  /* ── Bad prompt / good prompt comparison ── */
  .prompt-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 16px;
  }

  .pc-col { display: flex; flex-direction: column; gap: 0; }

  .pc-col .pc-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    padding: 8px 14px;
    border-radius: 8px 8px 0 0;
  }

  .pc-col.bad  .pc-label { background: #fef2f2; color: #991b1b; border: 1px solid #fecaca; border-bottom: none; }
  .pc-col.good .pc-label { background: #f0fdf4; color: #166534; border: 1px solid #bbf7d0; border-bottom: none; }

  .pc-col .pc-body {
    border-radius: 0 0 10px 10px;
    padding: 14px 16px;
    font-size: 13.5px;
    line-height: 1.7;
    border: 1px solid var(--border);
  }

  .pc-col.bad  .pc-body { background: var(--white); color: var(--muted); border: 1px solid #fecaca; border-top: none; }
  .pc-col.good .pc-body { background: var(--white); color: var(--text);  border: 1px solid #bbf7d0; border-top: none; }

  .pc-col .pc-body .pc-hi { color: var(--blue); font-weight: 600; }
  .pc-col .pc-body .pc-num {
    display: inline-block;
    background: var(--blue);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    width: 20px;
    height: 20px;
    border-radius: 999px;
    text-align: center;
    line-height: 20px;
    margin-right: 5px;
    flex-shrink: 0;
  }

  /* ── Pipeline flow diagram ── */
  .pipeline {
    display: flex;
    flex-direction: column;
    gap: 0;
    margin: 16px 0;
  }

  .pipeline-step {
    display: flex;
    align-items: stretch;
    gap: 0;
  }

  .pipeline-step .ps-num {
    background: var(--blue);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    font-weight: 600;
    width: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    border-radius: 8px 0 0 8px;
  }

  .pipeline-step .ps-content {
    background: var(--white);
    border: 1px solid var(--border);
    border-left: none;
    border-radius: 0 8px 8px 0;
    padding: 11px 16px;
    flex: 1;
  }

  .pipeline-step .ps-title {
    font-weight: 600;
    font-size: 14px;
    color: var(--text);
  }

  .pipeline-step .ps-prompt {
    font-family: 'DM Mono', monospace;
    font-size: 11.5px;
    color: var(--blue);
    margin-top: 3px;
    line-height: 1.5;
  }

  .pipeline-step .ps-output {
    font-size: 12px;
    color: var(--muted);
    margin-top: 3px;
  }

  .pipeline-arrow {
    display: flex;
    align-items: center;
    padding: 3px 0 3px 17px;
  }

  .pipeline-arrow .pa-line {
    width: 1px;
    height: 100%;
    background: var(--border);
    margin-right: 6px;
    min-height: 14px;
  }

  .pipeline-arrow .pa-text {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    color: var(--muted);
  }

  /* ── Output feed box ── */
  .feed-row {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    gap: 10px;
    align-items: center;
    margin: 14px 0;
  }

  .feed-box {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .feed-box .fb-label {
    padding: 7px 14px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    background: var(--off-white);
    border-bottom: 1px solid var(--border);
    color: var(--muted);
  }

  .feed-box .fb-body {
    padding: 12px 14px;
    background: var(--white);
    font-size: 13px;
    color: var(--text);
    line-height: 1.6;
  }

  .feed-box.output .fb-label { background: #f0fdf4; color: #166534; border-color: #bbf7d0; }
  .feed-box.output            { border-color: #bbf7d0; }
  .feed-box.input  .fb-label  { background: var(--blue-light); color: #1e40af; border-color: var(--blue-mid); }
  .feed-box.input             { border-color: var(--blue-mid); }

  .feed-arrow {
    font-size: 22px;
    color: var(--blue);
    text-align: center;
    flex-shrink: 0;
  }

  /* ── Real breakdown example ── */
  .breakdown-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 14px;
  }

  .breakdown-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
  }

  .breakdown-card .bc-header {
    background: var(--off-white);
    padding: 9px 14px;
    display: flex;
    align-items: center;
    gap: 10px;
    border-bottom: 1px solid var(--border);
  }

  .breakdown-card .bc-num {
    background: var(--blue);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    width: 22px;
    height: 22px;
    border-radius: 999px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }

  .breakdown-card .bc-title {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
  }

  .breakdown-card .bc-body {
    padding: 10px 14px;
  }

  .breakdown-card .bc-prompt {
    font-family: 'DM Mono', monospace;
    font-size: 11.5px;
    color: var(--blue);
    line-height: 1.6;
    margin-bottom: 6px;
  }

  .breakdown-card .bc-output {
    font-size: 12px;
    color: var(--muted);
    padding: 6px 10px;
    background: var(--off-white);
    border-radius: 6px;
    border: 1px solid var(--border);
    line-height: 1.5;
  }

  /* ── Chunking rules list ── */
  .rule-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 14px;
  }

  .rule-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 13px 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }

  .rule-card .rc-icon {
    font-size: 20px;
    flex-shrink: 0;
    margin-top: 1px;
  }

  .rule-card .rc-title {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
    margin-bottom: 3px;
  }

  .rule-card .rc-desc {
    font-size: 12.5px;
    color: var(--muted);
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

# Break Down Projects
## for AI

&nbsp;

**The single most important skill for working with AI.** Not prompting. Decomposition.

`chunk` · `sequence` · `output → input` · `one job per prompt`

---

## Why Big Prompts Fail

Asking AI to "build me a full website" in one prompt is like hiring a contractor and handing them a napkin sketch. The output will technically answer the prompt — and be completely unusable.

<div class="tools">
  <div class="tool-card">
    <div class="icon">🌊</div>
    <div class="name">Context overflow</div>
    <div class="desc">The more you ask for at once, the more the model spreads its attention. Early requirements get "forgotten" as the prompt grows longer.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🎯</div>
    <div class="name">Vague = vague output</div>
    <div class="desc">A big vague request produces a big vague response. The model fills gaps with assumptions — not your actual requirements.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔁</div>
    <div class="name">Hard to iterate</div>
    <div class="desc">When a 2,000-word output is 80% right, you can't easily fix the 20%. You either regenerate everything or manually edit a wall of text.</div>
  </div>
  <div class="tool-card">
    <div class="icon">❌</div>
    <div class="name">No quality checkpoints</div>
    <div class="desc">One big prompt means one final review. If something breaks, you don't know which part of the request caused it — or where to re-enter.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## One Prompt, One Job

The core rule of AI decomposition: **each prompt does exactly one thing.**

<div class="prompt-compare">
  <div class="pc-col bad">
    <div class="pc-label">❌ &nbsp;One massive prompt</div>
    <div class="pc-body">
      Build me a personal finance tracker. It should have a dashboard, expense categories, monthly budget goals, a CSV import feature, charts for spending trends, email reminders, and a mobile-friendly design. Use React and a PostgreSQL backend.
    </div>
  </div>
  <div class="pc-col good">
    <div class="pc-label">✅ &nbsp;Broken into jobs</div>
    <div class="pc-body">
      <div style="margin-bottom:8px;"><span class="pc-num">1</span> <span class="pc-hi">Data model:</span> What fields does an Expense record need?</div>
      <div style="margin-bottom:8px;"><span class="pc-num">2</span> <span class="pc-hi">Schema:</span> Write the PostgreSQL tables for expenses + categories.</div>
      <div style="margin-bottom:8px;"><span class="pc-num">3</span> <span class="pc-hi">API:</span> Write a FastAPI endpoint to add an expense.</div>
      <div style="margin-bottom:8px;"><span class="pc-num">4</span> <span class="pc-hi">Component:</span> Build the ExpenseForm React component.</div>
      <div><span class="pc-num">5</span> <span class="pc-hi">Chart:</span> Add a spending-by-category bar chart using the API data.</div>
    </div>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**The test:** Can you describe what this prompt produces in one sentence? If not — split it. "Write the database schema for expenses" passes. "Build the whole app" doesn't.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Chunking Tasks — The Rules

<div class="rule-grid">
  <div class="rule-card">
    <div class="rc-icon">✂️</div>
    <div>
      <div class="rc-title">Split by deliverable</div>
      <div class="rc-desc">Each prompt should produce one concrete thing — a schema, a function, a component, a plan, a list. Not "the backend."</div>
    </div>
  </div>
  <div class="rule-card">
    <div class="rc-icon">📐</div>
    <div>
      <div class="rc-title">Separate thinking from doing</div>
      <div class="rc-desc">Use one prompt to plan ("List the steps to build X"), then separate prompts to execute each step. Never plan and build in the same request.</div>
    </div>
  </div>
  <div class="rule-card">
    <div class="rc-icon">🔢</div>
    <div>
      <div class="rc-title">Order matters</div>
      <div class="rc-desc">Foundations first. Data model before API. API before UI. Schema before validation logic. Respect the dependency tree.</div>
    </div>
  </div>
  <div class="rule-card">
    <div class="rc-icon">🧪</div>
    <div>
      <div class="rc-title">Verify before moving on</div>
      <div class="rc-desc">Test or review each output before feeding it to the next prompt. A wrong schema propagates through every step that follows it.</div>
    </div>
  </div>
  <div class="rule-card">
    <div class="rc-icon">📏</div>
    <div>
      <div class="rc-title">Keep prompts focused</div>
      <div class="rc-desc">A prompt that produces 20–50 lines of output is usually well-scoped. Prompts that produce 500+ lines are doing too much at once.</div>
    </div>
  </div>
  <div class="rule-card">
    <div class="rc-icon">🏷️</div>
    <div>
      <div class="rc-title">Name your chunks</div>
      <div class="rc-desc">Label each step before you start: "Step 3 — API endpoint." This keeps you oriented and makes it easier to backtrack if something breaks.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Define Steps Clearly

A well-defined step has three parts: **context**, **task**, and **output format**.

<div class="pipeline">
  <div class="pipeline-step">
    <div class="ps-num">1</div>
    <div class="ps-content">
      <div class="ps-title">Context — what AI needs to know</div>
      <div class="ps-prompt">"We are building a personal finance tracker. The Expense model has: id, amount, category, date, note."</div>
    </div>
  </div>
  <div class="pipeline-arrow"><div class="pa-line"></div><div class="pa-text">then</div></div>
  <div class="pipeline-step">
    <div class="ps-num">2</div>
    <div class="ps-content">
      <div class="ps-title">Task — the one thing to do</div>
      <div class="ps-prompt">"Write a FastAPI POST endpoint at /expenses that validates and inserts a new expense into PostgreSQL."</div>
    </div>
  </div>
  <div class="pipeline-arrow"><div class="pa-line"></div><div class="pa-text">then</div></div>
  <div class="pipeline-step">
    <div class="ps-num">3</div>
    <div class="ps-content">
      <div class="ps-title">Output format — what to return</div>
      <div class="ps-prompt">"Return only the Python function. No explanation. Include the Pydantic schema and database call."</div>
    </div>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**Context carries forward.** Paste the relevant output from the previous step into the next prompt as context. The model has no memory between conversations — you are the pipeline's state.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Feed Outputs into the Next Step

Each step produces an artifact. That artifact becomes the context for the next prompt.

<div class="feed-row">
  <div class="feed-box output">
    <div class="fb-label">✅ &nbsp;Output of Step 2</div>
    <div class="fb-body">
      <code style="font-size:12px;">CREATE TABLE expenses (<br>
      &nbsp;&nbsp;id SERIAL PRIMARY KEY,<br>
      &nbsp;&nbsp;amount NUMERIC(10,2),<br>
      &nbsp;&nbsp;category TEXT,<br>
      &nbsp;&nbsp;date DATE,<br>
      &nbsp;&nbsp;note TEXT<br>
      );</code>
    </div>
  </div>
  <div class="feed-arrow">→</div>
  <div class="feed-box input">
    <div class="fb-label">📥 &nbsp;Input to Step 3</div>
    <div class="fb-body" style="font-size:13px; line-height:1.7;">
      "Using this schema:<br>
      <em>[paste SQL above]</em><br><br>
      Write a FastAPI endpoint to insert a new expense. Return only the Python code."
    </div>
  </div>
</div>

<div class="two-col" style="margin-top:14px;">
  <div class="col-card">
    <div class="label">What to carry forward</div>
    <p style="font-size:13.5px; margin-top:6px;">The <strong>exact output</strong> of the previous step — code, schema, list, decisions. Not a summary. Paste the raw artifact directly into the next prompt.</p>
  </div>
  <div class="col-card">
    <div class="label">What to leave out</div>
    <p style="font-size:13.5px; margin-top:6px;">Explanations, disclaimers, and the model's preamble from the previous response. Strip it down to just the artifact — code, JSON, list items.</p>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## Full Example Breakdown

**Project:** Build a blog post ideas generator from a user's website URL.

<div class="breakdown-grid">
  <div class="breakdown-card">
    <div class="bc-header">
      <div class="bc-num">1</div>
      <div class="bc-title">Plan the steps</div>
    </div>
    <div class="bc-body">
      <div class="bc-prompt">"List the steps to build a Python script that takes a URL, scrapes the page text, and generates 5 blog post ideas."</div>
      <div class="bc-output">Output: numbered list of 6 steps → use as the roadmap</div>
    </div>
  </div>
  <div class="breakdown-card">
    <div class="bc-header">
      <div class="bc-num">2</div>
      <div class="bc-title">Scrape the URL</div>
    </div>
    <div class="bc-body">
      <div class="bc-prompt">"Write a Python function that fetches a URL with requests and extracts the main body text using BeautifulSoup."</div>
      <div class="bc-output">Output: get_page_text(url) function → save to scraper.py</div>
    </div>
  </div>
  <div class="breakdown-card">
    <div class="bc-header">
      <div class="bc-num">3</div>
      <div class="bc-title">Build the AI prompt</div>
    </div>
    <div class="bc-body">
      <div class="bc-prompt">"Given this page text, write a prompt template that asks an AI to generate 5 specific, non-obvious blog post ideas. Output JSON array."</div>
      <div class="bc-output">Output: prompt template string → save to prompts.py</div>
    </div>
  </div>
  <div class="breakdown-card">
    <div class="bc-header">
      <div class="bc-num">4</div>
      <div class="bc-title">Call the API</div>
    </div>
    <div class="bc-body">
      <div class="bc-prompt">"Using this prompt template [paste it]: write a function that calls the Anthropic API and returns the parsed JSON response."</div>
      <div class="bc-output">Output: generate_ideas(text) function → save to api.py</div>
    </div>
  </div>
  <div class="breakdown-card">
    <div class="bc-header">
      <div class="bc-num">5</div>
      <div class="bc-title">Wire it together</div>
    </div>
    <div class="bc-body">
      <div class="bc-prompt">"Here are the three functions [paste all]. Write a main.py that takes a URL as CLI input, runs the pipeline, and prints results."</div>
      <div class="bc-output">Output: main.py — the complete working script</div>
    </div>
  </div>
  <div class="breakdown-card">
    <div class="bc-header">
      <div class="bc-num">6</div>
      <div class="bc-title">Handle errors</div>
    </div>
    <div class="bc-body">
      <div class="bc-prompt">"Here is main.py [paste it]. Add error handling for: network timeout, empty page, invalid JSON from AI. Keep the same structure."</div>
      <div class="bc-output">Output: improved main.py — production-ready</div>
    </div>
  </div>
</div>

---

## Project Decomposition Cheatsheet

<table class="cheat-table">
  <tr>
    <th>Situation</th>
    <th>What to do</th>
  </tr>
  <tr>
    <td>Starting a new project</td>
    <td>First prompt: "List the steps to build X." Use the output as your task list — don't skip this.</td>
  </tr>
  <tr>
    <td>Prompt feels too long</td>
    <td>If you're using "and" more than twice, split the prompt. Each "and" is a separate task.</td>
  </tr>
  <tr>
    <td>Output was almost right</td>
    <td>Don't regenerate everything. Paste the output back and ask for one specific change: "Change only the error handling."</td>
  </tr>
  <tr>
    <td>Something broke mid-pipeline</td>
    <td>Go back to the last good artifact. Fix that step, then re-run only the steps that depend on it.</td>
  </tr>
  <tr>
    <td>Moving to the next step</td>
    <td>Paste the previous output as context. Be explicit: "Using this [artifact], now do [next task]."</td>
  </tr>
  <tr>
    <td>Unsure how to split a task</td>
    <td>Ask AI: "Break this task into the smallest independent steps: [describe the task]." Use that as your plan.</td>
  </tr>
  <tr>
    <td>Output is too generic</td>
    <td>Add constraints: length, format, tone, specific fields. Generic prompts get generic answers.</td>
  </tr>
  <tr>
    <td>Need to review a long output</td>
    <td>Ask AI to review it too: "Here is the code from the last step. What could break? What's missing?"</td>
  </tr>
  <tr>
    <td>Prompt keeps failing</td>
    <td>The step is probably still too big. Ask: "What are the two sub-tasks inside this step?" and split further.</td>
  </tr>
</table>

---

<!-- _class: final -->

# Small prompts.
# Big results.

&nbsp;

One job per prompt. Verify. Feed forward. Repeat.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*