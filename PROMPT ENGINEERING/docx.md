# Prompt Engineering 101
### From Zero to Agent-Ready — A Practical Guide

---

## How to Use This Course

Each chapter builds on the last. Read linearly the first time, then use it as a reference. Every technique is paired with a concrete example — the fastest way to internalize the concept is to immediately apply it to a prompt you're already using.

---

# Volume 1 — Foundations

---

## Chapter 1: What the Model Is Actually Doing

Before you can write better prompts, you need an accurate mental model of what you're prompting.

### It predicts tokens, not thoughts

A language model has one job: predict the most likely next token given everything before it. It does this billions of times per response. There are no goals, no intentions, no understanding — only patterns learned from training data.

This is not a limitation to work around. It's the foundation for everything.

### Why hallucination happens

The model doesn't "know" things the way you do. It generates text that is statistically consistent with its training. When the correct answer isn't strongly represented in the patterns it learned, it still produces confident text — just wrong confident text.

**Implication:** Never assume confidence means accuracy. Ask the model to cite, reason, or hedge when accuracy matters.

### The context window

The model can only "see" what's inside its context window — everything from the system prompt to the current message. It has no memory outside of this. Once a conversation exceeds the context limit, earlier content falls off.

**Implication:** In long conversations or agentic tasks, critical instructions belong at the start *and* end of your prompt — not buried in the middle.

### What prompting cannot fix

Some things aren't a prompting problem:
- The model doesn't know events after its training cutoff
- It can't perform precise arithmetic reliably
- It can't access external systems unless given a tool
- It has no persistent memory between sessions (without infrastructure)

Knowing these limits saves hours of debugging.

---

## Chapter 2: The Anatomy of a Prompt

Every prompt — simple or complex — has the same four layers. Most failures trace back to one of them.

### The four layers

| Layer | What it does | Common mistake |
|---|---|---|
| **Role** | Sets the persona and focus | Too vague ("be an expert") |
| **Instruction** | Tells the model what to do | Vague verbs ("help me with") |
| **Context** | Supplies the information it needs | Buried inside the instruction |
| **Output format** | Specifies how to structure the answer | Placed at the start instead of the end |

### Why order matters

The model has a recency bias — it weighs the end of your prompt more heavily. Format instructions buried in the middle get ignored. **Put your output format last.**

### The compression test

Before sending any prompt, ask: *If the model had to summarize my request in one sentence, what would it say?*

That sentence is what it's actually optimizing for. If that sentence doesn't match your intent, rewrite until it does.

### Example

**Weak prompt:**
```
Help me with my email about the project delay.
```

**Strong prompt (all four layers present):**
```
You are a professional business writer. [Role]

Rewrite the email below to be clear, concise, and to acknowledge the delay without over-apologizing. [Instruction]

<email>
Hi, so the project is going to be late. We ran into some problems and it's taking longer. Sorry about that.
</email>
[Context]

Output a single revised email, 3–5 sentences, formal tone. [Format]
```

---

## Chapter 3: Role + Instruction Design

### Why role prompting works

Assigning a role narrows the model's focus before generation starts. "You are a tax attorney" activates different patterns than "you are a creative writer" — vocabulary, reasoning style, and assumed audience all shift.

### Specificity is everything

**Vague role:** `"You are an expert."`
The model picks any direction — unpredictable output.

**Specific role:** `"You are a senior electrical engineer with 10 years in industrial power systems."`
Narrow focus, consistent tone, predictable expertise level.

A good role includes: **profession + seniority + domain specialization** (when relevant).

### Action verbs vs vague verbs

The instruction verb is the most important word in your prompt. Choose it deliberately.

| Vague (avoid) | Specific (use) |
|---|---|
| help | analyze |
| discuss | extract |
| think about | classify |
| go over | rewrite |
| explore | compare |
| look at | summarize |

