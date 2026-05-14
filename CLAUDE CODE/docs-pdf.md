---
marp: true
paginate: true
html: true
size: 4:3
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,400;0,500;0,600;1,400&family=DM+Mono:wght@400;500&display=swap');
  :root{--amber:#f59e0b;--amber-dim:#d97706;--green:#22c55e;--blue:#60a5fa;--purple:#c4b5fd;--white:#f1f5f9;--off-white:#cbd5e1;--subtle:#94a3b8;--muted:#64748b;--bg:#080808;--card-bg:#111111;--card-border:#222222;}
  section{font-family:'DM Sans',sans-serif;background:var(--bg);color:var(--white);padding:44px 52px;box-sizing:border-box;display:flex;flex-direction:column;overflow:hidden;position:relative;}
  h1{font-size:38px;font-weight:700;line-height:1.08;margin:0 0 14px;color:var(--white);letter-spacing:-1.5px;}
  h2{font-size:28px;font-weight:700;line-height:1.1;margin:0 0 14px;color:var(--white);letter-spacing:-1px;border:none;}
  p{font-size:16px;line-height:1.6;color:var(--subtle);margin:0 0 12px;}
  strong{color:var(--white);font-weight:600;}em{color:var(--muted);font-style:normal;}
  code{font-family:'DM Mono',monospace;background:var(--card-bg);border:1px solid var(--card-border);color:var(--amber);padding:1px 6px;border-radius:4px;font-size:.88em;}
  .tag{display:flex;align-items:center;gap:12px;font-family:'DM Mono',monospace;font-size:11px;font-weight:500;letter-spacing:3px;color:var(--amber);text-transform:uppercase;margin-bottom:18px;}
  .tag::before{content:'';display:block;width:24px;height:2px;background:var(--amber);flex-shrink:0;}
  .tag.purple{color:var(--purple);}.tag.purple::before{background:var(--purple);}
  .header-row{display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;}
  .page-num{font-family:'DM Mono',monospace;font-size:10px;color:var(--amber-dim);letter-spacing:2px;text-transform:uppercase;}
  .page-label{font-family:'DM Mono',monospace;font-size:10px;color:var(--muted);}
  .cards{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px;}
  .card{background:var(--card-bg);border:1px solid var(--card-border);border-radius:10px;padding:14px;}
  .card-icon{font-size:17px;margin-bottom:6px;display:block;}
  .card h3{font-size:14px;font-weight:600;color:var(--white);margin:0 0 4px;}
  .card p{font-size:13px;color:var(--subtle);line-height:1.45;margin:0;}
  .cards-col{display:flex;flex-direction:column;gap:8px;margin-bottom:12px;}
  .card-row{background:var(--card-bg);border:1px solid var(--card-border);border-radius:10px;padding:12px 16px;display:flex;align-items:flex-start;gap:12px;}
  .card-row-icon{font-size:17px;flex-shrink:0;margin-top:1px;}
  .card-row-body h3{font-size:14px;font-weight:600;color:var(--white);margin:0 0 3px;}
  .card-row-body p{font-size:13px;color:var(--subtle);margin:0;line-height:1.45;}
  .compare{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:10px;}
  .compare-col{background:var(--card-bg);border:1px solid var(--card-border);border-radius:10px;padding:14px 16px;}
  .compare-col.good{border-color:#14532d;}
  .compare-label{font-family:'DM Mono',monospace;font-size:9px;letter-spacing:3px;text-transform:uppercase;margin-bottom:6px;color:var(--muted);}
  .compare-label.bad{color:#ef4444;}.compare-label.good{color:var(--green);}
  .compare-col h3{font-size:14px;font-weight:600;color:var(--white);margin:0 0 5px;}
  .compare-col p{font-size:13px;color:var(--subtle);line-height:1.45;margin:0;}
  .list{display:flex;flex-direction:column;gap:7px;margin-bottom:12px;}
  .list-item{display:flex;align-items:flex-start;gap:12px;background:var(--card-bg);border:1px solid var(--card-border);border-radius:8px;padding:10px 14px;}
  .list-num{font-family:'DM Mono',monospace;font-size:11px;color:var(--amber);flex-shrink:0;margin-top:1px;min-width:18px;}
  .list-text{font-size:13.5px;color:var(--subtle);line-height:1.45;}
  .list-text strong{color:var(--white);}
  .insight{background:var(--card-bg);border:1px solid var(--card-border);border-radius:10px;padding:12px 18px;margin-top:auto;}
  .insight-label{font-family:'DM Mono',monospace;font-size:9px;letter-spacing:3px;color:var(--muted);text-transform:uppercase;margin-bottom:4px;}
  .insight p{font-size:14px;color:var(--off-white);line-height:1.5;margin:0;}
  section.cover{justify-content:flex-end;padding-bottom:80px;background:#050505;}
  section.cover h1{font-size:48px;}
  section.cover p{font-size:17px;color:var(--subtle);}
  section.cta{justify-content:center;align-items:center;text-align:center;background:var(--amber);}
  section.cta h1{color:#0F0F0F;font-size:40px;letter-spacing:-1px;margin-bottom:10px;}
  section.cta h2{color:#3a2e00;font-size:22px;border:none;margin-bottom:12px;}
  section.cta p{color:#5a4700;font-size:16px;max-width:540px;margin:0;}
  section.cta .handle{font-family:'DM Mono',monospace;font-size:13px;color:#7a6000;margin-top:22px;letter-spacing:2px;text-transform:uppercase;}
  section::after{font-family:'DM Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:1px;content:'CLAUDE CODE · File Skills · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);position:absolute;bottom:20px;right:40px;}
---

<!-- _class: cover -->

<div class="tag purple">Claude Code · Commands 15–17 · Skills</div>

# `/docx` `/pdf` `/pptx`

Professional documents — straight from the terminal.

*Three skills. One job: generate real files without leaving Claude Code.*

---

<div class="header-row">
  <span class="page-num">— what they are —</span>
  <span class="page-label">skill-based file generation</span>
</div>

## Why these are skills, not built-ins

These three commands are **skills** — when you run them, Claude reads a detailed playbook (a SKILL.md file) that teaches it exactly how to generate each file format correctly: right libraries, right page sizes, right structure, production-ready output.

<div class="cards">
  <div class="card">
    <span class="card-icon">📝</span>
    <h3>/docx</h3>
    <p>Word documents. Tables, headings, TOC, images, headers/footers. Compatible with Microsoft Word and Google Docs.</p>
  </div>
  <div class="card">
    <span class="card-icon">📄</span>
    <h3>/pdf</h3>
    <p>Create, fill, merge, split, watermark, and extract from PDFs. Handles scanned documents with OCR.</p>
  </div>
  <div class="card">
    <span class="card-icon">📊</span>
    <h3>/pptx</h3>
    <p>Full slide decks with layouts, speaker notes, transitions, and images — from a plain text description.</p>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— /docx —</span>
  <span class="page-label">word documents</span>
</div>

## What `/docx` can generate

<div class="cards-col">
  <div class="card-row">
    <span class="card-row-icon">📋</span>
    <div class="card-row-body">
      <h3>Structured reports</h3>
      <p>Table of contents, numbered headings, page numbers, headers and footers — proper Word structure, not just styled text.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">📊</span>
    <div class="card-row-body">
      <h3>Tables and data layouts</h3>
      <p>Multi-column tables with proper cell widths, shading, borders, and alignment. Works correctly in both Word and Google Docs.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">🖼️</span>
    <div class="card-row-body">
      <h3>Documents with images</h3>
      <p>Embed images with alt text, captions, and correct positioning — not pasted inline, but properly placed in the OOXML structure.</p>
    </div>
  </div>
</div>

<div class="insight">
  <div class="insight-label">prompt tip</div>
  <p>Describe the document's purpose and structure. Claude handles the formatting: <em>"Create a project proposal with an executive summary, three sections, and a budget table."</em></p>
</div>

---

<div class="header-row">
  <span class="page-num">— /pdf and /pptx —</span>
  <span class="page-label">the other two</span>
</div>

## `/pdf` and `/pptx` capabilities

<div class="compare">
  <div class="compare-col">
    <div class="compare-label">/pdf</div>
    <h3>More than just creation</h3>
    <p>Create new PDFs · Fill existing forms · Merge multiple PDFs · Split into separate files · Add watermarks · Extract text · OCR scanned documents</p>
  </div>
  <div class="compare-col good">
    <div class="compare-label good">/pptx</div>
    <h3>Full slide decks</h3>
    <p>Generate a complete presentation from a description · Title and content slides · Speaker notes · Image placeholders · Slide layouts · Theme-consistent output</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">for /pptx</div>
  <p>Describe your slide deck topic, number of slides, and key points per slide. Claude generates the full deck from a plain-language brief.</p>
</div>

---

<div class="header-row">
  <span class="page-num">— tips —</span>
  <span class="page-label">get better output</span>
</div>

## Getting the best results from file skills

<div class="cards">
  <div class="card">
    <span class="card-icon">📝</span>
    <h3>Describe structure, not formatting</h3>
    <p><em>"A report with an executive summary, three sections, and a conclusion"</em> — not "make it bold and 14pt." Claude handles formatting.</p>
  </div>
  <div class="card">
    <span class="card-icon">📁</span>
    <h3>Specify the output path</h3>
    <p>Tell Claude where to save: <em>"Save it as /reports/q3-summary.docx"</em> — otherwise it picks a default location.</p>
  </div>
  <div class="card">
    <span class="card-icon">🔄</span>
    <h3>Iterate with plain language</h3>
    <p>After the first output: <em>"Add a cover page and make the table span the full width."</em> Skills understand revision prompts.</p>
  </div>
  <div class="card">
    <span class="card-icon">📂</span>
    <h3>Reference existing files</h3>
    <p>For /pdf: <em>"Merge invoice.pdf and receipt.pdf into one file."</em> Point to real files — Claude reads them directly.</p>
  </div>
</div>

---

<!-- _class: cta -->

<div class="tag" style="justify-content:center;color:#0a0a0a;margin-bottom:20px;">Claude Code · /docx /pdf /pptx</div>

# Professional files.<br>No apps needed.

## Describe what you need. Get a real document.

<p>Run <code>/docx</code>, <code>/pdf</code>, or <code>/pptx</code> — then describe your document. Claude reads the playbook and generates production-ready output.</p>

<div class="handle">Claude Code · File Skills</div>