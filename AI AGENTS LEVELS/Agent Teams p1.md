---
marp: true
theme: default
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,400;0,500;0,600;1,400&family=DM+Mono:wght@400;500&display=swap');

  :root {
    --amber: #d97706;
    --amber-light: #fffbeb;
    --amber-mid: #fde68a;
    --amber-dim: #b45309;
    --text: #1c1917;
    --muted: #78716c;
    --border: #e7e5e4;
    --white: #ffffff;
    --off-white: #fafaf9;
    --slate: #44403c;
  }

  section {
    font-family: 'DM Sans', sans-serif;
    background: var(--white);
    color: var(--text);
    padding: 52px 64px;
    font-size: 18px;
    line-height: 1.65;
  }

  section::after {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
  }

  h1 {
    font-family: 'DM Sans', sans-serif;
    font-size: 42px;
    font-weight: 600;
    color: var(--text);
    line-height: 1.15;
    margin-bottom: 0.4em;
    letter-spacing: -0.5px;
  }

  h2 {
    font-family: 'DM Sans', sans-serif;
    font-size: 27px;
    font-weight: 600;
    color: var(--text);
    border-bottom: 1.5px solid var(--border);
    padding-bottom: 10px;
    margin-bottom: 22px;
    letter-spacing: -0.3px;
  }

  h3 {
    font-family: 'DM Sans', sans-serif;
    font-size: 19px;
    font-weight: 500;
    color: var(--amber);
    margin-bottom: 8px;
  }

  p { color: var(--text); margin: 0.4em 0; }
  ul { padding-left: 1.4em; }
  li { margin-bottom: 10px; color: var(--text); }
  strong { color: var(--amber-dim); font-weight: 600; }

  code {
    font-family: 'DM Mono', monospace;
    background: var(--amber-light);
    color: var(--amber-dim);
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.87em;
  }

  blockquote {
    border-left: 3px solid var(--amber);
    background: var(--amber-light);
    padding: 16px 20px;
    margin: 20px 0;
    border-radius: 0 6px 6px 0;
    font-family: 'DM Mono', monospace;
    font-size: 0.82em;
    color: #92400e;
    line-height: 1.6;
  }

  blockquote p { color: #92400e; margin: 0; }

  /* ── Cover ── */
  section.cover {
    background: #1c1917;
    color: var(--white);
    display: flex;
    flex-direction: column;
    justify-content: center;
    position: relative;
    overflow: hidden;
  }

  section.cover::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
      radial-gradient(ellipse at 80% 20%, rgba(217,119,6,0.08) 0%, transparent 55%),
      radial-gradient(ellipse at 10% 85%, rgba(217,119,6,0.05) 0%, transparent 45%);
    pointer-events: none;
  }

  section.cover h1 { color: var(--white); font-size: 44px; letter-spacing: -0.8px; }
  section.cover h2 { color: #a8a29e; border-bottom-color: #44403c; font-size: 20px; font-weight: 400; letter-spacing: 0; }
  section.cover p  { color: #78716c; }
  section.cover strong { color: #fbbf24; }
  section.cover code { background: #292524; color: #fbbf24; border: 1px solid #44403c; }

  section.cover .series-badge {
    display: inline-block;
    background: #292524;
    color: #d97706;
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 500;
    padding: 5px 14px;
    border-radius: 4px;
    margin-bottom: 22px;
    letter-spacing: 0.1em;
    border: 1px solid #44403c;
    width: fit-content;
  }

  section.step { background: var(--off-white); }

  .highlight {
    background: var(--amber-light);
    border: 1px solid #fde68a;
    border-radius: 8px;
    padding: 16px 22px;
    margin: 16px 0;
  }

  .step-badge {
    display: inline-block;
    background: var(--text);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    padding: 4px 12px;
    border-radius: 3px;
    margin-bottom: 12px;
    letter-spacing: 0.08em;
  }

  section.final {
    background: #1c1917;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    position: relative;
    overflow: hidden;
  }

  section.final::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at 50% 50%, rgba(217,119,6,0.10) 0%, transparent 65%);
    pointer-events: none;
  }

  section.final h1 { color: white; font-size: 40px; letter-spacing: -0.5px; }
  section.final p  { color: #a8a29e; font-size: 18px; }
  section.final strong { color: #fbbf24; }
  section.final em { color: #a8a29e; }

  /* ── Matters grid ── */
  .matters-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .matters-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 14px 16px;
    display: flex;
    align-items: flex-start;
    gap: 13px;
  }

  .matters-card .mcc-icon { font-size: 24px; flex-shrink: 0; }
  .matters-card .mcc-title {
    font-weight: 600;
    font-size: 14px;
    color: var(--text);
    margin-bottom: 4px;
  }
  .matters-card .mcc-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.55;
  }

  /* ── Versus grid ── */
  .versus-grid {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    gap: 0;
    align-items: stretch;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 16px 0;
  }

  .vs-side { padding: 16px 18px; }
  .vs-side.l3   { background: var(--off-white); }
  .vs-side.l4   { background: #fffbeb; }

  .vs-side .vs-label {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.09em;
    margin-bottom: 8px;
  }

  .vs-side.l3 .vs-label { color: var(--muted); }
  .vs-side.l4 .vs-label { color: #92400e; }

  .vs-side .vs-title {
    font-weight: 700;
    font-size: 16.5px;
    color: var(--text);
    margin-bottom: 10px;
  }

  .vs-side .vs-item {
    font-size: 13px;
    color: var(--muted);
    padding: 5px 0;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: flex-start;
    gap: 8px;
  }

  .vs-side .vs-item:last-child { border-bottom: none; }
  .vs-side.l4 .vs-item { border-bottom-color: #fde68a; color: var(--text); }
  .vs-side .vs-item .vi-icon { flex-shrink: 0; }

  .vs-divider {
    background: var(--white);
    border-left: 1px solid var(--border);
    border-right: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 14px;
    font-weight: 700;
    font-size: 12px;
    color: var(--muted);
    font-family: 'DM Mono', monospace;
  }

  /* ── Cheat table ── */
  .cheat-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13.5px;
    margin: 12px 0;
  }

  .cheat-table th {
    background: var(--text);
    color: white;
    padding: 8px 14px;
    text-align: left;
    font-weight: 500;
    font-size: 11.5px;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.07em;
  }

  .cheat-table td {
    padding: 9px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
    font-size: 13px;
  }

  .cheat-table tr:last-child td { border-bottom: none; }
  .cheat-table tr:last-child td { border-bottom: 1px solid var(--border); }
  .cheat-table tr:nth-child(even) td { background: var(--off-white); }
  .cheat-table .mono {
    font-family: 'DM Mono', monospace;
    color: var(--amber-dim);
    font-size: 12px;
  }

  /* ── Department analogy ── */
  .dept-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 14px 0;
  }

  .dept-side {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .dept-side .ds-head {
    padding: 10px 16px;
    font-weight: 600;
    font-size: 13px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border);
  }

  .dept-side.company .ds-head { background: #f0f9ff;           color: #0c4a6e; border-color: #bae6fd; }
  .dept-side.agents  .ds-head { background: var(--amber-light); color: #92400e; border-color: #fde68a; }

  .dept-side .ds-body {
    padding: 14px 16px;
    background: var(--white);
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .ds-unit {
    border-radius: 8px;
    padding: 10px 12px;
    font-size: 12.5px;
    line-height: 1.5;
  }

  .ds-unit .dsu-name { font-weight: 700; font-size: 13px; display: block; color: var(--text); margin-bottom: 2px; }
  .ds-unit .dsu-role { font-size: 12px; color: var(--muted); }
  .ds-unit .dsu-members {
    margin-top: 6px;
    display: flex;
    flex-wrap: wrap;
    gap: 4px;
  }

  .ds-unit .dsu-tag {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    padding: 2px 7px;
    border-radius: 3px;
    font-weight: 500;
  }

  .dept-side.company .ds-unit { background: #f0f9ff; }
  .dept-side.agents  .ds-unit { background: var(--amber-light); }
  .dept-side.company .dsu-tag { background: #bae6fd; color: #0c4a6e; }
  .dept-side.agents  .dsu-tag { background: #fde68a; color: #92400e; }

  .ds-arrow { text-align: center; font-size: 11px; color: var(--muted); font-family: 'DM Mono', monospace; padding: 2px 10px; }

  /* ── Architecture diagram ── */
  .arch-diagram {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0;
    margin: 14px 0;
  }

  .arch-top {
    background: var(--text);
    color: white;
    border-radius: 8px;
    padding: 12px 32px;
    text-align: center;
    font-weight: 700;
    font-size: 14px;
    letter-spacing: -0.2px;
    position: relative;
  }

  .arch-top .at-sub {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: #a8a29e;
    font-weight: 400;
    margin-top: 2px;
    display: block;
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }

  .arch-connector {
    display: flex;
    gap: 48px;
    align-items: flex-start;
    position: relative;
    padding: 0 10px;
  }

  .arch-connector::before {
    content: '';
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    height: 22px;
    width: 2px;
    background: var(--border);
  }

  .arch-line-down {
    width: 100%;
    display: flex;
    justify-content: center;
    padding: 0;
    height: 22px;
    position: relative;
  }

  .arch-line-down::after {
    content: '';
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    height: 22px;
    width: 2px;
    background: var(--border);
  }

  .arch-branches {
    display: flex;
    gap: 16px;
    width: 100%;
    position: relative;
  }

  .arch-branches::before {
    content: '';
    position: absolute;
    top: 0;
    left: 10%;
    right: 10%;
    height: 2px;
    background: var(--border);
  }

  .arch-team {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0;
    position: relative;
  }

  .arch-team::before {
    content: '';
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    height: 18px;
    width: 2px;
    background: var(--border);
  }

  .arch-team-box {
    margin-top: 18px;
    border-radius: 8px;
    padding: 10px 14px;
    text-align: center;
    width: 100%;
  }

  .arch-team-box .atb-icon { font-size: 20px; margin-bottom: 4px; }
  .arch-team-box .atb-label {
    font-family: 'DM Mono', monospace;
    font-size: 9.5px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 3px;
  }
  .arch-team-box .atb-name { font-weight: 700; font-size: 13px; color: var(--text); }

  .arch-team-box.content { background: var(--amber-light); border: 1px solid #fde68a; }
  .arch-team-box.content .atb-label { color: #92400e; }
  .arch-team-box.engineering { background: #f0f9ff; border: 1px solid #bae6fd; }
  .arch-team-box.engineering .atb-label { color: #0369a1; }
  .arch-team-box.data { background: #f0fdf4; border: 1px solid #bbf7d0; }
  .arch-team-box.data .atb-label { color: #166534; }
  .arch-team-box.ops { background: #fdf4ff; border: 1px solid #e9d5ff; }
  .arch-team-box.ops .atb-label { color: #6b21a8; }

  .arch-specialists {
    margin-top: 10px;
    display: flex;
    flex-direction: column;
    gap: 4px;
    width: 100%;
  }

  .arch-spec-tag {
    border-radius: 5px;
    padding: 5px 8px;
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    font-weight: 500;
    text-align: center;
    color: var(--muted);
    background: var(--off-white);
    border: 1px solid var(--border);
  }

  /* ── Scale signals stack ── */
  .signal-stack {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .ss-row {
    display: grid;
    grid-template-columns: 200px 1fr auto;
    align-items: stretch;
    border-bottom: 1px solid var(--border);
  }

  .ss-row:last-child { border-bottom: none; }

  .ss-row .ssr-signal {
    padding: 11px 14px;
    font-weight: 600;
    font-size: 12.5px;
    color: var(--text);
    background: var(--off-white);
    border-right: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 8px;
    line-height: 1.4;
  }

  .ss-row .ssr-desc {
    padding: 11px 14px;
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.6;
    display: flex;
    align-items: center;
  }

  .ss-row .ssr-verdict {
    padding: 11px 14px;
    border-left: 1px solid var(--border);
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    display: flex;
    align-items: center;
    white-space: nowrap;
  }

  .ss-row.stay   .ssr-verdict { background: #f0fdf4;           color: #166534; }
  .ss-row.team   .ssr-verdict { background: var(--amber-light); color: #92400e; }
  .ss-row.danger .ssr-verdict { background: #fef2f2;            color: #991b1b; }

  /* ── Team card grid ── */
  .team-card-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin: 14px 0;
  }

  .team-card {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .team-card .tc-head {
    padding: 11px 16px;
    font-weight: 700;
    font-size: 14px;
    display: flex;
    align-items: center;
    gap: 10px;
    border-bottom: 1px solid var(--border);
  }

  .team-card.content     .tc-head { background: var(--amber-light); color: #92400e; border-color: #fde68a; }
  .team-card.engineering .tc-head { background: #f0f9ff;            color: #0c4a6e; border-color: #bae6fd; }

  .team-card .tc-body {
    padding: 13px 16px;
    background: var(--white);
    display: flex;
    flex-direction: column;
    gap: 7px;
  }

  .tc-row {
    display: flex;
    align-items: flex-start;
    gap: 9px;
    font-size: 12.5px;
    line-height: 1.5;
    color: var(--text);
  }

  .tc-row .tcr-tag {
    font-family: 'DM Mono', monospace;
    font-size: 9.5px;
    font-weight: 700;
    padding: 2px 6px;
    border-radius: 3px;
    flex-shrink: 0;
    margin-top: 1px;
  }

  .content     .tcr-tag { background: #fde68a; color: #92400e; }
  .engineering .tcr-tag { background: #bae6fd; color: #0c4a6e; }

  .tc-row .tcr-text { color: var(--muted); font-size: 12px; }

  .team-card .tc-footer {
    padding: 9px 16px;
    border-top: 1px solid var(--border);
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
  }

  .team-card.content     .tc-footer { background: var(--amber-light); color: #92400e; }
  .team-card.engineering .tc-footer { background: #f0f9ff;            color: #0369a1; }
---

<!-- _class: cover -->

<div class="series-badge">AGENT TEAMS · LEVEL 4 — PART 1 OF 4</div>

# The Team Mental Model
## From multi-agent systems to autonomous teams

&nbsp;

**At Level 3, one orchestrator routes between specialists.** At Level 4, one orchestrator routes between teams — each one a self-contained system with its own orchestrator, its own specialists, and its own scope.

`teams` · `departments` · `top-level orchestrator` · `team scope` · `autonomous workflow`

---

## Multi-Agent vs. Agent Teams — The Core Difference

A multi-agent system has one orchestrator with a flat list of specialists. An agent team system has one top-level orchestrator with a structured set of teams — each team is its own Level 3 system.

<div class="versus-grid">
  <div class="vs-side l3">
    <div class="vs-label">🧭 &nbsp;Level 3 — one orchestrator</div>
    <div class="vs-title">One entry point. Many specialists.</div>
    <div class="vs-item"><span class="vi-icon">→</span> Top-level orchestrator routes to specialists</div>
    <div class="vs-item"><span class="vi-icon">→</span> All specialists report back to one orchestrator</div>
    <div class="vs-item"><span class="vi-icon">→</span> Works well for one domain — content, data, or code</div>
    <div class="vs-item"><span class="vi-icon">→</span> Starts to strain when domains are fundamentally different</div>
    <div class="vs-item"><span class="vi-icon">→</span> Orchestrator becomes a routing bottleneck at scale</div>
  </div>
  <div class="vs-divider">vs</div>
  <div class="vs-side l4">
    <div class="vs-label">🏢 &nbsp;Level 4 — teams of agents</div>
    <div class="vs-title">One entry point. Many teams.</div>
    <div class="vs-item"><span class="vi-icon">→</span> Top-level orchestrator routes to team orchestrators</div>
    <div class="vs-item"><span class="vi-icon">→</span> Each team manages its own specialists internally</div>
    <div class="vs-item"><span class="vi-icon">→</span> Each team owns one domain entirely</div>
    <div class="vs-item"><span class="vi-icon">→</span> Teams are independently deployable and testable</div>
    <div class="vs-item"><span class="vi-icon">→</span> Adding a new domain means adding a new team, not new specialists</div>
  </div>
</div>

<div class="highlight">

**Analogy:** Level 3 is a manager with ten direct reports. Level 4 is a director with four department heads — each one managing their own team. The director doesn't know every individual worker. They know the department heads.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## What Changes at Team Scale vs. Multi-Agent

The jump from Level 3 to Level 4 is not about adding more agents. It's about introducing a new layer of abstraction — the team — between the top-level orchestrator and the specialists who do the work.

<div class="matters-grid">
  <div class="matters-card">
    <div class="mcc-icon">🔭</div>
    <div>
      <div class="mcc-title">The top-level orchestrator changes its resolution</div>
      <div class="mcc-desc">At Level 3, the orchestrator knows about individual specialists — research, writer, QA. At Level 4, it knows only about teams — content team, engineering team. It routes at team granularity, not agent granularity.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">📦</div>
    <div>
      <div class="mcc-title">Teams have their own internal orchestration</div>
      <div class="mcc-desc">Each team is a complete Level 3 system — its own team orchestrator, its own specialists, its own contracts. The top-level orchestrator hands a task to the content team. The content team figures out how to do it. The top level doesn't need to know.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🧱</div>
    <div>
      <div class="mcc-title">Domains stay separated by design</div>
      <div class="mcc-desc">At Level 3 with many specialists, domain boundaries blur — the orchestrator's system prompt becomes a long list of overlapping capabilities. Teams enforce hard domain separation. The content team handles content. The engineering team handles code. No overlap.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">⚙️</div>
    <div>
      <div class="mcc-title">Failure isolation improves dramatically</div>
      <div class="mcc-desc">When a specialist fails in a Level 3 system, the orchestrator catches it. When a specialist fails in a Level 4 system, the team orchestrator catches it — before the top level is ever involved. Teams contain their own failures.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## The Departments Analogy

Companies solved the coordination-at-scale problem by creating departments. Each department has a manager, a defined scope, and a set of specialists. Leadership communicates with department managers — not with every individual contributor.

<div class="dept-compare">
  <div class="dept-side company">
    <div class="ds-head">🏢 &nbsp;A company with departments</div>
    <div class="ds-body">
      <div class="ds-unit">
        <span class="dsu-name">Marketing</span>
        <span class="dsu-role">Owns brand, content, and campaigns</span>
        <div class="dsu-members">
          <span class="dsu-tag">copywriter</span>
          <span class="dsu-tag">SEO analyst</span>
          <span class="dsu-tag">designer</span>
        </div>
      </div>
      <div class="ds-arrow">↓ department report</div>
      <div class="ds-unit">
        <span class="dsu-name">Engineering</span>
        <span class="dsu-role">Owns all code, infra, and deployment</span>
        <div class="dsu-members">
          <span class="dsu-tag">backend dev</span>
          <span class="dsu-tag">QA engineer</span>
          <span class="dsu-tag">devops</span>
        </div>
      </div>
      <div class="ds-arrow">↓ department report</div>
      <div class="ds-unit">
        <span class="dsu-name">Data</span>
        <span class="dsu-role">Owns analytics, reporting, and insights</span>
        <div class="dsu-members">
          <span class="dsu-tag">analyst</span>
          <span class="dsu-tag">data engineer</span>
          <span class="dsu-tag">BI lead</span>
        </div>
      </div>
    </div>
  </div>
  <div class="dept-side agents">
    <div class="ds-head">🤖 &nbsp;An agent system with teams</div>
    <div class="ds-body">
      <div class="ds-unit">
        <span class="dsu-name">Content Team</span>
        <span class="dsu-role">Owns research, writing, editing, QA</span>
        <div class="dsu-members">
          <span class="dsu-tag">research agent</span>
          <span class="dsu-tag">writer agent</span>
          <span class="dsu-tag">qa agent</span>
        </div>
      </div>
      <div class="ds-arrow">↓ team response envelope</div>
      <div class="ds-unit">
        <span class="dsu-name">Engineering Team</span>
        <span class="dsu-role">Owns code gen, testing, and deployment</span>
        <div class="dsu-members">
          <span class="dsu-tag">coder agent</span>
          <span class="dsu-tag">test agent</span>
          <span class="dsu-tag">reviewer agent</span>
        </div>
      </div>
      <div class="ds-arrow">↓ team response envelope</div>
      <div class="ds-unit">
        <span class="dsu-name">Data Team</span>
        <span class="dsu-role">Owns analysis, cleaning, and reporting</span>
        <div class="dsu-members">
          <span class="dsu-tag">analyst agent</span>
          <span class="dsu-tag">cleaner agent</span>
          <span class="dsu-tag">reporter agent</span>
        </div>
      </div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Top-Level Orchestrator — Routing Between Teams, Not Agents

The top-level orchestrator at Level 4 has one job: decide which team handles this request. It never interacts with specialists. It never knows what the content team's internal pipeline looks like. It routes to team orchestrators and reads team-level responses.

<div class="arch-diagram">
  <div class="arch-top">
    🌐 Top-Level Orchestrator
    <span class="at-sub">parse intent → select team → return team response</span>
  </div>
  <div class="arch-line-down"></div>
  <div class="arch-branches">
    <div class="arch-team">
      <div class="arch-team-box content">
        <div class="atb-icon">✍️</div>
        <div class="atb-label">Content Team</div>
        <div class="atb-name">Team Orchestrator</div>
      </div>
      <div class="arch-specialists">
        <div class="arch-spec-tag">research agent</div>
        <div class="arch-spec-tag">writer agent</div>
        <div class="arch-spec-tag">editor agent</div>
        <div class="arch-spec-tag">qa agent</div>
      </div>
    </div>
    <div class="arch-team">
      <div class="arch-team-box engineering">
        <div class="atb-icon">⚙️</div>
        <div class="atb-label">Engineering Team</div>
        <div class="atb-name">Team Orchestrator</div>
      </div>
      <div class="arch-specialists">
        <div class="arch-spec-tag">coder agent</div>
        <div class="arch-spec-tag">test agent</div>
        <div class="arch-spec-tag">reviewer agent</div>
        <div class="arch-spec-tag">deploy agent</div>
      </div>
    </div>
    <div class="arch-team">
      <div class="arch-team-box data">
        <div class="atb-icon">📊</div>
        <div class="atb-label">Data Team</div>
        <div class="atb-name">Team Orchestrator</div>
      </div>
      <div class="arch-specialists">
        <div class="arch-spec-tag">analyst agent</div>
        <div class="arch-spec-tag">cleaner agent</div>
        <div class="arch-spec-tag">reporter agent</div>
      </div>
    </div>
    <div class="arch-team">
      <div class="arch-team-box ops">
        <div class="atb-icon">🔧</div>
        <div class="atb-label">Ops Team</div>
        <div class="atb-name">Team Orchestrator</div>
      </div>
      <div class="arch-specialists">
        <div class="arch-spec-tag">monitor agent</div>
        <div class="arch-spec-tag">alert agent</div>
        <div class="arch-spec-tag">triage agent</div>
      </div>
    </div>
  </div>
</div>

<div class="highlight">

**The top-level orchestrator's registry maps team names to team orchestrators** — not to specialist functions. <code>TEAM_REGISTRY = {"content_team": run_content_team, "engineering_team": run_engineering_team}</code>. The internal structure of each team is completely invisible to the top level.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03 — CONTINUED</div>

## What the Top-Level Orchestrator Knows vs. Doesn't Know

The cleanest way to understand the top-level orchestrator's role is by listing what it is and is not allowed to know. Every piece of knowledge it holds is a coupling — and coupling at scale is how systems become unmaintainable.

<table class="cheat-table">
  <thead>
    <tr><th>The top-level orchestrator knows</th><th>The top-level orchestrator does NOT know</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>The names of the available teams and their domain descriptions</td>
      <td>Which specialists exist inside any team</td>
    </tr>
    <tr>
      <td>The input params each team accepts at its entry point</td>
      <td>How the team orchestrator sequences its specialists</td>
    </tr>
    <tr>
      <td>The shape of the <code>TeamResponse</code> envelope each team returns</td>
      <td>Which artifacts the team produces internally</td>
    </tr>
    <tr>
      <td>Whether a team's response was <code>ok</code>, <code>error</code>, or <code>flagged</code></td>
      <td>Which specialist inside the team caused a failure</td>
    </tr>
    <tr>
      <td>How to merge results from two teams when a task spans domains</td>
      <td>Any implementation detail of team-internal routing</td>
    </tr>
  </tbody>
</table>

<div class="highlight">

**Rule:** If you find yourself adding specialist names to the top-level orchestrator's system prompt, you've broken the abstraction. The top level talks to teams. Teams talk to specialists. That boundary is non-negotiable.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Team Architecture — Content Team vs. Engineering Team

Each team is a self-contained Level 3 system. It has a team orchestrator, a set of specialists, its own contracts, and its own routing logic. Here is what two real teams look like side by side.

<div class="team-card-grid">
  <div class="team-card content">
    <div class="tc-head">✍️ &nbsp;Content Team</div>
    <div class="tc-body">
      <div class="tc-row">
        <span class="tcr-tag">INPUT</span>
        <span class="tcr-text">topic, audience, format, word_count — passed from top-level routing decision params</span>
      </div>
      <div class="tc-row">
        <span class="tcr-tag">ORCH</span>
        <span class="tcr-text">Team orchestrator sequences: research → outline → write → edit → qa. May short-circuit if format is "brief".</span>
      </div>
      <div class="tc-row">
        <span class="tcr-tag">SPEC</span>
        <span class="tcr-text">research_agent, outline_agent, writer_agent, editor_agent, qa_agent — each with its own Level 2 contract</span>
      </div>
      <div class="tc-row">
        <span class="tcr-tag">STATE</span>
        <span class="tcr-text">Team-scoped RunState: run_id, pipeline sequence, per-stage artifacts, qa verdict</span>
      </div>
      <div class="tc-row">
        <span class="tcr-tag">OUTPUT</span>
        <span class="tcr-text">TeamResponse(status, payload={"final_draft": str, "qa_report": dict}, meta)</span>
      </div>
    </div>
    <div class="tc-footer">domain: written content · entry: run_content_team()</div>
  </div>
  <div class="team-card engineering">
    <div class="tc-head">⚙️ &nbsp;Engineering Team</div>
    <div class="tc-body">
      <div class="tc-row">
        <span class="tcr-tag">INPUT</span>
        <span class="tcr-text">task_description, language, test_required, deploy_target — passed from top-level routing decision params</span>
      </div>
      <div class="tc-row">
        <span class="tcr-tag">ORCH</span>
        <span class="tcr-text">Team orchestrator sequences: plan → code → test → review → (optional) deploy. Halts on test failure.</span>
      </div>
      <div class="tc-row">
        <span class="tcr-tag">SPEC</span>
        <span class="tcr-text">planner_agent, coder_agent, test_agent, reviewer_agent, deploy_agent — each with its own Level 2 contract</span>
      </div>
      <div class="tc-row">
        <span class="tcr-tag">STATE</span>
        <span class="tcr-text">Team-scoped RunState: run_id, code artifacts, test results, review verdict, deploy status</span>
      </div>
      <div class="tc-row">
        <span class="tcr-tag">OUTPUT</span>
        <span class="tcr-text">TeamResponse(status, payload={"code": str, "test_report": dict, "review": dict}, meta)</span>
      </div>
    </div>
    <div class="tc-footer">domain: code & deployment · entry: run_engineering_team()</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04 — CONTINUED</div>

## The Team Response Envelope

Just as specialists return `SpecialistResponse`, teams return `TeamResponse`. The top-level orchestrator reads only the envelope — never the internal artifacts the team produced along the way.

<table class="cheat-table">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Purpose</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="mono">status</span></td>
      <td><span class="mono">"ok" | "error" | "flagged" | "partial"</span></td>
      <td>Machine-readable result. The top-level orchestrator branches on this — never on payload content.</td>
    </tr>
    <tr>
      <td><span class="mono">team</span></td>
      <td><span class="mono">str</span></td>
      <td>Which team produced this response. Echoed back so the top level can log it without inspecting the payload.</td>
    </tr>
    <tr>
      <td><span class="mono">payload</span></td>
      <td>team-specific object</td>
      <td>The team's final deliverable. Shape varies by team — but the wrapper is always the same.</td>
    </tr>
    <tr>
      <td><span class="mono">error</span></td>
      <td><span class="mono">str | None</span></td>
      <td>Human-readable error message. Present only when status is <code>error</code>. Never exposes internal specialist failures.</td>
    </tr>
    <tr>
      <td><span class="mono">meta</span></td>
      <td>dict</td>
      <td>Aggregated diagnostics: total tokens, total duration, stages completed. The top level logs these — never routes on them.</td>
    </tr>
  </tbody>
</table>

<div class="highlight">

**<code>partial</code> is a new status at Level 4.** It means the team completed some but not all of its internal pipeline — perhaps QA flagged issues the team couldn't auto-resolve. The top level receives the partial payload and decides whether to surface it to the user, retry, or escalate. The team doesn't make that call — it just reports the partial result faithfully.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## When You Actually Need Teams vs. When Level 3 Is Enough

Teams add architectural complexity — a new layer of orchestration, new envelope types, new routing logic. That complexity only pays off in specific situations. Here are the precise triggers.

<div class="signal-stack">
  <div class="ss-row stay">
    <div class="ssr-signal">📋 &nbsp;One domain, many specialists</div>
    <div class="ssr-desc">All your specialists work on the same kind of task — everything is content, or everything is data. A single orchestrator with a flat specialist list is still the right shape at this scale.</div>
    <div class="ssr-verdict">→ stay at L3</div>
  </div>
  <div class="ss-row stay">
    <div class="ssr-signal">🔢 &nbsp;Fewer than 8 specialists total</div>
    <div class="ssr-desc">A registry of 6–8 specialists is manageable in a single orchestrator prompt and a flat registry. The routing table fits on one screen. Adding a team layer would add complexity with no real benefit.</div>
    <div class="ssr-verdict">→ stay at L3</div>
  </div>
  <div class="ss-row team">
    <div class="ssr-signal">🌐 &nbsp;Fundamentally different domains</div>
    <div class="ssr-desc">The system handles both content creation and code deployment. These domains have different specialists, different artifacts, different failure modes, and different quality criteria. They belong in separate teams.</div>
    <div class="ssr-verdict">→ add teams</div>
  </div>
  <div class="ss-row team">
    <div class="ssr-signal">📈 &nbsp;Orchestrator prompt keeps growing</div>
    <div class="ssr-desc">Every new specialist type requires a new section in the orchestrator system prompt. The prompt is now 600+ words and still can't correctly distinguish between overlapping capabilities. This is domain confusion — a team boundary would have prevented it.</div>
    <div class="ssr-verdict">→ add teams</div>
  </div>
  <div class="ss-row team">
    <div class="ssr-signal">🚀 &nbsp;Teams need independent deployment</div>
    <div class="ssr-desc">The engineering team needs to update its coder agent without touching the content team's specialists. At Level 3, all specialists share one codebase and one deployment cycle. Teams make independent deployment natural.</div>
    <div class="ssr-verdict">→ add teams</div>
  </div>
  <div class="ss-row danger">
    <div class="ssr-signal">❓ &nbsp;Teams because it feels more advanced</div>
    <div class="ssr-desc">Level 4 is not a prestige upgrade. If Level 3 is working and your system handles one clear domain well, adding teams introduces overhead with no structural benefit. Complexity without necessity is technical debt.</div>
    <div class="ssr-verdict">→ don't upgrade</div>
  </div>
</div>

---

## Quick Reference — Level 4 Vocabulary

The new terms that appear throughout the rest of this series, decoded.

<table class="cheat-table">
  <thead>
    <tr><th>Term</th><th>What it means</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="mono">Agent team</span></td>
      <td>A self-contained Level 3 system (orchestrator + specialists) that owns one domain and exposes a single entry point to the top level.</td>
    </tr>
    <tr>
      <td><span class="mono">Top-level orchestrator</span></td>
      <td>The single entry point for the whole system. Routes to team orchestrators — never directly to specialists.</td>
    </tr>
    <tr>
      <td><span class="mono">Team orchestrator</span></td>
      <td>The Level 3 orchestrator inside each team. Manages that team's specialists, state, and internal routing. Invisible to the top level.</td>
    </tr>
    <tr>
      <td><span class="mono">Team registry</span></td>
      <td>The top-level equivalent of the pipeline registry — maps team name strings to team entry-point functions.</td>
    </tr>
    <tr>
      <td><span class="mono">TeamResponse</span></td>
      <td>The standard envelope a team returns to the top-level orchestrator. Fields: status, team, payload, error, meta.</td>
    </tr>
    <tr>
      <td><span class="mono">partial status</span></td>
      <td>A team completed some but not all of its pipeline. Returns the partial payload for the top level to handle.</td>
    </tr>
    <tr>
      <td><span class="mono">Domain separation</span></td>
      <td>The hard rule that no team handles tasks outside its defined domain. Teams own domains; they don't share them.</td>
    </tr>
  </tbody>
</table>

---

<!-- _class: final -->

# The orchestrator routes to teams. Teams route to specialists. Specialists do the work.

&nbsp;

*Each layer knows only the layer below it. Never two layers down.*

&nbsp;

Next: **Part 2 — Designing the Team Orchestrators.**

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*