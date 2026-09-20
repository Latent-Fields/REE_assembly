# Failure autopsy (cluster) -- V3-EXQ-1057 + V3-EXQ-1057a (MECH-017, additive-budget replay arm)

Status: confirmed (Step 8 gate held 2026-09-20, user present; red-team opus cross-model CONTESTED, revisions applied)
Targets: `v3_exq_1057_..._20260918T211119Z_v3` (ree-cloud-2, 8.6 min) and `v3_exq_1057a_..._pass_order_20260918T234946Z_v3` (ree-worker-3, 14 min). Both `experiment_purpose: evidence`, FAIL, `substrate_not_ready_requeue`, `non_degenerate: false`, manifest direction `inconclusive` (a diagnosis-pending value). Routed here by the "evidence FAIL flagged degenerate" net. Predecessor: V3-EXQ-1048 autopsy 2026-09-17 (mixed; read in full), which named this successor question.

## 1. Facts (verified cell-by-cell by the red-team pass)
Dry-run gate clean; validate_recording OK on both. Question: is replay's recency cost intrinsic, or what is left when a fixed gradient budget is spent away from the recent window? Device: an additive arm D with A's whole-buffer pass AND B's recent-window pass (2N steps).

Mean E1 held-out MSE over 5 seeds (x 1e-5):

