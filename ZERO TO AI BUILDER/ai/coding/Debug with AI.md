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

  /* Code block */
  .code-block {
    background: #111827;
    border-radius: 8px;
    padding: 14px 20px;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #e5e7eb;
    line-height: 2;
    margin: 10px 0;
  }

  .code-block .kw  { color: #c4b5fd; }
  .code-block .fn  { color: #60a5fa; }
  .code-block .str { color: #86efac; }
  .code-block .var { color: #f9fafb; }
  .code-block .num { color: #fde68a; }
  .code-block .op  { color: #f9a8d4; }
  .code-block .cmt { color: #4b5563; font-style: italic; }
  .code-block .err { color: #f87171; }
  .code-block .fix { color: #86efac; }

  /* Error block */
  .error-block {
    background: #0d1117;
    border: 1px solid #7f1d1d;
    border-radius: 10px;
    overflow: hidden;
    margin: 10px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .error-bar {
    background: #7f1d1d;
    padding: 7px 16px;
  }

  .error-bar .eb-label {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #fca5a5;
    font-weight: 600;
  }

  .error-body {
    padding: 12px 18px;
    line-height: 2;
  }

  .error-body .el-trace { color: #6b7280; font-size: 12px; }
  .error-body .el-file  { color: #60a5fa; }
  .error-body .el-line  { color: #fde68a; }
  .error-body .el-msg   { color: #f87171; font-weight: 500; }

  /* Chat mock */
  .chat-mock {
    background: #111827;
    border-radius: 10px;
    padding: 12px 16px;
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

  /* Debug workflow strip */
  .debug-strip {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 0;
    align-items: stretch;
    margin: 18px 0;
  }

  .ds-step {
    background: #111827;
    border-radius: 8px;
    padding: 14px 12px;
    text-align: center;
    position: relative;
  }

  .ds-step .ds-num {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: #4b5563;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 6px;
  }

  .ds-step .ds-icon  { font-size: 20px; margin-bottom: 4px; }

  .ds-step .ds-label {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 4px;
  }

  .ds-step.s1 .ds-label { color: #f87171; }
  .ds-step.s2 .ds-label { color: #fde68a; }
  .ds-step.s3 .ds-label { color: #60a5fa; }
  .ds-step.s4 .ds-label { color: #c4b5fd; }
  .ds-step.s5 .ds-label { color: #86efac; }

  .ds-step .ds-desc { font-size: 11px; color: #6b7280; line-height: 1.4; }

  .ds-arrow {
    display: flex;
    align-items: center;
    justify-content: center;
    color: #374151;
    font-size: 16px;
    padding: 0 4px;
  }

  /* Context checklist */
  .context-check {
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 10px;
    padding: 16px 20px;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .context-check .cc-label {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #4b5563;
    margin-bottom: 10px;
    font-family: 'DM Mono', monospace;
  }

  .cc-row {
    display: flex;
    gap: 10px;
    align-items: flex-start;
    margin-bottom: 8px;
    line-height: 1.5;
  }

  .cc-row .cc-check { color: #86efac; flex-shrink: 0; font-size: 14px; }
  .cc-row .cc-key   { color: #60a5fa; min-width: 110px; flex-shrink: 0; }
  .cc-row .cc-val   { color: #d1d5db; }

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

  /* Step list */
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
    margin-bottom: 12px;
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

# Use AI to Debug
## Your Code Faster

&nbsp;

**An error message is a question. Learn how to ask it properly.**

`traceback` · `context` · `explain` · `fix` · `verify`

---

## Why Debugging is Slow

Most developers waste 80% of their debugging time before they even start looking in the right place.

<div class="tools">
  <div class="tool-card">
    <div class="icon">🔍</div>
    <div class="name">Staring at the wrong line</div>
    <div class="desc">The line that throws the error is rarely where the bug lives. You need to trace back further.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🌐</div>
    <div class="name">Stack Overflow rabbit holes</div>
    <div class="desc">Searching for error messages returns answers for different versions, different setups, different problems.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🤔</div>
    <div class="name">Not knowing what you don't know</div>
    <div class="desc">You don't know what the error means, so you don't know where to look, so you guess.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🤖</div>
    <div class="name">AI changes this entirely</div>
    <div class="desc">Give it the full error + your code + your context and it explains exactly what went wrong and why — in seconds.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Paste Error + Context — Not Just the Error

The error message alone is the least useful thing you can give an AI. Context is everything.

<div class="chat-mock">
  <div class="chat-row">
    <div class="chat-avatar user">👤</div>
    <div class="chat-bubble user-bad">
      <div class="bubble-label">❌ Useless</div>
      I'm getting a KeyError. How do I fix it?
    </div>
  </div>
  <div class="chat-row">
    <div class="chat-avatar ai">✦</div>
    <div class="chat-bubble ai-bad">
      <div class="bubble-label">AI response</div>
      A KeyError means the key doesn't exist in the dictionary. Make sure the key you're accessing is present. You can use .get() to avoid this error...
    </div>
  </div>
</div>

<div class="highlight warn">

Generic question → generic answer. The AI gave textbook advice with no idea what your actual problem is. It has no choice — you gave it nothing to work with.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## The Complete Error Report

Give the AI these five things and it can diagnose almost anything:

<div class="context-check">
  <div class="cc-label">📋 Minimum viable debug context</div>
  <div class="cc-row">
    <span class="cc-check">✓</span>
    <span class="cc-key">Full traceback</span>
    <span class="cc-val">The entire error output from your terminal — not just the last line</span>
  </div>
  <div class="cc-row">
    <span class="cc-check">✓</span>
    <span class="cc-key">The code</span>
    <span class="cc-val">The function or block that triggered the error</span>
  </div>
  <div class="cc-row">
    <span class="cc-check">✓</span>
    <span class="cc-key">Input sample</span>
    <span class="cc-val">What data you're passing in — column names, types, a sample row</span>
  </div>
  <div class="cc-row">
    <span class="cc-check">✓</span>
    <span class="cc-key">Stack</span>
    <span class="cc-val">Python version + relevant library versions (pandas, numpy, etc.)</span>
  </div>
  <div class="cc-row">
    <span class="cc-check">✓</span>
    <span class="cc-key">What you tried</span>
    <span class="cc-val">Any fixes you already attempted — so it doesn't suggest them again</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Ask AI to Explain First — Then Fix

The fastest path to fixing a bug long-term is understanding it first. Two prompts beat one.

<div class="chat-mock">
  <div class="chat-row">
    <div class="chat-avatar user">👤</div>
    <div class="chat-bubble user-good">
      <div class="bubble-label">Prompt 1 — Explain</div>
      Here's my error and code [paste]. Don't fix it yet. Explain in plain English what caused this and why.
    </div>
  </div>
  <div class="chat-row">
    <div class="chat-avatar ai">✦</div>
    <div class="chat-bubble ai-good">
      <div class="bubble-label">AI response</div>
      The error happens because your CSV has a column named "v_pu" but your code references "voltage_pu". pandas raises a KeyError when you try to access a column that doesn't exist in the DataFrame.
    </div>
  </div>
</div>

<div class="chat-mock">
  <div class="chat-row">
    <div class="chat-avatar user">👤</div>
    <div class="chat-bubble user-good">
      <div class="bubble-label">Prompt 2 — Fix</div>
      Now give me the corrected code. Add a comment where the fix was applied.
    </div>
  </div>
  <div class="chat-row">
    <div class="chat-avatar ai">✦</div>
    <div class="chat-bubble ai-good">
      <div class="bubble-label">AI response</div>
      [code block] — changed "voltage_pu" → "v_pu" on line 12. # column name corrected to match CSV header
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 04</div>

## Verify Step-by-Step — Never Blindly Accept

AI can confidently produce code that looks right but runs wrong. Always verify.

<div class="two-col">
  <div class="col-card">
    <div class="label">✅ How to verify</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">
      ✦ Run the fix in your actual environment<br>
      ✦ Test with your real data, not dummy data<br>
      ✦ Check output shape and values match expectations<br>
      ✦ Add a <code>print(df.head())</code> before and after<br>
      ✦ If it passes, commit — you're done
    </p>
  </div>
  <div class="col-card">
    <div class="label">⚠️ If it breaks again</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">
      Don't start a new chat. Stay in the same thread — the AI has your context. Paste the new error and say: "The fix didn't work. Here's the new traceback." One continuous conversation beats five fragmented ones.
    </p>
  </div>
</div>

<div class="highlight warn">

**The rule:** a fix is not a fix until it runs in your environment, on your data, without introducing a new error. "It looks right" is not a passing test.

</div>

---

<!-- _class: step -->

<div class="step-badge">WALKTHROUGH</div>

## Example: Full Debug Workflow

<div class="debug-strip">
  <div class="ds-step s1">
    <div class="ds-num">01</div>
    <div class="ds-icon">💥</div>
    <div class="ds-label">Error hits</div>
    <div class="ds-desc">Script throws KeyError on line 12</div>
  </div>
  <div class="ds-arrow">→</div>
  <div class="ds-step s2">
    <div class="ds-num">02</div>
    <div class="ds-icon">📋</div>
    <div class="ds-label">Assemble</div>
    <div class="ds-desc">Traceback + code + column names + Python version</div>
  </div>
  <div class="ds-arrow">→</div>
  <div class="ds-step s3">
    <div class="ds-num">03</div>
    <div class="ds-icon">🧠</div>
    <div class="ds-label">Explain</div>
    <div class="ds-desc">"Don't fix yet — explain what caused this"</div>
  </div>
  <div class="ds-arrow">→</div>
  <div class="ds-step s4">
    <div class="ds-num">04</div>
    <div class="ds-icon">🔧</div>
    <div class="ds-label">Fix</div>
    <div class="ds-desc">"Now give me the corrected code with a comment"</div>
  </div>
  <div class="ds-arrow">→</div>
  <div class="ds-step s5">
    <div class="ds-num">05</div>
    <div class="ds-icon">✅</div>
    <div class="ds-label">Verify</div>
    <div class="ds-desc">Run it. Check output. Commit if clean.</div>
  </div>
</div>

<div class="code-block">
  <span class="cmt"># Before fix — wrong column name</span><br>
  <span class="err">filtered = df[df["voltage_pu"] &lt; 0.95]  # KeyError</span><br>
  <br>
  <span class="cmt"># After fix — corrected to match actual CSV header</span><br>
  <span class="fix">filtered = df[df["v_pu"] &lt; 0.95]        # ✓ runs clean</span>
</div>

---

## Quick Reference

<div class="two-col">
  <div class="col-card">
    <div class="label">✅ Debug prompt template</div>
    <p style="font-size:13px; margin-top:8px; color:#374151; font-family: 'DM Mono', monospace; line-height:1.9;">
      Language + version:<br>
      Error (full traceback):<br>
      Code that triggered it:<br>
      Input data shape / columns:<br>
      What I already tried:<br>
      → First explain the cause.<br>
      → Then give the fix with a comment.
    </p>
  </div>
  <div class="col-card">
    <div class="label">❌ Habits that slow you down</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">
      ✦ Pasting only the last error line<br>
      ✦ Starting a new chat for each attempt<br>
      ✦ Accepting the fix without running it<br>
      ✦ Asking "why doesn't this work" with no code<br>
      ✦ Not mentioning what you already tried
    </p>
  </div>
</div>

<div class="highlight good">

**The shift:** stop treating debugging as looking for what's wrong. Start treating it as writing a clear bug report. A clear report produces a clear diagnosis. Every time.

</div>

---

<!-- _class: final -->

# Explain first.
# Fix second.
# Verify always.

&nbsp;

One good error report beats an hour of guessing.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*