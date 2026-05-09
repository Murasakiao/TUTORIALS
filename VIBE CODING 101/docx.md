
---

# Vibe Coding 101
### Build Real Things Without Being a Developer
*A Beginner's Guide to the Cursor + Claude Stack*

---

## Volume 1 — The Mindset & the Stack

---

### Chapter 1 — What Vibe Coding Actually Is

You don't need to learn to code before you can build something. That used to be the only path. It isn't anymore.

**Vibe coding** is directing an AI to write code on your behalf. You describe what you want — clearly and specifically — and the AI produces working code. You review the result, test it, and direct the next step.

This is different from asking ChatGPT to write code. A chatbot gives you a code snippet you have to manually place somewhere. Vibe coding with a tool like Cursor means the AI has full visibility into your project and can build across multiple files at once.

**Your role shifts.** You are not the programmer. You are the architect — deciding what to build — and the reviewer — deciding whether the output is correct.

**What you can realistically build as a complete beginner:**
- Simple web apps (habit trackers, link-in-bio pages, calculators)
- Internal tools (dashboards, form collectors, data displays)
- Lightweight automations and scripts
- Static sites and landing pages

**What vibe coding cannot do:**
- Replace your judgment about what to build
- Catch bad ideas early — that's still your job
- Guarantee working code without you testing it

**The one skill that makes everything else work:** knowing what you want clearly enough to describe it. If you can't explain it to a person, you can't explain it to an AI.

---

### Chapter 2 — The Cursor + Claude Stack

**Cursor** is a code editor built on top of VS Code with AI built directly into it. It's not a chatbot — it reads your entire codebase before responding, which makes it far more useful than asking a standalone AI for code.

**Claude** is the AI model running inside Cursor. It understands your files, folders, and how pieces connect. That context awareness is what makes it behave like a collaborator rather than a code generator.

**Three ways to interact with Cursor:**

| Mode | Shortcut | Best for |
|------|----------|----------|
| Chat | Cmd+L | Questions, explanations, exploring ideas |
| Agent | Cmd+I | Building features across multiple files |
| Inline edit | Cmd+K | Small, targeted changes to a specific block |

**How Claude sees your project.** It reads the files and folders you share with it. Use `@filename` to explicitly point Claude at a specific file — this prevents it from guessing what already exists.

**What you don't need to know:** syntax, frameworks, or how to debug from scratch. You need to know what the output should look like and whether the app behaves correctly.

**Setting up Cursor:**
1. Download Cursor at cursor.com
2. Open a new folder as your project
3. Set Claude as your model in settings
4. Start with a project brief before writing a single prompt

---

### Chapter 3 — The Vibe Coding Mindset

Three mental shifts separate people who ship things from people who get stuck.

**Shift 1: You are a product thinker, not a programmer.**
Your job is to define behavior and review output. You don't need to understand how the code works — you need to understand whether it does what you asked.

**Shift 2: Imperfect and working beats perfect and unbuilt.**
Most beginners stall trying to plan every detail upfront. Build the rough version first. Refine it when it exists.

**Shift 3: Errors are normal — Claude will fix them too.**
Every developer sees errors constantly. The difference is that developers know what to do with them. In vibe coding, you paste the error into Cursor and let Claude handle it.

**Why beginners quit:** they treat the first broken output as failure. It isn't. It's the first data point in a fix loop.

**The build loop:**
```
describe → generate → review → fix → repeat
```

Every step of that loop is a prompt. The loop doesn't end until the feature works — and most features take 3–6 loops, not 1.

---

## Volume 2 — The Core Workflow

---

### Chapter 4 — Starting a Project the Right Way

The most common mistake beginners make is jumping straight into prompting without knowing what they're building. Claude needs a map of your project before it can help you build it.

**Write a project brief first.** Before you open Cursor, write 1–2 paragraphs covering four things:

1. **What it is** — a one-sentence description
2. **Who it's for** — even if that's just you
3. **What it does** — the core actions a user can take
4. **What it looks like** — rough layout, not a design spec

