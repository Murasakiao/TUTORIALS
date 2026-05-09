Prompt Engineering 101: Essentials
From Zero to Agent-Ready — Compact Edition
Volume 1 — Understanding Models & Core Techniques
Part 1 — What the Model Is Actually Doing
Slides:
What a language model is doing at a mechanical level: predicting the next token
Why the model has no intentions, goals, or understanding — only pattern matching
Why the model is confidently wrong: hallucination explained simply
The context window: what it is, why it has limits, and why those limits matter
What the model cannot do no matter how well you prompt it
Part 2 — The Anatomy of a Prompt
Slides:
The four layers of every prompt: role + instruction + context + output format
How the model weighs each layer
Why most prompts fail at the instruction layer, not the context layer
Recency bias: why the model pays more attention to the end of your prompt
The diagnostic question: what did my prompt leave ambiguous?
Part 3 — Role + Instruction Design
Slides:
What role prompting is and why it works
Specificity in roles: "expert" vs "senior electrical engineer with 10 years in power systems"
Action verbs that produce reliable outputs: analyze, extract, classify, rewrite, compare
Vague verbs that produce unreliable outputs: help, discuss, think about
Breaking complex instructions into numbered steps
Negative instructions: what not to do is often clearer than what to do
Side-by-side: a prompt without a role vs the same prompt with a well-defined role
Part 4 — Context + Output Format Control
Slides:
The difference between context and instruction
Using delimiters to separate context from instruction: XML tags, triple quotes, markdown headers
The formats you can reliably request: plain text, JSON, markdown, lists, tables
Using examples to anchor the output format
Controlling length: word counts, sentence counts, section limits
Controlling tone: formal, conversational, technical, plain English
When the model ignores your format instructions and what to do about it
Part 5 — Few-Shot Prompting
Slides:
What few-shot prompting is: showing the model examples before asking
Zero-shot vs one-shot vs few-shot: the difference and when each applies
How examples teach the model format, tone, and reasoning style simultaneously
Choosing good examples: representative, diverse, and correctly labeled
How many examples is enough: usually 2–3
Negative examples: showing the model what you do not want
Common few-shot mistakes and what they produce
Part 6 — Iterating a Bad Prompt
Slides:
The prompt iteration mindset: bad output is diagnostic data, not failure
The four sources of bad output: wrong role, unclear instruction, missing context, wrong format
The diagnostic loop: identify → hypothesize → change one thing → retest
Why you should change one variable at a time
Reading the output to find where the model got confused
CTA: take one prompt giving you bad output and run it through the diagnostic loop
Volume 2 — Advanced Patterns & Agent Prompting
Part 1 — Prompt Chaining
Slides:
What prompt chaining is: using the output of one prompt as input to the next
Why chaining produces better results than one large prompt
The artifact model: every prompt in a chain produces something the next one consumes
Designing clean handoffs: what format should the first prompt output for the second to consume
Error propagation: how a bad output in step one degrades every step after
Real example: a three-prompt chain for researching and writing a piece of content
Part 2 — The Generator + Critic Pattern
Slides:
What the Generator + Critic pattern is and why it works
Why self-review in a single prompt is unreliable
Writing the generator prompt: focused on producing, not evaluating
Writing the critic prompt: a scoring rubric, not just "is this good?"
The refinement prompt: consuming critic feedback and producing an improved output
Real example: generating a blog draft and running it through a critic
Part 3 — How Agent Prompting Differs from Chat Prompting
Slides:
The fundamental difference: chat prompts are one-shot, agent prompts run in a loop
Why agents surface prompt weaknesses that chat interactions hide
The three new failure modes that only appear in agents: role drift, tool misuse, loop failure
How the model's behavior compounds across multiple reasoning steps
Why constraint design is more critical for agents than for chat
The agent prompting mindset: writing for a system, not a conversation
Part 4 — Writing the System Prompt for an Agent
Slides:
The system prompt as a job contract: role + responsibilities + constraints + output format
Why agent system prompts need to be longer and more precise than chat system prompts
Role definition for agents: identity, expertise, and behavioral defaults
Responsibility scoping: what the agent is and is not allowed to do
Constraint injection: hard limits the agent cannot reason its way around
Output format instructions that survive a multi-step reasoning loop
Side-by-side: a weak agent system prompt vs a strong one for the same task
Part 5 — Tool Description Prompting
Slides:
Why the tool description is the most important prompt you write for an agent
How the model decides which tool to call: it reads the description, not the code
Anatomy of a tool description: name + purpose + when to use it + when not to use it
Writing tool descriptions that prevent misuse
Parameter descriptions: how to tell the model what each argument expects
Describing tool limitations: what the tool cannot handle
Side-by-side: a vague tool description vs a precise one and the behaviors they produce
Part 6 — Prompting the ReAct Loop
Slides:
What the ReAct loop looks like from the prompt's perspective
How to structure the system prompt so the model reasons before it acts
Observation prompting: how to feed tool results back into the reasoning loop
Stop condition prompting: how to tell the agent when it is done
Loop failure modes: getting stuck, looping endlessly, premature termination
Prompting the agent to self-correct when it detects it is stuck
CTA: take one agent you have already built and rewrite its system prompt using everything in this volume