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
   - **review_tracker.json is ~1400 lines (~47k tokens). Do NOT read the full file.**
   - Check `evidence/experiments/review_tracker_summary.md` for coverage state and instructions.
   - Read only the tail: `Read` with `offset=1385, limit=15` to find the insertion point.
   - Update `last_review_utc` with a targeted Edit on line 3 only.
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

## Known Indexer Limitation: evidence_direction is Per-Experiment, Not Per-Claim

The indexer applies a single `evidence_direction` (supports/weakens/mixed) to **all** claims tagged
in a multi-claim experiment, derived from the overall PASS/FAIL outcome. This is systematically wrong
for multi-claim experiments where only some claims' criteria fail.

**Canonical example (2026-03-22):** EXQ-023 tested SD-008, SD-003, MECH-098, ARC-016 together.
SD-008's criterion (event_selectivity_margin=0.084) **passed**. But SD-007 R² and SD-003 calibration
failed, making the overall outcome FAIL and marking SD-008 as "weakens" — incorrect.

**Workaround:** When manual review identifies a per-claim direction error, correct the manifest
`evidence_direction` field directly and add an `evidence_direction_note` explaining the correction.
Rebuild the index after. This is a manual process — the pipeline does not detect these errors.

**Design gap:** A future indexer version should support `evidence_direction_per_claim` in manifests
so multi-claim experiments can record independent pass/fail per tagged claim. Not yet implemented.

## claim_ids Accuracy Rule (CRITICAL)

**`claim_ids` must reflect what the experiment actually tests, not what it was originally designed to test.**

This is a scientific accuracy issue, not a tagging detail. The governance algorithm computes confidence scores and conflict ratios directly from these tags — wrong tags corrupt the evidence record.

Rules:
1. **Do not inherit claim_ids from a prior iteration.** When writing EXQ-Nb to fix EXQ-N, re-evaluate from scratch which claims the new version tests. If the fix changed what is being measured, the claim_ids must change too.
2. **Do not tag a claim because the experiment was *intended* for it.** Tag only what the experiment directly tests with its actual implementation. Broken instrumentation, mislabelled conditions, or scope-drift during iteration are all reasons to change the tag.
3. **When architectural distinctions are being refined, err toward fewer tags.** Include a claim ID only if the experiment would produce interpretable signal for that claim specifically. Tagging related-but-distinct claims "for completeness" contaminates both claims' evidence records.
4. **At script-writing time, state the mechanism under test explicitly** in the docstring and verify that claim_ids matches. The question to answer: "If this experiment PASSes, which claim does that support, and why?"

**Canonical example of the failure mode (2026-03-22):** EXQ-048 was designed for MECH-057b (hippocampal candidacy gate) but had broken instrumentation — BetaGate was never called. EXQ-048b fixed the routing, shifting the mechanism under test to MECH-090 (BG beta propagation gate), but MECH-057b was carried forward in claim_ids. EXQ-059 and EXQ-060 then copied this tag list. Result: MECH-057b accumulated 2 false supports and 3 false mixed entries, producing a spurious confidence score of 0.66 with no genuine evidence. All had to be manually corrected.

## Experiment Proposals

- Proposals live in `evidence/planning/experiment_proposals.v1.json`
- After experiments run, mark addressed proposals `status: "executed"` — they are
  not auto-updated by the governance pipeline.
- The indexer (`build_experiment_indexes.py`) rebuilds `claim_evidence.v1.json`
  which is the ground truth for what evidence exists per claim.

## V3-Pending Gate

Claims with `v3_pending: true` or `implementation_phase: v3` in claims.yaml get
`hold_pending_v3_substrate` recommendations — do not promote until V3 evidence arrives.
