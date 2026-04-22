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

  /* Overwhelm visual */
  .overwhelm-list {
    background: #111827;
    border-radius: 10px;
    padding: 18px 22px;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .ow-row {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 8px;
    line-height: 1.5;
  }

  .ow-row:last-child { margin-bottom: 0; }

  .ow-row .ow-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
  }

  .ow-row.critical .ow-dot { background: #2563eb; }
  .ow-row.useful   .ow-dot { background: #1d4ed8; opacity: 0.7; }
  .ow-row.rare     .ow-dot { background: #374151; }
  .ow-row.never    .ow-dot { background: #1f2937; }

  .ow-row.critical .ow-text { color: #60a5fa; font-weight: 600; }
  .ow-row.useful   .ow-text { color: #93c5fd; }
  .ow-row.rare     .ow-text { color: #4b5563; }
  .ow-row.never    .ow-text { color: #374151; }

  .ow-row .ow-pct {
    margin-left: auto;
    font-size: 11px;
    font-weight: 600;
  }

  .ow-row.critical .ow-pct { color: #60a5fa; }
  .ow-row.useful   .ow-pct { color: #4b5563; }
  .ow-row.rare     .ow-pct { color: #374151; }
  .ow-row.never    .ow-pct { color: #1f2937; }

  /* Pareto bar */
  .pareto-bar {
    background: #111827;
    border-radius: 10px;
    padding: 20px 24px;
    margin: 16px 0;
  }

  .pb-track {
    height: 32px;
    border-radius: 6px;
    background: #1f2937;
    position: relative;
    overflow: hidden;
    margin-bottom: 10px;
  }

  .pb-fill-20 {
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 20%;
    background: #2563eb;
    border-radius: 6px 0 0 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 700;
    color: white;
  }

  .pb-fill-80 {
    position: absolute;
    left: 20%; top: 0; bottom: 0;
    right: 0;
    background: #1f2937;
    border-radius: 0 6px 6px 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: #374151;
  }

  .pb-label-row {
    display: flex;
    justify-content: space-between;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    margin-top: 6px;
  }

  .pb-label-row .pbl-left  { color: #60a5fa; font-weight: 600; }
  .pb-label-row .pbl-right { color: #4b5563; }

  /* 20% map — what to learn first */
  .twenty-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin: 14px 0;
  }

  .tg-card {
    border-radius: 10px;
    overflow: hidden;
  }

  .tg-card .tgc-header {
    padding: 8px 14px;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
  }

  .tg-card.python  .tgc-header { background: #1e3a5f; color: #60a5fa; }
  .tg-card.pandas  .tgc-header { background: #14532d; color: #86efac; }
  .tg-card.git     .tgc-header { background: #2e1065; color: #c4b5fd; }

  .tg-card .tgc-body {
    background: #0d1117;
    padding: 12px 14px;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    line-height: 1.9;
  }

  .tg-card.python .tgc-body  { border: 1px solid #1e3a5f; border-top: none; border-radius: 0 0 10px 10px; color: #93c5fd; }
  .tg-card.pandas .tgc-body  { border: 1px solid #14532d; border-top: none; border-radius: 0 0 10px 10px; color: #86efac; }
  .tg-card.git    .tgc-body  { border: 1px solid #2e1065; border-top: none; border-radius: 0 0 10px 10px; color: #c4b5fd; }

  .tg-card .tgc-skip {
    background: #0d1117;
    padding: 6px 14px 10px;
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: #374151;
  }

  /* Build it immediately visual */
  .build-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 14px 0;
  }

  .build-card {
    border-radius: 10px;
    overflow: hidden;
  }

  .build-card .bc-header {
    padding: 9px 16px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }

  .build-card.passive  .bc-header { background: #451a03; color: #fde68a; }
  .build-card.active   .bc-header { background: #14532d; color: #86efac; }

  .build-card .bc-body {
    background: #0d1117;
    padding: 14px 16px;
    font-size: 13px;
    line-height: 2;
  }

  .build-card.passive  .bc-body { border: 1px solid #451a03; border-top: none; border-radius: 0 0 10px 10px; color: #fde68a; }
  .build-card.active   .bc-body { border: 1px solid #14532d; border-top: none; border-radius: 0 0 10px 10px; color: #86efac; }

  /* On-demand learning vs upfront */
  .demand-flow {
    background: #111827;
    border-radius: 10px;
    padding: 16px 22px;
    margin: 14px 0;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
  }

  .df-row {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    margin-bottom: 10px;
  }

  .df-row:last-child { margin-bottom: 0; }

  .df-badge {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    padding: 3px 10px;
    border-radius: 999px;
    flex-shrink: 0;
    margin-top: 2px;
    white-space: nowrap;
  }

  .df-badge.need   { background: #1e3a5f; color: #60a5fa; }
  .df-badge.search { background: #14532d; color: #86efac; }
  .df-badge.learn  { background: #2e1065; color: #c4b5fd; }
  .df-badge.build  { background: #451a03; color: #fde68a; }
  .df-badge.keep   { background: #374151; color: #9ca3af; }

  .df-text { font-size: 13px; color: #d1d5db; line-height: 1.6; }
  .df-text span { font-family: 'DM Mono', monospace; color: #60a5fa; }

  /* Spaced rep schedule */
  .rep-schedule {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 10px;
    margin: 16px 0;
  }

  .rep-card {
    background: #111827;
    border-radius: 8px;
    padding: 14px 12px;
    text-align: center;
  }

  .rep-card .rc-when {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #4b5563;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 6px;
  }

  .rep-card .rc-day {
    font-family: 'DM Mono', monospace;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 4px;
  }

  .rep-card.d1  .rc-day { color: #60a5fa; }
  .rep-card.d3  .rc-day { color: #86efac; }
  .rep-card.d7  .rc-day { color: #c4b5fd; }
  .rep-card.d14 .rc-day { color: #fde68a; }
  .rep-card.d30 .rc-day { color: #f9a8d4; }

  .rep-card .rc-action {
    font-size: 11px;
    color: #6b7280;
    line-height: 1.4;
  }

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

# Learn Anything Technical Faster
## The 20% Rule

&nbsp;

**You don't need to master a tool. You need to be productive with it this week.**

`Pareto` · `deliberate practice` · `build fast` · `learn on demand`

---

## The Overwhelm Problem

Every technical field has the same trap: the curriculum is designed to cover everything, not to get you productive fast.

<div class="tools">
  <div class="tool-card">
    <div class="icon">📚</div>
    <div class="name">Courses cover 100%</div>
    <div class="desc">A Python course has 40 hours of content. You need 4 hours of it to do 80% of what you'll ever actually do.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🗺️</div>
    <div class="name">Documentation is for reference</div>
    <div class="desc">Reading docs front-to-back is like reading a dictionary to learn a language. Reference material is not learning material.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🏗️</div>
    <div class="name">You learn by building</div>
    <div class="desc">Passive learning — watching, reading, taking notes — has almost zero retention without active application within 24 hours.</div>
  </div>
  <div class="tool-card">
    <div class="icon">⚡</div>
    <div class="name">The fix is deliberate scope</div>
    <div class="desc">Identify the 20% of a skill that covers 80% of real use cases. Learn that. Build something. Learn the rest on demand.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Pareto Applied to Learning

20% of any skill's concepts cover 80% of real-world usage. The remaining 80% of concepts are used less than 20% of the time.

<div class="pareto-bar">
  <div class="pb-track">
    <div class="pb-fill-20">20%</div>
    <div class="pb-fill-80">remaining 80% of concepts</div>
  </div>
  <div class="pb-label-row">
    <span class="pbl-left">← Learn this first → covers 80% of use cases</span>
    <span class="pbl-right">Learn on demand when needed →</span>
  </div>
</div>

For Python specifically — the distribution is stark:

<div class="overwhelm-list">
  <div class="ow-row critical"><div class="ow-dot"></div><span class="ow-text">Variables, loops, functions, conditionals, lists, dicts, file I/O</span><span class="ow-pct">used daily</span></div>
  <div class="ow-row useful"><div class="ow-dot"></div><span class="ow-text">Classes, error handling, modules, list comprehensions</span><span class="ow-pct">used often</span></div>
  <div class="ow-row rare"><div class="ow-dot"></div><span class="ow-text">Decorators, generators, metaclasses, async/await</span><span class="ow-pct">used rarely</span></div>
  <div class="ow-row never"><div class="ow-dot"></div><span class="ow-text">C extensions, memory management, GIL internals</span><span class="ow-pct">almost never</span></div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Find the 20% That Covers 80% of Use Cases

For every technical skill, the critical 20% is identifiable before you start. Ask: **what do practitioners actually use every day?**

<div class="twenty-grid">
  <div class="tg-card python">
    <div class="tgc-header">🐍 Python — core 20%</div>
    <div class="tgc-body">
      variables + types<br>
      for loops + if/else<br>
      functions + return<br>
      lists + dicts<br>
      open() + csv module<br>
      pip + imports
    </div>
    <div class="tgc-skip">skip first: classes, decorators, async</div>
  </div>
  <div class="tg-card pandas">
    <div class="tgc-header">🐼 pandas — core 20%</div>
    <div class="tgc-body">
      read_csv / to_csv<br>
      df[ ] filtering<br>
      groupby + agg<br>
      sort_values<br>
      head / shape / dtypes<br>
      to_numeric + fillna
    </div>
    <div class="tgc-skip">skip first: MultiIndex, pivot_table, merge</div>
  </div>
  <div class="tg-card git">
    <div class="tgc-header">🌿 Git — core 20%</div>
    <div class="tgc-body">
      git init / clone<br>
      git add + commit<br>
      git push + pull<br>
      git status + log<br>
      git checkout -b<br>
      .gitignore
    </div>
    <div class="tgc-skip">skip first: rebase, cherry-pick, bisect</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Build Something Small Immediately

Learning without building has a half-life of about 48 hours. The moment you learn a concept, use it on something real.

<div class="build-compare">
  <div class="build-card passive">
    <div class="bc-header">⚠️ Passive learning — low retention</div>
    <div class="bc-body">
      Day 1: Watch 3 hours of Python tutorial<br>
      Day 2: Watch 2 more hours<br>
      Day 3: Can't remember the syntax<br>
      Day 7: Back to zero<br>
      Day 14: "I should restart the course"
    </div>
  </div>
  <div class="build-card active">
    <div class="bc-header">✅ Active building — high retention</div>
    <div class="bc-body">
      Day 1: Learn loops + file I/O (1 hour)<br>
      Day 1: Build a CSV reader for your own data<br>
      Day 2: Hit a problem — learn what you need<br>
      Day 3: Script is working and you remember why<br>
      Day 14: Extended the tool twice already
    </div>
  </div>
</div>

<div class="highlight">

**The minimum viable project rule:** before finishing a learning session, identify the smallest possible thing you can build with what you just learned. Not a tutorial project — something with your own data, your own problem.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Learn On Demand, Not Upfront

Most technical knowledge you'll ever use, you'll acquire the moment you need it — not in advance.

<div class="demand-flow">
  <div class="df-row">
    <span class="df-badge need">Need</span>
    <span class="df-text">You hit a specific problem while building. <span>"How do I read only certain columns from a CSV?"</span></span>
  </div>
  <div class="df-row">
    <span class="df-badge search">Search</span>
    <span class="df-text">Google / ask Claude / check docs. You find <span>pd.read_csv(usecols=[...])</span> in 60 seconds.</span>
  </div>
  <div class="df-row">
    <span class="df-badge learn">Learn</span>
    <span class="df-text">You read exactly what you need — not the whole docs page. Context makes it stick immediately.</span>
  </div>
  <div class="df-row">
    <span class="df-badge build">Build</span>
    <span class="df-text">You apply it now, in your actual project. The learning is anchored to a real outcome.</span>
  </div>
  <div class="df-row">
    <span class="df-badge keep">Keep</span>
    <span class="df-text">You remember it because you used it. Not because you wrote it in a notebook three months ago.</span>
  </div>
</div>

<div class="highlight warn">

This is also how AI accelerates learning — you get exactly the concept you need, explained for your level, in the context of your actual problem. That's more efficient than any course.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## Spaced Repetition for Retention

Passive review kills retention. Spaced repetition — revisiting at increasing intervals — is the most effective known method for long-term retention.

<div class="rep-schedule">
  <div class="rep-card d1">
    <div class="rc-when">Day 1</div>
    <div class="rc-day">Learn</div>
    <div class="rc-action">Build something with it immediately. Don't just read.</div>
  </div>
  <div class="rep-card d3">
    <div class="rc-when">Day 3</div>
    <div class="rc-day">Use</div>
    <div class="rc-action">Apply the concept again in a slightly different context.</div>
  </div>
  <div class="rep-card d7">
    <div class="rc-when">Day 7</div>
    <div class="rc-day">Recall</div>
    <div class="rc-action">Write or explain the concept from memory before checking.</div>
  </div>
  <div class="rep-card d14">
    <div class="rc-when">Day 14</div>
    <div class="rc-day">Teach</div>
    <div class="rc-action">Explain it to someone else or write a short post about it.</div>
  </div>
  <div class="rep-card d30">
    <div class="rc-when">Day 30</div>
    <div class="rc-day">Own</div>
    <div class="rc-action">It's in long-term memory. You now know this permanently.</div>
  </div>
</div>

<div class="highlight good">

**Writing about what you learn** is the most underrated retention technique. Every Substack post, LinkedIn carousel, or tutorial you create about a concept locks it in more thoroughly than any amount of passive review.

</div>

---

## The Full System

<div class="two-col">
  <div class="col-card">
    <div class="label">The 5-step framework</div>
    <p style="font-size:14px; margin-top:8px; color:#374151; line-height:2;">
      <strong>1.</strong> Identify the core 20% — ask practitioners or use AI<br>
      <strong>2.</strong> Learn just that 20% — ignore everything else for now<br>
      <strong>3.</strong> Build something with your own data immediately<br>
      <strong>4.</strong> Learn the remaining concepts on demand as you need them<br>
      <strong>5.</strong> Review at Day 3, 7, 14, 30 — and teach what you learned
    </p>
  </div>
  <div class="col-card">
    <div class="label">Real timelines with this method</div>
    <p style="font-size:14px; margin-top:8px; color:#374151; line-height:2;">
      ✦ Productive in Python: <strong>3–5 days</strong><br>
      ✦ Productive in pandas: <strong>2–3 days</strong><br>
      ✦ Productive in Git: <strong>1 day</strong><br>
      ✦ Productive in Terminal: <strong>half a day</strong><br>
      ✦ Productive in HTML/CSS: <strong>2–3 days</strong>
    </p>
  </div>
</div>

---

<!-- _class: final -->

# Learn the 20%.
# Build immediately.
# Fill the rest in as you go.

&nbsp;

Mastery is not a prerequisite for productivity. Productivity is the path to mastery.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*