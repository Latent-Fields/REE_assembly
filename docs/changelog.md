# Documentation Refactoring Changelog

**Claim Type:** implementation_note  
**Scope:** Documentation change history  
**Depends On:** None  
**Status:** stable  
**Claim ID:** IMPL-014
<a id="impl-014"></a>

## 2026-02-08: Thought Intake — Residue as Cognitive Map

### Overview

Captured a clarification that residue geometry is both a terrain and a recorded path, framing hippocampal traces as a cognitive map of thought trajectories.

### What Changed

- Updated `docs/architecture/residue_geometry.md` (ARC-013) to describe residue as terrain plus recorded traversal paths.
- Added `docs/thoughts/2026-02-08_residue_paths_cognitive_map.md`.
- Updated `docs/claims/claim_index.md` summary for ARC-013.

## 2026-02-08: Legacy M Alignment and Claim Triage

### Overview

Aligned canonical docs to treat the explicit ethical cost term \(M\) as legacy-only, and triaged open-question statuses.

### What Changed

- Marked explicit \(M\) references as legacy/evaluation-only in `docs/glossary.md`, `docs/REE_MIN_SPEC.md`, `docs/examples/toy_world_environment.md`, `docs/examples/toy_world_scoring_functions.md`, `docs/architecture/trajectory_selection.md`, `docs/architecture/social.md`, and `docs/REE_overview.md`.
- Clarified failure mode #5 in `docs/REE_failure_modes.md` to reference legacy \(M\) proxies or residue penalties rather than an explicit cost term.
- Updated `docs/claims/claims.yaml` to mark open questions (Q-001..Q-006) as active.

## 2026-02-08: Candidate Claim Promotions

### Overview

Promoted selected candidate claims to stable or provisional based on maturity and architectural scope.

### What Changed

- Promoted `INV-018` to stable (agency required).
- Promoted `ARC-006`, `ARC-008`, `ARC-015`, and `ARC-016` to provisional.
- Updated claim registry and aligned section headers where needed.

## 2026-02-08: Typed-Claims Docs Rebuild

### Overview

Rebuilt canonical REE documentation as a typed-claims system assembled from preserved sources with minimal glue text.

### What Changed

- Added `docs/processed/legacy_tree/` with a verbatim mirror of all documentation-like files and a manifest.
- Refreshed canonical docs under `docs/` with claim IDs, typed headers, and required end sections.
- Added new canonical files: `docs/architecture/hippocampal_systems.md` and `docs/architecture/temporal_dynamics.md`.
- Rebuilt `docs/claims/claims.yaml` and `docs/claims/claim_index.md` to index all current claims.
- Added `docs/conflicts/ethics_module_vs_cost_term.md` to capture a documented tension.
- Rewrote `docs/README.md` as executable agent guidance with verbatim prompts.

### Legacy Preservation

All prior documentation-like files are preserved verbatim under `docs/processed/legacy_tree/` with their original paths.

### Conflicts Recorded

- `docs/conflicts/ethics_module_vs_cost_term.md`

## 2026-02-08: Subsystem Promotions and Conflict Resolution

### Overview

Promoted language, social, and sleep subsystems into canonical typed-claims docs; added astrocyte-aware control-plane hypothesis; resolved the ethics-cost-term conflict.

### What Changed

- Added canonical subsystem docs:
  - `docs/architecture/language.md`
  - `docs/architecture/social.md`
  - `docs/architecture/sleep.md`
- Added `docs/architecture/astrocyte_regulatory_stack.md` as a control-plane mechanism hypothesis.
- Updated `docs/claims/claims.yaml` and `docs/claims/claim_index.md` with new ARC/MECH/Q claims.
- Resolved `docs/conflicts/ethics_module_vs_cost_term.md` and updated canonical E3 framing to remove explicit cost terms.

## 2026-02-08: Minimum Spec Alignment

### Overview

