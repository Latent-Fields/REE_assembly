# Thought Intake: Phase Segregation — Perception vs Imagination on Shared Substrate

**Date:** 2026-04-07
**Raw thought:** docs/thoughts/2026-04-07_phase_segregation_perception_imagination.md
**Claims registered:** (none yet — candidates below)

---

## Source and epistemic status

Daniel Golden's original insight, refined through ChatGPT dialogue. Core idea: direction of information flow through the shared E1/E2 substrate, combined with phase-of-firing segregation and precision weighting, determines whether a world-model instantiation is experienced as perception or imagination. Ephaptic (field-level) coupling proposed as the biophysical mechanism enforcing or disrupting phase segregation.

Epistemic confidence: moderate. The framework integrates established predictive processing, oscillatory phase coding, and ephaptic coupling literatures, but the specific synthesis (phase segregation as the perception/imagination boundary, ephaptic coupling as the enforcement mechanism) is novel and not yet experimentally validated.

---

## Core thesis

The brain does not separate perception and imagination by substrate, but by **phase-structured, precision-weighted routing of shared representational machinery** (E1 + E2).

- **Perception:** bottom-up prediction error dominates; top-down predictions and bottom-up error are phase-aligned within the same channel; high sensory precision; high verisimilitude.
- **Imagination / simulation:** top-down predictions dominate; run in phase-offset channels decoupled from sensory error; lower verisimilitude.
- **Hallucination (failure mode):** top-down signals invade the sensory phase channel with high precision; treated as real despite absent input.

Verisimilitude = phase-aligned coherence between ascending and descending signals on the same carrier.

---

## Key mechanisms

### Phase multiplexing on shared substrate

Same E1/E2 neurons participate in multiple representational streams, disambiguated by phase-of-firing relative to oscillatory carriers:

| Carrier | Role |
|---|---|
| Gamma (gamma) | Local binding (E1 content) |
| Theta (theta) | Sequencing / hippocampal rollout (E3-hippocampus loop) |
| Beta (beta) | Stabilised action / commitment bias |
| Delta (delta) | Global state / mode |

Phase offsets + cross-frequency coupling separate concurrent streams without separate circuits.

### Hippocampal simulations as phase-shifted reality proposals

Hippocampus generates theta-sequenced candidate futures, phase-offset from sensory channels. E3 evaluates them. If phase separation maintained: experienced as imagination. If phase separation collapses: experienced as perception / "this is happening."

### Ephaptic coupling as enforcement mechanism

Field-level (non-synaptic) electrical interactions between neurons:
- Enforce phase segregation (normal function)
- Disrupt phase segregation (pathological: hallucination, psychosis)
- Modulate large-scale synchronisation shifts (state changes: sleep, dreaming)

Bridges micro (neurons) / meso (oscillations) / macro (subjective experience).

### Sleep mapping

| State | Phase regime | Function |
|---|---|---|
| Wake | Mixed precision, partial coupling | Constrained simulation |
| NREM | Strong global delta synchrony | Reorganisation of priors (E1 updating) |
| REM | Decoupled sensory precision + active theta/gamma | Simulation borrowing sensory phase format = vivid internally generated "perception" |

---

## Temporal convergence: "subjective now" as the meeting point

Daniel's follow-up insight (same session): Both E1 perceptual predictions and hippocampal trajectory proposals are predictions *of the future*. Their coupled convergence — the point where the predicted sensory state and the planned trajectory state agree — defines **subjective now**.

This has three consequences:

### 1. Subjective now is ahead of real-time sensory input

"Subjective now" is not when sensory data arrives — it is where perceptual prediction and hippocampal plan converge. This convergence point sits slightly in the future relative to raw sensory processing, which provides the temporal buffer needed for motor commands to be issued from subjective-now and arrive at effectors in time to act on real-time-now. The perceptual lag is not a bug — it is the architecture ensuring that action decisions are made at a temporal offset that compensates for motor execution delay.

### 2. Plan origins emerge from convergence search

The convergence between E1 prediction and hippocampal rollout is a search process. Where the two streams first agree is where plans can "spring from" — it identifies the earliest future state from which a coherent action sequence is available. This means plan initiation is not arbitrary; it is anchored to the point where the world model and the trajectory proposal first become mutually consistent.

