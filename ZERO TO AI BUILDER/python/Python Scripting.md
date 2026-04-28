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

  /* Terminal — Mac style */
  .terminal {
    background: #111827;
    border-radius: 10px;
    overflow: hidden;
    margin: 12px 0;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .terminal-bar {
    background: #1f2937;
    padding: 9px 16px;
    display: flex;
    align-items: center;
    gap: 7px;
  }

  .terminal-bar .dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    display: inline-block;
  }

  .terminal-bar .dot.red    { background: #ef4444; }
  .terminal-bar .dot.yellow { background: #f59e0b; }
  .terminal-bar .dot.green  { background: #22c55e; }

  .terminal-bar .title {
    font-size: 12px;
    color: #6b7280;
    margin-left: 8px;
  }

  .terminal-body {
    padding: 14px 20px;
    line-height: 2;
  }

  .terminal-body .prompt { color: #22c55e; }
  .terminal-body .cmd    { color: #f9fafb; }
  .terminal-body .out    { color: #9ca3af; }
  .terminal-body .out-g  { color: #86efac; }
  .terminal-body .out-y  { color: #fde68a; }
  .terminal-body .cmt    { color: #4b5563; font-style: italic; }

  /* Code block with syntax highlighting */
  .code-block {
    background: #111827;
    border-radius: 8px;
    padding: 16px 22px;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #e5e7eb;
    line-height: 2;
    margin: 12px 0;
  }

  .code-block .kw   { color: #c4b5fd; }  /* import, for, in, os  */
  .code-block .fn   { color: #60a5fa; }  /* function calls        */
  .code-block .str  { color: #86efac; }  /* strings               */
  .code-block .var  { color: #f9fafb; }  /* variables             */
  .code-block .cmt  { color: #4b5563; font-style: italic; }
  .code-block .num  { color: #fde68a; }  /* numbers               */
  .code-block .op   { color: #f9a8d4; }  /* operators + f-string  */

  /* Before / after file name comparison */
  .file-compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 16px 0;
  }

  .file-col {
    background: #111827;
    border-radius: 8px;
    padding: 14px 18px;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    line-height: 2;
  }

  .file-col .col-label {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 8px;
    font-style: normal;
  }

  .file-col.before .col-label { color: #f87171; }
  .file-col.after  .col-label { color: #86efac; }
  .file-col.before .fname     { color: #f87171; }
  .file-col.after  .fname     { color: #86efac; }

  /* Tweak table */
  .tweak-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
    margin: 12px 0;
  }

  .tweak-table th {
    background: var(--text);
    color: white;
    padding: 8px 14px;
    text-align: left;
    font-weight: 500;
    font-size: 12px;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.05em;
  }

  .tweak-table td {
    padding: 9px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
    font-size: 13px;
  }

  .tweak-table tr:nth-child(even) td { background: var(--off-white); }
  .tweak-table .mono {
    font-family: 'DM Mono', monospace;
    color: var(--blue);
    font-size: 12px;
  }

  /* Next steps card grid */
  .next-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
  }

  .next-card {
    background: var(--off-white);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 14px 16px;
  }

  .next-card .next-title {
    font-weight: 600;
    font-size: 14px;
    color: var(--text);
    margin-bottom: 4px;
  }

  .next-card .next-desc {
    font-size: 12px;
    color: var(--muted);
    line-height: 1.5;
  }

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

# Your First Python Script
## Automate Renaming Files

&nbsp;

**Stop doing it by hand.** Write it once, run it forever.

`os` · `rename` · `for loop` · `f-string`

---

## The Problem

You have 100 photos from your camera. They're named like this:

<div class="file-compare">
  <div class="file-col before">
    <div class="col-label">❌ Before</div>
    <div class="fname">IMG_4021.jpg</div>
    <div class="fname">IMG_4022.jpg</div>
    <div class="fname">IMG_4023.jpg</div>
    <div class="fname">IMG_4024.jpg</div>
    <div class="fname">IMG_4025.jpg</div>
  </div>
  <div class="file-col after">
    <div class="col-label">✅ After</div>
    <div class="fname">photo_001.jpg</div>
    <div class="fname">photo_002.jpg</div>
    <div class="fname">photo_003.jpg</div>
    <div class="fname">photo_004.jpg</div>
    <div class="fname">photo_005.jpg</div>
  </div>
</div>

Doing this by hand = 100 clicks, 100 chances to make a typo.
Writing a script = 20 lines, runs in under a second, works on 10,000 files just as easily.

---

<!-- _class: step -->

<div class="step-badge">CONCEPT 01</div>

## The `os` Module

Python can't touch your files out of the box — you need to import a module first.

<div class="code-block">
  <span class="kw">import</span> <span class="var">os</span> &nbsp;<span class="cmt"># gives Python access to your file system</span>
</div>

`os` is part of Python's standard library — no pip install needed. It ships with every Python installation.

<div class="tools">
  <div class="tool-card">
    <div class="icon">📂</div>
    <div class="name">os.listdir()</div>
    <div class="desc">Returns a list of every file and folder in a directory.</div>
  </div>
  <div class="tool-card">
    <div class="icon">✏️</div>
    <div class="name">os.rename()</div>
    <div class="desc">Renames a file. Takes the old name and the new name as arguments.</div>
  </div>
  <div class="tool-card">
    <div class="icon">📍</div>
    <div class="name">os.chdir()</div>
    <div class="desc">Changes the working directory — tells Python which folder to operate in.</div>
  </div>
  <div class="tool-card">
    <div class="icon">🔗</div>
    <div class="name">os.path.join()</div>
    <div class="desc">Safely combines folder paths and filenames across Mac and Windows.</div>
  </div>
</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 01</div>

## Write the Script — Part 1

Create a new file called `rename.py`. Start by importing `os` and pointing it at your folder:

<div class="code-block">
  <span class="kw">import</span> <span class="var">os</span><br>
  <br>
  <span class="cmt"># Change this to the folder you want to rename files in</span><br>
  <span class="var">folder</span> <span class="op">=</span> <span class="str">"/Users/julius/Desktop/photos"</span><br>
  <br>
  <span class="cmt"># Get a sorted list of all files in that folder</span><br>
  <span class="var">files</span> <span class="op">=</span> <span class="fn">sorted</span>(<span class="fn">os.listdir</span>(<span class="var">folder</span>))<br>
  <br>
  <span class="cmt"># Preview what Python sees before doing anything</span><br>
  <span class="fn">print</span>(<span class="var">files</span>)
</div>

Run this first — before any renaming happens — to confirm Python is looking at the right folder and the right files.

<div class="highlight">

**Safe habit:** always preview before you rename. `print()` costs nothing. Undoing 100 bad renames costs a lot.

</div>

---

<!-- _class: step -->

<div class="step-badge">STEP 02</div>

## Write the Script — Part 2

Now add the renaming loop:

<div class="code-block">
  <span class="kw">import</span> <span class="var">os</span><br>
  <br>
  <span class="var">folder</span> <span class="op">=</span> <span class="str">"/Users/julius/Desktop/photos"</span><br>
  <span class="var">files</span> <span class="op">=</span> <span class="fn">sorted</span>(<span class="fn">os.listdir</span>(<span class="var">folder</span>))<br>
  <br>
  <span class="kw">for</span> <span class="var">i</span>, <span class="var">filename</span> <span class="kw">in</span> <span class="fn">enumerate</span>(<span class="var">files</span>, <span class="num">start</span><span class="op">=</span><span class="num">1</span>):<br>
  &nbsp;&nbsp;<span class="var">ext</span> <span class="op">=</span> <span class="fn">os.path.splitext</span>(<span class="var">filename</span>)[<span class="num">1</span>] &nbsp;<span class="cmt"># grab ".jpg"</span><br>
  &nbsp;&nbsp;<span class="var">new_name</span> <span class="op">=</span> <span class="op">f"</span><span class="str">photo_</span><span class="op">{</span><span class="var">i</span><span class="op">:03d}{</span><span class="var">ext</span><span class="op">}"</span> &nbsp;<span class="cmt"># photo_001.jpg</span><br>
  &nbsp;&nbsp;<span class="var">old_path</span> <span class="op">=</span> <span class="fn">os.path.join</span>(<span class="var">folder</span>, <span class="var">filename</span>)<br>
  &nbsp;&nbsp;<span class="var">new_path</span> <span class="op">=</span> <span class="fn">os.path.join</span>(<span class="var">folder</span>, <span class="var">new_name</span>)<br>
  &nbsp;&nbsp;<span class="fn">os.rename</span>(<span class="var">old_path</span>, <span class="var">new_path</span>)<br>
  &nbsp;&nbsp;<span class="fn">print</span>(<span class="op">f"</span><span class="str">Renamed: </span><span class="op">{</span><span class="var">filename</span><span class="op">}</span><span class="str"> → </span><span class="op">{</span><span class="var">new_name</span><span class="op">}"</span>)
</div>

`{i:03d}` pads the number to 3 digits — so you get `001`, `002` instead of `1`, `2`.

---

<!-- _class: step -->

<div class="step-badge">STEP 03</div>

## Run It

Save `rename.py` in any folder, then run it from Terminal (Mac) or CMD (Windows):

<div class="terminal">
  <div class="terminal-bar">
    <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
    <span class="title">zsh — Terminal</span>
  </div>
  <div class="terminal-body">
    <span class="prompt">~ %</span> <span class="cmd">python3 rename.py</span><br>
    <span class="out-g">Renamed: IMG_4021.jpg → photo_001.jpg</span><br>
    <span class="out-g">Renamed: IMG_4022.jpg → photo_002.jpg</span><br>
    <span class="out-g">Renamed: IMG_4023.jpg → photo_003.jpg</span><br>
    <span class="out">...</span>
  </div>
</div>

<div class="highlight warn">

⚠️ **This is permanent.** `os.rename()` does not move files to Trash — it renames them in place immediately. Test on a copy of your folder first if you're unsure.

</div>

---

## What to Tweak

One script — many use cases. Change two values and it handles any batch rename job:

<table class="tweak-table">
  <tr>
    <th>What to change</th>
    <th>Line to edit</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>Target folder</td>
    <td class="mono">folder = "..."</td>
    <td>Any path on your machine</td>
  </tr>
  <tr>
    <td>Prefix word</td>
    <td class="mono">f"photo_{i:03d}{ext}"</td>
    <td>Change <code>photo</code> to <code>invoice</code>, <code>scan</code>, etc.</td>
  </tr>
  <tr>
    <td>Number padding</td>
    <td class="mono">:03d</td>
    <td><code>:02d</code> → 01, 02 &nbsp;·&nbsp; <code>:04d</code> → 0001, 0002</td>
  </tr>
  <tr>
    <td>Filter by type</td>
    <td>add <code>if filename.endswith(".jpg")</code></td>
    <td>Only rename JPGs, skip other files</td>
  </tr>
  <tr>
    <td>Starting number</td>
    <td class="mono">enumerate(files, start=1)</td>
    <td>Change <code>1</code> to <code>100</code> to start at 100</td>
  </tr>
</table>

---

## Where to Go Next

You just used a loop, a module, f-strings, and file I/O — the core of 90% of Python scripts.

<div class="next-grid">
  <div class="next-card">
    <div class="next-title">🗂️ Move files too</div>
    <div class="next-desc">Use <code>shutil.move()</code> to rename and relocate in one step.</div>
  </div>
  <div class="next-card">
    <div class="next-title">📋 Read from a list</div>
    <div class="next-desc">Load new names from a <code>.txt</code> or <code>.csv</code> file instead of generating them.</div>
  </div>
  <div class="next-card">
    <div class="next-title">🔍 Use regex</div>
    <div class="next-desc">Import <code>re</code> to match and replace patterns inside filenames.</div>
  </div>
  <div class="next-card">
    <div class="next-title">↩️ Add an undo</div>
    <div class="next-desc">Write a <code>log.csv</code> of old → new names so you can reverse the script.</div>
  </div>
  <div class="next-card">
    <div class="next-title">🖥️ Add a dry run</div>
    <div class="next-desc">Add a <code>dry_run = True</code> flag that prints renames without executing them.</div>
  </div>
  <div class="next-card">
    <div class="next-title">📁 Walk subfolders</div>
    <div class="next-desc">Use <code>os.walk()</code> to recurse into nested folders automatically.</div>
  </div>
</div>

---

<!-- _class: final -->

# One script.
# Zero manual work.

&nbsp;

This is what Python is for — turning repetitive tasks into a single command.

&nbsp;

**Check out my other tutorials →**
*More things you can build with AI*