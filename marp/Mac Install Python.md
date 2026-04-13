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

  /* Terminal window mock */
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

  .terminal-body .prompt { color: #22c55e; }
  .terminal-body .cmd    { color: #f9fafb; }
  .terminal-body .out    { color: #9ca3af; }
  .terminal-body .out-g  { color: #86efac; }
  .terminal-body .out-y  { color: #fde68a; }
  .terminal-body .out-b  { color: #60a5fa; }
  .terminal-body .repl   { color: #c4b5fd; }
  .terminal-body .cmt    { color: #4b5563; font-style: italic; }

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

  /* pip card grid */
  .pip-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .pip-card {
    background: #111827;
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
---

<!-- _class: cover -->

# How to Install Python
## on Mac

&nbsp;

**The right way** — using Homebrew, not the website installer.

`python3` · `homebrew` · `pip` · `hello world`

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

## Check if Python is Already Installed

Macs often ship with a system Python. Open Terminal first and check:

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
    <span class="title">zsh — Terminal</span>
  </div>
  <div class="terminal-body">
    <span class="prompt">~ %</span> <span class="cmd">python3 --version</span><br>
    <span class="out-g">Python 3.x.x</span> &nbsp;<span class="cmt"># already installed — you may be done</span><br>
    <br>
    <span class="cmt"># or you might see:</span><br>
    <span class="out-y">command not found: python3</span> &nbsp;<span class="cmt"># needs installing</span>
  </div>
</div>

<div class="two-col">
  <div class="col-card">
    <div class="label">✅ Got a version number?</div>
    <p style="font-size:14px; margin-top:6px;">If it's <strong>3.10 or higher</strong>, you're good. Skip ahead to the verify slide.</p>
  </div>
  <div class="col-card">
    <div class="label">⚠️ Got an error or old version?</div>
    <p style="font-size:14px; margin-top:6px;">Continue to the next slide — we'll install it properly via Homebrew.</p>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Install via Homebrew

Homebrew is Mac's package manager — the cleanest way to install developer tools.

**First, install Homebrew** (skip if you already have it):

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
    <span class="title">zsh — Terminal</span>
  </div>
  <div class="terminal-body">
    <span class="prompt">~ %</span> <span class="cmd">/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"</span><br>
    <span class="cmt"># follow the prompts — it will ask for your Mac password</span>
  </div>
</div>

**Then install Python:**

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
    <span class="title">zsh — Terminal</span>
  </div>
  <div class="terminal-body">
    <span class="prompt">~ %</span> <span class="cmd">brew install python</span><br>
    <span class="out">==> Downloading python...</span><br>
    <span class="out-g">==> Installation successful!</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Verify the Installation

Confirm the right Python is active after Homebrew finishes:

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
    <span class="title">zsh — Terminal</span>
  </div>
  <div class="terminal-body">
    <span class="prompt">~ %</span> <span class="cmd">python3 --version</span><br>
    <span class="out-g">Python 3.13.2</span><br>
    <br>
    <span class="prompt">~ %</span> <span class="cmd">which python3</span><br>
    <span class="out-b">/opt/homebrew/bin/python3</span> &nbsp;<span class="cmt"># Homebrew path — correct</span>
  </div>
</div>

<div class="highlight">

**The path tells the story.** `/opt/homebrew/bin/python3` means you're running Homebrew's version — newer and easier to update. `/usr/bin/python3` is the older system version. Both work, but Homebrew's is preferred for dev work.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 04</div>

## Run Your First Python Program

Two modes to know — interactive and script.

**Interactive mode** — type Python directly in the terminal:

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
    <span class="title">zsh — Terminal</span>
  </div>
  <div class="terminal-body">
    <span class="prompt">~ %</span> <span class="cmd">python3</span><br>
    <span class="out">Python 3.13.2 (main) [Clang] on darwin</span><br>
    <span class="repl">>>></span> <span class="cmd">print("hello world")</span><br>
    <span class="out-g">hello world</span><br>
    <span class="repl">>>></span> <span class="cmd">exit()</span> &nbsp;<span class="cmt"># leave interactive mode</span>
  </div>
</div>

**Script mode** — write `print("hello world")` in a file called `hello.py`, then:

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
    <span class="title">zsh — Terminal</span>
  </div>
  <div class="terminal-body">
    <span class="prompt">~ %</span> <span class="cmd">python3 hello.py</span><br>
    <span class="out-g">hello world</span>
  </div>
</div>

---

## Bonus: What is pip?

`pip3` is Python's package manager — it installs libraries written by other developers.

<div class="pip-grid">
  <div class="pip-card">
    <div class="pip-cmd">pip3 install requests</div>
    <div class="pip-desc">Install a package from the internet</div>
  </div>
  <div class="pip-card">
    <div class="pip-cmd">pip3 list</div>
    <div class="pip-desc">See all installed packages</div>
  </div>
  <div class="pip-card">
    <div class="pip-cmd">pip3 uninstall X</div>
    <div class="pip-desc">Remove a package</div>
  </div>
</div>

&nbsp;

- Think of `pip3` like the App Store — but for Python code
- Most tutorials say `pip install [something]` — on Mac with Homebrew, use `pip3`
- Packages extend Python with capabilities you'd otherwise write yourself

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