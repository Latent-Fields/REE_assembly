# Koechlin & Hyafil 2007 -- Frontopolar cognitive branching and its structural limit

**Claims:** SD-046 (primary), SD-033e, MECH-264
**Direction:** supports (with a structural-limit caveat)
**Confidence:** 0.74

## What the paper did

Koechlin & Hyafil synthesise behavioural and model-based fMRI evidence into a now-canonical account of what the lateral frontopolar cortex (FPC, lateral area 10) is *for*. Their proposal: the FPC implements **cognitive branching** -- the ability to set aside an ongoing task in a *pending, counterfactual* state ("I will return to this") while engaging a second task, and then to re-engage the first without losing its task-set. Critically, they argue this capacity is bounded by a hard **structural limit**: humans can hold one pending branch (two task-sets in play), but cannot recursively branch between more than two tasks. The frontopolar lobe is what lets you keep the alternative you are *not* currently doing alive.

## Findings relevant to the claims

This is the direct biology behind the V4 goal-deliberation roadmap's central move -- from a single committed trajectory to a layer that *holds the alternative you didn't pick*. Three mappings:

- **SD-046 (multi-slot GoalState).** Branching is the neural primitive for a parked goal slot: the pending task-set held in counterfactual status is exactly what a second GoalState slot represents when its trajectory is not the one committed this tick. The paper's structural limit is the most useful constraint it supplies: it argues the honest default is **N = 2** (one engaged + one pending), and that N = 3-4 is not free -- it must be earned against a capacity bound. This is why I tag SD-046 as the primary claim even though SD-033e/MECH-264 are the named frontopolar pair: SD-046 is the claim that was *un*grounded before this pull, and branching is its cleanest biological anchor.
- **SD-033e (frontopolar-analog deliberation substrate).** The engage<->deliberate / engage<->branch transition the claim reserves is precisely the FPC's branching operation. Already near-ceiling from the prong_d pull (Boorman/Mansouri/Burgess); this entry adds the branching-specific anchor that prong_d's Koechlin paper (the *Summerfield* information-theoretic gradient paper, a different 2007 Koechlin paper) did not cover.
- **MECH-264 (counterfactual-value tracking).** Branching maintains a pending alternative; MECH-264 maintains a running *value* estimate of that alternative. The paper grounds the maintenance substrate; Boorman 2009 (prong_d) grounds the value-tracking computation that rides on it.

## Limitations and caveats

The headline finding cuts both ways for REE. It endorses the parked-branch primitive but **constrains** SD-046's slot count: a naive N = 4 discrete-slot design that assumes all four slots carry full counterfactual branch status would, on Koechlin's reading, fail beyond the second slot. The honest design consequence is to treat slots 3-4 as capacity-degraded (stored-but-not-fully-branchable), not as four equal branches. There is also a construct gap: human dual-task *branching* alternates between two task-sets, whereas SD-046 proposes simultaneously-active goals each spawning ghost-bank ranks and proposers -- the parallel-monitoring side is Mansouri 2017 / MECH-265 territory, not this paper's. And the localisation is human-elaborated; transfer to an artificial agent is an architectural analogy.

## Confidence reasoning

Source quality is high (Science, foundational, model-based fMRI). I held overall confidence at 0.74 rather than higher because mapping_fidelity is moderate-high (the structural-2 limit qualifies SD-046 rather than cleanly confirming it) and transfer risk is real (human FPC -> artificial multi-slot state). It raises SD-046's literature confidence from zero to a genuine grounding, which is the point of this node; it promotes nothing (exp_conf stays 0; SD-046 is candidate / implementation_phase v4).
