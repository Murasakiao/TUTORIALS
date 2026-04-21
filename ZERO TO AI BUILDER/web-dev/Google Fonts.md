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

  /* ── Code block ── */
  .code-block {
    background: #111827;
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .code-block .cb-bar {
    background: #1f2937;
    padding: 8px 16px;
    font-size: 11.5px;
    color: #6b7280;
    letter-spacing: 0.04em;
  }

  .code-block .cb-body {
    padding: 14px 20px;
    line-height: 2;
  }

  .cb-tag   { color: #f87171; }
  .cb-attr  { color: #93c5fd; }
  .cb-val   { color: #34d399; }
  .cb-str   { color: #fde68a; }
  .cb-prop  { color: #93c5fd; }
  .cb-sel   { color: #f9fafb; }
  .cb-cmt   { color: #4b5563; font-style: italic; }
  .cb-punct { color: #6b7280; }
  .cb-url   { color: #34d399; }

  /* ── Two-column layout ── */
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

  /* ── Font preview cards ── */
  .font-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 14px;
  }

  .font-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
  }

  .font-card .fc-preview {
    background: var(--off-white);
    padding: 16px 18px 12px;
    border-bottom: 1px solid var(--border);
  }

  .font-card .fc-heading {
    font-size: 22px;
    font-weight: 700;
    color: var(--text);
    line-height: 1.2;
    margin-bottom: 4px;
  }

  .font-card .fc-body {
    font-size: 13px;
    color: var(--muted);
    line-height: 1.5;
  }

  .font-card .fc-info {
    padding: 10px 18px;
  }

  .font-card .fc-name {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
  }

  .font-card .fc-tags {
    display: flex;
    gap: 6px;
    margin-top: 5px;
    flex-wrap: wrap;
  }

  .font-card .fc-tag {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    color: var(--blue);
    background: var(--blue-light);
    padding: 2px 8px;
    border-radius: 4px;
    border: 1px solid var(--blue-mid);
  }

  /* ── Before / after font comparison ── */
  .before-after {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 16px;
  }

  .ba-card {
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .ba-card .ba-label {
    padding: 7px 16px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.07em;
    text-transform: uppercase;
  }

  .ba-card.before .ba-label { background: #fef2f2; color: #991b1b; }
  .ba-card.after  .ba-label { background: #f0fdf4; color: #166534; }

  .ba-card .ba-content {
    background: var(--white);
    padding: 16px 18px;
  }

  .ba-card.before .ba-content .ba-heading {
    font-family: Arial, sans-serif;
    font-size: 20px;
    font-weight: bold;
    color: var(--text);
    margin-bottom: 6px;
  }

  .ba-card.after .ba-content .ba-heading {
    font-family: 'DM Sans', sans-serif;
    font-size: 20px;
    font-weight: 600;
    color: var(--text);
    margin-bottom: 6px;
  }

  .ba-card .ba-content .ba-body {
    font-size: 13px;
    color: var(--muted);
    line-height: 1.55;
  }

  .ba-card.before .ba-content .ba-body { font-family: Arial, sans-serif; }
  .ba-card.after  .ba-content .ba-body { font-family: 'DM Sans', sans-serif; }

  /* ── Pairing row ── */
  .pair-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .pair-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 16px;
  }

  .pair-card .p-display {
    font-size: 17px;
    font-weight: 700;
    color: var(--text);
    line-height: 1.2;
    margin-bottom: 4px;
  }

  .pair-card .p-body {
    font-size: 12px;
    color: var(--muted);
    line-height: 1.5;
    margin-bottom: 8px;
  }

  .pair-card .p-tag {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--blue);
    background: var(--blue-light);
    padding: 2px 7px;
    border-radius: 4px;
    border: 1px solid var(--blue-mid);
    display: inline-block;
  }

  /* ── Weight comparison ── */
  .weight-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
    margin: 14px 0;
  }

  .weight-table th {
    background: var(--text);
    color: white;
    padding: 8px 14px;
    text-align: left;
    font-weight: 500;
    font-size: 12px;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.05em;
  }

  .weight-table td {
    padding: 9px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
  }

  .weight-table tr:nth-child(even) td { background: var(--off-white); }

  .weight-table .mono {
    font-family: 'DM Mono', monospace;
    color: var(--blue);
    font-size: 13px;
  }

  .weight-table .good { color: #059669; font-weight: 600; }
  .weight-table .bad  { color: #dc2626; font-weight: 600; }

  /* ── Cmd grid ── */
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

# Google Fonts in
# 2 Minutes

&nbsp;

**Two lines of code.** Your site never looks the same again.

`@import` · `font-family` · `font-weight` · `display=swap`

---

## Why Default Fonts Look Amateur

The browser's default fonts were designed for operating systems — not websites.

<div class="before-after">
  <div class="ba-card before">
    <div class="ba-label">❌ &nbsp;Without Google Fonts</div>
    <div class="ba-content">
      <div class="ba-heading">Welcome to My Site</div>
      <div class="ba-body">This is what Arial looks like as your body font. It's fine, technically. But it signals nothing was decided intentionally here.</div>
    </div>
  </div>
  <div class="ba-card after">
    <div class="ba-label">✅ &nbsp;With Google Fonts</div>
    <div class="ba-content">
      <div class="ba-heading">Welcome to My Site</div>
      <div class="ba-body">Same words. Different font. The page immediately feels considered, designed, and trustworthy — without changing anything else.</div>
    </div>
  </div>
</div>

<div class="highlight" style="margin-top: 18px;">

**The rule:** Visitors don't notice good typography. They only notice bad typography — and they feel it as distrust, not a font complaint.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## What Google Fonts Is

<div class="tools">
  <div class="tool-card">
    <div class="icon">🆓</div>
    <div class="name">Completely free</div>
    <div class="desc">Over 1,500 font families. No license fees, no attribution required, no account needed.</div>
  </div>
  <div class="tool-card">
    <div class="icon">☁️</div>
    <div class="name">Hosted by Google</div>
    <div class="desc">You link to Google's servers. They serve the font file to your visitors — you don't host anything.</div>
  </div>
  <div class="tool-card">
    <div class="icon">⚡</div>
    <div class="name">Cached globally</div>
    <div class="desc">If a visitor already loaded the font on another site, their browser uses the cached version. Effectively instant.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔗</div>
    <div class="name">Two ways to load</div>
    <div class="desc">Via an HTML <code>&lt;link&gt;</code> tag in your <code>&lt;head&gt;</code>, or a CSS <code>@import</code> at the top of your stylesheet. Both work.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Pick a Font — and a Pairing

Go to **fonts.google.com**, search, and click a font to grab its embed code. Here are four reliable starting points:

<div class="font-grid">
  <div class="font-card">
    <div class="fc-preview">
      <div class="fc-heading" style="font-family:'DM Sans',sans-serif;">The quick brown fox</div>
      <div class="fc-body" style="font-family:'DM Sans',sans-serif;">Body text feels clean and modern at any size.</div>
    </div>
    <div class="fc-info">
      <div class="fc-name">Inter</div>
      <div class="fc-tags">
        <span class="fc-tag">sans-serif</span>
        <span class="fc-tag">neutral</span>
        <span class="fc-tag">SaaS / dashboards</span>
      </div>
    </div>
  </div>
  <div class="font-card">
    <div class="fc-preview">
      <div class="fc-heading" style="font-family:Georgia,serif; font-size:21px;">The quick brown fox</div>
      <div class="fc-body" style="font-family:Georgia,serif;">Body text with warmth, character, and good rhythm.</div>
    </div>
    <div class="fc-info">
      <div class="fc-name">Lora</div>
      <div class="fc-tags">
        <span class="fc-tag">serif</span>
        <span class="fc-tag">editorial</span>
        <span class="fc-tag">blogs / articles</span>
      </div>
    </div>
  </div>
  <div class="font-card">
    <div class="fc-preview">
      <div class="fc-heading" style="font-family:'DM Sans',sans-serif; letter-spacing:-0.02em; font-size:21px;">The quick brown fox</div>
      <div class="fc-body" style="font-family:'DM Sans',sans-serif;">Tight, confident heading presence on landing pages.</div>
    </div>
    <div class="fc-info">
      <div class="fc-name">Manrope</div>
      <div class="fc-tags">
        <span class="fc-tag">sans-serif</span>
        <span class="fc-tag">geometric</span>
        <span class="fc-tag">landing pages</span>
      </div>
    </div>
  </div>
  <div class="font-card">
    <div class="fc-preview">
      <div class="fc-heading" style="font-family:'DM Mono',monospace; font-size:19px;">The quick brown fox</div>
      <div class="fc-body" style="font-family:'DM Mono',monospace; font-size:12px;">Code samples, labels, and developer-facing UIs.</div>
    </div>
    <div class="fc-info">
      <div class="fc-name">JetBrains Mono</div>
      <div class="fc-tags">
        <span class="fc-tag">monospace</span>
        <span class="fc-tag">code</span>
        <span class="fc-tag">dev tools</span>
      </div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Font Pairing Tips

One font for headings, one for body. That's the whole system.

<div class="pair-grid">
  <div class="pair-card">
    <div class="p-display" style="font-family:'DM Sans',sans-serif;">Heading</div>
    <div class="p-body" style="font-family:Georgia,serif;">Body text flows here with a contrasting personality that makes headings feel intentional.</div>
    <span class="p-tag">Manrope + Lora</span>
  </div>
  <div class="pair-card">
    <div class="p-display" style="font-family:'DM Sans',sans-serif; font-size:18px;">Heading</div>
    <div class="p-body" style="font-family:'DM Sans',sans-serif;">Stick to one font family in two weights. Clean, minimal, and harder to mess up.</div>
    <span class="p-tag">Inter 700 + Inter 400</span>
  </div>
  <div class="pair-card">
    <div class="p-display" style="font-family:'DM Sans',sans-serif; letter-spacing:-0.02em;">Heading</div>
    <div class="p-body" style="font-family:'DM Mono',monospace; font-size:11px;">Mono body works for developer tools, documentation, and technical blogs.</div>
    <span class="p-tag">Manrope + JetBrains</span>
  </div>
</div>

&nbsp;

<div class="cmd-grid">
  <div class="cmd-row">
    <div class="cmd-name" style="min-width:90px;">Serif + Sans</div>
    <div class="cmd-desc">Classic editorial contrast<span>Lora headings + Inter body</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name" style="min-width:90px;">Sans + Sans</div>
    <div class="cmd-desc">Safe, always works, minimal risk<span>One family, two weights</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name" style="min-width:90px;">Sans + Mono</div>
    <div class="cmd-desc">Developer / technical aesthetic<span>Geometric heading + mono body</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name" style="min-width:90px;">Avoid</div>
    <div class="cmd-desc">Two decorative or two serif fonts<span>They compete instead of contrasting</span></div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## The 2-Line Install

**Method A — HTML `<link>` tag** (recommended for most sites):

<div class="code-block">
  <div class="cb-bar">index.html — inside &lt;head&gt;, before your stylesheet</div>
  <div class="cb-body">
    <span class="cb-cmt">&lt;!-- Paste this BEFORE your &lt;link rel="stylesheet"&gt; --&gt;</span><br>
    <span class="cb-tag">&lt;link</span> <span class="cb-attr">rel</span><span class="cb-punct">=</span><span class="cb-str">"preconnect"</span> <span class="cb-attr">href</span><span class="cb-punct">=</span><span class="cb-str">"https://fonts.googleapis.com"</span><span class="cb-tag">&gt;</span><br>
    <span class="cb-tag">&lt;link</span> <span class="cb-attr">rel</span><span class="cb-punct">=</span><span class="cb-str">"preconnect"</span> <span class="cb-attr">href</span><span class="cb-punct">=</span><span class="cb-str">"https://fonts.gstatic.com"</span> <span class="cb-attr">crossorigin</span><span class="cb-tag">&gt;</span><br>
    <span class="cb-tag">&lt;link</span> <span class="cb-attr">href</span><span class="cb-punct">=</span><span class="cb-str">"https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap"</span> <span class="cb-attr">rel</span><span class="cb-punct">=</span><span class="cb-str">"stylesheet"</span><span class="cb-tag">&gt;</span>
  </div>
</div>

**Method B — CSS `@import`** (for stylesheet-only setups):

<div class="code-block">
  <div class="cb-bar">style.css — very first line of the file</div>
  <div class="cb-body">
    <span class="cb-cmt">/* Must be the absolute first line — nothing above it */</span><br>
    <span class="cb-prop">@import</span> <span class="cb-url">url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap')</span><span class="cb-punct">;</span>
  </div>
</div>

<div class="highlight">

**Which to use:** The `<link>` method is faster — it loads in parallel with your HTML. The `@import` method blocks rendering until the CSS file loads. Use `<link>` unless you have no access to the HTML.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Apply It in CSS

Loading the font doesn't use it. You still need to assign it in your stylesheet.

<div class="code-block">
  <div class="cb-bar">style.css</div>
  <div class="cb-body">
    <span class="cb-cmt">/* Apply to everything */</span><br>
    <span class="cb-sel">body</span> <span class="cb-punct">{</span><br>
    &nbsp;&nbsp;<span class="cb-prop">font-family</span><span class="cb-punct">:</span> <span class="cb-str">'Inter'</span><span class="cb-punct">,</span> <span class="cb-val">sans-serif</span><span class="cb-punct">;</span><br>
    &nbsp;&nbsp;<span class="cb-prop">font-weight</span><span class="cb-punct">:</span> <span class="cb-val">400</span><span class="cb-punct">;</span> <span class="cb-cmt">/* regular */</span><br>
    <span class="cb-punct">}</span><br>
    <br>
    <span class="cb-cmt">/* Heavier weight for headings */</span><br>
    <span class="cb-sel">h1</span><span class="cb-punct">,</span> <span class="cb-sel">h2</span><span class="cb-punct">,</span> <span class="cb-sel">h3</span> <span class="cb-punct">{</span><br>
    &nbsp;&nbsp;<span class="cb-prop">font-family</span><span class="cb-punct">:</span> <span class="cb-str">'Inter'</span><span class="cb-punct">,</span> <span class="cb-val">sans-serif</span><span class="cb-punct">;</span><br>
    &nbsp;&nbsp;<span class="cb-prop">font-weight</span><span class="cb-punct">:</span> <span class="cb-val">600</span><span class="cb-punct">;</span> <span class="cb-cmt">/* semibold */</span><br>
    <span class="cb-punct">}</span>
  </div>
</div>

Always include a **fallback font** after the comma — `sans-serif`, `serif`, or `monospace`. If Google Fonts fails to load, the browser falls back gracefully instead of showing the OS default.

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Performance Tip — Limit to 2 Weights

Every font weight you request is a separate file download.

<table class="weight-table">
  <tr>
    <th>What you load</th>
    <th>Extra requests</th>
    <th>Verdict</th>
  </tr>
  <tr>
    <td>Inter 400 only</td>
    <td>1 file</td>
    <td class="good">✓ Fast</td>
  </tr>
  <tr>
    <td>Inter 400 + 600</td>
    <td>2 files</td>
    <td class="good">✓ Ideal</td>
  </tr>
  <tr>
    <td>Inter 300 + 400 + 500 + 600 + 700</td>
    <td>5 files</td>
    <td class="bad">✗ Slow</td>
  </tr>
  <tr>
    <td>Inter + Lora + Playfair Display</td>
    <td>6+ files</td>
    <td class="bad">✗ Very slow</td>
  </tr>
</table>

<div class="two-col" style="margin-top: 14px;">
  <div class="col-card">
    <div class="label">URL for 2 weights</div>
    <p style="font-family:'DM Mono',monospace; font-size:11.5px; color:#2563eb; margin-top:8px; line-height:1.8;">…family=Inter:wght@<strong>400;600</strong>&display=swap</p>
    <p style="font-size:13px; color:var(--muted); margin-top:4px;">Separate weights with semicolons in the URL. One request, two weights.</p>
  </div>
  <div class="col-card">
    <div class="label">The display=swap trick</div>
    <p style="font-size:13px; color:var(--text); margin-top:8px;">Always include <code>display=swap</code> in your URL. It tells the browser to show fallback text immediately while the font loads — no invisible text flash.</p>
  </div>
</div>

---

## Google Fonts Quick Reference

<table class="weight-table">
  <tr>
    <th>Task</th>
    <th>How to do it</th>
  </tr>
  <tr>
    <td>Find a font</td>
    <td>Go to fonts.google.com → search → click → "Get font" → "Get embed code"</td>
  </tr>
  <tr>
    <td>Load via HTML</td>
    <td>Paste the <code>&lt;link&gt;</code> tags inside <code>&lt;head&gt;</code>, before your stylesheet</td>
  </tr>
  <tr>
    <td>Load via CSS</td>
    <td><code>@import url('...')</code> as the very first line of your CSS file</td>
  </tr>
  <tr>
    <td>Use the font</td>
    <td>Set <code>font-family: 'Font Name', sans-serif</code> on <code>body</code> or individual elements</td>
  </tr>
  <tr>
    <td>Add bold headings</td>
    <td>Request weight 600 or 700 in the URL, then set <code>font-weight: 600</code> on headings</td>
  </tr>
  <tr>
    <td>Pair two fonts</td>
    <td>Add both to the URL: <code>…family=Inter&family=Lora&display=swap</code></td>
  </tr>
  <tr>
    <td>Prevent invisible text</td>
    <td>Add <code>&display=swap</code> to the end of your Google Fonts URL</td>
  </tr>
  <tr>
    <td>Keep it fast</td>
    <td>Max 2 font families, max 2 weights each. Always include the preconnect tags</td>
  </tr>
  <tr>
    <td>Add a fallback</td>
    <td>Always write <code>'Font Name', sans-serif</code> — never rely on the Google Font alone</td>
  </tr>
</table>

---

<!-- _class: final -->

# Two lines of code.
# A completely different site.

&nbsp;

Pick a font. Paste the link. Set the family. Done.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*