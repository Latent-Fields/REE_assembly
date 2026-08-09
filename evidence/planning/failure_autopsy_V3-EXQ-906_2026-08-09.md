# Failure Autopsy — V3-EXQ-906 (Full-Stack Observational Fishtank Showcase, `vacuous_pass` flag)

**Generated:** 2026-08-09T05:43:28Z
**Scope:** single
**Status:** confirmed (interactive gate run 2026-08-09 — low controversy; this is a tooling-bug finding with zero claim impact)

## Executive summary

This is a confirmed **false positive** on the indexer's `vacuous_pass` adjudication flag, not a genuine degenerate-criterion problem. The run's actual load-bearing gate (`core_channels_non_degenerate`, scoped to 4 named core channels: z_harm_a, z_harm_un, drive, z_goal) is real, non-degenerate, and correctly computed. The flag fires because the indexer's legacy join between `interpretation.criteria_non_degenerate{}` (a broader, 10-channel informational telemetry report) and `interpretation.criteria[]` (the narrow, 3-entry gating declaration) cannot find a matching `criteria[]` entry for two of the ten reported channels (`channel_vigor`, `channel_z_block`) — because the driver never gave them one; they were only ever meant to be reported, not to individually gate PASS. Under the indexer's documented "ambiguity resolves toward flagging" convention, the unmatched `False` values trip `vacuous_pass` on an otherwise-real PASS.

## 1. Facts

Manifest `v3_exq_906_full_stack_observational_fishtank_20260809T003857Z_v3`, `claim_ids: []`, `experiment_purpose: diagnostic`, `evidence_direction: non_contributory`. Not a dry run. Recording core present, no recording-debt.

One precondition (`harm_pathway_trained`, measured=3794.0 vs threshold=1.0, `met: true`, wide margin). `criteria_non_degenerate{}` (10 keys, informational): 8 true, `channel_vigor: false`, `channel_z_block: false`. `criteria[]` (3 entries, gating): `core_channels_non_degenerate` (load_bearing, passed=true), `harm_pathway_trained` (load_bearing, passed=true), `freeze_not_locked` (non-load-bearing, passed=true). `summary_markdown` is explicit and honest about the flat channels ("vigor: FLAT," "z_block: FLAT").

Driver (`ree-v3/experiments/v3_exq_906_full_stack_observational_fishtank.py`): docstring states explicitly "Claims: None (diagnostic showcase; does not weight governance)... this script exists to look, not to score." `CORE_CHANNELS = ["z_harm_a", "z_harm_un", "drive", "z_goal"]` (line 221) is the only scope of the load-bearing gate (`core_ok = all(chan_nondegen.get(k, False) for k in CORE_CHANNELS)`, line 604). All 10 monitored channels are computed and rolled into `criteria_non_degenerate{}` for reporting, but only the 4-channel subset feeds the single `core_channels_non_degenerate` gating criterion.