**Vague:** `"Think about what's wrong with this code."`
**Specific:** `"Identify every bug in this code and classify each as a logic error, syntax error, or edge case."`

### Negative instructions

Telling the model what *not* to do is often clearer than describing what you want. Use both.

```
Rewrite this paragraph for clarity.
- Do not change the meaning or omit any facts.
- Do not use bullet points.
- Do not start sentences with "Additionally" or "Furthermore."
```

### A note on modern Claude models

Claude 4.x models are highly literal — they do exactly what you ask and little else. This is a feature, not a bug: vague prompts now produce reliably vague output, which makes it easier to diagnose what went wrong.

---

## Chapter 4: Context + Output Format Control

### Context vs instruction

These are different jobs.

- **Context** = what the model needs to *know*
- **Instruction** = what the model needs to *do*

Mixing them produces inconsistent results. Separate them explicitly.

### Delimiters

Use delimiters to make the boundary unmistakable:

```
Analyze the customer feedback below and identify the top 3 complaints.

<feedback>
The app crashes every time I try to upload a photo. The support team took 5 days to respond. 
The interface is confusing and I couldn't find the settings.
</feedback>

Output: a numbered list, one complaint per line, each under 15 words.
```

Good delimiter options: XML tags `<context>`, triple quotes `"""`, or markdown headers `### Input`.

### Format options you can reliably request

- Plain prose
- JSON (specify the exact keys)
- Markdown with specific heading structure
- Numbered or bulleted lists
- Tables (specify columns)
- Code blocks
- Length-constrained output (`"under 100 words"`, `"exactly 3 sentences"`)

### Show, don't describe

Describing a format is less reliable than showing one.

**Weak:** `"Format your answer as a structured summary."`

**Strong:**
```
Format your answer exactly like this:

Problem: [one sentence]
Root cause: [one sentence]
Recommended fix: [one to three sentences]
```

The model will follow the pattern far more consistently.

---

## Chapter 5: Few-Shot Prompting

### What it is

You provide examples of the task before asking the model to do it. The examples teach format, tone, and reasoning simultaneously — more efficiently than any description.

### How many examples

- **0-shot:** No examples. Works for simple, well-defined tasks.
- **1-shot:** One example. Good for format anchoring.
- **2–3 shot:** Usually the sweet spot. Covers format *and* variation.
- **5+:** Rarely better. Reserve for tasks with non-obvious patterns.

### Choosing good examples

Good examples are:
- Representative of the range of inputs you'll send
- Correctly labeled (wrong labels cause more damage than no examples)
- Diverse — don't pick three similar cases

### Negative examples

Showing what you *don't* want is often the clearest instruction available.

```
Input: "The new policy is terrible and makes no sense."
Bad output: "The customer is upset about the new policy."
Good output: "Customer complaint: new policy — reason for dissatisfaction unclear, follow-up needed."
```

### The quality trap

One wrong example undoes two correct ones. If you're not confident an example is correct, leave it out.

---

## Chapter 6: Chain-of-Thought + Iteration

### What chain-of-thought is

You instruct the model to reason before it answers. This improves accuracy on tasks that require multiple steps or inference.

**Trigger phrase:** `"Think step by step before responding."`

Or more explicitly:
```
Before giving your answer, reason through the problem in a <thinking> block.
Then provide your final answer after </thinking>.
```

### When to use it

**Use it for:**
- Multi-step math or logic
- Tasks with a single correct answer
- Diagnosing complex problems
- Anything where "show your work" would help a human

**Skip it for:**
- Simple reformatting tasks
- Short creative outputs
- Classification with clear rules already in the prompt

### Bad output is diagnostic data

When output is wrong, don't rewrite the whole prompt. Diagnose first.

**The four sources of failure:**
1. Wrong role — model is optimizing for the wrong context
2. Unclear instruction — ambiguous verb or missing constraint
3. Missing context — model didn't have what it needed
4. Wrong format — output format instructions were vague or misplaced

