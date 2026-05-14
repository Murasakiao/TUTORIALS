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
  section::after{font-family:'DM Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:1px;content:'CLAUDE CODE · /consolidate-memory · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);position:absolute;bottom:20px;right:40px;}
---

<!-- _class: cover -->

<div class="tag">Claude Code · Command 11</div>

# `/consolidate-memory`

Clean up what Claude remembers before it slows you down.

*Run it monthly. Memory bloat hurts quality silently.*

---

<div class="header-row">
  <span class="page-num">— the problem —</span>
  <span class="page-label">how memory gets messy</span>
</div>

## Why memory needs maintenance

Every session, Claude can save patterns, preferences, and learnings to auto-memory. Over time — across dozens of sessions — these entries accumulate, conflict, and go stale. The result is a bloated memory file that costs tokens and degrades quality.

<div class="cards">
  <div class="card">
    <span class="card-icon">🔁</span>
    <h3>Duplicates pile up</h3>
    <p>Multiple sessions can each save the same preference slightly differently — creating redundant entries that all load every time.</p>
  </div>
  <div class="card">
    <span class="card-icon">⚔️</span>
    <h3>Conflicts emerge</h3>
    <p>Session A saved "use tabs." Session B saved "use spaces." Both load. Claude picks one unpredictably.</p>
  </div>
  <div class="card">
    <span class="card-icon">👴</span>
    <h3>Entries go stale</h3>
    <p>A preference from 3 months ago may no longer apply. But it still loads and influences every session.</p>
  </div>
  <div class="card">
    <span class="card-icon">💰</span>
    <h3>Bloat costs tokens</h3>
    <p>Larger memory = more tokens loaded every session = less room for your actual work in the context window.</p>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— what it does —</span>
  <span class="page-label">four cleanup operations</span>
</div>

## What `/consolidate-memory` fixes

<div class="cards-col">
  <div class="card-row">
    <span class="card-row-icon">🧹</span>
    <div class="card-row-body">
      <h3>Removes duplicates</h3>
      <p>Merges redundant entries that say the same thing into a single clean fact.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">⚖️</span>
    <div class="card-row-body">
      <h3>Resolves conflicts</h3>
      <p>When two entries contradict each other, keeps the most recent or most specific one and removes the other.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">🗑️</span>
    <div class="card-row-body">
      <h3>Removes stale entries</h3>
      <p>Flags entries that no longer match the current project state and removes them from the active memory file.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">📐</span>
    <div class="card-row-body">
      <h3>Compresses what remains</h3>
      <p>Rewrites surviving entries in their most concise form so each one costs fewer tokens to load.</p>
    </div>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— when to use it —</span>
  <span class="page-label">the maintenance cadence</span>
</div>

## When to run `/consolidate-memory`

<div class="list">
  <div class="list-item">
    <span class="list-num">📅</span>
    <span class="list-text"><strong>Monthly</strong> — the right default cadence for most active Claude Code users</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>After a major project change</strong> — stack migration, architectural refactor, new conventions adopted</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>When Claude seems inconsistent</strong> — ignoring preferences it usually follows is a sign of conflicting memory entries</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>After /context flags memory bloat</strong> — if the visualization shows memory consuming unusual token share</span>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— tips —</span>
  <span class="page-label">memory hygiene</span>
</div>

## Building good memory habits

<div class="cards">
  <div class="card">
    <span class="card-icon">🗓️</span>
    <h3>Schedule it</h3>
    <p>Put it in your calendar as a monthly 5-minute task. Memory hygiene is invisible until it becomes a problem.</p>
  </div>
  <div class="card">
    <span class="card-icon">👁️</span>
    <h3>Review before consolidating</h3>
    <p>Use <code>/memory</code> first to browse what's in auto-memory. Delete obviously wrong entries manually before running consolidate.</p>
  </div>
  <div class="card">
    <span class="card-icon">📌</span>
    <h3>Prefer CLAUDE.md over auto-memory</h3>
    <p>For important conventions, write them in CLAUDE.md manually. Auto-memory is supplemental — it shouldn't carry critical rules.</p>
  </div>
  <div class="card">
    <span class="card-icon">🔄</span>
    <h3>Pair with /context after</h3>
    <p>Run <code>/context</code> after consolidating to confirm the memory footprint actually shrank. Verify the cleanup worked.</p>
  </div>
</div>

---

<!-- _class: cta -->

<div class="tag" style="justify-content:center;color:#0a0a0a;margin-bottom:20px;">Claude Code · /consolidate-memory</div>

# Lean memory.<br>Sharp Claude.

## Run it monthly. It takes two minutes.

<p>Bloated memory degrades quality silently. <code>/consolidate-memory</code> keeps Claude's knowledge clean and current.</p>

<div class="handle">Claude Code · Power Tools</div>