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

  /* ── Color swatch row ── */
  .swatch-row {
    display: flex;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    height: 56px;
    margin: 10px 0;
    box-shadow: 0 1px 4px rgba(0,0,0,0.10);
  }

  .swatch {
    flex: 1;
    display: flex;
    align-items: flex-end;
    justify-content: center;
    padding-bottom: 7px;
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    font-weight: 500;
    letter-spacing: 0.04em;
  }

  /* ── Palette card (steal-these section) ── */
  .palette-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 14px;
    margin-top: 16px;
  }

  .palette-card {
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
  }

  .palette-card .pal-swatches {
    display: flex;
    height: 52px;
  }

  .palette-card .pal-swatch {
    flex: 1;
  }

  .palette-card .pal-info {
    padding: 12px 14px;
    background: var(--white);
  }

  .palette-card .pal-name {
    font-weight: 600;
    font-size: 14px;
    color: var(--text);
  }

  .palette-card .pal-mood {
    font-size: 12px;
    color: var(--muted);
    margin-top: 2px;
  }

  .palette-card .pal-hex {
    display: flex;
    gap: 6px;
    margin-top: 8px;
    flex-wrap: wrap;
  }

  .palette-card .pal-hex span {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    color: var(--blue);
    background: var(--blue-light);
    padding: 2px 7px;
    border-radius: 4px;
    border: 1px solid var(--blue-mid);
  }

  /* ── 60-30-10 bar ── */
  .ratio-bar {
    display: flex;
    border-radius: 10px;
    overflow: hidden;
    height: 48px;
    margin: 16px 0;
    box-shadow: 0 1px 4px rgba(0,0,0,0.10);
  }

  .ratio-bar .seg {
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    font-weight: 500;
  }

  /* ── Tool cards (free tools) ── */
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

  /* ── Cheatsheet table ── */
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

  /* ── Extraction steps ── */
  .extract-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .extract-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 18px;
  }

  .extract-card .ex-num {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--blue);
    font-weight: 500;
    letter-spacing: 0.06em;
    margin-bottom: 6px;
  }

  .extract-card .ex-title {
    font-weight: 600;
    font-size: 14px;
    color: var(--text);
    margin-bottom: 4px;
  }

  .extract-card .ex-desc {
    font-size: 13px;
    color: var(--muted);
    line-height: 1.5;
  }
---

<!-- _class: cover -->

# Pick a Color Palette
## That Actually Works

&nbsp;

**Color isn't decoration.** It's the first thing visitors trust — or don't.

`60-30-10` · `primary` · `accent` · `neutral` · `hex`

---

## Why Random Colors Break Trust

Visitors form a visual impression in **under 100ms**. Mismatched colors signal "amateur" before they read a single word.

<div class="tools">
  <div class="tool-card">
    <div class="icon">🧠</div>
    <div class="name">It's subconscious</div>
    <div class="desc">Users don't think "bad colors." They just feel uneasy and leave. Color is felt, not analyzed.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🎯</div>
    <div class="name">Color signals intent</div>
    <div class="desc">Blue builds trust. Green signals growth. Orange creates urgency. Wrong color, wrong message.</div>
  </div>
  <div class="tool-card">
    <div class="icon">⚠️</div>
    <div class="name">The most common mistake</div>
    <div class="desc">Using too many colors — one for each section, button, and heading. Visual noise reads as chaos.</div>
  </div>
  <div class="tool-card">
    <div class="icon">✅</div>
    <div class="name">The fix is simple</div>
    <div class="desc">Limit yourself to 3 roles: one dominant color, one supporting color, one accent. That's the whole system.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## The 60-30-10 Rule

Every well-designed site (and room, and outfit) follows this ratio.

<div class="ratio-bar">
  <div class="seg" style="flex:6; background:#f1f5f9; color:#334155;">60% — Neutral</div>
  <div class="seg" style="flex:3; background:#2563eb; color:#fff;">30% — Primary</div>
  <div class="seg" style="flex:1; background:#f59e0b; color:#fff;">10%</div>
</div>

<div class="two-col">
  <div class="col-card">
    <div class="label">60% — Dominant / Neutral</div>
    <p style="font-size:13.5px; margin-top:8px;">Backgrounds, whitespace, large sections. Usually white, off-white, or a very light tint. This is the breathing room.</p>
  </div>
  <div class="col-card">
    <div class="label">30% — Primary Brand Color</div>
    <p style="font-size:13.5px; margin-top:8px;">Headers, navbars, cards, sidebars. Your main color — the one people associate with your brand.</p>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**10% — Accent:** CTAs, links, badges, highlights. This is your <strong>action color</strong>. Use it sparingly so it always draws the eye.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Primary + Accent + Neutral

