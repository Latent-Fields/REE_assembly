# Failure autopsy -- V3-EXQ-642a (MECH-353 blocked-agency z_block discriminative retest)

- **Status:** `awaiting_human_confirmation` (staging mode -- non-interactive session; routing NOT finalised)
- **Generated:** 2026-08-30T06:34:18Z
- **Run:** `v3_exq_642a_blocked_agency_zblock_discriminative_20260829T185417Z_v3`
- **Purpose:** `diagnostic`, `claim_ids: []` (bears on MECH-353, SD-029, MECH-112, MECH-320, MECH-342, ARC-016, SD-011, SD-019b, SD-070, SD-056)
- **Supersedes:** V3-EXQ-642 (FAIL 2026-06-06)
- **Dry-run gate:** clean (real run, `dry_run: false`)

## 1. Facts

| Criterion | Load-bearing | Result |
|---|---|---|
| C0 detector readiness | yes | **PASS** (margins 0.6241 / 0.5322 / 0.5077 vs floor 0.10) |
| C1 z_block rises | yes | **FAIL** |
| C2 dissociation from z_harm_a | yes | **FAIL** |
| C3 assert not withdraw | yes | **PASS** |

Per-seed, both arms:

| Seed | `z_block_peak` BLOCK | `z_block_peak` CONTROL | separation | `z_block_mean` BLOCK | `z_block_mean` CONTROL | mean sep |
|---|---|---|---|---|---|---|
| 42 | **1.5** | **1.5** | 0.0 | 1.4286 | 1.2636 | +0.165 |
| 43 | **1.5** | **1.5** | 0.0 | 1.4429 | 1.3215 | +0.121 |
| 44 | **1.5** | **1.5** | 0.0 | 1.4358 | 1.3527 | +0.083 |

`z_harm_a_mean` is exactly `0.0` in both arms on all seeds (by design, `num_hazards=0`).

Recording core present: `substrate_hash`, `config`, `seeds`, `machine_class`, `recording_schema`, `elapsed_seconds` all recorded.

## 2. The decisive finding -- C1 could not have passed

`z_block_cap = 1.5` is a hard clamp (`ree_core/affect/blocked_agency.py:114`, applied at `:257`). **Both arms reach it, on every seed.** C1 is `z_block_peak(BLOCK) - z_block_peak(CONTROL) >= 0.2`; with both terms pinned at the clamp the numerator is **0.0 by construction**, whatever z_block actually did. The criterion could not have returned any other value.

C2 is doubly vacuous: it subtracts a `z_harm_a` separation that is a constant `0.0` from a `z_block` separation that is a saturated `0.0`.

**Why the control arm saturates.** `blocked_agency` accumulates whenever `outcome_mismatch >= outcome_mismatch_floor` (0.1) and motor agency clears its own floor (`:238-244`). The CONTROL arm's *free-step* mismatch is 0.396 / 0.449 / 0.500 -- four to five times the attribution floor. So the integrator treats ordinary world-model prediction error as blocked agency, accumulates on essentially every free step, and pins at the cap with no block applied at all (`z_block_mean` 1.26-1.35 out of 1.5).

This is the sharp part: **C0 passed.** The comparator genuinely discriminates (blocked-step mismatch 0.997 vs free-step 0.40, margin 0.62). The integrator then throws that discrimination away, because its threshold sits below *both* conditions.

**The recorded `z_block_mean` does separate**, in the predicted direction, on 3/3 seeds -- and does so *under saturation*, so those values are a lower bound on a real effect, not a null.

## 3. Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | n/a | claim-free diagnostic |
| Biological reference | partial | frustrative-non-reward/RAGE analog is well-anchored; the failure is not a missing biological dependency |
| Prerequisites | present | SD-070 warmup + SD-056 contrastive both ran; C0 gate cleared |
| Implementation | partial | comparator discriminative; its consumer mis-scaled against it |
| Environment | adequate | all three controls behaved as designed |
| Measurement | **under-instrumented** | C1 built on the peak of a clamped integrator |
| Integration | coupled but unstable | comparator and integrator mis-scaled relative to one another |
| Scale | adequate | 2400 steps/arm/seed, ~1179 blocked steps per BLOCK arm |

