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

  /* File version chaos grid */
  .chaos-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    margin: 16px 0;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
  }

  .chaos-file {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 10px 14px;
    color: var(--muted);
    line-height: 1.8;
  }

  .chaos-file .cf-name { color: var(--text); font-weight: 500; font-size: 13px; }
  .chaos-file .cf-bad  { color: #f87171; }
  .chaos-file .cf-ok   { color: #86efac; }

  /* Git/GitHub split concept */
  .split-concept {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin: 16px 0;
  }

  .concept-card {
    border-radius: 12px;
    padding: 20px 22px;
  }

  .concept-card.git-card {
    background: #111827;
    border: 2px solid #374151;
  }

  .concept-card.gh-card {
    background: #0d1117;
    border: 2px solid #1d4ed8;
  }

  .concept-card .cc-icon {
    font-size: 28px;
    margin-bottom: 8px;
  }

  .concept-card .cc-title {
    font-family: 'DM Mono', monospace;
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 6px;
  }

  .concept-card.git-card .cc-title { color: #f9fafb; }
  .concept-card.gh-card  .cc-title { color: #60a5fa; }

  .concept-card .cc-sub {
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    font-family: 'DM Mono', monospace;
  }

  .concept-card.git-card .cc-sub { color: #6b7280; }
  .concept-card.gh-card  .cc-sub { color: #3b82f6; }

  .concept-card .cc-desc {
    font-size: 13px;
    color: #9ca3af;
    line-height: 1.7;
  }

  .concept-card .cc-fact {
    margin-top: 10px;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: #4b5563;
    line-height: 1.8;
  }

  .concept-card.git-card .cc-fact span { color: #86efac; }
  .concept-card.gh-card  .cc-fact span { color: #60a5fa; }

  /* Local/remote diagram */
  .diagram {
    display: flex;
    align-items: center;
    gap: 0;
    margin: 20px 0;
  }

  .diagram-side {
    flex: 1;
    background: #111827;
    border-radius: 10px;
    padding: 18px 20px;
  }

  .diagram-side.local  { border: 2px solid #374151; }
  .diagram-side.remote { border: 2px solid #1d4ed8; background: #0d1117; }

  .diagram-side .ds-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 10px;
    font-weight: 600;
  }

  .diagram-side.local  .ds-label { color: #6b7280; }
  .diagram-side.remote .ds-label { color: #3b82f6; }

  .diagram-side .ds-name {
    font-size: 15px;
    font-weight: 600;
    margin-bottom: 8px;
  }

  .diagram-side.local  .ds-name { color: #f9fafb; }
  .diagram-side.remote .ds-name { color: #60a5fa; }

  .diagram-side .ds-item {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: #6b7280;
    line-height: 2;
  }

  .diagram-side .ds-item span { color: #86efac; }

  .diagram-middle {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    padding: 0 16px;
    flex-shrink: 0;
  }

  .diagram-arrow {
    display: flex;
    align-items: center;
    gap: 6px;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    white-space: nowrap;
  }

  .diagram-arrow.push { color: #86efac; }
  .diagram-arrow.pull { color: #60a5fa; }

  .diagram-arrow .arrow-line {
    width: 48px;
    height: 2px;
    position: relative;
  }

  .diagram-arrow.push .arrow-line { background: #86efac; }
  .diagram-arrow.pull .arrow-line { background: #60a5fa; }

  /* Key terms grid */
  .terms-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin: 14px 0;
  }

  .term-card {
    background: #111827;
    border-radius: 8px;
    padding: 13px 16px;
    display: flex;
    gap: 12px;
    align-items: flex-start;
  }

  .term-card .tc-cmd {
    font-family: 'DM Mono', monospace;
    font-size: 14px;
    color: #60a5fa;
    font-weight: 600;
    min-width: 70px;
    padding-top: 1px;
    flex-shrink: 0;
  }

  .term-card .tc-body .tc-title {
    font-size: 14px;
    font-weight: 600;
    color: #f0f6fc;
    margin-bottom: 2px;
  }

  .term-card .tc-body .tc-desc {
    font-size: 12px;
    color: #6b7280;
    line-height: 1.5;
  }

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
  .terminal-body .prompt { color: #22c55e; }
  .terminal-body .cmd    { color: #f9fafb; }
  .terminal-body .out    { color: #9ca3af; }
  .terminal-body .out-g  { color: #86efac; }
  .terminal-body .cmt    { color: #4b5563; font-style: italic; }

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

# Git vs GitHub
## Why You Need Both

&nbsp;

**Git saves your work. GitHub shares it.** They're not the same thing.

`commit` · `push` · `pull` · `repo` · `branch`

---

## The Problem Without Version Control

Without Git, this is how most people manage files:

<div class="chaos-grid">
  <div class="chaos-file">
    <div class="cf-name">report.docx</div>
    <div class="cf-bad">original</div>
  </div>
  <div class="chaos-file">
    <div class="cf-name">report_v2.docx</div>
    <div class="cf-bad">added intro</div>
  </div>
  <div class="chaos-file">
    <div class="cf-name">report_v2_FINAL.docx</div>
    <div class="cf-bad">fixed typos</div>
  </div>
  <div class="chaos-file">
    <div class="cf-name">report_FINAL2.docx</div>
    <div class="cf-bad">more changes</div>
  </div>
  <div class="chaos-file">
    <div class="cf-name">report_v3_use_this.docx</div>
    <div class="cf-bad">??</div>
  </div>
  <div class="chaos-file">
    <div class="cf-name cf-ok">report_git.py</div>
    <div class="cf-ok">one file, full history</div>
  </div>
</div>

Git eliminates this entirely. Instead of duplicate files, you get a single file with a complete, named, reversible history of every change ever made to it.

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## What Git Is — Local

Git is a **version control system** that lives entirely on your own computer.

<div class="split-concept">
  <div class="concept-card git-card">
    <div class="cc-icon">🗂️</div>
    <div class="cc-title">Git</div>
    <div class="cc-sub">Local · on your machine</div>
    <div class="cc-desc">Tracks every change you make to files in a folder. Lets you go back to any point in time. Works completely offline.</div>
    <div class="cc-fact">
      <span>✦ Installed via Terminal / CMD</span><br>
      <span>✦ Stores history in a hidden .git folder</span><br>
      <span>✦ Free, open-source, runs everywhere</span>
    </div>
  </div>
  <div class="concept-card gh-card">
    <div class="cc-icon">🌐</div>
    <div class="cc-title">GitHub</div>
    <div class="cc-sub">Cloud · on the internet</div>
    <div class="cc-desc">A website that hosts your Git repositories online. Adds collaboration, visibility, and backup. Not required to use Git.</div>
    <div class="cc-fact">
      <span>✦ Website — github.com</span><br>
      <span>✦ Free for public and private repos</span><br>
      <span>✦ Owned by Microsoft since 2018</span>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## The Relationship Between Them

Git and GitHub are separate tools that work together — like Word and Google Drive.

<div class="two-col">
  <div class="col-card">
    <div class="label">🗂️ Git is the tool</div>
    <p style="font-size:14px; margin-top:8px;">You use Git commands in your terminal to track changes locally. It has nothing to do with the internet.</p>
    <p style="font-size:13px; color:#6b7280; margin-top:8px;">You can use Git your whole career and never touch GitHub.</p>
  </div>
  <div class="col-card">
    <div class="label">🌐 GitHub is the platform</div>
    <p style="font-size:14px; margin-top:8px;">GitHub is a cloud host for Git repositories. It adds a UI, pull requests, Issues, and a public profile on top of Git.</p>
    <p style="font-size:13px; color:#6b7280; margin-top:8px;">Alternatives: GitLab, Bitbucket — same Git underneath.</p>
  </div>
</div>

<div class="highlight">

**The analogy:** Git is like tracking changes in a Word document. GitHub is like uploading that document to Google Drive so others can see and collaborate on it.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Key Terms You'll See Everywhere

<div class="terms-grid">
  <div class="term-card">
    <div class="tc-cmd">repo</div>
    <div class="tc-body">
      <div class="tc-title">Repository</div>
      <div class="tc-desc">A project folder tracked by Git. Contains all your files and their full history.</div>
    </div>
  </div>
  <div class="term-card">
    <div class="tc-cmd">commit</div>
    <div class="tc-body">
      <div class="tc-title">Save a snapshot</div>
      <div class="tc-desc">A named checkpoint in your history. "Added login page." "Fixed CSV bug."</div>
    </div>
  </div>
  <div class="term-card">
    <div class="tc-cmd">push</div>
    <div class="tc-body">
      <div class="tc-title">Upload to GitHub</div>
      <div class="tc-desc">Send your local commits up to the remote repo on GitHub.</div>
    </div>
  </div>
  <div class="term-card">
    <div class="tc-cmd">pull</div>
    <div class="tc-body">
      <div class="tc-title">Download from GitHub</div>
      <div class="tc-desc">Fetch the latest commits from GitHub down to your local machine.</div>
    </div>
  </div>
  <div class="term-card">
    <div class="tc-cmd">clone</div>
    <div class="tc-body">
      <div class="tc-title">Copy a repo</div>
      <div class="tc-desc">Download a full copy of a GitHub repo to your machine for the first time.</div>
    </div>
  </div>
  <div class="term-card">
    <div class="tc-cmd">branch</div>
    <div class="tc-body">
      <div class="tc-title">Parallel version</div>
      <div class="tc-desc">A separate line of work that doesn't affect the main code until you merge it.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Local vs Remote — The Diagram

<div class="diagram">
  <div class="diagram-side local">
    <div class="ds-label">🗂️ Local — your machine</div>
    <div class="ds-name">Git Repository</div>
    <div class="ds-item"><span>git init</span> &nbsp;→ start tracking</div>
    <div class="ds-item"><span>git add .</span> &nbsp;→ stage changes</div>
    <div class="ds-item"><span>git commit -m "..."</span> &nbsp;→ save snapshot</div>
  </div>
  <div class="diagram-middle">
    <div class="diagram-arrow push">
      <span>push →</span>
    </div>
    <div style="width:2px; height:40px; background:#374151;"></div>
    <div class="diagram-arrow pull">
      <span>← pull</span>
    </div>
  </div>
  <div class="diagram-side remote">
    <div class="ds-label">🌐 Remote — GitHub</div>
    <div class="ds-name">github.com/you/repo</div>
    <div class="ds-item"><span>Stores full history</span></div>
    <div class="ds-item"><span>Visible to the world</span></div>
    <div class="ds-item"><span>Backed up, shareable</span></div>
  </div>
</div>

<div class="highlight">

**The daily loop:** make changes locally → `git add` → `git commit` → `git push` → your code is on GitHub.

</div>

---

## See It in Action

The four commands you'll use every single day:

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
    <span class="title">zsh — Terminal</span>
  </div>
  <div class="terminal-body">
    <span class="cmt"># 1. Stage all changed files</span><br>
    <span class="prompt">~/my-project %</span> <span class="cmd">git add .</span><br>
    <br>
    <span class="cmt"># 2. Save a named snapshot</span><br>
    <span class="prompt">~/my-project %</span> <span class="cmd">git commit -m "Add sales filter function"</span><br>
    <span class="out-g">[main 3f2a1b4] Add sales filter function</span><br>
    <br>
    <span class="cmt"># 3. Upload to GitHub</span><br>
    <span class="prompt">~/my-project %</span> <span class="cmd">git push</span><br>
    <span class="out-g">To github.com/julius/my-project.git</span><br>
    <span class="out-g">   main -> main</span>
  </div>
</div>

---

<!-- _class: final -->

# Git saves your work.
# GitHub shares it.

&nbsp;

Learn these four commands and you're 80% of the way there: `add` · `commit` · `push` · `pull`

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*