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
  .cb-wprompt{ color: #60a5fa; }
  .cb-cmd    { color: #f9fafb; }
  .cb-hi     { color: #34d399; }  /* highlighted important value */
  .cb-field  { color: #fb923c; }  /* cron field values */

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

  /* ── Platform split ── */
  .platform-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 16px;
  }

  .platform-card {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .platform-card .platform-header {
    padding: 10px 16px;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    letter-spacing: 0.06em;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .platform-card.mac .platform-header {
    background: #1f2937;
    color: #9ca3af;
  }

  .platform-card.win .platform-header {
    background: #1e3a5f;
    color: #93c5fd;
  }

  .platform-card .platform-body {
    background: #111827;
    padding: 14px 18px;
    font-family: 'DM Mono', monospace;
    font-size: 12.5px;
    line-height: 2;
  }

  .platform-card .platform-body .prompt  { color: #22c55e; }
  .platform-card .platform-body .wprompt { color: #60a5fa; }
  .platform-card .platform-body .cmd     { color: #f9fafb; }
  .platform-card .platform-body .out     { color: #9ca3af; }
  .platform-card .platform-body .cmt     { color: #4b5563; font-style: italic; }

  /* ── Cron anatomy ── */
  .cron-anatomy {
    background: #111827;
    border-radius: 10px;
    overflow: hidden;
    margin: 16px 0;
  }

  .cron-anatomy .ca-bar {
    background: #1f2937;
    padding: 8px 16px;
    font-family: 'DM Mono', monospace;
    font-size: 11.5px;
    color: #6b7280;
    letter-spacing: 0.04em;
  }

  .cron-anatomy .ca-expr {
    padding: 18px 24px 6px;
    font-family: 'DM Mono', monospace;
    font-size: 22px;
    letter-spacing: 0.04em;
    display: flex;
    gap: 18px;
    align-items: baseline;
  }

  .ca-f1 { color: #f87171; }
  .ca-f2 { color: #fb923c; }
  .ca-f3 { color: #fde68a; }
  .ca-f4 { color: #34d399; }
  .ca-f5 { color: #93c5fd; }
  .ca-cmd-text { color: #c084fc; font-size: 18px; }

  .cron-anatomy .ca-labels {
    display: flex;
    gap: 18px;
    padding: 4px 24px 18px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
  }

  .ca-lbl {
    display: flex;
    flex-direction: column;
    gap: 3px;
    min-width: 24px;
  }

  .ca-lbl .ca-tick {
    width: 1px;
    height: 8px;
    background: #374151;
  }

  /* ── Cron examples grid ── */
  .cron-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 12px;
  }

  .cron-row {
    background: #111827;
    border-radius: 8px;
    padding: 11px 16px;
    display: flex;
    align-items: flex-start;
    gap: 14px;
    border: 1px solid rgba(255,255,255,0.04);
  }

  .cron-row .cr-expr {
    font-family: 'DM Mono', monospace;
    font-size: 12.5px;
    color: #fb923c;
    font-weight: 500;
    min-width: 130px;
    padding-top: 1px;
    flex-shrink: 0;
  }

  .cron-row .cr-desc {
    font-size: 13px;
    color: #d1d5db;
    line-height: 1.5;
  }

  .cron-row .cr-desc span {
    display: block;
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    color: #4b5563;
    margin-top: 2px;
  }

  /* ── Windows step cards ── */
  .win-steps {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 11px;
    margin-top: 14px;
  }

  .win-step {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }

  .win-step .ws-num {
    background: #1e3a5f;
    color: #93c5fd;
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

  .win-step .ws-title {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
    margin-bottom: 3px;
  }

  .win-step .ws-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.5;
  }

  /* ── Log file viewer ── */
  .log-block {
    background: #111827;
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 12.5px;
  }

  .log-block .lb-bar {
    background: #1f2937;
    padding: 8px 16px;
    font-size: 11.5px;
    color: #6b7280;
    letter-spacing: 0.04em;
    display: flex;
    justify-content: space-between;
  }

  .log-block .lb-body {
    padding: 14px 20px;
    line-height: 2;
  }

  .lb-ts   { color: #4b5563; }
  .lb-ok   { color: #34d399; }
  .lb-warn { color: #fde68a; }
  .lb-err  { color: #f87171; }
  .lb-info { color: #93c5fd; }
  .lb-text { color: #d1d5db; }

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

  .cheat-table .cron {
    font-family: 'DM Mono', monospace;
    color: #d97706;
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

# Schedule a Python Script
## to Run Automatically

&nbsp;

**Write it once. Run it forever.** No manual triggering ever again.

`cron` · `crontab` · `Task Scheduler` · `>>` · `logging`

---

## Use Cases — Why You'd Want This

Once a script runs on a schedule, it becomes infrastructure. Here's what that unlocks.

<div class="tools">
  <div class="tool-card">
    <div class="icon">📊</div>
    <div class="name">Daily reports</div>
    <div class="desc">Pull data from an API every morning, format it, and email it to yourself. Zero effort after setup.</div>
  </div>
  <div class="tool-card">
    <div class="icon">💾</div>
    <div class="name">Automatic backups</div>
    <div class="desc">Copy files to a backup folder every night. Compress old logs weekly. Never manually remember again.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔔</div>
    <div class="name">Price or data alerts</div>
    <div class="desc">Check a website or API every hour. If something changes — a price drops, a seat opens — send yourself a notification.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🧹</div>
    <div class="name">Maintenance tasks</div>
    <div class="desc">Clear temp files, rotate logs, ping a server to check it's alive. Cron jobs are the backbone of every sysadmin's toolkit.</div>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**Mac/Linux uses cron.** Windows uses Task Scheduler. Both achieve the same thing — running a command at a defined time — just with different interfaces.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01 — MAC / LINUX</div>

## Cron Jobs Explained

Cron is a time-based job scheduler built into every Mac and Linux system. You edit a file called the **crontab** to define when your script runs.

<div class="code-block">
  <div class="cb-bar">terminal — open your crontab for editing</div>
  <div class="cb-body">
    <span class="cb-prompt">~</span> <span class="cb-cmd">crontab -e</span><br>
    <span class="cb-cmt"># Opens in your default terminal editor (usually vim or nano)</span><br>
    <br>
    <span class="cb-prompt">~</span> <span class="cb-cmd">crontab -l</span>    <span class="cb-cmt"># list your current cron jobs</span><br>
    <span class="cb-prompt">~</span> <span class="cb-cmd">crontab -r</span>    <span class="cb-cmt"># remove all cron jobs (careful!)</span>
  </div>
</div>

<div class="two-col">
  <div class="col-card">
    <div class="label">Find your Python path first</div>
    <div class="code-block" style="margin-top:8px;">
      <div class="cb-body" style="padding:10px 14px; line-height:1.9; font-size:12px;">
        <span class="cb-prompt">~</span> <span class="cb-cmd">which python3</span><br>
        <span class="cb-out">/usr/local/bin/python3</span><br>
        <span class="cb-cmt"># Use this full path in cron</span>
      </div>
    </div>
  </div>
  <div class="col-card">
    <div class="label">Use absolute paths — always</div>
    <p style="font-size:13px; margin-top:8px; color:var(--muted);">Cron runs in a minimal environment with no <code>$PATH</code>. Always use the full path to both Python and your script — never relative paths.</p>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## The Cron Syntax — Dissected

Every cron job is one line with five time fields followed by the command to run.

<div class="cron-anatomy">
  <div class="ca-bar">crontab — anatomy of one line</div>
  <div class="ca-expr">
    <span class="ca-f1">30</span>
    <span class="ca-f2">8</span>
    <span class="ca-f3">*</span>
    <span class="ca-f4">*</span>
    <span class="ca-f5">1-5</span>
    <span class="ca-cmd-text">/usr/local/bin/python3 /Users/you/script.py</span>
  </div>
  <div class="ca-labels">
    <div class="ca-lbl" style="min-width:28px;">
      <div class="ca-tick" style="background:#f87171;"></div>
      <span style="color:#f87171;">min</span>
    </div>
    <div class="ca-lbl" style="min-width:24px;">
      <div class="ca-tick" style="background:#fb923c;"></div>
      <span style="color:#fb923c;">hour</span>
    </div>
    <div class="ca-lbl" style="min-width:24px;">
      <div class="ca-tick" style="background:#fde68a;"></div>
      <span style="color:#fde68a;">day</span>
    </div>
    <div class="ca-lbl" style="min-width:24px;">
      <div class="ca-tick" style="background:#34d399;"></div>
      <span style="color:#34d399;">month</span>
    </div>
    <div class="ca-lbl" style="min-width:40px;">
      <div class="ca-tick" style="background:#93c5fd;"></div>
      <span style="color:#93c5fd;">weekday</span>
    </div>
    <div class="ca-lbl">
      <div class="ca-tick" style="background:#c084fc;"></div>
      <span style="color:#c084fc;">command</span>
    </div>
  </div>
</div>

<p style="font-size:14px; color:var(--muted);">The example above runs at <strong>8:30 AM, Monday through Friday</strong>. An asterisk <code>*</code> means "every." Weekdays: 0=Sun, 1=Mon … 6=Sat.</p>

<div class="cron-grid">
  <div class="cron-row">
    <div class="cr-expr">* * * * *</div>
    <div class="cr-desc">Every minute<span>Useful only for testing</span></div>
  </div>
  <div class="cron-row">
    <div class="cr-expr">0 9 * * *</div>
    <div class="cr-desc">Every day at 9:00 AM<span>Daily morning report</span></div>
  </div>
  <div class="cron-row">
    <div class="cr-expr">0 0 * * 0</div>
    <div class="cr-desc">Every Sunday at midnight<span>Weekly cleanup</span></div>
  </div>
  <div class="cron-row">
    <div class="cr-expr">*/15 * * * *</div>
    <div class="cr-desc">Every 15 minutes<span>Polling / price checks</span></div>
  </div>
  <div class="cron-row">
    <div class="cr-expr">0 8 1 * *</div>
    <div class="cr-desc">1st of every month at 8 AM<span>Monthly billing script</span></div>
  </div>
  <div class="cron-row">
    <div class="cr-expr">30 23 * * 1-5</div>
    <div class="cr-desc">11:30 PM weekdays only<span>End-of-day backup</span></div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01 — WINDOWS</div>

## Windows Task Scheduler

No crontab on Windows — use the built-in Task Scheduler GUI instead. It's more clicks but equally powerful.

<div class="win-steps">
  <div class="win-step">
    <div class="ws-num">1</div>
    <div>
      <div class="ws-title">Open Task Scheduler</div>
      <div class="ws-desc">Press <code>Win + S</code>, search "Task Scheduler", open it. Or run <code>taskschd.msc</code> from Run (<code>Win + R</code>).</div>
    </div>
  </div>
  <div class="win-step">
    <div class="ws-num">2</div>
    <div>
      <div class="ws-title">Create Basic Task</div>
      <div class="ws-desc">Click "Create Basic Task" in the right panel. Give it a name like "Daily Report" and a description.</div>
    </div>
  </div>
  <div class="win-step">
    <div class="ws-num">3</div>
    <div>
      <div class="ws-title">Set the trigger</div>
      <div class="ws-desc">Pick Daily, Weekly, or a specific time. The wizard walks through each option clearly.</div>
    </div>
  </div>
  <div class="win-step">
    <div class="ws-num">4</div>
    <div>
      <div class="ws-title">Set the action</div>
      <div class="ws-desc">Choose "Start a Program." In the Program field, paste the full path to <code>python.exe</code>. In Arguments, paste the full path to your script.</div>
    </div>
  </div>
  <div class="win-step">
    <div class="ws-num">5</div>
    <div>
      <div class="ws-title">Find your Python path</div>
      <div class="ws-desc">Open PowerShell and run <code>where python</code>. Copy the full path — usually <code>C:\Users\you\AppData\Local\Programs\Python\Python312\python.exe</code>.</div>
    </div>
  </div>
  <div class="win-step">
    <div class="ws-num">6</div>
    <div>
      <div class="ws-title">Test it immediately</div>
      <div class="ws-desc">Right-click the task in the list → "Run." Check Last Run Result — <code>0x0</code> means success. Any other code means an error occurred.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Test Your Cron Job

Don't wait until tomorrow morning to find out it's broken. Test immediately.

<div class="platform-grid">
  <div class="platform-card mac">
    <div class="platform-header">🍎 &nbsp;macOS — schedule for 1 minute from now</div>
    <div class="platform-body">
      <span class="cmt"># Check current time</span><br>
      <span class="prompt">~</span> <span class="cmd">date</span><br>
      <span class="out">Sat Apr 18 14:22:05 PST 2026</span><br>
      <br>
      <span class="cmt"># Set to run at 14:23 (1 min away)</span><br>
      <span class="prompt">~</span> <span class="cmd">crontab -e</span><br>
      <span class="out">23 14 * * * /usr/local/bin/python3 /Users/you/script.py</span><br>
      <br>
      <span class="cmt"># Wait a minute, then check the log</span>
    </div>
  </div>
  <div class="platform-card win">
    <div class="platform-header">🪟 &nbsp;Windows — run the task manually</div>
    <div class="platform-body">
      <span class="cmt"># In Task Scheduler:</span><br>
      <span class="cmt"># Right-click task → Run</span><br>
      <span class="cmt"># Check "Last Run Result" column</span><br>
      <br>
      <span class="cmt"># Or test from PowerShell:</span><br>
      <span class="wprompt">PS></span> <span class="cmd">Start-ScheduledTask -TaskName "MyScript"</span><br>
      <br>
      <span class="cmt"># 0x0 = success, anything else = error</span>
    </div>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**Common failure reason on Mac:** cron can't find the script or Python. Always verify by running the exact command from your crontab manually in Terminal first — if it works there, cron will work too.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Log Output to a File

By default, cron swallows all output silently. Redirect it to a file so you can see what happened.

<div class="code-block">
  <div class="cb-bar">crontab — redirect stdout and stderr to a log file</div>
  <div class="cb-body">
    <span class="cb-cmt"># >> appends to the file, 2>&1 captures errors too</span><br>
    <span class="cb-field">0 9 * * *</span> <span class="cb-var">/usr/local/bin/python3 /Users/you/script.py</span> <span class="cb-hi">>> /Users/you/logs/script.log 2>&1</span>
  </div>
</div>

<div class="code-block">
  <div class="cb-bar">script.py — log from inside Python too</div>
  <div class="cb-body">
    <span class="cb-kw">import</span> <span class="cb-var">logging</span><span class="cb-op">,</span> <span class="cb-var">datetime</span><br>
    <br>
    <span class="cb-var">logging</span><span class="cb-op">.</span><span class="cb-fn">basicConfig</span><span class="cb-op">(</span><br>
    &nbsp;&nbsp;<span class="cb-var">filename</span><span class="cb-op">=</span><span class="cb-str">"/Users/you/logs/script.log"</span><span class="cb-op">,</span><br>
    &nbsp;&nbsp;<span class="cb-var">level</span><span class="cb-op">=</span><span class="cb-var">logging</span><span class="cb-op">.</span><span class="cb-prop">INFO</span><span class="cb-op">,</span><br>
    &nbsp;&nbsp;<span class="cb-var">format</span><span class="cb-op">=</span><span class="cb-str">"%(asctime)s  %(levelname)s  %(message)s"</span><br>
    <span class="cb-op">)</span><br>
    <br>
    <span class="cb-var">logging</span><span class="cb-op">.</span><span class="cb-fn">info</span><span class="cb-op">(</span><span class="cb-str">"Script started"</span><span class="cb-op">)</span><br>
    <span class="cb-cmt"># ... your code ...</span><br>
    <span class="cb-var">logging</span><span class="cb-op">.</span><span class="cb-fn">info</span><span class="cb-op">(</span><span class="cb-str">"Done — 42 records processed"</span><span class="cb-op">)</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## What a Good Log File Looks Like

<div class="log-block">
  <div class="lb-bar">
    <span>/Users/you/logs/script.log</span>
    <span style="color:#374151;">tail -f script.log</span>
  </div>
  <div class="lb-body">
    <span class="lb-ts">2026-04-18 09:00:01</span>  <span class="lb-ok">INFO</span>     <span class="lb-text">Script started</span><br>
    <span class="lb-ts">2026-04-18 09:00:02</span>  <span class="lb-ok">INFO</span>     <span class="lb-text">Fetching data from API...</span><br>
    <span class="lb-ts">2026-04-18 09:00:03</span>  <span class="lb-ok">INFO</span>     <span class="lb-text">Done — 42 records processed</span><br>
    <span class="lb-ts">2026-04-19 09:00:01</span>  <span class="lb-ok">INFO</span>     <span class="lb-text">Script started</span><br>
    <span class="lb-ts">2026-04-19 09:00:02</span>  <span class="lb-warn">WARNING</span>  <span class="lb-text">API returned 429 — rate limited</span><br>
    <span class="lb-ts">2026-04-20 09:00:01</span>  <span class="lb-ok">INFO</span>     <span class="lb-text">Script started</span><br>
    <span class="lb-ts">2026-04-20 09:00:04</span>  <span class="lb-err">ERROR</span>    <span class="lb-text">ConnectionError: Max retries exceeded</span>
  </div>
</div>

<div class="two-col" style="margin-top:12px;">
  <div class="col-card">
    <div class="label">Watch it live</div>
    <p style="font-size:13.5px; margin-top:6px;">Run <code>tail -f script.log</code> in Terminal to stream new lines as they're written. Useful during initial testing.</p>
  </div>
  <div class="col-card">
    <div class="label">Rotate old logs</div>
    <p style="font-size:13.5px; margin-top:6px;">Add a weekly cron job to delete or compress logs older than 30 days — otherwise the file grows forever: <code>find /logs -mtime +30 -delete</code></p>
  </div>
</div>

---

## Scheduling Quick Reference

<table class="cheat-table">
  <tr>
    <th>Task</th>
    <th>Mac / Linux</th>
    <th>Windows</th>
  </tr>
  <tr>
    <td>Open scheduler</td>
    <td class="mono">crontab -e</td>
    <td class="mono">taskschd.msc</td>
  </tr>
  <tr>
    <td>List scheduled jobs</td>
    <td class="mono">crontab -l</td>
    <td>Task Scheduler → Task Library</td>
  </tr>
  <tr>
    <td>Find Python path</td>
    <td class="mono">which python3</td>
    <td class="mono">where python (PowerShell)</td>
  </tr>
  <tr>
    <td>Run every day at 9 AM</td>
    <td class="cron">0 9 * * *  /path/python3 /path/script.py</td>
    <td>Trigger: Daily at 09:00</td>
  </tr>
  <tr>
    <td>Run every 15 minutes</td>
    <td class="cron">*/15 * * * *  ...</td>
    <td>Trigger: Repeat every 15 min</td>
  </tr>
  <tr>
    <td>Log all output</td>
    <td class="mono">>> /path/log.txt 2>&1</td>
    <td>Redirect in script with <code>logging</code></td>
  </tr>
  <tr>
    <td>Test immediately</td>
    <td>Set 1 min from now, wait</td>
    <td>Right-click task → Run</td>
  </tr>
  <tr>
    <td>Watch log live</td>
    <td class="mono">tail -f script.log</td>
    <td class="mono">Get-Content log.txt -Wait</td>
  </tr>
  <tr>
    <td>Remove all cron jobs</td>
    <td class="mono">crontab -r</td>
    <td>Delete task in Task Scheduler</td>
  </tr>
</table>

---

<!-- _class: final -->

# Write it once.
# Schedule it. Forget it.

&nbsp;

Cron on Mac. Task Scheduler on Windows. Log everything.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*