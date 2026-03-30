# Summary: Shin, Tang & Jadhav (2019) — Dynamics of Awake Hippocampal-Prefrontal Replay

**Entry:** 2026-03-30_mech_022_hpc_pfc_replay_dynamics_shin2019
**Claim tested:** MECH-022 — Hippocampal systems inject hypotheses gated by control plane
**Evidence direction:** supports | **Confidence:** 0.76

---

Shin, Tang and Jadhav's 2019 Neuron paper is the strongest direct evidence in this directory for MECH-022 because it actually closes the loop: it does not merely show that hippocampus replays trajectories, but that prefrontal cortex *receives* and *uses* that replay content for decision-making. Using simultaneous multi-tetrode recordings in both CA1 and mPFC during a spatial alternation task, they tracked the dynamics of coordinated HPC-PFC replay across the full course of learning.

The key finding has two components. First, coordinated replay (SWR events in hippocampus co-occurring with organised sequential activity in mPFC) distinguishes correct future paths from incorrect alternatives. Both hippocampus and PFC participate in forward (prospective) replay during inter-trial pauses, and this coordination is selective: the correct upcoming path is over-represented relative to alternatives. Second, there is a learning-related shift: early in training, reverse replay (retrospective, evaluating the just-completed path) is dominant; as the animal learns, forward replay (prospective planning) becomes dominant. The PFC tracks this shift, reading out the prospectively-generated hippocampal content to guide the next decision.

This learning trajectory matters for REE in two ways. First, it suggests that MECH-022's hypothesis injection function is not static — the content and directionality of what gets injected changes as E3 learns. Early in training, the system might primarily replay and evaluate recent harm trajectories (retrospective); later, it would shift toward injecting candidate future trajectories (prospective). This is a prediction that REE's HippocampalModule should reproduce. Second, the PFC engagement during correct-path replay (but not error trials) suggests that injection is not just broadcasting but is selective — the system is not injecting random stored paths, but ones that are relevant to the current goal-state. This is exactly what MECH-022's "gated by control plane" language implies.

The failure case is also informative: on error trials, the hippocampal-prefrontal coordination was disrupted. Specifically, replay sequences during inter-trial periods were impaired prior to navigation on error trials. This is consistent with MECH-022's prediction that failures of hypothesis injection (gating failures) should lead to suboptimal path selection — in REE terms, a failure of the HippocampalModule to inject viable trajectories would leave E3 selecting from a reduced candidate set, increasing harm exposure.

The mapping caveat is important: REE's E3 is not purely equivalent to PFC. E3 is a composite of hippocampal indexing, trajectory evaluation, and commitment gating — it is more than a prefrontal readout. The data here establish the HPC->PFC pathway, but the internal E3 mechanism by which injected hypotheses are evaluated and selected is not illuminated by this paper.

Confidence is 0.76: direct empirical evidence for HPC->PFC injection during goal-directed behavior, good mapping fidelity with a meaningful caveat about E3 being more than PFC.
