# Morning Agenda — 2026-05-18

Generated: 2026-05-18T04:23:49Z

---

## Queue Status
- Total pending: **6** (Mac: 0 | PC: 0 | EWIN: 0 | any: 6)
- Queue depth healthy (>= 3). No affinity pins — all `any`.
- 3 of 6 are supersession re-issues: `V3-EXQ-481b` (sup. 481, MECH-090 V_s commit-release), `V3-EXQ-582a` (sup. 582, GAP-3 drive_floor sweep), `V3-EXQ-592` (sup. 461, GAP-11 committed-mode curriculum pilot).
- New work queued: `V3-EXQ-584` (GAP-7 traj cosine substrate-readiness), `V3-EXQ-586` (GAP-9 infant curriculum scheduler), `V3-EXQ-591` (EXQ-ISEF-005 4-phase infant curriculum vs flat baseline).

---

## Experiments Awaiting Review (5 indexed / 1 runner-only)

All 5 indexed pending entries belong to a single supersession chain testing the
same two claims: **ARC-062** and **MECH-309**. Chain: EXQ-543e → 543f → 543g
(543g supersedes 543f; 543f supersedes 543e).

### V3-EXQ-543f — `v3_exq_543f_arc062_onehot_dacc_falsifier` — FAIL (4 runs)
Run IDs: `…20260517T125958Z_v3`, `…T130046Z_v3`, `…T130300Z_v3`, `…T140320Z_v3`
- **Claims tested:** ARC-062 (candidate, architectural_commitment, epistemic_category `substrate_conditional`, **v3_pending**, no prior indexed evidence) · MECH-309 (candidate, mechanism_hypothesis, **v3_pending**, no prior indexed evidence)
- **Evidence direction:** overall `non_contributory`; per-claim → ARC-062 `weakens`, MECH-309 `non_contributory`
- **What it is:** MECH-309 monomodal-collapse falsifier re-issue on the ARC-062 one-hot dACC head-augmentation substrate. Applies two fixes from the 543e dual-root-cause autopsy (one-hot action augmentation bypassing E2 first-action compression; dacc_weight=1.0). `supersedes: V3-EXQ-543e`.
- **Classification:** diagnostic / falsifier (not a direct evidence experiment).
- **Governance impact if confirmed:** none automatic — ARC-062 and MECH-309 are both `v3_pending`, so governance already holds them at `hold_pending_v3_substrate`. The MECH-309 `non_contributory` direction means this needs `/diagnose-errors`-style triage interpretation, **not** force-mapping to weakens (see memory: non-standard directions). Superseded by 543g — its evidence should not weight scoring.

### V3-EXQ-543g — `v3_exq_543g_arc062_outcome_coupled_falsifier` — FAIL (1 run)
Run ID: `…20260517T144716Z_v3`
- **Claims tested:** ARC-062, MECH-309 (same as above)
- **Evidence direction:** overall `weakens`; per-claim → ARC-062 `weakens`, MECH-309 `non_contributory`
- **What it is:** Same falsifier with the P1 diversification regularizer replaced by REINFORCE on GatedPolicy params (advantage = ep_return − EMA baseline). Inherits both 543f substrate fixes. `supersedes: V3-EXQ-543f`.
- **Classification:** diagnostic / falsifier (head of the chain — the live iteration).
- **Governance impact if confirmed:** ARC-062 `weakens` on a deliberate falsifier is expected falsification-attempt semantics, not an auto-demotion trigger; the `v3_pending` gate holds ARC-062 regardless. Needs human interpretation of whether the falsifier landed (monomodal collapse persisted) or the substrate fix is still incomplete. **Supersedes 543f → the 4× 543f runs should be marked `evidence_direction: superseded` on review so they drop out of scoring.**

### Runner-only (1 — needs discussion, not researched here)
- `V3-EXQ-585` — result PASS — script `?` — flagged "index stale" in pending_review.md even though the index was just rebuilt; the PASS manifest is not landing in indexable form. Route to `/diagnose-errors` / manual manifest check, then add to `discussed_experiment_dirs`.

---

## Errors to Diagnose (12 scientific + 2 onboarding smokes)

ERRORs in `runner_status.json` with no queued fix and no PASS/FAIL successor of the same EXQ base:

- **V3-EXQ-263** — MECH-216 E1 predictive wanting schema readout validation — exit 1
- **V3-EXQ-476** — MECH-269 V_s validation entropy probe (cascade gate) — exit 1
- **V3-EXQ-385a** — INV-049 offline consolidation necessity: SHY decay rate fix — exit 1 (EWIN-PC)
- **V3-EXQ-250a** — INV-054 Phase-Transition Recovery (SD-018) — exit 1 (ree-cloud-1)
- **V3-EXQ-244a** — MECH-165 reverse-replay diversity scheduler validation — exit -15 (killed, ree-cloud-2)
- **V3-EXQ-445d** — SD-032b dACC full pipeline, V_s-enabled re-run — exit 1
- **V3-EXQ-455a** — SD-032a salience coordinator behavioural, V_s-enabled re-run — exit 1
- **V3-EXQ-449c** — MECH-074b BLA retrieval bias on action selection, V_s-gated — exit 1
- **V3-EXQ-495** — MECH-163 V3 full-completion gate (VTA / hippocampal arm) — exit -15 (killed after ~4 h, ree-cloud-1)
- **V3-EXQ-538** — SD-049 Phase 2 reef behavioural validation, sleep-on ablation — exit -15 (killed, ree-cloud-1)
- **V3-EXQ-542** — ARC-062 Phase 1 gated-policy substrate-readiness diagnostic — no runner sentinel (exit 0; wrote a JSON output_file — possible UNKNOWN silent-drop)
- **V3-EXQ-544** — MECH-313 (ARC-065) stochastic_noise_floor substrate-readiness diagnostic — no runner sentinel (exit 0; wrote a JSON output_file — possible UNKNOWN silent-drop)

