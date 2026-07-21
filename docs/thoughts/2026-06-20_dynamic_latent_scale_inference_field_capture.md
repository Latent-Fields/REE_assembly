# Dynamic Latent-Scale Inference Field — Capture Before Literature Drill

Status: processed
Processed in:
- `docs/claims/claims.yaml` (Q-079 `structured_uncertainty_field_distinctness` -- the DLIF / structured-uncertainty field question; verdict ANSWERED-NEGATIVE: DLIF is NOT a distinct mathematical object, it decomposes into factor-graph unification + Bayesian-nonparametric structure learning + active inference + ARC-013 residue. This file is cited in that claim's `sources`.)


**Date:** 2026-06-20  
**Status:** thought_intake / research_seed  
**Scope:** possible mathematical object underlying brain-like structured uncertainty; relevant to REE agent design and claims-index governance  
**Source:** follow-up discussion after Bayesian networks / Markov networks thought intake  
**Primary benchmark note:** preserve the REE-v3 strict green-board target of **Sunday 19 July 2026**. This is a research seed and should not become a v3 implementation dependency.

---

## Core intuition

The candidate object is not just a Bayesian network plus a Markov network.

It may need to support:

```text
directed evidence update
+
cyclic coherence constraint
+
latent-node discovery
+
granularity zoom
+
action-coupled temporal update
```

The emerging idea is that biological cognition may use a dynamic structured uncertainty representation that can infer hidden causes, move between scales, preserve unresolved constraints, and couple belief to action.

---

## Provisional object name

Working names:

- structured uncertainty field;
- dynamic latent-scale inference field;
- dynamic coherence-inference graph;
- hybrid inference field;
- embodied factor-constraint field;
- cognifold inference graph.

Current most descriptive phrase:

```text
Dynamic Latent-Scale Inference Field
```

Current most repo-friendly phrase:

```text
Structured Uncertainty Field
```

Do not lock terminology yet.

---

## Candidate definition

A **Structured Uncertainty Field** is a dynamic, multi-scale, typed factor–constraint system that supports directed evidence update, cyclic coherence constraint, latent-node discovery, granularity transformation, action-coupled inference, precision modulation, and offline consolidation.

Shorter REE-facing definition:

```text
REE should not merely represent uncertain variables.
It should represent uncertain structure: which nodes exist, which scale matters, which constraints bind, which latent causes explain the field, and which unresolved residues must persist across action.
```

---

## Capacities currently identified

### 1. Directed evidence update

The object must update beliefs when evidence arrives.

This is the Bayesian-facing side:

```text
evidence -> hypothesis -> belief update -> predicted outcome
```

### 2. Cyclic coherence constraint

The object must support mutually constraining variables and loops.

This is the Markov-facing side:

```text
harm / benefit / salience / fatigue / affordance / uncertainty / residue / goal persistence
```

### 3. Latent-node discovery

The object must infer hidden nodes that explain otherwise fragmented signals.

Examples:

```text
noise + shadow + smell + movement -> latent node: dog in the room
```

```text
failed trajectories + rising residue + low initiation -> latent node: blocked goal state
```

This means the graph cannot assume all relevant nodes are pre-specified. It needs node birth, node retirement, merging, splitting, and relabelling.

### 4. Granularity zoom / abstraction control

The object must move between levels of description.

Examples:

```text
sensory gradient -> local affordance -> trajectory -> goal -> superordinate goal -> ethical constraint
```

The system must infer not only what is true, but what **level of description** should currently control action.

### 5. Action-coupled update

The object must not merely represent the world. It must act into the world and update from consequences.

Possible loop:

```text
belief -> action -> outcome -> prediction error -> memory / belief / constraint update
```

### 6. Precision / gain / salience modulation

The object must be able to weight some variables, constraints, scales, or edges more strongly than others depending on context.

This may map to REE control-plane function.

### 7. Temporal persistence and offline consolidation

The object must preserve unresolved structure across time, then revise / compress / reconcile it offline.

This maps to REE sleep / consolidation and residue.

### 8. Residue preservation

The object must preserve unresolved morally relevant facts even after action commitment.

This is a REE-specific constraint not naturally captured by reward-maximising or prediction-error-minimising accounts.

---

## Possible formal sketch

Let:

```text
G_t = (V_t, F_t, E_t, S_t, A_t, P_t, R_t)
```

Where:

```text
V_t = variable / latent / claim nodes at time t
F_t = factor, constraint, or compatibility functions
E_t = typed directed and undirected edges
S_t = scale / abstraction structure
A_t = available actions or interventions
P_t = precision / salience / gain weights
R_t = residue / unresolved persistence traces
```

The object requires operators:

```text
update_evidence()
propagate_constraint()
infer_latent_node()
merge_nodes()
split_node()
coarsen()
refine()
shift_granularity()
select_action()
consolidate_offline()
preserve_residue()
```

The distinctive object is not just the graph. It is the graph plus its allowed transformations.

---

## Relation to REE

Potential REE mappings:

| Capacity | REE mapping |
|---|---|
| directed evidence update | world-model / prediction error |
| cyclic coherence | affect, drive, salience, residue, ethical constraint |
| latent-node discovery | hidden state inference / formulation / blocked-goal recognition |
| granularity zoom | sensorimotor to ethical abstraction control |
| action-coupled update | E3 trajectory commitment and outcome update |
| precision / gain | control plane |
| offline consolidation | sleep / memory / residue integration |
| residue preservation | moral non-erasure after action |
| scope gating | claims-index v3/v4/v5 distinction |

---

## Relation to claims index

The same object may also describe the claims index.

Claims-index equivalents:

```text
latent node discovery -> identify hidden assumptions / missing claims
coarsen -> merge detailed claims into a higher-level architecture principle
refine -> split vague claims into testable subclaims
cyclic coherence -> detect mutually constraining claims
residue -> preserve unresolved conflict instead of overwriting it
scope gating -> decide v3-blocking vs v4+ vs research-only
```

This may make the claims index an externalised version of the same structured uncertainty process hypothesised for the agent.

---

## Research directions to drill next

Initial neighbouring formalisms:

- factor graphs;
- dynamic Bayesian networks;
- Markov random fields;
- probabilistic graphical model structure learning;
- latent variable models;
- hierarchical Bayesian modelling;
- nonparametric Bayesian models;
- probabilistic circuits;
- predictive processing;
- active inference;
- neural sampling;
- probabilistic population codes;
- information bottleneck;
- abstraction / coarse-graining / renormalisation;
- graph rewriting / dynamic graphs;
- causal discovery with latent variables;
- options / temporal abstraction in reinforcement learning;
- world-model and state-abstraction literature.

The task is not to pick one of these as the answer. The task is to identify what each captures and what remains missing.

---

## Scope warning

This may deserve a separate repository later, probably something like:

```text
structured-uncertainty-fields
```

But before **Sunday 19 July 2026**, recommended handling is:

- preserve and refine the thought;
- build a literature map;
- avoid making it a REE-v3 dependency;
- use it only to clarify current design and claims-index structure if helpful.

---

## Open questions

1. What formalism best supports both directed and undirected relationships?
2. What formalism best supports latent-node birth / death / merge / split?
3. What formalism best supports granularity zoom and abstraction-level selection?
4. What formalism best supports action-coupled inference?
5. What formalism best supports residue-like persistence of unresolved constraints?
6. Can this be made computationally tractable in toy settings?
7. What is the smallest example that demonstrates the object without overclaiming?
8. Does this belong in REE_assembly long-term, or a separate `structured-uncertainty-fields` repo?
