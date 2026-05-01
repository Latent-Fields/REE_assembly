# Duplicate-Manifest Sweep — Phase 2 Manual Review Queue

Generated: 2026-05-01T19:56Z by post-EXQ-232 deduplication sweep.

These 4 Tier-2 clusters (span 2-24h between byte-identical-output manifests) had a git commit affecting the experiment script *between* the two emission timestamps. Auto-supersession was deferred — a human call is needed because either:
(a) the script change was cosmetic/no-op for output (still a real duplicate),
(b) the experiment short-circuited before reaching the changed code path (still a duplicate),
(c) the script change was real and the two outputs really being identical is a coincidence (unlikely with non-trivial metrics) or a bug elsewhere (probably a duplicate of a different kind).

In all 4 cases the seed_results / metrics signatures are bit-for-bit identical, which is hard to reconcile with a substantive script change unless the code path was unreachable.

## Clusters

### 1. v3_exq_074f_mech112_117_wanting_liking
- **Span:** 2.05h (2026-04-04 00:23:24Z -> 02:26:09Z)
- **Claims affected:** MECH-112, MECH-117 (both currently dir=supports/PASS)
- **Intervening commit:** c6c0cf5 (2026-04-04 01:27 BST) `cowork-2026-04-04-b: EXQ-223 re-queued; 074e->074f, 076e->076f; EXQ-224 in queue`
- **Likely diagnosis:** This commit appears to have created `074f.py` via rename from `074e.py`. The first emission (00:23Z = 01:23 BST, before commit) predates the file under that name -- suggests the file was renamed but the logic was unchanged, so identical output is expected. Probable real duplicate.
- **Recommended action:** confirm via `git log --follow -p experiments/v3_exq_074f...py` that the rename was content-preserving, then supersede the older copy.

### 2. v3_exq_497_mech293_ghost_probes_validation
- **Span:** 3.44h (2026-04-27 06:17:45Z -> 09:43:53Z)
- **Claims affected:** MECH-293 (dir=supports)
- **Intervening commit:** 9cd984c (2026-04-27 07:24 BST) `mech293: waking ghost-goal probe search consumer of MECH-292 bank`
- **Likely diagnosis:** Substantive content change between emissions. Identical output is suspicious. Either the new code path didn't fire (substrate guard?) or the experiment is testing something not affected by the change.
- **Recommended action:** read the commit diff and check whether the experiment's outputs depend on the changed code path.

### 3. v3_exq_496_mech292_ghost_goal_bank_validation
- **Span:** 4.06h (2026-04-27 05:39:46Z -> 09:43:39Z)
- **Claims affected:** MECH-292 (dir=supports)
- **Intervening commit:** 42f879f (2026-04-27 06:45 BST) `mech292: ranked ghost-goal bank substrate (derived view over SD-039 anchor pool)`
- **Likely diagnosis:** Sister case to 497. Same review approach.
- **Recommended action:** read the commit diff and check whether the experiment short-circuits on the substrate guard.

### 4. v3_exq_223_minimal_vertebrate_ablation
- **Span:** 12.67h (2026-04-03 23:00:55Z -> 2026-04-04 11:40:52Z)
- **Claims affected:** (no claim_ids on manifest -- but listed as PASS/supports)
- **Intervening commit:** c6c0cf5 (2026-04-04 01:27 BST) -- same commit as cluster #1 above
- **Likely diagnosis:** EXQ-223 was "re-queued" in this commit (likely with no script change of its own; the file might have been touched only as part of a larger commit). Probable real duplicate.
- **Recommended action:** confirm 223 script wasn't substantively changed by c6c0cf5, then supersede.

## Summary
- Phase 1 + Phase 2 unchanged-script: 13 + 6 = 19 phantom entries cleaned (5 EXQ-232 + 8 Tier-1 + 6 Tier-2-unchanged).
- Phase 2 script-changed: 4 clusters, 4 phantom entries pending human call (above).
- Tier 3 (10 clusters, span 1-7d, includes a striking 107h-batch-replay pattern): not yet investigated.
- Tier 4 (2 clusters, span >7d): edge cases, not yet investigated.

---

## Phase 3 Addendum (added 2026-05-01T20:00Z)

Tier-3 sweep complete — 10 clusters, 12 phantom manifests superseded.

**Root cause identified:** Runner regex bug active 2026-03-27 to 2026-03-30 (fixed in commit `071f1fc` "diagnose-errors: fix runner regex bugs + unblock queue (5 UNKNOWN re-queues)"). The runner's `RE_EXQ_VERDICT` regex did not match the `Done. Outcome: PASS/FAIL` format used by newer experiment scripts, so it logged outcomes as UNKNOWN and silently re-ran already-completed experiments. This produced two visible batch events:

- **2026-03-28 18:12** (within 37 seconds): re-emissions of 074e, 071d, 076e
- **2026-04-02 01:20–03:33**: re-emissions of 072b, 073b, 075d, 084d (the striking ~107h-span cluster from the analysis)

**Convention deviation from Phase 1/2:** Tier 3 kept the OLDEST emission as canonical (most likely the legitimate original observation), inverting the Phase 1/2 "keep latest" rule. Documented in each superseded manifest's note.

## Cumulative cleanup totals (after Phase 3)

| phase | clusters | manifests superseded |
|---|---|---|
| ARC-026 fix | 1 | 5 |
| Phase 1 (Tier 1, span <2h) | 8 | 8 |
| Phase 2 auto (Tier 2, unchanged script) | 6 | 6 |
| Phase 3 (Tier 3, regex-bug period) | 10 | 12 |
| **Total** | **25** | **31** |

Phase 2 manual-review queue (4 clusters: 074f, 497, 496, 223) remains pending.
Tier 4 (133, 137) remains pending.
Tooling fix in `build_experiment_indexes.py` remains pending.
