<!-- TRANSITION_BOUNDARY_VERSION: 2026-03-23.1 -->
# V3 / V4 Architecture Transition Boundary

## Overview

**V3** is the waking decision-making substrate: single-agent, fully online, no sleep/consolidation cycle. The core V3 achievement is a functioning commit gate (ARC-016/ARC-030) with symmetric go/no-go drives (MECH-112/116), multi-rate execution (SD-006), and the harm/reafference separation (SD-010).

**V4** adds the offline consolidation cycle: sleep phases (MECH-120-123), consolidated memory transfer from E3 to E1, precision prior recalibration, and dynamic modulation of setpoints currently hardcoded in V3.

The boundary is not a clean wall -- V3 must be designed with V4 in mind, measuring and scaffolding what V4 will later make dynamic.

---

## V3 Static Setpoints -> V4 Dynamic Mechanisms

These values are fixed constants in V3. In V4, they will be dynamically modulated by sleep phase machinery. V3 must:
(a) measure their natural setpoints under normal operation (so V4 calibration is principled), and
(b) accept them as config parameters (already done via `from_dims()`) so V4 can override them.

| V3 Static Setpoint | Current Value | V4 Dynamic Mechanism |
|---|---|---|
| `commitment_threshold` | 0.40 | Post-SWS recalibration (MECH-120); REM reset (MECH-123) |
| `residue field decay` | per-step static | SWS denoising pass (MECH-120) replaces step-wise |
| `z_goal.decay_goal` | 0.005/step | Extended during NREM consolidation (MECH-121 protects goal traces) |
| `z_goal.alpha_goal` | 0.05 | Boosted during consolidation for goal-trace preferential strengthening |
| `z_delta` recalibration | none | SWS attractor flattening (MECH-120), REM prior reset (MECH-123) |
| `alpha_world` | 0.9 | Modulated by attentional state / z_beta arousal |
| `ThetaBuffer size` | 10 | Modulated by z_beta arousal (MECH-093); bidirectional in V4 (MECH-122) |
| `e3_steps_per_tick` | 10 | Modulated by MECH-093 z_beta heartbeat rate |
| `E1 prediction_horizon` | 20 | Extended during REM unconstrained simulation (MECH-123) |
| `D_eff threshold` | 1.5x baseline | Sleep-calibrated: EXQ-075 setpoint becomes V4 dynamic baseline |
| `z_beta EMA alpha` | 0.3 (shared) | Modulated by sleep phase (near-zero during REM aminergic suppression) |
| `precision_ema_alpha` | 0.05 | Recalibrated post-SWS (MECH-120 SNR restoration changes variance baseline) |
| `novelty_bonus_weight` | 0.0 (off) | V4: modulated by post-REM curiosity state (novel prior hypotheses from MECH-123) |

**V3 measurement requirement:** For each setpoint above, V3 experiments must log the value's natural range across episodes (min, max, mean, std) so V4 calibration targets are principled, not arbitrary.

---

## V3 Prerequisites for V4

These must be validated in V3 before V4 consolidation is implementable:

| Prerequisite | V3 Mechanism | Validation Experiment | Status |
|---|---|---|---|
| Quiescent replay infrastructure | MECH-092 | EXQ-061 (PASS) | PASS |
| Hypothesis tag (commit suppression) | MECH-094 | -- | candidate, untested |
| Multi-rate execution | SD-006 | EXQ-052b (PASS) | PASS |
| ThetaBuffer waking direction | MECH-089 | EXQ-052b (PASS) | PASS |
| ThetaBuffer bidirectional | MECH-122 prereq | Not yet designed | V4 design needed |
| D_eff monitoring with stable setpoint | MECH-113 | EXQ-075 (pending) | pending |
| z_goal persistent representation | MECH-112/116 | EXQ-074b, EXQ-076 (pending) | pending |
| Balanced harm/goal salience | MECH-124 prereq | EXQ-074b outcome | pending |
| z_beta natural setpoint measured | MECH-093 | ongoing telemetry | partial |
| Go/NoGo competitive commit | ARC-030 | EXQ-077 (planned) | planned |

---

## V4 Scope Summary

V4 implements the offline consolidation cycle:

1. **Entry trigger**: quiescent period detected (z_beta below threshold, no external input for N steps)
2. **Sub-phase sequence**:
   - Phase 0: Sensory gating (spindle analog, MECH-122) -- block new input
   - Phase 1: SWS denoising (MECH-120) -- residue flattening, z_delta recalibration
   - Phase 2: NREM replay (MECH-121) -- E3/hippocampal -> E1/neocortical transfer
   - Phase 3: Spindle coordination (MECH-122) -- theta channel bidirectional packaging
   - Phase 4: REM recalibration (MECH-123) -- precision priors reset, E1 unconstrained
3. **Exit**: all setpoints recalibrated; sensory gating lifted; z_beta restored to waking baseline
4. **Guard**: MECH-124 prevention -- balanced replay scheduling, MECH-094 tag active throughout

V4 also adds:
- Dynamic setpoint modulation (all items in table above become driven by sleep phase state)
- Bidirectional ThetaBuffer (MECH-122)
- Sleep phase controller (new module, analogous to mode_manager but for offline cycle)

---

## Current Session Priority Note (2026-03-23)

The go mechanism (ARC-030, MECH-112, MECH-116, MECH-117) is the current priority over completing the no-go mechanism. The no-go architecture (SD-010, MECH-095, ARC-016) is near-complete. The approach drive architecture (z_goal, wanting/liking separation, D1/D2 competitive commit) is actively being built. Experiments EXQ-072-076 address this. The MECH-124 consolidation failure mode further motivates prioritising go: without adequate z_goal salience in V3, V4 consolidation will amplify the imbalance.

---

## Relation to Existing Transition Documents

- `v2_v3_transition_roadmap.md` -- V2->V3 transition rationale and SD-004/SD-005 motivation
- This document -- V3->V4 boundary specification and static setpoint registry
- V5 scope (multi-agent social synchronisation) is noted in `control_plane_heartbeat.md`
