# Failure autopsy -- V3-EXQ-1070 (ARC-029 env operating-point feasibility)

Status: confirmed (Step 8 gate held 2026-09-20, user present; red-team opus cross-model CONTESTED, revisions applied)
Target: `v3_exq_1070_arc029_env_operating_point_feasibility_20260920T042654Z_v3` -- diagnostic, FAIL, `substrate_not_ready_requeue`, indexer `precondition_unmet`. ree-cloud-2, 3h31m, 5 rungs x 3 quantiles x 2 seeds.
A live session (`metaworker-science-20260920-arc029-1070a`, opened 09:34Z) is already repairing this as V3-EXQ-1070a. This autopsy reads that session's claims only; it touches none of its files.

## 1. Facts (verified cell-by-cell by the red-team pass)
Dry-run gate clean; validate_recording OK. Four of five readiness gates green (bar in force 1.0, window filled 30/30, rv collapse >= 1.27 decades, AST write-check 0). Red: `training_tick_budget_equalised` = 3.96 against a ceiling of 2.0.

| rung | premeasured ep len (random policy) | realised P0+P1 ticks, seed 0 / 42 | measured ep len after training |
|---|---|---|---|
| L0 lineage | 6.2 | 1099 / 1490 | 5.2-8.1 |
| L1 | 10.8 | 1825 / 1646 | 12.7-17.0 |
| L2 | 22.5 | 845 / 525 | 7.3-15.1 |
| L3 | 29.5 | 553 / 675 | 8.3-15.6 |
| L5 extreme | 40.0 (extrapolated) | 461 / 876 | 14.8-30.2 |

Design target ~1300 per (rung, seed). P1-feasible 30/30 cells; P3-feasible 19/30; rung-level jointly feasible 3/5 (L0, L1, L2).

Dry-run gate: check_dry_run_citations.py run 2026-09-20 over all 11 cited run_ids (1039, 1039a, 1043, 1043a, 1057, 1057a, 1060, 1063, 1065, 1069, 1070): 0 dry, 11 clean. validate_experiments --checks dry_run_unreachable_criterion: silent on all nine drivers; reduction blocks read by hand.

## Target V3-EXQ-1070 -- diagnostic FAIL, claims ARC-029
`v3_exq_1070_arc029_env_operating_point_feasibility_20260920T042654Z_v3`

**Self-route** `substrate_not_ready_requeue` -- adjudication: CONFIRMED. training_tick_budget_equalised is genuinely unmet (realised P0+P1 ticks 461..1825, spread 3.96 vs ceiling 2.0); no env verdict is licensed and D3 (3 of 5 rungs) must not be cited. The first draft RESCUED a P1 reading; that rescue is WITHDRAWN after red-team. The occupancy half of P1 cannot fail at q in {0.25, 0.5, 0.75}: the detrended quantile bar fires ~q of the time by design (e3_selector.py:915-919) and tests/contracts/test_commit_threshold_variance_tracking.py pins |frac - q| < 0.10 and mean run >= 3.0. And ARC-029's P1 is specified for the ALTERNATING arm on >= 4/5 seeds; this run asserts breath_period == 0 (MECH-108 off) with 2 seeds, so P1 as written was not measured. What the run does add over the contract: the bar took force end-to-end on a TRAINED agent (window filled 30/30), and the run-length floor survived at q=0.25 on the shortest-episode rung (3.86 vs 3.0), the cell the driver predicted would fail -- with the caveat that the window spanned 15-39 EPISODES in every cell, i.e. a cross-episode quantile, not the within-run one the estimator's drift premise describes.

**Failed criterion.** readiness (training_tick_budget_equalised 3.96 vs ceiling 2.0). D1, D2 passed; D3/D4 reported, not gating.

