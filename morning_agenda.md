# Morning Agenda — 2026-05-21

Generated: 2026-05-21T04:29:03Z

Pipeline run headless. No governance decisions made, nothing marked reviewed.

---

## Queue Status
- Total pending: 10 (Mac: 1 | PC: 0 | EWIN: 0 | any: 9)
- In progress (claimed): 3 — V3-EXQ-483c (ree-cloud-2), V3-EXQ-588b (ree-cloud-4), V3-EXQ-590a (ree-cloud-3)
- Queue depth healthy (>= 3 pending). No low-queue alert.
- Affinity note: only 1 machine-pinned item (V3-EXQ-592 -> DLAPTOP-4.local, GAP-11 committed-mode curriculum pilot). All other pending items are `any`.

Pending items: V3-EXQ-490g, 471a, 475a, 591, 592, 598, 599, 600, 601, 602.

---

## Experiments Awaiting Review (0 indexed / 0 runner-only)

`pending_review.md` reports **0 pending** — 0 PASS, 0 FAIL, 0 runner-only, 0 unclaimed manifests. All experiments reviewed; nothing to research this cycle.

---

## Errors to Diagnose (0)

No undiagnosed errors. `pending_review.md` reports 0 runner-only (ERROR/UNKNOWN/smoke) entries.

Note: `evidence/experiments/runner_status.json` was not found in the repo this run — error status was taken from `pending_review.md` (the indexer-derived runner-only count), which is the authoritative pending-error source.

---

## Governance Agenda (0 actionable recommendations)

No `pending_user` recommendations. All 115 rows in the `promotion_demotion_recommendations.md` decision queue carry `decision_status: applied` — governance has already processed every recommendation.

Standing (already-applied) holds, for context only — no action required:
- 160 × `hold_pending_v3_substrate` — claims awaiting V3 substrate evidence
- 56 × `hold_candidate_resolve_conflict` — candidates with unresolved conflict
- 14 × `narrow_open_question` — open questions near resolution

---

## Active Plans Heartbeat (7 plans)

| Plan | Phases in-flight | Blocked | Paused | Stale rows | Last decision |
|---|---|---|---|---|---|
| arc_062_rule_apprehension | 4 | 0 | 0 | 3 | 2026-05-21 |
| commitment_closure | 1 | 1 | 0 | 2 | 2026-05-20 |
| goal_pipeline | 1 | 1 | 0 | 1 | 2026-05-20 |
| infant_substrate | 1 | 0 | 0 | 0 | 2026-05-21 |
| sd033_governance | 0 | 0 | 0 | 0 | 2026-05-09 |
| self_attribution | 0 | 3 | 0 | 3 | 2026-05-17 |
| sleep_substrate | 0 | 1 | 0 | 1 | 2026-05-17 |

Notes:
- "Phases in-flight" counts rows with status `in-progress` or `open`. Rows tagged `partial` are not counted as in-flight but are listed below when stale.
- `sd033_governance` is a sub-plan of `commitment_closure`; all 8 of its nodes are `done`.
- `sleep_substrate` GAP-2 is `upstream-blocked` (counted as blocked).
- Rows with status `deferred v4` are excluded from the stale count (treated as deferred).
- No PLAN STALING flag: no plan has gone >14 days without a decision-log entry while holding in-flight phases.

**arc_062_rule_apprehension stale rows:**
- GAP-H (partial) — Last updated 2026-05-10 (11 days)
- GAP-I (partial) — Last updated 2026-05-10 (11 days)
- GAP-K (in-progress) — Last updated 2026-05-10 (11 days)

**commitment_closure stale rows:**
- GAP-4 (partial) — Last updated 2026-05-08 (13 days)
- GAP-8 (blocked) — Last updated 2026-05-08 (13 days)

**goal_pipeline stale rows:**
- GAP-2 (blocked) — Last updated 2026-05-08 (13 days)

**self_attribution stale rows:**
- GAP-1 (blocked) — Last updated 2026-05-11 (10 days)
- GAP-2 (blocked) — Last updated 2026-05-08 (13 days)
- GAP-3 (blocked) — Last updated 2026-05-08 (13 days)

**sleep_substrate stale rows:**
- GAP-2 (upstream-blocked) — Last updated 2026-05-09 (12 days)

---

## Literature Pull Candidates (Top 5)

Only 2 backlog items list `literature` in `evidence_needed`:

| # | Claim | Subject | Priority | Existing entries |
|---|-------|---------|----------|-----------------|
| 1 | MECH-339 | Composite retrieval cue / outshining gate (EVB-0276; needs experimental + literature) | medium | 0 |
| 2 | Q-019 | Three-Gate BG Architecture: Literature Extraction (EVB-PINNED-Q019) | medium | 0 |

No `targeted_review_*` directory exists for either claim yet.

---

## Machine Fleet (runner heartbeats)

All 6 reporting machines show state `running`:
- DLAPTOP-4.local (Mac) — V3-EXQ-591 (ARC-046 infant curriculum), 57.3% complete, last tick 2026-05-21T04:22Z
- ree-worker-1 — V3-EXQ-591
- ree-cloud-2 — V3-EXQ-483c
- ree-worker-3 — V3-EXQ-590a
- ree-cloud-4 — V3-EXQ-588b
- ree-cloud-1 — heartbeat last written 2026-05-20T22:25Z

---

## Serve.py Status
- RUNNING on port 8000.

---

## Blocked Items
- None for the digest run itself. No TASK_CLAIMS collision — governance.sh ran normally (with `SKIP_TRACEABILITY=1`; the traceability check reports 120 developmental claims missing register rows, informational only and non-blocking).
- `runner_status.json` absent from `evidence/experiments/` — noted under Errors to Diagnose; did not block the digest.
- **Fleet anomaly worth a look:** during this digest run a runner heartbeat fired `git pull --rebase --autostash` against REE_assembly and autostashed in-flight work. Two autostash entries are sitting in `git stash list`: `stash@{0}` is this digest's regeneration (recovered by re-running governance.sh — redundant, safe to drop), but `stash@{1}` holds an **earlier session's uncommitted edits** to `docs/claims/claims.yaml`, `evidence/planning/substrate_queue.json`, and `evidence/planning/inter_governance_workset.{md,v1.json}`. This stash was stranded before the digest started — review whether that work is already on `origin/master` before dropping it.
