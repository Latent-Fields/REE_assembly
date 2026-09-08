---
title: "The Cognitive Contract (ARC-142, GOV-CONTRACT-1, MECH-545, MECH-546, Q-104)"
parent: "Core Engines & Forward Models"
grandparent: Architecture
nav_order: 17
status: candidate
status_asof: 2026-09-08
status_claim: ARC-142
---

# The Cognitive Contract

**Status:** candidate architecture, registered 2026-09-08 from
`docs/thoughts/2026-09-08_deriving_the_cognitive_contract.md`
(intake: `evidence/planning/thought_intake_2026-09-08_deriving_the_cognitive_contract.md`).
Companion to [Mutual Legibility and Communication Subspaces](mutual_legibility_communication_subspaces.md)
(ARC-139, MECH-537..540, INV-105) and to INV-104 in
[Regulation-First Representation](regulation_first_representation.md).

**Primary question:** what information must survive translation between specialised cognitive
systems for them to constitute one unified mind?

Nothing on this page is a build instruction. Every claim below is `candidate`,
`substrate_conditional` (the governance rule excepted), and carries a "do not build in V3" caveat.

---

## The layering

```text
Cognitive contract                 <- what must remain recoverable across ANY translation
        |
Representation / translation machinery   <- learned bridges, communication subspaces, C/T/D pathways
        |
Schemas                            <- contingent body / environment / history knowledge; rewritten by sleep
        |
Particular concepts, memories and environmental models
```

Schema change alters what the organism knows. Contract failure alters whether its subsystems
can still understand one another. The contract is therefore not the schema, and it is also not
REE_assembly's claims / evidence / provenance invariant machinery
([Invariant Types](invariant_types.md)) -- deriving one from the other is circular
(GOV-CONTRACT-1, GOV-ANALOGY-1).

### A sharper reading of the cognifold

The cognifold is not a single latent space. It is the mutually interpretable representational
structure of one unified cognitive system, whose unity arises from overlapping transformations
among many latent spaces rather than from one universal representation. It may contain local
manifolds, specialised latent spaces, shared subspaces, learned translators, compression /
decompression pathways, recurrent loops, and the invariant relations spanning them. This is a
reading of ARC-089's "single cognifold", not an amendment to it.

---

## ARC-142 -- the cognitive contract {#arc-142}

Unified cognition across heterogeneous engines requires an invariant-preserving contract, not a
common latent space: a small set of relations `I` such that for any lossy translation
`x_A -> C_A(x_A) -> T_AB -> D_B -> x'_B`, `I(x_A) ~ I(x'_B)`, even though `x'_B = x_A` is
meaningless across different spaces. The contract is relational, not representational: engines
may encode an invariant differently as long as the relation is recoverable at the boundary. Two
failure poles: **representation collapse** (one canonical latent forced on every engine) and
**cognitive fragmentation** (engines keep exchanging tensors while losing shared meaning).

Relationship to existing claims, stated so a later session neither duplicates nor merges:

| Existing | Relation to ARC-142 |
|---|---|
| INV-104 | The first instantiated contract: one path (observation -> z_world -> E1/E2), five classes, sender-side. ARC-142 generalises it to every inter-engine boundary and adds the layering. |
| ARC-139 | Says integration needs legibility, not sameness. Says nothing about WHAT must be legible. ARC-142 is that content-side half. |
| MECH-538 | Measures the minimum bridge complexity. ARC-142 says what any bridge must carry. |
| MECH-539 | One candidate invariant (transition geometry survives the map), not the contract. |
| ARC-121 | Rival collapse-pole reading of the same convergence evidence. Deliberately untouched. |
| MECH-423 | Super-additivity over shared *features*. Must not be read as requiring shared *geometry*. |

**Candidate invariant inventory (research inventory, NOT a specification):** identity, persistence,
reference, agency, causality, temporal relation, process state / aspect, spatial relation,
quantity, actuality / reality status, observation vs memory vs imagination, counterfactual status,
uncertainty, confidence / precision, negation, value, harm / benefit significance, goal relevance,
commitment, controllability, salience, social attribution. Some are not fundamental, several may
reduce to one, some are consequences of human embodiment, some are linguistic conveniences, and
important ones may be missing. The goal is the smallest defensible set: derive and prune.

**Developmental clause.** The contract differentiates rather than arriving mature: coarse
primitives (`self-caused / not`, `here / not-here`, `now / not-now`) precede derived structure
(agency, intention, control, responsibility, social attribution), which precedes learned schemas.
A distinction required before substantial learning is a stronger architectural candidate than one
appearing only after extensive experience.

---

## GOV-CONTRACT-1 -- admissibility rule for contract invariants {#gov-contract-1}

A candidate invariant acquires architectural standing only by consilience across at least two of
six independent evidence domains:

1. cross-linguistic typology;
2. pre-linguistic developmental cognition;
3. neuroscience (subsystem-independent representation, or a known retaining translation);
4. comparative cognition;
5. independently trained artificial agents;
6. REE-internal necessity at an engine boundary.

Every candidate is classified **architectural / embodied-ecological / human-linguistic-convention /
uncertain**, with the alternative explanation recorded. Cross-linguistic universality alone is
inadmissible. Developmental precedence is the strongest single-domain signal. Negative findings are
preserved as first-class results. The contract is derived independently of the claims-registry
invariant machinery; convergence between the two is logged as a clue under GOV-ANALOGY-1.

