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

  /* Folder tree */
  .folder-tree {
    background: #111827;
    border-radius: 8px;
    padding: 20px 24px;
    font-family: 'DM Mono', monospace;
    font-size: 14px;
    color: #e5e7eb;
    line-height: 2;
    margin: 16px 0;
  }

  .folder-tree .folder {
    color: #60a5fa;
    font-weight: 500;
  }

  .folder-tree .file {
    color: #86efac;
  }

  .folder-tree .comment {
    color: #6b7280;
    font-size: 12px;
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

# Proper File Structure
## for a Simple Website

&nbsp;

**The one thing** beginners always skip — and later regret

`html` · `css` · `js` · `images` · `paths`

---

## Why Structure Matters

Messy folders break your site. Clean folders keep it maintainable.

<div class="tools">
  <div class="tool-card">
    <div class="icon">🔗</div>
    <div class="name">Broken Links</div>
    <div class="desc">Files in the wrong place = images that won't load</div>
  </div>
  <div class="tool-card">
    <div class="icon">😵</div>
    <div class="name">Confusion at Scale</div>
    <div class="desc">One file now → 20 files later. Structure saves you</div>
  </div>
  <div class="tool-card">
    <div class="icon">🤝</div>
    <div class="name">Collaboration</div>
    <div class="desc">Others (or future you) can navigate without guessing</div>
  </div>
  <div class="tool-card">
    <div class="icon">🚀</div>
    <div class="name">Deployment</div>
    <div class="desc">Hosts like GitHub Pages expect a specific layout</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## The Standard Folder Layout

This is the structure every beginner site should start with:

<div class="folder-tree">
  <span class="folder">my-website/</span><br>
  &nbsp;&nbsp;├── <span class="file">index.html</span> &nbsp;<span class="comment">← your homepage</span><br>
  &nbsp;&nbsp;├── <span class="folder">css/</span><br>
  &nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└── <span class="file">style.css</span> &nbsp;<span class="comment">← all your styles</span><br>
  &nbsp;&nbsp;├── <span class="folder">js/</span><br>
  &nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└── <span class="file">main.js</span> &nbsp;<span class="comment">← scripts (optional)</span><br>
  &nbsp;&nbsp;└── <span class="folder">images/</span><br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── <span class="file">profile.jpg</span> &nbsp;<span class="comment">← your assets</span>
</div>

One folder per file type. Simple. Scalable. Standard.

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Naming Rules

Bad names cause silent bugs. Follow these three rules:

- **No spaces** — use hyphens instead: `my-photo.jpg` not `my photo.jpg`
- **Lowercase only** — `style.css` not `Style.CSS` (servers are case-sensitive)
- **No special characters** — no `&`, `#`, `@`, or accents

&nbsp;

<div class="highlight">

✅ &nbsp;`about-me.html` &nbsp; `hero-image.jpg` &nbsp; `main.js`

❌ &nbsp;`About Me.html` &nbsp; `Hero Image (1).jpg` &nbsp; `Main_Script.JS`

</div>

When in doubt: lowercase, hyphens, no symbols.

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Relative vs Absolute Paths

A **path** is how your HTML file finds other files.

<div class="two-col">
  <div class="col-card">
    <div class="label">✅ Relative Path</div>
    <code>css/style.css</code><br>
    <code>images/photo.jpg</code><br>
    <code>../index.html</code>
    <p style="font-size:14px; margin-top:12px; color:#6b7280">Starts from the current file's location. Works everywhere — local and deployed.</p>
  </div>
  <div class="col-card">
    <div class="label">⚠️ Absolute Path</div>
    <code>C:/Users/Julius/site/css/style.css</code>
    <p style="font-size:14px; margin-top:12px; color:#6b7280">Hardcoded to your machine. Breaks the moment you upload to a server.</p>
  </div>
</div>

&nbsp;

**Always use relative paths** in your HTML and CSS.

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Why `index.html` is Special

Every web server looks for `index.html` **first** — automatically.

> https://yoursite.com/ → loads index.html
> https://yoursite.com/about/ → loads about/index.html

&nbsp;

- You don't type `index.html` in the URL — the server does it for you
- **Always name your homepage** `index.html`, not `home.html` or `main.html`
- Subfolders can each have their own `index.html` for cleaner URLs

<div class="highlight">

**Rule:** One `index.html` per folder. It's the default door into that directory.

</div>

---

## Quick Reference

<div class="folder-tree">
  <span class="comment"># The complete structure, one more time</span><br><br>
  <span class="folder">my-website/</span><br>
  &nbsp;&nbsp;├── <span class="file">index.html</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="comment">← always here, always this name</span><br>
  &nbsp;&nbsp;├── <span class="folder">css/</span><span class="file">style.css</span> &nbsp;&nbsp;<span class="comment">← link with: href="css/style.css"</span><br>
  &nbsp;&nbsp;├── <span class="folder">js/</span><span class="file">main.js</span> &nbsp;&nbsp;&nbsp;&nbsp;<span class="comment">← link with: src="js/main.js"</span><br>
  &nbsp;&nbsp;└── <span class="folder">images/</span><span class="file">photo.jpg</span> &nbsp;<span class="comment">← use: src="images/photo.jpg"</span>
</div>

&nbsp;

✦ Lowercase names &nbsp;·&nbsp; Hyphens not spaces &nbsp;·&nbsp; Relative paths always

---

<!-- _class: final -->

# Structure First.
# Build Second.

&nbsp;

Get this right at the start and everything else gets easier.

&nbsp;

**Check out my other tutorials →**
*More fundamentals you actually need to know*