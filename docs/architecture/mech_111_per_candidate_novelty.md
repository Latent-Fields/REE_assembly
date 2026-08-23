---
title: MECH-111 per-candidate E1-prediction-error novelty (PARKED design)
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 4
status: candidate
status_asof: 2026-07-10
status_claim: MECH-111
---

# MECH-111 per-candidate E1-prediction-error novelty (PARKED design)

**Status:** PARKED — design-complete, NOT implemented. Do not treat as a live
substrate. No code, no config, no contracts, no claims change exist for this.
**Authored:** 2026-06-09T22:06Z
**Maps to:** MECH-111 (E1-prediction-error novelty drive) rendered per-candidate;
equivalently the deferred MECH-314b Phase-2 refinement
("E1 LSTM forward variance over candidates", `structured_curiosity.py:24-25`).

---

## Why this is parked (read first)

This design was worked out for `infant_substrate:GAP-13` (V3-EXQ-590 novelty
Goldilocks calibration), then **stood down** after the 2026-06-09 GAP-13
re-adjudication (`REE_assembly` commit `1906f95a0d`) established that:

1. A **per-candidate novelty routing channel already landed** 2026-06-07
   (MECH-314a Phase-2, `curiosity_candidate_source=e2_world_forward`), and
   **V3-EXQ-648a proved it carries variance into E3** (C2 load-bearing PASS;
   consumed candidate z_world spread 0.149; curiosity bias range 0.0206). So
   "the per-candidate channel does not carry variance" is no longer true.
2. The real residual for GAP-13 is **selection authority** — whether a
   per-candidate-varying bias actually moves the committed `argmin` — which is
   owned by the shared behavioural-diversity frontier (modulatory-bias-selection
   -authority / V3-EXQ-643a, MECH-341 / V3-EXQ-660, V3-EXQ-604c), NOT by adding
   another novelty channel.

This mechanism (E1-prediction-error novelty) is a **scientifically distinct**
signal from the existing spatial-distance channel (MECH-314a, Wittmann-2008
striatal novelty = distance to visitation/residue centres). It is the faithful
rendering of MECH-111's actual claim — *novelty = E1 prediction error*. But:

- It is **not what GAP-13 or its unblocked claims (DEV-NEED-003, MECH-314) need**
  — those are served by the existing channel.
- It would hit the **same selection-authority wall**: a varying E1-PE bias still
  has to win the `argmin` against primary harm/goal scores, exactly what V3-EXQ
  -643a gates. Until that frontier lands contributory, this channel is as
  selection-inert as any other modulatory bias, so it would be non-validatable.
- MECH-111 is currently a **dead, non-priority claim** (the broadcast branch was
  deleted 2026-05-25; `novelty_bonus_weight` is a no-op knob).

**Resume trigger:** revisit only if (a) MECH-111 or MECH-314b Phase-2 becomes a
governance priority in its own right, AND (b) the selection-authority frontier
(V3-EXQ-643a + 604c + 660) has landed contributory so a validation experiment is
runnable rather than vacuous.

---

## Problem this would solve (if ever live)

MECH-111's claim is *novelty = E1 prediction error*. Its only V3 instantiation
was a **broadcast scalar** `E3Selector._novelty_ema` (EMA of E1 prediction-error
MSE) subtracted uniformly from every candidate score — which is **argmin
-invariant** (a uniform shift never changes selection) and was deleted
2026-05-25 (`evidence/planning/v3_exq_571_root_cause_2026-05-25.md`). The result:
`novelty_bonus_weight` is a dead knob, and V3-EXQ-590's 5-arm sweep produced
byte-identical coverage across all arms.

The existing per-candidate channel (MECH-314a) carries **spatial-distance**
novelty (distance of each candidate's predicted z_world to the visitation
buffer / active residue centres). It does **not** carry the E1-prediction-error
signal that defines MECH-111. This design adds that signal per-candidate.

## Core mechanism

A small **learned forward-variance head `nu`** on `E1DeepPredictor` that predicts
*how surprising E1 will find a state*, evaluated per candidate:

```
nu : z_world -> scalar   (expected E1 prediction error at that state)
```

Why a learned head rather than re-running E1 over each candidate rollout: a
hypothetical candidate rollout has no ground-truth next state, so the *true*
prediction error is uncomputable at selection time. `nu(z_world)` is the standard
predictive surrogate (Pathak 2017 ICM forward-error; Daw 2006 frontopolar
uncertainty) and is O(1) per candidate vs an LSTM re-roll.

## Design (implement-substrate Step 3 form)

### Config (all no-op defaults; gated on `novelty_bonus_weight > 0 AND use_e1_novelty_head`)

| Param | Type | Default | Purpose |
|---|---|---|---|
| `use_e1_novelty_head` | bool | False | master; builds `nu` head on E1 |
| `e1_novelty_head_hidden` | int | 32 | head width |
| `e1_novelty_target_ema_alpha` | float | 0.1 | EMA-smoothing of the regression target |
| `novelty_bonus_weight` | float | 0.0 | **revived** live per-candidate scale (the 590 sweep knob) |
| `novelty_bonus_bias_scale` | float | 0.1 | clamp, mirrors `curiosity_bias_scale` |

### Data flow

