# SD-019: Affective Harm Non-Redundancy Constraint

**Claim ID:** SD-019  
**Subject:** harm_stream.affective_nonredundancy  
**Status:** IMPLEMENTED 2026-04-10  
**Registered:** 2026-04-08  
**Depends on:** SD-011, SD-010, ARC-016  
**Blocks:** SD-020 (requires non-redundant z_harm_a before PE-weighting makes sense)

---

## Problem

SD-011 established the dual-stream split (z_harm_s sensory-discriminative, z_harm_a
affective-motivational) in principle. EXQ-241/241a showed that z_harm_a remained too
close to z_harm_s functionally (D3 reversal: z_harm_a predicted the sensory target better
than z_harm_s because both received the same spatial signal).

The SD-011 harm-history input (second source) reduces the correlation structurally, but
does not actively push the streams apart. Without an explicit non-redundancy constraint,
nothing prevents z_harm_a from collapsing to a delayed/smoothed copy of z_harm_s.

---

## Solution

Add a **cosine-squared penalty** between z_harm_s and z_harm_a to the training loss:

```
penalty = cosine_similarity(z_harm_s, z_harm_a)^2
loss += harm_nonredundancy_weight * penalty
```

`cos^2` penalises both positive and negative alignment symmetrically. Gradient is zero when
the streams are orthogonal; maximal when they are parallel (redundant).

### ARC-016 coupling

When `harm_nonredundancy_precision_scale > 0`, the penalty is scaled by normalised E3
precision:

```
precision_norm = min(e3.current_precision / 500.0, 2.0)
penalty *= (1 + harm_nonredundancy_precision_scale * precision_norm)
```

Higher precision (more confident state) → stronger non-redundancy enforcement. Biological
basis: in a stable, well-understood environment, the two harm streams should be maximally
informative (least redundant); in a volatile/uncertain environment, some redundancy is
tolerated (precision is low).

### Config params (REEConfig)

| Param | Type | Default | Purpose |
|-------|------|---------|---------|
| `harm_nonredundancy_weight` | float | `0.0` | loss weight (0 = disabled, backward compat) |
| `harm_nonredundancy_precision_scale` | float | `0.0` | ARC-016 coupling strength |

### New agent method: `compute_harm_nonredundancy_loss(latent_state)`

Returns the penalty scalar. Returns 0 when:
- `harm_nonredundancy_weight=0.0` (default)
- Either harm stream is absent from the latent state

---

## Architecture Context

Operates on z_harm_s (from HarmEncoder) and z_harm_a (from AffectiveHarmEncoder) after
encoding. No new modules — purely a loss-level constraint.

If z_harm_s dim != z_harm_a dim, the method projects to the smaller dimensionality
(first `min_dim` elements) before computing cosine similarity.

---

## What This SD Enables

- Structurally valid z_harm_a before SD-020 (precision-weighted PE) can be added
- EXQ-319 SD-022 dissociation test (HIGH_DAMAGE vs FRESH) depends on streams being distinct
- SD-020 becomes scientifically meaningful only after SD-019 reduces baseline redundancy

---

## Biological Grounding

Barlow (1961) redundancy reduction hypothesis: efficient neural coding minimises
redundancy between channels. A-delta (sensory-discriminative) and C-fiber
(paleospinothalamic, affective-motivational) pathways project to distinct cortical regions
(S1/S2 vs ACC/anterior insula) via distinct thalamic nuclei (VPL/VPM vs intralaminar
CM/PF). Cross-stream redundancy is biologically implausible for functionally distinct
channels serving different computational purposes.

---

## ML Engineering Notes

Technique: decorrelation loss (Barlow Twins 2021 uses a related approach). Standard
contrastive approach would push representations apart in norm-space; cos^2 is more
appropriate here because it is scale-invariant and penalises alignment, not distance.

Known failure mode: aggressive decorrelation collapses useful shared structure. Mitigation:
`cos_sim^2` penalises correlation, not dissimilarity — the streams can have the same norm
while being orthogonal. `harm_nonredundancy_weight=0.0` default ensures backward compat.

---

## Related Claims

- SD-019 (harm_stream.affective_nonredundancy)
- SD-011 (harm_stream.dual_nociceptive_streams)
- SD-020 (harm_stream.affective_surprise_pe — depends on SD-019)
- ARC-016 (cognitive_modes.control_plane_regimes — precision coupling)
- MECH-219, Q-036
