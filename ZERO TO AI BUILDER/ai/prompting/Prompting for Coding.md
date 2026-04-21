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

  .highlight.danger {
    background: #fff1f2;
    border-color: #fecdd3;
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

  /* Code block */
  .code-block {
    background: #111827;
    border-radius: 8px;
    padding: 16px 22px;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #e5e7eb;
    line-height: 2;
    margin: 12px 0;
  }

  .code-block .kw  { color: #c4b5fd; }
  .code-block .fn  { color: #60a5fa; }
  .code-block .str { color: #86efac; }
  .code-block .var { color: #f9fafb; }
  .code-block .num { color: #fde68a; }
  .code-block .op  { color: #f9a8d4; }
  .code-block .cmt { color: #4b5563; font-style: italic; }
  .code-block .err { color: #f87171; }

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

  .chat-bubble.user-bad  { background: #7f1d1d; border: 1px solid #991b1b; color: #fca5a5; }
  .chat-bubble.user-good { background: #1e3a5f; border: 1px solid #1d4ed8; color: #bfdbfe; }
  .chat-bubble.ai-bad    { background: #1f2937; border: 1px solid #374151; color: #9ca3af; font-style: italic; }
  .chat-bubble.ai-good   { background: #14532d; border: 1px solid #166534; color: #bbf7d0; font-style: italic; }

  .chat-bubble .bubble-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 3px;
    font-style: normal;
    color: #4b5563;
  }

  /* Error block */
  .error-block {
    background: #0d1117;
    border: 1px solid #7f1d1d;
    border-radius: 10px;
    overflow: hidden;
    margin: 12px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .error-bar {
    background: #7f1d1d;
    padding: 7px 16px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .error-bar .eb-label {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #fca5a5;
    font-weight: 600;
  }

  .error-body {
    padding: 14px 18px;
    line-height: 2;
  }

  .error-body .el-trace { color: #6b7280; font-size: 12px; }
  .error-body .el-file  { color: #60a5fa; }
  .error-body .el-line  { color: #fde68a; }
  .error-body .el-msg   { color: #f87171; font-weight: 500; }

  /* Prompt anatomy */
  .prompt-anatomy {
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 10px;
    padding: 18px 22px;
    margin: 14px 0;
    font-family: 'DM Sans', sans-serif;
    font-size: 13.5px;
    line-height: 2;
    color: #e5e7eb;
  }

  .prompt-anatomy .pa-stack      { color: #60a5fa; font-weight: 600; }
  .prompt-anatomy .pa-task       { color: #86efac; font-weight: 600; }
  .prompt-anatomy .pa-input      { color: #fde68a; font-weight: 600; }
  .prompt-anatomy .pa-output     { color: #c4b5fd; font-weight: 600; }
  .prompt-anatomy .pa-constraint { color: #f9a8d4; font-weight: 600; }
  .prompt-anatomy .pa-plain      { color: #d1d5db; }

  /* Anatomy legend */
  .anatomy-legend {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
    margin-top: 10px;
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

  /* Debug loop diagram */
  .debug-loop {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0;
    margin: 20px 0;
  }

  .dl-node {
    background: #111827;
    border-radius: 8px;
    padding: 12px 16px;
    text-align: center;
    flex: 1;
  }

  .dl-node .dn-icon  { font-size: 20px; margin-bottom: 4px; }
  .dl-node .dn-label { font-family: 'DM Mono', monospace; font-size: 12px; color: #60a5fa; font-weight: 500; margin-bottom: 2px; }
  .dl-node .dn-desc  { font-size: 11px; color: #6b7280; line-height: 1.4; }

  .dl-arrow {
    font-size: 18px;
    color: #374151;
    padding: 0 8px;
    flex-shrink: 0;
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
---

<!-- _class: cover -->

# Prompt AI for Coding
## Without the Frustration

&nbsp;

**AI writes bad code when you ask bad questions.** Here's how to ask better ones.

`inputs` · `outputs` · `errors` · `iteration` · `context`

---

## Why AI Code Fails

The model isn't the problem. The prompt is.

<div class="tools">
  <div class="tool-card">
    <div class="icon">🌫️</div>
    <div class="name">Too vague</div>
    <div class="desc">"Write a script to process my data" — what data? What processing? What format in and out?</div>
  </div>
  <div class="tool-card">
    <div class="icon">📦</div>
    <div class="name">No stack context</div>
    <div class="desc">Without knowing your Python version, libraries, and environment, it guesses — often wrong.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🧩</div>
    <div class="name">Missing input/output spec</div>
    <div class="desc">Code that works in theory fails in practice when the data structure doesn't match what was assumed.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔄</div>
    <div class="name">Pasting errors without context</div>
    <div class="desc">"It doesn't work" tells the AI nothing. The error message, the line, and the code together — that's a solvable problem.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">TECHNIQUE 01</div>

## Be Specific with Inputs and Outputs

The most important upgrade to any coding prompt. Describe exactly what goes in and what should come out.

<div class="chat-mock">
  <div class="chat-row">
    <div class="chat-avatar user">👤</div>
    <div class="chat-bubble user-bad">
      <div class="bubble-label">❌ Vague</div>
      Write a Python function to filter my CSV file.
    </div>
  </div>
</div>

<div class="chat-mock">
  <div class="chat-row">
    <div class="chat-avatar user">👤</div>
    <div class="chat-bubble user-good">
      <div class="bubble-label">✅ Specific</div>
      Write a Python 3.11 function using pandas. Input: a DataFrame with columns ["bus_id", "voltage_pu", "region"]. Output: a filtered DataFrame containing only rows where voltage_pu &lt; 0.95, sorted ascending by voltage_pu. No index in the output.
    </div>
  </div>
</div>

<div class="highlight">

**The rule:** treat the AI like a new developer on your team. Give it the same spec you'd write in a ticket — input shape, output shape, constraints, edge cases if any.

</div>

---

<!-- _class: step -->

<div class="step-badge">TECHNIQUE 02</div>

## Ask for Explanations and Comments

Code that works but you don't understand is a liability — you can't debug it or adapt it.

<div class="two-col">
  <div class="col-card">
    <div class="label">Ask for this</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">
      "Add a comment to any non-obvious line."<br><br>
      "After the code, explain what each section does in plain English."<br><br>
      "Explain why you used <code>groupby</code> here instead of a loop."
    </p>
  </div>
  <div class="col-card">
    <div class="label">Why it matters</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">You're not just getting working code — you're learning. A commented, explained snippet teaches you the pattern so you can write the next one yourself.</p>
  </div>
</div>

<div class="code-block">
  <span class="cmt"># Good comment: explains WHY, not WHAT</span><br>
  <span class="cmt"># Using .loc avoids SettingWithCopyWarning on sliced DataFrames</span><br>
  <span class="var">df</span>.<span class="fn">loc</span>[<span class="var">df</span>[<span class="str">"voltage_pu"</span>] <span class="op">&lt;</span> <span class="num">0.95</span>, <span class="str">"flag"</span>] <span class="op">=</span> <span class="str">"undervoltage"</span><br>
  <br>
  <span class="cmt"># Bad comment: just restates the code</span><br>
  <span class="cmt"># set flag column to "undervoltage"</span>
</div>

---

<!-- _class: step -->

<div class="step-badge">TECHNIQUE 03</div>

## Iterative Debugging with AI

Don't expect perfection on the first pass. Use a loop: run → break → feed back → fix.

<div class="debug-loop">
  <div class="dl-node">
    <div class="dn-icon">✍️</div>
    <div class="dn-label">Prompt</div>
    <div class="dn-desc">Specific task + stack + I/O</div>
  </div>
  <div class="dl-arrow">→</div>
  <div class="dl-node">
    <div class="dn-icon">▶️</div>
    <div class="dn-label">Run it</div>
    <div class="dn-desc">In your actual environment</div>
  </div>
  <div class="dl-arrow">→</div>
  <div class="dl-node">
    <div class="dn-icon">💥</div>
    <div class="dn-label">It breaks</div>
    <div class="dn-desc">Copy the full traceback</div>
  </div>
  <div class="dl-arrow">→</div>
  <div class="dl-node">
    <div class="dn-icon">📋</div>
    <div class="dn-label">Feed back</div>
    <div class="dn-desc">Error + code + what you tried</div>
  </div>
  <div class="dl-arrow">→</div>
  <div class="dl-node">
    <div class="dn-icon">✅</div>
    <div class="dn-label">Fixed</div>
    <div class="dn-desc">Verify in your environment</div>
  </div>
</div>

<div class="highlight warn">

**Never accept AI code without running it.** A response that looks correct is not the same as code that runs correctly in your environment, with your data, on your version of Python. Always test.

</div>

---

<!-- _class: step -->

<div class="step-badge">TECHNIQUE 04</div>

## Provide Errors Properly

An error message without context is unanswerable. Give the AI everything it needs to diagnose.

<div class="error-block">
  <div class="error-bar">
    <span class="eb-label">❌ What most people paste</span>
  </div>
  <div class="error-body">
    <span class="el-msg">it's not working, here's the error: KeyError: 'voltage_pu'</span>
  </div>
</div>

<div class="error-block" style="border-color: #166534;">
  <div class="error-bar" style="background: #14532d;">
    <span class="eb-label" style="color:#86efac;">✅ What to paste instead</span>
  </div>
  <div class="error-body">
    <span class="el-trace">Traceback (most recent call last):</span><br>
    <span class="el-trace">&nbsp;&nbsp;File <span class="el-file">"filter_buses.py"</span>, line <span class="el-line">12</span>, in &lt;module&gt;</span><br>
    <span class="el-trace">&nbsp;&nbsp;&nbsp;&nbsp;filtered = df[df[<span class="el-file">"voltage_pu"</span>] &lt; 0.95]</span><br>
    <span class="el-msg">KeyError: 'voltage_pu'</span><br>
    <br>
    <span style="color:#6b7280; font-size:12px;">My CSV has columns: bus_id, v_pu, region. Python 3.11, pandas 2.1.</span>
  </div>
</div>

Full traceback + the offending line + your column names + your library versions. That's a solvable error report.

---

<!-- _class: step -->

<div class="step-badge">WALKTHROUGH</div>

## Example: The Full Prompt Anatomy

A real coding prompt — every part labeled:

<div class="prompt-anatomy">
  <span class="pa-stack">Python 3.11, pandas 2.1, running in a venv.</span><br>
  <span class="pa-task">Write a function called `flag_undervoltage` that:</span><br>
  <span class="pa-input">— takes a DataFrame with columns: bus_id (str), voltage_pu (float), region (str)</span><br>
  <span class="pa-output">— returns the same DataFrame with a new column "status": "ok" if voltage_pu ≥ 0.95, "low" if below</span><br>
  <span class="pa-constraint">— uses .loc to avoid SettingWithCopyWarning</span><br>
  <span class="pa-constraint">— does not modify the original DataFrame (return a copy)</span><br>
  <span class="pa-plain">Add a comment explaining the .loc usage. No other comments needed.</span>
</div>

<div class="anatomy-legend">
  <div class="legend-item"><div class="legend-dot" style="background:#60a5fa"></div><span style="color:#60a5fa">Stack</span></div>
  <div class="legend-item"><div class="legend-dot" style="background:#86efac"></div><span style="color:#86efac">Task</span></div>
  <div class="legend-item"><div class="legend-dot" style="background:#fde68a"></div><span style="color:#fde68a">Input spec</span></div>
  <div class="legend-item"><div class="legend-dot" style="background:#c4b5fd"></div><span style="color:#c4b5fd">Output spec</span></div>
  <div class="legend-item"><div class="legend-dot" style="background:#f9a8d4"></div><span style="color:#f9a8d4">Constraints</span></div>
</div>

---

## Quick Reference Cheatsheet

<div class="two-col">
  <div class="col-card">
    <div class="label">✅ Always include</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">
      ✦ Python version + key libraries<br>
      ✦ Input: exact column names and types<br>
      ✦ Output: shape, columns, sort order<br>
      ✦ Full traceback when reporting errors<br>
      ✦ What you already tried
    </p>
  </div>
  <div class="col-card">
    <div class="label">❌ Stop doing this</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">
      ✦ "It doesn't work" without the error<br>
      ✦ Asking to "fix my code" without sharing it<br>
      ✦ Accepting code you don't understand<br>
      ✦ Not running it before saying it works<br>
      ✦ One giant prompt for a complex task
    </p>
  </div>
</div>

<div class="highlight good">

**The mindset shift:** you're not asking the AI to solve your problem — you're pairing with it. You bring the domain knowledge and the test environment. It brings the syntax and the patterns. Neither works without the other.

</div>

---

<!-- _class: final -->

# Specific prompt.
# Working code.
# You understand why.

&nbsp;

Stack + task + input + output + constraints. Every time.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*