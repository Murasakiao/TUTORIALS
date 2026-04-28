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

  /* CMD window mock */
  .terminal {
    background: #0c0c0c;
    border-radius: 8px;
    overflow: hidden;
    margin: 12px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .terminal-bar {
    background: #1f1f1f;
    padding: 8px 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .terminal-bar .win-title {
    font-size: 12px;
    color: #9ca3af;
    letter-spacing: 0.03em;
  }

  .terminal-bar .win-controls {
    display: flex;
    gap: 16px;
    font-size: 13px;
    color: #6b7280;
  }

  .terminal-body {
    padding: 14px 20px;
    line-height: 2;
  }

  .terminal-body .prompt { color: #60a5fa; }
  .terminal-body .cmd    { color: #f9fafb; }
  .terminal-body .out    { color: #9ca3af; }
  .terminal-body .out-g  { color: #86efac; }
  .terminal-body .out-y  { color: #fde68a; }
  .terminal-body .repl   { color: #c4b5fd; }
  .terminal-body .cmt    { color: #374151; font-style: italic; }

  /* Installer mock */
  .installer {
    background: #f3f4f6;
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
    margin: 16px 0;
  }

  .installer-bar {
    background: #1d4ed8;
    padding: 8px 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .installer-bar .inst-title {
    font-size: 13px;
    color: white;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
  }

  .installer-bar .inst-controls {
    display: flex;
    gap: 12px;
    font-size: 13px;
    color: #bfdbfe;
  }

  .installer-body {
    padding: 18px 24px;
    font-size: 14px;
    color: var(--text);
  }

  .installer-body .checkbox-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
  }

  .checkbox {
    width: 16px;
    height: 16px;
    border: 2px solid #6b7280;
    border-radius: 3px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    font-size: 11px;
    background: white;
  }

  .checkbox.checked {
    background: #2563eb;
    border-color: #2563eb;
    color: white;
  }

  .checkbox-row.critical {
    background: #fef9c3;
    border: 1px solid #fde047;
    border-radius: 6px;
    padding: 8px 10px;
  }

  .checkbox-row.critical .checkbox-label {
    font-weight: 600;
    color: #92400e;
  }

  /* pip card grid */
  .pip-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .pip-card {
    background: #0c0c0c;
    border-radius: 8px;
    padding: 14px 16px;
  }

  .pip-card .pip-cmd {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #60a5fa;
    font-weight: 500;
    margin-bottom: 6px;
  }

  .pip-card .pip-desc {
    font-size: 12px;
    color: #9ca3af;
    line-height: 1.5;
  }

  /* Two-column layout */
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

# How to Install Python
## on Windows

&nbsp;

**One checkbox** stands between you and a working install. Don't skip it.

`python.org` · `PATH` · `pip` · `hello world`

---

## Why Python?

Python is the most beginner-friendly language that also scales to professional work.

<div class="tools">
  <div class="tool-card">
    <div class="icon">🤖</div>
    <div class="name">AI & Automation</div>
    <div class="desc">Every AI library — OpenAI, LangChain, Pandas — runs on Python.</div>
  </div>
  <div class="tool-card">
    <div class="icon">📊</div>
    <div class="name">Data & Analysis</div>
    <div class="desc">The standard language for data science, scraping, and spreadsheet automation.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🌐</div>
    <div class="name">Web Backends</div>
    <div class="desc">Flask and Django let you build web apps and APIs quickly.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔰</div>
    <div class="name">Readable Syntax</div>
    <div class="desc">Closest to plain English of any language. The best first language to learn.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Download from python.org

<ul class="step-list">
  <li>Go to <strong>python.org/downloads</strong></li>
  <li>Click the big yellow <strong>"Download Python 3.x.x"</strong> button — it auto-detects Windows</li>
  <li>Run the downloaded <code>.exe</code> installer</li>
  <li>You'll see the setup screen — <strong>stop before clicking Install Now</strong></li>
</ul>

&nbsp;

<div class="highlight">

**Which version?** Always pick the latest **3.x** release shown on the homepage. Never install Python 2 — it's been retired since 2020.

</div>

---

<!-- _class: step -->

<div class="warn-badge">⚠️ CRITICAL STEP</div>

## The One Checkbox That Breaks Everything

Before you click anything, look at the bottom of the installer screen:

<div class="installer">
  <div class="installer-bar">
    <span class="inst-title">Python 3.13.2 (64-bit) Setup</span>
    <span class="inst-controls"><span>─</span><span>□</span><span>✕</span></span>
  </div>
  <div class="installer-body">
    <div class="checkbox-row">
      <span class="checkbox checked">✓</span>
      <span class="checkbox-label" style="color:#374151;">Use admin privileges when installing py.exe</span>
    </div>
    <div class="checkbox-row critical">
      <span class="checkbox checked">✓</span>
      <span class="checkbox-label">Add python.exe to PATH &nbsp;← CHECK THIS. Always.</span>
    </div>
    <br>
    <div style="display:flex; gap:12px; margin-top:4px;">
      <div style="background:#2563eb;color:white;padding:6px 18px;border-radius:4px;font-size:13px;font-weight:600;">Install Now</div>
      <div style="background:#e5e7eb;color:#374151;padding:6px 18px;border-radius:4px;font-size:13px;">Customize installation</div>
    </div>
  </div>
</div>

**Add python.exe to PATH** tells Windows where to find Python. Without it, every command returns `'python' is not recognized`.

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Complete the Installation

With the PATH checkbox ticked, proceed:

<ul class="step-list">
  <li>Click <strong>Install Now</strong> — default options are fine</li>
  <li>Click <strong>Yes</strong> if Windows asks for permission (UAC prompt)</li>
  <li>Wait for the progress bar to complete</li>
  <li>On the final screen, click <strong>"Disable path length limit"</strong> if offered — then Close</li>
</ul>

&nbsp;

<div class="highlight warn">

**Forgot the checkbox?** Uninstall Python from Settings → Apps, then reinstall with the box ticked. There's no clean way to add PATH manually as a beginner — a reinstall takes 2 minutes and is far easier.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Verify in CMD

Open a **new** Command Prompt window after installing — old windows won't see the updated PATH:

<div class="terminal">
  <div class="terminal-bar">
    <span class="win-title">Command Prompt</span>
    <span class="win-controls"><span>─</span><span>□</span><span>✕</span></span>
  </div>
  <div class="terminal-body">
    <span class="prompt">C:\Users\Julius&gt;</span> <span class="cmd">python --version</span><br>
    <span class="out-g">Python 3.13.2</span><br>
    <br>
    <span class="prompt">C:\Users\Julius&gt;</span> <span class="cmd">pip --version</span><br>
    <span class="out-g">pip 24.x.x from C:\Users\Julius\AppData\...</span>
  </div>
</div>

<div class="two-col">
  <div class="col-card">
    <div class="label">✅ Got version numbers?</div>
    <p style="font-size:14px; margin-top:6px;">Python and pip are both working. Move on to the next slide.</p>
  </div>
  <div class="col-card">
    <div class="label">❌ 'python' not recognized?</div>
    <p style="font-size:14px; margin-top:6px;">PATH wasn't set. Reinstall with the checkbox ticked — previous slide.</p>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 04</div>

## Run Your First Python Program

Two modes — interactive and script file.

**Interactive mode** — type Python directly in CMD:

<div class="terminal">
  <div class="terminal-bar">
    <span class="win-title">Command Prompt</span>
    <span class="win-controls"><span>─</span><span>□</span><span>✕</span></span>
  </div>
  <div class="terminal-body">
    <span class="prompt">C:\Users\Julius&gt;</span> <span class="cmd">python</span><br>
    <span class="out">Python 3.13.2 on win32</span><br>
    <span class="repl">>>></span> <span class="cmd">print("hello world")</span><br>
    <span class="out-g">hello world</span><br>
    <span class="repl">>>></span> <span class="cmd">exit()</span> &nbsp;<span class="cmt">:: leave interactive mode</span>
  </div>
</div>

**Script file** — write `print("hello world")` in a file called `hello.py`, then:

<div class="terminal">
  <div class="terminal-bar">
    <span class="win-title">Command Prompt</span>
    <span class="win-controls"><span>─</span><span>□</span><span>✕</span></span>
  </div>
  <div class="terminal-body">
    <span class="prompt">C:\Users\Julius&gt;</span> <span class="cmd">python hello.py</span><br>
    <span class="out-g">hello world</span>
  </div>
</div>

---

## Bonus: What is pip?

`pip` is Python's package manager — it installs libraries written by other developers.

<div class="pip-grid">
  <div class="pip-card">
    <div class="pip-cmd">pip install requests</div>
    <div class="pip-desc">Install a package from the internet</div>
  </div>
  <div class="pip-card">
    <div class="pip-cmd">pip list</div>
    <div class="pip-desc">See all installed packages</div>
  </div>
  <div class="pip-card">
    <div class="pip-cmd">pip uninstall X</div>
    <div class="pip-desc">Remove a package</div>
  </div>
</div>

&nbsp;

- On Windows, use `pip` — not `pip3` like on Mac
- Think of it like the App Store, but for Python code
- Most tutorials say `pip install [something]` — run that in CMD and it just works

<div class="highlight">

**First packages worth knowing:** `requests` (fetch web data) · `flask` (build web apps) · `pandas` (work with data)

</div>

---

<!-- _class: final -->

# Python is installed.
# Now use it.

&nbsp;

Every AI tool, automation script, and data project starts here.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*