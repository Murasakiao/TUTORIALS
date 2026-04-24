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

  /* Python syntax tokens */
  .cb-kw     { color: #c084fc; }   /* import, def, for, if, print */
  .cb-fn     { color: #60a5fa; }   /* function names */
  .cb-str    { color: #fde68a; }   /* strings */
  .cb-num    { color: #fb923c; }   /* numbers */
  .cb-cmt    { color: #4b5563; font-style: italic; }
  .cb-var    { color: #f9fafb; }   /* variables */
  .cb-prop   { color: #34d399; }   /* dict keys / attributes */
  .cb-op     { color: #6b7280; }   /* = . () [] {} , : */
  .cb-out    { color: #9ca3af; }   /* terminal output */
  .cb-good   { color: #34d399; }
  .cb-bad    { color: #f87171; }
  .cb-prompt { color: #22c55e; }
  .cb-cmd    { color: #f9fafb; }
  .cb-tag    { color: #f87171; }
  .cb-attr   { color: #93c5fd; }

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

  /* ── API analogy diagram ── */
  .api-diagram {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0;
    margin: 20px 0;
  }

  .api-node {
    background: var(--white);
    border: 2px solid var(--border);
    border-radius: 12px;
    padding: 14px 20px;
    text-align: center;
    min-width: 130px;
  }

  .api-node .an-icon { font-size: 28px; margin-bottom: 4px; }
  .api-node .an-label {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
  }

  .api-node .an-sub {
    font-size: 11.5px;
    color: var(--muted);
    margin-top: 2px;
    font-family: 'DM Mono', monospace;
  }

  .api-node.center {
    background: var(--blue);
    border-color: var(--blue);
    min-width: 110px;
  }

  .api-node.center .an-label { color: white; }
  .api-node.center .an-sub   { color: #bfdbfe; }

  .api-arrow {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 3px;
    padding: 0 10px;
  }

  .api-arrow .ar-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--muted);
    letter-spacing: 0.04em;
    white-space: nowrap;
  }

  .api-arrow .ar-line {
    font-size: 18px;
    color: var(--blue);
    line-height: 1;
  }

  /* ── Real-world example cards ── */
  .example-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .example-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 18px;
    display: flex;
    align-items: flex-start;
    gap: 14px;
  }

  .example-card .ec-icon { font-size: 26px; flex-shrink: 0; }

  .example-card .ec-name {
    font-weight: 600;
    font-size: 14px;
    color: var(--text);
  }

  .example-card .ec-url {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    color: var(--blue);
    margin-top: 2px;
  }

  .example-card .ec-desc {
    font-size: 12.5px;
    color: var(--muted);
    margin-top: 4px;
    line-height: 1.45;
  }

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

  .jb-key    { color: #93c5fd; }
  .jb-str    { color: #fde68a; }
  .jb-num    { color: #fb923c; }
  .jb-bool   { color: #c084fc; }
  .jb-null   { color: #6b7280; }
  .jb-punct  { color: #4b5563; }
  .jb-hl     { color: #34d399; }  /* highlighted key being accessed */

  /* ── Response status cards ── */
  .status-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 10px;
    margin-top: 14px;
  }

  .status-card {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .status-card .st-code {
    padding: 8px 14px;
    font-family: 'DM Mono', monospace;
    font-size: 18px;
    font-weight: 600;
    text-align: center;
  }

  .status-card .st-label {
    padding: 4px 14px 10px;
    font-size: 12px;
    font-weight: 600;
    text-align: center;
    color: var(--text);
  }

  .status-card .st-desc {
    padding: 0 14px 12px;
    font-size: 12px;
    color: var(--muted);
    text-align: center;
    line-height: 1.5;
  }

  .status-card.ok   .st-code { background: #d1fae5; color: #065f46; }
  .status-card.warn .st-code { background: #fef3c7; color: #92400e; }
  .status-card.err  .st-code { background: #fee2e2; color: #991b1b; }

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

# Working with APIs
## in Python — Beginner Intro

&nbsp;

**Your Python script can talk to the internet.** Here's how.

`requests` · `GET` · `JSON` · `.json()` · `status_code`

---

## What an API Is

An API (Application Programming Interface) is a **structured way to ask a server for data** and get a predictable response back.

<div class="api-diagram">
  <div class="api-node">
    <div class="an-icon">🐍</div>
    <div class="an-label">Your Script</div>
    <div class="an-sub">Python</div>
  </div>
  <div class="api-arrow">
    <div class="ar-label">request</div>
    <div class="ar-line">→</div>
  </div>
  <div class="api-node center">
    <div class="an-icon" style="color:white; font-size:24px;">🔌</div>
    <div class="an-label">API</div>
    <div class="an-sub">the middleman</div>
  </div>
  <div class="api-arrow">
    <div class="ar-label">response</div>
    <div class="ar-line">←</div>
  </div>
  <div class="api-node">
    <div class="an-icon">🗄️</div>
    <div class="an-label">Server</div>
    <div class="an-sub">data lives here</div>
  </div>
</div>

<div class="tools" style="margin-top:4px;">
  <div class="tool-card">
    <div class="icon">📋</div>
    <div class="name">A menu, not a kitchen</div>
    <div class="desc">You don't access the database directly. The API gives you a defined list of things you can ask for — like a menu. You order, it delivers.</div>
  </div>
  <div class="tool-card">
    <div class="icon">📦</div>
    <div class="name">Data comes back as JSON</div>
    <div class="desc">Almost every modern API responds with JSON — a structured text format that Python can parse into a dictionary with one method call.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔑</div>
    <div class="name">Some need an API key</div>
    <div class="desc">Public APIs (weather, cat facts) are open. Others require a free key to identify who's making requests. You pass it as a parameter.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🌐</div>
    <div class="name">It's just a URL</div>
    <div class="desc">Every API endpoint is a URL. Your script visits it — the same way a browser visits a website — and reads the response.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Real-World API Examples

APIs power almost every app you use. Here are four you can query for free — no account required.

<div class="example-grid">
  <div class="example-card">
    <div class="ec-icon">🌤️</div>
    <div>
      <div class="ec-name">Open-Meteo</div>
      <div class="ec-url">api.open-meteo.com</div>
      <div class="ec-desc">Real-time and forecast weather data. Pass a latitude and longitude, get temperature, wind speed, precipitation. Completely free, no key needed.</div>
    </div>
  </div>
  <div class="example-card">
    <div class="ec-icon">😸</div>
    <div>
      <div class="ec-name">Cat Facts</div>
      <div class="ec-url">catfact.ninja/fact</div>
      <div class="ec-desc">Returns a random cat fact as JSON. The simplest possible API — one endpoint, one field in the response. Perfect first API to hit.</div>
    </div>
  </div>
  <div class="example-card">
    <div class="ec-icon">📈</div>
    <div>
      <div class="ec-name">REST Countries</div>
      <div class="ec-url">restcountries.com/v3.1</div>
      <div class="ec-desc">Data for every country — population, currency, languages, flag, region. Search by name, code, or continent. Free, no key.</div>
    </div>
  </div>
  <div class="example-card">
    <div class="ec-icon">🪐</div>
    <div>
      <div class="ec-name">NASA APIs</div>
      <div class="ec-url">api.nasa.gov</div>
      <div class="ec-desc">Astronomy Picture of the Day, Mars rover photos, near-Earth objects. Free key from NASA in 30 seconds. Great for portfolio projects.</div>
    </div>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**Start with Cat Facts or REST Countries** — no signup, instant response, easy JSON structure. Once those work, move to weather or NASA.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Install the `requests` Library

Python doesn't include HTTP requests in the standard library. `requests` is the community standard — clean, readable, and handles everything for you.

<div class="code-block">
  <div class="cb-bar">terminal</div>
  <div class="cb-body">
    <span class="cb-prompt">~</span> <span class="cb-cmd">pip install requests</span><br>
    <span class="cb-out">Successfully installed requests-2.31.0</span>
  </div>
</div>

<div class="two-col">
  <div class="col-card">
    <div class="label">What it does for you</div>
    <p style="font-size:13.5px; margin-top:8px;">Handles the full HTTP lifecycle — opening a connection, sending headers, reading the response, and closing cleanly. You write one line instead of twenty.</p>
  </div>
  <div class="col-card">
    <div class="label">Verify the install</div>
    <div class="code-block" style="margin-top:8px;">
      <div class="cb-body" style="padding:10px 14px; line-height:1.9; font-size:12px;">
        <span class="cb-kw">import</span> <span class="cb-var">requests</span><br>
        <span class="cb-fn">print</span><span class="cb-op">(</span><span class="cb-var">requests</span><span class="cb-op">.</span><span class="cb-var">__version__</span><span class="cb-op">)</span><br>
        <span class="cb-out"># 2.31.0</span>
      </div>
    </div>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**Using a virtual environment?** Activate it first — `source venv/bin/activate` (Mac) or `venv\Scripts\activate` (Windows) — then run `pip install requests` inside it.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Make Your First GET Request

A GET request fetches data from a URL. It's the most common API operation.

<div class="code-block">
  <div class="cb-bar">api_test.py</div>
  <div class="cb-body">
    <span class="cb-kw">import</span> <span class="cb-var">requests</span><br>
    <br>
    <span class="cb-cmt"># The URL is the API endpoint — just a web address</span><br>
    <span class="cb-var">url</span> <span class="cb-op">=</span> <span class="cb-str">"https://catfact.ninja/fact"</span><br>
    <br>
    <span class="cb-cmt"># requests.get() sends the request and waits for the response</span><br>
    <span class="cb-var">response</span> <span class="cb-op">=</span> <span class="cb-var">requests</span><span class="cb-op">.</span><span class="cb-fn">get</span><span class="cb-op">(</span><span class="cb-var">url</span><span class="cb-op">)</span><br>
    <br>
    <span class="cb-cmt"># Always check the status code first</span><br>
    <span class="cb-fn">print</span><span class="cb-op">(</span><span class="cb-var">response</span><span class="cb-op">.</span><span class="cb-prop">status_code</span><span class="cb-op">)</span>  <span class="cb-cmt"># 200 means success</span><br>
    <span class="cb-fn">print</span><span class="cb-op">(</span><span class="cb-var">response</span><span class="cb-op">.</span><span class="cb-prop">text</span><span class="cb-op">)</span>         <span class="cb-cmt"># raw response as a string</span>
  </div>
</div>

<div class="status-grid">
  <div class="status-card ok">
    <div class="st-code">200</div>
    <div class="st-label">OK</div>
    <div class="st-desc">Request succeeded. Data is in the response body.</div>
  </div>
  <div class="status-card warn">
    <div class="st-code">404</div>
    <div class="st-label">Not Found</div>
    <div class="st-desc">The endpoint URL doesn't exist. Check for typos.</div>
  </div>
  <div class="status-card err">
    <div class="st-code">401</div>
    <div class="st-label">Unauthorized</div>
    <div class="st-desc">API key missing or invalid. Check your credentials.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Parse the JSON Response

`.text` gives you a raw string. `.json()` turns it into a Python dictionary you can actually work with.

<div class="two-col">
  <div class="col-card">
    <div class="label">What the API sends back</div>
    <div class="json-block" style="margin-top:8px;">
      <div class="jb-body" style="padding:10px 16px; line-height:1.9; font-size:12px;">
        <span class="jb-punct">{</span><br>
        &nbsp;&nbsp;<span class="jb-hl">"fact"</span><span class="jb-punct">:</span> <span class="jb-str">"Cats sleep 70% of their lives"</span><span class="jb-punct">,</span><br>
        &nbsp;&nbsp;<span class="jb-key">"length"</span><span class="jb-punct">:</span> <span class="jb-num">32</span><br>
        <span class="jb-punct">}</span>
      </div>
    </div>
  </div>
  <div class="col-card">
    <div class="label">What Python sees after .json()</div>
    <div class="code-block" style="margin-top:8px;">
      <div class="cb-body" style="padding:10px 14px; line-height:1.9; font-size:12px;">
        <span class="cb-op">{</span><br>
        &nbsp;&nbsp;<span class="cb-str">"fact"</span><span class="cb-op">:</span> <span class="cb-str">"Cats sleep 70%..."</span><span class="cb-op">,</span><br>
        &nbsp;&nbsp;<span class="cb-str">"length"</span><span class="cb-op">:</span> <span class="cb-num">32</span><br>
        <span class="cb-op">}</span><br>
        <span class="cb-cmt"># A regular Python dict — use [] or .get()</span>
      </div>
    </div>
  </div>
</div>

<div class="code-block">
  <div class="cb-bar">api_test.py — parsing the response</div>
  <div class="cb-body">
    <span class="cb-var">response</span> <span class="cb-op">=</span> <span class="cb-var">requests</span><span class="cb-op">.</span><span class="cb-fn">get</span><span class="cb-op">(</span><span class="cb-str">"https://catfact.ninja/fact"</span><span class="cb-op">)</span><br>
    <span class="cb-cmt"># .json() deserialises the response into a Python dict</span><br>
    <span class="cb-var">data</span> <span class="cb-op">=</span> <span class="cb-var">response</span><span class="cb-op">.</span><span class="cb-fn">json</span><span class="cb-op">()</span><br>
    <span class="cb-cmt"># Access keys exactly like a regular dictionary</span><br>
    <span class="cb-fn">print</span><span class="cb-op">(</span><span class="cb-var">data</span><span class="cb-op">[</span><span class="cb-str">"fact"</span><span class="cb-op">])</span><br>
    <span class="cb-out">Cats sleep 70% of their lives.</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 04</div>

## Print Useful Data — Full Working Script

Putting it all together with error handling and query parameters.

<div class="code-block">
  <div class="cb-bar">weather.py — Open-Meteo API, no key needed</div>
  <div class="cb-body">
    <span class="cb-kw">import</span> <span class="cb-var">requests</span><br>
    <span class="cb-var">url</span> <span class="cb-op">=</span> <span class="cb-str">"https://api.open-meteo.com/v1/forecast"</span><br>
    <span class="cb-cmt"># Query parameters — sent as ?key=value in the URL</span><br>
    <span class="cb-var">params</span> <span class="cb-op">=</span> <span class="cb-op">{</span><br>
    &nbsp;&nbsp;<span class="cb-str">"latitude"</span><span class="cb-op">:</span>  <span class="cb-num">14.5995</span><span class="cb-op">,</span>   <span class="cb-cmt"># Manila, Philippines</span><br>
    &nbsp;&nbsp;<span class="cb-str">"longitude"</span><span class="cb-op">:</span> <span class="cb-num">120.9842</span><span class="cb-op">,</span><br>
    &nbsp;&nbsp;<span class="cb-str">"current"</span><span class="cb-op">:</span>   <span class="cb-str">"temperature_2m,wind_speed_10m"</span><br>
    <span class="cb-op">}</span><br>
    <span class="cb-var">response</span> <span class="cb-op">=</span> <span class="cb-var">requests</span><span class="cb-op">.</span><span class="cb-fn">get</span><span class="cb-op">(</span><span class="cb-var">url</span><span class="cb-op">,</span> <span class="cb-var">params</span><span class="cb-op">=</span><span class="cb-var">params</span><span class="cb-op">)</span><br>
    <span class="cb-kw">if</span> <span class="cb-var">response</span><span class="cb-op">.</span><span class="cb-prop">status_code</span> <span class="cb-op">==</span> <span class="cb-num">200</span><span class="cb-op">:</span><br>
    &nbsp;&nbsp;<span class="cb-var">data</span>    <span class="cb-op">=</span> <span class="cb-var">response</span><span class="cb-op">.</span><span class="cb-fn">json</span><span class="cb-op">()</span><br>
    &nbsp;&nbsp;<span class="cb-var">current</span> <span class="cb-op">=</span> <span class="cb-var">data</span><span class="cb-op">[</span><span class="cb-str">"current"</span><span class="cb-op">]</span><br>
    &nbsp;&nbsp;<span class="cb-fn">print</span><span class="cb-op">(</span><span class="cb-str">f"Temp:  </span><span class="cb-op">{</span><span class="cb-var">current</span><span class="cb-op">[</span><span class="cb-str">'temperature_2m'</span><span class="cb-op">]}</span><span class="cb-str">°C"</span><span class="cb-op">)</span><br>
    &nbsp;&nbsp;<span class="cb-fn">print</span><span class="cb-op">(</span><span class="cb-str">f"Wind:  </span><span class="cb-op">{</span><span class="cb-var">current</span><span class="cb-op">[</span><span class="cb-str">'wind_speed_10m'</span><span class="cb-op">]}</span><span class="cb-str"> km/h"</span><span class="cb-op">)</span><br>
    <span class="cb-kw">else</span><span class="cb-op">:</span><br>
    &nbsp;&nbsp;<span class="cb-fn">print</span><span class="cb-op">(</span><span class="cb-str">f"Error: </span><span class="cb-op">{</span><span class="cb-var">response</span><span class="cb-op">.</span><span class="cb-prop">status_code</span><span class="cb-op">}</span><span class="cb-str">"</span><span class="cb-op">)</span>
  </div>
</div>

---

## Python + APIs Quick Reference

<table class="cheat-table">
  <tr>
    <th>Task</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>Install requests</td>
    <td class="mono">pip install requests</td>
  </tr>
  <tr>
    <td>Import the library</td>
    <td class="mono">import requests</td>
  </tr>
  <tr>
    <td>Make a GET request</td>
    <td class="mono">response = requests.get(url)</td>
  </tr>
  <tr>
    <td>Check if it succeeded</td>
    <td class="mono">response.status_code == 200</td>
  </tr>
  <tr>
    <td>Read raw response text</td>
    <td class="mono">response.text</td>
  </tr>
  <tr>
    <td>Parse JSON into a dict</td>
    <td class="mono">data = response.json()</td>
  </tr>
  <tr>
    <td>Access a JSON field</td>
    <td class="mono">data["key"]  or  data.get("key")</td>
  </tr>
  <tr>
    <td>Pass query parameters</td>
    <td class="mono">requests.get(url, params={"k": "v"})</td>
  </tr>
  <tr>
    <td>Pass an API key as header</td>
    <td class="mono">requests.get(url, headers={"Authorization": "Bearer KEY"})</td>
  </tr>
  <tr>
    <td>Loop through a list in JSON</td>
    <td class="mono">for item in data["results"]: print(item)</td>
  </tr>
</table>

---

<!-- _class: final -->

# Your script can now
# talk to the world.

&nbsp;

Install requests. GET the URL. Parse the JSON. Print the data.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*