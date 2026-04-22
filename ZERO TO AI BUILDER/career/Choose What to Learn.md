---
marp: true
theme: default
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=DM+Mono:wght@400;500&display=swap');

  :root {
    --blue: #2563eb;
    --blue-light: #eff6ff;
    --blue-mid: #bfdbfe;
    --text: #111827;
    --muted: #6b7280;
    --border: #e5e7eb;
    --white: #ffffff;
    --off-white: #f9fafb;
  }

  section {
    font-family: 'DM Sans', sans-serif;
    background: var(--white);
    color: var(--text);
    padding: 52px 64px;
    font-size: 18px;
    line-height: 1.6;
  }

  section::after {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: var(--muted);
  }

  h1 {
    font-family: 'DM Sans', sans-serif;
    font-size: 42px;
    font-weight: 600;
    color: var(--text);
    line-height: 1.2;
    margin-bottom: 0.4em;
  }

  h2 {
    font-family: 'DM Sans', sans-serif;
    font-size: 28px;
    font-weight: 600;
    color: var(--text);
    border-bottom: 2px solid var(--blue);
    padding-bottom: 10px;
    margin-bottom: 24px;
  }

  h3 {
    font-family: 'DM Sans', sans-serif;
    font-size: 20px;
    font-weight: 500;
    color: var(--blue);
    margin-bottom: 8px;
  }

  p { color: var(--text); margin: 0.4em 0; }
  ul { padding-left: 1.4em; }
  li { margin-bottom: 10px; color: var(--text); }
  strong { color: var(--blue); font-weight: 600; }

  code {
    font-family: 'DM Mono', monospace;
    background: var(--blue-light);
    color: var(--blue);
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.88em;
  }

  blockquote {
    border-left: 4px solid var(--blue);
    background: var(--blue-light);
    padding: 16px 20px;
    margin: 20px 0;
    border-radius: 0 8px 8px 0;
    font-family: 'DM Mono', monospace;
    font-size: 0.82em;
    color: #1e40af;
    line-height: 1.6;
  }

  blockquote p { color: #1e40af; margin: 0; }

  section.cover {
    background: var(--text);
    color: var(--white);
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  section.cover h1 { color: var(--white); font-size: 46px; }
  section.cover h2 { color: #93c5fd; border-bottom-color: #374151; }
  section.cover p  { color: #9ca3af; }
  section.cover strong { color: #60a5fa; }
  section.cover code { background: #1e3a5f; color: #93c5fd; }

  section.step { background: var(--off-white); }

  .highlight {
    background: var(--blue-light);
    border: 1px solid var(--blue-mid);
    border-radius: 10px;
    padding: 18px 24px;
    margin: 16px 0;
  }

  .tools {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 16px;
  }

  .tool-card {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px 20px;
  }

  .tool-card .icon  { font-size: 24px; margin-bottom: 6px; }
  .tool-card .name  { font-weight: 600; font-size: 15px; color: var(--text); }
  .tool-card .desc  { font-size: 13px; color: var(--muted); margin-top: 2px; }

  .step-badge {
    display: inline-block;
    background: var(--blue);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    padding: 4px 14px;
    border-radius: 999px;
    margin-bottom: 12px;
    letter-spacing: 0.05em;
  }

  section.final {
    background: var(--blue);
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
  }

  section.final h1 { color: white; font-size: 40px; }
  section.final p  { color: #bfdbfe; font-size: 18px; }
  section.final strong { color: white; }
  section.final em { color: #bfdbfe; }

  /* ── Two-column layout ── */
  .two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 16px;
  }

  .col-card {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px 20px;
  }

  .col-card .label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 8px;
  }

  /* ── Confusion trap cards ── */
  .trap-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .trap-card {
    background: var(--white);
    border: 1px solid #fecaca;
    border-radius: 10px;
    padding: 13px 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }

  .trap-card .tc-icon { font-size: 22px; flex-shrink: 0; }

  .trap-card .tc-title {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
    margin-bottom: 3px;
  }

  .trap-card .tc-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.5;
  }

  /* ── Direction cards ── */
  .direction-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .direction-card {
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .direction-card .dc-header {
    padding: 12px 14px;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .direction-card.web    .dc-header { background: var(--blue-light); border-color: var(--blue-mid); }
  .direction-card.data   .dc-header { background: #f0fdf4; border-color: #86efac; }
  .direction-card.auto   .dc-header { background: #f5f3ff; border-color: #c4b5fd; }
  .direction-card.game   .dc-header { background: #fef3c7; border-color: #fde68a; }
  .direction-card.ai     .dc-header { background: #fef2f2; border-color: #fecaca; }
  .direction-card.script .dc-header { background: #f0f9ff; border-color: #bae6fd; }

  .direction-card .dc-icon { font-size: 22px; }

  .direction-card .dc-name {
    font-weight: 700;
    font-size: 13.5px;
    color: var(--text);
  }

  .direction-card .dc-body {
    padding: 10px 14px;
    background: var(--white);
  }

  .direction-card .dc-learn {
    font-size: 12px;
    color: var(--muted);
    line-height: 1.55;
    margin-bottom: 6px;
  }

  .direction-card .dc-tools {
    display: flex;
    gap: 5px;
    flex-wrap: wrap;
  }

  .direction-card .dc-tool {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    padding: 2px 7px;
    border-radius: 4px;
    background: var(--off-white);
    color: var(--muted);
    border: 1px solid var(--border);
  }

  /* ── Job vs hobby split ── */
  .path-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0;
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin-top: 16px;
  }

  .path-side { padding: 18px 20px; }
  .path-side.job   { background: var(--blue-light); border-right: 1px solid var(--border); }
  .path-side.hobby { background: #f5f3ff; }

  .path-side .ps-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 8px;
  }

  .path-side.job   .ps-label { color: #1e40af; }
  .path-side.hobby .ps-label { color: #5b21b6; }

  .path-side .ps-title {
    font-weight: 700;
    font-size: 17px;
    color: var(--text);
    margin-bottom: 12px;
  }

  .path-side .ps-item {
    font-size: 13px;
    color: var(--muted);
    padding: 6px 0;
    border-bottom: 1px solid var(--border);
    display: flex;
    gap: 8px;
    align-items: flex-start;
    line-height: 1.5;
  }

  .path-side.hobby .ps-item { border-color: #ede9fe; }
  .path-side .ps-item:last-child { border-bottom: none; }
  .path-side .ps-item .pi-arrow { flex-shrink: 0; color: var(--border); }

  /* ── Skill stack diagram ── */
  .skill-stack {
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin: 16px 0;
  }

  .ss-layer {
    border-radius: 8px;
    padding: 12px 18px;
    display: flex;
    align-items: center;
    gap: 14px;
    border: 2px solid transparent;
  }

  .ss-layer.foundation { background: #dbeafe; border-color: #93c5fd; }
  .ss-layer.layer2     { background: #d1fae5; border-color: #6ee7b7; }
  .ss-layer.layer3     { background: #ede9fe; border-color: #c4b5fd; }
  .ss-layer.layer4     { background: #fef3c7; border-color: #fde68a; }
  .ss-layer.peak       { background: #fce7f3; border-color: #f9a8d4; }

  .ss-layer .sl-icon { font-size: 20px; flex-shrink: 0; }

  .ss-layer .sl-label {
    font-weight: 700;
    font-size: 13.5px;
    min-width: 160px;
  }

  .ss-layer.foundation .sl-label { color: #1e3a8a; }
  .ss-layer.layer2     .sl-label { color: #065f46; }
  .ss-layer.layer3     .sl-label { color: #3b0764; }
  .ss-layer.layer4     .sl-label { color: #78350f; }
  .ss-layer.peak       .sl-label { color: #831843; }

  .ss-layer .sl-desc {
    font-size: 13px;
    color: var(--muted);
    flex: 1;
  }

  .ss-layer .sl-time {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    flex-shrink: 0;
  }

  /* ── Roadmap timeline ── */
  .roadmap {
    display: flex;
    flex-direction: column;
    gap: 0;
    margin: 14px 0;
  }

  .rm-step {
    display: flex;
    align-items: stretch;
    gap: 0;
  }

  .rm-step .rm-timeline {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 48px;
    flex-shrink: 0;
    padding: 0 0 0 4px;
  }

  .rm-step .rm-dot {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: var(--blue);
    border: 2px solid var(--white);
    box-shadow: 0 0 0 2px var(--blue);
    flex-shrink: 0;
    margin-top: 12px;
  }

  .rm-step .rm-line {
    width: 2px;
    flex: 1;
    background: var(--border);
    margin-top: 4px;
    margin-bottom: -4px;
  }

  .rm-step:last-child .rm-line { display: none; }

  .rm-step .rm-content {
    flex: 1;
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px 16px;
    margin: 6px 0 6px 12px;
  }

  .rm-step .rm-content .rmc-phase {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--blue);
    font-weight: 600;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    margin-bottom: 3px;
  }

  .rm-step .rm-content .rmc-title {
    font-weight: 600;
    font-size: 14px;
    color: var(--text);
    margin-bottom: 3px;
  }

  .rm-step .rm-content .rmc-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.55;
  }

  .rm-step .rm-content .rmc-time {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    color: var(--muted);
    margin-top: 5px;
  }

  /* ── Decision questions ── */
  .question-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .question-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 16px;
  }

  .question-card .qc-q {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
    margin-bottom: 8px;
    display: flex;
    align-items: flex-start;
    gap: 8px;
  }

  .question-card .qc-q .qc-icon { font-size: 16px; flex-shrink: 0; margin-top: 1px; }

  .question-card .qc-answers {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  .question-card .qc-a {
    font-size: 12.5px;
    color: var(--muted);
    padding: 4px 8px;
    border-radius: 5px;
    background: var(--off-white);
    display: flex;
    align-items: baseline;
    gap: 8px;
    line-height: 1.5;
  }

  .question-card .qc-a .qa-choice {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    color: var(--blue);
    font-weight: 600;
    flex-shrink: 0;
  }

  /* ── Cheatsheet table ── */
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
    font-size: 12px;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.05em;
  }

  .cheat-table td {
    padding: 9px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
  }

  .cheat-table tr:last-child td { border-bottom: none; }
  .cheat-table tr:nth-child(even) td { background: var(--off-white); }

  .cheat-table .mono {
    font-family: 'DM Mono', monospace;
    color: var(--blue);
    font-size: 12.5px;
  }

  .step-list {
    counter-reset: steps;
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .step-list li {
    counter-increment: steps;
    display: flex;
    align-items: flex-start;
    gap: 14px;
    margin-bottom: 14px;
  }

  .step-list li::before {
    content: counter(steps);
    background: var(--blue);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    min-width: 24px;
    height: 24px;
    border-radius: 999px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 2px;
    flex-shrink: 0;
  }
---

<!-- _class: cover -->

# How to Choose What
# to Learn Next

&nbsp;

**The paralysis is the problem — not the options.** Here's a framework that cuts through it.

`direction` · `goal` · `skill stack` · `roadmap` · `focus`

---

## The Confusion Problem

Every beginner hits the same wall: too many options, too many opinions, and no clear signal for what to do next.

<div class="trap-grid">
  <div class="trap-card">
    <div class="tc-icon">🌀</div>
    <div>
      <div class="tc-title">Tutorial hopping</div>
      <div class="tc-desc">Starting five different courses, finishing none. Each one feels like the right one — until the next shiny topic appears two weeks in.</div>
    </div>
  </div>
  <div class="trap-card">
    <div class="tc-icon">😶</div>
    <div>
      <div class="tc-title">Waiting for the "right" path</div>
      <div class="tc-desc">Researching endlessly before starting. Comparing roadmaps. Reading "what to learn in 2026" articles instead of actually learning.</div>
    </div>
  </div>
  <div class="trap-card">
    <div class="tc-icon">📚</div>
    <div>
      <div class="tc-title">Learning without a goal</div>
      <div class="tc-desc">Picking topics that feel impressive rather than useful. JavaScript → then Rust → then machine learning, with no connecting thread.</div>
    </div>
  </div>
  <div class="trap-card">
    <div class="tc-icon">🏔️</div>
    <div>
      <div class="tc-title">Skipping to advanced topics</div>
      <div class="tc-desc">Trying to learn neural networks before understanding functions, or React before understanding HTML. The gaps make everything harder.</div>
    </div>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**The fix isn't finding the perfect path — it's picking a direction and staying on it long enough to see progress.** Any of the directions on the next slide leads somewhere real.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Pick a Direction — Six That Lead Somewhere

Every direction below leads to real skills and real opportunities. Pick the one closest to what you actually want to make or do.

<div class="direction-grid">
  <div class="direction-card web">
    <div class="dc-header">
      <div class="dc-icon">🌐</div>
      <div class="dc-name">Web Development</div>
    </div>
    <div class="dc-body">
      <div class="dc-learn">Build websites and web apps. The most job listings, the most learning resources, and the fastest path from zero to a working thing on the internet.</div>
      <div class="dc-tools">
        <span class="dc-tool">HTML</span>
        <span class="dc-tool">CSS</span>
        <span class="dc-tool">JavaScript</span>
        <span class="dc-tool">React</span>
      </div>
    </div>
  </div>
  <div class="direction-card data">
    <div class="dc-header">
      <div class="dc-icon">📊</div>
      <div class="dc-name">Data & Analysis</div>
    </div>
    <div class="dc-body">
      <div class="dc-learn">Turn numbers into insight. High demand in every industry. Works well for people who like spreadsheets but want to go further.</div>
      <div class="dc-tools">
        <span class="dc-tool">Python</span>
        <span class="dc-tool">pandas</span>
        <span class="dc-tool">SQL</span>
        <span class="dc-tool">Tableau</span>
      </div>
    </div>
  </div>
  <div class="direction-card auto">
    <div class="dc-header">
      <div class="dc-icon">🤖</div>
      <div class="dc-name">Automation & AI</div>
    </div>
    <div class="dc-body">
      <div class="dc-learn">Automate repetitive work and build AI workflows. The fastest-growing direction. Practical payoff even at beginner skill levels.</div>
      <div class="dc-tools">
        <span class="dc-tool">Python</span>
        <span class="dc-tool">APIs</span>
        <span class="dc-tool">Zapier</span>
        <span class="dc-tool">Claude</span>
      </div>
    </div>
  </div>
  <div class="direction-card game">
    <div class="dc-header">
      <div class="dc-icon">🎮</div>
      <div class="dc-name">Game Development</div>
    </div>
    <div class="dc-body">
      <div class="dc-learn">Build games — from browser minigames to mobile apps. High motivation because the project is the reward. Teaches fundamentals through play.</div>
      <div class="dc-tools">
        <span class="dc-tool">Python</span>
        <span class="dc-tool">Pygame</span>
        <span class="dc-tool">Unity</span>
        <span class="dc-tool">GDScript</span>
      </div>
    </div>
  </div>
  <div class="direction-card ai">
    <div class="dc-header">
      <div class="dc-icon">🧠</div>
      <div class="dc-name">Machine Learning</div>
    </div>
    <div class="dc-body">
      <div class="dc-learn">Build models that learn from data. Steeper curve — requires maths foundations. Higher ceiling. Best entered after Python + data fundamentals.</div>
      <div class="dc-tools">
        <span class="dc-tool">Python</span>
        <span class="dc-tool">scikit-learn</span>
        <span class="dc-tool">PyTorch</span>
        <span class="dc-tool">NumPy</span>
      </div>
    </div>
  </div>
  <div class="direction-card script">
    <div class="dc-header">
      <div class="dc-icon">⚙️</div>
      <div class="dc-name">Scripting & DevOps</div>
    </div>
    <div class="dc-body">
      <div class="dc-learn">Automate your computer, manage servers, and build pipelines. Invisible work that everything else depends on. Best if you like systems thinking.</div>
      <div class="dc-tools">
        <span class="dc-tool">Python</span>
        <span class="dc-tool">Bash</span>
        <span class="dc-tool">Docker</span>
        <span class="dc-tool">Linux</span>
      </div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Job Path vs Hobby Path

The right choice depends entirely on what you want at the end. These two paths require different learning strategies — not just different content.

<div class="path-compare">
  <div class="path-side job">
    <div class="ps-label">💼 &nbsp;Job / career path</div>
    <div class="ps-title">Learning to get hired</div>
    <div class="ps-item"><span class="pi-arrow">→</span> Start with what employers actually use — not what's trendy</div>
    <div class="ps-item"><span class="pi-arrow">→</span> Build a portfolio of 3–5 real projects early</div>
    <div class="ps-item"><span class="pi-arrow">→</span> Study job postings to learn which skills appear most</div>
    <div class="ps-item"><span class="pi-arrow">→</span> Practice explaining your code out loud — interviews test this</div>
    <div class="ps-item"><span class="pi-arrow">→</span> Depth beats breadth. Know one stack very well before diversifying</div>
  </div>
  <div class="path-side hobby">
    <div class="ps-label">🎨 &nbsp;Hobby / personal path</div>
    <div class="ps-title">Learning to build things</div>
    <div class="ps-item"><span class="pi-arrow">→</span> Start with whatever keeps you motivated the longest</div>
    <div class="ps-item"><span class="pi-arrow">→</span> Pick projects you actually want to exist in the world</div>
    <div class="ps-item"><span class="pi-arrow">→</span> Breadth is fine — follow curiosity across directions</div>
    <div class="ps-item"><span class="pi-arrow">→</span> Finishing small projects matters more than perfect code</div>
    <div class="ps-item"><span class="pi-arrow">→</span> The goal is the project, not the résumé</div>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**Neither path is wrong.** They're just different games with different rules. The mistake is playing the hobby game while trying to win the job game — or forcing yourself onto a career track when you just want to make something fun.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Skill Stacking — Why One Skill Is Never Enough

A skill stack is a combination of skills that creates rare and specific value. The goal isn't mastery of one thing — it's a combination nobody else has.

<div class="skill-stack">
  <div class="ss-layer foundation">
    <div class="sl-icon">🧱</div>
    <div class="sl-label">Foundation</div>
    <div class="sl-desc">Python or JavaScript — one language, solidly. Variables, loops, functions, files. Every other skill is built on this.</div>
    <div class="sl-time">months 1–3</div>
  </div>
  <div class="ss-layer layer2">
    <div class="sl-icon">🔧</div>
    <div class="sl-label">Domain skill</div>
    <div class="sl-desc">The direction you picked — data, web, automation, etc. This is where you start building things that look like real projects.</div>
    <div class="sl-time">months 3–8</div>
  </div>
  <div class="ss-layer layer3">
    <div class="sl-icon">🌐</div>
    <div class="sl-label">Adjacent skill</div>
    <div class="sl-desc">Something from a neighbouring domain that multiplies the first two. APIs + automation. SQL + data viz. Git + web dev. These combinations open new doors.</div>
    <div class="sl-time">months 6–12</div>
  </div>
  <div class="ss-layer layer4">
    <div class="sl-icon">💡</div>
    <div class="sl-label">Domain knowledge</div>
    <div class="sl-desc">Your industry or interest area — finance, biology, education, music. A coder who understands the domain is worth more than one who doesn't.</div>
    <div class="sl-time">ongoing</div>
  </div>
  <div class="ss-layer peak">
    <div class="sl-icon">✨</div>
    <div class="sl-label">The rare combination</div>
    <div class="sl-desc">Python + data + biology = bioinformatics. Automation + finance = quant tools. Web + music = music apps. Your stack is your niche.</div>
    <div class="sl-time">year 1+</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Four Questions That Cut Through the Noise

Answer these honestly. The answers narrow the field to one or two real directions.

<div class="question-grid">
  <div class="question-card">
    <div class="qc-q"><span class="qc-icon">🎯</span> What's the outcome you actually want?</div>
    <div class="qc-answers">
      <div class="qc-a"><span class="qa-choice">job →</span> Web dev or data. Both have clear hiring pipelines.</div>
      <div class="qc-a"><span class="qa-choice">freelance →</span> Web dev or automation. Both pay project-to-project.</div>
      <div class="qc-a"><span class="qa-choice">side projects →</span> Whatever you'd build even if nobody paid you.</div>
      <div class="qc-a"><span class="qa-choice">understand AI →</span> Python + APIs. Start building before studying theory.</div>
    </div>
  </div>
  <div class="question-card">
    <div class="qc-q"><span class="qc-icon">⏰</span> How much time do you have per week?</div>
    <div class="qc-answers">
      <div class="qc-a"><span class="qa-choice">1–3 hrs →</span> One small skill only. Pick one and ignore everything else.</div>
      <div class="qc-a"><span class="qa-choice">4–8 hrs →</span> One direction with one project running at all times.</div>
      <div class="qc-a"><span class="qa-choice">10+ hrs →</span> Main direction plus one adjacent skill simultaneously.</div>
    </div>
  </div>
  <div class="question-card">
    <div class="qc-q"><span class="qc-icon">💪</span> What have you already started?</div>
    <div class="qc-answers">
      <div class="qc-a"><span class="qa-choice">HTML/CSS →</span> Keep going. Web is the most documented path on earth.</div>
      <div class="qc-a"><span class="qa-choice">Python basics →</span> Add one of: data, automation, or scraping. Don't restart.</div>
      <div class="qc-a"><span class="qa-choice">Nothing yet →</span> Pick web (HTML first) or automation (Python first). Both are forgiving for beginners.</div>
    </div>
  </div>
  <div class="question-card">
    <div class="qc-q"><span class="qc-icon">🔥</span> What keeps you up at night (in a good way)?</div>
    <div class="qc-answers">
      <div class="qc-a"><span class="qa-choice">building things →</span> Web dev. Immediate visual feedback. Fast wins.</div>
      <div class="qc-a"><span class="qa-choice">solving puzzles →</span> Data or algorithms. Pattern recognition is the job.</div>
      <div class="qc-a"><span class="qa-choice">making life easier →</span> Automation. Small scripts with big daily impact.</div>
      <div class="qc-a"><span class="qa-choice">understanding AI →</span> APIs + prompting → then Python → then ML theory.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## A Simple Roadmap — Pick Your Direction, Follow the Phases

Same four phases for every direction. Only the content changes.

<div class="roadmap">
  <div class="rm-step">
    <div class="rm-timeline">
      <div class="rm-dot"></div>
      <div class="rm-line"></div>
    </div>
    <div class="rm-content">
      <div class="rmc-phase">Phase 1</div>
      <div class="rmc-title">Foundation — the basics of your chosen language</div>
      <div class="rmc-desc">Variables, loops, functions, data structures. One tutorial, one book, or one free course. Finish it. Don't start a second one while the first is unfinished.</div>
      <div class="rmc-time">weeks 1–6 · one focused resource · no side quests</div>
    </div>
  </div>
  <div class="rm-step">
    <div class="rm-timeline">
      <div class="rm-dot"></div>
      <div class="rm-line"></div>
    </div>
    <div class="rm-content">
      <div class="rmc-phase">Phase 2</div>
      <div class="rmc-title">First project — something embarrassingly simple</div>
      <div class="rmc-desc">Build one small thing from scratch. A to-do list. A weather widget. A simple script that does something useful. It will look bad. Build it anyway. Finishing it matters more than quality.</div>
      <div class="rmc-time">weeks 4–10 · one project · no tutorials, just building</div>
    </div>
  </div>
  <div class="rm-step">
    <div class="rm-timeline">
      <div class="rm-dot"></div>
      <div class="rm-line"></div>
    </div>
    <div class="rm-content">
      <div class="rmc-phase">Phase 3</div>
      <div class="rmc-title">Domain depth — go further into your chosen direction</div>
      <div class="rmc-desc">Learn the libraries and tools specific to your path. Web: add a framework. Data: add SQL and visualisation. Automation: add API calls. Build a second project using these new tools.</div>
      <div class="rmc-time">months 3–6 · project-driven learning · look things up as you need them</div>
    </div>
  </div>
  <div class="rm-step">
    <div class="rm-timeline">
      <div class="rm-dot"></div>
      <div class="rm-line"></div>
    </div>
    <div class="rm-content">
      <div class="rmc-phase">Phase 4</div>
      <div class="rmc-title">Adjacent skill — expand the stack deliberately</div>
      <div class="rmc-desc">Add the skill that multiplies what you already know. Git + deployment for web. SQL for data. AI APIs for automation. This is when the "rare combination" starts to form.</div>
      <div class="rmc-time">months 6–12 · one new skill at a time · integrate into ongoing projects</div>
    </div>
  </div>
</div>

---

## Learning Direction Cheatsheet

<table class="cheat-table">
  <tr>
    <th>If you want to…</th>
    <th>Start with</th>
    <th>Then add</th>
    <th>Avoid (for now)</th>
  </tr>
  <tr>
    <td>Get a developer job</td>
    <td class="mono">HTML → CSS → JavaScript</td>
    <td>React, Git, portfolio projects</td>
    <td>Multiple languages at once</td>
  </tr>
  <tr>
    <td>Work with data</td>
    <td class="mono">Python → pandas → SQL</td>
    <td>Matplotlib, Jupyter, dashboards</td>
    <td>Machine learning before the basics</td>
  </tr>
  <tr>
    <td>Build automations</td>
    <td class="mono">Python → requests → APIs</td>
    <td>cron, Zapier, AI integration</td>
    <td>Complex frameworks before scripts work</td>
  </tr>
  <tr>
    <td>Make games</td>
    <td class="mono">Python → Pygame</td>
    <td>Godot or Unity when ready</td>
    <td>3D engines before 2D games</td>
  </tr>
  <tr>
    <td>Understand AI/ML</td>
    <td class="mono">Python → APIs → prompting</td>
    <td>scikit-learn, then PyTorch</td>
    <td>Theory before you can code</td>
  </tr>
  <tr>
    <td>Automate your own life</td>
    <td class="mono">Python scripts → scheduling</td>
    <td>Zapier, email automation, AI</td>
    <td>Perfecting code before it works at all</td>
  </tr>
  <tr>
    <td>Freelance as a developer</td>
    <td class="mono">Web dev basics</td>
    <td>One CMS (WordPress, Webflow)</td>
    <td>Building tools instead of client work</td>
  </tr>
  <tr>
    <td>Switch careers into tech</td>
    <td>Job postings in your target role</td>
    <td>The exact stack mentioned most often</td>
    <td>Learning skills not in the job listings</td>
  </tr>
</table>

---

<!-- _class: final -->

# Pick a direction.
# Stay on it.
# Build something real.

&nbsp;

The perfect path doesn't exist. A finished project beats a perfect plan every time.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*