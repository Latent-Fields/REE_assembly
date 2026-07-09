# Project Insights — 2026-07-09

Generated: 2026-07-09T06:21:28Z

---

## Experiment Health

> **Caveat:** `runner_status.json` is frozen at **2026-06-09** (last_updated 2026-06-09T06:00Z). Under Phase 3 the live experiment record moved to the coordinator DB + per-run manifests in `evidence/experiments/`; the file below is the historical corpus (EXQ-000 .. ~653), **not** the current 700-series work. Counts are lifetime-to-cutover.

- **Total runs:** 840 (PASS: 283 | FAIL: 437 | ERROR: 87 | UNKNOWN: 32 | INCONCLUSIVE: 1)
- **Error rate:** 10.4% (87 / 840). FAIL is the dominant outcome (52%) — expected for a falsification-driven programme, but see "high-iteration" below for where FAILs are churning rather than resolving.

- **High-iteration experiments** (3+ lettered iterations — 79 chains total; top offenders):
  - `V3-EXQ-085` — 14 runs — claims: MECH-071 *(claim drifted to SD-015/ARC-030 mid-chain; goal-navigation, not harm-calibration)*
  - `V3-EXQ-418` — 13 runs — claims: SD-016 / SD-017
  - `V3-EXQ-514` — 13 runs — claims: SD-049 *(SD-049 Phase-2 still blocked; see substrate)*
  - `V3-EXQ-490` — 10 runs — claims: MECH-269b / MECH-295 / Q-040 *(Q-040 cohort found contaminated 2026-05-07, superseded)*
  - `V3-EXQ-543` — 10 runs — claims: ARC-062 / MECH-309 *(the f-dominance conversion-ceiling lineage)*
  - `V3-EXQ-047` (9), `V3-EXQ-445` (9, untagged), `V3-EXQ-603` (8, Q-045), `V3-EXQ-433` (7, SD-029), `V3-EXQ-540` (7, MECH-307)

- **Recurring trouble spots** (claim_ids in 2+ ERROR entries):
  - `MECH-112` — 4 ERRORs · `MECH-163` — 3 ERRORs
  - `SD-003`, `ARC-007`, `MECH-113`, `MECH-116`, `SD-018`, `SD-012`, `MECH-188`, `INV-052` — 2 ERRORs each

- **Stalled vs iterating:** the long chains above are mostly *iterating* (lettered successors queued). The genuine stall signal is now in the **substrate failure records**, not runner_status — see next section. The live queue (721/723/724) is **all diagnostics** circling one root.

---

## Substrate Bottlenecks

Source: `evidence/planning/substrate_queue.json` (106 entries; 53 implemented).