**Example brief — habit tracker:**
> "A simple web app for tracking daily habits. Single user, no login required. The user can add habits, mark them done each day, and see a basic streak count. One page layout: habit list on the left, calendar view on the right. Clean, minimal design."

This brief becomes the first thing you paste into every new Cursor session using `@` to reference it. Claude reads it before doing anything.

**Starting from a template vs. from scratch:**
- Use a template when your stack is already decided (React, Next.js, etc.)
- Start from scratch when you want Claude to pick the simplest approach

**Folder structure basics.** You don't need to know what files to create — ask Claude to scaffold the project structure based on your brief. Then keep that structure consistent throughout the build.

---

### Chapter 5 — Writing Prompts That Build

Vibe coding prompts are not the same as chat prompts. Chat prompts ask for information. Build prompts ask for working software.

**The anatomy of a good build prompt:**
- **What to build** — specific feature or component
- **Where it goes** — which file, which section of the page
- **How it should behave** — what happens when the user interacts with it

**Scope control.** Ask for one thing at a time. A prompt asking for an entire app produces code that's hard to review and even harder to fix. A prompt asking for a single form with two fields produces something you can test in 30 seconds.

**Describing UI in plain English.** You don't need design vocabulary. Spatial language works fine:
- "A centered card with a title at the top and two buttons below it"
- "A sidebar on the left taking up 30% of the width, with the main content on the right"
- "A sticky header with the app name on the left and a settings icon on the right"

**Always reference existing files.** Before adding anything new, tell Claude what already exists:
> "I have a `components/Header.jsx` file already. Add a logout button to the right side of it."

Without this, Claude may create a duplicate file or add conflicting code.

**Side-by-side: vague vs. clear build prompt**

| ❌ Vague | ✅ Clear |
|---------|---------|
| "Add a form to my app" | "Add a contact form to `pages/contact.jsx` with three fields: name, email, and message. On submit, show a success message below the form. No backend needed — just validate that all fields are filled." |

**When Claude builds the wrong thing.** Don't start over — use a correction prompt:
> "That's not quite right. I wanted X, but you built Y. Keep the existing file structure and change only [specific thing]."

---

### Chapter 6 — Reading the Output Without Knowing Code

You don't need to understand the code Claude writes. You need to understand what it does.

**Three questions to ask every time Claude generates something:**
1. Does it run without errors?
2. Does it look right visually?
3. Does it do what I asked?

If all three are yes, move to the next feature. If any is no, you have a prompt to write.

**How to run your project locally.** Claude will tell you, but the standard pattern is:
```
npm install    ← run once to install dependencies
npm run dev    ← starts the local server
```
Open the URL it gives you (usually `localhost:3000`) in your browser.

**Reading error messages as a non-developer.** You don't need to understand the error — you need to know what to copy. Copy the full error text, especially the part that starts with `Error:` or shows a file name and line number. Paste it directly into Cursor Chat.

**When the output looks wrong but there's no error.** This is a visual review issue, not a code error. Describe what you see vs. what you expected:
> "The form is displaying but the button is not visible on mobile. It looks like it's being cut off. Fix the layout so the button is always visible."

**Build the habit of testing every change before asking for the next one.** Each untested feature adds complexity to the next error. Test small, catch problems early.

---

### Chapter 7 — The Fix Loop

Errors are the normal state of building software. Every developer runs into them. The difference in vibe coding is that you have a collaborator who can read the error and fix it.

**The fix prompt formula:**
```
Here is the error: [paste error]
I expected: [what you thought would happen]
Fix it.
```

That's it. Don't explain more than that. Claude has the codebase context already.

**Why you should never manually edit code as a beginner.** You don't know what depends on what. Changing one line can silently break three other things. Always make changes through prompts so Claude can account for dependencies.

**When Claude's fix creates a new error.** This is normal and usually means the first fix was surface-level. Use the escalation prompt:
> "The previous fix introduced a new error: [paste new error]. Here's what the code is supposed to do overall: [brief description]. Fix both issues."

