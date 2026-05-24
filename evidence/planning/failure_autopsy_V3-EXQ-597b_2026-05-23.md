# Failure Autopsy: V3-EXQ-597b (MECH-258)

**Generated:** 2026-05-24T05:51:35Z
**Skill:** /failure-autopsy
**Scope:** single
**Status:** confirmed (user confirmed routing 2026-05-24T05:51Z)

---

## 1. Target

- **Run ID:** v3_exq_597b_mech258_pe_vs_raw_post_spcem_20260521T131756Z_v3
- **Queue ID:** V3-EXQ-597b
- **Claim tested:** MECH-258 (cingulate.precision_weighted_pain_PE)
- **Manifest verdict:** FAIL
- **Evidence direction (manifest):** mixed
- **Supersedes:** V3-EXQ-597 (non_contributory -- post-clip saturation voided C2)

---

## 2. Facts Reconstruction

### Pass criteria

| Criterion | Description | Result |
|-----------|-------------|--------|
| C0 | Policy entropy: agent learns non-uniform policy | PASS (3/3 seeds) |
| C1 | E2_harm_a forward R2 >= 0.3 in P2 | PASS (2/3 seeds; seed42=0.912, seed7=0.937, seed13=-1.624 FAIL) |
| C2 | corr(bias_pre_clip, model_pe) > corr(bias_pre_clip, raw_norm) + 0.05 in >=2/3 seeds | FAIL (1/3 wins: seed42 delta=-0.179, seed7 delta=-0.126, seed13 delta=+0.137) |

Evidence direction logic: C1 passes but C2 fails -> "mixed".

### Per-seed summary (PE_FORWARD condition)

| Seed | C1 R2 | pre_clip_bias mean | post_clip_bias mean | saturation_frac | corr_model_pe | corr_raw_norm | delta | C2 |
|------|-------|-------------------|--------------------|-----------------|--------------|-----------|----|--|
| 42 | 0.912 | 10.53 | 2.0 | 1.0 | 0.079 | 0.258 | -0.179 | FAIL |
| 7 | 0.937 | 11.14 | 2.0 | 1.0 | -0.114 | 0.012 | -0.126 | FAIL |
| 13 | -1.624 | 10.06 | 2.0 | 1.0 | 0.318 | 0.181 | +0.137 | PASS |

### Critical observation: universal post-clip saturation

bias_clip_saturation_frac = 1.0 and mean_score_bias_post_clip_abs = 2.0 in EVERY seed of
BOTH conditions (PE_FORWARD and RAW_NORM_ABLATION). The dACC output to E3 is a constant 2.0
in every P2 step of every seed in every condition.

Pre-clip magnitudes (~10-12) are 5-6x above dacc_bias_max_abs=2.0. E3 received no variation
in the dACC signal across conditions -- behavioral discrimination between arms is structurally
impossible.

### Seed 13 "win" is artifactual

Seed 13 produced the only C2 win (+0.137) but is a degenerate regime: C1 R2=-1.624 (forward
model did not train), p2_bias_samples=170 (vs seed7: 2042), action distribution skewed to
action 4 (105/170 = 62%). The positive corr_delta is a sampling artifact, not evidence that
PE drives the bias under normal training. Any future iteration should exclude C2 scoring for
seeds where C1 R2 < 0.3.

### Predecessor comparison

597 (non_contributory): used post-clip bias -- always 2.0, Pearson r undefined across all
seeds/conditions.

597b fix: correctly switched to pre-clip telemetry via _dacc_bias_pre_clip_tensor(). The
Pearson r is now computable, but the pre-clip bias is still dominated by the suppression term,
diluting the PE signal below detectability.

### Failed criterion

C2 (discrimination criterion). C0 and C1 pass. This is NOT the substrate-ceiling fingerprint
(absolute/negative-control passes + discrimination fails = ceiling). The suppression term
dominates the pre-clip bias; even a perfectly functioning PE signal would be diluted below
the C2 detection threshold.

---

## 3. Claim-Layer Mapping

**MECH-258** (cingulate.precision_weighted_pain_PE)