**Ledger record shape (one per candidate; ledger not yet built -- proposed home
`evidence/planning/cognitive_contract_invariant_ledger.v1.json`):**

| Field | Question |
|---|---|
| candidate | What relation is proposed? |
| definition | What precisely must be preserved? |
| linguistic | Does it recur cross-linguistically? Obligatorily encoded? |
| developmental | Does it appear before language or explicit teaching? |
| neural | Modality- or subsystem-independent representation? |
| comparative | Does it appear outside humans, in different ecologies? |
| artificial_agent | Does it emerge independently in learned systems? |
| ree | Is it already required, or spontaneously represented, at a boundary? |
| lesion_prediction | What should fail if it is removed (MECH-545)? |
| alternative_explanation | Could embodiment, culture or task structure explain it? |
| classification | architectural / embodied / cultural / uncertain |
| confidence | How strong is the present case? |

Language is admitted as an **inverse probe** -- recurrently grammaticalised distinctions are
evidence about what human cognition repeatedly needs to preserve and transmit -- never as a
definition of the contract. This composes with ARC-100 (grammar mined, never imported): a mined
cut that also survives GOV-CONTRACT-1 is a contract candidate.

---

## MECH-545 -- contract-lesion assays {#mech-545}

The decisive test of a candidate invariant is a **boundary lesion**: a translation that preserves
content but deletes one relation, producing a predicted, invariant-specific fragmentation
signature. Five pre-registered signatures:

| Lesion | Predicted failures | Content-level owner (already registered) |
|---|---|---|
| identity | broken persistence, duplicated selves/objects, incoherent credit assignment, unstable memory integration | ARC-080 |
| temporal | cause/effect inversion, present vs anticipated confusion, memory/prediction contamination | INV-035, INV-104 class 3, MECH-539 |
| reality status | confabulation-like commitment to imagined states, impaired counterfactual learning | MECH-094, MECH-365, MECH-271, ARC-092, MECH-430 |
| agency | poor action learning, attribution errors, failed intentional planning | MECH-256 and the reafference lineage |
| confidence | overcommitment, under-reaction to reliable predictions, failed precision-sensitive integration | precision / MECH-123 lineage |

What is new is the assay pattern (lesion the translation, not the content) and the five-way
dissociation. A boundary lesion is scored against a dimensionality-matched random-projection floor
(INV-105) and must rule out MECH-537's encoded-but-not-exposed confound. An invariant whose lesion
produces no reproducible deficit is struck from the contract and the negative result kept.
ARC-086's latent vulnerability axes are the index these lesions would populate; the overlap
(provenance, agency, precision) is a convergence clue, not evidence.

---

## MECH-546 -- grammar inherits the cognitive contract {#mech-546}

Some grammar-like relational structure emerges in a communication channel because external
transmission between minds inherits the relations internal translation between engines must
already preserve:

```text
Cognitive invariants
  -> internal representational contracts
  -> repeated compression / translation pressure
  -> proto-grammatical relational structure
  -> external language
```

Two-directional test: invariants derived from cognition should be over-represented among
recurrently grammaticalised distinctions, and grammaticalised distinctions lacking developmental,
comparative or computational support should classify as embodied or cultural. Agreement across
both directions is the evidence. Not a theory of grammar; not a claim that human grammar is a
universal grammar of cognition. Extends `docs/thoughts/2026-02-09_language.md` (ARC-009,
MECH-010) and sits beside ARC-101 (the ecology that produces language) and ARC-100 (grammar is
mined, never imported).

---

## Q-104 -- cognifold versus braidling {#q-104}

At what point does invariant-preserving translation between cognitive systems constitute internal
cognition rather than communication between agents? Proposed conceptual discriminator: two
systems are a **braidling** if each remains independently coherent when communication is
severed; they are parts of **one cognifold** if their normal cognition depends on
invariant-preserving transformations across the boundary and they jointly maintain one persistent
self / world structure, so that severance degrades coherence on both sides. Whether the contract
operationalises this (contract-dimension dependency, MECH-538 bridge complexity, a severance
assay) is open. The term "braidling" is first introduced to the registry here.

---

## What is deliberately NOT registered

- **The Cognitive Contract Specification** (section 20 of the thought: declared encodings,
  translator training, tolerated reconstruction error, drift monitoring, low-confidence behaviour,
  add/retire rules). An engineering output of the programme, conditional on the ledger having
  entries. Registering it now would convert a discovery programme into standing architecture.
- **The candidate inventory as individual claims.** Each becomes claim-shaped only when it has a
  ledger record and at least one lesion prediction.
- **Thoughts 2-4 of the programme** (candidate invariants synthesis; compression / decompression
  and the cognifold; mathematics of invariant-preserving translation). These are the user's
  authoring programme, tracked in the intake's next steps.

## Pollution risks (carried verbatim from the thought as standing cautions)

Do not implement the candidate list directly. Do not infer universality from human language. Do
not retrofit the evidence to REE's existing architecture. Do not assume one universal latent
representation. Do not confuse repeated usefulness with fundamentality. Preserve negative
findings.
