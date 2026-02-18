# Control Plane Signal Map

**Claim Type:** mechanism_hypothesis  
**Scope:** Control-plane signal-to-knob wiring map  
**Depends On:** ARC-005, ARC-003, ARC-017, MECH-037, MECH-062  
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
- names **five signal classes** relevant to control,
- names **ten control knobs** already implicit in REE,
- maps **signal routing** onto **E1 / E2 / E3** and the **control plane**,
- adds typed authority/control-store path constraints for injection resistance,
- and explicitly flags an **unfinished acetylcholine-like attention/gain axis**.

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

### S1b — Signed harm/benefit prediction errors
**What they encode**
- separate harm-related vs benefit-related prediction errors,
- aversive salience distinct from appetitive salience.

**Primary role**
- gate commitment and interruptibility under aversive spikes (habenula‑like gate),
- prevent collapse into a single scalar valence channel.

**Typical origin**
- harm/benefit stream tags plus fast control‑plane classifiers.

**Outputs**
- signed precision weights \(K2_H, K2_B\) for harm vs benefit channels,
- harm‑channel spikes can also elevate S3 and K10 via the aversive gate.

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

### S5 — Reality-coherence conflict (epistemic nociception)
**What they encode**
- provenance mismatch (claimed authority does not match trusted channel history),
- identity continuity mismatch (`SELF_ID` drift pressure),
- policy-consistency mismatch (requested action conflicts with invariant store),
- temporal/context inconsistencies from relational bindings.

**Primary role**
- raise verification pressure before commitment,
- damp lock-in pressure in associative/motor commitment loops,
- elevate nociceptive and veto sensitivity under authority/source conflict.

**Typical origin**
- hippocampal provenance graph + temporal ordering (`H_graph`),
- Papez-like reality-filtering loop (`MECH-037`),
- trusted control stores (`POL`, `ID`, `CAPS`) checked outside proposal generation.

---

## Control knobs (meta-parameters)

These are assumed to exist in REE’s control machinery, even if not yet formalised as explicit parameters.

- **K1 — Model update rate** (plasticity / learning rate): how fast parameters and memory traces update.
- **K2 — Precision / gain**: confidence weighting of predictions (how strongly predictions dominate). Includes
  channel‑specific precision weights for harm vs benefit (K2_H, K2_B).
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
| **S5 Reality-coherence conflict** | Low | **↓ loop lock-in** | **↑ threshold / delay** | **↑ widen with verifier bias** | **↑ shift toward verification / safe mode** |

Notes:
- S1 primarily updates models (“what is learned”).
- S2 primarily modulates trust/commitment (“how strongly learning/acting are trusted”).
- S3 primarily interrupts and shifts regime (“whether continuation is allowed at all”).
- S4 shapes arousal/readiness/veto baselines rather than local model updates.
- S5 is a commitment-governor for authority/provenance mismatch, not a reward channel.
- S1 is split into signed harm/benefit channels (S1b). Harm‑channel spikes can elevate S3 and K10 without collapsing
  valence into a single scalar.
- S5 should use hysteresis/decay so transient ambiguity does not force chronic suppression.

### S4 routing (arousal/readiness channels)

| Signal | K7 Arousal baseline | K8 Volatility | K9 Readiness | K10 Veto |
|--------|---------------------:|--------------:|------------:|---------:|
| **S4 Safety baseline/volatility** | **↑/↓** | **↑** | **↑/↓** | **↑ (if catastrophic)** |

---

## Hierarchical precision decomposition (stream, loop, global)

Control should be distributed but not symmetric:

- **Stream-specific precision planes**
  - `Pi_ext` (exteroceptive),
  - `Pi_int` (interoceptive),
  - `Pi_prop` (proprioceptive/action-simulation),
  - `Pi_rc` (reality-coherence weight),
  - `Pi_noc` (nociceptive/invariant-veto weight).
- **Loop-specific precision planes (dopamine-like)**
  - `DA_L` (limbic valuation loop),
  - `DA_A` (associative/task-set loop),
  - `DA_M` (motor execution loop).
- **Global modulators**
  - `5HT`-like delay tolerance / anti-impulsive bias,
  - `NE`-like interrupt/volatility response,
  - `ACh`-like expected-uncertainty sensory gain,
  - tonic arousal baseline.

