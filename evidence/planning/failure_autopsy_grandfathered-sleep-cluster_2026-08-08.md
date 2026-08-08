# Failure Autopsy (cluster, closure pass): SD-016/SD-017 origin lineage (v3_exq_418/418a-l + 436a, 12 runs)

**Generated:** 2026-08-08T17:10:36Z
**Scope:** cluster (12 runs, 2026-04-16 to 2026-05-10)
**Status:** confirmed (Step 8 interactive gate: user confirmed governance-note-only + one manifest correction)

## Context

Part of working down the 547-run grandfathered legacy-FAIL backlog. All 12 runs confirmed `dry_run: false`, `experiment_purpose: evidence`. This is one lettered lineage (v3_exq_418, 418a through 418l) plus a related sibling root (436a) -- a genuine iterative campaign against SD-016/SD-017, not a random grab-bag.

## Facts and supersession chain

| # | run_id (short) | date | claim_ids | manifest evidence_direction |
|---|---|---|---|---|
| 1 | 418 | 04-16 | SD-017 | does_not_support (STALE -- see correction below) |
| 2 | 418a-r1 | 04-19 | SD-017 | non_contributory |
| 3 | 418a-r2 | 04-20 | SD-017 | non_contributory |
| 4 | 418a-r3 (queue V3-EXQ-418c) | 04-24 | SD-017 | non_contributory |
| 5 | 418d | 04-25 | SD-016, SD-017 | does_not_support (per-claim: SD-016 weakens, SD-017 non_contributory) |
| 6 | 418e-r1 | 04-27 01:59Z | SD-016 | does_not_support |
| 7 | 418e-r2 | 04-27 05:44Z | SD-016 | does_not_support (near-exact duplicate of r1) |
| 8 | 418g | 04-28 | SD-016 | non_contributory |
| 9 | 418i | 05-04 | SD-016 | does_not_support |
| 10 | 418k | 05-05 | SD-016 | does_not_support |
| 11 | 418l | 05-09 | SD-017 | non_contributory |
| 12 | 436a | 05-09/10 | SD-017, ARC-045, MECH-166 | non_contributory (all 3) |

Supersession chain (from manifest `supersedes` fields): `418 <- 418a(x3) <- 418d <- 418e(x2) <- 418g` and `418e <- 418i` (parallel branch); `418j <- 418k` (418j not in this batch); `418a <- 418l` (separate branch resuming SD-017); `436 <- 436a` (436 is a sibling root, not part of "418").

**None of these 12 is the operative evidence in claims.yaml today.** SD-016's `live_status.evidence.from` cites `v3_exq_534_sd016_cue_terrain_training_20260506T094249Z_v3` (PASS, 05-06). SD-017's cites the `436b -> 436c -> 436d -> 436d-methodology-check` chain (2026-08-02 through 08-07), all already confirmed `/failure-autopsy` artifacts. The `418` root continued past this batch through `418m` (06-05, already autopsied) and on to `477`/`534`.

## Claim-layer status

