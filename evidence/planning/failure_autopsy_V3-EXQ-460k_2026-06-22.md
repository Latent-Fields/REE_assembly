# Failure Autopsy — V3-EXQ-460k (natural-commit occupancy-release de-commit falsifier)

- **run_id:** `v3_exq_460k_natural_commit_occupancy_release_decommit_falsifier_20260622T191736Z_v3`
- **queue_id:** V3-EXQ-460k  (supersedes V3-EXQ-460j)
- **claims:** MECH-445 (closure->beta coupling engagement), MECH-446 (de-commit-authority magnitude)
- **outcome:** FAIL — self-route `substrate_not_ready_requeue`, `evidence_direction: non_contributory`
- **scope:** single (lineage member 460d->k; 8th+ de-commit-falsifier iteration)
- **generated_utc:** 2026-06-23T03:57:45Z
- **status:** confirmed (user interactive gate, 2026-06-22T/23 walk)
- **routing:** implement-substrate (amend `f_dominance_conversion_ceiling`); **re-derive brake FIRED** — same-claim de-commit-falsifier re-queue REFUSED.

---

## 1. Facts (no interpretation)

- 3/3 guard seeds PASSED contact non-vacuity (`p2_contact_rate` 0.23-0.34, `z_goal_norm_at_contact_peak` > 0.41) and rule-bias-trained. **The substrate is trained and foraging-competent.**
- The NEW gate-2.5 precondition `closure_exclusive_eval_armed_hold` measured **0.0 (UNMET)**: `ncl_hold_closure_armed_total == 0` AND `ncl_hold_reassert_total == 0` on **every arm, every seed** (ARM_LEVER_OFF / ARM_GAP_SCALED / ARM_FLAT_RATE / ARM_ACTION_EXTENT, seeds 42/43/44).
- Consequently `off_baseline_sustained_natural_commit_hold = 0.0`, `mean_per_commit_hold = 1.0` and `max_consecutive_beta_run = 1` everywhere (the 460i fragmentation regime persists), `lever_shortened_occupancy = 0/3`, `coupling_nonvacuity = 0/3`, `within_window = 0/3`. The de-commit DV never scored.
- Both load-bearing criteria are degenerate: `CO_OCCURRENCE_gap_scaled_mech445_and_mech446 = False` (non_degenerate False), `D1_graded_beats_fixed_refractory = False` (non_degenerate False).
- Closures ARE present: `n_closures` 5-8 / arm, `n_hook_fires` 5-8, `n_sequence_completions` 5-8 (Leg-A env-completion hook fires). But `sd034_n_closure_commit_intent == 0` everywhere.
- `route_reason = closure_exclusive_eval_did_not_arm_hold`.

**Which criterion failed:** a precondition / non-vacuity gate (gate-2.5 closure-exclusive-eval-armed-hold). No discrimination criterion ever ran. This is a clean readiness self-route, not a claim test.

## 2. Claim-layer mapping

Both MECH-445 and MECH-446 are `mechanism_hypothesis`, `status: candidate`, `epistemic_category: standard`, `implementation_phase: v3`, `v3_pending: true`, `pending_retest_after_substrate: true`. Promotion is held by `v3_pending` regardless of this run.

The experiment did **not** test either claim under conditions where it could express itself — the DV is downstream of the gate-2.5 precondition, which was never met. Correctly `non_contributory`; **neither claim is weakened.**

**The clincher — the claim's predicate is structurally unreachable on the current substrate.** MECH-445's `what_would_answer` defines support as *"a refractory-independent commit-intent counter (closure-plane `e3._committed_trajectory` forming **while not** `result.committed`) is > 0."* In the current code `e3._committed_trajectory` is set in exactly one place — `e3_selector.py:1926` `if committed: self._committed_trajectory = selected_trajectory` — i.e. **only when the F-driven natural commit fires.** There is no code path that populates it without `committed` being True. So "closure-coupled committed trajectory forming while not committed" is a contradiction in the current substrate, and the MECH-445 commit-intent counter is pinned at 0 **by construction**.

## 3. Biological-reference triage

