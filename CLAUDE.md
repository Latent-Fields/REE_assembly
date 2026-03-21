# REE_assembly

## Git Workflow

Push directly to `master`: `git push origin HEAD:master`

Do NOT create feature branches or pull requests.

## Multi-Session Coordination

See `REE_Working/CLAUDE.md` for the session startup protocol.
Check `REE_Working/WORKSPACE_STATE.md` before editing `docs/claims/claims.yaml`.

## Governance Pipeline

Run `scripts/governance.sh` from repo root — it runs all steps in order:
```
bash scripts/governance.sh          # V3 (default)
bash scripts/governance.sh --v2     # V2 (also syncs from ree-v2/)
```

Or manually, from repo root:

**V3 pipeline** (V3 results write directly to `evidence/experiments/` — no sync step):
```
python evidence/experiments/scripts/build_experiment_indexes.py
python scripts/generate_pending_review.py
```

**V2 pipeline** (syncs from `../ree-v2/evidence/experiments/` first):
```
python evidence/experiments/scripts/sync_v2_results.py
python evidence/experiments/scripts/build_experiment_indexes.py
python scripts/generate_pending_review.py
```

**After editing `docs/claims/claims.yaml`** (governance decisions, new claims, status updates):
```
python scripts/build_claims_json.py   # rebuilds docs/assets/data/claims.json for site tooltips
```

`governance.sh` runs `build_claims_json.py` automatically as its final step.

## Experiment Review Protocol

After each governance/experiment discussion session:

1. **Check** `evidence/experiments/pending_review.md` at session start — flag to user before other work.
2. **Discuss** each pending result with the user (claim implications, PASS/FAIL interpretation, next steps).
3. **Mark reviewed** — add run IDs to `reviewed_run_ids` in `evidence/experiments/review_tracker.json`, update `last_review_utc`.
4. **Confirm cleared** — re-run `python scripts/generate_pending_review.py` and verify 0 pending before closing the session.
5. **Mark proposals executed** — any `experiment_proposals.v1.json` entry whose claim now has evidence should be set `status: "executed"`. The pipeline does NOT do this automatically.

> The pipeline generates `pending_review.md` automatically, but marking runs reviewed is always manual. Step 4 (confirm cleared) is the enforcement gate — do not skip it.

## Experiment Result Tagging

- `run_id` must end `_v2` (V2 runs) or `_v3` (V3 runs)
- `architecture_epoch` must be `"ree_hybrid_guardrails_v1"`
- Results go to `evidence/experiments/`
- V3 experiment scripts write `claim_ids` (list) in their flat JSON output.
  The runner writes `claim_ids_tested` in `runs/**/manifest.json`.
  The indexer accepts both — no action needed, but use `claim_ids` in new V3 scripts.

## Experiment Proposals

- Proposals live in `evidence/planning/experiment_proposals.v1.json`
- After experiments run, mark addressed proposals `status: "executed"` — they are
  not auto-updated by the governance pipeline.
- The indexer (`build_experiment_indexes.py`) rebuilds `claim_evidence.v1.json`
  which is the ground truth for what evidence exists per claim.

## V3-Pending Gate

Claims with `v3_pending: true` or `implementation_phase: v3` in claims.yaml get
`hold_pending_v3_substrate` recommendations — do not promote until V3 evidence arrives.
