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

  .highlight.danger {
    background: #fff1f2;
    border-color: #fecdd3;
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
  .terminal-body .out-y   { color: #fde68a; }
  .terminal-body .out-r   { color: #f87171; }
  .terminal-body .cmt     { color: #4b5563; font-style: italic; }

  /* The 3 types oops grid */
  .oops-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 14px;
    margin: 16px 0;
  }

  .oops-card {
    border-radius: 10px;
    padding: 18px 18px;
  }

  .oops-card.type-1 { background: #111827; border: 2px solid #1d4ed8; }
  .oops-card.type-2 { background: #111827; border: 2px solid #92400e; }
  .oops-card.type-3 { background: #111827; border: 2px solid #7f1d1d; }

  .oops-card .oc-icon  { font-size: 26px; margin-bottom: 8px; }

  .oops-card .oc-scenario {
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 6px;
    line-height: 1.4;
  }

  .oops-card.type-1 .oc-scenario { color: #93c5fd; }
  .oops-card.type-2 .oc-scenario { color: #fde68a; }
  .oops-card.type-3 .oc-scenario { color: #fca5a5; }

  .oops-card .oc-fix {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    margin-bottom: 4px;
  }

  .oops-card.type-1 .oc-fix { color: #60a5fa; }
  .oops-card.type-2 .oc-fix { color: #fbbf24; }
  .oops-card.type-3 .oc-fix { color: #f87171; }

  .oops-card .oc-desc {
    font-size: 11px;
    color: #6b7280;
    line-height: 1.5;
    margin-top: 4px;
  }

  /* Commit timeline for reset/revert */
  .commit-timeline {
    background: #111827;
    border-radius: 10px;
    padding: 18px 22px;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .ct-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 8px;
  }

  .ct-dot {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    flex-shrink: 0;
  }

  .ct-dot.blue   { background: #2563eb; border: 2px solid #60a5fa; }
  .ct-dot.green  { background: #14532d; border: 2px solid #86efac; }
  .ct-dot.red    { background: #7f1d1d; border: 2px solid #f87171; }
  .ct-dot.ghost  { background: #111827; border: 2px solid #374151; }

  .ct-line {
    flex: 1;
    height: 2px;
  }

  .ct-line.blue  { background: #2563eb; }
  .ct-line.gray  { background: #374151; }
  .ct-line.dash  { background: repeating-linear-gradient(90deg,#374151 0,#374151 6px,transparent 6px,transparent 12px); }

  .ct-label {
    font-size: 11px;
    white-space: nowrap;
  }

  .ct-label.ok    { color: #86efac; }
  .ct-label.bad   { color: #f87171; }
  .ct-label.undo  { color: #fde68a; }
  .ct-label.ghost { color: #4b5563; }

  /* Decision table */
  .decision-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
    margin: 14px 0;
  }

  .decision-table th {
    background: var(--text);
    color: white;
    padding: 9px 14px;
    text-align: left;
    font-weight: 500;
    font-size: 12px;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.05em;
  }

  .decision-table td {
    padding: 9px 14px;
    border-bottom: 1px solid var(--border);
    font-size: 13px;
    color: var(--text);
    vertical-align: top;
  }

  .decision-table tr:nth-child(even) td { background: var(--off-white); }
  .decision-table .mono { font-family: 'DM Mono', monospace; color: var(--blue); }
  .decision-table .safe   { color: #16a34a; font-weight: 600; }
  .decision-table .unsafe { color: #dc2626; font-weight: 600; }

  /* Cheatsheet table */
  .cheat-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
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
  .cheat-table .mono { font-family: 'DM Mono', monospace; color: var(--blue); font-size: 12px; }
  .cheat-table .safe   { color: #16a34a; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }
  .cheat-table .unsafe { color: #dc2626; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }

  /* two-col */
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

# How to Undo Mistakes in Git
## restore · reset · revert

&nbsp;

**Git doesn't delete history. It gives you a way back.** Learn which tool to reach for.

`git restore` · `git reset` · `git revert`

---

## The 3 Types of "Oops" Moments

Every Git mistake falls into one of three categories.

<div class="oops-grid">
  <div class="oops-card type-1">
    <div class="oc-icon">✏️</div>
    <div class="oc-scenario">I edited a file and haven't committed yet. I want the original back.</div>
    <div class="oc-fix">→ git restore</div>
    <div class="oc-desc">Discards uncommitted changes in your working directory. No commit involved.</div>
  </div>
  <div class="oops-card type-2">
    <div class="oc-icon">📦</div>
    <div class="oc-scenario">I committed something wrong locally. I haven't pushed yet.</div>
    <div class="oc-fix">→ git reset</div>
    <div class="oc-desc">Moves the branch pointer back. Rewrites local history. Safe before pushing.</div>
  </div>
  <div class="oops-card type-3">
    <div class="oc-icon">🌐</div>
    <div class="oc-scenario">I pushed a bad commit to a shared branch. Others may have pulled it.</div>
    <div class="oc-fix">→ git revert</div>
    <div class="oc-desc">Creates a new commit that undoes the bad one. History stays intact. Always safe.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">COMMAND 01</div>

## `git restore` — Discard Uncommitted Changes

You edited a file, it's a mess, and you haven't committed. Throw it away and go back to the last commit.

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
    <span class="title">zsh — Terminal</span>
  </div>
  <div class="terminal-body">
    <span class="cmt"># Restore a single file to its last committed state</span><br>
    <span class="prompt">~/project %</span> <span class="cmd">git restore index.html</span><br>
    <br>
    <span class="cmt"># Restore everything in the working directory</span><br>
    <span class="prompt">~/project %</span> <span class="cmd">git restore .</span><br>
    <br>
    <span class="cmt"># Unstage a file (added with git add but not committed)</span><br>
    <span class="prompt">~/project %</span> <span class="cmd">git restore --staged index.html</span>
  </div>
</div>

<div class="highlight danger">

⚠️ **This cannot be undone.** `git restore` permanently discards your unsaved edits. There is no recovery. Only use it when you're certain you don't need those changes.

</div>

---

<!-- _class: step -->

<div class="step-badge">COMMAND 02</div>

## `git reset` — Undo Local Commits

You committed too soon, committed the wrong files, or want to rewrite your last few commits. Fine — as long as you haven't pushed yet.

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
    <span class="title">zsh — Terminal</span>
  </div>
  <div class="terminal-body">
    <span class="cmt"># Undo last commit — keep your changes in the working directory</span><br>
    <span class="prompt">~/project %</span> <span class="cmd">git reset --soft HEAD~1</span><br>
    <span class="out-g">Commit undone. Changes still staged.</span><br>
    <br>
    <span class="cmt"># Undo last commit — unstage changes but keep the files</span><br>
    <span class="prompt">~/project %</span> <span class="cmd">git reset HEAD~1</span><br>
    <br>
    <span class="cmt"># Undo last commit — discard changes entirely (destructive)</span><br>
    <span class="prompt">~/project %</span> <span class="cmd">git reset --hard HEAD~1</span><br>
    <span class="out-r">HEAD is now at 3f2a1b4 Previous commit message</span>
  </div>
</div>

<div class="highlight warn">

`HEAD~1` means "one commit back." `HEAD~3` means three commits back. Use `git log --oneline` first to see exactly what you're stepping back to.

</div>

---

<!-- _class: step -->

<div class="step-badge">COMMAND 03</div>

## `git revert` — Safe Undo on Shared Branches

Someone already pulled your bad commit. You can't rewrite history — you need to add a new commit that undoes it.

<div class="commit-timeline">
  <div class="ct-row">
    <div class="ct-dot blue"></div>
    <div class="ct-line blue" style="width:32px"></div>
    <div class="ct-dot blue"></div>
    <div class="ct-line blue" style="width:32px"></div>
    <div class="ct-dot red"></div>
    <div class="ct-line blue" style="width:32px"></div>
    <div class="ct-dot green"></div>
    <span class="ct-label ok">&nbsp;← revert commit (new)</span>
  </div>
  <div style="display:flex; gap:0; margin-left:14px; font-family:'DM Mono',monospace; font-size:11px; color:#4b5563;">
    <span style="width:46px">A</span>
    <span style="width:46px">B</span>
    <span style="width:46px; color:#f87171">C ← bad</span>
    <span style="color:#86efac">D undoes C</span>
  </div>
</div>

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
    <span class="title">zsh — Terminal</span>
  </div>
  <div class="terminal-body">
    <span class="cmt"># Find the hash of the bad commit</span><br>
    <span class="prompt">~/project %</span> <span class="cmd">git log --oneline</span><br>
    <span class="out-y">c3f91a2 Add broken feature</span><br>
    <span class="out">b2e10f1 Update README</span><br>
    <br>
    <span class="cmt"># Revert it — creates a new "undo" commit</span><br>
    <span class="prompt">~/project %</span> <span class="cmd">git revert c3f91a2</span><br>
    <span class="out-g">Revert "Add broken feature" — commit created.</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## When to Use Which

<table class="decision-table">
  <tr>
    <th>Situation</th>
    <th>Command</th>
    <th>Rewrites history?</th>
    <th>Safe on shared branches?</th>
  </tr>
  <tr>
    <td>Edited a file, not committed yet</td>
    <td class="mono">git restore &lt;file&gt;</td>
    <td>No history yet</td>
    <td class="safe">✓ Yes</td>
  </tr>
  <tr>
    <td>Committed locally, not pushed</td>
    <td class="mono">git reset HEAD~1</td>
    <td>Yes — local only</td>
    <td class="safe">✓ Yes (local only)</td>
  </tr>
  <tr>
    <td>Committed + pushed, no one pulled</td>
    <td class="mono">git reset + force push</td>
    <td>Yes</td>
    <td class="unsafe">✗ Risky</td>
  </tr>
  <tr>
    <td>Pushed + others have pulled</td>
    <td class="mono">git revert &lt;hash&gt;</td>
    <td>No — adds new commit</td>
    <td class="safe">✓ Always safe</td>
  </tr>
  <tr>
    <td>Need to undo a specific old commit</td>
    <td class="mono">git revert &lt;hash&gt;</td>
    <td>No</td>
    <td class="safe">✓ Always safe</td>
  </tr>
</table>

<div class="highlight">

**The golden rule:** if the commit has been pushed to a shared branch, always use `git revert`. Never `git reset` on shared history.

</div>

---

## Cheatsheet

<table class="cheat-table">
  <tr>
    <th>Command</th>
    <th>What it undoes</th>
    <th>Keeps files?</th>
    <th>History</th>
    <th>Safety</th>
  </tr>
  <tr>
    <td class="mono">git restore &lt;file&gt;</td>
    <td>Uncommitted edits in one file</td>
    <td>❌ Gone</td>
    <td>Unaffected</td>
    <td class="safe">LOCAL ONLY</td>
  </tr>
  <tr>
    <td class="mono">git restore .</td>
    <td>All uncommitted edits</td>
    <td>❌ Gone</td>
    <td>Unaffected</td>
    <td class="safe">LOCAL ONLY</td>
  </tr>
  <tr>
    <td class="mono">git reset --soft HEAD~1</td>
    <td>Last commit (keeps staged)</td>
    <td>✅ Staged</td>
    <td>Rewritten</td>
    <td class="safe">LOCAL ONLY</td>
  </tr>
  <tr>
    <td class="mono">git reset HEAD~1</td>
    <td>Last commit (unstages files)</td>
    <td>✅ Unstaged</td>
    <td>Rewritten</td>
    <td class="safe">LOCAL ONLY</td>
  </tr>
  <tr>
    <td class="mono">git reset --hard HEAD~1</td>
    <td>Last commit + all changes</td>
    <td>❌ Gone</td>
    <td>Rewritten</td>
    <td class="unsafe">DESTRUCTIVE</td>
  </tr>
  <tr>
    <td class="mono">git revert &lt;hash&gt;</td>
    <td>Any specific past commit</td>
    <td>✅ In new commit</td>
    <td>Preserved</td>
    <td class="safe">ALWAYS SAFE</td>
  </tr>
  <tr>
    <td class="mono">git log --oneline</td>
    <td>—</td>
    <td>—</td>
    <td>Shows history</td>
    <td class="safe">READ ONLY</td>
  </tr>
</table>

---

<!-- _class: final -->

# Git doesn't forget.
# Neither should you.

&nbsp;

`restore` for edits · `reset` for local commits · `revert` for shared history

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*