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

  /* Spreadsheet mock */
  .sheet {
    border-collapse: collapse;
    width: 100%;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    margin: 12px 0;
    border-radius: 8px;
    overflow: hidden;
  }

  .sheet thead tr { background: #1e3a5f; }
  .sheet thead th { color: #93c5fd; padding: 7px 12px; text-align: left; font-weight: 500; font-size: 11px; letter-spacing: 0.04em; }
  .sheet tbody tr:nth-child(odd)  { background: #111827; }
  .sheet tbody tr:nth-child(even) { background: #1f2937; }
  .sheet tbody td { color: #e5e7eb; padding: 6px 12px; font-size: 12px; }
  .sheet tbody tr.dirty td { color: #f87171; }
  .sheet tbody tr.clean td { color: #86efac; }
  .sheet tbody td.warn { color: #fde68a; }

  /* Before/after compare */
  .compare-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 14px 0;
  }

  .compare-card {
    border-radius: 10px;
    overflow: hidden;
  }

  .compare-card .cc-label {
    padding: 7px 14px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 600;
  }

  .compare-card.dirty .cc-label { background: #7f1d1d; color: #fca5a5; }
  .compare-card.clean .cc-label { background: #14532d; color: #86efac; }

  .compare-card .cc-body {
    background: #0d1117;
    padding: 12px 14px;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    line-height: 2;
  }

  .compare-card.dirty .cc-body { border: 1px solid #7f1d1d; border-top: none; border-radius: 0 0 10px 10px; color: #f87171; }
  .compare-card.clean .cc-body { border: 1px solid #14532d; border-top: none; border-radius: 0 0 10px 10px; color: #86efac; }

  /* Automation pipeline */
  .pipeline {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 0;
    align-items: center;
    margin: 18px 0;
  }

  .pipe-node {
    background: #111827;
    border-radius: 8px;
    padding: 14px 10px;
    text-align: center;
  }

  .pipe-node .pn-icon  { font-size: 20px; margin-bottom: 5px; }
  .pipe-node .pn-label { font-family: 'DM Mono', monospace; font-size: 12px; font-weight: 600; margin-bottom: 3px; }
  .pipe-node .pn-desc  { font-size: 11px; color: #6b7280; line-height: 1.4; }

  .pipe-node.p1 .pn-label { color: #f87171; }
  .pipe-node.p2 .pn-label { color: #fde68a; }
  .pipe-node.p3 .pn-label { color: #60a5fa; }
  .pipe-node.p4 .pn-label { color: #c4b5fd; }
  .pipe-node.p5 .pn-label { color: #86efac; }

  .pipe-arrow {
    text-align: center;
    color: #374151;
    font-size: 16px;
    padding: 0 4px;
  }

  /* Insight card grid */
  .insight-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin: 14px 0;
  }

  .insight-card {
    background: #111827;
    border-radius: 8px;
    padding: 14px 16px;
    border-left: 3px solid #1d4ed8;
  }

  .insight-card .ic-prompt {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #60a5fa;
    margin-bottom: 6px;
    line-height: 1.4;
  }

  .insight-card .ic-result {
    font-size: 13px;
    color: #d1d5db;
    line-height: 1.5;
  }

  .insight-card .ic-result strong { color: #86efac; font-weight: 600; }

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
    margin-bottom: 12px;
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

# Spreadsheets Into Automations
## with AI

&nbsp;

**Your spreadsheet is already a database. AI turns it into a pipeline.**

`clean` · `analyse` · `automate` · `pandas` · `schedule`

---

## Why Spreadsheets Are Powerful Starting Points

Every organisation runs on spreadsheets. They're not the problem — the manual work around them is.

<div class="tools">
  <div class="tool-card">
    <div class="icon">📊</div>
    <div class="name">Already structured</div>
    <div class="desc">Rows, columns, headers — your data is already in a shape Python and pandas can read directly.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔁</div>
    <div class="name">Repetitive by nature</div>
    <div class="desc">The same cleaning, filtering, and summary steps run every week. That's not work — that's a script waiting to be written.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🤖</div>
    <div class="name">AI understands the structure</div>
    <div class="desc">Paste your headers and a few rows — AI immediately understands the schema and can write operations against it.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🚀</div>
    <div class="name">Zero infrastructure needed</div>
    <div class="desc">No database, no cloud setup, no API. A CSV file and a Python script is a complete automation pipeline.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Use AI to Clean Your Data

Messy data is the first bottleneck. Describe what's wrong — AI writes the fix.

<div class="compare-grid">
  <div class="compare-card dirty">
    <div class="cc-label">❌ Raw — before cleaning</div>
    <div class="cc-body">
      Santos R. | Visayas | Solar Panel | 48000<br>
      cruz m.   | luzon   | inverter    | 21,000<br>
      REYES J.  | Visayas | Battery     | N/A<br>
      Lim A.    | Mindanao| solar panel | 35000.0<br>
      Garcia P  | luzon   | Inverter    | 17000
    </div>
  </div>
  <div class="compare-card clean">
    <div class="cc-label">✅ Clean — after script</div>
    <div class="cc-body">
      Santos R. | Visayas  | Solar Panel | 48000<br>
      Cruz M.   | Luzon    | Inverter    | 21000<br>
      Reyes J.  | Visayas  | Battery     | NaN<br>
      Lim A.    | Mindanao | Solar Panel | 35000<br>
      Garcia P. | Luzon    | Inverter    | 17000
    </div>
  </div>
</div>

<div class="highlight">

**The AI prompt:** *"Here are my column headers and 5 sample rows [paste]. Write a pandas script that: normalises name casing, title-cases the region and product columns, strips commas from revenue and converts to float, and fills missing values with NaN."*

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Generate Insights from the Data

Once it's clean, ask AI to write the analysis — not to do the analysis for you.

<div class="insight-grid">
  <div class="insight-card">
    <div class="ic-prompt">"Revenue by region, sorted desc"</div>
    <div class="ic-result">df.groupby("region")["revenue"].sum()<br>.sort_values(<strong>ascending=False</strong>)</div>
  </div>
  <div class="insight-card">
    <div class="ic-prompt">"Month with highest avg revenue"</div>
    <div class="ic-result">df.groupby("month")["revenue"].mean()<br>.idxmax() → <strong>returns month label</strong></div>
  </div>
  <div class="insight-card">
    <div class="ic-prompt">"Flag rows where revenue is null"</div>
    <div class="ic-result">df[df["revenue"].isna()][["name","region"]] → <strong>missing rows only</strong></div>
  </div>
</div>

<div class="code-block">
  <span class="cmt"># AI-generated insight block — paste your headers + 5 rows, then ask for these</span><br>
  <span class="var">summary</span> <span class="op">=</span> <span class="var">df</span>.<span class="fn">groupby</span>(<span class="str">"region"</span>)[<span class="str">"revenue"</span>].<span class="fn">agg</span>([<span class="str">"sum"</span>, <span class="str">"mean"</span>, <span class="str">"count"</span>])<br>
  <span class="var">summary</span>.<span class="var">columns</span> <span class="op">=</span> [<span class="str">"total"</span>, <span class="str">"average"</span>, <span class="str">"deals"</span>]<br>
  <span class="var">summary</span> <span class="op">=</span> <span class="var">summary</span>.<span class="fn">sort_values</span>(<span class="str">"total"</span>, <span class="var">ascending</span><span class="op">=</span><span class="kw">False</span>)<br>
  <span class="fn">print</span>(<span class="var">summary</span>.<span class="fn">to_string</span>())
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Automate the Updates

A manual script run is better than a manual spreadsheet update. A scheduled script run is better still.

<div class="pipeline">
  <div class="pipe-node p1">
    <div class="pn-icon">📥</div>
    <div class="pn-label">Input</div>
    <div class="pn-desc">New CSV dropped into folder</div>
  </div>
  <div class="pipe-arrow">→</div>
  <div class="pipe-node p2">
    <div class="pn-icon">🧹</div>
    <div class="pn-label">Clean</div>
    <div class="pn-desc">Normalise, coerce types, fill NaN</div>
  </div>
  <div class="pipe-arrow">→</div>
  <div class="pipe-node p3">
    <div class="pn-icon">📊</div>
    <div class="pn-label">Analyse</div>
    <div class="pn-desc">Groupby, sort, flag anomalies</div>
  </div>
  <div class="pipe-arrow">→</div>
  <div class="pipe-node p4">
    <div class="pn-icon">📤</div>
    <div class="pn-label">Export</div>
    <div class="pn-desc">Write summary.csv + report.xlsx</div>
  </div>
  <div class="pipe-arrow">→</div>
  <div class="pipe-node p5">
    <div class="pn-icon">⏰</div>
    <div class="pn-label">Schedule</div>
    <div class="pn-desc">cron (Mac/Linux) or Task Scheduler (Windows)</div>
  </div>
</div>

<div class="two-col">
  <div class="col-card">
    <div class="label">Mac / Linux — cron</div>
    <p style="font-size:13px; margin-top:8px; font-family:'DM Mono',monospace; color:#374151; line-height:1.9;">
      # Run every Monday at 8am<br>
      0 8 * * 1 python3 /path/to/pipeline.py
    </p>
  </div>
  <div class="col-card">
    <div class="label">Windows — Task Scheduler</div>
    <p style="font-size:14px; margin-top:8px; color:#374151; line-height:1.8;">
      Task Scheduler → Create Basic Task → set trigger → action: run <code>python pipeline.py</code>
    </p>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">EXAMPLE</div>

## End-to-End: Monthly Sales Report

A real workflow you can build in an afternoon with AI:

<ul class="step-list">
  <li>Export your monthly sales data as a CSV — from any CRM, tool, or manual log</li>
  <li>Paste 5 rows + headers into Claude. Ask: <strong>"Write a pandas script to clean this data."</strong> Specify the issues — casing, types, missing values</li>
  <li>Ask: <strong>"Add a summary block: total and average revenue by region, top 5 products, and flag any rows with missing revenue."</strong></li>
  <li>Ask: <strong>"Export the cleaned data to clean.csv and the summary to summary.xlsx with bold headers."</strong></li>
  <li>Ask: <strong>"Wrap this in a function called run_pipeline() that accepts a filepath as input."</strong></li>
  <li>Save as <code>pipeline.py</code>. Drop any new monthly CSV in the folder. Run once to verify. Schedule with cron or Task Scheduler.</li>
</ul>

<div class="highlight good">

Total AI prompts: 4. Total time: under an hour. The same report that used to take a morning now runs while you sleep.

</div>

---

## The Full Code — What AI Writes for You

<div class="code-block">
  <span class="kw">import</span> <span class="var">pandas</span> <span class="kw">as</span> <span class="var">pd</span><br>
  <span class="kw">import</span> <span class="var">os</span><br>
  <br>
  <span class="kw">def</span> <span class="fn">run_pipeline</span>(<span class="var">filepath</span>):<br>
  &nbsp;&nbsp;<span class="var">df</span> <span class="op">=</span> <span class="var">pd</span>.<span class="fn">read_csv</span>(<span class="var">filepath</span>)<br>
  &nbsp;&nbsp;<span class="cmt"># Clean — normalise casing, coerce types</span><br>
  &nbsp;&nbsp;<span class="var">df</span>[<span class="str">"name"</span>]    <span class="op">=</span> <span class="var">df</span>[<span class="str">"name"</span>].<span class="fn">str.title</span>()<br>
  &nbsp;&nbsp;<span class="var">df</span>[<span class="str">"region"</span>]  <span class="op">=</span> <span class="var">df</span>[<span class="str">"region"</span>].<span class="fn">str.title</span>()<br>
  &nbsp;&nbsp;<span class="var">df</span>[<span class="str">"revenue"</span>] <span class="op">=</span> <span class="var">pd</span>.<span class="fn">to_numeric</span>(<span class="var">df</span>[<span class="str">"revenue"</span>].<span class="fn">astype</span>(<span class="var">str</span>).<span class="fn">str.replace</span>(<span class="str">","</span>, <span class="str">""</span>), <span class="var">errors</span><span class="op">=</span><span class="str">"coerce"</span>)<br>
  &nbsp;&nbsp;<span class="cmt"># Summarise</span><br>
  &nbsp;&nbsp;<span class="var">summary</span> <span class="op">=</span> <span class="var">df</span>.<span class="fn">groupby</span>(<span class="str">"region"</span>)[<span class="str">"revenue"</span>].<span class="fn">agg</span>([<span class="str">"sum"</span>, <span class="str">"mean"</span>, <span class="str">"count"</span>])<br>
  &nbsp;&nbsp;<span class="cmt"># Export</span><br>
  &nbsp;&nbsp;<span class="var">df</span>.<span class="fn">to_csv</span>(<span class="str">"clean.csv"</span>, <span class="var">index</span><span class="op">=</span><span class="kw">False</span>)<br>
  &nbsp;&nbsp;<span class="var">summary</span>.<span class="fn">to_excel</span>(<span class="str">"summary.xlsx"</span>)<br>
  &nbsp;&nbsp;<span class="fn">print</span>(<span class="op">f"</span><span class="str">Pipeline complete. </span><span class="op">{</span><span class="fn">len</span>(<span class="var">df</span>)<span class="op">}</span><span class="str"> rows processed."</span>)<br>
  <br>
  <span class="kw">if</span> <span class="var">__name__</span> <span class="op">==</span> <span class="str">"__main__"</span>:<br>
  &nbsp;&nbsp;<span class="fn">run_pipeline</span>(<span class="str">"sales.csv"</span>)
</div>

---

<!-- _class: final -->

# Your spreadsheet already
# has a script inside it.

&nbsp;

AI just helps you write it out.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*