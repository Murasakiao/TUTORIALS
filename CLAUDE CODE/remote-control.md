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
  section::after{font-family:'DM Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:1px;content:'CLAUDE CODE · /remote-control · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);position:absolute;bottom:20px;right:40px;}
---

<!-- _class: cover -->

<div class="tag">Claude Code · Command 14</div>

# `/remote-control`

Control your local terminal from a browser — anywhere.

*Your session stays local. You don't have to.*

---

<div class="header-row">
  <span class="page-num">— what it is —</span>
  <span class="page-label">browser interface for local sessions</span>
</div>

## What `/remote-control` does

Makes your active Claude Code terminal session accessible through claude.ai in any browser. Your code, tools, files, and MCP connections stay on your machine — but you can send prompts and see results from anywhere.

<div class="cards">
  <div class="card">
    <span class="card-icon">🖥️</span>
    <h3>Session stays local</h3>
    <p>Your code never leaves your machine. Claude runs against your actual files and local environment — not a cloud copy.</p>
  </div>
  <div class="card">
    <span class="card-icon">🌐</span>
    <h3>Control from anywhere</h3>
    <p>claude.ai becomes a remote terminal interface. Send prompts from your phone, a tablet, or another machine.</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">alias</div>
  <p>Also available as <code>/rc</code> — shorter to type, identical behavior. Use whichever you prefer.</p>
</div>

---

<div class="header-row">
  <span class="page-num">— how it works —</span>
  <span class="page-label">the connection model</span>
</div>

## How the connection works

<div class="list">
  <div class="list-item">
    <span class="list-num">01</span>
    <span class="list-text"><strong>Run <code>/remote-control</code></strong> in your terminal — Claude Code generates a session link and displays it</span>
  </div>
  <div class="list-item">
    <span class="list-num">02</span>
    <span class="list-text"><strong>Open the link in claude.ai</strong> — your terminal session appears as an active chat interface in the browser</span>
  </div>
  <div class="list-item">
    <span class="list-num">03</span>
    <span class="list-text"><strong>Send prompts from the browser</strong> — they execute against your local Claude Code session in real time</span>
  </div>
  <div class="list-item">
    <span class="list-num">04</span>
    <span class="list-text"><strong>Results appear in both places</strong> — you can monitor in the terminal and interact in the browser simultaneously</span>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— when to use it —</span>
  <span class="page-label">the right situations</span>
</div>

## When `/remote-control` shines

<div class="cards">
  <div class="card">
    <span class="card-icon">🤖</span>
    <h3>Long agentic tasks</h3>
    <p>Start a long autonomous run, then monitor and steer it from your phone while you're away from the desk.</p>
  </div>
  <div class="card">
    <span class="card-icon">💻</span>
    <h3>Multi-device workflows</h3>
    <p>Start on your laptop, continue from an iPad or secondary screen — same session, no context lost.</p>
  </div>
  <div class="card">
    <span class="card-icon">🏃</span>
    <h3>Check-ins on the go</h3>
    <p>Left the office while a build is running. Check the status and send the next instruction from your phone.</p>
  </div>
  <div class="card">
    <span class="card-icon">👥</span>
    <h3>Live demos and pairing</h3>
    <p>Share the session link with a colleague for real-time pairing — both of you can see the same session state.</p>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— tips —</span>
  <span class="page-label">use it safely</span>
</div>

## Getting the most from `/remote-control`

<div class="cards">
  <div class="card">
    <span class="card-icon">🔒</span>
    <h3>Treat the link as sensitive</h3>
    <p>The session link gives access to your local Claude Code environment. Don't share it in public channels or with people you don't trust.</p>
  </div>
  <div class="card">
    <span class="card-icon">⏱️</span>
    <h3>Sessions expire</h3>
    <p>Remote control links are time-limited. If you step away too long, you'll need to run <code>/rc</code> again to generate a fresh link.</p>
  </div>
  <div class="card">
    <span class="card-icon">📡</span>
    <h3>Needs a running terminal</h3>
    <p>Your local machine must stay on and the Claude Code session must remain open. It's remote control — not cloud hosting.</p>
  </div>
  <div class="card">
    <span class="card-icon">🤝</span>
    <h3>Pair with /loop</h3>
    <p>Start a <code>/loop</code> monitoring task, then connect via <code>/rc</code> from your phone to check progress and send adjustments.</p>
  </div>
</div>

---

<!-- _class: cta -->

<div class="tag" style="justify-content:center;color:#0a0a0a;margin-bottom:20px;">Claude Code · /remote-control</div>

# Your terminal.<br>From anywhere.

## Start the task. Walk away. Check in from your phone.

<p>Run <code>/rc</code>, grab the link, open it in claude.ai. Your local session is now in your pocket.</p>

<div class="handle">Claude Code · Power Tools</div>