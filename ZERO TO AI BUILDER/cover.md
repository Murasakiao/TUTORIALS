---
marp: true
theme: default
paginate: false
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&family=DM+Mono:wght@400;500&display=swap');

  section {
    font-family: 'DM Sans', sans-serif;
    background: #080d1a;
    color: #f0f4ff;
    padding: 40px 52px 32px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  /* ── Top bar ── */
  .top-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 30px;
  }
  .brand {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    font-weight: 500;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #2563eb;
  }
  .pill {
    font-family: 'DM Mono', monospace;
    font-size: 0.55rem;
    font-weight: 500;
    letter-spacing: 0.08em;
    color: #34d399;
    background: #0d2a1f;
    border: 1px solid #16a34a44;
    border-radius: 99px;
    padding: 3px 12px;
  }

  /* ── Title ── */
  .title-block {
    margin-bottom: 30px;
  }
  .title-block h1 {
    font-size: 2.15rem;
    font-weight: 800;
    line-height: 1.08;
    letter-spacing: -0.02em;
    color: #fff;
    margin: 0 0 8px;
  }
  .title-block h1 em {
    font-style: normal;
    color: #2563eb;
  }
  .title-block p {
    font-size: 0.7rem;
    color: #475569;
    margin: 0;
  }

  /* ── Section label ── */
  .section-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.5rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: #2d3f5a;
    margin-bottom: 9px;
  }

  /* ── Phase grid ── */
  .phase-grid {
    display: grid;
    grid-template-columns: repeat(8, 1fr);
    gap: 7px;
    margin-bottom: auto;
  }
  .phase-card {
    background: #0d1525;
    border: 1px solid #1a2740;
    border-radius: 10px;
    padding: 13px 8px 11px;
    text-align: center;
  }
  .phase-card.wip {
    border-color: #92400e44;
  }
  .phase-num {
    font-family: 'DM Mono', monospace;
    font-size: 0.46rem;
    color: #2d3f5a;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 9px;
  }
  .phase-icon {
    font-size: 1.4rem;
    display: block;
    margin-bottom: 8px;
    line-height: 1;
  }
  .phase-title {
    font-size: 0.58rem;
    font-weight: 700;
    color: #94a3b8;
    line-height: 1.3;
    margin-bottom: 6px;
  }
  .phase-count {
    font-family: 'DM Mono', monospace;
    font-size: 0.5rem;
    color: #2d3f5a;
  }
  .phase-count b { color: #2563eb; }
  .phase-count b.warn { color: #f59e0b; }

  /* ── Footer ── */
  .footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-top: 1px solid #1a2740;
    padding-top: 18px;
    margin-top: 22px;
  }
  .footer-stat .num {
    font-family: 'DM Mono', monospace;
    font-size: 1.1rem;
    font-weight: 700;
    color: #2563eb;
    line-height: 1;
  }
  .footer-stat .num.green { color: #34d399; }
  .footer-stat .lbl {
    font-size: 0.5rem;
    color: #2d3f5a;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-top: 3px;
  }
  .footer-divider {
    width: 1px;
    height: 26px;
    background: #1a2740;
  }
  .footer-note {
    font-size: 0.56rem;
    color: #2d3f5a;
    text-align: right;
    line-height: 1.6;
  }

  section::after { display: none; }
  h1, h2, h3, p, ul, li { margin: 0; padding: 0; }
---

<div class="top-bar">
  <span class="brand">Zero to AI Builder</span>
  <span class="pill">● 100% complete — 56 of 56 tutorials done</span>
</div>

<div class="title-block">
  <h1>From <em>Zero</em> to Building<br>AI-Powered Apps</h1>
  <p>A complete beginner curriculum · No prior coding experience needed · MARP slide decks · Sold on Gumroad</p>
</div>

<div class="section-label">8-Phase Curriculum</div>

<div class="phase-grid">
  <div class="phase-card">
    <div class="phase-num">Phase 1</div>
    <span class="phase-icon">🖥️</span>
    <div class="phase-title">Foundation</div>
    <div class="phase-count"><b>6</b> tutorials</div>
  </div>
  <div class="phase-card">
    <div class="phase-num">Phase 2</div>
    <span class="phase-icon">🌿</span>
    <div class="phase-title">Version Control</div>
    <div class="phase-count"><b>5</b> tutorials</div>
  </div>
  <div class="phase-card wip">
    <div class="phase-num">Phase 3</div>
    <span class="phase-icon">🌐</span>
    <div class="phase-title">Web Dev</div>
    <div class="phase-count"><b>8</b> tutorials</div>
  </div>
  <div class="phase-card">
    <div class="phase-num">Phase 4</div>
    <span class="phase-icon">🐍</span>
    <div class="phase-title">Python</div>
    <div class="phase-count"><b>11</b> tutorials</div>
  </div>
  <div class="phase-card">
    <div class="phase-num">Phase 5</div>
    <span class="phase-icon">💬</span>
    <div class="phase-title">AI Prompting</div>
    <div class="phase-count"><b>5</b> tutorials</div>
  </div>
  <div class="phase-card">
    <div class="phase-num">Phase 6</div>
    <span class="phase-icon">🤖</span>
    <div class="phase-title">AI Agents</div>
    <div class="phase-count"><b>5</b> tutorials</div>
  </div>
  <div class="phase-card">
    <div class="phase-num">Phase 7</div>
    <span class="phase-icon">⚡</span>
    <div class="phase-title">Agentic Coding</div>
    <div class="phase-count"><b>5</b> tutorials</div>
  </div>
  <div class="phase-card">
    <div class="phase-num">Phase 8</div>
    <span class="phase-icon">🔄</span>
    <div class="phase-title">Automations</div>
    <div class="phase-count"><b>5</b> tutorials</div>
  </div>
</div>

<div class="footer">
  <div class="footer-stat">
    <div class="num">56</div>
    <div class="lbl">Tutorials</div>
  </div>
  <div class="footer-divider"></div>
  <div class="footer-stat">
    <div class="num">8</div>
    <div class="lbl">Phases</div>
  </div>
  <div class="footer-divider"></div>
  <div class="footer-stat">
    <div class="num">+10</div>
    <div class="lbl">Bonus</div>
  </div>
  <div class="footer-divider"></div>
  <div class="footer-stat">
    <div class="num">0</div>
    <div class="lbl">Prerequisites</div>
  </div>
  <div class="footer-divider"></div>
  <div class="footer-stat">
    <div class="num green">100%</div>
    <div class="lbl">Complete</div>
  </div>
  <div class="footer-note">PDF PRESENTATION STYLE v2.5</div>
</div>