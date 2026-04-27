---
marp: true
paginate: true
html: true
size: 4:3
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,400;0,500;0,600;1,400&family=DM+Mono:wght@400;500&display=swap');

  :root {
    --amber:       #f59e0b;
    --amber-dim:   #d97706;
    --green:       #22c55e;
    --green-dim:   #16a34a;
    --purple:      #c4b5fd;
    --white:       #f1f5f9;
    --off-white:   #cbd5e1;
    --subtle:      #94a3b8;
    --muted:       #64748b;
    --faint:       #334155;
    --bg:          #080808;
    --card-bg:     #111111;
    --card-border: #222222;
    --code-bg:     #0a0a0a;
  }

  section {
    font-family: 'DM Sans', sans-serif;
    background: var(--bg);
    color: var(--white);
    padding: 44px 52px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    position: relative;
  }

  /* ── TAG ── */
  .tag {
    display: flex;
    align-items: center;
    gap: 12px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 3px;
    color: var(--amber);
    text-transform: uppercase;
    margin-bottom: 22px;
  }
  .tag::before {
    content: '';
    display: block;
    width: 24px;
    height: 2px;
    background: var(--amber);
    flex-shrink: 0;
  }
  .tag.green  { color: var(--green); }
  .tag.green::before  { background: var(--green); }
  .tag.purple { color: var(--purple); }
  .tag.purple::before { background: var(--purple); }

  /* ── HEADINGS ── */
  h1 {
    font-size: 38px;
    font-weight: 700;
    line-height: 1.08;
    margin: 0 0 14px 0;
    color: var(--white);
    letter-spacing: -1.5px;
  }
  h2 {
    font-size: 30px;
    font-weight: 700;
    line-height: 1.1;
    margin: 0 0 12px 0;
    color: var(--white);
    letter-spacing: -1px;
    border: none;
  }
  p {
    font-size: 17px;
    line-height: 1.6;
    color: var(--subtle);
    margin: 0 0 16px 0;
  }
  strong { color: var(--white); font-weight: 600; }
  code {
    font-family: 'DM Mono', monospace;
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    color: var(--amber);
    padding: 1px 6px;
    border-radius: 4px;
    font-size: 0.88em;
  }

  .accent-green  { color: var(--green); }
  .accent-amber  { color: var(--amber); }
  .accent-purple { color: var(--purple); }
  /* strikethrough: visible but clearly "crossed out" */
  .strike { color: var(--faint); text-decoration: line-through; }

  /* ── HEADER ROW ── */
  .header-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }
  .page-num {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--amber-dim);
    letter-spacing: 2px;
    text-transform: uppercase;
  }
  /* was #2d2d2d — now readable */
  .page-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--muted);
  }

  /* ── CODE BLOCK ── */
  .code-block {
    background: var(--code-bg);
    border: 1px solid var(--card-border);
    border-radius: 10px;
    overflow: hidden;
    margin: 0 0 16px;
    font-family: 'DM Mono', monospace;
  }
  .cb-bar {
    background: #0f0f0f;
    border-bottom: 1px solid var(--card-border);
    padding: 8px 14px;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .cb-dot { width: 9px; height: 9px; border-radius: 50%; display: inline-block; }
  .cb-dot.r { background: #ef4444; }
  .cb-dot.y { background: #eab308; }
  .cb-dot.g { background: var(--green); }
  /* was #2d2d2d — now readable */
  .cb-title  { font-size: 11px; color: var(--muted); margin-left: 6px; letter-spacing: 0.04em; }
  .cb-status { margin-left: auto; font-size: 11px; color: var(--green); }
  .cb-body {
    padding: 16px 20px;
    font-size: 14px;
    line-height: 1.85;
    color: var(--off-white);
    white-space: pre;
  }
  .cb-body .cmd   { color: var(--green); }
  /* was #374151 — now readable */
  .cb-body .key   { color: var(--muted); }
  .cb-body .val   { color: var(--amber); }
  .cb-body .check { color: var(--green); }
  .cb-body .arr   { color: var(--purple); }
  .cb-body .str   { color: #86efac; }
  /* comments: subtle but still visible */
  .cb-body .cm    { color: var(--faint); }

  /* ── CARDS 2-col ── */
  .cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 14px;
  }
  .card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 10px;
    padding: 16px 15px;
  }
  .card-icon { font-size: 18px; margin-bottom: 8px; display: block; }
  .card h3 {
    font-size: 15px;
    font-weight: 600;
    color: var(--white);
    margin: 0 0 5px;
    letter-spacing: -0.2px;
  }
  /* was #374151 — now readable */
  .card p {
    font-size: 13.5px;
    color: var(--subtle);
    line-height: 1.45;
    margin: 0 0 10px;
  }

  /* ── CARDS 1-col (stacked) ── */
  .cards-col { display: flex; flex-direction: column; gap: 10px; margin-bottom: 14px; }
  .card-row {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 10px;
    padding: 14px 18px;
    display: flex;
    align-items: flex-start;
    gap: 14px;
  }
  .card-row-icon { font-size: 18px; flex-shrink: 0; margin-top: 1px; }
  .card-row-body h3 {
    font-size: 15px;
    font-weight: 600;
    color: var(--white);
    margin: 0 0 3px;
  }
  /* was #374151 — now readable */
  .card-row-body p {
    font-size: 13.5px;
    color: var(--subtle);
    margin: 0;
    line-height: 1.5;
  }

  /* ── BEFORE / AFTER ── */
  .compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 14px;
  }
  .compare-col {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 10px;
    padding: 14px 16px;
  }
  .compare-col.now-col { border-color: #14532d; }
  .compare-label {
    font-family: 'DM Mono', monospace;
    font-size: 9px;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 8px;
  }
  /* was #374151 — now readable */
  .compare-label.before { color: var(--muted); }
  .compare-label.now    { color: var(--green); }
  .compare-col h3 {
    font-size: 15px;
    font-weight: 600;
    color: var(--white);
    margin: 0 0 8px;
  }
  /* was #374151 — now readable */
  .compare-col p {
    font-size: 13.5px;
    color: var(--subtle);
    line-height: 1.5;
    margin: 0 0 10px;
  }
  .compare-tags { display: flex; flex-wrap: wrap; gap: 5px; margin-top: 8px; }
  .ctag {
    font-family: 'DM Mono', monospace;
    font-size: 9px;
    padding: 2px 7px;
    border-radius: 4px;
    border: 1px solid var(--card-border);
    /* was #374151 — now readable */
    color: var(--muted);
  }
  .ctag.g { color: var(--green); border-color: #14532d; }

  /* ── PILL ── */
  .pill {
    display: inline-block;
    background: var(--code-bg);
    border: 1px solid var(--card-border);
    border-radius: 5px;
    padding: 3px 9px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--amber);
  }
  .pill.green  { color: var(--green); }
  .pill.purple { color: var(--purple); }

  /* ── LIST ITEMS ── */
  .list { display: flex; flex-direction: column; gap: 8px; margin-bottom: 14px; }
  .list-item {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 8px;
    padding: 12px 15px;
  }
  .list-num {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--amber);
    flex-shrink: 0;
    margin-top: 2px;
    min-width: 20px;
  }
  /* was #9ca3af — fine, but bumping up */
  .list-text { font-size: 14px; color: var(--subtle); line-height: 1.5; }
  .list-text strong { color: var(--white); }

  /* ── INSIGHT BOX ── */
  .insight {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 10px;
    padding: 16px 20px;
    margin-top: auto;
  }
  .insight-label {
    font-family: 'DM Mono', monospace;
    font-size: 9px;
    letter-spacing: 3px;
    /* was #2d2d2d — now readable */
    color: var(--muted);
    text-transform: uppercase;
    margin-bottom: 6px;
  }
  .insight p { font-size: 15px; color: var(--off-white); line-height: 1.5; margin: 0; }

  /* ── CTA SLIDE ── */
  section.cta {
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  section.cta h2 { text-align: center; }
  section.cta p  { text-align: center; max-width: 460px; }
  .cta-options { display: flex; flex-direction: column; gap: 10px; width: 100%; margin: 18px 0; }
  .cta-option {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 10px;
    padding: 14px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .cta-option-left { display: flex; align-items: center; gap: 12px; }
  .cta-option-left span { font-size: 18px; }
  .cta-option h3 { font-size: 15px; font-weight: 600; color: var(--white); margin: 0; }
  /* was #2d2d2d — now readable */
  .cta-option .cta-cmd {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--muted);
  }

  /* ── FOOTER (native paginate) ── */
  section::after {
    font-family: 'DM Mono', monospace;
    font-size: 9px;
    color: var(--muted);
    letter-spacing: 1px;
    content: '@juliusdarang · ' attr(data-marpit-pagination);
    position: absolute;
    bottom: 22px;
    right: 40px;
  }
---

<!-- ══════════════════════════════════════════════════ -->
<!-- SLIDE 1 · HOOK                                    -->
<!-- ══════════════════════════════════════════════════ -->

<div class="tag green">free & powerful</div>

## Run AI tasks on a schedule — <span class="accent-green">laptop off.</span>

GitHub Actions lets you automate Claude API calls on a cron schedule. **No paid tools. No always-on machine.** Just a YAML file and your existing repo.

<div class="code-block">
  <div class="cb-bar">
    <span class="cb-dot r"></span><span class="cb-dot y"></span><span class="cb-dot g"></span>
    <span class="cb-title">.github/workflows/nightly.yml</span>
    <span class="cb-status">● workflow active</span>
  </div>
  <div class="cb-body"><span class="key">on:</span>
  <span class="key">  schedule:</span>
    <span class="arr">-</span> <span class="key">cron:</span> <span class="str">'0 3 * * *'</span>  <span class="cm"># 3 AM daily</span>

<span class="key">jobs:</span>
  <span class="val">ai-task:</span>
    <span class="key">runs-on:</span> <span class="str">ubuntu-latest</span>
    <span class="key">steps:</span>
      <span class="arr">-</span> <span class="check">calls Claude API via HTTP</span>
      <span class="arr">-</span> <span class="check">laptop can be fully off</span></div>
</div>

---

<!-- ══════════════════════════════════════════════════ -->
<!-- SLIDE 2 · WHAT IS IT                              -->
<!-- ══════════════════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— what is it — github actions · claude api</span>
</div>

## GitHub Actions + Claude API = <span class="accent-green">free automation.</span>

You define a workflow YAML, set a cron trigger, and GitHub handles all execution in the cloud. Your codebase, your rules.

<div class="cards-col">
  <div class="card-row">
    <span class="card-row-icon">☁️</span>
    <div class="card-row-body">
      <h3>Runs in GitHub's cloud</h3>
      <p>No server, no VPS, no laptop. GitHub spins up a runner, executes your workflow, and shuts it down.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">💸</span>
    <div class="card-row-body">
      <h3>Free for public repos</h3>
      <p>Public repos get unlimited free minutes. Private repos get 2,000 free minutes/month on the free plan.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">🔗</span>
    <div class="card-row-body">
      <h3>Lives inside your codebase</h3>
      <p>Workflow files sit in <code>.github/workflows/</code>. Versioned, reviewable, no external dashboards.</p>
    </div>
  </div>
</div>

---

<!-- ══════════════════════════════════════════════════ -->
<!-- SLIDE 3 · THE WORKFLOW FILE                       -->
<!-- ══════════════════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 01 — the workflow file</span>
  <span class="page-label">nightly.yml</span>
</div>

## One YAML file, one <span class="accent-amber">scheduled task.</span>

Drop this in `.github/workflows/nightly.yml`. GitHub reads it, schedules it, and runs it — no further setup.

<div class="code-block">
  <div class="cb-bar">
    <span class="cb-dot r"></span><span class="cb-dot y"></span><span class="cb-dot g"></span>
    <span class="cb-title">.github/workflows/nightly.yml</span>
    <span class="cb-status" style="color:var(--amber);">● creating workflow</span>
  </div>
  <div class="cb-body"><span class="key">name:</span> <span class="str">Nightly Claude Task</span>
<span class="key">on:</span>
  <span class="key">schedule:</span>
    <span class="arr">-</span> <span class="key">cron:</span> <span class="str">'0 3 * * *'</span>
<span class="key">jobs:</span>
  <span class="val">run-claude:</span>
    <span class="key">runs-on:</span> <span class="str">ubuntu-latest</span>
    <span class="key">steps:</span>
      <span class="arr">-</span> <span class="key">name:</span> <span class="str">Call Claude API</span>
        <span class="key">env:</span>
          <span class="val">ANTHROPIC_API_KEY:</span> <span class="cm">${{ secrets.ANTHROPIC_API_KEY }}</span>
        <span class="key">run:</span> <span class="str">|
          curl https://api.anthropic.com/v1/messages             -H "x-api-key: $ANTHROPIC_API_KEY"             -d '{"model":"claude-sonnet-4-20250514"}'</span></div>
</div>

<div class="insight">
  <div class="insight-label">the moment it clicks</div>
  <p>Push the file. Close the laptop. GitHub runs it tonight at 3 AM. <strong>You do nothing.</strong></p>
</div>

---

<!-- ══════════════════════════════════════════════════ -->
<!-- SLIDE 4 · CRON SYNTAX                             -->
<!-- ══════════════════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 02 — scheduling</span>
  <span class="page-label">cron syntax</span>
</div>

## Cron syntax — <span class="accent-purple">five fields.</span>

<div class="cards">
  <div class="card">
    <span class="card-icon">🕒</span>
    <h3>Every night</h3>
    <p>Runs at 3:00 AM UTC, every day of the year.</p>
    <span class="pill green">0 3 * * *</span>
  </div>
  <div class="card">
    <span class="card-icon">📅</span>
    <h3>Every Monday</h3>
    <p>Weekly digest. Fires at 8 AM on Monday mornings.</p>
    <span class="pill purple">0 8 * * 1</span>
  </div>
  <div class="card">
    <span class="card-icon">⚡</span>
    <h3>Every 15 min</h3>
    <p>Near real-time polling. Minimum interval GitHub allows.</p>
    <span class="pill">*/15 * * * *</span>
  </div>
  <div class="card">
    <span class="card-icon">📆</span>
    <h3>1st of month</h3>
    <p>Monthly reports, billing summaries, or archive tasks.</p>
    <span class="pill">0 9 1 * *</span>
  </div>
</div>

<div class="insight">
  <div class="insight-label">tip</div>
  <p>GitHub cron runs in <strong>UTC</strong>. Adjust for your timezone — PHT is UTC+8, so <code>0 3 * * *</code> = 11 AM Manila time.</p>
</div>

---

<!-- ══════════════════════════════════════════════════ -->
<!-- SLIDE 5 · 4 TASKS WORTH AUTOMATING               -->
<!-- ══════════════════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 03 — what to automate</span>
  <span class="page-label">4 tasks worth gold</span>
</div>

<div class="cards">
  <div class="card">
    <span class="card-icon">🔍</span>
    <h3>Nightly code review</h3>
    <p>Claude scans new commits, flags issues, posts a summary to Slack.</p>
    <span class="pill green">cron · 0 3 * * *</span>
  </div>
  <div class="card">
    <span class="card-icon">📄</span>
    <h3>PR summarizer</h3>
    <p>On every PR open, Claude writes a plain-English summary as a comment.</p>
    <span class="pill purple">on: pull_request</span>
  </div>
  <div class="card">
    <span class="card-icon">📊</span>
    <h3>Weekly digest</h3>
    <p>Monday 8 AM: merged PRs, closed issues, top contributors → email.</p>
    <span class="pill">cron · 0 8 * * 1</span>
  </div>
  <div class="card">
    <span class="card-icon">🏷️</span>
    <h3>Issue labeler</h3>
    <p>New issue opened → Claude reads it and applies the right label automatically.</p>
    <span class="pill">on: issues.opened</span>
  </div>
</div>

<div class="insight">
  <div class="insight-label">rule of thumb</div>
  <p>If you do it <strong>every week by hand</strong> and it's boring → it's a workflow.</p>
</div>

---

<!-- ══════════════════════════════════════════════════ -->
<!-- SLIDE 6 · MANAGING SECRETS                        -->
<!-- ══════════════════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 04 — secrets</span>
  <span class="page-label">keep your API key safe</span>
</div>

## Never hardcode your <span class="accent-amber">API key.</span>

GitHub Secrets stores sensitive values encrypted. Your workflow reads them as environment variables — never exposed in logs or code.

<div class="code-block">
  <div class="cb-bar">
    <span class="cb-dot r"></span><span class="cb-dot y"></span><span class="cb-dot g"></span>
    <span class="cb-title">adding your secret</span>
  </div>
  <div class="cb-body"><span class="cm"># In GitHub: Settings → Secrets → Actions</span>
<span class="cm"># Add: ANTHROPIC_API_KEY = sk-ant-...</span>

<span class="cm"># Then reference it in your workflow:</span>
<span class="key">env:</span>
  <span class="val">ANTHROPIC_API_KEY:</span> <span class="str">${{ secrets.ANTHROPIC_API_KEY }}</span>

<span class="cm"># Never do this:</span>
<span class="key">env:</span>
  <span class="val">ANTHROPIC_API_KEY:</span> <span class="arr">sk-ant-abc123...</span>  <span class="cm">✗ exposed!</span></div>
</div>

<div class="list">
  <div class="list-item">
    <span class="list-num">01</span>
    <span class="list-text">Go to your repo → <strong>Settings → Secrets and variables → Actions</strong></span>
  </div>
  <div class="list-item">
    <span class="list-num">02</span>
    <span class="list-text">Click <strong>New repository secret</strong>, name it <code>ANTHROPIC_API_KEY</code></span>
  </div>
  <div class="list-item">
    <span class="list-num">03</span>
    <span class="list-text">Reference it in YAML as <code>${{ secrets.ANTHROPIC_API_KEY }}</code></span>
  </div>
</div>

---

<!-- ══════════════════════════════════════════════════ -->
<!-- SLIDE 7 · PROS & CONS                             -->
<!-- ══════════════════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 05 — tradeoffs</span>
  <span class="page-label">honest assessment</span>
</div>

## The good and the <span class="accent-amber">hard parts.</span>

GitHub Actions is powerful, but it comes with setup overhead. Know what you're signing up for.

<div class="compare">
  <div class="compare-col">
    <div class="compare-label before">PROS</div>
    <h3>Why it's great</h3>
    <p>Free for public repos. Lives in your codebase. No extra tools or dashboards to manage.</p>
    <div class="compare-tags">
      <span class="ctag g">free</span>
      <span class="ctag g">versioned</span>
      <span class="ctag g">no vendor lock-in</span>
    </div>
  </div>
  <div class="compare-col now-col">
    <div class="compare-label now">CONS</div>
    <h3>What's harder</h3>
    <p>You write YAML. You manage secrets. You handle errors and retries yourself. More setup than a GUI tool.</p>
    <div class="compare-tags">
      <span class="ctag">yaml required</span>
      <span class="ctag">manual error handling</span>
    </div>
  </div>
</div>

<div class="insight">
  <div class="insight-label">the verdict</div>
  <p>If you live in a repo and know basic YAML, this is the <strong>best free option</strong> for scheduled AI tasks.</p>
</div>

---

<!-- ══════════════════════════════════════════════════ -->
<!-- SLIDE 8 · ALTERNATIVES                            -->
<!-- ══════════════════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 06 — alternatives</span>
  <span class="page-label">other options</span>
</div>

## Not a dev? <span class="accent-amber">There are easier paths.</span>

<div class="cards">
  <div class="card">
    <span class="card-icon">🔀</span>
    <h3>n8n</h3>
    <p>Visual node editor. Self-host free or use their cloud. Great for non-YAML people.</p>
    <span class="pill green">open source</span>
  </div>
  <div class="card">
    <span class="card-icon">⚡</span>
    <h3>Zapier / Make</h3>
    <p>No-code. Fully managed. Easy to start, pricier at scale. Call Claude via HTTP.</p>
    <span class="pill purple">no-code</span>
  </div>
  <div class="card">
    <span class="card-icon">🖥️</span>
    <h3>Trigger.dev</h3>
    <p>Developer-focused. Write a JS function, set a cron, runs in their cloud.</p>
    <span class="pill">free tier</span>
  </div>
  <div class="card">
    <span class="card-icon">🤖</span>
    <h3>Claude Code Routines</h3>
    <p>Most integrated option. Requires Claude Pro+. No YAML, no setup at all.</p>
    <span class="pill">$20+ / mo</span>
  </div>
</div>

<div class="insight">
  <div class="insight-label">bottom line</div>
  <p>GitHub Actions = best <strong>free</strong> option. Claude Code Routines = easiest if you already pay for Pro.</p>
</div>

---

<!-- ══════════════════════════════════════════════════ -->
<!-- SLIDE 9 · CTA                                     -->
<!-- ══════════════════════════════════════════════════ -->

<section class="cta">

<div class="tag green" style="justify-content:center;margin-bottom:18px;">try it tonight</div>

## Which workflow would you <span class="accent-green">build first?</span>

<p>Create <code>.github/workflows/nightly.yml</code> in your repo and push it.</p>

<div class="cta-options">
  <div class="cta-option">
    <div class="cta-option-left">
      <span>🔍</span>
      <h3>NIGHTLY CODE REVIEW</h3>
    </div>
    <span class="cta-cmd">comment "REVIEW"</span>
  </div>
  <div class="cta-option">
    <div class="cta-option-left">
      <span>📄</span>
      <h3>PR SUMMARIZER</h3>
    </div>
    <span class="cta-cmd">comment "PR"</span>
  </div>
  <div class="cta-option">
    <div class="cta-option-left">
      <span>📊</span>
      <h3>WEEKLY DIGEST</h3>
    </div>
    <span class="cta-cmd">comment "DIGEST"</span>
  </div>
</div>

</section>