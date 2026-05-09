Vibe Coding 101: Build Real Things Without Being a Developer
A Beginner's Guide to the Cursor + Claude Stack
Volume 1 — The Mindset & the Stack
Part 1 — What Vibe Coding Actually Is
Slides:
The old way: you had to learn to code before you could build anything
What vibe coding is: directing an AI to write code on your behalf
Why this is different from just asking ChatGPT to write code
You are not the programmer — you are the architect and the reviewer
What you can realistically build as a complete beginner
What vibe coding cannot do: why judgment still matters
The one skill that makes everything else work: knowing what you want clearly enough to describe it
Part 2 — Understanding the Cursor + Claude Stack
Slides:
What Cursor is: a code editor built on top of VS Code with AI baked in
What Claude is doing inside Cursor: reading your entire codebase, not just your message
Why this combination is more powerful than a chatbot: full project context awareness
The three ways to interact with Cursor: Chat (Cmd+L), Agent mode (Cmd+I), and inline edits (Cmd+K)
Chat for questions and explanations, Agent for building across multiple files, inline edits for targeted single changes
How Claude sees your project: files, folders, and the codebase as a whole using @-mentions
What you do not need to know: syntax, frameworks, debugging from scratch
Setting up Cursor for the first time: a quick walkthrough
Part 3 — The Vibe Coding Mindset
Slides:
Shift one: you are a product thinker, not a programmer
Shift two: imperfect and working beats perfect and unbuilt
Shift three: errors are normal — Claude will fix them too
Why beginners quit: they treat the first broken output as failure
The build loop: describe → generate → review → fix → repeat
How to stay unblocked: every error has a prompt that fixes it
CTA: write down one thing you have wanted to build but thought you couldn't — that is your first project
Volume 2 — The Core Workflow
Part 1 — Starting a Project the Right Way
Slides:
Why jumping straight into prompting breaks most projects
The project brief: writing what you want to build before touching Cursor
The four things your brief needs: what it is, who it is for, what it does, what it looks like
Folder structure basics: what Claude needs to see to help you properly
Starting from a template vs starting from scratch: when each is better
How to tell Claude the full context of your project at the start of every session using @-mentions
Real example: a project brief for a simple habit tracker web app
Part 2 — Writing Prompts That Build
Slides:
Why vibe coding prompts are different from regular prompts
The anatomy of a good build prompt: what to build + where it goes + how it should behave
Scope control: ask for one thing at a time, not the whole app
Describing UI in plain English: you do not need design vocabulary
Referencing existing files with @filename so Claude knows what already exists before adding more
What to do when Claude builds the wrong thing: the correction prompt
Side-by-side: a vague build prompt vs a clear one and what each produces
Part 3 — Reading the Output Without Knowing Code
Slides:
You do not need to understand the code — you need to understand the behavior
The three questions to ask every time Claude generates something: does it run, does it look right, does it do what I asked
How to run your project locally: the basics every beginner needs
Reading error messages as a non-developer: what to copy, what to ignore
When to paste the error directly into Cursor Chat
When the output looks wrong but there is no error: the visual review prompt
Building the habit of testing every change before asking for the next one
Part 4 — The Fix Loop
Slides:
Errors are not failures — they are the normal state of building software
The fix prompt formula: here is the error + here is what I expected + fix it
Why you should never manually edit code as a beginner
Pasting error messages directly into Cursor Chat: what Claude does with them
When Claude's fix creates a new error: the escalation prompt
When to start over vs when to keep fixing
The rule: if you have gone three fixes deep on the same error, describe the feature from scratch
Volume 3 — Building Real Things
Part 1 — Scoping Your First Build
Slides:
The beginner trap: building something too big to finish
The MVP mindset: what is the smallest version that still does the thing
How to break a big idea into a sequence of small builds
The feature list exercise: write every feature, then cut it in half, then cut it again
What to build first: always the core action, never the settings page
Estimating scope as a non-developer: the one-session rule
Real example: scoping a simple link-in-bio tool down to a first buildable version
Part 2 — Building Page by Page
Slides:
Why building one page at a time beats building everything at once
The page prompt structure: layout + components + behavior + data
How to describe a layout without knowing CSS: use spatial language
Telling Claude what a component should do, not how to build it
Connecting pages: how to prompt Claude to add navigation between views
Reviewing each page before moving to the next: the sign-off checklist
Real example: prompting a home page, then a detail page, then wiring them together
Part 3 — Adding Real Functionality
Slides:
The difference between a static page and a working app
What functionality means for a beginner: forms, buttons, data, and state
How to describe a form and what it should do with the data
Prompting for local storage: saving data without a database
When you need a database: the simplest option for beginners (Supabase)
Prompting Claude to connect your app to an external tool or API
Real example: adding a form that saves entries and displays them on the same page
Part 4 — Shipping What You Built
Slides:
What deployment means: making your app accessible to anyone with a link
The simplest deployment path for beginners: Vercel in under five minutes
How to prompt Claude to prepare your project for deployment
What a domain name is and whether you need one yet
Sharing your build: the difference between a preview link and a production link
What to do after you ship: collecting feedback before building more
CTA: deploy one thing this week — even if it is unfinished — and share the link with one person
Volume 4 — Going Further
Part 1 — Managing a Growing Project
Slides:
Why projects get harder to manage as they grow
The context problem: Claude does not remember your last session
How to write a project summary Claude can read at the start of every session
The SPEC file: a living document that describes your entire project
Using @file to pin your SPEC directly into every new Agent session
When to refactor: signs that your codebase is becoming a mess
How to ask Claude to clean up without breaking what works
The golden rule: always describe what you have before asking for what's next
Part 2 — When Vibe Coding Breaks Down
Slides:
The three signs you have hit the limits of pure vibe coding
When complexity outgrows what Claude can hold in context
The copy-paste trap: why duplicating code across files causes compounding errors
When to bring in a developer vs when to simplify your scope
The restart protocol: how to cleanly begin a new version of a broken project
What to salvage and what to leave behind
The honest truth: vibe coding is a starting point, not a ceiling
Part 3 — Building the Vibe Coding Habit
Slides:
Why consistency beats intensity: building something small every week
The one-hour build session: a repeatable format for making progress
Keeping an ideas list: capturing what you want to build before you sit down
Reviewing your own builds: the five questions to ask after every session
How each project makes the next one faster: the compounding skill curve
The builder identity: you do not need a CS degree to ship real things
CTA: commit to one build per week for the next four weeks — scope it small enough that you cannot fail