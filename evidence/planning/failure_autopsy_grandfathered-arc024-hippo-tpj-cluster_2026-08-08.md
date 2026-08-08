# Failure Autopsy: ARC-024/MECH-071 + MECH-089 hippocampal + MECH-095/MECH-099 TPJ, 17 nominal / 11 formal targets

**Generated:** 2026-08-08T19:22:21Z
**Scope:** cluster (3 threads, round-4 grandfathered-backlog sweep)
**Status:** confirmed

## Dry-run gate and deduplication

`check_dry_run_citations.py` over all 17 nominal run_ids: 0 dry cited, 17 clean. Two runs are functionally-degenerate pilots the automated flag cannot catch (`098b`@155304Z: warmup=5eps/eval=3eps, 1 seed, attr_auc=0.5000=chance; `121`@195503Z: min_contacts=10, fails its own C4 gate, 1 seed) -- treated as thin/uninformative shakedowns per the skill's small-N caution, excluded from evidentiary weight, not counted as independent replicates. `052`'s two batch-form ids (prefix/suffix directory naming) are confirmed the same physical manifest.

## Thread 1 -- ARC-024/MECH-071 training-depth + MECH-102 satellite (4 runs, fully covered)

`033`, `039` cite `failure_autopsy_grandfathered-wanting-liking-cluster_2026-08-08.json` (MECH-071/MECH-112/MECH-117 wanting/liking closure, both `superseded` by EXQ-232 PASS 2026-04-05). `045` is the same physical run as `v3_exq_045_mech102_ethical_ttype_20260319T201636Z_v3`, confirmed via identical `timestamp_utc`/`claim_ids`/`verdict` across both directory-naming conventions -- covered under Thread 2 of `failure_autopsy_grandfathered-arc024-arc033-sd005-cluster_2026-08-08.json`. No new work owed.

## Thread 2 -- MECH-089 hippocampal theta/multirate (6 unique runs)

MECH-089's own claims.yaml note already narrates EXQ-066 and EXQ-122 FAILs in full detail and states explicitly: "uniform static-k theta batching (k=1,2,4) is CONFIRMED HARMFUL... a run using only static-k configurations cannot reopen this question." SD-006's note already fully explains EXQ-052's FAIL as a diagnostic bug (wrong buffer attribute, silently-caught AttributeError), resolved by EXQ-052b PASS.

**066 and 122 (both timestamps)**: backfill registration only, matching the already-correct claims.yaml narrative. **052**: backfill only, diagnostic bug already resolved.

