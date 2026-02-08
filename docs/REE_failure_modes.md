# REE failure modes (implementation-focused)

**Claim Type:** implementation_note  
**Scope:** Failure mode taxonomy for REE implementations  
**Depends On:** INV-006, INV-008, ARC-005, ARC-013, ARC-010  
**Status:** stable  
**Claim ID:** IMPL-005
<a id="impl-005"></a>

This document lists REE-relevant failure modes as **computational pathologies**. It is not a clinical guide.

## 1. Moral amnesia (residue disabled)

**Mechanism:** \(R\) is not stored or not coupled into selection.

**Expected behavior:** repeated harmful choices with no enduring aversive curvature; ethics collapses into short-horizon optimization.

**Implementation smell:** residue map \(\phi(z)\) remains near-zero; changing \(\rho\) has no effect on behavior.

## 2. Residue overload (trajectory paralysis)

**Mechanism:** \(R\) grows without a repair pathway; \(\Phi_R\) dominates selection.

**Expected behavior:** avoidance of all actions, excessive conservatism, or oscillation between inaction and impulsive escape.

**Mitigations:** introduce controlled offline reprojection (sleep-like replay) that reduces spurious dents while preserving true residue.

## 3. Precision misrouting (depth mismatch)

**Mechanism:** \(\alpha_k\) is high at the wrong depth.

**Examples:**
- High \(\alpha_\gamma\): agent becomes stimulus-captured and brittle.
- High \(\alpha_\delta\): regime becomes too sticky; depression-like inertia.
- High \(\alpha_\theta\): context over-precision; delusion-like narrative lock.

## 4. Other-model collapse (ethical blindness)

**Mechanism:** the system cannot sustain a homologous model of others, or coupling \(\kappa\) is forced near zero.

**Expected behavior:** instrumental treatment of other agents; reduced sensitivity to predicted other degradation.

## 5. Reward hijack (policy corruption)

**Mechanism:** reward terms dominate selection; ethical consequence signals (legacy \(M\) proxy or residue penalties) become a small regularizer.

**Expected behavior:** superficially competent behavior with systematic exploitation of other agents or environment loopholes.

## 6. Spurious residue (false dents)

**Mechanism:** residue updates on irrelevant error signals or noisy attributions.

**Expected behavior:** superstition-like avoidance; fear of harmless states.

**Mitigations:** calibration of attribution, uncertainty-aware residue update, replay with counterfactual checking.

## 7. Control-plane regime mis-tuning (cross-link)

These failure modes are also described as mis-tuned control regimes in `docs/architecture/modes_of_cognition.md` (MECH-027), including hypervigilance, dissociation, rumination, mania, and psychosis-like states.

This document does not reclassify them clinically; it links them as implementation-relevant pathologies driven by control-plane parameterization.

See: `docs/architecture/modes_of_cognition.md#mech-027`

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- IMPL-005
- INV-006
- INV-008
- ARC-005
- ARC-013
- ARC-010
- ARC-016
- MECH-027

## References / Source Fragments

- `docs/processed/legacy_tree/docs/REE_failure_modes.md`
- `docs/thoughts/2026-02-08_modes_of_cognition_control_plane_regimes.md`
