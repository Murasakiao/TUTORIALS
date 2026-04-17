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
  section.cover h2 { color: var(--white); border-bottom-color: #374151; }
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
  .terminal-body .prompt   { color: #22c55e; }
  .terminal-body .prompt-b { color: #f9a8d4; }
  .terminal-body .cmd      { color: #f9fafb; }
  .terminal-body .out      { color: #9ca3af; }
  .terminal-body .out-g    { color: #86efac; }
  .terminal-body .out-b    { color: #60a5fa; }
  .terminal-body .cmt      { color: #4b5563; font-style: italic; }

  /* Branch diagram */
  .branch-diagram {
    background: #111827;
    border-radius: 10px;
    padding: 22px 26px;
    margin: 16px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .branch-row {
    display: flex;
    align-items: center;
    gap: 0;
    margin-bottom: 10px;
  }

  .branch-label {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    font-weight: 600;
    min-width: 90px;
    flex-shrink: 0;
  }

  .branch-label.main    { color: #60a5fa; }
  .branch-label.feature { color: #f9a8d4; }

  .commit-dot {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    flex-shrink: 0;
  }

  .commit-dot.blue   { background: #2563eb; border: 2px solid #60a5fa; }
  .commit-dot.pink   { background: #9d174d; border: 2px solid #f9a8d4; }
  .commit-dot.green  { background: #14532d; border: 2px solid #86efac; }
  .commit-dot.hollow { background: #111827; border: 2px solid #374151; }

  .branch-line {
    height: 2px;
    flex: 1;
  }

  .branch-line.blue  { background: #2563eb; }
  .branch-line.pink  { background: #9d174d; }
  .branch-line.gray  { background: #374151; }

  .branch-fork {
    display: flex;
    align-items: flex-start;
    margin-left: 90px;
    gap: 0;
  }

  .branch-merge-label {
    font-size: 11px;
    color: #86efac;
    margin-left: 8px;
    align-self: center;
  }

  .branch-commit-label {
    font-size: 11px;
    color: #6b7280;
    margin-left: 8px;
    align-self: center;
  }

  /* Fork vs branch split */
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

  .concept-card.branch-card {
    background: #111827;
    border: 2px solid #1d4ed8;
  }

  .concept-card.fork-card {
    background: #0d1117;
    border: 2px solid #9d174d;
  }

  .concept-card .cc-icon  { font-size: 28px; margin-bottom: 8px; }

  .concept-card .cc-title {
    font-family: 'DM Mono', monospace;
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 6px;
  }

  .concept-card.branch-card .cc-title { color: #60a5fa; }
  .concept-card.fork-card   .cc-title { color: #f9a8d4; }

  .concept-card .cc-sub {
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    font-family: 'DM Mono', monospace;
  }

  .concept-card.branch-card .cc-sub { color: #3b82f6; }
  .concept-card.fork-card   .cc-sub { color: #be185d; }

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
    line-height: 2;
  }

  .concept-card.branch-card .cc-fact span { color: #60a5fa; }
  .concept-card.fork-card   .cc-fact span { color: #f9a8d4; }

  /* Workflow flow strip */
  .workflow-strip {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 0;
    margin: 18px 0;
    align-items: center;
  }

  .wf-step {
    background: #111827;
    border-radius: 8px;
    padding: 12px 14px;
    text-align: center;
  }

  .wf-step .wf-icon  { font-size: 20px; margin-bottom: 4px; }
  .wf-step .wf-label {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: #60a5fa;
    font-weight: 500;
    margin-bottom: 2px;
  }

  .wf-step .wf-desc {
    font-size: 11px;
    color: #6b7280;
    line-height: 1.4;
  }

  .wf-arrow {
    text-align: center;
    color: #374151;
    font-size: 18px;
    flex-shrink: 0;
  }

  /* PR review mock */
  .pr-mock {
    background: #0d1117;
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0;
    border: 1px solid #30363d;
  }

  .pr-header {
    background: #161b22;
    padding: 12px 18px;
    border-bottom: 1px solid #30363d;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .pr-status {
    background: #238636;
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 600;
    padding: 3px 10px;
    border-radius: 999px;
    flex-shrink: 0;
  }

  .pr-title {
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    font-weight: 600;
    color: #f0f6fc;
  }

  .pr-meta {
    font-family: 'DM Sans', sans-serif;
    font-size: 12px;
    color: #8b949e;
    margin-left: auto;
    white-space: nowrap;
  }

  .pr-body {
    padding: 14px 18px;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .pr-comment {
    display: flex;
    gap: 10px;
    align-items: flex-start;
  }

  .pr-avatar {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 13px;
  }

  .pr-avatar.reviewer { background: #1d4ed8; }
  .pr-avatar.author   { background: #374151; }

  .pr-bubble {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 8px 12px;
    font-family: 'DM Sans', sans-serif;
    font-size: 12px;
    flex: 1;
  }

  .pr-bubble .pb-name  { color: #60a5fa; font-weight: 600; margin-right: 6px; }
  .pr-bubble .pb-text  { color: #8b949e; }
  .pr-bubble .pb-green { color: #86efac; }

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

# Collaborate on GitHub
## Forks, Branches, and Pull Requests

&nbsp;

**How real teams ship code** without stepping on each other.

`branch` · `fork` · `pull request` · `merge` · `review`

---

## Why You Don't Edit `main` Directly

`main` is your production branch — the code that's live, working, and trusted.

<div class="tools">
  <div class="tool-card">
    <div class="icon">💥</div>
    <div class="name">One bad commit breaks everything</div>
    <div class="desc">Push a bug directly to main and it's immediately in production. No safety net.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🚧</div>
    <div class="name">No room for review</div>
    <div class="desc">Editing main skips the review step entirely. No one catches your mistakes before they ship.</div>
  </div>
  <div class="tool-card">
    <div class="icon">👥</div>
    <div class="name">Teams collide</div>
    <div class="desc">Two people editing the same file on main at the same time = merge conflicts and lost work.</div>
  </div>
  <div class="tool-card">
    <div class="icon">✅</div>
    <div class="name">The solution</div>
    <div class="desc">Work on a branch. Review it. Merge it when it's ready. Main stays clean.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## What a Branch Is

A branch is a parallel copy of your code where you can work freely without touching `main`.

<div class="branch-diagram">
  <div class="branch-row">
    <span class="branch-label main">main</span>
    <div class="commit-dot blue"></div>
    <div class="branch-line blue" style="width:40px"></div>
    <div class="commit-dot blue"></div>
    <div class="branch-line blue" style="width:40px"></div>
    <div class="commit-dot blue"></div>
    <div class="branch-line blue" style="width:80px"></div>
    <div class="commit-dot green"></div>
    <span class="branch-merge-label">← merge</span>
  </div>
  <div style="margin-left:154px; margin-top:-4px; margin-bottom:4px;">
    <div style="width:2px; height:14px; background:#9d174d; margin-left:0px;"></div>
  </div>
  <div class="branch-row">
    <span class="branch-label feature">feature</span>
    <div class="branch-line gray" style="width:40px"></div>
    <div class="commit-dot pink"></div>
    <div class="branch-line pink" style="width:40px"></div>
    <div class="commit-dot pink"></div>
    <div class="branch-line pink" style="width:40px"></div>
    <div class="commit-dot pink"></div>
    <span class="branch-commit-label">← your work lives here</span>
  </div>
</div>

- Branch off `main` → work freely → merge back when done
- `main` keeps running uninterrupted while you build
- You can have **multiple branches** running in parallel — one per feature or fix

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Branch vs Fork — What's the Difference

<div class="split-concept">
  <div class="concept-card branch-card">
    <div class="cc-icon">🌿</div>
    <div class="cc-title">Branch</div>
    <div class="cc-sub">Inside the same repo</div>
    <div class="cc-desc">A parallel line of work within a repository you already have access to. Used by team members working on the same project.</div>
    <div class="cc-fact">
      <span>✦ Same repo, different timeline</span><br>
      <span>✦ git checkout -b feature-name</span><br>
      <span>✦ Merged via pull request</span>
    </div>
  </div>
  <div class="concept-card fork-card">
    <div class="cc-icon">🍴</div>
    <div class="cc-title">Fork</div>
    <div class="cc-sub">Your own copy on GitHub</div>
    <div class="cc-desc">A full copy of someone else's repository under your own GitHub account. Used when contributing to projects you don't own.</div>
    <div class="cc-fact">
      <span>✦ Separate repo on your account</span><br>
      <span>✦ Fork button on GitHub.com</span><br>
      <span>✦ Contribute via pull request</span>
    </div>
  </div>
</div>

<div class="highlight">

**Rule of thumb:** branch if you're on the team. Fork if you're contributing from outside.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## The Full Workflow

Fork → Clone → Branch → Edit → Push → Pull Request

<div class="workflow-strip">
  <div class="wf-step">
    <div class="wf-icon">🍴</div>
    <div class="wf-label">Fork</div>
    <div class="wf-desc">Copy repo to your GitHub account</div>
  </div>
  <div class="wf-arrow">→</div>
  <div class="wf-step">
    <div class="wf-icon">💻</div>
    <div class="wf-label">Clone</div>
    <div class="wf-desc">Download your fork locally</div>
  </div>
  <div class="wf-arrow">→</div>
  <div class="wf-step">
    <div class="wf-icon">🌿</div>
    <div class="wf-label">Branch</div>
    <div class="wf-desc">Create a feature branch</div>
  </div>
  <div class="wf-arrow">→</div>
  <div class="wf-step">
    <div class="wf-icon">✏️</div>
    <div class="wf-label">Edit + Push</div>
    <div class="wf-desc">Make changes, commit, push</div>
  </div>
  <div class="wf-arrow">→</div>
  <div class="wf-step">
    <div class="wf-icon">🔀</div>
    <div class="wf-label">PR</div>
    <div class="wf-desc">Open pull request for review</div>
  </div>
</div>

<div class="highlight">

A **pull request** (PR) is a formal request to merge your branch into main. It's where code gets reviewed, discussed, and approved before it touches production.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## The Commands — Fork to PR

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
    <span class="title">zsh — Terminal</span>
  </div>
  <div class="terminal-body">
    <span class="cmt"># 1. Clone your fork locally</span><br>
    <span class="prompt">~ %</span> <span class="cmd">git clone https://github.com/you/project.git</span><br>
    <span class="prompt">~ %</span> <span class="cmd">cd project</span><br>
    <br>
    <span class="cmt"># 2. Create and switch to a new branch</span><br>
    <span class="prompt-b">(main)</span> <span class="prompt">~/project %</span> <span class="cmd">git checkout -b fix/update-readme</span><br>
    <span class="out-g">Switched to a new branch 'fix/update-readme'</span><br>
    <br>
    <span class="cmt"># 3. Make your changes, then commit</span><br>
    <span class="prompt-b">(fix/update-readme)</span> <span class="prompt">~/project %</span> <span class="cmd">git add .</span><br>
    <span class="prompt-b">(fix/update-readme)</span> <span class="prompt">~/project %</span> <span class="cmd">git commit -m "Fix typo in README installation steps"</span><br>
    <br>
    <span class="cmt"># 4. Push branch to your fork on GitHub</span><br>
    <span class="prompt-b">(fix/update-readme)</span> <span class="prompt">~/project %</span> <span class="cmd">git push origin fix/update-readme</span><br>
    <span class="out-g">Branch 'fix/update-readme' set up to track remote.</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Open and Review a Pull Request

After pushing, GitHub shows a **"Compare & pull request"** banner. Click it.

<div class="pr-mock">
  <div class="pr-header">
    <span class="pr-status">Open</span>
    <span class="pr-title">Fix typo in README installation steps</span>
    <span class="pr-meta">julius wants to merge 1 commit into main</span>
  </div>
  <div class="pr-body">
    <div class="pr-comment">
      <div class="pr-avatar reviewer">👤</div>
      <div class="pr-bubble">
        <span class="pb-name">reviewer</span>
        <span class="pb-text">Looks good! One suggestion — can you also update the Windows path while you're at it?</span>
      </div>
    </div>
    <div class="pr-comment">
      <div class="pr-avatar author">👤</div>
      <div class="pr-bubble">
        <span class="pb-name">julius</span>
        <span class="pb-text">Done — pushed a follow-up commit.</span>
      </div>
    </div>
    <div class="pr-comment">
      <div class="pr-avatar reviewer">👤</div>
      <div class="pr-bubble">
        <span class="pb-name">reviewer</span>
        <span class="pb-green">✓ Approved. Merging.</span>
      </div>
    </div>
  </div>
</div>

A PR is a conversation, not just a code diff. Reviewers can comment on specific lines, request changes, or approve and merge.

---

## Real Example Walkthrough

Contributing a fix to an open-source repo you don't own:

<ul class="step-list">
  <li>Go to the repo on GitHub → click <strong>Fork</strong> → it copies to your account</li>
  <li>Clone your fork: <code>git clone https://github.com/you/their-repo.git</code></li>
  <li>Create a branch: <code>git checkout -b fix/broken-link</code></li>
  <li>Make your change in the file, save it</li>
  <li>Stage and commit: <code>git add . && git commit -m "Fix broken docs link"</code></li>
  <li>Push to your fork: <code>git push origin fix/broken-link</code></li>
  <li>Go to GitHub → click <strong>"Compare & pull request"</strong> → write a clear description → submit</li>
  <li>Respond to any reviewer comments → maintainer merges when satisfied</li>
</ul>

---

<!-- _class: final -->

# Branch. Review. Merge.
# That's how teams ship.

&nbsp;

Every open-source contribution you've ever used started with this exact workflow.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*