Three color roles. Every color on your site should map to one of them.

<div class="swatch-row">
  <div class="swatch" style="background:#1e293b; color:#94a3b8;">Primary</div>
  <div class="swatch" style="background:#334155; color:#94a3b8;">&nbsp;</div>
  <div class="swatch" style="background:#f59e0b; color:#fff;">Accent</div>
  <div class="swatch" style="background:#fef3c7; color:#92400e;">&nbsp;</div>
  <div class="swatch" style="background:#f8fafc; color:#94a3b8;">Neutral</div>
  <div class="swatch" style="background:#e2e8f0; color:#64748b;">&nbsp;</div>
</div>

<div class="cmd-grid" style="margin-top:14px;">
  <div class="cmd-row">
    <div class="cmd-name" style="min-width:80px;">Primary</div>
    <div class="cmd-desc">Your brand color. Used for nav, headings, key UI elements.<span>Pick one. Derive a darker shade for hover states.</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name" style="min-width:80px;">Accent</div>
    <div class="cmd-desc">High-contrast pop. Used only for CTAs, links, badges.<span>Should be visually different from primary — not just darker.</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name" style="min-width:80px;">Neutral</div>
    <div class="cmd-desc">Light backgrounds, borders, muted text, dividers.<span>Usually greys or warm off-whites. The glue of your palette.</span></div>
  </div>
  <div class="cmd-row">
    <div class="cmd-name" style="min-width:80px;">Text</div>
    <div class="cmd-desc">Near-black for body, medium grey for secondary content.<span>Never pure #000000 — it's too harsh. Use #111827.</span></div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Free Tools to Build Your Palette

<div class="tool-row">
  <div class="tool-item">
    <div class="t-icon">🎨</div>
    <div>
      <div class="t-name">Coolors</div>
      <div class="t-url">coolors.co</div>
      <div class="t-desc">Hit spacebar to generate palettes. Lock colors you like and keep regenerating. Fast and addictive.</div>
    </div>
  </div>
  <div class="tool-item">
    <div class="t-icon">🖥️</div>
    <div>
      <div class="t-name">Realtime Colors</div>
      <div class="t-url">realtimecolors.com</div>
      <div class="t-desc">Preview your palette on a live webpage as you pick colors. The best way to see if it actually works.</div>
    </div>
  </div>
  <div class="tool-item">
    <div class="t-icon">🌈</div>
    <div>
      <div class="t-name">Paletton</div>
      <div class="t-url">paletton.com</div>
      <div class="t-desc">Color wheel-based builder. Great for generating complementary and triadic schemes with theory baked in.</div>
    </div>
  </div>
  <div class="tool-item">
    <div class="t-icon">🔬</div>
    <div>
      <div class="t-name">WebAIM Contrast Checker</div>
      <div class="t-url">webaim.org/resources/contrastchecker</div>
      <div class="t-desc">Paste two colors, check if text is readable. WCAG AA requires a ratio of 4.5:1. Don't skip this step.</div>
    </div>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**Workflow:** Build in Coolors → preview on Realtime Colors → verify contrast on WebAIM → copy hex codes into your CSS.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## How to Extract Colors from Inspiration Sites

Find a site you love and reverse-engineer its palette in four steps.

<div class="extract-grid">
  <div class="extract-card">
    <div class="ex-num">STEP 01</div>
    <div class="ex-title">Use a browser eyedropper</div>
    <div class="ex-desc">In Chrome, open DevTools (F12) → Elements → click any element → its color shows in the Styles panel. Or use the CSS Overview tool.</div>
  </div>
  <div class="extract-card">
    <div class="ex-num">STEP 02</div>
    <div class="ex-title">Screenshot + upload to Coolors</div>
    <div class="ex-desc">Take a screenshot of the site. Go to coolors.co → "Create" → "Image" → upload it. Coolors extracts the dominant colors automatically.</div>
  </div>
  <div class="extract-card">
    <div class="ex-num">STEP 03</div>
    <div class="ex-title">Install the ColorZilla extension</div>
    <div class="ex-desc">Free Chrome/Firefox extension. Hover over any pixel on any webpage and it shows the exact hex code. Instant, accurate, free.</div>
  </div>
  <div class="extract-card">
    <div class="ex-num">STEP 04</div>
    <div class="ex-title">Map to your 3 roles</div>
    <div class="ex-desc">Don't copy everything. Identify which extracted color is their primary, which is their accent, which is neutral. Borrow the roles, not the exact shades.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## 3 Ready-Made Palettes to Steal

