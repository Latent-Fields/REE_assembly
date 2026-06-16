# Morning Agenda — 2026-06-16

Generated: 2026-06-16T04:23:27Z

> Read-only digest. No governance decisions made, nothing marked reviewed.

---

## Queue Status
- **Total pending: 0** (Mac: 0 | PC: 0 | EWIN: 0 | any: 0)
- **ALERT: Queue empty — 0 pending experiments.** Coordinator DB confirms 0 active (pending/claimed/running). The full overnight cohort drained: 684a (PASS), 514q (FAIL), and the 654c / 680d / 591f / 685 / 686 batch all cleared the queue. **Queue needs replenishing today** — several routed follow-ons are ready to author (see below).
- Fleet is idle. The two pending reviews below are the gating decisions; once adjudicated, their routed successors (notably GAP-A 569h, now unblocked by 684a) are the natural refill.

---

## Experiments Awaiting Review (2 indexed / 0 runner-only)

### V3-EXQ-684a — modulatory_conversion_readiness — PASS
- **Claims tested:** none (claim-free diagnostic; supersedes V3-EXQ-684)
- **Key metrics:** label `conversion_mechanism_identified`. Winning arm **ARM_STD_G2** (std basis, gain=2): committed selected-action entropy **0.989** vs ARM_LEGACY_E2WF 0.775 vs ARM_PROPOSER/MATCHED_NOISE 0.549. Route-range 0.427 (STD_G2) vs 0.187 (legacy). Readiness OK (route ready 3/3, e2-divergence 3/3, metric-can-move 2/2); negative control (matched noise) did **not** lift (0/3) — clean.
- **Classification:** diagnostic
- **Governance impact if confirmed:** This is the gate that **unblocks behavioral_diversity_isolation:GAP-A 569h** — the conversion mechanism is identified (gain/contrast amend, std basis, gain=2 carries the per-candidate range into the committed argmax). Per the GAP-A plan, 569h is GATED on exactly this readiness PASS. Confirming 684a clears that gate; the winning STD_G2 config selects 569h. Also feeds the shared CONVERSION-ceiling off-ramp used by arc_062:GAP-B (654c) and self_attribution:GAP-2.
- **Supersedes:** V3-EXQ-684 (mis-designed positive control)

### V3-EXQ-514q — sd049_phase2_mech229_drive_coupled_wanting_liking — FAIL
- **Claims tested:** MECH-229 (status: **provisional**, exp_conf **0.807**, lit_conf 0.844, quadrant `confirmed_established`, prior evidence: 10 supporting / 2 mixed / 2 weakens of 14 entries)
- **Key metrics:** non_degenerate=True. Preconditions PASSED — positive control separates (1.0), bank populated (1.0), raw-dissociation non-vacuity 0.702 > 0.30. Load-bearing **C_WL_DRIVE_coupled_dissociation FAILED**. Label: `drive_delta_below_effect_size_genuine_weakens_run_offarm_overshoot` — the drive-coupled dissociation delta fell below the SD-of-delta + FLOOR effect-size margin.
- **Classification:** evidence
- **Governance impact if confirmed:** A **genuine (non-degenerate) weakens** on MECH-229 under the corrected load-bearing criterion (514q made the drive-coupled delta load-bearing per the 514p autopsy; supersedes 514p). MECH-229 already carries `pending_retest_after_substrate: true` and `narrow_supports_flag: true` — this FAIL is the retest landing on the weakens side. The interpretation flags an off-arm overshoot route. **Needs `/failure-autopsy`** before it drives any demotion — do not demote MECH-229 on this alone (mechanism not refuted; the question is whether the drive-coupling effect-size gate is the right test or whether off-arm overshoot contaminated the delta). Prior governance had flagged goal_pipeline GAP-2/GAP-7 closures as resting on the 514o PASS that 514q's lineage re-examines.

---

## Errors to Diagnose (10 with no completed successor)

Queue is empty, so none have a queued fix. Most are legacy carryover; flagged for `/diagnose-errors` if still relevant:

- **V3-EXQ-606a** — ERROR — no successor (most recent; likely real)
- **V3-EXQ-538** — ERROR — no successor
- **V3-EXQ-517c** — ERROR — no successor
- **V3-EXQ-495** — ERROR — no successor
- **V3-EXQ-455a** — ERROR — no successor
- **V3-EXQ-449c** — ERROR — no successor
- **V3-EXQ-244a** — ERROR — no successor
- **V3-EXQ-008** — ERROR — no successor (legacy)
- **V3-ONBOARD-smoke-EWIN-PC** / **V3-ONBOARD-smoke-ree-cloud-1** — onboarding smoke ERRORs (infra, not scientific)

(87 ERRORs total in runner_status; the 77 not listed have a lettered successor already run.)

---

## Governance Agenda (13 pending_user — 2 actionable, 11 routine holds)

