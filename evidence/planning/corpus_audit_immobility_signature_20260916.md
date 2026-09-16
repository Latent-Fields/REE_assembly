# Corpus audit 2 -- immobility signature (near-zero reach-dependent event counts) (read-only)

**Status: COMPLETE 2026-09-16T23:06:31Z (chip `chip-20260916-corpus-audits-contamination-immobility`, worktree `angry-leakey-c8b0a0`). Read-only: no manifest touched, no regen run, nothing queued. Companion report: `corpus_audit_contamination_footgun_20260916.md`.**

## 0. Provenance

- Trigger: `navigation_immobility_scoping_2026-08-18.md` section 3 recommended "a small, mechanical corpus audit (grep every manifest for its actual consumption/foraging/waypoint event-count field, wherever it is nested, and flag near-zero counts against non-zero eval-tick budgets)"; ratified 2026-09-16.
- The signature: an agent that moves on ~14/300 ticks and consumes nothing, so a reach-dependent DV is starved to a 0/0 denominator. Adjudicated there as MECH-439 F-dominance amplified by the E3 hold-and-repeat cadence, not a bug; already directly confirmed once (MECH-467 / V3-EXQ-874 -> 874b).

## 1. What was scanned

| Corpus | Count |
|---|---|
| Pack manifests `evidence/experiments/*/runs/*/manifest.json` | 2958 |
| Pack `metrics.json` siblings (scanned alongside; most event counts live here, under `values.*`) | 2944 |
| Packs carrying at least one metric the screen recognises as a reach-dependent count or rate | 102 |
| Packs with a derivable tick budget from `config` | 446 (plus 51 with only realised `z_goal_stream.ticks_total`) |
| Packs FLAGGED | 14 (10 chip-scored) |

## 2. Schema keys used

There is no standard event-count field: the corpus names these per script. The screen therefore matched numeric leaves at any depth of manifest + metrics whose key name is a reach-dependent **count** (`n_consumption_events`, `n_contact`, `n_contact_eval`, `train_contact_events`, `n_resource_events`, `n_approach_contacts_min`, `n_contact_steps`, `unique_cells`, `n_forage_steps`, ...) or **rate** (`resource_visit_rate[_mean][_<ARM>]`, `contact_rate*`, `goal_reach_rate`, `p_moved_*`, `foraging_competence`, ...), and EXCLUDED keys that are not counts (accuracy / gap / slope / significance / recall / spread / floor / threshold / `resource_respawn_on_consume` / `contact_gate` / `post_contact_steps`) and keys naming hazard or ethical contact (`contact_rate_ethical*`, `n_forage_hazards`) because there a low count is the avoidance DV working, not immobility. Rate semantics were checked in the scripts where flagged: `resource_visit_rate = resource_visits / total_steps` (V3-EXQ-072b line 261, 866 series), i.e. per tick, so `< 0.01` is literally "< 1% of ticks".

Tick budget, in order: `config.steps_per_episode * n_episodes`, then `config.{n_steps,n_ticks,num_ticks,eval_ticks,total_steps,max_steps}`, else the realised `z_goal_stream.ticks_total` (which is not a budget; flags against it are marked WEAK).

Flag tiers: **STRONG** = count == 0 or rate == 0 (budget-independent); **WEAK** = count < 1% of a config budget, count < 0.1% of realised ticks, or 0 < rate < 0.01.

Autopsy coverage: `scripts/check_autopsy_coverage.py` over the flagged run_ids (content-based, 513 artifacts).

## 3. Table -- flagged runs (14)

