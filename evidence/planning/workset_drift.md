# Inter-Governance Workset Drift Report

Generated: 2026-08-02T09:20:34Z

Re-validates every `ready` item in `evidence/planning/inter_governance_workset.v1.json` against current ground truth (claim status, epistemic_category, substrate_queue `ready` flags, queue-claim coverage, experimental-evidence presence). A ready item that is in fact blocked, done, already-queued, or inappropriate is flagged below. Warn-only -- never blocks the governance pipeline. If findings appear, regenerate the workset (`scripts/generate_inter_governance_workset.py`); if they persist, the generator logic or the ground-truth data has drifted.

## Ready items that look wrong (2)

| item | title | reason |
|------|-------|--------|
| IGW-20260802-219 | Proposal for MECH-166 | proposal EXP-0342 claim MECH-166 already has experimental evidence -- likely executed |
| IGW-20260802-221 | Proposal for MECH-025b | proposal EXP-0361 claim MECH-025b already has experimental evidence -- likely executed |

