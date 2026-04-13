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

  .url-box {
    background: #111827;
    border-radius: 8px;
    padding: 14px 20px;
    font-family: 'DM Mono', monospace;
    font-size: 15px;
    color: #60a5fa;
    margin: 16px 0;
    display: flex;
    align-items: center;
    gap: 10px;
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

  /* CMD window mock — Windows aesthetic */
  .terminal {
    background: #0c0c0c;
    border-radius: 8px;
    overflow: hidden;
    margin: 16px 0;
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
    padding: 16px 20px;
    line-height: 2;
  }

  .terminal-body .prompt { color: #60a5fa; }
  .terminal-body .cmd    { color: #f9fafb; }
  .terminal-body .out    { color: #9ca3af; }
  .terminal-body .out-w  { color: #fde68a; }
  .terminal-body .cmt    { color: #374151; font-style: italic; }

  /* Command reference grid */
  .cmd-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 12px;
  }

  .cmd-row {
    background: #0c0c0c;
    border-radius: 8px;
    padding: 12px 16px;
    display: flex;
    align-items: flex-start;
    gap: 14px;
  }

  .cmd-row .cmd-name {
    font-family: 'DM Mono', monospace;
    font-size: 14px;
    color: #60a5fa;
    font-weight: 500;
    min-width: 72px;
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

  /* Cheatsheet table */
  .cheat-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
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
    padding: 8px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
  }

  .cheat-table tr:nth-child(even) td { background: var(--off-white); }

  .cheat-table .mono {
    font-family: 'DM Mono', monospace;
    color: var(--blue);
    font-size: 13px;
  }

  /* Two-column layout */
  .two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
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

# Command Prompt for the First Time
## Windows Edition

&nbsp;

**It's just a text interface** to your computer. Nothing to fear.

`dir` · `cd` · `mkdir` · `echo` · `cls`

---

## What is Command Prompt?

It's Windows' built-in text interface — the same idea as Mac's Terminal, different syntax.

<div class="tools">
  <div class="tool-card">
    <div class="icon">🗂️</div>
    <div class="name">File Explorer (GUI)</div>
    <div class="desc">You click folders and drag files. Visual, familiar, slow for dev work.</div>
  </div>
  <div class="tool-card">
    <div class="icon">⌨️</div>
    <div class="name">Command Prompt (CLI)</div>
    <div class="desc">You type commands. Faster for repetitive tasks, required for dev tools.</div>
  </div>
  <div class="tool-card">
    <div class="icon">💙</div>
    <div class="name">PowerShell</div>
    <div class="desc">A more powerful alternative — also built into Windows. Most basic commands are the same.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🚀</div>
    <div class="name">Why learn it</div>
    <div class="desc">Git, Node, Python, and every dev tool runs here. You'll need it eventually.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Opening Command Prompt

Three ways — pick one and remember it:

<ul class="step-list">
  <li><strong>Run dialog</strong> — Press <code>Win + R</code>, type <code>cmd</code>, hit Enter. Fastest.</li>
  <li><strong>Start Menu</strong> — Click Start → type <code>Command Prompt</code> → press Enter</li>
  <li><strong>File Explorer</strong> — Navigate to any folder → click the address bar → type <code>cmd</code> → Enter. Opens directly in that folder.</li>
</ul>

&nbsp;

Once open, you'll see a window like this:

<div class="terminal">
  <div class="terminal-bar">
    <span class="win-title">Command Prompt</span>
    <span class="win-controls"><span>─</span><span>□</span><span>✕</span></span>
  </div>
  <div class="terminal-body">
    <span class="out">Microsoft Windows [Version 11.0.22631]</span><br>
    <span class="out">(c) Microsoft Corporation. All rights reserved.</span><br>
    <br>
    <span class="prompt">C:\Users\Julius&gt;</span> <span class="cmd">█</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## 8 Essential Commands

<div class="cmd-grid">
  <div class="cmd-row">
    <div class="cmd-name">cd</div>
    <div class="cmd-desc">Change directory<span>cd Documents · cd .. to go back</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">dir</div>
    <div class="cmd-desc">List files and folders<span>Like ls on Mac</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">mkdir</div>
    <div class="cmd-desc">Make a new folder<span>mkdir my-project</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">echo</div>
    <div class="cmd-desc">Print text or create a file<span>echo. > index.html</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">cls</div>
    <div class="cmd-desc">Clear the screen<span>Like clear on Mac</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">del</div>
    <div class="cmd-desc">Delete a file permanently<span>⚠️ No Recycle Bin — gone for good</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">start .</div>
    <div class="cmd-desc">Open folder in File Explorer<span>Like open . on Mac</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">type</div>
    <div class="cmd-desc">Print file contents to screen<span>type index.html</span></div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## See Them in Action

<div class="terminal">
  <div class="terminal-bar">
    <span class="win-title">Command Prompt</span>
    <span class="win-controls"><span>─</span><span>□</span><span>✕</span></span>
  </div>
  <div class="terminal-body">
    <span class="prompt">C:\Users\Julius&gt;</span> <span class="cmd">mkdir my-website</span><br>
    <span class="prompt">C:\Users\Julius&gt;</span> <span class="cmd">cd my-website</span><br>
    <span class="prompt">C:\Users\Julius\my-website&gt;</span> <span class="cmd">echo. > index.html</span><br>
    <span class="prompt">C:\Users\Julius\my-website&gt;</span> <span class="cmd">dir</span><br>
    <span class="out"> Directory of C:\Users\Julius\my-website</span><br>
    <span class="out-w"> 13/04/2026 &nbsp;index.html &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 bytes</span><br>
    <span class="prompt">C:\Users\Julius\my-website&gt;</span> <span class="cmd">start .</span><br>
    <span class="cmt">:: File Explorer opens — index.html is right there</span>
  </div>
</div>

In 5 commands: made a folder, entered it, created a file, listed it, opened it in Explorer.

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Tab Autocomplete

Works the same way as Mac Terminal — and just as essential.

<div class="two-col">
  <div class="col-card">
    <div class="label">Without Tab</div>
    <p style="font-size:14px; margin-top:8px;">Type the full path every time:</p>
    <p style="font-family:'DM Mono',monospace; font-size:13px; color:#2563eb; margin-top:8px;">cd Documents\Projects\my-website</p>
  </div>
  <div class="col-card">
    <div class="label">✅ With Tab</div>
    <p style="font-size:14px; margin-top:8px;">Type a few letters, press <code>Tab</code>:</p>
    <p style="font-family:'DM Mono',monospace; font-size:13px; color:#2563eb; margin-top:8px;">cd Doc<kbd style="background:#e5e7eb;padding:1px 5px;border-radius:3px;color:#111827;font-size:11px;">Tab</kbd> → fills in automatically</p>
  </div>
</div>

&nbsp;

- Press `Tab` repeatedly to **cycle through** all matches
- Works for folder names, file names, and paths
- On CMD, backslash `\` is the path separator — not forward slash `/`

<div class="highlight">

**Rule:** Never type a full path from memory. Type 3 letters, hit Tab.

</div>

---

## Don't Panic Cheatsheet

<table class="cheat-table">
  <tr>
    <th>Command</th>
    <th>What it does</th>
    <th>Example</th>
  </tr>
  <tr>
    <td class="mono">dir</td>
    <td>List files in folder</td>
    <td class="mono">dir</td>
  </tr>
  <tr>
    <td class="mono">cd [folder]</td>
    <td>Enter a folder</td>
    <td class="mono">cd Documents</td>
  </tr>
  <tr>
    <td class="mono">cd ..</td>
    <td>Go up one level</td>
    <td class="mono">cd ..</td>
  </tr>
  <tr>
    <td class="mono">mkdir [name]</td>
    <td>Create a folder</td>
    <td class="mono">mkdir my-site</td>
  </tr>
  <tr>
    <td class="mono">echo. > [file]</td>
    <td>Create an empty file</td>
    <td class="mono">echo. > index.html</td>
  </tr>
  <tr>
    <td class="mono">start .</td>
    <td>Open folder in Explorer</td>
    <td class="mono">start .</td>
  </tr>
  <tr>
    <td class="mono">cls</td>
    <td>Clear the screen</td>
    <td class="mono">cls</td>
  </tr>
  <tr>
    <td class="mono">Tab</td>
    <td>Autocomplete — cycle matches</td>
    <td class="mono">cd Doc → Tab</td>
  </tr>
  <tr>
    <td class="mono">Ctrl + C</td>
    <td>Stop whatever is running</td>
    <td>Escape hatch — always works</td>
  </tr>
</table>

---

<!-- _class: final -->

# The Black Window
# isn't scary.

&nbsp;

It's just File Explorer — with a keyboard instead of a mouse.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*