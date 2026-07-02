#!/usr/bin/env python3
"""
Schedule email delivery of terminal tutorial content.

Sends one tutorial from the terminal/ folder per run.
Intended to be triggered daily via cron.

Usage:
    python schedule_terminal_emails.py              # send next unsent
    python schedule_terminal_emails.py --list        # list all tutorials
    python schedule_terminal_emails.py --reset       # reset send tracking
    python schedule_terminal_emails.py --all         # send all immediately
    python schedule_terminal_emails.py --file "Mac Terminal.md"  # send specific

Setup:
    1. Create a .env file in this directory (see .env.example)
    2. Run once to test:  python schedule_terminal_emails.py
    3. Add to crontab for daily delivery:
       0 8 * * * /usr/local/bin/python3 /path/to/schedule_terminal_emails.py
"""

import os
import re
import sys
import json
import smtplib
import argparse
from pathlib import Path
from email.mime.text import MIMEText

TERMINAL_DIR = Path(__file__).parent / "terminal"
TRACKING_FILE = Path(__file__).parent / "_email_progress.json"
ENV_FILE = Path(__file__).parent / ".env"

TUTORIALS = [
    "Mac Terminal.md",
    "Windows Terminal.md",
    "Install VS Code.md",
    "Install VS Code: Windows.md",
    "Markdown.md",
    "What is a Browser.md",
    "DevTools CSS Inspection.md",
]

SIGNATURE = """
<hr>
<p style="color:#6b7280; font-size: 12px;">
  <strong>Zero to AI Builder</strong> — by @juliusdarang<br>
  <a href="[gumroad-link]">Get the full course →</a>
</p>
"""


def load_env():
    """Load .env file manually (zero external dependencies)."""
    if not ENV_FILE.exists():
        print(f"ERROR: {ENV_FILE} not found. Create it from .env.example")
        sys.exit(1)

    env = {}
    for line in ENV_FILE.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        env[key.strip()] = val.strip().strip('"').strip("'")

    required = ["GMAIL_SENDER", "GMAIL_APP_PW", "GMAIL_RECEIVER"]
    missing = [k for k in required if k not in env]
    if missing:
        print(f"ERROR: Missing env vars: {', '.join(missing)}")
        sys.exit(1)

    return env


def load_tracking():
    """Load the send progress tracker."""
    if TRACKING_FILE.exists():
        return json.loads(TRACKING_FILE.read_text())
    return {"sent": [], "current_index": 0}


def save_tracking(tracking):
    """Persist the send progress tracker."""
    TRACKING_FILE.write_text(json.dumps(tracking, indent=2))


def extract_title(filepath):
    """Extract the tutorial title (H1 after <!-- _class: cover -->) from a MARP file."""
    text = filepath.read_text()
    match = re.search(r'<!-- _class: cover -->\s*\n\s*#\s+(.+?)(?:\n|$)', text)
    if match:
        return match.group(1).strip()
    return filepath.stem


def strip_frontmatter_and_css(text):
    """Remove YAML frontmatter (---...---) and <style>...</style> blocks."""
    text = re.sub(r'^---\n.*?\n---\n', '', text, count=1, flags=re.DOTALL)
    text = re.sub(r'<style>.*?</style>', '', text, flags=re.DOTALL)
    return text


