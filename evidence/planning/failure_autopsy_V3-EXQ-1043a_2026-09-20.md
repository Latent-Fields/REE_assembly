# Failure autopsy -- V3-EXQ-1043a (MECH-537 communication subspace, permutation-null repair)

Status: awaiting_human_confirmation (Step 8 gate pending)
Target: `v3_exq_1043a_mech537_communication_subspace_permutation_null_20260919T030056Z_v3` -- diagnostic, FAIL, `substrate_not_ready_requeue`, indexer `precondition_unmet`. ree-cloud-2, 11.13 h, seeds 42-47. Instrument repair of V3-EXQ-1043 (autopsy 2026-09-17, read in full).

## 1. Facts (verified cell-by-cell by the red-team pass)
Dry-run gate clean. validate_recording OK. `substrate_stable_across_run: false` (ree-v3 main moved during the 11 h; single per-cell hash, so internally consistent).
Six of seven readiness gates green. Red: `randrank_control_supra_trivial` -- margin of the random-rank arm over the previous-action predictor, read at the parsimonious rank:

| seed | r_pars | full | comm | randrank | trivial | rand - trivial | C2 obs | null mean (sd) | p |
|---|---|---|---|---|---|---|---|---|---|
| 42 | 11 | 0.940 | 0.601 | 0.587 | 0.566 | 0.020 | -0.014 | 0.182 (0.023) | 1.0 |
| 43 | 11 | 0.934 | 0.588 | 0.635 | 0.580 | 0.054 | 0.047 | 0.229 (0.025) | 1.0 |
| 44 | 10 | 0.943 | 0.544 | 0.585 | 0.572 | 0.013 | 0.042 | 0.192 (0.026) | 1.0 |
| 45 | 8 | 0.921 | 0.531 | 0.562 | 0.554 | 0.008 | 0.031 | 0.190 (0.026) | 1.0 |
| 46 | 10 | 0.943 | 0.504 | 0.595 | 0.579 | 0.016 | 0.091 | 0.197 (0.026) | 1.0 |
| 47 | 10 | 0.947 | 0.510 | 0.614 | 0.570 | 0.044 | 0.103 | 0.216 (0.023) | 1.0 |

Complement arm 0.92-0.95 on every seed. Majority-class floor 0.25. At full rank the randrank margin is 0.21-0.24. C4b 2/6 (need 4). C5 premise holds (0.643 vs 0.216). Legacy 1043 predicate recomputed: 2/6, mean 0.04998 vs floor 0.05.

Dry-run gate: check_dry_run_citations.py run 2026-09-20 over all 11 cited run_ids (1039, 1039a, 1043, 1043a, 1057, 1057a, 1060, 1063, 1065, 1069, 1070): 0 dry, 11 clean. validate_experiments --checks dry_run_unreachable_criterion: silent on all nine drivers; reduction blocks read by hand.

## Target V3-EXQ-1043a -- diagnostic FAIL, claims MECH-537
`v3_exq_1043a_mech537_communication_subspace_permutation_null_20260919T030056Z_v3`

**Self-route** `substrate_not_ready_requeue` -- adjudication: CONFIRMED that no scientific leg is adjudicated (readiness gate red: randrank margin over the trivial predictor 0.0085-0.054 against a 0.05 floor, 5 of 6 seeds under). The gate is a MARGIN gate: the random-rank arm is above the trivial predictor on 6/6 seeds, just not by 0.05. The first draft's stronger reading ('no low-rank bottleneck; refuse 1043b') is WITHDRAWN after red-team: a rank 8-11 projection of 146 live sender dimensions reproduces the receiver to R2 0.996, the complement carries the action (0.92-0.95) and the communication subspace does not (0.50-0.60) -- which is MECH-537's registered routing phenotype, met on C1, C3, C4a (6/6 each) and C5 (0.643 vs chance 0.066). What is unresolved is ORIENTATION versus a random same-rank subspace (C2) and the in-run C4b ceiling (2/6).

**Failed criterion.** readiness (randrank_control_supra_trivial 0.0085 vs 0.05, worst seed 45; 5/6 under the floor, 6/6 above zero). Recorded, unadjudicated: C2 contrast positive 5/6, mean 0.04998, 95% CI [0.0051, 0.0948]; permutation clause 0/6; C4b 2/6.