- **`ready: true`: 49 SDs — but this flag means "substrate BUILT / on the shelf", NOT "awaiting implementation".** Verified 2026-07-09: all 49 carry `implementation_status: implemented` (or landed/validated/built). **There is no starved build backlog.** What these built substrates are missing is, in most cases, a **validation experiment** that converts their unblocked claims out of `v3_pending` — not code. High-leverage built-but-unconverted examples (claims they'd unblock): `MECH-269` (9), `SD-035` (6, val V3-EXQ-473/474), `SD-022` (5, val V3-EXQ-319), `SD-018` (goal-directed pathway / EXQ-085 cluster). The sleep cluster (`MECH-272/273/275/285/287/288`) is contract-validated already.
  - *Correction note:* an earlier draft of this report called these "ready to implement" and "starved" — that misread the `ready` flag. The genuine adjacent lever is **validation-experiment coverage of already-built substrate**, not new implementation.

- **Blocked (unresolved deps): 36 SDs.** Deepest dependency knots: the `SD-033*` cluster (033/033b/033c/033d/033e all waiting on MECH-261/094), `SD-024/025/026/027/028` chain, `SD-049-PHASE-2` (waiting on V3-EXQ-514u measurement redesign).

- **SDs with failure records: 50.** The concentration is stark — two entries own the churn:
  | Substrate | Failures | Ready? |
  |---|---|---|
  | `f_dominance_conversion_ceiling` (MECH-439) | **26** | ❌ |
  | `scaffolded_sd054_onboarding` | **28** | ✅ |
  | `modulatory-bias-selection-authority` | 15 | ✅ |
  | `ARC-062` (rule-apprehension) | 11 | ❌ |
  | `MECH-256` (self-attribution) | 10 | ❌ |
  | `v4_loop_segregation` | 9 | ❌ |
  | `SD-049-PHASE-2` | 8 | ❌ |

**The single dominant bottleneck is the F-dominance committed-action conversion ceiling** (`f_dominance_conversion_ceiling`, 26 failures; its sibling `scaffolded_sd054_onboarding` foraging-competence residual, 28). The entire live queue is diagnostics against it: V3-EXQ-721 (MECH-446 closure→latch lag), V3-EXQ-724 (competence-localization OFAT — explicitly "shared root of the 654h/485i/625e/460h/460i substrate_not_ready wall"), plus V3-EXQ-723 (J-lens readout). This is where iteration effort is being spent and where it is *not yet converging* — the arbitration-reweighting route (709/711/713) was declared **exhausted** in autopsy 2026-07-05, and the question was reclassified V4→V3 (must be closed in V3).

---

## Governance State

- **Claims pending V3 substrate (`v3_pending: true`): 220** · **`implementation_phase: v3`: 309**. The v3_pending pool is large and growing — most cannot move until substrate lands, and substrate is bottlenecked on the one ceiling above.
- **Promotion/demotion decisions pending user: 3** live rows — `ARC-106`, `Q-080` (question narrowing), `SD-063`. The bulk of the decision queue (121 demote / 29 promote references) is already `applied`; the dominant standing recommendation is `hold_pending_v3_substrate`.
- **Pending experiment review: 1** — `v3_exq_720_coherence_nonreducibility_bound_substrate` (FAIL, no claim tags). Clean.
- **Rework (supersession):** the Q-040 / EXQ-471/483/490/490b cohort remains the canonical contamination event (swallowed TypeError → `is_active()` always False, superseded 2026-05-07); the 654-lineage CRF-gate lockout was a second multi-letter substrate-amend cycle (654c→654f).

---

## Literature Coverage

- **Literature backlog is effectively saturated.** `evidence_backlog.v1.json`: of 366 items, **365 need `experimental` evidence, exactly 1 needs `literature`**. There are **no open priority-1 literature items.**
- `evidence/literature/` holds **384 entries** (targeted reviews across ARC/MECH/SD families).
- **Implication:** literature is no longer the constraint. The backlog is entirely experiment-bound — 150 open + 155 in_progress experimental items. Effort spent on lit-pulls now has near-zero marginal governance value except for *newly registered* claims.

---

## Human-Intervention Patterns

Derived from the last ~150 WORKSPACE_STATE Recent-Work entries (session-type mentions):

- **governance (44), queue-experiment (35), review (35), failure-autopsy (35), diagnose-errors (23)** dominate. sync (16), implement-substrate (16), lit-pull (7), morning-digest (7).
- **Recurrently needs human input:**
  - **failure-autopsy / diagnose-errors** — the highest-friction loop. The f-dominance ceiling has generated repeated autopsy cycles (709/711/713 exhaustion call, 654d, 603m, 719a) each requiring a judgement call on *root vs measurement artifact*. This is where the project actually spends its human attention.
  - **governance decisions** — the `pending_user` rows and conflict-resolution holds are interactive by design (skill pauses for input).
  - **claim attribution on high-iteration chains** — the EXQ-085 / 490 / 543 drift cases need a human to confirm which claim a FAIL actually bears on.
- **Low-friction / headless-safe:** lit-pull (saturated, rarely contested), morning-digest, sync, insights, pending-review generation. These ran clean.

---

## Recommendations

1. **Stop widening; force a verdict on the F-dominance conversion ceiling.** It owns 26 (+28 sibling) failure records, the entire live queue, and the reclassified-to-V3 closure requirement. The diagnostics (721/724) are localization, not fixes. Once V3-EXQ-724 localizes *why* the all-ON agent forages below floor, route straight to a single `/implement-substrate` build attempt — do not queue further OFAT letters. The arbitration-reweighting route is already declared exhausted; a new lever (competence/training-regime), not another reweighting, is what 724 is scoped to find.

2. **Convert already-built substrate, don't "implement" it — there is no build backlog.** The 49 `ready` SDs are *built*, not waiting to be built (correction above). The real starvation is on the **validation-experiment** side: built substrates (`MECH-269`, `SD-035`, `SD-022`, `SD-018`, …) that unblock `v3_pending` claims but whose validation run hasn't landed. While the F-dominance ceiling waits on V3-EXQ-724, the highest-value *parallel* work is queuing those validation experiments (a `/queue-experiment` task, and exactly what the fleet-idle loop should surface once it filters on "validation not yet run"). Pick targets by (claims-unblocked x validation-not-run), not by leverage alone.

3. **Retire routine lit-pull as a standing loop.** Literature is saturated (1 open lit item of 366). Keep lit-pull **event-triggered** (fires only when a genuinely new claim registers), not scheduled. Redirect that cadence to substrate implementation and autopsy throughput.

4. **Fix the stale-telemetry blind spot.** `runner_status.json` froze 2026-06-09; insights/morning-digest that read it are analysing a month-old corpus. Point trend analysis at the coordinator DB / manifests (or the `live-status` branch) so health metrics reflect the 700-series work.
