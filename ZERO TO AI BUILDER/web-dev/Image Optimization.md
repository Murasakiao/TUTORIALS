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
  .cb-num   { color: #fb923c; }
  .cb-kw    { color: #c084fc; }
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

  /* ── Speed impact bar ── */
  .impact-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 16px;
  }

  .impact-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 18px;
  }

  .impact-card .ic-label {
    font-size: 13px;
    color: var(--muted);
    margin-bottom: 8px;
    display: flex;
    justify-content: space-between;
    align-items: baseline;
  }

  .impact-card .ic-label strong {
    font-size: 14px;
    color: var(--text);
  }

  .impact-card .ic-bar-wrap {
    background: var(--border);
    border-radius: 999px;
    height: 10px;
    overflow: hidden;
    margin-bottom: 6px;
  }

  .impact-card .ic-bar {
    height: 100%;
    border-radius: 999px;
  }

  .impact-card .ic-note {
    font-size: 12px;
    color: var(--muted);
  }

  /* ── Format comparison table ── */
  .format-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13.5px;
    margin: 14px 0;
  }

  .format-table th {
    background: var(--text);
    color: white;
    padding: 9px 14px;
    text-align: left;
    font-weight: 500;
    font-size: 12px;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.05em;
  }

  .format-table td {
    padding: 10px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
    vertical-align: top;
  }

  .format-table tr:last-child td { border-bottom: none; }
  .format-table tr:nth-child(even) td { background: var(--off-white); }

  .format-table .fmt-pill {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    padding: 3px 10px;
    border-radius: 5px;
    display: inline-block;
  }

  .fmt-jpg  { background: #fef3c7; color: #92400e; }
  .fmt-png  { background: #ede9fe; color: #5b21b6; }
  .fmt-webp { background: #d1fae5; color: #065f46; }
  .fmt-svg  { background: #eff6ff; color: #1e40af; }

  .format-table .good { color: #059669; font-weight: 600; }
  .format-table .bad  { color: #dc2626; }
  .format-table .ok   { color: #d97706; }

  /* ── Tool cards ── */
  .tool-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 14px;
  }

  .tool-item {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 18px;
    display: flex;
    align-items: flex-start;
    gap: 14px;
  }

  .tool-item .t-icon { font-size: 26px; flex-shrink: 0; }

  .tool-item .t-name {
    font-weight: 600;
    font-size: 14.5px;
    color: var(--text);
  }

  .tool-item .t-url {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--blue);
    margin-top: 2px;
  }

  .tool-item .t-desc {
    font-size: 12.5px;
    color: var(--muted);
    margin-top: 4px;
    line-height: 1.45;
  }

  /* ── Size recommendation grid ── */
  .size-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .size-card {
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
  }

  .size-card .sc-header {
    padding: 10px 14px;
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
    border-bottom: 1px solid var(--border);
    background: var(--off-white);
  }

  .size-card .sc-body {
    padding: 12px 14px;
    background: var(--white);
  }

  .size-card .sc-row {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    padding: 4px 0;
    border-bottom: 1px solid var(--border);
    font-size: 13px;
  }

  .size-card .sc-row:last-child { border-bottom: none; }

  .size-card .sc-row .sc-type {
    color: var(--muted);
    font-size: 12.5px;
  }

  .size-card .sc-row .sc-val {
    font-family: 'DM Mono', monospace;
    font-size: 12.5px;
    color: var(--blue);
    font-weight: 500;
  }

  /* ── Bulk compress steps ── */
  .bulk-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .bulk-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 13px 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }

  .bulk-card .bk-num {
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

  .bulk-card .bk-title {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
    margin-bottom: 3px;
  }

  .bulk-card .bk-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.5;
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

# Optimize Images
## for the Web

&nbsp;

**Images are the #1 cause of slow websites.** Here's the fix.

`WebP` · `compression` · `lazy loading` · `Squoosh` · `srcset`

---

## Why Image Size Kills Load Speed

Images are typically **60–80% of a webpage's total download size**. Nothing else comes close.

<div class="impact-grid">
  <div class="impact-card">
    <div class="ic-label"><strong>Unoptimized hero image</strong> <span>~4.2 MB</span></div>
    <div class="ic-bar-wrap"><div class="ic-bar" style="width:100%; background:#ef4444;"></div></div>
    <div class="ic-note">Shot on iPhone, dropped straight into the site. Causes 8–12s load on mobile.</div>
  </div>
  <div class="impact-card">
    <div class="ic-label"><strong>Optimized hero image</strong> <span>~120 KB</span></div>
    <div class="ic-bar-wrap"><div class="ic-bar" style="width:3%; background:#22c55e;"></div></div>
    <div class="ic-note">Same image, resized + compressed. 35× smaller. Under 0.3s on mobile.</div>
  </div>
  <div class="impact-card">
    <div class="ic-label"><strong>Google's threshold</strong> <span>< 2.5s LCP</span></div>
    <div class="ic-bar-wrap"><div class="ic-bar" style="width:60%; background:#f59e0b;"></div></div>
    <div class="ic-note">Largest Contentful Paint. Usually the hero image. Affects SEO ranking directly.</div>
  </div>
  <div class="impact-card">
    <div class="ic-label"><strong>Mobile bandwidth</strong> <span>avg. 10 Mbps</span></div>
    <div class="ic-bar-wrap"><div class="ic-bar" style="width:25%; background:#3b82f6;"></div></div>
    <div class="ic-note">A 4 MB image takes ~3s on a good connection. 10s+ on a weak signal.</div>
  </div>
</div>

<div class="highlight" style="margin-top: 14px;">

**The rule:** Every image on your site should be under **200 KB**. Hero images under 150 KB. Thumbnails under 30 KB.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## JPG vs PNG vs WebP

Picking the right format before compressing is the biggest lever you have.

<table class="format-table">
  <tr>
    <th>Format</th>
    <th>Best for</th>
    <th>Transparency</th>
    <th>Typical size</th>
    <th>Browser support</th>
  </tr>
  <tr>
    <td><span class="fmt-pill fmt-jpg">JPG</span></td>
    <td>Photos, hero images, backgrounds</td>
    <td class="bad">✗ None</td>
    <td class="ok">Medium</td>
    <td class="good">Universal</td>
  </tr>
  <tr>
    <td><span class="fmt-pill fmt-png">PNG</span></td>
    <td>Logos, icons, screenshots with text</td>
    <td class="good">✓ Yes</td>
    <td class="bad">Large</td>
    <td class="good">Universal</td>
  </tr>
  <tr>
    <td><span class="fmt-pill fmt-webp">WebP</span></td>
    <td>Everything — photos and transparent images</td>
    <td class="good">✓ Yes</td>
    <td class="good">Smallest</td>
    <td class="good">95%+ browsers</td>
  </tr>
  <tr>
    <td><span class="fmt-pill fmt-svg">SVG</span></td>
    <td>Logos, icons, illustrations</td>
    <td class="good">✓ Yes</td>
    <td class="good">Tiny</td>
    <td class="good">Universal</td>
  </tr>
</table>

<div class="highlight" style="margin-top: 14px;">

**Default choice:** Use **WebP** for everything except vector graphics (use SVG for those). WebP is 25–35% smaller than JPG at the same visual quality and supports transparency — there's almost no reason to use PNG anymore.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Free Tools to Compress Images

<div class="tool-row">
  <div class="tool-item">
    <div class="t-icon">🗜️</div>
    <div>
      <div class="t-name">Squoosh</div>
      <div class="t-url">squoosh.app</div>
      <div class="t-desc">Google's browser-based tool. Drag in an image, choose format, drag the quality slider, compare before/after side by side. The best single-image tool available — nothing to install.</div>
    </div>
  </div>
  <div class="tool-item">
    <div class="t-icon">📌</div>
    <div>
      <div class="t-name">TinyPNG / TinyJPG</div>
      <div class="t-url">tinypng.com</div>
      <div class="t-desc">Drop up to 20 images at once. Automatically compresses and lets you download individually or as a ZIP. Dead simple. Free tier handles most small projects.</div>
    </div>
  </div>
  <div class="tool-item">
    <div class="t-icon">⚡</div>
    <div>
      <div class="t-name">Sharp (Node.js)</div>
      <div class="t-url">sharp.pixelplumbing.com</div>
      <div class="t-desc">Code-based image processing library. Convert, resize, compress, and output WebP in a build script. The right tool once you're automating a pipeline.</div>
    </div>
  </div>
  <div class="tool-item">
    <div class="t-icon">🖼️</div>
    <div>
      <div class="t-name">ImageOptim</div>
      <div class="t-url">imageoptim.com/mac</div>
      <div class="t-desc">Mac desktop app. Drag a folder of images onto it. Losslessly compresses every file in place, without quality loss. Fastest workflow for batch processing on a Mac.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Recommended Max Sizes

These are targets — not rules. Always judge quality with your eyes, not just the number.

<div class="size-grid">
  <div class="size-card">
    <div class="sc-header">🖼️ &nbsp;Hero / Banner</div>
    <div class="sc-body">
      <div class="sc-row"><span class="sc-type">Max file size</span><span class="sc-val">150 KB</span></div>
      <div class="sc-row"><span class="sc-type">Max dimensions</span><span class="sc-val">1920 × 1080px</span></div>
      <div class="sc-row"><span class="sc-type">Format</span><span class="sc-val">WebP / JPG</span></div>
      <div class="sc-row"><span class="sc-type">Quality</span><span class="sc-val">75–85%</span></div>
    </div>
  </div>
  <div class="size-card">
    <div class="sc-header">🃏 &nbsp;Card / Thumbnail</div>
    <div class="sc-body">
      <div class="sc-row"><span class="sc-type">Max file size</span><span class="sc-val">30 KB</span></div>
      <div class="sc-row"><span class="sc-type">Max dimensions</span><span class="sc-val">600 × 400px</span></div>
      <div class="sc-row"><span class="sc-type">Format</span><span class="sc-val">WebP / JPG</span></div>
      <div class="sc-row"><span class="sc-type">Quality</span><span class="sc-val">70–80%</span></div>
    </div>
  </div>
  <div class="size-card">
    <div class="sc-header">🔷 &nbsp;Logo / Icon</div>
    <div class="sc-body">
      <div class="sc-row"><span class="sc-type">Max file size</span><span class="sc-val">10 KB</span></div>
      <div class="sc-row"><span class="sc-type">Max dimensions</span><span class="sc-val">scales to fit</span></div>
      <div class="sc-row"><span class="sc-type">Format</span><span class="sc-val">SVG preferred</span></div>
      <div class="sc-row"><span class="sc-type">Quality</span><span class="sc-val">lossless</span></div>
    </div>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**Resize before compressing.** A 4000px wide photo at 80% quality is still huge. Resize to the actual display width first — a card image never needs to be wider than 600px regardless of quality settings.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## How to Bulk Compress

<div class="bulk-grid">
  <div class="bulk-card">
    <div class="bk-num">1</div>
    <div>
      <div class="bk-title">Mac — ImageOptim</div>
      <div class="bk-desc">Open ImageOptim. Drag your entire <code>images/</code> folder onto the window. It compresses every file in place and shows the savings per file. Done.</div>
    </div>
  </div>
  <div class="bulk-card">
    <div class="bk-num">2</div>
    <div>
      <div class="bk-title">Windows — Caesium</div>
      <div class="bk-desc">Free desktop app at <strong>saerasoft.com/caesium</strong>. Add a folder, set quality, choose output folder, compress. Handles JPG and PNG in batches with a clean UI.</div>
    </div>
  </div>
  <div class="bulk-card">
    <div class="bk-num">3</div>
    <div>
      <div class="bk-title">Online — Squoosh CLI</div>
      <div class="bk-desc">Run <code>npx @squoosh/cli --webp auto *.jpg</code> in your images folder. Converts every JPG to WebP with optimal settings. No install needed beyond Node.</div>
    </div>
  </div>
  <div class="bulk-card">
    <div class="bk-num">4</div>
    <div>
      <div class="bk-title">Build pipeline — Sharp</div>
      <div class="bk-desc">Add Sharp to your npm build script. Runs automatically on every build, converting and resizing images to exact output specs. Best for production projects.</div>
    </div>
  </div>
</div>

<div class="code-block" style="margin-top:14px;">
  <div class="cb-bar">terminal — Squoosh CLI one-liner</div>
  <div class="cb-body" style="padding:10px 20px; line-height:1.9;">
    <span class="cb-prompt">~</span> <span class="cb-cmd">npx @squoosh/cli --webp auto --resize '{"width":1200}' *.jpg</span><br>
    <span class="cb-out">Squoosh results: hero.jpg → hero.webp  4.1 MB → 118 KB  (97% reduction)</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">BONUS</div>

## Lazy Loading in One Line

Images below the fold load **only when the user scrolls near them** — built into HTML since 2019.

<div class="code-block">
  <div class="cb-bar">index.html — the only change needed</div>
  <div class="cb-body">
    <span class="cb-cmt">&lt;!-- Without lazy loading — all images download on page load --&gt;</span><br>
    <span class="cb-tag">&lt;img</span> <span class="cb-attr">src</span><span class="cb-punct">=</span><span class="cb-str">"photo.webp"</span> <span class="cb-attr">alt</span><span class="cb-punct">=</span><span class="cb-str">"..."</span><span class="cb-tag">&gt;</span><br>
    <br>
    <span class="cb-cmt">&lt;!-- With lazy loading — downloads only when near the viewport --&gt;</span><br>
    <span class="cb-tag">&lt;img</span> <span class="cb-attr">src</span><span class="cb-punct">=</span><span class="cb-str">"photo.webp"</span> <span class="cb-attr">alt</span><span class="cb-punct">=</span><span class="cb-str">"..."</span> <span class="cb-attr">loading</span><span class="cb-punct">=</span><span class="cb-str">"lazy"</span><span class="cb-tag">&gt;</span>
  </div>
</div>

<div class="two-col">
  <div class="col-card">
    <div class="label">When to use it</div>
    <p style="font-size:13.5px; margin-top:8px;">Add <code>loading="lazy"</code> to every image that isn't visible on the initial screen load — product images, article thumbnails, anything below the fold.</p>
  </div>
  <div class="col-card">
    <div class="label">When NOT to use it</div>
    <p style="font-size:13.5px; margin-top:8px;">Never add it to your hero image or logo. Those are above the fold and need to load immediately. Lazy loading them <em>hurts</em> your LCP score.</p>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**Browser support:** 96%+. No JavaScript, no library, no build step. One attribute on every non-hero image. It's the highest effort-to-impact ratio in web performance.

</div>

---

## Image Optimization Cheatsheet

<table class="cheat-table">
  <tr>
    <th>Situation</th>
    <th>What to do</th>
  </tr>
  <tr>
    <td>Photo or hero image</td>
    <td>Convert to WebP, resize to max 1920px wide, compress to 75–85% quality, target under 150 KB</td>
  </tr>
  <tr>
    <td>Logo or icon</td>
    <td>Use SVG if possible — scales to any size, tiny file, perfectly sharp on all screens</td>
  </tr>
  <tr>
    <td>Screenshot with text</td>
    <td>Use PNG or WebP — JPG blurs text edges. WebP at 90%+ quality preserves sharpness</td>
  </tr>
  <tr>
    <td>Need transparency</td>
    <td>Use WebP or PNG — JPG has no alpha channel. WebP is always the smaller option</td>
  </tr>
  <tr>
    <td>One image to optimize</td>
    <td>Use Squoosh — drag in, pick WebP, drag quality slider, download</td>
  </tr>
  <tr>
    <td>Folder of images</td>
    <td>Mac: ImageOptim. Windows: Caesium. CLI: Squoosh CLI or Sharp</td>
  </tr>
  <tr>
    <td>Images below the fold</td>
    <td>Add <code>loading="lazy"</code> — instant win, one attribute, no downsides</td>
  </tr>
  <tr>
    <td>Above-the-fold / hero</td>
    <td>Never lazy load. Preload instead: <code>&lt;link rel="preload" as="image"&gt;</code></td>
  </tr>
  <tr>
    <td>Still too slow after compression</td>
    <td>Check actual display size in DevTools. You may be serving 1200px images in a 400px slot</td>
  </tr>
</table>

---

<!-- _class: final -->

# Smaller images.
# Faster sites.
# Happier visitors.

&nbsp;

Convert to WebP. Resize to display size. Add lazy loading. Done.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*