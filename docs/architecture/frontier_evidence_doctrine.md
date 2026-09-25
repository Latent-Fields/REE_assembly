---
title: "Frontier Evidence Doctrine (GOV-FRONTIER-1, GOV-INSERT-1)"
parent: "Foundations & Rationale"
grandparent: Architecture
nav_order: 23
status: candidate
status_asof: 2026-09-25
status_claim: GOV-FRONTIER-1
---

# Frontier Evidence Doctrine

**Status:** candidate governance rules, registered 2026-09-25 (user-confirmed registration) from
`docs/thoughts/2026-09-24_experimental_learning_beyond_literature.md`
(intake: `evidence/planning/thought_intake_2026-09-24_experimental_learning_beyond_literature.md`).
Registration changes no gate, threshold, schema or indexer behaviour. Adopting the `literature_status`
field is follow-on tooling that needs a separate decision.

## Context: what REE already has

Promotion already reads experimental confidence only (the 2026-05-01 lit/exp decoupling), and the
indexer already labels strong-experiment / weak-literature claims `novel_discovery`. So "experimental
evidence may carry a claim alone" is not new. What is missing is a record of HOW direct the literature is:
today an adjacent analogue and a direct mechanistic precedent raise literature confidence identically (for
example INV-082's literature confidence rose from 0.0 to 0.824 on attachment and shame/guilt analogues, none
of which supplies the learning rule). The one remaining hard literature floor is
`provisional_to_stable.min_literature_entries: 2`; whether frontier claims are exempt is undecided.

<a id="gov-frontier-1"></a>
## GOV-FRONTIER-1 -- literature status: direct / adjacent / frontier

After a documented, scoped search, a mechanism claim may be labelled DIRECT, ADJACENT or FRONTIER. "No
direct precedent found" is a sanctioned terminal outcome of a literature pull, not a veto. Adjacent
literature constrains the design and must not be read as direct support. A frontier mechanism may be built
default-OFF and promoted on REE experimental evidence alone, but absence of literature RAISES the
experimental burden (pre-registered competing candidates, production-path causal reach, negative controls,
ablation, world-family replication, a non-compensable adjudication battery). Frontier status is never
itself evidence.

<a id="gov-insert-1"></a>
## GOV-INSERT-1 -- insertion-dependence counts against the derivation

If an axiom-derived mechanism only produces its predicted causal pattern when the desired ethical outcome
is inserted (reward term, hard-coded rule, privileged label, hard constraint, or deleting the unethical
affordance), that is admissible negative evidence against the derivation. An insertion arm is an oracle:
it may set a ceiling but never counts FOR the derivation. Binds v4 (needs axiom-derived ethical mechanisms
with a live insertion alternative); gives `axiom_chain_adversarial_audit.md` an experimental route.

## Open items (for /governance)

- Frontier exemption from `min_literature_entries: 2`, or keep the floor (caps frontier claims at
  provisional).
- The GOV-INTRO-1 reading for introspectively-sourced mechanisms (proposed: met only through a labelled
  ADJACENT mapping).
- Tooling to adopt `literature_status` (claims schema, validator, `build_claims_json.py`, the indexer's
  planning reasons, a non-scoring null-result record, and the lit-pull skill -- GOV-HELDOUT-1 check owed).
