# Failure Autopsy: V3-EXQ-821b (MECH-457, consummation binding)

**Generated:** 2026-08-08T16:39:36Z
**Scope:** single (diagnostic)
**Status:** confirmed (Step 8 interactive gate: user confirmed governance-close, no re-queue)

## 1. Facts

Run: `v3_exq_821b_mech457_consummation_binding_20260808T161718Z_v3`, `supersedes: V3-EXQ-821a` (which superseded V3-EXQ-821, 2026-07-25). `experiment_purpose: diagnostic`, `outcome: FAIL`, self-route label `consummation_binding_eroded_under_both`.

Design: two arms in the consummatory-act env (contact affords, distinct CONSUME action effects, consumption), both BC-installed at a calibrated dose (1200, up from 821's degenerate 300) then RL-refined under a fixed appetitive approach drive (`approach_coef=1.0`). Only `approach_extinguishes_on_contact` differs: `consumbind_extinct_off` (control, non-extinguishing) vs `consumbind_extinct_on` (treatment, extinguishes and hands off to CONSUME).

Readiness/preconditions all 9 green, no scoped-out failures. Anchors floor-achievable (local_view_greedy=34.17, greedy_oracle=42.8). **Usable install cleared** (the fix over 821): `post_bc_foraging_competence` worst-seed = 20.95 vs `USABLE_INSTALL_FLOOR=10.0` (821's degenerate 4.3-5.7, 14% of ceiling, is gone).

Result: both arms fully erode -- `retained_fraction=0.0` on all 3 seeds in both arms; post-RL `foraging_competence=0.0`; `goal_reach_rate=0.0`; trajectory peak never re-cleared the install floor in either arm. `C_extinguishing_drive_retains_installed_competence` (load-bearing) failed; `C_non_extinguishing_control_erodes_installed_competence` passed. Margin (on-off) = 0.0 < required 0.15.

**Self-route trustworthiness check.** Both arms erode to *exactly* 0.0 (total collapse), whereas the two confirmed process-family retention legs on the same reference config (V3-EXQ-788 scalar-critic control, V3-EXQ-792a unconstrained control) retained ~0.51-0.53 (partial erosion), not 0.0 -- a magnitude gap worth checking for an unaddressed confound. It is explained, not confounded: 788/792a carry no approach-primitive drive at all, while 821/821b's arms both carry `use_approach_primitive=True, approach_coef=1.0`, and V3-EXQ-781 already independently established (pre-registered, no retention framing) that this same drive at this coefficient earns strongly (~0.7-0.9) while suppressing forage to near-zero regardless of retention. The trajectory collapses from episode 250 onward (not gradual decay), and both arms' `mean_approach_reward_recent` (0.72-0.88) replicate 781's "approach without consummation" signature almost exactly. The self-route is read as substantively correct, distinct from the skill's canonical V3-EXQ-642 mislabel trap -- but the drive-magnitude axis itself is untested and is new territory the `competence_floor` growth-restriction (below) blocks from attaching here.

## 2. MECH-457 history digest

MECH-457 is the most heavily-autopsied claim in the corpus: 28 confirmed autopsy targets tag it. Categories under the R1-R3 convention: `competence_implementation_gap` 15, `standard` 7, `measurement_test_design_defect` 5, `substrate_starved_precondition_unmet` 1. **Zero `substrate_ceiling` hits, ever.** The claim decomposed 2026-07-22 (`/claim-synthesis`, user-approved) into MECH-475 (uninformative-value-baseline) and MECH-476 (retention-dissociable-from-acquisition), with MECH-457 retained as the narrowed umbrella (necessity, not sufficiency). The retention sub-question (`competence_floor` qid) was decided 2026-07-25 (`decision_log.v1.jsonl#2026-07-25T23:26:31Z`): process-family loci (value estimator/update constraint) set decay half-life; constitution-family loci (auxiliary-decay, consummation-binding) do not. 821's original consummation-binding read contributed to that decision but was later found instrument-broken (14% install) and reset `eliminated -> alive` on 2026-08-07 without un-deciding the question. 821b is the sanctioned recalibrated re-test of that one still-alive leg.

## 3. Claim-layer mapping

MECH-457 (`mechanism_hypothesis`, `status: candidate`, `implementation_phase: v3`, `v3_pending: true`, `granularity_debt_disposition: decomposed`). Asserts a dedicated RPE-driven actor-critic substrate is required (necessity, not sufficiency) for competent action learning. This run tests the narrow rival hypothesis H-consummation-binding, a dependency candidate *under* MECH-457's retention sub-question, not MECH-457 itself -- neither supports nor weakens the parent claim.

## 4. Biological-reference triage

Closest mammalian mechanism: Craig (1918)/Sherrington's ethological appetitive-consummatory distinction -- appetitive approach normally terminates in a consummatory act that resolves the drive, with satiety extinguishing the appetitive signal. Not a formal-definition import; well-established, textbook mechanism (no dedicated `targeted_review_consummation_binding` lit entry exists, a low-priority nice-to-have, not a blocking gap since the divergence read doesn't hinge on a citation).

The consummatory binding mechanism itself is present and functional (CONSUME wired, extinction knob active, demonstrator consummatory-aware); the installed foraging policy is simply not protected against the RL gradient regardless of that binding. The dependency this converges on is value-protection/consolidation (already independently confirmed by 788/792a as process-family), not consummatory binding -- a discovered non-dependency, itself informative.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | diagnostic; eliminates one rival dependency leg, not the parent claim |
| Biological reference | clear | Craig/Sherrington appetitive->consummatory; cleanly tested |
| Prerequisites | present | install cleared usable floor (20.95>=10.0) both arms, calibrated dose 1200 |
| Implementation completeness | complete | consummatory env + approach_extinction + reference policies landed 2026-07-25; 821a anchor-reachability bug fixed |
| Environment | adequate | anchors floor-achievable, resource retained until CONSUME |
| Measurement | adequate | 12 readings/cell, rate/tick added per 2026-08-07 audit fix |
| Integration | coupled but drive-dominated | mechanically works; approach-drive reward term (untested as an axis) appears to crowd out forage/consume regardless of extinction, replicating V3-EXQ-781's independent signature |
| Scale/capacity | adequate | collapse is immediate (by episode 250), not budget-starved |

## 6. Recommended epistemic_category / evidence_direction / evidence_quality_note

`epistemic_category: standard` (matches direct precedent `failure_autopsy_V3-EXQ-821_2026-07-25`; 0 substrate_ceiling hits, no reason to deviate). `evidence_direction: non_contributory` (per-claim MECH-457 -> non_contributory; rival-dependency elimination, not a parent-claim verdict).

> V3-EXQ-821b (H-consummation-binding, MECH-457 competence_floor retention leg, DIAGNOSTIC, non_contributory; supersedes V3-EXQ-821a [ERROR, anchor-threshold-unit bug] and V3-EXQ-821 [instrument-invalidated, 14%-install]): calibrated re-run (BC dose 1200, post_bc worst 20.95 >= USABLE_INSTALL_FLOOR 10.0 on both arms, foraging-rate DV added alongside composite per the 2026-08-07 instrument audit). Both the extinguishing (treatment) and non-extinguishing (control) arms erode installed competence to retained_fraction 0.0 on all 3 seeds (margin on-off = 0.0 < 0.15 required); neither arm's trajectory peak re-cleared the install floor. Anchors floor-achievable, criteria non-degenerate. H-consummation-binding ELIMINATED (re-confirms the pre-instrument-fix 821 reading, now on a valid instrument). Both arms replicate V3-EXQ-781's independent "approach-earned/forage-suppressed" signature regardless of extinction -- the deficit is upstream of the consummatory act; the approach-drive's reward weighting (held fixed, untested as an axis here) is the more plausible proximate driver of total (not partial) erosion. MECH-457 neither supported nor weakened; stays candidate/v3_pending. Converges the competence_floor retention sub-question fully: of the 4 originally-named retention mechanisms, 2 process-family loci (value estimator, update constraint) are CONFIRMED and 2 constitution-family loci (auxiliary-decay, consummation-binding) are ELIMINATED.

## 7. Recommended routing — CONFIRMED governance-close, no re-queue

**Re-derive brake: does NOT fire.** 0 confirmed `substrate_ceiling` hits for MECH-457 under R1-R3 across 28 tagged runs. No `implement-substrate` obligation.

`recommended_substrate_queue_entry.action: none` -- `mech457_consummatory_act` and the retention-trajectory probe instrumentation are already built and functioned correctly here. No `fanout_recommendation` -- this Mode-B resolve closes the last alive leg of an already-designed 4-leg portfolio; no live rival-hypothesis set remains open on this question.

**routing: governance** -- apply the resolution, close the leg. Do not re-letter this leg (821c) on the same axis; it is resolved cleanly with a replicated signature.

**Flagged but NOT routed by this autopsy** (growth-restriction gated, see below): whether the approach-drive's reward coefficient (held fixed at 1.0, untested as an axis) determines whether forage/consummation can compete with approach at all is a genuinely new candidate mechanism. Surfaced as a possible follow-on for the user/governance to weigh via a new `qid`, not chipped or attached here.

## 8. Growth-restriction check — HARD STOP, respected

`competence_floor` (the qid `H-consummation-binding` belongs to) carries a non-empty `growth_restriction` set 2026-08-08 (`competence_floor_recurrence_repose_2026-08-08.md`):

> "CLOSED TO FURTHER FAN-OUT (2026-08-08, competence_floor_recurrence_repose_2026-08-08.md, chip-20260808-competence-floor-refpose). This qid accumulated 5 labelled GOV-FANOUT-1 portfolios (denominator 7 -> 20) before its own standing rule ... was checked against a real case. ... a claim whose depends_on includes MECH-457, MECH-459, MECH-460, MECH-475, or MECH-476, and whose first /failure-autopsy would otherwise grow competence_floor by Step 9b's claims+theme matching, should instead pre-register its OWN qid -- UNLESS the specific mechanism under test targets an axis family this qid's decision block still lists as undecided (there is currently none). ... **The one still-alive leg, H-consummation-binding, is not an exception -- it is complicated (buildable) work (a probe-function fix + one calibrated re-run), not a discrimination, so it does not need or license a sixth portfolio.**"

**Disposition:** this run is a pure Mode B resolve of the already-pre-registered `H-consummation-binding` hid (registered 2026-07-18, `pre_registered_utc` already <= this run's `resolved_utc`) -- it does not attach a new hypothesis or grow the denominator, and the restriction text itself explicitly pre-blesses exactly this resolution path. **No STOP applies to resolving this leg.** The STOP does apply prospectively: any follow-on hypothesis about approach-drive reward magnitude must not be attached here -- it needs a new `qid` (all five named families already carry a resolved answer).

## 9. Learning extracted

- H-consummation-binding is re-confirmed ELIMINATED on a validated instrument: extinguish-and-hand-off binding does not rescue installed competence from erosion under RL refinement, replicating the pre-instrument-fix 821 read.
- The magnitude of erosion (total vs the process-family legs' partial ~0.5) is not itself evidence of an unaddressed substrate defect -- explained by the approach-primitive drive's own known crowding-out effect (V3-EXQ-781), present identically in both 821b arms and absent from 788/792a's comparison arms.
- The competence_floor retention sub-question is now fully resolved on all 4 originally-named mechanisms (2 confirmed process-family, 2 eliminated constitution-family) -- the campaign converged, and its growth_restriction correctly anticipated and pre-authorized exactly this closing move while blocking further fan-out.
- The approach-drive reward-coefficient axis is a plausible next candidate mechanism but is explicitly out of scope for `competence_floor`; any follow-on needs a fresh qid, a user/governance decision.

## 10. Hypothesis-space ledger (Step 9b) — see companion registry edit

This autopsy performs a **Mode B resolve** of the pre-registered `H-consummation-binding` hid under the `competence_floor` qid in `hypothesis_space_registry.v1.json` (registered 2026-07-18, well before this run). No fan-out, no discovery growth, no denominator change. See the registry diff landed alongside this artifact; `check_hypothesis_space_integrity.py` was re-run after the edit and reports no new flags attributable to this change.
