# AI AGENTS LEVELS — Product Overview

A tiered curriculum teaching you how to build AI agents at increasing levels of complexity.

---

## The Product

| Attribute | Value |
|-----------|-------|
| **Format** | MARP Markdown slides (exportable to PDF + images) |
| **Price** | To be determined (Gumroad) |
| **Audience** | Developers who know the basics of AI prompting and want to build autonomous systems |
| **Prerequisite** | Familiarity with AI prompting (LLM API calls, system prompts) |
| **Style** | Visual, diagram-heavy, concept-first, then implementation |

---

## Structure — 4 Levels × 4 Parts = 16 Tutorials

### Level 1: Single Agent (4 parts)
**Theme:** Your First AI Worker

| Part | Title | Status |
|------|-------|--------|
| p1 | What Is an Agent | ✅ Complete |
| p2 | Anatomy of an Agent | ✅ Complete |
| p3 | Tools + ReAct Loop | ✅ Complete |
| p4 | Building Your First Agent | ✅ Complete |

**Covers:** ReAct loop, tool calling, memory, the core difference between plain LLM calls and agents.

---

### Level 2: Pipeline Agent (4 parts)
**Theme:** Chaining Specialists

| Part | Title | Status |
|------|-------|--------|
| p1 | The Pipeline Mental Model | ✅ Complete |
| p2 | The Orchestrator | ✅ Complete |
| p3 | Artifact Design | ✅ Complete |
| p4 | Error Handling + Debugging | ✅ Complete |

**Covers:** Single-responsibility principle, agent handoffs, artifact contracts, running multi-step pipelines.

---

### Level 3: Multi-Agent (4 parts)
**Theme:** Orchestrator + Specialists

| Part | Title | Status |
|------|-------|--------|
| p1 | The Orchestrator Mental Model | ⚠️ Outline only |
| p2 | Agent Selection Routing | ⚠️ Placeholder |
| p3 | Result Handling + Synthesis | ⚠️ Placeholder |
| p4 | Full Multi-Agent Build | ⚠️ Placeholder |

**Covers:** Intent parsing, rule-based vs LLM routing, when to use multi-agent vs pipeline.

---

### Level 4: Agent Teams (4 parts)
**Theme:** Full Autonomous Workflow

| Part | Title | Status |
|------|-------|--------|
| p1 | The Team Mental Model | ⚠️ Outline only |
| p2 | Building Teams (Content vs Engineering) | ⚠️ Placeholder |
| p3 | Top-Level Orchestration | ⚠️ Placeholder |
| p4 | Full Autonomous System | ⚠️ Placeholder |

**Covers:** Team architecture, department-style routing, full autonomous workflows.

---

## Current Completeness

| Level | Complete | Placeholder | Total |
|-------|----------|------------|-------|
| Single Agent | 4 | 0 | 4 |
| Pipeline Agent | 4 | 0 | 4 |
| Multi-Agent | 0 | 4 | 4 |
| Agent Teams | 0 | 4 | 4 |
| **Total** | **8** | **8** | **16** |

**8 complete教程 / 8 placeholders = 50% complete**

---

## Visual Design System

- **Font:** DM Sans (headings), DM Mono (code/vocabulary)
- **Primary color:** Amber (#d97706)
- **Background:** Light mode with dark cover slides
- **Style elements:** VS grids, diagrams, stepped content, cheat tables
- **Export:** MARP-compatible, paginated

---

## Files

```
AI AGENTS LEVELS/
├── Single Agent p1.md      # ✅ Complete
├── Single Agent p2.md     # ✅ Complete
├── Single Agent p3.md      # ✅ Complete
├── Single Agent p4.md      # ✅ Complete
├── Pipeline Agent p1.md   # ✅ Complete
├── Pipeline Agent p2.md   # ✅ Complete
├── Pipeline Agent p3.md   # ✅ Complete
├── Pipeline Agent p4.md   # ✅ Complete
├── Multi-Agent p1.md      # ⚠️ Outline
├── Multi-Agent p2.md      # ⚠️ Placeholder
├── Multi-Agent p3.md      # ⚠️ Placeholder
├── Multi-Agent p4.md      # ⚠️ Placeholder
├── Agent Teams p1.md      # ⚠️ Outline
├── Agent Teams p2.md      # ⚠️ Placeholder
├── Agent Teams p3.md      # ⚠️ Placeholder
├── Agent Teams p4.md      # ⚠️ Placeholder
└── SA p1 v2.md, v3.md     # 🗑️ Duplicates to clean up
```

---

## What's Next

1. **Finish Levels 3 & 4** — Write full content for Multi-Agent and Agent Teams
2. **Clean up duplicates** — Remove v2, v3 draft files
3. **Export pipeline** — Set up MARP CLI for PDF/images
4. **Social images** — Create platform-specific image variants
5. **Launch** — Upload to Gumroad, start social posting

---

## Platform Notes

- **MARP** is already configured in each file (YAML frontmatter)
- **PDF export:** `npx @marp-team/marp-cli --pdf input.md`
- **Image export:** Use PDF as base, convert to images via Canva/CloudConvert
- **Social posting:** Best for LinkedIn (carousel) + Twitter (thread snippets)