| # | queue_id | run_id | date | claim_ids | status / direction | S | metric read (STRONG first) | tier | tick budget (source) | existing autopsy |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | V3-EXQ-041 | v3_exq_041_full_pipeline_smoke_test_20260319T070039Z_v3 | 2026-03-19 | MECH-089, ARC-016, MECH-071 | FAIL / non_contributory | S | `n_contact_eval`=0 | STRONG | - (none) | grandfathered-wanting-liking-cluster_2026-08-08 (confirmed) |
| 2 | V3-EXQ-043 | v3_exq_043_sd003_trajectory_attribution_20260319T070057Z_v3 | 2026-03-19 | SD-003, MECH-102 | FAIL / weakens | S | `n_contact_eval`=0 | STRONG | - (none) | grandfathered-sd003-cluster_2026-08-08 (confirmed) |
| 3 | V3-EXQ-072b | v3_exq_072b_q021_behavioral_flatness_20260328T135541Z_v3 | 2026-03-28 | Q-021 | FAIL / non_contributory | S | `resource_visit_rate_nogo`=0; `resource_visit_rate_comp`=0; `resource_visit_rate_rand`=0 | STRONG | - (none) | grandfathered-r5-batch01-mixed-findings_2026-08-08 (confirmed) |
| 4 | V3-EXQ-072b | v3_exq_072b_q021_behavioral_flatness_20260402T012059Z_v3 | 2026-04-02 | Q-021 | FAIL / superseded |  | `resource_visit_rate_nogo`=0; `resource_visit_rate_comp`=0; `resource_visit_rate_rand`=0 | STRONG | - (none) | grandfathered-superseded-batch1_2026-08-08 (confirmed) |
| 5 | V3-EXQ-228b | v3_exq_228b_arc032_theta_bypass_onboarded_20260809T030541Z_v3 | 2026-08-09 | ARC-032 | FAIL / does_not_support | S | `resource_visit_rate_mean_THETA_ACTIVE`=0.00178364; `resource_visit_rate_mean_THETA_ZEROED`=0.00390018 | WEAK | 86889 (z_goal_stream.ticks_total) | V3-EXQ-228b_2026-08-09 (confirmed) |
| 6 | V3-EXQ-228c | v3_exq_228c_arc032_theta_bypass_readout_20260809T110214Z_v3 | 2026-08-09 | ARC-032 | FAIL / does_not_support | S | `resource_visit_rate_mean_THETA_ACTIVE`=0.00377297; `resource_visit_rate_mean_THETA_ZEROED`=0.00283114 | WEAK | 87742 (z_goal_stream.ticks_total) | V3-EXQ-228c_2026-08-10 (confirmed) |
| 7 | V3-EXQ-228d | v3_exq_228d_arc032_theta_phase_weighted_readout_20260811T234236Z_v3 | 2026-08-11 | ARC-032 | FAIL / does_not_support | S | `resource_visit_rate_mean_THETA_ACTIVE`=0.00361753; `resource_visit_rate_mean_THETA_ZEROED`=0.00388823 | WEAK | 86091 (z_goal_stream.ticks_total) | V3-EXQ-228d_2026-08-13 (confirmed) |
| 8 | V3-EXQ-728b | v3_exq_728b_trained_allon_capability_point_20260721T113845Z_v3 | 2026-07-21 | (none) | PASS / non_contributory |  | `_a_verdict/trained_allon_normalized_position/goal_reach_rate`=0 | STRONG | - (none) | no |
| 9 | V3-EXQ-866 | v3_exq_866_inv034_q021_goal_maintenance_agency_20260802T074409Z_v3 | 2026-08-02 | INV-034, Q-021 | FAIL / non_contributory | S | `resource_visit_rate_mean_FULL`=0.0046019; `resource_visit_rate_mean_AVOIDANCE_ONLY`=0.00610579 | WEAK | 50031 (z_goal_stream.ticks_total) | V3-EXQ-866_2026-08-02 (confirmed) |
| 10 | V3-EXQ-866a | v3_exq_866a_inv034_q021_goal_maintenance_agency_onboarded_20260803T075813Z_v3 | 2026-08-03 | INV-034, Q-021 | FAIL / non_contributory | S | `resource_visit_rate_mean_FULL`=0.00331043; `resource_visit_rate_mean_AVOIDANCE_ONLY`=0.00325847 | WEAK | 98980 (z_goal_stream.ticks_total) | V3-EXQ-866a-G0_2026-08-08 (confirmed); V3-EXQ-866a_2026-08-03 (confirmed) |
| 11 | V3-EXQ-866c | v3_exq_866c_inv034_q021_goal_maintenance_agency_onboarded_20260808T195345Z_v3 | 2026-08-08 | INV-034, Q-021 | FAIL / non_contributory | S | `resource_visit_rate_mean_FULL`=0.00327873; `resource_visit_rate_mean_AVOIDANCE_ONLY`=0.00297323 | WEAK | 114407 (z_goal_stream.ticks_total) | V3-EXQ-866c_2026-08-08 (confirmed) |
| 12 | V3-EXQ-874b | v3_exq_874b_mech467_distractor_three_leg_battery_20260816T222900Z_v3 | 2026-08-16 | MECH-467 | FAIL / non_contributory | S | `per_seed[0]/arms/ARM_REPLAY_SIMPLE/n_consumption_events`=0; `per_seed[0]/arms/ARM_REPLAY_COMPLEX/n_consumption_events`=0; `per_seed[1]/arms/ARM_PRECOMMIT_SIMPLE/n_consumption_events`=0 (+9 more) | STRONG | 28674 (z_goal_stream.ticks_total) | V3-EXQ-874b_2026-08-17 (confirmed) |
| 13 | V3-EXQ-899 | v3_exq_899_arc030_mech307_g0_readiness_20260808T153148Z_v3 | 2026-08-08 | (none) | FAIL / non_contributory |  | `/metrics/resource_visit_rate_mean_FULL_M307_ON`=0.0026633; `/metrics/resource_visit_rate_mean_FULL_M307_OFF`=0.00277709; `/arm_results[0]/resource_visit_rate`=0.00277111 (+30 more) | WEAK | 203971 (z_goal_stream.ticks_total) | no |
| 14 | V3-EXQ-899 | v3_exq_899_arc030_mech307_g0_readiness_20260808T214833Z_v3 | 2026-08-08 | (none) | FAIL / non_contributory |  | `resource_visit_rate_mean_FULL_M307_ON`=0.00400506; `resource_visit_rate_mean_FULL_M307_OFF`=0.00390044 | WEAK | 201003 (z_goal_stream.ticks_total) | V3-EXQ-899_2026-08-09 (confirmed) |

