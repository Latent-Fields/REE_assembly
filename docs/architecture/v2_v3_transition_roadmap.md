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
| EXQ-014 | MECH-059 V2 parity | running |
| EXQ-015 | MECH-056 V2 parity | pending |
| EXQ-016 | MECH-060 V2 parity | pending |
| EXQ-017 | MECH-061 V2 parity | pending |
| EXQ-018 | SD-003 prereq (CausalGridWorld baseline) | pending |
| EXQ-019 | MECH-033 kernel chaining | pending |
| EXQ-020 | ARC-007 path memory ablation | pending |
| EXQ-021 | ARC-018 rollout viability | pending |
| EXQ-022 | Q-007 valence correlation | pending |
| EXQ-023 | MECH-058 E1/E2 terrain timescale | pending |
| EXQ-024 | MECH-057 attribution completion gating | pending |
| EXQ-025 | MECH-057 attribution completion gating v2 | pending |
| EXQ-026 | MECH-025 action-doing mode probe | pending |
| EXQ-027 | MECH-071 E2 attribution calibration (SD-003) | pending |
| EXQ-028 | MECH-072 selective residue attribution (SD-003) | pending |

**V2 experiment series closes after EXQ-028.** At that point, do a governance cycle then
assess whether to continue V2 or pause for V3 design.

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

---

## V2 "Done" Criteria — Transition Triggers

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

These interact: action objects (SD-004) encode `z_world_t → z_world_{t+1}`, which requires
z_world to exist (SD-005). They should be designed and implemented together.

**V3 substrate checklist:**
- [ ] Observation encoder routes sensory channels: body-state → z_self, world → z_world
- [ ] E2 operates on z_self: `f(z_self_t, a_t) → z_self_{t+1}`
- [ ] E2 also produces action objects: `f(z_world_t, a_t) → (z_world_{t+1}, o_t)` where `o_t`
  is the world-effect action object
- [ ] HippocampalModule navigates action-object space, not raw z_world
- [ ] ResidueField operates over z_world, not z_gamma
- [ ] Three separate optimizers with three separate error signals (currently true in V2, cleaner in V3)
- [ ] CausalGridWorld extended (or replaced) with explicit self/world observation channels

---

## V3 Experiment Targets

These experiments cannot be run in V2 and should be designed during the V3 architecture phase:

### V3-EXQ-001 — Z_self vs Z_world Separation Validation
*Claim target: SD-005 prerequisite*
- Confirm that E2 prediction error on z_self is lower than on z_world (E2 specialises)
- Confirm that E3 planning error on z_world is lower than on z_self (E3 specialises)
- Pass: each component predicts its own channel significantly better than the other

### V3-EXQ-002 — Full Self-Attribution (SD-003 V3)
*Claim target: MECH-071 V3 form, SD-005*
- Compute `world_delta = ||E2_world(z_world, a_actual) - E2_world(z_world, a_cf)||`
- Test discrimination: world_delta higher for agent_caused than env_caused
- Compare against V2 EXQ-027 calibration_gap — V3 should show stronger discrimination

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

---

## What Should Be Known Before V3 Design Starts

After EXQ-028 completes, we need clarity on:

1. **Which parity claims survive at V2 substrate** (EXQ-014–017)
   → determines which V3 architectural changes don't regress proven behaviour

2. **Whether E2 can discriminate at all in z_gamma** (EXQ-027)
   → determines how urgently SD-005 is needed; informs V3 priority ordering

3. **Whether residue gating is useful at all** (EXQ-028)
   → if ORACLE barely beats NAIVE, the attribution problem may be less important than expected

4. **Root cause of persistent FAILs** (MECH-058, MECH-033, ARC-018, ARC-007)
   → clarifies whether they're SD-004 failures, SD-005 failures, or claim failures

This evidence base is what the governance cycle after EXQ-028 should adjudicate.

---

## Summary: The V2→V3 Boundary

```
V2 can show:     structural separation, qualitative BG loops, approximate attribution
V2 cannot show:  self/world moral ontology, action-object planning, full attribution

V3 enables:      clean motor-sensory vs world-consequence isolation (SD-005)
                 compressed world-effect planning at longer horizons (SD-004)
                 proper residue field grounded in world_delta, not z_gamma (SD-005)
                 full causal self-attribution (SD-003 V3)

Transition:      after EXQ-028 + governance cycle, before further self-attribution experiments
```