**Actionable:**
- **MECH-057b** (`candidate`) — Recommendation: **hold_candidate_resolve_conflict** (conflict resolution before promotion). Prior decision exists but recommendation changed — needs fresh review. First genuine non-degenerate weakens landed via 672b (exp_conf ~0.325); conflict-hold stands.
- **Q-054** (`open`) — Recommendation: **narrow_open_question**.

**Routine V3-substrate holds** (`hold_pending_v3_substrate` — not actionable until substrate built): ARC-088, ARC-096, ARC-097, INV-081, INV-082, MECH-129, MECH-180, MECH-217, MECH-339, MECH-340, MECH-411.

---

## Active Plans Heartbeat

Only plans with non-zero in-flight/blocked/stale rows shown (the V4/V5/v6 forward-roadmap plans are all clean/quiescent; behavioral_diversity_isolation & arc_062_rule_apprehension use closure-node format and were actively reconciled 2026-06-15 — see TASK_CLAIMS).

| Plan | Phases in-flight | Blocked | Paused | Stale rows | Last decision |
|---|---|---|---|---|---|
| commitment_closure_plan | 3 | 0 | 0 | 3 | 2026-06-03 |
| goal_pipeline_plan | 1 | 1 | 0 | 2 | 2026-06-15 |
| self_attribution_plan | 0 | 3 | 0 | 3 | 2026-05-30 |

**commitment_closure_plan stale rows:**
- GAP-1 (in-progress) — Last updated 2026-05-20 — Next: V3-EXQ-598 (2-arm frozen vs trainable bias head); closes on 598 PASS. *(598 is in the undiagnosed-ERROR list — likely the blocker.)*
- GAP-4 (in-progress) — Last updated 2026-06-03 — Next: Phase 4/5 *b cohort (460b/461b/463b/464b/466b/467b/468b); closes when the *b cohort PASSes.
- GAP-8 (in-progress) — Last updated 2026-06-03 — Next: on 485b/485c PASS → GAP-8 PARTIAL (full needs trained-OFC-head behavioural arm).

**goal_pipeline_plan stale rows:**
- GAP-2 (blocked) — Last updated 2026-05-08 — Next: re-queue V3-EXQ-514 successor under MECH-307-fixed substrate. *(514q just landed FAIL — this row's lineage is live again; reconcile after the 514q autopsy.)*
- GAP-4 (in-progress) — Last updated 2026-05-29 — Next: two-fork disposition per the 490g-cohort autopsy.

**self_attribution_plan stale rows:**
- GAP-1 (blocked) — Last updated 2026-05-30 — Next: after upstream gates close, fresh 3-arm ARC-033 vs ARC-058 ablation.
- GAP-2 (blocked) — Last updated 2026-05-08 — Next: re-queue SD-029/MECH-256 retest with full substrate stack. *(684a PASS unblocks the shared conversion gate this depends on.)*
- GAP-3 (blocked) — Last updated 2026-05-08 — Next: after Phase 2 PASS, re-queue MECH-257 dual-function 3-arm ablation.

**PLAN STALING:** `self_attribution_plan` — no decisions logged since 2026-05-30 (17 days); 3 rows blocked on upstream gates. The 684a conversion PASS may now unblock GAP-2's upstream dependency — worth a reconcile pass.

---

## Literature Pull Candidates (Top 5)

| # | Claim | Next action | Priority | Existing entries |
|---|-------|-------------|----------|-----------------|
| 1 | MECH-346 | Paired experiment + literature cycle (insufficient_experimental_replication) | medium | 0 |
| 2 | MECH-347 | Paired experiment + literature cycle (insufficient_experimental_replication) | medium | 0 |
| 3 | Q-019 | (open question, no evidence) | medium | 0 |
| 4 | SD-057 | Paired experiment + literature cycle (insufficient_experimental_replication) | medium | 0 |
| 5 | Q-055 | Paired experiment + literature cycle (no_evidence_for_open_question) | low | 0 |

(24 lit-needing backlog items total; none have an existing targeted_review directory.)

---

## Serve.py Status
- **RUNNING on port 8000** (PID 1670).

---

## Blocked Items
- None. No TASK_CLAIMS governance collision — 0 active non-stale claims at digest start, so governance.sh ran fully.
- Note: REE_assembly was ahead 4 / behind 7 at pull time (4 local igw-ledger commits); rebased cleanly with autostash (concurrent IGW `inter_governance_workset.*` edits preserved untouched). Those 4 igw-ledger commits will land with this digest's push.

---

## Suggested First Moves (digest's read — not decisions)
1. **`/governance`** to walk the 2 pending reviews: confirm 684a PASS (clears GAP-A 569h gate) and adjudicate 514q FAIL.
2. **`/failure-autopsy V3-EXQ-514q`** — the genuine MECH-229 weakens needs adjudication before any demotion; check off-arm-overshoot contamination.
3. **Refill the empty queue** — 569h (GAP-A falsifier, now unblocked by 684a) is the highest-leverage author; plus the self_attribution GAP-2 reconcile that 684a may unblock.
