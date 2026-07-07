# Failure Autopsy (CLUSTER) -- MECH-445 de-commit cluster: V3-EXQ-715a (M1) + V3-EXQ-717 (M2)

- **Generated:** 2026-07-07T16:37:57Z
- **Scope:** cluster (2 targets, shared claim MECH-445; 715a additionally tags MECH-446)
- **Status:** confirmed (user gate 2026-07-07: 717 -> "Narrow weakens (reliability)"; 715a -> "Confirm as recommended")
- **Lineage:** the two forward moves from `claim_synthesis_MECH-445-446_2026-07-06.md` (STOP verdict + M1-M6 menu), following `failure_autopsy_V3-EXQ-715_2026-07-06`. 715a = **Move M1** (selection-face ceiling-lift, supersedes 715); 717 = **Move M2** (MECH-445-only, test-power decouple).
- **Prior substrate_ceiling autopsies tagging MECH-445:** 6 (460h/i/j/k/l, 715). This cluster is the 7th (715a) and a fair-test resolution (717).

---

## 1. Why a cluster

715a and 717 are the two halves of the claim-synthesis M1/M2 program, both `claim_id: MECH-445`, both testing the same SD-034 closure->beta commit-intent mechanism on the validated `use_closure_commit_entry` substrate, both descending from the 6-iteration 460/715 lineage. The claim-synthesis doc predicted an **asymmetry**: M2 (MECH-445 alone, test-power) was "close" to promotable; M1 (does the selection-face lift double as the de-commit-release substrate?) was "far" (needs a substrate). This cluster **resolves that asymmetry** -- and the resolution is the load-bearing output.

## 2. Facts (no interpretation)

### V3-EXQ-715a -- M1, selection-face lift ON (MECH-445, MECH-446)

- Self-routed `substrate_not_ready_requeue`; `route_reason: lift_engaged_but_arming_still_regime_scoped`; `evidence_direction: unknown` per-claim (both), `non_degenerate: false` (scoring-excluded).
- Readiness legs: contact-guard PASS (1.0), rule-directed PASS (1.0), **lift_engaged PASS (1.0, 3/3)** -- the MECH-448 demotion + MECH-449 Go/No-Go DID engage (not the 485i all-admit), off_did_not_arm PASS. **armed_and_sustained FAIL (0.333, 1/3)** <- the failing leg. within_window_nonvacuous FAIL (0.0).
- Science arm `ARM_LIFT_ON_ENTRY_ON` per seed: seed 42 armed (commit_intent 28) window vacuous (0 events); seed 43 no arm, no window; seed 44 no arm but the only non-vacuous window (pre 1.0 -> post 0.2, valid drop). **Arming (seed 42) and the MECH-446 window (seed 44) land on disjoint seeds** -- empty intersection, reproducing the 460h/k/715 pattern.
- **moderate_f_delta_entry_on = -63.0** (positive = lift reduced F-commits): the lift did NOT moderate F into the arming band; science-arm mean F-commits 407 vs repro-715 arm 344.

### V3-EXQ-717 -- M2, MECH-445-only, 12 seeds, decoupled (MECH-445)

- `outcome: FAIL`; **`evidence_direction: weakens`** (per-claim MECH-445); **`non_degenerate: true`**; route_reason `readiness_met_but_commit_intent_below_2of3_on_in_regime_subset`. **A genuine fair test, not a self-route.**
- Readiness all cleared: contact guard 12/12; weak-natural-commit regime populated (9 in-regime >= 3); commit-intent opportunity 1.0. So the science gate was **scorable**.
- Science: commit-intent counter > 0 on **2 of 9 in-regime seeds** (seeds 46=222, 52=195; a third armed seed 47=177 fell out-of-regime) -> fraction 0.222 < 0.667 -> FAIL / weakens on the single load-bearing criterion.
- In-regime classification uses the OFF-arm (`ARM_ENTRY_OFF`) committed_frac <= 0.15 -- a different arm and quantity than the scored ON-arm counter (non-circular). 9 in-regime, 3 strong (43, 47, 51).

## 3. Claim-layer mapping

- **MECH-445** (`mechanism_hypothesis`, `candidate`, `v3_pending`, `epistemic_category: substrate_ceiling`; depends_on SD-034, MECH-090, SD-033a). `what_would_answer`: SUPPORTED if the refractory-independent commit-intent counter > 0 on >= 2/3 in-regime (weak-commit) seeds. Prior narrow non-scoring positives: 715 seed 44 = 398 commit-intents (F-independent), 460h seed 44. No prior weakens; all prior iterations non_contributory / substrate-blocked.
- **MECH-446** (`mechanism_hypothesis`, `candidate`, `v3_pending`, `epistemic_category: substrate_ceiling`; depends_on SD-034, MECH-090, MECH-445, MECH-342). `what_would_answer`: within-arm post-closure occupancy below pre-closure by >= DECOMMIT_MIN_DROP_FRAC on >= 2/3 seeds. 715a only tags MECH-446 via the joint gate; its window was vacuous on all ON-arm seeds again.

