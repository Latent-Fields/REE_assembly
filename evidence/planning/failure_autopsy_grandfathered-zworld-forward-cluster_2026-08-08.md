# Failure Autopsy: SD-011/SD-012/ARC-033 + companions (8 runs, 3 independent groups)

**Generated:** 2026-08-08T17:10:36Z
**Scope:** cluster (8 runs -- explicitly NOT one cluster; 3 independent groups)
**Status:** confirmed (Step 8 interactive gate: user confirmed both actions -- V3-EXQ-247 run-2 reclassification, V3-EXQ-595 corrupting-severity routing)

## Scope note

These 8 runs resolve into **three independent findings groups** sharing ancestry (all trace to the 2026-03-24 dual-nociceptive-streams design doc) but with structurally different failure shapes. Reported separately per the skill's guidance not to force an artificial cluster narrative.

## Dry-run gate

All 8 confirmed clean via `check_dry_run_citations.py`: 0 dry, 8 clean.

---

## Group A: V3-EXQ-247 ×2 (2026-04-06/04-07) -- SD-011/SD-012/ARC-033/ARC-030 co-integration

**Facts.** `v3_exq_247_sd011_sd012_integration`, 4 conditions (FULL/NO_URGENCY/NO_AFFECT/BASELINE) × 3 seeds. Both runs: `mean_goal_norm = 0.0` in every condition, every seed -- the z_goal pathway is completely dead. C1 (commit_diff)/C3 (goal_norm) fail structurally; C4/C5 pass. This is an absolute/precondition failure, not a discrimination failure -- SD-011/SD-012's actual mechanism was never exercised.

**Finding -- governance inconsistency.** Run 1 (04-06) was already correctly reclassified `evidence_direction: non_contributory`. Run 2 (04-07) -- identical defect, identical magnitude -- was **not**: it still carries `evidence_direction: does_not_support` with a per-claim breakdown (SD-011/SD-012/ARC-030: does_not_support; ARC-033: mixed) stamped 2026-04-08, apparently before the run-1 correction pattern was applied. **User-confirmed action: reclassify run 2 to match run 1.**

**Claim-layer / biology.** SD-010/SD-011 (the dual-stream split) was already validated stable substrate by the time 247 ran (EXQ-178b PASS 03-30, EXQ-198 PASS 04-01, promoted stable 04-18) -- so 247 tests AFTER the split existed, as post-split integration evidence, not motivating evidence for the split itself. Literature present for all four claims (SD-011: Melzack & Casey 1968, Craig 2002/2003/2009, Rainville 1997; SD-012: Berridge & Robinson 2016, Balleine & Dickinson 1998, Keramati & Gutkin 2014; ARC-030: Cox 2015, Hikida 2012, Bariselli 2018). Faithful biological translation, no lit-pull owed.

**Four-layer diagnosis (both runs):**

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (uninformative) | z_goal never fired |
| Biological reference | clear | dual-stream nociception + drive-scaled incentive-salience, well-grounded |
| Prerequisites | missing | z_goal seeding pathway (pre-MECH-307/GAP-1/GAP-2/GAP-7) structurally broken at this date |
| Implementation | partial | dual-stream harm encoders functioning (C4/C5 pass); goal-seeding pipeline had crossed wiring |
| Environment | adequate | not the bottleneck |
| Measurement | adequate | z_goal_norm correctly reports 0.0 |
| Integration | isolated | harm stream and goal stream never co-integrated because goal stream was dead |
| Scale | moot | irrelevant given precondition failure |

**Already resolved.** ARC-030's current evidence_quality_note (2026-08-08 entry) explicitly names V3-EXQ-247's FAIL as "the same defect, not a fresh finding," tracing the fix path: GAP-1/MECH-307 (05-11), GAP-7/SD-057 (06-04->15), GAP-2/SD-049 Phase 2 (closed 06-15 on V3-EXQ-514o). No V3-EXQ-247 letter successor was ever queued -- correctly, since the fix path abandoned the 247 lineage for the GAP-1/2/7 substrate rebuild.

**Recommended disposition:** `epistemic_category: substrate_ceiling` (historical, already-superseded -- the substrate that blocked it is now built). `evidence_direction: non_contributory` for BOTH runs (correcting run 2). `pending_retest_after_substrate: false` -- the retest already happened under different EXQ numbers. `routing: governance-note-only` -- no chip, this is closure/documentation.

