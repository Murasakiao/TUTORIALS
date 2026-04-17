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
  .cb-str   { color: #fde68a; }
  .cb-prop  { color: #93c5fd; }
  .cb-val   { color: #34d399; }
  .cb-sel   { color: #f9fafb; }
  .cb-cmt   { color: #4b5563; font-style: italic; }
  .cb-punct { color: #6b7280; }
  .cb-prompt { color: #22c55e; }
  .cb-cmd    { color: #f9fafb; }
  .cb-out    { color: #9ca3af; }

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

  /* ── Browser tab mock ── */
  .browser-mock {
    background: #f1f5f9;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 16px 0;
  }

  .browser-mock .bm-bar {
    background: #e2e8f0;
    padding: 10px 14px;
    display: flex;
    align-items: center;
    gap: 6px;
    border-bottom: 1px solid var(--border);
  }

  .browser-mock .bm-dots {
    display: flex;
    gap: 5px;
    margin-right: 8px;
  }

  .browser-mock .bm-dot {
    width: 11px;
    height: 11px;
    border-radius: 50%;
  }

  .browser-mock .bm-dot.r { background: #ef4444; }
  .browser-mock .bm-dot.y { background: #f59e0b; }
  .browser-mock .bm-dot.g { background: #22c55e; }

  .browser-mock .bm-tabs {
    display: flex;
    gap: 3px;
    flex: 1;
  }

  .browser-mock .bm-tab {
    background: var(--white);
    border-radius: 6px 6px 0 0;
    padding: 5px 12px;
    font-size: 12px;
    color: var(--text);
    display: flex;
    align-items: center;
    gap: 6px;
    font-family: 'DM Sans', sans-serif;
    border: 1px solid var(--border);
    border-bottom: none;
    max-width: 160px;
  }

  .browser-mock .bm-tab.inactive {
    background: #e2e8f0;
    color: var(--muted);
  }

  .browser-mock .bm-tab .bm-fav {
    width: 14px;
    height: 14px;
    border-radius: 3px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 10px;
    flex-shrink: 0;
  }

  .browser-mock .bm-tab .bm-fav.blank {
    background: #cbd5e1;
  }

  .browser-mock .bm-tab .bm-fav.has {
    background: #2563eb;
    color: white;
  }

  .browser-mock .bm-url {
    background: var(--white);
    border-radius: 6px;
    padding: 5px 12px;
    font-family: 'DM Mono', monospace;
    font-size: 11.5px;
    color: var(--muted);
    width: 260px;
    border: 1px solid var(--border);
  }

  .browser-mock .bm-body {
    padding: 20px 24px;
    background: var(--white);
    min-height: 60px;
    display: flex;
    align-items: center;
    gap: 16px;
  }

  /* ── Credibility comparison ── */
  .cred-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 16px;
  }

  .cred-card {
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .cred-card .cc-label {
    padding: 7px 14px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.07em;
    text-transform: uppercase;
  }

  .cred-card.bad  .cc-label { background: #fef2f2; color: #991b1b; border-bottom: 1px solid #fecaca; }
  .cred-card.good .cc-label { background: #f0fdf4; color: #166534; border-bottom: 1px solid #bbf7d0; }

  .cred-card .cc-body {
    padding: 14px 16px;
    background: var(--white);
    font-size: 13px;
    color: var(--muted);
    line-height: 1.6;
  }

  .cred-card .cc-body strong { color: var(--text); font-weight: 600; }

  /* ── Step cards (favicon.io walkthrough) ── */
  .step-cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .step-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 13px 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }

  .step-card .sk-num {
    background: var(--blue);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    min-width: 26px;
    height: 26px;
    border-radius: 999px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-top: 1px;
  }

  .step-card .sk-title {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
    margin-bottom: 3px;
  }

  .step-card .sk-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.5;
  }

  /* ── Icon size table ── */
  .size-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13.5px;
    margin: 14px 0;
  }

  .size-table th {
    background: var(--text);
    color: white;
    padding: 9px 14px;
    text-align: left;
    font-weight: 500;
    font-size: 12px;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.05em;
  }

  .size-table td {
    padding: 9px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
    vertical-align: middle;
  }

  .size-table tr:last-child td { border-bottom: none; }
  .size-table tr:nth-child(even) td { background: var(--off-white); }

  .size-table .mono {
    font-family: 'DM Mono', monospace;
    color: var(--blue);
    font-size: 12.5px;
  }

  .size-table .tag {
    display: inline-block;
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    padding: 2px 8px;
    border-radius: 4px;
    border: 1px solid var(--border);
    background: var(--off-white);
    color: var(--muted);
  }

  .size-table .req {
    display: inline-block;
    font-size: 11px;
    font-weight: 600;
    padding: 2px 8px;
    border-radius: 4px;
  }

  .req.must { background: #fee2e2; color: #991b1b; }
  .req.good { background: #d1fae5; color: #065f46; }
  .req.nice { background: #fef3c7; color: #92400e; }

  /* ── Folder tree ── */
  .folder-tree {
    background: #111827;
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .folder-tree .ft-bar {
    background: #1f2937;
    padding: 8px 16px;
    font-size: 11.5px;
    color: #6b7280;
    letter-spacing: 0.04em;
  }

  .folder-tree .ft-body {
    padding: 14px 22px;
    line-height: 2.1;
  }

  .ft-dir   { color: #60a5fa; }
  .ft-file  { color: #f9fafb; }
  .ft-fav   { color: #34d399; }
  .ft-line  { color: #374151; }
  .ft-cmt   { color: #4b5563; font-style: italic; }

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
    padding: 9px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
  }

  .cheat-table tr:last-child td { border-bottom: none; }
  .cheat-table tr:nth-child(even) td { background: var(--off-white); }

  .cheat-table .mono {
    font-family: 'DM Mono', monospace;
    color: var(--blue);
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

# What Is a Favicon
## and How to Add One

&nbsp;

**The tiny icon that makes your site feel real.** Takes 5 minutes.

`favicon.ico` · `apple-touch-icon` · `manifest` · `16px` · `512px`

---

## What a Favicon Is

A favicon is the small icon that appears in the browser tab, bookmarks bar, and search results next to your site's name.

<div class="browser-mock">
  <div class="bm-bar">
    <div class="bm-dots">
      <div class="bm-dot r"></div>
      <div class="bm-dot y"></div>
      <div class="bm-dot g"></div>
    </div>
    <div class="bm-tabs">
      <div class="bm-tab">
        <div class="bm-fav has">◆</div>
        My Portfolio
      </div>
      <div class="bm-tab inactive">
        <div class="bm-fav blank"></div>
        Untitled
      </div>
      <div class="bm-tab inactive">
        <div class="bm-fav blank"></div>
        New Tab
      </div>
    </div>
    <div class="bm-url">myportfolio.com</div>
  </div>
  <div class="bm-body">
    <p style="font-size:14px; color:var(--muted); margin:0;">The blue ◆ on the first tab — that's the favicon. The grey squares on the other tabs are sites with no favicon set.</p>
  </div>
</div>

<div class="tools" style="margin-top:4px;">
  <div class="tool-card">
    <div class="icon">📌</div>
    <div class="name">Browser tabs</div>
    <div class="desc">Shown at 16×16px next to the page title. How visitors identify your tab when 10+ tabs are open.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔖</div>
    <div class="name">Bookmarks</div>
    <div class="desc">Displayed beside bookmarked pages. Without one, bookmarks show a blank grey square.</div>
  </div>
  <div class="tool-card">
    <div class="icon">📱</div>
    <div class="name">Home screen</div>
    <div class="desc">"Add to Home Screen" on iOS and Android uses your icon. Without it you get a screenshot thumbnail.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔍</div>
    <div class="name">Search results</div>
    <div class="desc">Google shows the favicon beside your URL in search results. A missing icon signals an unfinished site.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Why It Matters for Credibility

The favicon is the smallest detail with the biggest credibility signal.

<div class="cred-grid">
  <div class="cred-card bad">
    <div class="cc-label">❌ &nbsp;No favicon</div>
    <div class="cc-body">The browser shows a <strong>blank grey square</strong> in the tab. Visitors subconsciously read this as "unfinished" or "not a real business" — even if the rest of the site looks great. It's the digital equivalent of a shop sign with no name on it.</div>
  </div>
  <div class="cred-card good">
    <div class="cc-label">✅ &nbsp;Favicon present</div>
    <div class="cc-body">The tab shows your brand mark. Visitors can find your tab quickly when multitasking. Bookmarked versions look intentional. It signals <strong>attention to detail</strong> — the same quality signal as a matching email domain.</div>
  </div>
</div>

&nbsp;

<div class="tools" style="margin-top:4px;">
  <div class="tool-card">
    <div class="icon">⏱️</div>
    <div class="name">Takes 5 minutes</div>
    <div class="desc">One free tool, one HTML line, one file in the right folder. The effort-to-impact ratio is extraordinary.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🎯</div>
    <div class="name">Often overlooked</div>
    <div class="desc">Most tutorials skip it. That's exactly why having one sets your site apart from beginner projects immediately.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Create One Free with favicon.io

favicon.io generates every size you need from a single input — no design software required.

<div class="step-cards">
  <div class="step-card">
    <div class="sk-num">1</div>
    <div>
      <div class="sk-title">Go to favicon.io</div>
      <div class="sk-desc">Three generators available: from text (initials), from an emoji, or from an image. Pick whichever matches what you have.</div>
    </div>
  </div>
  <div class="step-card">
    <div class="sk-num">2</div>
    <div>
      <div class="sk-title">From text — fastest</div>
      <div class="sk-desc">Type your initials or a short letter. Pick a font, background color, and text color. Preview updates in real time. Takes under a minute.</div>
    </div>
  </div>
  <div class="step-card">
    <div class="sk-num">3</div>
    <div>
      <div class="sk-title">From image — most branded</div>
      <div class="sk-desc">Upload your logo PNG. favicon.io crops it to a square and generates all sizes. Your logo should already be square or close to it.</div>
    </div>
  </div>
  <div class="step-card">
    <div class="sk-num">4</div>
    <div>
      <div class="sk-title">Download the package</div>
      <div class="sk-desc">Click Download. You get a ZIP containing <code>favicon.ico</code>, <code>favicon-16x16.png</code>, <code>favicon-32x32.png</code>, <code>apple-touch-icon.png</code>, and a <code>site.webmanifest</code>.</div>
    </div>
  </div>
  <div class="step-card">
    <div class="sk-num">5</div>
    <div>
      <div class="sk-title">Place files in project root</div>
      <div class="sk-desc">Copy all files into the root of your project — the same folder as your <code>index.html</code>. Do not put them in an <code>/images</code> subfolder.</div>
    </div>
  </div>
  <div class="step-card">
    <div class="sk-num">6</div>
    <div>
      <div class="sk-title">Paste the HTML snippet</div>
      <div class="sk-desc">favicon.io gives you the exact <code>&lt;link&gt;</code> tags to copy. Paste them into <code>&lt;head&gt;</code> and you're done.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## The HTML Lines to Add

Paste this inside your `<head>` — favicon.io generates it for you, but here's what each line does.

<div class="code-block">
  <div class="cb-bar">index.html — inside &lt;head&gt;</div>
  <div class="cb-body">
    <span class="cb-cmt">&lt;!-- Standard favicon — browsers + search results --&gt;</span><br>
    <span class="cb-tag">&lt;link</span> <span class="cb-attr">rel</span><span class="cb-punct">=</span><span class="cb-str">"icon"</span> <span class="cb-attr">type</span><span class="cb-punct">=</span><span class="cb-str">"image/x-icon"</span> <span class="cb-attr">href</span><span class="cb-punct">=</span><span class="cb-str">"/favicon.ico"</span><span class="cb-tag">&gt;</span><br>
    <br>
    <span class="cb-cmt">&lt;!-- High-res for modern browsers --&gt;</span><br>
    <span class="cb-tag">&lt;link</span> <span class="cb-attr">rel</span><span class="cb-punct">=</span><span class="cb-str">"icon"</span> <span class="cb-attr">type</span><span class="cb-punct">=</span><span class="cb-str">"image/png"</span> <span class="cb-attr">sizes</span><span class="cb-punct">=</span><span class="cb-str">"32x32"</span> <span class="cb-attr">href</span><span class="cb-punct">=</span><span class="cb-str">"/favicon-32x32.png"</span><span class="cb-tag">&gt;</span><br>
    <span class="cb-tag">&lt;link</span> <span class="cb-attr">rel</span><span class="cb-punct">=</span><span class="cb-str">"icon"</span> <span class="cb-attr">type</span><span class="cb-punct">=</span><span class="cb-str">"image/png"</span> <span class="cb-attr">sizes</span><span class="cb-punct">=</span><span class="cb-str">"16x16"</span> <span class="cb-attr">href</span><span class="cb-punct">=</span><span class="cb-str">"/favicon-16x16.png"</span><span class="cb-tag">&gt;</span><br>
    <br>
    <span class="cb-cmt">&lt;!-- iOS "Add to Home Screen" icon --&gt;</span><br>
    <span class="cb-tag">&lt;link</span> <span class="cb-attr">rel</span><span class="cb-punct">=</span><span class="cb-str">"apple-touch-icon"</span> <span class="cb-attr">sizes</span><span class="cb-punct">=</span><span class="cb-str">"180x180"</span> <span class="cb-attr">href</span><span class="cb-punct">=</span><span class="cb-str">"/apple-touch-icon.png"</span><span class="cb-tag">&gt;</span><br>
    <br>
    <span class="cb-cmt">&lt;!-- Android / PWA manifest --&gt;</span><br>
    <span class="cb-tag">&lt;link</span> <span class="cb-attr">rel</span><span class="cb-punct">=</span><span class="cb-str">"manifest"</span> <span class="cb-attr">href</span><span class="cb-punct">=</span><span class="cb-str">"/site.webmanifest"</span><span class="cb-tag">&gt;</span>
  </div>
</div>

<div class="highlight">

**Order matters:** Put these tags after your `<title>` but before any stylesheet `<link>` tags. The browser reads `<head>` top to bottom — favicon declarations early means faster tab icon rendering.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Your File Structure After Setup

<div class="folder-tree">
  <div class="ft-bar">project root — what it should look like</div>
  <div class="ft-body">
    <span class="ft-dir">my-website/</span><br>
    <span class="ft-line">├── </span><span class="ft-file">index.html</span><br>
    <span class="ft-line">├── </span><span class="ft-file">style.css</span><br>
    <span class="ft-line">├── </span><span class="ft-fav">favicon.ico</span>          <span class="ft-cmt"># required — legacy browsers</span><br>
    <span class="ft-line">├── </span><span class="ft-fav">favicon-16x16.png</span>   <span class="ft-cmt"># browser tabs</span><br>
    <span class="ft-line">├── </span><span class="ft-fav">favicon-32x32.png</span>   <span class="ft-cmt"># high-dpi tabs, taskbar</span><br>
    <span class="ft-line">├── </span><span class="ft-fav">apple-touch-icon.png</span> <span class="ft-cmt"># iOS home screen</span><br>
    <span class="ft-line">├── </span><span class="ft-fav">site.webmanifest</span>    <span class="ft-cmt"># Android + PWA icons</span><br>
    <span class="ft-line">└── </span><span class="ft-dir">images/</span>
  </div>
</div>

<div class="highlight">

**Root placement is required.** Browsers automatically request <code>/favicon.ico</code> from the root of any domain — even before reading your HTML. If the file isn't there, every page load logs a silent 404. Always place favicon files at the project root, not inside a subfolder.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 04</div>

## Test It Locally

Favicons are cached aggressively. Follow these steps if yours isn't showing up.

<div class="two-col">
  <div class="col-card">
    <div class="label">Normal test</div>
    <ul class="step-list" style="margin-top:8px;">
      <li style="font-size:13.5px;">Open your site in the browser with a local server — not by double-clicking the file. Use VS Code's Live Server extension or run <code>npx serve .</code></li>
      <li style="font-size:13.5px;">Look at the browser tab. The favicon should appear within a second or two of the page loading.</li>
    </ul>
  </div>
  <div class="col-card">
    <div class="label">If it's not showing</div>
    <ul class="step-list" style="margin-top:8px;">
      <li style="font-size:13.5px;">Hard refresh: <code>⌘ Shift R</code> (Mac) or <code>Ctrl Shift R</code> (Windows). Clears the favicon cache for that tab.</li>
      <li style="font-size:13.5px;">Open DevTools → Network tab → reload → search for <code>favicon</code>. Confirm the file returns a 200, not a 404.</li>
    </ul>
  </div>
</div>

<div class="code-block" style="margin-top:14px;">
  <div class="cb-bar">terminal — serve your project locally</div>
  <div class="cb-body" style="padding:10px 20px; line-height:1.9;">
    <span class="cb-prompt">~</span> <span class="cb-cmd">npx serve .</span><br>
    <span class="cb-out">Serving!  →  Local: http://localhost:3000</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Multi-Device Icon Sizes Explained

Different contexts pull different sizes. favicon.io generates all of them automatically.

<table class="size-table">
  <tr>
    <th>File</th>
    <th>Size</th>
    <th>Where it's used</th>
    <th>Priority</th>
  </tr>
  <tr>
    <td class="mono">favicon.ico</td>
    <td class="mono">16 + 32px</td>
    <td>All browsers — fallback if PNGs are missing. Legacy IE support.</td>
    <td><span class="req must">Must have</span></td>
  </tr>
  <tr>
    <td class="mono">favicon-16x16.png</td>
    <td class="mono">16 × 16px</td>
    <td>Standard browser tab on most desktop displays</td>
    <td><span class="req must">Must have</span></td>
  </tr>
  <tr>
    <td class="mono">favicon-32x32.png</td>
    <td class="mono">32 × 32px</td>
    <td>High-DPI tabs, Windows taskbar pinned sites, Safari reading list</td>
    <td><span class="req must">Must have</span></td>
  </tr>
  <tr>
    <td class="mono">apple-touch-icon.png</td>
    <td class="mono">180 × 180px</td>
    <td>iOS "Add to Home Screen." Also used by some Android browsers.</td>
    <td><span class="req good">Recommended</span></td>
  </tr>
  <tr>
    <td class="mono">icon-192x192.png</td>
    <td class="mono">192 × 192px</td>
    <td>Android Chrome home screen shortcut</td>
    <td><span class="req good">Recommended</span></td>
  </tr>
  <tr>
    <td class="mono">icon-512x512.png</td>
    <td class="mono">512 × 512px</td>
    <td>Android splash screen, PWA install prompt, Google Search</td>
    <td><span class="req nice">Nice to have</span></td>
  </tr>
  <tr>
    <td class="mono">site.webmanifest</td>
    <td>—</td>
    <td>Declares 192 and 512px icons for Android + PWA. JSON file.</td>
    <td><span class="req good">Recommended</span></td>
  </tr>
</table>

---

## Favicon Quick Reference

<table class="cheat-table">
  <tr>
    <th>Task</th>
    <th>How to do it</th>
  </tr>
  <tr>
    <td>Generate all sizes at once</td>
    <td>Go to favicon.io → pick text, emoji, or image → download ZIP</td>
  </tr>
  <tr>
    <td>Where to place the files</td>
    <td>Project root — same folder as <code>index.html</code>. Not inside <code>/images</code></td>
  </tr>
  <tr>
    <td>Minimum HTML needed</td>
    <td><code>&lt;link rel="icon" href="/favicon.ico"&gt;</code> — one line works in all modern browsers</td>
  </tr>
  <tr>
    <td>Full cross-device support</td>
    <td>Add all four <code>&lt;link&gt;</code> tags: .ico, 32px PNG, 16px PNG, apple-touch-icon</td>
  </tr>
  <tr>
    <td>Favicon not showing locally</td>
    <td>Use a local server (Live Server / <code>npx serve .</code>), then hard-refresh with <code>⌘ Shift R</code></td>
  </tr>
  <tr>
    <td>Favicon not showing after deploy</td>
    <td>Check DevTools → Network → favicon returns 200, not 404. Confirm root placement.</td>
  </tr>
  <tr>
    <td>iOS home screen icon</td>
    <td>Requires <code>apple-touch-icon.png</code> at 180×180px linked with <code>rel="apple-touch-icon"</code></td>
  </tr>
  <tr>
    <td>Android home screen icon</td>
    <td>Requires <code>site.webmanifest</code> linked in <code>&lt;head&gt;</code> with 192 and 512px icons declared inside it</td>
  </tr>
  <tr>
    <td>Updating an existing favicon</td>
    <td>Rename the new file or append <code>?v=2</code> to the href to bust the browser cache</td>
  </tr>
</table>

---

<!-- _class: final -->

# Five minutes.
# One file. One line.
# Your site looks real.

&nbsp;

Generate on favicon.io. Drop in root. Paste the tags. Done.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*