def markdown_to_simple_html(md_text):
    """Convert a subset of markdown to basic HTML for email."""
    html = md_text

    html = re.sub(r'^###\s+(.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^##\s+(.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^#\s+(.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)

    html = re.sub(r'^-{3,}', r'<hr>', html)

    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)

    html = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', html)

    html = re.sub(r'^-\s+(.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)

    html = re.sub(r'(<li>.*?</li>(\s*<li>.*?</li>)*)', r'<ul>\1</ul>', html, flags=re.DOTALL)

    html = re.sub(r'\n\n', r'</p><p>', html)
    html = '<p>' + html + '</p>'
    html = re.sub(r'<p>\s*</p>', '', html)

    return html


def build_email_body(filepath, title):
    """Build the HTML email body for a given tutorial file."""
    text = filepath.read_text()
    clean = strip_frontmatter_and_css(text)

    lines = clean.split("\n")
    content_start = 0
    for i, line in enumerate(lines):
        if line.strip().startswith("<!-- _class: cover -->"):
            content_start = i + 1
            break

    body_lines = []
    for line in lines[content_start:]:
        stripped = line.strip()
        if stripped.startswith("<!--"):
            continue
        if stripped == "&nbsp;":
            continue
        if stripped.startswith("---"):
            continue
        body_lines.append(line)

    body_md = "\n".join(body_lines).strip()
    body_html = markdown_to_simple_html(body_md)

    return f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {{ font-family: 'DM Sans', -apple-system, sans-serif; color: #111827; line-height: 1.6; max-width: 600px; margin: 0 auto; padding: 20px; }}
    h1 {{ font-size: 24px; color: #111827; margin-bottom: 8px; }}
    h2 {{ font-size: 20px; color: #2563eb; border-bottom: 2px solid #2563eb; padding-bottom: 8px; margin-top: 24px; }}
    h3 {{ font-size: 16px; color: #2563eb; margin-top: 20px; }}
    code {{ font-family: 'DM Mono', monospace; background: #f3f4f6; padding: 2px 6px; border-radius: 4px; font-size: 14px; color: #d97706; }}
    pre {{ background: #f3f4f6; padding: 12px; border-radius: 6px; overflow-x: auto; }}
    hr {{ border: none; border-top: 1px solid #e5e7eb; margin: 24px 0; }}
    ul {{ padding-left: 20px; }}
    li {{ margin-bottom: 6px; }}
    .header {{ background: #eff6ff; padding: 20px; border-radius: 8px; margin-bottom: 20px; }}
    .header h1 {{ margin: 0 0 4px; color: #2563eb; }}
    .header p {{ margin: 0; color: #6b7280; font-size: 14px; }}
  </style>
</head>
<body>
  <div class="header">
    <h1>{title}</h1>
    <p>Zero to AI Builder — Terminal &amp; Tools</p>
  </div>
  {body_html}
  {SIGNATURE}
</body>
</html>"""


def send_email(env, subject, body_html):
    """Send an email via Gmail SMTP."""
    msg = MIMEText(body_html, "html")
    msg["Subject"] = subject
    msg["From"] = env["GMAIL_SENDER"]
    msg["To"] = env["GMAIL_RECEIVER"]

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(env["GMAIL_SENDER"], env["GMAIL_APP_PW"])
        smtp.sendmail(env["GMAIL_SENDER"], env["GMAIL_RECEIVER"], msg.as_string())

    print(f"Sent: {subject}")


def list_tutorials():
    """Print all tutorials and their send status."""
    tracking = load_tracking()
    print(f"{'Status':<8} {'#':<3} Tutorial")
    print("-" * 50)
    for i, fname in enumerate(TUTORIALS):
        fpath = TERMINAL_DIR / fname
        title = extract_title(fpath) if fpath.exists() else fname
        sent = "✅" if fname in tracking["sent"] else "  "
        print(f"{sent:<8} {i+1:<3} {title}")


def send_tutorial(tracking, env, fname):
    """Send a single tutorial by filename."""
    fpath = TERMINAL_DIR / fname
    if not fpath.exists():
        print(f"ERROR: {fpath} not found")
        return False

    title = extract_title(fpath)
    body = build_email_body(fpath, title)
    subject = f"Zero to AI Builder — {title}"

    send_email(env, subject, body)

    if fname not in tracking["sent"]:
        tracking["sent"].append(fname)
    save_tracking(tracking)
    return True


def main():
    parser = argparse.ArgumentParser(description="Email terminal tutorials one at a time.")
    parser.add_argument("--list", action="store_true", help="List all tutorials and status")
    parser.add_argument("--reset", action="store_true", help="Reset send tracking")
    parser.add_argument("--all", action="store_true", help="Send all unsent tutorials now")
    parser.add_argument("--file", type=str, help="Send a specific tutorial by filename")
    args = parser.parse_args()

    env = load_env()
    tracking = load_tracking()

    if args.list:
        list_tutorials()
        return

    if args.reset:
        tracking = {"sent": [], "current_index": 0}
        save_tracking(tracking)
        print("Tracking reset. All tutorials marked as unsent.")
        return

    if args.file:
        send_tutorial(tracking, env, args.file)
        return

    if args.all:
        for fname in TUTORIALS:
            if fname not in tracking["sent"]:
                send_tutorial(tracking, env, fname)
            else:
                print(f"Skipped (already sent): {fname}")
        return

    index = tracking.get("current_index", 0)
    if index >= len(TUTORIALS):
        print("All tutorials sent. Use --reset to start over or check _email_progress.json")
        return

    fname = TUTORIALS[index]
    send_tutorial(tracking, env, fname)

    tracking["current_index"] = index + 1
    save_tracking(tracking)

    remaining = len(TUTORIALS) - tracking["current_index"]
    print(f"{remaining} tutorial(s) remaining.")


if __name__ == "__main__":
    main()