**Did the tests let the claims express?**
- 715a: NO for the joint gate -- readiness aborted (arming 1/3); the science criteria were never reachable. Non-scoring.
- 717: YES for MECH-445 existence -- readiness cleared, adequate power (9 in-regime), opportunity present, counter placed before the refractory gate so MECH-446's magnitude lever cannot zero it. This is the fairest MECH-445 existence test to date.

## 4. Biological-reference triage

- **Closest mechanism:** BG-like commitment gate with closure/completion-triggered commit-entry (SD-034 closure operator + MECH-090 bistable latch, `use_closure_commit_entry`). Grounded, not a formal import.
- **Dependency:** a closure fire must co-locate with a sustained committed occupancy that arms F-independently and survives moderate F. In real BG the completion-triggered commitment is reliable across contexts; in REE it arms only in the rare regime where the F-driven natural commit is weak.
- **Missing-dependency signature?** Yes. Both 715a (arming 1/3 despite the lift) and 717 (2/9 in-regime armed) show the F-independent arming is REAL but RARE -- exactly what you would see if the closure->beta coupling is correctly built but the substrate does not reliably produce armed-and-sustained closure commits outside the weak-F regime. The selection-face lift moderating F did NOT rescue arming (delta -63) -> the arming reliability gap needs a **distinct** de-commit-release lever, not more F-moderation.

## 5. Four-layer diagnosis (per target)

### 715a (M1) -- substrate_ceiling / non_contributory (non-scoring)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | readiness abort; joint gate never scorable; NO-weakens |
| Biological reference | partial | closure-triggered commitment; arming reliability is the missing dependency |
| Prerequisites | missing | F-independent arming that survives moderate F; closure-fire co-located with latch-armed occupancy |
| Implementation | live-but-insufficient | the selection-face lift (MECH-448/449) engaged 3/3 but did NOT double as the de-commit-release substrate (arming 1/3, moderate_f_delta -63) |
| Environment | adequate | full curriculum; contact/rule-directed 3/3 |
| Measurement | under-instrumented (ON regime) | MECH-446 window vacuous again; arming and window on disjoint seeds |
| Integration | partially coupled, unstable | commit-intent latch and closure-fire de-commit window do not co-locate within-seed |
| Scale | adequate | 3 seeds; blocker is regime + missing lever, not budget |

### 717 (M2) -- narrow weakens (reliability reading of MECH-445)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened (narrow) | fair test: existence PROVEN (2/9 + prior 398-count) but the 2/3 RELIABILITY bar failed |
| Biological reference | partial | mechanism fires F-independently when armed; reliability across the weak regime is the gap |
| Prerequisites | missing | reliable arming across weak-regime seeds (same de-commit-release lever as 715a) |
| Implementation | complete | `use_closure_commit_entry` ON; counter placed before refractory gate; 12-seed power adequate |
| Environment | adequate | contact guard 12/12; 9 in-regime seeds |
| Measurement | adequate | test-power hole from 715 (3-seed/2-of-3) fixed; fair scorable gate |
| Integration | isolated (by design) | MECH-446 dropped; MECH-445 tested alone |
| Scale | adequate | 12 seeds -> 9 in-regime; power sufficient to certify a regime-scoped claim |

## 6. Cluster pattern (Step 6)

| Experiment | Claim | Readiness / absolute criterion | Discrimination / science criterion | Read |
|---|---|---|---|---|
| 715a (M1) | MECH-445 + MECH-446 | lift engaged 3/3 (PASS); armed_and_sustained 1/3 (FAIL) | joint co-occurrence unreachable (readiness abort) | selection-face lift does NOT double as de-commit-release substrate; distinct lever needed |
| 717 (M2) | MECH-445 | readiness cleared 3/3 legs (PASS) | commit-intent 2/9 in-regime (FAIL, fair) | F-independent existence proven but sub-2/3-reliable within the weak regime |

**Not N independent bugs -- one structural property with two faces.** Both targets converge on the same root: **F-independent closure->beta commit-intent arming is real but unreliable, and the reliability gap is not fixed by moderating F at the selection face (715a: delta -63) -- it needs a distinct arming-under-moderate-F / closure-co-location lever on the de-commit-release face.** 715a establishes the substrate need directly (non-scoring diagnostic); 717 quantifies the reliability gap as a fair weakens (2/9). Together they are the M1/M2 resolution the claim-synthesis predicted: M2 was close and resolved to a narrow weakens on reliability; M1 was far and confirmed the distinct-lever substrate need.

