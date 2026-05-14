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
  section::after{font-family:'DM Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:1px;content:'CLAUDE CODE · /loop · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);position:absolute;bottom:20px;right:40px;}
---

<!-- _class: cover -->

<div class="tag">Claude Code · Command 10 · Skill</div>

# `/loop`

Run a task on repeat while you focus elsewhere.

*Set it. Let Claude handle the checking.*

---

<div class="header-row">
  <span class="page-num">— what it is —</span>
  <span class="page-label">autonomous repeating tasks</span>
</div>

## What `/loop` does

Runs a prompt repeatedly on an interval while your session stays open. Claude self-paces between iterations and acts on what it finds each time. Think of it as a lightweight background agent for monitoring and maintenance tasks.

<div class="cards-col">
  <div class="card-row">
    <span class="card-row-icon">🔁</span>
    <div class="card-row-body">
      <h3>Repeats on your schedule</h3>
      <p>Set an interval — <code>5m</code>, <code>1h</code>, <code>30s</code> — and Claude runs the task each time without you prompting it.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">🤖</span>
    <div class="card-row-body">
      <h3>Autonomous when run alone</h3>
      <p>Run <code>/loop</code> with no arguments and Claude decides what to check and when — a proactive maintenance mode.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">📄</span>
    <div class="card-row-body">
      <h3>Reads a playbook if present</h3>
      <p>Put instructions in <code>.claude/loop.md</code> — Claude reads it at the start of each iteration as its standing orders.</p>
    </div>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— three modes —</span>
  <span class="page-label">how to run it</span>
</div>

## The three ways to use `/loop`

<div class="list">
  <div class="list-item">
    <span class="list-num">01</span>
    <span class="list-text"><strong>With interval + prompt:</strong> <code>/loop 5m check if the deploy pipeline finished and report status</code></span>
  </div>
  <div class="list-item">
    <span class="list-num">02</span>
    <span class="list-text"><strong>Autonomous mode:</strong> <code>/loop</code> — Claude decides what to monitor and at what pace based on project context</span>
  </div>
  <div class="list-item">
    <span class="list-num">03</span>
    <span class="list-text"><strong>Playbook mode:</strong> Create <code>.claude/loop.md</code> with standing instructions — Claude reads it every iteration</span>
  </div>
</div>

<div class="insight">
  <div class="insight-label">alias</div>
  <p>Also available as <code>/proactive</code> — same command, different name. Use whichever feels more natural for your workflow.</p>
</div>

---

<div class="header-row">
  <span class="page-num">— when to use it —</span>
  <span class="page-label">the right jobs for /loop</span>
</div>

## What `/loop` is great for

<div class="cards">
  <div class="card">
    <span class="card-icon">🚀</span>
    <h3>Deploy monitoring</h3>
    <p><code>/loop 2m check if the Vercel deploy succeeded and flag any build errors</code></p>
  </div>
  <div class="card">
    <span class="card-icon">🧪</span>
    <h3>Test watching</h3>
    <p><code>/loop 1m run the failing tests and report which ones are still red</code></p>
  </div>
  <div class="card">
    <span class="card-icon">📊</span>
    <h3>Log tailing</h3>
    <p><code>/loop 30s check the error log for new entries and summarize any new ones</code></p>
  </div>
  <div class="card">
    <span class="card-icon">🔧</span>
    <h3>Maintenance passes</h3>
    <p>Autonomous mode while you're away — Claude proactively checks for lint errors, stale deps, or failing health checks.</p>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— tips & limits —</span>
  <span class="page-label">use it safely</span>
</div>

## Getting the most from `/loop`

<div class="cards">
  <div class="card">
    <span class="card-icon">⏱️</span>
    <h3>Set a sensible interval</h3>
    <p>Too short and you burn tokens fast. Too long and it's not useful for monitoring. 2–5 minutes is a good default.</p>
  </div>
  <div class="card">
    <span class="card-icon">📄</span>
    <h3>Use loop.md for standing orders</h3>
    <p>For recurring maintenance routines, define them in <code>.claude/loop.md</code> once. Reuse across sessions without re-typing.</p>
  </div>
  <div class="card">
    <span class="card-icon">🚫</span>
    <h3>Not for write-heavy tasks</h3>
    <p>Loop is best for read + report tasks. Avoid looping tasks that write files or push to remotes without human review at each step.</p>
  </div>
  <div class="card">
    <span class="card-icon">🛑</span>
    <h3>Ctrl+C to stop</h3>
    <p>The loop runs until you interrupt it. Keep the terminal visible so you can stop it if something unexpected happens.</p>
  </div>
</div>

---

<!-- _class: cta -->

<div class="tag" style="justify-content:center;color:#0a0a0a;margin-bottom:20px;">Claude Code · /loop</div>

# Set it running.<br>Go build something.

## Your terminal works while you do.

<p><code>/loop 5m [what to check]</code> — Claude monitors, reports, and acts. You stay in flow.</p>

<div class="handle">Claude Code · Power Tools</div>