- Status: candidate, v3_pending=true, implementation_phase=v3
- Claim: z_harm_a enters action selection as a precision-weighted PE against E2_harm_a,
  not as raw magnitude
- Depends on: SD-020, SD-032b, ARC-033, SD-003
- Prior evidence: EXQ-445h supports C1 (wins=2/3, harm_a forward R2=0.94-0.99)

**Did the experiment test the claim under conditions where the claim could express itself?**

No. The post-clip output was a constant 2.0 in all steps of all seeds of both conditions.
E3 received no variation in the dACC signal. The behavioral contrast needed to detect any
difference between PE_FORWARD and RAW_NORM_ABLATION never materialized. The claim was not
fairly tested.

Claim tags are accurate -- MECH-258 is the correct tag, not inherited without re-evaluation.

---

## 4. Biological-Reference Triage

### Closest mammalian reference mechanism

Seymour 2019 (Neuron): pain-as-precision-weighted-control-signal framework. The dACC/aMCC
reads nociceptive input as a precision-weighted prediction error against an internal pain
forward model. Precision = function of controllability + variance of recent PE. Same physical
pain input produces large behavioral adjustment when precision is high (uncontrollable,
unexpected) and small adjustment when precision is low (expected, controllable). This is
exactly what MECH-258 claims.

### Surrounding dependencies in real brains

- Pain forward model in anterior insula (Horing & Buchel 2022, Ploghaus 1999) -- unsigned PE
  computed in AI regardless of modality; signed PE is pain-specific in dorsal posterior
  insula. Architectural fingerprint: shared trunk + per-stream heads (ARC-058).
- dACC/aMCC integration of PE + cognitive conflict + control demand -> behavioral-adjustment
  magnitude (Shackman 2011 meta-analysis, Kolling/Scholl 2015 effort learning).
- ACC-NAc coupling for striatal-analog action-value target write (Baliki 2010 -- learnable
  weight, shifts under chronic pain).
- Song et al. 2021 biophysical model: S1 (sensory-discriminative) + ACC (affective) coupled
  populations, fits rat LFP; two coupled populations, not one or two independent.

### Is this a formal-definition import?

No. MECH-258 is a biological translation (precision-weighted PE as the cingulate read of
z_harm_a), not a formal-definition import (Pearl counterfactual, Shannon info, etc.).
The mechanism has clear mammalian substrate.

### Lit status

PRESENT -- two targeted reviews directly address MECH-258:
- targeted_review_pain_predictive_coding_substrate (2026-04-19): 9 entries; strong support
  for shared-trunk + per-stream-head architecture and precision-weighted PE. Recommendation:
  shared substrate confidence 0.75.
- targeted_review_cingulate_integration_substrate (2026-04-19): 9 entries; Seymour 2019 is
  the load-bearing anchor; confirms dACC as the adaptive-control integrator.

### Does the failure match a missing-dependency signature?

No. All dependencies are implemented (SD-020, E2_harm_a, SD-032b, SP-CEM active). The C1
PASS (R2=0.91-0.94 in working seeds) confirms E2_harm_a trains correctly. The FAIL is a
measurement instrument problem, not a missing dependency.

---

## 5. Four-Layer Diagnosis

| Layer | Status | Notes |
|-------|--------|-------|
| Claim alignment | intact | Post-clip constant = no behavioral contrast; claim never fairly tested |
| Biological reference | clear | Seymour 2019 + Horing 2022 + Song 2021; two targeted reviews present; biology unambiguous |
| Prerequisites | present | SD-020, E2_harm_a (C1 PASS 2/3), SD-032b, SP-CEM all active |
| Implementation completeness | partial | Wiring correct; weight config (suppression=4.0) dominates pre-clip bias ~5x more than PE term (dacc_weight=0.5) |
| Environment adequacy | unknown | CausalGridWorldV3 may be too sparse for precision-weighting to separate from raw magnitude; not the primary issue here |
| Measurement adequacy | inadequate | C2 measures corr(total_pre_clip_bias, model_pe); suppression term (~80% of total) is independent of PE vs raw condition; dilutes PE signal below detectability |
| Integration adequacy | absent | post_clip constant at 2.0 => E3 never receives a varying dACC signal; behavioral integration impossible during P2 eval |
| Scale / capacity | adequate | E2_harm_a R2=0.91-0.94 in working seeds; sufficient capacity |

