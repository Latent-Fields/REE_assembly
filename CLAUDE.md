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
`build_claims_json.py` runs `scripts/validate_claims.py` first (warn-only mode currently).

## Lit/Exp Decoupling Shadow (Option E, Phase 1)

The governance pipeline is mid-transition between two regimes for how literature
and experimental evidence combine into claim confidence.

**Legacy regime (still authoritative):** `overall_confidence` blends `exp_conf`
and `lit_conf` via a weighted average. Used by every promotion/demotion gate.

**Decoupled regime (shadow only in Phase 1):** lit and exp are separate signals.
`overall_confidence_decoupled = exp_conf` (lit is informational). Each claim is
classified into a 2D quadrant:

|              | high exp (>= 0.62)        | low exp           |
|--------------|---------------------------|-------------------|
| **high lit** (>= 0.55) | confirmed_established | plausible_unproven |
| **low lit**            | novel_discovery       | speculative        |

The high-exp / low-lit quadrant ("novel_discovery") is where most genuinely new
REE substrate findings live -- the legacy regime under-rated them because their
literature support was thin by construction.

**What Phase 1 changes (no behavioral effect on promotion):**

- `evidence/experiments/scripts/build_experiment_indexes.py` writes three new
  fields per claim summary: `experimental_confidence_decoupled`,
  `literature_confidence_parallel`, `evidence_quadrant`. The legacy
  `overall_confidence` is unchanged.
- `scripts/generate_option_e_shadow.py` (run by `governance.sh` step 3b)
  produces `evidence/experiments/option_e_recommendations.md` -- the
  side-by-side report of what governance would recommend under the decoupled
  regime, including the discrepancy list, the implementation-cohort claims with
  zero experimental backing, and the novel-discovery quadrant.
- `explorer.html` shows a small quadrant badge alongside the confidence chip in
  claim inspector lists. Informational only.

**What is intentionally NOT changed in Phase 1:**

- `decision_criteria.v1.yaml` thresholds (`min_overall_confidence`).
- `promotion_demotion_recommendations.md` (still keyed off `overall_confidence`).
- Any claim's `status` in `docs/claims/claims.yaml`.
- The `low_overall_confidence` flag in `planning_criteria.v1.yaml`.

**Phase 2 is the discrepancy reckoning.** Work through
`option_e_recommendations.md` claim by claim: queue an experiment, adjust
status, or surface a new evidence class. When the discrepancy list is empty (or
the residue is explicitly accepted), Phase 3 cuts over: gates switch to
`exp_conf`; legacy fields kept for one cycle then removed.

**Methodology rule:** never propose tweaking the lit/exp blend coefficients --
the blend is the bug, not its weights. See
`memory/feedback_lit_exp_decoupled.md` for the full rationale and the failed
B-strict / B-softened / C-balanced staging variants in
`evidence/experiments/staging_aggregator_b/`.

## Claim-type evidence gating

Different `claim_type` values play different epistemic roles and have
different evidence needs. The shadow report (and eventually production gates)
applies one of three gating rules per claim:

| gating | claim_types | evidence rule |
|---|---|---|
| `standard` | `mechanism_hypothesis`, `design_decision`, `implementation`, `invariant` (emergent / grey_zone / unspecified) | exp_conf required for promotion. Discrepancy + impl_no_exp + low_exp + lit_only flags fire normally. |
| `substrate_coherence` | `architectural_commitment`, `invariant` + universal | Foundational design choices that ARE the substrate. Tested by the substrate's coherent operation, not isolated probes. Discrepancy / impl_no_exp / low_exp / lit_only flags suppressed; surfaced separately for transparency. |
| `answer_state` | `open_question` | Question, not assertion. Evidence is "we reached an operating answer." Exempt from exp_conf gating until restated as a hypothesis. Same flags suppressed. |

The mapping is applied in `scripts/generate_option_e_shadow.py` via
`_evidence_gating(meta)`. Sub-type matters: `invariant_type: universal` is
gated as `substrate_coherence`; emergent / grey_zone invariants use standard
gating because they have substrate-level subject matter that can be probed.