**Re-derive brake:** 0 confirmed ceiling hits for SD-011/SD-012/ARC-033/ARC-030 in the corpus. This would be hit #1 if stamped -- brake does not fire.

---

## Group B: V3-EXQ-260/261/262 (2026-04-08, same-day companion triple) -- SD-020, SD-021, MECH-220

**Companion-set confirmed** (not coincidental): same registration date, same source literature (Chen 2023 cingulate-insula hub), same location doc, runs within 36 seconds of each other; 260 and 262 share identical seeds/config and 262's `mean_stream_corr` matches 260's exactly per seed (shared substrate checkpoint).

**260 (SD-020 harm_surprise_pe):** C1 fails (0/3 seeds), C2 passes (2/3, stream decorrelation). `weakens` for SD-020, `supports` for SD-011 (legitimate C2 dissociation read). Predates SD-020's eventual stable promotion (04-22, via a later, better-designed EXQ-324b on the SD-022 limb-damage substrate) -- superseded in substance, not formally tagged `supersedes`.

**261 (SD-021 descending pain mod) -- already self-documented.** Manifest carries `non_degenerate: false` and a `degeneracy_reason` stating plainly: NO_DESCENDING and WITH_DESCENDING are bit-identical on every metric (12/12 comparisons) because `E3Selector.post_action_update()` unconditionally clears the `_committed_trajectory` handle the driver's gate reads, so the gate never fires -- AND that the "SD-011 supports" tag on this run is an **unconditional hardcode in the driver source (line 289)**, not a measured criterion outcome. This is an already-correctly-self-diagnosed `non_degenerate: false` case.

**262 (MECH-220 harm hub):** `fwd_r2 < -0.89` in every condition including NO_HUB. Precisely-dated missing-dependency finding: `E2HarmSForward` (the ARC-033 prerequisite) was implemented 2026-04-09 -- literally the day after this run.

**Claim-layer / biology.** Literature present for all three (SD-020: 4 entries, lit_conf 0.915; SD-021: 8 entries, lit_conf 0.852; MECH-220: 4 entries, lit_conf 0.878). Faithful biological translations (anterior/posterior insula PE dissociation, cingulate-insula hub, PAG descending modulation). No lit-pull owed.

**Four-layer diagnosis:**

| Run | Claim alignment | Dominant layer |
|---|---|---|
| 260 (SD-020) | weakened (real, underpowered) | Measurement/scale (n_steps too small) |
| 261 (SD-021) | unclear/non-informative | Prerequisites (commitment gate never latches; already self-documented) |
| 262 (MECH-220) | unclear/non-informative | Prerequisites (dependency landed next day) |

