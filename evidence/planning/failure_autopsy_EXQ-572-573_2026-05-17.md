# Failure Autopsy -- Cluster A: EXQ-572 + EXQ-573 (ARC-065 / Intervention A + Diversity Bias)

**Date:** 2026-05-17T14:20:35Z
**Scope:** cluster (2 experiments)
**Status:** confirmed

---

## Targets

| Experiment | Run ID | Claims | Outcome | Reclassified |
|---|---|---|---|---|
| v3_exq_572_intervention_a_dual_attractor | v3_exq_572_intervention_a_dual_attractor_20260516T095117Z_v3 | ARC-065 | FAIL | non_contributory (already applied) |
| v3_exq_573_arc065_bias_scale_sweep | v3_exq_573_arc065_bias_scale_sweep_20260516T083605Z_v3 | ARC-065, MECH-313, MECH-314, MECH-320 | FAIL | non_contributory (already applied) |

---

## Facts Reconstruction

### EXQ-572 (Intervention A dual-attractor, 4 seeds)

Acceptance criteria (ARM_3 must pass >= 2/3 seeds):
- C1: TV of action distributions between hazard and resource contexts > 0.20
- C2: z_harm_a_norm-conditioned reef_presence_rate delta > 0.15
- C3: goal_active-conditioned resource_presence_rate delta > 0.15
- PASS = C1 AND (C2 OR C3)

Observed:

| Arm | mean_c1_tv | mean_c2_delta | mean_c3_delta | c1_pass_seeds |
|---|---|---|---|---|
| ARM_0_baseline | ~1e-14 | -0.001 | 0.0 | 0 |
| ARM_1_harm_affect | ~1e-14 | -0.001 | 0.0 | 0 |
| ARM_2_goal | ~1e-14 | -0.0002 | 0.0 | 0 |
| ARM_3_all | ~1e-14 | +0.001 | 0.0 | 0 |

C1_TV is machine-epsilon across all arms and seeds. n_c2_records=6000, n_c3_records=6000 (data collection was successful in final run; earlier 3 runs had n=0, correctly reclassified). The zero is real, not a collection artifact.

The manifest carries `outcome_note`: "ARM_3 (full Intervention A) passed overall on only 0/3 seeds. Reclassified non_contributory 2026-05-16: n_c2_records=0, n_c3_records=0 for all arms/seeds in earlier runs -- systematic data collection failure. Original verdict: weakens." The 095117Z run (final) has non-zero records but still zero TV and deltas.

**Failed criterion:** discrimination (all three criteria fail; no arm shows any behavioral differentiation).

### EXQ-573 (ARC-065 bias scale sweep 1x/5x/10x)

Acceptance: P1 = any diversity arm entropy > ARM_0 + 0.05.

| Arm | entropy |
|---|---|
| ARM_0 baseline | 0.515109 |
| ARM_1..ARM_9 (all) | 0.515109 (identical) |

All 10 arms -- including combined 10x -- produce identical entropy to machine precision. P3 (combined_10x >= combined_5x) passes trivially because both are identical.

`evidence_direction_note` (in manifest, already applied by governance): "Reclassified non_contributory 2026-05-16 governance review. All 10 arms produced identical entropy (delta=0 at 1x/5x/10x scale) because the bias channel is not propagating to E3 selection -- bias components are machine-epsilon regardless of scale factor. EXQ-571 confirmed: bias_fraction=0 for all components."

**Failed criterion:** discrimination (P1); absolute zero, not marginal.

---

## Claim Layer

| Claim | Type | Status | v3_pending | supports/weakens (claims.yaml) | Can it express itself? |
|---|---|---|---|---|---|
| ARC-065 | ARC | candidate | True | 0 / 0 | No -- monostrategy ceiling |
| MECH-313 | MECH | candidate_substrate_landed | True | 0 / 0 | No -- bias not propagating |
| MECH-314 | MECH | candidate_substrate_landed | True | 0 / 0 | No -- bias not propagating |
| MECH-320 | MECH | candidate_substrate_landed | True | 0 / 0 | No -- bias not propagating |

**Claim alignment: intact.** The experiments could not test the claims -- the substrate collapses to monostrategy before the diversity/intervention signals have any behavioral surface to act on.

---

## Biological Reference Triage

**ARC-065 (behavioral diversity generation, LC-NE + frontopolar + striatal novelty):**

Closest mammalian mechanism: LC-NE tonic firing modulates the entire cortical gain globally -- it shifts the exploration/exploitation temperature of downstream processing, not adds a local score offset. Frontopolar BA10 drives directed exploration by tracking uncertainty in regions not recently sampled (Daw 2006, Wittmann 2008). Striatal tonic dopamine (mesolimbic vigor) sets the baseline action vigor threshold (Niv 2007).

