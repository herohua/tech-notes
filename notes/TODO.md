# Notes backlog

Candidate essays mined from past work. Dates indicate when the original discussion happened. Not front-matter'd yet — promote to a real note when drafted.

## Drafting order (top picks)

1. **Quota-as-a-resource: reliable allocation for rate-limited APIs** *(2026-05-15)*
   When the limited resource is API posting quota across N app identities, neither a distributed lock nor a naive queue is enough. What you want is a token-bucket pool with reservation semantics, fair across consumers, with backpressure rather than failure.

2. **The case for code-mode MCP** *(2026-04-21)*
   When the workflow is fixed, having the LLM emit a script that calls MCP tools — rather than chatting through a dozen tool calls — collapses latency and cost. Compares CLI vs MCP-tool-loop vs code-mode and when each wins.

3. **Skills with style** *(2026-04-22)*
   Companion to *Taste in software*, applied to prompt/skill design. The recurring shape across good skills: short framing, hard-coded *don'ts*, a runnable checklist, one strong verb per step.

## Also worth writing

4. **Two archetypes that survive the AI shift: creative builders and deep system experts** *(2026-05-18)*
   Notes for individual engineers on where to invest. Distillation of a talk + personal synthesis.

5. **Static fields lie in distributed systems** *(2026-05-07)*
   A clock helper used a process-local `static` monotonic counter to guarantee unique IDs. It looks like a global invariant at the call site and is useless across a fleet. Sub-lesson: uniqueness at one layer (100 ns ticks) is silently destroyed by formatting at the next (100 μs string) — any "unique because precise" guarantee must be traced end-to-end to where the value is actually compared.

6. **The three logging blind spots that recur in every service** *(2026-05-08)*
    A reusable checklist for any observability pass: (1) no log at the pass/fail *decision point* of a gate; (2) telemetry/side-effect exceptions silently swallowed instead of logged as warnings; (3) parser/extractor failures that return defaults without recording why. These three cover most "we had no idea why prod did that" incidents. Pairs with: ship a focused important-only PR first, not one mega-PR.

7. **Stop calling all three things "agent": model-call, tool-orchestrator, goal-seeking loop** *(2026-05-14)*
    Useful framing for any AI write-up. Concrete diagnostic questions: is there a real loop per API call? Does anything check whether the user's purpose was met before returning? Most "agents" are model-calls in a coat; collapsing the three hides the interesting design differences.
