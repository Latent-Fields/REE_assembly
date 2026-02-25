# Runtime Authority Probe Summary: runtime_authority_commit_boundary_seed11_20260225T195039888432Z

## Outcome
- seed: `11`
- run_status: `PASS`
- evidence_direction: `supports`
- failure_signatures: `none`

## Scenario Steps
- safe_write_commit: allowed=True, reason=allowed, rc_state=NORMAL, commit_id=a300e0b2-e59a-4c71-bf09-ec891f8c584e, ledger_event=commit_executed
- destructive_commit_with_consent: allowed=True, reason=allowed, rc_state=NORMAL, commit_id=e61c69fa-0e62-4f50-ba4c-4e24e6cd09a9, ledger_event=commit_executed
- post_dispatch_lockdown_reflex: allowed=False, reason=lockdown_posture_block, rc_state=LOCKDOWN, commit_id=none, ledger_event=proposal_rejected
- privileged_without_consent: allowed=False, reason=consent_required, rc_state=NORMAL, commit_id=none, ledger_event=proposal_rejected

## Key Metrics
- boundary_reclassification_error_rate: 0.000000
- commit_executed_count: 2.000000
- commit_lineage_integrity_rate: 1.000000
- commit_token_coverage_rate: 1.000000
- consent_gate_rejection_rate: 0.500000
- lockdown_rejection_rate: 0.500000
- mean_rc_conflict_score: 0.416509
- post_commit_safety_reflex_rate: 0.500000
- privileged_release_under_lockdown_count: 0.000000
- proposal_rejected_count: 2.000000
- rejection_without_commit_rate: 1.000000
- seed_used: 11.000000
- total_cycles: 4.000000

## Interpretation
Runtime authority probes exercised commit minting, rejection lineage, and lockdown reflex behavior for post-dispatch safety pressure.
