# Diagnostic autopsy (cluster) -- V3-EXQ-1060, 1063, 1069 (INV-063 leg-B lineage: three diagnostic PASSes)

Status: awaiting_human_confirmation (Step 8 gate pending)
All three are `experiment_purpose: diagnostic` PASSes and so require adjudication whatever their flags (trigger 2). Indexer flags: 1060 none; 1063 `vacuous_pass`; 1069 `precondition_unmet` + dead z_goal stream. Together they feed one decision: the four-arm intake ladder V3-EXQ-1071, under design today by a live session (claims read only; nothing of that session's touched). Predecessor: V3-EXQ-1026 autopsy 2026-09-14 (read in full) and the two 798a autopsies.

Dry-run gate: check_dry_run_citations.py run 2026-09-20 over all 11 cited run_ids (1039, 1039a, 1043, 1043a, 1057, 1057a, 1060, 1063, 1065, 1069, 1070): 0 dry, 11 clean. validate_experiments --checks dry_run_unreachable_criterion: silent on all nine drivers; reduction blocks read by hand.

## Cluster reading
**Shape.** three diagnostic PASSes in 31 hours, each green on its own self-route, chained into one go decision (the four-arm intake ladder; V3-EXQ-1071 is RESERVED AND UNUSED -- the designing session stopped at 2026-09-20T10:56Z and reported inv063_legb_tau_bind_20260920 / GFLAG-0382 instead of queueing)

**Independent bugs?** no -- one structural property.

**Structural property.** Each PASS answers a narrower question than the decision it is cited for. 1060: wired. 1063: one citeable direction finding, NEGATIVE for leg B as registered, with the objective-mismatch signature (trained objective up 3/3, DV down 3/3). 1069: gradeable on exactly 2/3 seeds. With GFLAG-0382 (every readable tau gives a negative across-sleep delta) the chain contains no showing, on either readout, that a sleep cycle improves the world-forward model in the regime leg B reads.

**Readings.** test_design_ceiling, substrate_enrichment

**Planning decision forced.** the decision already in front of the user in inv063_legb_tau_bind_20260920 sec 4: (c) fold the tau ladder into the run with a pre-registered leg_b_dv_sign_inverted refusal route, (b) relax the readability floor, (a) read the degradation, (e) convert INV-063 to substrate_conditional. This cluster adds: whichever is chosen, the three ~30-min fan-out probes in the ladder's regime are the cheap way to learn WHY the sign is inverted first.

## Target V3-EXQ-1060 -- diagnostic PASS, claims MECH-423
`v3_exq_1060_inv063_e2_world_forward_sleep_trainer_20260919T012511Z_v3`

**Self-route** `e2_world_forward_sleep_trainer_live` -- adjudication: CONFIRMED as LIVENESS and nothing more. C1/C2/C4/C5 are sharp (the e2_world metric key and 8 updates appear only with the lever on; the OFF arm's world heads are bit-identical with the same pass running). C3 and C6 are near-tautological once a gradient exists: the landed world-head delta 0.007899 is 98.7% of the 8 x lr = 0.008 fresh-Adam step bound and the action-encoder delta 0.00653 is 82% of it. The PASS says 'wired and receiving gradient', not 'learning'.

**Failed criterion.** none (PASS). Weakest criteria: C3, C6 (cannot fail once the readiness gate is green).

### Four-layer diagnosis
- **claim_alignment**: intact but PERIPHERAL -- MECH-423 (super-additivity) is a traceability tag by the driver's own statement; the run tests neither MECH-423's falsifier (answered by V3-EXQ-680e) nor INV-063's (the four-arm intake ladder, never run).
- **biological_reference**: partial -- offline consolidation of a forward/world model during sleep (CLS; Kumaran 2016).
- **prerequisites**: present (42/42 per-cell preconditions met).
- **implementation**: complete for wiring -- use_sleep_world_forward_consolidation adds an e2_world module scoped to world_transition + world_action_encoder; OFF is structural absence.
- **environment**: adequate for a wiring check (5x5 grid, 180 transitions per cell).
- **measurement**: adequate for liveness; efficacy ungated by declaration. C3/C6 read the MOST-moved weight: world_head max|delta| 0.0079 is ~99% of the 8 x lr Adam step scale, while other tensors moved 49-83% of it -- the pass is gradient-magnitude-blind in step SCALE, not 'every weight moves 8 x lr'.
- **integration**: coupled -- the lever reaches the two world heads through a real sleep cycle; nothing downstream is asserted to consume the change.
- **scale**: adequate for the question asked (22.5 s, 6 cells)

### Failure location (GOV-FAILLOC-1)
- **mechanism**: established
- **measures**: partial
- **environment**: established
- **ree**: False
- **net_classification**: n/a (PASS). Liveness established; efficacy explicitly ungated and, per V3-EXQ-1063, negative on a converged base.

### Biological reference
- **closest_mechanism**: sleep-dependent consolidation of a predictive world model
- **dependencies**: []
- **is_formal_import**: False
- **divergence**: none at the wiring level
- **lit_status**: present (MECH-423: 6 entries; INV-063: 5 entries)

### Claim-layer recommendation
- direction: `non_contributory`
- epistemic_category: `standard` -- Clean liveness diagnostic (instrumentation/wiring validation); no category applies.
- per claim: MECH-423: manifest stamps evidence_direction supports for a liveness check that tests no MECH-423 contrast; correct flat AND run-pack copies -> non_contributory [none -- stays provisional (V3-EXQ-680e remains its evidence)]

**Draft evidence_quality_note.** V3-EXQ-1060 (diagnostic, PASS, e2_world_forward_sleep_trainer_live): non_contributory for MECH-423 -- the manifest's 'supports' is NOT warranted: the run is a wiring/liveness check of the 2026-09-17 lever use_sleep_world_forward_consolidation and tests no super-additivity contrast (sibling test-bed validations 798a and 1063 stamp non_contributory). What it establishes: through a real sleep cycle the lever moves E2's world heads (min max|delta| 0.0079, 8 updates) and the OFF arm is bit-identical. What it does not: that the movement is learning -- 0.0079 is 98.7% of the 8 x lr fresh-Adam step bound. Discharges the open failure_record on substrate_queue e2-world-forward-sleep-trainer as a LIVENESS showing only. failure_autopsy_INV-063-1060-1063-1069-cluster_2026-09-20.

### Substrate queue
- **action**: amend
- **target_sd_id**: e2-world-forward-sleep-trainer
- **note**: Entry is STALE (GFLAG-0355, GFLAG-0359 both open): status pending_implementation / build_owed although the build landed (ree-v3 4610133, 2026-09-17). Set status implemented_pending_validation -- NOT implemented/validated: liveness is shown, efficacy is negative on a converged base (see the 1063 failure_record_entry in this cluster). Also owed: a ree-v3/CLAUDE.md substrate-index record for the lever.
- **resolves_prior_failure_record**: [{"run_id": "v3_exq_1026_mech423_sleep_integrated_e2_consolidation_20260914T111100Z_v3", "resolved": "resolved", "resolved_note": "V3-EXQ-1060 PASS 2026-09-19: with the lever on, E2.world_forward parameters move through a real sleep cycle (delta > 0 ON, == 0 OFF). Liveness only."}]

### Brake, granularity, debt class
- re-derive brake: fired=False, literal count 2. MECH-423 literal count is 2 but this target is a PASS, declares MECH-423 peripheral, and routes no MECH-423 re-test. Nothing to refuse.
- granularity trigger: fires=False. MECH-423: 4 targets, intact=3 strengthened=1, none weakened; claim carries granularity_debt_disposition coherent_campaign.
- debt class: closed for liveness.

### Learning extracted
- Three green self-routes do not add up to a green light: 1060 = wired; 1063 = one citeable direction finding, negative for leg B as registered; 1069 = gradeable at the boundary. With GFLAG-0382, no readable readout shows sleep improving the world-forward model.
- When the trained objective improves and the DV worsens on every seed, suspect the objective before the optimiser.
- A liveness criterion of the form 'parameter moved > 0' is met by any optimiser that saw any gradient. Report the move against the step scale.
- An OFF-arm attribution control is only as good as the evidence the rest of the pass ran. updates_e2 = 0 in all 12 cells was in the manifest; the cause is one missing call (record_transition).
- Driver and indexer disagree about applies:false. Every scoped-out-and-recorded precondition raises a false precondition_unmet today.
- WITHDRAWN (first draft): 'the converged model IS the identity predictor, so the DV cannot improve' -- seed 123 beats identity by 23%.

### Routing: `governance-note-only`

## Target V3-EXQ-1063 -- diagnostic PASS, claims INV-063
`v3_exq_1063_inv063_legb_dv_direction_20260919T102929Z_v3`

**Self-route** `legb_dv_converged_base_infonce_positive_mse_not` -- adjudication: HALF CONFIRMED, HALF WITHDRAWN. 'mse_not' stands as a measurement. 'infonce_positive' is UNCITEABLE by the run's own headroom condition (0.0215 vs 0.2079; readout at 99.5% of ln 64). The indexer's vacuous_pass is GENUINE and lands on C4: its attribution premise ('the same MECH-423 pass ran in both arms') is certified by updates_e2 >= 1, and updates_e2 is 0.0 in all 12 cells -- PROVED from source: compute_e2_loss reads _e2_transition_buffer, which only record_transition fills, and record_transition has no caller in ree_core. D1's attribution to the lever survives (ON and OFF differ only in the lever; OFF bit-identical).

**Failed criterion.** none routed (validity C1-C6 all pass). Degenerate: C4 (non-degeneracy assertion false), D2, D4.

### Four-layer diagnosis
- **claim_alignment**: unclear -- no intake question is posed (world_rule_shift disabled in every arm); this adjudicates an instrument.
- **biological_reference**: partial -- sleep improves a world model that has something left to learn; synaptic downscaling/renormalisation (Tononi & Cirelli) is the closest analogue to 'sleep perturbs a saturated model', and it is homeostatic, not a fixed-size step.
- **prerequisites**: present (108/108 preconditions met).
- **implementation**: partial -- inert by STARVED UPSTREAM for the e2 self-forward module (record_transition is never called, so its replay buffer is empty and the module is never stepped); e2_world is live. Fresh Adam per cycle gives a step SCALE of ~lr per step for the most-moved weights (max|delta| 0.00798-0.00807 ~ 8 x lr).
- **environment**: adequate
- **measurement**: misleading. Two properties, neither yet separated from the other: (i) OBJECTIVE MISMATCH -- the trainer descends InfoNCE and the DV is MSE; InfoNCE improved 3/3 while MSE worsened 3/3, monotonically across cycles on two seeds, which a magnitude-blind perturbation alone does not produce; (ii) LITTLE HEADROOM -- the converged base is near the copy-the-input reference, so there is ~1e-5 of error to win and three cycles cost 7e-5 to 9e-4. Regime caveat: alpha_world = 0.3 here; the ladder's regime sets 0.9.
- **integration**: coupled
- **scale**: adequate

### Failure location (GOV-FAILLOC-1)
- **mechanism**: partial
- **measures**: not_established
- **environment**: established
- **ree**: False
- **net_classification**: MIXED (MEASURES + MECHANISM): trainer objective and DV disagree, and the DV has little headroom. Not chargeable to REE; not evidence against INV-063.

### Biological reference
- **closest_mechanism**: sleep-dependent world-model consolidation with homeostatic scaling
- **dependencies**: ["residual error to consolidate", "update magnitude scaled to the error signal"]
- **is_formal_import**: False
- **divergence**: the trainer's step is fixed-size (fresh Adam), not error-scaled
- **lit_status**: present (targeted_review_inv_063, 5 entries)

### Claim-layer recommendation
- direction: `non_contributory`
- epistemic_category: `standard` -- Instrument adjudication; measurement_gap (DV floor) + optimiser artefact. No suppression asserted on INV-063.
- per claim: INV-063: INV-063 carries neither flag today; leg B stays blocked on a trainer whose efficacy is unshown, so write the note above and -> set pending_retest_after_substrate true [none -- stays candidate]

**Draft evidence_quality_note.** V3-EXQ-1063 (diagnostic, PASS on validity; indexer vacuous_pass genuine, on C4): non_contributory for INV-063, by design. CITEABLE: on a converged base at alpha_world 0.3, three sleep cycles with the world-forward trainer on made frozen-battery MSE worse on 3/3 seeds while the trained objective (InfoNCE) moved the other way -- the objective-mismatch signature. The base sits near the copy-the-input reference (ratio 1.07 / 0.77 / 1.01; seed 123 is 23% BETTER, so it is a reference, not a bound). UNCITEABLE: D2/D4 (InfoNCE at 99.5% of chance at tau 0.1) and C4's attribution premise. Read with inv063_legb_tau_bind_20260920 / GFLAG-0382: on 798a's configuration every READABLE tau (<= 0.01) gives a NEGATIVE across-sleep delta and every positive delta (tau >= 0.03) is unreadable. Neither readout currently shows sleep improving the world-forward model where leg B needs it. failure_autopsy_INV-063-1060-1063-1069-cluster_2026-09-20.

### Substrate queue
- **action**: amend
- **target_sd_id**: e2-world-forward-sleep-trainer
- **severity**: degrading
- **substrate_paths**: ["ree_core/sleep/cross_module_consolidation.py", "ree_core/sleep/phase_manager.py"]
- **note**: severity stays degrading. The fresh-optimiser-per-call property is shared by every module the consolidator steps, not only e2_world.
- **implementation_hint**: Decide deliberately whether the MECH-094-exempt pass should keep 'no persistent optimiser state'. Options: error-scaled step (plain SGD or lr tied to loss), persistent per-module Adam state across cycles, or a lower cross_module_consolidation_lr. Whichever is chosen, the acceptance test is a converged-base run in which sleep does not push the model off its floor.
- **failure_record_entry**: {"run_id": "v3_exq_1063_inv063_legb_dv_direction_20260919T102929Z_v3", "experiment_type": "v3_exq_1063_inv063_legb_dv_direction", "metric": "converged base: frozen-battery world-forward MSE worse after sleep on 3/3 seeds (delta -7.1e-5, -6.7e-4, -9.2e-4 against a base of ~1e-5); world-head max|delta| 0.00798-0.00807 = the 8 x lr fresh-Adam bound", "target": "on a converged base, post-sleep battery MSE within 2x of pre-sleep on >= 2/3 seeds, with the world heads still moving on an unconverged base", "resolved": "open"}

### Brake, granularity, debt class
- re-derive brake: fired=False, literal count 0. INV-063 literal count 0 before this cluster. Per R3 this target (non_contributory, category standard, amend owed) is the FIRST counting hit on INV-063; the brake does not fire at 1.
- granularity trigger: fires=False. granularity_debt_cluster.py INV-063: 0 targets before this cluster.
- debt class: complex (probe-gated) / puzzle (known rules): objective mismatch (now the best-supported leg) vs step scale vs DV headroom.

### Learning extracted
- Three green self-routes do not add up to a green light: 1060 = wired; 1063 = one citeable direction finding, negative for leg B as registered; 1069 = gradeable at the boundary. With GFLAG-0382, no readable readout shows sleep improving the world-forward model.
- When the trained objective improves and the DV worsens on every seed, suspect the objective before the optimiser.
- A liveness criterion of the form 'parameter moved > 0' is met by any optimiser that saw any gradient. Report the move against the step scale.
- An OFF-arm attribution control is only as good as the evidence the rest of the pass ran. updates_e2 = 0 in all 12 cells was in the manifest; the cause is one missing call (record_transition).
- Driver and indexer disagree about applies:false. Every scoped-out-and-recorded precondition raises a false precondition_unmet today.
- WITHDRAWN (first draft): 'the converged model IS the identity predictor, so the DV cannot improve' -- seed 123 beats identity by 23%.

### Routing: `queue-experiment`

**Fan-out (GOV-FANOUT-1).** Live hypotheses:
- H-objective-mismatch: the sleep trainer descends InfoNCE while the DV is MSE (best supported: InfoNCE up 3/3, MSE down 3/3; GFLAG-0382's tau trade-off)
- H-step-scale: a fresh Adam per cycle gives a gradient-magnitude-blind step that perturbs a well-fit model
- H-dv-headroom: the converged base is near the copy-the-input reference, leaving ~1e-5 to win

Probes:
- H-objective-mismatch [representation]: train the world heads on an MSE objective in the sleep pass (same steps, lr), read the same MSE battery. Null: still worsens.
- H-step-scale [algorithm]: consolidation lr in {1e-3, 1e-4, 1e-5} or SGD on the converged arms. Null: MSE delta flat in lr.
- H-dv-headroom [measurement]: a battery with headroom (post-shift dynamics the model has not seen). Null: still negative with headroom.

GOV-FANOUT-1. Run in the LADDER'S regime (798a configuration, alpha_world 0.9), not 1063's alpha_world 0.3 harness. These probes are one way to take option (a)/(c) of inv063_legb_tau_bind_20260920 sec 4; they do not replace the user decision that doc is waiting on.

## Target V3-EXQ-1069 -- diagnostic PASS, claims INV-063
`v3_exq_1069_inv063_p1_gate_798a_p0_20260920T082003Z_v3`

**Self-route** `inv063_p1_intake_ladder_gradeable` -- adjudication: CONFIRMED, at the boundary. P1 met on exactly 2 of 3 seeds (need 2): spreads 0.394 / 0.241 / 1.691 vs 0.25, monotone 3/3; survives the episode-truncation control (late-in-episode MEL: same two seeds, 0.91 and 3.18; seed 123 inverts). Both indexer flags CLEARED: precondition_unmet is an artefact (driver hardcodes met:true on the scoped-out R1, applies:false; the indexer's recompute ignores applies/kind -- confirmed by mutation test); the dead z_goal stream does not reach the MEL DV (update_residue has no goal reference; arm-symmetric; inherited from 798a). NOT 'the identical configuration' as 798a: P0 is computed once per seed and restored from a state_dict snapshot, and the NONE-arm MEL differs from 798a-linux on all three seeds (x0.81, x1.32, x1.11).

**Failed criterion.** none (PASS at threshold).

### Four-layer diagnosis
- **claim_alignment**: unclear -- a manipulation check for INV-063's P1 precondition; no leg of the falsifier is touched.
- **biological_reference**: partial -- novelty/entropy intake as the driver of sleep need (Huber 2004/2006 local sleep; Larkin 2014 CA1 novelty).
- **prerequisites**: present (R2 P0 converged 3/3 at 0.93-0.99; config fields equal 798a's; weights restored 12/12). Declared deviation: P0 shared per seed.
- **implementation**: complete
- **environment**: adequate -- shift counts grade 0 -> 15 -> 36 -> 90 and mean MEL rises 1.97e-5 -> 3.31e-5.
- **measurement**: adequate but THIN. Matched-class pass rate 4/6 -> ~1-in-4 void odds for a 3-seed gate (pooling the darwin execution gives 7/9 and ~1-in-8, but seeds 123/456 are identical across the two 798a executions to printed precision, so they are not independent draws).
- **integration**: coupled
- **scale**: likely insufficient for a gate that a long evidence run will hang on

### Failure location (GOV-FAILLOC-1)
- **mechanism**: established
- **measures**: partial
- **environment**: established
- **ree**: False
- **net_classification**: n/a (PASS). The manipulation check is real but under-powered at n=3.

### Biological reference
- **closest_mechanism**: waking novelty intake grading offline consolidation demand
- **dependencies**: []
- **is_formal_import**: False
- **divergence**: none identified
- **lit_status**: present (targeted_review_inv_063, 5 entries)

### Claim-layer recommendation
- direction: `non_contributory`
- epistemic_category: `standard` -- Clean manipulation check (a measurement-instrument validation, no build owed) at threshold; no category applies.
- per claim: INV-063: INV-063 carries no adjudication flag today; write the note above and -> set diagnostic_evidence_adjudicated true [none -- stays candidate]

**Draft evidence_quality_note.** V3-EXQ-1069 (diagnostic, PASS, inv063_p1_intake_ladder_gradeable): non_contributory for INV-063, by design. On 798a's configuration with P0 shared per seed, the SD-MEL-PRODUCER ladder grades waking MEL: monotone 3/3, relative spread 0.394 / 0.241 / 1.691 (floor 0.25), P1 met on 2/3 = exactly the requirement; robust to the episode-truncation control. Both indexer flags cleared as artefacts. Power: on the matched machine class (798a-linux 2/3, this run 2/3) the per-seed pass rate is 4/6, at which a 3-seed gate needing 2 voids about 1 time in 4; part of the 798a linux/darwin difference is a documented cross-machine-class divergence, which seeds on one box do not hedge. failure_autopsy_INV-063-1060-1063-1069-cluster_2026-09-20.

### Substrate queue
- **action**: none

### Brake, granularity, debt class
- re-derive brake: fired=False, literal count 0. PASS; category standard, no build owed by this target -> does not count.
- granularity trigger: fires=False. INV-063: 0 prior targets.
- debt class: closed for the question asked; aleatoric (irreducible) component named: per-seed P1 noise -- hedge with seeds, do not research.

### Learning extracted
- Three green self-routes do not add up to a green light: 1060 = wired; 1063 = one citeable direction finding, negative for leg B as registered; 1069 = gradeable at the boundary. With GFLAG-0382, no readable readout shows sleep improving the world-forward model.
- When the trained objective improves and the DV worsens on every seed, suspect the objective before the optimiser.
- A liveness criterion of the form 'parameter moved > 0' is met by any optimiser that saw any gradient. Report the move against the step scale.
- An OFF-arm attribution control is only as good as the evidence the rest of the pass ran. updates_e2 = 0 in all 12 cells was in the manifest; the cause is one missing call (record_transition).
- Driver and indexer disagree about applies:false. Every scoped-out-and-recorded precondition raises a false precondition_unmet today.
- WITHDRAWN (first draft): 'the converged model IS the identity predictor, so the DV cannot improve' -- seed 123 beats identity by 23%.

### Routing: `governance-note-only`

### Step 7b pre-routing fires
- C2: DISMISSED with reason -- that entry lists INV-063 in unblocks_claims but was CORRECTED 2026-09-15: it validates E2's SELF-forward path only and is closed. The entry that actually gates INV-063 leg B is e2-world-forward-sleep-trainer, which the 1060 and 1063 targets of this cluster amend. 1069 measures the P1 manipulation check and owes no substrate write.

## Read-across (NOT adjudicated)
- V3-EXQ-1071 / inv063_legb_tau_bind_20260920 (AWAITING USER REVIEW) -- NOT adjudicated. The across-sleep direction at the pinned tau=1e-3 on a converged 798a base HAS been measured by that session and is negative (-3.89e-01 at 18.54% headroom); readability needs tau <= 0.01, a positive delta needs tau >= 0.03, no overlap. Additional cautions for any ladder: P1 voids ~1 in 4 at n=3 on the matched machine class; 1069's scoped-out R1 (frozen probe responds to shock on 1/3 seeds) becomes relevant once a frozen battery is the DV; the inherited dead z_goal stream needs re-arguing for an evidence-purpose run.
- MECH-017 -- same fresh-optimiser property; see failure_autopsy_V3-EXQ-1057-1057a-cluster_2026-09-20
- indexer (_compute_adjudication) -- applies:false preconditions are recomputed as gating; route via governance_flag.py evidence_discrepancy

## Owed to governance
- GFLAG-0355 / 0359: reconcile e2-world-forward-sleep-trainer status
- GFLAG-0360 (INV-063, MECH-423): objective-mismatch correction
- GFLAG-0364 / 0367 / 0382: weigh together -- 0382 carries the contrary number against 0364's re-point
- INV-063 what_would_answer leg-B label E1 -> E2
- indexer: honour applies:false in _compute_adjudication, or change the driver convention (route via governance_flag.py)
- ree_core: record_transition has no caller, so the e2 self-forward consolidation module is never stepped

## Step 7c red-team (cluster level)
- **model**: opus (claude-opus-5[1m]); drafting session was fable -- cross-model pass
- **verdict**: CONTESTED
- **disposition_survived**: True
- **accepted**: ["F1 stale by 3 minutes: tau-bind doc + GFLAG-0382 already measured the direction at tau=1e-3 (negative); 1071 session stopped", "F2 identity-'floor' refuted by seed 123 (23% better); measured at alpha_world 0.3, not the ladder's 0.9", "F3 'identical configuration' / 'different seed each time' false; matched-class void odds ~1 in 4, not 1 in 8", "F4 'every weight moves 8 x lr' -> the most-moved weight; 0.008 is a step scale, not a bound", "F5 objective mismatch under-ranked"]
- **cleared**: updates_e2 = 0 mechanism PROVED from source (record_transition has no caller); C4 localisation of vacuous_pass; indexer applies:false artefact (mutation-tested); brake counts (INV-063 0, MECH-423 2); substrate-queue staleness
- **what_changed**: identity-floor claim withdrawn; fan-out reordered and moved to the ladder's regime; 1071 status corrected; GFLAG-0360/0382 added; void odds restated. Dispositions unchanged.
- **cheap_confirmers_run**: 15 of 20 recomputes exact; the 5 that differed are the corrections above

