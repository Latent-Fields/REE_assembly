# Morning Agenda -- 2026-05-25

Generated: 2026-05-25T04:21:23Z

---

## Queue Status
- Total pending: **1** (Mac: 0 | PC: 0 | EWIN: 0 | any: 0 | ree-cloud-3: 1)
- **[ALERT: Queue critically low -- only 1 pending experiment]** Threshold (<3) crossed; new experiments should be queued today.
- V3-EXQ-590a (ree-cloud-3 only): MECH-314 novelty bonus Goldilocks rerun with partial checkpoint -- do NOT run on other hosts.
- V3-EXQ-591 (any): CLAIMED by DLAPTOP-4.local since 2026-05-23T21:06Z (~31h, well past 6h stale threshold). Either the Mac runner is silently stalled on EXQ-591 (ARC-046 infant curriculum, ~120min estimate), or the claim is stale and needs release_claim. Worth checking the Mac runner heartbeat / runner.log.

---

## Experiments Awaiting Review (0 indexed / 0 runner-only)

Nothing pending. `pending_review.md` cleared (last review 2026-05-24T18:16:00Z).

---

## Errors to Diagnose (5 -- after filtering held-by-design)

Cross-referenced runner_status.json completed ERRORs against queue + completed lettered successors. Excluded V3-EXQ-606a and V3-EXQ-598 (fix scripts written but intentionally HELD on the V3-EXQ-543k gate per 2026-05-23 / 2026-05-24 sessions). Remaining:

- **V3-EXQ-008**: V2-era; very old. Likely safe to dismiss but check whether it should be marked discussed in `review_tracker.json`.
- **V3-ONBOARD-smoke-EWIN-PC**: Onboarding smoke for EWIN-PC (Eoin's machine). Original errored 2026-04-06; -b not yet queued. Blocks throughput calibration / contribution attribution for EWIN-PC.
- **V3-EXQ-495**: V3 full-completion gate / MECH-163 dual-systems test (large behavioural run gated on MECH-293). Status unclear -- needs an autopsy check before re-queueing.
- **V3-EXQ-538**: needs `/diagnose-errors`.
- **V3-EXQ-544**: MECH-313 noise-floor substrate-readiness diagnostic. ree-v3 CLAUDE.md reports the substrate landed 2026-05-10 with smoke 5/5 PASS and a queued canonical entry; presence in the runner_status ERROR list suggests an earlier failed attempt that was superseded -- worth confirming via the indexer pass.

(Heuristic over `experiment_runner.runner_status.json` completed list; suffix-trim may miss some lettered successors. Verify before /diagnose-errors.)

---

## Governance Agenda (0 pending_user recommendations)

Every recommendation in `evidence/experiments/promotion_demotion_recommendations.md` has `decision_status: applied`. No action needed from the human at the governance gate. Substrate-side hold queue (V3-pending) continues to dominate -- many MECH-3xx claims sit at `hold_pending_v3_substrate`.

---

## Active Plans Heartbeat (7 plans -- 6 actionable rows below)

| Plan | Phases in-flight | Blocked | Paused | Stale rows | Last decision |
|---|---|---|---|---|---|
| arc_062_rule_apprehension_plan | ? | ? | ? | ? | (parser missed frontmatter; manual check) |
| commitment_closure_plan | 1 | 1 | 0 | 1 | unknown |
| goal_pipeline_plan | 1 | 1 | 0 | 1 | unknown |
| infant_substrate_plan | 0 | 0 | 0 | 0 | 2026-05-16 |
| sd033_governance_plan | 0 | 0 | 0 | 0 | unknown |
| self_attribution_plan | 0 | 3 | 0 | 3 | unknown |
| sleep_substrate_plan | 0 | 1 | 0 | 1 | unknown |

**Stale rows (last_updated > 7 days before today 2026-05-25):**

- **self_attribution_plan**: GAP-1 (Phase 1) last updated 2026-05-11; GAP-2 (Phase 2) and GAP-3 (Phase 3) last updated 2026-05-08. All three rows blocked -- worth a refresh pass to confirm the blockers are still real and that no upstream substrate has landed in the interim.
- **commitment_closure_plan**: GAP-8 (Phase 7) last updated 2026-05-08. Per ree-v3 CLAUDE.md the env extensions (GAP-3) and the rule_state training curriculum helper (GAP-11) landed 2026-05-17, which may have moved the blocker. Recommend re-checking the GAP-8 status row.
- **goal_pipeline_plan**: GAP-2 (Phase 2) last updated 2026-05-08. ree-v3 CLAUDE.md notes MECH-307 default-value recalibration landed 2026-05-12 and V3-EXQ-540e was queued for the validation. Re-check.
- **sleep_substrate_plan**: GAP-2 (Phase 2) last updated 2026-05-09. Worth a fresh status pass given the sleep aggregation cluster Phases A-E all landed 2026-04-25.

No plan triggered the "PLAN STALING" >14-day-no-decision rule for in-flight rows; infant_substrate_plan has the only fresh decision-log entry (2026-05-16).

---

## Literature Pull Candidates (Top 5)

| # | Claim | Subject | Priority | Existing entries |
|---|-------|---------|----------|-----------------|
| 1 | MECH-282 | (subject blank in backlog) | medium | 0 |
| 2 | MECH-286 | (subject blank in backlog) | medium | 0 |
| 3 | MECH-339 | (subject blank in backlog) | medium | 0 |
| 4 | MECH-340 | (subject blank in backlog) | medium | 0 |
| 5 | Q-019 | Three-Gate BG Architecture: Literature Extraction | medium | 1 |

All five are medium priority (no high-priority lit pulls outstanding). MECH-282 / MECH-286 / MECH-339 / MECH-340 just landed substrate-side in the last week and have no targeted_review_* directory yet -- they are the most actionable.

---

## Serve.py Status
- **RUNNING** on port 8000 (PID 22867).

---

## Blocked Items
- No governance.sh collision (all active TASK_CLAIMS entries are stale >6h, so morning-digest proceeded normally).
- `check_backward_traceability.py` reports 120 developmental claims missing from `docs/architecture/developmental_needs_register.md` (WARN-only, does not block the pipeline). Long-running registry-hygiene gap rather than a session blocker.
- 6 active TASK_CLAIMS entries (governance-603-manifests, queue-experiment-598b/588b/608/543l/483d) are >9h old without a `done` flip. Per the autonomous-task protocol these were left in place. Worth a pass to close out the ones whose work has landed.