**SD-016** -- `status: implemented`, `epistemic_category: substrate_ceiling`. `what_would_answer` explicitly cites 418d/e/i (Path 1 exhausted), 418j/k (env enrichment doesn't help), 418m (Path 3 also fails identically) as the evidentiary basis, and states the open question has moved upstream to the z_world encoder itself.

**SD-017** -- `status: stable`, `pending_retest_after_substrate: true`. Promoted provisional->stable 2026-04-24 on literature alone (5 supporting/0 opposing/1 mixed, conf 0.903), explicitly noting "no contributing genuine experimental evidence yet -- all SD-017 ablation runs to date are non_contributory." Real experimental support only arrived later via V3-EXQ-691 (06-20) and the 436-chain successors.

**ARC-045/MECH-166** (co-tagged on 436a) -- both `pending_retest_after_substrate: true`, currently `non_contributory/measurement_test_design_defect` per the 436d-methodology-check autopsy (2026-08-07).

## Biological-reference triage

Both claims have existing targeted literature reviews -- no `/lit-pull` commission needed. SD-016: `targeted_review_sd_016/` (Bechara 1999 anticipatory vmPFC SCR, Dunn 2005, Lichtenberg 2017 BLA-OFC cue-expectation). SD-017: `targeted_review_sd_017/` (Aleman-Zapata 2022 ripple necessity, Girardeau 2009, Wikenheiser 2015, Ego-Stengel & Wilson 2010; grounded in Diekelmann & Born 2010 SWS/REM consolidation).

Three progressively-discovered biological dependencies, each a genuine "translation incomplete, not claim false" finding:
1. **Phase 1 (418, 418a x3):** wiring gap -- `cue_action_proj` consumer collapsed (std ~2.7e-8), so downstream E2/E3 never received a differentiable signal. Implementation debt, not biology.
2. **Phase 2 (418d/e/g/i/k):** encoder-level gap -- z_world carries no cue-selective structure (attention pinned at uniform-distribution ceiling ln(16)=2.7726 across every arm, every architecture tried). Real biological prerequisite: a differentiated exteroceptive representation to select over, which vmPFC-cue-selectivity presupposes.
3. **Phase 3 (418l, 436a):** behavioural-diversity gap -- "sleep cannot diversify what was never diverse." Motivated and was later confirmed resolved by the ARC-065/MECH-313/314 substrate (registered same day, 05-10; confirmed fixed in the 436b autopsy, 08-02).

## Four-layer diagnosis (by phase)

| Layer | Phase 1 (418, 418a×3) | Phase 2 (418d/e/g/i/k) | Phase 3 (418l, 436a) |
|---|---|---|---|
| Claim alignment | unclear (wrong instrument) | weakened->unclear (real negative result, not a claim-level falsification) | unclear (precondition unmet) |
| Biological reference | clear but untested | clear; genuine encoder-selectivity gap | clear; behavioural-diversity prerequisite real |
| Prerequisites | missing (wiring) | present (wiring fixed), deeper dependency missing | missing (ARC-065 cluster, registered same day) |
| Implementation | stub/partial | partial (3 remedies tried, all consume same near-constant z_world) | complete for what's tested; upstream substrate absent |
| Environment | unknown (masked) | ruled out as bottleneck (418k: enrichment ladder, no change) | adequate |
| Measurement | adequate (correctly reports null) | adequate (well-designed entropy + divergence instrumentation) | adequate |
| Integration | isolated | partially coupled | isolated |
| Scale/capacity | unknown | likely insufficient at encoder level | insufficient (diversity floor not yet built) |

**Structural verdict: one story, three acts**, each a real, informative negative result that correctly motivated the next phase -- not N independent bugs, and not duplicate/noise probing (with the sole exception of 418e-r1/r2, a genuine same-day near-duplicate, flagged not double-counted).

## Recommended epistemic_category / evidence_direction / routing (per run)

| Run | epistemic_category | evidence_direction | routing |
|---|---|---|---|
| 418 | competence_implementation_gap | non_contributory (correction -- see below) | governance-note-only |
| 418a-r1/r2/r3 | competence_implementation_gap | non_contributory (already correct) | governance-note-only |
| 418d | substrate_ceiling (component) | SD-016: weakens (already correct, per-claim); SD-017: non_contributory | governance-note-only |
| 418e-r1 | substrate_ceiling (component) | does_not_support (already correct) | governance-note-only |
| 418e-r2 | substrate_ceiling (component) | does_not_support -- flag as near-duplicate of r1, do not double-count | governance-note-only |
| 418g | precondition_unmet | non_contributory (already correct) | governance-note-only |
| 418i | substrate_ceiling (component) | does_not_support (already correct) | governance-note-only |
| 418k | substrate_ceiling (component) | does_not_support (already correct) | governance-note-only |
| 418l | precondition_unmet | non_contributory (already correct) | governance-note-only |
| 436a | precondition_unmet | non_contributory (already correct, all 3 claims) | governance-note-only |

**All 12 -> `governance-note-only`.** Every open question this batch surfaced has already been carried forward by later, more sophisticated, already-autopsied work (encoder ceiling -> 418m/477/534 + the 2026-07-18 z_world near-static characterisation + SD-070; behavioural-diversity gap -> resolved by ARC-065/MECH-313, confirmed in the 436b autopsy). A fresh `/queue-experiment` off any of these 12 would re-derive work already 3-4 generations ahead.

**Manifest correction recommended:** V3-EXQ-418 (04-16)'s manifest still carries `evidence_direction: does_not_support`, inconsistent with claims.yaml's treatment as `non_contributory` since 2026-04-19. Recommend governance correct the manifest field for consistency.

## Recommended evidence_quality_note addendum

> Formal `/failure-autopsy` backfilled 2026-08-08 for the full 12-run 2026-04-16->05-10 v3_exq_418/v3_exq_436 origin lineage. Confirms the three-phase structural read already present in this claim's prose (wiring gap -> encoder-selectivity ceiling -> behavioural-diversity precondition) and that none of these 12 runs is current operative evidence -- both claims' live_status already cites later runs (SD-016: v3_exq_534; SD-017: the 436b-436d-methodology-check chain). No new routing generated; historical record only.

## Re-derive brake check

SD-016: 0 confirmed `substrate_ceiling` autopsy targets currently (the claims.yaml-level `substrate_ceiling` category was set by governance narrative, not yet by a confirmed autopsy target). SD-017: 1 confirmed hit (`failure_autopsy_V3-EXQ-538a_2026-07-10`). Threshold=2; neither at/above. **Brake does not fire.** If this batch's recommendations are applied, SD-016 would newly acquire several component `substrate_ceiling` hits (418d, 418e×2, 418i, 418k) -- worth flagging that this could bring SD-016 to/above threshold for the *next* live re-test candidate, though it doesn't fire retroactively here (all 12 are historical/superseded).

## Granularity-debt recurrence

Does not fire -- per the skill's own rule, no target in this batch reads `weakened` at the claim-broad level (418d's SD-016 `weakens` is scoped to one specific mechanism, the v2 writepath design, and is itself superseded). Consistent with SD-016 staying `implemented` (not split) and SD-017 staying `stable` (not split) throughout the much longer downstream chain.

## Learning extracted

1. A "reviewed but never autopsied" backlog run can already be functionally resolved by the time it's picked up -- all 12 were extensively governance-annotated contemporaneously and correctly carried forward through two more generations each, without ever having a formal artifact for the origin runs. The gap is purely artifact-production, not diagnosis.
2. Lettered-lineage batches should be checked for "has the lineage already run past the batch" (via claims.yaml `live_status.evidence.from`) before assuming any routing work is owed.
3. A same-day, same-params, bit-identical rerun (418e×2) is a distinct pattern from a lettered iteration -- worth naming explicitly so a future reader doesn't double-count it.
