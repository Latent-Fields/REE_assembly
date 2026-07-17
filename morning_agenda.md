# Morning Agenda — 2026-07-17

Generated: 2026-07-17T04:24:08Z

---

## Headlines — Positive Results & Live Decisions

Comparison window: results terminal since the last digest (2026-07-15T04:25:32Z).

- **V3-EXQ-767a — sd025_curiosity_drive_selection_bias_margin — PASS** (diagnostic, **pending review**)
  - Cloud-authoritative (ree-worker-3, `linux-x86_64-py3.10`). Clean re-operationalization of the vacuous 767: the saturating binary `pref_dense` gate replaced with the continuous CEM score-margin. Non-degenerate this time — `median_margin_on` 39.26 varies across seeds, `margin_off` 0.0, `min_r2_margin` 78.76, weight-independence 0.0. Cross-seed variance guard all True.
  - **Moves:** SD-025 (curiosity_drive) — supports; the drive-mechanism (curiosity biases CEM selection toward higher-density regions, familiarity discount prevents perseveration) is validated at the re-operationalized readout.
  - **Makes live / unblocks:** confirms the SD-025 leg of the SD-024×SD-025 story; the ARC-057 interaction spike **V3-EXQ-768a** (still the sole queue item) is the paired next node.
  - **Gate on acting:** diagnostic PASS — must be adjudicated via `/failure-autopsy` before it can drive SD-025 governance. Not yet reviewed.

- **MECH-423 — PROMOTED candidate → provisional** (V3-EXQ-680e cloud PASS/supports, applied governance cycle 2026-07-16d, REE_assembly `e40362ebb7`)
  - Cross-model super-additivity. Completed the 680b→e corrected-gate campaign: the recalibrated readiness cosine gate (min(cos)≥0 → magnitude-floored band 0.15) unmasked the verdict 680d's false-route had suppressed. All 7 integration-readiness preconditions met; load-bearing `superadditivity_margin_pair` passed.

- **MECH-232 — PROMOTED candidate → provisional** (V3-EXQ-766a cloud PASS/supports, adjudicated + governance 2026-07-16, REE_assembly `46db726a00`)
  - DA-modulated RBF representational expansion. SD-024 cloud-authoritative gate CLOSED (ree-cloud-2, cloud class); autopsy `failure_autopsy_V3-EXQ-766a` verified.

---

## Queue Status
- **Total pending: 1** (Mac: 0 | PC: 0 | EWIN: 0 | any: 0 | ree-cloud-4: 1)
  - `V3-EXQ-768a` — ARC-057 DA×curiosity interaction spike (margin re-op), priority 7, ree-cloud-4
- **ALERT: Queue low — fewer than 3 pending experiments.**
- **Fleet-idle watcher:** `idle_risk=true`, claimable backlog=1 (threshold 3), snapshot 2026-07-17T03:37:05Z. `ready_sd_validation_candidates` is **EMPTY** — `excluded_validation_already_ran=32`, i.e. every built SD's validation has already been queued or run. **Refill needs a fresh `/queue-experiment` design, not a re-queue.** Natural refills on the table: the 767a→SD-025 adjudication continuation, 769→MECH-457 re-route, and 767a/768a follow-ons (see below).
- Owed successors: **none** (all plan-row Owner-EXQs cleared the Step 7c existence cross-check — every candidate has a manifest or a `completed` runner_status entry; nothing is both unqueued and unrun).

---

## Experiments Awaiting Review (2 indexed / 0 runner-only)

### V3-EXQ-769 — mech457_bootstrap_explorer_capacity — FAIL
- **Claims tested:** MECH-457 (status: candidate, v3_pending, epistemic_category: standard)
- **Machine:** ree-cloud-2 (`linux-x86_64-py3.10`, cloud class)
- **Key metrics:** label `bootstrap_explorer_plateaus_capacity_gap_remains`; `non_degenerate: true` (a real, non-vacuous FAIL). Positive controls clear the floor (local-view-greedy 48.05, greedy-oracle 57.2, thr 1.0) — the bootstrap explorer's capacity/reliability/detached-z_world amend did **not** close the competence gap.
- **Classification:** diagnostic (evidence_direction `unknown`) → **needs `/failure-autopsy`**
- **Supersedes:** V3-EXQ-765 (competence bootstrap-explorer, capacity-side amend). This is the latest MECH-457 non-passing autopsy target in the lineage — the re-derive brake is standing; expect the autopsy to REFUSE another same-axis probe and route to a distinct reframe / substrate move.
- **Governance impact:** MECH-457 stays candidate/v3_pending; INV-088 conflict-resolution stays blocked-on-upstream (this was its retest).

