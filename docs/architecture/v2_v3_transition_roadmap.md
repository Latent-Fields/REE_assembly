---
nav_exclude: true
---

# V2 → V3 Transition Roadmap

**Created:** 2026-03-14
**Status:** Living document — update after each major V2 experiment batch

---

## Purpose

This document defines:
1. What V2 can and cannot usefully test
2. The transition criteria — when to stop V2 and pause for roadmap redraw
3. What V3 must be architecturally capable of
4. V3 experiment targets mapped to open claims and design decisions

---

## V2 Experiment Plan (Complete Picture)

| ID | Claim | Status |
|---|---|---|
| EXQ-014 | MECH-059 V2 parity | **PASS** |
| EXQ-015 | MECH-056 V2 parity | **PASS** |
| EXQ-016 | MECH-060 V2 parity | **PASS** |
| EXQ-017 | MECH-061 V2 parity | **PASS** |
| EXQ-018 | SD-003 prereq (CausalGridWorld baseline) | **PASS** |
| EXQ-019 | MECH-033 kernel chaining | **FAIL** |
| EXQ-020 | ARC-007 path memory ablation | **FAIL** |
| EXQ-021 | ARC-018 rollout viability | **FAIL** |
| EXQ-022 | Q-007 valence correlation | **FAIL** |
| EXQ-023 | MECH-058 E1/E2 terrain timescale | **FAIL** |
| EXQ-024 | MECH-057a action-loop completion gate | **PASS** (heartbeat reframing; see MECH-090) |
| EXQ-025 | MECH-057 attribution completion gating | **FAIL** |
| EXQ-026 | MECH-025 action-doing mode probe | **FAIL** |
| EXQ-027 | MECH-071 E2 attribution calibration (SD-003) | **FAIL** (wrong module; E3 should predict harm) |
| EXQ-028 | MECH-072 selective residue attribution (SD-003) | **FAIL** confirmed — MECH-072 requires SD-005 substrate (same root cause as EXQ-027) |

**V2 experiment series closed after EXQ-028.** All three hard-stop criteria triggered.
Governance cycle completed 2026-03-19: 7 decisions applied, V3-pending gate lifted,
ARC-024 and SD-010 registered. V3 transition executed.

---

## What V2 Can Test

**Structural separation** (architectural — substrate-independent):
- MECH-059: E1 precision and E3 confidence are independent signals ✓
- MECH-056: residue accumulates along trajectory, not only at endpoint ✓
- MECH-060: write-locus separation between pre/post-commit channels ✓
- MECH-061: commit boundary correctly separates error channels ✓

**Qualitative three-loop structure** (ARC-021):
- Does the agent have three functionally distinct components (E1, E2, E3)?
- Do they receive different effective error signals?
- V2 can show qualitative separation; quantitative incommensurability needs SD-005

**First-approximation self-attribution** (SD-003):
- MECH-071: does E2.predict_harm calibrate higher for agent-caused harm?
  (relies on contamination visible in z_gamma — possible but noisy due to conflation)
- MECH-072: does foreseeable-harm gating reduce false attribution?
  (limited by same conflation)

**E2 as transition model** (MECH-070 partial):
- Does E2 learn motor-sensory transitions that differ from E1's sensory predictions?
- Can only be tested approximately in V2 — z_gamma mixes self and world effects

---

## What V2 Cannot Meaningfully Test

These are the V3 motivating failures:

### 1. Self/World Latent Separation (SD-005)
V2 z_gamma conflates proprioceptive/interoceptive self-state with exteroceptive world-state.
This means:
- Motor-sensory error (E2) and world-consequence error (E3) cannot be cleanly isolated
- Residue accumulation cannot distinguish "my body state changed" from "I changed the world"
- The full SD-003 causal attribution (world_delta vs self_delta) cannot be computed
- MECH-069 incommensurability cannot be demonstrated precisely — only approximated

**Symptom to watch:** If EXQ-027 shows weak calibration_gap (E2 barely discriminates
agent-caused harm from env-caused harm), the self/world conflation is the likely reason.

### 2. Action Object Planning Horizon (SD-004)
The hippocampal map currently navigates raw z_gamma state space. This caps the effective
planning horizon because CEM must operate at full latent dimensionality.
- Cannot test whether action-object space navigation extends horizon (SD-004 claim)
- Cannot test MECH-070's stronger form: E2's horizon exceeds E1's because E2 operates in
  compressed world-effect space

