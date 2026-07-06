# Failure Autopsy — V3-EXQ-715 (SD-034 de-commit science falsifier)

- **Generated (UTC):** 2026-07-06T16:41:21Z
- **Run:** `v3_exq_715_sd034_decommit_science_closure_commit_entry_falsifier_20260706T113002Z_v3`
- **Queue ID:** V3-EXQ-715 (supersedes V3-EXQ-460l)
- **Claims:** MECH-445 (closure→beta commit-intent, refractory-independent), MECH-446 (within-arm around-closure occupancy drop)
- **Outcome:** FAIL · self-route `substrate_not_ready_requeue` · `evidence_direction: unknown` · `non_degenerate: false`
- **Machine:** ree-cloud-2
- **Status:** confirmed (user-directed routing, 2026-07-06)

---

## 1. Facts (no interpretation)

Two arms on the full `scaffolded_sd054_onboarding` curriculum (460o config): `ARM_ENTRY_OFF` (baseline) vs `ARM_ENTRY_ON` (`use_closure_commit_entry` latch ON — the only variable). Question: do the two SD-034 de-commit-pipeline children **co-occur** on ≥2/3 seeds on the now-validated F-independent substrate?

Readiness / science ladder (self-routed):

| Precondition / criterion | measured | threshold | met |
|---|---|---|---|
| foraging_contact_guard | 1.0 | 0.667 | ✅ |
| closure_rule_directed_commit_formed | 1.0 | 0.667 | ✅ |
| gate (a) armed_and_sustained_f_independent | **0.333** | 0.667 | ❌ |
| mech446_around_closure_window_nonvacuous | **0.0** | 0.667 | ❌ |
| — science criteria (mech445 2of3 / mech446 2of3 / co-occurrence 2of3) — | — | — | never reachable |

Per-seed (ON arm):

| Seed | n_f_commits | ncl_hold_closure_armed | sd034_commit_intent | armed+sustained | n_window_events | mean_pre_occ | MECH-445 | MECH-446 |
|---|---|---|---|---|---|---|---|---|
| 42 | 181 | 0 | 0 | no | 0 | 0.0 | ✗ | ✗ |
| 43 | 274 | 0 | 0 | no | 0 | 0.0 | ✗ | ✗ |
| 44 | **7** | **398** | **398** | **yes** | 0 | 0.0 | ✓ | ✗ |

Reference (OFF arm) DID form windows: seed 42 pre_occ 0.7 (n=3), seed 43 pre_occ 0.333 (n=1) — the scorer works; the ON arm specifically vanishes.

**Which criterion failed:** the negative-control / readiness gate (a) and the MECH-446 non-vacuity precondition. The load-bearing science criteria were never reached. This is a **readiness abort, not a falsification.**

## 2. Claim layer

Both MECH-445 and MECH-446 are `candidate` / `v3_pending` / `implementation_phase: v3`, already carrying `epistemic_category: substrate_ceiling` and `pending_retest_after_substrate`. `depends_on`: SD-034, MECH-090, SD-033a (445); + MECH-445, MECH-342 (446). The RE-DERIVE BRAKE fired at 460k. 715 is the **sanctioned retest** cashing in the brake's release condition — build an F-independent closure-plane occupancy substrate — which 460o/p (`use_closure_commit_entry`) delivered.

## 3. Biological-reference triage

Closest mechanism: BG-like commitment gate with closure/completion-triggered de-commitment (SD-034 closure operator + BetaGate commit-entry). Not a pure formal import — grounded in the commit/release cycle. The de-commit **magnitude** DV presupposes a sustained committed occupancy to release from; on the current substrate the F-independent latch only produces that when the F-driven natural commit collapses, and even then it is not temporally aligned with the SD-034 closure fires.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact (MECH-445 narrowly strengthened) | test could not let both children co-express; nothing falsified |
| Biological reference | partial | de-commit presupposes committed occupancy the substrate only makes under weak F |
| Prerequisites / dependency | missing | F-independent arming that survives *moderate* F (= F-dominance ceiling, MECH-439) |
| Implementation | partial → **advance** | 460h/k structural-unreachability RESOLVED; arming now regime-scoped (1/3) |
| Environment | adequate | contact guard 3/3, rule-directed 3/3 |
| Measurement | under-instrumented (ON regime) | MECH-446 window vacuous even on the arming seed — closure fires ⟂ latch occupancy within-episode |
| Integration | partially coupled, unstable | the two children's certifiers do not co-locate (disjointness migrated cross-seed → within-seed) |
| Scale | adequate | 3 seeds; blocker is regime, not budget |

