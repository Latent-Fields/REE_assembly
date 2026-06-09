# Morning Agenda — 2026-06-09

Generated: 2026-06-09T04:21:11Z

---

## Queue Status
- Total pending: **0** (Mac: 0 | PC: 0 | EWIN: 0 | any: 0)
- **ALERT: Queue empty — 0 pending experiments.** Queue holds 1 item total: `V3-EXQ-640b` (status `claimed`, running on `DLAPTOP-4.local`, priority 300 — cue-authority gain sweep / 640b). Nothing is waiting behind it.
- Action: queue the next experiment(s) soon. The post-603i E2-escape-affordance-linker readiness microdiagnostic (V3-EXQ-653) was claimed last night (TASK_CLAIMS `queue-experiment-653`, now stale ~7h) but is **not present in the queue file** — verify whether it was ever committed/landed or needs re-queuing via `/queue-experiment`.

---

## Experiments Awaiting Review (0 indexed / 0 runner-only)

Pending review = **1 item**, but it is a diagnostic self-route flagged for adjudication, not a standard PASS/FAIL review:

### V3-EXQ-603i — escape_affordance_bridge_validation — FAIL
- **Run ID:** `v3_exq_603i_escape_affordance_bridge_validation_20260608T201133Z_v3`
- **Claims tested:** none (claim-free diagnostic — does not weight any claim)
- **Self-route label:** `substrate_not_ready_requeue`, flagged **`precondition_unmet`** by the indexer (a declared precondition's `met` is false — the self-route's premise did not hold). Per the diagnostic adjudication gate, this label must NOT drive a governance action until adjudicated.
- **Classification:** diagnostic (substrate-readiness for SD-059/MECH-358 escape-affordance bridge)
- **Status — autopsy landed:** A `/failure-autopsy` was run last night and **is now on origin/master** (commit `3c714ae49d`, carried up by the governance session `d1efafaf31`). Verdict: `substrate_not_ready_requeue` confirmed — nav-competence ceiling primary, safety-half starvation secondary; amended x2 as a handoff to governance. The run stays in `pending_review` only because clearing a flagged diagnostic for review does not clear its adjudication flag; the manifest `interpretation` is source of truth.
- **Governance impact:** none yet — claim-free; SD-059/MECH-358 stay candidate/v3_pending and unweakened regardless. The autopsy adjudicates whether the bridge substrate is genuinely not-ready (re-queue a corrected successor) vs the diagnostic's own precondition being mis-set.

---

## Errors to Diagnose (0 new)

No new undiagnosed errors. `runner_status.json` carries 87 historical ERRORs (of 808 completed), but `generate_pending_review.py` reports **0 runner-only (ERROR/UNKNOWN/smoke) pending** — all are already recorded in `review_tracker.json` `discussed_experiment_dirs` and/or superseded by lettered successors. Nothing routes to `/diagnose-errors` this morning.

---

## Governance Agenda (3 recommendations, all holds)

All three `pending_user` items are `hold_pending_v3_substrate` — not promote/demote actions, just awaiting V3 substrate before evidence can be collected. The rest of the Decision Queue is `applied`/`approved`.

- **MECH-346** (`candidate`) — Recommendation: **hold** (`hold_pending_v3_substrate`)
- **MECH-347** (`candidate`) — Recommendation: **hold** (`hold_pending_v3_substrate`)
- **SD-057** (`candidate`) — Recommendation: **hold** (`hold_pending_v3_substrate`)

No promotion or demotion decisions are pending. (MECH-346/347 + SD-057 are the cue-authority cohort held per user at the 2026-06-08 governance cycle.)

---

## Active Plans Heartbeat (11 plan files; 3 active, 8 done/blocked)

> Parse note: the status-table parser is heuristic and tolerant of column variation. `status=?` rows below are plans whose frontmatter `Status:` line did not match the parser but which recent governance touched (treated as active). Counts may slightly under-read rows in non-standard tables.

| Plan | Phases in-flight | Blocked | Paused | Stale rows | Last decision |
|---|---|---|---|---|---|
| arc_062_rule_apprehension_plan | 0 | 0 | 0 | 0 | 2026-05-08 |
| arm_reuse_fingerprint_plan | 0 | 0 | 0 | 0 | — |
| behavioral_diversity_isolation_plan | 2 | 0 | 0 | 0 | — |
| commitment_closure_plan (done) | 0 | 0 | 0 | 0 | 2026-06-02 |
| goal_pipeline_plan (done) | 0 | 0 | 0 | 0 | 2026-05-08 |
| infant_substrate_plan (done) | 0 | 0 | 0 | 0 | 2026-05-16 |
| sd033_governance_plan (done) | 0 | 0 | 0 | 0 | — |
| sd_037_axis_a_..._plan (done) | 0 | 0 | 0 | 0 | — |
| sd_037_axis_b_..._plan (blocked_pending_substrate) | 0 | 0 | 0 | 0 | — |
| self_attribution_plan (blocked) | 0 | 0 | 0 | 0 | 2026-04-21 |
| sleep_substrate_plan (done) | 0 | 0 | 0 | 0 | 2026-05-31 |

- No stale rows detected across any plan.
- `arc_062_rule_apprehension_plan` last logged decision 2026-05-08 (>14d ago) but its in-flight count is 0 and it was reconciled in the 2026-06-08 governance cycle (GAP-A done / GAP-B open / GAP-H partial / GAP-K in-progress), so no staling flag.
- `behavioral_diversity_isolation_plan` shows 2 rows in-flight (GAP-B partial after V3-EXQ-614e autopsy; GAP-C in-flight on the 603i lineage) — both were reconciled 2026-06-08.

---

## Literature Pull Candidates (Top 5)

No high-priority literature gaps; all top items are `medium`. 15 backlog items list `literature` in `evidence_needed`.

| # | Claim | Subject | Priority | Existing entries |
|---|-------|---------|----------|-----------------|
| 1 | ARC-046 | (no subject in backlog record) | medium | 0 |
| 2 | SD-055 | (no subject in backlog record) | medium | 0 |
| 3 | MECH-282 | (no subject in backlog record) | medium | 0 |
| 4 | MECH-286 | (no subject in backlog record) | medium | 0 |
| 5 | MECH-306 | (no subject in backlog record) | medium | 0 |

---

## Serve.py Status
- **RUNNING on port 8000** (PID 62468).

---

## Blocked Items
- No TASK_CLAIMS collision with the governance collision set — governance.sh ran normally. (The one `active` claim, `queue-experiment-653`, was ~7h old and stale; it covers only the queue file + a script, outside the collision set.)
- **Cleared this run:** a stale `ree-v3/.git/ORIG_HEAD.lock` (empty, from 2026-06-08T23:07, crashed git process, no holder) was removed to allow the `ree-v3` pull.
- No outstanding hand-off blocks: the 603i autopsy and the prior governance regen both landed on origin/master overnight (`3c714ae49d` / `d1efafaf31` / `17c8335695`).

---

*Read-only digest. No governance decisions made, nothing marked reviewed.*
