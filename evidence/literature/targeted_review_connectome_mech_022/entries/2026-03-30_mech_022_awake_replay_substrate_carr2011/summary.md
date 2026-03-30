# Summary: Carr, Jadhav & Frank (2011) — Hippocampal Replay in the Awake State

**Entry:** 2026-03-30_mech_022_awake_replay_substrate_carr2011
**Claim tested:** MECH-022 — Hippocampal systems inject hypotheses gated by control plane
**Evidence direction:** supports | **Confidence:** 0.72

---

Carr, Jadhav and Frank's 2011 Nature Neuroscience review is probably still the best single entry point for understanding *when* hippocampal replay occurs and *what* it is likely doing. The paper focuses on the awake state specifically — a deliberate focus, because the field had for years equated hippocampal replay with sleep consolidation, and the awake component had been underappreciated. Their central claim is that awake replay is a mechanistically distinct phenomenon: it occurs during brief pauses (typically post-reward or at decision points), it reactivates previously experienced spatial sequences on a compressed timescale, and it can represent trajectories from environments the animal is not currently in (remote replay).

The temporal structure of awake replay is particularly relevant to MECH-022. Replay events are short (50-150ms), time-compressed (20-30x behavioural speed), and occur in clusters associated with SWRs. They are not continuous background activity — they are episodic, punctuate the ongoing behaviour, and are concentrated at moments when the animal is behaviorally least engaged with the current sensory input (pausing, resting, consuming reward). This is almost a caricature of what MECH-022 needs: the injection events are discrete, they occur during quiescent control-plane states, and their content is retrieved from stored memory rather than reconstructed from current sensation.

The "remote replay" observation is worth pausing on. The fact that replay can represent environments the animal is not currently in suggests that the injection mechanism does not require sensory priming from the current context. This has two implications for REE: it means the HippocampalModule can in principle surface trajectories from previously visited harm scenarios even when the current environment contains no obvious cues, and it means the control-plane gate is not purely reactive to sensory input but is internally generated. This is consistent with MECH-022 but also raises the question of what determines which remote trajectory is selected — a question the paper notes remains unresolved.

The review also documents that sensory information can *influence* replay content — suggesting that while the gate is internal, it is not closed to current-state information. This bidirectional sensitivity (internally gated but externally influenced) maps onto REE's architecture in a satisfying way: the control plane opens the gate, but the current z_world state biases what gets retrieved. That said, the mechanism of content selection is not well enough understood in the biology to specify how this would be implemented in HippocampalModule.

Confidence is 0.72: the phenomenology directly supports MECH-022's hypothesis injection claim, but the immobility-triggered biological gate translates imperfectly to REE's discrete control-plane signal, and the paper is a review (phenomenological) rather than a causal intervention study.
