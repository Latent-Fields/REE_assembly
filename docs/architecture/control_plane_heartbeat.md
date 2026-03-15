# Control Plane Heartbeat Architecture

**Registered:** 2026-03-15

---

## Overview

The three cortico-striatal-like learning loops of REE (E1/sensorium, E2/action-enacting, E3/planning-gates) do not update their control planes only at completion events. Each loop has a characteristic *heartbeat* — a periodic update rate driven by thalamic pacemaking — that maintains coherence under indeterminate processing latency. Completion events are high-salience signals *within* this continuous stream, not the exclusive trigger for control plane updates.

This document covers six related claims: ARC-023 (multi-rate heartbeat architecture), MECH-089 (cross-frequency coupling), MECH-090 (beta as policy-output gate), MECH-091 (phase reset on salient events), MECH-092 (SWR-equivalent replay), and MECH-093 (z_beta modulates heartbeat rate).

---

<a id="arc-023"></a>
## Each BG loop has a characteristic thalamic heartbeat rate (ARC-023)

**Claim Type:** architectural_commitment
**Subject:** basal_ganglia.three_loop_thalamic_heartbeat
**Status:** candidate
**Claim ID:** ARC-023

The REE architecture requires three distinct periodic update channels, one per learning loop, each driven by thalamic pacemaking:

- **E1 (sensorium loop):** Updates at the sensory frame rate. Essentially continuous — every perceptual timestep generates a prediction error that updates the E1 world model. No action required to trigger an update.
- **E2 (action-enacting loop):** Updates at the motor command rate — faster than E3 deliberation, slower than raw E1 sensory input. Motor-sensory error requires action, but the motor loop does not wait for sequence *completion* to update. Cerebellar-equivalent: ongoing correction during movement.
- **E3 (planning-gates loop):** Updates at the deliberation rate — the slowest of the three. Does not wait for action sequence completion; instead, receives periodic harm/goal estimate refreshes from the thalamic pacemaker. Completion events provide a *high-salience* update within this stream (see MECH-090, MECH-091), but are not the exclusive update trigger.

**Thalamic substrate:** Mediodorsal (MD) thalamus gates the E3 complex; VL thalamus gates the E2 motor pathway; pulvinar and sensory relay nuclei gate E1. The reticular nucleus of the thalamus (TRN) acts as an inter-loop routing switch, gating cross-loop communication at each clock tick.

**Why this is required:** Processing latency for E1, E2, and E3 is indeterminate (variable computation time). Without a thalamic clock, the loops would drift out of phase, producing stale harm estimates mid-plan and inconsistent action selection signals. The heartbeat is the coherence mechanism for a system with asynchronous internal processing.

**Architectural implication:** V2 and V1 substrates use synchronous single-timestep updates (everything updates on the same discrete step). This means the heartbeat architecture cannot be properly tested until V3 implements asynchronous multi-rate loop execution (SD-006).

---

<a id="mech-089"></a>
## Cross-frequency coupling packages fast updates for slow loops (MECH-089)

**Claim Type:** mechanism_hypothesis
**Subject:** thalamus.cross_frequency_coupling_inter_loop_integration
**Status:** candidate
**Claim ID:** MECH-089

Three loops running at different rates cannot simply broadcast to each other — fast updates would overwhelm slow loops, and slow update windows would underrepresent fast events. The mechanism that resolves this is cross-frequency coupling: fast oscillations (E1-rate, gamma-band equivalent) nest *within* slow oscillation cycles (E3-rate, theta-band equivalent). E1's continuous sensory updates are temporally integrated into a rolling summary over each theta cycle, and E3 samples that summary at its own heartbeat rate rather than receiving raw E1 output.

In neuroscience: theta-gamma coupling is well-established in hippocampal-prefrontal circuits. Each theta cycle (~125ms) contains ~5-7 gamma sub-cycles; each gamma sub-cycle can carry a distinct sensory or motor-consequence representation. The thalamic relay performs the cross-rate integration.

**REE implication:** E3 never sees raw E1 prediction error — it sees a theta-cycle-averaged representation of recent sensory state. This temporal abstraction is what makes E3's harm estimates tractable: it operates on integrated context, not moment-to-moment sensory noise. The packaging boundary also defines the minimum meaningful temporal resolution for moral attribution (E3 cannot attribute harm finer-grained than one E3 heartbeat cycle).

---

