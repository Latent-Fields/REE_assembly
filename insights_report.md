# Project Insights — 2026-07-26

Generated: 2026-07-26T13:20:01Z
Recommendations fixed as of: 2026-07-26T13:19:22Z (re-checked `git log --since="2 hours ago"` on REE_assembly immediately before writing Recommendations — see note below)

---

## Experiment Health

- **Total runs:** 190 classified (PASS: 62 | FAIL: 128 | ERROR: 0 | error rate: 0.0%) — window: last 30 days, source: coordinator DB (`experiment_error_rate.py --days 30`).
  Phantom completions (marked `completed`, no results row) = 6, giving interval **error rate: 0.0%–3.06% (0 recorded ERROR / 190 classified; 6 phantom completions unclassified)**. Quote the interval, not the point estimate.
- **Last ERROR recorded fleet-wide:** 2026-06-11 (`fleet_last_error_recorded`, per the per-machine `runner_status/` split — 45 days stale relative to today, consistent with a currently low-crash fleet).
- **Per-machine activity (last 30d):** ree-cloud-2 (59), ree-worker-1/hub (36), ree-cloud-4 (28), ree-cloud-1 (24), ree-worker-3 (23), ree-cloud-3 (9), DLAPTOP-5 (6), DLAPTOP-4 (5).
- **High-iteration experiments** (3+ lettered iterations, counted from unique manifest-directory letters, not raw manifest files):
  - V3-EXQ-603 — 18 lettered iterations (a–q+) — claims: MECH-358/SD-059 (Stage-H harm-pathway / escape-affordance-bridge cluster)
  - V3-EXQ-514 — 17 iterations — claims: SD-049, SD-015, MECH-229, MECH-230, MECH-307, MECH-436 (wanting/liking behavioural validation)
  - V3-EXQ-460 — 16 iterations — claims: SD-034, MECH-260, MECH-261 (closure control plane / decommit)
  - V3-EXQ-485 — 14 iterations — claim: SD-033b (OFC-analog devaluation)
  - V3-EXQ-085 — 14 iterations — claims: MECH-071 → SD-015 → ARC-030 (claim_ids drift across the chain — documented, not an error)
  - V3-EXQ-543 — 12 iterations — claim: ARC-062 (mode-separation falsifier)
  - V3-EXQ-047 — 12 iterations — claims: SD-005, MECH-095 (agency-routing / TPJ)
- **Recurring trouble spots** (claim_ids in 2+ FAIL/ERROR entries, cross-referenced with substrate-queue `failure_record` counts, Step 4): `scaffolded_sd054_onboarding` (28 failure-record entries), `f_dominance_conversion_ceiling` (26), `modulatory-bias-selection-authority` (15), `ARC-062` (11), `MECH-256` (10), `v4_loop_segregation` (10), `SD-049-PHASE-2` (9). These are pre-existing, actively-tracked ceiling nodes (MECH-457 competence-floor campaign, F-dominance conversion-ceiling campaign) — not silent recurrences.
- **Stalled chains** — liveness check executed per the mandatory Step-2 protocol for every chain above:
  - **None.** All seven high-iteration chains cleared at least one of the four liveness legs:
    - V3-EXQ-603 (MECH-358/SD-059): autopsy hit (`failure_autopsy_V3-EXQ-603p_2026-06-15.md` + others in the same cluster).
    - V3-EXQ-514 (SD-049 family): **actively adjudicated in the last hour** — `failure_autopsy_batch-793a-817-819_2026-07-26` (committed `05e8543300`, 12:38Z today) closed V3-EXQ-793a as `inconclusive/standard`, routing = governance record-finding, no re-queue. Not stalled; currently owned.
    - V3-EXQ-460 (SD-034): landed and validated per prior session record (`460o/460p` closure-commit-entry BUILT+VALIDATED).
    - V3-EXQ-485 (SD-033b): SD-033e successor built; validation co-blocked on V3-EXQ-724 (documented blocker, not abandonment).
    - V3-EXQ-085 (MECH-071→SD-015): migrated to a new EXQ ladder (622/626) under the corrected claim, per the canonical documented case.
    - V3-EXQ-543 (ARC-062): autopsy hits present (`failure_autopsy_gapA-cluster-604b-648a-649_2026-06-07.json`, `failure_autopsy_f-dominance-conversion-cluster_2026-06-20.json`).
    - V3-EXQ-047 (SD-005/MECH-095): autopsy hits present (`failure_autopsy_batch9_2026-06-12`); chain reached a `supports` at 047k before continuing to 047l/047m (`non_contributory`/`mixed`).

---

## Substrate Bottlenecks

- **Ready SDs (precondition-met AND not yet built):** **0.** All 55 substrate-queue entries with `ready: true` already carry `implementation_status: implemented` (or an equivalent landed/validated status) — there is currently no substrate that is unblocked and simply waiting to be built. The buildable backlog has been cleared; everything remaining is either landed or genuinely blocked.
- **Blocked SDs** (`ready: false` with `depends_on_unresolved` populated): 69 of 124 queue entries. Representative examples: `SD-025` (deps ARC-057, MECH-111, INV-051), `SD-033c/d/e` (deps SD-033, ARC-035, MECH-151/152/235/261/264/265), `escape-affordance-bridge` (deps SD-058, MECH-357, MECH-279, SD-011), `v4_loop_segregation` (deps ARC-109, MECH-452, MECH-451), `mech457_competence_bootstrap_explorer` (dep MECH-229).
- **SDs with failure records** (experiments failed against this substrate node), ranked: `scaffolded_sd054_onboarding` (28), `f_dominance_conversion_ceiling` (26), `modulatory-bias-selection-authority` (15), `ARC-062` (11), `MECH-256` (10), `v4_loop_segregation` (10), `SD-049-PHASE-2` (9), `ARC-065` (8), `commitment-closure-control-plane` (7), `SD-037` (6). These are dominated by the two known root-cause campaigns already tracked in memory (F-dominance conversion ceiling, MECH-457 competence floor) — high FAIL volume here is a symptom of active, multi-session probing of a known-hard node, not an unowned defect.

