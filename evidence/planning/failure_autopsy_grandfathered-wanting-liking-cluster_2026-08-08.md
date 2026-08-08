# Failure Autopsy (closure pass): MECH-071/MECH-112/MECH-117 wanting/liking cluster (37 nominal / 26 real)

**Generated:** 2026-08-08T17:37:36Z
**Scope:** cluster (26 real deduplicated events, 2026-03-18 to 2026-05-08)
**Status:** confirmed (Step 8 interactive gate: user confirmed closure, flagged gaps, respected brake constraints)

## Deduplication and dry-run gate

37 nominal run_ids -> **30 deduplicated events** (6 duplicate groups: 2 prefix/suffix naming pairs, 4 byte-identical runner re-emission groups) -> **26 real events** after excluding 4 dry/smoke runs (`v3_exq_328_..._dry`, `v3_exq_328a_..._dry` x2 dup, `v3_exq_238_20260404T185519Z` self-declared smoke_test).

## Claims.yaml state (6 most-tagged claims)

MECH-071 (provisional), MECH-112 (**deprecated 2026-04-13, split into MECH-229 + MECH-230**), MECH-117 (stable), ARC-030 (candidate, `substrate_ceiling`), SD-012 (provisional, `standard`), SD-015 (candidate, `substrate_ceiling`). All six claims' operative evidence already postdates this batch.

