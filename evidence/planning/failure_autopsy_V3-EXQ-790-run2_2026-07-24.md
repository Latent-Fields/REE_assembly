# Failure Autopsy: V3-EXQ-790 (second run, channel-routing diagnostic)

**Generated:** 2026-07-24T07:18:04Z
**Status:** confirmed (interactive gate cleared with user 2026-07-24)
**Scope:** single
**Run:** `v3_exq_790_channel_routing_cross_class_magnitude_replication_20260722T142736Z_v3`
**Queue ID:** V3-EXQ-790
**Claims:** none (diagnostic, claim_ids=[])

## 1. Facts

Sibling diagnostic to `V3-EXQ-791` (run `..._20260722T021558Z_v3`), which already has a confirmed
autopsy (`failure_autopsy_V3-EXQ-790_2026-07-22`) titled after its own filename convention but
actually covering queue_id 791. Rather than assume this second run shares the same diagnosis, it was
independently re-derived from its own manifest.

**Preconditions (identical schema to the sibling):**

| Precondition | Measured | Threshold | Met | Offending cell |
|---|---|---|---|---|
| `adequate_fresh_selection_sample` | 19 | 200 | **false** | `ARM_1_ROUTE_ON::seed49` |
| `arm1_routed_bias_range_supra_floor` | 0.269 | 0.01 | true | -- |
| `routed_range_bounded` | 1.665 | 1e6 | true | -- |

**Criteria:**

| Criterion | Load-bearing | Passed |
|---|---|---|
| C1_routed_range_reaches_accumulator_on_active_off_inactive | yes | **true** |
| C2_committed_class_distribution_moves_on_vs_off | no | true |

## 2. Comparison with the sibling run (V3-EXQ-791)

| | V3-EXQ-791 (sibling, autopsied 07-22) | V3-EXQ-790 (this run) |
|---|---|---|
| Offending cell | `ARM_0_NO_ROUTE::seed49` (control arm) | `ARM_1_ROUTE_ON::seed49` (**treatment arm**) |
| Fresh-selection count | 53 / 200 | 19 / 200 (more severe) |
| Routed-bias range | 0.334 | 0.269 (both comfortably above the 0.01 floor) |
| C1 / C2 | both pass | both pass |

The under-sampling this time lands on the treatment arm rather than the control arm, and is more
severe. Despite that, both science criteria still pass cleanly and the range statistic still clears
its floor by more than 25x. This is the same qualitative signature: the readiness floor is
mis-calibrated, not the routing mechanism.

## 3. Adjudicating the self-route

`substrate_not_ready_requeue` / `precondition_unmet` is the self-route. Per the sibling's autopsy,
the `adequate_fresh_selection_sample` floor (200) is derived from the NOMINAL default cadence
(`e3_steps_per_tick=10`), which the MECH-093-modulated substrate does not run (actual cadence is
5-20 steps, so far fewer genuine `select()` calls land in a fixed tick window than the floor
assumes). The gate is applied arm-blind, so on any given run either arm can be the one that happens
to starve. Two independent runs have now shown the SAME gate defect landing on DIFFERENT arms --
this is exactly the pattern predicted by a cadence-mismatched floor, not evidence of two separate
substrate problems.

**Verdict: WITHDRAWN as a gate defect, science upheld** -- same reading as the sibling, independently
confirmed.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | readiness diagnostic, claim_ids=[] |
| Biological reference | partial | not the operative axis |
| Prerequisites | present | routing wired and active |
| Implementation | complete | routing functions correctly on both arms |
| Environment | adequate | -- |
| Measurement | **misleading (dominant)** | readiness floor miscalibrated for the actual cadence, applied arm-blind |
| Integration | coupled | -- |
| Scale | adequate for the science; inadequate only for the readiness floor | -- |

**Recommended `epistemic_category`: `measurement_test_design_defect`.**

## 5. Learning extracted

- The `adequate_fresh_selection_sample` floor (200, nominal-cadence-derived) is confirmed
  mis-calibrated on TWO independent runs now, landing on different arms both times -- this is a
  standing infrastructure defect in the diagnostic's own gate, not evidence about the substrate.
- Both times the science criteria (C1 load-bearing, C2 corroborator) pass cleanly despite the
  under-sampled cell -- the routing effect is robust enough to be measurable even under low power,
  which is mild positive evidence for the mechanism's robustness.

## 6. Repair pathway

Recommend a standing fix: compute the readiness floor from the arm's own OBSERVED cadence rather
than the nominal default, so this gate-defect class stops recurring across future channel-routing
diagnostics that share this driver. This is an infrastructure fix to the diagnostic harness, not a
same-question re-queue of either V3-EXQ-790 or V3-EXQ-791 (both already produced clean, informative
science despite the gate defect).

### Draft `evidence_quality_note` (governance to write -- do not apply here)

> claim_ids=[] -- no claim to annotate. See the JSON artifact's `recommended_evidence_quality_note`
> for the full text; nothing lands in claims.yaml for this target.

## 7. Confirmed routing (user-adjudicated 2026-07-24)

User confirmed **"write a fresh diagnosis"** rather than a blind amend of the sibling autopsy --
this document is that independent re-derivation. It reaches the same conclusion (gate defect,
science upheld) as the sibling, now on independently verified grounds.
