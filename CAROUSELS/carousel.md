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
    font-size: 13px;
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

<div class="tag green">just shipped</div>

## If you still use Claude Code as a <span class="strike">terminal</span>… you're <span class="accent-green">behind.</span>

Anthropic just dropped **Routines**: Claude Code that runs on its own. On cron, from GitHub, or by API. **Laptop closed.**

<div class="code-block">
  <div class="cb-bar">
    <span class="cb-dot r"></span><span class="cb-dot y"></span><span class="cb-dot g"></span>
    <span class="cb-title">~/focus-timer · claude-code</span>
    <span class="cb-status">● routine active</span>
  </div>
  <div class="cb-body"><span class="cmd">$</span> claude <span class="val">/schedule</span> <span class="str">"audit repo, open PRs"</span>
  <span class="key">cadence:</span> <span class="val">every night @ 03:00</span>
  <span class="key">trigger:</span> <span class="val">cron</span> · <span class="val">github</span> · <span class="val">api</span>

<span class="check">✓</span> saved <span class="str">"nightly-audit"</span>
<span class="arr">→</span> next run in <span class="val">4h 12m</span></div>
</div>


---

<!-- ══════════════════════════════════════════════════ -->
<!-- SLIDE 2 · WHAT IS IT                              -->
<!-- ══════════════════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— what is it — claude code · routines</span>
</div>

## Native cron jobs, <span class="accent-green">inside</span> Claude Code.

Configure **once**: prompt + repo + connectors. Claude runs it headless — no terminal, no laptop, no babysitting.

<div class="cards-col">
  <div class="card-row">
    <span class="card-row-icon">⏰</span>
    <div class="card-row-body">
      <h3>Cron — On a clock</h3>
      <p>Every night, every hour, every Monday. Set a schedule, forget it exists.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">🔗</span>
    <div class="card-row-body">
      <h3>Webhook — On events</h3>
      <p>PRs, issues, pushes — Claude reacts. GitHub fires it, you don't lift a finger.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">&lt;/&gt;</span>
    <div class="card-row-body">
      <h3>API — On demand</h3>
      <p>Fire it from your own scripts and SaaS. POST <code>/routines/:id/run</code> and go.</p>
    </div>
  </div>
</div>


---

<!-- ══════════════════════════════════════════════════ -->
<!-- SLIDE 3 · THE COMMAND                             -->
<!-- ══════════════════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 01 — the command</span>
  <span class="page-label">/schedule</span>
</div>

## One slash, one <span class="accent-amber">routine.</span>

Inside Claude Code, `/schedule` creates the routine. Prompt, repo, connectors — and when it should run.

<div class="code-block">
  <div class="cb-bar">
    <span class="cb-dot r"></span><span class="cb-dot y"></span><span class="cb-dot g"></span>
    <span class="cb-title">~/acme-saas · claude-code</span>
    <span class="cb-status" style="color:var(--amber);">● creating routine</span>
  </div>
  <div class="cb-body"><span class="cmd">$</span> claude <span class="val">/schedule</span>
<span class="key">?</span> name       <span class="arr">›</span> <span class="str">"nightly-audit"</span>
<span class="key">?</span> prompt     <span class="arr">›</span> <span class="str">"fix flaky tests + types"</span>
<span class="key">?</span> repo       <span class="arr">›</span> <span class="val">acme/saas-core</span>
<span class="key">?</span> cron       <span class="arr">›</span> <span class="val">0 3 * * *</span>  <span class="cm">(3 AM daily)</span>
<span class="key">?</span> connectors <span class="arr">›</span> <span class="val">github</span> · <span class="val">linear</span> · <span class="val">slack</span>

<span class="check">✓</span> saved · id: <span class="str">rt_8fk2a</span>
<span class="arr">→</span> next run <span class="val">tonight @ 03:00</span></div>
</div>

<div class="insight">
  <div class="insight-label">the moment it clicks</div>
  <p>Close the laptop. Routine keeps going. Wake up to <strong>3 open PRs.</strong></p>
</div>


---

