# Morning Agenda — 2026-07-21

Generated: 2026-07-21T04:22:30Z

---

## Headlines — Positive Results & Live Decisions

Window: since the last digest (2026-07-17T04:24:08Z).

- **V3-EXQ-795 — `sd024_benefit_terrain_live_path_efficacy` — PASS / `supports`** (evidence; **not yet reviewed**)
  - **Moves:** SD-024, SD-025 — all 4 load-bearing criteria pass (L1a benefit centers ON, L2a density ON, L3a live bonus ON, L4a cross-candidate range ON), plus all 4 OFF-arm zero falsifiers.
  - **Makes live / unblocks:** confirms the producer wired 2026-07-20 (`REEAgent.update_z_goal -> ResidueField.accumulate_benefit`) makes the SD-025 curiosity drive **non-zero in a real episode loop**. Between 2026-07-16 and 2026-07-20 `accumulate_benefit` had **no caller** in `ree_core/`, so the curiosity bonus was exactly 0.0 on all 14,432 live calls — the drive contributed nothing to CEM scoring in every live run. Any conclusion about curiosity-drive behaviour drawn from a live run in that window is suspect; conversely, every downstream consumer of the curiosity channel is now actually driven.
  - **Explicitly NOT superseded:** V3-EXQ-766/767/767a remain valid *in-vitro* validations (they populate the terrain themselves) — different question, hence a new number not a letter.
  - **Gate on acting:** none — actionable now. Needs a `/governance` pass to close.

- **V3-EXQ-788 + V3-EXQ-789 (MECH-457 RETENTION leg) — diagnostic, already reviewed**
  - 788 `retention_critic_retains_competence` and 789 `retention_auxiliary_succeeded_then_decayed` both landed; 792 (below) is the third leg and came back **non-discriminative**. The three read jointly.

Already-reviewed `supports` results in the window (closed; listed for continuity, no action):
V3-EXQ-768a (ARC-057, DA x curiosity interaction margin), 775 (MECH-086 selection-gain dose-response),
776 (MECH-279 PAG freeze-gate signature), 773 (MECH-076 residue-basin geometry), 778/778a/778g
(SD-068 SWS readout content-contingent — note the same family also produced `weakens` at 778c/778e/778f),
784 (SD-074 warmup desaturation).

---

## Queue Status
- Total pending: **11** (Mac `DLAPTOP-4.local`: 1 | `ree-cloud-2`: 1 | `ree-cloud-3`: 1 | any: 8) — plus 4 `claimed`.
- Queue is healthy (> 3 pending). No low-queue alert.
- Claimed: 707c (ree-cloud-3, ~17h), 742a (ree-cloud-1, ~22.8h), 734a (ree-cloud-4, ~12.5h), 742m-b (ree-cloud-2, ~4.5h).
- Fleet-idle watcher: `idle_risk=false`, claimable backlog **11** (threshold 3), snapshot 2026-07-21T03:48:23Z.
  `ready_sd_validation_candidates` is **empty**, with 32 excluded as `validation_already_ran` — so if the
  queue does drain, refill needs a fresh `/queue-experiment` design, not a re-queue.
- **Owed successors** (passed all three Step 7c checks — not queued, no manifest, not completed):
  - **V3-EXQ-631** — MECH-342 maintenance-release ecological follow-on. `commitment_closure_plan` lists it
    as "queued (next-wave session)" but it never was. It is the row that clears MECH-342's `v3_pending`.
  - **V3-EXQ-667a** — infant_substrate GAP-14 (c-1) exploration-strength-collapse successor to 667;
    the plan explicitly says "667a not yet queued". EXQ-ISEF-005 stays blocked until it runs.
  - **V3-EXQ-475a** — goal_pipeline GAP-4 Tier-1 StepHarness retest. **Ambiguous**: it *was* queued
    (ree-v3 `4d9cbc0`) and removed by `d1a9443` "queue: remove completed/failed items" on 2026-05-21,
    but produced no manifest and no `runner_status` completion. Treat as owed pending a coordinator-DB
    check, not as a confirmed never-queued item.

---

## Experiments Awaiting Review (3 indexed / 0 runner-only)

### V3-EXQ-795 — `sd024_benefit_terrain_live_path_efficacy` — PASS
- **Claims tested:** SD-024 (design_decision, status: candidate), SD-025 (candidate)
- **Key metrics:** 8/8 criteria pass including all 4 load-bearing; P0 readiness positive control
  cross-candidate range = 13.83 (threshold 1e-06)
- **Classification:** evidence (`supports`)
- **Governance impact if confirmed:** first live-path evidence for the SD-024 benefit terrain ->
  SD-025 curiosity coupling; establishes that pre-2026-07-20 live runs had a dead curiosity channel.

