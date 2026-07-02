---
marp: true
theme: default
paginate: false
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300&family=DM+Mono:wght@400;500&display=swap');

  section {
    font-family: 'DM Sans', sans-serif;
    background: #0a0a0a;
    color: #f5f5f4;
    padding: 0;
    margin: 0;
    display: grid;
    grid-template-columns: 1fr 1fr;
    height: 100%;
    overflow: hidden;
  }

  /* ══ LEFT PANEL ══ */
  .left-panel {
    padding: 56px 52px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background: #0a0a0a;
    border-right: 1px solid #1f1f1f;
  }

  .eyebrow {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 0;
  }

  .eyebrow-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #e5e5e5;
    flex-shrink: 0;
  }

  .eyebrow-text {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: #737373;
    letter-spacing: 0.12em;
    text-transform: uppercase;
  }

  /* headline */
  .headline {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 28px 0 20px;
  }

  .kicker {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #a3a3a3;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 14px;
  }

  h1 {
    font-size: 44px;
    font-weight: 600;
    color: #fafafa;
    line-height: 1.1;
    margin: 0 0 8px 0;
    letter-spacing: -0.03em;
  }

  h1 em {
    font-style: normal;
    color: #ffffff;
    opacity: 0.92;
  }

  .h1-sub {
    font-size: 44px;
    font-weight: 300;
    color: #737373;
    line-height: 1.1;
    margin: 0 0 24px 0;
    letter-spacing: -0.03em;
  }

  .rule {
    width: 32px;
    height: 2px;
    background: #2a2a2a;
    border-radius: 999px;
    margin-bottom: 20px;
  }

  .sub {
    font-size: 14px;
    color: #a3a3a3;
    line-height: 1.75;
    margin: 0;
    max-width: 310px;
  }

  /* what's inside */
  .includes {
    margin-top: 28px;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .include-row {
    display: flex;
    align-items: flex-start;
    gap: 10px;
  }

  .inc-check {
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: #18181b;
    border: 1px solid #333333;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-top: 1px;
  }

  .inc-check-inner {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #d4d4d4;
  }

  .inc-text {
    font-size: 13px;
    color: #d4d4d4;
    line-height: 1.5;
  }

  .inc-text strong {
    font-weight: 500;
    color: #fafafa;
  }

  /* bottom */
  .left-bottom {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-top: 24px;
    border-top: 1px solid #1a1a1a;
  }

  .price-tag {
    display: flex;
    align-items: baseline;
    gap: 4px;
  }

  .price-free {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #f5f5f4;
    font-weight: 500;
    letter-spacing: 0.04em;
  }

  .price-note {
    font-size: 11px;
    color: #737373;
  }

  .tags {
    display: flex;
    gap: 5px;
  }

  .tag {
    font-family: 'DM Mono', monospace;
    font-size: 9px;
    color: #737373;
    border: 1px solid #262626;
    padding: 3px 8px;
    border-radius: 3px;
    letter-spacing: 0.05em;
    background: #131313;
  }

  /* ══ RIGHT PANEL ══ */
  .right-panel {
    background: #111113;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 48px 40px;
    position: relative;
    overflow: hidden;
  }

  /* subtle grid bg */
  .right-panel::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image:
      linear-gradient(#232326 1px, transparent 1px),
      linear-gradient(90deg, #232326 1px, transparent 1px);
    background-size: 28px 28px;
    opacity: 0.35;
  }

  .diagram-wrap {
    position: relative;
    z-index: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 18px;
  }

  /* slide stack */
  .slide-stack {
    position: relative;
    width: 300px;
    height: 260px;
  }

  .slide-card {
    position: absolute;
    width: 248px;
    height: 160px;
    border-radius: 10px;
    border: 1px solid #262626;
    padding: 16px 18px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    gap: 10px;
    background: #18181b;
  }

  .slide-card.c1 {
    top: 0;
    left: 40px;
    transform: rotate(-6deg);
    opacity: 0.3;
    background: #1c1c1f;
    border-color: #2a2a2a;
    box-shadow: none;
  }

  .slide-card.c2 {
    top: 22px;
    left: 20px;
    transform: rotate(-2.5deg);
    opacity: 0.65;
    box-shadow: 0 2px 10px rgba(0,0,0,0.4);
  }

  .slide-card.c3 {
    top: 52px;
    left: 4px;
    transform: rotate(1deg);
    opacity: 1;
    box-shadow: 0 10px 32px rgba(0,0,0,0.55);
  }

  /* card internals */
  .sc-bar {
    width: 100%;
    height: 4px;
    background: #d4d4d4;
    border-radius: 2px;
  }

  .sc-bar.gray { background: #3f3f3f; }

  .sc-title-block {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  .sc-t {
    height: 7px;
    border-radius: 3px;
    background: #e5e5e5;
    opacity: 0.85;
  }

  .sc-t.w60 { width: 60%; }
  .sc-t.w40 { width: 40%; }

  .sc-body {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 5px;
  }

  .sc-line {
    height: 4px;
    border-radius: 2px;
    background: #2e2e2e;
  }
  .sc-line.w100 { width: 100%; }
  .sc-line.w80  { width: 80%; }
  .sc-line.w55  { width: 55%; }
  .sc-line.blue { background: #4d4d4d; }

  .sc-cols {
    flex: 1;
    display: flex;
    gap: 7px;
  }

  .sc-col {
    flex: 1;
    border-radius: 5px;
  }
  .sc-col.b1 { background: #2a2a2d; }
  .sc-col.b2 { background: #202023; }
  .sc-col.b3 { background: #1a1a1c; }

  .sc-pills {
    display: flex;
    gap: 4px;
    flex-wrap: wrap;
  }

  .sc-pill {
    height: 9px;
    border-radius: 999px;
  }
  .sc-pill.blue { background: #d4d4d4; opacity: 0.4; }
  .sc-pill.gray { background: #333333; }
  .sc-pill.s { width: 24px; }
  .sc-pill.m { width: 38px; }
  .sc-pill.l { width: 52px; }

  /* stat row */
  .stat-row {
    display: flex;
    gap: 12px;
    position: relative;
    z-index: 1;
  }

  .stat-chip {
    background: #18181b;
    border: 1px solid #262626;
    border-radius: 8px;
    padding: 10px 16px;
    text-align: center;
    box-shadow: 0 1px 4px rgba(0,0,0,0.3);
  }

  .stat-val {
    font-family: 'DM Mono', monospace;
    font-size: 18px;
    font-weight: 500;
    color: #fafafa;
    line-height: 1;
    margin-bottom: 3px;
  }

  .stat-lbl {
    font-size: 10px;
    color: #737373;
    letter-spacing: 0.04em;
    white-space: nowrap;
  }

  .diagram-caption {
    font-family: 'DM Mono', monospace;
    font-size: 9px;
    color: #737373;
    letter-spacing: 0.08em;
    text-align: center;
    position: relative;
    z-index: 1;
    margin-top: 4px;
  }
---

<div class="left-panel">

  <div class="eyebrow">
    <div class="eyebrow-dot"></div>
    <span class="eyebrow-text">Marp Presentation Template</span>
  </div>

  <div class="headline">
    <div class="kicker">stop designing. start shipping.</div>
    <h1>Present like<br>a <em>developer.</em></h1>
    <div class="h1-sub">Write less.<br>Ship more.</div>
    <div class="rule"></div>
    <p class="sub">Everything you need to build polished, professional slides — in plain Markdown. No Figma. No PowerPoint. Just text that becomes beautiful decks.</p>
    <div class="includes">
      <div class="include-row">
        <div class="inc-check"><div class="inc-check-inner"></div></div>
        <div class="inc-text"><strong>20+ slide components</strong> — highlights, grids, timelines, diagrams, tables, and more</div>
      </div>
      <div class="include-row">
        <div class="inc-check"><div class="inc-check-inner"></div></div>
        <div class="inc-text"><strong>4 slide classes</strong> — dark cover, light body, blue CTA, centered lead</div>
      </div>
      <div class="include-row">
        <div class="inc-check"><div class="inc-check-inner"></div></div>
        <div class="inc-text"><strong>Full CSS design system</strong> — colors, typography, spacing, all pre-configured</div>
      </div>
    </div>
  </div>

  <div class="left-bottom">
    <div class="price-tag">
      <span class="price-free">DOWNLOAD NOW</span>
      <span class="price-note">— to get started.</span>
    </div>
    <div class="tags">
      <span class="tag">marp</span>
      <span class="tag">markdown</span>
      <span class="tag">v1.0</span>
    </div>
  </div>

</div>

<div class="right-panel">
  <div class="diagram-wrap">
    <div class="slide-stack">
      <!-- Card 1: back -->
      <div class="slide-card c1">
        <div class="sc-bar gray"></div>
        <div class="sc-title-block">
          <div class="sc-t w40"></div>
        </div>
        <div class="sc-cols">
          <div class="sc-col b1"></div>
          <div class="sc-col b3"></div>
        </div>
      </div>
      <!-- Card 2: middle -->
      <div class="slide-card c2">
        <div class="sc-bar"></div>
        <div class="sc-title-block">
          <div class="sc-t w40"></div>
        </div>
        <div class="sc-body">
          <div class="sc-line w100 blue"></div>
          <div class="sc-line w80"></div>
          <div class="sc-line w55"></div>
        </div>
        <div class="sc-pills">
          <div class="sc-pill blue s"></div>
          <div class="sc-pill blue m"></div>
          <div class="sc-pill gray l"></div>
        </div>
      </div>
      <!-- Card 3: front -->
      <div class="slide-card c3">
        <div class="sc-bar"></div>
        <div class="sc-title-block">
          <div class="sc-t w60"></div>
        </div>
        <div class="sc-cols">
          <div class="sc-col b1"></div>
          <div class="sc-col b2"></div>
          <div class="sc-col b3"></div>
        </div>
        <div class="sc-body">
          <div class="sc-line w80"></div>
          <div class="sc-line w55"></div>
        </div>
      </div>
    </div>
    <div class="stat-row">
      <div class="stat-chip">
        <div class="stat-val">20+</div>
        <div class="stat-lbl">components</div>
      </div>
      <div class="stat-chip">
        <div class="stat-val">4</div>
        <div class="stat-lbl">slide classes</div>
      </div>
      <div class="stat-chip">
        <div class="stat-val">6</div>
        <div class="stat-lbl">color variants</div>
      </div>
    </div>
    <div class="diagram-caption">markdown → beautiful slides · works with marp cli + vscode</div>

  </div>
</div>