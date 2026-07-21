# Dynamic Latent-Scale Inference Field — Initial Research Map

Status: processed
Processed in:
- `docs/claims/claims.yaml` (Q-079 `structured_uncertainty_field_distinctness` -- the DLIF / structured-uncertainty field question; verdict ANSWERED-NEGATIVE: DLIF is NOT a distinct mathematical object, it decomposes into factor-graph unification + Bayesian-nonparametric structure learning + active inference + ARC-013 residue. This file is cited in that claim's `sources`.)


**Date:** 2026-06-20  
**Status:** research_map / literature_drill_start  
**Scope:** neighbouring mathematical and neuroscientific formalisms for the proposed Structured Uncertainty Field / Dynamic Latent-Scale Inference Field  
**Source:** follow-up research pass after capture document  
**Primary benchmark note:** this is not a REE-v3 strict green-board dependency. Preserve the Sunday 19 July 2026 benchmark by keeping this as a parallel research line unless it directly clarifies a current v3 blockage.

---

## Working refinement

The object is probably not best understood as a static graph.

It is better understood as:

```text
graph + typed factors/constraints + scale structure + transformation operators + action loop
```

The core candidate is therefore:

```text
A dynamic latent-scale inference field: a structured uncertainty system that can update evidence, propagate coherence constraints, infer latent nodes, change granularity, act into the world, preserve unresolved residue, and consolidate offline.
```

---

## Nearby formalisms and what they contribute

### 1. Factor graphs

**Contribution:** unify directed and undirected graphical models; provide variable/factor decomposition and message passing.

**Why relevant:** factor graphs can represent the strengths of Bayesian networks and Markov random fields in a common form.

**Likely limitation:** mostly assume a specified graph/factor structure. They do not by themselves solve latent-node birth/death, scale selection, action coupling, or residue preservation.

Representative source:

- Brendan J. Frey, `Extending Factor Graphs so as to Unify Directed and Undirected Graphical Models`, arXiv:1212.2486.

### 2. Dynamic Bayesian networks

**Contribution:** directed probabilistic dependencies across adjacent time steps.

**Why relevant:** useful for modelling state_t -> state_t+1, outcome prediction, and sleep/offline belief revision.

**Likely limitation:** directed acyclic per time slice / specified structure; weak on cyclic coherence and flexible granularity.

Representative source:

- Dynamic Bayesian network literature; see Paul Dagum / two-timeslice Bayesian network tradition.

### 3. Markov random fields / Markov networks

**Contribution:** cyclic, undirected mutual constraint and compatibility structure.

**Why relevant:** close to REE's coherence-field side: affect, harm, benefit, residue, salience, fatigue, affordance, goal persistence.

**Likely limitation:** weak directionality; does not naturally represent evidence -> claim -> experiment -> result flow.

Representative source:

- Markov random field / Gibbs random field literature.

### 4. Active inference / free-energy principle

**Contribution:** perception and action are coupled; agents update models and act to reduce expected free energy.

**Why relevant:** captures action-coupled inference and information-seeking behaviour better than passive Bayesian updating.

**Likely limitation for REE:** does not obviously include REE-specific moral residue, non-erasure, claims governance, or explicit granularity zoom.

Representative sources:

- Da Costa, Parr, Sengupta, Friston, `Neural dynamics under active inference`, arXiv:2001.08028.
- Da Costa et al., `Active inference on discrete state-spaces: a synthesis`, arXiv:2001.07203.

### 5. Bayesian nonparametrics / hierarchical Dirichlet processes

**Contribution:** can infer an unbounded or initially unknown number of latent clusters/states.

**Why relevant:** points toward latent-node discovery rather than assuming all variables are pre-specified.

**Likely limitation:** often cluster/state discovery rather than full graph-transforming action-coupled inference.

Representative sources:

- Teh, Jordan, Beal, Blei, `Hierarchical Dirichlet Processes`, Journal of the American Statistical Association, 2006.
- Infinite hidden Markov model / hierarchical Dirichlet process hidden Markov model literature.

### 6. Causal discovery with latent variables

**Contribution:** attempts to recover causal structure when hidden causes/confounders exist.

**Why relevant:** helps with latent-node inference and hidden assumption discovery.

**Likely limitation:** often observational-data focused and not naturally coupled to ongoing action, scale zoom, residue, or ethics.

Representative sources:

- Fast Causal Inference / partial ancestral graph tradition.
- Recent RelFCI and latent-variable causal discovery work.

### 7. Information bottleneck and abstraction

**Contribution:** formalises compression while preserving task-relevant information.

**Why relevant:** granularity zoom likely requires compressing detail into useful abstraction without losing action-relevant content.

**Likely limitation:** compression target must be specified; does not by itself decide ethical salience, residue preservation, or action commitment.

Representative source:

- Tishby, Pereira, Bialek, `The Information Bottleneck Method`, arXiv:physics/0004057.

### 8. Temporal abstraction / options in reinforcement learning

**Contribution:** agents act and plan over multiple temporal scales.

**Why relevant:** REE needs trajectories, subgoals, superordinate goals, and persistence across delayed feedback.

**Likely limitation:** often assumes reward-like objectives and may not capture non-scalar residue or ethical non-erasure.

Representative source:

- Machado, Barreto, Precup, Bowling, `Temporal Abstraction in Reinforcement Learning with the Successor Representation`, arXiv:2110.05740.

### 9. Probabilistic circuits

**Contribution:** tractable probabilistic inference under structural constraints.

**Why relevant:** arbitrary inference over dynamic cyclic latent-scale graphs will be computationally hard; tractability constraints may be essential.

**Likely limitation:** tractability often comes from strong structural restrictions; may not naturally handle flexible graph rewriting and action-coupled scale shifts.

Representative sources:

- Probabilistic circuits literature.
- Wang and Kwiatkowska, `Compositional Probabilistic and Causal Inference using Tractable Circuit Models`, arXiv:2304.08278.

### 10. Neural sampling / probabilistic population codes

**Contribution:** possible neural implementation families for representing uncertainty over latent causes.

**Why relevant:** supports the idea that the brain may implement probabilistic inference without literal explicit Bayesian networks.

**Likely limitation:** often addresses representation / coding rather than whole-agent graph transformation, action selection, claims governance, or moral residue.

Representative sources:

- Ma, Beck, Latham, Pouget, `Bayesian inference with probabilistic population codes`, Nature Neuroscience, 2006.
- Shivkumar et al., `A probabilistic population code based on neural samples`, arXiv:1811.09739.

---

## Initial synthesis

Each neighbouring formalism captures part of the object:

| Needed capacity | Nearby formalism |
|---|---|
| directed evidence update | Bayesian networks / dynamic Bayesian networks |
| cyclic coherence | Markov random fields / factor graphs |
| unified message passing | factor graphs |
| action-coupled inference | active inference |
| unknown latent structure | Bayesian nonparametrics / causal discovery with latents |
| granularity / compression | information bottleneck / abstraction literature |
| temporal scale | options / temporal abstraction / successor representation |
| tractability | probabilistic circuits |
| neural plausibility | neural sampling / probabilistic population codes |
| graph transformation | graph rewriting / dynamic graph systems |
| REE moral persistence | residue / non-erasure; not captured cleanly elsewhere |

The gap is the combination.

---

## Provisional research claim

```text
No single neighbouring formalism appears to fully capture the target object. The proposed Structured Uncertainty Field may be useful precisely because it combines: directed evidence update, cyclic coherence, inferred latent structure, scale transformation, action coupling, precision modulation, offline consolidation, and residue preservation.
```

---

## Next drill sequence

1. Factor graphs and message passing: what can be reused directly?
2. Latent structure learning: what supports node birth/death/merge/split?
3. Abstraction / information bottleneck: what formalises granularity zoom?
4. Active inference: what should be borrowed, and where does REE diverge?
5. Tractability: what toy object can actually run?
6. REE residue: what is genuinely novel / non-standard?

---

## Minimal toy target

A first toy demonstration should be tiny:

```text
observations: partial sensory cues
latent inference: hidden cause proposed
coherence: constraints across cues and goals
scale shift: local cue -> abstract goal state
action: choose probe / commit action
residue: preserve unresolved harm/conflict trace
consolidation: offline merge/split/reweight after outcome
```

The toy should demonstrate the object rather than solving a large task.

---

## Scope warning

Do not make this a REE-v3 strict green-board requirement.

Use it before Sunday 19 July 2026 only if it clarifies:

- why a v3 experiment fails;
- how to classify a claim;
- how to avoid scope creep;
- how to name a current architectural gap.