### V3-EXQ-792 — `mech457_retention_consolidation` — FAIL
- **Claims tested:** MECH-457 (candidate, `v3_pending: true`)
- **Key metrics:** `C_anchored_arm_consolidates_installed_competence` PASS,
  `C_unconstrained_control_erodes_installed_competence` PASS,
  `C_anchor_bound_dose_response` **FAIL** -> label `retention_grid_nondiscriminative`
- **Classification:** diagnostic — explicitly excluded from scoring, promotes/demotes nothing
  (`evidence_direction: unknown`). Manipulation is the update constraint only
  (`use_policy_kl_anchor` / `kl_anchor_coef`); the value estimator is untouched.
- **Governance impact:** none directly. Route to `/failure-autopsy`, read **jointly** with the other
  two RETENTION legs — H-retention-critic (788) and H-retention-auxiliary-decay (789).

### V3-EXQ-708a — `mech440_noisy_selection_head_propagation_falsifier` — FAIL
- **Claims tested:** MECH-440 (candidate, `v3_pending: true`)
- **Supersedes:** V3-EXQ-708
- **Result:** `non_contributory`, `non_degenerate: false` — **NOT a falsification.**
- **Unmet preconditions (2):** `temperature_control_raises_precommit_entropy` measured **0.0** vs
  threshold 2.0; `weight_noise_raises_precommit_entropy` measured **1.0** vs threshold 2.0.
  (`enough_divergent_seeds` was met: 4 vs 3.)
- **Self-route:** `substrate_not_ready_requeue` — flagged **`precondition_unmet`** by the indexer.
  The label must NOT drive a governance action until adjudicated via `/failure-autopsy`.
- **Reading:** neither the ARM_TEMP temperature control nor the injected weight noise lifted
  pre-commit sampling entropy on a majority of divergent seeds, so MECH-440's propagation claim
  could not be validly measured. Same non-propagating-floor territory V3-EXQ-687 hit.

---

## Errors to Diagnose (0)

No undiagnosed ERRORs. `pending_review.md` reports 0 runner-only and 0 ERROR manifests.

Caveat: `runner_status.json` is stale under Phase 3 — its 87 ERROR entries all predate 2026-05-31
and are historical. The coordinator DB is the authoritative ERROR-rate source.

---

## Governance Agenda (0 recommendations)

`promotion_demotion_recommendations.md` (regenerated 2026-07-21T04:17:33Z) contains **159 rows, all
`applied`** — zero `pending_user`. Nothing awaits a promotion/demotion decision.

**Granularity-debt recurrence (GOV-GRAN-1): none.** `dropped_handoff` = 0, `unflagged_recurrence` = 0
across 62 claims with hits (26 excluded as already-metabolized / ceiling-lane). Healthy steady state —
the reactive `/failure-autopsy` trigger caught everything. No chip spawned.

**Epistemic-category completeness (GOV-CAT-1): clean** — `missing_category` = 0, `claimless_missing` = 0,
with 10 legacy singular-`claim_id` schema warns (all from `failure_autopsy_V3-EXQ-455a_2026-05-25`,
every one of which DOES carry a category). No backfill needed; steady state holds after the
2026-07-20 backfill.

---

## Fleet Git Health

| Machine | Repo | State | Note |
|---|---|---|---|
| ree-cloud-1 (hub) | REE_assembly / ree-v3 | OK | — |
| ree-cloud-2 | REE_assembly / ree-v3 | OK | 1 stash entry each — inspect before dropping |
| **ree-cloud-3** | **REE_assembly** | **BEHIND** | **62 commits behind upstream**; 2 stash entries |
| ree-cloud-3 | ree-v3 | OK | — |
| **ree-cloud-4** | — | **UNREACHABLE** | ssh connection reset — but `hcloud` shows it **running** |

Two things to look at (do **not** repair from the digest — a wedge needs the preserve-before-reset
procedure; stashes have previously held the only surviving copy of completed-run evidence):

1. **ree-cloud-3 is 62 commits behind on REE_assembly** and currently **holds the claim on
   V3-EXQ-707c** (claimed 2026-07-20T11:21Z, ~17h). Not wedged (no unmerged entries), but it is
   executing against a stale checkout.
2. **ree-cloud-4 is powered ON per `hcloud server list` but refuses ssh** (connection reset), and it
   **holds the claim on V3-EXQ-734a** (claimed 2026-07-20T15:54Z, ~12.5h). Powered-on-but-unreachable
   is not the routine powered-off case — worth a look.

---

## Active Plans Heartbeat (5 active plans with parseable status tables)

