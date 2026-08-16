#!/usr/bin/env python3
"""
Schedule email delivery of tutorial content from any folder.

Sends one tutorial per run, tracking progress per folder.
Intended to be triggered daily via cron, or scheduled via --schedule-days.

Usage:
    python schedule_emails_terminal.py                     # send next unsent (default: terminal/)
    python schedule_emails_terminal.py --dir python         # send next from python/
    python schedule_emails_terminal.py --list               # list all tutorials
    python schedule_emails_terminal.py --reset              # reset send tracking
    python schedule_emails_terminal.py --all                # send all unsent now
    python schedule_emails_terminal.py --file "Mac Terminal.md"  # send specific
    python schedule_emails_terminal.py --schedule-days 2    # schedule next send in 2 days

Setup:
    1. Create a .env file in this directory (see .env.example)
    2. Run once to test:  python schedule_emails_terminal.py
    3. Add to crontab for daily delivery:
        0 8 * * * /usr/local/bin/python3 /path/to/schedule_emails_terminal.py
"""

import os
import re
import sys
import json
import smtplib
import argparse
import subprocess
import shlex
from pathlib import Path
from email.mime.text import MIMEText

BASE_DIR = Path(__file__).parent
TRACKING_DIR = BASE_DIR
ENV_FILE = BASE_DIR / ".env"

DEFAULT_FOLDER = "terminal"

SIGNATURE = """
<hr>
<p style="color:#6b7280; font-size: 12px;">
  <strong>Zero to AI Builder</strong> — by @juliusdarang<br>
  <a href="https://gumroad.com/juliusdarang">Get the full course →</a>
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


def tracking_file(folder):
    return TRACKING_DIR / f"_email_progress_{folder}.json"


def load_tracking(folder):
    fpath = tracking_file(folder)
    if fpath.exists():
        return json.loads(fpath.read_text())
    return {"folder": folder, "sent": [], "current_index": 0}


def save_tracking(folder, tracking):
    tracking_file(folder).write_text(json.dumps(tracking, indent=2))


def get_tutorials(folder):
    folder_path = BASE_DIR / folder
    if not folder_path.is_dir():
        print(f"ERROR: Folder '{folder}' not found at {folder_path}")
        sys.exit(1)
    return sorted(f.name for f in folder_path.glob("*.md") if f.is_file())


def extract_title(filepath):
    text = filepath.read_text()
    match = re.search(
        r'<!--\s*_class:\s*cover\s*-->\s*\n\s*#\s+(.+?)(?:\n|$)', text
    )
    if match:
        return match.group(1).strip()
    return filepath.stem


def strip_frontmatter_and_css(text):
    text = re.sub(r'^---\n.*?\n---\n', '', text, count=1, flags=re.DOTALL)
    text = re.sub(r'<style>.*?</style>', '', text, flags=re.DOTALL)
    return text


def markdown_to_simple_html(md_text):
    html = md_text

    html = re.sub(r'^###\s+(.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^##\s+(.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^#\s+(.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)

    html = re.sub(r'^-{3,}', r'<hr>', html)

    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)

    html = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', html)

    html = re.sub(r'^-\s+(.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)

    html = re.sub(
        r'(<li>.*?</li>(\s*<li>.*?</li>)*)',
        r'<ul>\1</ul>',
        html,
        flags=re.DOTALL,
    )

    html = re.sub(r'\n\n+', r'</p><p>', html)
    html = '<p>' + html + '</p>'
    html = re.sub(r'<p>\s*</p>', '', html)

    return html


def build_email_body(filepath, title, folder):
    text = filepath.read_text()
    clean = strip_frontmatter_and_css(text)

    lines = clean.split("\n")
    content_start = 0
    for i, line in enumerate(lines):
        if line.strip().startswith("<!--"):
            content_start = i + 1

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

    folder_label = folder.replace("_", " ").title()

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
    <p>Zero to AI Builder — {folder_label}</p>
  </div>
  {body_html}
  {SIGNATURE}
</body>
</html>"""


def send_email(env, subject, body_html, smtp=None):
    msg = MIMEText(body_html, "html")
    msg["Subject"] = subject
    msg["From"] = env["GMAIL_SENDER"]
    msg["To"] = env["GMAIL_RECEIVER"]
    message = msg.as_string()

    if smtp is None:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(env["GMAIL_SENDER"], env["GMAIL_APP_PW"])
            connection.sendmail(
                env["GMAIL_SENDER"], env["GMAIL_RECEIVER"], message
            )
    else:
        smtp.sendmail(env["GMAIL_SENDER"], env["GMAIL_RECEIVER"], message)

    print(f"Sent: {subject}")


def list_tutorials(folder):
    tutorials = get_tutorials(folder)
    tracking = load_tracking(folder)
    folder_path = BASE_DIR / folder

    print(f"Folder: {folder}/")
    print(f"{'Status':<8} {'#':<3} Tutorial")
    print("-" * 50)
    for i, fname in enumerate(tutorials):
        fpath = folder_path / fname
        title = extract_title(fpath)
        sent = "✅" if fname in tracking["sent"] else "  "
        print(f"{sent:<8} {i+1:<3} {title}")
    sent_count = len(tracking["sent"])
    print(f"\n{sent_count}/{len(tutorials)} sent")


def send_tutorial(folder, env, fname, smtp=None, tracking=None):
    fpath = BASE_DIR / folder / fname
    if not fpath.exists():
        print(f"ERROR: {fpath} not found")
        return False

    title = extract_title(fpath)
    body = build_email_body(fpath, title, folder)
    subject = f"Zero to AI Builder — {title}"

    send_email(env, subject, body, smtp=smtp)

    if tracking is None:
        tracking = load_tracking(folder)
    if fname not in tracking["sent"]:
        tracking["sent"].append(fname)
    save_tracking(folder, tracking)
    return True


