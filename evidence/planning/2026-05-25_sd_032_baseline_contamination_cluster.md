# SD-032 Cluster -- Pre-SP-CEM Baseline-Contamination Pattern

**Date:** 2026-05-25
**Author:** failure-autopsy session failure-autopsy-455a-igw022-20260525T043640Z
**Scope:** SD-032a / SD-032b / SD-032c / SD-032d / SD-032e + MECH-258 / MECH-259 / MECH-260 / MECH-261 / MECH-094 (where evidence comes from an SD-032 cluster experiment)
**Status:** Observation note -- for /governance application. No claim status changes proposed in this doc; the per-target autopsy `failure_autopsy_V3-EXQ-455a_2026-05-25.{md,json}` carries the recommended `evidence_quality_note` / `pending_retest_after_substrate` writes.
**Related:** `failure_autopsy_V3-EXQ-455a_2026-05-25.md`; IGW-20260521-022.

## Summary

Every experiment in the SD-032 cluster whose `per_seed_results` records `action_class_entropy` for its OFF / baseline arm shows **action_class_entropy = 0.0** -- the same monostrategy-locked baseline (every action collapses to a single class). This is the substrate failure mode ARC-065 SP-CEM was designed to fix, landed as main-path default 2026-05-17. **Every SD-032 cluster experiment ran BEFORE 2026-05-17.**

Governance has applied `evidence_quality_note` substrate caveats to the FAIL experiments in this cluster (SD-032b/c) but not to the PASS experiments (SD-032a/d/e and MECH-094/259/261). The asymmetry is structurally inconsistent: the substrate condition is identical across the cohort; only the experiment outcome differed. PASS evidence collected against a substrate-broken baseline is no less baseline-contaminated than FAIL evidence collected against the same baseline.

## The cluster table

| EXQ | Date | Substrate target | Outcome | Baseline arm `action_class_entropy` | Current claim status | Current EQN substrate caveat |
|---|---|---|---|---|---|---|
| V3-EXQ-455  | 2026-04-20 | SD-032a + MECH-259 + MECH-261 | PASS  | **0.0 / 0.0 / 0.0** (3 seeds, all 5542 actions = class 1) | SD-032a / MECH-259 / MECH-261 = **stable** | none beyond "Registered pre-implementation. See SD-032 parent." |
| V3-EXQ-445h | 2026-05-08 | SD-032b + MECH-258 + MECH-260 | FAIL  | **0.0 / 0.0 / 0.0** | SD-032b / MECH-258 / MECH-260 = candidate | "V_s-monostrategy substrate gap blocks SD-032b validation; pending_retest_after_substrate" (free-text in EQN; structured field absent) |
| V3-EXQ-325d | 2026-04-20 | SD-032c (AIC) + SD-021 | FAIL  | (not recorded in flat manifest) | SD-032c = candidate | "V_s-monostrategy substrate gap that blocks SD-032b validation" (free-text in EQN; structured field absent) |
| V3-EXQ-447  | 2026-04-23 | SD-032d (PCC) + MECH-259 | PASS  | (not recorded in flat manifest) | SD-032d = candidate, MECH-259 = stable | none beyond "Registered pre-implementation. See SD-032 parent." |
| V3-EXQ-448  | 2026-04-19 | SD-032e (pACC) + MECH-094 | PASS  | (not recorded in flat manifest) | SD-032e = stable, MECH-094 = stable | none beyond "Registered pre-implementation. See SD-032 parent." |

All five experiments ran before the ARC-065 SP-CEM main-path landing (2026-05-17). The two for which `action_class_entropy` IS recorded confirm the monostrategy lock empirically; the other three ran on the same `CausalGridWorldV2` substrate at the same period, so the baseline-contamination prior holds in expectation even where the metric was not collected.

## Why this is the load-bearing signal

The cluster shape is not "five independent experiments at varying outcomes." It is one structural property: **the SD-032 cluster was tested under a substrate regime in which the OFF arm could not produce behaviorally diverse rollouts**. The PASS / FAIL split is informative only relative to that broken baseline:

- A FAIL on a monostrategy baseline means the substrate-under-test ALSO couldn't break out of monostrategy (already caveated for SD-032b/c).
- A PASS on a monostrategy baseline means the substrate-under-test DID break out of monostrategy -- but it doesn't say whether the substrate is doing real work above and beyond what the now-default SP-CEM already provides (NOT caveated for SD-032a/d/e/MECH-259/261/094).

Both readings reduce to the same governance ask: **retest against an SP-CEM-diverse baseline before treating the prior evidence as conclusive in either direction.**

## Two readings (both consistent with the cluster shape)

**Reading A -- compositional, brains-are-existence-proof default:** SP-CEM (candidate-generation layer) and the SD-032 salience cluster (operating-mode-arbitration layer) are biologically distinct mechanisms that should compose additively (Menon & Uddin 2010 anterior salience network is a network-level operating-mode arbiter, distinct from hippocampal candidate generation). Under this reading, the PASSes were measuring a real substrate effect; a retest against SP-CEM should preserve the supports tags with a sharper differential signal. The candidate-cohort FAILs are then genuinely about something else (consumer-pathway absent / measurement gap / etc., as the existing EQNs note).

**Reading B -- SP-CEM-subsumes:** SP-CEM at the candidate-generation layer makes the operating-mode arbiter redundant for the diversity-as-end objective the SD-032 cluster's existing pass criteria measure. Under this reading, the PASS tags would soften to "supports relative to a substrate-broken baseline that no longer exists" and the cluster needs re-grounded pass criteria that measure what the salience network adds biologically (e.g. context-appropriate write-gate modulation under genuine task-mode transitions), not behavioral diversity at large.

Both readings yield the same near-term governance action: **apply `pending_retest_after_substrate: ARC-065` across the cluster.** The retest result discriminates between A and B.

## Relation to the existing 2026-05-03 substrate-ceiling cluster

The 2026-05-03 cross-claim pattern doc (`2026-05-03_substrate_ceiling_cross_claim_pattern.md`) flagged a convergent shape: negative-control / absolute criteria pass while discrimination criteria fail. **Today's pattern is structurally adjacent but distinct.** Substrate-ceiling describes claims whose substrate cannot CARRY the discriminative signal; baseline-contamination describes claims whose BASELINE is broken in a way that makes the substrate's signal look like the substrate did the work. Both are pre-`/governance`-cycle observation notes; both apply to a real cluster; the right `epistemic_category` for affected claims differs (substrate_ceiling vs `standard` + `pending_retest_after_substrate`).

## Specific governance recommendations

Carried in the per-target autopsy `failure_autopsy_V3-EXQ-455a_2026-05-25.json` under `targets[].recommended_*`. Summary:

1. **EQN amendment**, all SD-032 cluster members carrying "supports" tags from pre-2026-05-17 evidence (SD-032a, SD-032d, SD-032e, MECH-094, MECH-259, MECH-261): note the SP-CEM-naive baseline; set structured `pending_retest_after_substrate: ARC-065`.
2. **EQN amendment**, all SD-032 cluster members already carrying free-text V_s-monostrategy notes (SD-032b, SD-032c, MECH-258, MECH-260): promote the free-text to the structured `pending_retest_after_substrate: ARC-065` field. Existing free-text retained for the audit trail.
3. **V3-EXQ-455a script + queue entry**: mark non-runnable. Either delete the script + remove the queue entry (cleanest), or add a `[SUPERSEDED-2026-05-25-by-ARC-065-driven-retest]` block to the docstring. The runner's skip-on-completed already prevents re-execution; this is hygiene.
4. **Commission a new V3-EXQ** (NEW number, not 455b -- the scientific question has changed) for the SP-CEM-baseline differential test: COORD_OFF+SP-CEM vs COORD_ON+SP-CEM, same C1/C2/C3 metric family as V3-EXQ-455, plus a C5 behavioral-differential criterion that the original V3-EXQ-455 didn't carry. claim_ids re-evaluated from scratch -- likely shifts to include ARC-065 / MECH-326 contrast tags.

No edits to claims.yaml / manifests / review_tracker / substrate_queue / queue / script in this session.
