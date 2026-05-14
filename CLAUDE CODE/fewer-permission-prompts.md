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
  section::after{font-family:'DM Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:1px;content:'CLAUDE CODE · /fewer-permission-prompts · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);position:absolute;bottom:20px;right:40px;}
---

<!-- _class: cover -->

<div class="tag">Claude Code · Command 13</div>

# `/fewer-permission`
# `-prompts`

Stop approving the same thing over and over.

*Turns your approval history into permanent rules.*

---

<div class="header-row">
  <span class="page-num">— the problem —</span>
  <span class="page-label">why approvals interrupt flow</span>
</div>

## Why this command exists

By default, Claude Code asks for permission before running Bash commands or calling MCP tools — every time. After your first week, you've approved the same safe operations dozens of times. This command fixes that permanently.

<div class="cards">
  <div class="card">
    <span class="card-icon">🔔</span>
    <h3>Constant interruptions</h3>
    <p>Every <code>npm install</code>, every <code>git status</code>, every read-only file operation — each one pauses the agent to ask.</p>
  </div>
  <div class="card">
    <span class="card-icon">🧠</span>
    <h3>Wasted decisions</h3>
    <p>Approving the same safe tool call repeatedly is cognitive overhead that adds up across a day of work.</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">what it does</div>
  <p>Reads your recent approval history → builds a prioritized allowlist → writes it to <code>.claude/settings.json</code> permanently.</p>
</div>

---

<div class="header-row">
  <span class="page-num">— how it works —</span>
  <span class="page-label">from history to rules</span>
</div>

## How `/fewer-permission-prompts` works

<div class="list">
  <div class="list-item">
    <span class="list-num">01</span>
    <span class="list-text"><strong>Reads your session history</strong> — analyzes which Bash commands and MCP tool calls you've been approving repeatedly</span>
  </div>
  <div class="list-item">
    <span class="list-num">02</span>
    <span class="list-text"><strong>Generates a prioritized allowlist</strong> — the most frequently approved operations ranked by usage frequency</span>
  </div>
  <div class="list-item">
    <span class="list-num">03</span>
    <span class="list-text"><strong>You review and confirm</strong> — it shows you the list before writing anything. You can remove items you want to keep prompting for.</span>
  </div>
  <div class="list-item">
    <span class="list-num">04</span>
    <span class="list-text"><strong>Writes to .claude/settings.json</strong> — rules persist across all future sessions and apply to your whole team if committed to git</span>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— when to use it —</span>
  <span class="page-label">timing matters</span>
</div>

## When to run it

<div class="cards">
  <div class="card">
    <span class="card-icon">📅</span>
    <h3>After your first week</h3>
    <p>Work normally for 5–7 days. Build up real approval history. Then run it once to convert that history into rules.</p>
  </div>
  <div class="card">
    <span class="card-icon">🔄</span>
    <h3>After adding new MCP servers</h3>
    <p>New servers bring new tool calls. Use normally for a few days, then run again to allowlist the safe ones.</p>
  </div>
  <div class="card">
    <span class="card-icon">👥</span>
    <h3>When onboarding teammates</h3>
    <p>Commit the generated <code>settings.json</code> to git so new team members start with pre-approved safe operations.</p>
  </div>
  <div class="card">
    <span class="card-icon">⚠️</span>
    <h3>Not on day one</h3>
    <p>You need real usage history first. Running it immediately generates a thin allowlist based on almost nothing.</p>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— tips —</span>
  <span class="page-label">stay safe while staying fast</span>
</div>

## Safety and flow — both at once

<div class="cards">
  <div class="card">
    <span class="card-icon">🔍</span>
    <h3>Review every entry</h3>
    <p>Before confirming the list, read each item. Remove anything that touches production, deletes data, or feels risky.</p>
  </div>
  <div class="card">
    <span class="card-icon">📖</span>
    <h3>Read the generated rules</h3>
    <p>Open <code>.claude/settings.json</code> after running. Understand what's been allowlisted and what it permits Claude to do.</p>
  </div>
  <div class="card">
    <span class="card-icon">🚫</span>
    <h3>Keep prompts for write ops</h3>
    <p>Read operations are safe to allowlist. Write operations — especially to production — should still require approval.</p>
  </div>
  <div class="card">
    <span class="card-icon">🔁</span>
    <h3>Re-run periodically</h3>
    <p>As your workflow evolves, new patterns emerge. Run it every few months to keep the allowlist current with how you actually work.</p>
  </div>
</div>

---

<!-- _class: cta -->

<div class="tag" style="justify-content:center;color:#0a0a0a;margin-bottom:20px;">Claude Code · /fewer-permission-prompts</div>

# Work normally first.<br>Then run this once.

## Your approval history becomes permanent rules.

<p>Five days of normal work → one command → no more repetitive approvals. Stay in flow without sacrificing safety.</p>

<div class="handle">Claude Code · Power Tools</div>