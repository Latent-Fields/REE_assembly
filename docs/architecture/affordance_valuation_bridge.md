---
title: "Affordance-and-Valuation Bridge (z_world -> commitment)"
parent: "Core Engines & Forward Models"
grandparent: Architecture
nav_order: 21
status: candidate
status_asof: 2026-09-22
status_claim: ARC-149
---

# The affordance-and-valuation bridge

**Status:** candidate. Registered from
[`docs/thoughts/2026-09-18_affordance_valuation_bridge_sensory_to_commitment.md`](../thoughts/2026-09-18_affordance_valuation_bridge_sensory_to_commitment.md)
on 2026-09-22. **DO NOT build in V3 and DO NOT queue an experiment against these claims
without a `/governance` routing decision** -- see "Version routing is unresolved" below.

## What this page covers

The raw thought names an intermediate object REE has not explicitly committed to: the
representation that sits between the world model and the commitment boundary.

```text
observation
  -> z_world / E1-E2
  -> affordance-and-action geometry      <-- this page
  -> competing approach / avoidance / investigation tendencies
  -> E3 / commitment boundary
  -> motor policy / action
```

Its compact formulation, verbatim from the source:

> The path from sensory input to motor output should be modelled as a changing geometry
> of reachable, affectively and socially consequence-bearing possibilities.

Four claims are registered from it, deliberately separated so that each can fail alone:

| claim | asserts |
|---|---|
| [ARC-149](#arc-149) | the intermediate representation is **necessary** (separability falsifier) |
| [MECH-575](#mech-575) | it has **metric/field structure**, with a deformation signature |
| [MECH-576](#mech-576) | rival tendencies **alternate** before commitment rather than summing |
| [MECH-577](#mech-577) | the sensorimotor path carries **phase-shared + phase-exclusive** dimensions |

## What was NOT registered, and why

Extraction beat invention on four of the thought's threads. They are already owned:

- **Commitment as a jurisdiction change.** MECH-090 (beta gating of E3 -> action
  propagation), MECH-342 (release of an elevated latch mid-commitment) and MECH-138
  (cancel-window flag) already constitute "one path acquires privileged ability to alter
  body and world, while retaining an interrupt route". ARC-145 supplies the jurisdiction
  vocabulary for the inter-engine information case. The thought contributes unifying
  language, not new falsifiable content.
- **The structured proposal object** (trajectory + consequences + confidence + provenance
  + affective exposure + dominance) is the union of MECH-487 (provenance-tagged retention
  of uncommitted candidates), MECH-035 (vector valence, no scalar collapse), MECH-125
  (multi-constraint viability, not scalar reward maximisation), ARC-115 (non-collapsible
  confidence readouts) and MECH-530 (non-oracular output typing).
- **Ethics begins in affect and is cognitively reconstructed later.** ARC-094 (no empathy
  module, no empathy scalar), MECH-405 (fast-empathy stream binding), INV-084 (kindness is
  not constraint compliance) and especially **MECH-569** -- registered 2026-09-18, the same
  day as this thought and from an unrelated route (the `ree-lit-pull-am-b` pull for
  ARC-089/ARC-094) -- already assert that the fast affective route is the developmental
  scaffold the slower mentalizing route differentiates from. This thought rediscovered that
  shape independently and applied it to ethical grounds.
- **"Local success without organismal benefit"** is the thought's own cited parent,
  `2026-09-16_local_mechanism_success_vs_organism_level_intelligence.md`, already registered
  as GOV-JURIS-1 / GOV-ECOL-1 / GOV-HOTHER-1 / GOV-DELETE-1 / Q-108.

## Relation to the 2026-09-03 sensorimotor lens

[`lens_predictive_sensorimotor_transformation.md`](lens_predictive_sensorimotor_transformation.md)
re-describes REE as a recurrent predictive sensorimotor transformation and deliberately
registers **no** claim. This page is the sharper successor of that lens: it accepts the same
re-description and then asks what object must exist in the middle of it, in a form that can
be falsified. The lens is the framing; these four claims are what the framing costs if true.

## Version routing is unresolved

The raw thought says "V3 assays first; richer social consequences are later-tier work".
All four claims are nonetheless registered `implementation_phase: v4` /
`version_relevance: v4_v5` per the ingestion default, because none of them is cleanly and
cheaply testable on substrate that exists in V3 today. **This disagreement is deliberate and
is flagged for a `/governance` routing decision** -- do not resolve it unilaterally in
either direction. The nearest V3-testable sibling is MECH-561 (`implementation_phase: v3`),
which MECH-577 is explicitly distinguished from.

## Claims

### ARC-149

Anchor for the necessity commitment. See `docs/claims/claims.yaml`.

### MECH-575

Anchor for the affordance-field geometry hypothesis. See `docs/claims/claims.yaml`.

### MECH-576

Anchor for the precommitment tendency-alternation hypothesis. See `docs/claims/claims.yaml`.

### MECH-577

Anchor for the phase-conditioned sensorimotor subspace hypothesis. See `docs/claims/claims.yaml`.

## External prompts (biological evidence, not REE evidence)

Both are evidence about the recorded populations and tasks, not evidence that REE requires
the named regions. Per `feedback_lit_exp_decoupled`, neither strengthens any REE claim's
confidence.

- Diomedi et al. (2026), *The posterior parietal cortex supports motor planning and execution
  through a gradient of neural subspaces*, Commun Biol.
  <https://www.nature.com/articles/s42003-026-10878-6> -- partly shared, partly
  phase-exclusive subspaces across planning and execution; overlap varies by area. Prompt
  for MECH-577.
- Starkweather et al. (2026), *Intracranial recordings in humans reveal differential
  contributions of medial and lateral orbitofrontal cortex to approach-avoidance
  decision-making*, Nat Neurosci.
  <https://www.nature.com/articles/s41593-026-02444-4> -- pre-choice medial/lateral OFC
  signals oppositely related to later approach; activity alternated between discrete
  approach-favouring and avoidance-favouring states. Prompt for MECH-576.
