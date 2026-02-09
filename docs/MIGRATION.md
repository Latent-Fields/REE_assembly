# Documentation Migration Summary

**Claim Type:** implementation_note  
**Scope:** Migration mapping and legacy status notes  
**Depends On:** None  
**Status:** legacy  
**Claim ID:** IMPL-006
<a id="impl-006"></a>

This document tracks the migration of content from original locations to the canonical documentation structure.

## Migration Map

### Core Architecture Files

| Original Path | Canonical Path | Status | Notes |
|--------------|----------------|--------|-------|
| `architecture/E1.md` | `docs/architecture/e1.md` | Migrated | Added claim typing header |
| `architecture/E2.md` | `docs/architecture/e2.md` | Migrated | Added claim typing header |
| `architecture/E3.md` | `docs/architecture/e3.md` | Migrated | Added claim typing header |
| `architecture/latent_stack.md` | `docs/architecture/l_space.md` | Migrated | Added claim typing header; renamed for consistency |
| `architecture/control_plane.md` | `docs/architecture/control_plane.md` | Migrated | Added claim typing header |
| `architecture/residue_geometry.md` | `docs/architecture/residue_geometry.md` | Migrated | Added claim typing header |
| `architecture/Default_mode.md` | `docs/architecture/default_mode.md` | Migrated | Added claim typing header |
| `architecture/Hippocampal_braid.md` | `docs/architecture/hippocampal_braid.md` | Migrated | Added claim typing header |
| `docs/glossary.md` | `docs/glossary.md` | In Place | Will be updated with canonical references |

### New Canonical Documents

| Path | Status | Notes |
|------|--------|-------|
| `docs/README.md` | Created | Navigation guide and structure explanation |
| `docs/invariants.md` | Created | 17 core invariants extracted from README.md, REE_CORE.md, DANIEL_README.md |
| `docs/architecture/entities_and_binding.md` | Created | Extracted from DANIEL_README.md Layer 3 |
| `docs/claims/claims.yaml` | Created | Machine-readable claim registry with 28 claims |
| `docs/claims/claim_index.md` | Created | Human-readable claim index |

### Remaining Original Files (Supplementary)

These files remain in their original locations as they provide additional detail or alternative perspectives:

| Path | Type | Relationship to Canonical |
|------|------|---------------------------|
| `architecture/trajectory_selection.md` | Implementation Detail | Overlaps with `e3.md`; provides additional implementation guidance |
| `architecture/depth_phase_spec.md` | Mechanism Hypothesis | Referenced by MECH-001; provides detailed phase-compatibility specification |
| `architecture/precision_scoping.md` | Mechanism Hypothesis | Referenced by MECH-002; provides τ-scoped precision rules |
| `architecture/control_plane_signal_map.md` | Implementation Detail | Supplements `control_plane.md` |
| `architecture/why_attention_must_be_fragmented.md` | Rationale Document | Supports INV-009 |
| `architecture/serotonin.md` | Mechanism Detail | Supplements `control_plane.md` neuromodulatory section |
| `architecture/precision_control.md` | (Check if exists) | Related to `control_plane.md` |
| `architecture/path_authority_and_interrupts.md` | Implementation Detail | Related to `control_plane.md` |

### Subsystems (Preserved Structure)

These subsystems retain their original structure under `architecture/`:

- `architecture/sleep/` → Referenced from canonical docs
- `architecture/language/` → Referenced from canonical docs
- `architecture/social/` → Referenced from canonical docs

## Semantic Mapping

### Self Definition

**Canonical Location:** `REE_CORE.md` §4 "Self (Operational Definition)"

**Definition:** The Self is the **currently committed trajectory prefix**, continuously re-anchored to shared sensory evidence and hippocampal path memory, and extended forward by hippocampal rollouts seeded by fast predictors.

**Status:** Should be promoted to invariant or architectural commitment

**Related Claims:**
- INV-012 (Commitment Gates Responsibility)
- ARC-003 (E3 Selects and Commits Trajectories)
- ARC-008 (Hippocampal Braid Stores Path Memory)

### E1 Implementation Constraint

**Source:** `DANIEL_README.md` Layer 3 §1

**Claim:** "E1 is a predictive field, not a deep network. Shallow, recurrent, multi-rate. Iterative refinement over a shared latent space. Columns as local predictive kernels."

**Status:** Mechanism hypothesis not yet formally documented

**Action Required:** Create `docs/architecture/hypotheses/` or add to MECH claims

## Compatibility Notes

### Forward Compatibility

Original paths in `architecture/` remain accessible. No links will break.

### Canonical References

New documents should reference canonical locations in `docs/architecture/` rather than original `architecture/` locations.

### Cross-Reference Strategy

1. Canonical documents link to each other within `docs/`
2. Supplementary documents in `architecture/` link to canonical documents
3. Root documents (`README.md`, `REE_CORE.md`) link to canonical `docs/` locations

## Archive Strategy

### Content Not Yet Archived

No content has been moved to `docs/archive/` yet. All original files remain in place.

### Future Archive Candidates

Files that may be archived after canonical consolidation:
- Duplicate definitions in multiple files
- Superseded specifications
- Draft documents that have been formalized

## Conflicts and Forks

### Detected Conflicts: None

The consistency analysis found:
- ✓ No circular dependencies
- ✓ All invariants depend only on other invariants
- ✓ No documented conflicts between claims

### Potential Semantic Variations

Areas requiring further review:
1. E1 implementation details (field vs. network)
2. Self definition prominence
3. Phase compatibility mechanism details

## Next Steps

1. Update internal links in root documents to point to canonical locations
2. Add claim typing headers to remaining architecture files
3. Create redirect/superseded notes where appropriate
4. Document any newly discovered conflicts in `docs/conflicts/`
5. Update `docs/glossary.md` to reference canonical definitions

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- IMPL-006

## References / Source Fragments

- `docs/processed/legacy_tree/docs/MIGRATION.md`
