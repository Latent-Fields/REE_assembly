# Project Insights — 2026-06-03

Generated: 2026-06-03T22:36:53Z

Read-only trend analysis over `runner_status.json` (808 completed runs), the live
queue, `substrate_queue.json`, `claims.yaml`, `promotion_demotion_recommendations.md`,
`evidence_backlog.v1.json`, and the last ~160 `WORKSPACE_STATE.md` entries. Pair with
`/morning-digest` for the daily action list.

---

## Experiment Health

- **Total completed runs:** 808 — PASS 260 | FAIL 428 | ERROR 87 | UNKNOWN 32 | INCONCLUSIVE 1
  - **Error rate (ERROR / all):** 10.8%
  - **Pass rate (PASS / PASS+FAIL):** 37.8% — FAIL-heavy, as expected for a falsification-driven programme
  - 32 UNKNOWN are legacy residue (silent-drop fixed f36461d 2026-05-08); not live failures.

- **High-iteration chains (3+ distinct queue_ids on one base):** 82 bases. Heaviest:

  | Base | # iters | runner_status result mix | claim signal (caveat below) |
  |------|---------|--------------------------|-----------------------------|
  | EXQ-085 | 14 | 14 FAIL | tagged MECH-071, but chain **drifted** to SD-015/ARC-030 and migrated to the 622/626 ladder (626 FAILed 2026-06) |
  | EXQ-418 | 13 | 8F / 2U / 1P / 2E | SD-016, SD-017 (sleep action-bias-div) — 418l live |
  | EXQ-514 | 13 | 9F / 1E / 3P | SD-049 wanting/liking identity — 514k FAILed 2026-06-01 (identity-distinct probe) |
  | EXQ-543 | 10 | 9F / 1P | ARC-062, MECH-309 — evidence-gated on 543k/598 |
  | EXQ-490 | 9 | 8F / 1U | MECH-269b, MECH-295, Q-040 factorial — 490j queued |
  | EXQ-445 | 9 | 7F / 1U / 1E | untagged |
  | EXQ-047 / 433 / 540 / 074 / 076 / 166 / 325 | 6–9 each | mostly FAIL | various |

  **Attribution caveat (per skill):** runner_status `claim_id` is stale/blank on most
  recent rows and does NOT capture claim drift. EXQ-085 is the canonical trap — its later
  letters dropped MECH-071 and re-tagged to goal-navigation claims; those FAILs are not
  evidence against MECH-071. Confirm per-iteration claim_ids and per-criterion direction
  in the manifests before treating any of these as evidence against the head claim.

- **Recurring ERROR trouble spots (claim_id in 2+ ERROR rows):**
  - **MECH-112 — 4 ERRORs** (EXQ-074, 074d, 225a, 225b) — top recurring code-crash claim
  - **MECH-163 — 3 ERRORs** (EXQ-237b, 237c, 495)
  - SD-003, ARC-007, MECH-113, MECH-116, SD-018, SD-012, MECH-188, INV-052 — 2 ERRORs each
  - 39 ERRORs carry **no claim_id** — diagnostic/untagged scripts dominate the crash pool.

- **Recent ERROR cluster (last 15) is infra, not code:** 599/600/610a/621/612b/598/606a.
  WORKSPACE_STATE confirms 606a/598 root-caused to a git-sync gap on ree-cloud-2 (no code
  bug); 610a was a SIGTERM/cloud-timeout rescue. SIGTERM mitigation (`_transient_exit_codes`)
  is in place but the cloud fleet still produces transient-crash noise.

- **Stalled / open FAIL fronts (most-recent iteration FAILed, no PASS yet):**
  - EXQ-514 (SD-049 identity-distinct wanting) — 514k FAIL 2026-06-01; substrate landed, retest cycle continues
  - EXQ-085→626 ladder (SD-015/ARC-030 goal-nav) — 626 FAIL, no same-base successor queued
  - EXQ-543 (ARC-062/MECH-309 crystallization-falsifier) — 543{f–k} all FAIL, evidence-gated
  - EXQ-616 (Q-054), EXQ-603d (Q-045), EXQ-524a, EXQ-588b, EXQ-592c — recent FAILs, successor status unconfirmed

---

## Substrate Bottlenecks

- **94 substrate-queue items; 48 `implemented`.** No items in `ready` state — the pipeline
  is not deps-blocked, it is **validation-blocked**: most landed substrate is awaiting
  experiment confirmation, not implementation.
- **`next_implement_substrate` is a governance decision pending Q-040** (the MECH-269b vs
  MECH-295 factorial via EXQ-490b). No automatic next target.
