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

  /* Stateless vs stateful split */
  .state-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
    margin: 16px 0;
  }

  .state-card {
    border-radius: 12px;
    padding: 20px 22px;
  }

  .state-card.stateless {
    background: #111827;
    border: 2px solid #374151;
  }

  .state-card.stateful {
    background: #111827;
    border: 2px solid #1d4ed8;
  }

  .state-card .sc-icon  { font-size: 28px; margin-bottom: 8px; }

  .state-card .sc-title {
    font-family: 'DM Mono', monospace;
    font-size: 17px;
    font-weight: 700;
    margin-bottom: 6px;
  }

  .state-card.stateless .sc-title { color: #6b7280; }
  .state-card.stateful  .sc-title { color: #60a5fa; }

  .state-card .sc-sub {
    font-size: 12px;
    font-family: 'DM Mono', monospace;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 10px;
  }

  .state-card.stateless .sc-sub { color: #4b5563; }
  .state-card.stateful  .sc-sub { color: #3b82f6; }

  .state-card .sc-desc {
    font-size: 13px;
    color: #9ca3af;
    line-height: 1.7;
  }

  .state-card .sc-fact {
    margin-top: 10px;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    line-height: 2;
  }

  .state-card.stateless .sc-fact { color: #4b5563; }
  .state-card.stateful  .sc-fact span { color: #60a5fa; }
  .state-card.stateless .sc-fact span { color: #6b7280; }

  /* Memory type tier cards */
  .memory-tiers {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 12px;
    margin: 16px 0;
  }

  .tier-card {
    border-radius: 10px;
    padding: 16px 14px;
    text-align: center;
  }

  .tier-card.t1 { background: #1e3a5f; border: 1px solid #1d4ed8; }
  .tier-card.t2 { background: #14532d; border: 1px solid #166534; }
  .tier-card.t3 { background: #2e1065; border: 1px solid #7c3aed; }
  .tier-card.t4 { background: #451a03; border: 1px solid #92400e; }

  .tier-card .tc-icon  { font-size: 22px; margin-bottom: 6px; }

  .tier-card .tc-name {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 4px;
  }

  .tier-card.t1 .tc-name { color: #60a5fa; }
  .tier-card.t2 .tc-name { color: #86efac; }
  .tier-card.t3 .tc-name { color: #c4b5fd; }
  .tier-card.t4 .tc-name { color: #fde68a; }

  .tier-card .tc-scope {
    font-size: 11px;
    font-family: 'DM Mono', monospace;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 6px;
  }

  .tier-card.t1 .tc-scope { color: #3b82f6; }
  .tier-card.t2 .tc-scope { color: #16a34a; }
  .tier-card.t3 .tc-scope { color: #7c3aed; }
  .tier-card.t4 .tc-scope { color: #92400e; }

  .tier-card .tc-desc { font-size: 11px; color: #9ca3af; line-height: 1.5; }

  /* Context storage diagram */
  .context-diagram {
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 10px;
    padding: 16px 20px;
    margin: 12px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .context-diagram .cd-label {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #4b5563;
    margin-bottom: 10px;
  }

  .cd-row {
    display: flex;
    align-items: baseline;
    gap: 12px;
    margin-bottom: 7px;
    line-height: 1.5;
  }

  .cd-row .cd-key  { color: #60a5fa; min-width: 120px; flex-shrink: 0; font-size: 12px; }
  .cd-row .cd-type { color: #c4b5fd; min-width: 80px; flex-shrink: 0; font-size: 11px; }
  .cd-row .cd-val  { color: #d1d5db; font-size: 12px; }

  /* Use case grid */
  .use-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 14px 0;
  }

  .use-card {
    background: #111827;
    border-radius: 8px;
    padding: 14px 16px;
    border-left: 3px solid #1d4ed8;
  }

  .use-card .uc-title { font-size: 14px; font-weight: 600; color: #f0f6fc; margin-bottom: 5px; }
  .use-card .uc-without { font-size: 12px; color: #f87171; margin-bottom: 4px; line-height: 1.5; }
  .use-card .uc-with    { font-size: 12px; color: #86efac; line-height: 1.5; }
  .use-card .uc-label   { font-family: 'DM Mono', monospace; font-size: 10px; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 2px; }
  .use-card .uc-label.bad  { color: #f87171; }
  .use-card .uc-label.good { color: #86efac; }

  /* Risk cards */
  .risk-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin: 14px 0;
  }

  .risk-card {
    background: #fff1f2;
    border: 1px solid #fecdd3;
    border-radius: 8px;
    padding: 14px 16px;
  }

  .risk-card .rc-icon  { font-size: 20px; margin-bottom: 6px; }
  .risk-card .rc-title { font-size: 13px; font-weight: 600; color: #9f1239; margin-bottom: 4px; }
  .risk-card .rc-desc  { font-size: 12px; color: #be123c; line-height: 1.5; }

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

# Memory in AI Agents
## Why It Changes Everything

&nbsp;

**A stateless AI answers your question. A stateful one remembers your context.**

`stateless` · `stateful` · `context` · `storage` · `persistence`

---

## The Problem with Stateless AI

Every time you open a new chat, the AI starts cold. No memory. No history. No you.

<div class="tools">
  <div class="tool-card">
    <div class="icon">🧊</div>
    <div class="name">Starts from zero every time</div>
    <div class="desc">Your job title, your stack, your preferences, your project context — re-explained in every session.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔁</div>
    <div class="name">Repetitive prompting</div>
    <div class="desc">You spend 20% of every session re-establishing context that hasn't changed since last week.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🧩</div>
    <div name="name">No learning over time</div>
    <div class="desc">Correcting the same mistake twice doesn't help a stateless AI. The correction dies with the session.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🚀</div>
    <div class="name">Memory changes the model</div>
    <div class="desc">An agent that remembers who you are, what you're building, and how you work is a fundamentally different tool.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Stateless vs Stateful

<div class="state-grid">
  <div class="state-card stateless">
    <div class="sc-icon">❄️</div>
    <div class="sc-title">Stateless</div>
    <div class="sc-sub">No memory between sessions</div>
    <div class="sc-desc">Each conversation is isolated. The model has no knowledge of past interactions. Context window resets on every new chat.</div>
    <div class="sc-fact">
      <span>✦ Default ChatGPT / Claude without custom instructions</span><br>
      <span>✦ Context window is the only "memory"</span><br>
      <span>✦ Session ends → everything gone</span>
    </div>
  </div>
  <div class="state-card stateful">
    <div class="sc-icon">🧠</div>
    <div class="sc-title">Stateful</div>
    <div class="sc-sub">Persists context across sessions</div>
    <div class="sc-desc">The agent stores facts, preferences, decisions, and history externally. Each new session retrieves and injects relevant context automatically.</div>
    <div class="sc-fact">
      <span>✦ Custom instructions (partial)</span><br>
      <span>✦ External memory stores (full)</span><br>
      <span>✦ Context survives session end</span>
    </div>
  </div>
</div>

<div class="highlight">

The difference is not the model. It's whether context is being written somewhere and read back in. Stateful behaviour is engineered — it doesn't happen automatically.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Four Types of AI Memory

<div class="memory-tiers">
  <div class="tier-card t1">
    <div class="tc-icon">💬</div>
    <div class="tc-name">In-Context</div>
    <div class="tc-scope">This session only</div>
    <div class="tc-desc">Everything in the current conversation window. Disappears when the session ends.</div>
  </div>
  <div class="tier-card t2">
    <div class="tc-icon">📋</div>
    <div class="tc-name">External Store</div>
    <div class="tc-scope">Persists across sessions</div>
    <div class="tc-desc">Facts saved to a file, database, or vector store. Retrieved and injected at the start of new sessions.</div>
  </div>
  <div class="tier-card t3">
    <div class="tc-icon">⚙️</div>
    <div class="tc-name">System Prompt</div>
    <div class="tc-scope">Permanent until edited</div>
    <div class="tc-desc">Role, rules, and user context baked into every session. Manual — you write and maintain it.</div>
  </div>
  <div class="tier-card t4">
    <div class="tc-icon">🗂️</div>
    <div class="tc-name">Retrieval (RAG)</div>
    <div class="tc-scope">On-demand from a corpus</div>
    <div class="tc-desc">Agent searches a knowledge base and pulls relevant chunks into context when needed.</div>
  </div>
</div>

Most production agents combine all four — system prompt for identity, external store for user facts, RAG for domain knowledge, context window for the current task.

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Storing Context — What It Looks Like

A simple external memory store is just a structured file the agent reads at the start of each session:

<div class="context-diagram">
  <div class="cd-label">📁 memory/user_context.json</div>
  <div class="cd-row">
    <span class="cd-key">"name"</span>
    <span class="cd-type">string</span>
    <span class="cd-val">"Julius Darang"</span>
  </div>
  <div class="cd-row">
    <span class="cd-key">"role"</span>
    <span class="cd-type">string</span>
    <span class="cd-val">"Registered Electrical Engineer, renewable energy"</span>
  </div>
  <div class="cd-row">
    <span class="cd-key">"stack"</span>
    <span class="cd-type">array</span>
    <span class="cd-val">["Python", "pandas", "pandapower", "Flask"]</span>
  </div>
  <div class="cd-row">
    <span class="cd-key">"preferences"</span>
    <span class="cd-type">object</span>
    <span class="cd-val">{"tone": "direct", "code": "comments on non-obvious lines only"}</span>
  </div>
  <div class="cd-row">
    <span class="cd-key">"active_project"</span>
    <span class="cd-type">string</span>
    <span class="cd-val">"N-1 contingency analysis — Visayas 60Hz grid"</span>
  </div>
  <div class="cd-row">
    <span class="cd-key">"last_session"</span>
    <span class="cd-type">string</span>
    <span class="cd-val">"2026-04-19 — built voltage flagging pipeline"</span>
  </div>
</div>

At session start, the agent reads this file and injects it into the system prompt. Every response is now informed by who you are and what you're working on.

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Real Use Cases — Memory in Action

<div class="use-grid">
  <div class="use-card">
    <div class="uc-title">🛠️&nbsp; Engineering assistant</div>
    <div class="uc-label bad">❌ Without memory</div>
    <div class="uc-without">"What's your grid frequency?" — Every. Single. Session.</div>
    <div class="uc-label good">✅ With memory</div>
    <div class="uc-with">Agent already knows: Visayas grid, 60Hz, pandapower, N-1 scope. Answers without preamble.</div>
  </div>
  <div class="use-card">
    <div class="uc-title">✍️&nbsp; Writing assistant</div>
    <div class="uc-label bad">❌ Without memory</div>
    <div class="uc-without">Generic blog tone on every draft. Re-explain "direct, no hype, Dan Koe style" every time.</div>
    <div class="uc-label good">✅ With memory</div>
    <div class="uc-with">Agent retrieves voice samples, past post style, Substack focus. Writes on-brand from turn one.</div>
  </div>
  <div class="use-card">
    <div class="uc-title">🤖&nbsp; Coding agent</div>
    <div class="uc-label bad">❌ Without memory</div>
    <div class="uc-without">Suggests frameworks you don't use. Writes Python 2 syntax. Ignores your naming conventions.</div>
    <div class="uc-label good">✅ With memory</div>
    <div class="uc-with">Knows your stack, version, project structure, and style preferences. Code fits first pass.</div>
  </div>
  <div class="use-card">
    <div class="uc-title">📅&nbsp; Planning agent</div>
    <div class="uc-label bad">❌ Without memory</div>
    <div class="uc-without">No awareness of ongoing projects, deadlines, or recurring tasks.</div>
    <div class="uc-label good">✅ With memory</div>
    <div class="uc-with">Picks up where last session left off. Flags tasks from previous days. Suggests based on project status.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## The Risks of Agent Memory

Memory makes agents more powerful — and more consequential when something goes wrong.

<div class="risk-grid">
  <div class="risk-card">
    <div class="rc-icon">🔐</div>
    <div class="rc-title">Sensitive data in storage</div>
    <div class="rc-desc">Memory files that hold credentials, personal data, or internal context need to be stored and encrypted securely. Treat them like a password file.</div>
  </div>
  <div class="risk-card">
    <div class="rc-icon">🗑️</div>
    <div class="rc-title">Stale context</div>
    <div class="rc-desc">Memory that isn't updated becomes wrong. An agent acting on outdated project status or old preferences produces confidently wrong outputs.</div>
  </div>
  <div class="risk-card">
    <div class="rc-icon">💉</div>
    <div class="rc-title">Prompt injection</div>
    <div class="rc-desc">If user-provided data gets written into memory unchecked, a bad actor could inject instructions that persist across sessions.</div>
  </div>
  <div class="risk-card">
    <div class="rc-icon">📈</div>
    <div class="rc-title">Compounding errors</div>
    <div class="rc-desc">A wrong fact in memory gets used across every future session. Errors don't stay local — they compound until the memory is corrected.</div>
  </div>
  <div class="risk-card">
    <div class="rc-icon">🔍</div>
    <div class="rc-title">Opaque behaviour</div>
    <div class="rc-desc">When agents behave unexpectedly, memory is a hidden variable. Always log what's being read and written so you can audit later.</div>
  </div>
  <div class="risk-card">
    <div class="rc-icon">🧹</div>
    <div class="rc-title">The fix: hygiene</div>
    <div class="rc-desc">Review your memory store regularly. Version-control context files. Build a clear() function. Memory you can't inspect, update, or delete is a liability.</div>
  </div>
</div>

---

## Building Memory Into Your Agent

The simplest implementation — no framework required:

<div class="code-block">
  <span class="kw">import</span> <span class="var">json</span><br>
  <span class="kw">from</span> <span class="var">pathlib</span> <span class="kw">import</span> <span class="var">Path</span><br>
  <br>
  <span class="var">MEMORY_FILE</span> <span class="op">=</span> <span class="var">Path</span>(<span class="str">"memory/context.json"</span>)<br>
  <br>
  <span class="kw">def</span> <span class="fn">load_memory</span>():<br>
  &nbsp;&nbsp;<span class="kw">if</span> <span class="var">MEMORY_FILE</span>.<span class="fn">exists</span>():<br>
  &nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">return</span> <span class="var">json</span>.<span class="fn">loads</span>(<span class="var">MEMORY_FILE</span>.<span class="fn">read_text</span>())<br>
  &nbsp;&nbsp;<span class="kw">return</span> {}<br>
  <br>
  <span class="kw">def</span> <span class="fn">save_memory</span>(<span class="var">data</span>: <span class="var">dict</span>):<br>
  &nbsp;&nbsp;<span class="var">MEMORY_FILE</span>.<span class="fn">parent</span>.<span class="fn">mkdir</span>(<span class="var">exist_ok</span><span class="op">=</span><span class="kw">True</span>)<br>
  &nbsp;&nbsp;<span class="var">MEMORY_FILE</span>.<span class="fn">write_text</span>(<span class="var">json</span>.<span class="fn">dumps</span>(<span class="var">data</span>, <span class="var">indent</span><span class="op">=</span><span class="num">2</span>))<br>
  <br>
  <span class="cmt"># At session start — inject into system prompt</span><br>
  <span class="var">ctx</span> <span class="op">=</span> <span class="fn">load_memory</span>()<br>
  <span class="var">system_prompt</span> <span class="op">=</span> <span class="op">f"</span><span class="str">User context: </span><span class="op">{</span><span class="var">ctx</span><span class="op">}</span><span class="str">. Act accordingly.</span><span class="op">"</span>
</div>

---

<!-- _class: final -->

# Stateless answers.
# Stateful understands.

&nbsp;

Memory is the difference between a tool you use and an assistant you work with.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*