**Recommended disposition:**
- 260: `epistemic_category: measurement_gap`. `evidence_direction: weakens` (SD-020, low-weight/superseded-in-practice by the later validated design), `supports` (SD-011, genuine C2 read) stand as recorded. `routing: governance-note-only` -- SD-020 already resolved via a better successor.
- 261: `epistemic_category: measurement_test_design_defect` (the driver's own self-documented conclusion). `evidence_direction: non_contributory` for SD-021 (matches how the claims.yaml SD-021 note already treats the sibling EXQ-325 series). **Recommend striking the hardcoded "supports SD-011" tag** -- `evidence_direction_per_claim.SD-011 -> non_contributory`, noting it was never measured. `routing: governance-note-only`.
- 262: `epistemic_category: precondition_unmet`. `evidence_direction: non_contributory` for MECH-220 (already how claims.yaml treats it via the sibling EXQ-395 note); `supports` for SD-011 stands (a real, non-hardcoded criterion here, unlike 261). `routing: governance-note-only`.

**Re-derive brake:** 0/0/0 confirmed ceiling hits for SD-020/SD-021/MECH-220. Not applicable -- none of these are `substrate_ceiling` reads (measurement/precondition categories, correctly excluded from the brake by rule R3).

---

## Group C: V3-EXQ-595 ×3 (2026-05-20/21, really 2 distinct executions) -- ARC-033 vs ARC-058 arbitration

**Duplicate-manifest finding.** Git-history reconstruction shows run 1 (05-20T06:33:23Z) and run 2 (05-20T21:54:56Z) are genuinely distinct executions (different per-seed rollout data), but run 3 (05-21T07:47:13Z) is **byte-identical to run 2** in every `per_seed_results` and `pass_criteria_summary` field, to full float precision -- produced by the documented git-based coordinator auto-sync conflict-recovery machinery (a re-apply-after-rebase-conflict event), not a third independent execution. **There are 2 genuine executions, not 3.** Flag to governance so this isn't double-counted in any population statistic.

**Facts (both distinct executions).** 3 conditions (OFF/ON_INDEPENDENT/ON_SHARED) × 3 seeds. C0 policy diversity passes (min_entropy>=0.10, 3/3 seeds both arms). **C1 (balanced-harm-events) fails**: zero interoceptive harm events tagged at all during the 30-episode P2 eval window, every seed/condition, both executions. C2 (forward-learnability) passes. **C3 (cross-arm discrimination) fails**: `harm_a_forward_r2` bit-identical between ON_INDEPENDENT and ON_SHARED for every seed, both executions.

**Root-cause investigation, driver-level (this OVERTURNS the manifest's own self-label of `substrate_ceiling`):**

1. **C1 is real and structural, not a substrate gap.** The env's interoceptive-event classifier only tags an "agent-caused harm event" when the agent is *currently colliding* with a hazard during the 30-episode P2 window, which comes after 150 episodes of training a policy whose entire objective is to avoid harm. This is a self-defeating test design: the better training works, the less testable the criterion becomes. SD-048 (interoceptive noise substrate) is already landed and functioning -- this is an eval-window design gap, not a missing substrate.

2. **C3 has a sharper cause: the "shared trunk" arm is never actually shared.** Traced through `ree_core/agent.py:465-495`: `use_shared_harm_trunk=True` constructs a `HarmForwardTrunk` and wires it into `E2HarmAForward` -- but the code's own comment states a genuine ARC-058 shared-trunk test requires a competing experiment to ALSO construct `E2HarmSForward` consuming the same trunk, at the experiment-script level. Grepped the driver (`v3_exq_595_arc033_vs_arc058_post_diversity_three_arm.py`) for `harm_forward_trunk`, `E2HarmSForward`, `e2_harm_s`, `shared_trunk` -- **zero matches, all four**. The driver only ever trains `e2_harm_a`; it never constructs the z_harm_s side on either arm. "ON_SHARED" differs from "ON_INDEPENDENT" only in whether one trunk submodule is externally-vs-internally constructed -- functionally equivalent for a single-stream fit, with no second stream ever sharing the trunk to make "shared" mean anything. **The C3 criterion is structurally unreachable by any training budget -- unsettable, not merely underpowered.** A full-budget analog of the documented `dry_run_unreachable_criterion` trap.

**This reclassifies severity upward from "environment sparsity" to a `corrupting` design defect for C3 specifically** -- a future unmodified re-run of this driver would reproduce the same false-negative-on-sharing result and could be mistaken for real evidence against ARC-058, while C1's sparsity issue is a separate, independently-fatal `degrading`-adjacent gap.

**Claim-layer / biology.** ARC-033 vs ARC-058 arbitration is the still-open half of ARC-033's own `what_would_answer` (ARC-033 is `stable` on the learnability question via V3-EXQ-525; the independent-vs-shared-trunk arbitration is separately open, successor to the already-autopsied `V3-EXQ-445h` non_contributory/standard read). Literature present for both claims (ARC-033: 1 entry; ARC-058: 2 entries, Horing & Buchel 2022 modality-general aversive-PE finding). Faithful biological translation, not formal import.

**Four-layer diagnosis (both executions, same read):**

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (uninformative for C3; C1 also blocks) | arbitration not actually testable as coded |
| Biological reference | clear | Horing & Buchel 2022 modality-general aversive PE |
| Prerequisites | present | committed-action diversity genuinely landed -- C0 passes |
| Implementation | **stub/absent for the discriminating mechanism** | shared trunk never actually shared; driver never builds E2_harm_s |
| Environment | too sparse | trained avoidant policy generates near-zero harm contact in eval window |
| Measurement | adequate | the classifier itself is fine; what triggers it is absent |
| Integration | isolated | e2_harm_a alone; no cross-stream integration attempted |
| Scale | not the bottleneck | training budget is not the limiter |

**Recommended disposition (both distinct executions):** `epistemic_category: measurement_test_design_defect` (NOT `substrate_ceiling` despite the manifests' own self-label -- a V3-EXQ-642-shaped self-route mislabel: the manifest's word was a hypothesis, not a verdict, and the driver-level read shows the correct category). `evidence_direction: non_contributory` for both ARC-033 and ARC-058 (correct outcome, wrong stated cause -- stands).

**`severity: corrupting`** for the C3 shared-trunk wiring gap (a future unmodified re-run would produce the same false-negative-on-sharing result); `degrading` for the C1 eval-window sparsity issue in isolation.

**`substrate_paths`**: `ree-v3/experiments/v3_exq_595_arc033_vs_arc058_post_diversity_three_arm.py` (driver never constructs E2_harm_s / never uses `harm_forward_trunk`); `ree-v3/ree_core/agent.py` lines ~465-495 (comment explicitly documents the missing script-level wiring -- a known, named gap, not a fresh discovery).

**routing: `/queue-experiment`** (redesign, new letter V3-EXQ-595a) -- **not `/implement-substrate`**: `HarmForwardTrunk` and `E2HarmSForward` already exist as substrate; what's missing is driver-level glue constructing both streams against the same trunk object in the ON_SHARED arm, plus an eval-window redesign for C1 (e.g. a forced-exposure/held-out harm-encounter window, or evaluating during P1 rather than post-convergence P2, or an explicit external-hazard-injection variant using SD-029's `_inject_external_hazard` -- noting that path tags events as externally-caused, not agent-caused, so it needs its own criterion adjustment, not a drop-in fix).

**Re-derive brake:** 0 confirmed `substrate_ceiling` hits for ARC-033/ARC-058 (the one existing confirmed autopsy, V3-EXQ-445h, is stamped `standard`, excluded by R3). Since this autopsy recommends `measurement_test_design_defect` (not `substrate_ceiling`), it would not add a ceiling hit either -- brake state unaffected. A redesigned re-queue here is explicitly NOT the same-question ceiling-circling the brake exists to stop; it is a genuine implementation-bug fix.

---

## Confirmed routing summary (per user's Step 8 gate answer)

- **Group A (V3-EXQ-247 ×2)**: reclassify run 2 to `non_contributory` (matching run 1). `governance-note-only`, no chip.
- **Group B (V3-EXQ-260/261/262)**: no action beyond the recommended per-run categories above (already correctly disposed). `governance-note-only`, no chip.
- **Group C (V3-EXQ-595, 2 distinct + 1 duplicate)**: `severity: corrupting` on C3's wiring gap, `substrate_paths` named, routed `/queue-experiment` (595a redesign). Duplicate-manifest artifact (run2=run3) flagged for governance/review_tracker so it isn't double-counted. **Not chipped from this session** -- recorded here for `/governance` Step 2b to ratify.

## Learning extracted

1. **Reclassification-consistency gap**: identical defects across sibling runs of the same experiment (247 04-06 vs 04-07) can get inconsistently reclassified -- one corrected, its twin left stale. Worth a standing check across other multi-run same-experiment_type pairs.
2. **Driver self-documentation is sometimes already excellent** (261's own `degeneracy_reason` did most of this autopsy's work) -- always check for pre-existing self-diagnosis before re-deriving.
3. **A `substrate_ceiling` self-label in `evidence_direction_note` is not self-evidently correct** (595's own notes say "substrate_ceiling" three times; driver-level investigation shows the real cause is an unreached experiment-design wiring gap -- canonical "self-route is a hypothesis" case, V3-EXQ-642-shaped).
4. **A corrupting implementation gap can hide behind a criterion that also has an independent, milder confound** (595's C1 sparsity vs C3 unreachability) -- check both before assuming the first-cited confound is the whole story.
5. **Coordinator auto-sync conflict recovery can duplicate a manifest under a fresh run_id/timestamp** (595 run 2 = run 3), inflating apparent replicate counts silently.