Aligned the minimum specification with the current canonical framing that removes explicit ethical cost terms.

### What Changed

- Added canonical notes to `docs/REE_MIN_SPEC.md` clarifying that explicit ethical cost terms are legacy.

## 2026-02-08: Extended Preservation Sweep

### Overview

Extended preservation to non-markdown REE-relevant files and extracted code comment fragments.

### What Changed

- Added `CITATION.cff` and `.github/ISSUE_TEMPLATE/*.yml` to `docs/processed/legacy_tree/`.
- Added `docs/processed/extracted_fragments/code_comments.md` with verbatim excerpts from `src/cathedral.py`.

## 2026-02-08: Astrocyte Stack Relocation

### Overview

Relocated the astrocyte-aware regulatory stack subsystem out of `docs/` to keep canonical docs focused on typed-claims files.

### What Changed

- Moved `docs/astrocyte_aware_regulatory_stack/` to `architecture/astrocyte_aware_regulatory_stack/`.

## 2026-02-08: Full Legacy Capture and Intake Workflow

### Overview

Captured all original documentation-like sources into canonical typed-claims files or indexed claims, and added a thoughts/resolution intake workflow.

### What Changed

- Added canonical docs for remaining architecture, language, sleep, and example files.
- Added `docs/thoughts/` and `docs/conflicts/resolutions/` with workflow guidance.
- Added repository meta, roadmap, and notes docs to the canonical set.
- Updated claim registry and claim index to include all remaining sources.

## 2026-02-08: Thought Intake — Control Plane, Modes, Responsibility

### Overview

Processed a new thought on control-plane mode shaping, temporal “now” construction, hippocampal hypothesis injection, and responsibility flow.

### What Changed

- Added `docs/thoughts/2026-02-08_control_plane_modes_responsibility_flow.md`.
- Added `docs/architecture/agency_responsibility_flow.md` and updated control-plane, mode-manager, temporal-dynamics, and hippocampal systems docs.
- Added INV-018, ARC-015, MECH-019..MECH-024, and Q-006 to the claim registry and index.

## 2026-02-08: Thought Intake — Modes as Control-Plane Regimes

### Overview

Processed a new thought detailing control-plane regimes for action, vigilance, reflective/DMN cognition, sleep modes, and pathological extremes.

### What Changed

- Added `docs/thoughts/2026-02-08_modes_of_cognition_control_plane_regimes.md`.
- Updated `docs/architecture/mode_manager.md`, `docs/architecture/default_mode.md`, and `docs/architecture/sleep.md`.
- Added ARC-016 and MECH-025..MECH-030 to the claim registry and index.

## 2026-02-08: Split Modes of Cognition Doc and Cross-Link Failures

### Overview

Separated the control-plane regime taxonomy into its own architecture file and cross-linked regime pathologies into the failure-mode taxonomy.

### What Changed

- Added `docs/architecture/modes_of_cognition.md` and trimmed regime details from `docs/architecture/mode_manager.md`.
- Updated claim registry/index links for ARC-016 and MECH-025..MECH-028.
- Linked regime pathologies into `docs/REE_failure_modes.md`.

## 2026-02-07: Systematic Documentation Refactoring

### Overview

Completed a comprehensive 8-phase refactoring of REE documentation to create a structured, dependency-aware system that explicitly surfaces inconsistencies rather than resolving them silently.

### Phase 1: Inventory ✓

**Completed:**
- Scanned all documentation files (.md format)
- Identified 56+ markdown files across repository
- Catalogued core concepts: E1, E2, E3, L-space, control plane, residue, entities, binding
- Located repeated definitions and potential conflicts

**Key Findings:**
- Core architecture well-documented in `architecture/` directory
- Three critical root documents: `README.md`, `REE_CORE.md`, `DANIEL_README.md`
- Subsystems organized under: `sleep/`, `language/`, `social/`
- Existing `docs/` directory with REE_MIN_SPEC.md and other specifications