---

## Governance State

- Claims pending V3 substrate (`v3_pending: true`): **225**.
- Pending promotion/demotion decisions (`decision_status` not `applied` in `promotion_demotion_recommendations.md`, 3241-line file, last generated 2026-07-26T06:10:24Z): **0** — every decision row in the current file reads `applied`.
- Evidence marked `superseded` across flat manifests: **321** (rework/correction volume — consistent with the EXQ-lettering supersession policy, not necessarily a defect).
- `pending_review.md` (generated 2026-07-26T11:21:11Z, last review 2026-07-26T00:07:00Z): **7 items** — 5 FAIL, 1 runner-only, 1 diagnostic self-route flagged. **Flag to user per skill Step 6:** all 5 FAILs (793a, 816, 817, 819, 820) already have autopsy coverage as of 12:38Z today (either the direct `failure_autopsy_batch-793a-817-819_2026-07-26` or the earlier same-day `failure_autopsy_816-820-policy-decomposition-cluster_2026-07-26`) — governance's own mark-reviewed step (Step 5) simply hasn't run since. No unowned FAILs are sitting in the backlog.

---

## Literature Coverage

- Backlog items (`evidence_backlog.v1.json`) needing literature evidence: **5** total (MECH-324 in_progress, SD-078 open, SD-079 open, SD-080 in_progress, Q-019 covered/pinned).
- Priority-1 backlog items still open: **0**. (SD-078/SD-079 are both `medium` priority.)
- `evidence/literature/` directory: **411** targeted-review entries on disk.
- Covered in recent sessions (from WORKSPACE_STATE, last ~5 days): Q-083 + Q-084 (2026-07-25 scheduled lit-pull, `targeted_review_q_083` + `targeted_review_q_084`, both lit_conf raised, both flagged `substrate_conditional`/v4/DO NOT BUILD); ARC-112 + Q-081 + INV-091 + MECH-466 (2026-07-22, search 10 of a 10-search programme, closed).

---

## Human-Intervention Patterns

- **Governance cycles requiring an interactive decision pause**: the 2026-07-24 governance cycle explicitly deferred Step 3 (promotion/demotion `pending_user` agenda) as "large pre-existing backlog" — but the *current* recommendations file shows 0 pending, meaning a later cycle cleared it without a further flagged pause.
- **Concurrency/worktree friction dominates recent session overhead, not scientific ambiguity**: of the ~12 WORKSPACE_STATE entries reviewed in the last 6 days, the majority describe navigating diverged/dirty shared checkouts via throwaway worktrees (2026-07-22 claim-synthesis, 2026-07-22 Q-081 build, 2026-07-24 governance cycle, 2026-07-24 two worktree-blindness fixes, 2026-07-24 SD-081 build) rather than requiring a human science call. This is infrastructure-driven friction (many parallel sessions on a shared trunk), not a substrate/design ambiguity pattern.
- **Low-friction headless tasks:** scheduled `/lit-pull` runs (2026-07-25 AM) and `/failure-autopsy` batches (2026-07-26, this morning) both completed and landed without any recorded pause.
- **Recurring infra defect class worth naming (not new — already chipped per its own entries):** "worktree-blindness" — code that hardcodes `parents[2]` or a sibling-directory assumption to locate `REE_assembly`/`ree-v3` from a script's own path, which breaks under `.claude/worktrees/<slug>/` nesting. Hit and fixed 4 times in one day (2026-07-24: `test_arm_reuse.py`, `pack_writer.py`, plus two infra scripts referenced in the same entries). No further instance found in this pass; not re-flagging beyond noting the pattern.

---

## Recommendations

**Gate check result: no recommendation survives all four gates.** Specifically:

1. The two most obvious candidate actions from Step 3 — re-running V3-EXQ-817/819 with corrected objectives/gates — are **already queued and claimed** (`V3-EXQ-817a`, `V3-EXQ-819a`, both `status: claimed` in the live queue as of this run). Recommending them would be redundant.
2. No substrate node is `ready` (precondition-met) and unbuilt (Substrate Bottlenecks, above) — there is nothing to recommend building right now that isn't already blocked on an unresolved dependency.
3. `pending_review.md`'s 5 FAILs all have same-day autopsy coverage; the only remaining action is governance's own review-tracker mark-as-reviewed step, which is `/governance` work and out of scope for a recommendation here per the skill's own exclusion.
4. No priority-1 literature gap is open.

Stating this as the finding rather than manufacturing a plausible-sounding action: **the project is in a genuinely clean, fully-routed state at this snapshot** — every FAIL has an owner, every buildable substrate node has been built, and the queue's own re-tests (817a/819a) already reflect this morning's autopsy findings. The one open thread worth naming without recommending action on it: the **693b guard-fragility design note** from the 793a autopsy (goal-latching-at-contact fragility on hard seeds, SD-049) is explicitly *not* queued by the autopsy's own routing (to avoid circling SD-049's ceiling) — correctly left as a design note, not a gap.