Per-row reading (script checked where the metric name alone is ambiguous):

- **V3-EXQ-874b** (MECH-467): the known case, caught by the screen -- 7 of 12 arm x seed cells report `n_consumption_events = 0`, the rest 1-3, against 300-tick windows. Already autopsied (874b 2026-08-17) and re-measured (940/941).
- **V3-EXQ-866 / 866a / 866c** (INV-034, Q-021): `resource_visit_rate_mean_FULL` 0.003-0.005 per tick -- the FULL agent visits a resource on < 0.5% of ticks. The `AVOIDANCE_ONLY` arm's low rate is by design (script line 116 uses it as the quiescence baseline) and is not itself a finding; the FULL arm's is the immobility shape. All three autopsied; all `non_contributory`.
- **V3-EXQ-228b / 228c / 228d** (ARC-032): `resource_visit_rate_mean_THETA_ACTIVE` and `_THETA_ZEROED` both 0.002-0.004 per tick. Both arms near-immobile, so the theta manipulation was measured on a starved denominator. All three autopsied; all `does_not_support`.
- **V3-EXQ-072b** (Q-021, two runs, one superseded): `resource_visit_rate_{nogo,comp,rand}` all exactly 0.0 -- including the random-policy arm, which suggests the visit counter or the resource placement was inert rather than the agent immobile. Autopsied.
- **V3-EXQ-041, 043** (MECH-089/ARC-016/MECH-071; SD-003/MECH-102): `n_contact_eval = 0`, where `n_contact = len(scores_by_ttype["contact"])` is the count of eval transitions typed `contact` in the SD-003 trajectory-attribution scoring (script lines 322 / 373). That is a reach-dependent denominator at zero (the contact-attribution DV is undefined), but "contact" there covers hazard as well as resource contact, so it is ambiguous whether it is immobility or a hazard-free eval. Both 2026-03 runs, both autopsied.
- **V3-EXQ-728b** (no claims): `goal_reach_rate = 0.0`, the fraction of episodes collecting >= 1 resource, on the trained-all-on capability-point probe; the manifest itself labels the block `reported_context_not_a_verdict`. Not autopsied; carries no claim.
- **V3-EXQ-899** (no claims; two packs): `resource_visit_rate*` 0.003-0.004 per tick across FULL_M307_ON/OFF arms; `non_contributory` readiness probe.

