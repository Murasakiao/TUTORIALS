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

  .cb-kw     { color: #c084fc; }
  .cb-fn     { color: #60a5fa; }
  .cb-str    { color: #fde68a; }
  .cb-num    { color: #fb923c; }
  .cb-cmt    { color: #4b5563; font-style: italic; }
  .cb-var    { color: #f9fafb; }
  .cb-prop   { color: #34d399; }
  .cb-cls    { color: #f87171; }
  .cb-op     { color: #6b7280; }
  .cb-out    { color: #9ca3af; }
  .cb-hi     { color: #34d399; }
  .cb-prompt { color: #22c55e; }
  .cb-cmd    { color: #f9fafb; }

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

  /* ── Calculator mockup ── */
  .calc-mock {
    background: #1c1c1e;
    border-radius: 16px;
    overflow: hidden;
    width: 220px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.28);
    font-family: 'DM Mono', monospace;
  }

  .calc-mock .cm-display {
    background: #1c1c1e;
    padding: 20px 16px 12px;
    text-align: right;
  }

  .calc-mock .cm-expr {
    font-size: 13px;
    color: #636366;
    min-height: 18px;
    margin-bottom: 4px;
  }

  .calc-mock .cm-result {
    font-size: 36px;
    color: #ffffff;
    font-weight: 300;
    letter-spacing: -1px;
  }

  .calc-mock .cm-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1px;
    background: #3a3a3c;
  }

  .calc-mock .cm-btn {
    padding: 14px 0;
    text-align: center;
    font-family: 'DM Mono', monospace;
    font-size: 16px;
    font-weight: 500;
    cursor: default;
  }

  .cm-btn.gray  { background: #636366; color: #fff; }
  .cm-btn.dark  { background: #2c2c2e; color: #fff; }
  .cm-btn.op    { background: #ff9f0a; color: #fff; }
  .cm-btn.zero  { background: #2c2c2e; color: #fff; grid-column: span 2; text-align: left; padding-left: 22px; }

  /* ── Widget anatomy (window + widget labels) ── */
  .widget-map {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 16px;
    align-items: start;
  }

  .widget-frame {
    background: #e5e7eb;
    border-radius: 10px;
    overflow: hidden;
    border: 2px solid #9ca3af;
  }

  .widget-frame .wf-titlebar {
    background: #374151;
    padding: 7px 12px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .widget-frame .wf-dot {
    width: 10px; height: 10px;
    border-radius: 50%;
    background: #6b7280;
  }

  .widget-frame .wf-title {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #9ca3af;
    margin-left: 4px;
  }

  .widget-frame .wf-body {
    padding: 12px;
    background: #f3f4f6;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .wf-display {
    background: #111827;
    color: #34d399;
    font-family: 'DM Mono', monospace;
    font-size: 18px;
    padding: 8px 12px;
    border-radius: 6px;
    text-align: right;
  }

  .wf-btn-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 5px;
  }

  .wf-btn {
    background: #374151;
    color: #f9fafb;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    padding: 7px 4px;
    border-radius: 5px;
    text-align: center;
  }

  .wf-btn.accent { background: var(--blue); }
  .wf-btn.light  { background: #9ca3af; color: #111827; }

  /* widget label list */
  .widget-labels {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .wl-row {
    display: flex;
    align-items: baseline;
    gap: 10px;
  }

  .wl-row .wl-name {
    font-family: 'DM Mono', monospace;
    font-size: 12.5px;
    color: var(--blue);
    font-weight: 500;
    min-width: 100px;
  }

  .wl-row .wl-desc {
    font-size: 13px;
    color: var(--muted);
  }

  /* ── Grid layout explainer ── */
  .grid-demo {
    background: #f1f5f9;
    border-radius: 10px;
    padding: 14px;
    margin: 14px 0;
    border: 1px solid var(--border);
  }

  .grid-demo .gd-label {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.07em;
    margin-bottom: 10px;
  }

  .grid-demo .gd-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 6px;
  }

  .gd-cell {
    background: var(--blue);
    color: white;
    border-radius: 6px;
    padding: 8px 4px;
    text-align: center;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
  }

  .gd-cell.op    { background: #f59e0b; }
  .gd-cell.light { background: #64748b; }
  .gd-cell.eq    { background: #059669; }
  .gd-cell.wide  { grid-column: span 2; }

  .gd-cell .gd-coord {
    font-size: 9px;
    opacity: 0.65;
    display: block;
    margin-top: 2px;
  }

  /* ── "What to build next" cards ── */
  .next-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .next-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 18px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }

  .next-card .nc-icon { font-size: 24px; flex-shrink: 0; }

  .next-card .nc-title {
    font-weight: 600;
    font-size: 14px;
    color: var(--text);
    margin-bottom: 3px;
  }

  .next-card .nc-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.5;
  }

  .next-card .nc-tag {
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

  /* ── Cmd / property grid ── */
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

# Build a Calculator App
## with Python + tkinter

&nbsp;

**A real GUI app. Zero extra installs.** tkinter ships with Python.

`Tk()` · `Button` · `Entry` · `grid()` · `eval()`

---

## What tkinter Is

tkinter is Python's **built-in GUI library** — create windows, buttons, labels, and input fields with pure Python.

<div class="two-col">
  <div class="col-card" style="display:flex; align-items:center; justify-content:center; padding:20px;">
    <div class="calc-mock">
      <div class="cm-display">
        <div class="cm-expr">9 × 8</div>
        <div class="cm-result">72</div>
      </div>
      <div class="cm-grid">
        <div class="cm-btn gray">AC</div>
        <div class="cm-btn gray">+/-</div>
        <div class="cm-btn gray">%</div>
        <div class="cm-btn op">÷</div>
        <div class="cm-btn dark">7</div>
        <div class="cm-btn dark">8</div>
        <div class="cm-btn dark">9</div>
        <div class="cm-btn op">×</div>
        <div class="cm-btn dark">4</div>
        <div class="cm-btn dark">5</div>
        <div class="cm-btn dark">6</div>
        <div class="cm-btn op">−</div>
        <div class="cm-btn dark">1</div>
        <div class="cm-btn dark">2</div>
        <div class="cm-btn dark">3</div>
        <div class="cm-btn op">+</div>
        <div class="cm-btn zero">0</div>
        <div class="cm-btn dark">.</div>
        <div class="cm-btn op">=</div>
      </div>
    </div>
  </div>
  <div style="display:flex; flex-direction:column; gap:12px; justify-content:center;">
    <div class="tool-card">
      <div class="icon">📦</div>
      <div class="name">Already installed</div>
      <div class="desc">Ships with Python on Mac, Windows, and Linux. <code>import tkinter</code> just works — no pip needed.</div>
    </div>
    <div class="tool-card">
      <div class="icon">🪟</div>
      <div class="name">Real native windows</div>
      <div class="desc">Opens an actual OS window — not a browser tab. Your app runs as a desktop application.</div>
    </div>
    <div class="tool-card">
      <div class="icon">🎓</div>
      <div class="name">Best first GUI library</div>
      <div class="desc">The concepts — widgets, layout managers, event callbacks — are the same in every GUI framework. Learn once, understand all.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Install Check

tkinter comes with Python but isn't always enabled. Verify it works first.

<div class="two-col">
  <div class="col-card">
    <div class="label">Test in terminal</div>
    <div class="code-block" style="margin-top:10px;">
      <div class="cb-body" style="padding:10px 14px; line-height:1.9; font-size:12px;">
        <span class="cb-prompt">~</span> <span class="cb-cmd">python3 -m tkinter</span><br>
        <span class="cb-cmt"># A small test window opens.</span><br>
        <span class="cb-cmt"># If it does — you're good.</span><br>
        <span class="cb-cmt"># If not, see fix below.</span>
      </div>
    </div>
  </div>
  <div class="col-card">
    <div class="label">Test in Python</div>
    <div class="code-block" style="margin-top:10px;">
      <div class="cb-body" style="padding:10px 14px; line-height:1.9; font-size:12px;">
        <span class="cb-kw">import</span> <span class="cb-var">tkinter</span><br>
        <span class="cb-fn">print</span><span class="cb-op">(</span><span class="cb-var">tkinter</span><span class="cb-op">.</span><span class="cb-prop">TkVersion</span><span class="cb-op">)</span><br>
        <span class="cb-out"># 8.6  ← means it's working</span>
      </div>
    </div>
  </div>
</div>

<div class="cmd-grid" style="margin-top:14px;">
  <div class="cmd-row">
    <div class="cmd-name">Mac — fix</div>
    <div class="cmd-desc">Install via Homebrew<span>brew install python-tk</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">Ubuntu — fix</div>
    <div class="cmd-desc">Install the system package<span>sudo apt install python3-tk</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">Windows</div>
    <div class="cmd-desc">Included by default<span>Reinstall Python if missing — check "tcl/tk" option</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">Virtual env</div>
    <div class="cmd-desc">Install in the active env<span>pip install tk  (Windows fallback)</span></div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02 — part 1 of 2</div>

## Window + Widget Basics

Every tkinter app starts with a `Tk()` window. Everything else — buttons, labels, inputs — is a **widget** placed inside it.

<div class="code-block">
  <div class="cb-bar">hello.py — smallest possible tkinter app</div>
  <div class="cb-body">
    <span class="cb-kw">import</span> <span class="cb-var">tkinter</span> <span class="cb-kw">as</span> <span class="cb-var">tk</span><br>
    <span class="cb-var">root</span> <span class="cb-op">=</span> <span class="cb-var">tk</span><span class="cb-op">.</span><span class="cb-fn">Tk</span><span class="cb-op">()</span>                        <span class="cb-cmt"># create the window</span><br>
    <span class="cb-var">root</span><span class="cb-op">.</span><span class="cb-fn">title</span><span class="cb-op">(</span><span class="cb-str">"Calculator"</span><span class="cb-op">)</span>              <span class="cb-cmt"># set the title bar text</span><br>
    <span class="cb-var">root</span><span class="cb-op">.</span><span class="cb-fn">resizable</span><span class="cb-op">(</span><span class="cb-num">False</span><span class="cb-op">,</span> <span class="cb-num">False</span><span class="cb-op">)</span>          <span class="cb-cmt"># fixed size window</span><br>
    <span class="cb-var">lbl</span> <span class="cb-op">=</span> <span class="cb-var">tk</span><span class="cb-op">.</span><span class="cb-fn">Label</span><span class="cb-op">(</span><span class="cb-var">root</span><span class="cb-op">,</span> <span class="cb-prop">text</span><span class="cb-op">=</span><span class="cb-str">"Hello!"</span><span class="cb-op">)</span>  <span class="cb-cmt"># create a label widget</span><br>
    <span class="cb-var">lbl</span><span class="cb-op">.</span><span class="cb-fn">pack</span><span class="cb-op">()</span>                              <span class="cb-cmt"># add it to the window</span><br>
    <span class="cb-var">btn</span> <span class="cb-op">=</span> <span class="cb-var">tk</span><span class="cb-op">.</span><span class="cb-fn">Button</span><span class="cb-op">(</span><span class="cb-var">root</span><span class="cb-op">,</span> <span class="cb-prop">text</span><span class="cb-op">=</span><span class="cb-str">"Click me"</span><span class="cb-op">,</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-prop">command</span><span class="cb-op">=</span><span class="cb-kw">lambda</span><span class="cb-op">:</span> <span class="cb-fn">print</span><span class="cb-op">(</span><span class="cb-str">"clicked!"</span><span class="cb-op">))</span><br>
    <span class="cb-var">btn</span><span class="cb-op">.</span><span class="cb-fn">pack</span><span class="cb-op">()</span><br>
    <span class="cb-var">root</span><span class="cb-op">.</span><span class="cb-fn">mainloop</span><span class="cb-op">()</span>                      <span class="cb-cmt"># keep the window open</span>
  </div>
</div>

<div class="highlight">

**The pattern:** Create window → create widgets → call a layout method (`.pack()` or `.grid()`) on each widget → start `.mainloop()`. Every tkinter app follows this exact order.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02 — part 2 of 2</div>

## Widget Glossary

Every element you can put in a window is a widget. Here are the ones used in this project.

<div class="widget-labels" style="margin-top:4px;">
  <div class="wl-row"><span class="wl-name">tk.Tk()</span><span class="wl-desc">The root window — every app needs exactly one of these</span></div>
  <div class="wl-row"><span class="wl-name">tk.Label()</span><span class="wl-desc">Displays text or an image — read only, not interactive</span></div>
  <div class="wl-row"><span class="wl-name">tk.Button()</span><span class="wl-desc">Clickable button — runs the function passed to <code>command=</code></span></div>
  <div class="wl-row"><span class="wl-name">tk.Entry()</span><span class="wl-desc">Single-line text field — used as the calculator display</span></div>
  <div class="wl-row"><span class="wl-name">tk.StringVar()</span><span class="wl-desc">A tracked variable — updating it automatically refreshes the linked widget</span></div>
  <div class="wl-row"><span class="wl-name">.pack()</span><span class="wl-desc">Simple layout — stacks widgets top to bottom, no coordinates needed</span></div>
  <div class="wl-row"><span class="wl-name">.grid()</span><span class="wl-desc">Precise layout — places widget at exact row and column in a table</span></div>
  <div class="wl-row"><span class="wl-name">.mainloop()</span><span class="wl-desc">Starts the event loop — keeps the window alive and responsive</span></div>
</div>

<div class="highlight" style="margin-top:16px;">

**Rule:** Never mix <code>.pack()</code> and <code>.grid()</code> in the same container. Pick one and use it consistently for all widgets inside that window.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Layout with `.grid()`

`.pack()` stacks things vertically. `.grid()` places widgets in exact row/column positions — essential for a button pad.

<div class="grid-demo">
  <div class="gd-label">calculator button grid — row × col positions</div>
  <div class="gd-grid">
    <div class="gd-cell light">AC<div class="gd-coord">row=1 col=0</div></div>
    <div class="gd-cell light">+/-<div class="gd-coord">row=1 col=1</div></div>
    <div class="gd-cell light">%<div class="gd-coord">row=1 col=2</div></div>
    <div class="gd-cell op">÷<div class="gd-coord">row=1 col=3</div></div>
    <div class="gd-cell">7<div class="gd-coord">row=2 col=0</div></div>
    <div class="gd-cell">8<div class="gd-coord">row=2 col=1</div></div>
    <div class="gd-cell">9<div class="gd-coord">row=2 col=2</div></div>
    <div class="gd-cell op">×<div class="gd-coord">row=2 col=3</div></div>
    <div class="gd-cell">4<div class="gd-coord">row=3 col=0</div></div>
    <div class="gd-cell">5<div class="gd-coord">row=3 col=1</div></div>
    <div class="gd-cell">6<div class="gd-coord">row=3 col=2</div></div>
    <div class="gd-cell op">−<div class="gd-coord">row=3 col=3</div></div>
    <div class="gd-cell wide">0<div class="gd-coord">row=5 col=0 colspan=2</div></div>
    <div class="gd-cell">.<div class="gd-coord">row=5 col=2</div></div>
    <div class="gd-cell eq">=<div class="gd-coord">row=5 col=3</div></div>
  </div>
</div>

<div class="code-block">
  <div class="cb-bar">placing one button with grid()</div>
  <div class="cb-body" style="padding:10px 20px; line-height:1.9;">
    <span class="cb-var">btn</span> <span class="cb-op">=</span> <span class="cb-var">tk</span><span class="cb-op">.</span><span class="cb-fn">Button</span><span class="cb-op">(</span><span class="cb-var">root</span><span class="cb-op">,</span> <span class="cb-prop">text</span><span class="cb-op">=</span><span class="cb-str">"7"</span><span class="cb-op">)</span><br>
    <span class="cb-var">btn</span><span class="cb-op">.</span><span class="cb-fn">grid</span><span class="cb-op">(</span><span class="cb-prop">row</span><span class="cb-op">=</span><span class="cb-num">2</span><span class="cb-op">,</span> <span class="cb-prop">column</span><span class="cb-op">=</span><span class="cb-num">0</span><span class="cb-op">,</span> <span class="cb-prop">sticky</span><span class="cb-op">=</span><span class="cb-str">"nsew"</span><span class="cb-op">,</span> <span class="cb-prop">padx</span><span class="cb-op">=</span><span class="cb-num">1</span><span class="cb-op">,</span> <span class="cb-prop">pady</span><span class="cb-op">=</span><span class="cb-num">1</span><span class="cb-op">)</span>  <span class="cb-cmt"># sticky fills the cell</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 04 — part 1 of 2</div>

## Wire Up the Math Logic

The display is a `StringVar` — a tkinter variable that automatically updates the UI when its value changes.

<div class="code-block">
  <div class="cb-bar">calculator.py — window, display, and StringVar</div>
  <div class="cb-body">
    <span class="cb-kw">import</span> <span class="cb-var">tkinter</span> <span class="cb-kw">as</span> <span class="cb-var">tk</span><br>
    <span class="cb-var">root</span> <span class="cb-op">=</span> <span class="cb-var">tk</span><span class="cb-op">.</span><span class="cb-fn">Tk</span><span class="cb-op">()</span><br>
    <span class="cb-var">root</span><span class="cb-op">.</span><span class="cb-fn">title</span><span class="cb-op">(</span><span class="cb-str">"Calculator"</span><span class="cb-op">)</span><br>
    <span class="cb-var">root</span><span class="cb-op">.</span><span class="cb-fn">resizable</span><span class="cb-op">(</span><span class="cb-num">False</span><span class="cb-op">,</span> <span class="cb-num">False</span><span class="cb-op">)</span><br>
    <span class="cb-cmt"># StringVar tracks the display value — changing it updates the widget</span><br>
    <span class="cb-var">expr</span> <span class="cb-op">=</span> <span class="cb-var">tk</span><span class="cb-op">.</span><span class="cb-fn">StringVar</span><span class="cb-op">()</span><br>
    <span class="cb-cmt"># Entry widget — read-only, linked to expr via textvariable</span><br>
    <span class="cb-var">display</span> <span class="cb-op">=</span> <span class="cb-var">tk</span><span class="cb-op">.</span><span class="cb-fn">Entry</span><span class="cb-op">(</span><span class="cb-var">root</span><span class="cb-op">,</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-prop">textvariable</span><span class="cb-op">=</span><span class="cb-var">expr</span><span class="cb-op">,</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-prop">font</span><span class="cb-op">=(</span><span class="cb-str">"DM Mono"</span><span class="cb-op">,</span> <span class="cb-num">24</span><span class="cb-op">),</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-prop">justify</span><span class="cb-op">=</span><span class="cb-str">"right"</span><span class="cb-op">,</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-prop">bd</span><span class="cb-op">=</span><span class="cb-num">0</span><span class="cb-op">,</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-prop">state</span><span class="cb-op">=</span><span class="cb-str">"readonly"</span><span class="cb-op">)</span>  <span class="cb-cmt"># user can't type directly</span><br>
    <span class="cb-var">display</span><span class="cb-op">.</span><span class="cb-fn">grid</span><span class="cb-op">(</span><span class="cb-prop">row</span><span class="cb-op">=</span><span class="cb-num">0</span><span class="cb-op">,</span> <span class="cb-prop">column</span><span class="cb-op">=</span><span class="cb-num">0</span><span class="cb-op">,</span> <span class="cb-prop">columnspan</span><span class="cb-op">=</span><span class="cb-num">4</span><span class="cb-op">,</span> <span class="cb-prop">sticky</span><span class="cb-op">=</span><span class="cb-str">"nsew"</span><span class="cb-op">)</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 04 — part 2 of 2</div>

## The `press()` Callback

One function handles every button. It checks what was pressed and responds accordingly.

<div class="code-block">
  <div class="cb-bar">calculator.py — the press() function</div>
  <div class="cb-body">
    <span class="cb-kw">def</span> <span class="cb-fn">press</span><span class="cb-op">(</span><span class="cb-var">key</span><span class="cb-op">):</span><br>
    &nbsp;&nbsp;<span class="cb-kw">if</span> <span class="cb-var">key</span> <span class="cb-op">==</span> <span class="cb-str">"C"</span><span class="cb-op">:</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-var">expr</span><span class="cb-op">.</span><span class="cb-fn">set</span><span class="cb-op">(</span><span class="cb-str">""</span><span class="cb-op">)</span>                           <span class="cb-cmt"># clear the display</span><br>
    &nbsp;&nbsp;<span class="cb-kw">elif</span> <span class="cb-var">key</span> <span class="cb-op">==</span> <span class="cb-str">"⌫"</span><span class="cb-op">:</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-var">expr</span><span class="cb-op">.</span><span class="cb-fn">set</span><span class="cb-op">(</span><span class="cb-var">expr</span><span class="cb-op">.</span><span class="cb-fn">get</span><span class="cb-op">()[:</span><span class="cb-op">-</span><span class="cb-num">1</span><span class="cb-op">])</span>              <span class="cb-cmt"># delete last character</span><br>
    &nbsp;&nbsp;<span class="cb-kw">elif</span> <span class="cb-var">key</span> <span class="cb-op">==</span> <span class="cb-str">"="</span><span class="cb-op">:</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-kw">try</span><span class="cb-op">:</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-var">expr</span><span class="cb-op">.</span><span class="cb-fn">set</span><span class="cb-op">(</span><span class="cb-fn">eval</span><span class="cb-op">(</span><span class="cb-var">expr</span><span class="cb-op">.</span><span class="cb-fn">get</span><span class="cb-op">()))</span>          <span class="cb-cmt"># evaluate the expression</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-kw">except</span><span class="cb-op">:</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-var">expr</span><span class="cb-op">.</span><span class="cb-fn">set</span><span class="cb-op">(</span><span class="cb-str">"Error"</span><span class="cb-op">)</span>                  <span class="cb-cmt"># show error on bad input</span><br>
    &nbsp;&nbsp;<span class="cb-kw">else</span><span class="cb-op">:</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-var">expr</span><span class="cb-op">.</span><span class="cb-fn">set</span><span class="cb-op">(</span><span class="cb-var">expr</span><span class="cb-op">.</span><span class="cb-fn">get</span><span class="cb-op">()</span> <span class="cb-op">+</span> <span class="cb-var">key</span><span class="cb-op">)</span>          <span class="cb-cmt"># append digit or operator</span>
  </div>
</div>

<div class="two-col" style="margin-top:14px;">
  <div class="col-card">
    <div class="label">Why eval()?</div>
    <p style="font-size:13.5px; margin-top:6px;"><code>eval("9*8+2")</code> returns <code>74</code>. Python evaluates any math expression string. The <code>try/except</code> catches division by zero, empty input, and typos.</p>
  </div>
  <div class="col-card">
    <div class="label">How StringVar works</div>
    <p style="font-size:13.5px; margin-top:6px;"><code>expr.set("72")</code> updates the variable and the display widget refreshes automatically — no manual <code>.config(text=...)</code> needed.</p>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 05 — part 1 of 2</div>

## Build the Button Grid

Loop over a list of button labels to create the full pad in a few lines — no copy-pasting 20 `Button()` calls.

<div class="code-block">
  <div class="cb-bar">calculator.py — button layout data</div>
  <div class="cb-body">
    <span class="cb-cmt"># Nested list defines button label and its grid position</span><br>
    <span class="cb-cmt"># Each sub-list = one row. Index in sub-list = column.</span><br>
    <span class="cb-var">buttons</span> <span class="cb-op">=</span> <span class="cb-op">[</span><br>
    &nbsp;&nbsp;<span class="cb-op">[</span><span class="cb-str">"C"</span><span class="cb-op">,</span>  <span class="cb-str">"("</span><span class="cb-op">,</span> <span class="cb-str">")"</span><span class="cb-op">,</span>  <span class="cb-str">"/"</span><span class="cb-op">],</span>  <span class="cb-cmt"># row 1</span><br>
    &nbsp;&nbsp;<span class="cb-op">[</span><span class="cb-str">"7"</span><span class="cb-op">,</span>  <span class="cb-str">"8"</span><span class="cb-op">,</span> <span class="cb-str">"9"</span><span class="cb-op">,</span>  <span class="cb-str">"*"</span><span class="cb-op">],</span>  <span class="cb-cmt"># row 2</span><br>
    &nbsp;&nbsp;<span class="cb-op">[</span><span class="cb-str">"4"</span><span class="cb-op">,</span>  <span class="cb-str">"5"</span><span class="cb-op">,</span> <span class="cb-str">"6"</span><span class="cb-op">,</span>  <span class="cb-str">"-"</span><span class="cb-op">],</span>  <span class="cb-cmt"># row 3</span><br>
    &nbsp;&nbsp;<span class="cb-op">[</span><span class="cb-str">"1"</span><span class="cb-op">,</span>  <span class="cb-str">"2"</span><span class="cb-op">,</span> <span class="cb-str">"3"</span><span class="cb-op">,</span>  <span class="cb-str">"+"</span><span class="cb-op">],</span>  <span class="cb-cmt"># row 4</span><br>
    &nbsp;&nbsp;<span class="cb-op">[</span><span class="cb-str">"0"</span><span class="cb-op">,</span>  <span class="cb-str">"."</span><span class="cb-op">,</span> <span class="cb-str">"⌫"</span><span class="cb-op">,</span> <span class="cb-str">"="</span><span class="cb-op">],</span>  <span class="cb-cmt"># row 5</span><br>
    <span class="cb-op">]</span><br>
    <span class="cb-cmt"># enumerate(buttons, 1) starts counting from 1</span><br>
    <span class="cb-cmt"># because row 0 is already taken by the display</span><br>
    <span class="cb-kw">for</span> <span class="cb-var">r</span><span class="cb-op">,</span> <span class="cb-var">row</span> <span class="cb-kw">in</span> <span class="cb-fn">enumerate</span><span class="cb-op">(</span><span class="cb-var">buttons</span><span class="cb-op">,</span> <span class="cb-num">1</span><span class="cb-op">):</span><br>
    &nbsp;&nbsp;<span class="cb-kw">for</span> <span class="cb-var">c</span><span class="cb-op">,</span> <span class="cb-var">label</span> <span class="cb-kw">in</span> <span class="cb-fn">enumerate</span><span class="cb-op">(</span><span class="cb-var">row</span><span class="cb-op">):</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-var">tk</span><span class="cb-op">.</span><span class="cb-fn">Button</span><span class="cb-op">(</span><span class="cb-var">root</span><span class="cb-op">,</span> <span class="cb-prop">text</span><span class="cb-op">=</span><span class="cb-var">label</span><span class="cb-op">,</span> <span class="cb-prop">width</span><span class="cb-op">=</span><span class="cb-num">5</span><span class="cb-op">,</span> <span class="cb-prop">height</span><span class="cb-op">=</span><span class="cb-num">2</span><span class="cb-op">,</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-prop">command</span><span class="cb-op">=</span><span class="cb-kw">lambda</span> <span class="cb-var">k</span><span class="cb-op">=</span><span class="cb-var">label</span><span class="cb-op">:</span> <span class="cb-fn">press</span><span class="cb-op">(</span><span class="cb-var">k</span><span class="cb-op">))</span> \<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-op">.</span><span class="cb-fn">grid</span><span class="cb-op">(</span><span class="cb-prop">row</span><span class="cb-op">=</span><span class="cb-var">r</span><span class="cb-op">,</span> <span class="cb-prop">column</span><span class="cb-op">=</span><span class="cb-var">c</span><span class="cb-op">,</span> <span class="cb-prop">sticky</span><span class="cb-op">=</span><span class="cb-str">"nsew"</span><span class="cb-op">,</span> <span class="cb-prop">padx</span><span class="cb-op">=</span><span class="cb-num">1</span><span class="cb-op">,</span> <span class="cb-prop">pady</span><span class="cb-op">=</span><span class="cb-num">1</span><span class="cb-op">)</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 05 — part 2 of 2</div>

## The Lambda Gotcha + Finish

The most common bug when creating buttons in a loop — and how to fix it.

<div class="two-col">
  <div class="col-card">
    <div class="label">❌ &nbsp;Broken — all buttons call "="</div>
    <div class="code-block" style="margin-top:8px;">
      <div class="cb-body" style="padding:10px 14px; line-height:1.9; font-size:12px;">
        <span class="cb-cmt"># label is looked up at call time</span><br>
        <span class="cb-cmt"># by then the loop is done</span><br>
        <span class="cb-kw">lambda</span><span class="cb-op">:</span> <span class="cb-fn">press</span><span class="cb-op">(</span><span class="cb-var">label</span><span class="cb-op">)</span>
      </div>
    </div>
  </div>
  <div class="col-card">
    <div class="label">✅ &nbsp;Fixed — each button captures its own value</div>
    <div class="code-block" style="margin-top:8px;">
      <div class="cb-body" style="padding:10px 14px; line-height:1.9; font-size:12px;">
        <span class="cb-cmt"># k=label copies the value now</span><br>
        <span class="cb-cmt"># into a default argument</span><br>
        <span class="cb-kw">lambda</span> <span class="cb-var">k</span><span class="cb-op">=</span><span class="cb-var">label</span><span class="cb-op">:</span> <span class="cb-fn">press</span><span class="cb-op">(</span><span class="cb-var">k</span><span class="cb-op">)</span>
      </div>
    </div>
  </div>
</div>

<div class="code-block" style="margin-top:14px;">
  <div class="cb-bar">calculator.py — final line</div>
  <div class="cb-body" style="padding:10px 20px; line-height:1.9;">
    <span class="cb-cmt"># After all widgets are placed, start the event loop</span><br>
    <span class="cb-var">root</span><span class="cb-op">.</span><span class="cb-fn">mainloop</span><span class="cb-op">()</span>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**The complete file is now done.** `import` → window → `StringVar` → display → `press()` → button loop → `mainloop()`. Run it with `python3 calculator.py`.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 06</div>

## Run It

<div class="two-col">
  <div class="col-card">
    <div class="label">From terminal</div>
    <div class="code-block" style="margin-top:10px;">
      <div class="cb-body" style="padding:10px 14px; line-height:1.9; font-size:12px;">
        <span class="cb-prompt">~</span> <span class="cb-cmd">python3 calculator.py</span><br>
        <span class="cb-cmt"># A window opens immediately.</span><br>
        <span class="cb-cmt"># Click buttons to build an</span><br>
        <span class="cb-cmt"># expression, then press =</span>
      </div>
    </div>
  </div>
  <div class="col-card">
    <div class="label">From VS Code</div>
    <p style="font-size:13.5px; margin-top:8px;">Open <code>calculator.py</code> → press <code>▶ Run</code> or hit <code>F5</code>. The tkinter window opens alongside the terminal panel.</p>
    <p style="font-size:13px; color:var(--muted); margin-top:8px;">On Mac, the window may appear behind VS Code. Check the Dock — it shows as a Python icon.</p>
  </div>
</div>

<div class="cmd-grid" style="margin-top:14px;">
  <div class="cmd-row">
    <div class="cmd-name">Window not opening</div>
    <div class="cmd-desc">Check tkinter install<span>python3 -m tkinter → should show test window</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">= shows "Error"</div>
    <div class="cmd-desc">Invalid expression in display<span>The try/except catches bad input cleanly</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">Buttons same value</div>
    <div class="cmd-desc">Lambda capture bug<span>Use k=label default arg — see previous slide</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">Window closes instantly</div>
    <div class="cmd-desc">Missing mainloop()<span>Always end with root.mainloop()</span></div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## What to Build Next

The calculator introduced every core tkinter concept. Here's where each one leads.

<div class="next-grid">
  <div class="next-card">
    <div class="nc-icon">📝</div>
    <div>
      <div class="nc-title">Text editor</div>
      <div class="nc-desc">Add a <code>Text</code> widget and a menu bar. Opens, edits, and saves files — covers <code>Menu</code>, <code>filedialog</code>, and keyboard shortcuts.</div>
      <div class="nc-tag">tk.Text · filedialog · Menu</div>
    </div>
  </div>
  <div class="next-card">
    <div class="nc-icon">⏱️</div>
    <div>
      <div class="nc-title">Pomodoro timer</div>
      <div class="nc-desc">Use <code>root.after()</code> to call a function every second. Counts down, plays a sound with <code>playsound</code>, and resets. Great for practicing state.</div>
      <div class="nc-tag">root.after · StringVar · playsound</div>
    </div>
  </div>
  <div class="next-card">
    <div class="nc-icon">🌤️</div>
    <div>
      <div class="nc-title">Weather dashboard</div>
      <div class="nc-desc">Combine with the <code>requests</code> + API tutorial. Fetch weather data on button click, display it in <code>Label</code> widgets, refresh on a timer.</div>
      <div class="nc-tag">requests · Label · after()</div>
    </div>
  </div>
  <div class="next-card">
    <div class="nc-icon">✅</div>
    <div>
      <div class="nc-title">To-do list app</div>
      <div class="nc-desc">A <code>Listbox</code> widget + <code>Entry</code> + <code>Button</code>. Add tasks, mark them done, delete them. Persist to a JSON file between sessions.</div>
      <div class="nc-tag">Listbox · Entry · json · pickle</div>
    </div>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**Outgrown tkinter?** When you need a more polished look, try **CustomTkinter** (modern themed widgets, same API) or **PyQt6** (professional cross-platform desktop apps).

</div>

---

## tkinter Quick Reference

<table class="cheat-table">
  <tr>
    <th>Widget / Method</th>
    <th>What it does</th>
    <th>Key options</th>
  </tr>
  <tr>
    <td class="mono">tk.Tk()</td>
    <td>Create the root window</td>
    <td class="mono">.title() · .resizable() · .geometry()</td>
  </tr>
  <tr>
    <td class="mono">tk.Label()</td>
    <td>Display static text or image</td>
    <td class="mono">text= · font= · fg= · bg=</td>
  </tr>
  <tr>
    <td class="mono">tk.Button()</td>
    <td>Clickable button</td>
    <td class="mono">text= · command= · width= · height=</td>
  </tr>
  <tr>
    <td class="mono">tk.Entry()</td>
    <td>Single-line text input</td>
    <td class="mono">textvariable= · state= · justify=</td>
  </tr>
  <tr>
    <td class="mono">tk.StringVar()</td>
    <td>Variable bound to a widget — auto-updates UI</td>
    <td class="mono">.get() · .set(value)</td>
  </tr>
  <tr>
    <td class="mono">.grid()</td>
    <td>Place widget at row/column position</td>
    <td class="mono">row= · column= · columnspan= · sticky=</td>
  </tr>
  <tr>
    <td class="mono">.pack()</td>
    <td>Stack widgets top-to-bottom</td>
    <td class="mono">side= · fill= · expand=</td>
  </tr>
  <tr>
    <td class="mono">root.mainloop()</td>
    <td>Start the event loop — required at the end</td>
    <td>Never call twice</td>
  </tr>
  <tr>
    <td class="mono">lambda k=v: f(k)</td>
    <td>Capture loop variable in a button command</td>
    <td>Default arg trick — essential in loops</td>
  </tr>
  <tr>
    <td class="mono">eval(expr.get())</td>
    <td>Evaluate the expression string as math</td>
    <td>Always wrap in try/except</td>
  </tr>
</table>

---

<!-- _class: final -->

# You just built a
# real desktop app.

&nbsp;

Window. Widgets. Grid. Logic. That's all of GUI programming.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*