### Four-layer diagnosis
- **claim_alignment**: unclear -- the registered phenotype is largely present and one discriminating contrast (orientation vs random rank-r) was not measurable with the instrument built. NOT a weakening.
- **biological_reference**: clear -- Semedo 2019 V1->V2, Binish 2026 PFC->M1, Gonzalez 2026; 12 entries.
- **prerequisites**: present (6 of 7 readiness gates green: source adequacy 0.921, elevation 0.353, RRR R2 0.997, encoder trained, not collapsed, held-out steps 1965).
- **implementation**: partial -- the probe is complete and faithful to the 1043 autopsy's four required changes; the encoder carries the declared SD-106 limitation.
- **environment**: adequate
- **measurement**: under-instrumented -- DOMINANT. The orientation contrast is read against ONE random draw per seed. The permutation clause answers a different question (is the fitted map real? yes, 200/200 on every seed) and its non-zero null mean is the normal signature of a fit that found structure, not a defect. The in-run C4b ceiling rule was flagged pre-queue (M2) as weak. The anchor-reachability guard passed at rank 32 for a gate read at rank 8-11.
- **integration**: coupled (the SCORED rank is not at the ladder ceiling; the CV-argmax rank is, 6/6 -- rrr_rank_at_ladder_ceiling true)
- **scale**: adequate at n=6 for what it measured; the legacy 1043 predicate recomputed on these numbers still fails (2/6, mean 0.04998 vs floor 0.05), so n was not the problem.

### Failure location (GOV-FAILLOC-1)
- **mechanism**: not_established
- **measures**: not_established
- **environment**: established
- **ree**: False
- **net_classification**: MEASURES; not chargeable to REE and not to MECH-537

### Biological reference
- **closest_mechanism**: inter-areal communication subspace (Semedo et al. 2019)
- **dependencies**: ["a receiver that reads a strict subset of sender variance", "a sender with private (non-communicated) dimensions"]
- **is_formal_import**: True
- **divergence**: none established. (First draft asserted 'no selective reader at this interface'; withdrawn -- the receiver has participation ratio ~4-6 against 146 live sender dims.)
- **lit_status**: present (targeted_review_mutual_legibility_communication_subspaces, 12 entries)

### Claim-layer recommendation
- direction: `non_contributory`
- epistemic_category: `standard` -- measurement_test_design_defect: the orientation question lacks its reference distribution. No suppression asserted on MECH-537; nothing needs building.
- per claim: MECH-537: category already standard; replace the 1043-era evidence_quality_note lead, resolve the standing 'DO NOT queue' vs EXP-1403 contradiction in notes (owed since the 1043 autopsy), and fix GFLAG-0310's mis-pointed provenance -> stamp this artifact [none -- stays candidate]

**Draft evidence_quality_note.** V3-EXQ-1043a (diagnostic, FAIL, substrate_not_ready_requeue; instrument repair of V3-EXQ-1043, n=6, 11.1h): non_contributory for MECH-537. One readiness gate red: at the parsimonious rank (8-11 of 146 live dims) the random-rank arm clears the previous-action predictor on 6/6 seeds but by less than the 0.05 floor on 5/6. Unadjudicated but recorded: the claim's routing phenotype is largely present (C1, C3, C4a 6/6; C5 premise 0.643 vs chance 0.066); the orientation contrast is positive on 5/6 seeds, mean 0.050, 95% CI [0.005, 0.095] -- excludes 0, includes the 0.05 floor, so H1-small-but-real's declared null is NOT met. The permutation clause (p = 1.0, 6/6) means all 200 shuffled refits decode WORSE than the real subspace: it shows the sender->receiver map is real; it does not test orientation against a random same-rank subspace, because that reference (many random draws; randrank is ONE draw per seed) was never built. failure_autopsy_V3-EXQ-1043a_2026-09-20.

### Substrate queue
- **action**: none

