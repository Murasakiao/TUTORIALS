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
  section.cover h2 { color: var(--white); border-bottom-color: #374151; }
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

  .highlight.good {
    background: #f0fdf4;
    border-color: #bbf7d0;
  }

  .highlight.warn {
    background: #fefce8;
    border-color: #fde68a;
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

  /* What hiring managers see */
  .hm-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin: 16px 0;
  }

  .hm-card {
    border-radius: 10px;
    padding: 16px 18px;
    display: flex;
    gap: 12px;
    align-items: flex-start;
  }

  .hm-card.good { background: #f0fdf4; border: 1px solid #bbf7d0; }
  .hm-card.bad  { background: #fff1f2; border: 1px solid #fecdd3; }

  .hm-card .hmc-icon { font-size: 20px; flex-shrink: 0; margin-top: 2px; }

  .hm-card .hmc-body .hmc-title {
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 3px;
  }

  .hm-card.good .hmc-body .hmc-title { color: #14532d; }
  .hm-card.bad  .hmc-body .hmc-title { color: #9f1239; }

  .hm-card .hmc-body .hmc-detail {
    font-size: 12px;
    line-height: 1.5;
  }

  .hm-card.good .hmc-body .hmc-detail { color: #166534; }
  .hm-card.bad  .hmc-body .hmc-detail { color: #be123c; }

  /* Project card mock */
  .project-card {
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 12px;
    overflow: hidden;
    margin: 14px 0;
  }

  .project-card .proj-header {
    background: #161b22;
    padding: 12px 18px;
    border-bottom: 1px solid #30363d;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .project-card .proj-header .ph-title {
    font-size: 15px;
    font-weight: 600;
    color: #f0f6fc;
    flex: 1;
  }

  .project-card .proj-header .ph-stack {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #6b7280;
  }

  .project-card .proj-body {
    padding: 16px 18px;
    font-size: 13px;
    line-height: 1.8;
  }

  .proj-row {
    display: flex;
    gap: 12px;
    margin-bottom: 10px;
    align-items: flex-start;
  }

  .proj-row:last-child { margin-bottom: 0; }

  .proj-row .pr-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    min-width: 80px;
    flex-shrink: 0;
    padding-top: 1px;
  }

  .proj-row.problem .pr-label { color: #f87171; }
  .proj-row.solution .pr-label { color: #86efac; }
  .proj-row.role .pr-label { color: #60a5fa; }
  .proj-row.result .pr-label { color: #c4b5fd; }

  .proj-row .pr-text { color: #d1d5db; line-height: 1.6; }

  .project-card .proj-footer {
    background: #0d1117;
    border-top: 1px solid #21262d;
    padding: 9px 18px;
    display: flex;
    gap: 12px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #4b5563;
  }

  .project-card .proj-footer .pf-link { color: #60a5fa; }

  /* About page anatomy */
  .about-anatomy {
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 12px;
    overflow: hidden;
    margin: 14px 0;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
  }

  .about-bar {
    background: #161b22;
    padding: 9px 18px;
    border-bottom: 1px solid #30363d;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: 0.07em;
  }

  .about-body {
    padding: 16px 20px;
    line-height: 2;
  }

  .about-body .ab-line { display: flex; gap: 10px; align-items: baseline; margin-bottom: 4px; }
  .about-body .ab-num  { font-family: 'DM Mono', monospace; font-size: 10px; color: #4b5563; min-width: 20px; flex-shrink: 0; }
  .about-body .ab-role { color: #f9a8d4; font-weight: 600; }
  .about-body .ab-work { color: #86efac; font-weight: 600; }
  .about-body .ab-for  { color: #60a5fa; font-weight: 600; }
  .about-body .ab-why  { color: #fde68a; font-weight: 600; }
  .about-body .ab-cta  { color: #c4b5fd; font-weight: 600; }
  .about-body .ab-plain{ color: #d1d5db; }

  /* Leave out red cards */
  .leave-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin: 14px 0;
  }

  .leave-card {
    background: #fff1f2;
    border: 1px solid #fecdd3;
    border-radius: 8px;
    padding: 14px 16px;
  }

  .leave-card .lc-icon  { font-size: 20px; margin-bottom: 6px; }
  .leave-card .lc-title { font-size: 13px; font-weight: 600; color: #9f1239; margin-bottom: 4px; }
  .leave-card .lc-why   { font-size: 12px; color: #be123c; line-height: 1.5; }

  /* Quality vs quantity */
  .qq-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 16px 0;
  }

  .qq-card {
    border-radius: 10px;
    overflow: hidden;
  }

  .qq-card .qqc-header {
    padding: 9px 16px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }

  .qq-card.many .qqc-header  { background: #451a03; color: #fde68a; }
  .qq-card.few  .qqc-header  { background: #14532d; color: #86efac; }

  .qq-card .qqc-body {
    background: #0d1117;
    padding: 14px 16px;
    font-size: 13px;
    line-height: 1.9;
  }

  .qq-card.many .qqc-body { border: 1px solid #451a03; border-top: none; border-radius: 0 0 10px 10px; color: #fde68a; }
  .qq-card.few  .qqc-body { border: 1px solid #14532d; border-top: none; border-radius: 0 0 10px 10px; color: #86efac; }

  /* two-col */
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
---

<!-- _class: cover -->

# Build a Portfolio That Gets You Noticed

&nbsp;

**Most portfolios are lists of things you did. The best ones show how you think.**

`projects` · `problem` · `solution` · `evidence` · `voice`

---

## What Hiring Managers Actually Look For

They spend 90 seconds on your portfolio. Here's what sticks and what doesn't.

<div class="hm-grid">
  <div class="hm-card good">
    <div class="hmc-icon">✅</div>
    <div class="hmc-body">
      <div class="hmc-title">Evidence of real problem-solving</div>
      <div class="hmc-detail">Not "I built a thing" — "here was the problem, here's what I chose and why."</div>
    </div>
  </div>
  <div class="hm-card good">
    <div class="hmc-icon">✅</div>
    <div class="hmc-body">
      <div class="hmc-title">A clear technical or creative point of view</div>
      <div class="hmc-detail">What you care about, what you're good at, what makes your work distinct.</div>
    </div>
  </div>
  <div class="hm-card good">
    <div class="hmc-icon">✅</div>
    <div class="hmc-body">
      <div class="hmc-title">Live work or working code</div>
      <div class="hmc-detail">Something they can click, run, or read. Not a description of something they can't see.</div>
    </div>
  </div>
  <div class="hm-card good">
    <div class="hmc-icon">✅</div>
    <div class="hmc-body">
      <div class="hmc-title">How you communicated about the work</div>
      <div class="hmc-detail">Writing quality on the portfolio itself is a proxy for communication quality on the job.</div>
    </div>
  </div>
  <div class="hm-card bad">
    <div class="hmc-icon">❌</div>
    <div class="hmc-body">
      <div class="hmc-title">Ten mediocre projects</div>
      <div class="hmc-detail">Volume without depth signals someone who builds things but doesn't finish or refine them.</div>
    </div>
  </div>
  <div class="hm-card bad">
    <div class="hmc-icon">❌</div>
    <div class="hmc-body">
      <div class="hmc-title">Skills listed without evidence</div>
      <div class="hmc-detail">"Proficient in Python" means nothing next to a GitHub repo that shows it.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Quality Over Quantity — 3 Strong Projects

<div class="qq-compare">
  <div class="qq-card many">
    <div class="qqc-header">⚠️ 10 projects — quantity approach</div>
    <div class="qqc-body">
      ✦ 7 are unfinished or toy examples<br>
      ✦ No project has depth or explanation<br>
      ✦ Reviewer doesn't know what you're actually good at<br>
      ✦ Each project competes for attention — none wins<br>
      ✦ Signals: prolific but unfocused
    </div>
  </div>
  <div class="qq-card few">
    <div class="qqc-header">✅ 3 projects — quality approach</div>
    <div class="qqc-body">
      ✦ Each is polished, documented, and complete<br>
      ✦ Each has a clear problem, solution, and outcome<br>
      ✦ Reviewer immediately knows your level and style<br>
      ✦ One outstanding project is worth five mediocre ones<br>
      ✦ Signals: selective, thorough, confident
    </div>
  </div>
</div>

<div class="highlight">

**Pick 3 that each show a different dimension:** one technical depth project, one creative or design project, one that shows you can ship and communicate. Three angles, one clear picture.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Each Project Needs: Problem + Solution + Your Role

The template every strong project page follows:

<div class="project-card">
  <div class="proj-header">
    <span class="ph-title">Visayas Grid Voltage Monitoring Tool</span>
    <span class="ph-stack">Python · pandas · Flask · pandapower</span>
  </div>
  <div class="proj-body">
    <div class="proj-row problem">
      <span class="pr-label">Problem</span>
      <span class="pr-text">Weekly N-1 contingency analysis produced raw CSV output that took 90 minutes to manually clean, flag, and format into a readable report for the engineering team.</span>
    </div>
    <div class="proj-row solution">
      <span class="pr-label">Solution</span>
      <span class="pr-text">Built an automated pipeline that ingests the export, flags undervoltage buses (&lt;0.95 pu), generates a summary Excel report, and sends it to the team — triggered by dropping a file in a folder.</span>
    </div>
    <div class="proj-row role">
      <span class="pr-label">My role</span>
      <span class="pr-text">Sole developer. Designed the schema, wrote the pandas pipeline with AI assistance, built the n8n automation, and set up the scheduling on Oracle Cloud.</span>
    </div>
    <div class="proj-row result">
      <span class="pr-label">Result</span>
      <span class="pr-text">90-minute weekly task reduced to 8 minutes. Now runs automatically — zero manual intervention required.</span>
    </div>
  </div>
  <div class="proj-footer">
    <span>📁 GitHub repo</span>
    <span class="pf-link">→ github.com/julius/grid-monitor</span>
    <span>🔗 Live demo available</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Screenshots, Live Links, and Evidence

A project description without evidence is just a claim. Evidence is what converts a reviewer into a contact.

<div class="tools">
  <div class="tool-card">
    <div class="icon">📸</div>
    <div class="name">Screenshots</div>
    <div class="desc">Show the UI, the output, the terminal — whatever the "done state" looks like. One good screenshot beats three paragraphs of description.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔗</div>
    <div class="name">Live links</div>
    <div class="desc">GitHub Pages, Render, Railway — your project should be reachable. A dead link signals a dead project.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🎬</div>
    <div class="name">Short demo GIF or video</div>
    <div class="desc">30 seconds of it working is worth more than any written description. Record with QuickTime or Loom.</div>
  </div>
  <div class="tool-card">
    <div class="icon">📂</div>
    <div class="name">GitHub repo with a README</div>
    <div class="desc">Clean code + a good README = evidence of engineering discipline. Messy repos without documentation hurt more than they help.</div>
  </div>
</div>

<div class="highlight warn">

⚠️ Test every link before sharing your portfolio. A broken link on a portfolio page is the professional equivalent of showing up late to an interview.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## The About Page Formula

Your about page is the only place on the portfolio that's about you, not your work. Use it precisely.

<div class="about-anatomy">
  <div class="about-bar">📋 About page — sentence by sentence</div>
  <div class="about-body">
    <div class="ab-line">
      <span class="ab-num">1</span>
      <span><span class="ab-role">I'm a [specific role / title]</span> <span class="ab-plain">— one noun, not a paragraph. No "passionate about".</span></span>
    </div>
    <div class="ab-line">
      <span class="ab-num">2</span>
      <span><span class="ab-work">I [what you build / do]</span> <span class="ab-for">for [who you do it for / in what domain].</span></span>
    </div>
    <div class="ab-line">
      <span class="ab-num">3</span>
      <span><span class="ab-why">Right now I'm focused on [current project or interest]</span> <span class="ab-plain">— shows momentum and direction.</span></span>
    </div>
    <div class="ab-line">
      <span class="ab-num">4</span>
      <span><span class="ab-plain">One sentence of specificity</span> <span class="ab-plain">— something that only you would say. A real opinion, a specific technology, an unusual combination.</span></span>
    </div>
    <div class="ab-line">
      <span class="ab-num">5</span>
      <span><span class="ab-cta">Contact / availability line</span> <span class="ab-plain">— what you're open to and the best way to reach you.</span></span>
    </div>
  </div>
</div>

<div class="highlight good">

**Example:** *I'm a Registered Electrical Engineer building automation tools for power systems analysis. I work on renewable energy integration in the Philippine Visayas grid. Currently building Python pipelines that replace manual reporting workflows. I also write about engineering and AI on Substack. Open to consulting and collaborations — julius@example.com*

</div>

---

## What to Leave Out

<div class="leave-grid">
  <div class="leave-card">
    <div class="lc-icon">🚫</div>
    <div class="lc-title">Unfinished projects</div>
    <div class="lc-why">If you wouldn't show it to a client, don't show it to a hiring manager. Half-built work signals half-commitment.</div>
  </div>
  <div class="leave-card">
    <div class="lc-icon">🚫</div>
    <div class="lc-title">Generic tutorial projects</div>
    <div class="lc-why">To-do apps, weather apps, and CRUD examples say "I followed a tutorial." They don't show independent thinking.</div>
  </div>
  <div class="leave-card">
    <div class="lc-icon">🚫</div>
    <div class="lc-title">Skills lists without evidence</div>
    <div class="lc-why">"Proficient in Python, React, Docker..." means nothing. Show a project that uses them. Let the work make the claim.</div>
  </div>
  <div class="leave-card">
    <div class="lc-icon">🚫</div>
    <div class="lc-title">Objective statements</div>
    <div class="lc-why">"Seeking a challenging role where I can grow..." Nobody has ever hired anyone because of an objective statement.</div>
  </div>
  <div class="leave-card">
    <div class="lc-icon">🚫</div>
    <div class="lc-title">Dead links and broken demos</div>
    <div class="lc-why">A broken link is worse than no link. It signals you don't maintain your own work. Check everything monthly.</div>
  </div>
  <div class="leave-card">
    <div class="lc-icon">🚫</div>
    <div class="lc-title">Walls of text about yourself</div>
    <div class="lc-why">Your about page should be readable in 20 seconds. If it requires scrolling, it's too long. Cut everything non-essential.</div>
  </div>
</div>

---

## The Portfolio Checklist

<div class="two-col">
  <div class="col-card">
    <div class="label">✅ Must have</div>
    <p style="font-size:14px; margin-top:8px; color:#374151; line-height:2;">
      ✦ 3 polished, complete projects<br>
      ✦ Problem + solution + role on each<br>
      ✦ At least one live link or working demo<br>
      ✦ GitHub repo with a real README<br>
      ✦ A specific, human about page<br>
      ✦ Contact info that's easy to find
    </p>
  </div>
  <div class="col-card">
    <div class="label">⚠️ Common mistakes</div>
    <p style="font-size:14px; margin-top:8px; color:#374151; line-height:2;">
      ✦ Too many projects, none with depth<br>
      ✦ Generic about page with no point of view<br>
      ✦ Skills listed, not demonstrated<br>
      ✦ No screenshots or visual evidence<br>
      ✦ Broken links left unchecked<br>
      ✦ Last updated two years ago
    </p>
  </div>
</div>

<div class="highlight good">

**The fastest way to improve any portfolio:** pick your single weakest project, remove it, and spend that time writing a better description of your strongest one. Subtraction is almost always the right first move.

</div>

---

<!-- _class: final -->

# Three strong projects.
# One clear voice.
# Everything else is noise.

&nbsp;

A portfolio is a curated argument for why you're the right person. Make it count.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*