**The diagnostic loop:**
1. Identify which layer failed
2. Form a hypothesis about why
3. Change **one thing**
4. Retest

Changing multiple variables at once means you can't know what fixed it.

---

# Volume 2 — Advanced Patterns & Agent Prompting

---

## Chapter 7: Prompt Chaining

### What it is

Instead of one large prompt, you break the task into a sequence. Each prompt produces an artifact — a concrete output — that becomes the input for the next.

### Why it's better than one long prompt

One prompt trying to do everything spreads the model's "attention" across competing objectives. Chained prompts give each step a single job.

### Example: Writing pipeline

```
Prompt 1 (Research):
Summarize the three most important findings from the document below. 
Output: a bullet list, one finding per bullet, each under 30 words.
<document>...</document>

Prompt 2 (Outline):
Using the research summary below, create a 5-section article outline.
<summary>[output from Prompt 1]</summary>

Prompt 3 (Draft):
Write section 2 of the article based on the outline below.
<outline>[output from Prompt 2]</outline>
```

### The handoff problem

The most common failure in chaining: Prompt 1 produces output in a format that Prompt 2 wasn't designed to handle.

**Rule:** Design the output format of each step with the next step's input in mind — before you write either prompt.

### Error propagation

A bad output at step 1 degrades every step after it. The earlier the failure, the worse the compounding. Validate intermediate outputs before passing them forward.

---

## Chapter 8: The Generator + Critic Pattern

### Why self-review fails

When you ask a model to generate *and* evaluate in the same prompt, it's biased toward its own output. The review is rarely useful.

### Split the job

**Generator prompt** — focused on producing. No judgment.
```
Write a cold outreach email for a B2B SaaS product targeting HR managers.
Output: the email only, no commentary.
```

**Critic prompt** — evaluates against a specific rubric.
```
Evaluate the email below against this rubric:
1. Subject line: does it avoid spam trigger words? (0–2)
2. Opening line: does it reference the recipient's context? (0–2)
3. Value proposition: is it specific and outcome-focused? (0–2)
4. CTA: is it low-friction and single-action? (0–2)

<email>[generator output]</email>

Output: a score for each dimension + one specific improvement per dimension.
```

**Refinement prompt** — sends the critique back to the generator.
```
Rewrite the email below using the critique provided.
<email>[original]</email>
<critique>[critic output]</critique>
```

### Key principle

Give the critic a rubric with specific dimensions. "Is this good?" produces unusable feedback. "Does the opening line reference the recipient's role or company?" produces actionable feedback.

---

## Chapter 9: How Agent Prompting Differs

### The fundamental shift

Chat prompts are one-shot — one input, one output, done. Agent prompts run in a loop. The model reasons, acts (calls a tool), observes the result, reasons again, acts again.

This changes everything.

### Failure modes unique to agents

**Role drift:** The agent gradually forgets its defined role over many reasoning steps. By step 8, it may be behaving like a general assistant rather than the specialized role you defined.

**Tool misuse:** When tool descriptions are vague, the model picks the wrong tool or passes wrong parameters. In a loop, this cascades.

**Loop failure:** The agent gets stuck, loops endlessly, or stops too early because stop conditions weren't explicitly defined.

### Why weaknesses compound

A prompt weakness that produces a 10% failure rate in chat produces a much higher failure rate in an agent — every step is another chance for the error to manifest and compound.

**Implication:** Write agent prompts with more precision than you think is necessary.

---

## Chapter 10: Writing the Agent System Prompt

### Think of it as a job contract

An agent system prompt defines:
1. **Role** — who the agent is and what it specializes in
2. **Responsibilities** — what it is supposed to accomplish
3. **Constraints** — hard limits it cannot reason its way around
4. **Stop conditions** — exactly when it is done

All four must be explicit. Missing any one of them produces unpredictable behavior.

### Example: weak vs strong

**Weak:**
```
You are a helpful research assistant. Use the tools available to answer user questions.
```

