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

  .highlight.warn {
    background: #fefce8;
    border-color: #fde68a;
  }

  .highlight.good {
    background: #f0fdf4;
    border-color: #bbf7d0;
  }

  .highlight.danger {
    background: #fff1f2;
    border-color: #fecdd3;
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

  .warn-badge {
    display: inline-block;
    background: #f59e0b;
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
    padding: 16px 22px;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #e5e7eb;
    line-height: 2;
    margin: 12px 0;
  }

  .code-block .kw   { color: #c4b5fd; }
  .code-block .fn   { color: #60a5fa; }
  .code-block .str  { color: #86efac; }
  .code-block .var  { color: #f9fafb; }
  .code-block .num  { color: #fde68a; }
  .code-block .op   { color: #f9a8d4; }
  .code-block .cmt  { color: #4b5563; font-style: italic; }
  .code-block .tag  { color: #60a5fa; }
  .code-block .attr { color: #86efac; }

  /* Terminal */
  .terminal {
    background: #111827;
    border-radius: 10px;
    overflow: hidden;
    margin: 12px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .terminal-bar {
    background: #1f2937;
    padding: 9px 16px;
    display: flex;
    align-items: center;
    gap: 7px;
  }

  .terminal-bar .dot { width: 12px; height: 12px; border-radius: 50%; display: inline-block; }
  .terminal-bar .dot.red    { background: #ef4444; }
  .terminal-bar .dot.yellow { background: #f59e0b; }
  .terminal-bar .dot.green  { background: #22c55e; }
  .terminal-bar .title { font-size: 12px; color: #6b7280; margin-left: 8px; }

  .terminal-body { padding: 14px 20px; line-height: 2; }
  .terminal-body .prompt { color: #22c55e; }
  .terminal-body .cmd    { color: #f9fafb; }
  .terminal-body .out    { color: #9ca3af; }
  .terminal-body .out-g  { color: #86efac; }
  .terminal-body .out-b  { color: #60a5fa; }
  .terminal-body .cmt    { color: #4b5563; font-style: italic; }

  /* HTML source mock */
  .html-source {
    background: #0d1117;
    border-radius: 8px;
    padding: 16px 20px;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    line-height: 2;
    margin: 12px 0;
    border: 1px solid #30363d;
  }

  .html-source .ht  { color: #60a5fa; }   /* tag          */
  .html-source .ha  { color: #86efac; }   /* attribute    */
  .html-source .hv  { color: #fde68a; }   /* attr value   */
  .html-source .hc  { color: #e5e7eb; }   /* content text */
  .html-source .hcm { color: #4b5563; font-style: italic; } /* comment */

  /* DevTools walkthrough */
  .devtools-steps {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .dt-step {
    background: #111827;
    border-radius: 8px;
    padding: 14px 16px;
  }

  .dt-step .dt-num    { font-family: 'DM Mono', monospace; font-size: 11px; color: #6b7280; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 6px; }
  .dt-step .dt-action { font-size: 14px; font-weight: 600; color: #f0f6fc; margin-bottom: 4px; }
  .dt-step .dt-key    { font-family: 'DM Mono', monospace; font-size: 12px; color: #60a5fa; margin-bottom: 4px; }
  .dt-step .dt-desc   { font-size: 12px; color: #6b7280; line-height: 1.5; }

  /* ok/bad two-col */
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

  /* method reference grid */
  .method-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin: 14px 0;
  }

  .method-card {
    background: #111827;
    border-radius: 8px;
    padding: 13px 16px;
    display: flex;
    gap: 12px;
    align-items: flex-start;
  }

  .method-card .mc-fn {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #60a5fa;
    font-weight: 600;
    min-width: 100px;
    flex-shrink: 0;
    padding-top: 1px;
  }

  .method-card .mc-body .mc-title { font-size: 14px; font-weight: 600; color: #f0f6fc; margin-bottom: 2px; }
  .method-card .mc-body .mc-desc  { font-size: 12px; color: #6b7280; line-height: 1.5; }

  /* sheet */
  .sheet {
    border-collapse: collapse;
    width: 100%;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    margin: 12px 0;
    border-radius: 8px;
    overflow: hidden;
  }

  .sheet thead tr { background: #1e3a5f; }
  .sheet thead th { color: #93c5fd; padding: 8px 14px; text-align: left; font-weight: 500; font-size: 12px; }
  .sheet tbody tr:nth-child(odd)  { background: #111827; }
  .sheet tbody tr:nth-child(even) { background: #1f2937; }
  .sheet tbody td { color: #e5e7eb; padding: 7px 14px; font-size: 13px; }
---

<!-- _class: cover -->

# Scrape a Webpage with Python
## requests + BeautifulSoup

&nbsp;

**Pull data off any public page** — and save it as a CSV in under 50 lines.

`requests` · `BeautifulSoup` · `find_all` · `csv`

---

<div class="warn-badge">⚠️ BEFORE YOU START</div>

## What Web Scraping Is — and When It's Okay

Web scraping is fetching a webpage and extracting structured data from its HTML.

<div class="two-col">
  <div class="col-card">
    <div class="label">✅ Generally fine</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">
      ✦ Public pages with no login required<br>
      ✦ Data not available via an official API<br>
      ✦ Personal research and learning<br>
      ✦ Sites that don't block bots in <code>robots.txt</code><br>
      ✦ Scraping slowly — not hammering servers
    </p>
  </div>
  <div class="col-card">
    <div class="label">❌ Don't do this</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">
      ✦ Pages behind login walls<br>
      ✦ Sites that explicitly ban scraping in their ToS<br>
      ✦ Scraping at high speed — it's a DoS attack<br>
      ✦ Republishing scraped content as your own<br>
      ✦ Personal or private user data
    </p>
  </div>
</div>

<div class="highlight warn">

Always check `robots.txt` first: `https://example.com/robots.txt`. If scraping is disallowed — don't.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Two Libraries — One Job Each

<div class="tools">
  <div class="tool-card">
    <div class="icon">🌐</div>
    <div class="name">requests</div>
    <div class="desc">Fetches the raw HTML of a page. Like a browser downloading the source — no rendering, just text.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🍲</div>
    <div class="name">BeautifulSoup</div>
    <div class="desc">Parses the raw HTML and lets you search it by tag, class, id, or CSS selector.</div>
  </div>
  <div class="tool-card">
    <div class="icon">📦</div>
    <div class="name">Install both</div>
    <div class="desc"><code>pip3 install requests beautifulsoup4</code> — one command, both libraries.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔗</div>
    <div class="name">They work together</div>
    <div class="desc"><code>requests</code> gets the page → <code>BeautifulSoup</code> reads it. You always use them as a pair.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Inspect the Page First — DevTools

Before writing a line of Python, find the HTML element that holds the data you want.

<div class="devtools-steps">
  <div class="dt-step">
    <div class="dt-num">01 — Open</div>
    <div class="dt-action">Open DevTools</div>
    <div class="dt-key">F12 &nbsp;/&nbsp; ⌘ + Opt + I</div>
    <div class="dt-desc">Opens the inspector panel on any page in Chrome or Firefox.</div>
  </div>
  <div class="dt-step">
    <div class="dt-num">02 — Pick</div>
    <div class="dt-action">Inspect Element</div>
    <div class="dt-key">Right-click → Inspect</div>
    <div class="dt-desc">Click the element you want — its HTML tag and class name highlight in the panel.</div>
  </div>
  <div class="dt-step">
    <div class="dt-num">03 — Note</div>
    <div class="dt-action">Copy the selector</div>
    <div class="dt-key">tag + class name</div>
    <div class="dt-desc">Note the tag (<code>h2</code>, <code>li</code>, <code>div</code>) and its <code>class</code> or <code>id</code> — you'll use both in your script.</div>
  </div>
</div>

What you're looking for in the HTML panel:

<div class="html-source">
  <span class="ht">&lt;ul</span> <span class="ha">class</span>=<span class="hv">"product-list"</span><span class="ht">&gt;</span><br>
  &nbsp;&nbsp;<span class="ht">&lt;li</span> <span class="ha">class</span>=<span class="hv">"product-item"</span><span class="ht">&gt;</span><br>
  &nbsp;&nbsp;&nbsp;&nbsp;<span class="ht">&lt;h2</span> <span class="ha">class</span>=<span class="hv">"product-name"</span><span class="ht">&gt;</span><span class="hc">Solar Panel 400W</span><span class="ht">&lt;/h2&gt;</span><br>
  &nbsp;&nbsp;&nbsp;&nbsp;<span class="ht">&lt;span</span> <span class="ha">class</span>=<span class="hv">"price"</span><span class="ht">&gt;</span><span class="hc">₱12,500</span><span class="ht">&lt;/span&gt;</span><br>
  &nbsp;&nbsp;<span class="ht">&lt;/li&gt;</span><br>
  <span class="ht">&lt;/ul&gt;</span>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Fetch the Page

<div class="code-block">
  <span class="kw">import</span> <span class="var">requests</span><br>
  <span class="kw">from</span> <span class="var">bs4</span> <span class="kw">import</span> <span class="var">BeautifulSoup</span><br>
  <br>
  <span class="var">url</span> <span class="op">=</span> <span class="str">"https://example.com/products"</span><br>
  <span class="var">response</span> <span class="op">=</span> <span class="var">requests</span>.<span class="fn">get</span>(<span class="var">url</span>)<br>
  <br>
  <span class="cmt"># Check it worked — 200 means OK</span><br>
  <span class="fn">print</span>(<span class="var">response</span>.<span class="var">status_code</span>)<br>
  <br>
  <span class="cmt"># Parse the HTML</span><br>
  <span class="var">soup</span> <span class="op">=</span> <span class="fn">BeautifulSoup</span>(<span class="var">response</span>.<span class="var">text</span>, <span class="str">"html.parser"</span>)
</div>

<div class="two-col">
  <div class="col-card">
    <div class="label">✅ Status 200</div>
    <p style="font-size:14px; margin-top:6px;">Page fetched successfully. Continue to the next step.</p>
  </div>
  <div class="col-card">
    <div class="label">⚠️ Status 403 / 429</div>
    <p style="font-size:14px; margin-top:6px;">Server blocked the request. Add a <code>User-Agent</code> header or slow down your requests with <code>time.sleep()</code>.</p>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Find Elements and Extract Data

BeautifulSoup gives you four methods to locate elements:

<div class="method-grid">
  <div class="method-card">
    <div class="mc-fn">find()</div>
    <div class="mc-body">
      <div class="mc-title">First match only</div>
      <div class="mc-desc"><code>soup.find("h1")</code> — returns one element or None.</div>
    </div>
  </div>
  <div class="method-card">
    <div class="mc-fn">find_all()</div>
    <div class="mc-body">
      <div class="mc-title">All matches</div>
      <div class="mc-desc"><code>soup.find_all("li")</code> — returns a list. Loop over it.</div>
    </div>
  </div>
  <div class="method-card">
    <div class="mc-fn">.get_text()</div>
    <div class="mc-body">
      <div class="mc-title">Extract inner text</div>
      <div class="mc-desc">Strips all HTML tags and returns the visible text content.</div>
    </div>
  </div>
  <div class="method-card">
    <div class="mc-fn">.get("href")</div>
    <div class="mc-body">
      <div class="mc-title">Extract an attribute</div>
      <div class="mc-desc"><code>tag.get("href")</code> pulls the URL from a link. Works for any attribute.</div>
    </div>
  </div>
</div>

<div class="code-block">
  <span class="var">items</span> <span class="op">=</span> <span class="var">soup</span>.<span class="fn">find_all</span>(<span class="str">"li"</span>, <span class="var">class_</span><span class="op">=</span><span class="str">"product-item"</span>)<br>
  <span class="kw">for</span> <span class="var">item</span> <span class="kw">in</span> <span class="var">items</span>:<br>
  &nbsp;&nbsp;<span class="var">name</span>  <span class="op">=</span> <span class="var">item</span>.<span class="fn">find</span>(<span class="str">"h2"</span>).<span class="fn">get_text</span>(<span class="var">strip</span><span class="op">=</span><span class="kw">True</span>)<br>
  &nbsp;&nbsp;<span class="var">price</span> <span class="op">=</span> <span class="var">item</span>.<span class="fn">find</span>(<span class="str">"span"</span>, <span class="var">class_</span><span class="op">=</span><span class="str">"price"</span>).<span class="fn">get_text</span>(<span class="var">strip</span><span class="op">=</span><span class="kw">True</span>)<br>
  &nbsp;&nbsp;<span class="fn">print</span>(<span class="var">name</span>, <span class="var">price</span>)
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 04</div>

## Save to CSV

Collect your results into a list, then write with `csv.DictWriter`:

<div class="code-block">
  <span class="kw">import</span> <span class="var">csv</span><br>
  <br>
  <span class="var">results</span> <span class="op">=</span> []<br>
  <span class="var">items</span> <span class="op">=</span> <span class="var">soup</span>.<span class="fn">find_all</span>(<span class="str">"li"</span>, <span class="var">class_</span><span class="op">=</span><span class="str">"product-item"</span>)<br>
  <br>
  <span class="kw">for</span> <span class="var">item</span> <span class="kw">in</span> <span class="var">items</span>:<br>
  &nbsp;&nbsp;<span class="var">results</span>.<span class="fn">append</span>({<br>
  &nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"name"</span>:  <span class="var">item</span>.<span class="fn">find</span>(<span class="str">"h2"</span>).<span class="fn">get_text</span>(<span class="var">strip</span><span class="op">=</span><span class="kw">True</span>),<br>
  &nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"price"</span>: <span class="var">item</span>.<span class="fn">find</span>(<span class="str">"span"</span>, <span class="var">class_</span><span class="op">=</span><span class="str">"price"</span>).<span class="fn">get_text</span>(<span class="var">strip</span><span class="op">=</span><span class="kw">True</span>)<br>
  &nbsp;&nbsp;})<br>
  <br>
  <span class="kw">with</span> <span class="fn">open</span>(<span class="str">"products.csv"</span>, <span class="str">"w"</span>, <span class="var">newline</span><span class="op">=</span><span class="str">""</span>) <span class="kw">as</span> <span class="var">f</span>:<br>
  &nbsp;&nbsp;<span class="var">writer</span> <span class="op">=</span> <span class="var">csv</span>.<span class="fn">DictWriter</span>(<span class="var">f</span>, <span class="var">fieldnames</span><span class="op">=</span>[<span class="str">"name"</span>, <span class="str">"price"</span>])<br>
  &nbsp;&nbsp;<span class="var">writer</span>.<span class="fn">writeheader</span>()<br>
  &nbsp;&nbsp;<span class="var">writer</span>.<span class="fn">writerows</span>(<span class="var">results</span>)<br>
  <br>
  <span class="fn">print</span>(<span class="op">f"</span><span class="str">Saved </span><span class="op">{</span><span class="fn">len</span>(<span class="var">results</span>)<span class="op">}</span><span class="str"> rows to products.csv"</span>)
</div>

---

## The Full Output

Run it and you get a clean CSV — ready to open in Excel, load into pandas, or feed into another script:

<table class="sheet">
  <thead><tr><th>name</th><th>price</th></tr></thead>
  <tbody>
    <tr><td>Solar Panel 400W</td><td>₱12,500</td></tr>
    <tr><td>Lithium Battery 100Ah</td><td>₱8,200</td></tr>
    <tr><td>MPPT Charge Controller</td><td>₱3,750</td></tr>
    <tr><td>Grid-Tie Inverter 3kW</td><td>₱21,000</td></tr>
    <tr><td>Mounting Rail Kit</td><td>₱1,800</td></tr>
  </tbody>
</table>

<div class="highlight good">

**What to do next:** load `products.csv` into pandas for analysis, add `time.sleep(1)` between page requests to be polite, or loop over multiple pages by incrementing a `?page=` URL parameter.

</div>

---

<!-- _class: final -->

# Fetch it. Parse it.
# Save it.

&nbsp;

Three imports, one loop, fifty lines — and you have a scraper that runs forever.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*