# Lin et al. (2026) - Neural sampling from cognitive maps enables goal-directed imagination and planning

**Claim tested:** ARC-018 - hippocampus generates explicit rollouts and post-commitment viability mapping, indexed by E2 action-object coordinates and updated by E3 harm/goal error.

**Primary source:** Lin, H., Yang, Y., Zhao, R., Pezzulo, G. and Maass, W. (2026). *Neural sampling from cognitive maps enables goal-directed imagination and planning*. Nature Machine Intelligence 8:1045-1065. DOI: [10.1038/s42256-026-01254-4](https://doi.org/10.1038/s42256-026-01254-4). Preprint DOI: [10.1101/2025.05.14.654027](https://doi.org/10.1101/2025.05.14.654027). Code/data: [LH-cbicr/GCML](https://github.com/LH-cbicr/GCML); Zenodo: [10.5281/zenodo.19370442](https://doi.org/10.5281/zenodo.19370442). Secondary trigger: Neuroscience News, ["Brain-Inspired AI Uses Cognitive Maps"](https://neurosciencenews.com/brain-inspired-ai-cognitive-maps-31145/).

## What the paper did

The authors build a generative cognitive map learner (GCML) that combines three ingredients: a learned cognitive map, stochastic action sampling, and compositional coding. In the spatial case, a grid-cell-like map learns both forward structure and a simple inverse model that maps a goal-current-state difference to action commands. With noise in virtual action selection, iterating this inverse/forward loop samples imagined goal-directed trajectories.

They then generalize the same form beyond physical space. In abstract graph tasks, the model samples multiple near-shortest paths from start to goal, with higher noise producing more diverse paths that can be useful when later reward/loss structure is assigned to nodes. In compositional silhouette assembly/decomposition tasks, the same cognitive-map sampling scheme works over building-block states rather than locations, including test silhouettes larger than the training examples. The paper also compares graph replanning and working-memory-style search costs against exact baselines: GCML is less exact but much cheaper when the start or goal changes because it reuses the learned map instead of re-enumerating the graph.

## REE interpretation

This is a strong formal analogue for the combination REE already names across ARC-018 and ARC-065:

- ARC-018: a cognitive map can generate prospective, goal-directed imagined trajectories by repeatedly applying a forward model from internally generated next states.
- ARC-065: stochasticity in the proposal layer can be useful when it remains goal-directed; randomness is not valuable as noise alone, but as diversity around a map-guided homing heuristic.
- Q-074 / MECH-300: non-spatial and compositional problem domains can still be traversed as cognitive maps when relational structure is encoded geometrically.

The paper is particularly useful because it turns the Pfeiffer/Foster and Mattar/Daw intuition into an explicit algorithmic bridge: goal-directed imagination emerges when the map has both a forward model and a state-difference-to-action inverse model. That maps cleanly onto REE's E2/E3 rollout interface at the level of form.

## What REE already captures

Most of the user's "parallel" is already present in the architecture. REE has hippocampal proposal/rollout machinery (ARC-018), stochastic candidate generation via CEM and diversity controls (ARC-065 and the candidate-support-preserving CEM review), non-spatial cognitive-map grounding (Behrens 2018; Q-074/TEM), and explicit attention to proposal-side diversity rather than only action-selection noise.

So this paper does not require a new REE mechanism. It strengthens the case that REE's direction is not idiosyncratic: map-guided stochastic imagination is a real computational family, not just a metaphor.

## What it does not settle

The paper is not direct neuroscience evidence. It is a computational model inspired by hippocampal/grid-cell data and validated on simulations. It does not show that biological hippocampus uses this exact inverse model, nor that REE's E2 action-object coordinate is the correct map coordinate. It also does not address explicit harm as a first-class viability signal; the benchmarks are goal/path/problem-solving tasks with reward/loss variants, not ethical harm topology.

The important negative constraint is therefore: do not read this as "ARC-018 is now solved." It supports the formal plausibility of a map-guided stochastic rollout generator, while leaving ARC-018's V3-specific gaps unchanged: action-object indexing, live E2 fidelity, candidate support, and harm/goal error updating still have to be earned empirically inside REE.

## Design note

If a future ARC-018 or SD-004 session revisits action-object indexing, Lin et al. is a useful reference for the missing inverse-model discipline: a map is more useful for planning when the difference vector between current and goal states can be mapped to actions that move the agent in the right direction. REE should not import GCML wholesale, but the state-difference-to-action readout is the clean formal contrast to the known action-object roundtrip defects in the current stack.