**Critical finding**: MECH-112 was atomically split 2026-04-13 into MECH-229 (behavioral wanting/liking dissociation, now `standard`/confirmed_established) and MECH-230 (z_goal latent structure, now `provisional`/`standard`, ceiling lifted 2026-06-11). Two post-split batch runs (EXQ-527 x2, EXQ-536) still carry the stale MECH-112 tag -- noted, not corrected (both already superseded-in-practice by MECH-229/230's much richer evidence).

## Lineage read: genuinely mixed, stage-dependent

**Early/middle stage (074d->085g->SD-015 series->354, progressive dependency discovery, SD-016/017-pattern):** test-design confound (074d/e) -> z_goal spatial-misalignment discovery (085g) -> SD-015 encoder built+validated (085h-l, outside batch) -> measurement-infrastructure bug (322/322a) -> wiring bug (354, outside batch) -> first PASS via design change (074f/234, outside batch) -> claim split (04-13) -> MECH-229 promotes to standard.

**Middle sub-cluster (183/185/186/225, same-wall tuning, NOT progressive):** four different 1-step selector mechanisms each independently rediscover that 1-step greedy underperforms random on this grid. **Correctly closed, not left circling**: EXQ-182a (oracle-ceiling test, outside batch) confirmed the mechanism *can* work given perfect goal signal, pinning the bottleneck precisely (SD-004 multi-step planning, never built in this era) -- the re-derive brake worked as intended before it existed formally. Worth naming as a precedent.

**Net read**: the MECH-112 lineage is a success story with one closed dead-end sub-cluster inside it, not a stalled ceiling -- consistent with 0 confirmed `substrate_ceiling` hits for MECH-112 anywhere in the corpus.

## Biological-reference triage

Well covered: `targeted_review_connectome_mech_071`, `_mech_112` (Berridge 1996/2016, Barch 2010, Gobbo 2022, Tremblay 1999, Rusu 2019), `_mech_117` (Berridge 1998). REE's trajectory-scoring metrics (`l2_redirect` for liking, `l1_fraction` for wanting) are a genuine behavioral operationalization of the Berridge/Robinson dissociation, not a formal-definition import.

## Four-layer diagnosis (dominant MECH-112 lineage)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | strengthened (MECH-229) / weakened-resolved-elsewhere (MECH-230) | Split correctly separated two bundled empirical questions |
| Biological reference | clear | Berridge/Robinson dissociation, well lit-pulled |
| Prerequisites | missing->resolved mid-lineage | SD-015 encoder wired correctly only by 04-12; SD-004 multi-step planning never implemented (load-bearing absent dependency for the 183/185/186/225 sub-cluster) |
| Implementation | stub (1-step greedy stand-in for planning) -> complete for narrow spatial-greedy workaround only | |
| Environment | adequate but mechanism-mismatched | Grid rewards exploration breadth a 1-step greedy policy cannot provide |
| Measurement | under-instrumented in 3 members | 322x2 (cosine probe never fired), 527 (empty metrics.json, pre-Recording-Standard), 233 (config default left unset) |
| Integration | isolated -> unstable-coupled -> stable (narrow scope) | |
| Scale/capacity | adequate for representation, insufficient for planning | Confirmed by oracle-ceiling EXQ-182a |

## Recommended per-run disposition (grouped)

- **033/039 (ARC-026 leg)**: `superseded` -- resolved by EXQ-232 PASS (2026-04-05). `governance-note-only`.
- **041**: `non_contributory` unchanged -- already excluded in both directions by the 2026-07-25 rescore. `governance-note-only`.
- **074d/074e (x2)/074f (dedup)**: `non_contributory` unchanged, already narrated (measurement-design confound -> later serotonergic-substrate gap per MECH-117 note). `governance-note-only`.
- **079 (x3)**: `non_contributory` -- superseded in practice by higher-budget sibling; the 350ep/60ep member (closest to PASS) flagged as **never governance-reviewed**, recommend `/governance` formalize (narrows to "SD-008 alpha-sharpness is not the primary lever", not a threat to MECH-071 core).
- **085**: `non_contributory` unchanged, covered by the 2026-06-02 disposition memo.
- **112**: `weakens` -> recommend `non_contributory` with caveat, flagged **never governance-reviewed** -- design not comparable to 026/029's setup, worth an explicit claims.yaml note rather than silent omission.
- **183/185/186/225**: unchanged (`mixed`/`non_contributory`), `substrate_ceiling` (planning-horizon, SD-004 absent) -- superseded-in-practice.
- **189**: `mixed` unchanged, `standard` -- EXQ-189's env params later confirmed valid.
- **233**: `non_contributory` unchanged, `measurement_test_design_defect` (config error).
- **235 (x2 unique)**: `non_contributory` unchanged, `substrate_ceiling`.
- **238 (real run)**: `mixed` unchanged, `substrate_ceiling`/measurement.
- **322 (x2)**: `non_contributory` unchanged, `measurement_gap` (`n_cosine_samples=0` harness bug -- the manifest's own note requested `/diagnose-errors`, which appears never to have run; flagged as an open loose end, though moot given SD-015's later resolution).
- **322a**: `does_not_support` unchanged, `measurement_gap` likely -- **no `evidence_direction_note` despite a non-standard direction value; flagged for governance**.
- **328 (real, non-dry)**: `non_contributory` unchanged, substrate (SD-012 drive-substrate immaturity at the time).
- **527 (x2 dedup)**: **the cleanest "never touched" specimen in the batch** -- stale MECH-112 tag (claim deprecated), `metrics.json` genuinely empty, never once referenced in claims.yaml. Recommend `non_contributory` (recording-debt, pre-dates the Experimental Recording Standard) and note the claim tag should read MECH-229/230 if ever re-surfaced.
- **536**: `non_contributory` unchanged -- already correctly self-diagnosed (`update_residue()` never called, BG commit gate dormant); superseded by the next-day 536a/536b diagnostics.

## Re-derive brake state (R1-R3)

MECH-071: 0 hits. MECH-112: 0 hits (consistent with "resolved via split," not "stalled ceiling"). MECH-117: 0 hits. **ARC-030: 2 hits, already AT threshold** (from `failure_autopsy_grandfathered-zworld-forward-cluster_2026-08-08.json`, V3-EXQ-247). **SD-012: 2 hits, already AT threshold** (same file/runs, co-tagged). **SD-015: 4 hits, well past threshold** (V3-EXQ-514l, 538a, 693, 693a, all post-batch).

**This autopsy does NOT stamp new `substrate_ceiling` for ARC-030, SD-012, or SD-015** without the mandatory refusal language -- ARC-030/SD-012 are already at threshold (any further stamp would be the 3rd hit) and SD-015 is 4x past. All routing for these claims is `governance-note-only`/superseded-in-practice, never a fresh same-claim re-queue.

## Recommended routing summary

**All 26 real events -> `governance-note-only`.** Two items flagged for `/governance` (never chipped, per standing rule): (1) EXQ-079 (350/60 config) and EXQ-112's un-reviewed status -- formalize a claims.yaml note narrowing what these rule out; (2) EXQ-527's stale MECH-112 tag and empty-metrics recording gap.

## Learning extracted

1. The MECH-112 lineage's 183/185/186/225 sub-cluster is a documented instance of the re-derive brake's *spirit* working before the brake existed formally (a single oracle-ceiling test pinned the bottleneck and stopped further lettered iteration).
2. Two runs (EXQ-079 350/60, EXQ-112) directly bear on MECH-071's core calibration mechanism but were never governance-reviewed -- a real, if minor, gap.
3. EXQ-527 is the batch's clearest "never touched" specimen: stale claim tag, empty metrics, zero governance mention.
4. ARC-030/SD-012/SD-015 brake states must be respected in this batch's routing -- confirmed at or past threshold from other autopsies, not from this batch's own runs.
