# Failure autopsy -- V3-EXQ-1067 (v3_exq_1067_mech266_squash_vs_clamp_cap_sweep_20260925T161024Z_v3)

- Generated: `2026-09-26T10:19:36Z` | Status: **confirmed** (2026-09-26T10:43:53Z, user at /failure-autopsy Step 8 interactive gate (session failure-autopsy-20260926-batch7))
- Batch: failure-autopsy-20260926-batch7 (V3-EXQ-1105a/1067/1106/1107/1099/1104/1090)
- Claims: MECH-266, SD-032a
- Recommendation ledger: rec-20260926-614b94c8
- Dry-run gate: scripts/check_dry_run_citations.py run over all 7 2026-09-25 diagnostic run_ids of this batch: 0 dry, 7 clean.

## 1. Self-route and failed criterion

Self-route `occupancy_responds_but_never_grades_bang_bang_persists`; failed criterion: **discrimination**.

Does the self-route hold? partially -- the outcome traces, but (a) the null_meaning's item-2 latch residual is unsupported (et_drive_saturated_frac 0.0 on every cell), (b) the attribution machinery mislabels a gain cut as gradedness (the control targets the wrong signal), and (c) the grid cannot resolve the transition for any bounded operator. The driver's pre-registered SD-032a 'weakens' for this branch is overridden.

## 2. Facts (re-measured from the flat manifest and driver)

- **H_squash_graded**: longest adjacent qualifying run 1 (need 2): squash reaches 3/3-seed mixed occupancy at cap 1.0 -- the best cell in the lineage -- but 1/3 at 0.75 and 0/3 at 1.25..1.75. Near-miss by one grid step on a 0.25 grid.
- **clamp_baseline**: 0 qualifying caps (934 reproduced); gain-matched clamp 0
- **operator_bite**: external_task_drive is ~dead in eval (et_drive_mean 0.00053), so the external_task logit is external_task_bias plus ~0 and the cap-vs-bias comparison IS the regime switch. dacc_pe exceeds the cap on 100% of ticks (abs max 11.2). RED-TEAM RECOMPUTE: fitting the clamp margin as a line in cap and evaluating it at the squash's effective cap c_eff = c*v/(c+v) reproduces the squash margin to +-0.002 on seeds 42/44 (+0.008..0.021 on 43): the squash arm is the clamp arm with the cap rescaled by 0.85-0.93 -- a pure GAIN cut on dacc_pe, not gradedness. The gain-matched control targets the drive (derived at e=1), not dacc_pe, so its margin equals the baseline clamp's to 4 decimals: it controlled the wrong signal.
- **occupancy**: moves between arms (occ_shift_gradedness 0.129 vs gain 0.005), so the operator changes WHICH regime the register lands in, but does not produce a graded window across caps
- **precondition_weakness**: external_task_drive_signal_nonzero reads met 3/3 on a per-seed MAX over cells while the eval mean drive is 0.0005 -- it cannot distinguish a live drive from a near-dead one
- **provenance**: Ran on the Mac from ~2026-09-20 13:30Z for 122.7 h (9.7x its 760-min estimate). The run predates 1fc881692d (freeze no-op UP -> STAY, 2026-09-25 09:33Z) and ran WITHOUT it (Python does not reload imported modules); the recorded commit 0a3169c (committed 15:57Z, 13 min before manifest write) is not the code that ran (substrate_identity manifest_write_disk_read, 1 snapshot; driver never called pin_recording_substrate). With use_pag_freeze_gate on and a trained harm stream, under pre-fix code a frozen agent walks UP; GFLAG-0508 lists 1067 as straddling the fix, so the 3/3 contact guard may be an UP-walking artefact.
- **sticky_arm**: ARM_ASYM_STICKY_TASK saturated_bimodal at every cap under every operator -- MECH-266's own arm again not exercised
- **grid**: The occupancy transition is ~0.2 effective-cap units wide (occ 0.97 at c_eff 0.70 -> 0.01-0.52 at 0.91-1.0 -> 0.0 at 1.1). A 0.25 grid cannot place two adjacent points inside it under ANY operator whose output is ~k*cap for v >> sigma: the load-bearing gate discriminates effective-cap placement, not operators. The 'best cell' (squash cap 1.0, 3/3 mixed) is the clamp at effective cap 0.91.

## 3. Four-layer diagnosis

| Layer | Reading |
|---|---|
| claim_alignment | n/a for both -- the run tests mode-governance-engagement item (1) (the bounding operator). SD-032a specifies a DISCRETE operating-mode register (its functional_restatement), so a register that stays bang-bang is SD-032a behaving as written; MECH-266's arm is saturated and unexercised. |
| biological_reference | partial -- divisive normalisation (Carandini & Heeger 2012; Louie et al.) is the biological gain-control form; lit present (targeted_review_salience_gain_normalisation and siblings). A fixed-sigma squash is a formal saturating nonlinearity, not normalisation: it is not scale-free, and that divergence is exactly what bit here. |
| prerequisites | partial -- contact guard 3/3, but the run executed pre-STAY-fix code with the freeze gate on (GFLAG-0508): the guard may reflect UP-walking. |
| implementation | complete -- the squash did exactly what a saturating bound does (output ~0.9*cap on an input 5-11x sigma). |
| environment | adequate for the question. |
| measurement | misleading -- the gain-matched control targets the external_task drive (~0 in eval) instead of dacc_pe, so the gain/gradedness decomposition mislabels a gain cut as gradedness; the 0.25 grid is coarser than the ~0.2-wide transition; the drive-signal precondition is a max-over-cells check that cannot see a near-dead drive; the recorded substrate is not the code that ran. |
| integration | coupled -- the operator acts on the input it receives; the defect is in the design's control and grid, not a missing link. |
| scale | insufficient resolution -- 0.25 cap grid vs a ~0.2-wide transition. |

