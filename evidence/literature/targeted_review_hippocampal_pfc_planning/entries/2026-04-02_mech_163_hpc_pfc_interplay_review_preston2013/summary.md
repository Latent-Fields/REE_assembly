# Preston & Eichenbaum (2013) — HPC-PFC Interplay: Division of Labor for MECH-163 and ARC-035

**Claims tested:** MECH-163, ARC-035
**Evidence direction:** supports | **Confidence:** 0.74

---

## What the paper did

Preston and Eichenbaum synthesised a decade of convergent human fMRI, rodent electrophysiology, and computational modelling work to articulate a detailed division of labor between hippocampus and prefrontal cortex in memory. Their framework centres on a key asymmetry: the hippocampus rapidly encodes episodic events with high precision (pattern-separated representations that preserve episode-specific detail), while PFC slowly builds schematic knowledge that captures regularities across many episodes. Critically, this is not a static division — PFC top-down projections to hippocampus actively guide encoding and retrieval in the moment, biasing which representations are activated based on current goals and schemas.

The review draws on three streams of evidence: studies showing that PFC is required for schema-based memory performance even when HPC lesions leave individual memory intact; fMRI studies showing that HPC-PFC connectivity at encoding predicts subsequent memory, especially for schema-congruent information; and computational modelling work showing that the complementary learning systems architecture (fast HPC, slow PFC/neocortex) naturally produces the behavioural profile of human episodic and semantic memory.

## Key findings for MECH-163 and ARC-035

**MECH-163 (multi-step planning via VTA/hippocampal system):** The Preston/Eichenbaum framework provides the functional division of labor that MECH-163 requires. In multi-step planning, the hippocampus contributes the trajectory structure — the sequential action-consequence relationships stored as episodic traces and replayed during planning. PFC contributes the goal context that biases which trajectories are retrieved and evaluated. The hippocampus cannot plan without PFC's goal signal; PFC cannot plan without hippocampus's trajectory library. This is the architecture MECH-163 specifies at the V3/V4 boundary.

**ARC-035 (vmPFC loads content into hippocampal nodes):** The review's characterisation of PFC→HPC top-down projection as a goal-context biasing mechanism is precisely the mechanism ARC-035 claims. vmPFC does not compute trajectories — it does not perform the rollout. Instead, it provides goal representations that activate appropriate hippocampal nodes, biasing the attractor landscape so that goal-consistent trajectories are favoured during prospective simulation. The hippocampus retains authorship of the trajectory geometry; vmPFC provides the goal prior that shapes which geometry is accessed.

The review also notes an important asymmetry: once a schema is well-learned, PFC can support retrieval even without HPC — but novel multi-step planning (requiring the hippocampus's flexible relational encoding) is HPC-dependent. This maps onto REE's claim that the first encounter with a novel harm trajectory requires hippocampal encoding, while familiar trajectories can be handled by PFC schema retrieval.

## Limitations

The review focuses on encoding and retrieval of episodic and semantic memories, not on real-time sequential decision-making or multi-step planning. The application to MECH-163's online planning circuit is an extension of the framework beyond its explicit scope. The PFC→HPC projection characterised here is based on memory encoding/retrieval paradigms — whether the same pathway operates in the planning/prospective simulation mode has been shown by Benchenane et al. (2010) and Ito et al. for theta-scale coupling, but Preston/Eichenbaum do not directly address this timescale. ARC-035's specific vmPFC node (as opposed to lateral PFC schema retrieval) requires the Gauthier & Tank and HPC-vmPFC connectivity literature for full grounding.