**Failure-location (GOV-FAILLOC-1): MIXED -- `MECHANISM + MEASURES`.** Measurement is not adequate (saturating DV) and implementation is not complete (mis-calibrated floor), so **REE FAILED is not reachable** and is not asserted.

## 4. Arguments raised and withdrawn

Recorded so a later session knows these were tested, not overlooked.

1. **"The SD-070 P0a warmup was vacuous."** Its grounding-head holdout reports `balanced_accuracy 1.0` with `chance 1.0`, `lift 0.0`, `n_classes_scored 1`, on single-class labels. **Withdrawn:** the driver docstring anticipates exactly this -- on a `num_hazards=num_resources=0` warmup env the grounding heads "degrade gracefully to a trivial single-class fit ... without corrupting the reconstruction/anti-collapse terms". The functional test is C0, and C0 passed.
2. **"`z_goal_stream.writer_defect: true` means z_goal was dead."** **Withdrawn -- false positive.** The driver pins a constant goal deliberately (lines 225-227 assign `agent.goal_state._z_goal` directly) because goal-value is a held-constant control here; `active_frac` is 1.0 and `goal_state_present` is true. `writer_calls == 0` is correct behaviour for this design. Carried forward as a separate detector finding (section 6).

## 5. Learning extracted

- A readiness gate on the **comparator** does not license conclusions about the **consumer** of that comparator. Place readiness gates on the statistic the load-bearing criterion actually consumes.
- A criterion built on the **peak of a hard-clamped integrator** is degenerate whenever the clamp is reachable. Prefer a DV with headroom (mean, time-to-threshold, area under accumulation), or record the saturation fraction beside the peak.
- The degeneracy net did not fire despite the load-bearing DV being fully saturated in both arms. A **ceiling rail keyed to `z_block_cap`** on `z_block_peak` would have caught it.

## 6. Cross-cutting finding (bears on, not adjudicated here)

The `z_goal_stream` writer-defect detector cannot distinguish *"the driver omitted `update_z_goal`"* from *"the driver deliberately pins a constant z_goal as an experimental control"*. Both present as `writer_calls == 0` with `goal_state_present: true`. `pending_review.md`'s "Dead z_goal stream" section currently lists this run on that basis, and for this run the listing is a false positive. The published interpretation rule ("`active_frac` is NOT the signal ... `writer_calls == 0` is what separates the defect") does not hold against the direct-pin case.

## 7. Routing (proposed -- awaiting confirmation)

**`implement-substrate`**, new substrate entry `sd_blocked_agency_mismatch_floor_calibration`, priority 1, severity **`corrupting`**, path `ree_core/affect/blocked_agency.py`.

Make the attribution threshold relative to a running free-step mismatch baseline (or standardise the mismatch before thresholding), so the floor selects genuinely blocked steps. **Until that lands, no blocked-agency DV has dynamic range**, and re-running any z_block discrimination test is wasted compute.

Secondary, for whoever re-poses the test afterwards: replace the C1 peak statistic with a non-saturating DV, and add a ceiling rail on `z_block_peak`.

**Re-derive brake:** does not fire. Claim-free diagnostic, no `claim_ids` to count against; this reading is **not** `substrate_ceiling` and adds no ceiling hit to any claim.

**No fan-out recommendation:** the bottleneck routes to a single unambiguous build.

## 8. Recommended direction

`non_contributory`. MECH-353's `v3_pending` gate is **not cleared and not contradicted** -- the question was not reached.

## Adversarial red-team pass (Step 7c) -- NOT RUN

**No independent verifier ran, and no CONFIRMED verdict is claimed.** Step 7c calls for spawning a separate agent (preferably on a different model) to attack the conclusion. This session operates under a standing instruction not to invoke the Agent tool unless the user requests it, and the user did not.

The adversarial discipline was applied in-context instead, and it did change conclusions rather than rubber-stamping them -- six arguments were raised and withdrawn on direct code or docstring reads, each recorded under `arguments_withdrawn`. That is explicitly **weaker** than an independent pass: it shares the drafter's priors by construction, which is the exact property the pass exists to break.

**For governance:** treat every routing recommendation here as unverified by a second reader. The two highest-value targets for an independent check are V3-EXQ-963's claim that sampling starvation is refuted by the 779a comparison, and V3-EXQ-964's claim that C2 was mathematically unsatisfiable at `n_targets == 1`.
