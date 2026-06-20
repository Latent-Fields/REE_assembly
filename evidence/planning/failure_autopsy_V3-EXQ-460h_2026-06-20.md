# Failure Autopsy -- V3-EXQ-460h (SD-034 closure de-commit; refractory-INDEPENDENT commit-intent retest; FIRST evidence for MECH-445 + MECH-446)

- **Generated / confirmed:** 2026-06-20T08:33:34Z
- **Status:** confirmed (interactive gate; user AskUserQuestion 2026-06-20)
- **Scope:** single target, adjudicated under a **cluster lens** (user-directed: "look at all four recent failures as a cluster and consider F-dominance conversion ceiling"). 8th autopsy in the SD-034 closure lineage; **first** autopsy of the re-grained children MECH-445 / MECH-446.
- **Predecessor:** `failure_autopsy_V3-EXQ-460g_2026-06-19` (confirmed; drove the /claim-synthesis decomposition `claim_synthesis_SD-034-closure_2026-06-19.md`). Lineage: 460b-cluster -> SD-034-cluster(+ext) -> control-plane-d -> 460e -> 460f -> 460g -> **460h**.
- **Run:** `v3_exq_460h_sd034_decommit_refractory_independent_20260620T014714Z_v3` (machine ree-cloud-4). FAIL, `evidence_direction: non_contributory`, self-route `substrate_not_ready_requeue`, route_reason `closure_coupling_not_engaged`.
- **Claims:** MECH-446 (scored), MECH-445 (coupling-engagement precondition). MECH-260/MECH-261 NOT tagged (correct; see below).

---

## One-line verdict

