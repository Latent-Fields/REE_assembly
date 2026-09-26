# Failure autopsy -- V3-EXQ-1104 (v3_exq_1104_sd032b_effort_proxy_validation_20260925T202059Z_v3)

- Generated: `2026-09-26T10:19:36Z` | Status: **confirmed** (2026-09-26T10:43:53Z, user at /failure-autopsy Step 8 interactive gate (session failure-autopsy-20260926-batch7))
- Batch: failure-autopsy-20260926-batch7 (V3-EXQ-1105a/1067/1106/1107/1099/1104/1090)
- Claims: (claim-free)
- bears_on: substrate_queue:sd032b-candidate-effort-proxy, GFLAG-0447
- Recommendation ledger: rec-20260926-614b94c8
- Dry-run gate: scripts/check_dry_run_citations.py run over all 7 2026-09-25 diagnostic run_ids of this batch: 0 dry, 7 clean.

## 1. Self-route and failed criterion

Self-route `effort_proxy_live_scale_inert`; failed criterion: **discrimination**.

Does the self-route hold? yes on the arithmetic; the routing gloss 'calibration, puzzle (known rules)' is NOT adopted -- see routing

## 2. Facts (re-measured from the flat manifest and driver)

- **C1_liveness**: effort spread > 0 on 100% of fresh ticks, 3/3 seeds (PASS)
- **C2_argmin_responsive**: best-cost flip fraction 0.0024 / 0.0 / 0.0 (need >=0.05 on 2 seeds). ONE flipping tick in 1,504 (seed 42, cost 10, an episode-start tick). FAIL
- **C2_default_cost_0.1**: reach never exceeds the top-2 gap on any tick in any seed -> degenerate at the shipped default
- **scale**: effort_term_range 0.005-0.031 vs payoff_range 15.8-161 (3-4 orders of magnitude); reach > gap 0.0% @0.1, 0.3% @1, 2.3% @10, mostly step-0 ticks where pe is 20x the mid-episode value
- **controls**: positive 1.0, negative 0.0, counterfactual fidelity 1.0 on every seed -- the instrument is clean
- **E2_harm_a_validity**: skill_vs_persistence -40.8 / -51.9 / -79.5 -- SD-PP-B9 reproduced in-run: the per-candidate effort spread is largely forward-model error
- **process**: GFLAG-0447 (open, raised 2026-09-24T07:19Z) was NOT carried: the user launched IGW-20260923-222 manually and interactively at 2026-09-25T06:18:32Z (igw_routine_log.md:3658, REQUIRES_HUMAN_SKILLS; WORKSPACE_STATE 06:56Z 'running interactively (user)'), before the 18:00Z re-raise the hold named; the build (4cce9b8, 07:34Z) and this validation followed. The defect is an uncarried open design flag inside a user-assented early launch, not a build against a standing hold. The queue note cites GFLAG-0507 but never GFLAG-0447.

## 3. Four-layer diagnosis

| Layer | Reading |
|---|---|
| claim_alignment | n/a -- claim-free substrate validation (sd032b-candidate-effort-proxy). SD-032b's EVC design intent is not tested: the run asks whether this producer can move the argmin at all. |
| biological_reference | partial -- Shenhav 2013 EVC (payoff - control x effort cost) and Croxson 2009 (dACC encodes reward x effort interaction), targeted_review_mcc_effort_value present. The divergence is load-bearing: biology treats effort as a first-class cost variable decoupled from harm (MECH-354); this producer derives 'effort' from a HARM forward model already charged by E3's harm channels (GFLAG-0447). |
| prerequisites | partial -- a trained E2_harm_a was present but is worse than persistence (SD-PP-B9), so the per-candidate spread is not a validated effort signal. |
| implementation | partial -- coupled but inert by DEFECT (neutralising default): at dacc_effort_cost 0.1 the term cannot reach the top-2 gap on any tick. The fix is NOT a larger cost constant: scaling a model-error term until it dominates E3 selection would make selection noise-driven. |
| environment | partial -- P2 lives end by health depletion in 3-10 steps; per-seed action collapse (e.g. seed 43 [0,3585,751,0]). |
| measurement | adequate -- within-tick counterfactuals with positive, negative and fidelity controls all perfect; per-tick-class reporting. |
| integration | coupled but inert -- missing link: neutralising default (cost scale); the deeper gap is a producer-validity question, not wiring. |
| scale | adequate for the question (425-558 fresh ticks per seed). |