**Symptom to watch:** If ARC-018 (rollout viability mapping) continues to FAIL, the V2
hippocampal map is not navigating effectively — this is an SD-004 substrate problem.
ARC-007 (path memory ablation) also fails for the same reason: the V2 proxy (26-element
obs-vector slice) cannot represent structured path memory — a proper hippocampal module
navigating action-object space (SD-004) is required before ARC-007 is testable.

### 3. Three-Loop Credit Isolation (ARC-021 full form)
V2 can show the three components exist but cannot show that mixing their error signals is
harmful — because z_gamma makes the signals partially correlated anyway. The experiment to
demonstrate incommensurability requires clean signal separation, which needs SD-005.

### 4. Full Counterfactual Attribution (SD-003 V3)
The V3 SD-003 would compute:
```
world_delta = ||E2_world(z_world, a_actual) - E2_world(z_world, a_cf)||
```
This requires z_world to exist as a separate channel. In V2 there is only z_gamma.

**EXQ-027 architectural finding (2026-03-16):** The V2 SD-003 experiment (EXQ-027) placed
`predict_harm` on E2 directly. This is architecturally wrong per MECH-069: harm prediction
is E3's domain (trains on harm/goal error), not E2's (trains on motor-sensory error). E2's
`predict_harm` head received only indirect, noisy supervision — explaining the near-zero
calibration_gap (-0.004) across all seeds, indistinguishable from untrained RANDOM condition.

**Consequence for V3 SD-003 design:** Attribution is a joint E2+E3 computation:
1. E2 provides dynamics: `z_{t+1}_actual = E2(z_world, a_actual)` and `z_{t+1}_cf = E2(z_world, a_cf)`
2. E3 evaluates harm of each projected state: `harm_actual = E3(z_{t+1}_actual)`, `harm_cf = E3(z_{t+1}_cf)`
3. Causal signature = `harm_actual − harm_cf`

V3-EXQ-002 should be redesigned accordingly — it must test the E2+E3 joint pipeline,
not `E2.predict_harm` alone.

### 6. Dynamic Precision Regime and Behavioral Mode Switching (ARC-016)
V2 precision is hardcoded (0.5). ARC-016 requires precision to be dynamically calibrated
from E3's own prediction error and to gate commitment in a way that produces distinct
behavioral outcomes. The V2 experiment (precision_regime_probe) showed that even with
100% commit rate vs 0% commit rate, harm is identical — meaning commitment is not connected
to action-selection in a way that changes outcomes. Two distinct V3 requirements:
- **E3-derived dynamic precision**: precision must be computed from E3 prediction error,
  not externally imposed; must vary as the agent's confidence in harm predictions varies
- **End-to-end behavioral circuit**: precision → commitment threshold → action selection →
  harm must be genuinely wired; different precision regimes must produce measurably
  different harm profiles. Note: MECH-059 (structural separation of precision from PE)
  PASSED in V2, confirming the channels exist; ARC-016 requires those channels to produce
  behaviorally distinct operating modes — the wiring gap is in the commitment→behavior link.

### 5. Valenced Hippocampal Map Geometry (Q-020)
The NC-01–NC-09 cluster (registered 2026-03-15) raises the question of whether valence is
intrinsic to hippocampal map geometry (MECH-073) or externally applied by a downstream
comparator (ARC-007 strict). V2 cannot resolve this because:
- V2's HippocampalModule does not have enough geometric richness for rollout weights to
  reflect map-geometry valence separately from E3 scoring
- z_gamma conflation means any apparent valence-in-rollouts could be an E2 artifact

**Key insight (2026-03-15):** the Q-020 conflict may dissolve under SD-005. Once z_gamma is
split into z_self and z_world:
- z_self (E2 domain): ARC-007's "no value computation" constraint applies cleanly
- z_world (E3/Hippocampus/ResidueField domain): this space is inherently value-laden via the
  residue field — MECH-073 may simply be re-stating ARC-013 applied to z_world specifically
If this is right, Q-020 is not a genuine conflict but an artifact of the unsplit z_gamma — the
hippocampal map *is* z_world, which *is* the residue field's domain. Valence lives in z_world
structure, not in hippocampal computation. ARC-007 is vindicated and MECH-073 is reframed.
This hypothesis cannot be confirmed until SD-005 exists.

---

## V2 "Done" Criteria — Transition Triggers

> **All three hard stops triggered. V2→V3 transition executed (2026-03-19).** This
> section is historical. Active V3 roadmap in `docs/roadmap.md` §REE-v3.

