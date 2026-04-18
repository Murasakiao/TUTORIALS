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

  /* Framework card — full-width anatomy block */
  .framework-card {
    border-radius: 12px;
    padding: 20px 24px;
    margin: 14px 0;
  }

  .framework-card.rtf   { background: #111827; border: 2px solid #1d4ed8; }
  .framework-card.cot   { background: #111827; border: 2px solid #7c3aed; }
  .framework-card.few   { background: #111827; border: 2px solid #166534; }
  .framework-card.step  { background: #111827; border: 2px solid #92400e; }
  .framework-card.neg   { background: #111827; border: 2px solid #9d174d; }

  .framework-card .fc-header {
    display: flex;
    align-items: baseline;
    gap: 12px;
    margin-bottom: 10px;
  }

  .framework-card .fc-abbr {
    font-family: 'DM Mono', monospace;
    font-size: 18px;
    font-weight: 700;
  }

  .framework-card.rtf  .fc-abbr { color: #60a5fa; }
  .framework-card.cot  .fc-abbr { color: #c4b5fd; }
  .framework-card.few  .fc-abbr { color: #86efac; }
  .framework-card.step .fc-abbr { color: #fde68a; }
  .framework-card.neg  .fc-abbr { color: #f9a8d4; }

  .framework-card .fc-name {
    font-size: 14px;
    font-weight: 600;
    color: #9ca3af;
  }

  .framework-card .fc-body {
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    color: #d1d5db;
    line-height: 1.8;
  }

  .framework-card .fc-body .fc-hl-blue   { color: #60a5fa; font-weight: 600; }
  .framework-card .fc-body .fc-hl-purple { color: #c4b5fd; font-weight: 600; }
  .framework-card .fc-body .fc-hl-green  { color: #86efac; font-weight: 600; }
  .framework-card .fc-body .fc-hl-yellow { color: #fde68a; font-weight: 600; }
  .framework-card .fc-body .fc-hl-pink   { color: #f9a8d4; font-weight: 600; }

  /* Chat bubbles */
  .chat-mock {
    background: #111827;
    border-radius: 10px;
    padding: 14px 18px;
    margin: 10px 0;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
  }

  .chat-row {
    display: flex;
    gap: 10px;
    align-items: flex-start;
    margin-bottom: 8px;
  }

  .chat-row:last-child { margin-bottom: 0; }

  .chat-avatar {
    width: 26px;
    height: 26px;
    border-radius: 50%;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
    margin-top: 2px;
  }

  .chat-avatar.user { background: #374151; }
  .chat-avatar.ai   { background: #1d4ed8; }

  .chat-bubble {
    border-radius: 8px;
    padding: 9px 13px;
    line-height: 1.6;
    flex: 1;
    font-size: 13px;
  }

  .chat-bubble.user-msg  { background: #1e3a5f; border: 1px solid #1d4ed8; color: #bfdbfe; }
  .chat-bubble.ai-msg    { background: #1f2937; border: 1px solid #374151; color: #9ca3af; font-style: italic; }
  .chat-bubble.user-good { background: #14532d; border: 1px solid #166534; color: #bbf7d0; }
  .chat-bubble.ai-good   { background: #1e3a5f; border: 1px solid #1d4ed8; color: #bfdbfe; font-style: italic; }

  .chat-bubble .bubble-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 3px;
    font-style: normal;
    color: #4b5563;
  }

  /* When-to-use decision table */
  .decision-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
    margin: 14px 0;
  }

  .decision-table th {
    background: var(--text);
    color: white;
    padding: 9px 14px;
    text-align: left;
    font-weight: 500;
    font-size: 12px;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.05em;
  }

  .decision-table td {
    padding: 9px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
    vertical-align: top;
  }

  .decision-table tr:nth-child(even) td { background: var(--off-white); }

  .decision-table .fw-tag {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 4px;
    display: inline-block;
  }

  .fw-tag.rtf  { background: #1e3a5f; color: #60a5fa; }
  .fw-tag.cot  { background: #2e1065; color: #c4b5fd; }
  .fw-tag.few  { background: #14532d; color: #86efac; }
  .fw-tag.step { background: #451a03; color: #fde68a; }
  .fw-tag.neg  { background: #4c0519; color: #f9a8d4; }

  /* 5-framework overview grid */
  .fw-overview {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin: 14px 0;
  }

  .fw-overview-card {
    border-radius: 8px;
    padding: 13px 16px;
    display: flex;
    gap: 12px;
    align-items: flex-start;
  }

  .fw-overview-card.rtf  { background: #1e3a5f; border: 1px solid #1d4ed8; }
  .fw-overview-card.cot  { background: #2e1065; border: 1px solid #7c3aed; }
  .fw-overview-card.few  { background: #14532d; border: 1px solid #166534; }
  .fw-overview-card.step { background: #451a03; border: 1px solid #92400e; }
  .fw-overview-card.neg  { background: #4c0519; border: 1px solid #9d174d; }

  .fw-overview-card .foc-abbr {
    font-family: 'DM Mono', monospace;
    font-size: 16px;
    font-weight: 700;
    min-width: 48px;
    padding-top: 1px;
    flex-shrink: 0;
  }

  .fw-overview-card.rtf  .foc-abbr { color: #60a5fa; }
  .fw-overview-card.cot  .foc-abbr { color: #c4b5fd; }
  .fw-overview-card.few  .foc-abbr { color: #86efac; }
  .fw-overview-card.step .foc-abbr { color: #fde68a; }
  .fw-overview-card.neg  .foc-abbr { color: #f9a8d4; }

  .fw-overview-card .foc-body .foc-name { font-size: 13px; font-weight: 600; color: #f0f6fc; margin-bottom: 2px; }
  .fw-overview-card .foc-body .foc-desc { font-size: 12px; color: #9ca3af; line-height: 1.4; }

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

# The 5 Prompt Frameworks
## Everyone Should Know

&nbsp;

**Most people write prompts. These people write systems.**

`RTF` · `Chain-of-Thought` · `Few-Shot` · `Step-by-Step` · `Negative Prompting`

---

## Why Frameworks Matter

A framework is a reusable structure that reliably produces a certain type of output.

<div class="tools">
  <div class="tool-card">
    <div class="icon">🧠</div>
    <div class="name">Reduces cognitive load</div>
    <div class="desc">You don't reinvent the prompt every time — you pick the right frame and fill it in.</div>
  </div>
  <div class="tool-card">
    <div class="icon">📐</div>
    <div class="name">Predictable outputs</div>
    <div class="desc">The same framework applied to different tasks produces consistently structured results.</div>
  </div>
  <div class="tool-card">
    <div class="icon">⚡</div>
    <div class="name">Faster iteration</div>
    <div class="desc">When a result is wrong, you know which part of the framework to adjust — not just "try something else."</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔁</div>
    <div name="name">Reusable across tasks</div>
    <div class="desc">Write once, adapt forever. The same RTF frame works for a blog post, an email, or a code review.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">FRAMEWORK 01</div>

## RTF — Role · Task · Format

The simplest universal framework. Three slots, any task.

<div class="framework-card rtf">
  <div class="fc-header">
    <span class="fc-abbr">RTF</span>
    <span class="fc-name">Role · Task · Format</span>
  </div>
  <div class="fc-body">
    <span class="fc-hl-blue">Role:</span> You are a direct, no-fluff copywriter who writes for technical audiences.<br>
    <span class="fc-hl-blue">Task:</span> Write a 3-sentence product description for a Python automation course aimed at engineers.<br>
    <span class="fc-hl-blue">Format:</span> Plain paragraph. No bullet points. No exclamation marks.
  </div>
</div>

<div class="two-col">
  <div class="col-card">
    <div class="label">When to use RTF</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">Any creative or communication task — emails, posts, summaries, descriptions, headlines. The default framework when you're not sure which to pick.</p>
  </div>
  <div class="col-card">
    <div class="label">The key insight</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;"><strong>Format</strong> is the most underused slot. Specifying "bullet list", "table", "two paragraphs", or "one sentence" changes the output more than any other variable.</p>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">FRAMEWORK 02</div>

## Chain-of-Thought — Make It Reason First

Asking the model to show its reasoning before answering dramatically improves accuracy on complex tasks.

<div class="framework-card cot">
  <div class="fc-header">
    <span class="fc-abbr">CoT</span>
    <span class="fc-name">Chain-of-Thought</span>
  </div>
  <div class="fc-body">
    <span class="fc-hl-purple">Without CoT:</span> "Which of these three business models is most viable for a solo creator?"<br><br>
    <span class="fc-hl-purple">With CoT:</span> "Which of these three business models is most viable for a solo creator? <br>Think through the pros and cons of each before giving your recommendation."
  </div>
</div>

- The phrase **"think step by step"** or **"reason through this before answering"** activates CoT
- Works best for: logic problems, tradeoff analysis, code debugging, multi-variable decisions
- The reasoning process often reveals assumptions you didn't know you were making

<div class="highlight">

**Why it works:** the model generates better answers when it externalises reasoning — the same way humans think better when they write things down.

</div>

---

<!-- _class: step -->

<div class="step-badge">FRAMEWORK 03</div>

## Few-Shot — Show, Don't Just Tell

Give the model 2–3 examples of the output you want. It pattern-matches from them.

<div class="framework-card few">
  <div class="fc-header">
    <span class="fc-abbr">Few-Shot</span>
    <span class="fc-name">Example-driven prompting</span>
  </div>
  <div class="fc-body">
    <span class="fc-hl-green">Convert feature → benefit. Follow this pattern:</span><br>
    Feature: 256GB storage → Benefit: Never delete a photo again.<br>
    Feature: 5000mAh battery → Benefit: Two full days without hunting for a charger.<br>
    Feature: IP68 waterproof → Benefit: Drop it in a pool. It won't care.<br><br>
    <span class="fc-hl-green">Now do this one:</span><br>
    Feature: 120Hz display → Benefit: <span style="color:#4b5563; font-style:italic;">[ model continues the pattern ]</span>
  </div>
</div>

<div class="highlight good">

**The rule of three:** two examples set a weak pattern. Three lock it in reliably. More than five adds noise without improving output. Two or three is almost always enough.

</div>

---

<!-- _class: step -->

<div class="step-badge">FRAMEWORK 04</div>

## Step-by-Step — Break It Into Stages

For complex tasks, instruct the model to work through a sequence — one stage at a time.

<div class="framework-card step">
  <div class="fc-header">
    <span class="fc-abbr">Step-by-Step</span>
    <span class="fc-name">Sequential task decomposition</span>
  </div>
  <div class="fc-body">
    <span class="fc-hl-yellow">Analyse this job description and help me write a tailored cover letter.</span><br>
    Do this in three stages:<br>
    1. List the 5 most important requirements from the job description.<br>
    2. Match each requirement to a specific skill or experience I have (I'll provide my CV).<br>
    3. Write a 200-word cover letter using those matches as the core argument.<br><br>
    <span style="color:#6b7280;">Start with stage 1 only. Wait for my confirmation before continuing.</span>
  </div>
</div>

"**Wait for my confirmation before continuing**" keeps you in the loop — you can course-correct between stages instead of getting a wall of text to fix at the end.

---

<!-- _class: step -->

<div class="step-badge">FRAMEWORK 05</div>

## Negative Prompting — Tell It What Not to Do

Excluding unwanted patterns is often more efficient than describing what you want.

<div class="framework-card neg">
  <div class="fc-header">
    <span class="fc-abbr">Negative</span>
    <span class="fc-name">Exclusion-based prompting</span>
  </div>
  <div class="fc-body">
    <span class="fc-hl-pink">Write a LinkedIn post about launching my automation tool.</span><br>
    Do not use: "excited to share", "journey", "game-changer", "thrilled", "proud to announce".<br>
    Do not use exclamation marks.<br>
    Do not open with "I".<br>
    Do not mention the word "passionate".
  </div>
</div>

<div class="two-col">
  <div class="col-card">
    <div class="label">Why this works</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">AI defaults to the most common patterns in its training data. Negative prompting explicitly blocks those patterns — forcing less generic output.</p>
  </div>
  <div class="col-card">
    <div class="label">Combine with RTF</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">Negative prompting works best as an addition to RTF — not as a standalone. Set the role and task first, then add the exclusion list.</p>
  </div>
</div>

---

## When to Use Which

<table class="decision-table">
  <tr>
    <th>Situation</th>
    <th>Framework</th>
    <th>Why</th>
  </tr>
  <tr>
    <td>Writing, emails, posts, summaries</td>
    <td><span class="fw-tag rtf">RTF</span></td>
    <td>Default framework — works for almost any communication task</td>
  </tr>
  <tr>
    <td>Logic, tradeoffs, debugging, decisions</td>
    <td><span class="fw-tag cot">CoT</span></td>
    <td>Forces reasoning before conclusion — reduces confident wrong answers</td>
  </tr>
  <tr>
    <td>Matching a specific tone or style</td>
    <td><span class="fw-tag few">Few-Shot</span></td>
    <td>Faster than describing the style in words — show it instead</td>
  </tr>
  <tr>
    <td>Multi-stage research or writing tasks</td>
    <td><span class="fw-tag step">Step-by-Step</span></td>
    <td>Keeps you in control between stages — catch errors early</td>
  </tr>
  <tr>
    <td>Output sounds generic or AI-ish</td>
    <td><span class="fw-tag neg">Negative</span></td>
    <td>Explicitly blocks the default patterns that make AI text recognisable</td>
  </tr>
  <tr>
    <td>High-stakes or complex tasks</td>
    <td><span class="fw-tag rtf">RTF</span> + <span class="fw-tag cot">CoT</span> + <span class="fw-tag neg">Negative</span></td>
    <td>Stack frameworks — they combine cleanly and rarely conflict</td>
  </tr>
</table>

---

<!-- _class: final -->

# Five frameworks.
# Every prompt covered.

&nbsp;

RTF · Chain-of-Thought · Few-Shot · Step-by-Step · Negative

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*