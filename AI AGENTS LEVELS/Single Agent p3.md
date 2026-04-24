---
marp: true
theme: default
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,400;0,500;0,600;1,400&family=DM+Mono:wght@400;500&display=swap');

  :root {
    --amber: #d97706;
    --amber-light: #fffbeb;
    --amber-mid: #fde68a;
    --amber-dim: #b45309;
    --text: #1c1917;
    --muted: #78716c;
    --border: #e7e5e4;
    --white: #ffffff;
    --off-white: #fafaf9;
    --slate: #44403c;
  }

  section {
    font-family: 'DM Sans', sans-serif;
    background: var(--white);
    color: var(--text);
    padding: 52px 64px;
    font-size: 18px;
    line-height: 1.65;
  }

  section::after {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
  }

  h1 {
    font-family: 'DM Sans', sans-serif;
    font-size: 42px;
    font-weight: 600;
    color: var(--text);
    line-height: 1.15;
    margin-bottom: 0.4em;
    letter-spacing: -0.5px;
  }

  h2 {
    font-family: 'DM Sans', sans-serif;
    font-size: 27px;
    font-weight: 600;
    color: var(--text);
    border-bottom: 1.5px solid var(--border);
    padding-bottom: 10px;
    margin-bottom: 22px;
    letter-spacing: -0.3px;
  }

  h3 {
    font-family: 'DM Sans', sans-serif;
    font-size: 19px;
    font-weight: 500;
    color: var(--amber);
    margin-bottom: 8px;
  }

  p { color: var(--text); margin: 0.4em 0; }
  ul { padding-left: 1.4em; }
  li { margin-bottom: 10px; color: var(--text); }
  strong { color: var(--amber-dim); font-weight: 600; }

  code {
    font-family: 'DM Mono', monospace;
    background: var(--amber-light);
    color: var(--amber-dim);
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.87em;
  }

  blockquote {
    border-left: 3px solid var(--amber);
    background: var(--amber-light);
    padding: 16px 20px;
    margin: 20px 0;
    border-radius: 0 6px 6px 0;
    font-family: 'DM Mono', monospace;
    font-size: 0.82em;
    color: #92400e;
    line-height: 1.6;
  }

  blockquote p { color: #92400e; margin: 0; }

  /* ── Cover ── */
  section.cover {
    background: #1c1917;
    color: var(--white);
    display: flex;
    flex-direction: column;
    justify-content: center;
    position: relative;
    overflow: hidden;
  }

  section.cover::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
      radial-gradient(ellipse at 80% 20%, rgba(217,119,6,0.08) 0%, transparent 55%),
      radial-gradient(ellipse at 10% 85%, rgba(217,119,6,0.05) 0%, transparent 45%);
    pointer-events: none;
  }

  section.cover h1 { color: var(--white); font-size: 44px; letter-spacing: -0.8px; }
  section.cover h2 { color: #a8a29e; border-bottom-color: #44403c; font-size: 20px; font-weight: 400; letter-spacing: 0; }
  section.cover p  { color: #78716c; }
  section.cover strong { color: #fbbf24; }
  section.cover code { background: #292524; color: #fbbf24; border: 1px solid #44403c; }

  section.cover .series-badge {
    display: inline-block;
    background: #292524;
    color: #d97706;
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 500;
    padding: 5px 14px;
    border-radius: 4px;
    margin-bottom: 22px;
    letter-spacing: 0.1em;
    border: 1px solid #44403c;
    width: fit-content;
  }

  section.step { background: var(--off-white); }

  .highlight {
    background: var(--amber-light);
    border: 1px solid #fde68a;
    border-radius: 8px;
    padding: 16px 22px;
    margin: 16px 0;
  }

  .step-badge {
    display: inline-block;
    background: var(--text);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    padding: 4px 12px;
    border-radius: 3px;
    margin-bottom: 12px;
    letter-spacing: 0.08em;
  }

  section.final {
    background: #1c1917;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    position: relative;
    overflow: hidden;
  }

  section.final::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at 50% 50%, rgba(217,119,6,0.10) 0%, transparent 65%);
    pointer-events: none;
  }

  section.final h1 { color: white; font-size: 40px; letter-spacing: -0.5px; }
  section.final p  { color: #a8a29e; font-size: 18px; }
  section.final strong { color: #fbbf24; }
  section.final em { color: #a8a29e; }

  .two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 16px;
  }

  .col-card {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px 20px;
  }

  .col-card .label {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 8px;
  }

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
    font-size: 11.5px;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.07em;
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
    color: var(--amber-dim);
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
    background: var(--amber);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    min-width: 24px;
    height: 24px;
    border-radius: 5px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 2px;
    flex-shrink: 0;
  }

  /* ── Job Definition Grid ── */
  .job-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 14px;
    margin-top: 14px;
  }

  .job-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
  }

  .job-card .jc-head {
    padding: 10px 14px;
    font-weight: 600;
    font-size: 12.5px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border);
    background: var(--off-white);
  }

  .job-card .jc-head .jc-icon { font-size: 16px; }
  .job-card .jc-head .jc-title { color: var(--text); }

  .job-card .jc-body {
    padding: 12px 14px;
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.6;
  }

  .job-card .jc-example {
    margin-top: 10px;
    background: var(--amber-light);
    border: 1px solid #fde68a;
    border-radius: 5px;
    padding: 8px 10px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #92400e;
    line-height: 1.5;
  }

  /* ── File tree ── */
  .file-tree {
    background: #1c1917;
    border-radius: 10px;
    padding: 20px 24px;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #d6d3d1;
    line-height: 2;
    margin: 14px 0;
  }

  .file-tree .ft-dir  { color: #fbbf24; font-weight: 500; }
  .file-tree .ft-file { color: #d6d3d1; }
  .file-tree .ft-note { color: #78716c; font-size: 11.5px; margin-left: 6px; }
  .file-tree .ft-key  { color: #86efac; }

  /* ── Prompt anatomy ── */
  .prompt-box {
    background: #1c1917;
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0;
    border: 1px solid #44403c;
  }

  .prompt-box .pb-header {
    padding: 9px 18px;
    background: #292524;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #78716c;
    border-bottom: 1px solid #44403c;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .prompt-box .pb-header .pb-label { color: #fbbf24; font-weight: 500; }

  .prompt-box .pb-body {
    padding: 16px 20px;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .pb-section {
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 12.5px;
    line-height: 1.6;
    font-family: 'DM Mono', monospace;
  }

  .pb-section .pbs-tag {
    font-size: 10px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 5px;
    display: block;
  }

  .pb-section.role    { background: rgba(251,191,36,0.10); border: 1px solid rgba(251,191,36,0.2); color: #fde68a; }
  .pb-section.goal    { background: rgba(134,239,172,0.08); border: 1px solid rgba(134,239,172,0.2); color: #86efac; }
  .pb-section.format  { background: rgba(196,181,253,0.08); border: 1px solid rgba(196,181,253,0.2); color: #c4b5fd; }
  .pb-section.limits  { background: rgba(253,186,116,0.08); border: 1px solid rgba(253,186,116,0.2); color: #fdba74; }

  .pb-section.role   .pbs-tag { color: #fbbf24; }
  .pb-section.goal   .pbs-tag { color: #86efac; }
  .pb-section.format .pbs-tag { color: #c4b5fd; }
  .pb-section.limits .pbs-tag { color: #fdba74; }

  /* ── Code block ── */
  .code-block {
    background: #1c1917;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid #44403c;
    margin: 14px 0;
  }

  .code-block .cb-header {
    padding: 8px 18px;
    background: #292524;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #78716c;
    border-bottom: 1px solid #44403c;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .code-block .cb-header .cb-lang { color: #d97706; font-weight: 500; }
  .code-block .cb-header .cb-file { color: #a8a29e; }

  .code-block .cb-body {
    padding: 16px 20px;
    font-family: 'DM Mono', monospace;
    font-size: 12.5px;
    line-height: 1.75;
    color: #d6d3d1;
  }

  .cb-kw   { color: #c4b5fd; }
  .cb-fn   { color: #93c5fd; }
  .cb-str  { color: #86efac; }
  .cb-cmt  { color: #57534e; font-style: italic; }
  .cb-num  { color: #fbbf24; }
  .cb-var  { color: #fde68a; }

  /* ── Output anatomy ── */
  .output-flow {
    display: flex;
    gap: 0;
    align-items: stretch;
    margin: 14px 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .of-step {
    flex: 1;
    padding: 16px 16px;
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .of-step + .of-step {
    border-left: 1px solid var(--border);
  }

  .of-step .ofs-icon  { font-size: 22px; }
  .of-step .ofs-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.09em;
    color: var(--muted);
    margin-bottom: 2px;
  }

  .of-step .ofs-title {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
    margin-bottom: 3px;
  }

  .of-step .ofs-desc {
    font-size: 12px;
    color: var(--muted);
    line-height: 1.55;
  }

  .of-step.raw    { background: var(--off-white); }
  .of-step.parse  { background: #fffbeb; }
  .of-step.check  { background: #f0fdf4; }
  .of-step.use    { background: #eff6ff; }

  /* ── Bad / good compare ── */
  .compare-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin: 14px 0;
  }

  .cg-card {
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .cg-card .cg-head {
    padding: 9px 14px;
    font-weight: 600;
    font-size: 12.5px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border);
  }

  .cg-card.bad  .cg-head { background: #fef2f2; color: #991b1b; border-color: #fecaca; }
  .cg-card.good .cg-head { background: #f0fdf4; color: #166534; border-color: #bbf7d0; }

  .cg-card .cg-body {
    padding: 12px 14px;
    font-family: 'DM Mono', monospace;
    font-size: 11.5px;
    color: var(--muted);
    background: var(--white);
    line-height: 1.7;
  }

  .cg-card.good .cg-body { color: var(--text); }
---

<!-- _class: cover -->

<div class="series-badge">SINGLE AGENT SERIES · PART 3 OF 4</div>

# Building Your First Agent
## From blank file to working LLM call

&nbsp;

**One agent. One role. One output.** The fastest path from concept to running code.

`system_prompt` · `context` · `LLM call` · `output format` · `project structure`

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Define the Job Before Writing Any Code

Every good agent starts the same way — a single, unambiguous job description. Resist the urge to open a file first.

<div class="job-grid">
  <div class="job-card">
    <div class="jc-head"><span class="jc-icon">🎭</span><span class="jc-title">One Role</span></div>
    <div class="jc-body">
      Give the agent a single identity. It should be the best in the world at one specific thing — not a generalist.
      <div class="jc-example">✓ "You are a competitive intelligence analyst."<br>✗ "You help with research, writing, and analysis."</div>
    </div>
  </div>
  <div class="job-card">
    <div class="jc-head"><span class="jc-icon">🎯</span><span class="jc-title">One Goal</span></div>
    <div class="jc-body">
      One task per invocation. If you find yourself writing "and also" — split into two agents.
      <div class="jc-example">✓ "Summarise a competitor's pricing page."<br>✗ "Research competitors and write a blog post."</div>
    </div>
  </div>
  <div class="job-card">
    <div class="jc-head"><span class="jc-icon">📄</span><span class="jc-title">One Output Format</span></div>
    <div class="jc-body">
      Decide the exact shape of the output before you write the prompt. Structured output = predictable code.
      <div class="jc-example">✓ JSON with keys: name, price, differentiator<br>✗ "Return whatever makes sense."</div>
    </div>
  </div>
</div>

<div class="highlight">

**Rule of thumb:** If you can fill in these three blanks, you're ready to code — *"This agent acts as a **[role]**, takes **[input]**, and returns **[output format]**."*

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Project Structure for a Single Agent

A single-agent project needs very little. Start with this layout and expand only when a real need arises.

<div class="file-tree">
  <span class="ft-dir">my_agent/</span><br>
  &nbsp;&nbsp;├── <span class="ft-key">agent.py</span> <span class="ft-note">← the loop + LLM call lives here</span><br>
  &nbsp;&nbsp;├── <span class="ft-dir">prompts/</span><br>
  &nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└── <span class="ft-file">system.txt</span> <span class="ft-note">← system prompt as a plain text file</span><br>
  &nbsp;&nbsp;├── <span class="ft-dir">context/</span><br>
  &nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└── <span class="ft-file">data.md</span> <span class="ft-note">← files fed into the agent at runtime</span><br>
  &nbsp;&nbsp;├── <span class="ft-dir">output/</span><br>
  &nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└── <span class="ft-file">result.json</span> <span class="ft-note">← agent writes its result here</span><br>
  &nbsp;&nbsp;└── <span class="ft-file">.env</span> <span class="ft-note">← API key — never commit this</span>
</div>

<div class="highlight">

**Why separate `prompts/` from code?** Prompts change often. Keeping them in `.txt` files means you can iterate without touching Python. No redeploy. No risk of breaking imports.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Writing the System Prompt

The system prompt is your agent's job contract. It defines who it is, what it does, and exactly what form the answer takes — before any user message arrives.

<div class="prompt-box">
  <div class="pb-header">
    <span class="pb-label">prompts/system.txt</span>
    <span>system prompt anatomy</span>
  </div>
  <div class="pb-body">
    <div class="pb-section role">
      <span class="pbs-tag">① Role</span>
      You are a competitive intelligence analyst. Your job is to extract pricing and positioning data from competitor content.
    </div>
    <div class="pb-section goal">
      <span class="pbs-tag">② Goal</span>
      Given a block of text from a competitor's website, identify their pricing tiers, key differentiators, and target customer segment.
    </div>
    <div class="pb-section format">
      <span class="pbs-tag">③ Output format</span>
      Return ONLY a JSON object with keys: "tiers" (list), "differentiators" (list of strings), "target_segment" (string). No extra commentary.
    </div>
    <div class="pb-section limits">
      <span class="pbs-tag">④ Constraints</span>
      If the input does not contain pricing data, return {"error": "no_pricing_data"}. Do not invent data.
    </div>
  </div>
</div>

<div class="highlight">

**The four-part system prompt:** Role → Goal → Output format → Constraints. Leave any one out and you'll get inconsistent, unparseable results.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Feeding Context Files to the Agent

Your agent is only as good as the context you give it. Load files at runtime — don't hardcode content into the prompt.

<div class="compare-grid">
  <div class="cg-card bad">
    <div class="cg-head">❌ &nbsp;Hardcoded content</div>
    <div class="cg-body">
      user_msg = "Analyse Acme Corp.<br>
      They charge $99/mo for 5 seats,<br>
      $299/mo for 20 seats..."<br><br>
      <span style="color:#ef4444;"># Brittle. Changes require code edits.</span>
    </div>
  </div>
  <div class="cg-card good">
    <div class="cg-head">✅ &nbsp;Runtime file loading</div>
    <div class="cg-body">
      <span class="cb-kw">with</span> <span class="cb-fn">open</span>(<span class="cb-str">"context/data.md"</span>) <span class="cb-kw">as</span> f:<br>
      &nbsp;&nbsp;context = f.read()<br><br>
      user_msg = <span class="cb-str">f"Analyse this:\n{context}"</span>
    </div>
  </div>
</div>

**What counts as context?**

- Raw scraped text from a webpage
- A CSV file read into a string
- Previous agent outputs fed as input to the next step
- A markdown knowledge base your agent reasons over

<div class="highlight">

**Pattern:** Keep your `context/` folder as the agent's inbox. Your script picks up whatever file is there and injects it into the user message — no code change needed when the data changes.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## Making Your First LLM Call in Python

Three imports. One function. This is the complete skeleton of a single-agent call.

<div class="code-block">
  <div class="cb-header">
    <span class="cb-lang">python</span>
    <span class="cb-file">agent.py</span>
  </div>
  <div class="cb-body">
    <span class="cb-kw">import</span> anthropic, json, pathlib<br>
    <span class="cb-cmt"># ① Load the system prompt from file</span><br>
    system = pathlib.Path(<span class="cb-str">"prompts/system.txt"</span>).read_text()<br>
    <span class="cb-cmt"># ② Load context at runtime</span><br>
    context = pathlib.Path(<span class="cb-str">"context/data.md"</span>).read_text()<br>
    <span class="cb-cmt"># ③ Build the call</span><br>
    client = anthropic.Anthropic()&nbsp;&nbsp;<span class="cb-cmt"># reads ANTHROPIC_API_KEY from .env</span><br>
    response = client.messages.create(<br>
    &nbsp;&nbsp;model=<span class="cb-str">"claude-opus-4-5"</span>,<br>
    &nbsp;&nbsp;max_tokens=<span class="cb-num">1024</span>,<br>
    &nbsp;&nbsp;system=system,<br>
    &nbsp;&nbsp;messages=[{<span class="cb-str">"role"</span>: <span class="cb-str">"user"</span>, <span class="cb-str">"content"</span>: <span class="cb-str">f"Analyse this:\n{context}"</span>}])<br>
    <span class="cb-cmt"># ④ Extract the text from the response</span><br>
    raw = response.content[<span class="cb-num">0</span>].text<br>
    <span class="cb-fn">print</span>(raw)
  </div>
</div>

<div class="highlight">

**That's the whole call.** System prompt + user message → model → text back. Everything that follows — parsing, saving, looping — builds on this exact skeleton.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 06</div>

## Reading and Using the Output

A raw API response is just a string. Your job is to turn it into something your code can act on.

<div class="output-flow">
  <div class="of-step raw">
    <div class="ofs-icon">📨</div>
    <div class="ofs-label">Step 1</div>
    <div class="ofs-title">Extract text</div>
    <div class="ofs-desc"><code>response.content[0].text</code> — always a string, even if the model returned JSON.</div>
  </div>
  <div class="of-step parse">
    <div class="ofs-icon">🔍</div>
    <div class="ofs-label">Step 2</div>
    <div class="ofs-title">Parse the format</div>
    <div class="ofs-desc">If you asked for JSON, wrap in <code>json.loads()</code>. Catch <code>JSONDecodeError</code> — the model occasionally returns prose around the JSON.</div>
  </div>
  <div class="of-step check">
    <div class="ofs-icon">✅</div>
    <div class="ofs-label">Step 3</div>
    <div class="ofs-title">Validate the shape</div>
    <div class="ofs-desc">Check that expected keys exist. If the model returned <code>{"error": ...}</code>, handle it explicitly — don't assume success.</div>
  </div>
  <div class="of-step use">
    <div class="ofs-icon">💾</div>
    <div class="ofs-label">Step 4</div>
    <div class="ofs-title">Save or pass on</div>
    <div class="ofs-desc">Write to <code>output/result.json</code> or pass the parsed object to the next step in your pipeline.</div>
  </div>
</div>

<ul class="step-list" style="margin-top:10px;">
  <li>
    <div><strong>Strip fences before parsing.</strong> If the model wraps its JSON in <code>```json ... ```</code>, use <code>.strip("` \n").removeprefix("json")</code> before <code>json.loads()</code>.</div>
  </li>
  <li>
    <div><strong>Log the raw string while developing.</strong> Print <code>raw</code> before you parse it. This is your fastest debugging tool — you'll see immediately if the model drifted from the format.</div>
  </li>
</ul>

---

## Quick Reference — Part 3 Checklist

Everything you need before calling your agent done.

<table class="cheat-table">
  <thead>
    <tr><th>Checkpoint</th><th>What to verify</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="mono">Role defined</span></td>
      <td>System prompt opens with a clear, single identity — not a list of capabilities.</td>
    </tr>
    <tr>
      <td><span class="mono">Output format locked</span></td>
      <td>Prompt specifies exact keys/fields. You've written the <code>json.loads()</code> call before testing.</td>
    </tr>
    <tr>
      <td><span class="mono">Context loaded at runtime</span></td>
      <td>No content hardcoded in the script. Data lives in <code>context/</code> and is read with <code>pathlib</code>.</td>
    </tr>
    <tr>
      <td><span class="mono">API key in .env</span></td>
      <td><code>.env</code> is in <code>.gitignore</code>. Key is never in source code.</td>
    </tr>
    <tr>
      <td><span class="mono">Error case handled</span></td>
      <td>Prompt instructs the model what to return on failure. Code checks for that before assuming success.</td>
    </tr>
    <tr>
      <td><span class="mono">Raw output logged</span></td>
      <td>You <code>print(raw)</code> before parsing during development. Removed or gated before production.</td>
    </tr>
    <tr>
      <td><span class="mono">Output saved to file</span></td>
      <td>Result written to <code>output/</code>. Not just printed to terminal.</td>
    </tr>
  </tbody>
</table>

---

<!-- _class: final -->

# Your Agent Is Ready to Run.

&nbsp;

*One role. One call. One clean output. That's all it takes.*

&nbsp;

Next: **Part 4 — Knowing Its Limits.**

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*