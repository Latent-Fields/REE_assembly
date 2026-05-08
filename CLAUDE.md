# REE_assembly

## Git Workflow

Push directly to `master`: `git push origin HEAD:master`

Do NOT create feature branches or pull requests.

## Multi-Session Coordination

See `REE_Working/CLAUDE.md` for the session startup protocol.
Check `REE_Working/WORKSPACE_STATE.md` before editing `docs/claims/claims.yaml`.

**Editing anything under `evidence/` requires an active TASK_CLAIMS entry.** The runner heartbeat (`ree-v3/runner_remote_control.py:push_heartbeat`) does `git pull --rebase --autostash` against this repo every minute under `--remote-control`. With no active claim listed in `REE_Working/TASK_CLAIMS.json`, the autostash interaction can silently revert uncommitted edits across multiple ticks. Two confirmed incidents to date: (1) 5 EXQ-232 ARC-026 supersession edits to `evidence/experiments/` made 2026-04-29 reverted by 2026-05-01 with no trace in git history; (2) `evidence/planning/substrate_queue.json` MECH-204 design_doc field edit made 2026-05-08 ~18:25Z silently reverted with the same signature. The heartbeat now skips its push entirely when an active claim covers ANY path under `evidence/` (originally just `evidence/experiments/`; broadened to the `evidence/` prefix on 2026-05-08 after the planning incident, since the autostash mechanism is not specific to experiments/). Register the claim *before* opening any evidence file for editing, and either commit or close the claim before walking away — uncommitted edits left without an open claim remain vulnerable.

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

## Lit/Exp Decoupling (Option E) -- Phase 3 Cutover Done 2026-05-01

The governance pipeline finished its three-phase transition for how literature
and experimental evidence combine into claim confidence.

**Current regime (Phase 3, authoritative):** lit and exp are separate signals.
Promotion / demotion gates read `experimental_confidence` directly. Each claim
is classified into a 2D quadrant:

|              | high exp (>= 0.62)        | low exp           |
|--------------|---------------------------|-------------------|
| **high lit** (>= 0.55) | confirmed_established | plausible_unproven |
| **low lit**            | novel_discovery       | speculative        |

The high-exp / low-lit quadrant ("novel_discovery") is where most genuinely new
REE substrate findings live -- the legacy blend under-rated them because their
literature support was thin by construction.

**What Phase 3 changes:**

- `evidence/experiments/decision_criteria.v1.yaml` thresholds renamed:
  `min_overall_confidence` -> `min_exp_conf`, `max_overall_confidence` ->
  `max_exp_conf`. The indexer accepts the legacy names too as a one-cycle
  backwards-compat fallback (helper `_t(d, new_key, legacy_key, default)` in
  `_decision_for_claim`).
- `evidence/planning/planning_criteria.v1.yaml`: retired
  `low_overall_confidence: 0.55`; replaced with `low_exp_conf: 0.55` and
  `lit_only_above_cap: 0.50`.
- Indexer gate logic now reads `claim_meta["experimental_confidence"]` instead
  of `overall_confidence`. The legacy `overall_confidence` field is still
  emitted on each claim summary so the explorer + transitional consumers can
  read it; remove after one stable cycle.
- Promotion / demotion rationale strings now report
  `exp_conf=…, lit_conf=…, overall_confidence_legacy=…` (the legacy value is
  kept for the audit trail).
- Planning evidence reasons: replaced `low_overall_confidence` flag with
  `low_exp_conf` + `lit_only_above_cap`. The legacy flag string is kept in
  the priority-marker set as a no-op alias for one cycle.

**What is preserved:**

- `evidence_quadrant` field per claim (added in Phase 1, still emitted).
- `scripts/generate_option_e_shadow.py` and its sibling
  `option_e_recommendations.md` report (now matches production -- kept as a
  cross-check that gating is internally consistent).
- `overall_confidence` field on every claim summary for one cycle.
- Claim-type evidence gating (substrate_coherence / answer_state / standard) --
  see next section.

**Phase history:**
- **Phase 1 (2026-04-29):** shadow-only -- added decoupled fields and a
  sibling recommendations report. No production behavior changed.
- **Phase 2 (2026-04-29 .. 2026-05-01):** discrepancy reckoning -- the
  shadow report exposed 15 implementation-cohort claims with zero
  experimental backing. Categorised them along existing claim_type lines:
  6 substrate_coherence (correctly suppressed), 5 answer_state (correctly
  exempt), 4 standard-gating that needed experiments. All 4 standard-gating
  claims (MECH-094, SD-017, SD-035, MECH-062) had discriminative-pair
  experiments queued and PASSed; all are now `confirmed_established`.
