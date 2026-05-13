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
  section::after{font-family:'DM Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:1px;content:'CLAUDE CODE · /memory · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);position:absolute;bottom:20px;right:40px;}
---

<!-- _class: cover -->

<div class="tag">Claude Code · Command 05</div>

# `/memory`

Edit what Claude always knows about your project.

*Your CLAUDE.md editor — without leaving the terminal.*

---

<div class="header-row">
  <span class="page-num">— what it is —</span>
  <span class="page-label">three layers of memory</span>
</div>

## How Claude's memory works

Claude has three memory layers. `/memory` gives you direct control over all of them.

<div class="cards-col">
  <div class="card-row">
    <span class="card-row-icon">📄</span>
    <div class="card-row-body">
      <h3>CLAUDE.md — project memory</h3>
      <p>You write this. Loaded every session. Stack, conventions, build commands, constraints. The most important file.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">🤖</span>
    <div class="card-row-body">
      <h3>Auto-memory — learned patterns</h3>
      <p>Claude writes this automatically. Preferences, patterns, and insights it learns across multiple sessions.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">⚡</span>
    <div class="card-row-body">
      <h3>Session memory — current context</h3>
      <p>Everything in the current window. This is what /compact and /clear manage. Lost when the session ends.</p>
    </div>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— how it works —</span>
  <span class="page-label">what you can do</span>
</div>

## What `/memory` lets you do

<div class="cards">
  <div class="card">
    <span class="card-icon">✏️</span>
    <h3>Edit CLAUDE.md in-session</h3>
    <p>Opens the file for editing directly. Add a new convention, update a build command, remove outdated info.</p>
  </div>
  <div class="card">
    <span class="card-icon">🔘</span>
    <h3>Toggle auto-memory on/off</h3>
    <p>Control whether Claude saves patterns automatically. Turn it off if you want to manage memory manually.</p>
  </div>
  <div class="card">
    <span class="card-icon">👁️</span>
    <h3>View auto-memory entries</h3>
    <p>See every pattern Claude has saved from past sessions — and delete specific ones you no longer want.</p>
  </div>
  <div class="card">
    <span class="card-icon">🗑️</span>
    <h3>Delete stale entries</h3>
    <p>Remove outdated preferences before they confuse future sessions or crowd out useful context.</p>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— when to use it —</span>
  <span class="page-label">build memory as you work</span>
</div>

## When to run `/memory`

<div class="list">
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>After establishing a new convention mid-session</strong> — add it before you clear or compact so it survives</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>When Claude keeps making the same mistake</strong> — add an explicit constraint to CLAUDE.md to stop it</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>Monthly cleanup</strong> — review auto-memory entries and delete ones that are stale or contradictory</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>After a major refactor</strong> — update stack references, folder paths, and conventions that changed</span>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— what to put in CLAUDE.md —</span>
  <span class="page-label">a practical template</span>
</div>

## What belongs in CLAUDE.md

<div class="cards">
  <div class="card">
    <span class="card-icon">🛠️</span>
    <h3>Stack & commands</h3>
    <p><em>"This is a Next.js 14 + Supabase app. Use <code>bun</code> not npm. Build: <code>bun run build</code>."</em></p>
  </div>
  <div class="card">
    <span class="card-icon">📁</span>
    <h3>Key file locations</h3>
    <p><em>"Auth logic lives in <code>/lib/auth</code>. Never touch <code>/legacy/*</code>."</em></p>
  </div>
  <div class="card">
    <span class="card-icon">📏</span>
    <h3>Coding conventions</h3>
    <p><em>"Use TypeScript strict mode. No default exports. All components in PascalCase."</em></p>
  </div>
  <div class="card">
    <span class="card-icon">🚫</span>
    <h3>Hard constraints</h3>
    <p><em>"Never modify the database schema directly. Always create a migration file first."</em></p>
  </div>
</div>

---

<!-- _class: cta -->

<div class="tag" style="justify-content:center;color:#0a0a0a;margin-bottom:20px;">Claude Code · /memory</div>

# Teach Claude once.<br>It remembers forever.

## Every convention you add saves a future prompt.

<p>Run <code>/memory</code> after every session where you established something new. Organic growth beats a stale setup.</p>

<div class="handle">Claude Code · Session Essentials</div>