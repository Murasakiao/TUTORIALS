---
marp: true
theme: default
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=DM+Mono:wght@400;500&display=swap');

  :root {
    --orange: #ea580c;
    --orange-light: #fff7ed;
    --orange-mid: #fed7aa;
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
    border-bottom: 2px solid var(--orange);
    padding-bottom: 10px;
    margin-bottom: 24px;
  }

  h3 {
    font-family: 'DM Sans', sans-serif;
    font-size: 20px;
    font-weight: 500;
    color: var(--orange);
    margin-bottom: 8px;
  }

  p { color: var(--text); margin: 0.4em 0; }
  ul { padding-left: 1.4em; }
  li { margin-bottom: 10px; color: var(--text); }
  strong { color: var(--orange); font-weight: 600; }

  code {
    font-family: 'DM Mono', monospace;
    background: var(--orange-light);
    color: var(--orange);
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.88em;
  }

  blockquote {
    border-left: 4px solid var(--orange);
    background: var(--orange-light);
    padding: 16px 20px;
    margin: 20px 0;
    border-radius: 0 8px 8px 0;
    font-family: 'DM Mono', monospace;
    font-size: 0.82em;
    color: #9a3412;
    line-height: 1.6;
  }

  blockquote p { color: #9a3412; margin: 0; }

  section.cover {
    background: var(--text);
    color: var(--white);
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  section.cover h1 { color: var(--white); font-size: 46px; }
  section.cover h2 { color: #fdba74; border-bottom-color: #374151; }
  section.cover p  { color: #9ca3af; }
  section.cover strong { color: #fb923c; }
  section.cover code { background: #431407; color: #fdba74; }

  section.step { background: var(--off-white); }

  .highlight {
    background: var(--orange-light);
    border: 1px solid var(--orange-mid);
    border-radius: 10px;
    padding: 18px 24px;
    margin: 16px 0;
  }

  .browsers {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    margin-top: 20px;
  }

  .browser-card {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 18px 14px;
    text-align: center;
  }

  .browser-card .icon  { font-size: 32px; margin-bottom: 8px; }
  .browser-card .name  { font-weight: 600; font-size: 15px; color: var(--text); }
  .browser-card .desc  { font-size: 12px; color: var(--muted); margin-top: 4px; }

  .step-badge {
    display: inline-block;
    background: var(--orange);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    padding: 4px 14px;
    border-radius: 999px;
    margin-bottom: 12px;
    letter-spacing: 0.05em;
  }

  .journey {
    display: flex;
    align-items: stretch;
    gap: 0;
    margin: 20px 0;
  }

  .journey-step {
    flex: 1;
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 16px;
    text-align: center;
    position: relative;
  }

  .journey-step .num {
    display: inline-block;
    background: var(--orange);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 600;
    width: 22px;
    height: 22px;
    border-radius: 999px;
    line-height: 22px;
    margin-bottom: 6px;
  }

  .journey-step .label {
    font-size: 13px;
    font-weight: 600;
    color: var(--text);
    margin-bottom: 4px;
  }

  .journey-step .sub {
    font-size: 11px;
    color: var(--muted);
    font-family: 'DM Mono', monospace;
  }

  .arrow {
    display: flex;
    align-items: center;
    padding: 0 6px;
    color: var(--orange);
    font-size: 18px;
  }

  .render-steps {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 16px;
  }

  .render-card {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-left: 3px solid var(--orange);
    border-radius: 0 10px 10px 0;
    padding: 14px 18px;
  }

  .render-card .title {
    font-weight: 600;
    font-size: 14px;
    color: var(--text);
    margin-bottom: 4px;
  }

  .render-card .body {
    font-size: 13px;
    color: var(--muted);
    line-height: 1.5;
  }

  .cache-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 20px;
  }

  .cache-col {
    border-radius: 10px;
    padding: 20px;
  }

  .cache-col.without {
    background: #fef2f2;
    border: 1px solid #fecaca;
  }

  .cache-col.with {
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
  }

  .cache-col .label {
    font-weight: 600;
    font-size: 13px;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    font-family: 'DM Mono', monospace;
    margin-bottom: 12px;
  }

  .cache-col.without .label { color: #dc2626; }
  .cache-col.with .label { color: #16a34a; }

  .cache-col ul {
    margin: 0;
    padding-left: 1.2em;
  }

  .cache-col li {
    font-size: 13px;
    margin-bottom: 8px;
  }

  .cache-col.without li { color: #7f1d1d; }
  .cache-col.with li { color: #14532d; }

  .ext-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 16px;
  }

  .ext-card {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 18px;
    display: flex;
    gap: 14px;
    align-items: flex-start;
  }

  .ext-card .icon { font-size: 24px; margin-top: 2px; }
  .ext-card .name { font-weight: 600; font-size: 14px; color: var(--text); }
  .ext-card .desc { font-size: 12px; color: var(--muted); margin-top: 3px; line-height: 1.4; }

  section.final {
    background: var(--orange);
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
  }

  section.final h1 { color: white; font-size: 40px; }
  section.final p  { color: #ffedd5; font-size: 18px; }
  section.final strong { color: white; }
  section.final em { color: #ffedd5; }

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
    background: var(--orange);
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

  .url-anatomy {
    background: #111827;
    border-radius: 10px;
    padding: 20px 28px;
    font-family: 'DM Mono', monospace;
    font-size: 17px;
    margin: 20px 0;
    letter-spacing: 0.02em;
    color: #f9fafb;
  }

  .url-anatomy .u-protocol { color: #fb923c; }
  .url-anatomy .u-sep      { color: #6b7280; }
  .url-anatomy .u-domain   { color: #34d399; }
  .url-anatomy .u-tld      { color: #60a5fa; }
  .url-anatomy .u-path     { color: #e2e8f0; }
  .url-anatomy .u-query    { color: #c084fc; }
---

<!-- _class: cover -->

# How Your Browser Actually Works
## A guide for curious beginners

&nbsp;

**You use it every day** — but what's really happening under the hood?

`URL` · `DNS` · `HTML` · `Cache` · `Extensions`

---

## What Even Is a Browser?

A browser is software that **translates the internet** into something humans can read, watch, and click.

Without it, a webpage looks like this:

> `<div class="hero"><h1>Welcome</h1><p>Hello world</p></div>`

With it, you see a beautiful homepage. That translation is the browser's whole job.

<div class="browsers">
  <div class="browser-card">
    <div class="icon">🌐</div>
    <div class="name">Chrome</div>
    <div class="desc">Most popular. By Google.</div>
  </div>
  <div class="browser-card">
    <div class="icon">🦊</div>
    <div class="name">Firefox</div>
    <div class="desc">Open source. Privacy-focused.</div>
  </div>
  <div class="browser-card">
    <div class="icon">🧭</div>
    <div class="name">Safari</div>
    <div class="desc">Built into every Mac & iPhone.</div>
  </div>
  <div class="browser-card">
    <div class="icon">🔷</div>
    <div class="name">Edge</div>
    <div class="desc">Microsoft's modern browser.</div>
  </div>
</div>

They all do the same thing. Pick one and stick to it.

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## What Happens When You Type a URL

You type `google.com` and hit Enter. Here's everything that fires in under a second:

<div class="journey">
  <div class="journey-step">
    <div class="num">1</div>
    <div class="label">You type</div>
    <div class="sub">google.com</div>
  </div>
  <div class="arrow">→</div>
  <div class="journey-step">
    <div class="num">2</div>
    <div class="label">DNS Lookup</div>
    <div class="sub">find the address</div>
  </div>
  <div class="arrow">→</div>
  <div class="journey-step">
    <div class="num">3</div>
    <div class="label">Server Request</div>
    <div class="sub">ask for the page</div>
  </div>
  <div class="arrow">→</div>
  <div class="journey-step">
    <div class="num">4</div>
    <div class="label">Response</div>
    <div class="sub">files sent back</div>
  </div>
  <div class="arrow">→</div>
  <div class="journey-step">
    <div class="num">5</div>
    <div class="label">Render</div>
    <div class="sub">you see a page</div>
  </div>
</div>

**DNS is like a phone book.** `google.com` is a human-friendly name. The internet actually runs on numbers — `142.250.190.46`. DNS translates between them.

<div class="highlight">

**The whole trip takes ~200ms.** That's faster than a blink. This happens every single time you click a link.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Anatomy of a URL

Every URL tells the browser exactly where to go and how to get there.

<div class="url-anatomy">
  <span class="u-protocol">https</span><span class="u-sep">://</span><span class="u-domain">www.example</span><span class="u-tld">.com</span><span class="u-path">/about</span><span class="u-query">?ref=home</span>
</div>

<ul class="step-list">
  <li><strong>https</strong> — The protocol. The "S" means your connection is encrypted. Always look for it.</li>
  <li><strong>www.example</strong> — The domain name. This is what DNS looks up.</li>
  <li><strong>.com</strong> — The top-level domain. Could be .org, .net, .ph, etc.</li>
  <li><strong>/about</strong> — The path. Like a folder inside the website.</li>
  <li><strong>?ref=home</strong> — Query parameters. Extra data passed to the page.</li>
</ul>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## How a Page Gets Rendered

Once the browser receives the files, it builds the page in stages — like assembling flat-pack furniture.

<div class="render-steps">
  <div class="render-card">
    <div class="title">📄 HTML — The Structure</div>
    <div class="body">The skeleton. Tells the browser what elements exist: headings, paragraphs, images, buttons.</div>
  </div>
  <div class="render-card">
    <div class="title">🎨 CSS — The Style</div>
    <div class="body">The paint and furniture. Colors, fonts, spacing, layout. Makes things look good.</div>
  </div>
  <div class="render-card">
    <div class="title">⚡ JavaScript — The Behavior</div>
    <div class="body">The electronics. Makes things interactive — dropdowns, animations, live updates.</div>
  </div>
  <div class="render-card">
    <div class="title">🖼️ Paint — The Display</div>
    <div class="body">Finally, the browser draws pixels to your screen. What you see is the finished result.</div>
  </div>
</div>

&nbsp;

When developers say "build a website," they mean writing these three types of files.

---

## What Is Cache?

Cache (pronounced *"cash"*) is your browser saving copies of websites locally so it doesn't have to download the same thing twice.

<div class="cache-compare">
  <div class="cache-col without">
    <div class="label">❌ Without Cache</div>
    <ul>
      <li>Every visit re-downloads every image, font, and file</li>
      <li>Slow load times, especially on slow connections</li>
      <li>More data usage on mobile</li>
      <li>More load on the server</li>
    </ul>
  </div>
  <div class="cache-col with">
    <div class="label">✅ With Cache</div>
    <ul>
      <li>Browser reuses files it already has</li>
      <li>Pages load almost instantly on repeat visits</li>
      <li>Works partially even offline</li>
      <li>Less bandwidth, faster experience</li>
    </ul>
  </div>
</div>

&nbsp;

**Tip for developers:** When you update a website and it looks the same — clear your cache. The browser is still showing you the old version.

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Extensions — Superpowers for Your Browser

Extensions are mini-apps you install inside the browser. They watch or modify what you see on every page.

<div class="ext-grid">
  <div class="ext-card">
    <div class="icon">🛡️</div>
    <div>
      <div class="name">uBlock Origin</div>
      <div class="desc">Blocks ads and trackers. The single most useful extension for anyone.</div>
    </div>
  </div>
  <div class="ext-card">
    <div class="icon">🔑</div>
    <div>
      <div class="name">1Password / Bitwarden</div>
      <div class="desc">Password manager. Fills in logins for you. Stop reusing passwords.</div>
    </div>
  </div>
  <div class="ext-card">
    <div class="icon">🐛</div>
    <div>
      <div class="name">React DevTools</div>
      <div class="desc">For developers. Inspect how a React app is built under the hood.</div>
    </div>
  </div>
  <div class="ext-card">
    <div class="icon">🎨</div>
    <div>
      <div class="name">ColorZilla</div>
      <div class="desc">Click any color on any webpage to get its exact hex code. Great for design.</div>
    </div>
  </div>
</div>

&nbsp;

**For web development:** The most important built-in tool is `F12` — the DevTools. It's like X-ray vision for any website.

---

<!-- _class: final -->

# The browser is your
# window to everything.

&nbsp;

Now you know what's happening on the other side of the glass.

&nbsp;

**Next up →**
*Learn HTML — write your first line of the web*