**The V2 series is complete when EXQ-028 finishes.** At that point, evaluate:

### Hard stops (any one of these → pause for V3 design):
1. **EXQ-027 FAIL** — E2 cannot discriminate agent-caused from env-caused harm in z_gamma.
   This means the full SD-003 attribution requires SD-005 substrate. No further V2
   self-attribution experiments will be informative.

2. **Persistent MECH-058 FAIL** (EXQ-023) — E1/E2 timescale separation is not demonstrable
   in V2. This strongly suggests the self/world split (SD-005) is needed to cleanly separate
   their error signals.

3. **ARC-018 FAIL** (EXQ-021) — Rollout viability mapping fails. Hippocampal map cannot
   navigate effectively without action-object space (SD-004). V3 substrate needed before
   further hippocampal experiments.

### Soft stops (accumulation of these → assess V3 readiness):
- More than 5 FAIL experiments from the same architectural root cause (SD-004 or SD-005)
- EXQ-027 PASS but calibration_gap < 0.10 (weak — V3 needed for strong test)
- EXQ-028 PASS but false_attribution reduction < 10% (marginal — SD-005 needed for real test)

### Continue V2 if:
- EXQ-027 PASS with calibration_gap > 0.15 (E2 is discriminating well in z_gamma)
  → design additional SD-003 experiments before V3
- Multiple unexpected PASSes from FAIL-list experiments → investigate why before V3

---

## V3 Architectural Prerequisites

V3 requires both SD-004 and SD-005 to be implemented together — they co-evolve:

| SD | What changes | Why needed |
|---|---|---|
| **SD-004** | E2 → `f(z_t, a_t) → (z_{t+1}, o_t)` (action objects); Hippocampus navigates action-object space | Longer planning horizon; compressed world-effect encoding |
| **SD-005** | z_gamma → z_self + z_world; E2 on z_self; E3/Hippocampus on z_world | Clean motor-sensory vs world-consequence separation; correct residue substrate |
| **SD-006** | Asynchronous multi-rate loop execution: E1/E2/E3 run at characteristic heartbeat rates (ARC-023), not synchronous single-timestep | Required for heartbeat architecture (ARC-023), cross-frequency coupling (MECH-089), beta-gated policy propagation (MECH-090), phase reset (MECH-091), SWR replay (MECH-092), z_beta rate modulation (MECH-093) |

These interact: action objects (SD-004) encode `z_world_t → z_world_{t+1}`, which requires
z_world to exist (SD-005). They should be designed and implemented together.

**V3 substrate checklist:**
- [x] Observation encoder routes sensory channels: body-state → z_self, world → z_world (SD-005 ✓)
- [x] E2 operates on z_self: `f(z_self_t, a_t) → z_self_{t+1}` (SD-004/005 ✓)
- [x] E2 also produces action objects: `f(z_world_t, a_t) → (z_world_{t+1}, o_t)` (SD-004 ✓)
- [x] HippocampalModule navigates action-object space, not raw z_world (SD-004 ✓)
- [x] ResidueField operates over z_world, not z_gamma (SD-005 ✓)
- [x] Three separate optimizers with three separate error signals (✓)
- [x] **SD-006: Asynchronous multi-rate execution** — time-multiplexed phase 1 implemented (✓).
  HTA phase 2 pending.
- [x] **ReafferencePredictor (SD-007)** — perspective-corrected z_world; MSTd-like efference
  copy subtraction. Implemented 2026-03-18 (MECH-098, MECH-101). ✓
- [x] CausalGridWorld extended with explicit self/world observation channels (✓)
- [x] **Q-020 adjudication complete** — ARC-007 strict (2026-03-16): HippocampalModule generates
  value-flat proposals; terrain sensitivity is residue geometry expressed through z_world. ✓
- [ ] **SD-010: Harm stream separation** — CausalGridWorldV2 emitting `harm_obs` separately
  from `world_obs`; dedicated HarmEncoder → z_harm; E3.harm_eval takes z_harm as primary
  input; SD-007 reafference restricted to z_world only. Registered 2026-03-19. Not yet
  implemented. Unblocks ~10 pending FAILs.
- [ ] **E3-derived dynamic precision**: precision computed from E3 prediction error, not
  hardcoded (required for ARC-016). EXQ-038 FAIL — root cause under analysis.
- [ ] **Precision→commitment→behavior circuit**: end-to-end wiring required (ARC-016).
- [ ] **TPJ comparator (MECH-095) wired**: agency_signal and residue_flag outputs.

