# Failure Autopsy: SD-029/MECH-256 (event-conditional comparator) + ARC-030 (go/no-go symmetry), 22 nominal / ~19 deduped

**Generated:** 2026-08-08T17:37:36Z
**Scope:** cluster (2 threads, 2026-03-23 to 2026-05-08)
**Status:** confirmed (Step 8 interactive gate: user confirmed ARC-030 closure citing existing chip chain, SD-029/MECH-256 routed to /governance reconciliation with V3-EXQ-878)

## Dry-run gate and deduplication

`v3_exq_331_..._dry_20260410T160253Z_v3` confirmed dry by content (script has a real `--dry-run` flag; self-declared "Non-contributory pending full run"). `138a` (x2 same day): NOT crash-recovery -- run 1 (04:36:47Z) used warmup=2/eval=1 (a degenerate manual sanity invocation, not the canonical config), run 2 (09:04:27Z, warmup=400/eval=50) is the real evidence point. **claims.yaml's own note is factually wrong here** (states "criteria_met=2/5" for run 1; run 1's own summary.md reports 1/5) -- worth a correction. `537` (x3, all within ~20min): genuine same-config statistical repeats (not byte-identical, real stochastic variation), only 1 of 3 was ever marked `superseded` by a prior governance pass -- the other 2 should carry the same disposition.

## Thread A -- ARC-030 (Go/No-Go symmetry), 4 real evidence points (of 6 nominal)

**Trajectory**: 086 (warmup=150, too short, author's own retrospective note) -> 138a-canonical (corrected training depth, still fails) -> 180a (parallel sub-question: representation present, C1 PASS resource-proximity encoding; readout fails and is actively counterproductive, C3 ratio 0.37<1.0) -> 331-full (already governance-annotated: goal seeding SD-015/MECH-112 not functional, "does not weaken ARC-030"). **One structural property, not 4 independent bugs**: every run in this batch predates the goal-seeding substrate fix (GAP-1/GAP-2/GAP-7, landed 2026-05-11->06-15) by 1.5-3 months.

**claims.yaml's own text already states the retest chain**: ARC-030 is "UNTESTED on the fixed substrate, not merely awaiting a fresh interpretation of old evidence." **Active retest chain already chipped by governance, not yet run**: `chip-20260807-mech307-fromdims-wiring` (DONE, landed) -> `chip-20260808-arc030-mech307-readiness` (pending). This is exactly a substrate-readiness gate governance is already running.

**Re-derive brake**: 2 confirmed `substrate_ceiling` hits already on record (both from `failure_autopsy_grandfathered-zworld-forward-cluster_2026-08-08.json`, V3-EXQ-247) -- **already at threshold**. Adding this batch's 4 runs would push well past. Brake implication (already what governance independently converged on): `implement-substrate`/refuse same-claim re-queue -- but do NOT spawn a duplicate retest chip; cite the existing chip chain.

**Recommended disposition (all 4 real runs)**: `non_contributory` (revise 086/138a-canonical from `weakens`), `substrate_ceiling`, `pending_retest_after_substrate: true` (already so). `routing: governance-note-only` -- cite the existing chip chain, explicitly refuse a duplicate.

## Thread B -- SD-029/MECH-256 (event-conditional comparator), 11 real runs (of 16 nominal) -- two-phase story

**Phase 1 (433->433f, monostrategy blocks event-count sufficiency, 04-19->05-07)**: consistent finding across 433/433a/433b/433d/433e/433f -- behavioral monostrategy (agent locks into pure-exploit or pure-avoid) prevents balanced event counts for the comparator's C0/C4 gates. 433e/433f's reef-substrate attempt (SD-054) partially effective but insufficient at 8x8 scale.

**Phase 2 (523/535/535a->537d, event balance achieved via reef, then a NEW bottleneck, 05-05->05-08)**: 523/535/535a inadvertently test the **superseded SD-003 two-pass counterfactual gap formula**, not SD-029's single-pass spec -- 535a's own note explicitly diagnoses this (a small-scale recurrence of the exact defect class SD-003 was created to retire; 535's identical tags are NOT self-corrected the way 535a's are). 537 (x3, correctly single-pass per spec) finally clears event-sufficiency (C4 PASS) but forward-model fit (C1) plateaus at r2~0.65, well below threshold. 537b (curriculum decoupling), 537c (capacity lift 128->256), 537d (no interventional training) each rule out one candidate cause -- **all three fail to move the r2~0.65 ceiling.** Batch ends 2026-05-08 on a genuinely open puzzle.

**Critical reconciliation finding**: MECH-256's 2026-08-06 `digestion_note` reports that **V3-EXQ-878** (2026-08-03, already confirmed autopsy, tests MECH-332's 2x2 factorial) shows the **same efference-copy comparator mechanism (Pathway 1 = MECH-256/SD-029) passing cleanly** (`d2_pass=true`, 3/3 seeds) via a differently-operationalized discrimination test once event-balance was achieved on a later substrate (SD-022 body-damage arena + EXQ-479-calibrated curriculum). **This does not directly resolve the r2~0.65 forward-fit puzzle** (878 uses a discrimination-floor test, not literally the same forward_r2 gate) -- it sidesteps rather than solves it. The digestion_note itself flags that this reconciliation into SD-029/MECH-256's `v3_pending`/`evidence_quality_note` has **not yet been applied** by governance.