```
TRAIN (sense / training tick):
  realized E1 PE = compute_prediction_loss()   # [z_self, z_world] MSE; harm-excluded
  target_ema <- EMA(realized PE)
  L_nu = MSE( nu(z_world_prev.detach()), target_ema )   # detached input: no grad into encoder

SELECT (select_action):
  cand_summaries[K, world_dim] <- _candidate_world_summaries(...)   # e2_world_forward (ARC-065 GAP-A)
  per_cand_novelty[K] = nu(cand_summaries).detach()                # genuinely per-candidate
  mech111_bias[i] = -clamp( novelty_bonus_weight * per_cand_novelty[i], +/- bias_scale )
  dacc_score_bias += mech111_bias   -> e3.select(score_bias=)      # argmin shifts
```

- The trainable `nu` head lives on `E1DeepPredictor` (it estimates E1's own
  error; sits beside the existing `schema_readout_head`, `e1_deep.py:170`).
- `StructuredCuriosity` stays **pure-arithmetic**: its 314b leg gains an optional
  `per_candidate_uncertainty` argument that, when supplied, replaces the
  broadcast `e3._running_variance` scalar with `nu(cand_summaries)` per-candidate.
  So the bias composition reuses the existing curiosity path; only the source of
  the 314b signal changes.

### Backward compatibility
Master off / `novelty_bonus_weight = 0.0` -> head not built, no channel ->
bit-identical. The ~30 existing callers passing `novelty_bonus_weight=0.0` are
unaffected.

### Phased training (REQUIRED — the correctness gate)
An untrained `nu` outputs noise -> per-candidate spread is noise -> re-vacuates
exactly like the e2 / encoder cases.
- **P0:** warm E1 + `nu` (regress realized E1 PE) until `nu`'s per-candidate
  spread over K exceeds a floor.
- **P1:** freeze E1; `nu` reads frozen z_world; channel active.
- **Validation non-vacuity precondition:** `nu_per_candidate_range > floor` AND
  `cand_world_pairwise_dist > floor` (requires SD-056-trained e2 +
  `candidate_summary_source="e2_world_forward"`), else
  `substrate_not_ready_requeue`. Same guard pattern as V3-EXQ-648a / 649.

### MECH-094
Applies. `nu` training and candidate reads are waking-only; the bias compute
takes `simulation_mode` and returns zeros under replay (mirrors 314a/b/c).
Handled by call-site scoping + the `simulation_mode` argument.

### GAP-4 stochastic-attractor safety (binding constraint from the closure node)
SD-048 interoceptive noise is the primary irreducible stochastic attractor; a
forward-PE novelty signal will otherwise chase irreducible noise (Burda 2018
noisy-TV). Mitigation is **structural**: `nu` regresses the **harm-excluded** E1
prediction error — `compute_prediction_loss` (`agent.py:6008`) is MSE over the
`[z_self, z_world]` sequence only (z_harm / z_harm_a are not in E1's input), and
`z_world` does not carry `harm_obs_a` (GAP-4 audit). So the autonomic-noise
attractor cannot enter `nu`. Deliberately **NOT** `e3._running_variance` (which
SD-048 inflates and which the broadcast 314b leg currently reads).

### ML/AI engineering notes
- Moving-target instability (BYOL / target-network lesson): the regression
  target (E1's own PE) drifts as E1 learns -> EMA-smoothed target +
  `.detach()` on the z_world input.
- Target = z_world / z_self prediction error, not the E2/E3 running variance —
  that departure is the whole point of the mechanism.

## Validation (when unblocked)
V3-EXQ-590b: the same 5-arm Goldilocks over `novelty_bonus_weight in {0.1..1.0}`,
on this channel — P0 trains e2 (SD-056) + E1 + `nu`; non-vacuity precondition
guards re-vacuity; the sweep then measures whether different weights produce
different `mean_coverage` / `H_pos` (the inverted-U Goldilocks point). Queue via
`/queue-experiment`. NOTE: this is the E1-PE-channel variant; the
re-adjudication's sanctioned 590b runs on the *spatial* MECH-314
`e2_world_forward` channel — these are different experiments testing different
novelty signals.

## Relationship to existing substrate
- **MECH-314a (live):** spatial-distance novelty (Wittmann 2008). Distance of
  candidate z_world to visitation/residue centres. Different signal.
- **MECH-314b Phase-1 (live):** broadcast `e3._running_variance` scalar. This
  design is its deferred Phase-2 per-candidate refinement.
- **MECH-111 broadcast (dead):** deleted 2026-05-25; argmin-invariant.
- **This design:** the per-candidate, learned, E1-PE rendering — instantiates
  MECH-111 per-candidate and closes MECH-314b Phase-2 in one head.

## References
- `evidence/planning/v3_exq_571_root_cause_2026-05-25.md` — broadcast deletion +
  the E2-bottleneck root cause + follow-on #5 (always-populating visitation buffer).
- `evidence/planning/infant_substrate_plan.md` — GAP-13 node + the 2026-06-09
  re-adjudication (`1906f95a0d`).
- `ree-v3/CLAUDE.md` — SD-056, ARC-065 GAP-A, MECH-314a Phase-2 amend (V3-EXQ-648a),
  MECH-314 / MECH-313 / MECH-320 entries.
- Pathak et al. 2017 (ICM forward-error intrinsic motivation); Daw et al. 2006
  (frontopolar exploration uncertainty); Burda et al. 2018 (noisy-TV).
