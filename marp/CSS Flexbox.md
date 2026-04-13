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

  .cb-prop  { color: #93c5fd; }
  .cb-val   { color: #34d399; }
  .cb-sel   { color: #f9fafb; }
  .cb-cmt   { color: #4b5563; font-style: italic; }
  .cb-punct { color: #6b7280; }

  /* ── Flex visual demo box ── */
  .demo-wrap {
    margin: 14px 0 6px;
  }

  .demo-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 8px;
  }

  .demo-container {
    background: #dbeafe;
    border: 2px dashed #93c5fd;
    border-radius: 10px;
    padding: 12px;
    display: flex;
    gap: 8px;
    min-height: 64px;
    align-items: stretch;
  }

  .demo-item {
    background: #2563eb;
    color: white;
    border-radius: 6px;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    display: flex;
    align-items: center;
    justify-content: center;
    min-width: 44px;
    padding: 0 10px;
    height: 40px;
  }

  .demo-item.tall { height: 64px; }
  .demo-item.short { height: 28px; }
  .demo-item.grow { flex-grow: 1; }
  .demo-item.b { background: #1d4ed8; }
  .demo-item.c { background: #1e40af; }

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

  /* ── Property reference grid ── */
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

  /* ── Property demo card (side-by-side code + visual) ── */
  .prop-demo {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 14px 0;
  }

  .prop-demo .pd-code {
    background: #111827;
    border-radius: 10px;
    padding: 14px 18px;
    font-family: 'DM Mono', monospace;
    font-size: 12.5px;
    line-height: 2;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .prop-demo .pd-visual {
    background: #dbeafe;
    border: 2px dashed #93c5fd;
    border-radius: 10px;
    padding: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 90px;
  }

  /* ── Layout showcase ── */
  .layout-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 14px;
    margin-top: 16px;
  }

  .layout-card {
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
  }

  .layout-card .lc-preview {
    background: #f1f5f9;
    padding: 14px;
    min-height: 90px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .layout-card .lc-info {
    padding: 10px 14px;
    background: var(--white);
    border-top: 1px solid var(--border);
  }

  .layout-card .lc-name {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
  }

  .layout-card .lc-css {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    color: var(--blue);
    margin-top: 3px;
  }

  /* mini flex items for layout previews */
  .mi {
    background: #2563eb;
    border-radius: 4px;
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  /* ── Cheatsheet table ── */
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
    font-size: 12.5px;
  }

  .cheat-table .val {
    font-family: 'DM Mono', monospace;
    color: #059669;
    font-size: 12px;
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

# CSS Flexbox
## in 5 Minutes

&nbsp;

**Stop fighting layouts.** One property changes everything.

`display: flex` · `justify-content` · `align-items` · `flex-wrap` · `gap`

---

## The Old Way Was a Mess

Before Flexbox, centering a div was a Stack Overflow adventure.

<div class="tools">
  <div class="tool-card">
    <div class="icon">🏚️</div>
    <div class="name">Floats</div>
    <div class="desc">Designed for text wrapping around images. Developers abused them for layout. Required clearfix hacks to not collapse.</div>
  </div>
  <div class="tool-card">
    <div class="icon">📊</div>
    <div class="name">Tables</div>
    <div class="desc">Semantically wrong. <code>&lt;table&gt;</code> is for tabular data — not for making a three-column page layout. But people did it anyway.</div>
  </div>
  <div class="tool-card">
    <div class="icon">📐</div>
    <div class="name">inline-block</div>
    <div class="desc">Close — but produced mysterious whitespace gaps between elements, and vertical alignment was still a nightmare.</div>
  </div>
  <div class="tool-card">
    <div class="icon">✅</div>
    <div class="name">Flexbox (2015)</div>
    <div class="desc">A layout model built for UI. Distribute space, align items, reorder content — all without hacks. Now supported everywhere.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## The Parent-Child Mental Model

Flexbox works on a **container and its direct children**. Nothing else.

<div class="two-col">
  <div class="col-card">
    <div class="label">The container (parent)</div>
    <p style="font-size:13.5px; margin-top:8px;">You set <code>display: flex</code> on the parent. This makes it the <strong>flex container</strong>. It controls how its children are arranged.</p>
    <p style="font-size:13.5px; margin-top:8px;">Properties live here: <code>justify-content</code>, <code>align-items</code>, <code>flex-wrap</code>, <code>gap</code>, <code>flex-direction</code>.</p>
  </div>
  <div class="col-card">
    <div class="label">The items (children)</div>
    <p style="font-size:13.5px; margin-top:8px;">Direct children become <strong>flex items</strong> automatically. They respond to the container's rules.</p>
    <p style="font-size:13.5px; margin-top:8px;">Properties live here: <code>flex-grow</code>, <code>flex-shrink</code>, <code>align-self</code>, <code>order</code>.</p>
  </div>
</div>

<div class="demo-wrap" style="margin-top:18px;">
  <div class="demo-label">flex container → flex items</div>
  <div class="demo-container">
    <div class="demo-item">A</div>
    <div class="demo-item b">B</div>
    <div class="demo-item c">C</div>
  </div>
</div>

<div class="highlight">

**Key rule:** Flexbox only affects the direct children of the container. Grandchildren are unaffected unless you also set <code>display: flex</code> on the child.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## 5 Properties You'll Use 90% of the Time

<div class="cmd-grid">
  <div class="cmd-row">
    <div class="cmd-name">display: flex</div>
    <div class="cmd-desc">Turns on flexbox for a container<span>Everything else requires this first</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">flex-direction</div>
    <div class="cmd-desc">Row (default) or column layout<span>row · column · row-reverse · column-reverse</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">justify-content</div>
    <div class="cmd-desc">Align items along the main axis<span>flex-start · center · space-between · space-around</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">align-items</div>
    <div class="cmd-desc">Align items along the cross axis<span>stretch · center · flex-start · flex-end</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">flex-wrap</div>
    <div class="cmd-desc">Let items wrap to the next line<span>nowrap (default) · wrap · wrap-reverse</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">gap</div>
    <div class="cmd-desc">Space between items — no margin hacks<span>gap: 16px · gap: 8px 24px (row col)</span></div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## `justify-content` — Main Axis

Controls how items are spaced **along the main axis** (horizontal by default).

<div class="prop-demo">
  <div class="pd-code">
    <span class="cb-sel">.container</span> <span class="cb-punct">{</span><br>
    &nbsp;&nbsp;<span class="cb-prop">display</span><span class="cb-punct">:</span> <span class="cb-val">flex</span><span class="cb-punct">;</span><br>
    &nbsp;&nbsp;<span class="cb-prop">justify-content</span><span class="cb-punct">:</span> <span class="cb-val">space-between</span><span class="cb-punct">;</span><br>
    <span class="cb-punct">}</span>
  </div>
  <div class="pd-visual" style="justify-content: space-between;">
    <div class="mi" style="width:44px; height:40px;">A</div>
    <div class="mi" style="width:44px; height:40px;">B</div>
    <div class="mi" style="width:44px; height:40px;">C</div>
  </div>
</div>

<div class="cmd-grid" style="margin-top:4px;">
  <div class="cmd-row">
    <div class="cmd-name" style="min-width:130px;">flex-start</div>
    <div class="cmd-desc">Pack items to the left<span>Default behavior</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name" style="min-width:130px;">center</div>
    <div class="cmd-desc">Center items horizontally<span>The one-liner centering fix</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name" style="min-width:130px;">space-between</div>
    <div class="cmd-desc">First and last item hug edges<span>Space distributed between items</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name" style="min-width:130px;">space-around</div>
    <div class="cmd-desc">Equal space around each item<span>Half space on the outer edges</span></div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## `align-items` — Cross Axis

Controls how items align **perpendicular to the main axis** (vertical by default).

<div class="prop-demo">
  <div class="pd-code">
    <span class="cb-sel">.container</span> <span class="cb-punct">{</span><br>
    &nbsp;&nbsp;<span class="cb-prop">display</span><span class="cb-punct">:</span> <span class="cb-val">flex</span><span class="cb-punct">;</span><br>
    &nbsp;&nbsp;<span class="cb-prop">align-items</span><span class="cb-punct">:</span> <span class="cb-val">center</span><span class="cb-punct">;</span><br>
    &nbsp;&nbsp;<span class="cb-prop">height</span><span class="cb-punct">:</span> <span class="cb-val">100px</span><span class="cb-punct">;</span><br>
    <span class="cb-punct">}</span>
  </div>
  <div class="pd-visual" style="align-items: center; height:100px;">
    <div class="mi" style="width:44px; height:64px;">A</div>
    <div class="mi b" style="width:44px; height:36px;">B</div>
    <div class="mi c" style="width:44px; height:50px;">C</div>
  </div>
</div>

<div class="cmd-grid" style="margin-top:4px;">
  <div class="cmd-row">
    <div class="cmd-name" style="min-width:110px;">stretch</div>
    <div class="cmd-desc">Items fill container height<span>Default — items grow to match tallest</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name" style="min-width:110px;">center</div>
    <div class="cmd-desc">Items centered vertically<span>The vertical centering holy grail</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name" style="min-width:110px;">flex-start</div>
    <div class="cmd-desc">Items align to the top<span>Regardless of their height</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name" style="min-width:110px;">flex-end</div>
    <div class="cmd-desc">Items align to the bottom<span>Useful for baseline-aligned footers</span></div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## `flex-wrap` and `gap`

Two properties that make responsive layouts nearly effortless.

<div class="two-col">
  <div class="col-card">
    <div class="label">flex-wrap: wrap</div>
    <div class="code-block" style="margin-top:10px;">
      <div class="cb-body" style="padding:10px 14px; line-height:1.9;">
        <span class="cb-sel">.container</span> <span class="cb-punct">{</span><br>
        &nbsp;&nbsp;<span class="cb-prop">display</span><span class="cb-punct">:</span> <span class="cb-val">flex</span><span class="cb-punct">;</span><br>
        &nbsp;&nbsp;<span class="cb-prop">flex-wrap</span><span class="cb-punct">:</span> <span class="cb-val">wrap</span><span class="cb-punct">;</span><br>
        <span class="cb-punct">}</span>
      </div>
    </div>
    <p style="font-size:13px; color:var(--muted); margin-top:8px;">When items don't fit on one line, they wrap to the next. No overflow, no horizontal scroll.</p>
  </div>
  <div class="col-card">
    <div class="label">gap</div>
    <div class="code-block" style="margin-top:10px;">
      <div class="cb-body" style="padding:10px 14px; line-height:1.9;">
        <span class="cb-sel">.container</span> <span class="cb-punct">{</span><br>
        &nbsp;&nbsp;<span class="cb-prop">display</span><span class="cb-punct">:</span> <span class="cb-val">flex</span><span class="cb-punct">;</span><br>
        &nbsp;&nbsp;<span class="cb-prop">gap</span><span class="cb-punct">:</span> <span class="cb-val">16px</span><span class="cb-punct">;</span><br>
        <span class="cb-punct">}</span>
      </div>
    </div>
    <p style="font-size:13px; color:var(--muted); margin-top:8px;">Replaces margin hacks between items. Works in both directions. Supported in all modern browsers.</p>
  </div>
</div>

<div class="highlight" style="margin-top:16px;">

**The responsive card pattern:** `display: flex` + `flex-wrap: wrap` + `gap: 16px` + a `min-width` on each item. That's it. Cards reflow automatically at any screen width.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 06</div>

## Common Layouts Built with Flexbox

<div class="layout-grid">

  <div class="layout-card">
    <div class="lc-preview">
      <div style="display:flex; justify-content:center; align-items:center; height:62px;">
        <div class="mi" style="width:80px; height:40px; font-size:11px;">centered</div>
      </div>
    </div>
    <div class="lc-info">
      <div class="lc-name">Perfect Center</div>
      <div class="lc-css">justify-content: center;<br>align-items: center;</div>
    </div>
  </div>

  <div class="layout-card">
    <div class="lc-preview">
      <div style="display:flex; justify-content:space-between; align-items:center; height:62px; padding:0 8px;">
        <div class="mi" style="width:36px; height:28px; font-size:10px;">logo</div>
        <div style="display:flex; gap:6px;">
          <div class="mi" style="width:28px; height:22px; font-size:9px;">nav</div>
          <div class="mi b" style="width:28px; height:22px; font-size:9px;">nav</div>
          <div class="mi c" style="width:28px; height:22px; font-size:9px;">nav</div>
        </div>
      </div>
    </div>
    <div class="lc-info">
      <div class="lc-name">Navbar</div>
      <div class="lc-css">justify-content: space-between;<br>align-items: center;</div>
    </div>
  </div>

  <div class="layout-card">
    <div class="lc-preview">
      <div style="display:flex; gap:6px; flex-wrap:wrap; padding:4px;">
        <div class="mi" style="width:52px; height:36px; font-size:10px;">card</div>
        <div class="mi b" style="width:52px; height:36px; font-size:10px;">card</div>
        <div class="mi c" style="width:52px; height:36px; font-size:10px;">card</div>
        <div class="mi" style="width:52px; height:36px; font-size:10px;">card</div>
      </div>
    </div>
    <div class="lc-info">
      <div class="lc-name">Card Grid</div>
      <div class="lc-css">flex-wrap: wrap;<br>gap: 16px;</div>
    </div>
  </div>

  <div class="layout-card">
    <div class="lc-preview">
      <div style="display:flex; flex-direction:column; gap:5px; padding:4px 8px;">
        <div class="mi" style="width:100%; height:20px; font-size:10px;">header</div>
        <div style="display:flex; gap:5px; flex:1;">
          <div class="mi b" style="width:30%; height:36px; font-size:9px;">side</div>
          <div class="mi c" style="flex:1; height:36px; font-size:9px;">main</div>
        </div>
      </div>
    </div>
    <div class="lc-info">
      <div class="lc-name">Sidebar Layout</div>
      <div class="lc-css">flex-direction: column;<br>flex: 1 on main content</div>
    </div>
  </div>

  <div class="layout-card">
    <div class="lc-preview">
      <div style="display:flex; align-items:center; gap:8px; padding:8px;">
        <div class="mi" style="width:36px; height:36px; border-radius:50%; font-size:10px;">av</div>
        <div style="display:flex; flex-direction:column; gap:4px;">
          <div class="mi" style="width:64px; height:12px; border-radius:3px; font-size:0px;"></div>
          <div class="mi b" style="width:44px; height:10px; border-radius:3px; font-size:0px;"></div>
        </div>
      </div>
    </div>
    <div class="lc-info">
      <div class="lc-name">Media Object</div>
      <div class="lc-css">align-items: center;<br>gap: 12px;</div>
    </div>
  </div>

  <div class="layout-card">
    <div class="lc-preview">
      <div style="display:flex; flex-direction:column; justify-content:space-between; height:62px; padding:6px 8px;">
        <div class="mi" style="width:100%; height:18px; font-size:9px;">content</div>
        <div class="mi b" style="width:100%; height:18px; font-size:9px; margin-top:auto;">sticky footer</div>
      </div>
    </div>
    <div class="lc-info">
      <div class="lc-name">Sticky Footer</div>
      <div class="lc-css">flex-direction: column;<br>margin-top: auto on footer</div>
    </div>
  </div>

</div>

---

## Flexbox Quick Reference

<table class="cheat-table">
  <tr>
    <th>Property</th>
    <th>Goes on</th>
    <th>Key values</th>
    <th>What it does</th>
  </tr>
  <tr>
    <td class="mono">display</td>
    <td>Container</td>
    <td class="val">flex</td>
    <td>Activates flexbox — always first</td>
  </tr>
  <tr>
    <td class="mono">flex-direction</td>
    <td>Container</td>
    <td class="val">row · column</td>
    <td>Sets the main axis direction</td>
  </tr>
  <tr>
    <td class="mono">justify-content</td>
    <td>Container</td>
    <td class="val">center · space-between</td>
    <td>Alignment along the main axis</td>
  </tr>
  <tr>
    <td class="mono">align-items</td>
    <td>Container</td>
    <td class="val">center · stretch</td>
    <td>Alignment along the cross axis</td>
  </tr>
  <tr>
    <td class="mono">flex-wrap</td>
    <td>Container</td>
    <td class="val">wrap · nowrap</td>
    <td>Whether items wrap to the next line</td>
  </tr>
  <tr>
    <td class="mono">gap</td>
    <td>Container</td>
    <td class="val">16px · 8px 24px</td>
    <td>Space between items — no margins needed</td>
  </tr>
  <tr>
    <td class="mono">flex-grow</td>
    <td>Item</td>
    <td class="val">0 · 1</td>
    <td>Whether item expands to fill space</td>
  </tr>
  <tr>
    <td class="mono">flex-shrink</td>
    <td>Item</td>
    <td class="val">0 · 1</td>
    <td>Whether item shrinks when space is tight</td>
  </tr>
  <tr>
    <td class="mono">align-self</td>
    <td>Item</td>
    <td class="val">center · flex-end</td>
    <td>Override align-items for one item</td>
  </tr>
  <tr>
    <td class="mono">order</td>
    <td>Item</td>
    <td class="val">0 · -1 · 2</td>
    <td>Reorder visually without changing HTML</td>
  </tr>
</table>

---

<!-- _class: final -->

# Layouts are easy now.
# You just needed the right tool.

&nbsp;

`display: flex` — two words that replace a decade of hacks.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*