<!-- ══════════════════════════════════════════════════ -->
<!-- SLIDE 4 · THREE TRIGGERS                          -->
<!-- ══════════════════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 02 — triggers</span>
  <span class="page-label">cron · webhook · api</span>
</div>

## Three ways to <span class="accent-purple">fire it.</span>

<div class="cards">
  <div class="card">
    <span class="card-icon">⏰</span>
    <h3>CRON</h3>
    <p>On a clock. Every night, every Monday, every 15 min.</p>
    <span class="pill green">0 3 * * *</span>
  </div>
  <div class="card">
    <span class="card-icon">🔗</span>
    <h3>WEBHOOK</h3>
    <p>On events. GitHub fires. New PR, issue, push — Claude reacts.</p>
    <span class="pill purple">on: pull_request</span>
  </div>
  <div class="card" style="grid-column: span 2;">
    <span class="card-icon">&lt;/&gt;</span>
    <h3>API</h3>
    <p>On demand. Your scripts, your SaaS — POST and run.</p>
    <span class="pill">POST /routines/:id/run</span>
  </div>
</div>

<div class="insight">
  <div class="insight-label">one routine, multiple triggers</div>
  <p>A single routine can combine cron <strong>+</strong> webhook <strong>+</strong> API. Mix and match.</p>
</div>


---

<!-- ══════════════════════════════════════════════════ -->
<!-- SLIDE 5 · 4 ROUTINES WORTH GOLD                  -->
<!-- ══════════════════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 03 — what to run</span>
  <span class="page-label">4 routines worth gold</span>
</div>

<div class="cards">
  <div class="card">
    <span class="card-icon">✓</span>
    <h3>Nightly audit</h3>
    <p>Tests, types, deps. One PR per fix with a clean changelog.</p>
    <span class="pill green">cron · 0 3 * * *</span>
  </div>
  <div class="card">
    <span class="card-icon">📄</span>
    <h3>PR reviewer</h3>
    <p>Every new PR gets a technical review, risks and exec summary.</p>
    <span class="pill purple">on: pull_request</span>
  </div>
  <div class="card">
    <span class="card-icon">📅</span>
    <h3>Weekly digest</h3>
    <p>Monday 8 AM: commits, closed issues, metrics → Slack.</p>
    <span class="pill">cron · 0 8 * * 1</span>
  </div>
  <div class="card">
    <span class="card-icon">⏱</span>
    <h3>Issue triage</h3>
    <p>New issue → label, priority, owner, duplicates flagged.</p>
    <span class="pill">on: issues.opened</span>
  </div>
</div>

<div class="insight">
  <div class="insight-label">rule of thumb</div>
  <p>If you do it <strong>every week by hand</strong> and it's boring → it's a routine.</p>
</div>


---

<!-- ══════════════════════════════════════════════════ -->
<!-- SLIDE 6 · WRITING A GOOD PROMPT                   -->
<!-- ══════════════════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 04 — writing prompts</span>
  <span class="page-label">the most critical step</span>
</div>

## A bad prompt <span class="accent-amber">breaks</span> the routine.

Routines run without human approval. **The prompt carries all the cognitive load.**

<div class="code-block">
  <div class="cb-bar">
    <span class="cb-dot r"></span><span class="cb-dot y"></span><span class="cb-dot g"></span>
    <span class="cb-title">prompt comparison</span>
  </div>
  <div class="cb-body"><span style="color:#f87171;">✗ bad  ›</span> <span class="key">"Check for issues."</span>

<span class="check">✓ good ›</span> <span class="str">"Read all GitHub issues opened today
         in {repo}, apply label from
         [bug, feature, docs, needs-triage],
         assign based on files referenced,
         post summary to #dev-standup."</span></div>
</div>

<div class="list">
  <div class="list-item">
    <span class="list-num">01</span>
    <span class="list-text"><strong>Specify what "done" looks like</strong> — a Slack message, a draft PR, a labeled issue.</span>
  </div>
  <div class="list-item">
    <span class="list-num">02</span>
    <span class="list-text"><strong>Name which connectors to use</strong> — GitHub, Slack, Linear, etc.</span>
  </div>
  <div class="list-item">
    <span class="list-num">03</span>
    <span class="list-text"><strong>Be concrete about scope</strong> — "issues opened today", not "recent issues".</span>
  </div>