**CORRECTION (round-5 sweep, 2026-08-08):** this section originally described 122's two timestamps as `195503Z`/`220939Z` with AUC/min_contacts content ("thin 1-seed pilot... AUC_ON=0.64>AUC_ABLATED=0.36... well-powered 2-seed... AUC_ON=0.41<AUC_ABLATED=0.75"). **That content-swap error is now fixed in the JSON artifact** — those AUC/min_contacts figures actually belong to `v3_exq_121_mech095_agency_attribution_pair` (MECH-095), not EXQ-122 (MECH-089), and were mislabeled under the wrong run_ids despite this file's own text at the time asserting the two families were "confirmed distinct via claim_ids and script name" — an assertion never actually checked against the real run_ids on disk. The real EXQ-122 timestamps are `200134Z` (already digested in MECH-089's claims.yaml note: harm_auc_ON=0.489 vs ABLATED=0.625, delta=-0.135, 32 harm steps) and `221059Z` (a genuinely fresh, well-powered replicate never previously folded in: harm_auc_on=0.505, harm_auc_ablated=0.633, delta=-0.128, 1094 harm steps — same adverse direction at much higher power). Both are `standard`/`weakens`, reinforcing MECH-089's own "do not re-litigate" static-k finding rather than reopening it. Found by round-5's disciplined coverage-verification pass. See each corrected target's `amendment_note`/`recommended_evidence_quality_note` in the JSON for the full trail.

**042 (both timestamps, one experimental event) -- the thread's genuinely fresh finding.** Neither SD-004 nor ARC-007's claims.yaml note mentions EXQ-042 anywhere despite extensive notes covering EXQ-114/397/397c/809/817/817a/114a (confirmed by full-text search). Source-read (`ree-v3/experiments/v3_exq_042_hippocampal_terrain_training.py:191-207`): the terrain_prior behavioral-cloning training loop is correctly wired -- real `zero_grad()`/`backward()`/`step()`, gradient flows through `terrain_prior`'s own weights per the driver's own comment. This rules out the sense()-only missing-training-loop defect confirmed elsewhere in this backlog (V3-EXQ-032-family) -- `terrain_loss` stays flat at 311.27 across the full run (0% reduction) while C4/C5 data-sufficiency gates both fail hard (`n_approach_eval=5` vs floor 30; `world_forward_r2=0.0`). This reads as genuine under-training / insufficient signal, not a wiring bug. `070048Z` is a same-day near-duplicate rerun (~2 min apart, same seed) whose only divergent field (`hippo_mean_residue` NaN->0.0) is a metric-computation artifact -- treated as one experimental event, `070243Z` canonical.

**Recommended for 042**: `measurement_gap`, `non_contributory`, routing `/queue-experiment` (a larger training budget or stronger BC target), **not** `/implement-substrate` -- the source read rules out a wiring bug.

## Thread 3 -- MECH-095/MECH-099 TPJ agency-attribution (7 unique runs)

MECH-095 is `substrate_ceiling`/`pending_retest_after_substrate: true`, GOV-CEIL-1-floored 2026-07-11, `implementation_phase: v5`. Its own 2026-05-02 note explicitly names 6 of this batch's 7 runs by family: "of 7 successor attempts after the EXQ-047k PASS (EXQ-089, 047i, 047j, 098b x2, 121 x2), all weakens or mixed."

**089, 098b (155605Z, the full run), 121 (220939Z, the full run)**: backfill registration only, matching the already-correct 2026-05-02 diagnosis (thin single-agent pre-SD-047 substrate). **098b (155304Z) and 121 (195503Z)**: thin pilots, excluded from evidentiary weight (see dry-run-gate section above).

**510 -- the thread's genuinely fresh finding, resolved by source read rather than left open.** MECH-095's claim note carries a live re-derive-brake count discrepancy: the mechanically-computed count under R1-R3 is **3** (V3-EXQ-741 the valid ceiling hit, plus V3-EXQ-047i/047j newly stamped `substrate_ceiling` in this round's SD-003/MECH-112/dACC-adjacent sibling files), while claims.yaml's own last-touched note (2026-07-11/12, predating today's stamping) still states `n_ceiling_hits=1`. This does not change the routing conclusion (the claim's own language already refuses a 4th single-agent SD-047 letter) but is flagged for governance to correct.

510 was suspected of sharing the V3-EXQ-047l/047m saturation-bug signature (the additive `is_world = WORLD_CAUSED or env_events>0` fold that saturated both 047l's eval probe and 047m's training label -- see `failure_autopsy_V3-EXQ-047l_2026-07-11.json` / `...047m_2026-07-11.json`). **Source-read confirms it does NOT**: `ree-v3/experiments/v3_exq_510_sd047_mech095_live_env_comparator_gap.py:25-55, 220-245` uses a distinct, carefully-partitioned 4-way causal-tagging scheme (`agent_caused` / `env_caused` / `agent_collateral` / `env_correlated`, keyed on `transition_type` + `action==stay` + `multi_source_n_env_events`, with an explicit code comment noting ARM_0 OFF still produces legacy env_drift events specifically so the comparator has env-side samples to learn the not-self baseline). All 4 arms pass C4 (non-degenerate) -- this run's C1/C2/C3 FAILs across all 4 arms are therefore a **valid** additional data point, not a repeat of the measurement-degeneracy class. SD-047's own claims.yaml note is stale (still reads "Validation pending: V3-EXQ-509 -> V3-EXQ-510 ... pending" though this run completed 2026-05-04).

**Recommended for 510**: `substrate_ceiling` (MECH-095 face) / `standard` (SD-047 face), `evidence_direction` mixed(MECH-095)/weakens(SD-047) matching the manifest, `governance-note-only` -- correct SD-047's stale "pending" note and fold 510 into MECH-095's note, reinforcing the already-confirmed ceiling read via V3-EXQ-741. No new substrate build owed.

## Biological-reference triage

All threads have present, previously-established literature (`targeted_review_connectome_mech_089`, `targeted_review_theta_abstraction_scaling`, `targeted_review_connectome_mech_095`, `targeted_review_mech_099`, `targeted_review_reafference_streams` -- the latter shared with SD-005's own grounding, confirming it's a genuinely shared thread, not duplicated independently).

## Re-derive brake state (R1-R3)

MECH-089 = 0 (claim-level narrative brake already in force independent of the formal mechanism). MECH-095 = 3 (see governance-flag above; brake already fired via V3-EXQ-741, `refused_requeue: true`, routed to `multi_agent_ecology_v5:MAE-3`). SD-004/ARC-007/SD-006 = 0.

## Recommended routing summary

- **Thread 1**: no action, cite existing artifacts.
- **Thread 2**: 066/122x2/052 `governance-note-only` (backfill). 042 `/queue-experiment` (training-budget redesign, not a substrate build).
- **Thread 3**: 089/098b(B)/121(B) `governance-note-only` (backfill, explicit re-queue refusal). 098b(A)/121(A) excluded, `governance-note-only`. 510 `governance-note-only`, corrects SD-047's stale note, reinforces MECH-095's ceiling.

## Learning extracted

1. A driver superficially resembling a known saturation-bug family (047l/047m) must be checked against its actual partition logic before being dismissed or accepted -- 510's causal-tagging scheme is meaningfully different and the source read overturned the initial suspicion.
2. A correctly-wired training loop with zero measurable learning (042) is a genuinely distinct diagnosis from a missing-training-loop defect (the sense()-only pattern found elsewhere this round) -- routing differs accordingly (`/queue-experiment` vs `/implement-substrate`).
3. MECH-095's re-derive-brake count has drifted ahead of claims.yaml's stated figure since this round's own earlier files stamped 047i/047j -- a same-day staleness gap worth a governance sweep across today's other artifacts too.