- **Pending implementation:** ARC-046 (`pending_implementation`).
- **`candidate_v3_pending` (9):** MECH-204, MECH-256, MECH-257, MECH-258, MECH-260, MECH-262/263/264/265 cluster — substrate not yet built.
- **SDs with the most failure records** (experiments that failed for substrate reasons):
  - `scaffolded_sd054_onboarding` — **12** (seeding-calibration amend pending validation; 634c live)
  - MECH-256 — **10** (candidate_v3_pending)
  - ARC-062 — **9** (phase-1, evidence-gated 543k/598)
  - SD-037 — 6 · SD-049 — 4 · SD-016 — 4 (parked pending env-entropy precondition) · MECH-307 — 3 · modulatory-bias-selection — 3 · SD-015 / SD-029 — 3 each

  **Cross-reference:** the heaviest experiment chains map directly onto the heaviest
  substrate failure records — EXQ-543↔ARC-062, EXQ-514↔SD-049, EXQ-490↔MECH-269b. These
  are not flaky scripts; they are hard scientific fronts where substrate and experiment
  are co-evolving.

---

## Governance State

- **Claims with `v3_pending: true`:** 117 (was 6 in the early-V3 baseline — the held-claim
  pool has grown ~20× as the architecture expanded).
- **Claims with `implementation_phase: v3`:** 240.
- **Claims flagged `pending_retest_after_substrate: true`:** 28 — the active retest backlog
  (INV-074, MECH-229, etc.).
- **Decision queue:** 109 rows, **all `applied`** — 0 net-pending human decisions. Breakdown:
  75 `hold_pending_v3_substrate`, 25 `hold_candidate_resolve_conflict`, 9 `narrow_open_question`.
  The 25 conflict-resolution holds (ARC-030/032/041/042, INV-054, INV-074, MECH-073/075/098/099/111/112/116…)
  are the real governance debt — they need conflict adjudication, not more experiments.

---

## Literature Coverage

- **13 backlog items need literature:** 7 `in_progress`, 5 `open`, 1 `covered`.
- **No priority-1 lit items** — all are `medium` or `low`. Backlog is not literature-starved.
- **Open items:** EVB-0282 (ARC-046), EVB-0289 (MECH-306), EVB-0284 (Q-054), EVB-0285 (Q-055, low), EVB-0291 (Q-056, low).
- **In-progress:** MECH-282, MECH-286, MECH-333, MECH-339, MECH-340, MECH-341, MECH-342.
- **Recently covered (from WORKSPACE_STATE):** MECH-320 (EVB-0240, Niv/Daw 2007), ARC-067
  boredom (8 entries), Q-053 goal-disengagement (narrowed), EVB-PINNED-Q019 (reconcile-only).

---

## Human-Intervention Patterns

- **IGW (inter-governance-brief) duplicate-spawn churn — recurring.** 2026-05-30 IGW-020 and
  2026-06-02 IGW-029 each spawned 3× (hourly) and every spawn closed NO-OP because the work
  was already complete from a prior session. This is wasted scheduled-session overhead, not a
  blocked task. **Worth a dedup/idempotency guard on the IGW spawn trigger.**
- **Copy-and-modify propagated bugs — confirmed live.** The `emit_outcome()` copy-paste bug
  was swept across **6** experiment scripts (2026-05-30) before a regression guard landed.
  This is exactly the failure mode the mandatory `/queue-experiment` skill path exists to
  catch — reinforces that direct edits to `experiments/` must not bypass it.
- **Infra > code as the crash cause.** Recent diagnose-errors sessions (606a/598/610a)
  root-caused to git-sync gaps and SIGTERM on the cloud fleet, not script bugs. The
  human-facing diagnose-errors load is increasingly infra triage.
- **Low-friction headless tasks:** lit-pull (multiple clean autonomous completions, incl.
  the delegated 9-entry pull 2026-05-19), nightly `/update-docs`, and governance cycles run
  without human dispute in the recent window.

---

## Recommendations

1. **Drive the Q-040 factorial to resolution (EXQ-490b/490j).** It is the single gate on
   `next_implement_substrate` AND it sits under the 9-iteration EXQ-490 chain. Resolving the
   MECH-269b-vs-MECH-295 question unblocks the substrate selection that downstream chains
   (490/543/514) are all waiting on.
2. **Clear the 25 `hold_candidate_resolve_conflict` claims.** This is the real governance
   debt — they need conflict adjudication, not experiments. The conflict ratios (not missing
   substrate) are blocking promotion of ARC-030/032, INV-074, MECH-073/075/098/099/111/112/116.
3. **Add an idempotency guard to IGW spawn.** Six NO-OP triple-spawns in the last week are
   pure overhead; an "already-disposed-this-cycle" check before spawning would eliminate it.
4. **Audit MECH-112 and MECH-163 scripts (4 and 3 ERRORs).** These are the two claims with
   the most repeated code-crashes; route through `/diagnose-errors` for a root-cause fix
   rather than another letter.
5. **Pick up the 5 open `medium` lit items** (ARC-046, MECH-306, Q-054) opportunistically —
   low cost, and ARC-046 lit (EVB-0282) pairs with its `pending_implementation` substrate.
