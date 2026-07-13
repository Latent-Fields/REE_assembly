# Morning Agenda — 2026-07-13

Generated: 2026-07-13T04:24:54Z

_Read-only digest. No governance decisions made, nothing marked reviewed._

---

## Headlines — Positive Results & Live Decisions

No new positive or decision-flipping results since 2026-07-10.

All 5 experiments that ran since the last digest are FAIL. None promote a claim or
make a downstream node/gate decision live. The one interpretively-rich result —
V3-EXQ-742 (MECH-457) `deeper_than_action_learning` — is a `weakens` FAIL, not a
positive; it is surfaced under "Experiments Awaiting Review" below, not here.

---

## Queue Status

- **Total pending: 1** (Mac: 0 | PC: 0 | EWIN: 0 | ree-cloud-4: 1 | any: 0) — **0 claimed**
- **ALERT: Queue effectively empty.** The single pending item is a **baseline mint**,
  not a scientific experiment: `V3-EXQ-742-m` (`v3_exq_742m_mech457_bias_head_baseline_mint.py`,
  priority 5, ree-cloud-4) — the reusable OFF arm (724-A0 all-ON incompetence control) for
  the MECH-457 actor-critic lineage. No hypothesis-testing experiment is queued.
- **Fleet-idle watcher** (snapshot 2026-07-13T04:03:42Z): `idle_risk=true`,
  claimable backlog **1** (threshold 3), `ready_sd_validation_candidates` **EMPTY**.
  Exclusions: `excluded_validation_already_ran=32`, `excluded_no_queueable_validation=17`,
  `excluded_known_churn=3`. An empty candidate list with 32 already-ran means every built
  SD's validation has been attempted — **refill needs a fresh `/queue-experiment` design,
  not a re-queue.** New scientific experiments should be queued today.
- **Owed successors:** none actionable. (Step 7c cross-check: `V3-EXQ-483f` is unqueued with
  no manifest, but its plan row `sd_037_axis_b:P4` is `blocked` on upstream P2/P3 — gated, not
  owed. `V3-EXQ-445h` already ran — manifest 2026-05-08, completed — so not owed.)

---

## Experiments Awaiting Review (5 indexed / 0 runner-only)

### V3-EXQ-742 — mech457_actor_critic_onoff — FAIL (`weakens`)
- **Claims tested:** MECH-457 (candidate, `v3_pending: true`, exp_conf 0.325, lit_conf 0.889,
  quadrant plausible_unproven; prior 4 supporting / 1 weakens / 1 mixed, 0 PASS / 1 FAIL)
- **Interpretation:** `deeper_than_action_learning` — all readiness preconditions **met**
  (D0/D3 greedy-oracle clear the 1.0 floor 6.33/57.2; local-view greedy 6.05/48.05;
  bias-head reproduces incompetence at D0). i.e. the dedicated RPE actor-critic arm did **not**
  recover competence the base substrate lacks — the incompetence sits deeper than action-learning.
- **Classification:** evidence (informative negative — non-degenerate, preconditions met)
- **Governance impact if confirmed:** weakens MECH-457's "dedicated actor-critic is the
  missing action-learning substrate" thesis; keeps it candidate. Worth a `/failure-autopsy`
  read (real WEAKENS, not a starved test).

### V3-EXQ-746a — inv089_harm_eval_z_harm_calibrated_bound_v2 — FAIL (`weakens`)
- **Claims tested:** INV-089 (provisional, exp_conf 0.599, lit_conf 0.0, quadrant speculative;
  1 supporting / 1 weakens, 1 PASS / 1 FAIL)
- **Supersedes:** V3-EXQ-746 (the starved bound — see below). This is the corrected
  state-determined-target run; it extends the V3-EXQ-743 positive control.
- **Classification:** evidence — the core harm_eval↔z_harm quality-bound coupling
- **Governance impact if confirmed:** a genuine `weakens` on INV-089's core coupling; holds
  it at provisional (exp_conf near the 0.62 gate but now with a real opposing entry).

### V3-EXQ-746 — inv089_harm_eval_z_harm_calibrated_bound — FAIL (STARVED / degenerate)
- **Claims tested:** INV-089. `non_degenerate: false`, `evidence_direction: unknown`.
- **Degeneracy reason:** z_harm differentiation gradient did not move (mean IV delta −0.18,
  rank rho −0.15 ≤ 0 — bound test starved, not falsified); state target not decodable from
  mature z_harm (r² −0.196 < 0.05).
- **Note:** superseded by V3-EXQ-746a. Should be scoring-excluded — the FAIL is a test-design
  artefact, not evidence. Handle in `/governance` (set `evidence_direction: superseded` on this
  manifest so it does not weight INV-089).

### V3-EXQ-744a — inv088_world_goal_evaluator_dv_coupling — FAIL (`weakens`)
- **Claims tested:** INV-088 (candidate, exp_conf 0.324, lit_conf 0.0, quadrant speculative;
  **first entry** — 0 supporting / 1 weakens, 0 PASS / 1 FAIL)
