# REE_assembly

## Git Workflow

Push directly to `master`: `git push origin HEAD:master`

Do NOT create feature branches or pull requests.

## Multi-Session Coordination

See `REE_Working/CLAUDE.md` for the session startup protocol.
Check `REE_Working/WORKSPACE_STATE.md` before editing `docs/claims/claims.yaml`.

## Governance Pipeline

From repo root, after experiments complete:
```
python scripts/sync_v3_results.py      # (or sync_v2_results.py for V2)
python scripts/build_experiment_indexes.py
python scripts/generate_pending_review.py   # updates evidence/experiments/pending_review.md
```
This updates `evidence/planning/promotion_demotion_recommendations.md` and `evidence/experiments/pending_review.md`.

After any changes to `docs/claims/claims.yaml`, also run:
```
python scripts/build_claims_json.py    # rebuilds docs/assets/data/claims.json for hover tooltips
```

## Experiment Result Tagging

- `run_id` must end `_v2` (V2 runs) or `_v3` (V3 runs)
- `architecture_epoch` must be `"ree_hybrid_guardrails_v1"`
- Results go to `evidence/experiments/`

## V3-Pending Gate

Claims with `v3_pending: true` or `implementation_phase: v3` in claims.yaml get
`hold_pending_v3_substrate` recommendations — do not promote until V3 evidence arrives.
