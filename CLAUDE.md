# REE_assembly

**Orientation:** [docs/START_HERE_HOW_REE_DEVELOPS.md](docs/START_HERE_HOW_REE_DEVELOPS.md) -- claim/experiment/evidence/governance loop, key files, Explorer-first path. Agents at umbrella root: [NEW_AGENT_START_HERE.md](../NEW_AGENT_START_HERE.md).

**Mobile / remote access:** [docs/mobile_access.md](docs/mobile_access.md) is the sanitized public overview. Concrete endpoints, WireGuard addresses, public keys, SSH user/host aliases, and phone setup notes belong only in the gitignored local runbook `docs/mobile_access.local.md`. Helpers: `scripts/wg_add_peer.sh`, `scripts/wg_enable_forwarding.sh`, `scripts/claude_mobile.sh`. `serve.py --bind` can restrict the explorer to WireGuard + localhost.

## Git Workflow

Push directly to `master`: `git push origin HEAD:master`

Do NOT create feature branches or pull requests.

## Multi-Session Coordination

See `REE_Working/CLAUDE.md` for the session startup protocol.
Check `REE_Working/WORKSPACE_STATE.md` before editing `docs/claims/claims.yaml`.

## Public Information Architecture

Before `/update-docs` or any other user-facing documentation landing, read
[`docs/design/public_information_architecture.md`](docs/design/public_information_architecture.md).
Treat it as a required impact review: determine whether the change affects the
reader's current orientation, a public status/count, a source route, a generated
visualization, or the public evidence export. Record the answer in the session
completion note.

The review includes the documentation system itself: inspect the `/update-docs`
routine plus the affected generators or configuration sources, including
`docs/apply_nav_frontmatter.py`, `scripts/build_site_visualizations.py`, and
`scripts/export_public_explorer.py`. Claim and update a system when needed; if
it is deliberately deferred, name the owner, reason, and next review point in
the completion note.

The public explorer is a redaction-reviewed publication artifact, not a normal
derived index. An agent may run its export and safety checks when the design
record calls for a freshness review, but must not publish regenerated public
explorer data until the established redaction review is complete. Never expose
future tests, queue details, or unreviewed run identities to solve a freshness
problem.

**Editing anything under `evidence/` — or `docs/claims/claims.yaml` — requires an active TASK_CLAIMS entry.** The runner heartbeat (`ree-v3/runner_remote_control.py:push_heartbeat`) does `git pull --rebase --autostash` against this repo every minute under `--remote-control`. With no active claim listed in `REE_Working/TASK_CLAIMS.json`, the autostash interaction can silently revert uncommitted edits across multiple ticks. Three incidents to date: (1) 5 EXQ-232 ARC-026 supersession edits to `evidence/experiments/` made 2026-04-29 reverted by 2026-05-01 with no trace in git history; (2) `evidence/planning/substrate_queue.json` MECH-204 design_doc field edit made 2026-05-08 ~18:25Z silently reverted with the same signature; (3) 2026-06-14 IGW window — an autostash cycle transiently swept a session's (ABM-1/Q-060) uncommitted `docs/claims/claims.yaml` edits out of the working tree (briefly showing it clean) then restored them a tick later (no data lost that time, same shape as the others). The heartbeat now skips its push entirely when an active claim covers ANY path under `evidence/` or `docs/claims/` (originally just `evidence/experiments/`; broadened to the `evidence/` prefix on 2026-05-08 after the planning incident; broadened again 2026-06-14 to add `docs/claims/` since claims.yaml is the most-contended governance file and lives outside the `evidence/` prefix). Register the claim *before* opening any evidence or claims.yaml file for editing, and either commit or close the claim before walking away — uncommitted edits left without an open claim remain vulnerable.

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

