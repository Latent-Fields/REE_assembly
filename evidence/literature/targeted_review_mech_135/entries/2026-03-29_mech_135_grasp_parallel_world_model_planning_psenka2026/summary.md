# Summary: Psenka, Rabbat, Krishnapriyan, LeCun & Bar (2026) — Parallel Stochastic Gradient-Based Planning for World Models (GRASP)

**Entry ID:** 2026-03-29_mech_135_grasp_parallel_world_model_planning_psenka2026
**Claim tested:** MECH-135 (planning.e1_e2_parallel_rollout)

---

## What the paper did

This arXiv preprint from Meta FAIR, UC Berkeley, and NYU introduces GRASP (Gradient RelAxed Stochastic Planner), a planning algorithm for learned latent world models. The problem they address is well-defined: sequential trajectory rollout in a learned world model (the "shooting" method) is vulnerable to gradient explosion and local minima because errors compound across timesteps when differentiating through the full sequence. GRASP's solution is to treat future latent states as independent optimization variables -- what they call "lifted" or "virtual" states -- with dynamics constraints applied softly rather than strictly. This decouples the temporal dependencies, allowing all future states to be optimized in parallel. Langevin dynamics (stochastic noise) is added for exploration, and a stop-gradient mechanism handles the non-Euclidean geometry of learned latent spaces. The result is a planner that can be parallelized over timesteps and achieves up to +10% success rate at less than half the compute time versus sequential shooting baselines on D4RL and DeepMind Control Suite benchmarks.

## Key findings

The central computational finding is that *parallel optimization of future states* outperforms sequential rollout both in solution quality and computational efficiency. The soft constraints mechanism is key: by allowing virtual states to evolve under gradient pressure rather than being strictly chained to their predecessors, GRASP escapes the local minima that trap sequential planners. The Langevin noise prevents early commitment to suboptimal trajectories. The stop-gradient on the world model's Jacobian at the action interface prevents the gradient instabilities that arise in full differentiable planning. Together, these constitute an existence proof that parallel latent state evolution during planning is not just a biologically motivated design choice -- it is demonstrably superior to sequential evaluation on standard planning benchmarks.

## REE translation

GRASP provides computational evidence for a key aspect of the MECH-135 rationale: that sequential evaluation of trajectory steps introduces avoidable errors that parallel co-evolution can correct. In the REE context, if z_world is held fixed during an E2 rollout and updated only after the rollout completes, the trajectory being evaluated is planned against a stale world model. GRASP's "lifted states" formulation is an abstract analogue of allowing z_world to co-evolve under E2's influence at each step, rather than being fixed throughout. The performance improvement GRASP demonstrates -- in a purely computational setting, without any biological constraints -- lends engineering plausibility to MECH-135's claim that the parallel architecture produces better trajectory evaluation than the sequential alternative. This is relevant evidence even though the mechanism differs.

## Limitations and caveats

The mapping requires care. GRASP operates within a single world model; MECH-135 claims that two structurally distinct models (E2 fast/cerebellar and E1 slow/cortical) must co-evolve. GRASP shows that parallel state optimization within one model is beneficial -- it does not show that having a *separate, slower* model tracking a different latent (z_world vs z_self) and co-evolving with the fast model is necessary. A single faster model with GRASP-style parallel rollout might accomplish the same thing. The paper is also a preprint and has not yet gone through peer review, which reduces the source quality assessment. Additionally, the computational motivation for parallelism in GRASP (optimization landscape escape) differs from REE's biological motivation (time-delay compensation, Kalman-style state tracking), which means the evidence is supportive in spirit but not mechanistically aligned. A skeptic of MECH-135 could correctly note that GRASP demonstrates parallel optimization benefits within a model, not the necessity of two coupled models.

## Confidence reasoning

The confidence of 0.55 reflects a genuine mixed assessment. The paper supports the *utility* of parallel latent computation during planning, which is a necessary component of the MECH-135 argument, but does not test the *two-model co-evolution* structure that is the claim's specific architectural commitment. The preprint status, single-model architecture, and motivational mismatch collectively keep confidence below 0.60. This entry is most useful as a computational plausibility argument and a pointer to the active engineering work on parallel planning -- it contextualizes MECH-135 within a contemporary ML research agenda that has independently arrived at similar architectural conclusions for functional reasons.
