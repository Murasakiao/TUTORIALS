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

  /* Platform two-column */
  .platform-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 16px;
  }

  .platform-card {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .platform-card .platform-header {
    padding: 10px 16px;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    letter-spacing: 0.06em;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .platform-card.mac .platform-header {
    background: #1f2937;
    color: #9ca3af;
  }

  .platform-card.win .platform-header {
    background: #1e3a5f;
    color: #93c5fd;
  }

  .platform-card .platform-body {
    background: #111827;
    padding: 14px 18px;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    line-height: 2;
  }

  .platform-card .platform-body .prompt { color: #22c55e; }
  .platform-card .platform-body .wprompt { color: #60a5fa; }
  .platform-card .platform-body .cmd    { color: #f9fafb; }
  .platform-card .platform-body .out    { color: #9ca3af; }
  .platform-card .platform-body .cmt    { color: #4b5563; font-style: italic; }

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

  /* Ignore file example */
  .ignore-box {
    background: #111827;
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .ignore-box .ignore-bar {
    background: #1f2937;
    padding: 8px 16px;
    font-size: 12px;
    color: #6b7280;
    letter-spacing: 0.04em;
  }

  .ignore-box .ignore-body {
    padding: 14px 20px;
    line-height: 2;
  }

  .ignore-box .ig-cmt  { color: #4b5563; font-style: italic; }
  .ignore-box .ig-rule { color: #f9fafb; }
  .ignore-box .ig-dir  { color: #60a5fa; }
  .ignore-box .ig-ext  { color: #34d399; }
---

<!-- _class: cover -->

# Git for the First Time
## Mac & Windows Edition

&nbsp;

**Version control for humans.** Set it up once, use it forever.

`git init` · `git add` · `git commit` · `git push` · `git status`

---

## What Git Is (and Isn't)

Git is a tool that **saves snapshots of your work** so you can go back in time, or collaborate without overwriting each other.

<div class="tools">
  <div class="tool-card">
    <div class="icon">📸</div>
    <div class="name">Git = snapshots</div>
    <div class="desc">Every commit is a saved state you can return to. Like unlimited undo for your entire project.</div>
  </div>
  <div class="tool-card">
    <div class="icon">☁️</div>
    <div class="name">GitHub ≠ Git</div>
    <div class="desc">Git runs on your computer. GitHub is a website that stores your Git history online. They're different things.</div>
  </div>
  <div class="tool-card">
    <div class="icon">📂</div>
    <div class="name">It's just a folder</div>
    <div class="desc">Git tracks a folder (called a repo). Everything inside it — code, text, configs — is versioned.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🚫</div>
    <div class="name">Not a backup tool</div>
    <div class="desc">Git doesn't auto-save. You decide when to commit. Think of commits as intentional checkpoints, not autosaves.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Install Git

<div class="platform-grid">
  <div class="platform-card mac">
    <div class="platform-header">🍎 &nbsp;macOS</div>
    <div class="platform-body">
      <span class="prompt">~ %</span> <span class="cmd">git --version</span><br>
      <span class="out">git version 2.39.3 (Apple Git-145)</span><br>
      <span class="cmt"># Already installed on most Macs.</span><br>
      <span class="cmt"># If not, macOS will prompt you to</span><br>
      <span class="cmt"># install Xcode Command Line Tools.</span><br>
      <span class="cmt"># Click Install and wait ~5 min.</span>
    </div>
  </div>
  <div class="platform-card win">
    <div class="platform-header">🪟 &nbsp;Windows</div>
    <div class="platform-body">
      <span class="cmt"># Go to git-scm.com/download/win</span><br>
      <span class="cmt"># Run the installer. Keep all</span><br>
      <span class="cmt"># defaults — they're sensible.</span><br>
      <span class="cmt"># This also installs Git Bash,</span><br>
      <span class="cmt"># a terminal that understands</span><br>
      <span class="cmt"># Unix commands. Use that.</span>
    </div>
  </div>
</div>

<div class="highlight">

**Verify it worked:** Open Terminal (Mac) or Git Bash (Windows) and run `git --version`. If you see a version number, you're good.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Configure Your Name & Email

Git stamps every commit with your name and email. Do this once — it applies globally to all your projects.

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span>
    <span class="dot yellow"></span>
    <span class="dot green"></span>
    <span class="title">Terminal / Git Bash — same commands on both platforms</span>
  </div>
  <div class="terminal-body">
    <span class="cmt"># Set your name</span><br>
    <span class="prompt">~ %</span> <span class="cmd">git config --global user.name "Your Name"</span><br>
    <span class="cmt"># Set your email — use the same one as your GitHub account</span><br>
    <span class="prompt">~ %</span> <span class="cmd">git config --global user.email "you@example.com"</span><br>
    <span class="cmt"># Verify both are saved</span><br>
    <span class="prompt">~ %</span> <span class="cmd">git config --list</span><br>
    <span class="out">user.name=Your Name</span><br>
    <span class="out">user.email=you@example.com</span>
  </div>
</div>

These settings are stored in `~/.gitconfig` and never need to be set again unless you change computers.

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Set Your Default Branch Name

New Git installs may default to `master`. The industry standard is now `main`. Set it once globally.

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span>
    <span class="dot yellow"></span>
    <span class="dot green"></span>
    <span class="title">Terminal / Git Bash</span>
  </div>
  <div class="terminal-body">
    <span class="prompt">~ %</span> <span class="cmd">git config --global init.defaultBranch main</span><br>
    <span class="cmt"># Also set VS Code as your default editor for Git messages</span><br>
    <span class="prompt">~ %</span> <span class="cmd">git config --global core.editor "code --wait"</span>
  </div>
</div>

&nbsp;

On **Windows only** — also set line ending handling so files don't break when shared with Mac users:

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span>
    <span class="dot yellow"></span>
    <span class="dot green"></span>
    <span class="title">Git Bash — Windows only</span>
  </div>
  <div class="terminal-body">
    <span class="wprompt">$</span> <span class="cmd">git config --global core.autocrlf true</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 04</div>

## The 5 Commands You'll Use 90% of the Time

<div class="cmd-grid">
  <div class="cmd-row">
    <div class="cmd-name">git init</div>
    <div class="cmd-desc">Start tracking a folder with Git<span>Run once per project, inside that folder</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">git status</div>
    <div class="cmd-desc">See what's changed since last commit<span>Run this constantly — it's always safe</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">git add .</div>
    <div class="cmd-desc">Stage all changed files for commit<span>The dot means "everything in this folder"</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">git commit -m ""</div>
    <div class="cmd-desc">Save a snapshot with a message<span>git commit -m "add login page"</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">git push</div>
    <div class="cmd-desc">Upload commits to GitHub<span>Requires a remote repo to be linked first</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">git log --oneline</div>
    <div class="cmd-desc">See your commit history, compact<span>Press Q to exit the log view</span></div>
  </div>
</div>

<div class="highlight">

**The everyday loop:** `git status` → `git add .` → `git commit -m "what you did"` → `git push`

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 05</div>

## What `.gitignore` Is

A `.gitignore` file tells Git which files to **never track** — secrets, dependencies, system junk.

<div class="two-col">
  <div class="col-card">
    <div class="label">Why it matters</div>
    <p style="font-size:13.5px; margin-top:8px;">Without it, you might accidentally commit API keys, 300MB of <code>node_modules</code>, or macOS <code>.DS_Store</code> clutter into your repo.</p>
  </div>
  <div class="col-card">
    <div class="label">How to create it</div>
    <p style="font-size:13.5px; margin-top:8px;">Create a file named exactly <code>.gitignore</code> (no extension) in your project root. Add one rule per line.</p>
  </div>
</div>

<div class="ignore-box">
  <div class="ignore-bar">.gitignore — typical starter file</div>
  <div class="ignore-body">
    <span class="ig-cmt"># Dependencies</span><br>
    <span class="ig-dir">node_modules/</span><br>
    <span class="ig-cmt"># Environment variables — never commit these</span><br>
    <span class="ig-ext">.env</span><br>
    <span class="ig-cmt"># macOS system files</span><br>
    <span class="ig-ext">.DS_Store</span><br>
    <span class="ig-cmt"># Windows system files</span><br>
    <span class="ig-ext">Thumbs.db</span><br>
    <span class="ig-cmt"># Build output</span><br>
    <span class="ig-dir">dist/</span>&nbsp;&nbsp;&nbsp;<span class="ig-dir">build/</span>
  </div>
</div>

---

## Git Quick Reference

<table class="cheat-table">
  <tr>
    <th>Command</th>
    <th>What it does</th>
    <th>Notes</th>
  </tr>
  <tr>
    <td class="mono">git init</td>
    <td>Initialize a new repo</td>
    <td>Creates a hidden .git folder</td>
  </tr>
  <tr>
    <td class="mono">git status</td>
    <td>Show changed / untracked files</td>
    <td>Safe to run anytime</td>
  </tr>
  <tr>
    <td class="mono">git add .</td>
    <td>Stage everything for commit</td>
    <td>Use <code>git add filename</code> for one file</td>
  </tr>
  <tr>
    <td class="mono">git commit -m ""</td>
    <td>Save a snapshot</td>
    <td>Write a clear, present-tense message</td>
  </tr>
  <tr>
    <td class="mono">git push</td>
    <td>Upload to GitHub</td>
    <td>Need <code>git remote add origin</code> first</td>
  </tr>
  <tr>
    <td class="mono">git pull</td>
    <td>Download latest from GitHub</td>
    <td>Always pull before you push on a team</td>
  </tr>
  <tr>
    <td class="mono">git log --oneline</td>
    <td>See commit history</td>
    <td>Press Q to exit</td>
  </tr>
  <tr>
    <td class="mono">git diff</td>
    <td>See exact line changes</td>
    <td>Before staging — what changed?</td>
  </tr>
  <tr>
    <td class="mono">git clone [url]</td>
    <td>Download a repo from GitHub</td>
    <td>No init needed — cloning does it</td>
  </tr>
  <tr>
    <td class="mono">git config --list</td>
    <td>Check your Git settings</td>
    <td>Verify name, email, editor</td>
  </tr>
</table>

---

<!-- _class: final -->

# Git is set up.
# Your work is now saved forever.

&nbsp;

Commit early, commit often. Messages to your future self.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*