## 7. Re-derive brake (MOVE-3)

**FIRED for the substrate-ceiling face (715a).** MECH-445 already carries 6 prior substrate_ceiling autopsies (460h/i/j/k/l, 715); 715a is the 7th substrate_not_ready reading. **REFUSE** any further same-claim de-commit-MAGNITUDE / co-occurrence / joint-gate re-queue against the current substrate -- route to `/implement-substrate`.

**717 is exempt from the brake** -- it is a *fair test that produced a real weakens*, not a same-selector substrate-ceiling re-derive. Its narrow weakens is applied to MECH-445 (see routing). But its finding (the reliability gap) routes to the SAME implement-substrate work.

**Route (both targets):** `/implement-substrate` on `f_dominance_conversion_ceiling` -- the **de-commit-release face**: a distinct lever that produces F-independent arming surviving moderate F, with the SD-034 closure fire co-located with the latch-armed occupancy (so the MECH-446 window is non-vacuous). This confirms and sharpens the primary route of `failure_autopsy_V3-EXQ-715_2026-07-06` and the claim-synthesis Section-6 hand-off. The moderate-F selection-face lift is now RULED OUT as that lever (715a delta -63).

## 8. Draft `evidence_quality_note`s (governance to write; NOT written here)

**MECH-445:**
> V3-EXQ-717 (confirmed failure_autopsy_MECH-445-cluster-715a-717_2026-07-07; M2 test-power decouple, 12 seeds) -> WEAKENS (NARROW, reliability-scoped). Fair test: readiness cleared, 9 in-regime seeds, opportunity 1.0, counter placed before the refractory gate. Commit-intent > 0 on 2/9 in-regime seeds (46=222, 52=195) < 2/3 -> the F-independent commit-intent EXISTS (this + prior 715 seed-44=398 are existence proofs) but does NOT clear the 2/3 RELIABILITY bar within the weak-natural-commit regime. This weakens the RELIABILITY/PREVALENCE reading only; the existence claim stands. Status UNCHANGED (candidate / v3_pending); does NOT flip to weakened-overall. Paired with V3-EXQ-715a (M1, confirmed same autopsy) -> non_contributory: the selection-face lift engaged 3/3 but arming stayed 1/3 with moderate_f_delta -63, so moderating F does NOT rescue arming; a DISTINCT de-commit-release lever is needed. 7th substrate-ceiling reading (715a); RE-DERIVE BRAKE FIRED; same-claim de-commit-MAGNITUDE re-queue REFUSED. Reliability gap release condition: f_dominance_conversion_ceiling de-commit-release face (F-independent arming surviving moderate F).

**MECH-446:**
> V3-EXQ-715a (confirmed failure_autopsy_MECH-445-cluster-715a-717_2026-07-07; M1 selection-face lift) -> non_contributory + pending_retest_after_substrate (status UNCHANGED: candidate / v3_pending). Self-routed substrate_not_ready_requeue (lift_engaged_but_arming_still_regime_scoped): the within-arm around-closure occupancy window was VACUOUS on all ON-arm seeds again -- arming (seed 42) and the only non-vacuous window (seed 44, pre 1.0 -> post 0.2) landed on disjoint seeds. The selection-face lift did NOT co-locate the closure fire with a sustained latch-armed occupancy. NOT a falsification, NOT scorable -- the MECH-446 DV is starved. 7th substrate-blocked iteration; RE-DERIVE BRAKE FIRED; same-claim re-queue REFUSED. Release condition: a de-commit-release lever where the SD-034 closure fire co-locates with a sustained latch-armed occupancy across >= 2/3 seeds (f_dominance_conversion_ceiling de-commit-release face). The moderate-F selection-face lift is RULED OUT as that lever (moderate_f_delta -63).

## 9. Routing summary

- **MECH-445:** narrow weakens (717, reliability reading) + non_contributory context (715a); status UNCHANGED (candidate / v3_pending); existence proof preserved; brake FIRED; same-claim de-commit re-queue REFUSED.
- **MECH-446:** non_contributory (715a); status UNCHANGED; brake FIRED; re-queue REFUSED.
- **Substrate:** amend `f_dominance_conversion_ceiling` de-commit-release face with the cluster failure record + "distinct arming-under-moderate-F lever; selection-face lift RULED OUT" hint. `/implement-substrate` owns the build.