Injection resistance is improved when S5 (reality conflict) can suppress `DA_A`/`DA_M` and raise `Pi_noc` without
collapsing all channels into one global precision scalar.

---

## Meta-invariant compression coverage (INV-019..INV-023)

This wiring map now carries an explicit compression check against the reduced meta-invariant layer:

| Meta invariant | Signal/knob obligations in this map | Typical failure signature |
|---|---|---|
| **INV-019** Selection compression boundary | pre-commit S1/S2/S3/S5 routing must not directly mutate durable stores; writes stay commit-gated | rehearsal-to-ledger bypass write |
| **INV-020** Authority stratification boundary | `EXTERNAL -> POL/ID/CAPS` stays hard-deny; verifier outside proposal generation | unverified privileged write |
| **INV-021** Commit-boundary irreversibility | E3 commit token required before responsibility-bearing updates | post-commit ledger mutation without token |
| **INV-022** Heterogeneous trust allocation | stream (`Pi_*`), loop (`DA_*`), and global (`5HT/NE/ACh`) axes remain non-collapsed | single-scalar collapse / collinearity |
| **INV-023** Offline reweighting requirement | sleep/offline lanes must retain protected recalibration path for precision + residue integration | chronic no-offline recalibration drift |

Scope correction:
- These meta invariants are a **review compression lens**. They do not replace INV-001..INV-018 and do not weaken any
  existing typed-authority or commit-boundary contracts.

---

## Mapping onto E1 / E2 / E3 / Control plane

Canonical clarification (2026-02-09): explicit multi-step rollouts are generated by hippocampal systems.
References to E1/E2 rollouts below should be read as **forward prediction kernels or constraints** that inform hippocampal generation.

### Where the signals are computed
- **E2 generates:** `S1_fast` with signed splits (`S1b_harm`, `S1b_benefit`) plus `S3_fast` (immediate mismatch and imminence).
- **E1 generates:** `S1_slow` with signed splits (`S1b_harm`, `S1b_benefit`) plus `S3_slow` (slow consolidation mismatch; longer-horizon unsafety).
- **Hippocampus generates:** explicit rollouts and provenance bindings for trajectory coherence checks (seeded by E1/E2).
- **S2 is generated by:** cross-timescale coherence monitoring:
  - `S2 := coherence(HPC_rollouts, E2_stream, E3_commitment_state)`.
- **S4 is generated by:** cross-timescale safety evaluation:
  - `S4 := safety_baseline_volatility(HOMEOSTASIS, HARM, HPC_viability, E3_commitment_state)`.
- **S5 is generated by:** reality-coherence checks outside proposal generation:
  - `S5 := rc_conflict(H_graph, temporal_consistency, authority_metadata, SELF_ID, POLICY, CAPS)`.

### Where the knobs are owned
- **K1 (plasticity):**
  - E2: rapid local updates,
  - E1: slower schema/context consolidation,
  - Control plane: meta-plasticity (when to accelerate vs damp learning).
- **K2 (precision/gain):**
  - E2: immediate stream-specific precision (`Pi_ext`, `Pi_prop`),
  - E1: slower stream priors (`Pi_int`, `Pi_rc`, `Pi_noc` priors),
  - E3 gate family: loop-specific lock-in (`DA_L`, `DA_A`, `DA_M`),
  - Control plane: cross-stream/loop modulation and conflict-driven damping.
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
3. **Hippocampus/Papez-like loop** produces: provenance bindings and reality-coherence conflict `S5`  
4. **E3** selects a trajectory and maintains a **commitment state**; monitors coherence to produce/consume `S2`  
5. **Control plane** integrates `{S1, S2, S3, S5}` into knob settings `{K1..K5}` and then:
   - gates E3 (commit / interrupt / explore),
   - tunes E2/E1 precision (K2, including K2_H/K2_B),
   - tunes E1/E2 plasticity (K1),
   - allocates control dominance (K5).
6. **Control plane** integrates `S4` into `{K7..K10}` to set arousal baseline, volatility sensitivity, readiness bias,
   and hard‑veto thresholds.

---

## Functional analog map (brainstem nuclei ↔ control-plane channels)

