# Failure Autopsy (cluster): 2026-03-29/04-01 "action-selection-decoupled" blind-spot-net FAILs

**Generated:** 2026-08-08T16:39:36Z
**Scope:** cluster (14 runs, 13 unique experiment scripts, 1 outlier date)
**Status:** confirmed (Step 8 interactive gate: user confirmed one cluster artifact covering all 14 targets)

This is the `pending_review.md` "Reviewed FAIL with no confirmed autopsy" blind-spot net: 14 claim-tagged, non-diagnostic FAILs marked reviewed in `review_tracker.json` but never autopsied. All 14 manifests confirmed `dry_run: false`.

## 1. Facts and per-run signature

| # | run_id (short) | claim(s) | failed criterion | degeneracy_reason present? | arms-identical signature |
|---|---|---|---|---|---|
| 1 | v3_exq_150 (Q-005 sleep anneal) | Q-005 | discrimination (C1/C3/C4) | yes -- explicit: `random.randint` every condition | Yes -- harm metrics bit-identical across NO_ANNEAL/ANNEAL/RESET |
| 2 | v3_exq_151 (Q-006 ethics developmental) | Q-006 | discrimination (C1/C2/C2a/C2b) | no field, inferred | Yes -- `mean_harm_final` bit-identical; script confirmed `random.randint` x2 |
| 3 | v3_exq_152 (Q-012 control constraints) | Q-012 | discrimination (C1/C2) | no field, inferred | Yes -- REE_FULL==PREDICTIVE_ONLY==NO_LEARNING bit-for-bit; script confirmed `random.randint` x2 |
| 4 | v3_exq_154 (Q-014 JEPA blind-spot) | Q-014 | C4 (insufficient harm events) | no field | Zero-events; script's random-walk policy is **intended design** (measures representation, not behavior) |
| 5 | v3_exq_155 (Q-015 commit boundary) | Q-015 | C1/C4/C7 (insufficient harm events) | no field | Zero-events; same intended-random-policy design as #4 |
| 6 | v3_exq_156 (Q-016 tri-loop arbitration) | Q-016 | C1-C5 (insufficient conflict steps) | no field | Yes -- 4-way bit-identical; `n_conflict_steps=0` everywhere |
| 7 | v3_exq_159 (Q-020/ARC-007 valence) | Q-020, ARC-007 | C2/C4/C5 (insufficient harm events) | no field | Zero-events; script uses `random.randint`/`random.choices`/`random.choice` |
| 8 | v3_exq_160 (Q-023 multiagent convergence) | Q-023 | C4/C5 (insufficient events) | yes -- entropy-bonus-only gradient on `.detach()`ed z_world/z_self | Yes -- 3-way, 28-metric bit-identical, `n_harm_events_final=0` |
| 9 | v3_exq_161 (Q-024 trajectory representation) | Q-024 | C1/C2/C5 (insufficient events) | yes -- same detached-gradient mechanism as #8 | Yes -- 3-way, 38-metric bit-identical incl. transfer entropy |
| 10 | v3_exq_163 (MECH-140/141 dual-timescale) | MECH-140, MECH-141 | C1/C4 | no field | Yes -- 3-way bit-identical; script confirmed `random.randint` |
| 11 | v3_exq_165 f3319520 (MECH-143/144, run 1) | MECH-143, MECH-144 | C4 only (data-quality gate) | no field | **No** -- `harm_rate`/`path_efficiency` genuinely differ; real `HippocampalTerrainNavigator`, not random.randint |
| 12 | v3_exq_165 d2d314a9 (MECH-143/144, run 2) | MECH-143, MECH-144 | C4 only, identical numbers to #11 | no field | Same as #11 -- duplicate/re-run of the identical config |
| 13 | v3_exq_164a (MECH-063/142 axis decorrelation) | MECH-063, MECH-142 | C1/C2 | no field | Yes -- bit-identical per seed; policy trained on `.detach()`ed z_world/z_self, same detached-gradient family as #8/#9 |
| 14 | v3_exq_196 (ARC-018 rollout viability, **2026-04-01**) | ARC-018 | C1/C2 | manifest self-decision `retire_ree_claim` | Yes but **different mechanism**: E3 CEM candidate set collapsed to one first-action class (already root-caused 2026-07-22) |

