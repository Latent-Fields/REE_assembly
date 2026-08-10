# Failure Autopsy Batch — 2026-08-10 (6 targets / 5 groups)

**Generated:** 2026-08-10T06:27:24Z
**Session:** queue-depth-low-ops-aac785, claim `failure-autopsy: batch-20260810-6targets`
**Status:** confirmed (all 5 groups adjudicated interactively at the Step 8 gate)

Discovered via a full `pending_review.md`/index regen at session start. Excludes the V3-EXQ-906-lineage items (906b, 906c, 909, 910, 911), which were owned by a concurrent active claim (`relaxed-shtern-75392b`, organism-level review) at discovery time — not duplicated here.

## Targets and outcomes

| Group | Target(s) | Claim(s) | Verdict | Routing | Artifact |
|---|---|---|---|---|---|
| 1 | V3-EXQ-228c | ARC-032 | weakens (implementation gap) | `/implement-substrate` — phase-aware ThetaBuffer | `failure_autopsy_V3-EXQ-228c_2026-08-10` |
| 2 | V3-EXQ-903a + V3-EXQ-905a | MECH-075 | inconclusive (903a) / weakens (905a) | `/queue-experiment` diagnostic (903a) + `/lit-pull` (905a) | `failure_autopsy_mech075-second-cluster_2026-08-10` |
| 3 | V3-EXQ-603s | MECH-357 | non_contributory | `/implement-substrate` — pursuit AI or env-mechanics redesign | `failure_autopsy_V3-EXQ-603s_2026-08-10` |
| 4 | V3-EXQ-324d | SD-020 | non_contributory | `/queue-experiment` diagnostic (shared with 903a) | `failure_autopsy_V3-EXQ-324d_2026-08-10` |
| 5 | V3-EXQ-907 + V3-EXQ-908 | (claim-free, SD-016 portfolio) | H1 confirmed, H3 split | `/implement-substrate` — SD-016 amend, combining H1+H3 | `failure_autopsy_V3-EXQ-907_2026-08-10` + `failure_autopsy_V3-EXQ-908_2026-08-10` |

## Cross-cutting observation (not a formal cluster — flagged for governance)

Two independent claims in this batch — **V3-EXQ-903a (MECH-075 ventral)** and **V3-EXQ-324d (SD-020)** — show the identical shape under otherwise clean, well-powered, non-degenerate tests: a signal (valuation-head grounding correlation; harm-surprise correlation) that trains reliably in a minority of seeds and reads near-zero-or-negative in the rest, under an *identical config across seeds*. Both were routed to a diagnostic spike (903a explicitly; 324d by cross-reference) rather than a claim-level verdict, on the reasoning that this looks like training-instability in newly-trained PE/valuation heads rather than two unrelated null results. Worth considering a single shared root-cause diagnostic (log per-seed training trajectories for both heads) rather than two separate investigations.

## Governance note (not a full autopsy — informational)

`V3-EXQ-899` has a near-duplicate manifest sitting in `pending_review.md`: `..._arc030_mech307_g0_readiness_20260808T153148Z` (no `queue_id`, near-identical interpretation text to the confirmed-autopsied `..._20260808T214833Z` which carries `queue_id: V3-EXQ-899` and whose finding is already applied to `claims.yaml`). Same script ran twice on 2026-08-08 with the same result. Recommend governance mark the `153148Z` manifest's stem discussed (scoring-neutral, `claim_ids: []`) as a redundant duplicate rather than running a second full autopsy on it.

## Recording-integrity finding (flagged separately, not part of any claim verdict)

V3-EXQ-603s's manifest shows `substrate_stable_across_run: false` — a substrate-hash mismatch between what was recorded and what was on disk at stamp time on `ree-cloud-4`. Adjudicated at face value per user confirmation (the scientific finding is internally consistent regardless); flagged here for an infra follow-up on whether a concurrent code change landed on that worker mid-run.

## Standing checks run (all clear)

- Dry-run citation check: all 6 run_ids confirmed real (not smokes).
- Re-derive brake (R1-R3 convention): zero prior `substrate_ceiling` reads for ARC-032, MECH-075, SD-020, or MECH-357 — brake does not fire for any target.
- Granularity-debt recurrence: does not fire for ARC-032 (1 weakened target, no structural overlap), MECH-075 (zero weakened targets), SD-020 (3 weakened targets, same substrate-confound shape, not structurally distinct), or MECH-357 (explicitly "not granularity debt regardless of count" per the reader's own check).

See individual target files for full facts, biological-reference triage, four-layer diagnosis, and draft `evidence_quality_note` text for governance.
