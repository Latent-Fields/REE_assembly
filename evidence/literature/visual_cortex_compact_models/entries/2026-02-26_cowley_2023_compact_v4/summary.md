# Literature Summary: Cowley et al. 2023 — Compact deep neural network models of visual cortex

**Source:** Cowley BR, Stan PL, Pillow JW, Smith MA. bioRxiv 2023.11.22.568315
**DOI:** 10.1101/2023.11.22.568315
**Evidence direction:** supports
**Confidence:** 0.72
**Primary claims supported:** ARC-001, ARC-003, ARC-005, INV-014, MECH-068

---

## What the paper did

Trained large data-driven ensemble DNNs to predict macaque V4 neural responses (~78k unique images,
3 animals, 96-electrode arrays). Compressed these ensembles ~5000× using knowledge distillation
and pruning while preserving predictive accuracy. Analysed the compressed models to identify
recurring circuit motifs. Validated predicted preferred stimuli causally using adversarial
image synthesis.

## Key empirical findings

1. **Shared early filter bank**: Compact models across many neurons share similar early-stage
   filters. Representational diversity does not arise from separate early circuits per neuron.

2. **Consolidation step determines selectivity**: Stimulus preference is determined entirely by
   a neuron-specific consolidation step — selective pooling, nonlinear weighting, and
   competition/normalisation over the shared basis. This is the critical motif.

3. **5000× compression with no accuracy loss**: The accurate data-driven ensembles can be
   radically compressed. The computational core is compact; high-dimensional representations
   carry large functional redundancy.

4. **Canonical operations identified**: The circuit-level operations are: edge/curve detectors,
   surround suppression, winner-take-all competition, divisive normalisation. These are
   well-established canonical cortical computations (cf. Carandini & Heeger 2012).

5. **Causal validation**: Adversarial image synthesis confirmed that models correctly predict
   neuronal preferred stimuli — not just correlational fits.

## REE mapping

### ARC-001 (E1 Persistent Substrate)
E1 should be understood as a **shared canonical basis + structured transforms**, not a
monolithic free parameterisation. Diversity in downstream behaviour arises from how
consolidation operators (E3/gating) pool from the E1 basis, not from E1 encoding unique
representations per entity. See MECH-068 (Consolidation Selectivity Hypothesis).

### ARC-003 (E3 Trajectory Selection)
E3's tri-loop commit gating (MECH-062) instantiates the consolidation step in REE terms:
selective pooling + competition + normalisation over the shared E1 basis. Selectivity of
trajectory preference lives at E3, not in E1 representations. This provides a discriminating
experimental prediction: E3 weight variation should change trajectory preference while E1
latent structure remains stable (see MECH-068, CSH-1).

### ARC-005 (Control Plane)
Surround suppression, divisive normalisation, and winner-take-all are empirically confirmed as
canonical cortical computational motifs. REE mappings:
- Surround suppression → precision modulation (MECH-040, MECH-054)
- Divisive normalisation → gain control (MECH-063, ARC-005)
- Winner-take-all → commit threshold (MECH-062)

### INV-014 (Separation of representation and regulation)
The shared-basis / consolidation-step decomposition is direct empirical evidence for the
architectural separation of representation (E1 basis) from regulation/gating (E3 consolidation).

## JEPA scope note

JEPA corresponds to stage 1 of this paper's framework: the shared feature basis / early filter
bank. Stage 2 — the consolidation step that determines behavioural selectivity — is not in
JEPA's architecture. This empirically confirms that JEPA should be treated as a reference
architecture for E1 representation only, not as a complete REE substrate.

## Caveats

- Paper studies V4 (mid-level visual cortex). Extension to full cognitive architecture is
  inferential.
- Canonical operations (WTA, divisive normalisation, surround suppression) are well-established
  and have lower transfer risk than the broader consolidation principle applied to cognition.
- "Consolidation" here refers to a circuit-level computational motif, not memory consolidation.

## Provenance

Paper accessed via bioRxiv (open access preprint). Local copy stored at:
`~/Desktop/REE_Master/nihpp-2023.11.22.568315v1.pdf`
Licence: bioRxiv standard preprint terms (CC-BY-NC-ND 4.0 for preprint).
