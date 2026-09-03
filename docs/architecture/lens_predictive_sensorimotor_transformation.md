---
title: "REE as Predictive Sensorimotor Transformation (lens)"
parent: "Foundations & Rationale"
grandparent: Architecture
nav_order: 20
---

# REE as Predictive Sensorimotor Transformation (a lens, not a claim)

**Status:** conceptual lens. Registers **no** REE claim and changes no architecture,
status, or confidence value. Source thought (read in full before this page):
[`docs/thoughts/2026-09-03_ree_as_predictive_sensorimotor_transformation.md`](../thoughts/2026-09-03_ree_as_predictive_sensorimotor_transformation.md).

## The reframing

The thought re-describes REE's existing architecture in different coordinates.
Instead of foregrounding modules (world model, planner, selector), it foregrounds
the *transformation of sensed distinctions into action*:

```text
sensed distinction -> predicted consequence distinction -> action distinction
```

Its concise formulation (source, section 17):

> REE can be understood as a recurrent predictive sensorimotor transformation:
> sensed world and organism state are transformed through learned prediction,
> memory and counterfactual action into behaviour. E1, E2, hippocampal,
> frontal-like, control and E3/basal-ganglia-like machinery are specialized
> contributors to this transformation rather than necessarily independent
> cognitive stages.

The thought is explicit that this adds nothing architecturally (source, section
16): "Nothing new has necessarily been added to REE. We may simply have rotated
it until the current failure becomes easier to see." Existing module names
(E1, E2, E3, hippocampal memory) remain the operative vocabulary elsewhere in
this documentation set; this page does not propose replacing them.

## Verbs, not nouns

The one substantive methodological point (source, section 4) is that REE's
functional nouns — memory, goal, planner, selector — describe operations more
faithfully as *verbs*: remembering, conditioning, predicting, chaining,
suppressing, amplifying, comparing, stabilizing, committing. The thought's
caution: "If REE is engineered around the nouns too literally, it risks
imposing artificial interfaces between processes that should remain
dynamically coupled." This is a design caution, not an empirical claim, and is
recorded here for the same reason `docs/architecture/policy_primitive_granularity.md` and `arc_106_biology_grounding_framework.md` carry design
cautions alongside claims: it constrains how future substrate is built without
itself being falsifiable.

## The diagnostic consequence

The thought's practical payoff (source, section 17) is a diagnostic reframing
for exactly the situation V3-EXQ-978 presents — resource direction substantially
decodable from `z_world`, foraging competence unchanged:

> When behaviour fails despite the relevant information being represented,
> trace where the sensory distinction stops producing the appropriate
> difference in predicted consequences and action dynamics before adding
> another representation.

Operationally (source, section 10), this is a **transformation-tracing**
primitive: hold a distinguishing input pair fixed (e.g. resource left vs.
right) and track whether the distinction survives at each successive stage:

```text
D0 = d(S^L, S^R)                          D1 = d(z_world^L, z_world^R)
D2 = d(E1^L, E1^R)                        D3 = d(predicted trajectories^L, ...)
D4 = d(E3^L, E3^R)                        D5 = d(P(A|L), P(A|R))
```

The diagnostic question is not the absolute magnitude of any D_i but *at which
transformation the sign, ordering, or usefulness of the distinction
disappears*.

## Cross-reference: D0–D5 against ARC-130's audit ladder

ARC-130 ([`causal_reach_and_installability.md`](causal_reach_and_installability.md))
already names an 8-stage audit projection for exactly this kind of question —
"the furthest stage demonstrated" rather than a flat implemented/not label —
and `ree-v3/experiments/_lib/capability_contract.py` already instruments five
collapsed interpretation routes over it. The table below maps the thought's
chain onto both, so a 978-successor autopsy can reuse the existing instrument
rather than build a parallel one:

| Thought stage | Distinguishing question | ARC-130 stage(s) | `capability_contract.py` route if the distinction dies *at* this stage |
|---|---|---|---|
| D0 (sensed) | Does the distinction exist in the observation at all? | existence | *(pre-audit; not a `capability_contract` case — a construction check)* |
| D1 (`z_world`) | Is the distinction represented internally? | representation | `capability_precondition_unmet` |
| D2 (E1) | Is the representation endogenously recruited by the predictive machinery, not merely latent? | endogenous recruitment | `mechanism_unreached` |
| D3 (predicted trajectories) | Does the distinction locally operate — produce differentiated candidate consequences? | local operation | `mechanism_unreached` |
| D4 (E3) | Does the distinction have *competitive* (not merely non-zero) influence in trajectory arbitration? | competitive authority | `authority_floor_unmet` |
| D5 (P(action)) | Does the distinction survive to committed action, past any selector/latch boundary? | committed throughput | `authority_floor_unmet` (if D4 passed but D5 does not) / `interpretable` (if D5 passed) |
| *(not reached by D0–D5)* | Does the differential action actually change environmental outcomes? Is it retained across contexts? | ecological consequence; retention/generalisation | *(outside this chain's scope)* |

Two things follow from the mapping rather than being asserted by either
source document. First, the thought's chain is a strict **prefix** of ARC-130's
ladder — D0–D5 stop at committed action and never ask whether the resulting
behavioural difference reaches ecological consequence or survives
retention/generalisation; a 978-successor autopsy that stops at D5 has not
audited those two stages and should say so rather than imply completeness.
Second, `capability_contract.py`'s routes are reported at the level of *whole
declared mechanisms/capabilities* (`requires_mechanisms`, `requires_capabilities`),
while D0–D5 is a per-distinction trace within one already-instantiated
organism; the mapping above says which route a per-distinction failure would
resemble, not that the existing contract mechanism already computes D0–D5
directly. Building that instrumentation (if wanted) is a separate,
unauthorised step — this page does not propose it.

## What this page is not

This page registers no claim, changes no `status`, `confidence`, or
`epistemic_category` field on any existing claim, and takes no position on
V3-EXQ-978 (autopsy pending at
`REE_assembly/evidence/planning/failure_autopsy_V3-EXQ-978_2026-09-03.md`).
Read the source thought in full for context this summary omits, including its
treatment of goals, continuation, and social extension as similarly
transformation-level rather than object-level properties.
