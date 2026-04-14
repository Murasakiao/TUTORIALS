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

  p {
    color: var(--text);
    margin: 0.4em 0;
  }

  ul {
    padding-left: 1.4em;
  }

  li {
    margin-bottom: 10px;
    color: var(--text);
  }

  strong {
    color: var(--blue);
    font-weight: 600;
  }

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

  blockquote p {
    color: #1e40af;
    margin: 0;
  }

  /* Cover slide */
  section.cover {
    background: var(--text);
    color: var(--white);
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  section.cover h1 {
    color: var(--white);
    font-size: 46px;
  }

  section.cover h2 { 
    color: #93c5fd; 
    border-bottom-color: #374151; 
  }

  section.cover p {
    color: #9ca3af;
  }

  section.cover strong {
    color: #60a5fa;
  }

  section.cover code {
    background: #1e3a5f;
    color: #93c5fd;
  }

  /* Step slides */
  section.step {
    background: var(--off-white);
  }

  /* Highlight box */
  .highlight {
    background: var(--blue-light);
    border: 1px solid var(--blue-mid);
    border-radius: 10px;
    padding: 18px 24px;
    margin: 16px 0;
  }

  /* Tool card grid */
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

  .tool-card .icon {
    font-size: 24px;
    margin-bottom: 6px;
  }

  .tool-card .name {
    font-weight: 600;
    font-size: 15px;
    color: var(--text);
  }

  .tool-card .desc {
    font-size: 13px;
    color: var(--muted);
    margin-top: 2px;
  }

  /* Step badge */
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

  /* URL display */
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

  /* Final slide */
  section.final {
    background: var(--blue);
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
  }

  section.final h1 {
    color: white;
    font-size: 40px;
  }

  section.final p {
    color: #bfdbfe;
    font-size: 18px;
  }

  section.final strong { color: white; } 
  section.final em { color: #bfdbfe; }

  /* Code block dark */
  .code-block {
    background: #111827;
    border-radius: 8px;
    padding: 18px 24px;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #e5e7eb;
    line-height: 1.9;
    margin: 12px 0;
  }

  .code-block .tag    { color: #60a5fa; }
  .code-block .attr   { color: #86efac; }
  .code-block .val    { color: #fca5a5; }
  .code-block .prop   { color: #c4b5fd; }
  .code-block .css-val{ color: #fde68a; }
  .code-block .fn     { color: #fbbf24; }
  .code-block .str    { color: #86efac; }
  .code-block .cmt    { color: #4b5563; font-style: italic; }

  /* Three-column layer display */
  .three-col {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 16px;
    margin-top: 16px;
  }

  .layer-card {
    border-radius: 10px;
    padding: 18px 20px;
  }

  .layer-card.html-card {
    background: #eff6ff;
    border: 1px solid #bfdbfe;
  }

  .layer-card.css-card {
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
  }

  .layer-card.js-card {
    background: #fefce8;
    border: 1px solid #fde68a;
  }

  .layer-card .lang {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 500;
    margin-bottom: 6px;
  }

  .layer-card.html-card .lang { color: #2563eb; }
  .layer-card.css-card  .lang { color: #16a34a; }
  .layer-card.js-card   .lang { color: #ca8a04; }

  .layer-card .role {
    font-size: 15px;
    font-weight: 600;
    color: var(--text);
    margin-bottom: 4px;
  }

  .layer-card .detail {
    font-size: 13px;
    color: var(--muted);
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
---

<!-- _class: cover -->

# HTML, CSS, and JavaScript
## How They Actually Relate

&nbsp;

**Three languages. One job.** Here's how they fit together.

`structure` · `style` · `behavior`

---

## The House Analogy

Every website is built from three distinct layers — just like a house.

<div class="three-col">
  <div class="layer-card html-card">
    <div class="lang">HTML</div>
    <div class="role">🏗️ Structure</div>
    <div class="detail">The walls, floors, and rooms. Raw content with no decoration.</div>
  </div>
  <div class="layer-card css-card">
    <div class="lang">CSS</div>
    <div class="role">🎨 Style</div>
    <div class="detail">Paint, furniture, lighting. Controls how everything looks.</div>
  </div>
  <div class="layer-card js-card">
    <div class="lang">JavaScript</div>
    <div class="role">⚡ Behavior</div>
    <div class="detail">Electricity, plumbing, doors that open. Makes things interactive.</div>
  </div>
</div>

&nbsp;

Remove CSS → the house still stands, just ugly.
Remove JS → it still exists, just static.
**Remove HTML → there is no house.**

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## The Same Button, Three Ways

Start with bare HTML — just structure, no style, no behavior:

<div class="code-block">
  <span class="cmt">&lt;!-- HTML only --&gt;</span><br>
  <span class="tag">&lt;button&gt;</span>Subscribe<span class="tag">&lt;/button&gt;</span>
</div>

Add CSS — now it looks intentional:

<div class="code-block">
  <span class="prop">button</span> {<br>
  &nbsp;&nbsp;<span class="prop">background</span>: <span class="css-val">#2563eb</span>;<br>
  &nbsp;&nbsp;<span class="prop">color</span>: <span class="css-val">white</span>;<br>
  &nbsp;&nbsp;<span class="prop">padding</span>: <span class="css-val">10px 24px</span>;<br>
  &nbsp;&nbsp;<span class="prop">border-radius</span>: <span class="css-val">6px</span>;<br>
  }
</div>

Add JavaScript — now it does something:

<div class="code-block">
  <span class="fn">document.querySelector</span>(<span class="str">'button'</span>).<span class="fn">addEventListener</span>(<span class="str">'click'</span>, () =&gt; {<br>
  &nbsp;&nbsp;<span class="fn">alert</span>(<span class="str">'Subscribed!'</span>);<br>
  });
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Where Each File Lives

Each language has its own file — and its own place in your project.

<div class="three-col">
  <div class="layer-card html-card">
    <div class="lang">HTML</div>
    <div class="role">index.html</div>
    <div class="detail">Lives at the root. Links to everything else via <code>&lt;link&gt;</code> and <code>&lt;script&gt;</code> tags.</div>
  </div>
  <div class="layer-card css-card">
    <div class="lang">CSS</div>
    <div class="role">css/style.css</div>
    <div class="detail">Linked in the <code>&lt;head&gt;</code> section. Loaded before the page renders.</div>
  </div>
  <div class="layer-card js-card">
    <div class="lang">JavaScript</div>
    <div class="role">js/main.js</div>
    <div class="detail">Linked just before <code>&lt;/body&gt;</code>. Runs after the HTML is ready.</div>
  </div>
</div>

&nbsp;

> &lt;link rel="stylesheet" href="css/style.css"&gt; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;!-- in &lt;head&gt; --&gt;<br>
> &lt;script src="js/main.js"&gt;&lt;/script&gt; &nbsp;&nbsp;&lt;!-- before &lt;/body&gt; --&gt;

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Why Order of Loading Matters

The browser reads your HTML **top to bottom**. Order is not optional.

- **CSS goes in `<head>`** — styles must load before the page is painted, or you get a flash of unstyled content
- **JS goes before `</body>`** — scripts that target HTML elements need those elements to exist first
- If your JS loads before the HTML it needs → it finds nothing → silent failure

&nbsp;

<div class="highlight">

**The rule of thumb:**

&nbsp;&nbsp;`<head>` → metadata + stylesheets
&nbsp;&nbsp;`<body>` → all your content
&nbsp;&nbsp;just before `</body>` → your scripts

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## One-File Shortcut vs Separation of Concerns

You can write CSS and JS directly inside your HTML file — and for small projects, that's fine.

<div class="two-col">
  <div class="col-card">
    <div class="label">⚡ One-File Shortcut</div>
    <p style="font-size:14px">CSS inside <code>&lt;style&gt;</code> tags.<br>JS inside <code>&lt;script&gt;</code> tags.<br>Everything in one <code>.html</code> file.</p>
    <p style="font-size:13px; color:#6b7280; margin-top:8px">✅ Great for prototypes, quick demos, and sharing single files.</p>
  </div>
  <div class="col-card">
    <div class="label">🏛️ Separation of Concerns</div>
    <p style="font-size:14px">HTML in <code>.html</code><br>CSS in <code>.css</code><br>JS in <code>.js</code></p>
    <p style="font-size:13px; color:#6b7280; margin-top:8px">✅ Right approach for anything you'll maintain, share, or grow.</p>
  </div>
</div>

&nbsp;

**The moment your project has more than one page — separate your files.**

---

## The Mental Model

Think of the browser as an assembly line:

<div class="url-box">
  1. Parse HTML &nbsp;→&nbsp; 2. Apply CSS &nbsp;→&nbsp; 3. Run JavaScript &nbsp;→&nbsp; 4. Show the page
</div>

Each layer depends on the one before it. That's why order matters, and why each has its own role.

<div class="highlight">

**HTML** gives you the elements to style.
**CSS** gives you the visual layer that JavaScript can read and change.
**JavaScript** manipulates both — but only after they exist.

</div>

---

<!-- _class: final -->

# Three Files.
# One Website.

&nbsp;

Once the relationship clicks, everything else in web development makes sense.

&nbsp;

**Check out my other tutorials →**
*More fundamentals you actually need to know*