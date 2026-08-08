# Failure Autopsy: Round-5 batch0+1 mixed findings, 39 targets

**Generated:** 2026-08-08T19:37:15Z
**Scope:** cluster (round-5 grandfathered-backlog sweep, batches 0+1 non-legacy findings)
**Status:** confirmed (Step 8: MECH-091 sync gap and MECH-104 stale tag both confirmed for correction; MECH-047, ARC-066/MECH-320 held pending confirmation before queuing)

## MECH-116/ARC-032 (076d/076e/076f) — probe-gated, not buildable-on-demand

`076d` (1/4 criteria, underpowered), `076e` (0/3, `E1Config.goal_dim` never set — E1 goal-agnostic in both arms), `076f` (bug fixed, result unchanged — 0.3806 vs 0.3793, 0.3% diff). User-adjudicated 2026-04-04: 076f is `non_contributory` because the test measures z_goal_norm persistence directly, but MECH-116's actual claim is about E1 prediction error on goal-directed trajectory segments — a different, unmeasured quantity. All three are distinct sibling timestamps from what round 4 already covered under this same run-id family. Prerequisite (SD-012 z_goal seeding reliability) is `complex (probe-gated)`, not `complicated (buildable)` — do not push into the queue blind.

## MECH-091 (133 pair) — manifest/governance sync gap

Both runs test the same absent-mechanism precondition (SD-006 phase-2 async multi-rate clock unbuilt — "no oscillatory clock phase to reset"). The 2026-03-29 run correctly shows `non_contributory`. **The 2026-04-21 rerun still shows `weakens` with no note**, despite claims.yaml documenting a 2026-04-22 governance reclassification to `non_contributory` for exactly this run. Step 8 confirmed: flag for correction.

## Held-for-confirmation cases (3)

- **MECH-047 (EXQ-068)**: zero `evidence_quality_note` in claims.yaml despite `status: provisional` — unusual. The manifest's own note specifies an exact fix (pre-convergence checkpoints or forced variance injection). Step 8 confirmed: flag both the missing note and whether the fix was ever queued, before recommending `/queue-experiment`.
- **MECH-104 (EXQ-126)**: a 10-total-step thin pilot where the surprise gate never fired in either arm, still tagged `weakens` against a now-`active`, strongly-supported claim (EXQ-197 6/6, EXQ-204 4/4). Step 8 confirmed: correct to `non_contributory`.
- **ARC-066/MECH-320 (EXQ-549)**: manifest already self-corrected to `non_contributory` with an exemplary note specifying the next design (forced `tonic_vigor_floor>0`). Step 8 confirmed: hold pending confirmation that follow-up wasn't already queued.

## Two active re-derive brakes reaffirmed (Q-021, ARC-046/ISEF-005)

`v3_exq_072b_q021_behavioral_flatness` (non-degeneracy precondition failure, "read 0 on every arm, tested nothing") and `v3_exq_591_isef005_curriculum_vs_flat_20260527T183919Z` (substrate-uniform FAIL, InfantCurriculumScheduler stuck in Phase 0) both belong to claims already past the re-derive-brake threshold and already escalated (Q-021 via `V3-EXQ-866a`'s scaffolded curriculum; ARC-046 via its 591b-591e family). Formalized as-is; explicit re-queue refusal.

## Formalization-only backfill (remaining targets)

ARC-018 (172/196 — clean negative + arithmetic-artifact, mechanism identified 2026-07-22), MECH-165 (2 of 3 same-signature runs need reclassifying to match their already-reclassified sibling — an internal-consistency gap), MECH-057b/MECH-090 tagging-correction pair (048/049 — real MECH-090 implementation bugs mistakenly still directory-named `mech057b`; do not credit MECH-057b, which has zero genuine evidence), ARC-029 (125 pair — substrate-drift confound, since resolved via EXQ-063a), ARC-036 (176 pair — probe-implementation bug corrected same-day as this sweep, 2026-08-08 GOV-REUSE-1 reanalysis leaves claim status open), MECH-186 (251 pair — already correctly `non_contributory`, V4-scope), MECH-092 (136 — precondition since resolved via V3-EXQ-761), 181b (MECH-150/ARC-041 — pre-experimental prerequisite finding, manifest mis-tagged SD-016 in its directory name), 235 (MECH-112/ARC-030 — already `non_contributory`, measurement bug), INV-010 (430 — already `non_contributory`, seed-variance anomaly), MECH-044 (688a — stale `live_status.evidence.from` pointer names the predecessor autopsy instead of this successor, low-priority hygiene flag), 074f pair (001929Z/002135Z — genuinely new, pre-final-fix iteration superseded by a same-day PASS 12 minutes later; also flags an unflagged seed=42 non-reproducibility between two byte-identical-code runs 3.5 minutes apart).

## Biological-reference triage

All claims touched have present literature grounding except MECH-047 (no biological anchor recorded at all in claims.yaml — a genuine `/lit-pull` gap, secondary to the missing-evidence-note gap already flagged).

## Re-derive brake state

Q-021 and ARC-046 both **fired** (already escalated, reaffirmed here, explicit re-queue refusal). No other target in this file recommends `substrate_ceiling` freshly.

## Recommended routing summary

All 39 targets: `governance-note-only`, except the three held-for-confirmation cases which stay `governance-note-only` with an explicit "do not queue blind" instruction pending governance's own check.

## Learning extracted

1. A manifest can silently drift out of sync with a governance reclassification recorded only in claims.yaml prose (MECH-091) — worth a periodic cross-check sweep independent of this backlog effort.
2. A claim can be `active` with strong support while still carrying a stale, misleadingly-tagged early pilot run (MECH-104) — the PASS chain accumulating doesn't automatically clean up the FAIL tail.
3. Two cases (MECH-047, ARC-066/MECH-320) show manifests that already fully diagnose their own fix and name the next step — but nobody had checked whether that next step was actually queued. Worth a standing convention: a manifest naming its own fix should get a `queued: true/false` marker.
