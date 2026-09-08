# Failure autopsy -- V3-EXQ-1007 (MECH-536 eval-time action-persistence discriminator)

Generated: 2026-09-08T07:24:26Z. Status: CONFIRMED at the interactive Step 8 gate (2026-09-08T13:52:11Z), all four recommended options accepted: non_contributory both / standard / no hold; successor 1007a re-poses the exposure DV; new registry question with both legs alive; C3 caveat recorded on MECH-536 now.
Scope: single. Autopsied INLINE under /governance cycle governance-20260908-0703 (Step 1.5 route A, user choice).
Target: `v3_exq_1007_mech536_eval_persistence_discriminator_20260907T072349Z_v3` (V3-EXQ-1007), experiment_purpose evidence, outcome PASS, self-route `latch_abolishes_cycle_competence_flat_representational_deficit`, claim_ids MECH-536 (primary), MECH-535 (read-across).

Why an autopsy on an evidence PASS: the mandatory /governance Step 2b driver skim found that the PASS rests on a criterion the driver itself declares degenerate. A PASS is not trusted more than a FAIL because nobody looked.

## 1. Facts (no interpretation)

Dry-run gate: `check_dry_run_citations.py V3-EXQ-1007 V3-EXQ-978` -> 0 dry; family v3_exq_1007 0 dry / 1 real. Recording provenance: `validate_recording.py` OK, always-core complete (recording_schema rec/v1, substrate_hash, substrate_commit ebcd1e896edb clean on main, machine ree-cloud-2, machine_class linux-x86_64-py3.10-torch2.12.0+cpu, elapsed 18776 s, config, seeds [42, 43, 44]).

Design (driver docstring): reproduce 978's field_loss_off cell per seed (x734 all-ON stack, D3_hazard_free, W3_survival_zeroed, PPO reader on 32-d sense-time z_world), snapshot (agent, net), then run paired EVAL-TIME arms on fresh deep copies: greedy_argmax (978 anchor), persist_k2 and persist_k4 (verdict arms), switch_cost (Schmitt), stochastic_sample (T=1.0, comparator). Anchors: random_walk, local_view_greedy, local_view_greedy_persist_k2. Contamination-off sub-grid on greedy and persist_k2.

Verdict grid (pre-registered): C1 = on cycle-present seeds a strict majority have cycle_incidence <= 0.05 on EACH verdict arm. C2 = on EVERY seed and each verdict arm the per-seed lift over greedy is below C2_EFFECT_FLOOR 0.5 res/ep. PASS iff C1 AND C2 under a green gate. Non-degeneracy (pre-registered, `=== NON-DEGENERACY ===`): C2 is non-degenerate iff on every cycle-present seed each verdict arm both outlives greedy AND visits >= UNIQUE_CELLS_MIN_GAIN (3) more mean unique cells. `_adjudicate()` (driver lines 1071-1101) takes (gate_green, c1, c2, exceeds_envelope, phenotype_absent) and never reads the non-degeneracy result.

Measured (manifest `per_arm`, `interpretation`):

| arm | res/ep per seed (42/43/44) | cycle incidence | bounded orbit / longer orbit | mean unique cells | survival |
|---|---|---|---|---|---|
| greedy_argmax | 0.00 / 0.25 / 0.55 | 0.80 / 0 / 0 | 0.80 / 0.00 | 4.45 / 5.0 / 9.75 | 50.75 / 200 / 200 |
| persist_k2 | 0.10 / 0.25 / 0.50 | 0 / 0 / 0 | 0.70 / 0.70 (period 4 x14) | 6.05 / 4.9 / 9.7 | 62.8 / 200 / 200 |
| persist_k4 | 0.15 / 0.25 / 0.50 | 0 / 0 / 0 | 0 / 0 | 7.55 / 4.9 / 9.7 | 103.55 / 200 / 200 |
| switch_cost | 0.25 / 0.25 / 0.50 | 0.15 / 0 / 0 | 0.20 / 0.05 | 6.6 / 4.9 / 9.65 | 127.75 / 200 / 200 |
| stochastic_sample | 2.05 / 1.70 / 1.90 | 0.05 / 0 / 0.05 | 0.05 / 0 | 26.5 / 24.85 / 24.7 | 66.25 / 72.1 / 63.65 |
| random_walk | 1.05 / 0.90 / 0.85 | 0 / 0.10 / 0.15 | | 17.05 / 17.3 / 19.3 | 48.1 / 42.6 / 47.3 |
| local_view_greedy | 45.75 / 49.7 / 48.7 | 0 | | 70.2 / 76.75 / 75.2 | 154 / 170 / 167 |
| local_view_greedy_persist_k2 | 5.75 / 3.45 / 7.7 | 0 | 0.80 / 0.80 | 21.6 / 15.7 / 26.1 | 38.9 / 30.0 / 46.6 |