### Phase 2: Canonical Structure ✓

**Created:**
- `docs/README.md` — Navigation guide explaining structure and reading paths
- `docs/invariants.md` — 17 non-negotiable architectural invariants
- `docs/architecture/` — Canonical architecture documents
  - `e1.md`, `e2.md`, `e3.md`
  - `l_space.md` (renamed from latent_stack.md)
  - `control_plane.md`
  - `residue_geometry.md`
  - `default_mode.md`
  - `hippocampal_braid.md`
  - `entities_and_binding.md` (newly synthesized)
- `docs/claims/` — Claim registry directory
- `docs/conflicts/` — Conflict documentation directory (prepared)
- `docs/archive/` — Archive directory (prepared)

**Directory Structure:**
```
docs/
  README.md
  invariants.md
  glossary.md (existing, to be updated)
  MIGRATION.md
  changelog.md (this file)
  architecture/
    e1.md, e2.md, e3.md
    l_space.md
    control_plane.md
    entities_and_binding.md
    residue_geometry.md
    default_mode.md
    hippocampal_braid.md
  claims/
    claim_index.md
    claims.yaml
  conflicts/ (empty)
  archive/ (empty)
```

### Phase 3: Claim Typing ✓

**Applied to 9 canonical architecture files:**

Standard header format:
```markdown
**Claim Type:** [invariant | architectural_commitment | mechanism_hypothesis | open_question | implementation_note]
**Scope:** [Brief description]
**Depends On:** [List of dependencies]
**Status:** [stable | provisional | legacy | candidate]
```

**Files Updated:**
- All 9 canonical architecture files received claim typing headers
- Dependencies explicitly linked
- Status clearly marked

### Phase 4: Content Migration (Partial)

**Completed:**
- Migrated core architecture files to canonical locations
- Preserved original files in `architecture/` for compatibility
- No content deleted or archived yet (per global rules)

**Deferred:**
- Full content consolidation from supplementary files
- Archive migration for superseded content
- Detailed duplicate removal

**Rationale:** Prioritized structure and claim typing over content consolidation to establish foundation first.

### Phase 5: Claim Registry ✓

**Created:**
- `docs/claims/claims.yaml` — Machine-readable registry with full metadata
- `docs/claims/claim_index.md` — Human-readable indexed list

**Claims Documented:**
- **17 Invariants (INV-001 to INV-017)**
  - Core thesis invariants (3): No ethics module, temporal binding, language emergence
  - Safety invariants (4): Persistent ethics, mirror modeling, residue persistence, language constraint
  - Control invariants (2): Routed precision, attention via modulation
  - Mode invariants (3): Offline integration, imagination safety, commitment gates
  - Foundational invariants (5): Predictive cognition, content/control separation, constraint-based ethics, stability priority, control failures

- **9 Architectural Commitments (ARC-001 to ARC-009)**
  - Core components (3): E1, E2, E3
  - Latent/control (3): L-space, control plane, residue geometry
  - Modes/memory (2): Default mode, hippocampal braid
  - Entity representation (1): Entities and binding

- **2 Mechanism Hypotheses (MECH-001 to MECH-002)**
  - Phase compatibility binding (candidate)
  - τ-scoped precision (candidate)

**Total: 28 claims**

### Phase 6: Consistency Pass ✓

**Automated Analysis Results:**
- ✓ No circular dependencies
- ✓ All invariants depend only on other invariants
- ✓ No contradictions detected in same-subject claims
- ✓ No documented conflicts

**Dependency Graph Verified:**
- 11 axiomatic invariants (no dependencies)
- 6 derived invariants (depend on other invariants)
- 9 architectural commitments (depend on invariants and other commitments)
- 2 mechanism hypotheses (depend on invariants and commitments)

