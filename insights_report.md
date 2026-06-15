# Project Insights — 2026-06-15

Generated: 2026-06-15T04:06:01Z

> **Data caveat:** `runner_status.json` is the legacy git-materialised completion log; its
> latest entry is 2026-06-09. Under Phase 3 the coordinator DB is authoritative for run
> outcomes, so EXQ rows numbered >= ~659 (e.g. 659, 671) appear in WORKSPACE_STATE / the queue
> but not yet in this file. Experiment-health counts below are therefore a lower bound through
> ~2026-06-09; governance/substrate/session analysis is current to 2026-06-13.

---

## Experiment Health

- **Total runs:** 840 (PASS: 283 | FAIL: 437 | ERROR: 87 | UNKNOWN: 32 | INCONCLUSIVE: 1 | error rate: 10.4%)
- **Date span:** 2026-02-26 -> 2026-06-09 (V1 + V3 combined log)
- **High-iteration experiments** (3+ lettered iterations — top of a long tail of ~78 chains with 3+ letters):
  - V3-EXQ-085 — 14 iterations — claims: MECH-071 (caveat: claim_ids drift across letters; later letters re-tagged toward SD-015/ARC-030 goal-navigation, *not* the harm-calibration claim MECH-071)
  - V3-EXQ-418 — 13 iterations — claims: SD-016, SD-017 (sleep/aggregation; SD-016 now `parked_pending_env_entropy_precondition`, 5 failure records)
  - V3-EXQ-514 — 13 iterations — claims: SD-049 (goal_pipeline GAP-2 Phase-2 behavioural; latest 514l FAIL 2026-06-02)
  - V3-EXQ-490 — 10 iterations — claims: MECH-269b / MECH-295 / Q-040 (the contaminated Q-040 cohort; live successor 490j/490k PASS)
  - V3-EXQ-543 — 10 iterations — claims: ARC-062, MECH-309 (rule-apprehension; latest 543k FAIL 2026-05-21)
  - V3-EXQ-047 — 9 iterations — claims: MECH-095, SD-005
  - V3-EXQ-445 — 9 iterations — claims: *untagged* (no claim_id on any letter)
  - V3-EXQ-603 — 8 iterations — claims: Q-045 (escape-affordance / scaffolded_sd054; live, 603j PASS 2026-06-09)
- **Recurring trouble spots** (claim_ids in 2+ ERROR entries):
  - **(untagged) — 39 ERROR entries** — by far the largest ERROR class; queue items with no `claim_id`/`claim_ids`. (Mitigation already shipped 2026-06-06: `validate_queue.py` now WARNs on claimless items; explicit `claim_ids: []` silences intentional diagnostics.)
  - MECH-112 — 4 ERROR (074, 074d, 225a, 225b)
  - MECH-163 — 3 ERROR (237b, 237c, 495)
  - SD-003 / ARC-007 / MECH-113 / MECH-116 / SD-018 / SD-012 / MECH-188 / INV-052 — 2 ERROR each
- **Stalled chains** (latest iteration is FAIL/ERROR, since 2026-05-15, no successor yet visible in this log):
  - V3-EXQ-610f — FAIL 2026-06-08 — INV-074 (crystallization-necessity; 6 iters)
  - V3-EXQ-624b — FAIL 2026-06-07 — MECH-320 (calibration-debt priority-1)
  - V3-EXQ-651a — FAIL 2026-06-07 — ARC-060
  - V3-EXQ-648a — FAIL 2026-06-07 — (untagged; MECH-314a Phase-2, autopsied -> redesign queued)
  - V3-EXQ-632 — FAIL 2026-06-03 — MECH-230
  - V3-EXQ-625c — FAIL 2026-06-02 — (SD-037 axis-b lock; see memory note)
  - V3-EXQ-514l — FAIL 2026-06-02 — SD-049 (13-iter chain)
  - V3-EXQ-622 — FAIL 2026-05-31 — Q-045
  - V3-EXQ-616 — FAIL 2026-05-31 — Q-054
  - V3-EXQ-517c — ERROR 2026-05-30 — MECH-302 (4-iter chain ending in a crash)

---

## Substrate Bottlenecks

Source: `evidence/planning/substrate_queue.json` (101-item queue, schema v2). Status field is
free-text and heavily annotated, so counts below use the `ready` boolean + `depends_on_unresolved`.

- **Ready SDs** (`ready=true`, not yet `implemented`): 7
  - `scaffolded_sd054_onboarding` (prio 1) — readiness FLIPPED true 2026-06-11 (603n PASS); **unblocks 18 claims** incl ARC-030, MECH-094, MECH-117, MECH-230, MECH-260/261/266/268, MECH-295/307/313, Q-040, Q-045, SD-032a, SD-033a, SD-034, SD-049-Phase-2. Highest-leverage ready node in the queue.
  - MECH-302 (prio 1, validated) — unblocks MECH-302/303
  - MECH-258 (prio 1, candidate_v3_pending) — unblocks SD-032b
  - ARC-058 (prio 1, candidate_v3_pending)
  - SD-033b (prio 2) — unblocks MECH-261/263
  - MECH-341 (prio 2, amend_validated 614c/614d — zero committed authority)
  - MECH-090 (prio 2) — unblocks MECH-090, SD-034, MECH-266/267/268
