# Failure Autopsy: Fresh 2026-08-08 items (878a, 812a, 703a), 3 targets

**Generated:** 2026-08-08T19:37:15Z
**Scope:** cluster (fresh un-autopsied FAILs/diagnostics landing 2026-08-08, alongside the day's grandfathered-backlog sweep)
**Status:** confirmed (Step 8: SD-032c reconciliation flagged rather than accepted; 812a held for code-level inspection)

## Coverage note

Of 8 fresh 2026-08-08 targets identified via `pending_review.md`, **5 were already autopsied by other parallel sessions the same day** (897/SD-009, 894a/MECH-074d, 898/SD-016, 901/INV-051, 821b/MECH-457) — not duplicated here. This file covers the remaining 3.

## v3_exq_878a_mech332_commitment_calibration — 4th independent hit on an untagged blocker, and a reconciliation flag

18-cell budget sweep (3 training schedules × 2 AIC-active arms × 3 seeds): every cell shows `n_committed_steps=0`, `running_variance_mean_fresh` pinned exactly at `precision_init` (0.5), never moving toward the 0.40 commit threshold even at 3× budget. This is the **4th** independent experiment (EXQ-325, EXQ-321, EXQ-878, EXQ-878a) across ~4 months reconfirming the identical E3-commitment-gate blocker, never formally tagged `substrate_ceiling`.

**Cross-check finding, explicitly requested**: this complicates, rather than confirms, round 4's `mech102-sd021-novelty-pain-cluster` finding that SD-032c is "newly unblocked" because its cited blocker (ARC-065) resolved 2026-06-17. Claims.yaml's current text for SD-032c (re-verified same day) names a *different* precondition — MECH-269 V_s landing, still unlanded — and ARC-065's actual fix (top-k shortlist routing of candidate diversity) is a logically distinct mechanism from both MECH-269 and this run's blocker (whether commitment happens at all). **Step 8 (user-confirmed, recommended option): flag for governance reconciliation across all three documents** rather than act on round 4's finding as-is.

## v3_exq_812a_mech295_cue_authority_sd054 — harness fix partially worked, exposed a second degeneracy

Successor to the confirmed V3-EXQ-812 autopsy (INVALID_HARNESS, proximity exactly 0.0 everywhere). The documented fix (`candidate_summary_source='e2_world_forward'`) is source-verified applied and partially worked — 2/3 seeds still exact zero, the third shows a sub-floor nonzero value not distinguishable between arms. A **second, unconditional degeneracy** newly exposed: `liking_bias_range` is exactly 0.0 in all 6 cells regardless of whether upstream proximity showed variance — a separate defect at the downstream bias-computation stage. The self-route label `INVALID_HARNESS`, carried over verbatim from the predecessor, is a partial mislabel — the signature materially changed. **Step 8 (user-confirmed, recommended option): hold for code-level inspection of `mech295_liking_bridge.py`'s bias-computation function** before any re-queue — this lineage has already cycled "fix one bug, hit another" roughly 5 times (490g→k→631→812→812a).

## v3_exq_703a_mech276_scientist_attribution_readiness — clean positive unlock, correctly non-promoting

Applies the confirmed V3-EXQ-703 autopsy's exact re-queue spec. Outcome PASS with real margin (R1 need-th-largest R²=0.557, 2.8× the floor) and a substantive discrimination criterion — not vacuous. One caveat: R2 clears at exactly the 2/3-seed minimum with seed 7 excluded entirely; a single additional seed failure next time would flip this. `claim_ids=[]` deliberately — correctly does not promote MECH-275 or MECH-276.

**Directly load-bearing downstream consequence**: `sleep_substrate_plan.md`'s GAP-3b explicitly deferred adding MECH-275 to V3-EXQ-702's `unblocks_claims` pending "the UNBUILT MECH-276 counterfactual-backed-attribution feedstock." This run's PASS is exactly that unlocking event, and the manifest's own notes field states so.

## Cross-cutting finding: MECH-269 as a shared chokepoint

MECH-269 (hippocampal proposer anchor selection / V_s landing, still `v3_pending`) blocks at least two independent research threads surfaced today: SD-021/SD-032c (via 878a) and MECH-276→MECH-275 (via 703a's dependency list). Worth flagging as an `implement-substrate` priority candidate independent of either single autopsy — this is a lower bound, not an exhaustive sweep.

## Biological-reference triage

878a and 812a both have solid, present biological grounding (PAG/RVM descending analgesia; liking→approach cue-bias bridge). 703a/MECH-276 has no dedicated literature review — a formal-definition import (Pearl-style counterfactual construct) with no specific circuit named. Not urgent for this readiness diagnostic, but a genuine `/lit-pull` gap if MECH-276 itself is queued next.

## Re-derive brake state

878a: mechanical count 0 (never formally tagged), but treated as brake-territory in spirit given 4 independent hits. 812a: MECH-295 already `substrate_ceiling` with ~20 prior confirmed autopsies — brake fired, refused re-queue pending code inspection. 703a: not applicable (claim-free, positive result).

## Recommended routing summary

All three: `governance-note-only`. 878a needs a reconciliation pass, not a build. 812a needs code-level inspection before any further routing. 703a's routing is really for governance to update `sleep_substrate_plan.md` GAP-3b and both claims' evidence_quality_notes.

## Learning extracted

1. A self-route label or a prior round's disposition, inherited verbatim by a successor run, can mislabel what actually changed — both 878a (SD-032c blocker citation) and 812a (INVALID_HARNESS label) needed re-derivation from the current run's own data rather than trusting the inheritance.
2. `claim_ids=[]` discipline held correctly in 703a — a clean PASS did not get promoted into claim credit it wasn't designed to carry, while still being recognized as load-bearing for a *different*, dependent claim's blocker status.
3. MECH-269 recurring as a named blocker across two unrelated threads on the same day is a useful cross-autopsy signal that a single-thread view would have missed.
