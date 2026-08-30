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

**Why the control arm saturates.** `blocked_agency` accumulates whenever `outcome_mismatch >= outcome_mismatch_floor` (0.1) and motor agency clears its own floor (`:238-244`). The CONTROL arm's *free-step* mismatch is 0.384 / 0.462 / 0.493 -- four to five times the attribution floor. (The BLOCK arm's free-step values are 0.396 / 0.449 / 0.500; an earlier revision of this line quoted those by mistake while attributing them to CONTROL. The argument is unaffected -- both arms' free steps sit far above the 0.1 floor, which is the point -- but the attribution was wrong.) So the integrator treats ordinary world-model prediction error as blocked agency, accumulates on essentially every free step, and pins at the cap with no block applied at all (`z_block_mean` 1.26-1.35 out of 1.5).

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

Make the attribution threshold relative to a running free-step mismatch baseline (or standardise the mismatch before thresholding), so the floor selects genuinely blocked steps. **Until that lands, every blocked-agency DV is compressed below its own pre-registered margin** -- note this is deliberately weaker than "no dynamic range": `z_block_mean` demonstrably does separate, 3/3 seeds, even under saturation. Re-running any z_block discrimination test before the floor is recalibrated is wasted compute.

Secondary, for whoever re-poses the test afterwards: replace the C1 peak statistic with a non-saturating DV, and add a ceiling rail on `z_block_peak`.

**Re-derive brake:** does not fire. Claim-free diagnostic, no `claim_ids` to count against; this reading is **not** `substrate_ceiling` and adds no ceiling hit to any claim.

**No fan-out recommendation:** the bottleneck routes to a single unambiguous build.

## 8. Recommended direction

`non_contributory`. MECH-353's `v3_pending` gate is **not cleared and not contradicted** -- the question was not reached.

## Adversarial red-team pass (Step 7c) -- VERDICT: CONFIRMED

An independent verifier (different model, given the JSON conclusion and raw evidence with this session's reasoning withheld until it had recomputed from the cells) attacked this diagnosis and could not refute it.

**Independently reproduced:** `z_block_peak` = 1.5 in both arms on all 3 seeds, separation 0.0000 per seed recomputed by hand; the clamp is a hard `min(c.z_block_cap, ...)` at `ree_core/affect/blocked_agency.py:257` (cap 1.5 at `:114`, confirmed at the run's own commit `1a0be594`), applied to exactly the value the driver's peak statistic reads (driver `:387-388`, `:403`). `z_block_mean` separations +0.165 / +0.121 / +0.083 confirmed.

**The counter-hypothesis this autopsy could not test was refuted by the verifier, using the control arm's own cells.** The attribution gate has a *second* condition (`motor_agency >= attribution_motor_floor`, 0.5) which could in principle have been the real driver. But CONTROL reached `z_block_mean` 1.26-1.35 with **zero** blocked steps, which is arithmetically possible only if all three gate conditions held on the bulk of free steps. The mismatch floor is the gate meant to discriminate blocked from free, and it discriminated nothing.

**Both withdrawals were independently judged correct.** The SD-070 withdrawal rests on the functional C0 pass rather than on trusting the docstring; the z_goal withdrawal is clinched empirically -- with `require_goal_active=True`, z_block could not have accumulated at all had the pinned goal been inactive.

**Routing independently checked:** no existing `substrate_queue` entry covers floor calibration (SD-031 covers the comparator and is implemented), no 642b is queued, and a measurement-only redesign would leave a regulator asserting blocked-agency 1.26 in a zero-block condition -- semantically broken for every consumer, including decommit (bound 1.0, continuously exceeded in both arms).

**Correction the verifier forced (applied above):** section 2 previously quoted 0.396 / 0.449 / 0.500 as CONTROL's free-step mismatch; those are the BLOCK arm's. CONTROL is 0.384 / 0.462 / 0.493.

**Also flagged, and worth a successor's attention:** C3's PASS is *differentially uninformative* -- its no-suffering conjunct is vacuous by environment construction (`num_hazards=0`) and both arms carried identical cap-saturated assert bias. This autopsy does not lean on C3, but a successor must not cite it as evidence.

**Not checkable by either party:** per-step `motor_agency` is unrecorded and was inferred arithmetically; the run's tree was dirty in `agent.py`/`config.py`, though `blocked_agency.py` was clean against the run commit and the conclusion is insensitive to whichever floor value actually executed (CONTROL saturation proves it sat below the ~0.38 free baseline).
