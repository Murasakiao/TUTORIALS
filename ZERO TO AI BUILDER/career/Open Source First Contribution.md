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

  /* ── Code / terminal block ── */
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
  .cb-out    { color: #9ca3af; }
  .cb-cmt    { color: #4b5563; font-style: italic; }
  .cb-hi     { color: #34d399; }
  .cb-str    { color: #fde68a; }
  .cb-kw     { color: #c084fc; }

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

  /* ── Open source definition split ── */
  .os-split {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0;
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 16px 0;
  }

  .os-side { padding: 18px 20px; }
  .os-side.closed { background: var(--off-white); border-right: 1px solid var(--border); }
  .os-side.open   { background: #f0fdf4; }

  .os-side .os-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 8px;
  }

  .os-side.closed .os-label { color: var(--muted); }
  .os-side.open   .os-label { color: #166534; }

  .os-side .os-title {
    font-weight: 700;
    font-size: 17px;
    color: var(--text);
    margin-bottom: 10px;
  }

  .os-side .os-item {
    font-size: 13px;
    color: var(--muted);
    padding: 5px 0;
    border-bottom: 1px solid var(--border);
    display: flex;
    gap: 8px;
    align-items: flex-start;
    line-height: 1.5;
  }

  .os-side.open .os-item { color: var(--text); border-color: #bbf7d0; }
  .os-side .os-item:last-child { border-bottom: none; }

  /* ── Why contribute benefit cards ── */
  .benefit-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .benefit-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 13px 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }

  .benefit-card .bc-icon { font-size: 22px; flex-shrink: 0; }

  .benefit-card .bc-title {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
    margin-bottom: 3px;
  }

  .benefit-card .bc-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.5;
  }

  /* ── Issue finder card ── */
  .issue-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
    margin: 14px 0;
  }

  .issue-card .ic-bar {
    background: #1f2937;
    padding: 9px 16px;
    display: flex;
    align-items: center;
    gap: 8px;
    font-family: 'DM Mono', monospace;
    font-size: 11.5px;
    color: #6b7280;
  }

  .issue-card .ic-bar .ib-dot {
    width: 11px; height: 11px; border-radius: 50%;
  }
  .ib-dot.r { background: #ef4444; }
  .ib-dot.y { background: #f59e0b; }
  .ib-dot.g { background: #22c55e; }

  .issue-card .ic-body {
    padding: 12px 16px;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .issue-row {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 9px 12px;
    border: 1px solid var(--border);
    border-radius: 8px;
    background: var(--off-white);
  }

  .issue-row .ir-icon { font-size: 16px; flex-shrink: 0; color: #22c55e; }

  .issue-row .ir-title {
    font-size: 13px;
    color: var(--text);
    font-weight: 500;
    flex: 1;
  }

  .issue-row .ir-labels {
    display: flex;
    gap: 5px;
    flex-shrink: 0;
  }

  .ir-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    padding: 2px 8px;
    border-radius: 999px;
    font-weight: 500;
  }

  .ir-label.good-first { background: #7c3aed; color: white; }
  .ir-label.docs       { background: #0ea5e9; color: white; }
  .ir-label.bug        { background: #dc2626; color: white; }
  .ir-label.help       { background: #d97706; color: white; }
  .ir-label.easy       { background: #16a34a; color: white; }

  .issue-row .ir-repo {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    flex-shrink: 0;
  }

  /* ── Fork → fix → PR workflow ── */
  .workflow-steps {
    display: flex;
    flex-direction: column;
    gap: 0;
    margin: 14px 0;
  }

  .wf-step {
    display: flex;
    align-items: stretch;
    gap: 0;
  }

  .wf-step .wfs-timeline {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 44px;
    flex-shrink: 0;
  }

  .wf-step .wfs-dot {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: var(--blue);
    border: 2px solid var(--white);
    box-shadow: 0 0 0 2px var(--blue);
    flex-shrink: 0;
    margin-top: 14px;
  }

  .wf-step .wfs-line {
    width: 2px;
    flex: 1;
    background: var(--border);
    margin-top: 4px;
    margin-bottom: -4px;
  }

  .wf-step:last-child .wfs-line { display: none; }

  .wf-step .wfs-content {
    flex: 1;
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 11px 16px;
    margin: 6px 0 6px 10px;
  }

  .wf-step .wfs-content .wfsc-step {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--blue);
    font-weight: 600;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    margin-bottom: 2px;
  }

  .wf-step .wfs-content .wfsc-title {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
    margin-bottom: 2px;
  }

  .wf-step .wfs-content .wfsc-cmd {
    font-family: 'DM Mono', monospace;
    font-size: 11.5px;
    color: var(--blue);
    margin-top: 3px;
  }

  .wf-step .wfs-content .wfsc-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.5;
  }

  /* ── PR message mock ── */
  .pr-mock {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
    margin: 14px 0;
  }

  .pr-mock .pm-header {
    background: var(--off-white);
    padding: 12px 16px;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .pr-mock .pm-icon { font-size: 18px; }

  .pr-mock .pm-title {
    font-weight: 600;
    font-size: 14px;
    color: var(--text);
  }

  .pr-mock .pm-badge {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    padding: 2px 8px;
    border-radius: 999px;
    margin-left: auto;
    font-weight: 500;
  }

  .pm-badge.open { background: #dcfce7; color: #166534; border: 1px solid #86efac; }

  .pr-mock .pm-body {
    padding: 14px 16px;
    font-size: 13.5px;
    color: var(--text);
    line-height: 1.75;
  }

  .pr-mock .pm-section {
    margin-bottom: 12px;
  }

  .pr-mock .pm-section .pms-label {
    font-weight: 600;
    font-size: 13px;
    color: var(--text);
    margin-bottom: 4px;
  }

  .pr-mock .pm-section .pms-content {
    font-size: 13px;
    color: var(--muted);
    line-height: 1.65;
    padding-left: 4px;
  }

  .pr-mock .pm-section .pms-check {
    display: flex;
    align-items: baseline;
    gap: 7px;
    font-size: 13px;
    color: var(--muted);
    padding: 2px 0;
  }

  .pm-tick { color: #22c55e; flex-shrink: 0; font-size: 12px; }
  .pm-box  { color: var(--border); flex-shrink: 0; font-size: 12px; }

  /* ── Where to find repos ── */
  .find-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .find-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 13px 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }

  .find-card .fc-icon { font-size: 22px; flex-shrink: 0; }

  .find-card .fc-name {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
    margin-bottom: 2px;
  }

  .find-card .fc-url {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    color: var(--blue);
    margin-bottom: 4px;
  }

  .find-card .fc-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.5;
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

# Open Source
## and Your First Contribution

&nbsp;

**Someone else's code is waiting for your fix.** Here's exactly how to make it happen.

`fork` · `clone` · `branch` · `commit` · `pull request` · `good first issue`

---

## What Open Source Means

Open source software is code that anyone can read, use, modify, and contribute to — for free, in public.

<div class="os-split">
  <div class="os-side closed">
    <div class="os-label">🔒 &nbsp;Closed source</div>
    <div class="os-title">Private code. Read-only.</div>
    <div class="os-item">→ Code is proprietary — employees only</div>
    <div class="os-item">→ You use the product, not the code</div>
    <div class="os-item">→ Can't see how it works internally</div>
    <div class="os-item">→ Can't fix bugs yourself</div>
    <div class="os-item">→ Examples: Photoshop, Windows, Slack</div>
  </div>
  <div class="os-side open">
    <div class="os-label">🌍 &nbsp;Open source</div>
    <div class="os-title">Public code. Anyone can contribute.</div>
    <div class="os-item">→ Code lives on GitHub, fully readable</div>
    <div class="os-item">→ Anyone can suggest changes</div>
    <div class="os-item">→ You can see exactly how it works</div>
    <div class="os-item">→ Bugs get fixed by the community</div>
    <div class="os-item">→ Examples: Python, Linux, VS Code, React</div>
  </div>
</div>

<div class="highlight" style="margin-top:4px;">

**The tools you use every day are open source.** Python, Git, Firefox, WordPress, pandas, NumPy — maintained by thousands of volunteers making small improvements, one pull request at a time.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Why Contribute — Learning + Credibility

Contributing to open source is the most underrated learning accelerator in software development.

<div class="benefit-grid">
  <div class="benefit-card">
    <div class="bc-icon">📖</div>
    <div>
      <div class="bc-title">Read professional codebases</div>
      <div class="bc-desc">Real projects show you patterns no tutorial teaches — naming conventions, test structure, PR reviews, code organisation at scale.</div>
    </div>
  </div>
  <div class="benefit-card">
    <div class="bc-icon">💼</div>
    <div>
      <div class="bc-title">Proof of work — public and permanent</div>
      <div class="bc-desc">A merged pull request is verifiable. Employers can click it. It proves you can navigate a real codebase, write clear explanations, and respond to review.</div>
    </div>
  </div>
  <div class="benefit-card">
    <div class="bc-icon">🔍</div>
    <div>
      <div class="bc-title">See how code review works</div>
      <div class="bc-desc">Maintainers leave detailed feedback on your PR. This is free mentorship from experienced engineers who have strong opinions about code quality.</div>
    </div>
  </div>
  <div class="benefit-card">
    <div class="bc-icon">🌐</div>
    <div>
      <div class="bc-title">Join a real community</div>
      <div class="bc-desc">Open source projects have Discord servers, mailing lists, and contributors across the world. Your first PR is an introduction to a professional network.</div>
    </div>
  </div>
  <div class="benefit-card">
    <div class="bc-icon">🛠️</div>
    <div>
      <div class="bc-title">Fix something that actually matters</div>
      <div class="bc-desc">A bug you fix in a library used by 10,000 projects improves the software of everyone downstream. The impact is immediate and real.</div>
    </div>
  </div>
  <div class="benefit-card">
    <div class="bc-icon">✅</div>
    <div>
      <div class="bc-title">Your first contribution is tiny</div>
      <div class="bc-desc">Nobody expects brilliance from a first PR. A typo fix, a missing docstring, a broken link — these are all valid and welcomed contributions.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Find Beginner Issues — the "good first issue" Label

GitHub's `good first issue` label exists specifically for first-time contributors. Maintainers tag issues that don't require deep project knowledge.

<div class="issue-card">
  <div class="ic-bar">
    <span class="ib-dot r"></span>
    <span class="ib-dot y"></span>
    <span class="ib-dot g"></span>
    <span style="margin-left:8px;">github.com — issues labelled "good first issue"</span>
  </div>
  <div class="ic-body">
    <div class="issue-row">
      <div class="ir-icon">●</div>
      <div class="ir-title">Fix typo in CONTRIBUTING.md — "recieve" → "receive"</div>
      <div class="ir-labels">
        <span class="ir-label good-first">good first issue</span>
        <span class="ir-label docs">docs</span>
      </div>
      <div class="ir-repo">requests/requests</div>
    </div>
    <div class="issue-row">
      <div class="ir-icon">●</div>
      <div class="ir-title">Add missing type hints to utils.py functions</div>
      <div class="ir-labels">
        <span class="ir-label good-first">good first issue</span>
        <span class="ir-label easy">easy</span>
      </div>
      <div class="ir-repo">psf/black</div>
    </div>
    <div class="issue-row">
      <div class="ir-icon">●</div>
      <div class="ir-title">Error message is unclear when API key is missing</div>
      <div class="ir-labels">
        <span class="ir-label good-first">good first issue</span>
        <span class="ir-label bug">bug</span>
      </div>
      <div class="ir-repo">anthropics/anthropic-sdk</div>
    </div>
    <div class="issue-row">
      <div class="ir-icon">●</div>
      <div class="ir-title">Add example for pagination to README</div>
      <div class="ir-labels">
        <span class="ir-label good-first">good first issue</span>
        <span class="ir-label help">help wanted</span>
      </div>
      <div class="ir-repo">encode/httpx</div>
    </div>
  </div>
</div>

<div class="highlight">

**Search GitHub:** `label:"good first issue" language:Python is:open` — filter by any language. Or visit **goodfirstissue.dev** and **firstcontributions.github.io** for curated beginner-friendly lists.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Where to Find Good First Repos

<div class="find-grid">
  <div class="find-card">
    <div class="fc-icon">🔍</div>
    <div>
      <div class="fc-name">GitHub search</div>
      <div class="fc-url">github.com/search?q=label:"good+first+issue"</div>
      <div class="fc-desc">Filter by language, topic, and date. Sort by "recently updated" to find active repos with responsive maintainers.</div>
    </div>
  </div>
  <div class="find-card">
    <div class="fc-icon">🌱</div>
    <div>
      <div class="fc-name">Good First Issue</div>
      <div class="fc-url">goodfirstissue.dev</div>
      <div class="fc-desc">Curated directory of beginner-friendly issues across popular projects. Filter by language. Updated daily.</div>
    </div>
  </div>
  <div class="find-card">
    <div class="fc-icon">🤝</div>
    <div>
      <div class="fc-name">First Contributions</div>
      <div class="fc-url">firstcontributions.github.io</div>
      <div class="fc-desc">A practice repo specifically for beginners. Make your very first PR here before touching a real project — zero pressure, instant merge.</div>
    </div>
  </div>
  <div class="find-card">
    <div class="fc-icon">🐍</div>
    <div>
      <div class="fc-name">Tools you already use</div>
      <div class="fc-url">github.com/psf/requests · pandas-dev/pandas</div>
      <div class="fc-desc">The best first contribution is to something you've actually run. You already know what the project does — half the onboarding is done.</div>
    </div>
  </div>
</div>

<div class="two-col" style="margin-top:14px;">
  <div class="col-card">
    <div class="label">Signs of a welcoming repo</div>
    <ul style="margin-top:6px; padding-left:1.2em;">
      <li style="font-size:13px;">Has a CONTRIBUTING.md file</li>
      <li style="font-size:13px;">Issues get responses within days</li>
      <li style="font-size:13px;">PRs get reviewed, not just merged or ghosted</li>
      <li style="font-size:13px;">Maintainers say "thank you" in comments</li>
    </ul>
  </div>
  <div class="col-card">
    <div class="label">Signs to avoid (for your first PR)</div>
    <ul style="margin-top:6px; padding-left:1.2em;">
      <li style="font-size:13px;">Last commit was more than a year ago</li>
      <li style="font-size:13px;">Issues go unanswered for months</li>
      <li style="font-size:13px;">No CONTRIBUTING.md or setup docs</li>
      <li style="font-size:13px;">Terse or dismissive responses to newcomers</li>
    </ul>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Fork → Fix → PR — The Full Workflow

<div class="workflow-steps">
  <div class="wf-step">
    <div class="wfs-timeline"><div class="wfs-dot"></div><div class="wfs-line"></div></div>
    <div class="wfs-content">
      <div class="wfsc-step">Step 1</div>
      <div class="wfsc-title">Fork the repo</div>
      <div class="wfsc-desc">Click "Fork" on GitHub. This creates a copy of the repo under your account. You can push to your fork — you can't push directly to the original.</div>
    </div>
  </div>
  <div class="wf-step">
    <div class="wfs-timeline"><div class="wfs-dot"></div><div class="wfs-line"></div></div>
    <div class="wfs-content">
      <div class="wfsc-step">Step 2</div>
      <div class="wfsc-title">Clone your fork locally</div>
      <div class="wfsc-cmd">git clone https://github.com/YOUR-NAME/repo.git</div>
    </div>
  </div>
  <div class="wf-step">
    <div class="wfs-timeline"><div class="wfs-dot"></div><div class="wfs-line"></div></div>
    <div class="wfs-content">
      <div class="wfsc-step">Step 3</div>
      <div class="wfsc-title">Create a branch for your fix</div>
      <div class="wfsc-cmd">git checkout -b fix/typo-in-contributing-docs</div>
      <div class="wfsc-desc">Never work on <code>main</code>. A descriptive branch name makes your PR easier to review.</div>
    </div>
  </div>
  <div class="wf-step">
    <div class="wfs-timeline"><div class="wfs-dot"></div><div class="wfs-line"></div></div>
    <div class="wfs-content">
      <div class="wfsc-step">Step 4</div>
      <div class="wfsc-title">Make the fix, commit with a good message</div>
      <div class="wfsc-cmd">git add . &amp;&amp; git commit -m "fix: correct typo in CONTRIBUTING.md"</div>
    </div>
  </div>
  <div class="wf-step">
    <div class="wfs-timeline"><div class="wfs-dot"></div><div class="wfs-line"></div></div>
    <div class="wfs-content">
      <div class="wfsc-step">Step 5</div>
      <div class="wfsc-title">Push to your fork</div>
      <div class="wfsc-cmd">git push origin fix/typo-in-contributing-docs</div>
    </div>
  </div>
  <div class="wf-step">
    <div class="wfs-timeline"><div class="wfs-dot"></div><div class="wfs-line"></div></div>
    <div class="wfs-content">
      <div class="wfsc-step">Step 6</div>
      <div class="wfsc-title">Open the Pull Request on GitHub</div>
      <div class="wfsc-desc">GitHub shows a "Compare &amp; pull request" banner automatically after you push. Click it. Write your PR description (next slide). Submit.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 04</div>

## What to Say in Your Pull Request

A good PR description answers three questions before the maintainer has to ask them.

<div class="pr-mock">
  <div class="pm-header">
    <div class="pm-icon">🔀</div>
    <div class="pm-title">fix: correct typo in CONTRIBUTING.md</div>
    <div class="pm-badge open">Open</div>
  </div>
  <div class="pm-body">
    <div class="pm-section">
      <div class="pms-label">What does this PR do?</div>
      <div class="pms-content">Fixes a typo on line 34 of CONTRIBUTING.md: "recieve" → "receive". Closes #217.</div>
    </div>
    <div class="pm-section">
      <div class="pms-label">Why is it needed?</div>
      <div class="pms-content">The CONTRIBUTING guide is the first thing new contributors read. A spelling error undermines trust and makes the project look unmaintained.</div>
    </div>
    <div class="pm-section">
      <div class="pms-label">How was it tested?</div>
      <div class="pms-content">Verified the word appears correctly in the rendered Markdown preview on GitHub. No code changes — documentation only.</div>
    </div>
    <div class="pm-section">
      <div class="pms-label">Checklist</div>
      <div class="pms-check"><span class="pm-tick">✓</span> I have read the CONTRIBUTING guidelines</div>
      <div class="pms-check"><span class="pm-tick">✓</span> The change is limited in scope — one issue, one fix</div>
      <div class="pms-check"><span class="pm-tick">✓</span> No unrelated changes included in this PR</div>
      <div class="pms-check"><span class="pm-box">☐</span> Tests added (not applicable — docs-only change)</div>
    </div>
  </div>
</div>

<div class="highlight">

**The golden rule:** Make the reviewer's job easy. Short description. Specific change. Link to the issue. Explain any non-obvious decisions. Never say "I hope this is helpful" — say what you did and why.

</div>

---

## Open Source Quick Reference

<table class="cheat-table">
  <tr>
    <th>Task</th>
    <th>How to do it</th>
  </tr>
  <tr>
    <td>Find beginner issues</td>
    <td>GitHub search: <code>label:"good first issue" language:Python is:open</code></td>
  </tr>
  <tr>
    <td>Practice before the real thing</td>
    <td>Make a PR at firstcontributions.github.io first — zero pressure</td>
  </tr>
  <tr>
    <td>Fork a repo</td>
    <td>Click Fork on GitHub → your copy appears at github.com/you/repo</td>
  </tr>
  <tr>
    <td>Clone your fork</td>
    <td class="mono">git clone https://github.com/YOU/repo.git</td>
  </tr>
  <tr>
    <td>Create a fix branch</td>
    <td class="mono">git checkout -b fix/description-of-change</td>
  </tr>
  <tr>
    <td>Commit your fix</td>
    <td class="mono">git add . && git commit -m "fix: what you fixed"</td>
  </tr>
  <tr>
    <td>Push to your fork</td>
    <td class="mono">git push origin fix/description-of-change</td>
  </tr>
  <tr>
    <td>Open a PR</td>
    <td>GitHub shows "Compare &amp; pull request" — click it, fill in the description</td>
  </tr>
  <tr>
    <td>PR description must include</td>
    <td>What it does · Why it's needed · How it was tested · Issue number it closes</td>
  </tr>
  <tr>
    <td>If maintainer requests changes</td>
    <td>Make the changes on the same branch and push — the PR updates automatically</td>
  </tr>
  <tr>
    <td>After it's merged</td>
    <td>Delete the branch locally: <code>git branch -d fix/your-branch</code></td>
  </tr>
</table>

---

<!-- _class: final -->

# Someone tagged it
# "good first issue"
# because they want your help.

&nbsp;

Fork. Fix one thing. Write one clear description. Submit.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*