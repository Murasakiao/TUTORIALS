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
  .code-block .warn-line { color: #fde68a; }

  /* Review checklist card */
  .review-card {
    border-radius: 10px;
    overflow: hidden;
    margin: 10px 0;
  }

  .review-card .rc-header {
    padding: 9px 16px;
    display: flex;
    align-items: center;
    gap: 8px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 600;
  }

  .review-card.logic     .rc-header { background: #1e3a5f; color: #60a5fa; }
  .review-card.edge      .rc-header { background: #451a03; color: #fde68a; }
  .review-card.security  .rc-header { background: #4c0519; color: #f9a8d4; }
  .review-card.perf      .rc-header { background: #2e1065; color: #c4b5fd; }

  .review-card .rc-body {
    padding: 12px 16px;
    font-size: 13px;
    line-height: 1.9;
  }

  .review-card.logic    .rc-body { background: #0d1117; border: 1px solid #1e3a5f; border-top: none; border-radius: 0 0 10px 10px; color: #93c5fd; }
  .review-card.edge     .rc-body { background: #0d1117; border: 1px solid #451a03; border-top: none; border-radius: 0 0 10px 10px; color: #fde68a; }
  .review-card.security .rc-body { background: #0d1117; border: 1px solid #4c0519; border-top: none; border-radius: 0 0 10px 10px; color: #f9a8d4; }
  .review-card.perf     .rc-body { background: #0d1117; border: 1px solid #2e1065; border-top: none; border-radius: 0 0 10px 10px; color: #c4b5fd; }

  .review-card .rc-body .check { margin-right: 6px; }

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

  .chat-bubble.user-good { background: #1e3a5f; border: 1px solid #1d4ed8; color: #bfdbfe; }
  .chat-bubble.ai-good   { background: #14532d; border: 1px solid #166534; color: #bbf7d0; font-style: italic; }
  .chat-bubble.ai-warn   { background: #451a03; border: 1px solid #92400e; color: #fde68a; font-style: italic; }

  .chat-bubble .bubble-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 3px;
    font-style: normal;
    color: #4b5563;
  }

  /* Review checklist table */
  .review-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
    margin: 12px 0;
  }

  .review-table th {
    background: var(--text);
    color: white;
    padding: 8px 14px;
    text-align: left;
    font-weight: 500;
    font-size: 12px;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.05em;
  }

  .review-table td {
    padding: 8px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
    font-size: 13px;
    vertical-align: top;
  }

  .review-table tr:nth-child(even) td { background: var(--off-white); }

  .review-table .area-tag {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 4px;
    display: inline-block;
    white-space: nowrap;
  }

  .area-tag.logic    { background: #1e3a5f; color: #60a5fa; }
  .area-tag.edge     { background: #451a03; color: #fde68a; }
  .area-tag.security { background: #4c0519; color: #f9a8d4; }
  .area-tag.perf     { background: #2e1065; color: #c4b5fd; }

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

# Review AI-Generated Code
## Properly

&nbsp;

**AI writes with confidence. That's the problem.** Learn what to check before you ship.

`logic` · `edge cases` · `security` · `performance` · `self-review`

---

## Why Blind Trust is Dangerous

AI code looks correct. It is formatted well, named sensibly, and passes a quick read. That's not the same as working correctly.

<div class="tools">
  <div class="tool-card">
    <div class="icon">😌</div>
    <div class="name">Confident tone ≠ correct code</div>
    <div class="desc">AI never says "I'm not sure about this." It writes bad logic in the same confident style as good logic.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🕳️</div>
    <div class="name">Silent failures</div>
    <div class="desc">The most dangerous bugs don't crash — they produce wrong output quietly. No error, no warning, just wrong data.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🌐</div>
    <div class="name">No knowledge of your data</div>
    <div class="desc">The AI doesn't know what your CSV actually contains, what your edge cases are, or what your production constraints look like.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🛡️</div>
    <div class="name">You're the last check</div>
    <div class="desc">There is no QA layer between AI output and your environment. The review you do is the only one that happens.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CHECK 01</div>

## Check the Logic

Does the code actually do what you asked — or what the AI assumed you meant?

<div class="review-card logic">
  <div class="rc-header">🧠 Logic checks</div>
  <div class="rc-body">
    <span class="check">✦</span> Does the function return what you expected, or a transformed version of it?<br>
    <span class="check">✦</span> Are conditions using <code>==</code> vs <code>is</code>, <code>&lt;</code> vs <code>&lt;=</code> correctly?<br>
    <span class="check">✦</span> Are loops iterating over the right thing — rows, columns, or values?<br>
    <span class="check">✦</span> Does the sort order match your intent — ascending or descending?<br>
    <span class="check">✦</span> Is the output being returned or just printed?
  </div>
</div>

<div class="code-block">
  <span class="cmt"># AI wrote this — looks fine at a glance</span><br>
  <span class="err">filtered = df[df["voltage_pu"] &lt;= 0.95]  # ← should be strictly &lt;, not &lt;=</span><br>
  <br>
  <span class="cmt"># What you actually wanted</span><br>
  <span class="fix">filtered = df[df["voltage_pu"] &lt; 0.95]</span>
</div>

A single character difference. The AI wasn't wrong about the approach — it was wrong about the boundary.

---

<!-- _class: step -->

<div class="step-badge">CHECK 02</div>

## Test Edge Cases

AI writes code for the happy path. Real data is never only the happy path.

<div class="review-card edge">
  <div class="rc-header">⚠️ Edge cases to test manually</div>
  <div class="rc-body">
    <span class="check">✦</span> Empty input — what happens if the DataFrame has zero rows?<br>
    <span class="check">✦</span> Missing values — does it handle <code>NaN</code> or <code>None</code> without silently dropping rows?<br>
    <span class="check">✦</span> Duplicate rows — does the logic still hold on repeated entries?<br>
    <span class="check">✦</span> Single-row input — some aggregations break on one row<br>
    <span class="check">✦</span> Unexpected types — string in a numeric column, negative where positive expected
  </div>
</div>

<div class="code-block">
  <span class="cmt"># AI assumed voltage_pu is always a float — but what if a row has "N/A"?</span><br>
  <span class="err">filtered = df[df["voltage_pu"] &lt; 0.95]  # TypeError on mixed types</span><br>
  <br>
  <span class="cmt"># Safer version — coerce to numeric, NaN rows will be excluded cleanly</span><br>
  <span class="fix">df["voltage_pu"] = pd.to_numeric(df["voltage_pu"], errors="coerce")</span><br>
  <span class="fix">filtered = df[df["voltage_pu"] &lt; 0.95]</span>
</div>

---

<!-- _class: step -->

<div class="step-badge">CHECK 03</div>

## Security Basics

You don't need to be a security engineer. You need to know the five most common AI security mistakes.

<div class="review-card security">
  <div class="rc-header">🔐 Security checks</div>
  <div class="rc-body">
    <span class="check">✦</span> Hardcoded credentials — API keys, passwords, tokens in the code itself<br>
    <span class="check">✦</span> SQL injection — string-formatted queries instead of parameterized ones<br>
    <span class="check">✦</span> User input used directly — filenames, paths, queries from untrusted sources<br>
    <span class="check">✦</span> Sensitive data in logs — PII, keys, or internal paths printed to console<br>
    <span class="check">✦</span> Overly permissive file writes — writing outside expected directories
  </div>
</div>

<div class="code-block">
  <span class="cmt"># AI wrote this — common and dangerous</span><br>
  <span class="err">API_KEY = "sk-abc123xyz"  # ← never hardcode credentials</span><br>
  <br>
  <span class="cmt"># Correct — load from environment variable</span><br>
  <span class="fix">import os</span><br>
  <span class="fix">API_KEY = os.environ.get("API_KEY")</span>
</div>

---

<!-- _class: step -->

<div class="step-badge">CHECK 04</div>

## Performance Checks

AI defaults to readable, not fast. For small datasets that's fine — at scale it matters.

<div class="two-col">
  <div class="col-card">
    <div class="label">🐢 Watch for these patterns</div>
    <p style="font-size:13px; margin-top:8px; color:#374151; line-height:1.9;">
      ✦ Loops over DataFrame rows — use vectorized operations instead<br>
      ✦ Reading the same file inside a loop<br>
      ✦ Loading entire files when you need 3 columns<br>
      ✦ No chunking for large CSV files
    </p>
  </div>
  <div class="col-card">
    <div class="label">⚡ Faster alternatives</div>
    <p style="font-size:13px; margin-top:8px; color:#374151; line-height:1.9;">
      ✦ <code>df.apply()</code> → vectorized column ops<br>
      ✦ <code>pd.read_csv(usecols=[...])</code> to load only needed columns<br>
      ✦ <code>pd.read_csv(chunksize=...)</code> for large files<br>
      ✦ <code>.loc</code> and boolean masks over loops
    </p>
  </div>
</div>

<div class="code-block">
  <span class="cmt"># AI wrote a row loop — works, but slow on large DataFrames</span><br>
  <span class="err">for i, row in df.iterrows():                    # O(n) Python loop</span><br>
  <span class="err">    df.at[i, "flag"] = "low" if row["v_pu"] &lt; 0.95 else "ok"</span><br>
  <br>
  <span class="cmt"># Vectorized — same result, 10-100x faster</span><br>
  <span class="fix">df["flag"] = df["v_pu"].apply(lambda v: "low" if v &lt; 0.95 else "ok")</span>
</div>

---

<!-- _class: step -->

<div class="step-badge">TECHNIQUE</div>

## Use AI to Review Itself

The most underused debugging technique: ask the same AI that wrote the code to critique it.

<div class="chat-mock">
  <div class="chat-row">
    <div class="chat-avatar user">👤</div>
    <div class="chat-bubble user-good">
      <div class="bubble-label">Self-review prompt</div>
      Review the code you just wrote. Check for: logic errors, unhandled edge cases (empty input, NaN values, wrong types), hardcoded values that should be parameters, and performance issues on large DataFrames. List any problems found. Be critical.
    </div>
  </div>
  <div class="chat-row">
    <div class="chat-avatar ai">✦</div>
    <div class="chat-bubble ai-warn">
      <div class="bubble-label">AI self-review response</div>
      Found 2 issues: (1) No handling for NaN in voltage_pu — will raise TypeError on mixed-type columns. (2) iterrows() loop will be slow on DataFrames over ~10k rows — suggest replacing with .apply() or boolean mask.
    </div>
  </div>
</div>

<div class="highlight good">

**The trick:** say "be critical" and "list problems found." Without those instructions, AI self-reviews tend to be flattering. Prompt it to look for problems, not to confirm the code is fine.

</div>

---

## The Code Review Checklist

<table class="review-table">
  <tr>
    <th>Area</th>
    <th>What to ask yourself</th>
    <th>How to test</th>
  </tr>
  <tr>
    <td><span class="area-tag logic">Logic</span></td>
    <td>Does it do exactly what I asked — boundaries, operators, return value?</td>
    <td>Run with known input. Check output manually.</td>
  </tr>
  <tr>
    <td><span class="area-tag edge">Edge cases</span></td>
    <td>What happens with empty, null, duplicate, or single-row input?</td>
    <td>Feed each edge case explicitly. Assert expected output.</td>
  </tr>
  <tr>
    <td><span class="area-tag security">Security</span></td>
    <td>Any hardcoded secrets? User input used directly? Sensitive data logged?</td>
    <td>Search for string literals. Check all <code>print()</code> calls.</td>
  </tr>
  <tr>
    <td><span class="area-tag perf">Performance</span></td>
    <td>Any row loops on DataFrames? Repeated file reads? Unnecessary full loads?</td>
    <td>Run with 10× your expected data size. Time it.</td>
  </tr>
  <tr>
    <td><span class="area-tag logic">Self-review</span></td>
    <td>Ask AI: "Review this code. Be critical. List problems found."</td>
    <td>Apply every fix it finds. Then run your own checks.</td>
  </tr>
</table>

---

<!-- _class: final -->

# AI writes the draft.
# You own the code.

&nbsp;

Logic · Edge cases · Security · Performance · Self-review. Five checks. Every time.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*