### 3. Retroactive causal inference via backward rollout

If hippocampal rollouts can start from states *earlier* than subjective-now and trace causal chains that converge on the current sensory-predicted state, then the system can test possible pasts — "what sequence of events could have produced what I'm perceiving now?" This is retroactive causal inference: the hippocampus proposes candidate histories, and the ones whose causal chains converge on subjective-now-plus-a-little-ahead are accepted as plausible explanations of the present.

This connects to:
- **SD-003** (self-attribution via counterfactual E2): backward rollouts with a_actual vs a_cf test "did *I* cause this?"
- **MECH-094** (hypothesis tag): backward rollouts must carry the simulation tag — they are hypothetical pasts, not memories
- **INV-049** (sleep): offline, without the sensory anchor, backward rollouts could run unconstrained — this is what episodic replay during sleep may actually be doing

---

## Candidate claim derivations

### Candidate: Phase segregation as perception/imagination boundary

The same E1/E2 substrate produces perception or imagination depending on precision-weighted routing and phase-of-firing segregation. Verisimilitude = phase-aligned coherence. This is a mechanistic refinement of MECH-094 (hypothesis tag as write gate) — the phase channel IS the tag at the biophysical level.

**Connects to:** MECH-094 (hypothesis tag), ARC-023 (thalamic heartbeat rates), MECH-089 (cross-frequency coupling), INV-049 (sleep as mathematical necessity for model-building agents), INV-062 (dream phenomenology).

### Candidate: Ephaptic coupling as phase-segregation enforcement

Non-synaptic field effects maintain or disrupt the phase boundaries that separate perception from simulation. This provides the biophysical grounding for why phase segregation fails in specific pathological states (psychosis, hallucination, dissociation).

**Connects to:** Clinical atlas (hallucination, intrusive imagery, rumination, dream phenomenology, dissociation).

### Candidate: Subjective now as perceptual-hippocampal convergence point

"Subjective now" is defined by the temporal convergence of E1 perceptual prediction and hippocampal trajectory proposal — not by raw sensory arrival time. This convergence sits ahead of real-time input, providing the motor execution buffer. Plan origins are anchored to where the two streams first agree. Backward hippocampal rollouts that converge on subjective-now constitute retroactive causal inference (testing possible pasts).

**Connects to:** SD-003 (counterfactual self-attribution — backward rollouts with a_actual vs a_cf), MECH-094 (hypothesis tag on backward rollouts), INV-049 (unconstrained backward rollouts during sleep = episodic replay), existing perceptual lag literature (~80-200ms).

### Candidate: Hallucination as phase-channel invasion

Top-down predictions with high precision invade the sensory phase channel, bypassing the normal phase-offset that marks content as simulated. This is not a content error but a routing/tagging error — the same content is experienced as real because it occupies the wrong phase channel.

**Connects to:** MECH-094 (tag loss = psychosis mechanism), clinical atlas.

---

## REE implementation implications

1. **Phase-channel tag** on representations in latent stack — marks content as sensory-anchored vs simulated
2. **Precision assignment per channel** — control plane parameter
3. **Cross-channel leakage** as a modellable failure mode — provides unified mechanism for hallucination, intrusive imagery, rumination, dissociation
4. REM dreaming = simulation running in sensory phase format (connects to INV-062 Type 1/2 phenomenology)

---

## Relationship to existing claims

- **MECH-094** (hypothesis tag): Phase channel may BE the biophysical implementation of the hypothesis tag. The categorical phi(z) write gate is phase-segregated routing.
- **MECH-089** (cross-frequency coupling): Theta-gamma nesting is one instance of the broader phase-multiplexing scheme described here.
- **ARC-023** (thalamic heartbeat): Thalamic pacing sets the carrier frequencies that define the phase channels.
- **INV-049** (sleep necessity): Sleep state changes are large-scale phase-regime transitions.
- **INV-062** (dream phenomenology): REM dreaming = simulation borrowing sensory phase format. Type 3 dreams may reflect delta-dominated phase regime (NREM consolidation).
