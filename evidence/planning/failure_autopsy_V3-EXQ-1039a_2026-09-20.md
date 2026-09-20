# Failure autopsy -- V3-EXQ-1039a (waypoint-field consumer reach, H1 drive leg, absorption-gated re-run)

Status: confirmed (Step 8 gate held 2026-09-20, user present; red-team opus cross-model CONTESTED, revisions applied)
Target: `v3_exq_1039a_mech428_inv086_waypoint_field_consumer_drive_signal_absorption_gated_20260919T022652Z_v3` -- diagnostic, FAIL, self-route `substrate_not_ready_requeue`, indexer `precondition_unmet`. Claims INV-086, MECH-428. Supersedes V3-EXQ-1039. ree-cloud-2, 3h11m, seeds 42/43/44.

## 1. Facts (verified cell-by-cell by the red-team pass)
Dry-run gate: clean (1039 and 1039a both real runs). validate_recording: OK, one advisory (C1 never recorded because never reached).
Five of ten conjunctive readiness gates red; the driver returned before R1/R2/C1.

| gate | measured | bar | worst cell |
|---|---|---|---|
| C0d bias-head weight-norm delta | 0.0 | > 1e-9 | all three arms @ seed 42 |
| A1 shaped-vs-sparse return separation | 0.952 SD | >= 1.0 | seed 44 (seeds 42/43: 2.64 / 1.07) |
| A3 demo CE below chance | 1.00007 x ln 32 | <= 0.9 | seed 43; seed 42 = 3.465736 after 232 steps |
| B1 first-action diversity | 0.005 of ticks >= 3 classes | > 0.5 | all arms @ seed 43 (seed 42: 1.0, seed 44: 0.865) |
| B2 bias-ablation changes action | 0 of 3 seeds | >= 2 | shaped_rl (others 1/3; 3 of 400 actions) |

Green: C0 oracle 10.8, C0b, C0c span 11.1, C0e, A2 advantage-surviving 0.999.
Recorded, not gated: `lpfc_bias_saturated_frac` = 1.0 in all three arms at seed 42 (|bias| == bias_scale 0.1 to float precision); 0.0-0.19 elsewhere. DV, never scored: sparse_rl and shaped_rl again bit-identical (0.4 / 0.2 / 0.0 waypoints per episode).

Dry-run gate: check_dry_run_citations.py run 2026-09-20 over all 11 cited run_ids (1039, 1039a, 1043, 1043a, 1057, 1057a, 1060, 1063, 1065, 1069, 1070): 0 dry, 11 clean. validate_experiments --checks dry_run_unreachable_criterion: silent on all nine drivers; reduction blocks read by hand.

## Target V3-EXQ-1039a -- diagnostic FAIL, claims INV-086, MECH-428
`v3_exq_1039a_mech428_inv086_waypoint_field_consumer_drive_signal_absorption_gated_20260919T022652Z_v3`

**Self-route** `substrate_not_ready_requeue` -- adjudication: CONFIRMED that no verdict is licensed; cause REFINED into three routes, per seed. (1) Seed 42: the treatment recipe trains the lPFC bias head on the HARD-CLAMP path (lateral_pfc_train_rule_bias_head=True, lateral_pfc_rule_readout_consumer absent from an exhaustive enabled_default_off_flags walk); the clamp sat on its rail on every recorded P1 tick in all three arms (|bias| mean == max == bias_scale), weight-norm delta exactly 0.0 -> C0d. (2) Seeds 43/44: the clamp is NOT saturated and the head DID move; A3 fails there because the demo CE update is skipped whenever no candidate's first action matches the oracle (14 and 22 matched vs 186 and 178 defaulted), so A3's statistic is the mean of 1 and 2 updates. That starvation is DOWNSTREAM of the seed-43 proposer-pool collapse (B1) -- one cause, not two. (3) B2 (ablation changes 0-3 of 400 actions) has a clamp-independent explanation already on record: lPFC bias / raw E3 score range is 0.004-0.03 here, the regime V3-EXQ-1029 adjudicated argmin-inert with the read-out consumer ON (0 of 1694 argmin, 0 of 13857 sampled actions).

**Failed criterion.** readiness -- 5 of 10 conjunctive preconditions (C0d, A1, A3, B1, B2); verdict criterion C1 never reached

