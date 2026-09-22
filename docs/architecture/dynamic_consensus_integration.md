---
title: "Dynamic Consensus as Post-Translation Integration (MECH-578, MECH-579)"
parent: "Core Engines & Forward Models"
grandparent: Architecture
nav_order: 22
status: candidate
status_asof: 2026-09-22
status_claim: MECH-578
---

# Dynamic consensus as post-translation integration

**Status:** candidate. Registered from
[`docs/thoughts/2026-09-19_dynamic_consensus_post_translation_integration.md`](../thoughts/2026-09-19_dynamic_consensus_post_translation_integration.md)
on 2026-09-22. **DO NOT build in V3 and DO NOT queue an experiment** against these claims
without a `/governance` routing decision.

This page is the fourth in the mutual-legibility programme, after
[mutual legibility and communication subspaces](mutual_legibility_communication_subspaces.md)
(ARC-139, INV-105), [receiver-conditioned translation](receiver_conditioned_translation.md)
(MECH-547, MECH-548) and [dynamic information governance](dynamic_information_governance.md)
(ARC-145, MECH-560, MECH-561).

## The question it asks

The programme so far has asked how two systems with different internal representations can
exchange usable information. The source thought asks what happens *after* translation
succeeds, and proposes:

```text
cross-system integration = mutual legibility + selective reciprocal coupling + agreement-dependent dynamics
```

with the terminal state of a coupled pair being not identical but **mutually supportable**:

```text
A(t) <-> B(t) -> A(t+1),B(t+1) -> ... -> A*,B*
```

> The goal is therefore not representational equality. It is dynamical compatibility.

## The two claims

| claim | asserts |
|---|---|
| [MECH-578](#mech-578) | reciprocally coupled REE subsystems show **agreement-dependent timescale separation** (`tau_agree > tau_disagree`), which collapses under coupling ablation or correspondence scramble |
| [MECH-579](#mech-579) | that separation is **developmentally acquired** -- pruning carves a consensus topology, not merely a translation dictionary |

## What was NOT registered, and why

This thought is an unusually strong extraction case: most of its architecture is already in
the registry, and saying so precisely is the substance of the pass.

- **"No privileged global representation" / integration without representational sameness** is
  **ARC-139** in full, including its non-redundant prediction that rising local competence with
  flat-or-falling global similarity is the expected maturation signature.
- **"An interface can be legible yet dynamically pathological"** is **MECH-548**, which already
  states that a bridge with one-step utility > 0 can fail repeated closed-loop application, and
  already supplies the cumulative-vs-clean-base diagnostic. MECH-578 is distinguished from it by
  *directionality*: MECH-548 is one bridge applied repeatedly; MECH-578 is two systems coupled
  reciprocally, where the predicted signature is a timescale *separation between agreeing and
  disagreeing joint states* rather than drift or gain escalation.
- **"A system must know when NOT to settle" / false consensus / agreement among clones is
  cheap** is **INV-108** in five explicit parts, including the protected path to attention for
  a competent dissenting route and the warning that optimising an agreement objective destroys
  the independence that gave agreement its evidential value. The source thought's self-vs-other
  section and its false-consensus and dominance failure modes are all downstream of INV-108 and
  **MECH-558** (vote count is not evidence count).
- **Transition-geometry compatibility** -- that a mapping can succeed pointwise while destroying
  transition geometry -- is **MECH-539**.
- **"What may couple now"** is **ARC-145**'s jurisdiction property, with **MECH-561** supplying a
  phase-indexed addressing mechanism.
- **Organism-level validation of a pretty internal metric** is GOV-JURIS-1 / GOV-ECOL-1 and
  `feedback_local_mechanism_success_vs_organism_level_intelligence`'s registered family.

## A numbering collision this page deliberately does not join

INV-105's ladder has **seven** rungs. Four separate claims (MECH-548, MECH-555, GOV-CONTRACT-3,
INV-110) each describe themselves as adding "an eighth" rung, and MECH-556 describes a "ninth".
The ordinals are therefore already inconsistent in the registry.

MECH-578 proposes a further rung -- **RECIPROCALLY RECONCILED** -- but deliberately asserts **no
ordinal**, and the collision is flagged for `/governance` rather than compounded here.

## External evidence, and its limits

Javadzadeh M, Schimel M, Hofer SB, Ahmadian Y, Hennequin G. *Reciprocal connections dynamically
build consensus between neocortical areas.* Nature Neuroscience 2026. DOI:
10.1038/s41593-026-02437-3. Simultaneous V1/LM recording in mice during visual discrimination,
with focal optogenetic perturbation and biologically constrained latent circuit models;
reciprocal excitatory connections generated an approximate line attractor in the joint system,
congruent patterns occupied slower modes and incongruent ones decayed faster, the slow dynamics
depended on long-range inter-area connections specifically, and fine-grained consensus required
selective like-to-like connectivity.

The source thought is explicit, and this page preserves the caution verbatim:

> The evidence is currently specific to V1-LM interactions in a relatively simple visual task.
> The claim that dynamic consensus is a general cortical principle remains a generalisation
> rather than an established universal mechanism.

Per `feedback_lit_exp_decoupled`, this paper is an external prompt. It is **not** evidence for
any REE claim and does not move any confidence value.

## Claims

### MECH-578

Anchor for agreement-dependent timescale separation. See `docs/claims/claims.yaml`.

### MECH-579

Anchor for the developmental consensus-topology hypothesis. See `docs/claims/claims.yaml`.