**The three-fix rule.** If you've gone three fix prompts deep on the same error without resolution, don't keep going. Describe the feature from scratch in a new prompt and ask Claude to rebuild it cleanly. Incremental patches on broken code compound the problem.

**When to start over vs. when to keep fixing:**
- Keep fixing: the error is isolated to one file or one behavior
- Start over: the same error keeps reappearing, or multiple files are involved in unpredictable ways

---

## Volume 3 — Building Real Things

---

### Chapter 8 — Scoping Your First Build

The most common beginner failure is building something too big to finish. A half-built app with ten features teaches you less than a complete app with one.

**The MVP mindset:** what is the smallest version that still does the core thing? Not the smallest version you'd be proud to show — the smallest version that works end-to-end.

**How to scope down a big idea:**
1. Write every feature you want
2. Circle the one feature the app doesn't work without
3. Cut everything else to a second version
4. Build only the circled feature first

**The feature list exercise — example: a link-in-bio tool**

Full idea: custom themes, analytics, scheduled links, password protection, mobile preview, custom domain.

Scoped MVP: a page that displays your name, a short bio, and a list of clickable links. That's it. Everything else is v2.

**The one-session rule.** If you can't reasonably build it in one focused session (1–3 hours), it's too big for your first attempt. Scope it until it fits.

---

### Chapter 9 — Building Page by Page

Build one page at a time. Review it. Sign off on it. Then move to the next.

**The page prompt structure:**
1. **Layout** — where things sit on the page
2. **Components** — what individual elements exist (buttons, cards, inputs)
3. **Behavior** — what happens when the user interacts
4. **Data** — what information is displayed or stored

**Example: prompting a home page**
> "Build the home page at `pages/index.jsx`. Layout: full-width header with app name, centered hero section with a headline and a 'Get Started' button, and a three-column features section below. No data yet — use placeholder text. Style it clean and minimal with a white background."

**Describing components without design vocabulary:**
- "A card with a border, a small icon in the top left, a title, and two lines of description text"
- "A button that's solid blue with white text and slightly rounded corners"
- "An input field that stretches the full width of its container"

**Connecting pages.** After building two pages, add navigation in a separate prompt:
> "I now have `pages/index.jsx` and `pages/about.jsx`. Add a nav link in the header that goes from the home page to the about page and back."

**The sign-off checklist before moving on:**
- Does the page render without errors?
- Does it look correct on desktop?
- Does it look correct on mobile?
- Does every interactive element respond?
- Is the file structure clean?

---

### Chapter 10 — Adding Real Functionality

A page that renders is not the same as an app that works. Functionality means the app responds to user input and does something with it.

**The four building blocks of functionality:**
- **Forms** — collecting input from the user
- **Buttons** — triggering actions
- **State** — the app remembering something mid-session
- **Data persistence** — saving something so it survives a page refresh

**Prompting a form:**
> "Add a form to `pages/index.jsx` with two fields: task name (text input) and due date (date picker). When the user submits, add the task to a list displayed below the form. Validate that both fields are filled before submitting."

**Prompting for local storage (no database needed):**
> "Save the task list to `localStorage` so it persists when the user refreshes the page. Load existing tasks on page load."

**When you need a database.** Local storage breaks when multiple users need to share data, or when data needs to sync across devices. The simplest starting option is Supabase — a hosted database with a straightforward API.

Prompt for it like this:
> "I want to store tasks in a Supabase database instead of localStorage. I have a Supabase project set up. Create a `tasks` table with columns: id, name, due_date, completed. Show me the SQL to run in Supabase, then update the app to read and write from it."

**Connecting to an external API:**
> "This app needs to fetch weather data. I have an API key for OpenWeatherMap. Add a weather widget to the top of the page that shows the current temperature for a city the user types in."

---

### Chapter 11 — Shipping What You Built

Deployment means making your app accessible via a URL anyone can open. It's simpler than most beginners expect.

**The simplest path: Vercel.** Push your project to GitHub, connect it to Vercel, and your app is live in under five minutes. Every time you push a new commit, Vercel rebuilds automatically.