## Biological-reference triage

ARC-030: `targeted_review_arc_030/` (Cox 2015) + Bariselli 2018 (competitive D1/D2 model), Hikida 2012 -- solid, specific biology grounding (D1/D2 competitive evaluation of the SAME hippocampal trajectory proposals). SD-029/MECH-256: `targeted_review_sd003_successor_comparator/` -- 4-paper convergence (Frith 2000, Shergill 2003, Haggard 2017, Blakemore 1998), explicitly the biology-corrected successor to SD-003.

## Four-layer diagnosis

| Layer | ARC-030 | SD-029/MECH-256 |
|---|---|---|
| Claim alignment | unclear->weakened-but-wrong-substrate | unclear->strengthened elsewhere (878) |
| Biological reference | clear (Bariselli 2018) | clear (Frith/Shergill/Haggard/Blakemore, explicit SD-003 corrected successor) |
| Prerequisites | missing at time of these runs (goal-seeding pipeline non-functional) | missing->immature in two ways (monostrategy, then unexplained forward-fit ceiling) |
| Implementation | partial (Go channel structurally present, unfed) | complete for final design (537+); 523/535/535a tested the WRONG design |
| Environment | adequate | reef enrichment (SD-054) partially effective, fixed event-balance not forward-fit |
| Measurement | adequate, exposes the gap well (180a) | biggest finding: C0/C4 and C1 are separate gates, conflated across letters until 537+ |
| Integration | isolated | isolated pieces work (C3 falsification consistently passes -- real signal, not noise) |
| Scale/capacity | unknown, confounded | directly tested and ruled out (537c, no improvement) |

## Recommended routing (confirmed at Step 8)

**ARC-030**: `governance-note-only`, cite the existing chip chain (`chip-20260807-mech307-fromdims-wiring` DONE, `chip-20260808-arc030-mech307-readiness` pending) -- explicit note to NOT spawn a duplicate retest chip.

**SD-029/MECH-256**: **do NOT recommend a fresh SD-029-specific experiment** (re-derive brake territory -- this autopsy would be the first formal stamping of ~11 targets, immediately exceeding threshold on first write). **Route to `/governance`** to (a) apply V3-EXQ-878's already-confirmed recommendation (lift `v3_pending`, per the claim's own stale-note flag), (b) update SD-029/MECH-256's `evidence_quality_note` to reflect this 04-19->05-08 lineage as superseded-in-substance by 878 even though 878 tests a different queue_id, (c) formally stamp the ~11 real Thread-B runs as `substrate_ceiling`/`non_contributory` for the historical record. This is a reconciliation task, not a new experiment.

**Also flagged for governance**: (1) correct 535's tags to `non_contributory` (matching 535a's self-correction for the same two-pass-formula defect); (2) align all 3 same-day 537 runs to the same disposition (currently only 1 of 3 marked `superseded`); (3) correct claims.yaml's factually-wrong 138a "criteria_met=2/5" note (run 1's own summary.md says 1/5).

## Re-derive brake state (R1-R3)

ARC-030: 2 hits, already at threshold (from a different file). SD-029/MECH-256: 0 hits currently formally stamped (despite extensive claims.yaml prose already reading `substrate_ceiling`) -- **this autopsy would be the first formal stamping**, immediately exceeding threshold. Per the brake's own spirit, the correct response to "first stamping already exceeds threshold" is not a queue refusal for a re-test that was never proposed, but exactly the reconciliation routing above -- do not let the mechanical brake language obscure that no same-claim re-queue is being recommended here in the first place.

## Learning extracted

1. ARC-030's retest is already in motion via governance's own chip chain -- this autopsy's job is confirming, not proposing.
2. SD-029/MECH-256's real "unresolved puzzle" (forward-fit ceiling at r2~0.65) was sidestepped, not solved, by a later differently-designed test (878) -- both facts need to be stated plainly, not conflated into "already resolved."
3. A small-scale recurrence of SD-003's exact two-pass-counterfactual mistake was caught locally (535a) but not fully propagated (535's tags left uncorrected) -- a reminder that even a successfully-caught defect needs its correction applied consistently across sibling runs.
4. Two independent "same-day duplicate run inconsistently treated" findings in this one batch (138a's wrong claims.yaml count, 537's 1-of-3 supersession) mirror a pattern seen across multiple batches this round.
