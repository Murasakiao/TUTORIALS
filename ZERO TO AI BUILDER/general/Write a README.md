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

  /* GitHub README mock */
  .gh-window {
    background: #0d1117;
    border-radius: 10px;
    overflow: hidden;
    margin: 12px 0;
    font-size: 13px;
  }

  .gh-bar {
    background: #161b22;
    padding: 9px 16px;
    display: flex;
    align-items: center;
    gap: 10px;
    border-bottom: 1px solid #30363d;
  }

  .gh-bar .gh-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #30363d;
    display: inline-block;
  }

  .gh-bar .gh-title {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: #8b949e;
  }

  .gh-bar .gh-tabs {
    margin-left: auto;
    display: flex;
    gap: 16px;
    font-family: 'DM Sans', sans-serif;
    font-size: 12px;
    color: #8b949e;
  }

  .gh-bar .gh-tabs .active {
    color: #f0f6fc;
    border-bottom: 2px solid #f78166;
    padding-bottom: 2px;
  }

  .gh-body {
    padding: 18px 22px;
    line-height: 1.8;
  }

  .gh-body .md-h1 {
    font-family: 'DM Sans', sans-serif;
    font-size: 20px;
    font-weight: 600;
    color: #f0f6fc;
    margin-bottom: 4px;
    border-bottom: 1px solid #30363d;
    padding-bottom: 8px;
  }

  .gh-body .md-h2 {
    font-family: 'DM Sans', sans-serif;
    font-size: 15px;
    font-weight: 600;
    color: #f0f6fc;
    margin-top: 14px;
    margin-bottom: 4px;
    border-bottom: 1px solid #21262d;
    padding-bottom: 4px;
  }

  .gh-body .md-p {
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    color: #8b949e;
    margin-bottom: 8px;
  }

  .gh-body .md-code {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 8px 12px;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: #79c0ff;
    margin: 6px 0;
  }

  .gh-body .md-li {
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    color: #8b949e;
    margin-bottom: 4px;
    padding-left: 14px;
  }

  .gh-body .md-li::before {
    content: "•";
    color: #6e7681;
    margin-right: 8px;
  }

  /* Badge row */
  .badge-row {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin: 10px 0;
  }

  .badge {
    height: 20px;
    border-radius: 4px;
    display: inline-flex;
    align-items: center;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    overflow: hidden;
  }

  .badge .badge-label {
    background: #555;
    color: #fff;
    padding: 0 7px;
    height: 100%;
    display: flex;
    align-items: center;
  }

  .badge .badge-value {
    padding: 0 7px;
    height: 100%;
    display: flex;
    align-items: center;
    color: #fff;
  }

  .badge .badge-value.green  { background: #2ea44f; }
  .badge .badge-value.blue   { background: #0075ca; }
  .badge .badge-value.yellow { background: #e7b009; }
  .badge .badge-value.orange { background: #e05d44; }

  /* Before / after README compare */
  .readme-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 14px 0;
  }

  .readme-card {
    border-radius: 10px;
    overflow: hidden;
  }

  .readme-card .rc-label {
    padding: 7px 14px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 600;
  }

  .readme-card.before .rc-label { background: #7f1d1d; color: #fca5a5; }
  .readme-card.after  .rc-label { background: #14532d; color: #86efac; }

  .readme-card .rc-body {
    background: #0d1117;
    padding: 14px 16px;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    line-height: 2;
    color: #8b949e;
  }

  .readme-card.before .rc-body { border: 1px solid #7f1d1d; border-top: none; border-radius: 0 0 10px 10px; }
  .readme-card.after  .rc-body { border: 1px solid #14532d; border-top: none; border-radius: 0 0 10px 10px; }

  .readme-card .rc-body .good { color: #86efac; }
  .readme-card .rc-body .bad  { color: #f87171; }

  /* Section anatomy grid */
  .section-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 12px;
  }

  .section-card {
    background: #111827;
    border-radius: 8px;
    padding: 13px 16px;
    display: flex;
    gap: 12px;
    align-items: flex-start;
  }

  .section-card .sc-num {
    font-family: 'DM Mono', monospace;
    font-size: 18px;
    font-weight: 600;
    color: #2563eb;
    min-width: 24px;
    line-height: 1.4;
  }

  .section-card .sc-body .sc-title {
    font-weight: 600;
    font-size: 14px;
    color: #f0f6fc;
    margin-bottom: 2px;
  }

  .section-card .sc-body .sc-desc {
    font-size: 12px;
    color: #6b7280;
    line-height: 1.5;
  }

  /* Markdown reference block */
  .md-ref {
    background: #111827;
    border-radius: 8px;
    padding: 16px 20px;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #e5e7eb;
    line-height: 2;
    margin: 12px 0;
  }

  .md-ref .md-kw  { color: #c4b5fd; }
  .md-ref .md-str { color: #86efac; }
  .md-ref .md-url { color: #60a5fa; }
  .md-ref .md-cmt { color: #4b5563; font-style: italic; }

  /* Two-column */
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

# Write a README That Gets You Noticed
## on GitHub

&nbsp;

**Your repo's first impression.** Most developers skip it. That's your advantage.

`markdown` · `badges` · `structure` · `before/after`

---

## Why README Matters

A README is the front page of your project. It does more work than the code itself.

<div class="tools">
  <div class="tool-card">
    <div class="icon">👀</div>
    <div class="name">First thing visitors see</div>
    <div class="desc">GitHub renders README.md automatically below the file list. No readme = no context.</div>
  </div>
  <div class="tool-card">
    <div class="icon">💼</div>
    <div class="name">Portfolio signal</div>
    <div class="desc">A polished README tells employers and collaborators you care about your craft.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔍</div>
    <div class="name">Searchability</div>
    <div class="desc">GitHub indexes README content. The right keywords help people find your work.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🤝</div>
    <div class="name">Collaboration</div>
    <div class="desc">Contributors can't help you if they don't understand how to install or run your project.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## The 5 Sections Every Good README Has

<div class="section-grid">
  <div class="section-card">
    <div class="sc-num">01</div>
    <div class="sc-body">
      <div class="sc-title">Title + One-line Description</div>
      <div class="sc-desc">What is this? Answer in one sentence. No jargon.</div>
    </div>
  </div>
  <div class="section-card">
    <div class="sc-num">02</div>
    <div class="sc-body">
      <div class="sc-title">Demo or Screenshot</div>
      <div class="sc-desc">Show it working. A GIF or image does more than 10 paragraphs.</div>
    </div>
  </div>
  <div class="section-card">
    <div class="sc-num">03</div>
    <div class="sc-body">
      <div class="sc-title">Installation</div>
      <div class="sc-desc">Exact commands to get it running from a fresh machine. No assumptions.</div>
    </div>
  </div>
  <div class="section-card">
    <div class="sc-num">04</div>
    <div class="sc-body">
      <div class="sc-title">Usage</div>
      <div class="sc-desc">How to actually use it once installed. Code examples over prose.</div>
    </div>
  </div>
</div>

&nbsp;

The 5th section — **Tech Stack / Built With** — is optional but adds credibility and searchability. List the key languages and frameworks only.

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Badges, Screenshots, and GIFs

These three elements separate a skimmable README from a wall of text.

**Badges** — tiny status indicators generated from shields.io:

<div class="badge-row">
  <div class="badge"><span class="badge-label">python</span><span class="badge-value blue">3.11+</span></div>
  <div class="badge"><span class="badge-label">license</span><span class="badge-value green">MIT</span></div>
  <div class="badge"><span class="badge-label">build</span><span class="badge-value green">passing</span></div>
  <div class="badge"><span class="badge-label">version</span><span class="badge-value yellow">1.0.0</span></div>
</div>

<div class="md-ref">
  <span class="md-cmt">&lt;!-- Badge syntax --&gt;</span><br>
  ![<span class="md-str">Python</span>](<span class="md-url">https://img.shields.io/badge/python-3.11+-blue</span>)<br>
  ![<span class="md-str">License</span>](<span class="md-url">https://img.shields.io/badge/license-MIT-green</span>)<br>
  <br>
  <span class="md-cmt">&lt;!-- Screenshot --&gt;</span><br>
  ![<span class="md-str">App screenshot</span>](<span class="md-url">assets/screenshot.png</span>)<br>
  <br>
  <span class="md-cmt">&lt;!-- GIF demo --&gt;</span><br>
  ![<span class="md-str">Demo</span>](<span class="md-url">assets/demo.gif</span>)
</div>

For GIFs: record with **QuickTime** (Mac) or **ScreenToGif** (Windows), keep under 5MB.

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## README Template

Copy this structure for every project:

<div class="md-ref">
  <span class="md-kw"># Project Name</span><br>
  One sentence. What it does and who it's for.<br>
  <br>
  ![<span class="md-str">demo</span>](<span class="md-url">assets/demo.gif</span>) <span class="md-cmt">&lt;!-- or screenshot --&gt;</span><br>
  <br>
  <span class="md-kw">## Installation</span><br>
  ```bash<br>
  git clone https://github.com/you/project<br>
  cd project<br>
  pip install -r requirements.txt<br>
  ```<br>
  <span class="md-kw">## Usage</span><br>
  ```python<br>
  from project import main<br>
  main.run()<br>
  ```<br>
  <span class="md-kw">## Built With</span><br>
  - Python 3.11 · pandas · Flask<br>
  <br>
  <span class="md-kw">## License</span><br>
  MIT
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Real Before / After

<div class="readme-compare">
  <div class="readme-card before">
    <div class="rc-label">❌ Before — what most repos look like</div>
    <div class="rc-body">
      <span class="bad"># my project</span><br>
      <br>
      this is my project for data<br>
      analysis. run main.py to start<br>
      <br>
      requires python
    </div>
  </div>
  <div class="readme-card after">
    <div class="rc-label">✅ After — what a good README looks like</div>
    <div class="rc-body">
      <span class="good"># SalesLens 📊</span><br>
      <span style="color:#8b949e">Automated regional sales report generator for CSV exports.</span><br>
      <br>
      <span style="color:#60a5fa">![Python](https://img.shields.io/badge/python-3.11-blue)</span><br>
      <br>
      <span class="good">## Installation</span><br>
      <span style="color:#fde68a">pip install -r requirements.txt</span><br>
      <br>
      <span class="good">## Usage</span><br>
      <span style="color:#fde68a">python main.py --input sales.csv</span><br>
      <br>
      <span class="good">## Built With</span><br>
      <span style="color:#8b949e">Python · pandas · matplotlib</span>
    </div>
  </div>
</div>

Same project. The "after" takes 10 extra minutes to write and signals a completely different level of care.

---

## Quick Reference

<div class="two-col">
  <div class="col-card">
    <div class="label">✅ Always include</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">
      ✦ Project name + one-line description<br>
      ✦ Installation commands (exact, copy-pasteable)<br>
      ✦ Usage example with real code<br>
      ✦ At least one screenshot or GIF<br>
      ✦ License line at the bottom
    </p>
  </div>
  <div class="col-card">
    <div class="label">⚠️ Common mistakes</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">
      ✦ "See code for details" — never do this<br>
      ✦ Assuming the reader knows your setup<br>
      ✦ No visuals — text-only READMEs get skipped<br>
      ✦ Outdated install steps that no longer work<br>
      ✦ Writing it last — write it as you build
    </p>
  </div>
</div>

<div class="highlight">

**Shortcut:** paste your project description into Claude and ask it to generate a README draft using the 5-section structure. Edit from there — faster than starting from a blank file.

</div>

---

<!-- _class: final -->

# Your code deserves
# a front door.

&nbsp;

A great README turns a repo into a project. Takes 20 minutes. Lasts forever.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*