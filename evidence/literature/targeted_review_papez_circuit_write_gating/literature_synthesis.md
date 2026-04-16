# Literature Synthesis: Papez Circuit Write Gating

**Date:** 2026-04-16
**Purpose:** Targeted literature pull to ground the anatomical substrate for action-mode-specific
write profiles to the hippocampal system. The Papez circuit (hippocampus -> fornix -> mammillary
bodies -> anterior thalamus -> cingulate -> entorhinal cortex -> hippocampus, plus multiple
reciprocal connections) is proposed as the circuit through which the hypothesis_tag signal is
delivered to hippocampal phi(z) write operations (MECH-094), and through which trajectory
proposals navigating residue-field terrain are enabled (ARC-007).

**Claims under investigation:** MECH-094, ARC-007.

---

## Summary of Evidence

### ARC-007: Hippocampal Map Navigation

**Bubb et al. 2017** (DOI: 10.1177/2398212817723443) establishes the full anatomy of the
hippocampal-diencephalic-cingulate network as a multiply-connected reciprocal system, not a
simple serial loop. The anterior thalamic nuclei are a convergence node receiving both direct
hippocampal input and mammillary body input, and projecting back to hippocampus via cingulate
and retrosplenial cortex. This architecture supports the claim that hippocampal terrain navigation
requires the full circuit, not hippocampus alone.

**Aggleton et al. 2010** (PMID: 20550571) provides disconnection evidence: severing
hippocampal-anterior thalamic connectivity impairs spatial memory even with intact hippocampus
and intact anterior thalamus. This establishes that the anterior thalamic relay is necessary
(not merely associated) for the kind of memory that terrain navigation requires.

### MECH-094: Hypothesis Tag as Write Gate

**Schnider 2003** (PMID: 12894241) provides the most direct neurobiological account:
confabulation is a failure of orbitofrontal reality filtering, producing write of contextually
inappropriate memory traces to the agent's behavioral state. The OFC reality filter normally
flags whether activated content pertains to ongoing reality -- exactly the function assigned to
the hypothesis_tag in MECH-094. Confabulation (tag loss -> simulated content written as real)
is mechanistically equivalent to OFC reality-filter failure.

The cingulate-to-hippocampus pathway identified in Bubb et al. provides the anatomical substrate
for top-down tag delivery from OFC/cingulate circuits to hippocampal encoding machinery.

---

## Gaps

- Action-mode specificity (habitual vs deliberate vs simulated vs sleep) not directly tested
  in any of the three papers; this functional specificity must be inferred from circuit position.
- The REM sleep write-profile (hypothesis_tag active but may fail) is addressed separately
  in targeted_review_connectome_mech_094 (Hobson & Pace-Schott 2002 entry).
- Fornix lesion data confirming write-gate loss are covered in existing ARC-007 entries.
