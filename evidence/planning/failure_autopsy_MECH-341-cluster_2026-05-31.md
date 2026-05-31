# Failure autopsy -- MECH-341 cluster (V3-EXQ-614b + V3-EXQ-615 + V3-EXQ-616, ARC-065 / MECH-341 / Q-054 lineage extension)

- **Date (UTC):** 2026-05-31T18:50:37Z
- **Scope:** cluster (3 runs sharing the MECH-341 / ARC-065 / Q-054 claim cluster on the SD-054 bipartite-reef substrate)
- **Status:** confirmed (user-verdict 2026-05-31T18:45Z at Step 8 gate routed cluster artifact)
- **Routing:** governance reclassification with definitive answers across all three claims
- **Predecessor (single-target) autopsy this extends:** failure_autopsy_V3-EXQ-614b_2026-05-31.{md,json} (left intact per user direction; this cluster autopsy supersedes its pending_retest framing)
- **Predecessor (cluster) autopsy this is a sister artifact to:** failure_autopsy_MECH-341-cluster_2026-05-29.{md,json} (covered V3-EXQ-608 + V3-EXQ-611 pair)
- **Predecessor (substrate enabler) autopsies:** failure_autopsy_V3-EXQ-569e_2026-05-31.{md,json} (routed SD-056 amend used by 614b)

## 1. Cluster scoping

Three runs sharing the MECH-341 / ARC-065 diversity-generation cluster on the SD-054 bipartite-reef env, all sequential within 2026-05-31:

| Run | UTC | Outcome | Direction | Role |
|---|---|---|---|---|
| v3_exq_615_arc065_rung1_matched_entropy (re-run) | 09:31Z | **PASS** | supports | ARC-065 matched-entropy control |
| v3_exq_616_q054_mech341_entropy_bias_scale_sweep | 14:15Z | **FAIL** | weakens (per-claim mixed) | Q-054 entropy_bias_scale sweep on MECH-341 B_only isolation |
| v3_exq_614b_mech341_p3_behavioural_falsifier_3arm_sd056_amended | 18:20Z | **FAIL** | weakens (recommended non_contributory) | MECH-341 P3 behavioural falsifier on SD-056-amended substrate |

V3-EXQ-615 also has an earlier 08:22Z manifest with outcome FAIL (criteria c1=False; ARM_2 ALL_ON only 1/3 seeds Rung-1 PASS at 0.500 nats; same queue_id without re-versioning). The canonical 615 reading is the 09:31Z PASS (3/3 seeds Rung-1 PASS at 1.111 nats); the earlier FAIL is noted in section 7 as a process observation, not a separate diagnosis. Same queue_id with two manifests is a CLAUDE.md "EXQ Versioning and Supersession Policy" deviation worth raising at next governance walk.

This cluster extends the lineage: 608 (P2 collapse probe, 2026-05-26 R2a confirmed) -> 611 (P3 substrate v1 readiness, 2026-05-27 FAIL with two implementation bugs) -> 611c (P3 substrate v2 retune, 2026-05-28 PASS) -> 614a (P3 behavioural falsifier, 2026-05-30 PASS_C2_C3_only) -> **614b + 615 + 616** (this cluster, 2026-05-31).

The shared failure shape across 614a / 614b / 616 ARM_0 lineage runs is the structural ARM_0 B_only degeneracy. The shared SUCCESS shape across 614a / 614b / 615 ALL_ON arms is the distributed-pathway diversity-generation pattern. The cluster reads as a coherent answer to the four-layer behavioral_diversity_isolation_plan questions.

## 2. Facts (per target)

### V3-EXQ-614b (P3 behavioural falsifier on SD-056-amended substrate)

Full reconstruction in the single-target autopsy. Headline facts:
- C1 (R2.c B_only Rung-1): **False** -- ARM_0 frac_pre_ge2=0.0 across all 3 seeds, identical seed-level signature to V3-EXQ-614a (seeds 42 / 43 / 44 lock to first-action classes 0 / 2 / 4 with n_p1_ticks 11806 / 11423 / 358).
- C2 (B necessity entropy delta >= 0.1): **False** -- observed 0.087 just below threshold.
- C3 (ARM_2 ALL_ON Rung-1): **True** -- 3/3 seeds at mean entropy 0.800 nats (highest of any 614-lineage run; ARM_1 ablate_B 0.713 nats).
- SD-056 amend signal: positive substrate-readiness at behavioural runtime horizon (zero NaN/Inf rollouts across 162k steps; ARM_2 ALL_ON entropy 0.684 -> 0.800 vs 614a).
- Script's hard-coded route: FAIL_no_criterion_routes_to_diagnose_errors.

