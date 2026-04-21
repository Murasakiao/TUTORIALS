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
    padding: 16px 22px;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #e5e7eb;
    line-height: 2;
    margin: 12px 0;
  }

  .code-block .kw   { color: #c4b5fd; }
  .code-block .prop { color: #93c5fd; }
  .code-block .val  { color: #86efac; }
  .code-block .sel  { color: #60a5fa; }
  .code-block .mq   { color: #f9a8d4; }
  .code-block .cmt  { color: #4b5563; font-style: italic; }
  .code-block .tag  { color: #60a5fa; }
  .code-block .attr { color: #86efac; }
  .code-block .str  { color: #fde68a; }

  /* Broken vs responsive device mock */
  .device-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin: 16px 0;
  }

  .device-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
  }

  .device-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 600;
  }

  .device-label.bad  { color: #f87171; }
  .device-label.good { color: #86efac; }

  .phone-frame {
    width: 120px;
    height: 210px;
    border-radius: 18px;
    border: 3px solid #374151;
    background: #0d1117;
    overflow: hidden;
    position: relative;
    flex-shrink: 0;
  }

  .phone-frame .phone-screen {
    width: 100%;
    height: 100%;
    padding: 8px 6px;
    display: flex;
    flex-direction: column;
    gap: 5px;
  }

  /* broken layout */
  .phone-frame.broken .phone-screen {
    overflow: hidden;
  }

  .broken-nav {
    background: #1d4ed8;
    height: 22px;
    width: 280px;
    border-radius: 3px;
    flex-shrink: 0;
  }

  .broken-hero {
    background: #374151;
    height: 60px;
    width: 280px;
    border-radius: 3px;
    flex-shrink: 0;
  }

  .broken-text {
    background: #1f2937;
    height: 8px;
    width: 260px;
    border-radius: 2px;
  }

  /* good layout */
  .good-nav {
    background: #1d4ed8;
    height: 22px;
    width: 100%;
    border-radius: 3px;
    flex-shrink: 0;
  }

  .good-hero {
    background: #374151;
    height: 60px;
    width: 100%;
    border-radius: 3px;
    flex-shrink: 0;
  }

  .good-text {
    background: #1f2937;
    height: 8px;
    width: 100%;
    border-radius: 2px;
  }

  .good-text.short { width: 75%; }

  /* DevTools step walkthrough */
  .devtools-steps {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .dt-step {
    background: #111827;
    border-radius: 8px;
    padding: 14px 16px;
  }

  .dt-step .dt-num {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 6px;
  }

  .dt-step .dt-action {
    font-size: 14px;
    font-weight: 600;
    color: #f0f6fc;
    margin-bottom: 4px;
  }

  .dt-step .dt-key {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: #60a5fa;
    margin-bottom: 4px;
  }

  .dt-step .dt-desc {
    font-size: 12px;
    color: #6b7280;
    line-height: 1.5;
  }

  /* Breakpoints cheatsheet table */
  .bp-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
    margin: 12px 0;
  }

  .bp-table th {
    background: var(--text);
    color: white;
    padding: 8px 14px;
    text-align: left;
    font-weight: 500;
    font-size: 12px;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.05em;
  }

  .bp-table td {
    padding: 9px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
    font-size: 13px;
  }

  .bp-table tr:nth-child(even) td { background: var(--off-white); }

  .bp-table .mono {
    font-family: 'DM Mono', monospace;
    color: var(--blue);
  }

  .bp-table .device-icon { font-size: 16px; }

  /* Two-column */
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

# Responsive Design
## What It Is and How to Test It

&nbsp;

**Your site looks great on desktop. Does it work on a phone?**

`viewport` · `media queries` · `breakpoints` · `DevTools`

---

## What Breaks on Mobile

Build a site for desktop, open it on a phone — here's what typically goes wrong:

<div class="device-compare">
  <div class="device-wrap">
    <div class="device-label bad">❌ Not responsive</div>
    <div class="phone-frame broken">
      <div class="phone-screen">
        <div class="broken-nav"></div>
        <div class="broken-hero"></div>
        <div class="broken-text"></div>
        <div class="broken-text"></div>
        <div class="broken-text"></div>
      </div>
    </div>
    <p style="font-size:12px; color:#f87171; text-align:center; font-family:'DM Mono',monospace;">content overflows · tiny text<br>horizontal scrollbar appears</p>
  </div>
  <div class="device-wrap">
    <div class="device-label good">✅ Responsive</div>
    <div class="phone-frame">
      <div class="phone-screen">
        <div class="good-nav"></div>
        <div class="good-hero"></div>
        <div class="good-text"></div>
        <div class="good-text short"></div>
        <div class="good-text"></div>
        <div class="good-text short"></div>
      </div>
    </div>
    <p style="font-size:12px; color:#86efac; text-align:center; font-family:'DM Mono',monospace;">layout adapts · text readable<br>no overflow</p>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## What Responsive Design Means

Responsive design means your layout **adapts to the screen it's being viewed on** — automatically.

<div class="tools">
  <div class="tool-card">
    <div class="icon">📐</div>
    <div class="name">Fluid layouts</div>
    <div class="desc">Use percentages and relative units instead of fixed pixel widths.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔀</div>
    <div class="name">Flexible content</div>
    <div class="desc">Images and text scale with their container rather than overflowing it.</div>
  </div>
  <div class="tool-card">
    <div class="icon">📏</div>
    <div class="name">Media queries</div>
    <div class="desc">CSS rules that activate only when the screen crosses a certain width.</div>
  </div>
  <div class="tool-card">
    <div class="icon">📱</div>
    <div class="name">Mobile-first</div>
    <div class="desc">Write styles for small screens first, then add complexity for larger ones.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## The Viewport Meta Tag

This one line in your `<head>` is required on every site. Without it, mobile browsers zoom out to fit a desktop-width page — making everything tiny.

<div class="code-block">
  <span class="cmt">&lt;!-- Put this inside &lt;head&gt; --&gt;</span><br>
  <span class="tag">&lt;meta</span> <span class="attr">name</span>=<span class="str">"viewport"</span><br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="attr">content</span>=<span class="str">"width=device-width, initial-scale=1.0"</span><span class="tag">&gt;</span>
</div>

<div class="two-col">
  <div class="col-card">
    <div class="label">width=device-width</div>
    <p style="font-size:14px; margin-top:8px;">Tells the browser to use the actual screen width as the layout width — not a virtual 980px desktop width.</p>
  </div>
  <div class="col-card">
    <div class="label">initial-scale=1.0</div>
    <p style="font-size:14px; margin-top:8px;">Sets the starting zoom level to 1 — no zoom in or out on first load.</p>
  </div>
</div>

<div class="highlight warn">

⚠️ This tag does nothing visual on desktop. It only matters on mobile — but without it, all your responsive CSS is ignored.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Media Queries in Plain English

A media query says: **"apply these styles only when the screen is this wide."**

<div class="code-block">
  <span class="cmt">/* Base styles — apply to all screens */</span><br>
  <span class="sel">.container</span> {<br>
  &nbsp;&nbsp;<span class="prop">width</span>: <span class="val">80%</span>;<br>
  &nbsp;&nbsp;<span class="prop">font-size</span>: <span class="val">18px</span>;<br>
  }<br>
  <span class="cmt">/* Tablet — screens 768px wide or narrower */</span><br>
  <span class="mq">@media</span> (<span class="prop">max-width</span>: <span class="val">768px</span>) {<br>
  &nbsp;&nbsp;<span class="sel">.container</span> {<br>
  &nbsp;&nbsp;&nbsp;&nbsp;<span class="prop">width</span>: <span class="val">95%</span>;<br>
  &nbsp;&nbsp;&nbsp;&nbsp;<span class="prop">font-size</span>: <span class="val">16px</span>;<br>
  &nbsp;&nbsp;}<br>
  }<br>
  <span class="cmt">/* Mobile — screens 480px wide or narrower */</span><br>
  <span class="mq">@media</span> (<span class="prop">max-width</span>: <span class="val">480px</span>) {<br>
  &nbsp;&nbsp;<span class="sel">.nav-links</span> { <span class="prop">display</span>: <span class="val">none</span>; } <span class="cmt">/* hide nav items */</span><br>
  }
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## How to Test in Chrome DevTools

No phone needed — Chrome can simulate any device size.

<div class="devtools-steps">
  <div class="dt-step">
    <div class="dt-num">01 — Open</div>
    <div class="dt-action">Open DevTools</div>
    <div class="dt-key">F12 &nbsp;or&nbsp; ⌘ + Opt + I</div>
    <div class="dt-desc">Opens the browser's inspector panel. Works on any page.</div>
  </div>
  <div class="dt-step">
    <div class="dt-num">02 — Toggle</div>
    <div class="dt-action">Device Mode</div>
    <div class="dt-key">Ctrl+Shift+M &nbsp;/&nbsp; ⌘+Shift+M</div>
    <div class="dt-desc">Switches the view to a resizable mobile frame. Look for the phone icon.</div>
  </div>
  <div class="dt-step">
    <div class="dt-num">03 — Simulate</div>
    <div class="dt-action">Pick a Device</div>
    <div class="dt-key">Dropdown at top</div>
    <div class="dt-desc">Choose iPhone 14, Pixel 7, iPad, or drag to any custom width.</div>
  </div>
</div>

&nbsp;

<div class="highlight">

**Drag the edge** of the device frame to see exactly where your layout breaks. The pixel width shown at the top tells you which media query is active.

</div>

---

## Common Breakpoints Cheatsheet

<table class="bp-table">
  <tr>
    <th>Device</th>
    <th>Breakpoint</th>
    <th>CSS Media Query</th>
    <th>Common use</th>
  </tr>
  <tr>
    <td><span class="device-icon">📱</span> Mobile S</td>
    <td class="mono">≤ 320px</td>
    <td class="mono">max-width: 320px</td>
    <td>Small phones, single column</td>
  </tr>
  <tr>
    <td><span class="device-icon">📱</span> Mobile L</td>
    <td class="mono">≤ 480px</td>
    <td class="mono">max-width: 480px</td>
    <td>Most phones in portrait</td>
  </tr>
  <tr>
    <td><span class="device-icon">📟</span> Tablet</td>
    <td class="mono">≤ 768px</td>
    <td class="mono">max-width: 768px</td>
    <td>Tablets, landscape phones</td>
  </tr>
  <tr>
    <td><span class="device-icon">💻</span> Laptop</td>
    <td class="mono">≤ 1024px</td>
    <td class="mono">max-width: 1024px</td>
    <td>Small laptops, iPad Pro</td>
  </tr>
  <tr>
    <td><span class="device-icon">🖥️</span> Desktop</td>
    <td class="mono">≤ 1280px</td>
    <td class="mono">max-width: 1280px</td>
    <td>Standard desktop widths</td>
  </tr>
  <tr>
    <td><span class="device-icon">🖥️</span> Wide</td>
    <td class="mono">≥ 1536px</td>
    <td class="mono">min-width: 1536px</td>
    <td>Large monitors, cap content width</td>
  </tr>
</table>

---

<!-- _class: final -->

# Build for mobile first.
# Scale up from there.

&nbsp;

Most web traffic is mobile. Design for the small screen and everything else gets easier.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*