---

## V3 Experiment Targets

These experiments cannot be run in V2 and should be designed during the V3 architecture phase:

### V3-EXQ-001 — Z_self vs Z_world Separation Validation
*Claim target: SD-005 prerequisite*
- Confirm that E2 prediction error on z_self is lower than on z_world (E2 specialises)
- Confirm that E3 planning error on z_world is lower than on z_self (E3 specialises)
- Pass: each component predicts its own channel significantly better than the other

### V3-EXQ-002 — Full Self-Attribution (SD-003 V3)
*Claim target: MECH-071 V3 form, MECH-095, SD-005*
- Requires: TPJ comparator (MECH-095) + dual-stream encoder (MECH-096) wired
- Compute `world_delta = ||z_world_{t+1}(a_actual) - z_world_{t+1}(a_cf)||` (E2+E3 joint pipeline)
- Compute TPJ `agency_signal` per step; confirm residue_flag route aligns with ground-truth agent-caused transitions
- Test discrimination: world_delta + agency_signal higher for agent_caused than env_caused
- Compare against V2 EXQ-027 calibration_gap (0.027) — predicted V3 gap: 0.15+ (see tpj_agency_comparator.md §6)
- Pass: calibration_gap > 0.05 (required); > 0.15 (confirms clean z_world signal)

### V3-EXQ-003 — Action Object Planning Horizon Extension (SD-004)
*Claim target: MECH-070 stronger form*
- Test that hippocampal rollout in action-object space effectively plans over longer
  horizons than V2's raw state-space CEM
- Pass: effective planning horizon in V3 > 2× V2 baseline

### V3-EXQ-004 — Three-Loop Incommensurability Demonstration (ARC-021 full)
*Claim target: MECH-069 full form*
- With z_self and z_world separated, show that mixing E2's motor-sensory error with
  E3's world-consequence error produces worse attribution than keeping them separated
- Directly tests the incommensurability claim that V2 can only approximate

### V3-EXQ-005 — World-Delta Residue Accuracy
*Claim target: MECH-072 V3 form, SD-005*
- Replace foreseeable-harm gating (V2 EXQ-028) with world_delta gating
- Pass: world_delta gating achieves near-ORACLE false attribution rate

### V3-EXQ-006 — Intrinsic Map Valence vs External Comparator (Q-020 core test)
*Claim target: MECH-073 vs ARC-007; prerequisite: SD-005*
- With z_world separated, test whether rollout proposals from HippocampalModule arrive at E3
  with value-correlated sampling frequencies *before* E3 scores them
- Design: compare rollout proposal distribution from HippocampalModule under (a) normal
  operation and (b) E3 scoring signals zeroed — if proposal distribution is value-flat in
  condition (b), ARC-007 strict holds; if still value-skewed, MECH-073 is confirmed
- Pass (MECH-073): proposal distribution is significantly value-skewed under zeroed E3 scoring
- Pass (ARC-007): proposal distribution is value-flat under zeroed E3 scoring; E3 introduces
  the weighting

### V3-EXQ-007 — Amygdala Write Operations Affect Map Geometry (MECH-074)
*Claim target: MECH-074, prerequisite: SD-005, Q-020 adjudication*
- Test whether ablating amygdala-analogue write access to the HippocampalModule during
  encoding flattens the value-skew in rollout proposals
- Pass: ablation reduces rollout value-correlation toward chance; confirms MECH-074 role (a)
  (encoding modulation as the write mechanism for map valence)
- This experiment also discriminates MECH-074 from MECH-075: if BG threshold-setting ablation
  (not amygdala write) flattens proposals, MECH-075 is the proximate cause

### V3-EXQ-009 — Path Memory Ablation with Proper HippocampalModule (ARC-007)
*Claim target: ARC-007, prerequisite: SD-004*
- Ablate hippocampal path memory in a V3 substrate where HippocampalModule navigates
  action-object space, not a raw obs-vector proxy
- Pass: PATH_MEMORY agent harm significantly lower than PATH_ABLATED (≥ 5% reduction,
  consistent across seeds)
- This re-tests the V2 experiment with a substrate capable of representing the claim

### V3-EXQ-010 — Dynamic Precision Regime Behavioral Distinction (ARC-016)
*Claim target: ARC-016, prerequisites: E3-derived dynamic precision, commitment→behavior circuit*
- Run HIGH_PRECISION and LOW_PRECISION conditions where precision is E3-derived
  (from prediction error variance), not externally imposed
