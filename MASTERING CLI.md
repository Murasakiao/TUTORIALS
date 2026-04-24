Volume 1 — Mastering the CLI
Part 1 — Why the Terminal Exists
Slides: GUI vs CLI: what you gain and what you give up → What the terminal actually talks to (the shell) → Why developers live here → Why you cannot build serious projects without it → What you will be able to do by the end of this volume
Part 2 — Your Shell and Your Environment
Slides: bash vs zsh vs fish: differences that matter → How to know which shell you are running → The prompt: what each part means → Environment variables: what they are and why they exist → PATH explained: why some commands work and others don't → Setting up a minimal useful shell configuration
Part 3 — Navigation and the Filesystem
Slides: The filesystem as a tree: roots, branches, leaves → Absolute vs relative paths: the distinction that breaks beginners → pwd ls cd — the three commands you use a thousand times → Hidden files and why they exist → Tab completion: the one habit that saves the most time → tree for visualizing a project structure
Part 4 — Files and Directories
Slides: Creating files and folders: touch mkdir → Copying, moving, renaming: cp mv → Deleting safely: rm rmdir and why rm -rf deserves respect → Viewing file contents: cat less head tail → Searching inside files: grep basics → Finding files by name: find with common patterns
Part 5 — Reading and Writing Text in the Terminal
Slides: Standard input, output, and error explained → Redirecting output to a file: > and >> → The pipe | and what it means → echo for printing and quick file creation → sed for simple find-and-replace → awk for extracting columns from structured output → Why these matter for reading logs and transforming outputs
Part 6 — Processes and Job Control
Slides: What a process is → ps and top for seeing what is running → Running a command in the background with & → jobs fg bg explained → Killing a process: kill and Ctrl+C vs Ctrl+Z → nohup for keeping a process alive after closing the terminal → tmux basics: running persistent sessions
Part 7 — Permissions and Ownership
Slides: What file permissions are and why they matter → Reading rwx in ls -la output → chmod for changing permissions: numeric vs symbolic → Why scripts need to be executable and how to make them so → Sudo: what it means, when to use it, and when not to → Why permission errors are one of the most common beginner blockers
Part 8 — Shell Scripts: Automating the Terminal
Slides: What a shell script is → The shebang line: what #!/bin/bash does → Variables, conditionals, and loops in shell scripts → Accepting arguments: $1 $2 $@ → Exit codes: how scripts signal success and failure → Real example: a shell script that sets up a new project folder structure → CTA: automate one repetitive terminal task you do manually today
Part 9 — Customizing Your Shell
Slides: The .zshrc and .bashrc files: what they are and when they run → Aliases: shortcuts for commands you type constantly → Functions in your rc file: aliases that take arguments → Persisting environment variables across sessions → Shell plugins worth installing: zsh-autosuggestions, zsh-syntax-highlighting → A minimal fast rc file for a developer → CTA: set up your shell so your environment is ready in one terminal open

Volume 2 — CLI for AI Agents
Part 1 — Python Environment Management
Slides: Why global Python installs cause chaos → pyenv for managing multiple Python versions → venv for isolated project environments → Activating and deactivating environments: what actually changes → The requirements.txt file: freezing and restoring dependencies → pip vs pip3: which one you are actually calling → CTA: set up a clean isolated environment for your agent project
Part 2 — Project Structure for Agent Projects
Slides: Why structure matters more for agents than for scripts → Standard layout for a single-agent project → Separating prompts from code: the prompts/ folder pattern → Separating config from code: the config/ folder pattern → Context files: where voice samples and reference documents live → The README.md as operational documentation
Part 3 — Environment Variables and Secrets Management
Slides: Why API keys must never live in your code → The .env file: what it is and how it works → python-dotenv: loading .env into Python → The .gitignore file: making sure secrets never reach a repository → Managing multiple API keys across multiple providers → Secrets management for deployed agents: beyond the .env file
Part 4 — Git for Agent Builders
Slides: Why version control is non-negotiable for agent projects → git init git add git commit — the core loop → What to never commit in an agent project: API keys, cached outputs, large context files → Branches: working on a new agent version without breaking the current one → git diff for seeing what changed in a prompt → Reverting a bad prompt change: git checkout and git revert
Part 5 — Running and Managing Agent Scripts
Slides: Running a Python script from the CLI → Passing arguments with argparse: running different configs without editing the file → Logging output to a file while watching it live: tee → Running long pipelines in the background → Monitoring a running agent: tail -f on the log file → Killing a runaway agent: finding and stopping the process cleanly
Part 6 — Scheduling and Automation
Slides: Why agents are most powerful when they run without you → cron explained: syntax, gotchas, and common patterns → Cron environment vs shell environment: why your cron job fails when your script works → Logging cron output so you know if it ran → Running an agent on a schedule → Triggering agents from other scripts: chaining runs with exit codes
Part 7 — Debugging Agent Pipelines from the CLI
Slides: Reading Python tracebacks without panic → python -m pdb for step-by-step debugging → The logging module: levels, handlers, and formatters → Writing logs that are actually useful for agent debugging → grep-ing your logs for specific agent decisions or errors → Diffing two agent output files to see what changed: diff → Reproducing a failure: re-running a specific agent call with the same inputs
Part 8 — CLI Tools Every Agent Builder Should Know
Slides: curl for testing API endpoints directly from the terminal → jq for reading and transforming JSON output from agent calls → watch for monitoring a file or command output in real time → bat as a better cat for reading prompt files → ripgrep as a faster grep for large codebases → fzf for fuzzy-finding files and history → Building a personal CLI toolkit: the tools that stay installed on every machine
Part 9 — The Agent Development Loop from the CLI
Slides: What the full development loop looks like from a terminal → Writing a prompt, running the agent, reading the output, iterating → Using make and a Makefile to standardize common agent commands → Running evals from the CLI: a simple eval script you can call anytime → Committing prompt changes with descriptive git messages → Building a dev.sh script that sets up your environment and runs your agent in one command → CTA: set up the full CLI development environment for your own agent project