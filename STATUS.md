---
name: tutorials
description: Gumroad course business — paid Marp slide decks across multiple learning tracks
domain: brand
status: active
stack: Marp (.md → .pdf) · shared styling templates
entry: marp <deck>.md --pdf  ·  PI-CODING-AGENT/build-pdf.sh
has_repo: true
updated: 2026-08-14
---

# tutorials

## State
ZERO TO AI BUILDER (~45) is complete and published. The remaining tracks are AI AGENTS
LEVELS (4 topics × 4 parts), CLAUDE CODE (~18 single-page guides), PROMPT ENGINEERING
(stub), and VIBE CODING 101 (stub). Plus CAROUSELS/ for social derivatives and
PI-CODING-AGENT/ for the Pi tutorial package. PI-CODING-AGENT has separate
concise/expanded Marp decks and a canonical long-form source for its vertical PDF.

## Next action
Promote the published ZERO TO AI BUILDER product, then fill the PROMPT ENGINEERING
and VIBE CODING 101 stubs. Keep the remaining tutorial tracks separate from the
canonical long-form PDF and deck sources.

## Conventions
- Global `marp-output` skill — authoring, structure, template selection, rendering, and QA; use `.pi/skills/visual-style/` for the Polymath tutorial template and design contract.
- `tutorial-content` owns canonical long-form tutorial Markdown; `pandoc-pdf` owns the vertical PDF pipeline; `marp-output` owns slide decks. Keep these sources and outputs separate.
- Styling source: `_templates/MARP_STYLING_TEMPLATE.md` — reuse, don't recreate.
- Brand structure: `_product/juliusdarang_BRAND_STRUCTURE.md` + product defs.

## Pointers
- Templates: `_templates/` · product defs: `_product/` · Pi package: `PI-CODING-AGENT/`.
- Canonical Pi tutorial: `PI-CODING-AGENT/pi-agent-contents.md`; build with `PI-CODING-AGENT/build-pdf.sh`.
- Own `.git` (origin `github.com/Murasakiao/TUTORIALS`).