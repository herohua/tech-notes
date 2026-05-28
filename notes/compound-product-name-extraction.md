---
title: "Practical product-name extraction: a compound pipeline that ships"
date: 2025-11-07
tags: [nlp, entity-extraction, fuzzy-matching, llm, taxonomy, branding]
publish: true
---

> *Detecting "Azure AD" in a paragraph is easy. Detecting it without also flagging `Azure.Identity` (a namespace), `azure-ad-cli` (a package), or the literal text `AzureAD` inside a fenced code block — that is the practical problem this note is about.*

## TL;DR

- Finding product names in technical docs looks like a regex job until you try it on real content — then it turns into a short pipeline of cooperating stages.
- A canonical list of products and their aliases is the most valuable asset. Every other stage anchors to it.
- A surprising amount of the work is *not* matching but *un*-matching: skipping code, URLs, and common English words that happen to be product names ("Teams", "Lists", "Forms").
- The LLM runs last, not first. It confirms or extends what cheaper code has already found, and it can't move a match that was already pinned.

## What this note is for

If you've been asked to find every mention of a product in a piece of documentation — to lint it, to rewrite stale names ("Office 365" → "Microsoft 365"), or to produce a citation list — this note describes a working pipeline you can copy and adapt. No prior background in natural language processing (NLP) or named-entity recognition (NER) is assumed; terms are introduced as they come up.

The shape generalizes beyond product names: it works for any task where you need to extract entities from a fixed vocabulary and the output has to be precise enough to drive automated edits.

## Why naive approaches don't survive contact with real content

Start with the obvious idea: take a list of product names, search for each one in the document, mark every hit. This breaks immediately, in four predictable ways.

**Product names look like ordinary nouns.** "Teams" is a Microsoft product. "Teams" is also a normal English word ("the engineering teams shipped on time"). A plain dictionary match against running prose lights up everywhere it shouldn't. The same is true for "Forms", "Lists", "Bookings", "Loop", "Stream", "Office".

**Product names have many aliases.** "Microsoft Entra ID" is also "Entra ID", "Azure AD", "AAD", and "Azure Active Directory" — and a few years ago it was something else entirely. A list with just one of those names misses content that uses the others. A list with all of them creates overlaps you then have to resolve: when the text says "Microsoft Entra ID", do you flag the whole phrase, or also separately flag "Entra ID" inside it?

**Product names appear inside code that you must not touch.** `using Azure.Identity;` contains the word "Azure", but it's a C# import statement — rewriting it would break the sample. The same goes for URLs, package names, and dotted identifiers.

**Product names change over time.** "Office 365" became "Microsoft 365"; "Azure AD" became "Entra ID". Old documentation still uses the old names. Any useful product list has to carry historical aliases so old content can be detected even as new content is rewritten to current terminology.

Each of these problems calls for a different technique. The pipeline below is what you get when you address them one at a time, in an order where each stage can rely on the previous one.

## Building the pipeline, one stage at a time