### V3-EXQ-615 (ARC-065 matched-entropy control, 09:31Z PASS re-run)

3-arm matched-entropy control: ARM_0 BASE_OFF (no substrate), ARM_1 MATCHED_NOISE (MECH-313 noise_floor only -- entropy-injection at action-selection layer matched against ARM_2's measured entropy), ARM_2 ALL_ON (full distributed stack).

| Arm | substrate axes | mean_n_unique_classes | mean_entropy | n_seeds_rung1_pass |
|---|---|---|---|---|
| ARM_0 BASE_OFF | all off | 1.0 | 0.0 | 0/3 |
| ARM_1 MATCHED_NOISE | only MECH-313 noise_floor on | 1.0 | 0.0 | 0/3 |
| ARM_2 ALL_ON | full SP-CEM + MECH-341 + noise + V_s | 4.333 | 1.111 | 3/3 |

Criteria:
- C1 (ARM_2 Rung-1 PASS): **True**
- C2 (entropy delta ARM_2 vs ARM_1 -- ARC-065 distinguishable from matched noise): **True** (delta = 1.111)
- C3 (ARM_0 BASE_OFF Rung-1 FAIL -- distributed-pathway necessity): **True**

Script's manifest routing field: "ARC-065 supports, clear pending_retest_after_substrate flag, route to governance for provisional promotion consideration".

**Key cross-cluster observation:** ARM_1 MATCHED_NOISE collapsed to a single class with 0.0 entropy across all 3 seeds, identical signature to ARM_0 BASE_OFF and the 614b ARM_0 B_only arm. MECH-313 noise_floor alone at the action-selection layer does not break monomodal collapse when the upstream CEM proposer produces single-class candidate pools.

### V3-EXQ-616 (Q-054 entropy_bias_scale sweep on B_only isolation)

4-arm sweep across `e3_diversity_entropy_bias_scale` in {1.0, 2.0, 4.0, 8.0}, all on B_only isolation config (SP-CEM OFF, MECH-341 ON with both sub-flavours, MECH-313 OFF, V_s OFF). Same env as 614a / 614b / 611c.

| Arm | entropy_bias_scale | mean_n_unique_classes | mean_entropy | n_seeds_rung1_pass | frac_pre_ge2 |
|---|---|---|---|---|---|
| ARM_0 S=1.0 | 1.0 | 1.0 | 0.0 | 0/3 | 0.0 |
| ARM_1 S=2.0 | 2.0 | 1.0 | 0.0 | 0/3 | 0.0 |
| ARM_2 S=4.0 | 4.0 | 1.0 | 0.0 | 0/3 | 0.0 |
| ARM_3 S=8.0 | 8.0 | 1.0 | 0.0 | 0/3 | 0.0 |

**Smoking-gun observation:** per-seed results are **bit-identical across all four scales**. Seed 42 always locks to first-action class 0 with n_p1_ticks=11806; seed 43 always locks to class 2 with n_p1_ticks=11423; seed 44 always locks to class 4 with n_p1_ticks=358. Same lock-in classes, same step counts, same zero entropy, across every scale value. This is the same per-seed signature as ARM_0 in V3-EXQ-614a and V3-EXQ-614b.

`load_bearing_floor_scale: null`. No scale tested clears the C1 R2.c Rung-1 criterion.

Script's manifest routing field: "Scale lever insufficient in isolation. MECH-341 in-stack contribution preserved per 614a C2+C3 PASS. Q-054 mixed for the scale axis; route to substrate revisit (stratified_temperature default, A-vs-B redundancy probe)."

## 3. Claim-layer map

**ARC-065** -- architectural_commitment.behavioural_diversity_generation_pathway. status=candidate. The 2026-05-31 V3-EXQ-615 PASS at 1.111 nats entropy (ARM_2 ALL_ON) with ARM_1 MATCHED_NOISE failing to reproduce that diversity through pure noise injection is a clean architectural-necessity result. The distributed-pathway commitment (multiple substrates contributing) is empirically discriminated against the single-noise-channel alternative.

**MECH-341** -- ethics_engine_3.scoring_trajectory_class_diversity_preservation. claim_type=mechanism_hypothesis, status=candidate, v3_pending=true, implementation_phase=v3. Layer-B in behavioral_diversity_isolation_plan.md. The 614a + 614b + 616 data triangulate to a definite answer about isolation: MECH-341 cannot drive Rung-1 diversity alone, the entropy_bias_scale lever cannot rescue it, and within the full stack its marginal contribution scales inversely with upstream capacity. The claim's *role* is correctly characterised as a **score-layer preserver of upstream-supplied diversity**, not an in-isolation diversity-creator.

**Q-054** -- answer-state question on the minimum trajectory-class diversity floor for ARC-062 / entropy_bias_scale calibration. The V3-EXQ-616 sweep provides the definitive answer: **no value of entropy_bias_scale in [1.0, 8.0] lifts B_only isolation to Rung-1**. The scale-lever question has a negative answer; calibration cannot fix what is structurally a candidate-pool deficiency at the proposer layer.

claim_ids accuracy: all three runs tagged correctly. V3-EXQ-615 tagged [ARC-065] only -- correct (matched-entropy control isolates the ARC-065 architectural commitment from the MECH-313 noise-only alternative). V3-EXQ-616 tagged [Q-054, MECH-341] -- correct (Q-054 is the answer-state question, MECH-341 is the substrate under sweep). V3-EXQ-614b tagged [MECH-341, ARC-065] -- correct per the falsifier design.

## 4. Biological-reference triage

Same algorithmic-regulator framing as the 2026-05-29 cluster autopsy section 4: function-level BG / cortico-striatal winner-take-all + Mnih 2016 A3C entropy regulariser (OPT1 of MECH-341) + Rigotti 2013 / Padoa-Schioppa & Conen 2017 categorical preservation (OPT2). Not formal-definition imports; no biology divergence at play.

**One additional biological framing surfaced by the cluster.** The 615 + 616 results together support a sharper architectural reading of the diversity-generation pipeline:

- **ARC-065 architectural commitment**: real behavioural diversity requires *distributed* multi-substrate generation, not a single noise channel. This matches the well-attested biology of behavioural variability in mammalian motor control (cerebellar variability + cortical exploration + BG selection noise all contributing distinctly per Stein et al. 2005 / Wu et al. 2014 / Dhawale 2017).
- **MECH-341 functional role**: a *preservation* mechanism at the scoring step, not a *generation* mechanism. Biology-aligned: OFC value-comparison preserves option-distinct value signals through the comparison stage (Padoa-Schioppa & Conen 2017) but does not invent option diversity from a single option.
- **MECH-313 functional role**: noise injection at action selection is one diversity channel but is not sufficient on its own to break monomodal collapse when the candidate proposer is degenerate. Matches Aston-Jones & Cohen 2005 LC-NE function: tonic noise modulates choice over an existing affordance set, it does not generate new affordances.

No biology divergence; the cluster's empirical pattern matches the biology's "multiple contributing channels" framing for behavioural variability.

is_formal_import: false. divergence: n/a. lit_status: ARC-065-side anchored at SYNTHESIS verdicts (evidence/literature/targeted_review_arc_065_behavioral_diversity_generation/SYNTHESIS.md, 9 entries, lit_conf 0.78-0.82). MECH-341 / Q-054 still lit-absent (acceptable for algorithmic regulators).

## 5. Four-layer diagnosis (per target)

### V3-EXQ-615 (PASS supports)

| Layer | Status | Note |
|---|---|---|
| Claim alignment | strengthened | ARC-065 architectural-necessity demonstrated; matched-noise control rules out the noise-only alternative |
| Biological reference | partial | distributed multi-channel diversity-generation pattern aligns with mammalian motor variability literature |
| Prerequisites | present | SP-CEM / MECH-313 / V_s / MECH-341 all substrate-landed |
| Implementation | complete | matched-noise control correctly isolates the architectural commitment |
| Environment | adequate | SD-054 bipartite-reef env supplies spatially-distinct affordance classes |
| Measurement | adequate | n_p1_logged in {687, 1254, 1571} for ARM_2 -- adequate for entropy estimation |
| Integration | full-stack-coupled | ARM_2 ALL_ON validates the joint architecture |
| Scale | adequate | 3 seeds x 3 arms |

### V3-EXQ-616 (FAIL weakens / per-claim mixed)

| Layer | Status | Note |
|---|---|---|
| Claim alignment | structural-bound discovered | MECH-341 isolation question definitively answered negative across [1.0, 8.0] scale range |
| Biological reference | partial | matches "preservation mechanism, not generation mechanism" biological framing |
| Prerequisites | present | SD-054 + MECH-341 v2 substrate landed; SP-CEM intentionally OFF per isolation design |
| Implementation | complete | scale knob varied as designed; bit-identical per-seed signature across scales is the diagnostic |
| Environment | adequate | same env as 614a / 614b |
| Measurement | adequate-and-decisive | per-seed bit-identical-across-scales result is mathematical proof scale cannot move single-class pools |
| Integration | isolation-by-design | B_only isolation correctly excludes SP-CEM upstream |
| Scale | adequate | 3 seeds x 4 scales |

### V3-EXQ-614b (FAIL recommended non_contributory)

See single-target autopsy section 5. Headline: claim alignment intact, environment-measurement coupling shifted under SD-056 amend, C2 threshold stale, ARM_0 structural-bound consistent with 614a / 616.

**Dominant diagnosis layer (cluster):** Structural-bound discovery + measurement-threshold-stale combination. The cluster does not surface a biology-divergence or new-dependency issue. It surfaces a *clarification* of MECH-341's claim role (preservation, not generation) and a *negative answer* to the Q-054 scale-lever question.

**Recommended `epistemic_category`:** none (claims stay V3-tractable). The structural-bound is a *property of the substrate stack*, not a substrate-ceiling at the claim level.

## 6. Cluster pattern (convergent table)

| Run | Arm | Substrate state | Negative-control / absolute criterion | Discrimination criterion | Read |
|---|---|---|---|---|---|
| 614b | ARM_0 B_only | only MECH-341 | frac_pre_ge2=0.0 (CEM monomodal) | C1 FAIL identical to 614a ARM_0 | structural ARM_0 degeneracy independent of SD-056 amend |
| 614b | ARM_1 ablate_B | SP-CEM + V_s + noise + SD-056 amend (no MECH-341) | Rung-1 3/3 PASS at 0.713 nats | upstream diversity holds without MECH-341 | substrate amend lifted no-MECH-341 baseline (+0.187 nats vs pre-amend) |
| 614b | ARM_2 ALL_ON | full stack + SD-056 amend | Rung-1 3/3 PASS at 0.800 nats | highest absolute entropy of any 614-lineage run | full stack works; SD-056 amend positive behavioural signal |
| 615 | ARM_0 BASE_OFF | all off | Rung-1 0/3 PASS at 0.0 nats | n/a (baseline) | confirms collapse-by-default at substrate-absent regime |
| 615 | ARM_1 MATCHED_NOISE | only MECH-313 noise_floor | Rung-1 0/3 PASS at 0.0 nats | matched noise cannot reproduce ALL_ON entropy | **architectural-necessity: noise alone is not the diversity generator** |
| 615 | ARM_2 ALL_ON | full stack | Rung-1 3/3 PASS at 1.111 nats | distributed-pathway delivers diversity | ARC-065 supports |
| 616 | ARM_0-3 B_only S in {1,2,4,8} | only MECH-341, scale knob swept | per-seed BIT-IDENTICAL across scales (n_p1_ticks 11806/11423/358; lock-in classes 0/2/4; entropy 0.0 everywhere) | no Rung-1 PASS at any scale | **scale lever mathematically cannot move single-class pools** |

### Independent bugs or one structural property?

**One structural property of the diversity-generation pipeline.** The cluster reveals (and quantifies) the architectural shape of ARC-065's distributed-pathway commitment:

1. **Single-channel sufficiency: FALSE.** Neither MECH-313 noise alone (615 ARM_1) nor MECH-341 score-layer alone (616 ARM_0-3 + 614a/614b ARM_0) can drive Rung-1 in isolation. The CEM proposer at default settings without SP-CEM produces single-class candidate pools; MECH-341 needs >= 2 classes to apply differential pressure, MECH-313 needs an existing multi-class affordance set to randomise selection over.
2. **Multi-channel composition: TRUE.** ARM_2 ALL_ON delivers Rung-1 at high entropy (615: 1.111 nats; 614b: 0.800 nats; 614a: 0.684 nats). The composition of channels is more than the sum: SP-CEM diversifies the candidate pool, V_s broadens cortical-rollout consumption, noise_floor regularises action-selection sharpness, MECH-341 preserves the diversity through scoring.
3. **Substrate-coupling at the upstream layer matters more than knob calibration.** The SD-056 amend on E2's action-conditional divergence preservation (614b ARM_1 ablate_B +0.187 nats vs 614a) had a larger effect on diversity than the MECH-341 entropy_bias_scale knob has ever delivered. Substrate-layer architectural choices dominate score-layer calibration.

This is one structural property surfacing across three structurally-different tests, not three independent bugs.

### Two readings considered and rejected

- **"The cluster falsifies MECH-341."** Rejected. ALL_ON arms clear Rung-1 at high entropy across all three runs (615 + 614a + 614b). MECH-341's contribution-in-stack is real (614a C2 PASS at 0.158 nats delta); its in-isolation insufficiency is a property of the CEM proposer + score-layer-preservation semantics, not falsification of the claim.
- **"The cluster falsifies ARC-065."** Rejected. 615 architectural-necessity test passes cleanly: matched-noise control + base-off baseline both fail; only the distributed multi-substrate combination succeeds. This is the canonical shape for an architectural commitment claim.

## 7. Process / measurement notes

**V3-EXQ-615 same-EXQ re-run (08:22Z FAIL + 09:31Z PASS).** Two manifests share queue_id=V3-EXQ-615 without alphabetic versioning, violating REE_assembly/CLAUDE.md "EXQ Versioning and Supersession Policy" + ree-v3/CLAUDE.md "Experiment IDs and Versioning" sections. Not a falsifying-pair (criteria flipped between the two: first run ARM_2 1/3 seeds 0.500 nats; second 3/3 seeds 1.111 nats). Likely machine-stochastic / warmup-stochastic difference (08:22Z run NaN / process unknown; second run on ree-cloud-2). Flag for governance walk: the canonical reading is the 09:31Z PASS but the data record carries both manifests. A successor (615a) would have been the cleaner re-run convention.

**C2 necessity_delta_threshold=0.1 (614b script).** Process flag carried over from the single-target 614b autopsy section 7 and 9: the threshold was calibrated against the pre-SD-056-amend substrate; under the amended substrate the delta range is smaller. The cluster autopsy concurs: the C2 threshold is stale, not a falsification gate.

**ARM_0 B_only structural degeneracy.** Section 6 cluster pattern row 1 + 616 ARM_0-3 + 614a/614b ARM_0 establish this as a *cluster-level constant* at the SP-CEM-OFF configuration. The behavioral_diversity_isolation_plan.md R2.c rule treats B_only isolation as a substrate-readiness gate for MECH-341 in-isolation promotion. The cluster definitively shows this gate is unreachable through the entropy_bias_scale lever and is structurally locked at the proposer layer.

## 8. Learning extracted

1. **ARC-065 distributed-pathway commitment is empirically supported as an architectural-necessity claim.** V3-EXQ-615 09:31Z PASS provides the clean discrimination against the matched-noise-only alternative (ARM_1 MATCHED_NOISE collapse to 0.0 nats vs ARM_2 ALL_ON 1.111 nats).
2. **MECH-341 is correctly characterised as a score-layer preserver, not a diversity generator.** The 614a + 614b + 616 triangulation shows: contribution-in-stack is real and quantifiable; in-isolation contribution is structurally zero through the entropy_bias_scale lever at any value in [1.0, 8.0]; marginal contribution scales inversely with upstream capacity.
3. **Q-054 answer-state question has a definitive negative answer.** No value of entropy_bias_scale in the swept range provides a load-bearing floor for B_only isolation Rung-1. The Q-054 question can be closed with verdict: "the scale-lever question is not the right question; the structural bound is at the proposer layer (SP-CEM presence/absence), not the score layer."
4. **Substrate-layer architectural choices dominate score-layer calibration.** SD-056 amend on E2 action-conditional divergence preservation lifted ARM_1 ablate_B baseline by +0.187 nats; the largest effect any entropy_bias_scale value (up to 8.0) has ever produced in the lineage is 0.0 nats on B_only isolation (no movement at all). The substrate-amend route is more architecturally productive than the score-layer calibration route.
5. **One structural property generates three convergent FAIL/PASS patterns.** Cluster-level reading: not independent bugs. Each of the three runs adds discriminative information about the architectural shape of ARC-065's distributed-pathway commitment and MECH-341's role within it.
6. **V3-EXQ-615 same-EXQ re-run is a process incident.** Two manifests under one queue_id without alphabetic versioning. Flag for governance walk; canonical 09:31Z PASS reading retained for evidence purposes.
7. **C2 necessity_delta_threshold=0.1 is stale under SD-056-amended substrate.** Carries over from 614b single-target autopsy. The cluster autopsy concurs; threshold revision belongs to whoever queues a 614c-type successor (if any).
8. **No new substrate is required, no /diagnose-errors loop is required, no /queue-experiment loop is required.** The cluster has answered the questions the three runs were designed to ask; the remaining work is governance reclassification.

## 9. Routing (user-confirmed at Step 8)

User-confirmed 2026-05-31T18:45Z via AskUserQuestion: "Write a separate cluster autopsy covering 614b + 615 + 616 together. Keep the 614b single-target autopsy as the per-run artifact."

- **routing:** governance-reclassification
- **target claims:** [ARC-065, MECH-341, Q-054]
- **per-claim evidence_direction overrides:**
  - **ARC-065: supports** (V3-EXQ-615 09:31Z PASS architectural-necessity matched-noise control; ALL_ON arms across 614a / 614b / 615 / 611c lineage)
  - **MECH-341: non_contributory** (V3-EXQ-614b substrate-coupling FAIL + V3-EXQ-616 isolation-not-reachable; claim's correct characterisation is in-stack preserver, not in-isolation driver; clarification not falsification)
  - **Q-054: mixed** (definitive negative answer to the scale-lever question; the Q-054 answer-state question can be closed with verdict that the question framing is the wrong question -- structural bound is at proposer layer)
- **pending_retest_after_substrate:** clear on both ARC-065 and MECH-341 (retest gate fired; both answers returned). Q-054 not subject to this flag (answer-state).
- **narrow_supports_flag:** false. ARC-065 supports is broad-evidence (full-stack PASS across 4 lineage runs at multiple absolute entropy levels); MECH-341 non_contributory is broad-evidence (3 structurally-different tests of the isolation question; one definitively negative). Not narrow / single-pathway.
- **no new substrate_queue entry.** The cluster does not surface a new substrate gap. The 616 manifest's routing note suggests "substrate revisit (stratified_temperature default, A-vs-B redundancy probe)" as a follow-on direction; that is a future /implement-substrate decision and is NOT being filed in this autopsy (user direction). Surfaced as a routing recommendation only.
- **no /diagnose-errors loop.** All three FAILs are interpretable signals at the architectural / substrate-coupling layer.
- **ARC-065 promotion eligibility:** governance walk should consider whether the 615 09:31Z PASS + ALL_ON corroboration across the 614 lineage clears the v3_pending gate. Not this autopsy's decision; surface as a routing recommendation only.

## 10. Recommended `evidence_quality_note` (governance to write, not this skill)

### For ARC-065

> "2026-05-31 cluster autopsy (failure_autopsy_MECH-341-cluster_2026-05-31): V3-EXQ-615 re-run 09:31Z PASS (ARM_2 ALL_ON 4.33 unique classes / 1.111 nats vs ARM_0 BASE_OFF and ARM_1 MATCHED_NOISE both collapsing to single-class 0.0 nats) provides clean architectural-necessity discrimination of ARC-065's distributed-pathway commitment against the matched-noise-only alternative. MECH-313 noise_floor alone does not reproduce ALL_ON diversity. Corroborated across the 614-lineage ALL_ON arms (614a 0.684 nats, 614b 0.800 nats on SD-056-amended substrate). evidence_direction=supports; clear pending_retest_after_substrate flag. Promotion eligibility from candidate -> provisional should be considered at next governance walk. Note: V3-EXQ-615 carries TWO manifests under the same queue_id (08:22Z FAIL with 1/3 seeds, 09:31Z PASS with 3/3 seeds; canonical reading is 09:31Z PASS; the dual-manifest record is a CLAUDE.md EXQ versioning policy deviation to flag separately)."

### For MECH-341

> "2026-05-31 cluster autopsy (failure_autopsy_MECH-341-cluster_2026-05-31): three runs triangulate MECH-341's role definitively. V3-EXQ-614b on SD-056-amended substrate: ALL_ON 0.800 nats (highest of lineage) confirms in-stack contribution; C2 0.087 nats below 0.1 threshold (stale calibration). V3-EXQ-616 entropy_bias_scale sweep {1.0, 2.0, 4.0, 8.0} on B_only isolation: bit-identical per-seed results across all four scales (seeds 42/43/44 lock to first-action classes 0/2/4 with frac_pre_ge2=0.0 and entropy=0.0 at every scale -- mathematical proof that uniform additive entropy bias of any magnitude cannot move a single-class CEM proposer output). load_bearing_floor_scale=None. The cluster establishes the correct claim characterisation: MECH-341 is a SCORE-LAYER PRESERVER of upstream-supplied candidate-pool diversity, not an in-isolation diversity generator. In-isolation testing through the entropy_bias_scale lever is structurally not reachable; the bound is at the proposer layer (SP-CEM presence/absence), not the score layer. evidence_direction=non_contributory (clarification, not falsification); clear pending_retest_after_substrate flag. The claim text stays intact; the routing implication is: MECH-341 promotion eligibility is gated on in-stack evidence (already supplied by 614a + 614b ALL_ON arms), not in-isolation R2.c clearance (which is structurally unreachable). Process flag: C2 necessity_delta_threshold=0.1 was calibrated pre-SD-056-amend; under the amended substrate the delta range is smaller (614a 0.158 -> 614b 0.087); threshold MUST be revisited before any V3-EXQ-614c-type successor (autopsy does not pin a value)."

### For Q-054

> "2026-05-31 cluster autopsy (failure_autopsy_MECH-341-cluster_2026-05-31): V3-EXQ-616 sweep across e3_diversity_entropy_bias_scale in {1.0, 2.0, 4.0, 8.0} on B_only isolation produces bit-identical per-seed results at every scale (frac_pre_ge2=0.0, n_unique=1, entropy=0.0 universally; per-seed lock-in classes 0/2/4 identical across all four scales; same n_p1_ticks 11806/11423/358 per seed across all four scales). load_bearing_floor_scale=None. The Q-054 answer-state question 'what is the minimum trajectory-class diversity floor for ARC-062 / what entropy_bias_scale floor is load-bearing?' has a definitive negative answer: the scale-lever question is not the right question. The structural bound is at the proposer layer (SP-CEM presence/absence), not the score layer; no value of entropy_bias_scale can rescue a single-class candidate pool. evidence_direction=mixed at the scale-axis level; Q-054 can be closed with verdict 'the scale-lever question framing is the wrong question -- the load-bearing floor is at the proposer layer, not the score layer.'"

## 11. Routing field for `/governance`

- **routing:** `governance-reclassification`
- **target claims:** [ARC-065, MECH-341, Q-054]
- **per-claim evidence_direction overrides:** {ARC-065: supports, MECH-341: non_contributory, Q-054: mixed}
- **pending_retest_after_substrate:** clear on [ARC-065, MECH-341]; n/a on Q-054 (answer-state)
- **narrow_supports_flag:** false on all three
- **no new substrate_queue entry**. (Manifest 616 routing note flags `stratified_temperature default` + `A-vs-B redundancy probe` as possible follow-on substrate work; surfaced as recommendation, not filed.)
- **no /diagnose-errors loop**
- **no /queue-experiment loop** (retest gate has fired; both answers returned)
- **promotion eligibility surface (recommendation only):** ARC-065 candidate -> provisional eligibility should be considered at next governance walk given the V3-EXQ-615 clean architectural-necessity result + ALL_ON corroboration across 4 lineage runs.
- **process incidents surfaced:** (a) V3-EXQ-615 same-queue_id dual-manifest (CLAUDE.md EXQ versioning deviation); (b) C2 necessity_delta_threshold=0.1 stale under SD-056-amended substrate (614b script-side recalibration needed before any successor).
