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
  .compare{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:10px;}
  .compare-col{background:var(--card-bg);border:1px solid var(--card-border);border-radius:10px;padding:14px 16px;}
  .compare-col.good{border-color:#14532d;}
  .compare-label{font-family:'DM Mono',monospace;font-size:9px;letter-spacing:3px;text-transform:uppercase;margin-bottom:6px;color:var(--muted);}
  .compare-label.bad{color:#ef4444;}.compare-label.good{color:var(--green);}
  .compare-col h3{font-size:14px;font-weight:600;color:var(--white);margin:0 0 5px;}
  .compare-col p{font-size:13px;color:var(--subtle);line-height:1.45;margin:0;}
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
  section::after{font-family:'DM Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:1px;content:'CLAUDE CODE · /compact · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);position:absolute;bottom:20px;right:40px;}
---

<!-- _class: cover -->

<div class="tag">Claude Code · Command 02</div>

# `/compact`

Your session is getting slow. This fixes it.

*The token lifesaver for long working sessions.*

---

<div class="header-row">
  <span class="page-num">— what it is —</span>
  <span class="page-label">how context windows fill up</span>
</div>

## The problem `/compact` solves

Every message, every file Claude reads, every tool output — it all stacks up in the context window. When it fills up, Claude starts forgetting earlier parts of the conversation. `/compact` summarizes everything into a dense snapshot so you can keep going.

<div class="cards">
  <div class="card">
    <span class="card-icon">📈</span>
    <h3>Context grows with every turn</h3>
    <p>Tool outputs are the biggest culprit — each file read and bash result adds hundreds of tokens silently.</p>
  </div>
  <div class="card">
    <span class="card-icon">🧠</span>
    <h3>Claude forgets when it's full</h3>
    <p>Once the window is too full, early instructions and decisions fall out. Quality drops before you notice.</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">what /compact does</div>
  <p>Replaces the full conversation history with a <strong>dense summary</strong> — keeping decisions, code state, and key context, dropping the noise.</p>
</div>

---

<div class="header-row">
  <span class="page-num">— how it works —</span>
  <span class="page-label">plain and focused modes</span>
</div>

## Two ways to use `/compact`

<div class="compare">
  <div class="compare-col">
    <div class="compare-label">Plain</div>
    <h3><code>/compact</code></h3>
    <p>Claude summarizes the session automatically, preserving what it thinks matters most. Good for general use.</p>
  </div>
  <div class="compare-col good">
    <div class="compare-label good">Focused</div>
    <h3><code>/compact focus on X</code></h3>
    <p>Tell Claude what to keep sharp. <em>"Focus on the auth module and current test failures"</em> — that thread stays clear.</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">what gets preserved</div>
  <p>The current task · decisions already made · file states · constraints you set · errors being debugged</p>
</div>

---

<div class="header-row">
  <span class="page-num">— when to use it —</span>
  <span class="page-label">proactive beats reactive</span>
</div>

## When to run `/compact`

<div class="list">
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>Context usage above 80%</strong> — check with <code>/context</code>, then compact before it hits the ceiling</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>Switching to a new phase</strong> — finished a feature, starting a new one — compact at the boundary</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>Claude seems to be forgetting earlier instructions</strong> — compact + restate the current goal</span>
  </div>
  <div class="list-item">
    <span class="list-num">🚫</span>
    <span class="list-text"><strong>Don't use it to start a new task</strong> — use <code>/clear</code> for that. Compact continues; clear resets.</span>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— mistakes & tips —</span>
  <span class="page-label">get more out of it</span>
</div>

## Common mistakes + pro tips

<div class="cards">
  <div class="card">
    <span class="card-icon">⚠️</span>
    <h3>Waiting too long</h3>
    <p>Don't wait for the warning. By then Claude is already degraded. Run it proactively at phase transitions.</p>
  </div>
  <div class="card">
    <span class="card-icon">⚠️</span>
    <h3>Compacting without a focus</h3>
    <p>If you're mid-debug, tell Claude what to keep: <code>/compact focus on the failing test in auth.ts</code>.</p>
  </div>
  <div class="card">
    <span class="card-icon">💡</span>
    <h3>Check first with /context</h3>
    <p>Run <code>/context</code> before compacting so you understand <em>what</em> is filling the window and can compact intelligently.</p>
  </div>
  <div class="card">
    <span class="card-icon">💡</span>
    <h3>Restate the goal after</h3>
    <p>After compacting, send one message re-confirming the current task. Keeps Claude sharply aligned on what's next.</p>
  </div>
</div>

---

<!-- _class: cta -->

<div class="tag" style="justify-content:center;color:#0a0a0a;margin-bottom:20px;">Claude Code · /compact</div>

# Don't wait for<br>the warning.

## Compact at phase transitions, not in crisis.

<p>Run <code>/context</code> first. Then <code>/compact focus on [current task]</code>. Keep going.</p>

<div class="handle">Claude Code · Session Essentials</div>