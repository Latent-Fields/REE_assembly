# Failure Autopsy: V3-EXQ-862 (Q-040c dACC PE weight-delta correlation, 475c requeue)

**Generated:** 2026-08-02T10:50:16Z | **Status:** confirmed | **Scope:** single

## Facts

- Run: `v3_exq_862_q040c_dacc_pe_weight_delta_correlation_20260802T032301Z_v3`, FAIL, claim Q-040. Supersedes V3-EXQ-475b.
- 475b's confirmed autopsy (`failure_autopsy_V3-EXQ-475b_2026-08-01`) found `build_config()` never received `enable_affective_harm_stream=True`, so `z_harm_a` stayed structurally `None` and dACC's own invocation guard (`self.dacc is not None and z_harm_a is not None`) never fired: `n_dacc_fires=0` on every seed x arm.
- 862 (475c) is the fix requeue: passes `enable_affective_harm_stream=True`, and also adds a preflight smoke gate (`_preflight_dacc_engagement_check`) asserting dACC fires at least once before the full design commits compute.
- **The fix worked for engagement**: seed 42's per_run row shows `n_dacc_fires=451` (was 0). P1 (MECH-269b V_s gating) passed cleanly (2/3 seeds).
- **But P2 (dACC engagement, defined as bias-magnitude nonzero) still fails completely**: `dacc_bias_nonzero_steps=0` in every per-run cell, `p2_on_dacc_fired_seeds=0`, `p2_off_dacc_fired_seeds=0`. `acceptance.degenerate_metrics.dacc_bias_magnitude_series` shows all 6 groups pinned at constant 0, zero spread.
- Self-route: `substrate_not_ready_requeue` (acceptance.pass=false, preconditions_met=false) -- correctly caught by the driver's own P2 precondition, before any correlation statistic was computed.

## Code-verified root cause

`ree_core/cingulate/dacc.py:505-550`, `DACCtoE3Adapter.forward()`:
```
weight = self.config.dacc_weight * float(bundle.get("drive_gain", 1.0))
if weight == 0.0:
    scaled = torch.zeros_like(mode_ev)
```
The class's own docstring states verbatim: *"All multipliers default to 0, so with default config the bias is the zero vector regardless of bundle content."* `dacc_weight` defaults to 0.0 in `DACCConfig`. Grep of `experiments/v3_exq_862_q040c_dacc_pe_weight_delta_correlation.py` confirms zero mentions of `dacc_weight` anywhere in the driver -- it was never set. So the bias output is structurally guaranteed to be zero, entirely independent of dACC actually firing or of what PE it computes.

The new preflight gate (`_preflight_dacc_engagement_check`) checks `pe is not None and bias_mag is not None` -- `bias_mag=0.0` satisfies `is not None`, so the gate passes even though the bias is guaranteed zero. It catches 475b's defect class (signal never computed) but is structurally blind to this one (signal computed but its consumer weight is zero).

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | P1 fine, DV unmeasurable |
| Biological reference | unchanged | Shenhav 2013 EVC |
| Prerequisites | present | MECH-269b confirmed fine |
| Implementation | working-as-documented STOPGAP | dacc_weight=0 default is intentional and documented |
| Measurement | defect | preflight checks definedness, not magnitude |
| Integration | isolated | two independently-gated stages; only one was fixed |

## Learning extracted

1. A preflight gate for "signal never computed" doesn't catch "signal computed but consumer weight is zero" -- check magnitude, not definedness.
2. DACCtoE3Adapter is an explicit STOPGAP with a documented no-op default; a driver exercising it must opt in via `dacc_weight>0`.
3. P1-clean/P2-fails-completely is informative again: defect isolated to one config flag, not the upstream substrate.

## Routing

**epistemic_category:** `measurement_test_design_defect` | **evidence_direction:** `non_contributory` | **routing:** `/queue-experiment` same-question letter setting `dacc_weight` (+ at least one sub-weight) nonzero, and extending the preflight to assert bias MAGNITUDE nonzero, not just definedness.

**User gate (2026-08-02):** Approved as recommended.
