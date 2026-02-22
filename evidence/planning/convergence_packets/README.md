# Convergence Packet Inbox

Place convergence promotion packets here for review in `REE_assembly`.

## Paths

- inbox folder:
  - `evidence/planning/convergence_packets/inbox/`
- packet schema:
  - `evidence/planning/schemas/v1/convergence_promotion_packet.schema.json`
- packet template:
  - `evidence/planning/CONVERGENCE_PROMOTION_PACKET_TEMPLATE.json`

## Validation

```bash
python3 evidence/planning/scripts/validate_convergence_promotion_packet.py \
  --input-glob "evidence/planning/convergence_packets/inbox/*.json"
```

## Queue Build

```bash
python3 evidence/planning/scripts/build_convergence_intake_queue.py
```
