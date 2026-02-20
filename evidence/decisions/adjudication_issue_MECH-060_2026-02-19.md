# Adjudication Issue Brief: MECH-060 (2026-02-19)

Generated: `2026-02-19`

## What Mechanism Is Being Decided

`MECH-060` is the **pre-commit vs post-commit dual-error-channel mechanism**.

In architecture terms (`docs/architecture/agency_responsibility_flow.md#mech-060`):
- Pre-commit error (`sim_error`) is for search/gating only.
- Post-commit error (`realized_error`) is for durable attribution and durable learning.

Why this exists:
- REE needs to distinguish rehearsal mistakes from real committed outcomes.
- If pre-commit channels can write durable state, responsibility attribution is corrupted.
- This mechanism is part of agency/responsibility flow (`ARC-015`) and is paired with:
  - `MECH-061` (commit-boundary tokenization)
  - `MECH-062` (tri-loop commit arbitration)
  - write-locus enforcement in `MECH-067`.

## How It Functions In The Architecture

At runtime, the intended flow is:
1. Simulate options before commitment.
2. Use pre-commit error only to rank/gate options.
3. Cross commit boundary with a commit token/provenance tag.
4. Observe realized outcome after commitment.
5. Apply post-commit error to durable stores (policy, ledger, residue, attribution).

Failure signatures for this mechanism are exactly about boundary failure:
- `mech060:precommit_channel_contamination`
- `mech060:postcommit_channel_contamination`
- `mech060:attribution_reliability_break`
- `mech060:commitment_reversal_spike`

## Why This Is A Governance Decision

The unresolved question is not just "promote/hold status."  
It is whether this mechanism should remain REE-native, be constrained/hybridized, or be replaced/retired as an architectural primitive.

Open governance checkpoint:
- `architecture_structure_adjudication` is `HUMAN_ONLY` with decision required (`evidence/planning/GOVERNANCE_AGENDA.md:26`).

## Metric Glossary (Human-Readable)

`conflict_ratio`
- Meaning: How split support vs weakening evidence is.
- Formula: `2 * min(supports, weakens) / (supports + weakens)`.
- Interpretation: `0` means one-directional evidence; `1` means perfectly split conflict.
- Source: `evidence/experiments/scripts/build_experiment_indexes.py:837`.

`overall_confidence`
- Meaning: Combined confidence that weights experiment and literature confidence.
- Built from consistency, volume, recency, and quality of evidence.
- Source: `evidence/experiments/scripts/build_experiment_indexes.py:847`.

`lit_non_support_ratio`
- Meaning: fraction of literature evidence that is not supportive (`weakens + mixed`).
- Source: `evidence/experiments/scripts/build_experiment_indexes.py:2146`.

`delta_lit_minus_exp`
- Meaning: `literature_confidence - experimental_confidence`.
- Positive value: literature currently supports claim more strongly than experiments do.
- Source: `evidence/experiments/scripts/build_experiment_indexes.py:2176`.

`recurring_failure_signatures`
- Meaning: repeated failure tags across runs (counts aggregated from run `failure_signatures`).
- Source: `evidence/experiments/scripts/build_experiment_indexes.py:2101`.

`stale_ratio` (epoch applicability)
- Meaning: fraction of evidence entries outside current architecture epoch applicability.
- Source: `evidence/planning/architecture_epoch_applicability.v1.json:8`.

`conflict_types` in `conflicts.md`
- `directional`: both supports and weakens exist.
- `source_disagreement`: experimental majority disagrees with literature majority.
- `mixed_evidence`: mixed-direction entries present.
- Source: `evidence/experiments/scripts/build_experiment_indexes.py:1741`.

## Reference Glossary (What The Evidence Labels Mean)

`commit_dual_error_channels`
- Direct mechanism experiment family for MECH-060.

`claim_probe_mech_060`
- Probe suite that tests claim-level behavior under controlled toggles.