**Classification Safety:**
- No invariants depend on hypotheses or open questions ✓
- No architectural commitments promote mechanism hypotheses without justification ✓
- Provisional and candidate statuses appropriately marked ✓

### Phase 7: Linking and Hygiene (Partial)

**Completed:**
- Created `docs/MIGRATION.md` with path mapping
- Internal links within canonical docs point to canonical locations
- Cross-references added to architecture files

**Remaining:**
- Update root documents (`README.md`, `REE_CORE.md`) to reference canonical locations
- Add redirect notes to original `architecture/` files
- Verify all orphaned sections

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- IMPL-014

## References / Source Fragments

- `docs/processed/legacy_tree/docs/changelog.md`

### Phase 8: Final Output ✓

See sections below.

---

## Documentation Tree

```
/home/runner/work/Reflective-Ethical-Engine-assembled/Reflective-Ethical-Engine-assembled/
├── README.md (root, to be updated with canonical links)
├── REE_CORE.md (canonical spine, preserved)
├── DANIEL_README.md (refinement process, preserved)
├── CONTRIBUTING.md
├── docs/
│   ├── README.md ✓ NEW
│   ├── invariants.md ✓ NEW
│   ├── glossary.md (existing, to be updated)
│   ├── MIGRATION.md ✓ NEW
│   ├── changelog.md ✓ NEW (this file)
│   ├── REE_MIN_SPEC.md (existing, preserved)
│   ├── REE_overview.md (existing, to be reviewed)
│   ├── REE_failure_modes.md (existing, to be reviewed)
│   ├── architecture/
│   │   ├── e1.md ✓ MIGRATED
│   │   ├── e2.md ✓ MIGRATED
│   │   ├── e3.md ✓ MIGRATED
│   │   ├── l_space.md ✓ MIGRATED
│   │   ├── control_plane.md ✓ MIGRATED
│   │   ├── residue_geometry.md ✓ MIGRATED
│   │   ├── default_mode.md ✓ MIGRATED
│   │   ├── hippocampal_braid.md ✓ MIGRATED
│   │   └── entities_and_binding.md ✓ NEW
│   ├── claims/
│   │   ├── claims.yaml ✓ NEW
│   │   └── claim_index.md ✓ NEW
│   ├── conflicts/ (prepared, empty)
│   ├── archive/ (prepared, empty)
│   └── astrocyte_aware_regulatory_stack/ (existing subsystem)
├── architecture/ (original files preserved for compatibility)
│   ├── E1.md, E2.md, E3.md (originals)
│   ├── latent_stack.md, control_plane.md, etc.
│   ├── trajectory_selection.md (supplementary)
│   ├── depth_phase_spec.md (mechanism hypothesis)
│   ├── precision_scoping.md (mechanism hypothesis)
│   ├── sleep/, language/, social/ (subsystems)
│   └── ... (other supplementary files)
└── ... (other repository content)
```

---

## Migration Summary

### Newly Created Files (11)
1. `docs/README.md`
2. `docs/invariants.md`
3. `docs/MIGRATION.md`
4. `docs/changelog.md`
5. `docs/architecture/e1.md`
6. `docs/architecture/e2.md`
7. `docs/architecture/e3.md`
8. `docs/architecture/l_space.md`
9. `docs/architecture/control_plane.md`
10. `docs/architecture/residue_geometry.md`
11. `docs/architecture/default_mode.md`
12. `docs/architecture/hippocampal_braid.md`
13. `docs/architecture/entities_and_binding.md`
14. `docs/claims/claims.yaml`
15. `docs/claims/claim_index.md`

### Modified Files (0)
- No existing files modified (preservation principle)

### Archived Files (0)
- No files archived yet (all content preserved in original locations)

---

## Detected Conflicts

**Count:** 0

No formal conflicts detected during consistency analysis. All claims are compatible within their dependency structure.

### Potential Semantic Variations (For Future Review)

