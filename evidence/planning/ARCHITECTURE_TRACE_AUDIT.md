# Architecture Trace Audit

Generated: `2026-02-13T16:34:49.726149Z`

## Summary

- Nodes traced from sensory roots: 13/14
- Edges traversed: 20/23
- Unowned edges: 0
- Ambiguous edges: 2
- Trace breaks: 0
- Open sections without owner claims: 0
- Suggested claim stubs: 2

## Missing Dependency Targets

- _none_

## Dependency Link Gaps

- `ISS-DEP-LINK-GAP-IFACE-EDGE-001` edge_id=IFACE-EDGE-001; source_claim_ids=ARC-017; target_claim_ids=ARC-002
- `ISS-DEP-LINK-GAP-IFACE-EDGE-002` edge_id=IFACE-EDGE-002; source_claim_ids=ARC-017; target_claim_ids=ARC-002
- `ISS-DEP-LINK-GAP-IFACE-EDGE-003` edge_id=IFACE-EDGE-003; source_claim_ids=ARC-017; target_claim_ids=ARC-002
- `ISS-DEP-LINK-GAP-IFACE-EDGE-004` edge_id=IFACE-EDGE-004; source_claim_ids=ARC-017, ARC-015; target_claim_ids=ARC-002

## Unowned Edges

- _none_

## Ambiguous Edges

- `ISS-AMBIGUOUS-EDGE-IFACE-EDGE-021` edge_id=IFACE-EDGE-021; unknown_fields=bias_amplitude_bounds, reorientation_dwell_time, saturation_detection_rule; linked_open_questions=Q-011, Q-012
- `ISS-AMBIGUOUS-EDGE-IFACE-EDGE-022` edge_id=IFACE-EDGE-022; unknown_fields=agency_detection_schema, other_harm_projection_gate, selflike_threshold_calibration; linked_open_questions=Q-009

## Trace Breaks

- _none_

## Open Sections Without Ownership

- _none_

## Owned Edges Without Evidence

- `ISS-NO-EVIDENCE-EDGE-IFACE-EDGE-001` edge_id=IFACE-EDGE-001; owner_claim_ids=ARC-017, ARC-002
- `ISS-NO-EVIDENCE-EDGE-IFACE-EDGE-002` edge_id=IFACE-EDGE-002; owner_claim_ids=ARC-017, ARC-002
- `ISS-NO-EVIDENCE-EDGE-IFACE-EDGE-003` edge_id=IFACE-EDGE-003; owner_claim_ids=ARC-017, ARC-002
- `ISS-NO-EVIDENCE-EDGE-IFACE-EDGE-004` edge_id=IFACE-EDGE-004; owner_claim_ids=ARC-017, ARC-002, ARC-015
- `ISS-NO-EVIDENCE-EDGE-IFACE-EDGE-005` edge_id=IFACE-EDGE-005; owner_claim_ids=ARC-001, ARC-002
- `ISS-NO-EVIDENCE-EDGE-IFACE-EDGE-008` edge_id=IFACE-EDGE-008; owner_claim_ids=ARC-002, ARC-018
- `ISS-NO-EVIDENCE-EDGE-IFACE-EDGE-010` edge_id=IFACE-EDGE-010; owner_claim_ids=ARC-018, ARC-003
- `ISS-NO-EVIDENCE-EDGE-IFACE-EDGE-013` edge_id=IFACE-EDGE-013; owner_claim_ids=ARC-003, ARC-015
- `ISS-NO-EVIDENCE-EDGE-IFACE-EDGE-014` edge_id=IFACE-EDGE-014; owner_claim_ids=ARC-017, ARC-015
- `ISS-NO-EVIDENCE-EDGE-IFACE-EDGE-015` edge_id=IFACE-EDGE-015; owner_claim_ids=ARC-015
- `ISS-NO-EVIDENCE-EDGE-IFACE-EDGE-017` edge_id=IFACE-EDGE-017; owner_claim_ids=ARC-015, ARC-003
- `ISS-NO-EVIDENCE-EDGE-IFACE-EDGE-018` edge_id=IFACE-EDGE-018; owner_claim_ids=ARC-001, ARC-015
- `ISS-NO-EVIDENCE-EDGE-IFACE-EDGE-019` edge_id=IFACE-EDGE-019; owner_claim_ids=ARC-018, ARC-015
- `ISS-NO-EVIDENCE-EDGE-IFACE-EDGE-022` edge_id=IFACE-EDGE-022; owner_claim_ids=ARC-010, MECH-031, MECH-032, Q-009
- `ISS-NO-EVIDENCE-EDGE-IFACE-EDGE-023` edge_id=IFACE-EDGE-023; owner_claim_ids=ARC-010, MECH-031, MECH-036, ARC-005

## Stub Suggestions

- `STUB-0001` type=`open_question` subject=`interface.iface-edge-021.ambiguity` location=`docs/architecture/residue_geometry.md`
- `STUB-0002` type=`open_question` subject=`interface.iface-edge-022.ambiguity` location=`docs/architecture/social.md`
