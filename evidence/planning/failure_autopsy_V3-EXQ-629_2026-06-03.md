# Failure Autopsy -- V3-EXQ-629 (2026-06-03)

**Scope:** single
**Status:** confirmed (interactive gate answered 2026-06-03)
**Generated:** 2026-06-03T06:13:09Z
**Session:** failure-autopsy-629-20260603T061309Z

Target: `v3_exq_629_mech342_ecological_maintenance_release_evidence_20260602T225839Z_v3`
(queue_id V3-EXQ-629). MECH-342 maintenance-time commitment-release -- the ECOLOGICAL
evidence complement the 2026-06-02 /governance disposition required before MECH-342
can advance past candidate / v3_pending. The 592g diagnostic probe (PASS, all six
criteria) is the predecessor (NOT superseded).

---

## 1. Facts reconstruction

- outcome FAIL; evidence_direction `non_contributory`; `claim_ids = []`; experiment_purpose=evidence; diagnostic_outcome `NO_NATURAL_COMMITMENT`.
- 2 arms (ARM_0_RELEASE_OFF / ARM_1_RELEASE_ON); commit-entry gating identical across arms (R-c conjunction + commit_readiness gate); the only manipulated variable is `use_maintenance_release`.

Acceptance:
| Criterion | Result | Evidence |
|---|---|---|
| C1 baseline_commits (non-vacuity) | **FAIL** | all commit counts 0; `n_commit_entries = 0`, `beta_elevated_occupancy = 0.0` in both arms, both windows |
| C2 degradation_occurred (C0 guard) | pass (vacuous) | off_degraded_ticks 6782 > 10 -- but counted via `committed_pointer` (always 1.0), not beta-elevated commitment |
| C3 release_authority (core) | FAIL | `on_degraded_decommit_transitions = 0`, `on_degraded_mech342_fires = 0` |
| C4 no_false_abort | pass (vacuous) | no commitment, no abort |
| C5 distinct_from | FAIL (vacuous) | `on_degraded_beta_releases = 0`, `mech342_fired_in_on_degraded = false` |

**Failed criterion type: absolute / non-vacuity baseline (C1).** The experiment could not establish the precondition (natural commitment) the mechanism operates on.

**Root cause (single, decisive):** the MECH-090 R-c admission gate is an AND of (score_margin decisiveness >= 0.05) AND (nav_competence >= nav_floor 0.3).
- nav axis is FINE: `mean_nav_proxy = 0.99995`, `nav_below_floor_ticks = 0` -- never degraded.
- decisiveness axis is DEGENERATE: `mean_score_margin = 0.00074` (~70x below the 0.05 admission floor), `margin_below_floor_ticks = ALL ticks`, **identical in healthy and degraded windows** (0.00074 vs 0.00074).

The agent's E3 candidate scores are nearly tied, so it is never decisive enough to commit. `committed_pointer_occupancy = 1.0` is a red herring -- it tracks the E3 `_committed_trajectory` pointer (set once any trajectory is proposed), NOT the beta-elevated commitment state MECH-342 acts on (which is 0 throughout).

**Two compounding harness gaps:**
1. **Commitment never forms** (primary) -- score_margin decisiveness ~0 < admission floor, so MECH-090 admission never fires.
2. **Degradation driver inert** (secondary) -- `max_running_variance = 3.9e-5` (barely moved), so nav_proxy stayed ~1.0; the script flags the env-side auto-drive of commit_readiness as "a Phase-2 substrate follow-on not yet wired." This only bites once gap #1 is fixed.

The script's interpretation grid has **no C1-FAIL cell** -- it pre-supposed commitment would form (C2/C3/C4/C5 cells assume C1 holds). So the run hit an un-anticipated state.

---

## 2. Claim-layer map

- MECH-342 [mechanism_hypothesis, candidate, v3_pending] -- maintenance-time release; depends_on MECH-090; substrate_queue status `implemented_validated_v3_exq_592g`. The 2026-06-02 governance disposition required an ecological evidence-grade run before promotion past the v3_pending gate. 629 was that run.
- `claim_ids = []` on the manifest -- so 629 carries **no governance weight on any claim** regardless of outcome. The autopsy's value is the learning + routing, not protecting a claim weight.

**Did the experiment test the claim under conditions where it could express itself?** **No.** MECH-342 releases an already-elevated beta commitment; the agent never commits, so MECH-342 is untestable here. NOT a falsification.

---

## 3. Biological-reference triage