Gate: green (encoder delta 0.28 > 1e-6; lvg clears floor; greedy replication 3/3 bit-identical to 978 OFF, competence_abs_diff 0.0; greedy cycle present on seed 42 at 0.80 >= 0.25). n_cycle_present_seeds = 1 (seed 42). C1: persist_k2 1/1, persist_k4 1/1 -> true. C2: lifts k2 [0.10, 0.00, -0.05], k4 [0.15, 0.00, -0.05], all < 0.5 -> true. exceeds_envelope: false for both verdict arms; TRUE for stochastic_sample (per_seed_above_random_walk_with_rise [T,T,T], supra_floor_with_rise [T,T,T]). C3 (non-gating): FAILED -- lvg_persist_k2 retention 5.63/48.05 = 0.117 < 0.50. `criteria_non_degenerate`: C1 true, **C2 false**, C3 true, C2_survival_matched true. Top-level `non_degenerate: false`, `degeneracy_reason`: "C2: on some cycle-present seed a verdict arm did not both outlive greedy AND visit >= 3 more cells -- the latch created no foraging opportunity (wall-press or lengthened orbit), so 'flat' measured nothing about direction". Caveats recorded by the driver: `latch_costs_good_representation`, `cycle_replaced_by_longer_orbit` (persist_k2). Manifest stamps: outcome PASS, evidence_direction supports, evidence_direction_per_claim supports/supports.

Arithmetic of the degeneracy on seed 42: persist_k2 survival 62.8 > 50.75 (met); unique cells 6.05 vs required 4.45 + 3 = 7.45 (NOT met, +1.60). persist_k4: 103.55 > 50.75 (met); 7.55 >= 7.45 (met, by 0.10). `all(opportunity)` over verdict arms is therefore false on the only cycle-present seed.

Indexer state: `build_experiment_indexes.py` lines 3731-3733 exclude a run with `non_degenerate is False` from scoring (`scoring_excluded: degenerate`); the fresh claim_evidence.v1.json shows MECH-535 and MECH-536 at exp=0 entries. pending_review.md lists the run under "PASS (verify & close)" with no adjudication flag because that flag is computed only for diagnostic/baseline runs.

## 2. Claim layer

MECH-536 (candidate, standard, phase v3, no evidence_quality_note, lit 6 entries / exp 0): BG-like action persistence is PROTECTIVE against representational degradation rather than NECESSARY for competence; predicted signature: a k>=2 latch on the direction-blind actor removes the two-cell cycle AND leaves resources/episode flat; a competence rise under the latch would indicate a gating deficit. MECH-535 (candidate, standard, phase v3, no evidence_quality_note, lit 11 entries / exp 0): direction-blind reactive ambitendency -- a memoryless reactive actor on a proximity-only representation yields a two-cell approach/withdraw cycle or a boundary-press fixed point by initial condition. Both registered 2026-09-06; this is the first autopsy target for either (granularity_debt_cluster: no tagging targets; brake count 0/0).