**Recommended `epistemic_category`: `substrate_ceiling`** — but a *partial release*: the old structural-unreachability blocker is gone; the release condition has moved to arming-under-moderate-F + closure-fire co-location.

## 5. The load-bearing finding — substrate partially delivered, signature changed

| | 460h/k (prior 5 iterations) | 715 (now) |
|---|---|---|
| MECH-445 commit-intent | **structurally pinned at 0** — latch source gated on F-driven `e3._committed_trajectory`; `what_would_answer` unreachable by construction | seed 44 = **398** with n_f_commits=7, ncl_hold_closure_armed=398 → **F-independent, no longer pinned** |
| Residual blocker | latch unreachable | (a) arming regime-scoped (survives only weak F); (b) MECH-446 window ⟂ closure fires within-seed |
| Disjoint-certifier | cross-seed (intent on weak-commit seeds, window on strong-commit seeds) | migrated **within-seed** — even the arming seed can't score the de-commit window |

`use_closure_commit_entry` (460o/p) **resolved** the 460h/k structural-unreachability. That is a genuine advance and a narrow non-scoring positive for MECH-445 (existence proof, 1/3 — single seed, weak-natural-commit regime; must NOT be read as a support). The gate still fails, but for two *new* reasons, both traceable to the F-dominance conversion ceiling (MECH-439): the closure latch only gets purchase when F collapses, and the closure fires don't co-locate with the latch-armed occupancy the MECH-446 DV reads.

Verified the window vanishing is **not an instrumentation bug**: `beta_history`/`fire_ticks` reset per episode (script lines 538-539) and align with per-episode `tick_idx`; the OFF arm formed real windows.

## 6. Learning extracted

- 460o/p `use_closure_commit_entry` unpinned MECH-445's commit-intent counter (F-independent arming now demonstrable — seed 44).
- The residual blocker changed signature: structural-unreachability → regime-scoped arming + within-seed certifier disjointness.
- Regime-scoped arming is a residue of the F-dominance conversion ceiling (MECH-439) — the latch only arms when the natural commit is weak.
- 6 iterations, ≥2 distinct signatures circling one claim pair → **granularity debt**.

## 7. Routing (user-confirmed 2026-07-06: "Substrate + claim-synthesis")

**PRIMARY — `/implement-substrate` (governance writes the amend):** amend `substrate_queue.json` entry `f_dominance_conversion_ceiling` (priority 1; already lists MECH-445/446 in `unblocks_claims`; status already flags `decommit_release_duration_face_rung6_460_lineage_readiness_pending`). Add an arming-under-moderate-F lever on the de-commit-release face so the closure-commit-entry latch gets purchase without needing F to collapse, and so SD-034 closure fires co-locate with the latch-armed occupancy the MECH-446 DV reads. Append the 715 failure record. Keep MECH-445/446 `pending_retest_after_substrate`. **Same-claim de-commit-falsifier re-queue REFUSED (re-derive brake remains fired).**

**SECONDARY — `/claim-synthesis` (granularity-debt recurrence trigger):** refer the MECH-445/446 cluster for proposal-first, lit-grounded decomposition — separate the F-independent commit-**INTENT** existence child (narrow positive, seed 44) from the co-located de-commit-**MAGNITUDE** child (structurally unmeasurable on the current substrate). The persistent within-seed certifier disjointness across 6 iterations is the signal that these may be separate mechanisms no single regime co-satisfies. NOT a demotion — the claims aren't wrong, they're coarse.

## 8. Draft `evidence_quality_note` text for governance to write

See the two `recommended_evidence_quality_note_MECH-44{5,6}` fields in the sibling `.json`. Governance applies them; this skill does not touch claims.yaml.

## 9. Verdict summary

- **Failed criterion:** readiness gate (a) 1/3 + MECH-446 non-vacuity 0/3 — a readiness abort.
- **Dominant diagnosis layer:** prerequisite (F-independent arming under moderate F) + measurement (within-seed certifier disjointness).
- **Biological-reference verdict:** partial; not a falsification. Class existence proof intact.
- **Learning:** substrate advance (460h/k blocker resolved) with a new, finer residual + granularity signal.
- **Routing:** implement-substrate (f_dominance_conversion_ceiling amend) + /claim-synthesis referral. Brake stays fired; same-claim re-queue refused.
