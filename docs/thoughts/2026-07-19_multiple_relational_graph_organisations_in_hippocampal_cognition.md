# Thought Intake: Multiple Relational Graph Organisations in Hippocampal Cognition

Status: processed

Processed in:
- `evidence/planning/thought_intake_2026-07-19_multiple_relational_graph_organisations_hippocampal.md` (structured intake, already-owned split, routing)
- `docs/claims/claims.yaml` -- MECH-468 (anchor topology carries functional information absent from local payloads), MECH-469 (relation types not collapsible to one adjacency), MECH-470 (topological position improves ghost-goal reactivation ranking), Q-084 (higher-order metapath/hyperedge structure -- gated, do not build)

No experiment proposal minted: the routing's first move is an EDGE-TYPE INVENTORY spike against logged telemetry (open questions 1-3), not a probe. The organisational/representational separation travels with all four claims -- this does NOT justify replacing the hippocampal representation with a GNN. Candidate 5 (biological multiple-relational-organisation question) deliberately NOT registered: out-of-domain, routed to /lit-pull.

---

**Status:** Thought Intake / Literature Search Seed / Possible Experimental Design Seed

**Prompting source**

*A Coding Implementation on Spatial Graph Neural Networks for Urban Function Inference Using city2graph, OSMnx, and PyTorch Geometric*

The source is a practical implementation tutorial rather than primary evidence about hippocampal biology. Its value is therefore conceptual and methodological: it demonstrates how the functional identity of a location can be inferred from relational position, neighbourhood structure, typed edges, and multistep paths rather than from intrinsic features alone.

---

# Central Thought

Hippocampal function may be encoded not only in the content of individual locations, states, anchors, or episodes, but in the typed relations among them.

The relevant relations may include:

- spatial proximity,
- temporal succession,
- action reachability,
- causal dependency,
- event membership,
- shared goal relevance,
- harm and benefit structure,
- motivational significance,
- social relation,
- contextual similarity.

These relation types are not necessarily reducible to one universal adjacency structure.

The hippocampal system may therefore contain, generate, or support several partially distinct relational organisations, each serving different cognitive functions.

---

# Repository-Grounded Starting Point

REE already uses a relational hippocampal architecture.

Its hippocampal map is organised around action objects and candidate trajectories rather than being a simple Cartesian map of physical location.

The current REE-v3 implementation also includes:

- scale-tagged anchors,
- nested event segments,
- per-stream and per-region verisimilitude,
- motivational and goal-state payloads,
- wanting and recoverability,
- residue and valence structure,
- staleness and invalidation,
- backward trajectory credit,
- mode-conditioned proposal generation,
- inactive dual traces,
- ghost-goal retrieval.

The prompting tutorial therefore does not introduce relational hippocampal organisation to REE.

It raises the more specific question:

> Are several different graph semantics already implicit within REE’s hippocampal machinery, and should some of them become explicit for analysis, prediction, or planning?

---

# Functional Identity From Relational Structure

A place, state, or memory may have a functional role that is not fully stored in its own local features.

Its function may instead follow from its position within a wider relational structure.

Examples include:

- gateway,
- bottleneck,
- recurrent trap,
- safe approach route,
- interruption point,
- transition between behavioural regimes,
- goal-supporting region,
- hazard-adjacent region,
- repair opportunity,
- high-recoverability route,
- repeatedly invalidated region.

Such roles may be inferred from:

```text
neighbourhood composition
+
typed connectivity
+
multistep relational paths
+
historical outcomes
+
current goals
```

The same anchor may have different functions under different relational projections.

---

# Multiple Graph Constructions

A single environment can support several legitimate graph constructions.

## Spatial-proximity graph

Two states are related because they are physically or representationally near.

## Transition graph

Two states are related because an action or observed trajectory moves between them.

## Temporal-adjacency graph

Two states are related because they occurred near one another in experienced time.

## Event graph

Two states belong to the same event or nested event structure.

## Causal graph

One state or action is treated as contributing to another outcome.

## Goal-relevance graph

States are related through a shared goal, subgoal, or superordinate objective.

## Harm–benefit graph

States share similar harm, safety, relief, wanting, or benefit structure.

## Social graph

States, agents, or memories are organised through social relationships or partner-specific context.

## Semantic or schema graph

States are related through shared abstract structure despite spatial or temporal separation.

These graph types expose different information.

They should not be collapsed merely because all can be represented with nodes and edges.

---

# Multiple Relational Graph Hypothesis

## Working hypothesis

