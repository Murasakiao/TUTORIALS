# Polymath Tutorials

Educational slide-based tutorials by **[Julius Darang](https://github.com/juliusdarang)** — from zero to AI developer.

## What's Inside

**~120 files** across ~93 MARP slides and ~25 PDF exports, covering 13 subject areas:

| Subject | Location | Status |
|---------|----------|--------|
| **Zero to AI Builder** — flagship curriculum | `ZERO TO AI BUILDER/` | ~98% done |
| **Claude Code** — tool-specific deep dives | `CLAUDE CODE/` | ~100% done |
| **AI Agents Levels** — agent architecture | `AI AGENTS LEVELS/` | ~50% done |
| **CLI Mastery** | `MASTERING CLI.md` | Outline |
| **Prompt Engineering** | `PROMPT ENGINEERING/` | Mixed |
| **Vibe Coding 101** | `VIBE CODING 101/` | Complete |
| **Social Carousels** | `CAROUSELS/` | Complete |
| **Templates & Design System** | `_templates/` | — |
| **Product & Brand Strategy** | `_product/` | — |

### Zero to AI Builder (the flagship)

8 phases, from absolute beginner to AI developer:

- **terminal/** — Mac & Windows terminal, VS Code install, Markdown, browsers, DevTools
- **git/** — Install Git, Git vs GitHub, undo mistakes, commit messages, collaboration
- **web-dev/** — HTML/CSS, Flexbox, color, fonts, domains, responsive design, images, favicons, APIs
- **python/** — Python install (Mac/Windows), venv, scripting, CSV, APIs, Pandas, web scraping, email, scheduling, Tkinter
- **ai/prompting/** — Prompt frameworks, coding prompts, structured outputs, AI as personal assistant
- **ai/agents/** — What is an agent, build your first, tools, single vs multi-agent, memory
- **ai/coding/** — Agentic coding, debug with AI, build apps, break down projects, review AI code
- **ai/automations/** — Daily task automation, connect apps, workflows, spreadsheets, scheduling
- **career/** — Portfolio, LinkedIn, open source, learning strategies, documentation, consistency
- **content/** — Copy-paste prompt templates, quick automation wins, case studies
- **general/** — File structure, README writing, tutorial index

## How Tutorials Are Built

Every tutorial is a **single-file MARP Markdown slide deck**.

### File format

```markdown
---
marp: true
paginate: true
html: true
size: 4:3
style: |
  @import url('...');
  /* CSS variables + component styles */
---

<!-- _class: cover -->

# Title Slide

Content with HTML grid/card components...
```

**Key conventions:**
- YAML frontmatter with `marp: true`, `html: true`, `size: 4:3`
- Embedded CSS in `<style>` tags (inline in the `style:` frontmatter field)
- HTML `<div>` components for layouts (cards, grids, columns, diagrams)
- Slide classes via `<!-- _class: -->` comments (cover, step, cta, lead)
- Page footers auto-generated via `section::after`

### Design system

The master template is at `_templates/MARP_STYLING_TEMPLATE.md` (1551 lines).

**Typography:** DM Sans (headings/body) + DM Mono (code/vocabulary)

**Color themes:**

| Theme | Primary | Used In |
|-------|---------|---------|
| Blue | `#2563eb` | ZERO TO AI BUILDER |
| Amber | `#d97706` | AI AGENTS LEVELS |
| Dark (amber accents) | `#080808` bg | CLAUDE CODE |
| Dark (blue/green) | — | CAROUSELS |

**Slide classes:**
- `cover` — dark full-bleed title slide
- `step` — alternate background section divider
- `cta` — branded call-to-action closing slide
- `lead` — centered bold statement slide

**Components** (all built with HTML/CSS grids):
- Cards & card rows — feature highlights
- Stat cards — numbers/metrics
- Tool/memory cards — software-specific callouts
- Versus grids — comparison layouts
- Process flow / timeline — step-by-step
- Code comparison — side-by-side code
- ReAct loop diagram — agent reasoning visualization
- Checklists — actionable items
- Pros/cons — balanced comparison

### Adding a new tutorial

1. Copy the relevant template (`_templates/MARP_STYLING_TEMPLATE.md`)
2. Set the color variables to your theme
3. Write slides with the available component classes
4. Export to PDF (see below)

## Export Workflow

### Prerequisites

```bash
npm install -g @marp-team/marp-cli
```

### Export a single file

```bash
npx @marp-team/marp-cli --pdf "ZERO TO AI BUILDER/terminal/Mac Terminal.md"
```

### Export all in a directory

```bash
npx @marp-team/marp-cli --pdf "ZERO TO AI BUILDER/**/*.md"
```

### VS Code alternative

1. Install "Marp for VS Code" extension
2. Right-click a `.md` file → "Marp: Export Slide Deck..."
3. Or command palette → "Marp: Export All"

### Git note

`*.pdf` is gitignored — PDFs are build artifacts. Export them before distribution.

## Distribution

Tutorials are sold on **[Gumroad](https://gumroad.com/)** as PDF bundles.

- **Phases 1–2:** Free
- **Phases 3–8:** $9 each
- **Full bundle:** $29
- **Pricing tiers:** $5 (budget), $9 (standard), $15 (supporter)

See `_product/GUMROAD_PRODUCT_DESCRIPTIONS.md` and `ZERO TO AI BUILDER/GUMROAD_LAUNCH_PLAN.md` for full strategy.

## Project Structure

```
tutorials/
├── _product/           # Brand docs, product descriptions, pricing
├── _templates/         # MARP CSS template + cover template
├── AI AGENTS LEVELS/   # 4 levels × 4 parts (50% complete)
├── CAROUSELS/          # Social media carousel slides
├── CLAUDE CODE/        # 18 tutorials — one per Claude Code command
├── PROMPT ENGINEERING/ # Curriculum + carousel + long-form doc
├── VIBE CODING 101/    # Curriculum + carousel + long-form doc
├── ZERO TO AI BUILDER/ # Flagship: 8 phases across 11 subdirectories
│   ├── terminal/       git/  web-dev/  python/
│   ├── ai/             {prompting/  agents/  coding/  automations/}
│   ├── career/         content/  general/
│   ├── LEARNING_PATH.md
│   └── GUMROAD_LAUNCH_PLAN.md
├── MASTERING CLI.md    # CLI mastery outline
└── README.md           # This file
```

## Quick Start

```bash
# Preview a deck in the browser
npx @marp-team/marp-cli --preview "path/to/file.md"

# Export to PDF
npx @marp-team/marp-cli --pdf "path/to/file.md"

# Watch and auto-rebuild on save
npx @marp-team/marp-cli --watch --pdf "path/to/file.md"
```

## License

All content © Julius Darang. All rights reserved.
