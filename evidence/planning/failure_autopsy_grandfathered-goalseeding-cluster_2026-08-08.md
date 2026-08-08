# Failure Autopsy: SD-015/SD-010/SD-012/SD-007/SD-049 goal-seeding cluster (21 nominal / 19 unique, 6 threads)

**Generated:** 2026-08-08T17:37:36Z
**Scope:** cluster (6 threads, 2026-03-20 to 2026-06-01)
**Status:** confirmed (Step 8 interactive gate: user confirmed SD-007 not-a-crash, dry-run reclassifications, V3-EXQ-514b as fresh substrate_ceiling target)

## Cross-cutting mechanical finding

The automated dry-run checker (`check_dry_run_citations.py`) reports 0/19 dry -- **a recording gap, not a clean bill**, for pre-2026-07 manifests lacking the `dry_run` boolean. Manual content inspection found **7 genuine dry/smoke artifacts**: Thread C's 6 `_dry`-named runs (byte-identical `results_per_condition` across repeat invocations minutes apart) and Thread D's one `_dry`-named run. **5 of these 7 are already correctly reclassified `non_contributory`; 2 are NOT** (`v3_exq_326_..._dry_154537Z`, `..._155010Z`, still `does_not_support`) plus Thread D's `327_dry_155627Z` (also still `does_not_support`). **These 3 need reclassification to `non_contributory` for consistency with their already-corrected siblings** -- confirmed at Step 8.

## Thread A -- SD-010/ARC-027 harm-stream baseline (V3-EXQ-056), 2 unique runs (of 4 nominal)

Deduplication: 4 nominal strings collapse to 2 physical runs (naming-convention duplicates). Both real (0622Z, 1553Z) show C3 (z_harm variance across event types) FAIL -- HarmEncoder output collapses near-constant regardless of event type. **Already substantively diagnosed in claims.yaml's SD-010 evidence_quality_note**: "HarmEncoder received saturated or constant harm_obs input; architecture was correct but input was not. EXQ-058b fixed by adding direct MSE supervision." Already resolved downstream. `epistemic_category: competence_implementation_gap`, `governance-note-only`.

## Thread B -- SD-007 "c1fail" runs (V3-EXQ-111, V3-EXQ-118), 2 runs -- CONFIRMED NOT CRASHES

Both scripts carry an explicit interpretation grid: predictor-quality precondition gate (`R2_test >= 0.10`). When the predictor's own held-out R2 falls below this, the script **intentionally aborts before Phase 2** and self-stamps `status: FAIL`, `evidence_direction: not_applicable`, `fail_reason: C1_FAIL_predictor_quality_insufficient`. No traceback, no exception field, empty `failure_signatures: []` -- a clean, self-classified precondition-gate exit. **Confirmed: `epistemic_category: precondition_unmet`, NOT routed to `/diagnose-errors`.** Recording gap noted (the script computes R2/sample-count fields internally but the stored evidence pack carries none of them -- `metrics.json: {"values": {}}`); SD-007's 2026-08-07 governance flag already names this exact precondition as "not retested since ARC-027/SD-010 landed." `governance-note-only`.

## Thread C -- SD-015/MECH-216/SD-012 wanting-gradient nav-fix dry cluster (V3-EXQ-326/326a), 6 runs -- ALL DRY

Confirmed dry by content (see cross-cutting finding). None are autopsy targets in the scientific sense. Two need mechanical reclassification (154537Z, 155010Z -> `non_contributory`, matching the 4 already-corrected siblings). No four-layer diagnosis needed.

## Thread D -- SD-015/MECH-163 goal-conditioned nav (V3-EXQ-327), 2 runs

`327_dry_155627Z` -- dry by content, needs the same reclassification as Thread C. `327` real run (2026-04-14) -- genuine full-budget FAIL, `non_contributory` already correctly set: "Goal conditioning had zero effect: GOAL_CONDITIONED and GOAL_ABLATED produced identical resource_rate/benefit_exposure for all 3 seeds." Implementation/integration gap (mechanism inert), not claim falsification. `governance-note-only`.

## Thread E -- SD-049 phase-2 behavioural validation lineage (MECH-229/230, SD-015, MECH-307), 6 runs -- THE FRESH FINDING

**Coverage audit**: `514k` already covered (via `failure_autopsy_V3-EXQ-626_2026-06-01`, which directly adjudicates its `wanting_liking_dissoc_fraction=0.0`). `514j` covered in narrative/`substrate_queue.json` prose but has no formal `targets[]` entry. `514f` (x2) reclassified `non_contributory` via a bare governance-walk note, never a formal artifact. **`514b` has zero prior coverage anywhere -- genuinely uncovered, and is the ORIGIN POINT of the row1b/GAP-2 lineage.**

