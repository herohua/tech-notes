---
title: "Taste in software: the skill that matters more in the AI era"
date: 2026-05-19
tags: [software-engineering, ai, craft]
publish: true
---

## TL;DR

- **Taste** is the judgment that picks *good* out of merely *working* — what to leave out, where to draw the seam, when to stop.
- It shows up as one underlying instinct — **proportion, restraint, honesty** — applied at every altitude: product, architecture, API, implementation, ops.
- Anthropic's engineering blog illustrates this well: each post is really one variation of "don't build/include/claim what you don't need" (build effective agents, write fewer tools, minimize context, keep the safety classifier reasoning-blind, name where auto mode is worse).
- **Why it matters more now:** AI makes producing plausible code nearly free. The scarce skill is rejecting the nine outputs that aren't right.
- **How to develop it:** read code by people you respect, maintain things for years, review in both directions, rewrite the same thing multiple ways, cultivate a delete reflex, study failures. For AI-native work: read generated diffs critically, throw away what feels off, specify constraints rather than code, resist volume.

---

When an AI can produce *a* working implementation in seconds, the scarce skill is no longer typing code — it's deciding which of ten plausible outputs is the right one, and rejecting the other nine. That decision is **taste**.

Taste is the judgment that distinguishes *technically correct* from *actually good*. It's the felt sense for which abstraction to pick, when to stop, what to leave out, and what will age well — the stuff that doesn't show up in tests or type checkers.

