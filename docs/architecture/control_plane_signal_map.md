# Control Plane Signal Map

**Claim Type:** mechanism_hypothesis  
**Scope:** Control-plane signal-to-knob wiring map  
**Depends On:** ARC-005, ARC-003  
**Status:** candidate  
**Claim ID:** MECH-004
<a id="mech-004"></a>

---

Source: `docs/processed/legacy_tree/architecture/control_plane_signal_map.md`

# Control Plane Signal→Knob Wiring Map (E1/E2/E3)

> **Status:** Draft / architectural note  
> **Scope:** Functional wiring (computational roles), not anatomical claims  
> **Repo placement suggestion:** `docs/architecture/control_plane_signal_knob_map.md`

## Why this file exists

REE appears to already contain the right *parts* (multi-timescale prediction, memory, regime control, trajectory selection), but the **causal wiring** between signals and control parameters (“knobs”) has been under-specified.

This note:
- names **three signal classes** relevant to control,
- names **five control knobs** already implicit in REE,
- maps **signal routing** onto **E1 / E2 / E3** and the **control plane**,
- explicitly flags an **unfinished acetylcholine-like attention/gain axis**.

---

## Terms

### E1 / E2 / E3 (recap)
- **E1** — deep / slow generative predictor (long-horizon modelling, schema/context integration).
- **E2** — fast / near-horizon predictor (immediate prediction, affordance generation, quick mismatches).
- **E3** — trajectory selector + commitment operator (selects a path/policy; maintains commitment state).
- **Control plane** — modulatory stack that (a) integrates control-relevant signals and (b) sets meta-parameters:
  precision/gain, plasticity, exploration pressure, commitment interruptibility, control allocation.

> This is a *functional* partition. Anatomical mappings (prefrontal cortex, basal ganglia, hippocampus, monoamines, etc.) are intentionally not asserted here.

---

## Control-relevant signal classes

### S1 — Outcome-linked prediction signals
**What they encode**
- prediction mismatch (better/worse/different than expected),
- outcome magnitude and timing,
- surprise relative to local model.

**Primary role**
- update internal models and memories (“error for learning”).

**Typical origin**
- fast versions: **E2** and sensorimotor micro-predictors,
- slower consolidation: **E1**.

---

### S2 — Trajectory-stability signals
**What they encode**
- whether a policy/path is holding together over time,
- coherence of predictions across multiple steps,
- streak viability vs volatility/drift.

**Primary role**
- determine how strongly to keep trusting the current path (“commitment viability”).

**Typical origin**
- cross-timescale interaction **E1 ↔ E2** (stability is inherently cross-horizon),
- monitoring within **E3** (did the selected path remain coherent?).

---

### S3 — Aversive / interruptive prediction signals
**What they encode**
- anticipated harm, instability, or unsafety,
- rising uncertainty that demands interruption,
- “stop trusting continuing like this” signals.

**Primary role**
- break commitment, suppress precision, widen search, and/or escalate control.

**Typical origin**
- fast imminence: **E2**,
- slower path-unsafety forecasts: **E1**,
- actioned via **control plane → E3 gating**, plus **control plane → E2 precision suppression**.

> **Asymmetry principle:** S3 is *not* simply “negative reward.” It has privileged access to commitment-breaking and regime-shift mechanisms.

---

### S4 — Safety baseline and volatility (arousal drivers)
**What they encode**
- baseline safety: whether core viability is within bounds (tonic),
- safety volatility: how rapidly safety is changing (phasic),
- rapid hazard change vs stable safe state.

**Primary role**
- set arousal baseline and volatility sensitivity,
- bias readiness and interrupt thresholds.

**Typical origin**
- cross-timescale evaluation of HOMEOSTASIS/HARM streams (E1 + E2),
- augmented by hippocampal path viability signals and E3 commitment state.

---

## Control knobs (meta-parameters)

These are assumed to exist in REE’s control machinery, even if not yet formalised as explicit parameters.

- **K1 — Model update rate** (plasticity / learning rate): how fast parameters and memory traces update.
- **K2 — Precision / gain**: confidence weighting of predictions (how strongly predictions dominate).
- **K3 — Commitment depth**: how long a selected trajectory/policy is held; resistance to switching.
- **K4 — Exploration pressure**: breadth of policy sampling; willingness to deviate.
- **K5 — Control allocation**: which loop dominates (fast habitual vs slower deliberative), escalation policy.
- **K6 — Expected uncertainty / channel-specific gain (acetylcholine-like)**: attention and cue‑validity weighting.
- **K7 — Arousal baseline**: tonic availability and throughput.
- **K8 — Unexpected uncertainty / volatility sensitivity (noradrenaline-like)**: phasic change tracking and interrupt bias.
- **K9 — Action readiness**: motor gating bias and readiness-to-act.
- **K10 — Hard veto threshold**: catastrophic interrupt trigger.

