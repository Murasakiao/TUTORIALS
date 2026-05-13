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
  section::after{font-family:'DM Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:1px;content:'CLAUDE CODE · /init · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);position:absolute;bottom:20px;right:40px;}
---

<!-- _class: cover -->

<div class="tag">Claude Code · Command 01</div>

# `/init`

Set up your project once. Never re-explain it again.

*The first command you run in any new repo.*

---

<div class="header-row">
  <span class="page-num">— what it is —</span>
  <span class="page-label">your project's permanent memory</span>
</div>

## What `/init` does

Run it once when you open a project for the first time. Claude scans your codebase and generates a `CLAUDE.md` file — a permanent project brief that gets loaded at the start of every future session.

<div class="cards-col">
  <div class="card-row">
    <span class="card-row-icon">🔍</span>
    <div class="card-row-body">
      <h3>Scans your repo automatically</h3>
      <p>Claude reads your files, folders, package configs, and existing docs to understand your stack.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">📄</span>
    <div class="card-row-body">
      <h3>Generates CLAUDE.md</h3>
      <p>A markdown file at your project root capturing stack, conventions, build commands, and key paths.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">🔁</span>
    <div class="card-row-body">
      <h3>Loaded every session automatically</h3>
      <p>Claude reads CLAUDE.md before your first message in every new session — no re-explaining needed.</p>
    </div>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— how it works —</span>
  <span class="page-label">two modes</span>
</div>

## Running `/init`

<div class="compare">
  <div class="compare-col">
    <div class="compare-label">Standard</div>
    <h3>Just type <code>/init</code></h3>
    <p>Claude scans and generates CLAUDE.md silently. Fast, automatic, no prompts. Best for existing projects.</p>
  </div>
  <div class="compare-col good">
    <div class="compare-label good">Interactive</div>
    <h3>Set <code>CLAUDE_CODE_NEW_INIT=1</code></h3>
    <p>Guided setup that also walks through skills, hooks, MCP servers, and personal memory files. Best for new projects.</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">what goes into CLAUDE.md</div>
  <p>Tech stack · build & test commands · folder structure · coding conventions · things Claude must never change</p>
</div>

---

<div class="header-row">
  <span class="page-num">— when to use it —</span>
  <span class="page-label">and when to re-run it</span>
</div>

## When to run `/init`

<div class="list">
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>First session in any repo</strong> — run it before your first real task, always</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>Inherited or unfamiliar codebases</strong> — let Claude map it before you start asking questions</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>After major refactors</strong> — re-run to update CLAUDE.md when the stack or structure changes significantly</span>
  </div>
  <div class="list-item">
    <span class="list-num">🚫</span>
    <span class="list-text"><strong>Don't re-run for small changes</strong> — use <code>/memory</code> to edit CLAUDE.md directly for minor updates</span>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— pro tips —</span>
  <span class="page-label">get more out of it</span>
</div>

## Make `/init` work harder

<div class="cards">
  <div class="card">
    <span class="card-icon">✏️</span>
    <h3>Edit after generating</h3>
    <p>Claude's first draft is a starting point. Add constraints, team conventions, and "never touch" rules manually.</p>
  </div>
  <div class="card">
    <span class="card-icon">📌</span>
    <h3>Add explicit constraints</h3>
    <p>Write what Claude must never do: <em>"Never modify the legacy auth module"</em> or <em>"Always use bun, not npm."</em></p>
  </div>
  <div class="card">
    <span class="card-icon">🔄</span>
    <h3>Keep it updated</h3>
    <p>Use <code>/memory</code> to add new conventions as you work. Treat CLAUDE.md as a living document, not a one-time artifact.</p>
  </div>
  <div class="card">
    <span class="card-icon">👥</span>
    <h3>Commit it to git</h3>
    <p>CLAUDE.md in version control means every teammate and every future Claude session starts with the same context.</p>
  </div>
</div>

---

<!-- _class: cta -->

<div class="tag" style="justify-content:center;color:#0a0a0a;margin-bottom:20px;">Claude Code · /init</div>

# First command.<br>Every project.

## Run it before anything else.

<p>The 30 seconds you spend on <code>/init</code> saves minutes of re-explaining on every future session.</p>

<div class="handle">Claude Code · Session Essentials</div>