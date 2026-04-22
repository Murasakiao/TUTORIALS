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

  /* ── Quick win overview strip ── */
  .quickwin-strip {
    display: flex;
    gap: 8px;
    margin-top: 16px;
    align-items: stretch;
  }

  .qw-item {
    flex: 1;
    border-radius: 10px;
    padding: 14px 10px;
    text-align: center;
    border: 2px solid transparent;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
  }

  .qw-item.one   { background: #fef3c7; border-color: #fde68a; }
  .qw-item.two   { background: var(--blue-light); border-color: var(--blue-mid); }
  .qw-item.three { background: #f0fdf4; border-color: #86efac; }
  .qw-item.four  { background: #f5f3ff; border-color: #c4b5fd; }
  .qw-item.five  { background: #fef2f2; border-color: #fecaca; }

  .qw-item .qw-num {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.06em;
    opacity: 0.6;
  }

  .qw-item .qw-icon { font-size: 26px; }

  .qw-item .qw-name {
    font-weight: 600;
    font-size: 12.5px;
    color: var(--text);
    line-height: 1.3;
    text-align: center;
  }

  .qw-item .qw-time {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--muted);
  }

  /* ── Big automation card ── */
  .auto-card {
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .auto-card .ac-header {
    padding: 14px 18px;
    display: flex;
    align-items: center;
    gap: 14px;
    border-bottom: 1px solid var(--border);
  }

  .auto-card.one   .ac-header { background: #fef3c7; border-color: #fde68a; }
  .auto-card.two   .ac-header { background: var(--blue-light); border-color: var(--blue-mid); }
  .auto-card.three .ac-header { background: #f0fdf4; border-color: #86efac; }
  .auto-card.four  .ac-header { background: #f5f3ff; border-color: #c4b5fd; }
  .auto-card.five  .ac-header { background: #fef2f2; border-color: #fecaca; }

  .auto-card .ac-num {
    font-family: 'DM Mono', monospace;
    font-size: 22px;
    font-weight: 700;
    opacity: 0.3;
    color: var(--text);
    line-height: 1;
    flex-shrink: 0;
  }

  .auto-card .ac-icon { font-size: 28px; flex-shrink: 0; }

  .auto-card .ac-title-wrap { flex: 1; }

  .auto-card .ac-title {
    font-weight: 700;
    font-size: 17px;
    color: var(--text);
  }

  .auto-card .ac-subtitle {
    font-size: 13px;
    color: var(--muted);
    margin-top: 2px;
  }

  .auto-card .ac-time {
    font-family: 'DM Mono', monospace;
    font-size: 11.5px;
    padding: 4px 12px;
    border-radius: 999px;
    flex-shrink: 0;
    font-weight: 500;
  }

  .auto-card.one   .ac-time { background: #fde68a; color: #78350f; }
  .auto-card.two   .ac-time { background: var(--blue-mid); color: #1e3a8a; }
  .auto-card.three .ac-time { background: #bbf7d0; color: #14532d; }
  .auto-card.four  .ac-time { background: #ddd6fe; color: #3b0764; }
  .auto-card.five  .ac-time { background: #fecaca; color: #7f1d1d; }

  .auto-card .ac-body {
    padding: 14px 18px;
    background: var(--white);
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 14px;
  }

  .ac-section { }

  .ac-section .acs-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--muted);
    margin-bottom: 5px;
  }

  .ac-section .acs-content {
    font-size: 13px;
    color: var(--text);
    line-height: 1.6;
  }

  /* ── Flow strip (mini) ── */
  .mini-flow {
    display: flex;
    align-items: center;
    gap: 5px;
    flex-wrap: wrap;
    margin-top: 4px;
  }

  .mf-node {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    padding: 3px 8px;
    border-radius: 4px;
    white-space: nowrap;
  }

  .mf-node.src { background: #f0fdf4; color: #166534; border: 1px solid #86efac; }
  .mf-node.ai  { background: #f5f3ff; color: #5b21b6; border: 1px solid #ddd6fe; }
  .mf-node.dst { background: var(--blue-light); color: #1e40af; border: 1px solid var(--blue-mid); }
  .mf-arr      { font-size: 11px; color: var(--muted); }

  /* ── Setup step cards ── */
  .setup-steps {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 14px;
  }

  .setup-step {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px 15px;
    display: flex;
    align-items: flex-start;
    gap: 11px;
  }

  .setup-step .ss-num {
    background: var(--blue);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 600;
    min-width: 24px;
    height: 24px;
    border-radius: 999px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-top: 1px;
  }

  .setup-step .ss-title {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
    margin-bottom: 3px;
  }

  .setup-step .ss-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.5;
  }

  /* ── Benefits table ── */
  .benefit-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
    gap: 10px;
    margin-top: 14px;
  }

  .benefit-col {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .benefit-col .bc-header {
    padding: 10px 10px 8px;
    text-align: center;
    border-bottom: 1px solid var(--border);
  }

  .benefit-col.one   .bc-header { background: #fef3c7; }
  .benefit-col.two   .bc-header { background: var(--blue-light); }
  .benefit-col.three .bc-header { background: #f0fdf4; }
  .benefit-col.four  .bc-header { background: #f5f3ff; }
  .benefit-col.five  .bc-header { background: #fef2f2; }

  .benefit-col .bc-icon { font-size: 20px; }
  .benefit-col .bc-name {
    font-weight: 600;
    font-size: 11.5px;
    color: var(--text);
    margin-top: 4px;
    text-align: center;
    line-height: 1.3;
  }

  .benefit-col .bc-items {
    padding: 10px 10px;
    background: var(--white);
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .benefit-col .bc-item {
    font-size: 11.5px;
    color: var(--muted);
    line-height: 1.4;
    display: flex;
    align-items: flex-start;
    gap: 5px;
  }

  .benefit-col .bc-item::before {
    content: '✓';
    font-size: 10px;
    color: var(--blue);
    flex-shrink: 0;
    margin-top: 1px;
    font-weight: 700;
  }

  /* ── Time saved summary ── */
  .time-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 8px;
    margin-top: 14px;
  }

  .time-card {
    border-radius: 10px;
    padding: 12px 10px;
    text-align: center;
    border: 1px solid var(--border);
    background: var(--white);
  }

  .time-card .tc-icon { font-size: 20px; margin-bottom: 4px; }

  .time-card .tc-name {
    font-size: 11px;
    font-weight: 600;
    color: var(--text);
    margin-bottom: 5px;
    line-height: 1.3;
  }

  .time-card .tc-time {
    font-family: 'DM Mono', monospace;
    font-size: 18px;
    font-weight: 700;
    color: var(--blue);
    line-height: 1;
  }

  .time-card .tc-unit {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--muted);
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

  .cheat-table .time {
    font-family: 'DM Mono', monospace;
    color: #059669;
    font-size: 12.5px;
    font-weight: 600;
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

# 5 AI Automations
## You Can Set Up Today

&nbsp;

**No code. No theory. Just five workflows that save real hours.** Pick one and build it today.

`Zapier` · `Make` · `ChatGPT` · `Claude` · `Gmail` · `Slack` · `Sheets`

---

## The Five — At a Glance

All five work with free or low-cost tools. Each takes under 30 minutes to set up.

<div class="quickwin-strip">
  <div class="qw-item one">
    <div class="qw-num">01</div>
    <div class="qw-icon">📧</div>
    <div class="qw-name">Email<br>Summariser</div>
    <div class="qw-time">~10 min setup</div>
  </div>
  <div class="qw-item two">
    <div class="qw-num">02</div>
    <div class="qw-icon">📝</div>
    <div class="qw-name">Meeting Notes<br>to Tasks</div>
    <div class="qw-time">~15 min setup</div>
  </div>
  <div class="qw-item three">
    <div class="qw-num">03</div>
    <div class="qw-icon">🐦</div>
    <div class="qw-name">Content<br>Repurposer</div>
    <div class="qw-time">~20 min setup</div>
  </div>
  <div class="qw-item four">
    <div class="qw-num">04</div>
    <div class="qw-icon">🧾</div>
    <div class="qw-name">Invoice<br>Data Extractor</div>
    <div class="qw-time">~25 min setup</div>
  </div>
  <div class="qw-item five">
    <div class="qw-num">05</div>
    <div class="qw-icon">🔔</div>
    <div class="qw-name">Daily News<br>Digest</div>
    <div class="qw-time">~15 min setup</div>
  </div>
</div>

<div class="tools" style="margin-top:14px;">
  <div class="tool-card">
    <div class="icon">🛠️</div>
    <div class="name">What you need</div>
    <div class="desc">A free Zapier or Make account. A free OpenAI or Claude API key. The apps you already use — Gmail, Slack, Notion, Google Sheets.</div>
  </div>
  <div class="tool-card">
    <div class="icon">⏱️</div>
    <div class="name">Time to first result</div>
    <div class="desc">The fastest automation (email summariser) sends your first AI-powered Slack message within 10 minutes of starting. Pick that one first.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">AUTOMATION 01</div>

<div class="auto-card one">
  <div class="ac-header">
    <div class="ac-num">01</div>
    <div class="ac-icon">📧</div>
    <div class="ac-title-wrap">
      <div class="ac-title">Email Summariser → Slack</div>
      <div class="ac-subtitle">Important emails land in Slack as 3-bullet summaries before you open them</div>
    </div>
    <div class="ac-time">~10 min</div>
  </div>
  <div class="ac-body">
    <div class="ac-section">
      <div class="acs-label">Flow</div>
      <div class="mini-flow">
        <span class="mf-node src">Gmail label</span><span class="mf-arr">→</span>
        <span class="mf-node ai">AI: summarise</span><span class="mf-arr">→</span>
        <span class="mf-node dst">Slack #inbox</span>
      </div>
      <div class="acs-content" style="margin-top:8px; font-size:12.5px;">Trigger: email with label <code>needs-summary</code>. AI prompt: "3 bullet points, be concise, no preamble." Output: Slack message with subject + bullets.</div>
    </div>
    <div class="ac-section">
      <div class="acs-label">AI Prompt</div>
      <div class="acs-content" style="font-family:'DM Mono',monospace; font-size:11.5px; color:#2563eb; line-height:1.8;">Summarise this email in exactly 3 bullet points. Be direct. No intro sentence.<br><br>{{Email Body}}</div>
    </div>
    <div class="ac-section">
      <div class="acs-label">Time saved</div>
      <div class="acs-content"><strong>~3 min/email.</strong> 10 emails a day = <strong>30 min/day</strong> back. 130+ hours/year. The first automation you should build.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">AUTOMATION 02</div>

<div class="auto-card two">
  <div class="ac-header">
    <div class="ac-num">02</div>
    <div class="ac-icon">📝</div>
    <div class="ac-title-wrap">
      <div class="ac-title">Meeting Notes → Tasks</div>
      <div class="ac-subtitle">Every meeting transcript becomes a list of tasks in your project tool — automatically</div>
    </div>
    <div class="ac-time">~15 min</div>
  </div>
  <div class="ac-body">
    <div class="ac-section">
      <div class="acs-label">Flow</div>
      <div class="mini-flow">
        <span class="mf-node src">Fireflies / Otter</span><span class="mf-arr">→</span>
        <span class="mf-node ai">AI: extract tasks</span><span class="mf-arr">→</span>
        <span class="mf-node dst">Notion / Linear</span>
      </div>
      <div class="acs-content" style="margin-top:8px; font-size:12.5px;">When a meeting transcript is ready, AI extracts action items with owner and deadline. Each item becomes a task. No manual note-taking required.</div>
    </div>
    <div class="ac-section">
      <div class="acs-label">AI Prompt</div>
      <div class="acs-content" style="font-family:'DM Mono',monospace; font-size:11.5px; color:#2563eb; line-height:1.8;">Extract all action items from this transcript. Return JSON array. Each item: {"task": str, "owner": str, "due": str or null}.<br><br>{{Transcript}}</div>
    </div>
    <div class="ac-section">
      <div class="acs-label">Time saved</div>
      <div class="acs-content"><strong>~20 min/meeting.</strong> 5 meetings a week = <strong>100 min/week</strong> back. No missed follow-ups. Tasks exist before you leave the call.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">AUTOMATION 03</div>

<div class="auto-card three">
  <div class="ac-header">
    <div class="ac-num">03</div>
    <div class="ac-icon">🐦</div>
    <div class="ac-title-wrap">
      <div class="ac-title">Blog Post → Social Content</div>
      <div class="ac-subtitle">Every post you publish becomes a tweet thread + LinkedIn post automatically</div>
    </div>
    <div class="ac-time">~20 min</div>
  </div>
  <div class="ac-body">
    <div class="ac-section">
      <div class="acs-label">Flow</div>
      <div class="mini-flow">
        <span class="mf-node src">Notion / WordPress</span><span class="mf-arr">→</span>
        <span class="mf-node ai">AI: rewrite for platform</span><span class="mf-arr">→</span>
        <span class="mf-node dst">Buffer / Hypefury</span>
      </div>
      <div class="acs-content" style="margin-top:8px; font-size:12.5px;">Trigger: new post published or moved to "Published" status. Two AI calls — one for X/Twitter, one for LinkedIn. Both scheduled in Buffer for review.</div>
    </div>
    <div class="ac-section">
      <div class="acs-label">AI Prompt</div>
      <div class="acs-content" style="font-family:'DM Mono',monospace; font-size:11.5px; color:#2563eb; line-height:1.8;">Rewrite this blog post as a 5-tweet thread. Hook tweet first. Each tweet under 280 chars. Conversational tone. No hashtag spam.<br><br>{{Post Body}}</div>
    </div>
    <div class="ac-section">
      <div class="acs-label">Time saved</div>
      <div class="acs-content"><strong>~45 min/post.</strong> 4 posts a month = <strong>3 hours/month</strong> back. Your content reaches more channels without writing anything twice.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">AUTOMATION 04</div>

<div class="auto-card four">
  <div class="ac-header">
    <div class="ac-num">04</div>
    <div class="ac-icon">🧾</div>
    <div class="ac-title-wrap">
      <div class="ac-title">Invoice → Spreadsheet Row</div>
      <div class="ac-subtitle">PDFs emailed to you are parsed and logged in Google Sheets without touching them</div>
    </div>
    <div class="ac-time">~25 min</div>
  </div>
  <div class="ac-body">
    <div class="ac-section">
      <div class="acs-label">Flow</div>
      <div class="mini-flow">
        <span class="mf-node src">Gmail: PDF attach</span><span class="mf-arr">→</span>
        <span class="mf-node ai">AI: extract fields</span><span class="mf-arr">→</span>
        <span class="mf-node dst">Google Sheets row</span>
      </div>
      <div class="acs-content" style="margin-top:8px; font-size:12.5px;">Trigger: email with PDF attachment matching "invoice" subject filter. AI reads the PDF text and extracts structured data. Row added to Sheets instantly.</div>
    </div>
    <div class="ac-section">
      <div class="acs-label">AI Prompt</div>
      <div class="acs-content" style="font-family:'DM Mono',monospace; font-size:11.5px; color:#2563eb; line-height:1.8;">Extract from this invoice. Return JSON: {"vendor": str, "amount": number, "currency": str, "date": str, "due_date": str, "invoice_no": str}.<br><br>{{PDF Text}}</div>
    </div>
    <div class="ac-section">
      <div class="acs-label">Time saved</div>
      <div class="acs-content"><strong>~8 min/invoice.</strong> 20 invoices a month = <strong>2.5 hours/month</strong> back. Zero manual data entry. No transcription errors.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">AUTOMATION 05</div>

<div class="auto-card five">
  <div class="ac-header">
    <div class="ac-num">05</div>
    <div class="ac-icon">🔔</div>
    <div class="ac-title-wrap">
      <div class="ac-title">Daily News Digest</div>
      <div class="ac-subtitle">AI reads your RSS feeds every morning and emails you the 5 most relevant stories</div>
    </div>
    <div class="ac-time">~15 min</div>
  </div>
  <div class="ac-body">
    <div class="ac-section">
      <div class="acs-label">Flow</div>
      <div class="mini-flow">
        <span class="mf-node src">Schedule: 7 AM</span><span class="mf-arr">→</span>
        <span class="mf-node ai">AI: curate + summarise</span><span class="mf-arr">→</span>
        <span class="mf-node dst">Email digest</span>
      </div>
      <div class="acs-content" style="margin-top:8px; font-size:12.5px;">Runs every morning at 7 AM. Pulls from your RSS feeds, AI picks the 5 most relevant, writes a 2-sentence summary of each, sends before your first meeting.</div>
    </div>
    <div class="ac-section">
      <div class="acs-label">AI Prompt</div>
      <div class="acs-content" style="font-family:'DM Mono',monospace; font-size:11.5px; color:#2563eb; line-height:1.8;">From these headlines, pick the 5 most relevant to [your industry]. Write 2 sentences per story. Plain text, no markdown. Today's date: {{Date}}.<br><br>{{RSS Headlines}}</div>
    </div>
    <div class="ac-section">
      <div class="acs-label">Time saved</div>
      <div class="acs-content"><strong>~25 min/day</strong> not scanning news. You get signal, not noise. Relevant stories only. Delivered before you even open your laptop.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">SETUP OVERVIEW</div>

## How to Set Any of These Up

The same six steps work for all five automations.

<div class="setup-steps">
  <div class="setup-step">
    <div class="ss-num">1</div>
    <div>
      <div class="ss-title">Create a free Zapier account</div>
      <div class="ss-desc">Go to zapier.com. Free tier covers all five of these automations. No credit card needed to start.</div>
    </div>
  </div>
  <div class="setup-step">
    <div class="ss-num">2</div>
    <div>
      <div class="ss-title">Get an AI API key</div>
      <div class="ss-desc">OpenAI (platform.openai.com) or Claude (console.anthropic.com). Both have free tiers or cheap pay-per-use pricing — these automations cost cents per run.</div>
    </div>
  </div>
  <div class="setup-step">
    <div class="ss-num">3</div>
    <div>
      <div class="ss-title">Create a new Zap</div>
      <div class="ss-desc">Click "Create" → search for your trigger app (Gmail, Notion, Schedule) → choose the trigger event → connect your account.</div>
    </div>
  </div>
  <div class="setup-step">
    <div class="ss-num">4</div>
    <div>
      <div class="ss-title">Add a ChatGPT / Claude step</div>
      <div class="ss-desc">Search "ChatGPT" or "Claude AI" as an action. Select "Send Message." Paste the prompt from the slide above. Reference trigger data with <code>{{placeholders}}</code>.</div>
    </div>
  </div>
  <div class="setup-step">
    <div class="ss-num">5</div>
    <div>
      <div class="ss-title">Add the output action</div>
      <div class="ss-desc">Add Slack, Google Sheets, Notion, Buffer, or Email as the final step. Map the AI response into the right fields.</div>
    </div>
  </div>
  <div class="setup-step">
    <div class="ss-num">6</div>
    <div>
      <div class="ss-title">Test → Enable → Forget</div>
      <div class="ss-desc">Click "Test step" on each part. If the output looks right, hit "Publish." You never need to touch it again unless the API changes.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">BENEFITS</div>

## What Each Automation Gives You

<div class="benefit-grid">
  <div class="benefit-col one">
    <div class="bc-header">
      <div class="bc-icon">📧</div>
      <div class="bc-name">Email Summariser</div>
    </div>
    <div class="bc-items">
      <div class="bc-item">Inbox zero becomes realistic</div>
      <div class="bc-item">Never miss a key ask buried in prose</div>
      <div class="bc-item">Async teams stay in sync via Slack</div>
      <div class="bc-item">30 min/day reclaimed</div>
    </div>
  </div>
  <div class="benefit-col two">
    <div class="bc-header">
      <div class="bc-icon">📝</div>
      <div class="bc-name">Meeting→ Tasks</div>
    </div>
    <div class="bc-items">
      <div class="bc-item">Zero missed action items</div>
      <div class="bc-item">Tasks exist before you leave the call</div>
      <div class="bc-item">Accountability is automatic</div>
      <div class="bc-item">No post-meeting admin</div>
    </div>
  </div>
  <div class="benefit-col three">
    <div class="bc-header">
      <div class="bc-icon">🐦</div>
      <div class="bc-name">Content Repurposer</div>
    </div>
    <div class="bc-items">
      <div class="bc-item">Write once, publish everywhere</div>
      <div class="bc-item">Consistent posting without effort</div>
      <div class="bc-item">Grows audience on autopilot</div>
      <div class="bc-item">3 hrs/month back</div>
    </div>
  </div>
  <div class="benefit-col four">
    <div class="bc-header">
      <div class="bc-icon">🧾</div>
      <div class="bc-name">Invoice Extractor</div>
    </div>
    <div class="bc-items">
      <div class="bc-item">Zero manual data entry</div>
      <div class="bc-item">No transcription errors</div>
      <div class="bc-item">Real-time spend visibility</div>
      <div class="bc-item">Scales to any volume</div>
    </div>
  </div>
  <div class="benefit-col five">
    <div class="bc-header">
      <div class="bc-icon">🔔</div>
      <div class="bc-name">News Digest</div>
    </div>
    <div class="bc-items">
      <div class="bc-item">Signal only — no noise</div>
      <div class="bc-item">Stay informed in 5 min</div>
      <div class="bc-item">Relevant to your industry</div>
      <div class="bc-item">25 min/day reclaimed</div>
    </div>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**Combined time saving: 4–6 hours per week.** That's 200+ hours per year from five automations that each took under 30 minutes to set up. The compounding math is hard to ignore.

</div>

---

## All Five — Quick Reference

<table class="cheat-table">
  <tr>
    <th>#</th>
    <th>Automation</th>
    <th>Trigger</th>
    <th>AI Job</th>
    <th>Setup</th>
    <th>Saves</th>
  </tr>
  <tr>
    <td>01</td>
    <td>Email Summariser</td>
    <td>Gmail label</td>
    <td>3-bullet summary</td>
    <td class="mono">~10 min</td>
    <td class="time">30 min/day</td>
  </tr>
  <tr>
    <td>02</td>
    <td>Meeting → Tasks</td>
    <td>Transcript ready</td>
    <td>Extract action items as JSON</td>
    <td class="mono">~15 min</td>
    <td class="time">20 min/meeting</td>
  </tr>
  <tr>
    <td>03</td>
    <td>Blog → Social</td>
    <td>Post published</td>
    <td>Rewrite for X + LinkedIn</td>
    <td class="mono">~20 min</td>
    <td class="time">45 min/post</td>
  </tr>
  <tr>
    <td>04</td>
    <td>Invoice Extractor</td>
    <td>PDF email</td>
    <td>Extract vendor, amount, date</td>
    <td class="mono">~25 min</td>
    <td class="time">8 min/invoice</td>
  </tr>
  <tr>
    <td>05</td>
    <td>News Digest</td>
    <td>Schedule 7 AM</td>
    <td>Curate + summarise RSS</td>
    <td class="mono">~15 min</td>
    <td class="time">25 min/day</td>
  </tr>
</table>

<div class="highlight" style="margin-top:14px;">

**Start with #01.** It takes 10 minutes, delivers immediate value, and teaches you the exact pattern every other automation uses. Once #01 works, the other four take half the time.

</div>

---

<!-- _class: final -->

# Pick one.
# Build it today.
# Come back for the next.

&nbsp;

Start with the email summariser. Everything else follows the same pattern.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*