**Architecture concern (not falsification):** The REE implementation of MECH-313/314/320 adds score biases (scalar offsets to E3 candidate scores). This is a formal-definition import (additive utility), not the biological mechanism (global gain modulation, uncertainty-driven directed exploration, tonic vigor coupling). Until the monostrategy is resolved, this distinction cannot be tested. Even if the architecture were wrong, EXQ-573 cannot tell -- the signals never arrive at E3 selection.

**Lit status:** partial (targeted_review_arc065_behavioral_diversity/Pull 1, Pull 4 in evidence_quality_notes). No direct falsification of the formal-import concern from current lit.

**Does the failure resemble a missing-dependency signature?** Yes -- MECH-269/V_s monostrategy resolution is the explicit prerequisite. EXQ-572/573 join EXQ-550/553/569/582 as converging evidence that the monostrategy is the load-bearing gap.

---

## Four-Layer Diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | Cannot test under monostrategy; not falsification |
| Biological reference | partial | LC-NE/frontopolar/striatal mechanism known; bias-addition architecture may be wrong abstraction but untestable until monostrategy resolved |
| Prerequisites | missing | MECH-269/V_s monostrategy resolution required |
| Implementation | partial | Substrate landed; bias signal not propagating to selection |
| Environment | too sparse | CausalGridWorldV2 monostrategy ceiling confirmed (TV~=1e-14) |
| Measurement | adequate for 573; misleading for 572 | 572 earlier runs had data collection failure; final run has records but outcome trivially zero |
| Integration | uncoupled | Bias signals not reaching E3 score function |
| Scale | unknown | Cannot evaluate until propagation fixed |

**Recommended `epistemic_category`:** `substrate_ceiling`

---

## Cluster Pattern

| Experiment | Claim | Absolute/negative-control | Discrimination | Read |
|---|---|---|---|---|
| EXQ-572 | ARC-065 | n/a (no negative control arm) | C1_TV~=1e-14 (vs 0.20); C3_delta=0.0 | substrate_ceiling |
| EXQ-573 | ARC-065, MECH-313/314/320 | ARM_0=0.515 (implicit control) | ALL arms = 0.515 identical | substrate_ceiling |
| EXQ-569 | diversity track | SP-CEM control | identical entropy all 6 arms | substrate_ceiling |
| EXQ-550 | MECH-269/V_s | monostrategy falsifier | monostrategy confirmed | substrate_ceiling |
| EXQ-582 | SD-012/goal | n_contacts_post_warmup=0 | zero contact density | substrate_ceiling |

**Structural property:** The substrate collapses to monostrategy before any diversity/intervention signal can produce behavioral differentiation. This is one structural property, not N independent bugs.

---

## Learning Extracted

1. **Monostrategy ceiling is the gating prerequisite for the entire diversity track.** EXQ-572/573 add two more experiments to this convergent signal.
2. **Bias-addition architecture may be formally wrong.** LC-NE/frontopolar/striatal mechanisms modulate global gain/temperature, not local score offsets. This is a biology-divergence flag: commission a targeted lit-pull when diversity track resumes post-MECH-269.
3. **Scale invariance is diagnostic.** EXQ-573's 10x result confirms the bias channel is structurally disconnected, not just under-powered.

---

## Repair Pathway

| Diagnosis | Routing |
|---|---|
| Monostrategy ceiling blocks all discrimination | pending_retest_after_substrate: gate on MECH-269/V_s monostrategy landing |
| Bias-addition architecture may diverge from biology | lit-pull commission (targeted_review_diversity_bias_architecture) when monostrategy track concludes |

**Draft `evidence_quality_note` (governance should write for ARC-065, MECH-313/314/320):**
"Non-contributory: monostrategy ceiling prevents discrimination. EXQ-572 (C1_TV~=1e-14, C2/C3_delta~=0 across all 4 arms) and EXQ-573 (bias_fraction=0 at 1x/5x/10x scale -- all 10 arms identical entropy) both confirm the diversity/intervention signals don't reach E3 selection under CausalGridWorldV2 monostrategy. Both reclassified non_contributory 2026-05-16 (pre-existing governance note). pending_retest_after_substrate: MECH-269/V_s monostrategy. Not claim pressure; the substrate has landed but the ceiling makes the test uninformative. Biology-divergence flag: bias-addition architecture may not match LC-NE/frontopolar/striatal gain-modulation mechanism -- commission lit-pull when diversity track resumes."

---

## Confirmed Routing

- **ARC-065, MECH-313, MECH-314, MECH-320:** `pending_retest_after_substrate` (MECH-269/V_s gate). Non_contributory confirmed. No governance demotion.
- **Lit-pull flag:** when monostrategy track concludes, commission targeted_review for diversity bias architecture (bias-addition vs global gain modulation).