Before any stage runs, you need the **taxonomy**: a structured list of every product, with every name you know it by — the canonical short name, the long name, the abbreviation, the previous name, any informal synonyms ("use-for" names that aren't preferred but appear in the wild), and a code name if one exists. A spreadsheet or JSON file is fine. A typical taxonomy has a few thousand entries.

Flatten every alias into one big lookup table — every string that, when it appears in text, should map back to a specific product. That table is what every stage below leans on.

### Stage 1: find the easy matches (the "dictionary spotter")

Feed every alias into a fast string-matching engine — anything that takes a vocabulary and tells you where each entry appears in a document. Set it to be case-insensitive and to prefer the longest match when two aliases overlap. (The canonical fast implementation is the [Aho-Corasick algorithm](https://dl.acm.org/doi/10.1145/360825.360855); a simpler modern alternative is [FlashText](https://arxiv.org/abs/1711.00046).)

That last bit matters: if the text says "Microsoft Entra ID", you want one hit for the whole phrase, not separate hits for "Entra" and "Entra ID" and "Microsoft Entra ID" piled on top of each other.

This stage catches anything that appears verbatim. It's your floor: if a product is in your list and shows up in plain text, it gets found here.

### Stage 2: a backup scan for what the spotter missed

Spotter engines tokenize first, and their tokenizers occasionally split or skip names that contain punctuation (`.NET 8`, `C#`) or unusual casing. A plain substring sweep over the text catches what the spotter missed. Merge its results into the main candidate list using the same "longer wins" rule.

(An alternative is to expand the alias list with singular/plural variants — extra detection pass versus expanded inputs. Either way works.)

### Stage 3: throw out matches that are inside code, URLs, or identifiers

This is where most false positives die. Identify regions of the document that aren't prose:

- fenced code blocks (`` ``` ... ``` ``)
- inline code (single backticks)
- URLs inside markdown links
- dotted identifiers like `Azure.Identity` or `Microsoft.Extensions.Logging`

Drop every match whose position falls inside one of those regions. The dotted-identifier rule matters more than it sounds — every code sample is full of namespaces that contain valid product words, and without this guard each sample turns into a sea of false brand mentions.

### Stage 4: try expanding the match boundaries

Sometimes the spotter matches a fragment when the full product name is right there. Suppose "Studio" is in your alias list but "Visual Studio" isn't separately listed. If the spotter catches "Studio" and you stop there, you've underspecified the match.

Try growing each match left and right to swallow adjacent capitalized words, skipping common connectives ("the", "of", "and"). After expanding, re-score against the alias list. If the expanded version scores better, keep it; if not, revert. The pattern is *speculate aggressively, validate cheaply, revert on failure* — at worst it's a no-op.

### Stage 5: deduplicate overlapping matches

Stages 1–4 produce candidates that frequently overlap: "Microsoft Entra ID" and "Entra ID" might both fire on the same span. Apply the same rule one more time: **longer match wins**. By the end, no two surviving matches overlap.

### Stage 6: clean up near-misses with fuzzy matching

So far everything has been exact-or-nothing. Now score each surviving match against the full alias list using a **fuzzy string similarity score** — a number between 0 and 100 measuring how similar two strings are, where 100 is identical. The classic algorithm is **Levenshtein distance** (count of single-character edits to turn one string into the other), expressed as a ratio. A threshold around 80 works well in practice.

This stage does two jobs:

1. **Catches typos and formatting drift.** "AzureAD" (missing space), "Azure A.D." (extra punctuation), "azureAD" (casing) — none match exactly, but all score above 80 against "Azure AD" and link to the right product.
2. **Picks a canonical name.** Each match now points to a specific taxonomy entry, so downstream consumers know the official name when rewriting.

Cache the scores; without caching, this stage dominates pipeline time on long documents.

### Stage 7: drop products whose names are also common English

Some products are unfortunately named after ordinary words: "Lists", "Forms", "Stream". A small curated blocklist drops these. It's manual work to maintain, but empirically nothing else works as reliably.

This trades a little **recall** (how many real mentions you catch) for a lot of **precision** (how few false alarms you raise). You'll miss the rare paragraph that genuinely talks about Microsoft Lists by name; you'll stop flagging the hundreds that mention "lists" in passing.

A reasonable question: why not skip this and let the LLM in stage 8 sort it out? You can — the model handles "teams the noun" vs. "Teams the product" well. But these common-word collisions are *high-volume*: every technical document is full of "teams", "forms", "lists" in their ordinary sense. Dropping them deterministically keeps the LLM pass focused on genuinely ambiguous cases instead of paying for tokens on every benign mention, and the failure mode is easier to debug — a missed entry in a blocklist is a one-line fix; a one-off model misjudgment is a prompt-tuning rabbit hole. Flip the cost trade-off (cheap inference, expensive blocklist maintenance) and stage 7 becomes optional.

### Stage 8: let the LLM confirm or extend the results

Every stage so far has been deterministic — same input, same output, no model in sight. Now hand the document and the surviving matches (plus a relevant subset of the taxonomy) to a language model and ask it to do two things:

1. **Confirm.** For each match, is it really talking about the product in context? "We migrated to Teams" almost certainly means Microsoft Teams; "we split into three teams" almost certainly doesn't. The model is much better at this distinction than any static rule.
2. **Extend.** Are there mentions the deterministic stack missed entirely? Novel phrasings ("the Entra identity service", "your AAD tenant's principals") that don't match any alias literally but a human reader would recognize.

Two rules constrain the model:

- It can **agree** with a position that was already pinned, or it can **propose a new mention** (whose position you then compute by lookup in the text). It cannot **move** a pinned position.
- Its output is constrained to canonical names from the taxonomy — by **constrained decoding** (asking the model to emit JSON matching a schema whose product-name field is an enumeration of valid values). This prevents the model from confidently inventing canonical names that don't exist.

Alternatively: instead of asking the model for spans, have it emit placeholders like `<==={type}{value}===>` inside a rewritten document, then resolve those placeholders deterministically against the taxonomy in post-processing.

### Stage 9: tag and emit

Final assembly tags each match with where it came from: `nlp` (found by the spotter), `nlp+fuzzy` (spotter plus fuzzy normalization), `nlp+fuzzy+ai` (deterministic stack, confirmed by the model), or `ai` (model-only). This **provenance tag** is what makes the pipeline debuggable months later — when a wrong answer shows up, the tag tells you which stage to look at.

Output shape depends on the consumer: a diff stream for an authoring tool, a structured findings list for a linter, inline replacements for a content pipeline.

## The assembled pipeline

```
taxonomy (canonical + aliases)
        │
        ▼
┌────────────────────┐
│ 1. Dictionary      │  Match every flattened alias, longest-first,
│    spotter         │  case-insensitive
└────────────────────┘
        │
        ▼
┌────────────────────┐
│ 2. Substring scan  │  Backup pass for what the spotter tokenizer missed
└────────────────────┘
        │
        ▼
┌────────────────────┐
│ 3. Exclusion masks │  Drop matches inside code, URLs, dotted identifiers
└────────────────────┘
        │
        ▼
┌────────────────────┐
│ 4. Boundary expand │  Grow matches to absorb adjacent capitalized words;
│                    │  revert if the score drops
└────────────────────┘
        │
        ▼
┌────────────────────┐
│ 5. Dedupe / merge  │  Longest match wins on overlap
└────────────────────┘
        │
        ▼
┌────────────────────┐
│ 6. Fuzzy match     │  Levenshtein-style ratio ≥ 80 against every alias
└────────────────────┘
        │
        ▼
┌────────────────────┐
│ 7. Common-word     │  Drop entries whose names are also generic English
│    filter          │
└────────────────────┘
        │
        ▼
┌────────────────────┐
│ 8. LLM pass        │  Confirm/extend; constrained to taxonomy names;
│                    │  cannot move existing positions
└────────────────────┘
        │
        ▼
┌────────────────────┐
│ 9. Merge & tag     │  Provenance tag per match; first-vs-subsequent
│                    │  occurrence resolution
└────────────────────┘
```

## The quiet rules that hold it together

Three rules show up in multiple stages and are easy to overlook:

1. **Longest match wins.** Applied at the spotter, at merge time, and at dedupe time. Same rule, three places.
2. **The deterministic stages own positions.** The LLM can agree with a position or propose a new one (whose offsets you compute by lookup), but it cannot perturb a position that was already pinned. This is what makes the output stable enough to drive find-and-replace edits.
3. **First-vs-subsequent occurrence is stateful.** Branding style guides almost always say "full name on first mention, short name thereafter." Track first-vs-subsequent in a seen-set walked in document order, and emit the right form per occurrence.

These rules are unglamorous but they're what turn a row of independent detectors into a single system that produces the same answer twice on the same input.

## Why the LLM goes last (and the alternatives that don't work as well)

The most common alternative pipeline shapes each have a specific failure mode worth knowing about before you commit.

### "Just ask the LLM"

Hand the model the document and the full taxonomy in one call, get back the mentions. Simple — and modern context windows can fit a few-thousand-entry taxonomy comfortably. The real problems are subtler:

- **Recall is bounded by attention, not by what's in the prompt.** A taxonomy in-context doesn't get enumerated against every paragraph — the model skims, and entries in the middle of a long list get under-attended ("lost in the middle"). A new product on row 4,000 gets noticed less often than one on row 5. The deterministic spotter doesn't skim; it checks every alias against every position. Recall is *guaranteed by construction*, not approximated by attention.
- **Quiet hallucination of canonical names.** Ask for "the official name" and the model will produce something that *sounds* official but isn't actually in the taxonomy. Constrained decoding helps when the model can return a structured list of names. If the output format is a rewritten document with placeholders (e.g. `<====Azure AD====>`), you still need a post-processing step that maps each emitted name to a taxonomy entry and rejects unmatched ones.
- **Document-rewrite outputs amplify drift.** A common workaround for span precision is asking the model to emit the document back with placeholders inserted — boundaries become a parser problem, not a model problem. This *does* solve position accuracy, but introduces its own failure mode: models silently skip paragraphs, paraphrase sentences, or truncate at the end. For find-and-replace on production content this is a hard blocker without a diff verifier ("rewritten text equals original except for inserted placeholders, else reject"), which is real complexity.
- **Cost scales with content, twice over.** The model reads every paragraph (input tokens) and, in the rewrite shape, writes a near-copy back (output tokens — typically 3–5× more expensive). The deterministic pre-filter shrinks the LLM's job to a small candidate list, so you pay output tokens only on the genuinely ambiguous parts.
- **Non-determinism in a deterministic problem.** Two runs over the same input can produce slightly different outputs even at temperature 0, especially with long prompts. The deterministic stack gives you reproducibility for free.

If your documents are short, your taxonomy is small, you have a diff verifier, and cost-per-doc isn't load-bearing, the LLM-only shape can be a perfectly valid pipeline. The cascade earns its place when *any* of those conditions stops holding — especially recall on products the model has never seen.

### "LLM first, taxonomy confirms"

Let the model propose candidates, look each one up in the taxonomy to confirm. Better than no taxonomy at all — but recall is still bounded by what the model proposes, not by what's in your list. Products the model has never seen (new ones, renamed ones, obscure SKUs) simply don't get proposed; the confirmation step can't rescue what was never proposed. Your taxonomy knows them; the model doesn't.

### "Dictionary only, no LLM"

Skip stage 8 entirely. For low-risk use cases this is fine, and it's a defensible baseline. Where the LLM earns its place:

- **Novel phrasings** that don't match any literal alias ("the Entra identity service").
- **Contextual disambiguation** of common-English-also-product names ("Teams" the product vs. "teams" the noun).
- **The long tail** of false positives the curated blocklist hasn't caught yet.

### What the chosen ordering buys you

Three properties fall out of putting the deterministic stages first:

1. **Recall is set by the taxonomy, not the model.** Anything in your alias list will be found, including products the model has never heard of. Taxonomies are cheap to update; retraining is expensive.
2. **Positions are exact by construction.** Spans come from substring matches against the known text. The output is stable enough to drive automated edits.
3. **The LLM's job shrinks to what it's actually good at.** Confirmation, disambiguation, and the long tail — each a yes/no or short-text question over a small candidate set, much cheaper and more reliable than "extract everything from this document."

The deeper principle: **when a problem decomposes into a deterministic part and a judgment part, do the deterministic part deterministically.** Spend the LLM budget on the irreducibly fuzzy stuff and let cheap, reproducible code own everything else. Every wrong answer is then either "the dictionary missed it" or "the model got it wrong," and the provenance tag tells you which.

## Honest limits

The pipeline has real weaknesses worth naming:

- **Levenshtein with a fixed threshold of 80 is a crude similarity metric.** It's length-biased — short brand names get matched too liberally, long ones too conservatively. Industry has largely moved to learned similarity (small models trained to score how alike two strings are). The reason to keep Levenshtein is reproducibility and no training data, but it's a deliberate simplification, not the best available scoring.
- **No per-match confidence score.** Every hit is binary. A combined score (mixing fuzzy ratio, source-tag count, and LLM confirmation strength into a single number) is a cheap upgrade.
- **The common-word blocklist is curated, not learned.** It drifts as the corpus drifts.
- **Longest-match-wins discards legitimately nested entities.** "Azure" inside "Azure DevOps" gets suppressed. For brand detection that's usually correct; for richer entity extraction it would be a loss.
- **No evaluation harness built in.** The provenance tags *enable* per-tier precision/recall measurement, but the loop only closes if you maintain a gold set.

## When to use this shape (and when not to)

**Reach for it when:**

- The vocabulary is closed and finite — hundreds to low thousands of items — and updates faster than you can retrain a model.
- Output drives automated edits, so getting exact positions right matters more than chasing the last few percentage points of accuracy.
- Debuggability matters; every wrong answer needs to be traceable to a specific stage.
- Recall on items the model has never seen must not silently degrade.

**Reach for something else when:**

- The fuzzy-match stage becomes the bottleneck — at tens of thousands of aliases its *candidates × aliases* scoring cost gets painful. Cheap fixes (blocking by first letter or shared token, or skipping fuzzy entirely and accepting that "AzureAD" without a space gets missed) buy headroom; past that, you'll want search-engine-style retrieval to narrow candidates before scoring, in the shape of systems like [BLINK](https://arxiv.org/abs/1911.03814).
- The task is open-domain extraction with no fixed vocabulary — use a model designed for that.
- Catching novel phrasings matters more than exact positions — an LLM-first pipeline with constrained decoding wins on the long tail, at the cost of position stability.

### Deliberate simplifications versus the state of the art

Even within the "use this shape" case, several stages are deliberately simpler than current research-grade entity linking. Naming the gaps honestly:

| This pipeline | Current state of the art | Why we diverge |
|---|---|---|
| **Levenshtein ratio ≥ 80** for matching the *surface form* — the exact spelling as it appears in text | **Learned similarity** — small neural models trained to score string-pair similarity ([sentence-transformers](https://www.sbert.net/), *cross-encoder rerankers* — a model that takes a candidate match and the surrounding text together and scores how well they fit) | No training data, no GPU at inference (see *Honest limits* for the cost). |
| **Curated common-word blocklist** | **Learned context classifier** that decides per-mention whether the surrounding text is product-shaped | The blocklist's failure mode is visible; a learned classifier's is not. |
| **Generative LLM as the reranker** | **Purpose-built cross-encoder rerankers** ([BLINK](https://arxiv.org/abs/1911.03814)-style) trained on linked entity pairs | The LLM is already in the stack; adding a second specialized model is more infrastructure for marginal gain. |
| **Closed-world taxonomy, gazetteer-first** | **Zero-shot / open-vocabulary extraction** ([GLiNER](https://arxiv.org/abs/2311.08526), generative linkers like [GENRE](https://arxiv.org/abs/2010.00904)) | We *want* the closed world — recall must be bounded by the taxonomy, not by what the model happens to know. |
| **Binary hits** with provenance tags | **Calibrated confidence scores** per mention | A combined score is a known cheap upgrade we haven't taken yet. |

The pattern: each divergence trades a couple of accuracy points for reproducibility, debuggability, or the ability to update behavior by editing a list instead of retraining a model. If those properties are not load-bearing for you, the SOTA alternatives are better choices.

## Where this sits in the wider literature

This shape isn't novel — it's a recognized architecture with standard names for each stage, and it's the same shape several well-known systems converged on:

| Stage | Standard name (and what it means) |
|---|---|
| Dictionary spotter (longest-first) | **Gazetteer matching** — "gazetteer" is the term of art for a fixed vocabulary list scanned against text ([Aho-Corasick](https://dl.acm.org/doi/10.1145/360825.360855), [FlashText](https://arxiv.org/abs/1711.00046)) |
| Exclusion masks | **Span masking** / **negative gazetteer** — regions or strings to ignore |
| Boundary expansion | **Span repair** — fixing the start/end of a match after the fact |
| Fuzzy match | **Surface-form normalization** — mapping a real-world spelling ("AzureAD") to its canonical entry ("Azure AD") |
| Common-word filter | **Negative dictionary** — a list of strings to actively reject |
| LLM pass | **LLM-as-verifier** / **LLM reranking** — using the model to judge, not to discover |
| Provenance tags | **Source-attributed ensembling** — recording which detector produced each result |

The overall shape is what the academic literature calls a **hybrid NER + entity linking cascade** — a pipeline that first finds candidate mentions (NER, named-entity recognition) and then links each to a canonical record (entity linking) — restricted to a closed-world taxonomy. It mirrors [spaCy's `EntityRuler → ner → EntityLinker` ordering](https://spacy.io/usage/rule-based-matching#entityruler), [Microsoft Presidio's recognizer cascade](https://microsoft.github.io/presidio/analyzer/), and the *propose-then-rerank* shape of neural entity linkers — with the twist that the reranker here is a generative LLM rather than a separately trained scoring model.

The closest production analogues are terminology management in computer-assisted translation tools (such as [Trados](https://www.trados.com/), backed by [TBX termbases](https://www.tbxinfo.net/) with fuzzy thresholds), and biomedical pipelines like [SciSpaCy](https://allenai.github.io/scispacy/) and [MetaMap](https://lhncbc.nlm.nih.gov/ii/tools/MetaMap.html) (medical dictionary plus disambiguator). Knowing you're in good company — rather than inventing — is itself useful.

## What I'd carry forward

- **Start with the taxonomy, not the model.** A high-quality alias list with previous-term and "use-for" fields does more for detection quality than any prompt tweak. The taxonomy is the artifact that pays back across every stage.
- **Spend the exclusion budget early.** Half the work is teaching the pipeline what *not* to detect — that's where most false positives die, and it's cheap to do up front.
- **Treat first-vs-subsequent as a real concern.** Bake the long-form/short-form rule into the pipeline rather than asking authors to fix it by hand.

The shape generalizes: any time you're extracting entities from a closed vocabulary and need stable, reproducible spans, this stack — dictionary, exclusion, fuzzy, LLM-confirm — is a practical default to start from.
