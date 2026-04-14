---
marp: true
theme: default
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=DM+Mono:wght@400;500&display=swap');

  :root {
    --purple: #2563eb;
    --purple-light: #f5f3ff;
    --purple-mid: #ddd6fe;
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
    border-bottom: 2px solid var(--purple);
    padding-bottom: 10px;
    margin-bottom: 24px;
  }

  h3 {
    font-family: 'DM Sans', sans-serif;
    font-size: 20px;
    font-weight: 500;
    color: var(--purple);
    margin-bottom: 8px;
  }

  p { color: var(--text); margin: 0.4em 0; }
  ul { padding-left: 1.4em; }
  li { margin-bottom: 10px; color: var(--text); }
  strong { color: var(--purple); font-weight: 600; }

  code {
    font-family: 'DM Mono', monospace;
    background: var(--purple-light);
    color: var(--purple);
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.88em;
  }

  blockquote {
    border-left: 4px solid var(--purple);
    background: var(--purple-light);
    padding: 16px 20px;
    margin: 20px 0;
    border-radius: 0 8px 8px 0;
    font-family: 'DM Mono', monospace;
    font-size: 0.82em;
    color: #4c1d95;
    line-height: 1.6;
  }

  blockquote p { color: #4c1d95; margin: 0; }

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
    background: var(--purple-light);
    border: 1px solid var(--purple-mid);
    border-radius: 10px;
    padding: 18px 24px;
    margin: 16px 0;
  }

  .step-badge {
    display: inline-block;
    background: var(--purple);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    padding: 4px 14px;
    border-radius: 999px;
    margin-bottom: 12px;
    letter-spacing: 0.05em;
  }

  /* Where Markdown is used — platform cards */
  .platforms {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    margin-top: 20px;
  }

  .platform-card {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 18px 16px;
  }

  .platform-card .icon { font-size: 28px; margin-bottom: 8px; }
  .platform-card .name { font-weight: 600; font-size: 15px; color: var(--text); }
  .platform-card .desc { font-size: 12px; color: var(--muted); margin-top: 4px; line-height: 1.4; }

  /* Side-by-side syntax comparison */
  .syntax-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 16px;
  }

  .syn-col {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .syn-col .syn-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    padding: 8px 16px;
  }

  .syn-col.raw .syn-label  { background: #111827; color: #6b7280; }
  .syn-col.out .syn-label  { background: var(--purple); color: white; }

  .syn-col .syn-body {
    padding: 14px 18px;
    font-size: 14px;
    line-height: 2;
  }

  .syn-col.raw .syn-body {
    background: #1e1e2e;
    font-family: 'DM Mono', monospace;
    color: #cdd6f4;
  }

  .syn-col.out .syn-body {
    background: var(--purple-light);
    color: var(--text);
  }

  .syn-col.raw .syn-body .c-punct { color: #89b4fa; }
  .syn-col.raw .syn-body .c-text  { color: #cdd6f4; }
  .syn-col.raw .syn-body .c-bold  { color: #f38ba8; }
  .syn-col.raw .syn-body .c-em    { color: #a6e3a1; }

  /* Code block demo */
  .dark-block {
    background: #111827;
    border-radius: 10px;
    overflow: hidden;
    margin: 16px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .dark-block .bar {
    background: #1f2937;
    padding: 8px 16px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .dark-block .bar .dot {
    width: 11px; height: 11px;
    border-radius: 50%;
    display: inline-block;
  }

  .dark-block .bar .dot.r { background: #ef4444; }
  .dark-block .bar .dot.y { background: #f59e0b; }
  .dark-block .bar .dot.g { background: #22c55e; }
  .dark-block .bar .lang  { font-size: 11px; color: #6b7280; margin-left: 8px; }

  .dark-block .body {
    padding: 16px 20px;
    line-height: 1.9;
  }

  .dark-block .kw   { color: #c084fc; }
  .dark-block .fn   { color: #60a5fa; }
  .dark-block .str  { color: #86efac; }
  .dark-block .cmt  { color: #4b5563; font-style: italic; }
  .dark-block .def  { color: #f9fafb; }

  /* Lists cheatsheet grid */
  .list-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 16px;
  }

  .list-card {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
  }

  .list-card .lc-label {
    background: var(--purple);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    padding: 7px 14px;
  }

  .list-card .lc-body {
    padding: 12px 16px;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    line-height: 1.9;
    color: var(--text);
  }

  .list-card .lc-body .dim { color: var(--muted); }

  /* Table demo */
  .md-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
    margin: 16px 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .md-table th {
    background: var(--purple);
    color: white;
    padding: 10px 16px;
    text-align: left;
    font-weight: 600;
    font-size: 13px;
  }

  .md-table td {
    padding: 9px 16px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
    font-size: 13px;
  }

  .md-table tr:nth-child(even) td { background: var(--off-white); }
  .md-table .mono {
    font-family: 'DM Mono', monospace;
    color: var(--purple);
    font-size: 12px;
  }

  /* README practice block */
  .readme-box {
    background: #111827;
    border-radius: 10px;
    padding: 20px 24px;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    line-height: 2;
    margin: 16px 0;
  }

  .readme-box .r-h1    { color: #c084fc; font-weight: 600; font-size: 15px; }
  .readme-box .r-h2    { color: #818cf8; font-weight: 600; }
  .readme-box .r-bold  { color: #f9fafb; font-weight: 600; }
  .readme-box .r-text  { color: #9ca3af; }
  .readme-box .r-code  { color: #86efac; }
  .readme-box .r-link  { color: #60a5fa; }
  .readme-box .r-dim   { color: #374151; }

  /* Two column layout */
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

  section.final {
    background: var(--purple);
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
  }

  section.final h1 { color: white; font-size: 40px; }
  section.final p  { color: #ddd6fe; font-size: 18px; }
  section.final strong { color: white; }
  section.final em { color: #ddd6fe; }

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
    background: var(--purple);
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

# Markdown in 10 Minutes
## Write once. Render everywhere.

&nbsp;

**Plain text with superpowers.** No software needed, no formatting toolbar.

`#` · `**bold**` · `- list` · `` `code` `` · `[link](url)`

---

## Where Is Markdown Used?

Markdown is the quiet language behind most of the tools developers — and creators — use every day.

<div class="platforms">
  <div class="platform-card">
    <div class="icon">🐙</div>
    <div class="name">GitHub</div>
    <div class="desc">Every README, issue, pull request, and wiki is written in Markdown.</div>
  </div>
  <div class="platform-card">
    <div class="icon">🗒️</div>
    <div class="name">Notion</div>
    <div class="desc">Type <code>/</code> or use Markdown shortcuts — it converts on the fly.</div>
  </div>
  <div class="platform-card">
    <div class="icon">✍️</div>
    <div class="name">Substack</div>
    <div class="desc">Writers paste Markdown directly. Clean formatting with zero clicking.</div>
  </div>
  <div class="platform-card">
    <div class="icon">💬</div>
    <div class="name">Slack & Discord</div>
    <div class="desc">Bold, italic, and code blocks all use Markdown syntax.</div>
  </div>
  <div class="platform-card">
    <div class="icon">📝</div>
    <div class="name">VS Code</div>
    <div class="desc">Built-in preview. The editor every developer already has open.</div>
  </div>
  <div class="platform-card">
    <div class="icon">🌐</div>
    <div class="name">Static Sites</div>
    <div class="desc">Jekyll, Hugo, Astro — they all turn <code>.md</code> files into webpages.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Headers, Bold, and Italic

The three things you'll type in every single document.

<div class="syntax-compare">
  <div class="syn-col raw">
    <div class="syn-label">You type</div>
    <div class="syn-body">
      <span class="c-punct">#</span> <span class="c-text">Big Heading</span><br>
      <span class="c-punct">##</span> <span class="c-text">Smaller Heading</span><br>
      <span class="c-punct">###</span> <span class="c-text">Even Smaller</span><br>
      <br>
      <span class="c-punct">**</span><span class="c-bold">this is bold</span><span class="c-punct">**</span><br>
      <span class="c-punct">*</span><span class="c-em">this is italic</span><span class="c-punct">*</span><br>
      <span class="c-punct">**</span><span class="c-bold">bold </span><span class="c-punct">*</span><span class="c-em">and italic</span><span class="c-punct">*</span><span class="c-punct">**</span>
    </div>
  </div>
  <div class="syn-col out">
    <div class="syn-label">You get</div>
    <div class="syn-body">
      <span style="font-size:20px; font-weight:700; color:#111827;">Big Heading</span><br>
      <span style="font-size:17px; font-weight:600; color:#111827;">Smaller Heading</span><br>
      <span style="font-size:14px; font-weight:600; color:#111827;">Even Smaller</span><br>
      <br>
      <span style="font-weight:700; color:#111827;">this is bold</span><br>
      <span style="font-style:italic; color:#111827;">this is italic</span><br>
      <span style="font-weight:700; color:#111827;">bold <em>and italic</em></span>
    </div>
  </div>
</div>

<div class="highlight">

**Rule of thumb:** `#` = biggest. The more `#` symbols, the smaller the heading. Stop at `###` for most documents.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Lists and Checkboxes

Unordered lists, numbered lists, and task lists — all from plain characters.

<div class="list-grid">
  <div class="list-card">
    <div class="lc-label">Unordered List</div>
    <div class="lc-body">
      <span class="dim">- </span>Apples<br>
      <span class="dim">- </span>Oranges<br>
      <span class="dim">- </span>Mangoes<br>
      <br>
      <span class="dim"># Use - or * or +</span>
    </div>
  </div>
  <div class="list-card">
    <div class="lc-label">Ordered List</div>
    <div class="lc-body">
      <span class="dim">1. </span>Install Node<br>
      <span class="dim">2. </span>Clone the repo<br>
      <span class="dim">3. </span>Run npm install<br>
      <br>
      <span class="dim"># Numbers auto-increment</span>
    </div>
  </div>
  <div class="list-card">
    <div class="lc-label">Task / Checkbox List</div>
    <div class="lc-body">
      <span class="dim">- [x] </span>Write the draft<br>
      <span class="dim">- [x] </span>Add screenshots<br>
      <span class="dim">- [ ] </span>Publish post<br>
      <br>
      <span class="dim"># [x] = done  [ ] = todo</span>
    </div>
  </div>
  <div class="list-card">
    <div class="lc-label">Nested List</div>
    <div class="lc-body">
      <span class="dim">- </span>Frontend<br>
      <span class="dim">&nbsp;&nbsp;- </span>HTML<br>
      <span class="dim">&nbsp;&nbsp;- </span>CSS<br>
      <span class="dim">- </span>Backend<br>
      <br>
      <span class="dim"># Indent with 2 spaces</span>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Code Blocks

The most important syntax for developers. Inline code and full fenced blocks.

**Inline:** Wrap with backticks `` ` `` — use for commands, filenames, variable names.
Write `` `npm install` `` → renders as `npm install`

&nbsp;

**Fenced block:** Three backticks, then the language name for syntax highlighting.

<div class="dark-block">
  <div class="bar">
    <span class="dot r"></span>
    <span class="dot y"></span>
    <span class="dot g"></span>
    <span class="lang">python</span>
  </div>
  <div class="body">
    <span class="cmt"># You write this above your block:</span><br>
    <span class="def">```python</span><br>
    <span class="kw">def </span><span class="fn">greet</span><span class="def">(name):</span><br>
    <span class="def">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="kw">return </span><span class="str">f"Hello, {name}!"</span><br>
    <span class="def">```</span><br>
    <br>
    <span class="cmt"># Works for: python, javascript, bash, html, css, json...</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Links and Images

Both use nearly the same syntax — images just add a `!` at the front.

<div class="two-col">
  <div class="col-card">
    <div class="label">🔗 Link</div>
    <div style="font-family:'DM Mono',monospace; font-size:13px; color:#7c3aed; margin-top:10px; line-height:2;">
      [Link text](https://url.com)<br>
      <span style="color:#6b7280;">[Visit GitHub](https://github.com)</span>
    </div>
    <p style="font-size:13px; color:#6b7280; margin-top:8px;">Square brackets = the label you see. Round brackets = where it goes.</p>
  </div>
  <div class="col-card">
    <div class="label">🖼️ Image</div>
    <div style="font-family:'DM Mono',monospace; font-size:13px; color:#7c3aed; margin-top:10px; line-height:2;">
      ![Alt text](image.png)<br>
      <span style="color:#6b7280;">![Logo](./assets/logo.png)</span>
    </div>
    <p style="font-size:13px; color:#6b7280; margin-top:8px;">The <code>!</code> tells Markdown to show the image, not just link to it.</p>
  </div>
</div>

<div class="highlight">

**Memory trick:** Think of it as a label in `[ ]` and a destination in `( )`. Images are links that display instead of navigate.

</div>

---

## Tables

Tables look intimidating to type — but the pattern is always the same.

> `| Column 1 | Column 2 |`
> `| -------- | -------- |`
> `| Cell A   | Cell B   |`

The second row of dashes `---` is what tells Markdown "this is a table header."

<table class="md-table">
  <tr>
    <th>Syntax</th>
    <th>What it does</th>
    <th>Rendered result</th>
  </tr>
  <tr>
    <td class="mono">| Name | Age |</td>
    <td>Defines columns</td>
    <td>Table header row</td>
  </tr>
  <tr>
    <td class="mono">| --- | --- |</td>
    <td>Marks the header</td>
    <td>Separator (invisible)</td>
  </tr>
  <tr>
    <td class="mono">| Julius | 27 |</td>
    <td>Data row</td>
    <td>Table body row</td>
  </tr>
  <tr>
    <td class="mono">:---</td>
    <td>Left align column</td>
    <td>Text hugs the left</td>
  </tr>
  <tr>
    <td class="mono">---:</td>
    <td>Right align column</td>
    <td>Text hugs the right</td>
  </tr>
</table>

**Tip:** VS Code extensions like *Markdown Table Formatter* auto-align the pipes for you.

---

<!-- _class: step -->

<div class="step-badge">PRACTICE</div>

## Write Your First README

Every project on GitHub starts with a `README.md`. Here's the template — copy it, fill it in.

<div class="readme-box">
  <span class="r-h1"># Project Name</span><br>
  <span class="r-text">A short description of what this project does.</span><br>
  <br>
  <span class="r-h2">## Getting Started</span><br>
  <span class="r-text">Clone the repo and install dependencies:</span><br>
  <span class="r-dim">```bash</span><br>
  <span class="r-code">git clone https://github.com/you/project.git</span><br>
  <span class="r-code">cd project && npm install</span><br>
  <span class="r-dim">```</span><br>
  <br>
  <span class="r-h2">## Features</span><br>
  <span class="r-text">- [x] </span><span class="r-bold">Core feature</span><span class="r-text"> — does the main thing</span><br>
  <span class="r-text">- [ ] Dark mode </span><span class="r-dim">(coming soon)</span><br>
  <br>
  <span class="r-text">Made by </span><span class="r-link">[Your Name](https://yoursite.com)</span>
</div>

---

<!-- _class: final -->

# Plain text.
# Infinite reach.

&nbsp;

You now know everything you need to write clean, professional Markdown — anywhere.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*