1. **E1 Implementation Details**
   - `DANIEL_README.md` describes E1 as "predictive field, not deep network; shallow, recurrent, multi-rate"
   - This detail not prominently featured in canonical `e1.md`
   - **Action:** Consider adding as MECH claim or architectural note

2. **Self Definition Prominence**
   - Strong operational definition in `REE_CORE.md`: "Self is currently committed trajectory prefix"
   - Should be elevated to architectural commitment or invariant
   - **Action:** Add as ARC-010 or INV-018

3. **Phase Compatibility Mechanism**
   - `depth_phase_spec.md` provides detailed phase-coordinate system
   - `precision_scoping.md` provides τ-scoped precision rules
   - Both are mechanism hypotheses (MECH-001, MECH-002)
   - **Action:** Ensure clear status as candidate mechanisms, not committed architecture

---

## Classification Uncertainties

### Items Flagged for Review

1. **Entities and Binding (ARC-009)**
   - Status: Provisional
   - Reason: Extracted from DANIEL_README.md Layer 3; needs fuller specification
   - Recommendation: Expand with detailed emergence mechanisms and binding constraints

2. **Phase Compatibility (MECH-001)**
   - Status: Candidate
   - Reason: Detailed specification exists but marked as hypothesis
   - Recommendation: Test and validate before promoting to architectural commitment

3. **τ-Scoped Precision (MECH-002)**
   - Status: Candidate
   - Reason: Strong normative language ("MUST") but still marked as hypothesis
   - Recommendation: Clarify if this is mechanism hypothesis or architectural requirement

### Items Successfully Classified

All 17 invariants have clear, conservative classification:
- No borderline cases
- No conflicting invariants requiring downgrade
- All dependencies valid

All 9 architectural commitments have stable or provisional status:
- 8 stable
- 1 provisional (entities_and_binding)

---

## Statistics

- **Total Documentation Files:** 56+ markdown files
- **Canonical Architecture Files:** 9
- **Total Claims:** 28
  - Invariants: 17 (60.7%)
  - Architectural Commitments: 9 (32.1%)
  - Mechanism Hypotheses: 2 (7.2%)
- **Claim Statuses:**
  - Active: 17 (invariants)
  - Stable: 8 (architectural commitments)
  - Provisional: 1 (entities_and_binding)
  - Candidate: 2 (mechanism hypotheses)
- **Dependency Relationships:** 35+ documented dependencies
- **Circular Dependencies:** 0
- **Documented Conflicts:** 0

---

## Principles Followed

All global rules were respected:

1. ✓ No content deleted
2. ✓ Original wording preserved where possible
3. ✓ No silent meaning changes
4. ✓ No silent claim type changes
5. ✓ No contradictions resolved by choosing "winner"
6. ✓ Uncertain classifications marked as provisional/candidate
7. ✓ Invariants treated conservatively

---

## Next Steps (Deferred)

The following items were identified but deferred for future work:

1. Decide promotion/demotion for remaining candidate claims (IMPL-008, IMPL-016, MECH-001..MECH-030).
2. Expand `docs/architecture/entities_and_binding.md` with emergence/binding mechanisms and resolve Q-001.
3. Add Self operational definition as a formal claim and link dependencies (candidate ARC or INV).
4. Formalize the E1 implementation constraint from `DANIEL_README.md` as a mechanism hypothesis.
5. Review and consolidate duplicate content across supplementary files and legacy references.
6. Decide whether to split mechanism hypotheses into a dedicated directory if the count continues to grow.

---

## Conclusion

This refactoring establishes a solid foundation for REE documentation:
- Clear dependency structure
- Explicit claim typing
- No hidden conflicts
- Preserved content safety
- Machine-readable registry
- Human-readable navigation

The documentation is now ready for:
- Systematic evolution via the claim registry
- Safe refinement following DANIEL_README.md process
- Falsifiable architectural testing
- Multi-contributor collaboration with clear change boundaries
