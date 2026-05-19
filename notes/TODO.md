# Notes backlog

Candidate essays mined from past work. Dates indicate when the original discussion happened. Not front-matter'd yet — promote to a real note when drafted.

## Drafting order (top picks)

1. **Prompt caching is a system design problem, not a config flag** *(2026-05-15)*
   Stable prefix order, alphabetizing optional sets, putting timestamps last, why timestamp-ordered memories sabotage cache hits. Cache-hit-rate as a first-class metric.

2. **Quota-as-a-resource: reliable allocation for rate-limited APIs** *(2026-05-15)*
   When the limited resource is API posting quota across N app identities, neither a distributed lock nor a naive queue is enough. What you want is a token-bucket pool with reservation semantics, fair across consumers, with backpressure rather than failure.

3. **The case for code-mode MCP** *(2026-04-21)*
   When the workflow is fixed, having the LLM emit a script that calls MCP tools — rather than chatting through a dozen tool calls — collapses latency and cost. Compares CLI vs MCP-tool-loop vs code-mode and when each wins.

4. **Skills with style** *(2026-04-22)*
   Companion to *Taste in software*, applied to prompt/skill design. The recurring shape across good skills: short framing, hard-coded *don'ts*, a runnable checklist, one strong verb per step.

## Also worth writing

5. **Why your "AI fix" looked good in eval but bad in review** *(2026-04-17)*
   Separate *structure correctness* (covered by build) from *meaning correctness* (needs human judgement). Never make a model choose between two valid renderings of the same intent. Pre-filter cases that exceed your tool's structural limits before scoring, or you'll chase phantom regressions.

6. **Using a coding-agent SDK as a faster eval harness** *(2026-04-17)*
   Don't always run end-to-end through CI; drive the SDK directly with the same model spec and capture trajectories. Mark ungradeable cases passed rather than skipped. Keep downstream artifact shapes stable so diffing across runs stays meaningful.

7. **Workload identity, demystified for the impatient** *(2026-04-21)*
   "You know how this works, here are the gotchas": federated-credential per region, Kubernetes service-account → managed-identity mapping, how to verify on-cluster, why infra-as-code beats portal clicks as the source of truth.

8. **Two archetypes that survive the AI shift: creative builders and deep system experts** *(2026-05-18)*
   Notes for individual engineers on where to invest. Distillation of a talk + personal synthesis.

9. **When an LLM call is "slow," suspect task-model fit before infra** *(2026-04-21)*
   A 25-minute call wasn't capacity or auth — a reasoning model was burning tens of thousands of hidden chain-of-thought tokens on a binary classification. Also: default 5-minute network timeouts on a 25-minute response silently triggered 2–3 retries per success, tripling cost and latency. Big-prompt-one-call vs. many-small-prompts is a real design axis, and reasoning models punish you for collapsing it.

10. **Static fields lie in distributed systems** *(2026-05-07)*
    A clock helper used a process-local `static` monotonic counter to guarantee unique IDs. It looks like a global invariant at the call site and is useless across a fleet. Sub-lesson: uniqueness at one layer (100 ns ticks) is silently destroyed by formatting at the next (100 µs string) — any "unique because precise" guarantee must be traced end-to-end to where the value is actually compared.

11. **The three logging blind spots that recur in every service** *(2026-05-08)*
    A reusable checklist for any observability pass: (1) no log at the pass/fail *decision point* of a gate; (2) telemetry/side-effect exceptions silently swallowed instead of logged as warnings; (3) parser/extractor failures that return defaults without recording why. These three cover most "we had no idea why prod did that" incidents. Pairs with: ship a focused important-only PR first, not one mega-PR.

12. **Stop calling all three things "agent": model-call, tool-orchestrator, goal-seeking loop** *(2026-05-14)*
    Useful framing for any AI write-up. Concrete diagnostic questions: is there a real loop per API call? Does anything check whether the user's purpose was met before returning? Most "agents" are model-calls in a coat; collapsing the three hides the interesting design differences.
