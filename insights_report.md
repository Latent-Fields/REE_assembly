# Project Insights — 2026-08-01

Generated: 2026-08-01T12:37:29Z

---

## Experiment Health

- **Total runs:** 229 (PASS: 77 | FAIL: 152 | ERROR: 0 | error rate: 0.0%) — window: last 30 days
  (2026-07-02T05:25Z .. 2026-08-01T12:05Z), source: coordinator DB. 6 unexplained phantom
  completions (no evidence on disk) are not folded into the numerator; treating every one as a
  crash gives an upper bound — **error rate: 0.0%–2.6% (0 recorded ERROR / 229 classified; 6
  phantom completions unclassified)**.
- **Last ERROR recorded fleet-wide:** 2026-06-11T21:18:10Z (per-machine `runner_status/` split;
  unchanged since the 10:44Z run today).
- **High-iteration experiments** (3+ lettered iterations) — 52 base EXQ numbers, unchanged from
  the 10:44Z run this session (2 additional classified runs in the last 90 minutes did not add a
  new letter to any top-20 chain). See that run's table for the full top-20 list — reused here
  per this skill's own rule (same session, same underlying manifest corpus).
- **Recurring trouble spots** (claim_ids in 2+ ERROR entries): **none in the 30-day window** —
  still 0/229 ERROR.
- **Stalled chains:** liveness check from the 10:44Z run stands — **none survive**. Nothing in
  the last 90 minutes of activity (8 new REE_assembly commits: phase3 result manifests, IGW
  ledger updates, one paused governance sync) touched any of the 34 screened claims.

---

## Substrate Bottlenecks

Unchanged from the 10:44Z run this session (18 ready-and-unbuilt entries, 38 blocked, same
failure-record ranking) — `substrate_queue.json` was not among the files touched by the last
90 minutes of commits.

---

## Governance State

- Claims pending V3 substrate (`v3_pending: true`): 228 (unchanged)
- Pending promotion/demotion decisions: **0** — Decision Queue regenerated 2026-08-01T12:26:47Z
  (a "partial, paused: pipeline sync only, no decisions applied" governance cycle ran in the
  interim) — still all 169/169 rows `applied`.
- Evidence superseded (rework): 72 manifests (unchanged).

---

## Literature Coverage

Unchanged from the 10:44Z run this session (3 open items, all `priority: low`; healthy cadence).

---

## Human-Intervention Patterns

Unchanged from the 10:44Z run this session — see that run for the WORKSPACE_STATE
session-type mix and adjudication-pause count.

---

## Recommendations

Re-checked `git log --since="2 hours ago"` immediately before this section — 8 commits landed
(phase3 result manifests, IGW ledger updates, one paused governance cycle) since the 10:44Z run;
none change an autopsy routing or a substrate-queue entry.

1. **No substrate-build recommendation this cycle** — unchanged reasoning from the 10:44Z run.
2. **The pending_review queue grew from 8 to 15 items in the last 90 minutes** (4 PASS to close,
   11 FAIL to adjudicate: MECH-163/Q-085, MECH-180, MECH-476 ×2, MECH-204/SD-076 ×2 diagnostic
   self-routes, MECH-321, Q-040, INV-091, ARC-062/MECH-309, MECH-294). **Unlike the 10:44Z run,
   this queue currently has no TASK_CLAIMS owner** — the session that owned the FAIL side then
   (`elastic-merkle-e0cca8`) has since closed, and the two currently-active claims
   (`igw-214-proposal-for-mech-203`, `frosty-satoshi-2e7cbc`) are scoped to unrelated work. This
   is worth surfacing as a real gap, not a duplicate-of-owned-work case this time.
3. **Literature backlog is not actionable** — unchanged.
