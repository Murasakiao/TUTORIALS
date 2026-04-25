---
marp: true
theme: default
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,400;0,500;0,600;1,400&family=DM+Mono:wght@400;500&display=swap');

  :root {
    --amber: #d97706;
    --amber-light: #fffbeb;
    --amber-mid: #fde68a;
    --amber-dim: #b45309;
    --text: #1c1917;
    --muted: #78716c;
    --border: #e7e5e4;
    --white: #ffffff;
    --off-white: #fafaf9;
    --slate: #44403c;
  }

  section {
    font-family: 'DM Sans', sans-serif;
    background: var(--white);
    color: var(--text);
    padding: 52px 64px;
    font-size: 18px;
    line-height: 1.65;
  }

  section::after {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
  }

  h1 {
    font-family: 'DM Sans', sans-serif;
    font-size: 42px;
    font-weight: 600;
    color: var(--text);
    line-height: 1.15;
    margin-bottom: 0.4em;
    letter-spacing: -0.5px;
  }

  h2 {
    font-family: 'DM Sans', sans-serif;
    font-size: 27px;
    font-weight: 600;
    color: var(--text);
    border-bottom: 1.5px solid var(--border);
    padding-bottom: 10px;
    margin-bottom: 22px;
    letter-spacing: -0.3px;
  }

  h3 {
    font-family: 'DM Sans', sans-serif;
    font-size: 19px;
    font-weight: 500;
    color: var(--amber);
    margin-bottom: 8px;
  }

  p { color: var(--text); margin: 0.4em 0; }
  ul { padding-left: 1.4em; }
  li { margin-bottom: 10px; color: var(--text); }
  strong { color: var(--amber-dim); font-weight: 600; }

  code {
    font-family: 'DM Mono', monospace;
    background: var(--amber-light);
    color: var(--amber-dim);
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.87em;
  }

  blockquote {
    border-left: 3px solid var(--amber);
    background: var(--amber-light);
    padding: 16px 20px;
    margin: 20px 0;
    border-radius: 0 6px 6px 0;
    font-family: 'DM Mono', monospace;
    font-size: 0.82em;
    color: #92400e;
    line-height: 1.6;
  }

  blockquote p { color: #92400e; margin: 0; }

  /* ── Cover ── */
  section.cover {
    background: #1c1917;
    color: var(--white);
    display: flex;
    flex-direction: column;
    justify-content: center;
    position: relative;
    overflow: hidden;
  }

  section.cover::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
      radial-gradient(ellipse at 80% 20%, rgba(217,119,6,0.08) 0%, transparent 55%),
      radial-gradient(ellipse at 10% 85%, rgba(217,119,6,0.05) 0%, transparent 45%);
    pointer-events: none;
  }

  section.cover h1 { color: var(--white); font-size: 44px; letter-spacing: -0.8px; }
  section.cover h2 { color: #a8a29e; border-bottom-color: #44403c; font-size: 20px; font-weight: 400; letter-spacing: 0; }
  section.cover p  { color: #78716c; }
  section.cover strong { color: #fbbf24; }
  section.cover code { background: #292524; color: #fbbf24; border: 1px solid #44403c; }

  section.cover .series-badge {
    display: inline-block;
    background: #292524;
    color: #d97706;
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 500;
    padding: 5px 14px;
    border-radius: 4px;
    margin-bottom: 22px;
    letter-spacing: 0.1em;
    border: 1px solid #44403c;
    width: fit-content;
  }

  section.step { background: var(--off-white); }

  .highlight {
    background: var(--amber-light);
    border: 1px solid #fde68a;
    border-radius: 8px;
    padding: 16px 22px;
    margin: 16px 0;
  }

  .step-badge {
    display: inline-block;
    background: var(--text);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    padding: 4px 12px;
    border-radius: 3px;
    margin-bottom: 12px;
    letter-spacing: 0.08em;
  }

  section.final {
    background: #1c1917;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    position: relative;
    overflow: hidden;
  }

  section.final::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at 50% 50%, rgba(217,119,6,0.10) 0%, transparent 65%);
    pointer-events: none;
  }

  section.final h1 { color: white; font-size: 40px; letter-spacing: -0.5px; }
  section.final p  { color: #a8a29e; font-size: 18px; }
  section.final strong { color: #fbbf24; }
  section.final em { color: #a8a29e; }

  /* ── Matters grid ── */
  .matters-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .matters-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 14px 16px;
    display: flex;
    align-items: flex-start;
    gap: 13px;
  }

  .matters-card .mcc-icon { font-size: 24px; flex-shrink: 0; }
  .matters-card .mcc-title {
    font-weight: 600;
    font-size: 14px;
    color: var(--text);
    margin-bottom: 4px;
  }
  .matters-card .mcc-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.55;
  }

  /* ── Cheat table ── */
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
    font-size: 11.5px;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.07em;
  }

  .cheat-table td {
    padding: 9px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
    font-size: 13px;
  }

  .cheat-table tr:last-child td { border-bottom: none; }
  .cheat-table tr:nth-child(even) td { background: var(--off-white); }
  .cheat-table .mono {
    font-family: 'DM Mono', monospace;
    color: var(--amber-dim);
    font-size: 12px;
  }

  /* ── Code block ── */
  .code-block {
    background: #1c1917;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid #44403c;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
  }

  .code-block .cb-header {
    background: #292524;
    border-bottom: 1px solid #44403c;
    padding: 8px 16px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .code-block .cb-header .cb-dots { display: flex; gap: 5px; }
  .code-block .cb-header .cb-dot  { width: 10px; height: 10px; border-radius: 50%; }
  .code-block .cb-header .cb-dot.red    { background: #ef4444; }
  .code-block .cb-header .cb-dot.yellow { background: #eab308; }
  .code-block .cb-header .cb-dot.green  { background: #22c55e; }

  .code-block .cb-header .cb-filename {
    font-size: 11px;
    color: #a8a29e;
    font-weight: 500;
    letter-spacing: 0.04em;
    margin-left: 4px;
  }

  .code-block .cb-body {
    padding: 16px 20px;
    font-size: 12px;
    line-height: 1.75;
    color: #d6d3d1;
    white-space: pre;
  }

  .code-block .cb-body .kw  { color: #c084fc; }
  .code-block .cb-body .fn  { color: #fbbf24; }
  .code-block .cb-body .st  { color: #86efac; }
  .code-block .cb-body .cm  { color: #57534e; }
  .code-block .cb-body .nu  { color: #fb923c; }
  .code-block .cb-body .bi  { color: #67e8f9; }
  .code-block .cb-body .va  { color: #d6d3d1; }

  /* ── Schema block ── */
  .schema-block {
    background: #182932;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid #0369a1;
    margin: 14px 0;
    font-family: 'DM Mono', monospace;
  }

  .schema-block .sb-header {
    background: #305264;
    padding: 8px 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .schema-block .sb-header .sb-title {
    font-size: 11px;
    color: #bae6fd;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.09em;
  }

  .schema-block .sb-header .sb-badge {
    font-size: 10px;
    background: #0c4a6e;
    color: #7dd3fc;
    padding: 2px 8px;
    border-radius: 3px;
    font-weight: 500;
  }

  .schema-block .sb-body {
    padding: 14px 18px;
    font-size: 12px;
    line-height: 1.8;
    color: #bae6fd;
    white-space: pre;
  }

  .schema-block .sb-body .sk { color: #fde68a; }
  .schema-block .sb-body .sv { color: #86efac; }
  .schema-block .sb-body .sn { color: #fb923c; }
  .schema-block .sb-body .sc { color: #57534e; }

  /* ── Walkthrough ── */
  .walkthrough {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .wt-row {
    display: grid;
    grid-template-columns: 36px 1fr;
    border-bottom: 1px solid var(--border);
    align-items: stretch;
  }

  .wt-row:last-child { border-bottom: none; }

  .wt-row .wr-num {
    background: var(--text);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .wt-row .wr-content { padding: 11px 16px; }

  .wt-row .wr-content .wrc-title {
    font-weight: 600;
    font-size: 13px;
    color: var(--text);
    margin-bottom: 3px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .wt-row .wr-content .wrc-desc {
    font-size: 12px;
    color: var(--muted);
    line-height: 1.55;
  }

  .wt-row .wr-content .wrc-code {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--amber-dim);
    background: var(--amber-light);
    padding: 2px 8px;
    border-radius: 3px;
    margin-top: 5px;
    display: inline-block;
  }

  .wt-row:nth-child(odd)  .wr-content { background: var(--white); }
  .wt-row:nth-child(even) .wr-content { background: var(--off-white); }

  /* ── Compare grid ── */
  .compare-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin: 14px 0;
  }

  .cg-card {
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .cg-card .cg-head {
    padding: 9px 14px;
    font-weight: 600;
    font-size: 12.5px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border);
  }

  .cg-card.bad  .cg-head { background: #fef2f2; color: #991b1b; border-color: #fecaca; }
  .cg-card.good .cg-head { background: #f0fdf4; color: #166534; border-color: #bbf7d0; }

  .cg-card .cg-body {
    padding: 12px 14px;
    font-size: 12.5px;
    color: var(--muted);
    background: var(--white);
    line-height: 1.65;
  }

  .cg-card.good .cg-body { color: var(--text); }

  /* ── Team anatomy box ── */
  .team-anatomy {
    border-radius: 10px;
    overflow: hidden;
    border: 2px solid #fde68a;
    margin: 14px 0;
  }

  .team-anatomy .ta-header {
    padding: 10px 16px;
    background: var(--amber-light);
    border-bottom: 1px solid #fde68a;
    font-weight: 700;
    font-size: 14px;
    color: #92400e;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .team-anatomy .ta-body {
    padding: 14px 16px;
    background: var(--white);
    display: flex;
    flex-direction: column;
    gap: 9px;
  }

  .ta-layer {
    border-radius: 7px;
    padding: 10px 14px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
    font-size: 12.5px;
    line-height: 1.55;
  }

  .ta-layer .tal-icon  { font-size: 19px; flex-shrink: 0; margin-top: 1px; }
  .ta-layer .tal-name  { font-weight: 600; font-size: 13px; color: var(--text); display: block; margin-bottom: 2px; }
  .ta-layer .tal-desc  { color: var(--muted); font-size: 12px; }

  .ta-layer.entry  { background: #f0f9ff;           border: 1px solid #bae6fd; }
  .ta-layer.orch   { background: var(--amber-light); border: 1px solid #fde68a; }
  .ta-layer.specs  { background: #f0fdf4;            border: 1px solid #bbf7d0; }
  .ta-layer.state  { background: #fdf4ff;            border: 1px solid #e9d5ff; }
  .ta-layer.output { background: var(--off-white);   border: 1px solid var(--border); }

  /* ── Handoff flow ── */
  .handoff-flow {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .hf-row {
    display: grid;
    grid-template-columns: 36px 170px 1fr 150px;
    align-items: stretch;
    border-bottom: 1px solid var(--border);
  }

  .hf-row:last-child { border-bottom: none; }

  .hf-row .hfr-num {
    background: var(--text);
    color: white;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }

  .hf-row .hfr-actor {
    padding: 11px 13px;
    font-weight: 600;
    font-size: 12.5px;
    color: var(--text);
    border-right: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 7px;
    line-height: 1.4;
  }

  .hf-row.top-level  .hfr-actor { background: #1c1917; color: #fbbf24; }
  .hf-row.content-t  .hfr-actor { background: var(--amber-light); color: #92400e; }
  .hf-row.eng-t      .hfr-actor { background: #f0f9ff; color: #0c4a6e; }
  .hf-row.validate   .hfr-actor { background: #f0fdf4; color: #166534; }

  .hf-row .hfr-action {
    padding: 11px 14px;
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.6;
    display: flex;
    align-items: center;
  }

  .hf-row .hfr-artifact {
    padding: 11px 13px;
    border-left: 1px solid var(--border);
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    display: flex;
    align-items: center;
    gap: 6px;
    font-weight: 500;
  }

  .hf-row.top-level  .hfr-artifact { background: #292524; color: #fbbf24; }
  .hf-row.content-t  .hfr-artifact { background: var(--amber-light); color: #92400e; }
  .hf-row.eng-t      .hfr-artifact { background: #f0f9ff; color: #0369a1; }
  .hf-row.validate   .hfr-artifact { background: #f0fdf4; color: #166534; }

  /* ── Shared context tiers ── */
  .context-tiers {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .ct-row {
    display: grid;
    grid-template-columns: 160px 1fr 160px;
    align-items: stretch;
    border-bottom: 1px solid var(--border);
  }

  .ct-row:last-child { border-bottom: none; }

  .ct-row .ctr-tier {
    padding: 11px 14px;
    font-weight: 700;
    font-size: 12.5px;
    border-right: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 8px;
    line-height: 1.4;
  }

  .ct-row.global    .ctr-tier { background: #1c1917;           color: #fbbf24; }
  .ct-row.team      .ctr-tier { background: var(--amber-light); color: #92400e; }
  .ct-row.specialist .ctr-tier { background: #f0fdf4;          color: #166534; }

  .ct-row .ctr-what {
    padding: 11px 14px;
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.6;
    display: flex;
    align-items: center;
  }

  .ct-row .ctr-scope {
    padding: 11px 13px;
    border-left: 1px solid var(--border);
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    display: flex;
    align-items: center;
  }

  .ct-row.global     .ctr-scope { background: #292524;          color: #fbbf24; }
  .ct-row.team       .ctr-scope { background: var(--amber-light); color: #92400e; }
  .ct-row.specialist .ctr-scope { background: #f0fdf4;           color: #166534; }

  /* ── State isolation visual ── */
  .isolation-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin: 14px 0;
  }

  .ig-col { padding: 18px 20px; }
  .ig-col + .ig-col { border-left: 1px solid var(--border); }
  .ig-col.rot   { background: #fef2f2; }
  .ig-col.clean { background: #f0fdf4; }

  .ig-col .igc-label {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.09em;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .ig-col.rot   .igc-label { color: #991b1b; }
  .ig-col.clean .igc-label { color: #166534; }

  .ig-col .igc-item {
    font-size: 12.5px;
    padding: 8px 0;
    border-bottom: 1px solid rgba(0,0,0,0.06);
    display: flex;
    align-items: flex-start;
    gap: 9px;
    color: var(--text);
    line-height: 1.5;
  }

  .ig-col .igc-item:last-child { border-bottom: none; }

  /* ── Generator-critic flow ── */
  .gc-flow {
    display: flex;
    align-items: stretch;
    gap: 0;
    margin: 16px 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .gcf-node {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 18px 10px;
    text-align: center;
    gap: 5px;
    min-width: 0;
  }

  .gcf-node .gfn-icon { font-size: 26px; }
  .gcf-node .gfn-type {
    font-family: 'DM Mono', monospace;
    font-size: 9.5px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
  }
  .gcf-node .gfn-name { font-weight: 700; font-size: 13.5px; color: var(--text); }
  .gcf-node .gfn-sub  { font-size: 11px; color: var(--muted); line-height: 1.4; }

  .gcf-node.n-input   { background: #f0f9ff; }
  .gcf-node.n-input   .gfn-type { color: #0369a1; }
  .gcf-node.n-gen     { background: var(--amber-light); }
  .gcf-node.n-gen     .gfn-type { color: #92400e; }
  .gcf-node.n-artifact { background: var(--off-white); }
  .gcf-node.n-artifact .gfn-type { color: var(--muted); }
  .gcf-node.n-critic  { background: #fef2f2; }
  .gcf-node.n-critic  .gfn-type { color: #991b1b; }
  .gcf-node.n-decide  { background: #f0fdf4; }
  .gcf-node.n-decide  .gfn-type { color: #166534; }

  .gcf-arrow {
    display: flex;
    align-items: center;
    padding: 0 6px;
    font-size: 16px;
    color: var(--amber);
    background: var(--white);
    border-left: 1px solid var(--border);
    border-right: 1px solid var(--border);
    flex-shrink: 0;
  }

  .gc-loop-back {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 6px;
    gap: 8px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
  }

  .gc-loop-line {
    height: 1.5px;
    background: var(--border);
    border-radius: 999px;
    flex: 1;
    max-width: 100px;
  }

  /* ── GC team compare ── */
  .gc-team-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin: 14px 0;
  }

  .gc-team-card {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .gc-team-card .gctc-head {
    padding: 10px 14px;
    font-weight: 700;
    font-size: 13px;
    display: flex;
    align-items: center;
    gap: 9px;
    border-bottom: 1px solid var(--border);
  }

  .gc-team-card.gen    .gctc-head { background: var(--amber-light); color: #92400e; border-color: #fde68a; }
  .gc-team-card.critic .gctc-head { background: #fef2f2;            color: #991b1b; border-color: #fecaca; }

  .gc-team-card .gctc-body {
    padding: 12px 14px;
    background: var(--white);
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.6;
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .gctc-row {
    display: flex;
    gap: 8px;
    align-items: flex-start;
    font-size: 12px;
    line-height: 1.5;
  }

  .gctc-row .gctr-tag {
    font-family: 'DM Mono', monospace;
    font-size: 9.5px;
    font-weight: 700;
    padding: 2px 6px;
    border-radius: 3px;
    flex-shrink: 0;
    margin-top: 1px;
  }

  .gen    .gctr-tag { background: #fde68a; color: #92400e; }
  .critic .gctr-tag { background: #fecaca; color: #991b1b; }

  .gctc-row .gctr-text { color: var(--muted); }

  .gc-team-card .gctc-footer {
    padding: 8px 14px;
    border-top: 1px solid var(--border);
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
  }

  .gc-team-card.gen    .gctc-footer { background: var(--amber-light); color: #92400e; }
  .gc-team-card.critic .gctc-footer { background: #fef2f2;            color: #991b1b; }
---

<!-- _class: cover -->

<div class="series-badge">AGENT TEAMS · LEVEL 4 — PART 2 OF 4</div>

# Designing Teams and Handoffs
## Anatomy, inter-team passing, shared context, state isolation, and the Generator + Critic pattern

&nbsp;

**A team is more than a group of specialists.** It has a structure, a boundary, and a strict set of rules about what crosses that boundary — and what never does.

`team anatomy` · `inter-team handoff` · `shared context` · `state isolation` · `generator + critic`

---

## What This Part Covers

Part 1 introduced the team mental model. Part 2 is about the engineering decisions that make teams work in practice — before you write a single line of team code.

<div class="matters-grid">
  <div class="matters-card">
    <div class="mcc-icon">🏗️</div>
    <div>
      <div class="mcc-title">Team anatomy</div>
      <div class="mcc-desc">Every team has five layers: an entry point, a team orchestrator, a set of specialists, a scoped state store, and an output envelope. Knowing the anatomy prevents the most common design mistake — letting teams grow without structure.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🔀</div>
    <div>
      <div class="mcc-title">Inter-team handoffs</div>
      <div class="mcc-desc">When one team's output becomes another team's input, the handoff must go through the top-level orchestrator — never team to team directly. The rules for what crosses the boundary, and what shape it takes, are the engineering.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">💾</div>
    <div>
      <div class="mcc-title">Shared context and state isolation</div>
      <div class="mcc-desc">Some context is genuinely shared — run ID, user preferences, original intent. Most context is team-scoped. Getting this separation wrong produces the worst failure mode at Level 4: context rot, where stale data from one run poisons the next.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">⚔️</div>
    <div>
      <div class="mcc-title">Generator + Critic at team scale</div>
      <div class="mcc-desc">The Generator + Critic pattern — one team produces, another team evaluates — is the most powerful quality gate available at Level 4. Implemented correctly it catches failures before they reach the top level. Implemented incorrectly it creates loops that never converge.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## Anatomy of a Team

Every team — regardless of its domain — has the same five layers. The layers are what make a team a team, not just a group of specialists assigned to the same folder.

<div class="team-anatomy">
  <div class="ta-header">✍️ &nbsp;Content Team — five-layer anatomy</div>
  <div class="ta-body">
    <div class="ta-layer entry">
      <div class="tal-icon">🚪</div>
      <div>
        <div class="tal-name">① Entry point — <code>run_content_team(**params)</code></div>
        <div class="tal-desc">The single public function the top-level orchestrator calls. Validates team-level input params. Never calls specialists directly — only calls the team orchestrator. Returns a <code>TeamResponse</code>.</div>
      </div>
    </div>
    <div class="ta-layer orch">
      <div class="tal-icon">🧭</div>
      <div>
        <div class="tal-name">② Team orchestrator — sequences specialists internally</div>
        <div class="tal-desc">Owns the internal pipeline: research → outline → write → edit → QA. Manages team-scoped <code>RunState</code>. Decides which specialists to call and in what order based on the task params. Never visible to the top level.</div>
      </div>
    </div>
    <div class="ta-layer specs">
      <div class="tal-icon">🤖</div>
      <div>
        <div class="tal-name">③ Specialists — each returns a <code>SpecialistResponse</code></div>
        <div class="tal-desc">research_agent, outline_agent, writer_agent, editor_agent, qa_agent. Each has its own input contract, its own system prompt, and returns the standard Level 3 envelope. Invisible to the top-level orchestrator.</div>
      </div>
    </div>
    <div class="ta-layer state">
      <div class="tal-icon">💾</div>
      <div>
        <div class="tal-name">④ Team-scoped state — isolated per run, per team</div>
        <div class="tal-desc">A <code>ContentTeamState</code> dataclass holding the run_id, completed stages, and team-internal artifacts. Never shared with other teams. Persisted to <code>runs/{run_id}/content/</code> — its own subdirectory, separate from every other team's state.</div>
      </div>
    </div>
    <div class="ta-layer output">
      <div class="tal-icon">📤</div>
      <div>
        <div class="tal-name">⑤ Output envelope — <code>TeamResponse</code></div>
        <div class="tal-desc">status, team="content_team", payload={"final_draft": str, "qa_report": dict}, meta. This is the only thing that crosses the team boundary. Internal artifacts stay inside the team.</div>
      </div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01 — CONTINUED</div>

## The Team Boundary Rule

One rule governs everything that crosses a team boundary — in either direction. Violating it at any layer is how teams become entangled and lose their independence.

<div class="compare-grid">
  <div class="cg-card bad">
    <div class="cg-head">❌ &nbsp;What must never cross a team boundary</div>
    <div class="cg-body">
      Internal artifacts — <code>research.json</code>, <code>outline.json</code>, <code>draft.md</code> — are produced inside the team for the team. They are never forwarded directly to another team or to the top-level orchestrator.<br><br>
      Team-internal state objects (<code>ContentTeamState</code>) are never passed outward. Another team's specialists are never called from inside this team. Internal routing decisions stay internal.
    </div>
  </div>
  <div class="cg-card good">
    <div class="cg-head">✅ &nbsp;What is allowed to cross a team boundary</div>
    <div class="cg-body">
      The <code>TeamResponse</code> envelope — and only the envelope — crosses outward. The top-level orchestrator's routing params cross inward at the entry point.<br><br>
      Global context (run_id, user_id, original intent) may be passed inward at call time. No internal artifact, state object, or specialist response ever crosses outward. The boundary is a one-way valve for anything internal.
    </div>
  </div>
</div>

<div class="highlight">

**The diagnostic test:** Can you replace the entire Content Team's internal implementation — swap every specialist, rewrite the pipeline sequence — without changing a single line of the top-level orchestrator? If yes, the boundary is correct. If no, something internal has leaked out.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02</div>

## Designing Inter-Team Handoffs

A task that spans two teams — for example, research content then deploy it as a web page — requires a handoff between the Content Team and the Engineering Team. That handoff always goes through the top-level orchestrator. Teams never call each other.

<div class="handoff-flow">
  <div class="hf-row top-level">
    <div class="hfr-num">1</div>
    <div class="hfr-actor">🌐 Top-Level Orch.</div>
    <div class="hfr-action">Receives user request: "Research quantum computing and publish a technical blog post." Parses intent — identifies this spans two teams: content first, then engineering.</div>
    <div class="hfr-artifact">routing_decision</div>
  </div>
  <div class="hf-row content-t">
    <div class="hfr-num">2</div>
    <div class="hfr-actor">✍️ Content Team</div>
    <div class="hfr-action">Receives params from top-level. Runs its full internal pipeline: research → outline → write → edit → QA. Returns <code>TeamResponse</code> with the final draft and QA report in the payload.</div>
    <div class="hfr-artifact">TeamResponse(ok)</div>
  </div>
  <div class="hf-row top-level">
    <div class="hfr-num">3</div>
    <div class="hfr-actor">🌐 Top-Level Orch.</div>
    <div class="hfr-action">Reads the Content Team's <code>TeamResponse</code>. Validates status is <code>ok</code>. Extracts <code>payload.final_draft</code>. Constructs Engineering Team params from the draft and the original deploy target.</div>
    <div class="hfr-artifact">extracts + builds</div>
  </div>
  <div class="hf-row eng-t">
    <div class="hfr-num">4</div>
    <div class="hfr-actor">⚙️ Engineering Team</div>
    <div class="hfr-action">Receives <code>{content: str, deploy_target: "web", format: "html"}</code> from top-level. Runs its internal pipeline: format → build → test → deploy. Returns its own <code>TeamResponse</code>.</div>
    <div class="hfr-artifact">TeamResponse(ok)</div>
  </div>
  <div class="hf-row validate">
    <div class="hfr-num">5</div>
    <div class="hfr-actor">🌐 Top-Level Orch.</div>
    <div class="hfr-action">Merges both team responses. Constructs the final caller response: draft written by Content Team, deployed at URL from Engineering Team. Both teams completed successfully.</div>
    <div class="hfr-artifact">→ final response</div>
  </div>
</div>

<div class="highlight">

**The top-level orchestrator is the courier.** It picks up the Content Team's output, extracts only what the Engineering Team needs, and delivers it. It never passes raw internal artifacts — only the fields from the <code>TeamResponse</code> payload that the next team's input contract requires.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 02 — CONTINUED</div>

## The Inter-Team Handoff Contract

When designing a multi-team task, define the handoff contract before writing either team. The contract answers three questions: what does Team B need, what does Team A's payload contain, and which fields map between them?

<div class="cheat-table-wrapper">
<table class="cheat-table">
  <thead>
    <tr><th>Question</th><th>Content Team (Team A)</th><th>Engineering Team (Team B)</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Entry point params</strong></td>
      <td><span class="mono">topic, audience, format, word_count</span></td>
      <td><span class="mono">content, deploy_target, output_format</span></td>
    </tr>
    <tr>
      <td><strong>Payload fields</strong></td>
      <td><span class="mono">final_draft (str), qa_report (dict)</span></td>
      <td><span class="mono">deploy_url (str), build_report (dict)</span></td>
    </tr>
    <tr>
      <td><strong>Handoff mapping</strong></td>
      <td colspan="2">Top-level maps: <span class="mono">A.payload.final_draft → B.params.content</span>. Nothing else from A is passed to B.</td>
    </tr>
    <tr>
      <td><strong>Failure handling</strong></td>
      <td>If A returns <span class="mono">status="error"</span>, top-level halts. B is never called.</td>
      <td>If A returns <span class="mono">status="flagged"</span>, top-level surfaces to caller before calling B.</td>
    </tr>
  </tbody>
</table>
</div>

<div class="matters-grid" style="margin-top: 0;">
  <div class="matters-card">
    <div class="mcc-icon">📝</div>
    <div>
      <div class="mcc-title">Write the handoff mapping before the teams</div>
      <div class="mcc-desc">The mapping — which field from Team A's payload feeds which param of Team B's entry point — is the interface between teams. If you can't write it before building the teams, the domain boundary isn't clear yet.</div>
    </div>
  </div>
  <div class="matters-card">
    <div class="mcc-icon">🔐</div>
    <div>
      <div class="mcc-title">Map only what Team B's contract requires</div>
      <div class="mcc-desc">Team B's entry point accepts <code>content, deploy_target, output_format</code>. Pass exactly those three fields — extracted from Team A's payload. The QA report, the outline, the research notes — all stay inside Team A. They are not Team B's concern.</div>
    </div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 03</div>

## Shared Context and Memory Across Teams

Not everything belongs inside a single team's state. Some information is genuinely shared across the entire run — the user's identity, the original request, the global run ID. Understanding the three tiers of context prevents both duplication and leakage.

<div class="context-tiers">
  <div class="ct-row global">
    <div class="ctr-tier">🌐 &nbsp;Global context</div>
    <div class="ctr-what">Run-level data that every team receives at call time and may read but never mutate. Passed in at the top-level entry point and forwarded to each team's entry function as a read-only struct.</div>
    <div class="ctr-scope">run_id, user_id,<br>original_intent,<br>session_preferences</div>
  </div>
  <div class="ct-row team">
    <div class="ctr-tier">🏢 &nbsp;Team context</div>
    <div class="ctr-what">Data that only one team produces and only that team uses internally. Lives in the team's scoped <code>RunState</code>. Never shared with other teams. Persisted to the team's own subdirectory under <code>runs/{run_id}/</code>.</div>
    <div class="ctr-scope">completed_stages,<br>team artifacts,<br>internal routing</div>
  </div>
  <div class="ct-row specialist">
    <div class="ctr-tier">🤖 &nbsp;Specialist context</div>
    <div class="ctr-what">Data that a single specialist uses for one call — its input params and the LLM's context window. Destroyed when the call ends. Never persisted. Never shared upward to the team orchestrator except through the <code>SpecialistResponse</code> envelope.</div>
    <div class="ctr-scope">input params,<br>LLM context window,<br>single call only</div>
  </div>
</div>

<div class="schema-block">
  <div class="sb-header">
    <div class="sb-title">GlobalContext — the read-only struct every team receives</div>
    <div class="sb-badge">contracts.py</div>
  </div>
  <div class="sb-body"><span class="sk">"run_id"</span>:            <span class="sv">"string — unique per top-level request"</span>,
<span class="sk">"user_id"</span>:           <span class="sv">"string | null — present for authenticated requests"</span>,
<span class="sk">"original_intent"</span>:  <span class="sv">"string — the raw user input, verbatim"</span>,
<span class="sk">"session_prefs"</span>: {
  <span class="sk">"language"</span>:         <span class="sv">"string — e.g. 'en-AU'"</span>,
  <span class="sk">"tone"</span>:             <span class="sv">"string — e.g. 'professional'"</span>
}                              <span class="sc">// teams read this — they never write to it</span></div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04</div>

## State Isolation — Preventing Context Rot Between Runs

Context rot is the Level 4 failure mode where state from one run leaks into a subsequent run — because the team's state was mutated rather than replaced, or because a shared object was modified in place. It produces subtle, hard-to-reproduce bugs.

<div class="isolation-grid">
  <div class="ig-col rot">
    <div class="igc-label">🦠 &nbsp;Context rot — how it happens</div>
    <div class="igc-item"><span>→</span> Team state is a module-level dict, mutated across calls. Run 2 inherits Run 1's artifact references.</div>
    <div class="igc-item"><span>→</span> <code>GlobalContext</code> object is shared by reference. A team mutates <code>ctx.session_prefs</code> in place — the mutation persists for all subsequent teams in the same run.</div>
    <div class="igc-item"><span>→</span> A specialist caches its last response at module level. Run 3 uses Run 1's cached research because the cache key was never invalidated.</div>
    <div class="igc-item"><span>→</span> The team's <code>completed_stages</code> list is never reset between runs. It grows across calls until the specialist it references no longer exists.</div>
  </div>
  <div class="ig-col clean">
    <div class="igc-label">✅ &nbsp;State isolation — how to enforce it</div>
    <div class="igc-item"><span>→</span> Team state is created fresh at the start of every team call: <code>state = ContentTeamState.new(run_id)</code>. Never a module-level singleton.</div>
    <div class="igc-item"><span>→</span> <code>GlobalContext</code> is a frozen Pydantic model. Any attempt to mutate it raises immediately. Teams receive a copy — never a reference.</div>
    <div class="igc-item"><span>→</span> Specialist responses are never cached at module level. Each call to a specialist function creates a new API call. Cache at the artifact layer — not the function layer.</div>
    <div class="igc-item"><span>→</span> State is persisted to a run-scoped path: <code>runs/{run_id}/content/state.json</code>. Loading a prior run's state requires an explicit <code>load_state(run_id)</code> call — never automatic.</div>
  </div>
</div>

<div class="highlight">

**The rule:** No team-level object survives a run boundary. Every team call starts with a fresh state, a frozen global context, and no assumptions about prior runs. If resuming a crashed run, load the last saved state explicitly — never rely on in-memory state from a previous execution.

</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 04 — CONTINUED</div>

## State Isolation in Code

<div class="code-block">
  <div class="cb-header">
    <div class="cb-dots">
      <div class="cb-dot red"></div>
      <div class="cb-dot yellow"></div>
      <div class="cb-dot green"></div>
    </div>
    <div class="cb-filename">teams/content/runner.py — state isolation pattern</div>
  </div>
  <div class="cb-body"><span class="kw">from</span> <span class="va">pydantic</span> <span class="kw">import</span> <span class="va">BaseModel</span>
<span class="kw">from</span> <span class="va">contracts</span> <span class="kw">import</span> <span class="va">GlobalContext</span>, <span class="va">TeamResponse</span>

<span class="kw">class</span> <span class="fn">ContentTeamState</span>(<span class="va">BaseModel</span>):
    <span class="va">run_id</span>:           <span class="va">str</span>
    <span class="va">completed_stages</span>: <span class="va">list</span>[<span class="va">str</span>] = []
    <span class="va">artifacts</span>:        <span class="va">dict</span>       = {}

    <span class="kw">@classmethod</span>
    <span class="kw">def</span> <span class="fn">new</span>(<span class="va">cls</span>, <span class="va">run_id</span>: <span class="va">str</span>) -> <span class="st">"ContentTeamState"</span>:
        <span class="kw">return</span> <span class="va">cls</span>(<span class="va">run_id</span>=<span class="va">run_id</span>)  <span class="cm"># always fresh — no defaults from prior runs</span>

<span class="kw">def</span> <span class="fn">run_content_team</span>(
    <span class="va">ctx</span>: <span class="va">GlobalContext</span>,             <span class="cm"># frozen — read-only</span>
    **<span class="va">params</span>
) -> <span class="va">TeamResponse</span>:

    <span class="cm"># ── Always create state fresh — never reuse ─────────────</span>
    <span class="va">state</span> = <span class="va">ContentTeamState</span>.<span class="fn">new</span>(<span class="va">ctx</span>.<span class="va">run_id</span>)

    <span class="cm"># ── ctx is a frozen model — mutation raises immediately ──</span>
    <span class="cm"># ctx.session_prefs["tone"] = "casual"  ← raises FrozenInstanceError</span>

    <span class="cm"># ── Run the internal pipeline with isolated state ───────</span>
    <span class="kw">return</span> <span class="fn">_run_pipeline</span>(<span class="va">ctx</span>, <span class="va">state</span>, <span class="va">params</span>)</div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05</div>

## The Generator + Critic Pattern at Team Scale

At Level 3, a single specialist can act as a critic — reviewing another specialist's output within the same pipeline. At Level 4, the Generator and Critic are full teams. The Generator Team produces a complete deliverable. The Critic Team evaluates it independently, with no shared internal state.

<div class="gc-flow">
  <div class="gcf-node n-input">
    <div class="gfn-icon">💬</div>
    <div class="gfn-type">Input</div>
    <div class="gfn-name">Request</div>
    <div class="gfn-sub">Original task<br>from top level</div>
  </div>
  <div class="gcf-arrow">→</div>
  <div class="gcf-node n-gen">
    <div class="gfn-icon">✍️</div>
    <div class="gfn-type">Generator Team</div>
    <div class="gfn-name">Produces</div>
    <div class="gfn-sub">Full draft,<br>plan, or code</div>
  </div>
  <div class="gcf-arrow">→</div>
  <div class="gcf-node n-artifact">
    <div class="gfn-icon">📄</div>
    <div class="gfn-type">TeamResponse</div>
    <div class="gfn-name">Payload</div>
    <div class="gfn-sub">Passed through<br>top-level orch.</div>
  </div>
  <div class="gcf-arrow">→</div>
  <div class="gcf-node n-critic">
    <div class="gfn-icon">🔍</div>
    <div class="gfn-type">Critic Team</div>
    <div class="gfn-name">Evaluates</div>
    <div class="gfn-sub">No access to<br>generator state</div>
  </div>
  <div class="gcf-arrow">→</div>
  <div class="gcf-node n-decide">
    <div class="gfn-icon">🔀</div>
    <div class="gfn-type">Top-Level</div>
    <div class="gfn-name">Decides</div>
    <div class="gfn-sub">Pass · Revise<br>Halt · Escalate</div>
  </div>
</div>

<div class="gc-loop-back">
  <div class="gc-loop-line"></div>
  ↺ &nbsp;if critic returns "revise" — top level re-routes to generator with critic notes
  <div class="gc-loop-line"></div>
</div>

<div class="gc-team-grid">
  <div class="gc-team-card gen">
    <div class="gctc-head">✍️ &nbsp;Generator Team — Content</div>
    <div class="gctc-body">
      <div class="gctc-row"><span class="gctr-tag">JOB</span><span class="gctr-text">Produce the best possible draft given the brief. Optimise for quality, not for passing evaluation.</span></div>
      <div class="gctc-row"><span class="gctr-tag">KNOWS</span><span class="gctr-text">Its own internal pipeline. The task params. Global context. Nothing about the Critic Team.</span></div>
      <div class="gctc-row"><span class="gctr-tag">RETURNS</span><span class="gctr-text"><code>TeamResponse(payload={"final_draft": str})</code> — always status "ok" or "error". Never self-evaluates.</span></div>
    </div>
    <div class="gctc-footer">never sees critic's rubric</div>
  </div>
  <div class="gc-team-card critic">
    <div class="gctc-head">🔍 &nbsp;Critic Team — QA &amp; Evaluation</div>
    <div class="gctc-body">
      <div class="gctc-row"><span class="gctr-tag">JOB</span><span class="gctr-text">Evaluate the draft against an explicit rubric. Return a verdict and specific, actionable revision notes.</span></div>
      <div class="gctc-row"><span class="gctr-tag">KNOWS</span><span class="gctr-text">The draft payload from the generator. The evaluation rubric. Global context. Nothing about how the draft was produced.</span></div>
      <div class="gctc-row"><span class="gctr-tag">RETURNS</span><span class="gctr-text"><code>TeamResponse(payload={"verdict": "pass"|"revise"|"reject", "notes": []})</code></span></div>
    </div>
    <div class="gctc-footer">never sees generator's internal state</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 05 — CONTINUED</div>

## Preventing Infinite Generator + Critic Loops

The Generator + Critic pattern introduces a revision loop. Without a ceiling, a Generator that can't satisfy the Critic's rubric loops forever — burning tokens on every turn. Three guards are mandatory.

<div class="walkthrough">
  <div class="wt-row">
    <div class="wr-num">1</div>
    <div class="wr-content">
      <div class="wrc-title">🔢 &nbsp;Set a maximum revision count — per run, not per request</div>
      <div class="wrc-desc">Define <code>MAX_REVISIONS = 2</code> as a named constant in the top-level runner. After two Critic evaluations, if the verdict is still "revise", the top level returns a <code>partial</code> status to the caller with the best draft produced so far. Never loop a third time silently.</div>
      <div class="wrc-code">if state.revision_count >= MAX_REVISIONS: return partial_response(best_draft)</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">2</div>
    <div class="wr-content">
      <div class="wrc-title">📋 &nbsp;Pass critic notes to generator — not the rubric</div>
      <div class="wrc-desc">When re-routing to the Generator Team, the top-level passes <code>critic_notes</code> — specific actionable feedback from the last Critic evaluation — not the full rubric. The Generator receives targeted revision instructions, not a chance to re-optimise from scratch.</div>
      <div class="wrc-code">generator_params["revision_notes"] = critic_response.payload["notes"]</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">3</div>
    <div class="wr-content">
      <div class="wrc-title">🛑 &nbsp;Treat "reject" as a halt, not a revision</div>
      <div class="wrc-desc">A Critic verdict of "reject" means the draft has a fundamental problem that revision won't fix — wrong topic, wrong format, factual contradiction with the research. The top level halts immediately and surfaces the rejection notes to the caller. Do not re-route to the Generator on "reject".</div>
      <div class="wrc-code">if verdict == "reject": return halt_response(critic_notes)</div>
    </div>
  </div>
  <div class="wt-row">
    <div class="wr-num">4</div>
    <div class="wr-content">
      <div class="wrc-title">📊 &nbsp;Log every revision cycle with a loop counter</div>
      <div class="wrc-desc">Each time the Generator is called with revision notes, log <code>revision=N</code> alongside the run_id. If token costs spike on a specific run_id, this log entry tells you immediately whether it's a Generator + Critic loop — without having to reconstruct the sequence from raw timestamps.</div>
      <div class="wrc-code">log("[GC_LOOP]", run_id=ctx.run_id, revision=state.revision_count)</div>
    </div>
  </div>
</div>

---

## Quick Reference — Part 2 Design Rules

Every decision made in this part, condensed to one table.

<table class="cheat-table">
  <thead>
    <tr><th>Decision</th><th>Rule</th><th>Where it lives</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Team boundary</strong></td>
      <td>Only <code>TeamResponse</code> crosses outward. Only routing params + global context cross inward.</td>
      <td>Architecture rule</td>
    </tr>
    <tr>
      <td><strong>Inter-team handoff</strong></td>
      <td>Always through the top-level orchestrator. Teams never call each other directly.</td>
      <td><span class="mono">top_level/runner.py</span></td>
    </tr>
    <tr>
      <td><strong>Handoff mapping</strong></td>
      <td>Define which TeamResponse payload field maps to which downstream team param — before building either team.</td>
      <td>Design document first</td>
    </tr>
    <tr>
      <td><strong>Global context</strong></td>
      <td>Frozen Pydantic model. Passed to every team. Read-only. Never mutated, never rebuilt mid-run.</td>
      <td><span class="mono">contracts.py → GlobalContext</span></td>
    </tr>
    <tr>
      <td><strong>Team state</strong></td>
      <td>Created fresh on every team call with <code>.new(run_id)</code>. Never a module-level singleton.</td>
      <td><span class="mono">teams/*/runner.py</span></td>
    </tr>
    <tr>
      <td><strong>Generator max revisions</strong></td>
      <td>Hard ceiling of 2 revision cycles. Exceeded → return <code>partial</code>. Never silent loop iteration 3.</td>
      <td><span class="mono">MAX_REVISIONS</span> constant</td>
    </tr>
    <tr>
      <td><strong>Critic "reject" verdict</strong></td>
      <td>Halt immediately. Surface rejection notes to caller. Never re-route to generator on "reject".</td>
      <td><span class="mono">top_level/runner.py</span></td>
    </tr>
  </tbody>
</table>

---

<!-- _class: final -->

# Teams own their internals. The top level owns the handoffs.

&nbsp;

*Fresh state every run. Frozen context everywhere. Two revision cycles maximum.*

&nbsp;

Next: **Part 3 — Shared Memory and Cross-Team Communication.**

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*