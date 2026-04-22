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
  section.cover h2 { color: var(--white); border-bottom-color: #374151; }
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

  .highlight.good {
    background: #f0fdf4;
    border-color: #bbf7d0;
  }

  .highlight.warn {
    background: #fefce8;
    border-color: #fde68a;
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

  /* LinkedIn profile mock */
  .li-profile {
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 12px;
    overflow: hidden;
    margin: 14px 0;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
  }

  .li-banner {
    background: #1d4ed8;
    height: 60px;
    position: relative;
  }

  .li-avatar-row {
    background: #161b22;
    padding: 0 18px 14px;
    display: flex;
    align-items: flex-end;
    gap: 14px;
    border-bottom: 1px solid #30363d;
  }

  .li-avatar {
    width: 52px;
    height: 52px;
    border-radius: 50%;
    background: #2563eb;
    border: 3px solid #161b22;
    margin-top: -26px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    flex-shrink: 0;
  }

  .li-name-block { padding-top: 8px; }

  .li-name {
    font-size: 15px;
    font-weight: 700;
    color: #f0f6fc;
    margin-bottom: 2px;
  }

  .li-headline {
    font-size: 12px;
    line-height: 1.5;
  }

  .li-headline.bad  { color: #f87171; }
  .li-headline.good { color: #86efac; }

  .li-location { font-size: 11px; color: #4b5563; margin-top: 2px; font-family: 'DM Mono', monospace; }

  /* Headline formula */
  .headline-anatomy {
    background: #111827;
    border-radius: 10px;
    padding: 18px 22px;
    margin: 14px 0;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
  }

  .ha-row {
    display: flex;
    gap: 12px;
    align-items: baseline;
    margin-bottom: 10px;
    line-height: 1.5;
  }

  .ha-row:last-child { margin-bottom: 0; }

  .ha-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    min-width: 80px;
    flex-shrink: 0;
    padding-top: 1px;
  }

  .ha-row.formula .ha-label { color: #4b5563; }
  .ha-row.bad     .ha-label { color: #f87171; }
  .ha-row.good    .ha-label { color: #86efac; }

  .ha-row.formula .ha-text { color: #60a5fa; font-family: 'DM Mono', monospace; font-size: 13px; }
  .ha-row.bad     .ha-text { color: #f87171; }
  .ha-row.good    .ha-text { color: #86efac; }

  /* Featured section mock */
  .featured-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin: 14px 0;
  }

  .featured-card {
    background: #111827;
    border: 1px solid #30363d;
    border-radius: 8px;
    overflow: hidden;
  }

  .featured-card .fc-thumb {
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
  }

  .featured-card.fc1 .fc-thumb { background: #1e3a5f; }
  .featured-card.fc2 .fc-thumb { background: #14532d; }
  .featured-card.fc3 .fc-thumb { background: #2e1065; }

  .featured-card .fc-body {
    padding: 10px 12px;
  }

  .featured-card .fc-title {
    font-size: 12px;
    font-weight: 600;
    color: #f0f6fc;
    margin-bottom: 3px;
    line-height: 1.3;
  }

  .featured-card .fc-sub {
    font-size: 11px;
    color: #6b7280;
    line-height: 1.4;
    font-family: 'DM Mono', monospace;
  }

  /* Post examples */
  .post-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 14px 0;
  }

  .post-card {
    background: #0d1117;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid #30363d;
  }

  .post-card .poc-label {
    padding: 8px 14px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    border-bottom: 1px solid #21262d;
  }

  .post-card.bad  .poc-label { background: #7f1d1d; color: #fca5a5; }
  .post-card.good .poc-label { background: #14532d; color: #86efac; }

  .post-card .poc-body {
    padding: 12px 14px;
    font-family: 'DM Sans', sans-serif;
    font-size: 12px;
    line-height: 1.8;
  }

  .post-card.bad  .poc-body { color: #f87171; }
  .post-card.good .poc-body { color: #d1d5db; }

  /* Connection type cards */
  .connect-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin: 14px 0;
  }

  .connect-card {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 14px 16px;
  }

  .connect-card .cc-icon  { font-size: 20px; margin-bottom: 6px; }
  .connect-card .cc-type  { font-size: 13px; font-weight: 600; color: var(--text); margin-bottom: 4px; }
  .connect-card .cc-why   { font-size: 12px; color: var(--muted); line-height: 1.5; }
  .connect-card .cc-how   { font-size: 11px; color: var(--blue); font-family: 'DM Mono', monospace; margin-top: 6px; }

  /* 1-post calendar */
  .post-calendar {
    background: #111827;
    border-radius: 10px;
    padding: 18px 22px;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .pc-week {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 8px;
    margin-bottom: 10px;
  }

  .pc-day {
    border-radius: 6px;
    padding: 8px 4px;
    text-align: center;
  }

  .pc-day .pd-label { font-size: 9px; color: #4b5563; text-transform: uppercase; margin-bottom: 4px; }
  .pc-day .pd-dot   { width: 10px; height: 10px; border-radius: 50%; margin: 0 auto; }

  .pc-day.empty .pd-dot   { background: #1f2937; }
  .pc-day.engage .pd-dot  { background: #374151; }
  .pc-day.post .pd-dot    { background: #2563eb; width: 14px; height: 14px; }

  .pc-day.post   { background: #1e3a5f; border: 1px solid #2563eb; }
  .pc-day.engage { background: #1f2937; }
  .pc-day.empty  { background: #111827; }

  .pc-legend {
    display: flex;
    gap: 20px;
    font-size: 11px;
    margin-top: 8px;
  }

  .pc-legend .pcl-item { display: flex; align-items: center; gap: 6px; }
  .pc-legend .pcl-dot  { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }

  /* Post ideas list */
  .ideas-block {
    background: #111827;
    border-radius: 10px;
    padding: 16px 20px;
    margin: 12px 0;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    line-height: 2.2;
    color: #d1d5db;
  }

  .ideas-block .ib-cat {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #4b5563;
    margin-bottom: 6px;
  }

  .ideas-block .ib-item { color: #d1d5db; }
  .ideas-block .ib-item .ib-tag { color: #60a5fa; }

  /* two-col */
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
---

<!-- _class: cover -->

# How to Use LinkedIn
## as a Developer

&nbsp;

**You don't need to perform. You need to be findable and credible.**

`headline` · `featured` · `posting` · `connections` · `consistency`

---

## Profile vs Resume Mindset

A resume is a document you send. A LinkedIn profile is a surface people search.

<div class="tools">
  <div class="tool-card">
    <div class="icon">📄</div>
    <div class="name">Resume mindset</div>
    <div class="desc">Formatted for one reader, one job, one moment. Static. Passive. Only seen when you send it.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔍</div>
    <div class="name">LinkedIn mindset</div>
    <div class="desc">Optimised for search, skimmability, and ongoing credibility. Works for you while you sleep.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🎯</div>
    <div class="name">What LinkedIn actually does</div>
    <div class="desc">Recruiters search keywords. Collaborators check your profile after meeting you. Strangers find your posts and follow. None of that happens with a resume.</div>
  </div>
  <div class="tool-card">
    <div class="icon">⚡</div>
    <div class="name">The shift</div>
    <div class="desc">Stop treating your profile as a job application. Treat it as a standing answer to: "Who is this person and what do they do?"</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## The Headline Formula

Your headline is the most-seen text on LinkedIn. It appears in search results, connection requests, notifications, and comments.

<div class="headline-anatomy">
  <div class="ha-row formula">
    <span class="ha-label">Formula</span>
    <span class="ha-text">[What you do] · [for whom / in what domain] · [what you're building or known for]</span>
  </div>
  <div class="ha-row bad">
    <span class="ha-label">❌ Weak</span>
    <span class="ha-text">Electrical Engineer | Open to Opportunities</span>
  </div>
  <div class="ha-row bad">
    <span class="ha-label">❌ Weak</span>
    <span class="ha-text">Software Developer | Passionate about Technology</span>
  </div>
  <div class="ha-row good">
    <span class="ha-label">✅ Strong</span>
    <span class="ha-text">Electrical Engineer · Power Systems + Python Automation · Building AI tools for grid analysis</span>
  </div>
  <div class="ha-row good">
    <span class="ha-label">✅ Strong</span>
    <span class="ha-text">Python Developer · pandas & Flask · Automating the manual work engineers hate</span>
  </div>
</div>

<div class="highlight">

The strong headlines answer the same question a recruiter is asking: "What does this person do and is it relevant to what I need?" Weak headlines make them guess. Strong headlines make them click.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Featured Section as Mini Portfolio

The Featured section sits above the fold — it's the first content a profile visitor scrolls to. Use it as a three-slot portfolio.

<div class="featured-grid">
  <div class="featured-card fc1">
    <div class="fc-thumb">🔗</div>
    <div class="fc-body">
      <div class="fc-title">Visayas Grid Monitoring Tool</div>
      <div class="fc-sub">GitHub · Python · pandapower<br>Live demo available</div>
    </div>
  </div>
  <div class="featured-card fc2">
    <div class="fc-thumb">✍️</div>
    <div class="fc-body">
      <div class="fc-title">Why Engineers Should Learn Python</div>
      <div class="fc-sub">Substack post · 1.2k reads<br>Most-read article</div>
    </div>
  </div>
  <div class="featured-card fc3">
    <div class="fc-thumb">📊</div>
    <div class="fc-body">
      <div class="fc-title">N-1 Contingency Analysis — Explained Simply</div>
      <div class="fc-sub">LinkedIn carousel · 4.3k impressions<br>Top performing post</div>
    </div>
  </div>
</div>

<div class="two-col">
  <div class="col-card">
    <div class="label">What to feature</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">Best GitHub repo · best Substack post · best LinkedIn post · portfolio site · live project demo</p>
  </div>
  <div class="col-card">
    <div class="label">What not to feature</div>
    <p style="font-size:14px; margin-top:8px; color:#374151;">Certificates · generic media mentions · outdated projects · anything without a working link</p>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## How to Post Without Cringing

The reason most developers don't post: they think LinkedIn requires corporate performance. It doesn't.

<div class="post-compare">
  <div class="post-card bad">
    <div class="poc-label">❌ Performing — avoid this</div>
    <div class="poc-body">
      Excited to announce that I've just completed my AWS certification! 🎉 This journey has been incredibly humbling and I'm so grateful for the support of my amazing team. #AWS #Cloud #Blessed
    </div>
  </div>
  <div class="post-card good">
    <div class="poc-label">✅ Real — do this instead</div>
    <div class="poc-body">
      Spent 3 hours debugging a pandas merge yesterday. The issue: duplicate column names after joining two DataFrames.<br><br>
      The fix was one line: df.merge(..., suffixes=('_left', '_right'))<br><br>
      If you've hit this — check your column names first.
    </div>
  </div>
</div>

<div class="highlight good">

**The developer posting formula:** share what you just learned, built, or fixed. One specific thing. One concrete takeaway. No performance required. Your working knowledge is more valuable to your audience than any announcement.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## Who to Connect With

Quality of connections matters more than quantity. Strategic connecting builds a relevant, active network.

<div class="connect-grid">
  <div class="connect-card">
    <div class="cc-icon">🤝</div>
    <div class="cc-type">People in your domain</div>
    <div class="cc-why">Engineers, data scientists, developers working in areas adjacent to yours. Mutual relevance = mutual engagement.</div>
    <div class="cc-how">Search job title + industry</div>
  </div>
  <div class="connect-card">
    <div class="cc-icon">✍️</div>
    <div class="cc-type">Creators you read</div>
    <div class="cc-why">Connect with people whose posts you actually engage with. Your comments on their posts become visibility for your profile.</div>
    <div class="cc-how">Follow + comment first, then connect</div>
  </div>
  <div class="connect-card">
    <div class="cc-icon">🏢</div>
    <div class="cc-type">Hiring managers + recruiters</div>
    <div class="cc-why">In roles or companies you're interested in. A warm connection profile view beats a cold application every time.</div>
    <div class="cc-how">Connect after liking their content</div>
  </div>
  <div class="connect-card">
    <div class="cc-icon">🌱</div>
    <div class="cc-type">People at your level</div>
    <div class="cc-why">Peers learning alongside you are the highest-engagement connections. They share your content, and you share theirs.</div>
    <div class="cc-how">Bootcamp, course, or community peers</div>
  </div>
  <div class="connect-card">
    <div class="cc-icon">🔝</div>
    <div class="cc-type">One level above you</div>
    <div class="cc-why">Seniors and leads who post regularly. Their engagement on your content expands your reach dramatically.</div>
    <div class="cc-how">Comment thoughtfully on their posts first</div>
  </div>
  <div class="connect-card">
    <div class="cc-icon">🚫</div>
    <div class="cc-type">Everyone with a pulse</div>
    <div class="cc-why">Spray-connecting dilutes your feed and hurts the algorithm. 500 irrelevant connections is worse than 200 relevant ones.</div>
    <div class="cc-how">Skip if no clear relevance</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## The 1-Post-Per-Week Minimum

Consistency beats frequency. One post per week, every week, compounds faster than daily posting that burns out.

<div class="post-calendar">
  <div class="pc-week">
    <div class="pc-day empty"><div class="pd-label">Mon</div><div class="pd-dot"></div></div>
    <div class="pc-day engage"><div class="pd-label">Tue</div><div class="pd-dot"></div></div>
    <div class="pc-day empty"><div class="pd-label">Wed</div><div class="pd-dot"></div></div>
    <div class="pc-day post"><div class="pd-label">Thu</div><div class="pd-dot"></div></div>
    <div class="pc-day engage"><div class="pd-label">Fri</div><div class="pd-dot"></div></div>
    <div class="pc-day empty"><div class="pd-label">Sat</div><div class="pd-dot"></div></div>
    <div class="pc-day empty"><div class="pd-label">Sun</div><div class="pd-dot"></div></div>
  </div>
  <div class="pc-legend">
    <div class="pcl-item"><div class="pcl-dot" style="background:#2563eb"></div><span style="color:#60a5fa">Post (1× per week)</span></div>
    <div class="pcl-item"><div class="pcl-dot" style="background:#374151"></div><span style="color:#6b7280">Engage — comment on 2–3 posts (2× per week)</span></div>
    <div class="pcl-item"><div class="pcl-dot" style="background:#1f2937"></div><span style="color:#374151">Rest days</span></div>
  </div>
</div>

<div class="ideas-block">
  <div class="ib-label">10 post ideas that never run dry for developers</div>
  <div class="ib-item"><span class="ib-tag">thing I fixed</span> · One bug you solved this week — the problem, the fix, one line of code</div>
  <div class="ib-item"><span class="ib-tag">thing I learned</span> · One concept you finally understood — explain it simply</div>
  <div class="ib-item"><span class="ib-tag">thing I built</span> · A script, a feature, a tool — screenshot + one paragraph</div>
  <div class="ib-item"><span class="ib-tag">tool comparison</span> · Two approaches to the same problem — what you chose and why</div>
</div>

---

## The LinkedIn Audit Checklist

<div class="two-col">
  <div class="col-card">
    <div class="label">✅ Profile must-haves</div>
    <p style="font-size:14px; margin-top:8px; color:#374151; line-height:2;">
      ✦ Headline using the formula — not your job title alone<br>
      ✦ About section: role + domain + current focus + contact<br>
      ✦ 3 items in Featured — best work, live links<br>
      ✦ Profile photo — professional but human<br>
      ✦ Custom URL: linkedin.com/in/yourname
    </p>
  </div>
  <div class="col-card">
    <div class="label">⚡ Weekly minimum</div>
    <p style="font-size:14px; margin-top:8px; color:#374151; line-height:2;">
      ✦ 1 post — something you learned, built, or fixed<br>
      ✦ 2–3 genuine comments on others' posts<br>
      ✦ 1–2 new connections with a personal note<br>
      ✦ No hashtag spam, no engagement bait<br>
      ✦ Consistency > virality. Every. Time.
    </p>
  </div>
</div>

<div class="highlight good">

**The compound effect:** 1 post per week = 52 posts per year. After 6 months of consistency, your profile becomes a searchable archive of your thinking and expertise. That archive does work you don't have to.

</div>

---

<!-- _class: final -->

# Show your work.
# Do it consistently.
# Let it compound.

&nbsp;

LinkedIn doesn't reward the loudest voice. It rewards the most consistent one.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*