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
  .cb-hi     { color: #34d399; }
  .cb-out    { color: #9ca3af; }
  .cb-field  { color: #fb923c; }
  .cb-prompt { color: #22c55e; }
  .cb-cmd    { color: #f9fafb; }

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
    padding: 20px 24px 6px;
    font-family: 'DM Mono', monospace;
    font-size: 24px;
    letter-spacing: 0.04em;
    display: flex;
    gap: 20px;
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
    gap: 20px;
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
    font-size: 11px;
    color: #4b5563;
    margin-top: 2px;
  }

  /* ── Tool option cards ── */
  .tool-option-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .tool-option {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
  }

  .tool-option .to-header {
    padding: 10px 14px;
    display: flex;
    align-items: center;
    gap: 10px;
    border-bottom: 1px solid var(--border);
    background: var(--off-white);
  }

  .tool-option .to-icon { font-size: 20px; }

  .tool-option .to-name {
    font-weight: 600;
    font-size: 14px;
    color: var(--text);
  }

  .tool-option .to-tag {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    padding: 2px 7px;
    border-radius: 4px;
    margin-left: auto;
  }

  .to-tag.nocode { background: #f0fdf4; color: #166534; border: 1px solid #bbf7d0; }
  .to-tag.code   { background: #f5f3ff; color: #5b21b6; border: 1px solid #ddd6fe; }
  .to-tag.cloud  { background: var(--blue-light); color: #1e40af; border: 1px solid var(--blue-mid); }

  .tool-option .to-body {
    padding: 10px 14px;
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.55;
  }

  .tool-option .to-best {
    padding: 7px 14px;
    font-size: 12px;
    font-family: 'DM Mono', monospace;
    color: var(--blue);
    border-top: 1px solid var(--border);
    background: var(--blue-light);
  }

  /* ── Schedule calendar visual ── */
  .schedule-week {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 6px;
    margin: 14px 0;
  }

  .sw-day {
    border-radius: 8px;
    padding: 10px 6px;
    text-align: center;
    border: 1px solid var(--border);
    background: var(--white);
  }

  .sw-day .swd-name {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 6px;
  }

  .sw-day .swd-jobs {
    display: flex;
    flex-direction: column;
    gap: 3px;
  }

  .sw-day .swd-job {
    font-size: 10px;
    padding: 2px 4px;
    border-radius: 3px;
    line-height: 1.3;
    text-align: left;
  }

  .swd-job.daily  { background: var(--blue-light); color: #1e40af; }
  .swd-job.weekly { background: #f5f3ff; color: #5b21b6; }
  .swd-job.none   { background: var(--off-white); color: var(--muted); opacity: 0.4; }

  .sw-day.weekend { opacity: 0.5; }

  /* ── Monitor dashboard ── */
  .monitor-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .monitor-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 13px 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }

  .monitor-card .mc-icon { font-size: 22px; flex-shrink: 0; margin-top: 1px; }

  .monitor-card .mc-title {
    font-weight: 600;
    font-size: 13.5px;
    color: var(--text);
    margin-bottom: 3px;
  }

  .monitor-card .mc-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.5;
  }

  /* ── Log viewer ── */
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

  /* ── Platform split (Mac/Windows) ── */
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

  .platform-card.mac .platform-header { background: #1f2937; color: #9ca3af; }
  .platform-card.win .platform-header { background: #1e3a5f; color: #93c5fd; }

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

# Schedule Automations
## That Run by Themselves

&nbsp;

**Set it up once. It runs at 3 AM without you.** That's the point.

`cron` · `schedule` · `Task Scheduler` · `Zapier` · `APScheduler`

---

## Why Scheduling Matters

Running a script manually is still work. A scheduled script is infrastructure.

<div class="tools">
  <div class="tool-card">
    <div class="icon">🕐</div>
    <div class="name">Consistency</div>
    <div class="desc">Scheduled tasks run at the same time every day — regardless of whether you remembered, were busy, or were asleep. Humans aren't consistent. Schedulers are.</div>
  </div>
  <div class="tool-card">
    <div class="icon">😴</div>
    <div class="name">Runs while you sleep</div>
    <div class="desc">Backups at 2 AM. Reports ready before standup. Monitoring every 5 minutes through the night. None of this requires you to be awake.</div>
  </div>
  <div class="tool-card">
    <div class="icon">📈</div>
    <div class="name">Compounds over time</div>
    <div class="desc">A script that saves you 20 minutes runs daily, saves 120 hours a year. Scheduling is what transforms a one-time script into a permanent time asset.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔒</div>
    <div class="name">Reduces human error</div>
    <div class="desc">Forgetting to run the backup, skipping the weekly report — these are human problems. Scheduling eliminates them entirely.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Cron Basics — Kept Simple

Cron is a time-based scheduler built into every Mac and Linux system. One line tells it when to run your script.

<div class="cron-anatomy">
  <div class="ca-bar">crontab — reading the five time fields</div>
  <div class="ca-expr">
    <span class="ca-f1">0</span>
    <span class="ca-f2">8</span>
    <span class="ca-f3">*</span>
    <span class="ca-f4">*</span>
    <span class="ca-f5">1-5</span>
    <span class="ca-cmd-text">/usr/local/bin/python3 /Users/you/report.py</span>
  </div>
  <div class="ca-labels">
    <div class="ca-lbl" style="min-width:28px;">
      <div class="ca-tick" style="background:#f87171;"></div>
      <span style="color:#f87171;">min</span>
    </div>
    <div class="ca-lbl" style="min-width:28px;">
      <div class="ca-tick" style="background:#fb923c;"></div>
      <span style="color:#fb923c;">hour</span>
    </div>
    <div class="ca-lbl" style="min-width:28px;">
      <div class="ca-tick" style="background:#fde68a;"></div>
      <span style="color:#fde68a;">day</span>
    </div>
    <div class="ca-lbl" style="min-width:28px;">
      <div class="ca-tick" style="background:#34d399;"></div>
      <span style="color:#34d399;">month</span>
    </div>
    <div class="ca-lbl" style="min-width:56px;">
      <div class="ca-tick" style="background:#93c5fd;"></div>
      <span style="color:#93c5fd;">weekday</span>
    </div>
    <div class="ca-lbl">
      <div class="ca-tick" style="background:#c084fc;"></div>
      <span style="color:#c084fc;">command</span>
    </div>
  </div>
</div>

<p style="font-size:14px; color:var(--muted);">The above runs at <strong>8:00 AM Monday–Friday</strong>. An asterisk <code>*</code> means "every." Weekdays: 0 = Sun, 1 = Mon … 6 = Sat.</p>

<div class="cron-grid">
  <div class="cron-row">
    <div class="cr-expr">0 9 * * *</div>
    <div class="cr-desc">Every day at 9:00 AM<span>Daily morning report</span></div>
  </div>
  <div class="cron-row">
    <div class="cr-expr">0 0 * * 1</div>
    <div class="cr-desc">Every Monday at midnight<span>Weekly digest or cleanup</span></div>
  </div>
  <div class="cron-row">
    <div class="cr-expr">*/15 * * * *</div>
    <div class="cr-desc">Every 15 minutes<span>Monitoring, price checks</span></div>
  </div>
  <div class="cron-row">
    <div class="cr-expr">0 8 1 * *</div>
    <div class="cr-desc">1st of every month at 8 AM<span>Monthly billing or summary</span></div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Set Up Cron — Mac & Windows

<div class="platform-grid">
  <div class="platform-card mac">
    <div class="platform-header">🍎 &nbsp;macOS — crontab</div>
    <div class="platform-body">
      <span class="cmt"># Find your Python path first</span><br>
      <span class="prompt">~</span> <span class="cmd">which python3</span><br>
      <span class="out">/usr/local/bin/python3</span><br>
      <br>
      <span class="cmt"># Open crontab editor</span><br>
      <span class="prompt">~</span> <span class="cmd">crontab -e</span><br>
      <br>
      <span class="cmt"># Add this line (runs daily 9 AM)</span><br>
      <span class="out">0 9 * * * /usr/local/bin/python3<br>/Users/you/script.py >> /Users/you/logs/out.log 2>&1</span>
    </div>
  </div>
  <div class="platform-card win">
    <div class="platform-header">🪟 &nbsp;Windows — Task Scheduler</div>
    <div class="platform-body">
      <span class="cmt"># Open Task Scheduler</span><br>
      <span class="wprompt">Win+S</span> <span class="cmd">→ "Task Scheduler"</span><br>
      <br>
      <span class="cmt"># Or open via Run dialog</span><br>
      <span class="wprompt">Win+R</span> <span class="cmd">→ taskschd.msc</span><br>
      <br>
      <span class="cmt"># Find Python path</span><br>
      <span class="wprompt">PS></span> <span class="cmd">where python</span><br>
      <span class="out">C:\...\Python312\python.exe</span>
    </div>
  </div>
</div>

<div class="highlight" style="margin-top:14px;">

**Always use absolute paths in cron.** Cron runs in a stripped-down environment with no `$PATH`. Use the full path to both Python (`/usr/local/bin/python3`) and your script (`/Users/you/script.py`) — relative paths will silently fail.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Tool-Based Scheduling — No Terminal Required

If cron feels intimidating, these tools offer scheduling through a GUI or config file.

<div class="tool-option-grid">
  <div class="tool-option">
    <div class="to-header">
      <div class="to-icon">⚡</div>
      <div class="to-name">Zapier / Make</div>
      <span class="to-tag nocode">no-code</span>
    </div>
    <div class="to-body">Set a "Schedule" trigger — daily, weekly, or at a specific time. No setup beyond the platform itself. Easiest option for non-developers.</div>
    <div class="to-best">Best for: no-code automations already in Zapier/Make</div>
  </div>
  <div class="tool-option">
    <div class="to-header">
      <div class="to-icon">🐍</div>
      <div class="to-name">APScheduler</div>
      <span class="to-tag code">Python lib</span>
    </div>
    <div class="to-body">Schedule jobs from inside Python code. Runs inside a long-lived process — perfect for scripts that need to keep state between runs.</div>
    <div class="to-best">Best for: Python scripts you want to self-contain</div>
  </div>
  <div class="tool-option">
    <div class="to-header">
      <div class="to-icon">☁️</div>
      <div class="to-name">GitHub Actions</div>
      <span class="to-tag cloud">cloud</span>
    </div>
    <div class="to-body">Schedule workflows in the cloud using <code>on: schedule</code> with a cron expression. Free tier includes 2,000 minutes/month. No server needed.</div>
    <div class="to-best">Best for: scripts already in a GitHub repo</div>
  </div>
  <div class="tool-option">
    <div class="to-header">
      <div class="to-icon">🔧</div>
      <div class="to-name">n8n / Prefect</div>
      <span class="to-tag code">code + UI</span>
    </div>
    <div class="to-body">Full workflow orchestration with scheduling, retry logic, dependency graphs, and monitoring dashboards. For complex multi-step pipelines.</div>
    <div class="to-best">Best for: production-grade data pipelines</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Daily and Weekly Job Patterns

<div class="schedule-week">
  <div class="sw-day">
    <div class="swd-name">Mon</div>
    <div class="swd-jobs">
      <div class="swd-job daily">9 AM report</div>
      <div class="swd-job weekly">Weekly digest</div>
      <div class="swd-job daily">Backup 2 AM</div>
    </div>
  </div>
  <div class="sw-day">
    <div class="swd-name">Tue</div>
    <div class="swd-jobs">
      <div class="swd-job daily">9 AM report</div>
      <div class="swd-job daily">Backup 2 AM</div>
    </div>
  </div>
  <div class="sw-day">
    <div class="swd-name">Wed</div>
    <div class="swd-jobs">
      <div class="swd-job daily">9 AM report</div>
      <div class="swd-job daily">Backup 2 AM</div>
    </div>
  </div>
  <div class="sw-day">
    <div class="swd-name">Thu</div>
    <div class="swd-jobs">
      <div class="swd-job daily">9 AM report</div>
      <div class="swd-job daily">Backup 2 AM</div>
    </div>
  </div>
  <div class="sw-day">
    <div class="swd-name">Fri</div>
    <div class="swd-jobs">
      <div class="swd-job daily">9 AM report</div>
      <div class="swd-job weekly">EOW summary</div>
      <div class="swd-job daily">Backup 2 AM</div>
    </div>
  </div>
  <div class="sw-day weekend">
    <div class="swd-name">Sat</div>
    <div class="swd-jobs">
      <div class="swd-job daily">Backup 2 AM</div>
    </div>
  </div>
  <div class="sw-day weekend">
    <div class="swd-name">Sun</div>
    <div class="swd-jobs">
      <div class="swd-job daily">Backup 2 AM</div>
    </div>
  </div>
</div>

<div class="two-col">
  <div class="col-card">
    <div class="label">APScheduler — Python</div>
    <div class="code-block" style="margin-top:8px;">
      <div class="cb-body" style="padding:10px 14px; line-height:1.9; font-size:12px;">
        <span class="cb-kw">from</span> <span class="cb-var">apscheduler.schedulers.blocking</span> <span class="cb-kw">import</span> <span class="cb-fn">BlockingScheduler</span><br>
        <span class="cb-var">sched</span> <span class="cb-op">=</span> <span class="cb-fn">BlockingScheduler</span><span class="cb-op">()</span><br>
        <span class="cb-var">sched</span><span class="cb-op">.</span><span class="cb-fn">add_job</span><span class="cb-op">(</span><span class="cb-var">my_report</span><span class="cb-op">,</span> <span class="cb-str">'cron'</span><span class="cb-op">,</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-prop">hour</span><span class="cb-op">=</span><span class="cb-num">9</span><span class="cb-op">,</span> <span class="cb-prop">minute</span><span class="cb-op">=</span><span class="cb-num">0</span><span class="cb-op">,</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-prop">day_of_week</span><span class="cb-op">=</span><span class="cb-str">'mon-fri'</span><span class="cb-op">)</span><br>
        <span class="cb-var">sched</span><span class="cb-op">.</span><span class="cb-fn">start</span><span class="cb-op">()</span>
      </div>
    </div>
  </div>
  <div class="col-card">
    <div class="label">GitHub Actions — cloud cron</div>
    <div class="code-block" style="margin-top:8px;">
      <div class="cb-body" style="padding:10px 14px; line-height:1.9; font-size:12px;">
        <span class="cb-prop">on</span><span class="cb-op">:</span><br>
        &nbsp;&nbsp;<span class="cb-prop">schedule</span><span class="cb-op">:</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-op">-</span> <span class="cb-prop">cron</span><span class="cb-op">:</span> <span class="cb-str">'0 9 * * 1-5'</span><br>
        <span class="cb-prop">jobs</span><span class="cb-op">:</span><br>
        &nbsp;&nbsp;<span class="cb-prop">run-script</span><span class="cb-op">:</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="cb-op">-</span> <span class="cb-fn">run</span><span class="cb-op">:</span> <span class="cb-str">python report.py</span>
      </div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Monitor for Failures

A scheduled job that fails silently is worse than no job at all — you assume it's running when it isn't.

<div class="monitor-grid">
  <div class="monitor-card">
    <div class="mc-icon">📄</div>
    <div>
      <div class="mc-title">Log every run</div>
      <div class="mc-desc">Append a timestamped line to a log file on every run — success or failure. Check it weekly. If the log stops growing, something broke.</div>
    </div>
  </div>
  <div class="monitor-card">
    <div class="mc-icon">📧</div>
    <div>
      <div class="mc-title">Email on error</div>
      <div class="mc-desc">Wrap the script in try/except. On exception, send yourself an email with the error message and traceback before the script exits.</div>
    </div>
  </div>
  <div class="monitor-card">
    <div class="mc-icon">💬</div>
    <div>
      <div class="mc-title">Slack alert on failure</div>
      <div class="mc-desc">Post to a <code>#alerts</code> channel when something goes wrong. Slack is harder to miss than email — especially for urgent failures.</div>
    </div>
  </div>
  <div class="monitor-card">
    <div class="mc-icon">🔔</div>
    <div>
      <div class="mc-title">Heartbeat monitoring</div>
      <div class="mc-desc">Use a service like <strong>Healthchecks.io</strong> (free). Your script pings a URL on success. If the ping doesn't arrive on schedule, you get alerted.</div>
    </div>
  </div>
</div>

<div class="code-block" style="margin-top:14px;">
  <div class="cb-bar">script.py — wrap everything in try/except + alert on failure</div>
  <div class="cb-body" style="padding:10px 20px; line-height:1.9;">
    <span class="cb-kw">import</span> <span class="cb-var">logging</span><span class="cb-op">,</span> <span class="cb-var">traceback</span><br>
    <span class="cb-var">logging</span><span class="cb-op">.</span><span class="cb-fn">basicConfig</span><span class="cb-op">(</span><span class="cb-var">filename</span><span class="cb-op">=</span><span class="cb-str">"/logs/job.log"</span><span class="cb-op">,</span> <span class="cb-var">level</span><span class="cb-op">=</span><span class="cb-var">logging</span><span class="cb-op">.</span><span class="cb-prop">INFO</span><span class="cb-op">,</span> <span class="cb-var">format</span><span class="cb-op">=</span><span class="cb-str">"%(asctime)s %(levelname)s %(message)s"</span><span class="cb-op">)</span><br>
    <span class="cb-kw">try</span><span class="cb-op">:</span><br>
    &nbsp;&nbsp;<span class="cb-fn">run_my_job</span><span class="cb-op">()</span><br>
    &nbsp;&nbsp;<span class="cb-var">logging</span><span class="cb-op">.</span><span class="cb-fn">info</span><span class="cb-op">(</span><span class="cb-str">"✓ Job completed successfully"</span><span class="cb-op">)</span><br>
    <span class="cb-kw">except</span> <span class="cb-fn">Exception</span> <span class="cb-kw">as</span> <span class="cb-var">e</span><span class="cb-op">:</span><br>
    &nbsp;&nbsp;<span class="cb-var">logging</span><span class="cb-op">.</span><span class="cb-fn">error</span><span class="cb-op">(</span><span class="cb-str">f"✗ Job failed: </span><span class="cb-op">{</span><span class="cb-var">e</span><span class="cb-op">}</span><span class="cb-str">"</span><span class="cb-op">)</span><br>
    &nbsp;&nbsp;<span class="cb-fn">send_alert</span><span class="cb-op">(</span><span class="cb-var">traceback</span><span class="cb-op">.</span><span class="cb-fn">format_exc</span><span class="cb-op">())</span>  <span class="cb-cmt"># email or Slack</span>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## What a Healthy Log Looks Like

<div class="log-block">
  <div class="lb-bar">
    <span>/logs/job.log</span>
    <span style="color:#374151;">tail -f job.log</span>
  </div>
  <div class="lb-body">
    <span class="lb-ts">2026-04-14 09:00:01</span>  <span class="lb-ok">INFO</span>    <span class="lb-text">Job started</span><br>
    <span class="lb-ts">2026-04-14 09:00:03</span>  <span class="lb-ok">INFO</span>    <span class="lb-text">Fetched 24 records from API</span><br>
    <span class="lb-ts">2026-04-14 09:00:05</span>  <span class="lb-ok">INFO</span>    <span class="lb-text">✓ Job completed successfully</span><br>
    <span class="lb-ts">2026-04-15 09:00:01</span>  <span class="lb-ok">INFO</span>    <span class="lb-text">Job started</span><br>
    <span class="lb-ts">2026-04-15 09:00:02</span>  <span class="lb-warn">WARNING</span> <span class="lb-text">API returned 429 — retrying in 5s</span><br>
    <span class="lb-ts">2026-04-15 09:00:08</span>  <span class="lb-ok">INFO</span>    <span class="lb-text">✓ Job completed successfully</span><br>
    <span class="lb-ts">2026-04-16 09:00:01</span>  <span class="lb-ok">INFO</span>    <span class="lb-text">Job started</span><br>
    <span class="lb-ts">2026-04-16 09:00:02</span>  <span class="lb-err">ERROR</span>   <span class="lb-text">✗ Job failed: ConnectionError — Slack alert sent</span>
  </div>
</div>

<div class="two-col" style="margin-top:12px;">
  <div class="col-card">
    <div class="label">Watch it live</div>
    <p style="font-size:13.5px; margin-top:6px;"><code>tail -f job.log</code> streams new lines as they are written. Run this during initial testing to see each run in real time.</p>
  </div>
  <div class="col-card">
    <div class="label">Rotate old logs</div>
    <p style="font-size:13.5px; margin-top:6px;">Add a weekly cron job to delete or compress logs older than 30 days: <code>find /logs -mtime +30 -delete</code> — otherwise the file grows forever.</p>
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
    <td>Every day at 9 AM</td>
    <td class="cron">0 9 * * * /path/python3 /path/script.py</td>
    <td>Trigger: Daily at 09:00</td>
  </tr>
  <tr>
    <td>Every 15 minutes</td>
    <td class="cron">*/15 * * * * ...</td>
    <td>Trigger: Repeat every 15 min</td>
  </tr>
  <tr>
    <td>Weekdays only</td>
    <td class="cron">0 9 * * 1-5 ...</td>
    <td>Trigger: Weekly, Mon–Fri</td>
  </tr>
  <tr>
    <td>Log all output</td>
    <td class="mono">>> /path/log.txt 2>&1</td>
    <td>Use <code>logging</code> module in script</td>
  </tr>
  <tr>
    <td>Alert on failure</td>
    <td colspan="2">Wrap in try/except → send email or Slack on exception</td>
  </tr>
  <tr>
    <td>Heartbeat monitoring</td>
    <td colspan="2">healthchecks.io — ping URL on success; get alerted if ping is missed</td>
  </tr>
  <tr>
    <td>Cloud scheduling</td>
    <td colspan="2">GitHub Actions: <code>on: schedule: - cron: '0 9 * * 1-5'</code></td>
  </tr>
  <tr>
    <td>Python scheduling</td>
    <td colspan="2"><code>pip install apscheduler</code> → <code>scheduler.add_job(fn, 'cron', hour=9)</code></td>
  </tr>
</table>

---

<!-- _class: final -->

# You scheduled it.
# Now it just runs.

&nbsp;

Cron on Mac. Task Scheduler on Windows. GitHub Actions in the cloud. Log everything.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*