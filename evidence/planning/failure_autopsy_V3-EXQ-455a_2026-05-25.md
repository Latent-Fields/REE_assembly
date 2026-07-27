# Failure Autopsy -- V3-EXQ-455a + SD-032 Cluster Baseline Contamination

**Date:** 2026-05-25
**Session:** failure-autopsy-455a-igw022-20260525T043640Z
**IGW:** IGW-20260521-022 (deferred from /diagnose-errors per user gate selection 2026-05-25T03:33Z)
**Scope:** **cluster** (V3-EXQ-455a is the entry point; the load-bearing finding is a cluster-wide SD-032 baseline-contamination pattern)
**Status:** confirmed (user gate Step 8 selected "Recommend cluster-wide SD-032 audit")
**Related artefact:** [`2026-05-25_sd_032_baseline_contamination_cluster.md`](2026-05-25_sd_032_baseline_contamination_cluster.md)

## 0. Caveat about skill applicability

V3-EXQ-455a's result is ERROR (NotImplementedError raise), not FAIL. The /failure-autopsy skill is strictly scoped to FAILs. This autopsy is a **design autopsy** of the architectural-reassessment question the user routed to /failure-autopsy via the /diagnose-errors Step-7 gate. Carried in the autopsy format because the substantive output is governance-targeted recommendations on the SD-032 cluster, which is exactly what the autopsy artifact schema is for. Flagged here so the next /governance walk reads it correctly.

## 1. Facts -- no interpretation

