# Failure Autopsy — V3-EXQ-768a (ARC-057 DA-density × curiosity interaction, margin re-op)

**Generated:** 2026-07-17T07:05:54Z
**Scope:** single (flagged-PASS adjudication)
**Status:** confirmed
**Verdict:** REAL / verified PASS — `supports`. Route: **governance promotion, ARC-057 candidate → provisional (approach-side scoped).**

---

## 1. Scope

`V3-EXQ-768a` (`v3_exq_768a_arc057_da_curiosity_interaction_spike_margin_20260717T064620Z_v3`) is the re-operationalized replacement for the confirmed **768 vacuous_pass cluster** (`supersedes: v3_exq_768_arc057_da_curiosity_interaction_spike`; adjudicated in `failure_autopsy_767-768-cluster_2026-07-16`). It is a **diagnostic** (`experiment_purpose=diagnostic`, `claim_ids=[ARC-057]`) and the load-bearing interaction test for ARC-057. Ran cloud-class on **ree-cloud-4 (linux-x86_64-py3.10)**, 8 seeds, 28.8 s. This is a flagged-PASS adjudication (a diagnostic superseding a confirmed-vacuous run must be confirmed non-vacuous before it clears a gate), not a FAIL autopsy.

Operational note: 768a sat pending/unclaimed for ~10 h because it was affinity-pinned to `ree-cloud-4`, which was offline 2026-07-15 → 2026-07-17; the user woke ree-cloud-4, and it ran at 06:46Z.

## 2. Facts (no interpretation)

2×2 ablation (SD-024 DA-expansion × SD-025 curiosity), continuous CEM score-margin, 8 seeds, counterbalanced:

| arm | median margin |
|---|---|
| both off | 0.000 |
| SD-024 alone (DA-expansion ON, curiosity OFF) | 0.000 |
| SD-025 alone (curiosity ON, flat / non-DA map) | −0.009 ≈ 0 |
| **both on** | **14.53** (per-seed range 9.02 – 16.98) |
| interaction margin | 14.52 |
| weight-zeroed both-on | 14.53 (identical → rides density, not value) |

Load-bearing criteria (all pass): C1_interaction_margin_contrast 14.37 ≥ 1.0 · C2_both_on_margin 14.40 ≥ 1.0 · C3_sd025_alone_no_gradient 0.0011 ≤ 0.35 · C4_interaction_rides_density_not_value (weight-zeroed both-on ≡ both-on). Supporting: C5 SD-024-alone-no-margin 0.0 · C6 baseline-near-zero 0.0 · C7 value_non_discriminating 0.092 ≤ 0.2.
Readiness preconditions **both met**: density_read_discriminates 13.09 ≥ 0.5; selection_margin_responds_to_curiosity 17.86 ≥ 1.0.
`non_degenerate=True` — all 4 variance guards TRUE (density_dense_exceeds_sparse, interaction_margin_varies_across_seeds, both_on_margin_varies_across_seeds, da_creates_density_gradient).
Recording: `recording_schema=rec/v1`, `substrate_hash=be9a4d7f…`, full `config`, `seeds=[0..7]` present — reproducible.

**The degeneracy is resolved.** 768 was vacuous because the binary argmin gate `C2_both_on_approaches` pinned at exactly 1.0 with zero cross-seed variance. 768a replaces it with the continuous score-margin: both-on = 14.53 and **varies 9.0–17.0** (`both_on_margin_varies_across_seeds` TRUE). The self-route (`arc057_approach_margin_emerges_from_da_curiosity_interaction_not_either_alone`, supports) is therefore trustworthy.

## 3. Claim-layer mapping

**ARC-057** (architectural_commitment, `hippocampus.curiosity_approach_emergence`, candidate/v3_pending). depends_on: MECH-232 (now **provisional**), ARC-007, SD-004 (implemented). The experiment let the claim express itself: the 2×2 with equal-mass value isolation and the C4 weight-zeroing discriminator isolate the **interaction** (both-on high; both singles ≈ 0) and confirm it rides **density not value** — the "no explicit approach gradient" core of ARC-057. C3 confirms the SD-025-alone (flat-map) leg produces no gradient. `claim_ids` tag is accurate (single-claim diagnostic authored for exactly this claim).

## 4. Biological-reference triage