**Root-cause mechanism confirmed across every driver lacking an explicit `degeneracy_reason`:** `v3_exq_151:259,301`, `v3_exq_152:274,312`, `v3_exq_163:346` -- literal `random.randint`; `v3_exq_164a:438-440` -- policy sampled via multinomial but both `z_world`/`z_self` inputs `.detach()`ed before reaching the policy (same "gradient never reaches representation" family as #8/#9); `v3_exq_154`/`v3_exq_155` -- `random.randint`, and the scripts' own scenario text says "random action policy" (this was the *intended* baseline, testing representation/attribution independent of behavior); `v3_exq_159:426,439,448` -- `random.randint`/`random.choices`/`random.choice` for CEM-style candidate generation.

**The substrate dependency, not a per-script slip:** `ree_core/action_learning/actor_critic.py` -- the first real, RPE-driven, trained actor-critic action-learning module (MECH-457) -- landed **2026-07-12**, over three months after this cluster ran (2026-03-29 for 12 of 14; 2026-04-01 for the ARC-018 outlier). At the time these 13 scripts were authored, no substrate existed capable of learning a policy whose action choices are causally driven by a harm-evaluation/ethics/arbitration/decorrelation signal. The hippocampal terrain navigator (SD-004/SD-005, landed ~2026-03-19/20) did exist -- exactly why #11/#12 (MECH-143/144) are the one pair whose arms actually differ.

## 2. Claim-layer status (checked against current claims.yaml, 2026-08-08)

| Claim | Current status | Already superseded/digested by later work? |
|---|---|---|
| Q-005 | active, sleep unimplemented in V3 | **Yes** -- claims.yaml already marks EXQ-150 `superseded`, explicit note: precondition (real sleep substrate) still unmet |
| Q-006 | active, residue-field precondition | **Yes** -- claims.yaml already scored-excluded (implementation gap, residue_field_not_building) |
| Q-012 | candidate | **Yes, with signal** -- explicitly superseded by **EXQ-193** (2026-04-04): REE_FULL beat PREDICTIVE_ONLY by 7.5 harm units, real directional result |
| Q-014 | legacy/retired | **Yes -- moot.** JEPA integration dropped from the architecture on 2026-03-29 (same day this ran) |
| Q-015 | active/substrate_conditional | **Partially** -- blocked on a different, still-missing knob (tunable commit-boundary granularity), already correctly routed |
| Q-016 | active | No formal re-test, but the "EXQ-156 lesson" is already written into the claim's own `what_would_answer` text |
| Q-020 | candidate (reopened 2026-07-25) | Reopened by a later, unrelated experiment (V3-EXQ-266b); EXQ-159 not cited anywhere in Q-020's evidence -- genuinely un-digested but superseded in effect |
| Q-023 | open, `epistemic_category: derivational` | Re-routed 2026-06-11 (`/thought-digestion`) to "answerable by proof, not experiment"; EXQ-160's degeneracy already cited as the reason |
| Q-024 | open, same derivational reframing | Same as Q-023; EXQ-161's degeneracy already cited |
| MECH-140 | candidate, `substrate_ceiling` | **Yes -- superseded.** `evidence.from: failure_autopsy_V3-EXQ-710_2026-07-03`, substrate (soft-competitive settling) built 2026-07-02 |
| MECH-141 | candidate, `evidence: []` | **No -- genuinely untouched.** No later autopsy references it |
| MECH-063 | provisional | **Yes -- superseded.** `evidence.from: failure_autopsy_V3-EXQ-779b_2026-07-19`; two dedicated cluster autopsies already exist |
| MECH-142 | candidate, `evidence: []` | **No -- genuinely untouched** |
| MECH-143 | candidate, `evidence: []` | **No** -- both March runs untagged in claims.yaml despite manifest claim_ids |
| MECH-144 | candidate, `evidence: []` | Same as MECH-143 |
| ARC-007 | provisional, strong independent PASS chain | EXQ-159 not cited in ARC-007's evidence note; peripheral, not load-bearing (ARC-007 well-supported independently) |
| ARC-018 | provisional (demoted from active 2026-07-25) | **Extraordinarily well-digested already** -- 2026-07-22 investigation (session `keen-varahamihira-791a46`) root-caused the exact mechanism and confirmed the blocker was incidentally fixed 2026-05-17 (SP-CEM became main-path default, `cb1c6da`). Diagnosis exists; formal `/failure-autopsy` + `/governance` close-out was the missing step |

## 3. Biological-reference triage

All 14 converge cleanly on the same read: **there is no biological content to triage.** Every manipulated mechanism (sleep annealing, developmental ethics timing, control constraints, JEPA invariance, commit-boundary tokens, tri-loop arbitration, multiagent convergence, trajectory representation, dual-timescale arbitration, axis decorrelation, hippocampal value-blindness [partially], hippocampal viability mapping) was never actually instantiated as something that could act on behavior. This is not "biology says X, REE shows not-X" -- it is "REE's harness could not express X at all, in either direction." Formal-import-vs-faithful-translation is moot for the same reason.

The one partial exception: MECH-143/144 (#11/#12) used a real, behaviorally-active `HippocampalTerrainNavigator`, and the observed deltas are genuine measurements -- close to a real biological read, gated shut only by an over-strict data-quality threshold (see below).

## 4. Four-layer diagnosis (shared table, applies to the 11-member core: #1,2,3,6,7,8,9,10,13; #4/#5 with the caveat below)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (not weakened) | Every criterion depending on differential behavior was structurally unable to discriminate; claims never given a fair test |
| Biological reference | absent | Nothing biological was instantiated to compare against |
| Prerequisites | **missing** | The real dependency -- a trained, differentiable, condition-sensitive action-learning policy -- did not exist until MECH-457 landed 2026-07-12, ~3.5 months later |
| Implementation completeness | **stub** | `random.randint`/`random.choice` action selection, or a policy trained on `.detach()`ed representations with only an entropy-bonus gradient -- symbol of "a policy" without the functional role |
| Environment | adequate-to-unknown | Configs reasonable; for #4-#7,#9 the random walk additionally failed to generate enough hazard contacts -- compounding, not primary |
| Measurement | adequate | Metrics correctly reported "no differential signal" because there genuinely was none |
| Integration | isolated | Each script independently reimplements its own action loop; no shared, tested action-selection component existed to integrate with |
| Scale/capacity | not reached | The bottleneck is categorical (no signal path exists), not a scale question |

**#4/#5 (Q-014, Q-015) divergent note:** random-action baseline was the *intended design* (testing representation/attribution independent of behavior) -- "implementation completeness: stub" doesn't quite apply to intent, but the C4/C7 insufficient-harm-events outcome traces to the same mechanical fact (random walk rarely touches a hazard at these densities). Classified as environment/protocol-underpowered, sharing the same root population.

**#11/#12 (MECH-143/144) divergent table:** claim alignment unclear/arguably-strengthened-but-blocked (real deltas measured, closest to a fair test in the cluster); implementation complete for this specific test; measurement **under-instrumented/mis-gated** -- `C4` requires `n_shuffle_events > 4` (strict); both seeds land on exactly 4 with `K_SHUFFLE=50` over 400 episodes -- an off-by-one threshold (`>` instead of `>=`) auto-fails a run that otherwise cleared C1-C3 close to the line. A measurement/test-design gate defect, not a substrate gap.

**#14 (ARC-018) divergent table:** implementation completeness stub, **already fixed** -- E3's CEM candidate set collapsed to exactly one first-action class (confirmed by independent reproduction, 68/68 ticks); prerequisites resolved as of 2026-05-17 when SP-CEM became the main-path default, incidentally removing the blocker six weeks after this run.

## 5. Cluster convergent-pattern table (Step 6)

| Experiment | Claim | Negative-control/absolute criterion | Discrimination criteria | Read |
|---|---|---|---|---|
| v3_exq_150 | Q-005 | n/a (pair design) | C1/C3/C4 FAIL -- bit-identical | `random.randint`; explicit degeneracy_reason |
| v3_exq_151 | Q-006 | n/a | C1/C2/C2a/C2b FAIL -- harm bit-identical | `random.randint`, confirmed in source |
| v3_exq_152 | Q-012 | n/a | C1/C2 FAIL -- 3-way bit-identical incl. variance | `random.randint`; superseded by EXQ-193 with real signal |
| v3_exq_154 | Q-014 | C4 FAIL (min harm events) | n/a -- never reached | Random-walk-by-design + sparse hazards; claim retired anyway |
| v3_exq_155 | Q-015 | C7 FAIL (min harm events) | n/a -- never reached | Random-walk-by-design + sparse hazards; substrate-blocked on unrelated knob |
| v3_exq_156 | Q-016 | C4 FAIL (min conflict steps) | C1/C2/C3/C5 FAIL -- 4-way bit-identical | Same policy-substrate gap; lesson already in claim text |
| v3_exq_159 | Q-020/ARC-007 | C4/C5 FAIL (min events, valence head) | C2 FAIL | `random.randint`/`random.choice`; superseded by later EXQ-266b for Q-020 |
| v3_exq_160 | Q-023 | C5/C6 FAIL (zero events) | C4 FAIL -- 3-way, 28-metric bit-identical | Detached-gradient entropy-only walk; explicit degeneracy_reason; reframed derivational |
| v3_exq_161 | Q-024 | C5 FAIL (zero events) | C1/C2 FAIL -- 3-way, 38-metric bit-identical | Same detached-gradient mechanism; reframed derivational |
| v3_exq_163 | MECH-140, MECH-141 | C4 FAIL (min conflict steps) | C1 FAIL -- 3-way bit-identical | `random.randint`; MECH-140 already superseded, MECH-141 still open |
| v3_exq_165 (x2) | MECH-143, MECH-144 | **C4 FAIL -- threshold defect** (n_shuffle_events>4, actual=4) | C1/C2/C3 close/passing | Real navigator, real behavioral deltas -- different bug entirely |
| v3_exq_164a | MECH-063, MECH-142 | C1/C2 FAIL | WITH/NO_DECORRELATION bit-identical | Detached-gradient family; MECH-063 already superseded, MECH-142 still open |
| v3_exq_196 (04-01) | ARC-018 | C1/C2 FAIL -- harm_advantage exactly 0.0 | n/a | Different, already-diagnosed mechanism (CEM candidate collapse); fixed 2026-05-17 |

**Is this N independent bugs or one structural property?** One structural property for 11 of 13 unique scripts (85%), a distinct-but-related property for 1 (ARC-018), and a genuinely unrelated bug for 1 (MECH-143/144). The dominant reading: **substrate-immaturity, not test-design-ceiling.** No real, differentiable, condition-sensitive action-learning policy existed in `ree_core` for this driver population on 2026-03-29 (and the 04-01 outlier); scripts fell back to literal random sampling or a policy trained only on an entropy bonus over detached representations -- functionally identical outcomes. This is not 11 separate coding mistakes, it is one missing substrate dependency instantiated mechanically across every driver cut against that gap that week. MECH-143/144's near-miss is the control case validating this read: when a real mechanism *was* wired in, the test worked and produced graded, sensible deltas.

**Planning decision this forces:** do not treat this as a per-script design defect to fix; treat it as "queued and run before its prerequisite substrate existed," now resolved by MECH-457's landing.

**Illusory-conflict check:** for every claim recommended `non_contributory` above, the remaining live "supports" evidence was checked and is not narrow/single-pathway as a side effect of this batch: ARC-007 (strong, multi-run PASS chain, independent of this cluster); ARC-018 (currently demoted to provisional, single-pathway concern already flagged in claims.yaml's own 2026-07-25 note); Q-012 (rests on EXQ-193's positive signal, not synthetic evidence).

## 6. Recommended routing per claim

| Claim | Recommended `epistemic_category` | `evidence_direction` | Routing |
|---|---|---|---|
| Q-005 | measurement_test_design_defect (pre-substrate) | non_contributory | No action -- already correctly superseded |
| Q-006 | measurement_test_design_defect (pre-substrate) | non_contributory | No action -- already correctly scored-excluded |
| Q-012 | n/a -- superseded | n/a | No action -- EXQ-193 supersedes with positive signal |
| Q-014 | n/a -- claim retired | n/a | No action -- moot |
| Q-015 | measurement_gap | non_contributory | No action -- already correctly substrate_conditional on unrelated knob |
| Q-016 | competence_implementation_gap | non_contributory | Formal write-up owed (this artifact); candidate for `/queue-experiment` re-run now that MECH-457 exists -- flagged, not chipped |
| Q-020 | measurement_test_design_defect (pre-substrate) | non_contributory | No action -- Q-020 already has a later, better-designed re-test (EXQ-266b) |
| Q-023 | n/a -- reframed | n/a | No action -- already routed derivational |
| Q-024 | n/a -- reframed | n/a | No action -- already routed derivational |
| MECH-140 | n/a -- superseded | n/a | No action -- V3-EXQ-710 autopsy supersedes |
| MECH-141 | competence_implementation_gap (pre-substrate) | non_contributory | Genuinely open -- candidate for `/queue-experiment` re-run now that MECH-457 exists -- flagged, not chipped |
| MECH-063 | n/a -- superseded | n/a | No action -- V3-EXQ-779b + dedicated cluster autopsies supersede |
| MECH-142 | competence_implementation_gap (pre-substrate) | non_contributory | Genuinely open -- candidate for `/queue-experiment` re-run -- flagged, not chipped |
| MECH-143 | measurement_test_design_defect | **inconclusive** (real signal present) | Cheapest fix in the cluster: `n_shuffle_events > 4` -> `>= 4` (or extend episode budget) -- flagged, not chipped |
| MECH-144 | measurement_test_design_defect | inconclusive | Same run as MECH-143 |
| ARC-007 | n/a | n/a | No action -- well-supported independently; this run peripheral |
| ARC-018 | competence_implementation_gap, already resolved | non_contributory | **Governance-only action**: apply the deferred 2026-07-22 re-adjudication; decide whether a re-test under current SP-CEM defaults is now warranted -- flagged, not chipped |

**Per the standing rule** (this autopsy's own recommendations are proposals, not yet governance-ratified): none of the `/queue-experiment` candidates (Q-016, MECH-141, MECH-142, MECH-143/144) or the ARC-018 governance close-out are chipped from this session. They are recorded here and in the closing session report for `/governance`'s Step 2b to ratify and chip.

**Re-derive brake check:** MECH-140 and MECH-063 already carry `substrate_ceiling` autopsies from later runs (V3-EXQ-710, V3-EXQ-779b). This March run would be a second/third hit if counted independently, but since it predates and is superseded by those later autopsies, it is **not** counted as an independent brake increment -- it's the same underlying finding surfacing earlier in time, already correctly resolved downstream.

## 7. Learning extracted

1. Substrate-dependency timing, not per-script quality control, was the failure mode. 11 of 13 driver scripts needed a differentiable, condition-sensitive action-learning policy that did not exist in `ree_core` until MECH-457 (2026-07-12), ~3.5 months after this cluster ran. This is the skill's "positive-negative result" case: the FAIL strengthens the prerequisite claim that a real action-learning substrate is required before behavior-dependent discriminative-pair experiments are meaningful.
2. Two structurally distinct sub-mechanisms produce the identical observable symptom (bit-identical/zero-variance arms): literal `random.randint`, and a policy trained only on an entropy bonus over `.detach()`ed representations. Both should be recognized as the same family when triaging future clusters.
3. The "insufficient harm events" sub-shape (#4,#5,#6,#7,#9) compounds, rather than separates from, the same root cause: a random walk in moderate-hazard-density grids rarely generates enough contacts to power any metric.
4. Most of this cluster's substantive diagnosis was already done -- just not through this skill. Several claims carry detailed, mechanism-level prose in claims.yaml's `evidence_quality_note`/`what_would_answer` fields, written by prior governance cycles and one dedicated investigation (ARC-018, 2026-07-22). What was missing was the formal `failure_autopsy_*` artifact and, for ARC-018, a closing governance re-adjudication -- a process/paperwork gap, not a knowledge gap.
5. MECH-143/144 is the exception that validates the rule: the one script in the cohort with a real, wired behavioral mechanism (hippocampal terrain navigator, built before 2026-03-29), and the one run whose arms genuinely differ.
6. Recording note: none of these manifests carry `substrate_hash` (older schema, pre-dating the Experimental Recording Standard, 2026-07-12) -- a future re-run under current recording standards would also close that gap.

## 8. Summary for governance

- **11 targets recommend `non_contributory`/no live claim-layer action** (already superseded, retired, reframed-derivational, or substrate-blocked on an unrelated knob) -- this autopsy's value for those is formally closing the loop.
- **3 targets are genuinely open**: MECH-141, MECH-142 (pre-MECH-457 policy gap, now unblocked -- candidates for `/queue-experiment`), and MECH-143/144 (cheap same-question re-run fixing one threshold operator).
- **ARC-018 needs a governance decision**, not a new experiment: formally close the 2026-07-22 deferred re-adjudication now that its blocker (SP-CEM) has been resolved for 3 months.
- **Do not re-queue** Q-005/006/012/014/015/020/023/024/MECH-140/063 -- each is already correctly handled by existing claims.yaml state; re-queuing would duplicate work a later, better-informed run or reframing has already done.
