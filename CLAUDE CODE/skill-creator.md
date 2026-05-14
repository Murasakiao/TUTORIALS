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
  .tag.purple{color:var(--purple);}.tag.purple::before{background:var(--purple);}
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
  section::after{font-family:'DM Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:1px;content:'CLAUDE CODE · /skill-creator · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);position:absolute;bottom:20px;right:40px;}
---

<!-- _class: cover -->

<div class="tag purple">Claude Code · Command 16 · Skill</div>

# `/skill-creator`

Build your own slash commands — for any task you repeat.

*Describe once. Reuse forever. Share with your team.*

---

<div class="header-row">
  <span class="page-num">— what it is —</span>
  <span class="page-label">the meta-skill</span>
</div>

## What `/skill-creator` does

Guides you through creating a new custom skill — your own reusable slash command. You describe a task you do repeatedly, and Claude builds a complete `SKILL.md` file with the correct frontmatter, trigger description, behavioral instructions, and examples.

<div class="cards">
  <div class="card">
    <span class="card-icon">🛠️</span>
    <h3>Guided creation flow</h3>
    <p>Claude asks you about the task, its triggers, its constraints, and its output format — then writes the SKILL.md from your answers.</p>
  </div>
  <div class="card">
    <span class="card-icon">📁</span>
    <h3>Saves in the right place</h3>
    <p>Project skills → <code>.claude/skills/</code>. Personal skills → <code>~/.claude/skills/</code>. Active on the next session automatically.</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">the rule</div>
  <p>Any task you've typed out manually <strong>three times</strong> belongs in a skill. That's your signal to run <code>/skill-creator</code>.</p>
</div>

---

<div class="header-row">
  <span class="page-num">— what a skill contains —</span>
  <span class="page-label">the four parts</span>
</div>

## What /skill-creator builds for you

<div class="cards-col">
  <div class="card-row">
    <span class="card-row-icon">🏷️</span>
    <div class="card-row-body">
      <h3>Trigger description</h3>
      <p>The text Claude reads to decide when to activate this skill. Precise triggers mean consistent activation.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">📋</span>
    <div class="card-row-body">
      <h3>Behavioral instructions</h3>
      <p>Step-by-step guidance on exactly how Claude should execute the task — what to do, what to avoid, what to produce.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">🚫</span>
    <div class="card-row-body">
      <h3>Constraints</h3>
      <p>Hard limits the skill must never cross — format rules, scope limits, prohibited actions.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">💡</span>
    <div class="card-row-body">
      <h3>Examples</h3>
      <p>One or two worked examples of ideal skill output — the most reliable way to anchor Claude's behavior.</p>
    </div>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— what to build —</span>
  <span class="page-label">good skill candidates</span>
</div>

## Tasks worth turning into skills

<div class="list">
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>PR description generator</strong> — reads the diff and writes a structured PR description every time</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>Daily standup writer</strong> — reads git log and generates a standup summary in your team's format</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>Component scaffolder</strong> — generates a new React/Vue component with your team's exact conventions pre-applied</span>
  </div>
  <div class="list-item">
    <span class="list-num">✅</span>
    <span class="list-text"><strong>Release notes generator</strong> — turns a list of merged PRs into formatted release notes for your changelog</span>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— tips —</span>
  <span class="page-label">build skills that last</span>
</div>

## Building skills that work consistently

<div class="cards">
  <div class="card">
    <span class="card-icon">🎯</span>
    <h3>One skill, one job</h3>
    <p>Skills with narrow scope activate reliably. Skills that try to do multiple things activate inconsistently — or not at all.</p>
  </div>
  <div class="card">
    <span class="card-icon">🔬</span>
    <h3>Test with five prompts</h3>
    <p>After creating: 3 prompts that should trigger it, 2 that should not. Fix the trigger description until all five behave correctly.</p>
  </div>
  <div class="card">
    <span class="card-icon">👥</span>
    <h3>Commit project skills to git</h3>
    <p>Skills in <code>.claude/skills/</code> are shareable. Every teammate gets the same reusable commands — one build, whole team benefits.</p>
  </div>
  <div class="card">
    <span class="card-icon">🔄</span>
    <h3>Iterate after real use</h3>
    <p>The first version won't be perfect. Use it for a week, note where it fails, then edit the SKILL.md and re-test.</p>
  </div>
</div>

---

<!-- _class: cta -->

<div class="tag" style="justify-content:center;color:#0a0a0a;margin-bottom:20px;">Claude Code · /skill-creator</div>

# What did you type<br>three times this week?

## That's your first skill.

<p>Run <code>/skill-creator</code>, describe the task, let Claude build the playbook. Done once. Works forever.</p>

<div class="handle">Claude Code · Build Your Own</div>