---

## Signal → knob influence (functional table)

| Signal class | K1 Update | K2 Precision/Gain | K3 Commitment | K4 Exploration | K5 Control allocation |
|-------------|----------:|------------------:|--------------:|---------------:|----------------------:|
| **S1 Outcome-linked** | **High** | Medium (local) | Low–Medium | Low | Low |
| **S2 Trajectory-stability** | Medium | **High** | **High** | Medium | Medium |
| **S3 Aversive/interruptive** | Low–Medium | **↓ suppress** | **↓ break** | **↑ widen** | **↑ escalate** |

Notes:
- S1 primarily updates models (“what is learned”).
- S2 primarily modulates trust/commitment (“how strongly learning/acting are trusted”).
- S3 primarily interrupts and shifts regime (“whether continuation is allowed at all”).
- S4 shapes arousal/readiness/veto baselines rather than local model updates.

### S4 routing (arousal/readiness channels)

| Signal | K7 Arousal baseline | K8 Volatility | K9 Readiness | K10 Veto |
|--------|---------------------:|--------------:|------------:|---------:|
| **S4 Safety baseline/volatility** | **↑/↓** | **↑** | **↑/↓** | **↑ (if catastrophic)** |

---

## Mapping onto E1 / E2 / E3 / Control plane

Canonical clarification (2026-02-09): explicit multi-step rollouts are generated by hippocampal systems.
References to E1/E2 rollouts below should be read as **forward prediction kernels or constraints** that inform hippocampal generation.

### Where the signals are computed
- **E2 generates:** `S1_fast`, `S3_fast` (immediate mismatch and imminence).
- **E1 generates:** `S1_slow`, `S3_slow` (slow consolidation mismatch; longer-horizon unsafety).
- **Hippocampus generates:** explicit rollouts for trajectory coherence checks (seeded by E1/E2).
- **S2 is generated by:** cross-timescale coherence monitoring:
  - `S2 := coherence(HPC_rollouts, E2_stream, E3_commitment_state)`.
- **S4 is generated by:** cross-timescale safety evaluation:
  - `S4 := safety_baseline_volatility(HOMEOSTASIS, HARM, HPC_viability, E3_commitment_state)`.

### Where the knobs are owned
- **K1 (plasticity):**
  - E2: rapid local updates,
  - E1: slower schema/context consolidation,
  - Control plane: meta-plasticity (when to accelerate vs damp learning).
- **K2 (precision/gain):**
  - E2: immediate sensory/action precision,
  - E1: slower precision priors,
  - Control plane: global + channel-specific gain setting.
- **K3 (commitment depth):**
  - E3: primary owner (commitment is E3’s job),
  - Control plane: sets interrupt thresholds and stickiness policies.
- **K4 (exploration pressure):**
  - E3: selects exploit vs explore for the current window,
  - Control plane: biases exploration baseline (fatigue/stress/uncertainty/novelty context),
  - E2: implements exploration via action proposal diversification,
  - E1: supplies alternative roll-outs and constraints.
- **K5 (control allocation):**
  - Control plane: primary owner (escalate to deliberation vs handoff to habit; pause/freeze/defer),
  - E3: executes within the allocated control budget.
- **K7–K10 (arousal/readiness/veto):**
  - Control plane: primary owner (tonic baseline, phasic volatility, readiness bias, veto threshold),
  - E3: consumes readiness/veto settings for commitment and interrupt decisions.

### Routing summary (textual diagram)

1. **E2** produces: fast predictions + `S1_fast` + `S3_fast`  
2. **E1** produces: slow roll-outs + `S1_slow` + `S3_slow`  
3. **E3** selects a trajectory and maintains a **commitment state**; monitors coherence to produce/consume `S2`  
4. **Control plane** integrates `{S1, S2, S3}` into knob settings `{K1..K5}` and then:
   - gates E3 (commit / interrupt / explore),
   - tunes E2/E1 precision (K2),
   - tunes E1/E2 plasticity (K1),
   - allocates control dominance (K5).
5. **Control plane** integrates `S4` into `{K7..K10}` to set arousal baseline, volatility sensitivity, readiness bias,
   and hard‑veto thresholds.

---

## Functional analog map (brainstem nuclei ↔ control-plane channels)

This is a **functional mapping** only. It does not assert anatomical equivalence, but provides a compact
neuroscience‑informed analog for REE control channels and knobs. Evidence anchors live in
`docs/notes/evidence_map.md` (P24–P29).