- **Blocked SDs** (`depends_on_unresolved` non-empty): 33. Deepest dependency knots:
  - SD-033 family (SD-033/b/c/d/e) — all gated on the MECH-094 / MECH-261 / ARC-035 cluster
  - SD-024 -> SD-025 -> SD-026 -> SD-027/SD-028 — a 4-deep INV-009/MECH-007 chain
  - ARC-065 / MECH-313 / MECH-314 — gated on the Q-043/044/045 ablation cohort
- **SDs with failure records** (experiments failed for want of this substrate): 46. Highest counts:
  - `scaffolded_sd054_onboarding` — 27 failure records (now resolved/ready)
  - modulatory-bias-selection-authority — 14
  - MECH-256 — 10 | ARC-062 — 10 | SD-037 — 6 | SD-016 — 5 | ARC-065 — 5
  - commitment-closure-control-plane — 4 | SD-049 — 4

**Cross-reference with high-iteration chains:** the 543 (ARC-062, 10 failure records), 514
(SD-049, 4), and 610 (INV-074) chains map directly onto the top failure-record substrates —
these are the same bottlenecks seen from the experiment side.

---

## Governance State

- **Claims pending V3 substrate** (`v3_pending: true` in claims.yaml): **211**
- **Pending promotion/demotion decisions** (`pending_user` in promotion_demotion_recommendations.md): **31 rows / 13 distinct claims** — ARC-088, ARC-096, ARC-097, INV-081, INV-082, MECH-057b (conflict-resolution), MECH-129, MECH-180, MECH-217, MECH-339, MECH-340, MECH-411, Q-054
- **Evidence superseded (rework):** 51 manifests carry `evidence_direction: superseded`. Largest rework cluster remains the Q-040 contamination cohort (EXQ-471/483/490 series).

---

## Literature Coverage

- **Priority-1 backlog items still open: 0** — no high-priority literature gaps. (Recent lit-pull cadence has kept pace: RHM-6, DRV-3 closed 2026-06-12/13.)
- **Total open literature items: 20** — all `priority: low` (EVB-0285..0396, claims Q-055..Q-077, a block of low-priority Q-claim groundings).
- **In progress: 3 | Covered recently: 1**
- **Covered in recent sessions** (from WORKSPACE_STATE): MECH-129 + MECH-164 (RHM-6 relational-harm / love-as-care, 2026-06-12), MECH-394 + SD-060 (DRV-3 drive-arbitration, 2026-06-13).

---

## Human-Intervention Patterns

Session-type tally from the last ~300 lines of WORKSPACE_STATE.md (keyword frequency, not exact session count):

| Activity | Mentions | Friction profile |
|----------|----------|------------------|
| governance | 39 | structural; runs but produces `pending_user` decisions needing the user |
| lit-pull | 22 | **low-friction / headless** — RHM-6, DRV-3, etc. completed clean |
| register (claims) | 17 | **needs user sign-off** — proposal-first; MECH-435 explicitly waited for user direction |
| queue-experiment | 14 | mostly clean (skill-gated smoke tests catch errors pre-queue) |
| failure-autopsy | 14 | **recurrently needs user** — routing decisions (amend-vs-requeue) user-confirmed |
| diagnose-errors | 10 | claim-attribution disputes recur here |
| implement-substrate | 6 | each pauses for plan confirmation |

- **Tasks that recurrently required human input:**
  - **failure-autopsy routing** — autopsies (648, 640a, 603m) consistently end with a *user-confirmed* routing decision (amend substrate vs requeue vs reclassify). The diagnostic self-route label is a hypothesis, not a verdict (see `feedback_diagnostic_self_route_is_hypothesis`).
  - **claim registration** — proposal-first by policy; MECH-435 and the memory-allocation-gate cohort both stopped for user sign-off before any claims.yaml edit.
  - **promotion decisions** — 13 claims sitting in `pending_user`, several needing conflict resolution (MECH-057b) or a fold-vs-separate call.
- **Low-friction headless tasks:** lit-pull (kept priority-1 backlog at zero), queue-experiment (skill smoke-tests catch propagated errors before they reach the runner), insights/digest.

---

## Recommendations

1. **Action the `scaffolded_sd054_onboarding` ready flag — it is the single highest-leverage node.** It flipped `ready=true` 2026-06-11 (603n PASS), carries 27 historical failure records, and **unblocks 18 claims** including the MECH-094/261/295 and SD-049-Phase-2 clusters that dominate the high-iteration chains (514, 490). The 514l/SD-049 GAP-2 Phase-2 successor is now queueable per the substrate note. Run `/implement-substrate` (or queue the SD-049 Phase-2 behavioural validation) against this next.

2. **Triage the stalled INV-074 (610f) and MECH-320 (624b) chains.** Both are recent (2026-06-08/07) FAILs with no successor visible in the log. INV-074 is a 6-iteration crystallization-necessity chain; MECH-320 is a calibration-debt priority-1 claim. Route each through `/failure-autopsy` to decide requeue-vs-amend before they stale further.

3. **Clear the 13 `pending_user` promotion decisions in a single governance-interactive pass.** Most are routine `hold_pending_v3_substrate` acks, but MECH-057b needs conflict resolution and MECH-129/180/217 are evidence-bearing. Batching them keeps the decision queue from accreting.

4. **(Maintenance) The 39 untagged-ERROR class is the largest recurring failure mode.** The `validate_queue.py` WARN mitigation shipped 2026-06-06; confirm new queue entries are either tagged or carry explicit `claim_ids: []`. No priority-1 literature gaps remain — lit cadence is healthy and can stay headless.