**Failure location (GOV-FAILLOC-1):** mechanism established, measures not_established, environment partial, REE failed: False. Net: MEASURES (mis-targeted gain control, grid coarser than the transition, wrong provenance) + ENVIRONMENT (pre-fix freeze-gated harness, GFLAG-0508), not chargeable to REE.

## 4. Biological reference

divisive normalisation of salience inputs (Carandini & Heeger 2012) -- divergence: fixed-sigma squash is not scale-free; biology normalises by pooled activity; lit: present.

## 5. Recommendations

- evidence_direction: `non_contributory`; epistemic_category: `standard` (note: operator-level diagnostic; register discreteness is SD-032a's specification; MECH-266 arm unexercised)
- **MECH-266**: change `STANDS`; none -- stays provisional; pending_retest_after_substrate stays true
- **SD-032a**: change `manifest evidence_direction_per_claim SD-032a weakens (driver attribution-table stamp) overridden -> non_contributory`; none -- stays stable
- Substrate queue: ```{
 "action": "amend",
 "target_sd_id": "mode-governance-engagement",
 "note": "bookkeeping amend only -- NO build instruction. Record the failure, and refresh depends_on_unresolved (still names only V3-EXQ-935).",
 "failure_record_entry": {
  "run_id": "v3_exq_1067_mech266_squash_vs_clamp_cap_sweep_20260925T161024Z_v3",
  "experiment_type": "v3_exq_1067_mech266_squash_vs_clamp_cap_sweep",
  "metric": "squash longest adjacent graded run 1/5 caps; squash margin == clamp margin at effective cap c*v/(c+v) (+-0.002 on 2/3 seeds), i.e. a gain cut; gain-matched control inert (targets drive, et_drive_mean 0.0005); transition ~0.2 effective-cap wide vs 0.25 grid",
  "target": ">=2 adjacent graded caps on >=2/3 seeds on a grid finer than the transition, on post-STAY-fix code",
  "resolved": "open"
 }
}```
- Re-derive brake: {'fired': False, 'threshold': 2, 'note': 'per-claim category standard for both claims -> this target does not count (R3 per-claim branch); lineage count stays 7, released for a different-mechanism operator build'}

## 6. Routing

**queue-experiment** -- complex (probe-gated) / puzzle: the operator question is not answered and cannot be at this grid. Next is a finer CLAMP-only sweep over cap 0.70-1.00 in 0.05 steps (or a continuous occupancy-vs-margin readout) on post-STAY-fix code, with the freeze-gate question settled first (GFLAG-0508). NOT an H4 normaliser build: nothing here separates gain from gradedness, and a normaliser would move the same transition to effective cap ~cap/2 and meet the same grid problem. New EXQ number (different design question: where is the transition).


## 7. Hypothesis-space ledger (Step 9b)

```
{
 "qid": "mech266_mode_arbitration_saturation",
 "growth_restriction": null,
 "mode": "B (basis addenda; no state change)",
 "H1-cap-miscalibration": "append V3-EXQ-1067 to resolving_runs; state alive; basis addendum: the squash arm equals the clamp at effective cap 0.85-0.93x; the regime transition is ~0.2 effective-cap wide, narrower than the 0.25 grid -- consistent with H1 / grid too coarse",
 "H4-clip-not-normalisation": "append V3-EXQ-1067; state alive; basis addendum: untested -- a fixed-sigma squash acted as a gain cut; this run cannot separate gain from gradedness",
 "H3-instrument-illposed": "append V3-EXQ-1067; state alive; basis addendum: another instance of the family -- the gain-matched control targeted the drive, not the input the operator bites on",
 "h_other": "not fired"
}
```

## 8. Learning extracted

- A gain-matched control must match gain on the input the operator actually bites on; here it matched the (dead) drive.
- A saturating operator on inputs far above sigma is a gain cut, not a grader; check the input's scale against sigma before attributing gradedness.
- A discrete cap grid coarser than the regime transition cannot show a graded window for any bounded operator.
- The pre-written null_meaning named a residual (the item-2 latch) that never fired; check a null's story against the run.
- Long runs need substrate identity pinned at process START (pin_recording_substrate).

**Cross-run read:** Cross-run read (this batch): the dACC/harm-affect signal scale is unnormalised and inflates with training (1067 dacc_pe 6-11 vs cap <=1.75; 1107 dacc_pe up 36-53x and ||z_harm_a|| 9-13x; 1104 effort term 3-4 orders below the payoff range; V3-EXQ-1089 pe_unsat p50 2.1-5.6 across seeds). Fixed-constant operating points in the SD-032 family are set against a scale that moves by an order of magnitude. Observation only, bears on dec-20260923T185804-MECH-268; not a build recommendation from this run.

## 9. Checks

- Step 7b pre-routing checks: no fires
- Step 7c red-team (Step 7c red-team run on fable (cross-model; drafter opus)): {'model': 'fable', 'verdict': 'CONTESTED', 'applied': 'squash = gain cut (recompute adopted); H4 build routing withdrawn -> finer clamp sweep; ledger addenda reworded; pre-STAY-fix / GFLAG-0508 caveat added; provenance and SD-032a override confirmed', 'file': 'redteam_B.md'}

Granularity-debt recurrence trigger: does NOT fire (no target in any of this run's claim clusters reads `weakened` with structurally different signatures attributable to this run; this run's own claim_alignment is n/a / could-not-express).
