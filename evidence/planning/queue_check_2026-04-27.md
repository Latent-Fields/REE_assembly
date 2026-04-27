# Queue check -- 2026-04-27 (afternoon scheduled)

**Session:** ree-diagnose-queue, automated afternoon run
**Generated UTC:** 2026-04-27T14:20:31Z

## Outcome

**No new experiment queued.** The three highest-priority `proposed` items in the proposals index are all auto-generated `discriminative_pair` templates whose requested evidence has already been produced by passing EXQs the indexer has not yet matched back to the proposal `backlog_id`. Re-queuing would produce duplicate work without scientific benefit. The next 70+ medium-priority `targeted_probe` items are either substrate-blocked (`v3_pending: true`) or generic `claim_probe_*` templates for claims that already have substantial active evidence.

The current `experiment_queue.json` has 1 pending item (V3-EXQ-495, the V3 full-completion gate / MECH-163 dual systems test), which was recently wired with fishtank-viz episode-log emission per the 06:30 session.

## High-priority proposals audited

| backlog_id | claim_id   | dispatch_mode      | suggested_script                                      | actual evidence already on disk                      | recommended action |
|------------|------------|--------------------|--------------------------------------------------------|------------------------------------------------------|--------------------|
| EVB-0061   | SD-011     | discriminative_pair | v3_exq_106_harm_obs_a_temporal_persistence            | V3-EXQ-472 PASS 2026-04-21 (anchor C7 recovery); V3-EXQ-365 PASS; many earlier runs | governance: mark executed, link to V3-EXQ-472 |
| EVB-0062   | MECH-104   | discriminative_pair | v3_exq_126_mech104_surprise_gate_pair                 | **V3-EXQ-126 PASS 2026-04-21** (script name match), V3-EXQ-204 PASS, V3-EXQ-365 PASS | governance: mark executed, link to V3-EXQ-126 |
| EVB-0065   | ARC-018    | discriminative_pair | claim_probe_arc_018                                   | V3-EXQ-053 PASS 2026-03-20 (Rollout Viability Mapping), V3-EXQ-236 PASS 2026-04-05 (Rollout Fidelity Gate, ROLLOUT_k5 vs GREEDY_k1 -- the discriminative pair) | governance: mark executed, link to V3-EXQ-236 |

### Why these did not auto-mark executed

The indexer carries forward non-`"proposed"` statuses by `backlog_id`. These three are coming back each governance cycle because no prior session has linked them to the matching EXQs. They are surfaced because the underlying claims still have `active_conflict` (conflict_ratio above threshold) -- but the resolution is governance work (re-tag stale manifests, supersede pre-substrate evidence -- exactly what the 2026-04-26 SD-011 path-3 cleanup did, dropping conflict_ratio 0.308 -> 0.143), not new experiments.

## Medium-priority proposals audited (top 35)

Substrate readiness from `claims.yaml`:

| backlog_id | claim_id   | claim status / impl_phase | v3_pending | recent evidence | substrate ready? |
|------------|------------|---------------------------|-----------|-----------------|------------------|
| EVB-0069   | MECH-074   | candidate / v3            | true      | -               | NO -- v3_pending |
| EVB-0072   | ARC-060    | candidate / v3            | true      | -               | NO -- v3_pending |
| EVB-0073   | MECH-295   | candidate / v3            | true      | -               | substrate landed 2026-04-26; V3-EXQ-493 already queued |
| EVB-0074   | SD-033e    | candidate / v4            | false     | -               | V4 scope, not V3 |
| EVB-0075   | INV-057    | candidate / -             | -         | -               | generic targeted_probe; no specific substrate hook |
| EVB-0076   | MECH-183   | candidate / -             | -         | -               | generic targeted_probe |
| EVB-0077   | MECH-E2-DUAL-FUNCTION | (not in claims.yaml) | -    | -               | unknown -- claim entry missing |
| EVB-0078   | INV-048    | candidate / -             | -         | -               | generic targeted_probe |
| EVB-0079   | MECH-168   | candidate / -             | -         | -               | generic targeted_probe |
| EVB-0080   | MECH-171   | candidate / -             | -         | -               | generic targeted_probe |
| EVB-0081   | MECH-180   | candidate / -             | -         | -               | generic targeted_probe |
| EVB-0082   | MECH-185   | candidate / -             | -         | -               | generic targeted_probe |
| EVB-0083   | MECH-191   | candidate / -             | -         | -               | generic targeted_probe |
| EVB-0084   | MECH-270   | candidate / v3            | true      | -               | NO -- v3_pending (ephaptic substrate, V4-deferred per 2026-04-26 boundary memo) |
| EVB-0085   | MECH-271   | candidate / v3            | true      | -               | NO -- v3_pending (V3 substrate plan registered 2026-04-26 but module not yet built) |
| EVB-0086   | MECH-275   | candidate / v3            | true      | -               | NO -- v3_pending (scientist-agent cluster) |
| EVB-0099   | MECH-265   | candidate / v4            | true      | -               | NO -- V4 scope |
| EVB-0101   | ARC-051    | candidate / v3            | -         | -               | hold_pending_v3_substrate per 2026-04-26 governance |

The remaining ~35 medium-priority items follow the same pattern: candidate-status claims with no `implementation_phase: v3` flag (so the proposal is a generic targeted_probe template) and no substrate hook explicit enough to write a meaningful discriminative experiment without first deciding what the probe should actually measure. Those decisions belong to governance / claim-design sessions, not to an automated queue-experiment run.

## Why no candidate was queued

The queue-experiment skill is for surfacing a single substrate-ready proposal and writing/queueing a script. In this scan:

1. **High-priority items** have substrate ready AND requested evidence already on disk -- the bottleneck is governance bookkeeping (mark executed), not execution.
2. **Substrate-ready medium-priority items** (i.e., MECH-295) already have queued or executed validation experiments.
3. **All other medium-priority items** are either `v3_pending: true` (substrate not implemented), `implementation_phase: v4` (out of scope for V3 substrate), or generic targeted_probes whose specific test design has not been decided yet.

Queueing a duplicate of V3-EXQ-126 / V3-EXQ-236 / V3-EXQ-472 (the only high-priority items with executable scripts) would consume runner cycles without producing new evidence. The runner currently has V3-EXQ-495 pending which is a more discriminative test (V3 full-completion gate) than any duplicate would be.

## Recommended next governance actions

These are out-of-scope for this scheduled session; flagging for the next interactive governance cycle:

1. **Mark EVB-0061 / 0062 / 0065 as executed** in `experiment_proposals.v1.json`, linking to V3-EXQ-472 / V3-EXQ-126 / V3-EXQ-236 respectively, and rebuild indexes. This will stop them resurfacing each governance cycle.
2. **Walk the underlying conflict_ratios** for SD-011, MECH-104, and ARC-018 -- if conflict_ratio is still high after marking the proposals executed, the next step is the same kind of re-tagging cleanup that landed for SD-011 on 2026-04-26 (path-3 supersession + per-claim non_contributory on over-broad-tagged manifests), not new experiments.
3. **Either resolve or remove `MECH-E2-DUAL-FUNCTION`** -- it appears in proposals_index but has no entry in `claims.yaml`. Likely a stale auto-generated ID from an earlier proposal pass.

## Pending review (informational)

`pending_review.md` shows 13 items as of 2026-04-27T14:12:44Z:
- 4 FAIL (V3-EXQ-433d, V3-EXQ-418e, V3-EXQ-490, V3-EXQ-490 second run)
- 5 PASS (V3-EXQ-496, V3-EXQ-497 x2, V3-EXQ-494, V3-EXQ-496 second run)
- 4 UNKNOWN (V3-EXQ-433d, V3-EXQ-484, V3-EXQ-485, V3-EXQ-493 -- "index stale, run build_experiment_indexes.py")

These are governance-cycle work, not queue-experiment work. The active 14:11 governance session (per TASK_CLAIMS.json) is presumably already handling them.