| Plan | Phases in-flight | Blocked | Paused | Stale rows | Last decision |
|---|---|---|---|---|---|
| commitment_closure_plan | 3 | 0 | 0 | 3 | 2026-06-03 |
| goal_pipeline_plan | 1 | 2 | 0 | 3 | 2026-06-15 |
| infant_substrate_plan | 3 | 1 | 0 | 4 | 2026-05-21 |
| self_attribution_plan | 0 | 3 | 0 | 3 | 2026-05-30 |
| sleep_substrate_plan | 0 | 1 | 0 | 1 | 2026-07-20 |

(`convergence_demand_pipeline_plan` and `sd033_governance_plan` are `active` but carry no
`## Status table` — nothing parseable to report.)

**commitment_closure_plan stale rows:**
- GAP-1 (Phase 1) — last updated 2026-05-20 — Owner-EXQ V3-EXQ-598 — **ran** (manifests + completed). Row unreconciled.
- GAP-4 (Phase 2/4/5) — 2026-06-03 — Owner-EXQ V3-EXQ-460b..468b — **all ran** (manifests present). Row unreconciled.
- GAP-8 (Phase 7) — 2026-06-03 — Owner-EXQ V3-EXQ-485b/485c — **ran** (completed). Row unreconciled.

**goal_pipeline_plan stale rows:**
- GAP-2 (Phase 2, blocked) — 2026-05-08 — Owner-EXQ V3-EXQ-514g — completed in runner_status; not owed.
- GAP-4 (Phase 4, in-progress) — 2026-05-29 — 490g / 471a / 524a / 603c **ran**; 483c has manifests;
  **475a is the only one with no evidence** (see owed list above).
- GAP-7 (blocked_pending_substrate) — 2026-06-10 — 636 / 637 / 626b / 640a **all ran**. Row unreconciled.

**infant_substrate_plan stale rows:**
- GAP-11 EXQ-ISEF-002 — 2026-05-21 — V3-EXQ-588b **ran**.
- GAP-12 EXQ-ISEF-003 — 2026-05-17 — V3-EXQ-589 **ran**.
- GAP-13 EXQ-ISEF-004 — 2026-05-17 — V3-EXQ-590 **ran**.
- GAP-14 EXQ-ISEF-005 — 2026-06-19 — **V3-EXQ-667a is genuinely owed** (see owed list). Only the
  (c-1) exploration-strength-collapse sub-blocker remains; (b) and (c-2) are cleared.

**self_attribution_plan stale rows:** GAP-1 / GAP-2 / GAP-3 all `blocked` with Owner-EXQ `TBD` — no id
to cross-check; gated on sleep_substrate Phase 1 PASS + MECH-269 V_s, not on an unqueued run.

**sleep_substrate_plan:** GAP-2 `upstream-blocked` — the row's cells are corrupted (prose has leaked
across the pipe delimiters, so the parser reads `>0.05 between WITH/WITHOUT_SLEEP...` as the status and
`diff` as the owner). Worth a manual tidy; nothing is derivable from the row as-is. The plan's decision
log IS current (2026-07-20).

**PLAN STALING:**
- `infant_substrate_plan` — no decisions logged since 2026-05-21 (2 months); 3 rows in-flight + 1 blocked.
- `self_attribution_plan` — no decisions since 2026-05-30; 3 rows blocked.
- `commitment_closure_plan` — no decisions since 2026-06-03; 3 rows in-flight, **all of whose owners have
  in fact run**. This plan needs a **reconciliation pass**, not new experiments.

---

## Literature Pull Candidates

Only **2** items in `evidence_backlog.v1.json` list `literature` in `evidence_needed`, both `medium`:

| # | Claim | Status | Next action | Existing entries |
|---|-------|--------|-------------|-----------------|
| 1 | SD-024 | in_progress | Run paired experiment + literature cycle before status change | 0 |
| 2 | Q-019 | covered | (none — Three-Gate BG Architecture extraction already covered) | 0 |

Note the timing: **SD-024 is the claim V3-EXQ-795 just supported** — the paired-experiment half of that
backlog item has now landed, so the literature half is the remaining piece.

---

## Serve.py Status
- **RUNNING** on port 8000 (PID 27847).

---

## Blocked Items

- No TASK_CLAIMS collisions. `governance.sh` ran in full.
- Three stale claims were present at digest time and treated as cleared per the 6-hour rule (none
  blocked anything): `v3-exq-778e-machine-pinning-04cd10` (60h),
  `claims-explorer-queue-state-223906` (31h), `strange-payne-281125` (8h, MECH-465 stage-2 SD-063
  conditional-gate probe). The 8h one is only just over the line — if that session is still live it
  should be re-opened rather than pruned.
- `sleep_substrate_plan.md` GAP-2 status-table row is malformed (unescaped pipes in prose).
- 15 architecture/top-level docs have no frontmatter and are hidden from the site left-nav
  (governance.sh Step 9 FYI, unchanged from prior runs).
