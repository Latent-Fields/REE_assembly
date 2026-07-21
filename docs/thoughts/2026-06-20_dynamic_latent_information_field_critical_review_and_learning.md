# Dynamic Latent Information Field: Critical Review and Learning

Status: processed
Processed in:
- `docs/claims/claims.yaml` (Q-079 `structured_uncertainty_field_distinctness` -- the DLIF / structured-uncertainty field question; verdict ANSWERED-NEGATIVE: DLIF is NOT a distinct mathematical object, it decomposes into factor-graph unification + Bayesian-nonparametric structure learning + active inference + ARC-013 residue. This file is cited in that claim's `sources`.)


**Date:** 2026-06-20  
**Status:** critical_review / learning_capture  
**Scope:** Dynamic Latent Information Field (DLIF), field-first structured uncertainty, REE agent design, claims-index governance  
**Source:** critical review after minimal formal specification  
**Primary benchmark note:** preserve the REE-v3 strict green-board target of **Sunday 19 July 2026**. This review should constrain and clarify the research line, not add v3 implementation scope.

---

## Purpose

This document reviews the Dynamic Latent Information Field idea critically and captures the learning produced by that review.

The goal is to make the idea more testable, less poetic, and less likely to become an unfalsifiable theory-of-everything.

---

## Headline review

The field-first correction is promising, but the current DLIF framing is still too broad.

The idea risks becoming an all-purpose container for:

- Bayesian updating;
- Markov coherence;
- active inference;
- information geometry;
- neural fields;
- residue;
- claims governance;
- ethical commitment;
- granularity control.

That breadth is useful for discovery but dangerous for formalisation.

The next step is therefore not to make DLIF larger. The next step is to make it smaller, sharper, and testable.

---

## Critical learning 1: DLIF has ancestors and must not overclaim novelty

The idea overlaps with several existing field-first traditions more than initially acknowledged.

Important ancestors / neighbours:

- **Lewin-style psychological field theory:** action space, valence, force, and dynamic perceived situation.
- **Dynamic Field Theory:** cognitive and embodied behaviour modelled through activation fields, peaks, competition, and stabilisation.
- **Neural field theory:** population-level continuous models of neural activity with non-linear dynamics and state transitions.
- **Decision field theory:** decision-making as evolving preference fields rather than static utility comparison.
- **Energy / attractor models:** stable interpretations or actions as basins in an energy landscape.
- **Active inference:** action and perception coupled through model updating and expected information / value structure.

This does not invalidate DLIF. It means the novelty claim must be narrowed.

DLIF should not claim:

```text
Cognition is field-like.
```

That is not new.

The narrower candidate claim is:

```text
A useful REE-facing field formalism must combine field-native pre-node structure, graph projection, latent-node discovery, scale control, residue/non-erasure, and claims-governance outputs.
```

---

## Critical learning 2: Separate substrate, algorithm, and projection

The earlier DLIF notes mixed several layers.

These must be separated:

```text
Substrate: what is represented natively?
Algorithm: how does it update?
Projection: what inspectable artefact is extracted?
Use: what task does the projection serve?
```

A cleaner separation:

```text
Field substrate:
  distributed values over latent cells / regions

Update algorithm:
  observation, propagation, precision adjustment, scale shift, residue preservation

Projection layer:
  graph, claim, trajectory, residue report, hidden assumption list

Governance / action layer:
  promote claim, split claim, defer claim, choose action, recommend experiment
```

Without this separation, DLIF becomes conceptually attractive but computationally unclear.

---

## Critical learning 3: The minimum version should be discrete, not continuous

Although the word "field" suggests continuous mathematics, the first implementation should not require differential geometry or continuous neural-field equations.

Use a discrete approximation first.

Minimal object:

```text
latent cell = candidate region of latent possibility
field = typed values over latent cells
projection = extraction of stable / tense / salient structures
```

A cell should probably contain only a few measurable values:

```text
belief
uncertainty / entropy
salience / precision
coherence cost
action affordance
residue
scale
```

This gives a testable object without pretending to solve the full mathematics.

---

## Critical learning 4: Residue must be operationalised or it becomes magic

Residue is the most REE-native part of DLIF, but also the highest-risk concept.

If residue is simply "important unresolved moral information," it may become unfalsifiable.

Minimum operational definition:

```text
Residue is a persistent field component that remains after action commitment when morally relevant conflict or harm remains unresolved, and that measurably affects later action selection, repair-seeking, or consolidation.
```

Necessary ablations:

```text
DLIF with residue
DLIF without residue
DLIF with salience-only persistence
DLIF with uncertainty-only persistence
```

Residue is useful only if it changes behaviour in a way not explained by salience or uncertainty alone.

Possible metrics:

```text
residue retention under successful action
repair-action probability
non-erasure after reward
specificity of residue to unresolved harm / conflict
false residue rate
```

---

## Critical learning 5: Granularity zoom must be made mechanical

"Zooming in and out" is a strong intuition, but it must become an operator.

Possible operationalisation:

```text
coarsen(): merge cells / claims / causes into a higher-scale structure
refine(): split a vague structure into lower-scale candidates
shift_scale(): change which scale controls projection or action
```

Scale should not be mystical. It should be defined by partitions or layers:

```text
local cue
trajectory
subgoal
goal
ethical constraint
research programme
```

For the claims index:

```text
fragment -> claim -> mechanism -> architecture principle -> roadmap implication
```

Scale-control metrics:

```text
scale-switch accuracy
harmful over-coarsening rate
unnecessary refinement rate
latency to useful abstraction
```

---

## Critical learning 6: Projection loss is central

If graphs are projections from fields, then projections lose information.

This is not a weakness; it is a testable property.

DLIF should track:

```text
projection_fidelity
projection_loss
projection_purpose
```

A projected graph is useful only relative to a purpose:

```text
explanation
claim governance
action commitment
experiment design
debugging
communication
```

A graph that is useful for explanation may be poor for action. A graph useful for experiment design may omit affective or residue structure.

Therefore:

```text
No projection is neutral.
Every projection has a purpose and a loss profile.
```

---

## Critical learning 7: The first useful pilot should probably be claims-index, not agent-world

The hidden-cause gridworld is conceptually clean, but the claims-index simulator may be more useful sooner.

Reasons:

- REE_assembly already contains claims, thought intakes, evidence, conflicts, roadmap stage, and dispatch structure.
- Claims-index DLIF can be tested without building a new agent substrate.
- It can produce immediate useful outputs: hidden assumptions, conflict/residue reports, scale recommendations, and next-experiment suggestions.
- It avoids derailing REE-v3 agent work before strict green-board.

First pilot candidate:

```text
Claims-Index DLIF Simulator
```

Input:

```text
thought intakes
claims
evidence entries
experiment results
known conflicts
roadmap tags
implementation dependencies
```

Output:

```text
projected claim graph
inferred hidden assumptions
scale recommendation
residue / conflict report
next experiment recommendation
```

This would make DLIF useful even if it never becomes the native REE agent substrate.

---

## Critical learning 8: Add explicit kill criteria

A testable theory needs conditions under which it loses.

DLIF should be demoted or narrowed if:

```text
1. It performs no better than a fixed claims graph on hidden-assumption detection.
2. Its residue variable predicts nothing beyond salience or uncertainty.
3. Its scale-shift operator adds complexity without improving recommendations.
4. Its projections are not more useful than ordinary graph summaries.
5. It cannot produce repeatable metrics in toy settings.
6. It repeatedly becomes a vocabulary expansion rather than a computational constraint.
```

This protects the project from attractive but unproductive abstraction.

---

## Revised minimal uniqueness claim

The refined uniqueness claim should be:

```text
DLIF is not novel because it is field-like. Field-like cognition has many precedents.

DLIF is potentially useful if it provides a minimal computable bridge between field-native uncertainty, graph/claim projection, latent structure discovery, granularity control, and residue-preserving governance.
```

This is much more defensible.

---

## Revised minimal formal object

```text
DLIF_min = (Z, B, U, S, C, A, R, L, P)
```

Where:

```text
Z = latent cells / regions
B = belief over cells
U = uncertainty / entropy over cells
S = salience / precision over cells
C = coherence cost / constraint tension
A = affordance / action potential
R = residue / unresolved moral or governance deformation
L = scale / abstraction layer
P = projection operators
```

Required operators:

```text
observe()
update_field()
coarsen()
refine()
infer_latent_structure()
project_claim_graph()
project_residue_report()
recommend_next_experiment()
consolidate()
```

This is smaller and more implementable than the previous full tuple.

---

## Recommended next action

Do not immediately build a new agent environment.

Build a tiny claims-index pilot first:

```text
Input: 10-30 thought intakes / claims
Field values: belief, uncertainty, salience, coherence cost, residue, scale
Projection: claim graph + hidden assumption list + conflict/residue report
Baseline: ordinary tag/edge claims graph
Evaluation: does DLIF produce better next-experiment or claim-splitting recommendations?
```

This would be useful to REE_assembly and safer than expanding REE-v3 scope.

---

## REE-v3 scope warning

Before **Sunday 19 July 2026**, DLIF should not become a REE-v3 implementation requirement.

Permitted before strict green-board:

```text
use language from DLIF to clarify claims
use residue-as-field-deformation as conceptual support
use claims-index DLIF only if lightweight
use DLIF to prevent premature graph-freezing
```

Not permitted before strict green-board:

```text
major agent refactor
new core mathematical dependency
large claims-index rewrite
standalone repo buildout unless it is a thin preservation stub
```

---

## Learning summary

The review strengthens DLIF by narrowing it.

The next version should be:

```text
less universal
more measurable
closer to claims-index utility
clearer about existing ancestors
stricter about residue
explicit about projection loss
safe from v3 scope creep
```

The key lesson:

```text
DLIF is useful only if it turns field-first intuition into better projections, better hidden-assumption detection, better conflict preservation, better scale decisions, or better next-experiment recommendations.
```

---

## Open questions after review

1. Should the first pilot operate over `docs/thoughts/` and `docs/claims/claims.yaml`?
2. What is the smallest possible field-value schema for claims-index DLIF?
3. How should residue be separated from salience and uncertainty?
4. What counts as a good hidden-assumption inference?
5. Can projection loss be measured in a human-reviewed workflow?
6. Should this critical review become the basis of a future `docs/research/dlif/` folder?
