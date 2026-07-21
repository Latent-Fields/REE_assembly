# Thought Intake — Rule apprehension as an organisational principle of cognition

**Date of thought:** 2026-07-14
**Intake written:** 2026-07-21
**Raw thought file:** `docs/thoughts/2026-07-14_rule_apprehension_as_an_organisational_principle_of_cognition.md`
**Session:** `sad-newton-00451d` (thought-intake ingestion, 2026-07-21)
**Prompting literature:** MIT Brain and Cognitive Sciences, *Separating Logic and Language* — evidence that formal logical reasoning and language are at least partially dissociable. Treated as **convergent evidence**, not the origin of the architectural proposal.
**Status:** structured intake written; candidate claims NOT yet registered (concurrent session held the `claims.yaml` claim).
**Promotes/demotes:** nothing.

## Why this needed an intake rather than a marker

Initial triage suspected this thought was already discharged into the ARC-062 / ARC-063 rule-apprehension line. It is not. **No file in `REE_assembly` cites it**, and the logic/language dissociation appears nowhere in `claims.yaml`. ARC-062/063 predate it (they were registered and already deep in GAP-B falsifier work by mid-June); this thought arrives *after* that machinery and generalises it in two directions the registry does not cover.

## The claim (verbatim)

> The primary organisational function of reasoning is not language manipulation nor formal logical deduction. It is the continual apprehension, evaluation, refinement, application and integration of regularities that improve prediction, behaviour and long-term viability. Language functions as a powerful interface to these processes rather than their fundamental substrate.

## Already owned — cross-reference, do NOT re-assert

| Element in the thought | Existing claim(s) |
|---|---|
| Rule apprehension as an architectural slot (weak reading: gated policy, two heads + context discriminator) | **ARC-062** |
| Strong reading: distributed CandidateRule field with tolerance | **ARC-063** (V4-deferred) |
| Cue-driven context-bound rule retrieval (the "select" face) | **MECH-338** |
| Rule-selective persistence through distractors, training-emergent | **MECH-262**, **SD-033a** |
| Rule-state write gating by mode | **MECH-261** |
| Cross-episode regularity extraction (successor-representation / CLS analog) | **MECH-316**, **ARC-064** |
| Schema abstraction / consolidation as search grammar | **MECH-211**, **MECH-166**, **MECH-429**, **INV-039** |
| Simulation-mode rule-write gating (categorical replay tag) | **MECH-319** |
| Counterfactual simulation as a distinct operation | **SD-003**, **ARC-092** (licit forms of update from imagined experience) |
| Prediction-error-driven refinement | the E1/E2 predictive machinery generally; **MECH-069** (error types incommensurable) |
| Policy composition / decomposition / re-granularisation | **ARC-069**, **ARC-070**, **ARC-071** |
| Language as separate from core cognition | the language thought cluster (`2026-02-09_language.md`, `2026-06-23_language_as_cooperation_interface.md`) — **note: those are themselves still unprocessed**, so this is a thought-level not a claim-level cross-reference |

So the *stages* of the pipeline are largely instantiated. Do not re-register them.

## Genuinely new — three things

### N1. The pipeline is registered as pieces, never as an ordered organisational cycle

```
Experience -> pattern sensitivity -> candidate regularity apprehension -> representation
  -> prediction -> counterfactual simulation -> behavioural interaction -> outcome comparison
  -> regularity refinement -> generalisation -> long-term integration
```

Each stage has claims. **The cycle does not**, and the thought's implication is specifically that the stages must not collapse into a single "reasoning module." That non-collapse requirement is the same shape as ARC-025 (engine irreducibility) and MECH-069 (error incommensurability) but has never been asserted for the rule pipeline.

The practically useful part is the thought's own open question: *which REE mechanisms currently support rule persistence, refinement and generalisation, and which remain only planned?* That is an answerable audit, and the answer is the gap map.

### N2. "Rule apprehension" is deliberately broader than induction, and domain-agnostic

> "Induction" already implies a formal reasoning framework. Rule apprehension is intentionally broader: recognition that the world appears to contain a reusable regularity.

Spanning physical dynamics, spatial relations, motor control, social interaction, emotional behaviour, ethics, language and mathematics — with the architecture **agnostic regarding domain**. ARC-062/063 are scoped to policy-layer behavioural regimes; the domain-agnosticism claim is wider and is not registered. Its sharp form is the thought's open question: *are there separate systems for causal / social / ethical / motor / spatial / abstract-relational regularities, or one domain-general apprehender?* That is a genuine architectural fork, currently unasked.

### N3. Language as interface, not substrate — with the LLM counterexample handled

> Highly trained language systems such as LLMs demonstrate that considerable reasoning-like behaviour can emerge from language alone. However this does not imply that language constitutes the native substrate of reasoning.

