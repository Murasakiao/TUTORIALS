---
marp: true
paginate: true
html: true
size: 4:3
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,400;0,500;0,600;1,400&family=DM+Mono:wght@400;500&display=swap');

  :root {
    --amber:       #f59e0b;
    --amber-dim:   #d97706;
    --green:       #22c55e;
    --blue:        #60a5fa;
    --purple:      #c4b5fd;
    --white:       #f1f5f9;
    --off-white:   #cbd5e1;
    --subtle:      #94a3b8;
    --muted:       #64748b;
    --faint:       #334155;
    --bg:          #080808;
    --card-bg:     #111111;
    --card-border: #222222;
  }

  section {
    font-family: 'DM Sans', sans-serif;
    background: var(--bg);
    color: var(--white);
    padding: 44px 52px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    position: relative;
  }

  h1 {
    font-size: 38px;
    font-weight: 700;
    line-height: 1.08;
    margin: 0 0 14px 0;
    color: var(--white);
    letter-spacing: -1.5px;
  }
  h2 {
    font-size: 28px;
    font-weight: 700;
    line-height: 1.1;
    margin: 0 0 14px 0;
    color: var(--white);
    letter-spacing: -1px;
    border: none;
  }
  p {
    font-size: 16px;
    line-height: 1.6;
    color: var(--subtle);
    margin: 0 0 12px 0;
  }
  strong { color: var(--white); font-weight: 600; }
  em     { color: var(--muted); font-style: normal; }
  code {
    font-family: 'DM Mono', monospace;
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    color: var(--amber);
    padding: 1px 6px;
    border-radius: 4px;
    font-size: 0.88em;
  }

  .accent-amber  { color: var(--amber); }
  .accent-green  { color: var(--green); }
  .accent-blue   { color: var(--blue); }
  .accent-purple { color: var(--purple); }

  /* ── TAG ── */
  .tag {
    display: flex;
    align-items: center;
    gap: 12px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 3px;
    color: var(--amber);
    text-transform: uppercase;
    margin-bottom: 18px;
  }
  .tag::before {
    content: '';
    display: block;
    width: 24px;
    height: 2px;
    background: var(--amber);
    flex-shrink: 0;
  }
  .tag.green  { color: var(--green); }
  .tag.green::before { background: var(--green); }
  .tag.blue   { color: var(--blue); }
  .tag.blue::before  { background: var(--blue); }

  /* ── HEADER ROW ── */
  .header-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
  }
  .page-num {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--amber-dim);
    letter-spacing: 2px;
    text-transform: uppercase;
  }
  .page-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--muted);
  }

  /* ── CARDS 2-col ── */
  .cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-bottom: 12px;
  }
  .card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 10px;
    padding: 14px;
  }
  .card-icon { font-size: 17px; margin-bottom: 6px; display: block; }
  .card h3 {
    font-size: 14px;
    font-weight: 600;
    color: var(--white);
    margin: 0 0 4px;
  }
  .card p {
    font-size: 13px;
    color: var(--subtle);
    line-height: 1.45;
    margin: 0;
  }

  /* ── CARDS 1-col stacked ── */
  .cards-col { display: flex; flex-direction: column; gap: 8px; margin-bottom: 12px; }
  .card-row {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 10px;
    padding: 12px 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }
  .card-row-icon { font-size: 17px; flex-shrink: 0; margin-top: 1px; }
  .card-row-body h3 {
    font-size: 14px;
    font-weight: 600;
    color: var(--white);
    margin: 0 0 3px;
  }
  .card-row-body p {
    font-size: 13px;
    color: var(--subtle);
    margin: 0;
    line-height: 1.45;
  }

  /* ── COMPARE 2-col ── */
  .compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-bottom: 10px;
  }
  .compare-col {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 10px;
    padding: 14px 16px;
  }
  .compare-col.good { border-color: #14532d; }
  .compare-label {
    font-family: 'DM Mono', monospace;
    font-size: 9px;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 6px;
    color: var(--muted);
  }
  .compare-label.bad  { color: #ef4444; }
  .compare-label.good { color: var(--green); }
  .compare-col h3 {
    font-size: 14px;
    font-weight: 600;
    color: var(--white);
    margin: 0 0 5px;
  }
  .compare-col p {
    font-size: 13px;
    color: var(--subtle);
    line-height: 1.45;
    margin: 0;
  }

  /* ── LIST (numbered rows) ── */
  .list { display: flex; flex-direction: column; gap: 7px; margin-bottom: 12px; }
  .list-item {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 8px;
    padding: 10px 14px;
  }
  .list-num {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--amber);
    flex-shrink: 0;
    margin-top: 1px;
    min-width: 18px;
  }
  .list-text { font-size: 13.5px; color: var(--subtle); line-height: 1.45; }
  .list-text strong { color: var(--white); }

  /* ── PILL ── */
  .pill {
    display: inline-block;
    background: #0a0a0a;
    border: 1px solid var(--card-border);
    border-radius: 5px;
    padding: 2px 8px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--amber);
  }
  .pill.green  { color: var(--green); border-color: #14532d; }
  .pill.blue   { color: var(--blue);  border-color: #1e3a5f; }

  /* ── INSIGHT BOX ── */
  .insight {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 10px;
    padding: 12px 18px;
    margin-top: auto;
  }
  .insight-label {
    font-family: 'DM Mono', monospace;
    font-size: 9px;
    letter-spacing: 3px;
    color: var(--muted);
    text-transform: uppercase;
    margin-bottom: 4px;
  }
  .insight p { font-size: 14px; color: var(--off-white); line-height: 1.5; margin: 0; }

  /* ── COVER ── */
  section.cover {
    justify-content: flex-end;
    padding-bottom: 80px;
    background: #050505;
  }
  section.cover h1 { font-size: 48px; }
  section.cover p  { font-size: 17px; color: var(--subtle); }

  /* ── VOLUME DIVIDER ── */
  section.vol-divider {
    justify-content: center;
    border-left: 5px solid var(--amber);
    background: #0c0c0c;
  }
  section.vol-divider .tag { margin-bottom: 20px; }
  section.vol-divider h1   { font-size: 44px; color: var(--amber); margin-bottom: 10px; }
  section.vol-divider h2   { font-size: 24px; color: var(--white); border: none; margin: 0 0 16px; }
  section.vol-divider p    { font-size: 15px; color: var(--muted); }

  /* ── CTA ── */
  section.cta {
    justify-content: center;
    align-items: center;
    text-align: center;
    background: var(--amber);
  }
  section.cta h1 { color: #0F0F0F; font-size: 40px; letter-spacing: -1px; margin-bottom: 10px; }
  section.cta h2 { color: #3a2e00; font-size: 22px; border: none; margin-bottom: 12px; }
  section.cta p  { color: #5a4700; font-size: 16px; max-width: 540px; margin: 0; }
  section.cta .handle {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #7a6000;
    margin-top: 22px;
    letter-spacing: 2px;
    text-transform: uppercase;
  }

  /* ── FOOTER ── */
  section::after {
    font-family: 'DM Mono', monospace;
    font-size: 9px;
    color: var(--muted);
    letter-spacing: 1px;
    content: '@juliusdarang · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
    position: absolute;
    bottom: 20px;
    right: 40px;
  }
---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 1 · COVER                        -->
<!-- ══════════════════════════════════════ -->
<!-- _class: cover -->

<div class="tag">Mini Tutorial · Vol 1 & Vol 2</div>

# Prompt Engineering 101

Get consistently better outputs from AI — from first principles to agentic systems.

*The essential techniques only.*

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 2 · THE CORE PROBLEM             -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— vol 1 · foundations —</span>
  <span class="page-label">what the model is doing</span>
</div>

## The model is not "thinking"

It predicts the next token. No goals, no memory, no intentions.

<div class="cards-col">
  <div class="card-row">
    <span class="card-row-icon">🎲</span>
    <div class="card-row-body">
      <h3>Hallucination</h3>
      <p>Confident wrong prediction — not lying, just pattern-matching badly.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">📐</span>
    <div class="card-row-body">
      <h3>Context window</h3>
      <p>Everything it can "see" at once. Beyond this limit — it forgets.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">⚠️</span>
    <div class="card-row-body">
      <h3>Vague prompt → vague output</h3>
      <p>Claude 4.x is very literal. Ambiguity is never resolved in your favour.</p>
    </div>
  </div>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 3 · ANATOMY OF A PROMPT          -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 01 — prompt anatomy</span>
  <span class="page-label">the 4 layers</span>
</div>

## Every prompt has 4 layers

<div class="list">
  <div class="list-item">
    <span class="list-num">01</span>
    <span class="list-text"><strong>Role</strong> — who the model is acting as</span>
  </div>
  <div class="list-item">
    <span class="list-num">02</span>
    <span class="list-text"><strong>Instruction</strong> — what it must do (use action verbs: analyze, extract, rewrite)</span>
  </div>
  <div class="list-item">
    <span class="list-num">03</span>
    <span class="list-text"><strong>Context</strong> — what it needs to know (separate with XML tags or triple quotes)</span>
  </div>
  <div class="list-item">
    <span class="list-num">04</span>
    <span class="list-text"><strong>Output format</strong> — how to structure the answer (put this <em>last</em>)</span>
  </div>
</div>

<div class="insight">
  <div class="insight-label">diagnostic test</div>
  <p>If the model summarized your prompt in one sentence — that's what it's actually optimizing for.</p>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 4 · ROLE + INSTRUCTION           -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 02 — role & instruction</span>
  <span class="page-label">be specific</span>
</div>

## Role + Instruction design

<div class="compare">
  <div class="compare-col">
    <div class="compare-label bad">❌ Vague</div>
    <h3>"You are an expert."</h3>
    <p>Too broad. The model picks any direction and runs with it.</p>
  </div>
  <div class="compare-col good">
    <div class="compare-label good">✅ Precise</div>
    <h3>"You are a senior data analyst."</h3>
    <p>Narrow focus, predictable behaviour, reliable tone.</p>
  </div>
</div>

<div class="compare">
  <div class="compare-col">
    <div class="compare-label bad">❌ Vague verbs</div>
    <p><em>help, discuss, think about</em></p>
  </div>
  <div class="compare-col good">
    <div class="compare-label good">✅ Action verbs</div>
    <p><strong>analyze, extract, classify, rewrite, compare</strong></p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">note on claude 4.x</div>
  <p>Modern Claude models are <strong>more literal than ever</strong> — vague instructions produce vague outputs more reliably now.</p>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 5 · CONTEXT & FORMAT             -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 03 — context & format</span>
  <span class="page-label">structure matters</span>
</div>

## Context vs Output Format

<div class="compare">
  <div class="compare-col">
    <div class="compare-label">Context</div>
    <h3>What it needs to know</h3>
    <p>Use XML tags or triple quotes to separate it from the instruction. Don't bury it in prose.</p>
  </div>
  <div class="compare-col good">
    <div class="compare-label good">Format</div>
    <h3>How to structure the answer</h3>
    <p>Put format instructions <strong>last</strong> — the model has recency bias toward the end of your prompt.</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">pro tip</div>
  <p>Examples anchor format <strong>better than descriptions alone</strong>. Show one good output — don't just describe it.</p>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 6 · FEW-SHOT PROMPTING           -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 04 — few-shot prompting</span>
  <span class="page-label">show, don't tell</span>
</div>

## Few-shot prompting

Show examples before asking. They teach tone, format, and reasoning simultaneously.

<div class="cards">
  <div class="card">
    <span class="card-icon">✅</span>
    <h3>2–3 examples is enough</h3>
    <p>More is not always better. Quality beats quantity.</p>
  </div>
  <div class="card">
    <span class="card-icon">🎯</span>
    <h3>Choose representative ones</h3>
    <p>Diverse, correctly labelled. Cover the range of inputs you expect.</p>
  </div>
  <div class="card">
    <span class="card-icon">⚠️</span>
    <h3>One bad example = damage</h3>
    <p>A wrong example does more harm than providing no examples at all.</p>
  </div>
  <div class="card">
    <span class="card-icon">🚫</span>
    <h3>Negative examples work</h3>
    <p>Show what you do NOT want — often clearer than describing it.</p>
  </div>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 7 · CHAIN-OF-THOUGHT             -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 05 — chain-of-thought</span>
  <span class="page-label">make it reason first</span>
</div>

## Chain-of-thought + Iteration

Force reasoning before the answer: <strong>"Think step by step before responding."</strong>

<div class="compare">
  <div class="compare-col good">
    <div class="compare-label good">✅ Use when</div>
    <p>Complex reasoning, multi-step problems, tasks with a single right answer.</p>
  </div>
  <div class="compare-col">
    <div class="compare-label bad">❌ Skip when</div>
    <p>Simple tasks — extra reasoning just adds noise and length.</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">the diagnostic loop</div>
  <p>Bad output = data. Identify the failing layer → change <strong>one variable at a time</strong> → retest. Never change two things at once.</p>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 8 · VOLUME 2 DIVIDER             -->
<!-- ══════════════════════════════════════ -->
<!-- _class: vol-divider -->

<div class="tag">Volume 2</div>

# Advanced Patterns
## & Agent Prompting

Chaining · Generator+Critic · Agentic systems · ReAct loop

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 9 · PROMPT CHAINING              -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 06 — prompt chaining</span>
  <span class="page-label">one thing at a time</span>
</div>

## Prompt chaining

Break complex tasks into a sequence. Each prompt produces an artifact the next one consumes.

<div class="list">
  <div class="list-item">
    <span class="list-num">01</span>
    <span class="list-text"><strong>Research prompt</strong> → summary document</span>
  </div>
  <div class="list-item">
    <span class="list-num">02</span>
    <span class="list-text"><strong>Outline prompt</strong> → structured outline</span>
  </div>
  <div class="list-item">
    <span class="list-num">03</span>
    <span class="list-text"><strong>Draft prompt</strong> → final content</span>
  </div>
</div>

<div class="insight">
  <div class="insight-label">main risk</div>
  <p>A bad output at step 1 degrades every step after. The first prompt's output format <strong>must match</strong> what the next prompt expects.</p>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 10 · GENERATOR + CRITIC          -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 07 — generator + critic</span>
  <span class="page-label">split the job</span>
</div>

## Generator + Critic pattern

The model is biased toward its own output. Self-review in a single prompt is unreliable.

<div class="compare">
  <div class="compare-col">
    <div class="compare-label">Generator</div>
    <h3>Focused on producing</h3>
    <p>No self-judgment. Output one concrete artifact.</p>
  </div>
  <div class="compare-col good">
    <div class="compare-label good">Critic</div>
    <h3>Evaluates against a rubric</h3>
    <p>Give it specific dimensions — not just "is this good?"</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">refinement step</div>
  <p>Feed the critic's output back to the generator. Draft → critique → improved draft. Each loop gets better.</p>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 11 · AGENT PROMPTING             -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 08 — agent prompting</span>
  <span class="page-label">loops, not one-shots</span>
</div>

## How agent prompting differs

Chat prompts are one-shot. **Agent prompts run in a loop.** Weaknesses in chat compound badly across steps.

<div class="cards">
  <div class="card">
    <span class="card-icon">🌀</span>
    <h3>Role drift</h3>
    <p>Agent loses its defined role over many reasoning steps.</p>
  </div>
  <div class="card">
    <span class="card-icon">🔧</span>
    <h3>Tool misuse</h3>
    <p>Vague descriptions cause the model to call the wrong tool.</p>
  </div>
  <div class="card">
    <span class="card-icon">♾️</span>
    <h3>Loop failure</h3>
    <p>Loops endlessly, stops too early, or gets stuck on an error.</p>
  </div>
  <div class="card">
    <span class="card-icon">📋</span>
    <h3>System prompt = contract</h3>
    <p>Role + responsibilities + hard constraints + stop conditions.</p>
  </div>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 12 · TOOL DESCRIPTIONS           -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 09 — tool descriptions</span>
  <span class="page-label">the model reads, not runs</span>
</div>

## Tool description prompting

The model picks tools by reading the **description** — not the code.

<div class="cards-col">
  <div class="card-row">
    <span class="card-row-icon">🏷️</span>
    <div class="card-row-body">
      <h3>Name + purpose + when to use</h3>
      <p>Be explicit about what this tool does and the exact conditions that should trigger it.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">🚫</span>
    <div class="card-row-body">
      <h3>When NOT to use it</h3>
      <p>Describing limitations prevents misuse — often more valuable than capability alone.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">🔢</span>
    <div class="card-row-body">
      <h3>Describe every parameter</h3>
      <p>Tell the model exactly what each argument expects. Ambiguity = misuse.</p>
    </div>
  </div>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 13 · REACT LOOP                  -->
<!-- ══════════════════════════════════════ -->

<div class="header-row">
  <span class="page-num">— 10 — react loop</span>
  <span class="page-label">reason → act → observe</span>
</div>

## Prompting the ReAct loop

Structure the system prompt so the model reasons **before** it acts, every step.

<div class="list">
  <div class="list-item">
    <span class="list-num">01</span>
    <span class="list-text"><strong>Reason</strong> — model thinks about what to do before calling any tool</span>
  </div>
  <div class="list-item">
    <span class="list-num">02</span>
    <span class="list-text"><strong>Act</strong> — calls the right tool with the right parameters</span>
  </div>
  <div class="list-item">
    <span class="list-num">03</span>
    <span class="list-text"><strong>Observe</strong> — reads the tool result cleanly back into the reasoning loop</span>
  </div>
  <div class="list-item">
    <span class="list-num">04</span>
    <span class="list-text"><strong>Stop</strong> — the agent must know <em>explicitly</em> when it is done</span>
  </div>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 14 · THE ONE RULE                -->
<!-- ══════════════════════════════════════ -->

<div style="display:flex;flex-direction:column;justify-content:center;height:100%;text-align:center;align-items:center;">
  <div class="tag" style="justify-content:center;margin-bottom:24px;">the one rule</div>
  <h1 style="font-size:54px;line-height:1.12;letter-spacing:-2px;">Precision<br>beats<br>vagueness</h1>
  <p style="font-size:17px;color:var(--subtle);margin-top:20px;max-width:520px;line-height:1.6;">Every technique in this course is a way to be more specific about what you want — from role design to tool descriptions to stop conditions.</p>
</div>

---

<!-- ══════════════════════════════════════ -->
<!-- SLIDE 15 · CTA                         -->
<!-- ══════════════════════════════════════ -->
<!-- _class: cta -->

<div class="tag" style="justify-content:center;color:#0a0a0a;margin-bottom:20px;">
  Prompt Engineering 101
</div>

# Found this useful?

## Save it for the next time your prompt fails.

<p>Apply one technique per day — role → few-shot → chaining → critic → agent.</p>

<div class="handle">Full course · Vol 1 & Vol 2</div>