**Failure location (GOV-FAILLOC-1):** mechanism partial, measures established, environment partial, REE failed: False. Net: MIXED (MECHANISM inert-by-scale on an unvalidated producer + ENVIRONMENT short lives), not chargeable to REE.

## 4. Biological reference

dACC Expected Value of Control (Shenhav 2013); reward x effort interaction (Croxson 2009) -- divergence: effort derived from a harm forward model (double-counts harm; contradicts MECH-354; pre-empts Q-080); lit: present.

## 5. Recommendations

- evidence_direction: `non_contributory`; epistemic_category: `standard` (note: claim-free substrate validation; inert-by-scale on an unvalidated producer)
- Substrate queue: ```{
 "action": "amend",
 "target_sd_id": "sd032b-candidate-effort-proxy",
 "status_note": "stays implemented_pending_validation -- do NOT mark validated",
 "failure_record_entry": {
  "run_id": "v3_exq_1104_sd032b_effort_proxy_validation_20260925T202059Z_v3",
  "experiment_type": "v3_exq_1104_sd032b_effort_proxy_validation",
  "metric": "argmin flip fraction across 7 forced f_sat values: 0.0024/0.0/0.0 at best cost (need >=0.05 on 2/3 seeds); 0.0 at default cost 0.1, where reach never exceeds the top-2 gap; effort_term_range 0.005-0.031 vs payoff_range 15.8-161; E2_harm_a skill_vs_persistence -41..-80",
  "target": "argmin responsive (>=0.05 flip fraction) on a VALIDATED effort producer that is not a harm quantity, per GFLAG-0447",
  "resolved": "open"
 },
 "resolves_prior_failure_record": [],
 "note": "Closes the OPEN argmin-responsiveness half of the pre-build failure_record item with a negative. The next step is the GFLAG-0447 design decision, not a cost re-sweep."
}```
- Re-derive brake: {'fired': False, 'threshold': 2, 'note': 'claim-free'}

## 6. Routing

**governance** -- complex (probe-gated) / mystery (known data): the data are in; what is missing is the design decision GFLAG-0447 asks for (what 'effort' means; a producer not already charged by E3's harm channels). REFUSE a same-question cost re-sweep: raising dacc_effort_cost until the term competes would hand selection to E2_harm_a model error. This explicitly OVERRIDES the substrate entry's own implementation_note, which prescribes exactly that cost re-sweep ('a cost/bias setting that puts the effort term on the payoff's scale').


## 7. Hypothesis-space ledger (Step 9b)

No registered question names this run or its claims and no fan-out was emitted: nothing to register.

## 8. Learning extracted

- Liveness is not validity: a per-candidate spread from a forward model worse than persistence moves nothing and would mean nothing if it did.
- A shipped default at which the manipulation cannot reach the decision gap is a neutralising default -- degenerate, not a null.
- Process: an open design flag (GFLAG-0447) was not carried into a user-launched early build or its validation queue note; open flags on a substrate item should travel with every launch of it.

**Cross-run read:** Cross-run read (this batch): the dACC/harm-affect signal scale is unnormalised and inflates with training. 1067: dacc_pe exceeds the affinity cap on 100% of ticks (abs max 11.2 vs cap <=1.75). 1107: dacc_pe grows 36-53x and ||z_harm_a|| 9-13x init->final. 1104: the effort term sits 3-4 orders of magnitude below the E3 payoff range. Same-day V3-EXQ-1089: pe_unsat p50 spans 2.1-5.6 across seeds. Every fixed-constant operating point in the SD-032 family (cap, sigma=cap, effort cost, saturation floor) is set against a scale that moves by an order of magnitude between seeds and across training. Bears on dec-20260923T185804-MECH-268 (normalising dacc_pe).

## 9. Checks

- Step 7b pre-routing checks: no fires
- Step 7c red-team (Step 7c red-team run on fable (cross-model; drafter opus)): {'model': 'fable', 'verdict': 'CONTESTED (process fact only; science and routing confirmed)', 'applied': "process fact reworded (user-assented early launch, uncarried flag); explicit override of the entry's own re-sweep prescription", 'file': 'redteam_A.md'}

Granularity-debt recurrence trigger: does NOT fire (no target in any of this run's claim clusters reads `weakened` with structurally different signatures attributable to this run; this run's own claim_alignment is n/a / could-not-express).