This is the thought's most defensible novel position, and it is the one the MIT source directly supports. It is also a **positioning claim REE needs and lacks**: the programme's entire bet is a non-linguistic substrate, and the obvious external objection ("LLMs reason, so language suffices") currently has no registered answer. The reply — language is a powerful *approximation and coordination interface*, and may *compensate* for weaknesses in other reasoning systems — is a claim with an empirical shape, not just a stance.

Also note the thought's own guard, which matters given the neighbouring 2026-07-19 Assembly thought: **REE and REE Assembly have strong parallels, and any analogy between them must be labelled an analogy, never used as evidence that REE operates the same way.** That is a good standing rule and should survive into whatever is registered.

## Candidate claims (for registration at digestion)

1. **The rule pipeline is an ordered cycle of non-collapsible stages.** *Candidate, architectural.* Apprehension, representation, application, behavioural testing, refinement and generalisation are distinct organisational stages that must not be collapsed into one reasoning mechanism. *Falsifier shape:* stage-ablation — removing or short-circuiting one stage should produce a *characteristic* failure signature distinct from the others (e.g. apprehension-without-testing yields elegant-but-unvalidated regularities; testing-without-refinement yields repeated identical failures). PASS requires the failure signatures to be dissociable, not merely "performance drops." *Non-degeneracy guard:* the intact baseline must show live variance on the discriminating metric for each stage — a pipeline where no stage measurably contributes has nothing to dissociate. *Type:* architectural commitment. *Cross-ref:* ARC-062, ARC-063, MECH-338, MECH-316, ARC-069/070/071, ARC-025 and MECH-069 (the same non-collapse argument at other levels).

2. **Rule apprehension is domain-general, or it is not — an architectural fork.** *Candidate, open question.* Does REE need separate regularity-apprehension systems per domain (causal / social / ethical / motor / spatial / relational), or one domain-general apprehender that inherits domain structure from its inputs? *Falsifier:* cross-domain transfer — a rule apprehended in one domain should (domain-general) or should not (domain-specific) accelerate apprehension in another under matched structure. *Non-degeneracy guard:* single-domain apprehension must first be demonstrated above floor in both domains separately. *Type:* open question, likely `substrate_conditional` — V3 has only one real domain. *Cross-ref:* ARC-062/063, MECH-316, MECH-211.

3. **Language is an interface to reasoning, not its substrate (REE positioning claim).** *Candidate.* Reasoning-like behaviour emerging from language alone (LLMs) does not establish language as the native substrate; language functions as compression, communication, coordination, long-horizon scaffolding, working-memory support, explanation — and may **compensate** for weaknesses in other reasoning systems. *Falsifier shape:* the compensation leg is the testable one — if language is a compensator, a system with a weakened non-linguistic reasoning stage should show *greater* reliance on linguistic scaffolding, not merely worse performance. Substrate-blocked in V3 (no language stream). *Type:* architectural positioning / `substrate_conditional`. *Cross-ref:* the language thought cluster; the MIT logic/language dissociation as the external anchor; register the source as a `research_anchor`/`EXT-*` if it is to be citable.

4. **(Standing discipline, not a claim) REE:Assembly analogies must be labelled as analogies.** Fold into the intake/digestion discipline notes rather than the registry — unless the 2026-07-19 Assembly governance-rule cluster gives it a natural home, in which case register it there.

## Routing

- **Cheapest first move is the audit, not an experiment.** Answer the thought's own closing question — *which rule-pipeline stages are implemented, which are planned, which are absent* — as a table against ARC-062/063/MECH-338/MECH-316/ARC-069-071. That is `complicated (buildable)` and it is the precondition for candidate 1's ablation design.
- **Candidate 1 is the registrable core.** Note its dependency on the live ARC-062 GAP-B blocker: rule-*selective* behaviour is untestable until a rule-creator emits differentiated (non-monomodal) rule state, and the monostrategy-collapse ceiling is the standing obstacle. **Do not queue candidate 1's ablation while GAP-B is unresolved** — it would inherit the same degeneracy.
- **Candidates 2 and 3 are substrate-blocked** (one domain; no language stream). Register scoped to V4/V5; do not design.
- **`/lit-pull`:** the six search families are well formed. The load-bearing one for candidate 3 is *language and reasoning / language as cognitive scaffold / private speech / language compensation* — and note there is an existing unprocessed thought on private speech and externalised DMN that should be pulled in the same pass rather than separately.

## Next steps

1. Register candidate 1 as testable-but-gated; 2 and 3 as `substrate_conditional`. **Deferred from this session.**
2. Mark the raw thought `Status: processed` once (1) lands.
3. Rule-pipeline implementation audit (see Routing).
