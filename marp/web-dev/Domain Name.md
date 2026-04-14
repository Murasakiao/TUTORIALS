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

  /* DNS flow diagram */
  .dns-flow {
    display: flex;
    align-items: center;
    gap: 0;
    margin: 20px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .dns-node {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 10px 16px;
    text-align: center;
    flex: 1;
  }

  .dns-node .node-label {
    font-size: 11px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 4px;
  }

  .dns-node .node-val {
    font-weight: 500;
    color: var(--text);
    font-size: 13px;
  }

  .dns-arrow {
    color: var(--blue);
    font-size: 20px;
    padding: 0 6px;
    flex-shrink: 0;
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

  /* Step list */
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

  /* DNS record table */
  .dns-table {
    width: 100%;
    border-collapse: collapse;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    margin: 16px 0;
  }

  .dns-table th {
    background: var(--text);
    color: white;
    padding: 8px 14px;
    text-align: left;
    font-weight: 500;
    font-size: 12px;
    letter-spacing: 0.05em;
  }

  .dns-table td {
    padding: 9px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
  }

  .dns-table tr:nth-child(even) td { background: var(--off-white); }

  .dns-table .mono { color: var(--blue); }
---

<!-- _class: cover -->

# What is a Domain Name
## and How Do You Get One

&nbsp;

**Your address on the internet** — and how to make it yours.

`dns` · `ip address` · `namecheap` · `github pages`

---

## Every Website Has an Address

Before domains, you had to memorize numbers to visit a website.

<div class="url-box">
  🔢 &nbsp; 185.199.108.153 &nbsp;&nbsp;→&nbsp;&nbsp; 🌐 &nbsp; yoursite.com
</div>

<div class="tools">
  <div class="tool-card">
    <div class="icon">🔢</div>
    <div class="name">IP Address</div>
    <div class="desc">The actual numerical location of a server. Every device on the internet has one.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🏷️</div>
    <div class="name">Domain Name</div>
    <div class="desc">A human-readable label that maps to an IP. Much easier to share and remember.</div>
  </div>
  <div class="tool-card">
    <div class="icon">📖</div>
    <div class="name">DNS</div>
    <div class="desc">The system that translates domain names into IP addresses — automatically.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🏢</div>
    <div class="name">Registrar</div>
    <div class="desc">The company where you buy and manage your domain name.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## How DNS Works

DNS stands for **Domain Name System**. Think of it as the internet's phonebook — you look up a name, it returns a number.

&nbsp;

<div class="dns-flow">
  <div class="dns-node">
    <div class="node-label">You type</div>
    <div class="node-val">yoursite.com</div>
  </div>
  <div class="dns-arrow">→</div>
  <div class="dns-node">
    <div class="node-label">DNS Lookup</div>
    <div class="node-val">DNS Server</div>
  </div>
  <div class="dns-arrow">→</div>
  <div class="dns-node">
    <div class="node-label">Returns IP</div>
    <div class="node-val">185.199.108.153</div>
  </div>
  <div class="dns-arrow">→</div>
  <div class="dns-node">
    <div class="node-label">Browser loads</div>
    <div class="node-val">Your website</div>
  </div>
</div>

&nbsp;

This happens in **milliseconds**, invisibly, every time someone visits a URL. You configure DNS records to control where your domain points.

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Free Option: GitHub Pages Subdomain

When you deploy to GitHub Pages, you get a free URL automatically — no purchase needed.

<div class="url-box">
  🔗 &nbsp; https://<span style="color:#86efac">yourusername</span>.github.io/<span style="color:#fca5a5">repository-name</span>
</div>

- **No setup required** — it's assigned the moment you enable Pages
- **Completely free**, forever
- Great for portfolios, demos, and personal projects
- The tradeoff: your username and GitHub's brand are baked into the URL

<div class="highlight">

**When the free subdomain is enough:**
You're sharing a portfolio, a side project, or a tutorial site — and you don't need a custom brand. `yourusername.github.io/portfolio` is perfectly professional.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Paid Options: Buying a Domain

A custom domain costs ~$10–15/year. Two registrars stand out for beginners:

<div class="two-col">
  <div class="col-card">
    <div class="label">🐷 Porkbun — porkbun.com</div>
    <p style="font-size:14px; margin-top:8px">Consistently the cheapest prices. Clean, no-nonsense UI. Includes free WHOIS privacy on every domain. Highly recommended for first-time buyers.</p>
  </div>
  <div class="col-card">
    <div class="label">🌿 Namecheap — namecheap.com</div>
    <p style="font-size:14px; margin-top:8px">Reliable, well-established, good support. Free WHOIS privacy included. Slightly more expensive than Porkbun but still very affordable.</p>
  </div>
</div>

&nbsp;

> Avoid buying domains from web hosts bundled with "free hosting deals" — they lock you in and renewals are expensive.

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## How to Connect a Domain to GitHub Pages

Once you own a domain, four DNS records point it to GitHub's servers.

<table class="dns-table">
  <tr>
    <th>Type</th>
    <th>Host</th>
    <th>Value</th>
    <th>Purpose</th>
  </tr>
  <tr>
    <td>A</td>
    <td class="mono">@</td>
    <td class="mono">185.199.108.153</td>
    <td>Root domain → GitHub</td>
  </tr>
  <tr>
    <td>A</td>
    <td class="mono">@</td>
    <td class="mono">185.199.109.153</td>
    <td>Redundancy</td>
  </tr>
  <tr>
    <td>A</td>
    <td class="mono">@</td>
    <td class="mono">185.199.110.153</td>
    <td>Redundancy</td>
  </tr>
  <tr>
    <td>CNAME</td>
    <td class="mono">www</td>
    <td class="mono">yourusername.github.io</td>
    <td>www subdomain</td>
  </tr>
</table>

Add these in your registrar's **DNS settings panel** — then wait up to 24 hours to propagate.

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## Finishing the Connection in GitHub

After your DNS records are set, tell GitHub about your custom domain:

<ul class="step-list">
  <li>Go to your repository → <strong>Settings → Pages</strong></li>
  <li>Under <strong>Custom domain</strong>, enter your domain (e.g. <code>yoursite.com</code>) and click Save</li>
  <li>GitHub will create a <code>CNAME</code> file in your repo automatically</li>
  <li>Wait for the DNS check to pass — a green checkmark appears when it's verified</li>
  <li>Check <strong>Enforce HTTPS</strong> once available — this adds the padlock to your URL</li>
</ul>

<div class="highlight">

⏳ DNS propagation can take anywhere from a few minutes to 24 hours. If it's not working yet — wait, don't panic.

</div>

---

## The Full Picture

<div class="dns-flow" style="margin-bottom: 20px;">
  <div class="dns-node">
    <div class="node-label">Buy domain</div>
    <div class="node-val">Porkbun / Namecheap</div>
  </div>
  <div class="dns-arrow">→</div>
  <div class="dns-node">
    <div class="node-label">Add DNS records</div>
    <div class="node-val">A + CNAME</div>
  </div>
  <div class="dns-arrow">→</div>
  <div class="dns-node">
    <div class="node-label">Set custom domain</div>
    <div class="node-val">GitHub Pages</div>
  </div>
  <div class="dns-arrow">→</div>
  <div class="dns-node">
    <div class="node-label">Live at</div>
    <div class="node-val">yoursite.com</div>
  </div>
</div>

<div class="highlight">

**Free route:** `yourusername.github.io/repo` — zero cost, zero setup, works immediately.

**Custom domain:** ~$10/year + 30 minutes of setup — your name, your brand, your URL.

</div>

---

<!-- _class: final -->

# Your Name.
# Your Domain.

&nbsp;

A custom domain is the cheapest upgrade you can make to look serious online.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*