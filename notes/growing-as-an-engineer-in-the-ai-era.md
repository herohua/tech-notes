---
title: "Growing as an engineer in the AI era: five themes from Fiona Fung's talk"
date: 2026-06-01
tags: [career, ai, engineering-management, claude-code]
publish: true
---

## TL;DR

Notes inspired by [Fiona Fung](https://claude.com/code-with-claude/session/sf-running-an-ai-native-engineering-org)'s *Running an AI-native engineering org* talk at Code with Claude 2026. Five themes for where to invest your growth as the model gets stronger:

1. **Two archetypes worth becoming** — creative builders with product sense, or deep systems experts. Raw coding throughput is no longer the differentiator.
2. **Product sense and taste are premium.** When the model can generate three implementations in minutes, picking the right one is the skill that scales.
3. **Embrace role blurring.** PMs are coding; engineers are writing copy and doing design. Build a T-shape — pick one adjacent discipline and grow real fluency in it.
4. **Managers must stay hands-on.** Fiona requires managers to start as ICs and dogfood the product. Street cred is earned, not titled.
5. **Growth mindset is the meta-skill.** What made you senior last year may not next year. Refactor your own habits like you refactor code.

---

## Why I'm writing this down

Fiona's framing of the talk is that the tool isn't the hard part — *your processes are*. The talk itself is about org-level adaptation at Anthropic, but most of the punch for me lands one level down: what does this mean for the individual engineer trying to stay relevant? These are my notes on that.

The unifying thread across all five themes: **as generation gets cheap, the scarce skills are judgment, taste, and the willingness to refactor yourself.** Everything below is a different facet of that.

---

## Theme 1 — Two archetypes worth becoming

The model gives everyone baseline coding throughput. So what's left to differentiate on?

Two archetypes hold up:

**Creative builders with product sense.** Curious dreamers who turn problems into delightful products. They iterate quickly, obsess over UX, critique AI output with taste (not just acceptance), and are comfortable shipping prototypes, gathering signal, and pivoting. Their edge is *what to build and why*.

**Deep systems experts** — the hard parts AI still struggles with. Distributed systems, infra, performance, correctness. They reason about failure modes the model can't see, design for scale and reliability, and make the hard architectural calls under uncertainty. Their edge is *where the model's confidence outruns its competence*.

The honest question to ask yourself: **which archetype am I leaning into deliberately?** Drifting in the middle — neither a strong product instinct nor deep systems chops — is the spot the model is closing in on fastest.

---

## Theme 2 — Product sense and taste are premium

When generation is cheap, judgment becomes the scarce resource. Three plausible implementations in minutes; picking the right one is the actual skill.

What to grow:

- **Design thinking and user empathy.** Read the user behind the feature request, not just the words.
- **Taste to critique AI output.** Fiona told a story of asking Claude to render an ASCII snowman; her design partner took one look and said *"you turned Claude into the Mr. Peanut character."* Catching that — knowing the output is *technically what was asked for* but *clearly wrong* — is the skill.
- **Quality judgment over volume.** Engineers who can't evaluate output get out-shipped by those who can. Volume without judgment is just faster wrongness.

This connects directly to the [taste essay](taste-in-software.md): when AI makes producing plausible code nearly free, the scarce skill is rejecting the nine outputs that aren't right.

---

## Theme 3 — Embrace role blurring; build a T-shape

PMs are coding. Engineers are writing content and doing design. The strict lanes of the pre-AI org are dissolving because the tooling cost of crossing them has collapsed.

The healthy response is a deliberate T-shape: keep depth in your engineering core, then pick **one** adjacent discipline and build real fluency in it with AI augmentation. The adjacent discipline matters less than picking one and getting genuinely competent:

- **Design** — wireframe, critique UI, talk shape with designers.
- **Content** — write crisp copy, error messages, docs that ship without a rewrite.
- **Data** — query, analyze, and dashboard your own features instead of filing tickets.
- **Product** — frame problems, write specs, talk to users directly.

The trap is being shallow in five things instead of fluent in one. AI lets you fake breadth; it doesn't grant you taste in the adjacent domain. That still comes from doing the work.

---

## Theme 4 — Managers must stay hands-on

Fiona's policy: managers on her team start as ICs and dogfood the product. She mentioned her recruiters pushed back hard — *no manager would want to be hired into a role that started as an IC* — but she held the line. That's the new bar for credibility in an AI-native org.

Three reasons this matters even if you're not a manager today:

- **Sharp judgment comes from shipping.** You can't lead what you don't use. Decisions about architecture, hiring, and process degrade fast when the leader hasn't touched the system in a year.
- **AI removes the old excuse.** The context-switching cost that used to justify "I don't have time to code anymore" is dramatically lower with Claude. The math has changed; the rationalization hasn't caught up.
- **Street cred is earned, not titled.** Teams trust leaders who can debug alongside them. In an AI-native org, the manager who can't critique a generated diff is invisible during the moments that matter most.

For ICs: this raises the bar on what you should expect from your manager, and signals what the path up looks like. The companion to this discipline is taking a team process you actually own and [agentizing every step of the iteration loop](evaluating-a-self-healing-content-agent.md#3-agentize-every-step-of-the-iteration-loop) — there's no faster way to recover the judgment that pure management drift erodes.

---

## Theme 5 — Growth mindset is the meta-skill

What made you senior last year may not next year. Git commands shift. IDEs shift. Workflows shift. The half-life of any specific tool is shrinking.

Three habits that compound:

- **Re-learn willingly.** Be at peace with the fact that the specific *how* of your craft will keep changing. Attachment to the current toolchain ages badly.
- **Refactor yourself.** Treat your own working habits as code worth improving every quarter. What you optimized for a year ago may be the bottleneck now.
- **Question the norm.** Ask of every process: *is this still serving us?* Be the one who removes things, not just the one who adds. Most AI-era process pain comes from running pre-AI workflows on top of post-AI capabilities. The strongest version of this is [agentizing every step of the loop](evaluating-a-self-healing-content-agent.md#3-agentize-every-step-of-the-iteration-loop) — once you've tried to encode a workflow as an agent, you find out fast which steps were load-bearing and which were ceremony.

Continuous re-learning beats depth in any single tool. The meta-skill underneath all four prior themes is the willingness to do this work on yourself.

---

## What I'm taking away

- Pick an archetype. For me: deep systems expert, with deliberate investment in product sense as the T-shape's adjacent leg.
- Treat taste as a trainable skill — read more code I respect, critique more AI output instead of accepting it, cultivate a delete reflex on generated diffs.
- Audit one team process per quarter against "is this still serving us in an AI-native workflow, or is it pre-AI muscle memory?"

The talk's org-level message — *the tool isn't the hard part, your processes are* — has an individual mirror: **the model isn't the hard part, your habits are.**
