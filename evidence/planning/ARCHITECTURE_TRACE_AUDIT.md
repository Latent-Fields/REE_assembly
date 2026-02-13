# Architecture Trace Audit

Generated: `2026-02-13T15:32:39.697392Z`

## Summary

- Nodes traced from sensory roots: 13/14
- Edges traversed: 19/22
- Unowned edges: 1
- Ambiguous edges: 3
- Trace breaks: 1
- Open sections without owner claims: 1
- Suggested claim stubs: 6

## Missing Dependency Targets

- _none_

## Dependency Link Gaps

- `ISS-DEP-LINK-GAP-IFACE-EDGE-001` edge_id=IFACE-EDGE-001; source_claim_ids=ARC-017; target_claim_ids=ARC-002
- `ISS-DEP-LINK-GAP-IFACE-EDGE-002` edge_id=IFACE-EDGE-002; source_claim_ids=ARC-017; target_claim_ids=ARC-002
- `ISS-DEP-LINK-GAP-IFACE-EDGE-003` edge_id=IFACE-EDGE-003; source_claim_ids=ARC-017; target_claim_ids=ARC-002
- `ISS-DEP-LINK-GAP-IFACE-EDGE-004` edge_id=IFACE-EDGE-004; source_claim_ids=ARC-017, ARC-015; target_claim_ids=ARC-002
- `ISS-DEP-LINK-GAP-IFACE-EDGE-020` edge_id=IFACE-EDGE-020; source_claim_ids=ARC-013, MECH-056; target_claim_ids=ARC-005, MECH-054
- `ISS-DEP-LINK-GAP-IFACE-EDGE-022` edge_id=IFACE-EDGE-022; source_claim_ids=ARC-017; target_claim_ids=ARC-010, MECH-051, MECH-052

## Unowned Edges

- `ISS-UNOWNED-EDGE-IFACE-EDGE-022` edge_id=IFACE-EDGE-022; from_node=SENSORY.world_tag; to_node=SOCIAL.other_model

## Ambiguous Edges

- `ISS-AMBIGUOUS-EDGE-IFACE-EDGE-020` edge_id=IFACE-EDGE-020; unknown_fields=signed_pe_precision_mix_rule, noradrenaline_imminence_interaction, stage_separation_constraints; linked_open_questions=Q-011
- `ISS-AMBIGUOUS-EDGE-IFACE-EDGE-021` edge_id=IFACE-EDGE-021; unknown_fields=bias_amplitude_bounds, channel_escalation_trigger; linked_open_questions=Q-011
- `ISS-AMBIGUOUS-EDGE-IFACE-EDGE-022` edge_id=IFACE-EDGE-022; unknown_fields=agency_detection_schema, other_harm_projection_gate; linked_open_questions=Q-009

## Trace Breaks

- `ISS-TRACE-BREAK-SOCIAL-OTHER_MODEL` node_id=SOCIAL.other_model; owner_claim_ids=ARC-010, MECH-051, MECH-052

## Open Sections Without Ownership

- `ISS-OPEN-UNOWNED-OPEN-003` open_section_id=OPEN-003; doc=docs/architecture/social.md

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

## Stub Suggestions

- `STUB-0001` type=`architectural_commitment` subject=`interface.sensory.world_tag_to_social.other_model` location=`docs/architecture/overview.md`
- `STUB-0002` type=`open_question` subject=`interface.iface-edge-020.ambiguity` location=`docs/architecture/residue_geometry.md`
- `STUB-0003` type=`open_question` subject=`interface.iface-edge-021.ambiguity` location=`docs/architecture/residue_geometry.md`
- `STUB-0004` type=`open_question` subject=`interface.iface-edge-022.ambiguity` location=`docs/architecture/overview.md`
- `STUB-0005` type=`open_question` subject=`open_section.open-003.ownership` location=`docs/architecture/social.md`
- `STUB-0006` type=`mechanism_hypothesis` subject=`trace.continuation.social.other_model` location=`docs/architecture/social.md`