| Neuroanatomy analog | Dominant transmitter(s) | Control-plane channel/knob analog | Notes |
|---|---|---|---|
| Locus coeruleus (LC) | NE | K7/K8 arousal baseline + volatility, K9 readiness | Adaptive gain; tonic vs phasic explore/exploit. |
| Dorsal raphe (DRN) | 5‑HT | safety baseline bias, collapse/stability control | Slow regime bias; arousal gating independent of local outcomes. |
| VTA/SN | DA | K2 precision, K3 commitment strength | Precision‑weighted learning/commitment modulation. |
| PPN/PPT | ACh/Glu/GABA | K7 arousal gating, K9 readiness | State‑dependent readiness and locomotor bias. |
| ARAS | mixed | K7 global arousal availability | Distributed arousal baseline rather than single node. |
| PAG (P28) | mixed | K10 hard‑veto / defensive interrupt | Safety extension; defensive repertoire organizer. |

Use this map as a design heuristic to keep control‑plane signals **orthogonal** and to prevent overload of any
single channel (e.g., using precision for arousal).

---

## Unfinished / underspecified: acetylcholine-like attention/gain axis

REE currently risks letting **K2 (precision/gain)** do too much work. A distinct axis is required for **expected
uncertainty (acetylcholine-like)**, separate from **unexpected uncertainty (noradrenaline-like)**.

### Proposed additional control parameter (draft)
- **K6 — Expected uncertainty / channel-specific gain (acetylcholine-like)**

**What it modulates**
- selective attention,
- cue validity weighting,
- expected uncertainty handling (separable from NE‑like surprise),
- sensory vs associative emphasis,
- “how much to learn from this channel” without necessarily changing global commitment.

**Where it sits**
- Control plane with channel-specific projections into E2 (and slower priors in E1).

**Why it matters**
It separates:
- “I should attend more / sample better” (K6),
from
- “I should stop trusting this plan” (S3 → K3/K2),
and
- “my outcome was surprising” (S1 → K1).

> **Action item:** keep K6 explicitly marked “unfinished” until REE’s control plane is formalised.

---

## Design constraints implied by this wiring

1. **Learning rules are state-dependent.**  
   Control parameters (K1–K5, and K6) vary with latent regime state; they are not fixed hyperparameters.

2. **Aversive signals are privileged interrupters.**  
   S3 has direct access to commitment-breaking and precision suppression, not merely to value decrement.

3. **Trajectory stability is cross-timescale.**  
   S2 necessarily references multiple horizons; it cannot be computed purely within E2.

4. **Expected vs unexpected uncertainty are distinct.**  
   ACh‑like expected‑uncertainty (K6) should not be conflated with NE‑like surprise/interrupt (K8).

---

## TODOs for the repo

- [ ] Formalise control plane state variables (including explicit K1–K5, and draft K6).
- [ ] Specify update equations/interfaces for:
  - `S2` coherence computation,
  - commitment state transition rules in E3,
  - control allocation policy (K5).
- [ ] Implement minimal simulation hooks:
  - synthetic “streak vs explore” tasks to validate S2/K3/K4 behaviour.
- [ ] Add a “no anatomy claims” disclaimer section to architecture docs (if needed).

---

## Abstracted language (human-readable formal-ish)

**Types:** E1, E2, E3, CP (control plane)  
**Signals:** S1 (outcome mismatch), S2 (trajectory coherence), S3 (aversive interrupt), S4 (safety baseline/volatility)  
**Knobs:** K1..K5, K6 (expected uncertainty), K7–K10 (arousal/readiness/veto)

1. Generation
- E2 → {S1_fast, S3_fast}  
- E1 → {S1_slow, S3_slow}  
- (E1 ⊗ E2 ⊗ E3) → S2

2. Control
- CP computes {K1..K10} := F(S1,S2,S3,S4,state_CP)  
- CP gates E3: {commit, interrupt, explore}  
- CP tunes {E1,E2} via {K1,K2,K6}

3. Unfinished
- (K6) remains underspecified (expected‑uncertainty attention/gain)
- Constraint: K6 ≠ K2 (channel-attention is not identical to global precision)

---

## Confidence markers

- **Training Data Confidence:** Medium–High (general computational neuroscience framing + behavioural constraints; REE partition is an architectural choice).
- **Epistemic Confidence:** Medium (functional partition is robust; exact boundaries between E3 and control plane may be revised as CP is implemented).
---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- MECH-004

## References / Source Fragments

- `docs/processed/legacy_tree/architecture/control_plane_signal_map.md`
