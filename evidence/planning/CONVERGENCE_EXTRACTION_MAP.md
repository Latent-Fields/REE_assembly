# JEPA Convergence Extraction Map (REE_assembly -> REE_convergence)

Date: 2026-02-22  
Status: Active

## Purpose

Define what should remain canonical in `REE_assembly` versus what should move to `REE_convergence` for cleaner
evidence hygiene.

## Decision

Do a **partial extraction**:

- keep canonical REE architecture decisions and machine contracts in `REE_assembly`,
- move external-source intake, translation, and pre-promotion comparison work into `REE_convergence`,
- re-enter `REE_assembly` only through explicit promotion packets and review.

## Keep In `REE_assembly` (Canonical)

1. Claim registry and claim lifecycle metadata:
- `docs/claims/claims.yaml`
- `docs/claims/claim_index.md`

2. Canonical architecture positions and adopted contracts:
- `docs/architecture/jepa_e1e2_integration_contract.md`
- `docs/architecture/ree_v2_spec.md`
- `docs/architecture/agency_responsibility_flow.md`

3. Machine-readable ingestion and experiment contracts:
- `evidence/experiments/schemas/v1/jepa_adapter_signals.v1.json`
- `evidence/experiments/schemas/v1/manifest.schema.json`

4. Governance outputs and adjudication state:
- `evidence/decisions/*`
- `evidence/planning/*` (generated planning artifacts and agendas)

## Move To `REE_convergence` (External Intake Layer)

1. External source intake records and minimally interpreted claims:
- source metadata, claim extraction tables, source-specific glossaries

2. Cross-source comparison work:
- REE comparison matrices
- separation-test checklists tied to external systems

3. Candidate deltas before canonical acceptance:
- provisional adapter ideas
- integration hypotheses not yet adjudicated in `REE_assembly`

4. Translation and vocabulary harmonization drafts:
- source-level terminology mappings before promotion to canonical glossary

## Promotion Contract (How Work Re-enters `REE_assembly`)

1. `REE_convergence` emits a promotion packet JSON using:
- `evidence/planning/schemas/v1/convergence_promotion_packet.schema.json`

2. Packet is copied into:
- `evidence/planning/convergence_packets/inbox/`

3. Validate packet(s):
- `python3 evidence/planning/scripts/validate_convergence_promotion_packet.py --input-glob "evidence/planning/convergence_packets/inbox/*.json"`

4. Build review queue:
- `python3 evidence/planning/scripts/build_convergence_intake_queue.py`

5. Human governance decides promotion outcome:
- retain as convergence-only,
- hybridize into canonical docs/contracts,
- adopt external structure,
- or reject/defer.

## Extraction Phases

1. Phase 1 (Now): stop adding new external-intake prose directly into canonical docs unless it is already adjudicated.
2. Phase 2: relocate ongoing source-intake drafting work to `REE_convergence` and reference packet IDs in REE planning.
3. Phase 3: enforce packet-first promotion for any external-source change touching canonical claim/docs/contracts.
4. Phase 4: optionally automate cross-repo packet sync after packet format stabilizes.