</div>


---

<!-- ══════════════════════════════════════════════════ -->
<!-- SLIDE 7 · THE MENTAL SHIFT                        -->
<!-- ══════════════════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 05 — why it matters</span>
  <span class="page-label">the mental shift</span>
</div>

## From assistant to <span class="accent-green">night-shift teammate.</span>

Claude Code stopped being a terminal helper. Now it's a process that **works while you're gone.**

<div class="compare">
  <div class="compare-col">
    <div class="compare-label before">BEFORE</div>
    <h3>You, in the terminal</h3>
    <p>Open laptop → open Claude → paste prompt → wait → close → tomorrow repeat.</p>
    <div class="compare-tags">
      <span class="ctag">sync</span>
      <span class="ctag">manual</span>
      <span class="ctag">your time</span>
    </div>
  </div>
  <div class="compare-col now-col">
    <div class="compare-label now">NOW</div>
    <h3>Claude, in the background</h3>
    <p>Set it once. Runs on cron, GitHub, API. Wake up to PRs, reviews, summaries.</p>
    <div class="compare-tags">
      <span class="ctag g">async</span>
      <span class="ctag g">headless</span>
      <span class="ctag g">runs alone</span>
    </div>
  </div>
</div>

<div class="insight">
  <div class="insight-label">the insight</div>
  <p>Your repo now has its own <strong>heartbeat</strong>. It does things without you — and that reshapes your week.</p>
</div>


---

<!-- ══════════════════════════════════════════════════ -->
<!-- SLIDE 8 · PLAN LIMITS & SETUP                     -->
<!-- ══════════════════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 06 — limits & setup</span>
  <span class="page-label">what you need to know</span>
</div>

## Plan limits + <span class="accent-amber">how to start.</span>

<div class="cards">
  <div class="card">
    <span class="card-icon">🟡</span>
    <h3>Pro</h3>
    <p>5 routine runs per day. Draws from your regular usage.</p>
    <span class="pill">$20 / mo</span>
  </div>
  <div class="card">
    <span class="card-icon">🟠</span>
    <h3>Max</h3>
    <p>15 routine runs per day. More headroom for heavy automation.</p>
    <span class="pill">$100 / mo</span>
  </div>
  <div class="card" style="grid-column: span 2;">
    <span class="card-icon">🏢</span>
    <h3>Team / Enterprise</h3>
    <p>25 routine runs per day. Shared across your org's Claude Code seats.</p>
    <span class="pill green">team plan</span>
  </div>
</div>

<div class="list">
  <div class="list-item">
    <span class="list-num">→</span>
    <span class="list-text">Create at <strong>claude.ai/code/routines</strong> or run <code>/schedule</code> in any session</span>
  </div>
  <div class="list-item">
    <span class="list-num">→</span>
    <span class="list-text">Cron expressions faster than <strong>once per hour</strong> are rejected by the system</span>
  </div>
</div>


---

<!-- ══════════════════════════════════════════════════ -->
<!-- SLIDE 9 · CTA                                     -->
<!-- ══════════════════════════════════════════════════ -->

<section class="cta">

<div class="tag green" style="justify-content:center;margin-bottom:18px;">try it tonight</div>

## Which routine would you <span class="accent-green">build first?</span>

<p>Pick one. Start with <code>/schedule</code> inside Claude Code.</p>

<div class="cta-options">
  <div class="cta-option">
    <div class="cta-option-left">
      <span>⏰</span>
      <h3>NIGHTLY AUDIT</h3>
    </div>
    <span class="cta-cmd">comment "AUDIT"</span>
  </div>
  <div class="cta-option">
    <div class="cta-option-left">
      <span>📄</span>
      <h3>PR REVIEWER</h3>
    </div>
    <span class="cta-cmd">comment "PR"</span>
  </div>
  <div class="cta-option">
    <div class="cta-option-left">
      <span>📅</span>
      <h3>WEEKLY DIGEST</h3>
    </div>
    <span class="cta-cmd">comment "DIGEST"</span>
  </div>
</div>


</section>