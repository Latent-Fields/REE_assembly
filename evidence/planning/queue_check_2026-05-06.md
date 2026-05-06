# Queue Check -- 2026-05-06 (afternoon scheduled, automated mode)

**Generated UTC:** 2026-05-06T14:18Z
**Queue depth at check:** 0 (empty)
**Result:** **NO QUEUE ACTION TAKEN.** Today's batch was queued and run earlier in the day; review and follow-up decisions are the appropriate next step, not more queueing.

---

## Why no item was queued

### Today's batch is in flight or just completed

Earlier today (2026-05-06) ten experiments were queued and have completed:

| Queue ID | Result | Completed |
|----------|--------|-----------|
| V3-EXQ-514d / 514e | UNKNOWN | 01:35Z / 06:48Z |
| V3-EXQ-517b | UNKNOWN/FAIL (FAIL per pending_review) | 02:36Z |
| V3-EXQ-523a | UNKNOWN/PASS | 06:49Z |
| V3-EXQ-525 | PASS (then FAIL re-run) | 06:51Z |
| V3-EXQ-524 / 526 / 527 / 528 / 529 / 531-534 | mixed PASS/FAIL/UNKNOWN | morning batch |
| V3-EXQ-530 | ERROR (SIGTERM) | 09:28Z |
| V3-EXQ-244a | ERROR (SIGTERM) | 09:28Z |

The runner_status entries for today are mostly UNKNOWN at the runner level even though the underlying flat-JSON manifests carry PASS/FAIL — this is a known indexer/runner reconciliation lag. `pending_review.md` lists 18 items: 3 PASS, 10 FAIL, 5 runner-only (ERROR/UNKNOWN) -- these need human review before the next iteration cycle.

### High-priority "proposed" items already have prior runs

The 12 `priority: high` items in `experiment_proposals_index.v1.json` are:

| EVB | Claim | Suggested type | Latest run | Outcome |
|-----|-------|----------------|------------|---------|
| EVB-0192 | MECH-302 | v3_exq_517_mech302_relief_completion_discriminative_pair | V3-EXQ-517b | UNKNOWN today (02:36Z), FAIL per pending_review |
| EVB-0189 | SD-049 | v3_exq_513_sd049_multi_resource_heterogeneity_substrate_readiness | V3-EXQ-513 | UNKNOWN 2026-05-03 |
| EVB-0149 | Q-040 | v3_exq_490_mech269b_vs_rollout_gating | V3-EXQ-490e | FAIL 2026-05-01 (5 iterations done) |
| EVB-0198 | MECH-304 | v3_exq_519_sd051_conditioned_safety_store_readiness | V3-EXQ-519a | PASS 2026-05-04 |
| EVB-0188 | SD-047 | v3_exq_509_sd047_multi_source_substrate_readiness | V3-EXQ-509 | UNKNOWN 2026-05-03 |
| EVB-0061 | SD-011 | v3_exq_106_harm_obs_a_temporal_persistence | V3-EXQ-106a | PASS 2026-04-28 |
| EVB-0065 | ARC-018 | claim_probe_arc_018 (generic placeholder) | V3-EXQ-053/120/172/196/236 | adjudicated retain_ree |
| EVB-0196 | MECH-230 | v3_exq_328b_mech112_zgoal_structured_latent | V3-EXQ-328b | UNKNOWN 2026-04-13 |
| EVB-0197 | MECH-229 | v3_exq_326a_wanting_gradient_nav_fix | V3-EXQ-326a | UNKNOWN 2026-04-14 |
| EVB-0062 | MECH-104 | v3_exq_126_mech104_surprise_gate_pair | V3-EXQ-126 | PASS 2026-04-21 |
| EVB-0209 | SD-032b | v3_exq_445a_sd032b_dacc_full_pipeline | V3-EXQ-445g | UNKNOWN today (23:34Z 2026-05-05), FAIL per pending_review |
| EVB-None | SD-016 | v3_exq_NNN_env_complexity_gate (placeholder name) | n/a (no script) | -- |

Every `priority: high` candidate either:
- Already has the latest iteration completed but pending review (517b, 445g)
- Has older completed iterations whose status persistence in `experiment_proposals.v1.json` is stale (no executed marker propagated)
- Is a generic placeholder (`claim_probe_arc_018`, `v3_exq_NNN_env_complexity_gate`) that requires human design decisions before scripting

The PASS-resolved ones (MECH-304/SD-011/MECH-104) have proposals that should be marked `executed` in the next /governance walk via the proposal-status-persistence block in `build_experiment_indexes.py`. Re-queuing them is not the right move.

### "claim_probe_<lowercase_id>" suggested types are indexer placeholders

83 of 84 "no script exists" proposals share the pattern `claim_probe_<lowercase_claim_id>`. This is the indexer's auto-suggested generic name when it has not been given a specific experiment_type. These are not actionable scripts -- they require design work first (which mechanism, which condition arms, what acceptance threshold). The /queue-experiment skill is not equipped to invent a discriminative-pair design for a generic claim probe in automated mode without human input.

## Recommended next steps (for human session)

1. **Triage `pending_review.md` (18 items)** -- 10 FAILs, 3 PASS, 5 ERROR/UNKNOWN.
   - Decide for each FAIL whether to iterate (new letter) or accept (mark `evidence_direction` and reviewed). Priorities: 517b (MECH-302 FAIL), 445g (SD-032b FAIL), 525 FAIL re-run vs PASS first run, 526 (Q-034), 527 (MECH-112 FAIL+PASS), 418k (SD-016).
2. **Investigate 2026-05-06T09:28Z coincident SIGTERM on ree-cloud-1 + ree-cloud-2** (V3-EXQ-530, V3-EXQ-244a) -- see `diagnose_staging_report.md`.
3. **Mark proposals executed** for the high-priority items where governance has reached PASS verdict (MECH-304 / SD-011 / MECH-104) so the proposal index doesn't keep re-suggesting them.
4. **Design a real probe** for EVB-0065 / ARC-018 if the human still wants iteration there -- "claim_probe_arc_018" is a placeholder name. ARC-018 already has 5 V3 scripts (053, 120, 172, 196, 236) and is adjudicated retain_ree; the proposal may be redundant.
5. **Wait for runner reconciliation** of today's UNKNOWN entries -- many should resolve to PASS/FAIL once the indexer catches up, eliminating most of the apparent UNKNOWN noise.

## Status

`automated_mode_no_queue_action`. Empty queue is the correct state given current pending review depth.
