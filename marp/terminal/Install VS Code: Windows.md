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

  /* Extension cards */
  .ext-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 12px;
  }

  .ext-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 18px;
    display: flex;
    align-items: flex-start;
    gap: 14px;
  }

  .ext-card .ext-icon {
    font-size: 26px;
    flex-shrink: 0;
    margin-top: 2px;
  }

  .ext-card .ext-name {
    font-weight: 600;
    font-size: 14px;
    color: var(--text);
  }

  .ext-card .ext-id {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--blue);
    margin-top: 2px;
  }

  .ext-card .ext-desc {
    font-size: 12.5px;
    color: var(--muted);
    margin-top: 4px;
    line-height: 1.4;
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

# VS Code for the First Time
## Windows Edition

&nbsp;

**The editor everyone uses.** Here's how to set it up properly.

`download` · `install` · `extensions` · `theme` · `shortcuts`

---

## Why VS Code?

It's free, fast, and runs everything — from HTML files to full Python projects.

<div class="tools">
  <div class="tool-card">
    <div class="icon">🆓</div>
    <div class="name">Free forever</div>
    <div class="desc">Made by Microsoft, open source. No subscriptions, no paywalls.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🧩</div>
    <div class="name">Extensions</div>
    <div class="desc">Add support for any language or tool in two clicks from the marketplace.</div>
  </div>
  <div class="tool-card">
    <div class="icon">⚡</div>
    <div class="name">Fast & lightweight</div>
    <div class="desc">Opens instantly. Handles single files and huge projects equally well.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🖥️</div>
    <div class="name">Built-in Terminal</div>
    <div class="desc">Run PowerShell or CMD without leaving the editor. Code and terminal, side by side.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Download & Install

<ul class="step-list">
  <li>Go to <strong>code.visualstudio.com</strong> — click the big blue Download button. It auto-detects Windows and offers a <code>.exe</code> installer.</li>
  <li>Run the installer. When prompted, check <strong>"Add to PATH"</strong> and <strong>"Add Open with Code to context menu"</strong> — both are worth enabling.</li>
  <li>Also check <strong>"Register Code as an editor for supported file types"</strong> so VS Code opens code files by default.</li>
  <li>Click through the rest and hit <strong>Install</strong>. Launch VS Code when the installer finishes.</li>
</ul>

<div class="highlight">

**After install:** Open a new Command Prompt or PowerShell and run <code>code .</code> in any folder to open it in VS Code instantly. If the command isn't found, restart your PC — PATH changes need a fresh session.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Install 5 Essential Extensions

Open the Extensions panel with `Ctrl Shift X`, then search by name.

<div class="ext-grid">
  <div class="ext-card">
    <div class="ext-icon">🎨</div>
    <div>
      <div class="ext-name">Prettier</div>
      <div class="ext-id">esbenp.prettier-vscode</div>
      <div class="ext-desc">Auto-formats your code on save. Never argue about indentation again.</div>
    </div>
  </div>
  <div class="ext-card">
    <div class="ext-icon">🔍</div>
    <div>
      <div class="ext-name">ESLint</div>
      <div class="ext-id">dbaeumer.vscode-eslint</div>
      <div class="ext-desc">Underlines JS/TS mistakes in real time before you even run the code.</div>
    </div>
  </div>
  <div class="ext-card">
    <div class="ext-icon">🌈</div>
    <div>
      <div class="ext-name">indent-rainbow</div>
      <div class="ext-id">oderwat.indent-rainbow</div>
      <div class="ext-desc">Colors each indentation level. Instantly spot misaligned blocks.</div>
    </div>
  </div>
  <div class="ext-card">
    <div class="ext-icon">📁</div>
    <div>
      <div class="ext-name">Material Icon Theme</div>
      <div class="ext-id">pkief.material-icon-theme</div>
      <div class="ext-desc">Adds file-type icons to the sidebar. Makes navigating projects much faster.</div>
    </div>
  </div>
  <div class="ext-card">
    <div class="ext-icon">🤖</div>
    <div>
      <div class="ext-name">GitHub Copilot</div>
      <div class="ext-id">github.copilot</div>
      <div class="ext-desc">AI autocomplete for code. Free for students, paid otherwise — worth it.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Change Your Theme

The default theme is fine. These are better.

<div class="two-col">
  <div class="col-card">
    <div class="label">How to change it</div>
    <p style="font-size:14px; margin-top:8px;">Press <code>Ctrl K</code> then <code>Ctrl T</code> to open the theme picker. Arrow keys preview in real time.</p>
  </div>
  <div class="col-card">
    <div class="label">Or via Command Palette</div>
    <p style="font-size:14px; margin-top:8px;">Press <code>Ctrl Shift P</code>, type <code>color theme</code>, hit Enter.</p>
  </div>
</div>

&nbsp;

<div class="cmd-grid">
  <div class="cmd-row">
    <div class="cmd-name">One Dark Pro</div>
    <div class="cmd-desc">Most popular dark theme<span>zhuangtongfa.material-theme</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">GitHub Dark</div>
    <div class="cmd-desc">Clean, familiar from GitHub<span>github.github-vscode-theme</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">Catppuccin</div>
    <div class="cmd-desc">Soft pastel dark theme<span>catppuccin.catppuccin-vsc</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">Solarized Light</div>
    <div class="cmd-desc">Best light theme, built-in<span>no install needed</span></div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 04</div>

## Enable Autosave

VS Code does **not** autosave by default. Fix this immediately.

<div class="two-col">
  <div class="col-card">
    <div class="label">Option A — Menu</div>
    <p style="font-size:14px; margin-top:8px;">Go to <strong>File → Auto Save</strong>. One click. Done. A checkmark appears when it's on.</p>
  </div>
  <div class="col-card">
    <div class="label">Option B — Settings</div>
    <p style="font-size:14px; margin-top:8px;">Press <code>Ctrl ,</code> to open Settings. Search <code>autosave</code>. Set to <strong>afterDelay</strong> (1000ms default).</p>
  </div>
</div>

&nbsp;

The dot on the tab means **unsaved changes**. Once autosave is on, you'll never see it again.

<div class="highlight">

**Recommended setting:** `afterDelay` at 1000ms — saves one second after you stop typing. Fast enough to feel instant, without saving every single keystroke.

</div>

---

## Key Shortcuts Cheatsheet

<table class="cheat-table">
  <tr>
    <th>Shortcut</th>
    <th>What it does</th>
    <th>When to use it</th>
  </tr>
  <tr>
    <td class="mono">Ctrl P</td>
    <td>Quick Open — find any file</td>
    <td>Jump between files instantly</td>
  </tr>
  <tr>
    <td class="mono">Ctrl Shift P</td>
    <td>Command Palette</td>
    <td>Run any VS Code command by name</td>
  </tr>
  <tr>
    <td class="mono">Ctrl `</td>
    <td>Toggle integrated Terminal</td>
    <td>Run commands without leaving VS Code</td>
  </tr>
  <tr>
    <td class="mono">Ctrl B</td>
    <td>Toggle sidebar</td>
    <td>More screen space when coding</td>
  </tr>
  <tr>
    <td class="mono">Ctrl \</td>
    <td>Split editor</td>
    <td>View two files side by side</td>
  </tr>
  <tr>
    <td class="mono">Ctrl Shift F</td>
    <td>Search across all files</td>
    <td>Find anything in the whole project</td>
  </tr>
  <tr>
    <td class="mono">Ctrl D</td>
    <td>Select next occurrence</td>
    <td>Multi-cursor rename in one go</td>
  </tr>
  <tr>
    <td class="mono">Ctrl Z / Ctrl Y</td>
    <td>Undo / Redo</td>
    <td>Your safety net — always works</td>
  </tr>
  <tr>
    <td class="mono">Ctrl /</td>
    <td>Toggle line comment</td>
    <td>Comment out code in any language</td>
  </tr>
  <tr>
    <td class="mono">Ctrl Shift X</td>
    <td>Open Extensions panel</td>
    <td>Install, manage, disable extensions</td>
  </tr>
</table>

---

<!-- _class: final -->

# VS Code is ready.
# Start building.

&nbsp;

You've got the editor, the extensions, and the shortcuts.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*