**Derive-only gotcha — a claims.yaml-direct STATUS change needs a manual reconcile in the same pass.**
This applies to ANY session that edits `claims.yaml` status / `v3_pending` directly — `/governance`,
`/failure-autopsy`, `/implement-substrate`, `/claim-synthesis`, `/thought-digestion`, OR an ad-hoc
ratification/demotion session — not just `/governance`. The governance pipeline is **derive-only**: it
regenerates derived files from `claims.yaml` / `decision_log.v1.jsonl` / plan-doc frontmatter but
**never edits a hand-authored source**, so a status change applied directly in `claims.yaml` (e.g. a
promotion + `v3_pending: false`) does NOT propagate to two places, and **no later `/governance` run will
sweep them**:
1. **The owning closure-plan node's `phase`/`status`/`resume_condition` prose** (`evidence/planning/*_plan.md`
   frontmatter). `closure_status.md` is derived FROM it, but the frontmatter itself is hand-kept. Update it
   by hand + regenerate the snapshot/drift. NOTE: bumping the node's `last_updated` resets the
   `stale_since_review` clock AND a legitimately-`partial` node with a PASS owner is Case-3-suppressed, so
   `check_closure_drift.py` will NOT flag the stale prose for you.
2. **`decision_state.v1.json`** — derives from the append-only `decision_log.v1.jsonl`; a direct claims.yaml
   edit bypasses the log, so decision_state keeps echoing the last logged decision (e.g. a stale
   `hold_pending_v3_substrate` / `applied`). Reconcile via
   `evidence/experiments/scripts/record_decision.py --claim-id X --recommendation promote_to_provisional --decision-status applied ...`
   then rebuild the index.

(`promotion_demotion_recommendations.md` DOES reconcile — it recomputes from claims.yaml.) Do both in the
SAME pass as the claims.yaml edit. Incident 2026-06-14: MECH-341 ratified in claims.yaml only (commit
80f4fcf250); the GAP-B closure node + decision_state stayed stale across the next full `/governance` cycle.
Full detail in the `/governance` skill Step 4 ("Derive-only gotcha").

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
| `governance_rule` | EXPLICIT only -- a standing governance gate (welfare / release / legal / security / process policy), NOT a testable mechanism | promote/demote suppressed; `narrow_open_question` suppressed; conflict alerts may fire. Used for the SENT-* / GOV-* ethics-perimeter claims (paired with `claim_type: governance_rule`, which is outside `SUBSTRATE_CLAIM_TYPES` so it does not enter the substrate-status map). The right response is to advance the owning governance artifact, not to run an experiment. See `evidence/planning/ethics_perimeter_plan.md`. |

The resolver lives in `evidence/experiments/scripts/build_experiment_indexes.py`
as `_resolve_epistemic_category(claim_type, invariant_type, explicit_category)`.
The recommendation function `_recommendation_for_claim` reads the resolved
category and dispatches accordingly.

**Validation.** `scripts/validate_claims.py` validates explicit
`epistemic_category` values against the canonical set
`{standard, substrate_coherence, answer_state, substrate_ceiling,
substrate_conditional, derivational, out_of_domain, governance_rule}`.
**ELEVATED to ERROR 2026-06-22** (the stabilise-then-elevate window is done --
the field has carried explicit values warn-clean since 2026-05-02; gate
confirmed at 0 invalid WARNs before flipping). A typo'd explicit value now
blocks `governance.sh` (`validate_claims --strict`) instead of silently masking
the bad value behind the indexer's `_resolve_epistemic_category()` inference
fallback. Mirrors the `assembly_state`/`assembly_status` elevation (master
`df62e84575`) and the invariant-type ERROR posture. (`epistemic_stance` and the
`ceiling_decision`/`ceiling_routing_note` checks remain warn-only -- they are
not the subject of the stabilise-then-elevate note.)

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

## Epistemic stance: shown / believed / asked (derived view, 2026-06-11)

Beyond `status`, `claim_type`, and `epistemic_category`, every claim carries a
derived **`epistemic_stance`** in {`shown`, `believed`, `asked`} -- the
author-facing reading of where the claim sits. It is a VIEW computed by
`scripts/build_claims_json.py` over existing fields, NOT a hand-labelled axis:

| stance | derivation | meaning |
|---|---|---|
| `shown` | `experimental_confidence >= 0.62` (the candidate->provisional gate) | experimentally confirmed |
| `asked` | `epistemic_category in {answer_state, derivational, out_of_domain}` OR `claim_type in {open_question, question}` | a question, not an assertion |
| `believed` | the remainder (an assertion not yet experimentally shown) | committed-to but untested; the ideas-first tail |

`exp_conf` comes from `evidence/experiments/claim_evidence.v1.json` (run the
indexer first for an up-to-date split; an absent matrix just yields
`exp_conf=0` -> `believed` for untested assertions, the correct default).
`build_claims_json.py` prints the `shown=/believed=/asked=` tally and emits
`epistemic_stance` (+ `what_would_answer` when present) into `claims.json` for
the explorer.

**Optional override:** set `epistemic_stance: shown|believed|asked` on a claim
to override the derivation (same pattern as `epistemic_category`).
`scripts/validate_claims.py` warns on an invalid explicit value.

**`what_would_answer` (asked bucket):** an `asked` claim should carry a
`what_would_answer:` line -- the observation that would answer or falsify it.
This is the discipline that separates genuinely-new epistemic ground (you can
state the falsification condition even if you can't yet run it) from the merely
not-yet-operationalised. `validate_claims.py` emits a warn-only flag for any
asked-bucket claim missing it. Warn-only by design; it does not block the
strict governance gate.

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

**Degenerate (vacuous-criterion) runs (2026-06-11):** A run is *degenerate* when a discriminative metric is pinned at a constant — zero cross-arm/cross-seed variance, or floor-pinned on every step — so its criterion could never fire regardless of behaviour. The PASS/FAIL it produces is an artefact of the test design, not evidence about the claim. Canonical cases: V3-EXQ-514m (`C_WL=0.0` on a valence channel that was never written), V3-EXQ-642 (`z_block` identically 0 on an untrained encoder). Set `non_degenerate: false` (whole run) or `non_degenerate_per_claim: {"MECH-229": false}` (one claim only) on the manifest, with a `degeneracy_reason` string. The indexer keeps the entry in the full log but marks it `scoring_excluded: "degenerate"` and drops it from confidence/conflict scoring — exactly parallel to `superseded`/`stale_substrate`. Only an explicit `false` excludes; absent/true is a no-op, so the legacy record is untouched. **Producer side:** new experiments self-report via `ree-v3/experiments/_experiment_lib.check_degeneracy()` at measurement time (it computes the flag and writes the manifest fields); a `/failure-autopsy` may also set the field by hand. This is the automatic catch-net for the vacuous-criterion failure mode that previously required a manual autopsy to reclassify `non_contributory`.

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

## Closure-plan node status: `assembling` (anti-forcing keystone, 2026-06-21)

Closure-plan nodes (`evidence/planning/*_plan.md` frontmatter) may carry
`status: assembling` (alias `open_by_design`): **required for v3 but actively /
intentionally under construction — substrate being built, not a stalled gap.**
It exists so the machinery has a penalty-free, low-maintenance way to say "this
is being assembled, leave it alone" instead of biasing every node toward closure.

Semantics (enforced in `serve.py:CLOSURE_STATUS_WEIGHTS` +
`scripts/generate_closure_snapshot.py` + `scripts/check_closure_drift.py`):

- **Excluded from the closure % (weight `None`)** — never punishes the
  green-board for correct, unhurried assembly. Surfaced on a separate
  **assembly-frontier** axis, NOT folded into `deferred` or `remaining`.
- **Restful in drift** — never flagged drifted/stale, needs no recurring
  re-stamp. Listed in the drift report's "Assembly frontier" section for
  visibility only.
- **Opt-in resume trigger** — `revisit_after: YYYY-MM-DD`; once past, the node
  is flagged `revisit_due` for review. No date == rests indefinitely.

Companion fields: `awaiting:` (the substrate being built) and `assembly_status:`
(`queued`/`in_progress`/`built`). Full diagnosis, the 3 remaining moves
(assembly-chip path, re-derive brake, portfolio view), and rollout guidance
(first migration candidate: `commitment_closure:GAP-8`) are in
`evidence/planning/assembly_vs_closure_plan.md`.

## Claim-level `assembly_state` (claims-layer consolidation, 2026-06-22)

The closure-NODE `assembling` state above has a CLAIMS-layer companion. The 6
scattered "this claim is waiting on substrate still being assembled" conventions
in `claims.yaml` (`epistemic_category: substrate_conditional` / `substrate_ceiling`,
`v3_pending`, `implementation_phase>=v4`, `implementation_phase=v3`, the
`pending_*` booleans) are consolidated into ONE canonical, machine-readable,
**derived** field **`assembly_state`** whose values PRESERVE each distinction
(they are NOT synonyms):

| `assembly_state` | derived from | maturity bucket |
|---|---|---|
| `mature` | status active/stable/provisional, not gated | mature |
| `enriching` | `substrate_ceiling` (V3-tractable, substrate too coarse → enrich) | awaiting_construction |
| `awaiting_substrate` | `substrate_conditional` (planned upstream unbuilt) | awaiting / mid (by `assembly_status`) |
| `gated_v3` | `v3_pending` or `implementation_phase=v3` | awaiting_construction |
| `deferred_future` | `implementation_phase` v4/v5/v6 | excluded (parked out of v3) |
| `remaining` | open assertion, not assembly-blocked | remaining |
| `parked` | legacy/superseded/retired/applied | excluded |
| `blocked` | blocked / upstream_blocked / blocked_pending_substrate | genuinely_blocked |

**Derive-first / additive.** The canonical resolver is
`scripts/build_claims_json.py:resolve_assembly_state` (emits `assembly_state`
into `claims.json`), kept in sync with `serve.py:_resolve_claim_assembly_state`.
It computes from the existing conventions — NO bulk hand-edits, and it changes
NO governance dispatch (`build_experiment_indexes.py` still gates on
`epistemic_category`/`v3_pending`; `_load_claim_registry` only ACCEPTS the new
fields). Three OPTIONAL explicit companion fields mirror MOVE-1 and override the
derivation: `awaiting:` (upstream `sd_id`/claim id — auto-joined from
`substrate_queue.json:unblocks_claims` when absent), `assembly_status:`
(`queued`/`in_progress`/`built` — auto-joined), `revisit_after:` (ISO date).
`scripts/validate_claims.py` validates the companion fields. The
`assembly_state` + `assembly_status` enums are **ERROR-level** (elevated from
warn-only 2026-06-22, after the one-cycle backwards-compat window: governance
cycle `c2aeb4823f` 2026-06-22T05:19Z ran with the field present and exercised it
at zero assembly WARNs) — a typo'd explicit value blocks `governance.sh`
(`validate_claims --strict`) instead of silently masking the bad value behind the
derivation. `revisit_after` (date format) stays **warn-only** (a bad date is
ignored by the revisit-due check, not substituted) and `awaiting:` is a free-form
upstream pointer with no enum check. This mirrors the `epistemic_category`
elevation posture ("Elevate to ERROR once the field stabilises across the
registry").

**Portfolio view.** `serve.py:_claims_assembly_view` draws the same maturity
buckets MOVE-4 draws over closure nodes over the WHOLE registry, exposed on
`/api/closure` as `claims_assembly` and surfaced via the **nodes ↔ claims
toggle** on `closure.html`'s "Assembly maturity" strip. See
`evidence/planning/assembly_vs_closure_plan.md` "Open follow-ons".

## V3-Pending Gate

Claims with `v3_pending: true` or `implementation_phase: v3` in claims.yaml get
`hold_pending_v3_substrate` recommendations — do not promote until V3 evidence arrives.
