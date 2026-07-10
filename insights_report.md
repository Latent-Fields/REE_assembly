# Project Insights — 2026-07-10

Generated: 2026-07-10T16:34:12Z

> **Corpus caveat:** `runner_status.json` completed entries span **2026-02-26 → 2026-06-09**
> (840 runs). Since the Phase-3 cutover (2026-05-28/29), live results are written by the
> coordinator to per-run manifests, so `runner_status.json` is **no longer the live record**
> for June–July runs. Experiment-health numbers below are the historical Feb–Jun corpus;
> governance/substrate/backlog numbers are current-state.

---

## Experiment Health

- **Total runs (Feb–Jun corpus):** 840 — PASS: 283 | FAIL: 437 | ERROR: 87 | UNKNOWN: 32 | INCONCLUSIVE: 1
  - **Error rate: 10.8%** (87 / 807 terminal). FAIL rate 54% — high, but FAIL = "ran, criteria not met," the expected mode for a falsification-driven programme.
- **ERROR root-cause breakdown** (the actionable slice):
  - `exit code 1` (genuine code bug): **65**
  - `no sentinel / silent` (no PASS/FAIL emitted): **11**
  - `infra SIGTERM (-15/137)` (cloud-scaler shutdown-during-run): **9** — infra, not code; already mitigated by the runner `_transient_exit_codes` set
  - reentrant-IO: 1 · Windows FS permission: 1
- **High-iteration experiments** (3+ lettered iterations — repeated diagnose/rework cycles):
  - **EXQ-085 — 14 iters** (085, b–o) — claims: MECH-071 *(⚠ claim drifted mid-chain; last letters re-tagged SD-015/ARC-030 — do not attribute all 14 to MECH-071)*
  - **EXQ-418 — 13 iters** (418, a–l) — claims: SD-016, SD-017 (sleep/aggregation lineage)
  - **EXQ-514 — 13 iters** (514, a–l) — claims: SD-049 (Phase-2 behavioural validation ladder)
  - **EXQ-490 — 10 iters** — claims: MECH-269b, MECH-295, Q-040
  - **EXQ-543 — 10 iters** — claims: ARC-062, MECH-309
  - **EXQ-047 — 9 iters** — claims: MECH-095, SD-005
  - **EXQ-445 — 9 iters** — claims: *(none tagged)*
  - **EXQ-603 — 8 iters** — claims: Q-045 (harm-pathway / foraging-competence ecology)
  - EXQ-433 (7, SD-029) · EXQ-540 (7, MECH-307) · EXQ-074/076 (6, MECH-112/116/117) · EXQ-166 (6) · EXQ-325 (6) · EXQ-610 (6, INV-074)
- **Recurring trouble spots** (claim_ids in 2+ ERROR entries):
  - **MECH-112 — 4 ERRORs** (EXQ-074, 225a, 225b, 074d) — most error-prone claim in the corpus
  - **MECH-163 — 3 ERRORs** (237b, 237c, 495)
  - ARC-007 (2) · MECH-113 (2) · MECH-116 (2) · SD-003 (2) · SD-012 (2) · SD-018 (2) · MECH-188 (2) · INV-052 (2)

---

## Substrate Bottlenecks

Substrate queue: **106 items** (54 implemented/validated).

- **Ready & not-yet-implemented** (buildable now): **MECH-090** (P2 — BetaGate commit-entry readiness conjunction). *(The other 48 `ready:true` items are already implemented/validated.)*
- **Highest-blast-radius blockers** (ready:false, ranked by failure-record count — these missing/incomplete SDs are directly causing repeated FAIL/ERROR iterations):
  1. **`f_dominance_conversion_ceiling` — 26 failure records** (P1) — the dominant recurring bottleneck; the committed-action-diversity / selection→conversion ceiling. Route of record is the GAP-A/GAP-B falsifier ladder, not a further CRF amend.
  2. **ARC-062 — 11** (P1)
  3. **MECH-256 — 10** (P1) — blocked on MECH-269 V_s landing before C2/C3 are measurable
  4. **SD-049-PHASE-2 — 9** (P1) — Phase-2 hybrid encoder validation (feeds the EXQ-514 13-iter chain)
  5. **`v4_loop_segregation` — 9** (P1, reappointed V4→V3) — also gates Q-019
  6. **`modulatory-bias-selection-authority` — 15** — the cue-to-action selection-authority ceiling that keeps EXQ-603/634 foraging-contact at ~0
  7. ARC-065 (7) · commitment-closure-control-plane (7) · SD-037 (6) · SD-016 (5) · crf-availability-maintenance (5)
