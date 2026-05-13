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
  section::after{font-family:'DM Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:1px;content:'CLAUDE CODE · /clear · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);position:absolute;bottom:20px;right:40px;}
---

<!-- _class: cover -->

<div class="tag">Claude Code · Command 04</div>

# `/clear`

New task. Fresh start. Same project.

*Wipe the session without losing your project memory.*

---

<div class="header-row">
  <span class="page-num">— what it is —</span>
  <span class="page-label">two things cleared, one thing kept</span>
</div>

## What `/clear` does

Wipes the entire conversation history from the context window, giving Claude a completely blank slate. But it does not delete your `CLAUDE.md` or auto-memory — Claude still knows your project the moment you send the next message.

<div class="cards">
  <div class="card">
    <span class="card-icon">🗑️</span>
    <h3>Clears conversation history</h3>
    <p>Every message, every tool output, every file read from this session — gone. The context window is empty.</p>
  </div>
  <div class="card">
    <span class="card-icon">💾</span>
    <h3>Project memory survives</h3>
    <p>CLAUDE.md and auto-memory files are untouched. Claude reloads them on your next message automatically.</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">aliases</div>
  <p>Also works as <code>/reset</code> and <code>/new</code> — three names for exactly the same action.</p>
</div>

---

<div class="header-row">
  <span class="page-num">— clear vs compact —</span>
  <span class="page-label">the most important distinction</span>
</div>

## `/clear` vs `/compact` — know the difference

<div class="compare">
  <div class="compare-col">
    <div class="compare-label bad">❌ Wrong choice</div>
    <h3>Clearing mid-task</h3>
    <p>If you're still working on the same feature, clearing loses all the context Claude built up. Use compact instead.</p>
  </div>
  <div class="compare-col good">
    <div class="compare-label good">✅ Right choice</div>
    <h3>Clearing between tasks</h3>
    <p>Feature is done. Now starting something unrelated. Clear gives Claude a clean slate for the new work.</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">the rule</div>
  <p><strong>/clear</strong> = starting a new task. <strong>/compact</strong> = continuing the same task with more room. Never confuse the two.</p>
</div>

---

<div class="header-row">
  <span class="page-num">— when to use it —</span>
  <span class="page-label">task boundaries</span>
</div>

## When `/clear` is the right move

<div class="list">
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>Between unrelated tasks</strong> — finished auth, now starting the dashboard. Clear and begin fresh.</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>When Claude seems confused by accumulated context</strong> — contradictory instructions from earlier in the session are throwing it off</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>Morning restart</strong> — beginning a new day's work with no leftover noise from yesterday's session</span>
  </div>
  <div class="list-item">
    <span class="list-num">🚫</span>
    <span class="list-text"><strong>Don't clear to save tokens mid-task</strong> — that's /compact's job. Clearing loses your work context.</span>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— tips —</span>
  <span class="page-label">make clearing smooth</span>
</div>

## Getting the most from `/clear`

<div class="cards">
  <div class="card">
    <span class="card-icon">📝</span>
    <h3>Update CLAUDE.md first</h3>
    <p>Before clearing, use <code>/memory</code> to capture any new conventions or constraints you established this session.</p>
  </div>
  <div class="card">
    <span class="card-icon">🎯</span>
    <h3>State the new task immediately</h3>
    <p>After clearing, send a clear task description right away. Don't leave Claude to guess what you're starting on.</p>
  </div>
  <div class="card">
    <span class="card-icon">💡</span>
    <h3>Clear is faster than a new session</h3>
    <p>Closing and reopening Claude Code reloads everything from disk. <code>/clear</code> resets in-place — quicker.</p>
  </div>
  <div class="card">
    <span class="card-icon">🔄</span>
    <h3>Use it freely</h3>
    <p>There's no cost to clearing. When in doubt, clear and restate. A fresh context produces sharper responses.</p>
  </div>
</div>

---

<!-- _class: cta -->

<div class="tag" style="justify-content:center;color:#0a0a0a;margin-bottom:20px;">Claude Code · /clear</div>

# Done with that task.<br>On to the next.

## Clear the session. Keep the memory.

<p>Update CLAUDE.md, run <code>/clear</code>, state the new task. Three steps to a sharp start every time.</p>

<div class="handle">Claude Code · Session Essentials</div>