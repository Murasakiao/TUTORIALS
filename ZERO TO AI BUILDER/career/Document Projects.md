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

  .cb-kw    { color: #c084fc; }
  .cb-fn    { color: #60a5fa; }
  .cb-str   { color: #fde68a; }
  .cb-num   { color: #fb923c; }
  .cb-cmt   { color: #4b5563; font-style: italic; }
  .cb-cmt-g { color: #34d399; font-style: italic; }
  .cb-var   { color: #f9fafb; }
  .cb-prop  { color: #34d399; }
  .cb-op    { color: #6b7280; }
  .cb-h1    { color: #60a5fa; font-weight: 600; }
  .cb-h2    { color: #93c5fd; }
  .cb-h3    { color: #bfdbfe; }
  .cb-bold  { color: #f9fafb; font-weight: 600; }
  .cb-muted { color: #4b5563; }
  .cb-good  { color: #34d399; }
  .cb-bad   { color: #f87171; }

  /* ── Why skipped — reason cards ── */
  .reason-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .reason-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 13px 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }

  .reason-card .rc-icon { font-size: 22px; flex-shrink: 0; }

  .reason-card .rc-title {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
    margin-bottom: 3px;
  }

  .reason-card .rc-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.5;
  }

  /* ── Five things checklist ── */
  .five-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 14px;
  }

  .five-item {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }

  .five-item .fi-num {
    background: var(--blue);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 600;
    min-width: 26px;
    height: 26px;
    border-radius: 999px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-top: 1px;
  }

  .five-item .fi-title {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
    margin-bottom: 3px;
  }

  .five-item .fi-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.5;
  }

  .five-item .fi-example {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--blue);
    margin-top: 4px;
  }

  /* ── README section viewer ── */
  .readme-viewer {
    background: #111827;
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 12.5px;
  }

  .readme-viewer .rv-bar {
    background: #1f2937;
    padding: 8px 16px;
    font-size: 11.5px;
    color: #6b7280;
    letter-spacing: 0.04em;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .readme-viewer .rv-bar .rv-badge {
    font-size: 10px;
    padding: 2px 8px;
    border-radius: 4px;
    background: #1e3a5f;
    color: #60a5fa;
    border: 1px solid #2563eb;
  }

  .readme-viewer .rv-body {
    padding: 14px 18px;
    line-height: 2.1;
  }

  .rv-h1    { color: #60a5fa; font-size: 17px; font-weight: 700; }
  .rv-h2    { color: #93c5fd; font-size: 14px; font-weight: 600; }
  .rv-h3    { color: #bfdbfe; font-size: 13px; font-weight: 600; }
  .rv-text  { color: #d1d5db; font-size: 12.5px; }
  .rv-code  { color: #34d399; background: #0f172a; padding: 1px 6px; border-radius: 3px; font-size: 12px; }
  .rv-badge-g { background: #166534; color: #86efac; padding: 1px 6px; border-radius: 3px; font-size: 11px; }
  .rv-badge-b { background: #1e3a5f; color: #93c5fd; padding: 1px 6px; border-radius: 3px; font-size: 11px; }
  .rv-link  { color: #60a5fa; }
  .rv-dim   { color: #374151; }

  /* ── Comment good/bad compare ── */
  .comment-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 14px;
  }

  .cc-col {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .cc-col .ccl-label {
    padding: 8px 14px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    border-bottom: 1px solid var(--border);
  }

  .cc-col.bad  .ccl-label { background: #fef2f2; color: #991b1b; border-color: #fecaca; }
  .cc-col.good .ccl-label { background: #f0fdf4; color: #166534; border-color: #bbf7d0; }
  .cc-col.bad             { border-color: #fecaca; }
  .cc-col.good            { border-color: #bbf7d0; }

  .cc-col .ccl-body {
    background: #111827;
    padding: 12px 16px;
    font-family: 'DM Mono', monospace;
    font-size: 12.5px;
    line-height: 2;
  }

  /* ── Changelog viewer ── */
  .changelog-block {
    background: #111827;
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 12.5px;
  }

  .changelog-block .clb-bar {
    background: #1f2937;
    padding: 8px 16px;
    font-size: 11.5px;
    color: #6b7280;
    letter-spacing: 0.04em;
  }

  .changelog-block .clb-body {
    padding: 14px 18px;
    line-height: 2.1;
  }

  .cl-version { color: #60a5fa; font-weight: 600; font-size: 13.5px; }
  .cl-date    { color: #4b5563; font-size: 11px; margin-left: 8px; }
  .cl-added   { color: #34d399; }
  .cl-fixed   { color: #fde68a; }
  .cl-changed { color: #93c5fd; }
  .cl-removed { color: #f87171; }
  .cl-text    { color: #d1d5db; }
  .cl-sect    { color: #6b7280; font-size: 11px; text-transform: uppercase; letter-spacing: 0.06em; }

  /* ── Tool item cards ── */
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

# Document Your Projects
## So Others Actually Understand Them

&nbsp;

**Code without documentation is a mystery. Add 20 minutes. Save everyone hours.**

`README` · `comments` · `changelog` · `setup` · `examples`

---

## Why Documentation Gets Skipped

It's not laziness. These are the four real reasons — and why they're all false economies.

<div class="reason-grid">
  <div class="reason-card">
    <div class="rc-icon">⏰</div>
    <div>
      <div class="rc-title">"I'll do it later"</div>
      <div class="rc-desc">Later never comes. Three months from now you'll open the project and spend 45 minutes figuring out how to run it — the thing you already knew.</div>
    </div>
  </div>
  <div class="reason-card">
    <div class="rc-icon">🧠</div>
    <div>
      <div class="rc-title">"It's obvious how it works"</div>
      <div class="rc-desc">It's obvious right now, to you, while it's fresh. Return in six weeks and it will feel like someone else's code. It always does.</div>
    </div>
  </div>
  <div class="reason-card">
    <div class="rc-icon">👤</div>
    <div>
      <div class="rc-title">"Nobody else will use this"</div>
      <div class="rc-desc">Future you is someone else. Every undocumented project eventually gets handed to you-from-the-future who has no idea what past-you was thinking.</div>
    </div>
  </div>
  <div class="reason-card">
    <div class="rc-icon">📄</div>
    <div>
      <div class="rc-title">"The code documents itself"</div>
      <div class="rc-desc">Clean code shows what it does. Documentation explains why it does it. Both are necessary. Self-documenting code is a myth for everything non-trivial.</div>
    </div>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**The real cost of skipping it:** every future collaborator, employer, or version of yourself spends time re-discovering what you already knew. Documentation is selfishness prevention.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## The 5 Things Every Project Needs Documented

If your project has these five, anyone can pick it up — including future you.

<div class="five-grid">
  <div class="five-item">
    <div class="fi-num">1</div>
    <div>
      <div class="fi-title">What it does</div>
      <div class="fi-desc">One or two sentences. Not what technology it uses — what problem it solves and for whom.</div>
      <div class="fi-example">"Fetches weather data for any city and emails a daily summary at 8 AM."</div>
    </div>
  </div>
  <div class="five-item">
    <div class="fi-num">2</div>
    <div>
      <div class="fi-title">How to install and run it</div>
      <div class="fi-desc">The exact commands from a fresh machine. Include the Python version, required packages, and any environment variables needed.</div>
      <div class="fi-example">pip install -r requirements.txt · python main.py</div>
    </div>
  </div>
  <div class="five-item">
    <div class="fi-num">3</div>
    <div>
      <div class="fi-title">Configuration and environment</div>
      <div class="fi-desc">What does .env need to contain? What API keys are required? Where do you get them? Never make someone guess.</div>
      <div class="fi-example">OPENAI_API_KEY=your_key · GMAIL_APP_PW=xxxx</div>
    </div>
  </div>
  <div class="five-item">
    <div class="fi-num">4</div>
    <div>
      <div class="fi-title">At least one working example</div>
      <div class="fi-desc">A sample input, the command to run it, and what the output should look like. Removes all ambiguity about whether it's working correctly.</div>
      <div class="fi-example">python run.py --city Manila · → 28°C, clear sky</div>
    </div>
  </div>
  <div class="five-item" style="grid-column: span 2;">
    <div class="fi-num">5</div>
    <div>
      <div class="fi-title">Known issues and limitations</div>
      <div class="fi-desc">What doesn't work yet? What are the edge cases? What's intentionally out of scope? This prevents people from filing bug reports for features you know about — and signals that you thought carefully about the scope.</div>
      <div class="fi-example">"Does not support cities outside the Open-Meteo coverage area. Rate limited to 60 requests/minute."</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## README Structure — The Standard That Works

A README that follows this structure takes 20–30 minutes to write and saves hours of "how do I run this?" questions.

<div class="readme-viewer">
  <div class="rv-bar">
    <span>README.md — the structure every project needs</span>
    <span class="rv-badge">MARKDOWN</span>
  </div>
  <div class="rv-body">
    <span class="rv-h1"># Project Name</span>&nbsp; <span class="rv-badge-g">Python</span> <span class="rv-badge-b">MIT</span><br>
    <span class="rv-text">One sentence: what it does and who it's for.</span><br>
    <br>
    <span class="rv-h2">## What it does</span><br>
    <span class="rv-text">2–3 sentences. Problem → solution. No jargon.</span><br>
    <br>
    <span class="rv-h2">## Quick start</span><br>
    <span class="rv-code">git clone ... &amp;&amp; pip install -r requirements.txt</span><br>
    <span class="rv-code">cp .env.example .env  # fill in your keys</span><br>
    <span class="rv-code">python main.py</span><br>
    <br>
    <span class="rv-h2">## Configuration</span><br>
    <span class="rv-text">Table of env vars: name · required · description · where to get it.</span><br>
    <br>
    <span class="rv-h2">## Usage examples</span><br>
    <span class="rv-text">Real input → real output. At least one. Screenshots welcome.</span><br>
    <br>
    <span class="rv-h2">## Known issues</span><br>
    <span class="rv-text">Honest list of gaps. Links to open issues if on GitHub.</span><br>
    <br>
    <span class="rv-h2">## License</span><br>
    <span class="rv-link">MIT</span> <span class="rv-dim">· © 2026 Your Name</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01 — continued</div>

## README — Part 2 of 2

Two sections that get skipped most often but matter most.

<div class="two-col">
  <div class="col-card">
    <div class="label">Configuration table — do this, not prose</div>
    <div class="code-block" style="margin-top:10px;">
      <div class="cb-body" style="padding:10px 14px; line-height:1.9; font-size:12px;">
        <span class="cb-bold">| Variable &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Required | Description &nbsp;&nbsp;&nbsp;&nbsp;|</span><br>
        <span class="cb-muted">|----------------|----------|----------------|</span><br>
        <span class="cb-prop">OPENAI_API_KEY</span>  <span class="cb-muted">| Yes &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</span> <span class="cb-str">platform.openai</span> <span class="cb-muted">|</span><br>
        <span class="cb-prop">GMAIL_SENDER</span>  &nbsp;&nbsp;<span class="cb-muted">| Yes &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</span> <span class="cb-str">your Gmail addr</span> <span class="cb-muted">|</span><br>
        <span class="cb-prop">REPORT_TIME</span>  &nbsp;&nbsp;&nbsp;<span class="cb-muted">| No &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</span> <span class="cb-str">default: "09:00"</span><span class="cb-muted">|</span>
      </div>
    </div>
    <p style="font-size:13px; color:var(--muted); margin-top:6px;">A table is scannable. Prose descriptions of env vars are not. Always include where to get each key.</p>
  </div>
  <div class="col-card">
    <div class="label">Usage example — show actual output</div>
    <div class="code-block" style="margin-top:10px;">
      <div class="cb-body" style="padding:10px 14px; line-height:1.9; font-size:12px;">
        <span class="cb-muted">$ python main.py --city Manila</span><br>
        <br>
        <span class="cb-good">✓ Fetched weather data</span><br>
        <span class="cb-good">✓ Summary generated</span><br>
        <span class="cb-good">✓ Email sent → you@gmail.com</span><br>
        <br>
        <span class="cb-muted">Manila: 31°C, partly cloudy</span><br>
        <span class="cb-muted">Humidity: 85% · UV: 9 (Very High)</span>
      </div>
    </div>
    <p style="font-size:13px; color:var(--muted); margin-top:6px;">Anyone reading can verify it works. Show what success looks like — not just the command.</p>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**The .env.example rule:** Always commit a <code>.env.example</code> file with all keys listed but values blanked. Never commit the real <code>.env</code>. Add <code>.env</code> to <code>.gitignore</code> immediately.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Inline Comments Done Right

Comments explain **why** — not what. The code already shows what it does. The comment should explain why it was written that way.

<div class="comment-compare">
  <div class="cc-col bad">
    <div class="ccl-label">❌ &nbsp;Comments that explain the obvious</div>
    <div class="ccl-body">
      <span class="cb-cmt"># increment i by 1</span><br>
      <span class="cb-var">i</span> <span class="cb-op">+=</span> <span class="cb-num">1</span><br>
      <br>
      <span class="cb-cmt"># check if user exists</span><br>
      <span class="cb-kw">if</span> <span class="cb-var">user</span> <span class="cb-kw">in</span> <span class="cb-var">db</span><span class="cb-op">:</span><br>
      <br>
      <span class="cb-cmt"># loop through items</span><br>
      <span class="cb-kw">for</span> <span class="cb-var">item</span> <span class="cb-kw">in</span> <span class="cb-var">items</span><span class="cb-op">:</span><br>
      <br>
      <span class="cb-cmt"># convert to string</span><br>
      <span class="cb-var">result</span> <span class="cb-op">=</span> <span class="cb-fn">str</span><span class="cb-op">(</span><span class="cb-var">value</span><span class="cb-op">)</span>
    </div>
  </div>
  <div class="cc-col good">
    <div class="ccl-label">✅ &nbsp;Comments that explain why</div>
    <div class="ccl-body">
      <span class="cb-cmt-g"># API rate-limits at 60/min — sleep prevents 429</span><br>
      <span class="cb-var">time</span><span class="cb-op">.</span><span class="cb-fn">sleep</span><span class="cb-op">(</span><span class="cb-num">1</span><span class="cb-op">)</span><br>
      <br>
      <span class="cb-cmt-g"># Retry on 503 — server is flaky on first req</span><br>
      <span class="cb-kw">for</span> <span class="cb-var">attempt</span> <span class="cb-kw">in</span> <span class="cb-fn">range</span><span class="cb-op">(</span><span class="cb-num">3</span><span class="cb-op">):</span><br>
      <br>
      <span class="cb-cmt-g"># Use repr() not str() — preserves None vs "None"</span><br>
      <span class="cb-var">result</span> <span class="cb-op">=</span> <span class="cb-fn">repr</span><span class="cb-op">(</span><span class="cb-var">value</span><span class="cb-op">)</span><br>
      <br>
      <span class="cb-cmt-g"># TODO: replace with proper validation (issue #42)</span><br>
      <span class="cb-kw">if</span> <span class="cb-var">len</span><span class="cb-op">(</span><span class="cb-var">data</span><span class="cb-op">) ></span> <span class="cb-num">0</span><span class="cb-op">:</span>
    </div>
  </div>
</div>

<div class="two-col" style="margin-top:14px;">
  <div class="col-card">
    <div class="label">Comment these things</div>
    <ul style="margin-top:6px; padding-left:1.2em;">
      <li style="font-size:13px;">Non-obvious decisions and trade-offs</li>
      <li style="font-size:13px;">Workarounds for external bugs or quirks</li>
      <li style="font-size:13px;">Business rules that aren't in the code</li>
      <li style="font-size:13px;">TODO / FIXME with issue numbers</li>
    </ul>
  </div>
  <div class="col-card">
    <div class="label">Skip comments for these</div>
    <ul style="margin-top:6px; padding-left:1.2em;">
      <li style="font-size:13px;">Anything a good function name already says</li>
      <li style="font-size:13px;">Restating what the code clearly does</li>
      <li style="font-size:13px;">Commented-out dead code — delete it</li>
      <li style="font-size:13px;">Placeholders with no actionable plan</li>
    </ul>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## A Changelog Habit — One Minute Per Commit

A changelog is a human-readable record of what changed and why — written for people, not machines. The format that became the standard: **Keep a Changelog** (keepachangelog.com).

<div class="changelog-block">
  <div class="clb-bar">CHANGELOG.md — one file, updated with every release</div>
  <div class="clb-body">
    <span class="cl-version">[1.2.0]</span><span class="cl-date">— 2026-04-18</span><br>
    <span class="cl-sect">Added</span><br>
    <span class="cl-added">+ </span><span class="cl-text">Support for hourly weather updates (previously daily only)</span><br>
    <span class="cl-added">+ </span><span class="cl-text">--dry-run flag to preview email without sending</span><br>
    <span class="cl-sect">Fixed</span><br>
    <span class="cl-fixed">~ </span><span class="cl-text">Crash when city name contains non-ASCII characters (#31)</span><br>
    <span class="cl-sect">Changed</span><br>
    <span class="cl-changed">→ </span><span class="cl-text">REPORT_TIME env var now uses 24h format (was 12h AM/PM)</span><br>
    <br>
    <span class="cl-version">[1.1.0]</span><span class="cl-date">— 2026-04-01</span><br>
    <span class="cl-sect">Added</span><br>
    <span class="cl-added">+ </span><span class="cl-text">Slack notification as alternative to email output</span><br>
    <span class="cl-sect">Removed</span><br>
    <span class="cl-removed">- </span><span class="cl-text">WeatherAPI.com support — replaced by Open-Meteo (free, no key)</span>
  </div>
</div>

<div class="highlight" style="margin-top:10px;">

**The habit:** Every time you tag a release or push a meaningful change, add one entry. Use the four categories — <strong>Added, Fixed, Changed, Removed</strong> — and keep each line under two sentences. It takes 60 seconds and compounds enormously over a project's life.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Tools — Where to Put Your Docs

<div class="tool-row">
  <div class="tool-item">
    <div class="t-icon">📄</div>
    <div>
      <div class="t-name">README.md in the repo</div>
      <div class="t-url">your-repo/README.md</div>
      <div class="t-desc">The default landing page for any GitHub or GitLab repo. Always start here. Markdown renders automatically. Zero setup, always co-located with the code.</div>
    </div>
  </div>
  <div class="tool-item">
    <div class="t-icon">📚</div>
    <div>
      <div class="t-name">GitHub Wiki</div>
      <div class="t-url">github.com/user/repo/wiki</div>
      <div class="t-desc">Built into every GitHub repo. Good for multi-page documentation — architecture decisions, API references, deployment guides. Free and searchable.</div>
    </div>
  </div>
  <div class="tool-item">
    <div class="t-icon">📝</div>
    <div>
      <div class="t-name">Notion</div>
      <div class="t-url">notion.so</div>
      <div class="t-desc">Great for team projects needing rich docs — diagrams, tables, embedded videos, linked databases. Free personal plan. Shareable via link without login.</div>
    </div>
  </div>
  <div class="tool-item">
    <div class="t-icon">📖</div>
    <div>
      <div class="t-name">MkDocs / Docusaurus</div>
      <div class="t-url">mkdocs.org · docusaurus.io</div>
      <div class="t-desc">Turn a folder of Markdown files into a full documentation site. Free to host on GitHub Pages. Best for open-source projects or APIs with many users.</div>
    </div>
  </div>
</div>

<div class="two-col" style="margin-top:14px;">
  <div class="col-card">
    <div class="label">For solo projects</div>
    <p style="font-size:13.5px; margin-top:6px;">README.md + CHANGELOG.md in the repo. Two files, always current, zero maintenance overhead.</p>
  </div>
  <div class="col-card">
    <div class="label">For team or open-source projects</div>
    <p style="font-size:13.5px; margin-top:6px;">README.md + GitHub Wiki or Notion for extended docs + CHANGELOG.md for release history. Add a CONTRIBUTING.md if you want pull requests.</p>
  </div>
</div>

---

## Documentation Quick Reference

<table class="cheat-table">
  <tr>
    <th>What to document</th>
    <th>Where it lives</th>
    <th>When to write it</th>
  </tr>
  <tr>
    <td>What the project does</td>
    <td class="mono">README.md — top</td>
    <td>Before you write a single line of code</td>
  </tr>
  <tr>
    <td>How to install and run</td>
    <td class="mono">README.md — Quick start</td>
    <td>The moment it first runs on your machine</td>
  </tr>
  <tr>
    <td>Environment variables</td>
    <td class="mono">.env.example + README table</td>
    <td>Every time you add a new variable</td>
  </tr>
  <tr>
    <td>Usage examples</td>
    <td class="mono">README.md — Usage</td>
    <td>As soon as you have a working example to show</td>
  </tr>
  <tr>
    <td>Why a decision was made</td>
    <td>Inline comment above the code</td>
    <td>At the same time you write the tricky code</td>
  </tr>
  <tr>
    <td>What changed between versions</td>
    <td class="mono">CHANGELOG.md</td>
    <td>Every time you tag a release</td>
  </tr>
  <tr>
    <td>Architecture and diagrams</td>
    <td>GitHub Wiki or Notion</td>
    <td>When the project grows past one file</td>
  </tr>
  <tr>
    <td>Known issues</td>
    <td class="mono">README.md — Known issues</td>
    <td>Every time you discover one you're not fixing yet</td>
  </tr>
  <tr>
    <td>How to contribute</td>
    <td class="mono">CONTRIBUTING.md</td>
    <td>Before you share the repo publicly</td>
  </tr>
</table>

---

<!-- _class: final -->

# Write it now.
# Thank yourself later.

&nbsp;

README. Comments that explain why. A changelog entry. That's all of documentation.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*