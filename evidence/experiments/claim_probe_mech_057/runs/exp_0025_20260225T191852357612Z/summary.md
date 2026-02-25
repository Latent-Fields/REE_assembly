# Run Summary: EXP-0025

## Scenario
- proposal_id: `EXP-0025`
- claim_id: `MECH-057`
- experiment_type: `claim_probe_mech_057`
- seed: `713397892`

## Outcome
- run_status: `FAIL`
- evidence_direction: `weakens`
- failure_signatures: `mech057:action_prediction_gap, mech057:consequence_model_drift, mech057:lineage_integrity_drop`

## Key Metrics
- action_emission_without_prediction_rate: 0.245944
- action_lineage_integrity_rate: 0.745147
- consequence_prediction_drift_rate: 0.253565
- seed_used: 713397892.000000

## Interpretation
Claim-aware stress metrics are emitted from proposal context to preserve architecture-level nuance in dispatch evidence.