The 460h refractory-independent commit-intent fix **worked at the instrumentation level** -- it is no longer zeroed by the de-commit-magnitude lever (seed 44 reports `sd034_n_closure_commit_intent=375`, exactly where 460g's same-seed coupled-elevation counter collapsed 36->0). But the run still self-routes because the **two non-vacuity certifiers now fire on disjoint seeds**: the closure-coupling certifier (commit-intent) fires only where the natural F-driven commit is weak (seed 44), while the within-arm de-commit window has power only where the natural commit is strong (seed 42). **Their intersection across the three seeds is empty**, so the load-bearing C2 DV (MECH-446) can never be scored on a MECH-445-coupling-certified seed. This is **not a falsification** (existence proofs for both children) and **not a substrate ceiling** (the substrate carries and expresses both on their respective seeds). The self-route is correct and conservative.

**The load-bearing output (cluster lens):** 460h is fresh evidence that the SD-034 de-commit is **NOT orthogonal** to the F-dominance conversion ceiling (the standing `conversion_ceiling_phase0_synthesis_2026-06-18.md` classification of root C as "OPEN, ORTHOGONAL"). The closure-coupled de-commit is a **modulatory channel subdominant to the F-driven natural commit** -- measurable only where the F-driven commit is weak (seed 44, OFF-arm committed_steps = 0). That is the same "every modulatory channel drowns at the F-dominated commitment" shape as root B, surfacing one layer down at the **commit/release-duration** face of the latch rather than the candidate argmax. Recommended routing therefore reclassifies root C under the F-dominance front and **gates the 460i de-commit retest on the F-dominance commit-decisiveness lever**, not a bespoke SD-034 eval hack.

---

## Facts reconstruction

### Readiness gates (2 of 5 fail -- the load-bearing disjoint pair)

| Gate | measured | threshold | met |
|---|---|---|---|
| foraging_contact_guard | 1.0 | 0.667 | yes |
| rule_bias_head_trained (Leg C) | 1.0 | 0.667 | yes |
| **closure_coupling_nonvacuous_refractory_independent** (ON `sd034_n_closure_commit_intent > 0` AND `n_sequence_completions > 0`) | **0.333** | 0.667 | **NO** |
| closure_trigger_available (n_closures > 0) | 1.0 | 0.667 | yes |
| **within_arm_window_nonvacuous** (>= 2 scored windows, mean_pre_occ > floor) | **0.333** | 0.667 | **NO** |

`criteria_non_degenerate` = {C1 false, C2 false, C3 false}; per-seed criteria pass `[true, false, false]`; `mech261_exercised` false; route_reason `closure_coupling_not_engaged`. The run self-routed at the readiness preconditions **before C2 (the MECH-446 scored DV) was scored** -- this is a `precondition_unmet` adjudication, not a fair C2 FAIL.

### Per-seed ARM_CLOSURE_ON -- the disjoint-seed dissociation

| seed | OFF committed_steps | ON commit_intent (460h gate) | ON coupled_elev (460g gate) | n_window_events | mean pre->post occ | C2 within | coupling certified | window non-vacuous |
|---|---|---|---|---|---|---|---|---|
| 42 | **2414** (strong natural commit) | **0** | 0 | 2 | 0.333 -> 0.0 | **PASS** | no | yes |
| 43 | **2609** (strong) | **0** | 0 | 0 | 0.0 -> 0.0 | FAIL | no | no |
| 44 | **0** (no natural commit) | **375** | 375 | 1 | 0.333 -> 0.0 | FAIL (1 < 2 windows) | **yes** | no |

The OFF-arm `committed_steps` column is the diagnostic key: it reports each seed's **natural (F-driven) commit strength**. commit-intent > 0 occurs on exactly the seed (44) whose OFF arm never commits.

### Why commit-intent still fires only 1/3 (the central question)

`note_closure_commit_intent` increments on `_closure_commit_active AND not result.committed` -- it counts closure-plane commitments that occur **without** a concurrent natural commit, BEFORE the elevate/refractory gate. The refractory-independent fix is real: on seed 44 the counter reports 375 where 460g's coupled-elevation counter (counted *inside* the elevate if-block, guarded by `not is_elevated`) was pinned to 0 by the 60-tick refractory cap. So the 460g self-defeat (S5) is broken.

The residual reason is **regime coverage, not a broken certifier**: commit-intent by construction only counts closure coupling that does work the natural path would not have. That regime exists only on the **weak-natural-commit** seed (44, OFF committed_steps = 0). On seeds 42/43 the agent reaches commitment via the natural running_variance path (OFF committed_steps 2414/2609), so the closure-plane commitment **co-occurs with** a natural commit rather than substituting for it -- `not result.committed` is False, nothing increments. The counter is correctly reporting that 2/3 seeds are **outside the regime MECH-445 is defined for** ("on seeds where the agent does not naturally commit decisively, the closure still drives a latch elevation").

### The binding fault: anti-correlated, disjoint certifiers

- **commit-intent > 0** requires **weak** natural commit (closure coupling does independent work) -> seed 44.
- **n_window_events >= 2** requires **rich** committed runs with pre-closure latch occupancy -> seed 42.

These are **anti-correlated by construction**: the closure coupling engages precisely when the natural commit is weak, but a weak-natural-commit agent produces sparse closures / short occupancy and hence few scorable around-closure windows. The intersection {coupling certified AND window non-vacuous} is **empty** across all three seeds:
- seed 42: window OK (2), coupling NOT (0)
- seed 44: coupling OK (375), window NOT (1)
- seed 43: neither

So MECH-446's C2 (within-arm post-closure occupancy drop) can never be scored on a MECH-445-coupling-certified seed. And where C2 *does* pass (seed 42, 0.333 -> 0.0) it cannot be **attributed** to the closure-coupled de-commit because the agent naturally commits there -- the drop could be the natural-commit release.

### Existence proofs (narrow non-scoring positives)

- **MECH-445** (coupling engagement): seed 44, commit_intent = 375 with OFF-arm committed_steps = 0 -> the closure coupling is the **sole** commit driver (ON total_beta_elevated = 355 vs OFF = 0). Positive, 1/3.
- **MECH-446** (de-commit magnitude): seed 42, within-arm 0.333 -> 0.0 (C2 PASS) -> correct de-commit sign + magnitude. Positive but on a coupling-uncertified seed, 1/3.

### claim_ids accuracy: MECH-261 not exercised (unchanged)

`n_automatic_fires = 0` on all three seeds; every closure is hook-driven (`n_hook_fires == n_closures`). Mode-conditioning is bypassed; MECH-261 correctly NOT tagged (protects the stable claim, EXQ-048/MECH-057b inherited-tag class). MECH-260 also not re-tagged (No-Go is reported diagnostic only; already a narrow supports in 460f/g).

---

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact (both children)**; seed-44 strengthens MECH-445, seed-42 strengthens MECH-446 | neither weakened; the 2/3 commit-intent zeros are out-of-regime (strong natural commit), not falsifications |
| Biological reference | clear | Collins & Frank 2014 / Smith & Graybiel 2013 (closure drives the committed program off); Mayr & Keele 2000 (post-completion refractory magnitude). The failure resembles measuring a backup mechanism (closure coupling) on subjects whose primary (natural commit) already reaches commitment -- redundant, not broken |
| Prerequisites | present | Legs A/B/C + beta coupling + committed-run-scaled magnitude lever + refractory-independent commit-intent certifier all built and firing |
| Implementation completeness | **complete (substrate)** | the 460g-prescribed certifier fix landed and works (seed 44 proves decoupling). The gap is **experiment regime**, not substrate |
| Environment adequacy | adequate | 603n foraging, guard 3/3, closures + completions on all seeds |
| Measurement adequacy | **the binding fault** | two non-vacuity gates (commit-intent, within-window) fire on disjoint seeds -> empty intersection -> C2 never scorable on a coupling-certified seed; plus an attribution confound on the strong-natural-commit seeds |
| Integration adequacy | regime-dependent / partially coupled | closure coupling engages iff natural commit weak; de-commit windows rich iff natural commit strong -- anti-correlated. The closure de-commit is subdominant to the F-driven natural commit |
| Scale / capacity | seed-44 windows under-powered (1 of 5 closures cleared the window gate) | more eval episodes would help window power on the coupling seed but NOT the commit-intent disjointness on 42/43 |

**Recommended epistemic_category:** keep MECH-445 + MECH-446 `candidate` / `v3_pending` / `pending_retest_after_substrate`, both `non_contributory`. The dominant reading is a **measurement/test-design regime-coverage gap + attribution confound on a built substrate**, which the cluster lens resolves into the **commit/release-duration face of the F-dominance conversion ceiling** -- NOT `substrate_ceiling` (the substrate expresses both children on their respective seeds), NOT a falsification.

---

## Cluster reading -- the F-dominance conversion ceiling (user-directed, load-bearing)

The standing `conversion_ceiling_phase0_synthesis_2026-06-18.md` classifies the four roots of the committed-action conversion ceiling and places the SD-034 de-commit at **root C: "de-commit authority magnitude (commitment-dynamics): OPEN, ORTHOGONAL (the 460f problem; fixed 5-tick refractory can't move occupancy vs ~530-560 natural-commit steps). Dissociated from A/B by the 460e inverse tell."**

**460h is the test of that orthogonality, and it argues against it.** The "~530-560 natural-commit steps" the synthesis names as the de-commit's obstacle ARE the F-driven E3 commitment: `result.committed` <- `running_variance < commit_threshold` <- E3 score-stability <- the F-dominated harm/goal score (V3-EXQ-571: F = 88-89% of E3 committed-selection variance). So the de-commit (root C) is a **modulatory lever subdominant to the same F-driven commitment** that root B shows monopolising the candidate argmax. The 460h disjoint-seed signature is the precise fingerprint:

- where F-commit is **strong** (seeds 42/43): the closure de-commit cannot carve against ~2400-2600 committed steps (the 460f swamping), and the coupling is unmeasurable because F already commits;
- where F-commit is **weak** (seed 44): the closure coupling drives commitment and the de-commit can act.

This is "every modulatory channel drowns at the F-dominated commitment," now at the **commit/release-duration** layer rather than the selection layer. Root C is the same root cause as root B, one control point down.

### Convergent cluster table (460h adjudicated; siblings cross-referenced, NOT re-adjudicated)

| Run | Claim(s) | Primary that dominates | Modulatory channel that drowns | Shape | Status |
|---|---|---|---|---|---|
| **V3-EXQ-460h** | MECH-445/446 (de-commit) | F-driven natural commit (running_variance) | closure-coupled de-commit / coupling | de-commit measurable only where F-commit weak; disjoint certifiers | **this autopsy** |
| V3-EXQ-569g/682 + 654g/485h | ARC-065/MECH-341/ARC-062/MECH-294 | F at the committed argmax | modulatory + within-class + CRF + OFC | committed entropy flat despite diverse pool | root B (established; `f_dominance_conversion_ceiling` / GAP-I) |
| V3-EXQ-514t | MECH-436 (drive-coupled wanting) | base_value (IncentiveTokenBank primary) | per-axis drive modulation | drive delta can't flip most_wanted vs base_value gaps | **in-flight sibling autopsy** -- same "modulatory drowns at dominant primary" meta-shape |
| V3-EXQ-625e | SD-037 axis-b | F at committed selection | override/axis-b channel | listed `689a`-gated downstream of the F-front | **in-flight sibling autopsy** |

The meta-shape -- *a secondary/modulatory channel reaches its accumulator but cannot carve against a dominant primary selector* -- is shared by all four. F-dominance (the E3 committed selection, V3-EXQ-571) is the canonical/largest instance; 460h is its **commit/release-duration** face; 514t is the same shape at a different primary (`base_value`). 625e is explicitly a 689a-gated downstream. These convergent failures are **N instances of one structural property**, not N independent bugs. (514t / 625e have their own in-flight autopsies; this record cross-references the convergence and does not re-adjudicate their per-claim directions.)

---

## Learning extracted

- The 460g->460h refractory-independent certifier fix is **confirmed working** (seed-44 commit_intent 375; decoupled from the magnitude lever). The S5 self-defeat is closed; the children's decomposition was the right move.
- commit-intent fires 1/3 **because only 1/3 seeds are in the weak-natural-commit regime the coupling is defined for** -- a regime-coverage property, not a broken certifier. The de-commit is measurable iff the F-driven natural commit is weak.
- The two non-vacuity certifiers (commit-intent vs within-window) are **anti-correlated by construction**; their empty intersection is the binding fault. No refractory tweak fixes it.
- **Reducing F's grip on natural commit-entry decisiveness resolves BOTH halves at once**: shorter, less-decisive natural-commit runs make commit-intent fire broadly (coupling no longer masked) AND make every de-commit window closure-attributable on the same seeds. The 460h disjoint-seed problem dissolves under the F-dominance commit-decisiveness lever -- it does not need a bespoke SD-034 eval-only knob.
- **Root C is the commit/release-duration face of root B**, not orthogonal. The F-dominance front's current levers (conflict-graded-k, gap-scaled commit-T; MECH-439) operate at **selection** and do not directly shorten natural-commit latch occupancy -- so the front needs an additional **commit-entry-decisiveness / latch-occupancy** lever for the de-commit face.
- MECH-445's `what_would_answer` falsification clause ("coupling inert on >= 2/3") is **mis-specified**: it conflates "coupling inert" with "coupling redundant on a strong-natural-commit seed." It must be **regime-scoped to weak-natural-commit seeds** (user-confirmed). Otherwise a strong-natural-commit seed produces a spurious "inert" reading (exactly the 42/43 zeros).
- claim_ids hygiene unchanged: a Leg-A-hook-only run (n_automatic_fires = 0) does not exercise MECH-261; do not weaken the stable claim.

---

## Repair pathway (user-confirmed routing)

**PRIMARY: reclassify root C under the F-dominance front + gate the 460i de-commit retest on a commit-entry-decisiveness lever (`implement-substrate` amend on `f_dominance_conversion_ceiling`).** 460h shows the de-commit is the commit/release-duration face of F-dominance. The F-dominance front (`behavioral_diversity_isolation:GAP-I`, owner V3-EXQ-689a, substrate `f_dominance_conversion_ceiling`, MECH-439) owns the commitment-decisiveness fix. Its current levers act at selection; the de-commit face needs a **commit-entry-decisiveness / natural-commit-latch-occupancy** lever (e.g. a gap-scaled commit-entry threshold or run-length cap so the F-driven natural commit is less monolithic). With that lever, weak-natural-commit becomes the norm across seeds -> commit-intent fires broadly AND de-commit windows are closure-attributable on the same seeds -> the 460h disjoint-certifier problem dissolves and BOTH children become scorable on one regime. Do NOT re-queue 460i on the current F-dominated selector.

**SECONDARY (local control, only if the front lever is far out): closure-exclusive de-commit eval mode.** A natural-commit-suppressed evaluation mode in `commitment-closure-control-plane` (beta elevates ONLY via `_closure_commit_active`, not `result.committed OR _closure_commit_active`, during the de-commit eval) would force every seed into the seed-44 regime, giving clean attribution. This is a **local per-experiment instance** of what the F-dominance commit-decisiveness lever does systemically -- recommended only as a fallback to keep the children testable if the front lever is not imminent; flag it as a hack, not the substantive fix.

**GOVERNANCE flag (root-C reclassification).** Recommend the F-dominance-front owner / a `/governance` walk update `conversion_ceiling_phase0_synthesis_2026-06-18.md` root-C from "OPEN, ORTHOGONAL" to "commit/release-duration face of root B (F-dominance)", add 460h as a `f_dominance_conversion_ceiling` failure record, and register the convergence of 514t / 625e (in-flight) as candidate cluster members for the F-dominance front. (This autopsy provides the evidence; it does not edit the synthesis doc, GAP-I node, or substrate entries -- those are governance writes owned by the front.)

**Plan node.** `commitment_closure:GAP-4` resume_condition: refresh (by governance) to "closes when the de-commit retest (460i) returns a contributory PASS for MECH-445 + MECH-446 on the F-dominance commit-decisiveness lever (NOT the current selector)."

---

## Draft evidence_quality_note (governance applies; this skill does not write it)

> V3-EXQ-460h (supersedes 460g): the refractory-independent commit-intent certifier WORKED (decoupled from the de-commit-magnitude lever -- seed-44 sd034_n_closure_commit_intent=375 where 460g's coupled-elevation counter collapsed 36->0), closing the S5 self-defeat. But the run self-routes substrate_not_ready_requeue because the two non-vacuity certifiers fire on DISJOINT seeds: commit-intent (MECH-445 coupling) fires only where the F-driven natural commit is weak (seed 44, OFF committed_steps=0) while the within-arm de-commit window (MECH-446) has power only where natural commit is strong (seed 42) -- empty intersection, so C2 is never scorable on a coupling-certified seed. Existence proofs both children: MECH-445 seed-44 (375 commit-intent, OFF beta=0), MECH-446 seed-42 (within-arm 0.333->0.0, C2 PASS). NOT a falsification, NOT a substrate ceiling. Cluster reading (user-directed): the SD-034 de-commit is the COMMIT/RELEASE-DURATION FACE of the F-dominance conversion ceiling, not orthogonal (root C reclassified) -- the closure-coupled de-commit is a modulatory channel subdominant to the same F-driven natural commit that monopolises the candidate argmax (V3-EXQ-571 88-89%); measurable only where F-commit is weak. MECH-445 -> non_contributory + pending_retest_after_substrate (+ its what_would_answer falsifier needs regime-scoping to weak-natural-commit seeds; the 2/3 commit-intent zeros are strong-natural-commit redundancy, not inert coupling). MECH-446 -> non_contributory + pending_retest_after_substrate. MECH-261 -> not exercised (n_automatic_fires=0). Route: gate the 460i de-commit retest on a commit-entry-decisiveness lever in the F-dominance front (f_dominance_conversion_ceiling / GAP-I / MECH-439, extended to commit-entry/latch-occupancy), NOT a re-queue on the current selector; reclassify synthesis-doc root C; register 514t/625e convergence.

---

## Routing decision (user-confirmed 2026-06-20)

1. **PRIMARY -- F-dominance front (`implement-substrate` amend on `f_dominance_conversion_ceiling`):** add a commit-entry-decisiveness / latch-occupancy lever so the de-commit (root C) face is covered; gate the 460i de-commit retest on it. Reclassify root C as the commit/release-duration face of root B. (User: "look at all four recent failures as a cluster and consider F-dominance conversion ceiling.")
2. **SECONDARY (fallback) -- bespoke closure-exclusive de-commit eval mode** in `commitment-closure-control-plane`, only if the front lever is not imminent; a local instance of (1), flagged as a hack.
3. **Evidence disposition:** MECH-445 -> non_contributory + pending_retest_after_substrate; record seed-44 as a narrow non-scoring positive existence proof; **flag the MECH-445 what_would_answer for regime-scoping** to weak-natural-commit seeds (user-confirmed). MECH-446 -> non_contributory + pending_retest_after_substrate; record seed-42 within-arm drop (0.333 -> 0.0) as a narrow positive. MECH-261 -> not exercised (do not tag/weaken). 460g -> set `evidence_direction: superseded` on its manifest.
4. **pending_retest_after_substrate:** TRUE for MECH-445 + MECH-446 until a contributory PASS on the F-dominance commit-decisiveness lever (or the fallback closure-exclusive eval).
5. **Governance reclassification (flag, not applied here):** update `conversion_ceiling_phase0_synthesis_2026-06-18.md` root C "OPEN, ORTHOGONAL" -> "commit/release-duration face of root B"; add 460h failure record to `f_dominance_conversion_ceiling`; register 514t / 625e convergence as candidate cluster members (they have their own in-flight autopsies).
6. **Plan node:** `commitment_closure:GAP-4` resume_condition refreshed (by governance) to the F-dominance-gated 460i retest; do NOT re-author 460d/e/f/g/h.

`commitment_closure:GAP-4` stays in-progress; closes when the de-commit retest returns a contributory PASS for MECH-445 + MECH-446 on the F-dominance commit-decisiveness lever.
