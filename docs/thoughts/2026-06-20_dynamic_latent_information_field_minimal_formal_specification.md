# Dynamic Latent Information Field: Minimal Formal Specification and Test Programme

Status: processed
Processed in:
- `docs/claims/claims.yaml` (Q-079 `structured_uncertainty_field_distinctness` -- the DLIF / structured-uncertainty field question; verdict ANSWERED-NEGATIVE: DLIF is NOT a distinct mathematical object, it decomposes into factor-graph unification + Bayesian-nonparametric structure learning + active inference + ARC-013 residue. This file is cited in that claim's `sources`.)


**Date:** 2026-06-20  
**Status:** thought_intake / minimal_formal_specification / test_programme_seed  
**Scope:** possible mathematical object underlying field-first structured uncertainty; relevant to Reflective–Ethical Engine (REE) agent design and claims-index governance  
**Source:** discussion after latent information fields / graphs-as-projections capture  
**Primary benchmark note:** preserve the REE-v3 strict green-board target of **Sunday 19 July 2026**. This is a research and test-programme seed, not a v3 implementation dependency.

---

## Purpose

This document converts the latent-information-field intuition into a minimal testable object with field components, projection operators, toy environments, and falsifiable success criteria.

The goal is to move the idea from metaphor toward a usable formal research programme.

---

## Core claim

A **Dynamic Latent Information Field** is a multi-scale latent information space in which uncertainty, salience, coherence tension, affordance, abstraction level, and residue are represented as field properties.

Graphs, claims, causes, trajectories, and actions are projections extracted from the field when the system needs inspection, testing, communication, or commitment.

Compact version:

```text
DLIF = uncertainty field + scale field + action field + residue field + projection operators
```

---

## Relationship to existing formalisms

The proposed object is not invented from nothing. It draws partial structure from existing traditions:

- **Factor graphs:** useful for unifying directed and undirected graphical-model reasoning, but usually graph-structure-first.
- **Information geometry:** useful for treating probability / uncertainty spaces geometrically.
- **Active inference:** useful for action-coupled perception, planning, and learning.
- **Information bottleneck:** useful for relevance-preserving compression and granularity control.
- **Hypergraphs / simplicial complexes:** useful for higher-order relationships beyond pairwise edges.
- **Sheaf theory:** useful for local consistency versus global consistency failure.
- **Energy / attractor models:** useful for basins, gradients, convergence, and commit-readiness.

The candidate object may be useful because it combines these capacities while adding REE-native residue / non-erasure.

---

## Formal skeleton

Let the system at time `t` be:

```text
DLIF_t = (M_t, q_t, E_t, Π_t, C_t, A_t, R_t, S_t, P_t)
```

Where:

```text
M_t = latent manifold / latent space
q_t = belief density over latent states
E_t = energy or coherence-cost landscape
Π_t = precision / salience / gain field
C_t = constraint field
A_t = affordance / action field
R_t = residue field
S_t = scale / granularity structure
P_t = projection operators
```

The critical design move is that nodes are not primitive.

Nodes are extracted.

---

## Projected objects

```text
node := stable local structure extracted from DLIF_t
edge := projected relation between extracted structures
claim := inspectable proposition projected from field tension
action := commit structure selected from affordance/coherence landscape
residue := persistent deformation in R_t after unresolved morally relevant structure
```

Therefore:

```text
graph_t = P_graph(DLIF_t)
claim_index_t = P_claims(DLIF_t)
trajectory_set_t = P_actions(DLIF_t)
residue_report_t = P_residue(DLIF_t)
```

The projected graph is useful but not native.

---

## Minimum operators

A minimal Dynamic Latent Information Field needs operators:

```text
observe(o_t)
update_belief(q_t, o_t)
update_precision(Π_t)
propagate_coherence(C_t)
infer_latent_structure()
coarsen(S_t)
refine(S_t)
project_graph(P_graph)
project_claims(P_claims)
select_action(A_t)
commit(action)
preserve_residue(R_t)
consolidate_offline()
```

The testable object is:

```text
field + projection + transformation + action + consolidation
```

---

## First toy environment

### Hidden-cause gridworld

The agent receives ambiguous cues:

```text
smell gradient
sound cue
blocked path
other-agent distress signal
harm-risk marker
goal marker
```

There are hidden causes:

```text
food source
danger source
trapped other
blocked route
false alarm
```

The agent must infer latent structure, choose scale, and act.

A graph-only model is given a fixed set of nodes and edges.

The field-first model starts with distributed uncertainty and extracts temporary nodes only when needed:

```text
field tension -> latent cause candidate
latent cause candidate -> projected node
projected node -> action hypothesis
action outcome -> field update
unresolved harm -> residue deformation
```

---

## Discriminating tests

### Test 1: Latent-node discovery

Give the system ambiguous observations best explained by an unobserved hidden cause.

Expected Dynamic Latent Information Field advantage:

```text
It should infer a provisional latent cause before a labelled node exists.
```

Failure mode:

```text
It can only reason over pre-specified variables.
```

Metrics:

```text
latent-cause recovery accuracy
time-to-latent-hypothesis
false latent-node rate
```

---

### Test 2: Granularity zoom

Give the system tasks where the correct action depends on scale.

Example:

```text
local cue says: move toward reward
higher-scale cue says: moving now blocks rescue later
ethical-scale cue says: rescue matters more than local reward
```

Expected advantage:

```text
The system should shift from local affordance to higher-scale action framing when the field tension demands it.
```

Metrics:

```text
scale-switch accuracy
unnecessary refinement rate
harmful over-coarsening rate
```

---

### Test 3: Local consistency versus global inconsistency

Create three local interpretations that each make sense, but cannot all be true together.

Expected advantage:

```text
The system should preserve unresolved global inconsistency rather than prematurely forcing one coherent story.
```

Metrics:

```text
detected inconsistency count
premature-collapse rate
conflict-preservation score
```

---

### Test 4: Residue preservation

Give the system a case where it takes the best available action but leaves unresolved harm.

Expected advantage:

```text
The unresolved moral structure should persist as field deformation and influence later consolidation or repair-seeking.
```

Failure mode:

```text
Once reward/action success occurs, the system erases the unresolved harm.
```

Metrics:

```text
residue retention
repair-action probability
non-erasure under success
```

This is likely where REE diverges most sharply from ordinary active inference or reinforcement learning.

---

### Test 5: Projection usefulness

Compare field-native processing with graph projection.

Expected result:

```text
The field should support ambiguous pre-graph processing, while the projected graph should improve inspection, explanation, testing, and governance.
```

Metrics:

```text
performance before projection
interpretability after projection
projection fidelity
projection loss
```

---

## What would make the object useful

The object is useful if it can answer questions like:

```text
What hidden structure is the system implying?
What scale should control action?
What conflict is being prematurely collapsed?
What residue is being erased?
What graph should be projected for inspection?
Which claim should be promoted, deferred, split, or merged?
```

For REE, this gives three possible uses:

```text
1. Agent cognition:
   perception, action, residue, consolidation

2. Claims index:
   thought intake, claim tension, evidence, projection, governance

3. Research tool:
   mapping existing formalisms and testing what remains missing
```

---

## First implementable version

The first useful implementation does not need real differential geometry.

Start with a small discrete approximation:

```text
latent cells = possible hidden states
field values = uncertainty, salience, coherence cost, affordance, residue
scale layers = local / trajectory / goal / ethical
projection = extract top-k stable structures as graph nodes
```

Minimal data sketch:

```python
class LatentCell:
    belief: float
    salience: float
    coherence_cost: float
    affordance: dict[str, float]
    residue: float
    scale: str
```

Minimal field:

```python
class LatentInformationField:
    cells: list[LatentCell]
    constraints: list[Constraint]
    projections: list[Projection]
```

Minimal loop:

```text
observe
update field
infer latent cells
shift scale if needed
project graph
select action
apply outcome
preserve residue
offline consolidate
```

---

## Comparison baselines

Compare the Dynamic Latent Information Field against:

```text
fixed Bayesian network
fixed Markov random field
factor graph
flat scalar confidence model
ordinary claims graph
ordinary reward-shaped agent
```

---

## Expected useful outputs

A useful early implementation should produce:

```text
projected claim graph
inferred hidden assumptions
scale recommendation
residue / conflict report
next-experiment recommendation
```

If it can do those, it is useful even before becoming a full cognitive architecture.

---

## Difference from neighbouring formalisms

| Formalism | It gives | It lacks for DLIF |
|---|---|---|
| Factor graph | unified directed/undirected message passing | field-native pre-node structure |
| Information geometry | geometry of probability distributions | action, residue, projection |
| Active inference | perception-action coupling | moral residue, claims governance |
| Information bottleneck | relevance-preserving compression | non-erasure, conflict preservation |
| Hypergraph / simplicial complex | higher-order relations | field dynamics before relations are named |
| Sheaf theory | local/global consistency | action and residue dynamics |
| Energy / attractor model | basins, gradients, convergence | projection and ethical non-erasure |

---

## Concrete research programme

### Phase 1 — Definition

Write a short specification containing:

```text
state variables
field components
operators
projection types
minimal toy examples
test metrics
```

### Phase 2 — Toy implementation

Build either:

```text
hidden-cause gridworld
```

or:

```text
claims-index simulator
```

The claims-index simulator may be easier and immediately useful:

```text
thoughts enter as diffuse field tension
claims are projected
conflicts deform the field
experiments reduce uncertainty
unresolved conflicts persist as residue
```

### Phase 3 — Baseline comparison

Compare against fixed graph and scalar-confidence baselines.

### Phase 4 — Useful output

Produce outputs usable by REE_assembly:

```text
claim graph
hidden assumption list
scale recommendation
residue/conflict report
next experiment recommendation
```

---

## Immediate REE-v3 relevance

This should not become a REE-v3 blocker before the strict green-board benchmark of **Sunday 19 July 2026**.

It can still help indirectly by giving language for:

```text
why residue must persist
why scalar reward is insufficient
why claims need multi-axis status
why experiments should reduce field tension
why graph outputs are useful but not native
```

---

## Provisional formal claim

```text
A Dynamic Latent Information Field is useful when an agent must reason under uncertainty before the relevant variables, relations, and abstraction level are known. Its native representation is field-like: distributed uncertainty, salience, coherence tension, affordance, and residue. Graphs are projected when the system needs explanation, testing, communication, governance, or commitment.
```

---

## Abstracted-language sketch

```text
DLIF := (M, q, E, Π, C, A, R, S, P)

NATIVE(DLIF) = FIELD
GRAPH = PROJECT(DLIF, purpose)

TEST(DLIF):
LATENT_DISCOVERY ∧ SCALE_SHIFT ∧ LOCAL_GLOBAL_CONFLICT ∧ RESIDUE_PERSISTENCE ∧ ACTION_UPDATE

USEFUL_IF:
PROJECTS(hidden_assumptions, claim_graph, residue_report, next_experiment)
```

---

## Open questions

1. Should the first toy be the hidden-cause gridworld or the claims-index simulator?
2. Can residue be operationalised as a field deformation with measurable persistence?
3. What is the simplest projection operator from field to graph?
4. Can scale-shift be implemented without a large architecture?
5. Which baseline is the fairest first comparison?
6. Does this belong in REE_assembly permanently, or should it become a standalone `latent-information-fields` or `structured-uncertainty-fields` repository?
