# Daw, Niv & Dayan 2005 — Uncertainty-based competition between PFC and dorsolateral striatum

According to PubMed: Daw, Niv & Dayan. *Nature Neuroscience* 8(12):1704-1711 (2005). [DOI 10.1038/nn1560](https://doi.org/10.1038/nn1560). PMID 16286932.

## What the paper did

The paper synthesises a large body of behavioural and lesion evidence that the brain contains multiple systems for behavioural choice and offers a normative Bayesian framework for how those systems compete. Empirically, two systems are well-established. A goal-directed system, primarily implemented in prefrontal cortex and dorsomedial striatum, learns and uses a model of the environment to plan action by simulation — flexible, statistically efficient, but computationally expensive. A habitual system, primarily in dorsolateral striatum, caches state-action values directly from experience without an internal model — computationally cheap, but inflexible to outcome devaluation.

The authors' contribution is the arbitration framework. They propose that the brain compares the *uncertainty* of each system's prediction and deploys whichever is currently more accurate. The model-based system tends to win early in learning (when the habit cache is undertrained) and after surprise (when cached values are stale); the model-free system takes over once the habit cache stabilises. Bayesian principles formalise the comparison.

## Why this matters for REE's decomposition question

This is the canonical paper for the action-decomposition question. If biology decomposes action representation, the most empirically robust decomposition is **at minimum two levels**: a model-based goal-directed planner and a model-free habit cache. Daw 2005 grounds this with substrate-level evidence (lesion dissociations, fMRI signatures, behavioural transfer-paradigm data).

For REE V3 the architectural mapping is direct. The model-based system has a clear V3 analogue: `HippocampalModule.propose_trajectories` runs the E2 transition model rolled forward through CEM, scored by E3 against goal and harm criteria, with MECH-293 ghost-goal probes biasing the seed states. That is functionally a goal-directed model-based planner.

The model-free system has **no V3 analogue at all**. There is no cached state-action value table. There is no substrate that, given a frequently-visited state, returns "the action you usually do here" without running a rollout. Every action decision in V3 goes through the proposer + selector path. That is biologically the model-based pathway, all the time. The habit cache is missing.

Architecturally for REE this is a real lacuna with concrete consequences:

- **Monostrategy lock-in.** Without a habit cache, agents cannot exhibit the canonical biological habit-formation curve where flexibility decreases with practice. V3 monostrategy lock might partly reflect the absence of a habit substrate to *off-load* repeated trajectories from the proposer.
- **OCD / automaticity modelling.** Compulsive behaviour is biologically a habit-system runaway (Graybiel 2008, separate entry). REE cannot express OCD-like automaticity faithfully without a habit-cache substrate that can over-train.
- **Computational efficiency.** The biological reason the habit cache exists is computational economy. A V4 environment with longer horizons would benefit from caching frequently-traversed action sequences rather than re-rolling them through CEM each tick.

The architectural recommendation: a habit-cache substrate is a real candidate SD for V3 or V4, not just a V4 luxury. The question is whether V3's current monostrategy issues are partly a habit-substrate issue or wholly a goal-substrate issue (multi-goal arbitration, MECH-269 V_s gating, etc.).

## What it does NOT settle

The Daw 2005 framework is a flat two-system decomposition. More recent literature (Dolan & Dayan 2013 in this same review) argues for a *spectrum* rather than a clean dichotomy, and Botvinick 2009 (also in this review) argues for an additional *hierarchical option* level above goal-directed planning. An REE commitment to two-and-only-two systems would over-simplify; the canonical reading is at minimum three levels (habit, goal-directed, hierarchical options) plus motor primitives below.

REE's existing ARC-021 already specifies three BG-like cortico-striatal loops with distinct learning channels — a richer architecture than the Daw 2005 two-system model. So adding a habit cache to REE is not "adding the model-free system." It is filling in the cached-action-value role within the existing three-loop framework. The architectural slot is somewhere within ARC-021's three-loop scaffold, probably in the dorsolateral-loop slot.

The paper does not specify the arbitrator substrate precisely. ACC is one candidate; the dACC-analog in SD-032b is functionally close. Whether REE's existing dACC adapter is sufficient to arbitrate model-based vs model-free predictions, or whether a dedicated arbitrator substrate is needed, is open.

## Confidence reasoning

I sit this at 0.85. Source quality 0.90 — *Nature Neuroscience*, foundational, framework remains canonical 20 years later with substantial empirical accumulation. Mapping fidelity 0.82 because the model-based / model-free dichotomy maps cleanly onto REE's existing planner and the missing habit substrate, with the caveat that ARC-021's three-loop framing is richer than Daw 2005's two-system framing. Transfer risk 0.25 because the framework is computational and translates directly to REE's architectural scaffolding.