| arm | early probes | late probes |
|---|---|---|
| A whole-buffer replay | 8.0 | 10.4 |
| B budget-matched recent | 14.7 | 7.8 |
| C no extra training | 17.5 | 9.5 |
| D1 whole THEN recent (= 1057's D) | 17.4 | 8.1 |
| D2 recent THEN whole | 7.5 | 11.3 |

1057: `additive_arm_retains_replay_gain` 0/5 (D1 early is 11-28% WORSE than B on every seed; D1 late / B = 0.95-1.11). 1057a: replay gain retained by D2 5/5, but `additive_arm_retains_recency_benefit_d2` 2/5. Neither run reached C1-C4.

Dry-run gate: check_dry_run_citations.py run 2026-09-20 over all 11 cited run_ids (1039, 1039a, 1043, 1043a, 1057, 1057a, 1060, 1063, 1065, 1069, 1070): 0 dry, 11 clean. validate_experiments --checks dry_run_unreachable_criterion: silent on all nine drivers; reduction blocks read by hand.

## Cluster reading
**Shape.** two evidence-purpose FAILs on one claim, same harness, each refusing on the retention gate OPPOSITE to the other's pass order

**Independent bugs?** no -- one structural property.

**Structural property.** Two BLOCKED sequential passes over conflicting data windows do not combine on this harness; pass ORDER determines which way the additive arm is displaced. Whole-then-recent cancels to the untrained control on early probes (worse than both parents, 5/5). Recent-then-whole keeps and extends the early gain (best early arm of five) and loses the late one. Neither order delivers both parents' benefits. The mechanism is NOT established: the first draft's 'fresh Adam per call' account was refuted in-run (wake training is 18 such calls and accumulates).

**Readings.** test_design_ceiling

**Planning decision forced.** stop lettering the blocked construction; run the final-pass dose ladder (and, if specified properly, an interleaved arm) as the LAST letter, or accept V3-EXQ-1048's mixed reading as the record.

## Target V3-EXQ-1057 -- evidence FAIL, claims MECH-017
`v3_exq_1057_mech017_reality_consolidation_replay_additive_budget_20260918T211119Z_v3`

**Self-route** `substrate_not_ready_requeue` -- adjudication: CONFIRMED. additive_arm_retains_replay_gain 0/5. D (whole buffer THEN recent window) is worse than BOTH parents on early probes on 5/5 seeds (D/B 1.11-1.28, D/A 2.02-2.33) and lands at the NO-TRAINING control (D/C early 0.997; forgetting ratio 2.73 vs C's 2.48), while staying within 5-11% of B on late probes. Two passes that each help, run back to back, cancel on the early window: destructive interference, not a collapse onto B. Ungated, C4 would have passed 4/5 and stamped 'supports' off an arm that had lost replay.

**Failed criterion.** readiness (additive_arm_retains_replay_gain 0 of 5 vs 4); C4 never evaluated

### Four-layer diagnosis
- **claim_alignment**: unclear -- not exercised (gated out before C1-C4).
- **biological_reference**: partial -- see biological_reference.divergence
- **prerequisites**: present (14/15 gates green; forgetting present 2.49x, replay covers early regime 0.73, consolidator updated E1/E2 96 steps each).
- **implementation**: complete -- the consolidator does what it is asked; A/B/C cells are bit-identical to V3-EXQ-1048's on the same box.
- **environment**: adequate
- **measurement**: misleading -- DOMINANT: the manipulated arm is not the construct. Two BLOCKED sequential passes over conflicting data windows do not combine on this harness; order determines which way the arm is displaced. The first draft attributed this to CrossModuleConsolidator building a fresh Adam per call; WITHDRAWN -- wake training in the same run is 18 fresh-Adam calls of the same function at 5x the lr and accumulates, as do ARM_A's four. The blocked SCHEDULE is implicated, not the optimiser.
- **integration**: coupled
- **scale**: adequate

### Failure location (GOV-FAILLOC-1)
- **mechanism**: established
- **measures**: not_established
- **environment**: established
- **ree**: False
- **net_classification**: MEASURES (the additive-budget ARM construction). Not chargeable to REE or to MECH-017.

### Biological reference
- **closest_mechanism**: complementary learning systems: hippocampal replay INTERLEAVES old and new experience into neocortex (McClelland 1995; Kumaran 2016)
- **dependencies**: ["interleaving of remote and recent traces within one consolidation episode", "slow cortical learning rate"]
- **is_formal_import**: True
- **divergence**: LOAD-BEARING: 'additive budget' was built as two BLOCKED sequential passes. The reference system's answer to interference between remote and recent traces is INTERLEAVING within a consolidation episode (McClelland 1995; Kumaran 2016). The arm tests the schedule biology avoids, and it shows the interference biology avoids it for.
- **lit_status**: present (targeted_review_mech_017, 5 entries)

### Claim-layer recommendation
- direction: `non_contributory`
- epistemic_category: `standard` -- measurement_test_design_defect (arm construction). No suppression asserted; MECH-017's standing reading is still V3-EXQ-1048's (mixed).
- per claim: MECH-017: STANDS [none -- stays candidate]
- note: No claim-layer or scoring change is owed. Both runs already index as scoring_excluded: degenerate (non_degenerate false short-circuits before direction is read, build_experiment_indexes.py:3777-3783), and 'inconclusive' is inside the indexer's direction enum. Do NOT copy annotations into the run-pack manifest: the flat overlay that supplies non_degenerate:false fires only while the pack is un-annotated (:1770).

**Draft evidence_quality_note.** V3-EXQ-1057 (evidence-purpose, FAIL, substrate_not_ready_requeue, non_degenerate false; already scoring_excluded): does not bear on MECH-017. The additive arm (whole-buffer pass then recent-window pass) failed its retention gate 0/5: on early probes it fell to the no-training control, worse than both parents (destructive interference between blocked passes over conflicting windows). Instrument finding. failure_autopsy_V3-EXQ-1057-1057a-cluster_2026-09-20.

### Substrate queue
- **action**: none

### Brake, granularity, debt class
- re-derive brake: fired=False, literal count 0. MECH-017 literal count 0. Instrument defect owing no build -> neither run counts.
- granularity trigger: fires=False. granularity_debt_cluster.py MECH-017: 1 target (1048, free-text alignment 'mixed'). The 1048 autopsy recorded the two-claims-in-one-id observation and the user chose record-not-route; two instrument refusals do not change that.
- debt class: complex (probe-gated) / puzzle (known rules) -- two live hypotheses about the recency cost (intrinsic vs budget reallocation) and no arm yet built that can separate them.

### Learning extracted
- Blocked sequential passes over conflicting windows interfere; they do not add. Whole-then-recent cancels to the untrained control on early probes; recent-then-whole keeps and extends the early gain and loses the late one.
- WITHDRAWN (first draft): 'fresh Adam per consolidate() call makes passes overwrite'. The same call accumulates 18 times per cell in wake training. Test a proposed mechanism against other uses of the same code path in the same run.
- Compare a manipulated arm with the CONTROL as well as with its parents: D1 ~= C was the most informative number in the cluster and no gate reads it.
- 'Within noise' needs the run's own noise band (0.8% here, declared). 7-26% is heterogeneity of a real effect.
- Both retention gates earned their keep: ungated, 1057 stamps supports and 1057a weakens from one instrument.
- 1048 vs 1057 on one box are bit-identical on A/B/C; 1057 vs 1057a on two boxes of the same machine_class string differ by up to 3.2% in a cell.

### Routing: `queue-experiment`

**Fan-out (GOV-FANOUT-1).** Live hypotheses:
- H-intrinsic: the recency cost is intrinsic to training on remote traces, at any budget
- H-reallocation: the recency cost is what is left when a fixed budget is spent away from the recent window
- H-schedule: on a blocked schedule the displacement is set by pass ORDER, so 'cost' and 'benefit' are schedule artefacts (open -- NOT established; the first draft stated it as the structural property)

Probes:
- all three [measurement]: FIRST: dose ladder on the final pass -- after a fixed whole-buffer pass run k in {0, 3, 6, 12, 24} recent-window steps (and the mirror), tracing early and late MSE against k, with C as a plotted reference. It can explain why the additive budget buys early retention only. Null: both curves flat in k.
- H-reallocation vs H-intrinsic [algorithm]: interleaved arm D3: alternate single whole-buffer and recent-window steps inside ONE optimisation (needs either a driver-built mixture buffer or a consolidate() that accepts a per-step window; specify which before queueing -- the sketch is under-specified as it stands). Both retention gates kept.

GOV-FANOUT-1. Two letters have now circled one construction. If the interleaved arm ALSO fails both retention gates, stop: the additive-budget question is not answerable at this dose on this consolidator and the honest record is V3-EXQ-1048's mixed reading.

## Target V3-EXQ-1057a -- evidence FAIL, claims MECH-017
`v3_exq_1057a_mech017_reality_consolidation_replay_additive_budget_pass_order_20260918T234946Z_v3`

**Self-route** `substrate_not_ready_requeue` -- adjudication: CONFIRMED. With order reversed, D2 (recent THEN whole) retained replay's early gain 5/5 and is the BEST early arm of all five (7.48e-5 vs A 8.03e-5; forgetting ratio 1.17 vs A 1.25), but is worse than A on late probes on 3/5 seeds (D2/A 1.26, 1.15, 0.91, 0.84, 1.12) -> additive_arm_retains_recency_benefit_d2 2/5. These gaps are 9-32x the run's declared 0.8% noise band, so they are real and seed-heterogeneous, not noise: D2 is partially additive -- A's early benefit and more, none of B's late benefit. (First-draft wording 'D2 IS A within seed noise' WITHDRAWN.)

**Failed criterion.** readiness (additive_arm_retains_recency_benefit_d2 2 of 5 vs 4); C4 never evaluated (it would have read 1/5)

### Four-layer diagnosis
- **claim_alignment**: unclear -- not exercised.
- **biological_reference**: partial -- see biological_reference.divergence
- **prerequisites**: present (17/18 gates green).
- **implementation**: complete
- **environment**: adequate
- **measurement**: misleading -- DOMINANT: the manipulated arm is not the construct. Two BLOCKED sequential passes over conflicting data windows do not combine on this harness; order determines which way the arm is displaced. The first draft attributed this to CrossModuleConsolidator building a fresh Adam per call; WITHDRAWN -- wake training in the same run is 18 fresh-Adam calls of the same function at 5x the lr and accumulates, as do ARM_A's four. The blocked SCHEDULE is implicated, not the optimiser.
- **integration**: coupled
- **scale**: adequate

### Failure location (GOV-FAILLOC-1)
- **mechanism**: established
- **measures**: not_established
- **environment**: established
- **ree**: False
- **net_classification**: MEASURES (the additive-budget ARM construction). Not chargeable to REE or to MECH-017.

### Biological reference
- **closest_mechanism**: complementary learning systems: hippocampal replay INTERLEAVES old and new experience into neocortex (McClelland 1995; Kumaran 2016)
- **dependencies**: ["interleaving of remote and recent traces within one consolidation episode", "slow cortical learning rate"]
- **is_formal_import**: True
- **divergence**: LOAD-BEARING: 'additive budget' was built as two BLOCKED sequential passes. The reference system's answer to interference between remote and recent traces is INTERLEAVING within a consolidation episode (McClelland 1995; Kumaran 2016). The arm tests the schedule biology avoids, and it shows the interference biology avoids it for.
- **lit_status**: present (targeted_review_mech_017, 5 entries)

### Claim-layer recommendation
- direction: `non_contributory`
- epistemic_category: `standard` -- measurement_test_design_defect (arm construction). No suppression asserted; MECH-017's standing reading is still V3-EXQ-1048's (mixed).
- per claim: MECH-017: STANDS [none -- stays candidate]
- note: No claim-layer or scoring change is owed. Both runs already index as scoring_excluded: degenerate (non_degenerate false short-circuits before direction is read, build_experiment_indexes.py:3777-3783), and 'inconclusive' is inside the indexer's direction enum. Do NOT copy annotations into the run-pack manifest: the flat overlay that supplies non_degenerate:false fires only while the pack is un-annotated (:1770).

**Draft evidence_quality_note.** V3-EXQ-1057a (evidence-purpose, FAIL, substrate_not_ready_requeue, non_degenerate false; already scoring_excluded): does not bear on MECH-017. Reversed order (recent then whole): replay's early gain retained 5/5 and exceeded (best early arm of five), recency benefit retained 2/5. Partially additive -- early only. With 1057: order decides which way a blocked two-pass arm is displaced; neither order delivers both parents' benefits. The intrinsic-vs-reallocation question stays OPEN. failure_autopsy_V3-EXQ-1057-1057a-cluster_2026-09-20.

### Substrate queue
- **action**: none

### Brake, granularity, debt class
- re-derive brake: fired=False, literal count 0. MECH-017 literal count 0. Instrument defect owing no build -> neither run counts.
- granularity trigger: fires=False. granularity_debt_cluster.py MECH-017: 1 target (1048, free-text alignment 'mixed'). The 1048 autopsy recorded the two-claims-in-one-id observation and the user chose record-not-route; two instrument refusals do not change that.
- debt class: complex (probe-gated) / puzzle (known rules) -- two live hypotheses about the recency cost (intrinsic vs budget reallocation) and no arm yet built that can separate them.

### Learning extracted
- Blocked sequential passes over conflicting windows interfere; they do not add. Whole-then-recent cancels to the untrained control on early probes; recent-then-whole keeps and extends the early gain and loses the late one.
- WITHDRAWN (first draft): 'fresh Adam per consolidate() call makes passes overwrite'. The same call accumulates 18 times per cell in wake training. Test a proposed mechanism against other uses of the same code path in the same run.
- Compare a manipulated arm with the CONTROL as well as with its parents: D1 ~= C was the most informative number in the cluster and no gate reads it.
- 'Within noise' needs the run's own noise band (0.8% here, declared). 7-26% is heterogeneity of a real effect.
- Both retention gates earned their keep: ungated, 1057 stamps supports and 1057a weakens from one instrument.
- 1048 vs 1057 on one box are bit-identical on A/B/C; 1057 vs 1057a on two boxes of the same machine_class string differ by up to 3.2% in a cell.

### Routing: `queue-experiment`

**Fan-out (GOV-FANOUT-1).** Live hypotheses:
- H-intrinsic: the recency cost is intrinsic to training on remote traces, at any budget
- H-reallocation: the recency cost is what is left when a fixed budget is spent away from the recent window
- H-schedule: on a blocked schedule the displacement is set by pass ORDER, so 'cost' and 'benefit' are schedule artefacts (open -- NOT established; the first draft stated it as the structural property)

Probes:
- all three [measurement]: FIRST: dose ladder on the final pass -- after a fixed whole-buffer pass run k in {0, 3, 6, 12, 24} recent-window steps (and the mirror), tracing early and late MSE against k, with C as a plotted reference. It can explain why the additive budget buys early retention only. Null: both curves flat in k.
- H-reallocation vs H-intrinsic [algorithm]: interleaved arm D3: alternate single whole-buffer and recent-window steps inside ONE optimisation (needs either a driver-built mixture buffer or a consolidate() that accepts a per-step window; specify which before queueing -- the sketch is under-specified as it stands). Both retention gates kept.

GOV-FANOUT-1. Two letters have now circled one construction. If the interleaved arm ALSO fails both retention gates, stop: the additive-budget question is not answerable at this dose on this consolidator and the honest record is V3-EXQ-1048's mixed reading.

## Cluster routing
- **refused**: a third sequential-pass letter
- **successor**: one run, V3-EXQ-1057b, the LAST letter: dose ladder on the final pass first (it explains the early-only additivity), interleaved arm second and only once its sampler is specified. Both retention gates kept; add D-vs-C as a reported reference. Pre-register that a failure of both gates again ends the additive-budget line. Evaluate gates over the full seed set (V3-EXQ-999 learnings 6-7).
- **in_flight_check**: no 1057b script, queue entry or claim (checked 2026-09-20)

## Read-across (NOT adjudicated)
- MECH-423 -- MECH-423's R3 interleaved schedule interleaves MODULES within a call, not data windows across calls; nothing here bears on 680e.
- INV-063 cluster of this date -- WITHDRAWN: the first draft read one shared 'fresh-optimiser' property across both clusters. Not supported.

## Step 7c red-team (cluster level)
- **model**: opus (claude-opus-5[1m]); drafting session was fable -- cross-model pass
- **verdict**: CONTESTED
- **disposition_survived**: True
- **accepted**: ["F1 'D1 -> B' refuted: D1 is at the no-training control, worse than both parents", "F2 fresh-Adam mechanism falsified in-run (wake training, ARM_A)", "F3 'D2 IS A within noise' contradicts the declared 0.8% band; D2 is the best early arm", "F4 the inconclusive->non_contributory disposition is inert (already scoring_excluded: degenerate; 'inconclusive' is in the enum)", "F5 annotating the run-pack copy would suppress the flat overlay", "F6 D3 sketch under-specified"]
- **what_changed**: structural property restated as a schedule finding with the mechanism open; per-claim change -> STANDS; INV-063 read-across withdrawn; fan-out reordered (dose ladder first). Direction/category unchanged.
- **cheap_confirmers_run**: 12/12 recomputes matched (ratios, gates 0/5 and 2/5, C4 counterfactuals 4/5 and 1/5, brake 0, cross-box 3.19%)