- Pass: HIGH_PRECISION → lower harm and more committed action sequences;
  LOW_PRECISION → more exploratory, higher harm tolerance, behaviorally distinct
- Confirms that MECH-059's structural separation (precision ≠ PE) produces the
  behavioral regime switching that ARC-016 asserts

### V3-EXQ-008 — SD-005 Dissolves Q-020 (z_world = residue domain test)
*Claim target: Q-020 resolution via z_self/z_world split*
- With z_world separated, confirm that HippocampalModule rollout weights correlate with
  ResidueField curvature over z_world — i.e., the "valence" in rollouts is the residue field
  expressed through map geometry, not a separate value signal computed by the hippocampus
- Pass: rollout proposal weights ≈ function(ResidueField(z_world)) — valence is residue
  geometry, ARC-007 is not violated, MECH-073 is reframed as a consequence of ARC-013 on
  z_world
- Fail: rollout weights deviate from ResidueField predictions — hippocampus has independent
  value signal requiring MECH-073 full form and ARC-007 revision

---

## What Should Be Known Before V3 Design Starts

> **This section is now historical** — questions answered by the governance cycle
> (2026-03-19). Annotations added for reference.

After EXQ-028 completes, we need clarity on:

1. **Which parity claims survive at V2 substrate** (EXQ-014–017)
   → **RESOLVED:** EXQ-014–017 all PASS. MECH-059/056/060/061 confirmed on V2 substrate.
   These structural-separation results transfer to V3 and define the regression baseline.

2. **Whether E2 can discriminate at all in z_gamma** (EXQ-027)
   → **RESOLVED:** EXQ-027 FAIL (calibration_gap = -0.004). E2 cannot discriminate
   agent-caused harm in z_gamma — SD-005 is urgently needed. V3-form SD-003 subsequently
   validated at EXQ-030b PASS (attribution_gap=0.035, world_forward_r2=0.947) on V3
   substrate with z_world separation.

3. **Whether residue gating is useful at all** (EXQ-028)
   → **RESOLVED:** EXQ-028 FAIL. MECH-072 requires SD-005. Hard stop criterion 3 triggered.
   Attribution problem remains important but requires clean z_world (SD-010 also needed).

4. **Root cause of persistent FAILs** (MECH-058, MECH-033, ARC-018, ARC-007)
   → **RESOLVED:** All substrate-limited. MECH-058 → SD-005 needed; MECH-033/ARC-018/
   ARC-007 → SD-004 (action-object space) needed. All now retestable on V3 substrate.

5. **Q-020 provisional direction** (from theoretical analysis, before V3 experiments)
   → **RESOLVED:** ARC-007 strict adjudicated 2026-03-16. HippocampalModule generates
   value-flat proposals; valence in rollouts is residue geometry expressed through z_world,
   not an independent hippocampal value signal. MECH-073 reframed as ARC-013 applied to
   z_world specifically. HippocampalModule architecture finalised on this basis.

This evidence base was adjudicated in the governance cycle 2026-03-19.

---

## Summary: The V2→V3 Boundary

```
V2 can show:     structural separation, qualitative BG loops, approximate attribution
V2 cannot show:  self/world moral ontology, action-object planning, full attribution,
                 intrinsic map valence (Q-020)

V3 enables:      clean motor-sensory vs world-consequence isolation (SD-005)
                 compressed world-effect planning at longer horizons (SD-004)
                 proper residue field grounded in world_delta, not z_gamma (SD-005)
                 full causal self-attribution (SD-003 V3)
                 Q-020 resolution: SD-005 z_world split likely dissolves the conflict,
                   confirming residue field = map valence, ARC-007 intact (V3-EXQ-008)
                 heartbeat architecture: characteristic per-loop update rates, beta-gated
                   policy propagation, phase reset, SWR replay, z_beta rate modulation
                   (SD-006, ARC-023, MECH-089–MECH-093)

Design gate:     Q-020 adjudication required before HippocampalModule architecture
                 is finalised → DONE: ARC-007 strict (2026-03-16). E3 input contract
                 confirmed: value-flat proposal set from HippocampalModule.

Transition:      EXECUTED 2026-03-19. Governance cycle complete. V3 active.
                 Next substrate debt: SD-010 (harm stream separation).
```

---

*This document is historical. V2→V3 transition is complete. Active V3 roadmap in
`docs/roadmap.md` §REE-v3 (Step 3.1 current).*