**Prepare for deployment with a prompt:**
> "I'm about to deploy this to Vercel. Check for any environment variables that need to be set, any build errors that would prevent deployment, and make sure the project has a `package.json` with a build script."

**Preview links vs. production links:**
- Vercel gives you a preview URL for every branch — use this for testing
- Your main branch deploys to your production URL — only push there when it works

**What to do after you ship:**
Share it with one person before building more. Their feedback is more useful than any feature you could add next. Observe how they actually use it — not how you expected them to.

---

## Volume 4 — Going Further

---

### Chapter 12 — Managing a Growing Project

Projects get harder to manage as they grow — not because the code is more complex, but because Claude has no memory between sessions. Every new session starts cold.

**The SPEC file.** Create a file called `SPEC.md` in your project root. It's a living document that describes your project. Claude reads it at the start of every session.

**What your SPEC.md should include:**
```markdown
# Project Name

## What it is
One paragraph description.

## Tech stack
React + Tailwind + Supabase

## File structure
/pages      — route pages
/components — reusable UI components
/lib        — utility functions and API clients

## Current state
What's built and working.

## Known issues
What's broken or incomplete.

## Next steps
The next 1–3 things to build.
```

**Starting every session:**
> "Read @SPEC.md before doing anything. That's the current state of the project. I want to add [next feature]."

**When to refactor.** Signs your codebase needs cleanup:
- The same logic appears in three or more places
- You're afraid to change one file because it might break others
- Claude keeps making the same mistake across sessions

Refactoring prompt:
> "Don't add any new features. Review the codebase and consolidate any repeated logic, simplify any components that are doing too much, and update SPEC.md to reflect the current structure."

---

### Chapter 13 — When Vibe Coding Breaks Down

There are real limits. Knowing them prevents wasted time.

**Three signs you've hit the limits:**

**1. Claude keeps introducing the same bug.** This usually means the feature is architecturally tangled. The fix is to simplify the feature, not to keep prompting.

**2. The context is too large.** When your project has dozens of files, Claude can lose track of what connects to what. Break large features into smaller isolated pieces, or split the project into modules.

**3. You're copying logic across files.** If you have the same function pasted in multiple places, and Claude keeps editing one but not the others, you have a structural problem. Ask Claude to refactor before adding anything new.

**The copy-paste trap.** Duplicated code is the most common cause of compounding errors in vibe-coded projects. Every copied block is a future bug in two places instead of one.

**When to bring in a developer:**
- The app handles sensitive user data (payment, medical, legal)
- Performance is critical and you're hitting real bottlenecks
- The architecture needs a design you can't describe clearly

**The restart protocol.** If a project is genuinely broken and three sessions haven't fixed it:
1. Save the SPEC.md and any working components you want to keep
2. Start a new project folder
3. Paste the SPEC and ask Claude to scaffold the project cleanly
4. Rebuild only the features that worked

What to leave behind: any code you can't explain the purpose of.

---

### Chapter 14 — Building the Vibe Coding Habit

Consistency matters more than the length of any single session. One focused hour a week compounds faster than occasional five-hour marathons.

**The one-hour build session format:**
- 10 min — review last session, update SPEC.md
- 40 min — build one thing
- 10 min — test, document what changed, define next step

**Keeping an ideas list.** Don't rely on remembering what to build next. Keep a running list — even a plain text file — of ideas, features, and fixes. Review it before each session. Pick one thing.

**Five questions to ask after every session:**
1. Does the app work end-to-end right now?
2. What did I learn about scoping this time?
3. What would I prompt differently?
4. Is the SPEC.md up to date?
5. What's the one thing to build next?

**The compounding skill curve.** Each project makes the next one faster. Not because you've learned to code — but because you've learned how to describe what you want more precisely. That skill transfers to every tool and every project.

**The one rule, restated:** description quality determines output quality. Everything in this course — the briefs, the scoped prompts, the fix formulas, the SPEC file — is a way to be more specific about what you want. That's the skill.

---

*Vibe Coding 101 · Vol 1–4 · Build something small this week.*