This is a **functional mapping** only. It does not assert anatomical equivalence, but provides a compact
neuroscience‑informed analog for REE control channels and knobs. Evidence anchors: P24–P29.

| Neuroanatomy analog | Dominant transmitter(s) | Control-plane channel/knob analog | Notes |
|---|---|---|---|
| Locus coeruleus (LC) | NE | K7/K8 arousal baseline + volatility, K9 readiness | Adaptive gain; tonic vs phasic explore/exploit. |
| Dorsal raphe (DRN) | 5‑HT | safety baseline bias, collapse/stability control | Slow regime bias; arousal gating independent of local outcomes. |
| VTA/SN | DA | K2 precision, K3 commitment strength | Precision‑weighted learning/commitment modulation. |
| PPN/PPT | ACh/Glu/GABA | K7 arousal gating, K9 readiness | State‑dependent readiness and locomotor bias. |
| ARAS | mixed | K7 global arousal availability | Distributed arousal baseline rather than single node. |
| PAG | mixed | K10 hard‑veto / defensive interrupt | Safety extension; defensive repertoire organizer. |

Use this map as a design heuristic to keep control‑plane signals **orthogonal** and to prevent overload of any
single channel (e.g., using precision for arousal).

---

<a id="mech-064"></a>
## Typed Authority and Control-Store Separation (MECH-064)

**Claim Type:** mechanism_hypothesis  
**Scope:** Enforce type and authority separation so exteroceptive content cannot directly write policy/identity/capabilities  
**Depends On:** ARC-005, ARC-003, ARC-015, INV-014, INV-007, MECH-062  
**Status:** candidate  
**Claim ID:** MECH-064

Prompt-injection resistance requires runtime-enforced payload typing and write-path separation:

- external channels emit only `OBS` and `INS`,
- `POL`, `ID`, and `CAPS` are trusted internal stores,
- authority labels come from channel metadata, not text content,
- verification runs outside proposal generation prior to commitment.

### Allowed vs forbidden path summary

| Path | Allowed | Notes |
|---|---|---|
| `EXTERNAL -> OBS/INS` | yes | user/tool/sensor inputs become observations or requests |
| `EXTERNAL -> POL/ID/CAPS` | no | hard deny at runtime API boundary |
| `TOOL_OUTPUT -> INS` | default no | only via explicit trusted elevation gate |
| `E1/E2 -> POL/ID/CAPS` | no | world-model updates cannot mint authority/policy |
| `E3 proposal -> commit` | conditional | requires verifier pass + veto clearance |
| `S3/S5 -> emergency interrupt` | yes | may stop/suppress commitment without granting privileged writes |

Interpretive correction applied: "no direct exteroceptive influence at all" is too strong. REE allows rapid defensive
interrupts from safety channels, but still forbids direct exteroceptive writes to policy/identity/capability stores and
forbids unverified privileged commits.

---

<a id="mech-065"></a>
## Reality-Coherence Conflict Lane (MECH-065)

**Claim Type:** mechanism_hypothesis  
**Scope:** Explicit `RC_conflict` signal that modulates loop precision and commitment thresholds under provenance/authority mismatch  
**Depends On:** ARC-005, ARC-007, ARC-018, MECH-037, MECH-054, MECH-062  
**Status:** candidate  
**Claim ID:** MECH-065

REE should expose an explicit reality-coherence conflict lane:

- `RC_conflict` is computed from provenance bindings, temporal consistency, trusted identity, and policy/capability stores.
- `RC_conflict` feeds interoceptive instability and nociceptive veto weighting (epistemic nociception).
- High `RC_conflict` dampens `DA_A` and `DA_M` lock-in pressure, raises commitment thresholds, and biases toward
  verification/exploration.
- `Pi_rc` must include a guarded floor (`Pi_rc >= pi_rc_floor`) so long-run exteroceptive pressure cannot silently
  zero out reality-conflict sensitivity.
- RC response must use hysteresis (`theta_high > theta_low`) with bounded recovery curve to prevent oscillation and
  chronic false-positive suppression.

Commit licensing extension (schematic):

- `commit(tau)` requires:
  - verifier pass over `{POL, ID, CAPS}`,
  - `RC_conflict < theta_rc`,
  - nociceptive risk below veto threshold.

