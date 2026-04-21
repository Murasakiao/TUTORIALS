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

  /* System prompt block */
  .system-block {
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
  }

  .system-bar {
    background: #161b22;
    padding: 8px 16px;
    border-bottom: 1px solid #30363d;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .system-bar .sb-icon { font-size: 13px; }

  .system-bar .sb-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #6b7280;
  }

  .system-bar .sb-tag {
    margin-left: auto;
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    padding: 2px 8px;
    border-radius: 999px;
  }

  .system-bar .sb-tag.planner { background: #1e3a5f; color: #60a5fa; }
  .system-bar .sb-tag.coder   { background: #14532d; color: #86efac; }
  .system-bar .sb-tag.generic { background: #374151; color: #9ca3af; }

  .system-body {
    padding: 16px 20px;
    line-height: 2;
    color: #d1d5db;
  }

  .system-body .sp-role       { color: #f9a8d4; font-weight: 600; }
  .system-body .sp-rule       { color: #fde68a; }
  .system-body .sp-context    { color: #60a5fa; }
  .system-body .sp-constraint { color: #c4b5fd; }
  .system-body .sp-format     { color: #86efac; }
  .system-body .sp-plain      { color: #d1d5db; }

  /* Chat mock */
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

  .chat-bubble.user-msg { background: #1e3a5f; border: 1px solid #1d4ed8; color: #bfdbfe; }
  .chat-bubble.ai-msg   { background: #1f2937; border: 1px solid #374151; color: #9ca3af; font-style: italic; }
  .chat-bubble.ai-good  { background: #14532d; border: 1px solid #166534; color: #bbf7d0; font-style: italic; }

  .chat-bubble .bubble-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 3px;
    font-style: normal;
    color: #4b5563;
  }

  /* Before/after split */
  .before-after {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 16px 0;
  }

  .ba-card {
    border-radius: 10px;
    overflow: hidden;
  }

  .ba-card .ba-label {
    padding: 7px 14px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 600;
  }

  .ba-card.before .ba-label { background: #7f1d1d; color: #fca5a5; }
  .ba-card.after  .ba-label { background: #14532d; color: #86efac; }

  .ba-card .ba-body {
    background: #0d1117;
    padding: 13px 16px;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    line-height: 1.8;
  }

  .ba-card.before .ba-body { border: 1px solid #7f1d1d; border-top: none; border-radius: 0 0 10px 10px; color: #fca5a5; }
  .ba-card.after  .ba-body { border: 1px solid #14532d; border-top: none; border-radius: 0 0 10px 10px; color: #86efac; }

  /* Context block */
  .context-block {
    background: #111827;
    border-radius: 10px;
    padding: 16px 20px;
    margin: 12px 0;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
  }

  .context-block .cb-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #4b5563;
    margin-bottom: 10px;
  }

  .context-row {
    display: flex;
    align-items: baseline;
    gap: 10px;
    margin-bottom: 6px;
  }

  .context-row .cr-key {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: #60a5fa;
    min-width: 100px;
    flex-shrink: 0;
  }

  .context-row .cr-val {
    font-size: 13px;
    color: #d1d5db;
    line-height: 1.5;
  }

  /* Two-col */
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

  /* step list */
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

# Turn ChatGPT into a
## Personal Assistant

&nbsp;

**Default ChatGPT answers questions. A configured one works for you.**

`system prompt` · `role` · `rules` · `context` · `memory`

---

## Why Default ChatGPT is Underpowered

Out of the box, ChatGPT is a generic responder — polite, verbose, and calibrated for the average user. Not you.

<div class="tools">
  <div class="tool-card">
    <div class="icon">🌐</div>
    <div class="name">No role context</div>
    <div class="desc">It doesn't know if you're a student, an engineer, or a solo founder — so it writes for everyone, which means no one.</div>
  </div>
  <div class="tool-card">
    <div class="icon">📜</div>
    <div class="name">Defaults to long answers</div>
    <div class="desc">Without constraints, it fills the page. You spend more time editing than thinking.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔁</div>
    <div class="name">No memory of your context</div>
    <div class="desc">Every new chat starts cold. It doesn't know your stack, your goals, or how you like to work.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🧰</div>
    <div class="name">The fix is a system prompt</div>
    <div class="desc">A well-written system prompt turns a generic chatbot into a specialist that knows who you are and how to help.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Give It a Role

The single highest-leverage thing you can do: tell it who it is before you ask it anything.

<div class="before-after">
  <div class="ba-card before">
    <div class="ba-label">❌ Default — no role</div>
    <div class="ba-body">ChatGPT responds as a helpful general assistant. Measured tone, hedged language, covers all angles whether you need them or not.</div>
  </div>
  <div class="ba-card after">
    <div class="ba-label">✅ With role assigned</div>
    <div class="ba-body">You are a direct, senior software engineer who prefers concise answers with working code examples. Skip preamble. If something has a better approach, say so.</div>
  </div>
</div>

<div class="highlight">

**Where to set this:** in ChatGPT, go to **Settings → Personalization → Custom Instructions** (top box). This persists across all conversations automatically — you write it once and it applies everywhere.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Set Rules and Constraints

Rules eliminate the behaviors that waste your time most.

<div class="system-block">
  <div class="system-bar">
    <span class="sb-icon">⚙️</span>
    <span class="sb-label">Custom Instructions — Rules</span>
    <span class="sb-tag generic">always applied</span>
  </div>
  <div class="system-body">
    <span class="sp-rule">Never start a response with "Great question!" or "Certainly!"</span><br>
    <span class="sp-rule">Never use bullet points unless I ask for them.</span><br>
    <span class="sp-rule">Keep answers under 150 words unless I ask for more.</span><br>
    <span class="sp-rule">If I ask for code, give me the code first — explanation after, if needed.</span><br>
    <span class="sp-rule">If you're unsure, say so instead of guessing confidently.</span>
  </div>
</div>

<div class="two-col">
  <div class="col-card">
    <div class="label">Most useful rules</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">No filler openers · enforce brevity · code-first · no unsolicited caveats · ask clarifying questions before writing</p>
  </div>
  <div class="col-card">
    <div class="label">Rules to avoid</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">Too many rules conflict with each other. Keep it to 5–7. Review and prune every few weeks as your needs change.</p>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Add Memory and Context

Tell it about you once — so you never have to repeat yourself.

<div class="context-block">
  <div class="cb-label">📋 Custom Instructions — About You (bottom box)</div>
  <div class="context-row">
    <span class="cr-key">Profession:</span>
    <span class="cr-val">Knowledge worker managing multiple cross-functional projects.</span>
  </div>
  <div class="context-row">
    <span class="cr-key">Toolkit:</span>
    <span class="cr-val">Notion, Slack, Google Workspace, and basic project management software.</span>
  </div>
  <div class="context-row">
    <span class="cr-key">Writing:</span>
    <span class="cr-val">Professional yet conversational. Clear, active voice without fluff or buzzwords.</span>
  </div>
  <div class="context-row">
    <span class="cr-key">Preferences:</span>
    <span class="cr-val">Direct answers. Scannable formatting. Bolded key terms. No motivational commentary.</span>
  </div>
  <div class="context-row">
    <span class="cr-key">Avoid:</span>
    <span class="cr-val">Suggesting overly complex frameworks or tools I didn't ask for.</span>
  </div>
</div>


This context lives in ChatGPT's Custom Instructions and applies silently to every conversation — no repasting needed.

---

<!-- _class: step -->

<div class="step-badge">EXAMPLE 01</div>

## Daily Planner Assistant

A configured assistant that turns a brain dump into a structured day plan:

<div class="system-block">
  <div class="system-bar">
    <span class="sb-icon">📅</span>
    <span class="sb-label">System Prompt</span>
    <span class="sb-tag planner">planner</span>
  </div>
  <div class="system-body">
    <span class="sp-role">You are a calm, no-nonsense daily planning assistant.</span><br>
    <span class="sp-plain">When I give you a list of tasks, you will:</span><br>
    <span class="sp-format">1. Group them into: Deep Work / Admin / Comms</span><br>
    <span class="sp-format">2. Suggest a time block order based on energy (deep work in the morning)</span><br>
    <span class="sp-constraint">3. Flag anything that should be delegated or dropped</span><br>
    <span class="sp-rule">Keep the output to a single structured list. No motivational commentary.</span>
  </div>
</div>

<div class="chat-mock">
  <div class="chat-row">
    <div class="chat-avatar user">👤</div>
    <div class="chat-bubble user-msg">Write tutorial slides, reply to 3 emails, fix CSV bug, review N-1 results, post on Threads, update portfolio site.</div>
  </div>
  <div class="chat-row">
    <div class="chat-avatar ai">✦</div>
    <div class="chat-bubble ai-good">Deep Work: Fix CSV bug · Review N-1 results · Write tutorial slides — Admin: Update portfolio · Comms: Reply to 3 emails · Post on Threads — Consider: Post on Threads → schedule instead of doing manually.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">EXAMPLE 02</div>

## Coding Assistant

A system prompt that turns ChatGPT into a Python pair-programmer who knows your stack:

<div class="system-block">
  <div class="system-bar">
    <span class="sb-icon">💻</span>
    <span class="sb-label">System Prompt</span>
    <span class="sb-tag coder">coding</span>
  </div>
  <div class="system-body">
    <span class="sp-role">You are a senior Python engineer and pair-programmer.</span><br>
    <span class="sp-context">My stack: Python 3.11, pandas, Flask, pandapower. I work on power systems analysis and automation scripts.</span><br>
    <span class="sp-rule">Always give working, runnable code. No pseudocode unless I ask.</span><br>
    <span class="sp-rule">Add inline comments to non-obvious lines only — not every line.</span><br>
    <span class="sp-constraint">If my approach has a better alternative, say so briefly before writing my version.</span><br>
    <span class="sp-rule">Never wrap code in prose. Code block first, short explanation after if needed.</span>
  </div>
</div>

<div class="chat-mock">
  <div class="chat-row">
    <div class="chat-avatar user">👤</div>
    <div class="chat-bubble user-msg">Write a function that reads a CSV, filters rows where voltage_pu &lt; 0.95, and returns a sorted DataFrame.</div>
  </div>
  <div class="chat-row">
    <div class="chat-avatar ai">✦</div>
    <div class="chat-bubble ai-good">Note: consider using .query() for readability — but here's your version: [code block with inline comments on non-obvious lines only]</div>
  </div>
</div>

---

## The Setup Checklist

Everything you need to configure once and benefit from forever:

<ul class="step-list">
  <li>Go to <strong>ChatGPT → Settings → Personalization → Custom Instructions</strong></li>
  <li><strong>Top box (how to respond):</strong> add your role, rules, and format preferences — 5 to 7 rules maximum</li>
  <li><strong>Bottom box (about you):</strong> add your profession, stack, writing style, and what to avoid</li>
  <li>Test with a real task — check if it's shorter, more direct, and more on-target than default</li>
  <li>Save a copy of your system prompts in a text file — you'll want to reuse them in new tools</li>
  <li>Review and update monthly — your context changes, your instructions should too</li>
</ul>

<div class="highlight warn">

**Note:** Custom Instructions apply to ChatGPT's web and mobile app. For API use, pass these as the `system` message. For Claude, use the equivalent settings in Personalization or paste at the start of a conversation.

</div>

---

<!-- _class: final -->

# Same tool.
# Completely different results.

&nbsp;

The gap between default ChatGPT and a configured one is wider than most people realise.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*