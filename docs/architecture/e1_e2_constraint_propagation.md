# E1/E2 Constraint Propagation and Perceptual Bias

**Source thought:** Theoretical development session 2026-03-15 (NC-02 through NC-03)
**Registered:** 2026-03-15

---

<a id="mech-081"></a>
## E2 Sufficiency Constraint Reduces E1 Effective Dimensionality (MECH-081)

**Claim Type:** mechanism_hypothesis
**Scope:** Top-down dimensional constraint from E2 on E1 feature-discovery target
**Depends On:** ARC-001, ARC-002, MECH-033
**Status:** candidate
**Claim ID:** MECH-081
**Extends:** ARC-001 (E1 as persistent predictive substrate), ARC-002 (E2 as fast forward predictor), MECH-033 (E2 kernels seed hippocampal rollouts)

E1 operates by comparing sensed data against predicted sensory data, with prediction error serving a dual function: (a) updating the generative model, and (b) directing attentional sampling toward high-error regions. This is established by ARC-001 and INV-009.

**New claim:** E2's prediction task — anticipating the effect on E2-level objects (latent-object transitions, `f(z_γ,a_t) → z_γ_{t+1}`) — generates a top-down *sufficiency constraint* on what E1 needs to resolve. Specifically:

- For E2's predictions to be well-formed, E1 must track a specific subset of covariances in the sensory stream: those covariances that are discriminative for E2's transition predictions.
- This implicitly specifies which features E1 must discover, *before* E1 has discovered them through unsupervised error minimisation alone.
- The hard problem of feature discovery is therefore *partially specified from above* (by E2's objective) rather than requiring purely bottom-up unsupervised discovery.

**Architectural consequence:** the sufficiency constraint reduces the effective dimensionality of E1's target representation — E1 need not represent all possible covariances, only those necessary for E2's task. This may reduce the hidden-layer depth or parameter count required for E1 to converge on useful representations, because the search space is narrowed by the downstream task.

**Relationship to MECH-033:** MECH-033 describes E2 forward-prediction kernels seeding hippocampal rollouts. MECH-081 is an upstream complement: E2's requirement for well-formed kernels constrains what E1 must produce, making E2 an active shaper of E1 representations (not merely a consumer of them).

**Relationship to ARC-001 (MECH-068, Consolidation Selectivity):** MECH-068 specifies that representational diversity lives in the consolidation operator (E3 gating), not in the E1 basis. MECH-081 is compatible: the dimensionality constraint from E2 shapes the E1 basis, while E3 gating then selects from it. The two claims address different levels of specification.

**Testable implication:** in a REE model trained with E2 present, E1 representations should be lower-dimensional (sparser or more clustered) than in a model trained with E1 alone (no E2 top-down signal). The specific dimensions captured should be predictive of E2 transition accuracy.

---

<a id="mech-082"></a>
## Top-Down Perceptual Bias via E2 Model Distortion (MECH-082)

**Claim Type:** mechanism_hypothesis
**Scope:** Propagation of E2/hippocampal-map distortion into E1 attentional sampling without explicit E1 retraining
**Depends On:** MECH-081, MECH-076, MECH-027, ARC-001, ARC-002
**Status:** candidate
**Claim ID:** MECH-082
**Extends:** MECH-076 (residue as hippocampal map structural deformation), MECH-081 (E2 sufficiency constraint)

Because E2's predictions constrain what E1 attends to (MECH-081), changes in E2's predictive model propagate *downward* as changes in E1 perceptual sampling — without requiring explicit retraining of E1's weights.

**Mechanism:**
1. Hippocampal map distortion (MECH-076: deep attractor basins, over-represented regions from high-arousal experience) biases the trajectory bundles generated during rollout.
2. These distorted rollouts shape E2's short-horizon predictions — E2's anticipation of near-future states is skewed toward outcomes consistent with the dominant map attractors.
3. Via the E2 → E1 sufficiency constraint (MECH-081), E1's attentional sampling is directed toward sensory dimensions that are discriminative for those E2 predictions.
4. Result: E1 over-samples sensory dimensions that are consistent with map-level residue and under-samples dimensions that are not — without any change to E1's weights.

**This is a computational account of perceptual bias in:**
- **Trauma / PTSD:** deeply encoded threat-consistent map regions (MECH-076) create E2 predictions skewed toward threat; E1 samples selectively for threat-consistent sensory cues (hypervigilance).
- **Paranoia:** aversive map attractors around social-threat themes drive E2 to predict threat-consistent transitions; E1 attends to confirming social cues.
- **Depression:** attractor over-representation of loss/failure-consistent states biases E2 predictions downward; E1 selectively samples negative-valence sensory dimensions.

**Relationship to MECH-056 (trajectory-first residue placement):** MECH-082 is consistent with MECH-056's prescription that residue should constrain trajectories before distorting core representations — the mechanism here operates via map geometry (trajectory level) propagating upward through E2 to influence E1 *sampling* (attentional weighting), not by directly rewriting E1's representational content.

**Clinical implication:** interventions targeting map geometry (MECH-077: EMDR, psychedelic-assisted therapy) should produce downstream changes in E1 perceptual sampling without requiring direct cognitive retraining. This predicts that map-level treatments should reduce perceptual bias even in the absence of deliberate attentional retraining — a testable distinction from CBT-style approaches (which operate on OFC/vmPFC evaluation of the existing map, per MECH-077).

---

## Open Questions

None currently registered. MECH-082 is consistent with existing REE constraints but has not been experimentally probed.

---

## Related Claims (IDs)

- MECH-081
- MECH-082
- ARC-001
- ARC-002
- MECH-033
- MECH-076
- MECH-077
- MECH-027
- MECH-056
- MECH-068

## References / Source Fragments

- Theoretical development session 2026-03-15 (NC-02 through NC-03)
