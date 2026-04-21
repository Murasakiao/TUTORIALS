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

  /* Terminal window mock */
  .terminal {
    background: #111827;
    border-radius: 10px;
    overflow: hidden;
    margin: 16px 0;
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
    letter-spacing: 0.04em;
  }

  .terminal-body {
    padding: 16px 20px;
    line-height: 2;
  }

  .terminal-body .prompt { color: #22c55e; }
  .terminal-body .cmd    { color: #f9fafb; }
  .terminal-body .out    { color: #9ca3af; }
  .terminal-body .cmt    { color: #4b5563; font-style: italic; }

  /* Command reference grid */
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

# Terminal for the First Time
## Mac Edition

&nbsp;

**It's just a text interface** to your computer. Nothing to fear.

`ls` · `cd` · `mkdir` · `pwd` · `rm`

---

## What is Terminal?

Terminal is a window where you talk to your Mac using text commands instead of clicks.

<div class="tools">
  <div class="tool-card">
    <div class="icon">🖱️</div>
    <div class="name">Finder (GUI)</div>
    <div class="desc">You click folders and drag files. Visual, intuitive, slow for repetitive tasks.</div>
  </div>
  <div class="tool-card">
    <div class="icon">⌨️</div>
    <div class="name">Terminal (CLI)</div>
    <div class="desc">You type commands. Faster, scriptable, and required for most developer tools.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔧</div>
    <div class="name">Same computer</div>
    <div class="desc">Terminal doesn't do anything Finder can't — it just does it in text form.</div>
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

## Opening Terminal

Three ways to open it — pick one and remember it:

<ul class="step-list">
  <li><strong>Spotlight Search</strong> — Press <code>⌘ Space</code>, type <code>Terminal</code>, hit Enter. Fastest.</li>
  <li><strong>Finder</strong> — Go to Applications → Utilities → Terminal.app</li>
  <li><strong>Dock</strong> — If you've opened it before, right-click the icon → Keep in Dock</li>
</ul>

&nbsp;

Once open, you'll see something like this:

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span>
    <span class="dot yellow"></span>
    <span class="dot green"></span>
    <span class="title">bash — 80×24</span>
  </div>
  <div class="terminal-body">
    <span class="prompt">julius@macbook ~ %</span> <span class="cmd">█</span>
  </div>
</div>

That blinking cursor is waiting for your first command.

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## 8 Essential Commands

<div class="cmd-grid">
  <div class="cmd-row">
    <div class="cmd-name">pwd</div>
    <div class="cmd-desc">Print working directory<span>Where am I right now?</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">ls</div>
    <div class="cmd-desc">List files and folders<span>What's in this folder?</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">cd</div>
    <div class="cmd-desc">Change directory<span>cd Documents · cd .. to go back</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">mkdir</div>
    <div class="cmd-desc">Make a new folder<span>mkdir my-project</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">touch</div>
    <div class="cmd-desc">Create a new empty file<span>touch index.html</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">open .</div>
    <div class="cmd-desc">Open current folder in Finder<span>Bridge between CLI and GUI</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">clear</div>
    <div class="cmd-desc">Clear the screen<span>Or press ⌘ K</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">rm</div>
    <div class="cmd-desc">Delete a file permanently<span>⚠️ No Trash — gone for good</span></div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## See Them in Action

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span>
    <span class="dot yellow"></span>
    <span class="dot green"></span>
    <span class="title">zsh — Terminal</span>
  </div>
  <div class="terminal-body">
    <span class="prompt">~ %</span> <span class="cmd">pwd</span><br>
    <span class="out">/Users/julius</span><br>
    <span class="prompt">~ %</span> <span class="cmd">mkdir my-website</span><br>
    <span class="prompt">~ %</span> <span class="cmd">cd my-website</span><br>
    <span class="prompt">~/my-website %</span> <span class="cmd">touch index.html</span><br>
    <span class="prompt">~/my-website %</span> <span class="cmd">ls</span><br>
    <span class="out">index.html</span><br>
    <span class="prompt">~/my-website %</span> <span class="cmd">open .</span><br>
    <span class="cmt"># Finder opens — you can see index.html sitting there</span>
  </div>
</div>

In 6 commands: you found your location, made a folder, entered it, created a file, listed it, and opened it in Finder.

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Tab Autocomplete

The single most useful thing to know about Terminal.

<div class="two-col">
  <div class="col-card">
    <div class="label">Without Tab</div>
    <p style="font-size:14px; margin-top:8px;">Type the full name every time:</p>
    <p style="font-family:'DM Mono',monospace; font-size:13px; color:#2563eb; margin-top:8px;">cd Documents/Projects/my-website</p>
  </div>
  <div class="col-card">
    <div class="label">✅ With Tab</div>
    <p style="font-size:14px; margin-top:8px;">Type a few letters, press <code>Tab</code>:</p>
    <p style="font-family:'DM Mono',monospace; font-size:13px; color:#2563eb; margin-top:8px;">cd Doc<kbd style="background:#e5e7eb;padding:1px 5px;border-radius:3px;color:#111827;font-size:11px;">Tab</kbd> → fills in automatically</p>
  </div>
</div>

&nbsp;

- Press `Tab` once → autocompletes if there's only one match
- Press `Tab` twice → shows all possible matches
- Works for **commands, file names, and folder paths**

<div class="highlight">

**Rule:** Never type a full filename from memory. Type 3 letters, hit Tab.

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
    <td class="mono">pwd</td>
    <td>Show current location</td>
    <td class="mono">pwd</td>
  </tr>
  <tr>
    <td class="mono">ls</td>
    <td>List files in folder</td>
    <td class="mono">ls</td>
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
    <td class="mono">touch [file]</td>
    <td>Create an empty file</td>
    <td class="mono">touch index.html</td>
  </tr>
  <tr>
    <td class="mono">open .</td>
    <td>Open folder in Finder</td>
    <td class="mono">open .</td>
  </tr>
  <tr>
    <td class="mono">clear</td>
    <td>Clear the screen</td>
    <td class="mono">clear</td>
  </tr>
  <tr>
    <td class="mono">Tab</td>
    <td>Autocomplete anything</td>
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

# The Command Line
# isn't scary.

&nbsp;

It's just Finder — with a keyboard instead of a mouse.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*