**Mechanical trace of the flag** (`build_experiment_indexes.py`'s diagnostic adjudication gate): readiness recomputation passes (met, not unmet); the aggregation-vacuity check on `criteria[]` passes (no load-bearing entry is `passed: false`); the legacy fallback join builds `by_name = {core_channels_non_degenerate: True, harm_pathway_trained: True, freeze_not_locked: False}` from `criteria[].name -> load_bearing`, then for every key in `criteria_non_degenerate{}` tries to match a `criteria[]` name. For `channel_vigor`/`channel_z_block`: zero candidates match (no `channel_*`-prefixed `criteria[]` entry exists at all — the aggregate is named `core_channels_non_degenerate`, not `channel_...`). Per the documented design ("0 candidates (unmatched)... ambiguity resolves toward FLAGGING"), the unmatched `False` values are not excluded, and `any(v is False for v in degeneracy_assertions)` while `status=="PASS"` returns `vacuous_pass`.

**Root cause**: the join key space has no possible matching name in `criteria[]` at all — the driver rolled 10 channels' non-degeneracy status into exactly one aggregate gating criterion covering only 4 of them, by design. This is a **third, distinct sub-case** of the join-mismatch class beyond the two documented precedents (V3-EXQ-783 name-spelling mismatch, V3-EXQ-830 direction-reversed key/name length) — here no corresponding `criteria[]` entry exists at all, by design, not by a spelling slip.

**Confirmed recurring, not one-off**: both `v3_exq_665_curriculum_affective_fishtank_showcase` runs (2026-06-10) carry `adjudication: "vacuous_pass"` in `claim_evidence.v1.json` under the identical mechanism, and neither has ever been autopsied (~2 months un-adjudicated, discovered live during this investigation).

## 2. Claim-layer mapping — not applicable

`claim_ids: []`. No claim is under test, tagged, or at risk of mis-weighted demotion/promotion. Explicit and intentional per the driver's own docstring.

## 3. Biological-reference triage — largely not applicable

No mechanism is under test as a claim. One narrow, non-pursued observation: `vigor` (MECH-320 tonic vigor) and `z_block` (MECH-353 blocked-agency) read exactly flat (std=0.0000) in this eval — plausibly an artifact of this specific observational configuration (sparse block events, only 10 across 447 eval steps) rather than a substrate defect. Not escalated: `claim_ids=[]` means there is no claim this would weigh against, and the driver's own design already treats these two as non-load-bearing for the showcase's PASS.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | N/A | no claim under test by design |
| Biological reference | N/A | no mechanism-vs-claim triage applicable |
| Dependency prerequisites | N/A | — |
| Implementation completeness | complete (for what's gated) | `core_channels_non_degenerate` correctly implemented and scoped; harm pathway genuinely trained (3794 steps) |
| Environment adequacy | adequate for stated purpose | broadest mechanically-stable flag combination, full curriculum, matches the driver's own showcase-breadth goal |
| Measurement adequacy | adequate for the run; the ADJUDICATION TOOLING is under-instrumented | the run's own metrics are complete and honestly reported (including the flat channels); the defect is in the indexer's join heuristic, not the experiment |
| Integration adequacy | N/A | — |
| Scale/capacity | N/A | — |

## 5. Cluster pattern (tooling recurrence, not a claim cluster)

Not a claim-bearing cluster (no `substrate_ceiling` reading, no claim recurrence). But there is a genuine recurrence worth naming as a tooling pattern: 3 confirmed instances of the identical false-positive mechanism (this run + both V3-EXQ-665 runs), all `experiment_purpose: diagnostic`, all `claim_ids: []`, all `vacuous_pass`. One structural property of this driver family's declaration shape (a broad-report/narrow-gate split with no per-excess-channel `criteria[]` entry), not three independent bugs.

## 6. Learning extracted / routing (confirmed)

**Diagnosis class**: `complicated (buildable)` — the fix is a named build with no open scientific question: either (a) driver-side, have this driver family emit an explicit `criteria[]` entry per reported-but-non-gating channel with `load_bearing: false`; or (b) indexer-side, recognize that an aggregate `criteria[]` entry declares its own channel scope and exclude `criteria_non_degenerate{}` keys outside that scope from the vacuity check by default.

**Routing: no claim-facing action.** `claim_ids: []` means no governance demotion/promotion, no `/lit-pull`, no `/queue-experiment` re-test. Recommend to governance: treat this run's adjudication as a known false positive, clear it from `pending_review.md`'s flagged-diagnostic section without further action. Surface (not build, per scope discipline) the indexer/driver join-gap as out-of-scope maintenance for whoever next touches `build_experiment_indexes.py` or this driver family. Note the two orphaned V3-EXQ-665 `vacuous_pass` flags (2026-06-10) as pre-existing, now-discovered instances of the identical mechanism, so they aren't independently re-discovered.

`recommended_substrate_queue_entry.action: none` — not a substrate gap.

**Step 9b**: not applicable — no claim under test, no `fanout_recommendation`.

## 7. Evidence quality note (informational — no claim to attach it to; offered for the manifest/governance record)

> PASS is genuine and not vacuous: the run's load-bearing gate (core_channels_non_degenerate, scoped to z_harm_a/z_harm_un/drive/z_goal per CORE_CHANNELS) and harm_pathway_trained (3794 optimizer steps, 3794x threshold) both cleared on real signal. The indexer's vacuous_pass flag is a false positive: its legacy criteria_non_degenerate{} <-> criteria[] join has no matching criteria[] entry for channel_vigor/channel_z_block (this driver intentionally reports 10 channels' non-degeneracy but gates on only 4 via one aggregate criterion), so the unmatched False values are conservatively treated as ungated degenerate gate-clearers. Same mechanism confirmed on both V3-EXQ-665 runs (2026-06-10), neither previously autopsied. No claim is affected (claim_ids: []); no governance action required beyond clearing the flagged-diagnostic pending_review entry.