Onboarding smokes (not scientific — machine onboarding, separate handling):
- `V3-ONBOARD-smoke-EWIN-PC`, `V3-ONBOARD-smoke-ree-cloud-1`

> Note: heuristic cross-ref (runner_status has no experiment_type/claim fields for most). 542/544 look like the UNKNOWN-result silent-drop pattern (`experiment_runner.py:1394`) — check `evidence/` for their manifests before treating as lost.

---

## Governance Agenda (1 recommendation)

- **MECH-332** (`candidate`) — Recommendation: **hold** (`hold_pending_v3_substrate`)
  - Evidence: 1 supporting, 0 opposing, 0 mixed (conflict_ratio 0)
  - Flagged `v3_pending` (explicit manual gate) — no promotion/demotion until the flag clears.
  - This is the **only** `pending_user` item; all other ~110 Decision Queue rows are `applied`.

---

## Active Plans Heartbeat (7 plans)

| Plan | Front-matter status | Phases in-flight | Blocked | Paused | Stale rows | Last decision |
|---|---|---|---|---|---|---|
| arc_062_rule_apprehension_plan | done | 6 | 1 | 0 | 3 | 2026-05-17 |
| commitment_closure_plan | in-progress | 1 | 1 | 0 | 2 | 2026-05-17 |
| goal_pipeline_plan | done | 1 | 2 | 0 | 2 | 2026-05-17 |
| infant_substrate_plan | done | 1 | 0 | 0 | 0 | 2026-05-17 |
| sd033_governance_plan | done | 0 | 0 | 0 | 0 | — |
| self_attribution_plan | blocked | 0 | 3 | 0 | 2 | 2026-05-17 |
| sleep_substrate_plan | done | 0 | 1 | 0 | 1 | 2026-05-17 |

**Discrepancy flag:** `arc_062_rule_apprehension_plan` front-matter says `done` but its
status table still has **6 in-flight + 1 blocked + 3 stale** rows — and today's 5 pending
FAILs (ARC-062 / MECH-309 falsifier chain 543f/543g) are exactly this plan's subject.
The plan is not actually closed. Same pattern (status `done` with live/blocked rows) on
`goal_pipeline_plan` and `sleep_substrate_plan`.

**arc_062_rule_apprehension_plan stale rows:**
- GAP-G — open — last updated 2026-05-09
- GAP-I — blocked — last updated 2026-05-10
- GAP-K — in-progress — last updated 2026-05-10

**commitment_closure_plan stale rows:**
- GAP-4 — last updated 2026-05-08
- GAP-8 — blocked — last updated 2026-05-08

**goal_pipeline_plan stale rows:**
- GAP-2 — blocked — last updated 2026-05-08
- GAP-4 — blocked — last updated 2026-05-08

**self_attribution_plan stale rows (plan status = blocked):**
- GAP-2 — blocked — last updated 2026-05-08
- GAP-3 — blocked — last updated 2026-05-08

**sleep_substrate_plan stale rows:**
- GAP-2 — blocked — last updated 2026-05-09

---

## Literature Pull Candidates (Top 5)

Only 1 backlog item has `evidence_needed: literature`:

| # | Claim | Subject | Priority | Existing entries |
|---|-------|---------|----------|-----------------|
| 1 | Q-019 | Three-Gate BG Architecture: Literature Extraction | medium | ~1 (`targeted_review_*` dir present) |

---

## Serve.py Status
- **RUNNING** on port 8000 (PID 22000, LISTEN).

---

## Blocked Items
- **None** — no `TASK_CLAIMS.json` collision; `governance.sh` ran in full.
- **Note (non-blocking):** `governance.sh` exited 1 due to the pre-existing backward-traceability G2 gate — 117 developmental claims lack a `developmental_needs_register.md` row reference. This is informational and fires *after* the core pipeline; index rebuild (1093 runs, FAIL=630, lit=1441), `pending_review.md`, `promotion_demotion_recommendations.md`, and `claims.json` (645 claims) all completed and are fresh as of this run.
- **Note (reconciliation):** REE_assembly diverged 342 behind / 173 ahead of origin/master at pull time — verified **100% per-machine heartbeat commits, zero real commits on either side** (local DLAPTOP-4 vs cloud-worker heartbeats touching disjoint files). Reconciled non-destructively via merge (autostash). ree-v3 was already up to date.
