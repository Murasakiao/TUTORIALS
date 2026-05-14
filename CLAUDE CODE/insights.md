---
marp: true
paginate: true
html: true
size: 4:3
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,400;0,500;0,600;1,400&family=DM+Mono:wght@400;500&display=swap');
  :root{--amber:#f59e0b;--amber-dim:#d97706;--green:#22c55e;--blue:#60a5fa;--purple:#c4b5fd;--white:#f1f5f9;--off-white:#cbd5e1;--subtle:#94a3b8;--muted:#64748b;--bg:#080808;--card-bg:#111111;--card-border:#222222;}
  section{font-family:'DM Sans',sans-serif;background:var(--bg);color:var(--white);padding:44px 52px;box-sizing:border-box;display:flex;flex-direction:column;overflow:hidden;position:relative;}
  h1{font-size:38px;font-weight:700;line-height:1.08;margin:0 0 14px;color:var(--white);letter-spacing:-1.5px;}
  h2{font-size:28px;font-weight:700;line-height:1.1;margin:0 0 14px;color:var(--white);letter-spacing:-1px;border:none;}
  p{font-size:16px;line-height:1.6;color:var(--subtle);margin:0 0 12px;}
  strong{color:var(--white);font-weight:600;}em{color:var(--muted);font-style:normal;}
  code{font-family:'DM Mono',monospace;background:var(--card-bg);border:1px solid var(--card-border);color:var(--amber);padding:1px 6px;border-radius:4px;font-size:.88em;}
  .tag{display:flex;align-items:center;gap:12px;font-family:'DM Mono',monospace;font-size:11px;font-weight:500;letter-spacing:3px;color:var(--amber);text-transform:uppercase;margin-bottom:18px;}
  .tag::before{content:'';display:block;width:24px;height:2px;background:var(--amber);flex-shrink:0;}
  .header-row{display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;}
  .page-num{font-family:'DM Mono',monospace;font-size:10px;color:var(--amber-dim);letter-spacing:2px;text-transform:uppercase;}
  .page-label{font-family:'DM Mono',monospace;font-size:10px;color:var(--muted);}
  .cards{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px;}
  .card{background:var(--card-bg);border:1px solid var(--card-border);border-radius:10px;padding:14px;}
  .card-icon{font-size:17px;margin-bottom:6px;display:block;}
  .card h3{font-size:14px;font-weight:600;color:var(--white);margin:0 0 4px;}
  .card p{font-size:13px;color:var(--subtle);line-height:1.45;margin:0;}
  .cards-col{display:flex;flex-direction:column;gap:8px;margin-bottom:12px;}
  .card-row{background:var(--card-bg);border:1px solid var(--card-border);border-radius:10px;padding:12px 16px;display:flex;align-items:flex-start;gap:12px;}
  .card-row-icon{font-size:17px;flex-shrink:0;margin-top:1px;}
  .card-row-body h3{font-size:14px;font-weight:600;color:var(--white);margin:0 0 3px;}
  .card-row-body p{font-size:13px;color:var(--subtle);margin:0;line-height:1.45;}
  .list{display:flex;flex-direction:column;gap:7px;margin-bottom:12px;}
  .list-item{display:flex;align-items:flex-start;gap:12px;background:var(--card-bg);border:1px solid var(--card-border);border-radius:8px;padding:10px 14px;}
  .list-num{font-family:'DM Mono',monospace;font-size:11px;color:var(--amber);flex-shrink:0;margin-top:1px;min-width:18px;}
  .list-text{font-size:13.5px;color:var(--subtle);line-height:1.45;}
  .list-text strong{color:var(--white);}
  .insight{background:var(--card-bg);border:1px solid var(--card-border);border-radius:10px;padding:12px 18px;margin-top:auto;}
  .insight-label{font-family:'DM Mono',monospace;font-size:9px;letter-spacing:3px;color:var(--muted);text-transform:uppercase;margin-bottom:4px;}
  .insight p{font-size:14px;color:var(--off-white);line-height:1.5;margin:0;}
  section.cover{justify-content:flex-end;padding-bottom:80px;background:#050505;}
  section.cover h1{font-size:48px;}
  section.cover p{font-size:17px;color:var(--subtle);}
  section.cta{justify-content:center;align-items:center;text-align:center;background:var(--amber);}
  section.cta h1{color:#0F0F0F;font-size:40px;letter-spacing:-1px;margin-bottom:10px;}
  section.cta h2{color:#3a2e00;font-size:22px;border:none;margin-bottom:12px;}
  section.cta p{color:#5a4700;font-size:16px;max-width:540px;margin:0;}
  section.cta .handle{font-family:'DM Mono',monospace;font-size:13px;color:#7a6000;margin-top:22px;letter-spacing:2px;text-transform:uppercase;}
  section::after{font-family:'DM Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:1px;content:'CLAUDE CODE · /insights · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);position:absolute;bottom:20px;right:40px;}
---

<!-- _class: cover -->

<div class="tag">Claude Code · Command 17</div>

# `/insights`

A month of your usage, turned into an actionable report.

*Most developers have no data on how they use AI. This changes that.*

---

<div class="header-row">
  <span class="page-num">— what it is —</span>
  <span class="page-label">your personal usage report</span>
</div>

## What `/insights` produces

Reads your last 30 days of Claude Code sessions and generates a detailed HTML report showing where you spend time, what's working, what's creating friction, and what you should probably automate or turn into a skill.

<div class="cards-col">
  <div class="card-row">
    <span class="card-row-icon">📊</span>
    <div class="card-row-body">
      <h3>Usage breakdown</h3>
      <p>Which files, directories, and tasks you work on most. Where Claude Code is spending the most tokens on your behalf.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">🔦</span>
    <div class="card-row-body">
      <h3>Friction points</h3>
      <p>Where you're repeating prompts, re-explaining context, or running fix loops more than you should be.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">💡</span>
    <div class="card-row-body">
      <h3>Automation opportunities</h3>
      <p>Recurring patterns that should become skills or loop tasks — identified from your actual behavior, not guesses.</p>
    </div>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— what's in the report —</span>
  <span class="page-label">the eight sections</span>
</div>

## What the report covers

<div class="cards">
  <div class="card">
    <span class="card-icon">🗂️</span>
    <h3>Project hotspots</h3>
    <p>Which files and modules you edited most — and which ones kept needing fixes after Claude touched them.</p>
  </div>
  <div class="card">
    <span class="card-icon">🔁</span>
    <h3>Repeated prompts</h3>
    <p>Prompts you sent more than 3 times. Each one is a skill candidate — the report flags them explicitly.</p>
  </div>
  <div class="card">
    <span class="card-icon">💸</span>
    <h3>Token cost breakdown</h3>
    <p>Where tokens went: file reads, tool calls, conversation history, memory files. See what's expensive.</p>
  </div>
  <div class="card">
    <span class="card-icon">🏆</span>
    <h3>Most effective patterns</h3>
    <p>Prompts that got the best results in fewest turns — your personal best practices, extracted automatically.</p>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— when to use it —</span>
  <span class="page-label">the monthly review</span>
</div>

## When to run `/insights`

<div class="list">
  <div class="list-item">
    <span class="list-num">📅</span>
    <span class="list-text"><strong>Once a month</strong> — the right cadence. Enough history to be meaningful, recent enough to act on.</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>Before a skills audit</strong> — identify what to build next based on what you actually repeat, not what you think you repeat</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>When sessions feel slower than they used to</strong> — the report will show where the new friction is coming from</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>When onboarding a teammate</strong> — share the report to show them how you work and what workflows to adopt</span>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— tips —</span>
  <span class="page-label">act on one thing</span>
</div>

## Getting value from the report

<div class="cards">
  <div class="card">
    <span class="card-icon">1️⃣</span>
    <h3>Act on one finding</h3>
    <p>Don't try to fix everything. Pick the highest-friction item and address it before the next report. One improvement per month compounds.</p>
  </div>
  <div class="card">
    <span class="card-icon">🛠️</span>
    <h3>Convert repeated prompts to skills</h3>
    <p>Any prompt flagged as repeated 3+ times: open <code>/skill-creator</code> right after reading the report and build it immediately.</p>
  </div>
  <div class="card">
    <span class="card-icon">📄</span>
    <h3>Update CLAUDE.md from findings</h3>
    <p>If a pattern shows you keep re-explaining the same thing, that explanation belongs in CLAUDE.md — not in every prompt.</p>
  </div>
  <div class="card">
    <span class="card-icon">🔄</span>
    <h3>Pair with /consolidate-memory</h3>
    <p>Run both together monthly. Insights tells you what to improve. Consolidate cleans up the memory that's slowing things down.</p>
  </div>
</div>

---

<!-- _class: cta -->

<div class="tag" style="justify-content:center;color:#0a0a0a;margin-bottom:20px;">Claude Code · /insights</div>

# You can't improve<br>what you can't see.

## Run it monthly. Act on one finding.

<p>Repeated prompts → skills. Re-explained context → CLAUDE.md. Slow sessions → /consolidate-memory. One report, three actions.</p>

<div class="handle">Claude Code · Build Your Own</div>