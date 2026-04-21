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

  .warning {
    background: #fef2f2;
    border: 1px solid #fecaca;
    border-radius: 10px;
    padding: 18px 24px;
    margin: 16px 0;
  }

  .warning p { color: #991b1b; }
  .warning strong { color: #7f1d1d; }

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

  .step-badge.danger {
    background: #dc2626;
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

  .cb-kw     { color: #c084fc; }
  .cb-fn     { color: #60a5fa; }
  .cb-str    { color: #fde68a; }
  .cb-num    { color: #fb923c; }
  .cb-cmt    { color: #4b5563; font-style: italic; }
  .cb-var    { color: #f9fafb; }
  .cb-prop   { color: #34d399; }
  .cb-op     { color: #6b7280; }
  .cb-out    { color: #9ca3af; }
  .cb-prompt { color: #22c55e; }
  .cb-cmd    { color: #f9fafb; }
  .cb-hi     { color: #34d399; }
  .cb-bad    { color: #f87171; }
  .cb-env    { color: #fb923c; }

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

  /* ── Gmail setup steps ── */
  .gmail-steps {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 11px;
    margin-top: 14px;
  }

  .gmail-step {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }

  .gmail-step .gs-num {
    background: #dc2626;
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

  .gmail-step .gs-title {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
    margin-bottom: 3px;
  }

  .gmail-step .gs-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.5;
  }

  /* ── Email preview mock ── */
  .email-mock {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
    margin: 14px 0;
  }

  .email-mock .em-header {
    background: var(--off-white);
    padding: 14px 18px;
    border-bottom: 1px solid var(--border);
  }

  .email-mock .em-field {
    display: flex;
    gap: 10px;
    margin-bottom: 6px;
    font-size: 13px;
    align-items: baseline;
  }

  .email-mock .em-field:last-child { margin-bottom: 0; }

  .email-mock .em-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    min-width: 50px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    padding-top: 1px;
  }

  .email-mock .em-value {
    font-size: 13px;
    color: var(--text);
  }

  .email-mock .em-subject {
    font-weight: 600;
    color: var(--text);
  }

  .email-mock .em-body {
    padding: 16px 18px;
    font-size: 13.5px;
    color: var(--text);
    line-height: 1.7;
  }

  .email-mock .em-dynamic {
    background: #fef3c7;
    border-radius: 4px;
    padding: 1px 6px;
    font-family: 'DM Mono', monospace;
    font-size: 11.5px;
    color: #92400e;
  }

  /* ── Security do/don't comparison ── */
  .sec-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 14px;
  }

  .sec-col .sc-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    padding: 7px 14px;
    border-radius: 8px 8px 0 0;
  }

  .sec-col.bad  .sc-label { background: #fef2f2; color: #991b1b; border: 1px solid #fecaca; border-bottom: none; }
  .sec-col.good .sc-label { background: #f0fdf4; color: #166534; border: 1px solid #bbf7d0; border-bottom: none; }

  .sec-col .sc-body {
    border-radius: 0 0 8px 8px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .sec-col.bad  .sc-body { border: 1px solid #fecaca; border-top: none; }
  .sec-col.good .sc-body { border: 1px solid #bbf7d0; border-top: none; }

  /* ── smtplib flow ── */
  .flow-row {
    display: flex;
    align-items: center;
    gap: 0;
    margin: 18px 0;
    justify-content: center;
  }

  .flow-node {
    background: var(--white);
    border: 2px solid var(--border);
    border-radius: 10px;
    padding: 12px 16px;
    text-align: center;
    min-width: 110px;
  }

  .flow-node .fn-icon  { font-size: 22px; margin-bottom: 4px; }
  .flow-node .fn-label { font-weight: 600; font-size: 13px; color: var(--text); }
  .flow-node .fn-sub   { font-family: 'DM Mono', monospace; font-size: 10.5px; color: var(--muted); margin-top: 2px; }

  .flow-node.blue {
    background: var(--blue);
    border-color: var(--blue);
  }
  .flow-node.blue .fn-label { color: white; }
  .flow-node.blue .fn-sub   { color: #bfdbfe; }

  .flow-arrow {
    padding: 0 8px;
    color: var(--blue);
    font-size: 20px;
    flex-shrink: 0;
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

  .cheat-table .danger {
    font-family: 'DM Mono', monospace;
    color: #dc2626;
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

# Send Automated Email
## with Python

&nbsp;

**Your script can email you while you sleep.** Here's the whole thing.

`smtplib` · `MIMEText` · `app password` · `.env` · `schedule`

---

## Use Cases — When This Is Useful

Once Python can send email, a whole category of automation opens up.

<div class="tools">
  <div class="tool-card">
    <div class="icon">📊</div>
    <div class="name">Daily reports</div>
    <div class="desc">Run a script at 8 AM that pulls data, formats a summary, and emails it to you before you start work. Zero manual steps.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔔</div>
    <div class="name">Alerts & notifications</div>
    <div class="desc">Email yourself the moment a price drops, a server goes down, a file appears, or an API returns an error. Instant awareness.</div>
  </div>
  <div class="tool-card">
    <div class="icon">⏰</div>
    <div class="name">Reminders</div>
    <div class="desc">Weekly task lists, birthday reminders, subscription renewal warnings. A cron job + 10 lines of Python replaces any reminder app.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🗃️</div>
    <div class="name">Backup confirmations</div>
    <div class="desc">After a backup script runs, email yourself a confirmation with the file count, size, and any errors — so you know it actually worked.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## How `smtplib` Works

Python's built-in `smtplib` library handles the full email sending process. Nothing to install.

<div class="flow-row">
  <div class="flow-node">
    <div class="fn-icon">🐍</div>
    <div class="fn-label">Your Script</div>
    <div class="fn-sub">smtplib</div>
  </div>
  <div class="flow-arrow">→</div>
  <div class="flow-node blue">
    <div class="fn-icon" style="color:white;">🔒</div>
    <div class="fn-label">SMTP + TLS</div>
    <div class="fn-sub">port 587</div>
  </div>
  <div class="flow-arrow">→</div>
  <div class="flow-node">
    <div class="fn-icon">📬</div>
    <div class="fn-label">Gmail Server</div>
    <div class="fn-sub">smtp.gmail.com</div>
  </div>
  <div class="flow-arrow">→</div>
  <div class="flow-node">
    <div class="fn-icon">📥</div>
    <div class="fn-label">Recipient</div>
    <div class="fn-sub">inbox</div>
  </div>
</div>

<div class="tools" style="margin-top:4px;">
  <div class="tool-card">
    <div class="icon">📦</div>
    <div class="name">Built into Python</div>
    <div class="desc"><code>smtplib</code> and <code>email</code> are part of the standard library. No <code>pip install</code> needed — just import and use.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔐</div>
    <div class="name">TLS encryption</div>
    <div class="desc">Always use <code>SMTP_SSL</code> or <code>starttls()</code>. Never send credentials over a plain unencrypted connection.</div>
  </div>
  <div class="tool-card">
    <div class="icon">📧</div>
    <div class="name">Works with any provider</div>
    <div class="desc">Gmail, Outlook, Yahoo, custom SMTP — just swap the host and port. This tutorial uses Gmail since it's most common.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔑</div>
    <div class="name">App password required</div>
    <div class="desc">Gmail blocks your main password from scripts. You generate a special 16-character app password — it only works for this one script.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Gmail App Password Setup

Google blocks regular password login from scripts. An app password is a 16-character code that bypasses this — safely.

<div class="gmail-steps">
  <div class="gmail-step">
    <div class="gs-num">1</div>
    <div>
      <div class="gs-title">Enable 2-Step Verification</div>
      <div class="gs-desc">Go to <strong>myaccount.google.com → Security</strong>. Turn on 2-Step Verification if it's not already on. App passwords require it.</div>
    </div>
  </div>
  <div class="gmail-step">
    <div class="gs-num">2</div>
    <div>
      <div class="gs-title">Go to App Passwords</div>
      <div class="gs-desc">Search "App Passwords" in your Google Account search bar, or go to <strong>myaccount.google.com/apppasswords</strong> directly.</div>
    </div>
  </div>
  <div class="gmail-step">
    <div class="gs-num">3</div>
    <div>
      <div class="gs-title">Create a new app password</div>
      <div class="gs-desc">In the "App name" field type something like <strong>Python Mailer</strong>. Click Create. Google generates a 16-character password.</div>
    </div>
  </div>
  <div class="gmail-step">
    <div class="gs-num">4</div>
    <div>
      <div class="gs-title">Copy it immediately</div>
      <div class="gs-desc">Google shows it <strong>once only</strong>. Copy the 16-character code now and paste it into your <code>.env</code> file. You cannot retrieve it again.</div>
    </div>
  </div>
  <div class="gmail-step">
    <div class="gs-num">5</div>
    <div>
      <div class="gs-title">Store it as an env variable</div>
      <div class="gs-desc">Never paste it directly into your script. Put it in a <code>.env</code> file and load it with <code>python-dotenv</code>. Details on the safety slide.</div>
    </div>
  </div>
  <div class="gmail-step">
    <div class="gs-num">6</div>
    <div>
      <div class="gs-title">Revoke anytime</div>
      <div class="gs-desc">If the password leaks, go back to App Passwords and delete it. The script breaks immediately — your main account stays safe.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## The 10-Line Script

<div class="code-block">
  <div class="cb-bar">send_email.py — complete working script</div>
  <div class="cb-body">
    <span class="cb-kw">import</span> <span class="cb-var">smtplib</span><br>
    <span class="cb-kw">from</span> <span class="cb-var">email.mime.text</span> <span class="cb-kw">import</span> <span class="cb-var">MIMEText</span><br>
    <br>
    <span class="cb-var">sender</span>   <span class="cb-op">=</span> <span class="cb-str">"you@gmail.com"</span><br>
    <span class="cb-var">receiver</span> <span class="cb-op">=</span> <span class="cb-str">"friend@example.com"</span><br>
    <span class="cb-var">password</span> <span class="cb-op">=</span> <span class="cb-str">"xxxx xxxx xxxx xxxx"</span>  <span class="cb-cmt"># app password — see safety slide</span><br>
    <br>
    <span class="cb-var">msg</span> <span class="cb-op">=</span> <span class="cb-fn">MIMEText</span><span class="cb-op">(</span><span class="cb-str">"Hello from Python!"</span><span class="cb-op">)</span><br>
    <span class="cb-var">msg</span><span class="cb-op">[</span><span class="cb-str">"Subject"</span><span class="cb-op">]</span> <span class="cb-op">=</span> <span class="cb-str">"Automated message"</span><br>
    <span class="cb-var">msg</span><span class="cb-op">[</span><span class="cb-str">"From"</span><span class="cb-op">]</span>    <span class="cb-op">=</span> <span class="cb-var">sender</span><br>
    <span class="cb-var">msg</span><span class="cb-op">[</span><span class="cb-str">"To"</span><span class="cb-op">]</span>      <span class="cb-op">=</span> <span class="cb-var">receiver</span><br>
    <br>
    <span class="cb-kw">with</span> <span class="cb-var">smtplib</span><span class="cb-op">.</span><span class="cb-fn">SMTP_SSL</span><span class="cb-op">(</span><span class="cb-str">"smtp.gmail.com"</span><span class="cb-op">,</span> <span class="cb-num">465</span><span class="cb-op">)</span> <span class="cb-kw">as</span> <span class="cb-var">smtp</span><span class="cb-op">:</span><br>
    &nbsp;&nbsp;<span class="cb-var">smtp</span><span class="cb-op">.</span><span class="cb-fn">login</span><span class="cb-op">(</span><span class="cb-var">sender</span><span class="cb-op">,</span> <span class="cb-var">password</span><span class="cb-op">)</span><br>
    &nbsp;&nbsp;<span class="cb-var">smtp</span><span class="cb-op">.</span><span class="cb-fn">sendmail</span><span class="cb-op">(</span><span class="cb-var">sender</span><span class="cb-op">,</span> <span class="cb-var">receiver</span><span class="cb-op">,</span> <span class="cb-var">msg</span><span class="cb-op">.</span><span class="cb-fn">as_string</span><span class="cb-op">())</span><br>
    <br>
    <span class="cb-fn">print</span><span class="cb-op">(</span><span class="cb-str">"Email sent."</span><span class="cb-op">)</span>
  </div>
</div>

<div class="highlight">

**Run it:** `python send_email.py` — if your app password is correct you'll see `Email sent.` and the message arrives within seconds. That's the whole thing.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 03 — part 1 of 2</div>

## Add a Dynamic Subject and Body

Hard-coded messages aren't useful. Pull in real data with f-strings.

<div class="code-block">
  <div class="cb-bar">daily_report.py — dynamic content</div>
  <div class="cb-body">
    <span class="cb-kw">import</span> <span class="cb-var">smtplib</span><span class="cb-op">,</span> <span class="cb-var">datetime</span><br>
    <span class="cb-kw">from</span> <span class="cb-var">email.mime.text</span> <span class="cb-kw">import</span> <span class="cb-var">MIMEText</span><br>
    <span class="cb-cmt"># Gather data — swap these for your own functions</span><br>
    <span class="cb-var">today</span>      <span class="cb-op">=</span> <span class="cb-var">datetime</span><span class="cb-op">.</span><span class="cb-var">date</span><span class="cb-op">.</span><span class="cb-fn">today</span><span class="cb-op">()</span><span class="cb-op">.</span><span class="cb-fn">strftime</span><span class="cb-op">(</span><span class="cb-str">"%b %d, %Y"</span><span class="cb-op">)</span><br>
    <span class="cb-var">temp</span>       <span class="cb-op">=</span> <span class="cb-fn">get_temperature</span><span class="cb-op">()</span>   <span class="cb-cmt"># your function here</span><br>
    <span class="cb-var">task_count</span> <span class="cb-op">=</span> <span class="cb-fn">count_open_tasks</span><span class="cb-op">()</span>  <span class="cb-cmt"># your function here</span><br>
    <span class="cb-cmt"># Build subject and body using f-strings</span><br>
    <span class="cb-var">subject</span> <span class="cb-op">=</span> <span class="cb-str">f"Daily Report — </span><span class="cb-op">{</span><span class="cb-var">today</span><span class="cb-op">}</span><span class="cb-str">"</span><br>
    <span class="cb-var">body</span>    <span class="cb-op">=</span> <span class="cb-str">f"""Good morning,</span><br>
    <span class="cb-str">Here's your summary for </span><span class="cb-op">{</span><span class="cb-var">today</span><span class="cb-op">}</span><span class="cb-str">:</span><br>
    <span class="cb-str">  • Temperature  : </span><span class="cb-op">{</span><span class="cb-var">temp</span><span class="cb-op">}</span><span class="cb-str">°C</span><br>
    <span class="cb-str">  • Open tasks   : </span><span class="cb-op">{</span><span class="cb-var">task_count</span><span class="cb-op">}</span><br>
    <span class="cb-str">"""</span><br>
    <span class="cb-cmt"># Attach subject and body to the message object</span><br>
    <span class="cb-var">msg</span>             <span class="cb-op">=</span> <span class="cb-fn">MIMEText</span><span class="cb-op">(</span><span class="cb-var">body</span><span class="cb-op">)</span><br>
    <span class="cb-var">msg</span><span class="cb-op">[</span><span class="cb-str">"Subject"</span><span class="cb-op">]</span> <span class="cb-op">=</span> <span class="cb-var">subject</span><br>
    <span class="cb-var">msg</span><span class="cb-op">[</span><span class="cb-str">"From"</span><span class="cb-op">]</span>    <span class="cb-op">=</span> <span class="cb-var">sender</span><br>
    <span class="cb-var">msg</span><span class="cb-op">[</span><span class="cb-str">"To"</span><span class="cb-op">]</span>      <span class="cb-op">=</span> <span class="cb-var">receiver</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 03 — part 2 of 2</div>

## What the Email Looks Like

The amber highlights show which parts of the email are filled in dynamically by Python at send time.

<div class="email-mock">
  <div class="em-header">
    <div class="em-field"><span class="em-label">From</span><span class="em-value">you@gmail.com</span></div>
    <div class="em-field"><span class="em-label">To</span><span class="em-value">friend@example.com</span></div>
    <div class="em-field"><span class="em-label">Subject</span><span class="em-value em-subject">Daily Report — <span class="em-dynamic">Apr 18, 2026</span></span></div>
  </div>
  <div class="em-body">
    Good morning,<br><br>
    Here's your summary for <span class="em-dynamic">Apr 18, 2026</span>:<br><br>
    &nbsp;&nbsp;• Temperature &nbsp;: <span class="em-dynamic">28°C</span><br>
    &nbsp;&nbsp;• Open tasks &nbsp;&nbsp;: <span class="em-dynamic">4</span>
  </div>
</div>

<div class="two-col" style="margin-top:14px;">
  <div class="col-card">
    <div class="label">🟡 &nbsp;Dynamic values</div>
    <p style="font-size:13.5px; margin-top:6px;">The amber fields — date, temperature, task count — are interpolated by Python at run time. Change the data source and the email updates automatically.</p>
  </div>
  <div class="col-card">
    <div class="label">Going further</div>
    <p style="font-size:13.5px; margin-top:6px;">Swap <code>MIMEText(body)</code> for <code>MIMEText(body, "html")</code> to send a fully styled HTML email with headings, colors, and tables instead of plain text.</p>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 04</div>

## Schedule It to Run Daily

Combine with cron (Mac) or Task Scheduler (Windows) from the previous tutorial.

<div class="two-col">
  <div class="col-card">
    <div class="label">🍎 &nbsp;Mac — crontab</div>
    <div class="code-block" style="margin-top:10px;">
      <div class="cb-body" style="padding:10px 14px; line-height:1.9; font-size:12px;">
        <span class="cb-cmt"># Runs every day at 8:00 AM</span><br>
        <span class="cb-hi">0 8 * * *</span> <span class="cb-var">/usr/local/bin/python3</span><br>
        <span class="cb-var">/Users/you/daily_report.py</span><br>
        <span class="cb-op">>> /Users/you/logs/email.log 2>&1</span>
      </div>
    </div>
  </div>
  <div class="col-card">
    <div class="label">🪟 &nbsp;Windows — Task Scheduler</div>
    <p style="font-size:13px; margin-top:10px; color:var(--muted);">Open Task Scheduler → Create Basic Task → Trigger: Daily at 08:00 → Action: Start a Program → Program: full path to <code>python.exe</code> → Arguments: full path to <code>daily_report.py</code></p>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**From the previous tutorial:** The scheduling slide covers cron syntax and Task Scheduler step-by-step. The only addition here is making sure your <code>.env</code> file path is absolute in the script — cron runs without your home directory in scope.

</div>

---

<!-- _class: step -->

<div class="step-badge danger">⚠ SAFETY WARNING</div>

## Never Hardcode Passwords

Pasting your app password directly into the script is the most common beginner mistake. One accidental commit to GitHub and it's exposed.

<div class="sec-grid">
  <div class="sec-col bad">
    <div class="sc-label">❌ &nbsp;Never do this</div>
    <div class="sc-body">
      <div class="code-block" style="margin:0; border-radius:0;">
        <div class="cb-body" style="padding:12px 16px; line-height:1.9; font-size:12px;">
          <span class="cb-cmt"># Hardcoded — dangerous</span><br>
          <span class="cb-var">password</span> <span class="cb-op">=</span> <span class="cb-bad">"abcd efgh ijkl mnop"</span><br>
          <span class="cb-cmt"># One git push = leaked forever</span>
        </div>
      </div>
    </div>
  </div>
  <div class="sec-col good">
    <div class="sc-label">✅ &nbsp;Do this instead</div>
    <div class="sc-body">
      <div class="code-block" style="margin:0; border-radius:0;">
        <div class="cb-body" style="padding:12px 16px; line-height:1.9; font-size:12px;">
          <span class="cb-kw">import</span> <span class="cb-var">os</span><br>
          <span class="cb-kw">from</span> <span class="cb-var">dotenv</span> <span class="cb-kw">import</span> <span class="cb-fn">load_dotenv</span><br>
          <span class="cb-fn">load_dotenv</span><span class="cb-op">()</span><br>
          <span class="cb-var">password</span> <span class="cb-op">=</span> <span class="cb-var">os</span><span class="cb-op">.</span><span class="cb-fn">getenv</span><span class="cb-op">(</span><span class="cb-str">"GMAIL_APP_PW"</span><span class="cb-op">)</span>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="code-block" style="margin-top:14px;">
  <div class="cb-bar">.env — lives in project root, NEVER committed to git</div>
  <div class="cb-body" style="padding:10px 20px; line-height:1.9;">
    <span class="cb-env">GMAIL_SENDER</span><span class="cb-op">=</span><span class="cb-str">you@gmail.com</span><br>
    <span class="cb-env">GMAIL_APP_PW</span><span class="cb-op">=</span><span class="cb-str">abcd efgh ijkl mnop</span><br>
    <span class="cb-env">GMAIL_RECEIVER</span><span class="cb-op">=</span><span class="cb-str">friend@example.com</span>
  </div>
</div>

<div class="warning">

<strong>Add .env to .gitignore immediately.</strong> Run `echo ".env" >> .gitignore` before your first commit. If you've already committed it, rotate the app password right now — treat it as compromised.

</div>

---

## Python Email Quick Reference

<table class="cheat-table">
  <tr>
    <th>Task</th>
    <th>Code / Notes</th>
  </tr>
  <tr>
    <td>Import libraries</td>
    <td class="mono">import smtplib &nbsp;·&nbsp; from email.mime.text import MIMEText</td>
  </tr>
  <tr>
    <td>Connect to Gmail</td>
    <td class="mono">smtplib.SMTP_SSL("smtp.gmail.com", 465)</td>
  </tr>
  <tr>
    <td>Login</td>
    <td class="mono">smtp.login(sender, app_password)</td>
  </tr>
  <tr>
    <td>Build the message</td>
    <td class="mono">msg = MIMEText(body) &nbsp;·&nbsp; msg["Subject"] = "..."</td>
  </tr>
  <tr>
    <td>Send it</td>
    <td class="mono">smtp.sendmail(sender, receiver, msg.as_string())</td>
  </tr>
  <tr>
    <td>Get app password</td>
    <td>myaccount.google.com/apppasswords — requires 2FA enabled</td>
  </tr>
  <tr>
    <td>Store credentials safely</td>
    <td class="mono">python-dotenv + os.getenv() — never hardcode</td>
  </tr>
  <tr>
    <td>Add .env to .gitignore</td>
    <td class="danger">echo ".env" >> .gitignore — do this before first commit</td>
  </tr>
  <tr>
    <td>Send HTML email</td>
    <td class="mono">MIMEText(html_string, "html") — second arg sets type</td>
  </tr>
  <tr>
    <td>Other providers</td>
    <td>Outlook: smtp-mail.outlook.com:587 &nbsp;·&nbsp; Yahoo: smtp.mail.yahoo.com:465</td>
  </tr>
</table>

---

<!-- _class: final -->

# Python just became
# your personal assistant.

&nbsp;

smtplib. App password. .env file. Cron job. Done.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*