- **Cross-reference:** the top failure-record SDs map straight onto the high-iteration chains — SD-049↔EXQ-514, ARC-062↔EXQ-543, f_dominance↔EXQ-654 ladder, selection-authority↔EXQ-603. The iteration churn is substrate-gated, not instrumentation-gated.

---

## Governance State

- **Claims pending V3 substrate (`v3_pending: true`): 221** (of 877 claims; `implementation_phase: v3` on 311). This is the structural backlog — the bulk of the registry is waiting on V3 substrate before any evidence can move it.
- **Pending promotion/demotion decisions: 1** (`Q-080`, `narrow_open_question`, `pending_user`). All other 102 recommendations are `applied` — governance board is otherwise clean.
- **Evidence superseded / reworked:** **100 manifests** carry a `superseded` marker (rework from lettered re-runs; correctly excluded from claim confidence by the indexer).

---

## Literature Coverage

- **Backlog note:** `evidence_backlog.v1.json` tracks **365 experimental / 1 literature** item — literature is *not* tracked there. Actual literature lives in `evidence/literature/` as **376 `targeted_review_*` dossiers**, indexed in `INDEX.md`.
- **No priority-1 literature gaps open** in the backlog (all P1 items are in_progress or covered; the 148 `open` items are all medium-priority experimental, not literature).
- **Recent lit-pull targets** (from WORKSPACE_STATE, last ~4 weeks): RHM6 relational-harm/love, DRV3 drive-arbitration, **Q-019 three-gate basal-ganglia** (DLS habit lesion / MD thalamus / VLS territory — landed 2026-07-10). Literature pulls are running low-friction and headless.

---

## Human-Intervention Patterns

Derived from WORKSPACE_STATE session labels (last ~30 sessions) and the error corpus:

- **Recurrently needs human input:**
  - **Substrate implementation** (`implement-substrate-*`) — every instance pauses for plan/scope confirmation before building (MECH-449, scaffolded_sd054). Highest-touch task type.
  - **Governance disposition** (`govdecision-*`, `governance-cycle-*`) — interactive by design; pauses before applying promote/demote decisions.
  - **Failure autopsy** (`failure-autopsy-445h`, 732a) — claim-attribution and "is this substrate-not-ready vs a real fault" calls repeatedly need a judgement pass (the EXQ-085 / EXQ-654 claim-drift traps are the canonical reason).
- **Low-friction / headless-safe** (completed without intervention across multiple recent sessions):
  - **lit-pull** — 3/3 recent runs clean (RHM6, DRV3, Q-019).
  - **nightly /update-docs** — scheduled, bot-identity commits, no intervention.
  - **igw-ledger / phase-tag hygiene** (arc034, gapk) — mechanical, "PROMOTES NOTHING" closes.
  - **queue-experiment** — runs through the skill's smoke-test gate without dispute.

---

## Recommendations

1. **Attack the `f_dominance_conversion_ceiling` bottleneck as the single highest-leverage target** — 26 failure records, P1, and the shared root behind the EXQ-654 ladder plus the MECH-439 F-dominance conversion ceiling that keeps stalling behavioural retests (654h/485i/625e/445h all FAIL "substrate not ready"). Per the queue notes the arbitration-reweighting route is *exhausted* (709/711/713 autopsy 2026-07-05); the open question is now the GAP-A-lift generalisation. Confirm with the user whether the next move is the GAP-B falsifier or a design pivot — this one blocker is gating the most rework.
2. **Build `MECH-090`** (BetaGate commit-entry readiness conjunction) — the *only* ready-and-unimplemented SD, P2, and it appears in the promotion table at 0.72 confidence. Low-risk, unblocks its own retest, no dependency wait.
3. **Unwedge the SD-049 / EXQ-514 Phase-2 ladder** (9 failure records, 13 iterations) — the hybrid encoder is implemented but Phase-2 behavioural validation keeps re-failing; this is the second-largest substrate-gated iteration sink after f_dominance. Worth a focused autopsy on whether 514's gate is measurement-artifact (à la the 603m/603n G0 recalibration) rather than re-queuing another letter blind.
4. **Governance is clean** — only Q-080 pending. No action beyond the user's open-question narrowing call.