### Four-layer diagnosis
- **claim_alignment**: unclear -- not exercised. The run gated out before R1/R2/C1; it is the claim-free instrument-repair leg for H1 of waypoint_field_consumer_reach, not either claim's own falsifier.
- **biological_reference**: partial -- lateral-PFC rule representation biasing action selection (Badre 2009 hierarchy) and reward shaping as potential-based guidance (Ng 1999); MECH-428 has 3 lit rows, INV-086 has NONE in claim_evidence.v1.json (its grounding dir targeted_review_proxy_progress_goal_maintenance carries no INV-086-tagged entry).
- **prerequisites**: immature -- proposer pool collapses to a median of 2 distinct first-action classes at seed 43 in ALL THREE arms during the scored run (B1 frac_ge_floor 0.005 vs 1.0 at seed 42, 0.865 at seed 44): seed-dependent and arm-independent, i.e. upstream of the manipulation (ARC-065/MECH-314 candidate compression; SD-061 regulator is implemented_pending_validation and was not on).
- **implementation**: partial -- inert by DEFECT on two routes. (a) neutralising guard or default: hard clamp on its rail at seed 42 in all arms (saturated_frac 1.0; P0 and P1 weight-norm deltas both exactly 0.0, so the P1 weights are the init weights). (b) no consumer authority: bias / raw-score-range 0.004-0.03, the V3-EXQ-1029 argmin-inert regime.
- **environment**: adequate -- greedy oracle 11.6 vs random walk 0.5 waypoints/ep, achievable span 11.1 (floor 2.0).
- **measurement**: partial, not adequate. The paired gate localised the failure to seeds and code paths, which 1039's boolean could not. But A3 cannot discriminate where the pool collapses (n=1, n=2 update windows at seeds 43/44); B2 cannot separate 'no authority' from 'learned nothing differentiated'; modulatory_shortlist_size is constant at a dead sentinel where the design needs it to vary; A1's miss (0.952 vs 1.0 SD) is threshold noise.
- **integration**: coupled but inert -- by DEFECT. Missing links: neutralising default (seed 42) AND no consumer authority at selection (all seeds; SD-082's open question).
- **scale**: unknown -- the 90-episode budget was deliberately held (autopsy-1039 item 5: reconsider only after items 1-4).

### Failure location (GOV-FAILLOC-1)
- **mechanism**: partial
- **measures**: partial
- **environment**: established
- **ree**: False
- **net_classification**: MIXED (MECHANISM + MEASURES); not chargeable to REE, INV-086 or MECH-428

### Biological reference
- **closest_mechanism**: lateral PFC rule/context representation biasing basal-ganglia action selection; shaping as dense proxy progress signal
- **dependencies**: ["diverse candidate proposals (premotor/BG)", "reward-contingent plasticity at the PFC->selection synapse", "goal maintenance (MECH-116)"]
- **is_formal_import**: False
- **divergence**: none identified at this layer
- **lit_status**: partial (MECH-428: 3 literature rows; INV-086: 0 literature rows, 4 exp:simulation rows all non_contributory)

### Claim-layer recommendation
- direction: `non_contributory` per claim {"INV-086": "non_contributory", "MECH-428": "non_contributory"}
- epistemic_category: `standard` -- Instrument/recipe defect (precondition_unmet, measurement of absorption now adequate). No epistemic suppression asserted on either claim.
- per claim: INV-086: direction and category already match the stored values; append the evidence_quality_note and re-point live_status.evidence.from -> stamp this artifact [none -- stays candidate]; MECH-428: direction and category already match the stored values; pending_retest_after_substrate stays true (the 884a retest is still owed and this run is not it); append the note -> stamp this artifact [none -- stays candidate]

**Draft evidence_quality_note.** V3-EXQ-1039a (diagnostic, FAIL, substrate_not_ready_requeue; supersedes V3-EXQ-1039): non_contributory for INV-086 and MECH-428 -- neither claim exercised. 5 of 10 paired readiness gates red, by three routes: seed 42 -- bias head trained on the hard-clamp path (rule_readout_consumer off), clamp on its rail in all arms, exactly-zero gradient (C0d); seeds 43/44 -- proposer pool collapsed to a median of 2 first-action classes in every arm (B1), which also starved the demo CE update stream to 14 and 22 steps so A3 there is an n=1 and n=2 statistic; all seeds -- bias-head ablation changes 0-3 of 400 actions (B2), consistent with SD-082's open V3-EXQ-1029 finding that the read-out is argmin-inert at native magnitude even with the consumer ON. H1 (objective sparsity) of waypoint_field_consumer_reach is UNRESOLVED and is gated on SD-082's open authority question, not on a recipe tweak. failure_autopsy_V3-EXQ-1039a_2026-09-20.

### Substrate queue
- **action**: none
- **note**: WITHDRAWN after red-team: the first draft proposed an SD-082 amend. SD-082 already carries this debt as two OPEN failure_record items -- V3-EXQ-1029 (consumer ON: 0/1694 argmin, 0/13857 sampled actions) and V3-EXQ-1046 (consequence-trained read-out rule-invariant, 0/7) -- and a 12th item restating them at 400 actions per seed would be duplicated debt. USER DECISION 2026-09-18T18:50:48Z (Option A) deliberately emptied SD-082's substrate_paths and found NO live corruption precisely because rule_readout_consumer defaults False and the all-ON recipe does not set it; this autopsy does not re-open that. Owed bookkeeping only: sd-allon-training-signal-absorption-telemetry still reads pending_implementation although it landed (ree-v3 996dec30) and this run consumed it. A cross-flag config guard (train_rule_bias_head without rule_readout_consumer) would be a small ree_core BUILD, reported for governance to weigh, not recommended here as an amend.

### Brake, granularity, debt class
- re-derive brake: fired=False, literal count 1. Literal count MECH-428 = 1 (884), INV-086 = 0. This target declares both claims peripheral (per-claim category standard) so it does not add a hit. The brake does not fire -- but a blind same-question letter is REFUSED ON THE MERITS: see routing_detail.
- granularity trigger: fires=False. granularity_debt_cluster.py: INV-086 3 targets (all alignment=other/not exercised), MECH-428 4 targets (other=3, unclear=1). No target reads weakened -> instrument debt, not granularity debt.
- debt class: complex (probe-gated) / puzzle (known rules) at the SD-082 layer: no run has yet trained the read-out in a regime where its output reaches selection. Until that exists the H1 drive question cannot be asked through this consumer.

### Learning extracted
- The paired absorption + conversion gate converted 1039's vacuous PASS into an honest refusal and localised the cause per seed. It also showed its own limit: a gate whose statistic is a window over UPDATES needs an update-count floor.
- Check a recommended change against the corpus by WHAT IT CHANGES, not by the successor's name. 'Enable the read-out consumer' had already been run twice under SD-082.
- Two of the five red gates share one upstream cause (pool collapse -> update starvation). Count causes, not gates.
- Red-team F1 measured the clamp saturation in the SMOKE before queueing (saturated_frac 1.000 in all three arms); gating it was declined 2026-09-18. The full run reproduced it at seed 42.
- A telemetry key read from the wrong selector branch is constant at its initialiser and looks like a measurement. Verify a new readout varies in the smoke.

### Routing: `implement-substrate`
- **refused**: V3-EXQ-1039b in any form that keeps this consumer as the conversion surface. Enabling rule_readout_consumer is expected to clear C0d (822b: head trains once the driver is fixed) and is NOT expected to clear B2 (1029, 1046) or A3 at seeds 43/44 (pool starvation).
- **gated_on**: ["SD-082 open failure_record items V3-EXQ-1029 and V3-EXQ-1046 (read-out authority at selection)", "proposer-pool first-action diversity at seed 43 (SD-061 regulator is implemented_pending_validation, ready false)"]
- **if_a_successor_is_ever_built**: ["A3 needs a minimum-update floor (it reported a 1-sample chance ratio as a zero-gradient signature)", "record f_eligibility_envelope_size: modulatory_shortlist_size is a dead sentinel (0.0 in all nine cells) under use_f_eligibility_demotion, which writes a different key (e3_selector.py:4378 vs :4390)", "the driver's --probe mode is hard-wired to seeds=[42], the one seed that passes B1 -- it needs a seed list before it can pre-screen anything", "promote lpfc_bias_saturated_frac to a gate (the 2026-09-18 option C, re-asked with this run as evidence)"]
- **in_flight_check**: no 1039b script, queue entry or claim (2026-09-20). Checked by CHANGE as well as by name after red-team: the recommended change (consumer ON) has already run as V3-EXQ-1029 and V3-EXQ-1046.

### Step 7b pre-routing fires
- C2: DISMISSED with reasons -- all four list INV-086 / MECH-428 in unblocks_claims and none is this run's blocker. SD-094 (waypoint-arrival detection) is implemented_validated and SD-092 (cross-level subgoal credit) concerns MECH-428's OWN retest (V3-EXQ-884a), which this run is not. waypoint-proximity-field-observable is the SD-WAYPOINT-FIELD build V3-EXQ-1004 validated; the environment layer reads adequate here (oracle 11.6 vs random 0.5). SD-ZWORLD-SENSE-PATH-PARITY belongs to the sibling H2 (representation) leg, V3-EXQ-1030/1030a, not to this H1 (drive) leg. The entry that does gate this leg is SD-082, already named, with action none because its open items already carry the debt.

### Step 7c red-team
- **model**: opus (claude-opus-5[1m]); drafting session was fable -- cross-model pass
- **verdict**: CONTESTED
- **disposition_survived**: True
- **accepted**: ["F1 A3's offending cell is seed 43 where the clamp is NOT saturated; cause is update starvation from the pool collapse", "F2 the recommended fix already ran as V3-EXQ-1029 / 1046 (B2-equivalent open and negative)", "F3 --probe is hard-wired to seed 42", "F4 modulatory_shortlist_size is a dead sentinel; authority-share explains B2 without the clamp", "F5 the SD-082 amend contradicted the 2026-09-18 Option A decision -> WITHDRAWN", "F6 'zero evidence rows of any kind' corrected to zero LITERATURE rows"]
- **what_changed**: routing queue-experiment -> implement-substrate (gated on SD-082's existing open items); substrate amend withdrawn; measurement adequate -> partial; failure-location MECHANISM -> MIXED. Dispositions (non_contributory / standard, both claims peripheral) unchanged.
- **cheap_confirmers_run**: 10/10 recomputes matched incl. brake (MECH-428=1, INV-086=0); flag-unset confirmed via exhaustive dataclass walk; saturation-at-init confirmed (shared weight_norm_pre, P0 and P1 deltas 0.0)