### Brake, granularity, debt class
- re-derive brake: fired=False, literal count 0. MECH-537 literal count 0. Instrument defect owing no build -> does not count.
- granularity trigger: fires=False. granularity_debt_cluster.py MECH-537: 1 target (1043, alignment unclear). No weakened target.
- debt class: complex (probe-gated) / puzzle (known rules) -- one missing instrument (a many-draw random-subspace reference), cheaper than what already ran.

### Learning extracted
- A refit-based permutation null answers 'is the fitted structure real?'. 'Is its ORIENTATION special?' needs a reference over random subspaces of the same rank. Decide which question a null answers before reading its p.
- p = 1.0 is not 'no information': here it is the most extreme attainable value, in the direction opposite to the confirming signature (200 of 200 shuffled fits decode worse).
- The pre-queue red-team (H2) named the rank-32-anchor vs rank-8-11-gate mismatch and the late firing, and the run was queued with the fix owed.
- A reachability guard must be evaluated at the operating point of the gate it covers.
- WITHDRAWN (first draft): 'a permutation null is only valid if centred at 0' and the between-episode-structure mechanism -- the driver's own M3 diagnostic (between-episode subspace decodes 0.60, shuffled fit 0.40) refutes the mechanism.

### Routing: `queue-experiment`
- **successor**: V3-EXQ-1043b, same question, same interface: replace the single randrank draw AND the permutation clause with a reference distribution over B random rank-r subspaces (decoder fits only, no RRR refits -- strictly cheaper than 1043a's 200 refits per seed); report the C2 CI as the pre-registered H1 statistic; re-specify the randrank readiness gate so it certifies the comparator can MOVE rather than that one draw clears 0.05.
- **early_abort_caution**: do NOT abort on the first seed: this margin has cross-seed sd 0.0186 on mean 0.0260 (failure_autopsy_V3-EXQ-999 learnings 6-7: a first-seed abort turns a high-variance gate into a coin flip). Evaluate over the seed set; record cells even when refusing.
- **user_decision**: whether to spend it. The first draft refused 1043b; the red-team showed that refusal rested on a premise the cells contest.
- **in_flight_check**: no 1043b script, queue entry or claim (2026-09-20)

### Hypothesis ledger (Step 9b)
- **qid**: mech537_communication_subspace_orientation
- **mode**: B (resolve; all three stay alive -- readiness red, elimination bar not met)
- **H1-small-but-real**: alive. resolving_runs += V3-EXQ-1043a. Pre-registered statistic (CI on the C2 mean): [0.0051, 0.0948] at the parsimonious rank, [0.0154, 0.0535] at rank 32 -- excludes 0, includes 0.05, declared null NOT met.
- **H2-no-orientation**: alive. resolving_runs += V3-EXQ-1043a. The permutation null it named ran and returned p = 1.0 on 6/6, but that statistic tests fit-existence (P(D_comm_perm <= D_comm)), not orientation vs random; uninformative for this leg.
- **H3-no-low-rank-bottleneck**: alive. resolving_runs += V3-EXQ-1043a. Declared null ('C2 flat in rank') NOT met: C2 mean 0.0345 at rank 32 vs 0.0500 at the parsimonious rank.

### Step 7c red-team
- **model**: opus (claude-opus-5[1m]); drafting session was fable -- cross-model pass
- **verdict**: CONTESTED
- **disposition_survived**: True
- **accepted**: ["F1 p=1.0 is reachable-and-extreme, not an artefact (significance needed D_comm < 0.33-0.37; floor 0.25)", "F2 proposed null mechanism refuted by the M3 diagnostic", "F3 H1's pre-registered CI never computed; ledger blocks missing", "F4 'no low-rank bottleneck' unsupported; registered phenotype largely met", "F5 'neither arm above trivial' false (randrank above on 6/6); 'not rank-censored' needs the scored-rank qualifier", "F6 146 live dims, not ~230"]
- **what_changed**: routing governance-note-only + refuse-1043b -> queue-experiment (in-place 1043b with a many-draw random-subspace reference); debt class mystery -> puzzle; biological divergence withdrawn; ledger blocks added. Direction/category unchanged.
- **cheap_confirmers_run**: 14 recomputes; brake recipe verbatim = 0; per-seed table reproduced cell by cell

