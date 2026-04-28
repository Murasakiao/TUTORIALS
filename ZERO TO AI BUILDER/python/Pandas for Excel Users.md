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
  .terminal-body .prompt  { color: #22c55e; }
  .terminal-body .cmd     { color: #f9fafb; }
  .terminal-body .out     { color: #9ca3af; }
  .terminal-body .out-g   { color: #86efac; }
  .terminal-body .repl    { color: #c4b5fd; }
  .terminal-body .cmt     { color: #4b5563; font-style: italic; }

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

  .code-block .kw  { color: #c4b5fd; }
  .code-block .fn  { color: #60a5fa; }
  .code-block .str { color: #86efac; }
  .code-block .var { color: #f9fafb; }
  .code-block .num { color: #fde68a; }
  .code-block .op  { color: #f9a8d4; }
  .code-block .cmt { color: #4b5563; font-style: italic; }

  /* Spreadsheet table mock */
  .sheet {
    border-collapse: collapse;
    width: 100%;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    margin: 14px 0;
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

  .sheet tbody td {
    color: #e5e7eb;
    padding: 7px 14px;
    font-size: 13px;
  }

  .sheet tbody tr.highlight-row td { background: #1e3a5f; color: #86efac; }

  /* Excel vs pandas comparison */
  .compare-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 16px 0;
  }

  .compare-card {
    border-radius: 10px;
    padding: 16px 18px;
  }

  .compare-card.excel {
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
  }

  .compare-card.pandas {
    background: #111827;
    border: 1px solid #1d4ed8;
  }

  .compare-card .cc-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 600;
    margin-bottom: 10px;
  }

  .compare-card.excel  .cc-label { color: #166534; }
  .compare-card.pandas .cc-label { color: #60a5fa; }

  .compare-card.excel  .cc-body { font-size: 14px; color: #374151; line-height: 1.7; }
  .compare-card.pandas .cc-body { font-family: 'DM Mono', monospace; font-size: 13px; color: #86efac; line-height: 2; }

  /* Why-better card grid */
  .why-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .why-card {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 14px 16px;
  }

  .why-card .why-icon  { font-size: 22px; margin-bottom: 6px; }
  .why-card .why-title { font-weight: 600; font-size: 14px; color: var(--text); margin-bottom: 4px; }
  .why-card .why-desc  { font-size: 12px; color: var(--muted); line-height: 1.5; }

  /* Two-column */
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

# pandas in 5 Minutes
## Python for Excel Users

&nbsp;

**If you know Excel, you already know the concepts.** The syntax is just different.

`DataFrame` · `filter` · `sort` · `groupby` · `to_csv`

---

## pandas as "Excel in Code"

Every Excel operation has a pandas equivalent — and pandas runs on any file size, any time.

<div class="compare-grid">
  <div class="compare-card excel">
    <div class="cc-label">📊 Excel</div>
    <div class="cc-body">
      Open file → click column header → Data → Filter → tick boxes → sort arrow → File → Save As<br><br>
      Repeat manually for every new file.
    </div>
  </div>
  <div class="compare-card pandas">
    <div class="cc-label">🐼 pandas</div>
    <div class="cc-body">
      df = pd.read_csv("data.csv")<br>
      df = df[df["Region"] == "Visayas"]<br>
      df = df.sort_values("Revenue")<br>
      df.to_csv("output.csv")<br><br>
      <span style="color:#6b7280"># runs on any file, any time</span>
    </div>
  </div>
</div>

Same result. But the code runs in under a second — on 10 rows or 10 million.

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Install pandas and Load a CSV

First, install pandas into your virtual environment:

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
    <span class="title">zsh — Terminal</span>
  </div>
  <div class="terminal-body">
    <span class="prompt">~ %</span> <span class="cmd">pip3 install pandas</span><br>
    <span class="out-g">Successfully installed pandas-2.x.x</span>
  </div>
</div>

Then load any CSV file in three lines:

<div class="code-block">
  <span class="kw">import</span> <span class="var">pandas</span> <span class="kw">as</span> <span class="var">pd</span><br>
  <br>
  <span class="var">df</span> <span class="op">=</span> <span class="var">pd</span>.<span class="fn">read_csv</span>(<span class="str">"sales.csv"</span>)<br>
  <span class="fn">print</span>(<span class="var">df</span>.<span class="fn">head</span>()) <span class="cmt"># show first 5 rows</span>
</div>

`df` is short for **DataFrame** — pandas' name for a table. Think of it as a spreadsheet that lives in memory, with rows and columns you can manipulate with code.

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Explore the Data

Before touching anything, get a feel for what you have:

<div class="code-block">
  <span class="fn">print</span>(<span class="var">df</span>.<span class="fn">shape</span>)     <span class="cmt"># (rows, columns) — e.g. (1500, 6)</span><br>
  <span class="fn">print</span>(<span class="var">df</span>.<span class="fn">columns</span>)   <span class="cmt"># list of column names</span><br>
  <span class="fn">print</span>(<span class="var">df</span>.<span class="fn">dtypes</span>)    <span class="cmt"># data type of each column</span><br>
  <span class="fn">print</span>(<span class="var">df</span>.<span class="fn">describe</span>()) <span class="cmt"># min, max, mean, count per column</span>
</div>

This is what the loaded data looks like as a DataFrame:

<table class="sheet">
  <thead>
    <tr>
      <th>#</th><th>Name</th><th>Region</th><th>Product</th><th>Revenue</th><th>Month</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>0</td><td>Santos, R.</td><td>Visayas</td><td>Solar Panel</td><td>48000</td><td>Jan</td></tr>
    <tr><td>1</td><td>Cruz, M.</td><td>Luzon</td><td>Inverter</td><td>21000</td><td>Jan</td></tr>
    <tr><td>2</td><td>Reyes, J.</td><td>Visayas</td><td>Battery</td><td>63000</td><td>Feb</td></tr>
    <tr><td>3</td><td>Lim, A.</td><td>Mindanao</td><td>Solar Panel</td><td>35000</td><td>Feb</td></tr>
    <tr><td>4</td><td>Garcia, P.</td><td>Luzon</td><td>Inverter</td><td>17000</td><td>Mar</td></tr>
  </tbody>
</table>

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Filter Rows

Select only the rows you need — like Excel's filter, but in one line:

<div class="code-block">
  <span class="cmt"># Keep only rows where Region is "Visayas"</span><br>
  <span class="var">visayas</span> <span class="op">=</span> <span class="var">df</span>[<span class="var">df</span>[<span class="str">"Region"</span>] <span class="op">==</span> <span class="str">"Visayas"</span>]<br>
  <br>
  <span class="cmt"># Multiple conditions — use & for AND, | for OR</span><br>
  <span class="var">filtered</span> <span class="op">=</span> <span class="var">df</span>[(<span class="var">df</span>[<span class="str">"Region"</span>] <span class="op">==</span> <span class="str">"Visayas"</span>) <span class="op">&</span> (<span class="var">df</span>[<span class="str">"Revenue"</span>] <span class="op">></span> <span class="num">40000</span>)]
</div>

The matching rows highlighted:

<table class="sheet">
  <thead>
    <tr><th>#</th><th>Name</th><th>Region</th><th>Product</th><th>Revenue</th><th>Month</th></tr>
  </thead>
  <tbody>
    <tr class="highlight-row"><td>0</td><td>Santos, R.</td><td>Visayas</td><td>Solar Panel</td><td>48000</td><td>Jan</td></tr>
    <tr><td>1</td><td>Cruz, M.</td><td>Luzon</td><td>Inverter</td><td>21000</td><td>Jan</td></tr>
    <tr class="highlight-row"><td>2</td><td>Reyes, J.</td><td>Visayas</td><td>Battery</td><td>63000</td><td>Feb</td></tr>
    <tr><td>3</td><td>Lim, A.</td><td>Mindanao</td><td>Solar Panel</td><td>35000</td><td>Feb</td></tr>
  </tbody>
</table>

---

<!-- _class: step -->

<div class="step-badge">STEP 04</div>

## Sort and Summarise

Sort rows and collapse data into summaries — like Excel's sort and pivot table:

<div class="code-block">
  <span class="cmt"># Sort by Revenue, highest first</span><br>
  <span class="var">df_sorted</span> <span class="op">=</span> <span class="var">df</span>.<span class="fn">sort_values</span>(<span class="str">"Revenue"</span>, <span class="var">ascending</span><span class="op">=</span><span class="kw">False</span>)<br>
  <br>
  <span class="cmt"># Total revenue per Region — like a pivot table</span><br>
  <span class="var">summary</span> <span class="op">=</span> <span class="var">df</span>.<span class="fn">groupby</span>(<span class="str">"Region"</span>)[<span class="str">"Revenue"</span>].<span class="fn">sum</span>()<br>
  <span class="fn">print</span>(<span class="var">summary</span>)
</div>

<div class="compare-grid">
  <div class="compare-card excel">
    <div class="cc-label">📊 Excel equivalent</div>
    <div class="cc-body">Data → Sort → Column: Revenue → Order: Largest to Smallest → OK<br><br>Insert → PivotTable → drag Region to Rows, Revenue to Values → Sum</div>
  </div>
  <div class="compare-card pandas">
    <div class="cc-label">🐼 pandas output</div>
    <div class="cc-body">
      Region<br>
      Luzon &nbsp;&nbsp;&nbsp;&nbsp; 38000<br>
      Mindanao &nbsp; 35000<br>
      Visayas &nbsp;&nbsp; 111000<br>
      <span style="color:#6b7280">Name: Revenue, dtype: int64</span>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 05</div>

## Export to CSV

Save any DataFrame back to a file — one line:

<div class="code-block">
  <span class="cmt"># Export filtered and sorted result</span><br>
  <span class="var">filtered</span>.<span class="fn">to_csv</span>(<span class="str">"visayas_output.csv"</span>, <span class="var">index</span><span class="op">=</span><span class="kw">False</span>)<br>
  <br>
  <span class="cmt"># Export to Excel instead</span><br>
  <span class="var">filtered</span>.<span class="fn">to_excel</span>(<span class="str">"visayas_output.xlsx"</span>, <span class="var">index</span><span class="op">=</span><span class="kw">False</span>)<br>
  <br>
  <span class="cmt"># Confirm it worked</span><br>
  <span class="fn">print</span>(<span class="op">f"</span><span class="str">Exported </span><span class="op">{</span><span class="fn">len</span>(<span class="var">filtered</span>)<span class="op">}</span><span class="str"> rows."</span>)
</div>

<div class="highlight">

`index=False` skips the row numbers from being written into the file — you almost always want this. The file opens cleanly in Excel, Google Sheets, or anywhere else.

</div>

---

## Why This Beats Manual Excel

<div class="why-grid">
  <div class="why-card">
    <div class="why-icon">♾️</div>
    <div class="why-title">Runs forever</div>
    <div class="why-desc">Write the script once. Run it on next month's file without touching it.</div>
  </div>
  <div class="why-card">
    <div class="why-icon">📏</div>
    <div class="why-title">No size limit</div>
    <div class="why-desc">Excel struggles past 100k rows. pandas handles millions without flinching.</div>
  </div>
  <div class="why-card">
    <div class="why-icon">🔁</div>
    <div class="why-title">Reproducible</div>
    <div class="why-desc">Every step is written down. No mystery clicks, no forgotten filter settings.</div>
  </div>
  <div class="why-card">
    <div class="why-icon">🔗</div>
    <div class="why-title">Chainable</div>
    <div class="why-desc">Combine with APIs, email scripts, dashboards — Excel can't do any of that.</div>
  </div>
  <div class="why-card">
    <div class="why-icon">🚫</div>
    <div class="why-title">No human error</div>
    <div class="why-desc">You can't accidentally drag-copy over the wrong cells when using code.</div>
  </div>
  <div class="why-card">
    <div class="why-icon">📂</div>
    <div class="why-title">Batch files</div>
    <div class="why-desc">Loop over 50 CSV files and merge them in seconds. Try that in Excel.</div>
  </div>
</div>

---

<!-- _class: final -->

# Same data.
# A fraction of the work.

&nbsp;

pandas doesn't replace Excel — it replaces the repetitive parts you hate doing.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*