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

  /* ── Code block ── */
  .code-block {
    background: #111827;
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .code-block .cb-bar {
    background: #1f2937;
    padding: 8px 16px;
    font-size: 11.5px;
    color: #6b7280;
    letter-spacing: 0.04em;
  }

  .code-block .cb-body {
    padding: 14px 20px;
    line-height: 2;
  }

  .cb-prompt { color: #22c55e; }
  .cb-cmd    { color: #f9fafb; }
  .cb-type   { color: #c084fc; }
  .cb-scope  { color: #fb923c; }
  .cb-desc   { color: #f9fafb; }
  .cb-good   { color: #34d399; }
  .cb-bad    { color: #f87171; }
  .cb-muted  { color: #6b7280; }
  .cb-cmt    { color: #4b5563; font-style: italic; }
  .cb-prop   { color: #93c5fd; }
  .cb-val    { color: #34d399; }
  .cb-punct  { color: #6b7280; }

  /* ── Two-column layout ── */
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

  /* ── Commit log mock ── */
  .git-log {
    background: #111827;
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 12.5px;
  }

  .git-log .gl-bar {
    background: #1f2937;
    padding: 8px 16px;
    font-size: 11.5px;
    color: #6b7280;
    letter-spacing: 0.04em;
  }

  .git-log .gl-body {
    padding: 12px 18px;
  }

  .gl-row {
    display: flex;
    align-items: baseline;
    gap: 12px;
    padding: 5px 0;
    border-bottom: 1px solid #1f2937;
    line-height: 1.5;
  }

  .gl-row:last-child { border-bottom: none; }

  .gl-hash  { color: #fb923c; min-width: 52px; }
  .gl-type  { color: #c084fc; min-width: 64px; }
  .gl-msg   { color: #f9fafb; flex: 1; }
  .gl-msg.bad { color: #f87171; }
  .gl-date  { color: #4b5563; font-size: 11px; min-width: 70px; text-align: right; }

  /* ── Bad / good comparison ── */
  .compare-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 14px;
  }

  .compare-col .cmp-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    padding: 7px 14px;
    border-radius: 8px 8px 0 0;
  }

  .compare-col.bad  .cmp-label { background: #fef2f2; color: #991b1b; border: 1px solid #fecaca; border-bottom: none; }
  .compare-col.good .cmp-label { background: #f0fdf4; color: #166534; border: 1px solid #bbf7d0; border-bottom: none; }

  .compare-col .cmp-body {
    border-radius: 0 0 8px 8px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .compare-col.bad  .cmp-body { border: 1px solid #fecaca; border-top: none; }
  .compare-col.good .cmp-body { border: 1px solid #bbf7d0; border-top: none; }

  .cmp-row {
    display: flex;
    align-items: baseline;
    gap: 10px;
    padding: 9px 14px;
    background: #111827;
    border-bottom: 1px solid #1f2937;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    line-height: 1.5;
  }

  .cmp-row:last-child { border-bottom: none; }
  .cmp-row .cr-hash { color: #fb923c; min-width: 48px; }
  .cmp-row .cr-msg  { flex: 1; }
  .cmp-row .cr-msg.bad  { color: #f87171; }
  .cmp-row .cr-msg.good { color: #34d399; }

  /* ── Anatomy breakdown ── */
  .anatomy-box {
    background: #111827;
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0;
  }

  .anatomy-box .ab-bar {
    background: #1f2937;
    padding: 8px 16px;
    font-family: 'DM Mono', monospace;
    font-size: 11.5px;
    color: #6b7280;
    letter-spacing: 0.04em;
  }

  .anatomy-box .ab-body {
    padding: 16px 22px 10px;
    font-family: 'DM Mono', monospace;
    font-size: 17px;
    letter-spacing: 0.01em;
    line-height: 1.4;
  }

  .anatomy-box .ab-labels {
    display: flex;
    padding: 0 22px 16px;
    gap: 0;
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    color: #6b7280;
    margin-top: 6px;
  }

  .ab-lbl {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 3px;
  }

  .ab-lbl .ab-tick {
    width: 1px;
    height: 10px;
    background: #374151;
    margin-left: 2px;
  }

  /* ── Rules list ── */
  .rules-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 14px;
  }

  .rule-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }

  .rule-card .r-num {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    font-weight: 500;
    color: var(--blue);
    min-width: 22px;
    padding-top: 1px;
  }

  .rule-card .r-title {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
    margin-bottom: 3px;
  }

  .rule-card .r-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.5;
  }

  /* ── Type reference ── */
  .type-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 12px;
  }

  .type-row {
    background: #111827;
    border-radius: 8px;
    padding: 10px 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }

  .type-row .tr-type {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #c084fc;
    font-weight: 500;
    min-width: 72px;
    padding-top: 1px;
  }

  .type-row .tr-desc {
    font-size: 13px;
    color: #d1d5db;
    line-height: 1.5;
  }

  .type-row .tr-desc span {
    display: block;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #4b5563;
    margin-top: 2px;
  }

  /* ── Tool cards ── */
  .tool-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 14px;
  }

  .tool-item {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 18px;
    display: flex;
    align-items: flex-start;
    gap: 14px;
  }

  .tool-item .t-icon { font-size: 26px; flex-shrink: 0; }

  .tool-item .t-name {
    font-weight: 600;
    font-size: 14.5px;
    color: var(--text);
  }

  .tool-item .t-url {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--blue);
    margin-top: 2px;
  }

  .tool-item .t-desc {
    font-size: 12.5px;
    color: var(--muted);
    margin-top: 4px;
    line-height: 1.45;
  }

  /* ── Cheatsheet table ── */
  .cheat-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13.5px;
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
    padding: 9px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
  }

  .cheat-table tr:last-child td { border-bottom: none; }
  .cheat-table tr:nth-child(even) td { background: var(--off-white); }

  .cheat-table .mono {
    font-family: 'DM Mono', monospace;
    color: var(--blue);
    font-size: 12.5px;
  }

  .cheat-table .type-pill {
    font-family: 'DM Mono', monospace;
    font-size: 11.5px;
    color: #7c3aed;
    background: #f5f3ff;
    border: 1px solid #ddd6fe;
    padding: 2px 8px;
    border-radius: 4px;
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

# Write Good
# Commit Messages

&nbsp;

**Your git log is a story.** Make it one people can actually read.

`feat` · `fix` · `chore` · `refactor` · `scope` · `imperative`

---

## Why Bad Commits Hurt You Later

A messy git log isn't just ugly — it actively costs you time.

<div class="tools">
  <div class="tool-card">
    <div class="icon">🔍</div>
    <div class="name">You can't find the bug</div>
    <div class="desc">"fixed stuff" tells you nothing. Good messages let you scan history and pinpoint exactly when a behaviour changed.</div>
  </div>
  <div class="tool-card">
    <div class="icon">⏪</div>
    <div class="name">Reverting is guesswork</div>
    <div class="desc">To safely undo a change, you need to know what each commit did. Vague messages mean reading every diff just to find the right one.</div>
  </div>
  <div class="tool-card">
    <div class="icon">👥</div>
    <div class="name">Teammates are blocked</div>
    <div class="desc">On a team, your commit message is the only explanation a colleague gets before reading your code. A bad message is a silent handoff.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🤖</div>
    <div class="name">Automation breaks</div>
    <div class="desc">Changelogs, release notes, and semantic versioning tools parse your commit messages. Inconsistent format means none of that works.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## The Anatomy of a Good Message

The Conventional Commits standard — used by Vue, Angular, VS Code, and thousands of open-source projects.

<div class="anatomy-box">
  <div class="ab-bar">commit message structure</div>
  <div class="ab-body">
    <span style="color:#c084fc;">feat</span><span style="color:#6b7280;">(</span><span style="color:#fb923c;">auth</span><span style="color:#6b7280;">)</span><span style="color:#6b7280;">:</span> <span style="color:#f9fafb;">add Google OAuth login flow</span>
  </div>
  <div class="ab-labels">
    <div class="ab-lbl" style="width:52px;">
      <div class="ab-tick"></div>
      <span style="color:#c084fc;">type</span>
    </div>
    <div class="ab-lbl" style="width:60px; margin-left:4px;">
      <div class="ab-tick"></div>
      <span style="color:#fb923c;">scope</span>
    </div>
    <div class="ab-lbl" style="margin-left:16px;">
      <div class="ab-tick"></div>
      <span style="color:#94a3b8;">description</span>
    </div>
  </div>
</div>

<div class="two-col" style="margin-top:4px;">
  <div class="col-card">
    <div class="label">type (required)</div>
    <p style="font-size:13.5px; margin-top:8px;">What kind of change is this? <code>feat</code>, <code>fix</code>, <code>docs</code>, <code>chore</code>. Lowercase, no spaces. Tells readers the intent before they read the description.</p>
  </div>
  <div class="col-card">
    <div class="label">scope (optional)</div>
    <p style="font-size:13.5px; margin-top:8px;">Which part of the codebase? <code>(auth)</code>, <code>(api)</code>, <code>(ui)</code>. In parentheses after the type. Skip it for small repos — use it when a project has clear modules.</p>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Commit Types Reference

<div class="type-grid">
  <div class="type-row">
    <div class="tr-type">feat</div>
    <div class="tr-desc">A new feature for the user<span>feat(cart): add quantity selector</span></div>
  </div>
  <div class="type-row">
    <div class="tr-type">fix</div>
    <div class="tr-desc">A bug fix<span>fix(auth): handle expired token redirect</span></div>
  </div>
  <div class="type-row">
    <div class="tr-type">docs</div>
    <div class="tr-desc">Documentation only changes<span>docs: update API endpoint examples</span></div>
  </div>
  <div class="type-row">
    <div class="tr-type">style</div>
    <div class="tr-desc">Formatting, whitespace, semicolons<span>style: fix indentation in App.jsx</span></div>
  </div>
  <div class="type-row">
    <div class="tr-type">refactor</div>
    <div class="tr-desc">Code change that isn't a fix or feature<span>refactor(db): extract query helper function</span></div>
  </div>
  <div class="type-row">
    <div class="tr-type">test</div>
    <div class="tr-desc">Adding or updating tests<span>test(login): add unit tests for validation</span></div>
  </div>
  <div class="type-row">
    <div class="tr-type">chore</div>
    <div class="tr-desc">Tooling, config, dependencies<span>chore: upgrade eslint to v9</span></div>
  </div>
  <div class="type-row">
    <div class="tr-type">perf</div>
    <div class="tr-desc">Performance improvement<span>perf(images): lazy load below-fold assets</span></div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Bad vs Good — Side by Side

<div class="compare-grid">
  <div class="compare-col bad">
    <div class="cmp-label">❌ &nbsp;Bad commit history</div>
    <div class="cmp-body">
      <div class="cmp-row"><span class="cr-hash">a3f91c</span><span class="cr-msg bad">fixed bug</span></div>
      <div class="cmp-row"><span class="cr-hash">b22d04</span><span class="cr-msg bad">wip</span></div>
      <div class="cmp-row"><span class="cr-hash">c10f88</span><span class="cr-msg bad">changes</span></div>
      <div class="cmp-row"><span class="cr-hash">d84a11</span><span class="cr-msg bad">update stuff</span></div>
      <div class="cmp-row"><span class="cr-hash">e77b23</span><span class="cr-msg bad">asdfgh</span></div>
      <div class="cmp-row"><span class="cr-hash">f91c40</span><span class="cr-msg bad">final final v2</span></div>
    </div>
  </div>
  <div class="compare-col good">
    <div class="cmp-label">✅ &nbsp;Good commit history</div>
    <div class="cmp-body">
      <div class="cmp-row"><span class="cr-hash">a3f91c</span><span class="cr-msg good">fix(auth): redirect on token expiry</span></div>
      <div class="cmp-row"><span class="cr-hash">b22d04</span><span class="cr-msg good">feat(cart): add item quantity controls</span></div>
      <div class="cmp-row"><span class="cr-hash">c10f88</span><span class="cr-msg good">chore: update dependencies to latest</span></div>
      <div class="cmp-row"><span class="cr-hash">d84a11</span><span class="cr-msg good">docs: add setup steps to README</span></div>
      <div class="cmp-row"><span class="cr-hash">e77b23</span><span class="cr-msg good">refactor(api): extract error handler</span></div>
      <div class="cmp-row"><span class="cr-hash">f91c40</span><span class="cr-msg good">perf: lazy load dashboard charts</span></div>
    </div>
  </div>
</div>

<div class="highlight" style="margin-top:16px;">

The good log reads like a **changelog**. In six lines you know exactly what changed, where, and why — without opening a single file.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## The 7 Rules of Great Commit Messages

<div class="rules-grid">
  <div class="rule-card">
    <div class="r-num">01</div>
    <div>
      <div class="r-title">Use the imperative mood</div>
      <div class="r-desc">Write "add login page" not "added" or "adding." Git itself uses imperative: "Merge branch," "Revert commit."</div>
    </div>
  </div>
  <div class="rule-card">
    <div class="r-num">02</div>
    <div>
      <div class="r-title">Keep the subject under 72 chars</div>
      <div class="r-desc">GitHub truncates at 72. Terminals wrap. Short subjects are scannable in <code>git log --oneline</code>.</div>
    </div>
  </div>
  <div class="rule-card">
    <div class="r-num">03</div>
    <div>
      <div class="r-title">Don't end with a period</div>
      <div class="r-desc">Subject lines are titles, not sentences. "fix login redirect" — no full stop at the end.</div>
    </div>
  </div>
  <div class="rule-card">
    <div class="r-num">04</div>
    <div>
      <div class="r-title">One logical change per commit</div>
      <div class="r-desc">If your message needs "and" — it's probably two commits. Atomic commits are easier to revert and review.</div>
    </div>
  </div>
  <div class="rule-card">
    <div class="r-num">05</div>
    <div>
      <div class="r-title">Explain why, not what</div>
      <div class="r-desc">The diff already shows <em>what</em> changed. The message should explain <em>why</em> it was necessary.</div>
    </div>
  </div>
  <div class="rule-card">
    <div class="r-num">06</div>
    <div>
      <div class="r-title">Use a body for context</div>
      <div class="r-desc">Leave a blank line after the subject, then add detail. The body has no length limit and supports plain text.</div>
    </div>
  </div>
  <div class="rule-card">
    <div class="r-num">07</div>
    <div>
      <div class="r-title">Be consistent with your team</div>
      <div class="r-desc">Conventions only help if everyone follows them. Pick a format, write it down, enforce it with tooling.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## Tools That Enforce It

Good intentions drift. Tooling keeps the whole team consistent automatically.

<div class="tool-row">
  <div class="tool-item">
    <div class="t-icon">🔒</div>
    <div>
      <div class="t-name">commitlint</div>
      <div class="t-url">commitlint.js.org</div>
      <div class="t-desc">Lints commit messages against Conventional Commits rules. Rejects the commit at the terminal if the message is invalid — before it ever enters the log.</div>
    </div>
  </div>
  <div class="tool-item">
    <div class="t-icon">🐶</div>
    <div>
      <div class="t-name">Husky</div>
      <div class="t-url">typicode.github.io/husky</div>
      <div class="t-desc">Runs scripts on Git hooks — most commonly <code>commit-msg</code>. Pair with commitlint so the check fires automatically on every commit.</div>
    </div>
  </div>
  <div class="tool-item">
    <div class="t-icon">💬</div>
    <div>
      <div class="t-name">Commitizen</div>
      <div class="t-url">commitizen-tools.github.io</div>
      <div class="t-desc">Replaces <code>git commit</code> with an interactive prompt. Walks you through type → scope → description step by step. Great for onboarding new contributors.</div>
    </div>
  </div>
  <div class="tool-item">
    <div class="t-icon">📋</div>
    <div>
      <div class="t-name">standard-version</div>
      <div class="t-url">github.com/conventional-changelog</div>
      <div class="t-desc">Auto-generates a CHANGELOG.md and bumps your version number based on commit types. <code>feat</code> → minor bump. <code>fix</code> → patch. Breaking change → major.</div>
    </div>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**Minimal setup:** `npm install --save-dev husky @commitlint/cli @commitlint/config-conventional` — then add a <code>commit-msg</code> hook that runs `commitlint`. Five minutes, permanent effect.

</div>

---

## Commit Message Cheatsheet

<table class="cheat-table">
  <tr>
    <th>Type</th>
    <th>Use when</th>
    <th>Example</th>
  </tr>
  <tr>
    <td><span class="type-pill">feat</span></td>
    <td>Adding a new user-facing feature</td>
    <td class="mono">feat(nav): add mobile hamburger menu</td>
  </tr>
  <tr>
    <td><span class="type-pill">fix</span></td>
    <td>Patching a bug</td>
    <td class="mono">fix(form): validate email before submit</td>
  </tr>
  <tr>
    <td><span class="type-pill">docs</span></td>
    <td>README, comments, documentation</td>
    <td class="mono">docs: add contributing guidelines</td>
  </tr>
  <tr>
    <td><span class="type-pill">style</span></td>
    <td>Whitespace, formatting, no logic change</td>
    <td class="mono">style: remove trailing whitespace</td>
  </tr>
  <tr>
    <td><span class="type-pill">refactor</span></td>
    <td>Restructuring without behaviour change</td>
    <td class="mono">refactor(auth): simplify token refresh</td>
  </tr>
  <tr>
    <td><span class="type-pill">test</span></td>
    <td>Adding or fixing tests</td>
    <td class="mono">test: add coverage for edge cases</td>
  </tr>
  <tr>
    <td><span class="type-pill">chore</span></td>
    <td>Build process, tooling, dependencies</td>
    <td class="mono">chore: bump node to v20</td>
  </tr>
  <tr>
    <td><span class="type-pill">perf</span></td>
    <td>Performance improvement</td>
    <td class="mono">perf(db): add index on user_id column</td>
  </tr>
  <tr>
    <td><span class="type-pill">revert</span></td>
    <td>Undoing a previous commit</td>
    <td class="mono">revert: feat(cart) add quantity selector</td>
  </tr>
</table>

---

<!-- _class: final -->

# Your git log is a
# gift to your future self.

&nbsp;

Type. Scope. Imperative description. Under 72 chars. Done.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*