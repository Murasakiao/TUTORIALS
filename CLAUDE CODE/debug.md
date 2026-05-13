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
  section::after{font-family:'DM Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:1px;content:'CLAUDE CODE · /debug · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);position:absolute;bottom:20px;right:40px;}
---

<!-- _class: cover -->

<div class="tag">Claude Code · Command 08 · Skill</div>

# `/debug`

Something is wrong. Here's how to find out why.

*Enables session logging and focuses Claude on the problem.*

---

<div class="header-row">
  <span class="page-num">— what it is —</span>
  <span class="page-label">session-level diagnostics</span>
</div>

## What `/debug` does

Turns on debug logging for the current session and reads the log to help diagnose what went wrong. Debug mode is off by default — `/debug` starts capturing everything from that moment forward.

<div class="compare">
  <div class="compare-col">
    <div class="compare-label">Without /debug</div>
    <h3>Session runs silently</h3>
    <p>Normal operation. No log captured. You can't see what Claude did under the hood or why something failed.</p>
  </div>
  <div class="compare-col good">
    <div class="compare-label good">With /debug</div>
    <h3>Everything is logged</h3>
    <p>Tool calls, decisions, errors, retries — all captured from the moment you run it. Claude reads the log and analyzes.</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">important</div>
  <p>Only captures from the point you run <code>/debug</code> forward. Run it <strong>as soon as something starts going wrong</strong> — not after.</p>
</div>

---

<div class="header-row">
  <span class="page-num">— how it works —</span>
  <span class="page-label">plain and focused</span>
</div>

## Two ways to use `/debug`

<div class="cards">
  <div class="card">
    <span class="card-icon">🪵</span>
    <h3>Plain: <code>/debug</code></h3>
    <p>Starts debug logging and reads the session log. Claude analyzes whatever it finds without specific guidance.</p>
  </div>
  <div class="card">
    <span class="card-icon">🎯</span>
    <h3>Focused: <code>/debug [description]</code></h3>
    <p><code>/debug auth tokens not refreshing</code> — tell Claude what's wrong and it focuses the log analysis on that issue.</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">/debug vs /doctor</div>
  <p><code>/doctor</code> checks your <strong>Claude Code installation</strong> — wrong node version, missing config, etc. <code>/debug</code> diagnoses <strong>session behavior</strong> — what Claude is doing and why it's failing. Different problems, different tools.</p>
</div>

---

<div class="header-row">
  <span class="page-num">— when to use it —</span>
  <span class="page-label">the failure signals</span>
</div>

## When to run `/debug`

<div class="list">
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>Claude keeps failing on the same step</strong> — something is going wrong in the loop and you need to see what</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>Tool calls producing unexpected results</strong> — Claude is calling a tool but the output isn't what you'd expect</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>Agentic tasks stopping early or looping</strong> — the loop is broken and you don't know why</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>Before filing a bug report</strong> — attach the debug session to give the team full context</span>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— tips —</span>
  <span class="page-label">get useful output</span>
</div>

## Getting the most from `/debug`

<div class="cards">
  <div class="card">
    <span class="card-icon">⚡</span>
    <h3>Run it early</h3>
    <p>As soon as something feels wrong. Log capture only starts from when you run it — waiting loses context.</p>
  </div>
  <div class="card">
    <span class="card-icon">🎯</span>
    <h3>Describe the symptom</h3>
    <p>The more specific your description, the more focused the analysis. "fails" is vague. "returns 401 on token refresh" is actionable.</p>
  </div>
  <div class="card">
    <span class="card-icon">🔁</span>
    <h3>Reproduce after enabling</h3>
    <p>After running /debug, trigger the failing action again so it's captured in the log. Then Claude can read what actually happened.</p>
  </div>
  <div class="card">
    <span class="card-icon">📤</span>
    <h3>Pair with /feedback</h3>
    <p>Found a Claude Code bug? Run <code>/feedback</code> right after <code>/debug</code> — your report will include the session log automatically.</p>
  </div>
</div>

---

<!-- _class: cta -->

<div class="tag" style="justify-content:center;color:#0a0a0a;margin-bottom:20px;">Claude Code · /debug</div>

# Something's wrong.<br>Run it early.

## Don't debug blind. Turn the log on first.

<p><code>/debug [what's going wrong]</code> — then reproduce the failure. Claude reads the log and tells you what it sees.</p>

<div class="handle">Claude Code · Quality Gates</div>