**Why this matters:** without claim-type-aware gating, the shadow report
(and any cutover to decoupled production) would falsely flag every ARC and
universal invariant as "implementation cohort with no experimental backing"
-- but ARCs by definition can't be tested in isolation; they ARE the
substrate. Likewise every Q-claim would be flagged as needing experimental
backing for its "answer," which is a category error: a question becomes a
hypothesis (re-classified as MECH/SD) before standard gating applies.

**To restate a Q-claim as a testable hypothesis:** create a new MECH or SD
that operationalises the answer; mark the original Q-claim
`status: superseded` with a reference to the new claim. Don't change
`claim_type` in place -- the Q-claim's history is informative.

## Invariant Types

See `docs/architecture/invariant_types.md` for the full schema and governance rule.

Every `claim_type: invariant` entry must carry `invariant_type: universal | emergent | grey_zone`.
Emergent invariants additionally carry `emergent_from: [SD-.., ARC-..]` listing substrate designs
that give the invariant its subject matter.

**Governance rule:** when a substrate in some invariant's `emergent_from` drops below `active`
status, the invariant gets `pending_substrate_reconfirmation: true`. This does not demote the
invariant — it marks that the claim cannot be cited as supporting evidence for new claims until
governance explicitly reconfirms or reclassifies it. Universal invariants are never flagged.

`scripts/validate_claims.py` enforces the schema. `governance.sh` runs it in `--strict` mode
as a gate at the top of the pipeline — a malformed invariant blocks the entire run. The
defence-in-depth call inside `build_claims_json.py` remains warn-only so site rebuilds that
bypass governance.sh still surface drift without blocking.

The validator also emits flag-drift WARNs comparing `pending_substrate_reconfirmation` against
current substrate status (stale flag when all substrates active; missing flag when any
substrate below active). These are informational — the flag is a governance artifact, not an
auto-derived value. The substrate-change summary in
`evidence/experiments/promotion_demotion_recommendations.md` lists every substrate with
dependent emergent invariants after each governance run.

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

## evidence_direction: Per-Experiment Default with Optional Per-Claim Overrides

The indexer applies a single `evidence_direction` (supports/weakens/mixed) to all claims tagged
in a multi-claim experiment unless overridden. For experiments where different claims have distinct
pass/fail outcomes, use `evidence_direction_per_claim` (see below). Without it, a single FAIL
outcome incorrectly marks all tagged claims as "weakens" even if only some criteria failed.

**Canonical example of the failure mode (2026-03-22):** EXQ-023 tested SD-008, SD-003, MECH-098,
ARC-016 together. SD-008's criterion (event_selectivity_margin=0.084) **passed**. But SD-007 R²
and SD-003 calibration failed, making the overall outcome FAIL and marking SD-008 as "weakens" —
incorrect.

**Fallback workaround (for older manifests without per-claim field):** Correct the manifest
`evidence_direction` field directly and add an `evidence_direction_note` explaining the correction.
Rebuild the index after. This is a manual process — the pipeline does not detect these errors.

**Superseded experiments:** When a lettered iteration (EXQ-047j) corrects a bug that invalidated the predecessor's evidence (EXQ-047i), set `evidence_direction: "superseded"` on the old manifest and add an `evidence_direction_note`. The indexer records these entries in the full log but marks them `scoring_excluded: "superseded"` and excludes them from confidence and conflict scoring. See REE_Working/CLAUDE.md "EXQ Versioning and Supersession Policy" for the full workflow.

**Per-claim direction overrides (MANDATORY for multi-claim experiments, enforced 2026-04-01):**
Manifests with `len(claim_ids_tested) > 1` MUST include an `evidence_direction_per_claim` field —
a JSON object mapping each claim ID to its specific direction string:
```json
"evidence_direction_per_claim": {
  "ARC-024": "supports",
  "ARC-026": "weakens"
}
```
The indexer applies the per-claim override for each claim in `claim_ids_tested`; claims not listed
fall back to the run-level `evidence_direction`. Without per-claim overrides, a single FAIL outcome
incorrectly marks ALL tagged claims as "weakens" even if only some criteria failed.

**Enforcement:** Both `sync_v3_results.py` and `build_experiment_indexes.py` emit a WARNING when
a multi-claim evidence experiment lacks `evidence_direction_per_claim`. The queue-experiment skill
requires scripts to output this field when `len(claim_ids) > 1`. The `evidence_direction` field
must still be set to a reasonable overall summary value (the per-claim field supplements it).

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
