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

  .terminal {
    background: #111827;
    border-radius: 10px;
    overflow: hidden;
    margin: 16px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .terminal-bar {
    background: #1f2937;
    padding: 9px 16px;
    display: flex;
    align-items: center;
    gap: 7px;
  }

  .terminal-bar .dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    display: inline-block;
  }

  .terminal-bar .dot.red    { background: #ef4444; }
  .terminal-bar .dot.yellow { background: #f59e0b; }
  .terminal-bar .dot.green  { background: #22c55e; }

  .terminal-bar .title {
    font-size: 12px;
    color: #6b7280;
    margin-left: 8px;
    letter-spacing: 0.04em;
  }

  .terminal-body {
    padding: 16px 20px;
    line-height: 2;
  }

  .terminal-body .prompt { color: #22c55e; }
  .terminal-body .cmd    { color: #f9fafb; }
  .terminal-body .out    { color: #9ca3af; }
  .terminal-body .cmt    { color: #4b5563; font-style: italic; }

  .cmd-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 12px;
  }

  .cmd-row {
    background: #111827;
    border-radius: 8px;
    padding: 12px 16px;
    display: flex;
    align-items: flex-start;
    gap: 14px;
  }

  .cmd-row .cmd-name {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #60a5fa;
    font-weight: 500;
    min-width: 110px;
    padding-top: 1px;
  }

  .cmd-row .cmd-desc {
    font-size: 13px;
    color: #d1d5db;
    line-height: 1.5;
  }

  .cmd-row .cmd-desc span {
    display: block;
    color: #6b7280;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    margin-top: 2px;
  }

  .two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
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

  .cheat-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
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
    padding: 8px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
  }

  .cheat-table tr:nth-child(even) td { background: var(--off-white); }
  .cheat-table .mono {
    font-family: 'DM Mono', monospace;
    color: var(--blue);
    font-size: 13px;
  }

  .flow {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 20px 0;
    flex-wrap: wrap;
  }

  .flow-step {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 10px 16px;
    font-size: 13px;
    font-family: 'DM Mono', monospace;
    color: var(--text);
    white-space: nowrap;
  }

  .flow-arrow {
    color: var(--blue);
    font-size: 18px;
    font-weight: 600;
  }

  .prompt-box {
    background: #111827;
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .prompt-box .prompt-bar {
    background: #1f2937;
    padding: 8px 16px;
    font-size: 12px;
    color: #6b7280;
    letter-spacing: 0.04em;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .prompt-box .prompt-body {
    padding: 14px 20px;
    line-height: 1.9;
  }

  .prompt-box .p-label { color: #f59e0b; }
  .prompt-box .p-text  { color: #f9fafb; }
  .prompt-box .p-cmt   { color: #4b5563; font-style: italic; }
  .prompt-box .p-good  { color: #34d399; }
  .prompt-box .p-bad   { color: #f87171; }
---

<!-- _class: cover -->

# Build Apps Faster with AI
## The Agent Workflow

&nbsp;

**Stop writing code from scratch.** Describe what you want, iterate fast, ship sooner.

`idea` · `prompt` · `generate` · `test` · `refine` · `ship`

---

## Why This Workflow Changes Everything

AI coding assistants don't replace you — they collapse the time between **thinking and having a working thing**.

<div class="tools">
  <div class="tool-card">
    <div class="icon">⚡</div>
    <div class="name">10× faster first drafts</div>
    <div class="desc">Generate a working scaffold in seconds. Spend your time on logic and design, not boilerplate.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔁</div>
    <div class="name">Iterate in plain English</div>
    <div class="desc">Refining is just talking. "Make the button red" or "add error handling" — no syntax lookup needed.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🧠</div>
    <div class="name">You stay in charge</div>
    <div class="desc">AI writes code. You review, test, and decide. Understanding what it generates is still your job.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🚢</div>
    <div class="name">Ship real things</div>
    <div class="desc">The output is actual code — not mockups. Hook it to a real API and you have a real product.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Start With a Crisp Idea

Before you touch any AI tool, write your idea as **one sentence**. Vague ideas produce vague code.

<div class="two-col">
  <div class="col-card">
    <div class="label">Too vague ✗</div>
    <p style="font-size:13.5px; margin-top:8px; color:#6b7280;">"Build me an app."<br><br>"I want something for tracking stuff."<br><br>"Make a dashboard."</p>
  </div>
  <div class="col-card">
    <div class="label">Just right ✓</div>
    <p style="font-size:13.5px; margin-top:8px;">"A single-page web app where I paste a URL and it returns a 3-bullet summary using the OpenAI API."</p>
  </div>
</div>

<div class="highlight">

**The one-sentence test:** Can a stranger read your idea and build the exact same thing? If not, add one more constraint — the tech stack, the input, or the output format.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Write the Prompt That Does the Heavy Lifting

A great prompt has four parts. You don't need all four every time — but the more context you give, the better the first output.

<div class="prompt-box">
  <div class="prompt-bar">✏️ &nbsp; Anatomy of a high-quality prompt</div>
  <div class="prompt-body">
    <span class="p-label">ROLE &nbsp;&nbsp;&nbsp;&nbsp; </span><span class="p-text">You are a senior frontend developer.</span><br>
    <span class="p-label">TASK &nbsp;&nbsp;&nbsp;&nbsp; </span><span class="p-text">Build a single-page URL summarizer app in plain HTML/JS.</span><br>
    <span class="p-label">CONTEXT &nbsp;</span><span class="p-text">Uses the OpenAI API. Input: a URL. Output: 3 bullet points.</span><br>
    <span class="p-label">FORMAT &nbsp;&nbsp;</span><span class="p-text">One file. Inline CSS. No frameworks. Add error handling.</span><br>
    <span class="p-cmt"># The more specific your FORMAT, the less cleanup you'll do.</span>
  </div>
</div>

<div class="highlight">

**Rule of thumb:** If you'd have to explain it to a junior dev, put it in the prompt. AI doesn't infer intentions — it fills gaps with guesses.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Generate & Read the Output

Paste your prompt into your AI tool of choice and **read the code before running it**. This is the most important habit.

<div class="cmd-grid">
  <div class="cmd-row">
    <div class="cmd-name">Scan structure</div>
    <div class="cmd-desc">Does it match what you asked for?<span>Right file type, right approach, no extra files you didn't want</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">Check imports</div>
    <div class="cmd-desc">Are all dependencies real and available?<span>AI sometimes invents package names or uses outdated APIs</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">Find hardcodes</div>
    <div class="cmd-desc">Look for placeholder values to replace<span>API keys, URLs, usernames — never commit these</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">Spot the gaps</div>
    <div class="cmd-desc">What's missing or wrong?<span>Note it — your next prompt will fix it exactly</span></div>
  </div>
</div>

<div class="highlight">

**Copy → paste → run.** If it works on the first try, great. If it doesn't, the error message is your next prompt.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 04</div>

## Test It — Then Break It on Purpose

Running is not testing. After the happy path works, try to make it fail.

<div class="two-col">
  <div class="col-card">
    <div class="label">Happy path</div>
    <p style="font-size:13.5px; margin-top:8px;">Does it work with valid input? Button clicks, form submits, API responds correctly?</p>
  </div>
  <div class="col-card">
    <div class="label">Edge cases to try</div>
    <p style="font-size:13.5px; margin-top:8px;">Empty input. Very long input. Bad network. Wrong data type. Click the button twice.</p>
  </div>
</div>

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span>
    <span class="dot yellow"></span>
    <span class="dot green"></span>
    <span class="title">Browser console — your best debugging friend</span>
  </div>
  <div class="terminal-body">
    <span class="cmt"># Open DevTools: F12 or Cmd+Option+I</span><br>
    <span class="out">TypeError: Cannot read properties of undefined (reading 'choices')</span><br>
    <span class="cmt"># Copy this error → paste it into your AI chat</span><br>
    <span class="cmt"># "I got this error: [paste]. Here's my code: [paste]. Fix it."</span><br>
    <span class="prompt">→</span> <span class="cmd">AI will locate the issue and give you a corrected block.</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 05</div>

## Refine With Follow-Up Prompts

The first output is a draft. Refinement is where the real work happens — and it's just conversation.

<div class="prompt-box">
  <div class="prompt-bar">💬 &nbsp; Follow-up prompt patterns that work</div>
  <div class="prompt-body">
    <span class="p-good">✓ Fix: </span><span class="p-text">"I got this error: [paste error]. Here's the relevant code: [paste]. Fix it."</span><br>
    <span class="p-good">✓ Add: &nbsp;</span><span class="p-text">"Add a loading spinner while the API call is in progress."</span><br>
    <span class="p-good">✓ Change:</span><span class="p-text">"Change the layout to two columns on desktop, one on mobile."</span><br>
    <span class="p-good">✓ Explain:</span><span class="p-text">"Explain what this function does line by line."</span><br>
    <span class="p-bad">✗ Avoid: </span><span class="p-text">"It doesn't work." — No context. AI can't help without seeing the error.</span>
  </div>
</div>

<div class="highlight">

**The loop:** test → find an issue → describe it precisely → get a fix → test again. Most apps are done in 3–5 rounds.

</div>

---

## The Tools Involved

<table class="cheat-table">
  <tr>
    <th>Tool</th>
    <th>What it's for</th>
    <th>Free tier?</th>
  </tr>
  <tr>
    <td class="mono">Claude / ChatGPT</td>
    <td>Write, fix, and explain code via chat</td>
    <td>Yes (with limits)</td>
  </tr>
  <tr>
    <td class="mono">GitHub Copilot</td>
    <td>Inline AI autocomplete inside VS Code</td>
    <td>Free for students</td>
  </tr>
  <tr>
    <td class="mono">Cursor</td>
    <td>AI-native code editor — whole-file edits</td>
    <td>Yes (hobby plan)</td>
  </tr>
  <tr>
    <td class="mono">v0 by Vercel</td>
    <td>Generate React UI from a text description</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td class="mono">Replit Agent</td>
    <td>Build + deploy full apps from one prompt</td>
    <td>Yes (limited)</td>
  </tr>
  <tr>
    <td class="mono">Bolt.new</td>
    <td>Instant full-stack app from a description</td>
    <td>Yes (limited)</td>
  </tr>
  <tr>
    <td class="mono">VS Code + extensions</td>
    <td>Your editor — run, debug, version-control</td>
    <td>Free</td>
  </tr>
  <tr>
    <td class="mono">Browser DevTools</td>
    <td>Inspect errors, network calls, DOM output</td>
    <td>Built in</td>
  </tr>
</table>

---

## Example: URL Summarizer in 20 Minutes

The full agent workflow, end to end.

<div class="flow">
  <div class="flow-step">💡 Idea</div>
  <div class="flow-arrow">→</div>
  <div class="flow-step">✏️ One prompt</div>
  <div class="flow-arrow">→</div>
  <div class="flow-step">⚙️ Generate</div>
  <div class="flow-arrow">→</div>
  <div class="flow-step">🧪 Test</div>
  <div class="flow-arrow">→</div>
  <div class="flow-step">🔁 2 fix prompts</div>
  <div class="flow-arrow">→</div>
  <div class="flow-step">🚢 Done</div>
</div>

<div class="two-col">
  <div class="col-card">
    <div class="label">What was built</div>
    <p style="font-size:13px; margin-top:8px;">Single HTML file. Text input for a URL. Calls OpenAI. Returns 3-bullet summary. Styled, responsive, handles API errors.</p>
  </div>
  <div class="col-card">
    <div class="label">What the prompts looked like</div>
    <p style="font-size:13px; margin-top:8px;"><strong>Prompt 1:</strong> Full build spec (role + task + format).<br><strong>Prompt 2:</strong> "Fix: fetch error on invalid URLs."<br><strong>Prompt 3:</strong> "Add a loading state and disable the button while fetching."</p>
  </div>
</div>

---

<!-- _class: final -->

# The app exists now.
# You built it in an afternoon.

&nbsp;

Describe clearly. Read before you run. Fix with the error message.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*