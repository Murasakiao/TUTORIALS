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

  .url-box {
    background: #111827;
    border-radius: 8px;
    padding: 14px 20px;
    font-family: 'DM Mono', monospace;
    font-size: 15px;
    color: #60a5fa;
    margin: 16px 0;
    display: flex;
    align-items: center;
    gap: 10px;
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

  /* Terminal window mock */
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

  /* Command reference grid */
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
    font-size: 14px;
    color: #60a5fa;
    font-weight: 500;
    min-width: 72px;
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

  /* Cheatsheet table */
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

  /* Two-column layout */
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

# Inspect Any Website
## Using Browser DevTools

&nbsp;

**See how any website is built — live.**

`inspect` · `css` · `fonts` · `colors` · `debug`

---

## What is DevTools?

DevTools is a built-in tool in your browser that lets you inspect and modify any website in real time.

<div class="tools">
  <div class="tool-card">
    <div class="icon">🔍</div>
    <div class="name">Inspect Elements</div>
    <div class="desc">Click anything and see its HTML + CSS instantly.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🎨</div>
    <div class="name">Edit Styles</div>
    <div class="desc">Change colors, fonts, spacing — live on the page.</div>
  </div>
  <div class="tool-card">
    <div class="icon">⚡</div>
    <div class="name">Debug Faster</div>
    <div class="desc">Find layout issues, broken styles, and errors.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🧠</div>
    <div class="name">Learn by Reverse Engineering</div>
    <div class="desc">Study how great websites are built.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Open DevTools

Three easy ways — pick your favorite:

<ul class="step-list">
  <li><strong>Right Click</strong> → Click anywhere → <code>Inspect</code></li>
  <li><strong>Shortcut</strong> → Press <code>⌘ Option I</code> (Mac) / <code>Ctrl Shift I</code> (Windows)</li>
  <li><strong>Menu</strong> → Top-right menu → More Tools → Developer Tools</li>
</ul>

&nbsp;

Once opened, you'll see something like:

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span>
    <span class="dot yellow"></span>
    <span class="dot green"></span>
    <span class="title">DevTools — Elements</span>
  </div>
  <div class="terminal-body">
    <span class="out">&lt;div class="hero"&gt;</span><br>
    <span class="out">  &lt;h1&gt;Hello World&lt;/h1&gt;</span><br>
    <span class="out">&lt;/div&gt;</span>
  </div>
</div>

This is the **live structure** of the website.

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Inspect Any Element

Click the **cursor icon** (top-left of DevTools), then hover over the page.

<div class="highlight">

💡 As you hover, elements get highlighted — click one to inspect it.

</div>

<div class="terminal">
  <div class="terminal-body">
    <span class="cmt"># Click a button</span><br>
    <span class="out">&lt;button class="btn-primary"&gt;</span><br>
    <span class="out">  Get Started</span><br>
    <span class="out">&lt;/button&gt;</span>
  </div>
</div>

Now you can see:
- The **HTML structure**
- The **class names**
- The **styles applied**

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Live Edit CSS

On the right panel, you'll see styles like this:

<div class="terminal">
  <div class="terminal-body">
    <span class="out">.btn-primary {</span><br>
    <span class="out">  background: blue;</span><br>
    <span class="out">  color: white;</span><br>
    <span class="out">}</span>
  </div>
</div>

Try changing values directly:

<div class="highlight">

- Change <code>blue</code> → <code>red</code>  
- Add <code>border-radius: 20px;</code>  
- Disable styles by unchecking them  

</div>

⚡ Changes happen **instantly** — no refresh needed.

---

<!-- _class: step -->

<div class="step-badge">STEP 04</div>

## Copy Styles You Like

Found a cool design? Steal it (legally 😉).

<ul class="step-list">
  <li>Right-click the element in DevTools</li>
  <li>Click <strong>Copy → Copy styles</strong></li>
  <li>Paste into your own project</li>
</ul>

<div class="highlight">

This is how you learn fast:
**observe → copy → modify → understand**

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 05</div>

## Find Fonts & Colors

<div class="two-col">
  <div class="col-card">
    <div class="label">Fonts</div>
    <p>Look for <code>font-family</code> in styles.</p>
    <p class="mono">font-family: 'Inter', sans-serif;</p>
  </div>
  <div class="col-card">
    <div class="label">Colors</div>
    <p>Click color values to open picker.</p>
    <p class="mono">#2563eb</p>
  </div>
</div>

&nbsp;

💡 DevTools even shows:
- Color palettes
- Contrast ratios
- Font rendering

---

<!-- _class: step -->

<div class="step-badge">BONUS</div>

## Network Tab (Speed Secrets)

Switch to the **Network tab** and reload the page.

<div class="terminal">
  <div class="terminal-body">
    <span class="out">index.html     12ms</span><br>
    <span class="out">styles.css     8ms</span><br>
    <span class="out">app.js         15ms</span><br>
    <span class="out">image.png      120ms</span>
  </div>
</div>

You can see:
- What files load
- How long they take
- What’s slowing the site

<div class="highlight">

🔥 This is how developers optimize performance.

</div>

---

## Mini Workflow (Real Use)

<blockquote>
Open DevTools → Inspect a section → Change styles → Copy what works → Rebuild it yourself
</blockquote>

That’s how you go from:
**“I like this design” → “I can build this design”**

---

<!-- _class: final -->

# DevTools is your
# unfair advantage.

&nbsp;

**You see it. You edit it. You learn it.**

&nbsp;

**Next tutorial →**
*Build your first website from scratch*