- Closest reference: basal-ganglia committed-motor-program maintenance + graded pallidal/urgency de-commit (Thura & Cisek 2022; Jin 2014). `lit_status: present`.
- Not a formal-definition import; the levers are tuned renderings of graded-urgency duration timing.
- The biological reference is **not the failing layer** — the failure is a missing substrate dependency (a closure-coupled commitment that forms independently of the F-driven natural commit), exactly what would happen biologically if the closure/sequence-completion signal had no pathway to engage the commit latch. The failure matches a missing-dependency signature, not a falsification.

## 4. The wiring-vs-ceiling adjudication

The same-day build `closure_exclusive_decommit_eval` (ree-v3 `e52158d`, 2026-06-22) moved the latch-hold arm SOURCE from `result.committed` (460j) to `_closure_commit_active`:

```
_closure_commit_active = use_closure_commit_beta_coupling AND e3._committed_trajectory is not None
_ncl_closure_arm       = closure_exclusive_decommit_eval AND _closure_commit_active AND beta_gate.refractory_remaining == 0
hold arms iff use_natural_commit_latch_hold AND (result.committed OR _ncl_closure_arm)
```

But `_closure_commit_active` is gated on `e3._committed_trajectory is not None`, which (section 2) is set ONLY by the F-driven natural commit. So the "closure-exclusive" arm is, two hops down, gated on the **same fragile natural commit that 460j found never forms on this substrate.** The intended natural-commit <-> closure-de-commit dissociation is **illusory**.

The build's green activation signal (`closure_armed=1, reassert=8`) is a **false positive**: the contract test `_tick` helper directly injects `agent.e3._committed_trajectory = cands[0]` (`tests/contracts/test_closure_exclusive_decommit_eval.py:117`), bypassing the real commit path. The contract never exercises whether the closure plane can *produce* a committed trajectory on the real substrate, so it cannot catch this class of failure (a test-adequacy gap that let a same-day build look ready).

**This is NOT the V3-EXQ-642 pattern** (there P0 was simply untrained — a transient artifact correctly routed to re-queue). Here all guard seeds trained fine and the non-arm is **structural**: the closure->committed-trajectory path does not exist in code. Re-queuing after a "wiring fix" cannot help — making `_closure_commit_active` fire on weak-natural-commit seeds requires a NEW substrate path (a closure-coupled committed-trajectory / sustained occupancy independent of the F-driven commit). That is substrate construction. **Genuine substrate ceiling.**

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | MECH-445/446 never tested; DV gated out. Correctly non_contributory, never a weakens. |
| Biological reference | clear | BG commit-latch + graded de-commit (Thura/Cisek; Jin). Not the failing layer. |
| Prerequisites | missing | A closure-coupled committed-trajectory occupancy that forms INDEPENDENTLY of the F-driven natural commit. Does not exist in code. |
| Implementation | stub (symbol-not-role) | Eval arms on `_closure_commit_active`, but that symbol resolves to the same F-driven `committed`. Symbol of dissociation without its function. |
| Environment | adequate | Closures fire (5-8/arm); foraging substrate fine. |
| Measurement | adequate | The gate-2.5 arm certifier correctly caught the non-arm and self-routed (instrument working as designed; same class of redesign-win as 460j's gate-3). |
| Integration | isolated | Closure plane and the natural-commit latch never couple — the missing path. |
| Scale | not the issue | 240-ep budget already tried up-lineage. |

Recommended epistemic_category: **substrate_ceiling** (V3-tractable in principle, but the substrate is too coarse to deliver the needed closure->commit distinction; the right response is substrate enrichment, not more experiments on the existing substrate).

## 6. Lineage / re-derive brake

Prior `substrate_ceiling`/`non_contributory` autopsies tagging MECH-445 AND MECH-446: **460h, 460i, 460j** (3). This autopsy (460k) is the **4th** — `RE_DERIVE_BRAKE_THRESHOLD = 2`, exceeded.

The failure has stayed the SAME ceiling, letter after letter, each "fix" only relocating the arm source without escaping the dependency on the F-driven natural commit:
- 460h: disjoint-certifier (commit-intent and occupancy-drop never co-occur)
- 460i: off-baseline fragmentation (~35 re-commits/episode; no sustained occupancy)
- 460j: latch-hold armed on `result.committed`, which never forms -> reassert 0/armed 0
- 460k: latch-hold armed on `_closure_commit_active`, which is gated on `e3._committed_trajectory`, set only by the same `committed` -> armed 0/reassert 0

This is the re-derive brake's exact target (same granularity, same substrate ceiling) — **not** granularity debt requiring claim decomposition (the claim isn't coarse; it's blocked on a substrate capability that doesn't exist). **Brake FIRES:** route implement-substrate; **REFUSE** another de-commit-falsifier letter (no 460m on this substrate). A redesign that tests a *different* mechanism (new EXQ number, different claim_ids) is still allowed.