Run IDs like:
- `2026-02-17T225337Z_commit-dual-error-channels_seed151_pre_post_split_streams_toyenv_internal_minimal`

Mean (left to right):
- timestamp, experiment type, seed, condition, environment/profile.

`PASS` / `FAIL`
- Determined by manifest status and stop-criteria checks.
- Source: `evidence/experiments/INTERFACE_CONTRACT.md:123`.

## Current Issue State (MECH-060)

Core evidence pressure:
- Structure recommendation: `escalate_architecture_decision`.
- Conflict ratio in structure queue: `0.875`.
- Top recurring signatures: postcommit contamination `52`, attribution break `50`, commitment reversal spike `38`.
- Sources: `evidence/planning/ARCHITECTURE_GAP_REGISTER.md:9`, `evidence/planning/ARCHITECTURE_GAP_REGISTER.md:40`.

Mechanism-level signal:
- Split-channel condition tends to support.
- Single-error-stream condition tends to weaken in paired probes.
- Source examples: `evidence/planning/structure_review/2026-02-19/MECH-060/DOSSIER.md:47`, `evidence/planning/structure_review/2026-02-19/MECH-060/DOSSIER.md:48`.

Escalation threshold check (all exceeded):
- configured minimums: conflict `0.78`, exp entries `24`, max signature count `8`, recurring signatures `2`.
- current: conflict `0.875`, exp entries `135`, max signature count `52`, recurring signatures `5`.
- Sources: `evidence/planning/planning_criteria.v1.yaml:17`, `evidence/planning/structure_review/2026-02-19/MECH-060/dossier.v1.json:221`.

## Why Some Numbers Differ Across Files

You are seeing multiple valid windows/snapshots:
- `conflicts.md` uses **epoch-applicable conflict scope filtering** for conflict reporting.
- architecture gap/structure review uses the broader architecture-pressure aggregation path.
- anti-lock-in dispatch (`2026-02-15`) is an older snapshot.

That is why values like `0.788`, `0.875`, and `0.944` can all appear without being a data bug.
Sources: `evidence/experiments/scripts/build_experiment_indexes.py:1652`, `evidence/experiments/scripts/build_experiment_indexes.py:2064`.

## Decision History Mismatch You Need To Resolve

Two governance streams diverged:
- Model adjudication stream applied `hybridize` for `MECH-060`.
  - `evidence/decisions/decision_log.v1.jsonl:17`
  - reflected in claim registry: `docs/claims/claims.yaml:1594`
- Promotion/conflict stream later applied `hold_candidate_resolve_conflict`.
  - `evidence/decisions/decision_log.v1.jsonl:48`
  - `evidence/decisions/decision_state.v1.json:111`

So the practical issue is: reaffirm `hybridize`, or choose a different architecture outcome now.

## Decision To Make Now

Pick one architecture adjudication outcome for `MECH-060`:

1. `retain_ree`
2. `hybridize`
3. `adopt_jepa_structure`
4. `retire_ree_claim`

Operational meaning:
- `retain_ree`: keep current REE mechanism framing.
- `hybridize`: keep mechanism core but enforce additional guardrails/interface separation.
- `adopt_jepa_structure`: move to JEPA-structured replacement path (can trigger dependency cascade/reopen).
- `retire_ree_claim`: deprecate this claim (also a cascade-trigger outcome).

Allowed outcomes and cascade policy are defined in planning criteria:
- `evidence/planning/planning_criteria.v1.yaml:32`

## After Decision (Sync Step)

1. Append decision via `python3 evidence/experiments/scripts/record_decision.py ...`.
2. Rebuild indexes/governance artifacts.
3. Confirm consistency across:
   - `docs/claims/claims.yaml`
   - `evidence/decisions/decision_state.v1.json`
   - `evidence/planning/ARCHITECTURE_GAP_REGISTER.md`
   - `evidence/planning/structure_review/latest/ACTIVE_INDEX.md`