This post breaks taste into its components, shows how the same instinct operates at every level of the stack, and grounds each dimension in real design decisions from [Anthropic's engineering blog](https://www.anthropic.com/engineering).

---

## What taste actually consists of

A few concrete dimensions people lump under the word:

- **Proportion** — matching the weight of a solution to the weight of the problem.
- **Restraint** — knowing what *not* to build.
- **Naming & shape** — the function does one thing; its name says that thing.
- **Boundary placement** — where you draw the line between modules; who owns which state.
- **Failure aesthetics** — what happens when things go wrong, and where errors surface.
- **Honesty about tradeoffs** — refusing to oversell; naming the axis where your thing is worse.
- **Time horizon** — sensing what will read well in six months, not just what's clever today.

The unifying thread: at every level, taste answers the same question — *given many things that would technically work, which is right here, and why?*

---

## The same taste, at every altitude

What changes between levels isn't the underlying instinct — it's the unit of judgment.

| Scale | What taste decides |
|---|---|
| Product / UX | Which feature *not* to ship. When a default beats a setting. |
| System architecture | Where the seams go. Sync vs async. One service or three. |
| Module / API design | What the function signature looks like. What's public. |
| Implementation | Naming, control flow, where errors surface, what's worth a comment. |
| Operational | What to log, what to alert on, what failure looks like at 3am. |

A person with taste at one level often has it at others, because *proportion, restraint, honesty about tradeoffs* transfer. The best builders feel "coherent" end-to-end — product, architecture, and code share one sensibility.

The levels also reinforce each other: a clean product decision ("we don't support offline") removes a hundred implementation decisions. Bad architectural taste forces UX compromises ("we can't do that because the data model…"). Honest error handling shapes what the product can credibly promise.

---

## Taste in the wild: Anthropic's engineering blog

The clearest way to learn taste is to watch it operate. Each post below illustrates a dimension.

### 1. Proportion — match the machinery to the problem

["Building effective agents"](https://www.anthropic.com/engineering/building-effective-agents) opens by telling people *not* to build agents:

> "Sometimes [the right answer is] not building agentic systems at all… a single optimized LLM call with retrieval often suffices."

And warns against frameworks:

> Frameworks "often create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug."

The tasteless version of this post would have led with an architecture diagram. The tasteful version leads with "do you even need this?"

### 2. Restraint — subtraction as a design act

["Writing effective tools for agents"](https://www.anthropic.com/engineering/writing-tools-for-agents):

> "More tools don't always lead to better outcomes."
> "We recommend building a few thoughtful tools targeting specific high-impact workflows."

The tasteless default is to wrap every API endpoint as a tool — it feels productive and is easy to justify. The tasteful move is to consolidate: one `schedule_event` instead of `list_users` + `list_events` + `create_event`. Fewer surfaces, less confusion, better outcomes.

### 3. Boundary placement — where you draw the seams

["Claude Code auto mode"](https://www.anthropic.com/engineering/claude-code-auto-mode) describes a safety classifier that is **reasoning-blind by design**: it sees only user messages and raw tool calls — never the agent's prose or tool outputs.

Why this is taste, not just engineering: the obvious design is "give the safety classifier more context so it makes better decisions." That's wrong, for a non-obvious reason — more context lets the agent (or injected content) talk the classifier into approving. **Drawing the boundary tighter makes the system more robust.** Recognizing that inversion is taste.

### 4. Failure aesthetics — fail where the system can act

Same post, on what happens when the classifier denies an action: it returns the denial as a tool result, so the agent retries a safer path. Escalation to a human happens only after 3 consecutive or 20 total denials.

Tasteless failure handling: throw, halt, page the user. Tasteful failure handling: fail in a way the system can act on, with thresholds matched to how real workflows degrade.

### 5. Honesty about tradeoffs — name where you're worse

Same post again, on its own product:

> Auto mode is "not a drop-in replacement for careful human review on high-stakes infrastructure" — it's an upgrade over skipping permissions, arguably a regression versus diligent manual review.

The tasteless version sells auto mode as strictly better. The tasteful version names the axis where it's *worse*, because credibility compounds and overclaiming corrodes it. This is the same instinct as good error handling — surface the truth where it can be acted on.

### 6. Working with the grain of a scarce resource

["Effective context engineering"](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents):

> "Find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome."
> "Minimal does not necessarily mean short."

That second line is the tasteful refinement. A tasteless reading of "minimal" is "shortest possible prompt." The actual judgment is *high signal-to-noise*, which sometimes means more tokens, sometimes fewer. The post then expresses the same instinct at a different scale: prefer "just-in-time" retrieval over pre-loading everything.

### 7. Product taste — solve the real problem, not the stated one

Auto mode noticed that users approve 93% of permission prompts. So the prompts aren't really gating anything — they're just adding friction. The tasteful response isn't "better prompts," it's *"the prompt model is wrong; replace it."*

The tools post makes a parallel observation: the failure mode of giving an agent API access isn't capability — it's the agent burning context on low-signal responses. So the fix isn't more tools, it's `response_format: concise` and pagination.

In both cases, the tasteless engineer optimizes the thing in front of them. The tasteful one steps back and asks whether it's the right thing.

---

## The pattern across all of them

Read side by side, the same instinct surfaces in different costumes:

| Post | The instinct expressed as… |
|---|---|
| Building effective agents | …don't build the system you don't need |
| Writing tools for agents | …don't build the tools you don't need |
| Context engineering | …don't include the tokens you don't need |
| Auto mode (classifier) | …don't give the classifier the context it doesn't need |
| Auto mode (positioning) | …don't claim the safety you can't deliver |

One taste — **proportion plus restraint plus honesty** — applied at five different altitudes. Taste isn't five skills; it's one judgment showing up at every level of the stack.

---

## How to develop taste

Taste is pattern recognition built from high-volume, high-feedback exposure. The shortcuts that actually work:

1. **Read code by people you respect** — not tutorials. Real codebases (Redis, SQLite, Django, your language's standard library). Notice what they *don't* do.
2. **Maintain something for years.** Nothing teaches taste like living with your own decisions after the context has faded. Greenfield work hides the cost of bad calls.
3. **Do code review — both directions.** Reviewing forces you to articulate *why* something feels off. The articulation is where taste becomes transferable.
4. **Rewrite the same thing three ways.** Functional, OO, procedural. The discomfort of the wrong fit teaches more than any style guide.
5. **Read the diff before you commit.** Ask: "would I be happy to find this in someone else's PR?" If no, fix it now.
6. **Develop a delete reflex.** Every week, find code to remove. Subtraction is harder than addition and trains the muscle directly.
7. **Study failures.** Postmortems, CVE writeups, "we rewrote X" posts. Bad taste has consequences; seeing them concretely calibrates yours.

### Specifically for AI-native development

The new failure mode is *plausible-looking output you didn't think about hard enough*. So taste here means:

- **Read generated diffs as critically as a stranger's PR**, not as your own work to defend.
- **Throw it away when it feels off.** Regeneration is cheap. Don't sunk-cost your way into keeping a mediocre design.
- **Specify constraints, not code.** Good prompts describe the *shape* of the answer (must be pure, must not allocate, must fit on one screen). The taste is in the constraints you think to impose.
- **Resist volume.** AI makes it easy to produce a lot. Fewer files, fewer abstractions, fewer features — restraint is a stronger signal of taste than ever.

---

## A practical exercise

Pick any post from [Anthropic's engineering blog](https://www.anthropic.com/engineering). Find one design decision. Before reading the justification, try to articulate:

1. What would the *tasteless* version of this decision have looked like?
2. Why would a reasonable person have made the tasteless choice?
3. What does the tasteful version cost, and what does it buy?

The gap between your answer and the post's reasoning — and your ability to feel it *before* reading — is your taste developing.

---

The shortest version of the whole idea: **taste is the willingness to say "this works, and it's still not good enough," and the experience to know what *would* be good enough.**