<div class="palette-grid">
  <div class="palette-card">
    <div class="pal-swatches">
      <div class="pal-swatch" style="background:#0f172a;"></div>
      <div class="pal-swatch" style="background:#2563eb;"></div>
      <div class="pal-swatch" style="background:#60a5fa;"></div>
      <div class="pal-swatch" style="background:#f8fafc;"></div>
      <div class="pal-swatch" style="background:#f59e0b;"></div>
    </div>
    <div class="pal-info">
      <div class="pal-name">Midnight Tech</div>
      <div class="pal-mood">Confident, modern, SaaS</div>
      <div class="pal-hex">
        <span>#0f172a</span><span>#2563eb</span><span>#60a5fa</span><span>#f8fafc</span><span>#f59e0b</span>
      </div>
    </div>
  </div>
  <div class="palette-card">
    <div class="pal-swatches">
      <div class="pal-swatch" style="background:#064e3b;"></div>
      <div class="pal-swatch" style="background:#059669;"></div>
      <div class="pal-swatch" style="background:#6ee7b7;"></div>
      <div class="pal-swatch" style="background:#f9fafb;"></div>
      <div class="pal-swatch" style="background:#f97316;"></div>
    </div>
    <div class="pal-info">
      <div class="pal-name">Fresh Growth</div>
      <div class="pal-mood">Organic, startup, wellness</div>
      <div class="pal-hex">
        <span>#064e3b</span><span>#059669</span><span>#6ee7b7</span><span>#f9fafb</span><span>#f97316</span>
      </div>
    </div>
  </div>
  <div class="palette-card">
    <div class="pal-swatches">
      <div class="pal-swatch" style="background:#1c1917;"></div>
      <div class="pal-swatch" style="background:#78716c;"></div>
      <div class="pal-swatch" style="background:#e7e5e4;"></div>
      <div class="pal-swatch" style="background:#fafaf9;"></div>
      <div class="pal-swatch" style="background:#dc2626;"></div>
    </div>
    <div class="pal-info">
      <div class="pal-name">Editorial Stone</div>
      <div class="pal-mood">Minimal, portfolio, agency</div>
      <div class="pal-hex">
        <span>#1c1917</span><span>#78716c</span><span>#e7e5e4</span><span>#fafaf9</span><span>#dc2626</span>
      </div>
    </div>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**How to use them:** The first color is your primary, the middle two are neutrals, the last is your accent. Plug all five into Realtime Colors to preview before committing.

</div>

---

## Color Decision Cheatsheet

<table class="cheat-table">
  <tr>
    <th>Situation</th>
    <th>What to do</th>
  </tr>
  <tr>
    <td>Starting from zero</td>
    <td>Open Coolors, hit spacebar until something feels right, lock it, build around it</td>
  </tr>
  <tr>
    <td>You have a logo already</td>
    <td>Extract the logo's primary color — that's your primary. Build neutrals and an accent around it</td>
  </tr>
  <tr>
    <td>Text is hard to read</td>
    <td>Check contrast on WebAIM. Aim for 4.5:1 ratio minimum. Darken text or lighten background</td>
  </tr>
  <tr>
    <td>Too many colors on the page</td>
    <td>Apply the 60-30-10 rule. Audit every color — if it doesn't fit a role, remove it</td>
  </tr>
  <tr>
    <td>Nothing looks professional</td>
    <td>Desaturate slightly. Pure saturated colors often look toy-like. Muted tones read as refined</td>
  </tr>
  <tr>
    <td>Picking an accent color</td>
    <td>Look at the opposite side of the color wheel from your primary. Complementary pairs always pop</td>
  </tr>
  <tr>
    <td>Dark mode version needed</td>
    <td>Swap neutral (background) and primary. Lighten your text color. Keep the accent as-is</td>
  </tr>
  <tr>
    <td>Color feels off but you don't know why</td>
    <td>Try shifting the hue by 10–15°. Tiny hue shifts change mood dramatically without changing the overall scheme</td>
  </tr>
</table>

---

<!-- _class: final -->

# Good color is invisible.
# Bad color is unforgettable.

&nbsp;

Pick three roles. Follow the ratio. Check the contrast.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*