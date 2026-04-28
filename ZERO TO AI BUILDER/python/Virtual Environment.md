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

  /* Terminal — Mac style */
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

  .terminal-bar .dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    display: inline-block;
  }

  .terminal-bar .dot.red    { background: #ef4444; }
  .terminal-bar .dot.yellow { background: #f59e0b; }
  .terminal-bar .dot.green  { background: #22c55e; }

  .terminal-bar .title {
    font-size: 12px;
    color: #6b7280;
    margin-left: 8px;
  }

  .terminal-body {
    padding: 14px 20px;
    line-height: 2;
  }

  .terminal-body .prompt     { color: #22c55e; }
  .terminal-body .prompt-env { color: #86efac; }
  .terminal-body .cmd        { color: #f9fafb; }
  .terminal-body .out        { color: #9ca3af; }
  .terminal-body .out-g      { color: #86efac; }
  .terminal-body .out-y      { color: #fde68a; }
  .terminal-body .out-b      { color: #60a5fa; }
  .terminal-body .cmt        { color: #4b5563; font-style: italic; }

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
  .code-block .cmt { color: #4b5563; font-style: italic; }

  /* Project isolation diagram */
  .project-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 16px 0;
  }

  .project-box {
    border-radius: 10px;
    padding: 16px 18px;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .project-box.bad {
    background: #111827;
    border: 1px solid #374151;
  }

  .project-box.good {
    background: #111827;
    border: 1px solid #166534;
  }

  .project-box .proj-label {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 10px;
    font-family: 'DM Sans', sans-serif;
    font-weight: 600;
  }

  .project-box.bad  .proj-label { color: #f87171; }
  .project-box.good .proj-label { color: #86efac; }

  .project-box .proj-name {
    color: #60a5fa;
    font-weight: 500;
    margin-bottom: 4px;
  }

  .project-box .pkg {
    color: #d1d5db;
    font-size: 12px;
    line-height: 1.8;
  }

  .project-box .pkg-conflict { color: #f87171; }
  .project-box .pkg-ok       { color: #86efac; }

  /* venv 3-step strip */
  .venv-steps {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin: 16px 0;
  }

  .venv-step {
    background: #111827;
    border-radius: 8px;
    padding: 14px 16px;
  }

  .venv-step .vs-num {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 6px;
  }

  .venv-step .vs-cmd {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #60a5fa;
    font-weight: 500;
    margin-bottom: 6px;
  }

  .venv-step .vs-desc {
    font-size: 12px;
    color: #9ca3af;
    line-height: 1.5;
  }

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

  /* Habit checklist */
  .habit-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .habit-list li {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    margin-bottom: 14px;
    font-size: 16px;
  }

  .habit-list .hicon {
    font-size: 18px;
    margin-top: 1px;
    flex-shrink: 0;
  }
---

<!-- _class: cover -->

# pip and Virtual Environments
## How to Use Them

&nbsp;

**Install packages cleanly.** Keep projects from breaking each other.

`pip` · `venv` · `activate` · `requirements.txt`

---

## What pip Does

`pip` is Python's package manager — it downloads and installs libraries from the internet.

<div class="tools">
  <div class="tool-card">
    <div class="icon">📦</div>
    <div class="name">pip install</div>
    <div class="desc">Downloads a package and makes it available to import in your scripts.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔍</div>
    <div class="name">pip list</div>
    <div class="desc">Shows every package currently installed in your Python environment.</div>
  </div>
  <div class="tool-card">
    <div class="icon">📋</div>
    <div class="name">pip freeze</div>
    <div class="desc">Outputs your installed packages as a list — used to create requirements.txt.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🗑️</div>
    <div class="name">pip uninstall</div>
    <div class="desc">Removes a package. Asks for confirmation before deleting.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Install Your First Package

Installing a package is one command. Here we install `requests` — a library for fetching web data:

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
    <span class="title">zsh — Terminal</span>
  </div>
  <div class="terminal-body">
    <span class="prompt">~ %</span> <span class="cmd">pip3 install requests</span><br>
    <span class="out">Collecting requests</span><br>
    <span class="out">  Downloading requests-2.31.0-py3-none-any.whl</span><br>
    <span class="out-g">Successfully installed requests-2.31.0</span>
  </div>
</div>

Now use it in any script:

<div class="code-block">
  <span class="kw">import</span> <span class="var">requests</span><br>
  <span class="var">response</span> <span class="op">=</span> <span class="fn">requests.get</span>(<span class="str">"https://api.github.com"</span>)<br>
  <span class="fn">print</span>(<span class="var">response</span>.<span class="var">status_code</span>) <span class="cmt"># 200</span>
</div>

<div class="highlight">

**Mac:** use `pip3` &nbsp;·&nbsp; **Windows:** use `pip` &nbsp;·&nbsp; Both work the same way.

</div>

---

<!-- _class: step -->

<div class="warn-badge">⚠️ THE PROBLEM</div>

## Dependency Hell

Without virtual environments, every package installs globally — into the same Python on your machine.

<div class="project-grid">
  <div class="project-box bad">
    <div class="proj-label">❌ Global installs — no venv</div>
    <div class="proj-name">project-a/</div>
    <div class="pkg">needs <span class="pkg-conflict">flask==2.0</span></div>
    <div class="proj-name" style="margin-top:10px">project-b/</div>
    <div class="pkg">needs <span class="pkg-conflict">flask==3.1</span></div>
    <div class="pkg" style="margin-top:8px; color:#f87171;">⚠️ Only one version can exist globally.<br>One project breaks.</div>
  </div>
  <div class="project-box good">
    <div class="proj-label">✅ Each project has its own venv</div>
    <div class="proj-name">project-a/venv</div>
    <div class="pkg"><span class="pkg-ok">flask==2.0</span> · isolated</div>
    <div class="proj-name" style="margin-top:10px">project-b/venv</div>
    <div class="pkg"><span class="pkg-ok">flask==3.1</span> · isolated</div>
    <div class="pkg" style="margin-top:8px; color:#86efac;">✓ Both projects work perfectly.<br>No conflicts.</div>
  </div>
</div>

A virtual environment is a self-contained folder with its own Python and its own packages — completely separate from everything else.

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## What a Virtual Environment Is

Think of it as a clean room for each project.

<div class="two-col">
  <div class="col-card">
    <div class="label">Without venv</div>
    <p style="font-size:14px; margin-top:8px;">All packages live in one global pile. Projects share — and fight over — versions. Works until it doesn't.</p>
  </div>
  <div class="col-card">
    <div class="label">✅ With venv</div>
    <p style="font-size:14px; margin-top:8px;">Each project gets its own isolated folder. Install whatever version you need. Nothing bleeds between projects.</p>
  </div>
</div>

&nbsp;

`venv` is built into Python — no installation needed. It creates a folder (usually called `.venv`) that contains a private copy of Python and a private `site-packages` directory for that project's dependencies.

<div class="highlight">

**Rule:** one project folder → one virtual environment. Always.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## venv in 3 Commands

<div class="venv-steps">
  <div class="venv-step">
    <div class="vs-num">01 — Create</div>
    <div class="vs-cmd">python3 -m venv .venv</div>
    <div class="vs-desc">Creates a <code>.venv</code> folder inside your project. Run once per project.</div>
  </div>
  <div class="venv-step">
    <div class="vs-num">02 — Activate</div>
    <div class="vs-cmd">source .venv/bin/activate</div>
    <div class="vs-desc">Switches your terminal into the venv. Run every time you open a new terminal window.</div>
  </div>
  <div class="venv-step">
    <div class="vs-num">03 — Deactivate</div>
    <div class="vs-cmd">deactivate</div>
    <div class="vs-desc">Exits the venv and returns to your global Python. Run when you're done.</div>
  </div>
</div>

**On Windows**, the activate command is slightly different:

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
    <span class="title">zsh — Terminal</span>
  </div>
  <div class="terminal-body">
    <span class="cmt"># Windows CMD:</span><br>
    <span class="prompt">C:\project&gt;</span> <span class="cmd">.venv\Scripts\activate</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## The Full Workflow

From a fresh project folder to a running environment:

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
    <span class="title">zsh — Terminal</span>
  </div>
  <div class="terminal-body">
    <span class="prompt">~ %</span> <span class="cmd">mkdir my-project && cd my-project</span><br>
    <span class="prompt">~/my-project %</span> <span class="cmd">python3 -m venv .venv</span><br>
    <span class="prompt">~/my-project %</span> <span class="cmd">source .venv/bin/activate</span><br>
    <span class="prompt-env">(.venv)</span> <span class="prompt">~/my-project %</span> <span class="cmd">pip install requests flask</span><br>
    <span class="out-g">Successfully installed requests flask ...</span><br>
    <span class="prompt-env">(.venv)</span> <span class="prompt">~/my-project %</span> <span class="cmd">pip freeze > requirements.txt</span><br>
    <span class="cmt"># saves your exact package list for sharing or rebuilding</span>
  </div>
</div>

The `(.venv)` prefix on the prompt confirms the environment is active. **Every `pip install` you run now stays inside this project — nowhere else.**

---

## Why This Habit Matters Early

The earlier you start using venvs, the less you'll suffer later.

<ul class="habit-list">
  <li><span class="hicon">📦</span> <div><strong>requirements.txt</strong> — run <code>pip freeze > requirements.txt</code> to snapshot your dependencies. Anyone can rebuild your exact environment with <code>pip install -r requirements.txt</code>.</div></li>
  <li><span class="hicon">🙈</span> <div><strong>Add .venv to .gitignore</strong> — never commit the venv folder to Git. It's large, machine-specific, and reproducible from requirements.txt.</div></li>
  <li><span class="hicon">🔁</span> <div><strong>Activate every session</strong> — venvs don't auto-activate. Open a terminal, <code>cd</code> into your project, run <code>source .venv/bin/activate</code> before working.</div></li>
  <li><span class="hicon">🚀</span> <div><strong>Every serious project uses this</strong> — tutorials skip it, production never does. Starting the habit now means your code is already structured like a real project.</div></li>
</ul>

---

<!-- _class: final -->

# One venv per project.
# No exceptions.

&nbsp;

It takes 10 seconds to set up and saves hours of debugging broken dependencies.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*