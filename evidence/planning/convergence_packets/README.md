# Convergence Packet Inbox

Place convergence promotion packets here for review in `REE_assembly`.

Primary source-side workflow lives in `REE_convergence/handoff/README.md`.

## Paths

- inbox folder:
  - `evidence/planning/convergence_packets/inbox/`
- receipts folder:
  - `evidence/planning/convergence_packets/receipts/`
- packet schema:
  - `evidence/planning/schemas/v1/convergence_promotion_packet.schema.json`
- packet template:
  - `evidence/planning/CONVERGENCE_PROMOTION_PACKET_TEMPLATE.json`
- receipt schema:
  - `evidence/planning/schemas/v1/convergence_packet_receipt.schema.json`
- receipt template:
  - `evidence/planning/CONVERGENCE_PACKET_RECEIPT_TEMPLATE.json`

## Lifecycle State Model

Use this shared state machine across `REE_convergence` and `REE_assembly`:

1. `draft` (intake team prepares packet)
2. `ready_for_submission` (packet passes source-side checks)
3. `submitted` (packet copied to inbox)
4. `queued` (packet appears in intake queue)
5. `gate_ready` or `gate_blocked`
6. `adjudicated` (`accepted`, `rejected`, `deferred`, or `hybridize`)
7. `closed` (receipt written and linked to decision artifact)

## Validation

```bash
python3 evidence/planning/scripts/validate_convergence_promotion_packet.py \
  --input-glob "evidence/planning/convergence_packets/inbox/*.json" \
  --check-gate-readiness \
  --fail-on-gate-failure
```

Source-side submit + mirror command (run in `REE_convergence`):

```bash
python3 tools/run_cross_repo_handoff.py --assembly-repo ../REE_assembly
```

## Queue Build

```bash
python3 evidence/planning/scripts/build_convergence_intake_queue.py --fail-on-invalid
```

## Receipt Validation

```bash
python3 evidence/planning/scripts/validate_convergence_packet_receipt.py \
  --input-glob "evidence/planning/convergence_packets/receipts/*.json"
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

## Receipt Contract (Required For Closed-Loop Handoff)

After each queue/adjudication transition, write or update a receipt in:

- `evidence/planning/convergence_packets/receipts/`

Each receipt must include at minimum:

- `packet_id`, `queue_state`, `adjudication_state`
- `owner`, `created_at_utc`
- `decision_ref` + `adjudicated_at_utc` when adjudication is final

This ensures every submitted packet has a machine-readable acknowledgment and decision lineage.