> Note: V3-EXQ-460l in the ree-v3 queue is the ARC-108 JOB-2 control-plane (rho ramp + habenula) falsifier — a DIFFERENT mechanism, brake-exempt, NOT a successor to this de-commit lineage. It inherits the same unmet eval-arm precondition and carries its own non-vacuity self-route for it; expect it to self-route substrate_not_ready on the same arm-gate until the substrate path below is built.

## 7. Learning extracted

1. The closure-exclusive eval mode did NOT achieve the intended dissociation: its arm source `_closure_commit_active` is gated on `e3._committed_trajectory`, set only by the F-driven `committed` (`e3_selector.py:1926`). Relocating the arm source (460j -> 460k) cannot escape the F-driven commit dependency.
2. MECH-445's testable predicate ("closure-plane `e3._committed_trajectory` forming while not `result.committed`") is structurally unreachable on the current substrate — the commit-intent counter is pinned at 0 by construction, which is *why* 460h->k all self-route substrate_not_ready.
3. Test-adequacy gap: the activation/contract test reports `closure_armed=1` only because `_tick` directly injects `e3._committed_trajectory`. A contract that mocks the arm source cannot certify that the real substrate produces a closure-coupled commitment — a future substrate build must add a contract that drives arming through the real commit path (or explicitly document the mock).
4. The substrate work needed is sharp: a path where the SD-034 closure / env-completion plane sets a committed-trajectory-equivalent sustained occupancy WITHOUT requiring the F-driven `committed` threshold. Until it exists, no de-commit-falsifier letter can move MECH-445/446.

## 8. Routing decision (user-confirmed)

- `evidence_direction: non_contributory` CONFIRMED for MECH-445 + MECH-446 (NOT weakened). `pending_retest_after_substrate: true`.
- **Recommend governance set `epistemic_category: substrate_ceiling` on MECH-445 and MECH-446** (user-confirmed at the gate) — the durable signal that the response is substrate enrichment, not re-testing; promote/demote and narrow_open_question suppressed.
- **Routing: implement-substrate**, amend `f_dominance_conversion_ceiling` (already owns the SD-034 closure-de-commit / commit-release-duration face since 460h).
- **Re-derive brake FIRED:** no same-claim de-commit-falsifier re-queue.

### Draft `evidence_quality_note` (for governance to write — not written here)

> V3-EXQ-460k (2026-06-22, failure-autopsy): non_contributory CONFIRMED for MECH-445 + MECH-446 (NOT weakened). 4th substrate-blocked iteration of the de-commit falsifier (460h/i/j/k); RE-DERIVE BRAKE FIRED (threshold 2). The same-day closure_exclusive_decommit_eval build (ree-v3 e52158d) moved the latch-hold arm source to `_closure_commit_active`, but that is gated on `e3._committed_trajectory`, set ONLY by the F-driven natural commit (e3_selector.py:1926) — so the intended natural-commit/closure-de-commit dissociation is illusory and the gate-2.5 closure-exclusive-eval-armed-hold measured 0/3 (ncl_hold_closure_armed_total==0 all arms/seeds). The build's green activation test (closure_armed=1) is a false-positive: the contract harness injects e3._committed_trajectory directly. MECH-445's own predicate (closure-plane committed-trajectory forming while not result.committed) is structurally unreachable on the current substrate, so the commit-intent counter is pinned at 0 by construction. Recommend epistemic_category: substrate_ceiling. Release condition: a substrate path where the SD-034 closure/env-completion plane forms a committed-trajectory-equivalent sustained occupancy INDEPENDENTLY of the F-driven natural commit. pending_retest_after_substrate. Same-claim de-commit-falsifier re-queue REFUSED (brake).