- MECH-342 closest mechanism: motor-program-timescale commitment maintenance / release (Resulaj 2009 drift-to-bound; Cavanagh/Frank 2011 conflict-scaled; Falasconi 2025 / Wessel 2022 selective vs non-selective movement cancellation). Biology supports the *class* (committed motor programs are released under accumulating deficit). Not exercised here -- no commitment formed.
- The blocking signal -- E3 candidate-score decisiveness (score_margin) -- maps to the decision-confidence / value-margin that gates commitment onset (LIP/PFC ramping to a decision bound). A persistently ~0 margin resembles an agent whose option values are undifferentiated, i.e. no committable decision ever forms. lit_status: present (MECH-090 / commitment lineage).
- is_formal_import: n/a for this FAIL -- it is a harness precondition failure, not a claim divergence.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (protected) | mechanism untestable -- precondition (commitment) never formed |
| Biological reference | clear (untested) | commitment-release class is biologically grounded; not exercised |
| Prerequisites | **missing -- precondition** | natural beta commitment is the precondition; score_margin decisiveness never reaches the admission floor |
| Implementation completeness | complete (MECH-342) / partial (harness) | MECH-342 substrate landed + 592g-validated; harness lacks a working commitment-induction and an effective degradation driver |
| Environment adequacy | **wrong pressures** | ecological env produces undifferentiated E3 scores (margin ~0) and a near-zero running_variance perturbation |
| Measurement adequacy | adequate | metrics correctly captured the no-commitment state; the C1 non-vacuity guard did its job |
| Integration adequacy | isolated | maintenance-release branch never reached (no beta latch to release) |
| Scale / capacity | unknown | not reached |

Dominant diagnosis: **test-design / harness precondition failure** -- natural commitment cannot form because E3 score_margin decisiveness is degenerate in the ecological regime, compounded by an inert degradation driver. Recommended epistemic_category: `measurement_test_design_defect` (non-vacuity / precondition).

---

## 5. Learning extracted

1. **Ecological MECH-342 validation is blocked on a missing precondition:** the agent never naturally commits because E3 score_margin (decisiveness) sits at ~0.0007, ~70x below the 0.05 admission floor, in every window. The MECH-090 admission AND fails on the decisiveness axis (nav axis is fine).
2. **The score_margin degeneracy is a recurring E3-selection-landscape signal** -- a different facet of the same family as 604a/624a (modulatory bias cannot move selection) and the z_goal salience gap (603e/626a/622). Here the candidate scores are too *undifferentiated* for decisive commitment. Connects to the existing `MECH-341` substrate entry ("E3 score diversity preservation retune"). Watch item, not a new substrate write this autopsy.
3. **The degradation driver is inert** (running_variance max 3.9e-5; env-side commit_readiness auto-drive is an unwired Phase-2 follow-on) -- a second harness gap that only matters once commitment forms.
4. **MECH-342 is not falsified and carries no claim weight here** (`claim_ids = []`); it stays `implemented_validated_v3_exq_592g`, ecological validation **blocked** pending a harness that produces natural commitment.

---

## 6. Repair pathway / routing (confirmed at gate)

**Route: `/queue-experiment` redesign (629b -- same scientific question, alphabetic suffix).** The redesign must:
- Establish a real commitment precondition -- either calibrate `score_margin_floor` to the env's natural decisiveness distribution (the 0.05 floor was set against the 592g controlled-probe values, not the ecological E3 score_margin distribution), OR use a commitment-inducing curriculum / scenario that produces decisive margins. Add an explicit C1-FAIL interpretation cell.
- Fix the degradation driver -- wire the env-side commit_readiness auto-drive (the named Phase-2 follow-on) and/or raise `DEGRADE_INTENSITY_SCALE` and lengthen the degraded window so nav_competence genuinely drops below floor mid-commitment.
- Keep the distinct-from controls (use_harm_stream=False, V_s OFF, ghost-goal OFF) so a release remains attributable to MECH-342.

**Cross-link (watch, no write):** flag the score_margin decisiveness degeneracy to `/governance` as related to `MECH-341` (E3 score diversity retune) and the new `modulatory-bias-selection-authority` entry from the 604a/624a autopsy -- if the ecological E3 cannot produce committable margins even after recalibration, that becomes a substrate question.

### Draft evidence_quality_note text (for governance -- do not write here)

> V3-EXQ-629 (2026-06-03 autopsy): outcome FAIL, NO_NATURAL_COMMITMENT (C1 non-vacuity fail). The agent never naturally commits -- mean_score_margin 0.00074 is ~70x below the MECH-090 admission floor 0.05 in every window (nav axis fine at ~1.0), so the R-c admission AND never fires and there is no beta latch for MECH-342 to release. Compounded by an inert degradation driver (running_variance max 3.9e-5; env-side commit_readiness auto-drive unwired). NOT a MECH-342 falsification; claim_ids=[] so no claim weight. MECH-342 stays implemented_validated_v3_exq_592g, ecological validation BLOCKED. epistemic_category measurement_test_design_defect. Redesign queued (629b: establish commitment precondition -- recalibrate score_margin_floor or commitment-inducing curriculum -- AND fix the degradation driver). Score_margin degeneracy cross-linked to MECH-341 as an E3-selection-landscape watch item.
