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
  section.cover h2 { color: var(--white); border-bottom-color: #374151; }
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
  .code-block .prop { color: #93c5fd; }

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
  .terminal-body .cmt    { color: #4b5563; font-style: italic; }

  /* Raw CSV display */
  .csv-raw {
    background: #111827;
    border-radius: 8px;
    padding: 14px 20px;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #9ca3af;
    line-height: 2;
    margin: 12px 0;
  }

  .csv-raw .csv-header { color: #60a5fa; font-weight: 500; }
  .csv-raw .csv-val    { color: #e5e7eb; }
  .csv-raw .csv-hl     { color: #86efac; }

  /* Spreadsheet table mock */
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
  .sheet thead th {
    color: #93c5fd;
    padding: 8px 14px;
    text-align: left;
    font-weight: 500;
    font-size: 12px;
    letter-spacing: 0.04em;
  }

  .sheet tbody tr:nth-child(odd)  { background: #111827; }
  .sheet tbody tr:nth-child(even) { background: #1f2937; }
  .sheet tbody td { color: #e5e7eb; padding: 7px 14px; font-size: 13px; }
  .sheet tbody tr.hl-row td { background: #1e3a5f; color: #86efac; }

  /* csv vs pandas comparison */
  .compare-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 14px 0;
  }

  .compare-card {
    border-radius: 10px;
    padding: 16px 18px;
  }

  .compare-card.csv-card {
    background: #111827;
    border: 1px solid #1d4ed8;
  }

  .compare-card.pandas-card {
    background: #111827;
    border: 1px solid #166534;
  }

  .compare-card .cc-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 600;
    margin-bottom: 10px;
  }

  .compare-card.csv-card    .cc-label { color: #60a5fa; }
  .compare-card.pandas-card .cc-label { color: #86efac; }

  .compare-card .cc-body {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: #d1d5db;
    line-height: 1.9;
  }

  .compare-card .cc-desc {
    font-size: 12px;
    color: #6b7280;
    margin-top: 8px;
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

  /* bonus card grid */
  .bonus-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .bonus-card {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 14px 16px;
  }

  .bonus-card .bc-icon  { font-size: 22px; margin-bottom: 6px; }
  .bonus-card .bc-title { font-weight: 600; font-size: 14px; color: var(--text); margin-bottom: 4px; }
  .bonus-card .bc-desc  { font-size: 12px; color: var(--muted); line-height: 1.5; }
---

<!-- _class: cover -->

# Read and Write CSV Files
## with Python

&nbsp;

**The format every dataset lives in.** Learn to open, edit, and save it in code.

`csv` · `DictReader` · `DictWriter` · `pandas`

---

## What a CSV Is

CSV stands for **Comma-Separated Values** — the simplest possible data format.

<div class="csv-raw">
  <span class="csv-header">name,region,product,revenue</span><br>
  <span class="csv-val">Santos R.,Visayas,Solar Panel,48000</span><br>
  <span class="csv-val">Cruz M.,Luzon,Inverter,21000</span><br>
  <span class="csv-val">Reyes J.,Visayas,Battery,63000</span><br>
  <span class="csv-val">Lim A.,Mindanao,Solar Panel,35000</span>
</div>

That's it. Plain text, values separated by commas, one row per line. Opens in Excel, Google Sheets, Python, R — anything.

<div class="tools">
  <div class="tool-card">
    <div class="icon">📤</div>
    <div class="name">Exported everywhere</div>
    <div class="desc">Every database, CRM, analytics tool, and government dataset offers CSV export.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🪶</div>
    <div class="name">No software required</div>
    <div class="desc">It's just a text file. Open it in Notepad if you want. Nothing proprietary.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔁</div>
    <div class="name">Universal interchange</div>
    <div class="desc">The lingua franca of data. If two tools can't agree on anything else, they agree on CSV.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🐍</div>
    <div class="name">Python reads it natively</div>
    <div class="desc">The <code>csv</code> module is built into Python — no pip install needed.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## `import csv` vs `pandas` — Which to Use

<div class="compare-grid">
  <div class="compare-card csv-card">
    <div class="cc-label">📄 import csv</div>
    <div class="cc-body">
      import csv<br>
      with open("data.csv") as f:<br>
      &nbsp;&nbsp;reader = csv.DictReader(f)<br>
      &nbsp;&nbsp;for row in reader:<br>
      &nbsp;&nbsp;&nbsp;&nbsp;print(row["name"])
    </div>
    <div class="cc-desc">✦ Built-in, no install needed<br>✦ Works row by row — low memory<br>✦ Best for simple reads and writes<br>✦ Lightweight scripts and automation</div>
  </div>
  <div class="compare-card pandas-card">
    <div class="cc-label">🐼 pandas</div>
    <div class="cc-body">
      import pandas as pd<br>
      df = pd.read_csv("data.csv")<br>
      <br>
      df[df["region"] == "Visayas"]
    </div>
    <div class="cc-desc">✦ pip install pandas required<br>✦ Loads whole file into memory<br>✦ Best for filtering, sorting, analysis<br>✦ Any task with 5+ operations</div>
  </div>
</div>

<div class="highlight">

**Rule:** use `csv` for simple pipelines — read, maybe filter, write. Use `pandas` once you need to sort, group, merge, or analyse across columns.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Read a CSV in 4 Lines

`csv.DictReader` reads each row as a dictionary — column name is the key, cell value is the value.

<div class="code-block">
  <span class="kw">import</span> <span class="var">csv</span><br>
  <br>
  <span class="kw">with</span> <span class="fn">open</span>(<span class="str">"sales.csv"</span>, <span class="var">newline</span><span class="op">=</span><span class="str">""</span>) <span class="kw">as</span> <span class="var">f</span>:<br>
  &nbsp;&nbsp;<span class="var">reader</span> <span class="op">=</span> <span class="var">csv</span>.<span class="fn">DictReader</span>(<span class="var">f</span>)<br>
  &nbsp;&nbsp;<span class="kw">for</span> <span class="var">row</span> <span class="kw">in</span> <span class="var">reader</span>:<br>
  &nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">print</span>(<span class="var">row</span>[<span class="str">"name"</span>], <span class="var">row</span>[<span class="str">"revenue"</span>])
</div>

Output:

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
    <span class="title">zsh — Terminal</span>
  </div>
  <div class="terminal-body">
    <span class="prompt">~ %</span> <span class="cmd">python3 read_csv.py</span><br>
    <span class="out-g">Santos R. 48000</span><br>
    <span class="out-g">Cruz M. 21000</span><br>
    <span class="out-g">Reyes J. 63000</span><br>
    <span class="out-g">Lim A. 35000</span>
  </div>
</div>

`newline=""` prevents blank rows appearing between data rows on Windows — always include it.

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Filter and Edit Data

Loop through rows, check a condition, collect the ones you want:

<div class="code-block">
  <span class="kw">import</span> <span class="var">csv</span><br>
  <br>
  <span class="var">filtered</span> <span class="op">=</span> []<br>
  <br>
  <span class="kw">with</span> <span class="fn">open</span>(<span class="str">"sales.csv"</span>, <span class="var">newline</span><span class="op">=</span><span class="str">""</span>) <span class="kw">as</span> <span class="var">f</span>:<br>
  &nbsp;&nbsp;<span class="var">reader</span> <span class="op">=</span> <span class="var">csv</span>.<span class="fn">DictReader</span>(<span class="var">f</span>)<br>
  &nbsp;&nbsp;<span class="kw">for</span> <span class="var">row</span> <span class="kw">in</span> <span class="var">reader</span>:<br>
  &nbsp;&nbsp;&nbsp;&nbsp;<span class="cmt"># Keep only Visayas rows with revenue above 40000</span><br>
  &nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">if</span> <span class="var">row</span>[<span class="str">"region"</span>] <span class="op">==</span> <span class="str">"Visayas"</span> <span class="kw">and</span> <span class="fn">int</span>(<span class="var">row</span>[<span class="str">"revenue"</span>]) <span class="op">></span> <span class="num">40000</span>:<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="var">row</span>[<span class="str">"revenue"</span>] <span class="op">=</span> <span class="fn">int</span>(<span class="var">row</span>[<span class="str">"revenue"</span>]) <span class="op">*</span> <span class="num">1.1</span> <span class="cmt"># apply 10% increase</span><br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="var">filtered</span>.<span class="fn">append</span>(<span class="var">row</span>)
</div>

<div class="highlight">

**Note:** every value in a CSV row is a **string** by default. Use `int()` or `float()` to convert numbers before comparing or doing arithmetic.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Write Back to CSV

`csv.DictWriter` mirrors `DictReader` — pass it a list of column names and write row by row:

<div class="code-block">
  <span class="var">fieldnames</span> <span class="op">=</span> [<span class="str">"name"</span>, <span class="str">"region"</span>, <span class="str">"product"</span>, <span class="str">"revenue"</span>]<br>
  <br>
  <span class="kw">with</span> <span class="fn">open</span>(<span class="str">"output.csv"</span>, <span class="str">"w"</span>, <span class="var">newline</span><span class="op">=</span><span class="str">""</span>) <span class="kw">as</span> <span class="var">f</span>:<br>
  &nbsp;&nbsp;<span class="var">writer</span> <span class="op">=</span> <span class="var">csv</span>.<span class="fn">DictWriter</span>(<span class="var">f</span>, <span class="var">fieldnames</span><span class="op">=</span><span class="var">fieldnames</span>)<br>
  &nbsp;&nbsp;<span class="var">writer</span>.<span class="fn">writeheader</span>() <span class="cmt"># writes the column name row</span><br>
  &nbsp;&nbsp;<span class="var">writer</span>.<span class="fn">writerows</span>(<span class="var">filtered</span>) <span class="cmt"># writes all data rows at once</span><br>
  <br>
  <span class="fn">print</span>(<span class="op">f"</span><span class="str">Wrote </span><span class="op">{</span><span class="fn">len</span>(<span class="var">filtered</span>)<span class="op">}</span><span class="str"> rows to output.csv"</span>)
</div>

The result — `output.csv` — is ready to open in Excel, share via email, or feed into another script:

<table class="sheet">
  <thead><tr><th>name</th><th>region</th><th>product</th><th>revenue</th></tr></thead>
  <tbody>
    <tr class="hl-row"><td>Santos R.</td><td>Visayas</td><td>Solar Panel</td><td>52800.0</td></tr>
    <tr class="hl-row"><td>Reyes J.</td><td>Visayas</td><td>Battery</td><td>69300.0</td></tr>
  </tbody>
</table>

---

## Bonus: Open in Excel After

Add two lines to your script and it opens automatically when done:

<div class="code-block">
  <span class="kw">import</span> <span class="var">os</span><br>
  <span class="kw">import</span> <span class="var">subprocess</span><br>
  <br>
  <span class="cmt"># Mac</span><br>
  <span class="var">os</span>.<span class="fn">system</span>(<span class="str">"open output.csv"</span>)<br>
  <br>
  <span class="cmt"># Windows</span><br>
  <span class="var">os</span>.<span class="fn">system</span>(<span class="str">"start output.csv"</span>)
</div>

&nbsp;

<div class="bonus-grid">
  <div class="bonus-card">
    <div class="bc-icon">📊</div>
    <div class="bc-title">Excel opens it</div>
    <div class="bc-desc"><code>open</code> / <code>start</code> uses whatever app is registered for .csv on your machine.</div>
  </div>
  <div class="bonus-card">
    <div class="bc-icon">🔄</div>
    <div class="bc-title">Loop over files</div>
    <div class="bc-desc">Wrap the whole script in <code>os.listdir()</code> to process every CSV in a folder.</div>
  </div>
  <div class="bonus-card">
    <div class="bc-icon">🐼</div>
    <div class="bc-title">Upgrade to pandas</div>
    <div class="bc-desc">Once your logic gets complex, swap to <code>pd.read_csv()</code> — same file, far more power.</div>
  </div>
</div>

---

<!-- _class: final -->

# Read it. Edit it.
# Write it back.

&nbsp;

Every data pipeline starts with a CSV. Now you can build one in Python.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*