# V3-EXQ-133 -- MECH-091 Salient-Event Phase-Reset Discriminative Pair

**Status:** FAIL
**Claims:** MECH-091
**Decision:** retire_ree_claim
**Seeds:** [42, 123]
**Conditions:** PHASE_RESET_ON vs PHASE_RESET_ABLATED
**Warmup:** 400 eps  **Eval:** 50 eps
**Env:** CausalGridWorldV2 size=6, 4 hazards, nav_bias=0.5
**E3 heartbeat K:** 5 (both conditions)

## Design

MECH-091 asserts salient events phase-reset the E3 heartbeat clock,
ensuring harm estimates enter E3 at the start of a fresh cycle.

PHASE_RESET_ON: on harm contact (is_harm=True), heartbeat_counter resets to 0, aligning the next E3 update window with the salient event.

PHASE_RESET_ABLATED: heartbeat_counter increments continuously; salient events land at arbitrary phase positions (no alignment guarantee).

Both conditions: E3_HEARTBEAT_K=5, same architecture, same nav_bias. Only cycle-boundary alignment on harm events differs.

Key metric: harm_eval_gap = mean_harm_score - mean_safe_score at eval.
Manipulation check: n_salient_resets (phase resets fired in PHASE_RESET_ON).

## Pre-Registered Thresholds

C1: gap_reset_on >= 0.04 in all seeds  (PHASE_RESET_ON above floor)
C2: per-seed delta (ON - ABLATED) >= 0.02 in all seeds  (phase-reset adds >=2pp)
C3: gap_ablated >= 0.0  (ablation learns something; data quality)
C4: n_harm_eval_min >= 20  (sufficient harm events)
C5: n_salient_resets >= 10  (phase resets fired; manipulation check)

## Results

| Condition | gap (avg) | mean_harm | mean_safe | resets |
|-----------|-----------|-----------|-----------|--------|
| PHASE_RESET_ON      | 0.0140 | 0.5405 | 0.5265 | 5656 |
| PHASE_RESET_ABLATED | -0.0006 | 0.5039 | 0.5046 | -- |

**delta_gap (ON - ABLATED): +0.0146**

Manipulation check: n_salient_resets_total=5656 (confirms phase resets fired in PHASE_RESET_ON).

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: gap_on >= 0.04 (all seeds) | FAIL | 0.0140 |
| C2: per-seed delta >= 0.02 (all seeds) | FAIL | [0.0198, 0.0094] |
| C3: gap_ablated >= 0.0 | FAIL | -0.0006 |
| C4: n_harm_min >= 20 | PASS | 122 |
| C5: n_salient_resets >= 10 | PASS | 5656 |

Criteria met: 2/5 -> **FAIL**

## Interpretation

MECH-091 NOT supported at V3 proxy level: gap_on=0.0140 (C1 FAIL), delta=+0.0146 (C2 FAIL). Phase-reset of E3 heartbeat on salient events does not produce a detectable improvement in harm_eval quality at this scale. Possible reasons: (a) heartbeat_k=5 cycle is too short for phase alignment to matter -- try larger K; (b) harm events too rare to accumulate sufficient phase-aligned integration windows (check C5); (c) at world_dim=32 E3 harm_eval quality is dominated by training data volume rather than cycle-boundary alignment; (d) SD-006 phase 2 async implementation required for full effect.

## Per-Seed

PHASE_RESET_ON:
  seed=42: gap=0.0189 n_harm=396 resets=5703
  seed=123: gap=0.0091 n_harm=406 resets=5610

PHASE_RESET_ABLATED:
  seed=42: gap=-0.0009 n_harm=122 resets=-- (ablation)
  seed=123: gap=-0.0003 n_harm=130 resets=-- (ablation)

## Failure Notes

- C1 FAIL: PHASE_RESET_ON gap below 0.04 in seeds [42, 123] -- phase-reset does not produce discriminative harm eval signal
- C2 FAIL: per-seed deltas [0.0198, 0.0094] < 0.02 -- phase-reset does not add >=2pp harm eval advantage over ablation
- C3 FAIL: gap_ablated=-0.0006 < 0.0 -- ablated condition fails entirely; confound check required