### V3-EXQ-455a
- Script: [`ree-v3/experiments/v3_exq_455a_sd032a_salience_with_vs.py`](https://github.com/Latent-Fields/ree-v3/blob/main/experiments/v3_exq_455a_sd032a_salience_with_vs.py).
- Line 107: `raise NotImplementedError("V3-EXQ-455a gated. MECH-284 Phase 3 substrate landed 2026-04-24, but cascade gate V3-EXQ-476a/476b ran FAIL ... Do not run until SD-037 has landed and a new cascade gate has confirmed V_s flags break the baseline monostrategy lock.")`.
- Runner ran the script 2026-04-23T23:23:46Z on DLAPTOP-4.local, hit the raise, logged ERROR (exit code 1). Runner skip-on-completed prevents re-execution.
- The stub was written 2026-04-24 when SD-037 had not landed AND EXQ-476a/476b had FAILed. As of 2026-05-25: SD-037 substrate-landed 2026-04-25 (V3-EXQ-483b substrate-readiness PASS 2026-05-08); MECH-269b + MECH-284 substrate-landed (V3-EXQ-601 PASS 2026-05-21); ARC-065 SP-CEM substrate-landed as main-path default 2026-05-17 (V3-EXQ-567 PASS). EXQ-476a/476b themselves remain FAIL -- the V_s cascade gate via that pathway did not pass; the monostrategy lock the stub was waiting on was instead addressed at the candidate-generation layer by SP-CEM.

### V3-EXQ-455 (predecessor)
- Manifest `outcome: PASS`, `evidence_direction: supports`, `evidence_direction_per_claim: {SD-032a: supports, MECH-259: supports, MECH-261: supports}`.
- `pass_criteria_summary`: C1 trigger_count_natural>0 in >=2/3 seeds COORD_ON -> 2/3 PASS; C2 mean_operating_mode_entropy>0.3 nats -> 3/3 PASS; C3 write_gate_e3_policy std>0.01 -> 3/3 PASS; C4 backward-compat COORD_OFF gate-std<0.001 -> 3/3 PASS.
- `per_seed_results` COORD_OFF rows (all 3 seeds): `action_class_entropy: 0.0`, `trigger_count_natural: 0`, `write_gate_e3_policy_mean: 0.0`, `write_gate_e3_policy_std: 0.0`, `action_counts: {"1": 5542}`. **Every single one of 5,542 actions across the entire P2 evaluation window was action class 1.** Monostrategy lock confirmed.
- `per_seed_results` COORD_ON rows: `mean_operating_mode_entropy: 1.275`, `trigger_count_natural: 350`, `write_gate_e3_policy_std: 0.020`. Real coordinator activity.

### Cluster baseline-arm metrics (where recorded)
- V3-EXQ-445h (SD-032b/MECH-258/MECH-260, FAIL 2026-05-08): baseline-arm `action_class_entropy: 0.0` x 3 seeds.
- V3-EXQ-325d (SD-032c, FAIL 2026-04-20): baseline-arm entropy not captured in the flat manifest.
- V3-EXQ-447 (SD-032d, PASS 2026-04-23): baseline-arm entropy not captured.
- V3-EXQ-448 (SD-032e/MECH-094, PASS 2026-04-19): baseline-arm entropy not captured.
- All five cluster experiments ran before the ARC-065 SP-CEM main-path landing (2026-05-17). Two of the five record empirical monostrategy at the OFF / baseline arm; the other three ran on the same `CausalGridWorldV2` substrate at the same period.

## 2. Claim layer

| Claim | Type | Status | v3_pending | EQN posture today | Lead evidence |
|---|---|---|---|---|---|
| SD-032a | design_decision | **stable** | False | "Registered pre-implementation. See SD-032 parent." -- no substrate caveat | V3-EXQ-455 PASS (supports) |
| MECH-259 | mechanism_hypothesis | **stable** | False | same | V3-EXQ-455 PASS (supports) + V3-EXQ-447 PASS (supports) |
| MECH-261 | mechanism_hypothesis | **stable** | False | "Registered pre-implementation. 5 literature entries support... salience-network coordinator overlay is REE-specific and requires EXP-0148 ablation test after V3 implementation." -- no SP-CEM-baseline caveat | V3-EXQ-455 PASS (supports) |
| SD-032d | design_decision | candidate | True | none beyond "Registered pre-implementation" | V3-EXQ-447 PASS (supports) |
| SD-032e | design_decision | **stable** | False | "Registered pre-implementation. See SD-032 parent." | V3-EXQ-448 PASS (supports) |
| MECH-094 | mechanism_hypothesis | stable | (legacy invariant-flavour mechanism) | -- | V3-EXQ-448 PASS (supports) |
| SD-032b | design_decision | candidate | True | "V_s-monostrategy substrate gap blocks SD-032b validation; pending_retest_after_substrate." (free-text) | V3-EXQ-445h FAIL (weakens) |
| SD-032c | design_decision | candidate | True | "V_s-monostrategy substrate gap that blocks SD-032b validation. AIC harm_s_gain machinery is wired and structurally drive-dependent, but behavioural divergence cannot manifest until MECH-269 V_s landing." (free-text) | V3-EXQ-325d FAIL (does_not_support) |
| MECH-258 | mechanism_hypothesis | candidate | True | "EXQ-445h supports (C1 wins=2/3)" (mixed; substrate caveat not explicit) | V3-EXQ-445h partial supports |
| MECH-260 | mechanism_hypothesis | candidate | True | extended 2026-05-24 autopsy + 2026-05-25 V3-EXQ-603a measurement-gap caveats; substrate-baseline caveat not explicit | V3-EXQ-445h supports + V3-EXQ-603a non_contributory |

**The asymmetry:** the four stable claims in this cluster (SD-032a / SD-032e / MECH-259 / MECH-261) inherit their evidence from V3-EXQ-455 (and V3-EXQ-448) PASSes that ran against monostrategy-locked baselines. The candidate claims in this cluster (SD-032b/c, MECH-258/260) inherit their evidence from FAILs against the same monostrategy-locked baselines and have been caveated. The same substrate condition; the same substrate baseline; opposite treatment in claims.yaml. None of the five carries the structured `pending_retest_after_substrate` field, even where the free-text says exactly that.

## 3. Biological-reference triage

**Closest mechanism (SD-032a / MECH-259 / MECH-261):** anterior salience network (AIC + dACC hub: Menon & Uddin 2010; Craig 2009) coupled to a mode-conditioned consolidation-write gating system (lit-pull `targeted_review_systems_consolidation_waking_propagation`, MECH-261 aggregate lit_confidence 0.883). Distinct biological layer from hippocampal candidate generation (which is what SP-CEM / ARC-065 instantiates).

**Faithfulness:** not a formal-definition import. SD-032a is anchored to a network-level neuroanatomical claim (Menon & Uddin 2010). MECH-261 anchors to mode-conditioned write-gating biology with 5 entries. ARC-058 / ARC-033 are the formal-vs-biology contrast in the broader cluster, not these.

**Dependency on diverse rollouts:** under any biologically faithful reading, the salience network's job is to bias which OPERATING MODE the agent is in, not to manufacture behavioral diversity from nothing. Mode-arbitration on a monostrategy-locked baseline is the substrate version of asking "which lane is the driver in?" when there is only one lane open. The cluster's behavior under monostrategy doesn't say the salience cluster is wrong; it says the question wasn't testable.

**Compositionality reading:** ARC-065 SP-CEM and the SD-032 salience cluster are biologically distinct layers (candidate-generation vs operating-mode-arbitration). The default expectation is additive composition, not redundancy. This sharpens the post-SP-CEM retest question to: *"Holding the candidate-generation layer SP-CEM-diverse-by-default, does the salience coordinator (and its substrate sub-modules) still produce a measurable behavioral differential that is not already provided by SP-CEM?"* If yes: cluster validated against the new baseline. If no: the cluster either implements the wrong function or the test doesn't measure what the cluster actually does.

**Lit-pull status:** present for SD-032a (mean confidence ~0.80, 9 entries on the parent SD-032 lit-pull), MECH-261 (0.883 aggregate); other cluster members similar. No additional lit-pull is the autopsy's primary output -- the biology covers this cluster.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear (originally read as strengthened, weakened-by-baseline-shift on retrospective inspection)** | V3-EXQ-455 PASS tested SD-032a/259/261 under conditions where the COORD_OFF baseline produced 0/5542 action diversity. The PASS only proves the coordinator beats a broken baseline. The same applies to V3-EXQ-447 (SD-032d, MECH-259) and V3-EXQ-448 (SD-032e, MECH-094) in expectation. |
| Biological reference | clear | Menon-Uddin SAN + MECH-261 lit-synthesis; biology supports compositionality with SP-CEM, not redundancy. |
| Prerequisites | present at time-of-test; new upstream substrate (ARC-065) since | SD-032b dACC was wired (V3-EXQ-445); ARC-065 SP-CEM main-path landed AFTER all SD-032 cluster experiments (2026-05-17). |
| Implementation completeness | complete | SalienceCoordinator + DACCtoE3Adapter + per-substrate analogs all wired and exercised in the cluster manifests. |
| Environment adequacy | adequate at time-of-test; now ambiguous | CausalGridWorldV2 default config. SP-CEM main-path changes what the default-config COORD_OFF arm produces behaviorally. |
| Measurement adequacy | misleading post-SP-CEM | C1/C2/C3 measure direct coordinator outputs (trigger / mode entropy / gate modulation). These outputs will fire whether or not they ADD behavioral value over an SP-CEM baseline; behavioral differential is the missing criterion. |
| Integration adequacy | now incomplete | V3-EXQ-455 (and the rest of the SD-032 cluster) was not measured on top of the current main-path substrate stack. |
| Scale / capacity | adequate | 3 seeds x phased training (P0/P1/P2 50/100/50 eps) for the cluster's lead experiments. |

**Recommended `epistemic_category`** for all SD-032 cluster claims with pre-SP-CEM evidence: `standard` with `pending_retest_after_substrate: ARC-065`. **Not** `substrate_ceiling` -- that vocabulary is reserved for claims whose substrate cannot CARRY the discriminative signal; here the substrate is fine but the BASELINE was broken in a way that makes the substrate's apparent signal indistinguishable from substrate-supplied diversity at large.

## 5. Cluster pattern

See [`2026-05-25_sd_032_baseline_contamination_cluster.md`](2026-05-25_sd_032_baseline_contamination_cluster.md) for the full cluster table + two-reading framing. Summary: the SD-032 cluster is one structural property, not five independent experiment outcomes -- pre-SP-CEM substrate-broken baseline across the entire cluster, with governance applying caveats only to the FAIL outcomes. The PASS outcomes inherit the same baseline contamination and should carry parallel caveats.

This is *adjacent* to the 2026-05-03 substrate-ceiling pattern but distinct: substrate-ceiling describes substrate that cannot CARRY the signal; baseline-contamination describes a baseline that makes the substrate's signal LOOK like it did work the substrate may not have done.

## 6. Learning extracted

1. **Baseline-shift contamination** is a real epistemic hazard distinct from substrate-ceiling. A substrate landing as main-path retroactively reframes prior evidence collected against the previous baseline. ARC-065 SP-CEM main-path 2026-05-17 is the canonical example; the same pattern will recur every time a default-altering substrate lands.
2. **Governance asymmetry** between FAIL- and PASS-outcome substrate caveating is structurally inconsistent and worth a process correction: when a future governance walk applies a substrate caveat to a FAIL in a cluster, sibling PASSes from the same substrate condition should be audited at the same time, not deferred until they fail.
3. **V3-EXQ-455a's gating logic was right; its gating CONDITION was wrong.** The stub correctly identified that the V_s cascade gate needed to land before the V_s-enabled retest made sense. The cascade gate didn't land; SP-CEM landed at a different layer, achieving the same broad result. The stub kept waiting for the wrong landing. Lesson: substrate-gated stubs should reference the ARCHITECTURAL CONDITION ("diverse behavioral baseline available") rather than a specific named substrate ("V_s cascade gate"), so that any landing that satisfies the condition unblocks the stub.
4. **The SD-032 cluster is not falsified by this finding.** Its behavioral-value question is genuinely *untested* against an SP-CEM-diverse baseline. Demotion is not appropriate; substrate-conditional re-evaluation is.

## 7. Repair pathway

| Diagnosis | Recommended routing |
|---|---|
| All SD-032 cluster claims with pre-SP-CEM evidence | **/governance**: add EQN amendment + structured `pending_retest_after_substrate: ARC-065`; no demotion (highest threshold not met) |
| V3-EXQ-455a stale stub | **/governance** or low-touch script hygiene: mark non-runnable (docstring `[SUPERSEDED-2026-05-25-by-ARC-065-driven-retest]`) -- runner skip-on-completed already prevents re-execution; queue entry already not present |
| The SP-CEM-baseline differential question | **/queue-experiment**: commission new V3-EXQ (NEW number, not 455b -- the scientific question has changed) for COORD_OFF+SP-CEM vs COORD_ON+SP-CEM differential measurement. claim_ids re-evaluated from scratch. |

No edits to claims.yaml / manifests / review_tracker.json / substrate_queue.json / queue / scripts in this session.

## 8. Draft `evidence_quality_note` writes for /governance

These are the exact texts governance should write. Carried in `failure_autopsy_V3-EXQ-455a_2026-05-25.json` under `targets[].recommended_evidence_quality_note`.

**SD-032a:**
> [2026-05-25 autopsy]: V3-EXQ-455 PASS (2026-04-20) measured COORD_ON vs COORD_OFF on a `CausalGridWorldV2` configuration where the COORD_OFF baseline produced `action_class_entropy = 0.0` across all 3 seeds (5542/5542 actions = class 1). This is the monostrategy failure mode ARC-065 SP-CEM (main-path landed 2026-05-17) was designed to address at the candidate-generation layer. The supports tag is therefore "supports vs monostrategy-locked baseline," not "supports vs SP-CEM-diverse baseline." Behavioral-value question is **untested** against the post-2026-05-17 main-path substrate stack. `pending_retest_after_substrate: ARC-065`.

**MECH-259:**
> [2026-05-25 autopsy]: Both supporting experiments (V3-EXQ-455 PASS 2026-04-20, V3-EXQ-447 PASS 2026-04-23) ran on `CausalGridWorldV2` pre-SP-CEM main-path. V3-EXQ-455 OFF-arm `action_class_entropy = 0.0` confirmed empirically; V3-EXQ-447 OFF-arm entropy not captured but ran on the same substrate config. Trigger / mode-entropy / gate-modulation metrics measure direct coordinator outputs and will fire under SP-CEM too; the behavioral differential is the untested question. `pending_retest_after_substrate: ARC-065`.

**MECH-261:**
> [2026-05-25 autopsy]: V3-EXQ-455 PASS supports tag inherits the SD-032 cluster baseline-contamination pattern (see `evidence/planning/2026-05-25_sd_032_baseline_contamination_cluster.md`). MECH-261's biology lit-confidence (0.883) is unaffected; the V3 experimental tag specifically needs `pending_retest_after_substrate: ARC-065`.

**SD-032b, SD-032c, MECH-258, MECH-260:**
> [2026-05-25 autopsy]: Existing free-text V_s-monostrategy substrate caveats are confirmed and align with the cluster pattern. Promote the free-text reading to the structured `pending_retest_after_substrate: ARC-065` field. Existing free-text retained for the audit trail.

**SD-032d, SD-032e, MECH-094 (where evidence comes from an SD-032 cluster experiment):**
> [2026-05-25 autopsy]: V3-EXQ-447 / V3-EXQ-448 PASSes inherit the SD-032 cluster baseline-contamination pattern (see `evidence/planning/2026-05-25_sd_032_baseline_contamination_cluster.md`). `pending_retest_after_substrate: ARC-065`.

## 9. Routing decision -- confirmed by user at Step 8

User selected "Recommend cluster-wide SD-032 audit" at the Step 8 interactive gate 2026-05-25T04:36Z. Carried in the artifact as written. Next-step ownership:

1. **/governance**: apply the eight EQN amendments above + set `pending_retest_after_substrate: ARC-065` on each affected claim. Rebuild claims.json + run governance.sh. Note this is a process finding worth recording -- the FAIL-only substrate-caveat application asymmetry should become a routine check in the governance walk.
2. **Hygiene**: mark `ree-v3/experiments/v3_exq_455a_sd032a_salience_with_vs.py` non-runnable (docstring change). No queue removal needed -- it's already not in `experiment_queue.json`. Runner skip-on-completed prevents re-execution.
3. **/queue-experiment**: commission new V3-EXQ for SP-CEM-baseline differential test (new EXQ number; not 455b). Defer this until the user wants to spend the experimental budget; the cluster claims aren't blocking anything time-critical.