**Strong:**
```
You are a research assistant specialized in competitive analysis.

Responsibilities:
- Search for information using the web_search tool
- Synthesize findings into structured summaries
- Flag any information you could not verify

Constraints:
- Do not make claims without a source
- Do not call web_search more than 5 times per task
- Do not fabricate citations

Stop condition: You are done when you have produced a summary that addresses every sub-question in the user's request. Output "TASK COMPLETE" when finished.
```

### Constraint injection

Some constraints should be unambiguous hard limits, not soft guidelines. Phrase them as imperatives:

- ✅ `"Never call the delete_record tool without first calling get_record."`
- ❌ `"Try to verify records before deleting them."`

The first is a constraint. The second is advice the model can rationalize ignoring.

---

## Chapter 11: Tool Description Prompting

### How tool selection works

The model decides which tool to call by reading the description. Not the code, not the function signature — the *description*. A vague description leads to wrong tool calls.

### Anatomy of a good tool description

```
Name: search_knowledge_base

Purpose: Searches the internal product documentation for answers to user questions.

When to use: Use this tool when the user asks about product features, pricing, 
integrations, or troubleshooting steps.

When NOT to use: Do not use this tool for general knowledge questions, 
current events, or anything not related to the product.

Parameters:
- query (string): The search query. Should be a concise phrase, not a full sentence.
  Example: "export to CSV" not "How do I export my data to a CSV file?"
- max_results (integer): Number of results to return. Default 3. Max 10.
```

### The "when NOT to use" section

This is frequently omitted and frequently the source of tool misuse. If two tools have overlapping domains, the model needs to know which takes precedence and when.

### Parameter descriptions matter

`query (string)` — useless.
`query (string): A concise 2–5 word phrase representing the search intent. Do not pass full sentences.` — useful.

---

## Chapter 12: Prompting the ReAct Loop

### What ReAct is

ReAct (Reason + Act) is the standard agent loop:
1. **Reason** — think about what to do next
2. **Act** — call a tool
3. **Observe** — read the result
4. **Repeat** — until the stop condition is met

Your system prompt needs to explicitly structure this loop.

### Structuring the reasoning step

Tell the model to reason before every action:

```
Before calling any tool, write a brief reasoning step explaining:
- What you know so far
- What you still need to find out
- Which tool you are about to call and why
```

This prevents the model from taking reflexive tool calls without thinking.

### Observation prompting

How tool results re-enter the reasoning loop matters. If the model doesn't know how to interpret a tool result, it will either ignore it or hallucinate an interpretation.

```
After each tool call, interpret the result and note:
- What new information this gives you
- Whether this changes your plan
- What the next step is
```

### Stop conditions

This is the most commonly forgotten element. The agent must know explicitly when it is done.

**Vague:** `"Complete the task and report back."`

**Precise:**
```
You are done when all of the following are true:
1. Every sub-question in the original request has been addressed
2. All claims have a source cited
3. You have output the final summary in the specified format

When done, output exactly: "TASK COMPLETE"
Do not call any more tools after outputting "TASK COMPLETE".
```

### Loop failure modes

| Failure | Cause | Fix |
|---|---|---|
| Stops too early | Stop condition too easy to trigger | Make stop condition more specific |
| Loops endlessly | No stop condition or it's never satisfied | Add a max-step constraint |
| Gets stuck on error | No error handling instruction | Add: "If a tool returns an error, log the error and proceed with the next step" |

---

## Quick Reference: The One Rule

Every technique in this course is a way to be more specific.

- **Role design** → specific focus
- **Action verbs** → specific task
- **Delimiters** → specific boundaries
- **Few-shot examples** → specific format
- **Chain-of-thought** → specific reasoning steps
- **Tool descriptions** → specific selection criteria
- **Stop conditions** → specific completion state

**Precision beats vagueness. Every time.**

---

*Prompt Engineering 101 — Vol 1 & Vol 2*