### V3-EXQ-767a — sd025_curiosity_drive_selection_bias_margin — PASS
- **Claims tested:** SD-025 (status: candidate, design_decision)
- **Machine:** ree-worker-3 (`linux-x86_64-py3.10`, cloud class)
- **Key metrics:** `median_margin_on` 39.26 / `margin_off` 0.0 / propagation-delta 39.26; anti-perseveration margin 20.05; `min_r1_density_gap` 58.32; `min_r2_margin` 78.76. `criteria_non_degenerate` all True (margin varies across seeds — the vacuous-pass fix held).
- **Classification:** diagnostic → **adjudicate via `/failure-autopsy`** before it drives SD-025 governance (see Headlines).
- **Supersedes:** V3-EXQ-767 (binary `pref_dense` gate, adjudicated vacuous/measurement_degeneracy 2026-07-16d).

---

## Errors to Diagnose (0)

`generate_pending_review.py` reports 0 runner-only / 0 ERROR manifests pending. The 87 historical ERROR entries in `runner_status.json` all have queued or completed successors. Nothing to diagnose.

---

## Governance Agenda (1 recommendation)

- **INV-088** (candidate) — Recommendation: **hold_candidate_resolve_conflict** (`pending_user`)
  - Conflict resolution before promotion. **Blocked-on-upstream:** its retest path ran through MECH-457 bootstrap-explorer; V3-EXQ-769 (the capacity amend) just FAILed, so the conflict is not yet resolvable. Keep candidate; do not force.

**Granularity-debt recurrence (GOV-GRAN-1):** none. (P0 dropped-handoff = 0, P1 unflagged = 0; the reactive autopsy trigger caught everything — 29 claims already metabolized.)

---

## Active Plans Heartbeat (8 plans with status tables)

> Note: none of these plan files carry an explicit `Status: active` frontmatter line; they are surfaced here for visibility. Stale threshold = row `Last updated` before 2026-07-10. **No stale-row Owner-EXQ passed the Step 7c owed cross-check** — all have run or completed. Stale rows are unreconciled prose, not owed work.

| Plan | Phases in-flight | Blocked | Paused | Stale rows |
|---|---|---|---|---|
| arc_062_rule_apprehension_plan | 1 | 1 | 0 | 1 |
| commitment_closure_plan | 3 | 2 | 0 | 10 |
| behavioral_diversity_isolation_plan | 2 | 2 | 0 | 3 |
| goal_pipeline_plan | 1 | 2 | 0 | 2 |
| infant_substrate_plan | 0 | 1 | 0 | 3 |
| self_attribution_plan | 0 | 3 | 0 | 3 |
| ree_ai_design_critique_plan | 0 | 1 | 0 | 0 |
| sleep_substrate_plan | 0 | 1 | 0 | 0 |

Stale rows across these plans reference historical EXQs (543k, 629, 460b, 603n, 591, 567, 589, 590, 490g, 514g, …) — all verified run/completed (490g FAIL, 514g PASS in runner_status; the rest have manifests). These are unreconciled plan prose from April–June, not owed successors. No fresh owed work surfaced.

---

## Literature Pull Candidates (Top 4 with literature need)

| # | Claim | Priority | Existing entries |
|---|-------|----------|-----------------|
| 1 | MECH-232 | medium | 0 |
| 2 | SD-025 | medium | 0 |
| 3 | ARC-057 | medium | 0 |
| 4 | Q-019 | medium | 1 |

(MECH-232 and ARC-057 are the just-promoted / active-spike claims — a `/lit-pull` on either would ground the newly-provisional MECH-232 and the pending ARC-057 interaction node.)

---

## Serve.py Status
- **RUNNING on port 8000** (PID 67391).

---

## Blocked Items
- No TASK_CLAIMS governance collision — governance.sh ran normally.
- REE_assembly required a `git pull --rebase --autostash` at start (3 local igw-ledger bot commits + 2 incoming phase3 commits diverged; rebased cleanly, ~1061 pre-existing derive-noise dirty files left untouched per standing precedent).
- INV-088 governance is blocked-on-upstream (MECH-457 retest 769 FAILed) — see Governance Agenda.