- **Phase 3 (2026-05-01):** cutover landed. Production gates now drive on
  `experimental_confidence`. Diff against the pre-cutover snapshot:
  +2 actionable demotion recommendations surfaced (MECH-095, MECH-102 --
  both `mechanism_hypothesis` whose lit_conf was masking insufficient
  exp_conf under the legacy blend), 0 prior recommendations lost.

**Methodology rule:** never propose tweaking the lit/exp blend coefficients --
the blend was the bug, not its weights. See
`memory/feedback_lit_exp_decoupled.md` for the full rationale and the failed
B-strict / B-softened / C-balanced staging variants in
`evidence/experiments/staging_aggregator_b/`.

## Epistemic categories (Phase 3 wave 2, 2026-05-02)

Beyond `claim_type`, claims carry an **`epistemic_category`** field that
governs which evidence rule applies. The field is OPTIONAL on `claims.yaml`
entries; when absent the indexer infers from `claim_type` + `invariant_type`
using the Phase 2 mapping. When set explicitly, the explicit value
overrides inference (lets us tag a `mechanism_hypothesis` as
`substrate_ceiling` or a specific `open_question` as `derivational`).

Resolved values + dispatch:

| epistemic_category | inferred from / set explicitly when | dispatch in indexer |
|---|---|---|
| `standard` | claim_type in {mechanism_hypothesis, design_decision, implementation, emergent/grey_zone invariant}, OR explicit `standard` on a Q-claim that is V3-tractable | exp_conf required for promotion. Discrepancy / impl_no_exp / low_exp / lit_only flags fire normally. |
| `substrate_coherence` | architectural_commitment, OR invariant + invariant_type=universal | Foundational design choices that ARE the substrate. promote/demote suppressed; conflict-resolution alerts still fire. |
| `answer_state` | open_question (default) | Question, not assertion. Exempt from exp_conf gating. `narrow_open_question` recommendation fires when `total_entries >= 2 AND conflict_ratio < 0.35`. |
| `substrate_ceiling` | EXPLICIT only -- claim is V3-tractable in principle but the substrate is too coarse to deliver the needed distinctions | promote/demote suppressed; conflict alerts fire; `narrow_open_question` does NOT fire (not appropriate). The right response is substrate enrichment, not more experiments on the existing substrate. |
| `substrate_conditional` | EXPLICIT only -- claim depends on upstream substrate that is planned but not yet built | promote/demote suppressed; same flags as substrate_ceiling. The right response is to wait for the upstream substrate. |
| `derivational` | EXPLICIT only -- the question is answered by working through axioms / formal proof, not by experiment | promote/demote suppressed; `narrow_open_question` suppressed. The right response is to convert to a derivation artifact (or close as resolved-by-derivation). |
| `out_of_domain` | EXPLICIT only -- the question is empirical but its test domain is outside REE (clinical cohort, pharmacology, etc.); no substrate at any level helps | promote/demote suppressed; `narrow_open_question` suppressed. These claims may belong as `research_anchor` or `literature_synthesis` claim_type rather than `open_question`. |

The resolver lives in `evidence/experiments/scripts/build_experiment_indexes.py`
as `_resolve_epistemic_category(claim_type, invariant_type, explicit_category)`.
The recommendation function `_recommendation_for_claim` reads the resolved
category and dispatches accordingly.

**Validation.** `scripts/validate_claims.py` warn-only-validates explicit
`epistemic_category` values against the canonical set
`{standard, substrate_coherence, answer_state, substrate_ceiling,
substrate_conditional, derivational, out_of_domain}`. Invalid values
fall back to inference (do not crash the indexer). Elevate to ERROR
once the field stabilises across the registry.

**Why this matters.** Without category-aware gating, the production
recommendation queue collapses 5+ genuinely distinct epistemic situations
into either `narrow_open_question` (for Q-claims) or `demote_to_candidate`
(for MECH/SD with mixed evidence). Both are misleading for sub-categories
that need different next-step responses. The Phase 3 wave 2 walk
(2026-05-02, MECH-095 + MECH-102 + Q-025..Q-039 cohort) exposed the
collapse and the schema makes the distinction machine-readable.

**To restate a claim as testable:** create a new MECH or SD that
operationalises the answer; mark the original `status: superseded` with
a reference to the new claim. Don't change `claim_type` in place -- the
original's history is informative.

See `docs/architecture/substrate_roadmap.md` for the V3 enrichment work
that would unblock `substrate_ceiling` claims, and `docs/architecture/
v4_spec.md` for the V4 substrate that addresses the V4-bound sub-cohort.

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
