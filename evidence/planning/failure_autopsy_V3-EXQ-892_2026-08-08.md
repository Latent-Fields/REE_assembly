# Failure Autopsy: V3-EXQ-892 (MECH-322 replay-origin corroboration survival, diagnostic PASS)

Generated: `2026-08-08T06:33:36Z`
Scope: single
Status: confirmed

## Facts

- **Run**: `v3_exq_892_mech322_replay_corroboration_survival_20260808T051616Z_v3`, queue_id `V3-EXQ-892`, backlog EVB-0489. **Diagnostic PASS** -- requires confirmed autopsy per the 2026-08-07 policy (every `experiment_purpose: "diagnostic"` result needs adjudication regardless of adjudication flag).
- **Purpose**: diagnostic. Not a lettered continuation of V3-EXQ-873a. 873a's own question ("does the AND-gate fire and fail closed?") is answered (see the 873a Step 9b fix below); this is a NEW EXQ number for the distinct question 873a's autopsy explicitly routed onward and left open: does a minted replay-origin chunk ever get corroborated by real waking re-execution before its dissolution deadline, under realistic (non-accelerated) conditions?
- **Dry-run check**: `check_dry_run_citations.py` -> 0 dry, clean.
- **Recording core**: `substrate_hash` present, `substrate_commit` (`ca5fd4cff4`, clean, branch main), `machine_class`, `elapsed_seconds` (26025s -- a genuinely long run, 8 seeds x 3 arms x 120 episodes), full `config`, explicit `seeds: [101, 202, 303, 404, 505, 606, 707, 808]`. No recording gap.
- **Design**: 3 arms differing ONLY in corroboration deadline N (episode budget within which a real re-execution must land to prevent dissolution): `ARM_DEADLINE_15` (873a's accelerated regime, replicated as a negative-baseline control), `ARM_DEADLINE_75` (the SUBSTRATE DEFAULT -- the realistic condition, primary arm), `ARM_DEADLINE_200` (deadline set beyond the run length, isolating the true deadline-independent recurrence/exposure rate). Same seed mints the same sequence in all three arms; only the post-mint deadline counter differs. Single early sleep checkpoint (episode 20 of 120 -> 100 post-mint waking episodes), unlike 873a's late checkpoint (ep 90 -> only 30 post-mint episodes), specifically to give corroboration a real window to occur in.
- **C1/C2 are readiness/instrument gates, not the finding**: C1 = mint-fires-under-valid-conditions (fraction of cleared seeds that minted a `replay_origin=True` chunk, floor 1.0) -- **1.0 (7/7)**. C2 = minted-chunk-fate-trackable (every minted chunk's end-state is observable and internally consistent) -- **true**. Both green; `non_degenerate: true`. `readiness_seed_fraction_by_arm`: 0.875 (7/8 seeds cleared) on all three arms, above the 0.4 floor.
- **The actual finding (both directions pre-declared valid)**:
  | Arm | Deadline N | Corroboration rate | Survival rate | Crystallised |
  |---|---|---|---|---|
  | ARM_DEADLINE_15 (873a replication) | 15 | 42.9% (3/7) | **0.0%** (0/7) | 0/7 |
  | ARM_DEADLINE_75 (realistic default, primary) | 75 | 71.4% (5/7) | **57.1%** (4/7) | 4/7 |
  | ARM_DEADLINE_200 (deadline-independent) | 200 | 85.7% (6/7) | **85.7%** (6/7) | 4/7 |
  `exposure_recurrence_counts_n200` (per-minted-chunk re-execution counts, N=200 arm): `[0, 1, 2, 4, 6, 9, 11]` -- a genuine, non-degenerate spread, not all-zero or all-identical. `first_corroboration_offsets_n200`: `[1, 5, 5, 36, 36, 88]` -- corroboration timing spans nearly the entire post-checkpoint window.
- **Negative-control replication**: `ARM_DEADLINE_15` reproduces 873a's 0% survival finding under the accelerated regime exactly (873a: 7/7 dissolved under N=15/late-checkpoint; here: 0/7 survived under N=15/early-checkpoint) -- confirms the accelerated-dissolution safety valve fires consistently, not as an artifact of 873a's specific checkpoint timing.
- **Self-route label**: `replay_corroboration_survives_under_realistic_conditions`, correctly computed per the driver's own logic (`any_corroboration_observed and realistic_survived_any` under the primary N=75 arm) and matching the data above.

## Claim-layer mapping

**MECH-322** (sleep-replay carve-out mint/lifecycle). First confirmed support was 873a (2026-08-07, this same session's earlier work -- see the companion fix below); this is MECH-322's second genuine experimental touchpoint, testing a distinct post-mint-lifecycle question rather than re-testing the AND-gate.

## Biological-reference triage

- **Closest mechanism**: hippocampal-striatal offline replay driving sleep-dependent procedural-memory consolidation, with corroboration-by-re-execution as the biological analogue of memory-trace stabilization requiring behavioral reinforcement (a replay-tagged trace that is never behaviorally corroborated is expected to be pruned, not permanently retained).
- **Is formal import**: no.
- **Divergence**: none identified -- the deadline-gated dissolution behavior (short window = mostly fails to corroborate and safety-valve prunes; long window = mostly succeeds) is exactly the biologically-expected pattern.
- **Lit status**: present (inherited from MECH-322's existing lit base; Albouy 2013, Graybiel striatal-chunking, Thompson 2026 DLS procedural replay).

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | strengthened | genuinely informative both-directions-valid design; answers the exact question 873a's autopsy deferred |
| Biological reference | clear | deadline-dependent corroboration/pruning matches biological expectation for replay-tag stabilization |
| Prerequisites | present | entire mechanism confirmed built and validated by 873a itself (7/8 seeds minted correctly) |
| Implementation | complete | readiness (0.875 seed fraction), mint fraction (1.0), trackability (C2) all green across all three arms |
| Environment | adequate | same env family as 873a/810a, validated |
| Measurement | adequate, unusually careful | deadline isolated cleanly (same seed mints same sequence in every arm; only the post-mint counter differs); deadline-independent N=200 arm separately measures the true exposure/recurrence rate |
| Integration | coupled | exercises the mint -> corroborate -> survive lifecycle through the real chunk library and episode-end hooks, not a synthetic harness |
| Scale | 8 seeds, 7 cleared readiness, non-degenerate spread across all readouts | adequate for this fraction-based statistic |

## Learning extracted

- A replay-origin-tagged chunk CAN survive to real corroboration under realistic (non-accelerated) conditions: 57.1% did under the substrate default deadline (N=75), and 85.7% corroborated at least once given unlimited exposure window (N=200).
- The accelerated-regime 0% survival finding from 873a was a genuine artifact of an artificially short deadline, not evidence that corroboration cannot happen in principle -- confirmed by a clean negative-control replication in this same run.
- Corroboration timing (`first_corroboration_offsets_n200`) is genuinely deadline-independent per design and spans nearly the full post-checkpoint window (offsets 1 to 88 of 100 episodes), meaning a realistic deadline needs real headroom -- a short deadline is not merely "less generous," it specifically excludes the late-corroborating chunks that make up part of the true recurrence distribution.
- This closes the open question 873a's autopsy explicitly deferred, and does so with a clean, well-instrumented, non-vacuous result in both possible directions.

## Routing (user-confirmed)

**Confirm as `supports`.** The self-route label is correctly earned by the data -- non-vacuous, well-instrumented, matched design with a clean negative-control replication of 873a's finding. No further routing needed beyond governance applying this disposition; this closes EVB-0489's open question.

Draft `evidence_quality_note` for governance:

> V3-EXQ-892 (2026-08-08, diagnostic PASS, replay_corroboration_survives_under_realistic_conditions, confirmed autopsy): answers the post-mint-lifecycle question 873a's autopsy explicitly deferred. C1 (mint fraction 1.0/1.0) and C2 (fate trackable) are readiness/instrument gates, both green; the finding itself is descriptive and pre-declared both-directions-valid. Under the realistic default deadline (N=75), 57.1% (4/7) of minted replay-origin chunks survived via genuine emergent re-execution; under the deadline-independent N=200 arm, 85.7% (6/7) corroborated at least once; the accelerated N=15 arm cleanly replicated 873a's 0% survival finding as a negative control, confirming the accelerated-dissolution safety valve fires consistently rather than being an artifact of 873a's checkpoint timing. evidence_direction: supports.

## Substrate queue entry

`action: none` -- no substrate work needed; this is a confirming measurement of already-built and validated substrate.

## Re-derive brake

`fired: false` -- 0 prior `substrate_ceiling` hits for MECH-322 (873/873a were `measurement_test_design_defect` / `standard` respectively).

## Hypothesis-space ledger

New question registered and resolved in this same edit (Step 9b) -- see companion JSON and the registry diff. Distinct from the existing `mech322_replay_carveout_and_gate_validity` question (the AND-gate mint/fail-closed question, which this autopsy also fixes -- see below).

## Companion fix: V3-EXQ-873a's own Step 9b was never run (user-instructed)

While registering this run's new hypothesis-space question, found that the EXISTING `mech322_replay_carveout_and_gate_validity` question (registered 2026-08-03 off 873's autopsy) still carries its single hypothesis (`H-mech322-andgate-fires-and-fails-closed`) stamped `resolution.state: "alive"`, `resolved_utc: "2026-08-02T21:33:19Z"`, resolving_runs `["V3-EXQ-873"]` -- i.e. still showing 873's own inconclusive result, even though 873a (confirmed 2026-08-07, this session's earlier work) settled the question: 7/8 seeds cleared readiness under the corrected fraction-based gate, all 7 minted correctly, all fail-closed checks (wake, low-value, master-switch-off) held across 8 seeds x 3 arms. This looks like 873a's own Step 9b simply never ran (873a's autopsy JSON confirms it discusses no ledger update).

Fixed directly (not itself a new pre-registration -- an update to an already-registered hypothesis's resolution, using 873a's already-confirmed autopsy as the resolving run):

- `resolution.state`: `alive` -> `confirmed` (supports + control_passed, per the state-mapping table; not `eliminated`/`split` so `met_elimination_bar` stays `false`)
- `resolution.resolving_runs`: `["V3-EXQ-873"]` -> `["V3-EXQ-873", "V3-EXQ-873a"]`
- `resolution.evidence_direction`: `mixed` -> `supports`
- `resolution.epistemic_category`: `measurement_test_design_defect` -> `standard`
- `resolution.self_route_label`: `substrate_not_ready_requeue` -> `replay_carveout_fires_and_fails_closed`
- `resolution.control_passed`: `false` -> `true`
- `resolution.non_degenerate`: `false` -> `true`
- `resolution.resolved_utc`: `2026-08-02T21:33:19Z` -> `2026-08-04T06:23:09Z` (873a's manifest `timestamp_utc`)
- `resolution.basis`: updated to cite 873a's confirmed result
- `decision.decidable`: `false` -> `true` (decidable_now per the confirmed result; `decision_log_ref` left `null` -- that is a human decision-log entry, not something this autopsy sets)

This is a resolution UPDATE on an already-pre-registered hypothesis (873's own `pre_registered_utc` of 2026-08-02 stands unchanged, satisfying invariant 2: `pre_registered_utc <= resolved_utc`), not new denominator growth, so none of the growth invariants (3a/3b) apply.
