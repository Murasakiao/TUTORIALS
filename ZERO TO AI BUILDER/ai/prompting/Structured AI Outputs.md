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

  .warning {
    background: #fef2f2;
    border: 1px solid #fecaca;
    border-radius: 10px;
    padding: 18px 24px;
    margin: 16px 0;
  }

  .warning p { color: #991b1b; margin: 0; }
  .warning strong { color: #7f1d1d; }

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

  /* ── Code block ── */
  .code-block {
    background: #111827;
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .code-block .cb-bar {
    background: #1f2937;
    padding: 8px 16px;
    font-size: 11.5px;
    color: #6b7280;
    letter-spacing: 0.04em;
  }

  .code-block .cb-body {
    padding: 14px 20px;
    line-height: 2;
  }

  .cb-kw     { color: #c084fc; }
  .cb-fn     { color: #60a5fa; }
  .cb-str    { color: #fde68a; }
  .cb-num    { color: #fb923c; }
  .cb-cmt    { color: #4b5563; font-style: italic; }
  .cb-var    { color: #f9fafb; }
  .cb-prop   { color: #34d399; }
  .cb-op     { color: #6b7280; }
  .cb-out    { color: #9ca3af; }
  .cb-hi     { color: #34d399; }
  .cb-bad    { color: #f87171; }
  .cb-tag    { color: #f87171; }
  .cb-attr   { color: #93c5fd; }
  .cb-prompt { color: #22c55e; }
  .cb-cmd    { color: #f9fafb; }

  /* ── JSON viewer ── */
  .json-block {
    background: #111827;
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 12.5px;
  }

  .json-block .jb-bar {
    background: #1f2937;
    padding: 8px 16px;
    font-size: 11.5px;
    color: #6b7280;
    letter-spacing: 0.04em;
  }

  .json-block .jb-body {
    padding: 14px 22px;
    line-height: 2;
  }

  .jb-key   { color: #93c5fd; }
  .jb-str   { color: #fde68a; }
  .jb-num   { color: #fb923c; }
  .jb-bool  { color: #c084fc; }
  .jb-null  { color: #6b7280; }
  .jb-punct { color: #4b5563; }
  .jb-hl    { color: #34d399; }

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

  /* ── Prompt → output comparison ── */
  .prompt-output {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 14px;
  }

  .po-col { display: flex; flex-direction: column; gap: 8px; }

  .po-col .po-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.07em;
    padding: 0 2px;
  }

  .po-prompt {
    background: #1e293b;
    border-radius: 10px;
    padding: 14px 18px;
    font-size: 13.5px;
    color: #e2e8f0;
    line-height: 1.7;
    border-left: 3px solid #3b82f6;
  }

  .po-prompt .po-hi {
    color: #93c5fd;
    font-weight: 600;
  }

  /* ── Schema anatomy box ── */
  .schema-box {
    background: #111827;
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 12.5px;
  }

  .schema-box .sb-bar {
    background: #1f2937;
    padding: 8px 16px;
    font-size: 11.5px;
    color: #6b7280;
    letter-spacing: 0.04em;
  }

  .schema-box .sb-body {
    padding: 14px 22px;
    line-height: 2;
  }

  .sb-key    { color: #93c5fd; }
  .sb-type   { color: #c084fc; }
  .sb-str    { color: #fde68a; }
  .sb-req    { color: #34d399; }
  .sb-opt    { color: #fb923c; }
  .sb-punct  { color: #4b5563; }
  .sb-cmt    { color: #374151; font-style: italic; }

  /* ── Use case cards ── */
  .usecase-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .usecase-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 18px;
    display: flex;
    align-items: flex-start;
    gap: 13px;
  }

  .usecase-card .uc-icon { font-size: 24px; flex-shrink: 0; }

  .usecase-card .uc-title {
    font-weight: 600;
    font-size: 14px;
    color: var(--text);
    margin-bottom: 3px;
  }

  .usecase-card .uc-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.5;
  }

  .usecase-card .uc-tag {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    color: var(--blue);
    background: var(--blue-light);
    border: 1px solid var(--blue-mid);
    padding: 2px 7px;
    border-radius: 4px;
    display: inline-block;
    margin-top: 5px;
  }

  /* ── Mistake cards ── */
  .mistake-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 14px;
  }

  .mistake-card {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid #fecaca;
  }

  .mistake-card .mc-head {
    background: #fef2f2;
    padding: 8px 14px;
    font-weight: 600;
    font-size: 13px;
    color: #991b1b;
    display: flex;
    align-items: center;
    gap: 7px;
  }

  .mistake-card .mc-body {
    padding: 10px 14px;
    background: var(--white);
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.55;
  }

  .mistake-card .mc-fix {
    padding: 8px 14px 10px;
    background: #f0fdf4;
    font-size: 12px;
    color: #166534;
    font-family: 'DM Mono', monospace;
    border-top: 1px solid #bbf7d0;
  }

  /* ── Cmd grid ── */
  .cmd-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 12px;
  }

  .cmd-row {
    background: #111827;
    border-radius: 8px;
    padding: 12px 16px;
    display: flex;
    align-items: flex-start;
    gap: 14px;
  }

  .cmd-row .cmd-name {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #60a5fa;
    font-weight: 500;
    min-width: 110px;
    padding-top: 1px;
  }

  .cmd-row .cmd-desc {
    font-size: 13px;
    color: #d1d5db;
    line-height: 1.5;
  }

  .cmd-row .cmd-desc span {
    display: block;
    color: #6b7280;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    margin-top: 2px;
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

# Structured Outputs
## from AI

&nbsp;

**Stop copying text. Start parsing data.** JSON, tables, and schemas.

`JSON` · `schema` · `json.loads()` · `response_format` · `Pydantic`

---

## Why Structure Matters

Unstructured AI responses are useful for reading. They're useless for code.

<div class="tools">
  <div class="tool-card">
    <div class="icon">🔗</div>
    <div class="name">Plug into pipelines</div>
    <div class="desc">JSON output can be parsed into Python dicts, passed to APIs, stored in databases, or fed into the next step of a workflow — all automatically.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔁</div>
    <div class="name">Reliable and repeatable</div>
    <div class="desc">A consistent schema means the same code works every time. No regex. No fragile text parsing. No "sometimes it adds a header, sometimes it doesn't."</div>
  </div>
  <div class="tool-card">
    <div class="icon">📊</div>
    <div class="name">Tables become data</div>
    <div class="desc">Ask for a table as JSON and you get an array of objects you can sort, filter, and render in any format — not a markdown string you have to scrape.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🛡️</div>
    <div class="name">Validate before using</div>
    <div class="desc">Once output is structured, you can validate it — check that required fields exist, values are the right type, and nothing unexpected crept in.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Ask for JSON Format

The simplest technique — tell the model exactly what format you want in the prompt itself.

<div class="prompt-output">
  <div class="po-col">
    <div class="po-label">❌ &nbsp;Unstructured prompt</div>
    <div class="po-prompt">Tell me about three Python web frameworks.</div>
  </div>
  <div class="po-col">
    <div class="po-label">✅ &nbsp;Structured prompt</div>
    <div class="po-prompt">List three Python web frameworks. <span class="po-hi">Return only a JSON array</span>. Each object must have: <span class="po-hi">"name"</span> (string), <span class="po-hi">"use_case"</span> (string), <span class="po-hi">"stars_github"</span> (number). <span class="po-hi">No extra text, no markdown fences.</span></div>
  </div>
</div>

<div class="json-block" style="margin-top:4px;">
  <div class="jb-bar">AI response — clean, parseable JSON</div>
  <div class="jb-body">
    <span class="jb-punct">[</span><br>
    &nbsp;&nbsp;<span class="jb-punct">{</span> <span class="jb-key">"name"</span><span class="jb-punct">:</span> <span class="jb-str">"FastAPI"</span><span class="jb-punct">,</span> <span class="jb-key">"use_case"</span><span class="jb-punct">:</span> <span class="jb-str">"REST APIs"</span><span class="jb-punct">,</span> <span class="jb-key">"stars_github"</span><span class="jb-punct">:</span> <span class="jb-num">72000</span> <span class="jb-punct">},</span><br>
    &nbsp;&nbsp;<span class="jb-punct">{</span> <span class="jb-key">"name"</span><span class="jb-punct">:</span> <span class="jb-str">"Django"</span><span class="jb-punct">,</span> <span class="jb-key">"use_case"</span><span class="jb-punct">:</span> <span class="jb-str">"Full-stack web"</span><span class="jb-punct">,</span> <span class="jb-key">"stars_github"</span><span class="jb-punct">:</span> <span class="jb-num">78000</span> <span class="jb-punct">},</span><br>
    &nbsp;&nbsp;<span class="jb-punct">{</span> <span class="jb-key">"name"</span><span class="jb-punct">:</span> <span class="jb-str">"Flask"</span><span class="jb-punct">,</span> <span class="jb-key">"use_case"</span><span class="jb-punct">:</span> <span class="jb-str">"Lightweight APIs"</span><span class="jb-punct">,</span> <span class="jb-key">"stars_github"</span><span class="jb-punct">:</span> <span class="jb-num">67000</span> <span class="jb-punct">}</span><br>
    <span class="jb-punct">]</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Define a Schema in Your Prompt

A schema is an explicit contract — it tells the model exactly what fields to return, what type each one is, and which are required.

<div class="schema-box">
  <div class="sb-bar">prompt — schema definition in plain text</div>
  <div class="sb-body">
    Extract product data from the review below.<br>
    Return a JSON object with <span class="sb-req">exactly</span> these fields:<br>
    <span class="sb-punct">{</span><br>
    &nbsp;&nbsp;<span class="sb-key">"product_name"</span>  <span class="sb-punct">:</span> <span class="sb-type">string</span>             <span class="sb-cmt">// required</span><br>
    &nbsp;&nbsp;<span class="sb-key">"rating"</span>         <span class="sb-punct">:</span> <span class="sb-type">number</span> <span class="sb-punct">(</span><span class="sb-num">1</span><span class="sb-punct">–</span><span class="sb-num">5</span><span class="sb-punct">)</span>      <span class="sb-cmt">// required</span><br>
    &nbsp;&nbsp;<span class="sb-key">"pros"</span>           <span class="sb-punct">:</span> <span class="sb-type">array of strings</span>  <span class="sb-cmt">// required</span><br>
    &nbsp;&nbsp;<span class="sb-key">"cons"</span>           <span class="sb-punct">:</span> <span class="sb-type">array of strings</span>  <span class="sb-cmt">// required</span><br>
    &nbsp;&nbsp;<span class="sb-key">"would_recommend"</span><span class="sb-punct">:</span> <span class="sb-type">boolean</span>           <span class="sb-cmt">// required</span><br>
    &nbsp;&nbsp;<span class="sb-key">"price_mentioned"</span><span class="sb-punct">:</span> <span class="sb-type">string or null</span>    <span class="sb-cmt">// optional</span><br>
    <span class="sb-punct">}</span><br>
    If a field cannot be determined, use <span class="sb-type">null</span>. Return only JSON.
  </div>
</div>

<div class="highlight">

**The magic phrase:** "Return only JSON. No explanation, no markdown fences, no preamble." Without this, models often wrap output in ```json … ``` or add a sentence before it — which breaks `json.loads()`.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Parse and Validate the Output

Getting JSON from the model is step one. Parsing and validating it in Python is step two — always.

<div class="code-block">
  <div class="cb-bar">parse_output.py — safe JSON parsing</div>
  <div class="cb-body">
    <span class="cb-kw">import</span> <span class="cb-var">json</span><span class="cb-op">,</span> <span class="cb-var">re</span><br>
    <br>
    <span class="cb-kw">def</span> <span class="cb-fn">extract_json</span><span class="cb-op">(</span><span class="cb-var">text</span><span class="cb-op">):</span><br>
    &nbsp;&nbsp;<span class="cb-cmt"># Strip markdown fences if the model added them anyway</span><br>
    &nbsp;&nbsp;<span class="cb-var">clean</span> <span class="cb-op">=</span> <span class="cb-var">re</span><span class="cb-op">.</span><span class="cb-fn">sub</span><span class="cb-op">(</span><span class="cb-str">r'```(?:json)?\s*|\s*```'</span><span class="cb-op">,</span> <span class="cb-str">''</span><span class="cb-op">,</span> <span class="cb-var">text</span><span class="cb-op">.</span><span class="cb-fn">strip</span><span class="cb-op">())</span><br>
    &nbsp;&nbsp;<span class="cb-kw">return</span> <span class="cb-var">json</span><span class="cb-op">.</span><span class="cb-fn">loads</span><span class="cb-op">(</span><span class="cb-var">clean</span><span class="cb-op">)</span><br>
    <br>
    <span class="cb-kw">def</span> <span class="cb-fn">validate_product</span><span class="cb-op">(</span><span class="cb-var">data</span><span class="cb-op">):</span><br>
    &nbsp;&nbsp;<span class="cb-var">required</span> <span class="cb-op">=</span> <span class="cb-op">[</span><span class="cb-str">"product_name"</span><span class="cb-op">,</span> <span class="cb-str">"rating"</span><span class="cb-op">,</span> <span class="cb-str">"pros"</span><span class="cb-op">,</span> <span class="cb-str">"cons"</span><span class="cb-op">,</span> <span class="cb-str">"would_recommend"</span><span class="cb-op">]</span><br>
    &nbsp;&nbsp;<span class="cb-kw">for</span> <span class="cb-var">field</span> <span class="cb-kw">in</span> <span class="cb-var">required</span><span class="cb-op">:</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-kw">if</span> <span class="cb-var">field</span> <span class="cb-kw">not</span> <span class="cb-kw">in</span> <span class="cb-var">data</span><span class="cb-op">:</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-kw">raise</span> <span class="cb-fn">ValueError</span><span class="cb-op">(</span><span class="cb-str">f"Missing field: </span><span class="cb-op">{</span><span class="cb-var">field</span><span class="cb-op">}</span><span class="cb-str">"</span><span class="cb-op">)</span><br>
    &nbsp;&nbsp;<span class="cb-kw">if</span> <span class="cb-kw">not</span> <span class="cb-num">1</span> <span class="cb-op"><=</span> <span class="cb-var">data</span><span class="cb-op">[</span><span class="cb-str">"rating"</span><span class="cb-op">]</span> <span class="cb-op"><=</span> <span class="cb-num">5</span><span class="cb-op">:</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-kw">raise</span> <span class="cb-fn">ValueError</span><span class="cb-op">(</span><span class="cb-str">"Rating must be 1–5"</span><span class="cb-op">)</span><br>
    &nbsp;&nbsp;<span class="cb-kw">return</span> <span class="cb-var">data</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Use Pydantic for Robust Validation

For production code, Pydantic turns your schema into a Python class that validates automatically.

<div class="code-block">
  <div class="cb-bar">models.py — Pydantic schema</div>
  <div class="cb-body">
    <span class="cb-kw">from</span> <span class="cb-var">pydantic</span> <span class="cb-kw">import</span> <span class="cb-var">BaseModel</span><span class="cb-op">,</span> <span class="cb-var">Field</span><br>
    <span class="cb-kw">from</span> <span class="cb-var">typing</span> <span class="cb-kw">import</span> <span class="cb-var">Optional</span><span class="cb-op">,</span> <span class="cb-var">List</span><br>
    <span class="cb-kw">class</span> <span class="cb-cls">ProductReview</span><span class="cb-op">(</span><span class="cb-var">BaseModel</span><span class="cb-op">):</span><br>
    &nbsp;&nbsp;<span class="cb-var">product_name</span>   <span class="cb-op">:</span> <span class="cb-var">str</span><br>
    &nbsp;&nbsp;<span class="cb-var">rating</span>         <span class="cb-op">:</span> <span class="cb-var">float</span> <span class="cb-op">=</span> <span class="cb-fn">Field</span><span class="cb-op">(</span><span class="cb-prop">ge</span><span class="cb-op">=</span><span class="cb-num">1</span><span class="cb-op">,</span> <span class="cb-prop">le</span><span class="cb-op">=</span><span class="cb-num">5</span><span class="cb-op">)</span>   <span class="cb-cmt"># 1 ≤ x ≤ 5</span><br>
    &nbsp;&nbsp;<span class="cb-var">pros</span>           <span class="cb-op">:</span> <span class="cb-var">List</span><span class="cb-op">[</span><span class="cb-var">str</span><span class="cb-op">]</span><br>
    &nbsp;&nbsp;<span class="cb-var">cons</span>           <span class="cb-op">:</span> <span class="cb-var">List</span><span class="cb-op">[</span><span class="cb-var">str</span><span class="cb-op">]</span><br>
    &nbsp;&nbsp;<span class="cb-var">would_recommend</span><span class="cb-op">:</span> <span class="cb-var">bool</span><br>
    &nbsp;&nbsp;<span class="cb-var">price_mentioned</span><span class="cb-op">:</span> <span class="cb-var">Optional</span><span class="cb-op">[</span><span class="cb-var">str</span><span class="cb-op">]</span> <span class="cb-op">=</span> <span class="cb-var">None</span><br>
    <span class="cb-cmt"># Parse and validate in one line</span><br>
    <span class="cb-var">review</span> <span class="cb-op">=</span> <span class="cb-cls">ProductReview</span><span class="cb-op">.</span><span class="cb-fn">model_validate_json</span><span class="cb-op">(</span><span class="cb-var">ai_response</span><span class="cb-op">)</span><br>
    <span class="cb-fn">print</span><span class="cb-op">(</span><span class="cb-var">review</span><span class="cb-op">.</span><span class="cb-prop">rating</span><span class="cb-op">)</span>   <span class="cb-cmt"># 4.5 — typed float, not a string</span><br>
    <span class="cb-fn">print</span><span class="cb-op">(</span><span class="cb-var">review</span><span class="cb-op">.</span><span class="cb-prop">pros</span><span class="cb-op">)</span>     <span class="cb-cmt"># ['Fast shipping', 'Good build']</span>
  </div>
</div>

<div class="highlight">

**Why Pydantic?** It raises a clear error with the field name and reason if validation fails — rather than a confusing `KeyError` three steps later. Install with `pip install pydantic`.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Use the API's `response_format`

When calling the OpenAI or Anthropic API directly, you can enforce JSON at the API level — not just in the prompt.

<div class="code-block">
  <div class="cb-bar">openai_structured.py — JSON mode via the API</div>
  <div class="cb-body">
    <span class="cb-kw">from</span> <span class="cb-var">openai</span> <span class="cb-kw">import</span> <span class="cb-var">OpenAI</span><br>
    <br>
    <span class="cb-var">client</span> <span class="cb-op">=</span> <span class="cb-fn">OpenAI</span><span class="cb-op">()</span><br>
    <br>
    <span class="cb-var">response</span> <span class="cb-op">=</span> <span class="cb-var">client</span><span class="cb-op">.</span><span class="cb-var">chat</span><span class="cb-op">.</span><span class="cb-var">completions</span><span class="cb-op">.</span><span class="cb-fn">create</span><span class="cb-op">(</span><br>
    &nbsp;&nbsp;<span class="cb-prop">model</span>           <span class="cb-op">=</span> <span class="cb-str">"gpt-4o-mini"</span><span class="cb-op">,</span><br>
    &nbsp;&nbsp;<span class="cb-hi">response_format</span> <span class="cb-op">=</span> <span class="cb-op">{</span><span class="cb-str">"type"</span><span class="cb-op">:</span> <span class="cb-str">"json_object"</span><span class="cb-op">},</span>  <span class="cb-cmt"># ← enforces JSON</span><br>
    &nbsp;&nbsp;<span class="cb-prop">messages</span>        <span class="cb-op">=</span> <span class="cb-op">[{</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-str">"role"</span><span class="cb-op">:</span> <span class="cb-str">"user"</span><span class="cb-op">,</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-str">"content"</span><span class="cb-op">:</span> <span class="cb-str">"List 3 Python frameworks as JSON array with name and use_case fields."</span><br>
    &nbsp;&nbsp;<span class="cb-op">}]</span><br>
    <span class="cb-op">)</span><br>
    <br>
    <span class="cb-kw">import</span> <span class="cb-var">json</span><br>
    <span class="cb-var">data</span> <span class="cb-op">=</span> <span class="cb-var">json</span><span class="cb-op">.</span><span class="cb-fn">loads</span><span class="cb-op">(</span><span class="cb-var">response</span><span class="cb-op">.</span><span class="cb-var">choices</span><span class="cb-op">[</span><span class="cb-num">0</span><span class="cb-op">].</span><span class="cb-var">message</span><span class="cb-op">.</span><span class="cb-prop">content</span><span class="cb-op">)</span>
  </div>
</div>

<div class="two-col" style="margin-top:12px;">
  <div class="col-card">
    <div class="label">OpenAI — json_object mode</div>
    <p style="font-size:13px; margin-top:6px;">Set <code>response_format={"type": "json_object"}</code>. The API guarantees valid JSON — the model cannot return plain text.</p>
  </div>
  <div class="col-card">
    <div class="label">Anthropic Claude</div>
    <p style="font-size:13px; margin-top:6px;">No dedicated JSON mode yet. Use prompt engineering: instruct clearly, strip fences with regex, and validate with Pydantic.</p>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Use Cases — Where This Unlocks Real Power

<div class="usecase-grid">
  <div class="usecase-card">
    <div class="uc-icon">📥</div>
    <div>
      <div class="uc-title">Extract data from documents</div>
      <div class="uc-desc">Feed invoices, contracts, or emails to an AI. Get back structured JSON with names, dates, amounts, and line items — ready for a database.</div>
      <div class="uc-tag">extraction · NER · documents</div>
    </div>
  </div>
  <div class="usecase-card">
    <div class="uc-icon">🏷️</div>
    <div>
      <div class="uc-title">Content classification</div>
      <div class="uc-desc">Classify support tickets, reviews, or articles into categories. Return <code>{"category": "billing", "urgency": "high"}</code> — pipe straight into your routing logic.</div>
      <div class="uc-tag">classification · tagging · routing</div>
    </div>
  </div>
  <div class="usecase-card">
    <div class="uc-icon">🔄</div>
    <div>
      <div class="uc-title">Data transformation</div>
      <div class="uc-desc">Convert messy unstructured notes into clean structured records. "Meeting with Sarah re: Q3 budget" → JSON with person, topic, date, and action items.</div>
      <div class="uc-tag">ETL · normalization · parsing</div>
    </div>
  </div>
  <div class="usecase-card">
    <div class="uc-icon">🤖</div>
    <div>
      <div class="uc-title">AI agent tool calls</div>
      <div class="uc-desc">Agents that decide what action to take next return structured JSON — <code>{"action": "search", "query": "..."}</code> — which your code interprets and executes.</div>
      <div class="uc-tag">agents · tool-use · function calling</div>
    </div>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**The general pattern:** unstructured text in → structured JSON out → feed to the next system. This chain is how most real-world AI integrations work.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## Common Mistakes

<div class="mistake-grid">
  <div class="mistake-card">
    <div class="mc-head">🚫 &nbsp;Forgetting "no markdown fences"</div>
    <div class="mc-body">The model wraps JSON in ```json ... ``` by default. <code>json.loads()</code> fails with a parse error and you don't know why.</div>
    <div class="mc-fix">✓ Add: "Return only JSON. No code blocks, no explanation."</div>
  </div>
  <div class="mistake-card">
    <div class="mc-head">🚫 &nbsp;No type specification</div>
    <div class="mc-body">"Rating" could come back as <code>"4.5"</code> (string) or <code>4.5</code> (number) depending on phrasing. Downstream code breaks silently.</div>
    <div class="mc-fix">✓ Specify: "rating: number between 1 and 5"</div>
  </div>
  <div class="mistake-card">
    <div class="mc-head">🚫 &nbsp;Trusting output without validation</div>
    <div class="mc-body">Models hallucinate field names, skip required keys, or add unexpected ones. Running <code>data["field"]</code> without checking causes silent data loss.</div>
    <div class="mc-fix">✓ Always validate with Pydantic or a manual check loop</div>
  </div>
  <div class="mistake-card">
    <div class="mc-head">🚫 &nbsp;Too many fields at once</div>
    <div class="mc-body">Asking for 20+ fields in one prompt increases the chance of missing or hallucinated values. The model loses track of schema constraints.</div>
    <div class="mc-fix">✓ Split into multiple focused extractions if schema is large</div>
  </div>
  <div class="mistake-card">
    <div class="mc-head">🚫 &nbsp;No fallback for parse failure</div>
    <div class="mc-body">Even with good prompting, models occasionally return malformed JSON — especially on edge-case inputs. A bare <code>json.loads()</code> crashes the whole pipeline.</div>
    <div class="mc-fix">✓ Wrap in try/except and retry once with a stricter prompt</div>
  </div>
  <div class="mistake-card">
    <div class="mc-head">🚫 &nbsp;Ambiguous field names</div>
    <div class="mc-body">"date" could mean created_at, published_at, or event_date. The model guesses, and it guesses wrong half the time.</div>
    <div class="mc-fix">✓ Use precise names: "event_date (ISO 8601 format)"</div>
  </div>
</div>

---

## Structured Output Quick Reference

<table class="cheat-table">
  <tr>
    <th>Task</th>
    <th>How to do it</th>
  </tr>
  <tr>
    <td>Request JSON in the prompt</td>
    <td>End with "Return only a JSON object. No markdown, no explanation."</td>
  </tr>
  <tr>
    <td>Define which fields to return</td>
    <td>List field name, type, and whether it's required directly in the prompt</td>
  </tr>
  <tr>
    <td>Strip markdown fences</td>
    <td class="mono">re.sub(r'```(?:json)?\s*|\s*```', '', text.strip())</td>
  </tr>
  <tr>
    <td>Parse JSON string to dict</td>
    <td class="mono">data = json.loads(ai_response)</td>
  </tr>
  <tr>
    <td>Validate fields manually</td>
    <td>Check all required keys exist; assert types match expected</td>
  </tr>
  <tr>
    <td>Validate with Pydantic</td>
    <td class="mono">MyModel.model_validate_json(ai_response)</td>
  </tr>
  <tr>
    <td>Enforce JSON via OpenAI API</td>
    <td class="mono">response_format={"type": "json_object"}</td>
  </tr>
  <tr>
    <td>Handle parse failures safely</td>
    <td>Wrap in try/except — retry once with a stricter prompt on failure</td>
  </tr>
  <tr>
    <td>Get a table as data</td>
    <td>Ask for "a JSON array of objects" — one object per row, keys as column names</td>
  </tr>
  <tr>
    <td>Convert result to CSV</td>
    <td class="mono">import csv · csv.DictWriter(f, fieldnames=data[0].keys())</td>
  </tr>
</table>

---

<!-- _class: final -->

# Structure your prompts.
# Parse the output.
# Build something real.

&nbsp;

JSON in. Python dict out. Pipeline running. Done.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*