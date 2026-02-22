# REE_convergence Interface

Date: 2026-02-22  
Status: Active

## Purpose

Define the minimal interface between:

- `REE_assembly` (canonical REE architecture, claims, and governance), and
- `REE_convergence` (external-source intake, translation, and candidate delta development).

## Repository Roles

1. `REE_assembly`
- Owns canonical claims, architecture docs, and adoption decisions.
- Owns final machine contracts and governance outcomes.
- Accepts external updates only through promotion packets and review.

2. `REE_convergence`
- Owns external-source intake workflow and evidence-first translation.
- Owns provisional mappings, separation checks, and candidate deltas before promotion.

## Upstream Inputs From `REE_convergence`

- Promotion packets (JSON) copied into:
  - `evidence/planning/convergence_packets/inbox/`
- Optional source-side supporting docs linked from each packet.

Packet contract:
- `evidence/planning/schemas/v1/convergence_promotion_packet.schema.json`
- `evidence/planning/CONVERGENCE_PROMOTION_PACKET_TEMPLATE.json`

## Downstream Outputs From `REE_assembly`

- Queue and validation status for intake packets:
  - `evidence/planning/convergence_intake_queue.v1.json`
  - `evidence/planning/CONVERGENCE_INTAKE_QUEUE.md`
- Governance outcomes (accept/reject/hybridize/defer) captured through existing planning/decision flow.

## Operating Rule

Do not directly copy unresolved external-source analysis into canonical architecture docs.

Promotion path is:

1. intake in `REE_convergence`,
2. packet submission into `REE_assembly` inbox,
3. queue generation + human review,
4. canonical promotion only after explicit adjudication.

## Validation Commands

```bash
python3 evidence/planning/scripts/validate_convergence_promotion_packet.py \
  --input-glob "evidence/planning/convergence_packets/inbox/*.json"

python3 evidence/planning/scripts/build_convergence_intake_queue.py
```