**514b** (2026-05-05): well-instrumented 4-arm sweep, fails specifically on `C2b_arm2_probe_acc_neighborhood` (0.483 < 0.6 floor) while `C0/C1/C2a/C2c/C2d/C3a/C3b` all PASS -- encoder/classifier/drive plumbing all fire correctly, only the neighborhood identity-discrimination probe falls short. **This is the first appearance of the exact signature that recurs through 514f/j/k/538a** (low neighborhood-probe accuracy, low consumption-sample counts) -- confirmed as the origin of the row1b/GAP-2 lineage, not an independent bug.

**Cluster pattern (514b->514f->514j->514k->538a)**: encoder/classifier/drive substrate all wire and fire correctly (C0/C1/C2a/C2d/C3 pass throughout), but the neighborhood identity-discrimination probe and/or consumption-sample counts stay below floor. One structural property: insufficient foraging competence to generate enough resource-contact events for the identity probes to be well-powered -- exactly what `538a`'s confirmed `substrate_ceiling` reading concludes.

**328b** (SD-012/MECH-230, 2026-04-13, separate/earlier lineage member): partial signal, C1/C2 pass 2/3 seeds, C3 (ablation control) fails 2/3 -- a threshold-calibration gap (benefit_threshold=0.6 doesn't fully suppress ablated-condition seeding), two prior calibration bugs already fixed in this version.

**Re-derive brake, ALREADY LOUDLY FIRING**: SD-015: 4 hits. SD-049: 4 hits. MECH-229: 3 hits. MECH-230: 3 hits. **All well past threshold=2.**

**Routing (confirmed)**: **514b -> full `substrate_ceiling` autopsy target, `implement-substrate`, action `none`/`amend`** (the existing `substrate_queue.json` SD-049-PHASE-2 entry already tracks this gap -- amend note only), **explicitly refusing any same-claim re-queue**. 514f (x2) -> formalize the existing governance reclassification into this formal artifact. 514j -> add as a formal target citing the same cluster read (amends `failure_autopsy_V3-EXQ-514l`'s narrative coverage into a formal one). 514k -> no new work, already adjudicated via 626. 328b -> `measurement_gap`/threshold-calibration, `governance-note-only`.

## Thread F -- SD-015 resource encoder ablation (V3-EXQ-531), 1 run

C1 FAIL (`resource_prox_r2 < 0.5`), but the script itself carries `MANIFEST_WRITER_EXEMPT = "archival early-era manifest... superseded lineage, not re-run"`. claims.yaml's SD-015 `what_would_answer` states representation-adequacy is SETTLED PASS via EXQ-085l (03-30, prox_r2=0.908) and V3-EXQ-514o (06-15, goal_resource_r 0.93-0.96), both bracketing this 05-06 FAIL. Recording gap (`metrics.json: {}`). Outlier against surrounding bracketing evidence, plausibly explained by a narrower test config (grid_size=12, 50/20 episodes vs the more thoroughly-trained bracketing runs). `epistemic_category: measurement_test_design_defect`/superseded, cite EXQ-085l/514o, `governance-note-only`.

## Biological-reference triage (all threads)

SD-049/MECH-229/MECH-230: dopaminergic incentive-salience "wanting != liking" dissociation (Berridge/Robinson) and object-bound goal-identity representation -- biology basis present and load-bearing (`targeted_review_sd_049_encoder_identity_expansion`, `wanting_liking_sleep_consolidation_synthesis.md`). This is squarely a substrate/foraging-competence ceiling read, biology supports the mechanism, implementation/environment cannot yet sustain enough contact events -- not a formal-definition-import problem.

## Recommended routing summary

- **Thread A/B/C/D**: `governance-note-only` closure. Thread C: 2 dry runs reclassified. Thread D: 1 dry run reclassified.
- **Thread E**: `514b` -> full `substrate_ceiling` autopsy target, `implement-substrate` (amend existing substrate_queue entry), explicit re-queue refusal. `514f`/`514j` -> formalize existing coverage. `514k` -> no action. `328b` -> `governance-note-only`.
- **Thread F**: `governance-note-only`, cite bracketing evidence.

## Learning extracted

1. The automated dry-run checker's blind spot on pre-2026-07 manifests (no `dry_run` boolean field) recurred here exactly as documented in a prior round's ARC-024/033/SD-005 cluster -- content-level verification remains necessary for this era.
2. SD-007's "c1fail" naming convention is a self-documenting precondition gate, not a crash artifact -- confirms the skill's distinction between `/failure-autopsy` and `/diagnose-errors` scope holds even for confusingly-named runs.
3. V3-EXQ-514b is a genuine origin-point discovery: the SD-049/MECH-229/230 lineage's re-derive brake has fired repeatedly downstream, but its actual first occurrence had never been formally autopsied.
4. Two same-day inconsistent governance reclassifications found (326_dry pair vs its siblings) -- a recurring pattern across multiple rounds of this backlog sweep.
