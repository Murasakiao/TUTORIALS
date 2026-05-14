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
  section::after{font-family:'DM Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:1px;content:'CLAUDE CODE · /diff · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);position:absolute;bottom:20px;right:40px;}
---

<!-- _class: cover -->

<div class="tag">Claude Code · Command 09</div>

# `/diff`

See every change Claude made — before you commit.

*The review step most people skip. Don't.*

---

<div class="header-row">
  <span class="page-num">— what it is —</span>
  <span class="page-label">an interactive change viewer</span>
</div>

## What `/diff` shows you

Opens an interactive diff viewer showing every uncommitted change in your repo, plus a per-turn history of exactly what Claude changed on each individual step of the session.

<div class="cards-col">
  <div class="card-row">
    <span class="card-row-icon">📁</span>
    <div class="card-row-body">
      <h3>Full repo diff</h3>
      <p>Every uncommitted change across all files — the same view as <code>git diff</code> but browsable and interactive.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">🔢</span>
    <div class="card-row-body">
      <h3>Per-turn history</h3>
      <p>Left/right arrow keys step through what changed on each individual Claude turn — not just the final state.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">↕️</span>
    <div class="card-row-body">
      <h3>File-by-file navigation</h3>
      <p>Up/down arrows move between files. See exactly which files were touched and where the changes land.</p>
    </div>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— how to navigate —</span>
  <span class="page-label">keyboard controls</span>
</div>

## Navigating `/diff`

<div class="cards">
  <div class="card">
    <span class="card-icon">⬅️➡️</span>
    <h3>Left / Right arrows</h3>
    <p>Switch between the current git diff and the diff from each individual Claude turn. Step through the session history.</p>
  </div>
  <div class="card">
    <span class="card-icon">⬆️⬇️</span>
    <h3>Up / Down arrows</h3>
    <p>Move between files within the current diff view. Jump quickly across all changed files.</p>
  </div>
  <div class="card">
    <span class="card-icon">🔍</span>
    <h3>What to look for</h3>
    <p>Did it change only what you asked? Did it touch any file it should not have? Does the change make sense?</p>
  </div>
  <div class="card">
    <span class="card-icon">🚪</span>
    <h3>Exit</h3>
    <p>Press <code>q</code> to close the diff viewer and return to the session. No changes are applied — it's read-only.</p>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— when to use it —</span>
  <span class="page-label">make it a habit</span>
</div>

## When to run `/diff`

<div class="list">
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>After every multi-file task</strong> — before asking for the next one, always verify what changed</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>After /simplify or /security-review apply fixes</strong> — check exactly what they changed before committing</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>Before any git commit</strong> — your last line of defense before changes become permanent</span>
  </div>
  <div class="list-item">
    <span class="list-num">🚫</span>
    <span class="list-text"><strong>Not a substitute for testing</strong> — /diff shows what changed, not whether it works. Always test after reviewing.</span>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— tips —</span>
  <span class="page-label">review like a pro</span>
</div>

## Getting the most from `/diff`

<div class="cards">
  <div class="card">
    <span class="card-icon">🎯</span>
    <h3>Three questions per file</h3>
    <p>Did it change the right file? Did it change only what I asked? Does the change make logical sense?</p>
  </div>
  <div class="card">
    <span class="card-icon">🕵️</span>
    <h3>Check unexpected files</h3>
    <p>If a file you didn't mention shows up in the diff, find out why before accepting. Scope creep happens silently.</p>
  </div>
  <div class="card">
    <span class="card-icon">🔁</span>
    <h3>Use turn history for debugging</h3>
    <p>If something broke mid-session, step back through turns with the left arrow to find which change introduced the problem.</p>
  </div>
  <div class="card">
    <span class="card-icon">⏱️</span>
    <h3>Review before the next task</h3>
    <p>Catching a bad change now takes seconds. Catching it three tasks later — after Claude built on top of it — takes much longer.</p>
  </div>
</div>

---

<!-- _class: cta -->

<div class="tag" style="justify-content:center;color:#0a0a0a;margin-bottom:20px;">Claude Code · /diff</div>

# Review before<br>you continue.

## Every task. Every time. Before the next prompt.

<p>Catching a mistake now costs seconds. Catching it after Claude built on top of it costs minutes — or more.</p>

<div class="handle">Claude Code · Quality Gates</div>