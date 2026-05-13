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
  section::after{font-family:'DM Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:1px;content:'CLAUDE CODE · /simplify · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);position:absolute;bottom:20px;right:40px;}
---

<!-- _class: cover -->

<div class="tag">Claude Code · Command 06 · Skill</div>

# `/simplify`

Three agents review your code before you ship it.

*The quality gate Claude fast coders skip — and shouldn't.*

---

<div class="header-row">
  <span class="page-num">— what it is —</span>
  <span class="page-label">a parallel code review</span>
</div>

## What `/simplify` does

Spawns three review agents in parallel that each scan your recently changed files from a different angle. They aggregate their findings, then apply fixes — all before you open a PR.

<div class="cards-col">
  <div class="card-row">
    <span class="card-row-icon">🏗️</span>
    <div class="card-row-body">
      <h3>Agent 1 — Architecture</h3>
      <p>Looks for structural issues: tight coupling, missing abstractions, logic that belongs elsewhere.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">♻️</span>
    <div class="card-row-body">
      <h3>Agent 2 — Duplication</h3>
      <p>Finds repeated logic, functions that could be extracted, and copy-paste patterns that crept in.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">⚡</span>
    <div class="card-row-body">
      <h3>Agent 3 — Performance</h3>
      <p>Spots inefficiencies: unnecessary re-renders, redundant queries, memory usage issues, slow loops.</p>
    </div>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— how it works —</span>
  <span class="page-label">plain and focused modes</span>
</div>

## Two ways to run `/simplify`

<div class="cards">
  <div class="card">
    <span class="card-icon">🔍</span>
    <h3>Plain: <code>/simplify</code></h3>
    <p>Reviews all recently changed files across all three dimensions. Good default before any PR.</p>
  </div>
  <div class="card">
    <span class="card-icon">🎯</span>
    <h3>Focused: <code>/simplify focus on X</code></h3>
    <p>Pass text to concentrate the review: <code>/simplify focus on memory efficiency in the data layer</code>.</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">what it reviews</div>
  <p>Only your <strong>recently changed files</strong> — not the whole codebase. Scoped to what you actually touched this session.</p>
</div>

---

<div class="header-row">
  <span class="page-num">— when to use it —</span>
  <span class="page-label">the pre-PR habit</span>
</div>

## When to run `/simplify`

<div class="list">
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>After a feature works but before the PR</strong> — the right moment, every time</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>After a long multi-turn session</strong> — Claude writes fast; accumulated turns produce accumulated complexity</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>Before asking for code review from a human</strong> — clean up the obvious issues first</span>
  </div>
  <div class="list-item">
    <span class="list-num">🚫</span>
    <span class="list-text"><strong>Not during active development</strong> — wait until the feature is working. Simplifying half-built code creates confusion.</span>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— tips —</span>
  <span class="page-label">use it right</span>
</div>

## Pro tips for `/simplify`

<div class="cards">
  <div class="card">
    <span class="card-icon">🔄</span>
    <h3>Run /diff after</h3>
    <p>Always review what /simplify changed before committing. It applies fixes automatically — check every one.</p>
  </div>
  <div class="card">
    <span class="card-icon">🎯</span>
    <h3>Focus on specific concerns</h3>
    <p>If you know there's a performance issue, tell it: <code>/simplify the database query in UserService</code>.</p>
  </div>
  <div class="card">
    <span class="card-icon">🔁</span>
    <h3>Pair with /security-review</h3>
    <p>Run both before shipping. Simplify handles code quality. Security-review handles vulnerabilities. Different jobs.</p>
  </div>
  <div class="card">
    <span class="card-icon">📏</span>
    <h3>Don't skip it on small PRs</h3>
    <p>Accumulated complexity from "small" changes is exactly how codebases get messy. Run it every time.</p>
  </div>
</div>

---

<!-- _class: cta -->

<div class="tag" style="justify-content:center;color:#0a0a0a;margin-bottom:20px;">Claude Code · /simplify</div>

# It works.<br>Now make it clean.

## Feature done → /simplify → /diff → PR.

<p>Claude writes fast but not always clean. Three agents catch what one pass misses.</p>

<div class="handle">Claude Code · Quality Gates</div>