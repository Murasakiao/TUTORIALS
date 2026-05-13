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
  section::after{font-family:'DM Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:1px;content:'CLAUDE CODE · /security-review · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);position:absolute;bottom:20px;right:40px;}
---

<!-- _class: cover -->

<div class="tag">Claude Code · Command 07</div>

# `/security-review`

Scan your branch for vulnerabilities before they ship.

*Scoped. Targeted. Run it before every sensitive PR.*

---

<div class="header-row">
  <span class="page-num">— what it is —</span>
  <span class="page-label">branch-scoped security scan</span>
</div>

## What `/security-review` does

Reads the git diff on your current branch and analyzes only your changes for security vulnerabilities. Not a general codebase audit — a targeted scan of exactly what you modified.

<div class="cards-col">
  <div class="card-row">
    <span class="card-row-icon">🔍</span>
    <div class="card-row-body">
      <h3>Reads the git diff</h3>
      <p>Only reviews what changed on your branch — fast, focused, not a full-codebase scan.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">🛡️</span>
    <div class="card-row-body">
      <h3>Identifies real risk categories</h3>
      <p>SQL injection · XSS · exposed credentials · insecure configs · auth bypass · data exposure.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">📋</span>
    <div class="card-row-body">
      <h3>Read-only analysis</h3>
      <p>It reports findings — it does not apply fixes. You decide what to address and how.</p>
    </div>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— what it catches —</span>
  <span class="page-label">the risk categories</span>
</div>

## What gets flagged

<div class="cards">
  <div class="card">
    <span class="card-icon">💉</span>
    <h3>Injection risks</h3>
    <p>SQL injection, command injection, template injection — anywhere untrusted input reaches a dangerous sink.</p>
  </div>
  <div class="card">
    <span class="card-icon">🔑</span>
    <h3>Exposed credentials</h3>
    <p>API keys, passwords, tokens hardcoded or committed accidentally. Catches them before they hit the remote.</p>
  </div>
  <div class="card">
    <span class="card-icon">🔓</span>
    <h3>Auth and access issues</h3>
    <p>Missing authorization checks, broken access control, unauthenticated endpoints that should be protected.</p>
  </div>
  <div class="card">
    <span class="card-icon">📤</span>
    <h3>Data exposure</h3>
    <p>Sensitive fields returned in API responses, logging of PII, insecure data storage or transmission.</p>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— when to use it —</span>
  <span class="page-label">non-negotiable surfaces</span>
</div>

## When to run `/security-review`

<div class="list">
  <div class="list-item">
    <span class="list-num">🔴</span>
    <span class="list-text"><strong>Any PR touching auth, login, or session handling</strong> — mandatory, no exceptions</span>
  </div>
  <div class="list-item">
    <span class="list-num">🔴</span>
    <span class="list-text"><strong>Any PR touching user input handling or API endpoints</strong> — injection and exposure risks live here</span>
  </div>
  <div class="list-item">
    <span class="list-num">🔴</span>
    <span class="list-text"><strong>Any PR touching data storage, payments, or external integrations</strong> — high blast radius if wrong</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>Before any public API goes live</strong> — catch what the code review might miss</span>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— tips —</span>
  <span class="page-label">use it well</span>
</div>

## Getting the most from `/security-review`

<div class="cards">
  <div class="card">
    <span class="card-icon">🔄</span>
    <h3>Pair with /simplify</h3>
    <p>Run /simplify first for code quality. Then /security-review for vulnerabilities. Different tools, different jobs.</p>
  </div>
  <div class="card">
    <span class="card-icon">📖</span>
    <h3>Read every finding</h3>
    <p>It reports, it doesn't auto-fix. Read each item, understand it, then ask Claude to help address the ones that are real.</p>
  </div>
  <div class="card">
    <span class="card-icon">🏷️</span>
    <h3>Not all findings are critical</h3>
    <p>Some flags are informational. Ask Claude to explain the severity and exploitability of anything you're unsure about.</p>
  </div>
  <div class="card">
    <span class="card-icon">📅</span>
    <h3>Run it on feature branches</h3>
    <p>Don't wait for main. Run on the feature branch before requesting review — fix before the reviewer even sees it.</p>
  </div>
</div>

---

<!-- _class: cta -->

<div class="tag" style="justify-content:center;color:#0a0a0a;margin-bottom:20px;">Claude Code · /security-review</div>

# Ship code.<br>Not vulnerabilities.

## Run it before every PR that touches auth or data.

<p>It takes seconds. The cost of skipping it is measured differently.</p>

<div class="handle">Claude Code · Quality Gates</div>