## 4. What this does and does not show

- It DOES show every run in the corpus whose recorded reach-dependent count or per-tick rate is zero or below 1% of ticks, against the run's own recorded budget, and that all but 2 of them (V3-EXQ-728b 2026-07-21, V3-EXQ-899 2026-08-08) already carry an autopsy. Nothing new to adjudicate surfaced beyond what `/failure-autopsy` had already seen; the immobility signature is, on the recorded evidence, already accounted for where it occurs.
- It does NOT show that the other 2856 packs are free of the signature. Only 102 packs record a recognisable event count or rate at all; the rest either record no reach-dependent telemetry (V3-EXQ-884, the documented 32/19/90-of-400-step death, records nothing the screen can read -- it is caught by audit 1, not this one) or record it under a name the pattern does not know. The blind spot is the corpus's telemetry practice (memory `feedback_fishtank_telemetry_maximalism`: record generously), not the scan.
- The screen is a screen. A low visit rate is the immobility signature only when the arm was supposed to approach; avoidance-only arms, hazard-contact rates and readiness probes that deliberately fix the policy are excluded by name where the name says so, but not every such case is nameable, so each row above has its script noted.
- Rates below 1% are flagged against the navigation doc's 14/300-tick figure (4.7% movement, 0% consumption); a threshold of 1% on *consumption* is conservative and would miss a run that consumes on 2% of ticks yet is still under-powered for its DV.

## 5. Routing (recommendation only -- nothing applied)

One `evidence_discrepancy` governance flag for this audit, listing the claims whose scored evidence includes a flagged run, so `/governance` can confirm each already-autopsied disposition covers the immobility reading (and can decide whether 728b / 899, which carry no claim, need anything at all). **Not raised by this session:** the flags registry is owned by the active claim `campaign-w-scripts-corpus-20260916` (see audit 1 section 9). The exact command:

```bash
/opt/local/bin/python3 /Users/dgolden/REE_Working/scripts/governance_flag.py raise --flag-type evidence_discrepancy \
  --claim-id ARC-016 --claim-id ARC-032 --claim-id INV-034 --claim-id MECH-071 --claim-id MECH-089 --claim-id MECH-102 --claim-id MECH-467 --claim-id Q-021 --claim-id SD-003 \
  --summary "Corpus audit corpus_audit_immobility_signature_20260916.md: 14 runs (10 chip-scored) record a reach-dependent event count or per-tick rate at zero or below 1% of ticks (the MECH-439/E3-cadence immobility signature of navigation_immobility_scoping_2026-08-18.md); all but V3-EXQ-728b and 899 are already autopsied. Confirm per listed claim that the existing disposition accounts for a starved denominator rather than a substantive null."
```

**RAISED 2026-09-16T23:22:18Z as `GFLAG-0305`** (`evidence_discrepancy`, 9 claims) by session `angry-leakey-c8b0a0`, once the blocking claim `campaign-w-scripts-corpus-20260916` closed. Landed `REE_assembly` `2f097b859c`, verified on `origin/master`; `status: open`, awaiting `/governance` adjudication.
