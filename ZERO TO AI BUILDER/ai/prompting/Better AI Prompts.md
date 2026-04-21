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

  /* Prompt bubble — chat UI mock */
  .chat-mock {
    background: #111827;
    border-radius: 10px;
    padding: 16px 20px;
    margin: 12px 0;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
  }

  .chat-row {
    display: flex;
    gap: 10px;
    align-items: flex-start;
    margin-bottom: 10px;
  }

  .chat-row:last-child { margin-bottom: 0; }

  .chat-avatar {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 13px;
    margin-top: 2px;
  }

  .chat-avatar.user { background: #374151; }
  .chat-avatar.ai   { background: #1d4ed8; }

  .chat-bubble {
    border-radius: 10px;
    padding: 10px 14px;
    line-height: 1.6;
    flex: 1;
  }

  .chat-bubble.user-bad {
    background: #7f1d1d;
    border: 1px solid #991b1b;
    color: #fca5a5;
  }

  .chat-bubble.user-good {
    background: #14532d;
    border: 1px solid #166534;
    color: #bbf7d0;
  }

  .chat-bubble.ai-bad {
    background: #1f2937;
    border: 1px solid #374151;
    color: #9ca3af;
    font-style: italic;
  }

  .chat-bubble.ai-good {
    background: #1e3a5f;
    border: 1px solid #1d4ed8;
    color: #bfdbfe;
    font-style: italic;
  }

  .chat-bubble .bubble-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 4px;
    font-style: normal;
  }

  .chat-bubble.user-bad  .bubble-label { color: #f87171; }
  .chat-bubble.user-good .bubble-label { color: #86efac; }
  .chat-bubble.ai-bad    .bubble-label { color: #6b7280; }
  .chat-bubble.ai-good   .bubble-label { color: #60a5fa; }

  /* Formula pill strip */
  .formula-strip {
    display: grid;
    grid-template-columns: 1fr auto 1fr auto 1fr;
    gap: 0;
    align-items: center;
    margin: 20px 0;
  }

  .formula-pill {
    border-radius: 10px;
    padding: 16px 18px;
    text-align: center;
  }

  .formula-pill.clear     { background: #1e3a5f; border: 2px solid #2563eb; }
  .formula-pill.context   { background: #14532d; border: 2px solid #16a34a; }
  .formula-pill.constraint{ background: #4c1d95; border: 2px solid #7c3aed; }

  .formula-pill .fp-word {
    font-family: 'DM Mono', monospace;
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 4px;
  }

  .formula-pill.clear      .fp-word { color: #60a5fa; }
  .formula-pill.context    .fp-word { color: #86efac; }
  .formula-pill.constraint .fp-word { color: #c4b5fd; }

  .formula-pill .fp-desc {
    font-size: 12px;
    line-height: 1.4;
  }

  .formula-pill.clear      .fp-desc { color: #93c5fd; }
  .formula-pill.context    .fp-desc { color: #6ee7b7; }
  .formula-pill.constraint .fp-desc { color: #a78bfa; }

  .formula-plus {
    font-size: 22px;
    color: #374151;
    text-align: center;
    padding: 0 10px;
  }

  /* Role/goal/format anatomy */
  .anatomy-block {
    background: #111827;
    border-radius: 10px;
    padding: 18px 22px;
    margin: 14px 0;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    line-height: 1.9;
    color: #e5e7eb;
    position: relative;
  }

  .anatomy-block .ab-role       { color: #f9a8d4; font-weight: 600; }
  .anatomy-block .ab-goal       { color: #86efac; font-weight: 600; }
  .anatomy-block .ab-context    { color: #60a5fa; font-weight: 600; }
  .anatomy-block .ab-constraint { color: #fde68a; font-weight: 600; }
  .anatomy-block .ab-format     { color: #c4b5fd; font-weight: 600; }
  .anatomy-block .ab-plain      { color: #e5e7eb; }

  /* Anatomy legend */
  .anatomy-legend {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
    margin-top: 12px;
  }

  .legend-item {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 12px;
    font-family: 'DM Mono', monospace;
  }

  .legend-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    flex-shrink: 0;
  }

  /* Iteration strip */
  .iter-strip {
    display: grid;
    grid-template-columns: 1fr auto 1fr auto 1fr;
    gap: 0;
    align-items: center;
    margin: 18px 0;
  }

  .iter-card {
    background: #111827;
    border-radius: 8px;
    padding: 14px 16px;
    text-align: center;
  }

  .iter-card .ic-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 6px;
  }

  .iter-card.v1 .ic-label { color: #f87171; }
  .iter-card.v2 .ic-label { color: #fde68a; }
  .iter-card.v3 .ic-label { color: #86efac; }

  .iter-card .ic-text {
    font-size: 12px;
    color: #9ca3af;
    line-height: 1.5;
  }

  .iter-arrow {
    font-size: 20px;
    color: #374151;
    text-align: center;
    padding: 0 8px;
  }

  /* Template block */
  .template-block {
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 10px;
    padding: 20px 24px;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    line-height: 2;
    margin: 14px 0;
    color: #e5e7eb;
  }

  .template-block .tb-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #6b7280;
    margin-bottom: 12px;
  }

  .template-block .tb-role       { color: #f9a8d4; }
  .template-block .tb-goal       { color: #86efac; }
  .template-block .tb-context    { color: #60a5fa; }
  .template-block .tb-constraint { color: #fde68a; }
  .template-block .tb-format     { color: #c4b5fd; }
  .template-block .tb-blank      { color: #4b5563; font-style: italic; }

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

# Write Better AI Prompts
## That Actually Work

&nbsp;

**The output is only as good as the input.** Most people never learn this.

`role` · `goal` · `context` · `constraint` · `format`

---

## Why Vague Prompts Fail

AI doesn't guess what you mean — it responds to what you write. Vague in, vague out.

<div class="tools">
  <div class="tool-card">
    <div class="icon">🌫️</div>
    <div class="name">No target</div>
    <div class="desc">"Write me something about productivity" — something for who? What length? What angle?</div>
  </div>
  <div class="tool-card">
    <div class="icon">🎭</div>
    <div class="name">No role assigned</div>
    <div class="desc">Without a role, the model picks one itself — often the most generic possible answer.</div>
  </div>
  <div class="tool-card">
    <div class="icon">📏</div>
    <div class="name">No constraints</div>
    <div class="desc">No word count, no tone, no format — so you get the model's default, not yours.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔁</div>
    <div class="name">Wasted iterations</div>
    <div class="desc">A vague prompt means three rounds of "make it shorter / more casual / less generic" that a good first prompt prevents.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## The "Clear + Context + Constraint" Formula

Every good prompt answers three questions before the AI starts generating.

<div class="formula-strip">
  <div class="formula-pill clear">
    <div class="fp-word">Clear</div>
    <div class="fp-desc">What exactly do you want? Be specific about the task.</div>
  </div>
  <div class="formula-plus">+</div>
  <div class="formula-pill context">
    <div class="fp-word">Context</div>
    <div class="fp-desc">Who is it for? What situation? What background matters?</div>
  </div>
  <div class="formula-plus">+</div>
  <div class="formula-pill constraint">
    <div class="fp-word">Constraint</div>
    <div class="fp-desc">How long? What tone? What format? What to avoid?</div>
  </div>
</div>

<div class="highlight">

**The test:** read your prompt and ask — could someone else write ten very different responses to this? If yes, it needs more specificity. A good prompt narrows the solution space before the model enters it.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Bad vs Good Prompt Examples

<div class="chat-mock">
  <div class="chat-row">
    <div class="chat-avatar user">👤</div>
    <div class="chat-bubble user-bad">
      <div class="bubble-label">❌ Vague prompt</div>
      Write a LinkedIn post about my project.
    </div>
  </div>
  <div class="chat-row">
    <div class="chat-avatar ai">✦</div>
    <div class="chat-bubble ai-bad">
      <div class="bubble-label">AI response</div>
      Excited to share my latest project! It's been a challenging but rewarding journey. Looking forward to hearing your thoughts! #Innovation #Work
    </div>
  </div>
</div>

<div class="chat-mock">
  <div class="chat-row">
    <div class="chat-avatar user">👤</div>
    <div class="chat-bubble user-good">
      <div class="bubble-label">✅ Specific prompt</div>
      Write a LinkedIn post announcing my Python automation tool that renames 100 files in under a second. Audience: engineers and tech-curious professionals. Tone: direct, no hype. End with a question. Max 120 words.
    </div>
  </div>
  <div class="chat-row">
    <div class="chat-avatar ai">✦</div>
    <div class="chat-bubble ai-good">
      <div class="bubble-label">AI response</div>
      Built a Python script that renames 100 files in under a second — no clicks, no typos, no drag-and-drop. 20 lines of code, runs on any folder. The kind of thing that takes 10 minutes to write and saves hours every month. What repetitive file task would you automate first?
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Add Role + Goal + Format

The most reliable upgrade to any prompt: tell the AI what it is, what you need, and how to deliver it.

<div class="anatomy-block">
  <span class="ab-role">You are a senior technical writer</span><span class="ab-plain"> who specialises in beginner-friendly tutorials.</span><br>
  <span class="ab-goal">Write a step-by-step guide on how to set up a Python virtual environment</span><span class="ab-plain">.</span><br>
  <span class="ab-context">The reader has just installed Python for the first time and has basic Terminal knowledge.</span><br>
  <span class="ab-constraint">Keep it under 300 words. Avoid jargon. Don't explain what Python is — assume they know.</span><br>
  <span class="ab-format">Format as numbered steps. Include the exact commands to run in code blocks.</span>
</div>

<div class="anatomy-legend">
  <div class="legend-item"><div class="legend-dot" style="background:#f9a8d4"></div><span style="color:#f9a8d4">Role</span></div>
  <div class="legend-item"><div class="legend-dot" style="background:#86efac"></div><span style="color:#86efac">Goal</span></div>
  <div class="legend-item"><div class="legend-dot" style="background:#60a5fa"></div><span style="color:#60a5fa">Context</span></div>
  <div class="legend-item"><div class="legend-dot" style="background:#fde68a"></div><span style="color:#fde68a">Constraint</span></div>
  <div class="legend-item"><div class="legend-dot" style="background:#c4b5fd"></div><span style="color:#c4b5fd">Format</span></div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Iterating Prompts

A first prompt is a draft, not a final answer. Treat each response as a data point.

<div class="iter-strip">
  <div class="iter-card v1">
    <div class="ic-label">V1 — Too generic</div>
    <div class="ic-text">"Write a blog intro about habits." Result reads like every other habits post.</div>
  </div>
  <div class="iter-arrow">→</div>
  <div class="iter-card v2">
    <div class="ic-label">V2 — Add friction</div>
    <div class="ic-text">"Same, but open with a counterintuitive claim. No motivational language." Better hook, still safe.</div>
  </div>
  <div class="iter-arrow">→</div>
  <div class="iter-card v3">
    <div class="ic-label">V3 — Nail the voice</div>
    <div class="ic-text">"Rewrite in a direct, slightly wry tone. Short sentences. First person. Drop the word 'journey'." Now it sounds like a human.</div>
  </div>
</div>

<div class="two-col">
  <div class="col-card">
    <div class="label">What to add per iteration</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">Tone adjustment · length fix · specific thing to remove · example to match · angle to shift · audience to tighten</p>
  </div>
  <div class="col-card">
    <div class="label">What not to do</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">Don't start over — build on what worked. Don't add ten changes at once — one variable per iteration so you know what moved the needle.</p>
  </div>
</div>

---

## Reusable Prompt Template

Copy this structure. Fill in the brackets. Use it for any task.

<div class="template-block">
  <div class="tb-label">📋 Universal Prompt Template</div>
  <span class="tb-role">You are [role / expert type].</span><br>
  <span class="tb-goal">Your task is to [specific action verb] [specific deliverable].</span><br>
  <span class="tb-context">Context: [who it's for] + [relevant background or constraints].</span><br>
  <span class="tb-constraint">Requirements: [length] · [tone] · [what to avoid] · [what to include].</span><br>
  <span class="tb-format">Output format: [bullet list / numbered steps / prose / table / code block].</span><br>
  <br>
  <span class="tb-blank">— optionally add an example of the style or output you want —</span>
</div>

<div class="highlight good">

**Real example filled in:** *You are a concise technical educator. Your task is to explain what a REST API is. Context: the reader is a non-developer who builds no-code tools. Requirements: under 150 words, plain English, no acronyms without explanation. Output format: 3 short paragraphs.*

</div>

---

<!-- _class: final -->

# Better prompt.
# Better output.
# Less back and forth.

&nbsp;

Role + Goal + Context + Constraint + Format. Five ingredients. Every time.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*