Did the test let the claims express themselves? On persist_k4 only by a 0.10-cell margin (~0.2 SE) on an arm that is 9/20 wall-press (stationary 0.84-0.98, 87% of its steps) and 11/20 early death -- the claim's own predicted stupor signature, which the pre-registered opportunity test cannot separate from exposure (red-team finding 1, confirmed). On persist_k2, no: the latch lengthened the orbit rather than dissolving it, so 'competence flat' was measured on an agent that never left the orbit. C1 for k2 is true by construction (the driver's own `=== WHAT A PURE LATCH DOES BY CONSTRUCTION ===` block says so and reserves the scientific content for C2). The verdict requires both arms, so the PASS is half-degenerate and the run cannot carry a claim verdict. MECH-535's seed-42 cycle is a scalar-identical (competence, survival) re-observation of the 978 exemplar; the phenotype distribution on the scored DV (1 cycle / 2 stupor of 3) is recorded for the first time but is non-independent. claim_ids accuracy: correct as tagged.

## 3. Biological-reference triage

Closest mechanism: striatal/pallidal post-decision persistence (commitment hysteresis; the MECH-266 Schmitt switch cost is its formalisation) protecting action against a noisy or impoverished cortical state estimate; the clinical existence proof is catatonic ambitendency and stupor (targeted_review_mech_535, 11 entries: Northoff GABA-A/SMA, clinical case series, computational models). Not a formal-definition import; the design tests a functional role. Does the failure resemble a missing biological dependency? No -- it is a measurement defect. One biological read the successor should carry: a fixed k latch is a crude stand-in for a modulated gate; the k=2 latch on the GOOD representation cut competence ~8x (C3), which is what an unmodulated latch does to an actor that needs to re-decide every step -- the persistence contract is protective only when its depth is governed.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | k2 arm: lengthened lethal orbit, no exposure; k4 arm: opportunity test cleared by 0.1 cell on a 9/20 wall-press arm, the claim's own predicted signature |
| Biological reference | clear | BG persistence vs catatonic ambitendency; lit present |
| Prerequisites | present | eval-time wrapper on a frozen reader; nothing unimplemented exercised |
| Implementation | complete | wrapper behaves as specified; detector self-test 25/25 |
| Environment | adequate | 978's own rung; contamination-off sub-grid recorded |
| Measurement | misleading | grid ignores its own non-degeneracy flag; k2 C1 by construction; n=1 cycle-present seed; envelope-exceeding signal sits in a non-gating comparator |
| Integration | n/a | |
| Scale | likely insufficient | 3 seeds, phenotype seed-specific (1/3) |

Failure-location (GOV-FAILLOC-1): MECHANISM established, ENVIRONMENT established, MEASURES partial -> **MEASURES**, not chargeable to REE, not a finding against either claim.

Epistemic category: **standard** on both (failure mode measurement_test_design_defect; no build owed; does not count toward the re-derive brake under R3 step 2).

## 5. Learning extracted

1. A pre-registered non-degeneracy check that the verdict grid does not GATE on is decorative. This driver computed non_degenerate=false and returned PASS/supports anyway. The indexer caught it (scoring_excluded), but pending_review.md's discovery net did not: the adjudication flag fires only for diagnostic/baseline runs, so an evidence-purpose degenerate PASS is listed as "verify & close".
2. A k=2 latch on a period-2 argmax alternation produces a period-4 orbit by construction, and the period-4 orbit is a GENERIC latch artifact: local_view_greedy_persist_k2 orbits on 60-80% of episodes ({4: 16/16/12}) on a policy with zero orbits unlatched. persist_k2 cannot be a verdict arm; k3 is untested (k4 broke the orbit here).
2b. The non-degeneracy test (outlive greedy AND +3 unique cells) cannot separate 'straight run then press' from 'lengthened orbit': persist_k4 cleared it by 0.10 cells with 87% of its steps in 200-step wall-press. MECH-536 PREDICTS perseveration into the boundary, so a true claim makes the test hard to satisfy by construction. The exposure DV must change, not only the gating.
3. The 978 phenotype is seed-specific (1/3 cycle-present). A 3-seed design conditioned on cycle presence has n=1 by expectation.
4. The stochastic comparator exceeded the undirected envelope on 3/3 seeds (2.05/1.70/1.90 vs random_walk 1.05/0.90/0.85; per 100 survived steps 3.09/2.36/2.99 vs 2.18/2.11/1.80) while both latches stayed inside it. Whether that is direction recovered from the logits or exploration coverage (26 vs 4-9 unique cells) is unposed; it is the reading the grid would have called a gating deficit had a verdict arm produced it.
5. C3 failed: the k=2 latch on the good-representation anchor cut competence from 48.05 to 5.63 res/ep. MECH-536's "protective, not necessary" needs "costly at fixed depth on a good representation".