### Four-layer diagnosis
- **claim_alignment**: unclear (protected) -- this run is upstream of ARC-029's falsifier; it asks only whether an env operating point exists where P1 and P3 are jointly satisfiable.
- **biological_reference**: clear -- BG go/no-go commitment vs exploration modes (Humphries 2012; Schmidt 2013/2017 pause-cancel; Leventhal 2012 beta-stabilised state); 6 lit entries.
- **prerequisites**: present -- variance-tracking commit bar built 2026-09-18; rv collapse 1.27-1.88 decades in every (rung, seed).
- **implementation**: complete for the lever under test (bar_in_force_fraction 1.0 on 30/30 cells, window filled 30/30).
- **environment**: partial -- agent_health is hard-coded 1.0 with no constructor kwarg, so episode_length x |harm/step| is a conserved product; the ladder moves along it but cannot leave it. That is the open question, not a defect of this run.
- **measurement**: under-instrumented -- DOMINANT. Episode counts came from a random-policy pre-measurement (L5's 40.0 extrapolated) while _train_all_on_agent ends each episode on done. TRAINING-phase episode length vs the proxy: L1 -3%..+57%, L2 1.46x-2.78x shorter, L3 1.50x-2.79x, L5 1.43x-2.88x -> depth varied 4x along the manipulated dimension. Training and measurement are INTERLEAVED per (rung, seed); the spread first exceeded 2.0 at block 5 of 10, after 12 of 30 cells. P3 depends on policy competence and is confounded with depth.
- **integration**: coupled
- **scale**: unknown -- n=2 seeds, by design for a cheap diagnostic

### Failure location (GOV-FAILLOC-1)
- **mechanism**: established
- **measures**: not_established
- **environment**: partial
- **ree**: False
- **net_classification**: MEASURES (the training-budget instrument). Not chargeable to REE or ARC-029.

### Biological reference
- **closest_mechanism**: basal-ganglia commitment (go) vs deliberative (no-go/pause) operating modes with distinct risk profiles
- **dependencies**: ["a stable commit threshold relative to the agent's own variance statistics", "episodes long enough to contain both modes"]
- **is_formal_import**: False
- **divergence**: none identified
- **lit_status**: present (targeted_review_arc_029, 6 entries)

### Claim-layer recommendation
- direction: `non_contributory`
- epistemic_category: `standard` -- measurement / test-design defect (tick budget by proxy). The pre-registered 'no joint region -> substrate_conditional' disposition is NOT triggered and must not be applied from this run.
- per claim: ARC-029: category already standard; ARC-029 carries no diagnostic_evidence_adjudicated field, so write the note above and -> set diagnostic_evidence_adjudicated true [none -- stays candidate]

**Draft evidence_quality_note.** V3-EXQ-1070 (diagnostic, FAIL, substrate_not_ready_requeue): non_contributory for ARC-029. Readiness gate training_tick_budget_equalised unmet: realised training ticks 461..1825 across rung x seed (spread 3.96, ceiling 2.0), because per-rung episode counts were derived from a random-policy episode-length pre-measurement and the training agent's episodes ran 1.4x-2.9x shorter on L2/L3/L5 (L1 -3%..+57%). The joint-feasibility deliverable (3/5 rungs) is confounded with training depth and NOT citeable; the substrate_conditional disposition is NOT triggered. P1 is NOT discharged: the static quantile bar meets the occupancy band by construction, and P1 as registered (alternating arm, >= 4/5 seeds) was not run. Narrow residual: the variance-tracking bar took force on a trained agent in 30/30 cells (as a cross-episode quantile). Successor V3-EXQ-1070a was committed and claimed before this autopsy. failure_autopsy_V3-EXQ-1070_2026-09-20.

### Substrate queue
- **action**: none

### Brake, granularity, debt class
- re-derive brake: fired=False, literal count 0. ARC-029 literal count 0; instrument defect owing no build -> does not count.
- granularity trigger: fires=False. granularity_debt_cluster.py ARC-029: 4 targets, alignment unclear=4, none weakened -> measurement debt.
- debt class: complicated (buildable) -- the repair is a named driver change with no open question (budget by realised ticks).

### Learning extracted
- A verification statistic must be able to take the failing value. The red-team's 'realised 1710-1740, spread 1.02' (arc029_exq1066_prereg_derivation_20260919.md:394) reproduces EXACTLY as (ceil(400/L)+ceil(900/L)+ceil(400/L))*L over the pre-measured lengths: a design-time ceil() residue, bounded near 1 whatever training does, and denominated on a different phase set (it includes zworld P0a) from the precondition it was cited for.
- A random-policy pre-measurement is not a proxy for a training agent's episode length: up to 2.9x off, sign changing along the ladder.
- Before citing 'X held on N of N cells', ask whether X can fail. Occupancy ~ q is what a quantile bar is, and the substrate already pins it as a contract.
- Read the claim's precondition text before crediting a run with discharging it: P1 names the alternating arm; this run switched it off.
- Check the successor's actual design before writing requirements for it. 1070a existed, and had already rejected two of the first draft's four with reasons.

### Routing: `governance-note-only`
- **successor_exists**: V3-EXQ-1070a: ree-v3 a7c8c97 committed 2026-09-20T10:45:18Z, claimed by ree-cloud-2 10:50:35Z. It uses a two-stage per-(rung, seed) pilot and ONE trainer call.
- **first_draft_items_withdrawn**: ["'loop until the tick target is met' -- 1070a rejects chunked training with a mechanism: _train_all_on_agent constructs its optimisers internally, so every chunk boundary resets Adam moments, MORE often at short-episode rungs, re-introducing a rung-correlated confound", "'carry P1 = 30/30 forward as a prediction' -- 1070a refuses by design: a red gate licenses none of 1070's numbers"]
- **live_gaps_in_1070a**: ["training_tick_budget_equalised is still evaluated only in analyse(), after every cell has run", "the zworld P0a phase still budgets from LADDER_EP_LEN including L5's EXTRAPOLATED 40.0"]
- **pass_to_1070a_session**: 1070a's queue note quotes the L0 health-budget product as 1.159; the 1070 manifest reads 1.1812

### Step 7b pre-routing fires
- C1: DISMISSED with reasons -- none is a substitute for 1070a. v3_exq_1066 is the P1-P3 EVIDENCE design that was refused at /queue-experiment Step 4 (bar never took force at the lineage env); it is the run the pre-registered 'region_found' disposition re-queues AFTER a feasible operating point is known, i.e. downstream of 1070a. v3_exq_125a reuses the rv-forcing ablation vehicle the 063a autopsy found confounded (do not queue as-is). v3_exq_227 is the 2026-04 discrepancy diagnostic, a different question. Also on disk, untracked and owned by the live 1070a session: v3_exq_1049_arc029_threshold_side_commitment_harm.py.

### Step 7c red-team
- **model**: opus (claude-opus-5[1m]); drafting session was fable -- cross-model pass
- **verdict**: CONTESTED
- **disposition_survived**: True
- **accepted**: ["F1 occupancy half of P1 satisfied by construction (contract-pinned)", "F2 P1 as registered (alternating arm, >=4/5 seeds) not measured", "F3 two of four successor requirements contradict the committed 1070a", "F4 the '1710-1740' figure IS sourced and is a ceil() identity", "F5 divergence figures were measurement-phase, not training-phase", "F6 cross-episode window caveat omitted", "F7 L0 contrast re-imported a warm-budget artefact"]
- **what_changed**: rescued P1 reading withdrawn; routing queue-experiment -> governance-note-only (successor exists); successor requirements rewritten against 1070a. Direction/category unchanged.
- **cheap_confirmers_run**: 15 recomputes incl. brake 0 and granularity 4/unclear=4

