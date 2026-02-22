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
  --input-glob "evidence/planning/convergence_packets/inbox/*.json" \
  --check-gate-readiness \
  --fail-on-gate-failure
```

## Queue Build

```bash
python3 evidence/planning/scripts/build_convergence_intake_queue.py --fail-on-invalid
```

## Required Epistemic Controls

Each packet must include:

- `falsification`:
  - explicit claim under test,
  - disconfirming conditions (`could_be_wrong_if`),
  - test-plan references (`test_plan_refs`).
- `governance_controls`:
  - `blast_radius`: `lexical` | `interface` | `architecture`,
  - conflict review status/notes,
  - probation window days,
  - rollback conditions/owner.
- `implementation_readiness`:
  - `mechanism_probe_ids` (required for `interface`/`architecture`),
  - `adapter_patch_refs` (required for `interface`/`architecture`),
  - `benchmark_acceptance_criteria` (required for `interface`/`architecture`),
  - implementation owner/status.
- `source` licensing/provenance:
  - `content_mode` (what is being reused),
  - `upstream_license_id`,
  - `license_review_status` must be `verified`,
  - `license_review_notes`,
  - if `content_mode` is `quoted_text`, `code_copied`, `weights_used`, or `mixed`, include:
    - `attribution_paths` (non-empty),
    - `reuse_notes` (non-empty).

Gate-ready status is blocked when placeholder evidence tokens (`TODO`, `Needs evidence`, `example.org`) appear in
evidence-bearing fields.