## 6. Repair pathway and routing

Node: `complex (probe-gated) / puzzle (known rules)` for the science, with one FRAME question first (red-team finding 1): the claim's predicted perseveration signature and the exposure test pull against each other, so 'competence flat under the latch' needs re-posing before the letter is authored. Routing: **/queue-experiment**, same-question letter V3-EXQ-1007a: (1) verdict grid gates on `non_degenerate` (degenerate C2 -> non_contributory, never PASS); (2) exposure DV separating straight-run-then-press from lengthened orbit (pooled non-stationary step fraction + cells traversed vs random_walk per-step coverage, margin pre-registered above the per-episode SE ~2.1 cells; fixed-point caveat on pooled stationary fraction); (3) verdict k chosen by a per-k orbit-histogram reach check with an explicit 'k orbits -> reported only' branch (k2 excluded, k3 untested), and local_view_greedy_persist_k at the verdict k so C3 is measured where the verdict is; (4) >= 2 cycle-present seeds via a cheap greedy pre-screen; (5) keep switch_cost and stochastic_sample, add stochastic_sample_persist_k, pre-register the comparator's reading; (6) carry the C3 caveat into the claim note. Substrate entry: none. Brake: not fired (0 prior hits; instrument reading). Fan-out: not a discrimination needing a portfolio.

Recommended writes for governance: manifest evidence_direction supports -> non_contributory (run-level and per-claim) flat AND pack with an evidence_direction_note citing this artifact; evidence_quality_note (JSON `recommended_evidence_quality_note`) appended to MECH-536 and MECH-535; epistemic_category stays standard; no pending_retest_after_substrate. Follow-on NOT chipped by this autopsy; /governance chips it after Step 2b (infra gap in learning 1 is a separate chip).

Read-across not adjudicated: (a) pending_review.md discovery-net gap for evidence-purpose non_degenerate:false PASSes (confirmed: `_compute_adjudication` returns n/a unless diagnostic/baseline); (b) GFLAG-0131's stochastic-eval ask now has a first measurement on the 978 reader; (c) MECH-536's operationalisation of 'competence flat' vs its predicted perseveration signature. Pack note: the run pack carries no `non_degenerate` key; governance adds it (flat is the indexer's authority for that field).

## 7. Step 7b / 7c

7b `autopsy_pre_routing_checks.py`: 0 fires (C5/C7 inapplicable on the draft).
7c red-team (Fable, cross-model pass): CONTESTED on the successor spec, direction/category/route held, every number matched on recompute. Two verdict-moving findings (persist_k4 wall-press margin; k2 orbit generic, k3 untested, C3 anchor at verdict k) confirmed on the cells and applied above; 5 qualifications and 2 hygiene items applied; moves toward weakens or a weak MECH-535 supports were tested by the red team and rejected.

## 8. Gate disposition and registry

User-confirmed 2026-09-08T13:52:11Z: non_contributory on MECH-536 and MECH-535, epistemic_category standard, no substrate hold; 1007a specified with the re-posed exposure DV (Section 6); C3 caveat recorded on MECH-536 now. Step 9b: new question `mech536_latch_dissociation_representation_vs_gating` registered with two legs, both alive (H-representational-deficit, axis representation; H-gating-deficit, axis selection), resolving_runs V3-EXQ-1007, basis 'uninformative: C2 degenerate on the sole cycle-present seed'; pre_registered_utc 2026-09-07 (driver queue commit ree-v3 1bbcfd8) <= run date. Follow-on for /governance to chip: the 1007a /queue-experiment letter; the pending_review discovery-net gap for evidence-purpose non_degenerate:false PASSes.
