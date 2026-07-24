# Failure Autopsy: V3-EXQ-793 (SD-049 curriculum/density lever-sufficiency diagnostic)

**Generated:** 2026-07-24T07:18:04Z
**Status:** confirmed (interactive gate cleared with user 2026-07-24)
**Scope:** single
**Run:** `v3_exq_793_sd049_arm2_competence_calibration_20260721T113813Z_v3`
**Queue ID:** V3-EXQ-793
**Claims:** SD-049

## 1. Facts

Flagged `precondition_unmet` by the indexer despite a self-routed PASS
(`both_levers_sufficient_alone`). All 3 manifest preconditions pass:

| Precondition | Measured | Threshold | Met |
|---|---|---|---|
| `density_preserving_spawn_kwarg_available` | 1.0 | 1.0 | true |
| `baseline_arm_reproduces_693a_ceiling` | 0.0202 | 0.02 (upper) | true (barely -- see §2) |
| `density_manipulation_effective_on_on_arms` | 0.0 | 0.0 | true |

All 4 criteria pass, including load-bearing `C_JOINT`:

| Arm | Label | d3_clears | n_seeds_guard_pass |
|---|---|---|---|
| A00 | base curriculum, density off | **false** (correctly reproduces the ceiling) | 3/3 |
| A10 | amended curriculum alone | true | 2/3 |
| A01 | density alone | true | 2/3 |
| A11 | both levers | true | **1/3** |

## 2. Adjudicating the self-route

The arm-level `d3_clears` reading is genuine on its own terms -- A00 correctly fails to clear
(reproducing the 693a ceiling at 0.0202, just under the 0.02 threshold), and A10/A01/A11 each clear.
This licenses the `both_levers_sufficient_alone` reading: neither lever needs the other.

**But per-seed data shows fragility the arm-level criteria don't surface.** `arm_summaries.per_seed_
guard_pass`:

- A11 (both levers): `[true, false, false]` -- **2 of 3 seeds fail guard**, yet the arm reads
  `d3_clears: true` because that criterion is computed from mean `contact_rate`, which does not
  require `guard_pass`.
- A01: `[true, true, false]` -- 1/3 seed guard failure.
- A10: `[true, true, false]` -- 1/3 seed guard failure.

This is not itself a load-bearing criterion failure (the criteria as designed pass cleanly), but it
is a real signal that the JOINT-levers arm specifically is not robustly clearing on every seed --
only on the mean. At n=3, a 2/3 guard-failure rate on the strongest arm is a fragility flag, not
noise to be waved past.

**Separately, and more consequentially: SD-049 is parked on a DIFFERENT prerequisite.** Its
`ceiling_routing_note` (2026-06-19 triage) is explicit: *"Phase-2 V3-EXQ-514 validation blocked on
~0.2% consumption on the enriched reef... route to /implement-substrate foraging scaffold, not a
MECH-307 retest."* 793 tests curriculum/density lever sufficiency for a narrower D3 gate -- it does
not test, and cannot lift, the foraging-competent-policy prerequisite the actual park is gated on.

## 3. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | narrow | tests lever sufficiency for D3, not SD-049's actual parked prerequisite |
| Biological reference | partial | curriculum/environment-design diagnostic, not a mechanism test |
| Prerequisites | present | all 3 manifest preconditions pass |
| Implementation | complete | for the levers under test |
| Environment | adequate for D3; not for the broader Phase-2 question | -- |
| Measurement | arm-level `d3_clears` doesn't surface per-seed guard fragility | the gap is in criteria design, not the run |
| Integration | coupled | -- |
| Scale | 3 seeds/arm -- thin given the joint-levers arm's 2/3 guard failures | -- |

**Recommended `epistemic_category`: `measurement_gap`** (the criteria as designed don't surface
seed-level guard fragility; not itself grounds for `substrate_ceiling` or `measurement_test_design_
defect`).

## 4. Learning extracted

- Both the curriculum amendment and the density-preserving spawn independently lift the D3 gate over
  the 693a baseline -- a genuine, narrow curriculum/environment-design finding.
- The joint-levers arm (A11) is the LEAST robust by seed (2/3 guard failures) despite reading as the
  cleanest arm-level pass -- a criteria-design gap worth fixing if this diagnostic family is reused.
- This result does not lift SD-049's parked `substrate_ceiling` status; the park is gated on a
  foraging-competent policy for Phase-2 (V3-EXQ-514), which 793 does not address.

## 5. Repair pathway

Recommend `/queue-experiment` for a targeted power increase specifically on A11 (more seeds, and
make `guard_pass` load-bearing rather than informational for the joint-levers arm) if a decisive
read is wanted -- not a full re-letter, since A00/A10/A01's readings are solid. SD-049's actual park
remains untouched; it still needs the foraging scaffold `/implement-substrate` work the 2026-06-19
triage named, not a retest of this diagnostic.

### Draft `evidence_quality_note` (governance to write -- do not apply here)

See the JSON artifact's `recommended_evidence_quality_note`. Recommended `evidence_direction:
inconclusive` (informative but thin; does not change SD-049's parked status).

## 6. Confirmed routing (user-adjudicated 2026-07-24)

User confirmed **"Real but narrow finding (Recommended)"**: the lever-sufficiency result is genuine
but not decisive given the seed-level guard fragility, and it does not lift SD-049's park (gated on
a separate, unaddressed prerequisite).