### Dominant diagnosis

measurement_gap: C2 conflates the PE-signal component of the bias with the much larger
suppression-term component. The metric cannot distinguish PE from raw under these conditions
regardless of which representation is "correct." Compounded by: the post-clip constant means
E3 sees no variation to discriminate at the behavioral level (integration gap during eval).

### Recommended epistemic_category

measurement_gap

---

## 6. Learning Extracted

1. Suppression-term weight (4.0) must be separated from PE-term weight (0.5) in C2 telemetry.
   Record pe_component and raw_component as separate fields before summing with interaction/
   foraging/suppression. Run C2 on the component, not the total.

2. dacc_bias_max_abs=2.0 is incompatible with dacc_suppression_weight=4.0 at any typical
   action-count. Pre-clip values of ~10-12 are 5-6x above the clip. Clip must be raised to
   at least 15-20 OR suppression weight reduced so PE term is the dominant contributor.

3. Post-clip constant = E3 learns nothing from dACC variation across seeds or conditions.
   Future iterations must confirm bias_clip_saturation_frac < 0.1 as a pre-condition for
   interpreting C2.

4. Per-seed C1 gate before C2: if C1 R2 < 0.3 for a seed, the forward model did not train --
   C2 for that seed is pure noise. Exclude it from the C2 win-count denominator.

5. 597 (post-clip telemetry -> undefined Pearson) + 597b (pre-clip telemetry -> suppression-
   dominated) illustrate that measurement design for dACC PE vs raw tests requires direct
   access to the PE-term contribution, not indirect access via total bias.

---

## 7. Repair Pathway

**Routing:** /queue-experiment -> V3-EXQ-597c

### 597c redesign spec

Fix 1 (required): raise dacc_bias_max_abs to 20.0. Ensures post-clip output varies, so E3
receives a discriminative signal. Confirms bias_clip_saturation_frac < 0.1 in P2.

Fix 2 (required): per-component telemetry. Record separately:
- pe_component = dacc_weight * mode_ev (PE_FORWARD arm) or raw equivalent (RAW_NORM arm)
  BEFORE interaction/foraging/suppression terms are added
- C2 criterion: corr(pe_component, model_pe) > corr(raw_component, model_pe) + 0.05 in
  >=2/3 seeds WITH C1 R2 > 0.3 (exclude degenerate seeds)

Guard: assert bias_clip_saturation_frac < 0.1 per seed before scoring C2; flag inconclusive
for any saturating seed rather than scoring as a FAIL.

### Evidence_quality_note for governance to write

EXQ-597b pre-clip telemetry fix resolved 597's undefined-Pearson problem but revealed a
deeper confound: dacc_suppression_weight=4.0 drives pre-clip bias ~10-12 (5-6x above
dacc_bias_max_abs=2.0), making post-clip output a constant 2.0 in all seeds and conditions.
C2 measures corr(total_pre_clip_bias, model_pe), but the suppression term (~80% of total) is
independent of both PE and raw norm, diluting any discrimination signal below detectability.
The sole C2 win (seed13) is a degenerate-regime artifact (C1 R2=-1.624, 170 samples, action-
skewed). Diagnosis: measurement_gap -- C2 cannot distinguish PE from raw when suppression
dominates. MECH-258 not weakened; claim was not fairly tested (post-clip constant eliminated
behavioral contrast). Recommend: EXQ-597c with per-component telemetry isolating PE
contribution and dacc_bias_max_abs raised to 20.0.

---

## 8. Routing Decision (confirmed by user)

- Epistemic category: measurement_gap
- Evidence direction recommendation: retain "mixed" at manifest level; annotate with
  evidence_quality_note above
- MECH-258 alignment: intact (not weakened)
- Routing: /queue-experiment -> V3-EXQ-597c
- pending_retest_after_substrate: false (not a substrate gap; fix is metric redesign)
- narrow_supports_flag: false