def scheduled_command(folder):
    """Build a safely quoted command for the `at` job body."""
    return "cd {} && exec {} {} --dir {}".format(
        shlex.quote(str(BASE_DIR)),
        shlex.quote(sys.executable),
        shlex.quote(str(Path(__file__).resolve())),
        shlex.quote(folder),
    )


def schedule_send(folder, days):
    try:
        result = subprocess.run(
            ["at", "now", "+", str(days), "days"],
            input=scheduled_command(folder) + "\n",
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print(f"Scheduled: next '{folder}' email in {days} day(s)")
            if result.stdout:
                print(result.stdout.strip())
        else:
            print("WARNING: 'at' command failed. The 'atrun' daemon may be disabled.")
            print("Fallback: add this to your crontab to run now:")
            print(f"  {sys.executable} {Path(__file__).resolve()} --dir {folder}")
            return False
    except FileNotFoundError:
        print("WARNING: 'at' command not available on this system.")
        print(f"Run manually: {sys.executable} {Path(__file__).resolve()} --dir {folder}")
        return False
    return True


def schedule_send_on_date(folder, date_str):
    try:
        date_args = shlex.split(date_str)
    except ValueError as exc:
        print(f"WARNING: invalid date {date_str!r}: {exc}")
        return False

    try:
        result = subprocess.run(
            ["at", "08:00", *date_args],
            input=scheduled_command(folder) + "\n",
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print(f"Scheduled: next '{folder}' email for 08:00 on {date_str}")
            if result.stdout:
                print(result.stdout.strip())
        else:
            print("WARNING: 'at' command failed. The 'atrun' daemon may be disabled.")
            print(f"Fallback: add this to your crontab to run at 8am on {date_str}:")
            print(f"  {sys.executable} {Path(__file__).resolve()} --dir {folder}")
            return False
    except FileNotFoundError:
        print("WARNING: 'at' command not available on this system.")
        print(f"Run manually on {date_str}: {sys.executable} {Path(__file__).resolve()} --dir {folder}")
        return False
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Email tutorials from any folder, one at a time."
    )
    parser.add_argument(
        "--dir",
        type=str,
        default=DEFAULT_FOLDER,
        help=f"Tutorial folder to send from (default: {DEFAULT_FOLDER})",
    )
    parser.add_argument(
        "--list", action="store_true", help="List all tutorials and status"
    )
    parser.add_argument(
        "--reset", action="store_true", help="Reset send tracking for this folder"
    )
    parser.add_argument(
        "--all", action="store_true", help="Send all unsent tutorials now"
    )
    parser.add_argument(
        "--file", type=str, help="Send a specific tutorial by filename"
    )
    parser.add_argument(
        "--schedule-days",
        type=int,
        metavar="N",
        help="Schedule the next unsent tutorial N days from now via 'at'",
    )
    parser.add_argument(
        "--schedule-date",
        type=str,
        metavar="DATE",
        help="Schedule the next unsent tutorial for a specific date via 'at' (e.g. 'Jul 5', '2026-07-05')",
    )
    args = parser.parse_args()

    folder = args.dir
    env = load_env()

    if args.list:
        list_tutorials(folder)
        return

    if args.reset:
        tracking = {"folder": folder, "sent": [], "current_index": 0}
        save_tracking(folder, tracking)
        print(f"Tracking reset for '{folder}'. All tutorials marked as unsent.")
        return

    tutorials = get_tutorials(folder)

    if not tutorials:
        print(f"No .md files found in '{folder}/'")
        return

    if args.schedule_days:
        index = load_tracking(folder).get("current_index", 0)
        if index >= len(tutorials):
            print("All tutorials in this folder have been sent. Use --reset to start over.")
            return
        schedule_send(folder, args.schedule_days)
        return

    if args.schedule_date:
        index = load_tracking(folder).get("current_index", 0)
        if index >= len(tutorials):
            print("All tutorials in this folder have been sent. Use --reset to start over.")
            return
        schedule_send_on_date(folder, args.schedule_date)
        return

    if args.file:
        send_tutorial(folder, env, args.file)
        return

    if args.all:
        tracking = load_tracking(folder)
        # Reuse one authenticated connection for the whole batch. A new TLS
        # handshake and SMTP login for every tutorial dominates --all runtime.
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(env["GMAIL_SENDER"], env["GMAIL_APP_PW"])
            for fname in tutorials:
                if fname not in tracking["sent"]:
                    send_tutorial(folder, env, fname, smtp=smtp, tracking=tracking)
                else:
                    print(f"Skipped (already sent): {fname}")
        tracking["current_index"] = len(tracking["sent"])
        save_tracking(folder, tracking)
        remaining = len(tutorials) - tracking["current_index"]
        print(f"Done. {remaining} tutorial(s) remaining.")
        return

    tracking = load_tracking(folder)
    index = tracking.get("current_index", 0)

    while index < len(tutorials):
        fname = tutorials[index]
        if fname in tracking["sent"]:
            index += 1
            continue
        send_tutorial(folder, env, fname)
        tracking["current_index"] = index + 1
        save_tracking(folder, tracking)
        remaining = len(tutorials) - tracking["current_index"]
        print(f"{remaining} tutorial(s) remaining in '{folder}'.")
        return

    print(f"All tutorials in '{folder}' have been sent. Use --reset to start over.")


if __name__ == "__main__":
    main()
