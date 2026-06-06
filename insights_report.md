# Project Insights — 2026-06-06

Generated: 2026-06-06T07:35:04Z

---

## Experiment Health

- **Total runs:** 808 (PASS: 260 | FAIL: 428 | ERROR: 87 | UNKNOWN: 32 | INCONCLUSIVE: 1 | error rate: 10.8%)
- PASS:FAIL ratio ~0.61 — FAIL-dominant, consistent with a falsification-heavy substrate-probing regime, not broken instrumentation.

- **High-iteration experiments** (3+ lettered iterations — repeated diagnose/redesign cycles):
  - **EXQ-085 — 14 iterations** (085…085o) — all FAIL. ⚠️ *Claim drift:* tagged MECH-071 on the first run only; the remaining letters dropped to goal-navigation (SD-015 / ARC-030). Do NOT read 14 FAILs as evidence against MECH-071. Migrated to a fresh number under SD-015 (622/626 ladder).
  - **EXQ-418 — 13 iterations** (418…418l) — SD-016 / SD-017 (ContextMemory + sleep aggregation). Mixed: 8 FAIL, 1 PASS, 2 ERROR, 2 UNKNOWN. SD-016 is parked (`env_entropy_precondition` unmet).
  - **EXQ-514 — 13 iterations** (514…514l) — SD-049 multi-resource heterogeneity. 9 FAIL, 3 PASS, 1 ERROR. Phase-1/2/3 substrate now landed.
  - **EXQ-543 — 10 iterations** (543…543k) — ARC-062 rule-apprehension / MECH-309. 9 FAIL, 1 PASS. ARC-062 is `phase_1_implemented_evidence_gated_543k_598`.
  - **EXQ-047 — 9 iterations** — SD-005 / MECH-095. 8 FAIL, 1 PASS.
  - **EXQ-445 — 9 iterations** — claims untagged (`?`). 7 FAIL, 1 ERROR, 1 UNKNOWN — untagged + erroring = weakest-attributed chain.
  - **EXQ-490 — 9 iterations** — Q-040 factorial / MECH-269b vs MECH-295 (catatonic-lock diagnostic). 8 FAIL, 1 UNKNOWN.
  - **EXQ-433 — 7 iterations** — SD-029. All 7 FAIL, all reclassified non_contributory (monostrategy can't generate balanced agent-vs-env distributions). Gated on MECH-269 V_s.
  - **EXQ-540 — 7 iterations** — MECH-307 anticipatory affect. 4 FAIL, 2 PASS, 1 ERROR.
  - Also: EXQ-166 (6), EXQ-325 (6), EXQ-074/076 (6 each, MECH-112/116), EXQ-592 (5, MECH-090), EXQ-603 (5, Q-045), EXQ-610 (5, INV-074 — still live, 610f in queue).

- **Recurring trouble spots** (claim_ids in 2+ ERROR entries):
  - **MECH-112 — 4 ERRORs** (074, 074d, 225a, 225b) — top code-crash recurrence.
  - **MECH-163 — 3 ERRORs** (237b, 237c, 495).
  - SD-003 (2), ARC-007 (2), MECH-113 (2), MECH-116 (2), SD-018 (2), SD-012 (2), MECH-188 (2), INV-052 (2).
  - ⚠️ 39 ERROR rows carry **no claim_id** — untagged crashes are the single largest ERROR bucket and evade per-claim trend tracking.

- **Stalled chains:** the active queue holds only **3 items** (610f/INV-074 @prio 320, 643 @290, 641a @285). The closure pipeline reports `pending_review=0` and most FAIL chains are intentionally closed or migrated to new numbers — not stalled. The genuine open frontier is the three queued items plus in-flight 640a / 610f / 641.

---

## Substrate Bottlenecks

95 substrate-queue items. Status is heterogeneous (no bare `ready`): 49 `implemented`, 9 `candidate_v3_pending`, plus phased/landed/validation variants.

- **Implementable / decision-pending now:** `next_implement_substrate` is a **governance decision gated on the Q-040 (EXQ-490b) outcome** distinguishing MECH-269b vs MECH-295 as the dominant cause of the EXQ-471 catatonic-lock signature. Named ready-but-gated: SD-019a (socially gated on Q-036 controllability), MECH-269b-followup-A.
- **Blocked (explicit precondition):** **SD-016** — `parked_pending_env_entropy_precondition` (z_world cross-context separation not yet satisfiable in current CausalGridWorldV2). This is the substrate root cause behind the EXQ-418 chain's persistent FAILs.
- **Highest failure-record counts** (experiments that failed for want of the substrate):
  - **`scaffolded_sd054_onboarding` — 20** (foraging-competence residual; the cue→action **selection-authority ceiling**, now pushed downstream to `modulatory-bias-selection-authority` / EXQ-640a).
  - **MECH-256 — 10** (self-attribution single-pass comparator; candidate_v3_pending).
  - **ARC-062 — 9** (rule-apprehension; drives the EXQ-543 chain).
  - **SD-037 — 6** (broadcast override regulator).
  - **SD-016 — 5**, SD-049 — 4, `modulatory-bias-selection-authority` — 4, SD-015 — 3, SD-029 — 3, MECH-307 — 3.

The selection-authority ceiling (`modulatory-bias-selection-authority`, EXQ-640a) is the current critical-path substrate bottleneck — it blocks V3-EXQ-603f and is the residual behind the SD-054 foraging-competence work.

---

## Governance State

- **Claims pending V3 substrate** (`v3_pending: true` occurrences in claims.yaml): **135** (and 128 `pending_retest_after_substrate` markers).
- **Decision queue:** 111 rows — **109 `applied`, 2 `pending_user`**.
  - Pending user decision: **ARC-080** (object-representation umbrella, hold_pending_v3_substrate) and **MECH-342** (hold_pending_v3_substrate).
  - Recommendation mix: 154 `hold_pending_v3_substrate`, 50 `hold_candidate_resolve_conflict`, 1 `promote`.
- **Evidence superseded (rework):** **34** manifests carry `evidence_direction: superseded` — correctly excluded from confidence/conflict scoring.
- **Pending experiment review:** **0** — closure pipeline is fully caught up.

The dominant governance shape is a large `hold_pending_v3_substrate` backlog (154 holds): claims are out-running the substrate's ability to test them. This is the structural tension to watch.

---

## Literature Coverage

- **Literature backlog:** 14 items — 7 `in_progress`, 6 `open`, 1 `covered`.
- **Priority-1 open:** none — all open lit items are medium/low priority.
- **Open items:** ARC-046, SD-055, MECH-306 (medium); Q-054 (medium); Q-055, Q-056 (low).
- **In-progress:** MECH-044, MECH-282, MECH-286, MECH-333, MECH-339, MECH-340, MECH-341.
- 306 entries in `evidence/literature/` — coverage is broad; the backlog is the long tail.
- **Recent lit-pull targets** (from session history): ARC-067 boredom, MECH-320 crystallization, Q-019 pin-reconcile, and an in-flight `contextual_memory_allocation_gate` review (slug claimed, **no verdict.md yet** — gating the MECH-261 amend-vs-new-child decision).

---

## Human-Intervention Patterns

Derived from WORKSPACE_STATE session history + error analysis:

- **Tasks that recurrently required human input:**
  - **Governance candidate-claim dispositions** — recurring `STOP for user sign-off` pauses. Live: ARC-080 and MECH-342 (`pending_user`); the Contextual Memory Allocation Gate B+D claims explicitly gated behind a user fold-vs-separate / amend-vs-new decision + the in-flight lit verdict.
  - **IGW auto-spawn** — required a human-driven respawn-loop fix (2026-06-04): 20 of 23 ledger spawns were two items re-spawned (INV-074 12×, MECH-229 8×). Fixed (cooldown + time-boxed AUTO_DEFER), but launchd `com.ree.igwroutine` left **unloaded/disabled** pending user re-enable.
  - **Substrate implementation decisions** — `next_implement_substrate` is a governance decision pending Q-040, not auto-selectable.
  - **claim_id attribution on high-iteration chains** — EXQ-085's MECH-071→SD-015/ARC-030 drift is the canonical trap; attribution disputes need human adjudication.

- **Low-friction headless tasks** (completed cleanly across recent sessions):
  - lit-pull (ARC-067, MECH-320, Q-019), nightly update-docs, insights, pending-review sweeps, failure-autopsy, infant-substrate GAP implementations (GAP-11/12/13/14), and IGW NO-OP retest closes.

---

## Recommendations

1. **Resolve the selection-authority ceiling first.** `modulatory-bias-selection-authority` (EXQ-640a) is the live critical-path bottleneck: 4 failure records, blocks V3-EXQ-603f, and is the true residual behind the 20-failure `scaffolded_sd054_onboarding` chain. Prioritize 640a validation over new substrate.

2. **Land the Q-040 diagnostic (EXQ-490b) to unblock `next_implement_substrate`.** The entire substrate-selection pointer is parked on the MECH-269b-vs-MECH-295 catatonic-lock adjudication. Until it resolves, implement-substrate has no auto-target.

3. **Clear the 2 `pending_user` governance decisions** (ARC-080 object-rep umbrella, MECH-342) and the gated Contextual Memory Allocation Gate (B+D) once the in-flight lit verdict lands — these are the only items blocked solely on user sign-off.

4. **Tighten ERROR attribution.** 39 of 87 ERRORs (45%) and the EXQ-445 chain carry no claim_id; MECH-112 has 4 crashes. Untagged crashes evade trend tracking — enforce claim_id on every queue entry (the `/queue-experiment` smoke test should reject blank claim_id) and route MECH-112 through `/diagnose-errors`.

5. **Drain the lit long-tail opportunistically.** No priority-1 lit gaps remain; 6 open items are medium/low. Fold the in-flight `contextual_memory_allocation_gate` verdict to release the MECH-261 amend decision; otherwise lit is not on the critical path.
