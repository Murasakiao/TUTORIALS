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
  section::after{font-family:'DM Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:1px;content:'CLAUDE CODE · /mcp · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);position:absolute;bottom:20px;right:40px;}
---

<!-- _class: cover -->

<div class="tag">Claude Code · Command 12</div>

# `/mcp`

Connect Claude to your real tools and data.

*The command that turns Claude Code into an agent with reach.*

---

<div class="header-row">
  <span class="page-num">— what it is —</span>
  <span class="page-label">model context protocol</span>
</div>

## What MCP is — in plain terms

MCP (Model Context Protocol) is a standard that lets Claude connect to external tools — GitHub, Notion, Slack, databases, file systems — using a single consistent interface. `/mcp` is how you manage those connections.

<div class="cards">
  <div class="card">
    <span class="card-icon">🔌</span>
    <h3>Like USB for AI tools</h3>
    <p>Once a tool has an MCP server, any MCP-compatible agent can use it. No custom integration per tool.</p>
  </div>
  <div class="card">
    <span class="card-icon">🌐</span>
    <h3>Real-world reach</h3>
    <p>Claude can read your GitHub issues, create Notion pages, query your database, or send Slack messages — directly from the terminal.</p>
  </div>
</div>

<div class="insight">
  <div class="insight-label">what /mcp manages</div>
  <p>Connect servers · Disconnect servers · Authenticate via OAuth · View connected tools · Check server status</p>
</div>

---

<div class="header-row">
  <span class="page-num">— what you can connect —</span>
  <span class="page-label">popular mcp servers</span>
</div>

## Tools with MCP servers today

<div class="cards-col">
  <div class="card-row">
    <span class="card-row-icon">💻</span>
    <div class="card-row-body">
      <h3>Dev tools</h3>
      <p>GitHub · GitLab · Linear · Jira · Sentry — read issues, create PRs, triage bugs from Claude Code.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">📋</span>
    <div class="card-row-body">
      <h3>Productivity</h3>
      <p>Notion · Google Drive · Confluence · Airtable — read and write docs, pages, and databases.</p>
    </div>
  </div>
  <div class="card-row">
    <span class="card-row-icon">💬</span>
    <div class="card-row-body">
      <h3>Communication</h3>
      <p>Slack · Gmail · Calendar — read threads, draft messages, check schedules without leaving the terminal.</p>
    </div>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— how it works —</span>
  <span class="page-label">connect and use</span>
</div>

## From connection to tool call

<div class="list">
  <div class="list-item">
    <span class="list-num">01</span>
    <span class="list-text"><strong>Run <code>/mcp</code></strong> — opens the MCP management interface showing connected and available servers</span>
  </div>
  <div class="list-item">
    <span class="list-num">02</span>
    <span class="list-text"><strong>Connect a server</strong> — enter the server URL or select from the registry. OAuth runs automatically if needed.</span>
  </div>
  <div class="list-item">
    <span class="list-num">03</span>
    <span class="list-text"><strong>Tools appear as commands</strong> — each server's tools become available as <code>/mcp__servername__action</code></span>
  </div>
  <div class="list-item">
    <span class="list-num">04</span>
    <span class="list-text"><strong>Claude calls them in tasks</strong> — when you describe a task, Claude reads tool descriptions and picks the right one</span>
  </div>
</div>

---

<div class="header-row">
  <span class="page-num">— tips —</span>
  <span class="page-label">use mcp well</span>
</div>

## Getting the most from `/mcp`

<div class="cards">
  <div class="card">
    <span class="card-icon">🎯</span>
    <h3>Be explicit in prompts</h3>
    <p>Don't assume Claude will reach for the MCP tool. Say: <em>"Use the GitHub MCP server to list open issues labeled bug."</em></p>
  </div>
  <div class="card">
    <span class="card-icon">✂️</span>
    <h3>Connect only what you need</h3>
    <p>Each connected server adds tool descriptions to your context. Only connect servers relevant to the current task.</p>
  </div>
  <div class="card">
    <span class="card-icon">🧪</span>
    <h3>Test with a simple task first</h3>
    <p>After connecting, ask Claude to list available tools from the server before using it for real work. Verify it's working.</p>
  </div>
  <div class="card">
    <span class="card-icon">🔒</span>
    <h3>Review permissions carefully</h3>
    <p>MCP servers with write access can act on real systems. Understand exactly what each server can do before connecting it.</p>
  </div>
</div>

---

<!-- _class: cta -->

<div class="tag" style="justify-content:center;color:#0a0a0a;margin-bottom:20px;">Claude Code · /mcp</div>

# Claude in your terminal.<br>Connected to your world.

## Set up one MCP server this week.

<p>Start with GitHub or Notion — whichever you open most. Connect it. Tell Claude to use it explicitly. See what changes.</p>

<div class="handle">Claude Code · Power Tools</div>