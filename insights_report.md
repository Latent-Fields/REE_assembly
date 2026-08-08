# Project Insights — 2026-08-08

Generated: 2026-08-08T08:57:39Z
Recommendations fixed against: REE_assembly `2047b759a4` (2026-08-08T08:56:00Z governance index rebuild — re-checked `git log --since="2 hours ago"` immediately before finalizing; nothing landed after that commit).

---

## Experiment Health

- **Total classified runs: 281** (PASS: 94 | FAIL: 186 | ERROR: 1 | error rate: **0.36%**, upper bound **2.44%** with 6 phantom completions unclassified) — window: 2026-07-09 to 2026-08-08 (last 30 days), source: coordinator DB (`experiment_error_rate.py --days 30`).
- **Corroborating per-machine split:** 0 ERROR entries recorded fleet-wide in this window (`runner_status/*.json`); `fleet_last_error_recorded` in that split is 2026-06-11 — a slower-refreshing secondary source, not a contradiction of the DB figure above (the frozen monolithic `runner_status.json` was not used, per this skill's forbidden-sources rule).
- **High-iteration experiments (3+ lettered iterations): 58 chains.** The 10 largest (8+ letters), with terminal state and current disposition:
  - **EXQ-603** — 18 iterations (`` through `q`) — SD-059/MECH-358 (escape-affordance-bridge). Terminal: `supports` (603q). Resolved.
  - **EXQ-460** — 15 iterations — SD-034/MECH-260/261 → closure-commit-entry. Terminal: `PASS` (460p). Resolved.
  - **EXQ-485** — 17 manifests across 14 letters — SD-033b/MECH-263 (OFC analog). Terminal: `non_contributory` (485m); **active**, continues via EXQ-696 (2026-06-20/21) and a GAP-8-affordability note as recently as 2026-07-30.
  - **EXQ-543** — 19 manifests across 12 letters — ARC-062/MECH-309. Terminal: `mixed` (543l); **active**, part of the ongoing F-dominance conversion-ceiling campaign, continuing through EXQ-695/714/719/851/847a/863/858/857a (through 2026-08-01).
  - **EXQ-418** — 16 manifests across 11 letters — SD-016. Terminal: `diagnostic` (418m). **Explicitly parked** — substrate_queue.json status `parked_pending_env_entropy_precondition` (z_world cross-context separation not yet satisfied). Not stalled; documented precondition.
  - **EXQ-514** — 11 iterations — MECH-436/SD-049 Phase 2 (drive coupling). Terminal: `supports` (514u). Resolved; substrate_queue text confirms "no longer pending."
  - **EXQ-654** — 10 iterations — ARC-062/MECH-309, F-dominance ceiling cluster. Terminal: `non_contributory` (654j, 2026-07-24); **active** cluster member (see EXQ-689/543 above).
  - **EXQ-689** — 10 iterations — MECH-448/449, F-dominance ceiling cluster. Terminal: `non_contributory` (689j, 2026-07-24); **active** cluster member.
  - **EXQ-569** — 8 iterations — ARC-065 (top-k shortlist conversion). Terminal: `supports` (569i). Resolved — "ceiling_lifted" per substrate_queue.
  - **EXQ-445** — 11 manifests — SD-032b (DACC). Terminal: `weakens` (445h, 2026-05-08); **active**, continues via the `dacc-cluster-862a-870a` autopsy (2026-08-03) through EXQ-870a (2026-08-02).
- **Recurring trouble spots (claim_ids in 2+ ERROR entries):** None in the last 30 days — 0 runner-status ERROR entries recorded fleet-wide in-window.
- **Stalled chains (FAIL with no successor queued): None** — all 10 largest chains were checked for a terminal PASS/supports resolution, an explicit park/precondition, or active continuation; the 3 that lacked an obvious resolution (ARC-062 via EXQ-543, SD-033b via EXQ-485, SD-032b via EXQ-445) each passed the full mandatory liveness check: *ARC-062* — 0 task claims, 5 autopsies (incl. two dated 2026-08-01/08-03), successor manifests through 2026-08-01, 4 commits in the last 14 days. *SD-033b* — 0 task claims, 5 autopsies, successor manifests through 2026-06-21, 1 commit in the last 14 days (2026-07-30). *SD-032b* — 0 task claims, 5 autopsies (incl. `dacc-cluster-862a-870a_2026-08-03`), successor manifest through 2026-08-02.

---

## Substrate Bottlenecks

**Data-quality note before reading this section:** `substrate_queue.json` (146 entries) carries two readiness signals that disagree — a boolean `ready` field (69 true / 77 false) that in practice tracks "has this entry's own validation gate cleared" rather than "buildable now" (most `ready=true` entries are already `implementation_status: implemented`), and a structured `implementation_status` field left unpopulated (`None`) on 83 of 146 entries — including several, like `MECH-342` and `scaffolded_sd054_onboarding`, whose free-text `status` field says they are already implemented and validated. Treat any "ready SD" count below as an upper bound, not a build list, until that field is backfilled against the free-text status (see Recommendation 2).

- **Candidate-buildable-now (no `implementation_status`, no named unresolved dependency): 48 entries** — an upper bound per the caveat above, not a verified list.
- **Blocked (no `implementation_status`, named unresolved dependency): 36 entries**, e.g. `SD-033`/`SD-033c/d/e` (blocked on MECH-094/151/152/235/261/264/265), `SD-026/027/028` (blocked on INV-009/034/037/038, MECH-007/081/089), `cross_stream_binding_substrate` (blocked on the learned-binder substrate, explicitly V4-scoped).
- **Top failure-record counts** (a bottleneck signal independent of the `ready`/`implementation_status` ambiguity above):
  - `scaffolded_sd054_onboarding` — 28 — implemented; readiness flipped true 2026-06-11.
  - `f_dominance_conversion_ceiling` — 26 (the largest in the file) — **not a build gap**: its own status text reads "cross-loop arbitration-reweighting route EXHAUSTED (709/711/713, autopsied 2026-07-05) — no new build owed"; downstream behavioural retests (654h/485i/625e/460h/460i) all self-routed "substrate not ready, requeue." This is the F-dominance conversion-ceiling campaign (see `dual_insights_report.md`).
  - `modulatory-bias-selection-authority` — 15 — implemented, resolved via ARC-065/EXQ-569i.
  - `ARC-062` — 11 — implemented; active validation campaign (see EXQ-543 above), not a build gap.
  - `MECH-256` — 10 — blocked on MECH-269.
  - `v4_loop_segregation` — 10 — implemented; text reads "V3_CLOSURE_REQUIRED... PROMOTES_NOTHING."
  - `SD-049-PHASE-2` — 9 — text corrected 2026-08-07: the pending experiment (EXQ-514u) already ran and PASSed; "no longer pending," residual is downstream governance depth.

---

## Governance State

- Claims pending V3 substrate (`v3_pending: true`): **235** (re-verified after today's governance index rebuild, commit `2047b759a4`).
- Pending promotion/demotion decisions: **2** — `MECH-074d` (`demote_to_candidate`, status `discussing`) and `SD-033e` (`hold_pending_v3_substrate`, status `pending_user`). Both rows are current as of this morning's governance cycle (last touched by commit `4fcd58bb00`, rebuilt into the recommendations doc at `2047b759a4`, 08:56Z today) — this is not aged backlog.
- Evidence superseded (rework): **76** manifests flagged `evidence_direction: "superseded"`.
- `pending_review.md`: **0** items pending (cleared by today's governance cycle, commit `66d0d7a644`).

---

## Literature Coverage

- Priority-1 backlog items still open: **none** (0 of 3 literature-needed backlog items are priority `high`).
- Total open literature items in `evidence_backlog.v1.json`: **3** — MECH-467 (in_progress), MECH-480 (in_progress), Q-019 (covered).
- Covered in recent sessions: 4 new `evidence/literature/targeted_review_*` directories landed today (2026-08-08) — `mech_428`, `mech_471`, `q_091`, `q_090`. Other recent pulls in the last week: claustrum-coalition (2026-08-02), Q-088 (2026-08-02); ARC-005 and the E1 forward-model rollout-consistency review were commissioned (not yet run) as of 2026-08-03/08-05.

---

## Human-Intervention Patterns

- **`/failure-autopsy` sessions always pause at a user-confirmation gate (Step 8)** — every sampled autopsy in the last week (887a/894/892, 866b/873a/890, ARC-017-129-135) required and received explicit user confirmation of the routing/verdict before closing; in the sample, none of these confirmations required a revision — the gate is passing smoothly, not a source of rework.
- **`/governance` cycles require Step 2/3 user decisions on the promotion/demotion queue** — today's cycle logged 16 `pending_user` decisions and closed all but 2 (MECH-074d, SD-033e — see Governance State above) in the same session.
- **Low-friction, headless-safe:** `/lit-pull` and IGW-automated (`igw-auto-*`) sessions completed without a user gate in every sampled instance this window; `/thought-digestion` (trial-2, headless) ran draft-only with 0 direct writes and surfaced systemic findings for later user review rather than blocking on them mid-session.

---

## Recommendations

*Fixed against REE_assembly `2047b759a4` (08:56Z today); re-checked `git log --since="2 hours ago"` immediately before writing this section — nothing landed after that commit.*

1. **Resolve the two open governance decisions.** `MECH-074d` (`demote_to_candidate`, discussing) and `SD-033e` (`hold_pending_v3_substrate`, pending_user) are the entire current decision backlog and both were touched by this morning's cycle — a live, small, well-scoped ask, not aged debt. (Liveness confirmed: both rows still open after the 08:56Z index rebuild; not brake-refused; no autopsy supersedes either recommendation.)
2. **Backfill `substrate_queue.json`'s `implementation_status` field against its own free-text `status` field before using it to prioritize a build.** 83 of 146 entries show `implementation_status: None`, but at least some of the highest-failure-record entries in that same set (e.g. `scaffolded_sd054_onboarding`, and any entry whose free-text status already says "implemented"/"validated") are demonstrably already built — the structured field is silently under-reporting completed work, which would mislead a future `/implement-substrate` prioritization pass that trusts only the structured field. This is a data-hygiene finding, not a substrate-build recommendation.
3. **No literature-coverage action needed this cycle.** 0 open priority-1 items, 2 in-progress items with active recent lit-pulls (4 new reviews landed today) — the backlog looks caught up rather than gapped.

*No experiment or substrate-build recommendation is made from the high-iteration chains in this run* — all 10 largest chains were traced to a terminal resolution, an explicit documented park, or an active, already-owned campaign (see Experiment Health above); none passed the liveness check as genuinely stalled or unowned.