The biological hippocampal system may support multiple partially independent relational organisations rather than one universal cognitive map.

Different hippocampal subregions, longitudinal axes, entorhinal inputs, cortical partners, or replay regimes may preferentially support different kinds of relational computation.

Possible organisational roles include:

- spatial adjacency,
- temporal succession,
- sequence completion,
- pattern separation,
- pattern completion,
- event segmentation,
- goal-directed action structure,
- relational abstraction,
- contextual reinstatement,
- social or agent-relative structure.

This is a literature-search hypothesis, not an established anatomical mapping.

---

# Candidate Biological Predictions

If multiple relational organisations exist, then the literature may show that:

1. Different hippocampal subregions preferentially encode different relation types.

2. Distinct tasks recruit different hippocampal relational structures even when they involve the same physical environment.

3. Replay may traverse different relational organisations depending on whether the system is planning, consolidating, avoiding harm, pursuing a goal, or reorganising memory.

4. Longitudinal hippocampal differences may correspond to different levels of spatial, temporal, contextual, or abstract granularity.

5. Entorhinal–hippocampal and hippocampal–prefrontal interactions may transform between relational forms rather than simply pass one common map.

6. Offline consolidation may convert episodic transition structures into more abstract semantic or schema-like relations.

7. Lesions or selective disruption of different regions may impair different kinds of graph traversal or relational inference.

---

# Important Caution

REE does not need to claim that the brain literally stores software-style graph data structures.

A graph may be:

- an explicit computational representation,
- a diagnostic projection,
- a mathematical description of transition structure,
- or a useful abstraction over a richer field or dynamical system.

The organisational claim should therefore be kept separate from the representational claim.

```text
Organisational claim:
cognition depends on several distinct relational structures

Representational claim:
those structures should be implemented as explicit graphs
```

The first may be true even if the second is false.

---

# Relation to Dynamic Latent Information Field Research

This thought intake is related to, but distinct from, Dynamic Latent Information Field research.

Dynamic Latent Information Field asks what mathematical substrate may carry uncertainty, latent structure, granularity, affordance, and residue before discrete structures are extracted.

This thought asks:

> Which explicit relational projections are useful once hippocampal structure is extracted or made inspectable?

A possible relationship is:

```text
distributed latent dynamics
        ↓
hippocampal anchors or stable structures
        ↓
typed relational projections
        ↓
functional inference
        ↓
trajectory generation and action
```

The existence of useful graph projections would not establish that the native substrate is graph-like.

---

# Metapaths and Higher-Order Function

Some cognitive functions may be properties of typed multistep paths rather than individual nodes or direct edges.

For example:

```text
current state
→ available action
→ transition region
→ predicted hazard
→ repair opportunity
→ goal completion
```

or:

```text
inactive anchor
→ shared event
→ similar goal state
→ successful historical trajectory
→ candidate reactivation
```

These structures may be better represented by metapaths, hyperedges, simplicial relations, or higher-order constraints than by simple pairwise graphs.

The city2graph implementation is useful here because it makes explicit that graph construction and relation typing determine what information becomes learnable.

---

# Graph Construction as an Epistemic Commitment

The choice of graph is not neutral.

A proximity graph assumes that nearness is relevant.

A transition graph assumes that traversability is relevant.

A causal graph assumes that intervention and consequence are relevant.

A goal graph assumes that common motivational structure is relevant.

A semantic graph assumes that shared abstract structure is relevant.

For REE, the top-down question is therefore:

> Which relations must be preserved so the hippocampal system can support viable prediction, planning, commitment, causal attribution, residue-sensitive learning, and flexible generalisation?

The mathematical graph should follow that organisational answer.

---

# Possible REE Experimental Programme

## Retrospective graph-projection probe

Build several graph projections from existing hippocampal traces.

### Projection A: latent or spatial proximity

Edges reflect similarity or closeness in latent/world space.

### Projection B: action transition

Edges reflect observed or proposed action-mediated transitions.

### Projection C: shared event

Edges connect anchors belonging to the same nested event structure.

### Projection D: shared goal or valence

Edges connect anchors with related goal states, wanting, harm, safety, or benefit structure.

### Projection E: causal or outcome relation

Edges connect actions, states, and resulting outcomes.

### Projection F: heterogeneous typed graph

All relation types remain distinct.

---

# Candidate Prediction Tasks

Test whether graph structure predicts held-out functional labels such as:

- goal-supporting region,
- harm-associated region,
- recurrent trap,
- bottleneck,
- successful completion route,
- stale or invalidated region,
- repair opportunity,
- candidate anchor for reactivation,
- latent behavioural regime,
- likely interruption point.

Compare:

```text
local anchor features alone

versus

topology alone

versus

local features + topology

versus

heterogeneous typed topology
```

If topology adds predictive value, the existing architecture may contain relational information not currently being read out.

---

# Possible Ablations

- Collapse all edge types into one adjacency relation.
- Remove event-based edges.
- Remove goal and motivational edges.
- Remove action-transition directionality.
- Remove inactive or dual-trace anchors.
- Replace metapaths with direct local neighbourhood aggregation.
- Randomise topology while preserving node features.
- Preserve topology while shuffling node payloads.

These could distinguish whether performance depends on:

- anchor content,
- relational position,
- edge type,
- temporal direction,
- higher-order path structure,
- or their interaction.

---

# Candidate Literature Search Programme

## Hippocampal subregion specialisation

Search for differences among:

- dentate gyrus,
- CA3,
- CA2,
- CA1,
- subiculum,
- entorhinal cortex,
- anterior versus posterior hippocampus,
- dorsal versus ventral hippocampus.

Questions:

- Which regions favour pattern separation versus completion?
- Which support sequence prediction?
- Which represent goals, contexts, social relations, or abstract structure?
- Which support temporal versus spatial organisation?

## Cognitive maps beyond physical space

Search terms:

- hippocampal cognitive maps,
- relational memory,
- conceptual spaces,
- abstract cognitive maps,
- social space representation,
- task-state graphs,
- successor representation,
- predictive maps.

## Multiple map systems

Questions:

- Does the hippocampus maintain several maps of the same environment?
- Are maps task-dependent or goal-dependent?
- How are maps remapped across context?
- Can competing maps coexist?
- How are latent task structures selected?

## Replay across relation types

Search terms:

- hippocampal replay planning,
- reverse replay,
- nonlocal replay,
- goal-biased replay,
- schema replay,
- social replay,
- event replay.

## Graph and topology-based analyses

Search terms:

- hippocampal graph representation,
- topological data analysis hippocampus,
- graph neural networks hippocampal modelling,
- community structure cognitive maps,
- metapath cognition,
- higher-order hippocampal representation.

## Hippocampal–prefrontal transformation

Questions:

- Does the hippocampus provide episodic or transition structure while prefrontal systems extract rules and abstractions?
- Are relational structures transformed between regions?
- How do goals alter hippocampal graph traversal?

---

# Current Working Claim

REE already contains several distinct relational semantics within its hippocampal machinery.

The prompting city2graph implementation suggests that these relations may be usefully exposed as multiple typed graph projections and tested for their ability to recover functional roles that are not explicit in local anchor features.

A parallel literature question is whether the biological hippocampal system similarly supports multiple partially distinct relational organisations across its subregions, axes, inputs, and replay regimes.

---

# Immediate REE Implication

This thought does not justify replacing the current hippocampal representation with a graph neural network.

The immediate actions are narrower:

- make current relation types explicit,
- determine which relations are already logged,
- construct retrospective graph projections,
- test whether topology contains additional functional information,
- review biological evidence for multiple hippocampal relational systems.

Any architectural change should follow evidence from those analyses rather than precede it.

---

# Open Questions

1. What are the current explicit and implicit edge types in REE’s hippocampal system?

2. Are spatial, temporal, causal, action, event, goal, and harm relations currently distinguishable?

3. Are some relations stored only indirectly in trajectories or payloads?

4. Can anchor function be inferred from topology when local features are incomplete?

5. Which graph projection best supports planning?

6. Which projection best supports explanation or debugging?

7. Which projection best supports causal attribution and residue?

8. Do hippocampal subregions in biology preferentially encode different relational structures?

9. Are these structures separate maps, task-dependent projections, or expressions of one richer substrate?

10. Do offline processes translate between graph types?

11. Should some REE relations be modelled with hypergraphs, simplicial complexes, or factor structures rather than pairwise graphs?

12. Could topology help identify which inactive anchor should be reactivated during goal pursuit?

---

# Routing

**Primary:** REE hippocampal architecture and future diagnostic experiments

**Secondary:** literature review on multiple hippocampal relational organisations

**Dynamic Latent Information Field relationship:** cross-reference only; related at the projection boundary but not merged

**Source classification:** implementation tutorial / software inspiration, not primary biological evidence

**Current priority:** research and retrospective analysis rather than immediate architectural modification