<a id="mech-090"></a>
## Beta oscillations gate E3 policy-output, not E3 internal updating (MECH-090)

**Claim Type:** mechanism_hypothesis
**Subject:** basal_ganglia.beta_oscillation_policy_output_gate
**Status:** candidate
**Claim ID:** MECH-090

Beta oscillations (~13–30 Hz) in the subthalamic nucleus (STN) and striatum encode a "maintain current state" signal. The critical distinction: beta gates *propagation of E3 model updates to action selection*, not E3's internal model updating.

During a committed action sequence:
- E3 continues updating its harm estimates internally (heartbeat continues)
- Beta power is elevated → E3's updated model state does not propagate to action selection
- The agent continues the current sequence without mid-sequence policy changes

At completion or on a stop-change signal (hyperdirect pathway: cortex → STN → GPi, bypassing striatum):
- Beta power drops
- E3's current model state propagates to action selection
- Policy can change

**Why MECH-057a failed with this framing:** The `attribution_completion_gating` experiment modeled E3 as updating *only* at completion (binary gate). If the correct mechanism is beta-gated propagation within a continuous stream, the experiment's COMPLETION_GATED condition was neither the full mechanism (no internal continuous updating) nor a fair baseline (agent was fully blind between completions). The ATTRIBUTION_BLIND condition may have performed comparably because continuous updating without any beta gate is closer to the correct architecture than episodic gating.

**MECH-057a reframing:** Completion events remain architecturally significant — they are the primary occasions when beta drops and E3 updates propagate. But the claim should be: *completion events are the principal policy-update opportunities within an otherwise beta-gated continuous E3 stream*, not *the E3 control plane only updates at completion*.

**Hyperdirect pathway as fast interrupt:** The STN hyperdirect pathway can force an early beta drop in response to unexpected salient events (e.g. sudden harm signal mid-sequence), providing a rapid interrupt mechanism that does not wait for sequence completion. This is the neural substrate of action-stopping under urgency.

---

<a id="mech-091"></a>
## Salient events phase-reset the E3 heartbeat clock (MECH-091)

**Claim Type:** mechanism_hypothesis
**Subject:** basal_ganglia.salient_event_phase_reset
**Status:** candidate
**Claim ID:** MECH-091

When a high-salience event occurs — action sequence completion, unexpected harm, commitment boundary crossing — it does not merely boost E3 update signal amplitude. It *resets the phase* of the E3 heartbeat oscillator, ensuring the next heartbeat cycle starts from a coherent reference state.

Phase reset ensures that the updated harm estimates from the salient event enter the E3 stream at the beginning of a fresh cycle, not mid-cycle (which would produce partial integration artefacts). It is the mechanism by which completion events *reorganize the timing* of subsequent updates, not just inject a stronger signal.

In neuroscience: unexpected stimuli cause phase reset in theta and alpha oscillations (event-related potential P300 and its oscillatory basis). The reset is mediated by thalamic input that forces oscillator phase alignment.

**Implication for sequential plans:** In a multi-action plan W0→W1→W2, each waypoint completion phase-resets E3's clock. This means each sub-completion produces a coherent starting condition for the next planning cycle — harm estimates from W0→W1 are fully integrated before W1→W2 planning begins, even if E1/E2 were still processing.

---

<a id="mech-092"></a>
## Quiescent E3 heartbeat cycles trigger hippocampal SWR-equivalent replay (MECH-092)

**Claim Type:** mechanism_hypothesis
**Subject:** hippocampal.swr_equivalent_replay_during_heartbeat
**Status:** candidate
**Claim ID:** MECH-092

During quiescent E3 heartbeat cycles — periods when no new completion event or salient update is incoming — the hippocampal module performs *replay*: replaying compressed representations of recent trajectory experience to consolidate the viability map. This is the SWR (sharp-wave ripple) equivalent in the REE architecture.

Sharp-wave ripples in biological hippocampus occur during quiescent periods (rest, inter-trial intervals, slow-wave sleep) and replay compressed sequences (~10–20× faster than real time) for consolidation. They do not require external input — they are internally generated by CA3 recurrent dynamics.

**REE implication:** The hippocampal viability map (ARC-018) is not updated solely through online experience during active trajectories. It is also updated offline during quiescent E3 heartbeat cycles via replay. This means:

1. The map can consolidate trajectory experience that occurred too fast for E3's deliberative rate to fully integrate during execution.
2. ARC-018 (rollout viability mapping) may be testable in V3 by observing map improvement during explicitly modelled quiescent replay phases, not just during active rollout.
3. The failure of ARC-018 in V2 is partly explained by the absence of any replay mechanism — the viability map in CausalGridWorld updates only at each discrete step, with no quiescent consolidation phase.

**Connection to sleep architecture:** The sleep docs (`docs/architecture/sleep/`) describe offline consolidation. MECH-092 is the within-session, intra-action equivalent — the same replay machinery operating on shorter timescales during E3 heartbeat quiescence, not only during sleep.

---

<a id="mech-093"></a>
## z_beta modulates E3 heartbeat frequency (MECH-093)

**Claim Type:** mechanism_hypothesis
**Subject:** affective.z_beta_e3_heartbeat_rate_modulation
**Status:** candidate
**Claim ID:** MECH-093

The E3 heartbeat rate is not fixed. The affective latent z_beta modulates E3 update frequency: elevated harm salience (high z_beta arousal) increases E3 heartbeat rate (more frequent harm estimate refreshes); routine automated operation (low z_beta) decreases E3 heartbeat rate (more stable, less computationally expensive policy updates).

This is the neural analogue of arousal-modulated oscillation frequency: norepinephrine (NA) and acetylcholine (ACh) upregulate cortical and thalamic oscillation rates under high arousal, producing faster sampling and more frequent state updates. Under low arousal, oscillations slow and system enters more energy-efficient update regimes.

**REE implication:** z_beta is not only a precision-weighting signal (modulating *how much* each update matters) but also a rate-control signal (modulating *how often* updates occur). These are distinct contributions:
- Precision-weighting (existing, MECH-059): high z_beta → E3 prediction errors are upweighted
- Rate modulation (MECH-093): high z_beta → E3 heartbeat frequency increases → finer temporal resolution of harm attribution

**Predicted behaviour:** Under conditions of sustained high harm salience, the agent should exhibit faster control plane refresh and correspondingly more reactive (less stable) policy behaviour. Under routine conditions, policy stability increases. This connects the affective latent directly into the timing architecture, not only into the loss function.

**Connection to MECH-087 (four-plane hierarchy):** NA modulates perceptual sampling (MECH-084); ACh modulates encoding mode (MECH-083). MECH-093 adds: z_beta (the REE affective signal, corresponding primarily to NA arousal axis) modulates E3 heartbeat rate, placing it in the NA plane of the four-plane hierarchy as a rate-control rather than purely gain-control mechanism.

---

## SD-006: Asynchronous Multi-Rate Loop Implementation (V3-scoped)

**Type:** Design Decision
**Status:** held (V3)
**Registered:** 2026-03-15

V1 and V2 use synchronous single-timestep execution: all three loops update on the same discrete clock tick. This is architecturally incorrect for the heartbeat model and means ARC-023 through MECH-093 cannot be properly tested.

V3 must implement genuinely asynchronous multi-rate execution. Options:

1. **Separate threads with message-passing queues:** E1, E2, E3 run as independent threads; cross-loop communication via typed message queues with timestamped envelopes. E3 dequeues E1/E2 messages at its own heartbeat rate. Pros: clean separation. Cons: thread-safety complexity, GIL limitations in Python.

2. **Time-multiplexed execution with explicit loop-rate parameters:** Single execution loop with configurable update periods per module (e.g. `e1_steps_per_tick=1`, `e2_steps_per_tick=3`, `e3_steps_per_tick=10`). Simpler than threading; less faithful to true asynchrony.

3. **Hierarchical temporal abstraction (HTA):** Each loop operates on a different temporal grain explicitly represented in the architecture. E3 receives temporally-abstracted inputs (theta-cycle summaries, MECH-089) rather than raw E1/E2 outputs. Closest to the biological model; most faithful to cross-frequency coupling.

**Recommendation for V3:** HTA (option 3) co-designed with SD-004 (action objects) and SD-005 (z_self/z_world split). The temporal grain boundaries should align with the representational boundaries: E1 raw sensory → E2 action-object → E3 trajectory/harm are already distinct abstraction levels; each level's update rate should match its abstraction grain.

**Experiment implication:** Until SD-006 is implemented, any experiment testing ARC-023, MECH-089, MECH-090, MECH-091, MECH-092, or MECH-093 will produce null results by construction (the mechanism doesn't exist in the substrate). These claims are V3-scoped.