ARC-057 is a **biological translation**, not a formal import: DA-mediated representational expansion (Retailleau & Morris; Krishnan 2022) + an information-seeking/curiosity drive following map structure. Closest references: hippocampal predictive-map / reward-driven field reshaping (Stachenfeld 2017), incentive-salience "wanting" as emergent DA approach (Berridge), and intrinsic-motivation → directed approach (Pathak ICM 2017; Bellemare pseudo-counts 2016). **Lit status: PRESENT** — `evidence/literature/targeted_review_arc_057` (3 entries, lit_conf 0.745, added 2026-07-17). **No `/lit-pull` owed.** The biology supports the mechanism class and the experiment confirms the REE translation — no divergence to register.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **strengthened** | interaction expressed and passed; rides density not value (C4) |
| Biological reference | **clear** | DA-expansion × curiosity; lit present (targeted_review_arc_057) |
| Prerequisites | **present** | MECH-232 provisional; SD-024 + SD-025 IMPLEMENTED |
| Implementation | **complete** | 2×2 ablation, continuous margin, weight-zeroing discriminator |
| Environment | **adequate** | SD-024 internal-density workaround makes the grid-world test valid (no ecological env needed for the *interaction* claim) |
| Measurement | **adequate (resolved)** | continuous score-margin; the re-op fixed the 768 degeneracy — dominant resolved layer |
| Integration | **coupled + stable** | the interaction IS the result: both modules coupled produce approach neither yields alone |
| Scale | **adequate** | 8 seeds, variance-bearing, positive control met |

**Recommended `epistemic_category`:** `verified` (diagnostic PASS; degeneracy resolved). Not a ceiling, not degenerate.

## 6. Learning extracted

1. **ARC-057's super-additive approach-emergence is real and non-degenerate:** approach appears only from the DA-expansion × curiosity interaction; SD-024-alone (0.0) and SD-025-alone-on-flat-map (−0.01) produce none. The re-op margin resolves the 768 saturation.
2. **It rides density, not value** (C4 weight-zeroing invariant; C7 value non-discriminating) — the "no explicit approach gradient in hippocampal terrain" core holds under test.
3. **Scope boundary (load-bearing for the note):** the SD-025-alone = 0 result shows the curiosity drive produces *no* directed behaviour without prior DA-shaping. Combined with 767a's force decomposition (density-attraction 39.3 vs familiarity-discount ceiling 20.4, 0 at the decision point), the drive is a **reward-conditional exploitation amplifier**. This confirms the *approach* side (ARC-057) and is orthogonal to strategy **diversity generation** (conversion/competence/monostrategy ceiling) — see the reframe writeup. The promotion must not be read as evidence the drive addresses diversity.
4. The ecological richer-env test (ARC-057 Test C) remains **V4-deferred** (`arc_057_ecological_env_decision_2026-07-16`); 768a is the env-free interaction spike, which is the buildable node it targets.

## 7. Repair pathway / routing

`complex (probe-gated) / puzzle (known rules)` — the well-posed interaction question had a missing fact; the spike supplied it. Node **resolved**. Routing: **`governance`** — apply ARC-057 candidate → provisional (approach-side scoped). No substrate entry, no re-queue, no lit-pull. Re-derive brake: **not fired** (0 prior substrate_ceiling/non_contributory autopsies for ARC-057). Granularity trigger: **not fired** — the prior 767-768-cluster autopsy was the *measurement_degeneracy* diagnosis; this is its resolution, not a recurring divergent-signature failure.

### Draft `evidence_quality_note` (governance to write on ARC-057)

> 2026-07-17: candidate -> provisional. SD-024 x SD-025 interaction diagnostic V3-EXQ-768a (cloud, ree-cloud-4, linux-x86_64-py3.10) PASS/supports, adjudication=verified (evidence/planning/failure_autopsy_V3-EXQ-768a_2026-07-17.json). Re-operationalized replacement for the confirmed 768 vacuous_pass cluster: the binary argmin gate that saturated at exactly 1.0 (zero cross-seed variance) is replaced by the continuous CEM score-margin. Approach emerges ONLY from the DA-expansion x curiosity interaction -- both-on margin 14.53 (varies 9.0-17.0 across 8 seeds), while SD-024-alone (0.0) and SD-025-alone-on-a-flat-map (-0.01) produce no approach margin -- the super-additive interaction ARC-057 asserts. All 4 load-bearing criteria pass (C1 interaction contrast 14.37>=1.0; C2 both-on 14.40>=1.0; C3 sd025-alone-no-gradient 0.0011<=0.35; C4 interaction rides density not value: weight-zeroed both-on identical to both-on), C7 value non-discriminating (0.092), readiness met (density discrim 13.09; positive control 17.86), non_degenerate (all 4 variance guards TRUE). Cloud PASS satisfies the cloud-authoritative gate. Diagnostic (experiment_purpose excluded from confidence scoring) -- the promotion is the gate-clearing action, not a confidence increment. SCOPE: validates the interaction / approach-emergence claim ONLY. It does NOT bear on the ecological richer-env test (V4-deferred, arc_057_ecological_env_decision_2026-07-16), and it does NOT establish strategy-diversity generation: 767a+768a together show the curiosity drive is a reward-conditional exploitation amplifier (approach-side confirmed; diversity-generation is a separate open node -- see the curiosity=exploitation-amplifier reframe on behavioral_diversity_isolation / conversion_ceiling_campaign).

## 8. Routing decision (user-confirmed)

User selected **"Promote, approach-side scoped"** at the Step-8 gate (2026-07-17). Governance applies ARC-057 candidate → provisional with the scoped note above.
