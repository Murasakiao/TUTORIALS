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

  /* ── Waiter analogy flow ── */
  .flow {
    display: flex;
    align-items: center;
    gap: 0;
    margin: 20px 0;
  }

  .flow-node {
    flex: 1;
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 18px 16px;
    text-align: center;
  }

  .flow-node .fn-icon { font-size: 28px; margin-bottom: 6px; }
  .flow-node .fn-label {
    font-weight: 600;
    font-size: 14px;
    color: var(--text);
  }
  .flow-node .fn-sub {
    font-size: 12px;
    color: var(--muted);
    margin-top: 3px;
    font-family: 'DM Mono', monospace;
  }

  .flow-arrow {
    flex-shrink: 0;
    width: 48px;
    text-align: center;
    font-size: 20px;
    color: var(--blue);
    padding: 0 2px;
  }

  .flow-arrow .fa-label {
    font-family: 'DM Mono', monospace;
    font-size: 9.5px;
    color: var(--muted);
    display: block;
    margin-top: 2px;
    letter-spacing: 0.04em;
  }

  /* ── Request/Response diagram ── */
  .req-res {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    gap: 0;
    align-items: center;
    margin: 16px 0;
  }

  .rr-box {
    background: #111827;
    border-radius: 12px;
    padding: 20px 22px;
    font-family: 'DM Mono', monospace;
    font-size: 12.5px;
    line-height: 1.9;
    color: #f9fafb;
    white-space: pre;
  }

  .rr-box .rr-label {
    font-size: 10px;
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 10px;
    display: block;
    font-family: 'DM Sans', monospace;
    white-space: normal;
  }

  .rr-box .t-key   { color: #93c5fd; }
  .rr-box .t-str   { color: #34d399; }
  .rr-box .t-num   { color: #fb923c; }
  .rr-box .t-punct { color: #6b7280; }
  .rr-box .t-met   { color: #f472b6; }
  .rr-box .t-url   { color: #fbbf24; }

  .rr-middle {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    padding: 0 18px;
  }

  .rr-pill {
    background: var(--blue);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    padding: 5px 14px;
    border-radius: 999px;
    white-space: nowrap;
  }

  .rr-arrow {
    font-size: 18px;
    color: var(--blue);
    line-height: 1;
  }

  /* ── Real-world examples grid ── */
  .eg-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 14px;
    margin-top: 16px;
  }

  .eg-card {
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
  }

  .eg-card .eg-top {
    padding: 18px 16px 12px;
    background: var(--off-white);
    text-align: center;
  }

  .eg-card .eg-icon { font-size: 30px; margin-bottom: 6px; }

  .eg-card .eg-title {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
  }

  .eg-card .eg-bottom {
    padding: 12px 16px;
    background: var(--white);
    border-top: 1px solid var(--border);
  }

  .eg-card .eg-asks {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    color: var(--blue);
    margin-bottom: 4px;
  }

  .eg-card .eg-gets {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.5;
  }
---

<!-- _class: cover -->

# What is an API?
## Explained Without the Jargon

&nbsp;

**You use APIs dozens of times a day.** You just didn't know they had a name.

`Request` · `Response` · `Endpoint` · `JSON` · `Why it matters`

---

## APIs Are Everywhere — You Just Can't See Them

Every time an app goes out to get something, it uses an API.

<div class="tools">
  <div class="tool-card">
    <div class="icon">🌤️</div>
    <div class="name">Weather apps</div>
    <div class="desc">Your phone's weather app doesn't collect weather data. It calls a weather API. The API returns today's forecast. The app just displays it.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔐</div>
    <div class="name">"Sign in with Google"</div>
    <div class="desc">That button doesn't give the app your Google password. It calls Google's API to verify who you are — and Google sends back a thumbs up.</div>
  </div>
  <div class="tool-card">
    <div class="icon">💳</div>
    <div class="name">Online payments</div>
    <div class="desc">When you check out on a website, the site calls Stripe's or PayPal's API to handle the transaction. Your card data never touches their server.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🗺️</div>
    <div class="name">Maps in apps</div>
    <div class="desc">Uber, Airbnb, and Yelp all show maps — but none of them built a maps product. They all call the Google Maps API to embed it.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## The Waiter Analogy

An API is a **messenger** that takes your request, delivers it to the right place, and brings back the result.

<div class="flow" style="margin-top: 24px;">
  <div class="flow-node">
    <div class="fn-icon">🧑</div>
    <div class="fn-label">You (the app)</div>
    <div class="fn-sub">places an order</div>
  </div>
  <div class="flow-arrow">→<div class="fa-label">REQUEST</div></div>
  <div class="flow-node" style="background: var(--blue-light); border-color: var(--blue-mid);">
    <div class="fn-icon">🤵</div>
    <div class="fn-label">The API (waiter)</div>
    <div class="fn-sub">carries the message</div>
  </div>
  <div class="flow-arrow">→<div class="fa-label">QUERY</div></div>
  <div class="flow-node">
    <div class="fn-icon">👨‍🍳</div>
    <div class="fn-label">The server (kitchen)</div>
    <div class="fn-sub">has all the data</div>
  </div>
  <div class="flow-arrow">←<div class="fa-label">RESPONSE</div></div>
  <div class="flow-node" style="background: var(--blue-light); border-color: var(--blue-mid);">
    <div class="fn-icon">🍽️</div>
    <div class="fn-label">Your result</div>
    <div class="fn-sub">delivered back</div>
  </div>
</div>

<div class="highlight">

The key insight: **you never go into the kitchen.** You don't need to know how the food is made. You just place your order — the API handles the rest.

</div>

<p style="font-size:14px; color:var(--muted); margin-top:8px;">This is exactly how apps work. Your app never touches the other company's database directly. It just asks the API politely — and gets a clean answer back.</p>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Why Apps Need APIs

No app builds everything from scratch. APIs let apps **borrow capabilities** from other services.

<div class="eg-grid">
  <div class="eg-card">
    <div class="eg-top">
      <div class="eg-icon">🚗</div>
      <div class="eg-title">Uber</div>
    </div>
    <div class="eg-bottom">
      <div class="eg-asks">APIs it calls →</div>
      <div class="eg-gets">Google Maps for routing · Stripe for payments · Twilio for SMS alerts</div>
    </div>
  </div>
  <div class="eg-card">
    <div class="eg-top">
      <div class="eg-icon">✈️</div>
      <div class="eg-title">Flight booking sites</div>
    </div>
    <div class="eg-bottom">
      <div class="eg-asks">APIs it calls →</div>
      <div class="eg-gets">Airline APIs for live seat availability · Currency APIs for prices</div>
    </div>
  </div>
  <div class="eg-card">
    <div class="eg-top">
      <div class="eg-icon">🤖</div>
      <div class="eg-title">ChatGPT in your app</div>
    </div>
    <div class="eg-bottom">
      <div class="eg-asks">APIs it calls →</div>
      <div class="eg-gets">OpenAI's API to run the AI · No model training required</div>
    </div>
  </div>
</div>

<div class="highlight" style="margin-top: 18px;">

**The business logic:** APIs let small teams build powerful products by standing on the shoulders of giants. You focus on your core idea — and plug in everything else via API.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## A Request and a Response

Every API interaction has two parts: you **ask** for something, and the server **answers**.

<div class="req-res">
  <div class="rr-box"><span class="rr-label">REQUEST — what you send</span><span class="t-met">GET</span> <span class="t-url">/weather</span>
<span class="t-punct">{</span>
  <span class="t-key">"city"</span><span class="t-punct">:</span> <span class="t-str">"Manila"</span><span class="t-punct">,</span>
  <span class="t-key">"units"</span><span class="t-punct">:</span> <span class="t-str">"metric"</span>
<span class="t-punct">}</span></div>
  <div class="rr-middle">
    <div class="rr-pill">→ API →</div>
    <div class="rr-arrow">⇄</div>
    <div class="rr-pill">← API ←</div>
  </div>
  <div class="rr-box"><span class="rr-label">RESPONSE — what comes back</span><span class="t-punct">{</span>
  <span class="t-key">"city"</span><span class="t-punct">:</span> <span class="t-str">"Manila"</span><span class="t-punct">,</span>
  <span class="t-key">"temp"</span><span class="t-punct">:</span> <span class="t-num">31</span><span class="t-punct">,</span>
  <span class="t-key">"condition"</span><span class="t-punct">:</span> <span class="t-str">"Sunny"</span>
<span class="t-punct">}</span></div>
</div>

<div class="cmd-grid" style="margin-top: 16px;">
  <div class="cmd-row">
    <div class="cmd-name">Endpoint</div>
    <div class="cmd-desc">The specific URL you send requests to<span>Like a department within the kitchen</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">Request</div>
    <div class="cmd-desc">What you're asking for, plus any details<span>Your order, written on a slip of paper</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">Response</div>
    <div class="cmd-desc">The data the server sends back<span>Your food, arriving at the table</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name">JSON</div>
    <div class="cmd-desc">The common format data travels in<span>The language the waiter and kitchen share</span></div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## The Key Terms, Simply Defined

<table class="cheat-table">
  <tr>
    <th>Term</th>
    <th>Plain English</th>
    <th>Restaurant equivalent</th>
  </tr>
  <tr>
    <td class="mono">API</td>
    <td>A messenger between two software systems</td>
    <td>The waiter</td>
  </tr>
  <tr>
    <td class="mono">Endpoint</td>
    <td>A specific URL that does one thing</td>
    <td>A specific section of the menu</td>
  </tr>
  <tr>
    <td class="mono">Request</td>
    <td>What your app sends to the API</td>
    <td>Placing your order</td>
  </tr>
  <tr>
    <td class="mono">Response</td>
    <td>What the API sends back</td>
    <td>Your food arriving</td>
  </tr>
  <tr>
    <td class="mono">JSON</td>
    <td>The format data is usually sent in</td>
    <td>The standard order ticket format</td>
  </tr>
  <tr>
    <td class="mono">API Key</td>
    <td>A password that proves who you are</td>
    <td>Your reservation name</td>
  </tr>
  <tr>
    <td class="mono">Rate limit</td>
    <td>A cap on how many requests you can make</td>
    <td>Last orders at the kitchen</td>
  </tr>
  <tr>
    <td class="mono">Status 200</td>
    <td>Everything worked — here's your data</td>
    <td>Order confirmed ✓</td>
  </tr>
  <tr>
    <td class="mono">Status 404</td>
    <td>That thing you asked for doesn't exist</td>
    <td>Sorry, we're out of that dish</td>
  </tr>
</table>

---

<!-- _class: final -->

# Apps don't build everything.
# They just know who to ask.

&nbsp;

An API is just a messenger. Request in, response out.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*