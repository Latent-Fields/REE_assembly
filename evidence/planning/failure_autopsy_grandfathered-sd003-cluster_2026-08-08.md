# Failure Autopsy (cluster, closure pass): SD-003 origin population (66 nominal / 56 deduped runs)

**Generated:** 2026-08-08T17:37:36Z
**Scope:** cluster (56 deduped runs, 2026-03-17 to 2026-05-05)
**Status:** confirmed (Step 8 interactive gate: user confirmed governance-note-only, preserving recorded evidence_direction, V3-EXQ-525 excepted)

## Governing fact

SD-003 (two-pass counterfactual `E2(a) - E2(a_cf)`) is `status: superseded` in `claims.yaml` (superseded 2026-04-18 to MECH-256/SD-029). The supersession_note states verbatim: *"28 FAILs accumulated across V2+V3 iterations with no PASS... biological precedent gap -- Frith 2000, Shergill 2003, Blakemore 1998 evidence a single-pass comparator, not a two-pass counterfactual... Existing evidence chain (EXQ-030b/115/166a/195/353/431) remains in the historical record; new V3 evidence accrues to SD-029."* Five of those six cited runs (030b, 115, 195, 353, 431) are directly in this batch. **This batch is confirmed to be the population that motivated SD-003's supersession** -- exactly the "28 FAILs" example CLAUDE.md itself cites as the canonical formal-import-vs-biology-divergence case.

## Dry-run gate and deduplication

All 66 nominal run_ids confirmed `dry_run: false` (including the two `_dry`-named runs, 330 and 353, verified NOT actual smokes -- short exploratory configs, same pattern as the earlier V3-EXQ-431 case). **10 exact-timestamp duplicate pairs found** (same `experiment_type` + `timestamp_utc`, recorded twice under prefix-vs-suffix naming conventions) -- collapsing 66 nominal entries to **56 independent runs**.

## Failure-shape sample

Sampled ~15 of 56 across the full date range: consistent shape throughout -- world-model competence (`world_forward_r2` 0.91-0.98) stays strong across every architectural iteration (raw z_world -> gradient world -> SD-008 alpha fix -> SD-010 z_harm separation -> SD-011 dual-stream split -> interventional training -> trajectory-level attribution), while the SD-003-specific two-pass discrimination criterion (`causal_sig`, `attribution_gap`, `calibration_gap`) stays weak, near-zero, marginal, or sign-inverted, run after run. Textbook "negative-control passes, discrimination fails" fingerprint. No subset shows a structurally different failure shape (no wiring bugs, no crashes, no measurement gaps) -- one convergent story across the whole population.

## Biological-reference triage

`evidence/literature/targeted_review_sd_003/` (9 entries) and `targeted_review_sd003_successor_comparator/` (4 entries) both present and load-bearing. Frith 2000 (supports, 0.72) and Shergill 2003 (supports, 0.78) both explicitly frame the biological comparator as **single-pass** (predicted-vs-observed residual), explicitly contrasted against a two-pass counterfactual rollout, and both explicitly map onto the REE successor architecture. This is precisely the biology-divergence-from-formal-import case the skill and CLAUDE.md cite SD-003 as the canonical example of.

## Co-tagged claims -- all already independently resolved

Checked every co-tagged claim (MECH-071, ARC-024, MECH-102, SD-005, SD-007, SD-008, SD-009, SD-010, SD-011, SD-013, ARC-033, MECH-069, MECH-098, MECH-099, MECH-100): all already governance-synthesized, in most cases using this exact batch as cited evidence (e.g. MECH-069 promoted stable 2026-03-19 directly off EXQ-009 in this batch; MECH-100/SD-009 promoted using EXQ-020 in this batch). No co-tagged claim has a genuinely separate open thread this batch newly bears on.

**Exception -- V3-EXQ-525** (2026-05-05T22:04:44Z, minimal 1-seed/5-episode config): this run postdates SD-003's 2026-04-18 supersession. It is the direct one-iteration predecessor of a separate, non-batch run of the same experiment_type at 2026-05-06T06:51:02Z (4 seeds, `hf_r2=0.9191`, all criteria PASS) that is the sole evidence cited for **ARC-033's promotion to stable on 2026-08-07**. Per SD-003's own supersession_note, this run's evidence accrues to SD-029/ARC-033, not SD-003.

## Four-layer diagnosis (written once for the dominant story)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened -> already resolved by supersession | Tested fairly across 56 independent runs and multiple redesigns; superseded 2026-04-18, not merely weakened |
| Biological reference | clear | Frith 2000, Shergill 2003, Blakemore 1998 directly evidence single-pass comparator |
| Prerequisites | present (mostly) | SD-005/SD-007/SD-008/SD-010/SD-011 all independently promoted; ARC-033 later reached stable |
| Implementation completeness | complete (of the wrong mechanism) | Two-pass counterfactual repeatedly, competently implemented; forward-model R2 consistently strong |
| Environment adequacy | adequate | Negative controls and forward-model fits clean throughout |
| Measurement adequacy | adequate | Criteria correctly instrumented; measure exactly what the architecture fails to deliver |
| Integration adequacy | isolated -> partially coupled | Individual substrates work; the two-pass comparison across them is the persistent failure locus |
| Scale/capacity | not the bottleneck | Wider E2 (EXQ-009) worsened, not improved, attribution -- architectural, not capacity-limited |

## Recommended epistemic_category / evidence_direction / routing

**All 56: `epistemic_category: standard`, `evidence_direction: UNCHANGED (as originally recorded in each manifest)`, `routing: governance-note-only`.** Per-claim `evidence_direction_per_claim` values (which diverge meaningfully within some FAIL runs, e.g. SD-003 weakens while a co-tagged claim shows supports on its own criterion) are preserved as-is, not overwritten. Confirms/formalizes the existing 2026-04-18 supersession -- matches the precedent already set by `failure_autopsy_grandfathered-superseded-batch1_2026-08-08.json` (same-day, same "formalization-only closure pass" pattern).

**V3-EXQ-525**: flagged explicitly -- evidence accrues to SD-029/ARC-033 per SD-003's own supersession_note, not adjudicated against SD-003.

## Re-derive brake check

SD-003: 1 confirmed `substrate_ceiling` hit on record (below threshold 2) -- moot, claim is superseded and not subject to further re-queue. MECH-071/ARC-024/MECH-102: 0 hits each. Brake does not fire for any; not applicable given SD-003's dead status.

## Learning extracted

1. This batch is confirmed, not merely presumed, to be the actual population underlying CLAUDE.md's own cited "28 FAILs before supersession" example -- a rare case where a standing-rule citation could be traced back to its exact source runs.
2. The 10 duplicate pairs are a naming-convention artifact (prefix-vs-suffix timestamp), not independent evidence -- confirms the same mechanism found in prior rounds' clusters.
3. V3-EXQ-525 is the one run in this population requiring special handling: it postdates the supersession event it's nominally tagged against, and its evidence belongs to the successor claim.
4. No `/claim-synthesis` granularity-debt routing applies -- the "split" already happened via the MECH-256/SD-029 supersession itself.