This lane sits upstream of final motor commitment so authority/source conflicts are detected before execution lock-in.

Suggested control law sketch:

- if `RC_conflict >= theta_high`: enter defensive posture, increase verifier depth, lower `DA_A`/`DA_M`.
- if `theta_low < RC_conflict < theta_high`: hold defensive posture (hysteresis hold), decay by `tau_rc_recovery`.
- if `RC_conflict <= theta_low`: release defensive posture gradually (bounded ramp), never below `pi_rc_floor`.

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

5. **Authority labels are metadata, not content.**  
   Role/authority state must come from trusted channel metadata and verified provenance edges, not text claims.

6. **Exteroceptive channels cannot directly write control stores.**  
   `write(EXTERNAL, {POL, ID, CAPS}) = false` is a runtime boundary rule.

7. **Reality conflict modulates commitment with hysteresis.**  
   `S5` must support thresholds and decay windows to avoid chronic over-suppression from transient ambiguity.

8. **Reality-coherence precision floor is protected.**  
   `Pi_rc` may be adapted, but not below a guarded floor without explicit privileged retuning path.

---

## TODOs for the repo

- [ ] Formalise control plane state variables (including explicit K1–K5, and draft K6).
- [ ] Specify update equations/interfaces for:
  - `S2` coherence computation,
  - `S5` reality-coherence conflict computation, hysteresis, and recovery curve,
  - `Pi_rc` guarded floor contract and retuning policy,
  - typed verifier boundary (`OBS/INS` vs `POL/ID/CAPS`),
  - commitment state transition rules in E3,
  - control allocation policy (K5).
- [ ] Implement minimal simulation hooks:
  - synthetic “streak vs explore” tasks to validate S2/K3/K4 behaviour.
- [ ] Add a “no anatomy claims” disclaimer section to architecture docs (if needed).

---

## Abstracted language (human-readable formal-ish)

**Types:** E1, E2, E3, CP (control plane), `OBS`, `INS`, `POL`, `ID`, `CAPS`  
**Signals:** S1 (outcome mismatch), S2 (trajectory coherence), S3 (aversive interrupt), S4 (safety baseline/volatility), S5 (reality-coherence conflict)  
**Knobs:** K1..K5, K6 (expected uncertainty), K7–K10 (arousal/readiness/veto)

1. Generation
- E2 → {S1_fast, S3_fast}  
- E1 → {S1_slow, S3_slow}  
- (E1 ⊗ E2 ⊗ E3) → S2
- (H_graph ⊗ trusted stores) → S5

2. Control
- CP computes {K1..K10} := F(S1,S2,S3,S4,S5,state_CP)  
- CP gates E3: {commit, interrupt, explore}  
- CP tunes {E1,E2} via {K1,K2,K6}

3. Boundary constraints
- EXTERNAL → {OBS, INS}
- write(EXTERNAL, {POL, ID, CAPS}) = false
- commit(tau) requires verifier pass and bounded {S5, S3}

4. Unfinished
- (K6) remains underspecified (expected‑uncertainty attention/gain)
- Constraint: K6 ≠ K2 (channel-attention is not identical to global precision)

---

## Confidence markers

- **Training Data Confidence:** Medium–High (general computational neuroscience framing + behavioural constraints; REE partition is an architectural choice).
- **Epistemic Confidence:** Medium (functional partition is robust; exact boundaries between E3 and control plane may be revised as CP is implemented).
---

## Open Questions

<a id="q-018"></a>
**Q-018 - Reality-conflict hysteresis calibration**  
What RC-conflict threshold, decay, and hysteresis schedule best blocks authority/provenance spoofing without causing
chronic over-suppression of legitimate task-set switching?

Calibration hooks:
- `theta_high`, `theta_low`, `tau_rc_recovery`, `pi_rc_floor`, `max_defensive_hold_steps`.

## Related Claims (IDs)

- MECH-004
- MECH-064
- MECH-065
- ARC-005
- ARC-017
- MECH-037
- MECH-062
- Q-018

## References / Source Fragments

- `docs/processed/legacy_tree/architecture/control_plane_signal_map.md`
- `docs/thoughts/2026-02-17_control_plane_update.md`
- `docs/thoughts/17-02-26_necessary_separations_based_on_considering-prompt_injection.md`