- **Classification:** evidence — INV-088 world_goal_evaluator↔z_world differentiation bound
  (the world-side sibling of INV-089's harm-side bound).
- **Governance impact if confirmed:** INV-088's opening evidence is a weakens; keeps it
  candidate with low exp_conf.

### V3-EXQ-745 — rebinding_ecological_patchflip — FAIL (`non_contributory`)
- **Claims tested:** MECH-456 (provisional, `epistemic_category: substrate_conditional`,
  exp_conf 0.824, lit_conf 0.837, quadrant confirmed_established; 6 supporting / 1 mixed, 2 PASS)
- **evidence_direction_note:** readiness gate unmet — unconverged binder / a config never
  visited in P0 / too few overtakes / oracle below the achievability floor / the `couple()`
  path lacks behavioural authority (disabling the binding does not move foraging → a null
  ON-vs-FROZEN DV2 is uninterpretable, the V3-EXQ-478 false-weak trap).
- **Classification:** evidence — but non-contributory (does not move MECH-456's strong record).
- **Governance impact:** none (non_contributory; MECH-456 stays confirmed_established).

---

## Errors to Diagnose (0)

No undiagnosed ERRORs. `pending_review.md` reports 0 runner-only / 0 ERROR manifests, and the
most-recent runner_status ERRORs (V3-EXQ-612/612b/610a/517c/621, all late May 2026) already
have lettered successors or were long since handled.

---

## Governance Agenda (0 recommendations)

No actionable `pending_user` recommendations — all 159 rows in
`promotion_demotion_recommendations.md` are `applied`. (The 5 literal "pending_user" strings in
the file are rationale prose recording claims routed *off* pending_user.)

**Granularity-debt recurrence (GOV-GRAN-1):** P0 dropped-handoff **none** (healthy). P1
unflagged-recurrence — **2 claims** need discrimination (coarse-claim → `/claim-synthesis`
vs coherent substrate-build campaign); **no action taken, no chip:**
- **MECH-180** — 3 hits / 3 signatures — chain: V3-EXQ-677 (novelty_sleep_upregulation),
  V3-EXQ-718 + 718a (sd_mel_consumer cadence validation); autopsies 2026-06-14 / 07-07 / 07-08.
  (MECH-180 noradrenergic error-type→sleep-phase is substrate-blocked on V3 — likely a coherent
  campaign, not coarse-claim, but a human should confirm.)
- **MECH-423** — 3 hits / 2 signatures — chain: V3-EXQ-680b/680c/680d (superadditivity_ablation);
  autopsies 2026-06-14 / 06-15 / 06-15. (Cognifold cross-model super-additivity iteration —
  looks like a 460e..i-style substrate-build campaign, not granularity debt; confirm.)

---

## Active Plans Heartbeat

**Live V3-generation plans** (the working front):

| Plan | In-flight | Blocked | Stale rows | Last updated |
|---|---|---|---|---|
| conversion_ceiling_campaign | 6 | 0 | 0 | 2026-07-10 |
| behavioral_diversity_isolation | 4 | 0 | 0 | 2026-07-10 |
| arc_062_rule_apprehension | 3 | 2 | 4 | 2026-07-10 |
| commitment_closure | 3 | 0 | 2 | 2026-07-10 |
| global_workspace_jlens | 2 | 2 | 0 | 2026-07-10 |
| infant_substrate | 1 | 1 | 2 | 2026-05-30 |
| sd_037_axis_b | 1 | 3 | 3 | 2026-06-05 |
| self_attribution | 0 | 3 | 3 | 2026-06-04 |

**arc_062_rule_apprehension stale rows** (plan itself fresh — rows just unreconciled): GAP-H
(partial, 06-23), GAP-I (blocked_pending_substrate, 06-23), GAP-J (blocked, 05-17), GAP-K
(in-progress, 06-19). No Owner-EXQ on the rows.

**commitment_closure stale rows:** GAP-4 + GAP-4-battery (both in-progress, 06-25). No Owner-EXQ.

**infant_substrate stale rows:** GAP-13 (in_progress, 06-27), GAP-14 (blocked_pending_substrate, 06-23).

**sd_037_axis_b stale rows:** P2/P3 (blocked, 06-05), P4 (blocked, 06-05, Owner-EXQ V3-EXQ-483f —
unqueued but the row is blocked on P2/P3, so gated not owed).

**self_attribution stale rows:** GAP-1 (blocked, Owner-EXQ V3-EXQ-445h — already ran 2026-05-08),
GAP-2/GAP-3 (blocked, Owner TBD).

**PLAN STALING (in-flight rows, plan untouched > 14 days):**
- `infant_substrate` — no plan update since 2026-05-30 (44 days); GAP-13 in_progress.
- `sd_037_axis_b` — no plan update since 2026-06-05 (38 days); 1 row in-flight, P2/P3/P4 blocked.
- `self_attribution` — no plan update since 2026-06-04 (39 days); all rows blocked (Owner TBD).

**Future-generation roadmaps (V4/V5/V6):** ~25 plans, the large majority of their non-done rows
are `blocked` on future-generation substrate that does not yet exist (mostly stamped 2026-06-10..14).
These are generation-segmented roadmaps — blocked-by-design, not actionable staleness. Not expanded
here; see the closure snapshot's per-generation view.

---

## Literature Pull Candidates (Top 3 with literature need)

| # | Claim | Priority | Existing entries |
|---|-------|----------|------------------|
| 1 | INV-089 (harm_evaluator_bounded_by_z_harm_differentiation) | high | 0 |
| 2 | INV-088 (world_goal_evaluator_bounded_by_z_world_differentiation) | medium | 0 |
| 3 | Q-019 (Three-Gate BG Architecture: literature extraction) | medium | 0 |

(Only 3 backlog items list `literature` in `evidence_needed`. INV-088/INV-089 both have
lit_conf 0.0 — a `/lit-pull` on either would give the harm/world evaluator-bound invariants
their first literature anchor.)

---

## Serve.py Status

- **RUNNING** on port 8000 (PID 89993).

---

## Blocked Items

- None. No TASK_CLAIMS collisions (0 active non-digest claims at start); `governance.sh` ran
  clean. Umbrella `REE_assembly` had diverged (3 local igw-ledger automation commits vs 2 phase3
  writer commits + 2 uncommitted inter_governance_workset files) — reconciled with
  `git pull --rebase --autostash` before the pipeline run.
